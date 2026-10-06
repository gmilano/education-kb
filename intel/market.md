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
education-native agent project with real gravity. Below it, and substantially
re-measured in the third pass of 2026-10-06: **StudyMate** (MIT, 624★, China),
**anki-mcp-server** (MIT, 506★, 53 tools — the largest education MCP server),
**OpenTutor** (MIT, 130★, FSRS 4.5 + knowledge graph + local-first), **Mentingo**
(MIT, 91★, the first permissive AI-native LMS), OATutor (MIT, the auditable mastery
model), Educhain (MIT, content generation), canvas-mcp and moodle-mcp-server (MIT,
integration), plus a cluster of MIT **Agent Skills** at 100–300★
(universal-examprep-skill, algo-sensei, universal-diagnostic-tutor-skill,
kaogong-skill, education-skills). General frameworks — MAF, smolagents, LangGraph,
pydantic-ai, all MIT/Apache-2.0 — supply the rest.

**The layer is no longer thin, and that changes the pitch.** Three passes on
2026-10-06 took the permissive education shelf from "DeepTutor plus fragments" to
roughly 30 verified permissive projects, including a full MIT LMS. The
differentiator is shifting from *finding* the open source parts to **composing,
licensing and governing** them — which is also the part a client cannot do from a
listicle.

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

