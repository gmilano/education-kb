---
industry: education
region: Global
updated: 2026-10-10
---

# Education — compose patterns

**Pass 92, 2026-10-10.** ⏱️ **Second pass of this date.** Every repo named below was resolved this pass by
`git ls-remote --symref` with its **licence read from the payload** at the pinned SHA, using
`compose/code/grant-ladder-v4/ladder.sh` over **24** candidate filenames at a **1-byte floor**, classified by
the shared `compose/code/lib/license_family.sh` (`P237`). Each pattern names the specific repos, the licence
posture of the whole stack, and how the pieces wire together.

🔴 **`P91-E` was re-costed this pass because the licence it was built on was wrong.** It stated that
`portabilis/i-educar` is LGPL-3.0 and that *"LGPL-3.0 permits exactly that, and this distinction makes the
engagement possible"*. **i-educar is GPL-2.0, which has no linking exception.** The pattern survives but the
integration boundary — and therefore the cost — changed. See `P91-E` below and
`compose/code/grant-ladder-v4/README.md`.

🟢 **One new pattern this pass (`P92-A`)**, enabled by `Gap 335`'s discharge.

## `P91-A` — The closable AI university platform (EMEA)

**The ask it answers.** A European institution wants a self-hosted learning platform, extended with AI,
received as a **closed, owned deliverable**. Six passes of this KB answered *"impossible — the platform tier is
copyleft"*. It is not.

**Stack — permissive end to end, no copyleft anywhere.**

| layer | component | grant |
|---|---|---|
| platform | [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) · `develop` · `760e2e1` | **MIT** (1 091 B) |
| tutor | **Iris**, in-tree | MIT with the platform |
| feedback | **Athena**, in-tree | MIT with the platform |
| exercise authoring | **Hyperion** (Spring AI), in-tree | MIT with the platform |
| 🆕 public portal / catalogue | [`openfun/richie`](https://github.com/openfun/richie) · `master` · `8b14aec` | **MIT** (1 079 B) |
| assessment engine | [`numbas/Numbas`](https://github.com/numbas/Numbas) · `master` · `39b03e5` | **Apache-2.0** (11 357 B) |
| learner-data trail | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) · `main` · `cb794e4` | **Apache-2.0** (11 357 B) |
| statement mapping | [`adlnet/xAPI-SCORM-Profile`](https://github.com/adlnet/xAPI-SCORM-Profile) · `master` · `ea17c40` | **Apache-2.0** (11 324 B) |
| content shim | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) · `master` · `882f3b8` | **MIT** (1 072 B) |
| 🆕 accessibility gate | see **`P91-F`** | **MIT** |

**Wiring.** Fork Artemis. Iris/Athena/Hyperion are config-gated — point them at the client's model endpoint
(sovereign or on-prem) rather than a vendor API. 🆕 **Put `richie` in front as the catalogue and enrolment
funnel**: it is the only permissive row at the portal layer, it comes from a French public-HE consortium
(which reads well in a European tender), and it keeps the public-facing redesign — the thing institutions
actually ask for — outside the platform fork. Package Numbas assessments as SCORM and serve them through
`scorm-again`, so assessment content stays portable if the platform later changes. Every Iris interaction and
Athena feedback event emits an xAPI statement shaped by `xAPI-SCORM-Profile` into `lrsql`.

**Why the trail is the deliverable, not a feature.** 🟡 That store is the **human-oversight evidence** the AI
Act asks for, and it exists before the **2 Dec 2027** high-risk deadline rather than after. 🟢 **And it is
sold against a duty that already binds: Article 4's staff AI-literacy obligation is in force now and was not
deferred** — so phase one is literacy and evidence, phase two is high-risk conformity. See `intel/trends.md` `T4`.

## `P91-B` — The district AI-compliance recorder (North America)

**The ask it answers.** Ohio requires every K-12 district to adopt a formal AI policy by **1 Jul 2026**; 30+
states have guidance; 134 bills are live across 31 states. 🆕 **Only ~10 % of institutions have formal
guidelines and 71 % of US teachers report no AI training** — so the buyer has a legal deadline, no instrument
and no trained staff. California's AB 1159 would additionally bar training on student data absent direct
school benefit.

**Stack.**

| layer | component | grant |
|---|---|---|
| record store | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) · `cb794e4` | **Apache-2.0** |
| statement vocabulary | [`adlnet/xAPI-SCORM-Profile`](https://github.com/adlnet/xAPI-SCORM-Profile) · `ea17c40` | **Apache-2.0** |
| conformance gate | [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) · `efa045e` | **Apache-2.0** |
| orchestration | [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) · `12aeb0f` | **MIT** |
| HE platform (if in scope) | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) · `10a1d90` | **ECL-2.0** |
| 🆕 staff-capability curriculum | see **`P91-G`** | **MIT / Apache-2.0** |

