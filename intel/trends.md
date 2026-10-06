---
industry: education
region: Global
updated: 2026-10-06
---

# Trends — Education, October 2026

## 1. Purpose-built beats general-purpose

The most defining trend of 2026 is the move away from generic AI assistants
toward platforms built specifically for education. Buyers who piloted a general
chatbot in 2024–25 are now replacing it with something that understands
curriculum, mastery and assessment. Consequence for Globant: a thin wrapper over
a frontier API is no longer a differentiated offer; the pedagogy layer is.

## 2. From experimentation to governance

AI in education has shifted from "can we" to "under what policy." Clear policies,
data boundaries and oversight are now preconditions of adoption, not follow-ups.
Ohio required every district to have a written AI policy by July 2026; 134
state-level bills were introduced in the US in 2026; the EU AI Act classifies
educational assessment as high-risk. **The compliance artefact is now part of the
deliverable.** Ship the policy mapping, the audit trail and the oversight gate
with the software.

## 3. Agent-native tutoring architecture is settling

DeepTutor (Apache-2.0, 40.8k★, v1.6.13 on 2026-10-04) shows the shape the
category is converging on:

- a **two-layer plugin model** — single-shot *Tools* the model calls, and
  multi-stage *Capabilities* that take over a whole turn;
- **three entry points** — CLI, WebSocket API and Python SDK, so the same engine
  serves a terminal, a web client and an embedded integration;
- **per-learner workspaces with persistent memory**, personality and an evolving
  skill set, rather than one stateless assistant for everyone.

Copy this decomposition even if you do not use DeepTutor. Memory-per-learner and
the Tool/Capability split are the two decisions that matter.

## 4. MCP has become the LMS integration layer

This is the most practically important shift of the last few months.
`vishalsachdev/canvas-mcp` (MIT) now exposes **up to 102 Canvas tools and 8 agent
skills** — including a 20-check WCAG accessibility scanner and bulk grading —
and works with 40+ MCP clients. `peancor/moodle-mcp-server` (MIT) does the
equivalent for Moodle.

Why it matters beyond convenience: **MCP side-cars keep their permissive
license** while in-tree LMS plugins inherit copyleft. Every in-tree Moodle AI
plugin probed this pass is GPL-3.0; both canonical MCP servers are MIT. The
integration style now determines the IP outcome.

**Refinement from the second pass of 2026-10-06 — and it is a correction of
emphasis.** A side-car is permissive *by the author's choice*, not by
construction. Sweeping every Canvas and Moodle MCP server that surfaces in
search, the shelf is in worse shape than the canonical two suggest:
`DMontgomery40/mcp-canvas-lms` (103★, 54 tools, v2.3.0) and `loyaniu/moodle-mcp`
(38★) carry **no license at all** on any branch or in their READMEs, and
`csmediapro/moodle-mcp-server` is **AGPL-3.0 with a paid premium tier**. Only
four of the seven servers probed are usable, and the most-starred non-canonical
one is not. An unlicensed repo is worse than a copyleft one: AGPL is a constraint
you architect around, no license is all-rights-reserved. **A license probe is now
week-one engagement work, not diligence you defer.** Full table in
`agents/top.md`.

## 5. Framework consolidation — AutoGen is out

`microsoft/autogen` (61.3k★) is in **maintenance mode**: no new features,
community-managed, with the README directing new users to **Microsoft Agent
Framework** (MIT, 14.0k★, Python + .NET). Its `LICENSE` at HEAD is now CC-BY-4.0
rather than plain MIT. Any education proposal still specifying AutoGen should be
re-specified on MAF, smolagents or LangGraph. Earlier cycles of this KB
recommended AutoGen; that recommendation is withdrawn.

## 6. Sovereign and on-prem inference is a requirement, not a preference

EMEA districts with data-residency rules self-host open-weight models (Llama,
Mistral) rather than call commercial APIs. Every major APAC economy has built its
own base model — Sarvam AI, ILMU, Sahabat AI, SEA-LION, HyperCLOVA X Think, NTT
Sarashina. California AB 1159 makes "student data is not used for training" a
legal commitment that must be demonstrable. Ollama (MIT) and vLLM are therefore
infrastructure, not an optimisation.

Note the APAC gap: these are **base models with no education agent layer**.

## 7. Assessment is the regulated frontier — and the tooling gap

AI-driven assessment is named in nearly every forecast as a growth area, and in
nearly every regulation as high-risk. Meanwhile **no permissive open source
auto-grader exists** — searched again this pass, nothing credible found. OATutor
(MIT) supplies something more useful than a grader: Bayesian Knowledge Tracing,
which yields a *defensible, inspectable* mastery estimate, published at CHI '23
with follow-up in PLOS ONE.

The honest position with a client: automate item generation and feedback, keep
scoring human-gated, and use an explainable mastery model where a number has to
be justified.

## 8. Skills economy and verifiable competency

Real-time skills visibility, adaptive training and competency frameworks gained
ground in 2026, with career-navigation tools spreading across K-12,
post-secondary and workforce contexts. Open Badges tooling
(`1EdTech/openbadges-validator-core`, Apache-2.0) is the permissive
infrastructure for competency claims a third party can verify. Expect corporate
L&D and public workforce programmes to converge on this.

## 9. Offline-first is an equity requirement, not a legacy concern

Kolibri (MIT) — offline-first teaching and learning with no internet — is the
only fully permissive end-to-end platform on the education shelf. Given CEPAL's
findings on LATAM structural gaps and a widening talent gap since 2022, plus
sub-10% institutional readiness in a region where over half of Chilean and
Brazilian teachers already use AI personally, offline-capable and low-cost is
where the volume is.

## 10. Human connection is becoming the measured outcome

