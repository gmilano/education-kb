---
industry: education
region: Global
updated: 2026-10-11
---

# Education — market map and opportunities

**Pass 132, 2026-10-11.** 🔴 **This page's headline market claim is withdrawn and replaced: the
"1.8× spread for the current year" was an artefact of one year-shifted row** (`README.md` →
Pass 132, `P132-D`). The regional battery also **broke its four-pass saturation streak in all four
regions** — not with new facts, but with **dates, denominators and delivery structures**, which is
what it is actually good for. Figures are attributed to the kind of source they came from.

## Market size — the spread was mostly a base-year error

🔴 **Correction, `P132-D`. This page has said: *"estimates for the 2026 market span ~$6.4B to
~$11.4B — a 1.8× spread for the current year, so quote the range and the disagreement."* The
~$6.4B row is not a 2026 estimate. It is IMARC's 2025 base**, and IMARC's own earlier edition reads
**$4.8B for 2024 → $75.1B by 2033**. One misfiled row manufactured most of the disagreement this
page was built around.

🟢 **Restricted to figures genuinely for 2026, the firms nearly agree — a 1.19× spread.** The
**base year is not where these sources disagree. The horizon is.**

| year | estimate | forecast | implied CAGR | source |
|---|---|---|---|---|
| **2026** | **$10.6B** | → $42.48B by 2030 | 40.9–41.5% | The Business Research Company (its own 2025 base: **$7.52B**) |
| **2026** | **$10.4B** | → $32.27B by 2030 | 31.2% | market-research firm |
| **2026** | **~$11B** | — | — | market-research blog |
| **2026** | **~$9.58B** | → ~$136.79B by 2035 | 🔴 **34.52% and 36.02% on the same page** | Precedence Research (its own 2025 base: **$7.05B**) |
| **2026** | $4.09B (**higher education only**) | → $13.46B by 2030 | 34.7% | market-research firm — *a segment, not the market* |
| 🔴 **2025** | ~~~$6.4B~~ | → $79.6B by 2034 | 31.35% (2026–34) | **IMARC — misfiled as a 2026 figure by earlier passes of this KB** |
| 2025 *(context)* | $7.05B · $7.52B · $8.3B · $8.51B · $9.8B · $5.50B | — | — | Precedence · TBRC · Grand View · various |

**The 2035 end of the same sources, which is where the real disagreement lives:**
**~$70.55B** (SNS Insider) · **~$113.2B** (Research Nester) · **~$136.79B** (Precedence) ·
🔴 **~$1 169.44B** (Market Research Future). That is a **~17× spread** on the horizon against
**1.19×** on the current year.

**How to use this, revised:** 🟢 **Say that the firms agree within about 20% on what this market is
worth today (~$9.6–11B) and diverge seventeen-fold by 2035.** That is both true and far more useful
than "nobody agrees" — it tells a client the *current* opportunity is well-bounded and that any
ten-year business case built on a single forecast is arbitrary. Anchor commercial conversations on
the segment figure (higher ed, ~$4.09B in 2026), and 🔴 **always check a quoted figure's base year
before using it** — this page got that wrong for several passes. Note also that one source
publishes two different CAGRs for its own forecast (34.52% and 36.02%), so internal consistency
cannot be assumed either.

Regional share, as reported: **North America ~36%** (largest), **Asia-Pacific fastest-growing at
~35.3% CAGR**. 🟡 One tracker puts *"Rest of Latin America"* at **$18.2M in 2024 → $36M by 2029** —
three orders of magnitude below this page's held LATAM figures, because its scope excludes the
region's largest markets. **A LATAM number without its country list is unusable.**

## The structural fact of this market

Adoption by individuals has outrun institutional governance, and the gap is where the work is:

- **88%** of students worldwide report using generative AI; **95%** of UK undergraduates.
- **60%** of US K-12 teachers used AI tools in the 2024-25 school year; **32%** weekly.
- **18%** of US teachers have a written policy telling them how.
- An IDB review of **193** AI-in-education initiatives in Latin America found **59%** used
  generative AI.

Students and teachers are already using these tools; institutions have neither policy, procurement,
nor audit trail. **The sellable work is governance, integration and evidence — not another chatbot.**

## Key players

