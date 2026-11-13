---
industry: education
region: Global
updated: 2026-11-13
---

# Compose patterns — education

**Thirteen** concrete recipes. Each names the actual repos, the license
consequence, how the pieces wire together, and a rough build estimate. All
components were license-verified on 2026-11-13 (see `agents/top.md` and
`repos/foundations.md`). 🔴 **Count defect fixed this pass: the intro said "Ten
concrete recipes" and then "the rule all eight follow" in the next paragraph.**

**The rule twelve of the thirteen follow:** keep the AI layer permissive
(MIT/Apache/BSD), mount it into the copyleft platform over **LTI 1.3** or
**MCP**, and emit **xAPI** or **Caliper** events. Never fork the LMS.

🔴 **`P13`, new in the sixth pass, is the one exception — and the exception is
the point.** Where the platform itself is **Apache-2.0 and already ships a
pluggable AI provider layer**, there is no copyleft to mount around and no agent
to build: you configure. See `intel/trends.md` `T15`.

**Changes in the fifth pass (2026-11-13), in order of how much they move an
estimate.** (1) **`P12` is new and it is the cheapest SIS engagement in this
file at 2-3 weeks**: if the client's SIS is **OpenEduCat or any Odoo-based
education ERP**, the connector already exists at **433 stars under MIT**
(`erpipe-org/mcp-odoo`, with a three-call write gate) because OpenEduCat is Odoo
addons and the server addresses models by name. **Check what the SIS is built on
before quoting `P8` at 5-7 weeks.** (2) **`P11` is new**: a Caliper-bound North
American engagement is **no longer greenfield** — five of six components exist,
you write only the event store, so **5-7 weeks instead of an unpriceable
build**. (3) **`P8`'s scope narrows**: "not one open-source SIS has an agent
interface" is withdrawn; `P8` now applies to **RosarioSIS and Gibbon**, the two
that genuinely have no connector and no platform beneath them. 🔵 **The
methodological lesson behind (1) and (3), now `T13`: when a vertical system
appears to have no agent surface, check the general-purpose platform it is built
on.**

**Changes in the fourth pass (2026-11-13), in order of how much they move an
estimate.** (1) The **Python LTI constraint below is withdrawn** — see the
correction note; single-language Python LTI deployments are available and that
removes 1-2 weeks from any LTI-shaped engagement. (2) **`P8` is no longer
greenfield**: two MIT agent-to-SIS servers exist and its estimate drops to 5-7
weeks. (3) **`P10` is new** — mounting a permissively licensed *skill* rather
than shipping a service, which is the cheapest education pattern in this file at
1-2 weeks.

**Two changes from the previous edition.** The LTI front door no longer needs
writing from scratch — `Cvmcosta/ltijs` (Apache-2.0, 373 stars) implements the
full LTI Advantage surface. And **P3 is no longer a greenfield build**: seven
Moodle MCP servers exist, so P3 is now a selection-and-hardening pattern, which
is cheaper and lands sooner.

**CORRECTION 2026-11-13 (fourth pass) — the constraint that shaped every
pattern below was wrong.** The previous edition stated that every verified LTI
1.3 library was Node, PHP or Elixir, that **none was Python**, and that every
pattern therefore had to assume a two-process shape with a Python agent behind a
Node or PHP LTI front door, with the seam budgeted. **`dmitry-viskov/pylti1.3`
(MIT, 138 stars, 84 forks) is a Python LTI 1.3 Advantage implementation** with
Assignments and Grades, Names and Roles, Deep Linking, and shipped Django and
Flask adapters. A single-language Python deployment is available for every
pattern in this file.

**What to do with that, concretely.** The two-process shape is no longer
mandatory, but it is still often right, and the choice is now an engineering
decision instead of a constraint:

- **Choose `pylti1.3`** when the team is Python, the agent is Python (nearly all
  of them here are), and one language, one container and one dependency set
  matter more than library maturity. It removes an inter-process seam, a
  serialization format and a deployment unit from every estimate below — worth
  roughly **1-2 weeks** on a first LTI engagement.
- **Choose `ltijs` (Apache-2.0, 373)** when LTI conformance is contractual or
  the client's platform integration is unusual. It is the most-used, most
  exercised implementation and the reference for the full Advantage surface.
- **Weigh the maintenance risk honestly either way.** `pylti1.3` has an **empty
  GitHub Releases page**, a newest PyPI version of **2.0.0**, and a third-party
  report of no publish in roughly three years. Pin it, vendor it, and own the
  patch path — on an **authentication-boundary** component that is a real cost,
  and it is the one argument that still favours `ltijs` on a long engagement.

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
   🔴 `kaushal0494/AITutor-EvalKit` (**NO licence file — not adoptable; `p801`
   refuted the `MIT` claim and `p802` re-verified the absence at `HEAD`
   `a71078456a90`. Read it, do not ship it**) for pedagogical effectiveness,
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

## P8 — Agent on the student record (Global, topology proven; now scoped to RosarioSIS and Gibbon — check `P12` first)

**Problem:** advising, retention and early-warning are the use cases
institutions ask for most, and they all need the **student information
system** — not the LMS.

**Status changed 2026-11-13 (fourth pass).** This pattern was titled "nothing
exists" through three passes. It is no longer greenfield: **two MIT MCP servers
reach a real SIS** — `oliverhruby/edupage-mcp` (4 stars, **31 tools** over
EduPage, the SIS used across Slovakia and Czechia, including role-aware student
switching and 2FA) and `sukhrobyangibaev/mcp_hemis_student` (0 stars, over
HEMIS, used by Uzbek universities). Both are single-developer projects against
**national proprietary platforms**, and EduPage's runs on **undocumented
endpoints** through a community library.

