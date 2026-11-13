---
industry: education
region: Global
updated: 2026-11-13
---

# Compose patterns — education

Eight concrete recipes. Each names the actual repos, the license consequence,
how the pieces wire together, and a rough build estimate. All components were
license-verified on 2026-11-13 (see `agents/top.md` and `repos/foundations.md`).

**The rule all eight follow:** keep the AI layer permissive (MIT/Apache/BSD),
mount it into the copyleft platform over **LTI 1.3** or **MCP**, and emit
**xAPI** or **Caliper** events. Never fork the LMS.

**Two changes from the previous edition.** The LTI front door no longer needs
writing from scratch — `Cvmcosta/ltijs` (Apache-2.0, 373 stars) implements the
full LTI Advantage surface. And **P3 is no longer a greenfield build**: seven
Moodle MCP servers exist, so P3 is now a selection-and-hardening pattern, which
is cheaper and lands sooner.

**One constraint that shapes every pattern:** every verified LTI 1.3 library is
Node, PHP or Elixir — **none is Python**, while nearly every agent here is
Python. Assume a two-process shape: Python agent service behind a Node (`ltijs`)
or PHP (`packbackbooks`) LTI front door. Budget the seam.

---

## P1 — Compliance-safe practice tutor (North America, restrictive states)

**Problem:** the client wants an AI tutor, but Texas HB 2400 bars AI from
delivering direct classroom instruction, New York limits classroom AI to grade
9+, and Chicago-style district rules bar AI as the sole basis for high-stakes
decisions.

**Wiring:**
1. **Mastery/progression engine — outside the model.**
   `pykt-team/pykt-toolkit` (MIT) for knowledge tracing, or `CAHLR/OATutor`
   (MIT) if Bayesian Knowledge Tracing over an existing item bank is enough.
2. **Item bank and renderer.** `Khan/perseus` (MIT) for real exercise
   rendering and authoring.
3. **Agent role, scoped deliberately to practice and feedback.** Adapt
   `HKUDS/DeepTutor` (Apache-2.0) — use its learner-model and learning-path
   machinery, disable instruction delivery; the human teacher instructs.
4. **LMS mount.** `Cvmcosta/ltijs` (Apache-2.0) as the LTI 1.3 tool provider
   into Canvas; for agent-side access use `vishalsachdev/canvas-mcp` (MIT).
5. **Telemetry.** Emit Caliper (`1edtech/caliper-spec` — implement the spec, do
   not vendor the repo) plus an audit log of every agent action with the grade
   level and state policy applied.
6. **Policy gate.** A configuration layer keyed to state and district: grade
   floor, instruction-delivery off, human-in-the-loop gate on anything
   decision-shaped, logging retention, FERPA/COPPA posture. NYC's
   green/yellow/red tiers map directly onto a tool allowlist per tier.

**License outcome:** entire AI layer MIT/Apache; Canvas stays separate behind
LTI, so AGPL does not reach the deliverable.

**Estimate:** 8–10 weeks. **Sells because** it is the tutor that is legal where
a general tutor is not.

---

## P2 — EU AI Act high-risk conformity layer for assessment AI (EMEA)

**Problem:** the institution already runs AI touching assessment or admissions.
Under the AI Act that is high-risk in principle (Annex III covers access,
allocation, assessment and monitoring of pupils during tests). Obligations for
stand-alone Annex III systems are set at **2027-12-02** by Regulation (EU)
2026/1744 (published in the OJ 2026-07-24), with transparency duties from
August 2026 and **2028-08-02** for AI embedded in regulated products. Emotion
recognition in education has been banned since February 2025. Some vendor
guides still assert August 2026 for high-risk obligations — **verify on EUR-Lex
before committing to a timeline**, and expect clients who believe they are
already late.

**Wiring:**
1. **Inventory and classify.** Enumerate every AI touching admissions,
   assessment, progression or monitoring; classify against Annex III; record
   the low-risk exception argument where it applies.