- **Platforms (the installed base):** Instructure/Canvas (dominant in North American higher ed),
  Moodle (largest global deployment, HQ in Perth), Open edX / Axim Collaborative, Blackboard and
  D2L (proprietary, significant higher-ed share, almost no open-source connectors), Google
  Classroom, Microsoft (Education AI Toolkit updated April 2026 with agentic features for
  institutions).
- **Open-source agent supply:** concentrated and thin — `HKUDS/DeepTutor` (41k★, Apache-2.0) is
  the only education-specific agent with real scale; everything else on the shelf is under 1k stars.
- **Institutional/multilateral actors who shape procurement:** UNESCO (regional AI-in-education
  observatory for LAC; OECD's 2026 Digital Education Outlook argues for purpose-built educational
  AI over general-purpose tools), IDB, Google.org (AI-literacy funding across nine LATAM
  countries), teachers' unions (NEA, AFT, CTA have all issued classroom AI guidance).

## Opportunities by region

### North America

- **Market position:** largest share (~36%), reported at ~$3.68B in 2026 by one tracker. Canvas is
  the platform of record in higher ed, and it has the best connector ecosystem — the MCP work is
  largely done, so engagements start further along.
- **The binding constraint is state-by-state policy, and it is now mandatory, not advisory.**
  134 AI-in-education bills were introduced across 31 states in 2026. **Ohio requires every K-12
  district to adopt a formal AI use policy by 1 July 2026** — a hard date with no accompanying
  capacity. California AB 1159 bars using student data to train models. Oklahoma and Maryland
  require human oversight and bar AI from high-stakes decisions about students. More than 30 states
  have guidance documents. Federally, the K-12 AI Literacy and Readiness Act (H.R. 8747) advanced
  from committee on 21 July 2026.
- **Opportunity:** *policy-to-implementation*. A district with a mandated policy and no technical
  means to enforce it needs data-flow inventory, a model-routing layer that can prove student data
  never reached a training endpoint, human-in-the-loop gates on anything high-stakes, and an audit
  log a board can read. Sell the compliance artefact, deliver the platform underneath it. Build on
  the Canvas MCP connectors plus `tutor-mcp` for auditable pedagogical decisions.
- **Second opportunity:** the AI-literacy curriculum funding line that H.R. 8747 would open, paired
  with `GarethManning/education-agent-skills` as a content base (licence review required).
- 🆕 **New from this pass's battery (p132).** Two capacity figures beside the held *18% of teachers
  have a written policy*: **only ~10% of institutions have formal AI guidelines** and **~71% of US
  teachers lack AI training** (2026 statistics roundup — different predicates, so they stack rather
  than conflict). Capital is moving into courseware specifically: **Carnegie Mellon + the Gates
  Foundation, $55M**, aimed at *gateway college courses*; and **OpenAI has launched a country-level
  education programme with eight national partners**. 🔵 **Read the CMU/Gates target carefully —
  "gateway courses" (the high-failure first-year courses that gate a degree) is the one place in
  higher ed where a learning-outcome improvement is directly measurable in retention dollars.**
  That is the natural home for the outcome-evaluation build in `compose/patterns.md` → P6.
- 🆕 **Supply note: Canada is the best-served NA jurisdiction in the new SIS tier**, with three MIT
  connectors (`mcgill-vsb-mcp`, `UofT-MCP`, `uoft-quercus-mcp`) against the US's one
  (`zavora-ai/mcp-student-records`, Apache-2.0). 🟢 **That US row is the single most
  procurement-shaped agent in this KB** — FERPA access logging as a first-class feature, and the
  only organisation-owned row of its tier. It is the right starting point for the
  policy-to-implementation offer above, which needs exactly that audit trail.
- 🔴 **Expect a client to arrive holding a wrong EU date.** NA-facing sources still state that *"the
  EU AI Act classifies education AI as high-risk, with full effect in August 2026."* The
  schools-facing Annex III date is **2027-12-02**. Correcting this politely is a credibility
  opportunity, not a pedantic one.

### EMEA

- **The regulatory clock moved, and the deferral is now confirmed as law.** High-risk obligations
  for Annex III education use cases (admissions, grading, proctoring) were **postponed to 2 December
  2027** under the Digital Omnibus on AI. 🟢 **p131 correction:** p130 recorded the Council as not
  yet having adopted and told the reader to treat the delay as "politically agreed, not final". The
  **Council's final green light is reported for 29 June 2026**, and this KB's own pages have carried
  the instrument as **Regulation (EU) 2026/1744 of 8 July 2026** for several passes. **Plan against
  2 December 2027 as a legal date** (Annex I embedded systems: 2 August 2028).
