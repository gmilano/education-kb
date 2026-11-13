---
industry: education
region: Global
updated: 2026-11-13
---

# Compose patterns — education

Six concrete recipes. Each names the actual repos, the license consequence, how
the pieces wire together, and a rough build estimate. All components were
license-verified on 2026-11-13 (see `agents/top.md` and `repos/foundations.md`).

**The rule all six follow:** keep the AI layer permissive (MIT/Apache/BSD),
mount it into the copyleft platform over **LTI 1.3** or **MCP**, and emit
**xAPI** or **Caliper** events. Never fork the LMS.

---

## P1 — Compliance-safe practice tutor (North America, restrictive states)

**Problem:** the client wants an AI tutor, but Texas HB 2400 bars AI from
delivering direct classroom instruction and New York A 9190 would limit
classroom AI to grade 9+.

**Wiring:**
1. **Mastery/progression engine — outside the model.**
   `pykt-team/pykt-toolkit` (MIT) for knowledge tracing, or
   `CAHLR/OATutor` (MIT) if Bayesian Knowledge Tracing over an existing item
   bank is enough.
2. **Item bank and renderer.** `Khan/perseus` (MIT) for real exercise
   rendering and authoring.
3. **Agent role, scoped deliberately to practice and feedback.** Adapt
   `HKUDS/DeepTutor` (Apache-2.0) — use its learner-model and
   learning-path machinery, disable instruction delivery; the human teacher
   delivers instruction.
4. **LMS mount.** LTI 1.3 tool provider into Canvas; for agent-side access use
   `vishalsachdev/canvas-mcp` (MIT, 102 tools).
5. **Telemetry.** Emit Caliper (`1edtech/caliper-spec`) — the common choice in
   North American higher ed — plus an audit log of every agent action with the
   grade level and state policy applied.
6. **Policy gate.** A configuration layer keyed to state: grade floor,
   instruction-delivery off, logging retention, FERPA/COPPA posture.

**License outcome:** entire AI layer MIT/Apache; Canvas stays separate behind
LTI, so AGPL does not reach the deliverable.

**Estimate:** 8–10 weeks. **Sells because** it is the tutor that is legal where
a general tutor is not.

---

## P2 — EU AI Act high-risk conformity layer for assessment AI (EMEA)

**Problem:** the institution already runs AI that touches assessment or
admissions. That is Annex III high-risk; obligations for stand-alone Annex III
education systems are reported moved to **2027-12-02** by Regulation (EU)
2026/1744, transparency duties from August 2026, and emotion recognition in
education has been banned since February 2025. Verify current dates on EUR-Lex
before committing to a timeline.

**Wiring:**
1. **Inventory and classify.** Enumerate every AI touchpoint in
   `moodle/moodle` (GPL-3.0) or `ILIAS-eLearning/ILIAS` (GPL-3.0) — plugins,
   proctoring, grading assists, early-warning models.
2. **Human-oversight layer.** Interpose a review step on every
   consequential decision: `ArnaudGuiovanna/tutor-mcp` (MIT) is the
   reference design — auditable engine governs progression, model only creates
   and explains.
3. **Evaluation harness.** `kaushal0494/AITutor-EvalKit` (MIT) for pedagogical
   effectiveness; `pykt-team/pykt-toolkit` (MIT) for quantitative learner-model
   validation. Conformity requires evidence the system performs as claimed.
4. **Sovereign inference.** Self-hosted open weights — the Council of the EU's
   2026 position explicitly calls reduced dependency on non-European AI tools
   critical for education and training. No frontier API egress.
5. **Logging and documentation.** xAPI event stream plus a technical
   documentation pack: risk management, data governance, oversight procedures.
6. **AI literacy deliverable.** Build training against the **European
   Commission / OECD AI literacy framework for primary and secondary schools**
   published 2026-06-18, satisfying the Article 4 literacy duty.

**License outcome:** Moodle/ILIAS untouched (no fork); all added components
MIT/Apache.

**Estimate:** 12–16 weeks. **Highest-value regulated education work globally.**

---

