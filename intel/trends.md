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

**Added 2026-11-13:** the United States now has an equally sharp pairing, from
Google's November 2026 education report (Gallup-based): **85% of educators say
they use generative AI tools; 18% of US teachers report having received any
formal AI guidance from administrators.** This replaces "roughly a quarter of
faculty report a formal institutional policy" as the number to quote for North
America — it is more recent, it is teacher-side rather than policy-side, and the
67-point gap is the clearest statement of the thesis in any region. The pattern
now holds with near-identical shape in **three** regions (US 85/18, Brazil
53/22, LATAM higher ed 87/26), which makes it a structural feature of the
market rather than a local failing.

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

## T9 — The learner-record layer just became permissive, and it is where the defensible architecture lives

Three passes of this KB produced a uniform picture of the **platform** layer:
copyleft everywhere. Moodle GPL-3.0, Canvas AGPL-3.0, Open edX AGPL-3.0, with
Sakai (ECL-2.0) the single permissive exception. The strategic conclusion drawn
so far — build the agent layer permissively and talk to the platform across its
API — was right but incomplete, because the **data** layer was unexamined.

It is now examined, and it is permissive:

- `yetanalytics/lrsql` — **Apache-2.0**, 144 stars, SQL-based Learning Record
  Store, Postgres 14–18 / MySQL / MariaDB / SQLite.
- `openfun/ralph` — **MIT**, 51 stars, LRS plus analytics pipeline plus Python
  library, from France Université Numérique.
- `DavidLMS/learnmcp-xapi` — **MIT**, 16 stars, the MCP server that lets an
  agent read and write those records.

**Implication, and it is the most actionable one in this file:** the learner
data is the part of an education engagement a studio can actually own. The LMS
is the client's and it is copyleft; the model is a vendor's and it is
substitutable; the **learner record — mastery state, progression, evidence — is
the asset**, and it can now be built on Apache-2.0 and shipped inside a
deliverable. Architecture follows: *copyleft platform behind its network API,
permissive LRS and agent layer inside the product.* Pattern `P9`.

Corollary with teeth: **xAPI won the open-implementation race and Caliper did
not.** Caliper has only a spec-document repo in this base, and it is the
1EdTech-native standard most often specified in North American higher ed. Where
the client is free to choose, choose xAPI. Where a contract names Caliper,
price an adapter build.

## T10 — Platform defaults are now the fastest-moving education AI regulation

State legislatures and the EU work in sessions and multi-year transition
periods — the EU's own Annex III high-risk deadline just slipped from
**2026-08-02 to 2027-12-02** via the Digital Omnibus. A platform vendor changes
a default and the effect lands on every school at once.

Google is making **Gemini and Search opt-in (off by default) for K-12 student
accounts**, administrator-enabled, from early 2027 — and is **not** offering
traditional Search without AI summaries as a fallback, since AI Mode and AI
Overviews are built in. The backlash was immediate and political (Bernie
Sanders, NYC Mayor Zohran Mamdani), and Google's education VP defended it on the
grounds that "Search and AI are deeply integrated."

**Implication:** two things follow, and the second is the commercial one.

1. **The "disable AI" option is disappearing from the platform layer.** A
   district that wants search without generative AI no longer has a supported
   configuration. Governance has to be implemented at the institution's own
   layer — policy, logging, review workflow — which is exactly what this KB's
   patterns build.
2. **Forced administrative decisions are procurement triggers.** An
   opt-in default with a date converts an open-ended debate into a dated task
   with a named owner. That is when budget moves. Watch vendor default changes
   as leading indicators of education AI demand — they move faster than any
   legislature, and unlike legislation they arrive with a deadline attached.

## T11 — The most-adopted education AI artifact of this window is a prompt, not a program

**Added 2026-11-13 (fourth pass).**

**Evidence.** `janestreet/agent_skills` (MIT) holds **7.9k stars and 510 forks
on two commits**. It contains one skill, `socratic-tutor`: a `SKILL.md`
instruction set with a diagnostic, a 4-10 sub-skill map rated 0-5, one question
per turn, spaced review and a final assessment. It ships no executable code. In
this KB's own table it is now the **third-largest education-specific agent** by
stars, behind only DeepTutor (58.7k) and OpenMAIC (43.4k) — both of which are
substantial software projects with years of commits behind them.