**Status changed again 2026-11-13 (fifth pass) — read this before the paragraph
below it.** The sentence *"not one open-source SIS has an agent interface"* is
**withdrawn**. **OpenEduCat (LGPL-3.0, 911 stars, 789 forks) is reachable
today** by a generic Odoo MCP server, because it is Odoo addons and those
servers address models by name. **If the client runs OpenEduCat — or any
Odoo-based education ERP — do not use this pattern; use `P12`, which is a
configuration exercise rather than a build.** `P8` below remains the right
pattern for the two cases that are still genuinely unserved: **RosarioSIS**
(GPL-2.0, 654, PHP/Postgres, LATAM K-12) and **Gibbon** (GPL-3.0, 638,
PHP/MySQL, international K-12), neither of which has a general-purpose platform
underneath to inherit a connector from. 🔴 **`frappe/education` is unresolved —
check for a generic Frappe MCP server before quoting this pattern for it.**

**What that changes for the engagement:** the topology is proven, so this is a
**selection-and-build** pattern rather than a bet — cheaper to sell and faster
to de-risk, because `edupage-mcp` is a working reference for the tool surface
(31 tools over timetable, grades, homework, attendance) and
`zavora-ai/mcp-education` (Apache-2.0) is a working reference for **gating
writes in the tool contract**: 9 read-only tools plus 3 writes that require
approval. 🔴 **Superseded sentence, kept visible rather than deleted so the
correction is auditable:** this pattern used to continue *"What has not changed:
not one open-source SIS — OpenEduCat, RosarioSIS, Gibbon, openSIS,
`frappe/education` — has an agent interface."* **OpenEduCat has one** (see the
fifth-pass note above and `P12`), so the unserved list is now **RosarioSIS,
Gibbon, openSIS**, with `frappe/education` **unresolved pending one search for a
generic Frappe connector**. For those, the build below is still the work —
**quote the proven topology, not a solved problem.**

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
   read-only design is the precedent to copy. **If writes are unavoidable**, copy
   `zavora-ai/mcp-education`'s contract instead of inventing one: declare the
   read-only and approval-required tools as **separate, labelled sets in the
   server itself**, so the boundary survives a change of host and shows up in an
   audit. Leaving write-gating to the agent host is the failure mode.
3b. **Steal the tool surface rather than designing it.** `edupage-mcp`'s 31
   tools are a worked answer to "what does an agent need from a school SIS"
   (timetable, grades, homework, attendance, daily summary, role-aware student
   switching, 2FA), and `EdyVision/student-services-mcp` — **license
   unverified, synthetic data, do not adopt** — sketches the retention surface
   an advising agent needs: `fetch_student_dropout_risk`,
   `fetch_high_risk_students`, `fetch_attrition_statistics`,
   `fetch_attrition_feature_importance`. Two free references for the hardest
   design question in this pattern.
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

**Estimate:** **5-7 weeks** for a read-only advising surface on one SIS, revised
down from 6-8 now that the tool surface and the write-gating contract both have
working references to copy rather than needing design from scratch. Still
**nothing to compete with on any open-source SIS**, and it is the layer the ask
actually requires.

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

## P10 — Mount a licensed skill, not a service (Global, cheapest entry in this file)

**New 2026-11-13 (fourth pass).**

**Problem:** a client wants a credible tutoring capability in weeks, not a
platform in quarters — and the usual answer, "stand up a tutor service," buys
them a deployment, an inference bill, a security review and a maintenance
burden before any teaching happens.

**The opening:** `janestreet/agent_skills` (**MIT, 7.9k stars, 510 forks, 2
commits**) is a *skill*, not software — a `SKILL.md` instruction set that turns
any SKILL.md-compatible host (Claude Code, Codex, OpenClaw) or even a plain
chatbot into a strict Socratic tutor: a 3-5 question diagnostic, a 4-10
sub-skill map rated 0-5, **one question at a time**, spaced review, final
assessment. It ships no code, so there is **no dependency tree, no CVE surface
and no container**. It is also the first artifact of its class this KB can
actually use: `education-agent-skills` (977 stars) is the same shape under **CC
BY-SA**, which is a content license with share-alike and the wrong instrument
for a deliverable. This one is MIT.

**Wiring:**
1. **Start from the skill, fork it in-repo.** Take `socratic-tutor` and adapt
   the rubric and sub-skill map to the client's curriculum. This is prompt and
   pedagogy work — subject-matter experts can own it, which is the point.
2. **Add the guardrails the skill does not enforce.** A `SKILL.md` *asks* the
   model to behave; it cannot *prevent* it from answering. Port the three
   controls from `vulinh1704/ai-tutor-agent` (MIT): the **hint ladder** with a
   configurable escalation cap, the **answer-leak guard** that regenerates a
   draft which gives away the answer, and **rubric scoring whose totals are
   computed in code rather than by the model**. Without these, "strict Socratic
   tutor" is an instruction, not a property.
3. **Host it where the learner already is.** Mount as an LTI 1.3 tool with
   `dmitry-viskov/pylti1.3` (MIT) — now a **single-language Python** path, see
   the correction at the top of this file — or reach into the LMS over
   `vishalsachdev/canvas-mcp` (MIT, 324) or `Faixiang/Moodle-MCP` (MIT, 206,
   read-only).
4. **Make it reportable.** Emit xAPI through `DavidLMS/learnmcp-xapi` (MIT) into
   `yetanalytics/lrsql` (Apache-2.0), using the skill's own 0-5 levels as the
   `practiced` / `mastered` progression. The sub-skill map is already the shape
   an LRS wants, which is why this composes cleanly with `P9`.
