---
industry: education
region: Global
updated: 2026-10-31
---

# Education AI — market map and opportunities

Research date 2026-10-31. Sources are named inline. Where sources conflict, the
conflict is published rather than resolved by picking a favourite.

## Market size — published as a range, because the sources disagree

| Figure | Year | Source |
| --- | --- | --- |
| USD 7.52 bn | 2025 | ResearchAndMarkets, via Yahoo Finance |
| USD 8.3 bn | 2025 | secondary market summary (unattributed) |
| USD 10.6 bn | 2026 | ResearchAndMarkets, via Yahoo Finance |
| USD 12.3 bn | 2026 | X-Pilot, attributed to HolonIQ |
| USD 42.48 bn | 2030 | ResearchAndMarkets (total revenue "set to quadruple" 2026–2030) |

**The 2026 figure spans USD 10.6–12.3 bn and the 2025 base itself disagrees by
~10%.** Use the range in client material, never a point estimate. All of these
are market-research vendor outputs, not independent studies.

## The structural market fact

The commercially decisive feature of this market is not its size — it is a
licence asymmetry, measured first-hand this run across 25 repositories:

- **The AI/agent layer is permissive.** 5 of 6 shelved education agents are MIT,
  1 is Apache-2.0.
- **The platform-of-record layer is copyleft.** Moodle GPL-3.0, Open edX
  AGPL-3.0, Canvas AGPL-3.0, Chamilo GPL-3.0, Tutor AGPL-3.0, i-educar GPL-2.0,
  H5P GPL-3.0.
- **Every standard integration boundary is permissive.** LTI 1.3 (`ltijs`,
  Apache-2.0), xAPI (Apache-2.0), LRS (`ralph`, MIT), MCP servers (MIT).

Market consequence: **nobody can sell a proprietary fork of the systems schools
already run.** Value accrues at the integration boundary, and that boundary is
licence-clean. This is the structural reason an AI-on-top integration practice
is the defensible position in education, and it holds in every region.

## Demand-side signal: adoption is ahead of governance everywhere

This is the most consistent finding across all four regional searches, and it is
the sales thesis:

| Region | Adoption | Governance | Source |
| --- | --- | --- | --- |
| North America | 60% of US teachers use AI tools | Most US public schools still lack formal student AI policies | Gallup; Child Trends / US Dept. of Education |
| EMEA (schools) | **63%** of EU teachers use AI at least partly to generate explanations or practice exercises; **41%** do not use it for grading/summative assessment at all | Only **~30%** of EU teachers have had AI-focused training; only **~1/3** of national curricula include AI competences | European Commission, School Education Gateway teacher survey, Apr 2026 (n=1,130, secondary-skewed) |
| EMEA (schools, independent corroboration) | **63%** teacher AI use | — | Sanoma Learning European Teacher Survey 2026 — **20,000+ teachers across 14 countries** |
| EMEA — UK | — | **49%** of schools have no AI policy for staff *or* students | National Education Union, via secondary reporting |
| EMEA — Africa (higher ed) | — | **14%** confirm an institutional AI policy; **17%** report none; **69% do not know** | Frontiers in Education study, 2026 |
| EMEA + North America (higher ed) | — | ~70% of institutions have or are developing guidance | secondary summary |
| LATAM (higher ed) | 87% of institutions use AI in ≥1 area | Only 26% have a formal AI strategy | UNESCO IESALC / UNU-IAS, 200 institutions across 19 countries |
| APAC | China, India, Japan lead the regional market | Patchwork: binding law in Korea/Vietnam, light-touch in Japan/Singapore/Australia | Ken Research; Latham & Watkins |

The LATAM 87%-vs-26% gap is the sharpest quantified governance deficit found
anywhere in this research, and it comes from the most authoritative source in
the set (UNESCO).

## Opportunities by region

### North America

