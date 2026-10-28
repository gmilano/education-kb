---
industry: education
region: Global
updated: 2026-10-28
---

# Education AI — market map and opportunities by region

**Pass `p491` — reads of 2026-10-27.** `p490` (earlier the same day) rewrote this file; `p491`
**extends** it. Four things changed: the **EMEA sizing gap is partly closed**, **APAC school-adoption
data now exists** here, a **US statute this KB was about to inherit is refuted**, and **LATAM's
"no statute" gap now has a named bill and its status**. Pre-p490 sections remain in
[`archive/2026-10-27-p490-pre-rewrite/market.md`](../archive/2026-10-27-p490-pre-rewrite/market.md).

## Market size — the estimates do not agree, and that is the finding

| Source | 2026 | Later | CAGR |
|---|---|---|---|
| Precedence Research | ~$9.58B | $136.79B (2035) | 34.52% |
| Resourcera | $10.4B | $32.27B (2030) | — |
| Span of four firms surveyed | **$6.4B – $11.4B** | — | — |
| HolonIQ (two figures, mutually inconsistent) | $12.3B | ~$23B | — |

**Use the range, not a point.** 2026 estimates span **$6.4B–$12.3B — nearly 2×**. One widely
recirculated blog figure ($11B) is described by its own author as "our final guess."

🔴 **Two figures this KB has published are retired as unsupported:**

- **"$42.48B by 2030 at 41.5% CAGR"** — carried since cycle 2. No source found this pass
  supports it; Precedence's own current path is $136.79B by **2035** at **34.52%**, and
  Resourcera's 2030 figure is **$32.27B**. The 41.5%/2030 pair does not reconcile with either.
- **"LATAM $1.5B → $4.2B at 45% CAGR"** — carried since cycle 2. The only current regional
  sizing found puts **Brazil at $61.1M and Mexico at $59.2M**, i.e. the two largest LATAM
  markets together are ~**$120M**, roughly **12× below** the published $1.5B. Both cannot be
  true. The vendor report carrying the $61.1M/$59.2M figures has internally inconsistent dates,
  so treat *both* sides as unreliable and do not quote a LATAM market size without a primary
  source.

**Regional structure (the one point the sources agree on):** North America holds the largest
share at **36%**; **APAC is fastest-growing at 35.3% CAGR**.

## Demand signals

| Signal | Figure | Source |
|---|---|---|
| Students using AI in studies (16 countries) | **86%** | Digital Education Council |
| K-12 teachers using genAI for work | **25% → 53%** in one year | RAND |
| Institutions planning AI teaching-assistant deployment by end-2026 | **83%** | EDUCAUSE (as cited) |

## Opportunities by region

### North America

**Posture: largest market (36% share), most fragmented regulation, strongest buying intent.**

- **Regulation is state-by-state and inconsistent.** ~**34 states plus DC and Puerto Rico** have
  issued AI guidance. Enacted laws differ in kind: Maryland **S.B. 720** (state guidance +
  statewide collaborative), Idaho **S.B. 1227** (mandatory local policies + AI literacy
  standards), Oklahoma **S.B. 1734** (parent opt-out rights), Arizona **HB 4040** (public
  universities must adopt AI-use policies covering detection and consequences).
- **No federal law.** The **K-12 AI Literacy and Readiness Act of 2026 (H.R. 8747)** would let
  districts spend federal education funds on AI curricula. It **advanced in committee and is not
  enacted** — do not plan around it. 🟡 One tracker reports the federal Education Department
  finalised an **AI grant-priority rule on 13 Apr 2026**; unverified against a primary source.
- 🔴 **Refuted this pass — Texas HB 2400 is NOT law, and it is the most consequential bill in this
  sector if it ever passes.** It would bar districts and open-enrollment charters from using AI
  *"to provide instruction to students or to replace or supplement a teacher's role."* A current
  aggregator (`billtrack50`) lists it as **"became law"**. The Texas Legislature's own record shows
  it **filed 4 Feb 2025, referred to House Public Education 14 Mar 2025, and left in committee**;
  its Senate companion **SB 382** died the same way, and a 2026 review of the 90th Legislature
  describes it in the past conditional — a bill that *"would have"* prohibited AI instruction.
  Connecticut ran a near-identical bill. 🔵 **Caveat on this refutation:** `capitol.texas.gov` does
  not resolve from this session's network, so this rests on the convergent secondary record
  (Texas Legislature Online mirror, FastDemocracy, Education Commission of the States) rather than
  a primary read. The aggregator is the outlier, not the consensus. **Do not quote a Texas AI
  instruction ban as live law.**
- 🟡 **Texas is reported as one of five states with no statewide K-12 AI guidance** — the inverse of
  how it is usually characterised, and worth checking before a Texas pitch.
- 🟡 **Two of p490's statute descriptions are contradicted by this pass's sources and are now
  flagged rather than overwritten:**

  | statute | `p490` recorded | `p491` source says | status |
  |---|---|---|---|
  | Oklahoma **S.B. 1734** | parent opt-out rights | instructional AI must be **educator-directed with human-in-the-loop review** | 🟡 unresolved — these are different duties and both are plausible as parts of one act |
  | Maryland **S.B. 720** | state guidance + statewide collaborative | **every local school system must designate an AI coordinator** | 🟡 unresolved — read the enrolled text before citing either |

  Also newly named, unverified: **Alabama HB 329** (AI content inside a graduation-required CS
  course) and **Ohio HB 96** (board-approved district AI policy). Read the enrolled text before any
  of these reaches a client deck — this KB has now carried two different descriptions of the same
  two statutes.