**Wiring.** Put every AI interaction behind a LangGraph node that emits one xAPI statement per event:
*which learner, which model, which prompt class, which human reviewed it, which policy clause authorises it*.
Store in `lrsql`; validate the statement shapes against `ADL_LRS` so conformance is demonstrable rather than
asserted. The deliverable is a policy document **plus a running record that evidences the policy** **plus**
🆕 **the staff training that the 71 % figure says is the real bottleneck** — and the third part is what turns a
one-off compliance project into a programme.

🔴 🆕 **Conformance note that changes the build.** The official **SCORM 2004 4th Edition Test Suite**
(`adlnet/SCORM-2004-4ed-Test-Suite`) carries **no licence payload in 24 filenames**, and so do
`adlnet/SCORM-to-xAPI-Wrapper` and `adlnet/SCORM-to-TLA-Roadmap` — **three of ADL's five repos.** It cannot be
redistributed in a client deliverable. 🟢 **Conform against `ADL_LRS` (Apache-2.0) instead**, which is why it
is in this stack as a gate rather than as a reference.

**Deliberate exclusion.** No GPL component. `LearningLocker` is the better-known LRS and is **GPL-3.0**;
`lrsql` is Apache-2.0 and better maintained. Using the famous one here would convert the deliverable.

## `P91-C` — The pedagogy skill pack, now with content packaging (global, lowest cost to ship)

**The ask it answers.** A client wants AI tutoring that works inside the agent harness they already license,
with no new platform to host, procure or migrate — **and the output has to land in the LMS they already run.**

**Stack — all MIT, all verified this pass.**

