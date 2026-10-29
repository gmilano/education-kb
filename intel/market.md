---
industry: education
region: Global
updated: 2026-10-29
---

# Education AI — Market Map and Opportunities

**Pass `p526` · 2026-10-29.** Figures are attributed to the source that produced
them. Where sources disagree the disagreement is shown rather than averaged away,
because an averaged number is a number nobody published.

## Global market size — four firms, one wide band

| Source | 2026 | Forecast | CAGR |
|---|---|---|---|
| Precedence Research | **USD 9.58B** | USD 136.79B by 2035 | 34.52% (2026-2035) |
| Resourcera | USD 10.4B | USD 32.27B by 2030 | — |
| Range across four firms (roundup) | **USD 6.4B – 11.4B** | — | ~30-35% cluster |

**Read the band, not the point.** A 78% spread between the low and high 2026
estimate means the methodology is doing more work than the market. What the
sources agree on is the *growth rate* (30-35%) and the *regional ranking*, and
those are the usable parts.

Regional share: **North America ~36%** (largest), **APAC fastest-growing at
35.3% CAGR**.

## Adoption — better evidenced than market size

| Signal | Figure | Source |
|---|---|---|
| Students using AI in their studies (16 countries) | **86%** | Digital Education Council, 2025 |
| K-12 teachers using generative AI for work | **25% → 53%** in one year | RAND, 2025 |
| Time saved by weekly teacher AI users | **5.9 hours/week** | Gallup + Walton Family Foundation, 2025 |
| US teachers using AI tools | 60% | Child Trends / US Dept. of Education analysis |
| Schools with rules governing AI use | **under 10%** | roundup, unattributed to a primary |

**This gap is the commercial thesis.** Adoption is near-universal among students
and past half among teachers, while governance is near-absent. The scarce good is
not a tutor — it is a **defensible, auditable** tutor. Every regional opportunity
below is a variation on that sentence.

⚠️ *The "under 10%" figure appears in a secondary roundup without a primary
citation. Treat it as directional. The RAND, Gallup and Digital Education Council
figures carry named primaries and can be quoted to a client.*

## Opportunities by region

### North America

**Regulatory posture.** State-led and moving fast: **134+ bills across 31 states**
on AI in K-12 and higher education (MultiState and FutureEd trackers), mostly on
data privacy, classroom-use limits and curriculum. **Maryland, Idaho, Oklahoma and
Virginia** have 2026 laws requiring *both* state guidance *and* mandatory
district-level AI policy adoption. **Oklahoma bars AI as the primary basis for
grading, discipline, placement or other high-stakes decisions.** Federally, the
**K-12 AI Literacy and Readiness Act (H.R. 8747)** advanced out of the House
Education and Workforce Committee on 21 July, largely along party lines, and would
let schools spend federal funds on AI literacy.

**Players.** Instructure (Canvas) dominates higher-ed LMS; the NEA and AFT have
issued AI guidance (and drawn criticism for it); a student-authored *STUDENTS
FIRST Act* framework from all 50 states, published via Day of AI, rejects both a
ban and unrestricted use. UChicago Law removes devices from core first-year
classes from autumn 2026.

**Opportunities.**
1. **District policy-compliance layer.** Four states now mandate district-level AI
   policies and one forbids AI-determined grades. A deployment that *cannot
   technically* let a model decide a grade — human-in-the-loop enforced in code,
   with an audit trail — is a procurement requirement, not a feature. Build on
   [anthropics/k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills)
   eval rubrics (Apache-2.0) for the acceptability yardstick.
2. **Canvas-attached agents.** Canvas is AGPL-3.0 and must not be forked;
   [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) (MIT)
   is a ready, licence-clean seam into the dominant North American LMS.
3. **Teacher time recovery, measured.** 5.9 hours/week is a defensible ROI number
   for a lesson-prep and feedback agent — and it is measurable, which makes it
   sellable to a district CFO rather than a CIO.

### EMEA

**Regulatory posture — the most consequential change this pass.** The **Digital
Omnibus, Regulation (EU) 2026/1744**, was published in the Official Journal on
**24 July 2026** and applies from **27 July 2026**. It moved the high-risk
compliance deadline for stand-alone education AI systems — grading, admissions
triage, exam proctoring — from **2 August 2026 to 2 December 2027**. Two things
did *not* move: **Article 50 transparency duties still apply from 2 August 2026**
(users must be told they are interacting with an AI system), and
**emotion-recognition AI has been banned in schools since February 2025**.

**What that means commercially:** a **16-month build window** on high-risk
education AI, with transparency and the emotion-recognition ban live *now*. Schools
are in pilot-and-pre-compliance mode rather than enforcement.

