---
industry: education
region: Global
updated: 2026-10-10
---

# Education — market, players and opportunities

**Pass 92, 2026-10-10.** ⏱️ **Second pass of this date.** Regional sweep run once globally and once per
region (North America, EMEA, APAC, LATAM), plus four gap-targeted queries. Every instrument is dated and named. Where a region returned nothing on
a line of enquiry, that is written down rather than left blank.

🔴 **Sourcing caveat that governs this whole file.** The four primary sources this pass most needed —
`cbse.gov.in`, `digitaleducationcouncil.com`, `hepi.ac.uk`, `unu.edu` — are **blocked by this session's egress
allowlist**: `curl` returns `000`/0 B and `WebFetch` returns `ENOTFOUND` on the same hosts. Per `P950` they
were not retried host-by-host. 🟢 **Everything below sourced from them is labelled *search-summary* and is not
presented as a primary read.** Figures carrying a 🟢 were reproduced in at least two independent summaries.

## Market size — the figures disagree, and the disagreement is the finding

| source | 2026 figure | forecast |
|---|---|---|
| Precedence Research | **USD 9.58 B** | ~USD 136.79 B by 2035 |
| Research and Markets | **USD 10.6 B** | USD 42.48 B by 2030 |
| Grand View Research | **USD 11.4 B** | 25.9 % CAGR to 2033 |
| 🆕 IMARC (2025 base) | USD 6.4 B (2025) | USD 79.6 B by 2034 |
| 🆕 unnamed aggregator (2025 base) | USD 8.3 B (2025) | USD 57.2 B by 2033 |

🔴 **The spread got worse, not better.** Adding this pass's two 2025-base estimates, the implied 2026 band runs
from roughly **USD 7 B to USD 11.4 B**, and the 2033–2035 projections differ by more than **3×**.
🟢 **Use the band — "roughly USD 10 B in 2026, growing fast" — and never a single decimal figure in a client
deck.** 🔵 **New, and more useful than any of the point estimates: one analysis rates the market's maturity at
35 / 100, i.e. most institutions are still piloting.** That is consistent with every adoption figure below and
is the number to actually argue from.

**Segment splits (single-source, directional):** cloud delivery **71.22 %** of 2024 revenue · K-12 **45.62 %**
of adoption · STEM **34.78 %** of revenue, with **language learning the fastest-growing segment**.

**Funding, which is the more reliable signal:**
- 🔴 Global edtech VC was **~USD 1 B in H1 2026, down 26 % year on year.**
- 🟢 But AI-focused education companies took **USD 4.2 B in 2025 — 62 % of all edtech funding.**
- 🟢 Concentration is extreme: the **top 10 AI-education startups hold ~60 %** of reconstructed funding.
- Named rounds and commitments: **Preply, USD 150 M (Jan 2026)**, valuation USD 1.2 B · 🆕 **Carnegie Mellon
  with the Gates Foundation, USD 55 M into AI courseware** · 🆕 **a government commitment of USD 169 M to
  responsible AI in higher education, Q1 2026** — 🔴 **the source does not name the government and it is not
  attributed here.**

🔵 **Reading, unchanged and now better supported: the category is contracting while the AI slice expands.**
For a services studio that is favourable — institutions still need to build, and the vendors who could have
built it for them are fewer.

## Commercial players

**Horizontal / platform:** Microsoft (Education AI Toolkit updated **April 2026** with agentic capabilities),
Google, AWS, IBM. 🆕 **OpenAI launched a country-level education programme with eight national partners in
Q1 2026** and 🆕 **appointed a dedicated Australia/New Zealand policy lead** as Canberra tightened AI
governance and copyright rules — the first time a model vendor appears in this file as a *regulatory* actor
rather than a supplier.
**Education incumbents:** Pearson (🆕 **multi-year AI learning alliance with TCS**, aimed at employer skills
gaps), Anthology, Carnegie Learning, DreamBox Learning, BridgeU, Fishtree.
**APAC-specific:** Byju's, Chinese state-backed programmes, 🆕 **LearnUpon** (new Sydney HQ, `Create+` AI
course authoring), 🆕 **NIIT MTS** (16th consecutive year on Training Industry's Top 20 custom content
developers, 2026, citing AI-led design).

