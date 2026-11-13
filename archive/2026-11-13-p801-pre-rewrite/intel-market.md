---
industry: education
region: Global
updated: 2026-11-13
---

# Education AI — market map and opportunities by region

Researched 2026-11-13. Where sources disagree, the disagreement is shown rather
than averaged away. Market-size figures for AI in education come largely from
vendor blogs citing differing research firms and should be treated as
order-of-magnitude only.

## Market size — contested

Three 2026 figures for the AI-in-education market, all for the same year:
**$10.4B**, **$11.4B**, and **$12.3B**, with 2030–2033 projections ranging from
$32.3B (by 2030) to $57B (by 2033). All three trace to secondary vendor
sources. Use "roughly $10–12B in 2026, growing fast" and do not quote a
specific figure to a client without a primary report.

## The structural fact of this market

**Adoption has outrun governance everywhere, and the gap is the commercial
opportunity.** Every region shows the same shape — very high individual use by
students and teachers, very low institutional policy coverage:

| Evidence | Figure | Source type |
|---|---|---|
| Students using AI in their studies (16 countries) | 86% | Digital Education Council survey, via secondary |
| LATAM higher-ed institutions using AI in ≥1 area | 87% | UNESCO IESALC study |
| LATAM institutions with any formal AI framework | 26% | UNESCO IESALC study |
| LATAM universities with no specific AI budget | 55% | UNESCO IESALC study |
| LATAM institutions that evaluate their AI implementation | 9% | UNESCO IESALC study |
| US faculty reporting a formal institutional AI policy | ~25% | secondary roundup |

The sellable work is therefore rarely "build a tutor". It is **governance,
integration, evaluation and teacher enablement around tools the institution is
already using unofficially.**

## Global players

**Open-source / buildable layer:** HKUDS (DeepTutor, Apache-2.0, 58.6k),
Tsinghua MAIC (OpenMAIC, MIT, 43.4k), Open edX nonprofit (Harvard/MIT lineage),
Moodle HQ, Instructure (Canvas), Learning Equality (Kolibri, MIT), Khan Academy
(Perseus MIT; Khanmigo commercially), Oppia Foundation, Frappe, OpenEduCat.

**Policy and standards setters:** UNESCO and UNESCO IESALC, OECD, European
Commission (AI Act, Digital Education Action Plan), 1EdTech (LTI, Caliper,
QTI), national education ministries.

**Commercial incumbents to integrate with or displace:** Instructure, Anthology,
PowerSchool, Google for Education, Microsoft Education, Duolingo, Chegg,
Coursera, 2U/edX, plus OpenAI and Anthropic distributing directly into
education.

## Opportunities by region

### North America

**Adoption/regulation:** The most legislatively active region, and the activity
is restrictive rather than enabling. Trackers count **134 AI-in-education bills
across 31 states in 2026**, within **1,500+ AI bills nationwide**, of which
nearly 100 could directly affect K-12 student AI use. Concrete instruments:
**North Carolina SL 2026-41** (AI-literacy standards; state model policy by
2026-12-31, local policies by 2027-06-30, teacher training by 2028-06-30);
**Idaho SB 1227** → statewide generative-AI framework approved August 2026;
**Texas** general AI law effective 2026-01-01, with **HB 2400 barring AI from
delivering direct classroom instruction**; **New York A 9190** would restrict
classroom AI to grade 9+; **New Jersey A 4352 / S 2862** would add AI to
curriculum and require AI credentials at public colleges. Federally, the **K-12
AI Literacy and Readiness Act of 2026** advanced out of the House Education and
Workforce Committee. Teachers' unions (NEA, AFT, CTA) have issued classroom AI
guidance; OpenAI and Common Sense Media proposed a California ballot initiative
("Parents & Kids Safe AI Act"). Bill statuses in trackers mix introduced with
enacted — verify against the legislature before advising.

**Players:** Instructure/Canvas is the integration target that matters; Canvas
dominates higher ed. PowerSchool in K-12 SIS. Large districts (Chicago, Denver,
Charlotte-Mecklenburg) now have their own AI policies, which means district-level
procurement with real compliance requirements.

**Opportunities:**
1. **Compliance-aware tutoring that respects instruction bans.** Texas HB 2400
   forbids AI *delivering instruction*; practice, feedback, and teacher support
   remain open. A tutor architected as "practice and feedback, human delivers
   instruction" is sellable in states where a general tutor is not.
