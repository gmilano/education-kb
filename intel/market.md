---
industry: education
region: Global
updated: 2026-10-29
---

# Education AI — Market Map and Opportunities

**Pass `p527` · 2026-10-29.** Figures are attributed to the source that produced
them. Where sources disagree the disagreement is shown rather than averaged away,
because an averaged number is a number nobody published.

## Global market size — four firms, one wide band

| Source | 2026 | Forecast | CAGR |
|---|---|---|---|
| Precedence Research | **USD 9.58B** | USD 136.79B by 2035 | 34.52% (2026-2035) |
| Resourcera | USD 10.4B | USD 32.27B by 2030 | — |
| HolonIQ | USD 12.3B (2026, global) | — | — |
| Range across firms (roundup) | **USD 6.4B – 12.3B** | ~USD 32B by 2030 (low end) | ~30-35% cluster |

**Read the band, not the point.** A ~92% spread between the low and high 2026
estimate means the methodology is doing more work than the market. What the
sources agree on is the *growth rate* (30-35%) and the *regional ranking*, and
those are the usable parts.

Regional share: **North America ~36%** (largest), **APAC fastest-growing at
35.3% CAGR**.

## Adoption — better evidenced than market size

| Signal | Figure | Source |
|---|---|---|
| Students using AI in their studies (16 countries) | **86%** | Digital Education Council, 2025 |
| University students using AI | 92% (up from 66%) | K12 Academics, *State of AI in Education 2026* |
| K-12 teachers using generative AI for work | **25% → 53%** in one year | RAND, 2025 |
| K-12 students using AI for school | 54% | RAND, 2025 |
| Time saved by weekly teacher AI users | **5.9 hours/week** | Gallup + Walton Family Foundation, 2025 |
| US teachers using AI tools | 60% | Child Trends / US Dept. of Education analysis |
| 🆕 Higher-ed institutions in **Europe + North America** with AI guidance in place or in development | **70%** | regional overview, 2026 |
| 🆕 LATAM higher-ed institutions using AI somewhere | **87%** | **UNESCO IESALC + UNU-IAS**, 200 institutions / 19 countries |
| 🆕 …of those, with a **formal AI strategy** | **26%** | same study |
| US public schools with formal AI policies for students | "most still lack" one | Child Trends / US Dept. of Education |
| Schools with rules governing AI use | **under 10%** | roundup, unattributed to a primary |

**This gap is the commercial thesis, and the UNESCO pair now quantifies it
precisely.** 87% using, 26% with a strategy — a 61-point governance deficit, from
a named primary with a stated sample. Adoption is near-universal among students
and past half among teachers, while governance is near-absent. The scarce good is
not a tutor — it is a **defensible, auditable** tutor. Every regional opportunity
below is a variation on that sentence.

⚠️ *The "under 10%" figure appears in a secondary roundup without a primary
citation. Treat it as directional. The RAND, Gallup, Digital Education Council and
UNESCO IESALC figures carry named primaries and can be quoted to a client. The
X-Pilot report's headline statistics (42% learning-outcome gain, 83% planning
AI-TA deployment) are vendor-blog figures — **do not quote them.***

## Opportunities by region

### North America

**Regulatory posture.** State-led and moving fast: **134+ bills across 31 states**
on AI in K-12 and higher education (MultiState and FutureEd trackers), mostly on
data privacy, classroom-use limits and curriculum. Named 2026 statutes:

| Jurisdiction | Instrument | What it requires |
|---|---|---|
| **Maryland** | AI Ready Schools Act | All **24** local districts must adopt aligned AI policies within **120 days** of MSDE guidance |
| **Oklahoma** | S.B. 1734 | Written district AI policy **before the 2027-28 school year**; **bans AI as the main basis for high-stakes decisions** |
| 🆕 **Idaho** | S.B. 1227 | Student **data privacy** for AI tools in schools |
| 🆕 **Utah** | H.B. 218 | Required **grade 7/8 digital-skills course including AI literacy** |
| **Virginia** | H.B. 1186 | AI Innovation in Education Pilot Program |
| **Federal** | **H.R. 8747**, K-12 AI Literacy and Readiness Act of 2026 | Advanced out of House Education & Workforce Committee on **21 July**, largely along party lines; would let schools spend federal funds on AI curriculum |