- **What already binds, regardless of the delay:** emotion recognition in education has been
  **prohibited since 2 February 2025**; **AI literacy duties (Article 4) have applied since
  February 2025**; public schools face a fundamental-rights impact assessment.
- **Adoption is deliberately slow:** no generative AI tool has been approved for system-wide use in
  the European Schools network, and the approval procedure is still being written.
- **Opportunity:** the delay to December 2027 is a *sales window, not a reprieve* — institutions
  that start in 2026 can build conformity in rather than retrofit it. Concretely: AI inventory and
  classification against Annex III, vendor-contract review, AI-literacy programmes that discharge
  an obligation already in force, and architecture that keeps grading and admissions decisions
  human-made by construction. **Avoid emotion recognition entirely** — it is already illegal here,
  and products built elsewhere ship it.
- 🆕 **Two concrete EMEA openings p130 missed.** (1) **Proctoring is the asked-for capability the
  shelf cannot supply at grade** — four MIT projects exist, the largest is 18★, and three do
  affect-adjacent inference, which in an EU education setting is **prohibited outright** (Art. 5),
  not merely high-risk. An auditable, affect-free integrity system built for Annex III from the
  start has no open-source incumbent and a dated legal driver. (2) **The benchmark layer is
  EMEA-origin** — `eth-lre/mathtutorbench` (ETH Zurich, EMNLP 2025 oral) is the strongest
  evaluation asset in this KB, and its licence is unresolved; an EMEA engagement is the natural
  place to fund or negotiate that resolution.
- 🆕 **The UK has become a distinct market with its own delivery shape (p132).** Its first **AI
  Adoption Summit (8 June)** committed **£200m+** to AI adoption — two orders of magnitude above the
  £4M lesson-planning programme this KB already held. 🔴 **And the delivery structure is the
  finding, not the money:** government funds, **Big Tech delivers** (Cisco, IBM, BT, Rolls-Royce),
  trade unions legitimise, **Skills England** sets the curriculum framework — and **traditional
  education providers barely appear.** 🟢 **For a services firm that is the single most actionable
  structural fact on this page: the UK is routing education-AI money through systems integrators
  and vendors, not through EdTech companies.** That is Globant's shape of work, and the entry point
  is delivery partnership rather than product. Track the **QS/HolonIQ 2026 Europe EdTech 200** as
  the regional cohort list (the EMEA counterpart to the LATAM EdTech 100 held below).
- 🆕 **The national K-12 platforms are the real EMEA installed base, and this KB had never listed
  them** (`verticals/solutions.md`, added p132). **Librus** (Poland), **EduPage** (Slovakia and
  Czechia), **Pronote** (France), **IServ** (Germany) are the systems of record for grades,
  attendance and parent communication — and all four now have open-source MCP connectors, mostly
  MIT, all unofficial password-scrapers with **no sanctioned integration path, no LTI and no vendor
  agent programme**. 🟢 **This is the clearest unmet EMEA need in the KB:** a properly
  authenticated, logged, DPA-backed connector for a platform whose vendor has no agent story, in a
  jurisdiction where the data is children's. 🔴 **And the clearest hazard** — do not deploy the
  existing ones; `librus-mcp` only works where 2FA is disabled.
- 🆕 **EMEA is also the best-placed region in the new agent supply**, with nine of the twenty-one
  rows (Poland, Slovakia ×2, France, Germany, Finland, Bosnia, Norway, Russia) — the first time any
  region in this KB has had a double-digit placed count.
- **Platform reality:** EMEA procurement runs on ILIAS, OpenOLAT, Chamilo and Moodle far more than
  on Canvas, and all four have essentially no AI-on-top. 🟢 **Moodle is now better served than p130
  recorded:** five **MIT** standalone MCP servers exist (`repos`/`agents` pages), so a Moodle
  engagement no longer starts from a licence problem. Standards and accessibility compliance are
  scored in tenders. Richie (MIT, France) is proven at national scale for the public-facing layer.

### APAC

