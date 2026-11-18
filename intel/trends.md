---
industry: education
region: Global
updated: 2026-11-18
---

# Current trends — education

Nine trends, each with the evidence behind it and what it implies for delivery. Researched
2026-11-18; T9 added and T1/T3/T6 extended in pass **p890** the same day. Legal facts here were
sourced through search snippets with the source named — every non-GitHub host is blocked by this
session's network policy, so primary texts could not be byte-read. See the verification note in
`intel/market.md`.

## T1 — Regulation has moved from guidance to binding rules, and it regulates *use*, not existence

Across every region the question has shifted from "is AI allowed" to "under what oversight".
Oklahoma SB 1734 bars AI used solely for grading, discipline or promotion. Ohio districts must
have an AI framework by 1 July 2026. Korea's AI Basic Act is in force since 22 January 2026.
The EU AI Act is generally applicable since 2 August 2026. MultiState counts at least 25 US
states with enacted or introduced K-12 AI legislation, and **134 AI-in-education bills across
31 states in the 2026 session**.

**Three additions from pass p890 sharpen this considerably.** **Vietnam** now makes education
AI *statutorily* high-risk: Decision 33/2026/QD-TTg (effective 15 August 2026) lists 46
high-risk systems across six sectors with **education among them**, under the Law on AI
(134/2025/QH15) — existing education systems must comply by **1 September 2027**, new ones by
**1 March 2027**. **North Carolina** (Session Law 2026-41) requires a state model AI policy by
**31 December 2026** and local policies by **30 June 2027**. **California AB 1159** bars using
student data to train AI models outright. And in **Australia**, TEQSA has moved from an
educative to a **regulatory-led** posture in 2026, so the genAI action plans all 203 providers
submitted in 2024 are now inspected.

**Implication (revised).** The binding deadlines are no longer all in late 2027. The nearest is
**six weeks out** (North Carolina, 31 December 2026) and the first statutory education high-risk
clock outside Europe expires **1 March 2027** (Vietnam). California's rule is stronger than a
deadline — it forecloses a whole architecture. **Build retrieval-over-institutional-content with
no training feedback loop, and treat the policy layer as per-jurisdiction configuration rather
than a document.**

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

**But one EU duty is already live and almost nobody is selling against it.** **Article 4, the
AI-literacy obligation, has applied since 2 February 2025**, binds **providers *and* deployers**,
is **not limited to high-risk systems** — a school using an ordinary chatbot is in scope — and
reaches staff and contractors operating AI on the organisation's behalf. The Commission's
position is that supervision and enforcement began **2 August 2026**. No education-specific
guidance on it has been issued by the Commission or any national authority that this pass could
find. *Caveat: several secondary sources say the Digital Omnibus rewrote Article 4 into a softer
duty to "take measures to support the development" of AI literacy, dropping the "sufficient
level" standard; that could not be checked against the Official Journal here.*

**Implication.** Institutions have a known deadline and now have time to comply properly —
which is exactly when conformity work gets funded. Treat admissions, assessment and proctoring
as high-risk engineering with a December 2027 date. **Verify the date against the regulation
text:** many sources still carry the superseded August 2026 figure, and this is the most
commonly mis-stated fact in the industry right now. **And do not wait for 2027 to sell:**
Article 4 is enforceable now, applies to every institution using any AI, and has no official
playbook — a staff AI-literacy programme with evidence of completion is a deliverable that can
be scoped this quarter, and it is the natural door-opener to the 2027 conformity work.

## T4 — Adoption has outrun governance, most measurably in LATAM

TALIS 2024: Brazil 56%, Chile 55%, Colombia 53%, Costa Rica 52% teacher AI use against an OECD
average of 36%. But in Brazil only 22% of administrators report school guidelines while 53%
use AI, and UNESCO IESALC finds 87% of universities using AI with 26% holding a formal strategy.

**Pass p890 adds the student side, and it is more extreme than the teacher side.** **PISA 2025**:
across the **13** Latin American and Caribbean countries assessed, **nine in ten 15-year-olds
have already used AI chatbots for schoolwork**. The **Digital Education Council's 2026 LATAM
survey**: **92% of students** across 29 institutions and **79% of faculty**. Meanwhile **CENIA**
finds **13 of 19** LAC countries do not teach early AI adoption in schools at all. So the
sequence is: near-universal student use, majority faculty use, minority institutional strategy,
and a curriculum that does not mention it.

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

**Two developments from pass p890 harden this from preference into policy.** In EMEA, a
**Council of the EU** document of **29 October 2026** (ST-14902-2026) presses digital
sovereignty and strategic autonomy in AI for education — the preference is now a Council
position, not a university association's opinion. And LATAM finally has its own instance:
**Latam-GPT** (CENIA, Chile) launched **10 February 2026** as an open model trained on Latin
American data, and **UNESCO's Santiago office signed a cooperation agreement with CENIA** in
late February 2026 naming Latam-GPT integration as an early milestone, intended to serve
Ministries of Education. Previously every sovereignty instance in this KB was European.

