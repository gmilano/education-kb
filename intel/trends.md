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
over general-purpose tools. **Updated 2026-11-13 (fifth pass) with the specific
finding, because it is far more useful to a client than the preference was.**
The report — subtitled *Exploring Effective Uses of Generative AI in Education*
— separates **task performance** from **learning**, and finds that students with
access to general-purpose GenAI **produce higher-quality output, but that the
advantage disappears, and sometimes reverses, in exams once access is removed.**
Purpose-built educational AI, by contrast, shows **sustained** gains. 🔵 **This
is the single most sellable sentence in this KB**: it converts "buy a
purpose-built tutor instead of a chatbot licence" from a vendor preference into
an evidence claim from an OECD report, and it gives an institution a measurable
acceptance test — **measure under withdrawal, not under access.** The report
also recommends systems co-created with educators and learners in which
**teachers set acceptable error levels and monitor interactions**, which is the
same human-review-gate shape this KB's `P6`, `P7` and `AI-Teaching-Agent` row
already converge on. Industry predictions converge on AI being embedded
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
not** — but **the reason is narrower than this trend originally stated, and the
original wording is corrected here (fifth pass).** This paragraph used to read
"Caliper has only a spec-document repo in this base." **That is withdrawn:
Caliper has six verified implementations** (`repos/foundations.md`), including
an **MIT** sensor and an **Apache-2.0** analysis layer. 🔴 **What xAPI has and
Caliper does not is the _store_:** `yetanalytics/lrsql` is **Apache-2.0** with a
Postgres 14–18 / MariaDB / MySQL / SQLite matrix, while the only Caliper event
store found anywhere is **unlicensed**. Caliper's reference layer is also
**private** — 1EdTech made `caliper-php` private, which is documented in a
university fork's own description. **Where the client is free to choose, choose
xAPI — the store row is the whole reason.** Where a contract names Caliper,
**do not price "an adapter build"**: price the **event store only**, and adopt
the sensor, the Moodle emitter and the analysis layer. Full table and reasoning
in `T14`; recipe in `P11`.

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

**Updated 2026-11-13 (fifth pass) — this trend's own prediction landed, and half
of its premise broke.**

🟢 **The prediction landed.** Implication 3 below named *"Italy, Poland, Turkey
and the Gulf"* as the concentrated national school-platform markets to check for
the next instance. **Türkiye produced it.**
`hanifisenturk/sabis-mcp-server` (**ISC**, 2 stars) serves **SABIS**, the
student information system of Sakarya University — one tool, `get-grades`,
returning course codes, assessment types and weights, final letter grades and
term. It is **Puppeteer web scraping with the student's own credentials in
environment variables**, which makes it the third instance of the fragility in
implication 2 and the most fragile of the three. **Three-for-three: every
agent-to-proprietary-SIS path in this base is unofficial.** 🔵 **A named
prediction that resolves in one pass is worth more than the finding itself —
keep naming them.**

🔴 **The premise broke on the other side.** This trend asserted that **"not one**
open-source SIS has an agent interface," naming OpenEduCat first.
**OpenEduCat has one.** It is a set of **Odoo addons**, and Odoo has two mature
MCP servers whose tools take the model name as a parameter —
`erpipe-org/mcp-odoo` (**MIT, 433 stars**) and `ivnvxd/mcp-server-odoo`
(**MPL-2.0, 415 stars**). The error was not in the data but in the search: four
passes looked for an *education-specific* server. **The corrected trend is
therefore two-sided, and the two sides have opposite shapes** — proprietary
national SIS products get **bespoke, unofficial, fragile** agent paths, while
open-source SIS products inherit **generic, sanctioned, maintained** ones from
the platform underneath. That second half is now `T13`.

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

## T13 — The agent surface for a vertical system often already exists one layer down, as a general-purpose platform connector

**Added 2026-11-13 (fifth pass).** This is the methodological trend of the pass
and the one with the widest reach beyond education.

**Evidence.** Four consecutive passes of this KB searched for an education SIS
agent interface and concluded, with increasing confidence, that open-source SIS
products had none. The conclusion was wrong, and the reason was the search
frame: **every query asked for an *education* server.** OpenEduCat (LGPL-3.0,
**911 stars, 789 forks**) is a set of **Odoo addons**, and Odoo has two mature
MCP servers that address models by name:

| Connector | License | Stars | Governance model |
|---|---|---|---|
| `erpipe-org/mcp-odoo` | **MIT** | 433 | Writes gated in the **agent**: direct `create`/`write`/`unlink` blocked; `preview_write` → `validate_write` → `execute_approved_write` with a single-use, same-process, expiring token, `confirm=true` and `ODOO_MCP_ENABLE_WRITES=1` |
| `ivnvxd/mcp-server-odoo` | MPL-2.0 | 415 | Writes gated in the **institution**: companion Odoo module with a per-model allowlist and separate read/write/create/delete permissions, over Odoo's own record rules |

`search_records`, `read_record`, `get_model_fields` and `list_models` take the
model name as a parameter, so `op.student`, `op.admission`, `op.exam.attendees`
and `op.fees` are reachable with no education-specific code. **At 433 stars the
MIT connector is larger than every education-specific agent this KB has ever
admitted except DeepTutor, OpenMAIC and `janestreet/agent_skills`.**

**Why this generalises past education.** The economics are the same in every
vertical: a general-purpose platform (Odoo, Frappe, Salesforce, SAP, ServiceNow)
amortises connector maintenance across **every** industry that runs on it, while
a vertical-specific connector is paid for by one industry's installed base. **So
the vertical connector is built only where no general platform sits underneath.**
That predicts exactly what this base observes — Moodle, Canvas and Open edX
(purpose-built, no general platform below) each grew bespoke MCP servers, while
OpenEduCat (Odoo below) never needed one and never got one.

**Implications.**

1. **Search the substrate before declaring a vertical gap.** The question is not
   "is there an education MCP server for X" but "what general-purpose platform
   is X built on, and does *that* have one." 🔵 **The test is cheap and this
   base should run it on every remaining unserved row.**
2. **The next instance to check is Frappe.** `frappe/education` (GPL-3.0, 707)
   and `frappe/lms` (AGPL-3.0, 3.4k) sit on the Frappe framework, which is a
   general-purpose platform with its own ecosystem. **Nobody in this KB has
   checked whether a generic Frappe MCP server exists.** That single search
   could close the SIS gap for a second open-source product.
3. **Genuinely unserved means "purpose-built and small".** RosarioSIS (GPL-2.0,
   654, PHP/Postgres) and Gibbon (GPL-3.0, 638, PHP/MySQL) have no general
   platform beneath them and no connector — **and they are the LATAM K-12 and
   international K-12 incumbents.** The unserved set is now small, named, and
   regionally specific, which makes it sellable rather than embarrassing.
4. **Inherited governance is better governance, and it is a selling point.**
   Both Odoo connectors gate writes — one in the agent, one in the institution's
   own Odoo permissions — because a general-purpose ERP connector *must* survive
   finance and HR data. An education-specific server written by one developer
   rarely does: of the three proprietary-SIS servers in this base, none gates
   writes, and one replays the student's own credentials. 🔵 **"Your agent
   inherits Odoo's access rights and record rules" is a stronger governance
   story than anything a bespoke education server offers**, and `T1` says
   governance is the market.
5. **Pick the connector by who must own the policy.** MIT + agent-side gating
   (`erpipe-org`) where the studio operates the deployment; MPL-2.0 +
   institution-side allowlist (`ivnvxd`) where the client's administrator must
   hold the control. 🔴 **Never ship `ivnvxd`'s "YOLO mode"** — it needs no
   companion module, bypasses all MCP-level access control, exposes 200+ models,
   and in full form permits delete. Its own README restricts it to development.

🔴 **Stated limit, because this trend is new and load-bearing.** The path is
**architecturally verified** — model-generic tools, Odoo addons, both read off
the repository pages — and **has not been run**: no Odoo instance was stood up,
OpenEduCat installed, and a tool called against `op.student` (`Gap 286`). Quote
it as a verified architecture, never as a delivered integration.

## T14 — All five interoperability edges are now permissively implemented, but the two telemetry standards are not interchangeable

**Added 2026-11-13 (fifth pass), and it closes the question `T9` opened.**

