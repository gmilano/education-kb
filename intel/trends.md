---
industry: education
region: Global
updated: 2026-10-17
---

# Trends — Education, October 2026

> What changed, what it means for a studio engagement, and how confident the evidence is.

## T1 — The education agent consolidated around one project

`HKUDS/DeepTutor` is at **41.5k stars** with a release dated **2026.10.8**, under
**Apache-2.0**. This base previously published 22k for the same repository. Nothing else in
education is within an order of magnitude: the next education-specific agent found is
`Study-Mate` at 1.0k, then `education-agent-skills` at 873.

**For the studio:** the "which tutoring agent" question is effectively settled for
greenfield work. Spend the discovery hours on the student-data model and the integration
boundary instead.

## T2 — Education agents are shipping as *skills*, not applications

The single clearest structural shift this pass. Across the `ai-tutor` and `education-ai`
topic listings, the fastest-rising education repositories are agent **skill packages**:
`education-agent-skills` (873), `lineage-skill` (458, Apache-2.0),
`universal-examprep-skill` (308), `Bloom` (288), `universal-diagnostic-tutor-skill` (246),
`flysheep-ai/education-skills` (114), `skill-instructional-design`, `bloom-taxonomy-quiz-builder-skill`.
Even `instructional_agents` — a peer-reviewed EACL'26 system — published a Claude Code
Skills release (2026.4.15) alongside its v1.1.0.

**For the studio:** the deliverable shape is changing. A client who already runs an
assistant does not want a second web app; they want a skill inside the one they have. That
is a smaller build, a faster sale, and a much shorter integration path. Price accordingly.

## T3 — MCP is becoming the integration layer for education tooling

`ankimcp/anki-mcp-server` (MIT, 516) exposes spaced repetition to any MCP client;
`ArnaudGuiovanna/tutor-mcp` (MIT, 49) turns an LLM into a tutoring system; `Selleo/mentingo`
ships an MCP endpoint as a first-class LMS feature. Meanwhile the GitHub topic
`mcp-server-education` **has never been used by any public repository**.

**For the studio:** a real and growing category with no label. Low-cost, high-visibility
opening for whoever publishes and tags the first substantial education MCP server.

## T4 — EMEA's compliance deadline moved, and that is the engagement

The EU AI Act's high-risk obligations for education moved from **2026-08-02** to
**2027-12-02** via the AI omnibus amendments (in force 2026-07-27). **Transparency duties
went live on 2026-08-02 regardless.**

**For the studio:** two distinct offers, not one. A short remediation scope now (AI
disclosure, deepfake disclosure) and a 14-month compliance-by-design build before December
2027. Clients reading the delay as a reprieve are the pipeline.

## T5 — "Teach about AI before teaching with it" is now written policy

Brazil's MEC published a *Referencial* for responsible AI in education (March 2026) and
basic-education curriculum guidance (April 2026), with an official framing of avoiding
careless tool use in basic education. Mexico's SEP found **76% of professors make materials
with AI but only 36% teach students to use it**, with 9 in 10 asking for training. India
made AI and computational thinking **compulsory from Class 3** from AY 2026-27.

**For the studio:** the biggest funded demand in education AI right now is **curriculum and
teacher formation**, not student-facing tutors. Three governments on three continents are
buying the same thing.

## T6 — Digital sovereignty turned open source into the default, not the discount

Brazil's MEC *Referencial* explicitly calls for national solutions that reduce dependence on
global platforms. Moodle 5.1 added provider-level control and per-course/per-activity AI
toggles, so a local Ollama or vLLM endpoint is a supported configuration rather than a hack.

**For the studio:** self-hosted open source plus local inference is now the *compliant*
architecture in Brazil and the *sovereign* architecture in EMEA. The cost argument is no
longer the main argument, which is a much stronger place to sell from.

## T7 — Knowledge tracing is quietly broadening into cognitive diagnosis

