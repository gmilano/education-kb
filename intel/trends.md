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
>
> **`T32`–`T35` are new in pass 271** — arithmetic as the second oracle a market shelf never
> used, the discovery that a source this base judged unreliable per-clause supplies a figure it
> quotes, the false declaration of ABSENCE (the inverse of `p270`'s false declaration of presence),
> and the over-broad retraction that an English-only search produced
> ([evidence](../evidence/p271-websearch.2026-10-17-p271.tsv)).
>
> **`T42`–`T45` are new in pass 274** — the threshold that was tuned to exclude its own defect's
> signature, the three amendments that were written and never built (one of which is now code), the
> licence this base refuted twice and which was MIT all along, and the market's stated blocker turning
> out to be this base's own recommended architecture
> ([window sweep](../evidence/arithmetic-sweep.2026-10-17-p274.tsv),
> [re-count](../evidence/quantity-recount.2026-10-17-p274.tsv),
> [repos](../evidence/verified-repos.2026-10-17-p274.tsv),
> [legs](../evidence/p274-websearch.2026-10-17-p274.tsv)).
>
> **`T40`–`T41` are new in pass 273.** **`T36`–`T39` are new in pass 272** — the regional market picture resolving to a single upstream
> publisher (so that this base's "independent corroboration" was circular), a gap that is true but
> carried at a stale *magnitude*, a publisher mislabelling its own CAGR window in four regional
> databooks, and the measurement that this base's own byte-count practice cannot discriminate
> ([evidence](../evidence/p272-websearch.2026-10-17-p272.tsv),
> [arithmetic sweep](../evidence/arithmetic-sweep.2026-10-17-p272.tsv)).

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
**still empty** while **20 distinct education MCP server slugs are shelved on `agents/top.md`**
(**15** when `p274` measured it, plus the five that pass shelved from `trending.md`).
None was found through a topic listing.
🔴 **This sentence read "five" until pass 272 and "12" until pass 274** — a true gap carried at a
stale magnitude, because passes 267, 268 and 273 added servers and updated the count on one shelf at
a time. 🟢 **`p274` stopped counting by hand:** the number is now derived by
[`compose/code/p274-quantity-recount/recount.py`](../compose/code/p274-quantity-recount/recount.py),
which re-derives every registered quantity from the rows and printed **3 STALE of 5** on its first
run. See `T37` and `T43`.

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

> 🔴 **CORRECTED IN PASS 274: it is SIX, and five of the six are reachable under MIT.** `p273`'s
> backlog item 7 asked for `T37` to be applied as a standing re-count; it was built
> ([`compose/code/p274-quantity-recount/`](../compose/code/p274-quantity-recount/)) and this is what
> it found. **Every row below was payload-read first-hand in `p274`**
> ([ledger](../evidence/verified-repos.2026-10-17-p274.tsv)):
>
> | platform | server | licence (payload, `p274`) |
> |---|---|---|
> | **Canvas** | `vishalsachdev/canvas-mcp` · 🆕 `bruchris/canvas-lms-mcp` *(`1 070` B, **opt-in FERPA pseudonymisation**)* | 🟢 **MIT** |
> | **Moodle** | `MarcosNahuel/moodle-mcp` *(teacher, writes)* · `Jawadh-Salih/moodle-mcp-server` *(student, Go)* | 🟢 **MIT** *(`p273`)* |
> | **Google Classroom / Workspace** | `Kimmahone/edu-workspace-mcp` *(29 tools, whole tenant)* | 🟢 **MIT** |
> | **Brightspace / D2L** | `RohanMuppa/brightspace-mcp-server` *(`1 068` B, reproduced to the byte)* | 🟢 **MIT** |
> | **Blackboard Ultra** | `felipedias-ie/blackboard-mcp` *(`1 084` B)* · `NiccoloSalvini/mcp-blackboard-ucsc` *(`1 073` B, public REST API)* | 🟢 **MIT** |
> | **Open edX** | `blend-ed/tutor-contrib-openedxmcp` *(`34 524` B, 33 tools)* | 🔴 **AGPL-3.0** |
>
> 🔴 **And the correction has a commercial consequence that reaches past the count.**
> [`intel/market.md`](market.md)'s players table tells a studio that **Blackboard / Anthology** is a
> *"replacement engagement; the incumbent's lock-in is the pitch."* **Blackboard has two MIT MCP
> doorways on this base's own trending shelf.** 🔵 **That is exactly the error `p267` corrected for
> Canvas** — *"the opening is the opposite of migration"* — **left standing for the other North
> American higher-ed incumbent.** The `AGPL platform, MIT doorway` pattern now holds for **five**
> platforms, and nobody has to be migrated off any of them.

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

> 🔴 **CORRECTED IN PASS 274 — the sentence above is superseded and the word "narrow" is wrong.**
> `p273` added Grand View's current vintage (`$11.4B`) to that table and corrected the band **on
> `intel/market.md` only**; this entry kept the number it was written with. **The 2026 band is
> `$8.7–11.4B`, 31.0% wide**, across **four independent models** (`T40`), not five publishers.
> 🔵 **This is `T37`'s species — a quantified claim decaying in its quantity on the shelf that was
> not updated — and it is the SECOND instance between these same two files.** The first was the MCP
> count. ⚠️ **It also undercuts this entry's own argument in the base's favour:** `T30` contrasts a
> tight global band against loose regional figures. **The global band is not tight.** The
> regional-vs-global point survives; the adjective does not.

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


## T32 — Arithmetic is a second oracle, and a market shelf that never multiplies its own cells will carry an impossible one

Pass 271 was sent to re-verify the North America market figure against a second publisher. It never
needed one. The cell read **$3.68B (2026) → $32B (2030) @ 31.1% CAGR**, and:

```
3.68 × (1.311)^4 = 10.87      # what the stated CAGR produces
$32B from $3.68B in 4 years   # requires 71.7%, not 31.1%
```

The publisher, unrecorded for roughly 200 passes, turned out to be **ResourcERA**, which publishes
**$10.8B by 2030** — agreeing with the arithmetic and not with this base. The mechanism is exact and
reproducible: this base kept ResourcERA's *regional* baseline and *regional* CAGR and took its
**global** horizon (**$32.27B**). The two CAGRs — regional 31.1%, global 31.2% — differ by a tenth of a
point, which is why the row read as consistent to anyone checking the source rather than the
multiplication.

**Why this is a new defect class here.** Every defect passes 266–270 found was *cross-shelf*: a cell
disagreeing with another file, caught by `grep`. **This one is intra-cell — the row disagrees with
itself** — and no grep finds it, because nothing anywhere contradicts it.

**For the studio, and this generalises past education:** any client deck with a baseline, a CAGR and a
horizon has three numbers where two are free. **Multiply before you publish.** Run against this base's
four regional rows, EMEA, LATAM and ResourcERA's own NA all reconcile to within 1%; only the carried NA
row failed, and it failed by **2.9×**. One line of arithmetic found what two hundred passes of sourcing
discipline did not.

**The rule needs a THRESHOLD, and pass 271 calibrated it by running the check against its own new
figures** — which is the test a new rule should have to pass before it is handed to the next pass:

| figure this pass added | implied vs published | read |
|---|---|---|
| MEA AI-tutors (Grand View) $188.5M @ 32% → 2033 | **0.03%** | 🟢 reconciles |
| MEA AI-tutors (Transpire) $186.4M @ 32.13% → 2033 | **0.09%** | 🟢 reconciles |
| LATAM (Grand View) $259.6M @ 32.4% → 2030 | ~5% | 🟢 window rounding |
| APAC (Grand View) ~$2.28B @ 28.1% → $18.2B 2033 | **10%** | 🔴 **NOT noise — `p272` resolved it: a one-year window offset. Reads +0.0% from a 2026 base of $3,217.5M. See `T38`** |
| NA (Grand View) $3,113.8M @ 24.2% → $19.4B 2033 | **10%** | 🔴 **SAME defect as the APAC row (`p272`): $3,113.8M is a 2025 print, the CAGR is labelled 2026–2033. Reads −0.0% from a 2026 base of $4,253.6M. See `T38`** |
| NA (MarketsandMarkets) $951M @ 15.9% → $2.3B 2029 | **16%** | 🟡 rounding + window label |
| **NA as this base carried it** | **190%** | 🔴 **structural** |

**So a 10–16% mismatch is the normal noise of this literature** — publishers round their baselines,
label a CAGR to a window that differs from the span between the two numbers they print, and revise
base years between report vintages. ⚠️ Grand View's MEA row is the clearest case: its $280.8M (2024)
base and $1,645.9M (2030) horizon reconcile **only** if the 32.6% CAGR is applied to its labelled
2025–2030 window, which requires a **+43% single year** from 2024 to 2025 — almost certainly two report
vintages, not one growth curve.

**The threshold, therefore: flag at >25%, investigate at >50%, and treat a multiple as a structural
error rather than a disagreement.** A check that fires on every row is a check nobody runs. The carried
NA cell was out by **2.9×** — it would have cleared no threshold at all, which is the point.

> 🔴 **RETIRED IN PASS 274, and the calibration table above is wrong in two rows.** `p272` already
> refuted *"10–16% is the normal noise of this literature"* for the APAC and NA cells (`T38`).
> `p274` ran the window test on **every** cell and refuted it for the M&M rows too: **NA M&M's 16%
> closes to `+0.22%` at a six-year span and LATAM M&M's to `+0.20%`.** So the row annotated
> *"rounding + window label"* was **window label, no rounding** — and the row annotated *"window
> rounding 🟢"* (LATAM, Grand View, ~5–7%) **closes at no window at all and is a SPLICE.**
> 🟢 **The replacement rule is simpler and cheaper than a threshold:** a window test is **one
> multiplication**, so **run it on every cell and classify, rather than filtering by size** —
> `PASS` (closes as labelled) · `WINDOW_FIX` (closes at ±1 year: a year label is wrong) · `SPLICE`
> (closes at neither: two report vintages, never publish as a series).
> 🔵 **A threshold is a filter on which cells get checked; the defects on this shelf were in cells
> under the filter.** `p271`'s *">25%"* would not have fired on **any** of the five window defects
> now established. See `T42`.

## T33 — A source is not reliable per-clause, and this base was quoting half of a sentence it had thrown away

`p270` retracted *"Finland / Estonia / Netherlands as K-12 leaders"* on the grounds that it traced
**only to an aggregator citing no source**. Pass 271's EMEA leg returned the aggregator, and the
retracted claim and a figure this base quotes are **the same sentence**:

> the European AI in education market at **$2.64 billion in 2026**, forecast to grow at **31.9% CAGR**
> to **$8.0 billion by 2030**, with **Finland, Estonia, and the Netherlands leading in K-12 AI
> integration**

This base deleted the second half as unsourced and kept the first half as a market figure — and
`p270` re-published that figure as one half of its new two-publisher EMEA range, in the same pass that
performed the retraction.

**The rule:** when a source is disqualified, every datum taken from it inherits that grade. You may
keep the figure and downgrade it, or drop it, but you may not retract a source's policy claim and
promote its market claim in the same breath. The `$2.64B` end of the EMEA range now carries the grade of
the claim this base discarded; **MarketDataForecast's ~$2.11B is the end with a publisher behind it.**

**Corollary, and it is the more useful half:** the regional picture is not *one publisher per region* as
`T30` warned — it is **one publisher for the whole regional picture**. ResourcERA's signature (2026
baseline, 2030 horizon, 31–34% CAGR) fits all four carried regional rows, and they sum to **$7.55B**
against its own **$10.4B** global baseline, leaving an APAC residual of **$2.85B** that lands within
**2.5%** of Grand View's independent estimate. The decomposition is coherent, which is precisely the
problem: **a coherent single source reads exactly like corroborated multiple sources.**

## T34 — A declared gap is a claim, and it decays the same way every other carried claim does

`p270` found this base asserting a propagation it had never performed (`T29`: *"Recorded in
`intel/market.md`"* — `grep` said `0`). Pass 271 found the **inverse**: `market.md` declaring
*"MEA remains UNSIZED"* while the base carried **$0.56B (2026), 34.3% CAGR** in three other files.

**These two defects are mirror images and only one of them is catchable by `T29`'s amendment.** A false
claim of *presence* is refuted by grepping the destination. A false claim of *absence* is **confirmed by
the very silence it describes** — the check and the defect produce the same reading. This is the
**sixth cross-shelf defect in six passes**, and the third whose species was invisible to the check
written one pass earlier.

**The amendment:** before re-declaring a gap, `grep` the OTHER shelves for the thing said to be
missing. A gap declared in one file is a statement about the whole base, and no file can establish it
alone.

**For the studio:** an engagement's "we have no data on X" register needs re-verification on the same
cadence as its findings. **An institution's inventory of its own blind spots is not a different kind of
artefact from its inventory of facts** — pass 271 budgeted one sweep against seven declared gaps and
moved four of them.

## T35 — Retract the claim, not the country: `NOT_ESTABLISHED` is two verdicts wearing one label

`p270` retracted the Netherlands and recorded `NOT_ESTABLISHED`, writing that **"no national Dutch
instrument or programme was located"** — and costed the remedy without running it: *"Dutch-language
queries against the Ministerie van OCW and SLO."*

Pass 271 ran it in Dutch, and the instrument is there: **`kerndoelen digitale geletterdheid`**, with
**`AI-geletterdheid` explicitly included**, covering **primair onderwijs, onderbouw vo and (v)so**,
**legally official 2027-08-01**, fully introduced with **Inspectie** oversight in **2031**.

So the aggregator's *claim* — the Netherlands "leading in K-12 AI integration", present tense — is still
unsupported, and `p270`'s *conclusion* — nothing is there — was **false**. `NOT_ESTABLISHED` was
carrying two incompatible meanings: **"the assertion is wrong"** and **"nothing exists"**. The gap
between them was **the search language**.

**And the corrected finding is commercially better than the claim it replaces.** A present-tense
"leader" is a market already lost. **A concept curriculum that becomes binding on a named date, in the
primary band, inspected from 2031, is a procurement runway** — and it lands in exactly the band where
`Gap 367` has established, in four languages now, that permissive supply does not exist. See `P21`.

**For the studio:** when a regional claim fails verification, the next query is the same question in the
**national language**, not a retraction. This base runs its legs in English and has now found
country-level instruments in Spanish (`p270`), Chinese and Hindi (`p269`) and Dutch (`p271`) that the
English legs did not return. **An English-only absence is a statement about the query.**


## T36 — Re-publication is indistinguishable from corroboration, and this base had been checking Grand View against Grand View

`p271` established that this shelf's four regional market rows were **one vendor's decomposition** and
named the vendor **ResourcERA**, flagging the attribution as its *"one claim made on inference rather than
reading"*. `p272` ran the falsification `p271` asked for. **The attribution was half wrong and the real
structure is one level deeper.**

| row | `p271` said | `p272` established |
|---|---|---|
| **North America** `$3.68B → $10.80B @ 31.1%` | ResourcERA | 🔴 **Technotrenz.** The leg, asked directly, says it *"is not a ResourcERA figure"*. ResourcERA publishes NA as a **36% share**; `0.36 × $10.4B = $3.744B`, **1.7% from Technotrenz's number** |
| **EMEA** `$2.64B` | ResourcERA | 🔴 **Grand View, re-based.** GVR's Europe data-tree base `$1,520.1M` (year unprinted; arithmetic fixes it at **2024**) compounded **two** years at GVR's own 31.9% gives **$2,644.6M** — a **0.17%** match |
| **MEA** `$0.56B @ 34.3%` | ResourcERA | 🔴 **Grand View, re-based.** 34.3% is **exactly the CAGR implied by GVR's own MEA endpoints** `$280.8M → $1,645.9M` |
| **Global** `$32.27B @ 31.2%` | ResourcERA | 🔴 **Grand View, verbatim**, from its own press release |
| **LATAM** `$0.67B @ 33.5%` | ResourcERA | 🟡 **does NOT reconcile to Grand View** — GVR's 2026 point is **$455M**, so ResourcERA is **47% above it**. The one regional row with no established upstream |

🔴 **The consequence falls on `p271`'s headline result.** `p271` derived APAC as the residual of the
regional sum and reported it *"corroborated to 2.5% by Grand View … by a different method"*. **Grand View
is ResourcERA's source.** The residual was extracted from Grand View's decomposition and then validated
against Grand View. 🟢 **That agreement was arithmetically guaranteed** — and the tightness of it (2.5%)
is what made it persuasive.

🔵 **The general lesson, and it is the one worth taking to a client.** Four publisher names on a slide
look like four models. **Counting names counts citations, not models.** The tests that actually
discriminate cost nothing and need no page access:
1. **Look for a verbatim horizon.** `$32.27B` and `31.2%` are too specific to coincide.
2. **Try to reproduce one publisher's baseline from another's curve.** If `A(2026) = B(2024) × (1+B's CAGR)²`
   to within a fraction of a percent, A is re-basing B.
3. **Check whether an implied CAGR in one source is a labelled CAGR in another.** ResourcERA's MEA 34.3%
   is Grand View's MEA endpoints, solved.
4. **A share and a dollar figure are not two data points.** `p272`'s NA row exists because an aggregator
   multiplied someone else's percentage by someone else's base.

⚠️ **Standing consequence for this shelf: no independent corroboration of any regional
AI-in-education figure has been located. Every appearance of it so far has been re-publication.**
Say that to a client rather than presenting a consensus that does not exist.

**Confidence: high** on all four reconciliations (each is arithmetic over numbers this base can quote).
**Secondary-source grade** on every figure — `resourcera.com`, `technotrenz.com` and
`grandviewresearch.com` are all `ENOTFOUND` from this environment, re-tested this pass.

## T37 — A quantified gap decays in its quantity, and no check on this base reads the number

`intel/trends.md` stated that the `mcp-server-education` GitHub topic is *"still empty while **five**
payload-verified education MCP servers exist"*. `agents/top.md` prose says **eleven**; counting the rows
gives **12 distinct slugs**.

🔵 **The gap is TRUE.** The topic is empty. That is exactly why every existing check passes it:

| check | what it tests | verdict here |
|---|---|---|
| `T29` (`p270`) | grep the **destination** for a claimed presence | 🟢 PASS — the servers really are shelved |
| `T34` (`p271`) | grep **other shelves** before re-declaring an absence | 🟢 PASS — the absence is real |
| `T32` (`p271`) | multiply a cell and compare | 🟢 PASS — nothing to multiply |

🔴 **None of them reads the numeral in the sentence.** Passes 267 and 268 added MCP servers and
incremented the count on `agents/top.md` while `intel/trends.md` kept the number it was written with.

🟢 **Amendment: a quantity inside a gap statement is a carried datum and decays like every other one.
Re-derive it from the rows — on every shelf that states it — not from the sentence that last stated it.**
🔵 Note the direction of the decay, which matches `T31`: the stale count **understated** the base's own
holdings, i.e. it made this KB look weaker than it is. `T31` found carried claims decay toward
**overstating** their authority; a carried *count* can decay the other way, and both are errors a studio
would be briefed on.

**Confidence: high** — both numbers were counted from the files this pass.

## T38 — A publisher can mislabel its own CAGR window, and a 10% mismatch is the symptom this base had been writing off as rounding

`p271`'s costed item 2 — *"run `T32`'s arithmetic check across EVERY remaining numeric cell … it needs
zero searches, the cheapest audit available"* — was run over **19 cells**
([ledger](../evidence/arithmetic-sweep.2026-10-17-p272.tsv)).

🟢 **Headline: no cell on these shelves is impossible any more.** `p271`'s NA row was the only
`STRUCTURAL` one and it is corrected. **Two cells `FLAG`, and both are the same publisher-side defect:**

| Grand View databook | as the page LABELS the window | read one year earlier |
|---|---|---|
| **Europe** `$1,520.1M → $8,003.4M @ 31.9%` | labelled **2025–2030** → **+31.9%** 🔴 | **2024–2030** → **−0.0%** 🟢 |
| **MEA** `$280.8M → $1,645.9M @ 32.6%` | labelled **2025–2030** → **+43.0%** 🔴 | **2024–2030** → **+7.8%** 🔴 **NOT GREEN — `p274`.** `+7.8%` is not a resolution; this cell closes at **no** window and is a **SPLICE**, which `market.md` already said in prose (*"two report vintages, not one growth curve"*) while this table ticked it |
| 🆕 **GLOBAL** `$8.3B → $57.2B @ 25.9%` | printed baseline **2025** → **−8.40%** 🔴 | window **2026–2033** → **−0.07%** 🟢 — **added in `p274`: the house's signature is in its GLOBAL cell too, and that cell is this base's headline** |
| **APAC** `$2,282.9M → $18,214.1M @ 28.1%` | printed baseline **2025** → **+10.0%** 🟡 | window **2026–2033** → **+0.0%** 🟢 |
| **North America** `$3,113.8M → $19,388.3M @ 24.2%` | printed baseline **2025** → **+10.0%** 🟡 | window **2026–2033** → **−0.0%** 🟢 |

🔴 **The last two rows are the important ones, because this base had already measured them and filed them
away.** `T32`'s own calibration table carries the APAC row annotated **"base stated as 'roughly'"** and the
NA row as **"rounding + window label"**. 🟢 **Neither is rounding.** On Grand View's 2033-vintage regional
pages the printed "current" figure is a **2025** number while the CAGR is labelled **2026–2033**; compound
the printed baseline across the full span and you are a year out, every time, by about 10%.

🟢 **Correcting it is not cosmetic.** It moves APAC's 2026 point from **$2.92B to $3.22B** and NA's from
**$3.87B to $4.25B** — each a ~10% revision to a number a studio would size an engagement from, and in
both cases *upward*.

⚠️ **Standing rule: derive the baseline from the horizon and the CAGR; never trust the printed baseline's
implied year.** `base = horizon / (1 + CAGR)^(years in the LABELLED window)`.

🔵 **And `T32` gains a second duty.** `p271` set the threshold at *">25% flag, >50% investigate"* and
declared 10–16% *"the normal noise of this literature"*. **That calibration is sound as a floor but it was
being used as an explanation.** A 10% mismatch now means **test the window first**; only call it noise
once a one-year shift fails to resolve it. Four of the four cells tested this way resolved.

**Confidence: high** — pure arithmetic over published endpoints, reproducible from the ledger.

## T39 — A licence file's byte count discriminates nothing on its own, and this base measures bytes

This base's verification practice includes **blind re-measurement of licence payload byte counts**
(`p271` re-measured three and reported agreement "to the byte"). `p272` probed
`OpenOLAT/OpenOLAT` — already shelved on `verticals/solutions.md` as the one Apache-2.0 full LMS — and
measured **10,982 B**, which is **375 B SHORT** of the stock Apache-2.0 file (`apache/.github`: 11,357 B).

🔵 **A short Apache file is exactly the shape of a rider**, and this base has been burned there before:
`p252` found a **Commons Clause** rider on a row that had been blessed as MIT for four passes.

🟢 **It was not a rider.** Diffing the payload against upstream:
- **Lines 1–175 — the entire `TERMS AND CONDITIONS` — are byte-identical to stock Apache-2.0.**
- The deleted span is the **optional `APPENDIX: How to apply the Apache License to your work`**.
- What replaces it is **two attribution statements** naming the OLAT Zentrum / University of Zurich and
  frentix GmbH. **No additional restriction, no field-of-use limit, no non-commercial clause.**
- Every hit from a rider keyword grep (`except`, `does not grant`, `additional terms`) is **stock Apache
  text** — §3 patent, §5 contributions, §6 trademarks.

🟢 **Verdict: unmodified Apache-2.0, rider-cleared.** `OpenOLAT` is safe to recommend as the permissive
LMS, now at a stronger grade than the shelf carried.

🔴 **The methodological finding is about the measurement, not the repo — and `p272` measured the
distribution rather than arguing from one pair.** Eight payloads were read this pass; **six are
Apache-2.0 and they span `10,273 B` to `11,525 B`, a 1,252 B range straddling the stock 11,357 B in
BOTH directions:**

| repo | bytes | vs stock 11,357 B | terms |
|---|---|---|---|
| `tsugiproject/tsugi` | **10,273** | −1,084 | unmodified |
| `OpenOLAT/OpenOLAT` | **10,982** | −375 | unmodified *(diffed line-by-line)* |
| `autolab/Autolab` | **11,324** | −33 | unmodified |
| `numbas/Numbas` | **11,357** | **0** | unmodified |
| `yetanalytics/lrsql` | **11,357** | **0** | unmodified |
| `haxtheweb/haxcms-php` | **11,362** | +5 | unmodified |
| `HKUDS/DeepTutor` | **11,408** | +51 | unmodified |
| `adlnet/xAPI-Spec` | **11,525** | **+168** | unmodified |

🔵 **Every one is an unmodified grant, and no byte count predicts that.** The range is wider than any
plausible rider (a Commons Clause rider is ~300 B) and it is **two-sided**, so there is no threshold —
above or below — that separates modified from unmodified.
⚠️ **So a byte count can neither confirm nor refute a grant.** It is useful for exactly one thing — detecting
that a payload **changed between two passes** — and useless for deciding **what** a payload says.

🟢 **Amendment: a byte delta against stock is a TRIGGER for a terms-section diff, never a verdict.**
Diff lines 1 through `END OF TERMS AND CONDITIONS`; everything after it is boilerplate a project may
replace freely. 🔵 This also means `p271`-style agreement "to the byte" proves **stability**, not
**correctness** — two passes can agree to the byte on a payload neither of them read.

**Confidence: high** — eight payloads read first-hand this pass, one diffed against upstream line-by-line,
and the rider-keyword grep (`commons clause` / `non-commercial` / `may not sell`) returned **zero across
all eight** ([evidence](../evidence/verified-repos.2026-10-17-p272.tsv)).

## T40 — The market-size shelf cannot tell a research house from a shop that sells reports

*(new in pass 273)*

`T36` established that this base's regional market figures were aggregators re-publishing **one**
research house. The fix applied then was to trace each figure upstream until it stopped moving.
🔴 **Pass 273 shows that test has a blind spot: it checks whether a name is re-publishing someone
else's model, and never checks whether the name is a research house at all.**

The largest-CAGR row in the forecast-spread table on [`intel/market.md`](market.md) was credited to
**"Research and Markets."** ResearchAndMarkets.com does not produce forecasts — it is a **storefront that
resells them**. The model belongs to **The Business Research Company**: *AI in Education Market Report
2026*, February 2026, 250pp, with the numbers carried in a ResearchAndMarkets press release on
GlobeNewswire dated `2026-04-07`.

🟢 **Unusually, the correction is good news.** TBRC is genuinely independent of Grand View, so the count
of independent models behind this shelf goes **up** — to at least three — where `T36` had driven it down
to roughly one.

🔵 **And the comparison it unlocks is the most useful market sentence this base has produced.** Carried to
a common year on each house's own CAGR, **TBRC says $42.48B at 2030 and Grand View's own curve says
$28.64B — 1.48x apart** — while their 2026 baselines sit only 7% apart, in the *opposite* order. **The
two most independent houses available agree about today and diverge by half again about 2030.** A `T32`
sweep over all four independent rows came back **clean**, so this is a disagreement about the world, not
an arithmetic defect in anybody's model — and therefore not resolvable by picking the most careful-looking
publisher.

**What to do with it.** Quote the 2026 baseline as a **band ($8.7–11.4B, 31% wide)**, name the house —
not the storefront — beside any horizon figure, and never put a single 2030 TAM on a slide without saying
whose curve it is. **The spread is the finding; it always was, and `T40` is the reason the spread was
being under-counted.**

## T41 — A repository is not an artefact, and root-grant grading cannot see the difference

*(new in pass 273)*

This base grades licences at the repository root: `SOLE`, `OWN-GRANT-AT-ROOT`, one payload, one verdict.
🔴 **Pass 273 found a repository where that model is correct about the file and wrong about the
deliverable.**

[`MarcosNahuel/moodle-mcp`](https://github.com/MarcosNahuel/moodle-mcp) serves **MIT** at
`main/LICENSE` — 1,065 B, byte-identical to stock, zero rider keywords, measured four separate times by
this base's own instrumentation. 🟢 **That grade is right.** But the repository ships **two** artefacts
into **two different licence ecosystems**: the TypeScript MCP wrapper, which links nothing and talks REST,
and `local_italiciamcp`, a **Moodle `local_` PHP plugin** that performs every write, declares
`MOODLE_INTERNAL`, requires Moodle 4.0+, and calls `core_external\external_api`. The plugin serves **no
grant of its own** (no `LICENSE`, no `README` in its directory — both 404) and **no GPL notice on any of
the six files that serve** — while opening with Moodle's own file header, *the GPL paragraph removed*.

🟢 **The consequence is narrow, and must not be inflated into a warning.** MIT is **GPL-compatible**;
there is no conflict in the grant. What changes is the licence of the **combination**: Moodle plus the
plugin is a **GPL-3.0** work, so a *distributed* image carrying it ships as GPL-3.0 — while a **hosted**
deployment is unaffected, because GPL-3.0 has **no network clause**. 🔵 **Which means the MIT row remains
strictly cheaper than the AGPL-3.0 row this shelf used to carry as the only Moodle option.**

**The generalisable rule, and it reaches well past this repo.** 🔵 **Wherever a permissive repository
ships a plugin for a copyleft host — a Moodle `local_`/`mod_`, a WordPress plugin, a GIMP or Blender
extension — the root grant describes the source, and the host's licence describes the thing the client
actually deploys.** Ask of every permissive row: *is there a sub-directory here that only runs inside
somebody else's GPL?* This base's instrumentation does not currently ask it, which is why four correct
measurements of this repository never surfaced the question.

## T42 — A threshold is a filter on which cells get checked, and the defects were under the filter

*(new in pass 274)*

`T32` gave this base its arithmetic oracle and then gave it a **threshold**: *"flag at >25%,
investigate at >50%."* `T38` refuted that threshold for two cells. 🔴 **`p274` ran the window test on
all 28 market cells on these shelves and the threshold fails systematically: not one of the five
established window defects would have fired it.**

| cell | mismatch as labelled | would `>25%` fire? | what it actually is |
|---|---|---|---|
| Europe, Grand View | −24.17 % | 🔴 **no** *(and it is the one `p272` DID catch)* | `WINDOW_FIX` |
| APAC, Grand View | −9.12 % | 🔴 no | `WINDOW_FIX` |
| North America, Grand View | −9.07 % | 🔴 no | `WINDOW_FIX` |
| **Global, Grand View** | **−8.40 %** | 🔴 no | `WINDOW_FIX` — **the headline cell** |
| North America, M&M | −13.53 % | 🔴 no | `WINDOW_FIX` — **never swept at all** |
| LATAM, M&M | −10.30 % | 🔴 no | `WINDOW_FIX` — **swept and marked `ok`** |

🟢 **The replacement is not a better threshold. It is the removal of the threshold**, because the test
it was rationing costs one multiplication:

```
PASS        |projected/published − 1| ≤ 1 %  at the labelled span
WINDOW_FIX  closes at span ± 1 year       → a YEAR LABEL on the row is wrong
SPLICE      closes at neither             → TWO REPORT VINTAGES; never publish as a series
```

🔵 **Why a threshold was the wrong instrument in the first place.** It was calibrated on the *size* of
the error, and the errors on this shelf are not large — they are **structural and small**. A one-year
window offset on a 25–32 % CAGR produces a mismatch of roughly the CAGR divided by the span: **8–14 %**,
which sits precisely in the band `p271` defined as noise. 🔴 **The threshold was tuned to exclude the
defect's own signature.**

⚠️ **And a second-order finding worth more than the first: the two ledgers use OPPOSITE sign
conventions.** `p272` reports `published/projected − 1`; `p274` reports `projected/published − 1`. **The
same LATAM cell reads `+11.5 %` in one ledger and `−10.3 %` in the other.** A threshold compared across
two conventions was never comparing anything. **Every ledger on this base now states its convention in
its header.**

**For the studio, and this generalises past education:** a client's data-quality rule that fires on
*magnitude* will miss every defect whose mechanism bounds its own size — unit errors, off-by-one
periods, vintage splices. **Classify by mechanism, not by size, whenever the test is cheap enough to
run on everything.** Here it is one multiplication per row.

**Confidence: high.** 28 cells, pure arithmetic over published endpoints, reproducible from
[`compose/code/p274-window-sweep/window_sweep.py`](../compose/code/p274-window-sweep/window_sweep.py)
and [its ledger](../evidence/arithmetic-sweep.2026-10-17-p274.tsv).

## T43 — An amendment that is not built is not an amendment, and this base had three of them

*(new in pass 274)*

🔴 **`T37` (`p272`) wrote the rule: *"a quantity inside a gap statement is a carried datum — re-count
it from the rows, on every shelf that states it."* `p273` ranked building it seventh. Nobody ran it,
and in the two passes between the amendment and its implementation the base published three more
stale quantities.**

`p274` built it — 90 lines, no network
([`recount.py`](../compose/code/p274-quantity-recount/recount.py)) — and the first run printed
**3 STALE of 5 registered claims**:

| claim | published | measured | where |
|---|---|---|---|
| MCP server slugs on `agents/top.md` | **13** | **15** | `agents/top.md` prose (`p273`) |
| MCP server slugs on `agents/top.md` | **12** | **15** | `T21`, this file (`p272`) |
| LMS platforms reachable by MCP | **3** | **6** *(every one payload-verified)* | `T24`, this file + `agents/top.md` |
| permissive rows in the build-on tier | 23 | 23 🟢 | `agents/top.md:61` |

🔵 **And then the instrument caught `p274` itself, which is the part worth keeping.** This pass shelved
five of the missing servers; the next run read **20** against the **15** the pass had just written down,
and flagged its own prose `STALE` before it was committed. 🟢 **Both shelves now say 20 and the register
is green** — but the useful fact is that **a pass cannot hand-maintain a count it is simultaneously
changing**, which is the whole argument for deriving it.

⚠️ **Three defects in the instrument's own first draft, recorded because each is the thing it exists to
catch.** (a) It classified a slug by the **row text**, which filed `felipedias-ie/blackboard-mcp` under
**Canvas** because the row mentions Canvas in prose — fixed to read the **slug first**. (b) It accepted a
slug whose *line* mentioned MCP, which let `chamilo/chamilo-lms` and `huggingface/transformers` into a
per-platform tally — fixed to require the marker **in the slug**, which makes the count a **floor**.
(c) A word-boundary pattern silently dropped **`AStheTECH/mewcp-google-classroom`** and
**`blend-ed/tutor-contrib-openedxmcp`**, whose slugs carry `mcp` without a delimiter. 🔵 **A counting
instrument's own false negatives are invisible in its output** — the only way these surfaced was reading
the per-platform lists it printed, which is why it prints them.

🔵 **The pattern across the three stale rows is the same one `T31` named and it is not carelessness:**
each count was correct when written and each was written in a *different file* from the rows it counts.
**A number in prose and the rows it describes are two artefacts, and only one of them gets edited when
supply arrives.**

🟢 **The general rule, and it is the one `p274` would hand a client:** **a quantity in prose is a
cache.** Caches need invalidation, and the only reliable invalidation is **deriving the number at read
time from the thing it describes.** Three amendments on this base were written as instructions to
future passes (`T29`'s destination grep, `T34`'s cross-shelf grep, `T37`'s re-count) — 🔴 **and the two
that stayed instructions were both violated by the pass that came next.** `T37` is now **code**, and
`make recount` is the cheapest check on this base.

⚠️ **What this does NOT fix:** the register (`recount.py`) is hand-maintained, so a quantity nobody
registers is still uncounted. **The instrument moves the failure from "the number is stale" to "the
number is unregistered", which is a strictly better failure** — an unregistered number can be found by
grepping for digits, and a stale one cannot be found at all.

**Confidence: high** — the instrument is runnable and its output is committed.

## T44 — A licence can be refuted by a byte ceiling and a slug guess, and both read exactly like "no grant"

*(new in pass 274)*

🔴 **This base recorded, in two separate passes, that `gegok12`'s MIT claim *"died at payload"*. It did
not. `Gego-K12/gegok12` serves MIT at `main/LICENSE`, HTTP 200, `1 150` B, and `p274` read the whole
payload and diffed it.**

```
observed delta vs stock MIT  = +82 B
  SPDX HTML comment line     = +39 B   <!-- SPDX-License-Identifier: MIT -->
  four typographic quotes    =  +8 B   “Software” and “AS IS”, 3 B each in UTF-8
  longer copyright holder    = +35 B   "GegoSoft Technologies and GegoK12 Contributors"
  accounted                  = +82 B   ← exactly
normalised terms diff vs stock: differs ONLY in line-wrap column.  Rider keywords: zero.
```

🔵 **`T39` proved a byte count cannot discriminate a grant DOWNWARD** — six unmodified Apache files
spanning 1,252 B, straddling stock in both directions. 🔴 **This is the same proof UPWARD, and it
costs more**, because this base operates an **MIT ceiling** (`p1054`) and `1 150` B is `81` B above the
cluster its MIT rows sit in (`1 065`–`1 084` B). **Every byte of that excess is a thing that is not a
term**: a machine-readable identifier, four curly quotation marks, and the name of the copyright holder.

🔴 **And a second mechanism was in play, which is why the refutation looked solid.** The slug.
`gegok12/gegok12`, `GegoK12/gegok12` and `gegok12/school-erp` **all fail to resolve, and they fail
IDENTICALLY to a repository that does not exist.** Only `Gego-K12/gegok12` resolves. 🔵 **`T15`
documented this trap for Sunbird** (*"a kebab-case guess returns something indistinguishable from
absence"*) — **here it took down a licence verdict, twice, and the shelf recorded the absence as a
measurement.**

🟢 **Two rules follow, and both are cheap.**
1. **A byte delta is a trigger for a diff in both directions.** `T39` said it for short payloads;
   **a long payload is no more suspicious than a short one.** An SPDX comment, a UTF-8 quotation mark
   and a corporate copyright line will all push an unmodified grant above any ceiling.
2. 🔴 **A negative licence result must record the SLUG and REF it probed, or it is not a measurement.**
   *"Died at payload"* is a claim about a repository; **a 404 on a slug that does not exist is a claim
   about a string.** This base's own ledger format already has the columns — the two refutations did
   not use them.

**The commercial cost of this one false negative:** `Gego-K12/gegok12` is a **self-hosted school ERP
under MIT** whose fork network this base has already measured as **98 forks, near-zero fork stars, and
institution-shaped fork names across India, Indonesia and Vietnam** (`P933`: the signature of software
institutions RUN rather than developers EXTEND). 🔵 **This base's standing APAC gap is platform supply.
It refused an MIT platform row, twice, in the region where it says it has none.** ⚠️ **Corporate origin
is not established** — the copyright names GegoSoft Technologies, and a holder name is not a provenance
read — so it is shelved as **deployment-placed APAC on the base's own fork evidence**, not as
APAC-origin.

**Confidence: high.** Payload read, diffed, byte-accounted and rider-greped first-hand this pass
([ledger](../evidence/verified-repos.2026-10-17-p274.tsv)).

## T45 — The market's stated blocker is exactly this base's recommended architecture, and one row already answers it

*(new in pass 274)*

Two independent sources, two regions, one finding:

| source | what it says |
|---|---|
| **GovTech**, reporting **Bridges 2026** | **Few districts and colleges have deployed AI agents in day-to-day operations**, and leaders *"remain cautious about granting the tools access to sensitive systems and data"* |
| **EdTech Hub** (2026-03-30), Southeast Asia | Education-AI initiatives there *"remain **short-term and project-based**"* |

🔴 **Read those against `T21`/`T24`.** This base's strongest supply finding is **agents over the
systems the client already runs** — six platforms, five of them reachable under MIT. **The buyer-side
blocker named above is that exact move:** granting an agent access to the system of record. 🔵 **So the
pilots are not stalling on model quality or on licence cost. They are stalling on consent scope** —
which is what `T24` predicted from the supply side (*"the OAuth consent a pilot asks a school for is
much wider than the feature being piloted … in EMEA that is a GDPR conversation before an engineering
one"*).

🟢 **And the answer is already a row.** `bruchris/canvas-lms-mcp` (**MIT**, `1 070` B, payload-read
`p274`) ships an **opt-in FERPA mode that pseudonymises student names and contact details before tool
output reaches the model**. 🔵 **That inverts the pilot conversation**: the question stops being *"will
you let the model see your students"* and becomes *"the model never sees your students — here is the
boundary, in configuration you control."*

⚠️ **And the counter-example is in the same result set, which is why this is an architecture finding
and not a product recommendation.** `DMontgomery40/mcp-canvas-lms` carries **its own security
disclosure of a broken access control that exposed other students' personal information**. 🔵 **Same
category, same description in a search result, opposite risk posture** — the `PageLM`/`AStheTECH`
pattern (`T24`) in its **security** rather than its **licence** dimension. **Read the disclosure
history, not just the grant.**

**For the studio, as a scoping instruction:** price **data minimisation at the tool boundary** as a
first-class deliverable in every MCP engagement — pseudonymisation, per-tool scoping, an audit trail of
what the model actually read. 🟢 **It is the difference between a pilot that renews and one that is the
reason the district's AI committee says no.** See [`compose/patterns.md`](../compose/patterns.md) `P24`.

**Confidence: medium-high.** The two market sources are secondary (trade press and a research
organisation's brief); the repository rows are payload-verified first-hand.

## T46 — A path ladder cannot prove absence, and this base published its guesses as findings for three passes

🔴 **The defect species:** a `19-path × 4-ref` probe that comes back empty is **evidence about 76
paths**, not evidence about the repository. This base published it as *"no grant"*, *"licence
unverified"*, *"treat as all-rights-reserved"* — statements the probe never tested. Two rows fell to
this in a single pass, and **both failures were structurally guaranteed rather than unlucky**:

| row | carried verdict | where the grant actually was | why the ladder could not reach it |
|---|---|---|---|
| `os4ed/openSIS-Classic` | *"no licence payload served on any path tried"* | **`docs/License.txt`** — GPL-2.0, 200, **17 286 B** | the ladder tried `docs/LICENSE`. The file is **mixed case *and* `.txt` *and* under `docs/`**. An earlier cell recorded *"no payload in 17 filenames"* — **the 17 did not include it** |
| `ls1intum/Athena` | *"no grant across 76 path/ref probes over three passes"* | **12 of 14 manifests**, `license = "MIT"` | the ladder probed the **root** `pyproject.toml` — a 632-byte Poetry workspace stub with **zero occurrences of `license`** |

🔴 **And this base already knew.** [`compose/code/p275-tree-enumeration/`](../compose/code/p275-tree-enumeration/)
(**pase 93, `2026-10-04`**) states **`P275`** — *para sostener una ausencia en un árbol hay que
ENUMERARLO* — and **`P278`** — *un conteo de CERO sobre una ruta que no existe en esa ref mide la RUTA,
no el contenido* — **and ships a working blobless-clone enumerator.** 🔵 **`P278` is this trend, stated
~180 passes earlier**, and `P270` (*a negative over a path that encodes a NAME measures the name*) is
its sibling. All three were applied to **directory** trees and **never to licence paths**. 🔴 **So `T46`
is not a new method; it is the record of a principle that failed to cross domains** — `p273` extended a
ladder along the wrong axis for two passes (`ACTION YU`) while the instrument that refutes ladders sat
in `compose/code/`. **The fix was to stop guessing, with the tooling already present:**

```
git ls-remote <slug> HEAD                                    # positive control: does it resolve?
git clone --depth 1 --filter=blob:none --no-checkout <slug>   # blobless, seconds
git ls-tree -r --name-only HEAD                               # EVERY path. No guessing.
```

🔵 **Why this is a trend and not a one-off fix.** The ladder's failure mode is *silent and
self-confirming*: every added path makes the refusal feel better evidenced while leaving the
unexamined space exactly as large. **`QUEUE-UNENUMERATED=124`** — 124 negative licence verdicts on
these shelves still rest on a ladder. That number is the first honest measure of the exposure, and
`make gate-enumeration` now publishes it on every run. ⚠️ **A licence-like path is still not a grant:**
the gate excludes vendored dependencies (openSIS alone carries **20**), source files that merely carry
the word (`LicenseService.java`), and **icon assets** — `kolibri-design-system` holds **7** licence-like
paths and **all 7 are Vue icon components**.

## T47 — A monorepo declares its grant per package, so a root-only metadata probe is aimed at the one file that is silent

🔴 **Generalised from `T46`'s second limb, because it is a different mechanism wearing the same
result.** `p267`'s probe list is methodologically sound as written — it includes *"the package metadata
(`package.json`, `pyproject.toml`, `setup.py`, `build.gradle`, `composer.json`)"*. It is **aimed at the
repository root**, and that is where a workspace stub lives.

In a Poetry / npm-workspaces / Cargo-workspace layout the root manifest **declares the workspace** and
the **per-package** manifests declare the licence. Athena's twelve packages — `athena/`, `llm_core/`,
`assessment_module_manager/`, `log_viewer/` and all eight `modules/*/` — each carry `license = "MIT"`,
unanimous, **none declaring anything else**. 🔵 **The reusable units are precisely the ones that declare
it** (`module_text_llm`, `module_programming_llm`, `module_modeling_llm`), which is what makes this
commercially material rather than pedantic: the package a studio would actually depend on is the package
carrying the grant.

🟢 **Rule for this base:** before recording a metadata-channel absence on a multi-package repository,
**enumerate the manifests**, then read every one. One silent root manifest is not a silent project.
⚠️ And grade it honestly: twelve unanimous declarations is the **strongest metadata channel this base
has graded** (`kolibri-design-system` rests on one) — but it is **still metadata, not a payload**.

## T48 — A channel probed at one path licenses a false conclusion about the channel

🔴 **Nearly published this pass, and caught by re-testing instead of inheriting.**
`api.github.com/rate_limit` answers **200** — with a plausible body (`limit 15000, remaining 14998`).
`api.github.com/repos/<slug>` answers **403**, and so does `/search`. The 403 body is a **session-scope
message, not a rate limit**:

> *"GitHub access to this repository is not enabled for this session."*

🟢 **So `api.github.com` is NOT open, and `p274`'s recorded `403` was right.** The `200` on
`/rate_limit` is a **proxy-level reply** that never touches repository data. Reading it as access would
have published an open GitHub API this base does not have — and, worse, would have invited the next pass
to refresh **star counts** from it, re-introducing exactly the inflated-star defect that a sibling KB
cycle had to correct wholesale.

🔵 **The general shape:** `reachable` is not a property of a *host*, it is a property of a
**(host, path, method)** triple. This base already knows the narrower version — `p267`'s ref-sensitivity
note (`learningequality/kolibri` serves **MIT on `develop`** and **404 on `main`**) is the same lesson
one axis over. 🟢 **Operational rule: record channel state as the triple you actually probed, and probe
the path you intend to USE** — never a cheaper neighbour. **No star count was read from GitHub this
pass**; every star figure on these shelves is carried from an earlier pass and marked so.
