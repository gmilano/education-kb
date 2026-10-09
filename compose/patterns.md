---
industry: education
region: Global
updated: 2026-10-09
---

# Education — compose patterns

**Pass 90, 2026-10-09.** Every repo named below was resolved this pass by `git ls-remote --symref` with its
**licence read from the payload** at the pinned SHA. Each pattern names the specific repos, the licence posture
of the whole stack, and how the pieces wire together.

## `P90-A` — The closable AI university platform (EMEA, and the pattern that replaces "no permissive platform exists")

**The ask it answers.** A European institution wants a self-hosted learning platform, extended with AI, received
as a **closed, owned deliverable**. Six passes of this KB answered that with *"impossible — the platform tier is
copyleft"*. It is not.

**Stack — permissive end to end, no copyleft anywhere.**

| layer | component | grant |
|---|---|---|
| platform | [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) · `develop` · `760e2e1` | **MIT** (1 091 B) |
| tutor | **Iris**, in-tree | MIT with the platform |
| feedback | **Athena**, in-tree | MIT with the platform |
| exercise authoring | **Hyperion** (Spring AI), in-tree | MIT with the platform |
| assessment engine | [`numbas/Numbas`](https://github.com/numbas/Numbas) · `master` · `39b03e5` | **Apache-2.0** (11 357 B) |
| learner-data trail | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) · `main` · `cb794e4` | **Apache-2.0** (11 357 B) |
| statement mapping | [`adlnet/xAPI-SCORM-Profile`](https://github.com/adlnet/xAPI-SCORM-Profile) · `master` · `ea17c40` | **Apache-2.0** (11 324 B) |
| content shim | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) · `master` · `882f3b8` | **MIT** (1 072 B) |

**Wiring.** Fork Artemis. Iris/Athena/Hyperion are config-gated — point them at the client's model endpoint
(sovereign or on-prem) rather than a vendor API. Package Numbas assessments as SCORM and serve them through
`scorm-again`, so assessment content stays portable if the platform later changes. Every Iris interaction and
Athena feedback event emits an xAPI statement shaped by `xAPI-SCORM-Profile` into `lrsql`; that store is the
**human-oversight evidence** the AI Act asks for, and it exists before the 2 Dec 2027 deadline rather than after.

**Why this beats the alternative.** The honest previous answer was "build beside the client's Moodle". This
delivers the same capability with the platform inside the deliverable, and the AI subsystems are already written.

## `P90-B` — The district AI-compliance recorder (North America)

**The ask it answers.** Ohio requires every K-12 district to adopt a formal AI policy by **1 Jul 2026**; 30+
states have guidance; 134 bills are live across 31 states. Districts have a legal deadline and no instrument.
California's AB 1159 would additionally bar training on student data absent direct school benefit.

**Stack.**

