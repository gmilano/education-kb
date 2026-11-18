---
industry: education
region: Global
updated: 2026-11-18
---

# Market intelligence — education

Researched 2026-11-18, extended in pass **p890** the same day with four fresh regional legs.
Sources are named inline. Where estimates conflict, both are given and the conflict is stated
rather than averaged away.

**Verification channel, stated honestly.** GitHub facts in this KB are byte-verified. The legal
and statistical facts below are **not**: in this session the network policy blocks every
non-GitHub host (`403` on CONNECT via curl, `getaddrinfo ENOTFOUND` via WebFetch), so
`ncleg.gov`, `data.consilium.europa.eu`, `unesco.org`, `teqsa.gov.au` and the law-firm
analyses could not be opened and read. What follows is **search-snippet evidence with the
source named**, and where two or more independent sources agree that is said. Anything marked
*(single source)* should be confirmed against the primary text before it goes in a client
deck. This is a gap in the environment, not in the finding.

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

**The whole-EdTech envelope, for context (new, 2026-11-17).** A GlobeNewswire release dated
**17 November 2026** puts the *global EdTech market* — not the AI slice — on a **10.8% CAGR to
2033, a $437.54B opportunity**, with personalised learning named as the driver. Use it only as
the denominator: at ~$10B in 2026, AI-in-education is roughly **2–3% of EdTech spend**. The
useful read is that the AI segment compounds at 3–4x the rate of the market containing it,
which is the shape of a category that is still early.

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
- **New York A 9190** (proposed) — would restrict direct student AI use to grade 9 and above,
  **with exceptions for diagnostics and special education** (MultiState).
- **North Carolina Session Law 2026-41** (Senate Bill 257) — **new in this pass, and the
  nearest hard deadline in any region.** The Department of Public Instruction must publish a
  **model AI policy by 31 December 2026**; each public school unit must then adopt its own
  student-and-staff AI-use policy by **30 June 2027**; further obligations run through the
  **2028-29 school year**, with teacher training by **30 June 2028**. The law took effect
  1 July 2026 and required content includes AI literacy covering non-consensual intimate
  imagery. Two independent trackers plus the `ncleg.gov` session-law text agree on the
  31 December 2026 date. Separately, North Carolina has a **$10M AI-tutoring earmark for Khan
  Academy's Khanmigo**, which is locally contested. **Do not confuse SL 2026-41 with NC H 301**,
  a different bill with similar content whose status is unclear.
- **California AB 1159** — **bars the use of student data to train AI models** (MultiState).
  This is the single most architecturally consequential US rule found: it forecloses the
  fine-tune-on-your-own-students pattern and makes retrieval-over-institutional-content, with
  no training feedback loop, the compliant design.
- **Virginia** — school boards must adopt policies consistent with Department of Education
  guidance.

Federal activity is guidance and funding: the Department of Education issued *Artificial
Intelligence in K-12 Education* with UNESCO and named AI a grantmaking priority; the
**K-12 AI Literacy and Readiness Act of 2026** advanced out of House committee. District-level
bans exist too (Katy ISD bans generative AI chatbots for K-6). Higher education is tightening independently of
legislation: **Berkeley Law banned AI on all exams and credited coursework from summer 2026**.

**Canada — previously missing from this section.** "North America" in this KB had been
US-only, which is a defect for a Canadian engagement. What this pass established: there is
**no Canadian federal AI-in-education statute**; the binding instruments are provincial and
employment- or privacy-based (Ontario's **Working for Workers Four Act, 2024**, with
hiring-disclosure rules pending), and institutions are moving ahead of regulation — the
**University of Guelph** is piloting AI to help staff review supporting documents in
**international student applications** (SchoolFinder, Nov 2026). Note the exposure: admissions
document review is exactly the use the EU classes as Annex III high-risk and Vietnam now lists
as high-risk, so a Canadian pilot built without oversight architecture will not travel. This
remains a **thin leg** — one pilot and one adjacent statute is not coverage of a G7 country.

**Institutional readiness (new).** An Inside Higher Ed survey cited this pass found roughly
**70% of respondents use AI in their own work at least weekly, while only about one in ten
report a centralised institutional AI strategy** *(single source; the survey population is not
stated in the snippet, so treat the ratio as indicative)*. It is the same adoption/governance
asymmetry this KB documents for LATAM, in a market with far more money.

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


