---
industry: education
region: Global
updated: 2026-10-19
---

# Compose patterns — education

**Pass 319 · 2026-10-19.** Ten recipes. Every repo named below is in `agents/top.md`,
`repos/foundations.md` or `verticals/solutions.md`, with the pass in which it was read first-hand
recorded there. Timings are engagement estimates, not measurements.

**Changes this pass. P10 is new and it is the most defensible pattern in this file**: the verified
curriculum spine, built on Brazil's `bncc-dev` stack, with a published number behind it — curriculum
hallucination **31.9% ungrounded, 2.3% when the model queries the verified dataset over MCP**. It
comes with a port variant for India, where the same artefact does not exist and a 2026-27 mandate
is arriving without it.

**P1 gains a "prove it teaches" stage**, because the evaluation layer this KB declared missing for
four passes now exists and its finding is that **LLM-judged helpfulness is not a pedagogy signal**
(`agents/top.md`). **P7 gains a per-pupil opt-out, an approval queue and a decision log**, which US
statute has turned from nice-to-have into bid-qualifying. **P5 gains two more permissive offline
components.** And the cross-cutting LTI risk now has a real alternative rather than an index —
`tsugiproject/tsugi`, Apache-2.0, 4,011 commits.

Carried from pass 317: **P8** — the permissive-LMS build on OpenOLAT (Apache-2.0), the first
pattern in this KB that does *not* require an LTI boundary. **P1 gains a FERPA-filtered retrieval
step.** **P4 gains the 2026-12-02 watermarking date and ports to South Korea**, whose Framework Act
on AI has been in force since 2026-01-22. **Every pattern now carries the `pylti1.3` concentration
risk explicitly** — one 138-star, single-maintainer MIT library is the seam in seven of eight
recipes, and that belongs in the SOW.

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
   one namespace per institution. **Where a verified curriculum standard exists for the
   jurisdiction, ground against it rather than against the slides alone — see P10.** For Brazilian
   basic education that is `bncc-dev`; the measured difference is 31.9% → 2.3% curriculum
   hallucination.
1b. **Filter retrieved documents by student identity, institution and authorised category *before*
   prompt construction, and emit a disclosure record per retrieval.** New this pass. Copy the shape
   from `ashutoshrana/haystack-ferpa-filter` (Apache-2.0, 41 commits) — **read it, do not import it
   at 0 stars** — which returns filtered documents plus a `disclosure_record` for the caller to
   persist. This is cheap to build at design time, effectively impossible to retrofit after a
   FERPA/GDPR review, and it is the artefact that answers "prove this student could lawfully see
   that document". It also feeds P3's audit log for free.
2. Run DeepTutor as a service; pin the version — it released v1.6.15 on 2026-10-19 and moves weekly.
3. Expose the service as an LTI 1.3 Advantage tool via `pylti1.3`. The LMS launches it; the LMS is
   never patched. **This is what keeps Globant's code off the GPL/AGPL side of the line.**
