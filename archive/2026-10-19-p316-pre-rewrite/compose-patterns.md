---
industry: education
region: Global
updated: 2026-10-19
---

# Compose patterns — education

**Pass 315 · 2026-10-19.** Five recipes. Every repo named below was verified first-hand this pass
(see `agents/top.md`, `repos/foundations.md`, `verticals/solutions.md`). Timings are engagement
estimates, not measurements.

---

## P1 — Curriculum-grounded lifelong tutor

**For:** any institution that wants a tutor answering from *its* material, with a learner model that
survives across sessions. The default education engagement.

**Stack**
- `HKUDS/DeepTutor` (Apache-2.0, 41.7k ★) — tutoring agent and lifelong learner state
- `HKUDS/LightRAG` (MIT, 40.2k ★) — retrieval over the client's curriculum
- `huggingface/smolagents` (Apache-2.0, 29.9k ★) — the auditable agent loop for custom tools
- `dmitry-viskov/pylti1.3` (MIT) — LTI 1.3 tool so the tutor launches from the client's LMS
- Client LMS (`moodle/moodle` GPL-3.0 or `openedx/openedx-platform` AGPL-3.0) — **unmodified**

**Wiring**
1. Ingest course material (syllabi, slides, past assignments) into LightRAG; one index per course,
   one namespace per institution.
2. Run DeepTutor as a service; pin the version — it released v1.6.15 on 2026-10-19 and moves weekly.
3. Expose the service as an LTI 1.3 Advantage tool via `pylti1.3`. The LMS launches it; the LMS is
   never patched. **This is what keeps Globant's code off the GPL/AGPL side of the line.**
4. Return grades/progress through LTI AGS so the gradebook stays authoritative.
5. Persist learner state in Globant-owned storage, keyed by the LTI `sub` claim — never by email.

**Licence note:** every component Globant writes or links sits on the far side of the LTI boundary,
so the GPL-3.0/AGPL-3.0 platform never reaches it. Say this explicitly in the SOW.

**Estimate:** 8–10 weeks to a pilot with one faculty.

---

## P2 — Mastery-and-retention engine (the "actually pedagogical" tutor)

**For:** clients who will be asked by an accreditor or a ministry *why* the tutor showed what it
showed. Pattern P1 answers content; this one answers pedagogy.

**Stack**
- `CAHLR/OATutor` (MIT, 268 ★) — Bayesian Knowledge Tracing; mastery estimates and hint sequencing
- `open-spaced-repetition/fsrs-rs` (BSD-3-Clause, 447 ★) — review scheduling, embeddable, no Anki
- `satvik314/educhain` (MIT, 387 ★) — generate the item bank (MCQs, lesson plans) the above consume
- `HKUDS/DeepTutor` (Apache-2.0) — conversational surface
- `Ebimsv/AITutorAgent` (MIT, 15 ★) — **read only**, for its tutorial → Q&A → evaluation loop shape

**Wiring**
1. Educhain generates candidate items from the curriculum; a human SME approves into the bank. The
   approval step is not optional — Educhain is 387 ★ and slow-moving, so treat its output as a
   draft.
2. OATutor's BKT tracks per-skill mastery from responses; it, not the LLM, decides what comes next.
3. fsrs-rs schedules *when* a mastered skill is reviewed again.
4. DeepTutor renders the interaction; the LLM explains, the BKT decides. **Keep that separation —
   it is the whole defensibility argument.**

**Estimate:** 6–8 weeks on top of P1; 10–12 weeks standalone.

---

## P3 — Policy-gated deployment layer (North America, dated demand)

**For:** US districts and systems facing Ohio's 2026-07-01 framework requirement, Idaho SB 1227, or
any of the >28 states with K-12 AI guidance. **Sell this before selling a tutor.**

**Stack**
- Any tutor from P1/P2 as the governed subject
- `jupyterhub/jupyterhub` (BSD-3-Clause, 8.4k ★) — provenance-capturing compute for student work
- `jupyter/nbgrader` (BSD-3-Clause, 1.4k ★) + `ucbds-infra/otter-grader` (BSD-3-Clause, 161 ★) —
  autograding with a recorded execution trail
- `dmitry-viskov/pylti1.3` (MIT) — identity and grade passback from the LMS of record

**Wiring**
1. Put every agent call behind a gateway that logs: prompt, retrieved sources, response, learner id,
   timestamp, model version. This log *is* the deliverable — it satisfies "educator supervision" and
   "no high-stakes automated decisions" in one artefact.
2. Hard-gate high-stakes actions (final grades, placement, discipline) behind human approval.
   Idaho's "AI cannot replace human teachers" is a code-level constraint, not a policy sentence.
