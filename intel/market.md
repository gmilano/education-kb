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

## Cross-region summary

| | NA | EMEA | APAC | LATAM |
|---|---|---|---|---|
| Market position | largest (36%) | mid | fastest (35.3% CAGR) | smallest, badly sized |
| Binding AI law | none federal; state patchwork | **EU AI Act** | KR, CN, VN yes; JP no; IN partial | **none in force**; BR PL 2338 stalled in committee |
| Education named high-risk | no | **yes** (Annex III) | **yes — Vietnam**, *Decision 33/2026/QD-TTg*, issued **30 Jun 2026**, in force **15 Aug 2026**, **3 education systems** of 46 | 🟡 claimed for BR PL 2338, unconfirmed |
| Nearest deadline | varies by state | **2 Dec 2026** (Art. 50 marking) | IN labels live 20 Feb 2026; **KR penalties ~Jan 2027**; **VN education 1 Sep 2027** (not Mar 2027) | — |
| Individual adoption | 53% teachers | **$2.64B mkt; FI/EE/NL lead K-12**; rate still unmeasured | **CN compulsory from age 6**; KR mandate **reversed** | **highest measured** |
| Institutions with AI guidance | ~70% | ~70% | not established | **45%** |
| Sell on | policy configurability | **provider conformity** | jurisdiction routing | institutional delivery |


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
