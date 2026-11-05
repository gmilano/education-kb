---
industry: education
region: Global
updated: 2026-11-05
---

# 🧩 Composition patterns — Education

> Concrete recipes. Every component named below was verified on 2026-11-04, and the nine components cited by 🆕 **P38** were re-verified on 2026-11-05 at p669 (`git ls-remote --symref`, real default ref on all nine) (existence + licence payload + stars where shown) and appears in `agents/top.md`, `repos/foundations.md` or `verticals/solutions.md`.
> **The licence rule that governs all `38` patterns below — re-derived by counting the `## P` headings at p669, after the header had read *“all five patterns”* since the file held five:** keep proprietary work in the agent layer (MIT/Apache) and in Apache-2.0 XBlocks. Never fork a GPL/AGPL platform for a managed service.

## Base architecture

```
[LMS / SIS — stock, unmodified: Moodle GPL-3.0 | Open edX AGPL-3.0 | Canvas SaaS]
        │  REST / MCP  (process boundary = licence boundary)
        ▼
[MCP server layer — MIT]
   canvas-mcp (317★)  ·  Moodle REST adapter  ·  SIS adapter
        ▼
[Orchestration — LangGraph (MIT)]
        ▼
[Agents — MIT / Apache-2.0]
   DeepTutor (Apache-2.0, 55k★)   — 1:1 lifelong tutoring
   OpenMAIC  (MIT, 42.7k★)        — multi-agent classroom
   OATutor   (MIT, 276★)          — BKT mastery tutoring
   Instructional Agents (MIT, 490★) — course material generation
   Bloom     (MIT, 302★)          — adaptive lesson sequencing
   AI-Shifu  (Apache-2.0, 331★)   — course authoring from expert intent
   GenMentor (CC0-1.0, 136★)      — goal-oriented session planning
        ▼
[Mastery + retention — pyKT (MIT, 457★) / BKT  ·  fsrs-rs (BSD-3, 456★) scheduling]
        ▼
[Delivery — Kolibri (MIT, offline-first) · Richie portal (MIT) · WhatsApp · avatar (Open TutorAI CE, BSD-3) · LMS-native]
```

---

## P1 — Canvas agent pilot (fastest credible pilot: 3–4 weeks)
**Best fit:** North America HE, any Canvas client. **Licence exposure:** none — the LMS is the client's SaaS.