**Third pass (2026-10-06) — channel saturated, nothing net new.** The North America
query was re-run and returned the same facts already recorded above: 36% share /
$3.68B in 2026 → $32B by 2030; 60% of K-12 teachers using AI in 2024–25 with 32%
weekly; 134 bills across 31 states; California AB 1159 and Idaho SB 1227 on student
data; Oklahoma and Maryland human-oversight requirements; Ohio's July 2026 policy
deadline; North Carolina's $10M Khanmigo earmark; the AASA student framework from
all 50 states (created at America's Youth AI Festival in July 2026). **Stating this
explicitly rather than leaving silence:** the North America picture in this KB is
saturated for the open-web channel. Further depth needs a different instrument —
state procurement portals, district RFPs, or the state guidance trackers directly —
not another general search.

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

**New in the third pass (2026-10-06):**

- **Europe now has a growth curve, not just a 2026 number: $2.64B in 2026 →
  $8.0B by 2030 at 31.9% CAGR.** Note what that means — Europe is growing
  *materially slower* than the global 41.5% CAGR, so its 25% share of the market
  shrinks over the forecast period. The AI Act is both the demand driver and the
  brake, and a regional plan should assume Europe is the **compliance-depth**
  market rather than the growth market.
- **Middle East & Africa is sized for the first time in this KB: $0.56B in 2026 →
  $1.6B by 2030 at 34.3% CAGR** — small in absolute terms, and growing faster than
  Europe. Africa stops being a declared gap and becomes a sized opportunity.
- **Two sources disagree about MEA by two orders of magnitude, and the honest
  answer is a range.** Against the $0.56B regional figure, MarketsandMarkets sizes
  the **UAE** AI-in-education market at **$7.4M in 2024 → $21M by 2029 (19.1%
  CAGR)** and "Rest of Middle East" at 18.9% CAGR. A region cannot be $560M while
  its most advanced country is $7.4M, so the two are not reconcilable: they are
  almost certainly measuring different scopes (platform spend vs total AI-adjacent
  education technology). **Quote MEA as a range and name the uncertainty** rather
  than picking the flattering number — a client who checks will find the other one.
- **MEA has AI strategies, not AI statutes.** Saudi Arabia, the UAE, Egypt,
  Nigeria, Kenya, Rwanda, Morocco and South Africa all have published national AI
  strategies, and **none has an AI-specific binding statute yet.** That is the
  mirror image of the EU engagement: in Europe you sell conformity against a law
  that exists; in MEA you sell governance design *before* the law arrives, which is
  a shorter sales cycle and a weaker procurement trigger. Price and sequence
  accordingly.
- **The UAE has mandated AI in every public school, and this is the single most
  concrete demand signal in the region.** Approved by **Cabinet decision in May
  2025**, mandatory AI runs from **Kindergarten (age 4) to Grade 12** starting in
  the **2025–26 academic year**. The design details are the commercially useful
  part:
  - it is **woven into an existing subject** (Computing, Creative Design and
    Innovation) **without extending school hours** — so the deliverable is
    integrated curriculum material, not a new timetable slot;
  - it is taught by **specially trained teachers** — teacher enablement is funded
    and mandatory, not discretionary;
  - it is organised around **seven areas**: foundational concepts; data and
    algorithms; software use; **ethical awareness**; real-world applications;
    innovation and project design; and **policies and community engagement**.
  Two of the seven areas are governance and civics rather than technique, which
  means the content pipeline has to produce age-appropriate *ethics and policy*
  material, not only technical exercises. See the new pattern P9 in
  `compose/patterns.md`.

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

**New in the third pass (2026-10-06):**

- **The scale number this KB was missing: approximately 530 million K-12 students
  in Asia (2024).** Every per-learner cost, licence and inference decision changes
  shape at that denominator. It is also the reason offline-capable and
  small-model deployments matter in APAC and not only in LATAM.
- **Regional AI adoption is projected to move from 65–75% in 2025 to 80–90% in
  2026.** Adoption is not the constraint anywhere in APAC.
- **China's AI-education mandate is provincial, specific, and includes a
  restriction that directly constrains the architecture.** Earlier passes recorded
  China as having a "compulsory national AI curriculum"; probed precisely, the
  mandates are issued at provincial level:
  - **Beijing:** every primary and secondary school must deliver **at least 8 hours
    of AI lessons per year**, from **1 September 2025** — compulsory from age six.
  - **Guangdong:** **6 hours annually** in lower grades, rising to **one hour a
    fortnight in grades 10 and 11**.
  - The curriculum progresses from voice-recognition basics in early grades to
    machine learning, **misinformation detection** and applied projects by high
    school.
  - **Primary-school pupils are barred from independent generative-AI use, and
    teachers are prohibited from substituting AI for their core instructional
    duties.**
  That last point is a build requirement, not a policy footnote: a compliant K-12
  deployment in China needs **age-gated capability** (younger cohorts get
  teacher-mediated AI only) and a teacher-in-the-loop design that is enforced by the
  system rather than by guidance. It is also the strictest form of the
  human-oversight requirement that EMEA and North America express more loosely, so
  **a design that satisfies Beijing satisfies the others**. Pattern P9 in
  `compose/patterns.md` builds to it.
- **Regulatory posture, stated per country rather than per region:** Korea's
  Framework Act in force **22 January 2026**; **Vietnam's Law No. 134/2025/QH15 in
  force 1 March 2026 — Southeast Asia's first dedicated AI law**; China the most
  assertive regulator while also leading on deployment; **Japan deliberately
  light-touch and voluntary** to favour innovation; **India and Australia still
  without a national framework in force**, both working on one. A single APAC
  compliance story does not exist, and "APAC-ready" is not a claim you can make.

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

**New in the third pass (2026-10-06):**

- **The governance gap now has an institutional number, and it is the sharpest
  single statistic in this KB: 87% of LATAM higher-education institutions use AI in
  at least one area of their activities, and only 26% have a formal AI strategy.**
  Earlier passes carried "fewer than 10% have formal guidelines and sufficient
  capacity", which is a different and stricter measure. Use both and say which is
  which: **87/26** is the strategy gap, **>50% of teachers in Chile and Brazil vs
  <10% of institutions ready** is the capability gap. The second is the harder
  problem and the longer engagement.
- **LATAM faculty are measurably more positive about AI than the global average:
  72% report "positive" or "very positive" views, against 57% globally.** Combined
  with 79% of faculty using AI in teaching — **18 points above the global figure
  recorded in 2025** — the region is an *enthusiasm-rich, governance-poor* market.
  That is an unusual and favourable shape: the resistance that slows EMEA
  engagements is largely absent, and what is missing is structure.
- **Uruguay became the first Latin American country to sign the Council of Europe's
  Framework Convention on Artificial Intelligence and Human Rights, Democracy and
  the Rule of Law (2025).** This matters more than its market size: a Council of
  Europe convention signatory is committing to a governance vocabulary that is
  **interoperable with the EU's**, so compliance artefacts built for an EU AI Act
  engagement transfer to Uruguay with far less rework than to Brazil's PL 2.338 or
  Mexico's sectoral rules. Uruguay is small (62.21, third in the region's global
  top-50 placings) and is now the **cheapest bridgehead for reusing EMEA
  compliance IP in LATAM.**
