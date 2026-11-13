---
industry: education
region: Global
updated: 2026-11-13
---

# Education AI — market map and opportunities by region

Researched 2026-11-13, across four passes; the fourth-pass updates sit under
each region below. Where sources disagree, the disagreement is shown rather
than averaged away. Market-size figures for AI in education come largely from
vendor blogs citing differing research firms and should be treated as
order-of-magnitude only.

## Market size — contested

Four 2026 figures for the AI-in-education market, all for the same year:
**$10.4B**, **$11.4B**, **$12.3B** (HolonIQ), and projections running from
$32.3B (by 2030) to $57B (by 2033). All trace to secondary vendor sources. Use
"roughly $10–12B in 2026, growing fast" and do not quote a specific figure to a
client without a primary report.

**Segment figures added 2026-11-13 (third pass).** The whole-market number is
the least useful one to carry into a conversation; the segment numbers are
narrower and better matched to what a studio actually sells:

| Segment | 2026 | Forecast | Source |
|---|---|---|---|
| **Agentic AI in education** | **$2.37B** | $11.83B by 2031 | Mordor Intelligence |
| **AI tutors** | **$2.7B** | $17.7B by 2033 | Grand View Research |
| AI in education (whole) | $11.4B | 25.9% CAGR 2026–2033 | Grand View Research |

Mordor also puts **Intelligent Tutoring Systems at 26.04% of the agentic
education segment (2025)** — the largest single share, which is consistent with
ITS being where the open-source agent supply in this KB is concentrated
(`DeepTutor`, `OATutor`, `tutor-mcp`, `ai-shifu`).

**Use the agentic figure, not the headline figure.** "$2.37B in 2026 growing to
$11.83B by 2031" is defensible, segment-correct and roughly 5× growth; "$11.4B
AI in education" includes hardware, smart classrooms and proctoring that no
studio engagement touches. Same caveat as above: all of these are secondary
vendor estimates, cited as such.

## The structural fact of this market

**Adoption has outrun governance everywhere, and the gap is the commercial
opportunity.** Every region shows the same shape — very high individual use by
students and teachers, very low institutional policy coverage:

| Evidence | Figure | Source type |
|---|---|---|
| Students using AI in their studies (16 countries) | 86% | Digital Education Council survey, via secondary |
| LATAM higher-ed institutions using AI in ≥1 area (200 institutions, 19 countries) | 87% | UNESCO IESALC study |
| LATAM institutions with any formal AI framework | 26% | UNESCO IESALC study |
| LATAM universities with no specific AI budget | 55% | UNESCO IESALC study |
| LATAM institutions that evaluate their AI implementation | 9% | UNESCO IESALC study |
| Brazilian school administrators using AI | 53% | Cetic.br |
| Brazilian schools with any AI guideline | 22% | Cetic.br |
| US faculty reporting a formal institutional AI policy | ~25% | secondary roundup |

The sellable work is therefore rarely "build a tutor". It is **governance,
integration, evaluation and teacher enablement around tools the institution is
already using unofficially.**

## Global players

**Open-source / buildable layer:** HKUDS (DeepTutor, Apache-2.0, 58.7k),
Tsinghua MAIC (OpenMAIC, MIT, 43.4k), JuneYaooo (teacher-to-skills,
Apache-2.0, 475), Open edX nonprofit (Harvard/MIT lineage), Moodle HQ,
Instructure (Canvas), Learning Equality (Kolibri, MIT), Khan Academy (Perseus
MIT; Khanmigo commercially), Oppia Foundation, Frappe, OpenEduCat, and the
LTI 1.3 maintainers (Cvmcosta/ltijs Apache-2.0; Packback; Simon
Initiative/Open Learning Initiative).

**Policy and standards setters:** UNESCO and UNESCO IESALC, OECD, European
Commission (AI Act, Digital Education Action Plan), 1EdTech (LTI, Caliper,
QTI), national education ministries.

**Commercial incumbents to integrate with or displace:** Instructure, Anthology,
PowerSchool, Google for Education, Microsoft Education, Duolingo, Chegg,
Coursera, 2U/edX, plus OpenAI and Anthropic distributing directly into
education — OpenAI with named government and education-system partnerships
across EMEA.

## Opportunities by region

### North America