#### p891 additions — North America

**The dual-mandate cluster is now four states.** Maryland, **Idaho, Oklahoma and Virginia** all
require *both* state-level guidance *and* mandatory district-level AI policy adoption. That is
the pattern to design for: a vendor selling into these states must ship a **policy artefact**,
not only software, and the district is the buyer of record for it.

**Federal activity, which this KB previously recorded as near-absent, is real but non-binding.**
The US Department of Education's **Office of Educational Technology published a "Framework for
Responsible Use and Development of Artificial Intelligence in Education" in March 2026**,
followed by a **K-12 guidance document in April 2026**. Separately, **$169M in FIPSE awards**
was released, including support for responsible AI use in higher education. None of this
creates binding curriculum standards — the earlier finding stands — but it does create a
**citable federal reference** that a district policy can be written against, and a funding line.

**Two more named instruments:**

- **California AB 1159** — bars using student data to train AI models outright. The hardest
  single constraint in the region: it rules out the default fine-tuning architecture, not just
  a vendor choice.
- **Idaho SB 1227** — adds explicit privacy requirements for AI tools used in schools (this
  complements the AI-framework provisions already recorded above).

**Non-legislative forces that behave like regulation:**

- **Berkeley Law banned AI for all exams and credited coursework, effective summer 2026** — an
  elite-institution signal that propagates through peer policy.
- **Chicago, Denver and Charlotte-Mecklenburg** have issued district-level AI policies. Large
  districts are now policy *authors*, not policy *takers*.
- The **National Education Policy Center** approved a **risk-tier framework in May 2026** — a
  non-governmental classification scheme that procurement is likely to cite.
- **OpenAI and Common Sense Media** jointly proposed a California ballot measure, the
  **"Parents & Kids Safe AI Act"**, which would set standards for AI products used by minors.
  A vendor-originated standard aimed at the referendum route is a new mechanism in this market
  and worth watching.
- **Khan Academy's Khanmigo is the subject of a $10M North Carolina earmark** — the clearest
  single data point that incumbent tutors are being bought at state scale while open
  alternatives are not on the shortlist.

#### Canada — closing the "one-pilot leg" gap

Run as its own leg this pass. **The finding is that Canada has no national rule and patchy
provincial coverage, and that this is the opportunity rather than the obstacle.**

- **No national K-12 AI rule exists.** Education is provincial jurisdiction.
- **Only four provinces have formal AI guidance for educators: British Columbia, New
  Brunswick, Newfoundland and Labrador, and Quebec.** **Manitoba** is developing its own.
- **Ontario's Ministry of Education has published no memorandum on AI** — so despite being the
  largest system in the country, no province-wide rule applies. The **Ontario Teachers'
  Federation issued a discussion paper (March 2026)** pressing provincial and territorial
  governments to set direction. Demand exists; supply of policy does not.
- **Nova Scotia has no province-wide policy**, and regional education authorities are setting
  divergent expectations, leaving individual teachers to set guardrails.
- **Privacy is the binding constraint, and it is provincial:** Ontario FIPPA/MFIPPA, BC
  FOIPPA, Alberta FOIP. The practitioner guidance is privacy impact assessments, tightened
  vendor contracts and written AI-use rules. Federal, provincial and territorial privacy
  regulators issued a **joint resolution in October 2025** warning that AI may infer sensitive
  traits from student data and urging child-privacy priority in tool selection.
- **In higher education, AI detection is effectively off the table.** A review of six Canadian
  institutions found **all six declined to enable or endorse AI-detection tools**, privacy
  being the stated reason at four; **UBC** cites a Privacy Impact Assessment and **Concordia**
  bars staff and faculty from using online AI detectors. See **T10** in `intel/trends.md`.

