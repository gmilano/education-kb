---
industry: education
region: Global
updated: 2026-10-19
---

# Compose patterns — education

**Pass 316 · 2026-10-19.** Seven recipes. Every repo named below is in `agents/top.md`,
`repos/foundations.md` or `verticals/solutions.md`, with the pass in which it was read first-hand
recorded there. Timings are engagement estimates, not measurements.

Changes this pass: **P2 is rebuilt around `tutor-mcp`**, which ships the mastery-and-retention
engine this pattern used to assemble by hand. **P6 is new** — the Ed-Fi/OneRoster data spine.
**P7 is new** — grade-band gating, which US K-12 districts now require.

---

## P1 — Curriculum-grounded lifelong tutor

**For:** any institution that wants a tutor answering from *its* material, with a learner model that
survives across sessions. The default education engagement.

**Stack**
- `HKUDS/DeepTutor` (Apache-2.0, 41.7k ★) — tutoring agent and lifelong learner state
- `HKUDS/LightRAG` (MIT, 40.2k ★) — retrieval over the client's curriculum
- `huggingface/smolagents` (Apache-2.0, 29.9k ★) — the auditable agent loop for custom tools
- `dmitry-viskov/pylti1.3` (MIT, 138 ★) — LTI 1.3 tool so the tutor launches from the client's LMS
- Client LMS — `moodle/moodle` (GPL-3.0), `openedx/openedx-platform` (AGPL-3.0) or
  `instructure/canvas-lms` (AGPL-3.0), **unmodified**

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

**Competitive note, new this pass:** on Canvas, **Instructure's Project Athena (announced
2026-07-22) does this natively.** Do not sell P1 alone into a Canvas account. Sell P1 + P2 (the
pedagogy Athena does not do) or P1 + P3 (the audit trail the district must buy anyway).

**Estimate:** 8–10 weeks to a pilot with one faculty.

---

## P2 — Mastery-and-retention engine (the "actually pedagogical" tutor)

**For:** clients who will be asked by an accreditor or a ministry *why* the tutor showed what it
showed. P1 answers content; this one answers pedagogy. **This is the pattern that survives contact
with Canvas's native AI.**

**Stack**
- `ArnaudGuiovanna/tutor-mcp` (MIT, 52 ★, 467 commits) — **the engine.** Skill graph, Bayesian
  Knowledge Tracing, FSRS scheduling, prerequisite gating, cross-session narrative memory, as an
  MCP server. SQLite over stdio locally; PostgreSQL over HTTPS + OAuth in the institutional profile
- `CAHLR/OATutor` (MIT, 268 ★) — reference BKT implementation and hint sequencing; use to validate
  tutor-mcp's mastery estimates against a published academic implementation
- `open-spaced-repetition/fsrs-rs` (BSD-3-Clause, 447 ★) — standalone FSRS where you need
  scheduling outside the MCP server (offline clients, batch jobs)
