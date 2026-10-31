---
industry: education
region: Global
updated: 2026-10-31
---

# Education AI — market map and opportunities

## Market size — published as a range, because the sources disagree

**USD 10.6–12.5 bn (2026), growing to USD 42.5 bn by 2030 on a ~41% CAGR.**

Every figure in that range is a market-research or vendor output. HolonIQ puts
2026 at **USD 12.3 bn**; another 2026 roundup claims the market "surged past the
**USD 12.5 bn** milestone"; earlier cycles of this KB recorded **USD 9.58–10.6
bn** from other vendors. **No independent estimate has been located in three
passes.** Quote the range to a client, never a point. The 2030 figure and the
CAGR come from the same vendor family as the 2026 figures and inherit their
uncertainty.

Two widely circulated figures are **deliberately excluded**: an "83% of
institutions plan AI teaching assistant deployments by end of 2026" attributed
to EDUCAUSE (not traceable to EDUCAUSE in any source seen across three passes),
and "AI agents will take over 80% of routine educational labour" (unsupported).

## The structural market fact

The buyable asset in education AI is not the model and not the platform — it is
the **attachment**. Institutions run copyleft platforms of record (Moodle, Open
edX, Canvas, Chamilo) that cannot legally be forked into a proprietary product,
and they run them in exactly the networked way that triggers AGPL. So the
commercial surface is the licence-clean boundary: LTI 1.3, MCP, xAPI. See
[`../repos/foundations.md`](../repos/foundations.md).

Two things changed this pass. First, a **permissive AI-native LMS now exists**
(`Selleo/mentingo`, MIT, Poland, 102★), so "substrate replacement" is for the
first time a real option in the corporate-L&D segment, if not yet at university
scale. Second, the agent layer has moved from applications to **agent skills** —
markdown instruction bundles with no runtime — which changes what "delivering an
AI tutor" even means commercially. See [`trends.md`](trends.md).

## Demand-side signal: adoption is ahead of governance everywhere

This is the most robustly evidenced finding in the KB. It now holds with primary
or near-primary evidence on all four regions, which was not true a pass ago.

| Region | Use | Governance | Source quality |
| --- | --- | --- | --- |
| LATAM (higher ed) | **87%** of institutions use AI in ≥1 area | **26%** have a formal AI strategy; **55%** have no AI budget; public universities **4%** dedicated funding | **Strongest** — UNESCO IESALC with UNU-IAS, 200 institutions, 19 countries |
| EMEA (schools) | **63%** of teachers | ~70% of institutions in Europe/North America have or are developing guidance (UNESCO) | **Strong** — two independent surveys agree exactly |
| North America (schools) | **60%** of US teachers (Gallup) | Most US public schools still lack a formal student AI policy (Child Trends / Dept of Education) | Medium — survey + joint analysis |
| APAC (higher ed) | Not measured by use rate | **7 of 39** Australian universities document operational governance structures | Medium — but now **primary**: a regulator's own 100%-response exercise plus a peer-reviewed document analysis |

## Opportunities by region

### North America