**Regulatory driver.** 134 AI-in-education bills introduced across 31 states in
2026 (MultiState tracker), focused on research, transparency and guardrails
rather than mandating adoption. **Four states — Maryland, Idaho, Oklahoma and
Virginia — passed 2026 laws requiring both state guidance and mandatory
district-level AI policy adoption.** New York's A 9190 would restrict classroom
AI to grade 9 and above, with exceptions for diagnostics and special education.
Federally, the US Department of Education published its final supplemental
priority on advancing AI in education on 2026-04-13, and a House committee
advanced the K-12 AI Literacy and Readiness Act of 2026. 30 states had issued
guidance as of January 2026.

**Opportunity.** District-level **AI policy-to-implementation** work is now a
statutory requirement in four states and it is work districts cannot do
themselves. Pair policy instrumentation with the Canvas agent stack
(`vishalsachdev/canvas-mcp`, MIT, 310★ — the strongest verified agent in this
region) and an xAPI/LRS audit trail that evidences compliance. The grade-9
threshold in NY-style bills makes **age-gating and per-cohort policy enforcement**
a concrete, specifiable deliverable.

#### Canada (inside North America — not a separate region value)

**Closing the first pass's "Canada is effectively unrepresented" gap.** The
structural fact is constitutional: **education is exclusively provincial in
Canada, so there is no national policy and there will not be one.** The federal
level does not have the jurisdiction, and provincial education ministers'
discussion of AI at their **June 2026 council meeting in Quebec City** was
reportedly marked by friction over federal overreach. Plan per province.

- **Quebec — the furthest along, and the most restrictive.** A **November 2024**
  Ministry of Education guide covers pedagogical, ethical and legal questions
  for education staff. A **March 2025 government directive suspended the use of
  AI assistants**. A separate *Prêt pour l'IA* report sets out **12
  recommendations** for responsible use. Quebec is the one jurisdiction in this
  KB that has actively *withdrawn* permission — an engagement there starts from
  reinstatement conditions, not adoption.
- **Ontario — no province-wide rule, policy made at board level.** The Ministry
  has issued no Policy/Program Memorandum on AI, and there is no province-wide
  ChatGPT ban. Individual boards fill the gap: **Upper Canada DSB** and
  **Kawartha Pine Ridge** have published staff and student guidance, and the
  Ontario Catholic trustees' association published a **September 2025** policy
  paper for Catholic boards. A **June 2026 Fraser Institute survey** reported
  only **42.3% of Ontario school boards have any formal AI policy for students**
  (secondary source — treat cautiously).
- **Coverage elsewhere:** a 2023 legislative scan found only **British Columbia,
  Quebec and Ontario** had taken concrete steps; one later source adds Alberta.

**Opportunity.** Ontario is a **72-board addressable market for the same
deliverable** — nearly 58% of boards have no student AI policy and no ministry
template is coming, so the district-policy instrumentation work described above
for US states applies here without the statutory deadline, sold on liability
rather than compliance. Quebec is the opposite engagement: a suspension to be
lifted, where evaluation evidence (`pedagogy-benchmark`) and the *Prêt pour
l'IA* recommendations are the gating artefacts. **Francophone delivery capability
is a hard requirement in Quebec**, and it is also what makes the one EMEA-origin
agent candidate, `braiinz94/braiinz-education` (French curriculum), worth the
watch item recorded in [`../agents/top.md`](../agents/top.md).

**Players.** State education departments and legislatures, US Dept. of
Education, teachers' unions (NEA, AFT, California Teachers Association),
Instructure/Canvas, Khan Academy. **Canada:** provincial ministries (Quebec's
Ministère de l'Éducation, Ontario's Ministry of Education), the Council of
Ministers of Education Canada, individual school boards as the real buyers in
Ontario, Canadian Teachers' Federation, Fraser Institute (research). Note the contested procurement: North Carolina
lawmakers are defending a USD 10 m earmark in Senate Bill 1006 for Khanmigo —
evidence that large single-vendor AI tutoring buys are now politically exposed,
which favours integrator-led, platform-neutral alternatives.

### EMEA

