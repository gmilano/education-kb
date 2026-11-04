---
industry: education
region: Global
updated: 2026-11-04
---

# 🧩 Composition patterns — Education

> Concrete recipes. Every component named below was verified on 2026-11-04 (existence + licence payload + stars where shown) and appears in `agents/top.md`, `repos/foundations.md` or `verticals/solutions.md`.
> **The licence rule that governs all five patterns:** keep proprietary work in the agent layer (MIT/Apache) and in Apache-2.0 XBlocks. Never fork a GPL/AGPL platform for a managed service.

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

## Choosing a pattern

| Client situation | Pattern | Why |
|---|---|---|
| Already on Canvas | **P1** | No migration, no licence exposure, fastest demo |
| Already on Moodle (LATAM/EMEA) | **P2** | Meets the dominant installed base; local models for residency |
| MOOC / corporate academy on Open edX | **P3** | Only licence-safe Open edX shape |
| Wants explainable mastery (STEM) | **P4** | BKT + pyKT; budget content authoring |
| Uses AI already, controls nothing | **P5** | Sell governance first, then P1–P4 |
| Pilot must prove an outcome | **P6** | Permissive end to end, retention measurable, no per-review inference cost. Attach it to any other pattern |
| Connectivity cannot be assumed | **P7** | The only pattern with no copyleft component anywhere, and the only one that works offline |
| Needs a full education ERP (finance, HR) | **P2 + OpenEduCat** | `openeducat/openeducat_erp` (LGPL-3.0, 905★) on Odoo. ⚠️ default branch is `19.0` and `20.0` exists — resolve it |
| Already on Moodle and wants a **real agent**, not just REST glue | **P8** | Names the bridge P2 left as a placeholder. `G36maid/moodle-mcp` (MIT, 27★) — adopt and harden; **price the hardening, it is not P1** |
| Data residency, offline, **or** must stay off the graded system of record (Korea, Vietnam) | **P9** | Curriculum knowledge in the weights, FP8 on one GPU, no egress. 🔴 Resolve the OmniEdu weight licence first |
| Has a funded AI-literacy mandate (Canada, Saudi, Kenya, EU Art. 4) | **P10** | The deliverable is curriculum and teacher capacity, not software. MIT base at 41.1k★ permits a closed client derivative |

## 🔴 What these patterns deliberately avoid

- **No pattern forks a GPL or AGPL platform.** Ten of fourteen verified platforms are copyleft; forking one for a managed service is the single most expensive mistake available in this industry. **P7 is the exception that proves the rule** — it can own its platform layer precisely because Kolibri is MIT.
- 🟢 **Two exclusions from the previous version of this list are withdrawn.**
  - `OpenEduCat` was excluded as **HTTP 404**. The project is live at **`openeducat/openeducat_erp`** (LGPL-3.0, 905★, default branch `19.0`); only the published address was dead. It is now the recommended base when a client needs a full education ERP, and LGPL-3.0 is a better licensing position than the `frappe/lms` (AGPL-3.0) substitute that was recommended in its place.
  - `tutor-mcp` was excluded at **0 stars**. That measured `kvnloo/tutor-mcp`, which is a **fork**; the upstream `ArnaudGuiovanna/tutor-mcp` has **96★ / 13 forks** and is the backbone of **P6**.
- **Still excluded:** `awesome-ai-llm4education` (**no licence**, 221★) and `eduadapt-ai` (**no licence**, 26★), both previously published here as MIT and neither of which is. Added to the exclusion list at p651: `GarethManning/education-agent-skills` (949★ but **CC BY-SA 4.0** — ShareAlike, so a derivative skill library cannot be proprietary); `virtualryder/edu-ai-agents` (4★ and a **modified MIT payload with the limitation-of-liability paragraph removed**); `mthatipamula/educational-assessment-ai-agent-platform`, `luffycodes/Tutorbot-Spock` and `Micel357/Edu-mentor-AI` (**no licence file**); `CodeBreez/collejo` (MIT but **archived read-only since 2024-05-16**).
- **No pattern includes proctoring or emotion recognition.** Emotion recognition in schools is banned in the EU; exam monitoring is high-risk there and, since 22 January 2026, student assessment in K-12 is high-impact under South Korea's AI Basic Act with fines expected from around January 2027. No permissively-licensed open source option was found in any case.

## 🔴 Resolve the licence of the *tree*, not the repository — four live cases

Reading `LICENSE` is necessary and not sufficient. Four components these patterns use carry obligations that their repository badge does not mention, and all four were read from bytes or from a manifest field verbatim on 2026-11-04.

| Component | Badge | Actual obligation in the tree | What to do in a pattern |
|---|---|---|---|
| **OpenMAIC** (P10, P3) | MIT | `packages/mathml2omml` is **LGPL-3.0-or-later** (7,652 B), `"workspace:*"` in the root manifest, built as step one of `build:packages` | Keep it dynamically replaceable with source offered, or excise the MathML→OOXML export path. Design-time decision |
| **OmniEdu weights** (P9) | Apache-2.0 *(code)* | **No named grant for the weights.** README: *"Model weights and third-party datasets and benchmarks retain their respective licenses."* Backbones are Qwen | Read the Hugging Face card before scoping. Gate zero of P9 |
| **open-moodle** (not used) | MIT | Depends on **PyMuPDF (AGPL-3.0)** | Excluded from P8 for this reason. An AGPL dependency in a network-served agent defeats out-of-tree containment |
| **csmediapro/moodle-mcp-server** (not used) | "free use, no closed-source repackaging" | Plain **AGPL-3.0**, 34,523 B, plus paid Premium Plugins | Excluded from P8. Marketing language is not a licence; read the payload |

**The check to run once per engagement, in week one:** read `LICENSE` from bytes; then read `package.json`, `pyproject.toml` and `Cargo.toml` for every bundled or workspace component; then, for any model, read the weight card separately from the code licence. Four of the five grant-defect classes this KB has catalogued pass a licence-badge check.

## 🔴 Resolve the branch before you clone — four live cases on this shelf

Every pattern above assumes you check out the right thing, and on this shelf the default branch is frequently not it:

| Repo | Default branch | What goes wrong |
|---|---|---|
| `openeducat/openeducat_erp` | **`19.0`** | A hardcoded `main`/`master` builds nothing; a hardcoded `19.0` silently keeps building the old major, because `20.0` already exists |
| `francoisjacquet/rosariosis` | **`mobile`** | A default clone gives you the mobile branch, not the release line, among 44 branches that are otherwise version numbers |
| `learningequality/kolibri` | **`develop`** | A default clone gives you development code; deploy from `release-v0.19.x` or `release-v0.20.x` |
| `GeminiLight/gen-mentor` | `main`, and that is the problem | `main` is a browser-only Next.js demo app. **The multi-agent Python implementation its WWW '25 paper describes is on branch `v0.1-demo`** — so the default gives you a demo, not the evaluated system |

The fix is one command, and it belongs in any ingest or deployment script rather than in a human's memory:

```bash
git ls-remote --symref https://github.com/<owner>/<repo> HEAD   # returns the real default branch
```

Then read the README for which branch carries the artefact you actually want — resolving the default is necessary and, as `gen-mentor` shows, not always sufficient.