## P3 — Moodle MCP server (Global, greenfield asset)

**Problem:** Moodle is the most-deployed LMS in the world and has **no
significant MCP server**. Canvas has `canvas-mcp` (MIT, 324 stars, 102 tools);
Open edX has only `openedx-mcp` (AGPL-3.0, 3 stars).

**Wiring:**
1. **Model on the proven one.** `vishalsachdev/canvas-mcp` (MIT) is the
   reference for tool surface and granularity — courses, assignments,
   submissions, grades, enrolments, announcements, rubrics.
2. **Build against Moodle's web services REST API** (not the database), as an
   **MIT-licensed standalone MCP server**. Calling a GPL-3.0 platform's
   documented HTTP API from a separate process keeps the server permissive.
3. **Role scoping from day one.** Student, teacher, and admin tool sets with
   separate credentials — `openedx-mcp` demonstrates the staff/superuser facade
   pattern.
4. **Pair with an agent.** `HKUDS/DeepTutor` (Apache-2.0) or `ai-shifu/ai-shifu`
   (Apache-2.0) for scripted, author-controlled teaching flows.
5. **Emit xAPI** for every agent action.

**License outcome:** MIT server, reusable across every Moodle engagement in
EMEA, LATAM and APAC.

**Estimate:** 5–7 weeks for a solid tool surface. **Build once, bill many.**

---

## P4 — Institutional AI governance package (LATAM, productized)

**Problem:** UNESCO IESALC: 87% of LATAM higher-ed institutions use AI, 26%
have any framework, **9% evaluate it**, and **55% of universities have no AI
budget**. The Digital Education Council's 2026 LATAM survey reports 92% of
students and 79% of faculty actively using AI. The need is real and the money is
thin, so the package must be cheap to run.

**Wiring:**
1. **Discovery.** Map shadow AI use against the institution's
   `moodle/moodle` (GPL-3.0), `chamilo/chamilo-lms` (GPL-3.0) or
   `francoisjacquet/rosariosis` (GPL-2.0) footprint.
2. **Evaluation spine — this is the differentiator.**
   `kaushal0494/AITutor-EvalKit` (MIT) for pedagogical quality plus
   `pykt-team/pykt-toolkit` (MIT) for learning-gain measurement. Moves the
   client from the 91% who do not evaluate into the 9% who do.
3. **Low-cost delivery.** Self-hosted open weights, and
   `learningequality/kolibri` (MIT, offline-first) wherever connectivity is
   unreliable. No per-seat frontier spend.
4. **Localized content generation.** `satvik314/educhain` (MIT) for
   Spanish/Portuguese material aligned to national exams (ENEM, ICFES, PAES,
   SEP); `oppia/oppia` (Apache-2.0) for interactive lessons with misconception
   handling.
5. **Telemetry and reporting.** xAPI stream into a dashboard the rectorate can
   actually read.
6. **Policy and training artifacts.** Written framework plus teacher
   enablement, referencing the UNESCO IESALC **Observatory on AI in Education
   for Latin America and the Caribbean** (launched April 2026) and the
   Ceibal (Uruguay) national model.

**License outcome:** fully permissive AI layer; platforms untouched.

**Estimate:** 6–8 weeks per institution after the first; **the first build is
the product**.

---

## P5 — Multi-jurisdiction compliance architecture (APAC)

**Problem:** a regional university group or edtech vendor simultaneously faces
Korea's AI Basic Act (in force January 2026, education = high-impact),
Vietnam's AI law (in force March 2026, education high-risk, **pre-deployment
registration and human oversight required**), Australian TEQSA generative-AI
risk plans, Chinese content-labelling and algorithm registration, and the EU AI
Act for anything sold into Europe.

**Wiring:**
1. **One policy-enforcement layer, per-jurisdiction configuration.** Wrap every
   agent call in a gate that resolves tenant jurisdiction, then applies:
   registration status, human-oversight requirement, content labelling,
   logging retention, data residency.
2. **Auditable progression engine.** `ArnaudGuiovanna/tutor-mcp` (MIT) —
   per-tool permissions and an engine that governs progression outside the
   model, which is what "human oversight" means in evidence terms.