- **Fastest-growing region (~35.3% CAGR), and the only one where curriculum mandates are driving
  demand from the top down.** China made AI a compulsory subject from age six as of September 2025.
  **India makes AI and computational thinking mandatory from Class 3 starting in the 2026-27
  academic year**, across government and private schools.
- **Regulation is real and heterogeneous — one compliance posture will not travel:** South Korea's
  **AI Basic Act took effect 22 January 2026**; China has six binding AI regulations including
  content-labelling and Cybersecurity Law amendments effective January 2026; India signalled in
  July 2026 that it may pursue dedicated legislation and already requires labels on AI-generated
  content; Japan's AI Promotion Act is light-touch, with a second AI Basic Plan approved by Cabinet
  on 14 July 2026; **Vietnam's Decision 33/2026/QD-TTg explicitly names education — including
  automated assessment and behavioural monitoring — as high-risk.**
- **Opportunity:** teacher-capacity tooling at national scale. A Class-3-onward AI mandate in India
  requires curriculum, teacher training and assessment at a volume no vendor can staff manually —
  this is a content-generation and teacher-support engagement, and `satvik314/educhain` (MIT) plus
  `GarethManning/education-agent-skills` are the closest existing bases. Supply-side advantage:
  APAC-origin open source is unusually strong here — `HKUDS/DeepTutor` (Apache-2.0, 41k★),
  `frappe/lms`, `openeducat_erp`, and Moodle HQ itself.
- **Public attitudes are a real constraint:** support for *banning* AI in schools ranges from 23%
  (Indonesia) to 31% (South Korea), with India 26% and Japan 29% (Ipsos Education Monitor 2026).
  Roughly a quarter to a third of the public wants these tools out of classrooms.
- 🆕 **Australia and New Zealand entered this KB for the first time this pass (p132), and only as a
  regulatory signal:** Canberra is tightening AI governance and copyright rules, and **OpenAI has
  appointed a dedicated ANZ policy lead**. 🔴 **ANZ has been absent from every previous APAC
  section here** — which, given that Australia is a mature English-language higher-ed export market
  running Moodle and Canvas at scale, is a gap in this KB rather than a gap in the market. No
  ANZ-origin open-source education AI was found. Needs a dedicated probe next pass.
- 🆕 **APAC supply is now the deepest in the KB and it is curriculum-bound (p132).** Seven of the
  twenty-one new SIS/portal rows are APAC: India ×3 (`vtop-bhopal-mcp` Apache-2.0,
  `DAU-buddy` unlicensed, `AI-Based-Timetable-Generation-System` MIT), South Korea
  (`soongpt-plugin`, MIT, graduation-requirement reasoning), Taiwan (`nycu`, MIT), Vietnam
  (`qldt-hanu-mcp`, GPL-2.0) and China (`ddl-killer`). 🟢 **Two are built to a named national
  policy** — the timetable optimiser to India's **NEP 2020**, and `Tushar-cy/Offline-AI` to the
  Indian Class-10 curriculum — which is the pattern to expect where mandates drive demand from the
  top down, and the easiest kind of project to justify to a ministry.
- 🔴 **Jurisdiction warning on the Vietnam row:** `qldt-hanu-mcp` reads student records in the one
  APAC jurisdiction that **explicitly names education, automated assessment and behavioural
  monitoring as high-risk** (Decision 33/2026/QD-TTg). It is also the tier's only copyleft row.

### LATAM

- **Adoption is ahead of governance, more starkly than anywhere else.** UNESCO IESALC reports
  widespread AI adoption across higher education in Latin America and the Caribbean with governance
  lagging. The IDB's review of 193 regional initiatives found 59% using generative AI. In Brazil,
  generative AI reportedly reaches 43% of teachers and 58% at high-school level (secondary source —
  verify before quoting).
- **Regulation is pending almost everywhere, and education-specific rules are essentially absent.**
  Brazil's PL 2338/2023 is advanced but not enacted. Mexico's AI amendments to date are in
  copyright, labour and audiovisual law — **not education**. Brazil, Argentina, Chile, Colombia and
  Costa Rica are each advancing their own frameworks. There is no regional instrument.
