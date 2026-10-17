---
industry: education
region: Global
updated: 2026-10-17
---

# Market map — Education

> Key players, regulatory ground truth and opportunities **placed by region**.
> Sourced from web research on 2026-10-17. Vendor-sourced figures are marked; they are
> carried because they are the only numbers available, not because they are reliable.

## Market size — and a warning about these numbers

| Figure | Value | Source grade |
|--------|-------|--------------|
| North America share of global AI-in-education market | **36%** | aggregator |
| AI in education, North America | $3.68B (2026) → $32B (2030), 31.1% CAGR | **vendor/aggregator — unverified** |
| US K-12 teachers who used AI tools in SY 2024-25 | **60%** (32% at least weekly) | survey, reported secondhand |
| LATAM university students using AI | **92%** | Digital Education Council |
| Mexican university students/faculty using GenAI daily | **>60%** | SEP national survey, Apr 2026 |

**Read these as direction, not as magnitude.** Every market-size figure located this pass
traces back to a vendor or aggregator blog; none traces to a primary research house
document we could open. Prior versions of this file published a five-row market-size table
with named research houses — those attributions did not survive re-checking and have been
removed rather than recycled.

## Global players

| Player | Type | AI position | Opening for Globant |
|--------|------|-------------|---------------------|
| **Instructure (Canvas)** | Commercial SaaS | Native AI grading and content assistance | Migration path to Open edX/Moodle with an equivalent AI layer the client owns |
| **Blackboard / Anthology** | Commercial SaaS | Scale in North American higher ed | Replacement engagements; the incumbent's lock-in is the pitch |
| **Khanmigo (Khan Academy)** | Nonprofit | Socratic tutoring at national scale | UX reference, not a technical base — it is not open source |
| **Duolingo** | Consumer | Roleplay and voice tutoring | The consumer bar for engagement that institutional work gets compared against |
| **Moodle HQ** | Open source steward | First-party AI subsystem since 4.5, provider-pluggable | Partner, not competitor: the subsystem's gaps (question generation, conversational practice, SCORM) are studio work |
| **Microsoft Education** | Cloud/Enterprise | Agentic admin workflows + tutoring, Azure-coupled | Globant as the cloud-neutral implementer |
| **TUM / `ls1intum`** | Academic | Artemis: automated feedback at university scale, MIT | Adopt and extend; the licence invites it |
| **Selleo** | Vendor + OSS | Mentingo, MIT AI-native LMS | Build-on or partner for corporate L&D |

## Regulatory ground truth

This is the part of the file with the longest shelf life, and the part most worth getting right.

| Jurisdiction | What is actually in force | Date |
|--------------|---------------------------|------|
| **EU** | AI Act **transparency** duties live: users must be told they are dealing with an AI system; deepfakes disclosed | **2026-08-02** |
| **EU** | AI Act **high-risk** obligations for education **delayed** from 2026-08-02 to **2027-12-02** by the AI omnibus amendments (in force 2026-07-27) | **2027-12-02** |
| **EU** | In-scope education systems: those determining **access**, assessing **learning outcomes**, or influencing an individual's **educational path** (admissions, evaluation, exam scoring) | — |
| **US federal** | `H.R. 8747` K-12 AI Literacy and Readiness Act advanced out of House Education & Workforce, largely on party lines | 2026-07-21 |
| **US states** | **134 AI-in-education bills across 31 states** in the 2026 session | 2026 |
| **California** | `AB 1159` prohibits using student data to train AI models | 2026 |
| **Oklahoma, Maryland** | Require human oversight; bar AI from high-stakes decisions about students | 2026 |
| **New York City** | One-year moratorium on student-facing AI through 8th grade | 2026 |
| **Canada** | "AI for All" strategy incl. national AI literacy push — **strategy, not statute** | 2026-06-04 |
| **Brazil** | MEC/SEGAPE *Referencial para o Uso e Desenvolvimento Responsáveis de IA na Educação*; emphasises **digital sovereignty and national solutions** | 2026-03 |
| **Brazil** | MEC *IA na Educação Básica: Caminhos para o Currículo e a Prática Docente* | 2026-04 |
| **Brazil** | MEC reported to be preparing a **national resolution** on AI in teaching, based on CNE guidelines — **not yet published in the Diário Oficial** | reported 2026-10-15 |
| **Brazil** | `PL 2338` would be the first comprehensive AI law in Latin America — risk classification, mandatory transparency, data-protection requirements | in process |
| **India** | AI + computational thinking **mandatory from Class 3 in all schools**, academic year **2026-27**; aligned to NEP 2020 / NCF 2023; ₹500 crore AI Centre of Excellence for Education (Budget 2025-26); curriculum led by IIT Madras | AY 2026-27 |
| **China** | **Beijing**: compulsory 8 hours/year of AI education, primary and secondary, since 2025; Guangdong on its own schedule; national rollout **uneven** | 2025→ |
| **Singapore** | AI training for teachers at all levels incl. those in training; teacher-supervised AI in the Student Learning Space (SLS) | by 2026 |
| **Japan** | AI Promotion Act (framework law); Cabinet adopted a new AI Basic Plan | 2026-07 |
| **Mexico** | **No general AI law.** Sectoral patches; SEP published a 10-action roadmap after its national survey | 2026-04 |

## Opportunities by region

### North America

The largest market (36% share) and by far the most fragmented regulatory surface:
134 bills across 31 states means a national product does not exist — **compliance
configurability is the product**.

- **Per-jurisdiction policy enforcement as a feature.** `AB 1159`-style data-training bans,
  Oklahoma/Maryland human-oversight mandates and NYC's grade-banded moratorium are
  contradictory by design. Moodle 5.1's per-course/per-activity AI toggles map almost exactly
  onto this requirement; wire district policy to those toggles and the audit trail writes itself.