5. **Measure it, with the caveat stated — and the caveat is now a licence, not
   just coverage.** `kaushal0494/AITutor-EvalKit` (🔴 **no licence file; the `MIT`
   claim is refuted on bytes, re-verified `p802` at `HEAD` `a71078456a90`**, 4
   stars, mathematics only) is still the only pedagogy-specific eval harness in
   this KB. 🔴 **It cannot go into a client deliverable.** Use it as an internal
   reference, tell the client what it does not cover, and request a grant upstream.

**Why this is the cheapest pattern here:** steps 1-2 are the deliverable and
steps 3-5 are reuse. There is no model to train, no service to scale, and the
licensing question — normally the longest conversation in an education
engagement — is settled in one line: **MIT end to end**.

**Regional read:**
- **North America** — the 85%-of-educators-use-AI / 18%-have-guidance gap is a
  governance gap, and a reviewable `SKILL.md` plus a code-enforced rubric is an
  artifact a district can actually approve. Nothing leaves the host if the host
  is self-hosted.
- **EMEA** — no grade of record means no Annex III high-risk classification;
  stay on practice and formative feedback and the EU AI Act high-risk
  obligations (now dated **2 December 2027** on the Digital Omnibus reading) do
  not bind. The moment it grades, switch to `P2`.
- **LATAM** — the lowest-cost route to the governance artifact the UNESCO
  IESALC 87%/26% gap is asking for; translation and curriculum adaptation are
  the work, and both are local-team work.
- **APAC** — a skill file is reviewable text, which is the cheapest way to
  satisfy Korea's AI Basic Act disclosure duties and India's provenance-marking
  rules without a compliance build.

**License outcome:** MIT end to end, including the pedagogy artifact itself.

**Estimate:** **1-2 weeks** for an adapted, guardrailed skill mounted in one
LMS, plus 1 week to wire the xAPI stream. The cheapest credible engagement in
this KB — and the right thing to sell when the client's real question is "can
you show us something that teaches by March."

**The trap, stated plainly:** 7.9k stars on **two commits** measures attention,
not maturity. This is a well-designed prompt from a firm with a strong
engineering reputation, not a maintained product, and it will not be patched for
you. Fork it and own it from day one.

## P11 — Caliper-bound analytics layer (North America, newly priceable)

**Problem:** a North American higher-ed client's procurement document names
**Caliper Analytics**, not xAPI, as the learning-analytics standard. Through
four passes this KB answered that with "no open starting point in this base —
that is a build, and it must be priced as one." **That answer was wrong and cost
money.** Five of the six components now exist.

**When to use this instead of `P9`.** `P9` (the learner-record spine) is the
default and is permissive end to end on xAPI. **Use `P11` only when a contract
names Caliper.** Where the client is free to choose, choose xAPI — the reason is
the single asymmetry in the table below, and it is decisive.

**Step 0 — ask which Caliper *version* the contract names. Do this in week one.**
The only verified permissive sensor defaults to **v1.1**
(`http://purl.imsglobal.org/ctx/caliper/v1p1`). The only **v1.2** implementation
found anywhere is **unlicensed**. A 1.2 client is materially further from this
shelf than a 1.1 client, and no procurement document this KB has seen
distinguishes them. **If the answer is 1.2, the sensor is also a build and this
estimate doubles.**

**The stack, with what you get and what you write:**

| Layer | Repo | License | You |
|---|---|---|---|
| Sensor / client | `CarnegieLearningWeb/caliper-ts` | **MIT** | **Adopt.** TypeScript Sensor API, 225 commits. Entity factories for Assessment, AssessmentItem, Person, Session, SoftwareApplication, Membership |
| LMS emitter (Moodle) | `open-lms-open-source/moodle-logstore_caliper` | GPL-3.0 | **Install.** Expander → Translator → Emitter, immediate or batched, Moodle 2.7+ |
| Event store | 🔴 **nothing permissive exists** | — | **BUILD. This is the line item.** |
| Analysis / dashboards | `tl-its-umich-edu/caliper-event-analysis` | **Apache-2.0** | **Adopt and extend.** U-M + CSCAR notebooks |
| Profile reference | `UnizinAnalytics/caliper-net-public` | LGPL-3.0 | **Read, do not link.** Nine Metric Profiles = the scope definition for your store |
| PHP reference | `tl-its-umich-edu/caliper-php-public` | LGPL-3.0 | **Read** if the client is a PHP shop (Moodle, Chamilo) |

**Wiring, concretely.**

1. **Install the Moodle logstore plugin** and point it at your store: it needs
   an Event Store URL, an API key, a send-immediately flag and a batch size.
   Start batched; switch to immediate only if a dashboard needs sub-minute
   latency. 🟢 **GPL-3.0 here is correct and harmless — a Moodle plugin lives
   inside a GPL-3.0 host and does not reach your separately deployed agent
   layer.** Say this to any client who has internalised "do not fork the LMS":
   the rule is about forking the platform, not installing a plugin.
2. **Build the event store against the nine-profile list** from
   `caliper-net-public` — Base, Session, Reading, Annotation, Assignable,
   Assessment, Assessment Item, Outcome, Media. Accept
   `POST /ims/caliper/v1p1/events` with bearer-token auth and persist the
   envelope whole. **`open-ent/caliper` is the shape to copy** (it implements
   exactly this as an event store **and** a sensor, with 33 unit tests) — 🔴
   **read it, do not vendor it: no licence on the page.**
3. **Emit from the agent layer with `caliper-ts`**, so the agent's tutoring and
   assessment activity lands in the same store as the LMS's. 🔴 **Build caveat
   that will surprise a dev team: `caliper-ts` publishes to the GitHub Package
   Registry as `@imaginelearning/caliper-ts`, not public npm** — the build needs
   an `.npmrc` scoped to `@imaginelearning`. Budget an hour of CI plumbing and
   **vendor it**: 0 stars means no community will patch it for you.