2. **Human oversight layer.** A review queue in front of every consequential
   output: no automated decision without a named human decision-maker. The
   `EDUKAI-LONGVIEW` framing — "agent recommends, teacher decides" — is the
   right interaction model even though the repo itself is a prototype.
3. **Logging and traceability.** Append-only event log of inputs, model
   version, prompt, output, reviewer and outcome. Emit **xAPI** for the
   institution's own reporting.
4. **Mastery state outside the model**, so assessment decisions are explainable
   from `pykt-toolkit` (MIT) outputs rather than from model text.
5. **Sovereign deployment.** Self-hosted open weights, institution-controlled
   infrastructure — Council of the EU document ST-14902-2026 (2026-10-29) makes
   reduced dependence on non-European AI explicit for education and training,
   so this is procurement-relevant, not ideological.
6. **Platform mount without forking.** `ltijs` (Apache-2.0) into Moodle/ILIAS,
   plus `Faixiang/Moodle-MCP` (MIT, read-only) for agent read access — the
   read-only surface is an asset in a conformity story.
7. **Documentation pack.** Risk management file, data governance,
   instructions-for-use, post-market monitoring plan.

**License outcome:** Moodle/ILIAS untouched (no fork); all added components
MIT/Apache.

**Estimate:** 12–16 weeks. **Highest-value regulated education work globally.**

---

## P3 — Pick and harden a Moodle MCP server (Global, reusable asset)

**Problem:** the client runs Moodle — the most-deployed LMS in the world and
the incumbent across EMEA, LATAM and APAC public education — and wants agents
to work inside it. **Previously this KB called this greenfield. It is not.**
Seven servers exist; none is production-hardened, and they disagree on
everything that matters.

**The selection matrix (all verified 2026-11-13):**

| Server | License | Stars | Surface | Auth | Pick when |
|---|---|---|---|---|---|
| `Faixiang/Moodle-MCP` | MIT | 206 | 10 tools, **read-only** | Web-service token | Default. First engagement, security review pending, or read-only is genuinely enough |
| `G36maid/moodle-mcp` | MIT | 29 | Courses, assignments, forums, grades, files-as-markdown (Rust) | Token | Widest version coverage (verified 3.7 / 4.5 / 5.2); single-binary deployment |
| `falkenslab/moodle-mcp` | MIT | 2 | **~260 tools** incl. grading, quiz building | **Interactive browser login, SSO + 2FA, no token, no plugin** | The institution refuses to issue web-service tokens, or SSO/2FA is mandatory |
| `MarcosNahuel/moodle-mcp` | MIT | 1 | 40 tools + `ws_raw`, **idempotent upsert-by-`idnumber`** | Token + companion plugin `local_italiciamcp` | Agents must *publish* course content repeatedly without creating duplicates |
| `csmediapro/...` | AGPL-3.0 | 2 | 10 core + paid premium tools | Token | Avoid for client deliverables: copyleft plus commercial upsell |
| `lmscloud-io/...` | GPL-3.0 | 1 | Unstated | Token | Avoid for client deliverables |

**Wiring:**
1. **Fork the MIT server whose auth model matches the client's security
   posture** — this is the decision, not the star count. Token-issuance policy
   usually decides it.
2. **Harden:** pin Moodle version compatibility, add structured errors,
   rate-limit, scope the token or session to least privilege, add an audit log
   of every tool call with the acting user.
3. **Add write safety.** If writes are in scope, port `MarcosNahuel`'s
   upsert-by-`idnumber` idempotency pattern regardless of which server you
   started from. Generated content gets republished; duplicates are the default
   failure mode.
4. **Emit xAPI** for every agent action so the institution can report on it.
5. **Pair with `ltijs`** (Apache-2.0) when the same engagement needs a
   student-facing tool surface, not just agent access.

