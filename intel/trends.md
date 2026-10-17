---
industry: education
region: Global
updated: 2026-10-17
---

# Trends — Education, October 2026

> What changed, what it means for a studio engagement, and how confident the evidence is.
> **T1–T9 are from pass 264. T10 is revised and T11–T14 are new in pass 265**
> ([evidence](../evidence/verified-repos.2026-10-17-p265.tsv)), which also retracts two of this
> base's own declared gaps.

## T1 — The education agent consolidated around one project

`HKUDS/DeepTutor` is at **41.5k stars** with a release dated **2026.10.8**, under
**Apache-2.0**. This base previously published 22k for the same repository. Nothing else in
education is within an order of magnitude: the next education-specific agent found is
`Study-Mate` at 1.0k, then `education-agent-skills` at 873.

**For the studio:** the "which tutoring agent" question is effectively settled for
greenfield work. Spend the discovery hours on the student-data model and the integration
boundary instead.

## T2 — Education agents are shipping as *skills*, not applications

The single clearest structural shift this pass. Across the `ai-tutor` and `education-ai`
topic listings, the fastest-rising education repositories are agent **skill packages**:
`education-agent-skills` (873), `lineage-skill` (458, Apache-2.0),
`universal-examprep-skill` (308), `Bloom` (288), `universal-diagnostic-tutor-skill` (246),
`flysheep-ai/education-skills` (114), `skill-instructional-design`, `bloom-taxonomy-quiz-builder-skill`.
Even `instructional_agents` — a peer-reviewed EACL'26 system — published a Claude Code
Skills release (2026.4.15) alongside its v1.1.0.

**For the studio:** the deliverable shape is changing. A client who already runs an
assistant does not want a second web app; they want a skill inside the one they have. That
is a smaller build, a faster sale, and a much shorter integration path. Price accordingly.

## T3 — MCP is becoming the integration layer for education tooling

`ankimcp/anki-mcp-server` (MIT, 516) exposes spaced repetition to any MCP client;
`ArnaudGuiovanna/tutor-mcp` (MIT, 49) turns an LLM into a tutoring system; `Selleo/mentingo`
ships an MCP endpoint as a first-class LMS feature. Meanwhile the GitHub topic
`mcp-server-education` **has never been used by any public repository**.

**For the studio:** a real and growing category with no label. Low-cost, high-visibility
opening for whoever publishes and tags the first substantial education MCP server.

## T4 — EMEA's compliance deadline moved, and that is the engagement

The EU AI Act's high-risk obligations for education moved from **2026-08-02** to
**2027-12-02** via the AI omnibus amendments (in force 2026-07-27). **Transparency duties
went live on 2026-08-02 regardless.**

**For the studio:** two distinct offers, not one. A short remediation scope now (AI
disclosure, deepfake disclosure) and a 14-month compliance-by-design build before December
2027. Clients reading the delay as a reprieve are the pipeline.

## T5 — "Teach about AI before teaching with it" is now written policy

Brazil's MEC published a *Referencial* for responsible AI in education (March 2026) and
basic-education curriculum guidance (April 2026), with an official framing of avoiding
careless tool use in basic education. Mexico's SEP found **76% of professors make materials
with AI but only 36% teach students to use it**, with 9 in 10 asking for training. India
made AI and computational thinking **compulsory from Class 3** from AY 2026-27.

**For the studio:** the biggest funded demand in education AI right now is **curriculum and
teacher formation**, not student-facing tutors. Three governments on three continents are
buying the same thing.

## T6 — Digital sovereignty turned open source into the default, not the discount

Brazil's MEC *Referencial* explicitly calls for national solutions that reduce dependence on
global platforms. Moodle 5.1 added provider-level control and per-course/per-activity AI
toggles, so a local Ollama or vLLM endpoint is a supported configuration rather than a hack.

**For the studio:** self-hosted open source plus local inference is now the *compliant*
architecture in Brazil and the *sovereign* architecture in EMEA. The cost argument is no
longer the main argument, which is a much stronger place to sell from.

## T7 — Knowledge tracing is quietly broadening into cognitive diagnosis

`pykt-toolkit` is the reference benchmark at **450 stars** — materially smaller than this
base previously claimed (1.2k), and worth knowing before citing it as an "industry standard".
Around it: `EduData` (Apache-2.0, 313) for datasets, `pyedmine` (MIT, 82) covering tracing
*plus* cognitive diagnosis *plus* recommendation, `EduStudio` (MIT, 78) for unified
cognitive modelling.

**For the studio:** when the ask is "what should this student do next" rather than "what
does this student know", `pyedmine` is the better base. Both are MIT.

## T8 — Academic integrity became an assessment-architecture problem