3. Run assessment in JupyterHub; grade with nbgrader/otter-grader so the submission's execution
   history is evidence. This is the **process-evidence** answer to integrity — there is no credible
   open source AI-detector to buy instead.
4. Generate the parent-disclosure and retention report from the same log. FERPA/COPPA retention
   windows are configuration, not a rewrite.

**Estimate:** 4–6 weeks; deployable before the tutor it governs.

---

## P4 — EU AI Act provider package (EMEA)

**For:** EMEA engagements where Globant builds the tool and therefore becomes the **provider** under
the AI Act, while the school is only the deployer. Annex III lists education as high-risk.

**Stack**
- P1 tutor, plus:
- `openfun/richie` (MIT, 316 ★) — MIT portal/catalogue in front of an AGPL Open edX back end
- `overhangio/tutor` (AGPL-3.0, 1.1k ★) — reproducible Open edX deployment, in-region
- `learningequality/kolibri` (MIT, 1.2k ★) — where on-device/offline delivery is required
- Self-hosted models for data residency

**Wiring**
1. **Ship Article 50 transparency now.** It applied from 2026-08-02 and was *not* deferred: AI
   interaction disclosure in the UI and machine-readable marking of generated content. This is the
   smallest, most immediate billable item in EMEA.
2. Build the high-risk conformity file *during* development, not after: technical documentation,
   risk management, data governance, logging, human oversight, post-market monitoring. The deadline
   moved to **2027-12-02** under Regulation (EU) 2026/1744 — against 12–18 month public procurement
   cycles, conformity-ready is what wins 2026–27 bids.
3. **No emotion recognition anywhere in the stack.** Banned in schools since Feb 2025 — no
   engagement-detection from webcam, no affect scoring. Check this in code review.
4. Keep Open edX unmodified behind Richie; AGPL's network clause reaches modified platforms, and
   not modifying it is the cheapest compliance decision available.

**Estimate:** 10–12 weeks including the conformity file.

---

## P5 — Offline-first national curriculum delivery (APAC, and the India mandate specifically)

**For:** India's compulsory AI + Computational Thinking rollout for Classes 3–8 from 2026-27 across
32,900 CBSE schools — 50 h/yr for Classes III–V, 100 h/yr for VI–VIII — where **64.7% of schools
have computers and 63.5% have internet.** A cloud tutor does not serve this brief.

**Stack**
- `learningequality/kolibri` (MIT, 1.2k ★) — offline-first delivery; MIT, so AI can embed directly
- `Sunbird-Ed/SunbirdEd-portal` (MIT, 41 ★) — India's national stack; the integration target
- `satvik314/educhain` (MIT, 387 ★) — bulk generation of curriculum-aligned items, SME-reviewed
- `open-spaced-repetition/fsrs-rs` (BSD-3-Clause, 447 ★) — scheduling that works with no network
- `microsoft/ai-agents-for-beginners` (MIT, 77.5k ★) — white-labelled teacher-training base

**Wiring**
1. Generate and SME-approve the item bank **centrally and online**; this is the only step that needs
   connectivity at scale.
2. Package approved content into Kolibri channels; distribute by sync server, USB or sneakernet.
   Kolibri is MIT, so an embedded on-device scheduler or small local model is licence-clean.
3. Run FSRS scheduling fully on-device; sync learner state opportunistically, not continuously.
4. Integrate with Sunbird for national reporting — verify the wider `Sunbird-Ed` org's component
   repos before scoping; the portal is one piece of a larger stack.
5. Deliver teacher training from the `ai-agents-for-beginners` curriculum. 71% of US teachers lack
   AI training and the India rollout has no trained cohort either — **training is the engagement,
   not an add-on.**

**Estimate:** 12–14 weeks for a state-level pilot.

---

## Pattern selection by region

| Region | Lead with | Why |
|---|---|---|
| North America | **P3**, then P1/P2 | Dated legal requirements (Ohio 2026-07-01, Idaho SB 1227); governance is the budgeted line |
| EMEA | **P4** | Provider-side conformity under Annex III; Article 50 already live |
| APAC | **P5** (India), P1 + labelling (China), P1 (Japan) | Curriculum mandate + infrastructure gap; China needs labelling/registration at the generation step; Japan has the fewest blockers |
| LATAM | **P1 or P2 grounded in Latam-GPT** | No binding framework to win on; sovereignty and Spanish/Portuguese quality are the differentiators |

**No pattern here is LATAM-only or North-America-only.** P1 and P2 are the portable core; P3, P4 and
P5 are the regional wrappers that make them biddable.
