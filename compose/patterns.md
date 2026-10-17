---
industry: education
region: Global
updated: 2026-10-17
---

# Compose patterns — Education

> Concrete recipes: named repos, named licences, named wiring. Every component below was
> licence-verified from payload on 2026-10-17
> ([evidence: pass 264](../evidence/verified-repos.2026-10-17-p264.tsv),
> [pass 265](../evidence/verified-repos.2026-10-17-p265.tsv)). **P8–P10 are new in pass 265.**
> Each pattern states the licence boundary — the line the client's proprietary code must stay
> on to keep a copyleft platform from colouring the deliverable.

## P1 — Teacher co-pilot for a national AI-literacy mandate
**Target:** India (Class 3 mandate, AY 2026-27), Mexico (SEP teacher formation), Brazil (MEC basic-education guidance)
**Timeline:** 8–10 weeks to a measurable pilot

```
[instructional_agents  MIT]   multi-agent ADDIE: syllabus -> LaTeX slides -> assessments
        |                      roles: Teaching Faculty / Instructional Designer / TA / Coordinator
        v
[Claw-ED  MIT]                teacher edits and approves before anything reaches a student
        |                      (local-first: curriculum never leaves the institution)
        v
[lineage-skill  Apache-2.0]   every generated artefact stays tied to its source document
        |
        v
[Moodle  GPL-3.0]  <--LTI--  [tsugi  Apache-2.0]      delivery into the installed base
        |
        v
[pykt-toolkit  MIT]           did the teacher formation move learner outcomes?
```

**Wiring:** run `instructional_agents` in its Feedback-Guided mode so a human is in the loop
by construction, not by policy. Deliver through `tsugi` as an LTI 1.3 tool — the agent code
stays MIT/Apache-2.0 and never links against Moodle's GPL.
**Licence boundary:** LTI launch. Everything studio-built sits on the permissive side.
**Why it sells:** three governments are funding exactly this, and
[`intel/market.md`](../intel/market.md) shows Mexico's gap quantified at 76%-vs-36%.

## P2 — Compliant tutoring for the EU AI Act window
**Target:** EMEA higher education and vocational training
**Timeline:** 10–12 weeks; must land before **2027-12-02**

```
[DeepTutor  Apache-2.0]              persistent student model, multi-agent tutoring
        |
        +-- served by --> [Ollama / vLLM, self-hosted]   no prompt leaves the member state
        |
        v
[OpenOLAT  Apache-2.0]  or  [Artemis  MIT]   EMEA-origin, permissive platform
        |
        v
[lrsql  Apache-2.0]  +  [xAPI-Spec  Apache-2.0]   auditable record of every AI interaction
        |
        v
[Moodle 5.1 per-course/per-activity AI toggles]   where Moodle is the installed base
```

**Wiring:** two obligations, two mechanisms. **Transparency (live since 2026-08-02):** an
explicit AI-disclosure interstitial on every `DeepTutor` session entry, logged as an xAPI
statement into `lrsql` so disclosure is provable, not asserted. **High-risk (from
2027-12-02):** any function that determines access, assesses outcomes or influences an
educational path routes through a human-decision step — `DeepTutor` proposes, a named
educator disposes, and `lrsql` holds both records.
**Licence boundary:** the whole stack is Apache-2.0/MIT. Deliberate: an AI Act technical
file is easier to assemble when no component carries network copyleft.
**Why it sells:** the delay created a 14-month window and most clients will read it as a reprieve.

## P3 — Dropout early-warning for a LATAM public university
**Target:** Brazil, Mexico, Colombia, Argentina — Moodle/Chamilo installed base
**Timeline:** 6–8 weeks

```
[Moodle  GPL-3.0]  /  [Chamilo  GPL-3.0]        activity logs, grades, submissions
[academico  MIT]  /  [GibbonEdu  GPL-3.0]       enrolment, attendance, demographics
        |
        v
[lrsql  Apache-2.0]                             one event stream, xAPI vocabulary
        |
        v
[pyedmine  MIT]  or  [pykt-toolkit  MIT]        knowledge tracing + cognitive diagnosis
        |                                        [EduData  Apache-2.0] for baselining
        v
[risk scores + next-best-action]
        |
        v
[Moodle block via tsugi  Apache-2.0]            advisor dashboard, inside the LMS they use
```

**Wiring:** pull through Moodle's REST API into `lrsql` — never read the LMS database
directly, or the integration dies at the next platform upgrade. Train with `pykt-toolkit`'s
standard splits so the accuracy claim is comparable to published baselines instead of
self-graded. Use `pyedmine` when the client wants a recommendation, not just a prediction.
**Licence boundary:** REST + LTI. No studio code links to GPL internals.
**Why it sells:** Brazil's digital-sovereignty framing makes self-hosted inference the
policy-preferred architecture, not the budget option.

## P4 — Education skill pack for a client's existing assistant
**Target:** any region; clients who already run an AI assistant
**Timeline:** 3–4 weeks

```
[Bloom  MIT]                             adaptive tutoring skill
[universal-diagnostic-tutor-skill  MIT]  diagnose the misconception first
[universal-examprep-skill  MIT]          teach from the client's own slides, page-cited
[anki-mcp-server  MIT]                   spaced repetition behind MCP
[tutor-mcp  MIT]                         tutoring loop behind MCP
        |
        v
[client's assistant]  -- MCP -->  [institutional content + Anki decks]
```

**Wiring:** ship skills, not an application. The MCP servers expose the institution's
content and the learner's review schedule; the skills carry the pedagogy. `fsrs4anki` (MIT)
or `fsrs-rs` (BSD-3-Clause) supplies the scheduler so retention is managed by a real
algorithm rather than a prompt.
**Licence boundary:** every component MIT or BSD-3. Nothing to negotiate.
**Why it sells:** this is **T2** in [`intel/trends.md`](../intel/trends.md) — the fastest-moving
shape in education open source, and the cheapest engagement to start.
**Avoid:** `education-agent-skills` (873 stars) is **CC-BY-SA-4.0**. Superb reference,
ShareAlike on derivatives — read it, do not vendor it into a proprietary pack.

## P5 — Integrity-first assessment where student-facing AI is restricted
**Target:** US states barring AI from high-stakes decisions (OK, MD), NYC K-8 moratorium districts
**Timeline:** 6–8 weeks

```
[Artemis  MIT]              programming/modelling/text exercises, automated FEEDBACK
        |                    (feedback, explicitly not autonomous grading)
        v
[dolos  MIT]                source-code plagiarism detection across submissions
        |
        v
[Numbas  Apache-2.0]        randomised maths assessment; SCORM-packaged output
        |
        v
[scorm-again  MIT]          runs that SCORM inside the institution's existing LMS
        |
        v
[teacher sign-off]  ------>  grade of record
```

**Wiring:** the architecture encodes the regulation. No AI output becomes a grade without a
named educator's action; `Artemis` produces feedback and evidence, the teacher produces the
grade. `Numbas` randomisation means per-student variants, which is integrity by design
rather than detection after the fact.
**Licence boundary:** fully permissive, and `scorm-again` keeps legacy content in place —
no content migration in the SOW.
**Why it sells:** in restricted jurisdictions this is the AI story that is unambiguously
permitted (see **T8**).

## P6 — AI-native corporate L&D, no LMS legacy
**Target:** enterprise L&D, North America and EMEA
**Timeline:** 5–7 weeks

```
[mentingo  MIT]                      AI-native LMS: AI mentor w/ voice role-play + auto-scoring,
        |                             AI course builder (policy docs -> structured courses),
        |                             open-ended answer grading, bring-your-own-key
        +-- traces --> [Langfuse]     cost, latency and mentor output, per call
        +-- exposes --> [MCP]         the client's assistant can drive the LMS
        |
        v
[fsrs4anki  MIT]                     spaced repetition for compliance-knowledge retention
        |
        v
[lrsql  Apache-2.0]  + [xAPI-Spec]   completion and competency evidence for audit
```

**Wiring:** feed existing policy and knowledge-base documents into the AI course builder,
then use role-play scenarios for compliance and sales enablement with auto-scoring as
formative — never summative — signal. Langfuse tracing gives the client per-call cost
visibility from day one, which is usually the first question procurement asks in month two.
**Licence boundary:** MIT throughout.
**Why it sells:** retrofitting Moodle for corporate L&D costs more than starting on a base
that already has the agent, the tracing and the MCP endpoint.

## P7 — Sovereign tutoring deployment, air-gapped
**Target:** Brazil (MEC digital sovereignty), EMEA public sector, defence/government training
**Timeline:** 8–10 weeks

```
[Open TutorAI CE  BSD-3-Clause]      multimodal tutoring: voice, video, 3D avatars, Docker-first
        |
        +-- inference --> [Ollama / vLLM on-premise]    no external API
        v
[OpenOLAT  Apache-2.0]               Apache-2.0 LMS: no copyleft anywhere in the stack
        |
        v
[lrsql  Apache-2.0]                  all records on-premise
```

