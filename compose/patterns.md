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