🟢 🆕 **The standing Khanmigo discrepancy is resolved, and the cause is the instrument, not the market.**
Pass 90 recorded that **Khan Academy / Khanmigo appeared in no market-research player list** despite being the
most visible AI tutor in public discourse. 🟢 **Khan Academy's own 2026–27 district renewal materials show the
opposite of absence:** the platform has been rebuilt around *AI-enhanced mastery learning* with Khanmigo
positioned as both student learning coach and teacher assistant, a classroom-centred redesign, district
implementation tooling, and a 2026–27 content roadmap (updated Illustrative Mathematics for grades 6–8 and
Algebra 1 by summer 2026; Amgen-partnered middle-school biology with Khanmigo-supported activities).
🔴 **What is still absent is any district count, enrolment figure or share number — because Khan Academy is a
nonprofit that does not publish them.** 🔵 **Market-research player lists rank by revenue share, so an
organisation with no reported revenue share cannot appear in one.** The absence was an artefact of ranking by
revenue; it was never evidence of market position. **Closed as mis-posed.**

## Regulatory state of play

🆕 **This table now has two kinds of row, and the distinction is new this pass.** Rows that **regulate AI
systems** (risk classification, oversight duties) and rows that **mandate AI instruction** (curriculum). They
are different products — see `intel/trends.md` `T7`.

### Instruments that regulate AI systems

| jurisdiction | instrument | date | status |
|---|---|---|---|
| 🇪🇺 EU | **AI Act** — education explicitly **high-risk** (exam scoring named by the Commission) | enforcement powers from **2 Aug 2026** | 🟡 **High-risk compliance deadline moved to 2 Dec 2027** by the Digital/AI Omnibus (Council approval **29 Jun 2026**); embedded high-risk systems **2 Aug 2028**. 🔴 **Blogs still citing Aug 2026 for high-risk duties are outdated — and this pass found that exact error again in a current source.** |
| 🇪🇺 EU | 🆕 **AI Act Article 4 — staff AI-literacy duty** | 🟢 **already in force; NOT deferred** | 🟢 **The sharpest EMEA point on this page.** The one AI Act duty that already binds an educational institution is the obligation to ensure AI literacy among staff operating AI systems. It did **not** move to 2027 with the high-risk obligations. |
| 🇰🇷 South Korea | **AI Basic Act** — education is a **"high-impact AI"** area | in force **22 Jan 2026** | 🟢 The region's most comprehensive law |
| 🇻🇳 Vietnam | **AI law**; high-risk list names education (automated assessment, behavioural monitoring) | enacted **1 Mar 2026** | 🟢 In force |
| 🇹🇼 Taiwan | **AI Basic Act** | passed **Dec 2025** | 🟢 |
| 🇺🇸 Ohio | first state to **require every K-12 district to adopt a formal AI policy** | deadline **1 Jul 2026** | 🟢 Binding |
| 🇺🇸 federal | **K-12 AI Literacy and Readiness Act of 2026** (H.R. 8747) | committee markup **Jul 2026** | 🟡 Advanced from committee; 🔴 current status still not confirmed — **unresolved for a second pass** |
| 🇦🇺 Australia | **National Framework for Generative AI in Schools** | 2024 | 🟡 **Guidance, not binding** — transparency, safety, responsible use; states pilot independently |
| 🇲🇽 Mexico | **SEP — 10 recomendaciones** for ethical/critical genAI use in HE | **15 Apr 2026** | 🔴 **Recommendations, not binding.** Regulation reported *in preparation*; not recorded as in force. |
| 🇨🇱 Chile | **Política Nacional de IA** (2021) + AI bill (Boletín 16821-19) | — | 🟡 Second trámite in the Senate, 🔴 **and the Executive will replace the bill.** Not citable as a compliance driver. |
| 🇧🇷 Brazil | **PL 2338** | Senate approved 10 Dec 2024 | 🔴 *"Aguardando Parecer"* in the Chamber at 2 Sep 2026; vote after the October elections. 🔴 **Education-as-high-risk not verifiable.** No sectoral education rule. |
| 🇨🇴 Colombia | national AI strategy | — | 🔴 **No sectoral education regulation** |
| 🇸🇬🇯🇵 Singapore, Japan | voluntary guidelines on existing law; Japan standing up testing/assurance institutes | — | 🟡 Deliberately non-binding **as to AI systems** — but see the curriculum table |

