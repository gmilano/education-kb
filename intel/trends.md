---
industry: education
region: Global
updated: 2026-10-17
---

# Trends — Education, October 2026

> What changed, what it means for a studio engagement, and how confident the evidence is.
> **T1–T9 are from pass 264. T10 is revised and T11–T14 are new in pass 265. T15–T17 are new in
> pass 266, which also revises T10 a second time and T14. T28–T31 are new in pass 270** — the
> European use-vs-efficacy gap, this base catching itself asserting a propagation it never
> performed, the 25% spread that appears in a regional market figure the moment a second publisher
> is found, and the measured direction in which a carried datum decays
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

## T10 — The permissive platform market is three candidates deep *(revised twice — now five)*

> **Pass 266 revision:** add **Sunbird** (MIT, national scale, APAC-origin) and **Artemis**
> (MIT, assessment-first, EMEA-origin). The shelf is **five** deep, not three. Each successive
> count in this base was published as if settled; the recurrence is the part worth noting —
> the number has only ever moved in one direction, which suggests the current five is also a
> floor rather than a finding. See [`verticals/solutions.md`](../verticals/solutions.md).


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

> **Pass 266 revision:** stronger than stated. Beyond `nbgrader` (BSD-3-Clause) and `Autolab`
> (Apache-2.0), **Artemis is MIT and ships an automated-feedback engine (Athena) plus an LLM
> tutor (Iris, MIT) and AI exercise authoring (Hyperion)** — and `numbas/Numbas` (Apache-2.0,
> Newcastle) executes assessment **entirely in the browser**, so submissions need never leave
> the device. ⚠️ One caveat for procurement: **Athena's own repo serves no licence payload** —
> Artemis's MIT grant does not automatically cover it. Get it in writing.


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

## T15 — The star count is the wrong instrument for publicly-funded education software

**This is the methodological finding of pass 266, and it generalises past education.**

