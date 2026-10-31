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

#### Canada (inside North America — not a separate region value)

Education is **exclusively provincial**, so there is no national policy to find —
a structural fact, not a research gap. Quebec has a 2024 guide and a **March 2025
directive suspending AI assistants**; Ontario has no ministry memorandum and only
**42.3%** of its boards have a student AI policy. The opportunity is
province-by-province policy and procurement work, and it does not generalise
across the border.

### EMEA

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

### Global

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