| layer | component | grant |
|---|---|---|
| record store | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | **Apache-2.0** |
| statement vocabulary | [`adlnet/xAPI-SCORM-Profile`](https://github.com/adlnet/xAPI-SCORM-Profile) | **Apache-2.0** |
| conformance gate | [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) | **Apache-2.0** |
| orchestration | [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | **MIT** |
| HE platform (if in scope) | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | **ECL-2.0** |

**Wiring.** Put every AI interaction behind a LangGraph node that emits one xAPI statement per event:
*which learner, which model, which prompt class, which human reviewed it, which policy clause authorises it*.
Store in `lrsql`; validate the statement shapes against `ADL_LRS` so conformance is demonstrable rather than
asserted. The deliverable is a policy document **plus a running record that evidences the policy** — the second
half is what no incumbent is selling.

**Deliberate exclusion.** No GPL component. `LearningLocker` is the better-known LRS and is **GPL-3.0**;
`lrsql` is Apache-2.0 and better maintained. Using the famous one here would convert the deliverable.

## `P90-C` — The pedagogy skill pack (global, lowest cost to ship)

**The ask it answers.** A client wants AI tutoring that works inside the agent harness they already license,
with no new platform to host, procure or migrate.

**Stack — all MIT, all verified this pass.**

| role | component | grant |
|---|---|---|
| diagnosis before teaching | [`SenmuuuuW/universal-diagnostic-tutor-skill`](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) · `075c189` | **MIT** |
| exam coaching + cross-session memory | [`ZeKaiNie/universal-examprep-skill`](https://github.com/ZeKaiNie/universal-examprep-skill) · `b9e84f5` | **MIT** |
| retention mechanics as a tool call | [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) · `ed6774d` | **MIT** |
| model-agnostic ITS surface | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) · `3708287` | **MIT** |
| explicit mastery model | [`MysterionRise/adaptive-knowledge-graph`](https://github.com/MysterionRise/adaptive-knowledge-graph) · `f88f69f` | **MIT** |
| bundle reference | [`flysheep-ai/education-skills`](https://github.com/flysheep-ai/education-skills) · `b4c9352` | **MIT** |

**Wiring.** The diagnostic skill runs first and writes a mastery estimate into
`adaptive-knowledge-graph`'s Bayesian tracker — this is the piece most skills lack, and without it "adaptive"
means "whatever is in the context window". `anki-mcp-server` and `tutor-mcp` attach over MCP, so spacing and
tutoring are tool calls rather than prompt instructions. Ship as one versioned skill pack.

🔴 **Stated limit.** A skill inherits the host's model, rate limits and data policy. Where automated assessment
is regulated (Korea's AI Basic Act, Vietnam's high-risk list) or student-data training is restricted
(California AB 1159), this pattern needs `P90-B`'s recorder underneath it or it is not a compliance position.

## `P90-D` — Offline-first delivery for constrained connectivity (APAC and LATAM)

**The ask it answers.** UNESCO's finding on APAC is explicit: adoption is gated on IT infrastructure,
connectivity and teacher training — not on model quality. A cloud tutor is the wrong artefact for most of the
region's actual deployment conditions, and the same holds across much of LATAM.

**Stack.**

| layer | component | grant |
|---|---|---|
| delivery | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) · `d4fea9c` | **MIT** (1 097 B) |
| lesson model | [`oppia/oppia`](https://github.com/oppia/oppia) · `ad22e91` + [`oppia/oppia-android`](https://github.com/oppia/oppia-android) · `25e3860` | **Apache-2.0** |
| interactive content playback | [`tunapanda/h5p-standalone`](https://github.com/tunapanda/h5p-standalone) · `b5ac7dd` | **MIT** (1 077 B) |
| local tutor | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) · `f0142f2` (local-first) | **MIT** |
| pt-BR reference implementation | [`belentani7/aprende-brasil`](https://github.com/belentani7/aprende-brasil) · `bbeea5a` | **MIT** |

**Wiring.** Kolibri handles sync-when-connected delivery; Oppia supplies the structured lesson model;
`h5p-standalone` plays H5P interactive content **without pulling in the GPL H5P core** — that substitution is
the whole point of including it. The tutor runs against a local model (Ollama-class), degrading to retrieval
over cached material when no model is available. `aprende-brasil` already implements exactly this shape in
pt-BR with an offline fallback and 205 modules — read it before building.

## `P90-E` — Brazilian public-sector student records with AI on top (LATAM)

**The ask it answers.** A Brazilian municipality or state network wants AI assistance over student records it
already keeps. Mexico's ATDT plan names *software público* and sovereignty; Brazil has national AI strategy but
**no sectoral education regulation**, so the institution is the decision-maker and the cycle is short.

**Stack.**

| layer | component | grant | posture |
|---|---|---|---|
| SIS of record | [`portabilis/i-educar`](https://github.com/portabilis/i-educar) · `2.12` · `cd1da68` | 🟡 **LGPL-3.0** (18 092 B) | 🟡 **Link, do not absorb** |
| AI layer | your service, over i-educar's interfaces | 🟢 closed | 🟢 LGPL permits linking |
| record trail | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | **Apache-2.0** | 🟢 |
| incumbent LMS bridge | [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) via LTI 1.3 / SCORM | 🔴 GPL-3.0 | 🔴 integrate only |

**Wiring.** i-educar stays the system of record and is **linked, never forked into the deliverable** — LGPL-3.0
permits exactly that, and this is the distinction that makes the engagement possible. The AI layer sits beside
it as a separate service reading through i-educar's interfaces and writing xAPI into `lrsql`. Where the network
also runs Chamilo (common across LATAM), bridge by LTI 1.3 rather than modifying it.

🔵 **This pattern exists because of a correction.** Pass 87 recorded *"no permissive open-source SIS exists"* and
stopped. True but incomplete: no SIS is permissive, and a **large linkable one** is, and it is LATAM-origin with
municipal deployments. The missing move was distinguishing *permissive* from *usable*.

## `P90-RETIRED` — "the platform is always the client's; the intelligence on top is ours"

🔴 **Retired as a universal rule.** It was derived from the false `8 of 8 copyleft` census and survived six
passes. It remains correct for one case only — when the client's existing Moodle, Canvas or Open edX must be
kept — and in that case LTI 1.3 / SCORM / xAPI integration is still the right boundary. 🟢 **Otherwise the
platform can be inside the deliverable:** `Artemis` (MIT), `Sakai` or `Opencast` (ECL-2.0), `OpenOLAT`
(Apache-2.0), `pupilfirst` / `relate` / `academico` (MIT).

*Prior pass content is preserved in git history at commit `457eaba` and earlier.*