[`Sunbird-Ed/SunbirdEd-portal`](https://github.com/Sunbird-Ed/SunbirdEd-portal) — the MIT-licensed
stack beneath **DIKSHA**, India's national school education platform under NCERT — has **41
stars** and **38,046 commits**.

| | Sunbird | A star-findable education agent |
|---|---|---|
| Stars | **41** | 300 – 41,500 |
| Commits | **38,046** | 21 – 12,437 |
| Forks | **317** | 1 – 395 |

Every search leg this base runs sorts GitHub topic listings **by stars**. Ministry-funded digital
public infrastructure is adopted by education departments and system integrators who deploy it;
it is not starred by developers browsing GitHub. **A project can serve a national school system
and remain structurally invisible to the instrument** — which is how this base declared "no
APAC-origin education platform" for 265 passes while an MIT one of national scale sat in plain
sight.

**What to do instead:** rank the *platform* layer by **commits and forks**, and probe
national-programme names directly (DIKSHA/Sunbird, i-Educar, Kolibri, Ceibal, Me Capacito). Note
the slug trap too: `Sunbird-Ed/sunbird-ed-portal` does not resolve, because the live slugs are
camel-case — and a kebab-case guess returns something indistinguishable from absence.

**Why this is commercially material, not just hygiene:** the stars-first instrument biases every
recommendation this base makes toward **US and developer-popular** projects and against
**government-built** ones. In public-sector education — most of the addressable market outside
corporate L&D — that is backwards. An APAC ministry briefed to import a Western LMS, when its
own national stack is MIT and already deployed, is a recommendation that would have lost on
both cost and politics.

**Confidence: high.** Directly measured; the star and commit counts are from the repository
pages this pass.

## T16 — Adoption has outrun governance in LATAM, and the deficit is the sellable work

⚠️ **Secondary-source grade** — `WebFetch` to `iesalc.unesco.org` failed DNS resolution this
pass, so the UNESCO IESALC study could not be read first-hand.

UNESCO IESALC, across **200 institutions in 19 countries**: **87%** use AI in at least one area
and **74%** in teaching and learning, while **26%** have a formal AI strategy. TALIS 2024 has
secondary teachers using AI at **56%** in Brazil, **55%** Chile, **53%** Colombia and **52%**
Costa Rica, against an **OECD average of 36%**.

**A 61-point gap between use and governance** is the single clearest commercial opening in this
base. The work it implies — AI-use policy, model inventories, human-review design,
assessment-integrity controls, procurement criteria, staff training — **requires no platform
displacement**, which is normally what kills a public-sector education deal. And it becomes
mandatory rather than advisable the moment Brazil's `PL 2338` lands with education-related
selection classified high-risk.

The inverse reading matters too: **LATAM is not a laggard market in this category.** Four
countries sit 16–20 points above the OECD average on teacher use. Briefing LATAM as
"behind on AI" is both wrong and the wrong sales posture; "ahead on use, ungoverned" is
accurate and points at a different, larger engagement.

**Confidence: medium.** The numbers are consistent across several reports, but those reports
cite the *same* UNESCO study, so they are not independent confirmations.

## T17 — Regulators are converging on "meaningful human review" as the thing that declassifies a system

The year's regulatory texts stop asking *whether* AI is used and start asking **whether a human
decides**. That turns a compliance question into an architecture question, which is the form a
studio can actually build against.

| Jurisdiction | The hinge |
|---|---|
| **Vietnam** ⚠️ | Automated assessment and behavioural monitoring are high-risk **only where the AI output is the sole basis for a decision without meaningful human review**. Deadline 2027-03-01; +6 months if live before 2026-08-15. |
| **Oklahoma** `SB 1734` | AI permitted **only with educator supervision and human review**; barred from high-stakes decisions. |
| **EU AI Act** | High-risk education duties (delayed to **2027-12-02**) are built on **human oversight**, documentation and conformity assessment. |
| **Idaho** `SB 1227` | Explicit bar on AI **replacing** human teachers. |
| **Maryland** | Human oversight; no high-stakes AI decisions about students. |

**The design consequence, and it is a build instruction rather than an observation:** a system
where the model *proposes* and a human *disposes* — and which can be shown, by configuration, to
have had AI off for any given decision — is a *lower regulatory class* than a system that
decides. The same functionality, differently wired, lands in a different legal category.

This is why [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) (MIT) is the most
strategically interesting row added in pass 266. Its **Iris**, **Athena** and **Hyperion**
subsystems are **config-gated**: the platform runs identically with AI disabled, and feedback is
suggested to an instructor rather than applied to a student. That is not a compliance feature
anyone retrofitted — it is how a university built it for its own use — and it is the posture
four of the five jurisdictions above are converging on.

**Confidence: medium-high** on the pattern (five jurisdictions, independent texts); ⚠️ **low-medium**
on the Vietnam specifics, which are secondary-source and whose dates conflicted across sources.

## T18 — Education ministries are now upstream maintainers, and one of them publishes under MIT

The public-sector layer this KB discovered with Sunbird in pass 266 is not one project. Ranked by
commits and probed by hand, pass 267 found a class:

| Programme | Repo | Licence (payload) | Commits | Stars |
|-----------|------|-------------------|---------|-------|
| UK Department for Education | [DFE-Digital/apply-for-teacher-training](https://github.com/DFE-Digital/apply-for-teacher-training) | **MIT** *(Crown Copyright)* | **34,414** | 38 |
| UK Department for Education | [DFE-Digital/teaching-vacancies](https://github.com/DFE-Digital/teaching-vacancies) | **MIT** | — | — |
| India / NCERT (DIKSHA) | [Sunbird-Ed/SunbirdEd-portal](https://github.com/Sunbird-Ed/SunbirdEd-portal) | **MIT** | 38,046 | 41 |
| German school-cloud stack | [hpi-schul-cloud/schulcloud-server](https://github.com/hpi-schul-cloud/schulcloud-server) | AGPL-3.0 | 16,192 | 81 |
| Brazil (municipal lineage) | [portabilis/i-educar](https://github.com/portabilis/i-educar) | GPL-2.0 | 34,948 | 719 |

The UK row is the one that changes a pitch. `apply-for-teacher-training` is a **live production
government service** at `apply-for-teacher-training.service.gov.uk`, and its licence payload reads
*"Copyright (c) Crown Copyright (Department for Education)"* — **MIT**. A studio can read, reuse
and adapt a national education ministry's production code with no copyleft obligation at all.

**What this means commercially:** "we will build you a service like a ministry runs" stops being an
analogy. For a public-sector education engagement in EMEA there is now **working, MIT-licensed
reference code for the hardest parts** — application workflows, GOV.UK-pattern service design,
daily production automation — maintained by a department that has to keep it running.

🔴 **And the negative half of the trend is equally firm.** Two of the most-cited public programmes
publish **nothing usable**: Uruguay's **Plan Ceibal** has a GitHub organisation with *"no public
repositories"*, and **OpenEMIS**, the EMIS most associated with ministry deployment, resolves to a
**32-commit Docker packaging repo with no licence on any of 76 path/ref combinations**. Public-sector
provenance has to be **probed per programme**; it does not generalise from the region or the brand.

**Confidence: high** on every repository row (payloads and page metrics read first-hand this pass).
⚠️ **Org-handle grade only** on Schul-Cloud's German/ministry provenance — its README names no
funder, ministry or Land.

## T19 — Permissive autograding is not a gap, a workaround or an exception. It is a mature field with five options

Pass 266 reframed this base's grading gap from "no agent" to "the function lives in platforms".
Pass 267 closes it entirely by measurement:

| Repo | Licence (payload) | Stars | Commits | Covers |
|------|-------------------|-------|---------|--------|
| [Submitty/Submitty](https://github.com/Submitty/Submitty) | **BSD-3-Clause** | 802 | 9,316 | Submission + autograding + **TA grading workflow** (RPI/RCOS) |
| [jupyter/nbgrader](https://github.com/jupyter/nbgrader) | **BSD-3-Clause** | 1.4k | — | Notebook assignment and grading |
| [ucbds-infra/otter-grader](https://github.com/ucbds-infra/otter-grader) | **BSD-3-Clause** | 161 | 3,825 | Python **and R**; adapters for **Canvas and Gradescope** (UC Berkeley) |
| [autolab/Autolab](https://github.com/autolab/Autolab) | **Apache-2.0** | 808 | — | Autograding with a course-management shell (CMU) |
| [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | **MIT** | 819 | 12,437 | Build-test-analyse + feedback, config-gated AI (TUM) |

**Five options, three licences, zero copyleft, four continents of provenance between them.** Add
[`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) (BSD-3, **8.4k★**) as the
substrate and **the entire notebook-teaching lane is permissive end to end** — which this base had
never stated, because it had catalogued the graders without the thing they run on.

🔵 **The strategic read is a warning, not an opportunity.** Autograding is **solved and free**.
Proposing to *build* one is proposing to rebuild five mature systems; the billable work is
**integration, pedagogy and defensibility** — wiring a grader into the client's LMS, and making the
grade explainable to a regulator (T17) and to a student who appeals it. Note `otter-grader` ships a
**Canvas adapter**, so the integration half is partly solved too.

**Confidence: high.** All five licences payload-read; Submitty, otter-grader and jupyterhub measured
first-hand in pass 267.

## T20 — The licence risk has moved from the *name* of the grant to its *shape*

T9 established that the licence surface under education AI is unreliable, with mislabelled
families — Apache-stated-but-GPL, MIT-claimed-but-proprietary. Pass 267 found a harder class of
error: **repositories whose licence family is correctly reported and still tells you the wrong
thing**, because the grant is partitioned.

| Repo | What a label says | What the payload says |
|------|-------------------|----------------------|
| [PrairieLearn/PrairieLearn](https://github.com/PrairieLearn/PrairieLearn) | AGPL-3.0 | **Four partitions:** Community Edition AGPL-3.0; `apps/prairielearn/src/ee/` = **Enterprise Edition, separate terms**; **all client-side JS** AGPL-3.0; UIUC + outside-contributor portions **MIT** |
| [RunestoneInteractive/rs](https://github.com/RunestoneInteractive/rs) | MIT | MIT **except** the **Handsontable component — commercial software** requiring a compliance contact — plus two textbook texts under their own terms |
| [csmediapro/moodle-mcp-server](https://github.com/csmediapro/moodle-mcp-server) | AGPL-3.0 | AGPL-3.0 **and open-core**: premium plugin tools **sold separately** |
| [learningequality/kolibri-design-system](https://github.com/learningequality/kolibri-design-system) | *(none — "unlicensed")* | **MIT**, declared in `package.json` only |
| [DFE-Digital/apply-for-teacher-training](https://github.com/DFE-Digital/apply-for-teacher-training) | *(none — "unlicensed")* | **MIT**, at `main/LICENCE` — **the British spelling** |

**Four distinct failure modes, each of which produces a confident wrong answer:**

1. 🔴 **Directory-partitioned grants.** "AGPL-3.0" is wrong in two directions at once for
   PrairieLearn: too restrictive for the MIT portions, too permissive for the EE directory.
2. 🔴 **Exception lists with a commercial member.** An MIT headline over a **paid dependency**
   passes a licence audit and fails procurement.
3. 🔴 **Open-core.** The licence covers what ships free; the feature set in the demo may not be it.
4. 🔴 **Spelling and location.** `LICENCE` vs `LICENSE`, or a grant that exists only in package
   metadata, reads as *unlicensed* to any probe with a narrow path set — and "unlicensed" is the
   most expensive wrong answer available, because it discards usable code.

🔵 **Two operational rules follow, and both are cheap.** (a) **A GitHub sidebar "License" link with
no label is a signal, not a missing datum** — both partitioned-grant rows above show one. (b)
**Read the first paragraph of every payload, not just its title region.** Pass 266's rule (family
from the first 600 bytes) answers *which licence*; it can never answer *over which files*.

**Confidence: high.** Every row payload-read this pass.

## T21 — The LMS is becoming MCP-addressable, and the two big LMSs are not equally open about it

The integration layer T3 identified as "MCP is becoming the integration layer for education
tooling" now reaches the **institution's system of record**, not just the learner's study tools:

| | Canvas | Moodle |
|---|---|---|
| MCP server | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | [csmediapro/moodle-mcp-server](https://github.com/csmediapro/moodle-mcp-server) |
| Licence (payload) | 🟢 **MIT** | 🔴 AGPL-3.0, **open-core** |
| Stars / commits | **295** / 1,026 | **1** / 57 |
| Tools | **102–126** + 8 agent skills | **10** free |
| Platform source | AGPL-3.0, 78,765 commits | GPL-3.0 |

🟢 **The pattern worth naming: AGPL platform, MIT doorway.** Canvas's own source is AGPL-3.0, so a
studio stays outside it regardless — and `canvas-mcp` (MIT) makes staying outside it *more*
capable than forking would be, reaching roster, courses, assignments and grades through the API
with a permissive deliverable on top. This is the **shortest path in this entire KB from an agent
to a client's real institutional data**, and it requires no migration and no platform decision.

🔴 **The asymmetry is the finding, though.** Moodle is the world's most-deployed LMS and its MCP
surface is ~**1/300th** as adopted as Canvas's, copylefted, and partly commercial. **A proposal
promising "an agent over your LMS" without naming the LMS understates the Moodle case badly.**
Where the client runs Moodle, the honest answer is the AGPL open-core server or a direct build
against Moodle Web Services — i.e. actual engineering, not an install.

⚠️ **And the category is invisible to indexes:** the `mcp-server-education` GitHub topic is
**still empty** while five payload-verified education MCP servers exist. None was found through a
topic listing.

**Confidence: high** on every licence and metric (payload + page, first-hand). ⚠️ `canvas-mcp`'s
tool count is published inconsistently **on its own page** — About says 102, the README says 126 —
so cite the range.

## T22 — The curriculum-mandate wave is real, and it has a documented failure mode

Two APAC data points, pulling in opposite directions, should be briefed together:

🟢 **India is executing.** AI and computational thinking become compulsory from **Class 3**, with
the CT&AI curriculum for Classes 3–8 **launched on 2026-04-01** by the Education Minister;
implementation starts in the **2026–27 session**, Classes 9–10 follow in **2027–28**. Teacher
training runs through **NISHTHA**, and a **₹500 crore Centre of Excellence in AI for Education**
was announced in the 2025–26 budget.

🔴 **South Korea reversed.** Seoul mandated AI digital textbooks from 2025; adoption sat **below
30%** by March, and in **August 2025 the National Assembly stripped them of official textbook
status** after teachers' unions argued the pace had outrun preparation.

🔵 **The lesson for a studio is not "mandates create demand" — it is which half of the mandate is
unserved.** India's mandate lands on a country that already runs an **MIT-licensed national
platform** (Sunbird/DIKSHA, 38,046 commits) and a named teacher-training programme: the demand has
somewhere to execute. Korea's landed on content distribution without teacher readiness, and the
legislature withdrew it. **Teacher enablement, not content generation, is where a mandate
engagement either works or gets cancelled** — which is the same conclusion T5 reached from policy
text, now with a failed rollout behind it.

⚠️ **Confidence: medium.** Every figure here is **secondary-source**: news and education-sector
coverage reached through the search index. This session could not resolve a single non-GitHub host
by DNS on **either** instrument, so no primary ministry text was read. Treat dates as
decision-usable and figures as directional.

## T23 — The biggest permissive education codebase in the world is a curriculum platform whose curriculum you cannot have

**`code-dot-org/code-dot-org` is Apache-2.0 and has 215,796 commits** — 2.7x
`instructure/canvas-lms` (78,765), which pass 267 published as the largest education codebase this
KB had located. 901★, 538 forks, last commit **2026-10-17**, PR #76166. The GitHub sidebar shows a
License link **with no label**, which is exactly the signal pass 267 said to treat as "read the
payload in full" — and doing so is the whole trend.

The grant covers *"all source codes and assets"* **with one exception**: Code.org's *"proprietary
or licensed artwork, graphics, sounds, lectures, videos, logos, characters, fonts"*, which *"may
not be used or distributed or accessed in any manner other than directly via Code.org's own web
site, mobile applications, or social media channels ... **without modification or embedding in
another format**."* The `NOTICE` explains why that carve-out could not have been narrower: the
activities children actually remember are **licensed entertainment IP** — Minecraft (Microsoft),
Star Wars (Disney/Lucasfilm), Frozen (Disney), Ice Age (20th Century Fox), Angry Birds (Rovio),
Plants vs. Zombies (PopCap), The Amazing World of Gumball (Cartoon Network), The Bad Guys
(DreamWorks) — plus **Font Awesome Pro** and the Geist font (SIL OFL). **Code.org cannot
sublicense them, so neither can a studio.**

🟢 **Why this is a trend and not a licence anecdote: it structurally closes `Gap 367`, this base's
highest-priority demand-side gap.** `Gap 367` records that four jurisdictions now mandate AI
instruction — **China** (≥8 h/year from age six, since Sep 2025), **Singapore MoE** (Mar 2026),
**India CBSE** (Classes 3-8, session 2026-27) and the **EU AI Act Art. 4** staff-literacy duty —
and that *"every permissive AI curriculum on this shelf is written for adult developers"*, calling
it *"the largest named, dated, deadline-bearing demand on this shelf with no supply."* The gap
named **Code.org** and **MIT Day of AI** as the alternatives and never read either one's licence.

Now read: the gap is not under-searched, it is **correctly empty**. The world's largest K-12 CS
platform is permissive **in its engine and unlicensable in its content**; MIT Day of AI is
**CC-licensed**; and the reference framework both are organised on,
[`touretzkyds/ai4k12`](https://github.com/touretzkyds/ai4k12) (AAAI/CSTA), **serves no licence
payload at all**. Three independent sources of primary-school AI curriculum, three different
reasons you cannot ship it.

🔵 **So stop searching and change the deliverable.** For a K-5 or K-12 AI-literacy mandate the
honest proposal is **content origination on a free engine**: Apache-2.0 platform reuse, and
instructional design as the paid work. See [`compose/patterns.md`](../compose/patterns.md) `P17`.
🔴 **The failure mode to name explicitly:** a client who has seen Code.org assumes the curriculum
ships with the code. Discovering otherwise after signature is how this becomes a loss.

## T24 — Three LMSs are now MCP-addressable, and the most open one is the least adopted

Pass 267 established that the LMS is becoming MCP-addressable and that *"the two big LMSs are not
equally open about it."* Pass 268 found the third, and it breaks the implied correlation between
openness and usefulness.

| LMS | servers | best licence | best adoption | engagement posture |
|-----|---------|--------------|---------------|--------------------|
| **Canvas** | 2 | **MIT** (payload) | **295★ / 1,026 commits**, v1.14.0 Oct 2026, UIUC named | **Adopt.** One maintained choice. |
| **Moodle** | 1 | AGPL-3.0, **open-core** | 1★ / 57 commits | **Price twice.** Network clause *and* premium tools sold separately. |
| **Google Classroom** | **8** | **MIT** (payload on 6 of 8) | **2★ / 11 commits** at best | **Fork and own it.** Nobody upstream is carrying this. |

**The Google Classroom family in full:** `adriasantacreu` (46 tools, MIT at *metadata* grade — no
payload, no sidebar licence), `Kimmahone/edu-workspace-mcp` (MIT, 29 tools, reaches all of
Workspace for Education), `pengusto` (MIT, a correctly-attributed fork of `adriasantacreu` with
dual copyright in the payload), `alanmagno1` (MIT), `OmarNiazi` (MIT, read-only by construction),
`praisethefacts` (MIT), `faizan45640` (MIT), and
[`AStheTECH/mewcp-google-classroom`](https://github.com/AStheTECH/mewcp-google-classroom) — which
is **not open source at all**: a bespoke *"AStheTECH Community License (ACL) ... All rights
reserved"* at `LICENSE.md`, sitting in the same result set, describing itself the same way.

🔴 **Second instance of the PageLM pattern, and the lesson has sharpened.** `p238` built a
four-predicate lure gate for *deliberately mislabelled* repositories. This row **passes** that gate
on all three substantive predicates — it is not a fraud, it is simply **not permissive**. 🔵 **A
provenance gate and a grant read are different instruments and neither substitutes for the other.**
One in eight repositories in a category described identically by search was unusable, and only
reading the payload found it.

⚠️ **The scope asymmetry is the real commercial finding.** `canvas-mcp` reaches a course API;
`edu-workspace-mcp` reaches **Docs, Sheets, Slides, Forms, Drive and Classroom** — an entire
Workspace for Education tenant. The OAuth consent a pilot asks a school for is therefore much wider
than the feature being piloted, and `OmarNiazi`'s README states outright *"Google hasn't verified
this app."* In EMEA that is a GDPR conversation before an engineering one; in the US, FERPA/COPPA.
**Scope consent to the tools you enable and put it in the SOW.**

🟢 **And one new regional datum falls out of it.** `Kimmahone/edu-workspace-mcp` is the **first
Korean-language education agent this KB has payload-verified** — Korean README, Korean curriculum
standards referenced, and `docs_import_hwp` / `docs_export_hwpx` for Korea's national document
formats, which is *implementation* evidence rather than prose. Graded as **language** evidence, the
same grade as the Portuguese `ai_tutor_forge`, so Korea-origin is **not** asserted. It lands in the
one APAC jurisdiction with a comprehensive statute in force — South Korea's **AI Basic Act, 22
January 2026**.

## T25 — The most productive research channel this pass was not the web. It was this knowledge base

Three passes running have found shelf-grade rows that star-sorted search cannot see: pass 266 by
probing national-programme names, pass 267 by ranking on commits, and pass 268 — by **grepping this
repository**.

Both headline findings were already inside the base:

- **Ed-Fi.** `intel/open-gaps.md` carries it across at least six numbered gaps (`286`, `303`,
  `309`, `311`, `314`, plus `ACTION TM`/`TR`), records all five repositories as **Apache-2.0,
  payload-read, placed North America**, and states that **Ed-Fi DMS is the only permissive system of
  record this base has found.** Meanwhile `repos/foundations.md` had **no Ed-Fi row**, and
  `verticals/solutions.md` published in pass 267 that public-sector platforms exist for three
  regions *"and still none for North America."*
- **Code.org.** Named in `Gap 367` as the alternative to a missing permissive curriculum, and never
  probed. Grepping the slug `code-dot-org` returned **zero hits across every `.md` in this
  repository**, while the phrase `Code.org` hit four files.

🔴 **This is the third cross-shelf contradiction in three passes**, and it defeated the guard built
for exactly this. Pass 266's standing instruction — *"before republishing any declared gap, grep
the other shelves for its own counter-evidence"* — was followed, and still missed Ed-Fi, because
**the counter-evidence lives in the gap register, which is not a shelf.**

🟢 **Amended standing instruction, and it is cheap:**
1. **Grep `intel/open-gaps.md`**, not only the four `.md` shelves.
2. **Grep for the SLUG as well as the prose claim** — `code-dot-org` and `Code.org` are different
   searches and only one of them was ever run.
3. **Treat a gap note's "named alternative" as an unprobed lead with a deadline**, not as a
   discharge. `Gap 367` named two alternatives and read neither's licence for ~175 passes.

🔵 **Why this belongs in a trends file rather than a method note.** The research instrument defect
this base has been correcting since pass 265 was *external* — star-ranked search is blind to
ministry code. Pass 268's defect is *internal*: **the base knows more than its shelves say**, and
the gap between the two is now the single richest vein available to it. A pass that spends its first
ten minutes grepping itself will out-produce one that spends them searching.

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

### Pass 267 addendum to the confidence notes

- **The primary-source gap this base has carried since pass 266 is now diagnosed, and it is
  environmental.** Every non-GitHub host tried this pass failed DNS resolution on **both**
  instruments — `curl` and `WebFetch` alike: `ess.iesalc.unesco.org`, `iesalc.unesco.org`,
  `unu.edu`, `digital-strategy.ec.europa.eu`, `www.digitaleducationcouncil.com`, `ve.scielo.org`,
  `repositorio.cepal.org`, `www.marketsandmarkets.com`, plus the news hosts behind the APAC
  figures. GitHub-family hosts and package registries resolve normally. 🔵 **So "re-read the
  primary sources" is not an action a pass in this environment can discharge, and future passes
  should stop spending searches on it.** Non-GitHub material can be reached **only** as search-index
  text, which is secondary-source grade by construction — including every regional percentage in
  [`market.md`](market.md).
- **Repository evidence, by contrast, is at its strongest grade yet:** 31 rows this pass, 29
  licences read from payload or declared metadata, every star/fork/commit cell fetched from the
  repository page, and Sunbird's anomalous cells (41★ / 38,046 commits) **independently
  re-measured and reproduced exactly**.
- **A standing claim tested with a stronger instrument mostly survived.** Five "no licence
  payload" rows were re-probed against 19 paths x 4 refs; **four held** (Athena,
  autoGrader-frontend, openSIS-Classic, awesome-ai-llm4education) and one resolved to MIT at
  metadata grade. 🔵 Worth recording as explicitly as a correction: this base's careful calls are
  holding up, and a pass that reports only corrections misrepresents its own reliability.


## T26 — The curriculum-mandate wave has reached Africa and the Middle East, and the permissive supply has not

`T22` established the mandate wave and its failure mode. Pass 269 ran the four regional legs this
base had specified and never executed — **Kenya, Nigeria, South Africa, Egypt as four separate
queries** — and the wave is plainly there:

- 🇰🇪 **Kenya:** **10,382** public junior secondary schools in a World-Bank-funded (**KDEAP**)
  smart-classroom rollout; **62,000+** teachers ICT-trained as at **July 2026**.
- 🇳🇬 **Nigeria:** AI, cybersecurity, programming and robotics in the junior and senior secondary
  curriculum **from September 2025**.
- 🇪🇬 **Egypt:** a **UNESCO-launched national AI competency framework for teachers (2026-06-03)**,
  **236,000+** general-secondary students enrolled in coding and AI from **2025/26**, technical
  schools from **2026/27**, select primary and middle grades announced.
- 🇿🇦 **South Africa:** the counter-case — **the Draft National AI Policy 2026 was abrogated on
  2026-04-27**, leaving **no national instrument**, while **North-West University** became the first
  SA university with its own AI policy in **January 2026**.

🔴 **And the supply side is empty at the payload, not merely at the query.** Pass 269 located the
first two African-context education agents this base has ever carried —
[`muskvdc/EduTwin-Africa`](https://github.com/muskvdc/EduTwin-Africa) (South Africa, Grades 8–12) and
[`Valexxy/edunaija-os`](https://github.com/Valexxy/edunaija-os) (Nigeria) — resolved both default
refs, probed 19 paths on each, read the package metadata as a second channel, and found **no grant in
either**. Nigeria's **Naija Teacher AI** (UNESCO SDG4, offline-first, target **1.5M teachers by Q3
2026**) **states no licence**; Kenya's **Kytabu SOMANASI** is **proprietary**.

🔵 **Why this is the most commercially useful trend in this file.** It is the **inverse of LATAM**.
There, adoption outran governance and the sellable work is governance retrofit (`P13`). Here, **the
state programme arrives first** — funded, named, dated, with enrolment and teacher counts attached —
**and there is nothing off the shelf to satisfy it.** A market that has not yet bought anything is a
better starting position than one that has.

🟡 **The region splits on where to enter.** Kenya and Egypt have **national anchors** (a funded
rollout; a teacher-competency framework), so a ministry-level engagement has an instrument to attach
to. **South Africa has none at national level and a live one at institutional level** — so the same
pitch has to enter one country through a ministry and the next through a university.

⚠️ **Grade:** every figure above is **secondary-source**. `p268` established the non-GitHub DNS
failure as environmental, and pass 269 did not re-spend searches on primary retrieval. **There is
also still no MEA market sizing of any kind in this base** — the region now has programme rows and
no number.

## T27 — A licence can be inherited from a project template, and the most on-point artefact in a category is where that bites

`T20` moved licence risk from the **name** of a grant to its **shape**. Pass 269 found a third axis:
a grant's **provenance** — who chose it, and whether anyone chose it at all.

[`datawhalechina/ai-edu-for-kids`](https://github.com/datawhalechina/ai-edu-for-kids) is *"面向中小学的
人工智能通识课开源课程"* — an open-source **AI general-education course for primary and secondary
schools**, **128★ / 27 forks / 57 commits**, and **the most-adopted primary-band AI-curriculum
artefact this base has located.** It serves **no `LICENSE` payload on 19 of 19 paths**. Its README
declares **CC-BY-NC-SA-4.0** — NonCommercial *and* ShareAlike, the one shape a client deliverable
cannot carry. **And the line immediately after the declaration reads, verbatim:**

> *注：默认使用CC 4.0协议，也可根据自身项目情况选用其他协议*
> — "note: CC 4.0 is used by default; you may choose another licence depending on your project."

🔴 **The most restrictive attribute of the most relevant artefact in this category is boilerplate
carried over from an organisation's project template.** Nobody decided that this curriculum should
be non-commercial; the template said so, and the template's own text invites a different choice.

🔵 **Two practical consequences, in opposite directions.**
1. **Never assume it away.** A template default is legally identical to a deliberate NC-SA. Until an
   upstream says otherwise in writing, the course is unusable in a paid deliverable, and `P17`
   (originate the content, borrow only the specification) is the move.
2. **It is the licence most likely to change if asked.** Contrast a grant chosen *for* a reason —
   `PageLM`'s bespoke community licence, `AStheTECH`'s all-rights-reserved — which will not move.
   **A provenance read tells you which conversations are worth having**, and this base has, until
   now, recorded only the verdict and never who picked it.

🟡 **The same read has a second use, demonstrated this pass.**
[`muskvdc/EduTwin-Africa`](https://github.com/muskvdc/EduTwin-Africa) carries, in its README, *"Add
the project's chosen license here before publishing if a specific open-source license is required."*
**That is not an unlicensed project; it is a PRE-LICENCE one** — the author has written down that the
grant is missing. Against [`ls1intum/Athena`](https://github.com/ls1intum/Athena), silent through 76
path/ref probes across three passes, the difference is entirely actionable: **one of these rows is
worth an email and the other is not**, and only a provenance read separates them.

## T28 — European teachers have already adopted AI and already concluded the general-purpose tools do not work

The **Sanoma Learning 2026 European Teacher Survey** — **more than 20,000 teachers across 14
countries** — reports two numbers that have to be read together:

| | |
|---|---|
| European teachers using AI | **63%** |
| European teachers who believe **general-purpose** AI improves learning outcomes | **16%** |

**A 47-point gap between adoption and believed efficacy.** Adoption is not the open question in
EMEA; it is settled. What is open is whether the thing being adopted does anything.

**For the studio:** this inverts the standard pitch. The conversation is **not** "you should adopt
AI" — that argument is already won and the client has the receipts to prove it did not help. The
conversation is **"the general-purpose assistant your teachers are already using does not know your
curriculum, your assessment rules or your exam board, and that is why 84% of them do not think it
works."** Every education-specific, curriculum-bound asset on this base's shelves is an answer to
that sentence: `instructional_agents` (MIT) binds to a course spec, `Numbas` (Apache-2.0) binds to
an assessment, `OpenDidactia` (CC BY-SA 4.0) binds to **LOMLOE's own criteria**, and
`DECK6/korean-elementary-learning-map` (MIT) binds to a national curriculum graph.

⚠️ **Grade:** vendor-published survey. Sanoma sells education materials, so a finding that
general-purpose AI underperforms flatters the publisher's category. Carried anyway, for a specific
reason: **the 63% is self-damaging to the publisher's own "teachers need our tools" framing** (it
concedes teachers already have tools), and the direction is corroborated by `T22`'s independently
documented Korean failure — a mandated general-purpose rollout that reached **under 30% adoption**
and lost official textbook status. *Secondary-source; no primary channel available in this
environment.*

🔵 **The falsifiable form:** if a second, non-vendor European survey puts believed efficacy of
general-purpose AI materially above 16%, this trend weakens. Nobody has located one.

## T29 — A propagation claim is not evidence of propagation, and this base has now caught itself asserting one

Five consecutive passes have each found the same class of defect — a fact this base **knows** that
never reached a file this base **ships**. Pass 270's instance is a new species and the worst of the
five, because it is self-reporting:

Of the Sanoma survey above, `agents/trending.md` states, verbatim:
*"Recorded in `intel/market.md` and `intel/trends.md`."*

```
$ grep -c "Sanoma" intel/market.md intel/trends.md
intel/market.md:0
intel/trends.md:0
```

🔴 **A pass asserted the propagation it had not performed.** The four earlier defects were
omissions — silence, which a grep can find. **This one was worse than silence: it was a sentence
that answered the grep.** Any later pass auditing the register for unshelved datums would read that
line as proof the work was done, and `p269`'s backlog sweep — which found six unshelved datums by
grepping each one — **did not list Sanoma, because the register said it was shelved.**

**The method amendment, one line:** `p268` amended the **novelty** check to grep the *slug* rather
than the prose. **`p270` amends the *propagation* check to grep the DESTINATION file, never to
trust a claim in the source file.** Both defects were invisible to precisely the check that
preceded them, which is the argument for writing the amendment down rather than fixing the instance.

**For the studio:** the same failure mode is what a client's AI-governance register looks like after
two years. The deliverable that prevents it is not a better register — it is **a check that reads
the artefact instead of the claim about the artefact.**

## T30 — Regional market sizing is single-publisher sizing, and the EMEA number moves 25% when a second one shows up

This base's global market-size table is a **narrow band ($8.7–10.6B for 2026)** across five
publishers. Its **regional** figures are nothing like that well supported, and pass 270 measured
how badly:

| Europe, AI in education | 2026 | Horizon | CAGR |
|---|---|---|---|
| carried by this base ~200 passes | **$2.64B** | $8.0B by 2030 | 31.9% |
| MarketDataForecast | **~$2.11B** | ~$20B by 2034 | 32.47% |

**~25% apart on the same year, ~2.5× apart on the horizon, and their CAGRs agree to within half a
point** — so the entire disagreement is in the **baseline**, which is the one figure this base's own
market file instructs you to quote and the one a client slide actually carries. The leg that found
the second publisher states it could locate **no third**: two is the published universe for Europe.

🔵 **Why this generalises beyond EMEA.** The global band looks tight because five publishers
triangulate it. Every *regional* figure on this base — NA's **$3.68B**, MEA's **$0.56B**, LATAM's —
rests on **one** publisher each, and has never been tested the way EMEA's just was. **The tightness
of the global band is not evidence that the regional splits are sound; it is evidence that only the
global figure has been checked.**

**For the studio:** quote regional market size as a **range with the publisher count attached**
("$2.1–2.6B, two publishers"), or quote the global baseline and the regional *share*. A single
confident regional number is the one claim the evidence will not support — and a client who checks
will find the other publisher.

## T31 — A carried datum decays in one direction: toward overstating its own authority

Pass 270 re-verified six regional datums this base had carried in prose rather than on a shelf.
**Five of the six had changed shape.** The changes were not random:

| carried as | actually is | direction of the error |
|---|---|---|
| "the **STUDENTS FIRST Act** of 2026" | a student-written **model policy**, 82-16 in a mock Senate | 🔴 exercise → **statute** |
| "North Carolina's K-12 **implementation guidance**" | a **2024-01-16** DPI guidebook, two layers below NC's current position | 🔴 dated advisory → **current guidance** |
| "the **Linux Foundation LATAM AI workforce report**" | *Economic and Workforce Impacts of AI in Latin America*, 4th in a Meta-sponsored series | 🔴 real report → **a title that does not exist** |
| "the EMEA figure of **$2.64B**" | one of **two** publishers, ~25% apart | 🔴 a range → **a number** |
| "**Finland / Estonia / Netherlands** as K-12 leaders" | two stand on different grounds; the third is **unsubstantiated** | 🔴 one aggregator → **a grouping** |
| "the **US DOL AI Literacy Framework** (2026-02-13)" | confirmed, **TEN No. 07-25**, five content areas | 🟢 held |

🔴 **Every one of the five errors made the datum sound MORE authoritative than it was** — a model
policy gained the word "Act", a two-year-old guidebook became the current position, a report
acquired a cleaner title than the one it has, a forecast range collapsed into a point, and an
aggregator's grouping became a finding. **None of the five decayed toward understatement.**

🔵 **The mechanism is compression, not carelessness.** Each datum was shortened every time it was
restated, and the parts that get dropped when you shorten a fact are its **qualifiers** — the
status marker, the date, the publisher, the sample. What survives compression is the **claim**, and
a claim without its qualifiers reads as stronger than the evidence behind it.

**For the studio, and this is the transferable part:** a client knowledge base that has been
maintained by restatement — every quarterly deck summarising the last one — is **systematically
overconfident**, and the overconfidence is concentrated in exactly the cells a slide quotes.
**The audit that catches it is cheap and it is not an audit of the summary: re-run the original
query and compare.** Pass 270 ran six such queries and five came back different. **Budget one
re-verification pass per six carried datums**, and expect roughly that hit rate.