**License outcome:** MIT server, reusable across every Moodle engagement in
EMEA, LATAM and APAC.

**Estimate:** **3–5 weeks** to harden a chosen MIT server (down from the 5–7
weeks a from-scratch build was estimated at). **Build once, bill many.**

---

## P4 — Institutional AI governance package (LATAM, productized)

**Problem:** UNESCO IESALC across 200 institutions in 19 countries — 87% use
AI, 26% have a framework, 55% have no AI budget, 9% evaluate. Brazil's Cetic.br
— 53% of administrators use AI, 22% of schools have a guideline. The
institution is already exposed and cannot afford a frontier-API product.

**Wiring:**
1. **Policy artifact first**, mapped to the national instrument that applies
   (Brazil PL 2.338/2023 risk tiers; Colombia CONPES 4144; OECD AI Principles
   where adopted) and to UNESCO IESALC's framework categories.
2. **Cheap-to-run inference.** Self-hosted open weights. Where connectivity is
   the constraint, `learningequality/kolibri` (MIT, offline-first) as the
   delivery platform.
3. **Evaluation harness — the differentiator, because 9% evaluate.**
   `kaushal0494/AITutor-EvalKit` (MIT) for pedagogical effectiveness,
   `pykt-team/pykt-toolkit` (MIT) for mastery measurement, xAPI/Caliper
   telemetry into a dashboard. Thin upstream; say so, and own the gap.
4. **Teacher enablement** in Spanish/Portuguese — the one intervention every
   framework mandates.
5. **Content localization.** `satvik314/educhain` (MIT) and `oppia/oppia`
   (Apache-2.0) against national curricula (ENEM, ICFES, PAES, SEP). Shortcut:
   `THU-MAIC/OpenMAIC` (MIT) **already ships pt-BR and es-MX locales**.
6. **Platform mount.** Moodle or Chamilo (both PHP → `packbackbooks/lti-1-3-php-library`,
   Apache-2.0), plus `Faixiang/Moodle-MCP` (MIT) for agent read access.

**License outcome:** fully permissive AI layer; platforms untouched.

**Estimate:** 6–8 weeks per institution after the first; **the first build is
the product.** Ceibal (Uruguay) is the template for the ministry-scale version.

---

## P5 — Multi-jurisdiction compliance architecture (APAC)

**Problem:** a regional university group or edtech vendor faces Korea's AI Basic
Act (in force 2026-01-22, education = high-impact), Vietnam's binding AI law
(education high-risk, **pre-deployment registration and human oversight**,
implementing decree April 2026, compliance runway reported as late as September
2027), Australian TEQSA generative-AI risk management plans, Chinese content
labelling and algorithm registration, and the EU AI Act for anything sold into
Europe — simultaneously.

**Wiring:**
1. **One policy-enforcement layer, per-jurisdiction configuration.** Model
   obligations as declarative policy (allowed uses, registration state, human
   oversight requirement, logging retention, labelling duty), evaluated per
   request with the jurisdiction as an input.
2. **Policy as graph nodes, not prompt text.** Route every agent action through
   the policy evaluator; deny-by-default on unconfigured jurisdictions.
3. **Registration and evidence store.** Vietnam requires pre-deployment
   registration — keep the artifacts (system description, oversight design,
   test evidence) as first-class records, versioned with the deployed model.
4. **Human oversight queue** satisfying Vietnam and TEQSA in one mechanism.
5. **Content labelling** for China-facing deployments, emitted at generation
   time rather than retrofitted.
6. **Agent layer.** `HKUDS/DeepTutor` (Apache-2.0) or `THU-MAIC/OpenMAIC` (MIT)
   — regionally built, permissively licensed, already multi-locale.
7. **Sovereign deployment** per data-residency mandate; self-hosted weights.

**License outcome:** MIT/Apache throughout.

