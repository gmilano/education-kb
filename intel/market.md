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

#### Update 2026-11-13 (fifth pass) — the one telemetry standard North America specifies now has a priced path, and two new restriction instruments surfaced

🟢 **The opportunity that is specific to this region, and it is new.** **Caliper
Analytics is the 1EdTech-native learning-analytics standard and is the one most
often written into North American higher-ed procurement** — xAPI dominates
everywhere else. Until this pass this KB told a Caliper-bound client it had "no
open starting point; that is a build, and it must be priced as one." **That is
withdrawn.** Six implementations are now verified (`repos/foundations.md`), and
the regional detail matters: the most complete one,
`UnizinAnalytics/caliper-net-public` (LGPL-3.0, **nine Metric Profiles** — Base,
Session, Reading, Annotation, Assignable, Assessment, Assessment Item, Outcome,
Media) comes from **Unizin, the US higher-education consortium**, and the
permissively licensed analysis layer,
`tl-its-umich-edu/caliper-event-analysis` (**Apache-2.0**), comes from the
**University of Michigan** with its statistics consulting group CSCAR.
🔵 **Both are North American institutional provenance, which is usable evidence
in a US higher-ed procurement conversation in a way an EU or APAC repo is not.**

🔴 **The one Caliper component that is still a build: the event store.** The only
one found (`open-ent/caliper`, Caliper 1.2) carries **no licence**. **So the
revised North American pitch is: an MIT sensor, a GPL-3.0 Moodle emitter, an
Apache-2.0 analysis layer and a nine-profile reference to scope against — you
write the store and nothing else.** That is a line item, not a project
(pattern `P11`). 🔴 **Ask which Caliper *version* the contract names in week
one:** the only verified sensor defaults to **v1.1** and the only **v1.2**
implementation is the unlicensed one.

🟡 **Two further regulatory instruments surfaced this pass, both recorded with
their uncertainty rather than asserted.**

- **Texas HB2400** — reported as **banning AI from providing direct classroom
  instruction**. 🔴 **One secondary source calls it enacted; this pass could not
  confirm it against official legislative records, so it is logged as
  unverified.** If real it is the most restrictive instruction-level instrument
  in the region and it would make `P1` (compliance-safe practice tutor, the
  pattern written for restrictive states) directly applicable in the largest
  US K-12 market. **Verify against the Texas Legislature before quoting it.**
- **California "Parents & Kids Safe AI Act"** — a proposed **ballot
  initiative**, with **OpenAI and Common Sense Media** reported as joining it.
  🔵 **Why it matters out of proportion to its stage: a California ballot
  measure sets de facto national standards for edtech AI**, as this file's `T10`
  (platform defaults as the fastest-moving regulation) already argues for
  vendor-side changes. A ballot initiative is slower than a platform default and
  harder to reverse than a statute. **Track it; do not price against it yet.**

🔴 **Agent-side negative for this region, stated because silence would read as
coverage: no new North America-origin education agent was found this pass.**
The region's contribution to this pass is telemetry and regulation, not agents —
consistent with `T8`, which puts the agent centre of gravity in APAC.

#### Update 2026-11-13 (sixth pass) — the state-level count keeps climbing, higher ed is moving through institutions rather than statute, and federal remains empty

- **At least 25 states** have **enacted or introduced** legislation specifically
  addressing AI use in **K-12** as of spring 2026. Three themes dominate and
  they are the three a proposal must answer: **student-data privacy**,
  **classroom-use guardrails requiring human oversight**, and **AI literacy /
  curriculum requirements**.
- **Named instruments this pass:** **Idaho SB 1227** sets a statewide K-12
  framework and **bars AI from replacing human teachers**; **Maryland** requires
  state AI guidance plus local district policies; **Oklahoma** requires
  teacher-directed AI use. 🔴 **"Bars AI from replacing human teachers" is a
  design constraint, not a talking point** — it rules out autonomous-grading
  pitches in those jurisdictions and makes `P1`'s teacher-in-the-loop shape the
  only sellable one.
- **Guidance still far outruns statute:** more than half of state Departments of
  Education have issued AI guidance, while **few have enacted binding
  legislation**. Guidance is faster to satisfy and faster to change — price
  re-work in.
- **Federal remains effectively empty.** **No binding federal AI curriculum
  standards** as of mid-2026. A House committee **advanced** the *K-12 AI
  Literacy and Readiness Act of 2026*, which would create a federal funding
  pathway — **advanced, not enacted**. Do not build a proposal on it.
