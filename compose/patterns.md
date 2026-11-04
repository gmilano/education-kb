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
        ▼
[Mastery model — pyKT (MIT, 457★) / BKT]
        ▼
[Delivery — Richie portal (MIT) · WhatsApp · avatar (Open TutorAI CE, BSD-3) · LMS-native]
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

## Choosing a pattern

| Client situation | Pattern | Why |
|---|---|---|
| Already on Canvas | **P1** | No migration, no licence exposure, fastest demo |
| Already on Moodle (LATAM/EMEA) | **P2** | Meets the dominant installed base; local models for residency |
| MOOC / corporate academy on Open edX | **P3** | Only licence-safe Open edX shape |
| Wants explainable mastery (STEM) | **P4** | BKT + pyKT; budget content authoring |
| Uses AI already, controls nothing | **P5** | Sell governance first, then P1–P4 |

## 🔴 What these patterns deliberately avoid

- **No pattern forks a GPL or AGPL platform.** Nine of ten verified platforms are copyleft; forking one for a managed service is the single most expensive mistake available in this industry.
- **No pattern depends on `OpenEduCat`** — previously published here as an education-ERP base, now **HTTP 404**. The education-ERP slot has no verified open source occupant; `frappe/lms` (AGPL-3.0) is the nearest substitute.
- **No pattern depends on `tutor-mcp`** (MIT, **0 stars**), `awesome-ai-llm4education` (**no licence**, 221★) or `eduadapt-ai` (**no licence**, 26★). The latter two were previously published here as MIT and are not.
- **No pattern includes proctoring or emotion recognition.** Emotion recognition in schools is banned in the EU; exam monitoring is high-risk there. No permissively-licensed open source option was found in any case.