### 🆕 Instruments that mandate AI instruction

| jurisdiction | instrument | date | reach |
|---|---|---|---|
| 🇨🇳 China | **Ministry of Education** — compulsory AI instruction from **age six**, tiered primary → secondary | 🟢 from **Sep 2025** | 🟢 **≥ 8 hours per year, nationwide.** Moved past pilots to a structured tiered curriculum. 🔴 Critics note ethics, data privacy and equal access lag the rollout. *(search-summary; ministry document not reachable)* |
| 🇸🇬 Singapore | **Ministry of Education** — AI literacy built into curriculum, co-curriculum and self-directed learning, with **developmental milestones** | 🟢 announced **Mar 2026** | Delivered through **Student Learning Space (SLS)** and IMDA's **AI for Fun** modules, **reaching all schools in 2027** |
| 🇮🇳 India | **CBSE** — *Computational Thinking and Artificial Intelligence*, **Classes 3–8** | 🟢 **session 2026-27**; notification dated **9 Apr 2026** | Aligned to **NEP 2020** and **NCFSE 2023**; reported compulsory for CBSE-affiliated schools with **no board exam**. 🔴 Class 9 treatment is contradicted between sources and is **not** recorded. |
| 🇪🇺 EU | **AI Act Art. 4** staff AI-literacy duty | 🟢 in force | Institution-level, not pupil-level — and it is a *duty on the deployer*, which makes it purchasable |

🔴 **One misattribution recorded so it is not repeated:** a source credits "the first nationwide AI mandate" to
a **May 2025 cabinet decision**, which on inspection appears to describe the **UAE**, not China. **Not used.**

## Opportunities by region

### North America

🆕 🟢 **The regulatory centre of gravity is the states, and one of them now has a dated, binding deadline.**

| instrument | status | why it matters |
|---|---|---|
| 🆕 **Ohio** — mandatory district AI policy | 🟢 **first state to require EVERY K-12 district to adopt a formal AI use policy, deadline 1 Jul 2026** | 🔵 **The one dated, binding, already-passed K-12 AI obligation in the US.** ~600 districts each needing a defensible policy and the governance to back it — a procurement event with a date on it. |
| 🆕 **~134 AI-in-education bills across 31 states** in the 2026 session | 🟡 in progress; trackers disagree (another counts ~100 K-12-specific bills) | 🔴 **The count is contested, so use the shape, not the number.** Three clusters: **student-data privacy** (California AB 1159 would bar using student data to train models; Idaho SB 1227 would mandate protections), **classroom restriction**, and **curriculum**. |
| 🆕 **Human-oversight floors** | 🟡 reported for **Oklahoma** and **Maryland** — AI barred from high-stakes decisions about students | 🔵 Converges with the EU's Annex III posture: the same product needs a human-decision gate on both continents. |
| **H.R. 8747** — K-12 AI Literacy and Readiness Act of 2026 | 🟡 advanced at a **21 Jul 2026** markup; 🔴 **status beyond that unresolved for a third pass** | Would amend ESEA. Carried as a watch item, not a planning assumption. |

🔵 **The buyable consequence.** 30+ states have *guidance*; Ohio has a *deadline*. 🟢 **District-level
AI-use policy, data-protection review and staff training is the near-term North American engagement** —
and it is governance work, not model work. 🔴 **Canada and Mexico returned almost nothing again** under a
North America query; Mexico surfaces only under a Spanish-language LATAM query (see below), which is
`P955`/`P870` holding once more.


**Demand signal.** ~36 % of the global AI-in-education market (**~USD 3.68 B, 2026**); generative-AI adoption
among North American educational organisations reported at **86 %**. 60 % of US K-12 teachers used AI tools in
the 2024–25 school year, 32 % at least weekly. Market sizing for the region alone: **USD 951 M (2024) → USD
2 303 M (2029)**.
🆕 **Two readiness figures that are the actual sales argument:** only **~10 % of institutions have formal AI
guidelines**, and **71 % of US teachers report no AI training.**

**The opening is governance and capability, not tooling.** **134 AI-in-education bills across 31 states in
2026**; 30+ states have guidance documents; Ohio makes a district-level AI policy **mandatory by 1 Jul 2026**.
Districts are diverging hard — Katy ISD bans genAI chatbots for K-6, New York City has a one-year
student-facing moratorium through grade 8. California's **AB 1159** would bar training on student data absent
direct school benefit; Oklahoma and Maryland are moving on human oversight of high-stakes decisions.