- **The regional pioneer set is consistent across sources:** Chile, Brazil and
  Uruguay, on data availability, governance frameworks and infrastructure — with
  **Chile the standout through CENIA**, the national AI centre behind Latam-GPT.

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

4. **Curriculum mandates are now a funded demand driver, and they come with
   architectural constraints.** Two jurisdictions have made AI instruction
   compulsory with published specifics: the **UAE** (Cabinet, May 2025 — KG to
   Grade 12 from the 2025–26 school year, seven content areas, woven into an
   existing subject without extra school hours, specially trained teachers) and
   **China at provincial level** (Beijing: ≥8 hours a year for every primary and
   secondary school from 1 September 2025; Guangdong: 6 hours in lower grades
   rising to an hour a fortnight in grades 10–11). This is different in kind from
   the regulation in points 1 and 2: a mandate creates a **budgeted obligation to
   deliver content and train teachers**, not merely a constraint on how you deploy.
   It also hands you the two hardest requirements for free as design inputs:
   **age-gated capability** (Beijing bars primary pupils from independent
   generative-AI use) and **enforced teacher-in-the-loop** (teachers may not
   substitute AI for core instruction). Build to the mandate and the oversight
   obligations in points 1 and 2 are largely discharged as a side effect.

The deliverable that satisfies the first three is the same side-car. Build it once.
The fourth needs one more thing on top — a curriculum-alignment and age-gating
layer — which is pattern P9 in `compose/patterns.md`.

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

## What changed in the third pass of 2026-10-06

| Finding | So what |
|---|---|
| **UAE: AI compulsory KG→Grade 12** from 2025–26 (Cabinet May 2025), 7 content areas, inside an existing subject, trained teachers | a budgeted content-and-enablement mandate, not just a constraint. Two of the seven areas are ethics and policy, so the pipeline must produce governance material too |
| **China: Beijing ≥8 h/year from 1 Sep 2025; Guangdong 6 h → 1 h/fortnight (grades 10–11)**; primary pupils barred from independent generative-AI use; teachers may not substitute AI for core instruction | **age-gated capability and enforced teacher-in-the-loop are build requirements.** Satisfy Beijing and you satisfy EMEA/NA oversight |
| Europe: **$2.64B (2026) → $8.0B (2030), 31.9% CAGR** — slower than the 41.5% global rate | Europe is the compliance-depth market, not the growth market; its share shrinks over the forecast |
| **MEA sized for the first time: $0.56B (2026) → $1.6B (2030), 34.3% CAGR** — but a second source puts the **UAE** at $7.4M (2024) → $21M (2029) | irreconcilable scopes. **Quote MEA as a range and name the uncertainty** |
| MEA: Saudi, UAE, Egypt, Nigeria, Kenya, Rwanda, Morocco, South Africa all have AI **strategies, none has a binding AI statute** | mirror image of the EU sale: governance design *before* the law, shorter cycle, weaker procurement trigger |
| APAC: **~530M K-12 students** (2024); adoption 65–75% (2025) → 80–90% (2026) | the denominator that makes small-model and offline deployment an APAC concern, not only a LATAM one |
| APAC law, per country: Korea 22 Jan 2026 · **Vietnam 1 Mar 2026, SEA's first** · Japan deliberately voluntary · **India and Australia still have no national framework in force** | "APAC-ready" is not a claim you can make |
| LATAM: **87% of institutions use AI, 26% have a formal AI strategy**; **72% of faculty positive vs 57% globally** | enthusiasm-rich, governance-poor — the most favourable shape for a governance-led engagement in this KB |
| **Uruguay is the first LATAM signatory of the Council of Europe AI Framework Convention** (2025) | the cheapest bridgehead for reusing EMEA compliance IP in LATAM — an interoperable governance vocabulary |
| North America channel **saturated — no net new findings**, explicitly stated | further depth needs procurement portals and state trackers, not another general search |
| The permissive open source layer went from "DeepTutor plus fragments" to **~30 verified projects incl. a full MIT LMS** | the differentiator moves from *finding* the parts to **composing, licensing and governing** them |