**Regulatory driver, and a timing correction that matters.** Education AI is an
**Annex III high-risk category** under the EU AI Act — systems that evaluate
learners or influence access to qualifications require conformity assessment and
human oversight. **The deadline moved:** the Digital Omnibus amendment, in effect
late July 2026, pushed stand-alone Annex III high-risk obligations to
**2027-12-02**, and AI embedded in regulated products to **2028-08-02**. Older
guidance still circulating says August 2026 — that is superseded. A December 2026
ban on certain AI-generated intimate imagery and abuse material is coming into
force. The UK remains light-touch and principle-based through existing
regulators. Gulf states moved unusually fast on formal governance, with Dubai's
KHDA issuing guidance to private schools.

**Opportunity.** The deferral to December 2027 creates a **14-month conformity
runway** — the rare case where the compliance calendar and the capability
calendar have come apart, and the right offer is readiness work rather than
remediation. Annex III conformity packages (human-oversight design, technical
documentation, evaluation evidence) are specifiable now. OpenOlat (Apache-2.0,
Switzerland) is the one permissively licensed institutional LMS verified, making
it the natural substrate for an EU-sovereign build. The OECD's 2026 Digital
Education Outlook recommending **purpose-built educational AI over
general-purpose tools** is a direct mandate for vertical work.

**Demand-side evidence — added on the second pass of 2026-10-31, closing the
gap the first pass declared.** The first pass found no EMEA adoption study. There
are in fact two, and they agree on the headline number:

- **European Commission, School Education Gateway teacher survey (Apr 2026)**,
  n=1,130, secondary-skewed: **63%** use AI at least partly for generating
  explanations or practice exercises, but **41% do not use it for grading or
  summative assessment at all.** Read those together: European teachers have
  adopted AI for *preparation* and stayed away from *judgement* — which is
  exactly the Annex III boundary, reached by professional instinct before the
  regulation bites.
- **Sanoma Learning European Teacher Survey 2026**, **20,000+ teachers across 14
  countries** — an industry survey, but by far the largest sample anywhere in
  this KB — independently reports teacher AI use at **63%**, and its headline
  finding is that teachers *want tools built for education*. That is trend 3 in
  [`trends.md`](trends.md) corroborated at 20k-teacher scale rather than by an
  OECD recommendation alone.
- **The capability deficit is training, not willingness:** only **~30%** of EU
  teachers have had AI-focused training (eunews reports 29.7%) and only **~1/3**
  of national curricula include AI competences.
- **Two European Commission reports published 2026-09-22**: one on generative AI
  in teaching and learning, and the **Eurydice** report *Digital education at
  school in Europe 2026: Bridging gaps in access, teaching and learning*. These
  are the authoritative member-state-level source and the right citation for
  client material. The OECD also published *Empowering Learners for the Age of
  AI* in June 2026.

**Second EMEA opportunity, from that data.** The gap is **teacher capability**,
not teacher willingness: 63% use against ~30% trained. Training-plus-tooling as
a single engagement — purpose-built assistant, teacher enablement, and the
Annex III oversight evidence produced as a by-product of the training records —
is specifiable from these numbers alone. The 41%-avoid-grading figure also tells
you where *not* to aim first.

#### Africa (inside EMEA — not a separate region value)

**This was a declared coverage hole in the first pass. It is activity, not
absence.** Africa falls inside the EMEA bucket; findings are placed here rather
than in a new region value.

- **African Union Continental AI Strategy** names education a priority sector —
  the continental frame any national programme is aligned to.
- **Zimbabwe** adopted a **National AI Strategy 2026–2030**, six pillars,
  education among the covered sectors.
- **Ghana**'s **National AI Strategy 2025–2035** calls for primary-level data
  science and coding, ethics education and teacher training; a **July 2026 draft
  computing curriculum revision** adds **AI literacy from kindergarten to
  Primary 6** — the most concrete curriculum-level mandate found in the region.