4. Return grades/progress through LTI AGS so the gradebook stays authoritative.
5. Persist learner state in Globant-owned storage, keyed by the LTI `sub` claim — never by email.
6. **Prove it teaches, and do not use an LLM judge to do it. New this pass.** Before the pilot
   closes, run an evaluation the client's academics can defend:
   - Score tutoring behaviour with **`eth-lre/mathtutorbench`**'s task shapes — problem solving,
     socratic questioning, solution correctness, mistake location, mistake correction, scaffolding —
     which grade against **ground-truth teacher utterances via a reward model**, not a judge's
     opinion (licence caveat: CC BY badge vs CC BY-SA footer; resolve before extending it).
   - Borrow the discipline from **`bydeng01/conv-vs-ped-tutor`** and
     **`bydeng01/ability-levels-audit`** (both MIT): **pre-register the comparison, freeze and hash
     the data, keep a decisions log, separate registered analysis from post-hoc.**
   - **Measure answer leakage explicitly** — whether the tutor's "helpfulness" came at the cost of
     the student's later independent work. That is the failure mode an LLM helpfulness judge
     rewards.
   - **Never present a difference-in-differences on a bounded satisfaction scale as evidence of
     learning.** The audit above shows that design can manufacture an effect from nothing, and a
     client's statistician will eventually notice.
   **Cost:** 2–3 weeks inside the pilot. **Value:** it is the one claim in this market that
   competitors cannot make, in a sector where every deck asserts an uplift.

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
- `xiaoyang111222/cn-math-taxonomy` (**CC BY-NC 4.0**, 780 ★) — **new this pass; read, never
  ship.** The shape of the artefact step 1 asks the client's SMEs to produce, already built for
  Chinese K-9 mathematics: **531 knowledge points, 909 prerequisite edges distinguished as 788
  hard and 121 soft**, 2,271 items and 230 curriculum-standard entries, with a diagnostic engine
  and validation scripts. **NonCommercial rules it out of a deliverable, and its author states it
  is an AI-generated draft not reviewed by teachers** — so take two things from it: the
  **hard/soft prerequisite distinction** (a soft edge degrades the recommendation, a hard edge
  blocks progression) and the warning that a generated skill graph is a draft until a teacher signs
  each edge
- `brownplt/LTLTutor` (**GPL-3.0**, 12 ★, 320 commits, CAV 2025 Distinguished Paper) — **read,
  don't link.** Misconception-driven adaptation: it models the specific wrong beliefs learners hold
  and targets practice at them, which is a sharper decision rule than mastery probability alone

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
6. **Have a teacher sign every prerequisite edge, and record who signed it. New this pass.** The
   skill graph is the engine's entire authority; a generated graph is a hypothesis. Borrow the
   hard/soft edge distinction from `cn-math-taxonomy` and treat an unsigned edge as soft.
7. **Run P1's stage 6 evaluation here too, and it matters more in this pattern than in P1** —
   because a mastery engine makes progression decisions. Pre-register the comparison, freeze the
   data, measure answer leakage, and **do not report an LLM-judged helpfulness score to an
   accreditor** (`agents/top.md`).

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
   immediate billable item in EMEA. **The watermarking grace period for AI-generated content runs to
   2026-12-02** — six weeks from this pass — so machine-readable marking is a dated deliverable, not
   a backlog item.
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

**Reuse note — the conformity file is the most portable artefact in this KB.** It travels to:
- **Brazil.** PL 2338/2023 is risk-based and passed the Senate in December 2024.
- **South Korea, and this one is already in force.** The **Framework Act on AI (Law No. 20676) has
  applied since 2026-01-22**, its **high-impact AI** category explicitly covers **student evaluation
  in early childhood, elementary and secondary education**, and high-impact operators owe
  **user-protection measures and records of safety and trust measures (Art. 34(1))** — the same
  documentation set as the Annex III file. The **fundamental-rights impact assessment is voluntary
  (Art. 35)**, so lead with it as a differentiator rather than a cost. **A foreign vendor without a
  Korean presence must appoint a domestic agent** — a commercial arrangement to settle before
  bidding, not an engineering task. Grace period on fines is reported as one year from entry into
  force. Read the Enforcement Decree and MSIT guidance before quoting thresholds.
- **Uruguay**, as the LATAM pilot: first in Latin America to sign the Council of Europe AI Framework
  Convention, so European-shaped evidence is the evidence it already expects.

**Estimate:** 10–12 weeks including the conformity file. Porting it to a second jurisdiction:
2–3 weeks, almost entirely mapping and review rather than build.

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
- `elimu-ai/webapp` (MIT, 41 ★, **8,075 commits**) — **new this pass.** Per-language content hosting
  that pushes to Android devices for out-of-school children, with production deployments in Hindi,
  Tagalog, Thai, Vietnamese and English; the same org publishes MIT ML components for reading-level
  prediction and storybook/video recommendation
