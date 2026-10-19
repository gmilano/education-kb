---
industry: education
region: Global
updated: 2026-10-19
---

# Current trends — education

**Pass 315 · 2026-10-19.** Eight trends. Each names the evidence behind it and, where the evidence
is vendor marketing, says so.

## 1. Adoption outran governance, and 2026 is the year governance catches up

Student AI use went **66% → 92%** in a year while US district AI policies sat at ~40% and formal
higher-ed guidelines at ~10%. Every region is now legislating or guiding into an installed base that
already exists. **Implication:** the sellable work in 2026 is not "introduce AI" — it is making
already-ubiquitous AI use legible, logged and defensible.

## 2. Procurement is becoming policy-gated, not feature-gated

Ohio requires an AI framework in every public/community/STEM school by 2026-07-01; Idaho SB 1227
mandates a statewide framework plus a human-teacher guarantee; >28 US states have guidance; the EU
Act makes the tool vendor the "provider" carrying conformity duty. **The RFP question is shifting
from "what can your tutor do" to "show me the audit trail."** A tutor without a governance layer is
increasingly unbiddable in North America and EMEA.

## 3. The permissive-agent / copyleft-platform split is hardening

9/9 agents in `agents/top.md` are MIT, BSD-3-Clause or Apache-2.0. 6 of 10 platforms in
`verticals/solutions.md` are GPL/AGPL/LGPL/ECL. This is not noise — it is the sector's structure, and
it dictates architecture: permissive agents across a network boundary from a copyleft LMS, with
LTI 1.3 as the seam. Expect this to persist; the LMS incumbents have no reason to relicense.

## 4. Tutors are becoming stateful, and memory is the differentiator

DeepTutor's own framing is "**lifelong** personalised tutoring", and it shipped v1.6.15 on the day
of this pass at 41.7k ★. One trend piece describes AI tutors as "context-aware learning companions
rather than simple question-answer tools." The technical consequence: a 2026 tutor needs a learner
model that persists across sessions — which is why FSRS (retention scheduling) and BKT (mastery
estimation, via OATutor) matter more than another chat wrapper.

## 5. Retrieval-grounded tutoring is displacing prompt-only tutoring

LightRAG at 40.2k ★ (MIT, EMNLP 2025) alongside DeepTutor from the same lab is the clearest signal:
the tutor answers from the institution's own curriculum, not the model's priors. This is also the
cheapest route to defensibility under the EU Act's documentation duties — a cited source per answer
is a retrieval artefact, not a compliance feature bolted on afterwards.

## 6. Assessment integrity is pivoting from detection to process evidence

Institutions are moving to oral defence, process-based work and "use it, cite it" disclosure;
commentary reports that institutions with explicit disclosure policies fare better than those that
tried prohibition. There is **no credible open source AI-detection project** in this KB (declared
gap in `agents/top.md`). The open source that *is* available — nbgrader, otter-grader, notebook
provenance via JupyterHub — captures process. That is where the sector is going.

## 7. AI literacy is becoming compulsory curriculum, starting in APAC

India makes AI + Computational Thinking **compulsory for Classes 3–8 from 2026-27** (Classes 9–10
in 2027-28) across 32,900 CBSE schools, with specified hours (50/yr for III–V, 100/yr for VI–VIII).
India's education secretary places it alongside China, South Korea, Finland, Estonia and Singapore.
Revised US CSTA computer science standards are due summer 2026. **Content and teacher-training
demand at national scale, on fixed dates** — and in India, against a stated infrastructure gap
(64.7% of schools have computers, 63.5% have internet), which pushes offline-first design.

## 8. Regional model sovereignty arrives in LATAM

Latam-GPT launched 2026-02-10 (CENIA Chile, 30+ institutions, ~8 TB regional data, Spanish and
Portuguese, indigenous languages planned), explicitly as public infrastructure for governments and
universities. Against a backdrop where LATAM has **no unified AI framework for higher education**,
the sovereignty argument is doing the work that regulation does in EMEA: it is the reason to choose
a regional stack. **This is the one trend in this list with no North American analogue.**

## Trends asserted elsewhere that this pass could NOT verify

- **"EdTech moving from pilots to mainstream deployment in 2026", including VR/AR.** Sourced only
  to vendor/consultancy marketing. Plausible, unverified — and one source in the same search
  describes most institutions as *still in pilot mode*, which contradicts it. Do not put this in a
  client deck as fact.
- **"Language learning is the fastest-growing segment."** Single vendor blog. Unverified.
- **"European Commission published AI-in-education ethics guidelines on 2026-08-17."** Low-authority
  blog, could not be confirmed against any primary source. Treat as false until verified.
- **Corporate reskilling as a primary driver.** Named across several sources but always without
  education-sector-specific figures. Directionally credible, not quotable.
