---
industry: education
region: Global
updated: 2026-10-11
---

# Education — current trends

**Pass 132, 2026-10-11.** p131's trends retained; 🔴 **T8 and T9 are substantially corrected — both
had declared an absence that this pass filled** — **T4 and T10 are qualified**, and **T11 is added**
(see `README.md` → Pass 132). Each trend is stated with the evidence that supports it and, where it
matters, what would falsify it.

## T1 — The governance gap is the market

Student and teacher adoption has outrun institutional policy by an order of magnitude: **88%** of
students worldwide (95% of UK undergraduates) use generative AI, **60%** of US K-12 teachers used it
in 2024-25, and **18%** of US teachers have a written policy telling them how. This is the defining
condition of education AI in 2026. It means the buyer's problem is not capability — the tools are
already in the building — but control, evidence and defensibility.

**Consequence for engagements:** lead with inventory, data-flow proof, human-in-the-loop gates and
audit logs. A tutoring demo does not address the thing keeping the client awake.

## T2 — Mandates with hard dates replaced guidance

2026 is the year education AI rules acquired deadlines:

- **Ohio:** every K-12 district must adopt a formal AI use policy **by 1 July 2026**.
- **South Korea:** AI Basic Act in force **22 January 2026**.
- **India:** AI and computational thinking mandatory **from Class 3, 2026-27 academic year**.
- **China:** AI compulsory from age six since September 2025; Cybersecurity Law AI amendments
  effective January 2026.
- **Vietnam:** Decision 33/2026/QD-TTg names education — including automated assessment and
  behavioural monitoring — as high-risk.
- **EU:** AI literacy duties in force since February 2025; emotion recognition in education
  **prohibited** since 2 February 2025.
- **US states:** 134 bills across 31 states in 2026; 30+ states with guidance.

**The trend is not "regulation is coming" — it is "obligations are already in force and capacity is
missing."**

## T3 — The EU's high-risk clock slipped to December 2027, and that is a sales window

Annex III education obligations (admissions, grading, proctoring) were postponed to **2 December
2027** via the Digital Omnibus on AI. 🟢 **p131 closes p130's open question: the Council HAS adopted.**
A final Council green light is reported for **29 June 2026**, and this KB's own append-only pages
have carried the instrument as **Regulation (EU) 2026/1744 of 8 July 2026** for several passes.
p130's *"Council adoption was still outstanding"* was a regression against this KB's own record,
and an independent channel now corroborates the adoption. **The deferral is law, not a political
agreement.** Annex I embedded systems follow at **2 August 2028**.

Meanwhile what binds *now* is unmoved: Article 4 AI-literacy duties and the emotion-recognition
prohibition (both since February 2025), and **Art. 50 transparency, live since 2 August 2026**.

**Read it as:** ~14 months to build conformity in by design rather than retrofit it, not 14 months
of nothing to do. 🔴 **The old falsifier ("if the Council fails to adopt") is spent.** The live
falsifier is narrower: a further omnibus reopening Annex III, or a national regulator applying the
pre-deferral dates anyway.

## T4 — Supply is extraordinarily concentrated, and one repo is the whole mid-market

`HKUDS/DeepTutor` (Apache-2.0) stands at **41 136 stars**. The next education-specific agent found
this pass is `GarethManning/education-agent-skills` at 847 (and its licence does not resolve to an
OSI identifier), then `satvik314/educhain` at 388 and `vishalsachdev/canvas-mcp` at 288. There is
**no middle of this market** — one large permissive agent and a long tail of sub-1k projects.

**Consequence:** a client wanting "the open-source tutoring stack" gets DeepTutor plus bespoke
integration. Budget for the integration, not the engine.