- `ipti/br.tag` — **new this pass**, and read for one design decision rather than adopted: school
  management built for rural schools with **data sync for schools without internet**. Its licence is
  unresolved (README says BSD-3-Clause, sidebar links GPL-2.0), so **copy the sync model, not the
  code**

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
7. **Stage the adoption and say so in the bid. New this pass, and it is the lesson of the most
   expensive failure in this sector.** South Korea mandated AI digital textbooks nationally, met
   teacher and parent resistance, retreated to voluntary adoption, and on **2025-08-04** the
   National Assembly removed them from the legal definition of a textbook, taking the funding with
   them; usage had already fallen from ~37% of eligible classes in the first semester of 2025 to
   19% in the second, and schools from ~4,190 to 2,095. **Every education ministry in APAC watched
   that.** So: opt-in pilot schools, published outcome measures (P1 stage 6), teacher capability
   before coverage, and a documented exit path. **Price change management as the main line item,
   not the technology.**

**Estimate:** 12–14 weeks for a state-level pilot.

---

## P6 — The roster and SIS data spine (North America)

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

## P7 — Grade-band gating and teacher-only mode (North America K-12)

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
6. **Add a per-pupil opt-out that degrades gracefully. New this pass.** Four states enacted
   education-AI statutes in 2026 — **Idaho, Maryland, Oklahoma, Virginia** — and per one tracker
   Oklahoma's gives **parents an opt-out from student-facing AI tools together with a duty to
   provide alternative access to core instruction** *(single-tracker claim; verify against the
   statute, build for it regardless)*. The flag belongs on the roster record (P6), is enforced at
   the same gateway as the grade band, and **must leave the pupil with the instruction minus the AI
   path** — an opt-out that removes the lesson is a civil-rights problem, not a feature.
7. **Add an approval queue.** Oklahoma permits AI only under educator supervision with human review
   and **bars it from high-stakes student decisions**. So nothing AI-written reaches a student, a
   parent or a record until a named educator signs it, and the signature is logged with the draft
   it approved. `JaimeArriagadaRosas/Plugin-Feedback-Canvas` implements exactly this shape against
   Canvas over LTI 1.3 and **has no licence** (`agents/top.md`) — read it, rebuild it.
8. **Add a decision log that can answer "was any high-stakes determination AI-made?" with a
   query.** Placement, discipline, promotion, eligibility. The answer a district needs is "no, and
   here is the record", not a policy document.

**Why this is worth building once:** it is small, every K-12 district in a restricting state needs
it, and teacher-facing-only mode **keeps the engagement alive in a district that has banned
student-facing AI.** That is the difference between a lost account and a smaller one. **With the
opt-out, approval queue and decision log added, this pattern is no longer defensive — in Oklahoma,
Idaho, Maryland and Virginia it is the compliance surface the statute asks for**, and
`SirhanMacx/Claw-ED` (MIT, 778 commits) is a working reference for the teacher-facing-only product
shape.

**Estimate:** 2–3 weeks on top of P3 and P6 for gating; **+2 weeks for the opt-out, approval queue
and decision log.**

---

## P8 — The permissive-LMS build: no LTI boundary (greenfield, and EMEA sovereignty) — NEW

**For:** two specific situations, and no others. (1) A **greenfield** build — a corporate academy,
a bootcamp, a new programme, a ministry standing up something new — where no incumbent LMS exists.
(2) An **EMEA sovereignty** engagement where the buyer needs the data, the platform and ideally the
vendor inside Europe.

**Why it is new:** every other pattern in this KB pays the same architectural tax — Globant's agent
code must sit on the far side of a network boundary because the LMS is GPL/AGPL. **`OpenOLAT` is
Apache-2.0 with 31,877 commits**, so for the first time that tax is optional.

**Stack**
- `OpenOLAT/OpenOLAT` (**Apache-2.0**, 448 ★, 31,877 commits) — the LMS. Teaching, learning,
  assessment, communication, modular course authoring. frentix GmbH (Switzerland), built on the
  University of Zurich's OLAT 7.1