**Estimate:** 12–14 weeks. **The compliance layer is the product**; the tutor is
the demo. Note the politics: Ipsos Education Monitor 2026 shows support for
banning AI in schools **rising in Japan and South Korea** — lead with P7's
teacher-augmenting framing in those two markets.

---

## P6 — Agent-assisted grading and feedback (Global, still the open field)

**Problem:** grading is the highest-volume teacher workload and there is no
dominant open-source grading agent anywhere in the world. This remains the
clearest build opportunity in this KB.

**Wiring:**
1. **Start from the one real open system.** `wwrwbs/AI_AWE` (Apache-2.0 per
   README/LICENSE, 2 stars) is a complete pipeline worth copying structurally:
   fine-tuned Qwen2.5-7B LoRA **discourse-move classifier** → **LightGBM
   scorer over 31 linguistic/discourse features** → **label-aware feedback
   generator**, with a Gradio UI for single and batch scoring, locally
   deployable. **Citation trap:** the arXiv paper calls this "ArguLens"; the
   repository never uses that name.
2. **Why that shape matters:** the score comes from an interpretable feature
   model, not from model text. That is what makes it defensible to a regulator
   and auditable to a department — the same principle as keeping mastery state
   outside the model.
3. **Code and notebook assignments.** `jupyter/nbgrader` (BSD-3-Clause) is the
   autograding substrate; the agent adds feedback on top of deterministic test
   results, never replaces them.
4. **Rubric as data, not prompt.** Version rubrics; bind every score to a
   rubric version and keep the mapping explicit.
5. **Human-in-the-loop by construction.** Agent proposes score + evidence +
   feedback; teacher confirms. Required outright by Chicago-style district
   rules and by the EU high-risk oversight duty, and it is the only posture
   that survives an appeal.
6. **Calibration harness.** Hold back human-scored work and report
   agreement (quadratic weighted kappa against human raters) per cohort. Without
   this the client cannot defend the system, and only 9% of LATAM institutions
   evaluate anything today.
7. **LMS writeback.** Grades go back through **LTI Assignment & Grade
   Services** — supported by `ltijs` (Apache-2.0) and
   `packbackbooks/lti-1-3-php-library` (Apache-2.0). Do not write to the
   gradebook out of band.

**License outcome:** BSD/MIT/Apache throughout.

**Estimate:** 8–10 weeks for one discipline. **Still open space** — the entire
field is one 2-star Apache-2.0 prototype, notebook autograding infrastructure,
and Kaggle-era coursework.

---

## P7 — Teacher distillation (APAC and Global, politically safest shape)

**Problem:** the institution wants AI leverage without student-facing autonomy
— because policy forbids it (Texas HB 2400), because public opinion is turning
(Ipsos 2026: ban support rising in Japan and South Korea), or because the
faculty will not accept a tutor that replaces them.

**Wiring:**
1. **Distil the teacher, not the subject.** `JuneYaooo/teacher-to-skills`
   (Apache-2.0, 475 stars) converts a named teacher's own materials — lecture
   video, notes, marked-up feedback — into a source-backed agent Skill that
   teaches to *that teacher's* standard and tapers support as the learner
   improves.
2. **Two properties to preserve when adapting it:** conclusions are tied back
   to source material, and **material without evidence is flagged rather than
   filled in**. That is the anti-hallucination contract that makes faculty sign
   off, and it is worth keeping even if you rewrite everything else.
3. **Learner progress stored outside the generated Skill** — as the upstream
   project already does. Same principle as P1/P2/P6.
4. **Lesson and material drafting for the teacher.** `SirhanMacx/Claw-ED` (MIT,
   65 stars) drafts lessons, student materials and slides from the teacher's
   existing plans, local-first. **Read its limits before promising anything:**
   single-teacher per instance, not multi-tenant, student-facing features
   experimental, and hosted models still receive prompt content even though
   storage is local — so a data-residency client needs local weights.
5. **Content generation node.** `satvik314/educhain` (MIT) for questions,
   lesson plans and flashcards.
