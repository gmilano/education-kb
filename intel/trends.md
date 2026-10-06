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
plugin probed this pass is GPL-3.0; both MCP servers are MIT. The integration
style now determines the IP outcome.

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

## Regional notes where the trend diverges

- **North America:** adoption is broad (60% of K-12 teachers) and the binding
  constraint is policy and procurement, not willingness.
- **EMEA:** the AI Act deferral to December 2027 is a design window, and the
  trend is pre-emptive compliance architecture.
- **APAC:** sovereign models everywhere; an education agent layer nowhere. ANZ
  diverges from the rest of the region — higher public support for banning AI in
  schools, where Asian markets surveyed show lower support for bans.
- **LATAM:** the trend is teacher-led, bottom-up adoption outrunning institutional
  governance by a wide margin. UNESCO's LAC Observatory (14 April 2026) is the
  top-down counterweight now forming.

## Declared gaps this pass

- No permissive open source automated grading/assessment agent.
- No open source EU AI Act compliance toolkit specific to education.
- No LATAM-origin open source education agent project.
- No APAC-origin education agent layer on top of the region's sovereign models
  (`panaversity/learn-agentic-ai` is curriculum, not a product).