2. **State-mandated AI literacy programs with deadlines.** North Carolina's
   model-policy and teacher-training dates are fixed and near. Districts need
   curriculum, training, and a policy artifact — deliverable work with a
   statutory deadline.
3. **Canvas-native agents.** `canvas-mcp` (MIT, 102 tools) plus LTI 1.3 is the
   fastest route to an agent inside the dominant North American LMS.
4. **Policy-to-controls translation.** Turning a district AI policy into
   enforced technical controls (logging, age gating, FERPA/COPPA posture) is
   consulting work no open-source project covers.

### EMEA

**Adoption/regulation:** The binding regime is the **EU AI Act**, under which
education AI affecting admissions, assessment, or access to qualifications is
**high-risk (Annex III)**. Timelines shifted in 2026 and sources conflict: the
**Digital Omnibus, Regulation (EU) 2026/1744**, is reported to have moved
stand-alone Annex III high-risk education obligations to **2027-12-02**, with
transparency duties from August 2026; vendor guides still citing August 2026 for
high-risk obligations appear outdated. The **emotion-recognition ban in
education** has applied since February 2025. The **AI literacy duty (Article 4)**
was softened in July 2026 to a duty to "support the development of AI
literacy". Verify against EUR-Lex (Regulation (EU) 2024/1689) before advising a
client. On 2026-06-18 the **European Commission and OECD published an AI
literacy framework for primary and secondary schools**, alongside updated
ethical guidelines ("Empowering Learners for the Age of AI"). Council of the EU
2026 documents stress digital sovereignty explicitly, calling reduced dependency
on AI tools developed outside Europe "critical" for education and training.
Funding channels: Digital Education Action Plan, Erasmus+, Horizon Europe, ESF+.

**Players:** Moodle (dominant in European public education), ILIAS
(German-speaking vocational and public sector), Chamilo (Spain, francophone
Africa), Opencast and BigBlueButton (university infrastructure), national
ministries and agencies.

**Opportunities:**
1. **High-risk conformity packages for assessment and admissions AI.** The
   deadline moved; it did not disappear. Institutions need risk management,
   documentation, human oversight, and logging for exactly the systems they
   already run. This is the highest-value regulated work in education globally.
2. **Sovereign, self-hosted education AI.** The Council's sovereignty language
   plus GDPR makes "runs in our own infrastructure, on open weights" a
   procurement requirement rather than a preference. Moodle/ILIAS + self-hosted
   inference + MIT/Apache agent layer is a directly sellable stack.
3. **AI literacy delivery against the Commission/OECD framework.** A published
   framework with institutional obligations behind it, and a teacher population
   that needs training.
4. **Moodle MCP server.** Moodle is the most-deployed LMS in the world and has
   **no significant MCP server** in this window. Building one, MIT-licensed,
   would be a reusable asset across most EMEA education engagements.

### APAC

**Adoption/regulation:** The most fragmented region, and education is usually
caught as a *high-risk category inside general* AI law rather than addressed
directly. **South Korea's AI Basic Act took effect January 2026** and names
education a high-impact area alongside healthcare and finance; year one is
reported as a pilot with limited enforcement and enforcement decrees still being
finalized. **Vietnam's binding AI law took effect March 2026**, puts education
in its high-risk category, and requires **pre-deployment registration and human
oversight**, with an implementing decree in April 2026. **Australia** has no
AI-specific statute; its 2024 mandatory-guardrails proposal covers high-risk
education uses, and the higher-ed regulator **TEQSA has required universities to
submit generative-AI risk management plans**. **China** has the most detailed
targeted rules (content labelling, algorithm registration) but they are not
education-specific. **Singapore, Japan, New Zealand** rely on voluntary
toolkits and existing law. **Hong Kong** is focused on responsible adoption and
a new AI R&D institute. The EU AI Act reaches APAC vendors selling into Europe.
Data sovereignty and localization are recurring adoption priorities (Malaysia
frames sovereign cloud as foundational).

**Players:** Tsinghua MAIC (OpenMAIC, MIT, 43.4k) and HKUDS (DeepTutor,
Apache-2.0, 58.6k) — **the two largest education AI agent projects in the world
are both APAC-origin**. India: BHASHINI language infrastructure and DIKSHA
(which already ships AI features such as in-video keyword search and read-aloud
for visually impaired learners); **Bharat EduAI Stack** open Indic-language
models announced September 2026 by IIT Madras-incubated Bodhan AI — an
announcement, not a rollout. Moodle and Frappe LMS are widely deployed.