6. **Classroom simulation for teacher training.** `THU-MAIC/OpenMAIC` (MIT)
   turns a topic into a multi-agent classroom — useful for rehearsing a lesson
   or training new teachers, which is a sale to the institution rather than to
   students.
7. **Mount and measure.** `ltijs` (Apache-2.0) into the LMS; emit xAPI; keep
   the teacher as the named decision-maker on anything consequential.

**License outcome:** Apache-2.0/MIT throughout.

**Estimate:** 6–8 weeks. **Sells because** the deliverable augments the people
who would otherwise block it — and because it is the one tutor shape that is
legal and politically survivable in every region in this KB.

---

## P8 — Agent on the student record (Global, nothing exists)

**Problem:** advising, retention and early-warning are the use cases
institutions ask for most, and they all need the **student information
system** — not the LMS. Seven Moodle MCP servers exist. **Not one SIS has an
agent interface.** This is the newest gap this KB has identified and it is
wide open.

**Wiring:**
1. **Pick the SIS by region.** `openeducat/openeducat_erp` (LGPL-3.0) where
   Odoo is already in place; `francoisjacquet/rosariosis` (GPL-2.0) for LATAM
   K-12; `GibbonEdu/core` (GPL-3.0) for international K-12;
   `OS4ED/openSIS-Classic` for existing openSIS estates.
2. **Build the MCP server as a separate MIT/Apache process against the SIS
   API** — never as a fork or an in-tree plugin, because all four SIS options
   are GPL-family. The license boundary is the whole architecture here.
3. **Read-only first**, and probably read-only permanently. The student record
   is the most sensitive data in the institution; `Faixiang/Moodle-MCP`'s
   read-only design is the precedent to copy.
4. **Longitudinal framing.** `Keitous/EDUKAI-LONGVIEW` (ISC, 0 stars, Guinea)
   is the only project found that models a learner **across academic periods**
   with evidence retrieval and recurring-difficulty detection, under "agent
   recommends, teacher decides". It is a prototype on synthetic data — take the
   design, not the code.
5. **Join to learning data — now with named implementations.** Mastery
   estimates from `pykt-toolkit` (MIT) plus xAPI events give the agent
   behavioural signal the SIS does not hold. As of 2026-11-13 the xAPI side is
   no longer abstract: stand up `yetanalytics/lrsql` (Apache-2.0) or
   `openfun/ralph` (MIT) as the Learning Record Store and read it through
   `DavidLMS/learnmcp-xapi` (MIT) — see `P9`, which is the buildable half of
   this pattern. **Keep the distinction explicit in the SOW: the LRS holds
   learning activity, the SIS holds the student record.** P9 ships today; this
   pattern still requires the SIS MCP server to be built.
6. **Human-in-the-loop, hard.** Chicago's rule — no AI as the sole basis for
   discipline or special-education placement — is the floor, and the EU treats
   access and allocation decisions as high-risk. Every output is a
   recommendation with evidence attached, routed to a named human.
7. **FERPA/GDPR posture** stated up front: self-hosted inference, no student
   data to model training (and if California AB 1159 passes, that becomes a
   statutory requirement, not a preference).

**License outcome:** MIT/Apache agent layer; GPL-family SIS untouched behind
its own API.

**Estimate:** 6–8 weeks for a read-only advising surface on one SIS. **Nothing
to compete with**, and it is the layer the ask actually requires.

## P9 — The learner-record spine (Global, buildable today, permissive end to end)

**New 2026-11-13.** This is `P8`'s buildable half. `P8` needs an SIS MCP server
that does not exist; **P9 needs nothing that does not exist**, and every
component is MIT or Apache-2.0.

**Problem:** every other pattern in this file tells the agent to "emit xAPI so
the institution can report on it", and until this pass no repo in this KB
implemented the receiver. The practical consequence in delivery is familiar: the
tutor works in the demo, and the institution cannot answer "what did the cohort
actually learn?" — so the pilot does not renew. The missing piece was never the
model. It was the record.