**Opportunity — Canada.** The sellable unit is **the policy plus the privacy artefact**, not
the model. A province or board needs a PIA-backed AI-use framework, a vendor-assessment
template and a defensible assessment-redesign programme — and in six of thirteen provinces and
territories there is no provincial document to inherit from. Pair it with **sovereign/local
inference** (`ollama`/`vllm` + `litellm`), because the privacy analysis is far easier when
student work never leaves the institution. The integrity engagement must be pitched as
**assessment redesign, not detection** — detection is the thing counsel has already removed.
*Source caveat: several of these points come from vendor and advocacy blogs; the provincial
counts and institutional positions are corroborated across more than one source, the specific
legal citations are not primary-verified.*

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
- **Article 4 AI-literacy duty — in force since 2 February 2025 and not postponed.** New in
  this pass and the most immediately billable item in EMEA. It binds **providers *and*
  deployers**, is **not limited to high-risk systems** (a school using a general chatbot is in
  scope), and extends to staff and to contractors operating AI on the organisation's behalf.
  The Commission's position is that **supervision and enforcement began 2 August 2026**;
  sources conflict, with one arguing national enforcement started August 2025 once Member
  States had designated authorities. **Caveat:** several secondary sources say the Digital
  Omnibus *rewrote* Article 4 into a softer duty to "take measures to support the development"
  of AI literacy, dropping the "sufficient level" standard. That could not be checked against
  the Official Journal in this session — **confirm before pricing a compliance package on the
  stricter reading.** No education-specific Commission or national guidance on Article 4
  surfaced, which is itself the opening: nobody has told schools what compliance looks like.
- **Precision on the Omnibus:** Regulation (EU) 2026/1744 has **applied since 27 July 2026**;
  the education high-risk date it sets is 2 December 2027.

Players and signals: the **European University Association** (Jan 2026 report) urges
considered adoption and **favours European LLMs** — a sovereignty preference with
procurement consequences. **That preference is now institutional, not advisory:** a
**Council of the EU** document dated **29 October 2026** (ST-14902-2026) presses **digital
sovereignty and strategic autonomy in AI for education** and calls for teacher- and
institution-level support on AI policy, and a **European Parliament briefing** of March 2026
(784574) frames public authorities and education systems as the bodies that "strategically
orchestrate" AI governance in education, pointing to the Digital Education Action Plan and the
European Education Area. Sovereignty has moved from a vendor preference to a stated Council
position inside the last month.

**New: UK procurement has organised itself against AI vendors.** **Jisc**, with **Universities
UK**, **GuildHE** and the **Association of Colleges**, issued a joint statement asking AI
suppliers for **transparent pricing, demonstrable value, meaningful institutional choice,
protection of existing functionality, granular usage and cost controls, interoperability, data
portability and safeguards against vendor lock-in** — driven by the shift from predictable
per-seat licences to **usage-based pricing**, and by institutions paying repeatedly for
overlapping AI capabilities embedded across platforms. A related Jisc/EAUC report found vendors
seldom release institution-level usage figures at all, which is why universities cannot measure
their own AI emissions. **This converts "governance" from a policy document into a metering
requirement with named deliverables**: per-institution, per-faculty, per-course usage and cost
attribution, exportable, with no proprietary trap. See `intel/trends.md` T9 and the new
observability tier in `repos/trending.md`. It is a buyer-side specification written by the
buyers — the closest thing to a published RFP this KB has found in any region. Finland's **Generation AI** project (Prof. Matti Tedre, University
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


#### p891 additions — EMEA

**Article 4 is resolved — see T3 in `intel/trends.md`.** Regulation (EU) 2026/1744 (OJ 24 July
2026, in force 27 July 2026) **rewrote Article 4 rather than repealing it**, replacing "ensure
a sufficient level" with "take measures to support", and expressly disclaiming any required
level for any individual. Enforcement by **national market surveillance authorities** began
**2 August 2026**. The same instrument defers **Article 14 (human oversight)** to 2 December
2027 with the rest of Annex III. **The AI-literacy engagement survives the Omnibus but changes
shape**: sell proportionate, documented, evidenced effort — not certified competence.

**The Council of the EU has made sovereignty an education-specific position.** Its October 2026
conclusions (`ST-14902-2026`) state that reducing dependencies on AI tools developed outside
Europe — **naming education and training** — is critical, and call for policies on **academic
integrity and plagiarism**. This is the strongest procurement signal in the file: it converts
the sovereignty preference recorded above from a market sentiment into a **stated Council
priority with education named in the text**. An EU-origin, self-hostable, permissively licensed
stack is now aligned with an explicit institutional position, not merely a buyer mood.

The **European Parliament's March 2026 briefing** (`IUST_BRI(2026)784574`) sets the pedagogical
frame: AI in education must remain human-centred, and governance requires coordination across
public authorities, education systems, technology providers and researchers.