- **Higher ed is institutional, not legislative, and splits both ways.**
  **New Jersey** requires public colleges to offer AI certificate and degree
  programs (an *enablement* mandate — rare in this region). Against that,
  **Berkeley Law bans AI on exams and credited coursework from summer 2026**.
  🔵 **The implication for a studio: in US higher ed the buyer is the
  institution, and two institutions in the same state can be buying opposite
  products.** Segment the pipeline by institution, not by state.

#### Update 2026-11-13 (seventh pass) — two statewide vendor deployments are now named, and the mandate count keeps climbing

- 🟢 **North America now has *named statewide platform deployments*, not just policy.** **Utah** is
  deploying **Google Gemini for Education across all K-12 schools statewide from the 2026–27 school
  year**, and **Microsoft** has announced **Copilot and Teams for Education free to Washington state
  classrooms from 2026**. 🔵 **This is the displacement risk to put in front of any North American
  client:** where a hyperscaler lands the state contract, the studio's opening is **integration,
  assessment redesign and compliance evidence**, not a competing tutor.
- 🟢 **Guidance is now near-universal at state level: roughly `33`–`35` state education departments
  plus Puerto Rico publish official K-12 AI guidance**, up from about `28` in early 2025.
- 🟢 **Mandatory district AI policy is the live procurement trigger.** **Ohio** was first — every
  district had to adopt the state model policy or a locally developed equivalent **by 2026-07-01**.
  **Maryland**'s law is **effective 2026-06-01** (state guidance plus mandatory local policy), and
  **Idaho, Oklahoma and Virginia** carry 2026 laws of the same shape. **Oklahoma** additionally
  requires age-appropriate tools, **teacher review of AI output**, and **parent opt-out**, with
  district policies in place **before the 2027–28 school year**. **Tennessee** also requires district
  policies. 🔵 **California's model policy is advisory, not binding** — do not price it as a deadline.
- 🔴 **The tracker disagreement `T906` flagged has not closed.** One tracker counts **`134` bills
  across `31` states** in 2026; bill numbers and attributions conflict between sources (Georgia
  `SB 179` vs Idaho `SB 1227`; Tennessee numbering varies). 🔴 **Every instrument in this section is
  secondary-sourced** — `gov.uk`-class primary access is refused from this session for US state
  legislature domains too. Quote the *shape* of the requirement, never a bill number, without
  checking enacted text.
- 🔵 **Parent opt-out and teacher-review clauses are a product requirement, not a legal footnote.**
  Oklahoma's wording maps directly onto controls this KB already holds: `learnmcp-xapi`'s per-learner
  `ACTOR_UUID` separation for opt-out scoping, and `AI-Teaching-Agent`'s human review gate.


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

#### Update 2026-11-13 (fifth pass) — this file's own regional prediction landed in Türkiye, and France supplies the only Caliper event store in existence

🟢 **A named prediction resolved in one pass, and it was this region's.** `T12`
implication 3 named *"Italy, Poland, Turkey and the Gulf"* as the concentrated
national school-platform markets where the next agent-to-SIS server would
appear. **Türkiye produced it.** `hanifisenturk/sabis-mcp-server` (**ISC**, 2
stars) serves **SABIS**, the student information system of **Sakarya
University**: one tool, `get-grades`, returning course codes and names,
assessment types and weights, final letter grades and academic term.
**This is EMEA's first agent-to-SIS path in this base.**

🔴 **And it is the most fragile of the three, which is the commercially useful
part.** It reaches the SIS by **Puppeteer web scraping, not an API**, and reads
the student's own `USERNAME` and `PASSWORD` from environment variables. Its
README states it is unofficial and unaffiliated with the university. Together
with `edupage-mcp` (Slovakia/Czechia, undocumented endpoints via a community
library) and `mcp_hemis_student` (Uzbekistan), **every agent-to-proprietary-SIS
path in this base is unsanctioned — three for three.** 🔵 **The EMEA sales
motion that follows: institutions in this region are getting agent access to
their own student data through credential-replay scrapers built by students.
The engagement is to replace that with a sanctioned, contracted integration** —
a governance sale, which `T1` identifies as this market's actual product.
**Italy, Poland and the Gulf remain unprobed and are still the cheapest
regional wedge in the base.**

🟢 **France supplies something no other region does: the only Caliper event
store that exists.** `open-ent/caliper` implements **Caliper Analytics 1.2** —
the newest version found anywhere — as **both** an event store
(`POST`/`GET /ims/caliper/v1p2/events`, bearer-token auth) **and** a sensor
forwarding Open ENT access and login events, mapped to `ToolUseEvent`/`Used` and
`SessionEvent`/`LoggedIn`. Vert.x, 33 unit tests. It comes from **Open ENT**, the
French regional *espace numérique de travail* platform. 🔵 **This is directly
usable in an EU data-sovereignty conversation: a French public-education
platform's own learning-analytics module, deployable on EU infrastructure**,
alongside `openfun/ralph` (MIT) from **France Université Numérique**, which this
file already carries. 🔴 **But it cannot be adopted as code: no licence on the
page, so all-rights-reserved, and its README states the Assessment, Grading,
Forum and Media profiles are not implemented.** Read it as a design reference
and **send a licence request** — it is the single highest-value licence request
on this board, because it is the only event store in the Caliper column.

