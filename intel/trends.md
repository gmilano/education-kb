---
industry: education
region: Global
updated: 2026-11-13
---

# Education AI — current trends

Eight trends, each with the evidence behind it and what it implies for an
engagement. Researched 2026-11-13.

## T1 — The governance gap is the market, not a side issue

Adoption is near-universal among individuals and nearly absent at the
institutional level. 86% of students across 16 countries use AI in their
studies. UNESCO IESALC, surveying **200 institutions across 19 countries** in
LATAM: 87% use AI somewhere, 26% have any framework, 9% evaluate what they
deployed. In the US, roughly a quarter of faculty report a formal institutional
policy. More than 50% of teachers in Chile and Brazil use AI tools while fewer
than 10% of institutions have guidelines. Brazil's Cetic.br adds the sharpest
single pairing: **53% of school administrators use AI, 22% report their school
has any guideline on its use.**

**Implication:** lead with governance, integration and evaluation. "Build us a
tutor" is a smaller and more crowded ask than "make the AI our people already
use safe, measurable and policy-compliant."

## T2 — Regulation is arriving as restriction on instruction, not as enablement

2026 is the year education AI law became concrete, and much of it limits rather
than encourages. Texas HB 2400 bars AI from delivering direct classroom
instruction. New York restricts classroom AI to grade 9+ with carve-outs for
diagnostics and special education. California AB 1159 would bar using student
data to train AI models. The EU AI Act treats AI for access, allocation,
assessment and monitoring of pupils during tests as high-risk in principle, and
has banned emotion recognition in education since February 2025. Korea's AI
Basic Act (in force 2026-01-22) and Vietnam's AI law both name education
high-impact/high-risk, Vietnam requiring pre-deployment registration.

**Implication:** architect tutors as **practice, feedback and teacher
augmentation** with a human delivering instruction. That shape survives contact
with the restrictive statutes; a general instruction-delivering tutor does not.

## T3 — Purpose-built educational AI is beating general-purpose chat

The OECD's 2026 Digital Education Outlook favours purpose-built educational AI
over general-purpose tools. Industry predictions converge on AI being embedded
into admissions, advising and administration rather than run as standalone
pilots — one roundup's framing is that AI "has moved from experiment to
infrastructure." HolonIQ expects selective investment focused on proven
instructional benefit.

**Implication:** the deliverable is an agent wired into the institution's
systems of record, emitting learning telemetry — not a chat window.

## T4 — Agent architecture in education is converging on governed progression

The most architecturally mature education agents are not the biggest. Tutor MCP
(MIT, 102) separates concerns explicitly: the LLM creates and explains while a
persistent, auditable engine governs progression. OATutor (MIT) does the same
with Bayesian Knowledge Tracing; pyKT (MIT) supplies deep knowledge-tracing
models. New this pass, two independent projects reinforce the pattern from
opposite ends: **`teacher-to-skills`** (Apache-2.0, 475) keeps learner progress
stored *outside* the generated Skill and flags unevidenced material rather than
filling it in, and **EDUKAI LongView** (ISC) frames the whole system as "agent
recommends, teacher decides" over multi-period evidence.

**Implication:** keep mastery state and progression **outside** the model. It
gives auditability for regulators, measurability for the institution, and
protection from model drift. The LLM should not be the gradebook.

## T5 — MCP is now the LMS integration path for Canvas *and* Moodle — but Moodle's is fragmented

Canvas has consolidated: `canvas-mcp` (MIT, 324 stars; README claims up to 128
tools, sidebar says 102). **Moodle has not — it has seven.** Verified this
pass: `Faixiang/Moodle-MCP` (MIT, 206, 10 read-only tools, v1.4.0 2026-11-02),
`G36maid/moodle-mcp` (MIT, 29, Rust, verified against Moodle 3.7/4.5/5.2),
`falkenslab/moodle-mcp` (MIT, 2, ~260 tools via interactive browser login with
SSO/2FA and no token), `MarcosNahuel/moodle-mcp` (MIT, 1, 40 tools with
idempotent upsert-by-`idnumber` writes plus a companion plugin),
`csmediapro/moodle-mcp-server` (AGPL-3.0, 2, open-core with paid premium
tools), `lmscloud-io/moodle-mcp-server` (GPL-3.0, 1), and
`ernesto-butto/moodle-mcp-server` (a multi-course fork). Open edX still has
only `openedx-mcp` (AGPL-3.0, 3).