- `ArnaudGuiovanna/tutor-mcp` (MIT, 52 ★) — the P2 pedagogy engine; BKT, FSRS, prerequisite gating
- `HKUDS/LightRAG` (MIT, 40.2k ★) — retrieval over the client's curriculum
- `HKUDS/DeepTutor` (Apache-2.0, 41.7k ★) — conversational surface
- `huggingface/smolagents` (Apache-2.0, 29.9k ★) — agent loop for custom tools
- Self-hosted models (in-region) for the sovereignty case
- **Not** `pylti1.3`. That is the point of this pattern

**Wiring**
1. Confirm the licence from the **file, not the page.** OpenOLAT's GitHub sidebar names no licence;
   `LICENSE` is the full Apache-2.0 text followed by two provenance notices crediting the OLAT
   Zentrum at the University of Zurich and the OpenOLAT community/frentix GmbH. **Those are
   attribution notices in the NOTICE tradition, not additional licence terms** — the grant is
   Apache-2.0. Record it that way in the licence inventory and attach the file to the SOW. Pin to a
   commit and keep the NOTICE attribution intact in any distribution.
2. Deploy OpenOLAT in-region. For the sovereignty case this is the whole proposition: European
   platform, European maintainer, client-controlled infrastructure, no US hyperscaler dependency.
3. **Integrate the agent in-process.** Apache-2.0 permits linking Globant's code to the platform, so
   ship one deployable instead of a tool plus a bridge. Keep the agent in its own module behind a
   clean interface anyway — not for licence reasons now, but so the work ports to a Moodle or Canvas
   client later across an LTI boundary (P1).
4. Run tutor-mcp as the pedagogy engine and LightRAG as the retrieval layer, exactly as in P1/P2.
   Add P1's **step 1b FERPA/GDPR retrieval filter** — in EMEA this is GDPR and Annex III evidence,
   not optional.
5. If the client is EMEA, **run P4 on top.** Apache-2.0 removes the licence boundary; it removes
   nothing about the AI Act. Globant is still the provider and still owes the conformity file.

**What this pattern does NOT do.** It does not apply to a client already running Moodle, Canvas,
Open edX or Sakai — which is nearly every client. There, the incumbent platform is a given and the
LTI boundary is mandatory; use P1. **Do not propose a migration to OpenOLAT.** 448 stars against
Moodle's 7.5k and Canvas's 6.9k is not a competitive position, the documentation's centre of gravity
is Swiss-German, and no institution is leaving Canvas for it. This pattern is for the cases where
there is nothing to migrate from.

**The honest risk:** a smaller community than Moodle or Open edX, which means fewer integrators,
less third-party plugin supply and a thinner hiring pool. Price support accordingly, and do not
present it as a like-for-like Moodle substitute.

**Estimate:** 8–10 weeks to pilot (greenfield), 12–14 weeks with P4's conformity file for an EMEA
public-sector buyer. Roughly 2–3 weeks less than the equivalent P1 build, because the LTI bridge
and its testing disappear.

---

## P9 — The COPPA disclosure boundary (North America K-12) — NEW

**Time**: 3–5 weeks for the audit, 6–10 weeks for remediation | **Licences**: all permissive
**Trigger**: the amended COPPA Rule, full compliance required since **2026-04-22**

**Why this is the shortest-cycle pattern in this file.** It does not ask the district to buy a new
capability. It tells them something they already own is out of compliance with a federal rule that
took effect six months ago, and then fixes it. The budget line exists before the conversation does.

**The legal mechanic, stated precisely because the whole pattern turns on it.** Amended
§312.5(a)(2) requires **separate verifiable parental consent before a child's personal information
is disclosed to a third party**, and the exception covers disclosures *integral* to the service,
not merely useful or convenient. A parent may consent to the product and refuse the disclosure.
The Rule also adds **retention limits**, a **written, published retention policy**, and
**biometric identifiers** to the definition of personal information.

**In a typical 2025-vintage K-12 tutor, the pupil's prompt goes to OpenAI, Anthropic or Google.
That is a disclosure to a third party.** If it was covered by a single blanket consent at
sign-up — which is the normal implementation — the deployment is non-compliant.

### Stage 1 — the posture audit (3–5 weeks, sellable on its own)