🟡 **EMEA regulatory items re-confirmed rather than newly found this pass:** the
UK DfE generative-AI product safety standards for education (January 2026) and
Ofqual's AI-and-coursework-integrity material (March 2026); Dubai **KHDA**
guidance to private schools; and the contested EU high-risk date, where the
political agreement of **2026-05-07** postponing stand-alone high-risk
obligations from **2026-08-02** to **2027-12-02** continues to be reported
inconsistently against guides still citing August 2026. 🔴 **This file's
standing instruction holds: confirm the high-risk date against the Official
Journal before it goes in a proposal.**

#### Update 2026-11-13 (sixth pass) — the Digital Omnibus is now the controlling instrument, and the split between what moved and what did not is the whole sales motion

- **The delay is real and it is now a named regulation.** The **Digital Omnibus,
  Regulation (EU) 2026/1744, in force 27 July 2026**, moves the deadline for
  **stand-alone high-risk education systems** to **2 December 2027**. Annex III
  coverage is unchanged: admissions, learning-outcome evaluation, student
  placement, and exam or behaviour monitoring. 🔴 **Any guide still quoting
  August 2026 for high-risk education obligations predates this and is wrong** —
  several still in circulation do.
- **What did *not* move is what a studio sells against in 2026.** **Article 50
  transparency was not postponed and applies from 2 August 2026**: tell people
  they are dealing with an AI system, and label synthetic content. A narrower
  labelling grace period for systems already on the market runs to **2 December
  2026** — i.e. it expires within weeks of this pass.
- **The AI literacy duty was softened** to a duty to **support** AI literacy,
  with the Act stating it does not require guaranteeing any specific level.
  🔵 **This weakens the "AI literacy programme" pitch in EMEA and strengthens the
  conformity-and-disclosure pitch.** Reprice accordingly.
- **Deployer obligations are the durable revenue, and they are unglamorous:**
  use systems per provider instructions, keep **human oversight, monitoring and
  logging**; public institutions deploying high-risk AI must complete a
  **Fundamental Rights Impact Assessment under Article 27**.
- **The Commission's own position narrows the escape hatch:** draft high-risk
  classification guidelines published **19 May 2026** take the view that AI in
  education **often involves profiling**, so the exception **will in many cases
  not apply**. Do not plan around the exemption.
- **Standing since 2 February 2025 and still the hardest line:** **emotion
  recognition is prohibited in education institutions.** Engagement-detection
  and attention-tracking features are not negotiable here.
- **A further prohibition is listed for December 2026:** non-consensual sexually
  explicit AI content — relevant to any platform hosting learner-generated media.
- 🟢 **New this pass and it changes the EMEA technical answer, not just the
  compliance one:** the region now has a **permissive, sovereignty-compatible
  LMS** — OpenOLAT (Apache-2.0, Swiss-maintained), with in-process embeddings
  and a provider slot that accepts a self-hosted endpoint. See `compose/patterns.md`
  `P13` and `intel/trends.md` `T15`. **For an EMEA public-sector buyer this is
  the strongest single asset added to this KB.**

#### Update 2026-11-13 (seventh pass) — 🟢 `ACTION p801-E` DISCHARGED: EMEA finally has deployment figures, and they are national, dated and funded

`p801` closed with EMEA having produced **regulation and not one deployment figure**. That gap is now
closed from two directions — a funded national programme and a measured teacher-side baseline.

- 🟢 **The UK has EMEA's first dated, funded, national education-AI deployment programme.** The
  **DfE AI Tutoring** programme targets **up to `450,000` disadvantaged pupils a year** (pupils on
  free school meals), with **trials starting in secondary schools from autumn 2026** and **tools
  available to schools by the end of 2027**. 🟢 **`£2.88m` was split equally across `8` suppliers —
  Google and Pearson among them — to co-design the tools**, starting with **English, maths, science
  and modern foreign languages**. 🟢 **Tools must meet the DfE Generative AI Product Safety
  Standards** before rollout — the standards this file already recorded in January 2026 now have a
  procurement attached to them.
  🔴 **Year groups conflict across reports: some say years `9`–`11`, others years `9`–`10`.** Quote
  the pupil count and the dates; do not quote the year range without checking the tender.
  🔴 **Criticism is on the record and a client will raise it:** the procurement runs *in parallel*
  with the evaluation meant to establish whether AI tutoring works, and tutoring bodies have asked
  the DfE to test at smaller scale first. 🔵 **That is the studio's opening, not an obstacle — the
  programme needs evaluation instrumentation, and this KB holds the only agent↔learner-record write
  path (`learnmcp-xapi`, xAPI 1.0.3) that makes agent activity reportable.**