**Adoption/regulation:** The most legislatively active region, and the activity
is restrictive rather than enabling. Trackers count **134 AI-in-education bills
across 31 states in 2026**, with the consensus read that states favour
research, transparency and guardrails over mandated classroom adoption.
Concrete instruments: **Texas** general AI law (TRAIGA) effective 2026-01-01
with **HB 2400 barring AI from delivering direct classroom instruction**;
**New York** restricting classroom AI to grade 9+ with exceptions for
diagnostics and special education; **California AB 1159** would **bar using
student data to train AI models**; **Idaho SB 1227** requires privacy
protections for AI tools in schools and produced a statewide generative-AI
framework approved August 2026; **North Carolina SL 2026-41** (AI-literacy
standards; state model policy by 2026-12-31, local policies by 2027-06-30,
teacher training by 2028-06-30); **New Jersey A 4352 / S 2862** would add AI to
curriculum and require AI credentials at public colleges. **Four states —
Idaho, Oklahoma, Virginia and Maryland — passed 2026 laws requiring both state
guidance and mandatory district-level AI policy adoption.** Federally: the April
2025 executive order "Advancing Artificial Intelligence Education for American
Youth" sets K-12 priorities, and the **K-12 AI Literacy and Readiness Act of
2026** advanced out of the House Education and Workforce Committee. District
level is where procurement now bites: **New York City** issued preliminary
guidance in March 2026 on a **green/yellow/red traffic-light framework**, and
**Chicago's** board-approved policy **bars AI from being the sole basis for
high-stakes decisions such as discipline and special-education placement**.
California may become the de facto national regulator for AI used by minors;
OpenAI and Common Sense Media proposed a ballot initiative ("Parents & Kids
Safe AI Act").

**Source conflict to respect:** one tracker holds that **TRAIGA and HB 2400 are
the only *enacted* measures** so far, which contradicts sources treating the
North Carolina, Idaho and Maryland instruments as law. Trackers mix introduced
with enacted. Verify any specific bill against the legislature before advising.

**Players:** Instructure/Canvas is the integration target that matters; Canvas
dominates higher ed. PowerSchool in K-12 SIS. Large districts (NYC, Chicago,
Denver, Charlotte-Mecklenburg) now have their own AI policies, which means
district-level procurement with real compliance requirements. Canada's rules
are mainly workplace-focused and reach education only indirectly; **Mexico was
not covered by the sources found this pass — an unverified gap, not a finding
of absence.**

**Opportunities:**
1. **Compliance-aware tutoring that respects instruction bans.** Texas HB 2400
   forbids AI *delivering instruction*; practice, feedback and teacher support
   remain open. A tutor architected as "practice and feedback, human delivers
   instruction" is sellable in states where a general tutor is not.
2. **State-mandated AI literacy programs with deadlines.** North Carolina's
   model-policy date is **within seven weeks** of this update, with local
   policies and teacher training following. Four states now mandate district
   policy adoption. Districts need curriculum, training and a policy artifact —
   deliverable work with a statutory deadline.
3. **Decision-provenance controls for high-stakes use.** Chicago's rule
   (no AI as sole basis for discipline or placement) and NYC's traffic-light
   tiers are implementable as technical controls: human-in-the-loop gates,
   decision logging, tier-based tool allowlists. No open-source project covers
   this; it is consulting plus a small platform.
4. **Canvas-native agents.** `canvas-mcp` (MIT, 324 stars) plus `ltijs`
   (Apache-2.0) is the fastest route to an agent inside the dominant North
   American LMS.
5. **Student-data-boundary architecture.** If AB 1159 passes, "student data
   never reaches model training" becomes a contractual requirement — which
   means self-hosted or no-train-guarantee inference, and an auditable data
   path. Build it once, sell it in every state that follows.

#### Update 2026-11-13 (third pass) — regulation hardened, and a platform default changed the ground

- **The governance gap now has a number.** Google's November 2026 education
  report (Gallup-based) finds **85% of educators say they use generative AI**
  while **only 18% of US teachers report having received any formal AI guidance**
  from administrators. That 85/18 split is the single most sellable statistic in
  this KB: the demand is not for AI capability, it is for governance of AI
  already in use.
- **A platform default became policy.** Google is making **Gemini and Search
  opt-in (off by default) for K-12 student accounts**, administrator-enabled,
  with the change starting early 2027; traditional Search without AI summaries
  is **not** offered as an option (AI Mode and AI Overviews stay built in).
  Political backlash followed (Bernie Sanders, NYC Mayor Zohran Mamdani).
  **Consequence for engagements:** districts now face an explicit
  enable/disable decision with no middle setting, which converts "should we
  allow AI" from a philosophical question into a dated administrative task with
  a deadline. That is a procurement trigger.
- **Binding state law, not just guidance.** Maryland **SB 720** signed,
  effective **2026-06-01**. Oklahoma **SB 1734** signed May 2026 (age-appropriate
  tools, mandatory teacher review of AI output, parent opt-out). Ohio requires
  every public, community and STEM school to **adopt an AI framework by
  2026-07-01**. Mississippi embeds AI literacy into general education for all
  incoming undergraduates from **Fall 2026** and requires institutions to
  evaluate AI tools for bias. Florida's state board approved AI rules covering
  K-12 **and all 28 state colleges**.
- **Federal: still no binding curriculum standard.** The **K-12 AI Literacy and
  Readiness Act of 2026** was advanced by the House Education and Workforce
  Committee; status beyond committee unconfirmed. Treat federal action as a
  watch item, state action as the real driver.
- **Institution-level mandates are the new unit.** UT Austin requires every
  course syllabus from **Fall 2026** to carry a **Course AI Policy Statement**
  classifying generative AI as permitted / partially permitted / prohibited.
  This is a per-course, per-term artifact at university scale — i.e. a
  templating and compliance-tracking problem, which is a product.
- **Source conflict, recorded:** state-guidance counts range from "28+ states
  plus DC" to "34+ states plus DC/PR" across secondary trackers. Quote the
  direction, not the count.

#### Update 2026-11-13 (fourth pass) — the legislative volume is real, the counts disagree, and three states now have dated deadlines

**Bill volume, with the disagreement shown rather than averaged.** One tracker
counts **134 AI-in-education bills across 31 states** in the 2026 session;
**FutureEd counts roughly 71 across 27 states**. The gap is definitional — what
counts as an "AI in education" bill — and both are secondary trackers. Quote the
range and the reason for it, never a single number.

**The legislative posture is cautious, which is itself the commercial fact.**
Analysts reading the 2026 session describe states as focused on **research,
transparency and guardrails rather than mandating classroom adoption**. Nothing
in the US pipeline obliges a district to buy AI; several instruments oblige it to
*govern* AI it already has. That is the shape of the demand.

**Dated deadlines — the procurement triggers.** As `T10` argues, a date with a
named owner is when budget moves:

| Jurisdiction | Instrument | Date |
|---|---|---|
| **North Carolina** | State model policy due | **31 December 2026** |
| **North Carolina** | Local school-unit policies due | **30 June 2027** |
| **North Carolina** | Specified teacher professional development due | **30 June 2028** |
| **California** | AI Working Group statewide Model Policy published | June 2026 |
| **Maryland** | Package: designated AI coordinators + university-supported **certification of compliant AI tools** | 2026 session |
| **New York** | NY A 9190 would restrict classroom AI to **grade 9 and above**, with exceptions | pending |

North Carolina is the one to build a regional offer around: three successive
deadlines, each creating a different deliverable — policy, then local policy at
scale, then teacher training. Maryland's **tool-certification** provision is the
more interesting one commercially, because it implies a conformity-assessment
market inside a single US state, which is the EMEA motion arriving in North
America.

**Guidance is now near-universal at state level.** A June 2026 tracker puts
**35+ states** with official AI guidance from their education departments.
Guidance without enforcement is exactly the governance gap `T1` describes, and
the 85%/18% educator pairing already in this section quantifies it.

**Federal, and it is indirect.** The US Department of Education finalized a rule
**prioritizing federal education grants** for projects that expand understanding
of AI or its appropriate and ethical use. This is a funding signal, not a
mandate: it makes "AI literacy and ethical use" a fundable line item in grant
applications, which is a route into public-sector engagements that does not
depend on a district's own budget.

**One unusual input worth knowing about in a room.** Students from all 50 states
produced a national framework, the **"STUDENTS FIRST Act of 2026"** (via AASA),
which explicitly rejects *both* an outright ban and unrestricted adoption. It
carries no legal force and is useful for exactly one thing: it is the most
quotable evidence that the student constituency is asking for governed use
rather than either extreme.

**Reliability note.** Several items here come from secondary trackers with
inconsistent dates and counts, and at least one claim circulating for this period
(a Florida policy dated 16 September 2026) **could not be confirmed against a
primary source and is therefore not asserted above**. For anything that will
appear in a proposal, verify against the state legislature or department of
education directly.

### EMEA

**Adoption/regulation:** The binding regime is the **EU AI Act**, under which
AI for **access, allocation, assessment, or monitoring of pupils during tests**
is high-risk in principle (Annex III), with an exception for genuinely low-risk
uses. The **Digital Omnibus on AI was published in the Official Journal on
2026-07-24 as Regulation (EU) 2026/1744**, and the timeline it sets is
**2027-12-02 for stand-alone Annex III systems** and **2028-08-02 for AI
embedded in regulated products**, with transparency duties from August 2026.
**Sources conflict:** at least one consultancy states full enforcement of
high-risk requirements arrived in August 2026. Verify against EUR-Lex
(Regulation (EU) 2024/1689 as amended) before advising. The
**emotion-recognition ban in education** has applied since February 2025. The
**AI literacy duty (Article 4)** was softened in July 2026 to a duty to
"support the development of AI literacy". On 2026-06-18 the **European
Commission and OECD published an AI literacy framework for primary and
secondary schools** alongside updated ethical guidelines ("Empowering Learners
for the Age of AI"). **Council of the EU document ST-14902-2026 (2026-10-29)**
makes digital sovereignty and strategic autonomy explicit, treating reduced
dependence on AI tools developed outside Europe as critical for education and
training. Funding channels: Digital Education Action Plan, Erasmus+, Horizon
Europe, ESF+.

**Middle East:** materially more active than this KB previously recorded. The
**UAE** has expanded academic offerings to include AI-focused programs at all
levels; **Saudi Arabia has made AI literacy a mandatory component of
undergraduate education**; **Dubai's KHDA has issued explicit guidance to
private schools** on responsible AI use. Gulf AI spending is shifting from
pilots to sector-scale rollouts.

**Africa:** the **African Union's Continental Education Strategy for Africa
(CESA 16-25)** sets the digital-education direction, and structured AI use is
driven by **government and NGO programs rather than individual teacher
adoption** — which means the buyer is a ministry or a donor, not a school.
**Morocco's "AI Made in Morocco"** strategy targets the academia-industry gap.
First Africa-origin education agent found: **EDUKAI LongView** (ISC, Guinea,
bilingual FR/EN) — a 0-star prototype, but evidence of local capability.

**Players:** Moodle (dominant in European public education), ILIAS
(German-speaking vocational and public sector), Chamilo (Spain, francophone
Africa), Opencast and BigBlueButton (university infrastructure), national
ministries and agencies. **OpenAI reports government and education-system
partnerships including Estonia, Slovakia, Greece and Italy**, citing teacher
adoption and time savings — i.e. the frontier labs are already inside the
public systems a studio would sell to.

**Opportunities:**
1. **High-risk conformity packages for assessment and admissions AI.** The
   deadline moved to 2027-12-02; it did not disappear, and the conflicting
   August-2026 reading means some clients believe they are already late.
   Institutions need risk management, documentation, human oversight and
   logging for systems they already run. Highest-value regulated work in
   education globally.
2. **Sovereign, self-hosted education AI.** The Council's October 2026
   sovereignty language plus GDPR makes "runs in our own infrastructure, on
   open weights" a procurement requirement rather than a preference.
   Moodle/ILIAS + self-hosted inference + MIT/Apache agent layer, with a
   Moodle MCP server (`Faixiang`, MIT) for agent access, is a directly
   sellable stack — and it is the explicit counter-position to the OpenAI
   national partnerships.
3. **AI literacy delivery against the Commission/OECD framework.** A published
   framework, institutional obligations behind it, and a teacher population
   that needs training.
4. **Gulf mandate delivery.** Saudi Arabia's mandatory undergraduate AI
   literacy and the UAE's all-levels programs are funded, dated obligations at
   national scale — curriculum, teacher training and platform work, with a
   buyer that pays.
5. **Ministry-and-donor-scale African programs.** Since adoption is program-led
   under CESA, the deliverable is a national or donor-funded rollout:
   Kolibri (MIT, offline-first) plus localized content, with FR/EN bilingual
   handling as a baseline requirement rather than a feature.

#### Update 2026-11-13 (third pass) — the high-risk deadline moved, and that changes the sales motion

- **The Annex III high-risk deadline moved to 2027-12-02.** The **Digital
  Omnibus** postponed the standalone high-risk obligations under Annex III —
  the category containing education — from the previously circulated
  **2026-08-02** to **2 December 2027**. Earlier vendor guides still print the
  2026 date. **Verify against Regulation (EU) 2024/1689 and the Commission's own
  pages before quoting either to a client**, and expect the client's incumbent
  advisor to be working from the old date.
- **What this does to the pitch:** the compliance deadline is no longer
  imminent, so "you must be conformant by August" is dead as an urgency lever
  and repeating it will cost credibility. The live lever is the **two
  obligations already in force**: the **Article 5(1)(f) ban on emotion
  inference in education institutions** (applicable since **2025-02-02**,
  medical/safety exceptions only) and the **AI literacy duty** (same date).
  Those are enforceable now.
- **Scope is narrower than most clients assume.** Education AI is high-risk
  only when it performs one of the four functions in **Annex III point 3**:
  admissions/access, evaluating learning outcomes, assessing appropriate
  education level, or monitoring students during tests. The Commission's **May
  2026 draft guidelines** place **tutoring, practice feedback and information
  chatbots generally outside** high-risk. **This is a scoping instrument:** a
  practice tutor that never scores of record stays out; the moment it writes a
  grade of record it is in.
- **The obligation sits on the vendor, not the school.** Conformity assessment
  applies to the **EdTech vendor as provider**; schools are **deployers** (use
  as instructed, trained human oversight, logging, inform students and
  parents). A studio building for an institution may become the provider — that
  allocation must be settled in the contract, not discovered at audit.
- **EU-level frameworks to cite:** the Commission and **OECD** jointly
  published the **AILit** AI Literacy Framework ("Empowering Learners for the
  Age of AI") on **2026-06-17**; further guidance landed **2026-03-05** under
  the Digital Education Action Plan (ethical use of AI and data in teaching,
  disinformation and digital literacy, criteria for selecting high-quality
  digital education content). The **European AI Office** is the institutional
  counterpart.
- **Sovereignty angle, with a repo attached:** `openfun/ralph` (MIT) is a
  Learning Record Store from **France Université Numérique** — an EU
  public-education-origin, permissively licensed data layer. For an EU client
  asking where learner data lives, that is a concrete answer rather than a
  posture.

#### Update 2026-11-13 (fourth pass) — the high-risk date is contested, the UK has shipped concrete standards, and Africa is no longer a blank in this file

**The EU AI Act education high-risk date — sources genuinely conflict, so here
is the disagreement.** Education AI is high-risk where it is used for
**admissions, grading, and cheating detection**. On the timing: one reading puts
the obligations at **August 2026**; another, reflecting the **2026 Digital
Omnibus amendments**, at **2 December 2027**. The Commission's own page states
the amendments were **adopted June 2026 and entered into force 27 July 2026**,
which makes **2 December 2027** the more likely date for the education high-risk
obligations. **Carry the later date with the caveat attached, and verify against
the consolidated Act text before it goes in a contract** — a client who has
planned for August 2026 has planned for the wrong year, in both directions.

**What is already in force and is routinely missed: the AI literacy duty has
applied since February 2025.** It is not deferred by the Omnibus. An institution
using AI in teaching has a live obligation now, which makes AI literacy the
easiest EMEA engagement to justify and the one with no date to wait for.

**The UK has moved from guidance to standards, which is the more sellable
shape.** Department for Education **product safety standards for generative AI
in education (January 2026)**, and **Ofqual material on AI and coursework
integrity (March 2026)**. Product *standards* imply conformity work — the UK is
converging on the EMEA assessment-conformity motion in `P2` without the AI Act's
machinery.

**Policy scaffolding to cite rather than re-derive.** The European Parliament's
**March 2026 briefing** on AI in classrooms points to the **Digital Education
Action Plan** and the **European Education Area**; the Commission has presented a
new **Education and Skills Package** on AI and digital learning. In the Gulf,
**Dubai's KHDA issues explicit responsible-AI guidance to private schools** — the
region is policy-led and well-resourced, which is why it buys governance
packages rather than pilots.

**Demand-side signals.** OpenAI reports government and education-system
partnerships across EMEA including **Estonia, Slovakia, Greece and Italy**,
focused on equitable access, AI literacy and evaluation. Employer-side,
**Microsoft, AWS and Caterpillar have announced AI skills commitments totalling
roughly $3.6B** — skills funding that often routes through education
institutions.

**Africa — previously a declared gap in this file, now populated.** The third
pass recorded that EMEA searches returned little on Africa specifically. A
dedicated search this pass changes that:

| Country / body | Instrument | Status |
|---|---|---|
| **Kenya** | National AI Strategy 2025-2030 — commits to AI literacy across education, pilots Digital Innovation Hubs as curriculum anchors | Published March 2025 |
| **Nigeria** | National EdTech Strategy 2025-2030 — teacher capacity, safe AI use, data systems, financing | Active; a separate analysis argues the Digital Economy Policy has **not** translated into systemic education use |
| **South Africa** | Draft National AI Policy, covering education among other sectors | Published for comment **10 April 2026**; one source lists it **abrogated 27 April 2026** — **this conflict is unresolved and must be checked against the Government Gazette** |
| **African Union** | Continental Education Strategy 2026-2035 — treats digitalization and AI as cross-cutting themes | Adopted |
| **UNESCO** | AI readiness assessments across **six Southern African countries**, to inform national AI-in-education policy | In progress |
| **Multi-country** | **AI Research Foundations** launched **9 November 2026** — Google.org-backed, FATE Foundation (Nigeria) as grant holder, training university lecturers in Ghana, Kenya, Nigeria and South Africa, targeting **30,000 students** | Launched |

**The read:** Africa's AI-in-education activity is **strategy-and-capacity
shaped, not deployment shaped** — national strategies, teacher capacity, lecturer
training — which matches the one Africa-origin agent in this KB
(`Keitous/EDUKAI-LONGVIEW`, ISC, Guinea, synthetic data, 0 stars). The
engagement that fits is **teacher and lecturer enablement with a governance
artifact**, delivered against a national strategy document, not a platform
rollout. The 9 November launch is the freshest lead in this file.

**Reliability note.** The Africa sources are a mix of a preprint, a Wikipedia
entry, advocacy analysis and news reports; the South Africa policy status is
actively contradictory. Verify against official government documents before any
of it reaches a client.

**One EMEA-specific technical finding this pass.** The first verified
agent-to-SIS MCP server in this KB is **EMEA-origin**:
`oliverhruby/edupage-mcp` (MIT, 31 tools) over **EduPage**, the school
information system used across **Slovakia and Czechia**. See `T12` — the
concentrated national school-platform markets in Italy, Poland, Turkey and the
Gulf are the obvious next instances, and none has a verified MCP server yet.

### APAC

**Adoption/regulation:** The most fragmented region, and education is usually
caught as a *high-risk category inside general* AI law rather than addressed
directly. **South Korea's AI Basic Act entered into force 2026-01-22** and
names education a high-impact area alongside healthcare and finance; year one
is reported as a pilot with limited enforcement and enforcement decrees still
being finalized. **Vietnam's binding AI law** puts education in its high-risk
category and requires **pre-deployment registration and human oversight**, with
an implementing decree in April 2026; **one source gives high-risk sectors
until September 2027 to comply** — the compliance deadline and the
in-force date are different things and sources blur them, so verify.
**Japan** has the **AI Promotion Act (June 2025)**, though other sources
characterise Japan as voluntary-guidelines-and-self-regulation; both can be
true (a promotion-oriented statute without high-risk obligations), but do not
assert either without checking. **Australia** has no AI-specific statute; its
2024 mandatory-guardrails proposal covers high-risk education uses, and the
higher-ed regulator **TEQSA has required universities to submit generative-AI
risk management plans**. **China** has the most detailed binding rules (content
labelling, algorithm registration) but they are not education-specific.
**Singapore and New Zealand** rely on voluntary toolkits and existing law.
The EU AI Act reaches APAC vendors selling into Europe.

**Public opinion is moving, and not uniformly:** the **Ipsos Education Monitor
2026** finds overall lower support for banning AI in schools across the Asian
markets examined, but support for a ban **rose in Japan and South Korea** while
it **fell in Indonesia**. A region-wide message will misfire; the political risk
of classroom AI is increasing in exactly the two most advanced markets.

**Players:** Tsinghua MAIC (OpenMAIC, MIT, 43.4k), HKUDS (DeepTutor,
Apache-2.0, 58.7k) and JuneYaooo (teacher-to-skills, Apache-2.0, 475) — **the
three largest education AI agent projects in the world are all APAC-origin**.
India: BHASHINI language infrastructure and DIKSHA (already shipping AI
features such as in-video keyword search and read-aloud for visually impaired
learners); **Bharat EduAI Stack** open Indic-language models announced
September 2026 by IIT Madras-incubated Bodhan AI — an announcement, not a
rollout. Moodle and Frappe LMS are widely deployed. Every major APAC economy is
building domestically owned models; regional adoption is characterised as broad
but shallow.

**Opportunities:**
1. **Multi-jurisdiction compliance architecture.** A regional university group
   or edtech vendor faces Korean high-impact rules, Vietnamese registration,
   Australian TEQSA plans, Chinese labelling and the EU Act for exports — all
   at once. One policy-enforcement layer with per-jurisdiction configuration is
   a genuine architecture problem worth paying for.
2. **Vietnam pre-deployment registration and human oversight.** A hard,
   binding obligation already in force, with a compliance runway that sources
   place as late as September 2027. First-mover advisory plus the technical
   oversight/logging layer it requires.
3. **Localize the APAC-origin agents.** DeepTutor (Apache-2.0), OpenMAIC (MIT)
   and teacher-to-skills (Apache-2.0) are permissively licensed, large and
   built in the region. Adapting them to Indic, Bahasa, Thai, Vietnamese and
   Japanese curricula is lower-risk than building a tutor from zero.
4. **Sovereign deployment for localization mandates.** Self-hosted open weights
   plus a local LMS answers data-residency requirements directly.
5. **Teacher-led framing for Japan and Korea.** With ban sentiment rising in
   both, the saleable product is explicitly teacher-augmenting and
   parent-legible — `teacher-to-skills`-shaped (distil the teacher, keep them
   in the loop) rather than student-facing autonomous tutoring.

#### Update 2026-11-13 (third pass) — four regimes, four different instruments, and a cautionary rollout

- **South Korea — the region's first comprehensive statute.** The **AI Basic
  Act has been in force since 2026-01-22**. Generative AI users must be told
  they are interacting with AI, and generated content must be marked. Korea
  **declined** to add a text-and-data-mining exception to its Copyright Act in
  February 2026 — relevant to any training-on-course-materials proposal. A PIPA
  special provision for AI development reportedly passed 2026-08-20 and is
  **not yet in force** (tracker-sourced; verify).
- **Korea is also the cautionary tale.** Korea rolled out **AI-powered digital
  textbooks from 2025**, the first country to attempt it at national scale, and
  met **parental and teacher backlash over screen time**. Any national-scale
  pitch should cite this and lead with the mitigation, because the client's
  ministry will already know it.
- **China — no general AI law, binding specific rules.** Mandatory regimes
  cover recommendation algorithms, deepfakes, generative AI services, and
  **labelling of AI-generated content since 2025-09-01**. Note also that China
  **banned the private tutoring sector**, which is why **TAL pivoted into AI
  learning hardware** — the money moved from services to devices.
- **Japan — light touch.** The **AI Promotion Act (May 2025)** encourages
  cooperation with government safety measures and carries **no monetary
  penalties**. Lowest regulatory friction in the region.
- **India — labelling in force, statute signalled.** Amended IT Rules require
  AI-generated content to carry **prominent labels and provenance markers from
  2026-02-20**; in **July 2026** the government signalled it may pursue
  dedicated AI legislation. **PhysicsWallah** launched its own AI tutor;
  **BYJU'S** collapse is still the reference failure in the market.
- **Commercial players to know:** **Mathpresso's QANDA** (Korea, math-solving,
  global reach), **ByteDance's Gauth** (a top education app **in the US** —
  APAC-built product winning a North American market), TAL, PhysicsWallah.
- **Declared gap:** no source found in this pass regulates **AI in the
  classroom** specifically in any of these four countries — the instruments are
  economy-wide AI law plus content labelling. Education-specific rules must be
  verified **directly with each country's education ministry**; do not infer
  them from the AI statutes.

#### Update 2026-11-13 (fourth pass) — two binding laws are now in force, education is named high-risk in one, and public opinion diverges sharply within the region

**Binding law, in force, with education named.**

| Jurisdiction | Instrument | In force | Education treatment |
|---|---|---|---|
| **South Korea** | AI Basic Act | **22 January 2026** | Comprehensive; disclosure duties |
| **Vietnam** | Law on Artificial Intelligence | **1 March 2026** | **Education named high-risk**, specifically **automated assessment and behavioural monitoring** |
| **China** | Targeted rules — algorithms, deepfakes, generative AI | In force | Sectoral, not education-specific |
| **Australia** | Existing law plus voluntary guidance | — | No dedicated instrument |
| **India** | Governance guidelines plus **labelling rules for AI-generated content** | — | Provenance marking |

**Vietnam is the sharpest opportunity in the region and the date needs care.**
Education is on the high-risk list, and **automated assessment and behavioural
monitoring** are named — which is precisely what an assessment or proctoring
agent does. Existing education systems get a grace period, and **the sources
disagree on its length**: one says six months beyond a March 2027 deadline,
another that high-risk sectors have until **September 2027**. Both readings land
in 2027; do not quote either to a client without the statutory text. The
commercial shape is `P2` — a conformity layer for assessment AI — transplanted
from EMEA to Vietnam, and the EMEA work is reusable because the risk-based
structure is the same.

**Public opinion diverges inside the region, and it cuts against student-facing
autonomy in the Anglophone markets.** The **Ipsos Education Monitor 2026** finds
support for *banning* AI in schools is **lower across most Asian markets** but
**higher in Australia and New Zealand**, ranging from **23% in Indonesia to 31%
in South Korea** — and support for a ban **rose year-on-year in Japan and
Australia**. Ipsos characterizes Indonesia's posture as **"Protect and
Prepare"**: limits on children's social media alongside openness to AI in
education.

**What that means for how an engagement is pitched.** In Australia, New Zealand
and Japan — the markets with rising ban sentiment and no binding instrument — the
**teacher-augmenting** framing (`P7`, teacher distillation) is materially safer
than student-facing autonomy, and the risk is reputational rather than legal. In
Indonesia, Vietnam and Korea the receptiveness is higher but in two of the three
the law is now binding, so the constraint moves from public opinion to
conformity. **Same region, opposite dominant constraint** — do not carry one
country's pitch to the next.

**Policy maturity is bimodal.** UNESCO notes **China and Singapore** have
established AI-in-education policies and guidelines, while other countries in the
region are **still contending with basic educational needs**. The regional
average is not a useful planning number for anything.

**One APAC technical finding this pass.** The second verified agent-to-SIS
server in this KB is **Central Asian**: `sukhrobyangibaev/mcp_hemis_student`
(MIT) over **HEMIS**, used by Uzbek universities. With EduPage in EMEA this
establishes the `T12` pattern — agent integration arrives first where one
platform holds a captive national market.

**Reliability note.** The strongest sources here are the Ipsos survey and a
law-firm regulatory analysis; the in-force dates should still be checked against
official texts, and the Vietnamese grace period is unresolved between two
secondary readings.

### LATAM

**Adoption/regulation:** The widest gap between use and governance of any
region, and the best-documented. **UNESCO IESALC, across 200 institutions in 19
countries: 87% of higher-education institutions use AI in at least one area,
26% have any formal framework, 55% of universities have no specific AI budget,
and only 9% evaluate their AI implementation.** In schools, **more than 50% of
teachers in countries such as Chile and Brazil already use AI tools, while
fewer than 10% of institutions have formal guidelines.** Brazil's **Cetic.br**
reports **53% of school administrators using AI against 22% of schools having
any guideline**. The Digital Education Council's **2026 LATAM higher-ed survey
(with Tecnológico de Monterrey's Institute for the Future of Education) reports
92% of students and 79% of faculty actively engaging with AI.** Regulation is
fragmented: a 2026 **Universidad de los Andes** inventory identified **716
AI-related regulatory instruments, rules and proposals across 23 countries and
territories**. **Brazil's PL 2.338/2023** is the main risk-based bill;
**Colombia** adopted a national AI policy via **CONPES 4144 (February 2025)**
with budgeted actions through 2030 rather than immediate horizontal
obligations. Argentina, Brazil, Chile, Colombia, Costa Rica, Mexico and Peru
have adopted the OECD AI Principles.

**Players:** UNESCO IESALC — launched an **Observatory on AI in Education for
Latin America and the Caribbean in April 2026** to guide public policy;
**Cetic.br** (Brazil) and **Ceibal** (Uruguay) as national data sources and, in
Ceibal's case, a national deployment vehicle; Tecnológico de Monterrey; World
Economic Forum (regional white paper arguing for harmonized regulation);
Universidad de los Andes. Platform-wise: Moodle, Chamilo and RosarioSIS have
deep regional footprints. **New: the first LATAM-origin education agents** —
Manu (`Jeanikt/tutor-ai-agent`, MIT, Brazilian Portuguese voice math tutor) and
`nifalconi/educational-agents` (Chile, from the Niñas Pro girls' AI course,
**unlicensed as published**). Both are 0–1 star prototypes.

**Opportunities:**
1. **Institutional AI governance as a productized offering.** 87% using, 26%
   governed, 9% evaluating; 53% of Brazilian administrators using against 22%
   with guidelines. This is the single clearest product-market fit in this
   entire KB: a repeatable package of policy, controls, teacher training and an
   evaluation harness.
2. **Evaluation and measurement.** Only 9% evaluate. An evaluation layer
   (pedagogical eval plus xAPI/Caliper telemetry plus dashboards) is a
   defensible, repeatable deliverable — and `AITutor-EvalKit` (MIT) plus pyKT
   (MIT) give it an open-source spine, thin as they are.
3. **Low-budget deployment models.** 55% have no AI budget, so the offer must be
   cheap to run: Kolibri (MIT, offline-first) or Moodle plus self-hosted open
   weights, not per-seat frontier API spend.
4. **Ceibal-style national programs.** Uruguay's Ceibal is a working template
   for country-scale deployment; similar ministry programs are the large
   contracts in this region.
5. **Spanish/Portuguese pedagogical content generation — with a shortcut.**
   `educhain` (MIT) and Oppia (Apache-2.0) localized to national curricula
   (ENEM, ICFES, PAES, SEP), and note that **OpenMAIC already ships pt-BR and
   es-MX locales**, so the largest multi-agent classroom in the world is
   already partly localized for this region.
6. **Adopt and license the local prototypes.** Manu (MIT, Brazil) is usable as
   published; the Chilean Niñas Pro library is not, for want of a LICENSE file.
   Contributing licensing and engineering to regional projects buys both
   capability and standing.

#### Update 2026-11-13 (third pass) — adoption is high, governance is near-absent, and that is the whole opportunity

- **Teachers are already using it.** TALIS (2024) secondary-teacher AI use in
  the previous year: **Brazil 56%, Chile 55%, Colombia 53%, Costa Rica 52%** —
  materially level with developed-market rates.
- **Governance is not there.** Brazilian school administrators: **53% use AI,
  22% report their school has guidelines on its use**. Higher education
  (UNESCO IESALC): **87% of regional universities already use AI, 26% have a
  formal strategy**. A 61-point gap at university level.
- **Why that specific gap is the product:** the deficit is **policy,
  procurement rules and teacher guidance** — not models and not infrastructure.
  That is a 6–8 week productizable engagement (pattern `P4`), repeatable across
  institutions in one country, and it does not compete with the hyperscalers.
- **Regulatory status, corrected against the newest source.** **Peru is the
  only country in the region with an enacted AI statute.** Brazil's framework
  (EU-influenced, stringent) is **still a pending bill**; Chile's is pending;
  **Mexico has proposals and none enacted as of early 2026**, with a stated
  emphasis on **"technological sovereignty"** and reducing reliance on foreign
  AI models. **Source conflict recorded:** one aggregator describes Brazil as
  having comprehensive legislation and another describes Chile as having moved
  to a binding rights-protective framework; the newer CASRAI comparison
  (updated September 2026) says both are pending. **Go with pending**, and
  verify before any regulatory claim in a proposal.
- **Mexico's sovereignty framing is a selling position, not an obstacle:**
  self-hosted inference on `yetanalytics/lrsql` (Apache-2.0) or `openfun/ralph`
  (MIT) with no learner data leaving the country is a direct answer to it.
- **School-level AI education is largely absent.** Chile's **CENIA** found that
  **13 of the 19** Latin American and Caribbean countries it studied **do not
  teach early AI adoption in schools**. Commentary notes systems are
  integrating AI tools into classrooms *without oversight or guidelines* —
  which is the same finding as the Brazil 53/22 split, from the other direction.
- **Declared gap:** no 2026 source found covering **edtech vendor or
  procurement rules** specifically in Brazil, Mexico or Chile. Procurement is
  where a studio engagement is actually won or lost, so this needs a dedicated
  search before any LATAM public-sector pursuit.

#### Update 2026-11-13 (fourth pass) — the adoption/governance gap is now measured at four independent levels, and the regulatory volume is larger than this file assumed

**The gap, measured at four levels by four different bodies.** This is the most
evidenced claim in this KB and the numbers now stack from institution down to
classroom:

| Level | Finding | Source |
|---|---|---|
| **Institutional (HE)** | **87%** of institutions use AI in at least one area; **26%** have any formal framework. 200 institutions, 19 countries | UNESCO IESALC |
| **Individual (HE)** | **92% of students** and **79% of faculty** actively engaging with AI | Digital Education Council LATAM Survey 2026, with Tecnológico de Monterrey and the Institute for the Future of Education |
| **School capacity** | **Fewer than 10%** of institutions have formal guidelines *and* sufficient capacity for school use | UNESCO Observatory |
| **National (Brazil)** | **53%** of school administrators use AI; **22%** report their school has any guideline | Cetic.br 2026 |
| **National (Uruguay)** | **75%** of public-school teachers report using these tools | Ceibal 2026 |
| **Regional (teachers)** | **More than 50%** of teachers in Chile and Brazil already use AI tools | UNESCO |

The Brazil pairing (53/22) and the institutional pairing (87/26) are the two to
carry into a room: both are a single source, a single year, and the same
instrument measuring use and governance together, which is what makes them
unanswerable.

**Regulatory volume is much larger than "a few bills."** A Universidad de los
Andes study identifies **716 AI-related regulatory instruments, rules and
legislative proposals across 23 countries and territories**, most introduced
since 2023. The practical consequence is not that compliance is hard yet — most
are proposals — but that **no client can track this themselves**, which is a
billable service in its own right and the substance of `P4`.

| Country | Instrument | Status |
|---|---|---|
| **Brazil** | **PL 2.338/2023** — general AI rules, risk-based approach | Still moving through Congress |
| **Colombia** | Government-wide AI program with actions and **budget through 2030** | Adopted; **not** immediate binding obligations |
| **Argentina, Brazil, Chile, Colombia, Costa Rica, Mexico, Peru** | OECD AI Principles | Formally adopted |

**Colombia is the under-read opportunity.** A funded, government-wide program
through 2030 with no binding obligations attached is the most procurement-friendly
configuration in the region: money is allocated and there is no conformity
blocker. Argentina and Peru's OECD adoption matters for the same reason —
principles create a framework to deliver *against* without creating a hurdle.

**New institutional anchor.** UNESCO launched the **Observatory on Artificial
Intelligence in Education for Latin America and the Caribbean** in **April 2026,
in Santiago**. This is a standing regional reference point and a credible body to
align a governance deliverable with — more durable than citing a one-off survey.

**The frameworks the region actually reaches for are international.** **ISO/IEC
42001** and the **NIST AI RMF** are used as reference frameworks across LATAM.
That is a direct reuse opportunity: a governance package built to ISO/IEC 42001
for a North American or EMEA client **transfers to LATAM with translation and
local policy mapping**, rather than needing a new framework. Build it once.

**Reliability note.** The adoption figures are self-reported survey data from
different instruments and are **not** strictly comparable across studies; UNESCO
IESALC and the Digital Education Council measure different populations. Use them
as a consistent *direction*, which they unambiguously are, rather than as
arithmetic.

### Global / cross-region

**Opportunities not tied to one region:**
1. **Grading and feedback agents — the one genuinely open field.** No dominant
   open-source grading agent exists anywhere. `nbgrader` (BSD-3-Clause) is the
   substrate and `wwrwbs/AI_AWE` (Apache-2.0, 2 stars) proves the pipeline
   shape (discourse classifier → feature scorer → label-aware feedback), but
   nothing is production-grade. This is now the clearest build opportunity in
   this KB.
2. **An MCP server for the student record — scope corrected 2026-11-13 (fourth
   pass).** This item previously read "not one SIS has an agent interface." That
   is **withdrawn**: `oliverhruby/edupage-mcp` (MIT, 31 tools, EduPage) and
   `sukhrobyangibaev/mcp_hemis_student` (MIT, HEMIS) are real agent-to-SIS
   servers. **The opportunity is narrower and better defined than before:** not
   one *open-source* SIS — OpenEduCat, RosarioSIS, Gibbon, openSIS,
   `frappe/education` — has an agent interface, and the two servers that exist
   target **national proprietary platforms**, one of them over undocumented
   endpoints. Advising, retention and early-warning agents all need the student
   record. The topology is now proven, which makes `P8` cheaper to sell (5-7
   weeks) and lowers its delivery risk. See `T12`.
3. **Pedagogical evaluation as a practice.** `AITutor-EvalKit` at 4 stars is the
   state of the art. Institutions in every region are deploying tutors with no
   way to measure teaching quality. Whoever makes this credible sets the
   standard.
4. **Consolidate or harden a Moodle MCP server.** Seven fragmented servers,
   three MIT, none proven. Moodle is the most-deployed LMS in the world and the
   incumbent across EMEA, LATAM and APAC public education. One hardened MIT
   server is reusable in most education engagements Globant will see.
5. **Teacher enablement.** Universal across regions, consistently
   under-resourced, and the one intervention every policy framework mandates —
   now with APAC public opinion (Ipsos 2026) making the teacher-augmenting
   framing commercially safer than student-facing autonomy.