**Wiring:**

1. **Learning Record Store.** `yetanalytics/lrsql` (**Apache-2.0**, 144) by
   default — Postgres 14–18 in production, SQLite for development. Choose
   `openfun/ralph` (**MIT**, 51) instead when the engagement is analytics-shaped
   rather than storage-shaped, when the team wants one Python toolchain end to
   end, or when **EU provenance matters** (France Université Numérique).
2. **Agent interface.** `DavidLMS/learnmcp-xapi` (**MIT**, 16) as the MCP
   server. Three tools — record statement, retrieve progress, manage activity
   vocabulary — and the `practiced` / `mastered` / `experienced` / `achieved`
   verbs are built in, so the pedagogical vocabulary is not something you
   invent. Separate learners by `ACTOR_UUID`; one server serves a cohort.
   Verified against SQL LRS, Ralph and Veracity. **It is 16 stars: read it,
   pin the commit, and expect to maintain your own fork.**
3. **Tutor.** Any agent from `agents/top.md`. `HKUDS/DeepTutor` (Apache-2.0)
   where a learner model is wanted out of the box; `ArnaudGuiovanna/tutor-mcp`
   (MIT) where auditable progression state governed outside the model is the
   priority — it already holds learner state, so the two state stores must be
   reconciled deliberately rather than both left running.
4. **Mastery estimation, quantitative.** `pykt-team/pykt-toolkit` (MIT, 461)
   over the accumulated xAPI statements. This is the step that separates the
   build from a chat log: the LRS gives you the events, pyKT turns them into
   knowledge-tracing estimates the institution can defend.
5. **Platform integration across the network boundary.** LTI 1.3 via
   `Cvmcosta/ltijs` (Apache-2.0, 373) to launch inside Moodle/Canvas/Open edX,
   with grade writeback through AGS. **Never fork the LMS.** The copyleft stays
   on the far side of its own API; everything you ship stays permissive.
6. **Reporting surface.** The LRS is the source of truth for every
   institutional question — cohort mastery, time-on-task, evidence per claim.
   Build the dashboard against the LRS, not against the agent's transcript.

**Why it is defensible:** the LMS belongs to the client and is copyleft; the
model is a vendor's and is substitutable within a quarter. The **learner
record** — mastery state, progression, evidence — is the asset, and this is the
first configuration in this KB where it can be owned, shipped and
Apache-2.0-licensed inside a deliverable.

**Compliance fit by region, at no extra cost:**
- **EMEA** — the Commission's May 2026 draft guidelines place tutoring and
  practice feedback **outside** Annex III high-risk. Keep P9 on practice and
  formative feedback with no grade of record, and it stays out of scope. Pair
  with `openfun/ralph` for EU-origin data infrastructure. The moment it writes
  a grade of record, switch to `P2`.
- **North America** — answers the 85/18 governance gap directly: the LRS *is*
  the audit log, so "what did the AI do with my students" has a queryable
  answer on day one. Self-hosted satisfies FERPA posture.
- **LATAM** — self-hosted on `lrsql` with no learner data leaving the country
  is a direct answer to Mexico's "technological sovereignty" framing, and the
  governance artifact the 87%/26% gap is asking for.
- **APAC** — emits the record needed for Korea's AI Basic Act disclosure and
  India's provenance-marking rules without a separate compliance build.

**License outcome:** Apache-2.0 / MIT end to end. No copyleft in the
deliverable. This is the only pattern in this file for which that is true.

**Estimate:** **3–4 weeks** for LRS + MCP server + one tutor emitting a
governed xAPI statement stream, plus 2 weeks for the pyKT mastery layer and the
reporting surface. The cheapest credible first engagement in this KB, and the
right wedge ahead of `P8`.