- 🟢 **EMEA now has a measured teacher-side baseline.** The **National Education Union State of
  Education survey, fielded 5–16 February 2026**, reports **`76%` of teachers using AI tools for
  day-to-day work, up from `53%` a year earlier**. 🔴 **`49%` of schools have NO AI policy at all for
  staff or students**, and **`66%` of teachers report no policy specific to *student* use —
  unchanged from 2025.** **`66%` of secondary teachers agreed students' critical thinking has
  declined.**
  🔴 **Sample size is reported inconsistently: `9,408` vs `10,311` English state-school teachers.**
  🟢 **An independent check agrees on the shape:** a Bett/YouGov poll of UK teachers in June found
  **`48%` said their school had no policy on staff AI use, and `19%` did not know.**
  🔵 **Read the two together and the EMEA sales motion is unambiguous:** usage has crossed three
  quarters of the profession while **half of schools have no policy** — the governance deficit this
  file has been selling in LATAM is **also a UK fact**, and it is now measured.
- 🟢 **The Gulf is the other place with real deployment numbers.** The **UAE** mandated a nationwide
  **K-12 AI curriculum** (Cabinet decision May 2025 — reported as the first such national mandate),
  extended for the **2026–27 academic year, which began 31 August 2026**, to **government schools and
  MoE-curriculum private schools from KG to Grade 12**. Capability figures: **`1,000`+ AI-trained
  teachers deployed** and a teacher-competency programme covering **`23,000` educators and
  administrators**. 🔴 **Sources conflict on whether coverage is already all private schools or only
  MoE-curriculum ones**, and **no source gives a student count.**
- 🔴 **The gap that did NOT close, stated rather than smoothed: Germany, France and the Nordics
  returned no deployment figures on this pass.** A dedicated leg over those three returned UAE
  coverage and essentially nothing else — no national programme, no school count, no student count.
  🔵 **This is a real asymmetry, not a search failure to paper over: EMEA's measurable deployment
  evidence is concentrated in the UK and the Gulf.** `ACTION p802-B` carries the per-ministry legs.
  🔵 France remains present in this file for one thing only — the **Caliper event store** recorded in
  the fifth pass.
- 🔴 **Primary-source access remains refused.** `gov.uk` and `neu.org.uk` both **fail to resolve from
  this session** — the `T906` class, now at **twelve** government/institutional domains. **Every
  figure in this update is secondary-sourced and says so here.**


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

**Vietnam legislates the curriculum as well as the risk.** Beside the AI Law, **MOET
Decision `2422`** sets **12 periods per class per year** of AI content for **grades 1-12** —
a national teacher-enablement and courseware demand signal with a fixed hourly budget, which is
a far more concrete procurement hook than an adoption percentage. 🔵 Recorded in this base's
trending log since `p787`; promoted to this shelf at `p803`.

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

#### Update 2026-11-13 (fifth pass) — the region keeps the agent centre of gravity, and the first tool ecosystem around an education agent appears here

🟢 **APAC produced the pass's only new agent-adjacent artifact, and it is a new
*kind*.** `Suyutao/DeepTutor-MCP` (**Apache-2.0**, 1 star, **60 tools**) is the
first MCP server in this base built over **another education agent's data**
rather than over a platform: it exposes a self-hosted **DeepTutor** install
(HKUDS, Hong Kong — Apache-2.0, **58.7k stars**, 7.1k forks) to any MCP client,
covering Mastery Paths with outlines and evidence, Question Bank and practice
queues with analytics, generated books and reading material with notes and
highlights, knowledge-base metadata with file search and vector passage
retrieval, historical sessions and memory documents.

🔵 **Why this matters more than its 1 star suggests.** Every other education
agent in this KB is a leaf: it talks to an LLM and a platform. **A tool
ecosystem forming *around* an open education agent is the first sign that one of
them is becoming infrastructure** — the thing Moodle is for LMSs. DeepTutor is
the only candidate at that scale, it is Apache-2.0, and it is APAC-origin.
**Watch this specific signal: more third-party servers over DeepTutor means a
studio can build on DeepTutor rather than beside it.** 🔴 **Not yet adoptable:**
it needs a reachable self-hosted DeepTutor HTTP API, and its Mastery tutor tools
depend on upstream PR **`HKUDS/DeepTutor#1785`, still open and unmerged**.