- 🟡 **Bill counts are not usable.** Trackers disagree by more than 10× ("134 bills across 31
  states" vs "more than 1,500 AI-related bills"). Cite a specific statute, never a count.
- **Platform reality:** Canvas LMS (AGPL-3.0) dominates US higher ed, and it is the **only**
  incumbent LMS with a maintained agent tool surface
  ([`canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp), MIT).

**Opportunity:** a **policy-configurable** AI layer. The differentiator is not the tutor, it is
the compliance surface: per-district policy toggles, human-oversight gates on high-stakes
decisions, parent opt-out plumbing (Oklahoma), and AI-literacy reporting (Idaho). Build once on
Canvas via `canvas-mcp`, configure per jurisdiction. Institutional examples to design against:
Columbia Law's 2026-27 rule (AI as learning aid, barred from producing submitted work) and Katy
ISD's K-6 generative-AI restriction.

### EMEA

**Posture: the clearest regulatory calendar in the world, and it just moved. Compliance is the product.**

- **Schools are *deployers*; the vendor is the *provider*** under the EU AI Act — and the
  provider carries most design and conformity duties. **For a Globant-built education AI system,
  Globant is the provider.** This is the single most consequential fact in this section.
- **Already in force:** emotion-recognition AI in education has been **banned since 2 Feb 2025**.
  Article 4 AI-literacy duties also applied from that date; since **27 July 2026** the duty is to
  *take measures to support staff skills* rather than to ensure a given level.
- 🟢 **The high-risk deadline slipped 16 months.** The **2026 Digital Omnibus (Regulation (EU)
  2026/1744)** moved stand-alone education systems from **2 Aug 2026 → 2 Dec 2027**; embedded
  systems in regulated products get until **2 Aug 2028**.
- 🟢 **`p491` — the Omnibus now has a legislative chronology and a citable address.** Ten
  independent secondary sources converge, and they add detail p490 did not carry: **European
  Parliament approval 16 Jun 2026**, **Council final adoption 29 Jun 2026**, **published in the
  Official Journal 24 Jul 2026**, **in force 27 Jul 2026**. What is deferred is specifically
  **Chapter III, Sections 1–3 of Regulation (EU) 2024/1689** (classification, high-risk
  requirements, provider/deployer obligations). **National regulatory sandboxes move to Aug 2027**
  — and that duty binds *Member States*, not vendors. **Not deferred:** Article 50, the prohibited
  practices, and the GPAI-model obligations. Official address for the next pass to read:
  `eur-lex.europa.eu/eli/reg/2026/1744/oj`.
- 🔵 **The EUR-Lex verification p490 asked for is still open, and now for a stated reason.**
  `eur-lex.europa.eu` **does not resolve from this session's network**, so the primary text could
  not be read this pass either. The dates are now *convergent across ten secondary sources* rather
  than *from commentary*, which is better evidence but still not the OJ. One further claim surfaced
  and is **unverified**: that providers/deployers of high-risk systems used by **public
  authorities** must comply by **2 Aug 2030** — directly relevant to ministry and
  public-university work, so verify it before pricing a public-sector programme. 🟡 Also note one
  widely-circulated law-firm update (DLA Piper) still describes the Omnibus as *under negotiation*
  after an April 2026 trilogue — it is out of date and it is not the only one.
- **Article 50 transparency still starts 2 Aug 2026.** Systems already on the market before that
  date have until **2 Dec 2026** to meet the content-marking duty — **the nearest live deadline
  in this file.**
- **High-risk education uses:** admissions, assessment, exam proctoring, and anything determining
  access or influencing an educational path.
- 🔴 **Verify the Omnibus dates against EUR-Lex before client use.** The 2026/1744 dates come
  from secondary commentary, and many guides still print the superseded Aug 2026 date.
- **Platform reality:** the two permissive-friendly European LMSs are here — OpenOlat
  (Apache-2.0, Swiss) and ILIAS (GPL-3.0, German/DACH public sector).

**Opportunity:** **provider-grade conformity tooling** — technical documentation, logging,
human-oversight design, and Article 50 content marking, delivered as part of the build rather
than retrofitted. The Dec 2027 slip creates a 14-month window to become the vendor that is
already conformant. Pair with OpenOlat where a closed derivative is needed, since it is the only
permissive full LMS.

#### EMEA sizing — the gap is partly closed this pass

`p490` declared "no reliable adoption-rate or vendor-share data for European school AI." Found this
pass, all **secondary and flagged as such**:

| Figure | Value | Note |
|---|---|---|
| Europe AI-in-education market, 2026 | **$2.64B** | → **$8.0B by 2030**, **31.9% CAGR** |
| K-12 AI integration leaders | **Finland, Estonia, Netherlands** | the first named-country ranking this KB has carried for EMEA |
| Europe share of global edtech | **22%** (HolonIQ: NA 38%, APAC 32%) | a second estimate says **~18%**, UK + Germany largest |
| Institutions with AI guidance | **~70%** Europe/NA vs **45%** LATAM & Caribbean | the cleanest cross-region governance contrast available |
| EU institutions prioritising EEA data hosting | **>55%** | 🟡 unverified secondary outlook — but it names *data residency as a selection criterion*, which is a procurement fact, not a market-size one |
| Digital Education Action Plan + Digital Europe | **>€8.1B** for digital education transformation | 🟡 unverified against Commission sources |

🔵 **Consistency check, because these figures cut against each other:** $2.64B for Europe against a
global 2026 range of $6.4B–$12.3B implies a European share of **21–41%** of AI-in-education
spend — consistent with the 22% edtech share at the low end, impossible at the high end. The
figures are directionally usable and arithmetically soft. Quote the range and the source, never
the point.

🔵 **Still a genuine gap: no vendor-by-vendor European market share.** Searched this pass;
coverage of named European AI-education players remains thin to absent. An EMEA competitive
landscape still requires primary research.

### APAC

**Posture: fastest-growing region (35.3% CAGR), lowest resistance to classroom AI, no single regulatory model.**

- **Least opposition to AI in schools anywhere measured.** Support for *banning* AI in schools
  (Ipsos Education Monitor 2026): Indonesia **23%**, Thailand **25%**, India **26%**,
  Singapore **28%**, Japan **29%**, Malaysia **29%**, South Korea **31%**. Low numbers mean
  permissive public opinion — the inverse of the EMEA mood.
- **Four incompatible regimes, which is the integration problem:**
  - **South Korea** — **AI Basic Act in effect 22 Jan 2026**; the first comprehensive, mandatory
    AI law in APAC.
  - **China** — most prescriptive: rules on recommendation algorithms, deep synthesis,
    generative-AI services and AI-content labelling, plus a **national filing** requirement
    (**988 generative-AI services filed by 30 June 2026**).
  - **India** — no dedicated AI law; works through amended IT Rules: from **20 Feb 2026**
    AI-generated content must carry **prominent labels and provenance markers**.
  - **Japan** — deliberately **non-binding** AI Promotion Act; a new **AI Basic Plan was adopted
    by Cabinet on 14 July 2026**.
  - **Vietnam** — AI law effective **1 Mar 2026**, and 🟢 **a July 2026 decision classifies
    education as a high-risk AI sector** (new this pass). Vietnam is therefore the **second**
    jurisdiction after the EU to put education-AI explicitly in a high-risk tier — a compliance
    hook where p490 recorded none.
  - **South Korea** — the AI Basic Act carries a **grace period: penalties are not expected until
    roughly Jan 2027** (new this pass). The law binds now; the enforcement cliff is a year out,
    which is exactly the window to arrive conformant in.
- Content labelling is mandatory in **China and India** and absent in **Japan** — so the same
  product needs per-market provenance behaviour.

**Opportunity:** a **jurisdiction-routing content-provenance layer**. One tutor, with
label/provenance/filing behaviour selected per market, is the thing no single-market vendor can
easily ship. Korea's binding act makes it the natural beachhead for a compliance-first pitch;
India's labelling rule is the highest-volume one.

#### APAC school adoption — the gap is partly closed this pass

`p490` recorded "no dedicated data on school AI adoption … in China, India or Japan." Found this
pass (secondary sources; mandate detail is firmer than adoption detail):

- **China — the most advanced school mandate measured anywhere.** AI has been a **compulsory
  subject from age six since September 2025**, with **contact hours set by province**: **Beijing
  8 hours/year**; **Guangdong 6 hours** in lower grades rising to **one hour per fortnight in
  grades 10–11**. Rollout is uneven and ethics, privacy and equitable access are reported to lag
  the technology. **This is a curriculum-and-teacher-training market, not a tutoring-product
  market** — a different sale from every other region in this file.
- 🔴 **South Korea — a mandate that was reversed, and the most useful failure case in this KB.**
  AI digital textbooks were planned as mandatory from 2025; **adoption sat below 30% by March**,
  and in **August 2026 the National Assembly stripped them of official textbook status**. Sources
  conflict on the exact timeline, so verify before citing — but the direction is not in doubt.
  **Consequence:** a national AI mandate is not a durable demand floor. Price Korean public-sector
  work so it survives de-mandating, and expect procurement to ask how you avoid the textbook
  outcome.
- **Japan — digital textbooks may gain official status as early as the 2030 school year.** Slow,
  deliberate, non-binding, consistent with its AI posture. Not a near-term market.
- **India — a reported ten-million-teacher training push**, scale unconfirmed. India remains the
  highest-volume labelling-compliance market (IT Rules live 20 Feb 2026) rather than a
  school-adoption market in this data.

🔵 **Still a gap: no edtech *vendor share* for any APAC market**, and no reliable
institution-level adoption *rate* for China, India or Japan. What exists now is mandate structure
and contact hours — which is more actionable for a curriculum pitch than an adoption percentage
would have been.

### LATAM

**Posture: highest measured individual adoption, weakest institutional frameworks, thinnest reliable sizing.**

- **Adoption runs ahead of institutions — with hard numbers:**
  - **56% of Brazilian secondary teachers** used AI in the prior year vs an **OECD average of
    36%** (TALIS 2024). Brazil is **20 points above** the OECD mean.
  - **65% of Brazilian internet users aged 9–17** use AI tools (Cetic.br, 2026).
  - Higher ed (Digital Education Council, 29 LATAM institutions): **92% of students** and
    **79% of faculty** actively engaging with AI — **but only 30% of students** say their
    institution's current AI use meets expectations.
- 🟢 **That 92%-vs-30% gap is the commercial opening in this region**: demand is saturated,
  institutional delivery is not. UNESCO states it directly — institutional frameworks "do not
  match the speed of adoption."
- **Institutional momentum is real and funded:** UNESCO launched the **Observatory on AI in
  Education for Latin America and the Caribbean on 14 April 2026**, plus a **Mexico pilot**
  building centres of excellence with **CONALEP and DGETI**. **Google and the IDB** announced an
  AI training academy for public servants with **$5M in Google.org funding**.
- **Regional players:** **Teachy** (Brazil — AI lesson preparation, has expanded beyond the
  region into Asia), **Ginia** (Mexico — AI-driven employability linking employers,
  institutions and students), **Vetto** (Brazil — raised capital this window). Reference list:
  HolonIQ **2026 Latin America EdTech 100**.
- **Platform reality:** Chamilo (GPL-3.0) has a notable LATAM public-sector footprint; Kolibri
  (MIT, offline-first) is the right base wherever connectivity is not guaranteed.
- 🔴 **Sizing is not usable** — see the retraction above. Brazil $61.1M / Mexico $59.2M vs this
  KB's published $1.5B differ by ~12×.

**Opportunity:** **institutional delivery, not another tutor.** Students and faculty already use
AI; what is missing is the institution's own sanctioned, integrated offering. Concretely:
Portuguese/Spanish-first, **offline-capable** (Kolibri) deployments for ministries and public
university systems, aligned to the UNESCO Observatory and the CONALEP/DGETI centre-of-excellence
model, with Chamilo or Moodle as the incumbent integration target.

- 🟢 **`p491` — more regional players named.** Beyond Teachy, Ginia and Vetto: **Mattilda**
  (Mexico — billing and collections for private schools), **Questly** and **Beconfident** (Brazil,
  both seed-stage). Structural figure worth carrying: **Brazil holds 68.93% of Latin America's 898
  active edtech startups** — the region's supply is overwhelmingly one country, which is why a
  "LATAM" engagement is usually a Brazil engagement plus Mexico.

🔵 **Declared gap, now with a named bill and its status.** **There is still no
AI-in-education statute in force anywhere in LATAM** — p490's finding **holds**, and this pass can
say why rather than merely reporting absence:

- **Brazil — PL 2338/2023 (*Marco Legal da IA*) is the region's bellwether and it is NOT law.**
  The **Senate approved a substitute text on 10 Dec 2024** and sent it to the **Chamber of Deputies
  on 17 Mar 2025**, where it sits in a **special committee** (chair Dep. **Luisa Canziani**,
  rapporteur Dep. **Aguinaldo Ribeiro**) **still awaiting the rapporteur's report as of Oct 2026**.
  A plenary vote expected end-May 2026 **did not happen**. The approved text is risk-based, bans
  certain uses, and creates a national AI governance system (**SIA**) coordinated by the data
  protection authority (**ANPD**).
- 🟡 **Whether PL 2338 treats education as high-risk is NOT established.** One vendor blog claims
  it classifies *student selection for education* as high-risk and that a **CNE** (National
  Education Council) guidance was in preparation. The search results that discuss the bill's
  risk tiers **do not mention education at all**. Read the Senate's approved text before telling a
  client that Brazil has an education-AI high-risk category coming.
- **Mexico — no AI-in-education regulation found**, again. Coverage remains institutional
  (UNESCO Observatory, CONALEP/DGETI, the Google/IDB academy).

**Consequence, unchanged but now defensible:** unlike EMEA, Korea and now Vietnam, there is **no
binding LATAM compliance hook** to sell against. The pitch is delivery and outcomes. 🟢 But
**PL 2338 is the thing to watch** — it is one committee report away from giving the region its
first horizontal AI statute, and a vendor that is already EU-conformant will clear a risk-based
Brazilian regime with little extra work. That is a reason to build conformity once, in EMEA shape,
and reuse it.

### Global

🟢 **Added `p495`. It closes a structural red this KB was carrying unnoticed:
`make gate-region-headings` has been FAILING at `intel/market.md:50` with
`P383-MISSING-REGION — Global`**, because the region vocabulary is five values and this
file's single `## Opportunities by region` block carried only four. 🔵 The gate was right and
the file was wrong; `p495` checked the complaint against `HEAD` before writing, so the red is
**pre-existing, not introduced**. 🔴 **Nothing is placed here to satisfy a gate** — the
findings below are the ones that genuinely have no region, and parking them in a regional
section was itself the distortion.

🔴 **The open-source supply for education agents is exhausted, globally, and this is the most
decision-relevant global fact this KB holds.** Four consecutive passes of the star-ordered
sweep have returned nothing promotable above the floor (`p492`–`p495`), and `p495`'s single
genuinely-new address turned out to be an **unlicensed reskin** of a repo already on the shelf.
🟢 **The consequence is strategic, not clerical: differentiation cannot come from finding a
better open-source tutor, because everyone's search returns the same shelf.** It comes from
**integration, hardening and governance** — which is what every `P49x` pattern now sells.

🔴 **No permissive platform exists at the ERP / SIS / LMS layer, anywhere.** Three independent
passes of the vertical-platform query return LGPL / GPL / AGPL systems (`OpenEduCat`, Moodle,
Open edX, BigBlueButton) and no MIT or Apache education platform. 🔵 **So the first question on
every engagement, in every region, is which copyleft obligation the client can carry** — not
which platform is best. See [`../repos/foundations.md`](../repos/foundations.md).

🔴 **Agent surfaces on incumbent systems carry security debt that the incumbent's hardening does
not cover** (`T15`, evidenced first-hand `p495`: four advisories in one day on the only
maintained Canvas agent surface, two **High**). 🔵 **This is vendor- and region-independent**,
and it is the clearest global case for a studio engagement: arriving at a deployable posture
took a release-tag read, four advisory reads, a CVSS read and a runtime check.

🟡 **Global market sizing remains unusable, fifth pass (`T10`).** 2026 estimates from this
pass's own sweep: **$3.7B**, **$10.6B**, **$11.4B** — not agreeing within a factor of three.
🟢 **Quote direction and regional ordering, never a figure.** The one quantified contrast worth
quoting is LATAM's **~92% student engagement against ~30% institutional policy coverage**,
because it is measured, sourced, and names the product.

## Cross-region summary

| | NA | EMEA | APAC | LATAM |
|---|---|---|---|---|
| Market position | largest (36%) | mid | fastest (35.3% CAGR) | smallest, badly sized |
| Binding AI law | none federal; state patchwork | **EU AI Act** | KR, CN, VN yes; JP no; IN partial | **none in force**; BR PL 2338 stalled in committee |
| Education named high-risk | no | **yes** (Annex III) | **yes — Vietnam**, *Decision 33/2026/QD-TTg*, issued **30 Jun 2026**, in force **15 Aug 2026**, **3 education systems** of 46 | 🟡 claimed for BR PL 2338, unconfirmed |
| Nearest deadline | varies by state | **2 Dec 2026** (Art. 50 marking) | IN labels live 20 Feb 2026; **KR penalties ~Jan 2027**; **VN education 1 Sep 2027** if live before 15 Aug 2026, else **1 Mar 2027** 🟢 *confirmed `p494`; the fallback row is single-sourced — see `p494`* | — |
| Individual adoption | 53% teachers | **$2.64B mkt; FI/EE/NL lead K-12**; rate still unmeasured | **CN compulsory from age 6**; KR mandate **reversed** | **highest measured** |
| Institutions with AI guidance | ~70% | ~70% | not established | **45%** |
| Sell on | policy configurability | **provider conformity** | jurisdiction routing; 🟢 **SG: demonstrable conformity to a voluntary standard** (`p494`) | institutional delivery |


## 🆕 `p492` — `2026-10-28` — Vietnam's education high-risk tier, pinned to an instrument

`p491` reported "a July 2026 decision classifies education as a high-risk AI sector." **That was
right in substance and wrong in two details, and it had no instrument number** — which is the
difference between a slide and advice. Now citable:

| field | `p491` | `p492` |
|---|---|---|
| instrument | "a July 2026 decision" | **Decision `33/2026/QD-TTg`** |
| issued | — | **30 June 2026** (not July) |
| in force | — | **15 August 2026** |
| scope | "education is high-risk" | **46 high-risk AI systems across 6 sectors; education is 3 of them** |
| education compliance deadline | — | 🟢 **1 September 2027** |

### 🟢 The deadline correction matters commercially

The general Decision 33 deadline is **1 March 2027**. **Education does not run on it.** Systems in
**healthcare, education and finance already in operation before 15 Aug 2026 have until
1 September 2027** — a **six-month longer runway** than every other listed sector. A system put
into operation **within six months after** the effective date falls back to **1 March 2027**.

**So the date depends on when the system went live, not on what it does:**

| situation | deadline |
|---|---|
| education AI **in operation before 15 Aug 2026** | **1 Sep 2027** |
| education AI **first operated within 6 months after 15 Aug 2026** | **1 Mar 2027** |
| non-education sectors under Decision 33 | **1 Mar 2027** |

🟡 **The counter-intuitive consequence: shipping earlier buys more time.** An incumbent Vietnamese
deployment that was already live has the longer runway; a *new* 2026 entrant gets the **shorter**
one. For a Globant engagement standing up a new system, **plan on 1 Mar 2027, not 1 Sep 2027** —
the generous date is the incumbent's, not the newcomer's.

**Transition rule:** during the transitional period existing systems may keep operating **unless a
competent State agency determines a system poses a serious risk** and suspends or terminates it.
So the runway is **conditional, not guaranteed**.

**Named education scope:** the appendix includes systems that **automatically assess or rank
learners** — the same functional trigger as EU Annex III. 🟢 **An EU-conformant assessment design
therefore transfers to Vietnam with little rework**, which strengthens the standing
"build conformity once, in EMEA shape, and reuse it" conclusion in the LATAM section — it now
holds for APAC's second high-risk jurisdiction too.

🔵 **Evidence caveat, stated because this KB does not launder secondary sources.** This rests on
**convergent reporting from four independent law firms and a trade brief**, not a primary read.
`www.tilleke.com` **does not resolve from this session's network** — the same posture as the
standing EUR-Lex gap on the EU Digital Omnibus. Figures agree across sources; the instrument number
and both dates are consistent. **Read the official text before it reaches a client contract.** One
earlier source (a May 2026 vendor guide saying the high-risk list "has not been issued") simply
predates Decision 33 — it is stale, not contradictory.

### 🔵 Still missing in APAC, restated

No **edtech vendor share** for any APAC market, and no reliable institution-level adoption *rate*
for China, India or Japan. Decision 33 adds a **compliance hook** for Vietnam; it adds no
market-sizing figure, and this file still has none for Vietnam specifically.

## 🆕 `p493` — `2026-10-28` — regional reads, with the per-region queries run and their misses declared

🔵 **Evidence class:** everything in this section is **secondary** (institutional reports, policy
trackers, survey write-ups) and flagged as such. No primary legal text was readable: `eur-lex.europa.eu`,
`capitol.texas.gov` and `arxiv.org` still do not resolve from this session's network, which is the
same limit `p490`–`p492` recorded. **Nothing below should reach a client deck without a primary read.**

The brief's four per-region queries were each run. 🔴 **Two returned nothing new** and that is stated
rather than left silent, because an unstated miss reads exactly like coverage.

### North America

🟢 **The `p490`/`p491` conflict over Oklahoma S.B. 1734 is resolved by a third independent source,
in `p491`'s favour.** This KB has carried two incompatible descriptions of the same act:

| source | description |
|---|---|
| `p490` | parent opt-out rights |
| `p491` | instructional AI must be **educator-directed with human-in-the-loop review** |
| 🆕 `p493` | districts must **adopt a written AI policy before the 2027-28 school year**, and AI is **barred from being the primary basis for high-stakes decisions such as grading or discipline** |

🟢 **`p493`'s read and `p491`'s are the same duty in different words** — "not the primary basis for
grading or discipline" *is* a human-in-the-loop requirement. **Two of three sources now describe an
oversight duty; `p490`'s parent-opt-out reading is the outlier.** 🔵 Still not a primary read of the
enrolled text, so the flag stays — but **design against the oversight duty, not against opt-out
plumbing**, and note that the two are not mutually exclusive within one act.

🔵 **The commercial point is unchanged and now better supported:** a written-policy mandate with a
dated deadline (2027-28) plus a bar on AI-primary high-stakes decisions is **exactly** the
policy-configurable compliance surface this section already recommends selling. 🟢 It also aligns
North America with the EU shape: the differentiator is the human-oversight gate, so
[`compose/patterns.md`](../compose/patterns.md) `P490-2`'s conformity work is reusable across both.

🔴 **Miss declared:** no new NA adoption figure survived scrutiny. The widely-republished teacher-use
numbers (60% of US K-12 teachers in 2024-25, 32% weekly; a competing 61% for 2026) come from vendor
statistics round-ups that disagree with each other, and the "134 bills across 31 states" count is the
figure this file already ruled **unusable** (trackers disagree by >10×). **Cite a specific statute,
never a count** — that rule is re-confirmed, not replaced.

### EMEA

🟢 **Three institutional actors worth naming, none of them a regulator** — useful for positioning
rather than compliance:

- **The Apply AI Alliance** — a Commission forum convening AI providers, industry, public sector,
  academia and social partners. A venue, not a rule-maker.
- **Commission ethical-AI-in-education guidelines, updated May 2026.** 🔵 Guidance, not binding; the
  binding calendar is still the AI Act's.
- **Council conclusions on a human-centred approach to AI in education.** Direction-setting only.

🟢 **The Article 4 AI-literacy clarification is re-confirmed from an independent source**: since
July 2026 the duty is to **support** staff AI literacy and explicitly **does not require guaranteeing
any specific level**. This matters in pricing — an AI-literacy workstream is a *measures-taken*
deliverable, not a certified-outcome deliverable.

🔵 **The deferral dates re-confirmed again, now from an eleventh independent secondary source**:
stand-alone Annex III education systems **2 Dec 2027**, embedded-in-regulated-products **2 Aug 2028**,
with enforcement by the AI Office and national authorities having started **2 Aug 2026**, and
Regulation (EU) **2026/1744** published in the OJ on **24 Jul 2026**. 🔴 **Still not read at EUR-Lex**
— the convergence is now very strong but the primary text remains unread from this session.
🔵 The **2 Aug 2030 public-authority** claim `p491` flagged **did not resurface this pass** and stays
unverified; it remains the item to check before pricing a ministry programme.

🔴 **Miss declared:** the per-region query returned **no EMEA adoption rate and no vendor-share data**
beyond what `p492` recorded, and **no new EMEA-origin education repository**. The `$2.64B`/31.9% CAGR
and the Finland/Estonia/Netherlands K-12 ranking stand as `p491`'s secondary figures, unimproved.

### APAC

🟢 **A materially new regulatory fact, and it cuts against the obvious assumption: South Korea's
AI Basic Act does not put education in its high-impact tier.** The enumerated high-impact domains
are **health care, energy, transport, hiring and biometric analysis**. Education is **absent**.

🔵 **Why this is worth a paragraph.** Korea has APAC's only comprehensive binding AI statute (in
force **22 Jan 2026**, penalties expected ~Jan 2027), so it is the natural assumption that a Korean
education deployment inherits a high-risk compliance burden. **It does not.** Combined with `T12` —
Korea stripped AI digital textbooks of official textbook status in **August 2026** after adoption
stayed below 30% — the Korean picture is consistent and unusual: **a strong general AI law, no
education-specific high-risk tier, and a reversed national mandate.** 🟢 **Consequence:** sell Korea
on outcomes and general-AI-Act conformity, **not** on an education high-risk hook that does not
exist. The cross-region table's "education named high-risk → Vietnam only" row is confirmed, and
now confirmed *by enumeration* rather than by absence of evidence.

🟢 **The Ipsos ban-support series has an exception this KB had not recorded: Australia and New
Zealand.** Where the seven APAC markets already listed run **23–31%** support for banning AI in
schools, **ANZ shows *higher* support for a ban** — an EMEA-like public mood inside the region this
file characterises as the world's most permissive. 🔵 **Practical effect:** do not carry an
"APAC is permissive" framing into an Australian or New Zealand pitch. Treat ANZ as its own posture
— closer to EMEA on public sentiment, while sitting under Australia's non-statutory,
existing-law-plus-voluntary-guidance regime.

🔵 **Vietnam re-confirmed, not advanced:** a July 2026 decision places education among six
high-risk sectors (automated assessment, behavioural monitoring), **high-risk chiefly where the AI
output is the sole basis for a decision without meaningful human review**, with systems already
running before **15 Aug 2026** getting a grace period to **1 Mar 2027**. 🟡 **This KB's cross-region
table says Vietnamese education systems bind from 1 Sep 2027, "not Mar 2027".** The two dates are
reconcilable — a grace period for *pre-existing* systems versus a general application date — but
**they are not the same obligation and this KB should not carry both without saying which is which.**
Flagged for the next pass; do not quote either to a client yet.

🔴 **Miss declared:** still **no edtech vendor share for any APAC market**, four passes running. The
market report found names Google, Microsoft, IBM, Pearson and Byju's as "key players" with no share
figures attached, which is not usable.

### LATAM

🟢 **This is the region where the evidence genuinely improved this pass, and it improved in
*quality*, not just quantity** — the new figures come from UNESCO IESALC and PISA rather than from
vendor surveys.

| Figure | Value | Source class |
|---|---|---|
| Higher-ed institutions using AI in ≥1 area | **87%** of **200 institutions across 19 countries** | UNESCO IESALC with UNU-IAS |
| Those with a **formal AI strategy** | 🔴 **26%** | same study |
| 15-year-olds who have used AI chatbots for schoolwork | **~9 in 10**, across the **13** regional countries assessed | **PISA 2025** |
| Brazilian school administrators using AI | **53%** — but only **22%** report school guidelines | Cetic.br |
| Argentina, AI use by socio-economic class | **75%** high SES vs **42%** low SES | regional survey |
| AI regulatory instruments, rules and proposals | **716**, across **23** countries and territories | Universidad de los Andes, 2026 |

🟢 **The 87%-vs-26% pair is the strongest single statement of this region's thesis this KB has
carried.** It replaces nothing — the Digital Education Council's 92%-students-vs-30%-satisfied
figures stand — but it moves the claim from *student and faculty sentiment* to **institutional
capability, measured across 19 countries by UNESCO**. UNESCO's own framing matches this file's:
adoption is **driven by individual academics, researchers and students rather than institution-wide
strategies**. 🔵 **This is the sentence to put in a ministry or university-system pitch**, and it is
now attributable to UNESCO rather than to a vendor.

🔴 **The Argentina SES split is new to this KB and changes a pattern recommendation.** A 33-point
access gap between high and low socio-economic classes within one country means a national
deployment that assumes connected, device-equipped students **will widen the gap it was bought to
close**. 🟢 This is the strongest evidence yet for `T9`'s offline-first argument and for
[`compose/patterns.md`](../compose/patterns.md) `P490-3`'s Kolibri base — and `p493` adds a second
delivery surface below it: [`rumi-platform`](https://github.com/Orenda-Project/rumi-platform)
(Apache-2.0, **WhatsApp**, 15 languages), which needs neither an app nor a browser.

🟢 **A binding-ish hook exists after all, and this file said there was none.** This section states
*"there is no binding LATAM compliance hook to sell against."* **Uruguay signed the Council of
Europe Framework Convention on Artificial Intelligence in 2025 — the first country in Latin America
to do so.** 🔴 **Read this carefully before using it:** a signature is **not** ratification and the
Framework Convention is **not** an education-specific instrument; it binds *states* to principles,
not vendors to conformity duties. 🟡 **So the honest status:** LATAM still has **no
education-AI statute in force anywhere** — `p490`'s finding holds for a fourth pass — but Uruguay is
now the region's first treaty-level AI commitment and the natural beachhead for a
conformity-led pitch. **Also newly named:** Colombia's **CONPES 4144** national AI policy
(Feb 2025) and a **Peruvian** AI law whose entry into force is reported as 90 business days after
publication; 🔵 neither was read at source and Peru's status in particular needs verifying.

🔵 **The 716-instrument figure is the LATAM analogue of this file's US bill-count rule.** 716
instruments across 23 countries, with **none in force for education**, is not a sign of a maturing
regime — it is regulatory noise, and one commentary reads it exactly that way: hundreds of
overlapping initiatives producing **uncertainty rather than governance**. **Treat it as context,
never as a count to quote**, the same discipline this file already applies to the "134 bills"
figure in North America.

🔵 **Brazil's PL 2338/2023 re-checked: no movement.** Still in the Chamber of Deputies' special
committee, still awaiting the rapporteur's report, as `p491` recorded. 🟡 And the question of
whether it treats education as high-risk is **still unresolved** — this pass's sources discuss the
bill's risk tiers **without mentioning education**, which is the third pass to return that same
silence. **Do not tell a client Brazil has an education high-risk category coming.**

## 🆕 `p494` — `2026-10-28` — APAC repaired: a deleted jurisdiction restored, and Vietnam's date conflict closed

🔵 **Evidence class:** all regulatory material below is **secondary** (law-firm notes, compliance
trackers, a government-framework launch report) and flagged as such. No primary legal text was
readable: `eur-lex.europa.eu`, `www.tilleke.com` and `english.luatvietnam.vn` (subscriber-gated) do
not resolve or do not open from this session, and 🔴 **`arxiv.org` is now confirmed
`connect_rejected` by this session's egress proxy — an allowlist refusal, permanent, not transient.**
**Nothing below reaches a client deck without a primary read.** Full reads:
[`licence-and-stars.2026-10-28-p494.tsv`](../evidence/licence-and-stars.2026-10-28-p494.tsv).

🔴 **This pass moved one region. North America, EMEA and LATAM returned nothing this file does not
already hold, and the misses are itemised at the end** — because an unstated miss reads exactly like
coverage.

### APAC

🔴 **This file lost an entire jurisdiction to a rewrite, and the lost jurisdiction is the one with
the world's only agentic-AI governance instrument.**

Before this pass, `grep -n "Singapore"` across this file, [`trends.md`](trends.md),
[`../verticals/solutions.md`](../verticals/solutions.md) and
[`../compose/patterns.md`](../compose/patterns.md) returned **one hit** — the Ipsos ban-support
figure (**28%**) at line 181. `p315`'s pre-rewrite copy in
[`archive/2026-10-19-p315-pre-rewrite/intel-market.md`](../archive/2026-10-19-p315-pre-rewrite/intel-market.md)
held a full Singapore posture. `p315`'s rewrite deleted it and left no marker — the same mechanism
`p493` documented for eight table rows, now shown to apply to **prose**, where there is no repo URL
to `grep` for and therefore **no detector at all**. See
[`../agents/trending.md`](../agents/trending.md) `p494`.

🟢 **Restored and re-verified first-hand, in a stronger form than the version that was lost:**

- **Singapore — voluntary instruments that function as a procurement gate.** The **Model AI
  Governance Framework**, the **generative-AI framework**, and the **Model AI Governance Framework
  for Agentic AI** are all voluntary, as is **AI Verify**, the government testing-and-assurance
  toolkit (process checks plus technical tests). 🔵 **But vendors selling into government and banks
  are expected to point to them**, which makes a voluntary instrument a *de facto* procurement
  requirement. National push on student and teacher AI literacy, with teacher training at all
  levels by 2026.
- 🟢 **The agentic framework is dated and attributed:** launched by **IMDA on 22 January 2026** at
  the **World Economic Forum**, and described across multiple independent firm notes as the
  **world's first governance framework built specifically for agentic AI** — systems that plan,
  reason and act autonomously on a user's behalf. Its four axes are **how much autonomy an agent is
  granted**, **how its actions are bounded and logged**, **how humans stay meaningfully in the
  loop**, and **how accountability is assigned when several agents interact**.

🟢 **Why this is a commercial asset rather than a compliance cost, and why its loss was expensive.**
Every recipe in [`../compose/patterns.md`](../compose/patterns.md) is a **multi-agent education
system**, and those four axes are exactly what such a system has to defend. A voluntary framework
that a client's procurement function already recognises is **a scoring rubric Globant can design
to and point at** — not an obligation to argue down. 🔵 **Sell Singapore on demonstrable conformity
to a voluntary standard**, which is a different motion from EMEA's provider-conformity sale and from
the jurisdiction-routing sale this file recommends for APAC generally.

🔴 **And the deletion undercut an existing pattern's premise.** `p315` also held: *"The opportunity
is the DIVERGENCE itself. A single APAC education product cannot satisfy China's binding rules,
India's labelling duty, Japan's promotion posture and Singapore's voluntary assurance with one
configuration."* That is the argument [`../compose/patterns.md`](../compose/patterns.md) `P490-4`
(jurisdiction-routing provenance layer) rests on — and it has been standing on a
four-jurisdiction divergence with **one of the four deleted from this KB**. `P490-4`'s premise is
restored this pass.

🟢 **Vietnam — the date conflict `p493` flagged for this pass is closed, in `p492`'s favour.**
`p493` wrote that this file's cross-region table ("1 Sep 2027, not Mar 2027") might conflict with a
1 Mar 2027 grace period and that neither date should be quoted. 🔴 **There was no conflict.**
`p492`'s section above had already resolved it with a conditional table, and this pass's independent
read confirms `p492` term by term:

| situation | `p492` | `p494` independent read |
|---|---|---|
| education / healthcare / finance, **in operation before 15 Aug 2026** | **1 Sep 2027** | 🟢 confirmed — *"before September 01, 2027, for … healthcare, education, and finance"* |
| all **other** Decision 33 sectors | **1 Mar 2027** | 🟢 confirmed — *"other listed sectors have until March 01, 2027"* |
| issued | **30 Jun 2026** | 🟢 confirmed — `p493`'s "2 July 2026" is **wrong** |
| in force | **15 Aug 2026** | 🟢 confirmed |
| scope | 46 systems / 6 sectors, education is 3 | 🟢 confirmed |

🔴 **One element of `p492`'s picture is single-sourced, and it is the element its advice depends on.**
`p492` concludes *"plan on 1 Mar 2027, not 1 Sep 2027"* for a new build, which follows only from its
row *"a system put into operation within six months after the effective date falls back to 1 March
2027."* This pass finds that claim attributed to **one vendor compliance tracker (AesirX
ComplianceOne)** and **expressly flagged by the reporting as unconfirmed against the official text**.
Everything else in the Vietnam picture is convergent across multiple independent sources.

🟡 **Keep the advice, flag it, and name the primary read as a deliverable.** The error direction is
unfavourable: if the six-month fallback does not exist, a new entrant inherits the **1 Sep 2027**
education date and the engagement has been scoped to a deadline **six months tighter than the law
requires** — billable work nobody is obliged to buy.

🟢 **Vietnam's education scope is three system types; this file recorded one.** `p492` captured the
assessment trigger, which is the one that behaves like EU Annex III. The other two do not:

| Decision 33 education trigger | held before `p494` | engagement consequence |
|---|---|---|
| automatic **assessment, grading or ranking** of students | 🟢 yes | matches EU Annex III — `P490-2` conformity work transfers |
| 🆕 self-learning content generated from **uncontrolled data sources** | 🔴 **no** | a **corpus-governance** trigger. A RAG tutor over an unvetted corpus is high-risk in Vietnam **on retrieval design alone**, with no grading feature in the product at all |
| 🆕 **biometric** monitoring of learner behaviour | 🔴 **no** | the EU **bans** emotion recognition in education (`T6`); Vietnam **permits it as high-risk**. 🔴 **Opposite regimes, not stricter-and-looser** |

🔴 **This qualifies a conclusion this file states unconditionally.** "Build conformity once, in EMEA
shape, and reuse it" holds for the **assessment** trigger and **fails for the other two**: an
EU-conformant build has no corpus-provenance artefact to show a Vietnamese regulator, and on
biometrics an EU design *removes* the feature while Vietnam expects it *documented and governed*.
See `P494-1` in [`../compose/patterns.md`](../compose/patterns.md).

🔵 **Re-confirmed, not advanced:** Japan's **AI Basic Plan adopted 14 July 2026** under the AI
Promotion Act (promotion-first, no penalties); China's **AI-generated-content labelling rules in
force since 1 Sep 2025** alongside its 2022–2023 algorithm, deep-synthesis and generative-AI rules;
India's **DPDP rules notified Nov 2025, obligations phased to May 2027**, plus a **Feb 2026**
amendment requiring platforms above **5 million** Indian users to label AI-generated content. 🟢 All
four postures remain mutually unsatisfiable by one configuration — `P490-4`'s premise, now with its
fourth jurisdiction back.

🔴 **Miss declared, fifth pass running:** still **no edtech vendor share for any APAC market**, and
still no institution-level adoption *rate* for China, India or Japan. The population-level
generative-AI usage figures that surfaced this pass (Singapore **64.3%**, Japan **24.7%**, Jun 2026)
are **working-age population** measures, **not school or firm adoption**, and this file already holds
them — **do not let them be read as education adoption.**

### North America

🔴 **Miss declared: nothing new.** The per-region query returned the landscape this file already
holds — **Idaho SB 1227** (statewide K-12 AI framework, AI-literacy standards, educator training),
**Maryland SB 720** (MSDE guidance, professional development, district tool evaluation), **Arizona
HB 4040** (introduced, not enacted), the **K-12 AI Literacy and Readiness Act of 2026** (introduced
April 2026, advanced by a House committee, not law), **Katy ISD**'s grade-7 supervised-access policy
for 2026-27, and the recurring **"35 states plus Puerto Rico have K-12 AI guidance"** count.

🔵 **The state-count rule is re-confirmed, not replaced.** This pass's sources disagree among
themselves — "35 states and Puerto Rico" against "over half of U.S. states by early 2026" — which is
the same tracker divergence that made this file rule bill and state counts **unusable**. **Cite a
specific statute, never a count.** The teacher-adoption figures (54% of K-12 students, 92% of
university students; separately 86% of education organisations using gen-AI "but most lack a
policy") again come from vendor round-ups that disagree with each other and are **not promoted**.

### EMEA

🔴 **Miss declared: nothing new, twelfth independent confirmation of the same calendar.** The query
returned the Digital Omnibus picture this file already holds — Regulation (EU) **2026/1744**
published in the OJ **24 Jul 2026** and applying from **27 Jul 2026**; stand-alone Annex III
education systems deferred to **2 Dec 2027**; embedded-in-regulated-products **2 Aug 2028**;
**Article 50 transparency duties from 2 Aug 2026**; the emotion-recognition prohibition in education
live since **2 Feb 2025**; and the Article 4 AI-literacy duty softened to *supporting* staff skills
rather than guaranteeing a level. 🔴 **Still not read at EUR-Lex.** The convergence is now
overwhelming and the primary text remains unread from this session — **that is a human deliverable,
not a pass item.**

🔴 **Still missing:** no EMEA adoption rate, no vendor-share data, and **no EMEA-origin education
repository** beyond the two this KB holds
([`dolos`](https://github.com/dodona-edu/dolos), Belgium;
[`open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE), Morocco). The **$2.64B** /
31.9% CAGR figure and the Finland/Estonia/Netherlands K-12 ranking stand as `p491`'s secondary
figures, **unimproved for a fourth pass**.

### LATAM

🔴 **Miss declared: nothing new.** The query returned material this file holds — the **UNESCO
Observatory on AI in Education for Latin America and the Caribbean** (including the **CONALEP /
DGETI** centres-of-excellence pilot in Mexico and the Chilean teacher digital-competency project),
Brazil's **EBIA** national strategy with education as a vertical axis, **Chile's Boletín 16821-19**
(before Congress since 7 May 2024, still *en tramitación*), and **Mexico's** position that multiple
federal AI bills have been introduced and **none has passed**.

🔵 **One source conflict worth recording so it is not inherited.** One secondary source this pass
described Brazil's **PL 2338/2023** as *"in force with staged applicability."* 🔴 **That is wrong and
contradicts every other read this KB holds**, including three prior passes: the bill was approved by
the Senate on 10 Dec 2024 and remains **pending in the Chamber of Deputies' special committee**,
awaiting the rapporteur's report. **Brazil has no AI statute in force.** 🟢 `p490`'s finding —
**no education-AI statute in force anywhere in LATAM** — holds for a **fifth** pass, and whether
PL 2338 treats education as high-risk is **still** unresolved after four passes of silence on the
point. **Do not tell a client Brazil has an education high-risk category coming.**


## 🆕 `p495` — `2026-10-28` — a **second** instance of the prose-loss defect, and it is in LATAM

🔴 **`p494` found one deleted paragraph — Singapore's agentic-AI framework — and said the prose case
is the larger surface because nobody knows to look for a fact a file no longer mentions. `p495`
went looking on purpose and found a second instance, in this file, in LATAM.**

🟢 **The method, so it is repeatable.** This pass ran the per-region queries, then — before writing
anything — `grep -cF` for each returned figure **in the file that should carry it**, not across the
tree. North America came back fully held and nothing was written (see below). 🔴 **LATAM came back
held *somewhere* and absent *here*:**

| LATAM figure returned | in `intel/market.md` | elsewhere in the KB |
|---|---|---|
| UNESCO IESALC adoption split — teaching & learning **73.5%** | 🔴 **0 hits** | 🟢 held — `agents/trending.md`, `repos/trending.md`, `README.md`, `intel/open-gaps.md` |
| DEC LATAM survey population — **30,000+ responses** | 🔴 **0 hits** | 🟢 held in the same four |
| **29 institutions** | 🔴 **0 hits** | 🟢 held in the same four |
| **~30%** of LATAM universities with a published AI-use policy | 🔴 **0 hits** | 🟢 held — `README.md` |

🔵 **This is not a new discovery and must not be written up as one.** Every number was already
verified by an earlier pass. 🔴 **What is new is that the region file an engagement actually reads
had none of them** — they survived only in narrative history, the README and the gap register.
**`intel/market.md` is one of the three mostly-prose files `p494` identified as having been rewritten
in full**, which is precisely the predicted failure, observed a second time.

🟢 **Restored to this file below, and all four are now registered in**
[`../compose/code/p495-prose-claim-gate/claim_register.tsv`](../compose/code/p495-prose-claim-gate/claim_register.tsv)
**so a later rewrite cannot drop them silently** (`make gate-prose-claims`).

### North America

🔴 **Miss declared: nothing new, and `grep` is the reason that is a finding rather than a shrug.**
The query returned MultiState's count of **134 bills across 31 states** in the 2026 session, and the
four states whose 2026 laws require **both** state-level guidance **and** mandatory district-level AI
policy adoption — **Idaho, Maryland, Oklahoma, Virginia**. It also returned ~**10%** of institutions
having formal AI guidelines and **71%** of US teachers lacking AI training.

🟢 **Checked before writing: all of it is already held** — `Oklahoma` in 78 files, `Virginia` in 21,
`134 bills` in 61, `31 states` in 60. 🔵 **`p493`'s rule — grep the KB before filing a find — paid
here in the direction nobody credits it for:** it stopped a fresh-looking "new NA regulatory finding"
that this KB has carried for dozens of passes. **Nothing written.**

🔵 **The standing NA commercial read is unchanged and worth restating because it is the one that
closes work:** a mandate that a district *adopt a policy* is a procurement trigger, not a product
requirement. The four-state cluster buys a **policy-configurable** assistant (`P490-5`), not a
smarter tutor.

### EMEA

🔴 **No EMEA adoption rate and no vendor share. Thirteenth independent pass.** The query returned
the Omnibus calendar and a vendor-blog comparison table (UK light-touch and sector-specific,
Canada's AIDA pending, India's data-protection rules phasing through 2026) — **no adoption
percentage for any EMEA country, and no market-share figure for any vendor.**

🔵 **Thirteen passes of the same absence has itself become the datum.** 🟢 **This is a gap in the
*public* record, not in this KB's effort**, and the honest client sentence is: *EMEA education-AI
adoption is not publicly quantified; the EU position is defined by regulation rather than by
measured uptake.* 🔴 **Do not let a later pass convert this into silence** — silence reads exactly
like coverage, which is the defect this pass is about.

🟢 **One thing did firm up: the two dates the EMEA argument rests on now agree across independent
secondary reads.** This pass's return gives the Digital Omnibus as **Regulation (EU) 2026/1744**,
OJ-published **24 Jul 2026**, applying from **27 Jul 2026**, with stand-alone Annex III education
systems at **2 Dec 2027** and embedded AI at **2 Aug 2028** — matching `p491`'s `2026/1744` and the
**2 Dec 2027** slip this file already carries.

🔴 **And the EUR-Lex primary read this file has demanded since `p491` is now proven impossible from
this session, not merely outstanding.** `eur-lex.europa.eu` returns `http=000, curl exit 56 —
connect_rejected` on both the ELI and `legal-content` URLs: an **egress-allowlist refusal**, the same
signature `p494` established for `arxiv.org`. 🔵 **No future pass will find it cleared.** It moves to
the named **human** deliverable with the two arXiv papers and the Vietnam Decision 33 official text.
🟡 One four-day conflict recorded, not promoted: the Commission's own milestone list gives
**31 Jul 2026** as entry into force against the guide's 27 Jul. **It changes no deadline in any
pattern here.**

### APAC

🟡 **Thin, and the query drifted to enterprise APAC rather than education.** Returns were
financial-services consultation and copyright policy, not education rules. 🔴 **No ministry-level
education adoption rate for any APAC country was returned.**

🟢 **One usable demand-side signal.** Forrester's read that **60% of firms and governments in major
markets such as India and China will integrate locally developed large language models**, with
**education named as a target sector**. 🔵 **That is the sovereign-deployment thesis arriving from the
demand side rather than the regulatory side** — until now `P490-3` (offline-first ministry
deployment) and `P490-4` (jurisdiction-routing) have been argued almost entirely from regulation.
A procurement preference for locally-developed models is a *different* and more durable reason to
build for model-portability: it survives even where no rule requires it.

🟢 **`p494`'s restored Singapore holding stands and is now protected.** The **IMDA Model AI
Governance Framework for Agentic AI** (**22 Jan 2026**, WEF launch) and **AI Verify** are registered
claims in this file as of `p495` — `SG-AGENTIC-FIRST` and `SG-AI-VERIFY` — so the deletion that ran
~179 passes unnoticed now fails `make hooks`.

### LATAM

🟢 **The one region where the query returned quantities, and they are being written into this file
for the first time** (held elsewhere in the KB since earlier passes — see the defect note above):

| figure | source | reading |
|---|---|---|
| **92%** of students and **79%** of faculty actively engaging with AI | Digital Education Council **LATAM Survey 2026** — **30,000+ responses** across **29 institutions** | the demand side is not the constraint |
| adoption by function: teaching & learning **73.5%**, research **57.0%**, administration **34.1%**, community engagement **20.0%** | UNESCO **IESALC** — **200 higher-education institutions** across **19 countries** | 🔵 **administration at 34.1% is the gap in the middle of the stack** |
| **~30%** of LATAM universities have a **published AI-use policy** | Digital Education Council | 🔴 **the governance layer is where the hole is** |

🔴 **The commercial consequence, and it inverts the usual pitch.** With ~92% student engagement
against ~30% institutional policy coverage, **LATAM's bottleneck is not adoption and not capability
— it is governance.** 🟢 **The sellable unit is the policy-and-provenance layer, not another tutor:**
an AI-use policy instrumented in the product — logging, disclosure, assessment-integrity controls,
and a record a rector can show — which is `P490-4`'s provenance layer pointed at an institution
instead of a jurisdiction, and `P493-1`'s all-permissive stack as the base.

🔵 **Administration at 34.1% is the second opening, and it is where the open platforms already
are.** The LATAM shelf answer is the ERP/SIS layer this KB already holds first-hand —
[`openeducat_erp`](https://github.com/openeducat/openeducat_erp) (LGPL-3.0, pin `46a5d7d40082`,
licence byte-read `p495`) — with AI on top rather than a greenfield build.

🟡 **One caveat carried deliberately, not resolved.** This KB holds an unresolved DEC
ordering conflict (`Gap 242`) and a second DEC read reporting **88%** of faculty at *"minimal"* to
*"moderate"* engagement, which sits awkwardly beside **79% actively engaging**. 🔵 **Both are DEC
figures measuring different things (any engagement vs depth of engagement), and this pass does not
claim to have reconciled them.** Quote the **92% / ~30%** contrast, which is robust and is the one
that sells; do not quote the faculty-engagement depth figure without the conflict attached.

🟢 **`p490`'s finding holds for a sixth pass: no education-AI statute is in force anywhere in
LATAM** — which is exactly why the governance product is a *differentiator* here rather than a
compliance cost, and why it has a window.



## 🆕 `p496` — `2026-10-28` — **EMEA's regulatory picture in this file is missing an entire institution**, and the two bodies are easy to confuse

🔴 **The headline is a defect in this file, found by counting rather than by reading.**
`grep -c "Council of Europe" intel/market.md` returns **`0`**. This file's EMEA section carries the
EU AI Act calendar, the Digital Omnibus chronology (Regulation (EU) **2026/1744**) and *"Council
conclusions on a human-centred approach to AI in education"* — and **nothing at all** about the
**Council of Europe**, whose education-AI instrument pipeline this KB **does** hold, in
[`../agents/trending.md`](../agents/trending.md).

🔴 **The two are different institutions, and this file names only one of them while using a word that
reads like both.** The *Council of the European Union* issues the "Council conclusions" cited at the
top of the EMEA section. The *Council of Europe* is a separate treaty organisation of 46 member
states, not an EU body, and it is the one drafting education-specific AI instruments. 🔵 **An
engagement reading this file alone would brief a client that the AI Act is the whole EMEA picture.**

🟡 **This is the third instance of the prose-loss defect** `p494` found in APAC and `p495` found in
LATAM — and the first where the loss is not a deleted paragraph but a **fact that never crossed from
`trending.md` into the file an engagement actually reads.** `T14` covers it; `T16` below extends it.

🔴 **Grade: secondary, and permanently so.** `coe.int` was probed twice this pass and returned
**`getaddrinfo ENOTFOUND www.coe.int`** — this session's egress refusing the host, the same signature
`p494` established for `arxiv.org` and `p495` for `eur-lex.europa.eu`. **The Council of Europe
primary read can never be discharged from this session**, so it joins the named human deliverable.
Everything below is a search-channel snapshot. **Do not quote these titles to a client as verified.**

## Opportunities by region — `p496`

### North America

🟢 **The federal special-education baseline is now a buildable asset, and it is MIT.**
[`jscott5811/IEP-and-Section-504-Plans-Skill`](https://github.com/jscott5811/IEP-and-Section-504-Plans-Skill)
(MIT, 1 068 B, `sha1 e8b3ee2c48a2`) pins **IDEA 34 CFR Part 300** and **Section 504 of the
Rehabilitation Act of 1973**, sourced to US Dept. of Education OCR/OSERS documents by title and date.
🔵 **This KB already held Californian and Arizonan state packs; the federal floor beneath them was
missing.** The commercial shape that follows is *federal baseline + one state pack per jurisdiction*,
which is a per-state engagement with a shared core rather than 50 bespoke builds.

🔵 **A second US jurisdiction layer appears this pass and arrives unusable:** `avivkatz1/easy-iep`
frames IEP-meeting preparation around **FERPA** and Illinois **SOPPA** — the first appearance of
SOPPA anywhere on these shelves — and has **no licence at six paths**. 🔴 **SOPPA is a real
procurement gate in Illinois districts** (vendor contracts, breach notification, data-deletion
duties) and this KB has no permissive asset addressing it. **Named gap, not a filler row.**

🟡 **Demand-side reads this pass, both secondary and both consistent with `T1`:** a vendor roundup
dated April 2026 puts North America at **~36%** of the regional market and reports only **10% of
institutions have formal AI guidelines** while **71% of US teachers lack AI training**; a
market-research page gives **$951M (2024) → ~$2.3bn (2029), ~15.9% CAGR**. 🔴 **The 10%-guidelines
figure is the one that sells institutional delivery work**, and it is the same adoption-without-
governance split UNESCO measured in LATAM (87% using, 26% with a strategy). 🔵 **Two regions,
independent sources, the same gap** — that is `T1` with a second leg.

### EMEA

🆕 **The Council of Europe track, carried into this file for the first time.** Secondary throughout
(`coe.int` is proxy-refused), and the dates below are as reported rather than read:

- **Committee of Experts on AI and Education (`EDU-IA`)** — first meeting **January 2026**; second
  plenary reported for **Strasbourg, 16–17 September 2026**.
- **A legal instrument on AI in education** — listed among the committee's deliverables, in
  drafting. 🔴 **If this lands binding, it is a second EMEA conformity regime beside the AI Act**,
  and it is education-*specific* where the AI Act is horizontal.
- **European Reference Framework for the Evaluation of Educational Technologies** — reviewed at the
  second plenary, still in drafting. 🟢 **This is the procurement-side instrument** that would turn
  edtech evaluation from a vendor claim into a scored framework.
- **Compass for AI and Education** — reported for release **March 2026**, covering AI literacy,
  regulation, teaching and assessment with AI, and edtech evaluation.
- **4th Working Conference on AI Governance in Education** — in preparation. The 3rd (October 2025)
  reported broad stakeholder agreement that regulation is needed to protect children's rights.

🔵 **Why this changes an EMEA engagement's shape.** The AI Act tells a provider *what conformity
costs*; an evaluation framework tells a ministry *what it will score at procurement*. 🟢 **Those are
different deliverables, and only the AI Act one was in this file.** The commercial opportunity is
**conformity-plus-evaluability**: build the AI Act evidence pack, and build the artefacts an
evaluation framework will ask for, once.

🟡 **Adoption reads, all secondary:** **64%** of Europeans agree everyone will need to be AI-literate
by 2030; an Allianz survey across eight countries finds **48%** using AI at least weekly (Germany,
France, Austria in the low 40s); **>50%** of large firms use AI against **<15%** of SMEs. UK's AI
Adoption Summit committed **>£200m**, delivered largely with Big Tech rather than education
providers; the Commission signed **three Advanced Digital Skills grant agreements worth €25.4m**.
Market: **$512.6M (2024) → ~$1,328.8M (2029)**, with UK, Germany, France and Scandinavia named as
leading adopters. 🔴 **The large-firm/SME split is the one to design to** — a ministry or university
procures like a large firm; a school procures like an SME, and nothing in this market is priced for
that.

### APAC

🆕 **A reference design for Indian special education, and its licence makes it a read only.**
`SudhanvaJ-bit/project-samarth` (**no grant at six paths**, `d628b919449a`) targets the **Rights of
Persons with Disabilities Act 2016** and **NCTE/NCERT** guidance, using the **NASET** 11-section IEP
format adapted to Indian law. 🟢 **Its one transferable idea — a statutory accommodation baseline
the model may add to but never remove from — is generalised as
[`P496-1`](../compose/patterns.md).** 🔴 Upstream declares: drafts stored **unencrypted**, no real
student data, board- and state-specific rules **not** implemented, and **15 of 15** evaluation runs
returned `Partial` with the compliance agent never once returning `compliant`.

🔵 **India's statutory hook is new to this file.** The RPwD Act appears in `agents/trending.md` but
not here, and it is the kind of anchor an APAC engagement is built on: a named act, per-category
entitlements, and a national teacher-education body's guidance. 🔴 **No permissive asset addresses
it.** Named gap.

🟡 **Regional posture, secondary:** Forrester describes APAC AI legislation as **fragmented**,
unlike the EU's single regime — Singapore with mature responsible-AI guidelines, China focused on
algorithmic-misconduct law, the **ASEAN Guide on AI Governance and Ethics** still early-stage — and
reports **sovereignty, security and responsible deployment** as 2026 leadership priorities, with
Japan, South Korea and Australia advancing cautiously. Market: **$591.6M (2024) → $1,848.1M (2029),
~20.9% CAGR**. 🟢 **Fragmentation is the product requirement here**, which is why `P494-1`'s
jurisdiction-fork shape remains the right APAC architecture.

### LATAM

🔴 **This leg returned nothing this file did not already hold, and it held it more precisely.** The
mandated LATAM query surfaced the **UNESCO IESALC / UNU-IAS** study of **200 higher-education
institutions across 19 countries**, which this file already carries at finer grain: **87%** using AI
in ≥1 area against **26%** with a formal AI strategy, and the function split **teaching & learning
73.5% / research 57.0% / administration 34.1% / community engagement 20.0%**. 🟢 **The search channel
returned "74%" for teaching and learning; this file's held figure is 73.5%** — the KB is the better
source and the pass adds nothing. **Declared non-finding.**

🟡 **Secondary context that is new but thin:** a 2025 comparative study of AI regulation in higher
education across **Argentina, Brazil, Chile, Peru and Spain**; commentary naming **Chile** as the
regional leader whose AI roadmap survived a change of administration, against a regional pattern of
pilots dropped at each new administration. 🔵 **"Survived a change of government" is the only
durability signal this KB has found in LATAM policy**, and it is the argument for anchoring a
regional engagement in Chile.

🔴 **Mexico: nothing, again.** The Portuguese/Spanish agent query returned `Jeanikt/tutor-ai-agent`
(**held**, MIT, Brazilian-Portuguese voice math tutor) and generic Spanish language-learning repos
with no grants. **No Mexico-specific permissive education asset exists on these shelves**, which
matches this KB's standing record and is now restated with the query that failed to find one.

### Global

🔴 **Market sizing remains unusable, sixth consecutive pass (`T10`).** This pass's single trends
query returned **three different figures for the same year** — **$3.7bn**, **$10.6bn** and
**$11.4bn** for 2026 — from three vendors, with CAGRs from **15.9%** to **46.12%**. 🟢 **Use the
structural facts instead** (adoption-without-governance in two regions, the copyleft platform layer,
the four regulatory regimes); they are stable across passes where the dollar figures are not.

🟢 **One cross-region pattern is firm enough to brief:** the governance gap is measured
independently in two regions now — **26%** of LATAM institutions with a formal AI strategy (UNESCO,
200 institutions / 19 countries) and **10%** of North American institutions with formal AI
guidelines (vendor survey). 🔵 **Different instruments, different sources, same conclusion:
deployment has outrun governance everywhere it has been measured**, and the institutional-delivery
work that follows is the most portable offer in this KB.

## 🆕 `p497` — `2026-10-28` — **the Annex III function layer is the sellable cut**, and all four regions are read against it

Each regional leg below was run as its own query and **its misses are declared**, the practice
`p493` established. 🔵 **Channel caveat, unchanged:** `eur-lex.europa.eu`, `arxiv.org` and
`coe.int` return `ENOTFOUND` from this session, so every instrument cited here is a
**search-channel read, not a primary one**. Instrument numbers and dates below are
upstream-asserted; **do not quote them to a client as verified from the official text.**

### 🟢 The cross-region frame this pass adds

Four jurisdictions, four different instruments, **one shared list of functions**: admissions,
grading, placement, proctoring. The EU names them in Annex III point 3; Vietnam's Decision
33/2026/QD-TTg names education with automated assessment among six high-risk sectors; US states
legislate at the district-policy level; LATAM is building capacity before statute.

🔴 **The commercial consequence is the same everywhere and it is this pass's deliverable:** the four
functions regulators single out are the four where open-source supply is thinnest
([`verticals/solutions.md`](../verticals/solutions.md) `p497` has the per-function table — one MIT
admissions asset at 5★, thin grading, **nothing** for placement, **no permissive proctoring at all**
out of 145 repositories). Governed delivery in that layer is a build, and it is the build clients
have a dated reason to commission.

### North America

**Policy is at district level and it is now mandatory in a named set of states.** Districts are
required to adopt AI policies in **Ohio** (deadline **1 July 2026**, with a state model policy
released) and **Tennessee**; sources add **Maryland** (state education department must develop and
update guidance), **Idaho** (comprehensive generative-AI framework), **Oklahoma** (before the
**2027–28** school year) and **Virginia**. Roughly **33–35 states plus Puerto Rico** have issued
official guidance. More than **1,500** AI-related bills were introduced nationwide this year.

Named instruments: **California A.B. 1159** (proposed — would restrict using student data to train
AI models), **Alabama H.B. 329** (computer-science course including AI instruction as a graduation
requirement). Alabama also recommends a *"data usage restriction"* clause in district contracts.
District signals: **Los Angeles Unified** blocks student-facing generative AI on district devices;
**Wake County** targets a district-wide policy by autumn 2026.

🟢 **Opportunity.** The mandate is to *have a policy*, and the artefact a district must produce is a
governed configuration, not a model. Sell the policy-to-configuration pipeline: `P490-5` is the
pattern, and the ASU admissions agent found this pass is the first US-authored MIT asset to point at
when the conversation turns to admissions.
🔴 **Miss declared:** no national US statute; the picture is 50 patchworks and a vendor-blog-heavy
source base. Florida's proposed rule had a State Board hearing scheduled **16 September 2026** —
**status not confirmed this pass** and it is now past; re-check before citing.

### EMEA

**The dates are the asset here.** EU AI Act **Annex III point 3** makes AI for admissions, grading,
placement and exam proctoring high-risk. The **Digital Omnibus, Regulation (EU) 2026/1744**,
published in the Official Journal **24 July 2026**, defers those Annex III obligations by ~16 months
to **2 December 2027**. Still in force sooner: **Article 50** chatbot-transparency duties from
**2 August 2026**, and the **emotion-recognition prohibition**, which has applied to education
institutions since **February 2025** (subject to the medical/safety exception). The Omnibus softened
the AI-literacy duty — organisations no longer must *guarantee* a "sufficient level" among staff, but
literacy measures remain required.

Schools and universities using commercial AI tools are generally **deployers**, carrying their own
compliance obligations — a state secondary school using a commercial tool to assess student progress
is responsible for that use.

🟢 **Opportunity.** An **18-month dated runway** on functions with almost no permissive supply is the
cleanest build-versus-wait signal on these shelves. Globant can be the **provider** (`P490-2`) and
hold the conformance obligation as the product. Position on the **2 December 2027** date and on the
deployer/provider split, which most institutions have not yet worked out.
🔴 **Miss declared:** no EMEA adoption statistics found this pass — the regulatory picture is
well-sourced, the market-size and usage picture is not. The primary read of the Omnibus text remains
undischargeable from this session and stays on the human deliverable.

### APAC

**Vietnam's Decision No. 33/2026/QD-TTg** identifies high-risk AI systems across six sectors,
**education among them**, naming automated assessment and behavioural categories — an EU-style
risk classification, and the KB's existing entry on it is re-confirmed by this pass's independent
search. **China** and the **UAE** are the only jurisdictions found running **compulsory national AI
curricula**, from the 2025–26 school year. **India** is running a **ten-million-teacher** training
push and folds AI-generated content into its existing intermediary framework (platform rules amended
**February 2026**); sources disagree on how binding its guidance is. **South Korea** has had a public
reversal. **Japan**'s AI Promotion Act carries **no fines or prohibitions**; the Cabinet adopted a
revised AI Basic Plan (**14 July 2026** per one source, **23 December 2025** per another — ⚠️ check).
**China** has no general AI law but enforces service-type rules, including AI-content labelling from
**1 September 2025**.

Adoption is uneven: **Singapore** leads, then Australia, Korea, Taiwan, with Japan, India and China
relatively behind. Japanese firm-level generative-AI use is **34.5%** overall, **63.6%** at
1,000+ staff, **29.6%** at five or fewer (March 2026).

🟢 **Opportunity.** Multi-jurisdiction routing remains the regional differentiator (`P494-1`), and
this pass adds a concrete asset: **`oh-my-paper` is an MIT, APAC-origin, Chinese-language K-12
grading platform** — the first regionally-native permissive asset in the Annex III grading tier,
however early at 1★. Singapore's IMDA agentic-AI framework (recorded `p494`) remains the most
on-point instrument for this KB's own product.
🔴 **Miss declared:** no education-specific adoption rates for Japan, India or China. The Vietnam
Decision 33 official text is still unread (egress-refused) and stays on the human deliverable; the
Japan AI Basic Plan date conflict is **unresolved** — two sources, two dates, neither primary.

### LATAM

**The strongest adoption data of any region this pass, from a named primary institution.** The
**UNESCO IESALC** study of **200 higher-education institutions across 19 countries** found **87%**
using AI in at least one area and **74%** in teaching and learning, while only **26%** had a formal
AI strategy. Uptake splits by institution type: **84%** private non-profit, **68%** public, **52%**
private for-profit. **1 in 2 students** reports confusion about appropriate AI use.

School-level teacher use (OECD TALIS) runs well above the OECD average of 36%: **Brazil 56%**,
**Chile 55%**, **Colombia 53%**, **Costa Rica 52%**.

Regulation: **Brazil's PL 2.338/2023** is in the Chamber of Deputies (text can still change);
**Chile** has a government bill using risk-based grammar adapted to local institutions;
**Colombia** went the policy route with **CONPES 4144** (February 2025). A 2026 Universidad de los
Andes study counted **716 AI-related regulatory instruments and proposals across 23 countries and
territories**, **80%+ initiated since 2023** — fragmentation is the regional risk. **UNESCO** opened
an **Observatory on AI in Education for Latin America and the Caribbean** on **14 April 2026** in
Santiago, with ECLAC hosting and UNU-IAS co-supporting.

🟢 **Opportunity.** The gap is explicit and quantified: **87% adoption against 26% with a strategy**.
That 61-point spread is a governance engagement, not a tooling one — institutional AI strategy,
acceptable-use policy and a sanctioned integrated offering, which is exactly `T1`. Offline-first
delivery (`P490-3`, Kolibri MIT) still applies for ministry-scale and rural work.
🔴 **Miss declared:** no LATAM market-size figure found this pass; no LATAM-specific high-risk
instrument comparable to Annex III or Decision 33 — the region is building **capacity and policy**
ahead of statute, so a compliance-led pitch does not land here the way it does in EMEA.

### Global

Market size: the estimates still do not agree and the **range remains the finding** — 2026 estimates
span roughly **$6.4B–$12.5B**, with sources this pass adding **~$12.5B** and **~$12.3B** for 2026 and
one path of **~$6B (2024) → ~$32B (2030)**. 🔴 **Use the range, never a point**, and the two retired
figures above stay retired.

Themes converging across sources: AI moving **from pilots to embedded infrastructure** in higher ed
(admissions, advising, administration); **governance and oversight** displacing tool adoption as the
institutional priority; **agentic** multi-step AI as the year's development; **purpose-built
education platforms displacing general chatbots**; teacher adoption keyed to saving **5–10 hours a
week**; **verified digital credentials** and competency frameworks gaining ground; and rising pressure
for **explainability where AI influences grades or progression**.

🔴 **Unverified vendor statistics, flagged:** an "83% teaching-assistant deployment" figure and a
"42% outcome gain" circulate in vendor blogs this pass. **Neither is carried into this KB as data.**
