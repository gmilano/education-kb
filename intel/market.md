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

**New this pass (2026-10-06):**

- **All 50 states** have now introduced AI legislation — the 134 bills across 31
  states specific to education sit inside a universal legislative wave. There is
  no national stance to design against; the unit of compliance is the state.
- **States have split into two camps, and they need opposite offers.** One camp is
  building procurement pipelines with real budget behind adoption (North Carolina's
  $10M for Khanmigo is the template). The other is applying brakes — bans,
  moratoriums and strict consent requirements. Qualify which camp a district sits
  in before pitching: in camp one you sell deployment, in camp two you sell
  governance, assurance and an auditable oversight gate, and a deployment pitch
  will lose.
- **Idaho SB 1227** joins California AB 1159 on student-data protection for AI
  tools in schools — the no-training-on-student-data requirement is now a
  multi-state pattern, not a California quirk, so build the data boundary once and
  evidence it everywhere.
- **Students are now a stakeholder with a published position.** In August 2026,
  students from all 50 states produced a **national framework for AI in America's
  schools** (via AASA). Student-body buy-in is becoming part of the procurement
  conversation; cite the framework in proposals rather than being surprised by it.

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

**New this pass (2026-10-06):**

- **Sized at last: the European AI-in-education market is $2.64B in 2026.** That
  is the regional number the earlier passes were missing — roughly 25% of the
  $10.6B global market, against North America's 36% / $3.68B.
- **The leaders are small, digitally mature states, not the large economies:**
  **Finland, Estonia and the Netherlands** lead European K-12 AI integration. For
  a reference deployment, these are the markets where the institutional appetite
  and the digital baseline already exist. Treat them as the proof-point tier.
- **Timeline precision matters.** The AI Act's **general application date is
  2 August 2026** — already passed. What is deferred is the *high-risk* obligation
  set: stand-alone Annex III systems to **2 December 2027**, high-risk AI embedded
  in already-regulated products to **2 August 2028**. So the general-purpose and
  transparency regime is live now, while the education-specific high-risk regime
  is the design window. Do not tell a client "the AI Act does not apply yet."
- **Most European institutions are in pilot-and-pre-compliance mode**, deploying
  AI in administration and teacher support first, keeping humans in the loop on
  consequential decisions, documenting deployments, and disclosing to students and
  parents what is AI-decided versus human-decided. That sequence — admin first,
  assessment last — is the lowest-friction entry path in the region.
- **Africa enters this KB.** Earlier passes treated EMEA as Europe. South Africa's
  **Draft National Artificial Intelligence Policy (2026)** is in progress, and
  **GenAITEd Ghana** — a context-aware, curriculum-aligned conversational AI agent
  for *teacher education* — is a published, first-of-its-kind African education
  agent (research, not a product shelf). Africa is a genuine greenfield in the
  EMEA bucket: policy forming, almost no deployed open source education AI, and
  teacher capability the binding constraint.

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

**New this pass (2026-10-06):**

- **Singapore published the world's first governance framework for agentic AI**,
  at Davos in **January 2026** (IMDA Model AI Governance Framework for Agentic AI,
  updated again in June 2026). This is the single most useful regulatory document
  in this KB, because it governs *agents* specifically, and its four dimensions
  are effectively a build checklist:
  1. assess and bound risk upfront — choose appropriate agentic use cases and
     place explicit limits on an agent's powers;
  2. make humans **meaningfully** accountable — define the checkpoints that
     require human approval;
  3. technical controls and process across the whole agent lifecycle;
  4. enable end-user responsibility through transparency **and training** — where
     an agent assists a user in their workflow, the framework expects education on
     its capabilities, common failure points and risks.
  Dimension 4 is a services line item: the regulator is asking for exactly the
  teacher-and-student enablement work Globant already sells. Design to this
  framework and the resulting artefacts largely satisfy EU Annex III and the US
  human-oversight statutes too.
- **Korea's AI Framework Act took effect 22 January 2026** (precise date; earlier
  passes recorded only "January 2026").
- **Vietnam has a dedicated AI law: Law No. 134/2025/QH15, in force 1 March
  2026** — net new to this KB, and evidence the binding-regulation wave now
  extends well beyond Korea, Singapore and China.
- **Named incumbents in APAC education:** Google, Microsoft, IBM, Pearson and
  **Byju's**, with China, India and Japan dominating regional spend. The buyer
  relationship is held by global platforms plus one regional giant.