🟢 **New in the eighth pass (`p570`): two university-published assessment assets
placed from their grants** — [`ucbds-infra/ottr`](https://github.com/ucbds-infra/ottr)
(**UC Berkeley**, `cpyles@berkeley.edu`; an R autograding extension for
Otter-Grader, **BSD-3**) and
[`shmercer/writeAlizer`](https://github.com/shmercer/writeAlizer)
(**University of British Columbia**, `sterett.mercer@ubc.ca`; predicted
writing-quality scores). 🔵 **Note the second one is Canadian** — this base's
`North America` bucket is not a synonym for the United States, and a Canadian
engagement can be shown a Canadian-published asset. 🟢 **`ottr` is the
autograding half** of the assessment layer whose *gating* half (`itembank`) and
*calibration* half (`calibrate`) this base closed in the two prior passes.

**The regulatory surface is state-level and it is now large enough to be a
product.** A 2026 legislative tracker counts **134 AI-in-education bills across
31 states**, concentrated on data privacy, classroom restrictions and curriculum
integration. Four states — **Maryland, Idaho, Oklahoma and Virginia** — passed
2026 laws requiring *both* state guidance *and* mandatory district-level AI
policy adoption; Maryland's package (**SB 720**) also mandates AI coordinators.
**North Carolina's Session Law 2026-41 is the one with dates on it, and the first
is two months away:** a **state model policy due 31 December 2026**, **local
district policies due 30 June 2027**, and **teacher AI-literacy training due
30 June 2028**. That is a three-stage, statutory, date-certain pipeline in a
single state — the cleanest procurement trigger in the region and the one to lead
with, because the deadline sequence writes the engagement plan by itself. New York's
**A 9190** would restrict classroom AI to ninth grade and above, with exceptions
for diagnostics and special education. Federally, the **K-12 AI Literacy and
Readiness Act of 2026** has advanced out of House committee.

Governance lags use: **60% of US teachers** use AI tools (Gallup), while most
public schools have no formal student AI policy. A student-led coalition from all
50 states produced the **STUDENTS FIRST Act of 2026** framework with AASA in
August 2026, explicitly rejecting both an outright ban and unrestricted
adoption. Employer-side money is large: Microsoft, AWS and Caterpillar
commitments total roughly **USD 3.6 bn** in AI workforce and deployment spending.

**Opportunities.**
1. **District AI policy compliance-as-a-service.** Four states now *require*
   district-level policy and one requires named coordinators. This is a
   repeatable, deadline-driven engagement with a defined artefact. Nothing
   open-source addresses it.
2. **Canvas-attached agents.** Canvas dominates North American higher ed and has
   the strongest verified agent ecosystem anywhere — `vishalsachdev/canvas-mcp`
   (MIT, 310★) plus its agent skills. Highest-confidence technical starting point
   in the region.
3. **Accessibility remediation.** An **April 2026** deadline obliged large public
   institutions to meet updated ADA web-accessibility guidance. `canvas-mcp`
   already ships an accessibility-auditor skill — a narrow, verifiable,
   regulation-driven offer.
4. **Institutional repository RAG.** **DSpace** is **BSD-3-Clause** (see
   [`../repos/foundations.md`](../repos/foundations.md)) — the one place in the
   education stack where a client can own a proprietary derivative outright, over
   the corpus (theses, datasets, faculty output) a research agent most wants.

**Added on the fifth pass — three items, one of which changes a technical
recommendation above.**

- **California AB 1159 would bar using student data to train AI models.** This is
  a different kind of rule from the policy-and-guidance laws above: it constrains
  the *training* pipeline, not classroom use. For any engagement that touches
  Californian student records, it makes the **local-first** architecture a
  compliance feature rather than a preference — see
  [`OPTIMETA/PAIDEIA`](https://github.com/OPTIMETA/PAIDEIA) and
  `genspark-ai/genoffice` in [`../repos/foundations.md`](../repos/foundations.md).
  Status is a bill, not a law; do not quote it as enacted.
- **At least 29 states have a current or former AI-in-education task force or
  commission** (Education Commission of the States). That is the pre-legislative
  pipeline behind the 134 bills, and it is a mapped list of named bodies — i.e. a
  business-development target list, not just a statistic.
- **55% of high-school principals report their schools have not blocked or
  restricted AI tool access.** Read alongside "most schools have no formal
  student AI policy", this says the common state is **neither governed nor
  blocked** — unmanaged use. That is the honest framing for a district
  conversation, and it is a stronger opener than a compliance threat because it
  describes what the principal already knows.
- **Opportunity 3 above now has an open-source component, which it did not when
  it was written.**
  [`opendataloader-project/opendataloader-pdf`](https://github.com/opendataloader-project/opendataloader-pdf)
  (**Apache-2.0, 30,129★**) automates **PDF accessibility** and tagged-PDF/PDF-UA
  output. ADA-driven remediation of institutional document estates was previously
  scoped as audit-only via `canvas-mcp`'s auditor skill; it can now be scoped as
  **audit plus automated remediation**, which is a materially larger engagement.
  See pattern `P-570-B`.

#### Canada (inside North America — not a separate region value)

Education is **exclusively provincial**, so there is no national policy to find —
a structural fact, not a research gap. Quebec has a 2024 guide and a **March 2025
directive suspending AI assistants**; Ontario has no ministry memorandum and only
**42.3%** of its boards have a student AI policy. The opportunity is
province-by-province policy and procurement work, and it does not generalise
across the border.


**Sixth pass (`p568`) — the state-mandate wave now has a delivery component, and
an assessment component that answers its data politics.**

- **The mandates are curriculum, and curriculum is a production problem.** The
  2026 state wave is AI *literacy* instruction with dates attached — Illinois
  requires it for grades 6–12 **effective 2026-08-01**; Idaho's SB 1227 embeds it
  in general education for incoming undergraduates from **Fall 2026** and requires
  institutions to evaluate AI tools for bias; Florida's State Board approved rules
  covering K-12 **and its 28 state colleges**; Maryland's SB 720 requires
  statewide K-12 guidelines. 🟢 The deliverable those buy is **narrated, captioned
  courseware at volume**, and the sixth pass placed the engine for it:
  [`jhudsl/ari`](https://github.com/jhudsl/ari) (**MIT**, Johns Hopkins Data
  Science Lab) with [`galaxyproject/video-lectures`](https://github.com/galaxyproject/video-lectures)
  (**MIT**) as the reference pipeline. 🔴 Swap its Amazon Polly stage for
  `abogen` (**MIT**) if the district's procurement asks where the audio is
  generated — and `abogen` emits **synchronised captions**, which is an
  accessibility line item in US K-12 procurement.
- **Student-data politics is the real gate, and `itembank` is built for it.**
  California's proposed **A.B. 1159** would bar training models on student data
  unless it directly benefits the school; Idaho's law adds bias evaluation and
  privacy duties. 🟢 [`onionviolet/itembank`](https://github.com/onionviolet/itembank)
  (**MIT**) is **local-first with nothing leaving the machine but an optional
  update check**, and **no model sits in its scoring path** — short-answer items
  are never auto-graded. That is a procurement answer, not a feature.
- 🔵 **Federal position unchanged and still non-binding:** the April 2025 executive
  order sets priorities, and a **K-12 AI Literacy and Readiness Act** has been
  advanced in committee — a possible funding pathway, not law. Guidance still
  heavily outnumbers enacted statute, and the picture is state-by-state. Canada
  remains provincial (see above); Mexico is covered under LATAM.


#### 🆕 `p569` (`2026-10-31`) — one placed row, on a channel this base had not used

🟢 **[`finite-sample/guess`](https://github.com/finite-sample/guess) (MIT) is
placed North America, and the placement channel is new.** Its copyright line
names only two individuals — which under this base's own instrument places
nothing — but `master/DESCRIPTION`'s `Authors@R` field carries
**`mcor@ualberta.ca`**: the **University of Alberta**. 🔵 **For the R tier, a
CRAN manifest places a package where the grant cannot.** Registered `569-D`.

🔵 **Regional read, this pass (secondary sources, treated as directional).**
North America remains the largest regional market on every source that splits it
out, at **36–38% share** (one vendor puts 2026 at **USD 3.68 bn**); the
**USD 169 m** in FIPSE awards including responsible-AI use is the most concrete
public funding signal. 🔴 **Governance is still state-by-state, not federal** —
**134 bills across 31 states** tracked as of March 2026 — and a multi-country
engagement must reconcile Canadian federal/provincial requirements with US state
law. COPPA remains the binding constraint in the child-facing segment.

🟢 **The opportunity this pass creates here is assurance work, not discovery.**
`P-572-A` exists because certification and awarding bodies under accreditation
review must defend how item parameters were estimated and how forms were
equated. The permissive stack to do that is now complete (see
[`../repos/foundations.md`](../repos/foundations.md)) and **every component of it
is pre-adoption software** — which makes the cross-validation harness the
billable deliverable rather than a caveat.

🔴 **Declared gap, stated plainly: the `AI education North America 2026 adoption
regulation players` leg returned ZERO repository-level assets.** It returned
market-research summaries and vendor blogs only. That is the sixth consecutive
pass in which the regional search legs produced no new address in any region —
see the Global section.

### EMEA

🟢 **New in the eighth pass (`p570`): EMEA has locally published, permissively
granted assessment science — three countries, read from the grants themselves.**
This base recorded *"EMEA gained no placed row"* for three consecutive passes.
🔴 **That was an instrument gap, not a supply gap**: the rows were already in-tree
and already licence-read, and only their region column was blank. Running
`569-D`'s probe — the institutional email domain in a CRAN package's
`DESCRIPTION` → `Authors@R` field — placed them:

| Asset | Named entity in the grant | Country | Why an EMEA engagement cares |
| --- | --- | --- | --- |
| [`dexter-psychometrics/dexter`](https://github.com/dexter-psychometrics/dexter) | **Cito** (`cito.nl`) | 🇳🇱 Netherlands | 🟢 **A national testing institute publishes its own test-analysis stack.** The strongest institutional provenance available for an EMEA assessment conversation — the same class of publisher as France Université Numérique, whose `ralph`/`warren`/`potsie` this base already carries |
| [`cran/TAM`](https://github.com/cran/TAM) | **IPN Leibniz Institute for Science and Mathematics Education** (`ipn.uni-kiel.de`) | 🇩🇪 Germany | Test Analysis Modules from the institute that runs German large-scale assessment participation |
| [`yrosseel/lavaan`](https://github.com/yrosseel/lavaan) | **Ghent University** (`UGent.be`) | 🇧🇪 Belgium | The reference latent-variable / SEM implementation; ⚠️ **GPL-2+, so attach-only for a proprietary derivative** |

🔵 **The commercial sentence this changes.** Before this pass, an EMEA
assessment engagement was offered US- and APAC-origin psychometrics and told that
local supply did not exist. **It does, it is published by named public research
institutions in three member states, and `dexter` is permissive.** For a
procurement conversation under the **AI Act Annex III** evaluation-of-learning-outcomes
category — whose obligations this base prices against **2 December 2027** —
locally published, institutionally authored tooling is materially easier to
defend than imported tooling, independent of its technical merits.

🔴 **Say the limits in the same breath.** These are **R packages for
psychometric analysis**, not products and not agents: `lavaan` is **GPL-2+**
(attach-only), `TAM`'s grant lives in `DESCRIPTION` rather than a licence file
(so GitHub's sidebar shows none), and none of the three is an AI asset. **The
EMEA *agent* layer remains effectively empty** — one 24★ Apache-2.0 university
feedback system and one 13★ evaluator. What EMEA now has is a **measurement**
story, not a tutoring one.

**The compliance calendar has two tracks, and only one of them is live.**
Enforcement of the EU AI Act by the AI Office and national authorities
began **2 August 2026**. But the **Digital Omnibus postponed the high-risk
obligations**: **Annex III** systems — which include education AI that evaluates
learners, assigns them to programmes, or influences access to qualifications —
move from 2 August 2026 to **2 December 2027**, and AI embedded in regulated
products (Annex I) moves to **2 August 2028**. Secondary sources attribute this
to **Regulation (EU) 2026/1744**, in force 27 July 2026, after Council approval
on 29 June 2026. **Article 50 transparency duties were *not* delayed** and have
applied since 2 August 2026.

**A third track was missed by both earlier passes and it is the earliest one of
all: Article 4.** The AI Act's **AI-literacy obligation has applied since
2 February 2025** to every organisation that *uses* an AI system — which is every
school and every university now running AI tools, regardless of whether they
build anything. It is not risk-classified, not deferred, and already overdue
wherever nobody has done it. Of the three EU tracks, this is the only one whose
deadline is in the **past**, and it is the cheapest possible entry point to an
EMEA education engagement: AI-literacy training is a deliverable, not a
conformity programme.

**And the EU is not the only EMEA instrument track.** The **Council of Europe**
roadmap for Responsible AI in Education lists a planned **Legal Instrument on AI
in Education — "establishing rules to protect the integrity of education"** for
**2026**, following its 2025 recommendation on AI in teaching and learning. The
Council of Europe is a 46-state body wider than the EU and its instruments bind
by ratification, so a client in a non-EU European state (UK, Switzerland, Norway,
Türkiye, Western Balkans) has an education-specific track that the AI Act
analysis does not cover. *Single-source this pass; treat as a watch item with a
named instrument rather than an established obligation.*

What that means commercially: the **AI-literacy** work is already late, the
**transparency** work is due now, and the **conformity-assessment** work has
roughly fourteen more months. The Annex III
deferral was already on this KB's record from the previous pass and is
re-verified here from fresh sources; the **Article 50** half and the Regulation
(EU) 2026/1744 citation are new. Note the likely source of the confusion in the
market: enforcement *machinery* did start on 2 August 2026, so "the AI Act
applies from August 2026" is true of the institutions and false of the high-risk
duties.

Teacher adoption is the best-evidenced in the world: the **European Commission
School Education Gateway survey (April 2026, n=1,130)** and the **Sanoma Learning
European Teacher Survey 2026 (20,000+ teachers, 14 countries)** both land on
**63%**. The member-state-level source is the Commission's **Eurydice** report
*Digital education at school in Europe 2026* (2026-09-22). The UK remains
light-touch, principle-based via existing regulators, still in consultation. In
the Gulf, **Dubai's KHDA** has issued explicit responsible-AI guidance to private
schools, and the **UAE** is — with China — one of only two countries running a
**compulsory national AI curriculum**, since the 2025–26 school year.

**Opportunities.**
1. **Article 4 AI-literacy programmes — the obligation that is already
   overdue.** In force since **2 February 2025** for every organisation using AI
   systems, i.e. every school and university with a generative-AI tool in the
   building. No risk classification, no deferral, no conformity assessment:
   training, records and a policy. It is the smallest credible first engagement
   in EMEA and the only one where the client is *behind* rather than preparing.
   `Fazmin/AILearningGuide` (MIT, 242★, 51 labs, offline-first — see
   [`../agents/top.md`](../agents/top.md)) is a shippable starting artefact.
2. **Annex III conformity programmes, sold on the real date.** Learner
   assessment, programme assignment and qualification-access systems are
   high-risk; the deadline is **2 December 2027**. Selling this as a 2026
   emergency is now wrong and a client who checks will notice.
3. **Article 50 transparency, sold as the live one.** In force since 2 August
   2026 and **not** part of the deferral. Smaller, faster, and the honest "start
   here" — and the one place where a client who was told "nothing applies until
   2027" has been misadvised.
4. **The permissive-substrate play is European.** `Selleo/mentingo` (MIT,
   **Poland**) is the only AI-native LMS a client can fork and keep closed, and
   it ships SCORM and xAPI. Pair with `openfun/ralph` (MIT, France) for the LRS
   and `Cvmcosta/ltijs` (Apache-2.0) for LTI. An **entirely permissive, entirely
   EMEA-origin stack** is now assemblable — that was not true a pass ago.
5. **Gulf national-curriculum delivery.** The UAE's compulsory AI curriculum is a
   funded, centrally mandated content-and-training programme.

#### Africa (inside EMEA — not a separate region value)

Policy activity is real and was mistaken for absence in earlier passes: the **AU
Continental AI Strategy**, **Zimbabwe's National AI Strategy 2026–2030**,
**Ghana's 2025–2035 strategy** plus a **July 2026 KG–P6 AI-literacy curriculum
draft**, and strategies in Mauritius, Rwanda and Namibia. Institutional policy is
thin: a **14% / 17% / 69%-don't-know** split on whether institutions have an AI
policy.

**South Africa's status is now resolved, and the reason is a cautionary tale.**
The draft National AI Policy was gazetted on **10 April 2026** (Government Notice
3880), with comment due 10 June. Minister Solly Malatsi **withdrew it** —
announced **26 April 2026**, with the formal withdrawal notice published in a
Government Gazette dated **12 June 2026**, withdrawing Notice 3880 in its
entirety — after at least **10% of the academic references in the document's
reference list were found to be fictitious**. The **August 2024 National AI
Policy Framework** was not withdrawn but carries no statutory force. The
department was still targeting FY2026/27 to finalise a policy; no replacement
draft has been located.

That is a national AI policy withdrawn because its citations were hallucinated.
It is the strongest available argument for the verification discipline this KB
applies to itself, and it is a sellable one: **citation provenance as a
deliverable**.

**Opportunities.**
1. **Ministry curriculum pipelines, on MIT code that already exists.**
   `AI-for-Education/lesson-plan-parse-mbsse` (MIT) already parses **Sierra
   Leone's MBSSE** lesson plans into structured JSON. The same shape applies to
   Ghana's KG–P6 rollout.
2. **Offline-first and voice-first delivery.** `Kolibri` (MIT) for offline, and
   `AI-for-Education/nemoasr-android` for **on-device speech recognition** — the
   only connectivity-independent assets in this KB.
3. **African-language evaluation.** `luganda-linguistic-benchmarks` is the only
   located African-language benchmark. Building these out is the precondition for
   any credible tutor in the region, and nobody has done it.
4. **Citation-provenance tooling for government documents.** Sold directly off
   the South African withdrawal.

**Added on the fifth pass — the nearest EU date in this KB is now one month
away, and it is not the high-risk one.**

- **2 December 2026: Article 50 marking of synthetic content, for systems already
  on the market.** The transparency track — which the Digital Omnibus did *not*
  defer — carries this deadline for machine-readable marking and watermarking of
  AI-generated output on systems already placed on the market. **Every
  content-generating tool in this KB produces exactly the artefacts this covers**
  (generated decks, narrated lessons, interactive texts), so a client already
  running one in the EU has roughly a month, and the remedy is engineering, not
  policy. This is the most actionable EMEA date on this page and it is **13
  months earlier** than the Annex III date most guidance leads with.
- **The deferral itself reproduced independently this pass**: Annex III
  stand-alone high-risk **2026-08-02 → 2027-12-02** (16 months), embedded
  **2027-08-02 → 2028-08-02** (12 months), via **Regulation (EU) 2026/1744**,
  published in the Official Journal **24 July 2026**, in force **27 July 2026**,
  after Council approval **29 June 2026**. Multiple independent legal
  commentaries agree. *One* source in this pass's sweep still headlines that the
  Act "has not been formally delayed" — it is wrong, and it is the error the
  trends page already flags as circulating.
- ⚠️ **One row on the compliance table could not be corroborated this pass.** The
  "AI-generated intimate imagery / abuse material ban, December 2026" entry
  remains **single-source**. The December 2026 EU date this pass *can* corroborate
  from several sources is the Article 50 marking deadline above. These may have
  been conflated somewhere upstream. Keep the Article 50 item and treat the other
  as unverified until a second source appears.
- **OECD *Digital Education Outlook 2026*** recommends institutions move beyond
  general-purpose AI tools toward **purpose-built educational AI** — a
  supranational source for the "purpose-built beats general-purpose" trend that
  had been carried mainly on vendor commentary.
- **Gulf: Dubai's KHDA has issued explicit responsible-AI guidance to private
  schools.** The first named Gulf education regulator instrument in this KB. EMEA
  in this KB has been EU-plus-UK-plus-Africa; the Gulf private-school market is a
  distinct, well-funded buyer and this is the hook into it. Single-source;
  verify before client use.
- **Accessibility is the EMEA-specific technical wedge.**
  `opendataloader-pdf` carries an **`eaa`** topic — the **European Accessibility
  Act** — plus `pdf-ua` and tagged-PDF output. Accessibility conformance is a
  procurement gate across European public education that nothing else in this KB
  answers. See pattern `P-570-B`.


**Sixth pass (`p568`) — the strongest institutionally placed supply in this KB is
European, and it closes the region's provenance request.**

- 🟢 **A complete, all-MIT, nationally published analytics stack.**
  [`openfun/ralph`](https://github.com/openfun/ralph) (LRS) →
  [`openfun/warren`](https://github.com/openfun/warren) (xAPI dashboards) →
  [`openfun/potsie`](https://github.com/openfun/potsie) (Grafana dashboards as
  Jsonnet). All three grants read byte-for-byte this pass; all three name
  *"Copyright (c) 2020-present / 2021-present **France Université Numérique**"*.
  🟢 **The region is read off the grant, not inferred** — which is the instrument
  `567-A` asked for and the cleanest institutional placement on this base.
- 🟢 **The sellable shape: a closed analytics product on top of a copyleft
  platform.** A ministry or university on Moodle (GPL-3.0) or Chamilo (GPL-3.0)
  cannot have a closed derivative of the platform. It *can* have a white-labelled
  analytics layer attached over **xAPI**, with no platform code touched. ⚠️ Price
  it as a deployed service: `potsie`'s dashboards are MIT but **Grafana itself is
  AGPL-3.0**, and `potsie`'s last push is **2024-12-18** — stable, not active.
- 🟢 **Annex III conformity gets its first concrete artefact.** The Digital
  Omnibus moved the Annex III high-risk obligations — including **evaluation of
  learning outcomes** — to **2 December 2027**, while the **transparency duties
  have been live since 2 August 2026**. 🟢 `itembank`'s design — deterministic
  scoring, **no model in the scoring path**, short-answer always routed to a human
  rubric — is evidence that an automated marking pipeline kept a human in the
  loop. That is a conformity *deliverable*, and it is MIT. 🔴 Do not sell the
  Annex III date as 2026; a client told that has been misadvised.
- 🟡 **New in `p570`, and it is a cautionary row rather than an opportunity.**
  [`designfuchen/word-atlas`](https://github.com/designfuchen/word-atlas) —
  **3,500★ in six days**, 14 commits, Chinese/English, IELTS vocabulary with
  UK/US audio — is placed **`APAC†`** on artefact evidence (bilingual
  `CONTENT_LICENSE.md`, Chinese project name 词光, IELTS target). 🔴 **Its MIT
  grant covers the code only**; the 7,298-entry wordlist, the illustrations and
  the recordings are **CC BY 4.0**, *"to the extent of the rights the maintainers
  can grant"*, and were **generated by AI models and never reviewed entry by
  entry**. 🔵 **The APAC-relevant lesson, because exam-prep content is a large
  APAC budget line:** the fastest-growing education content repositories in this
  region are now **machine-generated corpora with hedged title and no editorial
  pass**. A studio that ships one into an IELTS product inherits an unreviewed
  corpus, an attribution obligation, and an unresolved upstream TTS rights
  question. See `570-B`.
- 🔵 **Accessibility stays the EMEA-specific technical wedge** and now has a second
  component: `abogen` (**MIT**) produces synchronised captions, beside
  `opendataloader-pdf`'s `eaa` / `pdf-ua` tagged-PDF output.


#### 🆕 `p569` (`2026-10-31`) — no new placed row, and the regulatory frame got more specific

🔴 **The EMEA leg returned no repository-level asset this pass.** EMEA's placed
institutional rows remain `p568`'s France Université Numérique stack
(`ralph` / `warren` / `potsie`, all MIT) plus
`thm-mni-ii/feedbacksystem` (Apache-2.0, Technische Hochschule Mittelhessen).
🔴 **`567-A`'s ask — place the two EMEA Moodle MCP vendors — is still open and
untouched for a third pass.**

🟢 **What did sharpen is the demand side, and it is specific enough to sell
against.** The **Council of Europe** has found a *lack of rigorous monitoring and
regulation of AI in education* and its expert group is now working on **which
aspects should be regulated** rather than whether. 🟢 **More concrete: the
Council of the EU's agenda carries an AI literacy framework for primary and
secondary education** inside the **2026–2030 European Education Area** work
programme. 🔵 Net public support for stronger AI regulation in Europe moved
**+61% (2025) → +78% (2026)**, so the direction of travel is tighter, not looser.
UK, Germany and France lead adoption on the vendor reports that split by country.

🟢 **Two distinct engagement shapes follow, and they are not the same sale:**

1. **Conformity work** — the EU AI Act's **Annex III** *evaluation of learning
   outcomes* category, obligations landing **2 December 2027**. `P-572-A` is
   built for this: calibration provenance, DIF screening across accountable
   splits, equating argument, full xAPI audit trail. 🔵 **The 2027 date is close
   enough that an awarding body starting in 2027 is already late.**
2. **AI literacy curriculum and assessment** — an EU-level framework for schools
   implies instruments to assess literacy against it. 🟢 That is `itembank` +
   `calibrate` + `ltijs` on a national curriculum, and it is a procurement that
   does not exist yet.

⚠️ **Licence note that bites hardest in EMEA:** the platforms of record here are
copyleft, and `p569` adds a sharper case —
[`swsgbl/ai-learning-os`](https://github.com/swsgbl/ai-learning-os) reads **MIT**
at its licence file while owing **AGPL-3.0 §13** on the one service a hosted
engagement would run. For a public-sector EMEA buyer with a hosting mandate,
read `NOTICE.md` before the licence file (`P-572-B`).

### APAC

**The region's evidence base improved sharply this pass and is no longer
vendor-only** — which retires the standing gap that called APAC the
weakest-evidenced region.

**Australia** has no AI-specific statute (a 2024 proposal for mandatory
"guardrails" in high-risk settings included education), but its higher-education
regulator **TEQSA** issued a June 2024 request requiring *every* provider to
submit a credible institutional action plan addressing gen-AI risk to award
integrity, and received a **100% response rate** — a regulator-collected census,
not a survey. TEQSA's toolkit *Gen AI strategies for Australian higher education:
Emerging practice* and its follow-up *Enacting assessment reform in a time of
artificial intelligence* (≈Sept 2025) came out of that analysis, the latter naming
three emergent approaches: programme-wide assessment reform, assuring learning in
every unit, or a combination. Independently, a peer-reviewed **AJET** national
document analysis of **39** universities offering ICT programmes found
operational governance structures documented in only **7 of 39** — policy
articulation is widespread, operational governance is not.

**South Korea's AI Basic Act entered into force 22 January 2026**, with
enforcement decrees still being finalised and a 2026 grace period focused on
guidance rather than penalties. Its education-specific experiment is the
cautionary one: **AI textbook adoption sat below 30% by March**, and lawmakers
subsequently **removed their official status**.

**Vietnam** adopted a comprehensive risk-based AI law — passed by the National
Assembly on **10 December 2025**, effective **1 March 2026** — and a follow-on
decision designates high-risk systems in six sectors **including education**,
reported to cover **automated assessment**: the most directly education-binding
instrument in the region. **New this pass, and it changes the sales calendar:
systems already in operation get a transition period of 12 months, extended to
18 months in health care, education and finance.** So an education system already
running when the law took effect has until approximately **1 September 2027** —
which is within three months of the EU's Annex III date of 2 December 2027. The
two most binding education-AI deadlines in the world now land in the same
quarter, and a multinational client needs one programme, not two. **China** maintains the most
comprehensive framework (mandatory registration, strict content labelling) and
runs, with the UAE, one of the world's only two compulsory national AI curricula.
**Japan** is light-touch and voluntary; **MEXT's** generative-AI pilot reached
**149 municipalities and 478 schools in FY2026** — under 2% of roughly 33,000
schools — and a MEXT-attributed figure puts elementary/junior-high use of
generative AI **for school administration at 17.2%, up 14.5 points year on year**.
**Singapore** relies on **AI Verify**, has a **Teacher AI Literacy Professional
Learning Roadmap** (one compulsory module by end 2026, two more recommended by
end 2027), and has commissioned a **survey of teacher and student AI use** under
its MOE Rapid Research Fund for H1 2026 — **results not yet published**.

**Public opinion is moving against classroom AI in three APAC markets, and it is
now measured over time.** The **Ipsos Education Monitor 2026** records rising
support for *banning* AI in schools: **Japan 21% → 29%**, **Australia 47% →
52%**, **South Korea 27% → 31%**. Australia and New Zealand sit highest in the
region; the Asian markets surveyed are lower but trending the same way. This is
the first attitudinal **time series** in this KB, and it is a risk datum rather
than an opportunity: in Australia, **a majority now supports a ban** in the same
market where TEQSA has made institutional AI plans mandatory. A proposal that
assumes public permission is reading the regulator and ignoring the electorate.
Pair it with the Korean textbook reversal below — the two together are the
strongest available argument for staging a rollout behind teacher capability.

**Opportunities.**
1. **Award-integrity and assessment-reform programmes, Australia first.** TEQSA
   has already made the plan mandatory and the gap measurable: 7 of 39 have
   operational governance. The remaining 32 are a named pipeline.
2. **Vietnam high-risk assessment compliance.** Automated assessment in a
   designated high-risk sector, under a law already in force. First-mover window.
3. **Teacher AI-literacy delivery at national scale.** Singapore has mandated it
   with dates; Korea's grace period runs through 2026. This is training
   delivery, not software, and it is funded.
4. **Agent sourcing.** The two largest education agents in the world are APAC and
   permissive — **DeepTutor** (Apache-2.0, 52,167★, HKU) and **OpenMAIC** (MIT,
   41,981★, Tsinghua). An engagement anywhere that sources from the shelf is
   sourcing from APAC.
5. **Avoid the Korean textbook failure mode.** Mandated content without teacher
   buy-in reached <30% adoption and then lost its official status. Any
   national-rollout proposal should carry an adoption-risk section citing it.

**Added on the fifth pass — the two Asian regimes are now specific enough to
scope work against, and one of them regulates RAG directly.**

- **Vietnam: Decision 33 is the instrument, and it names three education
  systems.** The AI Law (No. 134/2025/QH15) took effect **1 March 2026**;
  **Decision 33**, effective **15 August 2026**, publishes the high-risk list —
  **46 systems across six sectors**, education among them with **three** entries:
  (1) AI that **automatically tests, evaluates or ranks learners**; (2) AI that
  **monitors and analyses learner behaviour**; (3) **self-study tools that
  generate educational content from uncontrolled data sources.** **The third is
  the one to read twice.** Every retrieval-augmented tutor in this KB generates
  content from sources it does not curate — that is the architecture, not a
  misuse of it. A RAG tutor sold into Vietnam is **presumptively high-risk**
  unless the corpus is controlled, which turns "curated corpus" from a quality
  choice into a regulatory one. Several sources note that listed systems are
  high-risk chiefly where AI output is the **sole** basis for a decision with no
  human in the loop, so human-in-the-loop review is also a classification lever.
  Existing education systems have a transition to about **1 September 2027**.
- **Korea: correction to this KB's record — the Enforcement Decree is not
  pending.** The compliance table has carried "enforcement decrees pending". The
  **Decree entered into force on 22 January 2026 alongside the Act**. What is
  deferred is *enforcement*, specifically: **fact-finding and fines are suspended
  for at least one year from 22 January 2026**, except in extreme cases such as
  loss of life. Education appears as a named **high-impact** area — the sources
  specify **evaluation of students in early childhood, elementary and secondary
  education** — carrying risk-management, user-protection and human-oversight
  duties. **So the obligations are live now and the penalties are not**, which is
  a far better sales position than "pending decrees": a client can be brought into
  conformance inside the grace window.
- **Singapore procures frameworks, not rules.** **AI Verify** is a testing and
  accountability toolkit rather than a statute — meaning the deliverable in
  Singapore is **evidence of testing**, which pairs directly with the evaluation
  layer in [`../repos/foundations.md`](../repos/foundations.md) and with
  `terracotta`'s randomised-trial apparatus.
- **China's regime is the most assertive** — mandatory registration, content
  labelling obligations, penalties. Note the awkward commercial fact this creates:
  the two largest permissive education agents in this KB (**DeepTutor**, HKU;
  **OpenMAIC**, Tsinghua) and the strongest OCR (**PaddleOCR**, Baidu) are all
  Chinese-origin, so **an engagement anywhere is likely sourcing from the most
  heavily regulated AI jurisdiction in the region.** The licences are clean; the
  supply-chain question a client's risk committee will ask is not about licences.
- **Japan remains light-touch and voluntary** — no education-specific instrument
  located.
- **Market shape:** market-research sources put **APAC as the fastest-growing
  region** for AI in education, with China, India and Japan dominating spend, and
  name Google, Microsoft, IBM, Pearson and Byju's as key players. Vendor-sourced;
  quote as direction, not as figures.


**Sixth pass (`p568`) — the live permissive psychometrics layer is Chinese and
institutional; no new placed address, and the reason is stated.**

- 🟢 **[`bigdata-ustc/EduCDM`](https://github.com/bigdata-ustc/EduCDM)
  (**Apache-2.0**, 203★) is the one live, permissive, education-specific
  psychometrics asset on this base**, from a named university group (USTC). ⚠️ Be
  precise in a pitch: it does **cognitive diagnosis** — inferring what a learner
  knows from their responses — and **not item calibration**. The calibration half
  of that layer is genuinely missing everywhere (see
  [`../repos/foundations.md`](../repos/foundations.md)).
- 🔴 **No new APAC-placed address this pass.**
  [`sudazc/open-question-bank`](https://github.com/sudazc/open-question-bank) is
  Chinese-language (`组卷`, test assembly) but its grant names an individual
  handle, and **this base does not place an artefact on its language.** Recorded
  `Global`. The gap is a provenance gap, not a supply gap.
- 🟢 **Data residency is the regional wedge, and the sixth pass added the
  component for it.** Vietnam's AI law obliges identified systems by
  **1 March 2027**, with a grace position for education systems already operating
  before **15 August 2026**; Taiwan's **AI Basic Act** took effect
  **14 January 2026**; Indonesia's **GR 71** imposes data-residency duties that
  bear directly on EdTech hosting. 🟢
  [`Changochen/slide-to-video`](https://github.com/Changochen/slide-to-video)
  (**MIT**) is the only lecture-video row that runs with **no cloud TTS at all** —
  optional local voice cloning — which pairs with `PAIDEIA` and `WordLink`'s
  in-browser model as a fully local courseware-and-tutor story.
- 🔵 **A cautionary adoption datum worth carrying:** South Korea's AI digital
  textbook initiative was **walked back to optional "educational material" status
  within about a year** after objections over screen time and data. 🔴 It is the
  clearest available evidence that a national mandate is not a durable demand
  signal, and it should temper any roadmap built on one. Reported via secondary
  sources; treat as direction. Regional CAGR figures from market-research vendors
  remain unverified and should be quoted as direction only.


#### 🆕 `p570` (`2026-10-31`) — a Brazilian national-statistics asset, and the honest grade of the evidence

🟡 **[`SidneyBissoli/educabR`](https://github.com/SidneyBissoli/educabR) is
placed `LATAM†` — artefact grade, not grant grade.** An R package to *"Download
and Process Brazilian Education Data from **INEP**"* — INEP being Brazil's
national institute for education statistics and assessment, the body that runs
**ENEM** and the **Censo Escolar**. README is Portuguese; `R-CMD-check` and
coverage badges are live. 🔴 **The grant places nothing** — `DESCRIPTION`'s
`Authors@R` carries a gmail address, so unlike this pass's three EMEA rows the
placement rests on what the package *does*, not on who signed it. Marked `†` per
`569-E`.

🔵 **Why it is worth a row anyway.** Every LATAM engagement in this base's
history has needed a *data* starting point for a ministry or *secretaría*
conversation, and this is a maintained, permissively granted client for the
national education dataset of the region's largest education system. 🔵 It pairs
with `JaxisReal/Moodle-Reporte-Limpio` below (Moodle completion reports,
Spanish): **one row reads the national dataset, the other reads the institution's
own LMS.**

🔴 **And the regional ledger stays honest: LATAM gained no new *agent* and no new
*grant-placed* row this pass.** The region's only placed education agent,
`dio-agent` (2,750★), is still **unlicensed**, so the local-supply story and the
build-on-it story remain about different repositories — the structural finding
this base has now carried for four passes.

#### 🆕 `p569` (`2026-10-31`) — a corporate holder named in a grant, and a second row placed on artefact evidence only

🟢 **[`verycoolapps/Statistica`](https://github.com/verycoolapps/Statistica) is
the cleanest APAC placement this base has recorded on the grant itself.** Its
`main/LICENSE` (MIT, 1,096 B) reads *"Copyright (c) 2026 VeryCoolApps — **PT.
Agra Karya Digital**"* — `PT.` is the Indonesian form for a limited company, so
the holder is a **named corporate entity in a named jurisdiction**. 🔵 This base's
placement instrument was built for *institutional* holders (universities,
national operators); **a company name works identically and the rule should say
so.** ⚠️ Substance is thin — an offline statistics desktop app, bilingual ID/EN,
**2 commits** — so it is placed, not shelved as a foundation.

🟡 **[`swsgbl/ai-learning-os`](https://github.com/swsgbl/ai-learning-os) is
recorded APAC on a weaker footing, deliberately marked as such.** Its grant names
*"AI Learning OS contributors"* — not an institution — so it is placed on
**artefact evidence**: a **HarmonyOS / 深开鸿** client target, a `ChinaTextbook`
catalogue integration, Chinese-language documentation throughout. 🔴 **Two grades
of evidence, labelled, not blended** — `569-E`.

🔵 **Regional read (secondary, directional).** APAC is the **fastest-growing**
region for AI in education on the vendor reports that split it out
(**USD 591.6 m in 2024 → ~USD 1.85 bn by 2029**, ~20.9% CAGR). 🔴 **The
governance picture is the opposite of EMEA's: Forrester expects no APAC-wide
legislative framework** — rules stay fragmented per country — and the 2026 theme
across regional analysts is **sovereignty and "sovereign-by-design" execution**.
IDC places most APAC countries at mid-stage AI maturity with Singapore leading.

🟢 **That makes the self-hosted, measurement-first shape unusually well matched
to this region.** `ai-learning-os` is server-authoritative, keeps **ASR/TTS
local so voice audio never leaves the machine**, and holds LLM keys in a
server-side encrypted BYOK store. 🔵 **Sovereignty is the APAC buying criterion
and local inference is the answer to it** — which is also why the sub-floor tier
matters here specifically: `4 of 5` of this pass's new tutor-class agents run
locally or BYOK.

🔴 **Declared gap: the APAC leg returned no education-specific regulation for
China, Korea or Australia and no 2026 school adoption rate.** The only
education-specific player list any source offered was dated 2019. The APAC
governance rows on this page remain the Australian regulator exercise
(**7 of 39** universities with documented operational governance).

### LATAM

**The best-evidenced adoption-governance gap in the world, from the most
authoritative source in the KB.** The **UNESCO IESALC** study (with UNU-IAS),
launched at **Digital Learning Week 2026** at UNESCO HQ in Paris, surveyed **200
higher-education institutions across 19 Latin American and Caribbean countries**:
**87% already use AI in at least one area of activity, and only 26% have a formal
AI strategy.** **55% of universities have no specific AI budget**, and public
universities have the lowest rate of dedicated AI funding at **4%**. A UNU working
paper (1 September 2026, Arianna Valentini) maps adoption across five dimensions:
teaching and learning, research, community engagement, administration, and
governance.

School-level data is national and primary. **Cetic.br (2026)**: **53% of Brazilian
school administrators use AI, while only 22% report that their school has
guidelines**. UNESCO reports **more than 50% of teachers in Chile and Brazil**
already use these tools while **fewer than 10% of institutions region-wide have
formal guidelines**. **Ceibal (Uruguay)** reports **75% of public-school teachers**
using them — the highest national figure located anywhere.

**Regulation: volume without binding force.** A 2026 Universidad de los Andes
study identified **716 AI-related regulatory instruments, rules and legislative
proposals across 23 countries and territories, more than 80% initiated since
2023**. Education-specific binding law is almost nonexistent: **Peru's Ley 31814
plus DS 115-2025-PCM** remains the only binding instrument naming education;
Chile's MINEDUC *PotencIA el aprendizaje* is guidance.

**Brazil's PL 2338/2023 is not law, and its status is now pinned.** It passed the
**Senate in December 2024** and sits in the **Câmara dos Deputados** special
committee **awaiting the rapporteur's opinion** — Deputy **Aguinaldo Ribeiro
(PP-PB)**. Roughly **37 proposals are attached** to it; the last recorded
movements (20 July – 2 September 2026) are attachments including **PL 3060/2026**,
with nothing new recorded as of early October. On **24 August 2026** the
rapporteur stated the vote would wait until **after the October 2026 elections**.
It still needs a Câmara plenary vote, and any textual change sends it back to the
Senate. *Evidentiary caveat: the official Câmara record could not be read from
this session — see Declared gaps.*

Institutional players are unusually well defined: **UNESCO IESALC** (study),
**UNESCO's Observatory on AI in Education for Latin America and the Caribbean**
(launched **14 April 2026, Santiago, Chile**), **Cetic.br** and **Ceibal**
(national data), **CENIA** (Chile) and **Tecnológico de Monterrey** (UNESCO
partnerships), and the **Digital Education Council**, which publishes an *AI in
Higher Education LATAM Survey 2026* in English and Spanish.

**Opportunities.**
1. **AI strategy and governance for universities — the single clearest
   opportunity in this KB.** 87% use it; 26% have a strategy. The gap is 61
   points, measured by UNESCO, in a region where Globant already has the deepest
   presence. It is advisory work, not platform work, and the 55%-no-budget figure
   says to price it accordingly.
2. **Brazilian public-sector school management.** `portabilis/i-educar` (GPL-2.0)
   runs municipal *Secretarias de Educação* nationwide. Copyleft, so attach via
   LTI/MCP rather than fork — and Cetic.br's 53%/22% split is the business case
   for the governance layer on top.
3. **A compliance window that is still open.** With PL 2338 stalled past the
   October elections and no education-specific instrument outside Peru, clients
   can build governance before being compelled to. That is a *preparedness* sale,
   not a *compliance* sale, and it should be positioned honestly as such.
4. **Spanish- and Portuguese-language assets.** `Chamilo` has a strong LATAM
   install base; `ltijs` has a Brazilian maintainer; **`dio-agent`** (2,750★,
   Portuguese) proves the regional demand for study-mentor agents — **but it is
   unlicensed** (see [`../agents/top.md`](../agents/top.md)), so it is evidence,
   not a component.

**Added on the fifth pass — two new sources, and the budget finding is the one
to sell on.**

- **An October 2026 regional AI index across 20 LATAM economies gives the
  governance gap a sharper edge than the institutional data did.** **85%** of
  countries have a national AI strategy in place or under development and **75%**
  have formally designated a lead institution — but **only Brazil and Colombia
  explicitly allocate budget** within their national instruments. Top tier:
  **Brazil, Chile and Uruguay**. More than half of countries have incorporated AI
  into school curricula. **The pattern mirrors the institutional finding one level
  up:** strategy without funding at country level, exactly as UNESCO IESALC found
  87% use against 26% strategy and 55% with no AI budget at institution level.
  **Two independent levels of the same system show the same defect** — the
  artefact exists, the money does not — which is a far stronger basis for a
  funding-and-roadmap engagement than either finding alone.
- **The Digital Education Council's LATAM 2026 survey corroborates adoption at
  the individual level: 92% of students and 79% of faculty actively engaging with
  AI**, from **over 30,000 responses across 29 higher-education institutions**,
  produced with **Tecnológico de Monterrey's Institute for the Future of
  Education**. Note what this adds rather than repeats: IESALC measured
  *institutions*; this measures *people inside them*, and the two agree. Tec de
  Monterrey's involvement also makes it a citeable regional partner rather than
  an external observer.
- **UNESCO IESALC's causal reading should be quoted directly in pitches:**
  adoption is being driven by **faculty, researchers and students**, not by
  institutional policy or strategic guidance. The buyer is therefore being asked
  to catch up with their own staff — which is a different conversation from
  being asked to innovate, and an easier one to fund.
- ⚠️ **A widening-inequality signal, October 2026:** regional reporting describes
  Latin America facing AI inequality as **compute and adoption gaps widen**. This
  cuts against the offline/low-resource optimism elsewhere in this KB and argues
  for the **offline-first and local-inference** assets (`Kolibri`, `tesseract`,
  `PAIDEIA`, `WordLink`'s in-browser model) rather than hosted-model designs in
  the region's less-resourced systems.


**Sixth pass (`p568`) — 🔴 zero new addresses, and the demand-side case is
stronger than the supply-side one.**

- 🔴 **Supply: nothing new this pass.** Four regional WebSearch legs returned no
  address new to this base. The only LATAM-placed education agent on this base,
  [`digitalinnovationone/dio-agent`](https://github.com/digitalinnovationone/dio-agent)
  (2,750★), is still **ungranted** — verified by three methods — and the
  `measured-unusable` register still holds `ceanjonnube-negra/docente-ia`
  (Mexico, SEP-scoped, **no grant**). 🔴 **The region's local-supply story and its
  build-on-it story remain about different repositories**, and that must not be
  blurred in a market slide.
- 🟢 **Demand: the governance gap is the engagement, and it is now measured by a
  credible source.** UNESCO launched its **Observatory on AI in Education for
  Latin America and the Caribbean** in **Santiago on 14 April 2026**, reporting
  that in countries such as Chile and Brazil **more than 50% of teachers already
  use these tools while fewer than 10% of institutions have formal guidelines**.
  🟢 That asymmetry — adoption without policy — is precisely what a studio is paid
  to close, and it is an advisory-plus-platform engagement rather than a licence
  sale.
- 🟢 **The assets that answer it are already on this base, and two are new this
  pass.** An auditable assessment-and-telemetry trail a *secretaria* can show a
  regulator: `itembank` (**MIT**, local-first, no model in the scoring path) for
  defensible marking, plus `ralph` (**MIT**) for an xAPI record of what was
  actually delivered, attached to `i-educar` (GPL-2.0) — the reference Brazilian
  municipal platform — over a standard rather than a fork.
- 🔵 **Funding and market shape:** Google.org committed **$4.6M** with the
  Raspberry Pi Foundation to scale *Experience AI* across nine countries
  (Argentina, Brazil, Chile, Colombia, Dominican Republic, El Salvador, Mexico,
  Peru, Uruguay), targeting **1.25M students by 2028**; HolonIQ's **2026 LATAM
  EdTech 100** has **Brazil at roughly half the cohort**. 🔵 Regulation: Brazil's
  **PL 2338/2023** remains the anchor framework with an algorithmic-impact-assessment
  duty for high-risk deployers and the **ANPD** coordinating the national AI
  governance system; Mexico's bill carries a digital-rights chapter and no
  explicit prohibition tier. 🔴 Bill status moves — confirm against the Senado and
  the Mexican Congress before a client commitment.
- 🔵 **Counterweight already on this page:** compute and adoption gaps are
  *widening* in the region, which argues for the offline-first assets
  (`Kolibri`, `tesseract`, `PAIDEIA`, `WordLink`, and now
  `Changochen/slide-to-video`'s local voice cloning) over hosted-model designs in
  less-resourced systems.


#### 🆕 `p569` (`2026-10-31`) — two rows found, one unshelvable, and the region's structural disadvantage now has a measurement

🟢 **[`JaxisReal/Moodle-Reporte-Limpio`](https://github.com/JaxisReal/Moodle-Reporte-Limpio)**
— **MIT** (`main/LICENSE`, 1,086 B, *"Copyright (c) 2026 Jerry Anderson Carril
Chávez"*), 9 commits, 2 authors. A Moodle plugin for generating, processing and
visualising **course-completion reports**, Spanish-language. 🔵 The holder is an
individual, so **by grant it is `Global`; by artefact it is LATAM.** Useful as a
concrete starting point for a *secretaría* that already runs Moodle and wants
completion reporting before it wants AI.

🔴 **[`smatilio/ic-tri-simulacao`](https://github.com/smatilio/ic-tri-simulacao)
cannot be shelved, and this is the most actionable gap on the page.** It is a
Brazilian **TRI** (item response theory) simulation study — *"2PL longitudinal
with a human-machine effect, estimated with `mirt` and Stan"*, R, 16 commits,
pushed `2026-10-30`. 🔴 **It carries NO licence at 5 filenames × 2 branches**, so
it is unusable regardless of quality. 🟢 **The remedy is a message, not an
engagement:** this is a live academic repository whose author has very likely not
considered the question, and a polite issue asking for a licence is the
single highest-yield action available on LATAM supply this pass. 🔵 Registered as
part of `569-F`.

🟢 **And the structural point, now measured rather than asserted.** This base has
recorded thin LATAM supply for many passes. 🔴 **Part of that thinness is an
artefact of how it searched.** A star-sorted sweep systematically under-reports
projects that are non-English, single-author and unlaunched — which describes
most LATAM and APAC education supply. 🟢 **`topic:ai-tutor` holds `793` of its
`816` results below 50 stars, and three of this pass's four high-commit finds
are non-English-first.** 🔵 **The correction is `P-572-C`, and LATAM is where it
pays most.**

🔵 **Regional read (secondary, but the primary source here is strong).** The
**UNESCO IESALC / UNU-IAS** working paper (**1 September 2026**) maps AI use
across LAC universities on five dimensions — teaching, research, community
engagement, administration, governance — and remains the best-evidenced regional
item in this KB (the 87% / 26% / 55% figures above). **ECLAC/CEPAL's ILIA index**
puts **Chile, Brazil and Mexico** ahead regionally with persistent gaps in data,
training and regulation; Baker McKenzie confirms countries sit at **very
different regulatory stages**, so a multi-country LATAM engagement cannot assume
one compliance posture. Commercial actors named: **Platzi**, and a Huawei
education alliance launched 2025. The **World Bank's WDR 2026** is on AI.

🔴 **Declared gap: the LATAM leg returned no K-12 AI policy for any individual
country and no repository-level asset.** Both country-level K-12 policy (Brazil,
Mexico) and LATAM repository supply remain unmeasured by search; the two rows
above came from the `stars:<50` band, not from the regional leg.

### Global

- 🔴 **Read `Global` on this page as "unplaced", and know that `p570` found a
  structural reason it is over-counted.** Region here is recovered from the
  copyright line in a licence file. 🔴 **Apache-2.0 has no copyright line** — its
  template never asks for one — so **four of four** Apache rows added this pass
  carry no holder and are unplaceable *by construction*, whichever country wrote
  them. 🔵 **The consequence for anyone reading the regional counts on this page
  as a market measurement: `Global` is inflated by whichever licence family a
  layer happens to prefer, and the rubric/evaluation layer prefers Apache-2.0.**
  Five of its seven rows are `Global` for that reason alone. Registered as
  `570-C`.
- 🔴 **And the five-value vocabulary has no Africa value, so EMEA is a composite
  bucket.** `hanskepper/SMART-GRADE` is a **Cameroonian** school gradebook and is
  recorded `EMEA†` because there is nowhere else to put it. 🔵 **Any EMEA figure
  quoted off this page should state whether it includes African rows**, or a
  German research institute and an African school-IT project are being counted as
  one market. The vocabulary is closed on purpose and should stay closed — the
  fix is the `†` marker and the country in prose, not a sixth value. Registered
  as `570-E`.
- **The attachment layer is the product**, everywhere, for licence reasons that
  do not vary by region: LTI 1.3 (`ltijs`, Apache-2.0), MCP (MIT servers), xAPI →
  LRS (`xAPI-Spec` Apache-2.0, `ralph` MIT).
- **Quality gating is an unserved global need.** `learning-commons-org/evaluators`
  (rubrics, licence-unresolved) and `pedagogy-benchmark` (MIT) are the only
  verified evaluation assets in existence for education AI, and **neither is a
  runtime monitor**. Every region's governance gap is, concretely, this missing
  capability.
- **Agent skills travel across borders and licences do not.** The skill cohort is
  overwhelmingly APAC-origin and mostly MIT, but the largest member is **CC BY-SA
  4.0** (share-alike). Licence-screen every skill bundle before it enters a
  client deliverable.


#### 🆕 `p569` (`2026-10-31`) — the discovery channel, measured across all five regions at once

🔴 **The eight mandated search legs — four global, four regional — returned `0`
addresses new to this base. That is the SIXTH consecutive pass with that
result.** Every candidate they named (`OPTIMETA/PAIDEIA`,
`GarethManning/education-agent-skills`, `rohitg00/ai-engineering-from-scratch`,
Sakai, OpenEduCat, `irtorch`, OpenSIS, Fedena) was checked against the tree and
**all eight were already shelved.**

🟢 **One sweep of `stars:<50` across three topic axes returned `13`.**

| channel | legs / rows | new addresses | grants read |
| --- | --: | --: | --: |
| 🔴 `WebSearch`, the mandated queries | 8 legs | 🔴 **0** | — |
| 🟢 `github.com/search`, `stars:<50`, sorted by recency | 3 axes × 10 rows | 🟢 **13** | 🟢 **11 of 13** |

🔵 **What the regional legs ARE good for, since the nil result is now settled:**
policy, calendar and funding intelligence — the Council of Europe's regulatory
work, the EU's AI literacy framework, FIPSE's USD 169 m, ILIA's country ranking,
UNESCO IESALC's survey. 🟢 **Every regional paragraph above is built from them.**
🔴 **What they do not do is find code**, in any region, and six passes is enough
evidence to stop spending the discovery budget there. 🟢 **Reallocated this pass;
`P-572-C` is the replacement method and it is written to be run on every other
industry on this harness.**

## Declared gaps — what was searched and not found

### Closed this pass

- ~~**APAC rests on vendor market research with no primary survey.**~~ **Closed.**
  TEQSA's **100%-response** institutional census, the peer-reviewed **AJET**
  39-university document analysis (7/39), **MEXT's** pilot counts (149
  municipalities, 478 schools, <2%) and administrative-use figure (17.2%, +14.5
  pp), and Singapore's **MOE Rapid Research Fund** commission are all primary or
  near-primary. *What made the difference:* searching the **regulator and
  ministry** (TEQSA, MEXT, MOE) rather than the region — the same lesson that
  closed the EMEA gap by searching "European Commission" instead of "EMEA".
- ~~**South Africa's National AI Policy status is unresolved.**~~ **Closed.**
  Gazetted 10 April 2026 (Notice 3880), withdrawal announced 26 April 2026,
  formal Gazette withdrawal 12 June 2026, cause: ≥10% fabricated academic
  references. The 2024 Framework stands without statutory force.
- ~~**Brazil's PL 2338 status is contradicted across three sources.**~~ **Closed
  as far as this session can reach**, and the three sources no longer contradict:
  passed Senate Dec 2024, in Câmara special committee awaiting Deputy Aguinaldo
  Ribeiro's opinion, ~37 proposals attached, last movement 2 September 2026, vote
  deferred past the October 2026 elections, **not law**. See the caveat below.

### Still open

- **The official Câmara dos Deputados record could not be read from this
  session.** `www.camara.leg.br` does not resolve here — it is outside the
  session's allowed network domains. The PL 2338 account above rests on
  consultancy and law-firm trackers that **agree on every material point**, which
  is why it is recorded as closed-with-caveat rather than closed. A session with
  that domain allowed should confirm the *ficha de tramitação* directly.
- **Market-size figures remain entirely vendor outputs.** Three passes, no
  independent estimate. The USD 10.6–12.5 bn range stands as a range, and the
  2030/CAGR figures inherit the same provenance.
- **EU AI Act primary text cannot be read from this session, and that is now
  established rather than deferred.** The third pass named reading the Official
  Journal "the highest-value single action available to the next pass". It was
  attempted this pass and it is **not achievable from here**:
  `eur-lex.europa.eu` does **not resolve**, and neither does the
  `artificialintelligenceact.eu` mirror — the same failure class as
  `www.camara.leg.br`. This is a **network-policy constraint, not a research
  gap**, and it should stop being queued as an action item: it is a request to
  allow the domain in the session's network settings. Everything this page says
  about **Regulation (EU) 2026/1744**, the 2 December 2027 Annex III date, the
  2 August 2028 embedded-product date, the undeferred Article 50 duties and the
  Article 4 literacy obligation remains **multi-source secondary**, consistent
  across independent legal commentaries, and unverified against the OJ.
- **South Africa has no replacement draft** and no announced date beyond
  FY2026/27.
- **Singapore's MOE teacher/student AI survey is commissioned but unpublished.**
  Dated watch item: it will be the region's first government teacher-use survey.
- **African supply side is mapped but tiny.** `AI-for-Education` (MIT, LMIC-focused)
  closes the "nothing exists" gap, but every repo is 0–13★ and the
  organisation's own **location is not stated**. African-*domiciled* publishers
  remain unmapped.
- **A continental "USD 3 bn" African AI/STEM rollout figure is advocacy, not
  official** — still excluded from the numbers above.
- **LATAM returned nothing new this pass, and that is recorded rather than left
  silent.** The prescribed regional search
  (`AI education LATAM Latin America 2026 adoption regulation players`) returned
  the UNESCO IESALC study, the Observatory launch, Ceibal, Cetic.br, the
  Universidad de los Andes instrument count and Tecnológico de Monterrey —
  **every one of which was already on this page from the previous pass**. No new
  institution, instrument or figure. For the region where Globant has the deepest
  presence, the evidence base is now **stable rather than growing**, which is a
  different thing from under-researched: the 87/26 gap has been the headline for
  three passes and nothing has moved it.
- **The Council of Europe education instrument is single-source.** Named,
  dated 2026, and carried as a watch item, not an obligation.
- **The Ipsos Education Monitor 2026 ban-support figures are single-source** and
  the earlier comparison year is not stated in what was read, so the shifts are
  directionally reliable and the baselines are not pinned.
- **No independent audit of the UNESCO IESALC figures.** They are the most
  authoritative numbers on this page and they are single-source. The 26%
  strategy figure in particular was reported as "about a quarter" by one relay
  and **26%** by another; 26% is used here.
