---
industry: education
region: Global
updated: 2026-11-13
---

# Compose patterns — education

**Thirty** concrete recipes — derived recipes: **30**. 🟢 **Seventeenth pass (`p812`): `P29`–`P30` added** — the Frappe-based education ERP agent, and the LATAM university self-management agent. Each names the actual
repos, the license consequence, how the pieces wire together, and a rough build estimate.
All components were license-verified on 2026-11-13 (see `agents/top.md` and
`repos/foundations.md`). 🟢 **Sixteenth pass (`p811`): `P27`–`P28` added** — the OneRoster
agent nobody has built, and the European national-school-portal family agent. 🔵 **The count
on this line is now MACHINE-GRADED: `ingest/derive-counts.py` reads the marked claim
`derived recipes: **N**` and compares it with `^## P` headings on this page, so the drift
this paragraph has had to confess four times is now caught by `make hooks` instead.**
🟢 **Fifteenth pass (`p810`): `P24`–`P26` added** — a FRIA-survivable
district early-warning agent, a Markdown→SCORM pipeline with a conformance gate, and
assessment work shaped to Ofqual's open categories. 🔴 **This line said "Twenty-two" while the
file held `23`.** 🟢 **Re-derived: `grep -c '^## P' compose/patterns.md` = `26`.** 🔴 **Count defect, third occurrence, fixed again at
`p805`: `p804` corrected "Ten" to "Thirteen" while the file already carried
sixteen `## P` headings. It is now "Eighteen" and it matches
`grep -c '^## P'`.** 🔵 **A count written in prose drifts every time a pattern is
appended; until it is generated, this line will keep going stale.**

🟢 **New at `p808` (thirteenth pass): `P22` — Canvas-native grading assistant with
human-in-the-loop publication.** 🔵 **It is the first pattern in this file written
*because* no adoptable implementation exists** — `T24` established that the education
agent workflow layer is a population of `0★` single-author projects, so `P22` adopts the
connector and builds the loop. Like `P21` it has **no copyleft anywhere in the tree**.

🟢 **New at `p807` (twelfth pass): `P21` — admissions and enrolment agent on a
permissive CRM.** 🔵 **It is the first pattern in this file with NO copyleft anywhere in
the tree**, which is why it exists: a studio can fork, brand and ship it. The count
`Twenty-one` was checked with `grep -c '^## P'` before being written. 🔴 **All six
infrastructure slugs it cites were re-resolved this pass** against
`raw.githubusercontent.com` (`200` on `README.md@main` for each) because
`curl` to `github.com` returns a uniform `403` through this session's proxy and
therefore verifies nothing.

🟢 **New at `p806`: `P19` (agent on the state data standard) and `P20`
(AI-literacy programme from an open corpus).** 🔵 **The count above was checked with
`grep -c '^## P'` before being written, not carried forward from the previous edition
— which is how the three earlier defects happened.**

🟢 **New at `p805`: `P17` (defensible tutor audit trail) and `P18`
(skills-and-credentials advising).** Neither uses a component discovered this
pass — both are built from repos this base had verified and never shelved, now
promoted into `repos/foundations.md`.

**The rule sixteen of the eighteen follow:** keep the AI layer permissive
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

## P17 — The defensible tutor audit trail (Global, and the only pattern here that survives an EU AI Act Article 50 question)

**When to use.** Any engagement where an AI tutor or grader touches learners and
**someone will eventually ask what it did**. That is now most of them: EU
Article 50 transparency duties apply from **2026-08-02** and were *not*
postponed by the Digital Omnibus; FERPA binds any US tool handling personally
identifiable student data; South Korea's AI Basic Act names education a
high-impact sector. 🔵 **Every other pattern in this file tells the agent to
"emit xAPI". This one is the pattern that receives, validates, stores and
consolidates it — and until `p805` this base named no component that could
reject a malformed emission.**

### The components — all permissive, all re-verified live at `p805`

| Piece | Where | License |
|---|---|---|
| Statement validation, in the agent process | `github.com/LearningLocker/xapi-validation` | **MIT** (12★) |
| Statement service / LRS endpoint | `github.com/LearningLocker/xapi-service` | **MIT** (42★) |
| Or the database-shaped LRS | `github.com/yetanalytics/lrsql` | **Apache-2.0** (144★) |
| Record warehouse, multi-source | `github.com/Apereo-Learning-Analytics-Initiative/OpenLRW` | **ECL-2.0** (62★) |
| Agent↔record bridge | `github.com/DavidLMS/learnmcp-xapi` | **MIT** |
| The LMS it hangs off | Moodle (GPL-3.0) over LTI 1.3, or OpenOLAT (Apache-2.0) natively | — |

### How it wires together

1. **Validate before you emit.** The agent builds an xAPI statement and runs it
   through `xapi-validation` **in its own process**. A malformed statement is
   rejected at the source, where there is still a stack trace, rather than
   silently accepted by a lenient store.
2. **Emit to `xapi-service`** (Node stacks) **or `lrsql`** (when the client
   wants a database product with a verified Postgres/MariaDB/MySQL matrix).
   Both are permissive, so the store ships inside the deliverable.
3. **`learnmcp-xapi` gives the agent read access back** — the tutor reads the
   learner's own record before deciding what to do next, which is what makes
   the trail *useful* rather than merely compliant.
4. **Consolidate into `OpenLRW`** when more than one system emits — LMS, tutor,
   assessment tool. ECL-2.0 is Apache-derived and OSI-approved, so it composes
   with everything above it.
5. **Point the Article 50 answer at the warehouse**, not at the model: what the
   regulator wants is *which learner, which interaction, disclosed as AI, when*
   — which is a query, once the trail exists.

**Licence consequence.** MIT + MIT + Apache-2.0 + ECL-2.0 — **no copyleft
anywhere in the trail.** The GPL stays in the LMS, on the far side of LTI.

**Estimate.** **4–6 weeks** to a working trail against one LMS and one tutor;
**+3–4 weeks** for the OpenLRW consolidation and a regulator-facing query layer.

🔴 **Caveats.** `xapi-service` and `xapi-validation` show no release dates on
their pages — **pin commits and budget to carry them**. `OpenLRW` is Apereo
middleware: Java, institutional, and not a quick install. And an audit trail is
a *record*, not a defence — if the tutor's behaviour is wrong, the trail proves
it precisely.

## P18 — Skills-and-credentials advising (North America, and the only pattern here whose buyer is a workforce agency)

**When to use.** State systems, community colleges, workforce boards and
corporate academies — buyers who are not asking "did the learner engage" but
**"what is this person able to do, and what does that credential actually
certify"**. 🔵 **This is the one engagement shape in this KB whose data model
is a public vocabulary rather than a vendor schema**, which is why it is cheap
to be interoperable and expensive to be proprietary.

### The components — all permissive, promoted to the shelf at `p805`

| Piece | Where | License |
|---|---|---|
| Skill authoring against CTDL/RSD | `github.com/CredentialEngine/osmt` | **Apache-2.0** (67★) |
| The registry skills publish into | `github.com/CredentialEngine/CredentialRegistry` | **Apache-2.0** (15★) |
| Transcript line → CTID matching | `github.com/CredentialEngine/transcript-ctid-matcher` | **Apache-2.0** |
| Lived-experience skills elicitation | `github.com/tabiya-tech/compass` | **MIT** (14★) |
| Taxonomy side | `tabiya-tech/taxonomy-model-application`, `tabiya-livelihoods-classifier` | **MIT** |
| Learner record in / out | `lrsql` or `xapi-service` (see `P17`) | Apache-2.0 / MIT |

### How it wires together

1. **`transcript-ctid-matcher` maps the registrar's course rows to CTIDs.**
   This is the unglamorous core of the engagement and the reason a studio gets
   paid — a permissive reference implementation removes the worst of it.
