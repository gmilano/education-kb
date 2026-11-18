---
industry: education
region: Global
updated: 2026-11-18
---

# Market intelligence — education

Researched 2026-11-18. Sources are named inline. Where estimates conflict, both are given
and the conflict is stated rather than averaged away.

## Market size — and why the numbers disagree

**Broad AI-in-education market, 2026 base year:** estimates cluster between **$9.6B and
$11.4B**, and diverge sharply on growth.

| Source | 2026 base | Forecast | Implied CAGR |
|---|---|---|---|
| Research and Markets | $10.6B | $42.48B by 2030 | 41.5% |
| Coherent Market Insights | $11.40B | $57.25B by 2033 | 16.8% |
| Precedence Research | $9.58B | ~$136.79B by 2035 | 34.52% |

**Agentic AI in education specifically** — a much smaller base, and the single widest
disagreement we found in any industry:

| Source | 2026 base | Forecast | Implied CAGR |
|---|---|---|---|
| Research and Markets | $2.1B | — | **4.5%** |
| Mordor Intelligence | $2.37B | $11.83B by 2031 | **37.92%** |

Two reputable firms differ by **8x on the growth rate of the same segment in the same
year**. Do not cite either alone in a client deck. The defensible statement is: *agentic
education AI is a ~$2.1–2.4B segment in 2026, roughly a fifth of the broader AI-in-education
market, and analysts do not agree whether it compounds at 5% or 38%.*

**AI tutors sub-segment:** $3.6B in 2026 → $17.7B by 2033 at 30.5% CAGR (Grand View, via
IdeaPlan). Mordor's framing is the useful one: **tutoring is the gateway purchase that seeds
broader platform penetration.** Sell the tutor, land the platform.

**Caveat on secondary sources.** Several widely circulated pages (x-pilot, TechRT) quote
outcome statistics such as "42% improvement in learning outcomes" and "54% higher test
scores" with no traceable primary study. They are excluded here. A claim about learning
gains needs a primary citation or it does not go in a client deck.

## Key players

**Proprietary / commercial.** Microsoft launched **Microsoft Elevate for Educators**
(Jan 2026). Khan Academy (Khanmigo) and Duolingo are the most-cited tutoring deployments,
though the frequently repeated "50M+ students" figure is unverified. Instructure (Canvas),
Anthology, Ellucian and PowerSchool hold the North American institutional stack.

**Open-source institutional.** The credible AI-in-education engineering is coming out of
universities rather than startups: **TU Munich** (Artemis, EduTelligence, Pyris — MIT),
**HKU** (DeepTutor — Apache-2.0), **Tsinghua** (OpenMAIC — MIT), **UC Berkeley** (OATutor —
MIT), **ECNU** (EduWork — Mulan PSL v2), **Moodle HQ** (wiki-rag — BSD). That concentration
is the central strategic fact of this KB: the best permissive assets are academic, and
academic projects welcome implementation partners.

## Opportunities by region

### North America

**Regulatory posture: state-level, binding, and fragmenting fast.** At least **25 states**
have enacted or introduced K-12 AI legislation as of spring 2026 (MultiState); bill counts
vary by tracker — one cites 134+ bills across 31 states, another 1,500+ AI-related bills
overall. There are **zero binding federal AI curriculum standards** as of May 2026. Named
statutes:

- **Idaho SB 1227** — statewide K-12 AI framework, AI-literacy standards, bar on AI replacing
  human teachers; AI literacy embedded in general education for all incoming undergraduates
  from Fall 2026.
- **Oklahoma SB 1734** — mandatory teacher review of AI output, parent opt-out; the May 2026
  law **prohibits AI tools used solely for grading, discipline or student promotion**.
- **Maryland SB 720** — state guidance plus local AI policies and a statewide K-12 AI
  collaborative.
- **Ohio** — districts must adopt an AI framework by **1 July 2026**.
- **New York A 9190** (proposed) — would restrict direct student AI use to grade 9 and above.

Federal activity is guidance and funding: the Department of Education issued *Artificial
Intelligence in K-12 Education* with UNESCO and named AI a grantmaking priority; the
**K-12 AI Literacy and Readiness Act of 2026** advanced out of House committee. District-level
bans exist too (Katy ISD bans generative AI chatbots for K-6).