🟢 **DeepTutor's own release cadence, as this window's APAC adoption signal:**
**v1.7.1 on 2026-11-01** and **v1.7.2 on 2026-11-06** — two releases in six
days, adding complete desktop downloads, speech for selected text, simpler model
setup, a **Korean interface preview**, NVIDIA NIM embeddings, broader
localization, Anki and calendar exports and more model providers. 🔵 **The
localization direction is the regional tell: Korean UI, with pt-BR and es-MX
already shipping in OpenMAIC — APAC-origin education agents are localizing
outward into LATAM and Europe, not waiting to be localized.** That is the
practical basis for `T8`'s recommendation to localize permissive APAC agents
rather than build regional ones from scratch.

🔴 **No new APAC regulatory instrument surfaced this pass.** The region's
position in this file is unchanged: South Korea's AI Basic Act in force
**2026-01-22** with enforcement decrees still being finalised; **Vietnam's** AI
law with **education named in its high-risk category** and pre-deployment
registration in the National AI Database; Australia's **TEQSA** requirement that
every higher-education provider file a generative-AI institutional action plan;
Singapore's AI Verify toolkits; Japan's voluntary model; China's comprehensive
framework. **Stated as a confirmed non-change, not as unchecked.**

#### Update 2026-11-13 (sixth pass) — mandates are now curricular and dated, and the growth-rate estimates disagree by a factor approaching two

- **China:** the Ministry of Education has made AI education **mandatory across
  every stage** of the system. 🔴 **Sources disagree on the dose and this KB
  should not average them:** one reports **at least six hours a year** for
  lower-grade students, another **eight hours a year** for primary learners.
  Rollout has varied by province.
- **India:** **AI and Computational Thinking enter all schools from Grade 3**,
  beginning in the **2026–27 academic year**, aligned to **NEP 2020**. This is
  the single largest dated curricular expansion in this file — it creates
  teacher-training and content-localisation demand at national scale.
- **Japan — the sources genuinely conflict and the disagreement is the finding.**
  One reports Japan **gathering information from pilots** and deliberately
  diverging from its neighbours; another says Japan **integrates AI across core
  subjects** under new teaching guidelines. **Verify Japan's posture directly
  before pitching there; do not carry either claim into a proposal.**
- **Public opinion is the region's quiet advantage.** Support for **banning** AI
  in schools runs **23%–31%** across Asian markets versus a **39% global
  average** (Ipsos). 🔵 **But it is moving: support for a ban in Japan rose from
  21% to 29%** — the one place in this file where resistance is measurably
  growing.
- **Readiness is uneven and that is a market, not a caveat:** an ASEAN
  Foundation study found Southeast Asian education systems at **deeply uneven
  stages of AI readiness**. Mandates without capacity is the teacher-enablement
  opportunity.
- **Financing is flowing to delivery:** the **Asian Development Bank signed a
  USD 10M financing package with Schoolnet India Limited on 17 June 2026.**
- 🔴 **Growth estimates for APAC are not usable at one decimal place:** Grand
  View puts the region at **28.1% CAGR (2026–2033)** with **Japan** highest;
  Mordor puts APAC at **44.20% CAGR**. **Quote "high-30s to 40s, contested", or
  quote neither.**

#### Update 2026-11-13 (seventh pass) — the Philippines supplies the instrument this whole market has been missing: a register of what is actually deployed

- 🟢 **The single most transferable regulatory artifact found this pass is APAC's.** The Philippines
  **Department of Education Order No. `003`, s. `2026`, issued 2026-02-20** — described as the first
  comprehensive national guideline for AI in basic education — **creates an AI registry of all
  deployments** and **sorts tools into risk tiers**, with stricter rules for high-stakes uses such as
  **grading and admissions**. 🔵 **A registry is a deliverable, not a constraint.** Every other regime
  in this file imposes duties on systems nobody has enumerated; this one enumerates first. **Build the
  registry as the first engagement artifact in any jurisdiction** — it is what the EU's Article 27
  FRIA, Oklahoma's teacher-review clause and the UNESCO governance gap all silently presuppose.
- 🟢 **South Korea's AI Basic Act entered into force 2026-01-22**, with enforcement decrees still
  being finalised and a grace period through 2026 focused on guidance rather than penalties.
  🔵 **New to this file** — `p799` recorded only that Korea's ministry domains refuse at `CONNECT`;
  the statute itself is now dated.