Inventory, for every AI feature the district runs:

1. **Egress**: which fields leave the district boundary, to which processor, under what contract.
   Prompts are the obvious one; transcript history, assignment text, IEP-adjacent notes and voice
   audio are the ones that get missed. Voice adds biometrics, which are now PII by definition.
2. **Consent structure**: is there one consent or two? If the parent cannot accept the product and
   decline third-party model disclosure *independently*, there is a finding.
3. **Retention**: is there a written, published retention policy, and does the system actually
   enforce it — including on the processor's side, where the contract usually says 30 days and
   nobody has checked.
4. **Integrality argument**: for each disclosure you intend to keep, write the sentence explaining
   why it is integral to the service the parent asked for. If that sentence is hard to write, the
   disclosure fails the exception.

Deliverable: a findings register mapped clause-by-clause, with each finding marked
*remediate-in-place* or *remove-the-disclosure*.

### Stage 2 — remediation, and there are only two real answers

**Answer A — separate the consent and keep the disclosure.** Split the consent flow in two, gate
model calls on the second grant, and degrade gracefully for pupils whose parents granted only the
first: the product must still work, teacher-facing or with local-only features. Add retention
enforcement as a scheduled job with an audit record per deletion, reusing the hash-chained audit
shape the governance layer in **P3** already builds. This is the cheaper path and it leaves the
district's existing vendor relationships intact.

**Answer B — remove the disclosure entirely.** If the model call never leaves the district
boundary, §312.5(a)(2) is not engaged for that call. Two routes, both already in this KB:

- **On-premise inference behind the LMS the district already runs.** Moodle's core AI subsystem
  takes an **Ollama** provider directly, and its **OpenAI-compatible** provider accepts a
  self-hosted **LiteLLM** or **LocalAI** gateway (`verticals/solutions.md`). The pupil's prompt
  reaches a model the district operates. No third party, no second consent, no retention exposure
  at a processor.
- **Offline-first delivery** where connectivity or policy makes even on-premise inference
  impractical — **Kolibri** (MIT) plus the local tutor shell in **P5**, with
  `zijinz456/OpenTutor` (MIT, 10+ providers incl. local) as the agent shell.

**Pair B with the deterministic pedagogy engine and the compliance story gets better, not worse.**
`tutor-mcp` (MIT) runs BKT, FSRS and prerequisite gating **locally against SQLite** — the mastery
model, which is the most sensitive longitudinal record in the system, never needs to leave the
building at all. The LLM is then only a language surface over a local decision engine, and the
smallest possible share of pupil data crosses any boundary. **This is the strongest commercial
argument in this KB for the architecture it has advocated for four passes, and it now has a
federal rule behind it rather than an aesthetic preference.**

### What not to build

**Do not build a COPPA compliance engine.** `repos/foundations.md` records about a dozen
FERPA/COPPA governance repos, every one at 8 stars or fewer and nearly all started in the two
months after the April deadline. The market is forming; none has won; and a client's compliance
posture should not sit behind a 1-star dependency. Build the audit as a method and the remediation
as architecture, reuse **P3**'s audit-logging layer, and keep the legal determination with the
district's counsel — the engagement is the disclosure-boundary redesign, not a legal opinion.

**Scope boundary to state in the SOW:** Globant determines where data flows and makes it match what
the district's counsel says the Rule requires. Globant does not certify COPPA compliance.

---

## P10 — The verified curriculum spine (LATAM now; APAC as a build) — NEW

**For:** any engagement where the client is accountable to a **national or state curriculum
standard** — a ministry, a public school network, a board, a national edtech, a university serving
a regulated programme. This is the pattern that answers "how does your tutor know what my
jurisdiction requires it to teach?" with data instead of a prompt.

**Why it is new, and why it is the most defensible recipe in this file:** pass 319 found the first
artefact in this sector that turns a national curriculum into verified, permissively licensed,
machine-readable infrastructure **and publishes what it is worth.**

### Variant A — Brazil, today, with components that already exist

