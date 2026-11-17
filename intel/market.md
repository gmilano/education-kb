---
industry: education
region: Global
updated: 2026-11-17
---

# Market intelligence — education

**Pass `p871`, 2026-11-17.** Research legs run this pass: a global agent leg, a GitHub
trending leg, a platform leg, an industry-trends leg, a news leg, a market-sizing leg, and
**one leg per region** (North America, EMEA, APAC, LATAM).

## Source-quality warning, stated before the numbers

Market sizing for AI in education is **unusually unreliable**. This pass's sizing leg returned
2026 global estimates spanning **$9.58B to $23B** — a 2.4× spread — from publishers who do not
agree on whether "AI in education" means tutoring software, all edtech with an AI feature, or
institutional AI spend. Several of the sources are aggregator blogs restating each other.

**Use the figures below as directional only.** Where a client decision depends on the number,
commission the primary report. The *structural* findings in this file (who regulates what,
when obligations bite, which platforms are deployed where) are far more robust than the
dollar figures and should carry more weight in an engagement.

## Market size — directional

| Scope | 2026 estimate | Source character |
|---|---|---|
| AI in education, global | **$9.58B – $10.6B** (low cluster) | Market-research aggregators; the modal estimate |
| AI in education, global | **~$23B** | Attributed to Grand View Research — a broader definition |
| AI in education, global forward | ~$42.5B by 2030 | Single-source forecast, unverified |
| Total edtech, global | ~$213B in 2026 → ~$437B by 2033 | Separate and much larger category — do not conflate with AI-in-education |
| Edtech VC funding | **~$2.4B in 2025, down ~89% from the 2021 peak** (HolonIQ, via secondary) | The most strategically important number here |

**Read the funding number against the market-size number.** Forecast growth is strong while
venture funding has collapsed ~89% from peak. That combination means the buyer is the
**institution and the ministry**, not the venture-funded startup. Education AI in 2026 is a
services-and-integration market, not a product-launch market — which is precisely where a
studio like Globant has an advantage over a product company.

### Regional share of the AI-in-education market (directional, low-authority sources)

| Region | 2026 estimate | Growth |
|---|---|---|
| North America | ~$3.68B, **36–38% share** — largest | Mature |
| APAC | ~$2.85B, **fastest growing (~35% CAGR)** | Fastest |
| EMEA (Europe component) | ~$2.64B, ~32% CAGR | Steady |
| LATAM | **~$0.67B — smallest of the regions covered** | Thin data |

## Key players

| Category | Players |
|---|---|
| Hyperscaler / frontier vendors in education | OpenAI (ChatGPT Edu — four Australian universities, Nov 2026), Google Cloud (with Accenture, 1,000+ Indian institutions), Microsoft |
| Incumbent platforms | Instructure (Canvas), Moodle HQ, Anthology/Blackboard, D2L Brightspace, PowerSchool, Pearson, Chegg |
| Non-profit stewards | Axim Collaborative (Open edX), Apereo (Sakai, Opencast), 1EdTech (LTI/QTI/Open Badges), Ed-Fi Alliance, Learning Equality (Kolibri), PKP (OJS) |
| University labs shipping OSS | HKUDS / HKU (DeepTutor, LightRAG), THU-MAIC / Tsinghua (OpenMAIC), CAHLR / UC Berkeley (OATutor) |
| Services competitors | Accenture (the Google Cloud India deal is the reference case), Deloitte, Infosys, TCS, Globant |

## Opportunities by region

### North America

**Regulatory and procurement picture.** No single federal AI statute. The binding constraint
is **FERPA**, which applies the moment an AI tool touches identifiable student data. Activity
is state-led and fragmented: a tracker counts **134 AI-in-education bills across 31 states in
2026**, concentrated on data privacy, classroom use and curriculum. Federal action is funding-
shaped rather than prohibitive — the **K-12 AI Literacy and Readiness Act of 2026 (H.R. 8747)**
advanced out of committee, and the Department of Education issued a final rule making AI a
**weighted priority across all discretionary grant programs**. Institutional policy is
hardening in both directions: the **SUNY** systemwide policy requires AI-literacy training in
general education for undergraduates entering **fall 2026**, while **Berkeley Law** has barred
AI from all exams and credited coursework; Florida's Board of Governors is weighing mandatory
AI-use disclosure for faculty and students.

**Opportunities.**
- **FERPA-defensible self-hosted tutoring.** The combination "we never send student data to a
  model vendor" is directly sellable here. Stack: Ollama or vLLM + LiteLLM + DeepTutor or
  LibreChat, deployed in the institution's own tenancy.