It is not an isolated case. `GarethManning/education-agent-skills` reached 977
stars as a pure skill collection, `JuneYaooo/teacher-to-skills` (Apache-2.0,
475) exists specifically to *compile a teacher's materials into a skill*, and
`SirhanMacx/Claw-ED` (MIT, 65) is a prompt-and-template layer over a host agent.
Four of the ten most-starred education artifacts in this base are instruction
sets rather than services.

**Why it is happening.** Education's hard part is pedagogy, not inference. A
skill file is the smallest artifact that encodes pedagogy, and it is reviewable
by the people who actually hold the expertise — teachers and curriculum leads —
without a code review. It also inherits the host's model, auth, logging and
updates, which is most of what an education deployment otherwise has to build.

**Implications, including the uncomfortable one.**

1. **A studio's defensible asset in education may be a prompt library, not a
   platform.** That is cheaper to build, faster to localize (see `P10`) — and
   much easier for a client to walk away with. Price and contract accordingly:
   the durable value is in the guardrails, the evaluation and the integration,
   not in the skill text.
2. **Licensing matters more here, not less.** `education-agent-skills` (977,
   **CC BY-SA**) and Jane Street's (**MIT**) are the same artifact class with
   opposite consequences. A share-alike content license on the pedagogy layer
   infects the deliverable in a way most teams will not notice until review,
   because it does not look like software. Check the license on prompt
   collections exactly as hard as on code.
3. **Stars measure attention, not maturity — and the gap has never been
   wider.** Two commits and no maintenance commitment behind 7.9k stars. A skill
   cannot be patched for a vulnerability because it has no vulnerability
   surface, but it also will not be improved for you. Fork and own.
4. **A skill asks; it cannot enforce.** `SKILL.md` cannot stop a model from
   handing over the answer. The controls in `vulinh1704/ai-tutor-agent` — hint
   ladder with an escalation cap, answer-leak regeneration, rubric totals
   computed in code — are the difference between a tutor that is *instructed* to
   be Socratic and one that *is*. Expect to supply that layer in every
   engagement that starts from a skill.

## T12 — Agent-to-SIS integration is arriving through national platforms, not open-source ones

**Added 2026-11-13 (fourth pass). This trend exists because this KB got the
previous version of it wrong.** Three consecutive passes concluded that **no
student information system anywhere had an agent interface**, the third calling
it "a confirmed absence across two consecutive passes." A targeted search this
pass found two.

**Evidence.** `oliverhruby/edupage-mcp` (MIT, 4 stars, **31 tools**) serves
**EduPage**, the school information system used across Slovakia and Czechia —
timetables, grades, homework, daily summary, meal ordering, multi-school
discovery, role-aware student switching, 2FA — and ships on PyPI, Docker/GHCR
and the MCP Registry. `sukhrobyangibaev/mcp_hemis_student` (MIT, 0 stars) serves
**HEMIS**, the higher-education management information system used by Uzbek
universities. Meanwhile **not one** open-source SIS — OpenEduCat (LGPL-3.0,
911), RosarioSIS, Gibbon, openSIS, `frappe/education` (GPL-3.0, 707) — has an
agent interface of any kind.

**The pattern that explains it.** Agent integration is appearing where a
**single platform holds a captive national market**, built by individual
developers scratching their own itch. One developer in Slovakia serves every
EduPage school at once; one developer in Uzbekistan serves every HEMIS
university. No equivalent incentive exists for an open-source SIS, whose
installations are independent, individually configured and individually small.
The consequence is counter-intuitive and worth stating to a client: in the SIS
layer, **proprietary national platforms are better served by open-source agents
than open-source platforms are.**

**Implications.**

1. **Market entry is per-country in this layer, and that favours a global
   studio.** The reusable asset is the *tool surface* — EduPage's 31 tools are a
   worked answer to "what does an agent need from a school SIS" — while the
   adapter is per-platform. Build the surface once, adapt per country.
2. **Both existing servers are fragile in the same way.** EduPage's reaches the
   SIS through a community library on **undocumented endpoints**: no vendor
   contract, breakable by any upstream release. That is the normal state of SIS
   integration and it should be priced as ongoing maintenance, not a one-off
   build.
3. **Check the EMEA mid-market for the next instances.** Slovakia and Czechia
   produced the first one; Italy, Poland, Turkey and the Gulf all have
   concentrated national school-platform markets and no verified MCP server yet.
   This is the cheapest regional wedge in the base.
4. **The open-source SIS gap is a real opportunity, not an oversight.** See
   `P8`, now a selection-and-build pattern at 5-7 weeks with a proven topology
   rather than a greenfield bet.
