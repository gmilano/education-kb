---
industry: education
region: Global
updated: 2026-10-06
---

# Market Intelligence — Education

## Global market size

| Metric | Value | Source basis |
|---|---|---|
| AI in education market, 2025 | $7.52B | Research and Markets, AI in Education Market Report 2026 |
| AI in education market, 2026 | $10.6B | same; 40.9% CAGR 2025→2026 |
| Projected 2030 | $42.48B | 41.5% CAGR |

Growth is real but the composition is shifting: the defining movement of 2026 is
**away from generic AI tools and toward platforms purpose-built for education**,
and from experimentation toward governance. Budget is moving to whoever can show
instructional value and a defensible oversight story — which is a services
opportunity more than a licensing one.

## Market map

**Proprietary incumbents.** Khan Academy (Khanmigo — publicly funded at state
level in the US), Instructure (Canvas), Anthology/Blackboard, Pearson, Duolingo,
Google for Education, Microsoft Education. These own the buyer relationship.

**Open source platform layer.** Moodle (GPL-3.0), Open edX (AGPL-3.0), Canvas LMS
(AGPL-3.0), Chamilo (GPL-3.0), Sakai (ECL-2.0), ILIAS (GPL-3.0), Frappe LMS
(AGPL-3.0), Kolibri (MIT), Oppia (Apache-2.0). See `verticals/solutions.md`.

**Open source AI layer.** DeepTutor (Apache-2.0, 40.8k★) is the only
education-native agent project with real gravity. Below it: OATutor (MIT, the
auditable mastery model), Educhain (MIT, content generation), canvas-mcp and
moodle-mcp-server (MIT, integration). General frameworks — MAF, smolagents,
LangGraph, pydantic-ai, all MIT/Apache-2.0 — supply the rest.

**Where Globant fits.** The platform layer is copyleft and the AI layer is thin.
The reusable, defensible position is the **permissive side-car**: agent services
that integrate over LTI 1.3 and MCP, carry Globant's own license, and work
against whichever LMS the client already runs.

## Opportunities by region

### North America

- **Largest regional share: 36% of the global market, $3.68B in 2026**, projected
  to reach $32B by 2030.
- Adoption is already broad: **60% of US K-12 teachers used AI tools in the
  2024–25 school year; 32% used them at least weekly.** The sale is no longer
  "should you use AI" — it is governance, procurement and integration.
- **Regulation is the demand driver.** 134 AI-in-education bills introduced
  across 31 states in 2026. Concretely:
  - California **AB 1159** prohibits using student data to train AI models.
  - **Oklahoma and Maryland** require human oversight and bar AI from making
    high-stakes decisions about students.
  - **Ohio** mandated that every public district have a written AI policy by a
    July 2026 deadline.
  - **Georgia and Mississippi** require computer science credits including AI
    instruction from the late 2020s.
  - **New York City DOE** issued guidance in March 2026 built on a "Traffic
    Light Framework," informed by Google and OpenAI.
  - **North Carolina** committed $10M to fund Khanmigo across participating
    districts — evidence that states will buy AI tutoring directly.
- **Opportunity:** policy-to-implementation work. Districts now have mandates and
  no capability. Offer: AI policy implementation, a human-oversight gate wired
  into the grade path, student-data-boundary architecture (AB 1159 means
  no-training-on-student-data must be *provable*), and Canvas integration via
  canvas-mcp. Sell the audit trail, not the chatbot.

### EMEA

- **The EU AI Act is the whole conversation.** AI used in education access and
  assessment — admissions, student evaluation, exam scoring — is classified
  **high-risk** under Annex III.
- **Timeline matters and buys time:** high-risk obligations for stand-alone
  systems are **deferred to 2 December 2027**; high-risk AI embedded in
  already-regulated products to **2 August 2028**. The European AI Office
  implements the general-purpose AI provisions. In 2026 the EU agreed amendments
  clarifying overlap with machinery rules.
- **Deployment reality:** schools are running parent-facing and admin chatbots on
  commercial APIs, but districts with strict data-residency requirements
  **self-host open-weight models** (Llama, Mistral) instead.
