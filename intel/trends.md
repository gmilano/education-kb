---
industry: education
region: Global
updated: 2026-10-11
---

# Education — current trends

**Pass 135, 2026-10-11.** p134's trends retained; 🔴 **`T12` is qualified by the measurement that
finished its own register — the sanctioned layer is not uniformly mature, and the variable is the
standard's AGE** — **`T10`'s probe rule is generalised from a fact about one word into a rule about
institutions** (`ACTION BM`), and **`T13` and `T14` are added**. Each trend states its evidence and,
where it matters, what would falsify it.

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
projects" is **much longer and much better placed than this KB knew**: **36** SIS/portal rows at
0–40 stars (21 from p132, **15 added by p133**), ~90% region-placed. 🔴 **Licence mix corrected by
p133: p132's "~80% MIT" was measured before the LATAM and ANZ probes ran** — the 12 LATAM rows are
**42% MIT**, and the tier's new top row, `BetterSEQTA-Plus`, is **MIT at 40★**, which also retires
the "nothing above 10 stars" ceiling. 🔵 **The concentration finding holds for *engines* and is
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

### 🟢 p135 generalises the probe rule: it is about institutions, not about words

p133 found that *"EMEA"* returns enterprise IT because it is **a vendor sales-region word no ministry
uses** (`P133-E`), and p134's `ACTION BK` confirmed it by re-probing EMEA country by country.
`ACTION BM` tested the other two regions this pass:

| bare probe | result |
|---|---|
| **"EMEA"** | 🔴 **Fails.** Enterprise IT outlooks, a 2023 enterprise-AI trust study, enterprise compliance commentary. One education source, and its event sat in **October 2024** |
| **"APAC"** | 🔴 **Fails identically.** Enterprise tech priorities, sovereign-cloud analysis, and vendor press releases. The run recorded finding **no** education-specific regulation, ministry rule or edtech market data |
| **"LATAM"** | 🟢 **Succeeds.** UNESCO **IESALC** (200 institutions, 19 countries, 87% using AI, 26% with a framework), the **Digital Education Council** LATAM survey 2026 (30 000+ responses), the **IDB** readiness index, and country-level regulatory posture for Chile, Brazil, Colombia and Mexico |
| **"North America"** | 🟡 **Partly.** Market-research geography segments dominate, but real findings surface (state-legislature activity, a $169M government commitment, a $55M CMU/Gates courseware investment) |

🔴 **So `P134-H` is not a fact about the word "EMEA", and stating it that way was too narrow.**
🟢 **The rule:** *a bare regional probe returns education material exactly when a region-scoped
education body publishes under that label.* Latin America has two — **UNESCO IESALC**, the
institute for higher education in Latin America and the Caribbean, and the **IDB**. "EMEA" and
"APAC" have no counterpart; no ministry, university network or multilateral addresses research to
them. "North America" sits in between because market-research firms use it as a reporting segment.

🔵 **Why this is worth more than the three results.** It is **decidable before searching.** Ask
whether a region-scoped education institution exists; if not, probe by country from the start.
🟢 **That is a standing method rule, and it predicted this pass's APAC result correctly** — the
country probe returned India's Class-3 mandate, Singapore's literacy framework and South Korea's
2026 work plan, none of which the regional probe could see.

## T11 — The connector layer is being built bottom-up by students, not by vendors *(new, p132)*

🟢 **The strongest structural finding of this pass, and it reframes where supply comes from.** The
21 SIS/student-portal agents found this pass share a profile so consistent it is clearly a
phenomenon rather than a coincidence:

| property | value | what it implies |
|---|---|---|
| **author** | ~~one person, almost always a student~~ → 🔴 **not in LATAM or Australia** | p133: **4 rows serve a teacher**, one is **org-owned with a product homepage** (`expeditto`), and `BetterSEQTA` is a two-product org with 25 forks |
| **licence** | ~~**~80% MIT**~~ → 🔴 **tier-wide this is wrong; see p133** | 🟡 measured on 21 EMEA/APAC/NA rows. The **12 LATAM rows** p133 added are **42% MIT** (3 unlicensed, 2 GPL-3.0, 1 AGPL-3.0), and the one row p132 left unread reads **AGPL-3.0** |
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
4. ~~🔵 **Where it is NOT happening is the finding for LATAM:** zero of the 21 are LATAM-origin…~~
   🔴 **REFUTED BY p133, and this was a claim about a query.** Probing `sigaa`, `suap` and
   `siu-guarani` returns **12 LATAM rows**. The bottom-up wave had reached LATAM; the probe had not.
   🟢 **And it arrived in a different shape: LATAM's wave is partly *staff-side*** — `expeditto`
   (AGPL-3.0, org-owned, drafts a lecturer's RIT workload report), `auto-sigaa` and
   `Auto_Grade_Guarani` (both move grades into the national SIS for a teacher). See `T9`.
5. 🔴 **The structural risk of the whole tier now has a measured instance, not just a worry.**
   `st22209/Parent-Portal` (MIT, New Zealand, **KAMAR**) is **archived**, and its README gives the
   cause: *"[DEPRECATED AFTER KAMAR API CHANGE]"*. **An unsanctioned connector does not degrade when
   the vendor changes an endpoint — it ends.** That is the argument for pattern `P8` as an observed
   outcome.

**What would falsify this:** a vendor (Librus, EduPage, Instructure, Moodle HQ) shipping an official
agent or MCP surface, which would make the student connectors redundant overnight — and which is
exactly the engagement to propose to such a vendor.

## T12 — The sanctioned-integration layer is mature, permissive and agent-less *(new, p134)*

🔴 **This is the trend that reframes `T5`, `T6` and `T11` at once, and it took four passes of
connector-counting to see.** `T11` says the connector layer is being built bottom-up by students
rather than vendors, and `agents/top.md` says the resulting credential model makes nearly all of it
undeployable. 🟢 **Both are true of the *portal* layer and false of the layer beside it.**

**The interoperability standards layer — LTI 1.3 Advantage, OneRoster 1.2, Ed-Fi, xAPI — is built,
permissive, and owned by exactly the institutions this KB keeps saying are absent:**

| the claim this KB has been making | what the standards layer shows |
|---|---|
| *"supply is extraordinarily concentrated and student-built"* (`T4`, `T11`) | 🟢 **`Cvmcosta/ltijs` — Apache-2.0, 373★, pushed 2026-10-06.** Larger and more active than the LTI row this KB already had |
| *"licence risk is concentrated where the traction is"* (`T6`) | 🔴 **Inverted here.** The platforms are AGPL/GPL/LGPL; **the standards layer is Apache-2.0, MIT and 0BSD** — the most permissive set of rows in this entire KB |
| *"no institutional or vendor owners"* | 🟢 **Ed-Fi Alliance, Google, the US DoD's ADL Initiative, the Minnesota Department of Education, France Université Numérique, UNIwise ApS, Blackboard, Open Assessment Technologies** |
| *"the credential model is a tier-wide blocker"* | 🟢 **A tool launched over LTI holds no user password at all** — it runs on a client ID the institution issues and can revoke |

🔴 **And here is the trend, in one sentence: the standards are finished and the agents have not
arrived.** The bridge from an AI agent to any sanctioned learning standard is **one repository** —
[`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) (MIT, 15★, last push
2025-08-29) — and **the only Ed-Fi MCP server in existence is an empty repository**
(`cdweaver1992/edfi-mcp-server`: `size: 0`, HTTP 404 on 15 probes across 3 branch refs, created and pushed in
the same second).

🟢 **Why this is a trend and not a single finding.** The direction of travel across every other
trend on this page points at it. `T9` (administrative automation is the most-cited driver and least
served) needs a system of record, and OneRoster/Ed-Fi *is* the sanctioned route into one. `T3` and
the 2027 compliance clocks reward auditable access over scraped access. The market's
fastest-growing segment — **assessment and feedback agents at 44.36% CAGR** — is precisely what
**LTI AGS grade passback** was designed to carry. 🔵 **Four independent pressures all terminate at
the same missing component, which is usually what a build opportunity looks like before anyone
builds it.**

🟡 **What would falsify this trend.** If an MCP-over-LTI/OneRoster server appears with real
traction in the next few passes, this stops being an opportunity and becomes a dependency — and
**that is the thing to watch for, because it would also be the fastest-moving row in this KB.**
🔴 **Equally, if the standards layer turns out to be shallower than its metadata suggests — the
Python LTI library is already ~2 years dormant and the xAPI bridge ~14 months — then "mature" is
too strong, and this pass will have over-read activity from stars and a single `pushed_at`.** No
repository in this tier has been code-audited by this KB.

🔵 **The regional asymmetry is part of the trend, not an aside.** LTI, OneRoster and Ed-Fi are
**North-American and European procurement standards**. The LATAM national systems (SIGAA, SUAP,
SIU-Guaraní, SAES, Q-Acadêmico) publish no equivalent, and APAC's only standards-tier rows are an
AGPL-3.0 project and a spec translation. 🔴 **So the sanctioned path is available where the
standards are, and the scraping is a symptom of their absence — not of a different builder
culture.** That is a materially different explanation from `T11`'s, and it is testable: it predicts
that LATAM supply stays unsanctioned until a national system publishes an API, regardless of who
builds it.

### 🔴 p135 qualifies `T12`: maturity tracks the standard's AGE, not its design

p134 stated `T12` as *"the sanctioned-integration layer is mature, permissive and agent-less."*
🟢 **The second and third clauses hold.** 🔴 **The first is true only on average, and the average
hides the thing a studio needs to know.** Finishing the register (`ACTION BN`) measured all six
remaining standards:

| standard | first published | largest repo | ★ | supply verdict |
|---|---|---|---|---|
| **SCORM** | **1999** | `adaptlearning/adapt_framework` | **630** | 🟢 **Deep.** Four repos above 350★; a permissive modern runtime; authoring tools |
| **LTI** | 2010 (1.3 in 2019) | `Cvmcosta/ltijs` | **373** | 🟢 **Strong and current** (pushed 2026-10-06) |
| **QTI** | 2000s (QTI 3 in 2022) | `amp-up-io/qti3-item-player` | **30** | 🟡 **Thin but real** — 15 repos, mostly MIT, several vendor-owned |
| **Open Badges** | 2011 (3.0 in 2022) | `1EdTech/digital-credentials-public-validator` | **17** | 🟡 **Thin, converging on W3C Verifiable Credentials** |
| **Comprehensive Learner Record** | 2010s | *the same validator* | **17** | 🔴 **One real row in existence** |
| **Caliper Analytics** | 2015 | `lsloan/udp-notebooks` | 🔴 **0** | 🔴 **No usable supply at all.** One repo, unlicensed, untouched since 2023 |

🔵 **The pattern is monotonic in age and has nothing to do with the standards' quality.** SCORM is
technically the crudest of the six and has the most code; Caliper is the most modern event model and
has none. 🟢 **The mechanism is deployment, not merit: SCORM and LTI are what institutions have
*bought* for twenty years, so there is installed base to write against.** Caliper and CLR are
procured rarely, so nobody has written a client.

🔴 **What this changes in a pitch.** *"We build on the sanctioned standards"* is credible for content
and launch (SCORM, LTI), **defensible** for assessment and credentials (QTI, Open Badges), and
🔴 **not currently true for analytics** (Caliper). A proposal that promises standards-based learning
analytics is promising a standard with **no open-source client**, which is a build the client should
be told about rather than a dependency.

🔵 **Falsifier.** If a Caliper or CLR client library appears above ~50★ with a permissive licence,
this reframing weakens and `T12`'s original wording is closer to right.

## 🔴 `T13` — The credential blocker was solved and replaced by an identity-assertion blocker *(new, p135)*

**This is the most consequential thing p135 found, and it only became visible by reading source.**

For four passes this KB has said the portal-connector tier is undeployable because every row holds a
student's password, and that the sanctioned path fixes it. 🟢 **The second half is confirmed:** of
the three bridges read this pass, **`ltijs` holds no user credential at all**, and the two MCP
servers hold an institution-issued *service* credential, never a student's password.

🔴 **But the sanctioned standard carries a cryptographically verified identity, and both agent
bridges to it discard that verification:**

| bridge | how the user's identity is established |
|---|---|
| `Cvmcosta/ltijs` | 🟢 **A platform-signed JWT, signature verified** against the platform's keys, with nonce tracking |
| `DavidLMS/learnmcp-xapi` | 🔴 **An environment variable** (`ACTOR_UUID`). 🔴 And its own docstrings claim *"Actor UUID from JWT"* while **the project has no JWT dependency at all** |
| `nitsuah/bb-mcp` | 🔴 **The caller's own assertion** (`caller_identity`), documented as *"trusted at face value"*. `role: "admin"` bypasses the course-entitlement gate; the app token is **org-wide** |

🔵 **Why this is a trend and not three bugs.** It is structural. MCP has no end-user identity model —
`bb-mcp`'s source says so in its first paragraph — so **every MCP server that fronts an institutional
system of record must either invent an identity model or accept one on trust, and the shipped
examples accept it on trust.** As agent-mediated access spreads from reading a portal to writing a
system of record, that choice stops being acceptable: a grade write attributed to an unverified
subject is an audit finding.

🟢 **The commercial consequence, and it is a component rather than a caveat.** The missing piece is
an **identity broker**: something that terminates a verified identity (an LTI launch, OIDC, or the
institution's IdP) and only then calls the MCP server with a subject it has itself established.
🔴 **No repository in this KB does this, in any region.** That is the clearest unbuilt component on
the shelf, it sits between two mature layers, and it is required by every engagement on the
sanctioned path. See `compose/patterns.md` → **P13**.

🔵 **Falsifier.** If an MCP server appears that verifies an LTI or OIDC assertion itself before
acting — rather than accepting `caller_identity` — this trend has been answered by the ecosystem and
becomes a build-versus-buy question instead of a gap.

## 🟡 `T14` — Licence metadata is systematically wrong in the direction of institutional code *(new, p135)*

🔴 **Measured, twice, with a reason.** `P134-F` found that GitHub's `NOASSERTION` is *"biased toward
unusual, not toward fine."* p135 measured why, by hash-matching 26 licence payloads against
canonical SPDX texts (`compose/code/p135-licence-sha-identity`):

- 🔴 **A licence payload never matches its canonical text naively.** Real `LICENSE` files wrap at ~72
  columns; SPDX wraps at ~105. **Zero of 26 payloads were whitespace variants** — refuting the
  premise `ACTION BP` was written on.
- 🔴 **Matchers are defeated by punctuation.** SPDX's canonical GPL-3.0 uses curly quotes; the
  `COPYING` shipped in real repositories uses ASCII. That alone accounted for five payloads.
- 🔴 **And by the licence steward editing its own text.** Two such edits are known for GNU: the
  `http`→`https` change, and the FSF moving `why-not-lgpl.html` from `/licenses/` to `/philosophy/`.
- 🔴 **The bias has a cause: appended institutional attribution.** `OpenOLAT` is Apache-2.0 to the
  character and then carries two attribution statements for the University of Zurich's original OLAT
  base and frentix GmbH. `Citolab/qti-convert` fills GNU's appendix with its real holder —
  **Stichting Cito Instituut voor Toetsontwikkeling** — which is correct practice and makes the text
  non-canonical. 🟢 **Well-governed, institution-derived projects are the most likely to append
  attribution, so they are the most likely to be mislabelled.**

🔴 **The practical edge, because this is a procurement risk and not a curiosity.** In this corpus a
badge would have mislabelled an LMS a studio can use (`OpenOLAT`, permissive) and said nothing about
two it cannot: `pipwerks/scorm-api-wrapper` (**391★, 130 forks, no licence file at all**) and
`cybercussion/SCOBot` (**164★, and the licence file is the CC-BY-SA-4.0 human-readable deed, not the
legal code** — a ShareAlike content licence on software). 🟢 **Rule: on anything a client will ship,
read the payload and hash it. A badge is a lead.**

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
- ~~Whether `instructure/canvas-lms` resumes activity; `pushed_at` **2026-04-30**…~~ 🔴 **RETIRED
  BY p133 AS A MIS-MEASUREMENT.** `canvas-lms` declares the topic **`gerrit-mirror`**, and
  `instructure/analytics` shares its `pushed_at` **one second later** (14:52:10 / 14:52:11) — two
  repos cannot be hand-pushed a second apart. **This is a stopped mirror export, not four passes of
  developer silence.** 🟡 **Watch the right thing instead: whether the GitHub mirror resumes at all**
  — because while it is frozen, GitHub is not an activity signal for Canvas and anyone diffing the
  mirror to track upstream is reading a five-month-old tree. See `repos/foundations.md`.
- 🔴 **New standing rule from that correction: never read `pushed_at` as activity without checking
  for a mirror.** Flag a recency reading as unreliable when *"mirror"* appears in topics, when two
  repos in one org share `pushed_at` to the second, or when the README names an upstream elsewhere
  (Gerrit, GitLab, SVN). This KB's `git-recency-channel` and `p109-freshness` lanes currently
  mis-rank every mirror in the direction of looking abandoned; `gerrit` appeared **zero** times
  across 1 733 addresses before this pass.
- Whether **Open edX MCP** moves past experimental; `blend-ed/openedx-mcp` still **2 stars**.
- Whether any **proctoring project acquires an institutional owner** — tier still permissive and
  capped at 18★.
- Whether a national regulator applies the **pre-deferral AI Act dates**, or a further omnibus
  reopens Annex III.

**New for the next pass:**

- ~~🔴 **Probe ANZ directly.**~~ 🟢 **DONE p133 (`ACTION BF`) — and ANZ is not a blank.**
  `BetterSEQTA/BetterSEQTA-Plus` (**MIT, 40★**, org-owned, 25 forks, Chrome Web Store, pushed
  2026-10-06) and `BetterSEQTA/DesQTA` (**MIT, 16★**) over **SEQTA**, Australia. New Zealand:
  one MIT **KAMAR** row, archived. 🟡 **Watch next: whether `BetterSEQTA` adds an AI/MCP surface** —
  it is the only product-shaped org in the portal tier and has not yet shipped an agent.
- ~~🔴 **Probe LATAM with platform proper nouns, not category terms.**~~ 🟢 **DONE p133
  (`ACTION BE`) — REFUTED: 12 LATAM rows.** `sigaa` (5), `suap` (3), `siu-guarani` (4). 🔴 **Probes
  that returned nothing are recorded with their probe in `intel/market.md` → LATAM**: SIAGIE (Peru)
  and Q-Acadêmico (Brazil) have real installed bases and **no agent layer at all** — the two
  cleanest unclaimed LATAM slots this KB can name. **Chile's `ucampus` probe collided with a Chinese
  homograph and the qualified re-probe returned 0.** 🟡 **Not reached: `simat` (Colombia), `saes`
  (Mexico)** — carried as `ACTION BJ`.
- 🟡 Read **ILIA 2025 (CEPAL)** directly for LATAM country-level regulation, instead of re-running
  regional news queries that return commentary.
- ~~🟡 Licence-measure the three rows left `UNREAD`…~~ 🟢 **DONE p133, all three read:**
  `edwyj/ddl-killer` = 🔴 **AGPL-3.0** (holder is the FSF only — a `DOCUMENT-TEXT` case),
  `karissafuller/project-nomad-macos` = 🟢 **MIT** (*"Copyright (c) 2026 Karissa Fuller"*),
  `Tushar-cy/Offline-AI` = 🔴 **no payload at `/main/` or `/master/`** → measured-absent.
  🔴 **Instrument note for the next pass: the GitHub contents API is scope-blocked in this session**
  (it returns *"repository is not configured for this session"*, which is an authorisation refusal,
  **not** a 404 and **not** evidence about the repo). **The working lane is
  `raw.githubusercontent.com/<owner>/<repo>/<branch>/LICENSE`.**
- 🔵 Check whether `Tushar-cy/Offline-AI` and `Tushar-cy/Ai-edge-learning-hub` are a rename pair,
  and retire the dead one from this KB before it is ever counted twice.

### 🆕 Added to the watch list by p134

- 🟢 **An MCP server over LTI AGS, OneRoster or Ed-Fi gaining traction.** Today the whole category is
  one 15-star repo and one empty one. This is the highest-signal thing to re-measure next pass.
- 🔴 **`cdweaver1992/edfi-mcp-server` — watch for it to acquire code.** A named, described, empty
  repo in a high-demand slot is the kind of thing that gets filled, and if it is filled by someone
  else it stops being an opportunity.
- 🟡 **`dmitry-viskov/pylti1.3` (MIT, 138★, last push 2024-08-18).** The Python LTI binding is the
  weak link for any agent build. Watch for a fork gaining activity, or for the upstream to wake.
- 🟡 **`DavidLMS/learnmcp-xapi` last push (2025-08-29).** If it stays still, the bridge has to be
  built rather than adopted.
- 🟢 **France's fuller AI-in-education plan**, expected spring 2026 per the June 2025 *cadre
  d'usage*; and whether a **national monitoring body** is created, since its absence is the
  assurance opening.
- 🟢 **Jisc's AI marking and feedback pilots (38 UK institutions).** Findings from a 38-institution
  programme would be the best outcome evidence available in this market.
- 🔴 **Colorado's reported AI Act repeal (May 2026) and the FERPA-covered-institution exemption** —
  unconfirmed by any second source this pass. **Either confirm it against the state legislature or
  strike it; it must not reach a client either way until then.**
- 🟡 **Whether "APAC" and "LATAM" are mis-queried the way "EMEA" was.** `ACTION BK` proved the
  sales-region word reaches enterprise IT rather than ministries. The same test has not been run on
  the other two region words — see `ACTION BM`.

### 🆕 Added to the watch list by p135

- 🔴 **Whether an identity broker appears** — an MCP server, or a component in front of one, that
  verifies an LTI launch or an OIDC assertion itself rather than accepting `caller_identity` on
  trust. **This is the single most consequential thing to watch on this shelf** (`T13`). It would
  turn the sanctioned path from a build into an assembly.
- 🔴 **Whether anything at all appears for Caliper Analytics.** One repository, 0★, unlicensed,
  untouched since 2023. A permissive client above ~50★ would reframe `T12` and partially unblock the
  measurement layer of `T7`.
- 🟡 **Whether `pipwerks/scorm-api-wrapper` gains a licence.** 391★ and 130 forks with no grant of
  rights; the sector's most-used SCORM wrapper. Also worth measuring: **how far down this KB's own
  rows that defect propagates** — a dependency-closure question, and the instrument exists.
- 🟡 **Whether `learnmcp-xapi` is maintained or forked.** Last push **2025-08-29**, and it is still
  the only agent↔xAPI bridge in existence. Its docstrings describe a JWT trust anchor it does not
  implement, so a maintained fork would be a natural place for the identity work above to land.
- 🟡 **Whether `Selleo/mentingo` keeps its pace.** MIT, 92★, pushed 2026-10-10, and the only row
  where the AI *is* the platform rather than a connector onto someone else's. If it sustains, it is
  a fork base; if it stalls, it is a reference architecture.
- 🔴 **Japan's national AI-education policy, which this pass measured ABSENT** and which is a hole in
  this KB's APAC coverage rather than a finding about Japan. Probe MEXT directly, in Japanese.
- 🟡 **Whether Colorado's enforcement stay is lifted** (`X. AI LLC v. Weiser`) and whether the AG's
  rulemaking lands by its **2027-01-01** deadline. The compliance dates are not stayed; the cure
  period ends 2030.
- 🟡 **Whether ELM (European Learner Model) supply grows beyond three repositories**, and whether any
  of it appears in a language other than Rust. It is the EU's cross-border credential model and the
  only permissive implementation is a language mismatch for most AI work.