4. **Stand up dashboards from `caliper-event-analysis`.** Apache-2.0, so the
   notebooks can seed the client deliverable directly. **This is the layer the
   client actually buys** — events nobody reads are a cost centre.
5. **Keep the agent layer MIT/Apache and separately deployed**, per this KB's
   standing rule. Nothing in the GPL-3.0 or LGPL-3.0 rows above is linked into
   it: the plugin runs inside Moodle, and the LGPL-3.0 repos are read, not
   imported.

**Regional fit.** 🟢 **North America is the reason this pattern exists** — and
the provenance helps in procurement: the nine-profile reference comes from
**Unizin**, the US higher-education consortium, and the analysis layer from the
**University of Michigan**. 🟡 **EMEA** gets one bonus: `open-ent/caliper` is a
French public-education platform's module, usable as design evidence in an EU
data-sovereignty conversation (and the highest-value licence request on this
board). 🔴 **APAC and LATAM: do not sell this pattern.** Nothing in those
regions' procurement specifies Caliper; `P9` on xAPI is strictly better there.

**License outcome:** MIT/Apache in everything you ship. GPL-3.0 confined to the
Moodle plugin inside Moodle; LGPL-3.0 read-only.

**Estimate:** **5-7 weeks** — 1 week plugin + sensor wiring, **3-4 weeks event
store** (the whole variable), 1-2 weeks dashboards. 🔵 **Compare honestly in the
proposal: `P9` on xAPI is 3-4 weeks because `yetanalytics/lrsql` (Apache-2.0,
144★, Postgres 14–18 / MariaDB / MySQL / SQLite) *is* the store.** The entire
Caliper premium is one missing component. **A client free to choose should see
that number.**

**The trap:** quoting the old "Caliper is greenfield" line. It overprices the
work by a factor and loses the deal to someone who has read the shelf.
**The second trap:** reading licences off GitHub's sidebar. `caliper-ts` shows a
bare "License" link and **is MIT** — the grant is in the `LICENSE` file
(`MIT License / Copyright (c) 2021 Imagine Learning`). A sidebar-only check
records this whole pattern as impossible.

## P12 — Agent on an Odoo-based education ERP (Global, configuration not build, cheapest SIS engagement in this KB)

**Problem:** the client wants advising, retention or early-warning on the
**student record**, and runs **OpenEduCat** or another Odoo-based education ERP.

**Why this is separate from `P8`, and why it is the first thing to check.**
`P8` is a 5-7 week build. **This is a configuration exercise, because the
connector already exists at 433 stars and the SIS is just Odoo addons.**
OpenEduCat (LGPL-3.0, **911 stars, 789 forks**, branch `19.0`) ships
`openeducat_core`, `_admission`, `_exam`, `_fees`, `_attendance`, `_timetable`,
`_parent`, `_library` — and the Odoo MCP servers address models **by name**, so
`op.student`, `op.admission`, `op.exam.attendees` and `op.fees` need no new code.
🔵 **Ask "what is your SIS built on" before "does your SIS have an API."**

**Step 1 — choose the connector by who must own the write policy.** This is the
only real decision in the pattern.

| | `erpipe-org/mcp-odoo` | `ivnvxd/mcp-server-odoo` |
|---|---|---|
| License | **MIT** | MPL-2.0 (file-level weak copyleft) |
| Stars / forks | **433** / 198 | 415 / 190 |
| Tools | 41 | 17 |
| Odoo | 16–19 (smoke-tested 16.0/17.0/18.0/19.0) | 16.0+ standard mode; JSON-2 + API key on 19+ |
| Write gate lives in | **the agent** | **the institution** |
| Mechanism | `preview_write` → `validate_write` → `execute_approved_write`; single-use, same-process, expiring token; `confirm=true`; `ODOO_MCP_ENABLE_WRITES=1`; `ODOO_MCP_ELICIT_WRITES=1` adds a native prompt; direct `create`/`write`/`unlink` **blocked**; `execute_method` allowlisted only | Companion Odoo module: per-model allowlist with separate read / write / create / delete, layered on Odoo's own access rights and record rules |
| Pick it when | the studio operates the deployment | the client's Odoo admin must hold the control — **most institutional engagements** |

🔴 **Never ship `ivnvxd`'s "YOLO mode".** It requires no companion module,
bypasses **all** MCP-level access control, exposes 200+ models, and in full form
permits delete; its own README restricts it to development and testing. **Grep
for it in any deployment you inherit.**

**Step 2 — scope the model allowlist to the education models and nothing else.**
This is the whole security posture of the engagement, and it is the reason to
prefer `ivnvxd` + companion module in an institutional setting: an Odoo instance
running OpenEduCat is usually **also** running finance and HR. An agent that can
read `op.student` must not be able to read `hr.employee` or `account.move`.
🟢 **Inherited governance is the selling point: "your agent inherits Odoo's
access rights and record rules" is a stronger story than anything a bespoke
education MCP server offers** — of the three proprietary-SIS servers in this KB,
none gates writes and one replays the student's own credentials.

**Step 3 — read-only first, always.** Ship advising and early-warning on reads
(`search_records`, `read_record`, `aggregate_records`, `get_model_fields`) and
leave writes disabled. `aggregate_records` is what makes cohort-level retention
questions answerable without exporting student rows.

**Step 4 — add writes only behind the gate, and only for one model.** Typical
first write is an advising note or a flag on the student record, never grades or
fees. On `erpipe-org`, writes stay off until `ODOO_MCP_ENABLE_WRITES=1`; on
`ivnvxd`, until the companion module grants write on that one model.