| Component | Repo | Licence |
|---|---|---|
| LMS bridge | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT |
| Tutor | [Li-Evan/Bloom](https://github.com/Li-Evan/Bloom) | MIT |
| Orchestration | LangGraph | MIT |

**Wiring:**
1. Deploy `canvas-mcp` against the client's Canvas instance with a scoped API token — read-only on enrolments and assignments for the pilot. Its ~102–128 tools cover courses, assignments, submissions and grades.
2. Run Bloom as the learner-facing agent. It already works as a Claude Code skill, so the first demo needs no web build at all.
3. Point Bloom's context at `canvas-mcp` tools so lessons reference the student's *actual* upcoming assignments.
4. Instrument from day one (see P5) — Canvas pilots are judged on measured outcomes.

**Why it wins:** no platform migration, no licence question, and a working demo inside a week. This is the pattern to lead with when a client says "we already have an LMS".

---

## P2 — Moodle + out-of-tree tutor (LATAM public sector, EMEA K-12: 6–8 weeks)
**Best fit:** the Moodle installed base — dominant in LATAM and much of EMEA.
**Licence exposure:** none, if you respect the process boundary.

| Component | Repo | Licence |
|---|---|---|
| LMS | [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 — **stock** |
| Tutor | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 |
| Local inference | Ollama | MIT |
| Portal (optional) | [openfun/richie](https://github.com/openfun/richie) | MIT |

**Wiring:**
1. Leave Moodle **unmodified**. Enable Moodle Web Services and mint a scoped service token.
2. Stand up DeepTutor as a separate service. Its persistent learner model is the whole point — give it durable storage, not an ephemeral container.
3. Build a thin REST adapter (yours, MIT) that pulls course structure, activity logs and grades from Moodle into DeepTutor's student model.
4. For EMEA/LATAM data residency, back DeepTutor with local models via Ollama so learner data never leaves the jurisdiction.
5. Surface the tutor through Moodle's AI placements, or through a Richie (MIT) portal when the client wants their own branded front end.

**The licence reasoning:** a separate process talking to Moodle over REST is not a derivative work of Moodle. A Moodle plugin containing your tutor logic *would* be, and would owe GPL-3.0 on distribution. Keep the boundary at the network call.

---

## P3 — Open edX + XBlock, licence-contained (corporate academies, national platforms: 8–10 weeks)
**Best fit:** MOOC-scale and corporate L&D. **This is the only licence-safe shape for Open edX.**

| Component | Repo | Licence |
|---|---|---|
| Platform | [openedx/edx-platform](https://github.com/openedx/edx-platform) | **AGPL-3.0** — **stock** |
| Component SDK | [openedx/XBlock](https://github.com/openedx/XBlock) | **Apache-2.0** ← your code lives here |
| Classroom agent | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | MIT |
| Content generation | [DaRL-GenAI/instructional_agents](https://github.com/DaRL-GenAI/instructional_agents) | MIT |

**Wiring:**
1. Deploy Open edX **unmodified**. This is not a style preference: modifying an AGPL-3.0 platform and operating it as a service obliges you to offer modified source to its users.
2. Write an XBlock (Apache-2.0) as the in-course surface. The XBlock is a thin client — it renders and relays, holding no business logic.
3. Run OpenMAIC outside the platform as the lesson engine. Its LangGraph orchestration and AI-classmate simulation are what the XBlock embeds.
4. Use `instructional_agents` offline to generate the course scaffold (syllabus → LaTeX slides → assessments) before the cohort starts, cutting designer time on the critical path.
5. Keep all proprietary work in the XBlock and the external services. The AGPL obligation never attaches.

**Delivery note:** step 1 is the whole pattern. Teams that "just patch one thing" in the platform create a disclosure obligation that is extremely hard to unwind later.

---

## P4 — Mastery-based adaptive sequencing (STEM, K-12: 8–12 weeks)
**Best fit:** clients who want explainable mastery estimates, not free-form chat.

| Component | Repo | Licence |
|---|---|---|
| ITS + BKT | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT |
| KT models | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | MIT |
| LMS link | LTI (OATutor native) / canvas-mcp | MIT |

**Wiring:**
1. Deploy OATutor and connect it to the LMS over **LTI** — native, standards-based, no custom bridge.
2. Author or port problem sets with scaffolded hints into OATutor's content format. **This is the real cost of the pattern** — budget content work, not just engineering.
3. Train pyKT models on the client's historical interaction data to initialise mastery priors, instead of starting every learner from a cold BKT prior.
4. Expose mastery estimates to teachers as a dashboard. Explainability is the selling point here; do not hide the model behind a chat box.

**Honest scoping:** pyKT is a 457-star research library and OATutor is 276 stars. Both are solid and peer-reviewed, neither is a turnkey product. Promise explainable mastery modelling as an *engineering build*, not a component drop-in.

---

## P5 — Governance and measurement wrapper (sell this first, especially in LATAM)
**Best fit:** every region; the strongest standalone offer in LATAM and EMEA.
**Why first:** >50% of teachers in Chile and Brazil use AI while <10% of institutions have guidelines. The client's missing piece is control, not capability.

**Not a single repo — a layer wrapped around P1–P4:**

1. **Policy enforcement at the MCP boundary.** Every tool call from an agent to an LMS passes through the MCP server. That is the natural place for allow/deny rules, PII redaction and per-jurisdiction policy nodes. Implement it there, once, rather than inside each agent.
2. **Per-region policy nodes in the LangGraph graph.** Regulation has diverged (EMEA horizontal and dated; US state patchwork; India labelling from 20 Feb 2026; LATAM pending). Branch on jurisdiction in the graph:
   - **EMEA:** no emotion recognition (banned since Feb 2025); Article 50 AI-disclosure on every learner-facing surface (live since 2 Aug 2026); admissions/assessment/placement flagged high-risk ahead of **2 Dec 2027**.
   - **India:** synthetic-content labelling on generated material (from 20 Feb 2026).
   - **North America:** teacher-in-the-loop on anything touching instruction (Idaho SB 1227 bars AI replacing teachers); district policy artefacts (Ohio, Maryland).
3. **Audit log of every agent action against student data** — this is the specific thing the Bridges 2026 survey says leaders are withholding access over. Shipping it unblocks the rest of the engagement.
4. **Measurement harness, attached before launch:** pre/post assessment, 30-day retention, teacher hours saved. The July 2026 scoping review of 474 studies found the field's evidence fragmented; a pilot that cannot demonstrate an effect will not renew.

**Deliverables:** institutional AI policy, the technical controls that enforce it, the audit trail, and the measurement report. Spanish and Portuguese for LATAM. Repeatable across peer institutions with little rework — which is what makes it a product rather than a project.

---

## P6 — Retention engine: mastery + scheduling behind one MCP surface (4–6 weeks)
**Best fit:** any client whose pilot has to show a measured outcome — which, per `intel/trends.md` **T10**, is now most of them.
**Licence exposure:** none. Every component is MIT or BSD-3-Clause.

| Component | Repo | Licence |
|---|---|---|
| Mastery + scheduling tool surface | [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT (96★) |
| Scheduling engine | [open-spaced-repetition/fsrs-rs](https://github.com/open-spaced-repetition/fsrs-rs) | **BSD-3-Clause** (456★) |
| Reference scheduler + optimiser | [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | MIT (4.1k★) |
| Knowledge-tracing models | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | MIT (457★) |
| LMS reach | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) or a Moodle REST adapter | MIT |

**Wiring:**
1. Deploy `tutor-mcp` as the single tool surface. It already packages Bayesian Knowledge Tracing, FSRS spaced repetition, prerequisite skill graphs and a frozen scoring rubric — do not rebuild these.
2. Link `fsrs-rs` for the scheduling computation. It is the embeddable engine (bindings for C, Python, Node.js, Dart and PHP in sibling repos), and **the computation is local**: no model call, no per-review token cost. Use `fsrs4anki`'s optimiser as the reference for fitting parameters per learner from their own review history.
3. Train or initialise pyKT models on the client's historical interaction data so mastery priors are not cold.
4. Pull the review-eligible item set from the LMS over `canvas-mcp` or a Moodle REST adapter, and write completion back.
5. Report **retention at 30 and 90 days** as the headline metric, not engagement.

**Why this is the pattern to attach to every other one:** FSRS ships inside Anki from v23.10, so this is validated at consumer scale rather than research-grade — unusual on this shelf. It is permissive end to end, it computes on-device or server-side with no inference cost, and retention is the outcome institutions actually measure. It is the cheapest credible answer to "show me it worked".

**Honest scoping:** FSRS schedules *review of known items*. It does not teach, and it needs an item bank with stable identities. If the client has no item bank, that is the first deliverable, and it is content work.

---

## P7 — Offline-first, permissive all the way down (6–8 weeks)
**Best fit:** Sub-Saharan Africa, rural South Asia, Pacific islands, and any deployment where connectivity cannot be assumed.
**Licence exposure:** none — and uniquely on this page, **not even at the platform layer**.

| Component | Repo | Licence |
|---|---|---|
| Learning platform | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** (1.2k★) |
| Local inference | Ollama | MIT |
| Review scheduling | [open-spaced-repetition/fsrs-rs](https://github.com/open-spaced-repetition/fsrs-rs) | **BSD-3-Clause** |
| Tutor (optional, when a device can run it) | [Li-Evan/Bloom](https://github.com/Li-Evan/Bloom) | MIT |

**Wiring:**
1. Deploy Kolibri on a classroom server or directly on devices. ⚠️ **Resolve the branch first** — the default is `develop`; the release lines are `release-v0.19.x` and `release-v0.20.x`. Deploy from a release line, not from `develop`.
2. Run a small local model via Ollama on the classroom server. Learner data never leaves the premises, which is a connectivity answer *and* a trust answer — it is the posture African edtech builders have independently converged on.
3. Compute review scheduling with `fsrs-rs` on the device. This is the part that genuinely requires no network: no model call per review.
4. Sync to a central instance opportunistically, when connectivity appears. Design every workflow to be correct if the sync never happens.
5. Keep the proprietary layer in the Kolibri derivative itself — **MIT permits this**, which no other platform on this shelf does.

**Why it is strategically distinct:** every other pattern here keeps a stock copyleft platform and puts the IP in an out-of-tree agent layer. This is the one pattern where Globant can ship a closed product end to end, platform included. For a regional offering sold repeatedly across markets, that difference compounds.

**Honest scoping:** Kolibri is not an institutional LMS. There is no Moodle-class gradebook, no enrolment-at-scale, no large third-party plugin ecosystem. If the client needs institutional course management, this is the wrong base and **P2** is the right one.

---

## P8 — Moodle agent pilot, adopt-and-harden (LATAM public sector, EMEA K-12: 5–7 weeks)
**Best fit:** the ~60% of this KB's addressable market that runs Moodle — LATAM public education, EMEA K-12, Spanish- and Portuguese-speaking institutions.
**Licence exposure:** none in your code. The agent bridge is MIT and talks to Moodle over REST, so nothing you write becomes a GPL derivative.
**This is P1's twin for the other LMS, and it costs more. Price it that way.**

| Component | Repo | Licence | Role |
|---|---|---|---|
| Moodle agent bridge | [G36maid/moodle-mcp](https://github.com/G36maid/moodle-mcp) | MIT (1,064 B), **27★** | 22 tools over Moodle Web Services: courses, assignments (read + submit), forums, files-as-markdown, grades, schedule, messaging, quiz attempts, plus `call_ws_function` as the escape hatch. Rust, `rmcp`. States validation against Moodle 3.7 → 5.x |
| Permission model to copy | [GhaithAlHallak8/moodler-mcp](https://github.com/GhaithAlHallak8/moodler-mcp) | MIT (1,072 B), 4★ | Do not deploy it — **borrow its defaults**: writes and teacher grading off behind explicit env flags, token from browser SSO stored locally |
| Tutor | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 (55k★) | Persistent learner model. Self-host with local models for residency |
| Mastery + scheduling | [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT (96★) | BKT + FSRS behind one tool surface — attach **P6** |
| Local inference | Ollama / vLLM | MIT / Apache-2.0 | Keeps learner data in-jurisdiction |

**Wiring:**
1. Stand up stock, unmodified Moodle. Enable Web Services and mint a dedicated service account with the **narrowest** capability set that the tool list needs — not an admin token.
2. Deploy `moodle-mcp` **out-of-tree**, in its own process. Pin the commit, not a branch. ⚠️ **Clone `G36maid/moodle-mcp`, not `thc1006/moodle-mcp`** — the latter ranks higher in search, is a fork, and is 43 commits behind.
3. **Harden before piloting, and bill for it.** This is the step that distinguishes P8 from P1: at 27★ the bridge has no meaningful external review. Audit token handling and storage; set writes to off-by-default behind explicit flags (`moodler-mcp`'s model); constrain or disable `call_ws_function`, which by design reaches *any* Moodle web service and is the broadest privilege in the stack; run your own integration tests against the client's actual Moodle version rather than trusting the 3.7 → 5.x claim; add rate limiting.
4. Point DeepTutor at the bridge. Attach `tutor-mcp` for mastery and review scheduling (**P6**).
5. Contribute the hardening upstream. It is cheap, it removes the single-maintainer risk from the client's position, and it is the honest basis for recommending a 27★ dependency at all.
6. Wrap in **P5** governance before anything student-facing goes live.

**Honest scoping — say all three of these out loud in the proposal:**
- **The Moodle agent layer is ~12× less reviewed than the Canvas one** (27★ against `canvas-mcp`'s 317★). That asymmetry is structural, not temporary. **P8 is genuinely more expensive than P1 and the difference is the hardening step**, not margin.
- **Six of the eight permissive Moodle servers measured have ≤4 stars.** There is no mature alternative to fall back to. If `G36maid/moodle-mcp` proves unsuitable after audit, the next step is a build, so run the audit in week one, not week four.
- **Do not reach for `csmediapro/moodle-mcp-server`** as the "more commercial-looking" option. It is **AGPL-3.0** with paid Premium Plugins, and an AGPL network-served agent defeats the entire out-of-tree containment that makes this pattern licence-safe.

---

## P9 — Sovereign, curriculum-grounded tutoring on education open weights (8–10 weeks)
**Best fit:** EMEA public education under data-residency constraints; Sub-Saharan African and other offline-first deployments; **and any Korean or Vietnamese client that needs an agent demonstrably off the system of record** (`intel/trends.md` **T15**).
**Licence exposure:** 🔴 **one unresolved gate — read it before scoping, not before delivery.**

| Component | Repo / artefact | Licence | Role |
|---|---|---|---|
| Curriculum-grounded model | [haolpku/Omni-Edu](https://github.com/haolpku/Omni-Edu) — OmniEdu-9B-FP8 (~11.09 GiB) or 27B-FP8 (~28.30 GiB) | **Apache-2.0 code; weight licence NOT NAMED** ⚠️ | K-12 subject competence, curriculum grounding, diagnostic reasoning, pedagogical scaffolding — in the weights rather than the prompt |
| Model toolkit + evaluation | `omniedu` (PyPI, same repo) | Apache-2.0 | Unified interface, OpenAI-compatible serving, image inputs, JSONL batch inference, 12-benchmark eval suite |
| Serving | vLLM / Ollama | Apache-2.0 / MIT | Single-GPU FP8 serving, no egress |
| Delivery platform | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** (1.2k★, branch `develop`) | Offline-first content delivery, learner progress, coach tooling |
| Review scheduling | [open-spaced-repetition/fsrs-rs](https://github.com/open-spaced-repetition/fsrs-rs) | **BSD-3-Clause** (456★) | On-device scheduling, zero inference cost |
| Mastery estimation | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | MIT (457★) | Knowledge tracing priors |

**Wiring:**
1. 🔴 **Gate zero, before any engineering: read the OmniEdu weight licence on its Hugging Face card** (`lhpku20010120/Omni-Edu-9B` / `-27B`, and the `-FP8` variants). The repository's Apache-2.0 grant covers the **code**; the README says only that *"Model weights and third-party datasets and benchmarks retain their respective licenses"*, the backbones are Qwen, and `huggingface.co` did not resolve in the session that verified this pattern. **If the weight terms are not commercially usable, this pattern collapses to P7 with a general model** — so resolve it in the first conversation, not the first sprint.
2. Serve the FP8 checkpoint on a single GPU via vLLM. FP8 is the whole point: 37–44% smaller than BF16, which is what moves this from a research artefact to a deployable one.
3. Evaluate on the client's own curriculum with the `omniedu` suite **before** committing to the model. The published results are self-reported (27B: K12-Bench 63.12 EM / 76.69 F1, MathFish 85.89, EDUMATH MaC 86.95, MathTutorBench Scaffold 78.74) and — in the authors' own words — *"Benchmark performance does not establish classroom learning gains."* Take them at that value.
4. Deliver through Kolibri for offline-first, or through the client's LMS via **P8** / **P1** where there is connectivity.
5. Add `fsrs-rs` for review scheduling and pyKT for mastery priors — both compute locally, so the offline story stays intact.
6. **For Korea and Vietnam specifically:** keep the agent off the system of record and document that boundary as a deliverable. Vietnam's high-risk trigger bites only where results are *the official basis* for assessing or ranking learners; Korea names student assessment in its high-impact definition. A formative-only architecture with evidence is a materially smaller compliance programme than conformity work on a graded system.

**Why this pattern exists:** it is the first on this page where the *model* knows the curriculum rather than the prompt carrying it. That matters most exactly where general hosted models are hardest to use — in-jurisdiction, offline, or kept deliberately away from graded decisions. One artefact answers the binding constraint in three regions.

**Honest scoping:** the weight-licence gate is real and unresolved; a K-12 model trained on a Chinese-authored corpus needs curriculum-alignment evaluation per market before anyone claims grounding; and at 590★ / 9 commits this is a young repository with concentrated maintainer risk.

---

## P10 — AI-literacy delivery against a funded mandate (6–8 weeks per cohort)
**Best fit:** the mandate wave this KB tracks — **Canada's** National AI Literacy Initiative (one million entry-level post-secondary students, 3,000+ educators), **Saudi Arabia's** mandatory undergraduate AI literacy, **EU AI Act Article 4**, **Kenya's** strategy commitment with no framework yet written, **Idaho's** AI-literacy standards, the **UAE's** all-levels programmes.
**Licence exposure:** none. Every component is MIT.
**This is the one pattern on this page whose deliverable is curriculum and teacher capacity rather than software** — and it is the pattern that fits the largest publicly-funded commitments in this KB.

| Component | Repo | Licence | Role |
|---|---|---|---|
| Curriculum base | [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) | **MIT** (41.1k★, 6.6k forks) | 93+ runnable projects on LLMs, RAG, agents and MCP, tiered beginner (22) / intermediate (48) / advanced (23), plus an `ai-engineering-roadmap`. MIT ⇒ a commercial, closed, client-branded derivative is permitted |
| Delivery vehicle | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | MIT (42.7k★) ⚠️ see gate | Multi-agent classroom with AI teachers *and* AI peers. **12 locales across 11 languages including Portuguese (Brazil), Spanish (Mexico), Arabic, Vietnamese, French, German** — the broadest localisation on this shelf |
| Platform | client's Moodle / Canvas / Open edX via **P8** / **P1** / **P3** | — | Enrolment, completion, credentialing |
| Retention | **P6** (`tutor-mcp`, `fsrs-rs`) | MIT / BSD-3-Clause | Literacy that is assessed once is forgotten; schedule the review |
| Measurement | **P5** governance + evaluation wrapper | — | The funder will ask what changed |

**Wiring:**
1. Fork `ai-engineering-hub` and cut the tiers down to the mandate's actual scope. A ministry asking for AI literacy for first-year undergraduates needs the 22 beginner projects, not all 93. Resist shipping the whole hub.
2. ⚠️ **Licence gate on OpenMAIC before it enters a deliverable.** The repository is MIT, but `packages/mathml2omml` is **LGPL-3.0-or-later** (7,652 B payload; `"license": "LGPL-3.0-or-later"` in its own `package.json`), it is declared `"workspace:*"` in the root manifest, and `build:packages` compiles it as **step one**. A built deliverable links it. Either keep that component dynamically replaceable with its source offered — LGPL permits this and it is an architecture decision, not a blocker — or excise the MathML-to-OOXML path if the client does not need Word/PowerPoint export. Decide at design time; retrofitting replaceability into a bundled JS build is expensive. Note also that OpenMAIC has only been MIT since **v0.3.0 (2026-06-28)** and the prior licence is not named in the repository, so pre-June history has no answer for a diligence question.
3. Localise with OpenMAIC's existing locales rather than translating a course. pt-BR and es-MX are already there, which covers the LATAM mandates; Arabic covers the Gulf.
4. Run cohorts through the client's own LMS (**P8** for Moodle, **P1** for Canvas) so completion lands in the system of record and credentialing works.
5. Attach **P6** so literacy is retained and **P5** so the funder gets outcome evidence rather than attendance.

**Why this is commercially distinct:** the AI-literacy mandates are *funded* and *dated*, and they cannot be satisfied by a tutoring agent — a client cannot buy curriculum from a chatbot. `ai-engineering-hub` at 41.1k★ is the most-adopted permissive asset of its kind, and the licence is the whole reason it is here: the nearest alternative, `GarethManning/education-agent-skills` (949★), is **CC BY-SA 4.0**, whose ShareAlike term forces any derivative skill library to be CC BY-SA and so rules out a closed client deliverable. Same category, opposite answer, and the permissive option is 43× more adopted.

**Honest scoping:** `ai-engineering-hub` is *AI-engineering* material for developers — it is the right base for undergraduate, vocational and educator-upskilling cohorts, and the **wrong** base for K-12 AI literacy, which this KB has no permissive curriculum for and which remains an open gap. Contextualising and pedagogically sequencing the content is the real work; the repository is raw material, not a course.

---

## P11 — Permissive institutional LMS, closed deliverable (greenfield HE, EMEA public sector: 10–12 weeks) 🟢 new at p653

**The only pattern in this file where the institutional platform itself permits a closed derivative.** Use it when the client is *choosing* a platform rather than extending one — a new faculty, a national programme, a public-sector training body, a migration off a commercial LMS.

```
OpenOlat  (Apache-2.0, 449★/32,210 commits, branch OpenOLAT_21.1)
  ├── PostgreSQL JDBC 42.7.14 (BSD-2-Clause)   ← NOT MySQL Connector/J: see below
  ├── langchain4j 1.23.0 (Apache-2.0, already in pom.xml)
  │     ├── langchain4j-open-ai     ──► Ollama or vLLM on in-jurisdiction hardware
  │     │                                (OpenAI-compatible wire protocol: config, not code)
  │     ├── langchain4j-anthropic   ──► hosted fallback where egress is permitted
  │     └── langchain4j-embeddings  ──► embeddings computed in-process
  ├── Apache Lucene (Apache-2.0, already in pom.xml) ← semantic course search, no egress
  └── fsrs-rs (BSD-3-Clause) via JNI/sidecar  ← review scheduling
```

**Week 1–2** — stand up OpenOlat from `OpenOLAT_21.1` (never from `master`; see the branch section). Specify **PostgreSQL** in the architecture document and say why in one line.
**Week 3–5** — wire `langchain4j-open-ai` to a client-hosted Ollama or vLLM endpoint. No new dependency, no fork. Prove the no-egress claim with a network capture, not a diagram.
**Week 6–8** — course-content semantic search over Lucene + `langchain4j-embeddings`; this is the demo that lands with faculty.
**Week 9–12** — mastery and scheduling: `fsrs-rs` as a sidecar, exposed through the **P6** MCP surface so the tutor and the LMS share one retention model.

🔴 **The one licence decision that makes or breaks the closed deliverable.** Of 270 declared dependencies, exactly one is copyleft: **MySQL Connector/J (GPL-2.0 + Universal FOSS Exception)**. The exception covers combination with OSI-approved open source licences — it does **not** cover a closed proprietary derivative, which is the whole reason for choosing this platform. PostgreSQL JDBC (BSD-2-Clause) is already in the tree and a first-class backend. **Specify PostgreSQL and the tree is permissive end to end.** Verified absent from the tree: iText (AGPL-3.0) and JasperReports (LGPL), the two usual Java-LMS killers; Hibernate is 7.4.14 and hibernate-validator 9.1.6, both Apache-2.0 eras.

⚠ **Price the skill-set, not the licence.** Java/Spring/Hibernate is heavier than PHP-Moodle or Python-Open edX, there is no plugin marketplace of Moodle's scale, and the contributor base is concentrated around one vendor (frentix GmbH). P11 buys a licence position and a residency story. It does not buy a cheaper build, and a proposal that implies otherwise will be wrong by week 6.

## P12 — The OpenOlat agent bridge: build the thing that does not exist (6–8 weeks) 🟢 new at p653

**The cleanest greenfield position in this KB.** The LMS-bridge picture across the three platforms this base tracks is **Canvas 317★ → Moodle 27★ → OpenOlat 0**: `openolat-mcp`, `frentix/openolat-mcp` and `OpenOLAT/openolat-mcp` were all probed at p653 and **none resolves.**

Why this is a better build than it looks, on three counts that do not usually co-occur:

1. **No incumbent to displace.** Unlike Moodle (seven MIT servers competing at ≤27★, where the work is hardening someone else's code — see **P8**), there is nothing to fork and no upstream to negotiate with.
2. **No copyleft to route around.** Patterns A, B and C all exist to keep proprietary work *outside* a platform that cannot absorb it. OpenOlat is Apache-2.0, so **the agent can live in-tree, in the same Maven build**, and the deliverable can still be closed.
3. **The LLM layer is already there.** `langchain4j` with OpenAI, Anthropic and embeddings modules is in `pom.xml` today, so the bridge does not need to ship a model client.

```
Weeks 1–2   Read OpenOlat's REST surface + the langchain4j wiring already in-tree.
            Borrow the permission model from GhaithAlHallak8/moodler-mcp (MIT):
            browser SSO → locally-stored token; writes and grading OFF by default
            behind explicit env flags. It is the safest default posture this KB
            has measured in any LMS bridge — copy it rather than re-deriving it.
Weeks 3–5   MCP server over the official SDK. Tool surface modelled on
            G36maid/moodle-mcp (MIT, 22 tools: identity, courses, assignments
            read+submit, forums, files-as-markdown, grades, schedule, messaging)
            — a proven taxonomy, re-implemented against OpenOlat's API.
Weeks 6–8   Attach a tutor: zijinz456/OpenTutor (MIT, 166★) for local-first, or
            Bloom (MIT) for the fastest demo. Gate every write behind the
            WAITING_REVIEW shape from littlecookie0722/AI-Teaching-Agent.
```

🟢 **Contribute it upstream under Apache-2.0 and the strategic return exceeds the engagement fee.** This is the one place in this KB where Globant could own the reference integration for an entire platform rather than the third fork of someone else's.

## P13 — Assessment: adopt-and-harden a research decomposition (10–14 weeks) 🟢 new at p653

**The one pattern here where the production artefact does not exist yet and Globant would create it.** Four passes established that there is no adopted permissive education assessment tool; p653 established that there is permissive, education-specific, peer-reviewed *research* supply. That changes the engagement from "build a grader" to "productise a published decomposition", which is scopeable.

```
ArguLens / wwrwbs/AI_AWE  (Apache-2.0 by reference, arXiv:2608.17356)
  ├── discourse-move classifier
  ├── grade-independent LightGBM scorer over 31 linguistic/discourse features
  └── label-aware feedback generator        ← the part clients actually want
        │
        ├── calibration layer  ◄── microsoft/LLM-Rubric (MIT, 45★)
        │      calibrate rubric outputs against THIS client's human raters
        │
        └── human-approval gate ◄── littlecookie0722/AI-Teaching-Agent (MIT)
               WAITING_REVIEW state + Docker-sandboxed evaluation + no auto-publish
```

**Why these three and not one.** ArguLens supplies the education-specific decomposition and, unusually, *grade-independent* features — which is what makes it portable to a curriculum it was not trained on. `LLM-Rubric` supplies the mechanism ArguLens lacks and that every institution demands: calibrating machine scores against the client's own markers, so the output is defensible in an appeals process. `AI-Teaching-Agent` supplies the review-state machine, and its shape — explicit approve/reject, sandboxed execution, **no automatic publishing** — is the shape an Annex III high-risk deployment needs anyway.

🔴 **Three constraints to put in the proposal, not discover in week 9.**
- **The training corpus does not come with it.** Persuade 2.0 is academic-use-only and is deliberately not redistributed. A commercial retrain needs the client's own marked scripts — which is a data-collection workstream, and often the longest one.
- **Bias is documented by the authors, not discovered by you.** ArguLens's own licence file carries the notice: AES systems inherit bias from training data (Persuade 2.0 is US middle-school argumentative essays), and it is *"intended for research and assistive use, not for high-stakes automated decisions without human oversight."* Quote that in the proposal. It is the authors' own framing and it is the correct one.
- **Adoption is zero.** 2★ / 2 commits and 0★ / 30 commits. These are artefacts, not projects: budget for reading papers and writing tests, and do not price it as integration.

⚠ **Scope it as assistive scoring with human sign-off, never as autonomous grading.** Under EU AI Act Annex III, evaluating learning outcomes is high-risk; Washington DC's 2026 policy bars AI from grading outright. The deliverable that is legal in both places is the one that scores and explains while a human decides.

## P14 — Corporate L&D as a closed, client-branded product (EMEA / North America enterprise: 8–10 weeks) 🟢 new at p655

**Buyer:** a corporate L&D or compliance function, not an academic institution. They expect *their* brand on the product and will not accept a licence conversation.

```
Selleo/mentingo (MIT, 106★, main)                 ← fork; MIT permits a closed, rebranded derivative
  ├── already in core, read from the manifest at p655:
  │     ai 7.0.148 + @ai-sdk/openai 4.0.8 + @ai-sdk/workflow 2.0.80   (Vercel AI SDK)
  │     langchain 0.3.34 · pgvector retrieval on PostgreSQL 16
  │     LiveKit  → real-time voice role-play, scored automatically
  │     Langfuse → per-interaction trace = the compliance audit trail
  │     multi-tenant + white-label + SCORM export + 6 UI languages
  ├── swap the model provider for Ollama (MIT) or vLLM (Apache-2.0) when the client requires on-prem
  └── jupyter/nbgrader (BSD-3-Clause) only if the curriculum is technical — otherwise the
        in-core scenario assessment engine is sufficient and already scored
```

**Weeks 1–2** fork, rebrand, stand up Postgres 16 + pgvector / Redis / S3-compatible storage in the client's region; **EU-only residency is a configuration choice here, not a paid tier**. **Weeks 3–5** harden: this is a 1,397-commit, 106★ codebase — budget the security review, the load profile (its own `perf:load`/`perf:stress`/`perf:soak` suites exist and should be run against the client's concurrency target) and multi-tenancy isolation testing explicitly. **Weeks 6–8** author the first compliance track against the scenario assessment engine; wire Langfuse traces into the client's evidence store. **Weeks 9–10** recertification and expiry rules, then pilot cohort.

**Why this is not Pattern F.** F is OpenOlat for institutional higher education — a different buyer, a longer cycle, and one that does not need rebranding. **Say the trade out loud in the proposal:** Moodle (GPL-3.0), Open edX (AGPL-3.0) and Canvas (AGPL-3.0) are mature and copyleft; Mentingo is MIT and young. You are buying licence freedom with hardening effort. Quantify the hardening rather than hiding it.

**Do not** present 106★ as adoption. Present it as what it is: the only MIT platform where multi-tenancy, white-labelling and the agent are all in core.

## P15 — Autograded technical curriculum, permissive end to end (bootcamps, CS faculties, data academies: 6–8 weeks) 🟢 new at p655

**Buyer:** anyone teaching code, data or quantitative methods at cohort scale — and this KB's **largest unserved segment until p655**, because it searched for education tools and this stack files itself as infrastructure.

```
JupyterHub (BSD-3-Clause, 8,362★, main)           ← one isolated, authenticated, resource-capped env per learner
  ├── LTI auth → the client's existing Moodle / Canvas / Open edX stays the front door
  │                (no migration, no copyleft contact: the LMS is a separate process)
  ├── Kubernetes spawner for cohort scale; Docker spawner for a pilot
  └── jupyter/nbgrader (BSD-3-Clause, 1,370★, main)
        release → collect → autograde → manual grade → feedback
        ├── deterministic per-cell tests score what is checkable      (no LLM, no hallucination surface)
        ├── microsoft/LLM-Rubric (MIT, 45★) scores what is not: prose, design rationale, code quality,
        │     calibrated against this client's own human raters       ← the calibration is the deliverable
        └── formgrader + gradebook → the human decision boundary, which several jurisdictions now require
              └── Ollama (MIT) or vLLM (Apache-2.0) inside the client network for the rubric model
```

**Weeks 1–2** JupyterHub on the client's Kubernetes, LTI into their existing LMS, environment images per course. **Weeks 3–4** nbgrader assignment structure; port one real existing assignment and reproduce its historical grades — **that reproduction is the credibility test, run it before anything else is promised.** **Weeks 5–6** LLM-Rubric for the non-deterministic dimensions, calibrated on a sample the client's own graders have already scored; report the agreement statistic honestly, including if it is poor. **Weeks 7–8** cohort pilot, grader training, appeals workflow.

**The licensing story is the simplest on this page: BSD-3-Clause, BSD-3-Clause, MIT, MIT — no copyleft anywhere, no AGPL network trap, closed derivative permitted throughout.** Only Pattern E (Kolibri offline) matches it, and E does not cover assessment.

🟢 **Amended at p657 — scope this against P19 before proposing it.** This pattern is correct for a *course-level* engagement where the client's LMS stays the front door and Jupyter is the work surface. It is **not** the right answer at faculty or institution scale, because p657 shelved four permissive production autograders this pattern predates: `Artemis` (MIT, 826 ★), `Autolab` (Apache-2.0, 808 ★), `Submitty` (BSD-3-Clause, 805 ★) and `otter-grader` (BSD-3-Clause, 162 ★). **Two concrete substitutions.** First, if the curriculum includes **R** — statistics, econometrics, quantitative methods — use `otter-grader` rather than `nbgrader`: same BSD-3-Clause licence, same assignment source, and it grades R, which `nbgrader` does not. Second, if the client needs submission handling, plagiarism workflow, TA assignment, regrade requests and an appeals trail, those are **built** in `Submitty` and would be months of bespoke work here. Choose P15 for one course or one cohort; choose **P19** for a faculty.

**State the boundary explicitly and in writing:** this grades submitted work; it does not establish **who** submitted it. **No permissively-licensed proctoring or assessment-integrity tool was found in five passes of searching** (see `repos/foundations.md`). If the client needs identity assurance, that is a commercial tool and a separate line item — do not imply this stack provides it.

## P16 — Retention that writes into a scheduler people already use (4–5 weeks) 🟢 new at p655

A narrower, faster sibling to **P6**, enabled by one row added at p655.

```
ankimcp/anki-mcp-server (MIT, 544★, main, v0.27.0 "active beta")
  └── exposes decks, notes, note types, cards, scheduling and review state over MCP
       ├── ArnaudGuiovanna/tutor-mcp (MIT, 96★) → mastery: BKT + prerequisite graph + frozen rubric
       ├── CAHLR/pyBKT (MIT, 291★, master)      → interpretable mastery estimates when a board must audit them
       └── the agent of choice (any MCP client) decides WHAT to schedule; FSRS decides WHEN
            └── FSRS already ships inside Anki from v23.10 — fsrs4anki (MIT) / fsrs-rs (BSD-3-Clause)
```

**Why this is worth a separate pattern.** Every other retention design in this KB reimplements scheduling. This one does not: the learner keeps the client they already have, the scheduler is the one with consumer-scale production proof, and the agent's job shrinks to *selection* — which is the part a tutor is actually good at. **4–5 weeks** because there is no platform to stand up: weeks 1–2 wire the two MCP servers behind one agent, week 3 define the card-generation and selection policy against real course material, weeks 4–5 run a cohort and measure retention against the client's existing baseline.

⚠️ `anki-mcp-server` self-describes as **active beta at v0.27.0**. Pin the version, read the changelog before upgrading, and do not put it on a critical path for a graded outcome without a fallback.

## P17 — The evidence spine: LTI in, xAPI out, nothing forked (4–6 weeks) 🟢 new at p656

Not a standalone engagement — the layer that goes **underneath** P1–P16 and makes any of them provable. Every pattern above eventually meets the same two questions: how does our thing appear inside the LMS the client already runs, and how do we show it worked. Ten rows added at p656 answer both, and all of them are permissive.

```
THE CLIENT'S EXISTING LMS  (Moodle GPL-3.0 / Canvas / Brightspace / Open edX AGPL-3.0 / OpenOlat Apache-2.0)
  │
  │  ── LTI 1.3 launch ──▶  no fork, no copyleft inherited: an LTI tool is a separate work
  │
  ├── tsugiproject/tsugi (Apache-2.0, 377★, master)        → PHP: LTI13, AGS, NRPS, Deep Linking, unit tests
  ├── dmitry-viskov/pylti1.3 (MIT, 138★, master)           → Python/Django/Flask  ⚠️ 2 yrs quiet, pin it
  └── jupyterhub/ltiauthenticator (BSD-3, 73★, main)       → launches JupyterHub (BSD-3) + nbgrader (BSD-3)
       │
       ▼
  THE AGENT LAYER  (yours, proprietary — MIT/Apache deps only)
       │   e.g. HKUDS/DeepTutor (Apache-2.0) · ArnaudGuiovanna/tutor-mcp (MIT) · CAHLR/pyBKT (MIT)
       │
       ├── content the client already owns:
       │     jcputney/scorm-again (MIT, 362★, 0 open issues) → plays SCORM 1.2/2004, AICC, cmi5
       │     ⚠️ authored in H5P (GPL-3.0) or Adapt (GPL-3.0)? call it, never fork it
       │
       ├── assessment:
       │     numbas/Numbas (Apache-2.0, 216★) → maths/quantitative, randomised, partial credit
       │     jupyter/nbgrader (BSD-3, 1,370★) → notebook autograding
       │
       ▼
  THE EVIDENCE SPINE  ◀── the deliverable that converts a pilot into a renewal
       RusticiSoftware/TinCanJS (Apache-2.0, 208★)  → emits xAPI statements from content
            ⚠️ 3 yrs quiet: vendor and audit it; the protocol is frozen so this is survivable
       adlnet/xAPI-Spec (Apache-2.0, 955★)          → the statement shapes to conform to
       yetanalytics/lrsql (Apache-2.0, 144★, main)  → 🔴 THE ONLY LIVE PERMISSIVE LRS
            runs on SQLite / PostgreSQL / MySQL · actor, verb, object, result, timestamp
            └── query it for: time-on-task, attempt counts, mastery trajectory, cohort deltas
```

**Why this is a pattern and not a footnote.** P5 has sold "governance and measurement" since early in this KB's life without naming a single component, and T10 and T19 have recorded for many passes that the evidence base is this sector's weakest point. The gap was never that the measurement substrate did not exist — `lrsql` has been verified in this repository's logs under the words *"el candidato de producción permisivo"* — it was that it had never reached a shelf. **An Apache-2.0 LRS is the difference between "the tutor seems to help" and a queryable statement log a client's own analysts can audit.**

**Timeline 4–6 weeks**, on top of an existing engagement: week 1 stand up `lrsql` against the client's database of record and agree the statement vocabulary (this is the only genuinely hard design step — a vague verb set makes the whole log unanalysable); weeks 2–3 wire the LTI launch so the tool appears inside their LMS with their roster and no second login; week 4 instrument the agent and the content to emit statements; weeks 5–6 build the cohort-delta queries and hand the client the dashboard **plus the SQL**, because a measurement they cannot re-run themselves will not survive a change of sponsor.

🔴 **Two risks to put in the proposal, not discover later.**
1. **`lrsql` is a single point of failure.** It is the only live, maintained, permissively-licensed LRS. `LearningLocker/learninglocker` (584★) is GPL-3.0 *and* dormant since 2024-05-30; `adlnet/ADL_LRS` is Apache-2.0 but ~12 months quiet. One Clojure project, nine open issues. If the client needs a supported LRS with a vendor SLA, that is a commercial product and this pattern does not apply.
2. **Four of the ten components are over a year quiet and none is archived**, so GitHub's staleness signal never fires. Read `pushed_at` before `stars` on this layer and pin every version.

**Where this does not apply.** A greenfield build with no incumbent LMS (use P11 or P15 and own the whole stack), and any engagement where the client's measurement requirement is a compliance artefact rather than an analytical one — a regulator wanting a transparency notice under EU AI Act Article 50 is not asking for an LRS.

## P18 — Adaptive assessment, permissive end to end (ministries, national platforms, professional certification: 10–14 weeks) 🟢 new at p657

**Buyer:** anyone who must place a learner on a scale defensibly — a ministry running a national diagnostic, a professional body certifying candidates, a university placing students into streams. **This is the pattern this KB has pointed at since P4 without being able to name the item-selection component.** Now it can.

```
the client's existing item bank (usually PDF/Word, sometimes QTI)
  └── bigdata-ustc/EduNLP (Apache-2.0, 64★)        ← parse items: text + formulae + figures → structured objects
        └── CALIBRATE item parameters (difficulty, discrimination)
              ├── eribean/girth (MIT, 127★)  or  17zuoye/pyirt (MIT, 111★)   ← 1PL/2PL/3PL + polytomous
              └── tswsxk/EduData (Apache-2.0, 83★)  ← public response data for COLD START, before the
                                                        client has any of its own  ⚠️ not the client's learners
        └── DIAGNOSE which skills are held
              └── bigdata-ustc/EduCDM (Apache-2.0, 203★)  ← IRT · MIRT · DINA · NeuralCD
                    └── CAHLR/pyBKT · pykt-team/pykt-toolkit  ← mastery over time (already shelved)
        └── SELECT the next item   ★ the load-bearing component ★
              └── douglasrizzo/catsim (BSD-3-Clause, 153★, branch `dev`, v0.9.1)
                    initialisation · item selection · ability estimation · stopping rule,
                    each pluggable, plus SIMULATION to test the design before any learner sees it
                    └── bigdata-ustc/EduCAT (MIT, 77★) only if the client wants the learned-policy comparison
  └── DELIVER:  ls1intum/Artemis (MIT) quiz exercises  or  numbas/Numbas (Apache-2.0) in-browser
  └── RECORD:   yetanalytics/lrsql (Apache-2.0) over xAPI  ← the audit trail, non-negotiable
```

**Weeks 1–3** parse and structure the real item bank; agree the skill model with the client's subject experts — *this is the deliverable that takes longest and it is not a technical task*. **Weeks 4–6** calibrate on whatever historical response data exists; if none, fit on `EduData` and state in writing that the parameters are provisional. **Weeks 7–9** `catsim` simulation: run synthetic cohorts against the calibrated bank and report test length, measurement error and exposure rates **before** anything is promised about shortening the test. **Weeks 10–12** pilot delivery with the full xAPI trail. **Weeks 13–14** recalibrate on the pilot's own responses — which is the point at which the parameters become real.

🟢 **Why this is defensible where an LLM-scored adaptive test is not.** Every step is a **published, inspectable, five-decade-old statistical method**. Under EU AI Act Annex III, Korea's high-impact scope and US state guardrails, "we selected item 14 because the maximum-information criterion at the current ability estimate chose it" is an answer; "the model decided" is not. **Explainability here is a property of the algorithm, not a feature to build.**

⚠️⚠️ **The two risks to price explicitly, because this pattern hides them better than any other on this page.** First, **six of the seven components are dormant** — `EduNLP` (2024-03), `EduData` (2023-05), `EduCDM` (2024-10), `EduCAT` (2024-08), `girth` (2022-09), `pyirt` (2023-08); only `catsim` is live (2026-11-01). The mathematics does not rot, but **the engagement is adopting maintenance responsibility for unmaintained code and must bill for it.** Second, **`catsim`'s default branch is `dev`** — clone `main` and you get nothing. Third, **calibration needs response volume**: below a few hundred responses per item the parameters are noise, and a proposal that promises adaptivity on a cold bank is promising something it cannot deliver in the pilot window.

## P19 — Autograded faculty at institution scale: adopt and harden, do not build (CS / engineering faculties, technical universities: 8–12 weeks) 🟢 new at p657

**Buyer:** a faculty or university that grades code, proofs, diagrams or quantitative work at cohort scale and is currently doing it with teaching assistants, spreadsheets and goodwill. **The premise of this pattern is that Globant writes no grader.**

```
PICK ONE PLATFORM — they are not interchangeable:

  ls1intum/Artemis (MIT, 826★, `develop`, v10.3.1) — TUM        ← choose when AI is wanted in-tree
    ├── programming · text · modeling (Apollon, MIT) · quiz · file upload
    ├── Atlas: competencies, learning paths, analytics
    ├── Iris (LLM tutor) · Athena (feedback SUGGESTION) · Hyperion (exercise authoring)
    │     ALL configuration-gated, OFF by default  ← the procurement feature, not a limitation
    └── ls1intum/Pyris (MIT) → point at the CLIENT's Ollama / vLLM endpoint, never a public API

  Submitty/Submitty (BSD-3-Clause, 805★/1,119 forks, `main`, v26.10.04) — RPI
    └── choose when the SUBMISSION and HUMAN-GRADING workflow is the hard part:
        TA assignment, regrade requests, appeals trail, plagiarism workflow — all built

  autolab/Autolab (Apache-2.0, 808★, `master`) — CMU
    └── choose for containerised programming autograding with a clean separation:
        autolab/Tango (Apache-2.0) is the sandboxed execution service and runs standalone

  + ucbds-infra/otter-grader (BSD-3-Clause, 162★) for the R half of the curriculum
  + jupyter/nbgrader (BSD-3-Clause) if the work surface is notebooks → see P15
```

**Weeks 1–2** deploy on the client's own infrastructure; **LTI into the incumbent LMS so it stays the front door** (Pattern I / P17 — no migration, no copyleft contact). **Weeks 3–5** migrate real existing exercises and **reproduce their historical grades — run this before anything else is promised**, exactly as P15 requires; it is the credibility test and it is cheap. **Weeks 6–8** enable at most one AI subsystem, for one cohort, and **calibrate `Athena`'s suggestions against the client's own graders, reporting the agreement statistic honestly including if it is poor.** **Weeks 9–10** appeals workflow and grader training. **Weeks 11–12** xAPI trail into `lrsql` and the governance pack: which subsystem was enabled, for whom, what it touched, where the human decided.

🟢 **What Globant is actually selling, and it is worth more than a grader.** Deployment, integration, exercise migration, calibration against the client's raters, the appeals and governance workflow, and grader training. ⚠️ **Say out loud in the proposal that the platform is existing open source** — a client who later discovers that a "custom platform" was MIT software from TUM has a legitimate grievance, and the honest version is the stronger pitch anyway: six universities already run this code.

⚠️ **The same hard boundary as P15, restated because it does not move:** this grades submitted work; it does not establish **who** submitted it. **No permissively-licensed proctoring or assessment-integrity tool has been found in any pass** (see **T20**). Identity assurance is a commercial tool and a separate line item.

## P20 — Spoken-language assessment, self-hosted (LATAM and APAC language programmes, corporate English training: 6–8 weeks) 🟢 new at p657

**Buyer:** a language school, a ministry's English programme, or a corporate training function currently paying per utterance to a cloud speech API — or doing nothing because that cost did not scale.

```
learner records a target sentence (phone or browser, no special hardware)
  └── Halleck45/OpenPronounce (MIT, 184★) — CPU-only, `pip install openpronounce`
        returns: score · mispronounced words with sounds ACTUALLY HEARD in IPA ·
                 per-word confidence · transcription · pitch + energy curves
        ├── Kyubyong/g2p (Apache-2.0, 936★)          ← English target pronunciation
        ├── CUNY-CL/wikipron (Apache-2.0, 376★)      ← Spanish · Portuguese · hundreds more
        └── liguozheng-ac/japanese-speech-xray (MIT, 177★) ← pitch-accent languages (JA, ZH)
  └── launch inside the client's LMS over LTI 1.3  (Pattern I / P17 — tsugi or pylti1.3)
  └── record every attempt to yetanalytics/lrsql (Apache-2.0) over xAPI
        → the cohort-level progress curve, which is what the buyer is actually paying for
```

**Weeks 1–2** stand up `OpenPronounce` in the client's estate and **score a sample of the client's own recordings against their own teachers' judgements — report the correlation before anything else happens.** **Weeks 3–4** target-language lexicon from `g2p` (English) or `wikipron` (everything else); set the scoring thresholds *with* teachers rather than for them. **Weeks 5–6** LTI launch from the existing LMS; xAPI statements into `lrsql`. **Weeks 7–8** pilot cohort and the progress reporting.

🟢 **The commercial case is a line item the client already pays.** `OpenPronounce` is positioned by its own author as a self-hosted alternative to **Azure Pronunciation Assessment**: a metered per-utterance cloud cost becomes a CPU container. And because **voice is biometric-adjacent personal data**, keeping it on-premise *removes* an EMEA cross-border transfer question rather than answering it — the compliance argument and the cost argument are the same deployment decision.

⚠️ **Three boundaries, all of which belong in the proposal in writing.** (1) **Phoneme accuracy is not fluency and not a CEFR level** — it does not replace a human oral examiner, and a proposal implying otherwise will fail its first expert review. (2) `OpenPronounce` is **184 ★ with a single maintainer**: pilot against real recordings before committing, and budget to carry it. (3) The better-known project in this layer, `Thiagohgl/ai-pronunciation-trainer` (525 ★), is 🔴 **AGPL-3.0** — usable as a deployed service, **never** as the client's product; if a client has already found it, that licence difference is the reason to choose `OpenPronounce` despite lower adoption.

## P21 — Verifiable skills credentials, closed derivative permitted (corporate academies, professional bodies, workforce programmes: 6–8 weeks) 🟢 new at p657

**Buyer:** anyone whose completions currently end in a PDF certificate — a corporate academy, a professional body, a government reskilling programme. **Skills-based credentialing is a named 2026 buying trend (1EdTech, see T34) and the permissive supply for it is one project (T33).**

```
learner completes assessed work
  └── the assessment itself: Artemis (MIT, P19) or the adaptive test from P18
        └── evidence recorded to yetanalytics/lrsql (Apache-2.0) over xAPI
              ← the credential must POINT AT evidence, or it is a PDF with extra steps
  └── learningeconomy/LearnCard (MIT, 70★, `main`)   ★ the only permissive issuer ★
        Issue · Earn · Store · Share · Map
        standards read from the monorepo's own package list this pass:
          @learncard/vc-plugin · vc-api-plugin        → W3C Verifiable Credentials, VC-API
          @learncard/openid4vc-plugin · sd-jwt-vc-plugin → OpenID4VC, SD-JWT-VC
          @learncard/didkit-plugin · didkey-plugin · did-web-plugin · chapi-plugin → DIDs, CHAPI
        └── ships its own AGENT SKILL: `npx @learncard/cli skill install`
              → an agent from agents/top.md can issue and verify directly
```

**Weeks 1–2** the **competency model** — which skills exist, what evidence counts, who may assert it. This is the deliverable and it is a facilitation task, not an engineering one; `Artemis`'s Atlas competencies or a 1EdTech CASE framework can carry it. **Weeks 3–4** `LearnCard` issuance wired to the assessment's completion events, each credential referencing its xAPI evidence. **Weeks 5–6** holder wallet and verification flow; decide `did:web` (institution-anchored, simplest to explain to a registrar) versus `did:key`. **Weeks 7–8** recognition — the part that determines whether the credential has value: at least one external party that will *accept* it.

🟢 **Licence position is unusually clean: MIT throughout**, so the client's branded wallet and issuer are a closed derivative. **Every alternative in the layer is copyleft** — `tahrir` AGPL-3.0, `certo` AGPL-3.0, `openbadgeslib` LGPL-3.0, `badgr-ui` AGPL-3.0 **and archived** (**T33**). If a client has already piloted a badge platform, the licence is very likely why it cannot become their product.

⚠️ **Two risks, and the second is the one that kills these projects.** (1) **`LearnCard` is 70 ★ with 42 open issues and one sponsoring organisation** — the same single-vendor shape **T28** flags for `lrsql`, and both appear in this stack, so a proposal resting on P21 is resting on two single-vendor dependencies. Name them. (2) **A credential nobody accepts is worth nothing.** Standards conformance (W3C VC, OBv3, OpenID4VC) is necessary and not sufficient; **the engagement must deliver at least one relying party that will honour the credential**, and if the client cannot name one, build the evidence layer (`lrsql`) first and the credential later.

## P22 — A national or district K-12 coding platform, MIT end to end (ministries, state education departments, large districts: 10–14 weeks) 🟢 new at p658

**Buyer:** a ministry, state education department or large district that wants its *own* branded coding environment — its curriculum, its language, its hardware, its data residency — and has been quoted a per-seat SaaS price for Code.org or a commercial equivalent. **The whole stack below is MIT, so the deliverable can be a closed, branded product.**

```
MakeCode core — microsoft/pxt (MIT, 1,105 B, `master`, 2,314★, pushed 2026-11-05)
  │   blocks ⇄ JavaScript ⇄ Python on ONE AST; compiles IN-BROWSER; runs offline
  ├── target: microsoft/pxt-microbit  (MIT, 1,143 B, `master`, 806★)   → micro:bit hardware
  ├── target: microsoft/pxt-arcade    (MIT, 1,162 B, `master`, 550★)   → game-based CS curriculum
  └── block layer underneath: RaspberryPiFoundation/blockly (Apache-2.0, `main`, 13,600★)
        ★ note the OWNER: transferred from Google 10 Nov 2025 (T36). Cite the new address. ★
  │
  ├── hardware lab, no egress: openblockcc/openblock-desktop (MIT, `main`, 302★)
  │     + microbit-foundation/micropython-microbit-v2 (MIT, `master`) for firmware
  │
  └── LMS boundary — process boundary = licence boundary (base architecture above)
        Moodle (GPL-3.0) or Open edX (AGPL-3.0), STOCK, reached over LTI 1.3 via
        Cvmcosta/ltijs (Apache-2.0, 11,361 B — see p646)
        └── evidence out: yetanalytics/lrsql (Apache-2.0) over xAPI  → P17 / P21
```

**Weeks 1–3** stand up `pxt` with one target and reskin it — this is configuration, not a fork, and the demo that wins the engagement is the client's own logo on a block editor compiling their curriculum's first lesson in a browser with the network off. **Weeks 4–7** curriculum encoding: the blocks the client's syllabus actually needs, authored as a MakeCode extension, plus localisation. **Weeks 8–10** hardware path, if any — micro:bit is the cheapest credible option and its firmware is MIT. **Weeks 11–14** LTI integration into the existing LMS and xAPI telemetry, so the ministry can answer "did it work?" (**T19**'s outcome gap).

🟢 **Licence position: MIT throughout the layer you modify**, Apache-2.0 one level down in Blockly. No copyleft anywhere in the build path, so a branded closed derivative is permitted. 🔴 **Do not reach for Code.org for this** even though it looks like the closer fit: its code is Apache-2.0 but its courseware is carved out and may not be embedded in another format, and its Minecraft assets need a separate agreement with Microsoft (**T39**). **Do not fork `scratch-gui`** — AGPL-3.0, and this is a hosted service (**T40**).

⚠️ **Risks.** (1) `pxt` is Microsoft-governed and single-vendor; it is MIT, so a fork is always available, but roadmap influence is nil — name it. (2) **Curriculum content is the real cost**, not the editor; a proposal that prices the platform and not the lessons will be re-scoped in month two. (3) Blockly's stewardship changed hands a year ago and client SBOMs will still say `google/blockly` (**T36**) — budget an afternoon for alias reconciliation rather than discovering it in a security review.

## P23 — The block-to-text bridge with an LLM tutor inside the workspace (secondary schools, coding academies, CS faculties: 6–8 weeks) 🟢 new at p658

**Buyer:** anyone whose learners have outgrown blocks and stall on text. This is the highest-attrition moment in a coding curriculum and almost nothing addresses it — the tooling either keeps learners in blocks forever or drops them into a bare editor.

```
learner in a Blockly workspace
  └── TutoriaLLM/TutoriaLLM (MIT, 1,068 B, `main`, 303★, pushed 2026-11-03)  🇯🇵 APAC
        the ONLY permissive agent this base has found that watches the BLOCK
        WORKSPACE and guides inside it, rather than chatting beside it
        └── self-hosted; bring your own model via the LMS-side gateway
  │
  ├── progression step 1 — show the text:  leopard-js/leopard (MIT, 1,200 B, `master`, 168★)
  │     converts an existing Scratch project to READABLE JavaScript
  │     → the learner sees THEIR OWN project as code: the single best motivator available
  ├── progression step 2 — write the text: aspizu/goboscript (MIT + BSD-3-Clause subtree, `main`, 577★)
  │     a text language that COMPILES BACK to .sb3, so the project keeps running
  │     → and it is now in git: diffable, reviewable, assignable
  └── progression step 3 — run it fast:   forkphorus/forkphorus (MIT, 1,124 B, `master`, 150★)
        MIT runtime, replaces AGPL-3.0 scratch-vm (T40)

  evidence out → lrsql (Apache-2.0) over xAPI; grading → P19 (Artemis, MIT)
```

**Weeks 1–2** deploy `TutoriaLLM` self-hosted against the client's model endpoint and encode two lessons; measure where learners actually stall before changing anything. **Weeks 3–4** wire the `leopard` conversion as a *lesson step* — "here is your project as JavaScript" — not as an export button nobody clicks. **Weeks 5–6** `goboscript` for the first text-authored assignment, committed to git, so the CS faculty can review code rather than screenshots. **Weeks 7–8** optional: `forkphorus` as the runtime and xAPI telemetry on the block→text transition itself, which is the metric the client has never had.

🟢 **Licence position: MIT throughout.** ⚠️ **`goboscript` carries a conjunctive grant** — MIT for the project plus **BSD-3-Clause** scoped to `tools/sb3_definitions.json` and `tools/sb3_schema.json` (p382 subtree class). Both are permissive and the BSD attribution obligation is narrow, but it must appear in the client's notices. ⚠️ **The second copyright line in that payload reads "Massachusetts Institute of Technology" — the institution, not the licence.** Do not let it be transcribed as "MIT" in an SBOM; it is the BSD-3-Clause grant on the Scratch schema files.

⚠️ **Risk.** `TutoriaLLM` is 303 ★ with a small maintainer base and a Japanese-first community; it is MIT and self-hosted, so the downside is maintenance, not lock-in. If the client cannot accept that, the fallback is P4's tutoring stack plus a hand-built `leopard` step — more work, no agent in the workspace.

## P24 — The learner-owned study graph, driven by a local model, evidenced to the institution (5–7 weeks) 🟢 new at p659

**Who buys it:** universities and professional-certification bodies that want a study/revision tool for enrolled learners but cannot send course materials or learner performance to a third-party API — the EMEA sovereignty buyer, the LATAM public-sector buyer, and any APAC client inside South Korea's or Vietnam's assessment rules.

**What makes it buildable now:** p659 verified `OPTIMETA/PAIDEIA-mcp` (MIT) — the study engine behind `PAIDEIA` as a **standalone local MCP server**, with no dependency on any vendor's agent runtime. That is the piece that turns a consumer plugin (**T41**) into something an institution can host. It is the same move **P6** made for retention, one layer up.

```
THE LEARNER'S OWN COURSE MATERIALS  (lecture PDFs, scanned problem sets, past papers)
  │   ingest, on the institution's hardware — nothing leaves the building
  ├── Tesseract OCR                       → scanned/handwritten problem sets
  └── Qwen3-VL via ollama/ollama (MIT, 1,058 B payload read p659)  → figures, diagrams, equations
       │
       ▼
  OPTIMETA/PAIDEIA-mcp  (MIT, 1,068 B payload read p659, local MCP server)
       │   builds the per-course study graph: error patterns, homework-density weighting,
       │   strategy grading, cheatsheet — emitted as Markdown/LaTeX FILES, not rows in a vendor DB
       │
       ├── scheduling layer — do NOT reimplement it:
       │     open-spaced-repetition/fsrs-rs (BSD-3-Clause)  → the retention primitive, per T13
       │
       ├── model layer, client-controlled:
       │     ollama/ollama (MIT) serving an open-weight model on the client's own GPU
       │     ⚠️ no API key anywhere in this diagram — that is the deliverable, not a constraint
       │
       ▼
  THE EVIDENCE SPINE  (P17 — this is what makes it an institutional sale, not a download)
       ├── in:  dmitry-viskov/pylti1.3 (MIT) → LTI 1.3 launch from Moodle / Canvas / Brightspace /
       │        Open edX / OpenOlat. An LTI tool is a SEPARATE WORK: GPL-3.0 Moodle and AGPL-3.0
       │        Open edX impose nothing on your code.
       └── out: yetanalytics/lrsql (Apache-2.0) → xAPI statements into the institution's OWN LRS
                (adlnet/ADL_LRS, Apache-2.0, is the alternative)
       │
       ▼
  YOUR LAYER  (proprietary, closed — every dependency above is MIT / Apache-2.0 / BSD-3-Clause)
       course-pack onboarding, cohort dashboards, faculty review of generated material
```

**Weeks 1–2.** Stand up `PAIDEIA-mcp` against `ollama` on the client's hardware with one real course's materials. The acceptance test is adversarial and worth writing into the SOW: **pull the network cable and the system still works.** If it does not, something is calling out and the sovereignty claim is void.

**Weeks 3–4.** Wire `fsrs-rs` for scheduling and the LTI 1.3 launch, so the tool opens from inside the LMS the learners already use. No fork of the LMS at any point.

**Weeks 5–7.** The xAPI spine into the client's own LRS, and the faculty review surface — a human signs off generated study material before a cohort sees it.

🔵 **Why the licence stack is the sellable part.** Every component is MIT, Apache-2.0 or BSD-3-Clause, verified by first-hand payload read: `PAIDEIA-mcp` MIT, `ollama` MIT, `fsrs-rs` BSD-3-Clause, `pylti1.3` MIT, `lrsql` Apache-2.0. **Your layer can be closed and client-branded**, and nothing in the graph forces disclosure. Contrast **P2** and **P3**, where the copyleft LMS has to be held at arm's length by construction.

🔴 **Three things this pattern must not be sold as.**
1. **Not an assessment system.** The moment its output becomes the official basis for a grade or a ranking it is **Annex III high-risk** in the EU (2 December 2027), **high-impact** under South Korea's AI Basic Act, and inside Vietnam's `Decision 33/2026/QD-TTg` list. Keeping it demonstrably *formative* — a study aid the learner drives, never a system of record — is an **architecture deliverable**, and `intel/market.md` APAC says why that scoping line is itself billable.
2. **Not a proctoring or monitoring tool.** Nothing here watches a learner. Keep it that way: exam monitoring is high-risk and emotion recognition in schools has been prohibited in the EU since February 2025.
3. **Not evidence of adoption.** `PAIDEIA-mcp` carries `2` stars. It is a 2026 repository with one author and a single push on its creation date (`2026-06-14`). 🔴 **Pin the commit, read the code before it goes near a client, and budget for maintaining it yourself** — this is an adopt-and-harden of a small codebase, which is the honest framing, and the same caution `agents/top.md` attaches to every low-star row.

## Choosing a pattern

| Client situation | Pattern | Why |
|---|---|---|
| Already on Canvas | **P1** | No migration, no licence exposure, fastest demo |
| Already on Moodle (LATAM/EMEA) | **P2** | Meets the dominant installed base; local models for residency |
| MOOC / corporate academy on Open edX | **P3** | Only licence-safe Open edX shape |
| Wants explainable mastery (STEM) | **P4** | BKT + pyKT; budget content authoring |
| Uses AI already, controls nothing | **P5** | Sell governance first, then P1–P4 |
| Pilot must prove an outcome | **P6** | Permissive end to end, retention measurable, no per-review inference cost. Attach it to any other pattern |
| Ministry/district wants its OWN branded coding platform | **P22** | MIT end to end, offline-capable, closed derivative permitted |
| Learners stall moving from blocks to text | **P23** | The one permissive agent that works inside the block workspace |
| Connectivity cannot be assumed | **P7** | The only pattern with no copyleft component anywhere, and the only one that works offline |
| Needs a full education ERP (finance, HR) | **P2 + OpenEduCat** | `openeducat/openeducat_erp` (LGPL-3.0, 905★) on Odoo. ⚠️ default branch is `19.0` and `20.0` exists — resolve it |
| Already on Moodle and wants a **real agent**, not just REST glue | **P8** | Names the bridge P2 left as a placeholder. `G36maid/moodle-mcp` (MIT, 27★) — adopt and harden; **price the hardening, it is not P1** |
| Data residency, offline, **or** must stay off the graded system of record (Korea, Vietnam) | **P9** | Curriculum knowledge in the weights, FP8 on one GPU, no egress. 🔴 Resolve the OmniEdu weight licence first |
| Has a funded AI-literacy mandate (Canada, Saudi, Kenya, EU Art. 4) | **P10** | The deliverable is curriculum and teacher capacity, not software. MIT base at 41.1k★ permits a closed client derivative |
| 🟢 **Choosing a platform rather than extending one** — new faculty, national programme, migration off a commercial LMS | **P11** | The only pattern whose institutional platform is itself permissive. Apache-2.0 course management, `langchain4j` already in-tree. ⚠ Specify PostgreSQL, not MySQL; price the Java skill-set |
| 🟢 **Wants to own a reference integration rather than rent one** | **P12** | OpenOlat has **no** agent bridge at any address. No incumbent, no copyleft to route around, agent can live in-tree, and the result is contributable upstream under Apache-2.0 |
| 🟢 **Needs grading or written-feedback at scale** | **P13** | The only pattern where the production artefact does not exist yet. Permissive, education-specific, peer-reviewed *research* supply (ArguLens) + calibration to the client's own markers (`LLM-Rubric`) + an approval gate. ⚠ Assistive scoring with human sign-off only — never autonomous grading |
| 🟢 **Has an incumbent LMS and must prove the pilot worked** — i.e. almost every engagement | **P17** | The layer under all the others: LTI 1.3 in (no fork, no copyleft inherited), xAPI out to an Apache-2.0 LRS. **Attach it to any pattern above.** 🔴 `yetanalytics/lrsql` is the only live permissive LRS — scope that dependency explicitly |
| 🟢 **Must meet the April 2026 US ADA accessibility deadline** | **not a product** | `ucfopen/UDOIT` (GPL-3.0) is the only real tool and there is **no permissive alternative**. Client-operated deployment, bill the remediation, ship no derivative. See `intel/market.md` → North America |

## 🔴 What these patterns deliberately avoid

- **No pattern forks a GPL or AGPL platform.** 🔴 **Count corrected at p656: fifteen of twenty-six** verified platforms on `verticals/solutions.md` are copyleft (this line previously read "ten of fourteen", stale since p655 and again after p656 shelved the H5P, Adapt, UDOIT, TAO and Learning Locker rows); forking one for a managed service is the single most expensive mistake available in this industry. **P7 is the exception that proves the rule** — it can own its platform layer precisely because Kolibri is MIT.
- 🟢 **Two exclusions from the previous version of this list are withdrawn.**
  - `OpenEduCat` was excluded as **HTTP 404**. The project is live at **`openeducat/openeducat_erp`** (LGPL-3.0, 905★, default branch `19.0`); only the published address was dead. It is now the recommended base when a client needs a full education ERP, and LGPL-3.0 is a better licensing position than the `frappe/lms` (AGPL-3.0) substitute that was recommended in its place.
  - `tutor-mcp` was excluded at **0 stars**. That measured `kvnloo/tutor-mcp`, which is a **fork**; the upstream `ArnaudGuiovanna/tutor-mcp` has **96★ / 13 forks** and is the backbone of **P6**.
- **Still excluded:** `awesome-ai-llm4education` (**no licence**, 221★) and `eduadapt-ai` (**no licence**, 26★), both previously published here as MIT and neither of which is. Added to the exclusion list at p651: `GarethManning/education-agent-skills` (949★ but **CC BY-SA 4.0** — ShareAlike, so a derivative skill library cannot be proprietary); `virtualryder/edu-ai-agents` (4★ and a **modified MIT payload with the limitation-of-liability paragraph removed**); `mthatipamula/educational-assessment-ai-agent-platform`, `luffycodes/Tutorbot-Spock` and `Micel357/Edu-mentor-AI` (**no licence file**); `CodeBreez/collejo` (MIT but **archived read-only since 2024-05-16**).
- **No pattern includes proctoring or emotion recognition.** Emotion recognition in schools is banned in the EU; exam monitoring is high-risk there and, since 22 January 2026, student assessment in K-12 is high-impact under South Korea's AI Basic Act with fines expected from around January 2027. No permissively-licensed open source option was found in any case.

## 🔴 Resolve the licence of the *tree*, not the repository — five live cases

Reading `LICENSE` is necessary and not sufficient. Four components these patterns use carry obligations their repository badge does not mention; the fifth row is the case where the manifest read came back **clean**, which is the result that makes a pattern scopeable. All five were read from bytes or from a manifest field verbatim on 2026-11-04.

| Component | Badge | Actual obligation in the tree | What to do in a pattern |
|---|---|---|---|
| **OpenMAIC** (P10, P3) | MIT | `packages/mathml2omml` is **LGPL-3.0-or-later** (7,652 B), `"workspace:*"` in the root manifest, built as step one of `build:packages` | Keep it dynamically replaceable with source offered, or excise the MathML→OOXML export path. Design-time decision |
| **OmniEdu weights** (P9) | Apache-2.0 *(code)* | **No named grant for the weights.** README: *"Model weights and third-party datasets and benchmarks retain their respective licenses."* Backbones are Qwen | Read the Hugging Face card before scoping. Gate zero of P9 |
| **open-moodle** (not used) | MIT | Depends on **PyMuPDF (AGPL-3.0)** | Excluded from P8 for this reason. An AGPL dependency in a network-served agent defeats out-of-tree containment |
| 🟢 **OpenOlat** (P11, P12) | Apache-2.0 | **Clean, and verified rather than assumed.** 270 declared dependencies contain exactly one copyleft item: the *optional* **MySQL Connector/J** (GPL-2.0 + Universal FOSS Exception), whose exception covers OSI-approved open source licences but **not** a closed derivative. Verified absent: iText (AGPL-3.0), JasperReports (LGPL). Hibernate 7.4.14 / validator 9.1.6 are Apache-2.0 eras, not the old LGPL-2.1 Hibernate | **Specify PostgreSQL JDBC 42.7.14 (BSD-2-Clause), already a first-class in-tree backend.** One line in the architecture document and the tree is permissive end to end. This is the whole cost of the only clean copyleft exit on this shelf |
| **csmediapro/moodle-mcp-server** (not used) | "free use, no closed-source repackaging" | Plain **AGPL-3.0**, 34,523 B, plus paid Premium Plugins | Excluded from P8. Marketing language is not a licence; read the payload |

**The check to run once per engagement, in week one:** read `LICENSE` from bytes; then read `package.json`, `pyproject.toml` and `Cargo.toml` for every bundled or workspace component; then, for any model, read the weight card separately from the code licence. Five of the **six** grant-defect classes this KB has catalogued pass a licence-badge check. The sixth — *grant by reference*, where the Apache-2.0 notice stands in for the terms, as in `wwrwbs/AI_AWE` (P13) — **fails** the badge check and is nonetheless usable, so a short grant file is a reason to read it rather than to reject the project.

## 🔴 Resolve the branch before you clone — five live cases on this shelf

Every pattern above assumes you check out the right thing, and on this shelf the default branch is frequently not it:

| Repo | Default branch | What goes wrong |
|---|---|---|
| `openeducat/openeducat_erp` | **`19.0`** | A hardcoded `main`/`master` builds nothing; a hardcoded `19.0` silently keeps building the old major, because `20.0` already exists |
| `francoisjacquet/rosariosis` | **`mobile`** | A default clone gives you the mobile branch, not the release line, among 44 branches that are otherwise version numbers |
| `learningequality/kolibri` | **`develop`** | A default clone gives you development code; deploy from `release-v0.19.x` or `release-v0.20.x` |
| `OpenOLAT/OpenOLAT` | `master` | `master` is the development trunk, not a release. **Deploy from `OpenOLAT_21.1`** (latest tag `OpenOLAT_21.1.2`); live release branches run `OpenOLAT_18.0` → `OpenOLAT_21.1`. The naming is `OpenOLAT_<major>.<minor>` — note the all-caps prefix, which differs from the repository's own mixed-case `OpenOlat` branding and from the `OpenOlat_20.0.pre2` tag, so a generated branch name will not match |
| `GeminiLight/gen-mentor` | `main`, and that is the problem | `main` is a browser-only Next.js demo app. **The multi-agent Python implementation its WWW '25 paper describes is on branch `v0.1-demo`** — so the default gives you a demo, not the evaluated system |

The fix is one command, and it belongs in any ingest or deployment script rather than in a human's memory:

```bash
git ls-remote --symref https://github.com/<owner>/<repo> HEAD   # returns the real default branch
```

Then read the README for which branch carries the artefact you actually want — resolving the default is necessary and, as `gen-mentor` shows, not always sufficient.

## P25 — Early-years computational thinking with no device budget and no copyleft (6–8 weeks) 🟢 new at p660

**The engagement this answers.** A ministry, a school network or a foundation wants computational thinking for ages 5–10, at system scale, on hardware that does not exist yet, and wants a derivative it can brand and operate. Every earlier pattern on this page assumed either a device per learner or an AGPL platform. This one assumes neither.

**Why it is new at p660.** Until this pass the base held that the Scratch family's only permissive surfaces were `scratch-blocks` and `forkphorus` — components, not a product. Org enumeration found **ScratchJr under BSD-3-Clause** and a **live, MIT, browser-only micro:bit stack**. Those two facts together make a permissive early-years programme buildable for the first time in this KB.

```
          ┌─────────────────────── LEARNER SURFACE — pick ONE by age ───────────────────────┐
  ages 5–7   scratchfoundation/scratchjr        BSD-3-Clause  1,508 B  707★  `develop`
             └─ 🔴 dormant since 2022-07-22 → FORK AND OWN; budget the maintenance line
  ages 8–10  microbit-foundation/python-editor-v3   MIT  1,083 B  84★  `main`  (pushed 2026-11-04)
             └─ microbit-foundation/micropython-microbit-v2-simulator  MIT  1,117 B  21★
                └─ 🟢 THE BOARD RUNS IN THE BROWSER — zero hardware per learner
          └────────────────────────────────────────────────────────────────────────────────┘
                                   │  project files (.sb / .hex / .py)
                                   ▼
  ┌──────────────── ASSESSMENT — grades the ARTEFACT, not the prose ────────────────┐
    scratchfoundation/scratch-analysis   BSD-3-Clause  1,520 B  36★  `develop`
      structure · composition · complexity  →  your own rubric weights (closed, BSD permits it)
    microbit-foundation/cctd-ml-machine   MIT  1,126 B  10★   AI-literacy module:
      learner trains a gesture classifier on sensor data = "what is a model", by building one
  └─────────────────────────────────────────────────────────────────────────────────┘
                                   │  scores + evidence
                                   ▼
  ┌──────────────── PLUMBING — all permissive, all already on this base ────────────┐
    ollama/ollama        MIT  1,058 B   local model: feedback in-country, no per-seat API cost
    pylti1.3             LTI 1.3 launch from the client's existing LMS (Moodle stays stock)
    yetanalytics/lrsql   xAPI statements → the learning record the ministry reports on
  └─────────────────────────────────────────────────────────────────────────────────┘
```

**Licence boundary — the whole point of the pattern.** Every component above is BSD-3-Clause, MIT or Apache-2.0. There is **no GPL and no AGPL anywhere in the chain**, so the derivative can be closed, branded and sold as a managed service. Contrast the obvious-looking alternative: building on `scratch-gui` (AGPL-3.0) means hosting it as a service triggers network copyleft over your modifications, and building on `Scratch_1.4` drags in GPL-2.0 **plus** a runtime attribution obligation in the `Help > About` dialog (**T42**).

🔴 **Do not put the curriculum in scope on these terms.** `RaspberryPiFoundation/scratch-curriculum` is the natural lesson material and it is **CC BY-NC-SA 4.0** — NonCommercial, so it cannot be shipped in a paid programme at all (**T42**). Either license it separately and directly from the Raspberry Pi Foundation, or author lessons as a billable deliverable. The permissive content exception is `scratchfoundation/scratchjr-website` (BSD-3-Clause, live to 2026-08-20), which is a genuinely reusable starting point for teacher-facing material.

**Sequence.**
- **Weeks 1–2** — Fork ScratchJr, stand the simulator stack up behind the client's LMS via `pylti1.3`, and get one class of each age band producing project files. Do not build assessment yet; find out what learners actually make first.
- **Weeks 3–4** — Wire `scratch-analysis` over the collected projects and calibrate rubric weights against teacher judgement on a sample. This is where the value is: the complexity metrics are off-the-shelf, the weighting is the client's pedagogy and is yours to keep.
- **Weeks 5–6** — Add `cctd-ml-machine` as the AI-literacy unit and emit xAPI to `lrsql`, so the programme reports against the AI-literacy mandates this KB tracks (`intel/market.md`, North America and EMEA legs) rather than against seat counts.
- **Weeks 7–8 (conditional)** — Local-model feedback via `ollama` only if the client has a data-residency requirement; otherwise skip it and save the inference engineering.

**What to tell the client up front.** The ScratchJr fork is **four years cold**. That is not a defect for a fork-and-own engagement — it means the upstream will not surprise you — but it does mean there is no community fixing iOS/Android build breakage for you, and that maintenance line must be in the price. The micro:bit half is the opposite: pushed yesterday, so it needs tracking rather than owning. Scoping the two halves the same way is the mistake this pattern exists to prevent.

## P26 — Accessibility remediation where three quarters of it can be a closed product (institutions under the April 2026 US ADA deadline: 8–12 weeks) 🟢 new at p661

**The engagement this answers.** A large US public university or community-college system is under the **April 2026 ADA Title II** obligation and has a backlog of inaccessible course content: thousands of hours of uncaptioned lecture video, mathematics rendered as images, and HTML course pages that have never been audited. Until p661 this base answered that engagement with *"there is no permissive supply — sell services, ship no derivative"* (`intel/trends.md` **T29**). **That answer was wrong for three quarters of the work.**

**Why it is new at p661.** T29's blanket claim was withdrawn when the mandate was decomposed into the capabilities it actually creates. Three of four have production-grade permissive answers that this base had measured in its own logs and never shelved — `openai/whisper` is **MIT at `111,975★`** and is named in both append-only logs as *"the ASR baseline"*. Only the fourth is copyleft-locked. **The licence boundary runs between capabilities, not around the engagement**, and that is what makes a product possible here for the first time.

```
  BACKLOG IN  ─────────────────────────────────────────────────────────────────────
   lecture video · recorded lectures · podcasts         course HTML · PDFs · math
         │                                                       │
         ▼                                                       ▼
  ┌──── 🟢 PERMISSIVE — CLOSED DERIVATIVE PERMITTED ────────────────────────────┐
  │                                                                             │
  │  CAPTIONING  (biggest piece of the work by volume)                          │
  │    openai/whisper            MIT   1,063 B   111,975★   `main`              │
  │      └─ self-host: no per-minute vendor fee, no student audio leaving        │
  │         the estate → the data-residency answer sells this on its own        │
  │                                                                             │
  │  MATHEMATICS                                                                │
  │    NSoiffer/MathCAT          MIT   1,065 B   ★ unmeasured   `main`          │
  │      └─ MathML → speech (15 languages) + braille (Nemeth, UEB, CMU)         │
  │         + structural navigation · DAISY-sourced                             │
  │      └─ 🔴 needs MathML IN, so OCR/authoring is YOUR integration work       │
  │                                                                             │
  │  AUDIT / TRIAGE / REPORTING                                                 │
  │    GoogleChrome/lighthouse   Apache-2.0   11,358 B   31,019★   `main`       │
  │      └─ runs LOCALLY, nothing leaves the machine → quotable under an        │
  │         EMEA/LATAM data-residency clause as well as a US one                │
  │      └─ audits only; produces the WORKLIST, performs no repair              │
  │                                                                             │
  │   ⇒ wrap these three behind ONE MCP surface + a queue. This is the          │
  │     BRANDED, CLOSED DELIVERABLE. MIT and Apache-2.0 both permit it.         │
  └─────────────────────────────────────────────────────────────────────────────┘
         │  worklist: defect → file → owner → status
         ▼
  ┌──── 🔴 COPYLEFT — DEPLOY, DO NOT DERIVE ───────────────────────────────────┐
  │  IN-PLACE WCAG REPAIR INSIDE THE LMS COURSE                                │
  │    ucfopen/UDOIT   GPL-3.0   35,147 B   117★   `main`   (pushed 2026-11-04)│
  │      └─ scans Canvas content, explains defects, fixes many in place        │
  │      └─ STILL THE ONLY PRODUCTION TOOL. Run it inside the client's own     │
  │         estate, unmodified. Bill the remediation and the integration.      │
  │         Ship NO derivative of this component.                             │
  └────────────────────────────────────────────────────────────────────────────┘
         │  evidence of remediation
         ▼
  yetanalytics/lrsql   Apache-2.0   144★   ← xAPI statements per remediated asset
      (the evidence spine from P17 — reuse it, do not build a second one)
```

**Wiring, concretely.**

1. **Triage first, because it sizes the contract.** Run `lighthouse` headless across the course estate's public HTML and emit one row per defect. This is a worklist, not a fix, and it is the only step that tells the client how big the backlog is. Lighthouse is Apache-2.0, so the triage dashboard is yours.
2. **Captioning queue.** Self-host `whisper`, feed it the video backlog, emit WebVTT. Two commercial arguments, both stronger than the technical one: there is **no per-minute vendor fee** at estate scale, and **no student audio leaves the institution**, which is the clause that kills most SaaS captioning bids in public-sector procurement. Human review of the output is a billable line, not a defect — budget it explicitly.
3. **Mathematics path.** Route MathML through `MathCAT` for speech and braille. 🔴 **Scope this honestly:** MathCAT needs MathML as input, so if the client's maths is page images the conversion step is *your* work and is the larger half of the task. Do not price this alongside captioning as if it were the same kind of job.
4. **One MCP surface over all three.** `caption_asset`, `audit_page`, `render_math_accessible`, each returning a status the queue can track. This wrapper plus the triage dashboard **is the product**, and MIT + Apache-2.0 permit it to be closed and client-branded.
5. **UDOIT last, and at arm's length.** Deploy it unmodified in the client's estate for in-place Canvas repair. Do not import it, do not link it, do not fork it into the product tree. It is GPL-3.0 and it is the one component that must stay a deployed tool rather than a dependency.
6. **Evidence out.** Write an xAPI statement per remediated asset into `lrsql` (Apache-2.0), reusing **P17**'s spine rather than building a second one. The institution needs to *show* compliance, not merely achieve it, and a dated statement per asset is the artefact an auditor accepts.

**What to say in the proposal.** *"Most of this programme is a product we can build and brand; the last mile inside Canvas is a tool we deploy and operate for you."* That sentence is the whole value of this pattern, and until p661 this base could not say it.

**🔴 What this pattern does not claim.** The **April 2026 deadline itself is carried from secondary sources** and has never been read in primary form by this base — confirm it against the rule text before it anchors a contract date. `MathCAT`'s adoption is **unmeasured**: three independent channels refused the address at p661 (`gh api search/repositories` `422`, `gh api repos/` `403`, HTML `403`), so its licence and existence are first-hand facts and its popularity is not. And `lighthouse` is a **general-purpose** web auditor, not an education tool — it will flag defects in LMS chrome that the institution does not own, so the worklist needs a scoping filter before anyone is handed it.

## P27 — The licence-provenance gate, as the first two weeks of any education engagement (2 weeks, then a standing gate) 🟢 new at p662

**The engagement this answers.** A studio is about to build on an open source education platform. Procurement will run an SBOM and SPDX scan before anything ships, and the scan will return answers that are *wrong in both directions* on the exact repositories this KB recommends. Somebody has to be able to say, in a review, why a `NOASSERTION` is harmless and why a published comparison table is not. That is a two-week deliverable, and it pays for itself the first time it stops a fork.

**Why it is new at p662.** p658 established licence-truth as a billable deliverable on the `TurboWarp/extensions` case. p662 supplies the specimens that make it a *gate* rather than an audit: a controlled set in which the scanner's verdict is wrong in each direction, with the payload held constant across the pair that matters.

```
  ┌──── 🟢 THE GATE — THREE PERMISSIVE TOOLS, ALL VERIFIED 2026-11-05 ─────────┐
  │                                                                           │
  │  anchore/syft                  Apache-2.0  LICENSE  11,357 B              │
  │    sha256₁₂ c71d239df917   9,832★   `main`   pushed 2026-11-04            │
  │      └─ SBOM generation from images, dirs and archives → SPDX + CycloneDX  │
  │                                                                           │
  │  aboutcode-org/scancode-toolkit  Apache-2.0 + CC-BY-4.0  `develop`        │
  │    apache-2.0.LICENSE  11,357 B  sha256₁₂ c71d239df917   (the CODE)       │
  │    cc-by-4.0.LICENSE   18,651 B  sha256₁₂ 2a82ac9bbc3e   (the licence DB) │
  │    NOTICE 2,333 B      2,662★   pushed 2026-11-02                         │
  │      └─ reads grants out of a SOURCE TREE, which is the axis `syft` misses │
  │      └─ 🔴 DUAL-LICENSED: the tool is Apache-2.0, the licence DATA is      │
  │         CC-BY-4.0. Shipping its output means carrying attribution.        │
  │                                                                           │
  │  CycloneDX/cyclonedx-cli       Apache-2.0  LICENSE  11,341 B              │
  │    sha256₁₂ 6c29f22a4a73   555★   `main`   pushed 2026-10-19              │
  │      └─ convert / merge / diff SBOMs → the format procurement asks for     │
  │      └─ 🔧 p662 corrected this base's own ledger verdict (`unstated`)      │
  └───────────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
  ┌──── 🔴 WHAT THE GATE IS FOR: FOUR SPECIMENS, FOUR FAILURE MODES ──────────┐
  │                                                                           │
  │  1. SCANNER SAYS NOASSERTION, GRANT IS CLEAN — filename axis              │
  │     scancode-toolkit    gh api → NOASSERTION                              │
  │     anchore/syft        gh api → Apache-2.0                               │
  │       └─ SAME PAYLOAD. Both 11,357 B, both sha256₁₂ c71d239df917.         │
  │          The only variable is the FILENAME: `apache-2.0.LICENSE`          │
  │          vs `LICENSE`. Controlled specimen for `558-B` / `572-B`.         │
  │                                                                           │
  │  2. SCANNER SAYS NOASSERTION, GRANT IS CLEAN — appended-text axis         │
  │     OpenOLAT/OpenOLAT   LICENSE 10,982 B  sha256₁₂ 6dbc5b605ed0           │
  │       └─ sections 1–9 byte-identical to canonical; APPENDIX removed,      │
  │          two provenance statements appended. Mechanism = `659-F`.         │
  │       └─ 🟢 CONTRAST: cyclonedx-cli FILLED the appendix in place          │
  │          (`Copyright OWASP Foundation`, brackets `{}`) and still          │
  │          classifies Apache-2.0. Completing it is safe; removing it        │
  │          and appending is not.                                           │
  │                                                                           │
  │  3. A PUBLISHED TABLE SAYS MIT, THE REPO SAYS AGPL — the expensive one    │
  │     learnhouse/learnhouse  LICENSE 34,523 B  sha256₁₂ 8486a10c4393        │
  │       └─ AGPL-3.0 on `dev` AND on `main`. gh api agrees. 2,448★.          │
  │       └─ A current LMS comparison puts it under "MIT/Apache …             │
  │          maximum flexibility". Network-use clause, hosted deployment.    │
  │                                                                           │
  │  4. GRANT IS FORMALLY PERFECT AND NAMES NO LICENSOR                       │
  │     lebmatter/exampro  license.txt 1,069 B  sha256₁₂ 002c2696d92b        │
  │       └─ stock MIT whose copyright line is literally                      │
  │          `Copyright (c) [year] [fullname]`. Passes every badge check.    │
  │          Legally unattributable. Catalogued at `p202`, specimen `661-A`. │
  └───────────────────────────────────────────────────────────────────────────┘
```

**Wiring, concretely.**

1. **Resolve the ref before anything else.** `git ls-remote --symref <repo> HEAD`. Four of the repositories named on this page do not default to `main` — `scancode-toolkit` is `develop`, `OpenOLAT` is `master`, `oppia` is `develop`, `learnhouse` is `dev`. A grant read against `/main/` by habit is a grant read of the wrong branch, and specimen **3** — [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) — was nearly missed this way. See *"Resolve the branch before you clone"* above.
2. **Enumerate the filename space, do not trust one probe.** `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `LICENSE.TXT`, `COPYING`, `COPYING.txt`, `LICENCE`, `license`, **and `<spdx-id>.LICENSE`** — that last form is what hid `scancode-toolkit`'s clean Apache grant from a five-filename ladder.
3. **Byte-read and digest every grant.** Record `path`, `bytes`, `sha256₁₂` and the copyright line. A byte count is the cheapest tamper check there is, and it is what distinguishes specimen **2** from a genuine licence change. 🔴 **Name the canonical copy any `−N B` delta is measured against**: `apache/.github` serves Apache-2.0 at `11,357 B` and `apache.org` at `11,358 B`, so an unattributed delta is ambiguous by `1 B` (p662's standing rule).
4. **Run [`anchore/syft`](https://github.com/anchore/syft) for the dependency tree and [`aboutcode-org/scancode-toolkit`](https://github.com/aboutcode-org/scancode-toolkit) for the source tree.** They answer different questions and the gate needs both: `syft` sees declared package metadata, `scancode` sees grants actually present in files. The licence unit is the dependency graph, not the repository — the section above this one has the five live cases.
5. **Normalise to CycloneDX and hand procurement the diff, not the scan.** [`CycloneDX/cyclonedx-cli`](https://github.com/CycloneDX/cyclonedx-cli) converts and *diffs*, so the standing gate is a diff against last release: new grant, changed grant, or disappeared grant. Three states, each with an owner.
6. **Ship the rebuttal file with the SBOM.** One row per `NOASSERTION`, each with the mechanism (filename / appended text / no grant at all), the digest, and the sentence that closes it. This is the artefact that turns a two-week audit into a gate somebody can sign.

**What to say in the proposal.** *"Your scanner will flag the largest permissive LMS in this stack as unlicensed, and it is wrong. It will also pass a platform that a published comparison table calls MIT and which is actually network-copyleft, and that one would have cost you the source of your product. We will give you the evidence for both, in the format your procurement team already reads, and a diff-based gate that keeps answering the question after we leave."*

**🔴 What this pattern does not claim.** It does **not** constitute legal advice and it does **not** resolve clause-level residuals — a dual-licensed component like `scancode-toolkit` carries an attribution obligation that counsel, not a scanner, has to price. The four specimens are verified first-hand at `2026-11-05`; the *generalisation* that scanners err in both directions at a measurable rate is **not** quantified by this pass on a sampled population, and `572-B` is the only rate figure this base holds for the filename axis.

## P28 — Spanish-language tutoring inside Open edX, for a public university that cannot send student data anywhere (LATAM public higher education, rural and regional campuses: 8–10 weeks) 🟢 new at p663

🔵 **Why this pattern exists now.** Until p663 this base had **no placed LATAM agent row at all**, so every LATAM engagement had to be composed from APAC and North American parts and localised. It now has two Colombian rows, and — more usefully — a **worked reference for the hardest part of the job**, which is not the tutor but the *integration*. Open edX is the platform tier this region actually runs, and `LabSirius/TutorIA` is the only agent on this shelf that lands **inside** it.

### The parts

| Layer | Component | Licence | Why this one |
|---|---|---|---|
| Platform | [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | **AGPL-3.0** | The incumbent across LATAM public higher education. ⚠️ **Copyleft — it is the host, never the derivative.** You deploy it; you do not fork it into a client-branded product. |
| **Integration reference** | [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) | **MIT** (1,069 B, © *Grupo Sirius*) | 🟢 **The pattern's keystone.** An **Open edX XBlock/plugin**, so the tutor sits inside the course, enrolment and grading objects instead of talking to them over REST. Built for **rural higher education in Risaralda** at Universidad Tecnológica de Pereira — the same institutional shape as the client. **Read it as an integration reference, do not ship it: `0★`, 4 commits.** |
| Tutor engine | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | Apache-2.0 | Carries the persistent learner model, which `TutorIA` does not. This is the swap that turns the reference into a product. |
| Programming track | [`AndresGuido9820/trabajo2-agente-tutor`](https://github.com/AndresGuido9820/trabajo2-agente-tutor) | **MIT** (1,085 B) | 🟢 **Pyodide in the browser** — learner code runs client-side, so there is **no sandbox to operate or secure**, the single largest hidden cost in a CS tutoring build. Spanish-language and Socratic by construction. `0★` but **151 commits / 314 tests**. |
| Model | Ollama + an open-weight model, on university hardware | — | The binding constraint in this pattern is egress, not capability. |
| Mastery | [`kvnloo/tutor-mcp`](https://github.com/kvnloo/tutor-mcp) | MIT | BKT + FSRS behind one MCP tool surface, so mastery estimates are explainable to a faculty committee. |
| Evidence | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) + [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec) | Apache-2.0 | **P17**'s spine. Non-negotiable here — see *Why the statement log is the deliverable* below. |

### How it wires together

1. **Weeks 1–2 — run P27 first, and run it on the two Colombian rows specifically.** `TutorIA` ships **two addresses for one work**: its own README's clone command points at the predecessor [`Sof1SP/TutorIA`](https://github.com/Sof1SP/TutorIA), whose grant names **a different licensor** (© *Sofia Soto Parra*, 1,073 B) from the one you are adopting (© *Grupo Sirius*, 1,069 B). **Settle in writing which grant the derivative takes before any code is copied.** This is not pedantry — it is the one defect in this pattern that cannot be fixed later.
2. **Weeks 2–4 — stand up Open edX and lift the XBlock boundary from `TutorIA`.** Take its *shape* — how it registers, where it reads enrolment, how it writes grades, how the teacher statistics panel is mounted — and reimplement against your own MIT code. 🔴 **Keep the AGPL boundary clean:** the XBlock talks to the platform through published extension points, so your plugin stays separately licensed. Nothing you write enters `edx-platform`.
3. **Weeks 4–6 — swap the engine.** `TutorIA`'s backend is FastAPI calling a hosted model API. Replace it with **DeepTutor against local Ollama**. This is the step that converts a 4-commit artefact into something with a persistent learner model and no egress path.
4. **Weeks 5–7 — add the programming track.** Mount `Profe Bit`'s **Pyodide execution model** as the CS course type. Its one-SQLite-database-per-course design maps cleanly onto Open edX course keys, and its OpenAI-compatible client already points at Ollama with a base-URL change.
5. **Weeks 6–8 — wire the evidence spine.** Every tutor turn, mastery update and grade writes an xAPI statement into `lrsql`.
6. **Weeks 8–10 — faculty acceptance.** Expose mastery estimates through `tutor-mcp` so a committee can see *why* the system judged a learner ready.

### 🔵 Why the statement log is the deliverable, not a nice-to-have

LATAM's regulatory position is the **least settled** of the four regions this base tracks — only Peru has an enacted AI law, Brazil's bill is pending. It is tempting to read that as "fewer obligations, ship faster". **That is the wrong read for a public university**, for two reasons this base has already measured: a public institution procures against *institutional* accountability rules that exist whether or not an AI statute does (Universidad de los Andes counted **716** AI-related instruments and rules in the region), and student data is **minors' and protected data under LGPD and its peers regardless**. The statement log is what lets the university answer "what did the system do to this student" in a region where nobody has yet told it which form that answer must take. 🟢 **Build it first and the eventual statute is a reporting change, not a re-architecture.**

### ⚠️ What this pattern does not claim

- **Neither Colombian row is production software.** `0★`, 4 and 151 commits, no external review, and `trabajo2-` in the name of one marks it as coursework. They are **prior art and an integration reference**. A proposal that lists them as dependencies is misreading this page; a proposal that says *"the Open edX integration boundary has a published reference implementation from a peer institution"* is reading it correctly — and that is worth real weeks.
- **The tutor quality comes from DeepTutor, not from the LATAM rows.** What the LATAM rows contribute is **placement, language and integration shape** — which is precisely what a localisation exercise usually gets wrong and what a client committee will probe hardest.
- **This is not a Moodle pattern.** Moodle dominates much of LATAM schooling, and its bridge field tops out at **27★** across seven MIT servers (**P8**). This pattern is for the Open edX half of the region, and the two are not interchangeable.

## P29 — Licence remediation first: turn LATAM's most-used education agents into a base you can actually build on (2–3 weeks of relationship work, then 6–8 weeks of product) 🟢 new at p664

🔵 **Why this pattern exists, and why it is unlike every other one in this file.** Every other pattern here starts from a permissively-licensed component and composes. This one starts from the measurement at **T32**: in Brazil, the education agent with **2,988 stars and 367 forks** (`digitalinnovationone/dio-agent`, built by **DIO**, a major Brazilian technology-education platform) has **no licence file at all**, while the three permissive LATAM rows on `agents/top.md` have **zero stars between them**. Adoption and licensability are inversely correlated. So the first move is not engineering — it is **getting a licence file upstreamed** — and it unlocks more value per week than any build on this page.

### The parts

| Layer | Component | Licence | Why this one |
|---|---|---|---|
| **The remediation target** | [`digitalinnovationone/dio-agent`](https://github.com/digitalinnovationone/dio-agent) | 🔴 **NONE** — no file at `LICENSE`, `LICENSE.md`, `LICENSE.txt` or `COPYING`; `gh api spdx = null` | **2,988★ / 367 forks**, pushed 2026-10-29. The most-adopted LATAM education agent this base has measured. 🔴 **Unusable as-is by anyone, including its own forkers.** This is the asset the pattern is about |
| **The fallback base** | [`ThallesYVasconcelos/Agente-Educacional`](https://github.com/ThallesYVasconcelos/Agente-Educacional) | 🟢 **MIT** (1,089 B) | 🟢 **The template that already works.** BNCC-keyed lesson plans (`EF01`–`EF04`), page-cited answers over MEC documents, LangGraph supervisor, ChromaDB + `bge-m3`, Ollama-first, FastAPI **MCP server**, Giskard evals. If remediation fails, this is where the build starts instead |
| School/fee system | [`academico-sis/academico`](https://github.com/academico-sis/academico) | 🟢 **MIT** (1,094 B) | **411★ / 153 forks**, Laravel + Filament. 🟢 **The permissive SIS** — enrolments, attendance, grades, invoicing can be extended and shipped **closed**. The GPL-2.0 alternatives (RosarioSIS, openSIS) cannot |
| Platform | `moodle/moodle` **or** `openedx/edx-platform` | GPL-3.0 / AGPL-3.0 | Whatever the client already runs. ⚠️ **Host, never derivative** |
| Model | Ollama + an open-weight model on client hardware | — | EduRAG already defaults this way; `gpt-4o-mini` is its fallback, not its base case |
| Evaluation | [`OpenEuroLLM/JudgeArena`](https://github.com/OpenEuroLLM/JudgeArena) | Apache-2.0 | Swappable **local** judge, so lesson-plan and answer quality is scored without student work leaving the building |
| Evidence | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | Apache-2.0 | **P17**'s spine. The `<1/3-of-PoCs-reach-P&L` problem is a measurement problem |

### How it wires together

1. **Weeks 1–2 — the licence conversation, and run `P27` on everything first.** Grade the grant of every candidate before writing a line (`P27` is the standing gate). Then approach DIO with a *specific, small ask*: add a permissive `LICENSE` file. Bring the argument, not the request — **367 forks are currently in an unlicensed position**, which is a liability for DIO's own community and a trivially fixable one. 🔵 **Budget this as relationship work with a named publisher, not as a legal negotiation.** The deliverable is a file.
2. **Week 2 — fork the decision, honestly.** If a licence lands, the 2,988-star base becomes composable and the pattern continues on it. **If it does not, drop it and continue on `Agente-Educacional`** — that branch is why this pattern has a fallback column and why it is not a gamble. ⚠️ Never ship a derivative of an unlicensed repository while waiting for an answer.
3. **Weeks 3–5 — harden the BNCC spine.** Take EduRAG's corpus design — BNCC + PCN + PNLD with **output keyed to official skill codes** — and make it the product's contract. A lesson plan that emits `EF02MA03` is auditable by a Brazilian school inspector in a way that a generated paragraph is not. Replace its Self-RAG check with `JudgeArena` running a local judge, so faithfulness scores become reproducible artefacts.
4. **Weeks 4–6 — attach the administrative half, closed.** Mount **Academico** for enrolment, attendance and invoicing. 🟢 **This is the licence-tier payoff of `664-C`:** MIT means the fee-and-enrolment surface can be re-branded and shipped as the client's own product. Filament makes the admin surface generated resource work rather than bespoke CRUD.
5. **Weeks 6–7 — platform bridge.** Expose the assistant to whatever LMS the client runs, via the MCP server EduRAG already ships. Keep the boundary at the process edge so the GPL/AGPL host never contaminates the derivative.
6. **Weeks 7–8 — the evidence spine and the strategy document.** xAPI statements into `lrsql`, and a formal AI strategy artefact. **UNESCO IESALC measured 87% of LATAM higher-education institutions using AI with only 26% holding a formal strategy** — the document is not overhead, it is the thing 74% of the market is missing and can cite a denominator for.

### 🔵 Why the licence ask is the highest-leverage two weeks in the region

A studio entering LATAM can spend those weeks building a tutor that will be the region's fourth `0★` permissive agent, or it can spend them converting a **2,988-star, 367-fork** community asset into something the whole region can build on — including the studio. The second outcome creates a reusable base, standing with a major Brazilian education publisher, and a public contribution that costs no engineering. It is also reversible at no cost: step 2 is a clean fork point.

### ⚠️ What this pattern does not claim

- **It does not claim DIO will say yes.** The pattern is built so that a no costs two weeks and loses nothing — the fallback base is already verified MIT and already does the job.
- **It does not claim `dio-agent` is good software.** Nobody on this base has assessed its quality; **it cannot be read as a dependency at all until it has a grant**, which is the point. Stars measure adoption, not fitness.
- **It does not generalise beyond Brazil on this evidence.** **T32** is measured on Brazilian repositories in one pass. The Spanish-language legs at p663 and p664 surfaced only research-scale addresses, so there was no high-adoption Spanish-speaking case to grade.
- **`Agente-Educacional` is `0★` prior art, not a product.** 46 commits, 0 forks, no external review, and its README names no institution — only an LLM course. The engagement is to harden it; the BNCC corpus design is what is being reused, not the code quality.

## P30 — The sovereign course AI an EU institution can authorise in one meeting (EMEA public higher education and K-12: 6–8 weeks) 🟢 new at p664

🔵 **Why this pattern exists now.** Until p664, every EMEA data-residency conversation on this base was answered with an *architecture* — "OpenTutor or wordlink can run with no egress" — and not with a **named reference deployment at a European institution**. `RUC-Digital-Media-Lab/RUCAI` (MIT, Roskilde University's Digital Media Lab, Denmark) changes that, and it does so on the one design detail that matters to a data-protection officer: **the teacher surface and the student surface are separate artefacts, with separate credentials and separate document scope.**

### The parts

| Layer | Component | Licence | Why this one |
|---|---|---|---|
| **Reference deployment** | [`RUC-Digital-Media-Lab/RUCAI`](https://github.com/RUC-Digital-Media-Lab/RUCAI) | 🟢 **MIT** (1,075 B) | 🟢 **The pattern's keystone, and the first EMEA agent row on `agents/top.md`.** FastAPI + PostgreSQL/pgvector, Ollama for embeddings *and* chat, async ingestion, source-traced answers, **password-protected student instances scoped to selected material**, `deploy/` scripts for an Ubuntu VM under systemd. ⚠️ `0★` pilot software; placement provisional (`664-H`) |
| Platform | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** (10,982 B) | The permissive institutional LMS, **and EMEA-built** — its grant payload names the OLAT Zentrum at the University of Zurich. ⚠️ Default branch `master` |
| Administration | [`academico-sis/academico`](https://github.com/academico-sis/academico) | 🟢 **MIT** | Enrolment, attendance, grades, invoicing — shippable closed |
| Retention | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | MIT | Ships **FSRS 4.5 in-tree** and runs with no API key. Supplies the scheduling primitive `RUCAI` has no opinion about (**T13**, **P6**) |
| Model | Ollama, on institution hardware — `bge-m3` + `gemma3:12b` are RUCAI's defaults and are env-var swappable | open weights | The whole premise. A procurement officer who has specified *"EU-hosted, open weights, local deployment"* — as TU Eindhoven's published tool guidance does — is describing this row |
| Evaluation | [`OpenEuroLLM/JudgeArena`](https://github.com/OpenEuroLLM/JudgeArena) | Apache-2.0 | 🟢 **Local judge backend**, from the EU's own publicly funded programme. The Annex III *"show me this is fit for assessment"* evidence, produced without egress |
| Evidence | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | Apache-2.0 | **P17**'s spine; the logging and human-oversight record the Act asks for |

### How it wires together

1. **Week 1 — `P27` on every component, then stand RUCAI up as-is.** 🔴 **Resolve the address before cloning:** RUCAI's own README Quick Start points at [`Frederikmh90/RUCAI`](https://github.com/Frederikmh90/RUCAI), the author's personal account, while this pattern cites the **organisation** address. Both resolve to the identical `HEAD ebdaae609e529cbe3c0696d7f74de18d8ebf605a` and the identical payload (`sha256₁₂ 2e9f1f76d670`), so there is no content risk — but `gh api` cannot see the personal one at all (`664-D`), so **automation must be written against the organisation address**. Its `deploy/` scripts give a working Ubuntu VM + pgvector + systemd install; the README is explicit that they are operational helpers, not a production installer.
2. **Week 2 — the demo that ends the egress argument.** Upload the client's own course readings; show answers with sources; publish a student instance; then **pull the network cable and do it again**. Everything runs against local Ollama. This is a half-day, and it is the meeting the whole engagement turns on.
3. **Weeks 2–4 — harden the two surfaces.** `RUCAI` is pilot software: the teacher auth is `.env` credentials with an optional users file. Replace it with the institution's SSO, put per-course retention on the uploaded-document store, and make the student-instance password policy institutional. 🔵 **Keep the two-artefact separation intact — it is the reason this row was filed.**
4. **Weeks 3–5 — attach platform and administration.** Mount it alongside **OpenOlat** (Apache-2.0, so the integration layer can be closed) and **Academico** for the administrative tier. The whole stack below the LMS is now permissive, which means the deliverable can be the client's branded product rather than a published derivative.
5. **Weeks 4–6 — add retention.** Lift **OpenTutor**'s in-tree FSRS to schedule review over the same ingested material. `RUCAI` answers questions; it does not decide *when* a learner should see something again.
6. **Weeks 5–7 — the Annex III file.** `JudgeArena` with a local judge scores answer groundedness against the uploaded corpus on a repeatable schedule; `lrsql` holds the statement log; the human-oversight record names who reviewed what. 🔵 **Date it to December 2027, not August 2026** — the Digital Omnibus moved stand-alone Annex III obligations, and most published guidance is stale (**T7**, **T15**, and the EMEA section of `intel/market.md`).
7. **Weeks 7–8 — dual UK/EU conformity, if the client sells into both.** The UK DfE's **generative AI product safety standards for education (January 2026)** are a product-standards regime, not a risk-classification one. The same evidence base satisfies both; nobody is currently selling that as one artefact.

### ⚠️ What this pattern does not claim

- **`RUCAI` is not production software and the pattern does not pretend otherwise.** `0★`, 0 forks, one author, ~46 commits, explicitly *"research software developed for a pilot teaching context"*. What it contributes is a **validated shape** and an institutional reference — the hardening in steps 3–4 is the actual work.
- **Its EMEA placement is provisional.** The MIT grant, the code and the architecture are first-hand; the Roskilde affiliation is not — `zenodo.org` and `cambridge.org` are unreachable from the session that filed it (`664-H`). **Read `DOI 10.5281/zenodo.20622874` before putting "Roskilde University" in a client deck.**
- **It does not make anyone AI-Act compliant.** It produces the artefacts an Annex III assessment needs. Classification, DPIA and conformity are the institution's, with counsel.
- **`JudgeArena` knows nothing about education.** 19★, general evaluation infrastructure, filed because education's gap is measurement and this is permissive measurement. It will not tell you whether a rubric is pedagogically sound.

## P31 — The teacher-side pilot that passes a data-governance review, and is graded by a rubric the client can read (K-12 and vocational, North America and EMEA: 4–6 weeks) 🟢 new at p665

🔵 **Why this pattern exists now.** Every teaching-assistant pilot this base has scoped has failed one of two reviews: the **data** review (what leaves the building) or the **evidence** review (how anyone knows the output is any good — **T10**, **T19**). Until p665 this base had no permissive component that answered the second one; `anthropics/k12-teacher-skills` ships `evals/` with its rubrics, and that turns a demo into an acceptance test.

### The parts

| Layer | Component | Licence | Why this one |
|---|---|---|---|
| **Teacher application** | [`SirhanMacx/Claw-ED`](https://github.com/SirhanMacx/Claw-ED) | 🟢 **MIT** (`1,078 B`) | 🟢 **The keystone.** Local-first: ingests the teacher's own PDF/DOCX/PPTX corpus, builds a **teaching-style profile**, emits a teacher DOCX + student DOCX + PPTX bundle. `clawed serve` gives a local dashboard and API; the provider is chosen in a wizard, so it can be pointed at Ollama. On PyPI at `9.18.2026.1` |
| **Pedagogy + the grading instrument** | [`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills) | 🟢 **Apache-2.0** (`11,357 B`) | Four skills — plan creation, **differentiation into below/at/above tiers**, lesson prep, and a formative check whose **distractors come from documented misconceptions** — plus `evals/`, the only eval framework on any shelf here. ⚠️ Its Learning Commons Knowledge Graph is a hosted connector outside the grant: **take the skills and the rubrics, not the graph** |
| **Diagnosis before instruction** | [`SenmuuuuW/universal-diagnostic-tutor-skill`](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) | 🟢 **MIT** (`1,102 B`) | The student-facing half, and the only row here that establishes the gap before teaching into it. Needs a host runtime |
| **Delivery into the incumbent LMS** | [`Menkoban/KI-Unterrichtswerkstatt`](https://github.com/Menkoban/KI-Unterrichtswerkstatt)'s Moodle pipeline | 🟢 **MIT** (`1,065 B`) | 🟢 **The reason this pattern clears the data review.** It emits a themed Moodle course as an **`.mbz` course backup** — a file, handed to whoever administers the Moodle. **No API token, no web service enabled, no plugin installed, no egress.** Compare `moodle-mcp` (27 ★), which needs live web-service credentials |
| **Model** | Ollama on school or district hardware | MIT | Makes “nothing leaves the building” a fact rather than a configuration |
| **Retention, if the pilot proceeds** | [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) + [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT | FSRS timing and BKT mastery behind MCP surfaces (**P6**, **T13**) |

### Wiring

1. **Week 1 — corpus and profile.** `clawed ingest ./lessons/` over one teacher's real material for one subject and one year group. The teaching-style profile is the deliverable of this week; nothing is generated for students yet.
2. **Week 2 — load the pedagogy, then write the acceptance test first.** Install `k12-teacher-skills` as a plugin into the same runtime. 🟢 **Lift `evals/` before generating anything** and agree its rubrics with the client's head of department as the pilot's pass/fail criteria. *This step is the pattern.* A pilot with a rubric agreed in week 2 is an evaluation; the same pilot with a rubric written in week 6 is a sales demo.
3. **Week 3 — generate, differentiate, check.** Produce lesson bundles for one unit; run `k12-lesson-differentiation` to get the three tiers; attach a `k12-check-for-understanding` item to each lesson. Every artefact is reviewed and edited by the teacher in Word and PowerPoint — the hand-edit is the feature, not a gap.
4. **Week 4 — deliver without touching the LMS's credentials.** Run the `KI-Unterrichtswerkstatt` Moodle pipeline over the unit and hand the administrator an `.mbz`. 🔵 **Record in the pilot report that no LMS web service was enabled** — this is the sentence that gets the second unit approved.
5. **Weeks 5–6 — score against the week-2 rubric and decide.** Add `universal-diagnostic-tutor-skill` only if the teacher-side scores pass; a diagnostic tutor in front of students is a different review.

⚠️ **Honest limits.** `Claw-ED` is self-labelled **Beta** at 64 ★ and `KI-Unterrichtswerkstatt` is a 1 ★ repository four days old at p665: both are **adopt-and-harden bases, not installs**, and the pilot must be staffed accordingly. The `.mbz` route is one-way — it ships a course in, it does not read grades back out; for that you still need `moodle-mcp` or LTI (**Pattern I** in `verticals/solutions.md`). And `k12-teacher-skills`' maths check-for-understanding is **maths**: for other subjects the rubric transfers, the misconception bank does not.

## P32 — Integrating with a European ministry's open stack without inheriting the EUPL (EMEA public sector: 10–14 weeks) 🟢 new at p665

🔵 **Why this pattern exists now.** p665 filed the first **EUPL** tier on `verticals/solutions.md`: seven `Opetushallitus` repositories in which the Finnish National Agency for Education runs its production learner stack in public. The reflex — fork it, brand it, host it — is the one move the licence punishes, because the EUPL counts making the Work available **online** as distribution. The pattern is the other move.

### The parts

| Layer | Component | Licence | Role |
|---|---|---|---|
| **Curriculum authority** | [`Opetushallitus/eperusteet`](https://github.com/Opetushallitus/eperusteet) | 🟠 **EUPL-1.1+** | The national core curriculum and qualification requirements as a **service with a data model**. Read it; do not vendor it |
| **Statutory learner plan** | [`Opetushallitus/ehoks`](https://github.com/Opetushallitus/ehoks) | 🟠 **EUPL-1.1+** | The personal competence development plan — what “personalisation” means in a European tender |
| **Intake / attainments / identity** | [`ataru`](https://github.com/Opetushallitus/ataru) · [`suorituspalvelu`](https://github.com/Opetushallitus/suorituspalvelu) · [`oppijanumerorekisteri`](https://github.com/Opetushallitus/oppijanumerorekisteri) | 🟠 **EUPL-1.2+ / 1.1+** | Applications, completed studies, learner identifier |
| **Your agent layer** | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) or [`RUC-Digital-Media-Lab/RUCAI`](https://github.com/RUC-Digital-Media-Lab/RUCAI) | 🟢 MIT | **Separate process, separate repository, separate grant.** Calls the services over HTTP; links no EUPL code |
| **Synchronous teaching** | [`apache/openmeetings`](https://github.com/apache/openmeetings) | 🟢 **Apache-2.0** | 🆕 Live classroom with whiteboard, recording and LMS plugins — the permissive answer where BigBlueButton is LGPL-3.0 |
| **Evaluation** | [`OpenEuroLLM/JudgeArena`](https://github.com/OpenEuroLLM/JudgeArena) | Apache-2.0 | Local judge backend from the EU's own programme — the Annex III fitness evidence |
| **Oversight record** | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | Apache-2.0 | xAPI statements as the human-oversight log (**P17**) |

### Wiring

1. **Draw the boundary before the first commit, and write it down.** The EUPL components run as **their own services**, deployed unmodified, reached only over their HTTP APIs. Your code lives in its own repository under MIT or Apache-2.0 and links **no** EUPL library. Process separation plus network calls is the boundary; a vendored module or a static link is not.
2. **Pin and document each service's version and payload.** Each repository's grant, bytes and branch go in the project's licence register — `eperusteet`/`oppijanumerorekisteri`/`organisaatio` serve the **identical** `632 B` payload (`sha256₁₂ 7c5df5c3eacb`), `ataru` is EUPL-**1.2**, `suorituspalvelu` is EUPL-1.2 **on `main` while the rest are on `master`**. ⚠️ `gh api` reports every one of the seven as `NOASSERTION`: **read the file, not the sidebar**.
3. **Model the curriculum from `eperusteet`, do not re-key it.** Ground the agent's retrieval in the authority's own structures (units, competence requirements, assessment criteria) so that “standards-aligned” is a join, not a claim.
4. **Treat `ehoks` as the personalisation contract.** Your agent proposes; the statutory plan records. Writing a proposal back into the plan is a governance decision, not an integration task — scope it as a separate phase with the ministry's own data controller.
5. **Fix anything you must fix upstream, in the open.** If a service needs a change, contribute it to the ministry's repository under its EUPL rather than carrying a private fork: the patch stays theirs, your stack stays permissive, and the procurement story improves.
6. **If a fork becomes unavoidable, re-scope commercially before writing code.** Then the EUPL travels with your hosted service, and the appendix's compatibility list (GPL-2.0, AGPL-3.0, EPL, MPL-2.0, LGPL, OSL, CeCILL, LiLiQ) is the only relicensing room you have. ⚠️ **It does not contain MIT or Apache-2.0.**

⚠️ **Honest limits.** This stack is **Finland's**, in Finnish, built for Finnish statute — the *shape* generalises to other EU member states, the data model does not. Star counts (0–11 ★) are meaningless here and are not an adoption signal either way: this is one deployment with a nation behind it. And none of these seven repositories contains any AI — **this pattern buys an integration surface and a licence posture, not a model.**

## P33 — A curriculum-grounded teacher agent that grounds against the *local* curriculum, not a PDF (LATAM or EMEA K-12: 8–10 weeks) 🟢 new at p666

🔵 **Why this pattern exists now.** Every curriculum-grounded agent on `agents/top.md` grounds itself in a *document*. p666 filed the two halves that make grounding an **integration** instead: [`Opetushallitus/eperusteet`](https://github.com/Opetushallitus/eperusteet) publishes the **national** core curriculum as a service, and [`Opetushallitus/eperusteet-ylops`](https://github.com/Opetushallitus/eperusteet-ylops) is how a school or municipality derives its **local** curriculum from it. On the LATAM side, [`GuilhermeScarpini/agente-bncc-professores`](https://github.com/GuilhermeScarpini/agente-bncc-professores) is a working **MIT** reference for binding generation to official skill codes.

### The parts

| Layer | Component | Licence | Role |
|---|---|---|---|
| Curriculum source (EMEA) | [`Opetushallitus/eperusteet-ylops`](https://github.com/Opetushallitus/eperusteet-ylops) + [`eperusteet`](https://github.com/Opetushallitus/eperusteet) | 🟠 **EUPL-1.1-or-later** | The local curriculum *and* the national core it derives from, as data with a model — **read over the API, never forked** (see `P32`) |
| Curriculum source (LATAM) | BNCC skill codes, bound as in [`GuilhermeScarpini/agente-bncc-professores`](https://github.com/GuilhermeScarpini/agente-bncc-professores) | 🟢 **MIT** (code) | The reference implementation of code-level binding: semantic search over skills → generation → editable questions → PDF. ⚠️ The BNCC texts carry their own terms, separate from this MIT code |
| Agent runtime | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 Apache-2.0 | Multi-mode delivery and the persistent learner model (`55,260★` at p666, payload `11,408 B` re-read and reproduced) |
| Lesson/assessment generation | [`DaRL-GenAI/instructional_agents`](https://github.com/DaRL-GenAI/instructional_agents) | 🟢 MIT | ADDIE multi-agent materials generation, driven **from the curriculum codes** rather than from a prompt |
| Assessment content | [`Opetushallitus/ludos`](https://github.com/Opetushallitus/ludos) | 🟠 EUPL-1.1-or-later | Where EMEA scope needs items an authority issued rather than items a model wrote |
| Local model runtime | [`ollama/ollama`](https://github.com/ollama/ollama) | 🟢 MIT | Keeps learner data on-premise — the usual condition in a public K-12 tender |

### Wiring

1. **Resolve the curriculum object first, before any model call.** EMEA: pull the municipality's local curriculum from `eperusteet-ylops` and its national parent from `eperusteet`. LATAM: load the BNCC skill set and index it exactly as `agente-bncc-professores` does. 🔴 **The deliverable is a *skill-code → content* mapping, not a chat log** — this is what makes output inspectable by someone who does not trust the model.
2. **Generate against the code, not the topic.** Drive `instructional_agents` with a skill code as the unit of work, so every generated plan, slide and item carries the code it serves. One code in, one traceable artefact out.
3. **Serve assessment from the authority where one exists.** In EMEA, prefer a `ludos` item over a generated one and record which you used; in LATAM, generate but keep the answer key editable, as `agente-bncc-professores` already does.
4. **Deliver through `DeepTutor`**, whose persistent learner model is keyed to the same curriculum codes, so "where is this student" is answerable in the inspector's vocabulary.
5. **Run the model locally via `ollama`** and keep the curriculum service calls read-only.

🔴 **The two things that make this fail, both stated up front.** (1) **Licence boundary**: the EUPL tier is copyleft whose *"Distribution or Communication"* reaches making the Work available online — so `eperusteet*` and `ludos` are **integrated against over the network and never vendored into your tree** (`P32` is the full shape). (2) **`agente-bncc-professores` is `0★`, `0` forks, one author** — a reference implementation of the binding, **not a maintained dependency**. Read it, reimplement the binding in your stack, credit it.

🟢 **Why the pattern is worth the weeks.** "Curriculum-aligned" is the claim every edtech vendor makes in a K-12 tender and almost none can evidence. This produces an artefact that is aligned **by construction and traceable code by code** — and in Finland's case, traceable to the ministry's own service.

## P34 — Early-childhood education: start from the national register, not from the learning app (EMEA public sector: 6–8 weeks to a scoped pilot) 🟢 new at p666

🔵 **Why this pattern exists now, and what it corrects.** `p660` went looking for permissive **early-years** assets and found *learning* tools — ScratchJr (BSD-3-Clause, dormant since 2022), the micro:bit stack (MIT). Useful, and not what an ECEC engagement is about. p666's org enumeration found [`Opetushallitus/varda`](https://github.com/Opetushallitus/varda) — **the national early-childhood-education register**: children, guardians, placements, staff, fee decisions, under **EUPL-1.1-or-later**, pushed `2026-10-27`.

### The parts

| Layer | Component | Licence | Role |
|---|---|---|---|
| Record system | [`Opetushallitus/varda`](https://github.com/Opetushallitus/varda) | 🟠 **EUPL-1.1-or-later** | Reference data model for national ECEC administration — placements, staffing ratios, fee decisions. Python/Django on PostgreSQL |
| Identity / organisation | [`Opetushallitus/organisaatio`](https://github.com/Opetushallitus/organisaatio) + [`oppijanumerorekisteri`](https://github.com/Opetushallitus/oppijanumerorekisteri) | 🟠 EUPL-1.1-or-later | Provider and learner identifiers — the join keys the register assumes |
| Agent layer (**your IP**) | [`CrewAI`](https://github.com/crewAIInc/crewAI) or [`LangGraph`](https://github.com/langchain-ai/langgraph) | 🟢 MIT | Placement-matching, staffing-ratio checks, fee-decision drafting, multilingual guardian correspondence |
| Model runtime | [`ollama/ollama`](https://github.com/ollama/ollama) | 🟢 MIT | On-premise — this is children's data under GDPR, and no other posture survives procurement |
| Learning layer, *if* the scope reaches it | [`scratchfoundation/scratchjr`](https://github.com/scratchfoundation/scratchjr) (BSD-3-Clause) / micro:bit MIT stack | 🟢 permissive | Added **after** the record layer, never instead of it. ⚠️ ScratchJr is dormant since `2022-07-22` — fork-and-own with a priced maintenance line (`660-I`) |

### Wiring

1. **Read `varda`'s data model as the specification.** The valuable artefact is not the Django code — it is the set of entities and obligations a national regulator considers complete for ECEC. Clone to read, scope from the model.
2. **Build the agents outside the EUPL boundary**, speaking to the register over its API. Placement matching and staffing-ratio compliance are the two with an immediate operational payoff.
3. **Keep every model call local via `ollama`**, and keep guardian-facing output drafted-not-sent: an ECEC fee decision is an administrative act.
4. **Only then** consider a learning layer, and treat ScratchJr's dormancy as a cost line rather than a footnote.

🔴 **The honest limit.** `varda` is `3★`. That is not adoption evidence and must not be sold as it: 🟢 **it has exactly one deployment and a country behind it.** For a ministry or municipal buyer that is the stronger fact; for a private buyer it is irrelevant, and this pattern is not for them.


## P35 — Make it stick, and prove it: the retention layer as a product, with the objective function as a client decision (any sector delivering training at scale: 6–8 weeks) 🟢 new at p667

🔵 **Why this pattern exists now.** Every engagement that generates learning material eventually meets the same question from the buyer: *does any of this actually stick, and how would we know?* Until p667 this base could only answer "use FSRS" — true, and a dead end, because it offered no trade-off and no citation. `p667` filed sixteen permissive rows that turn retention from a library choice into an **architecture choice** with four explicit decisions (see **T49**). This pattern is how you walk a client through those decisions in one engagement.

### The parts

| Layer | Component | Licence | Role |
|---|---|---|---|
| Scheduler — option A | [`open-spaced-repetition/fsrs-rs`](https://github.com/open-spaced-repetition/fsrs-rs) | 🟢 **MIT** | Optimises **predicted recall**. The incumbent, consumer-scale, already on `repos/foundations.md`. Pick this when the client's goal is retention at a fixed review budget. |
| Scheduler — option B | [`maimemo/SSP-MMC`](https://github.com/maimemo/SSP-MMC) | 🟢 **MIT** (`1,064 B`, read at p667) | Optimises **total review cost to reach a target recall**. Research code, lift the algorithm. Pick this when the client's goal is *time-to-competence* — certification, onboarding, compliance training. |
| The citation | [`Human-Centric-Machine-Learning/memorize`](https://github.com/Human-Centric-Machine-Learning/memorize) | 🟢 **MIT** (`190★`, `master`) | Code **and real data** for the **PNAS 2019** spaced-repetition optimisation result. This is what you put in the deck when the client asks who says so. |
| Item bank — adopt | [`nastaso/cloudcertprep`](https://github.com/nastaso/cloudcertprep) | 🟢 **MIT** (`246★`) | **1,469 real questions** (AWS CLF-C02, AIF-C01). Start here for any cloud/AI certification programme instead of writing items. |
| Item bank — generate | [`assafkip/claudemy`](https://github.com/assafkip/claudemy) + [`ahmedEid1/lumen`](https://github.com/ahmedEid1/lumen) | 🟢 MIT | Already on `agents/top.md`; both generate **with cited sources**, which is the provenance requirement this pattern depends on. |
| Card store (**the governance trick**) | [`kitschpatrol/yanki-obsidian`](https://github.com/kitschpatrol/yanki-obsidian) | 🟢 **MIT** (`200★`) | Cards live as **plain Markdown in a git repository** and sync to Anki. Generated items become reviewable in a pull request. |
| Delivery — hand-off | [`repeat-space/anki-apkg-export`](https://github.com/repeat-space/anki-apkg-export) | 🟢 **MIT** (`182★`) | Writes a `.apkg` **file** with no Anki installed — the artefact you attach to an email or ship in a build. |
| Delivery — in-product | [`olmps/memo`](https://github.com/olmps/memo) | 🟢 **BSD-3-Clause** (`1,870★`) | Flutter, so one codebase gives iOS + Android + desktop. ⚠ Pushed 2024-07-29 — **adopt the codebase, budget for the fork.** |
| Agent surface | [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) + [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 MIT | Already on `agents/top.md`: the agent drives scheduling and mastery through MCP rather than reimplementing either. |

### Wiring

1. **Make the client choose the objective function in week 1, on the record.** Recall-at-budget (FSRS) or cost-to-mastery (SSP-MMC). This is a business decision disguised as a technical one, and it determines everything downstream. Put the PNAS result in front of them so the choice is argued, not asserted.
2. **Decide adopt-or-generate for the item bank.** If the domain is a certification with a public blueprint, `cloudcertprep` proves the bank is cheap to adopt. If the domain is the client's own material, generate with `claudemy`/`lumen` — **and keep the citations**, because step 3 depends on them.
3. **Put the cards in git as Markdown via `yanki-obsidian`.** This is the step that makes the whole thing auditable: every generated item arrives as a diff with its source citation, a subject-matter expert approves it in a pull request, and the review history is the evidence artefact. **Do this before building any UI** — it costs a day and it is what survives a governance review.
4. **Wire the scheduler behind MCP** (`anki-mcp-server` for scheduling state, `tutor-mcp` for the mastery model) so the tutoring agent reads and writes the real schedule instead of carrying its own.
5. **Pick the delivery form last, from the hand-off requirement.** A `.apkg` file (`anki-apkg-export`) if the learner already uses Anki or the client wants an artefact; a branded app (`olmps/memo`, BSD-3) if it must carry the client's name; the vault-native route (`LearnKit`) if the cohort is technical and local-first matters.
6. **Instrument from day one and report against the chosen objective.** Whichever function was picked in step 1 is the one the final report must measure, or the engagement has no verdict.

🔴 **The honest limits.** `SSP-MMC` and `memorize` are **research code, not libraries** — you are lifting an algorithm and owning the implementation, which is real effort and should be a line in the estimate. `olmps/memo` has not been pushed since July 2024; adopting it means forking it. And none of this answers whether the *content* is any good — retention scheduling makes correct material stick and makes wrong material stick just as well, so step 2's citation requirement is load-bearing, not decoration.

🟢 **Why this sells.** It is the only pattern in this file where the governance answer and the product are the same artefact: a git repository of cited, expert-approved, version-controlled learning items with a published scheduler behind it. **T3** says governance is the buying trigger; this is the cheapest place in the whole stack to satisfy it.

## P36 — The licence-provenance triage, extended: rank the claim before you ask for the grant (1 day, as the front half of P27) 🟢 new at p667

🔵 **Why this exists.** `P27` established licence provenance as the first two weeks of any education engagement, on the correct principle that a licence **identifier is not a licence** and the payload must be read. `p667` adds the case `P27` does not cover: **what to do when there is no payload at all.** This happens constantly outside English-language open source — `p666` measured 4 of 6 non-English candidates with no grant payload, and `p667` measured 3 of 6 — and the right response is not a uniform "reject", because the three forms it takes are worth very different things.

### The triage

| What you find | Specimen measured at p667 | Verdict | What to do |
|---|---|---|---|
| **Complete grant text inlined in the README**, no `LICENSE` file | [`MiradoAndreas/learning-plateform-ai`](https://github.com/MiradoAndreas/learning-plateform-ai) — verbatim canonical MIT in a fenced block, and `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `LICENCE`, `LICENCE.md`, `COPYING` **all 404** | 🟢 **Usable.** The grant exists and is complete; only its location is non-standard. | Normalise the grant text against the canonical template (wrap-insensitive). If it matches, proceed — and open a one-line pull request adding `LICENSE`. This is the cheapest licence remediation there is. |
| **A prose sentence naming a licence** — and check whether it is a *split* grant | [`JRS1986/KISchule`](https://github.com/JRS1986/KISchule) — *"Texte: CC BY-SA 4.0. Code: MIT."* | 🟠 **More restrictive than it looks.** | Work out which half you actually want. This repository is almost entirely Markdown lesson material, so **the asset is CC BY-SA** — share-alike — and only the build script is MIT. A search leg reported it as "MIT-licensed". |
| **A shields.io badge** | [`AiltonRock22/ia-professores`](https://github.com/AiltonRock22/ia-professores) — `![Licença](…badge/licença-MIT-blue.svg)` linked to `LICENSE`; `LICENSE`, `LICENSE.md`, `LICENCA`, `LICENCA.md` all **404** | 🔴 **Worthless as a grant.** No licence text exists anywhere in the repository. | Do not use it, and do not record it as MIT. Ask the maintainer to add a payload; until they do there is nothing to rely on. **This is the mechanism behind search engines' false licence reports** — the summariser reads the badge. |
| **A short bespoke payload** — read it, do not classify it | [`learningfactory-io/ki-werkstatt`](https://github.com/learningfactory-io/ki-werkstatt) — `LICENSE` serves `200` at `413 B` | 🔴 **Proprietary.** *"Alle Rechte vorbehalten… jede kommerzielle Nutzung… nicht gestattet."* | A served `LICENSE` is **not** evidence of a grant — this one is a reservation of rights. Any payload under ~800 B is bespoke by definition and must be read in full by a human. |

### Wiring it into the P27 gate

1. **`git ls-remote --symref` first**, for existence and the **real default branch** — 27% of the addresses p667 verified are not on `main`, and reading a payload at the wrong ref is how a licence gets mis-recorded.
2. **Try the payload at 8 filenames** (`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `LICENCE`, `LICENSE-MIT`, `COPYING`, `LICENSE.rst`, `license`) at that ref. A 404 on all eight means **run this triage**, not "unlicensed".
3. **If a payload exists, grade it on the title line and record the bytes** — never on body text. `p666` showed a body-text classifier grades the full EUPL as AGPL-3.0 off its compatibility appendix. **Abstention is the correct output** for an unrecognised title.
4. **Decompose any non-zero residual before calling it a mutation.** `p667` found `telekom/ki-in-schulen` at `+123`, which the predictor flagged `BODY-MUTATED` and which decomposes exactly into a URL line, a blank line, a **second copyright holder** and 1 B of re-wrap — the grant text is verbatim MIT. A positive residual means *look*, not *reject*.
5. **Strip leading blank lines and uniform indentation before any byte comparison.** `campfirium/foliole` reads canonical Apache-2.0 `+1` on one prepended newline; `microsoftarchive/Learn-LTI` is uniformly indented four spaces, which defeats a copyright-line detector anchored at byte 0.

🟢 **Why a client pays for this.** It is one day, it runs before any architecture work, and it is the difference between a shipped product and a renegotiation. The failure it prevents is specific and common: **a repository that advertises MIT in its README badge, and has no licence at all.**

## P37 — AI in the system of record, without inheriting the system of record's licence (any region, K-12 or small HE, 6–8 weeks)

🔵 **What this is for.** A client runs a school or a small institution on an open source SIS and wants AI in it — predicted grades, attendance triage, a parent-facing enquiry agent, report-card drafting. `T50` is why this is not the usual engagement: on this layer the adoption is copyleft (`rosariosis` GPL-2.0 at `652★`, `openSIS-Classic` GPL-2.0 at `349★`) and the only permissive system of record is `academico-sis/academico` (MIT, `411★`). The default move — fork the thing the client already runs and add AI to it — produces a derivative of a GPL-2.0 work, and on this layer that work holds student records, so the question is never hypothetical.

🟢 **The pattern: put the agent *beside* the SIS, not inside it, and make the process boundary the licence boundary.**

**Weeks 1–2 — gate, before any code.** Run **`P36`** (rank the licence claim) then **`P27`** (the licence-provenance gate) against the client's actual deployed tree, not the upstream repo. Byte-read the grant at the real default ref — `667-K` and `668-H` between them give four claim-forms, and two of this pass's three specimens were on `master`, not `main`. Deliverable: the client's own dependency graph with a licence per node, per `T16`, because **the licence unit is the graph, not the repository**.

**Weeks 2–4 — the boundary.** Stand the agent up as a separate service that talks to the SIS over its HTTP API and its database read replica. Nothing links against SIS code; nothing is compiled into it. Concretely:
- **Orchestration:** `LangGraph` (MIT) — the reference stack per `T2`, with the policy nodes `P6` uses for multi-jurisdiction rules.
- **SIS bridge:** the SIS's own REST API. `rosariosis` and `openSIS-Classic` both expose one; `academico` (MIT) can be linked against directly if the client is on it, and that is the one case where this pattern collapses into the cheap version — **check first, because it changes the estimate by two weeks.**
- **Retention/scheduling,** where the use case is revision or intervention timing: the layer `p667` filed and `T49` describes — FSRS and the `SSP-MMC` scheduler, permissive, already in production elsewhere.
- **Serving:** `Ollama` or `vLLM` on client infrastructure, for the data-residency reason `P30` sets out; this layer holds student records, so a hosted API is a governance conversation, not a technical default.

**Weeks 4–6 — the teacher-facing half.** Per `T35` and the 2026 consensus, ship to **teachers first**, not students: draft-and-confirm only, with the human edit as the committed action. `P31` is the pilot shape that passes a data-governance review; reuse its rubric rather than inventing one.

**Weeks 6–8 — the compliance artefact.** Produce the deployer documentation the client is actually obliged to hold. **EMEA:** AI used for student evaluation is Annex III high-risk, now applying from **`2027-12-02`** per the Digital Omnibus (`T7`, `T15`) — but **Article 50 transparency applies from `2026-08-02` and Article 4 AI literacy has applied since `2025-02-02`**, so two of the three obligations are live today and only the heavy one moved. **North America:** state-level, not federal; if the deployment touches grading, discipline or IEP decisions, check the jurisdiction first — DC's 2026-27 policy bans AI from exactly those four uses. **APAC:** South Korea's AI Basic Act (in force `2026-01-22`) and Vietnam's Law on AI (`2026-03-01`, with an 18-month education transition) are both binding and neither is education-specific (`T12`). **LATAM:** governance is the gap, not adoption — 87% of surveyed institutions use AI and 26% have a strategy, so the artefact itself is often the differentiator.

🔴 **When not to sell this.** If the client's requirement is genuinely *inside* the SIS — a field on a form, a column in the gradebook — this pattern does not deliver it, and `T50` option (a) or (b) is the honest answer. Say which one and what it costs. 🔵 **The failure mode this pattern exists to prevent is a fork of a GPL-2.0 student-records system shipped as a client-owned product, which is a licence problem discovered at the end of the engagement rather than in week one.**

## P38 — The multi-campus rollout: one agent layer, many institutions, per-tenant configuration (any region, higher education consortia or multi-campus groups, 8–10 weeks) 🟢 new at p669

🔵 **What this is for.** A client is not one institution. It is a university system, a consortium, a national network or a private group with several campuses — each with its own LMS tenant, its own API-token policy, its own data-governance committee, and frequently a *different LMS*. Every pattern above this one assumes a single institution, and the gap shows up immediately in delivery: the pilot works at campus A and the second deployment is a rewrite.

🟢 **Why it is in this file now, and what it rests on.** `669-R2` found the missing piece by accident, while reading repository text for a different purpose. [`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server) ships **six named institution presets in its own README** — `--purdue`, `--suny`, `--tudelft`, `--cuny`, `--leiden`, `--mcgill` — spanning **three countries and two regions**. That is not a location fact, it is an **architecture fact: the bridge is multi-tenant by construction**, and no other LMS bridge on `agents/top.md` declares per-institution configuration at all. 🔴 **It is also why that row is deliberately left `Global (unplaced)`** — placing a six-country switch list in one region would have been wrong, and `669-D` records the refusal.

**The pattern: make the tenant a configuration object, and the LMS bridge the only tenant-aware layer.**

**Weeks 1–2 — enumerate the tenants before writing anything.** For each campus, record four things and nothing else: which LMS and version, who issues API tokens and under what policy, which jurisdiction's rules bind it, and whether student data may leave the campus. 🔵 **The token policy is the one people skip and the one that stops rollouts.** `vishalsachdev/canvas-mcp`'s README exists partly to document this: it names **University of Illinois Urbana-Champaign** as an institution where self-service API access is unavailable *to everyone*, students and staff alike. A rollout plan that assumes per-user tokens dies at the first campus like that. Budget an admin-issued service-token conversation per tenant.

**Weeks 2–4 — the bridge layer, one adapter per LMS, tenant as a flag.**
- **Brightspace / D2L:** [`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server) — adopt its preset mechanism as the house pattern rather than inventing one, and extend the list; also [`AnonymousOnyx22/brightspace-d2l-mcp`](https://github.com/AnonymousOnyx22/brightspace-d2l-mcp) as a second reading.
- **Canvas:** [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (MIT, `317★`, **North America** — documentary) for the read/write surface, and [`boyuchengz/canvas-mcp`](https://github.com/boyuchengz/canvas-mcp) (MIT, `119★`) where the governance committee requires **read-only**. Diff the two per tenant; do not assume one.
- **Moodle:** the MCP field on `agents/top.md` — dominant in LATAM and much of EMEA, so in a mixed group this adapter is usually the second one built, not the last.
- **Open edX:** `TutorIA` as an XBlock/plugin, which lands *inside* the platform's own course surface rather than beside it.
- **Standards fallback, for any tenant whose LMS has no bridge:** [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (MIT) for LTI 1.3 launch and [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) where the surface is notebooks. **LTI is the lowest common denominator across every LMS in this list and it is the reason a mixed-LMS group is tractable at all.**

**Weeks 4–6 — one agent layer, zero tenant knowledge.** Orchestration on `LangGraph` (MIT) per `T2`, with the tutor chosen from the shelf by use case — `DeepTutor` (Apache-2.0) where a persistent learner model is the point, `Bloom` for the fastest demo, `OATutor` (MIT) where the client wants explainable mastery estimates. 🔵 **The rule that makes this a rollout instead of N projects: the agent layer receives a tenant context object and never branches on institution.** Everything institution-specific — base URL, token source, field mappings, retention rules — lives in the bridge's per-tenant config. Per `669-R2`, that is exactly the seam the Brightspace bridge already cuts.

**Weeks 6–8 — per-tenant evidence, one schema.** [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) (Apache-2.0) as the LRS with [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec), **one statement schema across all campuses with the tenant on the actor or context**. This is what lets the group compare campuses, which is usually the real reason a consortium is buying centrally — and per `T10` and `T19` the evidence layer is the sector's weak point, so it is also the differentiator.

**Weeks 8–10 — the per-jurisdiction compliance split, which is where a multi-region group costs more than a single-country one.** A mixed group does **not** have one compliance posture: **North America** — California's `AB 1159` prohibits training on student data, so a tenant there constrains the *architecture*, not just the paperwork; several states now mandate district-level policies (`SB 720` and others). **EMEA** — student evaluation is Annex III high-risk from **`2027-12-02`** after the AI Omnibus (`T7`, `T15`), with the UK on DfE/Ofqual national rules in the meantime. **APAC** — Korea's AI Basic Act is in force; Vietnam's law names education; **Australia is Threshold Standard 5.2 and TEQSA guidance, *not* a filing mandate** — see the rejection on `intel/market.md`, reproduced by four independent leg runs. **LATAM** — no binding education-AI statute in most countries, so the constraint is the institution's own framework, which per UNESCO IESALC only `26%` of them have. 🔵 **Scope the compliance artefact per jurisdiction and reuse the technical work across all of them; that ratio is the commercial case for doing it centrally.**

🔴 **When not to sell this.** If the group has one LMS, one jurisdiction and one data-governance authority, this is over-engineered — use `P37` or the single-institution patterns and keep the tenant object out. And if the campuses are genuinely autonomous buyers, the per-tenant conversations in weeks 1–2 are a sales process, not a sprint: say so before the timeline is agreed.
