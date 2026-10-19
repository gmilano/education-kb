---
industry: education
region: Global
updated: 2026-10-19
---

# Current trends — education

**Pass 316 · 2026-10-19.** Ten trends. Each names the evidence behind it and, where the evidence is
vendor marketing, says so. Three are new this pass (6, 7, 10); one earlier trend has been
reformulated because better data arrived (1).

## 1. Institutional AI deployment is not landing — and that, not adoption, is the gap

Earlier passes framed this sector as "usage is ahead of governance". The Digital Education Council
AI in Higher Education Global Survey 2026 (**45,398 responses — 27,284 students, 18,114 faculty —
across 35 countries**) supports a sharper reading:

- **88% of students use AI; 77% of faculty do, up 16 points year on year.**
- **43% of students report no AI integration in their courses at all.**
- Among students who *have* experienced institutional AI integration, **only 5% say it transformed
  how they learn.**
- **Only 29% think their instructors are equipped to guide them — 17% in the US and Canada.**
- **64% of faculty have had AI literacy training; 31% feel involved in shaping AI policy.**

Adoption is solved. Institutional deployment is near-absent, and where present it is judged
worthless by 95% of the students exposed to it. **Implication:** the sellable work is not
"introduce AI" and not only "govern AI" — it is making an institutional deployment that students
can tell apart from the chatbot they already use. Training exists (64%) and is not working; that is
a programme-design problem, not a content-sourcing problem.

## 2. Procurement is policy-gated, and the US volume has gone up again

**134 AI-in-education bills across 31 states in 2026.** Ohio requires an AI framework in every
public/community/STEM school by 2026-07-01; Idaho SB 1227 mandates a statewide framework plus a
human-teacher guarantee; California AB 1159 on student data; Oklahoma and Maryland reported to
require human oversight and bar AI from high-stakes student decisions. Federally, H.R. 8747 (K-12
AI Literacy and Readiness Act of 2026) cleared committee markup on 2026-07-21. **The RFP question
has shifted from "what can your tutor do" to "show me the audit trail."**

## 3. Restriction is now a design requirement, not a market loss

New this reading of North America: **New York City runs a one-year moratorium on student-facing AI
through eighth grade**, and **Katy ISD (Texas) is banning generative AI chatbots for K-6.** These
are not outliers to wait out — they are the shape of K-12 procurement. A product that cannot
enforce **grade-band gating** and a **teacher-facing-only mode** is unbiddable in those districts,
and the gate is cheap to build. Treat restriction as a feature spec.

## 4. The permissive-agent / copyleft-platform split is hardening, with one crack

13 of 15 agents in `agents/top.md` carry a permissive software licence. 10 of 15 platforms in
`verticals/solutions.md` are GPL-2.0/GPL-3.0/LGPL-3.0/AGPL-3.0. This is the sector's structure and
it dictates architecture: permissive agents across a network boundary from a copyleft LMS, LTI 1.3
as the seam.

**The crack:** `Selleo/mentingo` (MIT, 96 ★, 1,348 commits) is an MIT-licensed AI-native LMS — a
platform you can link agent code into. At 96 ★ against Canvas's 6.9k it changes no engagement yet,
but it is the first counter-example this KB has recorded, and it is worth watching.

## 5. Deterministic pedagogy under a generative surface is now a shipped architecture

This KB has argued for three passes that the LLM should explain while a deterministic engine
decides. `ArnaudGuiovanna/tutor-mcp` (MIT, 467 commits) ships exactly that — skill graph, Bayesian
Knowledge Tracing, FSRS scheduling, prerequisite gating and cross-session narrative memory — under
the stated principle **"Generative teaching. Deterministic pedagogy."** DeepTutor's own framing is
"lifelong personalised tutoring" (41.7k ★, v1.6.15 on 2026-10-19, now with arXiv 2604.26962), and
gen-mentor's multi-agent ITS architecture was a WWW '25 oral.

The argument has moved from position to implementation. **A 2026 tutor needs a learner model that
persists across sessions and a non-LLM component that decides what comes next** — and that is now
something to integrate rather than build.

## 6. MCP, not LTI, is where agent integration is actually happening — NEW

Every integration artefact found this pass speaks **MCP**: `tutor-mcp` (an entire ITS as an MCP
server), `ankimcp/anki-mcp-server` (520 ★, spaced repetition exposed to any LLM client), Canvas
MCP servers in the wild, `iblai/api`. None of them speaks LTI 1.3, SCORM or xAPI.

This is a genuine fork in the road. MCP gets an agent to *tools*; LTI gets an agent into the
*institution* — launch context, roster, identity, gradebook passback. **A tutor that is MCP-native
and LTI-absent works beautifully for an individual learner and cannot be deployed by a university.**
The glue remains unwritten (`pylti1.3`, MIT, 138 ★ is still the only solid library), which makes
"MCP server inside, LTI tool outside" the integration shape to standardise on across engagements.