**Wiring:** every component runs inside the perimeter and the entire stack is
permissive — which matters when a government client wants to audit, modify and redistribute
internally without GPL obligations following the artefact. Open TutorAI's avatar and voice
layer is the differentiator where face-to-face interaction is culturally expected.
**Licence boundary:** none to manage. That is the point of this pattern.
**Why it sells:** Brazil's MEC *Referencial* asks for national solutions reducing dependence
on global platforms. This is that, literally.

## P8 — Sovereign agentic layer over Brazil's municipal school stack
**Target:** Brazilian municipal and state education networks (SME/SEDUC)
**Timeline:** 8–10 weeks to a pilot in one network
**Why it exists:** this is the pattern pass 264 could not write, because it had not found a
LATAM-origin base.

```
[i-educar  GPL-2.0]        enrolment, attendance, grades, the municipal system of record
   (portabilis, BR)        origin: prefeitura de Itajai-SC -> Portal do Software Publico, 2008
        |  \                last commit 2026-10-14, 34,948 commits
        |   \__ teachers __> [i-diario  AGPL-3.0]   portal do professor (payload is pt-BR AGPL)
        |
        |  === LICENCE BOUNDARY: HTTP / LTI 1.3. Nothing below links against the above. ===
        v
[tsugi  Apache-2.0]        LTI 1.3 tool; the studio's deliverable starts here
        |
        v
[DeepTutor  Apache-2.0]    tutoring, persistent student model
[instructional_agents MIT] teacher materials, ADDIE pipeline
        |
        +-- served by --> [Ollama / vLLM, on-premise]   no student prompt leaves the municipality
        |
        v
[pyedmine  MIT]            dropout / at-risk modelling on i-Educar's attendance + grade history
        |
        v
[lrsql  Apache-2.0] + [xAPI-Spec  Apache-2.0]   audit trail for PL 2338 high-risk classification
```

**Wiring:** read i-Educar through its API/database views, never by patching it — GPL-2.0 is a
distribution licence and an unmodified upstream keeps the municipality's upgrade path intact.
Teacher-facing output surfaces in i-Diário, which teachers already open daily; student-facing
output goes through an LTI launch. Attendance plus grade history in i-Educar is exactly the
feature set `pyedmine` needs, so the dropout model has training data on day one instead of
after a year of instrumentation.
**Licence boundary:** the HTTP/LTI line. i-Educar stays GPL-2.0 and unmodified, i-Diário stays
AGPL-3.0 and unmodified, everything studio-built is MIT/Apache-2.0.
**Legal note:** i-Diário's licence payload is a **Portuguese translation** of AGPL-3.0; FSF
translations are unofficial. Cite the English AGPL-3.0 in the SOW.
**Why it sells:** MEC's *Referencial* (March 2026) asks for national solutions that reduce
dependence on global platforms. A Brazilian-maintained base with federal software-public
provenance, local inference and an auditable record is not an interpretation of that policy —
it is the policy, implemented. And `PL 2338` would classify education-related **selection** as
high-risk, so the xAPI trail is built before the law needs it, not after.

## P9 — Offline-first tutoring where there is no network
**Target:** rural LATAM, low-bandwidth APAC, anywhere power and connectivity are intermittent
**Timeline:** 6–8 weeks to a device-level pilot

```
[Kolibri  MIT]                     complete learning platform that runs with NO network
  (learningequality)               content channels sync opportunistically when a link appears
        |                          39,803 commits; MIT - no copyleft anywhere in this stack
        v
[local quantised model via Ollama]  tutoring and explanation on-device
        |                           (DeepTutor's prompting patterns, Apache-2.0, as the design
        |                            reference - its orchestration assumes a server; do not
        |                            port it wholesale onto a classroom device)
        v
[fsrs-rs  BSD-3]  /  [fsrs4anki  MIT]   retention scheduling that needs no server at all
        |
        v
[xAPI statements buffered locally] --sync-on-contact--> [lrsql  Apache-2.0]  central reporting
```

**Wiring:** every component assumes absence of network as the default state, not as an error.
Kolibri handles content distribution and sync; FSRS schedules review entirely locally (it is
an algorithm, not a service); xAPI statements queue on device and drain when a link appears.
The model is the only part that needs sizing care — budget the device class first and choose
the quantisation to fit it, because this is the one pattern where the hardware is the
constraint rather than the licence.
**Licence boundary:** none. MIT, BSD-3 and Apache-2.0 end to end.
**Why it sells:** it is simultaneously the answer to *"our schools lose connectivity"* and to
*"no student data may leave the premises"* — and nothing leaves the device, so the
data-protection conversation (LGPD, GDPR, state privacy statutes) is short. Note what it is
**not**: a frontier-model experience. Say that up front.

## P10 — Permissive autograding where AI is barred from the grade
**Target:** US states barring AI from high-stakes decisions (Idaho, Oklahoma, NYC K-8), EU
institutions under Annex III, Brazilian institutions ahead of `PL 2338`
**Timeline:** 4–6 weeks

```
[Autolab  Apache-2.0]        auto-graded programming assignments + course management (CMU)
   or
[nbgrader  BSD-3-Clause]     assign and grade notebooks (the data-science department's default)
   or
[Artemis  MIT]               automated FEEDBACK with an auditable exercise runner (TUM)
        |
        |   the grade is produced DETERMINISTICALLY, by a test suite, not by a model
        v
[teacher sign-off step]      explicit, logged, reversible
        |
        +--- optional, on the feedback side only ---> [LLM explains WHY a test failed]
        |                                              never proposes or alters the mark
        v
[dolos  MIT]                 integrity check on submissions
        |
        v
[lrsql  Apache-2.0]          who decided what, when - the record a regulator asks for
```

**Wiring:** the architectural claim is the separation. Marks come from a deterministic runner;
the model only ever produces explanation text attached to an already-computed result, and the
human sign-off is a logged state transition rather than a UI affordance. That makes "AI did not
make a decision about a student" demonstrable from the audit log instead of asserted in a
policy document.
**Licence boundary:** none to manage — Apache-2.0, BSD-3 and MIT throughout. `INGInious`
(AGPL-3.0) is the substitute where UCLouvain's feature set is wanted and AGPL is acceptable.
**Why it sells:** it is the one AI story that is unambiguously permitted in the jurisdictions
tightening fastest, it is cheaper than an LLM grader, and it gets *more* defensible as
regulation increases rather than less.

## P11 — Agent layer over India's national stack (MIT end-to-end, no copyleft anywhere)

**When:** an APAC public-sector engagement — a state education department or ministry — that
already runs **DIKSHA** or a Sunbird-derived platform. **Do not propose a migration.**

**Why it wins:** the platform, the content pipeline and the political precedent exist. The
engagement is the agent layer on top, and every component is permissive, so there is **no
copyleft obligation anywhere in the stack** — the only pattern in this file with that property.

```
Sunbird-Ed/SunbirdEd-portal        MIT    national platform (38,046 commits)
project-sunbird/knowledge-platform MIT    content/knowledge backend  <-- integrate HERE
Sunbird-Ed/SunbirdEd-mobile-app    MIT    mobile client
  |
  +-- ls1intum/Pyris               MIT    LLM microservice (REST, swappable pipelines)
  |     +-- ls1intum/Iris          MIT    tutor: hints and leading questions, not answers
  +-- numbas/Numbas                Apache-2.0  assessment, executes in-browser
  +-- pykt-team/pykt-toolkit       MIT    learner model over Sunbird telemetry
  +-- yetanalytics/lrsql           Apache-2.0  xAPI Learning Record Store
```

**Wiring, concretely:**
1. Integrate at the **`knowledge-platform` API**, not in the portal UI. The portal is the piece
   a ministry has customised and will keep customising; the backend API is stable.
2. Stand up **Pyris** as a separate service and point it at the content store. Pyris already
   exposes swappable LLM pipelines and RAG over instructor material, so bring-your-own-model
   (including a locally hosted one) is configuration, not code.
3. Emit **xAPI** statements to **lrsql** for every tutor interaction. This is what makes the
   learner model trainable later and the deployment auditable now.
4. Attach **Numbas** for assessment. Browser-side execution means submissions need not leave the
   device — carry that into the data-protection annex explicitly.
5. Fit **pykt-toolkit** on the accumulated telemetry only once there is enough of it. Do not
   promise a learner model in phase 1; promise the instrumentation that makes one possible.

**Licence posture to put in the SOW:** MIT / MIT / MIT / MIT / Apache-2.0 / MIT / Apache-2.0.
Nothing here triggers source disclosure, including on a hosted deployment.

**Slug caution:** `Sunbird-Ed/sunbird-ed-portal` **does not resolve**. The live slugs are
camel-case (`SunbirdEd-portal`, `SunbirdEd-mobile-app`).

---

## P12 — Declassify-by-design assessment for Vietnam's 2027 deadline

**When:** an APAC engagement touching **automated assessment** or any form of student
**behavioural monitoring**, in Vietnam or any jurisdiction converging on the same test (see T17).

**The governing fact** ⚠️ *(secondary-source grade)*: Vietnam's July 2026 decision makes these
uses high-risk **only where the AI output is the sole basis for a decision without meaningful
human review.** Compliance **2027-03-01**; **+6 months** if the system was live before
**2026-08-15**.