- **Grant-aligned AI-literacy delivery.** AI is now a weighted priority across *all* ED
  discretionary grants, and SUNY-style literacy mandates create a curriculum-build market.
  `microsoft/ai-agents-for-beginners` and `mlabonne/llm-course` are MIT/Apache-2.0 bases that
  can be white-labelled into institutional curricula.
- **Fifty-state policy-compliance tooling.** 134 bills across 31 states is an
  unmanageable-by-hand compliance surface for any multi-state operator — a product-shaped gap.
- **Canvas-adjacent integration.** Canvas dominates US higher ed and is AGPL-3.0. Build
  permissive LTI 1.3 tools (via `ltijs`) that attach to it rather than forking it.
- **Assessment redesign.** Berkeley Law's exam ban and the Florida disclosure debate signal
  demand for assessment that is robust to AI, not merely detection of it. `edx-ora2` plus
  oral/viva and process-evidence workflows is a concrete offering.

### EMEA

**Regulatory picture — the most consequential in the world this year, and it just moved.**
- **Emotion recognition in education is already banned.** AI Act Article 5(1)(f) has applied
  since **2 February 2025**: inferring emotions of natural persons in education settings is
  prohibited except for medical or safety purposes. This is in force now and rules out a whole
  class of engagement-detection and attention-tracking products.
- **High-risk obligations for education were delayed to 2 December 2027.** The Digital Omnibus
  on AI (**Regulation (EU) 2026/1744**) moved admissions, assessment and exam-proctoring
  obligations from 2 August 2026 by roughly 16 months. Sources differ on fine points of the
  adoption timeline, and this session **could not reach `eur-lex.europa.eu`** (see gap below),
  so the primary text is unconfirmed here.
- **Transparency duties were NOT delayed.** Article 50 applies from **2 August 2026**: a
  student-facing chatbot must disclose that it is an AI. This is live.
- **AI literacy (Article 4)** is reported to have been softened by the Omnibus from ensuring a
  level of literacy to taking measures — secondary sources only.

**Opportunities.**
- **The 2027 window is the offer.** Institutions have ~12 months before high-risk obligations
  bite on admissions, assessment and proctoring. "Build it conformant now, not retrofitted in
  2027" is a time-boxed, concrete engagement with a date attached.
- **Article 50 disclosure retrofit** — immediate, small, high-volume work across every
  institution already running a support chatbot.
- **Sovereign, self-hosted deployment.** The UK signal is unusually sharp: Newcastle,
  Westminster and Southampton have reportedly decided **not to renew** commercial AI contracts
  on expiry, citing concerns about entrusting student data to commercial providers and the
  limits of agentic AI marking (via Times Higher Education, secondary). Non-renewal is a
  procurement opening for a self-hosted alternative, and the strongest EMEA demand signal in
  this pass.
- **OpenOLAT and ILIAS are EMEA-native.** OpenOLAT is Apache-2.0 — the permissive LMS base for
  a European build. ILIAS carries the German-speaking public sector.
- **High-risk conformance tooling** (logging, human oversight, accuracy documentation) built
  once against the AI Act and resold across institutions.

### APAC

**Regulatory picture — four genuinely different models, which is itself the opportunity.**
- **China:** no general AI law but the most binding specific rules already in force —
  generative AI, deep synthesis and recommendation-algorithm measures, with **AI-content
  labelling mandatory since 1 September 2025**.
- **Japan:** promotion-led. The **AI Promotion Act** took effect **4 June 2025** with no direct
  penalties; a new **AI Basic Plan** was adopted **14 July 2026**.
- **Singapore:** voluntary frameworks — IMDA's **Model AI Governance Framework for Agentic AI**
  launched **January 2026**; MAS is consulting on AI risk-management guidelines.
- **India:** least settled; principles-based and non-statutory, with **IT Amendment Rules 2026**
  in force since **20 February 2026** targeting AI-generated content on platforms.
- **Australia:** the clearest adoption signal — **OpenAI partnerships announced 5 November 2026**
  with **UNSW Sydney, the University of Sydney, La Trobe and Adelaide University** to deploy
  ChatGPT Edu with curriculum integration, reaching tens of thousands of students.

**Opportunities.**
- **Fastest-growing region (~35% CAGR) and the largest single education deal in this pass:**
  Accenture + Google Cloud across **1,000+ Indian institutions** including agentic-AI
  curricula. That is the competitive benchmark — Globant should expect to bid against
  Accenture at national-programme scale here, not at campus scale.
- **Multi-jurisdiction compliance as a product.** A vendor selling across China, Japan,
  Singapore, India and Australia faces five different regimes plus EU extraterritorial reach.
  Policy-as-code in a LangGraph orchestration layer — jurisdiction-specific nodes for content
  labelling, disclosure and data residency — is a concrete, differentiated build.
