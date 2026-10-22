---
industry: education
region: Global
updated: 2026-10-22
---

# Compose patterns — education

**Pass `p383` · 2026-10-22 · FULL REWRITE.** Prior version archived at
[`archive/2026-10-22-p383-pre-rewrite/compose-patterns.md`](../archive/2026-10-22-p383-pre-rewrite/compose-patterns.md).

Every repo named here was verified first-hand on 2026-10-22 —
[`verified-repos`](../evidence/verified-repos.2026-10-22-p383.tsv). Licences are read from the
payload at the repository's **real default ref**, which for 13 of 58 live addresses is not `main`.

**The governing constraint for all of these:** the platform tier is copyleft, the agent tier is
permissive. Every pattern below therefore puts a **documented interop boundary** — LTI 1.3, MCP, or
web services — between client-owned code and the platform. None of them forks an LMS.

🆕 **`p389`** adds **`Pattern Q`** (the generated classroom, the greenfield answer when there is no
LMS to bolt onto), gives **`Pattern B`** a maintained mastery model, and gives **`Pattern D`** two
components that remove its server. Every repository named in those changes was **dated** this pass —
last commit at the real default ref:
[`verified-repos`](../evidence/verified-repos.2026-10-22-p389.tsv). 🔵 **Read a date as a cost line:**
a permissive repository nobody has touched in eight months is something you *vendor and maintain*, not
something you *integrate* — which is why `Pattern B` vendors `pybryt` and why `Pattern Q` pins a ref.

---

## Pattern A — Tutor over the client's existing LMS (no fork, no copyleft exposure)

**For:** a client who already runs Moodle or Canvas and wants a tutor that knows the actual course.

