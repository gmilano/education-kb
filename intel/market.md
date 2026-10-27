---
industry: education
region: Global
updated: 2026-10-27
---

# Education AI — market map and opportunities by region

**Pass `p490` — reads of 2026-10-27.** Rewritten this pass; 89 prior pass-sections preserved in
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
  enacted** — do not plan around it.
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

🔵 **Declared gap:** no reliable adoption-rate or vendor-share data for European school AI was
found. Coverage is almost entirely regulatory. Sizing an EMEA engagement needs primary research.

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
  - **Vietnam** — AI law effective **1 Mar 2026**.
- Content labelling is mandatory in **China and India** and absent in **Japan** — so the same
  product needs per-market provenance behaviour.

**Opportunity:** a **jurisdiction-routing content-provenance layer**. One tutor, with
label/provenance/filing behaviour selected per market, is the thing no single-market vendor can
easily ship. Korea's binding act makes it the natural beachhead for a compliance-first pitch;
India's labelling rule is the highest-volume one.

🔵 **Declared gap:** no dedicated data on school AI adoption or edtech vendor share in China,
India or Japan was found — only general AI regulation and the Ipsos attitude series. Adoption
figures for APAC are **not** established in this pass.

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

🔵 **Declared gap:** **no Brazilian or Mexican AI-in-education statute was found.** Searched;
coverage is entirely institutional (UNESCO, IDB) rather than legal. Unlike EMEA and Korea, there
is **no binding regional compliance hook** to sell against — the pitch must be delivery and
outcomes, not conformity.

## Cross-region summary

| | NA | EMEA | APAC | LATAM |
|---|---|---|---|---|
| Market position | largest (36%) | mid | fastest (35.3% CAGR) | smallest, badly sized |
| Binding AI law | none federal; state patchwork | **EU AI Act** | KR, CN, VN yes; JP no; IN partial | **none found** |
| Nearest deadline | varies by state | **2 Dec 2026** (Art. 50 marking) | IN labels live 20 Feb 2026 | — |
| Individual adoption | 53% teachers | not established | low resistance, adoption unmeasured | **highest measured** |
| Sell on | policy configurability | **provider conformity** | jurisdiction routing | institutional delivery |