| role | component | grant |
|---|---|---|
| diagnosis before teaching | [`SenmuuuuW/universal-diagnostic-tutor-skill`](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) · `075c189` | **MIT** |
| exam coaching + cross-session memory | [`ZeKaiNie/universal-examprep-skill`](https://github.com/ZeKaiNie/universal-examprep-skill) · `b9e84f5` | **MIT** |
| retention mechanics as a tool call | [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) · `ed6774d` | **MIT** |
| model-agnostic ITS surface | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) · `3708287` | **MIT** |
| explicit mastery model | [`MysterionRise/adaptive-knowledge-graph`](https://github.com/MysterionRise/adaptive-knowledge-graph) · `f88f69f` | **MIT** |
| 🆕 **package the output as SCORM** | [`kemalyy/edumints-scorm-mcp`](https://github.com/kemalyy/edumints-scorm-mcp) · `bd14b95` | **MIT** (1 069 B) |
| 🆕 **validate the package** | [`giacomomaria81/scorm-mcp-server`](https://github.com/giacomomaria81/scorm-mcp-server) · `fd5f110` | **MIT** (1 070 B) |
| bundle reference | [`flysheep-ai/education-skills`](https://github.com/flysheep-ai/education-skills) · `b4c9352` | **MIT** |

**Wiring.** The diagnostic skill runs first and writes a mastery estimate into `adaptive-knowledge-graph`'s
Bayesian tracker — this is the piece most skills lack, and without it "adaptive" means "whatever is in the
context window". `anki-mcp-server` and `tutor-mcp` attach over MCP, so spacing and tutoring are tool calls
rather than prompt instructions.
🆕 **The new closing move: `edumints-scorm-mcp` assembles whatever the pack produces into a SCORM package and
`scorm-mcp-server` validates the zip — both over MCP, both MIT.** Until this pass that glue was always
hand-written per engagement. 🔵 **This is what makes the pack deliverable rather than a demo: output that
imports into the client's existing Moodle, Canvas or Open edX with no integration project.** Two independent
servers of this shape exist, so the pattern is not resting on one maintainer.

🔴 **Stated limit.** A skill inherits the host's model, rate limits and data policy. Where automated
assessment is regulated (Korea's AI Basic Act, Vietnam's high-risk list) or student-data training restricted
(California AB 1159), this pattern needs `P91-B`'s recorder underneath it or it is not a compliance position.

## `P91-D` — Offline-first delivery for constrained connectivity (APAC and LATAM)

**The ask it answers.** UNESCO's finding on APAC is explicit: adoption is gated on IT infrastructure,
connectivity and teacher training — not on model quality. A cloud tutor is the wrong artefact for most of the
region's deployment conditions, and the same holds across much of LATAM.

**Stack.**

| layer | component | grant |
|---|---|---|
| delivery | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) · `d4fea9c` | **MIT** (1 097 B) |
| lesson model | [`oppia/oppia`](https://github.com/oppia/oppia) · `ad22e91` + [`oppia/oppia-android`](https://github.com/oppia/oppia-android) · `25e3860` | **Apache-2.0** |
| interactive content playback | [`tunapanda/h5p-standalone`](https://github.com/tunapanda/h5p-standalone) · `b5ac7dd` | **MIT** (1 077 B) |
| local tutor | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) · `f0142f2` | **MIT** |
| 🆕 local-model curriculum reference | [`pguso/agents-from-scratch`](https://github.com/pguso/agents-from-scratch) · `da3f9df` | **MIT** (1 091 B) |
| pt-BR reference implementation | [`belentani7/aprende-brasil`](https://github.com/belentani7/aprende-brasil) · `bbeea5a` | **MIT** (1 085 B) |

**Wiring.** Kolibri handles sync-when-connected delivery; Oppia supplies the structured lesson model;
`h5p-standalone` plays H5P interactive content **without pulling in the GPL H5P core** — that substitution is
the whole point of including it. The tutor runs against a local model (Ollama-class), degrading to retrieval
over cached material when no model is available. 🆕 `agents-from-scratch` is included because it is the one
permissive curriculum written **against a local LLM** — the right teaching material when student data cannot
leave the building, which is the same constraint that drives the rest of this stack.
`aprende-brasil` already implements exactly this shape in pt-BR with an offline fallback and 205 modules —
**read it before building.**

## `P91-E` — Brazilian public-sector student records with AI on top (LATAM)

**The ask it answers.** A Brazilian municipality or state network wants AI assistance over student records it
already keeps. Brazil has a national AI strategy but **no sectoral education regulation** and **PL 2338 is
still awaiting a Chamber vote**, so the institution is the decision-maker and the cycle is short.

**Stack.**

| layer | component | grant | posture |
|---|---|---|---|
| SIS of record | [`portabilis/i-educar`](https://github.com/portabilis/i-educar) · `2.12` · `cd1da68` | 🔴 **GPL-2.0** (18 092 B) | 🔴 **Separate service — do NOT link, do NOT absorb** |
| AI layer | your service, **across a process/network boundary** from i-educar | 🟢 closed | 🔴 **GPL-2.0 has no linking exception** — the boundary is what keeps the deliverable closed |
| record trail | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) · `cb794e4` | **Apache-2.0** | 🟢 |
| 🆕 programming-practice + autograding | [`mumuki/mumuki-laboratory`](https://github.com/mumuki/mumuki-laboratory) · `fce1ede` | 🔴 **AGPL-3.0** (34 523 B) | 🔴 **LTI 1.3 only — never in the deliverable** |
| incumbent LMS bridge | [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) · `f30df11` | 🔴 GPL-3.0 | 🔴 integrate only |

🔴 **This pattern was re-costed this pass, and the licence it was built on was wrong.** Pass 91 wrote
*"i-educar is **linked, never forked** — **LGPL-3.0 permits exactly that**, and this distinction makes
the engagement possible."* 🔴 **i-educar is GPL-2.0** (title block: *"Version 2, June 1991"*), which has
**no linking exception at all**, so the sentence that made the engagement possible was the sentence that
was wrong. See `verticals/solutions.md` and `compose/code/grant-ladder-v4/README.md` (`P960`).

**Wiring, corrected.** i-educar stays the system of record and runs **as its own deployed service** —
unmodified, unlinked, and outside the deliverable's build. The AI layer sits beside it **across a process
or network boundary**, reading through i-educar's HTTP interfaces and its database only via exported
views, and writing xAPI into `lrsql` (Apache-2.0). Where the network also runs Chamilo (common across
LATAM), bridge by LTI 1.3 rather than modifying it.

🔵 **Cost effect, stated plainly rather than buried.** The pattern survives — 🔴 **but it is no longer
the cheap one.** Linking would have allowed in-process extension; a service boundary means the
integration surface must be specified, versioned and tested, and **anything the client wants changed
*inside* i-educar is a GPL-2.0 contribution, not a deliverable feature.** Scope that explicitly in the
statement of work. 🔵 **If the ask can tolerate a different system of record, `OpenEduCat` (LGPL-3.0,
genuinely verified) is the only platform on this shelf where the original linking strategy is legal.**
🆕 **Where the ask includes programming education — and in Argentina and Brazil it often does —
`mumuki-laboratory` is the regional incumbent with real classroom use and automated feedback. It is AGPL, so
it attaches over LTI 1.3 alongside the deliverable and never inside it.**

🟢 **Credibility anchor for the pitch:** cite the **IADB/BID ILIA index** (AI readiness, adoption and
governance across 19 countries) rather than a market-research CAGR. A development-bank index is something a
rector's office or a ministry already recognises.

🔵 **This pattern exists because of a correction.** Pass 87 recorded *"no permissive open-source SIS exists"*
and stopped. True but incomplete: no SIS is permissive, and a **large linkable one** is, and it is
LATAM-origin with municipal deployments. The missing move was distinguishing *permissive* from *usable*.

## `P91-F` — 🆕 The accessibility conformance gate (North America first, EMEA second)

**The ask it answers.** Section 508 / WCAG exposure on course content, and an institution that needs
**evidence** rather than an assurance. 🔴 **This KB declared for five passes that no permissive AI
accessibility checker existed. That was false**, and the cause was the query naming the industry instead of
the standard (see `intel/trends.md` `T5`).

**Stack — all MIT, all verified from the payload this pass.**

| role | component | grant |
|---|---|---|
| audit + CI regression gate | [`tomaszboloz/WCAG-Accessibility-Skills`](https://github.com/tomaszboloz/WCAG-Accessibility-Skills) · `main` · `1b095c2` | **MIT** (1 070 B) |
| prevention at authoring time | [`Community-Access/accessibility-agents`](https://github.com/Community-Access/accessibility-agents) · `main` · `decf6ba` | **MIT** (1 069 B) |
| web **and PDF** scanning | [`9mtm/WCAG-Checker`](https://github.com/9mtm/WCAG-Checker) · `main` · `d34decd` | **MIT** (4 219 B) |
| evidence store | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) · `cb794e4` | **Apache-2.0** |
| content playback under audit | [`tunapanda/h5p-standalone`](https://github.com/tunapanda/h5p-standalone) · `b5ac7dd` | **MIT** |

**Wiring.** `WCAG-Accessibility-Skills` runs as the audit CLI in the content pipeline's CI, producing a dated
WCAG 2.1/2.2 finding set per course artefact; its findings are written as xAPI statements into `lrsql`, so the
institution holds a **time-series of conformance** rather than a one-off report.
`accessibility-agents` runs one tier earlier — inside the authoring host — so AI-generated course material is
checked **before** it is committed, which is cheaper than auditing it afterwards. `9mtm/WCAG-Checker` covers
the **PDF** surface, which is where institutional exposure actually lives: handouts, readings and scanned
packs, not the LMS chrome.

🟢 **The feature to sell is the refusal.** `WCAG-Accessibility-Skills` states explicitly that it **cannot
declare legal conformance from an automated pass** and keeps a human-review boundary. 🔵 **A checker that
overclaims is a liability in a dispute**; one that documents the boundary between automated evidence and
human judgement is exactly what counsel wants. Price the human-review step as part of the engagement rather
than pretending the tool removes it.

🔴 **Deliberate exclusions, and why.** [`qed42/ai-accessibility-checker`](https://github.com/qed42/ai-accessibility-checker)
is the most capable-looking tool in this space — Python CLI plus GitHub Action, WCAG 2.0–2.2 A/AA/AAA — and is
**described in search summaries as MIT while carrying no licence payload in 24 filenames.** Excluded.
`albertomf1979/wcag-accessibility-agent`: same, no payload. `ucfopen/UDOIT` is **GPL-3.0** and not AI-driven —
it stays an integration, never a component.
🔴 **Stated gap this pattern does not close: instructional alignment.** It proves content is *accessible*, not
that it *teaches the stated outcome*. There is still no permissive checker for that.

## `P91-G` — 🆕 The AI-literacy curriculum factory (APAC first, EMEA second)

**The ask it answers.** 🟢 **Four jurisdictions now mandate AI instruction rather than merely regulate AI
systems** (`intel/trends.md` `T7`): **China** (MoE, ≥8 h/year from age six, since Sep 2025), **Singapore**
(MoE, Mar 2026, all schools by 2027), **India** (CBSE, Classes 3–8, session 2026-27, notification 9 Apr 2026)
and the **EU** (AI Act Art. 4 staff literacy, in force now). Someone has to write the material, localise it,
train the teachers and assess it. 🔴 **No incumbent product covers this, and the deadlines are real.**

**Stack.**

| role | component | grant |
|---|---|---|
| adult/teacher-training spine | [`microsoft/ai-agents-for-beginners`](https://github.com/microsoft/ai-agents-for-beginners) · `main` · `ff2ba66` | **MIT** (1 141 B) |
| engineering depth track | [`rohitg00/ai-engineering-from-scratch`](https://github.com/rohitg00/ai-engineering-from-scratch) · `main` · `b6a7a17` | **MIT** (1 070 B) |
| local-model track (data cannot leave) | [`pguso/agents-from-scratch`](https://github.com/pguso/agents-from-scratch) · `main` · `da3f9df` | **MIT** (1 091 B) |
| agent-course reference | [`huggingface/agents-course`](https://github.com/huggingface/agents-course) · `main` · `3c469e7` | **Apache-2.0** (11 357 B) |
| lesson structure + explanations | [`oppia/oppia`](https://github.com/oppia/oppia) · `ad22e91` | **Apache-2.0** |
| assessment of the curriculum | [`numbas/Numbas`](https://github.com/numbas/Numbas) · `39b03e5` | **Apache-2.0** |
| packaging into the client LMS | [`kemalyy/edumints-scorm-mcp`](https://github.com/kemalyy/edumints-scorm-mcp) · `bd14b95` | **MIT** |
| completion + literacy evidence | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) · `cb794e4` | **Apache-2.0** |

**Wiring.** The four permissive curricula are the **source material for the teacher-training tier, not the
pupil tier** — be explicit about that with the client. Re-express the concepts through Oppia's structured
lesson model to get age-appropriate sequencing and explanation-driven interactions; author assessment in
Numbas; package with `edumints-scorm-mcp` so it drops into the ministry's or district's existing platform; and
record completion into `lrsql` — which, for the EU, **is the Article 4 literacy evidence**, and for a district
is the Ohio-style policy evidence. One pipeline, two compliance outputs.

🔴 **The honest gap, and it is the opportunity.** Every permissive AI curriculum found is written for **adult
developers**. 🔴 **Nothing on this shelf addresses primary-school AI literacy — the exact scope China has
already implemented and India begins this session.** The pupil-facing material has to be authored, and that
authoring is the billable core of this pattern rather than an input to it.
🔴 **Licence trap specific to this pattern: curriculum is content, and content is where non-commercial clauses
cluster.** [`cccareers/open-source-curriculum`](https://github.com/cccareers/open-source-curriculum) is
**CC-BY-NC-SA-4.0** — reference only, never in a paid deliverable. Check the grant on every piece of
curriculum before it enters the pipeline, and read the payload rather than the badge: this pass's own
instrument briefly mis-read that very row as public domain.

## `P92-A` — 🆕 Mastery-gated progression: the learner model the shelf lacked for eight passes

**The ask it answers.** An institution already has content and a tutor, and the complaint is that the tutor
is *"confidently helpful and never actually knows whether the student learned anything."* They want
progression gated on **evidence of mastery per skill**, not on completion or on a model's impression of the
conversation. 🔵 **This is the most common follow-on ask after a tutor pilot succeeds**, and until this pass
this shelf had no permissive answer to it — `Gap 335`, named openly for eight passes.

**Stack — permissive end to end, so the whole thing is closable.**

| layer | component | grant (payload · bytes · ref · SHA) | posture |
|---|---|---|---|
| mastery estimation | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | **MIT** · 1 066 B · `main` · `77c3e90` | 🟢 in the deliverable |
| skill graph / prerequisites | [`MysterionRise/adaptive-knowledge-graph`](https://github.com/MysterionRise/adaptive-knowledge-graph) | **MIT** · 1 094 B · `main` · `f88f69f` | 🟢 in the deliverable |
| tutor turn (option A) | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | **Apache-2.0** · 11 408 B · `main` · `6cf793b` | 🟢 in the deliverable |
| tutor turn (option B) | [`fborrasumh/tutoria`](https://github.com/fborrasumh/tutoria) | **MIT** · 1 120 B · `main` · `65b2903` | 🟢 in the deliverable — pick this one where the **teacher must validate the lesson first** |
| orchestration | [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | **MIT** · 1 072 B · `main` · `12aeb0f` | 🟢 |
| item bank / assessment | [`numbas/Numbas`](https://github.com/numbas/Numbas) | **Apache-2.0** · 11 357 B · `master` · `39b03e5` | 🟢 SCORM-packageable |
| evidence trail | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | **Apache-2.0** · 11 357 B · `main` · `cb794e4` | 🟢 |
| delivery | the client's LMS, via LTI 1.3 / SCORM | 🔴 theirs | 🔴 integrate, never fork |

**Wiring — the loop, concretely.**

1. **Tag the item bank to skills.** `Numbas` questions carry skill tags; the skill graph in
   `adaptive-knowledge-graph` holds prerequisites. 🔵 **This is the only genuinely manual step and it is
   where the engagement's domain value sits** — budget it as content work, not engineering.
2. **Every graded interaction becomes an xAPI statement** into `lrsql`. The LRS is the training corpus *and*
   the audit trail — **one store, two purposes**, which is why this stack is cheap to run.
3. **Fit a tracing model offline on that corpus.** `pykt-toolkit` gives DKT/AKT/SAINT/LPKT behind one
   interface, so the model is a swappable component rather than an architectural commitment. 🟢 **Start with
   **BKT or DKT** — interpretable, and an institution will ask *"why did it say my student hasn't mastered
   this?"* on day one.
4. **Serve a per-skill mastery probability** as a service the agent calls as a tool. 🔵 **The agent asks the
   model what the student knows; it does not infer it from the transcript.** That inversion is the whole
   pattern.
5. **Gate progression on a threshold**, and route the tutor's next turn from the weakest prerequisite — not
   from the syllabus order.
6. **A teacher sees and can override every gate.** 🔴 **Non-negotiable, and not for pedagogical reasons:**
   mastery gating decides what a student is allowed to attempt, which is *evaluating learning outcomes* —
   **EU AI Act Annex III high-risk**, and squarely inside Oklahoma's and Maryland's human-oversight floors.
   The override log is the Article 27 evidence.

**Timeline.** 6–8 weeks to a gated pilot on one course with an existing item bank; **+4–6 weeks** if the
item bank has to be skill-tagged from scratch. 🔴 **The binding constraint is interaction data, not
modelling**: a tracing model needs history, so a cold-start course gates on BKT priors and a rubric for the
first term. **Say this in the proposal** — a client who expects adaptive behaviour in week one will read a
correct implementation as a failure.

🔴 **Stated honestly: this is a build, not an integration.** Nothing on this shelf wires a tracing model to
an agent's turn today — `pykt-toolkit` is a benchmark library, not a service. **The glue (steps 2, 4 and 5)
is bespoke, and it is also the defensible part.** Tracked as `Gap 369`.

🔴 **And mind the name collision:** [`JonathanSilver/pyKT`](https://github.com/JonathanSilver/pyKT) is also
MIT and answers the same search string, but its README states its models do not match the originals'
performance. **Pin `pykt-team/pykt-toolkit` by slug in the dependency manifest** (`P968`).

🟢 **Where to sell it first.** EMEA and North America, because the oversight requirement that makes this
pattern *expensive* is also what makes it *procurable*: an institution facing Annex III or an Ohio district
policy needs a defensible decision trail, and **a mastery model with a teacher override and an LRS behind it
is that trail.** 🔵 The same build satisfies Vietnam's 72-hour incident reporting with a log subscriber.

## `P91-RETIRED` — "the platform is always the client's; the intelligence on top is ours"

🔴 **Retired as a universal rule, and it stays retired.** It was derived from the false `8 of 8 copyleft`
census and survived six passes. It remains correct for one case only — when the client's existing Moodle,
Canvas or Open edX must be kept — and in that case LTI 1.3 / SCORM / xAPI integration is still the right
boundary. 🟢 **Otherwise the platform can be inside the deliverable:** `Artemis` (MIT), `Sakai` or `Opencast`
(ECL-2.0), `OpenOLAT` (Apache-2.0), 🆕 `richie` (MIT, portal layer), `pupilfirst` / `relate` / `academico` (MIT).

*Prior pass content is preserved in git history at commit `306eb06` and earlier.*