**Opportunity.** The binding constraint is *human oversight you can prove*, not model
quality. Oklahoma's "no AI-only grading" rule and the general teacher-review mandates make
**auditable human-in-the-loop architecture the product**. Build on
`virtualryder/edu-ai-agents` (MIT — deny-by-default auth, PII masking, tamper-evident audit,
FERPA/COPPA/IDEA/ADA alignment, deterministic rubric scoring rather than LLM grading) and
**Ed-Fi-ODS** (Apache-2.0), the K-12 data standard across most US states. A
**50-state policy-conformance layer** — one AI tier, per-state policy configuration — is a
genuinely defensible studio asset, because fragmentation is the client's actual pain.
Higher-ed second play: Canvas is dominant, so `canvas-mcp` (MIT) plus CAS SSO is the fastest
institutional pilot.

### EMEA

**Regulatory posture: one regime, and a deadline that moved.** The EU AI Act became generally
applicable **2 August 2026**. Critically, the 2026 Digital Omnibus — cited as **Regulation
(EU) 2026/1744** — **postponed the Annex III high-risk obligations for stand-alone education
systems from 2 August 2026 to 2 December 2027**. Sources conflict on this (several
pre-Omnibus pages still say August 2026), so confirm against the regulation text before
advising a client. What is in force now:

- **Emotion recognition in schools is banned** (since February 2025, not postponed).
- **Article 50 chatbot transparency duties apply from August 2026** — a student must be told
  they are talking to an AI.
- High-risk categories when they land: **admissions, assessment/learning-outcome
  determination, educational-level assignment, and exam monitoring**.

Players and signals: the **European University Association** (Jan 2026 report) urges
considered adoption and **favours European LLMs** — a sovereignty preference with
procurement consequences. Finland's **Generation AI** project (Prof. Matti Tedre, University
of Eastern Finland) won the 2026 European Digital Skills Award. The **Russell Group's** five
AI principles remain the UK university reference model. Most institutions are in
pilot/pre-compliance mode rather than enforcement.

**Opportunity.** **The 2 Dec 2027 postponement is a 12-month selling window, not a reprieve** —
institutions now have time to do conformity properly, and budget-holders know the date. Sell
**AI Act conformity-by-construction**: Annex III classification, technical documentation,
human-oversight design and logging, built in from the start. The sovereignty preference makes
**self-hosted inference non-optional**: `ollama`/`vllm` plus `litellm` plus `qdrant`, no
US-hosted API in the data path. The permissive EMEA assets are unusually strong —
**Artemis + EduTelligence + Pyris (all MIT, TU Munich)** is the best licence-clean, EU-origin,
AI-capable LMS stack in existence, and OpenOLAT (Apache-2.0) and ILIAS serve the
German-speaking public sector. Proctoring and admissions work should be approached as
high-risk-system engineering with a 2027 compliance date, priced accordingly.

### APAC

**Regulatory posture: four incompatible regimes, no regional harmonisation.**

- **South Korea** — the **AI Basic Act in force since 22 January 2026**; described as the
  closest analogue to the EU AI Act, though shorter. The most comprehensive regime in APAC.
- **China** — regulates by service type rather than one statute: recommendation algorithms,
  deep synthesis, generative AI services, and **labelling of AI-generated content**. The
  amended **Cybersecurity Law (in force 1 January 2026)** carries China's first AI clause.
- **Japan** — promotion-first: a promotion-focused AI law backed by voluntary guidelines. No
  education-specific AI policy surfaced in this pass.
- **India** — no dedicated AI law yet; in **July 2026** the government signalled it may pursue
  one. Amended **IT Rules require prominent labels and provenance markers on AI-generated
  content from 20 February 2026**.

**The cautionary case is Korea's.** It attempted a national rollout of AI-powered digital
textbooks in schools from 2025 and, after parental and teacher backlash, **walked it back to
optional "educational material" status within a year**. This is the most instructive
deployment failure in the industry: the blocker was stakeholder consent, not technology.
Any APAC pilot plan that lacks a teacher- and parent-consent workstream is repeating it.

Market structure: China's tutoring crackdown reshaped edtech, with non-academic STEM/coding/AI
tutoring rebounding — **TAL pivoted into AI learning hardware**. India's **PhysicsWallah**
launched its own AI tutor.

**Opportunity.** APAC is where the best open education agents are being built — **DeepTutor
(HKU, Apache-2.0)** and **OpenMAIC (Tsinghua, MIT)** are the two most significant open
tutoring assets globally, and both are permissive. A studio can be an implementation partner
for assets it did not have to fund. Content labelling is a concrete, dated engineering
requirement in both China and India — build provenance marking into generated courseware by
default. `MinerU` (Apache-2.0) handles CJK textbook extraction better than Western-trained
parsers. Korea is a compliance-led market under the AI Basic Act; Japan's voluntary posture
makes it the lowest-friction pilot geography in the region.

