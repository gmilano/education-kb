---
industry: education
region: Global
updated: 2026-10-19
---

# Market intelligence — education

**Pass 315 · 2026-10-19.**

## Market size — and why the numbers disagree

Published 2026 estimates for AI-in-education span roughly **$6.4B to $11.4B** depending on the
house and what they count:

| Estimate | Source type | Note |
|---|---|---|
| $6.4B (2025), ~31% CAGR to 2034 | commercial forecast | lowest base of the set |
| $8.3B (2025) → ~$11.4B (2026) | commercial forecast | implies ~37% YoY |
| $10.6B (2026) | commercial forecast | the figure earlier passes of this KB carried |

**Do not quote a single figure to a client.** The honest framing is "high single-digit to low
double-digit billions in 2026, growing 30–40% a year, with no agreement on the base." All three are
vendor or research-house marketing; none publishes its segmentation. The *directional* claim —
fastest-growing software vertical in education, driven by tutoring and assessment — is well
supported; the decimal places are not.

Regional shares, same caveat (single-house figures):
- **North America** ≈ $951M (2024) → ≈ $2.3B (2029) — largest regional share.
- **APAC** ≈ $591.6M (2024) → ≈ $1.85B (2029); China (≈$417.5M) + Japan (≈$318.7M) > 55% of APAC.
- **EMEA / LATAM** — no regional figure found this pass that is not derived from one of the above.
  Declared gap.

## Adoption

- Student AI use: **66% (2024) → 92% (2025)** per one roundup — the steepest adoption curve in the
  sector, and it happened *ahead* of institutional policy everywhere.
- US K-12: teacher AI training **24% → 48%** of districts in the year to spring 2025; student
  ChatGPT-for-schoolwork **13% → 26%**; district AI policies only ~**40%**.
- Higher ed: one roundup puts institutions with formal AI guidelines at ~**10%**, and US teachers
  lacking AI training at **71%**. Treat as directional.
- Cloud deployment held **71.22%** share (2024); K-12 was **45.62%** of adoption.

**The structural gap is the opportunity: usage is near-universal, governance is not.** That holds in
all four regions and it is what a studio sells into.

## Key players — who the client is already talking to

- **Anthropic** — Claude for Education, with a Socratic "Learning Mode"; institutional deals.
- **Google** — free Gemini for college students through 2026; the volume play.
- **OpenAI** — $50M committed to university research partnerships.
- **Instructure (Canvas), Moodle HQ, edX/2U** — incumbent LMS vendors retrofitting AI.
- **Coursera + Udemy** — agreed an all-stock merger; consolidation at the content layer.
- **CENIA (Chile)** — Latam-GPT; the only regionally sovereign model effort in this KB.
- **Open source** — the nine agents in `agents/top.md`; HKUDS (DeepTutor, LightRAG) is the single
  most consequential lab for this sector's permissive tier.

## Regulation by region — the real buying trigger

- **North America:** state-led and fragmented. >1,000 AI bills introduced in 2025, 136 enacted.
  **Ohio is first to require an AI framework in every public/community/STEM school by 2026-07-01.**
  Idaho SB 1227 enacted (statewide framework, local policies, AI cannot replace human teachers).
  Tennessee (2024) requires district AI policies. >28 states + DC have K-12 AI guidance, mostly
  non-binding. Federal action is executive, not legislative; a Dec 2025 EO pushes a "minimally
  burdensome" national framework and state-law preemption is contested in Congress. FERPA, COPPA
  and stricter state privacy law (CA, IL, NY) do the actual binding work.
- **EMEA:** EU AI Act Annex III lists education as stand-alone high-risk. **The Digital Omnibus
  (Regulation (EU) 2026/1744, published in the OJ 2026-07-24, in force 2026-07-27) deferred
  high-risk obligations from 2026-08-02 to 2027-12-02.** Article 50 transparency duties were *not*
  deferred and have applied since 2026-08-02. Emotion-recognition AI has been banned in schools
  since Feb 2025. Schools are "deployers"; the AI vendor is the "provider" and carries conformity
  duty — which is precisely the role a Globant-built tutor occupies.
- **APAC:** fragmented and mostly not education-specific. China's Interim AI Measures (in force
  2023-08-15) require service registration, security review and labelling of AI-generated content;
  the State Council's "AI Plus" guideline (Aug 2025) targets 90% penetration of intelligent
  terminals/agents across six sectors by 2030. Japan is deliberately light-touch and voluntary.
  India's data-protection law phases in to full compliance by May 2027. **India's curriculum mandate
  is the hard date that matters: AI + Computational Thinking compulsory for Classes 3–8 from
  2026-27, extending to Classes 9–10 in 2027-28, rolling out across 32,900 CBSE-affiliated schools
  (50 h/yr for Classes III–V, 100 h/yr for VI–VIII).**