**Stack**
- `bncc-dev/bncc-dados` (**MIT code / CC BY 4.0 data**, 22 ★, 40 commits) — the BNCC as **1,721
  verified learnings** (1,580 basic-education skills across three stages plus the 141-item Computing
  complement), JSON canonical with SQLite/SQL/CSV builds, JSON Schema draft 2020-12, content version
  `dados-2026.08`
- `bncc-dev/bncc-pacotes` (**MIT code / CC BY 4.0 data**, 9 ★, 103 commits) — npm `@bncc/dados`,
  **npm `@bncc/mcp` (seven MCP tools)**, PyPI `bncc`, and a **hosted keyless MCP endpoint** at
  `mcp.bncc.dev`
- `bncc-dev/bncc-benchmark` (**MIT code / CC BY 4.0 items and results**, 9 ★, 82 commits) — the
  acceptance test
- `HKUDS/LightRAG` (MIT) + `HKUDS/DeepTutor` (Apache-2.0) — retrieval and tutoring, as in P1
- `portabilis/i-educar` (GPL-2.0, **34,948 commits**) and `portabilis/i-diario` (**licence not shown
  — read the file**) — the records layer a Brazilian public client is already running
- `dmitry-viskov/pylti1.3` (MIT) or `tsugiproject/tsugi` (Apache-2.0) — the boundary

**Wiring**
1. **Pin the curriculum dataset to a release, not a branch** (`dados-2026.08`, schema v1.1.0), and
   record the checksum. The packages already do this internally; your deployment must too, because
   a curriculum that changes silently under a tutor is a correctness incident.
2. **Resolve every learning objective through the MCP server or the typed package — never through
   the model's memory.** This is the whole point: a well-formed code that does not exist returns an
   explanatory error rather than `null`, which is what stops a tutor inventing a standard.
3. **Index the client's own material with LightRAG and link each chunk to one or more curriculum
   codes.** The codes are the join key between what the client teaches and what the state requires.
4. **Expose two retrieval paths to the tutor**: curriculum (authoritative, from the dataset) and
   course material (client-owned, from LightRAG). Keep them separate in the prompt and label them,
   so a citation can always be traced to one or the other.
5. **Run the benchmark as the acceptance test before go-live**, on the client's own model and
   configuration: direct lookup, existence (including plausible fake codes — this is the one that
   catches a confident tutor), open generation, reverse lookup. **Publish the result to the client.**
6. Keep Globant's agent on the far side of the LMS/SIS boundary as always: i-Educar is GPL-2.0, and
   i-Diário's licence is unresolved.

**What to promise, with the number behind it:** on this curriculum, an ungrounded model invents a
standard **31.9%** of the time; with the verified dataset queried over MCP, **2.3%**; with the data
pasted directly into the prompt, **0.2%**. Across the models the benchmark tested, faithful-text
rates ran from **88% down to 3%** — so **no model choice closes a 30-point grounding gap.**

**Estimate:** 5–7 weeks on top of P1, most of it in step 3 (mapping client material to codes).

### Variant B — India, where the artefact does not exist and the mandate is dated

**The gap, measured this pass:** GitHub's `ncert` and `cbse` topics hold 180 repositories and
**nothing above 15 stars that is curriculum infrastructure.** The one MCP server
(`jinanshm/ncert-mcp`, 1 ★, 2 commits) is **unlicensed** and ingests by downloading the NCERT PDFs
and **tagging chunks with an LLM via OpenRouter with no human verification described** — which is a
hallucination source with a schema. `praj2408/RAG-Enhanced-NCERT-Tutor` (MIT, 3 commits) **bundles
textbook PDFs**, a copyright question of its own. The best data asset is a **2018** scrape of
~20,000 schools. Meanwhile **AI + Computational Thinking is compulsory for Classes 3–8 from
2026-27 across 32,900 CBSE schools.**

**The build, copying Brazil's method rather than its data**
1. **Extract against the official source and verify it.** Character-level checking against the
   published curriculum document, not LLM tagging. A code sweep for missing and extra codes.