2. **`osmt` authors Rich Skill Descriptors** for what the institution teaches;
   **`CredentialRegistry` publishes them** so employers and other institutions
   can resolve them.
3. **`compass` runs the learner-facing half**, eliciting skills from lived
   experience rather than coursework — the only agent in this base that does.
   Its output is a skills profile, not a transcript.
4. **Join the two.** The advising agent answers *"given what you have done, here
   is the credential nearest to the job you want, and here is the gap"* — with
   both sides expressed in the same public vocabulary.
5. **Emit the advising session over xAPI** into `P17`'s trail.

**Licence consequence.** Apache-2.0 + MIT throughout — **fully derivable**.

**Estimate.** **8–10 weeks** for transcript→CTID matching plus a published skill
set against one institution; **+4 weeks** to add the `compass` elicitation front
end.

🔴 **Caveats, and they are real.** **CTDL/RSD is a US ecosystem** — this pattern
does **not** transfer to EMEA, APAC or LATAM without replacing the vocabulary,
and there is no equivalent permissive stack in this base for those regions
(**declared gap, `p805`**). `osmt`'s grant had to be read from the file because
the index says `NOASSERTION`. All four repos are under 70 stars: adopt the
vocabulary and the licence with confidence, read the code before promising the
pipeline.


## P19 — Agent on the state data standard (North America, the highest-ceiling pattern in this file)

🔵 **Why this pattern exists and why it is new at `p806`:** every other student-record
pattern here — `P8`, `P9`, `P12` — reaches the record through **one institution's**
system. This one reaches it through **Ed-Fi**, the interoperability model US **state
education agencies** run K-12 reporting on. 🟢 **Same engineering, one altitude up, and
the buyer changes from a district to a state.**

### The components — all Apache-2.0 or MIT, all verified at `p806`