`dodona-edu/dolos` (MIT, 352) for source-code plagiarism, `Artemis` (MIT, 819) for automated
feedback with an auditable exercise runner, `Numbas` (Apache-2.0) for randomised maths
assessment. Randomisation and provenance are design choices in the assessment, not
detectors bolted on after.

**For the studio:** in jurisdictions barring AI from high-stakes decisions (Oklahoma,
Maryland, NYC's K-8 moratorium), *assessment integrity* is the part of the AI story that is
unambiguously permitted. Lead with it where student-facing AI is restricted.

## T9 — The licence surface under education AI is unreliable, including ours

Four published cells failed verification this pass and one repository is gone:

- `openedx/edx-platform` is **AGPL-3.0**, not Apache-2.0 as previously published — a
  network-copyleft obligation on the most likely MOOC base in the shelf.
- `CaviraOSS/PageLM` ships a bespoke **non-commercial** licence that prohibits
  redistribution outright. **This base's own `evidence/verified-repos.2026-10-15-p213.tsv`
  grades it `MIT`.**
- `sakaiproject/sakai` is **ECL-2.0**, not Apache-2.0. `chamilo-lms` is GPL-3.0, not GPL-2.0.
  `instructional_agents` is MIT, not Apache-2.0.
- `OpenEduCat-Inc/OpenEduCat` is a **404**; the canonical repo is `openeducat/openeducat_erp`
  (LGPL-3.0).
- `GeminiLight/awesome-ai-llm4education` serves **no LICENSE file**, against a published MIT
  claim.

Counter-example in the other direction: `Open-TutorAi/open-tutor-ai-CE` opens *"All rights
reserved"* and **is** plain BSD-3-Clause — that phrase is part of the BSD form. Flagging it
would have been a false positive, and a false retraction costs a usable row.

**For the studio:** read the `LICENSE` payload for every repository that enters a client
deliverable. A secondary source, an aggregator table, a GitHub sidebar badge and this
knowledge base have all been wrong about an education licence in the last two weeks.

## T10 — The permissive platform market is three candidates deep *(revised)*

**Revised 2026-10-17 (pass 265).** The earlier version of this entry said *one*. Payload
verification of a wider candidate set makes it **three**, and they are not substitutes:

| Platform | Licence | Stars | The job it is actually good at |
|----------|---------|-------|--------------------------------|
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | Apache-2.0 | — | Behaves like an institutional LMS (courses, cohorts, assessment, administration) |
| [oppia/oppia](https://github.com/oppia/oppia) | Apache-2.0 | **6.9k** | Structured lesson delivery with formative feedback in the lesson model; 17,004 commits |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** | 1.2k | Offline-first distribution — runs with no network, syncs opportunistically; 39,803 commits |

Everything else at full-LMS scale remains copylefted (Moodle GPL-3.0, Open edX AGPL-3.0,
Chamilo/ILIAS/Gibbon GPL, Sakai and Opencast ECL-2.0, Vacademy and frappe/lms AGPL-3.0,
OpenEduCat LGPL-3.0, frappe/education GPL-3.0).

**For the studio:** the licence objection now has three answers instead of one, and the right
one depends on the job — which is a much better conversation than "there is exactly one". The
two architectural answers still hold where the client keeps a copyleft platform: an **LTI
tool** (`tsugi`, Apache-2.0) or an **XBlock** (Apache-2.0).

**And a warning about where the earlier claim came from.** Two platforms that 2026-dated
sources recommended to this KB as permissive do not survive payload verification:
**forma.lms** is **GPL-2.0** (published by a review as Apache-2.0), and **Fedena** — still
cited as *the* Apache-2.0 education ERP — has **no licence payload at all** and has been
abandoned since **2012** (community fork: 2016). Both directions of error appear in the same
pass: a permissive platform missed, and two permissive platforms imagined.

## T11 — Offline-first is a licence-free lane nobody is contesting

`learningequality/kolibri` (MIT, 39,803 commits) is a complete learning platform built on the
assumption that **there is no network** — content channels sync when a link appears and the
application is fully functional when it does not. No other platform in this KB is designed
that way; offline support elsewhere is a feature, not an architecture.

**For the studio:** this is the only credible base for rural LATAM, low-bandwidth APAC and
anywhere power is intermittent, and the AI layer has to follow the same assumption — a
quantised local model (Ollama), scheduling via FSRS, telemetry that syncs on contact. It is
also the cheapest possible answer to a data-sovereignty question, because nothing leaves the
device. Retrofitting offline onto a server-rendered LMS is a rebuild; starting from Kolibri is
a configuration.

## T12 — LATAM publishes the platform layer, in Portuguese, and this base had missed it

[`portabilis/i-educar`](https://github.com/portabilis/i-educar) — GPL-2.0, 719★, **34,948
commits**, last commit **2026-10-14** — is a Brazilian school-management system that started
in the *prefeitura de Itajaí (SC)* and was published on the Brazilian federal **Portal do
Software Público in 2008**. Its teacher portal `i-diario` (AGPL-3.0) committed on
**2026-10-09**. Its licence payload is in **Portuguese**.

This KB declared for several passes that *"the region consumes this layer; it does not yet
publish it."* That was an artefact of searching in English.

**For the studio:** in Brazil the question is not *which platform* but *how to put an agentic
layer on the one the client already runs*, with the copyleft held on the platform side of an
HTTP/LTI boundary. The sovereignty story that MEC's *Referencial* asks for is already
satisfied by the base — Brazilian maintainers, federal software-public provenance, local
inference — which turns a compliance conversation into a delivery conversation.
**Legal note:** i-Diário's payload is a *Portuguese translation* of AGPL-3.0; FSF translations
are unofficial, so cite the English text in a SOW.

## T13 — The most-adopted education agent in open source is APAC-origin

`HKUDS/DeepTutor`'s README states it is *"led by Bingxi Zhao within the **HKUDS Group**"* and
credits the *"director of the **Data Intelligence Lab @ HKU**"* — the University of Hong Kong.
At **41.5k stars** it is the most-adopted education agent anywhere, and the learner-modelling
layer beneath it is substantially Chinese-academic: `bigdata-ustc/EduData` (USTC),
`HFUT-LEC/EduStudio` (Hefei University of Technology).

Earlier passes of this KB declared "no APAC-origin education agent surfaced" **while listing
DeepTutor as its top row**. The gap was in the reading, not the supply.

**For the studio:** APAC is the research supply centre for education AI. An APAC engagement is
*integration* work on locally-authored components, not import — and saying so in a Hong Kong,
Singapore or mainland pitch changes who you sound like. The genuine APAC gap is a **platform**,
which is narrower and more actionable.

## T14 — Autograding is permissive, mature, and the answer regulators will accept

The "no open-source grading" gap this KB has declared was about **agents**. The platforms are
fine: `jupyter/nbgrader` (**BSD-3-Clause, 1.4k**) for notebooks, `autolab/Autolab`
(**Apache-2.0, 808**, CMU-origin) for programming assignments with a course-management shell,
`Artemis` (MIT, 819) for feedback with an auditable runner, `Numbas` (Apache-2.0) for
randomised maths, `INGInious` (AGPL-3.0, UCLouvain) where AGPL is acceptable.

**For the studio:** in every jurisdiction tightening up — Idaho and Oklahoma barring AI from
high-stakes decisions, Ohio mandating district policy, the EU's Annex III naming evaluation of
learning outcomes, Brazil's `PL 2338` naming education selection as high-risk — a
**deterministic autograder with a human sign-off step** is permitted where an LLM grader is
not. Lead with nbgrader/Autolab and keep the model on the feedback side of the line. This is
the rare case where the compliant architecture is also the cheaper one.

## Confidence notes

- **Payload-verified (strongest):** every licence in this KB's tables, read from
  `raw.githubusercontent.com` on 2026-10-17.
- **Page-verified:** star counts, from repository pages or topic listings dated 2026-10-17.
- **Policy, primary-adjacent:** EU AI Act dates, Brazil MEC documents, India's curriculum
  mandate, SEP survey figures — reported consistently across multiple sources but read
  through secondary coverage, not official gazettes.
- **Vendor-sourced, treat as direction only:** all market-size figures; Moodle 5.2/5.3
  version and LTS-date claims.
- **Declared gaps, as revised by pass 265:** no school-level Japan data (population AI use,
  24.7%, is a different measure and not a substitute); **no APAC-origin *platform*** — the
  agent-and-research claim is retracted, see T13; **no LATAM-origin *agent* and no LATAM-origin
  *permissive* base** — the blanket LATAM claim is retracted, see T12; **no grading *agent***,
  while permissive grading *platforms* are mature, see T14; Mexico's draft AI statute status
  unestablished; Maryland `SB 720` disputed across trackers; Estado de México's April 2026
  reform truncated in all located sources.
- **A note on how three of those gaps were wrong.** Each was a *declared* gap — stated
  honestly, with the search named. Two were still false, and both failed the same way: the
  search ran in English against GitHub's star-sorted topic listings, which under-serve
  Portuguese-language government software and say nothing about an author's institution. An
  informed gap is still information, but a gap is a claim, and claims need re-testing against a
  channel that could falsify them. Pass 265 found both by probing candidate repositories
  directly (`git ls-remote` plus a licence-payload read) rather than by searching harder.