- **South Africa** published a final draft **National AI Policy** in the
  *Government Gazette* (**Notice 3880 of 2026, 10 April 2026**), including STEAM
  curricula, community AI centres and a proposed national AI office. **Status is
  contested:** a separate policy tracker lists the draft as *withdrawn*. Do not
  cite South Africa as settled policy without checking the Gazette directly.
- **Mauritius** ran a *National Learn-AI School Innovation Challenge* (2026).
- **Rwanda** has a National AI Policy but inconsistent institutional adoption.
  **Namibia** has no cohesive national AI strategy at all.
- **Institutional governance is near-absent where it matters most:** in the
  Frontiers higher-education survey, **69% of respondents did not know** whether
  their institution had an AI policy, 17% said there was none, and only **14%**
  confirmed one.

**Opportunity.** The 14%-confirmed / 69%-don't-know figure is a *sharper*
governance deficit than LATAM's 87/26 — and unlike LATAM it sits against named
national strategies (Zimbabwe, Ghana, Rwanda, South Africa draft) that create
funded implementation mandates with no institutional capacity behind them.
National-strategy-to-institutional-policy translation is the engagement shape,
and the Ghana KG–P6 curriculum revision is the most procurement-ready single
item. Pair with `learningequality/kolibri` (MIT, offline-first) for
connectivity-constrained deployment — see
[`../compose/patterns.md`](../compose/patterns.md) P-568-F.

**Caveat on sources.** The African findings rest on analysis pieces, a
Wikipedia entry and one peer-reviewed study. A frequently-repeated **USD 3 bn**
figure for continental AI/STEM centre rollout 2025–2027 is an **advocacy
estimate, not an official figure** — excluded from any client-facing number.

**Players.** European AI Office, UNESCO, OECD, UK DfE and existing sector
regulators, KHDA (Dubai). **Africa:** African Union (Continental AI Strategy),
national ICT/education ministries of Ghana, Zimbabwe, Rwanda and South Africa,
CIPESA (policy analysis). Platform-side: Moodle's European install base, Tutor /
Open edX (France), H5P (Norway), France Université Numérique (`ralph`), OpenOlat
(frentix GmbH, Switzerland).

### APAC

**Regulatory driver.** Three distinct models, per Latham & Watkins: comprehensive
risk-based (**South Korea, Vietnam**), targeted (**China**), light-touch
(**Japan, Singapore, Australia**). **South Korea's AI Basic Act entered into
force 2026-01-22** — transparency, risk assessment, human oversight and
documentation for high-impact systems; enforcement decrees still being finalised,
with a guidance-first grace period through 2026. **Vietnam's law takes effect
2026-03-01**, and a Vietnamese decision identifying high-risk AI systems
**explicitly covers education including automated assessment**, applying to
systems already in operation before 2026-08-15. Australia's TEQSA requires **all**
higher-education providers to submit institutional action plans on generative-AI
risk.

**Opportunity.** Two hard, dated compliance events (Korea in force, Vietnam
retroactive to systems live before 2026-08-15) plus a regulator-mandated
document deliverable in Australia (TEQSA action plans) — the most
deadline-driven region in the set. Note that **Moodle is an APAC product**
(Perth, Australia): Moodle-platform depth is a home-region capability here, and
`G36maid/moodle-mcp` (MIT, Rust) is the verified APAC-origin agent for it.
A multi-jurisdiction engagement needs policy enforcement that varies by country
inside one deployment.

**Players.** Government programmes, with China leading on state backing. A
market-research vendor names Google, Microsoft, IBM, Pearson and Byju's as key
players — treat that list cautiously, as it is vendor-sourced. Regulators: Korea's
AI Basic Act authorities, Vietnam's ministries, TEQSA (Australia), Singapore's
light-touch regime. The EU AI Act also reaches APAC vendors selling into Europe.

### LATAM

**Demand driver, and it is the strongest quantified one in this research.** The
UNESCO IESALC / UNU-IAS study of **200 institutions across 19 countries** found
**87% use AI in at least one area, while only 26% have a formal AI strategy** —
adoption driven by individual academics, researchers and students rather than
institutional strategy, and running ahead of any consistent approach to privacy,
bias, academic integrity or evaluation.