| Component | Repo | Licence | Role |
|---|---|---|---|
| Data platform | [`Ed-Fi-Alliance-OSS/Data-Management-Service`](https://github.com/Ed-Fi-Alliance-OSS/Data-Management-Service) | **Apache-2.0** | **Ed-Fi API v8.** Data Management Service (Resources, Descriptors, Discovery) + Configuration Service (Management API). 🔴 **Build here, not against the v7 ODS** — the ODS README says v8.0+ lives in this repo |
| Legacy target | [`Ed-Fi-Alliance-OSS/Ed-Fi-ODS`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) | **Apache-2.0** | v7.x ODS/API — what the client is probably **actually running today**. Plan for it; do not design new work onto it |
| Write-gate design | [`PsychQuant/che-ntucool-mcp`](https://github.com/PsychQuant/che-ntucool-mcp) | **MIT** | 🟢 **Copy the protocol, not the code** (it is Swift / macOS): elicitation dialog **plus a single-use token bound to the previewed payload** |
| Write-gate alternative | [`12dora/waseda-moodle-mcp`](https://github.com/12dora/waseda-moodle-mcp) | **MIT** | `prepare_*` → `confirm_action` / `cancel_action`. Simpler; the right choice where there is no grade-write path |
| Telemetry | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | **MIT** | Emit xAPI for anything the agent does, so the activity is reportable |
| Governance | `P14` deployment registry | — | 🟢 **Mandatory here, not optional** — see below |

### How it wires together

1. **Stand up the Ed-Fi API** (v8 DMS) against a copy of the client's data, or point at
   their existing v7 ODS/API. Both speak a published REST specification.
2. **Write an MCP server over it.** 🔴 **This does not exist and is the build** — see
   `Gap 806-A`. Scope it by Ed-Fi **resource**: enrollment, attendance, assessment
   results, discipline. Start **read-only**.
3. **Gate every write before you ship one.** Adopt `che-ntucool-mcp`'s two-layer design:
   a `preview_*` call returns the exact payload and a single-use token; the `post_*` call
   refuses anything whose token does not match the previewed payload byte-for-byte.
4. **Emit xAPI** through `learnmcp-xapi` for every agent action.
5. **Register the deployment** (`P14`) before go-live.

### Why the write gate is not negotiable here

🔴 **A state longitudinal data system is the highest-consequence write surface in this
entire knowledge base.** An attendance or discipline record that an agent changed
silently is a legal problem for the agency, not a bug report. 🟢 **Ship read-only first
and sell the write path as phase two** — it is also an easier procurement conversation.

### Estimate

🟢 **Read-only MCP server over Ed-Fi v8, four resource families, xAPI emission,
deployment registry: 6–8 weeks.** Add **3–4 weeks** for the gated write path. 🔵 **The
discovery cost is the variable** — which Ed-Fi version the agency runs, and which
optional Ed-Fi extensions their state profile adds, decides more of the timeline than
the agent work does. **Scope a 1-week assessment first.**

### Three disqualifiers — check these first

- 🔴 **The client is a district, not a state or a regional service agency.** Then this is
  over-engineered: use `P8` or `P12` and sell a SIS-level integration.
- 🔴 **The agency is not on Ed-Fi.** Not every state is. Confirm before proposing —
  **this is a one-question disqualifier and it is free to ask.**
- 🔴 **The engagement needs writes in phase one.** Then the timeline and the compliance
  surface both roughly double; re-scope or re-price.

## P20 — AI-literacy programme from an open corpus (Global, and the only pattern here with three dated mandates pointing at it)

🔵 **Why this pattern exists:** `T19` records three regimes imposing a dated AI-literacy
duty — SUNY's gen-ed Information Literacy competency from Fall 2026, **EU AI Act Art.
`4`**, and Australia's national rollout at **1M students over three years** — against a
supply side that was empty. 🟡 **`p806` narrowed that: the first open-licensed education
curriculum exists, and it is a seed a studio can grow rather than a product that
competes with one.**

### The components

| Component | Repo / standard | Licence | Role |
|---|---|---|---|
| Curriculum seed | [`Emerging-Rule/community`](https://github.com/Emerging-Rule/community) | 🟡 **CC BY 4.0 (README + badge; no sidebar licence field)** | Bilingual **EN / ES** K-12 lessons, K-2 → 9-12. 🟢 **Attribution-only, no share-alike — shippable inside a client deliverable** |
| Difficulty sequence | [`patchy631/ai-engineering-hub`](https://github.com/patchy631/ai-engineering-hub) | **MIT** | 🟢 **Take the `22`/`48`/`23` three-tier grading as the prerequisite spine**, then cut the developer assumptions. Content for the upper secondary / tertiary end |
| Framework alignment | [`opensalt/opensalt`](https://github.com/opensalt/opensalt) | **MIT** | 🟢 **The piece that makes this saleable to a ministry.** Publishes the AI-literacy competency framework as machine-readable **1EdTech CASE® 1.1**, so every lesson is aligned to a stated competency rather than asserted to be |
| Credential | [`CredentialEngine/osmt`](https://github.com/CredentialEngine/osmt) | **Apache-2.0** | Rich Skill Descriptors against CTDL — for the North American workforce-outcome claim |
| Delivery | `pylti1.3` / `ltijs` + Moodle / Canvas / Open edX | MIT / copyleft host | Mount the sequence as an LTI tool so it runs inside whatever LMS the client already has |
| Assessment | [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | **MIT** | QTI 3 items, so the item bank is portable off the project |
| Reporting | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | **MIT** | Completion and mastery as xAPI — 🟢 **this is what turns "we ran training" into evidence of discharging the duty** |

### How it wires together

1. **Model the duty as a competency framework in `opensalt`** — Art. `4`, the SUNY
   competency or the Australian curriculum, whichever binds the client. 🔵 **Do this
   first:** it is what the auditor reads and it decides everything downstream.
2. **Map the seed lessons onto it.** `Emerging-Rule/community` for K-12,
   `ai-engineering-hub`'s tiers for upper secondary and tertiary.
3. 🔴 **Write the lessons that do not exist.** At six to thirteen lessons the seed covers
   a fraction of any mandate. **This is the actual work and the actual line item.**
4. **Author assessment as QTI 3 items**, delivered through the item player.
5. **Mount via LTI 1.3**; emit **xAPI** on completion and mastery.
6. **Contribute the new lessons back upstream.** 🟢 **Not altruism:** CC BY 4.0 lets the
   studio keep and ship them, and a studio that authors the reference corpus in a field
   with three mandates and no incumbent owns the category.

### Why the licence chain holds

🟢 **CC BY 4.0 (content) + MIT (sequence, player, telemetry) + Apache-2.0 (skills) is
attribution-only end to end.** Nothing here is share-alike, so the client's derived
curriculum stays theirs. 🔴 **The one weak link is provenance, not terms:**
`Emerging-Rule/community` shows **no licence field on its GitHub sidebar** — CC BY 4.0
is from the README and a badge. 🔵 **Confirm the grant in writing with the maintainer
before building a priced deliverable on it.** `20` commits and `3` stars means there is
a person who will answer an email.

### Estimate

🟢 **Framework modelling in `opensalt`, mapping the existing seed, LTI mount, QTI
assessment and xAPI reporting: 5–7 weeks.** 🔴 **Curriculum authoring is separate and
dominates the budget** — price per unit, not per project, and scope it against the
specific mandate.

### Three disqualifiers — check these first

- 🔴 **The client needs Portuguese.** The seed is English and Spanish only. **For Brazil,
  the largest education market in LATAM, the corpus does not exist** — that is an
  authoring project from zero, and it must be priced as one.
- 🔴 **The client wants accredited or certified courseware.** None of these components
  carries accreditation; it is a separate, slow, jurisdiction-specific process.
- 🔴 **The mandate is already met by a national programme.** Australia's rollout has
  materials and a funder (Code for Schools, AWS support). 🔵 **Check what the ministry
  already bought before proposing to build it.**


## P21 — Admissions and enrolment agent on a permissive CRM (Global, and the only pattern here that touches no copyleft at all)

🟢 **New at the twelfth pass (`p807`, 2026-11-13).** Every other pattern in this file
either integrates with a copyleft platform or accepts one in the tree. 🔵 **This is the
first end-to-end recipe a studio can fork, rebrand and ship as a product**, and it exists
because `p807` finally read the vertical leg's eight-pass nil instead of logging it: the
education-specific ERP/CRMs are all copyleft, so the permissive base has to be a
general-purpose CRM with the education domain built on top.

**The problem it solves.** Admissions and enrolment is **CRM-shaped work** — enquiry →
application → offer → acceptance → enrolment, with campaigns, attribution, document
chase and nurture. 🔴 **This base had been implicitly routing it to the SIS shelf, which
is entirely copyleft and structurally wrong anyway**: an SIS records students who are
already students. The pipeline before that is a sales funnel with a prospectus.

### Components — all permissive, all verified `2026-11-13`

| Layer | Component | Licence | Why this one |
|---|---|---|---|
| CRM base | [`krayin/laravel-crm`](https://github.com/krayin/laravel-crm) | **MIT** (`24.1k★`, `1.7k` forks) | The largest permissively licensed CRM found. Lead → opportunity → stage maps onto enquiry → application → offer with no structural violence |
| Alternative base | [`cortezaproject/corteza`](https://github.com/cortezaproject/corteza) | **Apache-2.0** (`2.2k★`) | Swap in **only** where the admissions process is unusual (multi-intake, competitive, ministry-reported) — it is a modeller, not a CRM to bend |
| Agent runtime | [`pydantic-ai`](https://github.com/pydantic/pydantic-ai) or [`LangGraph`](https://github.com/langchain-ai/langgraph) | **MIT** | Typed tool-calling; `LangGraph` where the offer path needs an explicit approval node |
| Model serving | [`vllm`](https://github.com/vllm-project/vllm) or [`ollama`](https://github.com/ollama/ollama) | **Apache-2.0** / **MIT** | Self-host where applicant PII cannot leave the institution — the usual EMEA and public-sector constraint |
| Gateway | [`litellm`](https://github.com/BerriAI/litellm) | **MIT** | One endpoint, per-programme cost attribution |
| Durable workflow | [`temporal`](https://github.com/temporalio/temporal) | **MIT** | Admissions runs for **months**; document chase and deferrals are long-lived timers, not request/response |
| Handoff to SIS | `OpenEduCat` via `erpipe-org/mcp-odoo`, or `Ed-Fi` (`P19`) | *integration only* | 🔴 **Copyleft stays on the far side of an API boundary — nothing is derived** |

### How it wires together

1. **Model the education domain in Krayin first, before any AI.** Add `Programme`,
   `Intake`, `Application`, `Qualification` and `Document` as custom entities; map
   Krayin's native `Lead` → `Applicant` and its pipeline stages → the admissions funnel.
   🔵 **This is configuration plus migrations, and it is the bulk of the schedule.**
2. **Wrap an admissions subset of Krayin's REST API as an MCP server.** 🔴 **No MCP
   server exists for Krayin, Corteza or OFBiz — this is net-new**, but all three are
   conventional API-first web apps, so it is days, not a connector project. 🟢 **Expose
   reads broadly and writes narrowly:** `search_applicants`, `get_application`,
   `list_outstanding_documents` read-side; `request_document`, `advance_stage`,
   `log_interaction` write-side.
3. **Apply `T20`'s preview-then-confirm discipline to every write.** Three independent
   LMS agent projects in three jurisdictions converged on it. 🔴 **An agent that advances
   an applicant's stage or issues an offer without an explicit human confirm is the
   failure mode that ends the engagement** — offers are contractual.
4. **Put Temporal behind anything with a clock.** Document chase, conditional-offer
   deadlines, deferral windows, clearing. 🔵 **The agent decides; Temporal remembers** —
   an LLM loop cannot be trusted to still be running in six weeks.
5. **Hand off at enrolment, do not absorb.** When an applicant converts, write to the SIS
   over its API — `OpenEduCat` through the Odoo MCP connectors, or a state system through
   `P19`'s Ed-Fi path in North America. 🟢 **The copyleft SIS is never in your tree.**

### Build estimate

🟢 **`8`–`10` weeks** for a single-intake institution: ~`3` weeks domain modelling in
Krayin, ~`2` weeks MCP server, ~`2` weeks agent plus preview-then-confirm, ~`1` week
Temporal workflows, ~`2` weeks SIS handoff and UAT. 🔴 **Add `3`–`4` weeks for Corteza
instead of Krayin** — more modelling, less out of the box.

### Why the licence position is the selling point

🟢 **Every component above is MIT or Apache-2.0.** 🔵 **A studio can fork this, brand it,
host it multi-tenant and sell it as a product** — which is true of no other pattern in
this file. 🔴 **The moment the SIS enters the tree rather than sitting behind an API,
that stops being true**, and the usual way it happens is a developer deciding it is
simpler to patch OpenEduCat than to call it.

### Three disqualifiers — check these first

- 🔴 **The institution already runs a commercial admissions CRM** (Slate dominates US
  higher ed; Salesforce Education Cloud is common). 🔵 **Then this is a displacement sale
  against an entrenched incumbent, which is a different and much harder motion** — pitch
  an agent layer on *their* CRM instead.
- 🔴 **Admissions is statutorily centralised.** UCAS in the UK, and national
  clearing-house systems elsewhere, mean the institution does not own the top of the
  funnel. 🟡 **The pattern still works below the centralised step — check where the
  boundary falls before scoping.**
- 🔴 **The client expects an education-ready product out of the box.** 🔵 **Krayin knows
  nothing about education**; there is no applicant, programme or intake entity until you
  build one. **If the client is comparing against OpenEduCat's admissions module on
  features, they will not like the first demo** — sell the licence position and the
  product ceiling, or do not sell this.

## P22 — Canvas-native grading assistant with human-in-the-loop publication

🟢 **Why this pattern exists.** `T24` established that education's agent supply is
atomised: this base found **seven** Canvas/Moodle grading agents in one window with a
**median of `0★`**, three of them unlicensed or AGPL. 🔴 **There is no mature grading
agent to fork.** 🟢 **But the connector layer is mature and permissive**, so the right
move is to adopt the connector and write the loop. This is the most-requested education
engagement shape and the one where a studio most often wastes a sprint looking for a base
to fork.

### Components — all MIT, no copyleft anywhere in the tree

| Role | Component | Licence | Stars | Why this one |
|---|---|---|---|---|
| LMS connector | [`canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | MIT | 324 | The only Canvas agent surface in this base with real traction. Includes a bulk-grading skill. 🔴 Tool count is inconsistent on its own page (README `128`, sidebar `102`) — pin the profile you enable. |
| Moodle variant | [`Moodle-MCP`](https://github.com/Faixiang/Moodle-MCP) | MIT | 206 | Swap in for Moodle estates. 🟢 **Read-only (10 tools)** — so for Moodle the write path must be built separately, which is a scoping fact, not a defect. |
| Orchestration | [`LangGraph`](https://github.com/langchain-ai/langgraph) | MIT | 44.9k | Explicit state machine. The approval gate must be a *graph node*, not a prompt instruction. |
| Content / rubric generation | [`educhain`](https://github.com/satvik314/educhain) | MIT | 388 | Generates questions, rubrics and feedback scaffolds as a library node. |
| Learner-path checkpoints | [`interactive-learning`](https://github.com/geekjourneyx/interactive-learning) | MIT | 52 | 🔵 **Optional, and read it as a design not a dependency (`52★`, `4` commits).** Supplies the verifiable-checkpoint card for returning remediation to a student who failed a rubric line. |
| Learning-activity record | [`learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | MIT | (held) | Writes what was practised and mastered to an LRS, so grading produces evidence rather than only a number. |

🔴 **Explicitly NOT in this tree, and each exclusion is deliberate:**
`canvas-pilot` (`AGPL-3.0` — network clause kills a hosted deliverable),
`AI-Grading-Tool` (**no grant at all**), `tutor-gpt` (`GPL-3.0`),
`PageLM` (source-available, not OSI).

### Wiring

```
      instructor rubric (Markdown, version-controlled)
                        │
                        ▼
   canvas-mcp ──► fetch submissions + roster  ──► LangGraph state
                        │
                        ▼
              grade node (LLM + educhain rubric scaffold)
                        │
                        ▼
        ┌───── PROPOSED grades + per-line feedback ─────┐
        │        (written to a staging store,            │
        │         NEVER to the Canvas gradebook)         │
        └────────────────────┬───────────────────────────┘
                             ▼
                  instructor review UI  ◄── the gate
                             │  approve / amend / reject
                             ▼
   canvas-mcp ──► publish approved set only ──► Canvas gradebook
                             │
                             ▼
              learnmcp-xapi ──► xAPI statements to the LRS
```

🟢 **The architectural rule, and it is the whole pattern:** the agent writes to a
**staging store**, never to the gradebook. Publication is a separate, explicitly
authorised action over an approved set. 🔵 **This is not a preference — it is the
convergent design of every credible implementation found.** `mini-homework-agent`
(review-then-publish), `canvas-pilot` (`scan -> approval -> execute`),
`waseda-moodle-mcp` (`prepare_* -> confirm_action`) and `mcp-odoo`
(`preview_write -> validate_write -> execute_approved_write`) all independently arrived
at it. 🔴 **Four unrelated projects converging on the same gate is the strongest design
evidence in this base.**

### Why the gate is also the compliance artefact

🟢 **The review step is what makes this sellable under every regime in `T25`
simultaneously.** EU AI Act Annex III treats evaluation of learners as high-risk and
requires **human oversight** (duties from `2027-12-02`); Korea's AI Basic Act requires
human oversight and a pre-deployment impact assessment for in-scope K-9 assessment; US
state and district policies increasingly bar AI from being the **sole basis** for a
high-stakes decision, and D.C.'s `2026-27` guidance bars AI from grading outright.
🔵 **A human-approval gate that is logged satisfies the common core of all of them**, and
the staging store is where the audit trail lives. 🟢 **Build the log as a first-class
output, not a debug artefact:** proposed grade, model version, rubric version, reviewer
identity, decision, timestamp.

🔴 **Scope check before selling this anywhere:** if the learners are K-9 in Korea it is
high-impact and needs the impact assessment; if the institution is a US district, check
whether local policy bars AI grading entirely — in which case this pattern is sold as
**feedback drafting**, with no grade path at all, which is still most of the value.

### Build estimate

🟢 **`5`–`7` weeks** for a single-course pilot on Canvas with a real instructor:
`1` week connector + rubric schema, `2` weeks grading loop and staging store,
`1`–`2` weeks review UI, `1` week xAPI/logging, `1` week hardening.
🔴 **Add `2`–`3` weeks for Moodle**, because `Moodle-MCP` is read-only and the write path
is yours to build. 🔵 **Add `2` weeks if the client needs the conformity pack**
(impact assessment, oversight design, model/data documentation) — and per `T25`, build it
once and reuse it across jurisdictions.

🔴 **The risk that actually kills these pilots is not technical.** It is that instructors
do not trust the proposed grades and review every line by hand, at which point the agent
has saved nothing. 🟢 **Mitigate by measuring agreement rate from week one** — proposed
vs. published grade, per rubric line — and by shipping the highest-agreement rubric lines
first. 🔵 **That metric is also the client's ROI story**, and per the LATAM finding that
there are roughly ten times more institutions using AI than measuring it, it is the thing
almost nobody builds.


## P23 — Brightspace/Blackboard study agent with an auditable write gate (Global; the first pattern here that serves D2L and Blackboard institutions)

🟢 **Why this pattern exists.** Until `p809` this KB could not serve a Brightspace or
Blackboard client at all — both are incumbents, neither had a connector on any shelf.
Five verified agents now exist, and they split cleanly into a **read tier** and a
**single gated write tier**, which is exactly the shape a safe engagement wants.

**Who it is for:** a university on D2L Brightspace or Blackboard Learn that wants a
student-facing study assistant (deadlines, course material, grade context) and, later, a
*narrow* ability to act — without handing an agent the power to submit coursework by
accident.

### The stack, by named repository

| Role | Repo | Licence | ★ | Why this one |
|---|---|---|---|---|
| **Brightspace read plane** | [`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server) | MIT | 67 | `29` tools, **read-only by declaration**; SSO + 2FA, password in OS keychain, session state AES-256-GCM. The most-starred and best-secured of the five. |
| **Brightspace write plane** *(optional, phase 2)* | [`JhostinAleck/brightspace-mcp`](https://github.com/JhostinAleck/brightspace-mcp) | MIT | 16 | The only agent in this base that can write to Brightspace, behind **two opt-ins + `dry_run` + idempotency key + audit log**. |
| **Blackboard read plane** | [`Mattlo0546/blackboard-mcp`](https://github.com/Mattlo0546/blackboard-mcp) (vendor-neutral Ultra) or [`alejooroncoy/campus-cli`](https://github.com/alejooroncoy/campus-cli) (ISC, far more mature) | MIT / ISC | 1 / 13 | Pick by tenant: `campus-cli` has `851` commits but is UPC/UPN-shaped; `blackboard-mcp` is generic but `4` commits. |
| **Learner-record write path** | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | MIT | 16 | Writes what the learner **did** to any xAPI 1.0.3 LRS. 🟢 **This is where progress belongs — not in the LMS.** |
| **Orchestration + policy nodes** | [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | MIT | — | Explicit graph: the write gate is a node you can show an auditor. |
| **Content packaging** *(if the agent generates material)* | [`dmmat/Scormly`](https://github.com/dmmat/Scormly) | MIT | 5 | Browser-only, no backend; exports SCORM 1.2/2004 so output mounts in either LMS. 🔴 cmi5 leg unverified upstream. |

### How to wire it

1. **Phase 1 is read-only, and ships on its own.** Stand up the Brightspace or Blackboard
   read plane. Every tool is a retrieval; there is nothing to gate. 🟢 **Most of the
   perceived value — "what is due, what did I miss, what does this rubric mean" — is
   entirely in this phase**, which is why it is worth shipping before any write exists.
2. **Put progress in the LRS, not the LMS.** Route every "learner practised / mastered /
   attempted" signal through `learnmcp-xapi` into the institution's LRS. 🔵 The LMS stays
   the system of record for *grades*; the LRS becomes the system of record for
   *learning*, and only the second one is safe for an agent to write.
3. **Phase 2 adds writes only if the client asks, and only through the gate.** Swap in
   `JhostinAleck/brightspace-mcp` with `writes.enabled: false` **and** no
   `--enable-writes` flag. Turn on `dry_run` first and run a full week in preview,
   diffing proposed writes against what staff would have approved.
4. 🔴 **Decide `submit_assignment` explicitly, in writing, with the registrar — not in
   config review.** It is the one tool in this stack that can commit academic work on a
   student's behalf. The default in this pattern is **off, permanently**, and the other
   two write tools (`post_discussion_reply`, `mark_announcement_read`) are the ones
   actually enabled.
5. **Keep the audit trail from day one.** `JhostinAleck` emits a warning-level log entry
   and requires an idempotency key per write. Ship those into the client's SIEM in phase
   2, and feed the same artefacts into `P17`'s EU AI Act Article 50 evidence pack.

### Effort and the honest caveats

🟢 **Phase 1: 3–4 weeks.** Phase 2 (gated writes + audit plumbing): **a further 4–6
weeks**, most of it governance rather than code.

🔴 **Four things to price, not discover:**
- **No vendor publishes an MCP server.** Every path here is unofficial — REST API, SSO
  session, or a scraped cookie. Confirm with the institution's IT that API access is
  sanctioned **before** quoting, or the integration is a policy violation wearing an
  architecture diagram.
- 🔴 **`campus-cli` brokers its tools through a remote relay (`mcp.campuscli.com`).** For
  an institution, **fork it and terminate the relay in-tenant** — the `ISC` grant allows
  exactly that. Do not deploy it as-is.
- 🔴 **`kingdonkatsu/ntulearn-mcp` is deliberately NOT in this stack** despite being
  verified `MIT`: it authenticates by auto-reading the `BbRouter` cookie out of the
  user's browser. Excellent reference, unacceptable dependency.
- 🔴 **`Mattlo0546/blackboard-mcp` has `4` commits.** If the client is on Blackboard
  Ultra and wants a supported path, budget to maintain a fork rather than to adopt.

## P24 — District early-warning agent that survives a FRIA (North America first, EMEA-portable)

**The ask this serves.** *"Which of my students are at risk, and why?"* — asked by a teacher,
answered from the SIS, in a form a data-protection officer will sign off.

**Why it is now buildable.** The reference implementation exists and comes from the standards
body: [`Ed-Fi-Exchange-OSS/Prototype-Semantic-Layer-with-MCP`](https://github.com/Ed-Fi-Exchange-OSS/Prototype-Semantic-Layer-with-MCP)
(`Apache-2.0`). 🔴 **Its own README says "demonstration purposes only; not intended to be a
robust production solution" — so this pattern ships the ARCHITECTURE and re-implements the
code.**

**Wiring.**

| Layer | Component | License | Role |
|---|---|---|---|
| Source of record | [`Ed-Fi-Alliance-OSS/Ed-Fi-ODS`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) | `Apache-2.0` | The district's existing Ed-Fi ODS/API |
| Semantic layer | `datamart/` from the prototype | `Apache-2.0` | PostgreSQL data mart; descriptor mapping; time-travel views. **Agents query the mart, never the ODS** |
| Access control | `datamart/sql/mcp-reader.sql` | `Apache-2.0` | `CREATE ROLE mcp_reader LOGIN`; `ALTER ROLE mcp_reader SET default_transaction_read_only = on`; `REVOKE ALL ON SCHEMA public`; `GRANT SELECT ON ALL TABLES IN SCHEMA analytics` |
| Identity | **Keycloak** (OAuth) | Apache-2.0 | Educator signs in; server takes the user from the token's **verified email** |
| Agent surface | `mcp-server/` — `get_my_scope`, `list_my_sections`, `find_students`, `list_students_at_risk`, `get_student_summary`, `get_attendance_trend` | `Apache-2.0` | Streamable HTTP on `:3000/mcp`; every tool read-only, returning compact JSON **naming the tables used** |
| Evidence trail | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | `MIT` | Records what the agent surfaced and what the human then did — the FRIA artifact |

**The three controls, and why each is where it is.**
1. 🟢 **Read-only at the DATABASE ROLE**, not in the prompt. A prompt restriction is defeated
   by the next jailbreak; `default_transaction_read_only` is defeated by nothing the model emits.
2. 🟢 **`get_my_scope` makes authorisation ANSWERABLE.** The agent can state what this educator
   may see before it answers — which is what turns "it only shows your students" from a claim
   into a demonstrable property.
3. 🟢 **Table-level provenance in every response** gives the FRIA its data-flow section
   for free.

**Regulatory fit.** 🟢 EU **Art. `27` FRIA** for public deployers (education is Annex III
high-risk, standalone deadline `2027-12-02`); 🟢 **Oklahoma's teacher-review requirement** and
🟢 the **Philippines' DepEd AI registry** are all satisfied by the scope tool plus the xAPI
trail. 🔴 **The agent must never rank, score or flag as the sole basis of a decision** — it
surfaces, a named teacher decides (`T30`).

**Estimate.** `8`–`10` weeks against an existing Ed-Fi ODS; `14`+ if the district's SIS is not
Ed-Fi-conformant and the mart must be built from a vendor export.

🔴 **Do not attempt on PowerSchool.** The three PowerSchool MCP servers found at `p810` carry
`NONE`, `NONE` and `GPL-3.0` — there is no permissive client to build on (`agents/top.md`,
Declared gaps).

## P25 — Markdown-to-SCORM course pipeline with a conformance gate before delivery (Global; APAC-sized)

**The ask this serves.** A training programme that must land in an LMS the client already runs,
at volume, with content reviewable before it ships. 🔵 **India's CBSE mandate — `10`M+ teachers
to train through NISHTHA against a fixed curriculum and a dated academic year — is this pattern
at national scale** (`intel/market.md`, APAC).

**Wiring — all permissive, no copyleft anywhere in the chain.**

| Step | Component | License | Role |
|---|---|---|---|
| 1. Write | Markdown in the client's own repo | — | 🟢 **Content reviewable in a pull request before it is a course** |
| 2. Assemble | [`kemalyy/edumints-scorm-mcp`](https://github.com/kemalyy/edumints-scorm-mcp) | `MIT` | Agent-driven assembly of interactive SCORM-compliant courses |
| 3. Package | [`giacomomaria81/scorm-mcp-server`](https://github.com/giacomomaria81/scorm-mcp-server) | `MIT` | HTML / design bundles → **SCORM 2004 / 1.2**, offline |
| 4. **Gate** | the same repo's **zip validator** | `MIT` | 🟢 **Validates ANY SCORM zip without an LMS** — a pre-delivery gate rather than a post-upload surprise |
| 5. Assess | [`johnnyrobot/qtimaker`](https://github.com/johnnyrobot/qtimaker) | `BSD-3-Clause` | Markdown → **QTI** item bank, same review path |
| 6. Code exercises | [`taybenlor/runno`](https://github.com/taybenlor/runno) | `MIT` | 🟢 **Sandboxed WASI execution in the browser** — the untrusted-code boundary, and it moves per-learner compute off the hosting bill |
| 7. Deliver | [`Faixiang/Moodle-MCP`](https://github.com/Faixiang/Moodle-MCP) (`MIT`) · [`boyuchengz/canvas-mcp`](https://github.com/boyuchengz/canvas-mcp) (`MIT`) · [`blend-ed/openedx-mcp`](https://github.com/blend-ed/openedx-mcp) | permissive | Into the LMS the client already runs |
| 8. Record | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | `MIT` | xAPI completion records |

🟢 **Step 4 is the one that earns its place.** Every other SCORM pipeline in the wild discovers
conformance failures on upload, per-LMS. 🔵 **A validator that runs without an LMS turns a
delivery risk into a CI check.**

🔴 **Licence trap, and it is the one that actually bites at this scale.** If an item bank is
retrieved rather than authored — e.g. [`weishao2/tizhuang-agent-skills`](https://github.com/weishao2/tizhuang-agent-skills)
(`MIT`, `39★`, 20M+ K-12 items) — 🔴 **the MIT grant covers the SKILL CODE and grants nothing
in the QUESTION BANK behind it.** 🟢 **Clear the corpus separately from the tooling** — the
same split as `P800-3`.

🔴 **`boyuchengz/canvas-mcp` is read-only by construction**, so step 7 into Canvas needs a
separate authenticated write path; do not assume the agent can publish.

**Estimate.** `6`–`8` weeks for the pipeline; content volume is the cost driver, not the code.

## P26 — Assessment assistance that is regulator-shaped: QA and moderation, never the sole marker (EMEA first)

**The ask this serves.** An awarding body or university wants AI in marking and has been told
it cannot have it. 🟢 **Ofqual's rule names the open territory as precisely as the closed one**
(`T30`): **closed** — AI as sole marker in regulated qualifications, extended to non-exam
assessment; **open and explicitly endorsed** — **quality assurance, marker training,
moderation, second-marking.**

🔵 **So do not sell marking. Sell the four open categories, and build so that the closed one is
structurally unreachable.**

**Wiring.**

| Component | License | Role |
|---|---|---|
| [`erictrainnlpinxihu/Grader-agent`](https://github.com/erictrainnlpinxihu/Grader-agent) | `MIT`, `94★` | Five-phase loop `perceive→plan→act→observe→respond`. 🟢 **The model decides only intent and confidence; routing, tool set and risk level are pinned in CODE** — which is the auditable separation a regulator asks to see |
| [`johnnyrobot/qtimaker`](https://github.com/johnnyrobot/qtimaker) | `BSD-3-Clause` | QTI item bank from Markdown, reviewable before use |
| [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) | 🔴 `GPL-2.0` | Full assessment platform **only if** the client can carry GPL; otherwise keep it out of the deliverable and integrate at the process boundary |
| [`VIABLE-Learning-Lab/viable`](https://github.com/VIABLE-Learning-Lab/viable) | `MIT` | A harness that wraps any agent to keep teaching policy outside the model — same control shape, arrived at independently |
| [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | `MIT` | The audit record: what the agent proposed, which human decided, when |

**The four sellable products, in order of regulatory ease.**
1. 🟢 **Marker training** — generate calibration scripts with known marks from the item bank.
2. 🟢 **Quality assurance** — agent re-marks a sample; **disagreement with the human marker is
   the output**, not a grade. 🔵 **The deliverable is a flag for human review, which is the
   regulator's own stated use.**
3. 🟢 **Moderation** — surface cross-marker drift across a cohort.
4. 🟡 **Second-marking** — agent as one of two markers, human reconciles. 🔴 **Only where the
   human reconciliation is recorded and binding.**

🔴 **The structural guarantee matters more than the policy.** 🟢 **Build so no agent output
reaches a candidate record without a named human write** — `Grader-agent`'s code-pinned
routing plus `P22`'s human-in-the-loop publication gate already give this; the xAPI trail
proves it after the fact. 🔵 **Then "AI is not the sole marker" is a property of the system,
not a promise in the contract.**

🔴 **Do not cite the reported DfE "progressive disclosure" standard in a bid** — `p810` could
not confirm it against any government source (`T30`).

**Estimate.** `6`–`8` weeks for QA and moderation on an existing item bank; second-marking adds
a reconciliation UI and a conversation with the regulator.

---

## P27 — The OneRoster agent nobody has built (North America first, Global-portable)

🟢 **This is the best-evidenced contribution target in this base, and `p811` re-tested the
evidence rather than restating it.** `OneRoster` — the 1EdTech standard by which a student
information system hands class rosters, enrolments and gradebook data to everything else —
is named over `3,000` times across this KB. 🔴 **And there is no agent for it.**

### Why the gap is real, with the evidence

| Check | Result (`2026-11-13`) |
|---|---|
| `gh api -X GET search/repositories -f q="oneroster mcp"` | 🔴 **zero items** |
| Vendor connector documentation (ibl.ai, dated October 2026) | 🔴 States that neither **1EdTech** nor **ClassLink** publishes an MCP server; its own "OneRoster agent skill" is a `SKILL.md` that assumes **you** host the server |
| Tooling that DOES exist | 🟢 a conformance suite, an importer, two server implementations and a client library — see below |

🔵 **Two independent channels, one answer. The standard has libraries and no agent.**

### The components — every one verified on the `repo:` channel this pass

| Component | Repo | Licence | State |
|---|---|---|---|
| **OneRoster client (REST + CSV)** | [`LongsightGroup/oneroster`](https://github.com/LongsightGroup/oneroster) | 🟢 MIT | pushed `2026-07-15`, `0★`, npm `@longsightgroup/oneroster` `0.3.0` — **new to this base at `p811`** |
| **Conformance gate** | [`googleworkspace/oneroster-integration-conformance-tests`](https://github.com/googleworkspace/oneroster-integration-conformance-tests) | 🟢 Apache-2.0 | `7★`; vendor-neutral, published by a party with no LMS to sell |
| **Reference server (wire format only)** | [`bgwdotdev/go-oneroster`](https://github.com/bgwdotdev/go-oneroster) | 🟢 MIT | 🔴 stale since `2020-07-30` — read it, do not depend on it |
| **Importer (separate process)** | [`oat-sa/oneroster-import`](https://github.com/oat-sa/oneroster-import) | 🔴 GPL-2.0 | run as its own process; never link it |
| **The control topology to copy** | [`Ed-Fi-Exchange-OSS/Prototype-Semantic-Layer-with-MCP`](https://github.com/Ed-Fi-Exchange-OSS/Prototype-Semantic-Layer-with-MCP) | 🟢 Apache-2.0 | read-only enforced at the **database role**, six tools, OAuth scope check |

### How it wires together

1. **Ingest.** Point `LongsightGroup/oneroster` at the district's OneRoster endpoint *or* its
   CSV export. 🔵 **Support the CSV binding first** — US districts hand over a CSV far more
   often than they stand up a REST service, and the MIT client covers both bindings, which is
   the specific reason it is the base of this pattern.
2. **Land it read-only.** Load into Postgres under a role pinned
   `default_transaction_read_only = on` with `GRANT SELECT` on the roster schema only.
   🟢 **Copy this from the Ed-Fi prototype: the read-only property is enforced by the database
   role, not asked for in a prompt.** That is the difference between a control and a convention.
3. **Expose few tools.** Six, after Ed-Fi's example — `get_my_scope`, `list_my_sections`,
   `find_students`, `get_section_roster`, `get_enrolment_changes`, `get_sync_health` — each
   returning the tables it read. 🔴 **Do not build a 77- or 137-tool surface; this base has
   two of those already and both are governance objects rather than features.**
4. **Gate the identity.** The agent's scope is the signed-in educator's scope, resolved
   server-side at every call. Never a shared service account.
5. **Prove conformance before delivery.** Run the Google conformance suite against the
   district's endpoint and **attach its output to the acceptance criteria**. 🟢 **This is the
   commercially clever part: the suite turns "the integration works" from an opinion into a
   contractual artifact, and it is Apache-2.0 so it can ship with the deliverable.**

### Why it survives review

🔵 **It reads rosters and writes nothing**, so in the EU it is outside Annex III's assessment
category, and in the US it is a FERPA *scope* question rather than a decision-making one.
🟢 **Every component is MIT or Apache-2.0 except the GPL importer, which runs as a separate
process by design.**

### Estimate

**5–7 weeks** for the ingest + read-only store + six-tool server + conformance run, assuming
the district can produce either a OneRoster endpoint or a conformant CSV export.
🔴 **Add 2–3 weeks if the "OneRoster export" turns out to be a bespoke CSV**, which is the
most common surprise on this seam.

### Three disqualifiers — check these first

1. 🔴 **The district's SIS is PowerSchool and they want the agent to talk to it directly.**
   PowerSchool has three MCP servers in this base and none with a usable grant (`NONE`,
   `NONE`, `GPL-3.0`). Go through OneRoster, or the pattern changes into a licence negotiation.
2. 🔴 **They want write-back of grades.** That is the gradebook service, it is a decision
   surface, and it moves the engagement into `P24`'s FRIA territory. Scope it separately.
3. 🔴 **They have no OneRoster export at all.** Then the first deliverable is the export, not
   the agent, and `oat-sa/oneroster-import` (GPL-2.0, run standalone) is where to start.

---

## P28 — The national school portal family agent (EMEA first, and the only pattern here whose buyer is a ministry)

🟢 **`p811` found that European education agent supply is attached to state-operated portals
rather than to LMS platforms (`T31`).** 🔵 **This pattern is what to do with that: one agent,
one portal, a family as the user, and a public body as the buyer.**

### The seam, with the reference implementations found in one five-day window

| Portal | Operator | Country | Reference implementation | Licence |
|---|---|---|---|---|
| Schulportal Hessen (Lanis) | the federal state of Hesse | 🇩🇪 | [`udondan/lanis`](https://github.com/udondan/lanis) | 🟢 MIT |
| DSBmobile (timetables, substitutions) | the DSB service | 🇩🇪 | [`udondan/dsbmobile`](https://github.com/udondan/dsbmobile) | 🟢 MIT |
| Admentum | Swedish platform vendor | 🇸🇪 | [`andyswe/admentum-mcp`](https://github.com/andyswe/admentum-mcp) | 🟢 MIT |
| iPasen / Séneca | Junta de Andalucía | 🇪🇸 | [`boraita/ipasen_mcp`](https://github.com/boraita/ipasen_mcp) | 🟢 MIT |
| Greek School Network (`sch.gr`) | Greek Ministry of Education | 🇬🇷 | [`weirdapps/sch-mail`](https://github.com/weirdapps/sch-mail) | 🟢 MIT |
| `edu.by` constructor | Belarusian national school-web service | 🇧🇾 | [`Severnbli/edu-by-agent`](https://github.com/Severnbli/edu-by-agent) | 🔴 GPL-3.0 |
| PRONOTE + EduConnect | Index Éducation + French state IdP | 🇫🇷 | [`sairo-cyber/pronoteConnect`](https://github.com/sairo-cyber/pronoteConnect) | 🔴 GPL-3.0-or-later (`T33`) |

### How it wires together

1. **Pick the portal, not the LMS.** The system a family logs into daily is the one worth an
   agent. 🔴 **A proposal offering "an agent for your Moodle" is answering a question the Land
   did not ask.**
2. **Read the reference implementation for the SEAM, then write your own client.** Every row
   above is `0–2★`, single-maintainer and self-declared unofficial. 🟢 **What they give you is
   which verbs the portal exposes and which auth path works** — normally the most expensive
   unknown in a public-sector bid. 🔴 **For France, `T33` applies: the GPL comes from the
   `@blockshub/pawnote-lts` client, so a permissive deployment needs a clean-room PRONOTE
   client as its own funded deliverable.**
3. **Adopt the two controls the field converged on without coordination.**
   🟢 **Preview-then-confirm on every write** — stated independently by
   [`boraita/ipasen_mcp`](https://github.com/boraita/ipasen_mcp) 🇪🇸,
   [`Severnbli/edu-by-agent`](https://github.com/Severnbli/edu-by-agent) 🇧🇾 and three earlier
   jurisdictions in this base (`T20`, now five).
   🟢 **Rate-shape the context** — [`andyswe/admentum-mcp`](https://github.com/andyswe/admentum-mcp) 🇸🇪
   serves messages **one item per call**, which bounds how much of a minor's correspondence
   can enter a model context in a single tool call. 🔵 **That is a quantitative limit rather
   than a prompt instruction, and it is the single most copyable idea in this pass.**
4. **Default to read-only for anything touching a minor's record**, and keep writes to the
   family's own actions (absence notes, meeting confirmations) behind the confirm step.
5. **Ship the FRIA with it.** 🟢 **Four of these seven portals are operated by a public body,
   so the EU AI Act Art. `27` fundamental-rights impact assessment falls on the DEPLOYER
   because the deployer is public.** 🔵 **Pair this pattern with `P14`'s deployment registry
   and `P2`'s conformance layer: the integration and the compliance artifact arrive in the
   same proposal, which is what actually unblocks a ministry purchase.**

### Estimate

**8–11 weeks** per portal for a read-mostly family agent with a confirm-gated write path, the
one-item-per-call context limit, and an Art. 27 FRIA pack. 🔵 **The second portal is roughly
`60%` of the first** — the controls, the FRIA template and the confirm gate are portable; only
the client changes.

### Three disqualifiers — check these first

1. 🔴 **The portal has no documented API and its terms forbid automated access.** Every
   reference above is "unofficial"; a ministry engagement needs the operator's written
   permission, and that conversation comes before any code.
2. 🔴 **The buyer wants it to speak to pupils directly.** Then the learner's AGE changes the
   regulatory category (`T25`) and child-safety law binds before education law does.
3. 🔴 **France, without funding for a clean-room PRONOTE client.** The permissive position
   cannot be reached by relicensing (`T33`), so a fixed-price permissive deliverable is not
   available on the French seam this quarter.

## P29 — Agent on a Frappe-based education ERP (Global, configuration not build, and the first pattern here whose connector is FIRST-PARTY)

**Who it is for.** An institution running **Frappe Education** (or ERPNext alongside it) that
wants an agent over the student record — enrolment, programs, assessment results, fees — without
commissioning a bespoke integration.

**Why it exists as a separate pattern from `P12`.** `P12` reaches OpenEduCat through two
**third-party** Odoo connectors, one of which ships a "YOLO mode" that bypasses its own access
control. 🟢 **Frappe's connector is in the framework itself.** See `T35`.

### The components — all verified at `p812`, licences byte-read

| Component | Repo | Licence | Role |
|---|---|---|---|
| Framework + **built-in MCP server** | [`frappe/frappe`](https://github.com/frappe/frappe) | **MIT** | 🟢 **The agent surface. `13` DocType-generic tools, verified in source at `frappe/mcp/tools/__init__.py`** |
| Education app | [`frappe/education`](https://github.com/frappe/education) | 🔴 GPL-3.0 | The system of record — `Student`, `Program Enrollment`, `Assessment Result`, fees |
| Approval-gated client (optional) | [`nasroykh/foxmayn_frappe_cli`](https://github.com/nasroykh/foxmayn_frappe_cli) | **MIT** | CLI/MCP/desktop with *"AI assistants with approval"* |
| Audit spine | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | **MIT** | Per `P17`, records what the agent did as xAPI statements |

### How it wires together

1. **Enable the endpoint.** The built-in server raises `NotFound` until the **`enable_mcp`**
   system setting is turned on — 🟢 **so the default state is closed, and turning it on is a
   dated, auditable change.**
2. **Design the role, because the role IS the gate.** `frappe/mcp/tools/documents.py` states that
   document tools *"reuse REST API v2 permissions and controller hooks."* 🔴 **`create_document`,
   `update_document`, `delete_document` and `call_method` are generic over every DocType the
   authenticated role can reach.** 🟢 **So create a dedicated agent role with `SELECT`-equivalent
   permissions on the education DocTypes and nothing else** — this is the deliverable's core, and
   it is configuration, not code.
3. **Use the annotations in the client.** Tools ship `readOnlyHint: True` on reads and
   **`destructiveHint: True` on `update_document` and `delete_document`.** 🟢 **Bind the client's
   confirmation dialog to `destructiveHint`** rather than to a hand-maintained verb list.
4. **Let the agent discover the schema.** `search_doctypes` + `get_doctype_schema` mean no
   hard-coded field maps, so the pattern survives a Frappe Education version bump.
5. **Record every call** to the LRS per `P17`, so the institution can answer "what did it touch."

### Why it survives review

🟢 **The permission boundary is the institution's own, already audited, already staffed.** No
parallel allowlist to drift. 🟢 **The connector is MIT**, so nothing copyleft enters the
deliverable: `frappe/education` is GPL-3.0 but it is the system being *integrated with*, not
derived from.

### Estimate

**3–5 weeks.** Role design and permission testing `1–2`; client wiring to annotations `1`; xAPI
audit spine `1`; UAT against a staging site `1`.

### Three disqualifiers — check these first

1. 🔴 **A Frappe version without the built-in server.** Probe
   `frappe/mcp/__init__.py` on the deployed version before quoting; fall back to
   [`rakeshgangwar/erpnext-mcp-server`](https://github.com/rakeshgangwar/erpnext-mcp-server)
   (MIT) and re-price, because that is a third-party dependency again.
2. 🔴 **The client wants the agent to WRITE marks.** Then `T25`, `P26` and the EU AI Act
   assessment rules bind before this pattern does: the agent drafts, a human posts.
3. 🔴 **Someone quotes [`frappe/mcp`](https://github.com/frappe/mcp) (`170★`) as the connector.**
   🔴 **It is deprecated by its own README and is a tool-authoring SDK, not a generic connector.**
   Scoping on it turns a configuration job into hand-written tools per DocType.

## P30 — Agent on a LATAM university self-management system (LATAM first; Argentina and Brazil only)

**Who it is for.** An Argentine or Brazilian university, institute or edtech that wants a student-
facing assistant over the system students actually log into — **SIGAA**, **Sysacad** or
**SIU Guaraní** — none of which publishes an API.

🔴 **Read this disqualifier before anything else: this pattern is ARGENTINE AND BRAZILIAN, not
regional.** `SIMAT` (Colombia) returns `total_count=0`; the Mexican, Chilean and Q-Acadêmico legs
each returned `0`; `SIAGIE` (Peru) returns `25` repositories with **zero agents and zero
licences**. 🟢 **Quoting "LATAM coverage" from this pattern is a false claim** (`T34`).

### The components — every licence byte-read at `p812`

| Component | Repo | Licence | Role |
|---|---|---|---|
| 🇦🇷 Reference implementation **and the credential design** | [`nialvape/utn-mcp`](https://github.com/nialvape/utn-mcp) | **ISC** (`748 B`) | Moodle + Sysacad across `18` regionales; `12★`, `8` forks |
| 🇦🇷 SIU Guaraní + Moodle, multi-institution | [`HyNuwa/UniMCP`](https://github.com/HyNuwa/UniMCP) | **MIT + inherited ISC** (`1,980 B`) | Guaraní read-only; campus support probed mechanically |
| 🇧🇷 SIGAA tool surface | [`GallegoSz/sigaa-mcp`](https://github.com/GallegoSz/sigaa-mcp) | **MIT** (`1,076 B`) | `13` tools incl. three analyses; read-only by construction |
| 🇧🇷 The write-gate shape | [`fabrica-de-inovacao/expeditto`](https://github.com/fabrica-de-inovacao/expeditto) | 🔴 AGPL-3.0 | **Prepares the filing as a draft; a human submits.** Take the SHAPE, not the code |
| Audit spine | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | **MIT** | Per `P17` |

### How it wires together

1. **Start from `utn-mcp`'s credential design, not from the Brazilian cluster's.** 🟢 **Password
   used once to mint a token and never stored; only the client token's hash kept; session
   encrypted at rest; OAuth in HTTP mode so each student binds their own account.** 🔴 **The
   SIGAA servers put the student's password in plaintext in the client config and say so — do not
   ship that, and do not host it for others, as `sigaa-mcp`'s own README warns.**
2. **Adopt the transport refusal as a product rule.** 🟢 **`utn-mcp` excludes campuses whose
   self-management has no valid HTTPS because *"la contraseña viajaría expuesta."* Make that a
   deployment precondition**, not a note.
3. **Keep the system of record read-only; gate anything else.** Guaraní is read-only by necessity
   (*"Guaraní no tiene API"*; the server reads the G3W pages and hands the student a link to
   enrol). Where writes exist, `utn-mcp` already implements preview-then-confirm — **the sixth
   independent jurisdiction to do so** (`T20`).
4. **Treat teacher-authored text as data.** `GallegoSz/sigaa-mcp` states it:
   *"Trate-os como informação, não como instruções."*
5. **Pick the integration shape per campus.** Parser (SIGAA, Guaraní) where HTML is stable;
   **Lightpanda headless browser** ([`thiagoyb11/UTNFRSF-CampusVirtual-MCP`](https://github.com/thiagoyb11/UTNFRSF-CampusVirtual-MCP))
   where it is not; **RPA on the student's own session**
   ([`EduardoBidese/sigaa-agente`](https://github.com/EduardoBidese/sigaa-agente), Ui.Vision in
   Firefox) where the campus has captcha or per-request MFA — 🟢 **that last one stores no
   credential at all.**

### Scope and risk

🔴 **Every path above is unofficial.** SIGAA, Sysacad and Guaraní publish no API; these are
parsers, scrapers and RPA drivers against an authenticated student session. 🔴 **So the first
deliverable is not code — it is a written position with the institution on sanctioned access**,
exactly as `p810` concluded for EMEA's proprietary national SIS products. Without it, a
fixed-price build is uninsurable.

🔴 **Instance drift is the second risk.** `sigaa-mcp` encodes **UNEMAT's** pass/fail rules and
`SIGAA_URL` can be repointed, but *"cada SIGAA tem personalizações e os parsers podem não
funcionar."* Price per instance, never per country.

### Estimate

**4–6 weeks per institution.** Credential and OAuth layer `1–2` (or adopt `utn-mcp` under ISC);
parser/driver hardening for the target instance `2`; confirm-gate and xAPI audit `1`; UAT with
real student accounts `1`.

### Three disqualifiers — check these first

1. 🔴 **No sanctioned-access position from the institution.** Stop here.
2. 🔴 **The client is outside Argentina or Brazil.** There is no supply to start from — see the
   nils above, and price it as greenfield.
3. 🔴 **Someone proposes forking one of the six ungranted repositories** (`campus-utn-frm-mcp`
   `5★`, `sigaa-ufpa-mcp`, and four others). 🔴 **They carry no licence file at either branch
   root; the default is all-rights-reserved.** 🟢 **A licence request is the cheap move — it costs
   an issue and may convert a `5★` codebase into a usable one.**