🟢 **Sell the compliance layer.** Thousands of districts have a legal deadline and no instrument. An auditable
record of *what the AI did, to which learner, on whose data, reviewed by which human* is a deliverable, and the
permissive substrate exists: `yetanalytics/lrsql` (Apache-2.0) + `adlnet/xAPI-SCORM-Profile` (Apache-2.0) for
the trail, `Sakai` (ECL-2.0) where an HE platform is in scope. See `P91-B`.
🟢 🆕 **And sell the teacher-capability layer, which is now measured as the larger hole**: 71 % untrained
against 10 % with guidelines means the binding constraint is people, not software.
🟢 🆕 **The accessibility build is now cheaper than pass 90 thought.** Three **permissive, AI-driven WCAG
checkers** were found and verified this pass (`agents/top.md`), so Section 508 / WCAG exposure can be addressed
by composition rather than from scratch. 🔴 **The instructional-alignment checker still does not exist
permissively** — that narrower gap is the remaining build.
🔴 **Procurement note:** the official **SCORM 2004 conformance test suite carries no licence** (`adlnet`, three
of five repos ungranted), so conformance must be demonstrated against `ADL_LRS` (Apache-2.0) instead.

### EMEA

🆕 🟢 **Assessment is where the EU AI Act and the market meet, and there is now a dated sector-scale pilot.**

- 🟢 **Jisc reported early findings in May 2026 from year-long AI marking-and-feedback pilots across
  **38 UK colleges and universities.** *(search-summary)* 🔵 **This is the most useful EMEA datum of the
  pass**: it is a named sector body, a real cohort size, and it is in **exactly** the activity the AI Act
  classifies as high-risk. A UK pilot is also outside the AI Act — so it is evidence of demand that the EU
  regime will shape rather than suppress.
- 🟢 **What Annex III actually catches, stated concretely** because this is the list a client needs:
  **evaluating learning outcomes**, **screening applicants for admission**, and **monitoring candidates
  during examinations** (proctoring). 🔴 **Automated marking is in the first category.** So the Jisc pilots
  describe a high-risk product category being adopted at sector scale.
- 🔴 **Article 27 adds a Fundamental Rights Impact Assessment** for public bodies — most schools and
  universities — deploying a high-risk system. 🔵 **A deliverable, not a disclaimer**: scope it as a
  work-product with an owner.
- 🔴 **The deadline conflict this KB already tracks (`T4`/`P284`) is re-confirmed, and the sources still
  disagree.** Several vendor pages still say Annex III high-risk applies from **2 Aug 2026**; the later and
  apparently current position is the **Digital Omnibus** deferral to **2 Dec 2027**. 🟢 **What is NOT
  deferred, and is the thing that binds now: Article 4 staff AI-literacy and the emotion-recognition ban,
  both enforceable since 2 Feb 2025.** 🔵 **Emotion recognition is banned in education specifically** —
  which puts a hard line through a whole category of "engagement analytics" proctoring features.
- 🟡 **England updated its generative-AI product safety standards in January 2026** *(search-summary)* —
  a non-EU, UK-specific instrument worth a primary read next pass.


🟢 🆕 **The EMEA measurement gap partly DISCHARGES — for the first time in this KB's history there are
EMEA-specific numbers.** They are national, not continental, and they measure *institutional provision* rather
than student adoption:

- 🟢 **HEPI Student Generative AI Survey 2026** (fieldwork by Savanta, **Dec 2025**, n = **1 054** full-time UK
  undergraduates): only **36 %** feel **encouraged by their institution** to use AI, and only **38 %** say the
  institution **provides** AI tools. *(search-summary; `hepi.ac.uk` blocked)*
- 🟢 **Digital Education Council AI in Higher Education Global Survey 2026**: n = **45 398** (27 284 students,
  18 114 faculty) across **35 countries** — the largest instrument on this page. 🔴 **No regional breakdown
  obtained**, so Europe is inside the sample but not separable from it.
- 🆕 **European Commission** runs a standing survey on AI for teaching and learning via the European School
  Education Platform — a live EU instrument, not a one-off report.