- **Human-in-the-loop assessment.** Where AI is barred from high-stakes decisions, the
  sellable architecture is `Artemis` (MIT, automated *feedback*) plus explicit teacher sign-off
  — not autonomous grading. `Claw-ED`'s teacher-reviewed posture is the right default.
- **Incumbent migration.** Canvas and Blackboard renewals are the natural trigger for an
  Open edX or Moodle migration with a client-owned AI layer.
- **AI literacy curriculum delivery.** `H.R. 8747` would let schools spend federal funds on AI
  curriculum. If it passes, procurement follows, and `instructional_agents` (MIT) is the
  content-generation engine for exactly that.

### EMEA

The clearest regulatory calendar in the world, and a **14-month window** before it closes.

- **The window is the offer.** High-risk obligations for education now bite on
  **2027-12-02**, not August 2026. Clients who read the delay as a reprieve will arrive late;
  the engagement is a compliance-by-design build *during* the window — classification of
  in-scope systems, human-oversight design, documentation.
- **Transparency is already live (2026-08-02).** Disclosure that a learner is talking to an
  AI, and deepfake disclosure, are obligations **today**. This is a short, concrete,
  immediately billable remediation scope.
- **Provenance as a procurement requirement.** `lineage-skill` (Apache-2.0) keeps generated
  material tied to its sources — the shape of evidence an AI Act file needs.
- **Sovereign deployment.** Moodle's AI subsystem pointed at local Ollama/vLLM means no
  student prompt leaves the member state. Pair with EMEA-origin, permissive bases:
  **OpenOLAT** (Apache-2.0, CH), **Artemis** (MIT, DE), **Richie/Marsha** (MIT, FR).
- **The market is ready**: nearly **two-thirds of European education systems** already have
  an AI strategy, guidance or policy framework, and two European Commission reports
  (2026-09-22) describe generative AI as a **mainstream** tool in EU education.

### APAC

The largest mandated demand anywhere, and the thinnest open-source supply.

- **India is the single biggest curriculum event in the world**: AI and computational
  thinking compulsory **from Class 3 in every school from AY 2026-27**. That is a national
  content, teacher-training and assessment problem with a legislated deadline.
  `instructional_agents` (MIT) for materials at multilingual scale; `pykt-toolkit` for
  measuring whether any of it lands.
- **Teacher capacity is the bottleneck, not the models.** India is standing up curriculum
  through IIT Madras; Singapore is training every teacher including trainees by 2026. Teacher
  co-pilots (`Claw-ED`, `instructional_agents`) sell better here than student-facing tutors.
- **China's unevenness is the opportunity.** Beijing mandates 8 hours/year; the national
  rollout varies by province. Provincial-grade delivery and measurement is an unmet need,
  with the obvious caveat that China's AI rules are the region's most binding (registration,
  content controls, localisation).
- **Singapore as the regional reference deployment.** Highest adoption in APAC, a
  government platform (SLS) built on teacher supervision, and voluntary frameworks
  (AI Verify) that make piloting cheap. Win here, cite everywhere.
- **Gap, stated plainly:** no APAC-origin open-source education platform or agent with
  meaningful adoption surfaced this pass. APAC engagements will be localisation and
  integration on non-APAC bases.

### LATAM

The region where the policy direction most favours what open source actually is.

- **Brazil's digital-sovereignty framing is a direct mandate for open source.** MEC/SEGAPE's
  March 2026 *Referencial* explicitly calls for national solutions that reduce dependence on
  global platforms. A self-hosted Moodle or Chamilo with local-model inference is not a
  cost compromise there — it is the stated policy preference.
- **Move before the resolution lands.** MEC is reported (2026-10-15) to be preparing a
  national resolution on AI in teaching based on CNE guidelines, not yet in the Diário
  Oficial. Institutions that build to the existing *Referencial* now will be compliant by
  construction; this is the moment to be in the room.
- **Teach-about-AI before teach-with-AI.** Brazil's MEC guidance orders it that way
  deliberately. Sell AI **literacy** curriculum and teacher formation first; student-facing
  tutors second. Pitching it in the other order misreads the buyer.
- **Mexico's gap is quantified and it is teacher training.** SEP's April 2026 survey:
  **76% of professors make materials with AI but only 36% teach students to use it**, and
  **9 in 10 want training**. There is **no public national AI competency standard for
  teachers**. MXN 284.1M is allocated to teacher professional development in 2026, and SEP
  announced three national encuentros on technology, phones and AI in schools (July 2026).
  A teacher-formation programme with a measurable competency framework is the highest-fit
  offer in the region.
- **Build on the installed base.** Chamilo has the deepest LATAM public-sector footprint;
  Moodle dominates the large public universities. Neither needs replacing — both need an
  agentic layer, delivered through an LTI tool so the platform licence stays untouched.
- **Adoption is not the obstacle.** Brazil and Mexico lead regional AI adoption (reported
  76% / 70%, August 2026) and 92% of LATAM university students already use AI. Governance
  and teacher capability are the obstacles, and both are services work.

## Declared gaps

- **Japan: no school-level education-AI adoption or policy data located.** Searches returned
  framework-law and higher-education-ethics material only. An informed gap: do not model
  Japan from the APAC aggregate.
- **No education-specific regulatory detail for Canada, Mexico at federal level, or most of
  APAC beyond the four countries above.** What exists is general AI regulation, cited as such.
- **Every market-size number in this file is vendor- or aggregator-sourced.** None was
  confirmed against a primary research document. Treated as direction only.
- **Estado de México's April 2026 education reform** appeared in search results but the
  substantive provision was truncated in every source located. Recorded as unverified rather
  than guessed.