- 🔴 **Vietnam's timetable is refined, and this base's carried date was incomplete.** This file
  recorded "in force 2026-03-01 with an 18-month education transition". The fuller picture:
  **compliance is required by 2027-03-01**, **education systems already operating before 2026-08-15
  receive a further six months**, and an **implementing decree, `142/2026/ND-CP`, was issued
  2026-04-30**. 🔵 **Material refinement: many listed systems are high-risk *only* where their output
  is the sole basis for a decision without meaningful human review** — so a human-in-the-loop design
  can move an education deployment out of the high-risk tier entirely. That is an architectural
  lever, and this KB already holds the components for it.
- 🟢 **APAC faculty remain the region most positive on AI: `57%` report being excited about it** and
  believe it can make learning more effective — the highest of any region in the same survey.
- 🔴 **Declared gap, unchanged: China, Japan, Singapore, Australia and India returned no education-
  specific binding instruments or deployment counts on this pass.** One secondary note only — China
  has made AI compulsory for school students from age six. 🔴 **No named APAC edtech vendor emerged
  at any point in this leg.**


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
   defensible, repeatable deliverable — but 🔴 **its eval half no longer has a
   usable grant: `AITutor-EvalKit` serves NO licence file** (`p801` refuted the
   `MIT` claim; `p802` re-verified the absence at `HEAD` `a71078456a90`), so the
   open-source spine here is **`pykt-team/pykt-toolkit` (MIT) alone**, plus
   xAPI/Caliper telemetry. Thin, and now thinner than this file claimed.
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
| **Learner (secondary)** | **Nine in ten 15-year-olds** have already used AI chatbots for schoolwork, across the **13** regional countries assessed | PISA 2025 |

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

#### Update 2026-11-13 (fifth pass) — the region's incumbent SIS is now the named unserved case, and that is a sharper opportunity than "governance is absent"

🔴 **Two consecutive passes have added nothing to LATAM's agent column.** The
region's only entry remains `Jeanikt/tutor-ai-agent` ("Manu", Brazil, MIT, **0
stars**, voice-first Brazilian-Portuguese maths tutor) from the fourth pass.
**Stated explicitly because silence would read as coverage:** this pass searched
globally and per region and found no new LATAM-origin education agent.
`T8`'s recommendation is unchanged and is still the right one — **localize a
permissively licensed APAC or North American agent rather than build from
scratch** — and this pass gives it fresh support: DeepTutor now ships broader
localization and OpenMAIC already ships **pt-BR and es-MX** locales.

🟢 **But the pass produced a genuinely new, LATAM-specific opportunity, and it is
more concrete than anything in this section.** The open-source SIS agent gap
**closed for OpenEduCat** this pass — it is Odoo addons, reachable by a generic
Odoo MCP server (`erpipe-org/mcp-odoo`, MIT, 433★). 🔴 **It did not close for
RosarioSIS** (GPL-2.0, **654 stars**, PHP/Postgres), which is **the most widely
deployed open-source SIS in LATAM K-12**, with Spanish, French and Portuguese
localization in core. RosarioSIS has **no agent interface and no general-purpose
platform beneath it to inherit one from** — searched by project name this pass,
nothing returned.

🔵 **Why this is the strongest LATAM line in this file.** It converts the
region's standing pitch from a negative ("adoption is high, governance is
near-absent, sell governance") into a **named, scoped, reusable build**: an MCP
server over RosarioSIS, serving a platform that LATAM K-12 ministries and
districts already run, in a market where **87% of surveyed higher-education
institutions use AI in at least one area while only 26% have any formal
framework** and **55% have no AI budget** (UNESCO IESALC, 200 institutions
across 19 countries). The governance sale and the integration build are the same
engagement. **And unlike the three proprietary-SIS servers in this base — all of
which reach the SIS unofficially, one by replaying the student's own credentials
— a RosarioSIS server would be built against an open schema the client controls,
so it can be sanctioned, contracted and maintained.** That is the difference
between a demo and a deliverable.

🟡 **Reusable asset to build it from, so this is not greenfield:** EduPage's
**31-tool** surface is a worked answer to "what does an agent need from a school
SIS", and `erpipe-org/mcp-odoo`'s three-call write gate
(`preview_write` → `validate_write` → `execute_approved_write`, single-use
same-process expiring token, `confirm=true`, env-var kill switch) is a worked
answer to "how does it write to a student record safely." **Copy the surface
from the first and the write protocol from the second.**

#### Update 2026-11-13 (sixth pass) — the adoption/governance gap is now measured at four levels by four independent sources, and it is the most sellable number in this entire file