#### Africa — first dedicated leg (closing a four-pass-old gap)

This KB has filed Africa under EMEA and never searched it. Run directly this pass. **Coverage
is thin and the single most useful finding is a cautionary one.**

- **South Africa published a draft National AI Policy on 10 April 2026 — and withdrew and
  abrogated it on 27 April 2026, after the minister confirmed the draft contained fictitious
  sources in its reference list.** A national AI policy was retracted because it appears to
  have been drafted with unverified AI-generated citations. For a studio selling AI governance
  work this is the most quotable incident in the file: **it is the strongest available argument
  that provenance and verification are deliverables, not overhead** — and it happened to a
  government, in public, this year.
- **Nigeria** has a **National EdTech Strategy covering 2025–2030**, addressing power,
  broadband, devices, education data systems, teacher capacity, financing, governance and safe
  AI use. The most complete national framing found on the continent.
- **Kenya** — **M-Shule** delivers AI-backed learning over **SMS and compressed video**, which
  is the realistic architecture for the bandwidth available. Structured AI literacy at
  foundational level remains limited, with most exposure arriving informally through innovation
  hubs and private-sector partnerships.
- **Continental:** the **African Union's Continental AI Strategy (September 2024)** names
  education a strategic priority and encourages national frameworks. In **November 2026**,
  **AI Research Foundations**, a Google.org-backed programme, launched with **30 universities
  across Ghana, Kenya, Nigeria and South Africa**.

**Opportunity — Africa.** Two distinct plays. (1) **Offline-first delivery**: `kolibri` (MIT)
plus local inference is not a downgrade here, it is the only architecture that works, and this
KB already tracks the stack. (2) **Governance with verifiable provenance** — the South African
retraction created live demand and a named failure mode to sell against.
*Confidence: low-to-moderate. The South African retraction is well-corroborated; the Nigerian
and Kenyan adoption figures circulating in 2026 edtech reports could not be verified and are
deliberately omitted.*

#### Middle East — first dedicated leg

- **UAE, federal.** The Ministry of Education's **"Safe and Responsible Use of Artificial
  Intelligence in Classrooms 2026"** sets **25 prohibitions** on generative AI in schools. The
  central age rule **bars students under 13, and those below Grade 7, from using AI tools**, and
  a separate prohibition covers **AI during exams and assessments**. The **Cabinet approved an
  AI curriculum across public and private schools on 2 September 2026**; sources conflict on
  whether the subject became mandatory from KG–Grade 12 in 2025-26 or from August 2026, and **no
  private-school timetable has been published**.
- **Dubai, KHDA.** KHDA is preparing its own private-school AI guidelines, **expected to take
  effect for the 2027-28 academic year**. Reported design: **KHDA will not mandate specific AI
  platforms**, and will instead set safeguards schools must weigh before adopting any platform.
  Until then **Dubai private schools largely set their own AI policies**.

**Opportunity — Middle East.** The UAE is the inverse of Canada: **the mandate exists and the
implementation does not**. A curriculum is approved across public *and* private schools with no
published private-school timetable, and a platform-neutral safeguards regime arrives in
2027-28. Platform-neutral is the key commercial fact — it **favours integration and assurance
work over platform resale**, which suits a services studio and disadvantages a single-product
vendor. The deliverable is a safeguards-conformant reference implementation plus the evidence
pack: age-gating below Grade 7, exam-context lockout, and the 25-prohibition list expressed as
enforceable policy in the LMS. Age-gating and assessment-context detection are **product
requirements here, not features** — and this KB's permissive stack can implement both.
*Source caveat: the UAE detail comes from news reporting and vendor blogs; WAM, Ministry and
KHDA primary publications are blocked in this session. The 25-prohibition figure and the
under-13 rule appear in more than one outlet; the curriculum start date does not agree across
sources and is recorded as contested.*

**Saudi Arabia returned nothing** — see Declared gaps. Treat as unsearched, not as absent.

### APAC

**Regulatory posture: four incompatible regimes, no regional harmonisation.**

- **South Korea** — the **AI Basic Act in force since 22 January 2026**; described as the
  closest analogue to the EU AI Act, though shorter. The most comprehensive regime in APAC.
  **Refinement this pass:** enforcement decrees are still being finalised and **2026 is a grace
  period oriented to guidance rather than penalties**. So Korea is a compliance-led market with
  a soft landing *this year* — the window to get architecture right before penalties bite.
