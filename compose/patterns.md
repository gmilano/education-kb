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

## 🔴 What these patterns deliberately avoid

- **No pattern forks a GPL or AGPL platform.** Ten of fourteen verified platforms are copyleft; forking one for a managed service is the single most expensive mistake available in this industry. **P7 is the exception that proves the rule** — it can own its platform layer precisely because Kolibri is MIT.
- 🟢 **Two exclusions from the previous version of this list are withdrawn.**
  - `OpenEduCat` was excluded as **HTTP 404**. The project is live at **`openeducat/openeducat_erp`** (LGPL-3.0, 905★, default branch `19.0`); only the published address was dead. It is now the recommended base when a client needs a full education ERP, and LGPL-3.0 is a better licensing position than the `frappe/lms` (AGPL-3.0) substitute that was recommended in its place.
  - `tutor-mcp` was excluded at **0 stars**. That measured `kvnloo/tutor-mcp`, which is a **fork**; the upstream `ArnaudGuiovanna/tutor-mcp` has **96★ / 13 forks** and is the backbone of **P6**.
- **Still excluded:** `awesome-ai-llm4education` (**no licence**, 221★) and `eduadapt-ai` (**no licence**, 26★), both previously published here as MIT and neither of which is. Added to the exclusion list at p651: `GarethManning/education-agent-skills` (949★ but **CC BY-SA 4.0** — ShareAlike, so a derivative skill library cannot be proprietary); `virtualryder/edu-ai-agents` (4★ and a **modified MIT payload with the limitation-of-liability paragraph removed**); `mthatipamula/educational-assessment-ai-agent-platform`, `luffycodes/Tutorbot-Spock` and `Micel357/Edu-mentor-AI` (**no licence file**); `CodeBreez/collejo` (MIT but **archived read-only since 2024-05-16**).
- **No pattern includes proctoring or emotion recognition.** Emotion recognition in schools is banned in the EU; exam monitoring is high-risk there and, since 22 January 2026, student assessment in K-12 is high-impact under South Korea's AI Basic Act with fines expected from around January 2027. No permissively-licensed open source option was found in any case.

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
