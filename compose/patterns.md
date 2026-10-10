---
industry: education
region: Global
updated: 2026-10-10
---

# Education — compose patterns

**Pass 93, 2026-10-10.** ⏱️ **Third pass of this date.** Each pattern names the specific repos, the licence
posture of the whole stack, and how the pieces wire together.

🔴 **Provenance of the licences below, stated precisely because it differs by row.** The repos in `P93-A`
and `P93-B` were resolved **this pass**: existence, default ref and SHA from `git ls-remote --symref`, the
licence **read from the payload** at `raw.githubusercontent.com/<slug>/<SHA>/<file>`, and the family
determined **by reading the payload's title block** — because this session's sandbox cannot execute
`compose/code/grant-ladder-v4/ladder.sh`, and `P237` forbids forking its shared classifier to replace it
(`P970`). 🟡 **Every repo in `P91-*` and `P92-A` is carried at its pass-92 SHA and was NOT re-resolved this
pass.** 🔵 **So treat a pass-92 row as a pass-92 measurement, and re-run v4 before quoting a licence into a
contract.**

🔴 **`P91-E` was re-costed this pass because the licence it was built on was wrong.** It stated that
`portabilis/i-educar` is LGPL-3.0 and that *"LGPL-3.0 permits exactly that, and this distinction makes the
engagement possible"*. **i-educar is GPL-2.0, which has no linking exception.** The pattern survives but the
integration boundary — and therefore the cost — changed. See `P91-E` below and
`compose/code/grant-ladder-v4/README.md`.

🟢 **Two new patterns this pass.** **`P93-A`** supersedes `P92-A`'s modelling layer with the psychometric
stack (`repos/foundations.md` Tier 2c) — and `P92-A` stays on the page, because the two differ in a way that
decides engagements rather than in detail. **`P93-B`** is the first pattern in this KB anchored on a
**national curriculum published as audited open data**, and the first with a **measured** justification for
its own central design choice.

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

## `P93-A` — 🆕 The adaptive assessment you can defend in an audit (supersedes `P92-A`'s modelling layer)

**The ask it answers.** *"We want adaptive testing — shorter tests, same confidence — and when a parent or a
regulator asks why a student got the item they got, or why the system says they haven't mastered a skill, we
need an answer that isn't 'the model decided'."* 🔵 **`P92-A` answers the first half. It does not answer the
second half, and under Annex III the second half is the one that blocks go-live.**

🔴 **Why this is a separate pattern rather than an edit to `P92-A`.** `P92-A` estimates mastery with a
**deep** tracing model (`pykt-toolkit`: DKT, AKT, SAINT). That is the right choice when the goal is
predictive accuracy over a large interaction corpus. 🔴 **It is the wrong choice when the deliverable has to
explain itself**, and *"assessing learning outcomes"* is named high-risk in the EU AI Act's Annex III, which
owes the person assessed an explanation. 🟢 **The classical psychometric stack gives the same loop with
parameters a human can read — and, measured this pass, it is also the better-licensed and more
production-worn option.** `intel/trends.md` `T10`.

**Stack — permissive end to end. All five modelling rows were resolved from the payload this pass.**