2. **Publish a schema** and 25–30 contract and completeness checks that run in CI, so a divergence
   fails the build rather than reaching a classroom.
3. **Keep a decisions log** for every inconsistency found in the source. This is what makes the
   dataset citable by a ministry.
4. **Split the licence deliberately**: permissive for the pipeline, attribution-only for the data,
   with the normative texts identified as official acts. That is what makes it adoptable by
   competitors — which is the point of a moat built on a standard.
5. **Ship an MCP server and typed packages** over it, plus a hosted endpoint.
6. **Build the benchmark alongside it**, including the fake-code existence task, and publish the
   numbers.

**Why do this rather than a tutor:** whoever holds the verified curriculum layer for a jurisdiction
is in every bid in that jurisdiction, because the alternative is each vendor re-deriving it badly.
At 22 stars in Brazil, **nobody is competing for this yet.** It is fundable as a standalone asset
(a board, a ministry, a national edtech, or a foundation), it is reusable across every subsequent
engagement in the market, and it is the rare deliverable whose quality is **objectively
demonstrable** — the benchmark is the proof.

**Estimate:** 10–14 weeks for one subject across the mandated grades, including verification;
longer for a full curriculum. **Verification is the majority of the work and the entire value.**

**Where else this applies:** anywhere with a published national curriculum and no data layer —
which, on the topics swept this pass, is everywhere except Brazil. Germany's attempt was archived
in 2021; the Dutch and Spanish-language topics produced course material; the English `oer` topic
produced textbooks and no competency metadata. Ed-Fi (`repos/foundations.md`) is the North American
**rostering** standard and does not cover curriculum.

---

## The cross-cutting risk, re-stated in pass 319 — and now with a real alternative

**Eight of these ten patterns cross the LMS boundary through `dmitry-viskov/pylti1.3`: one MIT
library, re-verified in pass 319 at 138 stars, 84 forks, 178 commits, a single maintainer, 39 open
issues and still no published release.** It is the most load-bearing and least redundant component in this KB's architecture, and
pass 317 is the first pass to say so out loud.

It is good software — it covers the whole LTI Advantage surface (Deep Linking, AGS, Names and Roles,
Course Groups, Submission Review, Data Privacy Launch), which is why every pattern leans on it. The
risk is not quality, it is concentration. **Name it in the risk section of any SOW that depends on
it**, and know the fallbacks — which pass 318 made specific. `1EdTech/ltibootcamp` indexes LTI 1.3
implementations across seven languages: **`ltijs` and Atomic LTI Worker (Node)**, **OAT's core /
Deep Linking / Names & Roles libraries and a Symfony bundle (PHP)**, **UOC's library and Spring
Boot library (Java)**, **`LtiAdvantagePlatform` (.NET)**, **Atomic Jolt's starter app (Ruby)**,
**Atomic Forge (Rust)**, and `django-lti` alongside `pylti1.3` itself (Python). `ltijs` is the
route `blamb/lti-tutor` took to working deep linking and AGS passback against Moodle.
**Caveat before you scope on any of them:** that index carries no LICENSE file, its newest content
folder is `europe_tech_2020`, and its own README says the entries "have not been vetted" — verify
each against its repository. And **P8 avoids the dependency entirely.**

**Pass 319 found the alternative itself, not another index: `tsugiproject/tsugi` — Apache-2.0,
376 ★, 266 forks, 4,011 commits, Apereo Incubating**, maintained around the co-author of the LTI
specification, with an IMS ContentItem app store and low-level IMS libraries shared with Sakai.
Against 178 commits and one maintainer that is a different class of dependency. **Two caveats
before it goes in a SOW:** it is **PHP**, and **its GitHub page does not state which LTI versions or
Advantage services it implements** — verify the Advantage surface against the repository and the
Tsugi documentation first. Also recorded for breadth: **`jcputney/scorm-again` (MIT, 356 ★, 1,229
commits)** covers **SCORM 1.2 and 2004** for the large installed base of courseware LTI does not
reach — **AICC was removed in v3.0.0 and cmi5/xAPI are roadmap "potential" only**, so promise
neither.