- **Teacher adoption leads the OECD, measurably.** OECD **TALIS (2024)** —
  share of secondary teachers who had used AI in the previous year: **Brazil
  56%, Chile 55%, Colombia 53%, Costa Rica 52%**, against an **OECD average of
  36%.** 🟢 **Four LATAM countries, all ~1.5× the OECD average. This is the
  single strongest regional statistic in this KB and it says the opposite of the
  "LATAM is behind" assumption a client arrives with.**
- **Learner adoption matches it:** Cetic.br reports **65% of Brazilian internet
  users aged 9–17 use AI tools.**
- **And governance does not — at every level:**
  - **Schools:** in Brazil **53% of school administrators use AI**, but only
    **22%** report their school has guidelines on its use.
  - **Universities:** UNESCO IESALC reports **87%** of regional universities
    already use AI, **26%** have a formal strategy, and **just 9% evaluate its
    implementation.**
- 🟢 **That 87/26/9 split is the pitch.** It names three distinct products in
  descending order of how ready the buyer is to sign: a **strategy** (61% of
  universities need one), an **evaluation framework** (78% need one), and the
  **guidelines** layer beneath both. `P4` is already shaped for exactly this —
  this update gives it its numbers.
- **Regulation is still mostly pending, which is why the governance product
  sells now rather than later.** **Brazil: PL 2338/2023** is the main vehicle —
  one tracker calls it *in advanced legislative process*, a secondary guide
  describes risk-based rules with fines up to **BRL 50M**; 🔴 **these conflict,
  so verify its current status before citing either.** **Brazil's National
  Education Council is preparing sector-specific guidance** for schools and
  universities. **Mexico:** multiple AI bills introduced, **none enacted as of
  early 2026**, with a national emphasis on **"technological sovereignty"**.
- **The market has names, and Brazil dominates it.** HolonIQ's **2026 Latin
  America EdTech 100** has Brazil at **nearly half the cohort** and the clear
  majority of deal and award activity. **Teachy** (Brazil — AI lesson
  preparation, and notably **expanded beyond the region into Asia**) and
  **Ginia** (Mexico — AI-driven employability linking employers, institutions
  and students) are the named standouts.
- **Donor money is targeting teachers, not tools:** **Google.org committed
  USD 4.6M** to expand AI education across Latin America, targeting **1.25M
  students by 2028 across nine countries** including Brazil and Mexico.
  🔵 **Teacher-training delivery at that scale is a services contract, and it is
  the shape of `P7`.**

#### Update 2026-11-13 (seventh pass) — the adoption/governance gap holds at a second instrument, and the binding constraint is capability, not policy

- 🟢 **The UNESCO IESALC headline reproduces, and its denominator is now explicit.** *AI
  Implementation in Higher Education in Latin America and the Caribbean* draws on **~`200`
  institutions across `19` countries**: **`87%` use AI in at least one area of activity**, while
  **only `26%` have a formal AI strategy**. 🔴 **Note the instrument boundary — this is NOT the same
  artifact as the UNESCO Observatory (`716` instruments, `23` countries) recorded in an earlier
  pass. Two instruments, two denominators; do not merge them into one statistic.**
- 🟢 **A second, independent instrument agrees on the shape:** a separate survey finds **only `30%`
  of Latin American universities have published policies on AI use**. 🔵 `26%` and `30%` from
  different instruments is **convergence**, and it is the strongest version of this file's
  longest-running regional claim.
- 🔴 **The binding constraint is capability and money, and `p799`'s correction holds.** **`55%` of
  universities carry no specific AI budget.** New this pass: **`17%` of public universities already
  using AI in teaching provide NO academic staff training at all.** 🔵 **Staff training is common but
  student training lags** — so the gap is not "no policy", it is **nobody able to implement one**.
  Sell appraisal capability and a funding case, not another acceptable-use document.
- 🟢 **A funded regional governance programme is now named: `Integrity AI`, EU-funded under
  Erasmus+, building governance frameworks with `7` universities across `4` Latin American
  countries.** 🔵 **This is a partner and a template, not a competitor** — and it is the first
  EMEA↔LATAM governance bridge this file has been able to name.
- 🔴 **Brazil's regulatory position is still pending, and this file should stop anticipating it.**
  The national AI bill that would classify education AI as **high-risk had not passed the Chamber as
  of June 2026 and is not law**. **LGPD applies to AI in higher education today** and is the
  instrument to design against. 🔴 Broader analyses describe South American regulation of AI in
  higher education as close to non-existent, and a 2026 study of `52` documents names
  **"borrowed ethics"** — institutions adopting international frameworks without the capacity to
  implement them. 🔵 **"Borrowed ethics" is the precise name for what the `55%`/`17%` figures
  measure, and it is the sharpest phrase in this file for a LATAM pitch.**