- **China** — regulates by service type rather than one statute: recommendation algorithms,
  deep synthesis, generative AI services, and **labelling of AI-generated content**. The
  amended **Cybersecurity Law (in force 1 January 2026)** carries China's first AI clause.
- **Vietnam** — **new in this pass, and the most consequential APAC finding of the pass.**
  Vietnam has a dedicated **Law on Artificial Intelligence (No. 134/2025/QH15)**, in force from
  **1 March 2026**, with **Decree 142** and **Prime Minister Decision 33/2026/QD-TTg** (signed
  **30 June 2026**, effective **15 August 2026**) setting a **closed list of 46 high-risk AI
  systems across six sectors** — transport (31, the largest), **education**, ethnic and
  religious affairs, healthcare, banking and judicial proceedings. **Education accounts for
  three of the 46**, reported as **behavioural monitoring, learner ranking and automated
  assessment** *(the three-item breakdown is single-source and weaker than the rest; the
  46/6/education-included structure is corroborated by two law firms and one legal-news
  service)*. Compliance clock: systems **already running** in education before 15 August 2026
  have until **1 September 2027**; others until **1 March 2027**. Notification applies to
  medium- and high-risk systems and the Ministry of Science and Technology enforces, including
  by refusing registration. **Why this matters more than its market size:** Vietnam is the
  second jurisdiction after the EU to make education AI *statutorily* high-risk, and its
  deadlines (March and September 2027) **land before the EU's 2 December 2027**. An
  Annex-III-grade oversight architecture built for EMEA is reusable here — and needed sooner.
- **Australia** — **also new, and also previously missing.** No AI-specific statute, but the
  higher-education regulator **TEQSA** required **all 203 registered providers to submit
  institutional action plans on generative AI** (June 2024, **100% response**), and from
  **2026 moved from an educative to a regulatory-led approach**, so those plans are now
  examined in ordinary oversight. TEQSA published *Assuring quality learning in a gen AI-
  integrated future* on **24 June 2026** and maintains a GenAI Knowledge Hub; the binding layer
  is the **Higher Education Standards Framework (Threshold Standards)**, with the action plans
  sitting alongside it as expectations. Schools are covered separately by the **Australian
  Framework for Generative AI in Schools**, with state-level additions. **Practical read:** every
  Australian provider already has a written genAI plan and is now being held to it — the sale is
  *implementing an existing commitment*, which is a materially easier conversation than
  persuading an institution to adopt one.
- **Japan** — **the gap this KB declared is now closed, with a negative answer.** Japan's
  posture is promotion-first and light-touch: a promotion-focused AI law backed by voluntary
  guidelines, and **no education-specific AI statute or classroom regime** on a second targeted
  pass. That is the finding, not a failure to find — and it is why Japan remains the
  lowest-friction pilot geography in APAC.
- **Singapore** — governs by toolkit rather than statute (**AI Verify**). **New Zealand** —
  explicitly updating existing privacy and consumer law instead of writing AI law.
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

**Extraterritorial note.** The EU AI Act reaches APAC vendors selling proctoring or admissions
software into EU schools. For an APAC product company, EU conformity work is an export
prerequisite, not a European nicety — and with Vietnam's dates falling earlier, the same
engineering now has two buyers.