- **Capital and institutional momentum are real:** HolonIQ's 2026 LATAM EdTech 100 shows AI-native
  positioning quadrupling since 2020 and the cohort leaning toward instructional support rather
  than consumer tutoring; Brazil is ~45% of the regional cohort. Google.org is funding AI literacy
  across Argentina, Brazil, Chile, Colombia, the Dominican Republic, El Salvador, Mexico, Peru and
  Uruguay, targeting 1.25M students by 2028. UNESCO launched a regional AI-in-education observatory
  and, in August 2026, a pilot with CONALEP and DGETI in Mexico.
- **Opportunity:** be the governance layer that regulators have not yet imposed. Institutions
  adopting at speed with no legal framework will face one within the engagement's lifetime — build
  for Brazil's PL 2338 shape now. Second, **offline and low-bandwidth delivery is a first-class
  requirement here, not an edge case**: Kolibri (MIT, offline-first) plus a small local model is a
  differentiated, legally clean offer. Third, **Blackboard and Chamilo matter in this region** and
  are unserved — `campus-cli` (ISC, Peru) shows demand with an 11-star answer.
- 🆕 **The IESALC figures are now dated, which changes how they may be quoted (p132).** The
  UNESCO IESALC / UNU-IAS working paper surveyed **200 higher-education institutions across 19 LAC
  countries**, and the fieldwork ran **August–October 2025**. 🔴 **So this KB's held *"87% adoption
  / 26% with a strategy"* describes late 2025, not 2026** — present it as a baseline, not as
  current state, because the denominator and the window are both now on record. 🟢 Tec de
  Monterrey's observatory shows movement since: **students 86% → 92%**, **teachers 61% → 79%**.
- 🆕 **A named instrument for the LATAM regulation gap.** The **Latin American AI Index (ILIA 2025,
  published by CEPAL)** carries a dedicated regulation sub-dimension within its governance pillar —
  the country-level detail this KB has repeatedly looked for and failed to find in news channels.
  🔵 **Next pass should read ILIA 2025 directly rather than re-running regional news queries.**
- **Supply-side gap, stated plainly:** LATAM-origin open-source education AI is nearly nonexistent.
  🔴 **This did not improve this pass, and the contrast is now stark.** p132 added **21** new
  SIS/portal agents: nine EMEA, seven APAC, four North America, two unplaced — and **zero LATAM**.
  `alejooroncoy/campus-cli` (ISC, 11★, Peru) remains the only LATAM-origin row in the entire KB.
  🟡 **And the regional school platforms that would be the obvious targets — Blackboard and
  Chamilo, both with real LATAM share — have one connector between them.** Globant's regional
  position is a genuine advantage precisely because nothing is being built locally; this pass makes
  that the single most consistent finding in the KB rather than a one-off observation.
- 🔴 **Nothing offline targets LATAM either.** The offline stack found this pass
  (`project-nomad`, Apache-2.0, 39 444★) is unplaced, and the one curriculum-specific offline
  project is Indian. Given that this page argues offline delivery is a *first-class requirement* in
  LATAM rather than an edge case, a Spanish/Portuguese curriculum deployment of that stack is an
  unclaimed, permissively licensed, and now much cheaper piece of work.

### Global / unplaced

- ~~Open-source supply is **not** regionally distributed in any useful way… Most agent repos carry
  **no location evidence at all** — 11 of the 17 agent rows are marked unplaced rather than
  guessed.~~ 🔴 **REFUTED BY p132 for the tier it did not know about.** The twenty-one new
  SIS/student-portal rows are **~90% placed on hard evidence** — a named university, a national
  platform, a country-coded homepage (`mine.ibu.edu.ba`, `qldt.hanu.edu.vn`) — giving
  **EMEA 9, APAC 7, North America 4, unplaced 2, LATAM 0**. 🔵 **The old claim was true of the tier
  it was measured on and false of the sector.** Famous repos are unplaced because they are
  international; small institution-bound repos come with their region attached as evidence. 🟢
  **Rule for later passes: if regional supply looks absent, the query was probably global.**
  Searching platform proper nouns (`librus`, `edupage`, `pronote`, `vtop`, `usaint`) returns placed
  rows that category terms cannot reach — see `agents/top.md` → the vocabulary rule.