**Implication.** Self-hosted inference (`ollama`, `vllm`) behind a gateway (`litellm`) with a
local vector store (`qdrant`) should be the default architecture, with hosted APIs as the
exception that needs justifying. Keep the **model layer swappable** — that is what lets the same
build answer "European LLM" in EMEA and "Latam-GPT" in LATAM without re-architecture, and it is
why `litellm` sits in the design rather than a direct SDK call. This also happens to be what makes the offline/low-bandwidth
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

## T9 — Procurement economics, not pedagogy, is becoming the blocker — and buyers have written the spec

**New in pass p890.** **Jisc**, with **Universities UK**, **GuildHE** and the **Association of
Colleges**, issued a joint statement asking AI suppliers for transparent pricing, demonstrable
value, meaningful institutional choice, protection of existing functionality, **granular usage
and cost controls**, interoperability, **data portability** and safeguards against **vendor
lock-in**. The driver is the shift from predictable per-seat licences to **usage-based pricing**,
which makes institutional budgeting impossible, compounded by institutions paying repeatedly for
overlapping AI capabilities embedded across several platforms. A related **Jisc/EAUC** report
found vendors seldom publish institution-level usage figures at all — universities cannot even
measure their own AI emissions.

**Why this is a trend and not a news item.** Every other trend in this file is about what
regulators require. This one is about what *buyers* require, it is written down, and it is
signed by the bodies that represent most of UK higher and further education. It is the closest
thing to a published RFP in this KB.

**Implication — and it is unusually concrete.** The deliverables are named for you:

1. **Per-institution, per-faculty, per-course usage and cost attribution**, exportable. Build it
   with `BerriAI/litellm` (MIT) for per-key budget caps plus an OpenTelemetry-native metering
   layer — **`traceloop/openllmetry` (Apache-2.0)** preferred, because OTel means the data lands
   in whatever stack the institution already runs, which *is* the portability answer.
   `Helicone/helicone` and `openlit/openlit` are Apache-2.0 alternatives.
   **Licence warning:** `langfuse/langfuse` is the largest option but its grant is split — MIT
   Expat core, separate enterprise licence on `ee/` paths, and the copyright now reads
   ClickHouse, Inc. See `repos/trending.md`.
2. **No-lock-in architecture as a contractual artefact**, not a slide: model layer behind
   `litellm`, content and embeddings in a store the client owns (`qdrant`), integration over
   **LTI 1.3** (`ltijs`) so the tool detaches from any one LMS.
3. **A cost model priced per learner-outcome, not per token** — because the buyer has just said
   in public that per-token exposure is the thing they will not sign.

Pricing transparency is now a differentiator a studio can actually win on, and it costs
engineering rather than research to deliver.

## Trends we looked for and could not substantiate

- **Measured learning-outcome gains from AI.** The widely circulated figures ("42% improvement
  in learning outcomes", "54% higher test scores") trace to secondary blogs with no primary
  study. We found no credible primary evidence of learning gains at scale. This is a real
  evidentiary hole, and it is why the measurement tier in T3/`compose/patterns.md` matters.
- **A November 2026 education-agent launch.** The newest dated artefact is OpenMAIC `v1.4.2`
  (2026-11-09). No new launch confirmed this month — re-checked in pass p890 against four fresh
  search legs. The nearest thing is `tutor-agent` on PyPI (MIT, released 2026-11-16), which
  teaches the concepts behind what a coding agent just did; it is developer upskilling, not
  classroom software.
- **Traction for the "tutor as an agent skill" form.** Measured again in p890: the whole cohort
  tops out at **118 ★** and not one member gained a star since the previous measurement. The
  form is real and the time-to-pilot argument holds, but it has no adoption. Demo material, not
  roadmap material.
- **Vendor market-share data in any region.** Market size exists; share does not.
- ~~**Japanese AI-in-education policy.**~~ **Resolved in p890 with a negative answer:** Japan's
  AI law is promotion-focused with voluntary guidelines and there is **no education-specific
  statute or classroom regime**. Confirmed absence, which is why Japan is the lowest-friction
  APAC pilot geography.
- **Any education-specific guidance on EU AI Act Article 4.** The duty is live and
  unenforced-by-guidance; neither the Commission nor a national authority has told schools what
  compliance looks like. Searched directly and found nothing. This is an opportunity, but it
  also means a client's Article 4 package is being designed without a safe harbour — say so.
- **Whether the Digital Omnibus softened Article 4.** Secondary sources say yes; the Official
  Journal text could not be opened in this session. **Unresolved and load-bearing** — it changes
  whether an AI-literacy engagement is compliance work or best practice.