- 🆕 **Council of Europe** (wider than the EU — 46 member states) has a **working conference series on the
  regulation of AI systems in education** through its Education Department, which has floated a **European
  evaluation framework for educational technologies**. 🔵 **A second, non-EU European regulatory track this
  KB had never named.** 🔴 The edition surfaced was **October 2024** and is dated; the current edition was not
  confirmed.

🔴 **Still missing, stated plainly: an EMEA-wide *adoption* percentage.** Provision and encouragement are now
measured (UK); adoption is not. 🔴 **EUA and EDUCAUSE returned nothing** on a targeted query.
🔴 **Rejected, not used:** an aggregator's claim that *"~70 % of institutions in Europe and North America have
or are developing AI guidance"* — untraceable to a primary source and inconsistent with North America's
measured ~10 % formal-guideline figure.
🔴 **Trap recorded:** CompTIA's widely-quoted **94 % of organisations likely to invest in AI training in
2026** is often cited in EMEA contexts; **its respondents are US-only.** Do not use it as an EMEA figure.

**The regulatory opening is a two-deadline story, and most published guidance gets both wrong.**
🟡 High-risk duties land **2 Dec 2027**, not Aug 2026 — a ~14-month build window institutions believe they
have already missed or already survived. 🟢 **But Article 4's AI-literacy duty binds now**, which converts
the pitch from "prepare for 2027" into "you are already non-compliant on staff literacy, and here is the
remedy". Obligations elsewhere land on transparency, **human oversight** and **staff AI literacy**, and the
Act reaches non-EU systems whose outputs affect EU-located students. Supporting instruments: Commission
**ethical AI guidelines for education (May 2026)**, Council conclusions on a human-centred approach, the
**Apply AI Alliance**.

🟢 **EMEA is the best-supplied region on this shelf and the pitch should say so.** `Artemis` (MIT, TU München,
Iris/Athena/Hyperion already built), `OpenOLAT` (Apache-2.0, Switzerland, Koblenz University), `Opencast`
(ECL-2.0), 🆕 **`richie` (MIT, France Université Numérique — the portal layer)**, `Numbas` (Apache-2.0,
Newcastle), 🆕 `Claroline` (AGPL, Belgium), `TAO` (LGPL, Luxembourg), `mentingo` (MIT, Poland), `ILIAS` (GPL,
Germany), `INGInious` (AGPL, UCLouvain). 🟢 **And the instrument now recognises EUPL-1.2**, the grant EU
public bodies are steered toward — the licence most likely to appear in a European public-sector tender.

### APAC

🆕 🟢 **Three binding instruments landed or took effect since this file last listed them, and two name
education as high-risk explicitly. This is the biggest regulatory change of the pass.**

| jurisdiction | instrument | status | why an education engagement must read it |
|---|---|---|---|
| 🆕 **South Korea** | **AI Basic Act** | 🟢 **in force 22 Jan 2026** — MSIT has signalled 2026 as a pilot year with a **one-year grace period on penalties** | 🔵 **The grace period is the window, and it closes.** The most comprehensive AI law in the region; a 2026 engagement can be designed for compliance cheaply, a 2027 one cannot. |
| 🆕 **Vietnam** | first **standalone AI statute in Southeast Asia** | 🟢 high-risk sectors — **finance, healthcare, education** — have until **Sep 2027** | 🔴 **The most operationally demanding regime found anywhere this pass.** High-risk systems require **pre-deployment registration in the National AI Database**, conformity assessment, **mandatory human oversight**, and **incident reporting within 72 hours**. 🔵 A 72-hour clock is an architecture requirement, not a policy one: it means logging, alerting and an owner, designed in. |
| 🆕 **Taiwan** | **AI Basic Act** | 🟢 passed **Dec 2025** | Framework-level; watch for the sectoral implementing rules. |

