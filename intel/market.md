---
industry: education
region: Global
updated: 2026-10-09
---

# Education — market, players and opportunities

**Pass 90, 2026-10-09.** Regional sweep run once globally and once per region (North America, EMEA, APAC, LATAM).
Every instrument below is dated and named. Where a region returned nothing on a line of enquiry, that is
written down rather than left blank.

## Market size — the figures disagree, and the disagreement is the finding

| source | 2026 figure | forecast |
|---|---|---|
| Precedence Research | **USD 9.58 B** | ~USD 136.79 B by 2035 |
| Research and Markets | **USD 10.6 B** | USD 42.48 B by 2030 |
| Grand View Research | **USD 11.4 B** | 25.9 % CAGR to 2033 |

🔴 **A 19 % spread between the low and high 2026 estimate, and the 2030–2035 projections differ by more than
3×.** These are market-research aggregators with incompatible scope definitions. 🟢 **Use the band — "roughly
USD 10 B in 2026, growing fast" — and never a single decimal figure in a client deck.** Any precision beyond
that is borrowed confidence.

**Funding, which is the more reliable signal:**
- 🔴 Global edtech VC was **~USD 1 B in H1 2026, down 26 % year on year.**
- 🟢 But AI-focused education companies took **USD 4.2 B in 2025 — 62 % of all edtech funding.**
- 🟢 Concentration is extreme: the **top 10 AI-education startups hold ~60 %** of reconstructed funding.
- Named 2026 round: **Preply, USD 150 M (January 2026), valuation USD 1.2 B.**

🔵 **Reading: the category is contracting while the AI slice of it expands.** Money is leaving
general edtech and consolidating into a few AI-native names. For a services studio that is favourable —
institutions still need to build, and the vendors who could have built it for them are fewer.

## Commercial players

**Horizontal / platform:** Microsoft (Education AI Toolkit updated **April 2026** with agentic capabilities),
Google, AWS, IBM.
**Education incumbents:** Pearson, Anthology, Carnegie Learning, DreamBox Learning, BridgeU, Fishtree.
**APAC-specific:** Byju's, plus Chinese state-backed programmes.
🔴 **Khan Academy / Khanmigo did not appear in any market-research player list this pass** despite being the
most visible AI tutor in public discourse. Recorded as a discrepancy, not resolved.

## Regulatory state of play

| jurisdiction | instrument | date | status |
|---|---|---|---|
| 🇪🇺 EU | **AI Act** — education is explicitly **high-risk** (exam scoring named by the Commission) | enforcement powers from **2 Aug 2026** | 🟡 **High-risk compliance deadline moved to 2 Dec 2027** by the Digital/AI Omnibus (Council approval **29 Jun 2026**); embedded high-risk systems **2 Aug 2028**. 🔴 Blogs still citing Aug 2026 for high-risk duties are outdated. |
| 🇰🇷 South Korea | **AI Basic Act** — education is a **"high-impact AI"** area | in force **22 Jan 2026** | 🟢 The region's most comprehensive law |
| 🇻🇳 Vietnam | **AI law**; implementing high-risk list includes education (automated assessment, behavioural monitoring) | enacted **1 Mar 2026** | 🟢 In force |
| 🇹🇼 Taiwan | **AI Basic Act** | passed **Dec 2025** | 🟢 |
| 🇺🇸 Ohio | first state to **require every K-12 district to adopt a formal AI policy** | deadline **1 Jul 2026** | 🟢 Binding |
| 🇺🇸 federal | **K-12 AI Literacy and Readiness Act of 2026** (H.R. 8747) | committee markup **Jul 2026** | 🟡 Advanced from committee; current status not confirmed this pass |
| 🇲🇽 Mexico | **SEP — 10 recomendaciones** for ethical/critical genAI use in HE | **15 Apr 2026** | 🔴 **Recommendations, not binding.** Press reports a regulation "in preparation"; not recorded as in force. |
| 🇨🇱 Chile | **Política Nacional de IA** (2021) + AI bill in discussion | — | 🟡 No education-sector rule |
| 🇧🇷🇨🇴 Brazil, Colombia | national AI strategies | — | 🔴 **No sectoral education regulation** |
| 🇸🇬🇯🇵 Singapore, Japan | voluntary guidelines on existing law; Japan drafting + standing up testing/assurance institutes | — | 🟡 Deliberately non-binding |