**This corrects the previous edition of this KB**, which stated Moodle had no
significant MCP server.

**Implication:** the Moodle agent path is open today, but the *choice* is a real
architectural decision rather than a default: read-only vs write, web-service
token vs interactive SSO, plugin vs plugin-free. Pick by the client's security
posture, not by star count. Consolidating this field — or hardening one of the
MIT servers to production — is a reusable asset across most of EMEA, LATAM and
APAC.

## T6 — "Open source" claims in education AI are frequently wrong

Verified: PageLM (2.1k stars) ships under a non-OSI "Community License"
requiring written permission for commercial use; llamatutor (2.1k) has no
license file at all; education-agent-skills (977) is CC BY-SA 4.0, a content
license. All three appear on "best open source AI agent" lists. New this pass:
`nifalconi/educational-agents` (Chile, Niñas Pro course) has **no license
file**, and the grading system published as **"ArguLens" in its arXiv paper is
named nothing of the sort in its repository** (`wwrwbs/AI_AWE`) — a citation
that will not resolve for anyone searching by the paper's name. Star-count
claims in third-party trend reports ran 3–6k stale for fast movers, and
DeepTutor is routinely described as MIT when the repository says Apache-2.0.

**Implication:** verify license and stars on the repository page before a repo
enters a client stack. Secondary roundups are leads, not evidence. The
corollary that bit this KB: **verify a declared gap before quoting it as an
opportunity** — two gaps asserted last pass (Moodle MCP, LTI libraries) were
closed by projects that already existed.

## T7 — The permissive layer is the AI layer; the platform layer is copyleft

Seven of eight significant open-source LMSs are GPL-3.0/AGPL-3.0 (only Sakai,
ECL-2.0, is permissive). Permissive licensing in education clusters in content,
modelling and now integration: Perseus (MIT), Kolibri (MIT), pyKT (MIT), Oppia
(Apache-2.0), nbgrader and JupyterHub (BSD-3-Clause), ODK Collect
(Apache-2.0), **ltijs (Apache-2.0)**, and the three largest agents — DeepTutor
(Apache-2.0), OpenMAIC (MIT), teacher-to-skills (Apache-2.0).

**Implication:** the standard education architecture is a permissive AI layer
mounted into a copyleft platform over LTI/MCP. One practical wrinkle found this
pass: **every verified LTI 1.3 library is Node, PHP or Elixir — none is
Python**, while nearly every agent in this KB is Python. Budget for a
two-process shape (Python agent behind a Node/PHP LTI front door).

## T8 — Education AI's centre of gravity is APAC; LATAM and Africa are nascent, not absent

The two largest education AI agent projects in the world remain Chinese
academic projects: DeepTutor (HKUDS, Apache-2.0, 58.7k, v1.7.2 on 2026-11-06)
and OpenMAIC (Tsinghua MAIC, MIT, 43.4k), with `teacher-to-skills`
(Apache-2.0, 475) a third Chinese-origin entrant. India's activity is still
public infrastructure (BHASHINI, DIKSHA) and announcements (Bharat EduAI Stack,
September 2026) rather than published agent repos.

**Revised from last pass:** LATAM-origin and Africa-origin education agents
**do** exist — they are simply at zero stars. **Manu**
(`Jeanikt/tutor-ai-agent`, MIT): voice-first math tutor in Brazilian
Portuguese, 1st grade to university, TypeScript + LiveKit. **EDUKAI LongView**
(`Keitous/EDUKAI-LONGVIEW`, ISC): MCP-powered longitudinal learner analytics
for African education, bilingual FR/EN, authored in **Guinea**, synthetic data
only. Also found: `nifalconi/educational-agents` (Chile) — unlicensed, so
unusable as published. The earlier claim of regional *absence* was wrong; the
claim of no regional project *at meaningful scale* holds.

**Implication:** the engagement strategy is unchanged — **localize permissively
licensed APAC and North American agents** to national curricula and languages,
and note that OpenMAIC already ships pt-BR and es-MX locales, which shortens
that path considerably. What changes is the sourcing posture: there are now real
regional projects to contribute to, hire from, or co-develop with, rather than a
blank map. A 0-star repo doing longitudinal learner analytics out of Guinea is a
lead, not noise.