## 7. The skill, not the app, is becoming the unit of educational AI — NEW

Among the highest-starred repos under GitHub's `ai-tutor` topic, a striking share are **agent
skills rather than applications**: `GarethManning/education-agent-skills` (878 ★, 165
evidence-grounded teaching skills), `ZeKaiNie/universal-examprep-skill` (309 ★),
`SenmuuuuW/universal-diagnostic-tutor-skill` (247 ★), `KeWang0622/kaogong-skill` (189 ★),
`flysheep-ai/education-skills` (116 ★). `Li-Evan/Bloom` (MIT, 289 ★) ships **both** a skill bundle
and a self-hostable web app.

Two consequences. **Commercially:** the distribution unit is shrinking, and a client's "AI tutor"
may arrive as a prompt bundle their faculty installed, below procurement's line of sight — a
shadow-IT problem that governance work (trend 2) has to cover. **Legally:** skill bundles are
published under *content* licences. `education-agent-skills` is **CC BY-SA 4.0** — ShareAlike
obligations attach to derivative teaching material. That is a licence conversation nobody is having
yet, and it will land in a client deliverable.

## 8. Retrieval-grounded tutoring is table stakes — and the incumbent is shipping it free

LightRAG (MIT, 40.2k ★) alongside DeepTutor from the same lab made curriculum-grounded answering
the default architecture. **Instructure's Project Athena, announced 2026-07-22, is course-context
grounding built natively into Canvas**, positioned as coaching "toward mastery, not answers".

**Grounding in the client's own material is no longer a differentiator against Canvas.** What
remains defensible: the deterministic pedagogy layer (trend 5), the governance and audit layer a US
district must buy anyway (trend 2), and anything on-premise or offline (trend 9). Price and pitch
accordingly.

## 9. Assessment integrity has settled on process evidence, and the detection gap is now a decision

Institutions continue moving to oral defence, process-based work and "use it, cite it" disclosure.
**57% of students say their assessments come with inadequate AI guidance** (DEC 2026) — the gap is
guidance, not detection.

Searched again this pass: there is still **no credible open source AI-detection or academic-
integrity project.** What exists is student-project proctoring (YOLO/OpenCV/MTCNN pipelines,
Electron kiosk browsers), much of it stale or unlicensed, plus MOSS-style code-plagiarism
detectors. Published work finds AI-text detectors inaccurate and unreliable, and the surveillance
posture carries privacy and fairness exposure. **Fourth consecutive pass declaring this gap — and
the correct reading is that it should stay a gap.** The open source that *is* available (nbgrader,
otter-grader, JupyterHub provenance) captures process. Sell that.

## 10. Interoperability standards are becoming the AI story — NEW

**1EdTech's 2026 position is that interoperability is the precondition for AI**, naming **CASE,
Edu-API and OneRoster** as the standards that give an AI system shared institutional context, with
an expanded Generative AI rubric signalled. **IEEE P3428** targets interoperability of LLM agents
in educational systems (initial phases). Agent-to-agent protocols (A2A) and NIST work on a trusted
interoperable agent ecosystem sit in the background.

What makes this actionable rather than standards-committee noise: **the Ed-Fi Alliance's Apache-2.0
implementations are real code** — `Data-Management-Service` (1,105 commits) and `edfi-oneroster`
serving OneRoster 1.2 (151 commits). This is the first pass where "how does your agent know
anything about my institution?" has an open source answer rather than a bespoke-integration answer,
at least in North America.

## Trends asserted elsewhere that this pass could NOT verify

- **"EdTech moving from pilots to mainstream deployment in 2026", including VR/AR.** Vendor and
  consultancy marketing. The DEC survey's 43%-no-integration figure argues directly against it.
  Do not put it in a client deck as fact.
- **"Language learning is the fastest-growing segment."** Single vendor blog. Unverified.
- **"European Commission published AI-in-education ethics guidelines on 2026-08-17."** Low-authority
  blog, unconfirmed against any primary source. Treat as false until verified.
- **APAC growing at ~48% CAGR.** A clear outlier against every other estimate in this KB.
- **Hinds Community College deploying Project Athena to 7,000 students.** Auto-generated news brief,
  not confirmed against Instructure's own release.
- **South Korea's AI Data Protection Act imposing strict edtech privacy protocols**, and
  Australia/Japan data-governance tightening. Single secondary source each, no primary confirmation.
- **Corporate reskilling as a primary driver.** Named across several sources but never with
  education-sector-specific figures. Directionally credible, not quotable.