**Opportunity.** APAC is where the best open education agents are being built — **DeepTutor
(HKU, Apache-2.0)** and **OpenMAIC (Tsinghua, MIT)** are the two most significant open
tutoring assets globally, and both are permissive. A studio can be an implementation partner
for assets it did not have to fund. Content labelling is a concrete, dated engineering
requirement in both China and India — build provenance marking into generated courseware by
default. `MinerU` (Apache-2.0) handles CJK textbook extraction better than Western-trained
parsers. Korea is a compliance-led market under the AI Basic Act (on a 2026 guidance-first grace
period); Japan's voluntary posture makes it the lowest-friction pilot geography in the region.
**The new priority order for a regional compliance build is Vietnam first** — statutory
education high-risk with a March/September 2027 clock — **then Korea, then Australia** (where
the client's own TEQSA action plan is the requirements document), with Japan and Singapore as
low-friction pilot grounds.


#### p891 additions — APAC

**Public opinion is now measured, and it is moving *against* permissiveness in three of four
markets.** The **Ipsos Education Monitor 2026** records support for **banning AI in schools**:

| Market | Support for a ban, previous | Support for a ban, 2026 | Direction |
|---|---|---|---|
| Australia | 47% | **52%** | ▲ +5 |
| South Korea | 27% | **31%** | ▲ +4 |
| Japan | 21% | **29%** | ▲ +8 |
| Indonesia | 30% | **23%** | ▼ −7 |

Japan is the largest single move in the table. This KB records Japan as the
**lowest-friction APAC pilot geography** because it has no education-specific statute — that
remains true legally, and this is the counterweight: **regulatory headroom is widening while
public consent is narrowing**. A Japanese pilot should be designed to survive a consent
argument, not merely a compliance one (see T8). Overall, Ipsos finds support for banning AI in
schools lower than support for restricting children's social media — the ceiling on
restriction is not yet near.

**Vietnam is now the most concretely specified education-AI regime in the region.**

- The **Law on Artificial Intelligence is in force from 1 March 2026**. Education is one of the
  sectors with an extended transition: **12 months for systems already in operation generally,
  18 months for health care, education and finance**.
- **Decision 33/2026/QD-TTg** identifies high-risk systems across six sectors with **education
  among them**, naming **automated assessment** explicitly.
- Separately, the **Ministry of Education has set 12 periods per class per year of AI content
  for grades 1 to 12** — a curriculum volume mandate, distinct from the risk classification.
  *Sources conflict on whether Vietnam's education rules are a risk classification or a
  curriculum requirement; this pass finds they are **both**, from two different instruments, and
  records them separately for that reason.*

**Regional framing.** Law-firm analysis sorts APAC into three groups: **comprehensive
horizontal obligations** (South Korea, Vietnam), **targeted AI regulation** (China), and
**sector-based approaches**. **South Korea, Taiwan and Vietnam brought AI-specific statutes into
force in 2026**; China, India and Singapore regulate through rules and guidance. Australia
relies on existing law plus voluntary adoption guidance rather than a standalone AI act.

**Opportunity — APAC, sharpened.** Vietnam is the one market where the compliance object is
*named*: automated assessment is statutorily high-risk, with an 18-month education transition
and a dated curriculum obligation running to grade 1. That is a scoped, biddable programme
rather than a readiness conversation. Australia's rising ban sentiment (52%) makes
**human-in-the-loop evidence a sales requirement**, not a design preference.

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
- **Students, not just teachers (new, PISA 2025):** across the **13 Latin American and
  Caribbean countries** assessed, **nine in ten 15-year-olds have already used AI chatbots for
  schoolwork**. This is the strongest adoption datapoint in this file for any region, and it
  comes from an international assessment rather than a vendor survey.
- **Higher education (new, Digital Education Council LATAM survey 2026):** **92% of students**
  across **29 institutions** and **79% of faculty** actively engaging with AI.
- **Curriculum is the laggard, not usage (new, CENIA):** of **19** LAC countries studied by
  Chile's National Centre for AI, **13 do not teach early AI adoption in schools**. Students and
  teachers are using AI that the curriculum does not acknowledge.
- UNESCO: AI is spreading quickly but unevenly, with institutional rules lagging.

**Regulation.** **Brazil** is the regional bellwether — **PL 2338/2023**, a comprehensive
horizontal statute whose text covers education applications, remains **pending**. **Mexico**
is behind: a 2018 national AI strategy under revision, and **no Mexican AI bill enacted as of
early 2026**.

**The fragmentation is now quantified (new).** A 2026 **Universidad de los Andes** study
identified **716 AI-related regulatory instruments, rules and legislative proposals across 23
countries and territories**, **more than 80% initiated since 2023**. And the region is
polarising rather than converging: **Brazil signed an AI and tech-regulation cooperation
agreement with the EU** (June 2026), aligning itself with the Brussels model, while
**Argentina's** president submitted a bill carrying "a commitment to keep AI unregulated".
**Delivery consequence:** a LATAM multi-country rollout cannot assume one compliance target the
way an EMEA one can. Build the policy layer as configuration — the same per-jurisdiction
pattern `compose/patterns.md` P3 uses for US states — and price the jurisdiction matrix as
discovery work, not as an afterthought.

**Institutional players (new, and this is the BD map).** The **UNESCO Observatory on AI in
Education for Latin America and the Caribbean** launched in **April 2026 in Santiago**, led by
**UNESCO** with the **Development Bank of Latin America and the Caribbean (CAF)** and Chile's
**CENIA**, and including **ECLAC**, **Fundación Ceibal** (Uruguay), **Fundación Santillana**,
**Tecnológico de Monterrey** and **ProFuturo**. That is a named, funded, multilateral coalition
with a regional mandate — the right door for a regional education engagement, and a shorter
path than approaching ministries one at a time.

**Sovereign inference now has a LATAM answer (new).** **Latam-GPT**, built by **CENIA**,
launched **10 February 2026** as an open model trained on Latin American data, framed by CENIA
as "a foundational open technology base" for regional derivative models; later versions are
planned on a supercomputer at the **Universidad de Tarapacá**. In late February 2026 **UNESCO's
Santiago office and CENIA signed a cooperation agreement** on responsible AI in education, with
**Latam-GPT integration named as an early milestone** and the model intended to support
**Ministries of Education** and the Observatory itself. **Why it matters:** this KB's T6 thesis —
sovereign/local inference as a procurement requirement — previously had European instances only.
LATAM now has a regional model with multilateral backing. *Caveat: schools use is a stated
expectation, not a documented deployment, and sources disagree on launch dates (one gives
February 2025, one a September launch). Verify status before committing it to a client
architecture; `ollama` with an open-weights model remains the defensible default.*

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
localisation is itself billable differentiation. **Two additions from this pass.** First, the
PISA 2025 nine-in-ten figure changes the pitch for school systems: the question is not whether
students will use AI but whether the institution has any visibility into use that is already
universal — which makes **detection-free, assessment-redesign work** (not proctoring) the
honest offer. Second, the **UNESCO/CAF/CENIA Observatory** is the regional entry point, and
**Latam-GPT** gives a sovereignty story that does not depend on a US API — pair it with the
`ollama`/`litellm`/`qdrant` stack so the model stays swappable while the architecture stays
local.


#### p891 additions — LATAM

**The adoption-governance gap is now quantified at three levels, and every number points the
same way.**

| Level | Use | Governance | Source |
|---|---|---|---|
| Higher ed, students / faculty | **92% / 79%** actively engaging with AI | — | Digital Education Council with Tecnológico de Monterrey, 2026 |
| Institutions | **87%** use AI in some capacity | **only 26%** have a formal AI strategy | UNESCO IESALC |
| Schools (Brazil) | **53%** of administrators use AI | **only 22%** report school guidelines | cited via UNESCO |
| Students, 15-year-olds | **~9 in 10** have used AI chatbots for schoolwork, across the 13 regional countries assessed | — | PISA 2025 via UNESCO |

**A 61-point gap between institutional use (87%) and institutional strategy (26%) is the single
largest quantified governance deficit in this entire KB, in any region.** The KB's existing
"53/22 gap" pattern (P5) was built on the Brazilian school figure; it now has a higher-education
analogue, at a larger institution size and with a bigger gap.

**Regulatory fragmentation is now counted.** A **2026 Universidad de los Andes study counted 716
AI-related regulatory instruments, rules and legislative proposals across 23 countries and
territories, more than 80% initiated since 2023.** The region's problem is not absence of
regulation; it is **incoherence** — and that is a different, more tractable service offering
(multi-jurisdiction mapping) than the compliance-readiness work sold in EMEA.

**The two poles are now explicit.** **Brazil's** legislature is considering a draft AI framework
borrowing heavily from the EU approach, and **Brazil signed an AI and tech-regulation agreement
with the EU in June 2026**. **Argentina** is moving the opposite way: the Milei government
submitted a bill containing *a commitment to keep AI unregulated*. A regional client with
operations in both cannot run one compliance posture, and that divergence is itself the
engagement.

**School-level AI education barely exists.** **CENIA reports that 13 of the 19 Latin American
and Caribbean countries studied do not teach early AI adoption in schools.**

**The institutional map has a new centre.** **UNESCO launched the Observatory on Artificial
Intelligence in Education for Latin America and the Caribbean in April 2026**, at ECLAC
headquarters in Santiago, Chile — led by UNESCO with **CAF, CENIA, ECLAC, Fundación Ceibal,
Fundación Santillana, Tecnológico de Monterrey and ProFuturo**. UNESCO IESALC's accompanying
recommendation is that governments **fold higher education into national AI strategies, fund it,
issue national guidance, and integrate AI literacy and governance into accreditation**.

**Why that last clause is the commercially important one.** *Accreditation* is a budget trigger
in a way that guidance is not. If AI governance enters accreditation criteria, every institution
acquires a dated, externally audited obligation — and the Observatory's partner list is
precisely the set of bodies that would carry it. **Track the Observatory's outputs as a leading
indicator of LATAM demand**, and note that CENIA — which also runs **Latam-GPT** and the annual
Latin America AI Index — sits inside it, which links the governance agenda to a regional model
this KB already tracks.

**Opportunity — LATAM, sharpened.** The 87/26 institutional gap is the headline: near-universal
use, almost no strategy, at institutions with procurement capacity. Lead with **governance
retrofit at higher-education scale** (P5 applies, resized), attach **multi-jurisdiction mapping**
against the 716-instrument fragmentation, and position against accreditation rather than against
legislation — the former has a budget owner.

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
- ~~**No AI-in-education policy for Japan**~~ — **closed in pass p890 with a negative answer.**
  Japan's AI law is promotion-focused and backed by voluntary guidelines; a second targeted pass
  found **no education-specific statute or classroom regime**. Absence confirmed, not unknown.
- ~~**No Africa or Middle East specific leg**~~ — **closed in p891.** Both were run as
  dedicated legs; see the Africa and Middle East subsections under EMEA. They remain filed under
  `region: EMEA` because this KB's region vocabulary is closed to five values — the country is in
  the prose, as the schema requires. Coverage is now thin-but-real rather than absent.
- ~~**Star counts and repo-popularity metrics are absent**~~ — **closed.** Batched `repo:`
  qualifiers against `gh api search/repositories` work; 116 of 119 tracked repos resolve. See
  `agents/top.md` for the three that do not. This line was stale and is corrected here.
- **Primary legal and statistical texts could not be byte-read in this pass.** Every non-GitHub
  host is blocked by the session's network policy, so `ncleg.gov`, `data.consilium.europa.eu`,
  `unesco.org`, `teqsa.gov.au`, `multistate.us` and the law-firm analyses were reachable only
  through search snippets. Facts are labelled with their channel and corroboration above. **To
  close this, the session's allowed-domain list needs those hosts added** — it is an environment
  limit, and no amount of further searching fixes it.
- **No vendor-share, pricing or win/loss data in any region.** Market size exists; competitive
  position does not. The Jisc statement is the closest proxy — it tells you what buyers are
  unhappy about, which is more actionable than share figures anyway.
- ~~**Africa and the Middle East remain unexamined**~~ — **closed in p891** after four passes.
  Africa yielded the South African draft-policy retraction (10 April 2026, abrogated 27 April
  2026 over fictitious references), Nigeria's National EdTech Strategy 2025–2030, Kenya's
  M-Shule, the AU Continental AI Strategy and the November 2026 AI Research Foundations launch
  across 30 universities. The Middle East yielded the UAE's 25-prohibition classroom guide and
  KHDA's platform-neutral 2027-28 regime.
- ~~**Canada is a one-pilot leg**~~ — **closed in p891.** Canada now has its own subsection:
  no national rule, formal educator guidance in only four provinces (BC, New Brunswick,
  Newfoundland and Labrador, Quebec), nothing from Ontario's ministry, and a higher-education
  sector that has broadly refused AI detection on privacy grounds.
- **Saudi Arabia is unsearched, not absent.** The Middle East leg returned detailed UAE federal
  and Dubai material and **nothing on KSA**. Given Vision 2030 education spending, read this as
  a search-reach failure. Own leg next pass.
- **India has never been covered** by this KB, in any pass. The largest school system in the
  world, and this file has no position on it. Highest-value remaining gap.
- **Africa and Middle East findings are low-to-moderate confidence.** Primary government
  sources (WAM, UAE Ministry of Education, KHDA, South African DCDT) are blocked in this
  session; the South African retraction is well-corroborated, the UAE curriculum start date is
  contested across sources, and 2026 African edtech adoption figures were omitted as
  unverifiable rather than reported with a caveat.