🔵 **What this does to the regional map.** APAC was previously the *"policy-and-curriculum"* region on this
shelf (China's and Singapore's MoE mandates, India's CBSE). 🟢 **It is now also the region with the hardest
system-level compliance surface** — and the two axes point at different buyers: the mandates are a
**curriculum services** market, the statutes are a **governance and audit** market.
🔴 **Divergence is the defining feature and must not be averaged.** Korea and Vietnam are
comprehensive-and-binding; **Japan is deliberately innovation-friendly and voluntary**; Singapore's
frameworks remain largely **voluntary**; India and Australia still rely on sectoral and privacy law.
🔴 **A single "APAC AI compliance" offer does not exist.** Price per jurisdiction.
🟡 **Public opinion also splits inside the region** — Ipsos Education Monitor 2026 reports **lower** support
for banning AI in schools across the Asian markets surveyed, but **higher** support in Australia and
New Zealand. *(search-summary)*


**Demand signal.** Projected **28.1 % CAGR 2026–2033** — the fastest-growing region. China leads on state
backing; India is the other major market. 🔴 **Trap: the Diligent Institute figure of 57 % of Asian
organisations using AI is enterprise data, not education data.** Do not repurpose it.

🟢 🆕 **The APAC regulatory picture is no longer only about risk classification — it is about mandated
curriculum, and that is a services opportunity rather than a compliance cost.** Binding, education-naming
*system* law in **South Korea** (22 Jan 2026), **Vietnam** (1 Mar 2026) and **Taiwan** (Dec 2025). Against
that, 🆕 **three jurisdictions now mandate AI *instruction*: China (≥8 h/year from age six, Sep 2025),
Singapore (MoE, Mar 2026, all schools by 2027) and India (CBSE, Classes 3–8, 2026-27).**

🔵 🆕 **This corrects a sentence this KB has published for several passes.** The shelf said *"Singapore and
Japan stay deliberately voluntary."* 🟢 **That is true of Singapore's stance on regulating AI systems and
false of its stance on AI in schools** — the MoE has committed to AI literacy across curriculum,
co-curriculum and self-directed learning with developmental milestones, delivered through SLS and IMDA
modules. **Voluntary regulation and mandated curriculum are not the same axis, and conflating them
understated the region's most purchasable commitment.**

🟡 **Australia is the inverse case and the tension is worth naming in a pitch:** its 2024 National Framework
is permissive guidance, while **Ipsos Education Monitor 2026 finds Australia and New Zealand with the
region's strongest public support for banning AI in schools.** Framework-permissive, opinion-restrictive —
so an ANZ engagement sells consent and transparency before capability.

UNESCO: **China and Singapore have established AI-in-education policies; others lag**, and adoption is gated
on IT infrastructure, connectivity and teacher training. The Philippines intends to propose a regional
framework under its **2026 ASEAN chairmanship**.

🟢 **No single APAC offer exists; the per-jurisdiction delta *is* the product** — and it now has two
dimensions: the same tutor needs behavioural-monitoring controls in Vietnam and high-impact documentation in
Korea, *and* the same curriculum needs localising to China's 8-hour tiering, Singapore's milestones and
CBSE's Classes 3–8 scope.
🟢 **APAC is also a supply region:** `DeepTutor` (Apache-2.0, 41k★, HKU) is the most-starred education agent
anywhere; **Moodle itself is Australian** (Perth); `frappe/lms` and `pupilfirst` are Indian; `GibbonEdu` is
Hong Kong; 🆕 `nsip/curriculum-mapper` (Apache-2.0) is Australia's National Schools Interoperability Program;
🆕 `feifei-companion` (Apache-2.0 variant) is a Chinese K-12 companion.
🟢 **`Kolibri` (MIT, offline-first) remains the right answer to UNESCO's connectivity constraint.**

### LATAM

**Demand signal — still the strongest evidence of any region, and now with the numbers corrected.**

🆕 🟢 **Mexico now has a dated education-AI instrument, and it is sub-national — which is why national
queries kept returning nothing.**

- 🟢 **Estado de México reformed Article 61 of its state Education Law in April 2026** to promote the
  responsible, graduated use of AI in upper-secondary and higher education — **the first Mexican state to
  legislate AI in the classroom.** *(search-summary)*
- 🔴 **Mexico still has no general AI law.** It entered H2 2026 with the Senate draft lacking a floor vote
  and no DOF publication. Seven proposals to add AI literacy and ethical use to the **Ley General de
  Educación** are reported pending. 🔵 **So the decision-maker is the state and the institution, not the
  federation** — the same short-cycle posture this file already records for Brazil.
- 🔵 🆕 **`P870` holds a fifth time, and this is the clean demonstration:** *"AI education Mexico
  regulation"* in English returned nothing usable across five previous passes and was recorded as an empty
  region. **The Spanish query returned a dated article-level reform on the first attempt.** The gap was in
  the query language, not in the world.

🆕 🟢 **A named, scaled institutional deployment — the LATAM reference this file lacked.**
**`AyudantIA`, Pontificia Universidad Católica de Chile.** Course-level AI tutors that **the professor
configures and grounds in the course's own bibliography and materials**. Reported scale: **~170–194 agents
across ~100 courses**, **2 300–4 600 students**, **10 000+ conversations**, on Azure OpenAI, with scaling to
new academic units written into UC's **2026–2030** strategy. *(figures vary by source — UC's own news page
and a Microsoft customer story disagree; both ranges given rather than one picked)*