`pykt-toolkit` is the reference benchmark at **450 stars** — materially smaller than this
base previously claimed (1.2k), and worth knowing before citing it as an "industry standard".
Around it: `EduData` (Apache-2.0, 313) for datasets, `pyedmine` (MIT, 82) covering tracing
*plus* cognitive diagnosis *plus* recommendation, `EduStudio` (MIT, 78) for unified
cognitive modelling.

**For the studio:** when the ask is "what should this student do next" rather than "what
does this student know", `pyedmine` is the better base. Both are MIT.

## T8 — Academic integrity became an assessment-architecture problem

`dodona-edu/dolos` (MIT, 352) for source-code plagiarism, `Artemis` (MIT, 819) for automated
feedback with an auditable exercise runner, `Numbas` (Apache-2.0) for randomised maths
assessment. Randomisation and provenance are design choices in the assessment, not
detectors bolted on after.

**For the studio:** in jurisdictions barring AI from high-stakes decisions (Oklahoma,
Maryland, NYC's K-8 moratorium), *assessment integrity* is the part of the AI story that is
unambiguously permitted. Lead with it where student-facing AI is restricted.

## T9 — The licence surface under education AI is unreliable, including ours

Four published cells failed verification this pass and one repository is gone:

- `openedx/edx-platform` is **AGPL-3.0**, not Apache-2.0 as previously published — a
  network-copyleft obligation on the most likely MOOC base in the shelf.
- `CaviraOSS/PageLM` ships a bespoke **non-commercial** licence that prohibits
  redistribution outright. **This base's own `evidence/verified-repos.2026-10-15-p213.tsv`
  grades it `MIT`.**
- `sakaiproject/sakai` is **ECL-2.0**, not Apache-2.0. `chamilo-lms` is GPL-3.0, not GPL-2.0.
  `instructional_agents` is MIT, not Apache-2.0.
- `OpenEduCat-Inc/OpenEduCat` is a **404**; the canonical repo is `openeducat/openeducat_erp`
  (LGPL-3.0).
- `GeminiLight/awesome-ai-llm4education` serves **no LICENSE file**, against a published MIT
  claim.

Counter-example in the other direction: `Open-TutorAi/open-tutor-ai-CE` opens *"All rights
reserved"* and **is** plain BSD-3-Clause — that phrase is part of the BSD form. Flagging it
would have been a false positive, and a false retraction costs a usable row.

**For the studio:** read the `LICENSE` payload for every repository that enters a client
deliverable. A secondary source, an aggregator table, a GitHub sidebar badge and this
knowledge base have all been wrong about an education licence in the last two weeks.

## T10 — The permissive LMS market is one candidate deep

Across every platform verified this pass, **OpenOLAT (Apache-2.0)** is the only complete LMS
without a copyleft licence. Moodle is GPL-3.0, Open edX AGPL-3.0, Chamilo/ILIAS/Gibbon GPL,
Sakai ECL-2.0, Vacademy AGPL-3.0, OpenEduCat LGPL-3.0.

**For the studio:** when procurement rules out copyleft, there is exactly one LMS answer and
two architectural ones — build the agent as an **LTI tool** (`tsugi`, Apache-2.0) or an
**XBlock** (Apache-2.0), keeping the permissive boundary around the part you deliver. Say
this early; it reframes a licence objection as a design decision.

## Confidence notes

- **Payload-verified (strongest):** every licence in this KB's tables, read from
  `raw.githubusercontent.com` on 2026-10-17.
- **Page-verified:** star counts, from repository pages or topic listings dated 2026-10-17.
- **Policy, primary-adjacent:** EU AI Act dates, Brazil MEC documents, India's curriculum
  mandate, SEP survey figures — reported consistently across multiple sources but read
  through secondary coverage, not official gazettes.
- **Vendor-sourced, treat as direction only:** all market-size figures; Moodle 5.2/5.3
  version and LTS-date claims.
- **Declared gaps:** no school-level Japan data; no APAC- or LATAM-origin open-source
  education project with meaningful adoption; no high-adoption open-source grading agent;
  Estado de México's April 2026 reform truncated in all located sources.