**Players.** Instructure (Canvas) dominates higher-ed LMS; the NEA and AFT have
issued AI guidance (and drawn criticism for it from Defending Education); a
student-authored national framework from all 50 states, published via Day of AI,
rejects both an outright ban and unrestricted adoption.

**Opportunities.**
1. **District policy-compliance layer.** Five states now mandate district-level
   AI policy or curriculum and one forbids AI-determined high-stakes decisions. A
   deployment that *cannot technically* let a model decide a grade —
   human-in-the-loop enforced in code, with an audit trail — is a procurement
   requirement, not a feature. Build the acceptability yardstick on
   [anthropics/k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills)
   eval rubrics (Apache-2.0, 601★) and the model-side yardstick on
   [pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark)
   (MIT) — CDPK and SEND answer *"does this model know how to teach"*, which is
   the question an Oklahoma-compliant procurement actually asks.
2. **Canvas-attached agents.** Canvas is AGPL-3.0 and must not be forked;
   [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) (MIT,
   308★, v1.16.0 Oct 2026) is a ready, licence-clean seam into the dominant North
   American LMS — and the most mature LMS-MCP bridge in the sector for any
   platform.
3. **Teacher time recovery, measured.** 5.9 hours/week is a defensible ROI number
   for a lesson-prep and feedback agent — and it is measurable, which makes it
   sellable to a district CFO rather than a CIO.
   🆕 [`SirhanMacx/Claw-ED`](https://github.com/SirhanMacx/Claw-ED) (MIT, 63★) is
   a working, honestly-scoped reference for exactly this shape: local-first,
   single-teacher, lesson drafts from the teacher's own curriculum, teacher review
   before use. Its explicit *"not multi-tenant"* limit is the gap a studio fills.

### EMEA

**Regulatory posture — re-verified from source this pass, with three dates
`p526` did not carry.** The **Digital Omnibus, Regulation (EU) 2026/1744**, was
published in the Official Journal on **24 July 2026** and has been in force since
**27 July 2026**. It moved the high-risk compliance deadline for stand-alone
Annex III education AI — grading, admissions triage, programme assignment, exam
proctoring, access to qualifications — from **2 August 2026 to 2 December 2027**.

| What | Date | Status |
|---|---|---|
| **Article 50 transparency** (tell users they are dealing with an AI) | **2 Aug 2026** | 🔴 **live now — not delayed** |
| Emotion-recognition AI in schools | Feb 2025 | 🔴 **banned — live now** |
| 🆕 Two new Article 5 prohibitions added by the Omnibus | **2 Dec 2026** | phasing in — ~5 weeks out |
| 🆕 National AI regulatory sandboxes | **2 Aug 2027** | deadline moved |
| **Annex III high-risk** (stand-alone education AI) | **2 Dec 2027** | moved from 2 Aug 2026 |
| 🆕 **Annex I** (AI as a safety component of a regulated product) | **2 Aug 2028** | |
| 🆕 **High-risk systems used by public authorities, including those already in service** | **2 Aug 2030** | separate, much later date |

🆕 **That last row is the most commercially significant line in this file for
EMEA public-sector work.** State schools and public universities *are* public
authorities across most of the EU. A system already in service there has until
**2 August 2030** — not December 2027. The practical consequence: **the private
and the public education buyer in the same country are on different clocks, more
than two and a half years apart.** Do not sell them the same urgency, and do not
let a public client be told they have 13 months when they may have 45.

**What that means commercially:** a **~25-month build window** on new high-risk
education AI, with transparency and the emotion-recognition ban live *now* and
two fresh prohibitions landing in about five weeks.

🆕 The **OECD 2026 Digital Education Outlook** reportedly recommends institutions
move **beyond general-purpose AI tools toward purpose-built educational AI** —
which is procurement language for "a generic chatbot will not clear review", and
the single best third-party sentence to quote into an EMEA pitch.

**Players.** Europe captured **62.3% of year-to-date 2026 edtech capital** (up
from 34.5% for full-year 2025) per trade aggregation. Named: **Multiverse**
(London, ~$70M at a ~$2.1B valuation), **Gizmo** (London, $22M Series A,
15 Apr 2026), **Ed.ai** (France, ~€5M seed, Sept 2026), **Lucida AI** ($5.4M seed,
Apr 2026, voice-first language coach), **Third Space Learning** ($5.94M growth
equity for *Skye*, a spoken maths tutor), plus AMBOSS, Preply and Knowunity.
Middle East and Africa are an order of magnitude smaller: **Dawraty** (Kuwait,
$2M seed, Qatar Development Bank), **3C Coding School** (Egypt, $3M seed for Saudi
expansion), **Eyone** (Dakar, Senegal). Gulf governance bodies moving unusually
fast relative to infrastructure: **KHDA** and the **UAE Ministry of Education**.

**Open-source anchors, placed:** [OpenOLAT](https://github.com/OpenOLAT/OpenOLAT)
(Apache-2.0, Switzerland), [ILIAS](https://github.com/ILIAS-eLearning/ILIAS)
(GPL-3.0, Germany), [Ralph LRS](https://github.com/openfun/ralph) (MIT, France),
[Dolos](https://github.com/dodona-edu/dolos) (MIT, Ghent — read from its
copyright line), [Open TutorAI CE](https://github.com/Open-TutorAi/open-tutor-ai-CE)
(BSD-3-Clause, **Morocco**), 🆕
[pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark)
(MIT, **Fab Inc**, UK-founded, LMIC focus) and 🆕 — read, not shipped —
[Lumen](https://github.com/ahmedEid1/lumen) (**GPL-3.0**, Essen, Germany).

**Opportunities.**
1. **AI Act conformity scaffolding, now priced per buyer type.** Dec 2027 for
   private providers, **Aug 2030 for public authorities' in-service systems**,
   Article 50 and the emotion-recognition ban enforceable today, two new
   prohibitions on 2 Dec 2026. An **audit-and-remediate engagement needs no new
   technology at all** and can start this quarter; the conformity build (technical
   documentation, logging, human oversight, risk management) follows on the clock
   that matches the client.
2. **Sovereign, self-hosted tutoring.** EU public-sector procurement rewards code
   provenance. OpenOLAT (Apache-2.0, Swiss) + a locally served model + Ralph for
   xAPI records is a stack with no US cloud dependency in the learning path — and
   the OECD "purpose-built, not general-purpose" line is the argument for it.
3. **MEA leapfrog, built on the Morocco row.** Open TutorAI CE is BSD-3-Clause
   with 194 forks against 114 stars — evidence of deployment, not hype. The
   natural base for francophone and Arabophone North Africa and Gulf work.
4. 🆕 **Pedagogical evaluation as a billable deliverable.** Fab Inc's CDPK/SEND
   benchmark is MIT, and **SEND** — special educational needs and disabilities —
   is where European regulators and parents apply the most pressure and where
   almost no vendor can show evidence. Running it is cheap; being the firm that
   ran it is the differentiator.

### APAC

**Regulatory posture — no single model.** Binding AI rules: **South Korea, China,
Vietnam**. Guidance and existing law: **Japan, Singapore, Hong Kong, Australia,
India**. **South Korea's AI Basic Act** is the region's landmark statute (sources
disagree on whether it is the region's first or the world's second comprehensive
AI law — the framing, not the fact, is in dispute). China regulates recommendation
algorithms, deep synthesis, generative AI services and **AI-generated-content
labelling**, with a non-binding AI-agent opinion effective **15 July 2026**. Japan
is promotion-led — its 2025 AI Promotion Act carries no explicit penalties.
**Australia's National AI Plan relies on existing law** rather than a standalone
act. **India requires prominent labels and provenance markers on AI-generated
content from 20 Feb 2026** and *plans* compulsory AI and computational thinking
**from Class 3 in the 2026-27 academic year**.

🆕 **Vietnam's risk-based AI law gives education a longer runway than other
sectors: an 18-month transition period for systems already in service.** That is
the kind of sector-specific carve-out that decides a sequencing decision, and it
makes Vietnam the easier APAC entry point for a product already running elsewhere.

⚠️ *Sources conflict on curriculum status: one claims China and the UAE are the
only countries running compulsory national AI curricula since the 2025-26 school
year, which sits badly with India's rollout being described as planned. UNESCO
separately reports China, Japan, Korea and Singapore integrating AI curricula, and
notes that **adoption needs infrastructure, connectivity and teacher training, not
just policy** — in much of the region basic educational needs come first. Verify
per country before quoting.*

**Players.** **TAL** (China, pivoted into AI learning hardware), **ByteDance
Gauth**, **PhysicsWallah** (India, own AI tutor). 🆕 **Public infrastructure is
the scale player India's commercial market cannot match: NCERT's DIKSHA** already
reaches teachers and students nationally. **SEAMEO INNOTECH** is the regional
body for Southeast Asia. Sector context matters: China shut its ~$100B private
tutoring industry in 2021 and India's BYJU'S collapsed into insolvency — the
market is rebuilding around AI tutoring from a low base of trust. Ipsos Education
Monitor 2026 finds **lower** support for banning AI in schools across Asian
markets, with **Australia and New Zealand more** supportive of a ban.

**Open-source anchors, placed — the strongest supply position of any region.**
Four of the thirteen agents on [`../agents/top.md`](../agents/top.md) are APAC,
including both of the two largest in the world:
[DeepTutor](https://github.com/HKUDS/DeepTutor) (Apache-2.0, **49.0k★**, Univ. of
Hong Kong) and [OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) (MIT, **41.8k★**,
Tsinghua), plus 🆕 [lineage-skill](https://github.com/JuneYaooo/lineage-skill)
(Apache-2.0, 462★, China) and
[Educhain](https://github.com/satvik314/educhain) (MIT, 387★, **India** — placed
this pass off its licence-file copyright line, `educhain.in`). **This is still
the single most actionable supply fact in this file.**

**Opportunities.**
1. **Build on the APAC agents, not around them.** DeepTutor and OpenMAIC are
   Apache-2.0 and MIT, both shipped releases on 28-29 Oct 2026, and together carry
   **90.8k stars**. Anywhere in the world, the fastest credible tutoring prototype
   starts from one of these two.
2. **Content-provenance compliance as a product.** India (20 Feb 2026) and China
   both require AI-content labelling. Generated lesson material needs provenance
   metadata baked in at authoring time. 🆕 **`lineage-skill` is the on-ramp:** it
   is Apache-2.0 and already produces **source-backed** lessons — provenance is
   its design, not a retrofit. Emit H5P with that provenance attached and the
   labelling obligation is satisfied structurally rather than by policy.
3. **India's Class-3 curriculum rollout, through DIKSHA.** A compulsory AI subject
   from Class 3 across 2026-27 is a teacher-training and
   content-at-national-scale problem, and DIKSHA is the distribution that already
   exists. Kolibri (MIT, offline-first) plus a content-generation agent addresses
   the connectivity constraint that will otherwise decide the outcome.
4. **ANZ needs the restraint story, not the capability story.** The one market in
   this region where public opinion leans toward *banning* AI in schools. Lead
   with controls, provenance and integrity tooling
   ([Dolos](https://github.com/dodona-edu/dolos), MIT).
5. 🆕 **Vietnam first for a port.** The 18-month education transition is the
   softest landing in the region for a system already in service.

### LATAM

**Regulatory posture — fragmented, and now measured.** 🆕 A 2026 **Universidad de
los Andes** study counts **716 AI-related instruments across 23 countries and
territories, more than 80% of them from 2023 onward** — the scale of the churn,
quantified. No regional AI law exists. Country detail:

- **Brazil** — **PL 2338/2023** at an advanced legislative stage, draft includes
  education provisions on AI literacy and reskilling; the data protection
  authority (**ANPD**) is running an **AI regulatory sandbox pilot through
  December 2026**; Brazil signed an AI and tech regulation agreement with the EU
  in June 2026.
- 🆕 **Uruguay** — **first Latin American country to sign the Council of Europe's
  AI convention** (2025). The region's strongest international-alignment signal.
- 🆕 **Peru** — framework with **regulatory sandboxes and a phased rollout**.
- 🆕 **Colombia** — national AI policy **CONPES 4144**, adopted February 2025.
- 🆕 **Mexico** — federal, risk-based AI bill **in the Senate**; still **no
  comprehensive AI law in force**, and the National AI Strategy dates to 2018.
- **Argentina** — the president submitted a bill that would leave AI
  *unregulated*, the opposite direction from Brazil.

ALSUR characterises the whole picture as *legislative reactivity without a
comprehensive legal framework*; commentators warn the overlapping initiatives are
themselves a source of uncertainty.

**Adoption.** 🆕 The **UNESCO IESALC + UNU-IAS** study of **200 institutions in 19
countries** is the best-evidenced regional figure now available: **87% use AI
somewhere, only 26% have a formal AI strategy**, adoption driven by **individual
faculty and students rather than institutional policy**, with public institutions
more resource-constrained than private. The IDB separately reviewed **193 regional
initiatives**: **59% used generative AI, 27% used language models**, concluding the
region *recombines* AI tools in its own ways rather than importing them wholesale.
Counterweight: **CENIA (Chile) finds 13 of 19 LAC countries studied have not yet
introduced early AI adoption in schools**, and adoption in urban schools is
concentrated in better-resourced and private institutions, with rural and
Indigenous-language contexts underserved. **Google.org has committed $4.6M to AI
literacy across nine countries including Brazil and Mexico, targeting 1.25M
students by 2028.**

**Players.** 🆕 **UNESCO is the most active institutional actor**: it launched the
**Observatory on Artificial Intelligence in Education for Latin America and the
Caribbean in Santiago on 14 April 2026**, runs capacity-building for officials in
Ecuador and Chile, and has an agreement with **Tecnológico de Monterrey** on AI in
education. **ECLAC** coordinates a regional AI working group with **Chile's CENIA**
and **Uruguay's AGESIC**. The World Bank, UNICEF and regional development banks
fund most lower-income pilots; **Derechos Digitales** and **Fundación Karisma**
are the digital-rights counterweight. From the 2026 Holon IQ LATAM EdTech 100:
**Teachy** (Brazil, AI lesson preparation — a regional incumbent that has expanded
into Asia), **Ginia** (Mexico, employability), **Vetto** (Brazil), **Mattilda**
(Mexico, billing for private schools). The list shows AI positioning shifting
**toward teachers**, with upskilling losing ground as a category.

**Open-source anchors, placed:** [i-educar](https://github.com/portabilis/i-educar)
(GPL-2.0, 722★) — Brazil's largest free school-management system, born in Itajaí
(SC) municipal government, on the federal Public Software Portal since 2008 — plus
[Chamilo](https://github.com/chamilo/chamilo-lms) and
[RosarioSIS](https://github.com/francoisjacquet/rosariosis) for ES/PT
localisation. 🆕 **And one asset that is LATAM *data* rather than LATAM code:**
[pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark)
(MIT) is built on exams from **Chile's Agencia de la Calidad de la Educación and
CPEIP**, credited on the repository. The region's teaching standards are already
inside an open benchmark — that is leverage nobody is using.

**Opportunities.**
1. **Teacher-facing first, mirroring where the market already moved.** Teachy's
   position and the EdTech 100 both say the buyer is the teacher, not the learner.
   Lesson preparation and feedback in Portuguese and Spanish, built on
   [Educhain](https://github.com/satvik314/educhain) (MIT) or 🆕
   [lineage-skill](https://github.com/JuneYaooo/lineage-skill) (Apache-2.0,
   source-backed) emitting
   [H5P](https://github.com/h5p/h5p-php-library) for portability.
2. **The i-educar modernisation engagement.** Hundreds of Brazilian municipalities
   run GPL-2.0 school management from 2008. The work is an integration layer —
   enrolment, attendance and performance signals into an advising agent — not a
   replacement, and GPL-2.0 means it must stay across a service boundary.
3. **Use the ANPD sandbox as the de-risking vehicle** — and now Peru's too, which
   also has sandboxes. A pilot inside Brazil's regulatory sandbox before December
   2026 produces a compliance story that survives PL 2338 becoming law. That is a
   reason to start now rather than wait.
4. 🆕 **Sell the strategy, not the tool — the 87/26 split is the pitch.** UNESCO
   IESALC says 87% of LATAM higher-ed institutions already use AI and only 26%
   have a strategy, with adoption driven bottom-up by individual faculty. The
   institutions do not need to be sold AI; they need **the governance layer over
   the AI already in their buildings**: inventory, policy, human-in-the-loop
   enforcement, xAPI audit trail via [Ralph](https://github.com/openfun/ralph)
   (MIT). This is a consulting-led engagement with a software tail, and it is the
   highest-probability LATAM opening on this file.
5. 🆕 **Build the Chilean benchmark into a Spanish-language evaluation offer.**
   CDPK/SEND over Chile's own teacher-certification exams, in Spanish, is a
   credible answer to "does this model know how to teach *here*" — and it is MIT.
   Pair it with CENIA, which already co-chairs the ECLAC working group.
6. **Thirteen of nineteen countries have not started.** CENIA's number is the
   greenfield read: national AI-literacy programmes with no incumbent to displace.
   Kolibri (MIT, offline-first) is the right base where connectivity binds.

## Declared gaps this pass

Written down because an unstated gap is indistinguishable from coverage.

- **No authoritative ranking of EMEA AI-education vendors.** The funding figures
  above come from trade aggregators that disagree with each other on round sizes
  and company locations. No primary announcements were checked.
- **North America: Canada and Mexico education-specific AI policy returned almost
  nothing again.** Searched this pass; the regional overviews cite Canada's
  *workplace* AI rules, not education policy. **The NA leg is effectively a US
  leg**, for the second consecutive pass.
- 🆕 **EMEA: no national-level detail for the UK, Germany, France, Saudi Arabia
  or the UAE**, and **no adoption data for Africa at all** — not thin data,
  *absent* data. The EMEA leg is an EU-regulation leg plus a funding list. A pass
  targeting the UK DfE, UAE KHDA and specific African education ministries would
  fix it; this pass did not.
- **No LATAM-origin open-source education agent exists on these shelves.** The
  region's shipped strength is school management (i-educar), not agents. What
  LATAM *does* contribute on the agent legs is **data** (Chile → CDPK/SEND).
- **The "under 10% of schools have AI rules" figure has no primary citation.**
- **APAC curriculum status is internally contradictory across sources** (see the
  warning above) and needs per-country verification before client use.
- **Market-size figures are vendor/blog-sourced**, not read from the research
  firms' own reports. The 30-35% CAGR consensus is the quotable part; the point
  estimates are not — and the band widened this pass rather than narrowing.
- 🆕 **The EU public-authority 2 Aug 2030 date comes from one commentary source**
  among the several that agree on 2 Dec 2027. It is the most commercially
  consequential line in the EMEA section and the least corroborated — **read
  Regulation (EU) 2026/1744 itself before putting that date in front of a public
  client.**