## Opportunities by region

### North America

**Demand signal.** ~36 % of the global AI-in-education market (**~USD 3.68 B, 2026**); one source puts
generative-AI adoption among North American educational organisations at **86 %**. 60 % of US K-12 teachers
used AI tools in the 2024–25 school year, 32 % at least weekly.

**The actual opening is governance, not tooling.** **134 AI-in-education bills across 31 states in 2026**;
30+ states have guidance documents; Ohio makes a district-level AI policy **mandatory by 1 Jul 2026**.
Meanwhile districts are diverging hard — Katy ISD bans genAI chatbots for K-6, New York City has a one-year
student-facing moratorium through grade 8. California's **AB 1159** would bar training on student data absent
direct school benefit; Oklahoma and Maryland are moving on human oversight of high-stakes decisions.

🟢 **Sell the compliance layer.** Thousands of districts have a legal deadline and no instrument. An
auditable record of *what the AI did, to which learner, on whose data, reviewed by which human* is a
deliverable, and the permissive substrate for it already exists: `yetanalytics/lrsql` (Apache-2.0) +
`adlnet/xAPI-SCORM-Profile` (Apache-2.0) for the trail, `Sakai` (ECL-2.0) where an HE platform is in scope.
🟢 Procurement here rewards foundation governance — Apereo's stewardship of Sakai/Opencast is a sales asset.
🔴 **Gap: no AI-driven accessibility or instructional-alignment checker exists under a permissive licence**
(only GPL `UDOIT`, non-AI). Given Section 508 / WCAG exposure, this is the clearest build-it-yourself opening found this pass.

### EMEA

**Demand signal.** 🔴 **No reliable EMEA-specific adoption percentage surfaced this pass** — the regional
market-sizing sources covered North America and APAC but not EMEA separately. Written down as a measurement gap.
What is solid is the regulatory calendar, which is the stronger driver here anyway.

**The opening is the AI Act's deferred deadline.** Education is high-risk; the duty date is **2 Dec 2027**, not
2026. That is a ~14-month build window that institutions currently believe they have already missed or already
survived — both readings are wrong, and both are sellable. Obligations land on transparency, **human oversight**
and **staff AI literacy**, and the Act reaches non-EU systems whose outputs affect EU-located students.
Supporting instruments: Commission **ethical AI guidelines for education (May 2026)**, Council conclusions on a
human-centred approach, and the **Apply AI Alliance**.

🟢 **EMEA is the best-supplied region on this shelf and the pitch should say so.** `Artemis` (MIT, TU München —
with Iris/Athena/Hyperion already built), `OpenOLAT` (Apache-2.0, Switzerland, Koblenz University),
`Opencast` (ECL-2.0), `Numbas` (Apache-2.0, Newcastle), `INGInious` (UCLouvain, AGPL), `TAO` (LGPL, Luxembourg),
`mentingo` (MIT, Poland), `ILIAS` (GPL, Germany). 🟢 **A European public institution asking for a
self-hostable, AI-extensible, closable deliverable can now be answered with `Artemis` or `OpenOLAT` — this KB
spent six passes wrongly answering "no permissive platform exists".**

### APAC

**Demand signal.** Projected **28.1 % CAGR 2026–2033** — the fastest-growing region. China leads on
state backing; India is the other major market.

