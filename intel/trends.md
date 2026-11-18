---
industry: education
region: Global
updated: 2026-11-18
---

# Current trends — education

Eight trends, each with the evidence behind it and what it implies for delivery. Researched
2026-11-18.

## T1 — Regulation has moved from guidance to binding rules, and it regulates *use*, not existence

Across every region the question has shifted from "is AI allowed" to "under what oversight".
Oklahoma SB 1734 bars AI used solely for grading, discipline or promotion. Ohio districts must
have an AI framework by 1 July 2026. Korea's AI Basic Act is in force since 22 January 2026.
The EU AI Act is generally applicable since 2 August 2026. MultiState counts at least 25 US
states with enacted or introduced K-12 AI legislation.

**Implication.** Oversight architecture is the product. A tutor without an audit trail and a
teacher-review path is unsellable to an institution in 2026, regardless of how good the model
is.

## T2 — The best open education agents are coming out of universities, not startups

Every institution-grade open education agent verified in this pass is academic: Artemis /
EduTelligence / Pyris (TU Munich, MIT), DeepTutor (HKU, Apache-2.0), OpenMAIC (Tsinghua, MIT),
OATutor (UC Berkeley, MIT), EduWork (ECNU, Mulan PSL v2). The commercial tutoring players
(Khanmigo, Duolingo, Microsoft Elevate) are closed.

**Implication.** The permissive, high-quality assets are academic and their authors want
implementation partners. This inverts the usual open-source posture: the studio is not
competing with these projects, it is the deployment arm they lack.

## T3 — The EU's high-risk deadline moved to December 2027, and that is a selling window

Regulation (EU) 2026/1744 postponed Annex III high-risk obligations for stand-alone education
systems from 2 August 2026 to **2 December 2027**. Transparency duties (Article 50) still apply
from August 2026, and the emotion-recognition ban in schools has been in force since February
2025.

**Implication.** Institutions have a known deadline and now have time to comply properly —
which is exactly when conformity work gets funded. Treat admissions, assessment and proctoring
as high-risk engineering with a December 2027 date. **Verify the date against the regulation
text:** many sources still carry the superseded August 2026 figure, and this is the most
commonly mis-stated fact in the industry right now.

## T4 — Adoption has outrun governance, most measurably in LATAM

TALIS 2024: Brazil 56%, Chile 55%, Colombia 53%, Costa Rica 52% teacher AI use against an OECD
average of 36%. But in Brazil only 22% of administrators report school guidelines while 53%
use AI, and UNESCO IESALC finds 87% of universities using AI with 26% holding a formal strategy.

**Implication.** The sales motion in high-adoption/low-governance markets is not "adopt AI" —
it is "govern the AI you are already using". Shorter cycle, visible pain, faster close.

## T5 — Agentic education is small, and analysts cannot agree whether it is growing

Research and Markets: $2.1B in 2026 at **4.5%** CAGR. Mordor: $2.37B in 2026 at **37.92%** to
$11.83B by 2031. Same segment, same year, an 8x disagreement on growth.

**Implication.** Do not build a client business case on a single analyst number. Build it on
the client's own cost base — graded submissions per term, support tickets per course, hours of
lecture transcription. Mordor's structural observation is the reliable part: tutoring is the
gateway purchase that seeds platform penetration.

## T6 — Sovereign and local inference is becoming a procurement requirement, not a preference

The European University Association's January 2026 report explicitly favours European LLMs.
EU data-residency expectations, plus the offline reality of rural deployment, push the same way.

**Implication.** Self-hosted inference (`ollama`, `vllm`) behind a gateway (`litellm`) with a
local vector store (`qdrant`) should be the default architecture, with hosted APIs as the
exception that needs justifying. This also happens to be what makes the offline/low-bandwidth
segment (Kolibri, Internet-in-a-Box, Project NOMAD) technically possible at all.

## T7 — Content-provenance labelling is now a dated legal requirement in APAC

India's amended IT Rules require prominent labels and provenance markers on AI-generated
content from **20 February 2026**. China's rules on labelling AI-generated content are in
force, alongside the amended Cybersecurity Law (1 January 2026) carrying its first AI clause.

**Implication.** Generated courseware, quiz items and feedback need provenance metadata
emitted at generation time. Retrofitting labels across an existing content library is far more
expensive than emitting them from the start.

## T8 — Stakeholder consent, not model quality, is what kills national deployments

South Korea rolled out AI-powered digital textbooks from 2025 and, after parental and teacher
backlash, reduced them to optional "educational material" status within a year. Separately,
Katy ISD banned generative AI chatbots for K-6.

**Implication.** The most expensive failure mode in this industry is social, not technical. Any
rollout plan above a single department needs a named teacher- and parent-consent workstream
with its own budget line. Korea is the case study to cite when a client wants to skip it.

## Trends we looked for and could not substantiate

- **Measured learning-outcome gains from AI.** The widely circulated figures ("42% improvement
  in learning outcomes", "54% higher test scores") trace to secondary blogs with no primary
  study. We found no credible primary evidence of learning gains at scale. This is a real
  evidentiary hole, and it is why the measurement tier in T3/`compose/patterns.md` matters.
- **A November 2026 education-agent launch.** The newest dated artefact is OpenMAIC `v1.4.2`
  (2026-11-09). No new launch confirmed this month.
- **Vendor market-share data in any region.** Market size exists; share does not.
- **Japanese AI-in-education policy.** Not surfaced despite a targeted search.