- **More sovereign base models, still no pedagogy layer:** add **BharatGen**
  (IndiaAI Mission, ~$1.2B state investment), Japan's **Fugaku-LLM**, and Korea's
  National Sovereign AI Initiative champions (LG AI Research, SK Telecom, Naver
  Cloud, NC AI, Upstage). Sovereign *inferencing platforms* with in-country data
  residency are also being commercialised (e.g. NxtGen in India). The gap is
  unchanged and widening: the models and now the hosting exist; the education
  agent layer does not.

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

**New this pass (2026-10-06):**

- **Hard survey numbers for higher education, from the Digital Education Council
  AI in Higher Education LATAM Survey 2026:** **92% of students** and **79% of
  faculty** are actively engaging with AI, and **94% of faculty** expect to use it
  in future teaching. Adoption is effectively universal — but **88% of faculty
  report only "minimal" to "moderate" engagement**, i.e. adoption has not become
  pedagogical integration.
- **That 92/79 vs 88 split is the sharpest opportunity statement in this KB.**
  The region does not need an adoption campaign; it needs depth — curriculum
  redesign, assessment redesign and faculty capability. Selling "get your teachers
  using AI" into LATAM higher ed is selling something they already have.
- **Anchor institutions for a regional play:** the survey was run by the Digital
  Education Council with the **Institute for the Future of Education at
  Tecnológico de Monterrey**, supported by the **AI Global Education Network
  (AIGEN)** and the **Educational Innovation Network (RIE360)**. With UNESCO's LAC
  Observatory (14 April 2026), these are the credible doors into regional
  procurement.
- **The regulatory map is fragmenting, not converging** — Brazil's PL 2.338/2023,
  Chile's framework, Colombia's CONPES and Mexico's sectoral rules are all moving
  at different speeds. Plan per-country, not per-region.
- **Colombia is further ahead than its profile suggests:** it adopted a national
  AI policy via **CONPES 4144 (February 2025)** — a government-wide programme with
  budgeted actions through 2030 covering capacity building, adoption and ethical
  guardrails. A funded national programme is a procurement signal; Colombia
  belongs on the target list alongside Brazil, Chile and Mexico.
- **UNESCO's warning is the sales argument:** LAC higher-education institutions
  are increasingly using generative AI for teaching, learning and research while
  lacking policies to govern it, and the agency has flagged that the absence of
  institutional guidelines raises misuse risk and leaves staff uncertain about
  acceptable use. Governance is the entry engagement; the platform work follows.

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

3. **Agent-specific governance is now a named requirement, not an extrapolation
   from general AI rules.** Singapore's Model AI Governance Framework for Agentic
   AI (January 2026, updated June 2026) is the first regulator-issued document
   that governs autonomous planning and action directly: bound the agent's powers,
   define human approval checkpoints, control the whole agent lifecycle, and train
   the end user. Those four dimensions also discharge most of what EU Annex III,
   the Oklahoma/Maryland oversight statutes and Korea's high-impact classification
   ask for. **Use the Singapore framework as the build checklist in every region**,
   because it is the most specific and the most agent-aware of the four.

The deliverable that satisfies all three is the same side-car. Build it once.

## What changed in this pass — read this if you read nothing else

| Finding | So what |
|---|---|
| Europe sized at **$2.64B** in 2026; leaders are Finland, Estonia, Netherlands | the EMEA reference deployment belongs in a small digitally mature state, not a large economy |
| AI Act **general application already live (2 Aug 2026)**; only high-risk deferred to Dec 2027 / Aug 2028 | stop telling clients the Act does not apply yet |
| Singapore's **agentic-AI** framework (Jan 2026, world first) | the cross-region build checklist, and its dimension 4 is a billable enablement line |
| **Vietnam** AI law in force 1 Mar 2026; **Korea** exactly 22 Jan 2026 | the APAC binding-regulation wave is wider than Korea/Singapore/China |
| LATAM: **92% students / 79% faculty** adopting, but **88% of faculty shallow** | sell depth and integration, not adoption |
| **Colombia CONPES 4144** — funded national AI programme through 2030 | add Colombia to the LATAM target list |
| **All 50 US states** legislating; states split into buyers vs brakers | qualify the camp before choosing the pitch |
| **Africa** enters the KB: South Africa draft national AI policy, GenAITEd Ghana | genuine EMEA greenfield; teacher capability is the constraint |
| Several popular education **MCP servers are unlicensed** (see `agents/top.md`) | a licence probe belongs in the engagement's first week |
| **OpenEduCat is LGPL-3.0** — proprietary modules permitted | on the admin side, a module is a viable commercial shape, not only a side-car |