3. **Agent layer, regionally sourced and permissive.**
   `THU-MAIC/OpenMAIC` (MIT, 43.4k) for multi-agent classroom, or
   `HKUDS/DeepTutor` (Apache-2.0, 58.6k) for lifelong tutoring. Both are
   APAC-origin and permissively licensed — localize rather than rebuild.
4. **Sovereign deployment.** Self-hosted open weights in-region, answering
   localization mandates (e.g. Malaysia's sovereign-cloud framing) directly.
5. **Evidence pack per jurisdiction.** Vietnam's registration and Korea's
   high-impact designation both require documentation, not just controls.

**License outcome:** MIT/Apache throughout.

**Estimate:** 12–14 weeks. **The compliance layer is the product**; the tutor is
the demo.

---

## P6 — Agent-assisted grading and feedback (Global, unbuilt space)

**Problem:** no dominant open-source grading agent exists in any region.
Grading is the single largest teacher workload, and every policy framework
treats automated grading as consequential.

**Wiring:**
1. **Substrate.** `jupyter/nbgrader` (BSD-3-Clause, 1.4k) for programming and
   data-science courses — assignment release, collection, autograding. Real,
   deterministic correctness checks run first.
2. **Agent layer on top, for what autograding cannot do:** qualitative
   feedback, partial credit rationale, misconception identification. Use
   `satvik314/educhain` (MIT) for rubric-aligned feedback generation.
3. **Never let the model be the gradebook.** Deterministic score from nbgrader;
   the agent proposes qualitative feedback and flags for human review. This is
   what keeps it lawful under Texas HB 2400-style instruction limits and EU
   high-risk assessment rules.
4. **Quality measurement.** `kaushal0494/AITutor-EvalKit` (MIT) to check
   feedback actually helps, plus inter-rater agreement against human graders
   before any rollout.
5. **Mount and report.** LTI 1.3 into Moodle/Canvas/Open edX; grade passback
   via LTI AGS; xAPI/Caliper telemetry.
6. **For non-notebook courses,** `Khan/perseus` (MIT) item types or
   `oppia/oppia` (Apache-2.0) explorations provide the structured response data
   that makes agent feedback tractable.

**License outcome:** BSD/MIT/Apache throughout.

**Estimate:** 8–10 weeks for one discipline. **Open space** — there is no
incumbent open-source grading agent to compete with.

---

## Component quick reference

| Need | Use | License |
|---|---|---|
| Lifelong tutoring agent | `HKUDS/DeepTutor` | Apache-2.0 |
| Multi-agent classroom | `THU-MAIC/OpenMAIC` | MIT |
| Governed progression / ITS over MCP | `ArnaudGuiovanna/tutor-mcp` | MIT |
| Bayesian mastery modelling | `CAHLR/OATutor` | MIT |
| Deep knowledge tracing | `pykt-team/pykt-toolkit` | MIT |
| Content/question generation | `satvik314/educhain` | MIT |
| Scripted teaching flow | `ai-shifu/ai-shifu` | Apache-2.0 |
| Canvas agent access | `vishalsachdev/canvas-mcp` | MIT |
| Pedagogical evaluation | `kaushal0494/AITutor-EvalKit` | MIT |
| Exercise rendering | `Khan/perseus` | MIT |
| Interactive lessons | `oppia/oppia` | Apache-2.0 |
| Offline-first delivery | `learningequality/kolibri` | MIT |
| Notebook autograding | `jupyter/nbgrader` | BSD-3-Clause |
| Offline field assessment | `getodk/collect` | Apache-2.0 |
| Learning analytics events | xAPI / `1edtech/caliper-spec` | spec |
| LMS mount (all platforms) | LTI 1.3 | spec |

**Do not put these in a client stack:** `CaviraOSS/PageLM` (non-OSI community
license, commercial use needs written permission), `Nutlope/llamatutor` (no
license file), `GarethManning/education-agent-skills` (CC BY-SA 4.0 — content,
not software).