**So the deliverable is not a compliance document — it is an architecture that stays out of the
high-risk class.**

```
ls1intum/Artemis            MIT   assessment platform, human-in-the-loop by construction
  +-- ls1intum/Athena       (!!)  feedback SUGGESTED to instructor, never applied to student
  +-- ls1intum/Iris         MIT   tutor: hints only, no grading authority
  +-- ls1intum/Pyris        MIT   LLM microservice; swap to a local model for data residency
  +-- config gate           ----  every AI subsystem independently switchable OFF
  |
  +-- yetanalytics/lrsql    Apache-2.0  immutable xAPI record of who decided what, and when
```

**The four build rules that do the legal work:**
1. **Athena suggests; an instructor disposes.** No code path applies a model-generated grade to
   a student record. This is the single requirement that keeps the system out of the high-risk
   class under Vietnam's carve-out, Oklahoma's `SB 1734` and Maryland's rule alike.
2. **Config-gate every AI subsystem.** Artemis already does this. It means "AI was off for this
   cohort" is a verifiable configuration claim, not a promise.
3. **Log the human decision, not just the model output.** `lrsql` holds an xAPI record showing a
   named human reviewer and a timestamp per decision. "Meaningful human review" is an evidentiary
   claim; without a log it is unprovable.
4. **Keep the model swappable** via Pyris, so a data-residency or sovereign-hosting requirement
   is a configuration change rather than a re-platforming.

⚠️ **Two cautions, stated plainly.** (a) **`ls1intum/Athena` serves no licence payload** — marked
`(!!)` above. Artemis's MIT grant does **not** automatically extend to it. Resolve the licence in
writing with TUM before Athena ships in a deliverable, or implement the feedback-suggestion step
yourself against Pyris. (b) The Vietnam dates **conflicted across sources** this pass and could
not be confirmed against the primary decision text; confirm before contracting to a deadline.

---

## P13 — Governance retrofit for a LATAM university that already adopted AI

**When:** the 87%-adopting / 26%-governed institution ⚠️ described in T16 — which is most of
LATAM higher education. The client has AI in use across faculties and **no strategy, inventory
or review process.** No platform displacement is required, which is why this sells.

**This pattern is deliberately mostly not software.** Writing code first is the standard mistake
here; the deliverable is governance *with* instrumentation, in that order.

```
Phase 1  Inventory        what models, in whose hands, on whose data
         +-- dodona-edu/dolos        MIT   integrity baseline on existing submissions
Phase 2  Policy           AI-use policy, human-review rules, assessment-integrity standard
         +-- aligned to: UNESCO IESALC guidance; Brazil MEC referencial; PL 2338 (high-risk
             education-related selection) if the client is Brazilian
Phase 3  Instrumentation  make the policy observable instead of aspirational
         +-- yetanalytics/lrsql     Apache-2.0  xAPI record store
         +-- adlnet/xAPI-Spec       Apache-2.0  the vocabulary
Phase 4  Controlled pilot one faculty, one use case, measured
         +-- ls1intum/Artemis       MIT   if assessment; config-gated AI
         +-- ls1intum/Iris + Pyris  MIT   if tutoring; local model where data cannot leave
Phase 5  Learner model    only once phases 1-4 produce trustworthy data
         +-- pykt-team/pykt-toolkit MIT
```

**Why this order and not the reverse:** a learner model built on ungoverned data inherits every
consent and integrity defect in the institution. Phase 5 is where the client *wants* to start
and where the engagement should finish.

**Entry points that are real convening bodies, not citations:** UNESCO's **Observatory on AI in
Education for LAC** (launched 2026-04-14, Santiago, at ECLAC), **UNESCO IESALC**, **Ceibal**
(Uruguay), and the **ILIA** index. The public/private split ⚠️ (**68%** public vs **84%** private
non-profit) says the public sector is the larger gap and the slower sale — staff accordingly.