🟡 **Qualified by p132 in two ways.** First, there is now a **second** repo at that scale:
[`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad)
(**Apache-2.0, 39 444★**) — so the shape is two large permissive projects, not one, and the second
one is an *offline composition layer* rather than an engine. Second, the "long tail of sub-1k
projects" is **much longer and much better placed than this KB knew**: 21 SIS/portal rows at 0–10
stars, ~80% MIT, ~90% region-placed. 🔵 **The concentration finding holds for *engines* and is
misleading about *connectors*** — the connector layer is not concentrated at all, it is atomised
across national platforms, which is a different procurement problem and a different opportunity.

**Correction to this KB's own record:** earlier passes recorded DeepTutor at "~22k★" and then
"~24k★", and `educhain` at "~9k★" then "~12k★". Verified today: DeepTutor **41 136**, educhain
**388**. The educhain figure was overstated by roughly 30×. Star counts in this KB predating pass
130 should not be trusted without re-verification.

## T5 — Connector effort has pooled on Canvas, and fork swarms inflate the apparent supply

Five-plus Canvas MCP servers exist; eight of the fifteen platforms in `verticals/solutions.md` have
**no** AI-on-top project at all.

🔴 **Correction to p130's version of this trend.** It said Moodle *"has no permissively licensed MCP
route"*. Moodle has **eight standalone MCP servers, five of them MIT** — the tier p130's queries
missed because it looked only for in-tree plugins. The concentration claim survives; the Moodle
exception does not. 🟡 **But note what the permissive tier looks like:** the largest MIT one
(`peancor/moodle-mcp-server`, 43★) has not been pushed since February 2026, and the most-starred
Moodle connector overall (`loyaniu/moodle-mcp`, 40★) carries **no licence at all**. The permissive
rows and the active rows are different rows.

Worse, the apparent supply is padded by **fork swarms**: at least five repositories carry a
byte-identical `canvas-mcp` description under different owners, and `tutor-mcp` appears under two.
A fork-excluding search resolves each to a single canonical upstream
(`vishalsachdev/canvas-mcp`, `ArnaudGuiovanna/tutor-mcp`); one fork still advertises an older
tool count as current. Counting repos overstates the field substantially.

## T6 — Licence risk is concentrated exactly where the traction is

The most-starred education agent-skills collection (847★) reads as **NOASSERTION**. A 103-star
Canvas MCP server has **no licence file at all**. The cleanest Moodle→MCP route is **unlicensed**.
Two platform licences (`openeducat_erp`, `OpenOLAT`) do not resolve to OSI identifiers.

Meanwhile the platforms are mostly **AGPL-3.0** (Open edX, Canvas, Frappe LMS, Tutor, LearnHouse,
ClassroomIO), which network-copyleft binds any client offering a hosted service. The permissive
shortlist is small and worth memorising: **Oppia (Apache-2.0), Sakai (ECL-2.0), Kolibri (MIT),
Academico (MIT), Richie (MIT), H5P (MIT), XBlock (Apache-2.0), codejail (Apache-2.0)**.

**Consequence:** licence review belongs at the start of an education engagement, not at hardening.
The highest-traction components are the riskiest ones.

## T7 — The measurement layer exists and cannot be shipped *(corrected by p131)*

🔴 **p130 stated this trend as "nobody measures learning" and called it the largest hole on the
shelf. That was false, and this KB's own pages refuted it.** Two real benchmarks exist:

- [`eth-lre/mathtutorbench`](https://github.com/eth-lre/mathtutorbench) — 43★, **ETH Zurich**,
  **EMNLP 2025 oral**, held in this KB **since pass 4**. Measures open-ended *pedagogical* capability
  (scaffolding, hint quality), not answer accuracy.
- [`Khan/tutoring-accuracy-dataset`](https://github.com/Khan/tutoring-accuracy-dataset) — 57★,
  **Khan Academy**, with its licence read in full by an earlier pass.

🔴 **The real constraint is the grant, and it is worse than a missing repo.** `mathtutorbench` has
**no licence field** and a README that names **two different licences in one file** (CC-BY-4.0 badge
vs CC-BY-SA-4.0 body); Khan's carries a **bespoke 2 690-byte "Evaluation Dataset License"**, not an
OSI one, and has been dormant since August 2024. **Both can be run and cited; neither can be shipped
inside a client deliverable without counsel.**

🟢 **The genuine gap, stated so it cannot regress again:** nothing open source measures **learning
outcomes** — durable gains in what a student knows. Both benchmarks measure *tutor behaviour*. The
OECD's 2026 Digital Education Outlook asks precisely for durable learning gains, and that standard
is still unmet.

**Still the most commercially valuable gap in the KB**, and now a cheaper build than p130 implied:
start from `mathtutorbench`'s task structure rather than a blank page, and anchor the quantitative
side on `OATutor` and `tutor-mcp`, which already expose Bayesian Knowledge Tracing mastery estimates
that an LLM's self-report cannot substitute for. See `compose/patterns.md` → P6.

## T8 — Offline and low-bandwidth stopped being an edge case

Kolibri (MIT, offline-first, content sync by LAN or USB) is the clearest instance of a trend driven
by where growth actually is: APAC at ~35.3% CAGR, India mandating AI from Class 3 across government
schools, LATAM adopting ahead of infrastructure, Google.org targeting 1.25M LATAM students by 2028.
Small local models make an offline tutor technically possible for the first time, and the data never
leaving the device resolves most of the privacy problem in T1 and T2 by construction.

~~**Nobody has built it:** no AI agent on top of Kolibri was found. MIT licence, offline design,
regulatory tailwind, no incumbent.~~

🔴 **CORRECTED BY p132 — somebody built it, at 39 444 stars.**
[`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad)
(**Apache-2.0**) is an offline-first knowledge and education server that orchestrates containerised
tools: **Kiwix** for the library, **Kolibri** for the education platform, **Ollama** for the AI
assistant. It is the **second-largest repository in this entire KB**, behind only DeepTutor. There
is also a macOS port ([`karissafuller/project-nomad-macos`](https://github.com/karissafuller/project-nomad-macos),
20★) and an Indian Class-10 offline LMS claiming Kolibri integration
([`Tushar-cy/Offline-AI`](https://github.com/Tushar-cy/Offline-AI), 2★).

🔵 **Why the probe missed it, which matters more than the miss.** p131's `kolibri stars:>2` query
was valid: 86 repos, 3 in the Learning Equality family, 0 with AI. **NOMAD composes Kolibri as a
Docker container and never names it in its description.** A dependency is not always visible in the
metadata of the thing that depends on it — so "no project builds on X" cannot be concluded from
searching for X's name.

🟢 **The trend is intact and stronger; only the opportunity changed shape.** Offline is real, the
drivers above are unchanged, and the engagement is now *"deploy and extend a permissive 39k-star
stack"* rather than *"build it"* — faster and far easier to defend in procurement.
🔴 **The surviving gaps are narrower and genuinely open: nothing builds AI *inside* Kolibri**
(NOMAD attaches from outside; the Learning Equality repos carry none), **and nothing offline
targets LATAM** — the one curriculum-specific offline project is Indian, in the region this KB
argues needs offline most. **What would falsify the trend:** NOMAD stalling, or local-model quality
on commodity hardware failing to reach tutoring grade.

## T9 — Administrative automation is the most-cited driver and the least-served

Intelligent tutoring, personalised learning, administrative automation, AI-driven assessment and
virtual assistants are the standard trend list; administration is where institutions report the
clearest return.

🔴 ~~**There is still no open-source *agent* for a student information system** — no enrolment,
records or timetabling agent. That half of the trend holds, and it is now the largest genuine hole
in this KB.~~ **REFUTED BY p132, one pass after being promoted to "the largest genuine hole".**
There are **21 rows** (`agents/top.md`), including a **NEP 2020 timetable optimiser** (MIT), a
**FERPA-logging student-records server** (Apache-2.0, org-owned), an **Okta/SCIM** identity demo,
and a **standalone 42-tool classroom-management server** (MIT) — plus national portal connectors for
Librus, EduPage, Pronote, IServ, Sisu, uSaint, VTOP, QLDT, VSB and NYCU.

🔵 **The cause of the false absence was vocabulary, not supply.** Every probe asked for *"student
information system"*, *"school management"*, *"SIS"*. The builders name repos after the platform
they connect to. The query that worked was `timetable timetabling MCP` — **timetable access is the
one capability all of them implement.**

🟢 **The trend's core claim survives in a sharper form, and it is better for an engagement.**
Administration is still underserved, but not for want of software: **(a) nothing in the tier exceeds
10 stars**, so there is no production-grade row; **(b) the credential model is unsanctioned portal
scraping with a stored pupil password**, which no client security team will accept; and
**(c) all 21 connect to proprietary or institution-hosted portals — the open-source systems of
record have exactly zero agent coverage.** 🔴 **That last point is the useful inversion: connector
effort has gone to the platforms a studio cannot fork and avoided the ones it can.**

🔴 **The other half was wrong.** p130 said the only candidates are `openeducat_erp` *"(licence
unclear)"* and `academico`. The **platform** tier is at least six systems deep —
`frappe/education` (662★), `openeducat_erp` (**LGPL-3.0**, payload-read, not "unclear"),
`academico` (MIT, 404★), RosarioSIS (GPL-2.0), Gibbon (GPL-3.0), openSIS, Fedena — all restored in
`repos/foundations.md`. 🟢 **The constraint is licensing, not supply: exactly one of them
(`academico`, MIT) can become a closed derivative.** "No software exists" and "the software is
copyleft" lead to opposite engagement plans.

## T10 — The demand-side channel is a dating channel, not a fact channel *(corrected by p132)*

🔴 **Fourth consecutive pass in which the prescribed regional battery returned nothing this KB did
not already hold.** All four regional queries plus the four global ones were run this pass. **Zero
new tokens in all four regions.** Everything they returned was already on a live page here: the
Digital Omnibus deferral (2027-12-02 / 2028-08-02), Ohio's 1 July 2026 district duty, H.R. 8747,
California AB 1159, Idaho SB 1227, Vietnam's high-risk education listing, Korea's AI Basic Act
(22 January 2026), UNESCO IESALC's **87% adoption / 26% with a strategy**, the Digital Education
Council's LATAM faculty figures, the UNESCO LAC Observatory (14 April 2026), the UK's £4M
lesson-planning programme, the OECD *2026 Digital Education Outlook*, **134 bills across 31 US
states**, and the EMEA market at ~$2.64B.

🟢 **One thing the channel did add, and it is worth the battery on its own:** independent
corroboration that the **Council adopted** the Digital Omnibus (29 June 2026), which closes a
question p130 left open and repairs `intel/policy-matrix.tsv`. A saturated channel is not a useless
channel — it is a *confirmation* channel, and should be budgeted as one.

🟢 **The supply side moved, as it has every pass.** p131's new addresses all came from
layer-specific repo queries aimed at this KB's own declared gaps, not from the generic battery:
three MIT proctoring projects, and the restoration of two tiers p130 had declared absent.

**Consequence for how these passes are run:** spend the regional battery on *confirmation and
dating*, and spend the pass's real effort on gap-directed supply queries and on **auditing this
KB's own claims against its own pages.** Pass 131 found more by grepping this repository than by
searching the web.

### 🟢 p132: the streak broke in 4 of 4 regions — and the reason refines the trend

p131 counted a **fourth consecutive pass** of zero new tokens and recommended budgeting the battery
as a confirmation channel. Run again unchanged, it produced **new tokens in all four regions**.
🔵 **But not one of them is a new fact.** Every one is a **date, a denominator or a delivery
structure**:

| region | the new token | its type |
|---|---|---|
| LATAM | IESALC fieldwork ran **August–October 2025** | 🟢 **a date that re-ages a held figure** — the *87% / 26%* numbers describe late 2025, not now |
| LATAM | **200** institutions, **19** countries; **ILIA 2025 (CEPAL)** carries country-level regulation detail | a denominator and a named instrument |
| EMEA | UK **AI Adoption Summit, £200m+**; delivered by **Cisco/IBM/BT/Rolls-Royce**, curriculum by **Skills England**, *few education providers involved* | 🟢 **a delivery structure** |
| North America | **10%** of institutions have AI guidelines; **71%** of teachers untrained; **CMU + Gates $55M** on *gateway courses* | denominators and a capital target |
| APAC | **Australia/New Zealand** tightening governance; OpenAI appoints an ANZ policy lead | a jurisdiction this KB had never covered |

🔴 **So the trend as p131 stated it was half right and the half it got wrong is the operative
half.** The battery is not saturated — it is **saturated for facts and productive for provenance**.
Four passes called it dead because they only ever asked *"what is new?"*. Asking **"when was this
measured, who was counted, and who is being paid to deliver it?"** of the *same* results is still
productive, and the answers change how a figure may be quoted to a client.

🔴 **One stale claim is still circulating and a client may arrive holding it:** that the EU AI Act
puts education AI in high-risk *"with full effect in August 2026"*. The schools-facing Annex III
date is **2027-12-02** (T3). This KB has flagged it for three consecutive passes.

## T11 — The connector layer is being built bottom-up by students, not by vendors *(new, p132)*

🟢 **The strongest structural finding of this pass, and it reframes where supply comes from.** The
21 SIS/student-portal agents found this pass share a profile so consistent it is clearly a
phenomenon rather than a coincidence:

| property | value | what it implies |
|---|---|---|
| **author** | one person, almost always a student at the institution | no roadmap, no support, no bus factor above 1 |
| **licence** | **~80% MIT** | 🟢 chosen by default, not by strategy — but genuinely usable |
| **stars** | **0–10**, none higher | no production-grade row anywhere in the tier |
| **created** | mostly within the last 6 months; three within 10 days of this pass | 🟢 the tier is *forming now* |
| **region** | **~90% placed** on hard evidence (named institution, national platform, country-coded host) | the best regional evidence in this KB |
| **target** | **proprietary** national platforms and university portals | 🔴 zero coverage of open-source systems of record |
| **auth** | the author's own portal password; unofficial; 2FA unsupported | 🔴 undeployable as published |

🔵 **Why this is happening, and why it will continue.** MCP made it a weekend's work to wrap a
portal an author already logs into daily, and the itch — *"when is my next class, what is my
attendance, am I on track to graduate"* — is universal. Nothing about that requires a vendor,
a budget, or permission.

**Consequences for a studio, in order of usefulness:**

1. 🟢 **The expensive part of a national-platform integration is already published under MIT.**
   Mapping Librus's or Pronote's undocumented surface is weeks of work; it is done and readable.
   **Keep the surface map, discard the auth layer, rebuild it sanctioned.**
2. 🟢 **These repos are a demand signal with a region attached** — and the only such signal this KB
   has. Two independent EduPage implementations is a better indicator of Slovak demand than any
   market report on this page.
3. 🔴 **None of it is adoptable.** A 1-star repo with a stored pupil password is a reference
   document, not a dependency. Say so to a client before they find it themselves.
4. 🔵 **Where it is NOT happening is the finding for LATAM:** zero of the 21 are LATAM-origin, in a
   region with real Blackboard and Chamilo share. The bottom-up wave has not reached it.

**What would falsify this:** a vendor (Librus, EduPage, Instructure, Moodle HQ) shipping an official
agent or MCP surface, which would make the student connectors redundant overnight — and which is
exactly the engagement to propose to such a vendor.

## Watch list for the next pass

**Resolved this pass:**

- ~~Whether a **student-information-system agent** appears — now the largest genuine hole (T9).~~
  🟢 **RESOLVED: 21 exist** (T9, T11). Watch instead for the *first one to exceed 10 stars*, and
  for any connector that authenticates through institutional SSO rather than a pupil password.
- ~~Whether any **Kolibri-based AI project** appears (T8).~~ 🟢 **RESOLVED: `project-nomad`,
  Apache-2.0, 39 444★**, orchestrating Kolibri + Kiwix + Ollama (T8).
- ~~**Africa and the Middle East:** no regional evidence for a second pass.~~ 🟡 **PARTLY
  RESOLVED:** one 63★ Egyptian-targeted row, unlicensed by declaration. Still no African or Gulf
  market sizing, no national instrument, no Sub-Saharan row.

**Carried forward, unchanged this pass:**

- Whether `mathtutorbench` **resolves its own licence** (T7). Re-checked: still no `LICENSE`, badge
  **CC-BY-4.0** vs body **CC-BY-SA-4.0**. Still the single highest-leverage upstream change
  available to this KB.
- Whether `instructure/canvas-lms` resumes activity; `pushed_at` **2026-04-30**, now ~5.4 months
  and a third consecutive pass unchanged.
- Whether **Open edX MCP** moves past experimental; `blend-ed/openedx-mcp` still **2 stars**.
- Whether any **proctoring project acquires an institutional owner** — tier still permissive and
  capped at 18★.
- Whether a national regulator applies the **pre-deferral AI Act dates**, or a further omnibus
  reopens Annex III.

**New for the next pass:**

- 🔴 **Probe ANZ directly.** Australia and New Zealand entered this KB this pass as a regulatory
  signal only, with **zero** ANZ-origin open-source education AI found and no dedicated query yet
  run. A mature English-language higher-ed export market running Moodle and Canvas at scale should
  not be a blank.
- 🔴 **Probe LATAM with platform proper nouns, not category terms.** The vocabulary rule
  (`agents/top.md`) was what unlocked EMEA and APAC supply this pass. The LATAM equivalents were
  never tried: **SIGA, SIGAA, Q-Acadêmico, Moodle-BR, Blackboard LATAM, Chamilo, SIAGIE (Peru),
  SIMAT (Colombia), SEP (Mexico)**. 🔵 **A LATAM zero is not credible until it is re-run this way.**
- 🟡 Read **ILIA 2025 (CEPAL)** directly for LATAM country-level regulation, instead of re-running
  regional news queries that return commentary.
- 🟡 Licence-measure the three rows left `UNREAD` this pass: `edwyj/ddl-killer`,
  `karissafuller/project-nomad-macos`, `Tushar-cy/Offline-AI`.
- 🔵 Check whether `Tushar-cy/Offline-AI` and `Tushar-cy/Ai-edge-learning-hub` are a rename pair,
  and retire the dead one from this KB before it is ever counted twice.