**Step 5 — emit xAPI so the institution can report on the agent.** Pair with
`P9`: `DavidLMS/learnmcp-xapi` (MIT) into `yetanalytics/lrsql` (Apache-2.0).
The SIS holds the student record; the LRS holds what the agent did. 🔴 **Keep
them separate** — this KB's most expensive available mistake is scoping an
advising engagement against the wrong one of the two.

**Regional fit.** Odoo's education footprint is heaviest in **India, LATAM and
EMEA SMB/private education**, so this is one asset serving three regions.
🟢 **LATAM and APAC private-education groups are the best first targets**:
Odoo is common in both and the connector is free. 🔴 **It does not help a LATAM
K-12 public engagement on RosarioSIS, or an international-school engagement on
Gibbon** — those are `P8`, and that distinction is worth getting right in the
first call because it is the difference between 2 weeks and 7.

**License outcome:** MIT end to end with `erpipe-org`. With `ivnvxd`, MPL-2.0 is
**file-level** weak copyleft — publish changes to its own files, combine freely
with proprietary code; it needs a licence note in the deliverable, not a
redesign. OpenEduCat itself stays LGPL-3.0 and **is not forked** — you connect
to it, which is this KB's standing rule applied to the SIS layer.

**Estimate:** **2-3 weeks** for read-only advising on an existing OpenEduCat
instance, plus 1 week for the gated first write, plus 1 week for the xAPI
stream. **The cheapest SIS engagement in this KB by a wide margin**, and the
right answer when a client with Odoo asks for the thing `P8` prices at 5-7
weeks.

🔴 **The trap, and it must be in the proposal, not just here.** This path is
**architecturally verified and has not been run** (`Gap 286`): the connectors'
tools are model-generic and OpenEduCat is Odoo addons — both read off the
repository pages — but **no Odoo instance has been stood up, OpenEduCat
installed, and a tool called against `op.student`.** Say *"the connector is
generic and the SIS is Odoo addons"*, never *"we have run it."* 🟢 **Do that run
first: it is a day of work and it converts this pattern's entire estimate from
inferred to demonstrated.** **Second trap:** `erpipe-org/mcp-odoo` was formerly
`tuanle96/mcp-odoo`, which is still what search results return — and its
maintainer sells a hosted product (ERPipe) built on it. The MIT grant is real;
the roadmap has a commercial owner. Pin a commit.

## P13 — Sovereign LMS-native AI on OpenOLAT (EMEA, configuration not build — and the only pattern here with no agent in it)

**When to use.** Greenfield or German-speaking-EMEA platform choice, where the
client has a **stated data-sovereignty or EU AI Act requirement** and the usual
answer ("mount a permissive agent into a copyleft LMS over LTI") either cannot
clear data protection or cannot be licensed the way the client needs the derived
product licensed. **This is the cheapest pattern in this file when it fits, and
it fits rarely — check the three disqualifiers below before pricing it.**

**Why it exists.** Every other pattern here assumes the platform is copyleft and
AI-less. [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) is
**Apache-2.0** (451 stars, 165 forks, 32,338 commits, Java; University of Zurich
origin, maintained by frentix GmbH, Switzerland) **and carries a first-party
pluggable AI layer in-tree**. So the derived product can be licensed however the
client wants, and the AI work is configuration plus a provider, not a build.

### The components — all verified in-repo this pass

| Piece | Where | License |
|---|---|---|
| The platform | `github.com/OpenOLAT/OpenOLAT` | **Apache-2.0** (read from `LICENSE`, not the sidebar) |
| Provider SPI | `org/olat/core/commons/services/ai/` — `AiSPI`, `AiEmbeddingSPI`, `AiApiKeySPI` | Apache-2.0 |
| The provider slot you use | `spi/generic` — **any OpenAI-compatible endpoint** | Apache-2.0 |
| In-process embeddings | `spi/localonnx` — `LocalOnnxSPI`, `QwenOnnxEmbeddingModel` | Apache-2.0 |
| Self-hosted inference | `vllm-project/vllm` (Apache-2.0) or `ollama/ollama` (MIT) — from `repos/foundations.md` | Apache-2.0 / MIT |
| Telemetry out | `yetanalytics/lrsql` (Apache-2.0) or `openfun/ralph` (MIT) over **xAPI** | Apache-2.0 / MIT |

### How it wires together

1. **Deploy OpenOLAT** as the LMS. No fork, no plugin, no LTI tool — but also
   **no copyleft reaching the derived product**, which is the whole reason to be
   here rather than on Moodle.
2. **Stand up a self-hosted OpenAI-compatible endpoint** — vLLM for throughput,
   Ollama for a small install — **inside the institution's own network
   boundary.**
3. **Configure the `generic` provider** to point at that endpoint. Per-function
   provider and model selection means `essay-grading` and
   `mc-question-generator` can run on different models, and a function can be
   left switched off entirely.
4. **Leave `localonnx` serving embeddings in-process** — these never leave the
   JVM, so the retrieval and `taxonomy-matching` side needs no network boundary
   argument at all.
5. **Turn on the features you can defend, one at a time**, from the five in
   `AiFeature`: `mc-question-generator`, `image-description-generator`,
   `essay-generation`, `essay-grading`, `taxonomy-matching`.
   `image-description-generator` is the easiest first win — it is an
   **accessibility** feature, which changes the conversation from "AI in the
   classroom" to "WCAG compliance", and it is user-controlled.
6. **Emit xAPI to an LRS** (`lrsql` or `ralph`) so the institution can report on
   learning activity independently of the LMS — the spine from `P9`, unchanged
   and fully compatible with this pattern.

### Why it survives an EU AI Act review

Mapped against the deployer obligations in `intel/market.md` → EMEA:

- **Article 50 transparency (applies 2 August 2026, *not* postponed by the
  Digital Omnibus):** learners must be told they are dealing with an AI system.
  `AiFeature` carries a **learner-facing name and a one-sentence description per
  feature** (`getI18nUserNameKey`, `getI18nDescriptionKey`) as part of the data
  model — the disclosure surface is built in, not bolted on.
- **Human oversight and per-learner control:** `AiFeature.isUserControlled()` —
  *"a person can switch this feature on or off in the user settings, on top of
  the system default of the administrator"*. **Opt-out is a platform primitive.**
- **Logging:** `AiUsageLog` / `AiUsageLogStatus` / `AiUsageLogSearchParams`
  record every AI call with token/cost attribution — this is simultaneously the
  audit artifact and the FinOps artifact.
- **Article 27 FRIA** (public bodies deploying high-risk systems) and the
  **2 December 2027** high-risk deadline for stand-alone education systems:
  running inference inside the institution's boundary removes the third-country
  transfer question from the assessment entirely.
- **Emotion recognition in education has been prohibited since 2 February 2025.**
  Nothing in `AiFeature` goes near it — confirm no custom provider adds it.

### Estimate

**3–5 weeks**, and it is mostly not AI work: deployment and SSO (1–2 weeks),
self-hosted endpoint plus `generic` provider configuration and model selection
(1 week), feature-by-feature enablement with the data-protection sign-off that
each one needs (1–2 weeks). **Compare with 8–12 weeks for the equivalent
mount-an-agent-into-Moodle shape, which then still owes the client a
data-protection story for the inference hop.**

### Three disqualifiers — check these first

1. 🔴 **An existing Moodle / Canvas / Open edX estate.** This pattern is a
   platform choice, not a migration plan. With an incumbent LMS, use `P3`, `P6`
   or `P9`. The installed base is overwhelmingly on the copyleft three.
2. 🔴 **"It all runs locally" is not true and must not be proposed.** The only
   local model class is `QwenOnnxEmbeddingModel` — **embeddings**. Essay grading
   and question generation call a provider. The defensible claim is *"inference
   runs on infrastructure you control"*, which the `generic` provider delivers
   and which is what a data-protection reviewer actually asks for.
3. 🔵 **An external agent may not be able to reach these features.** The AI
   services are Java interfaces; **nothing read this pass shows HTTP exposure**,
   and no MCP server for OpenOLAT exists. If the engagement needs an *external*
   agent orchestrating across systems, this pattern does not yet reach it —
   resolve that open question (`agents/trending.md`, sixth pass) before
   committing. **As scoped above, P13 is LMS-native AI, not agentic AI.**

### The contribution opportunity, stated because it is unusually well shaped

**There is no MCP server for OpenOLAT**, while Moodle has three and Canvas two.
The platform is **Apache-2.0**, so a `openolat-mcp` is a contribution rather
than a procurement, and it is the missing piece that would make this pattern
composable with every agent pattern in this file. 🔴 **Not opened unprompted —
it is an outward action**, and this KB's standing rule (see `Gap 240`) is that
outward actions are proposed, not taken.

## P14 — The AI deployment registry (Global, compliant in four regimes at once, and the cheapest first engagement in this file)

**New `p802` (seventh pass, 2026-11-13).** Built from `T16`. 🔵 **This is the only pattern in this
file whose output is an inventory rather than a capability** — and it is the input every other
pattern here silently assumes.

🔴 **State the unusual thing first: there is no repository to adopt for the registry itself.** A
search of this pass found no open-source education AI deployment registry. The registry is ~300 lines
of schema and CRUD; **the value is in what it is wired to**, and every one of those components is
already byte-verified in this KB.

### The components — all verified in this base