**Do not** brief [`guedesindev/ai_tutor_forge`](https://github.com/guedesindev/ai_tutor_forge)
as regional capability. It is GPL-3.0, 18★, 21 commits — a personal project, and the only
Portuguese-language education agent this base has verified.

---

## P14 — An agent inside the Canvas the client already runs, with an MIT-only deliverable *(new in pass 267)*

**When:** the client runs **Canvas** — the dominant LMS in North American higher education — and
wants an AI layer over *their* courses, rosters, assignments and grades. The most common NA
situation in this KB, and until pass 267 it had no pattern, because this base believed Canvas was
closed SaaS. It is **AGPL-3.0 with 78,765 commits**.

```
Client's existing system  instructure/canvas-lms         AGPL-3.0   DO NOT FORK. Do not link.
         |                                                          78,765 commits; the network
         |                                                          clause is the only reason you
         |                                                          stay out -- not access.
         | Canvas REST API  (process boundary = licence boundary)
         v
Doorway   vishalsachdev/canvas-mcp      MIT   295*, 1,026 commits, v1.14.0 (Oct 2026)
          +-- 102-126 tools + 8 agent skills; courses, assignments, grades, roster
          +-- speaks MCP to Claude / Cursor / Codex / 40+ clients
         |
         v
Pedagogy  ls1intum/Pyris                MIT   LLM microservice: exercise feedback, RAG over
          |                                   instructor-supplied course material
          +-- ArnaudGuiovanna/tutor-mcp  MIT   when a constrained tutoring loop is enough
          +-- ls1intum/Iris              MIT   hints and leading questions, not answers
         |
         v
Grading   Submitty/Submitty             BSD-3  submission + autograde + TA workflow
          +-- ucbds-infra/otter-grader  BSD-3  Python AND R; ships a CANVAS AUTOGRADER ADAPTER
          +-- jupyter/nbgrader          BSD-3  notebook courses
         |
         v
Audit     yetanalytics/lrsql            Apache-2.0  xAPI record of every AI interaction
          adlnet/xAPI-Spec              Apache-2.0  the vocabulary
```

**The licence argument, which is the point of the pattern:** every component you deliver is **MIT,
BSD-3 or Apache-2.0**. The only copyleft artefact in the system is **Canvas itself, which the
client already owns and operates**. You call its REST API across a process boundary and never link
its code, so nothing in the deliverable derives from an AGPL work — a sentence the client's legal
team can verify in an afternoon. **AGPL platform, MIT doorway.**

**Sequence that avoids the usual failure:** stand up `canvas-mcp` read-only against a sandbox
course first and prove the tool surface, *then* enable writes. Count the tools you actually
register — the project publishes **102 in its About blurb and 126 in its README**, and the default
profile registers fewer than either. Quote the range to the client, never a single number.

**Where the client runs Moodle instead:** the doorway is
[`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) — **AGPL-3.0,
open-core (premium tools sold separately), 10 free tools, 1★, 57 commits** — or a direct build
against Moodle Web Services. **Price the Moodle variant as engineering, not integration:** its MCP
surface is roughly 1/300th as adopted as Canvas's, and the AGPL network clause now sits in *your*
deliverable rather than only in the client's platform.

---

## P15 — Defensible autograding with zero copyleft, end to end *(new in pass 267)*

**When:** state or institutional rules bar AI from *determining* a grade (Oklahoma `SB 1734`,
Ohio `HB 96`, California `AB 1159`, Idaho `SB 1227`, and the "meaningful human review" test in
T17), but the client still needs assessment at scale. The grade must be **deterministic,
reproducible and explainable on appeal**; the AI may explain, suggest and tutor around it.

```
Substrate   jupyterhub/jupyterhub        BSD-3   8.4k*, 8,913 commits; per-student environments
           |
Grading    Submitty/Submitty            BSD-3   802*, 9,316 commits, 1.1k forks (RPI/RCOS)
           |                                    submission + autograding + TA grading workflow
           +-- ucbds-infra/otter-grader  BSD-3   UC Berkeley; Python AND R; Canvas/Gradescope
           |                                    adapters + student-side public checks
           +-- jupyter/nbgrader          BSD-3   notebook assign/release/collect/grade
           +-- autolab/Autolab           Apache-2.0  CMU; course-management shell
           +-- numbas/Numbas             Apache-2.0  maths; executes ENTIRELY IN THE BROWSER
           |                                        -> submission never leaves the device
           v
AI layer   ls1intum/Pyris               MIT     feedback SUGGESTIONS to the instructor
           (never writes a grade)               + RAG over the course's own material
           v
Record     yetanalytics/lrsql           Apache-2.0  who saw what, who approved, when
```

**Six permissive grading options, three licences (BSD-3 / Apache-2.0 / MIT), zero copyleft.**
This is the pattern's whole commercial content: **autograding is a solved, free problem.** Proposing
to build one is proposing to rebuild five mature university systems. The billable work is
(a) wiring a grader into the client's LMS — `otter-grader`'s Canvas adapter does half of it,
(b) the pedagogy of the feedback, and (c) **defensibility**: the appeal path, the human sign-off
record, the disclosure artefact.

**The regulatory test this satisfies by construction:** the deterministic grader produces the mark;
the model never touches it; `lrsql` holds the evidence that a human disposed of every AI
suggestion. That is **declassification by architecture** (T17), not by policy document — and it
reuses P10's posture with five permissive components instead of three.

**Do not** substitute `PrairieLearn` into this stack without legal review: it is strong software,
but the grant is **partitioned four ways** (AGPL-3.0 Community Edition, a separate-terms Enterprise
Edition directory, AGPL client-side JavaScript, MIT contributor portions) and the GitHub sidebar
shows no label at all. Likewise `RunestoneInteractive/rs`, whose MIT headline excepts a
**commercial** Handsontable dependency.

---

## P16 — Delivering India's Class 3-8 AI curriculum on India's own MIT stack *(new in pass 267)*

**When:** an APAC public-sector or education-group engagement in India. **The mandate is dated and
the platform is permissive** — the only region in this KB where both are verified (T22, and the
APAC section of [`intel/market.md`](../intel/market.md)).

- **Demand:** AI and computational thinking compulsory from **Class 3**; CT&AI curriculum for
  Classes 3-8 **launched 2026-04-01**; implementation from the **2026-27 session**; Classes 9-10 in
  **2027-28**; teacher training through **NISHTHA**; **₹500 crore** Centre of Excellence announced
  in the 2025-26 budget. ⚠️ Secondary-source — dates decision-usable, figures directional.
- **Supply:** the national stack is **MIT, end to end.**

```
Platform   Sunbird-Ed/SunbirdEd-portal            MIT   38,046 commits, 317 forks (41*)
           project-sunbird/knowledge-platform     MIT   content/knowledge services
           Sunbird-Ed/SunbirdEd-mobile-app        MIT   mobile client -- the real access path
           ^ the codebase under DIKSHA (NCERT / Ministry of Education)
           |
Curriculum DaRL-GenAI/instructional_agents        MIT   488*, EACL'26: ADDIE pipeline
           |                                            syllabus -> slides -> assessments,
           |                                            with Instructional Designer / TA roles
           +-- JuneYaooo/lineage-skill        Apache-2.0  turns NCERT material into agent skills
           |                                              that stay TIED TO THEIR SOURCES
           v
Teacher    SirhanMacx/Claw-ED                     MIT   local-first, teacher-reviewed lesson drafts
enablement ls1intum/Iris + Pyris                  MIT   tutor + LLM microservice, RAG over the
           |                                            ministry's own curriculum documents
           v
Offline    learningequality/kolibri                MIT  offline delivery where bandwidth fails
           learningequality/studio                 MIT  authoring + REMIX AGAINST NATIONAL CURRICULA
           Tangerine-Community/Tangerine        GPL-3.0  offline ASSESSMENT -- keep behind an API
           v
Measure    bigdata-ustc/EduData              Apache-2.0  datasets/preprocessing
           pykt-team/pykt-toolkit                  MIT   knowledge tracing, once data is trustworthy
```

**Why this is an unusually clean pattern:** no platform displacement is proposed, no copyleft
enters the deliverable (Tangerine is the one exception and sits behind an API boundary), and the
client's own ministry already maintains the base. **The scarce thing is not the platform — it is
Classes 3-8 content and teacher capability at national scale**, which is exactly what
`instructional_agents` (peer-reviewed, MIT) and `lineage-skill` (provenance-preserving) address.

**The failure mode to design against, from the region's own recent history:** South Korea mandated
AI digital textbooks, saw **under 30% adoption**, and in **August 2025 its National Assembly
stripped them of official textbook status** after teachers' unions said the pace had outrun
preparation. **Lead with NISHTHA-aligned teacher enablement and measurable classroom readiness,
not content volume.** A mandate engagement is cancelled by unprepared teachers, not by missing
content.

⚠️ **Sunbird slug trap:** the live slugs are camel-case (`Sunbird-Ed/SunbirdEd-portal`);
`Sunbird-Ed/sunbird-ed-portal` does not resolve. And do not read Sunbird's **41 stars** as
adoption — 38,046 commits and 317 forks are the signal, re-measured and reproduced in pass 267.

---

## P17 — Delivering a primary-school AI-literacy mandate when the curriculum cannot be licensed *(new in pass 268)*

**The engagement.** A ministry or large district must deliver AI instruction to primary pupils
against a dated mandate — China (≥8 h/year from age six, since Sep 2025), Singapore MoE (Mar 2026),
India CBSE Classes 3-8 (session 2026-27), or the EU AI Act Art. 4 staff-literacy duty.

**Why this pattern exists and `P91-G`/`P16` do not cover it.** `Gap 367` has carried *"no permissive
AI curriculum for primary"* for ~175 passes as *"the largest named, dated, deadline-bearing demand on
this shelf with no supply"*, naming **Code.org** and **MIT Day of AI** as alternatives. Pass 268 read
the licences. **The gap is not under-searched — it is correctly empty**, and that changes the
proposal rather than delaying it.

| what | component | licence | role |
|-------|-----------|---------|------|
| Delivery engine | [`code-dot-org/code-dot-org`](https://github.com/code-dot-org/code-dot-org) | **Apache-2.0** *(source and assets only — see the carve-out)* | Lesson delivery, progress tracking, classroom management, block-based programming environment. **215,796 commits** of it. |
| Offline delivery, where connectivity is the constraint | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** | Ships the originated content to schools with no network |
| Content authoring + national-curriculum remix | [`learningequality/studio`](https://github.com/learningequality/studio) | **MIT** | The pipeline that organises originated lessons into channels and aligns them to the national curriculum |
| Teacher-facing generation, human-in-the-loop | [`DaRL-GenAI/instructional_agents`](https://github.com/DaRL-GenAI/instructional_agents) | **MIT** (EACL'26) | ADDIE multi-agent: syllabus → slides → assessments, for *teacher review* |
| Local-first lesson drafting | [`SirhanMacx/Claw-ED`](https://github.com/SirhanMacx/Claw-ED) | **MIT** | Draft editable lessons where pupil data cannot leave the building |
| Pupil-facing tutoring, if in scope at all | [`ls1intum/Iris`](https://github.com/ls1intum/Iris) + [`Pyris`](https://github.com/ls1intum/Pyris) | **MIT** | Pedagogically constrained by design (hints, not answers) — the posture a high-risk classification wants |

**Wiring.**
1. **Fork the Code.org platform, strip the content.** Deploy the Apache-2.0 engine. Delete, do not
   adapt, every Proprietary Material: artwork, graphics, sounds, lectures, videos, logos, characters
   and fonts. The payload confines them to *"Code.org's own web site, mobile applications, or social
   media channels ... without modification or embedding in another format."*
2. **Originate the lessons against AI4K12's Five Big Ideas** — the framework Code.org and MIT Day of
   AI both organise on — but **write your own text**, because
   [`touretzkyds/ai4k12`](https://github.com/touretzkyds/ai4k12) **serves no licence payload**
   (`Gap 354`). An unlicensed framework can be *conformed to*; it cannot be *redistributed*.
3. **Author and package in Kolibri Studio**, align to the national curriculum there, publish as
   channels, and deliver through Kolibri where bandwidth is the real constraint.
4. **Put `instructional_agents` behind the teachers, not the pupils.** Generation for teacher review
   keeps the system out of the EU AI Act's high-risk band via the `P2`/`T17` meaningful-human-review
   route, and keeps a staff-literacy duty satisfiable by the same deployment.
5. **Add `Iris`/`Pyris` only if pupil-facing tutoring is genuinely in scope.** For primary pupils in
   a mandate engagement it usually is not, and the config-gated design means the platform runs
   identically with AI off — which is the demonstration a regulator wants.

🔴 **The three things that must be said in the first meeting.**
- **The curriculum is the deliverable; the engine is the freebie.** Budget belongs in instructional
  design and localisation, not platform build.
- **You cannot reuse Code.org's Minecraft, Star Wars, Frozen, Angry Birds or Plants vs. Zombies
  activities.** The `NOTICE` lists them as third-party licensed IP — Code.org cannot sublicense
  them, so no contract with Code.org would help either. Also excluded: **Font Awesome Pro**.
- **A client who has seen Code.org assumes the lessons come with the code.** Correcting that
  assumption before signature is the single highest-value sentence in this pattern.

🟢 **Estimate shape:** 10-14 weeks. Platform deployment and content stripping is ~2 weeks of it;
the rest is curriculum origination, translation and teacher enablement. **Do not quote this as a
platform project.**

## P18 — An agent over the system of record a US district already runs *(new in pass 268)*

**The engagement.** A US district, state education agency, or a vendor selling into them, wants
AI-assisted early warning, reporting or an agent surface — with no copyleft boundary in the
deliverable.

**Why this pattern exists.** `verticals/solutions.md` published, in pass 267, that no North American
public-sector base existed. It does: **Ed-Fi**, Apache-2.0, and this base's own gap register has
carried it as *the only permissive system of record* for roughly 200 passes. Every layer below is
permissive, which is what Canvas (AGPL-3.0) and Open edX (AGPL-3.0) deny.

| layer | component | licence |
|-------|-----------|---------|
| Student data model | [`Ed-Fi-Data-Standard`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard) | **Apache-2.0** |
| System of record (existing deployments) | [`Ed-Fi-ODS`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) + [`Ed-Fi-ODS-Implementation`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS-Implementation) | **Apache-2.0** |
| System of record (new builds) | [`Data-Management-Service`](https://github.com/Ed-Fi-Alliance-OSS/Data-Management-Service) | **Apache-2.0** |
| Learner event stream | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) + [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec) | **Apache-2.0** |
| Risk model | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) or [`ZhijieXiong/pyedmine`](https://github.com/ZhijieXiong/pyedmine) | **MIT** |
| Agent surface over the LMS beside it | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | **MIT** |
| Human review surface | [`uPortal-Project/uPortal`](https://github.com/uPortal-Project/uPortal) | **Apache-2.0** |

**Wiring.**
1. **Read from Ed-Fi, do not re-model.** The agency's students are already in the Ed-Fi model, so
   the integration is *conformance*, not mapping — and it ports to the next district unchanged.
2. **Write AI output to the LRS, never to the system of record.** This is the load-bearing decision.
   `Gap 314` establishes that **DMS provisioning is create-only**: an AI-generated risk flag, an
   AI-assisted grade or generated evidence is a **data-model extension and a re-provision of the
   database**, not an insert. Writing to `lrsql` as xAPI statements keeps the system of record
   untouched and keeps the AI output auditable and separable — which is also what a
   meaningful-human-review posture (`T17`) requires.
3. **Train the risk model on Ed-Fi reads plus xAPI events**, with `pykt-toolkit` for prediction or
   `pyedmine` where the deliverable is a recommender.
4. **Surface it to staff through uPortal** (Apache-2.0, campus single-pane) and reach the LMS via
   `canvas-mcp` (MIT) — never by forking `instructure/canvas-lms` (AGPL-3.0).

🔴 **Three prices to quote from the register, not the README.**
- **DMS adoption is a re-platforming with a data migration**, stated normatively in
  `docs/PRD-v8.0.md` (`Gap 303`). **Never price it as an in-place cutover.**
- **DMS provisioning is create-only** (`Gap 314`) — hence step 2.
- **OneRoster is absent from DMS v8.0** (`Gap 309`), while native **OneRoster 1.2** shipped in the
  **ODS/API 7.3.2** line (search-summary grade). **Say which line you are quoting**, because the
  rostering story differs between them. Also note the platform moved to **.NET 10** ahead of .NET 8
  end-of-support in **November 2026** — a client on an older ODS has a dated upgrade of its own.

⚠️ **Do not brief a state adoption count.** Neither Ed-Fi README names a state or an agency; the
14-state list is third-party, and **`ed.sc.gov` did not resolve from this environment**, so the one
primary government page that would settle it was not read. Quote the **licence** — payload-verified
2026-10-17 — and let the client's procurement confirm their own state's status.

🟢 **Estimate shape:** 8-10 weeks for the Ed-Fi read + LRS write + risk model + staff surface, on an
existing ODS deployment. **Add a separate migration line item if the client is moving ODS → DMS**;
that is not part of this pattern and it is not small.

## Component quick reference

| Need | Component | Licence |
|------|-----------|---------|
| Tutoring agent | `HKUDS/DeepTutor` | Apache-2.0 |
| Course material generation | `DaRL-GenAI/instructional_agents` | MIT |
| Human-reviewed lesson drafting | `SirhanMacx/Claw-ED` | MIT |
| Source provenance for generated content | `JuneYaooo/lineage-skill` | Apache-2.0 |
| Automated assessment + feedback | `ls1intum/Artemis` | MIT |
| Maths e-assessment | `numbas/Numbas` | Apache-2.0 |
| Code plagiarism detection | `dodona-edu/dolos` | MIT |
| Knowledge tracing | `pykt-team/pykt-toolkit` | MIT |
| Tracing + diagnosis + recommendation | `ZhijieXiong/pyedmine` | MIT |
| Education datasets | `bigdata-ustc/EduData` | Apache-2.0 |
| Spaced repetition scheduler | `open-spaced-repetition/fsrs4anki` · `fsrs-rs` | MIT · BSD-3 |
| LTI tool framework | `tsugiproject/tsugi` · `pylti1.3` | Apache-2.0 · MIT |
| Learning record store | `yetanalytics/lrsql` + `adlnet/xAPI-Spec` | Apache-2.0 |
| SCORM runtime | `jcputney/scorm-again` | MIT |
| Permissive LMS — institutional | `OpenOLAT/OpenOLAT` | Apache-2.0 |
| Permissive platform — lesson delivery | `oppia/oppia` | Apache-2.0 |
| Permissive platform — offline-first | `learningequality/kolibri` | MIT |
| Autograding — programming + course mgmt | `autolab/Autolab` | Apache-2.0 |
| Autograding — notebooks | `jupyter/nbgrader` | BSD-3-Clause |
| Brazilian municipal SIS + teacher portal | `portabilis/i-educar` · `portabilis/i-diario` | GPL-2.0 · AGPL-3.0 |
| AI-native LMS | `Selleo/mentingo` | MIT |
| Multimodal tutoring platform | `Open-TutorAi/open-tutor-ai-CE` | BSD-3-Clause |
| MCP: spaced repetition · tutoring | `ankimcp/anki-mcp-server` · `tutor-mcp` | MIT |

**Do not compose:** `formalms/formalms` (**GPL-2.0**, despite a 2026 review publishing it as
Apache-2.0), Fedena (`foradian/fedena`, `projectfedena/fedena` — **abandoned since 2012/2016,
no licence payload**, still recommended by vendor comparisons as *the* Apache-2.0 education
ERP), `h5p/h5p-php-library` (**GPL-3.0**, widely miscited as MIT — including in earlier Globant
KB cycles), `os4ed/openSIS-Classic` (no licence payload served; unverified),
`CaviraOSS/PageLM` (non-commercial, redistribution prohibited),
`GarethManning/education-agent-skills` (CC-BY-SA-4.0 ShareAlike),
`GeminiLight/awesome-ai-llm4education` (no licence served),
`human-skill-tree` / `freelingo` / `lumen` (AGPL/GPL — network copyleft on hosted delivery).

## Declared gaps

- **Still no pattern for autonomous grading, and now it is a design choice rather than a
  shortage.** P10 exists precisely because the regulated markets (US states, EU Annex III,
  Brazil's `PL 2338`) are converging on human decision-makers. Deterministic autograding plus a
  logged human sign-off is the architecture; an LLM that assigns marks is not a pattern this KB
  will publish.
- **Retracted: "no APAC-origin component appears in any pattern above."** `HKUDS/DeepTutor`
  (P2, P8) is from the **Data Intelligence Lab at the University of Hong Kong**, and
  `bigdata-ustc/EduData` (USTC) and `HFUT-LEC/EduStudio` (Hefei University of Technology) are
  in the quick reference. The APAC-origin components were in the patterns the whole time; the
  gap statement was not re-tested against them. What remains true: **no APAC-origin
  *platform*** anchors any pattern.
- **No LATAM-origin agent in any pattern.** P8 is anchored on LATAM-origin *platforms*
  (`i-educar`, `i-diario`) with non-LATAM agents on top. That is the honest state of the shelf:
  the region publishes systems of record, not agents.
- **P9's model layer is deliberately unspecified.** Device class drives quantisation, and this
  KB has not benchmarked tutoring quality for small local models on classroom hardware. Naming
  a model here would be a guess dressed as a recommendation.

### Added in pass 267

- **P14 is the pattern this file most needed and did not have.** The single most common North
  American situation — *"the client runs Canvas"* — had no recipe for 266 passes, because
  [`verticals/solutions.md`](../verticals/solutions.md) carried Canvas as closed SaaS. Its source
  is **AGPL-3.0, 78,765 commits**, and the engagement shape is an **MIT doorway**
  (`vishalsachdev/canvas-mcp`) over a platform the client already operates. 🔵 **The general rule
  this suggests:** before writing a pattern that routes *around* an incumbent, read the
  incumbent's licence payload. "Commercial" and "closed" are different claims.
- **P15 supersedes nothing but strengthens P10 materially** — five permissive graders plus a
  permissive substrate (`jupyterhub`, BSD-3, 8.4k★) instead of three graders and no substrate.
- **P16 is the only pattern in this file where mandate, platform and licence all line up**, and it
  is deliberately weighted toward teacher enablement because the region supplies a **documented
  failure case** (Korea's withdrawn textbook mandate) rather than only a success story.
- **Still no pattern for:** a North American *public-sector platform* engagement (none exists —
  the NA public-sector code located is a service layer, not a platform), and a LATAM engagement
  outside Brazil on open code (**Uruguay's Ceibal publishes no repositories at all**, verified this
  pass).


## P19 — Delivering an African or Middle Eastern ministry mandate when the regional supply serves no grant *(new in pass 269)*

**The engagement.** A ministry of education — or a development funder working through one — has a
**funded, dated AI mandate** and no licensed software to execute it. Kenya (**10,382** junior
secondary schools under **KDEAP**, **62,000+** teachers ICT-trained), Nigeria (AI + programming +
robotics in secondary curriculum since **September 2025**), Egypt (**UNESCO** national **AI
competency framework for teachers**, **2026-06-03**; **236,000+** general-secondary enrolments from
2025/26), South Africa (**no national policy in force** — the 2026 draft was **abrogated 2026-04-27**
— but **DBE Coding and Robotics for Grades R–9** in development).

**Why this pattern exists and why it is not `P17` or `P16`.** `P16` delivers India's mandate **on
India's own MIT stack** (Sunbird/DIKSHA) — there is a national permissive platform to stand on.
`P17` handles a mandate whose **curriculum** cannot be licensed. **MEA is the harder case: neither
exists.** Pass 269 located the first two African-context education agents in this base and **both
serve no grant** — [`muskvdc/EduTwin-Africa`](https://github.com/muskvdc/EduTwin-Africa)
(South Africa, Grades 8–12, **pre-licence**, placeholder still in the README) and
[`Valexxy/edunaija-os`](https://github.com/Valexxy/edunaija-os) (Nigeria, **no grant on either
channel**). **Nigeria's Naija Teacher AI states no licence; Kenya's Kytabu SOMANASI is
proprietary.** So the stack has to be assembled from permissive software built elsewhere, with the
*local* contribution being curriculum alignment and language — which is exactly what a studio sells.

| layer | component | licence | why this one |
|-------|-----------|---------|--------------|
| Teacher-facing authoring | [`DaRL-GenAI/instructional_agents`](https://github.com/DaRL-GenAI/instructional_agents) | **MIT** | Peer-reviewed (EACL'26) ADDIE pipeline: syllabus → slides → assessments. **The deliverable Egypt's teacher framework implies.** |
| Local-first lesson drafting | [`SirhanMacx/Claw-ED`](https://github.com/SirhanMacx/Claw-ED) | **MIT** | Runs without sending student or curriculum data out of the building — the posture for a ministry pilot. |
| Provenance of generated material | [`JuneYaooo/lineage-skill`](https://github.com/JuneYaooo/lineage-skill) | **Apache-2.0** | Generated material stays tied to its source. A ministry asks *"where did this come from"* before it asks anything else. |
| Offline delivery | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** | Connectivity is the binding constraint in every one of the four countries. `P9` is the offline half. |
| Offline assessment at national scale | [`Tangerine-Community/Tangerine`](https://github.com/Tangerine-Community/Tangerine) | GPL-3.0 ⚠️ | README claims **5M+ assessments across 65 countries** — the only regionally-proven assessment option. **Copyleft: keep it as a deployed system beside the deliverable, never linked into it.** |
| Lesson-plan structuring precedent | [`AI-for-Education/lesson-plan-parse-mbsse`](https://github.com/AI-for-Education/lesson-plan-parse-mbsse) | **MIT** | **Sierra Leone MBSSE national lesson plans → structured JSON**, corpus shipped. The one piece of Africa-engaged permissive code in this base, and a working template for doing the same to a Kenyan or Nigerian curriculum. ⚠️ Research-grade (1–12★), so read it as a method, not a dependency. |
| Tutor layer, if the pilot is student-facing | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | **Apache-2.0** | Default tutoring row; persistent student model. |

**Wiring.**
1. **Attach to the national instrument, and pick the right one per country.** Egypt → the **teacher
   competency framework** (teacher-facing workflow, which is where permissive supply actually
   exists). Kenya → the **KDEAP rollout** (devices and connectivity already funded; the gap is
   content and teacher capability). Nigeria → the **secondary curriculum lines** (Python, JS,
   HTML/CSS are named, so the scope is bounded). **South Africa → enter at INSTITUTION level**, not
   ministry: **NWU has a policy** and USAf keeps a register, while the national policy was withdrawn.
2. **Parse the national curriculum into structure before generating anything**, using
   `lesson-plan-parse-mbsse` as the worked precedent. **This is the step that makes the deliverable
   defensible and the step that cannot be imported** — it is per-country, and it is billable.
3. **Generate with `instructional_agents`, draft locally with `Claw-ED`, and keep lineage with
   `lineage-skill`.** Every one permissive, so the deliverable carries no copyleft.
4. **Ship offline through Kolibri (MIT).** Deploy `Tangerine` **as a system** if national assessment
   is in scope, and keep its GPL-3.0 boundary at the process edge.
5. **Originate the curriculum content; do not ship a found one.** `P17`'s rule applies with a new
   instance: `datawhalechina/ai-edu-for-kids`, the most-adopted primary-band curriculum artefact
   this base has found, is **CC-BY-NC-SA-4.0** (and only in README prose). Read it to establish
   *what a primary AI course must cover*; write the text yourself.

🔴 **Four prices to quote honestly.**
- **There is no MEA market sizing in this base** — no spend figure, no vendor share, no CAGR for any
  of the four countries. **Scope from the programme counts above (schools, teachers, enrolments),
  not from a market number**, because this base does not have one and will say so.
- **Every regional figure here is secondary-source grade.** `p268` established the non-GitHub DNS
  failure as environmental; no ministry document was read. **Make confirmation against the ministry's
  own circular an explicit first-phase task**, not an assumption.
- ⚠️ **Do not name Egypt's delivery platform.** Reporting splits across **QUREO**, the Japanese
  **Kiryo**, and a **Sprix** contract approved January 2026. **Brief the framework, not the vendor.**
- 🔴 **Do not cite the `EduNaija AI Tutor` paper and `Valexxy/edunaija-os` as the same thing.** The
  paper (ACL AfricaNLP 2026, DOI `10.18653/v1/2026.africanlp-main.11`) is a five-agent LangChain +
  FAISS tutor with **English / Yoruba / Hausa / Igbo** support **whose code this base could not
  locate**; the similarly-named repository is an unlicensed starter codebase.

🟢 **The one cheap upstream move.** `EduTwin-Africa`'s README says *"Add the project's chosen license
here before publishing."* **That author knows the grant is missing** — so unlike this base's other
ungranted rows, a licence request there has a plausible answer, and a South African engagement would
start from existing SA-curriculum-aware code rather than from zero. **Ask before you rebuild.**

🟢 **Estimate shape:** **6–8 weeks** for curriculum parsing + teacher-facing generation + offline
delivery against **one** country's instrument, assuming the device and connectivity layer is already
funded (true in Kenya, not assumed elsewhere). **Each additional country is a new curriculum parse
and a new language pass — price it as a new engagement, not a rollout**, because the permissive
layer ports and the national layer does not.

## P20 — The Spanish/LOMLOE teacher-workflow engagement, and how to ship against a ShareAlike curriculum framework *(new in pass 270)*

**Target:** Spain (LOMLOE + CCAA autonomous-community curricula). Transfers to any jurisdiction
whose curriculum publishes **official criteria** a deliverable must demonstrably cover.
**Why now:** the **Sanoma Learning 2026 European Teacher Survey** (>20,000 teachers, 14 countries)
measured **63% of European teachers using AI** and **only 16% believing general-purpose AI improves
learning outcomes** (`T28`). The client already has an AI tool, already has evidence it is not
working, and the reason is that it does not know their curriculum. **This pattern is the answer to
that specific objection, and nothing else on these shelves answers it as directly.**
**Timeline:** 6–8 weeks to a measurable teacher-facing pilot.

```
[OpenDidactia  CC BY-SA 4.0]  <- READ as a specification, NOT shipped as content
  nmarafo/OpenDidactia         OKF: curricular schemas for Programaciones Didacticas
  2,123 B licence payload      and Situaciones de Aprendizaje (LOMLOE / CCAA)
  50 commits / 0 stars         ** NOT runnable code — prompts + schemas **
        |
        |  (the licence boundary lives on THIS arrow — see below)
        v
[instructional_agents  MIT]    multi-agent ADDIE: syllabus -> slides -> assessments
  DaRL-GenAI/instructional_agents    roles: Teaching Faculty / Instructional Designer / TA
        |
        v
[Claw-ED  MIT]                 teacher approves before anything reaches a student;
  SirhanMacx/Claw-ED           
                               local-first, curriculum never leaves the institution
        |
        v
[Numbas  Apache-2.0]           assessment execution ENTIRELY CLIENT-SIDE —
  numbas/Numbas                answers a Spanish data-residency objection structurally
        |
        v
[Moodle  GPL-3.0]              the LMS Spanish public education already runs;
                               keep it at the process edge, integrate over its API
```

🔴 **The licence boundary, which is the whole engineering content of this pattern.**
`OpenDidactia` is **CC BY-SA 4.0** — verified first-hand at `main/LICENSE.md`, 2,123 B, pass 270.
**ShareAlike, and critically NOT NonCommercial**, which makes it *commercially usable* and puts it
in a different category from `datawhalechina/ai-edu-for-kids` (**NC *and* SA**, unusable in a
deliverable at all — `P17`, `p269`). **"CC with a hyphenated suffix" is not a verdict; read which
suffixes.**

What ShareAlike colours here is **adapted content**, not the client's code:
1. 🟢 **Read OpenDidactia's OKF schemas to learn the SHAPE of a LOMLOE programación** — the
   mandatory prior inventory of every official criterion, the 100%-coverage audit line, the
   analytic rubric per instrument. **Shape and method are not copyrightable; the text is.**
2. 🔴 **Do not ship its prompt text, its schemas or an edit of them** inside a proprietary
   deliverable. That is the derivative that triggers SA.
3. 🟢 **Write your own schemas against the official curriculum** — which is the authoritative source
   anyway, and which `OpenDidactia` is itself a reading of. **Then the generated programaciones are
   the client's, under whatever terms the client wants.**
4. 🟢 **If the client is a public body and SA is acceptable** (common in Spanish public education —
   CC BY-SA is the default in much of the sector), **adopt OpenDidactia directly and contribute
   back**. This is the cheaper path and it is available more often than a reflex "no copyleft" rule
   admits. **Ask which one the client wants in week one; do not decide it for them.**

🟡 **What to verify in week one, because this base cannot.**
- 🔴 **`OpenDidactia` is 0 stars at 50 commits, GitHub detects no language, and it is a
  prompt/knowledge framework rather than software.** **There is no community, no release and no
  maintenance signal.** Treat it as **one practitioner's written-down method** — valuable as that,
  and **not** as a dependency. Nothing in the chain above calls it at runtime, by design.
- ⚠️ **CCAA divergence is the real scope risk.** LOMLOE sets the frame; each autonomous community
  publishes its own criteria. **Price one community, then price each additional one as a new
  curriculum parse** — the same rule `P19` applies to additional countries.
- ⚠️ **Every regulatory and market figure behind this pattern is secondary-source grade** and the
  EMEA market number is now a **two-publisher range ($2.1–2.6B, 2026 — `T30`)**, not a point.
  **Quote the range and say it is a range.** Scope from teacher and school counts instead.

🟢 **Why this pattern beats the obvious alternative.** The obvious alternative is Estonia's: buy a
proprietary platform at national scale (`~half of 20,000` upper-secondary students, Minister
**Kristina Kallas** to *Politico*, May 2026). It works, and it is the thing a sovereignty-conscious
European procurement will be asked about afterwards. 🔵 **Every component above except Moodle's
GPL-3.0 edge is MIT or Apache-2.0, and every one of them is EMEA-origin or EMEA-hosted** — which
this base's EMEA section already establishes as the regional differentiator. **The permissive,
regionally-governed stack exists; this pattern is the assembly instructions.**

## P21 — Shipping against a DATED future mandate: the Netherlands `kerndoelen`, 2027-08-01 *(new in pass 271)*

**Target:** Netherlands — `primair onderwijs`, `onderbouw vo` and `(voortgezet) speciaal onderwijs`.
Transfers to any jurisdiction whose AI-literacy duty is **enacted with a named future commencement**
rather than already binding.
**Why now, and why this is a better engagement than the claim it replaces:** pass 270 retracted the
Netherlands as `NOT_ESTABLISHED`; pass 271's Dutch-language leg found the instrument
(`T35`). The **`kerndoelen digitale geletterdheid`** include **`AI-geletterdheid` explicitly**, are
**concept today**, become **legally official on 2027-08-01**, and are **fully introduced with
`Inspectie` oversight in 2031**.
🔵 **A present-tense "market leader" is a market already lost. A dated commencement is a procurement
runway with a deadline on it** — roughly 9 months of buying time before the duty attaches, and a
further inspection horizon that makes evidence-of-coverage the renewable part of the deliverable.
**Timeline:** 10–12 weeks to an inspectable pilot across two bands.

```
[kerndoelen digitale geletterdheid]   <- READ as the specification. A government instrument,
  SLO / OCW, concept (Jul+Nov 2025)      NOT a repo and NOT a licence question.
  official 2027-08-01                    3 domains; practical domain = AI exploration:
  Inspectie oversight from 2031          recognise AI around you / how it works /
        |                                social + ethical consequences
        |  map each kerndoel -> one competency id, ONCE, as data
        v
[competency map: your own artefact]   the deliverable the client actually owns.
  TSV/JSON, no upstream licence         po | onderbouw-vo | (v)so  x  3 domains
        |
        +-------------------------------+
        |                               |
        v                               v
[DeepTutor  Apache-2.0]          [instructional_agents  MIT]
  HKUDS/DeepTutor                  DaRL-GenAI/instructional_agents
  student-facing tutoring,         teacher-facing: syllabus -> slides ->
  bound to the competency id       assessments against the same ids
        |                               |
        +-------------------------------+
        |
        v
[H5P content generated, played through MIT]   <- THE LICENCE BOUNDARY OF THIS PATTERN
  generate interactive items, then play them with
  tunapanda/h5p-standalone  MIT  (1,077 B)
  package with sr258/scorm-h5p-wrapper  MIT  (1,073 B)
  ** NEVER fork h5p/h5p-php-library — GPL-3.0, 35,146 B, master/LICENSE.txt **
        |
        v
[Moodle  GPL-3.0]                the LMS Dutch schools run; integrate over its API and its
  moodle/moodle                    provider-pluggable AI subsystem (4.5+), never by forking
        |
        v
[Koha  GPL-3.0]  (optional, HE/vo+ only)   catalogue as the curated retrieval authority
  Koha-Community/Koha                      librarian-maintained metadata, not scraped text
```

🟢 **Why the competency map is the first deliverable and not the tutor.** The mandate is a
**coverage** obligation inspected from 2031, so what the client must be able to produce is *evidence
that every kerndoel is addressed*, per band. Build that as **data you own** — one row per kerndoel,
mapped to one competency id — and both the student-facing and teacher-facing agents become consumers
of it. 🔵 **This also makes the 2027→2031 gap billable in the right order:** map and pilot before
commencement, then widen coverage and produce inspection evidence after it.

🔴 **The H5P arrow is where this pattern is won or lost.** H5P is already inside most Dutch Moodle
estates, so generating interactive content is the path of least resistance — and the **authoring core
is GPL-3.0 with no permissive alternative** (`ACTION PW`, pass 271). **Generate content, play it
through the MIT runtime, package with the MIT wrapper.** A fork of the authoring core puts the
client's whole content pipeline inside GPL-3.0; the MIT playback path does not.

🟢 **The sovereignty argument is supplied by the ministry itself, which is rare and should be quoted.**
OCW's **Kamerbrief on `digitale autonomie` (2026-07-02)** states that Dutch education is
*"in grote mate afhankelijk van niet-Europese techbedrijven"* — **largely dependent on non-European
tech companies** — while naming responsible AI use as part of public digital provision. Pair it with
`p270`'s Estonia finding (≈half of 20,000 upper-secondary students on an **OpenAI-partnered
proprietary** platform) and the **Sanoma** numbers (**63%** of European teachers using AI, **16%**
believing general-purpose AI improves outcomes — `T28`). 🔵 **Every component above is open source and
curriculum-bindable, which is precisely what the general-purpose assistant cannot be.**

🟡 **What this pattern does NOT claim, stated so a proposal does not overreach:**
- 🔴 **The Netherlands is not a current K-12 AI leader.** That aggregator claim is still unsupported
  (`T33` — it is the same sentence as the `$2.64B` EMEA figure). **No Dutch deployment at Estonia's
  measured scale was located.** Sell the runway, not a race already run.
- 🔴 **The kerndoelen are CONCEPT.** Final wording can still change before 2027-08-01. Build the map
  as data precisely so a wording change is a data migration, not a re-architecture.
- 🟡 **`Gap 367` is not closed by this.** There is still **no permissively licensed primary-band
  AI-literacy curriculum artefact** in any of the four languages searched (`p269`–`p271`). This
  pattern works *because* it treats the government instrument as the specification and keeps the
  generated artefact as the client's own — the same move as `P17` and `P20`, now with a date attached.
- ⚠️ **All Dutch policy datums here are secondary-source grade.** The primary channel
  (`open.overheid.nl`, `rijksoverheid.nl`) is unreachable from this environment — re-tested pass 271,
  both transports. Verify the commencement date against the primary text before contracting on it.

## P22 — The zero-copyleft engagement: a full education stack where procurement excludes GPL/AGPL *(new in pass 272)*

**Target:** US state university systems and public agencies whose procurement or redistribution rules
exclude copyleft — the lane **SUNY's systemwide AI policy across 64 campuses** (new on `market.md` this
pass) and **Utah's statewide vendor deal** both sit in; also EMEA public bodies that must redistribute
derivative work without a network-copyleft obligation.
**Timeline:** 10–14 weeks to a production pilot.

**Why this pattern exists.** Every default answer in education is copyleft: **Moodle GPL-3.0**,
**Open edX AGPL-3.0**, **Canvas AGPL-3.0**, **OpenEduCat LGPL-3.0**, **Koha GPL-3.0**, **H5P GPL-3.0**.
When a client's procurement excludes copyleft, the usual advice is "use the API and don't fork" — which is
a constraint, not a stack. 🟢 **Pass 272 established there is a complete, genuinely permissive path**, every
component read at payload this pass and **rider-cleared**, not merely licence-labelled.

```
                     ALL COMPONENTS Apache-2.0 / MIT — NO copyleft anywhere in the tree
                     every grant read at payload on 2026-10-17 (see evidence TSV)

  [OpenOLAT          Apache-2.0  10,982 B]   LMS of record: courses, enrolment, assessment, groups
         |                                    rider-cleared: terms section byte-identical to upstream
         |  LTI 1.3
  [tsugi             Apache-2.0  10,273 B]   the sanctioned tool-integration boundary — your agent
         |                                    ships as an LTI tool, so core is NEVER forked
         +---> [Numbas        Apache-2.0  11,357 B]  randomised maths/science assessment, SCORM out
         +---> [Autolab       Apache-2.0  11,324 B]  autograding with per-submission containers
         +---> [scorm-again   MIT          1,072 B]  runtime for the client's existing SCORM estate
         |
  [xAPI-Spec         Apache-2.0  11,525 B]   the telemetry vocabulary
         |
  [lrsql             Apache-2.0  11,357 B]   Learning Record Store — SQL-backed, self-hosted
         |                                    every learner event lands here, on the client's infra
         +---> [pykt-toolkit  MIT          1,066 B]  learner model / knowledge tracing over the LRS
         |
  [academico         MIT          1,094 B]   SIS: enrolment, attendance, results
         |                                    (byte column filled in by p272; vendor page said
         |                                     "licence not named" — the payload says MIT)
         |
  [DeepTutor         Apache-2.0  11,408 B]   the tutor agent, pointed at a self-hosted model
```

### Wiring

1. **Stand up `OpenOLAT`** as the LMS of record. Java/Spring; it behaves like an institutional LMS
   (that is the reason to pick it over Oppia or Kolibri, which are not institutional).
2. **Put every agent behind `tsugi` as an LTI 1.3 tool.** This is the architectural commitment that makes
   the pattern hold: the agent is a *tool*, never a patch. A client can swap `OpenOLAT` for Moodle later
   without touching your code — and if they do, **the copyleft stays on their side of the LTI boundary.**
3. **Emit `xAPI` statements for every learner interaction into `lrsql`.** Do this from day one. The LRS
   is what makes the engagement extensible rather than a one-off tutor, and it is the client's data on
   the client's infrastructure.
4. **Train the learner model with `pykt-toolkit` against the LRS**, not against the LMS database. The
   model then survives a platform migration.
5. **`DeepTutor` as the tutor surface**, pointed at a self-hosted model. ⚠️ Apache-2.0 covers the
   *code*; it says nothing about the *weights* you point it at — that is a separate licence question and
   the one most likely to be missed in a procurement review.
6. **`academico` for SIS data** feeding dropout-risk work; `Numbas`/`Autolab` for assessment;
   `scorm-again` to keep the client's existing SCORM content playable.

### The licence boundary — the point of the pattern

🟢 **There isn't one inside the stack.** Apache-2.0 and MIT both permit proprietary derivative work with
attribution, so **the client's own code can sit anywhere in this tree**, including inside a fork of any
component. Apache-2.0 additionally carries an **express patent grant**, which is usually what a
public-sector legal review is actually asking about.

⚠️ **Three things still to get in writing:**
- **Model weights are not covered** by any grant above (step 5).
- **`xAPI-Spec` is a specification**, Apache-2.0 — implementing it is unencumbered, but conformance
  claims and the ADL trademark are not the same thing.
- **If the client insists on Moodle or Canvas** after all, the pattern degrades gracefully *only* through
  the LTI boundary in step 2. Keep it even if you think you won't need it.

### What this pattern is NOT

🔴 **It is not an ERP.** **No education ERP under MIT or Apache-2.0 has been located**, tested from two
independent channels (`p271`, `p272`). If the engagement needs admissions/fees/library as one system,
`OpenEduCat` is **LGPL-3.0** and that is a different conversation. 🔴 **And it is not a reason to quote a
market size** — see `T36`: the regional AI-in-education figures all trace to one publisher, and LATAM's
span roughly 6×. Size this engagement from the **adoption** datums on `intel/market.md`, not the forecasts.

## P23 — An agent inside the Moodle the client already runs, without the AGPL and without forking

*(new in pass 273)*

**When to reach for it.** The client runs **Moodle** — the default LMS of public education worldwide —
and wants an agent that does real work in it: publishing lesson content, building quizzes, enrolling
cohorts, reading the gradebook. `P14` is the same shape for Canvas. **This is its Moodle counterpart, and
until pass 273 this KB could not offer one without an AGPL-3.0 open-core dependency.**

### The stack

| layer | component | licence | why this one |
|---|---|---|---|
| LMS (incumbent) | [`moodle/moodle`](https://github.com/moodle/moodle) | GPL-3.0 | Already installed. **You are not forking it** |
| Agent doorway — **writes** | [`MarcosNahuel/moodle-mcp`](https://github.com/MarcosNahuel/moodle-mcp) | **MIT** *(payload, 1,065 B)* | 40 facades + `ws_raw`, upsert-by-`idnumber`, any Moodle 4.x/5.x with Web Services on |
| WS surface for writes | `local_italiciamcp` *(ships in `plugin-companion/`)* | covered by the root MIT; **no grant of its own** | Supplies the `type=write` WS functions Moodle core does not expose |
| Agent doorway — **student side** | [`Jawadh-Salih/moodle-mcp-server`](https://github.com/Jawadh-Salih/moodle-mcp-server) | **MIT** *(payload, 1,063 B)* | Go; grades, deadlines, notifications, `submit_assignment` |
| Tutor behaviour | [`ls1intum/Pyris`](https://github.com/ls1intum/Pyris) | MIT | Swappable LLM pipelines, RAG over instructor material. Pedagogically constrained by design |
| Assessment that never leaves the device | [`numbas/Numbas`](https://github.com/numbas/Numbas) | Apache-2.0 | Browser-executed marking — answers a residency objection structurally |
| Integrity | [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | MIT | Source-code plagiarism detection |

### How to wire it

1. **Enable Moodle Web Services** and mint a token scoped to a dedicated service account — *not* a
   teacher's account. The capability the write functions demand is `moodle/course:manageactivities`; grant
   that and nothing wider.
2. **Install `local_italiciamcp`** as a *Complemento local* and expose only the WS functions you intend to
   use. 🔵 **Enumerate them explicitly** — `db/services.php` declares write functions including
   `upsert_page`, `upsert_quiz`, `update_course_summary` and **`delete_module_by_idnumber`**. A deletion
   endpoint does not belong in a pilot's token.
3. **Run the wrapper over stdio** against your MCP client. Start with the **read-only facades**
   (`listar_alumnos`, `obtener_calificaciones`, `obtener_info_sitio`) and `ws_raw`, which work **without**
   the plugin at all — so phase 1 of the engagement needs no Moodle code installed and no licence
   conversation.
4. **Put a confirmation gate in front of every write.** 🔴 **Non-optional, and it is this base's own
   finding, not a precaution:** `T4` records that this wrapper's writes execute **with no confirmation and
   no disclosure**. Wrap `calificar_manualmente`, `matricular_csv`, `reset_password` and
   `delete_module_by_idnumber` in a human-approval step before a pilot touches a live course. **A grade
   written by an unattended agent is an EU AI Act Annex III problem, not a UX problem.**
5. **Lean on `upsert`-by-`idnumber`.** Every write is idempotent on a stable key, so the content pipeline
   can be re-run from source. **That is what makes the agent output reviewable** — regenerate, diff,
   re-publish.
6. **Keep the tutor out of the LMS.** Pyris behind the agent, Numbas for marking. Moodle stays the system
   of record; nothing pedagogical is forked into it.

### The licence boundary, stated once and precisely

🟢 **The wrapper is MIT and stays MIT** — it links nothing, it speaks REST.
🔵 **The deployed combination (Moodle + the `local_` plugin) is a GPL-3.0 work.** Hosting it for the
client triggers **nothing**, because GPL-3.0 has **no network clause**. Handing the client a *distributed*
image containing the plugin ships that image under **GPL-3.0**.
🟢 **Against the alternative this KB used to offer** —
[`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server), **AGPL-3.0 *and*
open-core — this is strictly cheaper on both axes**: no network clause, and no tools held behind a paid
tier. See `T41`.

⚠️ **What you are buying, honestly.** `1★ / 1 fork / 59 commits`, and a *burst-and-silence* release
pattern (`CHANGELOG` last moves `2026-05-03`). **Treat it as a reference implementation you adopt and
maintain, not as an upstream that will maintain itself.** The 40-facade surface and the `idnumber` upsert
discipline are the valuable parts, and they are worth more than the maintenance risk precisely because
you can read all of it.

**Rough shape:** 4-6 weeks to a governed pilot on one faculty — week 1 read-only against a Moodle staging
clone with no plugin installed, weeks 2-3 plugin plus gated writes on a single course, weeks 4-6
content-pipeline regeneration and the Annex III human-review record.
