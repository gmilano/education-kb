---
industry: education
region: Global
updated: 2026-11-13
---

# Education AI — current trends

**Thirty** trends, each with the evidence behind it and what it implies for an
engagement. 🟢 **Fifteenth pass (`p810`, 2026-11-13): `T27`–`T30` added.** 🔴 **This line said
"Twenty-five" while the file held `26` — the drift this very sentence warns about, uncorrected
through `p809`.** 🟢 **Re-derived here: `grep -c '^## T' intel/trends.md` = `30`.** The count
above was produced by `grep -c '^## T'` before being written, not carried forward.
🔵 **`T24` (the education agent long tail is numerous, atomised and unlicensed) came from
the first search leg in six passes to break the supply nil; `T25` (the same product
changes regulatory category by learner age, not by function) came from narrowing a claim
this file already carried about Korea.** 🔴 **The prescribed battery returned nil on
supply for a sixth pass and nil on regional facts for a third** — both new trends came
from differentiated legs, as every trend since `T19` now has.
🔵 **`T22` (a repository name is not an identifier) came from verifying a name this base
already carried, not from a search; `T23` (assessment is splitting into institutional
and workforce) came from the one genuine market event of the window — Pearson/Workera.**
🔴 **The prescribed battery returned nil on supply for a fifth pass and nil on regional
facts for a second.** 🟢 **Eleventh pass (`p806`, 2026-11-13): `T20` and `T21` added, and `T19`'s
headline claim narrowed** — the first open-licensed education AI-literacy curriculum
surfaced, but at `3★` it is a seed rather than a corpus. 🔵 **Neither new trend came
from the prescribed search battery, which returned nil on supply for a fourth pass and
nil on regional facts for the first time.** Both came from auditing this base's own
append-only trending logs against its shelves. Researched 2026-11-13. 🔴 **Tenth pass (`p805`, 2026-11-13):
no trend was added and none was retired — the four global and four regional legs
returned facts already carried here, the third consecutive nil.** 🟢 **One trend was
amended on new shelf evidence: `T7`, where two permissive student-information systems
and a third permissive platform row weaken the "platform layer is copyleft" claim for
the second time.** 🔵 **The amendment uses no component discovered this pass** — all
three were license-verified in earlier passes and had never reached a shelf file. 🔴 **The count in this line said "Eight" for
nine trends past the point it stopped being true; corrected at `p803`, and
re-counted at `p804` when `T18` and `T19` were added.**

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

🔴 **Revised, sixth pass (2026-11-13): this trend was overstated and the
correction is in `T15`.** **Six** of eight significant open-source LMSs are
GPL-3.0/AGPL-3.0; **two are permissive** — Sakai (ECL-2.0) and **OpenOLAT
(Apache-2.0)**. The "platform layer is copyleft" half of this trend is therefore
a strong tendency, not a law, and `T15` describes the exception and why it
matters more than its star count suggests. Permissive licensing in education
otherwise clusters in content,
modelling and now integration: Perseus (MIT), Kolibri (MIT), pyKT (MIT), Oppia
(Apache-2.0), nbgrader and JupyterHub (BSD-3-Clause), ODK Collect
(Apache-2.0), **ltijs (Apache-2.0)**, and the three largest agents — DeepTutor
(Apache-2.0), OpenMAIC (MIT), teacher-to-skills (Apache-2.0).

**Implication:** the standard education architecture is a permissive AI layer
mounted into a copyleft platform over LTI/MCP. One practical wrinkle found this
pass: **every verified LTI 1.3 library is Node, PHP or Elixir — none is
Python**, while nearly every agent in this KB is Python. Budget for a
two-process shape (Python agent behind a Node/PHP LTI front door).