- `satvik314/educhain` (MIT, 387 ★) — generate the item bank the engine consumes
- `HKUDS/DeepTutor` (Apache-2.0) — conversational surface
- `GeminiLight/gen-mentor` (CC0-1.0, 135 ★, WWW '25 oral) — **read, don't depend.** The
  peer-reviewed multi-agent ITS architecture to cite when a ministry asks for provenance

**Wiring**
1. Stand up tutor-mcp in the institutional profile (PostgreSQL, HTTPS, OAuth). Define the subject's
   skill graph — concepts and prerequisites — with the client's SMEs. **This is the engagement's
   real intellectual work and it is not LLM work.**
2. Educhain generates candidate items from the curriculum; a human SME approves into the bank.
   The approval step is not optional — Educhain is 387 ★ and slow-moving; treat output as a draft.
3. Let the engine decide: BKT tracks per-skill mastery, prerequisite rules gate progression, FSRS
   schedules review. **The LLM explains; the engine decides what comes next.** That separation is
   the entire defensibility argument and tutor-mcp enforces it architecturally.
4. Put DeepTutor (or any MCP-capable client) on the front as the conversational surface.
5. Validate against OATutor on a sample cohort before go-live — two independent BKT implementations
   agreeing is an evidence artefact an accreditor will accept.

**The integration caveat that decides scope:** tutor-mcp's README names **no LTI, SCORM or xAPI
support.** It is MCP-only. For an institutional deployment you write the LTI 1.3 wrapper yourself
with `pylti1.3` and bridge it to the MCP server. Budget that bridge explicitly — it is the single
most-repeated unbudgeted item in this sector (see trend 6 in `intel/trends.md`).

**Estimate:** 6–8 weeks on top of P1; 10–12 weeks standalone. Add 2–3 weeks for the LTI bridge.

---

## P3 — Policy-gated deployment layer (North America, dated demand)

**For:** US districts and systems facing Ohio's 2026-07-01 framework requirement, Idaho SB 1227,
Oklahoma/Maryland human-oversight rules, or any of the 134 bills across 31 states in 2026.
**Sell this before selling a tutor.**

**Stack**
- Any tutor from P1/P2 as the governed subject
- `jupyterhub/jupyterhub` (BSD-3-Clause, 8.4k ★) — provenance-capturing compute for student work
- `jupyter/nbgrader` (BSD-3-Clause, 1.4k ★) + `ucbds-infra/otter-grader` (BSD-3-Clause, 161 ★) —
  autograding with a recorded execution trail
- `dmitry-viskov/pylti1.3` (MIT) — identity and grade passback from the LMS of record
- P7's gating layer (below) — grade-band enforcement is now part of the same deliverable

**Wiring**
1. Put every agent call behind a gateway that logs: prompt, retrieved sources, response, learner id,
   timestamp, model version. This log *is* the deliverable — it satisfies "educator supervision" and
   "no high-stakes automated decisions" in one artefact.
2. Hard-gate high-stakes actions (final grades, placement, discipline) behind human approval.
   Idaho's "AI cannot replace human teachers", and Oklahoma's and Maryland's reported bars on
   high-stakes AI decisions, are code-level constraints, not policy sentences.
3. Run assessment in JupyterHub; grade with nbgrader/otter-grader so the submission's execution
   history is evidence. This is the **process-evidence** answer to integrity — there is no credible
   open source AI-detector to buy instead, and there should not be (trend 9).
4. Generate the parent-disclosure and retention report from the same log. FERPA/COPPA retention
   windows are configuration, not a rewrite.

**Estimate:** 4–6 weeks; deployable before the tutor it governs.

---

## P4 — EU AI Act provider package (EMEA)

**For:** EMEA engagements where Globant builds the tool and therefore becomes the **provider** under
the AI Act, while the school is only the deployer. Annex III lists education as high-risk —
admissions, learning-outcome evaluation, student level placement, exam/behaviour monitoring.

**Stack**
- P1 tutor, plus:
- `openfun/richie` (MIT, 316 ★) — MIT portal/catalogue in front of an AGPL Open edX back end
- `overhangio/tutor` (AGPL-3.0, 1.1k ★) — reproducible Open edX deployment, in-region
- `learningequality/kolibri` (MIT, 1.2k ★) — where on-device/offline delivery is required
- Self-hosted models for data residency

**Wiring**
1. **Ship Article 50 transparency now.** It applied from 2026-08-02 and was *not* deferred: AI
   interaction disclosure in the UI and machine-readable marking of generated content. The smallest
   immediate billable item in EMEA.
2. **Check the 2026-12-02 prohibitions before that date** — new bans (non-consensual intimate
   imagery, CSAM) take effect six weeks from this pass. For an education product this is a
   content-safety and image-generation audit, and it is not deferred.
3. **Article 4 is now an obligation to take AI-literacy measures for staff** (relaxed, not removed).
   A documented staff-training programme discharges it, and the client needs one anyway (trend 1).
4. Build the high-risk conformity file *during* development: technical documentation, risk
   management, data governance, logging, human oversight, post-market monitoring. The deadline moved
   to **2027-12-02** under Regulation (EU) 2026/1744 — against 12–18 month public procurement
   cycles, conformity-ready is what wins 2026–27 bids. The deferral moved the date, not the
   substance.
5. **No emotion recognition anywhere in the stack.** Banned in schools since Feb 2025 — no
   engagement-detection from webcam, no affect scoring. Check this in code review.
6. Keep Open edX or Canvas unmodified behind Richie; AGPL's network clause reaches modified
   platforms, and not modifying it is the cheapest compliance decision available.

**Reuse note:** this conformity file is portable to Brazil. PL 2338/2023 is risk-based and passed
the Senate in December 2024 — see P-selection below.

**Estimate:** 10–12 weeks including the conformity file.

---

## P5 — Offline-first national curriculum delivery (APAC, Africa, and the India mandate)

**For:** India's compulsory AI + Computational Thinking rollout for Classes 3–8 from 2026-27 across
32,900 CBSE schools — 50 h/yr for Classes III–V, 100 h/yr for VI–VIII — where **64.7% of schools
have computers and 63.5% have internet.** A cloud tutor does not serve this brief. **Also the right
pattern for Sub-Saharan Africa**, where the strongest evidence base for low-resource AI tutoring
exists (World Bank Edo State, Nigeria; EIDU in Kenya, ~400k children) and Kenya's DigiSchool has
put over 1 million tablets into primary schools.

**Stack**
- `learningequality/kolibri` (MIT, 1.2k ★) — offline-first delivery; MIT, so AI can embed directly
- `Sunbird-Ed/SunbirdEd-portal` (MIT, 41 ★) — India's national stack; the integration target
- `zijinz456/OpenTutor` (MIT, 145 ★) — **new this pass.** Local-first adaptive workspace, 10+ LLM
  providers, runs on-device; the tutor shell when nothing may leave the building
- `satvik314/educhain` (MIT, 387 ★) — bulk generation of curriculum-aligned items, SME-reviewed
- `open-spaced-repetition/fsrs-rs` (BSD-3-Clause, 447 ★) — scheduling that works with no network
- `microsoft/ai-agents-for-beginners` (MIT, 77.5k ★) — white-labelled teacher-training base

**Wiring**
1. Generate and SME-approve the item bank **centrally and online**; the only step needing
   connectivity at scale.
2. Package approved content into Kolibri channels; distribute by sync server, USB or sneakernet.
   Kolibri is MIT, so an embedded on-device scheduler or small local model is licence-clean.
3. Use OpenTutor as the on-device adaptive surface where a local LLM is available; fall back to
   pre-generated Kolibri content where it is not. **Design for both — device capability varies
   school to school in exactly these markets.**
4. Run FSRS scheduling fully on-device; sync learner state opportunistically, not continuously.
5. Integrate with Sunbird for national reporting — verify the wider `Sunbird-Ed` org's component
   repos before scoping; the portal is one piece of a larger stack.
6. Deliver teacher training from the `ai-agents-for-beginners` curriculum. **Training is the
   engagement, not an add-on** — and per trend 1, delivering training that *lands* is the hard part.

**Estimate:** 12–14 weeks for a state-level pilot.

---

## P6 — The roster and SIS data spine (North America) — NEW

**For:** any US district or state engagement, under any of the patterns above. An agent that does
not know who the student is, what they are enrolled in and which teacher owns them is a demo.
Earlier passes of this KB called this bespoke integration work; **it is not, and that was a
search error — see `repos/foundations.md`.**

**Stack**
- `Ed-Fi-Alliance-OSS/Data-Management-Service` (Apache-2.0, 12 ★, 1,105 commits) — the Ed-Fi API
  platform, successor to the ODS/API platform
- `Ed-Fi-Alliance-OSS/edfi-oneroster` (Apache-2.0, 6 ★, 151 commits) — serves a **OneRoster 1.2**
  API from data in an Ed-Fi ODS
- `dmitry-viskov/pylti1.3` (MIT) — LTI identity at launch, reconciled against the roster
- Whichever tutor and governance layer from P1/P2/P3

**Wiring**
1. Stand up the Data-Management-Service against the district's Ed-Fi ODS. **Pin to a commit —
   neither repo publishes GitHub releases.**
2. Expose OneRoster 1.2 through `edfi-oneroster` as the single read interface your agents use for
   enrolment, section and teacher-of-record data. One contract, not one per SIS vendor.
3. At LTI launch, resolve the `sub` claim to the roster identity; everything downstream — learner
   state, mastery estimates, audit log entries — keys off that resolved id, never off an email.
4. Feed the teacher-of-record relationship into P3's human-approval gates. "Educator supervision"
   has to name an actual educator, and this is where that name comes from.
5. Keep the roster read-only from the agent side. Writes go back through the LMS gradebook over
   LTI AGS, not into the SIS.

**The standards argument to put in the proposal:** 1EdTech's 2026 position is that interoperability
is the precondition for AI, naming CASE, Edu-API and OneRoster as the standards that give an AI
system trustworthy institutional context. This pattern is that position implemented on Apache-2.0
code.

**Scope limit, stated plainly:** Ed-Fi is a North American standard in practice. It is not a route
into EMEA, APAC or LATAM rostering, and nothing equivalent was found for those regions. Everywhere
else, SIS sync is still bespoke.

**Estimate:** 3–5 weeks alongside P1 or P3; longer if the district's ODS is not already populated,
which is a data-quality project and should be priced as one.

---

## P7 — Grade-band gating and teacher-only mode (North America K-12) — NEW

**For:** districts that restrict rather than adopt. **New York City runs a one-year moratorium on
student-facing AI through eighth grade; Katy ISD (Texas) is banning generative AI chatbots for
K-6.** A product that cannot be switched off for a grade band cannot be bid into these districts —
and they are not outliers.

**Stack**
- P6's roster spine — grade level is a roster attribute, and it is the only trustworthy source
- P3's logging gateway — the gate is enforced and evidenced at the same chokepoint
- Any P1/P2 tutor as the gated subject

**Wiring**
1. Resolve grade level from the roster at launch (P6), not from a profile field a student can edit.
2. Enforce three modes at the gateway, per grade band, as policy configuration rather than code:
   **student-facing**, **teacher-facing only** (the teacher may use the agent *about* the student's
   work; the student never sees it), and **off**.
3. Default to the most restrictive mode for any learner whose grade level does not resolve. Fail
   closed.
4. Emit the mode into every audit-log entry. "Prove no eighth-grader interacted with the AI" then
   becomes a query, which is exactly the question a district under a moratorium will ask.
5. Expose the configuration to district administrators. The policy will change mid-contract; make
   that a settings change, not a release.

**Why this is worth building once:** it is small, every K-12 district in a restricting state needs
it, and teacher-facing-only mode **keeps the engagement alive in a district that has banned
student-facing AI.** That is the difference between a lost account and a smaller one.

**Estimate:** 2–3 weeks on top of P3 and P6.

---

## Pattern selection by region

| Region | Lead with | Why |
|---|---|---|
| North America | **P3 + P6**, then P7 where restricted, then P1/P2 | Dated legal requirements (Ohio 2026-07-01, Idaho SB 1227, 134 bills/31 states); governance is the budgeted line and the roster spine is now open source |
| EMEA | **P4** | Provider-side conformity under Annex III; Article 50 live, 2026-12-02 prohibitions imminent, 2027-12-02 the real deadline |
| EMEA — Gulf | **P1/P2 with Arabic-first localisation** | UAE ~28% of GCC edtech, National AI Strategy 2031; incumbents (Alef, Classera, Abwaab) are proprietary and buying integration, not platforms |
| EMEA — Africa | **P5** | Strongest low-resource evidence base in the world (Edo State, EIDU); DigiSchool tablets are installed hardware needing content |
| APAC | **P5** (India), P1 + labelling (China), P1 (Japan) | Curriculum mandate plus infrastructure gap; China needs labelling/registration at the generation step; Japan has the fewest blockers |
| LATAM | **P2 grounded in Latam-GPT**, with P4's artefacts ported | The 92%-usage / 30%-satisfaction gap is a delivery problem, which P2 answers; Brazil's PL 2338 is risk-based, so the EU conformity file transfers |

**No pattern here is LATAM-only or North-America-only.** P1 and P2 are the portable core; P3, P4,
P5, P6 and P7 are the regional wrappers that make them biddable — and P6 and P7, both new this
pass, are the two that turn a North American pilot into a district-wide contract.