### LATAM

**Adoption is genuinely ahead of the OECD — governance is not.** This is the region's defining
asymmetry, and it is quantified:

- **Teacher AI use (TALIS 2024):** Brazil **56%**, Chile **55%**, Colombia **53%**, Costa Rica
  **52%** — against an **OECD average of 36%**. LATAM teachers use AI more than their OECD
  peers.
- **The governance gap:** in Brazil, **53% of school administrators use AI but only 22% report
  school guidelines** on its use. In higher education, **UNESCO IESALC finds 87% of
  universities already use AI but only 26% have a formal strategy**.
- **IDB** reviewed 193 regional initiatives: **59% used generative AI**, many combining several
  modalities.
- UNESCO: AI is spreading quickly but unevenly, with institutional rules lagging.

**Regulation.** **Brazil** is the regional bellwether — **PL 2338/2023**, a comprehensive
horizontal statute whose text covers education applications, remains **pending**. **Mexico**
is behind: a 2018 national AI strategy under revision, and **no Mexican AI bill enacted as of
early 2026**.

**Players and funding.** Brazil accounts for **nearly half** of HolonIQ's 2026 Latin America
EdTech 100 cohort and the clear majority of deal and award activity; named AI companies include
**Teachy** (AI lesson preparation) and **Vetto** (recently raised). In Mexico, **Ginia**
(AI-driven employability), **Talisis** and **Mattilda** (post-secondary and financing).
**Google.org committed $4.6M** with the **Raspberry Pi Foundation** to scale the Experience AI
curriculum across **nine countries**, targeting **1.25M students by 2028**.

**Opportunity.** The 53%-use/22%-guidelines gap is the offer: **governance and enablement, not
tooling**. Institutions are already using AI and know they are exposed. A packaged
"AI-use policy + teacher training + audit logging" engagement sells against a problem the
client can already see, and it is deliverable in weeks. Brazilian public-sector work has a
specific substrate — **i-Educar (LGPL)** is built around Brazilian regulatory requirements and
is the right SIS starting point. Cost discipline matters more here than elsewhere: `litellm`
budget caps plus local `ollama` inference keep per-student cost predictable in
currency-volatile markets. Equity/connectivity work is a real segment — **Kolibri (MIT)**,
**Internet-in-a-Box (LGPL)** and **Project NOMAD (Apache-2.0)**. Note the build gap: there is
almost no LATAM-origin open education agent (only `warleysr/ankipa`, an Anki add-on), so
expect to localise APAC- or EMEA-origin assets — and note that Spanish/Portuguese pedagogical
localisation is itself billable differentiation.

### Global

Cross-regional plays that do not depend on one jurisdiction.

- **Licence-clean AI-on-LMS.** Open edX, Canvas and Moodle are AGPL/GPL. A client wanting a
  proprietary derivative needs the permissive path: **Artemis (MIT)**, **Kolibri (MIT)**,
  **Oppia (Apache-2.0)**, **OpenOLAT (Apache-2.0)**. Licence triage is a billable first
  engagement in its own right, and it is the question most often got wrong.
- **LTI 1.3 as a multiplier.** Build the AI tool once against `ltijs` (Apache-2.0) or `tsugi`
  (Apache-2.0) and it ships into every compliant LMS. One build, many clients.
- **Evidence of efficacy.** Every regulator and procurement office is converging on
  "show me it helped". An LRS (`lrsql`, Apache-2.0) plus `pedagogy-benchmark` (MIT) plus
  `promptfoo` (MIT) regression gates is the measurement tier almost no vendor ships.
- **The unserved category: SIS and registrarial agents.** Tutoring, grading and content
  generation are crowded. Enrolment, timetabling, transcripts and financial aid have **no
  credible open agent anywhere**. Highest defensible-IP opportunity in the industry — with
  the caveat that admissions and financial-aid decisioning are EU Annex III high-risk and
  restricted under several US state laws, so build it oversight-first.

## Declared gaps

- **No 2026 market-share data for AI education providers** was found in any region. Market
  *size* estimates exist; vendor *share* does not.
- **No AI-in-education policy for Japan** surfaced, despite a targeted APAC search. Japan has
  an AI law; whether it reaches classrooms is unknown from this pass.
- **No Africa or Middle East specific leg** was run — both fall inside "EMEA" in this KB's
  closed region vocabulary, and the EMEA evidence above is overwhelmingly European. An EMEA
  engagement outside Europe is **not** covered by this file.
- **Star counts and repo-popularity metrics are absent**; no reachable route (see
  `agents/top.md`).