| Component | Repo | Grant | Role in this pattern |
|---|---|---|---|
| Learner-record spine | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | MIT | The **only** agent↔learner-record write path in this KB. xAPI 1.0.3 statements make agent activity *reportable*; `ACTOR_UUID` separation is what makes **per-learner opt-out** mechanically enforceable rather than a policy sentence |
| LRS target | SQL LRS / Ralph / Veracity | — | Verified targets of `learnmcp-xapi`. The registry stores *which* LRS a deployment writes to; the LRS stores the activity |
| Review gate | [`littlecookie0722/AI-Teaching-Agent`](https://github.com/littlecookie0722/AI-Teaching-Agent) | MIT | Its shape, not its code: **nothing publishes automatically**, a human decision gates export. This is Oklahoma's "teacher review of AI output" implemented rather than asserted |
| Write-boundary reference | [`zavora-ai/mcp-education`](https://github.com/zavora-ai/mcp-education) | Apache-2.0 | `9` read-only + `3` approval-gated write tools. The **server declares** the read/write boundary — copy this contract for any registry-registered tool that touches a gradebook |
| Governed platform connector | [`ivnvxd/mcp-server-odoo`](https://github.com/ivnvxd/mcp-server-odoo) | MPL-2.0 | Where the institution must own the policy: per-model allowlist in a **companion Odoo module**, so the client's administrator — not an env var — decides agent reach. 🔴 Ban "YOLO mode" in the registry's own policy text |
| Permissive LMS host | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | Apache-2.0 (`10,982 B`, affero×`0`, payload-verified) | The EMEA sovereignty-compatible host. See `P13` |

### How it wires together

1. **Enumerate.** One row per *deployment*, not per product: tool, version, vendor, which cohort,
   which subject, who approved it, what it writes to, and **whether its output is the sole basis for
   any decision**. That last field is not optional ceremony — it is the exact predicate that decides
   Vietnam's high-risk tier and the EU's profiling question.
2. **Tier.** Apply the Philippines' DepEd Order `003` risk tiers. **Grading and admissions are the
   high-stakes tier everywhere**; a reading-practice tutor is not.
3. **Bind each row to telemetry.** A registered deployment must name its LRS endpoint. Agent
   activity lands as xAPI statements through `learnmcp-xapi` under an `ACTOR_UUID`.
4. **Enforce opt-out at the identifier, not in prose.** Parent opt-out (Oklahoma) = suppress that
   learner's `ACTOR_UUID`. The registry holds the flag; the spine honours it.
5. **Gate the high-stakes tier behind review.** Anything in the grading/admissions tier adopts
   `AI-Teaching-Agent`'s no-automatic-publication shape and `mcp-education`'s declared write boundary.
6. **Emit the compliance artifact.** The same table renders an EU **Article 27 FRIA** input, a UK
   **DfE Generative AI Product Safety Standards** conformance list, a Philippine registry return, and
   a district policy appendix for **Ohio / Maryland / Idaho / Oklahoma / Virginia / Tennessee**.

### Why it survives review in four regimes at once

🟢 **It does not depend on the contested EU date.** Whether education high-risk obligations bite in
**August 2026** or **2 December 2027** under **Regulation (EU) 2026/1744**, the registry is identical
work and is compliant under both — this base's standing advice to plan to the earlier date, with no
rework if the later one holds. 🟢 **Article 50 transparency applies from 2026-08-02 regardless**, and
the registry is where the disclosure obligation per deployment is tracked.

### Estimate

**`3`–`5` weeks** for the registry and one bound telemetry path, against an institution that already
has an LMS. **`8`–`10` weeks** with the review gate and a governed platform connector in the
high-stakes tier. 🔵 **Deliberately small** — this is the engagement that *qualifies* the larger ones
by producing the inventory they need.

### Three disqualifiers — check these first

1. 🔴 **No LMS or SIS the client actually controls.** Without one, there is no deployment population
   to register, and `learnmcp-xapi` has nothing to bind to.
2. 🔴 **The client wants detection of student AI use.** `T953` settled this: UI-driving agents are
   near-undetectable server-side and Instructure marked the request **`Will not consider`**. That is
   an assessment-**design** engagement, not a registry.
3. 🔴 **The client expects the registry to be bought.** No open-source implementation exists (`T16`).
   If procurement requires an off-the-shelf product, this pattern does not apply this quarter.

---

## P15 — The tutor-efficacy gate (Global, build-not-adopt, and the answer to the question every regulator is about to ask)

**The question.** A client deploys a tutoring agent. A ministry, an accreditor
or a procurement officer asks: *does it teach, and how do you know?* 🔴 **As of
`p803` there is no open-source instrument a studio can ship to answer this** —
`T17` establishes that the four credible education benchmarks are ungranted,
contradictorily granted, or `0★`. This pattern builds the gate instead, from
components whose grants this base has read **at the byte level**.

### The components — every grant payload-verified

| Component | Repo | Grant (how established) | Role |
|---|---|---|---|
| Harness shape | [`Kobby-Adjei/ai-tutor-benchmark`](https://github.com/Kobby-Adjei/ai-tutor-benchmark) | 🟢 **MIT** — `LICENSE`, `1,351 B`, `affero×0`, title `MIT License`, `HEAD` `23fc97462c8f` | **Template, not dependency** (`0★`). Three-stage structure + simulated-learner cards + the split code/data grant to copy |
| Mastery model | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 **Verified on this base's shelf** | Bayesian Knowledge Tracing — the ground truth the gate scores *against*. Mastery movement, not answer accuracy |
| Learning-record store | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 **Apache-2.0**, `144★` | Holds the xAPI statements the gate reads. **Already the spine in `P9`** |
| Agent → record edge | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | 🟢 **MIT**, `16★` | Lets the tutor under test write its own activity, so the gate needs no bespoke instrumentation |
| Methodology (read, do not vendor) | [`eth-lre/mathtutorbench`](https://github.com/eth-lre/mathtutorbench) · [`kixlab/TutorCaseBench`](https://github.com/kixlab/TutorCaseBench) | 🔴 **Ungranted / contradictory — cite, never copy** | Task decomposition and rubric structure. **Papers are citable; the repos are not shippable** |

### How it wires together

1. **The tutor under test writes to the LRS, not to a log.** Mount
   `learnmcp-xapi` against `lrsql`. Every hint, every attempt, every scaffold
   becomes an xAPI statement with a learner and a timestamp. 🔵 **This is the
   step that makes the gate reusable across clients** — it measures the record,
   not the product.
2. **OATutor's BKT supplies the outcome variable.** A tutor "teaches" when
   posterior mastery rises on *subsequent unaided* items. Scoring the tutored
   turn itself measures compliance, not learning.
3. **Three stages, after `ai-tutor-benchmark`'s shape.** (a) Static rubric pass
   over held-out dialogues; (b) simulated learners with declared personas —
   including the struggling and the disengaged, which is `TutorCaseBench`'s
   contribution; (c) live A/B against an unaided control arm.
4. **Split the grant at the repository level, on day one.** MIT on the harness,
   CC BY 4.0 on the learner cards and the dialogue data. 🔴 **This is the single
   thing four institutional benchmarks got wrong**; it costs one `LICENSE` file
   and one README section to get right.
5. **Emit the result into the deployment registry from `P14`.** The registry row
   for the tutor gains an efficacy field with a date and a method. That is the
   artifact the regulator actually wants.

### Why it survives review

- **EU AI Act, Annex III.** Assessment and admissions AI is high-risk, and
  Article 27's Fundamental Rights Impact Assessment presupposes evidence about
  the deployed system. A dated efficacy measurement **is** that evidence.
- **Vietnam.** Automated assessment is named high-risk and status turns on
  whether output is *the sole basis for a decision* — a per-deployment property
  the gate records per deployment.
- **Oklahoma, DC, Texas `HB2400`.** Each restricts what AI may decide unaided.
  🟢 A control arm is the only way to show a human-in-the-loop design did not
  degrade learning — which is the argument that wins the exemption.

### Estimate

**6–8 weeks** for the first client, **2–3 weeks** for each one after. Stage (a)
is a week. Stage (b) is most of the cost — persona design is the skilled part
and is **the reusable asset across the whole studio**. Stage (c) needs a cohort
and a term, so it is sold as a follow-on, not bundled.

### Three disqualifiers — check these first

1. 🔴 **No unaided post-test is possible.** If the client will not hold out items
   or a control arm, stages (a) and (b) are all you can deliver — sell those, and
   say plainly that they measure dialogue quality, not learning.
2. 🔴 **The tutor is a closed third-party product with no record egress.** Without
   xAPI out, step 1 fails and the gate becomes bespoke per vendor.
3. 🔴 **The client wants a benchmark *number* for marketing.** This produces a
   dated, scoped, method-bound finding. It is evidence for a regulator, not a
   league-table score, and promising the latter will end badly.

🔵 **Why this is `build`, not `adopt` — stated plainly.** It is the only pattern
in this file besides `P14` with no adoptable upstream, and for the same reason:
the artifact that is needed is the one the field publishes as a paper and
forgets to license.

## P16 — The 64-campus policy pack (North America, deadline-driven, and the only pattern here with a date already set)

**Why this pattern exists.** `T18`: SUNY's systemwide AI policy requires each of
**64 campuses** to publish or update an AI policy **no later than 2026-12-31** —
**48 days from the pass that found it** — supported by a total of **31** AI for
the Public Good Fellows. 🔵 **Every other pattern in this file sells against a
trend. This one sells against a calendar**, and the same shape recurs wherever a
system or ministry sets a campus-level deadline (Ohio's July 2026 district
mandate is the K-12 analogue already recorded in `intel/market.md`).

🔴 **Provenance: the SUNY facts are search-tier** (`suny.edu` unreachable from the
pass that recorded them; `ACTION p804-V`). **Confirm the date and scope with the
client before pricing against it** — the pattern holds regardless, the deadline is
what must be checked.

**The insight that makes it a product rather than 64 consulting engagements.** A
campus can write policy prose from a template in an afternoon. 🔴 **What no campus
can produce from a template is an accurate statement of what it actually runs** —
and a published AI policy that cannot name the systems it governs fails on first
audit. 🟢 **So the deliverable is one policy template plus one inventory instrument,
and the inventory is the part that is worth money and the part that is reusable.**

### What to build

| Layer | Use | Grant |
|---|---|---|
| Deployment registry | **`P14`'s registry, unchanged** — the schema already satisfies four regimes at once; here it also becomes the evidence annex to the published policy | Per `P14` |
| LMS discovery (Canvas) | [`canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) — read the courses, external tools and LTI placements actually installed, rather than asking the registrar | MIT |
| LMS discovery (Moodle) | [`Moodle-MCP`](https://github.com/Faixiang/Moodle-MCP) — **read-only by construction**, which is the right property for a discovery pass across campuses that have not yet agreed a policy | MIT |
| Mount point for the literacy module | [`ltijs`](https://github.com/Cvmcosta/ltijs) (Node) or [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (Python) — LTI 1.3, so the module mounts into Canvas, Moodle, Blackboard and D2L without per-LMS work | Apache-2.0 / MIT |
| Literacy content | Re-levelled from [`patchy631/ai-engineering-hub`](https://github.com/patchy631/ai-engineering-hub) — take the **`22`/`48`/`23` difficulty grading as the prerequisite sequence**, discard the developer framing (`T19`) | MIT |
| Assessment items | [`LongsightGroup/qti3`](https://github.com/LongsightGroup/qti3) to author and score; pair with `qti3-item-player` for certified delivery — 🔴 **still a pairing exercise, per `repos/foundations.md`** | Per that file |
| Completion reporting | [`learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) against SQL LRS, Ralph or Veracity — so "the campus delivered AI literacy" becomes an institutional record, not an assertion | MIT |

### Sequence

1. **Week 1 — one campus, end to end.** Run the registry (`P14`) plus `canvas-mcp` /
   `Moodle-MCP` discovery against a single willing campus. Output: a populated
   inventory and a policy draft whose every claim cites a registry row.
2. **Weeks 2–3 — make it a kit.** Freeze the registry schema, the policy template
   and the discovery scripts. 🟢 **Hand it to the Fellows, not to the campuses** —
   31 people are the distribution channel, and training them is a smaller, better
   engagement than selling 64 times.
3. **Weeks 4–6 — the literacy module.** Re-level the corpus, emit items as QTI,
   mount over LTI 1.3, wire xAPI. 🔵 **This half is not deadline-bound and should be
   priced separately** — the policy must ship by December 31; the curriculum serves
   Fall-entry cohorts and can land after.
4. **Ongoing — the registry is the renewable.** It is what `T16` says every regime
   will ask for next, and it is already built.

### Scope and risk

- **Effort:** 2–3 weeks to the first campus artifact and the kit; 4–6 further weeks
  for the literacy module. 🔴 **Do not propose a 64-campus rollout inside the
  deadline** — propose the kit plus the Fellows' enablement, which is deliverable.
- 🔴 **Pitch AI *inside* the existing Information Literacy competency, not a
  standalone AI course.** The standalone reading is the contested one (`T18`) and
  the expensive one.
- 🔴 **Do not let the discovery pass acquire write access.** `Moodle-MCP` is
  read-only by design; keep `canvas-mcp` to read scopes. A governance engagement that
  writes to a gradebook before the policy exists is the one failure that ends it.
- 🟢 **Everything in the table is MIT or Apache-2.0** — the kit is deliverable to the
  client as a derived product with no copyleft propagation.
