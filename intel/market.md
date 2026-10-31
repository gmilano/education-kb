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

**Players.** State education departments and legislatures, US Dept. of
Education, teachers' unions (NEA, AFT, California Teachers Association),
Instructure/Canvas, Khan Academy. Note the contested procurement: North Carolina
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

**Players.** European AI Office, UNESCO, OECD, UK DfE and existing sector
regulators, KHDA (Dubai). Platform-side: Moodle's European install base, Tutor /
Open edX (France), H5P (Norway), France Université Numérique (`ralph`).

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

**Regulatory context.** Fragmented: a 2026 Universidad de los Andes study counted
**716 AI-related regulatory instruments, rules and legislative proposals across
23 countries and territories, over 80% initiated since 2023**. Mexico's generic
AI regulation seeks to replicate the EU risk model (dated ALSUR source — treat as
such).

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

- **EMEA: no dedicated EMEA-wide 2026 education-AI adoption study was found.**
  The search `AI education EMEA 2026 adoption regulation players` returned mostly
  US state activity and EU regulatory analysis. EMEA adoption evidence above is
  either EU-regulatory or a blended "Europe and North America" higher-ed figure.
  A follow-up on EU member-state education guidance or UK DfE policy is the way
  to close this.
- **EMEA: Africa is absent.** No African education-AI findings surfaced this run,
  despite Africa falling inside the EMEA bucket. This is a real coverage hole,
  not an absence of activity.
- **LATAM: no education-specific AI regulation was found.** The LATAM regulatory
  picture above is general AI policy. Education-specific regulatory instruments in
  the region were not located.
- **APAC: adoption figures are market-research vendor outputs**, not primary
  government or institutional survey data.
- **North America: Canada is effectively unrepresented.** Regional results were
  almost entirely US; Canadian provincial policy did not surface.
- **Vendor-source caveat.** Most trend and market sources in this run are vendor
  blogs or market-research summaries. The UNESCO IESALC figures and the named
  statutes are the most authoritative items on this page; percentages attributed
  to vendor blogs (e.g. an unverified "83% of institutions plan AI teaching
  assistant deployments") were deliberately excluded.