🔵 **Why this is the most useful single row in this file for a LATAM pitch.** It is not open source and is
not a competitor to anything on this shelf — **it is proof that the instructor-configured, course-grounded
tutor is the shape a flagship LATAM university actually bought**, which is exactly the architecture
`agents/top.md`'s `fborrasumh/tutoria` (teacher validates the lesson first) and the new
`LabSirius/TutorIA` (Open edX-integrated, MIT) implement permissively. 🟢 **The reference sells the
pattern; the MIT rows deliver it.**


🔴 🆕 **Two corrections to figures this KB has published:**

| this KB said | what the sources say |
|---|---|
| *"UNESCO IESALC with UNU-IAS, **September 2026**: 200 institutions across 19 countries; 87 % use AI"* | 🟡 **The fieldwork ran August–October 2025.** 200 institutions / 19 countries and 87 % stand; the 2026 date is the publication, not the measurement. 🟢 **And the matching governance figure is 26 %** — just over a quarter have **any** formal framework. |
| *"only **30 % of students and faculty** think their university integrates AI effectively"* | 🔴 **It is students only, and the wording is different: *30 % of students say their institution's current use of AI meets their expectations*.** "And faculty" was not in the source. |

🔴 🆕 **And a third claim is rejected outright.** A panel speaker was reported as saying *"only 30 % of
universities in LATAM have published AI policies."* 🔵 **Three different claims are circulating attached to
the same number 30 %** — students' expectations met, students-and-faculty on effectiveness, and universities
with published policies. 🟢 **Only the first is supported. For institutional policy coverage, use UNESCO's
measured 26 %, which is a different instrument and a different number.** A figure that attaches to three
referents is a figure to stop quoting.

**The measurements that stand, with sample sizes:**
- 🟢 **UNESCO IESALC with UNU-IAS** (fieldwork Aug–Oct 2025): **200 institutions, 19 countries; 87 % use AI in
  at least one area; 26 % have any formal framework.** Governance lags adoption.
- 🟢 **Digital Education Council LATAM Survey 2026** (DEC's own figure: **30 000+ respondents across 29 LATAM
  institutions**; 🔴 a secondary summary says 22 941 students — **the discrepancy is recorded, not resolved**):
  **92 % of students and 🆕 79 % of faculty** actively engaging with AI. Adoption by area — teaching and
  learning leads, then **research 57.0 %, administration 34.1 %, community engagement 20.0 %.**
  🟢 🆕 **The sharpest single row: only 19 % of faculty use AI for feedback on assignments, while 50 % of
  students support it.** 🆕 **47 % of students name clear usage guidelines as a key factor** in building AI
  skills. Participating institutions include UNAM, UPC Peru and PUC Chile.
- Mexico's SEP national survey (Apr 2026): **>60 % of university students *and* teachers use generative AI
  daily**, from 1.5 M+ students and 166 k+ teachers.

**Regulation is the region's defining absence.** 🔴 **No unified regional framework. No sectoral education
regulation in Brazil or Colombia. Mexico's SEP and ANUIES outputs are non-binding. Chile's bill will be
replaced by the Executive.** 🟢 **Consequence: each university writes its own internal code** — the buyer is
the institution, the sales cycle is short, and there is no regulator to wait for.

🟢 🆕 **A named regional instrument this KB had never carried: the Inter-American Development Bank (IADB/BID)**
publishes both an **AI regulation framework for the region** and the **ILIA index**, which tracks AI
readiness, adoption and governance across **19 countries**. 🔵 **For a LATAM engagement this is the
credibility anchor that was missing** — a development-bank index is something a rector's office already
recognises, where a market-research CAGR is not.