As AI becomes commonplace, human-driven indicators — engagement, well-being,
sustained participation — are becoming *more* important, not less. Practical
effect: instrument for retention and participation, not just for correctness and
completion. A tutoring deployment that improves completion while reducing
sustained participation is a failure that only shows up if you measure it.

## 11. Agent-specific governance has arrived, and a regulator wrote it first

Until 2026, education AI governance was general AI rules applied to education by
analogy. That changed: **Singapore's IMDA published the world's first Model AI
Governance Framework for Agentic AI** at Davos in January 2026, updated in June
2026 — a framework that governs autonomous planning, reasoning and action
directly. Its four dimensions read as a build checklist:

1. **bound the agent upfront** — pick appropriate agentic use cases and place
   explicit limits on the agent's powers;
2. **make humans meaningfully accountable** — define which checkpoints require
   human approval (note *meaningfully*: a rubber-stamp approval does not count);
3. **technical controls across the whole agent lifecycle**, not just at launch;
4. **enable end-user responsibility** through transparency and **training** — the
   framework explicitly expects users of workflow-assisting agents to be taught
   capabilities, common failure points and risks.

Two consequences. First, dimension 4 makes teacher and student enablement a
*compliance artefact*, which means it is fundable rather than discretionary.
Second, a system designed to this framework largely satisfies EU Annex III, the
Oklahoma/Maryland human-oversight statutes and Korea's high-impact
classification at the same time — so use it as the cross-region checklist even on
engagements nowhere near Singapore.

The binding-regulation wave is also wider than this KB recorded: **Korea's AI
Framework Act took effect 22 January 2026** and **Vietnam's dedicated AI law
(No. 134/2025/QH15) on 1 March 2026**.

## 12. Agent Skills are becoming the distribution format for pedagogy

The interesting packaging unit is shifting from "a tutoring app" to "a skill an
agent can load." `vishalsachdev/canvas-mcp` (MIT) ships **8 agent skills**
alongside its 103 tools. `JuneYaooo/lineage-skill` (Apache-2.0, 448★ — the
highest-starred project on the `education-ai` topic) exists only to produce them:
it distils videos, PDFs, transcripts and notes into **source-backed teacher Agent
Skills**, preserving source attribution, extracting the instructor's methodology
and ordering practice tasks progressively.

Why this matters commercially: a skill is portable across the 40+ clients that
speak MCP, which makes an institution's *pedagogy* — its methodology, its
sequencing, its worked examples — the reusable asset rather than the application
wrapped around it. Source-backed matters just as much: a skill that carries
provenance back to the instructor's own materials is defensible in a way a
fine-tune is not, and provenance is what the high-risk regimes ask for. Expect
"turn our course into agent skills" to become a recognisable engagement shape.

## Regional notes where the trend diverges

- **North America:** adoption is broad (60% of K-12 teachers) and the binding
  constraint is policy and procurement, not willingness.
- **EMEA:** the AI Act's general application is **already live (2 August 2026)**;
  what is deferred is the high-risk set (Annex III stand-alone to 2 December 2027,
  embedded to 2 August 2028). The trend is pre-emptive compliance architecture, and
  the sequencing institutions actually use is admin and teacher support first,
  assessment last. The region is $2.64B in 2026 and the K-12 integration leaders
  are Finland, Estonia and the Netherlands — small digitally mature states, not the
  large economies. Africa is in this bucket and is greenfield.
- **APAC:** sovereign models everywhere; an education agent layer nowhere — and
  now sovereign *inferencing platforms* too, so the hosting gap is closing while
  the pedagogy gap stays open. Singapore leads on agentic governance, Korea
  (22 Jan 2026) and Vietnam (1 Mar 2026) on binding law. ANZ
  diverges from the rest of the region — higher public support for banning AI in
  schools, where Asian markets surveyed show lower support for bans.
- **LATAM:** the trend is teacher-led, bottom-up adoption outrunning institutional
  governance by a wide margin — now quantified for higher education: **92% of
  students and 79% of faculty** actively using AI, **94% of faculty** expecting to,
  while **88% of faculty report only minimal-to-moderate engagement**. Adoption is
  done; depth is not. UNESCO's LAC Observatory (14 April 2026) is the top-down
  counterweight now forming, and Colombia's funded CONPES 4144 programme shows the
  regulatory map fragmenting country by country rather than converging.

## Declared gaps this pass

- No permissive open source automated grading/assessment agent.
- No open source EU AI Act compliance toolkit specific to education.
- No LATAM-origin open source education agent project — **re-probed with
  evidence this pass.** `planejaia/OpenMAIC-Brasil`, surfaced by search as a
  Brazil-origin multi-agent classroom with a v1.0.0 release, returns **HTTP 404**;
  every file 404s across four branches. The `education-ai` GitHub topic contains
  no LATAM-origin project at all (its long tail is Chinese, Indian and German, and
  nothing on it exceeds 448★). Latam-GPT is regional foundation infrastructure,
  not a pedagogy layer.
- **Africa: almost entirely uncovered, and that is now stated rather than
  implied.** South Africa's draft national AI policy (2026) is forming and
  GenAITEd Ghana is a published first-of-its-kind curriculum-aligned teacher-education
  agent, but there is no deployed open source African education AI shelf to
  recommend from. Greenfield, with teacher capability as the binding constraint.
- **No permissive open source auto-grader — and now a measured reason to distrust
  the shelf generally.** Of seven education MCP servers probed, three are
  unusable (two unlicensed, one AGPL + paid tier). The education open source
  shelf is thinner than its star counts imply.
- No APAC-origin education agent layer on top of the region's sovereign models
  (`panaversity/learn-agentic-ai` is curriculum, not a product).
