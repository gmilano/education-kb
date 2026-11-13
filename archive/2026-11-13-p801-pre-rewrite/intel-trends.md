---
industry: education
region: Global
updated: 2026-11-13
---

# Education AI — current trends

Seven trends, each with the evidence behind it and what it implies for an
engagement. Researched 2026-11-13.

## T1 — The governance gap is the market, not a side issue

Adoption is near-universal among individuals and nearly absent at the
institutional level. 86% of students across 16 countries use AI in their
studies. In LATAM higher ed, 87% of institutions use AI somewhere, 26% have any
framework, 9% evaluate what they deployed. In the US, roughly a quarter of
faculty report a formal institutional policy. More than 50% of teachers in Chile
and Brazil use AI tools while fewer than 10% of institutions have guidelines.

**Implication:** lead with governance, integration and evaluation. "Build us a
tutor" is a smaller and more crowded ask than "make the AI our people already
use safe, measurable and policy-compliant."

## T2 — Regulation is arriving as restriction on instruction, not as enablement

2026 is the year education AI law became concrete, and much of it limits rather
than encourages. Texas HB 2400 bars AI from delivering direct classroom
instruction. New York A 9190 would restrict classroom AI to grade 9+. The EU AI
Act classes admissions and assessment AI as high-risk and has banned
emotion recognition in education since February 2025. Korea's AI Basic Act
(January 2026) and Vietnam's AI law (March 2026) both name education
high-risk/high-impact, Vietnam requiring pre-deployment registration.

**Implication:** architect tutors as **practice, feedback and teacher
augmentation** with a human delivering instruction. That shape survives
contact with the restrictive statutes; a general instruction-delivering tutor
does not.

## T3 — Purpose-built educational AI is beating general-purpose chat

The OECD's 2026 Digital Education Outlook favours purpose-built educational AI
over general-purpose tools. Industry predictions converge on AI being embedded
into admissions, advising and administration rather than run as standalone
pilots. HolonIQ expects selective investment focused on proven instructional
benefit.

**Implication:** the deliverable is an agent wired into the institution's
systems of record, emitting learning telemetry — not a chat window.

## T4 — Agent architecture in education is converging on governed progression

The most architecturally mature education agent found this pass is not the
biggest: Tutor MCP (MIT, 102 stars) separates concerns explicitly — the LLM
creates and explains, while a persistent, auditable engine governs progression.
OATutor (MIT) does the same with Bayesian Knowledge Tracing, and pyKT (MIT)
supplies deep knowledge-tracing models.

**Implication:** keep mastery state and progression **outside** the model.
It gives auditability for regulators, measurability for the institution, and
protection from model drift. The LLM should not be the gradebook.

## T5 — MCP is becoming the LMS integration path, very unevenly

Canvas has a strong MIT MCP server (`canvas-mcp`, 324 stars, up to 102 tools
and 8 agent skills, works across 40+ agent clients). Open edX has only
`openedx-mcp` (AGPL-3.0, 3 stars). **Moodle — the most-deployed LMS in the
world — has no significant MCP server in this window.**

**Implication:** the Canvas path is ready today. For Moodle and Open edX, LTI
1.3 plus the platform's REST API remains the dependable route, and building a
Moodle MCP server is a reusable asset across most of EMEA, LATAM and APAC.

## T6 — "Open source" claims in education AI are frequently wrong

Verified this pass: PageLM (2.1k stars) ships under a non-OSI "Community
License" requiring written permission for commercial use; llamatutor (2.1k) has
no license file at all; education-agent-skills (977) is CC BY-SA 4.0, a content
license. All three are listed as open source in roundups. Star-count claims in
third-party trend reports were stale by 3–6k for fast movers, and DeepTutor is
routinely described as MIT when the repository says Apache-2.0.

**Implication:** verify license and stars on the repository page before a repo
enters a client stack. Secondary roundups are leads, not evidence.

## T7 — The permissive layer is the AI layer; the platform layer is copyleft

Seven of eight significant open-source LMSs are GPL-3.0/AGPL-3.0 (only Sakai,
ECL-2.0, is permissive). Permissive licensing in education clusters in content
and modelling instead: Perseus (MIT), Kolibri (MIT), pyKT (MIT), Oppia
(Apache-2.0), nbgrader and JupyterHub (BSD-3-Clause), ODK Collect (Apache-2.0),
and the two largest agents — DeepTutor (Apache-2.0) and OpenMAIC (MIT).

**Implication:** the standard education architecture is a permissive AI layer
mounted into a copyleft platform over LTI/MCP. Forking the LMS makes the
client's product copyleft; this should be said in week one.

## T8 — Regional origin of education AI has shifted to APAC, and LATAM/Africa produce none

The two largest education AI agent projects in the world are both Chinese
academic projects: DeepTutor (HKUDS, Apache-2.0, 58.6k) and OpenMAIC (Tsinghua
MAIC, MIT, 43.4k). Searched explicitly and found **no LATAM-origin and no
Africa-origin education AI agent at meaningful scale**, and no APAC-ex-China
agent either. India's 2026 activity is in public infrastructure (BHASHINI,
DIKSHA) and announcements (Bharat EduAI Stack, September 2026), not published
agent repos. Africa appears via EkStep's open-source voice stack reaching Kenya
(GITEX) and the Masakhane African-language dataset project — infrastructure,
not education agents.

**Implication:** for LATAM and African engagements, the realistic move is
**localizing permissively licensed APAC and North American agents** to national
curricula and languages, not sourcing a regional agent. Localization capacity is
the differentiator, and it is work Globant is positioned to do.