**Players.** Europe captured **62.3% of year-to-date 2026 edtech capital** (up
from 34.5% for full-year 2025) per trade aggregation. Named: **Multiverse**
(London, ~$70M at a ~$2.1B valuation), **Gizmo** (London, $22M Series A,
15 Apr 2026), **Ed.ai** (France, ~€5M seed, Sept 2026), **Lucida AI** ($5.4M seed,
Apr 2026, voice-first language coach), **Third Space Learning** ($5.94M growth
equity for *Skye*, a spoken maths tutor), plus AMBOSS, Preply and Knowunity.
Middle East and Africa are an order of magnitude smaller: **Dawraty** (Kuwait,
$2M seed, Qatar Development Bank), **3C Coding School** (Egypt, $3M seed for Saudi
expansion), **Eyone** (Dakar, Senegal).

**Open-source anchors, placed:** [OpenOLAT](https://github.com/OpenOLAT/OpenOLAT)
(Apache-2.0, Switzerland), [ILIAS](https://github.com/ILIAS-eLearning/ILIAS)
(GPL-3.0, Germany), [Ralph LRS](https://github.com/openfun/ralph) (MIT, France),
[Dolos](https://github.com/dodona-edu/dolos) (MIT, Ghent), and
[Open TutorAI CE](https://github.com/Open-TutorAi/open-tutor-ai-CE)
(BSD-3-Clause, **Morocco**) — the one EMEA-placed education agent on these shelves.

**Opportunities.**
1. **AI Act conformity scaffolding for education products.** Dec 2027 is close
   enough to sell against and far enough to build for: technical documentation,
   logging, human oversight, risk management. Article 50 disclosure and the
   emotion-recognition prohibition are enforceable today — an audit-and-remediate
   engagement needs no new technology at all.
2. **Sovereign, self-hosted tutoring.** EU public-sector procurement rewards code
   provenance. OpenOLAT (Apache-2.0, Swiss) + a locally served model + Ralph for
   xAPI records is a stack with no US cloud dependency in the learning path.
3. **MEA leapfrog, built on the Morocco row.** Open TutorAI CE is BSD-3-Clause
   with 194 forks against 114 stars — evidence of deployment, not hype. It is the
   natural base for francophone and Arabophone North Africa and Gulf work.

### APAC

**Regulatory posture — no single model.** Binding AI rules: **South Korea, China,
Vietnam**. Guidance and existing law: **Japan, Singapore, Hong Kong, Australia,
India**. China regulates recommendation algorithms, deep synthesis, generative AI
services and **AI-generated-content labelling**, with a non-binding AI-agent
opinion effective **15 July 2026**. Japan is promotion-led — its 2025 AI
Promotion Act carries no explicit penalties. **India requires prominent labels and
provenance markers on AI-generated content from 20 Feb 2026** and *plans*
compulsory AI and computational thinking **from Class 3 in the 2026-27 academic
year**.

⚠️ *Sources conflict on curriculum status: one claims China and the UAE are the
only countries running compulsory national AI curricula since the 2025-26 school
year, which sits badly with India's rollout being described as planned. UNESCO
separately reports China, Japan, Korea and Singapore integrating AI curricula.
Verify per country before quoting.*

**Players.** **TAL** (China, pivoted into AI learning hardware), **ByteDance
Gauth**, **PhysicsWallah** (India, own AI tutor). Sector context matters: China
shut its ~$100B private-tutoring industry in 2021 and India's BYJU'S collapsed
into insolvency — so the market is rebuilding around AI tutoring from a low base
of trust. Non-academic STEM, coding and AI tutoring has rebounded in China. Ipsos
Education Monitor 2026 finds **lower** support for banning AI in schools across
Asian markets, with **Australia and New Zealand more** supportive of a ban.

**Open-source anchors, placed:** both of the world's largest open-source education
agents are APAC-academic — [DeepTutor](https://github.com/HKUDS/DeepTutor)
(Apache-2.0, 48.9k★, Univ. of Hong Kong) and
[OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) (MIT, 41.7k★, Tsinghua). **This
is the single most actionable supply fact in this file.**

**Opportunities.**
1. **Build on the APAC agents, not around them.** DeepTutor and OpenMAIC are
   Apache-2.0 and MIT, both shipped releases on 28-29 Oct 2026, and together
   carry 90k+ stars. Anywhere in the world, the fastest credible tutoring
   prototype starts from one of these two.
2. **Content-provenance compliance as a product.** India (20 Feb 2026) and China
   both require AI-content labelling. Generated lesson material needs provenance
   metadata baked in at authoring time — emit H5P with provenance attached and
   the obligation is satisfied structurally.
3. **India's Class-3 curriculum rollout.** A compulsory AI subject from Class 3
   across the 2026-27 academic year is a teacher-training and
   content-at-national-scale problem. Kolibri (MIT, offline-first) plus a
   content-generation agent addresses the connectivity constraint that will
   otherwise decide the outcome.
4. **ANZ needs the restraint story, not the capability story.** It is the one
   market in this region where public opinion leans toward *banning* AI in
   schools. Lead with controls, provenance and integrity tooling
   ([Dolos](https://github.com/dodona-edu/dolos), MIT).

### LATAM

**Regulatory posture.** Fragmented and reactive. **Brazil's PL 2338/2023** is at
an advanced stage of the legislative process and its draft includes education
provisions on AI literacy and reskilling; **Brazil's data protection authority
(ANPD) is running an AI regulatory sandbox pilot through December 2026**, and
**Brazil signed an AI and tech regulation agreement with the EU in June 2026**.
**Mexico has no comprehensive AI law** — its National AI Strategy dates to 2018
and is under revision. **Argentina's president submitted a bill that would leave
AI unregulated**, the opposite direction from Brazil. A regional civil-society
analysis (ALSUR) characterises the whole picture as *legislative reactivity without
a comprehensive legal framework*.

**Adoption.** The IDB reviewed **193 regional initiatives**: **59% used generative
AI, 27% used language models**, and the authors conclude the region *recombines*
AI tools in its own ways rather than importing them wholesale. Counterweight:
**CENIA (Chile) finds 13 of 19 LAC countries studied have not yet introduced early
AI adoption in schools.** **Google.org has committed $4.6M to AI literacy across
nine countries including Brazil and Mexico, targeting 1.25M students by 2028.**

**Players.** From the 2026 Holon IQ LATAM EdTech 100: **Teachy** (Brazil, AI lesson
preparation — a regional incumbent that has expanded into Asia), **Ginia**
(Mexico, AI-driven employability), **Vetto** (Brazil), **Mattilda** (Mexico,
billing for private schools). The list shows AI positioning shifting **toward
teachers** and upskilling losing ground as a category.

**Open-source anchor, placed:** [i-educar](https://github.com/portabilis/i-educar)
(GPL-2.0, 722★) — Brazil's largest free school-management system, born in Itajaí
(SC) municipal government, on the federal Public Software Portal since 2008.

**Opportunities.**
1. **Teacher-facing first, mirroring where the market already moved.** Teachy's
   position and the EdTech 100 both say the buyer is the teacher, not the learner.
   Lesson preparation and feedback in Portuguese and Spanish, built on
   [Educhain](https://github.com/satvik314/educhain) (MIT) emitting
   [H5P](https://github.com/h5p/h5p-php-library) for portability.
2. **The i-educar modernisation engagement.** Hundreds of Brazilian municipalities
   run GPL-2.0 school management from 2008. The work is an integration layer —
   enrolment, attendance and performance signals into an advising agent — not a
   replacement, and GPL-2.0 means it must stay across a service boundary.
3. **Use the ANPD sandbox as the de-risking vehicle.** A pilot inside Brazil's
   regulatory sandbox before December 2026 produces a compliance story that
   survives PL 2338 becoming law. That is a reason to start now rather than wait.
4. **Thirteen of nineteen countries have not started.** CENIA's number is the
   greenfield read: national AI-literacy programmes with no incumbent to displace.
   Kolibri (MIT, offline-first) is the right base where connectivity is the binding
   constraint.

## Declared gaps this pass

Written down because an unstated gap is indistinguishable from coverage.

- **No authoritative ranking of EMEA AI-education vendors.** The funding figures
  above come from trade aggregators that disagree with each other on round sizes
  and company locations (one lists Sinai.ai in the Middle East, another in
  California). No primary announcements were checked.
- **North America: Canada and Mexico education-specific AI policy returned almost
  nothing.** The regional overview found cited Canada's *workplace* AI rules, not
  education policy. The NA leg is effectively a US leg this pass.
- **No LATAM-origin open-source education agent exists on these shelves.** The
  region's open-source strength is school management (i-educar), not agents.
- **The "under 10% of schools have AI rules" figure has no primary citation.**
- **APAC curriculum status is internally contradictory across sources** (see the
  warning above) and needs per-country verification before client use.
- **Market-size figures are vendor/blog-sourced**, not read from the research
  firms' own reports. The 30-35% CAGR consensus is the quotable part; the
  point estimates are not.