| layer | component | grant (payload · bytes · ref · SHA) | posture |
|---|---|---|---|
| item calibration | [`nd-ball/py-irt`](https://github.com/nd-ball/py-irt) | **MIT** · `LICENSE` 1 121 B · `master` · `6514928` | 🟢 in the deliverable |
| item calibration (alternative) | [`eribean/girth`](https://github.com/eribean/girth) | **MIT** · `LICENSE.txt` 1 064 B · `master` · `daf2277` | 🟢 — the one `catsim`'s own README points at |
| adaptive session | [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | **BSD-3-Clause** · `LICENSE` 1 514 B · **`dev`** · `7e6caae` | 🟢 — 🔴 **pin the ref: the default branch is `dev`, not `main`** |
| per-skill mastery | [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | **MIT** · `LICENSE` 1 132 B · `master` · `cc1682e` | 🟢 in the deliverable |
| review scheduling | [`open-spaced-repetition/py-fsrs`](https://github.com/open-spaced-repetition/py-fsrs) | **MIT** · `LICENSE` 1 079 B · `main` · `9446cb0` | 🟢 optional, and cheap |
| deep model, for comparison only | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | **MIT** · 1 066 B · `main` · `77c3e90` (pass-92 SHA) | 🟡 **offline benchmark, not in the serving path** |
| item bank | [`numbas/Numbas`](https://github.com/numbas/Numbas) | **Apache-2.0** · 11 357 B · `master` · `39b03e5` (pass-92 SHA) | 🟢 SCORM-packageable |
| evidence trail | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | **Apache-2.0** · 11 357 B · `main` · `cb794e4` (pass-92 SHA) | 🟢 |
| orchestration | [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | **MIT** · 1 072 B · `main` · `12aeb0f` (pass-92 SHA) | 🟢 |
| delivery | the client's LMS, via LTI 1.3 / SCORM | 🔴 theirs | 🔴 integrate, never fork |

**Wiring — and the seams are the libraries' own, not ours.**

1. **Author or import the item bank into `Numbas`**, tagged to skills. 🔵 Unchanged from `P92-A`, still the
   manual step where the domain value sits, still budgeted as content work.
2. **Calibrate the bank with `py-irt`.** Fit 2PL or 3PL over historical responses → **difficulty and
   discrimination per item, ability per learner, on one scale.** 🔴 **Do this before any adaptive session
   runs**: `catsim` selects items *using* these parameters and cannot produce them —
   **its README says so in its own words**: *"catsim does not implement item parameter estimation."*
   🟢 **That sentence is why this stack composes instead of overlapping**, and it is also the honest answer
   to "why two IRT libraries?" — `girth` is the drop-in alternative the same README names.
3. **Run the adaptive session with `catsim`**: initialiser → **item selector** → ability **estimator** →
   **stopping rule**. 🟢 **The stopping rule is the commercial payload** — it is what turns "shorter tests"
   from a claim into a parameter, and it is auditable: *stop when the standard error of the ability estimate
   falls below X*.
4. **Track mastery across sessions with `pyBKT`**, not within them. 🔵 **IRT answers "how able is this
   learner right now, on this scale"; BKT answers "has this learner learned this skill yet".** Different
   questions, and the institution asks both. `pyBKT`'s four parameters per skill — **prior, learn, slip,
   guess** — are the ones you put on a teacher's screen.
5. **Every response becomes an xAPI statement into `lrsql`** — the calibration corpus and the audit trail in
   one store, as in `P92-A`.
6. **Schedule retention with `py-fsrs`** where the subject rewards it (languages, vocabulary, clinical
   facts). 🟡 Optional. 🔵 **It answers a question neither IRT nor BKT does — *when will they forget* — so
   it is additive, not a third opinion on the same question.**
7. **Benchmark the deep model offline against the psychometric one, and keep it offline.** 🟢 Run
   `pykt-toolkit` on the same `lrsql` corpus and report the accuracy difference honestly. 🔵 **If DKT is
   materially better on the client's data, that is a finding worth presenting — and still not a reason to
   put it in the serving path of a high-risk decision without an explanation layer in front of it.**
8. **Teacher override on every gate, logged.** 🔴 Non-negotiable, same as `P92-A`: the override log is the
   Article 27 / human-oversight evidence.

**Timeline.** 🟢 **5–7 weeks to a calibrated adaptive pilot on one course with ≥ ~300 historical responses
per item-ish bank**; **+3–4 weeks** without historical response data, because calibration then needs a
seeding round. 🔵 **Faster than `P92-A`'s 6–8 weeks for a reason worth saying out loud: IRT needs far less
data than a deep tracing model, and classical psychometrics was designed for exactly the sample sizes a
single institution actually has.**

🔴 **What this pattern does *not* cover, stated before a client discovers it.** It is **structured
assessment only** — items with scorable responses. 🔴 **Open-response and essay scoring is not in this stack
and cannot be bolted on from this shelf**: the whole permissive supply is one 2★ research repository
(`Gap 372`, `agents/top.md`). 🔵 **Which means the activity the EU AI Act names most explicitly is the one
with the least open supply. Scope essays out, or price them as bespoke with a human grader in the loop.**

🟡 **Two integration cautions, both measured.** `catsim`'s default branch is **`dev`** — pin it in the
manifest or a `main`-assuming CI will fail. And `girth`'s grant lives in **`LICENSE.txt`**, not `LICENSE`;
a shallow licence scanner will report it as ungranted (`P969`'s neighbourhood).

🟢 **Where to sell it first.** 🟢 **EMEA** — Annex III makes the explainability the procurement criterion,
and Jisc's 38-institution marking pilots show the sector is already buying in this area. 🟢 **North
America** second, where Oklahoma's and Maryland's human-oversight rules and Ohio's district-policy deadline
create the same need without the same deadline pressure. 🔵 **And `catsim` being Brazilian is a real asset
in a LATAM pitch** — 🟡 though its placement rests on the project's documentation host rather than a payload
copyright line, so say "Brazilian-authored", not "a Brazilian product".

## `P93-B` — 🆕 Curriculum-aligned tutoring for Brazil, with the grounding decision made by measurement

**The ask it answers.** A Brazilian state secretariat, municipal network or private group wants a tutor or a
lesson-planning assistant that is **aligned to the BNCC** — and wants the alignment to be *true*, with the
official code cited, not a plausible-looking label. 🔴 **This is the ask that fails most often in this
industry, because an ungrounded model will produce a BNCC code that looks exactly right and is invented.**

🟢 **And for once the size of that failure is measured, by a third party, reproducibly.**
[`bncc-dev/bncc-benchmark`](https://github.com/bncc-dev/bncc-benchmark) — 8 models, 300 items:

| condition | hallucination rate | what it means for the build |
|---|---|---|
| 🔴 no source in context | **31.9 %** | 🔴 roughly **one citation in three is wrong**. Unshippable. |
| 🟢 **dataset embedded in the prompt** | **0.2 %** | 🟢 **the design choice** |
| 🟡 MCP tool call to the dataset | **2.3 %** | 🟡 **ten times worse than embedding, fourteen times better than nothing** |

🔵 **So the architecture is decided by evidence rather than taste: embed the curriculum data in the context
for alignment, and keep the tool call for what the data cannot answer.** `intel/trends.md` `T11`.

**Stack.**

| layer | component | grant (payload · bytes · ref · SHA) | posture |
|---|---|---|---|
| curriculum data | [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) | 🟡 **`LICENSE` = MIT** 1 073 B · `main` · `daabd7d` — 🔴 **but the data under `dados/` is CC BY 4.0** (`P969`) | 🟢 in the deliverable, **with attribution** |
| packages + MCP | [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) | 🟢 **split grant at the root** · `LICENSE` 1 299 B · `main` · `ac9feb8` → MIT code + CC BY 4.0 data | 🟢 — `@bncc/dados` 0.3.1, `@bncc/mcp` 0.2.0, PyPI `bncc` 0.2.0. 🟡 **all pre-1.0: vendor the version** |
| alignment regression | [`bncc-dev/bncc-benchmark`](https://github.com/bncc-dev/bncc-benchmark) | 🟢 split · `LICENSE` 911 B · `main` · `4713901` → MIT harness + CC BY 4.0 items | 🟢 **run it as your CI gate, not as a citation** |
| second MCP opinion | [`dfdb76/bncc-mcp`](https://github.com/dfdb76/bncc-mcp) | **MIT** · 1 218 B · `main` · `f94ca6a` | 🟡 independent implementation — useful as a cross-check |
| tutor turn | [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) | **MIT** · 1 069 B · `main` · `032b5aa` (pass-92 SHA) | 🟢 — Colombian, **already Open edX-integrated** |
| pt-BR content | [`belentani7/aprende-brasil`](https://github.com/belentani7/aprende-brasil) | **MIT** · 1 085 B · `main` · `bbeea5a` (pass-92 SHA) | 🟢 205 modules, **offline local fallback** |
| autograding (optional) | [`mumuki/mumuki-laboratory`](https://github.com/mumuki/mumuki-laboratory) | 🔴 **AGPL-3.0** · 34 523 B · `master` · `fce1ede` (pass-92 SHA) | 🔴 **integrate across a network boundary; never absorb** |
| offline delivery | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** · 1 097 B · `develop` · `d4fea9c` (pass-92 SHA) | 🟢 where connectivity binds |
| SIS, if records are in scope | [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | 🔴 **GPL-2.0** (**not** LGPL — see `P91-E`) | 🔴 service boundary only |

**Wiring.**

1. **Vendor `bncc-dados` into the deliverable** — JSON or SQLite, pinned to a commit, **not** fetched at
   runtime. 🟢 **Its provenance is the selling point and it is checkable**: every record carries a `fonte`
   (spreadsheet row + official PDF page), **1 576 of 1 580 BNCC-2018 texts match the MEC/CNE PDF character
   for character**, the 4 mismatches are documented in `DECISOES.md`, and **CI re-runs the extraction
   pipeline and rejects divergence.** 🔵 **A state secretariat can audit the dataset against its own
   ministry's PDF. Almost nothing else in this KB can say that.**
2. **🔴 Honour the data licence, and know that your tooling will not tell you to.** The code is MIT; **the
   data is CC BY 4.0**, which is an **attribution obligation** — and the grant is in `dados/LICENSE.md`,
   **not at the repo root**, where neither the 24-name ladder nor GitHub's own sidebar can see it
   (`P969`). 🟢 **Put the attribution in the product's about screen and in the proposal's IP annex at the
   start**, where it costs nothing; retrofitting it after a procurement review does not.
3. **Embed, don't call — because 0.2 % beats 2.3 %.** Load the objectives for the relevant stage and
   component into the context. 🟢 Use the MCP server (`@bncc/mcp`, **7 tools**, dataset embedded so queries
   stay local) for **search and decoding across the whole base** — the long-tail lookups that will not fit
   in context — and keep citation-critical paths on embedded data.
4. **Gate every release on the benchmark harness.** 🟢 `bncc-benchmark`'s `harness/` is **MIT**, so run it
   as your own regression suite against *your* prompt and *your* model: **a measured faithfulness number per
   release, on the client's own configuration.** 🔵 **That converts "aligned to the BNCC" from a marketing
   claim into a CI check with a number** — and it is the single most differentiating artefact in this
   pattern.
5. **Teacher validates before the student sees it.** Take the primitive from `fborrasumh/tutoria`: lesson →
   **teacher validation** → student. 🔴 Not optional where assessment or progression is touched.
6. **Deliver through what the network already runs** — Open edX (🔴 **AGPL-3.0**, integrate) or Moodle
   (🔴 **GPL-3.0**, integrate), or `Kolibri` (MIT) where connectivity is the binding constraint.

**Timeline.** 🟢 **4–6 weeks** to a BNCC-grounded lesson-planning assistant with a measured faithfulness
number — **the fastest credible pattern on this page**, because the hard part (a verified, machine-readable,
provenance-carrying curriculum base) is already built and granted. **+3–4 weeks** to attach a tutor turn and
teacher validation; **+4 weeks** for offline delivery via `Kolibri`.

🔴 **Three risks, named.** **(a) Pre-1.0 dependencies** — all three packages are below 1.0, so vendor the
version and expect breaking changes. **(b) The benchmark's publisher has a declared conflict of interest** —
*"a Profy opera produtos que usam LLMs sobre a BNCC"*, disclosed in its own README, with methodology, items
and raw responses published so the numbers can be recalculated. 🔵 **A disclosed conflict with reproducible
workings is a better position than an undisclosed one, and the right response is to re-run the harness
yourself — which step 4 already does.** **(c) Its own two surfaces disagree on corpus size** (description:
15 300 responses / 17 models; README: 19 models × 900, 17 100 published). 🟢 **Cite the grounding
percentages, which are the study's headline; do not cite a corpus size from the description.**

🟡 **Generalisation limit, so this pattern is not oversold.** The 0.2 % figure is **one benchmark, one
curriculum, one language, 300 items.** 🔵 **The direction is almost certainly general; the magnitude is
not.** Use it to justify the architecture — embed the standards data — **never to promise a client 0.2 %.**

🟢 **And the portable half of this pattern.** Steps 1, 2 and 4 — **vendor a verified standards dataset, honour
its data licence, gate releases on a faithfulness harness** — are jurisdiction-independent. 🔴 **What is not
portable is the dataset**: no other national curriculum was found published this way (`Gap 371`). 🔵 **So
outside Brazil this pattern is a *build the dataset first* engagement, and `bncc-dados` is the reference
implementation to copy — including the character-exact verification against the official PDF, which is what
makes it auditable rather than merely open.**

## `P91-RETIRED` — "the platform is always the client's; the intelligence on top is ours"

🔴 **Retired as a universal rule, and it stays retired.** It was derived from the false `8 of 8 copyleft`
census and survived six passes. It remains correct for one case only — when the client's existing Moodle,
Canvas or Open edX must be kept — and in that case LTI 1.3 / SCORM / xAPI integration is still the right
boundary. 🟢 **Otherwise the platform can be inside the deliverable:** `Artemis` (MIT), `Sakai` or `Opencast`
(ECL-2.0), `OpenOLAT` (Apache-2.0), 🆕 `richie` (MIT, portal layer), `pupilfirst` / `relate` / `academico` (MIT).

*Prior pass content is preserved in git history at commit `306eb06` and earlier.*