**Opportunities:**
1. **Multi-jurisdiction compliance architecture.** A regional university group
   or edtech vendor faces Korean high-impact rules, Vietnamese registration,
   Australian TEQSA plans, Chinese labelling, and the EU Act for exports — all
   at once. One policy-enforcement layer with per-jurisdiction configuration is
   a genuine architecture problem worth paying for.
2. **Vietnam pre-deployment registration and human oversight.** A hard, dated,
   binding obligation already in force. First-mover advisory and the technical
   oversight/logging layer it requires.
3. **Localize the APAC-origin agents.** DeepTutor (Apache-2.0) and OpenMAIC
   (MIT) are permissively licensed, large, and built in the region. Adapting
   them to Indic, Bahasa, Thai, Vietnamese and Japanese curricula is
   lower-risk than building a tutor from zero.
4. **Sovereign deployment for localization mandates.** Self-hosted open weights
   plus a local LMS answers data-residency requirements directly.

### LATAM

**Adoption/regulation:** The widest gap between use and governance of any
region, and the best-documented. **UNESCO IESALC: 87% of higher-education
institutions use AI in at least one area, 26% have any formal framework, 55% of
universities have no specific AI budget, and only 9% evaluate their AI
implementation.** In schools, **more than 50% of teachers in countries such as
Chile and Brazil already use AI tools, while fewer than 10% of institutions have
formal guidelines.** The Digital Education Council's **2026 LATAM higher-ed
survey (with Tecnológico de Monterrey's Institute for the Future of Education)
reports 92% of students and 79% of faculty actively engaging with AI.**
Regulation is fragmented: a 2026 **Universidad de los Andes** inventory
identified **716 AI-related regulatory instruments, rules and proposals across
23 countries and territories**. **Brazil's PL 2.338/2023** is the main risk-based
bill; **Colombia** chose a national policy with budgeted actions through 2030
rather than immediate horizontal obligations. Argentina, Brazil, Chile,
Colombia, Costa Rica, Mexico and Peru have adopted the OECD AI Principles.

**Players:** UNESCO IESALC — launched an **Observatory on AI in Education for
Latin America and the Caribbean in April 2026** to guide public policy;
**Cetic.br** (Brazil) and **Ceibal** (Uruguay) as national data sources and, in
Ceibal's case, a national deployment vehicle; Tecnológico de Monterrey; World
Economic Forum (regional AI white paper arguing for harmonized regulation);
Universidad de los Andes. Platform-wise: Moodle, Chamilo and RosarioSIS have
deep regional footprints.

**Opportunities:**
1. **Institutional AI governance as a productized offering.** 87% using,
   26% governed, 9% evaluating. This is the single clearest
   product-market fit in this entire KB: a repeatable package of policy,
   controls, teacher training, and an evaluation harness.
2. **Evaluation and measurement.** Only 9% evaluate. An evaluation layer
   (pedagogical eval plus xAPI/Caliper telemetry plus dashboards) is a
   defensible, repeatable deliverable — and `AITutor-EvalKit` (MIT) plus pyKT
   (MIT) give it an open-source spine.
3. **Low-budget deployment models.** 55% have no AI budget, so the offer must be
   cheap to run: Kolibri (MIT, offline-first) or Moodle plus self-hosted open
   weights, not per-seat frontier API spend.
4. **Ceibal-style national programs.** Uruguay's Ceibal is a working template
   for country-scale deployment; similar ministry programs are the large
   contracts in this region.
5. **Spanish/Portuguese pedagogical content generation.** `educhain` (MIT) and
   Oppia (Apache-2.0) localized to national curricula (ENEM, ICFES, PAES, SEP).

### Global / cross-region

**Opportunities not tied to one region:**
1. **An LTI 1.3 AI tool provider, MIT-licensed, built once.** It mounts in
   Moodle, Canvas, Open edX, Sakai and ILIAS — every region, every segment. No
   open-source library reached a foundational bar in this window, so this is
   greenfield and reusable across engagements.
2. **Grading and feedback agents.** No dominant open-source grading agent
   exists anywhere. `nbgrader` (BSD-3-Clause) is the substrate; the agent layer
   above it is unbuilt.
3. **Pedagogical evaluation as a practice.** `AITutor-EvalKit` at 4 stars is the
   state of the art. Institutions in every region are deploying tutors with no
   way to measure teaching quality. Whoever makes this credible sets the
   standard.
4. **Teacher enablement.** Universal across regions, consistently
   under-resourced, and the one intervention every policy framework mandates.