🔴 **Revised again, tenth pass (`p805`, 2026-11-13) — the "platform layer is
copyleft" half weakens a second time, and this time it is the *student-record*
layer, not the LMS.** Until this pass every student-information and institutional-ERP
row in this base was copyleft: OpenEduCat (LGPL-3.0), Frappe Education (GPL-3.0),
RosarioSIS (GPL-2.0), Gibbon (GPL-3.0), openSIS (GPL), i-educar (GPL-2.0). **Two
permissive SIS trees are now shelved:**
[`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) (**MIT**, 56★, Laravel,
APAC) and [`SVWS-NRW/SVWS-Server`](https://github.com/SVWS-NRW/SVWS-Server)
(**BSD-3-Clause**, 42★, 10,015 commits, a German state government's own school
administration server, EMEA). A third permissive platform row,
[`elimu-ai/webapp`](https://github.com/elimu-ai/webapp) (**MIT**, 41★), joins the
LMS table.

🔵 **The revised statement:** permissive platform software in education exists at
**every** layer — LMS, SIS, content — but it is **consistently one to two orders of
magnitude smaller** than the copyleft incumbent beside it. OpenOLAT 451★ against
Moodle 7.6k; GegoK12 56★ against OpenEduCat 911★; SVWS-NRW 42★ against i-educar
725★. 🟢 **So the architectural rule is unchanged for an incumbent-replacement
engagement — integrate, do not derive — but it is now wrong as a blanket statement
about what a studio may fork.** When the deliverable must be a product the client
owns outright, there is a permissive tree at each layer; it is just small, and the
maintenance burden transfers to the studio. 🔴 **Both permissive SIS rows are under
60 stars: verify maintenance before committing a client.**

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

## T15 — The sovereign-AI path in education is an LMS feature, not an agent — and it is Apache-2.0

**This is the correction to `T7`, and the most consequential finding of the
sixth pass.** Every pattern in this KB before now assumed the same shape: a
permissive AI layer mounted into a copyleft platform over LTI 1.3 or MCP,
because the platform itself could never be permissive and never shipped AI worth
using. **OpenOLAT is a counterexample on both counts**, and it was missed for
four passes for a mechanical reason worth naming (see `repos/foundations.md`):
its GitHub sidebar names no license, so every license-field read classified it
as unknown rather than opening the `LICENSE` file, which says *"Apache License /
Version 2.0, January 2004"*.

**What is actually in the tree** — verified by reading the repository, not the
release notes:

| Layer | Path / symbol | What it means |
|---|---|---|
| Provider SPI | `AiSPI`, `AiEmbeddingSPI`, `AiApiKeySPI` | AI providers are pluggable by contract, not hard-wired |
| Providers | `spi/anthropic`, `spi/generic`, `spi/localonnx`, `spi/openAI` | `generic` = **any OpenAI-compatible endpoint**, i.e. a self-hosted vLLM or Ollama |
| Local inference | `spi/localonnx/LocalOnnxSPI.java`, `QwenOnnxEmbeddingModel.java` | **In-process ONNX runtime** — some AI runs with no outbound call at all |
| Features | `AiFeature`: `mc-question-generator`, `image-description-generator`, `essay-generation`, `essay-grading`, `taxonomy-matching` | Five declared features, not a chatbot bolt-on |
| Learner control | `AiFeature.isUserControlled()` — *"a person can switch this feature on or off in the user settings, on top of the system default of the administrator"* | Per-learner opt-out **in the data model** |
| Cost/audit | `AiUsageLog`, `AiUsageLogStatus`, `AiUsageLogSearchParams` | Per-call accounting — the artifact an EMEA procurement asks for |

**The precise claim, and its limit.** 🔴 **Do not oversell `localonnx`.** The
only model class under it is `QwenOnnxEmbeddingModel` — an **embedding** model.
So the fully-local path today covers embeddings and the retrieval/taxonomy side,
while `essay-grading` and `mc-question-generator` still call out through a
provider. **The sovereign answer is therefore `generic` pointed at a
self-hosted OpenAI-compatible endpoint, with `localonnx` handling embeddings
in-process** — not "it all runs locally." That distinction is the difference
between a proposal that survives a data-protection review and one that does not.

**Why this matters more than 451 stars suggests.** Star count measures developer
attention; this KB's job is to measure *what a studio can hand a client*. An
Apache-2.0 LMS with per-learner AI opt-out in the data model, per-call cost
logging, and a provider slot that accepts a self-hosted endpoint is a direct
answer to the EU AI Act deployer obligations in `intel/market.md` (Article 50
transparency, applying 2 August 2026; human oversight and logging; Article 27
FRIA for public bodies). Nothing else in this KB answers all of those from
inside the platform.

**What this does not change.** For Moodle, Canvas and Open edX incumbents —
which is most of the installed base — the LTI/MCP mounting rule in `T7` is
unchanged and remains the default. `T15` applies when the platform is
greenfield, the client is in German-speaking EMEA, or sovereignty is a stated
requirement. 🔵 **The open question for the next pass:** whether OpenOLAT's AI
features are reachable over an API for an external agent, or only from the
platform UI. Nothing in the paths read this pass settles it, and it decides
whether `P13` can be combined with the agent patterns in this file.

## T16 — Every education-AI regime now imposes duties on a deployment inventory that nobody has built

**Established `p802` (seventh pass, 2026-11-13).**

Four regimes on three continents converged this pass on the same unstated premise, and one of them
finally names it.

- 🟢 **The Philippines wrote it down.** DepEd **Order No. `003`, s. `2026`** (2026-02-20) creates an
  **AI registry of all deployments** in basic education and **sorts tools into risk tiers**, with
  stricter treatment of **grading and admissions**.
- 🔴 **Everyone else assumes it.** The EU AI Act's **Article 27 Fundamental Rights Impact
  Assessment** requires a public deployer to assess *the high-risk systems it deploys* — which
  presupposes knowing what they are. **Oklahoma** requires **teacher review of AI output** and
  **parent opt-out** — both unenforceable without an inventory of what is running and for whom.
  **Vietnam** makes high-risk status contingent on whether a system's output is **the sole basis for
  a decision** — a per-deployment property, not a per-product one. The **NEU** figure that `49%` of
  UK schools have **no AI policy at all** is the same hole measured from the other side.
- 🔵 **So the gap is not policy and it is not product — it is the register in between.** This base
  has repeatedly found the governance deficit measured as *missing documents* (`26%` formal strategy
  in LATAM, `30%` published policies, `49%` of UK schools with none). A document cannot be written
  about systems nobody has enumerated, which is why **training and appraisal capability**, not
  policy templates, is what `p799` found actually binding.

**Why this is a trend and not an observation:** the registry is the **first deliverable that is
simultaneously compliant in all four regimes** and does not depend on which way the contested EU
high-risk date resolves. It is also cheap, it is the natural first engagement artifact, and it
produces exactly the inventory that every later pattern in `compose/patterns.md` needs as input.

🔴 **The honest limit:** no open-source implementation of an education AI deployment registry was
found in this pass. It is a **build**, not an adoption — which is unusual for this KB and is stated
plainly rather than filled with a near-match. See `P14`.


## T17 — Education AI now has benchmarks for whether a tutor teaches, and almost none of them carry a software grant

**This is the gap that has survived the longest in this KB, and `p803` is the
pass that establishes it is structural rather than accidental.** The field has
answered the measurement question — there are now credible, peer-reviewed
instruments for *pedagogical* quality, not just answer accuracy. It has not
answered the licensing question, and a studio cannot ship an instrument it has
no grant to.

**The evidence, every row payload-verified on the clone channel:**

| Repo | Size | Grant, established on bytes | Shippable |
|---|---|---|---|
| [`eth-lre/mathtutorbench`](https://github.com/eth-lre/mathtutorbench) | `48★` / `14` forks · `HEAD` `6faed173ec2b` | 🔴 **No licence file anywhere in the root tree (13 entries).** The README asserts a grant **twice and inconsistently**: a badge reading **CC BY 4.0** (line 3) and a footer reading **CC BY-SA 4.0** (line 199) | 🔴 **No** |
| [`kixlab/TutorCaseBench`](https://github.com/kixlab/TutorCaseBench) | `0★` / `0` forks · `HEAD` `6b9ac34262c7` | 🔴 **No licence file (11 root entries) and no licence line in the README at all.** KAIST KIXLAB; `923` dialogues; arXiv `2610.30828` | 🔴 **No** |
| [`kaushal0494/AITutor-EvalKit`](https://github.com/kaushal0494/AITutor-EvalKit) | `4★` | 🔴 **No grant in the root tree**, reproduced at `HEAD` `a71078456a90` across `p801`, `p802` and carried here. The `EACL 2026` paper's "MIT-licensed" claim is refuted on bytes | 🔴 **No** |
| [`Kobby-Adjei/ai-tutor-benchmark`](https://github.com/Kobby-Adjei/ai-tutor-benchmark) | `0★` / `0` forks · `HEAD` `23fc97462c8f` | 🟢 **MIT, payload-verified** — root `LICENSE`, `1,351 B`, `sha256:f32797392bf180dc…`, `affero×0`, title `MIT License`. README §Licence **splits the grant correctly**: MIT for code, CC BY 4.0 for paper, learner cards and data | 🟢 **Yes — and it is the only one** |

Add `p694`'s earlier sweep (four of five in the cluster ungranted, including
`kaushal0494/UnifyingAITutorEvaluation` at `34★` and `bigdata-ustc/Agent4Edu` at
`101★`, **AAAI**) and the shape is unambiguous.

**🔵 `mathtutorbench` is the important correction, and it sharpens `p694` rather
than repeating it.** This base previously recorded it as *"ships no licence at
all."* That is true of the **tree** and false of the **repository**: it asserts a
grant twice, and the two assertions **disagree on ShareAlike** — the single
clause that decides whether derived evaluation code must be published. A studio
reading the badge concludes it has no reciprocal obligation; a studio reading the
footer concludes it does. 🔴 **An ambiguous grant is worse than an absent one,
because an absent one cannot be misread as permission.** Both readings are also
**Creative Commons licences applied to software**, which CC itself advises
against.

**Why this is a trend and not a complaint.** Three forces are converging and
they explain the pattern:

- 🔵 **These artifacts are paper deliverables, not products.** The grant follows
  academic convention — CC, for a *dataset* — because the repository exists to
  make a paper reproducible. The code is incidental to the author and load-bearing
  for anyone else.
- 🔴 **Meanwhile the regimes are starting to require exactly this evidence.** The
  EU AI Act puts assessment AI in Annex III; Vietnam names automated assessment
  high-risk; Oklahoma requires teacher review of AI output. Each presupposes a
  defensible answer to *does this system teach, and how do you know*. **The
  instrument that answers it is the one nobody can ship.**
- 🟢 **The correct pattern exists and costs nothing to copy.**
  `Kobby-Adjei/ai-tutor-benchmark` — a `0★` solo project — does what four
  institutional repositories do not: **separate the code grant from the data
  grant and state both.** MIT on the harness, CC BY 4.0 on the learner cards.

**What this means for an engagement.** 🔴 **Do not plan on adopting a published
education benchmark**; plan on **building the harness and borrowing the
methodology**, which carries no licence at all and is free to read.
`mathtutorbench`'s task decomposition and `TutorCaseBench`'s rubric structure are
both readable and both describable in a paper citation. 🟢 The one adoptable
asset is the `ai-tutor-benchmark` *shape* — three stages, simulated learners,
split grant — at `0★`, so it is **a template, not a dependency**. See `P15`.

🔴 **Deliberately not promoted to a shelf row.** `ai-tutor-benchmark` is MIT and
build-safe, but `0★` / `0` forks does not meet this KB's bar that *"a row implies
a studio could start from this."* It is recorded here and in `agents/trending.md`
and nowhere else, which is the same treatment `Manu` and `EDUKAI LongView` got.

## T18 — In US higher education the binding instrument is the system's own policy, with a date on it

This base concluded three passes ago that American higher education is being
governed "through institutions rather than statute." `p804` found the named
instance, and it carries a deadline inside this quarter.

**The evidence.** SUNY's Board of Trustees adopted a **systemwide AI policy on
April 30, 2026**. It covers the system's **64 campuses**. Campuses "shall publish
AI policies and/or update relevant existing policies **no later than December 31,
2026**." AI was folded into the **Information Literacy** core competency of the
general-education framework from **Fall 2026**, adding no extra credits. Support
runs through the **AI for the Public Good Fellows**: an inaugural cohort of **20**,
then **11** more focused on discipline-specific integration. Meanwhile the federal
layer is still empty — the **K-12 AI Literacy and Readiness Act of 2026** advanced
out of committee without passing, and the only new federal lever is the Department
of Education's **accreditation rulemaking** touching AI-related research misconduct.

🔴 **Provenance: search-tier.** `suny.edu` is unreachable from the session that ran
this pass; re-verification is tracked as `ACTION p804-V`. 🔴 **Two contradictions
kept rather than resolved:** one source dates the Information Literacy revision to
**December 2024**, and several outlets describe a **standalone AI course
requirement** that SUNY's own materials do not describe.

**What it implies for an engagement.** 🔵 **A statute creates a market slowly and a
system policy creates one on a date.** 64 institutions must each produce a published
AI policy within 48 days of this pass, supported by 31 fellows in total. The work is
not writing 64 policies — it is giving 64 campuses the same defensible artifact, and
the part none of them can produce from a template is **an accurate inventory of what
their campus actually runs**. 🟢 **That is `T16` and `P14` arriving on a calendar.**
🔴 **Do not pitch the standalone-course reading: it is the contested one and the
expensive one.** Pitch AI inside an existing competency — cheaper to build, and it
is what the policy actually says.

## T19 — Three regimes now require AI literacy; the open curriculum to teach it is a seed, not a corpus

🟡 **Status changed at the eleventh pass (`p806`): this trend's headline claim — "no
open curriculum exists" — is NARROWED and the title above is rewritten accordingly.**
The first *education* AI-literacy curriculum under an open grant did surface:
[`Emerging-Rule/community`](https://github.com/Emerging-Rule/community), **CC BY 4.0**,
bilingual **English / Spanish**, grades K-2 through 9-12, across Math, ELA, Science,
SEL/Digital Citizenship and CS/AI Literacy. 🟢 **CC BY 4.0 is attribution-only — no
share-alike — so unlike `GarethManning/education-agent-skills` (CC BY-SA 4.0, rejected
at `p802`) its lessons can be cut down and shipped inside a client deliverable.**

🔴 **But the trend survives, because the gap was never "does any open lesson exist"; it
was "can open material meet a national mandate."** At **`3★`, `1` fork, `20` commits**,
a badge claiming `13` lessons against a README table listing `6`, three showcase packs
still marked draft-and-not-piloted, **no licence field on the GitHub sidebar at all**
(the grant is README-and-badge provenance only) and **no Portuguese**, this does not
meet Australia's million-student rollout, SUNY's gen-ed competency or Article 4. 🔵
**Read it as proof the category has started, and as a contribution target: a studio that
adds a graded, piloted K-12 sequence to a CC BY 4.0 repository with `20` commits owns
the reference corpus in a field that has three dated mandates and no incumbent.**

🔴 **Two stronger candidates could not be verified and are therefore NOT shelved:**
**Day of AI** (MIT RAISE, K-12, advertises Creative Commons licensing) and the **OER
Commons** AI-literacy collections (licences vary per item; at least one is CC BY-NC-SA,
which would be unusable commercially). 🔴 **`dayofai.org`, `www.dayofai.net` and
`oercommons.org` were all refused by this session's egress proxy.** An informed gap:
the next pass has named targets rather than a query.

### The original finding, which still holds on the scale question


**The evidence, assembled across three regions in one pass.** North America: SUNY
folds AI into the gen-ed **Information Literacy** competency from Fall 2026. EMEA:
**EU AI Act Article 4** binds **providers and deployers** to support AI literacy
among staff — in force now, and 🔴 **specifying no required level for any person**,
which makes it the one AI Act duty with no objective compliance test. APAC:
Australia's **national AI-literacy curriculum** is rolling out through public,
independent and Catholic schools (Code for Schools, AWS support), targeting
**1 million students within three years**.

🔴 **And the supply side is empty where it counts.** The largest permissively
licensed curricula found anywhere this pass are
[`rohitg00/ai-engineering-from-scratch`](https://github.com/rohitg00/ai-engineering-from-scratch)
(**MIT**, `78.6k★`, `14.0k` forks) and
[`patchy631/ai-engineering-hub`](https://github.com/patchy631/ai-engineering-hub)
(**MIT**, `41.8k★`, **93+ projects graded `22`/`48`/`23` across three difficulty
tiers**). 🔵 **Both are larger than every education-specific repository in this base
— only `DeepTutor` at `58.7k` is in range — and neither teaches AI literacy to a
student. They teach AI engineering to a developer.** National programme materials
are not published under an open grant, and vendor courseware is not redistributable.

**What it implies for an engagement.** 🟢 **This is the clearest unserved content gap
in this base, and unusually it has three dated mandates pointing at it rather than a
forecast.** The buildable move is not to write a curriculum from nothing: it is to
**re-level** the MIT corpora — take `ai-engineering-hub`'s difficulty grading as the
sequence, cut the developer assumptions, and emit the result through the layers this
base already verified (`qti3` for items, `pylti1.3`/`ltijs` to mount it,
`learnmcp-xapi` to make completion reportable). 🔴 **The grant is what makes this
viable: MIT permits redistribution and modification of the content itself, which no
vendor courseware does.** Tracked as `Gap 804-C` in `repos/foundations.md`.


## T20 — Student-facing LMS agents have converged on preview-then-confirm writes, independently, in three jurisdictions

**The evidence, and the reason it counts: nobody coordinated it.** Three MCP servers
verified this pass were written by unrelated authors, against three different host
platforms, in three regulatory regimes — and all three solve the write problem the same
way or refuse it outright.

| Repo | Jurisdiction | Host system | How writes are handled |
|---|---|---|---|
| [`PsychQuant/che-ntucool-mcp`](https://github.com/PsychQuant/che-ntucool-mcp) (MIT) | 🇹🇼 Taiwan | NTU COOL (Canvas) | 🟢 **Two layers:** an MCP **elicitation dialog** *plus* a **single-use token bound to the previewed payload**. `preview_grade_change` → `post_grades`; `preview_announcement` → `post_announcement` |
| [`12dora/waseda-moodle-mcp`](https://github.com/12dora/waseda-moodle-mcp) (MIT) | 🇯🇵 Japan | Waseda Moodle | 🟢 **Nine `prepare_*` verbs, one `confirm_action`, one `cancel_action`.** `20` read tools, `11` write tools, every mutation split |
| [`maurodruwel/Smartschool-MCP`](https://github.com/maurodruwel/Smartschool-MCP) (MIT) | 🇧🇪 Belgium | Smartschool | 🟢 **Refuses the problem: `15` tools, all of them `get_` or `download_`, no write path at all** |

🔵 **Convergent design across unrelated authors is a much stronger signal than any one
repository's star count**, and it is why three repos with `1`, `0` and `6` stars earn
rows in `agents/top.md`. It says the constraint is real and intrinsic to the domain:
**an agent that can silently change a grade is not deployable in a school**, and
everyone who builds one discovers this.

🟢 **It also supersedes a claim this base made two passes ago.** `p802` recorded
`zavora-ai/mcp-education` as "the only server that gates writes in its own tool
contract." **That is withdrawn: it is now one of at least four, and `che-ntucool-mcp`'s
gate is stronger than it.**

**What it implies for an engagement.** 🟢 **The human-oversight argument for an LMS
agent no longer has to be invented or defended from first principles.** EU AI Act Art.
`14` requires that high-risk systems be effectively overseen by natural persons; a
studio can now point at **three independent MIT implementations of a preview-then-confirm
protocol** and adopt one rather than design one. 🔵 **Make the posture an explicit
deliverable and price it as three tiers** — read-only (cheapest, and the easiest thing
to put in front of a European DPO), preview-then-confirm (the default), and
token-bound-to-payload (where grades or records are at stake). 🔴 **The tier is a
procurement decision, not an engineering detail: pick it in week one, because retrofitting
a write gate onto a deployed agent means rewriting its entire tool surface.**

🟢 **Extension (`p809`, 2026-11-13) — the cleanest natural experiment this base has found
for `T20`, because the two implementations are otherwise identical.**
[`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server)
(`MIT`, `67★`) and [`JhostinAleck/brightspace-mcp`](https://github.com/JhostinAleck/brightspace-mcp)
(`MIT`, `16★`) target **the same LMS** and expose **exactly `29` tools each** — and they
take opposite decisions on writes:

- 🔴 **`RohanMuppa` refuses writes outright**: *"It only reads your courses. It never
  submits, edits, or deletes anything."*
- 🟢 **`JhostinAleck` permits three** (`submit_assignment`, `post_discussion_reply`,
  `mark_announcement_read`) behind **two independent opt-ins** (`writes.enabled: true`
  in config **and** `--enable-writes` on `serve`), plus a **`dry_run`** preview, a
  **client-supplied idempotency key** per write, and a **warning-level audit-log entry**
  per write.

🔵 **`JhostinAleck`'s gate is now the strongest in this base**, ahead of
`che-ntucool-mcp`'s `prepare_* → confirm_action`, because it adds *idempotency* and an
*audit trail* rather than only a confirmation step — i.e. it is designed for a system
that will be asked what happened, not just whether the user agreed.

🔴 **`submit_assignment` is the live wire.** An agent that can submit coursework turns
academic integrity into a config flag. 🟢 **The reusable conclusion: in education the
write gate is not an implementation detail, it is the product decision**, and the fact
that two independent authors on the same platform landed on opposite sides of it in the
same window is the evidence. Convergence on *preview-then-confirm* is real; convergence
on *what may be written at all* is not.

## T21 — In North America the integration surface is the state data standard, not the LMS — and this base scoped eleven passes at the wrong altitude

**The evidence.** US K-12 student data does not move school-by-school. It moves through
**Ed-Fi**, the interoperability model that state education agencies run their reporting
on, with two **Apache-2.0** reference implementations:
[`Ed-Fi-Alliance-OSS/Ed-Fi-ODS`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS)
(v7.x, `28★` / **`48` forks**) and
[`Ed-Fi-Alliance-OSS/Data-Management-Service`](https://github.com/Ed-Fi-Alliance-OSS/Data-Management-Service)
(v8, `12★` / **`17` forks**).

🔵 **Read the fork-to-star ratio, not the star count.** Both repositories are forked
substantially more often than they are starred — the inverse of a trending repository's
shape. 🟢 **A repo forked more than starred is being deployed rather than admired**, and
judging Ed-Fi's `28★` against a `40k★` tutorial corpus is a category error that this
base made by omission for eleven passes.

🔴 **The omission is the trend's second half, and it is about method.** Every pattern in
this KB that touches a student record reaches it through an **LMS** (Moodle, Canvas,
Open edX) or through **one institution's SIS** (RosarioSIS, Gibbon, OpenEduCat, EduPage,
HEMIS, Smartschool). **Ed-Fi was mentioned `249` times in this base's own append-only
trending logs and `0` times in any file a studio reads.** The search battery never
surfaced it because the battery asks for *agents*, *trending repos* and *platforms* —
and a data standard with `28★` is none of those.

**What it implies for an engagement.** 🟢 **It is a change of altitude with a direct
revenue consequence. An agent that speaks one SIS sells to one district; an agent that
speaks Ed-Fi sells to a state education agency.** The dated district-policy deadlines
this base already tracks — North Carolina's `2027-06-30`, Ohio's `2026-07-01` — are
**state-level procurement events**, and a state-level integration is positioned for them
while a district-level one is not. 🔴 **No Ed-Fi agent interface exists anywhere
(`Gap 806-A`): it is a build and must be priced as one** — but every ingredient is on a
shelf, including three write-gating designs from `T20`, and a write path into a **state
longitudinal data system** is the highest-consequence write surface in this entire
knowledge base.

🔵 **The generalisable method, which is the part worth carrying to other industries:
when a vertical has a mandatory reporting standard, the standard is the integration
surface, and it will never appear in a "trending AI repos" search.** This base learned
the adjacent lesson at `T13` — *when a vertical system has no agent surface, check the
general-purpose platform underneath it.* **`T21` is the same move one layer further
down: check the regulator's data model.**


## T22 — A repository NAME is not an identifier, and in this space the collision is licence-shaped

**Evidence.** 🟢 **Measured directly this pass (`p807`, 2026-11-13).** The name
`LearnHarness` resolves to **at least three distinct GitHub repositories** with three
different licence positions:
[`amosblomqvist/learnharness`](https://github.com/amosblomqvist/learnharness) —
`9.1k★`, `1,202` commits, **AGPL-3.0 byte-verified** (`LICENSE`, `34,523 B`,
`sha256:0d96a4ff68ad6d4b…`);
[`h4ksclaw/learnharness`](https://github.com/h4ksclaw/learnharness) — `3★`, `52`
commits, **no `LICENSE` file at all** (`404` from `raw.githubusercontent.com` on
`LICENSE` *and* `LICENSE.md`, on *both* `main` and `master`) behind a README whose
`## License` section contains the bare word `MIT`; and the two `0★` forks already
recorded at `T966`, which serve a byte-identical AGPL-3.0 payload under an **empty**
sidebar. 🔴 **`h4ksclaw` is not a fork** — no "forked from" line, disjoint history,
different description, different purpose.

**Why it is a trend and not an anecdote.** 🔵 **This base has now hit the same class of
defect four times by four different mechanisms**: `NOASSERTION` from a classifier
defeated by an SPDX comment and curly quotes (`GegoK12`); a licence stated only in a
German README (`SVWS-NRW`); two halves of one vendor's stack under *different* copyleft
grants (`frappe/education` GPL-3.0 vs `frappe/lms` AGPL-3.0); and now **a name that
resolves to repositories whose grants disagree.** 🟢 **The common factor is that the
cheap, fast way to answer "what licence is this?" — read the sidebar, or search the name
— fails in a different way each time, and in education specifically it fails often**,
because the space is full of small single-author projects that copy a well-known
project's name.

🔴 **The directional hazard is what makes this expensive.** In every one of the four
cases, the **wrong** answer is the **more permissive** one. A studio that stops at the
name here concludes `MIT` on a `3★` repository and ships; the `9.1k★` project it
probably meant is AGPL-3.0, and the `3★` one has **no grant at all**, which is
all-rights-reserved by default — 🔵 **strictly worse than the AGPL it was mistaken for.**

**What it implies for an engagement.** 🟢 **Three rules, all cheap:**
1. **Resolve every component by `owner/repo`, never by product name** — and record the
   slug in the deliverable, not the name.
2. **Treat a licence named only in prose as unverified.** A `## License` heading reading
   `MIT` with no grant file is a statement of intent. 🔵 **`raw.githubusercontent.com`
   settles it in one request, and a `404` across `main` and `master` is a positive
   finding, not a failed check.**
3. **An empty GitHub licence sidebar carries no information in either direction**
   (`T966`) — it means the classifier declined, which happens both to repositories with
   a perfectly good bespoke-formatted grant *and* to repositories with none.

🔵 **Generalisable beyond education:** any industry KB assembling a component shelf from
search results inherits this, and the cost is asymmetric — a missed copyleft obligation
surfaces at client due-diligence, not at build time.


## T23 — The money in AI-era assessment is moving from "did the student learn the course" to "can this person do the task", and the two have almost no architecture in common

**Evidence.** 🟢 **[Pearson agreed to acquire Workera](https://www.reworked.co/learning-development/pearson-acquires-ai-skills-verification-platform-workera/),
announced `2026-09-29`, terms undisclosed, completion expected H2 `2026`.** Workera goes
into Pearson's **Enterprise Learning & Skills** unit; founder-CEO Kian Katanforoosh joins
its leadership. 🔵 **The product is the signal:** agentic AI + psychometrics + adaptive
assessment measuring proficiency through **role-specific scenarios and simulations**,
with reported customers **ServiceNow, Accenture and the US Space Force** — 🔴 **not one
of which is a school.** 🟢 Corroborating from the same window: the EMEA leg returned
**Instructure building an AI study coach into Canvas**, i.e. the incumbent LMS moving on
*instructional* assessment while the publisher buys *workforce* verification.

**Why it is a trend.** 🔴 **A company with Pearson's assessment franchise paying for an
AI-native verification capability is a statement that its existing psychometric stack
does not measure what buyers now want measured.** 🔵 The unit of assessment is shifting
from the **course** (did you pass it) to the **task** (can you do it), and simulation is
the mechanism.

**What it implies for an engagement.** 🟢 **There are two offers here, not one, and this
base had been describing them as one.**

| | **(a) Institutional assessment** | **(b) Skills verification** |
|---|---|---|
| Buyer | Registrar, faculty, assessment office | HR, L&D, enterprise capability |
| Regulatory load | 🔴 **High** — EU AI Act Annex III names assessment high-risk (obligations `2027-12-02`); US state integrity rules | 🟢 **Low** — largely unregulated |
| Core architecture | LMS/LTI integration, rubric, audit trail, human-in-the-loop | Simulation environment, scenario authoring, credential format |
| Shelf support here | `Moodle`/`Canvas`/`Open edX` + QTI rows + `T17` tutor benchmarks | `CredentialEngine/osmt`, `CredentialRegistry`, `tabiya-tech/compass` |
| Sales cycle | Institutional, slow, procurement-gated | Enterprise, faster, budget already exists |

🔴 **They share almost no architecture, and conflating them is how an education-shaped
proposal loses an L&D deal.** 🟢 **Consequence for this base's own shelves: the
credential-layer rows have been filed as education supply and are better read as
*workforce* supply** — they serve (b), where the acquisition money is going, and they
are the part of this knowledge base that a Globant enterprise engagement can use without
touching a school at all.

🟡 **Dating caveat.** One outlet dates the announcement `2026-10-05`; the Pearson release
and the majority of coverage give `2026-09-29`, which is what is asserted.

## T24 — Education's agent supply is numerous, atomised and frequently unlicensed; the adopt-vs-build calculus is therefore inverted

🟢 **Evidence, gathered in one window (`p808`, 2026-11-13).** A single search leg aimed at
the *LMS seam* rather than at the *education domain* returned **seven** education-specific
agents that five prior passes had missed:
[`canvas-pilot`](https://github.com/X-isdoingreat/canvas-pilot) (`AGPL-3.0`, `125★`),
[`interactive-learning`](https://github.com/geekjourneyx/interactive-learning) (`MIT`, `52★`),
[`AI-Grading-Tool`](https://github.com/end13s/AI-Grading-Tool) (**no licence**, `0★`),
[`mini-homework-agent`](https://github.com/chaoyuhao/mini-homework-agent) (`MIT`, `0★`),
[`canvas-ai-agent`](https://github.com/jans-johnson/canvas-ai-agent) (`MIT`, `0★`),
[`opencode-class-agents`](https://github.com/DTA-Projects/opencode-class-agents) (`MIT`, `0★`),
[`Canvas-grading-with-AI`](https://github.com/jlouisbru/Canvas-grading-with-AI) (`MIT`, `0★`).
🔴 **Median star count: `0`. Modal contributor count: `1`. Three of the seven carry no
usable grant or a network-copyleft one.** All figures read from rendered repository
sidebars, not roundups.

🔵 **The finding is not "there are few education agents" — it is the opposite.** There
are many; they are simply invisible to every ranking mechanism, because GitHub Trending
and "top repos" roundups both sort by star velocity and a population with a median of
zero generates none. 🟢 **Five consecutive passes of "nil on supply" in this base were a
measurement artefact, not a market fact.**

🟢 **Why it is this way.** An education agent is usually written by one instructor to
solve one course's grading or tutoring problem against one institution's LMS. It works,
it is published, and it stops — because its author's need is met. 🔵 **There is no
user base to accumulate**, since the next instructor's rubric, LMS tenant and
institutional policy differ enough that forking is as much work as rewriting. This also
explains the licence pattern: **a researcher publishing a course tool does not think
about grants**, which is how this base has accumulated four substantial unlicensed
education repositories (`llamatutor` at `2.1k★`, `AITutor-EvalKit`, `educational-agents`,
`AI-Grading-Tool`).

🟢 **What it implies for an engagement — the operative part.** In most verticals the
adopt-vs-build question is *which mature project do we fork*. 🔴 **In education that
question has no good answer at the workflow layer, and a studio that goes looking for one
will burn a sprint discovering it.** 🟢 **The correct shape is: adopt the CONNECTOR,
build the WORKFLOW.** The connector layer genuinely has traction and permissive
licences — `canvas-mcp` (`MIT`, `324★`), `Moodle-MCP` (`MIT`, `206★`),
`mcp-odoo` (`MIT`, `433★`), `learnmcp-xapi` — because a connector's value *does*
accumulate across institutions. 🔵 **The grading or tutoring loop on top should be
written, not adopted**, and the `0★` repositories above should be read as **design
references** for that loop rather than as dependencies. `P22` is this recipe made
concrete.

🟢 **A second, cheaper implication: always check the grant before the stars.** The most
functionally complete Moodle grader found this window (`AI-Grading-Tool`, `134` commits)
is unusable, and the highest-starred new agent (`canvas-pilot`, `125★`) is AGPL-3.0 with
`1` commit. 🔴 **Neither fact is visible from a search result snippet** — both required
reading the repository page.

## T25 — The same education product changes regulatory category by the LEARNER'S AGE, not by what the software does

🟢 **Evidence (`p808`, 2026-11-13).** South Korea's **AI Basic Act** (in force
`2026-01-22`) reaches education through a clause covering **student assessment in
early-childhood, primary and lower-secondary education**. 🔴 **It does not reach higher
education or corporate training.** The EU AI Act's **Annex III**, by contrast, covers
admissions, examination and evaluation across education *and vocational training* — all
levels — with those duties applying from **`2027-12-02`** after the Digital/AI Omnibus
delay. 🔵 **Vietnam** (binding law, commencement `2026-03-01`) places education in its
high-risk category with pre-deployment registration; **Taiwan's** framework AI Basic Act
names education but imposes no education-specific duties at all.

🟢 **So four jurisdictions take four different cuts at the same vertical**, and the axis
that separates them is **not function**. An automated essay grader is: high-impact in
Korea if the learners are `9` and out of scope if they are `19`; high-risk in the EU in
both cases; registrable in Vietnam; unregulated in Taiwan.

🔵 **Why this is a trend and not merely a compliance note.** Through 2025 the working
assumption across this base was that AI regulation would converge on a risk-based model
with education as a named high-risk sector — the EU template. 🔴 **2026's instruments
have diverged instead**, and they diverge on *scope definitions* rather than on duties:
the duties (risk management, human oversight, notification, impact assessment) are
strikingly similar everywhere, while **who is covered** is drawn differently in each
statute.

🟢 **Engagement consequence.** A multi-region education product needs **one control set
and several scope memos**, not several control sets. 🔵 **Build the conformity artefacts
once** — impact assessment, human-oversight design, notification surface, model and data
documentation — because every regime wants roughly the same evidence. 🔴 **Then decide
per jurisdiction whether they are mandatory**, and record that decision, because in Korea
classification is an operator **self-assessment** (MSIT confirmation is optional) and the
exposure for getting it wrong sits with the client. 🟢 **A proposal that says "education
is high-risk, here is our compliance package" is wrong in Korea for higher ed, wrong in
Taiwan everywhere, and over-priced in both.**

🔴 **Status: search-tier.** Primary statutory texts could not be reached this window —
`cset.georgetown.edu`, `digital-strategy.ec.europa.eu` and the other issuing hosts do not
resolve under this session's network policy. The Korean scope clause is corroborated
across several independent translations that agree on substance; `ACTION p808-A` tracks
confirmation against the statute.

## T26 — When this base names a platform often and shelves nothing for it, that is a search instruction, not a market fact

🟢 **Evidence (`p809`, 2026-11-13).** This KB had written **`Brightspace` `171` times**
and **`Blackboard` `159` times** across its own files, and carried **zero** agent rows
for either — the only shelf mention was a note that LTI 1.3 libraries mount into them.
🔴 **Both are served.** One pass of seam-named queries returned **five** shelf-ready
agents: two independent `MIT` Brightspace servers (the larger at `67★`, `492` commits)
and three Blackboard clients (`ISC` `13★` with `851` commits; `MIT` `4★`; `MIT` `1★`).

🔵 **This is the second confirmed instance of the shape, which is what promotes it from
accident to rule.** The eleventh pass (`p806`-era) found the **US state data standard**
mentioned `249` times in these logs and shelved `0` times. Same signature: heavy prose
presence, zero shelf presence, supply available on the first page of a correctly aimed
query.

🟢 **The mechanism.** A platform earns prose mentions because it is an *incumbent* — it
keeps appearing in market and regulatory analysis. It earns zero shelf rows because the
discovery legs are aimed at the **domain** (`education`), and domain queries return
general-purpose frameworks. **Incumbency and discoverability are driven by different
things, so they drift apart, and the drift is invisible from inside either file.**

🟢 **The operational rule, cheap to run every pass:**

```sh
for name in Brightspace Blackboard PowerSchool Schoology "Infinite Campus" Skyward Banner Workday; do
  prose=$(grep -rioc "$name" intel/ compose/ | awk -F: '{s+=$2} END{print s}')
  shelf=$(grep -ric "$name" agents/top.md repos/foundations.md verticals/solutions.md | awk -F: '{s+=$2} END{print s}')
  echo "$name prose=$prose shelf=$shelf"
done
```

🔴 **Any name with a high `prose` and a `shelf` of `0` is an unrun search, and should be
queried by SEAM before the next pass claims a gap.** Remaining candidates with that
signature right now: `PowerSchool` (`53` prose mentions, `0` shelf rows), `Schoology`,
`Infinite Campus`, `Skyward`.

🔵 **The limit of the rule, stated so it is not over-applied.** It generates leads, not
findings. The same pass that closed Brightspace and Blackboard ran the identical
transform on **Ellucian Banner, Ellucian Colleague and Workday Student** and returned
**nothing** — those gaps are real (see `agents/top.md` → Declared gaps). 🟢 **The rule
tells you which gaps have not been tested, not which gaps are false.**

## T27 — A licence field that is wrong in BOTH directions is not a weak signal, it is a non-signal: `NOASSERTION` obliges a byte read before shelving AND before rejecting

**Evidence, `p810`, two repositories, same hour, opposite outcomes.** Both carried GitHub
`license.spdx_id` = `NOASSERTION`:

| Repo | ★ | LICENSE bytes | Truth |
|---|---|---|---|
| [`webworn/openfoam-mcp-server`](https://github.com/webworn/openfoam-mcp-server) | `129` | blob `be1f2caa61c7`, `10,708 B`, `APPENDIX` present, no added clause, `shall not` hits are stock Apache §1/§9 | 🟢 **Unmodified Apache-2.0 — BUILD-SAFE** |
| [`affromero/Sotto`](https://github.com/affromero/Sotto) | `35` | blob `1a71cb643975`, `4,563 B`, *"Any noncommercial purpose is a permitted purpose"* | 🔴 **PolyForm Noncommercial 1.0.0 — COMMERCIALLY PROHIBITED** |

🔴 **Trusting the field would have rejected a usable `129★` repository and shipped an
unusable `35★` one, in the same pass.** 🔴 **`Sotto` calls itself "open source" in its own
repository description** — the self-description was wrong and the bytes were right.

🔵 **Why `openfoam` defeats the classifier is the mechanism, and it generalises:** its Apache
text is `10,708 B` against the Ed-Fi Apache's `11,558 B` — a **whitespace/formatting**
divergence that changes no term. 🔵 **A licence classifier is a string matcher, and whitespace
is a string.**

🟢 **What this corrects in this base's own practice.** Prior passes treated a blank or absent
licence signal as presumptive grounds for the REJECTED table (`p809` rejected
`bencered/d2l-mcp-server` on exactly that basis, and `p802`'s `T966` observed that a blank
sidebar "carries no information" without drawing the symmetric conclusion). 🟢 **`T966` is now
completed: the blank field carries no information in EITHER direction.** 🔴 **Re-probe any
row this base rejected on a blank or `NOASSERTION` signal alone** — `ACTION p810-A`.

**Implication for an engagement.** 🔴 **An automated licence gate in a client's CI that keys on
GitHub's API field will both block safe dependencies and admit prohibited ones.** 🟢 **Gate on
the LICENSE bytes with a normalised comparison** — this base's
[`p135`](../compose/code/p135-licence-sha-identity/) copyright-stripped hash is the instrument,
and it is immune to exactly the whitespace divergence that produced `NOASSERTION` here.

## T28 — The standards bodies have started shipping agents themselves, and they ship the CONTROLS the vendors do not

**Evidence, `p810`.** [`Ed-Fi-Exchange-OSS/Prototype-Semantic-Layer-with-MCP`](https://github.com/Ed-Fi-Exchange-OSS/Prototype-Semantic-Layer-with-MCP)
(`Apache-2.0`, pushed `2026-11-12`) is published by the **Ed-Fi Alliance**, author of the US
K-12 data standard. 🟢 **Across fifteen passes, every other education agent in this base came
from a vendor, a lab or a student.**

🟢 **What arrives with it is not the code, it is the control stack** — identity (Keycloak
OAuth, user taken from the token's **verified email**), authorisation (**`get_my_scope`**, so
the agent can state what the educator may see before answering), data (**Postgres role pinned
`default_transaction_read_only = on`**, `REVOKE ALL ON SCHEMA public`, `GRANT SELECT` on the
analytics schema only), and provenance (every tool returns **the data-mart tables it used**).

🔵 **The generalisable principle: read-only is enforced at the DATABASE ROLE, not in the
prompt and not in the tool definitions.** 🟢 **That is the difference between a control and a
convention** — a prompt-level restriction is defeated by the next jailbreak; a
`default_transaction_read_only` role is defeated by nothing the model can emit.

🟢 **This substantially answers `p792-D`** (no independent security or data-governance
evaluation of any education MCP server): there is now a reference implementation from the
standards body, carrying an **OpenSSF Scorecard** badge. 🔴 **It does not answer it for the
`137`-tool [`amirtds/cubite-mcp`](https://github.com/amirtds/cubite-mcp) or the `77`-tool
[`jeffercbs/chispa-mcp`](https://github.com/jeffercbs/chispa-mcp), both of which run at the
teacher's own permission level with no equivalent published.** 🔵 **The gap narrows from "no
one has done this" to "one organisation has, and it is the one with no product to sell."**

## T29 — `T26`'s transform is an INSTRUMENT, because this pass made it fail cleanly twice

`T26` (`p809`) held that when this base names a platform often and shelves nothing for it,
that is a search instruction. 🟢 **`p810` ran it against six platforms. It succeeded four
times and failed twice — and the failures are what promote it from slogan to instrument.**

| Platform | Mentions | Result |
|---|---|---|
| Sakai | `3,937` | 🟢 **2 agents** |
| SCORM | `3,434` | 🟢 **2 producers + a validator** |
| Schoology / Infinite Campus | `168` | 🟢 **3 agents** |
| Canvas | (platform layer since `p3`) | 🟢 **1 agent, `119★`** |
| **OneRoster** | `3,043` | 🔴 **EMPTY result set — zero repositories** |
| **PowerSchool** | `382` | 🔴 **3 servers, NONE with a usable grant** |

🟢 **A transform that always returns something is a confirmation bias generator.** 🔵 **This
one returns nothing when there is nothing, and it distinguishes two different kinds of
nothing:** OneRoster is a **supply** gap (nobody has built it) and PowerSchool is a **licence**
gap (three exist, none is permissive). 🟢 **Those take opposite responses — build one, or ask
for a grant** — and the transform told them apart.

🔵 **`p798-G` satisfied:** this is a rate measured somewhere it should not hold, and it did not
hold, twice.

## T30 — Regulators across four jurisdictions converged on the same control point, and England states it as a RULE rather than a principle

**Evidence.** 🟢 **Ofqual: AI may not be the SOLE marker in regulated qualifications, and its
guide for schools extends that to non-exam assessment.** Its January 2026 position: AI is
promising for **quality assurance and marker training**, not ready for **high-stakes marking**,
with research finding wide context-dependence and **no general case for AI marking**.

🔵 **Set beside what this base already holds:** 🇻🇳 Vietnam's **sole-basis** test, 🇪🇺 the EU's
Art. `27` **FRIA** for public deployers, 🇺🇸 Oklahoma's **teacher-review and parent opt-out**,
🇵🇭 the Philippines' **AI registry** (DepEd Order `003`, s. `2026`), and the **OECD 2026
Digital Education Outlook**'s finding that AI helps learning only where pedagogy stays in
control.

🟢 **Four jurisdictions, a multilateral and an exam board, with no shared method, arriving at
one architecture: AI proposes, a named human decides, the system proves it.**

🟢 **Why Ofqual's phrasing is the commercially useful one: it is a bright line that names the
OPEN territory, not just the closed.** 🔵 **Closed: sole-decider marking. Open — and
explicitly endorsed: quality assurance, marker training, moderation, second-marking.** 🟢 **A
proposal that sells QA and moderation is selling into a regulator-endorsed category**, which
is a materially easier sale than a tutoring pilot. 🔴 **`compose/patterns.md` `P810-3` is built
to this line; `P22`'s human-in-the-loop publication gate already satisfies it.**

🔴 **One claim NOT carried:** a reported 2026 DfE standard requiring "progressive disclosure"
(hints rather than answers) and usage limits could not be confirmed against a government
source. 🔵 **It is newsletter-grade and it is left out of the pattern it would have supported.**