---

## Pattern selection by region

| Region | Lead with | Why |
|---|---|---|
| Greenfield / no incumbent LMS (any region) | **P8** | Apache-2.0 OpenOLAT removes the LTI boundary; one deployable, 2–3 weeks less build |
| North America | **P9 first**, then **P3 + P6**, then P7 where restricted, then P1/P2 | **P9 leads because the amended COPPA Rule has been in force since 2026-04-22 and most deployed K-12 AI is likely non-compliant** — it sells into the installed base rather than competing with a frontier-model seat licence. Then the dated policy requirements (Ohio 2026-07-01, NC model policy 2026-12-31, Idaho SB 1227, 134 bills/31 states); governance is the budgeted line and the roster spine is now open source |
| EMEA | **P4**, with **P8** where sovereignty decides the deal | Provider-side conformity under Annex III; Article 50 live, watermarking and new prohibitions both land 2026-12-02, 2027-12-02 the real deadline. OpenOLAT is the only permissive, EMEA-authored, EMEA-maintained LMS in this KB |
| EMEA — Gulf | **P1/P2 with Arabic-first localisation** | UAE ~28% of GCC edtech, National AI Strategy 2031; incumbents (Alef, Classera, Abwaab) are proprietary and buying integration, not platforms |
| EMEA — Africa | **P5** | Strongest low-resource evidence base in the world (Edo State, EIDU); DigiSchool tablets are installed hardware needing content |
| APAC | **P10 Variant B + P5** (India), P1 + labelling (China), P1 (Japan), **P4 ported** (South Korea) | Curriculum mandate plus infrastructure gap — **and pass 319 found the curriculum *data* gap under it: 180 NCERT/CBSE repositories and no verified dataset**, so the spine is a build, not a dependency. China needs labelling/registration at the generation step; Japan has the fewest blockers; **Korea's Framework Act on AI is in force since 2026-01-22 and names student evaluation as high-impact**, so the EMEA conformity file sells there now — and the 2025 AI-textbook reversal means every Korean and regional buyer is bidding on deployment risk, not capability |
| APAC — Australia / NZ | **P7**, then P1 | Ipsos 2026 finds ANZ public support for banning AI in schools *higher* than in Asian markets — closer to the US restriction posture than to the rest of APAC |
| LATAM — Brazil | **P10 Variant A**, then P2, with P4's artefacts ported | **The only jurisdiction with a verified open curriculum dataset, an MCP server over it and a published grounding measurement (31.9% → 2.3%)**, plus a 34,948-commit municipally originated SIS with no AI in it. Brazil's June 2026 AI/tech agreement with the EU means the conformity file transfers, and PL 2338 is risk-based |
| LATAM — Spanish-speaking | **P2**, with P4's artefacts ported, and P10 as a build | No equivalent curriculum data layer was found in the Spanish-language topic sweep, so P10 here is Variant B work. The 92%-usage / 30%-satisfaction gap and the 50/19 feedback gap are delivery problems, which P2 answers |

**No pattern here is LATAM-only or North-America-only.** P1 and P2 are the portable core; P3, P4,
P5, P6, P7 and P9 are the regional wrappers that make them biddable. **P10 is portable in method and
regional in data** — Variant A is a Brazilian assembly job, Variant B is the same recipe anywhere a
curriculum is published and not yet machine-readable, which on this pass's evidence is everywhere
else. **P8, new this pass, is the only
one selected by the client's starting position rather than by region** — it applies wherever there
is no incumbent LMS, and it is strongest in EMEA because sovereignty and a permissive European
platform happen to answer the same objection.

**For LATAM specifically, pass 317 sharpened the pitch without needing a new pattern.** UNESCO
IESALC (2026-09-09; 200 institutions, 19 countries) found **87% of LAC higher-education institutions
using AI and only 26% with a formal AI strategy** — a 61-point gap, with adoption driven by
individuals rather than institutions. That is P3's governance deliverable with the compliance driver
swapped for an institutional-risk driver, and it is the same work this KB already sells in North
America.