- 🔴 **Correction to p130's "absent benchmark".** The benchmark layer is **not absent** — it is
  **ungranted**. `eth-lre/mathtutorbench` (43★, EMEA) carries no licence field and names two
  different licences in one README; `Khan/tutoring-accuracy-dataset` (57★, North America) carries a
  bespoke 2 690-byte evaluation-dataset licence and has been dormant since August 2024. 🟢 **What is
  genuinely absent is outcome measurement:** both measure tutor *behaviour*, neither measures
  durable learning gains — the standard the OECD's 2026 Digital Education Outlook asks for. The
  client who gets outcome evidence is still buying something no competitor can show; the build is
  just cheaper than p130 implied, because it starts from two real benchmarks.
- **The permissive/popular inversion** — the most-starred item in a tier is repeatedly the unusable
  one: Moodle connectors (most-starred `loyaniu/moodle-mcp`, 40★, **no licence**; permissive leader
  `peancor`, 43★ but quiet since February), Canvas (103★ `mcp-canvas-lms`, **no licence**, vs MIT
  `canvas-mcp` at 288★), agent skills (847★, **NOASSERTION**), benchmarks (both ungranted).
  **Licence screening is not a late-stage check in this sector; it reorders the shortlist.**
  🟡 **p132 qualifies the scope of this claim, which was overstated as "across every tier
  measured".** The new SIS/portal tier is **~80% MIT** — the inversion does *not* hold across it.
  🔵 **But it still holds at the top of that tier:** its two most-starred rows are the weak ones —
  `librus-mcp` (10★) is mixed-licence (MIT 2.x over a **GPL-3.0-only** `legacy_reference/`) and
  `DAU-buddy` (7★) is unlicensed. 🟢 **So the accurate form of the finding is narrower and still
  useful: popularity does not predict licence quality, and the correlation is strongest among the
  biggest repos in any tier.** It is not a law about the sector.
- 🆕 **A third of this pass's licence findings came from reading a payload rather than a field.**
  `zavora-ai/mcp-student-records` reads **Apache-2.0** where the API says `NOASSERTION`, because its
  `LICENSE` is the **~745-byte Apache notice block** without the licence body. 🔴 **And one row is
  unlicensed by *declaration* rather than omission** — `h9-tec/graduation-project-advisor` (63★)
  states *"Private / TBD. Licensing terms will be finalized before any public release."* 🔵 Those
  are three distinct states a client must not be told are the same thing: **granted-but-unmatched**,
  **silent**, and **deliberately withheld**.

## Declared gaps in this market picture

- **Africa and the Middle East are inside "EMEA" here but are not covered by it.** 🟡 **NARROWED by
  p132's dedicated probe, and still open.** The first MENA-targeted education AI project is now on
  record — [`h9-tec/graduation-project-advisor`](https://github.com/h9-tec/graduation-project-advisor),
  **63★**, Arabic-first, taking **Egyptian CS students** from an onboarding form to a
  supervisor-ready graduation project — and 🔴 **it is unlicensed by declaration**, so nothing can
  be built on it. [`mbzuai-oryx/ClimateGPT`](https://github.com/mbzuai-oryx/ClimateGPT) (80★,
  **MBZUAI, Abu Dhabi**) shows real institutional AI capacity in the Gulf but is not an education
  tool. 🔴 **Still missing entirely: any African or Gulf education-AI market sizing, any national
  regulatory instrument, and any Sub-Saharan row at all.** The 5-value region vocabulary keeps
  folding three very different markets into one bucket; this is a blind spot in the taxonomy, not a
  finding of absence.
- **No reliable open-source market-share data** for which LMS actually runs where, by region. The
  platform-share claims above come from vendor and roundup sources.
- ~~**The 2026 market-size spread (~$6.4B–$11.4B) was not resolvable** against primary sources from
  this runner.~~ 🟢 **LARGELY RESOLVED BY p132 — and it was not a source problem, it was a filing
  error here.** The low end was IMARC's **2025** base misfiled as a 2026 estimate; the genuine 2026
  figures agree within **1.19×** (~$9.6–11B). 🔴 **What remains open is the horizon:** 2035
  estimates span **~$70B to ~$1 169B (~17×)**, no primary report is readable from this runner, and
  one firm publishes two different CAGRs for its own forecast. **Treat any single long-range
  forecast as arbitrary.**
- 🆕 **No LATAM figure found this pass carries its country list.** A tracker reporting *"Rest of
  Latin America"* at **$18.2M (2024) → $36M (2029)** sits three orders of magnitude below this
  page's held LATAM figures purely on scope definition. A regional number without its denominator
  cannot be quoted.
