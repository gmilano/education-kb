---
industry: education
region: Global
updated: 2026-10-21
---

# Education — composition patterns

**Pass 360 · 2026-10-21.** Concrete recipes. Each names the specific repos, the licence
boundary that makes the composition safe, and what the engagement actually delivers.
Every repo referenced is verified live with its grant read from payload on
**2026-10-21** — see `agents/top.md` and `repos/foundations.md`.

**The rule that governs all of these.** Most education platforms are GPL or AGPL.
Reaching them **over a protocol boundary** — LTI 1.3, web services, or MCP — keeps a
client's proprietary work on its own side of the licence. Forking them does not.
Every pattern below is built on a boundary, deliberately.

---

## Pattern 1 — LMS-native tutor without touching the LMS

**Problem.** A university runs Canvas or Moodle. They want an AI tutor grounded in
their actual courses. They cannot accept AGPL obligations on their own code, and IT
will not approve a fork.

**Recipe.**
1. **Reach the LMS over MCP**, not code: [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (MIT) for Canvas, [`falkenslab/moodle-mcp`](https://github.com/falkenslab/moodle-mcp) (MIT) for Moodle, [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) (MIT) for Open edX.
2. **Tutoring logic** from [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) (MIT) — Bayesian Knowledge Tracing gives defensible mastery estimates instead of vibes.
3. **Pedagogical behaviour** loaded as skills from [`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills) (Apache-2.0) or [`learning-commons-org/agent-skills`](https://github.com/learning-commons-org/agent-skills) (Apache-2.0).
4. **Surface it in the LMS** as an LTI 1.3 tool via [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (Apache-2.0, Node) or [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (MIT, Python). On Canvas specifically, [`harvard-edtech/caccl`](https://github.com/harvard-edtech/caccl) (MIT) removes most of the boilerplate.
5. **Quality-gate the output** with [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) (MIT code).

🟢 **Licence boundary:** every component is MIT or Apache-2.0. The AGPL platform is
reached over MCP and LTI, so its copyleft never touches client code.

---

## Pattern 2 — BNCC-aligned lesson planner for Brazil

**Problem.** A Brazilian ministry, network or EdTech needs lesson planning provably
aligned to the national BNCC curriculum. Generic AI output cannot be defended to a
regulator or a school board.

**Recipe.**
1. **Ground in official standards:** [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) (MIT) — **1 721 BNCC learning objectives** as JSON/SQLite/CSV. Load it as the retrieval corpus so every generated plan cites a real objective code.
2. **Generate the courseware** with [`satvik314/educhain`](https://github.com/satvik314/educhain) (MIT) for course structure, or [`SYuan03/Skill-Anything`](https://github.com/SYuan03/Skill-Anything) (MIT) to turn existing material into quizzes and flashcards.
3. **Render as interactive content** teachers can still edit: [`h5p/h5p-cli`](https://github.com/h5p/h5p-cli) (**MIT** — note the core library is GPL-3.0, the CLI is not) or [`openpatch/hyperbook`](https://github.com/openpatch/hyperbook) (MIT).
4. **Deliver into the school's system:** [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) (GPL-2.0) for K-12 SIS, or [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) (GPL-3.0) — both with mature Portuguese/Spanish localisation. Integrate over web services to keep the boundary.
5. **Pull supporting public data** via [`Mcp-Brasil/mcp-brasil`](https://github.com/Mcp-Brasil/mcp-brasil) (MIT).

🟢 **Why this is defensible:** the alignment claim is checkable against a public MIT
dataset, objective by objective. 🔴 **And why it does not yet port:** no equivalent
open dataset exists for Mexico's SEP, Colombia's or Argentina's standards. Building
one is the regional asset play — see `intel/market.md` → LATAM.

---

## Pattern 3 — EU AI Act high-risk conformity wrapper

**Problem.** A European institution uses AI in admissions or assessment. That is a
**high-risk** system under EU AI Act **Annex III point 3**, and the obligations — risk
management, data governance, logging, human oversight — bind from **2 December 2027**,
postponed from 2 August 2026 by the Digital Omnibus (**Regulation (EU) 2026/1744**, in
force 27 July 2026). Their current tooling has none of it.

🔵 **Scope the engagement on the real date.** Telling this client they are bound *now*
is wrong by sixteen months and in the expensive direction. What binds them today is the
**prohibitions**, the **AI-literacy duty** and **Article 50 transparency**. The
high-risk work is a **readiness programme with a fixed, non-extendable deadline** — a
better engagement than emergency remediation, and an honest one.

**Recipe.**
1. **Instrument every decision.** Wrap the model call so each inference writes an
   immutable record: inputs, model version, output, the human who reviewed it. Emit
   it on the **Caliper** event vocabulary — implement [`1EdTech/caliper-spec`](https://github.com/1EdTech/caliper-spec) 🔴 (an **IMS specification licence**: implement the standard, do not vendor the document).
2. **Force human oversight structurally**, not by policy: the agent proposes, a named
   human disposes, and the gate is in the data model. [`byerlikaya/Septum`](https://github.com/byerlikaya/Septum) (MIT) is a working reference for the approval-gate shape — local PII detection → approval → de-anonymisation.
3. **Evidence of efficacy and non-discrimination:** run the model as a randomised
   experiment inside the LMS with [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta) (Apache-2.0). This produces the outcome data the Act's risk-management file needs, and the efficacy proof procurement now demands (see `intel/trends.md` §2).
4. **Accessibility obligations in the same pass:** [`ucfopen/UDOIT`](https://github.com/ucfopen/UDOIT) (GPL-3.0) inspects course content; have the agent generate remediations rather than only flagging.
5. **Host on a permissive platform** so the conformity layer can be a closed
   deliverable: [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) (**Apache-2.0**) is the only full HE platform where this is clean.

🟢 **This is the strongest opportunity in the KB.** Obligations are live, and a survey
of 450+ institutions put formal AI guidelines at ~10 %.

---

## Pattern 4 — Assessment integrity for the agent era

**Problem.** Students submit agent-assisted work. Detection-by-vibes is both unfair
and indefensible, and most "AI detectors" do not survive scrutiny.

**Recipe.**
1. **Measure similarity, not "AI-ness":** [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) (MIT, Ghent University) does structural source-code plagiarism detection. It makes a claim you can show a student.
2. **Execute submissions safely:** [`judge0/judge0`](https://github.com/judge0/judge0) (GPL-3.0) sandboxes 60+ languages — consume it **as a service over its API** so the GPL boundary holds.
3. **Grade deterministically:** [`ls1intum/Ares2`](https://github.com/ls1intum/Ares2) (MIT, TU Munich) for secure test execution, or [`INGInious/INGInious`](https://github.com/INGInious/INGInious) (AGPL-3.0, 🟡 *"most of the files"* — mixed grant, diligence it) as a full assessment platform.
4. **Shift the assessment design itself.** Pair the above with process evidence —
   version history, in-editor telemetry from [`SJRiz/pytogether`](https://github.com/SJRiz/pytogether) (MIT) — so the artefact is no longer the only evidence.
5. **Model the mastery signal:** [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) (MIT) and [`ZhijieXiong/pyedmine`](https://github.com/ZhijieXiong/pyedmine) (MIT) for knowledge tracing over the resulting data.

🔵 **Position it honestly:** this detects *similarity and process anomalies*, not
authorship. Say so to the client; the alternative is a product that fails its first
appeal.

---

## Pattern 5 — Offline-first delivery for low-connectivity regions

**Problem.** Rural LATAM, Sub-Saharan Africa, remote APAC. Intermittent or no
connectivity, shared low-end devices, and no frontier-model budget per learner.

**Recipe.**
1. **Platform:** [`learningequality/kolibri`](https://github.com/learningequality/kolibri) (**MIT**) — purpose-built offline-first, syncs when a link appears. MIT means the deployment can be a closed, branded client deliverable.
2. **Precompute, do not infer live.** Generate the full adaptive content tree
   server-side with [`satvik314/educhain`](https://github.com/satvik314/educhain) (MIT) or [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) (MIT), then ship it as a Kolibri channel. Inference cost becomes a one-time build cost.
3. **Local mastery model:** [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) (MIT) — BKT runs on-device with no network call.
4. **Spaced repetition instead of generation:** [`HumphreySun98/Smart-Study-Agent`](https://github.com/HumphreySun98/Smart-Study-Agent) (MIT) pairs RL action-selection with FSRS scheduling; [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) (MIT) where Anki is already in use.
5. **Literacy-specific base:** [`elimu-ai/webapp`](https://github.com/elimu-ai/webapp) (MIT) for early-grade literacy in African deployments.
6. **Mobile client:** fork [`moodlehq/moodleapp`](https://github.com/moodlehq/moodleapp) (**Apache-2.0** — permissive, unlike Moodle core) for a branded learner app.

🟢 **Every component is MIT or Apache-2.0.** This whole pattern can ship as a closed
deliverable, which matters for ministry and NGO procurement.

---

## Pattern 6 — Modernising a legacy SCORM corporate estate

**Problem.** An enterprise has thousands of hours of SCORM content, an LMS that
serves it, and no appetite to re-author any of it. They want AI on top.

**Recipe.**
1. **Keep the content, wrap the runtime:** [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) (MIT) is a modern SCORM 1.2/2004 JS runtime. It replaces the player, not the courseware, and its MIT grant lets you instrument it freely.
2. **Harvest the signal.** The SCORM runtime already emits completion, score and
   interaction data. Route it to a learning-record store on the **xAPI/Caliper**
   vocabulary — this is where the AI gets its training and personalisation signal,
   and it costs nothing to collect.
3. **Layer an agent over the catalogue:** [`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill) (MIT) is the closest working pattern for turning static documents into agent-loadable skills; apply the same shape to course PDFs and manuals.
4. **Fill gaps rather than rebuild:** generate only the missing modules with [`assafkip/claudemy`](https://github.com/assafkip/claudemy) (MIT) or [`sitor-ai/frametell`](https://github.com/sitor-ai/frametell) (AGPL-3.0 — 🔴 keep it a separate service if the client needs closed code).
5. **Corporate-academy platform** where a new one is needed: [`classroomio/classroomio`](https://github.com/classroomio/classroomio) (AGPL-3.0) or [`frappe/lms`](https://github.com/frappe/lms) (AGPL-3.0) — both copyleft, so run them as deployed services, not embedded code.

---

## Pattern 7 — Curriculum knowledge graph from raw textbooks

**Problem.** A client has textbooks and syllabi but no machine-readable curriculum
model, so nothing can be sequenced, diagnosed or aligned.

**Recipe.**
1. **Extraction pipeline:** [`clownjee/knowledge-import-pipeline`](https://github.com/clownjee/knowledge-import-pipeline) (Apache-2.0) does exactly this — PDF parsing → concept extraction → vector retrieval → prerequisite-edge construction → **MCP query service**. It is the only verified end-to-end implementation of this shape.
2. **Skeleton to align against:** [`withmarbleapp/os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) (ODbL-1.0 — 🟡 share-alike binds a derivative *database*, not a produced work) or [`aclascollege/polymath`](https://github.com/aclascollege/polymath) (ODbL-1.0 + CC-BY-SA-4.0) for disciplines, courses, prerequisites, skills and careers.
3. 🔴 **Do not seed from [`cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy)** despite it being the best Chinese K-12 graph available (1 244 nodes, 5 123 items). It is **CC-BY-NC-4.0** and cannot be used in paid work. Use it to validate your own graph's shape, never as an ingredient.
4. **Serve it to agents over MCP** so the graph is a boundary-crossing asset reusable
   by every downstream tutor, planner and diagnostic.
5. **Diagnose against it:** [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) (MIT) for knowledge tracing over the prerequisite structure.

🟢 **Why this is the durable play.** Agents are commoditising fast; the curriculum
graph underneath them is proprietary, defensible and compounding. See
`intel/trends.md` §9.

---

## Pattern 8 — Verifiable credentials for skills-based hiring

**Problem.** A client wants to issue credentials employers can verify without calling
the registrar, and tie them to demonstrated skills rather than seat time.

**Recipe.**
1. **Wallet and issuance:** [`openwallet-foundation-labs/learner-credential-wallet`](https://github.com/openwallet-foundation-labs/learner-credential-wallet) (MIT, OpenWallet Foundation) — the open reference implementation for verifiable learner credentials.
2. **Skills vocabulary to issue against:** [`withmarbleapp/os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) (ODbL-1.0) maps skills to careers, which is what makes a credential legible to an employer.
3. **Evidence behind each claim:** assessment results from Pattern 4, carried as
   Caliper/xAPI records so a credential points at verifiable evidence rather than a
   grade letter.
4. **Issue from the LMS** over LTI via [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) (Apache-2.0) or [`openfun/marsha`](https://github.com/openfun/marsha) (MIT).

🔵 1EdTech names credentials a core 2026 mechanism for skills-based learning and
hiring; this is the open stack for it.

## 🆕 Pattern 9 — A licence-clean programming-assessment stack for a coding academy

**Client shape.** A bootcamp, CS department, certification body or developer academy
that must run untrusted student code, grade it, detect copied submissions and report
results into an LMS the client already owns — and the deliverable has to ship inside a
closed engagement.

**Why this pattern did not exist one pass ago.** The only execution component this base
carried was `judge0` (GPL-3.0), so every version of this build had a copyleft component
at its centre. `p356`'s function legs found a **larger MIT alternative**.

**The stack, every grant read from the payload on 2026-10-21:**

1. **Execution and verdicts** — [`QingdaoU/OnlineJudge`](https://github.com/QingdaoU/OnlineJudge)
   (🟢 **MIT**, `master/LICENSE`, 6 552 ★). A complete judge: submissions, problem bank,
   contests, admin, Docker deployment. **Fork it and brand it** — the MIT grant reaches
   nothing.
2. **The sandbox underneath it** — [`QingdaoU/Judger`](https://github.com/QingdaoU/Judger)
   (🟢 **MIT**, 🔴 branch **`newnew`**, 496 ★). seccomp-based. Already wired into the row
   above; named separately because if the client has their own platform, **this is the
   only piece they need**.
3. **Notebook and data-science courses** — [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader)
   (🟢 **BSD-3-Clause**, 161 ★, UC Berkeley) for **Python *and* R** notebooks, behind
   [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) (BSD-3-Clause) with
   [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator)
   (BSD-3-Clause) for LMS single sign-on.
4. **Integrity** — [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos)
   (🟢 **MIT**, 353 ★, Ghent University) for source-code plagiarism. 🔵 **Choose this over
   proctoring:** of the five proctoring rows verified this pass, one has no grant, one has
   no identified licensor and two are AGPL plugins to AGPL hosts. Detect what the
   submission *is* rather than surveil the student.
5. **Rubric-bound human-in-the-loop grading** — [`erictrainnlpinxihu/Grader-agent`](https://github.com/erictrainnlpinxihu/Grader-agent)
   (🟢 **MIT**, 101 ★) for the written parts. Its four write actions are **absent from the
   tool table**, so the agent can only emit proposals, and every `GradingDraft` binds to a
   rubric line and a paragraph hash. That is a **structural** approval boundary, which is
   what the EU AI Act's high-risk regime wants for exam scoring (`intel/market.md`, EMEA).
6. **Report back into the client's LMS** — an **LTI 1.3 tool** with
   [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (Apache-2.0) or
   [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (MIT). Never a
   fork of Canvas or Open edX — both are AGPL.

🟢 **Every component is MIT, BSD-3-Clause or Apache-2.0.** The whole stack can ship
inside a closed client deliverable with no copyleft reach — which was not true of this
capability before this pass.

🟡 **When to pick the copyleft alternatives instead.** If the client will host it
themselves and publish nothing of their own, [`hydro-dev/Hydro`](https://github.com/hydro-dev/Hydro)
(AGPL-3.0, 7 137 ★) is better engineering for many courses at once, and
[`mjnaderi/Sharif-Judge`](https://github.com/mjnaderi/Sharif-Judge) (AGPL-3.0, branch
`Version-1`) is the only row actually built for **courses** — assignments, deadlines,
per-student feedback — rather than contests. Both stay the **client's** deployment, not
the studio's product.

🔴 **The two branch traps in this pattern, named because they will bite.**
`QingdaoU/Judger` defaults to **`newnew`** and `Sharif-Judge` to **`Version-1`**. A CI
licence check or a vendoring script that assumes `main` or `master` will report the MIT
sandbox at the centre of this stack as **unlicensed**.

## 🆕 Pattern 10 — Add retention to a tutor that already works

**Client shape.** A client already has a tutor, courseware or study app that generates
good material and cannot show that anyone **remembers** it. Procurement is starting to
ask for evidence of learning rather than evidence of output (`intel/trends.md` §2), and
"the model explained it well" is not an answer.

**The insight.** Every tutoring agent on `agents/top.md` decides *what* to teach next.
Almost none decides *when to come back to it* — and scheduling, not generation, is what
moves retention. The sector has a standard for this, it is small, and it is MIT.

**The stack:**

1. **The scheduler** — [`open-spaced-repetition/py-fsrs`](https://github.com/open-spaced-repetition/py-fsrs)
   (🟢 **MIT**, 514 ★). A few hundred lines; takes a review outcome and returns the next
   due date. Drop it beside the existing content pipeline without touching it.
2. **The algorithm, to justify it to the client** — [`free-spaced-repetition-scheduler`](https://github.com/open-spaced-repetition/free-spaced-repetition-scheduler)
   (🟢 **MIT**, 729 ★) is the published DSR-model specification, so the scheduling
   decisions are **explainable to a procurement committee** rather than opaque.
3. **Verification, not self-report** — [`nagisanzenin/engram`](https://github.com/nagisanzenin/engram)
   (🟢 **MIT**, 1 458 ★) does free-recall checking *with receipts*: the learner is
   measured recalling, and the evidence is kept. This is the row that produces the
   artefact an evidence-based procurement wants.
4. **Reach the learner where their cards already are** — [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server)
   (🟢 **MIT**) over MCP, or [`kitschpatrol/yanki`](https://github.com/kitschpatrol/yanki)
   (🟡 MIT, declared only in `package.json`) to push markdown into Anki. 🔵 Anki has the
   installed base; do not rebuild it.
5. **Instrument the claim** — [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta)
   (Apache-2.0) runs the A/B inside the client's LMS: same content, scheduled versus
   unscheduled, retention measured. **That comparison is the deliverable**, not the
   scheduler.

🟢 **Licence reach: none.** Every component is MIT or Apache-2.0.

🟡 **Two rows to leave out, and why.** [`trane-project/trane`](https://github.com/trane-project/trane)
(848 ★) and [`echo-loop/Echo-Loop`](https://github.com/echo-loop/Echo-Loop) (4 222 ★) are
the most interesting designs in this tier — a mastery dependency graph and a full
listening/speaking trainer — and **both are AGPL-3.0**. Study them; do not embed them in
a hosted client deliverable.

---

## 🆕 Pattern 11 — An England-curriculum tutor whose curriculum model stays the client's

**Problem.** A UK education client — an academy trust, a tutoring provider, a publisher —
wants a tutor aligned to the **National Curriculum for England**, and wants the enriched
curriculum model it builds (their sequencing, their question mappings, their mastery
thresholds) to remain **their closed asset**. 🔴 Pattern 7 cannot deliver this: it starts
from [`os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy), whose **ODbL-1.0**
share-alike reaches a *derivative database* — exactly what the client's enriched model
is.

**Why this pattern exists now.** `p357` verified
[`oaknational/oak-curriculum-ontology`](https://github.com/oaknational/oak-curriculum-ontology):
the Oak National Academy curriculum as **OWL/SKOS**, aligned to the National Curriculum
for England, with `ontology/`, `data/` and `docs/` under **OGL-3.0** and `scripts/` plus
workflows under **MIT**, both read at `main/LICENSE.md`. 🟢 **OGL-3.0 permits commercial
exploitation on attribution alone and imposes no share-alike.** That single difference is
what makes this pattern possible and Pattern 7 unsuitable.

**Recipe.**
1. **Curriculum spine:** the `ontology/` and `data/` trees of
   [`oaknational/oak-curriculum-ontology`](https://github.com/oaknational/oak-curriculum-ontology)
   (OGL-3.0). Load the OWL/SKOS directly; its CI already validates the ontology and
   generates distribution files, so the client inherits a tested artefact rather than a
   parse job.
2. **Typed prerequisite reasoning over it:**
   [`devissaputra/curriculum_knowledge_graph`](https://github.com/devissaputra/curriculum_knowledge_graph)
   (**MIT**). It gives `PREREQUISITE_OF`, `TEACHES`, `ASSESSES` and `ALIGNS_WITH` with
   entity-type constraints enforced per relation — so "this lesson assesses an objective
   it never taught" is a **constraint violation**, not a review opinion. Its alignment
   diagnostics and provenance are what an inspection conversation needs.
3. **Mastery estimates:** [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) (MIT) —
   Bayesian Knowledge Tracing, so progression claims are defensible.
4. **Scheduling:** [`open-spaced-repetition/py-fsrs`](https://github.com/open-spaced-repetition/py-fsrs)
   (MIT) for review timing, as in Pattern 10.
5. **Reach the LMS over a boundary**, per Pattern 1: Moodle via
   [`falkenslab/moodle-mcp`](https://github.com/falkenslab/moodle-mcp) or
   [`G36maid/moodle-mcp`](https://github.com/G36maid/moodle-mcp) (both **MIT**), Canvas
   via [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) or
   [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) (both **MIT**).

**The licence boundary.** 🟢 **Every component is MIT except the curriculum data, which
is OGL-3.0 with no share-alike.** The client's enriched graph is theirs; the only
obligation that travels is one attribution string:

> *"Contains public sector information licensed under the Open Government Licence v3.0."*

🔴 **Two constraints to put in the statement of work, not discover later.** The ontology
covers **England** — not Scotland, Wales, Northern Ireland or any EU curriculum — and it
is **`v0.1.3`, early release**, so pin a commit and expect schema movement. 🟡 Neither is
a reason not to build; both are reasons to scope and version deliberately.

**Delivers.** A curriculum-aligned tutor whose alignment is *checkable against a
statutory curriculum* rather than asserted, and whose curriculum model is a closed
client asset. 🔵 Alignment-to-standard is what §2's evidence gate actually asks for in a
UK procurement.

## 🆕 Pattern 12 — Process-evidence assessment, for when the client's detector stops being accepted

**Problem.** A university or faculty has been running AI-detection scores in
academic-misconduct cases, and that has stopped working. `intel/trends.md` §16: Yale,
Cornell and UW–Madison now **discourage or bar detection scores** in misconduct
proceedings, after a Stanford study found detectors flagged **61 % of essays by
non-native English speakers** as machine-written. 🔴 **A better detector does not fix
this** — the failure is an equity failure across language backgrounds, not a model-quality
one — so the engagement is a **replacement**, not an upgrade.

**What replaces it.** The sources name the substitution: oral examination, proctored
assessment, and **grading the writing process**. Only the third is a software build, and
it is a **telemetry** build.

**Recipe.**
1. **Instrument the process, not the artefact.** Draft history, revision sequence,
   time-on-task and paste events are learning-analytics events. Emit them as **Caliper**
   events against [`1EdTech/caliper-spec`](https://github.com/1EdTech/caliper-spec).
   🔴 **Implement the standard; do not vendor the document** — its grant is an IMS
   *specification document* licence, not a software grant (`agents/top.md`, licence
   flags).
2. **Carry the events over an LTI boundary**, so nothing forks the AGPL LMS:
   [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (Apache-2.0) for Node or
   [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (MIT) for
   Python. Both carry the **role claims** that decide who may see a process trace — and
   a process trace is more intrusive than a grade, so that boundary is a privacy control,
   not plumbing.
3. **Keep supervision and similarity, which §16 does *not* retire.**
   [`openedx/edx-proctoring`](https://github.com/openedx/edx-proctoring) or
   [`eLearning-BS23/moodle-quizaccess_proctoring`](https://github.com/eLearning-BS23/moodle-quizaccess_proctoring)
   for supervised assessment; [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos)
   (**MIT**) for code similarity. 🟢 **Neither claims to know what produced the text**,
   which is exactly why both survive the reversal.
4. **Evidence it, because evidence is the procurement gate.**
   [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta)
   (Apache-2.0) runs a randomised comparison **inside** the LMS: process-evidenced
   assessment against the status quo, on the client's own cohort.
5. **If marking is automated anywhere in this, apply §17's three rules:** blind the
   human reviewer to AI provenance on the first pass (a labelled grade **anchors** the
   reviewer — measured across 1 339 teachers), build the **student opt-out as a routing
   path** the LTI role claims can actually serve, and keep the **rubric** as the artefact
   of record.

**The licence boundary.** Apache-2.0 and MIT throughout; the LMS is reached over LTI 1.3
and never forked. 🟢 Nothing in this pattern obliges the client to open anything.

**Delivers.** An assessment-integrity posture that survives the objection that killed
the detector — defensible across language backgrounds, with the evidence to prove it on
the client's own students. 🔵 **And it is a budget conversation the client is already
having:** the money is currently committed to a detection line item that their own
academic board is moving away from.

## 🆕 Pattern 13 — A statutory inclusion deliverable for a Colombian school system

🔵 **The shape that makes this different from every other pattern on this file:** it is
not a capability a client might want, it is **a document Colombian law obliges a school
to produce.** `Decreto 1421 de 2017` makes the **PIAR** — *Plan Individual de Ajustes
Razonables* — mandatory for educational provision to students with disabilities, and
`Ley 2216 de 2022` extends inclusive-education duties to specific learning disorders
(dyslexia, ADHD, dyscalculia). The budget line is **CONPES 4144**, Colombia's national AI
policy, funded to 2030.

**Components**

| Role | Repo | Licence | Why this one |
|---|---|---|---|
| PIAR system of record | [`Dramoscuello/openpiar`](https://github.com/Dramoscuello/openpiar) | 🔴 **AGPL-3.0** | Already models the PIAR workflow and emits the documents the decree requires. Its AI assistant proposes DUA adjustments from the student profile, the institution's PEI, the subject and teacher-declared barriers |
| Tutoring layer | [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) | 🟢 **MIT** | Autonomous tutor agent already running **inside Open edX** against real courses at Universidad Tecnológica de Pereira. TTS replies, animated avatar, teacher statistics panel, context persisted across sessions |
| Host platform | [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) + [`overhangio/tutor`](https://github.com/overhangio/tutor) | 🔴 AGPL-3.0 | `TutorIA` is built for it, so the integration is proven rather than designed |
| Offline assessment | [`Riskbreaker2077/open-test`](https://github.com/Riskbreaker2077/open-test) | 🟢 **MIT** | Local server, school intranet, **every student a different paper**. No connectivity required |
| Oversight record | [`Yuanpeng-Li/gradescope-mcp`](https://github.com/Yuanpeng-Li/gradescope-mcp) pattern | 🟢 MIT | Copy its **preview-first write protocol**: no grade or adjustment is written without an explicit confirmation step |

**Wiring**

1. Deploy `openpiar` **for the client, as the client's system** — 🔴 AGPL-3.0 means this
   is a deployment, not a product Globant folds into an offering. Price it accordingly.
2. Run `TutorIA` as the learner-facing agent inside the client's Open edX. 🟢 Its MIT
   grant means **the tutor customisations can stay closed** even though the platform under
   it is AGPL — the boundary is Open edX's plugin/XBlock edge, exactly as this file's
   governing rule requires.
3. Feed the PIAR's declared barriers into `TutorIA`'s prompt context, so the reasonable
   adjustments the decree records are the adjustments the tutor actually applies.
   🔵 **This is the whole value of the pattern**: elsewhere the PIAR is a filed PDF.
4. Use `open-test` for assessment in schools without reliable connectivity, with its
   per-student randomisation standing in for invigilation.
5. Gate every write — adjustment, grade, PIAR revision — behind a **recorded teacher
   confirmation**. 🟢 No Colombian statute compels this yet; the EU AI Act and Vietnam's
   Law 134/2025/QH15 both do, so building it now makes the same deliverable exportable
   (see `intel/trends.md` §20).

**What the engagement delivers.** A funded, statutory compliance system — not a pilot —
with the tutoring layer as the part that stays proprietary. 🔴 **Licence boundary to
hold:** `openpiar` is network copyleft; any Globant modification to *it* is the client's
under AGPL. Keep Globant IP in the `TutorIA` layer and in the oversight record.

## 🆕 Pattern 14 — Reaching a client's LMS when "LTI support" is not one capability

🔵 **The failure this prevents.** An engagement scopes "we'll write grades back to the
client's LMS over LTI", picks an LTI library from a roundup, and discovers at integration
time that the library does **launches only** — no AGS, so no grade can be submitted.
`p358` found exactly that row:
[`SanDiegoCodeSchool/lti-node-library`](https://github.com/SanDiegoCodeSchool/lti-node-library)
is MIT, live, and its own README states NRPS and Deep Linking are not supported.

**Decide in this order, and the first question is not technical**

| Need | Component | Licence | Note |
|---|---|---|---|
| Node, full Advantage | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 Apache-2.0 | 🟢 **The default.** Launches, Deep Linking, grades, roles. 🟡 Pin a version — its README describes v7 as a full rewrite |
| Python agent | [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | 🟢 MIT | Deep Linking, AGS, NRPS. The default when the agent is Python, which on this base it usually is |
| Typed end-to-end | [`iamlucasb/lti-core`](https://github.com/iamlucasb/lti-core) | 🟢 MIT | Deep Linking 2.0, JWKS. 🟡 **RS256 only**, and its docs are explicit that the library *"never decides who may configure content"* — the tool must enforce that authorisation itself |
| Client runs Phoenix/Elixir | [`DecoyLex/ltix`](https://github.com/DecoyLex/ltix) | 🟢 MIT | The only BEAM-runtime option on this base |
| Canvas specifically | [`harvard-edtech/caccl`](https://github.com/harvard-edtech/caccl) | 🟢 MIT | Canvas app framework; pairs with `ltijs` |
| 🔴 **Never** | [`oat-sa/lib-lti1p3-deep-linking`](https://github.com/oat-sa/lib-lti1p3-deep-linking) | 🔴 **GPL-2.0** | IMS-certified — a conformance claim, not a grant. Strong copyleft **on a library** |
| 🔴 **Never** | [`GSU-CETLOE/lti1p3Library-php`](https://github.com/GSU-CETLOE/lti1p3Library-php) | 🔴 MIT, **no licensor named** | Holder line is the unfilled template `[Your Name / Organization]`. Nobody to attribute, and attribution is MIT's only condition |
| 🔴 **Never** | [`blackboard/BBDN-LTI-Tool-Provider-Node`](https://github.com/blackboard/BBDN-LTI-Tool-Provider-Node) | 🔴 **no grant** | A vendor-org reference sample with no `LICENSE` is as unusable as a student project with none |

**Wiring**

1. **Write down which of the four services you need before choosing** — launch, Deep
   Linking, AGS, NRPS. 🔵 If the deliverable writes grades, AGS is non-negotiable and it
   is the service most small libraries omit.
2. Stand the tool up against the client's LMS as an **LTI 1.3 tool**, never a fork — this
   is what keeps Canvas's and Open edX's AGPL on their own side of the boundary.
3. Where MCP is also available, prefer it for *agent* access and keep LTI for
   *platform* integration. 🔵 They are not alternatives: LTI is how the LMS launches your
   tool; MCP is how your agent reads the LMS. A complete engagement usually needs both.
4. 🔴 **Before vendoring any connector, read its `LICENSE` copyright holder.** If it names
   someone other than the repository owner it is a fork, and on `p358`'s evidence a fork
   is **18 to 27 tools behind** its upstream. Install by registry identifier instead — it
   resolves upstream regardless of which page you found (`intel/trends.md` §21).

**What the engagement delivers.** A grade-writing, roster-aware LMS integration whose
licence position is defensible, chosen on capability rather than on a roundup's ranking.

## 🆕 Pattern 15 — A Kenyan K-12 administration deliverable that can stay closed

🔵 **Why this pattern exists now and could not before.** `verticals/solutions.md` has
carried one of this base's most expensive findings — **there is no permissive education
ERP**, so a closed administration deliverable must be priced as a build. 🟢 `p358` found
the first permissive row on that tier, and it is narrow enough that the finding still
holds for institution-wide ERP while no longer holding for K-12 school administration.

**Components**

| Role | Repo | Licence | Note |
|---|---|---|---|
| Administration base | [`Moha-abshir/SMS`](https://github.com/Moha-abshir/SMS) | 🟢 **MIT** | Multi-role school management built against **Kenya's CBC**. TypeScript 5.3, React 18, Node 20, Drizzle ORM, PostgreSQL 16. 🟡 Single author, 2026, no deployment evidence — see `ACTION ZZ-bh` |
| National-data connector | [`gabrielmahia/elimu-mcp`](https://github.com/gabrielmahia/elimu-mcp) | 🟢 MIT | Kenya school registry, KCSE/KCPE, HELB loans, TVET. 🔴 **Its README states the shipped data is DEMO and "not suitable for operational decisions"** — this supplies the tool surface and schema; real endpoints and credentials are the engagement's to obtain |
| Offline learning | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT** | Offline-first by design. The licensed answer to the connectivity constraint |
| Offline assessment | [`Riskbreaker2077/open-test`](https://github.com/Riskbreaker2077/open-test) | 🟢 MIT | Local server over school intranet, per-student randomised papers |

**Wiring**

1. Fork `Moha-abshir/SMS` as the administration base. 🟢 MIT means the fork and every
   customisation **can stay in a closed client deliverable** — the one place on this base's
   administration tier where that is true.
2. Add `elimu-mcp` as the agent's read surface over Kenyan national education data, 🔴 with
   its demo data replaced by real endpoints before anything operational depends on it.
   🟡 Note its README also states **pull requests are not accepted**: an engagement that
   patches it owns a fork from that day.
3. Serve learning content through `kolibri`, which assumes no connectivity rather than
   degrading without it.
4. Assess with `open-test` on the school's own intranet.

**What the engagement delivers.** A closed, CBC-aligned school administration system with
an AI layer over national data, deliverable in a market where connectivity cannot be
assumed. 🔴 **The honest caveat to carry into the proposal:** the administration base is a
**young single-author project**, not a vendor-backed platform. For an *institution-wide*
ERP the recommendation is still `openeducat_erp` (LGPL-3.0) or a priced build — one school
management system is not an ERP, and `verticals/solutions.md` sets out the comparison.

## 🆕 Pattern 16 — A special-education IEP deliverable, built because it cannot be adopted

🔴 **Why this pattern is a build and not an integration.** `p359` measured the
special-education tier first-hand: **seven addresses, one permissive grant.** Two of the
seven — including the only genuinely mature one, at 836 commits and 7 authors — are
**explicitly noncommercial** (`CC-BY-NC-4.0` and `PolyForm Noncommercial 1.0.0`), and
four carry **no licence file at all**. 🟢 This is the clearest build-rather-than-adopt case
on these shelves, and §23 of `intel/trends.md` explains why it is likely to stay that way.

🔵 **And why it is worth building anyway.** An IEP is a **statutory document** — under
IDEA in the United States, with binding analogues across `intel/market.md`'s
jurisdictions — which means the deliverable has a compliance budget, a named owner at the
client, and an audit trail requirement. Those are the three things that make an
engagement fundable.

**Components — every grant read from payload, `2026-10-21`**

| Role | Repo | Licence | Why this one |
|---|---|---|---|
| Records, assessments, IEP workflow | [`dg13788/iep-system`](https://github.com/dg13788/iep-system) | 🟢 **MIT** (`main/LICENSE`) | **The one permissive row on the tier.** Student records, assessment capture, a five-step IEP wizard, e-signatures. React / PHP / MySQL. 🟡 Chinese-language UI, 38 commits, 4 authors — take the **data model and workflow**, expect to rewrite the presentation layer |
| Goal drafting over client documents | [`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills) | 🟢 **Apache-2.0** | Already carried on `agents/top.md`. Skills as the packaging for pedagogical instructions — §8 of `intel/trends.md` — so goal-drafting guidance stays **the client's content**, not vendored code |
| Compliance + specialist agents | [`iblai/k-12-agents`](https://github.com/iblai/k-12-agents) | 🟢 **MIT** (`main/LICENSE`) | Already held. School Assistant **plus 12 specialists**, including a **`special-education-agent`**, `assessment`, `curriculum-alignment` and `student-safety`, with PowerSchool skills. 🟢 **This is the row that corrected `T-p288b`, and it is the only permissive special-education *agent* on this base** |
| Progress evidence store | [`pelotech/xapi-lrs`](https://github.com/pelotech/xapi-lrs) | 🟢 **Apache-2.0** | 🆕 `p359`. xAPI **1.0.3 and 2.0** conformant, admin UI, OpenTelemetry. **An IEP's legal weight is its progress record** — this is where goal-progress statements land in a standard format rather than a bespoke table |
| Mastery / difficulty calibration | [`joakimwallmark/irtorch`](https://github.com/joakimwallmark/irtorch) | 🟢 **MIT** (`main/LICENSE.txt`) | 🆕 `p359`. **The only maintained permissive IRT engine** — committed 2026-10-19. Turns "the student is progressing" into a calibrated estimate a hearing officer can be shown. 🔴 Not `eribean/girth`: same licence, untouched since 2022 |
| Reaching the client's LMS | [`falkenslab/moodle-mcp`](https://github.com/falkenslab/moodle-mcp) or [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) | 🟢 MIT | Read coursework and grades across the protocol boundary. 🔴 **Never** `openedx-mcp` or `csmediapro/moodle-mcp-server` — copyleft connectors sit *inside* the deliverable |

**Wiring**

1. **Fork `dg13788/iep-system` for the data model, not the UI.** MIT means the fork and
   every customisation stay in a closed client deliverable. 🟡 Budget the presentation
   layer as a rewrite: the workflow is the asset, the Chinese-language React surface is
   not reusable in an English-, Spanish- or Portuguese-language engagement.
2. **Put goal drafting behind a skill pack, not in code.** Package the client's own
   jurisdictional guidance — IDEA goal grammar, the state's required fields, the
   district's templates — as skills on the `k12-teacher-skills` pattern. 🟢 **The
   client's pedagogy stays the client's**, and the same deliverable re-targets to another
   jurisdiction by swapping a skill directory.
3. **Write every goal-progress observation to `xapi-lrs` as an xAPI statement.** This is
   the step that makes the deliverable defensible: a standard, queryable, timestamped
   record rather than rows in the application's own database. 🟢 It is also what §2's
   evidence-of-impact procurement gate asks for, already in a portable format.
4. **Calibrate with `irtorch` where the client's goals are measured by assessment
   items.** Progress on an uncalibrated item set is not evidence. 🔵 The join of a
   permissive IRT engine to an LLM-assisted grader is **unbuilt** — `repos/foundations.md`
   §Psychometrics records the gap — so this step is engineering work, not configuration.
5. **Read coursework over MCP; never fork the LMS.** Standard boundary rule.
6. 🔴 **Put a human in the loop at the decision, by construction.** Oklahoma and Maryland
   now **require human oversight and bar AI from high-stakes decisions about students**
   (`intel/market.md` §North America); Korea's AI Basic Act names education a high-impact
   sector; Vietnam's Decision 33/2026 lists education as high-risk where output drives
   decisions without meaningful human review; and Annex III of the EU AI Act names
   education assessment by type. 🟢 **The model drafts and the case manager signs** —
   which is also exactly what `HernanDiaz/moodle-local_aigrader` demonstrates on the
   grading side, and a working reference worth reading even though its GPL-3.0-or-later
   grant keeps it outside the deliverable.

**What the engagement delivers.** A closed, jurisdiction-targeted IEP drafting and
progress-evidence system: statutory fields enforced, goals drafted under the client's own
pedagogical guidance, every progress observation in a standard xAPI record, calibrated
mastery estimates behind the progress claims, and a human signature at every decision
point.

🔴 **The honest caveats to carry into the proposal.**

- **The permissive base is a 38-commit project.** `dg13788/iep-system` is the *only*
  permissive option measured, not a safe one. Price the data-model fork as a read-and-
  reimplement, not as an adoption.
- 🔴 **Do not reach for the mature alternatives.** `The-Burnes-Center/a-iep` is the best-
  maintained special-education codebase this base has found and it is **CC-BY-NC-4.0**;
  `boktoday/iep-agent-hermes-agent` is **PolyForm Noncommercial**. Both read as "free" and
  neither can be used in paid work. 🟢 This is the single most likely way this engagement
  goes wrong.
- 🔴 **Four of the seven addresses have no grant** — including the one with the closest
  architecture to this pattern, `omerpanay/special-education-rag` (agentic teacher
  assistant with IEP draft generation over RAG). 🔴 **And the same is true of a row this
  base has held for far longer:** `eakarsu/ai-special-education-iep-compliance` covers
  evaluation timelines, service delivery and annual reviews — exactly this pattern's
  compliance surface — and carries **no grant in 21 files**, re-confirmed at `p359`. 🟢 It
  is a **requirements document**, not a component. 🟢 **Ask for the grant before designing
  around any of them.** Per §22 of `intel/trends.md`, these authors are not withholding a licence;
  they have never been asked for one, and a two-line email is the whole intervention.
- 🟡 **The data is special-category under every privacy regime that matters.** An IEP
  contains disability and health information: **GDPR Art. 9** in EMEA, FERPA plus state
  student-privacy statutes in the US (California **AB 1159** restricts using student data
  to train models at all), and LGPD Art. 11 in Brazil. Settle the lawful basis and the
  training-data position **before** the architecture, not after.

## 🆕 Pattern 17 — An AI layer on a French ENT, built beside the portal because AGPL reaches a fork

**Client shape.** A French *région*, *département* or académie — or the integrator holding
its contract — running an **ENT** (*Espace Numérique de Travail*) for every school in its
territory. One regional deployment reports **2.7 M users across 5 790 institutions**. They
want AI on top of data that already exists in the portal — the *cahier de textes*, the
competency record, attendance — and the deliverable must stay the integrator's property.

**Why this pattern did not exist one pass ago.** This base held the *interchange* layer
(LTI, SCORM, xAPI, Caliper, OneRoster) and a row of LMSes, and had **no row for a national
school portal**. `p360`'s French function legs shelved the ENT stack.

**The licence boundary, decided before anything else.** The entire ENT tier is
**AGPL-3.0**. 🔴 Forking `entcore` or any module carries network copyleft into whatever the
client deploys. 🟢 `entcore` is *a modular kernel with its own HTTP API and a module
boundary* — that boundary is the pattern.

**The stack, every grant read from the payload on 2026-10-21:**

1. **The portal, left alone.** [`edificeio/entcore`](https://github.com/edificeio/entcore)
   (🟡 **AGPL-3.0**, `master/LICENSE`, default ref 🔴 `master`). 🟢 **Deploy or extend it as
   a module, and keep your own service out of its process.** Use this address: 🔴
   `open-ent/entcore` is five months stale, `OPEN-ENT-NG/entcore` is a single-branch mirror
   one commit behind, and `opendigitaleducation/entcore` is the *same repository* under the
   vendor's former name.
2. **The statutory data you are reasoning over.**
   [`OPEN-ENT-NG/cahier-de-textes`](https://github.com/OPEN-ENT-NG/cahier-de-textes)
   (AGPL-3.0, `dev/LICENSE`) is the lesson log — per-session lessons, homework,
   attachments. [`OPEN-ENT-NG/competences`](https://github.com/OPEN-ENT-NG/competences)
   (AGPL-3.0, 🔴 `dev/LICENCE`) carries the *livret scolaire* competency model, which is
   the mastery signal this build needs and the reason not to invent one.
   [`OPEN-ENT-NG/presences`](https://github.com/OPEN-ENT-NG/presences) (AGPL-3.0, 🔴
   `dev/LICENCE`) is attendance.
3. **Read them over the API, from your own service.** The AI service is a separate process
   that authenticates to `entcore` and reads those modules' endpoints. 🟢 **This is the
   whole licence argument**: AGPL-3.0's network clause binds the portal's own source, which
   is already published, and does not reach a separate program that talks to it.
4. **Mastery estimates that survive a *conseil de classe*.**
   [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) (🟢 **MIT**) for Bayesian Knowledge
   Tracing over the competency records — a defensible per-competency estimate rather than a
   model's opinion, which is what a French teachers' council will actually interrogate.
5. **Exercises, if the client wants them inside the portal.**
   [`open-ent/exercizer`](https://github.com/open-ent/exercizer) (AGPL-3.0, 🔴
   `master/LICENCE`) already does MCQ, cloze and ordering with auto- and hand-marking.
   🟢 Extend it as an ENT module and the copyleft stays on the portal side where it already
   is; 🔴 do **not** lift its code into the closed service.
6. **Paper, because French assessment is still largely paper.**
   [`ajjalti/EvalStudio`](https://github.com/ajjalti/EvalStudio) (🔴 **AGPL-3.0**) does
   computer-vision marking of **scanned copies**. 🔴 Run it as its own service behind a
   queue — not linked into the deliverable — or reimplement the step; it is the one
   component here whose licence would otherwise reach the client's code.
7. **Disclosure, because this is the EU.** The EU AI Act treats education uses as
   high-risk and its obligations bite from **2 Aug 2026**. Wrap the whole thing in
   **Pattern 3**'s conformity layer; the competency record makes this an assessment system,
   not a chatbot.

**What the engagement delivers.** A closed AI service beside an AGPL portal the client
already owns, reading statutory data in place, with per-competency mastery estimates and an
Act-ready disclosure and oversight record.

🟡 **Price discovery from the source tree, not the documentation.** `entcore`'s README
still specifies **JSE 7** and a clone URL on a decommissioned host, while the code took a
commit on **2026-10-20** from 21 authors. 🔴 An estimate built by reading that README will
be wrong in the expensive direction.

🟢 **The market note that makes this a migration pattern rather than a greenfield one.**
The IGÉSR inspectorate (15 Jul 2025) puts ENT in **62 %** of French public primary schools
and records that one family can face **three different ENT solutions** across école,
collège and lycée, recommending territorial harmonisation and ÉduConnect. 🔵 Harmonisation
work is the near-term budget; the AI layer is what makes it worth doing twice.

## 🆕 Pattern 18 — Curriculum-bound exam generation for a national curriculum, with the generator swapped out

**Client shape.** A ministry, publisher, school group or teacher co-operative in a country
with a prescribed national curriculum, where teachers hand-write assessments. The
Indonesian case is measured: **4–8 hours a week** per teacher producing exams in a word
processor.

**Why the obvious build is wrong.** The tempting move is a prompt plus a PDF template.
🔴 It fails on the thing that actually matters, which is **curriculum binding** — an item
that does not map to a declared learning objective is unusable to the teacher who has to
justify the paper, and a model will produce plausible items that map to nothing.

**The reference implementation to start from, and the part to replace.**

1. **The orchestration** — [`naufaldi/teacher-exam`](https://github.com/naufaldi/teacher-exam)
   (🟢 **MIT**, `main/LICENSE`, © *Naufaldi Rafif*; **435 commits, 4 authors**, live
   deployment). One sentence in, an A4 print-ready paper out: mixed item types, answer key,
   and a teacher-facing *pembahasan* per item, bound to **Kurikulum Merdeka** CP/TP by an
   explicit review step. 🟢 **MIT, so fork it into the deliverable.**
2. 🔴 **The part that must be replaced.** Its core generation calls a **hosted proprietary
   model**. For a ministry deployment that is usually the blocker — data residency,
   procurement, or simply cost per paper. 🟢 **The curriculum binding and the print
   pipeline are the valuable, reusable parts**; the generator is a swap.
3. **Swap in an item bank with a review workflow** —
   [`gygy-open/question-bank`](https://github.com/gygy-open/question-bank) (🔴 AGPL-3.0,
   run as its own service) or [`QingdaoU/OnlineJudge`](https://github.com/QingdaoU/OnlineJudge)
   (🟢 MIT) where the subject is programming. 🟢 **Generate once, review, then reuse** —
   which converts a per-paper model cost into a one-off authoring cost and is what makes
   the economics work at ministry scale.
4. **Keep a human gate on free text, and say so.**
   [`nvaes/CEB`](https://github.com/nvaes/CEB) (🟢 MIT, 🇧🇪) is the posture to copy: it
   auto-marks **only** the checkbox items and states that automatic marking of free text
   would be unreliable. 🔵 That sentence in a ministry proposal is worth more than a
   benchmark.
5. **Paper in, paper out.** [`ajjalti/EvalStudio`](https://github.com/ajjalti/EvalStudio)
   (🔴 AGPL-3.0, own service) marks the scanned copies back. 🟢 The loop closes without the
   school needing a device per pupil, which is the constraint in most of the countries this
   pattern is for.
6. **Report into whatever the school runs**, over LTI or the portal's API — Pattern 14 for
   the LMS case, Pattern 17 where the client runs a national portal.

🔴 **The licensing warning this pattern exists to carry.** Of **20** live Indonesian
addresses `p360` probed, **one** carries a usable, author-attributed permissive grant over
actual software. The best-built one — `sira313/rapkumer`, **203 commits** — is under a
bespoke licence whose §3 prohibits commercial use *in any form*, explicitly including paid
installation, configuration or support. 🟢 **Read the payload before the README, and in
this market expect to ask the author.** Three other grant files in that leg did not survive
scrutiny: one is a marketing site, one names a **framework vendor** as copyright holder,
and one is the non-commercial licence above.

## Boundary cheat-sheet

| If the host platform is… | Reach it by… | Never |
|---|---|---|
| Canvas, Open edX, Frappe LMS, ClassroomIO (**AGPL**) | LTI 1.3 tool · MCP server · web services | Forking, or linking client code |
| Moodle, Chamilo, ELMSLN, Judge0, UDOIT, 🆕 HUSTOJ, 🆕 openSIS Classic (**GPL**) | Web services · the plugin API as a *separate* deployed plugin · the API over HTTP | Statically linking into proprietary code |
| 🆕 Hydro, DMOJ, Sharif Judge, the AGPL item banks (**AGPL**) | The client's own deployment, reached over HTTP | Hosting it as the studio's service |
| BigBlueButton, OpenEduCat (**LGPL**) | Dynamic linking · API | Forking into closed source |
| OpenOLAT, Sakai, Kolibri, Moodle App, Opencast, QingdaoU OnlineJudge, Judger, Otter-Grader, py-fsrs, 🆕 **LectureLab**, 🆕 **bruchris/canvas-lms-mcp**, 🆕 **G36maid/moodle-mcp** (**permissive**) | Anything, including forking | — |
| 🆕 ERPNext (**GPL-3.0**) | Its **REST API**, as a separate service | A Frappe app in-process, or linking client code |
| 🆕 Cap, CaptureFlow (**split: AGPL app, MIT engine**) | Vendoring the **MIT engine only** — `licenses/LICENSE-MIT`, `packages/engine/` | Forking the repository; the combined distribution is AGPL |
| 🔴 🆕 `csmediapro/moodle-mcp-server` (**AGPL-3.0 connector**) | 🔴 **Nothing.** Use a permissive Moodle MCP instead | Any use — a copyleft *connector* sits inside the engagement, not across the boundary |
| 🔴 🆕 `mrgutierrezmario/lecture-note-app`, 🆕 `boktoday/iep-agent-hermes-agent` (**PolyForm Noncommercial**) | 🔴 **Nothing in paid work** | All commercial use without a separate licence from the holder |
| 🔴 🆕 `The-Burnes-Center/a-iep` (**CC-BY-NC-4.0**) | 🔴 **Nothing in paid work.** Read it as a reference for parent-facing IEP explanation, build the deliverable from `dg13788/iep-system` | Any commercial use — and note it is the *best-maintained* special-education codebase on this base, which is what makes it dangerous |
| 🆕 `HernanDiaz/moodle-local_aigrader` (**GPL-3.0-or-later**) | Deploy it as a **plugin inside the client's own Moodle** | Vendoring it into a studio deliverable |
| 🟢 🆕 `jeffyding/OpenLRW` (**ECL-2.0** — permissive) | Anything, including forking — ECL-2.0 is Apache-2.0 with a narrowed patent grant | 🔴 Depending on it: **dead since January 2018.** Read the OneRoster↔Caliper↔xAPI schema, deploy `pelotech/xapi-lrs` |
| 🔴 🆕 `shaheeranser/exam-proctor` (**Apache-2.0** — permissive) | Reading its LTI 1.3 wiring and AGS grade passback as a **reference architecture** | 🔴 Deploying it into an EU engagement as it stands: GDPR Art. 9 biometrics, and clear of the Art. 5(1)(f) prohibition only because one MediaPipe default is unset |

**One-line version:** in education, the licence picks the architecture. Decide the
boundary before the stack.

🔴 **🆕 And `p357` found the one case where that rule inverts.** Every row above assumes
the copyleft component is the **platform**, which a protocol boundary holds at arm's
length. When the copyleft component **is the connector** — an AGPL MCP server — the
boundary is on the **wrong side of it**: the client's agent talks to it over exactly the
network interface AGPL's clause is written about, and it sits inside the deliverable
rather than across from it. 🟢 **So check the licence of the connector before the
licence of the platform.** It is the smaller component and the larger risk.