`T9` established that the learner-record layer became permissive and said
plainly that **"xAPI won the open-implementation race and Caliper did not"** —
Caliper having only a spec-document repo in this base. **The second half of that
is now withdrawn: Caliper has six verified implementations.** But the race was
won on a component xAPI has and Caliper does not, and that is the durable
finding.

| | xAPI (learning record) | Caliper (analytics) |
|---|---|---|
| Permissive **store** | 🟢 `yetanalytics/lrsql` — **Apache-2.0, 144★**, Postgres 14–18 / MariaDB / MySQL / SQLite | 🔴 **None.** The only store found, `open-ent/caliper` (Caliper **1.2**, Vert.x, 33 unit tests, Open ENT / France), carries **no licence** |
| Permissive **sensor / client** | 🟢 `openfun/ralph` (MIT, 51★), `DavidLMS/learnmcp-xapi` (MIT, 16★) | 🟡 `CarnegieLearningWeb/caliper-ts` — **MIT, 0★**, GitHub Package Registry only |
| **LMS** emitter | 🟡 via plugins and xAPI wrappers | 🟢 `open-lms-open-source/moodle-logstore_caliper` (GPL-3.0, Moodle 2.7+) |
| **Analysis** layer | 🟡 `ralph`'s pipeline CLI | 🟢 `tl-its-umich-edu/caliper-event-analysis` (**Apache-2.0**, U-M + CSCAR notebooks) |
| Reference layer | 🟢 public | 🔴 **member-gated** — 1EdTech's Best Practice Guide advertises Java/JS/PHP/Python/Ruby/.NET sensors and states that Contributing Members and Affiliates request GitHub access; `1EdTech/caliper-js` and `IMSGlobal/caliper-js` both **404** |

**The asymmetry is structural, not incidental.** xAPI's open stack grew from
public reference code; Caliper's reference lineage sits behind consortium
membership, and the implementations that *are* reachable are **university and
consortium forks of 1EdTech's public releases** — `tl-its-umich-edu/caliper-php-public`,
`umich-caliper-php`, `UnizinAnalytics/caliper-net-public`. 🟢 **One of those
forks documents the withdrawal in its own description, which turns this from
inference into evidence:** *"This had been archived, but has been unarchived
following **1EdTech making its caliper-php private**."* **The University of
Michigan un-archived a dormant fork because the upstream disappeared.** The
chain is 1EdTech → Unizin → Michigan. 🔵 **That fork pattern is the general
workaround for any member-gated standard, and it is why slug-guessing failed
here for four passes while one org-listing request succeeded** — the originals
are not merely unindexed, they are **private**, so no spelling of the slug could
ever have resolved.

**Implications.**

1. **Where the client is free to choose, still choose xAPI.** `T9`'s
   recommendation is unchanged and the store row above is the entire reason.
2. **Where a contract names Caliper, the price changed and the pitch should.**
   The old line — "no open starting point; that is a build" — is wrong. The
   accurate line: **an MIT sensor, a GPL-3.0 Moodle emitter, an Apache-2.0
   analysis layer and a complete nine-profile reference to scope against; you
   write the event store and nothing else.** That is a line item, not a project.
   Written up as `P11`.
3. **Ask which Caliper *version* the contract names, in week one.**
   `caliper-ts` defaults to **v1.1**. The only **v1.2** implementation found is
   unlicensed. A 1.2 client is materially further from this shelf than a 1.1
   client, and no procurement document this KB has seen distinguishes them.
4. **Read the `LICENSE` file, not the sidebar.** `caliper-ts` is the row that
   closed this gap and **GitHub's sidebar does not name its licence** — it shows
   a bare "License" link, with `MIT License / Copyright (c) 2021 Imagine
   Learning` inside the file. 🔴 **A pass that reads only the sidebar records it
   as unlicensed and leaves the gap open, which is very likely what happened
   here.** This is the second instance in this base (with `wwrwbs/AI_AWE`) of a
   real permissive grant invisible to the sidebar.
5. **Moodle is the one platform with a sanctioned Caliper path, and GPL-3.0 is
   not a problem there.** A Moodle plugin lives inside a GPL-3.0 host and is
   expected to be GPL-3.0; it does not reach a separately deployed MIT/Apache
   agent layer. 🔵 **Say this explicitly in any engagement that has internalised
   this KB's "do not fork the LMS" rule** — the rule is about forking the
   platform, not about installing a plugin.