- **Opportunity:** a sovereign, high-risk-ready stack delivered well before the
  2027 deadline — on-prem Ollama/vLLM, typed outputs, checkpointed audit trails,
  explainable mastery estimation, and a documented human-oversight gate. The
  deferral is the window: a system designed for Annex III now avoids a forced
  rebuild in 2027. Germany/Austria/Switzerland additionally skew toward ILIAS and
  SCORM compliance training.

### APAC

- **Largest absolute AI market: ~USD 102B as of March 2026** (all sectors, not
  education alone).
- **India is the fastest-growing APAC AI market at 38.9% CAGR**, anchored by the
  IndiaAI Mission and ~2.6M STEM graduates a year. In **July 2026 the Indian
  government signalled it may pursue dedicated, risk-based AI legislation.**
  India's DPDP Act obligations are now in force for systems processing personal
  data.
- **South Korea's AI Basic Act takes effect January 2026**, giving roughly a year
  to build compliance frameworks for high-impact systems. **China maintains the
  region's most restrictive framework**, built on three foundational laws.
- **Sovereign model build-out is universal:** India's Sarvam AI, Malaysia's ILMU,
  Indonesia's Sahabat AI, Singapore's SEA-LION, Korea's HyperCLOVA X Think,
  Japan's NTT Sarashina. These are base models — **none ships an education agent
  layer**, which is precisely the gap.
- **Cultural tailwind:** the Ipsos Education Monitor 2026 finds *lower* support
  for banning AI in schools across the Asian markets surveyed — while **Australia
  and New Zealand record higher support for banning AI in schools**, a real
  split inside the region.
- **Opportunity:** education agent layers on top of sovereign models — the models
  exist, the pedagogy layer does not. Multi-jurisdiction architecture is the hard
  part and the differentiator: one deployment must satisfy Korea's AI Basic Act,
  India's DPDP and China's framework simultaneously. Treat ANZ as a separate,
  more restrictive sub-market.

### LATAM

- **Teacher adoption is ahead of institutional readiness, sharply.** In Chile and
  Brazil **more than 50% of teachers already use AI tools, while fewer than 10%
  of institutions in the region have formal guidelines and sufficient capacity**
  to integrate them with clear criteria. That gap is the engagement.
- **UNESCO launched the Observatory on Artificial Intelligence in Education for
  Latin America and the Caribbean on 14 April 2026** — a regional platform to
  help states integrate AI with a focus on equity and quality. A credible anchor
  partner and a source of procurement momentum.
- **Enterprise AI deployment regionally sits at 47%.** Only Brazil (65.89), Chile
  (63.19) and Uruguay (62.21) place in the global top 50.
- **Regulation:** Brazil is the regional bellwether with **PL 2.338/2023**, a
  comprehensive horizontal, risk-based statute with transparency and supervisory
  architecture. **Mexico** added an opt-out requirement for automated
  decision-making in its latest data protection law, and its Congress is pushing
  labour and copyright amendments covering image rights and AI.
- **Constraints are structural, per CEPAL/ECLAC:** gaps in talent, investment and
  governance, with advanced AI training concentrated in a few countries and the
  **talent gap relative to the global average widening since 2022.**
- **Opportunity:** institutional capability, not just software — governance
  frameworks for the >90% of institutions that lack them, teacher enablement at
  scale, and low-cost deployments that respect connectivity and budget reality
  (Kolibri + ricecooker, fully MIT; Chamilo for Spanish-first public sector).
  Brazil's PL 2.338 readiness work mirrors the EU AI Act engagement and the
  artefacts transfer.

## Cross-region read

Two patterns hold in every region, which makes them safe to build once and sell
four times:

1. **Human oversight on any consequential decision** — required by Oklahoma and
   Maryland statute, by EU AI Act Annex III, by Brazil's PL 2.338 risk tiers, and
   by Korea's high-impact classification. It is also forced by the technical
   gap: no permissive open source auto-grader exists.
2. **Data residency and student-data boundaries** — California AB 1159, EU data
   residency practice, India's DPDP, and LATAM connectivity constraints all point
   at the same architecture: on-prem or in-region open-weight inference.

The deliverable that satisfies both is the same side-car. Build it once.
