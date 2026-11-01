---
industry: education
region: Global
updated: 2026-11-01
---
## 🆕 p590 — 2026-11-01 — the courseware-emit recipe is rewritten around a generator this base already held, and the xAPI telemetry leg gets named libraries instead of a bare "send statements" step

🔵 **Why these two patterns change.** `p589` told a courseware engagement to **build the
generator** because only two permissive SCORM emitters were alive. 🔴 **That is refuted**
(`589-E`, [`../repos/trending.md`](../repos/trending.md)): there are at least six, one of
them a finished multi-format exporter under BSD-3-Clause. 🟢 **Every component named below
was measured first-hand `2026-11-01` and every grant byte-read.**

---

## P-590-A — Courseware emit pipeline, buy-first (3–5 weeks)

**Problem it solves.** A client needs AI-generated courseware delivered **into their
existing LMS**, which means a conformant SCORM package, not a web app.

🔴 **What `p589`'s version of this recipe said:** add `scorm-again`, then *build the
generator*. 🟢 **What it should say:** the generator largely exists.

| Step | Component | Licence | Why this one |
|---|---|---|---|
| 1. Author | [course-code-framework/coursecode](https://github.com/course-code-framework/coursecode) **or** [kemalyy/edumints-scorm-skill](https://github.com/kemalyy/edumints-scorm-skill) | 🟢 MIT / MIT | Agent-native authoring. `coursecode` is framework-shaped (MCP-capable tools); `edumints-scorm-skill` is the skill half of an MCP pair. |
| 2. **Emit — buy, do not build** | [LiaScript/LiaScript-Exporter](https://github.com/LiaScript/LiaScript-Exporter) | 🟢 **BSD-3-Clause** | 🆕 **One Markdown-shaped source → SCORM 1.2, SCORM 2004, IMS, xAPI, H5P, PDF, ePub, Web**, with Moodle / ILIAS / OPAL presets. README read first-hand. 🔵 This is the step that was being budgeted as a build. |
| 2b. Emit, agent-driven alternative | [kemalyy/edumints-scorm-mcp](https://github.com/kemalyy/edumints-scorm-mcp) **or** [giacomomaria81/scorm-mcp-server](https://github.com/giacomomaria81/scorm-mcp-server) | 🟢 MIT / MIT | Use when the pipeline is already an agent loop and HTML/design bundles are the input rather than Markdown. |
| 3. Runtime | [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | 🟢 MIT | The content↔LMS API bridge. Still the first dependency; `362★`, pushed `2026-10-28`. |
| 4. If the deliverable is assessment | [numbas/Numbas](https://github.com/numbas/Numbas) | 🟢 Apache-2.0 | Newcastle University's engine, with its own `23,811`-byte SCORM storage runtime. Replaces steps 1–3 for assessment work. |
| 5. If sources are H5P | [sr258/scorm-h5p-wrapper](https://github.com/sr258/scorm-h5p-wrapper) | 🟢 MIT | Packs H5P into SCORM objects. `58★`, pushed `2026-10-29`. |
| 6. **Review before ship** | [savvides/idstack](https://github.com/savvides/idstack) | 🟢 MIT | 🆕 `11` instructional-design skills checking alignment, accessibility and assessment validity. 🔵 The only reviewer component on these shelves — without it the pipeline ships unaudited pedagogy. |

**Wiring.** `coursecode` writes LiaScript-flavoured Markdown → `LiaScript-Exporter` emits
every required target in one run → `scorm-again` is bundled inside the package for runtime
API calls → `idstack` runs as a gate on the authored source **before** export, so a failed
pedagogy check costs one re-author and not one re-package.

🔴 **Where to stop.** Do **not** add `Didask/scol-r` to a pipeline whose target LMS ingests
SCORM only — it is a SCORM *successor* format (MIT, live, French) and the client's LMS will
not take it. Offer it as the modern path, never as the compatible one.

🔴 **Validate, do not trust.** `SCORMShield-Admin/scorm-package-validator` and
`jowinjohnchemban/scormite` (both MIT, both live) will tell you whether the emitted package
is conformant. 🔵 Budget a validation step: `60.0 %` of the `topic:scorm` axis carries no
licence at all, so most of what a search surfaces here cannot be vendored anyway.

---

## P-590-B — Learning telemetry leg with named libraries, per runtime (2–3 weeks)

**Problem it solves.** The client wants learning events out of the courseware and into
something they can query — and `589-E` established that **xAPI is a conformance target you
SPEAK, so you buy the client library rather than writing one.**

| Client estate | Library | Licence | Measured |
|---|---|---|---|
| **JVM / Java** (most university back-offices) | [BerryCloud/xapi-java](https://github.com/BerryCloud/xapi-java) | 🟢 Apache-2.0 (`11,350 B`) | `20★`, `2026-10-30` |
| **PHP / Laravel** (the Moodle estate) | [ijeffro/laralocker](https://github.com/ijeffro/laralocker) | 🟢 MIT (`1,072 B`) | `9★`, `2026-10-03` |
| **Flutter / Dart** (mobile-native) | [jblough/TinCanDart](https://github.com/jblough/TinCanDart) | 🟢 Apache-2.0 (`11,358 B`) | `5★`, `2026-08-06` |
| **.NET** | [nurullahturkoglu/xapi-dotnet](https://github.com/nurullahturkoglu/xapi-dotnet) | 🟢 Apache-2.0 | `1★`, `2026-10-30` — 🔴 one-star, treat as reference |
| **Store (LRS)** | [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) **or** [openfun/ralph](https://github.com/openfun/ralph) | 🟢 Apache-2.0 / MIT | `144★` / `51★`, both pushed within a week |
| **Endpoint only, no full LRS** | [LearningLocker/xapi-service](https://github.com/LearningLocker/xapi-service) | 🟢 MIT (`1,070 B`, lowercase `license`) | `42★`, `2026-10-26` |
| **Validate at your own boundary** | [LearningLocker/xapi-validation](https://github.com/LearningLocker/xapi-validation) | 🟢 MIT (`1,070 B`) | `12★`, `2026-10-26` |
| **Validate the profile itself** | [yetanalytics/project-pan](https://github.com/yetanalytics/project-pan) | 🟢 Apache-2.0 (`11,356 B`) | `5★`, `2026-10-16` |
| **Dashboards** | [openfun/warren](https://github.com/openfun/warren) | 🟢 MIT | `17★`, `2026-10-31` |

**Wiring.** Emit with the library matching the client's runtime → validate statements with
`xapi-validation` **inside the studio's own boundary**, before anything reaches the client's
store → persist to `lrsql` (or `xapi-service` when the client refuses to host a full LRS) →
`warren` for dashboards. 🟢 **Validate the profile with `project-pan` and statements against
it with `project-persephone`** — two different jobs that are easy to conflate.

🔵 **The `pushed_at` dates above are the point.** `27` distinct owners hold the `35` live
permissive xAPI repositories, so this leg is a **real ecosystem**: if one library stalls,
another exists. 🔴 **That is not true one spec over** — see the QTI warning below.

---

## 🔴 P-590-C — QTI assessment interchange: a supplier, not an ecosystem (scoping note, not a recipe)

🔴 **Do not treat the QTI tooling list as a menu.** `8` of QTI's `14` live permissive
repositories belong to **one account** (`metyatech`), all pushed inside a six-day window in
September `2026`, **none above `2★`** (`Trend 42`). 🔵 **A liveness check passes this axis;
an owner count fails it.**

🟢 **How to scope a QTI engagement honestly:**

1. 🟢 **Stand on the two third-party rows** if a dependency is required:
   [feyst/qti3-validator](https://github.com/feyst/qti3-validator) (MIT, validates against
   the 1EdTech schemas) and [Citolab/qti-playground](https://github.com/Citolab/qti-playground)
   (MIT, preview/convert/modify).
2. 🟡 **Or speak QTI 3.0 directly** — the schemas are published, the XML is tractable, and
   this avoids a single-maintainer dependency entirely. 🔵 Budget the XML work explicitly
   instead of discovering it.
3. 🔴 **If the `metyatech` set is used, price it as vendoring one supplier's code**, with
   takeover budgeted. Treat the eight repositories as **one** dependency.

🔵 **Generalise the check, not the verdict:** before any interchange dependency, compute
**live repos ÷ distinct owners** over the axis. Near `1.0` is an ecosystem; `2.0` or one
owner above `50 %` is a supplier. The data comes free with the sweep.

---


## p589 — 2026-11-01 — two recipes this pass's rows make buildable: the courseware factory whose output crosses the copyleft boundary as *content*, and the university enablement engagement with a real course to copy

## P-589-A — 🟢 **The courseware factory that ships into a client's copyleft LMS without touching it** (6–8 weeks, Global; strongest in LATAM / EMEA where Moodle and Chamilo dominate)

**The brief it answers.** *"We have Moodle. We have 400 hours of material in PDFs, slides and
lecture recordings. Modernise it — and do not touch our LMS."*

🔵 **Why this is a pattern and not a project.** `Trend 41` establishes that SCORM is an
**export target**, not a conformance target: nothing needs to *speak* it at runtime, so there
is no integration to build. A SCORM package crosses into the platform as **content**. 🟢
**That is the cleanest licence boundary in this base** — Moodle's GPL-3.0 and Open edX's
AGPL-3.0 reach linked code, not uploaded course material.

**The wiring, every component measured first-hand `2026-11-01`:**

| step | component | licence | why this one |
|---|---|---|---|
| 1 — ingest source material | [`DozenTwelve/Papermorph`](https://github.com/DozenTwelve/Papermorph) `1,040★` · [`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill) `36,673★` | 🟢 MIT (text) | books and PDFs → structured, narrated, interactive material |
| 2 — generate decks and lessons | [`hugohe3/ppt-master`](https://github.com/hugohe3/ppt-master) `71,803★` | 🟢 MIT (text) | native PowerPoint with real shapes and narration, not screenshots |
| 3 — build the course shell | [`assafkip/claudemy`](https://github.com/assafkip/claudemy) `574★` | 🟢 MIT (text) | topic → researched course structure |
| 4 — assessments | [`numbas/Numbas`](https://github.com/numbas/Numbas) `216★` · [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) `1,370★` | 🟢 Apache-2.0 · 🟢 BSD-3-Clause | real maths engine; autograded notebooks for technical content |
| 5 — 🆕 **package for the LMS** | [`sr258/scorm-h5p-wrapper`](https://github.com/sr258/scorm-h5p-wrapper) `58★` | 🟢 **MIT (text)** | H5P interactions → SCORM objects; the only live permissive packer |
| 6 — 🆕 **the runtime contract** | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) `362★` | 🟢 **MIT (text)** | SCORM 1.2 / 2004 API; **the single external dependency the deliverable carries** |
| 7 — retention loop | [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) `540★` | 🟢 MIT | spaced repetition over the generated material |

🔴 **The three traps, each one measured rather than assumed:**

1. 🔴 **Do not reach for `S4-NetQuest/react-scorm-provider`, `gamestdio/scorm` or
   `raccoongang/edx_xblock_scorm`** — they are the obvious choices by name and they are
   `2023`, `2019` and **archived**. Budget the React layer as build, not integrate.
2. 🔴 **Do not vendor `cybercussion/SCOBot`** (`165★`, live, API says `NOASSERTION`): its
   licence is **CC BY-SA 4.0**, reciprocal, and propagates into client code. `589-F`.
3. 🔴 **Do not quote "an open-source SCORM stack"** — `56.6 %` of the axis has no licence.

🔵 **What to say in the room.** *"One MIT dependency. Everything else we generate. The output
is a file your LMS already accepts, so there is no integration, no fork, and no copyleft
obligation anywhere in what you receive."* 🟢 **And the generator is the billable artefact** —
the client keeps a pipeline, not a pile of courses.

**Shape.** 6–8 weeks: `1`–`2` ingest and taxonomy, `3`–`5` generation loop with the client's
own material, `6` packaging and LMS smoke test, `7`–`8` hand-over of the pipeline.
🟡 **Prerequisite:** the client's LMS version must be confirmed to accept SCORM 2004 — Moodle,
Open edX, Chamilo and Canvas all do, but the *version* decides which profile.

## P-589-B — 🟢 **The university enablement engagement, with a real graduate course as the template** (6–8 weeks, APAC-first, Global-portable)

**The brief it answers.** *"We are a business school. We must teach AI to our own faculty and
MBA cohort next term. We are not building a product."*

🔵 **Why this pattern changed this pass.** `P-587-B` and `P-588-B` sell the enablement tier to
a **corporate** engineering org. 🔴 **A university asks a different question — "show us a
course that has actually run"** — and until `p589` this base's enablement tier was five
English-language mega-repos with no institution attached to any of them.

🟢 **The template now exists and is permissively licensed:**
[`rphilipzhang/AI-PhD-S26`](https://github.com/rphilipzhang/AI-PhD-S26) — **MIT, byte-read,
`91★`** — is `DOTE 6635 Artificial Intelligence for Business Research`, Spring 2026, **CUHK
Business School**, Dept. of Decisions, Operations and Technology, with a named instructor,
TA and tutorial instructor, and **the 2024 and 2025 offerings of the same course in the same
repository**. 🔵 **Three years of a real course, and the licence permits adaptation.**

| layer | component | licence | role |
|---|---|---|---|
| course spine | [`rphilipzhang/AI-PhD-S26`](https://github.com/rphilipzhang/AI-PhD-S26) `91★` | 🟢 **MIT (text)** | 🆕 syllabus, per-session slides through to agentic AI, CoLab demos, problem sets, reading lists — **and three years of delivery history** |
| foundations module | [`microsoft/generative-ai-for-beginners`](https://github.com/microsoft/generative-ai-for-beginners) `122,693★` | 🟢 MIT (text) | 21 lessons, no content carve-out |
| agents module | [`microsoft/ai-agents-for-beginners`](https://github.com/microsoft/ai-agents-for-beginners) `78,550★` | 🟢 MIT (text) | 18 lessons from first principles |
| "we trained our own model" artefact | [`jingyaogong/minimind`](https://github.com/jingyaogong/minimind) `64,710★` | 🟢 Apache-2.0 (text) | ~64M params in ~2 h on modest hardware |
| 🆕 per-student study loop | [`OPTIMETA/PAIDEIA`](https://github.com/OPTIMETA/PAIDEIA) `91★` | 🟢 **MIT (text)** | ingests *the cohort's own* lectures and homework; emits drills, **graded handwritten answers**, weakness reports. 🔵 Ships for **Claude Code, Codex, opencode and hermes-agent** — so the institution is not locked to one agent vendor |
| assessment integrity | [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta) `21★` | 🟢 Apache-2.0 | randomised-experiment LMS plug-in; consent hidden from the instructor, identifiers stripped |

🔴 **The one hard constraint, and it is a licence, not a schedule.**
🔴 **`rasbt/LLMs-from-scratch` (`107,625★`) must not be used as course material.** Its
Apache-2.0 **modifies the definition of "Source"** to exclude *"any books specific to this
software and any related images"*. 🟢 The code is grantable; the book is not. 🔵 Cite it as a
reading recommendation students buy, never as a vendored handout.

🟡 **Second constraint:** `PAIDEIA` and `AI-PhD-S26` were last pushed `2026-07-11` and
`2026-07-28`. **Pin both commits** at kick-off; neither is abandoned, but neither is
weekly-active.

🔵 **Why APAC-first and why it travels.** The spine is a Hong Kong business-school course, so
the reference is credible to an APAC buyer and the delivery calendar matches. 🟢 **It travels
to LATAM and EMEA** for the reason `P-588-A` identified: every component here is
English-language and `Global`, so there is **no in-language supply dependency** — which is
exactly the `33×` gap `p587` measured and the thing that normally blocks LATAM delivery.
🔴 Translation of the spine is therefore in scope and should be priced; it is the single
largest LATAM line item.

**Shape.** 6–8 weeks: `1` audit of the cohort's existing material, `2`–`3` adapt the spine to
the client's discipline, `4`–`5` stand up `PAIDEIA` over the client's own lectures, `6` dry
run with faculty, `7`–`8` assessment-integrity setup and hand-over.


## p588 — 2026-11-01 — two recipes this pass's rows make buildable: the virtual classroom with NO copyleft boundary at all, and the enablement engagement whose deliverable is a model the client trained themselves

## P-588-A — 🟢 **The white-label virtual classroom a studio may fork, re-brand and ship closed** (10–14 weeks, EMEA / North America / LATAM)

**The client problem.** A ministry, university group or training provider wants *their own*
branded live-teaching platform — their domain, their look, their data residency — not a
reseller skin over someone else's SaaS. They expect to own the result.

🔴 **Why this recipe could not be written before this pass.** `P-587-A` solves the same
brief on [`bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) (**9,262★**),
which is **LGPL-3.0**: the studio may *link* to it but changes to BBB itself carry back, so
"fork it and ship it as ours" is exactly the thing that brief asks for and that licence
withholds. 🟢 **[`apache/openmeetings`](https://github.com/apache/openmeetings) is
Apache-2.0 and in the same tier**, and this base has carried its address on a
permissive-unshelved list since `p525` without filing it.

| Role | Component | Licence (text) | Stars | Note |
|---|---|---|--:|---|
| Live classroom platform | [apache/openmeetings](https://github.com/apache/openmeetings) | 🟡 **Apache-2.0** + declared third-party block | **688** | 🟢 **Fork, modify, re-brand, ship closed.** 🔴 Read the bundle first — one entry is **Oracle Free Use Terms**, which is not an open-source grant |
| LMS seam | [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | 🟢 **Apache-2.0** | **373** | 🟢 Makes the platform a full LTI 1.3 tool provider — it drops into the client's existing Moodle/Canvas/Open edX without forking *that* |
| Courseware out of recordings | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | 🟢 **MIT** | **71,880** | 🟢 Session transcript → native decks with real shapes and narration. 🔵 Re-measured `p588`: **71,880** against `p587`'s `71,803` — growth, not a contradiction |
| Revision material | [CaviraOSS/PageLM](https://github.com/CaviraOSS/PageLM) | 🟢 **MIT** | **2,057** | 🟢 Notes, quizzes and flashcards from the session's own material |
| Learning-record store | [openfun/ralph](https://github.com/openfun/ralph) | 🟢 **MIT** | **51** | 🟢 xAPI LRS, EMEA-origin (France Université Numérique) |
| Mastery model | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** | **456** | 🟢 Turns attendance and quiz streams into mastery estimates |

**How to wire it.** Fork OpenMeetings → re-brand and deploy in the client's own tenancy
(Kurento handles media, so residency is a deployment choice, not a vendor negotiation) →
expose it to the client's existing LMS as an LTI 1.3 tool via `ltijs`, so nothing in the
LMS is forked → each session's recording and transcript feed `ppt-master` for revision
decks and `PageLM` for quizzes and flashcards → `ralph` collects xAPI statements → `pykt`
converts the stream into per-learner mastery that drives what the next session revisits.

🟢 **The licence ledger has no copyleft row in it.** Apache-2.0 + Apache-2.0 + MIT × 4.
🔵 **That is the whole point of the recipe** and the sentence to put in the SOW: the
client owns a modified platform they may redistribute closed, which `P-587-A` cannot
promise them.

🔴 **The one thing to sequence first.** Enumerate OpenMeetings' bundled dependencies in
week one and decide, with counsel, which ship in the client's distribution. The ASF's own
code is clean; the bundle is where the question lives, and it is a build-configuration
question — cheap in week one, expensive in week twelve.

🟡 **Honest comparison, not a replacement.** BBB is **13× larger**, purpose-built for
teaching, and has the richer pedagogy surface. 🟢 **Choose on the deliverable: if the
client needs to *own and redistribute* the platform, this recipe; if they need the best
teaching features and will accept linking, `P-587-A`.**

---

## P-588-B — 🟢 **The enablement engagement whose deliverable is a model the client trained themselves** (6–8 weeks, Global — travels to every region, including LATAM)

**The client problem.** An enterprise or public-sector buyer has been told to "build AI
capability" and does not want another slide deck or vendor workshop. Their engineers want to
have *built* the thing, and their risk function wants evidence that a model can run inside
their own boundary.

🔵 **How this differs from `P-587-B`.** That recipe maps a workforce's skill gaps onto a
taxonomy and assembles a learning path — it answers *"what should these people learn?"*
This one answers *"can these people build it, and can it run in here?"* 🟢 **The two
compose: `P-587-B` selects the cohort, this one is what the cohort does.**

| Role | Component | Licence (text) | Stars | Note |
|---|---|---|--:|---|
| Foundations curriculum | [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 🟢 **MIT** | **122,693** | 🟢 21 lessons; the largest education-adjacent repo on GitHub. Week-one hand-off |
| Agent curriculum | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 🟢 **MIT** | **78,550** | 🟢 18 lessons on agents from first principles |
| Depth, mechanism | [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | 🟡 **Apache-2.0 — code only** | **107,625** | 🔴 **Vendor the code, not the book.** The grant's "Source" definition **excludes the books and images**; buy copies for the cohort rather than reproducing chapters in courseware |
| The capstone: a model they trained | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | 🟢 **Apache-2.0** | **64,710** | 🟢 **A ~64M-parameter model from scratch in ~2 hours on modest hardware** — the whole reason this recipe produces an artefact instead of a certificate |
| The full stack, end to end | [karpathy/nanochat](https://github.com/karpathy/nanochat) | 🟢 **MIT** | **59,252** | 🟢 Tokeniser → pretrain → fine-tune → inference → web UI. 🟡 ~2 months since last push — **pin the commit** at kickoff |
| Use-case bank for the brief | [ashishpatel26/500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects) | 🟢 **MIT** | **39,200** | 🟢 Agent use cases by industry, education among them — use it in pre-sales to turn "build AI capability" into three named candidate projects. 🟡 ~3 months stale; a catalogue, not a dependency |
| Mastery evidence | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** | **456** | 🟢 Converts exercise completion into mastery estimates — what the sponsor reports upward |
| Delivery surface | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0** | **1,240** | 🟢 The one platform of record a studio may lawfully fork and ship; or the client's own LMS over LTI 1.3 |

**How to wire it.** Weeks 1–2: the two Microsoft curricula run as a cohort on the client's
LMS, with `pykt` instrumenting completion as mastery rather than attendance. Weeks 3–4:
`LLMs-from-scratch` supplies the mechanism — **its code**, with the book bought per seat.
Weeks 5–6: the capstone — the cohort trains `minimind` end-to-end **inside the client's own
infrastructure**, then stands up `nanochat` to see the full serving path. Weeks 7–8: the
three candidate projects drawn from `500-AI-Agents-Projects` are scoped against what the
cohort now knows how to build.

🟢 **The two deliverables are what make this sellable.** (1) A cohort that has trained
and served a model, not watched one being trained. (2) 🔵 **A dated, reproducible record
that a language model was trained and served entirely within the client's boundary** —
which is the artefact a risk or data-protection function actually asks for, and it is a
by-product of the teaching rather than a separate engagement.

🟢 **Why it travels to LATAM, EMEA and APAC without modification.** Every row is
permissive and **English-language**, so there is no in-language-supply dependency —
`p587`'s measured binding constraint in LATAM. 🔵 **Localisation is a translation line
item on known, openly licensed content**, except `LLMs-from-scratch`'s book, which is not
granted and must be bought. 🟢 `minimind` is a Chinese-language project, which makes it
an easier sell in APAC, not a harder one.

🔴 **The two licence facts to settle before the SOW.** (1) `LLMs-from-scratch`: the book
and images are outside the grant — reproducing chapters in client courseware is the
mistake this recipe is designed to avoid. (2) Pin `nanochat` and
`500-AI-Agents-Projects`; both are months stale and both are teaching artefacts, where a
silent upstream change mid-cohort is worse than an old commit.

---

## p587 — 2026-11-01 — two recipes the new rows make buildable, both built on the LGPL *link* boundary and the permissive curriculum tier

Every component below was verified first-hand on **2026-11-01**: existence, stars and
recency from `gh api search/repositories`, **licence from the repository's own licence
file**. 🔴 Note the channel: `api.github.com/repos/{owner}/{name}` was unreachable in this
environment, so `search/repositories` is the authority for every figure here (`587-C`).

---

## P-587-A — 🟢 **The lecture-to-courseware loop: BigBlueButton recordings in, revision material out, no fork and no copyleft exposure** (8–10 weeks, EMEA / North America / APAC)

**The client problem.** An institution already runs virtual classes and already has
thousands of hours of recordings nobody can use. They want revision material, summaries and
assessment items generated from their *own* teaching, and they will not accept their
lectures leaving the estate.

**Why this is the cleanest offer in this file.** Every licence boundary falls the right way:

| Role | Component | Licence (text) | Stars | Boundary that makes it legal |
|---|---|---|--:|---|
| Virtual classroom + recordings | [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | 🔴 **LGPL-3.0** | **9,262** | 🟢 **LGPL permits *linking*.** The studio deploys BBB **unmodified** and consumes its recordings and events from outside. No derivative work, no carry-back. 🔴 Default branch `v4.0.x-develop`. |
| Transcript → deck | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | 🟢 **MIT** | **71,803** | 🟢 Native PPTX with real shapes and narration — the deliverable a lecturer will actually accept |
| Reading → study skill | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | 🟢 **MIT** | **36,673** | 🟢 Course reading list → a queryable skill, so generated material is grounded in the set text, not the model's memory. 🔴 branch `master` |
| Retrieval-grounded tutor | [towardsai/ai-tutor-app](https://github.com/towardsai/ai-tutor-app) | 🟢 Apache-2.0 | **34** | 🟢 LangGraph agentic RAG over a fixed corpus — answers come from *their* materials |
| Spacing schedule | [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | 🟢 **MIT** | **4,121** | 🟢 Turns generated items into a revision schedule instead of a dump |
| Local inference | [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT** | **1,163** | 🟢 Offline delivery where connectivity or residency rules bite |

**How to wire it.** BBB's post-publish hook drops a recording manifest → transcribe locally
→ `book-to-skill` indexes the course reading list as the grounding corpus →
`ai-tutor-app`'s LangGraph retrieval answers and drafts items **against that corpus only**
→ `ppt-master` renders the lecturer-facing revision deck → `fsrs4anki` schedules the items
for students → `Kolibri` serves it offline.

🔴 **The one thing not to do:** do not patch BBB. The moment the studio modifies BBB source,
LGPL-3.0 carry-back attaches to the modification and the clean story is gone. Everything
above consumes BBB's **outputs**.

🟡 **Honest gap:** transcription is not specified here because this base has not measured a
permissive education-grade ASR row. Declared rather than filled.

---

## P-587-B — 🟢 **The reskilling-path engagement: a skills taxonomy with a curriculum attached** (6–8 weeks, Global; LATAM-viable because it needs no in-language repo)

**The client problem.** A corporate-learning or workforce-development buyer wants to know
which skills their people lack, what to put in front of them, and whether it worked. This
is the commonest corporate-learning brief and this base could not previously answer it,
because the taxonomy spine was missing.

| Role | Component | Licence (text) | Stars | Note |
|---|---|---|--:|---|
| Skills / occupation spine | [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) | 🟡 **ODbL-1.0** | **7,489** | 🔴 **A data licence.** Build a *produced work* on it freely; publishing an **enriched taxonomy** means publishing the enrichment — settle this before the SOW (`587-E`) |
| Agent curriculum | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 🟢 **MIT** | **78,542** | 🟢 18 lessons, MIT — hand it to the client's engineers on day one |
| Shipping curriculum | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | 🟢 **MIT** | **76,141** | 🟢 The build-and-ship half; pairs with the row above |
| Hands-on labs | [Fazmin/AILearningGuide](https://github.com/Fazmin/AILearningGuide) | 🟢 MIT | **242** | 🟢 51 labs: ML, transformers, RAG, agents |
| Mastery model | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** | **456** | 🟢 Knowledge tracing — turns completion into *evidence of mastery*, which is what the buyer is actually paying for |
| Learning-record store | [openfun/ralph](https://github.com/openfun/ralph) | 🟢 **MIT** | **51** | 🟢 xAPI LRS, EMEA-origin (France Université Numérique), pushed `2026-10-31` |
| Delivery seam | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0** | **1,240** | 🟢 The one platform of record a studio may lawfully fork and ship |

**How to wire it.** `os-taxonomy` supplies the skill graph → the client's role definitions
are mapped onto it → gaps per person drive a path assembled from the three MIT curriculum
rows → `ralph` collects xAPI statements as learners move → `pykt` converts that stream into
mastery estimates that re-rank the path → `Sakai` (or the client's LMS over LTI 1.3) is the
delivery surface.

🟢 **Why this one travels to LATAM.** Nothing in it requires an in-language repository —
which, per `p587`'s measurement, is the binding constraint in that region: **two
Iberian-language education-AI repos above 10★, neither adoptable, against 67 in the Chinese
control.** The curriculum rows are English-language and MIT, so localisation is a
translation line item on known content rather than a build.

🔴 **Sequence the licence question first.** ODbL's share-alike on derived databases is the
only thing in this recipe that can surprise a client, and it surprises them *after* the
enrichment work is done. Settle it in week one.

---

## p586 — 2026-11-01 — four recipes the new rows make buildable, and the one the LGPL module boundary turns into the cleanest ERP offer in this file

Every component named below was verified first-hand on **2026-11-01**: existence, stars and
recency from `search/repositories`, **licence from the repository's own licence file**. No
component is named here that is not on [`../agents/top.md`](../agents/top.md) or
[`../repos/foundations.md`](../repos/foundations.md) with a measured licence.

---

### `P586-1` — Courseware factory: topic → deck → course → graded labs

🟢 **Why now.** `p586` found the generation tier moved up a layer: the unit of output is the
artefact a teacher hands over, not a question-bank item. All four generators are **MIT**.

| Step | Component | Licence | Stars | Role |
|---|---|---|--:|---|
| 1. Course skeleton | [`assafkip/claudemy`](https://github.com/assafkip/claudemy) | 🟢 MIT (text) | 574 | Topic in → researched course outline and materials out |
| 2. Slides | [`hugohe3/ppt-master`](https://github.com/hugohe3/ppt-master) | 🟢 MIT (text) | **71,803** | **Native** PPTX: real shapes, transitions, charts, narration — editable by the instructor afterwards |
| 3. Rich reading | [`DozenTwelve/Papermorph`](https://github.com/DozenTwelve/Papermorph) | 🟢 MIT (text) | 1,040 | Source text → animated, narrated, interactive web experience |
| 4. Assessment items | [`numbas/Numbas`](https://github.com/numbas/Numbas) | 🟢 Apache-2.0 (text) | 216 | Browser e-assessment with real maths handling |
| 5. Graded practical work | [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 BSD-3-Clause | 1,370 | Assign → autograde → release notebooks |
| 6. Code feedback | [`pedal-edu/pedal`](https://github.com/pedal-edu/pedal) | 🟢 MIT | 32 | Static + dynamic analysis of learner Python — *why* it failed, not just that it did |
| 7. Safe execution | [`openedx/codejail`](https://github.com/openedx/codejail) | 🟢 Apache-2.0 | 477 | Sandbox untrusted learner code — **do not skip this** |
| 8. Delivery into the client LMS | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 Apache-2.0 | 373 | LTI 1.3 tool provider — works against Moodle, Canvas, Sakai, Open edX without forking any of them |

**Wiring.** `claudemy` produces the outline and prose; `ppt-master` renders each module to
PPTX and `Papermorph` renders the readings; `Numbas` and `nbgrader` own assessment;
`codejail` wraps every execution of learner code; `ltijs` publishes the whole thing as one
LTI 1.3 tool so the LMS handles roster, SSO and grade passback.
🔴 **The one thing to get right:** keep generation **offline and human-reviewed** — generate
to artefacts an instructor edits, never into a live learner-facing surface. That single
boundary is what keeps the pipeline out of the "automated assessment" high-risk
classification in Vietnam's Decision 33/2026 and off the DC prohibited-use list.
**Estimate: 6–8 weeks** for a faculty-facing pilot in one department.

---

### `P586-2` — AI side-car for an education ERP, without forking it (the LGPL play)

🟢 **Why this is the cleanest offer in this file.** `p586` resolved
[`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) (903★, pushed
`2026-10-29`) to **LGPL-3.0 from its own licence file** — the API reports `NOASSERTION`.
LGPL-3.0 is **weak copyleft**: a *separate module* calling the API **keeps its own
licence**. And because OpenEduCat is built as **Odoo modules**, that side-car is the
platform's own standard extension pattern rather than a bespoke integration.

| Step | Component | Licence | Role |
|---|---|---|---|
| 1. System of record | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟡 **LGPL-3.0 (text)** | Admissions, fees, attendance, library, hostel, exams on one database. 🔴 Default branch **`19.0`**; owner is lowercase; repo has an **`_erp`** suffix |
| 2. The studio's AI module | *new, proprietary* | 🟢 **stays proprietary** | A separate Odoo module calling OpenEduCat's API — **never a patch to its files** |
| 3. At-risk-learner modelling | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 MIT | Knowledge tracing over attendance + assessment history |
| 4. Diagnosis | [`bigdata-ustc/EduCDM`](https://github.com/bigdata-ustc/EduCDM) | 🟢 Apache-2.0 | IRT/DINA/NCDM cognitive diagnosis. 🔴 **~24 months stale** — vendor the algorithms, do not depend on the package |
| 5. Staff-facing analytics | [`openfun/warren`](https://github.com/openfun/warren) | 🟢 MIT | xAPI learning analytics. 🔴 Self-described **proof of concept** — reference only |
| 6. Counselling agent | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 MIT | Turns the LLM into an ITS over the learner record |

🔴 **The hard rule that makes the whole pattern legal: the boundary is the module, and the
module must not be a fork.** Add a module; call the API; never edit OpenEduCat's own files.
If the client needs OpenEduCat's own behaviour changed, that change is LGPL-3.0 and must be
published — which is a contribution decision, not an accident to discover at delivery.
🔵 **Do not substitute `warren`'s stablemate `potsie` here.** This base previously
recommended `potsie` as "the production-ready alternative"; re-measured `2026-11-01`,
**`potsie` last pushed `2024-12-18` (~23 months)** against **`warren` `2026-10-31`**. The
recommendation was backwards and is withdrawn.
**Estimate: 8–10 weeks** for admissions + at-risk-learner scoring on one campus.

---

### `P586-3` — Assessment assurance for a regulated jurisdiction (APAC-first, EU-ready)

🟢 **Why now.** Vietnam's **Decision 33/2026/QD-TTg** names education a high-risk sector
citing **automated assessment** explicitly; South Korea's **AI Basic Act** (in force
22 January 2026) imposes **human-oversight** duties; Australia's **TEQSA** requires
generative-AI risk action plans. The sellable work is the **oversight layer around
assessment**, not the assessment — and the whole stack is permissive.

| Step | Component | Licence | Role |
|---|---|---|---|
| 1. Simulate before exposing learners | [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | 🟢 BSD-3-Clause | Computerised Adaptive Testing simulator — item-exposure and fairness analysis **before** a learner sees an item |
| 2. Defensible learner model | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 MIT | Knowledge tracing with published, inspectable models rather than an opaque score |
| 3. Pedagogical competence of the model itself | [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) | 🟢 MIT | Benchmark built from **Chile's Agencia de la Calidad de la Educación / CPEIP** exams — evidence the model knows how to *teach*, not just answer |
| 4. Auditable autograding | [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 BSD-3-Clause | Per-submission grading trail under Jupyter governance |
| 5. Controlled-experiment plumbing | [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta) | 🟢 Apache-2.0 | Consent hidden from the instructor, identifiers stripped from exports — **the human-subjects posture, built in** |
| 6. Lockdown, if the client insists | [`SafeExamBrowser/seb-win-refactoring`](https://github.com/SafeExamBrowser/seb-win-refactoring) | 🔴 **MPL-2.0** | Sector standard. 🔴 File-level copyleft — **compose alongside; do not modify its files** |

🔴 **State the gap in the proposal rather than papering over it.** There is **no permissive
proctoring platform**: the only permissive component, `Proctoring-AI` (MIT, 633★), last
pushed `2024-12-10` (~23 months). The honest architecture is **SEB + an agent**, with the
AI doing anomaly review under human sign-off — never autonomous invigilation.
🟢 **This stack ports to the EU unchanged**, which is the commercial point: Annex III
high-risk obligations ask for exactly these artefacts (risk management, logging, human
oversight), so one build serves APAC statute and EU compliance.
**Estimate: 10–12 weeks**, including the oversight documentation.

---

### `P586-4` — Offline-first tutoring where connectivity and data residency both bite (LATAM, rural APAC, EU public sector)

🟢 **Why now.** `p586`'s structural finding cuts both ways: a skill inherits the host
agent's model and data path, so residency becomes a *contract* question. These components
answer it **structurally** instead — the stack runs with **no frontier API call**.

| Step | Component | Licence | Role |
|---|---|---|---|
| 1. Platform | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT (text)** | Offline-first learning platform, 1,016 forks, built for low-connectivity deployment. Branch `develop` |
| 2. On-device model | [`orionsheep/wordlink`](https://github.com/orionsheep/wordlink) | 🟢 **MIT (text)** | A shipped **fine-tuned 1.5B model (SFT+DPO)** that runs offline — the proof the pattern works at useful quality |
| 3. Local tutoring stack | [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | 🟢 BSD-3-Clause | Voice, video and 3D avatars, Docker-first, local LLMs via **Ollama**. 🟡 Last push `2026-06-26` |
| 4. Local-first adaptive workspace | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | 🟢 MIT | Block-based adaptive learning that runs locally; 10+ providers incl. local |
| 5. Retention scheduling | [`open-spaced-repetition/free-spaced-repetition-scheduler`](https://github.com/open-spaced-repetition/free-spaced-repetition-scheduler) | 🟢 MIT | FSRS as a library — depend on this, not the Anki plug-in |
| 6. Speaking assessment | [`Halleck45/OpenPronounce`](https://github.com/Halleck45/OpenPronounce) | 🟢 MIT | Phoneme-level pronunciation scoring (Wav2Vec2 + DTW), self-hosted |
| 7. Curriculum-aligned content, LATAM | [`csepulvedai/libro-3d-interactivo`](https://github.com/csepulvedai/libro-3d-interactivo) | 🟢 MIT | Interactive 3D books with Chilean-Spanish narration, aligned to curriculum objective **OA 13**. Universidad de Los Lagos |

🟢 **Why this is the right LATAM answer specifically.** Adoption there is already
near-universal (92% of students, 79% of faculty, 87% of institutions), so the missing piece
is not AI — it is institutional capability under a **widening computing-inequality**
headwind reported in October 2026. An offline stack on a **permissive, forkable** platform
with **curriculum-aligned local content** is deliverable to a ministry without a
data-transfer argument. 🔴 Moodle and `rosariosis` dominate the regional installed base and
are GPL — **attach via LTI, never fork**.
🔴 **And for a language-learning brief, say the gap out loud:** `LibreLingo` (2,631★) is
**archived** and its live successor `freelingo` is **AGPL-3.0**, so there is no permissive
general language-learning platform. Composing rows 2, 5 and 6 above (plus
[`word-atlas`](https://github.com/designfuchen/word-atlas), MIT, 3,604★) is a **BUILD** —
price it as one. Gap `586-C`.
**Estimate: 8–10 weeks** for a pilot across a district or a ministry programme.

---

🔵 **One rule shared by all four patterns.** Not one of them forks a platform of record.
The AI attaches through a boundary that keeps the studio's code its own — an **LGPL module
boundary** (`P586-2`), a **permissive extension point** inside a copyleft platform
(`XBlock`, `codejail`), or **LTI 1.3** as a separate service (`ltijs`, every pattern).
🟢 Fork only when the client needs the platform itself changed, and then only **Sakai**
(ECL-2.0), **OpenOLAT** (Apache-2.0), **Kolibri** (MIT) or **relate** (MIT) — the four
platforms of record that permit it.

---

## p585 — 2026-11-01 — three recipes the licence resolutions make buildable, and the one the LATAM governance gap turns into the clearest offer in this file

Every component named below was verified first-hand on `2026-11-01` — existence and
recency from `search/repositories`, licence from the repository's own licence file.

---

## P-585-A — 🟢 **The forkable-platform engagement: own the LMS, ship it closed** (10–14 weeks, North America / EMEA)

**Why this is newly writable.** Every attachment pattern in this file exists because the
platform tier was believed to be uniformly copyleft. It is not: **four platforms of record
are permissive**, so "the client owns and ships a modified platform" is now a licit option
rather than a licence violation.

**Components**

| Role | Component | Licence | Stars |
|---|---|---|--:|
| Platform base — North America / higher ed | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 🟢 ECL-2.0 | 1,240 |
| Platform base — EMEA / DACH | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 Apache-2.0 | 449 |
| Platform base — git-backed / CS curricula | [inducer/relate](https://github.com/inducer/relate) | 🟢 MIT | 437 |
| Tutoring engine | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 🟢 Apache-2.0 | 53,084 |
| Knowledge tracing | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | 🟢 MIT | 456 |
| Mastery diagnosis | [bigdata-ustc/EduCDM](https://github.com/bigdata-ustc/EduCDM) | 🟢 Apache-2.0 | 203 |
| Untrusted code execution | [openedx/codejail](https://github.com/openedx/codejail) | 🟢 Apache-2.0 | 477 |
| Retention scheduling | [open-spaced-repetition/free-spaced-repetition-scheduler](https://github.com/open-spaced-repetition/free-spaced-repetition-scheduler) | 🟢 MIT | 731 |

**Wiring.** Fork the platform base. Expose `pyKT` and `EduCDM` behind one internal
"learner state" service — `pyKT` answers *what has this learner mastered*, `EduCDM` answers
*which specific skills are weak*; they are complementary, not alternatives. `DeepTutor`
consumes that state as context and generates the next interaction. `FSRS` schedules review
of anything marked mastered so it is not re-taught. Route any learner-submitted code
through `codejail` — never the application runtime.

🔴 **The one hard constraint:** `EduCDM` has not been pushed since `2024-10-25` (~24
months). It is Apache-2.0 and the models are sound, but **vendor it and own it** — do not
plan on upstream fixes.

---

## P-585-B — 🟢 **The LATAM institutional AI-governance offer: the gap is measured, the buyers are named** (8–12 weeks, LATAM)

**Why this is the clearest fit in this file.** The demand and the gap are both quantified
by third parties, not inferred: **92% of students and 79% of faculty** in LATAM higher
education are actively using AI (Digital Education Council / Tec de Monterrey, 29
universities, 2026), while **UNESCO IESALC** (200 institutions, 19 countries) finds a
**particularly wide gap between adoption and institutional governance**, and Tec de
Monterrey commentary states that formal institutional AI policies are simply lacking.
🟢 **Universities are already using AI and cannot evidence how.** That is a services sale,
not a licence sale.

**Components**

| Role | Component | Licence | Stars |
|---|---|---|--:|
| Pedagogical-quality baseline | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | 🟢 MIT | 13 |
| Controlled rollout + consent/anonymisation | [terracotta-education/terracotta](https://github.com/terracotta-education/terracotta) | 🟢 Apache-2.0 | 21 |
| Learning-record capture | [adlnet/xAPI-Spec](https://github.com/adlnet/xAPI-Spec) | 🟢 Apache-2.0 | 956 |
| Analytics surface | [openfun/warren](https://github.com/openfun/warren) | 🟢 MIT | 17 |
| Low-connectivity delivery | [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 MIT | 1,163 |
| Adaptive assessment | [douglasrizzo/catsim](https://github.com/douglasrizzo/catsim) | 🟢 BSD-3-Clause | 153 |

**Wiring.** `pedagogy-benchmark` first, as the **acceptance gate**: score the candidate
model on exams built by Chile's Agencia de la Calidad de la Educación and CPEIP *before*
any pilot, so the institution has a defensible pedagogical baseline rather than a vendor
claim. Deploy the tutor through `terracotta` so the rollout is a controlled comparison with
consent handling and identifier stripping built in — this is what converts a pilot into
evidence a rectorate can publish. Emit xAPI statements for every interaction;
`warren` renders them. Where connectivity is the binding constraint, deliver on `kolibri`.
Use `catsim` to simulate item exposure before any adaptive assessment touches students.

🔵 **Deliverable set, which is what is actually being bought:** an AI-use policy, an
auditable tutor, a staff capability programme, and an **ILIA-aligned** readiness baseline
(Latin American AI Index, with IDB and CEPAL) so the institution can benchmark itself
regionally. 🔵 Note `ILIA` (the index) is unrelated to `ILIAS` (the LMS) — they are
routinely confused in this industry's literature.
🔴 **`warren`'s own README still calls it a proof of concept** — ship dashboards on it only
with that stated, or render xAPI in the client's existing BI tool instead.
🔴 **Do not substitute `potsie` on recency grounds**: measured `2026-11-01`, `potsie` was
last pushed `2024-12-18` (~23 months) against `warren`'s `2026-10-31`.

---

## P-585-C — 🟢 **The contribution play: revive `pylti1.3` instead of writing a fourth Python LTI implementation** (3–4 weeks, Global — cheapest item in this file)

**The situation, measured.** Python LTI 1.3 has exactly one maintainable permissive
option, [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (🟢 MIT,
138★) — and it was **last pushed `2024-08-18`, ~26 months ago**. Node has a maintained
option ([`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs), 🟢 Apache-2.0, 373★, pushed
`2026-10-31`); Python does not.

**Why contribute rather than build.** LTI 1.3 is the seam every Moodle, Canvas, Open edX
and Chamilo engagement passes through. A fourth private implementation is unbillable
plumbing that must then be certified and maintained forever. 🟢 **Reviving the existing
MIT library costs less, and buys standing in the 1EdTech community that every subsequent
education engagement benefits from.**

**Scope.** Bring `pylti1.3` current against the 1EdTech LTI 1.3 Advantage certification
suite; validate credential handling against
[`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core)
(🟢 Apache-2.0) where badges are in scope; keep `ltijs` as the Node-side reference for
behaviour parity. 🔵 Pair it with [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again)
(🟢 MIT, 362★) when the client's legacy content is SCORM rather than LTI.

---

## 🔴 Licence ledger for all three recipes

Every component above is MIT, Apache-2.0, BSD-3-Clause or ECL-2.0 — **no recipe in this
section requires a copyleft component**, and none requires forking a copyleft platform.

🔴 **Two standing cautions that apply across all three:** (1) `EduCDM` (`2024-10-25`),
`girth` (`2022-09-09`), `pylti1.3` (`2024-08-18`) and `pupilfirst` (`2025-12-09`) are
permissive **and stale** — budget to own them. (2) **Never gate a build on the GitHub API's
licence field.** It reported `NOASSERTION` for six rows used above or alongside them, and it
cannot represent a split licence at all — [`andymatuschak/orbit`](https://github.com/andymatuschak/orbit)
is Apache-2.0 except for `packages/app` and `packages/backend`, which are AGPL-3.0-or-later
or **BUSL-1.1 (not an open-source licence)**. Read the licence file.


## p584 — 2026-11-01 — **five recipes the school-operations sweep makes buildable, including the first forkable-platform recipe this base has ever been able to write and a contribution play that costs less than any of them**

🔵 **Every repository named below was measured first-hand this pass:** grant byte-read via
`raw.githubusercontent.com` with byte counts, stars and `pushed_at` from
`gh api search/repositories`. 🔴 **No recipe here uses an unlicensed repository as a
dependency** — the unlicensed proctoring artefacts are cited as reference architecture only,
and said to be so.

## P-584-A — 🟢 **Shippable proctoring, which means SEB plus an agent — because there is no licensed proctoring platform to adopt** (8–10 weeks, EMEA or North America)

🔴 **The premise, measured:** `150` repositories on `topic:proctoring`; the credible
platforms (`narender-rk10/MyProctor.ai` `236★`, `AgnellusX1/GodsEye`,
`aryashinod/Multi-Agent-Online-Exam-Invigilation-System`) carry **no licence at all**, and
the Moodle plugin `eLearning-BS23/moodle-quizaccess_proctoring` (`30★`) is `NOASSERTION`.
🟢 **So the only lawful composition is a licensed lockdown client plus custom agent code.**

**Wiring:**
1. **Lockdown client — [`SafeExamBrowser/seb-win-refactoring`](https://github.com/SafeExamBrowser/seb-win-refactoring)**
   (🟡 **MPL-2.0**, `16,726 B` byte-read, `361★`, `2026-10-30`, ETH Zürich). Deploy as-is;
   configure, do not fork. 🟡 **MPL-2.0 is file-level reciprocity** — any SEB source file
   you modify must be published, so **keep all custom logic in separate files/processes.**
   That constraint is the whole licence plan.
2. **Exam launch — [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti)**
   (🟢 MIT, `1,098 B`, `26★`, `2026-10-28`, U. Michigan) if the tool is Django, so the exam
   launches from Canvas/Moodle as an **LTI 1.3 tool** rather than a parallel login.
   🔴 **If it is not Django, budget LTI as custom work** — see `P-584-D`.
3. **Integrity agent — build**, using
   [`wongcyrus/Google-AI-Classroom`](https://github.com/wongcyrus/Google-AI-Classroom)
   (🟢 MIT, `1,062 B`, `2026-10-28`) as the starting point: it already combines classroom
   multimodal sensing with exam invigilation, which is the exact shape needed.
4. **Low-infrastructure fallback —
   [`a8naaijetvi2lunk/carreau`](https://github.com/a8naaijetvi2lunk/carreau)**
   (🟢 MIT, `1,069 B`, `2026-10-01`, francophone): phone-based proctored MCQ with a
   **rotating QR code**. 🟢 Use where lockdown clients cannot be installed — BYOD
   classrooms and most LATAM/EMEA public-sector estates.
5. **Evidence trail —** `adlnet/lrs-conformance-test-suite` (MIT) for the xAPI statements,
   so the integrity decisions are auditable rather than asserted (`Trend 22`).

🔵 **Read, do not depend on:** the five-agent invigilation split (identity, gaze, phone
detection, …) in `aryashinod/Multi-Agent-Online-Exam-Invigilation-System` is the best
published decomposition of this problem and is **unlicensed** — reimplement the
decomposition, take no code.
🔴 **Regulatory gate before quoting:** Indonesia's SKB 7 Menteri and the Philippines'
DepEd Order `003` both constrain *runtime behaviour*; a proctoring agent in APAC needs
per-age-band limits and an incident-handling path, which is `P-583-B`'s pipeline.

## P-584-B — 🟢 **The forkable platform of record: Sakai, which is the only one a studio may lawfully modify and ship** (10–14 weeks, North America / EMEA)

🟢 **This recipe could not be written before this pass**, because this base published that
every platform of record was copyleft. It is not:
**[`sakaiproject/sakai`](https://github.com/sakaiproject/sakai)** is **ECL-2.0** (byte-read
`11,120 B`, *"Educational Community License, Version 2.0"*), **`1,240★`**, pushed
**`2026-10-30`**, and ECL-2.0 is an **Apache-2.0 derivative** — permissive.

**Wiring:**
1. **Fork Sakai.** This is the sentence this base has not previously been able to say about
   any platform of record. Moodle (GPL-3.0), Open edX (AGPL-3.0), Chamilo, ILIAS,
   OpenEduCat, Gibbon and ERPNext all remain **client-owned code, never shippable IP**.
2. **Extend through the contrib channel, not the core —
   [`sakaicontrib/attendance`](https://github.com/sakaicontrib/attendance)**
   (🟢 ECL-2.0, `11,120 B`, `14★`, `2026-09-01`) is the worked example: a tool that
   integrates with the Sakai gradebook without touching core.
3. **Add the agent tier** from `agents/top.md` — the MCP/skill rows
   (`PsychQuant/che-ntucool-mcp`, `timdrichards/canvas-lms-skill`, `amirtds/cubite-mcp`,
   all MIT) show the attach pattern against three different LMS tenancies; the same shape
   targets Sakai's REST surface.
4. **Where the client is small-to-medium and wants an SIS rather than an LMS**, use
   **[`academico-sis/academico`](https://github.com/academico-sis/academico)** (🟢 MIT,
   `1,094 B`, `410★`, `2026-10-28`, Laravel/Filament) instead — permissive, and explicitly
   scoped to small and medium institutions.

🔴 **Do not quote this as "we fork your LMS".** Sakai is an Apereo research-university
platform; the fork play is right for an institution already on Sakai or willing to migrate,
and wrong everywhere Moodle is incumbent — which is most of the market.
🔴 **The MIT near-miss is a trap worth naming to the client:**
[`4jean/lav_sms`](https://github.com/4jean/lav_sms) is MIT at `1,161★` and **cold since
`2024-03-06`** — a fork-and-adopt base, never a dependency.

## P-584-C — 🟢 **The guardian-facing tier, which nobody has shipped** (5–7 weeks, North America)

🟢 **The gap is positional, not technical.** This base holds tutor agents, grading agents,
and institutional agents. **It had no row facing the parent** until this pass.

**Wiring:**
1. **[`noestudios/lastbell`](https://github.com/noestudios/lastbell)** (🟢 MIT, `1,067 B`,
   `1★`, `2026-10-16`) — self-hosted **ParentVUE + Canvas** grade and assignment monitor
   with whole-family alerting. 🟢 Region placed from the product: **ParentVUE is a US K-12
   parent portal**, so this is a North America artefact by construction.
2. **Attach via LTI 1.3** (`academic-innovation/django-lti`, MIT) so the district sees one
   integration, not a scraper.
3. **Add a summarisation agent** that converts gradebook deltas into plain-language
   guardian updates — and gate it behind the **human-final-decision** architecture
   `Trend 28` describes, because a parent-facing claim about a child's performance is the
   highest-liability output in the whole stack.
4. **Evidence:** log every guardian-facing statement with provenance (`Trend 14`), because
   `134` bills across `31` states (March 2026) are converging on exactly this surface.

🔵 **Why it sells:** Ohio `HB 96`, Florida `SB 1194` and Tennessee require districts to
hold formal AI policies, and **Gallup (April 2026) measured > `60 %` of college students
using AI weekly against ~half of institutions discouraging it.** The parent is the
stakeholder nobody has given a legible interface, and Delaware's **AI Assurance Lab**
means "passes a state assurance review" is a shippable property.

## P-584-D — 🟢 **The contribution play: adopt `pylti1.3` instead of building a fourth implementation** (3–4 weeks, Global; cheapest item in this file)

🔴 **Measured this pass:** `dmitry-viskov/pylti1.3` is **MIT, `138★`, cold since
`2024-08-18`** — and the ecosystem has tried to re-home it **twice, unsuccessfully**:

| attempt | measurement | state |
|---|---|---|
| `CNIT-Organization/ltitoolkit` | `fork = false`, created `2026-06-04`; LICENSE byte-read `1,070 B` carries 🔴 **"Copyright (c) 2019 Dmitry Viskov"**; `pyproject.toml` renames to `ff-ltitoolkit`; README says *"Published via Git (no PyPI required)"* while the description advertises *"PYPI Package"* | 🔴 detached copy, `0★` |
| `pymsglobal/pylti1.3` | `fork = false`, **created and last pushed `2025-09-19`** | 🔴 abandoned same day, `2★` |

🟢 **So the cheapest high-leverage action available to a studio in this whole knowledge base
is maintenance, not construction:** adopt `pylti1.3`, which already carries `138★` of
dependents and is the framework-independent Python LTI 1.3 implementation of record.

**Wiring:** fork upstream → re-establish CI → publish to PyPI under a clearly derived name
with attribution → upstream the Django/Flask example repos (`31★` and `23★`, both MIT, both
cold) as adapters. 🔵 **Deliverable to the client:** every Python LTI integration they buy
afterwards becomes a connector line rather than custom work, which is the difference
`verticals/solutions.md` line 103 has been pricing for four passes.
🔴 **Scope honestly:** this closes the *framework-independent* gap. For Django it is already
closed by `academic-innovation/django-lti` (MIT, `26★`, `2026-10-28`) — **which sat in this
base's history `63` times without being shelved**, so check the shelves before quoting this
as custom work.

## P-584-E — 🟢 **The Philippines reference engagement: a graduated-latitude obligation with a one-million-seat capability programme already funded** (10–12 weeks, APAC)

🟢 **Why this one and not another APAC jurisdiction:** the Philippines is the first in this
base where the **obligation** and the **capability funding** are both specified and both
current.

| element | what it forces into the build |
|---|---|
| **DepEd Order No. `003`, s. `2026`** (Feb 2026), *Foundational Guidelines on AI in Basic Education* | **human-centred** and 🟢 **graduated by learner independence** — more independent learners get greater latitude. **This is a per-learner policy engine**, not a global setting: the product must carry a learner-autonomy attribute and vary affordances by it |
| DepEd's stated motive — use **outpaced** enforceable policy | the deliverable is **enforcement surface**: logging, policy versioning, and the ability to show what a given learner was permitted on a given date |
| **Google for Education, June 2026** — > `1` M educators, tiers incl. **"AI Mastery"** (Gemini + prompt engineering), > `1` M with Gemini access | 🔴 **the teacher base is being trained on Gemini**, so an agent that assumes a different model surface fights the installed skill base |
| **Project AGAP.AI** — ASEAN Foundation + Google.org, up to **`1.5` M participants in 2026** | the budget is **programme-shaped and partly donor-funded** — bid into the programme, not the school |
| **Aug 2026: master plan still in preparation** | 🟢 the window where a vendor's architecture can become the default (the Poland pattern) |

**Wiring:** `P-583-B`'s incident pipeline and per-age-band enforcement (built for Vietnam
and Indonesia) **transfers directly** — the Philippines adds a *learner-independence* band
to the age bands already required. Compose with `openfun/marsha` (MIT, LTI content
management) or a Moodle estate, the attach-boundary MCP pattern for the LMS, and the
`adlnet` conformance suites as the evidence trail.
🔴 **Declared, not hidden:** every figure above is **secondary-sourced** — `583-E` means no
primary legal text was obtainable from this session, and a "`40`-hour ECAIR / < `18 %`
completion" claim and a "$`3` bn" figure were **rejected as unverifiable single-source
developer-blog material.** Re-confirm DepEd Order `003` against a DepEd primary document
before it goes in a proposal.


## p583 — 2026-11-01 — **three recipes the integration sweep makes buildable, and the one it turns into a build**

🔵 All components below are byte-read this pass with `pushed_at` recorded
([`grants-byte-read`](../evidence/grants-byte-read.2026-11-01-p583.tsv),
[`integration-axis-sweep`](../evidence/integration-axis-sweep.2026-11-01-p583.tsv)).
🟢 **The rule every recipe here now obeys (`Trend 36`): the interchange layer is permissive
and shippable; the platform of record is copyleft and is deployed, not forked.**

## P-583-A — 🟢 **Put the agent inside the client's LMS and ship the conformance evidence with it** (6–8 weeks, North America)

🔵 **Why this is now a composition rather than a build:** `p582` published that no
maintained permissive LTI 1.3 library existed. One does, and the conformance suites are
permissive too — so the *proof* is a deliverable, which is what Delaware's AI Assurance
Lab and the Ohio/Florida district-policy duties actually buy.

**Wiring, concretely:**

1. 🟢 **Launch** — [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator)
   (BSD-3-Clause, `1,528 B`, `73★`, `2026-10-05`). Use `LTI13Authenticator` against the
   client's Canvas / Moodle / Open edX as **Platform**. 🔵 Non-Python stacks:
   [`StevenWeathers/peregrine-lti`](https://github.com/StevenWeathers/peregrine-lti)
   (Apache-2.0, Go) or
   [`swisnl/laravel-lti-provider`](https://github.com/swisnl/laravel-lti-provider) (MIT).
   🔴 **Do not start from `pylti1.3`** (MIT, `138★`) — `26.5` months cold.
2. 🟢 **Record** — statements to
   [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) (Apache-2.0, `144★`,
   `2026-10-27`) for a SQL-backed LRS, or
   [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) (Apache-2.0, `334★`) when the
   client wants the ADL reference implementation by name.
3. 🟢 **Emit from the browser** — [`xapijs/xapi`](https://github.com/xapijs/xapi) (MIT,
   `51★`, `2026-04-29`).
4. 🟢 **Prove it** — this is the step that is the product:
   [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite)
   (MIT, `78★`) for the xAPI MUST requirements, and
   [`adlnet/CATAPULT`](https://github.com/adlnet/CATAPULT) (Apache-2.0, `59★`) for **cmi5**
   course-launch conformance. 🟢 **Ship the two reports as the artefact a district files**
   under Ohio `HB 96` / Florida `SB 1194`.
5. 🟢 **Agent layer** — the tutor/grader itself, wired behind the LTI launch with the
   refusal and provenance defaults from `P-582-B` and `Trend 37`.

🔴 **The copyleft boundary to state in the SOW:** if the client wants Moodle *events*
pushed into the LRS, that is
[`davidpesce/moodle-logstore_xapi`](https://github.com/davidpesce/moodle-logstore_xapi)
(**GPL-3.0**) — and any Moodle plugin is GPL by the platform's own rule. **Price it as
client-owned code, not shippable IP.**

## P-583-B — 🔴 **The APAC compliance-shaped deployment: an incident pipeline and per-age-band enforcement, because two jurisdictions now require them** (10–12 weeks, APAC)

🔵 **Forced by `Trend 37`.** Vietnam's Công văn 5588/BGDĐT-GDPT (`2026-08-19`) requires an
**AI incident-handling process**; Indonesia's SKB 7 Menteri No. 400.1-492/2026 requires
**age-tiered limits on duration and content type** across formal, non-formal and informal
education. 🔴 **Neither is satisfiable by prompt design or a human-in-the-loop checkbox.**

**Wiring:**

1. 🟢 **Policy enforcement point, per age band.** One service in front of the model holding
   `(age_band, subject, max_minutes, allowed_content_classes)`. Indonesia's bands run from
   early childhood upward with *stricter duration and content limits for younger children*,
   so the band — not the user — is the policy key. 🔵 Vietnam's `12` periods/class/year
   core gives the duration budget a concrete denominator to meter against.
2. 🟢 **Tool-vetting register.** Công văn 5588 makes the **school** responsible for
   selecting and reviewing age-appropriate tools, so the deliverable includes a reviewable
   record per tool: version, data flows, age bands cleared, reviewer, date. 🔵 This is the
   same artefact Delaware's Assurance Lab wants in North America — **build it once**.
3. 🟢 **Incident pipeline.** Detect → classify → retain → escalate → audit. Minimum store:
   the prompt, the output, the policy decision, the age band, the human who was notified.
   🔵 Statements belong in the LRS from `P-583-A` (`lrsql`, Apache-2.0) — the incident log
   and the learning record are the same substrate, which is the cost saving.
4. 🟢 **Refusal by default on terminal decisions**, per `p582`: the grader may **filter**
   and may not **determine** pass/fail. Brazil and France already require this; it costs
   nothing to carry into APAC.
5. 🔴 **Do not price off the mandate.** Korea's AI digital textbook went `34.2 % → 5.2 %`
   adoption in one year after reclassification. Price off **funded** programmes.

## P-583-C — 🟢 **Item-bank round-trip for a national assessment mandate** (8–10 weeks, EMEA)

🔵 **Why now:** Saudi Arabia's AI curriculum has been in force since SY 2025-26 **with
learning outcomes counted in overall student assessment** — so assessment interchange is
mandated scope. 🟢 And the permissive QTI tier is **six tools, not one**, which this pass
established by refuting this page's own superlative.

**Wiring:**

1. 🟢 **Author** — [`metyatech/markdown-to-qti`](https://github.com/metyatech/markdown-to-qti)
   (MIT, `1,066 B`, `2026-09-19`): Markdown spec → **QTI 3.0** XML. The only permissive
   QTI **3.0** emitter measured.
2. 🟢 **Round-trip and validate** — [`examplary/qti`](https://github.com/examplary/qti)
   (MIT, `1,069 B`, `2026-10-12`) generates **and parses** IMS content packages. Parsing is
   what the converters below cannot do, and it is what makes the pipeline testable.
3. 🟢 **Inspect when it breaks** — [`sonyccd/qti-playground`](https://github.com/sonyccd/qti-playground)
   (MIT, `1,070 B`) as the debugging surface.
4. 🟢 **Ingest the legacy Canvas estate** — [`rolfis/qti-convert`](https://github.com/rolfis/qti-convert)
   (Apache-2.0, `11,357 B`, `22★`) for QTI → Word/JSON, and
   [`rikardroitto/canvas-quiz-skill`](https://github.com/rikardroitto/canvas-quiz-skill)
   (MIT, `1★`) for the reverse — Markdown → QTI 1.2 package for Canvas. 🔵 The latter is an
   **agent skill**, and the only agent artefact on `538` repositories.
5. 🟢 **Deliver** — [`ewels/starlight-quiz`](https://github.com/ewels/starlight-quiz)
   (Apache-2.0, `10★`, `2026-09-08`) renders the items permissively. 🔴 **Avoid
   [`Citolab/qti-components`](https://github.com/Citolab/qti-components) if the renderer
   must ship** — it is the maintained option of record and it is **GPL-3.0**.
6. 🔴 **The psychometric half is still a build.** Per `p582`, all eleven psychometric rows
   on these shelves are dead; `douglasrizzo/catsim` (BSD-3-Clause, Brazil) does adaptive-
   test *simulation* only. 🟢 **State plainly in the proposal that defensible calibration
   is bespoke or a commercial dependency** — it is not a composition.


## p582 — 2026-11-01 — **two recipes forced by this pass's measurements: the handwritten-assessment pipeline that finally has live components, and the compliance-shaped grader four regulators now require**

Every component below was verified first-hand on `2026-11-01` with `q=repo:owner/name`
(licence, stars, `pushed_at`, `archived`). 🔴 **Both recipes deliberately avoid the `19`
dead addresses this pass found cited elsewhere on this page** — see
`evidence/shelf-dead-rows.2026-11-01-p582.tsv`.

## P-583-A — 🟢 **Handwritten assessment capture and feedback — the first version of this recipe whose components are actually maintained** (8–10 weeks, LATAM / APAC lead, portable)

🔴 **Why this recipe is new rather than an update.** This base's handwriting primitives
were `githubharald/DeslantImg` (MIT, `156★`, 🔴 last push `2021-11-21`) and
`githubharald/WordDetector` (MIT, `276★`, 🔴 `2023-05-05`) — **dead for 5 and 3.5 years**.
Any recipe naming them does not build. 🟢 **`datalab-to/chandra` replaces both in one
component**, and adds the two things they never had: **table structure and full layout**.

🟢 **The engagement.** A school system or university whose assessment is *paper*, graded by
hand, photographed on a phone. This is the majority condition in LATAM, South and
Southeast Asia and much of Africa — and the reason digital-assessment pilots stall is that
the input was never digital.

| # | Component | Licence | Stars | Role |
|--:|---|---|--:|---|
| 1 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | 🟢 **Apache-2.0** | **12,655** | **Handwriting + tables + layout → structured text.** The load-bearing component |
| 2 | [breezedeus/Pix2Text](https://github.com/breezedeus/Pix2Text) | 🟢 **MIT** | **3,281** | **Maths formulae** → LaTeX. Small models — runs where `chandra` is too heavy |
| 3 | [naptha/tesseract.js](https://github.com/naptha/tesseract.js) | 🟢 **Apache-2.0** | **38,803** | Browser/WASM OCR fallback — **the image never leaves the device**, which is the data-protection answer for minors |
| 4 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | 🟢 **MIT** | **193,266** | Normalises the *reference* material (rubrics, answer keys, textbook extracts) into one text form |
| 5 | [Kozea/WeasyPrint](https://github.com/Kozea/WeasyPrint) | 🟢 **BSD-3-Clause** | **9,750** | Renders the marked-up script + feedback back to **PDF** — what a parent or teacher actually receives |
| 6 | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** | **456** | Knowledge tracing over the extracted item-level outcomes |

**Wiring.**
1. Phone photo → **`chandra`** for layout + handwriting; route any region it flags as
   mathematical to **`Pix2Text`** for LaTeX. Keep both outputs with per-region confidence.
2. Where policy forbids upload (minors' data; France's *cadre d'usage* bars identifiable
   student data in non-approved tools), run **`tesseract.js`** in-browser and send only
   the extracted text. 🔵 **Build this path first, not as a fallback** — it is what makes
   the product sellable in EMEA at all.
3. Rubric and answer key through **`markitdown`** once, at ingest, into the same text form.
4. An LLM scores *per item against the rubric*, emitting **item-level outcomes plus a
   confidence and a rationale — never an aggregate mark.** (See `P-583-B`: the terminal
   decision is barred.)
5. Item outcomes → **`pykt-toolkit`** for the learner model; feedback + annotated script →
   **`WeasyPrint`** → PDF.

🟢 **Where the margin is.** Steps 1–2 are commodity; **step 4's rubric-anchored,
item-level, confidence-bearing output is the product**, and step 2's on-device path is the
regulatory moat. 🔴 **Do not promise psychometric validity** — this pass established that
**every** open-source psychometric library is dead, so IRT-calibrated scoring is a build,
not a dependency. Scope this as *formative* feedback and say so in the SOW.

## P-583-B — 🔴 **A grader that is structurally incapable of deciding — because four regulators now require exactly that** (6–8 weeks, EMEA / LATAM, portable)

🟢 **This recipe exists because of a convergence measured this pass across four
jurisdictions queried in four languages** (see [`../intel/trends.md`](../intel/trends.md)):

| jurisdiction | the binding requirement |
|---|---|
| 🟢 **Brazil** — CNE *parecer* (≈`1 Sep 2026`, homologation ≈`13 Oct 2026`, 12 months to comply) | AI may be a **first filter** on essays and open responses; **may not determine approval or failure**. Four risk tiers. **Total ban in early-childhood education** |
| 🟢 **France** — *cadre d'usage* (Jun 2025) | AI use in submitted work **must be declared**; undeclared genAI is **fraud**; identifiable student data may not enter non-approved tools |
| 🟢 **Germany** — Länder | **Hessen:** AI use **and prompts** must be labelled. **NRW:** all aids disclosed |
| 🟢 **EU** — AI Act | **Art. 50** transparency from **`2 Aug 2026`**; grading is Annex III high-risk (Annex III timing contested — hedge it) |

🔵 **The requirement is not "add a human review screen". It is that the system must be
unable to emit a terminal decision**, and must carry provenance for every suggestion it
did emit.

| # | Component | Licence | Stars | Role |
|--:|---|---|--:|---|
| 1 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | 🟢 **MIT** | **193,266** | Submission + rubric normalisation |
| 2 | [ing-bank/popmon](https://github.com/ing-bank/popmon) | 🟢 **MIT** | **512** | Population-stability monitoring on the score and feature streams (**ING Bank N.V.**) |
| 3 | [IFCA-Advanced-Computing/frouros](https://github.com/IFCA-Advanced-Computing/frouros) | 🟢 **BSD-3-Clause** | **260** | Concept/data drift detection (**Instituto de Física de Cantabria**) |
| 4 | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** | **456** | Knowledge-tracing predictions — the distribution worth monitoring |
| 5 | [Kozea/WeasyPrint](https://github.com/Kozea/WeasyPrint) | 🟢 **BSD-3-Clause** | **9,750** | The auditable artefact: suggestion, rationale, model version, reviewer, timestamp |
| 6 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 🟢 **MIT** | **134,943** | Teacher review surface for annotating a script in-place |

**Wiring — the four constraints, implemented.**
1. **Refusal by construction.** The scoring service's response schema has **no total-mark
   field.** It returns per-criterion suggestions with confidence and a rationale. A mark
   exists only after a teacher writes one. 🟢 *This is a schema decision, not a UI
   decision* — it is what survives an audit.
2. **Declaration and labelling by default.** Every artefact leaving the system carries the
   AI-involvement label, the model version and — **for Hessen — the prompt**. Render via
   **`WeasyPrint`** so the record is a fixed document, not a database row.
3. **Age gating as a hard route, not a config flag.** Brazil bans AI in *educação
   infantil* outright, teacher-mediated included. The tenant's age band must be able to
   **disable the inference path entirely**.
4. **Post-market monitoring, which the AI Act requires and nothing education-specific
   provides.** **`frouros`** and **`popmon`** over **`pykt-toolkit`** outputs and the
   score distribution; alert on drift. 🔴 **Neither is education-aware — that integration
   is the billable work**, and it remains this base's clearest unmet build opportunity.

🟢 **Why this sells.** Germany's measured condition — **`56` rule-sets, `16` from the
Länder, and a teacher population that a Forsa survey finds has barely engaged with any of
them** — is a buyer who needs the compliance encoded in the tool, because they will not
read the rules. 🟢 **Spain is the cleanest entry:** a *real decreto* in preparation will
require **every university** to hold an ethical code covering faculty, students,
institution and research — a mandated artefact with no incumbent supplier.
🔵 **Brazil is the largest and most urgent:** homologation reported for mid-October 2026
starts a **12-month compliance clock** for schools *and* universities, and universities
must additionally write AI-mediation teacher training into their **PDI and PPC**.

🔴 **Known gap in both recipes, stated rather than hidden.** Attaching either to Moodle,
Canvas or Open edX properly needs **LTI 1.3**, and this base's only shelved implementation
(`dmitry-viskov/pylti1.3`, MIT) has been dead since 🔴 `2024-08-18`.
🟢 **CORRECTED `p584`:** if the tool is a **Django** application, use
[`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti)
(MIT, `26★`, `2026-10-28`, University of Michigan) and quote the integration as a
connector. **For any other framework the gap stands** — budget it as custom work, and do
not reach for `CNIT-Organization/ltitoolkit`, which `p584` established is a detached,
renamed copy of the same dead upstream.


## p581 — 2026-11-01 — **two new recipes: the lecture-archive pipeline, and the first buildable answer to this base's longest-standing gap**

Both use only rows verified first-hand `2026-11-01` (licence, stars, `pushed_at`,
`archived`) and name every component with its licence, because the licence is what decides
whether a studio can ship the result.

### 🟢 Pattern P-A — Lecture archive → searchable, tutorable, accessible corpus

**Who buys it:** a university system or ministry sitting on years of recorded lectures that
are undiscoverable and non-compliant. 🟢 **North America** buys the accessibility-audit
framing (captions that fail alignment audit); 🟢 **APAC** buys the ingestion framing (CJK
archives with captions burned into pixels, where no caption file exists to fetch).

**Wiring, in order:**

1. **Get text out of the recording — two routes, pick by what the archive is.**
   - Captions exist as a track → [`jdepoix/youtube-transcript-api`](https://github.com/jdepoix/youtube-transcript-api) (🟢 **MIT**, `8,543★`, `2026-10-30`). Cheapest path; also translates.
   - 🟢 **Captions are burned into the pixels** → [`YaoFANGUK/video-subtitle-extractor`](https://github.com/YaoFANGUK/video-subtitle-extractor) (🟢 **Apache-2.0**, `9,680★`). OCR over the subtitle region, fully local, no third-party API. **This is the only permissive route into hard-subbed archives and the reason this pattern exists.**
   - No captions at all → [`nexmoe/VidBee`](https://github.com/nexmoe/VidBee) (🟢 **MIT**, `11,026★`): local Whisper plus **speaker diarisation**. 🔵 Use VidBee specifically for **seminars, panels and vivas** — diarisation is what separates lecturer from student turns; for a single-speaker lecture it is overkill.
2. **Fix the timings** → [`smacke/ffsubsync`](https://github.com/smacke/ffsubsync) (🟢 **MIT**, `7,929★`). FFT alignment of the caption track against the audio. 🔴 **Do not skip this step.** A transcript with drifted timings cannot support seek-to-concept, clip extraction or a caption audit — and re-encoded archives drift as a rule.
3. **Cut it into teachable units** → [`zhouxiaoka/autoclip`](https://github.com/zhouxiaoka/autoclip) (🟢 **MIT**, `9,898★`, topics `ai-agent` + `mcp`). Long→short segmentation with subtitles and titles. 🟢 **Its description names 课程 (courses) as an input class**, so this is lecture-shaped, not only social-shaped. 🔵 Its `mcp` topic is the integration seam — drive it from your own agent rather than its desktop UI.
4. **Deliver inside the institution's LMS** on the permissive side of the licence seam:
   [`openedx/XBlock`](https://github.com/openedx/XBlock) (🟢 **Apache-2.0**) into Open edX
   (🔴 AGPL-3.0), or [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi)
   (🟢 **Apache-2.0**) over LTI into Moodle (🔴 GPL-3.0), with
   [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) (🟢 **MIT**) if the
   deliverable must be SCORM. 🟢 **Proprietary studio code stays out of the copyleft
   boundary.**
5. **Emit learning records** → [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec)
   (🟢 **Apache-2.0**) so step 2 of P-B has a stream to monitor.

🔴 **What this pattern does *not* do:** generate instructional video. Nothing open-source
does. Scope it as *archive activation*, never as content production.

### 🟢 Pattern P-B — Post-market monitoring for a deployed tutor or grader

🟢 **This is the first concrete recipe this base has for the gap it has called, for six
passes, the clearest unmet build opportunity in education AI.** It is assembled, not found:
the components are generic and the education-aware glue is the billable work.

**Who buys it:** 🟢 **EMEA first**, and on a dated clock — under the timetable this base
tracks, stand-alone education systems that grade work, screen applicants or supervise exams
carry Annex III obligations from **`2 December 2027`** (embedded products **`2 August
2028`**), with Article 50 transparency from **`2 August 2026`**, and **post-market
monitoring is a named duty**. 🔵 Also sells in **LATAM** as the evaluation half of a
governance engagement — note the `55 %`-no-AI-budget constraint, which is an argument for
composing permissive parts rather than licensing a platform.

**Wiring:**

1. **Model what the learner knows** → [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) (🟢 **MIT**, `456★`, `2026-10-18`). 🟢 **Its per-skill mastery predictions are the distribution to monitor** — that is the whole trick: you do not monitor the LLM's text, you monitor the learner-model outputs the tutor is supposed to be moving.
2. **Detect drift on those streams** — pick one:
   - [`IFCA-Advanced-Computing/frouros`](https://github.com/IFCA-Advanced-Computing/frouros) (🟢 **BSD-3-Clause**, `260★`): concept- and data-drift detectors. 🟢 **Default choice** — purpose-built for drift, permissive, public-institution provenance (Instituto de Física de Cantabria).
   - [`ing-bank/popmon`](https://github.com/ing-bank/popmon) (🟢 **MIT**, `512★`): population-stability over Pandas/Spark frames. 🟢 **Choose this when the deliverable is a report for a regulator or exam board** — ING Bank built it to be shown to a supervisor, and it produces stability reports rather than just alerts.
   - 🔴 **Not `SeldonIO/alibi-detect`** (`2,554★`) despite it being the highest-starred: licence reads **NOASSERTION** and it is stale since `2025-12-11`.
3. **Measure whether the intervention actually worked** → [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta) (🟢 **Apache-2.0**): randomised controlled trials inside LMS assignments, consent handling built in, identifiers stripped on export. 🔵 **Efficacy, which is a different question from drift** — pair them, do not substitute one for the other.
4. **Run untrusted learner code safely** if the subject is programming → [`openedx/codejail`](https://github.com/openedx/codejail) (🟢 **Apache-2.0**).
5. **Calibrate the assessment itself** → [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) (🟢 **BSD-3-Clause**, `153★`, live `2026-10-30`, 🟢 **Brazil-maintained — a LATAM-origin psychometric anchor**) for adaptive-test simulation. 🔴 **Do not promise item *generation*** from this: `catsim` simulates and calibrates, and no permissive item generator exists — searched three ways this pass and not found.

🔴 **State the limit to the client explicitly.** `frouros` and `popmon` **do not know what
a learner model is.** They will tell you a distribution moved; they will not tell you the
tutor's explanations got worse. **The education-aware layer — deciding which shifts are
pedagogically meaningful — is the engagement**, and it is unbuilt anywhere in open source.
🟢 Priced honestly, that is the strongest position: the commodity half is free and
permissive, the judgment half is the work.

### 🔵 Component licence ledger for both patterns

| Component | Licence | Shippable alongside proprietary code? |
|---|---|---|
| `youtube-transcript-api`, `ffsubsync`, `VidBee`, `autoclip`, `scorm-again`, `pykt-toolkit`, `popmon` | 🟢 MIT | 🟢 yes |
| `video-subtitle-extractor`, `XBlock`, `codejail`, `tsugi`, `terracotta`, `xAPI-Spec` | 🟢 Apache-2.0 | 🟢 yes |
| `frouros`, `catsim` | 🟢 BSD-3-Clause | 🟢 yes |
| Open edX platform | 🔴 AGPL-3.0 | 🟡 only across the `XBlock`/`codejail` seam |
| Moodle | 🔴 GPL-3.0 | 🟡 only across the LTI/`tsugi` seam |
| `alibi-detect` | 🔴 NOASSERTION | 🔴 **no — and stale** |

🟢 **Every permissive row above was licence-verified first-hand on `2026-11-01`** via
`q=repo:owner/name` against `search/repositories`. 🔵 `curl -sI` was **not** used: it
returns `403` for every `github.com` URL through this session's proxy, live repositories
included.


# Compose patterns — education

## p580 — 2026-11-01 — two recipes, both forced by this pass's measurements rather than chosen

## P-582-A — 🔴 **Safeguarding accountability for an EMEA school group — a BUILD, because the open supply is `6★`** (10–14 weeks, EMEA)

🔵 **Why this is a build and not an integration.** `Gap 579-D`'s falsifier run measured
`topic:safeguarding` at **`27` repositories with a `6★` head**, and that head
(`Brainhub24/TitanShield`, Apache-2.0) is a generic security toolkit, not an education
tool. Meanwhile safeguarding is a **statutory duty** for schools in England under *Keeping
Children Safe in Education*, with a named Designated Safeguarding Lead and audit
obligations. 🔴 **There is nothing to adopt.** Charge for the accountability.

**Components — every licence and star count read first-hand `2026-11-01`:**

| Layer | Component | Licence | Stars | Why this one |
|---|---|---|--:|---|
| LMS host | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** (byte-read) | `449` | 🟢 **The permissive EMEA LMS.** Swiss-origin, DACH university install base. Avoids Moodle's GPL-3.0 and Open edX's AGPL-3.0 — which matters because the safeguarding module itself will hold proprietary policy logic. |
| Evidence store | [DSpace/DSpace](https://github.com/DSpace/DSpace) | 🟢 **BSD-3-Clause** | `1,105` | Versioned, permissioned record store with durable identifiers. A safeguarding audit trail needs immutability and retention, not a database table. |
| Learning records | [adlnet/xAPI-Spec](https://github.com/adlnet/xAPI-Spec) | 🟢 **Apache-2.0** | `956` | The interchange format for "who did what, when". 🔵 Last pushed `2025-07-03` — **a ratified spec, legitimately static** (trend 35). |
| Agent runtime | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0** | `52,849` | Only if a learner-facing tutor is in scope; its three-layer memory is the component that creates the safeguarding exposure in the first place. |

**Wiring:**
1. 🔴 **Classification runs out-of-process.** The disclosure detector (self-harm, abuse,
   grooming signals in tutor transcripts) is a separate service behind an OpenOLAT REST
   hook — never an in-tree plugin, so the policy logic stays out of Apache-2.0 scope and
   can be audited independently.
2. 🟢 **Human-final-decision by architecture, not policy.** Every classification writes an
   xAPI statement to DSpace and raises a case to the Designated Safeguarding Lead; the
   system **cannot close a case itself**. 🔵 This is the carve-out `Trend 28` identified:
   where a regulator exempts human-final-decision systems, compliance stops being
   paperwork and becomes an architecture choice. `Submitty/Submitty`'s explicit TA-grading
   stage is the same pattern shipped as a product feature.
3. 🟢 **The deliverable is the evidence trail**, per `Trend 22`: retention schedule,
   immutable case history, reviewer identity, model version per decision. The classifier
   will be replaced within a year; the trail is what the school is actually buying.
4. 🔴 **Do not promise EU AI Act Annex III conformity artefacts off the shelf** — `p577`
   recorded that no EMEA-origin open conformity component exists, and this pass found none
   either. Scope it as bespoke.

## P-582-B — 🟢 **Assessment generation after the T5 tier died — the generator is a prompt, the product is everything around it** (8–10 weeks, Global)

🔴 **Why the obvious starting point is wrong.** This base shelved
`topic:question-generation` with correct licence bytes and called
`patil-suraj/question_generation` the axis's *"reference implementation"*. This pass
measured recency for the first time: **all five rows last pushed between `2023-12` and
`2024-08`, one archived.** Every one is a fine-tuned T5 pipeline for a task
instruction-following models now do zero-shot (trend 35). 🔴 **Starting there inherits a
dead dependency and builds the one layer that is no longer scarce.**

**Components — all measured current `2026-11-01`:**

| Layer | Component | Licence | Stars | Last push |
|---|---|---|--:|---|
| Item authoring & delivery | [numbas/Numbas](https://github.com/numbas/Numbas) | 🟢 **Apache-2.0** | `216` | `2026-10-28` |
| Autograded notebooks | [jupyter/nbgrader](https://github.com/jupyter/nbgrader) | 🟢 **BSD-3-Clause** ⬅️ *settled this pass* | `1,370` | `2026-10-28` |
| Untrusted code execution | [openedx/codejail](https://github.com/openedx/codejail) | 🟢 **Apache-2.0** | `477` | `2026-10-27` |
| Psychometric calibration | [bigdata-ustc/EduCDM](https://github.com/bigdata-ustc/EduCDM) | 🟢 **Apache-2.0** ⬅️ *was filed `no-grant`* | `203` | 🔴 `2024-10-25` |
| Offline item-bank reference | [BBkjdayup/BCTK](https://github.com/BBkjdayup/BCTK) | 🟢 **MIT** | `53` | `2026-09-28` |
| LMS seam | [openedx/XBlock](https://github.com/openedx/XBlock) | 🟢 **Apache-2.0** | `471` | `2026-11-01` |

**Wiring:**
1. 🟢 **Generate with a frontier model, store in Numbas' own item format.** No fine-tuned
   generator, no model to maintain. The generator is a prompt plus a schema validator.
2. 🟢 **Calibrate with `EduCDM`.** Adopt the DINA/IRT/MIRT/NCDM implementations —
   permissive, and this base had them wrongly filed as ungranted for most of `580` passes.
   🔴 Vendor the code; it has not been pushed to in a year.
3. 🟢 **Grade code submissions through `nbgrader` over `codejail`.** `codejail` is the
   component that makes "run the learner's program" safe, and it is Apache-2.0 inside an
   AGPL platform — so it can be lifted out and used alone.
4. 🟢 **Ship through `XBlock`** into Open edX, or over **LTI 1.3** into Moodle. Both keep
   the studio's generator out of the platform's copyleft scope.
5. 🔵 **Take the offline posture from `BCTK` where the buyer is liability-bearing.** It
   keeps the item bank and the data on the institution's own machine — the posture
   `Trend 32` says institution-accountable buyers actually want, and the reason that tier
   never produces popular repositories.
6. 🔴 **Do not use `asahi417/lm-question-generation` for pt-BR work** — nine languages, no
   Portuguese, and abandoned since `2024-08-20`.

🟢 **What the client is buying:** item banking, interchange (`scorm-again`, MIT),
calibration and a defensibility trail. 🔴 **Not the generator** — that is the part that
stopped being scarce, and the part whose open-source tier died proving it.

## p579 — 2026-11-01 — two recipes, every component licence read from its file this pass

## P-581-A — 🟢 Student-facing analytics and advising on Canvas, FERPA-scoped (6–8 weeks, North America)

**Who it is for.** A US university or college system already on **Canvas** that wants
learners to see their own progress — and wants it without a per-seat contract with
Instructure, and without shipping student records to a vendor.

**Why these parts.** Both halves of the Canvas seam are permissive and both were written
*by universities*, which is what makes the FERPA conversation tractable: the code already
assumes a US institutional data posture.

| Part | Repo | Licence | Stars | Role |
|---|---|---|---|---|
| Learner-facing analytics | `tl-its-umich-edu/my-learning-analytics` | **Apache-2.0** | 37 | The product surface: Resources Accessed, Assignment Planning, Grade Distribution. Django + MySQL, Docker. University of Michigan ITS |
| Canvas tool surface | the `canvas-mcp` field — head is a `310★` MIT University of Illinois server, `102` tools, naming FERPA five times (`p565`) | **MIT** | 310 | Read/write access to Canvas for the agent, without a bespoke integration |
| Student model | `pykt-team/pykt-toolkit` | **MIT** | 456 | Knowledge tracing over the Canvas activity stream — turns "accessed" into "likely knows" |
| Diagnosis + path | `ZhijieXiong/pyedmine` | **MIT** | 82 | Cognitive diagnosis and **learning-path recommendation** (`4` LPR models) for the advising suggestion |
| LMS integration without a fork | `dmitry-viskov/pylti1.3` | **MIT** | 138 | LTI 1.3 so the tool launches from Canvas as a tool, not a parallel login |

**How it wires together.**

1. **Weeks 1–2 — stand up MyLA against a Canvas sandbox.** Its three views are the whole
   product-market question answered for you: ship them first, unmodified, and get a
   registrar and a privacy officer to look at them. Do not build a new UI yet.
2. **Weeks 2–4 — attach the MCP server as the write side.** MyLA reads; the Canvas MCP
   server lets an agent act (nudge, schedule, draft a message). Keep the two apart: the
   analytics path stays deterministic and auditable, the agent path is advisory and logged.
3. **Weeks 4–6 — fit `pykt-toolkit` on the activity stream, then `pyedmine` on top.** KT
   gives a per-skill mastery estimate; `pyedmine`'s LPR models turn that into "do this
   next". 🔵 Train on the institution's own term-over-term data — the public KT datasets
   will not match a Canvas course shape.
4. **Weeks 6–8 — launch as an LTI 1.3 tool via `pylti1.3`.** Launching from inside Canvas
   is what makes it a feature rather than another login, and LTI keeps every integration
   boundary at a standard.

🔴 **The two things that will actually hold this up**, neither of them technical. **(a)
FERPA review**: student-facing analytics show a student *their own* record, which is the
easy case — but the advising agent generates new inferences about them, and that is a new
record. Budget a privacy review as a deliverable, not an afterthought. **(b) Grade
Distribution is politically live**: showing a learner where they sit in a cohort is a
decision the faculty senate makes, not the delivery team. Ship it switchable per course.

🟢 **Why it is sellable:** `134` AI-in-education bills across `31` states in 2026, and four
states (MD, ID, OK, VA) requiring state guidance **and** district-level policy. The
conformance documentation is billable alongside the build, and it is the part the client
cannot download.

---

## P-581-B — 🟢 Assessment generation as a service, because there is nothing to adopt (10–12 weeks, Global)

**Who it is for.** Any institution or awarding body that must *produce* assessments at
volume — a university assessment office, a vocational awarding body, a ministry
examinations unit, a corporate certification programme.

🔴 **Start from the honest finding: this layer has no open anchor.**
`topic:exam-generator` holds **`73` repositories and its head is `93★`**, measured this
pass on an axis no prior pass had queried. The two permissive heads are both **offline-first
desktop applications** — `heshengtao/exameow` (Apache-2.0, `93★`) and `BBkjdayup/BCTK`
(MIT, `53★`) — not libraries you embed. So this pattern is a **build**, and the recipe is
about which parts you do *not* build.

| Part | Repo | Licence | Stars | Role |
|---|---|---|---|---|
| Item model and maths assessment engine | `numbas/Numbas` | **Apache-2.0** | 216 | Browser-based e-assessment with real mathematics: randomised items, algebraic answer marking. **Do not rebuild this** — item types and marking are where assessment software goes to die |
| Interchange / LMS delivery | `jcputney/scorm-again` | **MIT** | 362 | Modern SCORM runtime — gets generated assessments into any LMS that already accepts SCORM |
| QTI interchange | `Citolab/qti-components` | 🔴 **GPL-3.0** | 18 | QTI item rendering. Copyleft — **keep it behind a service boundary**, or export QTI and render elsewhere |
| Generation reference | `heshengtao/exameow` | **Apache-2.0** | 93 | Read its prompt and item-type handling: MCQ, true/false, fill-in-the-blank, short answer, with offline bank storage and wrong-answer history. Apache-2.0, so you may lift code, not just ideas |
| Teacher-side reference | `BBkjdayup/BCTK` | **MIT** | 53 | Duplicate-item detection and Word/Excel bulk import — the two unglamorous features an assessment office asks for first |
| Course-material generation | `Hyan-Yao/instructional_agents` | **MIT** | 22 | ADDIE pipeline: syllabus → slides (`.tex`/`.pdf`/`.pptx`) → scripts → **assessments**, so the assessment is generated against the stated learning outcomes rather than against a PDF. EACL 2026 Main, arXiv:2508.19611 |
| Item calibration | `douglasrizzo/catsim` + `eribean/girth` | **BSD-3-Clause** / **MIT** | 153 / 127 | IRT calibration and CAT simulation — simulate item exposure *before* a generated item reaches a candidate |

**How it wires together.**

1. **Weeks 1–3 — Numbas first, generation second.** Model three real item types from the
   client's actual past papers in Numbas by hand. If Numbas cannot express them, the project
   scope is wrong and you have learned it in week two for the price of three items.
2. **Weeks 3–6 — generation against outcomes, not documents.** Drive
   `instructional_agents`' ADDIE pipeline from the syllabus so each generated item carries
   the learning outcome it tests. 🔵 This is the difference between an item bank and a pile
   of questions: without the outcome link there is no blueprint and no defensible coverage
   claim.
3. **Weeks 6–9 — calibration gate.** Every generated item goes through `girth` for IRT
   parameters and `catsim` for exposure simulation before any candidate sees it. **This is
   the gate that makes the service defensible** — a generated item with unknown difficulty
   cannot be used to certify anyone, and an awarding body's regulator will ask.
4. **Weeks 9–12 — delivery.** `scorm-again` for LMS delivery; export QTI for anything that
   needs it. Keep `qti-components` (GPL-3.0) out of your own binary — behind a service, or
   swapped for export-only.

🔴 **What this pattern must refuse, and this base already knew both.**
`CaviraOSS/PageLM` generates quizzes and flashcards and is widely treated as MIT —
**it is not**. Its `LICENSE.md` is MIT's body verbatim followed by commercial-use, SaaS and
resale restrictions, so it cannot go into a paid assessment deliverable without written
permission from CaviraOSS; these shelves have carried it as `BLOCK` for several passes.
Likewise `xiaoyang111222/cn-math-taxonomy` (`5,654★`) is the obvious blueprint source for a
maths assessment programme and is **CC BY-NC 4.0** — fine for a ministry or non-profit
engagement with attribution, unusable commercially, and already declared as `Gap 572-C`.
🔵 Both are re-confirmed here from their licence files rather than newly found; what this
pass corrected was the **ledger column**, which said `MIT` and `CC-BY` respectively.

🟢 **Why the economics work.** The client cannot download this layer — measured, not
asserted: `73` repositories, head `93★`. The parts worth buying (`Numbas`, `scorm-again`,
calibration) are permissive and mature; the part that must be built is the blueprint,
generation and calibration pipeline, which is also the part that carries the accountability
the client is actually paying to transfer.


## p578 — 2026-10-31 — two recipes, both built from rows verified this pass

## P-580-A — 🟢 Arabic-first children's literacy programme, forkable end to end (8–10 weeks, EMEA)

**Who it is for.** A ministry, a Gulf private-school group under KHDA guidance, or an NGO
funder running an early-grade literacy programme in Arabic or a Maghrebi dialect — the
engagement this base could not quote without greenfield game development until this pass.

**Why it is now buildable.** [`vgwb/Antura`](https://github.com/vgwb/Antura) is
**BSD-2-Clause** on its code (assets CC-BY-4.0), **128★**, Unity 6.x, already shipping
**Arabic, Darija, English, French and Polish**, and descended from the *EduApp4Syria* game.
BSD-2 means **fork, rebrand and ship** — no copyleft obligation anywhere in the chain.

**Wire-up, concretely.**

1. **Fork `vgwb/Antura`.** Keep the code under BSD-2 attribution; treat the CC-BY-4.0 art and
   media as a **separate grant** and keep the attribution file intact in the shipped build —
   this is the one compliance step teams skip, and it is in the assets, not the code.
2. **Add the target dialect** as a new language pack rather than a fork of the content
   pipeline, so upstream fixes keep merging. Budget the phoneme and grapheme work as
   content, not engineering; it is the long pole.
3. **Sequence the curriculum with [`miuuyy/Clew`](https://github.com/miuuyy/Clew) (MIT).**
   Model the literacy skills as a prerequisite graph, export the ordering, and drive Antura's
   mini-game progression from it instead of hand-ordering levels.
4. **Instrument with xAPI out to [`openfun/potsie`](https://github.com/openfun/potsie)
   (MIT)** — Grafana dashboards, production-ready. Use `potsie`, **not** `openfun/warren`,
   whose own README states it is a proof of concept.
5. **Evidence of effect:** if the funder wants a controlled claim, add
   [`terracotta`](https://github.com/terracotta-education/terracotta) (Apache-2.0) on the
   LMS side for randomised assignment of content variations.

**Licence ledger:** BSD-2 (game) + CC-BY-4.0 (assets) + MIT (`Clew`, `potsie`) + Apache-2.0
(`terracotta`). 🟢 **No copyleft, and the client can close the fork.**

🔴 **Two things to tell the client before signing.** The EU AI Act's stand-alone Annex III
obligations now apply from **`2 December 2027`** (secondary, twice-attested — the Official
Journal is not reachable from this harness), so an EU deployment has a dated runway, not an
exemption. And **there is no EMEA-origin pedagogical benchmark** to cite in the conformity
file: `eth-lre/mathtutorbench` carries **two contradictory content licences on one page** and
cannot be used as a dependency. Cite `AI-for-Education/pedagogy-benchmark` (MIT) instead and
be explicit that its items are Chilean in origin.

## P-580-B — 🟢 A tutor you can prove works before it meets a student (4–6 weeks, Global)

**The problem this closes.** `p573` registered that this base had **no usable
learner-simulation agent** — so every tutor engagement was sold on vibes and measured after
go-live, in front of real children. That is now only **partly** true, and the partial answer
is worth selling.

**Wire-up, concretely.**

1. **Take the evaluation harness, not the tutor.** From
   [`iwangjian/Coding-Tutor`](https://github.com/iwangjian/Coding-Tutor) (**Apache-2.0**,
   92★, ACL 2025 Findings) use **DICT**: simulated students paired with pre- and post-tests,
   plus the published dialogue corpus (`output/dialogue.zip`) and the verifier checkpoints
   (`jwanglvy/Verifier-7B`).
2. **Keep its second idea too — turn-by-turn verification.** Traver traces what the simulated
   learner knows and verifies each turn; that is the mechanism that makes the pre/post delta
   attributable to the tutor rather than to the test.
3. **Swap the domain.** 🔴 **DICT's tasks are code**, from `EvoCodeBench-2403`, downloaded
   separately **under its own terms — read them.** For a maths engagement, replace the task
   bank with items calibrated by `catsim` (BSD-3) and `girth` (MIT) — the permissive
   psychometrics pair already on these shelves — and keep DICT's protocol shape.
4. **Put the tutor under test.** `DeepTutor` (Apache-2.0) or `OATutor` (MIT) as the
   system under test; `Clew` (MIT) supplying the prerequisite ordering the simulated learner
   is walked through.
5. **Ship the numbers as the deliverable.** Pre/post delta per simulated-learner profile, with
   the profiles and the task bank handed over, so the client can re-run it on their own
   content. 🟢 **That artefact is the differentiator** — it is what a district or a ministry
   asks for and almost no bidder has.

**Licence ledger:** Apache-2.0 (`Coding-Tutor`, `DeepTutor`) + MIT (`Clew`, `girth`,
`OATutor`) + BSD-3 (`catsim`). 🔵 `EvoCodeBench-2403` is **outside** this ledger and is the
one term to check.

🔴 **State the limit in the proposal.** Simulated learners test the **tutoring loop**, not
safeguarding, not accessibility, and not whether a child will use it twice. Sell it as the
gate before a pilot, never as a substitute for one.

## p577 — 2026-10-31 — six recipes, every component verified

Each pattern names the exact repositories, their licences, and how they wire
together. Every component was verified on 2026-10-31. Licences are stated because
in education they decide the architecture (see
[`../repos/foundations.md`](../repos/foundations.md)).

### P1 — AI tutor beside the LMS, without forking it (any region)

**The default pattern. Use this unless there is a reason not to.**

```
Client LMS (unforked)                    Globant-built, permissive
Moodle GPL-3.0 / Canvas AGPL-3.0  <--LTI 1.3-->  ltijs (Apache-2.0)
Open edX AGPL-3.0                                      |
        |                                       DeepTutor (Apache-2.0)
        \-----------------xAPI----------------->  potsie (MIT) on Grafana
```

- **Seam:** `Cvmcosta/ltijs` (Apache-2.0, 373★) registers the AI service as an LTI
  1.3 tool. The LMS is never modified.
- **Tutor engine:** `HKUDS/DeepTutor` (Apache-2.0, 52.7k★) behind the LTI launch.
- **Telemetry:** emit xAPI statements; render with `openfun/potsie` (MIT, 11★)
  Grafana dashboards. **Not** `openfun/warren` — its README says proof of concept.
- **Why it matters:** engagement code stays outside the AGPL boundary. Forking
  Canvas or Open edX and hosting it for a client can oblige disclosure of the
  modifications; this pattern never raises the question.
- **Effort:** 6–8 weeks to a production pilot.

### P2 — Mastery-tracked practice with real psychometrics (all permissive)

For a client who wants adaptive practice and will be asked to defend it.

1. `satvik314/educhain` (MIT, 387★) generates the item bank from curriculum text.
2. `AI-for-Education/pedagogy-benchmark` (MIT, 13★) gates the generated items —
   it is built from exams developed by Chile's Agencia de la Calidad de la
   Educación and CPEIP, so it tests pedagogical knowledge, not just correctness.
3. `eribean/girth` (MIT, 127★) calibrates item difficulty and discrimination (IRT).
4. `douglasrizzo/catsim` (BSD-3-Clause, 153★) simulates adaptive item selection
   **before** any learner sees it.
5. `CAHLR/OATutor` (MIT, 274★) runs the tutoring loop with Bayesian Knowledge
   Tracing over the calibrated bank.

Every licence here is MIT or BSD. Steps 3 and 4 are what separate this from a
chatbot that guesses: the adaptivity is measured before deployment.

### P3 — Autograded technical coursework with proof it worked (North America)

1. `jupyter/nbgrader` (BSD-3-Clause, 1.4k★) releases and autogrades notebooks.
2. LLM partial-credit feedback layered on the deterministic autograde — never
   replacing it.
3. `Cvmcosta/ltijs` (Apache-2.0) surfaces it inside the client's Canvas.
4. `terracotta-education/terracotta` (Apache-2.0, 21★) runs the randomised
   evaluation: it assigns content variations to student groups, hides consent from
   the instructor, and strips identifiers from exports.

Step 4 is the differentiator in North American higher education, where the buyer
increasingly asks for evidence of effect rather than a demo.

### P4 — Multi-agent classroom simulation for teacher training (APAC-sourced, MIT)

1. `THU-MAIC/OpenMAIC` (MIT, 42.2k★) provides the simulated multi-agent classroom.
2. `huggingface/smolagents` (Apache-2.0, 30.2k★) adds role agents — disengaged
   student, parent, department head — around it.
3. Score the trainee's responses against `pedagogy-benchmark` (MIT).

The two largest education agents in open source (OpenMAIC 42.2k, DeepTutor 52.7k)
are both APAC-origin and both permissive. A teacher-training engagement can be
built almost entirely on APAC open source.

### P5 — EU-compliant self-hosted deployment (EMEA)

1. Client's own infrastructure; Moodle (GPL-3.0) or Open edX (AGPL-3.0) **unforked**.
2. P1's `ltijs` tool and `DeepTutor`, self-hosted — no learner data leaves the
   client's estate, which is what the EU AI Act and GDPR conversation turns on.
3. Use `thm-mni-ii/feedbacksystem` (Apache-2.0, 24★) as the **reference
   implementation** for feedback generation: a German public higher-education
   institution already ships it, which is a procurement argument, not just a
   technical one.
4. Document the deployment against the European Commission's AI literacy
   framework for primary and secondary education, and — for England, for anything
   touching marking — Ofqual's January 2026 principles for AI in high-stakes
   marking.
5. Dashboards: `potsie` (MIT), self-hosted Grafana.

**Effort:** 10–12 weeks; the compliance documentation is a real work package, not
an afterthought.

### P6 — Spanish-language curriculum content (LATAM)

1. `csepulvedai/libro-3d-interactivo` (MIT, 14★) is the **pattern** for
   curriculum-aligned interactive content: Three.js 3D pop-up books, Chilean-Spanish
   narration, mapped to a named curriculum objective (OA 13).
2. `satvik314/educhain` (MIT) generates the content at volume.
3. `pedagogy-benchmark` (MIT) gates it — already built on Chilean MINEDUC exams.
4. Deliver into Moodle or Chamilo (GPL-3.0), which is what the region actually runs,
   via the P1 LTI seam.

**Caveat, stated plainly:** the LATAM-origin repositories are 13–14 stars and
skill-shaped. Treat them as *patterns to reimplement*, not as dependencies to
build a client deliverable on. The reusable asset in LATAM is the curriculum
alignment method and the Spanish-language evaluation set, not the code.

## What these patterns deliberately avoid

- **Forking any LMS.** Every pattern attaches from outside.
- **`openfun/warren`** in client-facing work — its own README disclaims production
  readiness.
- **`bigdata-ustc/Agent4Edu`** — no licence file, so it cannot enter a deliverable
  regardless of its AAAI 2025 oral.
- **Unlicensed or micro-repos as dependencies.** Where only a micro-repo exists,
  the pattern says to reimplement it.

---

## Prior passes (superseded, retained for history)

### (archived) Compose patterns — education

<!-- machine-readable count claim, p570, for ingest/derive-counts.py -->
`derived recipes: **34**` — recipe headings on this page, counted with that gate's
own id regex (family-suffixed form, `P-572-A`). 🟢 **`p576` filed `P-578-A`, `P-578-B` and
`P-578-C`**, all three at `##` level in the counter's own form, and re-derived the page
afterwards: **`34` recipes across `11` families (`568`–`578`)**. 🟢 **AND THE GATE RAN AND AGREED**: `ingest/derive-counts.py`
reports `compose/patterns.md recipes: derived=34 families=11 range=P-568..P-578 claimed=34`
— **GREEN** (`576-G`). 🔴 **`p573` recomputed this: the
claim read `24` while the regex counted `28` before this pass's two additions.**
🔵 The gap is `P-573-A/B/C` and `P-574-A`, registered by earlier passes without
the count being refreshed — the same stale-claim defect this base records as a
trend.

Concrete recipes. Every component is a repo verified first-hand on 2026-10-31
with its licence named — and for everything added or re-read in the fourth pass,
**the licence text itself was read, not GitHub's summary of it**. Every pattern
obeys the one hard constraint of this industry: **the platform of record is
copyleft, so you attach to it, you do not fork it.**

**New in the fourth pass:** **P-569-A** (SCORM delivery — the attach doctrine
finally covers content moving *into* the platform) and **P-569-B** (the courseware
factory, built on the 71,498★ MIT content-production layer that four passes of
education-topic sweeps could not see). **P-568-K** carries a licence correction
that changes what it may ship.

Shared rule for all thirteen patterns — the licence boundary:

```
  [ client's LMS of record ]          GPL-3.0 / AGPL-3.0  ← never forked, never patched
   Moodle | Open edX | Canvas | Chamilo | i-educar
            │
            │  attach ONLY across a standard, permissively licensed boundary:
            ├── LTI 1.3 ....... Cvmcosta/ltijs        Apache-2.0  (launch + grades back)
            ├── MCP ........... canvas-mcp/moodle-mcp MIT         (agent reads LMS data)
            ├── xAPI → LRS .... adlnet/xAPI-Spec      Apache-2.0  (telemetry out)
            │                   openfun/ralph         MIT
            ├── SCORM ......... jcputney/scorm-again  MIT         (courseware IN)
            │
  [ Globant-built layer ]             your licence, your IP
```

**Shared step 0 — licence preflight (half a day; method upgraded again
2026-10-31, fourth pass).** Before any component enters a statement of work,
establish its licence from the **GitHub REST index** (`license.spdx_id`) and then
**read the licence file itself** over
`https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{filename}`, which
answers HTTP 200 from this session while `api.github.com` and `github.com` HTML
return 403 and MCP `get_file_contents` refuses third-party repositories. **Read
the file for every component, not only the ones the API flags** — the two licence
questions this KB carried longest were both resolved by reading text the API had
summarised as `NOASSERTION` or matched against no filter. Try **every filename**
(`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `licence`, `COPYING`) on **every
branch**: `24kchengYe/human-skill-tree` is AGPL-3.0 on `master` and 404 on
`main`, and two passes recorded it unresolved for exactly that reason. Do not
accept a sidebar or a README sentence. Across three passes this check has caught a defect
in roughly half the repos run through it. The failure modes, with the live
example to cite in a SoW appendix:

- *no licence field at all* → genuinely unlicensed, default exclusive copyright.
  **Disqualified.** `digitalinnovationone/dio-agent` — **2,750★** and no licence.
- *licence claimed in prose, file absent* → **disqualified**, regardless of the
  README. `DMontgomery40/mcp-canvas-lms` says "MIT License - see LICENSE file";
  that file 404s on every name and both branches, and GitHub's own licence index
  returns zero results for it.
- *`NOASSERTION` but actually a **split grant*** → **conditionally usable, per
  asset.** `learning-commons-org/knowledge-graph`: `LICENSE.md` with code **MIT**
  and datasets **"By data publisher"**, some datasets gated. The code clears; each
  dataset must be cleared individually.
- *content licence on code-shaped work* → **usable but viral on the text.**
  `brycewang-stanford/Auto-Empirical-Research-Skills`, 4,843★, **CC BY-SA 4.0**,
  and `GarethManning/education-agent-skills`, 932★, **also CC BY-SA 4.0** — the
  two largest education skill libraries in existence, both read from the licence
  file this pass. Share-alike propagates to derivatives of the skill text: fatal
  for a billable methodology asset, fine for internal reference. **Expect this
  shape whenever the artefact is pedagogy written in markdown.**
- *split grant with a **non-commercial** tier* → **the trap that matters most to
  a consultancy, because the restricted tier is the part you were going to
  ship.** `learning-commons-org/evaluators`, 87★: code **MIT**, prompts
  **CC BY 4.0**, and the **Annotated CLEAR and PERSUADE 2.0 corpora
  CC BY-NC-SA 4.0 — non-commercial.** The scoring machinery clears; the benchmark
  data does not. **Check every tier of a split grant for `NC`, not just the
  first.**
- *copyleft with a **per-directory** dual grant* → **partly usable, and no
  licence column can say so.** `24kchengYe/human-skill-tree`, 586★: AGPL-3.0
  overall, with `skills/*.md` available under **AGPL-3.0 or MIT at your option**.
  The platform is disqualified; the bundles inside it are not. Record the
  directory, not just the repository.
- *wrong version* → `openSIS-Classic` is GPL-**2.0**, not GPL-3.0: no patent
  grant, incompatible with GPL-3.0-only code in the same binary.
- *unparsed but present* → Odoo (LGPL-3.0) and `frappe/education` (GPL-3.0) name
  no licence in the sidebar and are perfectly licensed in the file.

A cheap corroborating trick worth knowing: `license:mit repo:owner/name` in
GitHub repository search returns **zero results** when GitHub detects no MIT
grant. It is a second, independent opinion for the cost of one query, and it is
how the `mcp-canvas-lms` defect was re-confirmed on the third pass.

One `curl` per dependency, written into the SoW appendix. It is the cheapest
risk control in this document and it has already caught a real defect. See
[`../intel/trends.md`](../intel/trends.md) for the measured results.

---


## 🆕 `p576` (2026-10-31) — three patterns, and all three exist because a *jurisdiction* was reached rather than a region

🔵 Every component below had its grant read byte-for-byte this pass or a prior one, with
the default branch resolved by `git ls-remote --symref` first — three of this pass's
components sit on a branch that is neither `main` nor `master` (`Artemis` → `develop`,
`i-educar` → `2.12`, `i-diario` → `1.6`), so a two-branch probe would report them dead.

## P-578-A — 🟢 BNCC-aligned tutor for Brazil, with the curriculum claim made falsifiable (6–8 weeks)

**The opening.** 🟢 **MEC published AI guidance for *educação básica* in April 2026** — four
pillars and ten diretrizes — plus a teacher-training course, and behind it the
**Referencial** (SEGAPE/MEC) asking institutions to stand up AI governance and ethics
committees. Every Brazilian network now needs to say how its AI tooling relates to the
**BNCC**. 🔵 **Almost everyone will *assert* alignment. This recipe lets a client
demonstrate it, and that is the whole differentiator.**

**Components, with grants read first-hand.**

| role | component | licence | why this one |
| --- | --- | --- | --- |
| curriculum spine | [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) | 🟢 **MIT** (code) **+ CC BY 4.0** (data) | `1,721` *aprendizagens* as JSON/CSV/SQLite with provenance per record; **npm + PyPI packages with data embedded, no internet needed**; **local MCP server** `npx -y @bncc/mcp`; Zenodo DOI `10.5281/zenodo.21625233` |
| alignment proof | [`bncc-dev/bncc-benchmark`](https://github.com/bncc-dev/bncc-benchmark) | 🟡 **MIT** harness **+ CC BY 4.0** items/results | `15,300` responses from `17` models scored for hallucination **against the BNCC itself** |
| tutoring loop | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 **MIT** (1,073 B) | MCP server that turns any LLM into an ITS; attaches to the same MCP surface as the curriculum spine |
| offline delivery | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT** | the reference choice where connectivity is absent — which is where Brazil's **rural-priority** obligations land |
| model serving | Ollama or vLLM | 🟢 MIT / Apache-2.0 | keeps student prompts on infrastructure the network controls |

**How it wires together.** 🔵 Both the curriculum spine and the tutor are **MCP servers**,
so the integration is configuration, not glue code: the tutor resolves every objective it
teaches to a BNCC *aprendizagem* code through `@bncc/mcp` running locally. Kolibri carries
the content offline; the model runs on the network's own infrastructure.

**The deliverable that wins the renewal.** 🟢 **Re-run `bncc-benchmark`'s harness against
the client's own configured stack and hand over the scores.** That converts "our tutor
follows the BNCC" into a number, per model, per curriculum stage, reproducible by the
client. 🔵 **No other jurisdiction in this base has an equivalent harness**, so this recipe
does not port — and that is an argument for pricing it as Brazil-specific work.

🔴 **Read these three constraints to the client before signing.** The data is **CC BY 4.0**,
so attribution to **Profy Tecnologias Educacionais Ltda** travels with every derived
artefact. The benchmark's stored **model responses were generated by third-party models and
carry those providers' reuse conditions** — the repository says so explicitly; re-run the
harness rather than redistributing its results. And `bncc-dados` is **`24★`** — judge it on
its DOI, validation workflow and stated provenance, not its popularity, and fork it so a
maintainer change cannot strand the engagement.

## P-578-B — 🟢 Human-final-decision assessment architecture, so a Korean deployment falls OUTSIDE high-impact AI (6–8 weeks)

🟢 **The finding this is built on.** Korea's **AI Framework Act** and Enforcement Decree
have been fully in force since **`22 January 2026`**. Education's named high-impact instance
is **`학생평가` — student assessment**. 🟢 **And the Decree provides that where a human
intervenes in the final decision, the system is judged controllable and is excluded from
high-impact AI.**

🔵 **So this is not a compliance-documentation engagement. It is an architecture engagement
whose output happens to be compliance** — and the architecture is one a pedagogue would
choose anyway.

**The architecture, stated as the rule it has to satisfy.**

1. 🟢 **The model never writes a grade of record.** It produces *feedback* and a *proposed*
   mark, both held in a pending state.
2. 🟢 **A teacher's action is the only transition that creates a grade.** Not a timeout, not
   a default-accept, not a bulk "approve all" — each of those re-imports the system into
   the high-impact class by removing the human from the decision.
3. 🟢 **Every transition is logged with the human actor, the proposed value, the final
   value and the delta.** That log is the evidence that the carve-out applies, and it is
   the artefact to hand the regulator.
4. 🟡 **Generative output shown to students carries the labelling** the Act requires of
   generative AI, independently of the high-impact question.

**Components.** 🟢 [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) — **MIT**,
1,091 B, branch **`develop`**, TUM — is the spine: *"Interactive Learning with Automated
Feedback"*, automated feedback with a teacher-owned grade, which is this pattern's shape
shipped as a product. 🟢 [`Submitty/Submitty`](https://github.com/Submitty/Submitty) —
**BSD-3-Clause**, grant in **`LICENSE.md`**, RPI — is the alternative where the
**explicit "TA grading" stage** is wanted as a first-class step. 🟢
[`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) — **BSD-3-Clause**,
UC Berkeley — handles notebook-based courses. 🔴 **Do not build this on
[`INGInious/INGInious`](https://github.com/INGInious/INGInious)**: **AGPL-3.0**, its own
licence says *"Most of the files…"* rather than all, and **§13 network exposure applies to
a hosted grader** — which is the only way a grader is ever deployed.

**Why it is worth more than a filing.** 🔵 The grace period is the window: MSIT grace of
**`≥1` year** with a delay to **2029** proposed. A client who adopts this architecture now
is not buying a reprieve — **they are buying a system that never enters the regime.**

🔴 **The honest grade, and say it in the proposal.** Every date, threshold and the carve-out
itself are **`C`-graded secondary** — read from policy trackers and law-firm briefings, not
from **`law.go.kr`**, which is unreachable from this harness along with every other
government host (`576-B`). 🟡 **Control families are reliable; the exact wording is not.**
**Have Korean counsel confirm the carve-out against the statute before the architecture is
sold as a compliance position.** 🔵 The architecture is good engineering regardless of how
the wording reads, which is what makes this safe to propose.

## P-578-C — 🟢 Colombia `Ley 2626 de 2026` curricular-compliance programme (10–12 weeks)

🟢 **The opening is a statute with a mechanism, which is rarer than a statute.**
**`Ley 2626 de 2026`, the "Ley de Educación Digital", expedida `24 August 2026`**, obliges
**Tecnología e Informática** in *básica* and *media* to carry **computational thinking,
programming, artificial intelligence, data science and digital citizenship**; orders a
**malla curricular obligatoria, progresiva y articulada por ciclos**; obliges **MEN** to
revise lineamientos **at least every three years** with a **Comisión Nacional de Educación
Digital**; creates an **Observatorio Nacional de Educación Digital**; carries a **teacher
training and updating programme** and an **ideological-neutrality clause**; and prioritises
**rural and ethnic-community** schools. 🔴 It is **obligatory in official schools**.

🔵 **Three properties make this a programme rather than a project:** the three-year revision
cycle makes the work **recurring**; the Observatorio makes outcomes **published and
therefore auditable**; and the neutrality clause makes **content review a named
deliverable** rather than an afterthought.

**The work, in the order a ministry or secretaría will buy it.**

1. 🟢 **Curriculum mapping by cycle.** The statute names five competency domains and orders
   progression by cycle; nobody has written that mapping. 🔵 **Reuse the structure rather
   than inventing it:** UNESCO's **AI competency framework for teachers** (`15`
   competencies, `5` dimensions, `3` progression levels) and the **student AI-literacy
   framework of `18/06/2026`** (four domains — *interact, create, manage, shape*) give a
   defensible, citable skeleton. 🟢 **Spain's INTEF «Guía» v2.0 (`08/09/2026`)** is a
   ministry-published Spanish-language precedent to align to, with a **«modelo de
   declaración de uso de la IA»** and a **«semáforo de uso»** already drafted — reuse them
   and bill the integration, not the policy text.
2. 🟢 **Teacher capability at scale**, which is where the budget is. Deliver against the
   UNESCO progression levels so "trained" is a measured claim.
3. 🟢 **Instrument the Observatorio.** MEN must publish implementation and gap data; help
   define the indicators and the pipeline, because **whoever defines the measurement
   defines the next three years of procurement.**
4. 🟡 **Equity build-out.** Rural and ethnic-community priority, plus the statute's
   dotación/connectivity/electricity provisions, with the constraint that it must not
   create new fiscal burdens — so **offline-capable delivery is a requirement, not a
   preference**: [`learningequality/kolibri`](https://github.com/learningequality/kolibri)
   (**MIT**) is the component.
5. 🔴 **Content neutrality review** against the statute's clause — a named, repeatable
   deliverable.

🔴 **The supply constraint is the reason to build rather than adopt, and it is measured.**
🔴 **Spanish-language open-source education supply is `410` repositories deep and tops out
at `71★`** — a JavaScript course, not a product. Below it: teaching materials, a Moodle
attendance plugin for Chile's SENCE (`29★`), a Spanish vocational grading app (`9★`).
🔵 **There is no Spanish-language platform tier to stand on**, unlike Portuguese
(`portabilis/i-educar`, `722★`). 🟢 **Say so in the bid**: this is a build, the local
open-source supply will not carry it, and the permissively licensed pieces that *will*
carry it are horizontal and English-language.

🟡 **One caveat to state.** The statute's text was read at article level through a
**domain-restricted search** of a norms repository, **not from the Diario Oficial**, which
is unreachable from this harness (`576-B`). Article numbering and exact wording should be
confirmed against the official text before anything is warranted to a client. 🔵 The
obligations' *shape* — curricular mandate, three-year cycle, Observatorio, teacher
programme — is corroborated across four independent secondary sources.

## `p575` (2026-10-31) — two patterns: the BUILD recommendation `574-C` asked for, and the first binding-obligation package outside the EU and the US

🔵 **On the ids.** This pass files **`P-577-A`** and **`P-577-B`**, not `P-575-*`:
`P-575-A/B` and `P-576-A/B` were allocated forward by earlier passes and are live on
this page. Families stay contiguous (`568`…`577`), which is what
[`../ingest/derive-counts.py`](../ingest/derive-counts.py) checks.

## P-577-A — 🟢 Education-specific accessibility remediation agent, built on the horizontal layer because the vertical one does not exist (8–10 weeks)

🔴 **This is a BUILD recipe, and it is here because `574-C` asked the right question
and got an honest answer.** `574-C` asked whether an education-specific, permissively
licensed accessibility agent exists. 🟢 **Four axes swept, `744` repositories: it does
not.** `topic:iep` holds `34` repositories and **the largest has `7★`**;
`topic:special-education` has exactly one repository above `11★`. 🔵 **The supply is
not badly licensed — it is absent.** Meanwhile the *horizontal* layer is mature and
permissive. So you build the thin education-specific part and buy the rest.

**What you are building:** an agent that reads a course in the client's LMS, finds the
accessibility defects that actually block a student, fixes what can be fixed
mechanically, and produces the evidence trail an audit or an accommodation request
will demand.

**Components, every grant read byte-for-byte on 2026-10-31:**

| role | component | grant | why this one |
| --- | --- | --- | --- |
| **CI accessibility gate** | [guidepup/guidepup](https://github.com/guidepup/guidepup) `591★` | **MIT** (`1,068 B`) | Drives **real** NVDA and VoiceOver from a test suite. Turns a duty into a gate. |
| **Gate, cheap tier** | [guidepup/virtual-screen-reader](https://github.com/guidepup/virtual-screen-reader) `158★` | **MIT** (`1,068 B`) | Simulated screen reader — runs in CI with no assistive tech installed. Use for every commit; use the real one at release. |
| **Conformance review** | [Community-Access/accessibility-agents](https://github.com/Community-Access/accessibility-agents) `431★` | **MIT** | Eleven **WCAG 2.2 AA** review specialists. 🔴 Knows nothing about courses — that is the part you write. |
| **Course-level remediation** | [ucfopen/UDOIT](https://github.com/ucfopen/UDOIT) `117★` | 🔴 **GPL-3.0** | Already scans a **Canvas** course and fixes defects in place. **Deploy it, call it, do not vendor it.** |
| **Reading accommodation** | [Ropaxyz/EaseView](https://github.com/Ropaxyz/EaseView) | **MIT** (`1,067 B`) | Colour-overlay accommodation as a vendorable component. |
| **AAC surface** | [manavrenjith/AAC-Web_Project](https://github.com/manavrenjith/AAC-Web_Project) | **MIT** (`1,084 B`) | Permissive AAC + TTS, where the deployed platform (`cboard`) is GPL-3.0. |
| **Differentiation** | [ellmos-ai/worksheet-generator](https://github.com/ellmos-ai/worksheet-generator) | **MIT** (`1,068 B`) | Individualised worksheets — the output an IEP goal actually needs. |
| **Target of record** | [nvaccess/nvda](https://github.com/nvaccess/nvda) `2.7k★` | 🔴 **GPL-2.0** (in **`copying.txt`**) | The screen reader students use. **A test target, never a dependency.** |

**Wiring:**
1. **Gate first, before any agent.** Put `virtual-screen-reader` in the per-commit
   suite and `guidepup` driving real NVDA in the release suite. 🔵 Do this first
   because it is the only step that produces a *regression* signal — without it you
   cannot prove a remediation did not break something else.
2. **Scan with what exists.** Stand up **UDOIT** against the client's Canvas instance
   **as a deployed service** and call it over its own interface. 🔴 It is GPL-3.0:
   crossing that boundary with your own code makes your code GPL-3.0 too.
3. **Write the thin vertical layer — this is the actual build.** An agent that knows
   what a *course*, a *cohort* and an *accommodation* are: it reads UDOIT's findings
   plus the course structure, ranks defects by **which student is actually blocked**
   rather than by WCAG clause number, and routes each to a fix, a human, or an
   accommodation. 🔵 **Nothing in open source does this** — that is the finding, and
   it is why this is a build.
4. **Fix mechanically where it is safe.** Alt-text drafting, heading structure,
   table headers, contrast, caption cleanup — all reviewable diffs, none auto-merged.
5. **Emit the evidence trail, and treat it as the deliverable.** Per-course
   conformance state, dated, with the standard version named and the scan tool
   version pinned. 🔵 Per **trend 22**, the deadline moves and the obligation does
   not: the evidence trail is the durable artefact.

🔴 **Licence boundary, stated once:** everything you *ship* is MIT. **UDOIT (GPL-3.0)
and NVDA (GPL-2.0) are deployed and tested against, never linked.** Keep that line
and the deliverable stays proprietary.

🔴 **What not to do: do not start from the education-specific repositories on this
axis.** They are `1`–`7★` single-sitting projects. Read
[`littlebordercollie/mcd-together-order`](https://github.com/littlebordercollie/mcd-together-order)
(MIT, `101★`) for its **interaction design** — picture-card selection with a parent
verification step is genuinely well judged — but note it is **pre-pilot by its own
admission**: `10` commits, no student trials, one ¥12 order created and never paid.
**Copy the pattern, do not adopt the dependency.**

🟡 **Jurisdictional hooks, so the same build sells in four places:** US **ADA Title
II** (`April 26, 2027` / `2028`, WCAG 2.1 AA — dates graded `C†`, `574-E`); EU **EN
301 549** under the Web Accessibility Directive; **India** AICTE / RPwD ss. 16–18 with
GIGW 3.0 at WCAG 2.1 AA; **Australia** Disability Standards for Education 2005 (Cth),
where **Victoria requires the accessibility check *before* deployment** — the cleanest
procurement checkpoint on these shelves.

## P-577-B — 🔴 Korea high-impact AI compliance package for an education deployment (6–8 weeks, and the grace period is the window)

🟢 **Why this pattern exists now.** Korea's **AI Basic Act** and its Enforcement
Decree took effect **`22 January 2026`**, and **education is a named high-impact
sector** — the first *binding* education-specific AI obligation on these shelves
outside the EU AI Act and the US Title II rule. 🟡 **MSIT is operating at least one
year of forbearance through 2026**, deferring investigations and fines except for
serious social harm. 🔵 **So the commercial shape is unusual and worth naming: the
obligation is live, the enforcement is not yet, and a client who builds the artefacts
during the grace period pays far less than one who retrofits them after.** 🔴 A bill
proposing delay to **January 2029** is in play — the date is contested, the duty is
not.

**The five statutory duties, and the artefact each one needs:**

| duty | artefact | component |
| --- | --- | --- |
| **Risk management** | A dated risk register per deployed model, versioned with the model | 🔵 Reuse the `P-568-D` EU AI Act Annex III package — the control families overlap substantially |
| **Explanation** | Per-decision rationale a student or parent can read | 🔴 Hardest for a tutor built on RAG: log retrieved context with the output, or you cannot reconstruct the decision later |
| **User protection** | Appeal route, human contact, data boundary | — |
| **Human oversight** | A human decision point on anything consequential | 🟢 The **read-only default** of `P-568-B` is the right posture: an education agent writes nothing to a record of consequence without review |
| **GenAI output labelling** | Machine-and-human-visible marking on generated output | 🟢 Cheapest duty to satisfy and the one most often missed — do it at generation, not at render |

**Wiring:**
1. **Classify the deployment.** Any system touching teaching, assessment or student
   records in Korea is high-impact. 🔵 Assume in scope and argue out, not the reverse.
2. **Reuse the EU package.** `P-568-D` already produces the risk register, the data
   governance record and the human-oversight design. Map, do not rebuild.
3. **Instrument explanation at generation time.** Log model id, prompt version,
   retrieved context ids and output together. 🔴 **Retrofitting this is the single
   most expensive step** — a system in production for a year has no history to
   reconstruct.
4. **Label generated output at the source.** Mark it where it is produced so the mark
   survives export, copy and LMS rendering.
5. **Date the evidence and keep it.** Per **trend 22** and because the compliance date
   is contested between 2026 and 2029, the defensible position is a **continuous,
   dated trail**, not a one-off certification against whichever date holds.

🔵 **Where this lands commercially.** Korea is the one APAC jurisdiction on these
shelves with a statute rather than guidance; **Singapore** next door has a dated
*mandate* of a different kind — three compulsory teacher AI modules, one due end-2026
and two by 2027 — which is a services engagement with the same deadline shape. 🟢
**The same evidence-trail machinery serves both**, and `P-568-D` serves the EU. 🔴
**Do not sell this against Japan or China:** Japan's MEXT instrument is guidance and
its `JIS X 8341-3` version is disputed between equal-quality sources, and no Chinese
education AI or `GB`/`GB/T` accessibility instrument has been reached in two queries
(`575-D`).

🟡 **Provenance, stated plainly: every Korea and Singapore item in this pattern is
`C`-graded** — from policy trackers, law-firm briefings and local news, not from MSIT,
the statute text or MOE publications. 🔵 **`575-C` asks for the primaries** before any
of this enters a client deliverable. The control families are reliable; the dates
need first-hand confirmation.
## `p573` (2026-10-31) — two patterns, and they are the two halves of one decision

🔵 **Both come out of the eleventh pass's central finding** (see
[`../intel/trends.md`](../intel/trends.md) trend 19): the psychometric
measurement layer is **permissive in Python and GPL in R**, and the R tier is the
one a client's psychometrician and their exam board actually trust. 🟢 **Every
component grant below was read byte-for-byte this pass** from
`raw.githubusercontent.com` — `evidence/psychometrics-licence-bytes.2026-10-31-p573.tsv`
and `evidence/python-tier-licence-bytes.2026-10-31-p573.tsv`.

🔴 **Note on ids:** `P-573-*` and `P-574-A` were already consumed by earlier
passes that registered pattern ids ahead of the pass counter, so this pass —
`p573` — publishes as **`P-575-*`**. 🔵 Pattern ids on this page are **not** pass
numbers and should not be read as a chronology.

## P-575-A — 🟢 Permissive item-calibration and adaptive-testing pipeline, no copyleft anywhere (6–8 weeks)

**When to use it.** The client wants to own a closed, rebrandable assessment
product — an item bank, a calibration step and an adaptive delivery policy — and
has **no external body that must bless the psychometrics**. Corporate L&D,
certification startups, ed-tech product teams.

**Components — every grant verified first-hand, `p573`:**

| role | component | grant (first-hand) |
| --- | --- | --- |
| IRT calibration (1PL/2PL/3PL, GRM), ability estimation | [eribean/girth](https://github.com/eribean/girth) | 🟢 **MIT** (`LICENSE.txt`) |
| CAT policy: item selection, ability estimators, stopping rules, **offline simulation of examinees** | [douglasrizzo/catsim](https://github.com/douglasrizzo/catsim) | 🟢 **BSD-3-Clause** (`LICENSE`) |
| skill-level reporting: DINA / IRT / MIRT / neural cognitive diagnosis | [bigdata-ustc/EduCDM](https://github.com/bigdata-ustc/EduCDM) | 🟢 **Apache-2.0** |
| alternative/second-opinion IRT engine | [17zuoye/pyirt](https://github.com/17zuoye/pyirt) · [inuyasha2012/pypsy](https://github.com/inuyasha2012/pypsy) | 🟢 **MIT** · **MIT** |
| knowledge tracing / learner modelling over response streams | [ZhijieXiong/pyedmine](https://github.com/ZhijieXiong/pyedmine) · [HFUT-LEC/EduStudio](https://github.com/HFUT-LEC/EduStudio) · [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** ×3 |
| benchmark datasets for pre-calibration sanity checks | [bigdata-ustc/EduData](https://github.com/bigdata-ustc/EduData) | 🟢 **Apache-2.0** |
| worked reference for a *calibrated* item bank's shape | [englishcentral/ovlt](https://github.com/englishcentral/ovlt) | 🟢 **MIT** |
| permissive CAT framework if the stack is not Python | [JuliaPsychometricsBazaar/ComputerAdaptiveTesting.jl](https://github.com/JuliaPsychometricsBazaar/ComputerAdaptiveTesting.jl) | 🟢 **MIT** |

**Wiring.**
1. **Item bank in** (CSV / QTI export from the client's LMS) → normalise to a
   response matrix. Use `EduData`'s loaders as the schema reference rather than
   inventing one.
2. **Calibrate with `girth`** → persist item parameters (`a`, `b`, `c`) in a
   plain table the client owns. This table, not the code, is the asset.
3. **Validate the adaptive policy offline in `catsim`** *before* any learner sees
   it: simulate examinees at known ability levels, check that the policy recovers
   their θ within tolerance and respects content constraints. 🟢 **This is the
   step that substitutes for the learner-simulation agent this KB cannot legally
   ship** — the gap is registered as `573-A` in [`../intel/open-gaps.md`](../intel/open-gaps.md). 🔴 **Pointer corrected `p590`:** this line cited `../agents/top.md` as `573-A`'s home and that page contains **no** occurrence of the id, so the reference was dangling at its destination, not merely unregistered.
4. **Skill profiles with `EduCDM`** → "mastered / not mastered" per named
   competency, which is what a certification report has to say.
5. **Re-estimate on live data** with `pyedmine` or `pykt-toolkit` for drift.

🔴 **The honest limitation, state it in the proposal.** This pipeline is
permissive end to end and the client may keep every modification closed. 🔴 **It
is *not* the toolchain an exam board, ministry or journal reviewer will recognise.**
If that recognition is required, this pattern is the wrong half of the decision —
use `P-575-B`, or run `P-575-B` as a one-off external validation of the parameters
this pipeline produced.

🔵 **Weeks:** 1–2 ingest and schema; 3–4 calibration and parameter store; 5–6
`catsim` policy validation harness; 7–8 skill reporting and drift job.

## P-575-B — 🟡 Arm's-length GPL psychometrics: use `mirt` and `TAM` without creating a derivative work (4–6 weeks)

**When to use it.** The client's psychometrician, awarding body, ministry or
academic board **requires output from the canonical R packages**. That is a
reasonable requirement, not a preference — these are the implementations the
field's evidentiary standards were written around.

**Components — all grants read from `DESCRIPTION`, `p573`:**

| role | component | grant (first-hand) |
| --- | --- | --- |
| multidimensional IRT, DIF, item fit, plausible values | [philchalmers/mirt](https://github.com/philchalmers/mirt) | 🔴 **GPL (>= 3)** |
| Rasch/2PL/3PL calibration, plausible values, weighting (large-scale assessment) | [alexanderrobitzsch/TAM](https://github.com/alexanderrobitzsch/TAM) | 🔴 **GPL (>= 2)** |
| **linking and equating**, local dependence, invariance | [alexanderrobitzsch/sirt](https://github.com/alexanderrobitzsch/sirt) | 🔴 **GPL (>= 2)** |
| Q-matrix validation, classification accuracy | [Wenchao-Ma/GDINA](https://github.com/Wenchao-Ma/GDINA) | 🔴 **GPL-3** |
| Bayesian DCM with built-in fit and reliability output | [r-dcm/measr](https://github.com/r-dcm/measr) | 🔴 **GPL (>= 3)** |
| content-constrained multidimensional CAT | [Karel-Kroeze/ShadowCAT](https://github.com/Karel-Kroeze/ShadowCAT) | 🔴 **GPL-3** |
| latent-variable / SEM work where a **permissive** engine suffices | [OpenMx/OpenMx](https://github.com/OpenMx/OpenMx) | 🟢 **Apache-2.0** |

**The posture, and it is an engineering boundary rather than a licence
negotiation.** GPL obligations attach to **distributing a derivative work**. So:

1. 🟢 **Run the R tier as its own process, in its own container, from unmodified
   upstream CRAN sources**, with the upstream `LICENSE`/`DESCRIPTION` files
   shipped intact alongside it.
2. 🟢 **Cross the boundary with data, not linkage** — files, or a thin HTTP
   endpoint (`plumber`), or batch `Rscript`. **Calibration output is data; data is
   not a derivative work.**
3. 🟢 **The client operates that container.** Globant's deliverable is the
   orchestration, the item bank, the UI and the audit trail — none of which
   links, embeds or statically compiles any GPL code.
4. 🔴 **Do not:** vendor modified copies, statically link, embed R into a
   proprietary binary, or ship a single artefact that contains both the GPL
   packages and the closed product.

🟢 **Two pieces of genuine relief worth putting in front of the client's
counsel.** 🟢 **First: none of these packages is AGPL.** `p573` read every grant
and found GPL-2, GPL-3 and LGPL only — so **there is no §13 network
source-offer obligation**, which is the clause that makes hosted deployments
painful. 🔵 This matters because this base's own naive copyleft detector has
previously misgraded GPL-3 as AGPL-3 (its §13 cites Affero by name); the
`DESCRIPTION` read settles it. 🟢 **Second: the separate-process posture also
sidesteps the GPL-2/GPL-3 compatibility problem** — `TAM`, `sirt` and `CDM` are
GPL (>= 2) while `GDINA` and `ShadowCAT` are GPL-3, and combining those into one
linked artefact raises a question that **never arises if nothing is linked.**

🔴 **Limitation, stated plainly: this is an engineering posture, not legal
advice.** The client's counsel signs off on the boundary before the first
`Rscript` runs. 🔵 And if the client's own policy forbids GPL anywhere in the
estate — some do, regardless of linkage — then `OpenMx` (Apache-2.0) is the only
R row that survives, and the honest answer is that it covers latent-variable
modelling but **not** IRT calibration or equating. At that point go back to
`P-575-A` and tell the client what evidentiary standing they are trading away.

🔵 **Weeks:** 1 boundary design and counsel sign-off; 2–3 containerised R service
with pinned CRAN versions and licence manifest; 4 calibration and equating runs
reproduced against the client's historical data; 5–6 audit trail, versioned
parameter releases, handover.


## `p572` (2026-10-31) — three patterns, every component licence read byte-for-byte this pass

### 🟢 `P-572-A` — Handwritten coursework → marked feedback, permissive end to end

🔵 **The job:** a school or university receives work on paper, wants it digitised,
marked against a rubric, and the outcome recorded where analytics can see it.
🟢 **Every component below carries a first-hand permissive grant read this pass,
and the one trap on the obvious path is named.**

| stage | component | licence (read) | note |
| --- | --- | --- | --- |
| 1. segment | [`githubharald/WordDetector`](https://github.com/githubharald/WordDetector) | **MIT** 1,071 B | classic CV — **no model, no GPU**; turns a scanned sheet into word crops |
| 2. ⛔ *do not* deslant with | [`githubharald/DeslantImg`](https://github.com/githubharald/DeslantImg) | MIT grant / **GPL-3.0 surface** | `Py-BOBYQA>=1.3` is GPL-3.0 and in-process — **skip this stage or reimplement it** |
| 3. recognise | [`arthurflor23/handwritten-text-recognition`](https://github.com/arthurflor23/handwritten-text-recognition) | **MIT** 1,074 B | 3,645 commits; ⚠️ its default path pulls `openai`, a **paid external API** — swap for a local model where student data cannot leave |
| 4. decode | [`githubharald/CTCDecoder`](https://github.com/githubharald/CTCDecoder) | **MIT** 1,071 B | beam/lexicon/prefix search; **a lexicon raises accuracy on subject vocabulary** |
| 5. mark | [`patil-suraj/question_generation`](https://github.com/patil-suraj/question_generation) + an LLM marker | **MIT** 1,068 B | over-generate → rank → gate, per `P-574-A` |
| 6. return the grade | [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | **MIT** 1,070 B | LTI 1.3 **Assignment & Grade Services** passback into the LMS the client already runs |
| 7. record | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | **Apache-2.0** 11,357 B | xAPI statements; the analytics substrate |

🔵 **Wiring:** scan → `WordDetector` crops → `handwritten-text-recognition`
logits → `CTCDecoder` with a subject lexicon → text → rubric marking →
`pylti1.3` AGS grade passback → xAPI statement to `lrsql`.
🟢 **Licence posture: MIT/Apache-2.0 throughout, nothing copyleft, nothing
NonCommercial, and the single GPL-3.0 exposure on the obvious path is excluded by
name.** 🔵 **Shape:** 6–8 weeks for one subject and one LMS; stages 1–4 are the
risk, 6–7 are a week.

### 🟢 `P-572-B` — Attach AI to the LMS the client already runs, without forking it

🔵 **The job:** the client runs Moodle, Canvas or Open edX. They want agent
features. Forking is the instinct and it is the expensive mistake — **Open edX and
Canvas are AGPL-3.0, so a hosted fork owes source to its users under §13.**

🟢 **The licence-safe spine, by platform:**

| platform | attach with | licence | why this and not a fork |
| --- | --- | --- | --- |
| Moodle (GPL-3.0) | [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) | **Apache-2.0** | PHP-native, IMS-certified; the tool stays yours |
| Canvas (AGPL-3.0) | [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) | **MIT** | courses, assignments, submissions, rubrics, quizzes; **grades and comments from any agent** |
| Open edX (AGPL-3.0) | [`openedx/XBlock`](https://github.com/openedx/XBlock) | **Apache-2.0** | 🟢 **the key fact: components are Apache-2.0 even though the platform is AGPL-3.0** — client course logic stays permissive |
| any / Python | [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | **MIT** | the generic LTI 1.3 route |
| analytics | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | **Apache-2.0** | one xAPI store behind all of them |

🔵 **Wiring:** agent service (your code, your licence) ← LTI 1.3 launch / MCP ←
LMS. Grades return over **AGS**; events land in `lrsql`; **no platform source is
modified, so no platform licence reaches the client's code.**
🟢 **This is the pattern that makes the copyleft question go away**, and it is why
the integration tier added this pass matters more than any platform on the shelf.
🔵 **Shape:** 4–6 weeks per platform; the second platform is half the first.

### 🟡 `P-572-C` — Teacher lesson-planning pack, local-first for data residency

🔵 **The job:** teachers want lesson plans, courseware, item banks and marking help
in their own template, and the procurement blocker is almost never features — it is
**whether student data leaves the building**.

🟢 **Reference implementations to study, both MIT, both read this pass:**
[`LeonhardJY/dsh-teacher-kit`](https://github.com/LeonhardJY/dsh-teacher-kit)
(MIT, 1,071 B) — **states it runs fully on the local machine, no network, no data
collection**, and covers exam papers, item-bank assembly, dictation sheets, lesson
plans, courseware and `docx`/`pptx` batch processing against the school's own blank
template; and
[`revjake1/lesson-plan-magic`](https://github.com/revjake1/lesson-plan-magic)
(MIT, 1,069 B) — fills a **US district** template and targets standards alignment.

🔴 **Both are thin (7 and 16 commits). Treat them as the specification, not the
dependency** — the feature chain they converge on independently
(**lesson plan → courseware → item bank → dictation → marking**) is the
transferable asset.

⛔ **Two components a naive build would reach for and must not:**
[`chewyenhan/malaysia-uec-teacher-workflow`](https://github.com/chewyenhan/malaysia-uec-teacher-workflow)
— its `SKILL.md`, `agents/` and `references/` are **CC BY-NC-SA 4.0**; and
[`xiaoyang111222/cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy)
— its prerequisite graph is **CC BY-NC 4.0**. 🔵 Both are excellent and both are
NonCommercial; read them for structure and build the artefact fresh.

🔴 **Declared gap (`572-C`): there is no permissively licensed, curriculum-aligned
prerequisite knowledge graph on these shelves.** The best one located —
`cn-math-taxonomy`, 1,644 nodes and 2,403 edges — is NonCommercial, and the
adaptive-sequencing layer of this pattern therefore has **no permissive supply**.
Said plainly rather than filled with something that does not exist.

🔵 **Shape:** 6–8 weeks, and the local-only deployment posture is the deliverable
as much as the prompts are.

## P-568-A — LTI-attached AI tutor over a copyleft LMS (6–8 weeks)

**For:** any client on Moodle, Open edX, Canvas or Chamilo who wants AI tutoring
inside their existing LMS without a platform migration or a licence problem.
**Regions:** all. This is the default engagement shape.

**Wiring:**
1. **Tutor core** — [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor)
   (Apache-2.0, 52k★, `v1.7.0`). Deploy from `ghcr.io/hkuds/deeptutor`. Apache-2.0
   permits commercial use and the derivative stays yours.
2. **Mastery model** — [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) (MIT).
   Take its **Bayesian Knowledge Tracing** implementation as the per-skill
   mastery estimator rather than letting the LLM self-assess mastery. This is the
   step that makes the tutor defensible under "proven instructional benefit."
3. **Attachment** — [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs)
   (Apache-2.0). Wrap the tutor as an LTI 1.3 tool provider: Deep Linking so
   instructors place it in a course, Names and Role Provisioning for roster and
   role, **Assignment and Grade Services to write results back to the gradebook**.
   Zero lines of LMS code modified.
4. **Telemetry** — emit [xAPI](https://github.com/adlnet/xAPI-Spec) (Apache-2.0)
   statements into [`openfun/ralph`](https://github.com/openfun/ralph) (MIT) as
   the LRS.
5. **Acceptance gate** — score the tutor on
   [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark)
   (MIT) **before** go-live and keep the score as release evidence.

**Why it holds up:** steps 1–5 are Apache-2.0/MIT throughout. The client's
AGPL obligations are never triggered because their platform is never modified.

---

## P-568-B — Canvas agent fleet with a read-only default (3–4 weeks)

**For:** institutions on Canvas wanting agent access to course data for staff and
students. **Region:** North America primarily (Canvas's install base, and the
verified agents are North American).

**Wiring:**
1. **Base server** — [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp)
   (MIT, 310★, `v1.16.0`). The most established option; also ships ready-made
   agent skills — **pre-semester course audit** and **accessibility auditor** —
   which are deliverables on their own and the fastest demonstrable value here.
2. **Lean alternative** — [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms)
   (MIT per README, `v2.2`, 54 tools) where a smaller, containerised surface is
   preferred over maximum coverage.
3. **Write-surface decision, made explicitly.** Tool counts here run from 54 to
   128 and some tools mutate LMS state (submit, grade, delete). Enumerate the
   tool list of the exact version you deploy, classify each tool read vs. write,
   and **expose the read set by default**; every write tool is enabled
   deliberately, per role, never by default. Do not infer the surface from the
   README — tool counts are version-specific and the README and sidebar of the
   same repo disagree.
4. **Grades stay on the sanctioned path.** Writes back to the gradebook go
   through LTI AGS (`ltijs`), not through an MCP write tool — AGS is the
   auditable, spec-sanctioned channel.
5. **Audit** — xAPI → `ralph`, so every agent action against student data is
   reconstructible. This is what satisfies a district AI policy.

---

## P-568-C — District AI policy instrumentation, North America (8–10 weeks)

**For:** US districts and state education agencies. **Region:** North America.
**Driver:** Maryland, Idaho, Oklahoma and Virginia now **require** state guidance
*and* district-level AI policy adoption; 134 bills across 31 states in 2026. Most
US public schools have no formal student AI policy. This is statutory work
districts cannot self-serve.

**Wiring:**
1. **Policy → machine-checkable rules.** Translate the district's adopted AI
   policy into enforceable predicates, not a PDF. The NY A 9190 shape —
   classroom AI restricted to **grade 9 and above, with exceptions for
   diagnostics and special education** — is the worked example: it requires
   per-cohort age gating plus a documented exception path.
2. **Enforcement point** — the MCP layer from **P-568-B**. Roster and role come
   from LTI Names and Role Provisioning (`ltijs`, Apache-2.0), so grade-level
   gating is driven by the SIS's own data rather than a hand-maintained list.
3. **Evidence layer** — xAPI into `ralph` (MIT), retained as the compliance
   record: who used which AI tool, in which course, under which policy version.
4. **Instructional-quality evidence** — `pedagogy-benchmark` (MIT) scores on any
   tool the district approves, including the special-educational-needs subset
   (**SEND, 223 questions**), which maps directly onto the special-education
   exception the statutes carve out.
5. **Deliverable.** Policy document, enforcement configuration, audit pipeline,
   and a per-tool evaluation report — the four artefacts a district needs to show
   it complied.

**Procurement note:** the contested USD 10 m Khanmigo earmark in North Carolina
SB 1006 shows large single-vendor AI tutoring buys are politically exposed.
Platform-neutral, policy-first work is the easier sell.

---

## P-568-D — EU AI Act Annex III conformity package (10–12 weeks)

**For:** EMEA institutions and edtech vendors whose systems evaluate learners or
affect access to qualifications — **Annex III high-risk** under the EU AI Act.
**Region:** EMEA.

**Timing, which is the whole reason to run this now:** stand-alone Annex III
obligations were **deferred to 2027-12-02** (Digital Omnibus, in effect late July
2026), and embedded-in-product to 2028-08-02. That is a ~14-month readiness
runway. Guidance still claiming August 2026 is superseded.

**Wiring:**
1. **Substrate choice matters here.** Where the client wants a
   licence-clean European build rather than an attachment,
   [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) (Apache-2.0 per
   README badge, Switzerland) is the only permissively licensed institutional LMS
   verified in this KB. Otherwise attach to Moodle via `ltijs` as in P-568-A.
2. **Human oversight, built in, not bolted on.** Implement the
   lesson-plan/assessment flow as **draft-for-teacher-review** — the shape
   Educativa reports the market converging on and the shape Annex III requires.
   The teacher's approval event is an xAPI statement, so oversight is evidenced
   rather than asserted.
3. **Evaluation evidence** — `pedagogy-benchmark` (MIT) gives reproducible,
   documented pedagogical-knowledge scores for the technical documentation pack.
4. **Telemetry under data-protection constraint** — self-host `ralph` (MIT) in
   region; xAPI's actor model lets you pseudonymise the learner at emission.
5. **Package** — risk classification memo, human-oversight design, technical
   documentation, evaluation results, post-market monitoring plan.

**Also in scope for EMEA:** the December 2026 ban on certain AI-generated
intimate imagery and abuse material — a content-safety obligation on any
deployment handling student-generated media, and it lands *before* the high-risk
duties.

---

## P-568-E — LATAM institutional AI strategy, from 87% use to 26% strategy (6–8 weeks)

**For:** Latin American universities and ministries. **Region:** LATAM.
**Driver:** UNESCO IESALC / UNU-IAS across 200 institutions in 19 countries —
**87% already use AI somewhere, only 26% have a formal strategy**, with adoption
driven by individuals rather than institutions. The client's problem is not
starting; it is that it already started without them.

**Wiring:**
1. **Shadow-use census first.** The engagement opens by measuring what is
   already in use, because individual-led adoption means nobody has the list.
   `ralph` (MIT) as LRS plus xAPI emission from sanctioned tools turns shadow use
   into an inventory.
2. **Strategy artefacts on UNESCO's own recommendations** — fold higher education
   into the national AI strategy, develop institutional guidance, fund it, and
   **integrate AI literacy and governance into accreditation and quality
   assurance**. That last one is the procurement wedge: accreditation is already
   a budgeted, calendared institutional function, so the work attaches to an
   existing budget line rather than requesting a new one.
3. **Public-sector build path, Brazil** —
   [`portabilis/i-educar`](https://github.com/portabilis/i-educar) (**GPL-2.0**,
   722★) is the reference municipal platform for *Secretarias de Educação*.
   GPL-2.0 means the AI layer attaches over LTI/xAPI; an i-educar fork would have
   to be released.
4. **Spanish/Portuguese-language capability** — Chamilo (GPL-3.0) has a notable
   LATAM and francophone install base and is a second common platform of record.
5. **Convening route** — the **UNESCO Observatory on AI in Education for Latin
   America and the Caribbean**, launched 2026-04-14 in Santiago with **CAF**
   (Development Bank of Latin America and the Caribbean). Partners include CENIA
   (Chile), Cetic.br (Brazil), ECLAC, Fundación Ceibal (Uruguay), Fundación
   Santillana, Tecnológico de Monterrey, ProFuturo and IRCAI. A funded regional
   body with a named partner list is a better entry point than institution-by-
   institution outreach.

---

## P-568-F — Africa: national strategy to institutional policy, offline-first (8–10 weeks)

**For:** a ministry or university system in a country with a national AI
strategy on paper and no institutional capacity behind it. **Region: EMEA**
(Africa sits inside the EMEA value — see
[`../intel/market.md`](../intel/market.md)).

**Why this pattern now exists.** The first pass of this KB declared "no
Africa-specific pattern" because the *demand evidence was missing*, while naming
Kolibri as the obvious component. The second pass found the evidence, so the
pattern can be written: **AU Continental AI Strategy** names education a
priority sector; **Zimbabwe** (National AI Strategy 2026–2030) and **Ghana**
(2025–2035, plus a July 2026 draft curriculum putting **AI literacy in
kindergarten through Primary 6**) have funded mandates; and only **14%** of
higher-education respondents can confirm their institution has an AI policy,
against **69% who do not know** (Frontiers, 2026).

**The two constraints that shape it:** connectivity cannot be assumed, and the
deficit is *institutional awareness*, not tooling. A cloud-first tutor
deployment answers neither.

**Wiring — permissive and offline-capable end to end:**
1. **Delivery substrate** —
   [`learningequality/kolibri`](https://github.com/learningequality/kolibri)
   (**MIT**, 1.2k★). Offline-first by design; the only platform in this KB built
   for intermittent connectivity. MIT means the deployment and any derivative
   stay licence-clean.
2. **Institutional corpus** —
   [`DSpace/DSpace`](https://github.com/DSpace/DSpace) (**BSD-3-Clause**, 1.1k★)
   as the repository of record for curriculum material, theses and local
   language content. Permissive, so a client-specific derivative is permitted —
   see P-568-G.
3. **Model hosting** — local/edge inference, not an API dependency. The
   connectivity constraint and the data-residency question resolve the same way.
4. **Curriculum alignment artefact** — the **Ghana KG–P6 AI-literacy curriculum
   draft** is the most procurement-ready single item in the region. Build the
   content packs against it; they are reusable across Anglophone systems.
5. **Policy instrumentation** — the deliverable that closes the 69%
   don't-know gap is *not* software: an institutional AI policy template derived
   from the national strategy, plus the training records and usage telemetry
   (xAPI → [`openfun/ralph`](https://github.com/openfun/ralph), MIT) that prove
   it is live. Ship this *first*; it is what the mandate is actually missing.
6. **Quality gate** —
   [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark)
   (MIT), whose **SEND** subset (223 questions) matters in systems with limited
   specialist-teacher provision.

**Why it holds up:** steps 1, 2, 5 and 6 are MIT or BSD-3-Clause — **the only
pattern in this document with no copyleft component anywhere in it**, because
Africa's institutions are less likely to be locked to an incumbent Moodle or
Canvas estate. That is the one structural advantage of a late-starting market.

**Sell it on the strategy, not the software.** The buyer has a national mandate
and no implementation path. Lead with step 5.

**Caveats, stated plainly.** South Africa's draft National AI Policy status is
**contested** (Gazette Notice 3880 of 2026 versus a tracker marking it
withdrawn) — do not build a pitch on it without the primary record. Namibia has
no national strategy at all. And the **supply side of this region is unmapped**:
no African education platform or agent repository appears anywhere in this KB,
so every component above is imported. Partnering locally is a gap-closing move,
not a courtesy.

---

## P-568-G — Permissive research-corpus agent on DSpace (4–6 weeks)

**For:** a university that wants AI discovery over its own scholarly output —
theses, datasets, faculty publications, grey literature — and wants to **own the
result**. **Regions:** all.

**Why this is the exception in this document.** Every other pattern here is an
*attachment* to something Globant may not fork. This one is not.
[`DSpace/DSpace`](https://github.com/DSpace/DSpace) is **BSD-3-Clause** —
verified in the sidebar and in `LICENSE` on `main` ("Copyright (c) 2002-2021,
LYRASIS") on 2026-10-31. It is the **only platform of record in this KB that
permits a proprietary derivative.** If a client needs owned IP in the substrate
rather than beside it, this is the one place in the education stack where that is
available, and it happens to sit on the corpus a RAG agent most wants.

**Wiring:**
1. **Substrate** — DSpace (BSD-3-Clause). Fork or extend freely; the derivative
   may stay closed. Java.
2. **Retrieval layer** — build it *into* the repository rather than beside it,
   which the licence permits and which is why this pattern is shorter than
   P-568-A: no LTI handshake, no plugin approval, no change-control queue on
   someone else's AGPL platform.
3. **Agent surface** — reuse the MCP shape the rest of the field has
   standardised on (four of six agents in [`../agents/top.md`](../agents/top.md)
   are MCP servers) so the corpus is reachable from whatever assistant the
   institution adopts later. Do not invent a bespoke connector.
4. **Course-facing delivery** — when results need to appear inside the LMS,
   attach *that* step with [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs)
   (Apache-2.0). The copyleft boundary applies to the LMS, not to DSpace.
5. **Library-system adjacency** — if the engagement also touches the catalogue,
   [`Koha-Community/Koha`](https://github.com/Koha-Community/Koha) is **GPL-3.0**:
   back inside the attach-don't-fork rule. Note Koha takes contributions through
   its **own bug tracker, not GitHub issues** — plan the upstreaming path.

**The trap to avoid:** DSpace's permissive licence tempts a full fork. Fork only
what the retrieval layer needs and track upstream, or the client inherits a
maintenance burden on a Java platform in exchange for IP they may not need.

**Honest sizing.** DSpace is 1.1k★ — an order of magnitude below Moodle or
Canvas. This is a narrower engagement than the LMS patterns and should be priced
and pitched as such. Its value is the licence position, not the market size.

---

## P-568-H — APAC award-integrity and assessment reform, Australia-first (8–10 weeks)

**For:** Australian higher-education providers (and the ASEAN institutions that
follow TEQSA's lead) that have an institutional gen-AI action plan on file and no
operational governance behind it.
**Region:** APAC.

**Why this is now a pattern rather than a note.** The previous pass declined to
write an APAC recipe, on the view that the region needed P-568-D run per
jurisdiction. Two pieces of evidence found on this pass change that: TEQSA
required a credible gen-AI action plan addressing **risk to award integrity**
from *every* Australian provider and received a **100% response rate**, and a
peer-reviewed AJET national document analysis of **39** universities found
operational governance structures documented in only **7**. So there is a named
population of ~32 institutions that have a filed plan, a regulator that has read
it, and no machinery underneath. That is a pattern, not a per-country variant of
an EU one — the driver is **award integrity**, not conformity assessment.

**Wiring:**
1. **Pick the assessment posture first.** TEQSA's own follow-up resource names
   three that have emerged: programme-wide assessment reform, assuring learning
   in every unit, or a combination. This is a curriculum decision and it sets
   everything downstream — do not start with tooling.
2. **Attach to Moodle, which is a home-region product.** Moodle HQ is in Perth.
   Use [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (Apache-2.0) for the
   LTI 1.3 boundary, and
   [`G36maid/moodle-mcp`](https://github.com/G36maid/moodle-mcp) (MIT, Rust) for
   agent read access — it is validated against **Moodle 3.7 → 5.x**, which
   matters because APAC institutional estates run old versions. Borrow the design
   choice of the AGPL-licensed `csmediapro/moodle-mcp-server` without using it:
   work through **Moodle Web Services** so no plugin install is needed on the
   client's server, which is usually the real blocker.
3. **Instrument integrity as evidence, not assertion.** Every AI-assisted step in
   an assessment flow emits an **xAPI** statement into a self-hosted
   [`openfun/ralph`](https://github.com/openfun/ralph) (MIT) LRS: what the student
   was shown, what the agent drafted, which human approved it. Award integrity is
   an evidentiary claim and this is what makes it auditable.
4. **Gate the generated material.** Score assessment items with
   [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators)
   (rubrics — **clear its licence at step 0**) and the model's pedagogical
   knowledge with [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark)
   (MIT). Without this the deliverable is an opinion.
5. **Package:** the governance structures the AJET study found missing —
   decision rights, escalation path, review cadence, a register of AI-touched
   assessments — plus the xAPI evidence trail and the evaluation results.

**Adoption-risk section is mandatory in this region, and cite Korea for it.**
South Korea's AI textbooks reached **below 30% adoption by March** and lawmakers
then **removed their official status**. Contrast Singapore, which mandated
*teacher capability* first (one compulsory AI module by end 2026, two more
recommended by end 2027). The lesson to put in front of an executive sponsor:
**fund the teacher, not the artefact.**

**Per-jurisdiction note (still true):** for Vietnam — risk-based law effective
**2026-03-01**, with education and automated assessment named high-risk — and for
Korea's AI Basic Act (in force **2026-01-22**, guidance-first grace period
through 2026), run **P-568-D**'s conformity artefacts against local thresholds.
The artefacts are the same; the thresholds differ.

---

## P-568-I — Multi-agent interactive classroom on OpenMAIC (4–6 weeks)

**For:** any client who wants course material turned into taught, interactive
lessons rather than documents — corporate L&D, exam-prep providers, universities
building a self-study track.
**Region:** Global (component origin APAC).

**Why this pattern exists now.** [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC)
is **MIT**, **41,981★**, TypeScript, `v1.3.0` dated 2026-10-29, from Tsinghua —
and it did not exist when this KB's earlier patterns were written (repo created
2026-03-11). It is the largest permissively licensed, *deployable* education
application in existence: topic or uploaded documents in, interactive lesson out,
with AI teachers **and AI classmates**, slides, quizzes, simulations, speech,
whiteboard and live discussion. MIT means the client owns the derivative.

**Wiring:**
1. **Stand it up on its own stack, not the client's LMS.** Node.js ≥ 22.19,
   pnpm ≥ 10, PostgreSQL 16. It is a separate application by design — which is
   exactly what the copyleft constraint wants.
2. **Attach it to the LMS of record across LTI 1.3** with `ltijs` (Apache-2.0):
   launch a lesson from inside Moodle/Canvas, write the quiz result back through
   Assignment & Grade Services. The client's platform is never touched.
3. **Feed it the client's corpus.** Its document-to-lesson path is the integration
   point. Where the material is scattered across an institutional repository, pull
   from **DSpace** (BSD-3-Clause) as in P-568-G.
4. **Use its export formats as the commercial hedge.** It exports **PPTX**, a
   **single offline HTML file**, and a classroom ZIP. The offline HTML export is
   the answer to low-connectivity delivery *and* to a client who will not host a
   new service: you can ship the artefact without shipping the platform.
5. **Add retention.** OpenMAIC teaches; it does not schedule revision. Pair with
   [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) (MIT,
   539★) so an agent writes cards into a real spaced-repetition scheduler instead
   of a reimplemented one.
6. **Gate and evidence it** exactly as in P-568-H step 4 and step 3.

**Risks to state plainly.** 211 open issues and eight months of existence. Pin a
commit, not a tag, and budget for upstream churn. Its origin is a Chinese
university, which is a procurement question in some public-sector contexts and
should be raised early rather than discovered at security review.

---

## P-568-J — Permissive AI-native LMS substrate, EMEA (6–8 weeks)

**For:** corporate L&D and compliance-training clients who want an AI-native
learning platform they can **own, rebrand and keep closed** — not an attachment
to someone else's copyleft LMS.
**Region:** EMEA.

🔴 **CORRECTED `p585` (2026-11-01):** the claim *"every platform of record is copyleft"* is **false** and was withdrawn as `Trend 36`. Four platforms of record are permissive and forkable: **Sakai** (ECL-2.0, 1,240★), **OpenOLAT** (Apache-2.0, 449★), **Kolibri** (MIT, 1,163★) and **relate** (MIT, 437★) — all four read from their own licence files. See [`../repos/foundations.md`](../repos/foundations.md). The statement below is retained as written for history.


**Why this is newly possible.** Every previous pattern in this file is an
*attachment*, because every platform of record is copyleft. [`Selleo/mentingo`](https://github.com/Selleo/mentingo)
is **MIT**, from **Selleo (Poland)**, and describes itself as a self-hosted
alternative to Moodle, Docebo, TalentLMS, Thinkific, Teachable and Open edX, with
an AI Mentor and role-play, **SCORM and xAPI** built in, and white-labelling as a
stated goal. It is the first time this KB can offer substrate replacement rather
than boundary attachment.

**Wiring:**
1. **Fork it, and mean it.** MIT: the derivative is the client's. This is the
   whole point of the pattern and the only reason to prefer it over P-568-A.
2. **Keep the standards boundaries anyway.** It ships xAPI, so point telemetry at
   a self-hosted `openfun/ralph` (MIT, France) rather than its internal store —
   that keeps analytics portable if the client later outgrows it. SCORM support
   is the migration path *in* from an incumbent LMS.
3. **Compose the tutor layer rather than writing one.** `Li-Evan/Bloom` (MIT) for
   Socratic tutoring, `GeminiLight/SocialCoach` (Apache-2.0) for the role-play
   and conflict-handling content that maps directly onto compliance training, and
   `dmoshehun-prog/learn-from-materials` (MIT) to turn the client's existing PDFs
   and policies into traceable lessons.
4. **An entirely permissive, entirely EMEA-origin stack is assemblable** —
   `mentingo` (Poland, MIT) + `ralph` (France, MIT) + `ltijs` (Apache-2.0) +
   `pedagogy-benchmark` (MIT). For a client with data-sovereignty or
   supply-chain-origin requirements, that combination is the differentiator;
   state it explicitly in the proposal.

**Risks to state plainly, because this one is easy to oversell.** 102★, 31 forks,
**105 open issues**. SSO, accessibility conformance, data residency and
Moodle migration were **not** verified by this KB. Scope a two-week technical
spike against the client's actual non-functional requirements *before* committing
to substrate replacement; if the spike fails, fall back to P-568-A, which is
mature.

---

## P-568-K — Governance harness for agent-skill deliverables (3–4 weeks)

**For:** any client adopting education AI that arrives as **agent skills** —
markdown instruction bundles loaded by Claude Code, Codex, OpenCode, Cursor or
Antigravity — rather than as a hosted application.
**Region:** Global.

**Why this is the most contemporary pattern in this file.** **Six of the
fourteen** agents on [`../agents/top.md`](../agents/top.md) are skill bundles, and
`topic:agent-skills topic:education stars:>50` returns 13 repositories led by one
at 4,843★. A skill bundle has **no runtime to monitor, no semver by convention,
no test suite by convention**, and its behaviour changes when the harness or the
underlying model changes — neither of which the client controls. Clients are
adopting these today with no governance at all.

**Wiring:**
1. **Licence-screen every bundle first** (step 0 above). This cohort is where the
   defects are: the largest member is **CC BY-SA 4.0** (share-alike on the skill
   text), the second-largest (**2,750★**) has **no licence**. A skill bundle looks
   like documentation and is governed like a work of authorship.
2. **Pin the harness and the model, and write both into the contract.** The
   deliverable is a prompt contract evaluated by a third party's runtime. If the
   model version is not pinned, the behaviour the client accepted is not the
   behaviour they will get.
3. **Build the regression suite the ecosystem does not have — and source your own
   corpus.** Freeze a golden set of task → expected-property pairs for the
   client's own syllabus. Score with `learning-commons-org/evaluators` for content
   quality and `pedagogy-benchmark` (MIT, 1,143 teacher-qualification questions)
   for pedagogical knowledge. Run it on every harness or model change. **This is
   the missing runtime-monitoring layer identified in
   [`../intel/trends.md`](../intel/trends.md), built by hand because nothing
   open-source provides it.**

   ⚠️ **Licence correction, fourth pass — read this before quoting the work.**
   `evaluators` is a **three-tier grant** (`main/LICENSE.md`, 1,615 B, read
   first-hand): the **code is MIT** and the **rubric prompts and settings are
   CC BY 4.0**, both fine commercially with attribution — but its **Annotated
   CLEAR Corpus** and **Annotated PERSUADE 2.0 Corpus** are **CC BY-NC-SA 4.0,
   non-commercial**, and the upstream originals are NC too, so there is nothing
   cleaner to substitute. **The scoring machinery goes into a billable
   deliverable; those two corpora do not.** The golden set must be built from the
   client's own syllabus and assessed work — better practice anyway, since a
   client-specific corpus is what makes the suite meaningful, but now also a
   licence requirement. **Price the corpus construction explicitly**; it is the
   line nobody budgets for.
4. **Check curriculum alignment, do not assume it.** `learning-commons-org/knowledge-graph`
   (code MIT, datasets per-publisher, ships an MCP server) links academic
   standards and curricula; where the client has no rich national standard, use
   `AI-for-Education/gpf-alignment` (MIT) against the **Global Proficiency
   Framework**.
5. **Require citation provenance as an acceptance criterion.** Prefer bundles
   engineered for it — `ZeKaiNie/universal-examprep-skill` (MIT) teaches from the
   instructor's own slides **with page citations** and is explicitly built against
   hallucination. Then cite the reason: **South Africa's draft National AI Policy
   was withdrawn because at least 10% of its academic references were
   fictitious.** That is the cheapest executive-level argument available for
   provenance work, and it is a matter of public record.

**What the client is buying.** Authoring and maintenance, not hosting. Say so in
the pricing conversation: infrastructure cost collapses, and the
recurring-revenue story has to be the regression suite and the model-upgrade
re-certification, not the servers.

---

## P-569-A — SCORM courseware delivery into an untouched LMS (4–6 weeks)

**For:** any client whose platform of record is copyleft (Moodle, Open edX,
Canvas, Chamilo) and who wants **AI-generated or AI-assisted courseware delivered
into it** without a platform project, an xAPI migration, or an LTI integration
review.
**Region:** Global. Strongest fit where procurement specifies SCORM by name,
which in practice means corporate L&D, compliance training and public-sector
tenders.

**Why this pattern exists, and why it did not until now.** Three passes of this
KB built the attach doctrine on **LTI 1.3**, **MCP** and **xAPI** — launch, read,
telemetry — and omitted the one standard that moves *content inward*. xAPI is the
better specification and **SCORM is the incumbent**: every platform on
[`../verticals/solutions.md`](../verticals/solutions.md) ingests it, and
`Selleo/mentingo` ships it alongside xAPI because buyers ask for it. The fourth
pass located a permissive, maintained runtime, so the gap closes.

**Components — every licence read from the licence file on 2026-10-31:**

| Role | Component | Licence | Note |
| --- | --- | --- | --- |
| SCORM runtime | [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | **MIT** (1,072 B) | SCORM 1.2, SCORM 2004, cross-frame, `offline-first`. 362★, 85 forks, pushed 2026-10-30. |
| Deck/courseware generation | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | **MIT** (1,069 B) | 71,498★. Native `.pptx` with the **client's own template** — i.e. branding compliance, which is what kills generated-content pilots. |
| Interactive conversion | [DozenTwelve/Papermorph](https://github.com/DozenTwelve/Papermorph) | **MIT** (1,069 B) | 1,034★. Books → animated, narrated, interactive web experiences; already carries a `scorm` topic. |
| Quality gate | [learning-commons-org/evaluators](https://github.com/learning-commons-org/evaluators) | **code MIT / prompts CC BY 4.0** | ⚠️ its two annotated corpora are **CC BY-NC-SA 4.0**; bring your own corpus. See step 0. |
| Pedagogical check | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | **MIT** | 1,143 teacher-qualification questions (CDPK 920, SEND 223). |
| Telemetry (optional) | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** | If the client wants learner data out as well as content in. |

**Wiring:**

1. **Establish the SCORM version the client's LMS actually consumes.** 1.2 and
   2004 are not interchangeable and the installed base is split. `scorm-again`
   supports both; the LMS decides which one you ship. Ask for a sample package
   that already imports successfully and match it.
2. **Generate the artefact, do not generate the package.** Produce decks with
   `ppt-master` against the client's own `.pptx` template, or interactive units
   with `Papermorph`. Keep generation separate from packaging so the quality gate
   sits between them.
3. **Gate before packaging.** Score every unit with `evaluators` rubrics for
   content quality and sample-check the generating model against
   `pedagogy-benchmark`. **A SCORM package is an opaque zip once imported** — the
   LMS will not tell you the content was wrong, and neither will the learner
   until the cohort has finished. This is the step that distinguishes the pattern
   from a content farm.
4. **Package with `scorm-again` and import through the client's normal course
   upload.** No LMS code is touched, no plugin is installed, no platform upgrade
   is blocked, and the licence boundary is never crossed — the GPL/AGPL platform
   simply consumes a file, which is exactly what it was built to do.
5. **Keep the source artefacts, version them, and hand them over.** The
   deliverable the client owns is the generator configuration, the template and
   the gated source units — not the zip. Re-packaging is then a build step.

**What the client is buying.** Courseware at a cadence their authoring team
cannot match, delivered through a route their platform team does not have to
approve. **What to be honest about:** SCORM telemetry is thin compared with xAPI
(completion, score, time — not behaviour), so if the engagement's value story is
learning analytics, this pattern is the wrong one and **P-568-A** with an LRS is
the right one. Say which is being bought.

---

## P-569-B — Courseware factory: syllabus in, gated multi-format units out (6–8 weeks)

**For:** a client with a large existing corpus — textbooks, lecture notes,
ministry curriculum PDFs, internal training manuals — and a mandate to turn it
into teachable material far faster than their authoring capacity allows.
**Region:** Global. The LMIC and ministry variant is noted at the end and it is
materially different.

**Why this is now possible and was not a pass ago.** The content-production layer
in [`../repos/foundations.md`](../repos/foundations.md) did not exist in this KB
before the fourth pass, because every sweep filtered on an education topic and
**the largest component carries none**. `hugohe3/ppt-master` is **MIT with
71,498★** — 🔴 *(described here as the largest permissively licensed repository
anywhere in this knowledge base; **superseded `p582` by `microsoft/markitdown`,
MIT, `193,266★`**)* — and it generates native PowerPoint from
documents or topics, with the client's own template, data-backed charts, and
**audio narration from speaker notes**. That last feature is a lecture-capture
path for free.

**Components — licences read first-hand 2026-10-31:**

| Role | Component | Licence | What it contributes |
| --- | --- | --- | --- |
| Deck and lecture generation | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | **MIT** | Documents/topics → native `.pptx`: shapes, transitions, animations, charts, tables, **narration from speaker notes**, client templates. 5,578 forks. |
| Interactive/animated units | [DozenTwelve/Papermorph](https://github.com/DozenTwelve/Papermorph) | **MIT** | Books → animated, narrated, interactive web experiences. For the material that should not be a deck. |
| Self-paced audio course | [assafkip/claudemy](https://github.com/assafkip/claudemy) | **MIT** | Topic → course of **2-minute audio lessons with cited sources**. The only generator here that starts from citations. |
| Document→study-page | [dmoshehun-prog/learn-from-materials](https://github.com/dmoshehun-prog/learn-from-materials) | **MIT** | PDFs/books/papers → traceable interactive pages with quizzes. 1,201★. |
| Retention layer | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | **MIT** | Hands the pipeline a real spaced-repetition scheduler instead of reimplementing one. |
| Standards alignment | [learning-commons-org/knowledge-graph](https://github.com/learning-commons-org/knowledge-graph) | **code MIT / data per publisher** | Checks units against academic standards and curricula; ships an MCP server. Clear each dataset individually. |
| Quality gate | [learning-commons-org/evaluators](https://github.com/learning-commons-org/evaluators) + [pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | **MIT / CC BY 4.0** + **MIT** | ⚠️ `evaluators`' two annotated corpora are **non-commercial**; the golden set comes from the client's syllabus. |
| Delivery | [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | **MIT** | Into the existing LMS (see **P-569-A**). |

**Wiring:**

1. **Classify the corpus by target format before generating anything.** Expository
   material → `ppt-master` decks. Narrative or conceptual material that benefits
   from motion → `Papermorph`. Material learners consume while commuting →
   `claudemy` audio. Reference material learners need to *search* →
   `learn-from-materials` pages. **Routing is the pattern's intellectual content;
   generating is the cheap part**, and a factory that sends everything through one
   generator produces 400 identical decks nobody opens.
2. **Pin the client's template and brand on day one.** `ppt-master`'s `.pptx`
   template support is the single feature that gets generated decks past an
   institution's communications team. Do this before volume, not after.
3. **Align to the standard, then gate on quality.** Run every unit through
   `knowledge-graph` for standards alignment, then `evaluators` rubrics for
   quality, then sample the generating model against `pedagogy-benchmark`. **Three
   checks, because they fail differently:** alignment catches off-syllabus,
   rubrics catch badly written, the benchmark catches a model that does not know
   how to teach.
4. **Attach spaced repetition rather than inventing it.** Emit flashcards from
   gated units into Anki via `anki-mcp-server`. Retention is the part of the value
   story a client can actually measure, and the scheduler is a solved problem.
5. **Package and deliver over SCORM** (P-569-A), keeping source artefacts and
   generator configuration as the versioned deliverable.
6. **Require citation provenance as an acceptance criterion**, and use `claudemy`
   as the reference for what that looks like in a generator rather than bolted on
   afterwards. The argument to make to an executive is on the public record:
   **South Africa's draft National AI Policy was withdrawn because at least 10% of
   its academic references were fictitious.**

**The LMIC / ministry variant.** Swap the front end: parse the national
curriculum with `AI-for-Education/lesson-plan-parse-mbsse` (MIT — real Sierra
Leone **MBSSE** lesson plans, PDF → structured JSON), align with
`AI-for-Education/gpf-alignment` (MIT) against the **Global Proficiency
Framework** where no rich national standard exists, deliver offline through
`learningequality/kolibri` (MIT) instead of SCORM, and add
`AI-for-Education/nemoasr-android` (on-device ASR) where literacy or devices are
the binding constraint. For vocabulary and language work,
[`orionsheep/wordlink`](https://github.com/orionsheep/wordlink) (MIT, 262★) runs
a fine-tuned 1.5B model **entirely in the browser via WebGPU** — no connectivity
and no inference bill, which is the only configuration that survives a
low-bandwidth classroom.

**What the client is buying.** Throughput with a quality floor, and the floor is
the product. **What to be honest about:** none of these generators knows whether
its output teaches. The gate is hand-built, the corpus behind it must be the
client's own for licence reasons as well as validity, and **nothing here monitors
the pipeline after go-live** — see the standing evaluation gap in
[`../intel/trends.md`](../intel/trends.md). Quote the gate as a permanent cost,
not a setup cost.

---

## P-570-A — Textbook-in, multi-format course-out: the client's own material as the starting point (6–8 weeks)

**For:** any institution or training provider that already owns the material —
textbooks, past papers, lecture PDFs, scanned worksheets — and wants it turned
into usable digital courseware. **This is the pattern the fifth pass's capability
sweep made possible**, and it inverts the usual pitch: it does not generate new
content that competes with the client's faculty, it **migrates what they already
have**.
**Region:** Global. Every component is permissive and every one runs on-premises.

**Why this pattern exists.** Four passes of this KB described the
content-*production* layer (`ppt-master`, `Papermorph`, `Claudemy`) and had no
**ingestion** layer at all, because every sweep filtered on an education topic
and no document parser carries one. The capability sweep returned sixteen
permissive components, three above 69,000★. **The ingestion step is the
commercially better place to start**: generating material competes with the
client's own authors, while ingesting their corpus is migration work — scopeable,
valuable, and not replicable with a chatbot subscription.

**Components — every licence read from the licence file on 2026-10-31:**

| Role | Component | Licence | Note |
| --- | --- | --- | --- |
| Primary document → structured text | [docling-project/docling](https://github.com/docling-project/docling) | **MIT** (1,072 B) | 69,909★. PDF/DOCX/**PPTX**/XLSX/HTML → markdown or JSON, **table structure preserved**. MIT, so the default choice. |
| STEM/formula-heavy fallback | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | ⚠️ **Apache-2.0 + additional terms** (3,301 B) | 82,860★. Best on formulas, tables, multi-column. **Carries a mandatory attribution duty — see step 5.** Branch `master`. |
| Scanned / handwritten input | [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | **Apache-2.0** (11,376 B) | 92,024★. Strongest CJK and handwriting. For exam scripts and worksheets. |
| Offline OCR fallback | [tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract) | **Apache-2.0** (11,358 B) | 77,267★, 100+ languages, no model licence, no inference bill. The ministry/offline answer. |
| Mixed legacy estates | [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) | **Apache-2.0** (11,360 B) | Use when the input is a repository of mixed formats rather than a book. |
| Knowledge structuring | [vanderbilt-data-science/knowledge-spaces](https://github.com/vanderbilt-data-science/knowledge-spaces) | **MIT** (1,090 B) | Knowledge Space Theory: material → knowledge graph → adaptive assessment. The pedagogical spine, from a named university. |
| Quality gate | [learning-commons-org/evaluators](https://github.com/learning-commons-org/evaluators) | **code MIT / prompts CC BY 4.0** | ⚠️ corpora are **CC BY-NC-SA 4.0** — bring your own. |
| Deck output | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | **MIT** (1,069 B) | Native `.pptx` against the client's own template. |
| In-place document editing | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | **Apache-2.0** (11,375 B) | 32,854★. For "update our 400 existing lesson plans", which `ppt-master` cannot do. |
| Typesetting | [tw93/Kami](https://github.com/tw93/Kami) | **MIT** (1,061 B) | Layout rules so output does not look machine-made. The cheapest fix for teacher rejection. |
| Audio + captions | [denizsafak/abogen](https://github.com/denizsafak/abogen) | **MIT** (1,069 B) | EPUB/PDF → narrated audio **with synchronised captions** — an accessibility deliverable, a transcript and a search index from one run. |
| Retention scheduling | [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | **MIT** (1,079 B) | FSRS as an algorithm. Build it in; do not invent a review schedule. |
| Delivery | [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | **MIT** (1,072 B) | Package into the untouched copyleft LMS. See **P-569-A**. |

**Wiring:**

1. **Triage the corpus before writing any code.** Split the client's material
   into three buckets: born-digital text (→ `docling`), formula- and
   table-heavy STEM (→ `MinerU`), and scanned or handwritten (→ `PaddleOCR`, or
   `tesseract` where nothing may leave the premises). **The triage is the
   estimate** — mixing these in one pipeline is the usual reason this work
   overruns.
2. **Extract to a single intermediate representation** (markdown + JSON with
   structure preserved) and **keep it as the versioned asset.** Every later
   output is a render of it. This is also what makes the deliverable ownable:
   the client ends up owning their corpus in an open format, which has value
   independent of whatever is generated from it.
3. **Impose structure before generating anything.** Run `knowledge-spaces` to
   derive the knowledge graph and prerequisite ordering. Skipping this yields a
   pile of generated units with no learning sequence — the most common failure of
   AI courseware and the one a teacher spots immediately.
4. **Gate, then render.** Score units with `evaluators` rubrics; only then
   render to decks (`ppt-master`), edited documents (`OfficeCLI`), typeset PDFs
   (`Kami`) and narrated audio with captions (`abogen`). Attach FSRS scheduling
   to anything that needs retention.
5. **If `MinerU` is in the shipped pipeline, the attribution duty is a product
   requirement, not a legal footnote.** Its licence obliges any online service
   built on it to state prominently — in the interface or public documentation —
   that MinerU is used, with **automatic termination** on breach. Route this to
   the client's engineering and UX teams at design time. **If that is
   unacceptable to the client, use `docling` (MIT) and accept weaker formula
   handling** — that trade is the decision, and it belongs to the client.
6. **Deliver through SCORM into the untouched platform of record** (P-569-A), or
   over LTI 1.3 if a live tutor is also in scope (P-568-A).

**What the client is buying.** Their own institutional knowledge, in an open
structured format they own, rendered into every format their learners and
platforms need. **What to be honest about:** ingestion quality on degraded scans
is genuinely variable and no amount of model choice fixes a bad scan — quote a
**sample-based** accuracy measurement on the client's real documents before
committing to a volume price. Run that sample in week one.

---

## P-570-B — Accessibility remediation of the document estate (4–6 weeks)

**For:** public-sector education bodies, universities and school systems facing
an accessibility conformance obligation over a large back-catalogue of PDFs.
**Region:** **EMEA** primarily — the **European Accessibility Act** — and
**North America**, where updated **ADA** web-accessibility guidance has obliged
large public institutions since April 2026. Applicable anywhere procurement
specifies WCAG or PDF/UA.

**Why this pattern exists.** This KB has carried accessibility remediation as a
North American opportunity since the third pass with **no open-source component
behind it** — scoped as audit-only, via `canvas-mcp`'s accessibility-auditor
skill. The capability sweep found a remediation engine, so the offer can change
from *finding* defects to *fixing* them, which is a materially larger engagement.

**Components:**

| Role | Component | Licence | Note |
| --- | --- | --- | --- |
| PDF accessibility automation | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | **Apache-2.0** (11,358 B) | 30,129★, Java, 2,881 forks. Topics include **`eaa`**, **`pdf-ua`**, `tagged-pdf`, `a11y`. **The only accessibility-as-a-feature asset in this KB.** |
| Structure extraction | [docling-project/docling](https://github.com/docling-project/docling) | **MIT** | Heading hierarchy and table structure — the inputs tagging needs. |
| Scanned-document OCR | [tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract) | **Apache-2.0** | A scanned PDF has no text layer and therefore **cannot** be made accessible without OCR first. |
| Audio alternative | [denizsafak/abogen](https://github.com/denizsafak/abogen) | **MIT** | Narrated audio with synchronised captions as an alternative format. |
| Live-session captioning | [collabora/WhisperLive](https://github.com/collabora/WhisperLive) | **MIT** (Collabora Ltd., **EMEA**) | Lecture captioning, where the obligation extends to live teaching. |
| LMS-side audit | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | **MIT** | Its accessibility-auditor skill, for the Canvas-resident content. |

**Wiring:**

1. **Inventory and classify.** Separate tagged PDFs, untagged born-digital PDFs
   and scanned images. Only the middle group is cheap; the third needs OCR first
   and the first may already pass.
2. **OCR the scans** (`tesseract`, on-premises — these are often student records).
3. **Extract structure** with `docling`, then **generate tagged, PDF/UA-oriented
   output** with `opendataloader-pdf`.
4. **Produce alternative formats** — narrated audio with captions (`abogen`) —
   because several conformance regimes accept an accessible alternative where
   remediating the original is disproportionate.
5. **Audit what stays inside the LMS separately** with `canvas-mcp`'s auditor.
6. **Deliver a conformance evidence pack**, not just fixed files: what was
   remediated, what was given an alternative, what was exempted and why.

**What the client is buying.** A regulator-facing evidence pack plus a remediated
estate, at a cost per document no manual process can match. **What to be honest
about: automated tagging is not conformance.** These tools produce structurally
tagged output; **WCAG and PDF/UA conformance requires human judgement** on
reading order, alt text and table semantics. Quote automation plus **sampled
human review**, and never let a client believe a tool signed off their legal
obligation. The evidence pack must say which documents a human checked.

---

## P-570-C — Efficacy trial for an AI tutor already in production (6–8 weeks)

**For:** a client who has deployed an AI tutor — often one bought or piloted
before this engagement — and is being asked by a board, a ministry or a funder
whether it actually works.
**Region:** Global. Strongest fit in **APAC** (Singapore's **AI Verify** makes
*evidence of testing* the deliverable; Korea's AI Basic Act imposes
human-oversight duties on high-impact education AI) and in **EMEA**, where Annex
III conformity work will need evidence of performance.

**Why this pattern exists, and its limits stated up front.** Six consecutive
passes of this KB have recorded that **no education-specific agent observability
or runtime regression tooling exists**. That is still true. What this pass found
is the adjacent thing: an **Apache-2.0 randomised-controlled-trial platform**
that attaches to the LMS over LTI. **It answers "did this intervention change
outcomes" and not "has the tutor degraded since Tuesday."** Both questions get
asked; only the first now has an open-source answer, and conflating them is the
mistake this pattern exists to prevent.

**Components:**

| Role | Component | Licence | Note |
| --- | --- | --- | --- |
| Randomised trial harness | [terracotta-education/terracotta](https://github.com/terracotta-education/terracotta) | **Apache-2.0** (11,323 B) | LTI plug-in: treatment variation inside real assignments, random assignment, **informed consent hidden from the teacher**, non-consenting students filtered from exports, identifiers stripped. Branch `development`. ⚠️ Licence names no licensor (template placeholders). 21★ — small. |
| Pedagogical-knowledge baseline | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | **MIT** | 1,143 teacher-qualification questions. Measures whether the model knows how to *teach*. |
| Output-quality rubrics | [learning-commons-org/evaluators](https://github.com/learning-commons-org/evaluators) | **code MIT / prompts CC BY 4.0** | ⚠️ **corpora CC BY-NC-SA 4.0 — the regression suite must source its own corpus.** |
| Mastery measurement | [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | **MIT** (1,073 B) | BKT behind MCP — an independent mastery estimate, not the tutor's own self-report. |
| Behavioural telemetry | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** | xAPI LRS. The event stream the trial analyses. |

**Wiring:**

1. **Fix the outcome measure before touching the tutor.** Assessment scores,
   completion, or an independent mastery estimate from `tutor-mcp` — decided and
   written down first. A trial whose outcome is chosen after the data arrives is
   not a trial.
2. **Get the ethics apparatus in place early, because it is the long pole.**
   `terracotta`'s consent model (hidden from the teacher, non-consenting students
   filtered from exports, identifiers stripped) is designed for exactly this, but
   institutional review timelines are measured in weeks and run in parallel with
   nothing. Start day one.
3. **Randomise within assignments, not between classes.** Class-level assignment
   confounds the teacher with the treatment, which is the standard way education
   pilots produce uninterpretable results. `terracotta` varies content *inside*
   an assignment for this reason.
4. **Stand up a model-side baseline too** — `pedagogy-benchmark` for pedagogical
   knowledge, `evaluators` rubrics on generated output, **on a corpus the
   engagement sources itself** (the bundled CLEAR and PERSUADE 2.0 corpora are
   non-commercial and cannot ship in a billable deliverable).
5. **Stream telemetry into `ralph`** so behavioural data is available alongside
   outcome data.
6. **Report the null if it is null.** The commercial value here is the client's
   ability to defend a decision to a board or a regulator, and a trial that can
   only produce good news defends nothing.

**What the client is buying.** Defensible evidence about a system they already
run — the artefact a funder, ministry or Annex III conformity assessment asks
for. **What to be honest about, twice over:** `terracotta` is a **21★** project
and should be treated as a methodology implementation to be understood and
possibly forked, not as vendor software; and **this is not monitoring.** If the
client's actual question is "will we know when it breaks", the answer today is
that they will need a bespoke harness, because open source does not supply one —
which is also, as this KB has recorded for six passes, the clearest unmet build
opportunity in the industry.

---

## P-571-A — Defensible assessment pipeline: model-authored items, human-provable marking (8–10 weeks)

**For:** exam boards, awarding bodies, universities with central assessment
units, and any client whose marking will be automated and audited.
**Region:** **EMEA** primarily — the EU AI Act's **Annex III** category
*evaluation of learning outcomes*, obligations landing **2 December 2027** — and
**North America**, where the binding constraint is student-data law rather than
conformity assessment (California's proposed A.B. 1159; Idaho's bias-evaluation
and privacy duties). Applicable in **LATAM** wherever a *secretaría* must show a
regulator what was marked and by whom.

**Why this pattern exists.** Five passes of this KB recorded *"nothing permissive
generates psychometrically defensible items"* and went looking for a generator.
The sixth pass found that the buyable artefact is the **gate**, not the generator
— and the gate is what the regulation actually demands evidence of. This pattern
is the first in this KB that can answer *"prove a human marked everything a
machine could not defensibly mark."*

🆕 **Amended `p571` — the premise above is half false, and the base knew it.** The
sentence bundles two claims. 🟡 **"Psychometrically defensible" still holds:**
nothing permissive *calibrates*, so the gate remains the buyable artefact and this
pattern still produces the conformity evidence. 🔴 **"Nothing permissive generates
items" is false, and was false when this pattern was written** — pass 85
(`2026-10-09`) recorded a 7-row MIT item-generation tier in `agents/trending.md`
that reached **no shelf page and no pattern for 86 passes**. 🟢 It is now shelved
in [`../repos/foundations.md`](../repos/foundations.md) and wired in **`P-574-A`**.
🔵 **Use `P-574-A` to author and this pattern to mark and prove** — the authoring
step below should no longer be a bare model prompt.

**Components:**

| Role | Component | Licence | Note |
| --- | --- | --- | --- |
| Source-material ingestion | [docling-project/docling](https://github.com/docling-project/docling) | **MIT** | Client's own syllabus, textbooks and past papers → markdown/JSON with table structure. The items must be grounded in the client's curriculum, not the model's memory. |
| STEM/handwriting ingestion | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | ⚠️ **Apache-2.0 + commercial thresholds** | Formulas and multi-column STEM papers. ⚠️ Its **prominent-attribution clause binds any online service** built with it — that reaches UX, not just legal. |
| **Item authoring contract** | [onionviolet/itembank](https://github.com/onionviolet/itembank) | **MIT** (1,068 B) | 🟢 **The load-bearing component.** Markdown banks, `itembank lint` **blocking on error**, `itembank guard` failing CI on committed real banks, deterministic scoring, **short-answer never auto-graded**. |
| Rubric quality gate | [learning-commons-org/evaluators](https://github.com/learning-commons-org/evaluators) | ⚠️ **code MIT · prompts CC BY 4.0 · corpora CC BY-NC-SA** | Scores generated content against research-backed rubrics. ⛔ **The two annotated corpora are non-commercial — bring your own corpus for a billable regression suite.** |
| Cognitive diagnosis | [bigdata-ustc/EduCDM](https://github.com/bigdata-ustc/EduCDM) | **Apache-2.0** | Infers learner mastery from responses. ⚠️ **Not item calibration** — see the honest limit below. |
| Retention scheduling | [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | **MIT** | FSRS, which `itembank` already implements — use the library form if you need it outside the bank. |
| Telemetry store | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** | xAPI LRS: every item served, every response, every human override, timestamped. **This is the audit trail.** |
| Dashboards | [openfun/warren](https://github.com/openfun/warren) · [openfun/potsie](https://github.com/openfun/potsie) | **MIT** · **MIT** | What the assessment board looks at. `potsie` is Jsonnet, so dashboards ship as reviewable code. |
| Drift baseline | [evidentlyai/evidently](https://github.com/evidentlyai/evidently) | **Apache-2.0** | Regression and drift on the authoring model's output distribution. 🔴 The **only** permissive option — see the licence warning below. |
| LMS attachment | [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | **Apache-2.0** | LTI 1.3 launch into Moodle/Canvas/Open edX without touching platform code. |

**Wiring:**

1. **Ingest the client's curriculum** with `docling` (and `MinerU` for STEM
   papers). Every item must trace to a source document — provenance is the first
   thing an auditor asks for.
2. **Author items with the model into `itembank`'s markdown format**, never
   straight into a database. The format is the contract.
3. **Gate in CI, not in review.** `itembank lint` blocks the merge on error —
   unexplained distractors, answer-position skew, select/key mismatch, duplicate
   stems. `itembank guard` keeps live banks out of the repository. 🟢 **A model may
   author; it may not merge.**
4. **Score deterministically.** Objective items score in `itembank`'s own runtime
   with **no model in the path**; `check` items run learner code against hidden
   cases. **Short-answer items are routed to a human rubric marker and stay
   pending** — this is the step that produces the conformity evidence, so
   instrument it rather than optimising it away.
5. **Layer rubric scoring as advisory only** (`evaluators`) on generated
   *content*, never as a score of record.
6. **Emit xAPI to `ralph` at every transition** — item served, response, lint
   verdict, human override, final mark. Surface it in `warren`/`potsie`.
7. **Baseline the authoring model in `evidently`** and re-run on every model or
   prompt change, so "the item quality changed in March" is answerable.
8. **Deliver a conformity pack**: the lint ruleset, the CI logs, the
   human-marking record, the drift baselines, and a written statement of which
   decisions were automated and which were not.

🔴 **Honest limits — state all four to the client before quoting.**

- **`itembank` gates items; it does not calibrate them.** There is **no live,
  permissive, education-specific item-calibration asset** on this base:
  `eribean/girth` (MIT) last shipped **2022**, `inuyasha2012/pypsy` (MIT)
  **2018**, `meyerjp3/psychometrics` (the most capable, Java) has **no licence
  file at all**, and the R options are copyleft. `EduCDM` does cognitive
  diagnosis. **Difficulty parameters mean a stale dependency, a licence risk, or
  a build.**
- **`itembank` ships no QTI.** Interchange (QTI/CASE/SCORM) is explicitly
  backburner — the README says it *"waits for a named consumer."* 🔵 If the client
  needs QTI, this pattern needs a build step or `tremby/questionbank` (⚠️ **CC BY**),
  and the engagement could be that named consumer.
- **`itembank`'s MCP surface is unshipped** ("Phase 999.3") and its wider course
  workspace is not yet runnable. Integrate over its **key-free JSON session
  protocol** (`start`/`next`/`submit`/`report`/`teach`), which does work.
- ⛔ **Do not reach for `Arize-ai/phoenix` for the observability slot.** It is
  **Elastic License 2.0**: *"You may not provide the software to third parties as
  a hosted or managed service."* For a studio that hosts and operates client
  solutions that is a **prohibition, not a threshold**, and it also forbids
  disabling its licence-key mechanism. ⚠️ `langfuse/langfuse` is usable but is
  MIT-Expat **only outside** `ee/`, `web/src/ee/`, `worker/src/ee/` and
  `packages/shared/src/server/ee/` — a build-configuration requirement. 🟢
  `evidently` is the clean pick.

## P-571-B — Lecture-video factory that never leaves the client's infrastructure (6–8 weeks)

**For:** ministries, national operators and universities that must produce
narrated courseware at volume **and** cannot send student or curriculum material
to a third-party cloud.
**Region:** **APAC** primarily — Vietnam's AI law duties by **1 March 2027**
(grace for education systems operating before **15 August 2026**), Taiwan's **AI
Basic Act** in force **14 January 2026**, Indonesia's **GR 71** data residency —
and **LATAM**, where widening compute and connectivity gaps argue for local
inference. In **EMEA** the driver is different: the **European Accessibility
Act** makes captions a procurement gate.

**Why this pattern exists.** The fifth pass asked for a `topic:video` sweep. The
sixth ran it and found **no open-source lecture-video product to adopt** — but a
well-understood four-stage pipeline (slides → page images → narration script →
TTS and mux) with a permissive component at every stage. 🔴 **Three of the four
pipelines found terminate in Amazon Polly and require AWS credentials**, which
disqualifies them by default for exactly the clients who need this most. The
pattern is the pipeline **with the TTS stage swapped**.

**Components:**

| Role | Component | Licence | Note |
| --- | --- | --- | --- |
| Reference pipeline | [galaxyproject/video-lectures](https://github.com/galaxyproject/video-lectures) | **MIT** (1,071 B, "Galaxy Project") | Pandoc → HTML slides → `wkhtmltoimage` page images → script extraction → mux. 🔴 **Replace its Polly stage.** |
| Narration/assembly engine | [jhudsl/ari](https://github.com/jhudsl/ari) | **MIT** (declared in `DESCRIPTION`) | R package, **Johns Hopkins Data Science Lab**. ⚠️ Its grant is **not** in `LICENSE` — that file is a 40 B stub. |
| Local-voice pipeline | [Changochen/slide-to-video](https://github.com/Changochen/slide-to-video) | **MIT** (1,070 B) | 🟢 **The sovereignty pick** — PDF deck + script, slides split on `NEWSLIDE`, with **optional local voice cloning**. The only row on this axis that needs no cloud TTS at all. |
| Script drafting | [htlin222/slides-to-video](https://github.com/htlin222/slides-to-video) | **MIT** (1,065 B) | Drafts **speaker notes** from the slides, then TTS + `ffmpeg`. Use when the client has decks but no narration scripts. |
| Captioned audio | [denizsafak/abogen](https://github.com/denizsafak/abogen) | **MIT** | 🟢 Emits **synchronised captions** — the EAA/WCAG deliverable, not an extra. |
| On-device TTS | [Blaizzy/mlx-audio](https://github.com/Blaizzy/mlx-audio) | **MIT** | Apple Silicon. ⚠️ `supertonic` (MIT, on-device) is **archived** — grant perpetual, patches not. |
| Source ingestion | [docling-project/docling](https://github.com/docling-project/docling) | **MIT** | Client's existing textbooks and decks → structured markdown to drive the slides. |
| Lesson construction | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | **MIT** | Topic or documents → slides, quizzes, whiteboard; **exports PPTX and single-file offline HTML**, which feeds this pipeline directly. |
| Delivery into the client LMS | [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | **MIT** (1,072 B) | SCORM 1.2 / 2004 runtime, `offline-first`. Ships the finished units into the incumbent LMS **without touching it**. |
| Telemetry | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** | xAPI record of what was delivered and watched. |

**Wiring:**

1. **Ingest** the client's existing material with `docling`; keep a
   source-to-slide map so every claim on a slide is traceable.
2. **Build the lesson** — `OpenMAIC` for interactive units (it exports PPTX and
   offline single-file HTML), or author markdown slides directly for the
   `galaxyproject` pipeline.
3. **Render page images** (`wkhtmltoimage`, or ImageMagick on the
   `slides-to-video` path).
4. **Produce the narration script.** Have `htlin222/slides-to-video` draft
   speaker notes where none exist, then **put them through human review** — this
   is a content-accuracy gate, and in the EU the **transparency duty on
   synthetic teaching material has been live since 2 August 2026**.
5. 🟢 **Synthesise locally.** `Changochen/slide-to-video`'s local voice cloning,
   or `mlx-audio`/`abogen`. **Do not configure Polly**; that single default is
   what would otherwise breach the client's residency position.
6. **Generate captions with `abogen`** as a first-class output, not a retrofit.
7. **Package with `scorm-again`** and deliver into the incumbent LMS; emit xAPI
   to `ralph` for what was actually watched.

🔴 **Honest limits.** Every component on this axis is **tiny** — 2★ and single
digits, against a document layer where five repositories clear 30,000★. 🔵 These
are *scripts to assemble*, not products to adopt, and the estimate must say so:
the engineering is in the integration and the voice quality, not in the
components. ⛔ **`harry0703/MoneyPrinterTurbo` (MIT, 136,744★) is explicitly not
in this pattern** — it is short-form social video, and its star count makes it the
most likely asset to be mis-offered here as courseware tooling.

## P-574-A — Multilingual item factory feeding a human-provable gate (6–8 weeks)

**For:** awarding bodies, universities with central assessment units, national exam
agencies, and corporate-training clients needing **volume** item authoring in more
than one language, on their own infrastructure.
**Region:** **APAC** first — `lmqg` ships evaluated `ja/ko/zh` models, and
**India's amended IT Rules require prominent labels and provenance markers on
AI-generated content from 20 Feb 2026**, which this pipeline emits by
construction. **EMEA** for `fr/de/it/es` plus the **Art. 50** transparency duty
(**2 Aug 2026**). **LATAM** for Spanish — 🔴 **not Portuguese**, see the limits.

**Why this pattern exists, and it is a correction rather than a discovery.**
`P-571-A` below leaves its item-authoring step to *"the model"* — a bare LLM
prompt — on the stated premise that *"nothing permissive generates
psychometrically defensible items."* 🔴 **Pass 85 (`2026-10-09`) had already found
a 7-row, permissively-licensed item-generation tier and recorded it in
`agents/trending.md`; it reached no shelf page and no pattern for 86 passes.**
🟢 `p571` shelved it ([`../repos/foundations.md`](../repos/foundations.md)) and
this pattern is the first to wire it. 🟡 **The other half of `P-571-A`'s premise
stands:** nothing here *calibrates*, so this pattern authors and `P-571-A` marks
and proves.

**Components** — grants carry pass 85's byte count plus a `p571` re-read; **5 of 5
re-reads matched exactly**.

| Role | Component | Licence | Note |
| --- | --- | --- | --- |
| Source-material ingestion | [docling-project/docling](https://github.com/docling-project/docling) | **MIT** | Client syllabus/textbooks/past papers → markdown+JSON with table structure. Every item must trace to a source document. |
| **Multilingual generator** | [asahi417/lm-question-generation](https://github.com/asahi417/lm-question-generation) | **MIT** (1,065 B) | 🟢 **Load-bearing.** `pip install lmqg`. Question **and answer** generation in **9 languages** (`en/fr/ja/ko/ru/it/es/de/zh`), HuggingFace checkpoints, **ACL 2023** system-demonstration paper, 385 commits. The only evaluated multilingual option on the base. |
| Item-**type** generator | [ramsrigouthamg/Questgen.ai](https://github.com/ramsrigouthamg/Questgen.ai) | **MIT** (1,077 B) | The shapes an assessment unit orders: MCQ with distractors, boolean, FAQ, paraphrase, answer prediction. T5 + sense2vec. ⚠️ Region **disputed** (pass 85 said APAC; the grant names an individual) — do not quote it. |
| **Distractor specialist** | [KristiyanVachev/Leaf-Question-Generation](https://github.com/KristiyanVachev/Leaf-Question-Generation) | **MIT** (1,073 B) | 🟢 MCQs **with wrong-answer options**. ⚠️ **Use the MIT `Leaf` repo** — the same author's `Question-Generation` is **GPL-3.0** with 3.5× the stars, so a star-sorted pick takes the copyleft one. |
| Candidate **ranker** | [AMontgomerie/question_generator](https://github.com/AMontgomerie/question_generator) | **MIT** (1,073 B) | Answer-aware evaluator that **ranks** generated questions. Over-generate → rank → gate. |
| Teacher-PDF entry point | [PragatiVerma18/MLH-Quizzet](https://github.com/PragatiVerma18/MLH-Quizzet) | **MIT** (1,069 B) | 🟢 Takes **teacher PDFs** and emits a quiz — the only row whose input is the artefact a teacher already has. Good pilot surface. |
| Baseline / control | [patil-suraj/question_generation](https://github.com/patil-suraj/question_generation) | **MIT** (1,068 B) | The axis's reference implementation. Use as the control when benchmarking the above. |
| ⚠️ Broad toolkit | [artitw/text2text](https://github.com/artitw/text2text) | 🟡 **MIT + rider** (1,324 B) | 🔴 **`Gap 353`/`P922`: a dependency-closure rider, 256 B over canonical MIT.** Clear it with counsel or skip the row — the rest of the pipeline does not need it. |
| **The gate** | [onionviolet/itembank](https://github.com/onionviolet/itembank) | **MIT** (1,068 B) | 🟢 `itembank lint` **blocks CI on error** — unexplained distractors, answer-position skew, select/key mismatch, duplicate stems. **A model may author; it may not merge.** |
| Rubric advisory | [learning-commons-org/evaluators](https://github.com/learning-commons-org/evaluators) | ⚠️ **code MIT · prompts CC BY 4.0 · corpora CC BY-NC-SA** | Advisory on generated *content* only. ⛔ Bring your own corpus for a billable suite. |
| Telemetry / provenance | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** | xAPI LRS: every item generated, ranked, linted, overridden — timestamped. **This is the provenance record India's rules ask for.** |
| Dashboards | [openfun/warren](https://github.com/openfun/warren) · [openfun/potsie](https://github.com/openfun/potsie) | **MIT** · **MIT** | Jsonnet dashboards ship as reviewable code. |
| Drift baseline | [evidentlyai/evidently](https://github.com/evidentlyai/evidently) | **Apache-2.0** | Baseline the generators' output distribution; re-run on every model or prompt change. |
| LMS attachment | [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | **Apache-2.0** | LTI 1.3 launch into Moodle/Canvas/Open edX without touching platform code. |

**Wiring:**

1. **Ingest the curriculum** with `docling`. Chunk to **passage** size — every
   generator here takes a paragraph, not a chapter.
2. **Route by language, not by preference.** `lmqg` for any of its 9 languages
   (`TransformersQG(language="es")`); `Questgen.ai`, `Leaf` and `MLH-Quizzet` are
   **English-only** and carry the richer item types. 🔵 For a non-English
   engagement `lmqg` *is* the pipeline and the others are unavailable — size the
   estimate accordingly.
3. **Over-generate, then rank.** Generate 5–10× the required items; rank with
   `question_generator`'s answer-aware evaluator. Never ship first-pass output.
4. **Generate distractors as a separate step** (`Leaf`, or `Questgen.ai`'s
   sense2vec path). Distractors are the quality ceiling of an MCQ bank and the
   thing the gate rejects.
5. **Write into `itembank`'s markdown format, never into a database.** The format
   is the contract; `itembank lint` blocks the merge, `itembank guard` keeps live
   banks out of the repository.
6. **Emit provenance at generation time** — model id, checkpoint or prompt hash,
   source document, language, timestamp — into `ralph` as xAPI. 🟢 This satisfies
   **India's 20 Feb 2026 labelling-and-provenance duty** and **EU Art. 50**, and
   **it cannot be reconstructed afterwards.**
7. **Hand scoring to `P-571-A`.** Objective items score deterministically in
   `itembank`'s runtime with **no model in the path**; **short-answer stays pending
   for a human.**
8. **Baseline in `evidently`** so *"item quality changed in March"* is answerable.

🔴 **Honest limits — state all six before quoting.**

- 🔴 **These are T5-era models (grants dated 2018–2024) and a current frontier LLM
  will out-write them on English fluency.** Do not sell them as better generators.
  Sell the four things they actually give: **determinism**, **on-premises
  execution** (data residency, no per-item API cost at volume), **evaluated
  multilingual coverage with a published paper**, and a **distractor step** general
  models handle poorly. 🟢 With no residency, volume or multilingual constraint,
  a prompted LLM behind the same `itembank` gate is the honest recommendation.
- 🔴 **The repository licence does not cover the model weights.** All rows are MIT,
  but the fine-tuned **checkpoints are distributed on HuggingFace under their own
  terms** and base models carry their own (T5 is Apache-2.0). ⚠️ **Check each
  model card separately** — the same licence-layering trap `p570` recorded for
  content carve-outs, one layer down.
- 🔴 **No Portuguese.** `lmqg`'s 9 languages exclude `pt`. 🟢 **But the corpus
  exists:** `lplnufpi/essay-br` is **MIT** and human-graded on **ENEM C1–C5**, so a
  Brazilian engagement is a *trainable* build, not a blank sheet. 🔴 Spanish is the
  harder case despite `lmqg` covering `es`: `Gap 237` records **no rubric and no
  graded corpus** for Spanish, so scoring there needs an annotation programme
  first. **Generation and scoring have opposite coverage in the two languages** —
  read that before scoping either.
- 🔴 **Nothing here calibrates.** No difficulty or discrimination parameters:
  `eribean/girth` (MIT) last shipped **2022**, `inuyasha2012/pypsy` (MIT) **2018**,
  `meyerjp3/psychometrics` has **no licence file**, R options are copyleft. **A
  generated bank is uncalibrated until it has been sat.** `P-572-A` is the
  calibration engagement.
- 🔴 **Do not promise automated essay marking.** `topics/automated-essay-scoring`
  holds 35 repositories with 8 permissive grants but **no production-grade
  implementation**, and the short-tag variant `topic:essay-scoring` is emptier
  still (17 rows, 34★ ceiling). Extended-response marking is `P-571-A`'s **human**
  path.
- ⚠️ **`itembank` ships no QTI** and its MCP surface is unshipped. Integrate over
  its key-free JSON session protocol (`start`/`next`/`submit`/`report`/`teach`).

## Declared gaps

- **No pattern for Blackboard, Brightspace or Google Classroom.** No agent
  population for these platforms reached verification this run, so no recipe is
  offered rather than a speculative one.
- ~~**No Africa-specific pattern.**~~ **Closed on the second pass of
  2026-10-31**: the regional demand and policy evidence was found, and the
  pattern is written up as **P-568-F** above, with Kolibri (MIT) as predicted
  plus DSpace (BSD-3-Clause). Its own caveats are stated in place.
- **No Canada pattern, deliberately.** Canadian findings are now in
  [`../intel/market.md`](../intel/market.md), but the two engagement shapes are
  **P-568-C run per board** (Ontario — ~58% of boards have no student AI policy
  and no ministry template is coming) and a reinstatement case in Quebec, where
  a **March 2025 directive suspended AI assistants**. Same artefacts, different
  trigger, so no new recipe — but **francophone delivery is a hard requirement**
  in Quebec, which is a staffing constraint rather than a technical one.
- ~~**No APAC pattern.**~~ **Closed as P-568-H above**, on evidence the previous
  pass did not have: TEQSA's 100%-response institutional census and the AJET
  finding that only **7 of 39** Australian universities document operational
  governance. The driver turned out to be **award integrity**, not conformity
  assessment, which is why it is a pattern and not a per-jurisdiction run of
  P-568-D.
- ~~**No pattern uses an EMEA-origin agent.**~~ **Partly closed.** The *agent*
  layer in EMEA is still imported, but **P-568-J** is built on an EMEA-origin
  permissive **platform** (`Selleo/mentingo`, MIT, Poland) and composes an
  entirely EMEA-origin permissive stack with `ralph` (France) and
  `pedagogy-benchmark`. **LATAM remains unclosed and the reason is now specific:**
  the one LATAM-origin agent found (`digitalinnovationone/dio-agent`, 2,750★) is
  **unlicensed**, so it cannot enter a pattern. It is evidence of demand, not a
  component.
- ~~**Africa's supply side is unmapped.**~~ **Closed, and P-568-F should be
  revised to use it.** `AI-for-Education` (MIT, LMIC-focused) publishes a Sierra
  Leone **MBSSE** lesson-plan parser, Luganda benchmarks, Global Proficiency
  Framework alignment, and on-device Android ASR for no-connectivity classrooms —
  see [`../repos/foundations.md`](../repos/foundations.md). Every repo is 0–13★,
  so local partnership stays part of the pattern, but P-568-F no longer has to
  compose *entirely* imported components. **Next pass: rewrite P-568-F around
  these components rather than around Kolibri alone.**
- ~~**No pattern delivers content *into* the platform of record.**~~ **Closed as
  P-569-A.** Three passes built the attach doctrine on LTI, MCP and xAPI —
  launch, read, telemetry — and never noticed that **nothing moved courseware
  inward**, which is what procurement actually asks for and what every platform
  on this KB's own verticals page ingests. `jcputney/scorm-again` (MIT, 362★,
  SCORM 1.2 + 2004) closes it. The gap survived three passes because the doctrine
  was built from the *integration* literature, where xAPI is the modern answer,
  rather than from what a buyer specifies.
- **The content-production layer arrived late and the next pass should expect
  more of it.** `ppt-master` (**MIT, 71,498★**) was believed the largest permissively
  licensed repository in this KB — 🔴 **superseded `p582` by `microsoft/markitdown`
  (MIT, `193,266★`)** — and went unfound for four passes because every
  sweep filters on an education topic and it carries none. **P-569-B** is built on
  it. Assume the same blind spot still hides document parsers, TTS pipelines,
  assessment-item generators and video tooling: sweep by **capability**
  (`topic:pptx`, `topic:text-to-speech`, `topic:pdf`, `topic:ocr`, `topic:scorm`)
  crossed with licence.
- **Every quality gate in this file now has a licence boundary through it.**
  `evaluators` is code-MIT / prompts-CC-BY-4.0 / **corpora-CC-BY-NC-SA-4.0**, and
  the upstream corpora are NC too. So the golden set in **P-568-K**, **P-569-A**
  and **P-569-B** must be built from the client's own syllabus — which is better
  practice and is now also a licence requirement. **It is also an unbudgeted
  line in most proposals**, and the main reason these three patterns should not be
  quoted from their component list alone.
- **No pattern uses `academico` yet.** `academico-sis/academico` (MIT, 410★,
  151 forks, `student-information-system`) is the permissive education SIS whose
  non-existence this KB asserted for three passes. It is a real option for a
  small-or-medium-institution client and there is no recipe built on it. **Next
  pass: a permissive-SIS pattern for the language-school / training-institute /
  private-school-group buyer**, which is a different buyer from every pattern
  currently in this file.
- **No pattern has been run end to end.** Every recipe here is composed from
  verified components with stated licences; none has been executed on a client
  engagement by this KB. Durations are estimates, not measured delivery times,
  and should be presented as such.

---

## P-572-A — Item calibration and score equating, with the assurance a 0★ library cannot supply (6–8 weeks)

**For:** any client in `P-571-A`'s position who has to defend a *score*, not just
a marking process — awarding bodies issuing grades, universities with placement
testing, certification programmes running multiple test forms a year.
**Region:** **EMEA** first (EU AI Act **Annex III**, *evaluation of learning
outcomes*, obligations landing **2 December 2027** — a conformity assessment will
ask how item parameters were estimated and how two forms were made comparable),
then **North America** for certification bodies under accreditation review.
Applies in **APAC** and **LATAM** wherever a ministry equates a national test
across sittings.

**Why this pattern exists, and why it could not exist last pass.** `P-571-A`
ships a defensible *marking* pipeline and closes with an admission: items could
be authored and gated permissively but **not calibrated**. 🟢 That is no longer
true — [`DaniyalMlk/calibrate`](https://github.com/DaniyalMlk/calibrate) (**MIT**,
dependency-free TypeScript) implements the calibration, adaptive-administration
and **equating** layer. 🔴 **But it is `0.1.0`, one author, 0★ and unpublished to
npm, so this pattern is half library and half assurance work.** The assurance
half is the billable, defensible part and it is specified here rather than left
implied.

**Components:**

| Role | Component | Licence | Note |
| --- | --- | --- | --- |
| Item authoring + blocking gate | [onionviolet/itembank](https://github.com/onionviolet/itembank) | **MIT** (1,068 B) | Carried from `P-571-A`. Produces the gated bank this pattern calibrates. Exports **answer-key TSV** — that is the response-matrix interface. |
| **Calibration + CAT + equating** | [DaniyalMlk/calibrate](https://github.com/DaniyalMlk/calibrate) | **MIT** (1,064 B) | 🟢 **Load-bearing.** 2PL/3PL **and** graded-response / partial-credit / generalized-partial-credit; **marginal maximum likelihood** (and joint, with its structural bias demonstrated); **four linking methods**; **DIF**; person-misfit; score→ability tables with SE. **Zero runtime dependencies** — verified from `package.json`. |
| **Reference implementation (assurance, not runtime)** | [eribean/girth](https://github.com/eribean/girth) | **MIT** | 🔴 Stale since **2022-09-09** — and that is *fine for this role*. A frozen, independently written MIT estimator is exactly what you want to cross-check `calibrate`'s MML output against. **Pin it, do not ship it.** |
| Gain validation | [finite-sample/guess](https://github.com/finite-sample/guess) | **MIT** (via `DESCRIPTION`) | R. Latent-class correction using **pre/post transitions** — answers "is this gain real or is it guessing?" after the scores are on one metric. |
| Cognitive diagnosis | [bigdata-ustc/EduCDM](https://github.com/bigdata-ustc/EduCDM) | **Apache-2.0** | Mastery inference for reporting. ⚠️ Still **not** calibration — keep the roles distinct in the report you hand the client. |
| Telemetry store | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** | xAPI LRS. Every administered item, response and ability estimate, timestamped — the evidence trail the equating argument rests on. |
| Dashboards | [openfun/warren](https://github.com/openfun/warren) · [openfun/potsie](https://github.com/openfun/potsie) | **MIT** · **MIT** | Item-parameter drift and form-comparability panels as reviewable Jsonnet. |
| LMS attachment | [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | **Apache-2.0** | LTI 1.3 launch; the adaptive session runs beside Moodle/Canvas, never inside it. |

**Wiring:**

1. **Export the gated bank** from `itembank` as answer-key TSV, and hold a
   pilot administration (paper or fixed-form) to get a response matrix. You
   cannot calibrate without responses; budget this as a real data-collection
   step, not a sprint task.
2. **Calibrate twice, on purpose.** Run `calibrate`'s `fit` (joint) and `mml`
   (marginal) over the same matrix. The library demonstrates JML's structural
   bias itself; **record both and report MML.** Divergence beyond expectation is
   a data problem, not a library problem, and you want it surfaced here.
3. 🟢 **Build the assurance artefact — this is the step that answers the 0★
   objection.** Estimate the *same* matrix with `girth` and diff the item
   parameters. Keep the diff, the seed and the matrix in the repository as a
   committed fixture. **Two independently written MIT estimators agreeing to a
   stated tolerance is evidence; a star count never was.** Re-run it in CI on
   every `calibrate` bump.
4. **Screen for DIF** across the demographic splits the client is accountable
   for before any item reaches a live form. Annex III conformity work will ask;
   so will any North American bias-evaluation duty.
5. **Equate the forms.** Use `calibrate`'s linking methods over a common anchor
   set to put sittings on one metric, and publish the score→ability conversion
   table *with its standard errors*. Run all four methods; if they disagree
   materially your anchor set is too thin, which is a finding you want before
   results day, not after.
6. **Administer adaptively** through the LTI launch, with maximum-information
   selection and a precision stopping rule. Stream every event to `ralph`.
7. **Validate observed gains** with `guess` on the pre/post transitions, so a
   reported improvement is net of guessing.
8. **Panel it** in `warren`/`potsie`: item-parameter drift between sittings,
   anchor stability, form comparability, DIF flags.

**What to tell the client, in one sentence.** *The whole chain — authoring,
gating, calibration, DIF, equating, gain validation — is permissively licensed
and self-hosted, and the calibration engine is eight weeks old, so you are
buying a cross-validation harness as part of the delivery.* 🔴 **Do not present
this stack as mature.** The honest pitch is that the alternative is a per-seat
psychometrics licence and a vendor who will not show you the estimator.

**Effort:** 6–8 weeks on top of `P-571-A`. Roughly half of it is steps 3 and 5 —
the cross-validation harness and the equating argument — and that split is the
point.

---

## P-572-B — Adopting a measurement-first learning platform without inheriting its AGPL obligation (4–6 weeks)

**For:** a client who wants `AI Learning OS`'s audit pipeline — equivalent
pre/post testing, CTT item analysis, mastery validity, metacognitive calibration,
effect sizes gated in CI — delivered as a **hosted** service by Globant.
**Region:** **APAC** as found (HarmonyOS target, `ChinaTextbook` integration),
but the pattern is region-neutral; the licence surgery is the same anywhere.

**Why this pattern exists.** [`swsgbl/ai-learning-os`](https://github.com/swsgbl/ai-learning-os)
is the only platform on these shelves whose selling point is **proving learning
happened** rather than delivering content, and at **1★ / 1,313 commits** it is a
real codebase. 🔴 **Its `main/LICENSE` says MIT and that answer is incomplete:**
its own `NOTICE.md` puts `services/api/` under **AGPL-3.0 combination
obligations**, because it links **PyMuPDF (AGPL-3.0)** in-process. Host that over
a network and §13 obliges you to hand your deployment's source to its users.
🟢 **The whole pattern is: remove one dependency, keep the platform.**

**Components:**

| Role | Component | Licence | Note |
| --- | --- | --- | --- |
| Platform | [swsgbl/ai-learning-os](https://github.com/swsgbl/ai-learning-os) | ⚠️ **MIT root; AGPL-3.0 on `services/api/`** | Clients (`apps/web`, `apps/android`, `apps/harmony`) and `services/console` are **MIT and untouched** by this work. |
| ⛔ Dependency to remove | **PyMuPDF** | ⛔ **AGPL-3.0** | The single cause. Used for PDF textbook parsing — page anchors and outline. |
| 🟢 Replacement parser | [py-pdf/pypdf](https://github.com/py-pdf/pypdf) | **BSD-3-Clause** | Outline and page-level extraction. First choice for structure. |
| 🟢 Replacement parser | [jsvine/pdfplumber](https://github.com/jsvine/pdfplumber) | **MIT** | Better word/table geometry where page anchors must be precise. |
| Scanned-book OCR | **rapidocr-onnxruntime** + **onnxruntime** | **Apache-2.0** · **MIT** | Already in the platform's dependency table and already permissive — **no change needed.** |
| Retention | **py-fsrs** | **MIT** | Already permissive. Same FSRS algorithm as `itembank` and `fsrs4anki`. |
| Local speech | **funasr** · **CosyVoice** | **MIT** · **Apache-2.0** | Already permissive. 🟢 **Keep these: local ASR/TTS is why voice audio never leaves the client's infrastructure.** |
| Assessment upgrade (optional) | [onionviolet/itembank](https://github.com/onionviolet/itembank) · [DaniyalMlk/calibrate](https://github.com/DaniyalMlk/calibrate) | **MIT** · **MIT** | Its audit pipeline is **CTT**. Bolt `P-572-A` on where the client needs IRT and equating. |

**Wiring:**

1. **Read `NOTICE.md` first and put it in the engagement record**, not the
   licence file. 🔴 **The lesson generalises past this repo: for a platform, the
   licence surface is the dependency manifest, not `LICENSE`.** A
   `raw.githubusercontent.com/.../LICENSE` read — the standard instrument —
   returns `MIT` here and misses an AGPL network obligation entirely.
2. **Fence the blast radius.** Everything except `services/api/` is MIT. Confirm
   the client's hosted surface and check whether `services/api` is even in it;
   if the deployment is private and single-tenant with no third-party users,
   §13 may not trigger and the cheapest answer is a documented legal position
   rather than code.
3. **Swap the parser** where it does trigger. Isolate PyMuPDF behind the
   existing parse interface, reimplement page-anchor and outline extraction on
   `pypdf` (fall back to `pdfplumber` where geometry matters), and keep the
   platform's own parser tests as the acceptance criterion.
4. **Prove the removal.** `pip`-tree the service and assert no AGPL-licensed
   package remains; make that assertion a **CI gate**, so a future dependency
   bump cannot reintroduce the obligation silently. This is the deliverable the
   client's counsel will ask for.
5. **Keep the audit pipeline intact.** The mastery-simulation validity study,
   metacognitive calibration (gamma) and pre/post effect sizes are the reason
   for the engagement — regression-test them before and after the swap and show
   the numbers unchanged.
6. **Alternative, priced honestly:** `NOTICE.md`'s other exit is a **commercial
   PyMuPDF licence from Artifex**. If the client's timeline is shorter than the
   swap, buy it and say so. ⚠️ Per-deployment cost, forever, versus a bounded
   one-off engineering task — that is the trade, and it is the client's call.

**Effort:** 4–6 weeks. Step 3 dominates; steps 1, 2 and 4 are days and carry
most of the risk reduction.

---

## P-572-C — Sub-floor supply census: find the open-source layer a star-sorted search cannot see (1 week, reusable across industries)

**For:** Globant's own studio practice, at the start of any engagement where
"we checked and there is no open-source option for X" would otherwise go in a
deck.
**Region:** **Global** — and it is the only pattern here whose value is highest
in **LATAM**, **EMEA** and **APAC**, because non-English, non-US-institutional
projects attract stars last and are therefore the most systematically hidden by
a star sort.

**Why this pattern exists.** This KB ran the same star-sorted discovery for six
passes and concluded three axes were saturated. 🔴 **They were saturated at the
floor, not in the field:** `topic:ai-tutor` answers **816** results sorted by
stars and **793** at `stars:<50`. 🟢 **One sweep of the band produced 13
addresses new to this base, against 0 from eight keyword search legs** — and two
of those 13 closed gaps this KB had published for five and six passes
respectively. The method, not the industry, was the limit.

**Components (all standard tooling — this is a method, not a stack):**

| Role | Tool | Note |
| --- | --- | --- |
| Discovery | `github.com/search?q=topic:<axis>+stars:<50&s=updated&o=desc` | 🔴 **Sort by `updated`, not stars** — inside the band, stars are pure noise (`3,2,1,1,0,0,…`). |
| Licence gate (**runs first**) | `raw.githubusercontent.com/<r>/{main,master}/{LICENSE,LICENSE.md,LICENSE.txt,LICENCE,COPYING}` | 🔴 This band is where ungranted repos concentrate: **2 of 13** here carried no grant at 5 filenames × 2 branches. Gate before you read. |
| Manifest gate (**second**) | `package.json` · `DESCRIPTION` · `pyproject.toml` · `NOTICE.md` | 🟢 Catches what `LICENSE` cannot: an R package's real grant (`guess`), and an AGPL obligation reaching one directory through one dependency (`ai-learning-os`). |
| **Ranking signal** | `git clone --filter=blob:none` + `git rev-list --count HEAD` | 🟢 **The discriminator.** Blobless, so it is cheap; exact, so it is not a rendered figure. |
| Absence-claim check | [`../ingest/absence-claims.py`](../ingest/absence-claims.py) | 🟢 Run it against your own findings page before publishing an absence. |

**Wiring:**

1. **Name the axes as topics, not keywords.** Keyword search legs returned **0**
   new addresses six passes running; `topic:` + a star bound returned 13 in one.
2. **Pull the band sorted by recency**, 10–30 rows per axis. Record the
   `total_count` — a null with no denominator is not a finding.
3. **Gate on licence before reading anything else.** Five filenames × two
   branches over `raw.githubusercontent.com`. 🟢 Accept on a **property test** —
   OSI-approved, no copyleft, no network clause — which admits `ISC`, `0BSD`,
   `Unlicense`, `MIT-0`, and not on a name list.
4. **Read the manifest even when `LICENSE` answered.** `ai-learning-os` reads MIT
   at `LICENSE` and carries an AGPL-3.0 network obligation in `NOTICE.md`.
5. **Rank by commits, and split the field.** Blobless-clone the survivors and
   `rev-list --count`. Expect a clean separation: here, **4 above 200 commits**
   and **5 at or below 9**, the latter first-committed within 48 hours.
   🔴 **Recency puts a two-commit announcement and a 1,313-commit platform on the
   same page; only the commit count tells them apart.**
6. 🔴 **Apply the right floor per layer.** Commit density for **tooling**
   (`calibrate`: 0★/214 commits, shelved). Stars for **tutors and agents**, where
   stars *are* the adoption evidence (`voyage` 1★/224 commits, **not** shelved).
   Promoting a 1★ tutor to a client deck is the failure mode this step prevents.
7. **Re-check your own absence claims** with `absence-claims.py` before the deck
   ships. It found this base publishing a gap its own shelf had closed.

**What this buys an engagement.** Two closed gaps and thirteen addresses for
about a week of one person's time — and, more valuable, it stops the studio
telling a client to *build* something that already exists permissively.
🟢 **Nothing in this pattern is education-specific; run it unchanged on gaming,
legal, financial, healthcare, media, retail, travel, technology, automotive,
energy and enterprise.**

**Effort:** 1 week per industry, 3 axes. Repeat quarterly, not hourly — the band
turns over fast but a quarter is the shortest interval over which a commit
history means anything.

## 🆕 `p574` — 2026-10-31 — two recipes off the accessibility and QTI layer

🔵 `P-576-A` is the conformance programme whose deliverable outlives the deadline;
`P-576-B` is assessment delivery that keeps a `GPL-3.0` front-end out of a client
product. Both licences were read byte-for-byte this pass — see
[`../repos/foundations.md`](../repos/foundations.md) and
[`../intel/market.md`](../intel/market.md) for the regional placement.

## P-576-A — Accessibility conformance programme for an LMS estate, with an evidence trail that outlives the deadline (6–8 weeks)

🔵 **The buyer and the trigger.** A public school district, state system or public
university in the United States has a **dated obligation** — `April 26, 2027`
(population ≥ 50,000) or `April 26, 2028` (below that, and special districts) — to
bring web content and mobile apps to **WCAG 2.1 AA**, PDFs, Word documents,
spreadsheets and presentations included. In EMEA the same work is driven by
`EN 301 549` under the Web Accessibility Directive, and in Brazil by `LBI` art. 63
with no deadline but an active public prosecutor. 🔴 **The dates have already moved
once this year** (see [`../intel/market.md`](../intel/market.md)), which is the
argument for selling the *inventory*, not the date.

🟢 **The stack, every licence read byte-for-byte this pass** (evidence:
[`../evidence/accessibility-qti-licence-bytes.2026-10-31-p574.tsv`](../evidence/accessibility-qti-licence-bytes.2026-10-31-p574.tsv)):

| layer | component | grant | how it is used — and the licence posture that follows |
| --- | --- | --- | --- |
| Course-content scanner | [ucfopen/UDOIT](https://github.com/ucfopen/UDOIT) | 🔴 **GPL-3.0-only** (`35,147 B`; `package.json` + `composer.json` agree) | **Canvas estates only.** Deploy **unmodified** in its own container, authenticate over the LMS API, send patches upstream. 🔴 Do **not** vendor it into a client product or a Globant-branded platform. |
| Permissive LMS alternative | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** (`10,982 B`) | Where the client is *choosing* a platform rather than remediating one. The only permissively granted institutional LMS on these shelves. |
| CI gate on content and templates | [Community-Access/accessibility-agents](https://github.com/Community-Access/accessibility-agents) | 🟢 **MIT** (`1,069 B`) | Eleven **WCAG 2.2 AA** review specialists, run per pull request on the courseware repository and the theme. Vendorable into the client's pipeline. |
| Design-system remediation | [plugin87/ux-ui-agent-skills](https://github.com/plugin87/ux-ui-agent-skills) | 🟢 **MIT** (`1,073 B`) | Fixes defects at the **template** level (tokens, components, contrast) so a thousand courses inherit one fix. |
| Estate-wide crawl | [liip/TheA11yMachine](https://github.com/liip/TheA11yMachine) | 🟡 **`BSD-3-Clause` in `package.json`, no licence file** | Internal auditing tool only. 🔴 A manifest-only grant has **no notice text to reproduce**, so do not ship it to the client; either obtain a grant clarification or replace it before delivery. |
| Learner-side adaptation | [ContentSquare/readapt](https://github.com/ContentSquare/readapt) · [evoluteur/braille-tools](https://github.com/evoluteur/braille-tools) · [dasher-project/dasher-web](https://github.com/dasher-project/dasher-web) · [mthebaud/predict4all](https://github.com/mthebaud/predict4all) | 🟢 Apache-2.0 / MIT / MIT / Apache-2.0 | Dyslexia reading adaptation, Grade-1 Braille rendering, gaze-and-switch text entry, AAC word prediction. All four are shippable in a client deliverable. |
| Document estate | — | — | 🔵 **Do not rebuild it here**: `P-570-B` on this page already covers remediation of the document estate. `P-576-A` is the **platform-and-evidence** half; run them together. |

🟢 **The deliverable, and this is the part that is worth money after the date
moves:**

1. A **per-course conformance inventory** — course id, owner, enrolment, defect
   classes, WCAG criteria failed, date last checked, remediation state.
2. A **remediation backlog ranked by enrolment**, so the first fix reaches the most
   learners, not the first alphabetical department.
3. A **re-check job** that re-runs the agents on every change and re-stamps the
   date, so the inventory never silently ages.
4. A **standard decision**: baseline **2.1 AA** for the US scope, deliver **2.2
   AA** where EMEA or APAC content is in play (`EN 301 549` v4.1.1 and Australia
   both land on 2.2 in 2026) — the MIT agents already enforce 2.2, so the
   over-delivery is free.

🔵 **Weeks.** 1–2: estate inventory and platform discovery. 2–4: UDOIT (or
OpenOLAT pilot) stood up, agents in CI on the theme. 4–6: template-level fixes,
backlog ranked, learner-side adaptations piloted with the disability services
office. 6–8: re-check job, evidence pack, handover to the client's own
accessibility coordinator.

🔴 **State the licence boundary in the SoW, in one sentence per component.** The
scanner and the platforms in this layer are **copyleft**; the CI agents and the
learner-side adaptations are **permissive**. A client who believes they bought a
product they can resell has bought the wrong thing, and this is the layer where
that misunderstanding is most likely — because the copyleft component is the one
that produces the visible output.

## P-576-B — Standards-conformant, accessible assessment delivery without inheriting GPL on the item bank (8–10 weeks)

🔵 **The buyer.** An exam board, ministry, professional certification body or
university assessment centre that must deliver tests which survive an appeal: the
item bank has to be portable, the delivery has to be accessible, and the scores
have to be defensible. 🟢 **The interchange contract is `QTI`**, and this pass read
the whole `topic:qti` population (`52` repositories) — so the licence map below is
the complete picture, not a sample.

| layer | component | grant | posture |
| --- | --- | --- | --- |
| Delivery platform | [oat-sa/tao-core](https://github.com/oat-sa/tao-core) + [oat-sa/extension-tao-itemqti](https://github.com/oat-sa/extension-tao-itemqti) | 🔴 **GPL-2.0-only** (`18,025 B`; `composer.json` agrees) | **TAO**, the QTI-native platform of record (OAT SA, Luxembourg). **Client-hosted, deployed unmodified.** Custom work goes in **separate TAO extensions**; those are derivative, so if anything is ever *distributed*, GPL-2.0 governs it. 🔵 GPL-2.0 has **no §13**, so a hosted deployment alone triggers no source-offer obligation — unlike the AGPL rows in this layer. Put the distribution question to the client's counsel in week 1, in writing. |
| Legacy item ingest | [rolfis/qti-convert](https://github.com/rolfis/qti-convert) | 🟢 **Apache-2.0** (`11,357 B`) | The **only permissively licensed QTI tool in the population.** Converts a Canvas QTI export to JSON/Word; wrap it as the ingest step and ship it. |
| Second ingest path | [Learnosity/learnosity-qti](https://github.com/Learnosity/learnosity-qti) | 🔴 **GPL-2.0** (`18,264 B`, on `develop`) | Run as an **external CLI step in a container**, never linked into client code. Use only if the client has Learnosity-format items. |
| Item rendering | [Citolab/qti-components](https://github.com/Citolab/qti-components) | 🔴 **GPL-3.0** (`35,199 B`) | 🔴 **Do not embed in a proprietary front-end.** Either deliver items through TAO's own (already-GPL, arm's-length) delivery, or build the renderer. This is the single most likely accidental GPL-3.0 contamination point in the recipe. |
| Accessible sittings | [mthebaud/predict4all](https://github.com/mthebaud/predict4all) | 🟢 **Apache-2.0** | AAC word prediction for candidates using switch or gaze input in an accommodated sitting. |
| Sign-language channel | [sign-language-translator/sign-language-translator](https://github.com/sign-language-translator/sign-language-translator) | 🟢 **Apache-2.0** (`11,364 B`; `pyproject.toml` agrees) | 🔴 **Not** [`sign/translate`](https://github.com/sign/translate), which is **CC BY-NC-SA** — noncommercial, and therefore unusable in a paid deliverable however good it is. In **Brazil this is not optional**: Libras is statutory (`Lei 10.436/2002`). |
| Item statistics | — | — | 🔵 Compose with **`P-575-A`** (permissive Python calibration) for item parameters and equating; **`P-575-B`** if the client's statistician insists on `mirt`/`TAM`, which are GPL and must stay arm's-length. |

🟢 **Deliverables.** A QTI-in/QTI-out item bank the client owns outright; a
client-hosted TAO deployment with named extensions; an **accessibility
conformance statement for the delivery surface** (the same evidence artefact
`P-576-A` produces, scoped to the test player); an accommodations matrix mapping
each supported accommodation to the component that provides it; and a licence
register naming every component, its grant, its byte count and its distribution
posture.

🔵 **Weeks.** 1–2: item inventory, licence register, counsel sign-off on the
distribution question. 2–4: TAO stood up client-side, ingest path built on
`qti-convert`. 4–6: accommodations (AAC input, sign-language channel, contrast and
keyboard paths) and the conformance statement. 6–8: calibration via `P-575-A`,
equating plan. 8–10: pilot sitting with the disability services office, appeal
rehearsal, handover.

🔴 **The failure mode this recipe exists to prevent.** The obvious build — take
`qti-components` for the renderer because it is the cleanest code in the
population, and wrap TAO — produces a **GPL-3.0 front-end inside a client
product**, which is the one outcome nobody in the room will have priced. The
grants here were read byte-for-byte precisely because the convenient choice and
the safe choice are different repositories.


## P-573-A — Rubric regression gate: prove the tutor has not degraded since Tuesday (4–6 weeks)

**For:** any client already running an AI tutor, content generator or marking
assistant in production, who cannot currently answer *"is it still as good as it
was at go-live?"*
**Region:** **Global**. 🔵 Highest urgency in **EMEA**, where an **AI Act Annex
III** evaluation-of-learning-outcomes system must hold post-market monitoring
evidence by **2 December 2027**, and in **North America**, where the four 2026
state laws requiring district-level AI policy imply an audit someone must pass.

**Why this pattern exists, and why it could not be written before this pass.**
This KB published *"no education-specific evaluation or regression tooling
exists"* for six passes. 🟢 **The scoring machinery does exist** — it is tagged
`rubric`, not `education` (see trend 15) — and it is permissive. 🔴 **What still
does not exist is a drift *detector*, so this pattern builds the detector out of
scoring parts.** That distinction is the whole design: you are not buying
monitoring, you are constructing it from a deterministic scorer plus a pinned
corpus plus a generic drift tool.

| Role | Component | Licence | Why this one |
| --- | --- | --- | --- |
| Trajectory scoring | [`alphadl/AdaRubrics`](https://github.com/alphadl/AdaRubrics) | **Apache-2.0** | 🟢 The only asset found that scores a **multi-turn trajectory** rather than one output — and every tutor in this KB is multi-turn. |
| Deterministic re-scoring | [`CurveAhoead/ScoreRune`](https://github.com/CurveAhoead/ScoreRune) **code only** | **Apache-2.0** | 🔴 **Use the code, never cite the history** — its 2,137-commit log is synthetic (`570-A`). Deterministic, two runtimes, **no model in the scoring path**, which is what makes a regression gate reproducible. |
| Education rubrics + prompts | [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) | ⚠️ code **MIT**, prompts **CC BY 4.0**, corpora **CC BY-NC-SA** | 🔴 **Take the code and the prompts. Do NOT ship the CLEAR or PERSUADE corpora** — they are non-commercial, and the upstream originals are too. |
| Pinned corpus | **the client's own** historical outputs, frozen | client's | 🔴 **The load-bearing step.** The corpus that exists cannot be shipped, so the engagement must mint one: 300–500 real interactions, human-scored once, versioned. |
| Skill-bundle scoring | [`AndrewNgGirl/SkillLens`](https://github.com/AndrewNgGirl/SkillLens) | **MIT** | Where the deliverable *is* a prompt contract — which is **15 of the 25** agents in this KB. |
| Item-side gate | [`onionviolet/itembank`](https://github.com/onionviolet/itembank) | **MIT** | `itembank lint` blocks on error; short-answer items never auto-graded. Reuse rather than re-implement. |
| Drift alerting | [`evidentlyai/evidently`](https://github.com/evidentlyai/evidently) | **Apache-2.0** | 🔴 Generic, not education-aware — it watches the *score series* this pattern produces, not the pedagogy. |
| Evidence trail | [`Sion612/rubrictrail`](https://github.com/Sion612/rubrictrail) | **Apache-2.0** | Criterion → evidence link, which is the shape an audit file needs. ⚠️ Dormant since Aug 2026: read as a design reference. |

**Wiring:**

1. **Freeze a corpus in week 1, before any tooling.** 300–500 real interactions,
   stratified by subject, learner level and language. 🔴 **Everything downstream
   is worthless without this and it is the step clients resist**, because it
   needs teacher time. Price it explicitly.
2. **Human-score it once** against a rubric taken from `evaluators`' prompts
   (CC BY 4.0 — attribute, do not relicense). This is the ground truth; it is
   produced once and never regenerated.
3. **Stand up `ScoreRune` as the deterministic scorer** and calibrate it against
   the human scores until agreement is stated as a number. 🔴 **Report the
   agreement figure to the client as the gate's accuracy** — a scorer that
   disagrees with teachers is a false-alarm generator.
4. **Add `AdaRubrics` for the trajectory dimension** — did the session actually
   progress, or did it produce eight individually acceptable turns that went
   nowhere? Single-output scoring cannot see this.
5. **Run both nightly against the frozen corpus** and push the score series into
   `evidently`. Alert on distribution shift, not on single scores.
6. **Keep the criterion → evidence links** (`rubrictrail`'s shape) so a regulator
   or accreditor can be shown *why* a score was given, not just the score.
7. 🔴 **Re-run the gate on every model, prompt and retrieval change** — the point
   is to catch a silent provider-side model update, which is the most common real
   cause of drift and the one no client monitors today.

**What to tell the client up front:** 🟢 *"You will be able to prove the tutor
still meets the standard, with permissive code and your own evidence."* 🔴
*"Nobody in open source will alert you that it drifted — we are building that
from scoring parts, and the quality of the alert is the quality of the corpus you
give us in week one."*

## P-573-B — Provenance gate: verify a component before it enters a client deliverable (1 week, reusable across every industry base)

**For:** Globant's own studio practice. 🔵 **This is the pattern most likely to
transfer unchanged to the gaming, legal, financial, healthcare, media, retail,
travel, technology, automotive, energy and enterprise bases on this harness** —
nothing in it is education-specific.
**Region:** **Global**.

**Why this pattern exists.** 🔴 **Two of this KB's own ranking signals have now
been shown forgeable, one of them one pass after it was adopted.** `p569` replaced
a star floor with commit density because the floor was discarding good libraries.
`p570`'s first never-swept axis returned a **35★ / 2,137-commit** repository whose
history is synthetic. 🔵 **Stars need other people; commits need a loop.** Any
shortlist built on self-reported repository metadata is a shortlist built on
claims the author controls.

| Check | Command / instrument | What it catches |
| --- | --- | --- |
| **1. Grant exists** | `raw.githubusercontent.com/<r>/{main,master,dev}/{LICENSE,LICENSE.md,LICENSE.txt,COPYING,licence}` | 🔴 Branch and filename traps. `human-skill-tree` is AGPL on `master` and 404 on `main`; probing only `main` manufactures a false "no licence". |
| **2. Grant is whole** | read the **body**, not the SPDX name | 🔴 **Four carve-out shapes, and only the first is API-visible:** separate content licence · per-directory grant · obligation inherited from an in-process dependency (`ai-learning-os` ← PyMuPDF, AGPL) · 🆕 **a `Scope:` clause inside the permissive file itself** (`word-atlas`, `570-B`). |
| **3. Manifest agrees** | `package.json` · `DESCRIPTION` · `pyproject.toml` · `NOTICE.md` | 🟢 Catches a real grant a stub `LICENSE` hides (`guess`: 52-byte `LICENSE`, MIT in `DESCRIPTION`) and a dependency surface (`calibrate`: `dependencies` absent — verified, not assumed). |
| **4. History is plausible** | 🆕 [`../ingest/history-plausibility.py`](../ingest/history-plausibility.py) | 🔴 **The new one.** Monotonic low-variance commits/year; commit conventions predating their own timestamps; author≠committer divergence of exactly zero; a repo whose first commit is a `refactor:`. |
| **5. Adoption is real** | stars **and** forks **and** distinct authors **and** `archived` | 🔴 `archived: true` is invisible in a licence or star read (`supertonic`: MIT, 13,757★, frozen). Two `noreply` authors on a "12-year" project is a tell. |
| **6. Figures are timestamped** | record the read time with the number | 🔴 Star counts move hourly (DeepTutor: +41 in 62 minutes measured here) and third-party digests emit impossible rates. **A star count is a reading, not a level.** |

**Wiring:**

1. **Run checks 1–3 before reading the README.** Licence first is not pedantry:
   it is the only check whose failure makes every other answer irrelevant.
2. **Run check 4 on anything admitted on commit density**, which costs one
   `git clone --filter=blob:none`. 🔴 **Mandatory whenever stars are low and
   commits are high** — exactly the profile the sub-floor census (`P-572-C`) is
   designed to surface, so these two patterns must be run as a pair.
3. **Record every verdict with its evidence string** — byte count of the licence
   file, the branch it was found on, the manifest field, the commit histogram.
   🔵 A verdict with no evidence string is re-derived from scratch next pass; this
   KB has measurably paid that cost.
4. **Carry defects forward rather than dropping the row.** `ScoreRune` is in this
   KB *with its defect named*, because the code is usable and the next reader
   would otherwise re-discover the same 2,137 and believe it.

**The honest limit:** none of these six checks establishes that code **works**.
They establish that it may be used, that it exists, and that its self-reported
history is not fabricated. 🔴 **Validation is still engineering** — `P-572-A`'s
cross-estimator harness is what that looks like.

## P-573-C — EMEA assessment engagement on locally published institutional psychometrics (8–10 weeks)

**For:** a European ministry, exam board, national testing institute or
university consortium that must evidence an **AI Act Annex III** system by
**2 December 2027** and would prefer not to base it on imported tooling.
**Region:** **EMEA**.

**Why this pattern exists and could not be written before this pass.** 🔴 This KB
recorded *"EMEA gained no placed row"* for three consecutive passes and offered
EMEA clients US- and APAC-origin psychometrics. 🟢 **`p570` placed three EMEA
rows from the grants themselves** — and the rows were already in-tree, already
licence-read, with only the region column blank. **The supply never changed; the
instrument did** (`569-D`).

| Role | Component | Licence | Provenance — the point of this pattern |
| --- | --- | --- | --- |
| Test analysis of record | [`dexter-psychometrics/dexter`](https://github.com/dexter-psychometrics/dexter) | ⚠️ **LGPL-3** — attach, do not fork | 🟢 **Cito**, the Dutch **national testing institute** (`jesse.koops@cito.nl` in `Authors@R`). The strongest EMEA institutional provenance in this KB. |
| Large-scale assessment models | [`cran/TAM`](https://github.com/cran/TAM) | GPL-2+ — attach | 🟢 **IPN Leibniz Institute**, Kiel (`ipn.uni-kiel.de`). ⚠️ Grant lives in `DESCRIPTION`; **GitHub's sidebar shows no licence** — do not let a reviewer read that as unlicensed. |
| Latent-variable modelling | [`yrosseel/lavaan`](https://github.com/yrosseel/lavaan) | GPL-2+ — attach | 🟢 **Ghent University**. |
| Item calibration + equating | [`DaniyalMlk/calibrate`](https://github.com/DaniyalMlk/calibrate) | **MIT** | 🔴 `0.1.0`, 0★, one author — **permissive and pre-adoption.** The only component here you may embed. |
| Item gate | [`onionviolet/itembank`](https://github.com/onionviolet/itembank) | **MIT** | Blocking linter; deterministic scoring, **no model in the scoring path** — the conformity artefact Annex III evaluation needs. |
| Autograding | [`ucbds-infra/ottr`](https://github.com/ucbds-infra/ottr) | **BSD-3** | **UC Berkeley**; R-native, so it sits beside `dexter` rather than fighting it. |
| Efficacy evidence | [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta) | **Apache-2.0** | LTI-attached randomised trials with consent handling. ⚠️ Grant **names no licensor** (template placeholders intact). |
| Regression gate | **P-573-A** above | — | Post-market monitoring is an Annex III obligation, not an optional extra. |

**Wiring:**

1. **Lead with provenance, not architecture.** 🟢 The opening slide is that the
   measurement core is published by **Cito, IPN Leibniz and Ghent** — three named
   public institutions in three member states. That is the procurement argument;
   the technical one follows.
2. 🔴 **Draw the copyleft boundary on day one.** `dexter`, `TAM` and `lavaan` are
   **LGPL/GPL** — they run as an **analysis service behind a process boundary**,
   invoked over a queue or REST, never linked into a proprietary product. This is
   the same doctrine this KB applies to the LMS of record: **attach, do not
   fork.**
3. **Put `calibrate` and `itembank` inside the product** — both MIT — and keep
   the GPL analysis tier outside it.
4. **Validate `calibrate` against `dexter` or `TAM`**, not instead of them:
   `P-572-A`'s cross-estimator harness, with the national-institute
   implementation as the reference. 🟢 **Two independently written estimators
   agreeing to a stated tolerance is the assurance evidence that a 0★ library
   cannot supply**, and here the reference carries a national institute's name.
5. **Attach `ottr` for marking** and `terracotta` for efficacy claims.
6. **Stand up P-573-A as the monitoring obligation** and keep its evidence trail
   from go-live.

🔴 **State the gap honestly in the same conversation:** this is a **measurement**
story, not a tutoring one. The EMEA *agent* layer is still effectively empty — one
24★ university feedback system and one 13★ evaluator — so the tutor itself will
be APAC- or US-origin, or built. **Conflating the two is the most expensive
mistake available on this page**, and it is the regional version of a finding this
KB has carried for four passes.