**Regulatory context.** Fragmented. The **Universidad de los Andes study, with
the Konrad Adenauer Foundation, published August 2026**, counted **716
AI-related regulatory instruments, rules and legislative proposals across 23
countries and territories, over 80% initiated since 2023** — and its own
conclusion is the useful part: *legislar rápido no es legislar bien*
("legislating fast is not legislating well"). **Mexico is the second most
prolific producer with 126 instruments, behind only Brazil.** Mexico's generic
AI regulation seeks to replicate the EU risk model (dated ALSUR source — treat as
such).

**Education-specific regulation — closing the first pass's declared gap.** The
first pass found none and said so. A Spanish-language search located it, and the
picture is thin but real:

| Country | Instrument | Binding? | What it does |
| --- | --- | --- | --- |
| **Peru** | **Ley N.º 31814 (2023)**, regulated by **Decreto Supremo N.º 115-2025-PCM** | **Yes** | The region's **first and only specific AI law**. The 2025 implementing decree prohibits certain uses and **names education among the sensitive domains**. School-level application detail was not located. |
| **Chile** | MINEDUC, ***PotencIA el aprendizaje*** (2025) | No — guidance | School-sector orientation document, explicitly not a closed norm. Chile also has a Política Nacional de IA (2021) and a bill in progress (**Boletín 16821-19**) that the current government reportedly does not want passed as drafted. |
| **Brazil** | **PL 2338** | Not yet | Sources conflict on status: one January 2026 survey says no norm in force, another says no law and no active debate, a third projects entry into force in 2026. **Verify in the Congresso Nacional record before citing.** |

**The honest summary:** Latin America has **no unified regulatory framework for
AI in higher education**; Chile and Brazil have national AI strategies without
education-sector regulation, and **Peru is the sole jurisdiction with a binding
instrument that names education at all.**

**Opportunity.** The 87/26 gap is a directly addressable **institutional AI
strategy and governance** engagement, and UNESCO's own recommendations name the
deliverables: fold higher education into national AI strategies, develop national
guidance, fund it, and **integrate AI literacy and governance into accreditation
and quality assurance** — that last one is procurement-ready, because
accreditation is already a budgeted institutional function. On the build side,
**i-educar** (GPL-2.0, 722★) is the reference Brazilian municipal platform; an
AI layer for it must attach across LTI/xAPI rather than fork, as GPL-2.0
requires.

**Players.** **UNESCO launched the Observatory on AI in Education for Latin
America and the Caribbean on 2026-04-14 in Santiago, Chile**, jointly with **CAF**
(Development Bank of Latin America and the Caribbean) — a named, funded, regional
convening body and the single best entry point in the region. Observatory
partners: CENIA (Chile), Cetic.br (Brazil), ECLAC, Fundación Ceibal (Uruguay),
Fundación Santillana, Tecnológico de Monterrey, ProFuturo, IRCAI. Tecnológico de
Monterrey has signed an agreement with UNESCO on AI in education.

### Global

**Cross-cutting drivers.** The year's consistent theme across every source is a
shift **from experimentation to governed, operational use** (1EdTech frames 2026
as the governance year; Tutorflow and Campus Technology both describe
pilots-to-operations). Agents that plan lessons and draft assessments for teacher
review are the named capability development (Educativa). HolonIQ expects focus on
ethics, transparency, agentic use cases and **proven instructional benefit over
broad personalisation promises**. 1EdTech points to digital credentials and
digital competencies rising, with employer expectations accelerating a
skills-driven model. Higher education is moving AI from experimentation to
embedded infrastructure across admissions, advising and administration.