**Wiring:**
1. **Expose the LMS.**
   - *Moodle:* install **`webservice_mcp`** from Moodle's own plugin directory (Moodle 4.5–5.2,
     latest release 23 Jul 2026). It serves Moodle's external functions as **MCP tools over
     JSON-RPC 2.0**, gated on the `webservice/mcp:use` capability. Configured inside Moodle — no
     patch to core, so **no GPL obligation reaches your agent**.
   - *Canvas:* [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) (**MIT**) for courses,
     assignments, submissions, grading, rubrics, students; or the fork
     [mdweaver/canvas-mcp](https://github.com/mdweaver/canvas-mcp) (**MIT**) which adds office-hour
     appointment groups, syllabus read/write, student groups and course-content copy.
   - 🆕 `p390` *Open edX:* skip the MCP hop and run **inside** the platform as an **XBlock** — and the licence maths
     works out better than it looks. The platform is **AGPL-3.0**, but the component API your plugin imports,
     [`openedx/XBlock`](https://github.com/openedx/XBlock), and the [`xblock-sdk`](https://github.com/openedx/xblock-sdk)
     you develop against are both **Apache-2.0** (`LICENSE.TXT`, both dated 2026-10-22). **So the XBlock you write can stay
     MIT or proprietary while running in an AGPL host** — no fork, no LTI hop, and full access to course state.
     [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) (MIT, Colombia) is the working proof.
     🔴 **Check the boundary per package, not per org:** [`openedx/openedx-learning`](https://github.com/openedx/openedx-learning)
     and the `frontend-app-*` MFEs are **AGPL-3.0**, so an import from those pulls network copyleft straight back in.
     Keep the plugin's dependency list to `XBlock` plus your own code and audit it in CI.
   - 🟡 **Grant status, corrected:** the plugin repo
     [onbirdev/moodle-webservice_mcp](https://github.com/onbirdev/moodle-webservice_mcp) has **no
     root licence file**, but `version.php` carries the full **GPL-3.0-or-later** header Moodle
     requires of every plugin — so it is granted, and GPL is survivable because you reach it over
     JSON-RPC rather than linking to it.
     [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) is
     **manifest-only MIT** (`package.json` declares it; the file it names is absent from the tree).
     🔴 **Do not use** [loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp): no licence file
     **and** no `license` field in `pyproject.toml` — genuinely no grant to redistribute.
2. **Ground it in the course material.** [infiniflow/ragflow](https://github.com/infiniflow/ragflow)
   (**Apache-2.0**) over the course files, with
   [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured)
   (**Apache-2.0**) for the PDF/DOCX/PPTX/scan reality. If the client has lecture video,
   [opencast/opencast](https://github.com/opencast/opencast) transcripts are the richest corpus
   available and nobody is using them.
3. **Give it pedagogy and memory.** [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)
   (**Apache-2.0**) for persistent learner memory plus material-grounded tutoring. If the client
   wants explanation *pitched* to the learner's state rather than merely retrieved, look at
   [plastic-labs/tutor-gpt](https://github.com/plastic-labs/tutor-gpt) — but it is **GPL-3.0**, so
   run it as a separate service, not as a library inside the deliverable.
4. **Front it.** [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) (**MIT**) — SSO,
   per-user quota, provider routing and the **audit log** that gets the build past a data-protection
   officer. (Not `open-webui`: its `LICENSE` is 2,819 B of BSD-3 text **plus** a branding
   restriction and a CLA.)
5. **Prove it.** [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)
   (**MIT**) with [MMLU](https://github.com/hendrycks/test) (**MIT**) and
   [GSM8K](https://github.com/openai/grade-school-math) (**MIT**), scored on the client's own
   subject mix, before and after.

**Licence posture:** client-owned code is MIT/Apache/BSD throughout. The only copyleft component is
the LMS itself, reached over a published protocol. **Deliverable stays closed if the client wants it
closed.**

---

## Pattern B — Autograding that assesses the approach, not just the output

**For:** CS, data-science and engineering programmes drowning in submissions.

**Wiring:** [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) (**BSD-3**) for
identical per-cohort compute → [jupyter/nbgrader](https://github.com/jupyter/nbgrader)
(**BSD-3**) for the release/collect/autograde/return lifecycle →
[ucbds-infra/otter-grader](https://github.com/ucbds-infra/otter-grader) (**BSD-3**, default ref
`master`) for container-isolated grading at cohort scale →
[microsoft/pybryt](https://github.com/microsoft/pybryt) (**MIT**) to check **how** the student got
there, not only whether the answer matched →
[jupyterlab/jupyter-ai](https://github.com/jupyterlab/jupyter-ai) (**BSD-3**) so the LLM explains
*why* the approach was wrong, inside the notebook the student is already in.

**Why this combination:** pybryt is the piece everyone misses. An LLM that reviews output rewards
the student who guessed; pybryt's annotations let you detect the *intended method* and then have the
model give feedback on the method. **Fully permissive — BSD-3 and MIT only, zero copyleft.**

🔴 🆕 `p387` **Vendor pybryt; do not install it.** PyPI `pybryt` has shipped nothing since
**v0.7.0, 2022-04-28** — four and a half years — so a client support contract cannot rest on it as a
dependency. The pattern does not change: copy the annotation approach (and, licence permitting under
its MIT grant, the code) into the deliverable and maintain it there, with the maintained BSD-3
halves of this stack (`nbgrader`, `otter-grader`) carrying the running infrastructure. Dates:
[`registry-recency`](../evidence/registry-recency.2026-10-22-p387.tsv).

🟢 🆕 `p388` **And the notebook-tutor half now has a maintained component, which changes what you
vendor.** [QuantStack/jupyter-ai-tutor](https://github.com/QuantStack/jupyter-ai-tutor) (**BSD-3**,
`main` · `139bb11`, **v0.3.2, 7 releases, → 2026-09-25**, from a known Jupyter-ecosystem maintainer)
replaces the ad-hoc "wire `jupyter-ai` into the grading loop" step with a component built for exactly
this job:

- A per-cell **Explain Code** button sends the cell source, the kernel language, **the error
  traceback**, and the preceding cells up to the last markdown cell **as the exercise statement** —
  so the model sees the task, not just the broken line.
- 🟢 **The tutor persona lives in a `TUTOR.md`, discovered by walking up from the notebook's
  directory to the server root.** Each course, module or folder carries its own pedagogy **in version
  control**. This is the single most useful thing on this shelf for a client engagement: *"AI must
  not give the answer"* stops being a prompt someone pasted and becomes a reviewable file in the
  course repository, diffable and auditable per cohort.
- 🟢 **`reference_solution` and `evaluation_criteria` ride in cell metadata, ROT13-encoded** so they
  are not casually readable by a student holding the notebook — the same instinct as `pybryt`'s
  annotations, shipped in a maintained package.

**Revised wiring:** `jupyterhub` → `nbgrader` → `otter-grader` for the lifecycle and
container-isolated grading (all BSD-3, all maintained) → **`jupyter-ai-tutor`** for the in-notebook
explanation layer, configured by a per-course `TUTOR.md` → **vendored `pybryt` annotations** for
approach assessment, maintained inside the deliverable as `p387` requires. 🔵 Note the division of
labour this produces, and it is the one the guardrail below wants anyway: `jupyter-ai-tutor` **explains
and never grades**, `nbgrader`/`otter-grader` grade and never explain. 🟡 It requires
`jupyter-ai-jupyternaut` (<0.1) for the agent, so pin that bound.

🟢 🆕 `p389` **And the missing third component: the mastery model.** Everything above assesses a
*submission*. Nothing in it answers the question a programme director actually asks — **which skills
has this student mastered, and what should come next** — and this base has carried that gap while
recommending a dependency that stopped shipping in 2022. The maintained answer is
[**CAHLR/pyBKT**](https://github.com/CAHLR/pyBKT) (**MIT**, real ref `master`, **last commit
2026-10-21 — 1 day**), from UC Berkeley's CAHLR, who also maintain
[**OATutor**](https://github.com/CAHLR/OATutor) (**MIT**, `main`, **1 day**) as the tutoring front end
built on it.

- **What it adds to this wiring:** fit **Bayesian Knowledge Tracing** on the client's *own*
  `nbgrader`/`otter-grader` outcome logs — one row per (student, skill, attempt, correct) — and you get
  per-skill **learn, guess, slip and forget** parameters plus a running mastery probability per student.
- 🟢 **Why it is the defensible choice and not just the available one:** those four parameters are
  **inspectable numbers a client can argue with**, re-estimated on their own cohort. "The model thinks
  Ana has not mastered partial fractions, with these parameters fitted on this data" survives a
  procurement review; "the LLM judged her weak" does not. North American and Maryland-style rules that
  bar AI from high-stakes decisions about students are satisfiable here precisely *because* the
  decision rule is a published model rather than a generation.
- **Revised wiring, end to end:** `jupyterhub` → `nbgrader` → `otter-grader` (lifecycle + isolated
  grading) → **`pyBKT`** fitted on the outcome log (mastery per skill) → **`jupyter-ai-tutor`** with a
  per-course `TUTOR.md` for in-notebook explanation → **vendored `pybryt` annotations** for approach
  assessment. 🟢 **Still fully permissive: BSD-3 and MIT only, zero copyleft.** 🔵 The sequencing
  matters: `pyBKT` decides *what to work on*, the tutor explains *why the attempt failed*, and the
  graders remain the only components that produce a grade.
- 🟡 **Cold start is the real constraint**, not the licence: BKT needs interaction history. For a new
  cohort, serve `OATutor`'s scaffolds with default parameters, log, and re-fit at the end of the first
  module — and say so in the estimate rather than discovering it in week three.

**Guardrail:** where DC-style rules apply, AI must not be the grader of record. Configure the LLM as
a **feedback generator with a human grade-of-record** and keep the audit trail; that configuration is
the deliverable, not a disclaimer. 🆕 `p389` The same rule governs the mastery model: a BKT mastery
probability is **advisory input to a human decision**, and the moment it auto-finalises anything
consequential it is the "sole basis for a decision without meaningful human review" that Vietnam's
Decision 33/2026 and EU Annex III both reach.

---

## Pattern C — Citation-grounded academic assistant (and the EU compliance story that comes free)

**For:** higher-ed research support, library services, graduate programmes.

**Wiring:** [Future-House/paper-qa](https://github.com/Future-House/paper-qa) (**Apache-2.0**) as
the answer engine → [AkariAsai/OpenScholar](https://github.com/AkariAsai/OpenScholar)
(**Apache-2.0**) or [allenai/ai2-scholarqa-lib](https://github.com/allenai/ai2-scholarqa-lib)
(**Apache-2.0**) for multi-paper synthesis →
[Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) (**Apache-2.0**)
for ingest → [LibreChat](https://github.com/danny-avila/LibreChat) (**MIT**) as the campus gateway.
For guided-inquiry assignments, [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher)
(**Apache-2.0**) as the student-facing research scaffold.

**The compliance argument:** paper-qa **declines to answer** without retrieved evidence. Under
**EU AI Act Art. 50** (transparency, live from **2 Aug 2026** — *not* delayed by Regulation (EU)
2026/1744) a system that cites its sources and refuses otherwise is dramatically easier to document
than one that generates fluently. Build the refusal behaviour in, then point at it in the
conformity file. **Fully Apache-2.0/MIT.**

---

## Pattern D — Offline-first deployment for connectivity-constrained regions

**For:** LATAM, African and rural APAC deployments — including the nine countries in the Google.org
AI-literacy rollout (Argentina, Brazil, Chile, Colombia, Dominican Republic, El Salvador, Mexico,
Peru, Uruguay).

**Wiring:** [learningequality/kolibri](https://github.com/learningequality/kolibri) (**MIT**,
default ref 🔴 `develop`) as the edge runtime — offline-first by design, not a degraded mode →
a small local model on the same device for the tutoring loop →
[FSRS](https://github.com/open-spaced-repetition/fsrs4anki) (**MIT**) for scheduling review, because
retention is the one outcome measurable without a network →
content authored in [H5P](https://github.com/h5p/h5p-php-library) — 🟡 **GPL-3.0, keep it as
runtime content, not linked code** → periodic sync to the central LMS over
[LTI 1.3](https://github.com/Cvmcosta/ltijs) (**Apache-2.0**) when a link is available. 🆕 `p391` **Use a maintained implementation:** `ltijs` (npm v7.0.7, 2026-10-06) for Node or `packbackbooks/lti-1p3-tool` (packagist v6.4.4, 2026-09-23) for PHP — **not** the standards-body copy `p390` cited, which is 2,333 days stale; and **not** `pylti1.3`, which is 1,431 days stale, so a Python agent sits behind a Node or PHP edge rather than speaking LTI itself.

**Why FSRS matters here:** it has published parameters, so "the student is retaining more" is a
number you can defend to a ministry, offline, without telemetry.

🟢 🆕 `p389` **Two components that remove a server from this pattern, which is the cost line that
actually kills offline deployments.**

1. **Lesson delivery with no application server at all.**
   [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) (**MIT**, committed **0 d**) exports a
   finished classroom as **one self-contained offline HTML file that plays the lesson** (or as a PPTX
   that keeps every scene). 🔵 **So the authoring server and the delivery target separate cleanly:**
   generate lessons once where there is power and bandwidth — a ministry office, a regional hub, a
   studio — and ship HTML files to the edge, where they need nothing but a browser. That is a
   fundamentally cheaper edge than "a Kolibri server per school", and the two compose: Kolibri remains
   the catalogue, progress store and sync layer; the exported HTML is the content it serves. 🟡 The
   export is a *playback* artefact — the agentic mid-lesson chat needs the server — so scope it as
   narrated, interactive courseware, not as a tutor that answers back offline.
2. **Notebook exercises with no per-student compute.**
   [jupyterlite/jupyterlite](https://github.com/jupyterlite/jupyterlite) (**BSD-3**, 6 d) runs the
   kernel **in the browser via WebAssembly**: no container, no install, no server, and it works offline
   once the page is cached. For a CS or data-science module this deletes the single largest
   infrastructure line in `Pattern B` at the edge. 🟡 No server also means no server-side autograding —
   collect the notebook and grade it with `nbgrader` when a link is available.

🔵 **What this pattern now says to a ministry.** The old answer was "a server per school, syncing when
it can." The 2026 answer is **generate centrally, deliver as files, compute in the browser, sync
progress when a link exists** — and every component in it is MIT or BSD-3, so the ministry owns the
deliverable outright. 🔴 One licence caution unchanged: H5P content stays **runtime content** under
GPL-3.0, never linked code.

---

## Pattern E — Sovereign EMEA public-sector stack

**For:** European public-sector clients demanding both data sovereignty and code ownership.

**Wiring:** **[OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) (Apache-2.0, default ref `master`)**
as the platform — **the only major open-source LMS a studio can extend with closed code** →
[serlo/serlo.org](https://github.com/serlo/serlo.org) (**Apache-2.0**) or
[oppia/oppia](https://github.com/oppia/oppia) (**Apache-2.0**, default ref `develop`) for structured
content → [openfun/richie](https://github.com/openfun/richie) (**MIT**, default ref `master`) as the
public catalogue → permissive agents over LTI 1.3 → all EU-hosted.

**The alternative, when the client insists on the openDesk lineage:** **ILIAS (GPL-3.0, default ref
`release_11`) + OpenProject behind a single SSO** — the ZenDiS pattern, and ZenDiS co-develops with
France's DINUM (LaSuite). 🔴 **But do not quote "8,600 schools":** that figure traces to a single
news item, and this pass found **no school deployment of openDesk in any source**. Named users are
administrative bodies. Sell the architecture, not the number.

**Dated compliance roadmap to attach to the bid** — this is the part competitors get wrong:
| obligation | when | status |
|---|---|---|
| Art. 4 AI literacy (every organisation using AI) | **since 2 Feb 2025** | 🔴 already binding |
| Emotion recognition in education | **prohibited since 2 Feb 2025** | 🔴 design it out |
| Art. 50 transparency | **from 2 Aug 2026** | 🔴 **not delayed** |
| Stand-alone high-risk education systems (admissions, assessment, proctoring, AI-detection in assessment, path-steering personalisation) | **2 Aug 2026 → 2 Dec 2027** per **Regulation (EU) 2026/1744** (OJ 24 Jul 2026) | 🟢 14 months of runway |

---

## Pattern F — Teacher-facing instructional assistant (the pattern the market and the regulator agree on)

**For:** LATAM and ANZ especially, where student-facing generative AI is either commercially
unproven or politically restricted.

**Wiring:** [satvik314/educhain](https://github.com/satvik314/educhain) (**MIT**) for lesson plans,
quizzes and question banks → [openedx/edx-ora2](https://github.com/openedx/edx-ora2)
(**AGPL-3.0**, run as the platform's own service) for rubric-based open-response assessment with
the human grade-of-record → [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) (**MIT**) so the
prompt pipeline has a metric attached instead of being hand-tuned →
[academico-sis/academico](https://github.com/academico-sis/academico) (**MIT**, Spanish built in) or
[openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) (**LGPL-3.0**, default ref
🔴 `19.0`) where the administrative record has to move too.

**Why it sells:** HolonIQ's 2026 LATAM EdTech 100 finds regional AI concentrated in **teacher-facing
instructional tools rather than consumer tutoring**; Brazil's PL 2.338/2023 reportedly targets
**student selection**; DC bans AI in grading, discipline, IEP and teacher evaluation; ANZ shows the
highest ban support in the Ipsos 2026 data. **Teacher-facing-only must be an architectural switch,
not a retrofit.**

---

## Pattern G — Provenance and labelling in the generation path (APAC, overdue)

**For:** anything shipped into **India** (amended IT Rules: prominent labels **and provenance
markers** on AI-generated content from **20 Feb 2026**) or **China** (AI-content labelling measures
applicable from **1 Sep 2025**; 988 services filed by 30 Jun 2026).

**Wiring:** label and sign **at generation**, not at display — every artefact an education agent
emits (generated question, feedback text, summary, image) carries a label and a provenance record
from the moment it is created; the LMS stores the record alongside the artefact (Moodle web services
/ MCP, Canvas API) so an audit can reconstruct what was machine-made months later; the student-facing
surface renders the label rather than deriving it.

**Why it is a build, not a memo:** if labelling happens in the UI, every export, API call and
copy-paste strips it. The requirement is on the content, so the marker belongs in the content
record. Most tutoring products shipped into IN/CN today do not do this and are already out of time.

---

## Pattern H — 🆕 `p384` Prerequisite-aware tutoring, grounded on a curriculum graph you must **not** fork

**For:** the adaptive-learning engagement everyone pitches and nobody can substantiate — "the tutor
knows what the learner is missing". The missing ingredient was never the model; it was a
machine-readable map of what must be mastered **before** the next topic. One now exists.

🔴 **Read this first.** [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy)
is licensed **ODbL** (`main/LICENSE`, 25,289 B), a **share-alike database licence**, and it has
**no code grant**. The whole pattern is built around keeping it on the right side of §4.4:

| what you do | ODbL clause | obligation |
|---|---|---|
| Tutor **output** grounded in the graph — next-topic choice, lesson plan, explanation, diagnosis | **§4.3** *Produced Work* | 🟢 **Attribution notice only.** Nothing to release. ODbL supplies the wording: *"Contains information from DATABASE NAME, which is made available here under the Open Database License (ODbL)."* |
| Shipping the graph **extended or merged** — client topics added, standards remapped, graph re-cut | **§4.4** *Derivative Database* | 🔴 **Share-alike.** Must be publicly used only under ODbL / a later ODbL / a compatible licence. §4.4(b): extracting *"the whole or a Substantial part of the Contents into a new database"* **is** a Derivative Database. |

🟢 **So the architectural rule is one sentence: join, never merge.** The client's curriculum data
stays in the client's own store; the taxonomy stays a read-only input resolved at query time. Break
that rule and the client's curriculum map becomes an ODbL obligation.

**Wiring:**
1. **Load the graph read-only, in its own store.** `data/topics.json` (1,930 micro-topics, each with
   a plain-language description, mastery **evidence** criteria, a type — conceptual / procedural /
   representational / language / meta — subject, domain and an approximate age range) and
   `data/dependencies.json` (4,102 edges, `topicId` → `prerequisiteId`, each tagged `hard`/`soft`
   with a one-line reason). 🔵 Keep it in a **separate schema or database** from anything client-
   specific, and never write client rows into it — that separation *is* the §4.4 firewall, and it
   should be visible in the deployment diagram so counsel can see it.
2. **Map the client's own curriculum to it by reference, not by insertion.** A join table
   `client_objective_id → topicId` in the **client's** store. The taxonomy's standards alignments
   (**NGSS, Common Core, UK National Curriculum**, Australian curriculum — Mathematics 442
   alignments across 325 topics, English 630/267, Science 245/131, HASS 210/124) usually give you
   the hook. 🟡 Unmapped client objectives are a **finding to report**, not a gap to paper over.
3. **Diagnose with the graph, not with the model's intuition.** Walk the DAG backwards from the
   failed topic over `hard` edges to find unmet prerequisites. This is a **graph traversal, not a
   generation** — deterministic, inspectable, and the reason the pattern can survive an audit that
   a pure-LLM "diagnosis" cannot. Treat `soft` edges as ranking hints only.
4. **Attach the tutor.** [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) (**Apache-2.0**) for
   persistent learner memory plus RAG over the learner's materials, with the traversal result from
   step 3 injected as the lesson objective. Teacher-facing variant: feed the same unmet-prerequisite
   list to [satvik314/educhain](https://github.com/satvik314/educhain) (**MIT**) to draft the
   remediation worksheet — which is the side of the market that is actually growing (Trend 5).
5. **Schedule the retention.** [fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki)
   (**MIT**) over the mastered topics. The graph says *what* to review next; FSRS says *when*, with
   published parameters. 🟢 Together they make "personalisation" two measurable quantities instead
   of a claim.
6. **Deliver it through the client's existing LMS**, per **Pattern A** — `webservice_mcp` for
   Moodle, [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) (**MIT**) for Canvas. For
   K-12 student records, [openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) (**GPL-2.0**,
   ref `master`) over its API — never linked.
7. **Prove it on the prerequisite claim specifically.**
   [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) (**MIT**) with
   [GSM8K](https://github.com/openai/grade-school-math) (**MIT**) for the multi-step maths chain.
   🟢 The honest measurement here is not a headline score: it is **whether remediating the
   prerequisite the graph identified improves the dependent topic**. That is an A/B the client has
   never been offered, and it is the whole value of the pattern.
8. **Ship the attribution notice.** §4.3 costs one line in the product's about page and the
   documentation. Put it in at step one; retrofitting a notice after a client review is avoidable
   embarrassment.

🟡 **Scope the research claim honestly.** The taxonomy's teaching-research payload
(`data/teaching-research.json`, ~24 MB) covers **1,049** topics — Science and Mathematics — and the
maintainers state that **881 topics have no research in this release**. "Research-backed guidance"
is true for roughly half the graph. Check which half a client's subject mix lands in **before** the
claim reaches a deck.

🔵 **Coverage note:** `v1` is primary/elementary and strongest on the Australian and US/UK
standards. Secondary and vocational curricula are not covered — for those, this pattern is the
*shape* to build, with the client's own map in place of the taxonomy.

**Licence posture:** client-owned code is MIT/Apache throughout. Two non-permissive components, both
held at arm's length: the **taxonomy** (ODbL, read-only input, joined never merged — §4.3 notice
only) and the **LMS/SIS** (GPL, reached over a published protocol). **Deliverable stays closed.**

---

## Pattern M — 🆕 `p385` The agent-native classroom (when the client has **no** LMS to bolt onto)

**Pattern A inverts the usual build: an agent over the client's existing LMS. Pattern M is for the
engagement where there is no LMS worth integrating** — corporate L&D, a bootcamp, a professional body,
a ministry pilot — and the deliverable is the learning loop itself, not a Moodle plugin.

**The shape.** The classroom is an **MCP server**; the agent is bring-your-own and replaceable. That
inversion is what makes it worth a pattern: the client is not buying a model, so a model swap (or a
provider outage, or a procurement decision two years out) does not invalidate the asset.

| layer | component | licence | why this one |
|---|---|---|---|
| Classroom / state | [sf-shenfeng/learn-shell](https://github.com/sf-shenfeng/learn-shell) | 🔴 AGPL-3.0 (`main`) · 🟢 MIT at `v0.1.0` | ~50 MCP tools over courses, lessons, graded exercises and a persistent learner memory. Read **Pattern L step 10 before you pick a ref** — this decision is the whole procurement question |
| Retention scheduling | [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | 🟢 MIT | learn-shell schedules flashcards with FSRS already; use the upstream parameters so retention is a published model, not a vendor claim |
| Course material ingest | [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) | 🟢 Apache-2.0 | the client's PDFs, DOCX and slide decks are the corpus |
| Grounding | [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | 🟢 Apache-2.0 | document-aware retrieval over that corpus |
| Measurement | [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | 🟢 MIT | the before/after on the client's own subject mix, which `intel/trends.md` Trend 2 makes a procurement precondition |
| Gateway / audit | [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) | 🟢 MIT | per-user quota and an audit log, which is what gets it past a DPO |

**Wiring.** The agent reaches learn-shell over MCP (JSON-RPC), exactly the boundary Pattern A uses to
stay clear of Moodle's GPL — so the agent code and the prompt/curriculum assets stay the client's.
`unstructured` → `ragflow` builds the grounding index; the agent writes lessons, exercises and
flashcards **into learn-shell** so the evidence of teaching outlives the context window; FSRS decides
what comes back and when; `lm-evaluation-harness` runs the before/after.

🔴 **Three things to say out loud in the pitch, because they are real:**
1. **AGPL reaches hosted use.** If you deploy `main` for the client as a service, the AGPL obligations
   attach to the deployment. The MIT `v0.1.0` tag avoids that and costs you every fix since
   2026-08-16. There is no third option, and this is the decision, not a detail.
2. **v1 is single-machine and unauthenticated by the maintainer's own description.** It is a pilot
   substrate. Multi-tenant auth, isolation and backup are *your* scope — budget them, do not discover them.
3. **It is one maintainer's project.** Weigh that against what it replaces: the alternative is building
   course/lesson/exercise/memory state from scratch, which is the part of this pattern nobody costs correctly.

🔵 **When NOT to use this.** If the client already runs Moodle, Canvas or Open edX, **Pattern A is
strictly better** — the learner records, rostering and gradebook already exist and integration beats
migration. Pattern M is for a greenfield loop, and its honest competitor is not an LMS but a spreadsheet.

## Pattern N — 🆕 `p386` Harden a student-side LMS MCP server into one an institution can deploy

**When to use it.** The client runs **Blackboard, D2L/Brightspace, Canvas or Moodle** and wants an
agent over it. As of `p386` there is a granted community MCP server for **every** one of those
platforms (see [`agents/top.md`](../agents/top.md#the-blackboard-and-d2l-supply-measured)) — so this
is never a greenfield build. 🔴 But **11 of the 12 granted Blackboard/D2L servers authenticate as the
signed-in student**: they ride the user's own browser SSO session, hold whatever rights that user
holds, and have no audit trail. **Licence-clean and still undeliverable.** This pattern is the gap
between the two.

**The parts.**

| role | pick | licence | why this one |
|---|---|---|---|
| Blackboard, institution-grade start | [nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp) | 🟢 MIT | The only server on these shelves that targets the **official Blackboard Learn REST API** and claims OAuth2, a role gate, FERPA handling, rate limiting, PII scrub and a JSON audit log. 🟡 Self-claims — **verify by execution before you quote them** |
| D2L start | [JhostinAleck/brightspace-mcp](https://github.com/JhostinAleck/brightspace-mcp) | 🟢 MIT | Multi-strategy auth (TOTP/OAuth/browser), retry + circuit-breaker + cache, **opt-in** writes. The nearest thing to a hardening base on D2L |
| Canvas start | [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) | 🟢 MIT | The clean default; [mdweaver](https://github.com/mdweaver/canvas-mcp) fork adds office hours and syllabus write |
| Moodle start | [onbirdev/moodle-webservice_mcp](https://github.com/onbirdev/moodle-webservice_mcp) | 🟡 GPL-3.0-or-later, header-granted | First-party route: it is in **Moodle's own plugin directory**, and the agent reaches it over JSON-RPC so GPL never reaches the agent — **Pattern A**'s boundary |
| Identity / gateway | [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) | 🟢 MIT | SSO, per-user quota and the audit log that gets a deployment past a DPO |
| Jurisdiction gate | [`intel/policy-matrix.tsv`](../intel/policy-matrix.tsv) | — | A granted licence does not make **grade write-back** lawful where you are deploying it |

**The work, in order — this is the whole deliverable.**

1. **Replace the session with a service identity.** Swap browser-session auth for the platform's
   own OAuth2 / API-key flow against a **service account scoped to the courses in scope**. If the
   chosen server cannot do this (most cannot), this step is a fork, and it is the reason the
   engagement exists.
2. **Scope by role, server-side.** Student / instructor / admin tool sets, enforced in the server,
   never in the prompt. A model that *can* call `update_grade` and is *asked not to* is not a
   control.
3. **Split read from write, and default write off.** Ship read-only first; put every mutation behind
   an explicit per-deployment flag. `JhostinAleck/brightspace-mcp`'s opt-in-writes design is the
   shape to copy.
4. **Gate grade write-back on the jurisdiction, before any code.** Several jurisdictions in the
   policy matrix gate or prohibit automated grading outright — Oklahoma and Maryland bar AI from
   high-stakes student decisions, the EU AI Act puts assessment in Annex III high-risk, Vietnam
   names automated assessment explicitly, and Illinois SB 2909 reaches *teacher* evaluation. 🔴 This
   gate decides the product's tool list, so run it in week one, not at security review.
5. **Add an audit trail that answers a DPO's actual question**: who (service identity + end user),
   which tool, which course, which record, when, and what the platform returned. Structured JSON to
   the client's existing log sink.
6. **Pin the contract, not the login page.** Pin the vendor API version and put contract tests
   around the tools you use; a student-side server breaks silently when the vendor restyles SSO.
7. **Carry the attribution the payload actually requires** — per **Pattern L step 11**. If you
   started from a fork-family server, the NOTICE file may owe **two** credits.
8. **Prove it before handover.** Execute the maintainer's claims rather than quoting them: run the
   role gate against an under-privileged token, confirm the audit record exists for every mutation,
   and confirm the PII scrub on a real transcript.

🟢 **Why this sells.** It is small, bounded, and the client can show the output to their
data-protection officer — and it is available on every major LMS today, because the licences are
already clear. 🔴 **Say the honest part too:** on D2L all six granted servers are student-side, so
step 1 there is a genuine build and should be costed as one, not as a configuration.

## Pattern O — 🆕 `p387` The LATAM engagement, built on what the region already shipped

**For:** a Brazilian or Spanish-speaking LATAM client — ministry, municipality, university or
school network — where the deliverable has to be in the local language, aligned to the *national*
curriculum, and deployable by an institution rather than demoed to one.

**The premise this pattern corrects:** the LATAM supply is not empty. Every component below is a
real address with a grant read first-hand on 2026-10-22.

**Wiring, Brazil (the fully-specified case):**

1. **Start from the national curriculum, not from a prompt.**
   [GuilhermeScarpini/agente-bncc-professores](https://github.com/GuilhermeScarpini/agente-bncc-professores)
   (**MIT**, `main`) already anchors generation to **BNCC** skill codes and **discards an invented
   code before the teacher sees it**. Keep that gate and extend it: the gate *is* the trust story,
   and it is the same mechanism `Pattern H` specifies against a curriculum graph.
2. **Deliver through the LMS the client runs, never a new portal.** On **Moodle**, the
   `webservice_mcp` plugin per **Pattern A**; on **Open edX**, start from
   [LabSirius/TutorIA](https://github.com/LabSirius/TutorIA) (**MIT**, `main`), which is already an
   XBlock/plugin with a teacher statistics panel, TTS and cross-session context.
   🔴 **Licence boundary, non-negotiable:** TutorIA's MIT grant covers *the plugin*. Open edX is
   **AGPL-3.0** and hosting it is hosting AGPL software. Keep the agent a **separate service** the
   plugin calls over HTTP, keep the plugin thin, and the client's AGPL obligations stay exactly
   where they were before you arrived.
3. **Integrate the student-record system over its API.**
   [portabilis/i-educar](https://github.com/portabilis/i-educar) (**GPL-2.0-or-later**, real default
   ref **`2.12`**) is what a Brazilian municipality is running. Read rosters and write results
   through its API; **do not fork it** — the fork pulls GPL into the deliverable and buys nothing.
   (Its sibling `i-diario` is AGPL-3.0; check per repository, not per organisation.)
4. **Make it multi-tenant before anyone calls it a pilot.** A school network is many tenants. On
   Moodle, [bycs-lp/moodle-local_ai_manager](https://github.com/bycs-lp/moodle-local_ai_manager)
   (**GPL-3.0-or-later**, in `version.php`) supplies exactly this — per-role provider routing, rate
   limits, per-tenant enable/disable, usage monitoring — and it reaches the agent over its own API,
   so the copyleft stays on the Moodle side. On Open edX, build the tenant boundary per
   **Pattern N** steps 1–5.
5. **Run it where connectivity is the constraint**, which is the actual deployment profile for
   TutorIA's own users (rural Risaralda) and for most of the nine Google.org rollout countries:
   [Kolibri](https://github.com/learningequality/kolibri) (**MIT**, default ref `develop`) per
   **Pattern D**, with a local open-weight model behind the AI manager's **Ollama** tool rather than
   a metered API.
6. **Schedule retention, in the local language.**
   [fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) (**MIT**) for the scheduler; the
   content language is a data property, not a code property, so this layer ports unchanged.
7. **Measure in the language of instruction, and publish the baseline.**
   [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) (**MIT**) with
   Portuguese/Spanish task sets built from the client's own past assessments. 🔴 Do **not** ship an
   English benchmark number as evidence for a Portuguese deployment.
8. **Say out loud what you are adding.** The agents exist and are MIT; **tenancy, support,
   governance and curriculum QA are the deliverable.** That is a defensible studio pitch and an
   honest one — and it is cheaper for the client than the rebuild a "no LATAM supply" story implies.

**Spanish-speaking variant:** swap step 1's BNCC grounding for the client's national curriculum
standard, keep TutorIA (Spanish-first) at step 2, and use
[academico-sis/academico](https://github.com/academico-sis/academico) (**MIT**, Spanish built in) or
[Chamilo](https://github.com/chamilo/chamilo-lms) (GPL-3.0) where no SIS/LMS is in place.

🟡 **Two addresses this pattern deliberately does not use, and why.**
[Daniel-ux1026/Tutor-Inteligente](https://github.com/Daniel-ux1026/Tutor-Inteligente) (Peru) is the
offline-first PWA tutor with explainable difficulty selection that step 5 would otherwise want — it
has **no grant at any of eight probed paths**, so it cannot enter a deliverable, and asking its
author to add a licence is the cheapest possible contribution to the region's supply.
[henriquebotelhogomes/educacao](https://github.com/henriquebotelhogomes/educacao) (Brazil, RAG
tutor, default ref `master`) is ungranted for the same reason.

---

## Pattern P — 🆕 `p388` The parent and guardian surface (and the FERPA line that splits it in two)

**For:** a K-12 district, school group or education provider that is being asked — by statute, by
families, or by its own board — to make a student's progress legible to parents, and an engagement
that wants a real deliverable rather than another policy PDF.

🔴 **Read this first: this is two different products, and conflating them is how the engagement
fails.** The code is the same; the obligations are not.

| | **P-1 · parent-side** | **P-2 · district-side** |
|---|---|---|
| Who holds the credential | the **parent**, for their own child | the **institution** |
| What a read is | a parent exercising their own access | a **FERPA-governed disclosure of an education record** |
| Tenancy | none needed — single user, single family | **full multi-tenant**, per-district, per-role |
| Who buys | a provider bundling it, or nobody (it is a tool, not a sale) | the district, through procurement |
| Build cost | days | the real engagement |

**Components (all verified first-hand 2026-10-22 — [`verified-repos`](../evidence/verified-repos.2026-10-22-p388.tsv)):**

- **Infinite Campus (SIS):** [chrischall/infinitecampus-mcp](https://github.com/chrischall/infinitecampus-mcp)
  — `main` · `971d58f`, 🟢 **MIT** (1,067 B), **47 npm releases → 2026-10-19**. 20 tools over **Campus
  Parent**: schedule, assignments (`missingOnly`), grades plus a 14-day recent window, **attendance
  events with codes and comments**, behavior, food service, documents, standardized **assessment
  scores**, fees, and messaging from three distinct sources. Linked districts auto-discovered via
  **CUPS SSO**; `FeatureDisabled`-aware, so a district with a module switched off degrades instead of
  erroring — which is what makes it deployable across a group of districts rather than one.
- **Canvas (LMS):** [chrischall/canvas-parent-mcp](https://github.com/chrischall/canvas-parent-mcp)
  — `main` · `428b78b`, 🟢 **MIT** (1,067 B), **43 releases → 2026-10-16**. 18 `canvas_*` tools held
  to the **read-only observer scope** (`canvas_list_observees` is the hinge), plus student
  self-access. Four auth modes in priority order. 🟢 Copy its download hardening rather than
  re-inventing it: host-pinned to the Canvas origin, confined to a download directory, never writes
  through a symlink, new files `0600`.

### Wiring P-1 (parent-side) — days, not weeks

1. Parent installs the MCP server locally against **their own** portal credential (token, OAuth, or
   session). Nothing is hosted; no institutional agreement is needed because no institutional
   credential is used.
2. Keep it **read-only**. Both servers are already scoped that way; do not add write tools. A parent
   agent that can submit work on a child's behalf is an academic-integrity incident waiting to be
   filed.
3. Add a **digest** rather than a chat surface: *"what changed this week, what is missing, what is
   due."* 🔵 The persona's actual job is **noticing**, not conversing — the portal already answers
   questions, badly, and nobody logs in.

### Wiring P-2 (district-side) — the real engagement

1. 🔴 **Do not host the parent-side tool for the district.** The moment the credential is
   institutional, every read is a FERPA disclosure. Build the institutional path deliberately:
2. **Put the district's own identity in front of it.** Parent identity comes from the district IdP,
   and **the parent↔student relationship is authoritative from the SIS** — never from a claim the
   agent accepts. `ic_list_students` / `canvas_list_observees` define the blast radius of the whole
   system, so that relationship check is the security boundary, not a feature.
3. **Borrow the tenancy layer that already exists.** This is the same problem `p386` identified for
   student-side LMS servers, and `Pattern A`'s answer applies unchanged: per-tenant configuration,
   per-role rate limits and usage monitoring — on Moodle,
   [bycs-lp/moodle-local_ai_manager](https://github.com/bycs-lp/moodle-local_ai_manager) is the
   worked example to copy the *shape* of.
4. **Log every read as a disclosure, not as a request.** Who asked, for which student, which fields,
   under which relationship, at what time. 🔵 This log is the deliverable a district's counsel signs
   off on, and it is cheap to build on day one and near-impossible to retrofit.
5. **Keep the model away from the record where you can.** Fetch and render deterministically;
   use the model for **summary and prioritisation over data already authorised**, not as the thing
   that decides what to fetch. Smaller surface, smaller disclosure, cheaper review.
6. **Ship the translation layer — it is the actual product.** Gradebook rows are not an answer to
   *"is my kid okay?"* Convert to plain language, in the family's language, at a reading level the
   district specifies, with **no inference about the child beyond what the record states**. A tool
   that volunteers *"your child seems disengaged"* has invented an education record.

**Guardrails:**
- 🔴 **No predictions, no risk scores, no labels.** A parent-facing risk score about a student is
  the high-stakes automated decision Oklahoma and Maryland's frameworks are written to restrain, and
  under the EU AI Act Annex III it is squarely high-risk. Report the record; do not score the child.
- 🔴 **Attendance, behavior, food-service and fee data are the sensitive tail.** `infinitecampus-mcp`
  exposes all four. Free-lunch status and behavior records are the fields a district will refuse last
  and worry about most — scope them out explicitly unless the district asks for them in writing.
- 🟡 **Both servers authenticate as a person.** Treat credential custody as the top risk in the
  design review; a stored parent credential in a studio-hosted service is the worst of both worlds.
- 🔵 **Multiple children, multiple districts.** `ic_list_districts` + CUPS SSO exist because families
  span districts. Test the two-children-two-districts case before a demo; it is the common case and
  the one that breaks naive implementations.

**Why this pattern is worth having at all:** it is the only education surface this base has found
with **granted, maintained components and no incumbent vendor** — the parent portal is a feature of
the SIS, not a market. And **family transparency is already in the statutes** (Oklahoma SB 1734
names it; Maryland's Chapter 634 is built on guidance districts hand down), so the buyer has an
obligation and no product. 🔵 See `Trend 10` in [`intel/trends.md`](../intel/trends.md).

---

## Pattern Q — 🆕 `p389` The generated classroom, governed (and what it supersedes in `Pattern M`)

**For:** a client with **no usable LMS** — a corporate academy, a ministry training programme, a
vocational provider, a new institution — who needs **teachable lessons in weeks, not a platform in
quarters**. Also the fastest credible answer to the EMEA teacher-training demand recorded in
[`intel/market.md`](../intel/market.md): the UAE has **22,000 teachers and education professionals**
to train on a curriculum that became compulsory by Cabinet decision.

**The base:** [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) — 🟢 **MIT** (read from the
payload at `main` @ `269fde2d991f`; `package.json` agrees), Tsinghua University, **committed
2026-10-22**, ~41.3k ★, **JCST 2026** paper, grown out of the internal **MAIC** system and validated
on **700+ students**. 🔴 **Pin `v1.2.1` (2026-10-18), not head.** Head is `v1.3.0-rc.1`, and the
project states breaking upgrade conditions with **no rollback below that release** — a pilot does not
want to be the first to find that out.

### Wiring

1. **Stand up the authoring server.** Node ≥ 22.19, pnpm ≥ 10, **PostgreSQL 16**, a long-running
   server (🔴 **not Vercel** — Vercel deployments are capped at the 1.1.x line, so "we'll host it
   serverless" is a downgrade). Generation is **server-first** from v1.2.0: it survives closed tabs and
   restarts, which is what makes it usable by teachers rather than by engineers.
2. **Write the governance file first, before any content.** `openmaic.yml` declares **providers** and
   assigns every AI use — a named **slot** (`llm`, `course.outline`, slide content, TTS, web search,
   `video`) — to one of them, with keys referenced as `${VAR}` from `.env.local`. 🟢 **Three settings
   are the compliance deliverable, not configuration:** pin each slot to the provider under the
   client's own contract; set the server to **forbid user-supplied keys**, so no teacher can route
   student work through an unvetted account; and set unused capabilities to `null` rather than leaving
   them available. 🔵 **This file is the artefact that answers a district's or ministry's AI policy
   question** — *which model saw student input, under whose contract* — in one reviewable, diffable
   page. Almost nothing else in this base can answer it at all.
3. **Ground the content in the client's curriculum, not in the model.** Feed the jurisdiction's own
   material through the **knowledge base** (v1.3.0 line) or as per-course uploads — parsed once and
   reused — and where a standards graph exists, drive the lesson plan from it rather than from a
   prompt: [`os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) (🔴 **ODbL-1.0 — a database
   licence; reach it over a service, do not fork it into the deliverable**, per `Pattern H`), or
   [`bc-curriculum-mcp-server`](https://github.com/pdg6/bc-curriculum-mcp-server) (**MIT**) for a
   North American engagement — 🟡 whose crawl is **209 days** old, so budget the re-crawl its MIT grant
   permits.
4. **Keep the record of record outside it.** 🔴 OpenMAIC has **no enrolment, no gradebook of record,
   no transcripts and no stated LTI story**. Pair it with the administration base the client already
   runs or should: [openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) (GPL-2.0, over its API),
   [academico](https://github.com/academico-sis/academico) (**MIT**) at SME scale,
   [i-educar](https://github.com/portabilis/i-educar) (ref `2.12`) for Brazilian municipal work, or
   [OpenEduCat](https://github.com/openeducat/openeducat_erp) (LGPL-3.0) where an ERP is wanted.
   **Completion and scores flow out of OpenMAIC into that system; identity and enrolment flow in.**
5. **Add the mastery model it does not have.** Quiz results are events, not a mastery estimate. Fit
   [`pyBKT`](https://github.com/CAHLR/pyBKT) (**MIT**, 1 d) on the quiz log per skill, as in the
   revised `Pattern B`, and use it to choose the next lesson. 🟢 This is also what keeps the
   high-risk-assessment line on the right side: the progression decision becomes **a published model
   plus a human review step**, not a generation.
6. **Deliver to the edge as files.** Export each finished classroom as **one offline HTML file** (or
   PPTX). See `Pattern D` — authoring stays central, delivery needs only a browser.
7. **Run the models where the data has to stay.** **Lemonade** for local inference and **FunASR** for
   local ASR are supported paths, not forks — so a deployment that may not send audio or text
   off-premises is a configuration change.

### Why this supersedes `Pattern M` for institutional delivery

`Pattern M` is built on [learn-shell](https://github.com/sf-shenfeng/learn-shell), whose v1 is
explicitly **single-machine and unauthenticated**, and whose grant is **AGPL-3.0 at `main`** (MIT only
at tag `v0.1.0`). That is a fine shape for an individual learner and an impossible one for an
institution. OpenMAIC is **MIT at head**, server-first, multi-user, with central model governance and
a published security practice — five releases since September 2026 carrying SSRF, DNS-rebinding,
token-expiry and provider-redirect fixes under **GHSAs**. 🔵 **Keep `Pattern M` for the
bring-your-own-agent, one-learner case; use `Pattern Q` whenever a client is the buyer.**

### Guardrails

- 🔴 **Auto-graded quizzes are the regulated surface.** Assessment is **Annex III high-risk** in the
  EU and named explicitly in **Vietnam's Decision 33/2026/QD-TTg**. The trigger in both is a decision
  taken on the system's output **without meaningful human review**, so ship the human review step for
  anything consequential and keep its audit trail. A practice score is not consequential; a module
  pass that gates progression is.
- 🔴 **Simulated classmates must be labelled.** An AI teacher with a voice and AI peers in a classroom
  is exactly the surface **EU AI Act Art. 50** transparency and China's labelling rules address, and
  `Pattern G` already covers the mechanics. Label in the UI, not in the terms of service.
- 🟡 **Generated content is a draft until a teacher signs it.** The 2026 procurement trend is evidence
  of instructional benefit; a lesson nobody reviewed cannot be put in front of a class at a client's
  reputational risk. Make teacher review a workflow state, and bill it — it is the part of the
  engagement that is actually about teaching.
- 🟡 **Language and regional fit:** interface is **EN + zh-CN** and the provider catalogue is built for
  a market that includes DeepSeek and Kimi. For a Gulf or LATAM engagement, **localisation of the
  teaching surface is a line item**, and there is no Arabic-first alternative in the open-source supply
  (see `intel/market.md`, EMEA).

---

## Pattern V — 🆕 `p390` The spoken tutor, and the two things that make or break it

**For:** learners who cannot or will not type their way through a lesson — early grades, low typing
fluency, shared-device households, visually impaired learners, and language learning where
*pronunciation is the skill being assessed*. This is also the pattern that reaches the LATAM and
APAC households `Trend 10` describes, where the phone is the only device.

**Why it is a separate pattern:** a voice tutor is not a text tutor with TTS bolted on. Two
properties decide whether a child keeps talking to it, and neither is in the LLM:

1. **Turn-taking.** The tutor must know when the learner has stopped speaking, tolerate a
   four-second pause while a 9-year-old thinks, and **stop talking the moment it is interrupted**.
2. **Latency budget.** Past roughly a second of silence the learner starts talking over it, and the
   session degrades into collision recovery.

**Wiring:**

1. **Do not write the voice loop.** [`livekit/agents`](https://github.com/livekit/agents)
   (🟢 **Apache-2.0**, dated 2026-10-22) is the substrate: full-duplex WebRTC transport, pluggable
   STT/LLM/TTS, **turn detection, interruption and barge-in handling**. All three legs are
   provider-swappable, which is what makes step 4 possible.
2. **Start from the working reference.** [`Jeanikt/tutor-ai-agent`](https://github.com/Jeanikt/tutor-ai-agent)
   ("Manu", 🟢 **MIT**, dated 2026-10-07) is a pt-BR maths tutor on exactly that substrate, scaling
   its explanation from 1st grade to university. 🔴 Its README says **"in development" with no public
   deployment** — take the pipeline and the prompt-scaffolding, not a production claim.
3. 🔴 **Put a symbolic checker behind any arithmetic.** Manu's correctness layer is the LLM itself.
   For a maths tutor that is the one unacceptable gap: route every numeric or algebraic claim through
   SymPy (or the client's own CAS) and have the agent *read back* the verified result. A spoken wrong
   answer is harder for a learner to catch than a written one — there is no transcript to re-read.
4. **Localise the ASR, not just the prompt.** Accent and dialect coverage is where regional voice
   tutors fail. [`mozilla/common-voice`](https://github.com/mozilla/common-voice) ships **CC0-1.0**
   corpora across ~130 language variants (pt-BR, es-419 variants, Hindi, Bengali, Kiswahili) — use
   them to *evaluate* candidate ASR models on the client's actual learner population before picking
   one, and to fine-tune where the gap is real. 🟢 CC0 means no attribution and no share-alike, so
   this is safe in a commercial deliverable. 🟡 MPL-2.0 covers the **platform code**, not the corpora.
5. **Keep the mastery model outside the voice path.** Voice is an I/O channel, not a pedagogy.
   [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) (🟢 MIT, dated 2026-10-22) holds the Bayesian
   Knowledge Tracing state so "what comes next" survives a dropped call and stays inspectable — which
   is also what makes the decision auditable under step 6.
6. 🔴 **Voice raises the compliance stakes, so settle three things before the pilot.**
   - **Biometrics.** A voice recording is biometric data under GDPR Art. 9 and most LATAM regimes
     (Brazil's LGPD included). Default to **transcribe-and-discard**, keep no audio unless the client
     has a lawful basis and a retention policy, and write that down.
   - **Emotion inference is prohibited in EU education** (AI Act, in force since 2 Feb 2025) — and
     voice is the modality vendors are most tempted to infer affect from. Do not ship it in EMEA,
     and strip it from any upstream SDK feature you enable.
   - **Disclosure.** AI Act Art. 50 applies from **2 Aug 2026**: a synthetic voice must be
     disclosed as synthetic. Say it in the first turn, in the learner's language, every session.
7. **Measure it as a tutor, not as a demo.** Score the *transcripts* with
   [`EleutherAI/lm-evaluation-harness`](https://github.com/EleutherAI/lm-evaluation-harness)
   (🟢 MIT) on the client's own item bank, and track interruption rate and mean response latency
   alongside learning gain — a tutor that is pedagogically right and 1.5 s slow will still be
   abandoned.

**Licence position:** Apache-2.0 substrate + MIT reference + CC0 data + MIT mastery model — the whole
chain is permissive, so this pattern can ship as a closed client deliverable with attribution only.

**What this pattern does not solve:** there is **no granted, maintained open-source voice tutor for
an African or South Asian language** on these shelves. See `Gap 390-A`.

## Pattern W — 🆕 `p391` Qualify the district *before* the pitch (North America)

**For:** a North America K-12 engagement, at the stage before anyone has written code — choosing
which districts to approach, and pricing a pilot against a budget that actually exists. Every other
pattern here answers *what to build*; this one answers *for whom, and with whose money*.

**Why it is a pattern and not a sales note:** US school AI spending is not discretionary in the way
enterprise AI spending is. It comes from identifiable federal, state and local lines, and the
largest flexible federal line — **Title I** — is allocated on **Census child-poverty counts**, not
on enrolment. A pilot proposed without that number is priced blind, and a district with a high
poverty count and a low per-pupil spend is a different conversation from the inverse.

**Wiring:**

1. **Pull the universe.** [`pipeworx-io/mcp-education-data`](https://github.com/pipeworx-io/mcp-education-data)
   (🟢 **MIT**, HEAD 2026-10-21) — `education_find_districts` for a state returns every local
   education agency with its **LEA id**, school count, enrolment and teacher counts. The `leaid` is
   the join key for everything below.
2. **Add the budget.** `education_district_finance` on that `leaid` returns revenue split
   **federal / state / local** and expenditure by function, with **per-pupil spending computed**.
   🔴 **The survey lags the directory by 1–2 years** — quote it as "FY-whatever per-pupil", never as
   current-year, or the first CFO in the room ends the meeting.
3. **Add the federal lever.** `education_child_poverty` returns Census **SAIPE** counts and rates of
   children 5–17 in poverty by district — the figures Title I formulas run on. High poverty rate plus
   low per-pupil spend identifies districts with *federal* money and *no* incumbent vendor: the
   cheapest pilot to land and the hardest to displace later.
4. **Add the surface.** `education_find_schools` carries **charter/magnet status, grade range and
   free/reduced-price lunch counts** per school, so the pilot can be scoped to named schools rather
   than to a district abstraction.
5. **Then pick the build.** Hand the shortlist to whichever pattern fits the client's platform —
   `Pattern F` (teacher-facing, the one the market and the regulator agree on) is the usual answer at
   this budget, `Pattern N` if they run an LMS already.

🔴 **Three things to decide before the first call, not after.** The integration is **unofficial** and
not affiliated with the upstream provider — fine for your own targeting, not something to resell as a
data product. The default path is a **hosted gateway** (`gateway.pipeworx.io`): the underlying data is
public federal data, but the **query pattern is not** — which districts a studio is sizing up is
commercially sensitive, so self-host before running this against a named client list. And a scoped
endpoint lists roughly **30 shared gateway meta-tools** alongside the four that matter, so budget the
context or connect once to the full gateway rather than to several pack endpoints.

🔵 **Regional honesty.** This is a **North America–only** instrument: it is NCES/Census data and has
no EMEA, APAC or LATAM analogue on these shelves. The equivalent question in those regions is still
answered by hand — recorded as `Gap 391-B` rather than left to look like coverage.

## Pattern X — 🆕 `p391` Keep the client's pedagogy as a separate, reviewable artefact

**For:** any tutoring engagement that will be audited, handed over, or argued about — which, under
EU AI Act high-risk obligations and most North American district procurement, is all of them. Also
the pattern for a studio that wants the *teaching* it built to outlive the *runtime* it shipped on.

**Why it is a separate pattern:** in nearly every tutor on these shelves, the pedagogy is diffused
through the application — prompt fragments, conditional branches, UI copy. That makes two things
expensive that clients ask for routinely: *show me the teaching policy* and *change the teaching
policy without a release*. [`SenmuuuuW/dsh-diagnostic-tutor`](https://github.com/SenmuuuuW/dsh-diagnostic-tutor)
(🟢 **MIT**, HEAD 2026-10-21) is the first row here built the other way round, and it is worth copying
even where the repository itself is not used.

**The split, which is the whole point:**

| | owns | where it lives |
|---|---|---|
| [`universal-diagnostic-tutor-skill`](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) (🟢 **MIT**, → 2026-09-24) | **what to teach next**: diagnosis, teaching moves, pacing, when a check is passed, what the next step is | its own repository, versioned independently |
| [`dsh-diagnostic-tutor`](https://github.com/SenmuuuuW/dsh-diagnostic-tutor) (🟢 **MIT**) | **where it is kept**: learner state, the diagnosis map, structured lessons, the UI | the runtime, which contains **no teaching logic at all** |

**Wiring:**

1. **Put the pedagogy in a versioned repository of its own**, as prose and rules rather than code:
   diagnosis strategy, teaching moves, mastery criteria, escalation. This is the artefact a client
   reviews, a subject expert edits without a developer, and an auditor reads **without reading the
   application**. It is also the thing a studio can hand over at the end of an engagement.
2. **Make the runtime record decisions, never make them.** The runtime stores what the teaching layer
   decided and renders it; every pedagogical choice arrives from the policy artefact. Test this by
   grepping the runtime for teaching rules — if `if blocked, explain the prerequisite` lives in the
   application, the separation has already leaked.
3. **Put the assessment behind a pure function.** [`intellectif/learning-kit`](https://github.com/intellectif/learning-kit)
   (🟢 **MIT**, HEAD 2026-10-18) — `@intellectif/lk-core` gives schemas, a **pure scoring engine**,
   **rubric and deferred grading**, attempt plans and redaction, with no runtime dependency beyond
   Zod. Scoring that is a pure function is unit-testable by the client and readable by a regulator;
   **deferred grading keeps a human marker in the loop by construction**, which is what high-risk
   assessment obligations ask for rather than something to retrofit.
4. **Emit evidence, do not hoard it.** `lk-core`'s **xAPI builder** sends statements to the client's
   own LRS — [`EscolaLMS/LRS`](https://github.com/EscolaLMS/LRS) where one is needed — so the learning
   record stays the client's property and the tutor stays replaceable.
5. **Launch it from the LMS over a maintained LTI edge.** [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs)
   (🟢 **Apache-2.0**, npm v7.0.7) in front of the agent — see the `Pattern A` note and `Gap 391-A`:
   the Python LTI library is 1,431 days stale, so the edge is Node or PHP regardless of what the agent
   is written in.

🔴 **What this pattern does not give you.** `dsh-diagnostic-tutor` is **v0.1.1 and early by its own
account**: no PDF or document ingestion, no RAG, no flashcards, no analytics, and **a route never
marks knowledge as mastered**. It also **requires DeepSeek Harness** — it is a harness extension, not
a standalone application, so an engagement that cannot adopt that harness should copy the *structure*
(steps 1–2) onto a tutor it can deploy, not adopt the repository. 🟢 Take the separation; shop for the
runtime.

## Pattern L — Clear a repository for reuse by **subtree**, not by its licence badge

**The one durable result of the `p3xx` apparatus**, kept as a procurement gate rather than a
narrative. Run it before any repo enters a client deliverable.

1. **Resolve the real default ref first.** `git ls-remote --symref https://github.com/<slug> HEAD`.
   **13 of 58 live addresses verified in `p383` are not on `main`** — `master`, `develop`, `dev`,
   `release`, `development`, `release_11`, and OpenEduCat's `19.0`; `p384` adds **openSIS-Classic
   → `master`**. A `main`-assuming read reports "no licence" for every one of them, and that false
   negative looks exactly like a real one.
2. **Probe more than one path — eight, not seven.** In order: `LICENSE`, `LICENSE.md`,
   `LICENSE.txt`, `LICENCE`, `COPYING`, `LICENSE-MIT`, `license`, and 🆕 **`docs/License.txt`**
   (with `doc/LICENSE` as its variant). Verified instances where the grant is *not* at `LICENSE`:
   **Moodle → `COPYING.txt`**, **Frappe LMS → `license.txt`** (lowercase),
   **ai-shifu → `LICENSE.txt`**, **lm-evaluation-harness → `LICENSE.md`**,
   **H5P → `LICENSE.txt`**, and 🆕 **openSIS-Classic → `docs/License.txt`** (17,286 B, stock
   GPL-2.0, *"Version 2, June 1991"*, corroborated by `"version 2 of the License"` headers in
   `index.php` and `Modules.php`). 🔵 `p384` added the eighth path because the seven-path read
   returned "ungranted" for **the most widely deployed open-source SIS in K-12** — a repository with
   a perfectly ordinary grant sitting one directory down.
3. **Check for a split grant.** **[microsoft/autogen](https://github.com/microsoft/autogen)**: root
   `LICENSE` is **CC-BY-4.0** (18,649 B, "Attribution 4.0 International"); the **code** grant is a
   separate file, `LICENSE-CODE` = **MIT**. One file read gives you the wrong answer either way.
   Conversely, confirm a split grant is **absent** before assuming one:
   [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) has **no** code grant —
   `LICENSE-CODE`, `LICENSE.code`, `CODE_LICENSE` and `licenses/LICENSE` all **404** — so its ODbL
   is the only grant on offer, for the tooling as well as the data.
4. **Compare byte length against the stock text.** A licence whose length is off is a licence that
   was edited. **[open-webui/open-webui](https://github.com/open-webui/open-webui)**: `LICENSE` is
   **2,819 B** against stock BSD-3's ~1,500 B — BSD-3 text **plus** a branding restriction and a
   CLA, self-titled "Open WebUI License". Not an OSI-standard grant.
5. **Read the manifest and the source headers before you call anything ungranted.** 🔴 **`p383`'s
   own first draft failed this step and `gate-enumeration` refused it.** Five repositories had no
   licence file at any of the seven paths; only **two** turned out to be ungranted.
   `DMontgomery40/mcp-canvas-lms` and `general-mudkip/d2l-mcp-server` declare
   `"license": "MIT"` in `package.json` (**manifest-only** — reusable, but record the line and ask
   for the file). `onbirdev/moodle-webservice_mcp` carries the full **GPL-3.0-or-later** header in
   `version.php`, as Moodle requires of every plugin — **granted, with no licence file at all.**
   Probe `package.json`, `pyproject.toml`, `composer.json`, the `README`'s licence section and the
   main source file's header before rejecting a repository;
   🆕 `p385` — **but read what that section *says*, not that it *exists*.** Two failure modes, both on
   these shelves: [moarshy/mcp-tutor](https://github.com/moarshy/mcp-tutor) has a `## License` heading whose
   entire body is *"This project is experimental and intended for educational and research purposes"* —
   which grants **nothing**, while satisfying any check that asks "is there a licence section?";
   [h9-tect/AI-Roadmaps](https://github.com/h9-tect/AI-Roadmaps) states *"provided under the
   [MIT License](LICENSE)"* and **that `LICENSE` link 404s**. A prose assertion is weaker evidence than a
   manifest field, which is weaker than the text itself — grade them separately and never as "MIT"; a file-only read would have wrongly
   rejected three of five, including the plugin Moodle's own directory distributes.
6. **Only now treat "no licence" as a hard stop — and it is a hard stop.** Two live, functional,
   actively advertised repositories survive every check above with no grant anywhere:
   `loyaniu/moodle-mcp` (no `license` field in `pyproject.toml` either) and
   `Seechange-edu/act-ai-tutor-backend` (no manifest at all). 🔵 Both were **re-probed at the new
   eighth path in `p384` and remain ungranted.** No grant means no right to redistribute, whatever
   the README invites you to do.
7. **Ask what the grant covers, not just what it is.** A valid, unmodified, correctly-recognised
   licence can still leave the part you are shipping ungranted — stock **ODbL** governs a database's
   *rights*, by its own preamble **not the contents of the database individually**. If you ship
   derivatives of the *contents* on the strength of "licence: ODbL-1.0", you have no grant for the
   part you shipped. Record the answer **per subtree** (`data/`, `docs/`, `scripts/`), and record
   "not stated" as distinct from "not granted".
   🟢 🆕 **This step was written abstractly in `p383`. `p384` gave it its first real instance** —
   `os-taxonomy`, ODbL, no code grant — and the concrete reading is now **Pattern H** below. The
   step was right in advance, which is reason to trust it on the next data artefact: education runs
   on standards, item banks and curriculum maps, so this will not be the last one.
8. **Re-check dead addresses.** Four in common circulation do not resolve: `apereo/opencast`,
   `edx/openassessment`, `openedx/openassessment`, `OpenEduCat/OpenEduCat`. Live replacements in
   [`repos/foundations.md`](../repos/foundations.md).
9. 🆕 **Confirm there is a *tree*, not just a *ref*.** `git ls-remote` on
   [projectfedena/fedena](https://github.com/projectfedena/fedena) returns two heads — and every
   content path at `master` (`README`, `README.md`, `LICENSE`, `Gemfile`, `app`) returns **404**.
   **`ls-remote` proves a ref, not a payload**, so step 1 can pass on a repository that has nothing
   in it to licence. A vendor article lists this slug as an Apache-2.0 SIS; the correct record is
   **"nothing read"** — neither granted nor ungranted. Any address census built on resolution alone
   over-counts the supply.

10. 🆕 **Read the grant at the ref you are shipping — the licence is a property of the *ref*, not of the
    repository.** [sf-shenfeng/learn-shell](https://github.com/sf-shenfeng/learn-shell) is **AGPL-3.0** at
    `main` (`LICENSE`, 34,523 B, stock) and **MIT** at tag **`v0.1.0`** (`LICENSE`, 1,081 B,
    *"Copyright (c) 2026 Learn Shell contributors"*). Both were read first-hand in `p385`; the project
    relicensed on **2026-08-16**. 🔵 This base already knew relicensing happens —
    `snflwr-ai/snflwr.ai` went AGPL-3.0 → proprietary (`p241`), `AIHawk` went MIT for releases after a date.
    What `p385` adds is the **direction that favours the buyer**: permissive → copyleft, with the permissive
    grant **still retrievable at a tag**. 🔴 The trap in both directions is a cached audit. "We cleared that
    repo as MIT last quarter" is a statement about a ref that has moved. Record **slug + ref + licence +
    date-read**, never slug + licence — and re-read before each release, not once per engagement.
    🟡 And when you pin a tag to keep a permissive grant, say out loud what it costs: a frozen tree, no
    upstream fixes, and a maintainer who has signalled they do not want that code used on those terms.

11. 🆕 `p386` **Classify a byte-length anomaly before you judge it — "longer than stock" has two
    opposite meanings.** Step 4 says a non-stock length means the text was edited. True, and `p386`
    found the benign half of that read, which a length check alone cannot distinguish from the
    hostile one:

    | repo | bytes | the excess is | what you do |
    |---|---|---|---|
    | [open-webui/open-webui](https://github.com/open-webui/open-webui) | 2,819 (BSD-3 ≈1,500) | 🔴 **added restriction** — branding clause + CLA | walk away, or get written permission |
    | [AnonymousOnyx22/brightspace-d2l-mcp](https://github.com/AnonymousOnyx22/brightspace-d2l-mcp) | 1,200 (MIT ≈1,065) | 🟢 **added attribution** — inline notice, *"Portions … derived from brightspace-mcp-server, Copyright (c) 2026 Rohan Muppa, used under the MIT License"* | ship it, carry the extra notice |
    | [RobertLMcCrary/D2L-MCP](https://github.com/RobertLMcCrary/D2L-MCP) | 2,181 | 🟢 **two complete MIT grants concatenated** — its own plus `d2l-cli`, © 2026 Aaryan Kapoor | ship it, carry **both** notices |
    | [apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) | 11,906 (Apache-2.0 ≈11,358) | 🟢 **ASF's appended notice text** | ship it, keep `NOTICE` |

    🔵 **So the test is not "is the length stock?" but "does the delta add a condition or a
    credit?"** Added conditions are procurement stops. Added credits are NOTICE-file entries — and
    they are *obligations you inherit silently*: ship `D2L-MCP` and you owe attribution to a project
    you never chose, which no SBOM built from a licence **identifier** will tell you.
    🟡 Record the delta's content, not just the byte count.

12. 🆕 `p386` **Count grants, not addresses — and never let a count of zero reads print as
    "ungranted".** For four passes [`agents/top.md`](../agents/top.md) said *"Blackboard has nine
    servers and not one verified grant; D2L has six and the only one checked is ungranted"*, and
    concluded both platforms needed a permissive server built. `p386` probed all fifteen: **6 MIT on
    Blackboard, 6 MIT on D2L**. 🔴 The grants existed; the reads did not. A harvest column headed
    *"distinct slugs"* answers **how many addresses exist**; `LIVE-GRANTED` / `LIVE-NOGRANT` answers
    **how many were read**. When the second number is zero the honest word is **unread**, and the
    cost of the wrong word here was a false build recommendation on two platforms.
    🔵 Before any shelf states a supply gap, state which census it is quoting.

13. 🆕 `p387` **Date the artefact you are about to ship, in the registry.** A grant tells you whether
    you *may* use it; a publish date tells you whether anyone is still there. Read the package name
    from the manifest at the real default ref, then:
    `curl -s https://registry.npmjs.org/<name>` → `dist-tags.latest`, `time.created`,
    `time.<latest>`, `versions.<latest>.license`, `.repository`; or
    `curl -s https://pypi.org/pypi/<name>/json` → `info.version`, `info.license`,
    `releases[*].upload_time`. 🟢 Three usable outputs: a **second, independently published grant**
    (a manifest-only MIT becomes an MIT published to a registry); a **maintenance date** that
    survives `api.github.com` being 403; and the discovery that an address ships **no artefact at
    all**, which is a different conversation with a client than "it is old". 🔴 `p387` found a
    four-and-a-half-year-stale dependency inside a pattern on this page, a 16-month-stale server
    recommended for its tool count, and an "institution-grade" server with no release.

14. 🆕 `p387` **A manifest's package name is not proof of a publication — match the registry back to
    the slug.** [faizan45640/google-classroom-mcp-server](https://github.com/faizan45640/google-classroom-mcp-server)
    declares the npm name **`class`**, and npm's `class` is an unrelated **2013** package by
    `deadlyicon`. Keyed on the name alone, a recency sweep would have printed *"MIT, published
    2013-08-15"* onto a Google Classroom row. 🟢 **The check:** accept a registry row only when its
    `repository` field — or the links in its description — point back at the same slug; otherwise
    record `NOT PUBLISHED` and say so. The same check collapses fork families for free: four
    Blackboard addresses declare `blackboard-mcp` and **one** publication exists, its `repository`
    naming `felipedias-ie`; `mdweaver/canvas-mcp` carries upstream's scoped name
    `@r-huijts/canvas-mcp`. **Count the artefact, not the slug.**

11. 🆕 `p388` **If the repository is unreadable, read the *artefact*. The manifest is a claim; the
    tarball is the evidence.** `git ls-remote` distinguishes two states a 404 conflates: a
    **credentials prompt means the repository exists and is closed**, not absent. For such a package
    — and **6 of 32 addresses probed in `p388` are in this state while publishing to npm
    normally** — the published tarball is still readable and is **the licence that actually ships**:
    ```
    curl -s https://registry.npmjs.org/<pkg> | jq -r '.versions[.["dist-tags"].latest].dist.tarball'
    curl -s <tarball> | tar -tz | grep -i -E 'license|copying'      # is a grant shipped at all?
    ```
    🔴 **This is how `p388` established that a major publisher's tutoring SDK is ungranted.**
    `@santillana-ai/typescript-tutor-sdk` — **115 published versions** — has **no `license` field in
    `package.json`**, **no licence file anywhere in its 896,006-byte tarball**, and **no `repository`
    field at all**; its sibling scaffolder claims `"license": "MIT"` in the manifest while shipping
    **no licence file either**. Neither the repo (private) nor the badge (absent) could have settled
    it; the artefact did.
    🔵 **Three sub-rules:**
    **(a)** A manifest reading **`"SEE LICENSE IN LICENSE"` that points into an unreadable
    repository is not a grant** — it is a circular reference
    — [ale-alejandro/beadkit](https://github.com/ale-alejandro/beadkit) is the worked example, and 🆕 `p390` re-confirmed its repository is **still unreadable**, so the circle is still closed.
    **(b)** Steps 1–10 clear a repository **by subtree**; when there is no readable subtree, *this*
    step is the only one available, and it can only ever yield 🟡 manifest-only or 🔴 ungranted —
    **never a clean clearance**.
    **(c)** 🔴 Check **which** package in a scope carries the grant. Here the MIT claim sits on the
    *scaffolder* and the **dependency a client's code would actually import carries nothing**. Read
    the licence of the package you will `import`, not of the one you will `npx` once.

**Channel note, so this is reproducible:** `curl -sI https://github.com/...` returns **403** through
this sandbox's agent proxy and `api.github.com` returns **403**. `git ls-remote --symref` and
`raw.githubusercontent.com` both work, and together they are a stronger check than a HEAD request —
one proves the address and its real ref, the other reads the grant itself.

🟢 🆕 `p389` **Step 11, and it makes steps 1–10 one command.** A **blobless shallow clone** does the
whole gate in ~1.2 s, from the payload, with no API and no credentials:

```bash
git clone --depth 1 --filter=blob:none --no-checkout https://github.com/&lt;owner&gt;/&lt;repo&gt; r
git -C r symbolic-ref --short HEAD    # the real default ref (step 1)
git -C r ls-tree --name-only HEAD     # is there a LICENSE at all, and where (steps 2-3)
git -C r show HEAD:LICENSE            # the grant text itself (step 4)
git -C r show HEAD:package.json       # the manifest that must agree with it (step 5)
git -C r log -1 --format='%H %cI'     # ← NEW: who still works on this, and when
```

🔵 **Why the last line belongs in a procurement gate and not just in a research note.** The gate has
only ever answered *may we use this*. It now also answers *will we be alone on it* — and the two
produce different estimates. **A permissive grant plus an eight-month-old HEAD is a vendoring
decision with a maintenance line**, which is precisely the call this base made for `pybryt` after
reading a *registry* date; the clone reads it for any repository, published package or not. 🟡 Read
the date against the artefact: a release branch can trail a default ref
([instructure/canvas-lms](https://github.com/instructure/canvas-lms), `master` **175 days** behind its
moving `stable/*` branches), and a finished specification is not decaying. 🔴 And the limit: this
channel gives no stars, forks or releases, and `api.github.com/search/*` stays **403**, so
**discovery** remains web search and package registries. Only **verification** is first-hand.