- **LATAM:** no unified framework. Chile leads with a National AI Policy since 2021 and a law under
  discussion. Brazil and Colombia have national AI strategies but no education-specific rules.
  Mexico has no binding national law — SEP/ANUIES recommendations are non-binding. A comparative
  study across Argentina, Brazil, Chile, Peru and Spain found shared need for ethical guidelines but
  sharply different scope and implementation. **Brazil's PL 2338 status could not be confirmed this
  pass — declared gap.**

## Opportunities by region

### North America

1. **Compliance-as-the-product.** Ohio's 2026-07-01 deadline and Idaho SB 1227 create a dated,
   budgeted need: districts must adopt an AI framework and prove human-teacher supervision. Sell the
   governance layer — audit logging, human-in-the-loop gates, parent disclosure, FERPA/COPPA-safe
   retention — not the tutor. This is pattern P3.
2. **Assessment redesign.** Institutions are moving to oral defence, process-based work and
   "use it, cite it" disclosure. Agent-assisted *process* capture (nbgrader/otter-grader +
   provenance trail) is a cleaner sell than AI-detection, which has no credible open source answer.
3. **Teacher enablement at scale.** 71% of US teachers lack AI training; `ai-agents-for-beginners`
   (MIT, 77.5k ★) is a free, licence-clean curriculum base to white-label into PD programmes.

### EMEA

1. **Provider-grade conformity packaging.** Under the AI Act the school is the deployer and the
   tool-builder is the provider. A Globant-built tutor inherits the heavier duty — so productise it:
   technical documentation, risk management, data governance and post-market monitoring shipped
   *with* the tutor. **The 2027-12-02 deferral is the sales window, not a reprieve**; procurement
   cycles in European public education run 12–18 months, so conformity-ready wins bids in 2026–27.
2. **Article 50 is live now.** Transparency duties applied from 2026-08-02 and were not deferred.
   Any deployed tutor needs AI-interaction disclosure and machine-readable marking today — a small,
   immediate, billable remediation across existing EMEA deployments.
3. **Sovereign/on-prem tutoring.** Richie (MIT) + Open edX + self-hosted models keeps data in-region
   and avoids US hyperscaler dependency — the standing EMEA public-sector requirement.

### APAC

1. **India's Class 3–8 mandate is the single most concrete opportunity in this KB.** 32,900 schools,
   a fixed 2026-27 start, specified contact hours, and a documented delivery gap — only 64.7% of
   schools have computers and 63.5% have internet. That gap is the brief: **Kolibri (MIT,
   offline-first) + Sunbird (MIT, the national stack) + locally-cached content**, not a cloud tutor.
2. **China's labelling and registration regime as a design constraint.** Service registration,
   security review and AI-content labelling are mandatory; "AI Plus" gives state-backed demand
   through 2030. Any engagement here is a compliance-first architecture with labelling at the
   generation step, not an afterthought.
3. **Japan's light-touch regime + low public AI use (26.7% in 2024 vs 81.2% China, 68.8% US)** makes
   it the region's adoption-enablement market: Japanese-language tutoring and teacher-facing
   automation, with the fewest regulatory blockers of any major market in this KB.

### LATAM

1. **Latam-GPT as the regional differentiator.** Launched 2026-02-10 by CENIA (Chile) with 30+
   partner institutions; ~8 TB of regional and synthetic data; reported 70B parameters on a Llama 3.1
   architecture; Spanish and Portuguese, with indigenous languages planned; explicitly positioned as
   public infrastructure for governments and universities to adapt. **A tutor grounded in Latam-GPT
   rather than a US-centric model is a proposition no global competitor is currently making.**
2. **The regulatory vacuum cuts both ways.** No binding national rules in Brazil or Mexico means
   faster deployment *and* no procurement checklist to win on. Lead with pedagogy and
   Spanish/Portuguese quality; bring governance as credibility, not as compliance.
3. **Evidence base exists and is usable.** A UNESCO IESALC / UNU-IAS working paper (Sept 2026)
   surveyed **200 higher-education institutions across 19 countries** (fieldwork Aug–Oct 2025),
   mapping AI use across teaching, research, administration and governance. That is a citable
   regional baseline for a proposal — rare in this sector.
4. **Private-market signal:** Luca raised **US$8M Series A** for K-12 AI education in Mexico with
   regional expansion planned; Mexico's AprendeINEA is expanding adult primary/secondary access.

## Declared regional gaps

- **No EMEA or LATAM market-size figure** independent of the global forecasts. Searched; not found.
- **No named EMEA edtech vendors or market-share data** — the EMEA search returned regulation only.
- **No named APAC edtech players**, and no AI-in-schools policy detail for China or Japan beyond
  the economy-wide rules above.
- **Brazil's PL 2338 legislative status** unconfirmed, and no Brazilian edtech market data found —
  a notable hole given Brazil is LATAM's largest education market.