**Opportunity.** Two things generalise across all regions. First, **evaluation**:
with "proven instructional benefit" becoming the bar and high-risk regimes
demanding evaluation evidence, `AI-for-Education/pedagogy-benchmark` (MIT, 1,143
teacher-exam questions incl. 223 on Special Educational Needs) is the only
verified permissive instrument for measuring pedagogical quality — it turns a
compliance obligation into a deliverable. Second, **purpose-built over
general-purpose**: both the OECD and Teachbetter identify the move away from
generic AI tools toward education-specific platforms, which is precisely an
integrator's position rather than a model vendor's.

## Declared gaps — what was searched and not found

Recorded explicitly, because a silent gap is indistinguishable from coverage.

### Closed on the second pass of 2026-10-31

The first pass declared five gaps. Four are now closed, and the record of how is
kept so the method is repeatable.

- ~~**EMEA: no dedicated EMEA-wide 2026 adoption study.**~~ **Closed.** Two
  exist and agree: the **European Commission School Education Gateway teacher
  survey (Apr 2026, n=1,130)** and the **Sanoma Learning European Teacher Survey
  2026 (20,000+ teachers, 14 countries)**, both at **63%** teacher AI use. Plus
  **two Commission reports of 2026-09-22**, including the **Eurydice** report
  *Digital education at school in Europe 2026*, which is the member-state-level
  source. *What made the difference:* searching the institution
  (`European Commission ... survey`) rather than the region acronym — "EMEA" is
  a Globant bucket, not a term European bodies publish under.
- ~~**EMEA: Africa is absent.**~~ **Closed.** AU Continental AI Strategy,
  Zimbabwe's National AI Strategy 2026–2030, Ghana's 2025–2035 strategy plus its
  July 2026 KG–P6 AI-literacy curriculum draft, South Africa's contested Gazette
  draft, Mauritius, Rwanda, Namibia — and a **14% / 17% / 69%-don't-know**
  institutional-policy split. It was a search gap, not an activity gap.
- ~~**LATAM: no education-specific AI regulation found.**~~ **Closed, and the
  answer is "almost none, for a reason."** Peru's **Ley 31814 + DS
  115-2025-PCM** is the only binding instrument naming education; Chile's
  MINEDUC *PotencIA el aprendizaje* is guidance; Brazil's **PL 2338** status is
  contested. *What made the difference:* searching in **Spanish**. The
  English-language query returned nothing because the instruments are not
  published or discussed in English.
- ~~**North America: Canada unrepresented.**~~ **Closed, and the finding is
  structural:** education is exclusively provincial, so there is no national
  policy to find. Quebec has a 2024 guide and a **March 2025 directive
  suspending AI assistants**; Ontario has no ministry memorandum and only
  **42.3%** of its boards have a student AI policy.

### Still open

- **APAC: adoption figures are market-research vendor outputs**, not primary
  government or institutional survey data. This is now the **weakest-evidenced
  region in the KB** — the EMEA closure above has overtaken it, and APAC is the
  one region with no primary teacher- or institution-level survey behind its
  numbers. Priority for the next pass.
- **South Africa's National AI Policy status is genuinely unresolved** — the
  Gazette (Notice 3880 of 2026, 10 April 2026) versus a tracker marking the
  draft withdrawn. Needs the primary Gazette record, not another secondary read.
- **Brazil's PL 2338 status is contradicted across three sources.** Check the
  Congresso Nacional record directly.
- **Market-size figures are still all vendor outputs.** No independent estimate
  was located in either pass; the USD 10.6–12.3 bn range stands as a range.
- **Africa has no mapped supply side.** Demand and policy are now evidenced, but
  no African education platform or agent repository appears anywhere in this KB.
  See [`../repos/foundations.md`](../repos/foundations.md).
- **A continental "USD 3 bn" African AI/STEM rollout figure is advocacy, not
  official** — deliberately excluded from the numbers above.
- **Vendor-source caveat.** Most trend and market sources in this run are vendor
  blogs or market-research summaries. The UNESCO IESALC figures and the named
  statutes are the most authoritative items on this page; percentages attributed
  to vendor blogs (e.g. an unverified "83% of institutions plan AI teaching
  assistant deployments") were deliberately excluded.