- **Australia is in buying mode and has chosen a proprietary vendor.** The complementary
  position is the integration, change-management, curriculum and evaluation layer around
  ChatGPT Edu, plus `pedagogy-benchmark` as independent efficacy measurement.
- **China's labelling mandate** means any AI-generated courseware shipped there needs
  provenance marking in the generation pipeline, not bolted on afterwards.
- **India's scale plus deficit** makes offline-capable, low-cost delivery (Kolibri + Ollama on
  modest hardware) viable where cloud-per-seat economics are not.

### LATAM

**Regulatory picture — mostly pending, with the binding layer being data protection.**
- **Brazil:** **PL 2338/2023** passed the Senate in December 2024 but remains in the Chamber of
  Deputies; a vote targeted for late May 2026 was postponed, with reporting suggesting it
  resumes after the **October 2026 elections**. The binding baseline today is the **LGPD**,
  which already grants a right to request review of automated decisions — directly relevant to
  automated grading and admissions. **EBIA**, Brazil's AI strategy, names AI training
  programmes as a priority.
- **Mexico:** no comprehensive AI law. The proposed **Federal Law Regulating Artificial
  Intelligence** remains in Senate discussion with passage expected in 2026; amendments
  already enacted in 2026 are described as the first concrete binding obligations. A deepfake
  criminal reform is pending.
- **Peru:** **the first enacted AI law in Latin America**, with implementing regulation — the
  only LATAM jurisdiction where an AI-specific statute is actually operative.
- **Regional:** **UNESCO has launched an observatory of AI in education for Latin America and
  the Caribbean** — directly relevant institutional infrastructure.

**Opportunities.**
- **LGPD automated-decision review is the sharpest near-term hook.** Brazil already gives
  learners a right to request review of automated decisions. Any AI grading or admissions
  system deployed there needs a human-review workflow and an explanation trail **today** —
  not after PL 2338 passes. `edx-ora2` plus a logged human-override step is the concrete build.
- **Pre-regulatory positioning.** Brazil and Mexico will both legislate; institutions that
  build conformant now avoid a retrofit. The EU AI Act is the best available template, and
  EU-conformant design will largely satisfy whatever Brazil enacts.
- **Peru as the compliance pilot.** The one jurisdiction with an operative law — the natural
  place to prove a compliance methodology before the larger markets legislate.
- **Offline-first is a LATAM differentiator, not a limitation.** Kolibri (MIT) and
  Internet-in-a-Box address rural connectivity directly, and Chamilo's LATAM installed base
  means integration targets already exist.
- **Spanish and Portuguese pedagogical quality is measurable and under-measured.**
  `pedagogy-benchmark` is model-agnostic; running it for Spanish and Portuguese teacher-exam
  content would produce regionally specific efficacy evidence no competitor currently holds.
- **The honest constraint:** LATAM is the **smallest regional market (~$0.67B)** with the
  thinnest data. Position it as public-sector and ministry-scale programme work with equity-of-
  access framing, not as per-seat commercial SaaS.

### Global

- **Student adoption has already outrun institutional policy.** Inside Higher Ed (17 November
  2026) reports **eight in ten students** using generative or agentic AI routinely, and that
  students prioritise learning over having AI do the work for them. Against that, this pass's
  trends leg found only about **a quarter of faculty** reporting a formal institutional AI
  policy. The governance gap, not the technology gap, is the sellable problem everywhere.
- **The buyer is institutional.** Venture funding down ~89% from peak while institutional
  mandates multiply — services, integration and compliance, not product launches.
- **Open-source education AI is concentrated in university labs**, not startups: HKUDS,
  THU-MAIC and CAHLR produced every serious education-native agent verified this pass. That
  makes academic partnership a credible sourcing channel for Globant.

## Declared gaps

- **`eur-lex.europa.eu` is unreachable from this session** (`000`, as in prior passes). All EU
  AI Act specifics above rest on secondary sources and are marked as such. The education
  high-risk delay to 2 December 2027 and Regulation (EU) 2026/1744 should be confirmed against
  the primary text before use in a client deliverable.
- **No reliable per-region AI-in-education adoption rates were found** for any region. The
  regional figures above are market *size* estimates from low-authority publishers, not
  measured institutional adoption. This gap persisted across all four regional legs.
- **MENA and Africa are not covered by the mandated region vocabulary.** A University Agentic
  AI Lab (25–26 November 2026, University of Dubai) and the AIJRF programme surfaced in the
  news leg but have no bucket in the closed five-value region set, so they are recorded here
  rather than silently dropped.
- **APAC and LATAM investment data is thin to absent.** Deal-level data existed only for North
  America (median ~$9M) and Europe.