- 🔴 **Every figure in this update is secondary-sourced from coverage of the underlying reports**;
  sources are inconsistent on dates and sample sizes. `T906` holds.


### Global

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

#### Update 2026-11-13 (fifth pass) — the OECD gave this market a measurable acceptance test, and the SIS layer got a cross-region connector

🟢 **The most sellable sentence added to this KB today, and it is global.** The
OECD's **2026 Digital Education Outlook** (*Exploring Effective Uses of
Generative AI in Education*) separates **task performance** from **learning**
and finds that students with access to general-purpose GenAI **produce
higher-quality output, but that the advantage disappears, and sometimes
reverses, in exams once access is removed.** Purpose-built educational AI shows
**sustained** gains. 🔵 **This converts "buy a purpose-built tutor, not a
chatbot licence" from a vendor preference into an OECD evidence claim, and it
hands an institution a measurable acceptance test for any pilot: measure under
withdrawal, not under access.** No procurement document this KB has seen
specifies that test, and a studio that writes it into a pilot design
differentiates on evidence rather than features. The report also recommends
systems co-created with educators and learners in which **teachers set
acceptable error levels and monitor interactions** — the same human-review-gate
shape `P6`, `P7` and this base's `AI-Teaching-Agent` row already converge on.

🟢 **Cross-region structural finding: the SIS layer has a general-purpose
connector, and it is the largest build-safe agent in this KB that touches
education.** `erpipe-org/mcp-odoo` (**MIT, 433 stars**, 198 forks, 41 tools,
Odoo 16–19) and `ivnvxd/mcp-server-odoo` (**MPL-2.0, 415 stars**) reach any Odoo
model by name, and **OpenEduCat** (LGPL-3.0, 911 stars, 789 forks) is Odoo
addons. Odoo's education footprint is heaviest in **India, LATAM and EMEA
SMB/private education**; the connectors themselves are region-neutral, so this
is one asset serving three regions. 🔴 **Architecturally verified, not run
(`Gap 286`)** — quote it as a verified architecture, never as a delivered
integration. Full reasoning in `T13`, recipe in `P12`.

🟡 **Adoption figures re-confirmed this pass, unchanged and still inconsistent
across sources** — treat as a range, not a number: **86%** of higher-education
students globally report using AI in their studies (Digital Education Council);
roughly **a quarter** of faculty say their institution has a formal AI policy;
global AI-in-education market estimates for 2026 still span **$10.4B** to
**$12.3B** depending on the house. 🔴 **This file's standing caution holds: the
market-size spread is wider than most of the growth rates being quoted on top of
it.**


#### Update 2026-11-13 (sixth pass) — the market-size spread is unchanged, the governance deficit is now a global figure, and the OECD has named the product

- **Market size: no convergence, and this file's standing caution holds.** Two
  more 2026 figures land inside the existing range rather than narrowing it —
  Research and Markets at **USD 10.6B (2026) → USD 42.48B by 2030 (41.5% CAGR)**
  and Grand View at **USD 11.4B (2026) → USD 57.2B by 2033 (25.9% CAGR)**.
  🔴 **Note what that pair actually shows: two houses differ by under 8% on
  today's size and by nearly 16 points on the growth rate.** The disagreement is
  about the future, not the present. **Carry "roughly $10–12B in 2026, growing
  fast, with growth rates contested between the mid-20s and the low-40s" and
  never a single CAGR.**
- **The governance deficit is global, not regional.** UNESCO finds **only 10% of
  schools and universities worldwide have formal AI guidelines.** Set against
  LATAM's 22% (schools) and 26% (university strategy) figures above, **LATAM is
  at or above the world average on governance as well as adoption** — a second
  correction to the "LATAM lags" assumption, and one worth making explicitly in
  a regional pitch.
- 🟢 **The OECD has effectively specified the product.** The **2026 Digital
  Education Outlook** recommends moving **beyond general-purpose AI tools toward
  purpose-built educational AI designed to produce durable learning gains.**
  This is `T3` stated by a standards-setting body rather than by vendors, and it
  is the strongest available argument for why a studio engagement beats handing
  teachers a general chatbot. **Quote the OECD, not the vendors.**
- 🔵 **Cross-region, newly true this pass:** a client anywhere who needs a
  **permissively licensed LMS** now has **two** options rather than one — Sakai
  (ECL-2.0) and OpenOLAT (Apache-2.0) — and the second ships AI in-tree. This
  file previously recorded "no permissive LMS exists at scale" as a hard
  constraint on every engagement. **It is withdrawn.** See
  `repos/foundations.md` and `compose/patterns.md` `P13`.