🟢 **The sharpest arbitrage on this shelf, restated on corrected numbers: 92 % of students using AI against
26 % of institutions having any framework, with no regulator.** The product is institutional AI governance and
integration — policy, disclosure, assessment redesign, staff capability — delivered per university. Mexico's
**Plan Nacional de IA (ATDT, Apr 2026)** explicitly carries *software público* and technological-sovereignty
pillars with an education→employment component: a named, dated public-sector hook.
🟢 **LATAM supply exists and is placed:** `belentani7/aprende-brasil` (MIT, pt-BR, 205 modules, offline
fallback), `portabilis/i-educar` (LGPL-3.0, Brazil's largest open education system, municipal SIS),
🆕 **`mumuki/mumuki-laboratory` (AGPL-3.0, Argentina — programming practice with automated feedback, in real
classroom use)**, `programadores-obreros/Agente-editor-inet` (GPL-3.0, Argentine INET technical schools,
offline), and `chamilo`'s large regional install base. Named reference: **PUC Chile × Microsoft "ConectIA"**.
🔵 **Method note that keeps paying: every LATAM repo row above was found by querying in Portuguese or
Spanish.** The English-language sweep returned nothing for this region — the variable was the language.

## Regions and lines of enquiry that returned nothing — stated, not hidden

- 🟡 **EMEA adoption percentages — partly discharged.** UK *provision* figures now exist (HEPI: 36 % / 38 %);
  🔴 **no EMEA-wide adoption percentage** and 🔴 **nothing from EUA or EDUCAUSE.**
- 🔴 **AICTE and UGC (India, higher education).** The CBSE school limb discharged on the first query with a
  dated primary notification; **the higher-education limb returned nothing primary.** A secondary PIB summary
  claims *"AI components are now mandatory in all IT-related courses"* — **unverified and not used.**
- 🔴 **Africa and the Middle East as distinct markets.** Not separable under this task's five-value region
  vocabulary (both fall inside EMEA), and no dated national instrument for either surfaced this pass.
  🔵 The UAE appears only as a probable misattribution in a China story — the one lead worth chasing next pass.
- 🔴 **H.R. 8747 current status** beyond the July 2026 markup — unresolved for a **third** consecutive pass.
- 🆕 🔴 **Canada returned nothing, for a second pass.** A North-America-framed query produces US state law
  almost exclusively. 🔵 **Per `P870`/`P955` the next attempt should name the instrument, not the region** —
  provincial ministries of education and PIPEDA, rather than "Canada AI education".
- 🆕 🔴 **No open-source repository was found for ANY of the four curriculum mandates.** China's MoE,
  Singapore's MoE, India's CBSE and the EU's Article 4 all require material that someone must author, and
  the permissive supply is **entirely adult-developer curricula**. The reference framework they align to,
  `touretzkyds/ai4k12` (AAAI/CSTA), carries **no licence payload in 24 filenames** — see `agents/top.md`.
- 🆕 🔴 **Africa and the Middle East, third pass running.** Still not separable under the five-value region
  vocabulary, still no dated national instrument surfaced. 🔵 Recorded as a **vocabulary limit of this KB**,
  not as an absence in the world — the distinction matters because the two read identically in a blank cell.
- 🆕 🟡 **GitHub Trending returned ZERO education-industry repositories, for a fourth consecutive pass.**
  `github trending education AI 2026` returns generalist agent infrastructure and AI-engineering curricula
  for adults. 🔵 **Four passes of the same negative is a property of the channel, not of the industry**:
  trending is a popularity surface and this industry's repos are small, institutional and slow. 🟢 **The
  channels that do work here are `github.com/topics/<spec>` via `WebFetch` and Spanish/Portuguese queries** —
  both already in use, and both found rows this pass that trending did not.
- 🔴 **Japanese and Korean *curriculum* mandates.** Both have system-level law; neither surfaced a curriculum
  instrument, so the curriculum table has three APAC rows and not five.
- 🔴 **Conflicting Mexican figures** — a blog citing 73.4 % weekly student use and "only 2 in 10 universities
  have published guidelines" contradicts SEP's own >60 % daily and is **not used**.
- 🔴 **Primary-source access.** Four needed hosts are egress-blocked (see the caveat at the top). This is a
  standing constraint on this KB, not a gap in the world.

*Prior pass content is preserved in git history at commit `306eb06` and earlier.*