**Regulation is the most advanced in the world and the most fragmented.** Binding, education-naming law in
**South Korea** (AI Basic Act, 22 Jan 2026 — education is "high-impact"), **Vietnam** (1 Mar 2026, high-risk
list names automated assessment and behavioural monitoring) and **Taiwan** (Dec 2025). Against that,
**Singapore and Japan** stay deliberately voluntary. UNESCO: **China and Singapore have established AI-in-education
policies; others lag**, and adoption is gated on IT infrastructure, connectivity and teacher training.
Public opinion splits sharply — Ipsos Education Monitor 2026 finds **Australia and New Zealand with the
region's strongest support for banning AI in schools**, Asian markets the weakest. The Philippines intends to
propose a regional framework under its **2026 ASEAN chairmanship**.

🟢 **No single APAC offer exists; the per-jurisdiction compliance delta *is* the product.** The same tutor
needs behavioural-monitoring controls in Vietnam, high-impact documentation in Korea, and neither in Singapore.
🟢 **APAC is also a supply region, which is under-appreciated:** `DeepTutor` (Apache-2.0, 41.0k★, HKU) is the
most-starred education agent anywhere; **Moodle itself is Australian** (Perth); `frappe/lms` and `pupilfirst`
are Indian; `GibbonEdu` is Hong Kong. 🟢 **`Kolibri` (MIT, offline-first) is the right answer to UNESCO's
connectivity constraint** rather than a cloud tutor.

### LATAM

**Demand signal — the strongest evidence of any region this pass.** **UNESCO IESALC with UNU-IAS, September 2026:
200 institutions across 19 countries; 87 % use AI in at least one area**, concentrated in teaching and learning,
**and governance lags adoption**. Digital Education Council / Tecnológico de Monterrey: **92 % of students use
an AI tool regularly, but only 30 % of students and faculty think their university integrates AI effectively.**
Mexico's SEP national survey (Apr 2026): **>60 % of university students *and* teachers use generative AI daily**,
from 1.5 M+ students and 166 k+ teachers.

**Regulation is the region's defining absence.** 🔴 **No unified regional framework. No sectoral education
regulation in Brazil or Colombia. Mexico's SEP and ANUIES outputs are non-binding.** Chile has a national AI
policy (2021) and a bill in discussion. 🟢 **Consequence: each university writes its own internal code** —
which means the buyer is the institution, the sales cycle is short, and there is no regulator to wait for.

🟢 **The sharpest arbitrage on this shelf: a 92 %-use / 30 %-effective gap with no regulator.** The product is
institutional AI governance and integration — policy, disclosure, assessment redesign, staff capability —
delivered per university. Mexico's **Plan Nacional de IA (ATDT, Apr 2026)** explicitly carries *software público*
and technological-sovereignty pillars with an education→employment component: that is a named, dated public-sector hook.
🟢 **LATAM supply exists and is placed:** `belentani7/aprende-brasil` (MIT, pt-BR, 205 modules, offline fallback),
`portabilis/i-educar` (LGPL-3.0, Brazil's largest open education system, municipal SIS deployments),
`programadores-obreros/Agente-editor-inet` (GPL-3.0, Argentine INET technical schools, offline), and `chamilo`'s
large regional install base. Named reference: **PUC Chile × Microsoft "ConectIA"** for institution-wide AI by 2026.
🔵 **Method note that keeps paying: every LATAM row above was found by querying in Portuguese or Spanish.**
The English-language sweep returned nothing for this region — the variable was the language, never the region's existence.

## Regions and lines of enquiry that returned nothing — stated, not hidden

- 🔴 **EMEA adoption percentages.** No EMEA-specific adoption figure found; regional sizing sources covered
  North America and APAC only.
- 🔴 **Africa and the Middle East as distinct markets.** Not separable under this task's five-value region
  vocabulary (both fall inside EMEA), and no dated national instrument for either surfaced this pass.
- 🔴 **Khanmigo / Khan Academy** absent from every market-research player list read.
- 🔴 **H.R. 8747 current status** beyond the July 2026 markup.
- 🔴 **Conflicting Mexican figures** — a blog citing 73.4 % weekly student use and "only 2 in 10 universities
  have published guidelines" contradicts SEP's own >60 % daily and is **not used**.

*Prior pass content is preserved in git history at commit `457eaba` and earlier.*
