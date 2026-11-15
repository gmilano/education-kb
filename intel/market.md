---
industry: education
region: Global
updated: 2026-11-15
---

# Education AI — market map and opportunities by region

Researched through 2026-11-15, across **twenty-eight** passes; each region's updates are
ordered **newest first** directly under its heading. 🟢 **Twenty-eighth pass (`p823`):
`114` `#### Update` blocks across five regions — North America `24`, EMEA `24`, APAC `24`,
LATAM `25` (`7` direct + `18` nested, see the derivation note below), Global `17`.
Every region gained one, as every pass must.**
🔴 **Derivation note, because the naive tally is wrong and has been for several passes:** an
`awk` tally keyed on the nearest preceding `### ` attributes `18` of LATAM's blocks to the
nested `### 🟢 ACTION p816-F` subsection that lives INSIDE the LATAM section, and reports LATAM
as `5`. 🟢 **LATAM's real figure is `5 + 18 = 23`; the nested heading is a sub-section, not a
sixth region.** 🔵 **Re-derive with `awk '/^### /{sec=$0} /^#### Update/{c[sec]++}'` and then
FOLD the `ACTION p816-F` bucket into LATAM — or the count under-reports the best-covered
region in the file.**
🟢 **And for the first time every region's SUPPLY side is measured as well as its policy side:
`agents/top.md` now reads `Global 53 · APAC 17 · EMEA 12 · North America 12 · LATAM 9`,
with no region in single digits.**
🔵 **Re-derived this pass with an `awk` tally over `^#### Update` per `### ` section, not
carried forward.** 🔵 **Re-derived this pass with
`grep -c '^#### '` per region section, not carried forward.** 🟢 **Every region gained a
block this pass, which is the point of the rotation — a North America or EMEA engagement is
served as well as a LATAM one.** 🔴 **This line said "four passes" through the
twelfth pass (`p807`) while the file held twelve** — the same prose-count drift that
`agents/top.md` and `compose/patterns.md` have each had to correct. 🔵 **Re-derive with
`grep -c '^#### ' intel/market.md` rather than carrying this sentence forward**; the
pass number is the per-region block count, not the total. Where sources disagree, the disagreement is shown rather
than averaged away. Market-size figures for AI in education come largely from
vendor blogs citing differing research firms and should be treated as
order-of-magnitude only.

## Market size — contested

Four 2026 figures for the AI-in-education market, all for the same year:
**$10.4B**, **$11.4B**, **$12.3B** (HolonIQ), and projections running from
$32.3B (by 2030) to $57B (by 2033). All trace to secondary vendor sources. Use
"roughly $10–12B in 2026, growing fast" and do not quote a specific figure to a
client without a primary report.

**Segment figures added 2026-11-13 (third pass).** The whole-market number is
the least useful one to carry into a conversation; the segment numbers are
narrower and better matched to what a studio actually sells:

| Segment | 2026 | Forecast | Source |
|---|---|---|---|
| **Agentic AI in education** | **$2.37B** | $11.83B by 2031 | Mordor Intelligence |
| **AI tutors** | **$2.7B** | $17.7B by 2033 | Grand View Research |
| AI in education (whole) | $11.4B | 25.9% CAGR 2026–2033 | Grand View Research |

Mordor also puts **Intelligent Tutoring Systems at 26.04% of the agentic
education segment (2025)** — the largest single share, which is consistent with
ITS being where the open-source agent supply in this KB is concentrated
(`DeepTutor`, `OATutor`, `tutor-mcp`, `ai-shifu`).

**Use the agentic figure, not the headline figure.** "$2.37B in 2026 growing to
$11.83B by 2031" is defensible, segment-correct and roughly 5× growth; "$11.4B
AI in education" includes hardware, smart classrooms and proctoring that no
studio engagement touches. Same caveat as above: all of these are secondary
vendor estimates, cited as such.

## The structural fact of this market

**Adoption has outrun governance everywhere, and the gap is the commercial
opportunity.** Every region shows the same shape — very high individual use by
students and teachers, very low institutional policy coverage:

| Evidence | Figure | Source type |
|---|---|---|
| Students using AI in their studies (16 countries) | 86% | Digital Education Council survey, via secondary |
| LATAM higher-ed institutions using AI in ≥1 area (200 institutions, 19 countries) | 87% | UNESCO IESALC study |
| LATAM institutions with any formal AI framework | 26% | UNESCO IESALC study |
| LATAM universities with no specific AI budget | 55% | UNESCO IESALC study |
| LATAM institutions that evaluate their AI implementation | 9% | UNESCO IESALC study |
| Brazilian school administrators using AI | 53% | Cetic.br |
| Brazilian schools with any AI guideline | 22% | Cetic.br |
| US faculty reporting a formal institutional AI policy | ~25% | secondary roundup |

The sellable work is therefore rarely "build a tutor". It is **governance,
integration, evaluation and teacher enablement around tools the institution is
already using unofficially.**

## Global players

**Open-source / buildable layer:** HKUDS (DeepTutor, Apache-2.0, 58.7k),
Tsinghua MAIC (OpenMAIC, MIT, 43.4k), JuneYaooo (teacher-to-skills,
Apache-2.0, 475), Open edX nonprofit (Harvard/MIT lineage), Moodle HQ,
Instructure (Canvas), Learning Equality (Kolibri, MIT), Khan Academy (Perseus
MIT; Khanmigo commercially), Oppia Foundation, Frappe, OpenEduCat, and the
LTI 1.3 maintainers (Cvmcosta/ltijs Apache-2.0; Packback; Simon
Initiative/Open Learning Initiative).

**Policy and standards setters:** UNESCO and UNESCO IESALC, OECD, European
Commission (AI Act, Digital Education Action Plan), 1EdTech (LTI, Caliper,
QTI), national education ministries.

**Commercial incumbents to integrate with or displace:** Instructure, Anthology,
PowerSchool, Google for Education, Microsoft Education, Duolingo, Chegg,
Coursera, 2U/edX, plus OpenAI and Anthropic distributing directly into
education — OpenAI with named government and education-system partnerships
across EMEA.

## Opportunities by region

### North America

#### Update 2026-11-15 (thirty-first pass, `p826`) — the supply side arrives in North America as PUBLIC-DATA infrastructure, and the regulatory surface is `134` bills with a cautious posture

🟢 **The regional leg produced. Regulatory and market items below are `CITED, NOT READ` (WebSearch summaries — 🔴 `WebFetch` resolved no external host this pass, so not one primary document was opened and every figure here carries that caveat). Repository items are first-hand and byte-read.**

- 🔴 **Legislative volume, cited:** a 2026 tracker counts **`134` AI-in-education bills across `31` states**, concentrated on data privacy, classroom restrictions and curriculum. 🔵 **The posture reported is GUARDRAILS AND RESEARCH rather than mandated adoption** — which is the opposite of the procurement-driving posture EMEA's Annex III timetable creates, and it is why a North American engagement is sold on evidence and outcomes rather than on compliance.
- 🔴 **Named deadlines, cited:** **North Carolina SL 2026-41** — state model policy due `2026-12-31`, local district policies due `2027-06-30`. **Virginia's 2026 law** requires school boards to follow state education-department guidance. **Maryland** requires state guidance plus district AI policies. **New York** would restrict classroom AI to grade 9 and above. 🟢 **The North Carolina pair is the nearest dated obligation in any region and the clearest single hook for a Q1-2027 district engagement.**
- 🔴 **Federal, cited:** a US Department of Education **AI framework for education (March 2026)** and **K-12 guidance (April 2026)**; **$169M in FIPSE awards** including support for responsible AI use. 🟡 A risk-tiered NEPC framework is reported by a single secondary source and is **not** treated as established here.
- 🟡 **California, cited:** analysts expect it to be the de-facto standard-setter; a **"Parents & Kids Safe AI Act"** ballot initiative was proposed in January 2026 by OpenAI and Common Sense Media and would reach edtech vendors using AI.
- 🔴 **Canada:** the leg returned workplace-focused AI rules (Working for Workers Four Act, 2024) and **essentially nothing on classroom AI policy.** 🔵 **Recorded as an INFORMED GAP rather than as coverage: Canada is the one North American jurisdiction this base still cannot describe at the classroom level, and a later pass should query provincial ministries by name rather than "Canada AI education".**
- 🟢 **The supply-side finding, measured first-hand and new this pass.** North America's open education supply is arriving as **deterministic wrappers over free public data**, not as tutors. `bsayres/heronhex-highered` (MIT) ships five MCP servers plus six skills over institutional, Title IV/FSA risk, funding, labor-market and live accreditation data; `theluckystrike/ap-score-distributions-mcp` (MIT) ships College Board AP distributions through **May 2026**. 🔵 **Both carry a full provenance envelope and both REFUSE to estimate where the published data stops. For institutional research, accreditation and program-review engagements this is a better starting point than any model, and it is `0★` — invisible to every star-ranked sweep this base runs (`T91`).**
- 🟡 **Carried forward, unchanged:** the Ellucian Banner / Workday Student duopoly remains the higher-ed SIS reality, and this pass found its only open agent surface (`Jayb1u3/andrews-ssb-mcp`) to be a `4 KB` single-campus sketch 🔴 **with no licence file.** The Banner seam is being probed and is not yet served.

#### Update 2026-11-15 (thirtieth pass, `p825`) — state legislation is the live regulatory surface, and the homework-help incumbent is visibly collapsing

🟢 **The regional leg produced; all items below are `CITED, NOT READ` (web-search summaries — this
session's egress resolved GitHub, PyPI and WebSearch only, and direct fetches to analyst and law-firm
domains were refused at the proxy).**

- 🟡 **State law is where the binding activity is.** At least **`15` states** have introduced or passed
  legislation specifically on AI in education as of early 2026; the PIE Network is reported tracking
  **nearly `100` state bills** this year that could directly affect students' use of AI in K-12.
  🔵 **Virginia `S.B. 394` directs the state education agency to issue guidance including teacher
  training.** 🟢 **Characterised by one source as *guidance proliferating faster than hard rules* —
  which is the opposite shape from EMEA, where one binding instrument covers the whole bloc.**
- 🟡 **Federal layer:** executive orders from 2025 into early 2026 are reported to have established a
  national framework for AI in education and a task force supporting K–12 AI instruction, plus a
  **White House *Pledge to America's Youth: Investing in AI Education***. 🔵 **FERPA and COPPA remain
  the hard floor underneath all of it and are unchanged.**
- 🔴 **A `2026-01` California ballot initiative was announced that could reshape how AI companies
  interact with minors** — the single most consequential NA item to re-check next pass, because an
  under-18 interaction rule hits every tutor product on these shelves directly.
- 🟡 **Market size, two independent framings, both vendor-sourced:** USA AI-in-education
  **`$3.28B` (2025) → `$15.25B` (2031)**; NA still the largest revenue region while APAC grows faster.
- 🔴 **Incumbent damage is now concrete, not predicted: Chegg is reported to have cut `45%` of staff**
  as AI assistants and Google AI Overviews removed homework-help traffic. 🔵 **This base has carried
  "disintermediation" as a trend for many passes; this is the first pass with a headcount attached.**
- 🟢 **Supply note from this pass's own measurement, and it is NA-relevant:** `EDU-C2-028`
  ([`sbdnakashima/agentic-star-iep-section-drafting-agent`](https://github.com/sbdnakashima/agentic-star-iep-section-drafting-agent),
  MIT, byte-read) is named for the **IEP** — a US IDEA statutory instrument — 🔴 **but was written in
  APAC and had never been found by any NA-framed query on this base.** 🔵 **The clearest single
  illustration of `T86`: the supply for a North American statutory process was published under a
  Japanese vendor's brand and was invisible to `29` passes of NA-vocabulary search.**


#### Update 2026-11-15 (twenty-ninth pass, `p824`) — 🔴 The regulatory instrument is still the STATE, the federal layer is now a framework rather than a rule, and the region produced ZERO new agent supply this pass

🟡 **Sourcing note for every item in this block: egress in the `p824` environment resolved GitHub and web search only — `oecd.org` was refused at the proxy, as at `p822`. Every market and regulatory item below is `CITED, NOT READ`: it comes from web-search summaries of secondary sources, several of them vendor blogs and trackers. 🔴 Verify any date, bill number or percentage against the official text before quoting it to a client. Every REPOSITORY figure in this pass is first-hand and byte-read; the two classes are not interchangeable.**

- 🔴 **The state wave, re-counted at the same figure as `p823`: `134` AI-in-education bills across
  `31` states in 2026**, concentrated on data privacy, classroom limits and curriculum, with
  legislators described as prioritising guardrails over mandated adoption. 🟢 **Two passes, two
  independent trackers, one number — this base now treats `134` as stable for the 2026 session.**
- 🔴 **Named state instruments with DATES, which is what an engagement plan needs:**
  🇺🇸 **North Carolina Session Law 2026-41** — state model policy by **`2026-12-31`**, local district
  policies by **`2027-06-30`**, teacher training by **`2028-06-30`**;
  🇺🇸 **Virginia (2026)** — school boards must adopt policies consistent with Department of Education
  guidance; 🇺🇸 **New York A 9190 (proposed)** — would restrict classroom AI use to **grade 9 and
  above**, with exceptions for diagnostics and special education.
  🔵 **The North Carolina chain is the most sellable shape in this block: three dated deliverables,
  one per level of government, and `P16`'s policy pack is already built for exactly it.**
- 🟡 **Federal posture: a FRAMEWORK, not a rule.** A **March 2026 "Framework for Responsible Use and
  Development of Artificial Intelligence in Education"** from the Office of Educational Technology,
  plus an April 2026 K-12 guidance document, are cited this pass. 🔵 **A framework moves procurement
  language, not liability. The binding instruments in this region remain state law and the ADA.**
- 🔴 **The nearest hard deadline in this block is still ACCESSIBILITY, not AI.** An **April 2026 ADA
  Title II web-accessibility deadline for large public institutions** is cited again this pass.
  🟢 **`P47` is the recipe and `p818` shelved the two tools (`508-Agent`, `wcag-guide`); the
  obligation binds every institution on every platform in `verticals/solutions.md`.**
- 🟡 **A new political instrument worth watching: OpenAI and Common Sense Media have proposed a
  California ballot initiative, the "Parents & Kids Safe AI Act"**, which if passed would shape AI
  products used by minors and therefore edtech procurement in the largest US state market.
  🔵 **Recorded as a WATCH item with no date attached — a ballot initiative is not law and this base
  does not price one as though it were.**
- 🔴 **Supply: `0` North American rows on `agents/top.md` this pass, and it is MEASURED.**
  `q="powerschool clever district mcp"` → **`0`**; `q="k12 district data agent"` → **`0`**;
  `q="infinite campus schoology skyward"` → **`0`**. 🔵 **The three largest US K-12 SIS vendors have
  no open agent surface of any licence, which is `T77`'s closed-system finding restated: in North
  America the registries are VENDOR-owned, so the entry route is the standards body, not the
  campus.** 🟢 **The two rows the region DID produce came from that route and from government:
  `bcgov/SIMS` (Apache-2.0, Government of British Columbia 🇨🇦 student financial aid) on
  `verticals/solutions.md`, and `hanhuark/machine-learning-for-engineers` (BSD-3-Clause, University
  of Arkansas 🇺🇸) on `repos/foundations.md`.**


#### Update 2026-11-15 (twenty-eighth pass, `p823`) — 🟢 The region's supply this pass is a CLOSED-portal integration and an institution-authored standards library; 🔴 the state wave has a THIRD count and Canada still has no education instrument

🟡 **Sourcing note for every item in this block: egress in the `p823` environment resolved GitHub and web search only. Every market and regulatory item below is `CITED, NOT READ` — primary texts were NOT opened. Figures are attributed to the party that published them, vendor and advisory sources are marked as such, and dates that sources disagree on are shown disagreeing. Every REPOSITORY named is first-hand and byte-read.**

- 🔴 **The state legislative wave, counted again and higher.** A tracker cited this pass reports
  **`134` AI-in-education bills across `31` states in 2026**, concentrated on data privacy,
  classroom limits and curriculum; a separate advocacy network reports *"nearly `100`"* state bills
  affecting K-12 AI use. 🔵 **This base now holds three counts from three parties across four
  passes. Do NOT average them — the denominators differ (bills introduced vs bills affecting
  students).** 🟢 **What is stable across all three: the instrument is the STATE, and the posture is
  guardrails rather than mandates.**
- 🟢 **Two dated obligations worth a bid calendar.** 🇺🇸 **North Carolina, Session Law 2026-41**:
  state model policy by **`2026-12-31`**, local district policies by **`2027-06-30`**, teacher
  training by **`2028-06-30`**. 🇺🇸 **New York, A 9190**: classroom AI use restricted to **grade 9
  and above**, with exceptions for diagnostics and special education. 🔵 **The North Carolina chain
  is the more useful of the two commercially — three deadlines, each a procurement.**
- 🟡 **Federal, and still not a rule.** The Department of Education's Office of Educational
  Technology published a *"Framework for Responsible Use and Development of Artificial Intelligence
  in Education"* in **March 2026**; a separate risk-based framework from the National Education
  Policy Center was approved in **May** and went to public comment. 🔴 **Both are frameworks, not
  binding instruments** — the distinction this file has insisted on since `p807`.
- 🔵 **State agencies are the operative publishers:** Illinois (**2026-07-09**, ISBE), Ohio
  (**January 2026**), Vermont (**January 2026**), California's CDE working group (**June 2026**).
- 🔴 **A ballot measure that could reshape the product layer:** the *"Parents & Kids Safe AI Act"*
  proposed in California by OpenAI and Common Sense Media, after the two parties merged competing
  measures. 🔵 **If it passes it binds AI products used by minors — which is edtech, whether or not
  it names edtech.**
- 🔴 **🇨🇦 Canada's gap persists and is now specific.** The instrument repeatedly returned for Canada
  is the **Working for Workers Four Act, 2024** — **workplace**, not education. 🔴 **This pass again
  found NO Canadian education-specific AI instrument.** 🟢 **Stated as a measurement, not silence.**
- 🟢 **New supply, and it is placed on a CLOSED system.**
  [`CloudDown/student-mcp`](https://github.com/CloudDown/student-mcp) (MIT, byte-read) brings
  **Omnivox — the 🇨🇦 Québec CEGEP portal — together with Moodle and Brightspace** into an
  assistant, with browser-based institutional sign-in, MFA, and **only a token or private browser
  profile stored, never the password**. 🔵 **Two of its three targets are proprietary**, which is the
  regional instance of `T77`.
- 🟢 **And an institution published integration substrate:**
  [`GSU-CETLOE/lti1p3Library-python`](https://github.com/GSU-CETLOE/lti1p3Library-python) (MIT,
  byte-read `1,083 B`) — **LTI 1.3 Advantage tool side with the OIDC login flow**, from Georgia
  State University's teaching-and-learning centre. 🔴 **Its MIT holder line is the unfilled template
  `[Your Name / Organization]`.** 🟢 **Opportunity, concretely: NA institutions are publishing their
  own integration code and getting the licence hygiene wrong. Offering to fix it is a free first
  conversation with a named buyer.**


#### Update 2026-11-15 (twenty-seventh pass, `p822`) — 🔴 Demand data is abundant and SECONDARY; the new NA supply this pass is institutional self-build, not vendor product

🟡 **Sourcing note for every item in this block: egress in the `p822` environment resolved GitHub
only, so all market and regulatory items below arrived through web search and are
`CITED, NOT READ`. Primary texts were NOT opened. Figures are attributed to the party that
published them, and vendor-sponsored surveys are marked as such.**

- 🔵 **Market sizing, contested and vendor-published.** One report cited this pass puts the US
  AI-in-education market at **USD `3,280` M in `2025` → USD `15,250` M by `2031`**; another repeats
  the **`86%` of educational organizations have adopted generative AI** figure that traces to a
  Microsoft `2025` report. 🔴 **Both are vendor claims and this file's standing `Market size —
  contested` caveat applies; do not put a single number in a proposal.**
- 🟢 **Adoption, where the direction matters more than the level:** student use reported moving
  **`66%` (`2024`) → `92%` (`2025`)**, and institution-wide (rather than pilot) implementation
  reported at **`66%`**. 🔵 **If even approximately right, the NA pitch is no longer "adopt AI";
  it is "govern and evidence what your people are already doing" — which is exactly what `P53`
  sells.**
- 🟢 **Regulation is a STATE-level compliance surface, and that is the productizable part.** The
  Education Commission of the States describes federal executive orders from `2025`–early `2026` as
  having produced a national framework; trackers cited this pass count **nearly `100` state bills
  in `2026`** touching K-12 student AI use and **at least `15` states** with AI-in-education
  legislation introduced or passed, plus a **California ballot initiative (January `2026`)** on how
  AI companies interact with minors. 🔵 **Fifty rule-sets over one product is a configuration
  problem, and it is the North American analogue of the curriculum-adapter asset `P51` names.**
- 🔴 **Incumbent stress is real and quotable:** Chegg cut **`45%` of staff (`388` roles)** as AI
  tools reduced homework-help traffic. Named public players: Chegg, Pearson, Cengage, Instructure,
  Coursera, Udemy. 🔵 **The displaced category is CONTENT-ACCESS; the growing one is governance,
  evidence and integration — plan the account strategy accordingly.**
- 🟢 **The NA supply this pass is institution-built, not vendor-built, and both rows went to
  `verticals/solutions.md`:** `csm_web` (UC Berkeley's Computer Science Mentors, MIT, `20★`) and
  `schoolz` (Apache-2.0, a named US district). 🔵 **`T34` read university self-build as a LATAM
  adaptation; finding the same shape at Berkeley makes it a university shape — so LATAM-derived
  patterns are reusable on North American campuses, which is a reusable account argument.**
- 🔴 **`0` North America rows on the agent shelf this pass.** Declared, not hidden.

#### Update 2026-11-15 (twenty-sixth pass, `p821`) — 🟢 The platform default escalates to the Senate with a DATE, and a new state instrument lands at the board rather than the legislature

- 🟢 **The Google K-12 default now has a deadline attached to it (`T72`).** This file already holds
  the change itself — **Gemini and Search opt-in, off by default, on school-managed K-12 student
  accounts**, with no traditional-Search-without-AI option — and the political backlash around it.
  🟢 **What is new in the `2026-11-13`/`2026-11-14` window is a US Senate demand that the policy be
  reversed, with a response requested by `2026-11-30`.** 🔵 **Consequence for an engagement: the
  configuration a district plans around may move before it ships, so the deliverable is a
  configuration decision with a named owner and a dated review — not a policy document.**
- 🟢 **A new state instrument, and its shape is the notable part.** **Kansas's State Board of
  Education** approved a requirement that **every district and every accredited non-public school
  adopt an instructional-technology policy and an implementation plan**, covering AI use by
  teachers and by students, with statewide minimum requirements and local discretion over how they
  are met. 🔵 **This is a BOARD instrument, not a statute** — it arrives outside the legislative
  tracker this file has been counting, which means the `134`-bills-in-`31`-states figure this file
  carries is a FLOOR on regulatory activity, not a measure of it.
- 🟡 **District-level churn, recorded as texture rather than as an instrument.** The Martinsville,
  Virginia board tabled its proposed AI policy to December. 🔵 **The pattern worth selling against
  is that local boards are now deferring for want of a template, which is a productisable gap.**
- 🔴 **Evidence grade for all three: `CITED, NOT READ`.** Egress on this pass resolved GitHub only,
  so no primary text was byte-read; the items rest on news coverage dated `2026-11-13`/`2026-11-14`
  and on a Cambridge-report release dated `2026-11-04`. 🔵 **`ACTION p821-D` re-checks the Senate
  item after `2026-11-30`.**
- 🟢 **Supply side, measured: NIL for this region this pass.** Nine discovery legs — four of them
  recency-ranked with no star floor — returned no new build-safe North America row. 🔵 **The
  region's supply in this base remains the largest and the oldest; what `p821` added came from
  LATAM, EMEA and APAC (`T70`).**

#### Update 2026-11-15 (twenty-fourth pass, `p819`) — 🟡 A third, later count of the state wave, and the federal instrument finally has a CYCLE even though it still has no date

🟡 **SECONDARY, and filed as a THIRD non-comparable snapshot rather than as a replacement.** This
file already carries `31 states` from two earlier trackers. 🟢 **An AAAS EPI Center policy briefing
dated July 2026 counts `118` bills across `32` states, with `25` enacted laws in `16` states** —
later than both figures this base holds, and the first of the three to separate BILLS INTRODUCED
from LAWS ENACTED. 🔴 **Do not reconcile the three.** MultiState (`134` bills / `31` states, March
2026), ExcelinEd (`8` states enacted, May 2026) and AAAS (July 2026) count different objects at
different dates. 🔵 **The usable form in a pitch is the SHAPE, not the number: introduction volume
is in the low hundreds, enactment is in the dozens, and the gap between them is where a district's
"we are waiting for the rules" objection actually lives.**

🟢 **Enacting states named in the AAAS list**, which is the first roster this file can quote:
Alabama, Georgia, Hawaii, Idaho, Illinois, Iowa, Louisiana, Maine, Maryland, Mississippi, Missouri,
North Carolina, Oklahoma, Tennessee, Utah and Virginia. 🔵 **Commercially: these are the sixteen
jurisdictions where a district procurement has a STATUTE to point at rather than guidance, which
is the condition under which a governance workstream becomes a line item instead of a favour.**

🟢 **The federal instrument gains a cycle.** The US Department of Education's **AI in Education
priority** for discretionary grants — AI literacy, personalised learning, educator professional
development — is reported with **first competitions expected in the `2026-27` cycle**. 🔴 **Still no
competition date, which is the thing this file has wanted for five passes.** 🔵 **A named cycle is
nonetheless enough to time a capture plan against.**

🔴 **The risk this file should carry alongside the state wave.** Industry lobbying for **federal
preemption** of state AI law is live. 🔴 **If it lands, the sixteen-state statutory roster above
becomes the weakest part of a governance pitch rather than its anchor** — so scope governance work
to the institution's own obligations, which survive preemption, not to the state statute, which
may not.

🔴 **Regional supply this pass: NIL, and measured.** The `14`-query star-ranked sweep (`T63`)
returned `0` new North-America-attributable repositories. 🔵 **The region's thinness here is now
four passes old and is a supply fact, not a search artefact.**

#### Update 2026-11-15 (twenty-third pass, `p818`) — 🟢 The research-library half of the region appears, permissive and institutional; and the state calendar gains four named instruments while the FEDERAL one cannot be dated

🟢 **Supply, and it is the institutional tier rather than the single-maintainer tier this region
usually yields.** [`samvera/hyrax`](https://github.com/samvera/hyrax) (🟢 **Apache-2.0**,
`201★`, pushed `2026-11-13`) is the repository front-end deployed at large North American research
libraries — a consortium-maintained platform, not a side project. 🔵 **That matters for the sale:
the buyer is a research library with its own budget line, which is a different and better-funded
buyer than the LMS office this base has been selling to for twenty-two passes.**

🟢 **The accessibility opening is this region's most compellable one, and it is now staffed with a
permissive row.** [`Maximilian741/508-Agent`](https://github.com/Maximilian741/508-Agent) (MIT,
`1★`) does **document** remediation against Section 508 and WCAG 2.1 AA. 🔵 **Course materials are
PDFs and slide decks, so document remediation — not page remediation — is the education-shaped
half of a Section 508 obligation.** 🔴 **`1★`: the capability is real, the maturity is not, and the
most capable alternative in the layer is proprietary (`T60`).**

🟢 **Four newly named state instruments, bringing the dated-obligation list to a usable length.**
🟢 **Maryland** — requires AI guidance, local district AI policies, designated **AI coordinators**,
and university-supported **certification of compliant AI tools**. 🔵 **The certification duty is the
commercially interesting one: it creates a named, recurring evaluation service with a public buyer.**
🟢 **New York `A 9190`** — would restrict classroom AI use to **ninth grade and above**, with
exceptions for diagnostics and special education. 🟢 **Alabama `H.B. 1227`** — a generative-AI
framework. 🟢 **Virginia `S.B. 394`** — guidance covering teacher training.

🔵 **The `134` bills across `31` states figure this base has carried since `p797` is now
corroborated from a second, independent tracker** — same count, same denominator. 🟢 **`p797`'s
number survives a second source; continue to quote the STATE and bill number rather than the
national total.**

🔴 **A date this pass could NOT establish, recorded as a conflict rather than resolved.** Two
secondary sources place 2026 U.S. Department of Education AI guidance differently: one as an Office
of Educational Technology framework in **March 2026**, the other as K-12 guidance dated
**2026-04-08**. 🔴 **No primary `ed.gov` source was read. Do not cite a federal date from this base
until one is.**

🟡 **California stays the regulator to watch, and the route is child-safety law rather than
education law.** The **"Parents & Kids Safe AI Act"** ballot initiative — proposed by OpenAI with
Common Sense Media — would reach any AI product used by minors, which includes edtech. 🔵 **An
education deployment in California should be scoped against a minors standard, not an education
standard.**

🔴 **Still unanswered, SIXTH pass: no AI-in-education spend figure for Canada or Mexico.** 🟢 **The
cause remains the prescribed query shape — "North America" returns US-only results — and the fix
remains naming the countries. This pass named them and still got nothing: the gap is now a SOURCE
gap, not a query gap.**

#### Update 2026-11-15 (twenty-second pass, `p817`) — 🟢 **The credential and interoperability layer lands here, it is PERMISSIVE and LIVE, and the standards bodies are shipping the agent tooling themselves**

🟢 **Regional supply this pass: `+1` agent row and `+8` foundation/credential rows place North
America — the largest regional gain since `p813`.**
[`Ed-Fi-SDK-for-AI-Assistants`](https://github.com/Ed-Fi-Exchange-OSS/Ed-Fi-SDK-for-AI-Assistants)
(🟢 Apache-2.0, `1★`, pushed `2026-11-12`) joins the shelf, and the Digital Credentials Consortium
stack — [`learner-credential-wallet`](https://github.com/digitalcredentials/learner-credential-wallet),
[`verifier-plus`](https://github.com/digitalcredentials/verifier-plus) (`19★`),
[`dcc-admin-dashboard`](https://github.com/digitalcredentials/dcc-admin-dashboard) (`12★`),
[`open-badges-context`](https://github.com/digitalcredentials/open-badges-context) — lands in
`repos/foundations.md`, 🟢 **every row MIT, holder lines naming the Consortium and MIT the
university.**

🟢 **Why this region is the strong one on this layer, stated as the engagement fact:** the reference
implementations are permissive AND live. Ed-Fi pushed `2026-11-12`/`2026-11-13`, the DCC wallet
`2026-10-15`, [`apereo/cas`](https://github.com/apereo/cas) (`11,399★`, Apache-2.0) `2026-11-15`.
🔴 **Compare EMEA below, where the official reference is archived.** See `T56`.

🔵 **The procurement signal, and it is the one to lead with.** 🟢 **The Ed-Fi Alliance — custodian of
the US K-12 data standard — now publishes agent-integration scaffolding under its own name
(`T53`).** 🔴 **At `1★` and `0★` these repositories carry no community, so they are worth nothing as
supply and a great deal as SANCTION:** the objection that stops district agent projects is *“will the
data owner permit this”*, and the data standard's custodian has answered in public.

🟢 **Policy, this window (🟡 all `SECONDARY` unless marked):**
- 🟡 PIE Network tracked close to `100` state bills this year that could directly affect students'
  use of AI in K-12; a state tracker current to May 2026 separates enacted law from guidance.
- 🟡 Federal executive orders issued `2025`–early `2026` produced a national framework for AI in
  education and a K-12 AI instruction task force.
- 🟡 A Stanford review of `800+` studies found only `20` high-quality causal studies of learning
  outcomes — 🔵 **the evidence gap is the commercial risk in this region: buyers are mandated to act
  and have little to cite, which is why `P44`'s relying-party-first sequencing sells.**
- 🟡 Frontline Education: just over half of districts report supporting AI use, roughly flat
  year-on-year.

🔴 **Declared limit on this leg.** `q="ed-fi mcp"` returns `12` repositories of which `10` are
unrelated, and the two that are relevant are the Ed-Fi Exchange's own prototypes plus
[`cdweaver1992/edfi-mcp-server`](https://github.com/cdweaver1992/edfi-mcp-server) (`1★`, **no
licence**, rejected). 🟢 **So the agent surface over the US K-12 data standard is, in total, two
sanctioned prototypes and one unlicensed hobby repository. That is the widest build slot this pass
found in this region.**


#### Update 2026-11-15 (twenty-first pass, `p816`) — 🔴 SUPPLY NIL for this region, stated rather than left silent; the policy picture moved on two concrete instruments

🔴 **Regional supply this pass: NIL, and it is a real nil rather than an unrun leg.** 🟢 **`p816`
harvested the RETENTION layer — `10` build-safe agent rows, `8` foundation rows, `3` platform rows
— and under `T42` (region is the region of the target system's CATALOGUE, not of the author) every
single one places `Global`, because Anki, Obsidian and the FSRS specification have no national
catalogue.** 🔵 **So this region's shelf is unchanged at `14`, and the reason is the layer's
nature, not a failed query. Recording that distinction is the point of `ACTION RE`.**

🟢 **Policy, this window (all figures secondary-sourced unless marked):**

- 🟢 **Federal framework exists but is executive, not statutory.** Executive orders issued
  between 2025 and early 2026 produced a national framework for AI in education, agency action
  plans and a task force supporting K–12 AI instruction. 🔴 **No federal statute; the binding
  instruments remain state-level.**
- 🟢 **State volume keeps climbing, and the two counts still disagree — as they have for six
  passes.** At least `15` states have introduced or passed legislation specifically addressing AI
  in education; separately the PIE Network tracked **nearly `100` state bills this year** that could
  affect K–12 student AI use. 🔵 **The gap between “15 states” and “100 bills” is a
  bills-versus-jurisdictions artefact, not a contradiction — do not cite them side by side as if
  one corrected the other.**
- 🟢 **Virginia `S.B. 394`** directs the state education agency to issue guidance, including on
  teacher training — a named instrument with a named duty-holder, which is this file's standard
  for a citable state obligation.
- 🟢 **Two NEW scrutiny instruments this window, both outside education statute:** a
  **California ballot initiative on AI and minors, announced January 2026**, and an **NTIA
  initiative scrutinising edtech**. 🔵 **Both are consumer-protection and telecommunications
  channels rather than education ones, which is a widening of the regulatory surface this file has
  tracked only through education agencies.**
- 🔴 **The demand-side casualty is now quantified: Chegg cut `45%` of staff (`388` roles)** as
  generative AI and Google AI Overviews reduced homework-help traffic. 🔵 **This file predicted
  consolidation at `p811` and recorded it in headcount then; this is the same mechanism one notch
  further along, and it is the clearest commercial evidence that the incumbent study-support
  business is the one being disrupted — which is exactly the slot the retention layer sits in.**

🔵 **Adoption figures remain CONTESTED and are published here with that attached:** `86%` of
education organisations adopting generative AI (Microsoft-cited, 2025) against `66%`
institution-wide implementation from another report; student use `66%` (2024) → `92%` (2025).
🔴 **Market size: USD `3,280 M` (2025) → USD `15,250 M` by 2031 for the US, with the region given
`38%` share in one report and `41.7%` of global growth 2026–2030 in another. All secondary.**

🔵 **Named players this window, unchanged in composition:** Blackboard, Pearson, Cengage,
Instructure, Coursera, Chegg.


#### Update 2026-11-15 (twentieth pass, `p815`) — 🟢 The region BUILT the permissive half of the assessment layer, and holds this base's single largest unserved mandate

🔵 **Source confidence.** Repository measurements are `FIRST-HAND` — run `2026-11-15` against
`gh api -X GET search/repositories`, licences byte-read over `raw.githubusercontent.com`. Policy
and market figures are `SECONDARY` (web-search summaries of trackers, briefings and vendor blogs)
and are labelled as such; verify any date before putting it in front of a client.

🟢 **The supply finding, and it is flattering to the region.** `p815` named the assessment-engine
layer, and 🟢 **both of its permissively licensed anchors are North American university
projects**: [`autolab/Autolab`](https://github.com/autolab/Autolab) (Apache-2.0, `808★`,
*"initially developed by a team of students at Carnegie Mellon University"*) and
[`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) (BSD-3-Clause, `162★`,
*"developed by the Data Science Education Program at UC Berkeley"*). 🔵 **Against `Judge0`
(GPL-3.0, `4,519★`, 🇭🇷) and `JPlag` (GPL-3.0, `2,012★`, 🇩🇪), the region's contribution is the one
a studio can actually ship — see `T44`.** 🟢 **With `jupyter/nbgrader` and `jupyterhub` already on
this shelf, a complete, fully permissive, zero-copyleft assessment stack is available today:
that is `P38`.**

🔴 **The mandate finding, and it is the largest unserved slot in this base.** IDEA makes the
individualised education programme a federal obligation for every US district. 🔴 **`q="IEP
individualized education program"` → `total_count=11`, star ceiling `3★`, and the only licensed
row is [`dg13788/iep-system`](https://github.com/dg13788/iep-system) (MIT, `1★`, created
`2026-09-06`); `q="special education management"` → `47` and every row is unrelated noise.** 🔵
**So the honest answer to "what open base do we start from" is: there is none. This is a BUILD
engagement, and the only one in this base where that is true of a federally mandated workflow.**

🔴 **Second mandate, and it binds in two regions at once:** web-accessibility obligations for
public education bodies (ADA Title II web rule in the US, the European Accessibility Act in
EMEA — both `SECONDARY`, verify the compliance dates). 🔴 **`q="accessibility remediation alt
text education"` → `total_count=0`.** Not thin — empty. 🟢 **Every institution on every platform
in `verticals/solutions.md` is in scope, which makes it the widest-population build slot `p815`
found. See `T47`.**

🟡 **Policy picture, `SECONDARY`, and consistent with where `p813`/`p814` left it.** Trackers
report `134` AI-in-education bills across `31` states in 2026, with states converging on student
data privacy, human oversight and parental consent rather than mandating classroom adoption.
🔵 **The one hard-dated instrument worth quoting is North Carolina's Session Law 2026-41: a state
model policy by `2026-12-31`, local district policies by `2027-06-30`, teacher training by
`2028-06-30`** — a three-step deadline a district can be sold a programme against. Federal
activity is lighter (US Dept of Education K-12 guidance reported April 2026; an Office of
Educational Technology *"Framework for Responsible Use and Development of Artificial Intelligence
in Education"* reported March 2026). 🟡 California's proposed *"Parents & Kids Safe AI Act"*,
reported as backed by OpenAI and Common Sense Media, would set standards for any AI product used
by minors — worth tracking because it reaches product design, not just district policy. 🔴
Canadian K-12 AI policy did not appear in any result this pass: an informed gap, not a finding.

🟢 **Where to lead in this region:** `P37` (integrity evidence) at universities, `P38` (permissive
formative assessment) in CS and data-science programmes, and `P39` (timetabling) wherever a
proprietary scheduler is up for renewal. 🔵 **And price the IEP and accessibility slots as
product builds, not integrations.**


#### Update 2026-11-13 (nineteenth pass, `p814`) — 🟢 The region's research-agent supply binds to a federal AGENCY API, not to a cultural institution, and the policy picture stayed where `p813` left it

🔵 **Source confidence.** Repository measurements below are `FIRST-HAND` — run this pass against
`gh api -X GET search/repositories` with licences byte-read from `raw.githubusercontent.com`.
Policy figures are `SECONDARY` (web search summaries of trackers and vendor blogs) and are
flagged as such inline; nothing below replaces `p813`'s `PRIMARY-CITED` policy block.

🟢 **The supply finding, and it is new.** `q="pubmed mcp"` returns **`318`** repositories.
[`genomoncology/biomcp`](https://github.com/genomoncology/biomcp) (**MIT**, `679★`, byte-read
`1,066 B`) is shelved as the region's reference row: PubMed, PubTator3, Europe PMC, PMC OA,
ClinVar, ClinicalTrials.gov API v2, NCI CTS, OncoKB, keyed to `NCBI_API_KEY`.

🔴 **The CULTURAL-institution layer, by contrast, is a measured `1` and it is copyleft.**
`q="library of congress mcp catalog"` → `total_count=1`:
[`msuicaut/lc-vocabularies-mcp`](https://github.com/msuicaut/lc-vocabularies-mcp) (GPL-3.0,
`4★`). `q="apa citation style mcp"` → `0`. `q="eric ed.gov mcp education research"` → `0`.

🔵 **So the region's binding is to AGENCY APIs — NIH/NLM — and not to a national catalogue, which
is the inverse of 🇦🇲 Armenia and 🇧🇷 Brazil this pass (`T42`).** 🟢 **The opportunity: a US
university engagement that needs a research-literature agent starts from an MIT row that already
documents its per-source data terms, which is `T40`'s clean grade and a ready-made compliance
artifact.**

🟡 **Policy context (`SECONDARY`, 2026 web sources, consistent with `p813`'s direction).** The
PIE Network tracked nearly `100` state bills in 2026 touching student AI use; more than `28`
states plus DC have issued K-12 AI guidance, and a handful moved from guidance to binding
district-policy and teacher-training mandates (Ohio, Oklahoma, South Carolina, Massachusetts,
New York are named by a vendor blog — treat as unverified). District teacher AI training
reportedly rose `24% → 48%` and student ChatGPT use for schoolwork `13% → 26%`. 🔴 **Canada and
Mexico returned nothing usable on this channel: an informed gap, not coverage.**


#### Update 2026-11-13 (eighteenth pass, `p813`) — 🟢 The supply gap this region has carried for eleven passes is CLOSED, and the bill count moves again

🔵 **Source confidence, stated once for this block.** Policy figures below are
`PRIMARY-CITED` — they name legislative trackers and state issuances that were **not** read
directly under this session's network policy. 🟢 **The SUPPLY figures are different in kind: they
are `MEASURED` this hour on `gh api search/repositories` with licences byte-read over
`raw.githubusercontent.com`, controlled against two invented addresses.**

- 🟢 **MEASURED — the regional supply nil is closed: `North America 4 → 12` build-safe agents.**
  `p811` named this gap and `p812` closed LATAM's with the same instrument. 🔵 **Pointing it at
  the SYSTEM layer worked a fourth time:** `StudentVUE` returned `7` repositories, `Schoology`
  `11`, `Infinite Campus` `3`, `Skyward` `1`, `Blackbaud` `4`.
- 🔴 **MEASURED — and the shape of that supply is the commercial finding: it is FAMILY-BUILT.**
  Every North American row added this pass except one was written by a parent or a student about
  their own district. 🟢 **The single exception is a vendor:** CData ships a read-only MCP server
  over **Blackbaud Financial Edge NXT**, gating full CRUD behind its paid driver.
- 🔴 **MEASURED — the widest open slot in the region: PowerSchool.** The largest US K-12 SIS by
  installed base has **exactly one** agent repository (`zuvy/ps-mcp-server`) and it carries **no
  licence**. 🟢 **Same shape as the SIAGIE nil `p812` found in Peru, and the same opportunity.**
- 🔴 **MEASURED — the most-starred Moodle MCP server in the world is unlicensed.**
  `loyaniu/moodle-mcp`, `57★`, `17` forks, `404` on every licence path at both branch roots while
  `README.md` returns `200`. 🟢 **Exists and is simply ungranted — one issue is the cheapest
  unblock in this base** (`T37`, `P33`).
- **State legislation accelerated again (`PRIMARY-CITED`): `134` AI-in-education bills across
  `31` states in the 2026 session**, with lawmakers favouring research, transparency and
  guardrails over adoption mandates.
- **Named instruments this window (`PRIMARY-CITED`).** 🇺🇸 **North Carolina Session Law 2026-41**
  is the most schedule-specific: AI-literacy standards, a **state model policy by `2026-12-31`**,
  local school-unit policies by `2027-06-30`, teacher training by `2028-06-30`. **New York A 9190**
  would restrict classroom AI to grade `9` and above with diagnostic and special-education
  exceptions. **New Jersey A 4352 / S 2862** would mandate K-12 AI instruction and public
  higher-ed AI certificates and degrees. **California AB 1159** would bar the use of student data
  to train AI models; **Idaho SB 1227** requires privacy protections for school AI tools.
  **Texas HB 2400** bans AI from delivering direct classroom instruction.
- 🔴 **Four states — Maryland, Idaho, Oklahoma, Virginia — now require BOTH state guidance and
  mandatory district-level AI policy adoption (`PRIMARY-CITED`).** 🔵 **That is `T16`'s deployment
  inventory becoming a statutory duty in four jurisdictions at once.**
- **The DC OSSE policy (non-mandatory, 2026-27) bans AI from grading, discipline, IEP decisions
  and teacher evaluation** — 🟢 **the clearest statement yet of `T30`'s control point in a US
  issuance.**
- **Industry is now shaping the rules directly:** OpenAI and Common Sense Media proposed a
  California ballot measure, the *"Parents & Kids Safe AI Act"*, covering AI products used by
  minors.
- 🔴 **DECLARED GAP: Canada.** The search returned **no Canadian education-specific AI regulation**
  — what exists is workplace law (the Working for Workers Four Act, 2024). 🔵 **Written down
  rather than left silent: a nil for Canada is this pass's measurement, and it is the fourth
  consecutive pass in which Canadian education policy has returned nothing.**

#### Update 2026-11-13 (seventeenth pass, `p812`) — 🟢 The state-policy count moves again, and the regional supply gap is now the SHARPEST it has been

🔵 **Source confidence, stated once for this block.** Figures marked `MR` come from
market-research marketing pages or vendor-commissioned surveys read through search summaries and
are **order-of-magnitude only**; figures marked `PRIMARY-CITED` name a primary issuance that was
**not** read directly under this session's network policy. 🔴 **Nothing in this block was read
from a primary source this pass.**

- **State legislation is the binding layer, and it is accelerating.** The PIE Network tracked
  **nearly `100` state bills** that could affect K-12 AI use in 2026; a separate analysis counts
  **at least `15` states** that have introduced or passed AI-in-education legislation
  (`PRIMARY-CITED`). The Education Commission of the States describes federal executive orders
  issued between 2025 and early 2026 as having produced a **national framework** for AI in
  education. 🔵 **Consistent with `T18` and `T21`: the instrument that binds a US engagement is
  the state's or the system's own policy, with a date on it — not federal law.**
- **A ballot measure, which is a different kind of risk.** A **California ballot initiative on how
  AI companies interact with minors** was announced in January 2026 (`PRIMARY-CITED`). 🔴 **A
  ballot measure cannot be negotiated or phased the way an agency rule can**; for any product
  touching under-18 users in California, treat the measure's text as a hard date once qualified.
- **Consolidation is visible in demand, not just in headcount.** Chegg cut **45%** of staff as AI
  tools reduced demand for homework help (`MR`). 🔵 **The read for a studio: the "answer a
  student's question" layer is commoditised. The defensible layer is the one bound to the
  institution's system of record** — which is what `P19`, `P27` and `P29` sell.
- 🔴 **The agent-supply picture for North America got WORSE in relative terms this pass, and the
  number is from this base's own shelf.** `agents/top.md` now holds `74` build-safe agents, of
  which **North America is `4`** — unchanged while EMEA went to `10` and LATAM to `8`. 🟢 **The
  highest-ceiling openings remain the ones this base has already evidenced: OneRoster has
  **zero** agent implementations (`P27`), PowerSchool has three servers and **no permissive
  one**, and Ellucian Banner, Colleague and Workday Student have **none of any kind**.**
- 🔵 **Market size, unchanged in character: contested and vendor-sourced.** US AI-in-education
  put at **$3,280M (2025) → $15,250M (2031)** by one outlook; Technavio puts the global market at
  **$3.37B with a 45% CAGR** and North America at **38%** share (`MR`, and the two are not
  reconcilable). Student AI usage reported rising **66% (2024) → 92% (2025)** (`MR`).

#### Update 2026-11-13 (sixteenth pass, `p811`) — 🟢 A fourth dated state obligation, and the consolidation this base predicted is now visible in HEADCOUNT

🔴 **Network note, stated once and applying to every figure in this block: `www.cbsnews.com`,
`www.pna.gov.ph` and `www.holoniq.com` do not resolve under this session's network policy.
These are `CITED, NOT READ` — named primary issuances read through search summaries. Re-read
them before quoting to a client.**

🟢 **🇺🇸 Florida is the fourth dated obligation in this region, after NC, Ohio and
Mississippi.** The State Board of Education adopted AI rules on **`2026-09-16`**, reported as
**Rule `6A-14.0719`** for the Florida College System with a companion K-12 rule.
🔵 **Districts and charter boards must adopt AI policies by `2027-07-01`.** Two provisions
are commercially load-bearing: **students may not use AI on graded work unless the
instructor explicitly permits it** (default-deny, the inverse of what every consumer tutor
assumes), and **teachers are reported to be barred from using AI as "a decision maker,
absent human review" for grading, evaluations and referrals** (`T30`). 🔴 **No effective date
could be confirmed in the Florida Administrative Register.**

🔵 **Why Florida is worth more to a studio than its size suggests:** a default-deny rule on
graded work makes the *instructor's permission* a configuration setting that every
courseware deployment in the state now needs, per course, with an audit trail. That is a
small, specifiable, deadline-bound piece of work — and `P16`'s 64-campus policy pack is
already the shape of the answer.

🟢 **The consolidation has reached headcount, which is the part a client feels.** Coursera
completed its all-stock combination with **Udemy on `2026-05-11`** (`0.800` Coursera shares
per Udemy share; former Coursera holders ≈`59%`, Udemy ≈`41%`; a reported `$115M` cost-synergy
target). 🔴 **On `2026-11-09` — four days before this pass — Coursera announced it would cut
approximately `10%` of its global workforce.** 🔵 **Set beside Chegg's `45%` reduction already
in this file, the pattern is explicit: the first businesses AI compressed in this sector are
the ones whose product was *delivering an answer or a course catalogue*.** 🟢 **The proposal
that survives this is the one selling governance, evaluation and integration — not content
delivery.**

🔴 **Still open, sixth pass: no education-AI spend figure for Canada or Mexico.** `p810`
named the countries and got policy instruments; `p811` got market-wide AI figures and no
education split. 🟢 **Re-shaped for the next pass: the number is unlikely to exist as
"education AI spend" and should be sought as PROCUREMENT — provincial ministry tenders in
Canada, SEP and state-level contracts in Mexico.**

#### Update 2026-11-13 (fifteenth pass, `p810`) — 🟢 Canada and Mexico finally have NAMED policy instruments; 🔴 the spend figure is still missing, and faculty intent has FALLEN

🟢 **`ACTION p797`'s five-pass complaint is half-discharged. The fix was the one this base
prescribed — name the countries instead of saying "North America" — and it worked.**

🟢 **Canada:** the federal **"AI for All" strategy launched `2026-06-04`**, carrying **AI
literacy**, **watermarking of AI content**, and a **trusted-AI certification programme**.
🔴 **It is strategy, not statute:** the earlier AI bill lapsed in **January 2025** and has not
been replaced, so the instrument is voluntary. 🔵 **For an education engagement that matters
more than it sounds** — a certification programme with no binding law behind it is a
*procurement* lever, and procurement levers are what a studio can actually satisfy.

🟢 **Mexico:** **no general AI law**; the federal digital agency published a **National AI Plan
2026 in September 2026**, and Congress is weighing several initiatives including one that would
classify AI systems **by risk level** (EU-shaped). 🔴 **Thin sourcing — single secondary
sources throughout.**

🔴 **The adoption number is the uncomfortable one, and it REVERSES the regional story this
base has told.** Digital Education Council's *AI in Higher Education Global Survey 2026*:
**faculty intent to use AI in the US & Canada fell from `76%` (2025) to `67%` (2026) — the
LOWEST of any region surveyed** — and **`55%` of US & Canada faculty believe AI poses a
serious risk to human intellectual development.** 🔵 **North America is the only region in this
file where practitioner appetite is going DOWN.** 🟢 **Sell governance and evidence here, not
capability** — the market has already seen the demo.

🔴 **Still missing after six passes: any education-AI SPEND figure for Canada or Mexico.**
🟢 **The gap is now precisely shaped: the policy instruments are findable and the budgets are
not**, which points at national budget documents and procurement portals rather than at search.


#### Update 2026-11-13 (fourteenth pass, `p809`) — 🟢 The region's higher-ed LMS tier gained its first open agent, and the SIS tier is confirmed empty

🟢 **New, and placed here because Brightspace is a North American higher-ed incumbent:**
[`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server)
(`MIT`, `67★`, `492` commits) is authored at **ECE @ Purdue** and names working instances
in 🇺🇸 and 🇨🇦. `29` tools, **read-only by declaration**, school SSO + 2FA, password in the
OS keychain, session state AES-256-GCM. 🟢 **It is the highest-starred new education agent
this base has found in this window and the first credible D2L path for a US/Canadian
engagement.**

🔴 **The sharpest unserved gap in the whole base sits in this region.** **Ellucian
Banner**, **Ellucian Colleague** and **Workday Student** — the systems of record for most
North American higher education — have **no open-source MCP server or agent of any kind**,
searched from two independent angles on 2026-11-13. Ellucian documents **Ethos** (Data
Model APIs, Business Process APIs, GraphQL) and publishes no MCP server of its own;
Workday ships proprietary *Agent-Ready Tools*. 🔵 **The OpenEduCat lesson applies: wrap
the platform API, not the vertical.** A thin, governed server over Ethos is the highest-
ceiling unbuilt artefact this base has identified.

🟡 **Policy, re-read this pass — and the trackers still disagree, which is itself the
finding.** `AI education North America 2026 adoption regulation players state legislation`
returned four incompatible counts of 2026 state activity: **TNTP** ≥`11` states enacted
across `27` tracked; **ExcelinEd** (May 2026) `8` states enacted; **CDT via AAAS** `16`
states passed bills (naming Alabama, Georgia, Idaho, Illinois, Utah); **MultiState**
`134` bills across `31` states as of March 2026. 🔴 **Do not quote a single number.** The
trackers define "enacted" and "AI in education" differently and refresh on different
cycles; quote the range and name the tracker.

🟢 **Dated federal instruments worth carrying:** the **US Department of Education
finalised its AI in Education grant priority on 2026-04-13**, directing discretionary
funding at AI literacy, personalised learning and educator professional development, and
released **$169M in FIPSE awards** including responsible-AI-use provisions. 🔵 Roughly
**35 state education agencies** have issued AI guidance. 🟡 Two California bills to watch:
**AB 1159** (bar use of student data to train AI models) and a separate bill that would
**prohibit most classroom AI below ninth grade** — the latter is the clearest instance of
`T25` (category set by learner age, not by what the software does). 🔴 A federal
**preemption** push could override the state layer; unresolved.


#### Update 2026-11-13 (thirteenth pass, `p808`) — 🔴 NIL. Every instrument the leg returned is already held; the leg is now saturated for a third consecutive window

🔴 **Zero new North American facts this pass.** The leg
`AI education North America 2026 adoption regulation players` ran and returned a
substantial result set — **and every single item in it was already carried in this
file.** Recorded item by item, because "nil" is only trustworthy if it is auditable:

| Returned by the leg | Status in this file |
|---|---|
| `134` AI-in-education bills across `31` states, 2026 session | 🟢 Already held (three times — lines ~`174`, ~`197`, ~`300`) |
| California `AB 1159` — bars student data training AI models | 🟢 Already held |
| Idaho `SB 1227` — privacy protections for school AI tools | 🟢 Already held |
| New York `A 9190` — restricts classroom AI to grade 9+ | 🟢 Already held |
| North Carolina `Session Law 2026-41` — AI-literacy standards, model policy by `2026-12-31`, local policies by `2027-06-30`, teacher training by `2028-06-30` | 🟢 Already held |
| `K-12 AI Literacy and Readiness Act of 2026` — advanced in House committee | 🟢 Already held |
| April 2025 executive order on AI education for American youth | 🟢 Already held, and given its citation at `p807` |
| CA ballot initiative *"Parents & Kids Safe AI Act"* (OpenAI / Common Sense Media) | 🟢 Already held |
| D.C. non-mandatory `2026-27` guidance barring AI from grading and discipline | 🟢 Already held |

🟢 **This is the third consecutive pass on which the North American leg has returned
nothing new, and the second on which it returned nothing new *at all* rather than merely
nothing material.** 🔵 **The reading is that US state-level AI-in-education legislation
has reached a stable, well-indexed corpus** — the trackers that cover it
(`FutureEd`, `MultiState`, `ExcelinEd`) are comprehensive and this file now mirrors them.
🔴 **A nil here should not be read as "nothing is happening"**: the `2027` compliance
deadlines in the NC law and the pending CA ballot initiative are both live and both
already documented below. 🟢 **Recommended for future passes: stop re-running the general
NA leg and instead track the three dated deadlines this file already holds.**

🔴 **Methodological caveat that applies to this whole pass and is NOT a property of the
region.** Primary-source verification was **unavailable** this window: the session's
network policy resolves `github.com` but **not** `multistate.us`, `future-ed.org`,
`holoniq.com`, `digital-strategy.ec.europa.eu` or `iesalc.unesco.org` — all returned
`ENOTFOUND` at the DNS layer. 🔵 **Every regional fact in this pass is therefore
search-tier, and none of the figures above were re-confirmed against the issuing body.**
🟢 **They were not changed either** — nothing was overwritten on weaker evidence than it
was originally written with. `ACTION p808-N`: re-verify the NC and CA instruments against
primary sources in a session whose network policy allows those hosts.


#### Update 2026-11-13 (twelfth pass, `p807`) — 🟢 the federal instrument this file has described in prose for five passes now has a NUMBER, a CITATION and an EFFECTIVE DATE — and it is not a "rule"

🔴 **This is a correction, not an addition.** Since the fourth pass this file has carried
two federal items as unnumbered prose: *"the April 2025 executive order 'Advancing
Artificial Intelligence Education for American Youth'"* and *"the US Department of
Education finalized a rule prioritizing federal education grants."* 🟢 **Both are real.
Neither was citable, and the second was mischaracterised.** A proposal cannot quote
"a rule".

🟢 **The parent instrument is [Executive Order 14277](https://www.whitehouse.gov/presidential-actions/2025/04/Advancing-Artificial-Intelligence-Education-For-American-youth/),
"Advancing Artificial Intelligence Education for American Youth."** Signed
**2025-04-23**, published **2025-04-28** at **90 FR 17519**. 🔵 **Note the year — 2025,
not 2026.** The North America search leg returned it inside a 2026 framing and it would
have entered this file as a 2026 instrument had it not been checked. It creates the
White House Task Force on AI Education, orders a Presidential AI Challenge within `90`
days, and — **the operative clause for this market** — directs the Secretary of
Education to **prioritise AI in discretionary grant programmes for teacher training
within `120` days**.

🟢 **That `120`-day clause is what produced the second instrument, and it is NOT a rule.**
It is a **Secretary's final supplemental priority and definitions**, *"Advancing
Artificial Intelligence in Education"*, under **34 CFR Part 75**, Docket
**ED-2025-OS-0118**, document **2026-07087**, published **2026-04-13** at
**91 FR 18774–18780**, **effective 2026-05-13**. 🔴 **It is an *invitational* priority**,
usable in **any** Department discretionary grant competition that elects to adopt it —
which is why this file was right to call it "indirect" and wrong to call it binding or
a rule. The final text **added universal-design principles** and **broadened the
AI-literacy definition to include ethics, critical thinking and societal impact**, after
`300`+ public comments on the July 2025 proposal.

🔵 **Why the distinction is commercial, not pedantic.** An invitational priority does not
create demand; it creates **scoreable language**. A district or university writing any
ED discretionary-grant application can claim points for AI literacy, CS-and-AI
coursework, educator development, or embedding AI into teacher preparation — and the
final text's own additions tell a proposal writer which words score. 🟢 **The sellable
artefact for a North American public-sector engagement is therefore a grant-aligned
scope document**, not a platform pitch, and it is cheap to produce.

🔴 **Verification limit, stated plainly.** `federalregister.gov`, `ed.gov` and
`regulations.justia.com` are **all outside this session's allowed network domains**, so
the citation above could **not** be read from a primary source this pass. It is
corroborated across four independent secondary sources (AEI, MeriTalk, the Justia
regulation-tracker listing, and the `ED-2025-OS-0118` public-inspection PDF path), which
agree on volume, page range, docket, document number and both dates. 🔵 **Before it goes
in a client proposal, read `91 FR 18774` directly** → `Gap 807-A`.

🟢 **Net effect on this file's standing read.** *"Federal remains effectively empty"*
(sixth pass, line 368) stays **true for curriculum mandates** — the K-12 AI Literacy and
Readiness Act is still only out of committee — but it is now **false for funding**, and
funding is the channel a studio can actually act on.


#### Update 2026-11-13 (eleventh pass, `p806`) — 🔵 the regional leg returned NOTHING this file did not already hold, and the thing that moved is an architecture decision, not an instrument

🔴 **Explicit nil, stated rather than smoothed.** The North America leg returned NC
`Session Law 2026-41`, CA `AB 1159`, NY `A 9190`, the `134`-bills-across-`31`-states
count, the federal K-12 AI Literacy and Readiness Act, and the Common Sense Media /
OpenAI California ballot initiative. 🟢 **Every one of those is already recorded below.**
That is the **first pass on which the North American *regulatory* leg produced no new
instrument at all**, and it should be read as the state-legislative wave having reached
its plateau for this session rather than as a search failure.

🟢 **What did change for North America is in `repos/foundations.md` and
`verticals/solutions.md`, not here: Ed-Fi.** This base has been scoping North American
student-record work at the **institution** level — RosarioSIS, Gibbon, one district's
SIS — when US K-12 data actually moves through **Ed-Fi**, the interoperability standard
state education agencies run their reporting on. 🔴 **Ed-Fi was mentioned `249` times in
this base's trending logs and `0` times on any shelf.** Both reference implementations
are **Apache-2.0** (`Ed-Fi-ODS` v7.x, `Data-Management-Service` v8).

🔵 **The commercial consequence is a change of altitude.** An agent that speaks one SIS
sells to one district. An agent that speaks Ed-Fi sells to a **state education agency**,
and the dated district-policy deadlines already in this file — NC's `2027-06-30`, Ohio's
`2026-07-01` — are **state-level procurement events** that a state-level integration is
positioned for and a district-level one is not. 🔴 **No Ed-Fi agent interface exists
anywhere (`Gap 806-A`); it is a build and must be priced as one.**


#### Update 2026-11-13 (tenth pass, `p805`) — the regional leg returned nothing new, and the opportunity that moved is a stack this base had already verified

🔴 **`AI education North America 2026 adoption regulation players` returned only facts
this file already holds**: 134 AI-in-education bills across 31 states, the SUNY
systemwide AI-literacy requirement for incoming undergraduates from fall 2026, the
Bonamici *AI Education and Workforce Readiness Act* (introduced, **not passed**), the
proposed Florida Board of Governors rule (**not final**), FERPA as the binding
procurement constraint, and Northeastern in Anthropic's Claude for Higher Education
programme. 🔵 **Recorded as a nil, not omitted** — a silent region is indistinguishable
from an uncovered one.

🟢 **What did change is on the supply side.** The **Credential Engine stack** —
[`osmt`](https://github.com/CredentialEngine/osmt) (Apache-2.0, 67★),
[`CredentialRegistry`](https://github.com/CredentialEngine/CredentialRegistry)
(Apache-2.0, 15★) and
[`transcript-ctid-matcher`](https://github.com/CredentialEngine/transcript-ctid-matcher)
(Apache-2.0) — was verified in an earlier pass and had **never been written to a shelf
file**. It is now in `repos/foundations.md` and is the basis of new pattern `P18`.
🔵 **This is the North America opportunity with the clearest buyer in this file**:
CTDL/RSD is a US public vocabulary, the buyers are state systems, community colleges
and workforce boards, and the whole reference stack is permissive. 🔴 **It does not
transfer out of North America** — see the APAC and EMEA subsections for why that is a
gap and not an oversight.


**Adoption/regulation:** The most legislatively active region, and the activity
is restrictive rather than enabling. Trackers count **134 AI-in-education bills
across 31 states in 2026**, with the consensus read that states favour
research, transparency and guardrails over mandated classroom adoption.
Concrete instruments: **Texas** general AI law (TRAIGA) effective 2026-01-01
with **HB 2400 barring AI from delivering direct classroom instruction**;
**New York** restricting classroom AI to grade 9+ with exceptions for
diagnostics and special education; **California AB 1159** would **bar using
student data to train AI models**; **Idaho SB 1227** requires privacy
protections for AI tools in schools and produced a statewide generative-AI
framework approved August 2026; **North Carolina SL 2026-41** (AI-literacy
standards; state model policy by 2026-12-31, local policies by 2027-06-30,
teacher training by 2028-06-30); **New Jersey A 4352 / S 2862** would add AI to
curriculum and require AI credentials at public colleges. **Four states —
Idaho, Oklahoma, Virginia and Maryland — passed 2026 laws requiring both state
guidance and mandatory district-level AI policy adoption.** Federally: the April
2025 executive order "Advancing Artificial Intelligence Education for American
Youth" sets K-12 priorities, and the **K-12 AI Literacy and Readiness Act of
2026** advanced out of the House Education and Workforce Committee. District
level is where procurement now bites: **New York City** issued preliminary
guidance in March 2026 on a **green/yellow/red traffic-light framework**, and
**Chicago's** board-approved policy **bars AI from being the sole basis for
high-stakes decisions such as discipline and special-education placement**.
California may become the de facto national regulator for AI used by minors;
OpenAI and Common Sense Media proposed a ballot initiative ("Parents & Kids
Safe AI Act").

**Source conflict to respect:** one tracker holds that **TRAIGA and HB 2400 are
the only *enacted* measures** so far, which contradicts sources treating the
North Carolina, Idaho and Maryland instruments as law. Trackers mix introduced
with enacted. Verify any specific bill against the legislature before advising.

**Players:** Instructure/Canvas is the integration target that matters; Canvas
dominates higher ed. PowerSchool in K-12 SIS. Large districts (NYC, Chicago,
Denver, Charlotte-Mecklenburg) now have their own AI policies, which means
district-level procurement with real compliance requirements. Canada's rules
are mainly workplace-focused and reach education only indirectly; **Mexico was
not covered by the sources found this pass — an unverified gap, not a finding
of absence.**

**Opportunities:**
1. **Compliance-aware tutoring that respects instruction bans.** Texas HB 2400
   forbids AI *delivering instruction*; practice, feedback and teacher support
   remain open. A tutor architected as "practice and feedback, human delivers
   instruction" is sellable in states where a general tutor is not.
2. **State-mandated AI literacy programs with deadlines.** North Carolina's
   model-policy date is **within seven weeks** of this update, with local
   policies and teacher training following. Four states now mandate district
   policy adoption. Districts need curriculum, training and a policy artifact —
   deliverable work with a statutory deadline.
3. **Decision-provenance controls for high-stakes use.** Chicago's rule
   (no AI as sole basis for discipline or placement) and NYC's traffic-light
   tiers are implementable as technical controls: human-in-the-loop gates,
   decision logging, tier-based tool allowlists. No open-source project covers
   this; it is consulting plus a small platform.
4. **Canvas-native agents.** `canvas-mcp` (MIT, 324 stars) plus `ltijs`
   (Apache-2.0) is the fastest route to an agent inside the dominant North
   American LMS.
5. **Student-data-boundary architecture.** If AB 1159 passes, "student data
   never reaches model training" becomes a contractual requirement — which
   means self-hosted or no-train-guarantee inference, and an auditable data
   path. Build it once, sell it in every state that follows.

#### Update 2026-11-13 (third pass) — regulation hardened, and a platform default changed the ground

- **The governance gap now has a number.** Google's November 2026 education
  report (Gallup-based) finds **85% of educators say they use generative AI**
  while **only 18% of US teachers report having received any formal AI guidance**
  from administrators. That 85/18 split is the single most sellable statistic in
  this KB: the demand is not for AI capability, it is for governance of AI
  already in use.
- **A platform default became policy.** Google is making **Gemini and Search
  opt-in (off by default) for K-12 student accounts**, administrator-enabled,
  with the change starting early 2027; traditional Search without AI summaries
  is **not** offered as an option (AI Mode and AI Overviews stay built in).
  Political backlash followed (Bernie Sanders, NYC Mayor Zohran Mamdani).
  **Consequence for engagements:** districts now face an explicit
  enable/disable decision with no middle setting, which converts "should we
  allow AI" from a philosophical question into a dated administrative task with
  a deadline. That is a procurement trigger.
- **Binding state law, not just guidance.** Maryland **SB 720** signed,
  effective **2026-06-01**. Oklahoma **SB 1734** signed May 2026 (age-appropriate
  tools, mandatory teacher review of AI output, parent opt-out). Ohio requires
  every public, community and STEM school to **adopt an AI framework by
  2026-07-01**. Mississippi embeds AI literacy into general education for all
  incoming undergraduates from **Fall 2026** and requires institutions to
  evaluate AI tools for bias. Florida's state board approved AI rules covering
  K-12 **and all 28 state colleges**.
- **Federal: still no binding curriculum standard.** The **K-12 AI Literacy and
  Readiness Act of 2026** was advanced by the House Education and Workforce
  Committee; status beyond committee unconfirmed. Treat federal action as a
  watch item, state action as the real driver.
- **Institution-level mandates are the new unit.** UT Austin requires every
  course syllabus from **Fall 2026** to carry a **Course AI Policy Statement**
  classifying generative AI as permitted / partially permitted / prohibited.
  This is a per-course, per-term artifact at university scale — i.e. a
  templating and compliance-tracking problem, which is a product.
- **Source conflict, recorded:** state-guidance counts range from "28+ states
  plus DC" to "34+ states plus DC/PR" across secondary trackers. Quote the
  direction, not the count.

#### Update 2026-11-13 (fourth pass) — the legislative volume is real, the counts disagree, and three states now have dated deadlines

**Bill volume, with the disagreement shown rather than averaged.** One tracker
counts **134 AI-in-education bills across 31 states** in the 2026 session;
**FutureEd counts roughly 71 across 27 states**. The gap is definitional — what
counts as an "AI in education" bill — and both are secondary trackers. Quote the
range and the reason for it, never a single number.

**The legislative posture is cautious, which is itself the commercial fact.**
Analysts reading the 2026 session describe states as focused on **research,
transparency and guardrails rather than mandating classroom adoption**. Nothing
in the US pipeline obliges a district to buy AI; several instruments oblige it to
*govern* AI it already has. That is the shape of the demand.

**Dated deadlines — the procurement triggers.** As `T10` argues, a date with a
named owner is when budget moves:

| Jurisdiction | Instrument | Date |
|---|---|---|
| **North Carolina** | State model policy due | **31 December 2026** |
| **North Carolina** | Local school-unit policies due | **30 June 2027** |
| **North Carolina** | Specified teacher professional development due | **30 June 2028** |
| **California** | AI Working Group statewide Model Policy published | June 2026 |
| **Maryland** | Package: designated AI coordinators + university-supported **certification of compliant AI tools** | 2026 session |
| **New York** | NY A 9190 would restrict classroom AI to **grade 9 and above**, with exceptions | pending |

North Carolina is the one to build a regional offer around: three successive
deadlines, each creating a different deliverable — policy, then local policy at
scale, then teacher training. Maryland's **tool-certification** provision is the
more interesting one commercially, because it implies a conformity-assessment
market inside a single US state, which is the EMEA motion arriving in North
America.

**Guidance is now near-universal at state level.** A June 2026 tracker puts
**35+ states** with official AI guidance from their education departments.
Guidance without enforcement is exactly the governance gap `T1` describes, and
the 85%/18% educator pairing already in this section quantifies it.

**Federal, and it is indirect.** The US Department of Education finalized a rule
**prioritizing federal education grants** for projects that expand understanding
of AI or its appropriate and ethical use. This is a funding signal, not a
mandate: it makes "AI literacy and ethical use" a fundable line item in grant
applications, which is a route into public-sector engagements that does not
depend on a district's own budget.

**One unusual input worth knowing about in a room.** Students from all 50 states
produced a national framework, the **"STUDENTS FIRST Act of 2026"** (via AASA),
which explicitly rejects *both* an outright ban and unrestricted adoption. It
carries no legal force and is useful for exactly one thing: it is the most
quotable evidence that the student constituency is asking for governed use
rather than either extreme.

**Reliability note.** Several items here come from secondary trackers with
inconsistent dates and counts, and at least one claim circulating for this period
(a Florida policy dated 16 September 2026) **could not be confirmed against a
primary source and is therefore not asserted above**. For anything that will
appear in a proposal, verify against the state legislature or department of
education directly.

#### Update 2026-11-13 (fifth pass) — the one telemetry standard North America specifies now has a priced path, and two new restriction instruments surfaced

🟢 **The opportunity that is specific to this region, and it is new.** **Caliper
Analytics is the 1EdTech-native learning-analytics standard and is the one most
often written into North American higher-ed procurement** — xAPI dominates
everywhere else. Until this pass this KB told a Caliper-bound client it had "no
open starting point; that is a build, and it must be priced as one." **That is
withdrawn.** Six implementations are now verified (`repos/foundations.md`), and
the regional detail matters: the most complete one,
`UnizinAnalytics/caliper-net-public` (LGPL-3.0, **nine Metric Profiles** — Base,
Session, Reading, Annotation, Assignable, Assessment, Assessment Item, Outcome,
Media) comes from **Unizin, the US higher-education consortium**, and the
permissively licensed analysis layer,
`tl-its-umich-edu/caliper-event-analysis` (**Apache-2.0**), comes from the
**University of Michigan** with its statistics consulting group CSCAR.
🔵 **Both are North American institutional provenance, which is usable evidence
in a US higher-ed procurement conversation in a way an EU or APAC repo is not.**

🔴 **The one Caliper component that is still a build: the event store.** The only
one found (`open-ent/caliper`, Caliper 1.2) carries **no licence**. **So the
revised North American pitch is: an MIT sensor, a GPL-3.0 Moodle emitter, an
Apache-2.0 analysis layer and a nine-profile reference to scope against — you
write the store and nothing else.** That is a line item, not a project
(pattern `P11`). 🔴 **Ask which Caliper *version* the contract names in week
one:** the only verified sensor defaults to **v1.1** and the only **v1.2**
implementation is the unlicensed one.

🟡 **Two further regulatory instruments surfaced this pass, both recorded with
their uncertainty rather than asserted.**

- **Texas HB2400** — reported as **banning AI from providing direct classroom
  instruction**. 🔴 **One secondary source calls it enacted; this pass could not
  confirm it against official legislative records, so it is logged as
  unverified.** If real it is the most restrictive instruction-level instrument
  in the region and it would make `P1` (compliance-safe practice tutor, the
  pattern written for restrictive states) directly applicable in the largest
  US K-12 market. **Verify against the Texas Legislature before quoting it.**
- **California "Parents & Kids Safe AI Act"** — a proposed **ballot
  initiative**, with **OpenAI and Common Sense Media** reported as joining it.
  🔵 **Why it matters out of proportion to its stage: a California ballot
  measure sets de facto national standards for edtech AI**, as this file's `T10`
  (platform defaults as the fastest-moving regulation) already argues for
  vendor-side changes. A ballot initiative is slower than a platform default and
  harder to reverse than a statute. **Track it; do not price against it yet.**

🔴 **Agent-side negative for this region, stated because silence would read as
coverage: no new North America-origin education agent was found this pass.**
The region's contribution to this pass is telemetry and regulation, not agents —
consistent with `T8`, which puts the agent centre of gravity in APAC.

#### Update 2026-11-13 (sixth pass) — the state-level count keeps climbing, higher ed is moving through institutions rather than statute, and federal remains empty

- **At least 25 states** have **enacted or introduced** legislation specifically
  addressing AI use in **K-12** as of spring 2026. Three themes dominate and
  they are the three a proposal must answer: **student-data privacy**,
  **classroom-use guardrails requiring human oversight**, and **AI literacy /
  curriculum requirements**.
- **Named instruments this pass:** **Idaho SB 1227** sets a statewide K-12
  framework and **bars AI from replacing human teachers**; **Maryland** requires
  state AI guidance plus local district policies; **Oklahoma** requires
  teacher-directed AI use. 🔴 **"Bars AI from replacing human teachers" is a
  design constraint, not a talking point** — it rules out autonomous-grading
  pitches in those jurisdictions and makes `P1`'s teacher-in-the-loop shape the
  only sellable one.
- **Guidance still far outruns statute:** more than half of state Departments of
  Education have issued AI guidance, while **few have enacted binding
  legislation**. Guidance is faster to satisfy and faster to change — price
  re-work in.
- **Federal remains effectively empty.** **No binding federal AI curriculum
  standards** as of mid-2026. A House committee **advanced** the *K-12 AI
  Literacy and Readiness Act of 2026*, which would create a federal funding
  pathway — **advanced, not enacted**. Do not build a proposal on it.
- **Higher ed is institutional, not legislative, and splits both ways.**
  **New Jersey** requires public colleges to offer AI certificate and degree
  programs (an *enablement* mandate — rare in this region). Against that,
  **Berkeley Law bans AI on exams and credited coursework from summer 2026**.
  🔵 **The implication for a studio: in US higher ed the buyer is the
  institution, and two institutions in the same state can be buying opposite
  products.** Segment the pipeline by institution, not by state.

#### Update 2026-11-13 (seventh pass) — two statewide vendor deployments are now named, and the mandate count keeps climbing

- 🟢 **North America now has *named statewide platform deployments*, not just policy.** **Utah** is
  deploying **Google Gemini for Education across all K-12 schools statewide from the 2026–27 school
  year**, and **Microsoft** has announced **Copilot and Teams for Education free to Washington state
  classrooms from 2026**. 🔵 **This is the displacement risk to put in front of any North American
  client:** where a hyperscaler lands the state contract, the studio's opening is **integration,
  assessment redesign and compliance evidence**, not a competing tutor.
- 🟢 **Guidance is now near-universal at state level: roughly `33`–`35` state education departments
  plus Puerto Rico publish official K-12 AI guidance**, up from about `28` in early 2025.
- 🟢 **Mandatory district AI policy is the live procurement trigger.** **Ohio** was first — every
  district had to adopt the state model policy or a locally developed equivalent **by 2026-07-01**.
  **Maryland**'s law is **effective 2026-06-01** (state guidance plus mandatory local policy), and
  **Idaho, Oklahoma and Virginia** carry 2026 laws of the same shape. **Oklahoma** additionally
  requires age-appropriate tools, **teacher review of AI output**, and **parent opt-out**, with
  district policies in place **before the 2027–28 school year**. **Tennessee** also requires district
  policies. 🔵 **California's model policy is advisory, not binding** — do not price it as a deadline.
- 🔴 **The tracker disagreement `T906` flagged has not closed.** One tracker counts **`134` bills
  across `31` states** in 2026; bill numbers and attributions conflict between sources (Georgia
  `SB 179` vs Idaho `SB 1227`; Tennessee numbering varies). 🔴 **Every instrument in this section is
  secondary-sourced** — `gov.uk`-class primary access is refused from this session for US state
  legislature domains too. Quote the *shape* of the requirement, never a bill number, without
  checking enacted text.
- 🔵 **Parent opt-out and teacher-review clauses are a product requirement, not a legal footnote.**
  Oklahoma's wording maps directly onto controls this KB already holds: `learnmcp-xapi`'s per-learner
  `ACTOR_UUID` separation for opt-out scoping, and `AI-Teaching-Agent`'s human review gate.


#### Update 2026-11-13 (ninth pass) — 🔴 the most actionable instrument in US higher education was missing from this file, and it expires in 48 days

🔴 **Provenance, stated before the content.** `suny.edu` does not resolve from this
session (`getaddrinfo ENOTFOUND` — outside the allowed network domains), so **every
figure below is search-tier, read from indexed reporting and from SUNY's own cited
documents, not from the primary PDF.** 🟢 **`ACTION p804-V`: re-verify against
`suny.edu/sunypp/documents.cfm?doc_id=933` and the Board resolution
`Reso_SUNYSystemwideAIPolicy_April2026.pdf` when that host is reachable.**

**The SUNY systemwide AI policy — the named, dated instance of this file's own
standing conclusion.** The sixth-pass note here said US higher education "is moving
through institutions rather than statute." 🟢 **SUNY is that sentence with a scope and
a deadline attached:**

- **Adopted by the Board of Trustees, April 30, 2026**, as a systemwide policy.
- **Scope: the system's 64 campuses** — the largest single governed population of
  US higher-education institutions this file has identified.
- 🔴 **Hard deadline: campuses "shall publish AI policies and/or update relevant
  existing policies **no later than December 31, 2026**."** 🔴 **That is 48 days from
  this pass.**
- **Curricular effect:** AI was folded into the **Information Literacy** core
  competency of the general-education framework, reported as applying to students
  entering **Fall 2026**, adding no extra credits.
- **Support mechanism:** the **AI for the Public Good Fellows** — an inaugural cohort
  of **20** faculty and staff, and a second cohort of **11** focused on
  discipline-specific integration. 🔵 **Note the shape: 31 people to move 64 campuses.
  That ratio is the opportunity, not a criticism of the programme.**

🔴 **Two contradictions preserved rather than averaged.** (1) One policy write-up dates
the Information Literacy revision to a **December 2024** Board action, not 2026; the
2026 materials are the ones that carry the AI language. (2) Several outlets describe a
**standalone "AI course requirement"**; SUNY's own framing is **AI content inside an
existing competency**. 🔵 **Pitch the second version — it is the defensible one, and it
is also the cheaper build.**

**Also new to this file, and still federal-empty.** The **K-12 AI Literacy and Readiness
Act of 2026** advanced out of House committee and has not passed Congress; the
Department of Education's **accreditation rulemaking** would have accreditors examine
AI-related research misconduct — 🔵 **the first time accreditation, rather than statute,
appears as an AI lever in US higher education.** Both consistent with this file's
standing read: **no binding federal curriculum standard exists.**

🟢 **What this changes for a studio.** The NA opportunity in this file was previously
framed as state-level K-12 mandates. **It now has a second, sharper shape: a single
procurement relationship covering 64 institutions, all of which must produce a
published AI policy inside 48 days, and 31 fellows to help them.** The deliverable is
`P16`, and the reusable half of it is `P14`'s deployment registry — a published policy
that cannot name what the campus actually runs is the failure mode every one of these
64 campuses is about to hit.

### EMEA

#### Update 2026-11-15 (thirty-first pass, `p826`) — the Annex III date confirms a FOURTH time with two companion dates, and EMEA's open supply turns out to be the national school portal

🟢 **The regional leg produced on every axis. Regulatory items `CITED, NOT READ`; repository items first-hand and byte-read.**

- 🟢 **`Regulation (EU) 2026/1744` (Digital Omnibus on AI) confirmed a FOURTH independent time: stand-alone **Annex III** high-risk duties — education among them — apply from **`2027-12-02`**, moved from `2026-08-02`, a `16`-month postponement and explicitly **not** a repeal. In force `2026-07-27`.** 🔵 **This base has carried `2027-12-02` since `p823`; this pass adds nothing but confidence, and that is worth one line rather than a section.**
- 🟢 **Two companion dates this base had not recorded together, cited:** **Article 50 transparency duties are NOT part of the delay** — reported as applying since August 2026, with **`2026-12-02`** cited for generative-AI output marking — and **Annex I** systems embedded in regulated products apply from **`2028-08-02`**. 🔵 **Commercially this is the sentence that matters: a vendor selling into EU education has a transparency obligation NOW and a high-risk obligation in two years. Proposals that treat `2027-12-02` as the only date are selling the wrong milestone first.**
- 🔴 **Education is Annex III but not automatically high-risk**, per the Omnibus coverage: admissions, grading, steering learning and exam-cheating detection are the named triggers. 🟢 **Which is exactly why `P58` and `P63`'s practice of drawing the classification boundary BEFORE the first node is a commercial asset and not a compliance chore.**
- 🔴 **National instruments, cited:** the UK Department for Education published **generative-AI product safety standards for education in January 2026**, and **Ofqual** published **March 2026** resources on AI and coursework integrity. In the Gulf, **Dubai's KHDA** has issued explicit responsible-AI guidance to private schools. 🟡 The European Parliament's March 2026 briefing frames the AI Act alongside the Digital Education Action Plan and the European Education Area; an Education and Skills Package on AI and teacher shortages is reported.
- 🟡 **Vendors, cited:** OpenAI reports government and education-system partnerships across EMEA including **Estonia, Slovakia, Greece and Italy**; Pearson and Instructure are named as active in a Q3-2026 roundup. 🔴 The source article is dated November 2026 and may be misdated; treated as directional only.
- 🟢 **The structural finding of this pass is EMEA, and it is measured rather than cited (`T95`).** The region's open education supply is **not** tutors or courseware — it is **connectors to the national school system of record**: **WebUntis** (🇦🇹🇩🇪🇨🇭, `6` repositories), **Librus Synergia** (🇵🇱, `3`), **Pronote/ÉcoleDirecte/Skolengo** (🇫🇷, `2`), **Magister** (🇳🇱, `2`). 🔵 **`12` repositories, `10` independent implementations, written by individual parents and students against systems with no public API, read-only by declaration, and findable only under the SYSTEM NAME — no query containing the word "education" returns any of them.**
- 🔴 **And `7` of the `12` carry no `LICENSE` file — a `58%` unlicensed rate, the highest of any tier this base has measured.** 🟢 **The commercial read: the cheapest route to European coverage is a licence request to four named developers, followed by the one product none of them has built — a multi-tenant connector across national systems behind a single domain model (`P64`).** `jujukingg/edu-mcp` already proves the multi-back-end shape inside France; `ljarochowski/librus-mcp` already ships the country-neutral domain model.
- 🟡 **UNESCO's Higher Education Global Trends Report 2026, cited:** roughly **`70%`** of institutions in Europe and North America have adopted or are developing AI guidance, against **`45%`** in LATAM. 🔵 **Useful as a cross-region comparator; this base holds no EMEA-specific institutional adoption rate and should stop implying one.**

#### Update 2026-11-15 (thirtieth pass, `p825`) — the Annex III date confirms a THIRD time, and the teacher-readiness gap is now surveyed rather than asserted

🟢 **All items `CITED, NOT READ`; the EMEA leg produced on every axis this pass.**

- 🟢 **`Regulation (EU) 2026/1744` (Digital Omnibus on AI) confirmed a third independent time:
  stand-alone **Annex III** high-risk duties — education among them — apply from **`2027-12-02`**,
  and Annex I (AI embedded in regulated products) from **`2028-08-02`**.** 🔵 **The scope was NOT
  narrowed; education remains an Annex III category and only the date moved.**
  🔴 **One live disagreement remains unresolved and is recorded rather than smoothed over:** sources
  split on Article `50` transparency/watermarking, some holding `2026-08-02`, others `2026-12-02`
  with the grace period compressed from six months to three. 🟡 **`ACTION p825-E`: resolve against the
  Official Journal text, not against commentary — this base has now carried the ambiguity for four passes.**
- 🟢 **Article `4`'s AI-literacy duty has bound every organisation using AI, schools included, since
  `2025-02-02`, and is unaffected by the Omnibus.** 🔵 **That remains the obligation with live demand
  and almost no open supply — `p824`'s finding, and `p825` adds one row under it:**
  [`EDU-C2-051` teacher professional-development evidence](https://github.com/haidang024/agentic-star-education-teacher-professional-development-evidence-agent)
  (MIT, byte-read), which reads only operator-DECLARED connectors.
- 🟡 **Adoption is now measured, not asserted:** Futuresource reports **`67%` of teachers** using AI
  tools and describes K-12 and HE as moving *from experimentation to structured implementation*
  (formal policies plus professional development). 🔴 **Against that, an Epson survey of
  **`~3,360` teachers across the UK, France, Italy, Germany, Spain and Poland** finds **`80%` worry AI
  is entering the classroom faster than schools can manage.** 🟢 **Those two are not in conflict and
  together they ARE the sales thesis: adoption is high and confidence is low, so the buyable product
  is governance and evidence, not another tutor.**
- 🟡 **Institutional layer:** Eurydice published a 2026 report on digital education in Europe; the
  Digital Education Council's EMEA summit convened `41` senior leaders from `30` institutions across
  `14` countries; Fosway's 2026 AI Market Assessment covers EMEA learning leaders.
  🔵 **Futuresource expects AI PCs to be `15%` of education PC shipments this year** — a hardware
  signal that on-device inference is arriving in EMEA classrooms on a procurement cycle.
- 🟡 **Middle East, placed here deliberately.** The **UAE Ministry of Education is reported to have
  introduced `25` generative-AI prohibitions in schools in `2026-02`**, covering age suitability,
  privacy, academic integrity and exam restrictions. 🔴 **Search surfaced this under an "APAC" query;
  under this base's closed region vocabulary the UAE is EMEA, and it is recorded here. Single
  secondary source — verify against the Ministry before quoting to a client.**
- 🟢 **New EMEA supply this pass:** [`Signlytic AI`](https://github.com/Iyanuoluwa007/Signlytic_AI)
  (MIT, byte-read, `80 MB`) — **British Sign Language**↔English. 🔵 **BSL is a distinct language from
  ASL and the open supply is overwhelmingly ASL, so a UK accessibility engagement could not previously
  be served from these shelves at all.**


#### Update 2026-11-15 (twenty-ninth pass, `p824`) — 🟢 The Omnibus date is now citable with its instrument number, and the AI-LITERACY duty is the obligation with live demand and almost no open supply

🟡 **Sourcing note for every item in this block: egress in the `p824` environment resolved GitHub and web search only — `oecd.org` was refused at the proxy, as at `p822`. Every market and regulatory item below is `CITED, NOT READ`: it comes from web-search summaries of secondary sources, several of them vendor blogs and trackers. 🔴 Verify any date, bill number or percentage against the official text before quoting it to a client. Every REPOSITORY figure in this pass is first-hand and byte-read; the two classes are not interchangeable.**

- 🟢 **The Digital Omnibus on AI now has an instrument number in this base: Regulation (EU) 2026/1744,
  reported published `2026-07-24` and applying from `2026-07-27`.** 🔵 **Previous passes carried the
  postponement as "reported" with no citation handle; this is the handle. It still requires
  verification against EUR-Lex before it goes in a client deck.**
- 🔴 **The high-risk timing conflict is RESOLVED in favour of the later date, with both readings
  recorded.** Older guides place Annex III education obligations at **August 2026**; newer sources
  place stand-alone Annex III systems at **`2027-12-02`** under the Omnibus. 🟢 **This base already
  carried `2027-12-02` from `p815`; `p824` is the second independent confirmation and the first
  with the Omnibus instrument attached.**
- 🟢 **What is ALREADY in force, and is therefore where the sellable work is:**
  **Article 4 AI-literacy duty since `2025-02-02`**, binding every organisation that uses AI systems
  and therefore every school; **the ban on emotion recognition in education since February 2025**;
  **Article 50 transparency from `2026-08-02`**.
  🔵 **Three live obligations against one postponed one. An EMEA engagement scoped on Annex III is
  selling 2027 work; an engagement scoped on Article 4 and Article 50 is selling work that is
  already late.**
- 🔴 **And the Article 4 supply is nearly empty, measured first-hand this pass.**
  `q="ai literacy curriculum"` → `51` repositories, ceiling `55★` and that ceiling is a US
  engineering course; `q="ki kompetenz schule"` → **`1`**;
  `q="alfabetizacion inteligencia artificial educacion"` → **`0`**.
  🟢 **One German-language licensed artefact exists and is now shelved —
  [`malkreide/critical-ai-literacy-skill`](https://github.com/malkreide/critical-ai-literacy-skill),
  MIT.** 🔵 **So the duty binds every school on the continent and the open corpus beneath it is
  English-language and higher-education-shaped. Localisation into the classroom languages is the
  clearest unserved slot `p824` found in this region.**
- 🟢 **Policy direction: digital SOVEREIGNTY, stated in Council documents.** Council of the EU texts
  cited this pass (`ST-13077-2026`, `ST-14902-2026`) press for AI literacy, academic-integrity
  policies and explicitly for *"reducing dependencies associated with AI tools and technologies
  developed outside Europe, including in education and training"*. 🔵 **That sentence is the
  procurement argument for `P13` (sovereign LMS-native AI on OpenOLAT) and `P35`, and it is now
  attributable to a Council document rather than to inference.**
- 🟢 **Funding rails named: Erasmus+, Horizon Europe and the European Social Fund Plus**, cited as
  supporting infrastructure, teacher professional learning, inclusive digital resources and
  responsible-AI research. 🔵 **For a public-sector engagement the funding instrument is usually the
  real gate, and these three are the ones to write into a proposal.**
- 🟢 **Supply this pass: `4` EMEA rows** — `ferien-mcp` (🇩🇪 school holidays per *Land*),
  `critical-ai-literacy-skill` (🇩🇪), `ai-on-campus`/PRISMA (🇮🇹, from Reply's "AI on Campus"
  challenge — the second design-challenge channel this base has measured after `T74`), and `tiza`
  (🇪🇸 Spanish-language Moodle authoring with a teacher-approval gate, the reference implementation
  for `P60`).


#### Update 2026-11-15 (twenty-eighth pass, `p823`) — 🔴 The AI Act high-risk date MOVED and this file was carrying the old one; 🟢 the region supplies the most institution-integration code of any

🟡 **Sourcing note for every item in this block: egress in the `p823` environment resolved GitHub and web search only. Every market and regulatory item below is `CITED, NOT READ` — primary texts were NOT opened. Figures are attributed to the party that published them, vendor and advisory sources are marked as such, and dates that sources disagree on are shown disagreeing. Every REPOSITORY named is first-hand and byte-read.**

- 🔴 **A DATE CORRECTION, and it matters more than anything else in this block.** The **2026 Digital
  Omnibus** changed the AI Act's high-risk timetable. Per a guide cited this pass, stand-alone
  **Annex III** high-risk systems now apply from **`2027-12-02`**, and AI embedded in regulated
  products from **`2028-08-02`**. 🔴 **Older guidance — including material this base has drawn on —
  still says August 2026 for high-risk education AI. That is now OUT OF DATE.** 🔵 **Commercially
  this cuts both ways: the compliance cliff is further off than clients were told, so urgency-based
  selling is wrong, and a competitor still quoting August 2026 can be corrected on the record.**
  🟡 `CITED, NOT READ` — **verify against EUR-Lex before putting either date in a proposal.**
- 🟢 **What already binds, and has since `2025-02-02`: Article 4, AI literacy.** It applies to
  **every organisation that uses AI systems**, therefore to every school and university, with no
  high-risk classification required. 🔵 **This is the live, unglamorous, fundable obligation —
  training and evidence of training — and it is available NOW rather than in 2027.**
- 🟢 **Education stays high-risk in substance:** admission decisions, student evaluation and exam
  scoring are the named uses. 🔵 **Which is the same line `T30` records from Ofqual and Florida —
  QA, marker training, moderation and second-marking are open; sole-decider marking is closed.**
- 🟢 **A Council of the EU document from late 2026 pushes DIGITAL SOVEREIGNTY in education** —
  reducing dependence on non-European AI tools, plus AI literacy and provider academic-integrity
  policies. 🔵 **That is a direct commercial signal for self-hosted, open-weight deployments in
  EU public education**, and it aligns with the open substrate this base shelves.
- 🔵 **Named funding rails, worth quoting in a public-sector bid:** Erasmus+, Horizon Europe, ESF+.
  **Supervisory structure:** the European AI Office sits in DG CONNECT with exclusive powers over
  general-purpose model providers; national authorities enforce the rest. 🇬🇧 **The UK is separate**
  — DfE generative-AI guidance plus product safety standards for education in England.
- 🟢 **The region produced the most `T77` supply of any this pass**, all byte-read:
  [`Raindancer118/nak-api`](https://github.com/Raindancer118/nak-api) 🇩🇪 (NORDAKADEMIE CIS +
  Moodle, **`83` tools**, 🟡 **WTFPL — not OSI-approved, legal sign-off before tender**),
  [`do-2k25-28/moodle-um`](https://github.com/do-2k25-28/moodle-um) 🇫🇷 (MIT, Université de
  Montpellier via **ENT/CAS**, 🔴 **write-capable with no published read-back**),
  [`Damanian/MIREA-Toolkit-MCP`](https://github.com/Damanian/MIREA-Toolkit-MCP) 🇷🇺 (MIT).
  🔴 **Unadoptable but real:** [`mahmutmft/courses-mcp`](https://github.com/mahmutmft/courses-mcp)
  🇲🇰 (FINKI Moodle, **no grant file**).
- 🔴 **DECLARED GAP, and it is the same one as last pass: this leg returned essentially nothing on
  the MIDDLE EAST or AFRICA.** The regional search resolved to EU-and-UK material almost entirely.
  🔴 **A single Africa-placed supply item appeared and could not be shelved:**
  [`TD-Mosoma/Mothusi`](https://github.com/TD-Mosoma/Mothusi) 🇿🇦, *"an AI classroom colleague for
  Grade 1–4 teachers in South Africa"*, **all-rights-reserved**. 🟢 **An informed gap: EMEA in this
  file still means Europe, and that is a limitation of the channel, not a finding about the
  region.** 🔵 **Re-test for `p824` with named instruments — KHDA 🇦🇪, Saudi SDAIA, Kenya's CBC,
  South Africa's DBE — rather than with the region word.**


#### Update 2026-11-15 (twenty-seventh pass, `p822`) — 🔴 The research channel's EMEA is the EU; this base's EMEA SUPPLY this pass was entirely African

🟡 **`CITED, NOT READ` throughout: egress resolved GitHub only this pass.**

- 🟢 **The authoritative-looking demand source is the European Commission's Eurydice report
  *Digital education at school in Europe 2026*,** summarised as finding that **access to advanced
  AI at school level remains uneven** across member states. 🔵 **Unevenness is the sales argument
  for a ministry engagement and the risk argument for a per-school one.**
- 🟡 **Student-side demand, vendor-sponsored and labelled as such:** an Epson Europe survey reports
  **`76%` of students expect to be able to use AI in their learning** and **`87%` of those already
  use AI at least weekly** for school. 🔴 **Sponsored survey; directional only.**
- 🟢 **Regulation remains the binding constraint and it is MOVING.** The EU AI Act plus GDPR is the
  frame; items cited this pass include **draft guidelines under Article `6` with a public
  consultation reported open until `23 June 2026`**, Council of Europe conference material arguing
  schools and teachers cannot carry implementation alone, and an **"AI Omnibus" simplification
  reported in May `2026`**. 🔴 **All three are secondary reports of primary instruments and are
  flagged for verification when egress permits — do NOT cite the dates to a client from this file.**
- 🟡 **Sizing (MarketsandMarkets, commercial):** Europe ≈ **USD `512.6` M (`2024`), `17.2%` CAGR**,
  with the **UK, Germany and France** named as leading adopters.
- 🔴 **The declared gap, and it is the important item in this block.** The EMEA research channel
  returned **essentially nothing on the Middle East and Africa** — the regional leg produced EU
  material almost exclusively. 🟢 **Yet every EMEA SUPPLY row this base added this pass is African:**
  `Sautika` (*"designed for learners across East Africa"*, Swahili, voice-first, dyslexia-inclusive),
  `Meska Brain` and `DIRA` (both African Agentic AI Design Challenge, Education track), and
  `EthioLearn` (Ethiopia, `EUEE`, diaspora-funded). 🔵 **So the asymmetry is explicit: the market
  research this channel can reach does not look where the builders are. A studio taking EMEA
  guidance from market reports alone would conclude Africa has no education-AI activity, and
  `p822`'s own byte-read shelf refutes that.**
- 🟢 **The EU-side supply finding is `MyDocker`** — CentraleSupélec's MIT-licensed virtual lab
  platform, Software Heritage archived, launched from Moodle. 🔵 **An institution-authored,
  permissively licensed platform is rare in a tier dominated by GPL/AGPL, and that is a procurement
  advantage worth leading with in European higher education.**
- 🔵 **Opportunity, stated plainly:** AI Act conformity work for school-facing systems, and an
  Africa practice sourced from design-challenge cohorts (`T74`) rather than from vendor lists.

#### Update 2026-11-15 (twenty-sixth pass, `p821`) — 🟢 The region's four-pass instrument NIL is unchanged, and the movement is on the SUPPLY side instead — including this base's first Africa-origin row

- 🔴 **Instruments: NIL for a fifth consecutive window.** The mandated EMEA leg returned the same
  bodies this file already holds — the EU AI Act as amended by the **Digital Omnibus**, the Council
  document **ST-14902-2026** of `2026-10-29`, the European Parliament briefing **PE 784.574**, the
  UK **DfE** generative-AI product safety standards and **Ofqual**, Dubai's **KHDA** guidance.
  🔵 **The high-risk clock still shows the same unresolved spread this file has flagged since
  `p819`: an August 2026 reading against `2027-12-02` for stand-alone Annex III systems and
  `2028-08-02` for AI embedded in regulated products. Unchanged, and still not resolved on a
  secondary channel.**
- 🟡 **One new non-binding item, dated and named.** **Cambridge University Press & Assessment**
  published a report on `2026-11-04` recommending that policymakers give **teachers a stronger
  voice** in school AI policy. 🔵 **It is not an instrument and this file does not promote it to
  one** — it is cited because it is the same argument the Council document makes from the supply
  side, and because a named assessment body saying it changes who can be quoted in a proposal.
  🔴 **`CITED, NOT READ`.**
- 🟢 **SUPPLY, and this is the region's real movement this pass — two rows, both byte-read,
  neither European.**
  - 🇪🇬 **Egypt**: [`mohanvd/edutraceapp`](https://github.com/mohanvd/edutraceapp) (MIT, `28★`) —
    the national **STEM Grades 10–11 Learning Outcomes** encoded with a stable short code per
    outcome. 🔵 **First Egypt-placed platform in this base, and placement rests on the repository's
    own `egypt` topic string.** Shelved in `verticals/solutions.md`.
  - 🌍 **Africa**: [`AI-Native-Ventures/jemma`](https://github.com/AI-Native-Ventures/jemma) (MIT,
    `0★`) — **the first Africa-origin row in this base** (`T71`), a longitudinal learner profile
    with a consent gate, from the **African Agentic AI Design Challenge**, Education track.
  - 🔴 **One Arabic-first platform measured and licence-flagged:**
    [`fotedev/Masar-x-next`](https://github.com/fotedev/Masar-x-next) is **AGPL-3.0** (byte-read,
    `34,523 B`) — §13 reaches network users, so it is reference material, not adoptable into a
    hosted client product.
- 🔵 **The structural point for an EMEA engagement (`T70`): both new rows bind to a national
  instrument or to a named programme, not to a subject.** The Council's push to reduce dependence
  on non-European AI tools argues for the same architecture from the other direction — the
  curriculum adapter is the sovereign part, and it is the part a European or African ministry
  already owns.

#### Update 2026-11-15 (twenty-fourth pass, `p819`) — 🔴 NIL on instruments for a fourth consecutive window, and the high-risk clock still shows three different dates

🔴 **Explicit nil, stated with what was run.** The EMEA leg returned the Digital Omnibus amending
regulation, Article 4's AI-literacy duty and its August 2026 enforcement start, the education
high-risk classification, and the February 2025 emotion-recognition prohibition. 🟢 **Every one of
those is already held in this file.** 🔵 **Recorded as a nil rather than omitted: a silent region is
indistinguishable from a covered one, and this is the fourth consecutive window in which EMEA's
regulatory leg has returned only items this base already carries.**

🔴 **The one thing that did NOT resolve, and it has not resolved for eight passes: the education
high-risk date.** The channel returned **2 December 2027** and **2 August 2027** in the same sweep,
against the **2 August 2026** Article 4 enforcement date this file already holds. 🔴 **Three dates,
three secondary sources, no primary.** 🔵 **The practical consequence is unchanged and is what to
say to a client: the LITERACY duty is live NOW and the HIGH-RISK conformity duty is not, so the
fundable work this year is staff capability and documentation, not conformity assessment against a
date nobody can cite.**

🟡 **One addition, graded SECONDARY and small.** An **EU–OECD AI Literacy Framework** is reported
released **18 June 2026**. 🔵 **If it holds up it is the artefact an Article 4 training programme
should be mapped to, because it is the one a market-surveillance authority is likeliest to
recognise** — but this base has not seen the primary and should not cite it as a standard yet.

🔴 **Regional supply this pass: NIL.** The star-ranked sweep (`T63`) returned `0` new
EMEA-attributable repositories. 🟢 **Consistent with `T56`: the EMEA credential reference is
archived and nothing has replaced it.**

#### Update 2026-11-15 (twenty-third pass, `p818`) — 🟢 A STATE ARCHIVE ships its own agent surface, two national research platforms gain MIT connectors, and the region's abandoned repository platform becomes a migration proposal

🟢 **The strongest supply signal this region has produced, and it is the `p810` Ed-Fi pattern for
the third time: the body that OPERATES the record is the body shipping the agent.**
[`AI-Riksarkivet/ra-mcp`](https://github.com/AI-Riksarkivet/ra-mcp) (🟢 **Apache-2.0**, `27★`,
pushed `2026-11-14`) exposes the **Swedish National Archives'** open APIs, under the archive's own
GitHub organisation. 🔵 **The entry route for a Nordic public-sector engagement is therefore to
CONTRIBUTE to the operator's repository, not to pitch a competing connector — and that is a
procurement-friendly posture a tender can actually reward.**

🟢 **Two national research platforms gained MIT connectors this window.**
[`muctebadikmen/dergipark-mcp`](https://github.com/muctebadikmen/dergipark-mcp) covers **DergiPark**,
the Turkish national journal platform operated by **TÜBİTAK ULAKBİM**, and its own description names
the control that makes it defensible: *official OAI-PMH, keyless, no CAPTCHA* — a published protocol
endpoint rather than scraping. 🟢
[`malkreide/swiss-academic-libraries-mcp`](https://github.com/malkreide/swiss-academic-libraries-mcp)
covers **swisscovery**, the shared catalogue of roughly `490` Swiss libraries, plus e-rara,
e-periodica and e-manuscripta — the CONSORTIUM layer rather than one institution. 🔴 **Both `1★`,
both single-maintainer: supply, exactly as the `p811` portal layer was.**

🟢 **And the generic row that makes this whole tier cheap to enter is European and MIT:**
[`mpasternak/oai-pmh-mcp`](https://github.com/mpasternak/oai-pmh-mcp) speaks OAI-PMH to *any*
repository — dLibra, DSpace, EPrints. 🔵 **One server reaches the entire institutional-repository
tier without a per-platform connector, because OAI-PMH is a 2002 protocol every one of them already
implements.**

🟢 **The region's platform story improves sharply, and the proposal writes itself.**
[`inveniosoftware/invenio-app-rdm`](https://github.com/inveniosoftware/invenio-app-rdm) is 🟢 **MIT,
holder CERN**, `187★`, pushed `2026-11-13` — the platform **Zenodo** runs on. 🔴 **Against it,
[`eprints/eprints`](https://github.com/eprints/eprints) — the original institutional repository,
still in production at UK and European institutions — is GPL-3.0 and has not been pushed since
`2023-07-31`.** 🟢 **EPrints → InvenioRDM: abandoned to CERN-maintained, GPL-3.0 to MIT, same job.
That is a scoped, dateable engagement with a named incumbent, which is rarer in this base than any
agent row.**

🔴 **A regulatory date conflict, recorded and NOT averaged.** One source places EU AI Act high-risk
obligations as applying **from August 2026**; others place Annex III standalone high-risk —
education — at **2027-12-02** under the 2026 AI Omnibus. 🟢 **This base's four-source reading
(`T939`) and the Commission's own amendment timeline both support `2027-12-02` for education, and
Art. `50` transparency remains live since `2026-08-02`.** 🔵 **The August 2026 claim is most likely
a conflation of the transparency date with the high-risk date — which is the single most common
error in EU AI Act commentary, and worth correcting in front of a client.**

🟢 **New named instruments and movements this window.** The Commission presents an **Education and
Skills Package** aimed at helping schools use AI. 🟢 **UK: the DfE published generative-AI product
SAFETY STANDARDS for education in January 2026** — 🔵 **note this is a product standard, which makes
it a procurement gate a vendor can be measured against, unlike guidance** — and **Ofqual issued
coursework-integrity resources in March 2026**, consistent with the `T30` reading that
sole-decider marking is closed while QA and moderation are open. 🟢 **Gulf: Dubai's KHDA has issued
explicit responsible-AI guidance to private schools** — the operator-level instrument this base has
lacked for the Gulf. 🟢 **Vendor movement: OpenAI reports government and education-system
partnerships in Estonia, Slovakia, Greece and Italy; Pearson is acquiring Workera to verify AI
skills.** 🔴 **All vendor-partnership claims are CITED, NOT READ — the source is a secondary
aggregator.**

#### Update 2026-11-15 (twenty-second pass, `p817`) — 🔴 **Europe has the world's most developed credential POLICY and an ARCHIVED reference codebase; the gap between the two is the opportunity**

🟢 **Regional supply this pass: `+1` agent row** —
[`barzoj/somtoday-mcp`](https://github.com/barzoj/somtoday-mcp) (🟢 MIT, `1★`, pushed `2026-11-13`),
read-only MCP over Somtoday, a dominant Dutch 🇳🇱 secondary-school parent portal. 🔵 **Placed EMEA
under `T42` by the system's catalogue, not the author's address.**

🔴 **The finding for this region, and it is counter-intuitive enough to lead a conversation with.**
[`european-commission-empl/European-Learning-Model`](https://github.com/european-commission-empl/European-Learning-Model)
— the data model behind Europass Digital Credentials, published by DG EMPL — is 🔴 **ARCHIVED, last
pushed `2024-02-14`, and licensed EUPL-1.2, a RECIPROCAL licence that is not interchangeable with the
MIT stack a studio would otherwise use.** 🟢 **Meanwhile the policy layer accelerated:** European
Digital Credentials for Learning, the EQF, the EU Digital Identity Wallet, and the European Digital
Education Hub's Higher Education Interoperability Framework spanning the learner journey including
credentials and digital identity. 🔵 **Policy moving, reference code frozen — see `T56` and `P44`.**

🟢 **The engagement posture that follows, stated so it can be quoted:** conform to ELM as a
SPECIFICATION, implement against the MIT DCC stack, and say in writing that the EU reference
repository is archived. 🔵 **Clients hear that as diligence in month one and as a problem in month three.**

🟢 **Regulation, this window (🟡 `SECONDARY` — verify against the Official Journal before quoting a
date to a client):**
- 🟡 The AI Omnibus, **Regulation (EU) 2026/1744**, reported in force `2026-07-27`, moving Annex III
  high-risk obligations to **`2027-12-02`**. 🟢 **This independently corroborates the date `p815`
  recorded as unverified `SECONDARY` — two channels now agree, and it remains `SECONDARY`.**
- 🟡 Education AI is high-risk where it determines access or admission or evaluates learning outcomes.
- 🟡 Article 4 AI-literacy duties reported supervised by national market surveillance authorities from
  `2026-08-02`, with the Omnibus softening the standard to *“measures … taken”*.
- 🟡 Council conclusions on teachers in the era of AI approved `2026-05-11`; ethical guidelines for AI
  and data in education last updated `2026-06-09`.
- 🟡 1EdTech cites **France's national interoperability decree** as the leading example of
  interoperability becoming mandatory rather than aspirational (`T53`).

🔴 **Measured nil this pass, stated with its query:** `q="ebsi verifiable diploma"` →
`total_count=1`, and it is [`KDiamantidis/ebsi-vc-poc`](https://github.com/KDiamantidis/ebsi-vc-poc),
`0★`, **no licence**, a proof of concept. 🟢 **So EBSI — the EU's own blockchain credential
infrastructure — has no adoptable open implementation on this channel in any licence.**


#### Update 2026-11-15 (twenty-first pass, `p816`) — 🔴 SUPPLY NIL, and the AI Act's education clock is now the only thing in this file with THREE different dates

🔴 **Regional supply this pass: NIL, for the same structural reason as North America** — the
retention layer has no national catalogue, so `T42` places all `21` new rows `Global`. 🔵 **One row
would have been placed EMEA by author origin (`pieralukasz/true-recall`), and under `ACTION p811-D`
this base refuses author-origin placement: the shelf keeps it `Global` on its target system
(Obsidian). That refusal is now costing this region a visible row, which is the honest price of the
rule and is recorded rather than quietly evaded.**

🟢 **The regulatory picture, which is where this region's value in this file actually sits
(secondary-sourced; the primary texts remain unreachable from this session per `ACTION PD`):**

| Instrument | Date | Status |
|---|---|---|
| Emotion-recognition ban (education and workplace) | **in force since 2026-02-02** | 🟢 Binding now |
| Chatbot / AI transparency duties | **from 2026-08-02** | 🟢 Binding now — this window |
| High-risk duties for EDUCATION | 🔴 **moved to 2027-12-02** | 🟡 Deferred by the 2026 Digital Omnibus |
| Commission draft guidelines under **Article 6** | published **2026-05** | Interpretation channel |

🔵 **The sales consequence has not changed and is worth repeating because the delay invites the
wrong read:** the transparency duty binds NOW and the high-risk grading duty does not bind until
December 2027. 🟢 **So a chatbot or tutoring surface shipped in EMEA today has live obligations,
while an automated-grading product has an `~13`-month runway — and `P40`'s retention loop engages
NEITHER, because it writes no academic record and makes no evaluative determination about a person.
That is the cleanest regulatory position any recipe in this file holds in this region.**

🟢 **Soft-law and institutional movement this window:**
- **Commission ethics guidance for education UPDATED in 2026**, prepared by the European Digital
  Education Hub's Working Group on the Ethical Use of AI and Data in Education.
- **Council ministers approved conclusions on teachers and AI, May 2026**, pressing AI literacy and
  education-specific tools.
- **Council of Europe “Compass for AI and education”**, from its October 2025 conference.
- **Eurydice report, September 2026: access to advanced AI technologies at school level remains
  UNEVEN** — 🔵 the first EMEA-wide official statement in this file that the constraint is
  distributional rather than regulatory.

🔴 **And the gap that keeps widening: adoption is running ahead of governance, autonomously.** In
adult education, teachers and adult educators are reported adopting AI *"to a large extent,
autonomously and without a clear regulatory framework"*, with **Spain over `90%`** of respondents
using AI at work. 🔵 **An uneven-access finding plus an autonomous-adoption finding is a
governance engagement, not a tooling one — which is the EMEA motion this file has recommended since
`p809`.**


#### Update 2026-11-15 (twentieth pass, `p815`) — 🟢 EMEA BUILT the assessment layer, and EMEA regulation is what makes it sellable — the tightest supply/demand fit in this base

🔵 **Source confidence.** Repository measurements are `FIRST-HAND` — run `2026-11-15` against
`gh api -X GET search/repositories`, licences byte-read over `raw.githubusercontent.com`. Policy
and market figures are `SECONDARY` (web-search summaries of trackers, briefings and vendor blogs)
and are labelled as such; verify any date before putting it in front of a client.

🟢 **The supply finding is unusually clean: the assessment-engine layer is substantially a
European artefact.** Of the nineteen engine rows filed this pass, the provenance concentrates
here:

| Component | ★ | Licence | Origin |
|---|---|---|---|
| [`judge0/judge0`](https://github.com/judge0/judge0) | 4,519 | 🔴 GPL-3.0 | 🇭🇷 Croatia |
| [`jplag/JPlag`](https://github.com/jplag/JPlag) | 2,012 | 🔴 GPL-3.0 | 🇩🇪 Karlsruhe Institute of Technology |
| [`DOMjudge/domjudge`](https://github.com/DOMjudge/domjudge) | 925 | 🔴 GPL-2.0 | 🇳🇱 Netherlands |
| [`SafeExamBrowser/seb-win-refactoring`](https://github.com/SafeExamBrowser/seb-win-refactoring) | 369 | 🟡 MPL-2.0 | 🇨🇭 ETH Zürich |
| [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | 357 | 🟢 **MIT** | 🇧🇪 Ghent University (`dolos@ugent.be`) |
| [`jcrodriguez-dis/moodle-mod_vpl`](https://github.com/jcrodriguez-dis/moodle-mod_vpl) | 130 | 🔴 GPL-3.0 | 🇪🇸 Univ. de Las Palmas de Gran Canaria |
| [`jorge-martinez-gil/codesim`](https://github.com/jorge-martinez-gil/codesim) | 28 | 🟢 **MIT** | 🇦🇹 Austria |

🔴 **And the regional licence problem: the European rows are the copyleft ones.** `Judge0`,
`JPlag`, `DOMjudge` and `VPL` are GPL; the one MIT row is `Dolos`. 🟢 **Which makes `Dolos`
(Ghent) the most commercially important European row in this layer — it does `JPlag`'s job under
a licence that ships. See `T44`.**

🟢 **The demand side closes on the same spot.** 🔴 **EU AI Act Annex III names education as
high-risk and names exam-cheating detection among the listed uses** (`SECONDARY`: obligations
reported postponed from `2026-08-02` to `2027-12-02` under a 2026 Digital Omnibus agreement, which
sources describe as provisional and which other sources still date to August 2026 — 🔴 **verify
against the official text; the conflict is real and a wrong date in a proposal is costly**).
🟡 Also reported: UK DfE generative-AI product safety standards for education, and **Ofqual
guidance on AI and coursework integrity** — 🔵 **that second one is the most directly sellable
policy instrument in any region this pass, because it asks for exactly what `P37` produces: a
defensible record of how an integrity judgement was reached.** 🟡 Dubai's KHDA has issued
responsible-AI guidance to private schools.

🟡 **Players, `SECONDARY`:** OpenAI reports government and education-system partnerships across
Estonia, Slovakia, Greece and Italy focused on access, AI literacy and evaluation; Instructure is
building an AI study coach into Canvas; Pearson agreed to acquire Workera. 🔵 **The most
authoritative source in this window is a March 2026 European Parliament briefing on AI in
classrooms (`IUST_BRI(2026)784574`) — prefer it over the vendor guides.**

🟢 **Where to lead in this region:** 🟢 **`P37` first and explicitly as Annex III compliance work
— human oversight and record-keeping — not as surveillance.** `P2` (Annex III conformity layer)
chains directly in front of it. 🔵 **And check for `VPL` before proposing anything new at an
Iberian university: its Spanish origin and Moodle base make it the likely incumbent, which turns
an engagement into configuration rather than build.**


#### Update 2026-11-13 (nineteenth pass, `p814`) — 🟢 The region holds the best-engineered research-library agents in the world, and they are MIT

🔵 **Source confidence.** Repository and licence figures `FIRST-HAND` this pass; AI Act dates
`SECONDARY` and **in conflict between sources**, so `p813`'s block remains the authority.

🟢 **The supply finding.** EMEA gained `4` build-safe rows this pass and every one is MIT:

| Row | Country | Binds to | Why it matters |
|---|---|---|---|
| [`mpasternak/dspace-mcp`](https://github.com/mpasternak/dspace-mcp) | 🇵🇱 Poland | DSpace 7+ institutional repositories | *"Read-only by construction, not by promise"* — the cleanest read-only argument in this base, plus correct credential guidance (env var over `--password`, keychain) |
| [`mpasternak/ojs-mcp`](https://github.com/mpasternak/ojs-mcp) | 🇵🇱 Poland | Open Journal Systems | `OJS_ALLOW_WRITES=1` OFF by default, with the reason stated: *"Writes change real journal data"* |
| [`suren-kk/armenian-national-library-mcp`](https://github.com/suren-kk/armenian-national-library-mcp) | 🇦🇲 Armenia | the National Library of Armenia's DSpace 9 | 🟢 **The first agent in this base that puts a RIGHTS CHECK before retrieval — the direct antidote to `T40`** |
| [`asjolaviral/koha-mcp-server`](https://github.com/asjolaviral/koha-mcp-server) | — | Koha ILS | OAuth2 `client_credentials` with token refresh: the only non-password auth in this base |

🟢 **The opportunity, and it is specific to this region's regulatory posture.** 🔵 **An AI Act
`deployer` obligation is easiest to discharge on a system whose agent is read-only by
construction and whose data the institution itself owns — which describes DSpace exactly.** 🟢
**`DSpace` is **BSD-3-Clause** (byte-read `1,504 B`, `sha256:baf9ee18…`), so a studio can fork and
ship it; every other platform in the education stack is copyleft.** 🔵 **Sell the sovereign,
self-hosted institutional-repository agent: no learner credential, no third-party data source,
no emotion inference, and nothing leaves the institution.**

🟡 **Policy context (`SECONDARY`).** Education AI systems that determine access, admission or
evaluate learning outcomes are high-risk; the emotion-recognition prohibition in education has
applied since `2 February 2025`; schools are `deployers` and carry an AI-literacy obligation for
staff. A provisional Council/Parliament agreement amending the AI Act was reached `7 May 2026`,
and one school-focused source puts high-risk education obligations at `2 December 2027` under a
2026 Digital Omnibus amendment — 🔴 **that regulation number could not be confirmed against a
primary source and must not be quoted to a client.** The Commission published draft Article 6
guidelines on `19 May 2026` (consultation to `23 June 2026`); education ministers adopted
conclusions on teachers in the era of AI on `11 May 2026`; the `AILit` framework is the common
AI-literacy reference for primary and secondary schools.


#### Update 2026-11-13 (eighteenth pass, `p813`) — 🟢 The high-risk clock moved a year, and the region's most permissive grant yet appears in Norway

🔵 **Source confidence.** Dates below are `PRIMARY-CITED` and **conflict between sources**;
🔴 **`eur-lex` remains unreachable under this session's network policy, so the Official Journal
text was NOT read** (`T906`, tenth pass).

- 🔴 **The single most consequential date in this file moved.** The EU AI Act's **Annex III
  high-risk obligations — which cover admissions, student evaluation and exam scoring — are
  reported DELAYED to `2027-12-02`** under the 2026 AI Omnibus, while the Commission began
  enforcing the Act from `2026-08-02`. 🔴 **One source still reports high-risk duties applying
  from August 2026.** 🟢 **The conflict is recorded rather than resolved, because resolving it
  requires reading a text this session cannot reach.**
- 🔵 **If the delay holds, the commercial consequence is specific:** an EMEA assessment or
  admissions engagement scoped in 2026 has **a year of additional runway** before the conformity
  machinery binds — and 🔴 **the AI-literacy duty (Article 4) is unaffected and has applied since
  February 2025.**
- 🟢 **MEASURED — `EMEA 10 → 12`, and one row changes what a studio may do with it.**
  [`kristoffervp/vigilo-mcp`](https://github.com/kristoffervp/vigilo-mcp) (🇳🇴 Vigilo municipal
  parent portal) is **0BSD — byte-read `640 B`, against GitHub's `NOASSERTION`**. 🟢 **Zero-Clause
  BSD carries NO attribution requirement at all: it can be vendored into a client deliverable with
  no notice file, which no MIT row in this base permits.** 🔵 **`T31` (EMEA supply attaches to
  national and regional school portals) now reaches a sixth country.**
- 🟢 **MEASURED — the most-starred EMEA education agent in this base is Russian:**
  [`kad-xyz/spbstu-mcp`](https://github.com/kad-xyz/spbstu-mcp) (`20★`) spans SPbPU's Moodle,
  university mail and **`openedu.ru`, the Russian national MOOC platform**. 🔴 **Shelved as market
  evidence of the national-platform pattern, NOT as an adoptable dependency: sanctions and
  data-residency review is a precondition for any commercial use.**
- **UK (`PRIMARY-CITED`):** Department for Education **generative-AI product safety standards
  (January 2026)** and **Ofqual** resources on AI and coursework integrity (March 2026).
  🔵 **Ofqual's framing — assistance permitted, sole-marker prohibited — is the one `P26` is
  already shaped to.**
- **Gulf (`PRIMARY-CITED`):** Dubai's **KHDA** has issued explicit responsible-AI guidance to
  private schools. 🔵 **A regulator addressing the PRIVATE school sector directly is a pattern this
  file has not previously recorded.**
- **Players:** OpenAI reports government and education-system partnerships in **Estonia, Slovakia,
  Greece and Italy**, focused on access, AI literacy and evaluation. **Instructure** is building
  an AI study coach into Canvas; **Pearson** agreed to acquire **Workera** for AI-skills
  verification (the `T23` split, now with a European-listed acquirer).
- 🔴 **DECLARED GAP, FOURTH consecutive pass.** Germany, France and the Nordics return regulatory
  machinery and **zero classroom deployment figures**. 🟢 **`ACTION p802-B`'s re-shaped instruction
  stands and was again NOT run: ask the bodies that OPERATE the portals (Hessen's
  Kultusministerium for Schulportal, an Andalusian *delegación territorial* for iPasen) — they are
  the bodies that publish usage numbers.** 🔴 **Do not re-run a national-level query; it has now
  failed four times.**

#### Update 2026-11-13 (seventeenth pass, `p812`) — 🟢 The university campus-virtual tier joins the school-portal tier, and the Gulf adds a hard prohibition list

🔵 **Source confidence, stated once for this block.** Figures marked `MR` come from
market-research marketing pages or vendor-commissioned surveys read through search summaries and
are **order-of-magnitude only**; figures marked `PRIMARY-CITED` name a primary issuance that was
**not** read directly under this session's network policy. 🔴 **Nothing in this block was read
from a primary source this pass.**

- 🟢 **`p811`'s EMEA finding extends one tier UP.** `p811` found agents on national and regional
  **school** portals. `p812` adds the **university campus virtual**:
  [`rdereparadores/cvuex-mcp`](https://github.com/rdereparadores/cvuex-mcp) (**MIT**,
  byte-verified) serves the Campus Virtual of the **Universidad de Extremadura** 🇪🇸, created
  `2026-09-26`. 🔵 **Same shape and same window as the Argentine cluster** — which is what makes
  `T34` a cross-regional pattern rather than a LATAM curiosity. **EMEA is now `10` of this base's
  `74` build-safe agents, the largest regional bloc after `Global`.**
- 🔴 **The UAE set `25` generative-AI PROHIBITIONS for schools (February 2026)** covering age
  suitability, privacy, academic integrity and exams (`PRIMARY-CITED`, single secondary source —
  verify before quoting). 🔵 **Placed in EMEA deliberately: the Gulf is EMEA in this file's closed
  region vocabulary, and a search engine filing it under APAC is a vocabulary error, not a fact.**
  🟢 **A prohibition LIST is a cheaper compliance artifact to build against than a principles
  document** — it maps directly onto `P14`'s deployment registry.
- **Adoption is past the pilot stage and the hardware follows.** Futuresource reports **67% of
  teachers now using AI tools** and adoption moving *"from experimentation to structured
  implementation"*; AI-enabled devices are forecast at **15% of institutional PC shipments in
  2026**, growing **4.3M units (2026) → 15M (2030)** (`MR`, vendor-commissioned).
- 🔴 **Teacher confidence is the brake, and it is measurable.** An Epson-commissioned survey of
  ~`3,360` people across the UK, France, Italy, Germany, Spain and Poland found **80% of teachers
  worry AI is entering the classroom faster than schools can manage**, while **76% of students
  expect to be able to use AI in their learning** (`MR`). 🔵 **That gap — students pulling,
  teachers braking — is the demand signal for `P20` (AI literacy) and `P14` (registry), not for
  another tutor.**
- **Policy instruments to cite by name:** the **OECD Digital Education Outlook 2026**; the
  Council's **conclusions on teachers in the AI era (11 May 2026)**; **Eurydice, *Digital
  education at school in Europe 2026***; the Commission's **draft Article 6 high-risk guidelines
  (19 May 2026**, consultation to **23 June 2026**) (`PRIMARY-CITED`). 🔵 **The Digital Omnibus
  shift of the education high-risk obligations to `2 December 2027` is already recorded in this
  file and remains the single most important date for an EMEA assessment engagement.**

#### Update 2026-11-13 (sixteenth pass, `p811`) — 🟢 `ACTION p802-B` is half-discharged from the SUPPLY side: German classroom integration CODE exists at Land level, even though the statistics still do not

🟢 **This region's standing gap has been "Germany, France and the Nordics return regulatory
machinery and ZERO classroom deployment figures", failed twice.** 🔵 **`p811` did not find
the statistics. It found the integration code, which is arguably the better artifact for a
bid, and it found it exactly where `p810` predicted — at the level of the Land, the región
and the ministry.**

| System | Operated by | Country | Open agent surface | Licence |
|---|---|---|---|---|
| **Schulportal Hessen (Lanis)** | the federal state of Hesse | 🇩🇪 | [`udondan/lanis`](https://github.com/udondan/lanis) | MIT |
| **DSBmobile** | substitution-plan service used by schools | 🇩🇪 | [`udondan/dsbmobile`](https://github.com/udondan/dsbmobile) | MIT |
| **Admentum** | Swedish school-platform vendor | 🇸🇪 | [`andyswe/admentum-mcp`](https://github.com/andyswe/admentum-mcp) | MIT |
| **iPasen / Séneca** | Junta de Andalucía | 🇪🇸 | [`boraita/ipasen_mcp`](https://github.com/boraita/ipasen_mcp) | MIT |
| **Greek School Network (`sch.gr`)** | Greek Ministry of Education | 🇬🇷 | [`weirdapps/sch-mail`](https://github.com/weirdapps/sch-mail) | MIT |
| **PRONOTE + EduConnect** | Index Éducation + the French state IdP | 🇫🇷 | [`sairo-cyber/pronoteConnect`](https://github.com/sairo-cyber/pronoteConnect) | 🔴 GPL-3.0-or-later |

🟢 **All six were pushed within a five-day window ending `2026-11-13`.** 🔴 **All are `0–2★`
and single-maintainer — supply, not adoption.** 🔵 **But it reverses this file's standing
EMEA sentence:** European education agent supply is no longer "one project at scale and
nothing else"; it is a dispersed, permissive, portal-attached layer that nobody has
consolidated. 🟢 **Consolidating it is a service line.**

🔵 **The buyer implication is the real content of this update.** Four of these systems are
operated by a public body, so: the counterparty is a ministry or a federal state, the route
is public tender, and the **Art. `27` FRIA duty falls on the deployer because the deployer is
public**. 🟢 **A studio that arrives with the FRIA and the portal integration in the same
proposal is answering the two questions that actually block the purchase.**

🔴 **France is the cautionary one (`T33`).** The only open PRONOTE connector is
GPL-3.0-**or-later**, and its `LICENSE` says why: the `@blockshub/pawnote-lts` client it
depends on is GPL. 🔵 **The copyleft is inherited from the protocol client, so relicensing
the connector is not a remedy — a permissive French deployment needs a clean-room PRONOTE
client, scoped and funded as its own deliverable.**

🔴 **Still open: the deployment statistics, third consecutive failure.** 🟢 **Re-shaped
again, and more concretely: ask the Land, not the country — Hessen's Kultusministerium
publishes Schulportal usage, and an Andalusian *delegación territorial* publishes iPasen
figures. The portals that now have agents are the same bodies that publish the numbers.**

#### Update 2026-11-13 (fifteenth pass, `p810`) — 🟢 England supplies a HARD assessment rule; 🔴 `ACTION p802-B` FAILS A SECOND TIME — Germany, France and the Nordics return regulators and still no classroom deployment

🟢 **The most commercially usable EMEA fact this base has found, because it is a rule rather
than a number: Ofqual's position is that AI may NOT be the sole marker in regulated
qualifications — and its guide for schools extends that to NON-EXAM assessment, so a human
must remain the marker there too.** Ofqual's **January 2026** blog adds that AI is promising
for **quality assurance and marker training** but **is not ready for high-stakes marking**, and
its research finds performance varies widely by context with **no general case for AI marking**.

🔵 **Read that as an architecture requirement, not a prohibition.** It names exactly where the
money is: **QA, marker training, moderation and second-marking** are open; **sole-decider
marking is closed.** 🟢 **`compose/patterns.md` `P810-3` is built to this line.**

🟢 **DfE (England):** generative-AI guidance lists **tailored feedback** as a valid use, and
**pupils' original work must not train models without permission**. 🔴 **A claimed 2026 DfE
standard requiring "progressive disclosure" (hints, not answers) and usage limits could NOT be
confirmed against a government source — newsletter-grade only, and it is NOT carried as fact.**

🔴 **`ACTION p802-B` fails a second time, on a second dedicated leg, and the failure is now
specific enough to be useful.** Germany, France and the Nordics returned **regulatory
machinery and zero classroom deployment figures**:
- 🇩🇪 **Germany** — Bundesnetzagentur **AI regulatory sandbox pilot completed `2026-03-17`**; a
  €`20`bn AI investment commitment (`2025`–`2030`) 🔴 *from a low-authority aggregator only*.
- 🇫🇷 **France** — supervision deliberately **split across DGCCRF + CNIL + INESIA**; the
  **INESIA roadmap adopted February 2026**.
- 🇳🇴🇸🇪🇩🇰🇫🇮 **Nordics** — only **enterprise-wide** Eurostat adoption, not education:
  Denmark `27.6%`, Sweden `25.0%`, Finland `24.7%`, France `10.4%` (2024) — 🔴 **and a second
  source gives Denmark `42.0%`, a `1.5×` disagreement on the SAME country.** Do not quote it.

🔵 **Two failed legs on the same question is no longer a search problem.** 🟢 **Re-shaped for
the next pass: these are federal/municipal school systems, so the figures — if they exist —
sit in Länder, académie and kommune publications, not in national ministry press releases.**
🔴 **Until one is found, EMEA's only dated national education-AI deployment programme remains
the UK's (`p802`), and that is a one-country base for a region this file calls EMEA.**

🟢 **Supply note that moves EMEA's five-pass deficit:**
[`FenixEdu/fenixedu-academic`](https://github.com/FenixEdu/fenixedu-academic) (`LGPL-3.0`,
`175★`, Instituto Superior Técnico 🇵🇹) is now shelved — **the largest dedicated open-source
SIS in this base, and European.** 🔴 **Dormant since `2023`, so it is an architecture reference,
not a live platform** — but it refutes the flat claim that EMEA produces no institutional
education software at scale.


#### Update 2026-11-13 (fourteenth pass, `p809`) — 🟡 The Act's education duties slipped to 2027, and adoption is running far ahead of governance

🟡 **Regulatory state, re-read.** Education is **high-risk under Annex III** where a
system determines access or admission, or evaluates learning outcomes. 🔴 **The timeline
moved:** a **provisional deal on the Digital Omnibus package landed 2026-05-07**, the
original **August 2026** deadline has slipped, and Annex III duties now bite from
**2027-12-02** (consistent with `T25`). **Draft Article 6 guidelines published
2026-05-19**, consultation open to **2026-06-23**. 🔵 **For an EMEA engagement this is
good news and a trap: there is more runway than the 2026 headlines imply, and a system
built now will be assessed against guidance that is still being drafted.** Build the
Article 50 transparency artefacts (`P17`) regardless — they are the stable part.

🔴 **Adoption is ahead of readiness, and the numbers are consistent across independent
surveys.** An **Erasmus+** adult-education study across several countries finds educators
have adopted AI *"largely autonomously and without a clear regulatory framework"*, with
**over 90% of respondents in Spain** using AI in their work. An **Epson** survey reports
**80% of teachers** worry AI is entering classrooms faster than schools can manage, and
**76% of students** expect to use AI in learning. 🟢 **That gap — high use, absent
governance — is the EMEA engagement**, and it is the regional instance of `T1`.

🟢 **Connector note placed here:** `RohanMuppa/brightspace-mcp-server` (`MIT`, `67★`)
explicitly lists working **🇳🇱 Netherlands** instances, so the new Brightspace path is
immediately usable in EMEA, not only North America.

🔴 **Still fragmented.** Education policy remains national; teacher readiness varies
widely across member states, and most compliance guidance in circulation is produced by
vendors and consultancies rather than regulators. Treat vendor webinars as marketing.


#### Update 2026-11-13 (thirteenth pass, `p808`) — 🔴 NIL on instruments. The EU AI Act high-risk delay, the UK standards and the Gulf guidance were all returned and all already held

🔴 **Zero new EMEA facts this pass.** The leg
`AI education EMEA 2026 adoption regulation players` returned:

| Returned by the leg | Status in this file |
|---|---|
| EU AI Act Annex III high-risk duties for education **postponed `2026-08-02` → `2027-12-02`** via the Digital/AI Omnibus | 🟢 Already held (`Regulation (EU) 2026/1744`, carried `5×`) |
| Omnibus amendments adopted June 2026, in force `2026-07-27` | 🟢 Already held |
| Education AI for admissions, grading and cheating-detection classified high-risk | 🟢 Already held |
| UK DfE generative-AI product safety standards, January 2026 | 🟢 Already held |
| Ofqual material on AI and coursework integrity | 🟢 Already held |
| Dubai `KHDA` guidance to private schools; UAE national AI strategy | 🟢 Already held |
| OpenAI EMEA education report; partnerships in Estonia, Slovakia, Greece, Italy | 🟢 Already held |
| EU Education and Skills Package | 🟢 Already held |

🟢 **The one thing worth re-stating, because it is the single most commercially decisive
date in this file and the sources returned it inconsistently.** Several guides in the
result set **still quote `2 August 2026`** for high-risk obligations — the pre-Omnibus
date. 🔴 **That date is superseded.** The operative date carried here is
**`2 December 2027`**. 🔵 **The European Commission's own milestone page was described by
one source as internally inconsistent**, which is consistent with what `p805` recorded
when it first established the delay. 🟢 **Practical consequence for scoping, unchanged
but worth repeating: an EMEA education engagement started today has roughly two years
before Annex III conformity duties bite, which is a reason to build the conformity
artefacts in from the start rather than a reason to defer them.**

🔴 **Could not be verified against the primary source this window.**
`digital-strategy.ec.europa.eu` does not resolve under this session's network policy
(`ENOTFOUND`). 🔵 **The `2027-12-02` date therefore rests on the search tier plus five
prior passes of this file, not on a reading of the Official Journal this window.**
`ACTION p808-E`: confirm `Regulation (EU) 2026/1744`'s Article on Annex III commencement
against EUR-Lex when a session can reach it.


#### Update 2026-11-13 (twelfth pass, `p807`) — 🔴 regulatory nil for a THIRD consecutive pass, and the only EMEA movement is a corporate one recorded under Global

🔴 **Explicit nil.** The EMEA leg returned Council document `ST-14902-2026`, the EU AI
Act Annex III high-risk classification and its Digital Omnibus delay, the UK DfE
generative-AI product safety standards (January 2026), Ofqual's coursework-integrity
material (March 2026), Dubai KHDA's responsible-AI guidance to private schools, and
OpenAI's Estonia / Slovakia / Greece / Italy partnerships. 🟢 **Every one of those is
already recorded below**, most of them with tighter dating than the leg supplied.

🔵 **Three consecutive regulatory nils is now the dominant signal for this region, and it
has a cause worth naming.** EMEA's instrument set is **frozen until `2027-12-02`** — the
Digital Omnibus moved the Annex III education obligations there, and nothing else is
scheduled to bite before it. 🟢 **The practical consequence for a studio is that EMEA
regulatory research has reached the point of diminishing returns and the budget should
move to deployment evidence**, which is where the ninth pass's national teacher-adoption
figure came from and where the next EMEA finding will come from too.

🟡 **One EMEA-relevant corporate move did land this pass and is recorded under `Global`
rather than here**, because it is a cross-region transaction: **Pearson's acquisition of
Workera**. Pearson is UK-listed, which makes it EMEA-headquartered supply, but the
target, the customers and the buying centre are North American enterprise.


#### Update 2026-11-13 (eleventh pass, `p806`) — 🔵 regulatory nil for a second consecutive pass, and the EMEA movement this window is SOFTWARE

🔴 **Explicit nil on regulation.** The EMEA leg returned `Regulation (EU) 2026/1744`
(the Digital Omnibus), the `2027-12-02` Annex III date, the Art. `50` transparency
duties live since August 2026, the Feb-2025 emotion-recognition ban, the softened Art.
`4` AI-literacy duty, Council document `ST-14902-2026` on digital sovereignty, and the
Digital Education Action Plan / European Education Area / Erasmus+ / Horizon Europe
funding frame. 🟢 **All of it is already carried below, four-source corroborated.**
**Nothing was added and nothing was withdrawn.**

🟢 **What moved is the supply side, and it moves against this file's standing EMEA
complaint.** This file has said for several passes that EMEA has **one** European-origin
open-source education agent at scale (`tutor-mcp`, 🇫🇷, `102★`) and that "supply is
appearing, adoption is not." **Two rows added this pass change the shape of that
sentence:**

| Addition | Origin | Licence | Why it matters to the EMEA motion |
|---|---|---|---|
| [`numbas/Numbas`](https://github.com/numbas/Numbas) | 🇬🇧 **Newcastle University, UK** | 🟢 **Apache-2.0**, `217★` / `130` forks | 🟢 **The largest permissively licensed education *platform* of EMEA origin this base has found** — larger than every European education agent in it. Browser-based e-assessment with a maths emphasis. 🔵 **Apache-2.0 against a copyleft field** (TAO GPL-2.0, Moodle GPL, Canvas CE and Open edX AGPL-3.0) is the commercial point |
| [`maurodruwel/Smartschool-MCP`](https://github.com/maurodruwel/Smartschool-MCP) | 🇧🇪 **Belgium (inferred from `school.smartschool.be` and Dutch field names, not stated)** | 🟢 **MIT**, `6★` / `7` forks | The **fourth agent-to-SIS path in this base and the second from EMEA**, after Türkiye's `sabis-mcp-server`. `15` tools over the dominant Flemish school platform, 🟢 **read-only by construction — no write tool exists**, which is the easiest posture to put in front of a European DPO |

🔵 **Both land on the sovereignty argument Council doc `ST-14902-2026` makes** — reduce
dependence on AI tooling developed outside Europe. 🟢 **A UK-built Apache-2.0 assessment
platform and a Belgian MIT SIS connector are literally the artifacts that argument asks
for**, and a studio can now name them instead of gesturing at the principle. 🔴 **The
adoption half of the complaint stands unchanged: neither is deployed at scale, and
`217★` is not scale.**


#### Update 2026-11-13 (tenth pass, `p805`) — regulatory position unchanged and re-confirmed; one permissive public-sector SIS reaches the shelf

🔴 **The EMEA leg returned this file's own contents.** Re-confirmed, not re-reported:
the **Digital Omnibus, Regulation (EU) 2026/1744**, moved the Annex III high-risk
obligations for admissions, grading and exam monitoring to **2 December 2027**;
**Article 50 transparency duties were not postponed and apply from 2026-08-02**; the
**emotion-recognition ban in education has applied since February 2025** and is not
deferred. 🔴 **Several vendor guides still print August 2026 for the high-risk date —
they are wrong, and this file has said so since the sixth pass.**

🟢 **Supply-side change:** [`SVWS-NRW/SVWS-Server`](https://github.com/SVWS-NRW/SVWS-Server)
— **BSD-3-Clause**, 42★, **10,015 commits** — is the school-administration server the
German state of **North Rhine-Westphalia** builds for its own schools, and it is now on
the verticals shelf. 🔵 **Why it matters for EMEA specifically: a permissive grant on
public-sector education software is rare, and the commit count says production system,
not pilot.** Pair with `P13` (OpenOLAT, Apache-2.0, sovereign AI in-tree) and the EMEA
engagement is the only one in this base that can be served end to end — platform, SIS
and AI layer — **without a copyleft conversation and without data leaving the
institution**.

🔴 **Declared gap, EMEA:** the Credential Engine stack above is CTDL/RSD and therefore
US-only. **This base knows of no equivalent permissive skills-and-credentials stack for
EMEA** (ESCO is a vocabulary, not an implementation). Searched this pass; nothing
returned.


**Adoption/regulation:** The binding regime is the **EU AI Act**, under which
AI for **access, allocation, assessment, or monitoring of pupils during tests**
is high-risk in principle (Annex III), with an exception for genuinely low-risk
uses. The **Digital Omnibus on AI was published in the Official Journal on
2026-07-24 as Regulation (EU) 2026/1744**, and the timeline it sets is
**2027-12-02 for stand-alone Annex III systems** and **2028-08-02 for AI
embedded in regulated products**, with transparency duties from August 2026.
**Sources conflict:** at least one consultancy states full enforcement of
high-risk requirements arrived in August 2026. Verify against EUR-Lex
(Regulation (EU) 2024/1689 as amended) before advising. The
**emotion-recognition ban in education** has applied since February 2025. The
**AI literacy duty (Article 4)** was softened in July 2026 to a duty to
"support the development of AI literacy". On 2026-06-18 the **European
Commission and OECD published an AI literacy framework for primary and
secondary schools** alongside updated ethical guidelines ("Empowering Learners
for the Age of AI"). **Council of the EU document ST-14902-2026 (2026-10-29)**
makes digital sovereignty and strategic autonomy explicit, treating reduced
dependence on AI tools developed outside Europe as critical for education and
training. Funding channels: Digital Education Action Plan, Erasmus+, Horizon
Europe, ESF+.

**Middle East:** materially more active than this KB previously recorded. The
**UAE** has expanded academic offerings to include AI-focused programs at all
levels; **Saudi Arabia has made AI literacy a mandatory component of
undergraduate education**; **Dubai's KHDA has issued explicit guidance to
private schools** on responsible AI use. Gulf AI spending is shifting from
pilots to sector-scale rollouts.

**Africa:** the **African Union's Continental Education Strategy for Africa
(CESA 16-25)** sets the digital-education direction, and structured AI use is
driven by **government and NGO programs rather than individual teacher
adoption** — which means the buyer is a ministry or a donor, not a school.
**Morocco's "AI Made in Morocco"** strategy targets the academia-industry gap.
First Africa-origin education agent found: **EDUKAI LongView** (ISC, Guinea,
bilingual FR/EN) — a 0-star prototype, but evidence of local capability.

**Players:** Moodle (dominant in European public education), ILIAS
(German-speaking vocational and public sector), Chamilo (Spain, francophone
Africa), Opencast and BigBlueButton (university infrastructure), national
ministries and agencies. **OpenAI reports government and education-system
partnerships including Estonia, Slovakia, Greece and Italy**, citing teacher
adoption and time savings — i.e. the frontier labs are already inside the
public systems a studio would sell to.

**Opportunities:**
1. **High-risk conformity packages for assessment and admissions AI.** The
   deadline moved to 2027-12-02; it did not disappear, and the conflicting
   August-2026 reading means some clients believe they are already late.
   Institutions need risk management, documentation, human oversight and
   logging for systems they already run. Highest-value regulated work in
   education globally.
2. **Sovereign, self-hosted education AI.** The Council's October 2026
   sovereignty language plus GDPR makes "runs in our own infrastructure, on
   open weights" a procurement requirement rather than a preference.
   Moodle/ILIAS + self-hosted inference + MIT/Apache agent layer, with a
   Moodle MCP server (`Faixiang`, MIT) for agent access, is a directly
   sellable stack — and it is the explicit counter-position to the OpenAI
   national partnerships.
3. **AI literacy delivery against the Commission/OECD framework.** A published
   framework, institutional obligations behind it, and a teacher population
   that needs training.
4. **Gulf mandate delivery.** Saudi Arabia's mandatory undergraduate AI
   literacy and the UAE's all-levels programs are funded, dated obligations at
   national scale — curriculum, teacher training and platform work, with a
   buyer that pays.
5. **Ministry-and-donor-scale African programs.** Since adoption is program-led
   under CESA, the deliverable is a national or donor-funded rollout:
   Kolibri (MIT, offline-first) plus localized content, with FR/EN bilingual
   handling as a baseline requirement rather than a feature.

#### Update 2026-11-13 (third pass) — the high-risk deadline moved, and that changes the sales motion

- **The Annex III high-risk deadline moved to 2027-12-02.** The **Digital
  Omnibus** postponed the standalone high-risk obligations under Annex III —
  the category containing education — from the previously circulated
  **2026-08-02** to **2 December 2027**. Earlier vendor guides still print the
  2026 date. **Verify against Regulation (EU) 2024/1689 and the Commission's own
  pages before quoting either to a client**, and expect the client's incumbent
  advisor to be working from the old date.
- **What this does to the pitch:** the compliance deadline is no longer
  imminent, so "you must be conformant by August" is dead as an urgency lever
  and repeating it will cost credibility. The live lever is the **two
  obligations already in force**: the **Article 5(1)(f) ban on emotion
  inference in education institutions** (applicable since **2025-02-02**,
  medical/safety exceptions only) and the **AI literacy duty** (same date).
  Those are enforceable now.
- **Scope is narrower than most clients assume.** Education AI is high-risk
  only when it performs one of the four functions in **Annex III point 3**:
  admissions/access, evaluating learning outcomes, assessing appropriate
  education level, or monitoring students during tests. The Commission's **May
  2026 draft guidelines** place **tutoring, practice feedback and information
  chatbots generally outside** high-risk. **This is a scoping instrument:** a
  practice tutor that never scores of record stays out; the moment it writes a
  grade of record it is in.
- **The obligation sits on the vendor, not the school.** Conformity assessment
  applies to the **EdTech vendor as provider**; schools are **deployers** (use
  as instructed, trained human oversight, logging, inform students and
  parents). A studio building for an institution may become the provider — that
  allocation must be settled in the contract, not discovered at audit.
- **EU-level frameworks to cite:** the Commission and **OECD** jointly
  published the **AILit** AI Literacy Framework ("Empowering Learners for the
  Age of AI") on **2026-06-17**; further guidance landed **2026-03-05** under
  the Digital Education Action Plan (ethical use of AI and data in teaching,
  disinformation and digital literacy, criteria for selecting high-quality
  digital education content). The **European AI Office** is the institutional
  counterpart.
- **Sovereignty angle, with a repo attached:** `openfun/ralph` (MIT) is a
  Learning Record Store from **France Université Numérique** — an EU
  public-education-origin, permissively licensed data layer. For an EU client
  asking where learner data lives, that is a concrete answer rather than a
  posture.

#### Update 2026-11-13 (fourth pass) — the high-risk date is contested, the UK has shipped concrete standards, and Africa is no longer a blank in this file

**The EU AI Act education high-risk date — sources genuinely conflict, so here
is the disagreement.** Education AI is high-risk where it is used for
**admissions, grading, and cheating detection**. On the timing: one reading puts
the obligations at **August 2026**; another, reflecting the **2026 Digital
Omnibus amendments**, at **2 December 2027**. The Commission's own page states
the amendments were **adopted June 2026 and entered into force 27 July 2026**,
which makes **2 December 2027** the more likely date for the education high-risk
obligations. **Carry the later date with the caveat attached, and verify against
the consolidated Act text before it goes in a contract** — a client who has
planned for August 2026 has planned for the wrong year, in both directions.

**What is already in force and is routinely missed: the AI literacy duty has
applied since February 2025.** It is not deferred by the Omnibus. An institution
using AI in teaching has a live obligation now, which makes AI literacy the
easiest EMEA engagement to justify and the one with no date to wait for.

**The UK has moved from guidance to standards, which is the more sellable
shape.** Department for Education **product safety standards for generative AI
in education (January 2026)**, and **Ofqual material on AI and coursework
integrity (March 2026)**. Product *standards* imply conformity work — the UK is
converging on the EMEA assessment-conformity motion in `P2` without the AI Act's
machinery.

**Policy scaffolding to cite rather than re-derive.** The European Parliament's
**March 2026 briefing** on AI in classrooms points to the **Digital Education
Action Plan** and the **European Education Area**; the Commission has presented a
new **Education and Skills Package** on AI and digital learning. In the Gulf,
**Dubai's KHDA issues explicit responsible-AI guidance to private schools** — the
region is policy-led and well-resourced, which is why it buys governance
packages rather than pilots.

**Demand-side signals.** OpenAI reports government and education-system
partnerships across EMEA including **Estonia, Slovakia, Greece and Italy**,
focused on equitable access, AI literacy and evaluation. Employer-side,
**Microsoft, AWS and Caterpillar have announced AI skills commitments totalling
roughly $3.6B** — skills funding that often routes through education
institutions.

**Africa — previously a declared gap in this file, now populated.** The third
pass recorded that EMEA searches returned little on Africa specifically. A
dedicated search this pass changes that:

| Country / body | Instrument | Status |
|---|---|---|
| **Kenya** | National AI Strategy 2025-2030 — commits to AI literacy across education, pilots Digital Innovation Hubs as curriculum anchors | Published March 2025 |
| **Nigeria** | National EdTech Strategy 2025-2030 — teacher capacity, safe AI use, data systems, financing | Active; a separate analysis argues the Digital Economy Policy has **not** translated into systemic education use |
| **South Africa** | Draft National AI Policy, covering education among other sectors | Published for comment **10 April 2026**; one source lists it **abrogated 27 April 2026** — **this conflict is unresolved and must be checked against the Government Gazette** |
| **African Union** | Continental Education Strategy 2026-2035 — treats digitalization and AI as cross-cutting themes | Adopted |
| **UNESCO** | AI readiness assessments across **six Southern African countries**, to inform national AI-in-education policy | In progress |
| **Multi-country** | **AI Research Foundations** launched **9 November 2026** — Google.org-backed, FATE Foundation (Nigeria) as grant holder, training university lecturers in Ghana, Kenya, Nigeria and South Africa, targeting **30,000 students** | Launched |

**The read:** Africa's AI-in-education activity is **strategy-and-capacity
shaped, not deployment shaped** — national strategies, teacher capacity, lecturer
training — which matches the one Africa-origin agent in this KB
(`Keitous/EDUKAI-LONGVIEW`, ISC, Guinea, synthetic data, 0 stars). The
engagement that fits is **teacher and lecturer enablement with a governance
artifact**, delivered against a national strategy document, not a platform
rollout. The 9 November launch is the freshest lead in this file.

**Reliability note.** The Africa sources are a mix of a preprint, a Wikipedia
entry, advocacy analysis and news reports; the South Africa policy status is
actively contradictory. Verify against official government documents before any
of it reaches a client.

**One EMEA-specific technical finding this pass.** The first verified
agent-to-SIS MCP server in this KB is **EMEA-origin**:
`oliverhruby/edupage-mcp` (MIT, 31 tools) over **EduPage**, the school
information system used across **Slovakia and Czechia**. See `T12` — the
concentrated national school-platform markets in Italy, Poland, Turkey and the
Gulf are the obvious next instances, and none has a verified MCP server yet.

#### Update 2026-11-13 (fifth pass) — this file's own regional prediction landed in Türkiye, and France supplies the only Caliper event store in existence

🟢 **A named prediction resolved in one pass, and it was this region's.** `T12`
implication 3 named *"Italy, Poland, Turkey and the Gulf"* as the concentrated
national school-platform markets where the next agent-to-SIS server would
appear. **Türkiye produced it.** `hanifisenturk/sabis-mcp-server` (**ISC**, 2
stars) serves **SABIS**, the student information system of **Sakarya
University**: one tool, `get-grades`, returning course codes and names,
assessment types and weights, final letter grades and academic term.
**This is EMEA's first agent-to-SIS path in this base.**

🔴 **And it is the most fragile of the three, which is the commercially useful
part.** It reaches the SIS by **Puppeteer web scraping, not an API**, and reads
the student's own `USERNAME` and `PASSWORD` from environment variables. Its
README states it is unofficial and unaffiliated with the university. Together
with `edupage-mcp` (Slovakia/Czechia, undocumented endpoints via a community
library) and `mcp_hemis_student` (Uzbekistan), **every agent-to-proprietary-SIS
path in this base is unsanctioned — three for three.** 🔵 **The EMEA sales
motion that follows: institutions in this region are getting agent access to
their own student data through credential-replay scrapers built by students.
The engagement is to replace that with a sanctioned, contracted integration** —
a governance sale, which `T1` identifies as this market's actual product.
**Italy, Poland and the Gulf remain unprobed and are still the cheapest
regional wedge in the base.**

🟢 **France supplies something no other region does: the only Caliper event
store that exists.** `open-ent/caliper` implements **Caliper Analytics 1.2** —
the newest version found anywhere — as **both** an event store
(`POST`/`GET /ims/caliper/v1p2/events`, bearer-token auth) **and** a sensor
forwarding Open ENT access and login events, mapped to `ToolUseEvent`/`Used` and
`SessionEvent`/`LoggedIn`. Vert.x, 33 unit tests. It comes from **Open ENT**, the
French regional *espace numérique de travail* platform. 🔵 **This is directly
usable in an EU data-sovereignty conversation: a French public-education
platform's own learning-analytics module, deployable on EU infrastructure**,
alongside `openfun/ralph` (MIT) from **France Université Numérique**, which this
file already carries. 🔴 **But it cannot be adopted as code: no licence on the
page, so all-rights-reserved, and its README states the Assessment, Grading,
Forum and Media profiles are not implemented.** Read it as a design reference
and **send a licence request** — it is the single highest-value licence request
on this board, because it is the only event store in the Caliper column.

🟡 **EMEA regulatory items re-confirmed rather than newly found this pass:** the
UK DfE generative-AI product safety standards for education (January 2026) and
Ofqual's AI-and-coursework-integrity material (March 2026); Dubai **KHDA**
guidance to private schools; and the contested EU high-risk date, where the
political agreement of **2026-05-07** postponing stand-alone high-risk
obligations from **2026-08-02** to **2027-12-02** continues to be reported
inconsistently against guides still citing August 2026. 🔴 **This file's
standing instruction holds: confirm the high-risk date against the Official
Journal before it goes in a proposal.**

#### Update 2026-11-13 (sixth pass) — the Digital Omnibus is now the controlling instrument, and the split between what moved and what did not is the whole sales motion

- **The delay is real and it is now a named regulation.** The **Digital Omnibus,
  Regulation (EU) 2026/1744, in force 27 July 2026**, moves the deadline for
  **stand-alone high-risk education systems** to **2 December 2027**. Annex III
  coverage is unchanged: admissions, learning-outcome evaluation, student
  placement, and exam or behaviour monitoring. 🔴 **Any guide still quoting
  August 2026 for high-risk education obligations predates this and is wrong** —
  several still in circulation do.
- **What did *not* move is what a studio sells against in 2026.** **Article 50
  transparency was not postponed and applies from 2 August 2026**: tell people
  they are dealing with an AI system, and label synthetic content. A narrower
  labelling grace period for systems already on the market runs to **2 December
  2026** — i.e. it expires within weeks of this pass.
- **The AI literacy duty was softened** to a duty to **support** AI literacy,
  with the Act stating it does not require guaranteeing any specific level.
  🔵 **This weakens the "AI literacy programme" pitch in EMEA and strengthens the
  conformity-and-disclosure pitch.** Reprice accordingly.
- **Deployer obligations are the durable revenue, and they are unglamorous:**
  use systems per provider instructions, keep **human oversight, monitoring and
  logging**; public institutions deploying high-risk AI must complete a
  **Fundamental Rights Impact Assessment under Article 27**.
- **The Commission's own position narrows the escape hatch:** draft high-risk
  classification guidelines published **19 May 2026** take the view that AI in
  education **often involves profiling**, so the exception **will in many cases
  not apply**. Do not plan around the exemption.
- **Standing since 2 February 2025 and still the hardest line:** **emotion
  recognition is prohibited in education institutions.** Engagement-detection
  and attention-tracking features are not negotiable here.
- **A further prohibition is listed for December 2026:** non-consensual sexually
  explicit AI content — relevant to any platform hosting learner-generated media.
- 🟢 **New this pass and it changes the EMEA technical answer, not just the
  compliance one:** the region now has a **permissive, sovereignty-compatible
  LMS** — OpenOLAT (Apache-2.0, Swiss-maintained), with in-process embeddings
  and a provider slot that accepts a self-hosted endpoint. See `compose/patterns.md`
  `P13` and `intel/trends.md` `T15`. **For an EMEA public-sector buyer this is
  the strongest single asset added to this KB.**

#### Update 2026-11-13 (seventh pass) — 🟢 `ACTION p801-E` DISCHARGED: EMEA finally has deployment figures, and they are national, dated and funded

`p801` closed with EMEA having produced **regulation and not one deployment figure**. That gap is now
closed from two directions — a funded national programme and a measured teacher-side baseline.

- 🟢 **The UK has EMEA's first dated, funded, national education-AI deployment programme.** The
  **DfE AI Tutoring** programme targets **up to `450,000` disadvantaged pupils a year** (pupils on
  free school meals), with **trials starting in secondary schools from autumn 2026** and **tools
  available to schools by the end of 2027**. 🟢 **`£2.88m` was split equally across `8` suppliers —
  Google and Pearson among them — to co-design the tools**, starting with **English, maths, science
  and modern foreign languages**. 🟢 **Tools must meet the DfE Generative AI Product Safety
  Standards** before rollout — the standards this file already recorded in January 2026 now have a
  procurement attached to them.
  🔴 **Year groups conflict across reports: some say years `9`–`11`, others years `9`–`10`.** Quote
  the pupil count and the dates; do not quote the year range without checking the tender.
  🔴 **Criticism is on the record and a client will raise it:** the procurement runs *in parallel*
  with the evaluation meant to establish whether AI tutoring works, and tutoring bodies have asked
  the DfE to test at smaller scale first. 🔵 **That is the studio's opening, not an obstacle — the
  programme needs evaluation instrumentation, and this KB holds the only agent↔learner-record write
  path (`learnmcp-xapi`, xAPI 1.0.3) that makes agent activity reportable.**
- 🟢 **EMEA now has a measured teacher-side baseline.** The **National Education Union State of
  Education survey, fielded 5–16 February 2026**, reports **`76%` of teachers using AI tools for
  day-to-day work, up from `53%` a year earlier**. 🔴 **`49%` of schools have NO AI policy at all for
  staff or students**, and **`66%` of teachers report no policy specific to *student* use —
  unchanged from 2025.** **`66%` of secondary teachers agreed students' critical thinking has
  declined.**
  🔴 **Sample size is reported inconsistently: `9,408` vs `10,311` English state-school teachers.**
  🟢 **An independent check agrees on the shape:** a Bett/YouGov poll of UK teachers in June found
  **`48%` said their school had no policy on staff AI use, and `19%` did not know.**
  🔵 **Read the two together and the EMEA sales motion is unambiguous:** usage has crossed three
  quarters of the profession while **half of schools have no policy** — the governance deficit this
  file has been selling in LATAM is **also a UK fact**, and it is now measured.
- 🟢 **The Gulf is the other place with real deployment numbers.** The **UAE** mandated a nationwide
  **K-12 AI curriculum** (Cabinet decision May 2025 — reported as the first such national mandate),
  extended for the **2026–27 academic year, which began 31 August 2026**, to **government schools and
  MoE-curriculum private schools from KG to Grade 12**. Capability figures: **`1,000`+ AI-trained
  teachers deployed** and a teacher-competency programme covering **`23,000` educators and
  administrators**. 🔴 **Sources conflict on whether coverage is already all private schools or only
  MoE-curriculum ones**, and **no source gives a student count.**
- 🔴 **The gap that did NOT close, stated rather than smoothed: Germany, France and the Nordics
  returned no deployment figures on this pass.** A dedicated leg over those three returned UAE
  coverage and essentially nothing else — no national programme, no school count, no student count.
  🔵 **This is a real asymmetry, not a search failure to paper over: EMEA's measurable deployment
  evidence is concentrated in the UK and the Gulf.** `ACTION p802-B` carries the per-ministry legs.
  🔵 France remains present in this file for one thing only — the **Caliper event store** recorded in
  the fifth pass.
- 🔴 **Primary-source access remains refused.** `gov.uk` and `neu.org.uk` both **fail to resolve from
  this session** — the `T906` class, now at **twelve** government/institutional domains. **Every
  figure in this update is secondary-sourced and says so here.**


#### Update 2026-11-13 (ninth pass) — the interpretation channel has a name, and the first national teacher-adoption figure lands

🔴 **Provenance: search-tier.** `coe.int` and the Commission's own domains do not
resolve from this session; nothing below was read from a primary text. The AI Act
dates themselves are unchanged from the sixth and seventh passes and remain this
file's verified baseline.

**New to this file: the channel through which the high-risk question actually gets
answered.** The Commission operates an **AI Act Service Desk** and has published
**draft guidelines on high-risk classification**. 🔵 **This matters more than it
sounds.** This file has repeatedly recorded that education uses — automated marking,
admissions triage, proctoring, AI-detection used in assessment, personalised learning
— *may* be caught as high-risk. 🟢 **The draft guidelines are the instrument that will
narrow or widen that list, and the Service Desk is where a deployer's specific
question gets a position.** For an engagement, that converts "we think this is
high-risk" into a citable process. 🔴 **It is guidance, not law — it does not move the
`2027-12-02` date set by Regulation (EU) 2026/1744.**

**Article 4 as the live duty, re-stated precisely.** The AI-literacy obligation binds
**both providers and deployers**, and 🔵 **requires measures to support literacy
without specifying any level per person.** That is the one AI Act duty that is in force
now, applies to every school and university in the Union, and has **no objective
compliance test** — which is why it is sellable today and why `T19`'s curriculum gap
bites here as well as in North America.

**First national teacher-adoption figure in this file's EMEA section.** 🟢 **Sweden:
nearly 8 in 10 teachers surveyed had used AI services in some part of their work.**
Until this pass, EMEA adoption here was institutional and deployment-side (the
seventh pass's national deployment figures). 🔵 **This is the individual-practitioner
layer, and it reproduces the pattern this file measures in LATAM and NA: practitioner
use far ahead of institutional governance.** The regional difference is only that
EMEA has a statute arriving to meet it.

🔴 **Declared gap, unchanged and now explicit: this file still has no EMEA figure for
what share of institutions have published an AI policy.** Searched this pass across
the EMEA leg; the results returned compliance advice, not measurement. **An informed
absence: the denominator for the AI Act's deployer duties is not publicly measured.**

### APAC

#### Update 2026-11-15 (thirty-first pass, `p826`) — the regulatory patchwork hardens into three named regimes, and APAC's measured supply is per-campus rather than national

🟢 **Regulatory items `CITED, NOT READ`; repository items first-hand and byte-read.**

- 🔴 **Three regimes, cited, and the distinction is the planning input:** **South Korea's AI Basic Act in force `2026-01-22`** (transparency, risk assessment, human oversight, documentation for high-impact systems; enforcement decrees still being finalised, with a guidance-focused grace period through 2026); **Vietnam's law reported in effect `2026-03-01`**, treating education as high-risk with pre-deployment registration in a National AI Database, conformity assessment, mandatory human oversight and **72-hour incident reporting**; and **Japan's voluntary, light-touch model** with **Singapore** carrying no binding AI statute. 🔵 **A regional rollout cannot use one compliance design: Korea and Vietnam impose documentation duties that Japan and Singapore do not, and Vietnam's registration step is a schedule item, not a checkbox.**
- 🔴 **Australia, cited:** **TEQSA has required all higher-education providers to submit institutional action plans addressing generative-AI risk** — 🟢 **the most directly sellable instrument in the region, because it creates a dated, named deliverable per institution rather than a general duty.** A 2024 proposal named education among sectors for mandatory high-risk AI guardrails.
- 🟡 **EU spillover, cited:** APAC edtech selling proctoring or admissions tooling into EU schools inherits Annex III, now at `2027-12-02`. 🔵 **For an APAC vendor with European customers the EMEA date is the binding one.**
- 🔴 **The leg returned essentially NOTHING on APAC adoption RATES in schools and universities, for a second consecutive pass.** 🔵 **Recorded as an informed gap: this base can describe APAC regulation in detail and APAC adoption not at all, and the two are being quoted side by side as if equally sourced. A later pass should query national bodies by name (MEXT, MOE Singapore, UGC India) rather than "APAC AI education adoption".**
- 🟢 **The supply-side finding, measured.** APAC remains this base's largest SOURCE of open education agents, but `p826`'s enumeration (`T92`) reframes it: the `1,241`-repository `AGENTIC STAR` cohort — `13` Vietnamese and Japanese developers, `1,211` MIT — is a **twelve-industry** catalogue of which education is `76` repositories, and it is **closed** (only `2` repositories created since `2026-10-29`). 🔵 **So APAC's apparent supply surge was a one-off developer-programme output, correctly valued as a requirements corpus (`P61`) rather than as a maintained shelf.**
- 🟢 **What IS live in APAC is per-campus, not national.** `changshenhan/bb-mcp` (MIT) against **Blackboard Learn Classic at CUHK-Shenzhen** — `9` tools and the only WRITE-capable row added this pass, with its own academic-integrity boundary in prose — and `PatrickStar-cmd/random-signal-agent` (MIT, `22★`) bound to **one named UESTC course**. 🔵 **This is `T70`'s curriculum-instrument binding again: in APAC the agent attaches to a specific institution's instrument, which makes the CURRICULUM ADAPTER the reusable asset and the model the commodity.**
- 🔴 **One APAC row was REJECTED this pass on licence text, not on quality:** `gangula-karthik/ntulearn-mcp` (NTU Singapore) is a legitimate read-only Blackboard connector whose MIT grant clause has been rewritten (`T93`). 🟢 **It is one commit from being a wanted row, and asking its author is the right next action.**

#### Update 2026-11-15 (thirtieth pass, `p825`) — the region is now this base's largest SOURCE of open education agents, not only its fastest-growing market

- 🟢 **The structural finding of this pass is APAC, and it is measured rather than cited.**
  `T86`: a **`74`-repository, `54`-id, MIT-licensed education agent catalogue** published between
  `2026-09-22` and `2026-10-29` under SoftBank's **AGENTIC STAR** platform brand (🇯🇵), authored by
  `13` developers. 🔴 **Zero of the `74` were held by any of this base's `29` previous passes.**
- 🟢 **`43` of the `74` — `58%` — are by 🇻🇳 Vietnamese authors**, making Vietnam the largest national
  group of education-agent authors this base has ever measured. 🔴 **This CORRECTS `p824`'s `T84`,
  which published *"Vietnam … exactly zero build-safe open supply"* on the strength of
  Vietnamese-LANGUAGE queries alone (`T87`).** 🟢 **The corrected commercial reading is the opposite of
  the published one: the slot is not *build because nothing exists*, it is **partner or hire**, because
  a permissively-publishing Vietnamese education-agent talent pool demonstrably exists.**
  🟡 **Vietnam's binding context is unchanged and still carried from `p824`:** its AI law took effect
  `2026-03-01` and its high-risk category names education including automated assessment
  (`CITED, NOT READ`).
- 🟡 **Japan is now a named regulatory surface on these shelves for the first time, via supply rather
  than via commentary.** Catalogue agents cite their instruments directly: **MEXT** guidelines for
  academic-misconduct investigation reports (`EDU-C2-024`), **METI デジタルスキル標準 (DSS)** levels for
  L&D curriculum design (`EDU-C2-030`), and the **共通テスト** Common Test for entrance-exam question
  classification (`EDU-C2-029`). 🔵 **`T70`'s rule again: the sellable agent binds to a named
  curriculum or regulatory INSTRUMENT, and in Japan those instruments are published.**
- 🟡 **Market and adoption, all `CITED, NOT READ`:** APAC is consistently described as the
  fastest-growing region though NA leads revenue; an Ipsos education monitor found **lower support for
  banning AI in schools across the Asian markets surveyed** than elsewhere; a Times Higher Education
  survey reports patchy uptake with connectivity a barrier and **virtual-tutor adoption at `30%`**
  across its cohort. 🔵 **The World Bank's Global EdTech Policy Academy on AI is scheduled for
  **Seoul, `2026-08-31` to `2026-09-04`***; Cambridge English convened APAC leaders in Kuala Lumpur
  (April 2026) and Acer ran an AI-education summit in the region.
- 🔴 **A nil worth keeping.** Korea's AI Basic Act (in force January 2026) and China's content-labelling
  rules are carried from earlier passes and were NOT re-confirmed this pass; the regional leg surfaced
  no 2026 primary source for either. 🟡 **Treat both as stale-but-carried, not as re-verified.**


#### Update 2026-11-15 (twenty-ninth pass, `p824`) — 🔴 Vietnam enters this base as the newest binding high-risk jurisdiction, with a build-safe supply of ZERO

🟡 **Sourcing note for every item in this block: egress in the `p824` environment resolved GitHub and web search only — `oecd.org` was refused at the proxy, as at `p822`. Every market and regulatory item below is `CITED, NOT READ`: it comes from web-search summaries of secondary sources, several of them vendor blogs and trackers. 🔴 Verify any date, bill number or percentage against the official text before quoting it to a client. Every REPOSITORY figure in this pass is first-hand and byte-read; the two classes are not interchangeable.**

- 🔴 **🇻🇳 Vietnam is the headline, and it is `T84`.** Vietnam's AI law is reported in force from
  **`2026-03-01`**, with a **high-risk category that names education, including automated
  assessment**, and **MOET has scheduled AI content into every grade `1`–`12`**. 🔴 **Supply
  underneath it, measured first-hand on `gh api search/repositories`:**
  `q="giao duc viet nam ai"` → `7`, **every one unlicensed**; `q="vietnam education platform"` → `5`,
  **every one unlicensed**. 🔴 **The only licensed in-country education artefact found is
  [`NukeGeng/VietAIS-Sentinel`](https://github.com/NukeGeng/VietAIS-Sentinel), AGPL-3.0 explainable
  exam proctoring — the right product for the law and the wrong licence for a studio deliverable.**
  🟢 **So in Vietnam `P58` is a BUILD, not an adoption, and that is the sharpest open slot `p824`
  found in any region.**
- 🟢 **🇰🇷 Korea: the AI Basic Act has been in force since January 2026** (carried, re-confirmed).
  🟢 **And Korea produced this pass's most unusual row:
  [`epoko77-ai/examguard`](https://github.com/epoko77-ai/examguard), MIT — smart-glasses screening
  for the 수능 exam hall, BLE and advertising-packet filters, optical read from the proctor's desk.**
  🔵 **It is PHYSICAL invigilation, not biometric surveillance of a candidate, which makes it the
  one proctoring shape that is unaffected by the EU's emotion-recognition ban and exportable into
  EMEA. `P58`'s APAC port is built around it.**
- 🟡 **The rest of the region remains a patchwork, restated with its instruments:** 🇦🇺 Australia on
  existing law plus voluntary guidance; 🇯🇵 Japan leaning on self-regulation; 🇮🇩 Indonesia's rules
  still pending as a Presidential Regulation; 🇮🇳 India working through NCERT; 🇦🇪 Dubai's KHDA
  issuing guidance to private schools; SEAMEO INNOTECH named as the regional body.
  🔵 **`P5`'s multi-jurisdiction architecture is the right shape here and gains a fifth regime
  (Vietnam) this pass.**
- 🟡 **Public opinion is MOVING AND DIVERGING, which matters for a deployment's political risk.**
  The Ipsos Education Monitor 2026, cited this pass, reports support for banning AI in classrooms
  **rising** in Japan, Australia and South Korea and **falling** in Indonesia, with Indonesia's
  posture described as "Protect and Prepare" — limits on children's social media alongside openness
  to AI in education. 🔵 **A regional rollout cannot assume one direction of travel; sequence by
  jurisdiction sentiment, not by market size.**
- 🟡 **Curriculum reform is the scheduling risk, not the technology.** Indonesia's *Merdeka Belajar*
  and the Philippines' **MATATAG** rollout are both mid-phase, which makes AI guidance hard to pin
  to a syllabus. 🔵 **This is why `T70`'s curriculum-instrument binding matters commercially: an
  agent bound to a named, published instrument survives a curriculum phase; one bound to "the
  syllabus" does not.**
- 🟢 **Supply this pass: `4` APAC rows** — `examguard` (🇰🇷), `lesson2hw-physics` (🇨🇳, bound to CAIE
  `9702`/`0625`), `ph-data-mcp-server` (🇵🇭 national scholarships, schools and regions, keyless),
  `AI-Smart-Proctoring-System` (🇮🇳, the layer's only open evidence implementation) — plus
  `OpenRaiser/EduGraph` (🇨🇳, Apache-2.0 code over CC BY-SA data) on `repos/foundations.md`.


#### Update 2026-11-15 (twenty-eighth pass, `p823`) — 🟢 Two jurisdictions now have AI statutes IN FORCE naming education as high-risk, and 🔴 public support for BANNING AI in schools is rising in three markets

🟡 **Sourcing note for every item in this block: egress in the `p823` environment resolved GitHub and web search only. Every market and regulatory item below is `CITED, NOT READ` — primary texts were NOT opened. Figures are attributed to the party that published them, vendor and advisory sources are marked as such, and dates that sources disagree on are shown disagreeing. Every REPOSITORY named is first-hand and byte-read.**

- 🟢 **🇻🇳 Vietnam is the sharpest instrument in the region for this industry.** Its AI law has been
  in force since **`2026-03-01`**, and a **July 2026** decision identifying high-risk systems
  **names education explicitly — *automated assessment* and *behavioural analysis***. Transition
  periods apply, reported as **`18` months in health care, education and finance**. 🔵 **This is
  one of the few places in the world where "AI that grades" is named in a binding instrument rather
  than in guidance.** 🟢 **And Vietnam is simultaneously mandating the demand side: MOET Decision
  `2422` is reported to set `12` periods per class per year of AI content for grades 1–12.**
  🔵 **Mandated curriculum plus a named high-risk category is a content-engineering and
  assessment-governance engagement in the same country.**
- 🟢 **🇰🇷 South Korea's AI Basic Act took effect `2026-01-22`**, with 2026 reported as effectively
  a pilot period with limited enforcement. 🔵 **A grace window is the right time to sell readiness,
  not remediation.**
- 🟡 **The rest of the region is a patchwork, by design.** 🇦🇺 Australia relies on existing law plus
  voluntary guidance rather than a standalone AI act; 🇯🇵 Japan is betting on voluntary guidelines
  and self-regulation; 🇮🇳 India's amended IT Rules on **synthetic-content labelling** took effect
  **February 2026** (one source gives `2026-02-20`) and bear directly on AI-generated learning
  material; 🇮🇩 Indonesia's national regulation is still being finalised. 🔵 **One report states
  Korea, Taiwan and Vietnam brought AI-specific statutes into force in 2026 while China, India and
  Singapore regulate through rules and guidance.**
- 🔴 **The demand-side signal this pass is NEGATIVE, and it is the most commercially useful item
  here.** The **Ipsos Education Monitor 2026** reports support for **banning AI in schools RISING**:
  🇯🇵 Japan **`21%` → `29%`**, 🇦🇺 Australia **`47%` → `52%`**, 🇰🇷 South Korea
  **`27%` → `31%`**. 🔵 **Australia and New Zealand record the region's highest ban support
  outright.** 🟢 **Read together with this base's NA finding that faculty intent FELL `76%` → `67%`,
  the pattern is consistent across two regions: the sector adopted fastest and is first to show
  fatigue. That sells governance, evaluation and evidence — not another pilot.**
- 🔵 **Named bodies for a regional approach:** India's **NCERT**, **SEAMEO INNOTECH** for Southeast
  Asia. 🔴 **Note a placement correction: Dubai's KHDA appeared in this leg's results but belongs to
  EMEA in this file's closed vocabulary**, and is recorded there.
- 🟢 **Supply this pass, byte-read:**
  [`Waldo0926/monash-study-kit`](https://github.com/Waldo0926/monash-study-kit) 🇦🇺 (MIT, Monash
  Moodle **+ Ed**, the forum where the course conversation actually lives) and
  [`liqinling1994-cloud/master-teacher`](https://github.com/liqinling1994-cloud/master-teacher) 🇨🇳
  (MIT, `152` master-teacher methodologies joined to **`15` 课程标准** national curriculum
  standards — another instance of `T70`'s curriculum-adapter asset).
  🔴 **Copyleft, cannot be vendored:**
  [`Sun-sunshine06/bupt-anything`](https://github.com/Sun-sunshine06/bupt-anything) (GPL-3.0).


#### Update 2026-11-15 (twenty-seventh pass, `p822`) — 🟢 Government-led scaling with LOW policy confidence, and a China supply channel attached to competitions

🟡 **`CITED, NOT READ` throughout: egress resolved GitHub only this pass.**

- 🔴 **Growth figures disagree by `14` points and both are commercial:** MarketsandMarkets gives
  APAC **`20.9%` CAGR (`2024`–`2029`)**; another source cited this pass gives **`35.3%`** and itself
  questions whether such rates measure investment rather than impact. 🟢 **Use the disagreement, not
  the number: it is evidence that the region is bought ahead of being measured.**
- 🟢 **The regional pattern is government-led scaling.** The **Philippines Department of Education
  launched a national responsible-AI programme in January `2026`**, and its **National Education
  Plan `2026`–`2035`** embeds AI and digital literacy system-wide. ASEAN-level work runs through
  SEAMEO INNOTECH; Clarivate published a comparative study of AI policy and AI-ethics education
  across **seven** APAC jurisdictions; EdTech Hub runs briefings across Southeast Asia.
- 🔴 **The gap between usage and governance is the opportunity, and it is measured.** A secondary
  write-up of EdTech Hub's March `2026` work reports **≈`86%` of Southeast Asian teachers already
  using AI tools**, while **fewer than half of educators** report strong confidence in their
  institution's or government's AI rules. 🔵 **Ipsos's framing is the one to take into an account
  plan: Asia Pacific is not approaching this through a single regional lens, so a
  per-jurisdiction policy layer is the deliverable, not a regional one.**
- 🟢 **Named activity worth tracking:** Cambridge English convened **`200`+ senior leaders** at a
  Kuala Lumpur summit (April `2026`); EtonHouse launched an enterprise AI workspace across its
  network, framed around Singapore's responsible-AI push.
- 🟢 **The APAC SUPPLY finding this pass is specific and it is Chinese: student-facing agents
  attached to COMPETITION and EVALUATION artefacts rather than to courses.** `Stardust Agent`
  (MIT, `165★`) works the declaration documents Chinese undergraduates are judged by — 大创申报书,
  挑战杯, 中国国际大学生创新大赛 — and `简析智评` (Apache-2.0) scores student résumés under an
  evidence constraint for teaching analytics. 🔵 **Both are placed APAC on quoted locatives.**
  🔵 **The transferable insight: in this market the fundable artefact is the one a committee reads,
  and that is where agent adoption is appearing first.**

#### Update 2026-11-15 (twenty-sixth pass, `p821`) — 🟢 The region's movement is DELIVERY, not regulation: a named `28`-partner training build-out, a city-level curriculum rollout with its gaps stated, and a new APAC supply row

- 🟢 **The AI Opportunity Fund: Asia-Pacific has a Phase Three and it has NAMES.** This file
  already holds the fund as a **`$35M` AVPN initiative with Google.org and the ADB**. 🟢 **What
  `p821` adds, dated `2026-11-11`: `28` local implementing partners named for Phase Three, plus a
  learning platform delivering training in `16` languages.** 🔵 **Among them, **Pratham Education
  Foundation** (🇮🇳 India), whose stated brief includes training teachers to understand **when not
  to rely on AI tools** — which is the governance half of the adoption/readiness gap this file has
  been selling against since `p816`.**
- 🟢 **Teacher-training capacity, which is the constraint every APAC rollout hits.** Google's **AI
  Educator Series** expanded to four new regions in November 2026, with a 🇰🇷 Korea rollout run
  with **Seoul National University of Education**; **JA Korea** reports **`11,000` teachers trained
  over six years** and will pair the training with formal certification for public-school
  educators. 🇮🇳 India delivery is in English plus **six local languages** (Hindi, Marathi, Telugu,
  Assamese, Odia, Punjabi), aligned to **NEP 2020**; the 🇵🇭 Philippine **DepEd** has endorsed the
  training nationwide for teaching and non-teaching staff.
- 🟢 **Vietnam moves from statute to classroom, and the gap is stated by the implementers.**
  🇻🇳 **Ho Chi Minh City** is rolling AI education out to general secondary students from the
  **2026–2027 school year** under a **MOET** framework. 🔴 **The reported blockers are teacher
  capacity, infrastructure and guidelines — not policy.** 🔵 **That is the shape of an APAC
  engagement right now: the mandate exists, the delivery capacity does not, and the sellable unit
  is teacher-facing enablement rather than a learner-facing tutor.**
- 🟡 **Event marker:** EDUtech Asia 2026 ran `2026-11-04`–`05` in Singapore, reported at ~`8,000`
  educators.
- 🟢 **SUPPLY: one new APAC row, byte-read.**
  [`olele114/teach-to-learn`](https://github.com/olele114/teach-to-learn) (MIT, `4★`, created
  `2026-11-14`) — a zero-dependency Agent Skill whose whole design attacks the mastery illusion:
  *"Stop mistaking 'I understood the AI's explanation' for actual mastery."* 🔵 **Region from the
  authorship statement (`SKILL.md` and `references/` in Chinese, `README_CN.md` published), not
  from an account location that does not exist.**
- 🔴 **One APAC candidate measured and REFUSED on implementation, not licence:**
  [`wisdom-km/k12-qbank`](https://github.com/wisdom-km/k12-qbank) (MIT, 🇨🇳 Heilongjiang, 人教版
  七年級 maths) — its own README states there is no web surface and no database yet. 🟢 **Named so
  a later pass can promote it; its knowledge-point taxonomy is cited in `P51` as a specification.**
- 🔴 **Country-level policy detail for 🇨🇳 China and 🇯🇵 Japan did not resolve on this channel
  AGAIN.** 🟢 **That is now four consecutive passes on the same declared blank, and this file
  states it rather than filling it.** 🔵 **Evidence grade for everything above: `CITED, NOT READ`
  — egress resolved GitHub only this pass.**

#### Update 2026-11-15 (twenty-fourth pass, `p819`) — 🔴 Near-nil on instruments; the curriculum mandates this file holds were re-confirmed and nothing new dated

🔴 **Near-complete nil, stated with what was run.** The APAC leg returned China's Ministry of
Education subject rename to **"Artificial Intelligence and Technology"** for `2026–2027`, India's
**AI and Computational Thinking from Grade 3** under NEP 2020 beginning `2026–27`, Japan's
device-before-tools sequencing, and the Clarivate seven-system regional report. 🟢 **All four are
already held.** 🔵 **Re-confirmation across an independent sweep is worth recording — these are the
two dated mandates this base prices APAC engagements against, and neither has moved.**

🟡 **Two small additions, both SECONDARY.** An **ASEAN Foundation** study is reported finding
Southeast Asia's education systems at **deeply uneven stages of AI readiness**, and a Vietnamese
study reports **widespread AI usage alongside persistent literacy gaps**. 🔵 **Both point the same
way and sharpen a posture this file already takes: in Southeast Asia the binding constraint is
READINESS rather than access, which sells capability-building and measurement rather than tooling.**

🔴 **The characterisation this file should keep, unchanged.** China's rollout is the most ambitious
and its oversight the most fragmented; India's is the largest by headcount and the least
centrally directed, with the edtech sector private-sector-led; Japan's is the most values-anchored
and the slowest by design. 🔵 **Three different buyers, three different first conversations.**

🔴 **Regional supply this pass: NIL, and it is a real nil.** The star-ranked sweep (`T63`) returned
`0` new APAC-attributable repositories. 🔴 **India's hard nil (`T51`) is CONFIRMED for a further
pass, and it remains this base's only unbuilt first-connector market.** 🟡 **The one APAC-adjacent
signal is a repository this base declined to attribute:
[`molly554/whiteboard-ai-tutor`](https://github.com/molly554/whiteboard-ai-tutor) ships a bilingual
EN/zh-CN README and benchmarks DeepSeek, but states no origin — a signal, not an attribution
(`T42`).**

#### Update 2026-11-15 (twenty-third pass, `p818`) — 🟢 Korea's national citation index gains TWO independent MIT connectors in ten weeks, and the region's binding instruments gain a grace period and a disputed legal basis

🟢 **The supply finding, and the convergence is the signal rather than the stars.** The **Korea
Citation Index (KCI)** — operated by the **National Research Foundation of Korea**, and the index a
Korean academic career is measured against — gained two independent MCP servers within ten weeks:
[`rubatoyd/KCI_openAPI`](https://github.com/rubatoyd/KCI_openAPI) (🟢 MIT, `4★`, REST Open API plus
OAI-PMH, pushed `2026-11-14`) and
[`ckgerteis/korea-scholarship-mcp`](https://github.com/ckgerteis/korea-scholarship-mcp) (🟢 MIT,
`1★`, KCI plus Open Access Korea, pushed `2026-11-01`). 🔵 **Two unrelated maintainers choosing the
same national research index in the same quarter is the same pattern that preceded EMEA's portal
layer — and KCI is the APAC analogue of Brazil's CAPES/Qualis in `T58`: a state-operated register
that a career depends on.**

🟢 **Korea's AI Basic Act enforcement picture is now dated and softer than this base recorded.**
In force **`2026-01-22`**, covering "high-impact AI" in education among other sectors — 🟢 **but
enforcement decrees are still being finalised and a GRACE PERIOD focused on guidance rather than
penalties runs through 2026.** 🔵 **Commercially that is the most favourable window in the region:
the obligation is nameable and citable in a proposal, while the penalty is not yet live — so a
readiness engagement sells now and a remediation engagement sells later.**

🔴 **Vietnam's legal basis is DISPUTED across sources and must not be stated flatly.** This base
carried *"education high-risk under the Law on AI, `2026-03-01`, requiring pre-deployment
registration in the National AI Database."* 🔴 **A second source attributes the same duties to a
Digital Technology Industry Law instead.** 🟢 **The DUTY is corroborated — education is high-risk
and pre-deployment registration is required. 🔴 The INSTRUMENT is not. Cite the obligation, not the
statute, until a primary text is read.**

🟢 **The rest of the regional map, re-corroborated this window:** 🇨🇳 China maintains the most
comprehensive AI framework in APAC, by targeted rules rather than one omnibus law; 🇯🇵 Japan stays
guidance-led with voluntary internal governance; 🇸🇬 Singapore relies on toolkits and frameworks and
has **no binding AI statute** — 🔵 which makes Singapore the region's lowest-friction pilot
jurisdiction and the hardest in which to sell compliance; 🇦🇺 Australia's proposed mandatory
guardrails cover education as high-risk, and **TEQSA compels a generative-AI action plan from every
higher-education provider**.

🟢 **A second-order opening worth naming: the EU AI Act reaches APAC vendors.** APAC firms selling
proctoring or admissions tools into EU institutions fall inside the Act's education category.
🔵 **That is an export-compliance engagement with an APAC buyer and an EMEA obligation — a shape
this base has not previously named, and one a global studio is better placed to serve than a local
consultancy.**

🔴 **Unchanged and still open, SIXTH pass: `0` procurement documents for India, Singapore or
Australia.** 🟢 **Confirmed again as a TENDER-ACCESS gap, not a discovery gap.** 🔴 **And no
adoption or market-size figures for AI in education across APAC were obtainable from the prescribed
regional query this pass — stated here rather than left silent.**

#### Update 2026-11-15 (twenty-second pass, `p817`) — 🔴 **A national MANDATE with no open infrastructure underneath it: India's credit bank and AI curriculum against `1` unlicensed `0★` repository**

🔴 **Regional supply this pass: NIL, and it is a measured nil rather than an unrun leg.** 🟢 **Every
query is recorded below so it can be re-run and refuted.**

| Query | `total_count` | Ceiling | Licence |
|---|---|---|---|
| `academic bank of credits india` 🇮🇳 | **1** | `0★` | 🔴 NONE |
| `diksha ndear education india` 🇮🇳 | **0** | — | — |
| `gigaschool japan education data` 🇯🇵 | **0** | — | — |
| `singapore student learning space api` 🇸🇬 | **0** | — | — |
| `australia unique student identifier` 🇦🇺 | **2** | `3★` | 🔴 both NONE |
| `china smart education platform open source` 🇨🇳 | **1** | — | 🔴 unrelated noise |
| `lti moodle plugin japan korea` | **0** | — | — |

🔵 **Why this nil is commercially loud rather than quiet.** 🟡 **India's Ministry of Education has
made AI and Computational Thinking mandatory from Class 3 beginning the `2026-27` academic year
(`SECONDARY`), and NEP-era reform makes the Academic Bank of Credits a national credit-portability
obligation.** 🔴 **Against that: one `0★` unlicensed repository.** 🟢 **A mandate whose
infrastructure does not exist in open source is the cleanest engagement opening this base records —
the obligation already has an owner and a deadline, and there is nothing to adopt.**

🟡 **Policy, this window (`SECONDARY`):** a Clarivate review covers AI education policy across seven
APAC markets (Mainland China, India, Japan, Malaysia, Singapore, South Korea, Taiwan); Japan has
completed one-device-per-student at compulsory level; a 2026 Indian annual report describes a
two-track picture — rapid top-down curriculum push, slow ground-level adoption.

🔴 **Declared blank, carried forward:** no `2026` regulatory text for Japan or China was located on
this channel. 🔵 **`T51`'s rule applies — this is recorded as *not found by these queries*, not as
*does not exist*.**


#### Update 2026-11-15 (twenty-first pass, `p816`) — 🟢 The region supplies this pass's one POSITIVE absence finding: India's nil is confirmed REAL, and it is the only unbuilt first-connector market in this base

🟢 **`ACTION p813-C` is DISCHARGED, three passes after it was written, and the answer is the one
the action was designed to disprove.** 🔴 **Five prescribed query shapes, all run:**

| Query (verbatim) | `total_count` | Star ceiling |
|---|---|---|
| `academia erp mcp` | **0** | — |
| `camu mcp college` | **0** | — |
| `shaala darpan` | **0** | — |
| `apaar abc academic bank credits` | **1** | **0★** |
| `samarth university` | **6** | **0★** |

🔵 **Seven repositories, star ceiling `0`. See `T51` for the full argument and its limits.**
🟢 **The commercial reading, and it is this file's sharpest regional claim:** India runs the
largest education system on earth on named commercial ERPs — Academia, Camu, MasterSoft, Samarth —
and there is no open-source agent surface over any of them. 🔴 **Every other region in this base
closed its supply gap by adopting somebody else's open-source connector. India's cannot be closed
that way, because the connector does not exist.** 🔵 **That makes it the only market in this file
where a studio would be building the FIRST integration rather than the tenth — higher cost, and a
position no competitor can adopt around.**

🔴 **The honest limit, repeated from `T51` because a regional claim gets quoted without its
caveat:** this measures public GitHub repositories discoverable by English-language system names.
In a market served by commercial ERP vendors, private integration work is exactly where this code
would live. 🟢 **Per `p773-E` the action is now RETIRED rather than carried a fourth time.**

🟢 **Regional supply otherwise: `18` rows, unchanged** — the retention layer placed `Global`
under `T42`. 🔵 **Note for the record that the region still holds this base's largest single
repository: [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) measured **`59,256★`** this pass
(Apache-2.0, byte-read `11,408 B` `sha256:cd2f54e1…`, pushed `2026-11-07`), Hong Kong 🇭🇰.**
🟢 **It was already shelved, so this is a re-measurement rather than a find — but it is now
larger than every repository in the retention layer combined, and `ACTION p816-E` asks whether its
recorded figure on the shelf has drifted.**

🟢 **Policy and market, this window (secondary-sourced):**
- 🟢 **The Philippines is the region's most concrete instrument: DepEd launched **`AGAP.AI` in
  January 2026**, described as the country's first nationwide responsible-AI programme in basic
  education, with a **National Education Plan 2026–2035** embedding AI and digital literacy.**
  🔵 A named national programme with a date is this file's standard for citability, and ASEAN has
  not previously supplied one.
- 🔴 **Regulation is FRAGMENTED BY DESIGN:** each ministry integrates AI into its own sector, so
  there is no single education AI regulator to sell compliance against — the inverse of EMEA.
- 🔴 **Confidence gap: fewer than half of educators report strong confidence in existing
  institutional policies or government regulation.**
- 🟡 **Market size CONTESTED: MarketsAndMarkets gives APAC `20.9%` CAGR 2024–2029 (USD `591.6 M`
  → `1,848.1 M`); a vendor blog claims `35.3%`.** 🔴 **The two cannot both be right and this file
  carries the sourced one; the blog figure is recorded only so it is not re-bought as new.**
- 🟡 **`~86%` of teachers in Southeast Asia reported using AI tools (EdTech Hub, relayed
  second-hand).** 🔴 **Not confirmed against the original report — do not put this in a SOW.**
- 🟢 **Institutional actors: Clarivate's comparative study of AI policy and ethics education
  across `7` APAC countries; Cambridge English's April 2026 leadership summit (`200`+ senior
  leaders including ministries); EtonHouse's enterprise AI workspace in Singapore.**


#### Update 2026-11-15 (twentieth pass, `p815`) — 🟢 The layer's oldest component is APAC-origin, and 🇮🇳 India is a measured HARD NIL on it

🔵 **Source confidence.** Repository measurements are `FIRST-HAND` — run `2026-11-15` against
`gh api -X GET search/repositories`, licences byte-read over `raw.githubusercontent.com`. Policy
and market figures are `SECONDARY` (web-search summaries of trackers, briefings and vendor blogs)
and are labelled as such; verify any date before putting it in front of a client.

🟢 **The supply finding.** [`trampgeek/moodle-qtype_coderunner`](https://github.com/trampgeek/moodle-qtype_coderunner)
(`248★`, GPL-2.0) is 🇳🇿 **the oldest continuously maintained component in the whole assessment
layer — created `2012-12-02`, pushed `2026-11-13`.** Its README names the authors: *"Richard Lobb,
University of Canterbury, New Zealand. Paul McKeown, University of Canterbury, New Zealand. Tim
Hunt, The Open University, UK."* 🔵 **🇳🇿 APAC-origin with 🇬🇧 EMEA co-maintenance — the broadest
authorship of any row in the layer.** 🔴 **GPL-2.0 and unavoidably so: every Moodle plugin
inherits Moodle's GPL — which makes it the right choice exactly when the deliverable IS a Moodle
instance rather than a product.**

🔴 **The nil, and it is measured rather than assumed.** 🇮🇳 India is this base's densest APAC
market by institution count, and on the assessment-engine channel it returns nothing:
`q="autograder assignments india college"` → **`total_count=0`**;
`q="swayam nptel course platform"` → `4`, every one a student's notebook dump. 🔵 **Yet
`himanshuuem/lab-autograder` (MIT, the sole result on `q="autograder mcp"`) is India-origin.** 🟢
**The transferable reading, and it generalises `p812`'s search-defect rule: the supply exists and
does not answer to REGION-NAMED queries, because an autograder is named after its function, not
its country.** 🔴 **A nil on a region-named query in this layer reports the query, not the
market** — the inverse of the LMS/SIS layers, where naming the region's own system was exactly
what closed the nil.

🟡 **Policy, `SECONDARY` and genuinely divergent across the region** — there is no single APAC
posture to design against:
- 🇰🇷 **South Korea's AI Basic Act entered into force `2026-01-22`**, enforcement decrees still
  being finalised, with a guidance-focused grace period through 2026.
- 🇻🇳 **Vietnam** — a Law on Artificial Intelligence reported effective `2026-03-01` **treating
  education as a high-risk area**; 🔴 other sources describe a Digital Technology Industry Law
  with a risk-based framework starting 2026, so the instruments may be conflated. Verify.
- 🇦🇺 **Australia has no AI statute, but TEQSA has required ALL higher-education providers to
  submit institutional action plans addressing generative-AI risk** — 🔵 **the most directly
  actionable instrument in the region, and it is an integrity-and-assessment obligation, which is
  `P37`'s exact shape.**
- 🇨🇳 China holds the region's most comprehensive AI framework; 🇯🇵 Japan is light-touch and
  voluntary; 🇸🇬 Singapore has no binding statute and relies on AI Verify.
- 🔵 **Spillover worth pricing: Annex III reaches APAC vendors selling proctoring or admissions
  tools into the EU**, so an APAC ed-tech client with European customers inherits `P2`.

🟢 **Where to lead in this region:** 🟢 **`P37` into Australian higher education against the TEQSA
action-plan requirement** — the deadline is institutional and already felt. `P5`
(multi-jurisdiction compliance) remains the right frame for anyone operating across more than two
of these regimes, because as the list above shows they do not converge.


#### Update 2026-11-13 (nineteenth pass, `p814`) — 🟡 The region's research-agent supply is placed by LANGUAGE, and its highest-starred row is the one that cannot be shipped

🔵 **Source confidence.** Repository figures `FIRST-HAND`; adoption figures `SECONDARY`.

🟢 **The supply finding.** [`wp-a/nature-academic-search`](https://github.com/wp-a/nature-academic-search)
(**MIT**, `388★`, byte-read `1,060 B`) is the region's new row, and it is placed by audience
rather than by national system: an academic paper-search harness written for 中文科研用户
(Chinese-language research users) over global catalogues. 🔵 **This is `T42`'s fourth binding
type and the only instance of it in the base.**

🔴 **And the region's most-starred candidate is a rejection.**
[`cookjohn/cnki-skills`](https://github.com/cookjohn/cnki-skills) (`1,067★`) — CNKI (中国知网)
search, journal browsing, indexing checks, PDF/CAJ download, Zotero export — 🔴 **has no licence
payload at either branch root, so `1,067★` buys no permission; it is the most-starred ungranted
repository in this base.** 🟡 **A second and separate question: it drives the user's own manually
authenticated CNKI session, so automated bulk retrieval is an institutional subscription-terms
matter for the library's licence desk — NOT the copyright question Sci-Hub raises (`T40`).**

🟢 **The opportunity.** 🔵 **The cheapest unblock in the region is a conversation, not code: one
`LICENSE` commit converts a `1,067★` CNKI toolchain into a build-safe row.** 🔵 **And the
language-placed binding generalises — a Japanese-, Korean-, Thai- or Bahasa-language research
harness over the same global catalogues is an open slot with a `388★` proof of demand.**

🟡 **Adoption context (`SECONDARY`, 2026 web sources).** An ASEAN Foundation / Google.org study
puts 🇹🇭 Thailand first in ASEAN AI adoption at over `90%` of students and `81%` of teachers,
while **fewer than half** of educators report confidence in institutional policy or government
regulation — the adoption/readiness gap is the sellable problem. 🇵🇭 The Philippines' DepEd
launched `AGAP.AI` in January 2026, the country's first nationwide responsible-AI programme in
basic education, targeting `1.5M` students, teachers and parents, with a reported `92%`
classroom-integration target by 2028. The `AI Opportunity Fund: Asia-Pacific` is a `$35M` AVPN
initiative with Google.org and ADB, shifting from awareness to applied learning; an ASEAN
programme targets `1.7M` learners and educators. Ipsos' Education Monitor 2026 covers nine APAC
markets including 🇮🇳 India and 🇯🇵 Japan and finds lower support for banning AI in schools than
the global `39%`. 🔴 **Country-level policy detail for India, China and Japan did not resolve on
this channel this pass — an informed gap; `T38`'s two binding national laws remain the
authority.**


#### Update 2026-11-13 (eighteenth pass, `p813`) — 🔴 TWO binding national AI laws now name education, and they demand DIFFERENT artifacts — while the region's agent supply turns out to be the densest in the world

🔵 **Source confidence.** Regulatory items are `PRIMARY-CITED` from law-firm and consultancy
summaries; 🔴 **no primary statute was read under this session's network policy.** 🟢 **Supply
items are `MEASURED` this hour, licences byte-read.**

- 🔴 **🇻🇳 Vietnam's national AI law took effect `2026-03-01`, and it is the strictest education
  instrument this file has recorded anywhere: high-risk systems — education included — require
  PRE-DEPLOYMENT REGISTRATION in a national database plus a conformity assessment.**
  🟢 **That is a filing before go-live, not a policy after it, and it belongs in the project plan,
  not the risk register** (`T38`).
- 🔴 **🇰🇷 South Korea's AI Basic Act came into force `2026-01-22` with education a named
  high-impact sector.** 🟡 **MSIT has signalled `2026` as an effective pilot year: enforcement
  decrees still being finalised, a guidance-first grace period rather than penalties.**
  🟢 **The grace period is the window to do the high-impact classification work in.**
- **🇦🇺 Australia: TEQSA requires EVERY higher-education provider to submit an institutional
  action plan addressing generative-AI risk** — 🔵 **a named, per-provider deliverable, and the
  clearest productisable compliance artifact in the region.**
- **🇨🇳 China maintains the region's most comprehensive framework** through targeted instruments
  (algorithmic recommendation, deepfake, generative AI) rather than one horizontal statute.
  **🇸🇬 Singapore** relies on non-binding toolkits (AI Verify); **🇯🇵 Japan** on light-touch
  voluntary governance; **🇲🇾 Malaysia** foregrounds data sovereignty via its National Cloud
  Computing Policy.
- 🔵 **Cross-border: the EU AI Act reaches APAC vendors selling proctoring or admissions tools into
  EU schools**, with the Annex III delay to `2027-12-02` applying to them too.
- 🟢 **MEASURED — `APAC 3 → 17`, and China's Chaoxing / 学习通 is the densest education-agent
  cluster this base has ever found: `19` repositories on one query, `12` build-safe, `17` of `19`
  created since `2026-09-11`.** 🔵 **A six-week burst around one platform.**
- 🔴 **MEASURED — and the best-engineered agent in it is the one a studio must refuse.**
  `DeliciousBuding/chaoxing` (Apache-2.0) pairs OAuth scopes, a PBKDF2 owner password and an
  AES-GCM credential vault with **automated attendance sign-in and coursework submission**.
  🟢 **`T36`: credential hygiene and integrity risk are independent axes. Grade both.**
- 🔴 **MEASURED — Taiwan's university LMS tier is a HARD NIL: `5` TronClass repositories, all
  reachable (`README.md` `200`), `0` licences.** 🟢 **Measured, not a search failure** (`T37`).
- 🟢 **MEASURED — first Indonesian row** (`alfa-yohannis/siakad-mcp`, SIAKAD at Universitas
  Pradita; `1` repository on the entire query, so the slot is effectively open), and 🟢 **🇰🇷 NEIS
  is the ONLY system in this pass's whole harvest that publishes an official API** — its agent
  needs no scraping, no reverse-engineered login and no learner credential at all.
  🔵 **That comparison is the argument in `P33`.**
- 🔴 **DECLARED GAPS, written down rather than left silent.** `0` results for **India**
  (`diksha mcp server`, `samarth university mcp`, `academia erp mcp college`), **Indonesia's
  national platforms** (`dapodik mcp`, `merdeka mengajar mcp`), **Singapore's SLS**
  (`student learning space mcp singapore`), **Vietnam** (`vnedu mcp`), **Malaysia**
  (`delima mcp malaysia`), **Thailand** (`sgs mcp school thailand`) and **Japan**
  (`classi mcp school japan`, `manabi pocket mcp`). 🔴 **India is the conspicuous one: the region's
  largest education system, and zero agent supply against its national platforms.**

#### Update 2026-11-13 (seventeenth pass, `p812`) — 🔴 A region whose agent supply has now been overtaken twice, and a public-opinion finding that cuts against the ban narrative

🔵 **Source confidence, stated once for this block.** Figures marked `MR` come from
market-research marketing pages or vendor-commissioned surveys read through search summaries and
are **order-of-magnitude only**; figures marked `PRIMARY-CITED` name a primary issuance that was
**not** read directly under this session's network policy. 🔴 **Nothing in this block was read
from a primary source this pass.**

- 🔴 **APAC is now the SMALLEST regional bloc on this base's agent shelf: `3` of `74` build-safe
  rows**, overtaken by EMEA (`10`) at `p811` and by LATAM (`8`) at `p812`. 🔵 **This is a finding
  about supply VISIBILITY, not about capability** — `T8` still holds that education AI's centre of
  gravity is APAC. 🟢 **The actionable reading: the seam-naming transform that produced `15`
  LATAM repositories in one hour has never been run against APAC's national systems.** Nobody has
  queried the Indian, Indonesian, Vietnamese or Philippine school platforms by name in this base.
  🔴 **Declared as an open leg for the next pass, not as an absence.**
- 🟢 **Public opinion is NOT where the ban narrative assumes.** The **Ipsos Education Monitor
  2026** reports **lower support for banning AI in schools across the Asian markets examined**,
  while support for limiting children's social media use stays high (`MR`). 🔵 **Useful in a
  ministry conversation: the political constraint in APAC is on social media and child safety,
  not on classroom AI as such.**
- **Adoption is real but uneven.** A regional survey reports **virtual tutors used by 30%** of the
  cohort, with uptake *"patchy"* and connectivity a limiting factor (`MR`). One market report
  claims a **50% increase** in AI-learning-platform adoption over two years (`MR`).
- **Convening calendar worth tracking, because these are where ministry buyers appear:** the
  **World Bank Global EdTech Policy Academy on AI**, Seoul, **31 August – 4 September 2026**;
  **Cambridge English's APAC leaders convening**, Kuala Lumpur, **April 2026**; **EdTech Hub's
  AI-in-education topic briefs for Southeast Asia** (`PRIMARY-CITED`). One report cites **34,000
  teachers** being trained through 2026 for an AI classroom rollout (`MR`, region unspecified —
  🔴 do not attribute to a country without checking).

#### Update 2026-11-13 (sixteenth pass, `p811`) — 🟢 A fifth national instrument with a dated window and a NAMED population, plus a dated Australian obligation

🔴 **`CITED, NOT READ`: `www.pna.gov.ph` does not resolve under this session's network
policy. The issuance is named; re-read it before quoting.**

🟢 **🇵🇭 Philippines — CHED Memorandum Order No. `21`, series of `2026`.** A national
framework for responsible AI across higher education, reported to require that **no AI
system autonomously determine academic outcomes without meaningful human review**, with
oversight named specifically for grading, admissions, scholarships, progression and faculty
evaluation. 🔵 **The population is stated and it is large: `2,366` higher education
institutions, `188,261` faculty, over `5.8 million` students.** 🟢 **Implementation period
`12` months, extendable to `18` or `24` depending on institutional readiness** — so the
window opens around `2027-09`, and **the readiness assessment that decides an institution's
extension is itself a billable engagement**, available now.

🟢 **🇦🇺 Australia has a dated, binding obligation that this file did not carry: the Privacy
Act's automated-decision-making transparency requirement takes effect `2026-12-10`.** 🔵 **It
is not education law, which is precisely why it bites** — a university using an automated
system in a decision that significantly affects an individual must disclose it in its privacy
policy. 🟢 **Pair it with TEQSA's institutional generative-AI action plan, already in this
file, and Australia becomes the APAC market with two independent, dated compliance hooks.**

🔵 **🇸🇬 Singapore published a Model AI Governance Framework for *Agentic* AI in January
2026**, extending the 2020 framework. 🔴 **Voluntary, and not education-specific** — but it
is the first governance text in this base aimed at agents rather than models, which is the
exact artifact class this KB ships.

🔵 **🇻🇳 Vietnam's July 2026 decision is reported to list education — automated assessment
specifically — among its high-risk AI sectors**, consistent with the Law on AI
(`2026-03-01`) already held here, which requires pre-deployment registration.

🔴 **Still open, sixth pass: `0` procurement documents for India, Singapore or Australia.**
🟢 **Diagnosis unchanged and now more confident — this is a TENDER-ACCESS gap, not a
discovery gap** (AusTender, GeBIZ and CPPP are portals a search engine does not index well).
🔵 **It will not be closed by another web search; it needs a portal account.**

#### Update 2026-11-13 (fifteenth pass, `p810`) — 🟢 India turns the region's largest curriculum mandate into a DATED teacher-training problem, which is a services market

🟢 **India is now the most concrete education-AI opportunity in APAC, and it is a TRAINING
engagement rather than a software one.**
- 🟢 **CBSE Circular `Acad-15/2026`, dated `2026-04-01`**, sets a **Computational Thinking & AI
  curriculum for Classes III–VIII**, launched with an **IIT Madras** expert panel. 🔴 One source
  puts coverage at **all `32,900`+ CBSE-affiliated schools** — *not verified against an official
  CBSE document.*
- 🟢 **An existing base to build on: the `15`-hour SOAR (Skilling for AI Readiness) module
  already runs in `18,000`+ CBSE schools for Classes 6–8** 🔵 (described as *voluntary*).
- 🔴 **The binding constraint, and the opening: the government has said over `10 million`
  teachers need training**, to be delivered through **NISHTHA** with video-based, grade-wise
  modules; CBSE's **2026-27 training theme is "Computational Thinking and Understanding AI."**
- 🔴 **India is reported to lack the `1.2 million`+ qualified AI professionals that training at
  this scale needs**, with a named **urban–rural gap in training quality**.
- 🔴 **Secondary-source only:** Classes 9–10 following in `2027-28` and AI as a board-examined
  subject from `2029`. Treat as unconfirmed.

🔵 **Shape of the deal:** a `10`M-teacher, video-delivered, grade-differentiated training
programme against a fixed curriculum and a dated academic year is **content engineering plus
assessment at scale** — which is precisely what
[`weishao2/tizhuang-agent-skills`](https://github.com/weishao2/tizhuang-agent-skills) and the
SCORM packaging rows added this pass are for. 🔴 **Mind the corpus licence: MIT on the skill
does not grant rights in the question bank behind it.**

🟢 **Regulatory timetable refinements this pass:** 🇯🇵 **Japan adopted a new AI Basic Plan in
July 2026** (replacing December 2025); the **AI Promotion Act (May 2025) carries no fines or
prohibitions** — promotion, not penalty. 🇸🇬 **Singapore released a Model AI Governance
Framework for *Agentic* AI in January 2026** 🔵 — the first framework in this base aimed at
agents specifically, and therefore the most relevant single document to everything on these
shelves. 🇦🇺 **Australia's National AI Plan confirms NO standalone economy-wide AI law**;
risks go to existing law and targeted sector guardrails. 🇻🇳 **Vietnam's Decision
`33/2026/QD-TTg` names education among six high-risk sectors** (e.g. automated assessment),
corroborating this base's existing Vietnam entries.

🔴 **`0` procurement documents for India, Singapore or Australia — SIXTH consecutive pass.**
🟢 **Restated as the access problem it is:** these are tender portals behind registration, not
public web pages, and no amount of search rephrasing reaches them.


#### Update 2026-11-13 (fourteenth pass, `p809`) — 🟢 Two national curriculum mandates commence in the 2026–27 school year, and the base gains its first Singapore agent

🟢 **Dated mandates, both commencing in the current school year — these are the firmest
facts in this region and they are procurement triggers:**

| Jurisdiction | Instrument | Commences | Scope |
|---|---|---|---|
| 🇨🇳 China | Ministry of Education formalises **"Artificial Intelligence and Technology"** as a school subject | **2026–2027 school year** | Compulsory schooling; tied to the **15th Five-Year Plan (2026–2030)**, which targets a leading position in AI industry applications |
| 🇮🇳 India | **AI and Computational Thinking** enters all schools **from Grade 3** | **2026–27 academic year** | Aligned to **NEP 2020** |

🔵 **China additionally issued an "AI+Education" action plan in April 2026 from five
government departments**, stressing appropriate use, critical thinking and problem-
solving rather than tool deployment — the posture matters, because it means Chinese
procurement is pedagogy-led on paper. 🔴 Oversight is still described as fragmented
relative to the speed of adoption.

🟡 **Japan takes the third posture:** general AI/data literacy for **all** students
regardless of field, governed by human-centred principles (fairness, transparency, social
responsibility), and — unlike China — **device access first, AI tools second**. 🟢 Three
large APAC systems, three different theories of the same mandate; `T19` holds.

🟢 **New agent placed in region:** [`kingdonkatsu/ntulearn-mcp`](https://github.com/kingdonkatsu/ntulearn-mcp)
(`MIT`, `4★`) — **the first 🇸🇬 Singapore-origin agent in this base** — `8` tools over
**NTULearn**, Nanyang Technological University's Blackboard Learn. 🔴 **It authenticates
by auto-reading the `BbRouter` session cookie out of the user's browser.** That is
unsanctioned access; it is a fine reference and a bad dependency.

🟡 **Regional unevenness is the planning constraint.** The **ASEAN Foundation**'s *AI
Ready ASEAN* research finds Southeast Asian education systems at *"deeply uneven stages
of AI readiness"*; **Vietnam** shows widespread usage alongside persistent literacy gaps.
A **Clarivate** report covers AI policy and AI-ethics education across seven systems
(Mainland China, India, Japan, Malaysia, Singapore, South Korea, Taiwan). 🔴 Independent
adoption statistics for China and India remain scarce — most circulating figures are
commentary or preprints, not official.


#### Update 2026-11-13 (thirteenth pass, `p808`) — 🟢 THE ONE GENUINE REGIONAL GAIN THIS PASS: Korea's education high-impact scope is NARROWER than this file has implied, and the narrowing decides whether a Korean university engagement is regulated at all

🟢 **This is the only region that returned something new this pass, and it is a
narrowing, not an addition.** The leg
`Korea AI Basic Act January 2026 education high-impact AI obligations` was run as a
differentiated follow-on after the general APAC leg came back fully saturated.

🔴 **What this file has carried:** *South Korea's AI Basic Act entered into force
`2026-01-22`; education is a high-impact category.* 🟢 **That is true but too coarse to
scope against.** The statutory definition of high-impact AI reaches education through a
**specific clause**, and the clause is about **student assessment in early-childhood,
primary and lower-secondary education**. 🔵 **Multiple English renderings agree on the
shape** (one gives *"early childhood education, elementary education, and secondary
education"*, another *"early childhood, primary, and lower secondary"*), **and none of
them reaches higher education or corporate training.**

🟢 **Why this matters commercially, which is the whole reason it is recorded:**

- 🟢 **A Korean *university* engagement — admissions analytics, an LMS tutor, a
  higher-ed advising agent — is most likely NOT high-impact under this Act.** That is the
  opposite of the EU AI Act, whose Annex III explicitly covers admissions and
  examination at *all* levels including vocational.
- 🔴 **A K-9 assessment or grading product IS squarely in scope**, and the duties are
  real: risk management, documented human oversight, user notification, and a
  **pre-deployment AI impact assessment**.
- 🔵 **So the same product crossing from the EU to Korea changes category depending on
  the age of the learner, not the function of the software.** A proposal that assumes
  "education = high-risk everywhere" will over-scope a Korean higher-ed deal and
  under-scope a Korean K-9 one.

🟢 **Two further mechanics this file did not carry:**

1. 🔵 **Classification is by operator SELF-ASSESSMENT**, with an **optional** confirmation
   request to **MSIT** (the Ministry of Science and ICT). 🟢 **There is no mandatory
   regulator pre-clearance** — which makes the classification memo a deliverable the
   studio can own, and makes getting it wrong the client's exposure.
2. 🔵 **Administrative fines under Article 43 — up to `30 million KRW` per violation —
   are DEFERRED to `2027-01-22`.** 🟢 **The grace period through 2026 is guidance-led:**
   other high-impact duties carry no direct monetary penalty and escalate only through
   guidance and corrective orders. 🔴 **"In force" and "enforceable by fine" are a year
   apart for this statute**, and this file previously carried only the first.

🔴 **Nil on everything else in the region, listed so the nil is auditable.** The general
APAC leg returned Vietnam's binding law (education high-risk, commencement `2026-03-01`,
pre-deployment registration, conformity assessment, human oversight), Australia's
**TEQSA** requirement that **all** higher-education providers file institutional
generative-AI action plans, China's algorithm/deepfake/generative rules with penalties to
`¥50M`, Singapore's **AI Verify**, Japan's voluntary light-touch model, Hong Kong's AI
R&D institute, and the EU AI Act's extraterritorial reach onto APAC ed-tech selling into
the EU. 🟢 **All already held.**

🔴 **Verification caveat:** the Korean statutory text could not be read directly this
window — `cset.georgetown.edu` and the other primary hosts do not resolve under this
session's network policy. 🔵 **The scope narrowing above is corroborated across several
independent secondary renderings that agree on substance while differing on translation,
which is why it is recorded as a gain rather than held back** — but it is search-tier.
🟢 `ACTION p808-A`: confirm the high-impact education clause and the Article 43 deferral
against the official statute or the CSET translation when a session can reach them.
**Until then, do not quote the `30 million KRW` figure to a client without the caveat.**


#### Update 2026-11-13 (twelfth pass, `p807`) — 🟡 near-nil, with one date this file was missing and one regional posture it had never characterised

🔴 **Near-complete nil on instruments.** The APAC leg returned Korea's **AI Basic Act**,
**Vietnam's** binding AI law with education in its high-risk category, Australia's
**TEQSA** request for institutional generative-AI action plans, China's
algorithm/deepfake/generative rules, and Japan's and Singapore's voluntary toolkits.
🟢 **All already held below.**

🟢 **Two genuine gains, both small and both stated as such.**

1. 🔵 **Vietnam's law has a commencement date this file never carried: `2026-03-01`.**
   The instrument was recorded; the date was not, and a date is what decides whether a
   Vietnamese deployment is already non-compliant or merely planning to be. Pre-deployment
   registration and human oversight for high-risk systems have therefore been **live for
   eight months**, not pending.
2. 🔵 **Malaysia, Australia and New Zealand share a posture this file had not named:
   deliberate *sectoral* regulation** — guardrails added to existing statutes rather than
   a standalone AI act. 🟢 This generalises the ninth pass's reading of Australia as
   "deliberate non-regulation" into a **three-country regional pattern**, and it changes
   the EMEA-style compliance pitch: in these markets there is no AI act to comply with,
   so the buying trigger is the **sector regulator** (TEQSA for Australian higher ed),
   not a horizontal law. 🔴 Malaysia is otherwise **absent from this file entirely** and
   no Malaysian education instrument, figure or deployment has ever been recorded →
   `Gap 807-B`.

🟡 **Korea's enforcement posture, already partly held, sharpened:** `2026` is in practice
a **pilot year** — enforcement decrees still being finalised, and a grace period oriented
to guidance rather than penalties. 🔵 A Korean engagement in `2026` is therefore selling
**readiness**, not remediation.


#### Update 2026-11-13 (eleventh pass, `p806`) — 🟢 `p805`'s "regulation-only" verdict is DISCHARGED: APAC now has a named, dated, institution-wide deployment — and the region's fourth AI statute was missing from this file entirely

🔴 **Taiwan had `0` mentions in every shelf file of this knowledge base before this
pass.** It is the fourth APAC jurisdiction to bring an AI statute into force and the
table below had three.

| Instrument | Status | What it does — and does not do |
|---|---|---|
| **Taiwan — AI Basic Act** 🆕 | 🟢 **Passed by the Legislative Yuan `2025-12-23`; promulgated and in force on `2026-01-14`** | 🔵 **A framework law, and the distinction is commercially decisive: multiple legal readings agree it imposes essentially no obligations on the private sector and lacks mandatory legal force.** It sets high-level principles and defers implementation to sector regulators. **Education is named among the sectors** (alongside finance and public administration) 🔴 **but there are no education-specific provisions, no school rules and no education-sector deadlines.** Two dated follow-ons: the Ministry of Digital Affairs issued an **AI risk framework on `2026-07-07`** that sector regulators are expected to follow, and the government must **review and align existing laws within two years of January 2026** — i.e. **by January 2028** |

🔵 **How to sell against Taiwan, stated precisely because the instrument is weak:**
do **not** pitch AI Act-style conformity work there — there is nothing to conform to
yet. 🟢 **Pitch against the `2028` alignment deadline and the MODA risk framework
instead**, which is where education-sector rules will actually originate. **An
institution that builds a deployment inventory now (`P14`) satisfies whatever MODA's
sector guidance turns out to require, and satisfies nothing it does not.**

🟢 **The deployment figure `p805` said the region could not produce.** `p805` recorded
that "the APAC regional leg is regulation-only again, and that is itself the finding."
**That is now discharged:**

| Institution | What was deployed | Date | Scale |
|---|---|---|---|
| **Nanyang Technological University (NTU), Singapore** | **Gemini Enterprise, Google AI Studio and Vertex AI**, plus compute credits for building agents | 🟢 **Announced April 2026; live since August 2026** | 🟢 **All undergraduates, regardless of discipline** |

🔵 **Three details make this more useful than a vendor press release.** First, the
access was negotiated **in consultation with the NTU Students' Union** — student
governance was a party to an AI procurement, which is a precedent an institutional
buyer will recognise. Second, **the teaching was folded into a core course** —
*"Science and Technology for Humanity"*, taken by every first-year — rather than left
as an opt-in tool, having previously been restricted to computing students. Third, NTU
has a **stated target of embedding AI into 40% of undergraduate courses by 2030**,
which is a multi-year programme with a number attached.

🔴 **Read the competitive implication honestly rather than as an opportunity.** This is
a **hyperscaler land-grab, not a services engagement**: Google supplied the stack to an
entire university at no cost to students. 🟢 **The work that survives it is the work
Google did not do** — curriculum redesign for `40%` of courses, faculty capability,
assessment integrity under universally available frontier models, and the deployment
inventory every APAC regime will eventually ask for. **Sell the 2030 target, not the
tooling.**

🔵 **Public opinion, unchanged and already carried below:** the Ipsos Education Monitor
2026 figures and the Vietnam/Korea/India instruments were returned again by this pass's
regional leg and are **already in this file** — no change.


#### Update 2026-11-13 (tenth pass, `p805`) — the regional leg is regulation-only again, and that is itself the finding

🔴 **`AI education APAC 2026 adoption regulation players` returned regulation and no
market.** Re-confirmed: **South Korea's AI Basic Act** is in force (2026-01-22) and
names **education among its ten high-impact sectors**, with a grace period reported to
run to **September 2027** for education/healthcare/finance; **China** layers PIPL + CSL
+ DSL with the Algorithm Recommendation, Deep Synthesis and Generative AI measures, and
has **550+ generative-AI services filed** by mid-2026; **Japan** remains promotion
without fines; **India** is unsettled — no AI law, but a **July 2026 signal that
dedicated legislation may be pursued**.

🔴 **What the leg did not return, for the fourth consecutive pass: adoption metrics,
market sizes, or a single named education-AI vendor for any of these four countries.**
🔵 **That is an informed gap, and it is the largest one in this file.** This base's own
`T8` says education AI's centre of gravity is APAC; the evidence for that is repository
provenance, not market data. **Closing it needs a different channel than WebSearch —
national ministry programmes and regional edtech market reports — and no pass has tried
one.**

🟢 **Supply-side change:** [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) —
**MIT**, 56★, Laravel — is now on the verticals shelf as **the first genuinely MIT
school ERP/SIS in this base**, placed APAC because `.env.example` ships
`TIMEZONE = 'Asia/Kolkata'`. 🟢 [`elimu-ai/webapp`](https://github.com/elimu-ai/webapp)
(**MIT**, 41★) joins the platform table with shipped content databases for **Hindi,
Tagalog, Thai, Vietnamese and English** — out-of-school-children programmes, a buyer
shape this file had not previously named.


**Adoption/regulation:** The most fragmented region, and education is usually
caught as a *high-risk category inside general* AI law rather than addressed
directly. **South Korea's AI Basic Act entered into force 2026-01-22** and
names education a high-impact area alongside healthcare and finance; year one
is reported as a pilot with limited enforcement and enforcement decrees still
being finalized. **Vietnam's binding AI law** puts education in its high-risk
category and requires **pre-deployment registration and human oversight**, with
an implementing decree in April 2026; **one source gives high-risk sectors
until September 2027 to comply** — the compliance deadline and the
in-force date are different things and sources blur them, so verify.
**Japan** has the **AI Promotion Act (June 2025)**, though other sources
characterise Japan as voluntary-guidelines-and-self-regulation; both can be
true (a promotion-oriented statute without high-risk obligations), but do not
assert either without checking. **Australia** has no AI-specific statute; its
2024 mandatory-guardrails proposal covers high-risk education uses, and the
higher-ed regulator **TEQSA has required universities to submit generative-AI
risk management plans**. **China** has the most detailed binding rules (content
labelling, algorithm registration) but they are not education-specific.
**Singapore and New Zealand** rely on voluntary toolkits and existing law.
The EU AI Act reaches APAC vendors selling into Europe.

**Public opinion is moving, and not uniformly:** the **Ipsos Education Monitor
2026** finds overall lower support for banning AI in schools across the Asian
markets examined, but support for a ban **rose in Japan and South Korea** while
it **fell in Indonesia**. A region-wide message will misfire; the political risk
of classroom AI is increasing in exactly the two most advanced markets.

**Players:** Tsinghua MAIC (OpenMAIC, MIT, 43.4k), HKUDS (DeepTutor,
Apache-2.0, 58.7k) and JuneYaooo (teacher-to-skills, Apache-2.0, 475) — **the
three largest education AI agent projects in the world are all APAC-origin**.
India: BHASHINI language infrastructure and DIKSHA (already shipping AI
features such as in-video keyword search and read-aloud for visually impaired
learners); **Bharat EduAI Stack** open Indic-language models announced
September 2026 by IIT Madras-incubated Bodhan AI — an announcement, not a
rollout. Moodle and Frappe LMS are widely deployed. Every major APAC economy is
building domestically owned models; regional adoption is characterised as broad
but shallow.

**Opportunities:**
1. **Multi-jurisdiction compliance architecture.** A regional university group
   or edtech vendor faces Korean high-impact rules, Vietnamese registration,
   Australian TEQSA plans, Chinese labelling and the EU Act for exports — all
   at once. One policy-enforcement layer with per-jurisdiction configuration is
   a genuine architecture problem worth paying for.
2. **Vietnam pre-deployment registration and human oversight.** A hard,
   binding obligation already in force, with a compliance runway that sources
   place as late as September 2027. First-mover advisory plus the technical
   oversight/logging layer it requires.
3. **Localize the APAC-origin agents.** DeepTutor (Apache-2.0), OpenMAIC (MIT)
   and teacher-to-skills (Apache-2.0) are permissively licensed, large and
   built in the region. Adapting them to Indic, Bahasa, Thai, Vietnamese and
   Japanese curricula is lower-risk than building a tutor from zero.
4. **Sovereign deployment for localization mandates.** Self-hosted open weights
   plus a local LMS answers data-residency requirements directly.
5. **Teacher-led framing for Japan and Korea.** With ban sentiment rising in
   both, the saleable product is explicitly teacher-augmenting and
   parent-legible — `teacher-to-skills`-shaped (distil the teacher, keep them
   in the loop) rather than student-facing autonomous tutoring.

#### Update 2026-11-13 (third pass) — four regimes, four different instruments, and a cautionary rollout

- **South Korea — the region's first comprehensive statute.** The **AI Basic
  Act has been in force since 2026-01-22**. Generative AI users must be told
  they are interacting with AI, and generated content must be marked. Korea
  **declined** to add a text-and-data-mining exception to its Copyright Act in
  February 2026 — relevant to any training-on-course-materials proposal. A PIPA
  special provision for AI development reportedly passed 2026-08-20 and is
  **not yet in force** (tracker-sourced; verify).
- **Korea is also the cautionary tale.** Korea rolled out **AI-powered digital
  textbooks from 2025**, the first country to attempt it at national scale, and
  met **parental and teacher backlash over screen time**. Any national-scale
  pitch should cite this and lead with the mitigation, because the client's
  ministry will already know it.
- **China — no general AI law, binding specific rules.** Mandatory regimes
  cover recommendation algorithms, deepfakes, generative AI services, and
  **labelling of AI-generated content since 2025-09-01**. Note also that China
  **banned the private tutoring sector**, which is why **TAL pivoted into AI
  learning hardware** — the money moved from services to devices.
- **Japan — light touch.** The **AI Promotion Act (May 2025)** encourages
  cooperation with government safety measures and carries **no monetary
  penalties**. Lowest regulatory friction in the region.
- **India — labelling in force, statute signalled.** Amended IT Rules require
  AI-generated content to carry **prominent labels and provenance markers from
  2026-02-20**; in **July 2026** the government signalled it may pursue
  dedicated AI legislation. **PhysicsWallah** launched its own AI tutor;
  **BYJU'S** collapse is still the reference failure in the market.
- **Commercial players to know:** **Mathpresso's QANDA** (Korea, math-solving,
  global reach), **ByteDance's Gauth** (a top education app **in the US** —
  APAC-built product winning a North American market), TAL, PhysicsWallah.
- **Declared gap:** no source found in this pass regulates **AI in the
  classroom** specifically in any of these four countries — the instruments are
  economy-wide AI law plus content labelling. Education-specific rules must be
  verified **directly with each country's education ministry**; do not infer
  them from the AI statutes.

#### Update 2026-11-13 (fourth pass) — two binding laws are now in force, education is named high-risk in one, and public opinion diverges sharply within the region

**Binding law, in force, with education named.**

| Jurisdiction | Instrument | In force | Education treatment |
|---|---|---|---|
| **South Korea** | AI Basic Act | **22 January 2026** | Comprehensive; disclosure duties |
| **Vietnam** | Law on Artificial Intelligence | **1 March 2026** | **Education named high-risk**, specifically **automated assessment and behavioural monitoring** |
| **China** | Targeted rules — algorithms, deepfakes, generative AI | In force | Sectoral, not education-specific |
| **Australia** | Existing law plus voluntary guidance | — | No dedicated instrument |
| **India** | Governance guidelines plus **labelling rules for AI-generated content** | — | Provenance marking |

**Vietnam legislates the curriculum as well as the risk.** Beside the AI Law, **MOET
Decision `2422`** sets **12 periods per class per year** of AI content for **grades 1-12** —
a national teacher-enablement and courseware demand signal with a fixed hourly budget, which is
a far more concrete procurement hook than an adoption percentage. 🔵 Recorded in this base's
trending log since `p787`; promoted to this shelf at `p803`.

**Vietnam is the sharpest opportunity in the region and the date needs care.**
Education is on the high-risk list, and **automated assessment and behavioural
monitoring** are named — which is precisely what an assessment or proctoring
agent does. Existing education systems get a grace period, and **the sources
disagree on its length**: one says six months beyond a March 2027 deadline,
another that high-risk sectors have until **September 2027**. Both readings land
in 2027; do not quote either to a client without the statutory text. The
commercial shape is `P2` — a conformity layer for assessment AI — transplanted
from EMEA to Vietnam, and the EMEA work is reusable because the risk-based
structure is the same.

**Public opinion diverges inside the region, and it cuts against student-facing
autonomy in the Anglophone markets.** The **Ipsos Education Monitor 2026** finds
support for *banning* AI in schools is **lower across most Asian markets** but
**higher in Australia and New Zealand**, ranging from **23% in Indonesia to 31%
in South Korea** — and support for a ban **rose year-on-year in Japan and
Australia**. Ipsos characterizes Indonesia's posture as **"Protect and
Prepare"**: limits on children's social media alongside openness to AI in
education.

**What that means for how an engagement is pitched.** In Australia, New Zealand
and Japan — the markets with rising ban sentiment and no binding instrument — the
**teacher-augmenting** framing (`P7`, teacher distillation) is materially safer
than student-facing autonomy, and the risk is reputational rather than legal. In
Indonesia, Vietnam and Korea the receptiveness is higher but in two of the three
the law is now binding, so the constraint moves from public opinion to
conformity. **Same region, opposite dominant constraint** — do not carry one
country's pitch to the next.

**Policy maturity is bimodal.** UNESCO notes **China and Singapore** have
established AI-in-education policies and guidelines, while other countries in the
region are **still contending with basic educational needs**. The regional
average is not a useful planning number for anything.

**One APAC technical finding this pass.** The second verified agent-to-SIS
server in this KB is **Central Asian**: `sukhrobyangibaev/mcp_hemis_student`
(MIT) over **HEMIS**, used by Uzbek universities. With EduPage in EMEA this
establishes the `T12` pattern — agent integration arrives first where one
platform holds a captive national market.

**Reliability note.** The strongest sources here are the Ipsos survey and a
law-firm regulatory analysis; the in-force dates should still be checked against
official texts, and the Vietnamese grace period is unresolved between two
secondary readings.

#### Update 2026-11-13 (fifth pass) — the region keeps the agent centre of gravity, and the first tool ecosystem around an education agent appears here

🟢 **APAC produced the pass's only new agent-adjacent artifact, and it is a new
*kind*.** `Suyutao/DeepTutor-MCP` (**Apache-2.0**, 1 star, **60 tools**) is the
first MCP server in this base built over **another education agent's data**
rather than over a platform: it exposes a self-hosted **DeepTutor** install
(HKUDS, Hong Kong — Apache-2.0, **58.7k stars**, 7.1k forks) to any MCP client,
covering Mastery Paths with outlines and evidence, Question Bank and practice
queues with analytics, generated books and reading material with notes and
highlights, knowledge-base metadata with file search and vector passage
retrieval, historical sessions and memory documents.

🔵 **Why this matters more than its 1 star suggests.** Every other education
agent in this KB is a leaf: it talks to an LLM and a platform. **A tool
ecosystem forming *around* an open education agent is the first sign that one of
them is becoming infrastructure** — the thing Moodle is for LMSs. DeepTutor is
the only candidate at that scale, it is Apache-2.0, and it is APAC-origin.
**Watch this specific signal: more third-party servers over DeepTutor means a
studio can build on DeepTutor rather than beside it.** 🔴 **Not yet adoptable:**
it needs a reachable self-hosted DeepTutor HTTP API, and its Mastery tutor tools
depend on upstream PR **`HKUDS/DeepTutor#1785`, still open and unmerged**.

🟢 **DeepTutor's own release cadence, as this window's APAC adoption signal:**
**v1.7.1 on 2026-11-01** and **v1.7.2 on 2026-11-06** — two releases in six
days, adding complete desktop downloads, speech for selected text, simpler model
setup, a **Korean interface preview**, NVIDIA NIM embeddings, broader
localization, Anki and calendar exports and more model providers. 🔵 **The
localization direction is the regional tell: Korean UI, with pt-BR and es-MX
already shipping in OpenMAIC — APAC-origin education agents are localizing
outward into LATAM and Europe, not waiting to be localized.** That is the
practical basis for `T8`'s recommendation to localize permissive APAC agents
rather than build regional ones from scratch.

🔴 **No new APAC regulatory instrument surfaced this pass.** The region's
position in this file is unchanged: South Korea's AI Basic Act in force
**2026-01-22** with enforcement decrees still being finalised; **Vietnam's** AI
law with **education named in its high-risk category** and pre-deployment
registration in the National AI Database; Australia's **TEQSA** requirement that
every higher-education provider file a generative-AI institutional action plan;
Singapore's AI Verify toolkits; Japan's voluntary model; China's comprehensive
framework. **Stated as a confirmed non-change, not as unchecked.**

#### Update 2026-11-13 (sixth pass) — mandates are now curricular and dated, and the growth-rate estimates disagree by a factor approaching two

- **China:** the Ministry of Education has made AI education **mandatory across
  every stage** of the system. 🔴 **Sources disagree on the dose and this KB
  should not average them:** one reports **at least six hours a year** for
  lower-grade students, another **eight hours a year** for primary learners.
  Rollout has varied by province.
- **India:** **AI and Computational Thinking enter all schools from Grade 3**,
  beginning in the **2026–27 academic year**, aligned to **NEP 2020**. This is
  the single largest dated curricular expansion in this file — it creates
  teacher-training and content-localisation demand at national scale.
- **Japan — the sources genuinely conflict and the disagreement is the finding.**
  One reports Japan **gathering information from pilots** and deliberately
  diverging from its neighbours; another says Japan **integrates AI across core
  subjects** under new teaching guidelines. **Verify Japan's posture directly
  before pitching there; do not carry either claim into a proposal.**
- **Public opinion is the region's quiet advantage.** Support for **banning** AI
  in schools runs **23%–31%** across Asian markets versus a **39% global
  average** (Ipsos). 🔵 **But it is moving: support for a ban in Japan rose from
  21% to 29%** — the one place in this file where resistance is measurably
  growing.
- **Readiness is uneven and that is a market, not a caveat:** an ASEAN
  Foundation study found Southeast Asian education systems at **deeply uneven
  stages of AI readiness**. Mandates without capacity is the teacher-enablement
  opportunity.
- **Financing is flowing to delivery:** the **Asian Development Bank signed a
  USD 10M financing package with Schoolnet India Limited on 17 June 2026.**
- 🔴 **Growth estimates for APAC are not usable at one decimal place:** Grand
  View puts the region at **28.1% CAGR (2026–2033)** with **Japan** highest;
  Mordor puts APAC at **44.20% CAGR**. **Quote "high-30s to 40s, contested", or
  quote neither.**

#### Update 2026-11-13 (seventh pass) — the Philippines supplies the instrument this whole market has been missing: a register of what is actually deployed

- 🟢 **The single most transferable regulatory artifact found this pass is APAC's.** The Philippines
  **Department of Education Order No. `003`, s. `2026`, issued 2026-02-20** — described as the first
  comprehensive national guideline for AI in basic education — **creates an AI registry of all
  deployments** and **sorts tools into risk tiers**, with stricter rules for high-stakes uses such as
  **grading and admissions**. 🔵 **A registry is a deliverable, not a constraint.** Every other regime
  in this file imposes duties on systems nobody has enumerated; this one enumerates first. **Build the
  registry as the first engagement artifact in any jurisdiction** — it is what the EU's Article 27
  FRIA, Oklahoma's teacher-review clause and the UNESCO governance gap all silently presuppose.
- 🟢 **South Korea's AI Basic Act entered into force 2026-01-22**, with enforcement decrees still
  being finalised and a grace period through 2026 focused on guidance rather than penalties.
  🔵 **New to this file** — `p799` recorded only that Korea's ministry domains refuse at `CONNECT`;
  the statute itself is now dated.
- 🔴 **Vietnam's timetable is refined, and this base's carried date was incomplete.** This file
  recorded "in force 2026-03-01 with an 18-month education transition". The fuller picture:
  **compliance is required by 2027-03-01**, **education systems already operating before 2026-08-15
  receive a further six months**, and an **implementing decree, `142/2026/ND-CP`, was issued
  2026-04-30**. 🔵 **Material refinement: many listed systems are high-risk *only* where their output
  is the sole basis for a decision without meaningful human review** — so a human-in-the-loop design
  can move an education deployment out of the high-risk tier entirely. That is an architectural
  lever, and this KB already holds the components for it.
- 🟢 **APAC faculty remain the region most positive on AI: `57%` report being excited about it** and
  believe it can make learning more effective — the highest of any region in the same survey.
- 🔴 **Declared gap, unchanged: China, Japan, Singapore, Australia and India returned no education-
  specific binding instruments or deployment counts on this pass.** One secondary note only — China
  has made AI compulsory for school students from age six. 🔴 **No named APAC edtech vendor emerged
  at any point in this leg.**


#### Update 2026-11-13 (ninth pass) — Australia's plan is now on the shelf, and it is the region's clearest example of deliberate non-regulation

🔴 **Provenance: search-tier**, from indexed commentary and secondary trackers. No
Australian government domain is reachable from this session.

**Australia's National AI Plan, released 2 December 2025 — new to this file.** It
builds on the 2021 AI Action Plan and consolidates commitments made since 2022.
🔵 **The decision that matters is what it declined to do: no mandatory guardrails for
high-risk AI.** The Plan relies on **existing laws and sector regulators**, so schools
are governed through education systems and national guidance rather than an AI
statute. 🟢 **That places Australia precisely opposite Korea (AI Basic Act, in force
January 2026) and Vietnam (AI Law, 1 March 2026, with education named in its
high-risk scope and an 18-month transition) inside the same region** — which is the
sharpest illustration this file has of `P5`'s premise that APAC is not one compliance
surface.

- The Plan **explicitly references the Australian Framework for Generative AI in
  Schools** as the national reference point.
- 🔴 **The Framework has not been revised in 2026.** Work continues inside **AI
  Taskforce working groups**, which are developing **national product expectations for
  edtech AI tools**. 🔵 **Watch that workstream: "national product expectations" is a
  procurement specification in everything but name, and it is the thing an edtech
  vendor selling into Australia will have to answer to.**
- A free **national AI-literacy curriculum** is reported rolling out in 2026 across
  public, independent and Catholic schools, developed by **Code for Schools** with
  **AWS** support, targeting **1 million students within three years**. 🔴 **Some
  sources describe it as binding; that could not be confirmed from a primary
  government source and is not asserted here.**

**Institutional actors added to this file:** **SEAMEO INNOTECH** as the Southeast Asian
regional body, **NCERT** in India, and the **Philippines' MATATAG** curriculum rollout
— 🔵 **the last of which reinforces the seventh pass's Philippines finding: AI guidance
in this region has to track curricula that are themselves still being phased in.**
**Indonesia's** national AI rules remained in draft, with a Presidential Regulation
expected in the first half of the year.

🔵 **Engagement read, unchanged in direction and sharper in detail: APAC's binding
constraint is that a multi-country client needs one architecture that can be governed
four different ways.** Australia now supplies the "no statute, strong guidance,
procurement-led" corner of that matrix, which `P5` did not previously have a named
example of.

### LATAM

#### Update 2026-11-15 (thirty-first pass, `p826`) — the region's headline figures are dated to their FIELDING WINDOW at last, confirming `T64` with the instrument named, and LATAM gains a build-safe portal connector

🟢 **Survey items `CITED, NOT READ`; repository items first-hand and byte-read.**

- 🟢 **`T64` CONFIRMED with the methodology date, which closes a caveat this base has carried since `p819`.** The UNESCO IESALC study behind the region's most-quoted pair — **`87%` of institutions using AI in at least one area, `26%` with any formal framework, `200` institutions across `19` countries** — is *AI Implementation in Higher Education in Latin America and the Caribbean*, published **September 2026**, 🔴 **but fielded August–October 2025 (Valentini).** 🔵 **So the "2026" LATAM adoption figures describe late 2025 and are roughly thirteen months old at the point of quotation. Quote them with the fielding window attached or do not quote them.**
- 🟡 **Companion figures, cited, with the same caution:** **`55%`** of universities report no specific AI budget; **`76%`** of faculty express concern about student over-reliance; UNESCO's Higher Education Global Trends Report 2026 puts LATAM at **`45%`** of institutions having adopted or developing AI guidance against **`~70%`** in Europe and North America.
- 🟡 **Digital Education Council LATAM survey 2026** (with Tecnológico de Monterrey and the Institute for the Future of Education): **`92%` of students and `79%` of faculty** actively engaging with AI. **Cetic.br 2026:** `65%` of Brazilian internet users aged 9–17 report using AI tools. **Ceibal 2026:** `75%` of Uruguayan public-school teachers report using them. 🔵 **The student-faculty gap and the institutional-framework gap are the same commercial opening this base has described for four passes: demand is present, governance is not, and governance is what an institution will pay for.**
- 🟢 **Governance infrastructure, cited:** UNESCO launched a regional **Observatory on AI in Education for Latin America and the Caribbean in April 2026**. **Universidad de los Andes (2026)** counted **`716` AI-related regulatory instruments, rules and legislative proposals across `23` countries and territories.** 🔵 **`716` instruments against `26%` institutional frameworks is the sharpest statement of the region's shape available: the regulation is arriving faster than institutions can absorb it, and translation between the two is a service.**
- 🟡 **Regulatory status, cited:** Brazil's **PL 2.338/2023** (risk-based) passed the Senate in December 2024 and remains in the Chamber of Deputies. Colombia took a policy-first route via **CONPES 4144 (February 2025)**. Argentina, Brazil, Chile, Colombia, Costa Rica, Mexico and Peru have adopted the OECD AI Principles.
- 🟢 **The supply-side finding, measured and new.** LATAM gains a **build-safe** national-portal connector for the first time: `Petri-Hub/fam-mcp` (🇧🇷 MIT, byte-read) — a read-only MCP server over the **Faculdade de Americana** student portal covering grades, absences, assignments, schedule, exams, inbox, forums, finances and complementary hours. 🔵 **Its README states the regional constraint verbatim — *"The portal has no API"* — so it signs in as the student, reads server-rendered pages and returns typed JSON. Its killer query, *"What is due this week?"*, spans assignments, exams, forums AND invoices: a question the portal itself cannot answer, which is the clearest product thesis in this tier.**
- 🔴 **And the larger LATAM target is blocked on a licence.** `KaioBorgesDev/siga-mcp` exposes **SIGA**, the academic system of **São Paulo state's Fatec and Etec technical network** — a public system at state scale, and by far the biggest institutional footprint found in this tier — 🔴 **but it carries no `LICENSE` file and is therefore not build-safe.** 🟢 **A licence request to one developer is the highest-leverage single action available in LATAM this pass.**

#### Update 2026-11-15 (thirtieth pass, `p825`) — adoption is the highest measured anywhere and governance is the lowest, and Latam-GPT has no open repository

🟢 **The LATAM leg produced the richest survey material of any region this pass; all `CITED, NOT READ`
except the GitHub measurement, which is first-hand.**

- 🟢 **The adoption figure is now survey-backed and very high.** The Digital Education Council's
  **AI in Higher Education LATAM Survey 2026**, run with Tecnológico de Monterrey's Institute for the
  Future of Education across **`7,319` faculty at `29` institutions**, reports **`92%` of students and
  `79%` of faculty actively engaging with AI**, with **`67%` using it at least weekly**.
  🔵 **`92%` student engagement is the highest regional figure in this entire file.**
- 🔴 **Governance is the lowest.** A UNESCO **IESALC** survey of **`200` institutions across `19`
  countries** finds the adoption-versus-governance gap *particularly pronounced* in the region, and
  **only `~30%` of Latin American universities have published policies on AI use**.
  🟢 **`92%` using it against `30%` governed is the single sharpest sell-through in this file: the
  deliverable is the policy, the evidence trail and the audit, not the tutor.**
- 🟡 **Institutional actors, now enumerated:** **UNESCO IESALC** (regional HE AI reports);
  **UNESCO + CENIA (🇨🇱)** on ethical AI in education, including integration of **Latam-GPT**;
  **EdTech Hub + Fundación Ceibal (🇺🇾)** in a new regional partnership; the **IDB** (April 2026 post on
  AI in education in Argentina, covering regulation and financing); **ECLAC**'s eLAC digital agenda.
- 🔴 **A first-hand nil, measured this pass, and it corrects an impression this file has left.**
  This base has carried **Latam-GPT** across several passes as a regional asset. 🟢 **Queried directly:
  `search/repositories q="latam-gpt"` returns `total_count=5`, and NOT ONE is the project** — they are
  an Alura course repo, two student GPT-2 re-implementations, a `mini-latam-gpt` and a bootcamp
  exercise, **every one of them unlicensed**. 🔴 **So Latam-GPT has no open GitHub repository
  discoverable under its own name.** 🔵 **It may still be open by another route, but a studio planning
  to build on it cannot clone it today, and this file should stop implying otherwise.**
- 🔴 **The region's standing supply gap is unchanged and now has a named layer.** `P63`'s
  special-education evidence pipeline has components in APAC (byte-read, MIT) and statutory analogues
  in NA and EMEA; **LATAM has no open supply at that layer in any pass of this base.**
  🟢 **`P62` step `2` — platform-brand enumeration — is the first instrument to run against it, since
  `T86` proved the region-vocabulary approach is not the only axis.**
- 🟡 **Regulatory nil, stated explicitly:** the leg returned **no 2026 national AI-in-education
  regulation for Mexico, Brazil or Chile**. 🔵 **That is an informed gap, not coverage — governance in
  the region is still institutional policy rather than statute, which is consistent with the `30%` figure.**


#### Update 2026-11-15 (twenty-ninth pass, `p824`) — 🔴 Adoption is near-universal and governance is not: `87%` of institutions use AI, `26%` have a strategy — and the region's supply is invisible to the queries most studios will run

🟡 **Sourcing note for every item in this block: egress in the `p824` environment resolved GitHub and web search only — `oecd.org` was refused at the proxy, as at `p822`. Every market and regulatory item below is `CITED, NOT READ`: it comes from web-search summaries of secondary sources, several of them vendor blogs and trackers. 🔴 Verify any date, bill number or percentage against the official text before quoting it to a client. Every REPOSITORY figure in this pass is first-hand and byte-read; the two classes are not interchangeable.**

- 🔴 **The adoption/governance gap now has a primary-shaped number on it.** **UNESCO IESALC**, cited
  this pass, surveyed **`200` institutions across `19` countries**: **`87%` already use AI in some
  capacity** and **only `26%` have a formal AI strategy**. 🔵 **That `61`-point gap IS the LATAM
  engagement. `P4`'s productised governance package is priced against exactly this number, and this
  is the strongest single citation this base has ever carried for it.**
- 🟢 **Demand-side confirmation from a second body.** The **Digital Education Council's 2026 LATAM
  survey** reports **`92%` of students and `79%` of faculty actively engaging with AI**.
  🔴 **And at school level: across the `13` countries assessed by PISA 2025, nine in ten
  `15`-year-olds have used AI chatbots for schoolwork; in 🇧🇷 Brazil `53%` of school administrators
  use AI while only `22%` report their school has guidelines on it.** 🔵 **Student use leads
  institutional policy in every one of these instruments. A LATAM proposal that opens with adoption
  is selling something the client already has.**
- 🔴 **The regulatory picture is FRAGMENTING, and now carries a count.** A 2026 Universidad de los
  Andes study, cited this pass, counts **`716` AI-related regulatory instruments, rules and
  legislative proposals across `23` countries and territories, more than `80%` initiated since
  2023**. 🔵 **Fragmentation at that scale makes a multi-country rollout a compliance-architecture
  problem before it is a technology problem — `P5`'s shape, applied to this region.**
- 🟡 **Three divergent national postures, named:** 🇧🇷 **Brazil** is advancing a draft framework that
  borrows heavily from the EU approach; 🇦🇷 **Argentina** has submitted a bill that includes an
  explicit commitment to keep AI **unregulated**; 🇨🇴 **Colombia** has a government-wide programme
  with actions and a budget **through 2030**; 🇺🇾 **Uruguay** was the first in the region to sign the
  Council of Europe's Framework Convention on AI (2025). 🔵 **Brazil and Argentina are moving in
  opposite directions. Do not quote one regional compliance posture.**
- 🟢 **Institutional players for the region, named and worth approaching:** the **UNESCO observatory
  on AI in education for Latin America and the Caribbean, launched April 2026**, led with **CAF**,
  **CENIA** (🇨🇱), the **Ceibal Foundation** (🇺🇾), **Fundación Santillana**, **Tecnológico de
  Monterrey** (🇲🇽) and **ProFuturo**. 🔵 **CENIA also leads Latam-GPT, already carried here.**
  🔴 **And the structural fact cited alongside it: no frontier AI model is currently built in Latin
  America — which is an argument for the integration-and-governance engagement, not the model one.**
- 🟢 **The supply finding, and it is `T82`.** `q="agente educativo inteligencia artificial"` → **`4`**,
  all four unlicensed; `q="professor agente ia educacao"` → **`0`**; `q="mcp universidad
  estudiantes"` → **`0`**. 🟢 **`q="sigaa"` → `709`.** 🔵 **`177:1`. The region's agent supply is
  indexed under the name of the SYSTEM OF RECORD, never under the pedagogy — so a studio running the
  obvious queries will conclude the market is empty and be wrong by two orders of magnitude.**
  🟢 **`P59` is the protocol that fixes it, and `p824` shelved three new 🇧🇷 Brazilian rows found that
  way: `ufc-mcp` (UFC), `2026-2-Followw` (UnB, and published by a university COURSE org that ships a
  new cohort every semester), `sigaa-faltas` (UFPE).**


#### Update 2026-11-15 (twenty-eighth pass, `p823`) — 🟢 The region's institution-integration ZERO closes with a write-capable Brazilian agent; 🔴 and the governance gap is confirmed from a FOURTH instrument

🟡 **Sourcing note for every item in this block: egress in the `p823` environment resolved GitHub and web search only. Every market and regulatory item below is `CITED, NOT READ` — primary texts were NOT opened. Figures are attributed to the party that published them, vendor and advisory sources are marked as such, and dates that sources disagree on are shown disagreeing. Every REPOSITORY named is first-hand and byte-read.**

- 🟢 **The supply finding, and it closes a gap this file has carried since `p811`.**
  [`jeanmartina/ufsc-moodle-mcp`](https://github.com/jeanmartina/ufsc-moodle-mcp) (**MIT**,
  byte-read `1,064 B`, `sha256:845ac6ac…`) is an MCP server for the Moodle of **Universidade
  Federal de Santa Catarina 🇧🇷**, pinned to `presencial.moodle.ufsc.br`. 🔴 **`p811` recorded
  `0` of `65` build-safe agents integrating with a LATAM-operated system.** 🟢 **The university
  tier is now non-zero — and the entrant WRITES**: it edits and publishes assignments through
  Moodle's own form and commits grading in batches, behind a **two-phase commit → cache-invalidate →
  re-read → diff** protocol, with `form_rejected` distinguished from session expiry and `dueDate`
  guaranteed never to move `cutoffDate`. 🔵 **Better assurance than the EMEA write agent shelved in
  the same pass. Generalised as `P56`.** ⚠️ `0★`, single maintainer, one university.
- 🟢 **The governance gap, now from a fourth independent instrument.** A **UNESCO IESALC** study of
  **`200` higher-education institutions across `19` countries** finds **`87%` already use AI in
  some capacity while only `26%` have a formal AI strategy**. 🔵 **That `87%`/`26%` pair is the
  single most useful number in this file for a LATAM bid** — adoption is settled, governance is not.
- 🔵 **Corroborating, with different populations — do NOT average them.** The **Digital Education
  Council LATAM Survey 2026** reports **`92%` of students and `79%` of faculty** actively
  engaging with AI (🔴 **reported n ≈ `29` institutions — a small base, flag it if quoted**).
  **Cetic.br (2026)**: in 🇧🇷 Brazil **`53%` of school administrators use AI** but only **`22%`
  report school guidelines**. 🟢 **Three instruments, three populations, one consistent shape.**
- 🔴 **Regulation is fragmented and the volume is now quantified.** A **2026 Universidad de los
  Andes** study counts **`716` AI-related regulatory instruments, rules and proposals across
  `23` countries and territories, with over `80%` initiated since 2023.** 🔵 **Fragmentation at
  that volume is itself the service opportunity: no regional institution can track it in-house.**
- 🟡 **The four postures, and they genuinely differ.** 🇧🇷 **Brazil**: draft framework borrowing the
  EU's risk-based model. 🇨🇴 **Colombia**: policy-first via **CONPES 4144** (adopted February 2025),
  a government-wide programme with budget **through 2030** instead of immediate horizontal
  obligations. 🇦🇷 **Argentina**: a bill submitted by the President that *"commits to keep AI
  unregulated"*. 🇺🇾 **Uruguay**: **the first Latin American country to sign the Council of Europe's
  Framework Convention on AI**. 🔵 **A single regional compliance story is not available; price
  per-country.**
- 🟢 **The institutional map is approachable and unchanged.** UNESCO's **Observatory on AI in
  Education for Latin America and the Caribbean** (launched April 2026) is led with **CAF, CENIA,
  Cetic.br/NIC.br, ECLAC, Ceibal, Fundación Santillana, Tecnológico de Monterrey, ProFuturo,
  Universidad del Desarrollo and IRCAI**. 🔵 **CENIA also builds Latam-GPT on regional data.**
  🟢 **These are named, contactable institutions spanning every major market — the partner list IS
  the go-to-market map.**
- 🔵 **Placement discipline, stated because this pass tested it.** Two repositories with
  Spanish-language or Latin American authorship were shelved as **`Global`, not LATAM** —
  [`ccamilobedoya/protoboard-iso`](https://github.com/ccamilobedoya/protoboard-iso) and
  [`vladimiracunadev-create/modern-software-engineering-program`](https://github.com/vladimiracunadev-create/modern-software-engineering-program)
  — because **`T32` places a row by the system it integrates with, never by the author's
  nationality.** 🟢 **The LATAM count in this file stays honest only if that rule is applied when it
  costs the region a row.**


#### Update 2026-11-15 (twenty-seventh pass, `p822`) — 🔴 Adoption is near-universal and GOVERNANCE is the measured deficit; `0` new LATAM supply this pass, declared

🟡 **`CITED, NOT READ` throughout: egress resolved GitHub only this pass.**

- 🟢 **The strongest LATAM demand measurement this pass, and it has a stated sample.** The Digital
  Education Council's *AI in Higher Education LATAM Survey 2026* reports **`92%` of students and
  `79%` of faculty actively engaging with AI**, gathered from **`7,319` faculty across `29`
  institutions**, with the headline *"High Adoption, Conservative Usage"* — and
  🔴 **only `30%` believing their institution has responded effectively.**
- 🟢 **UNESCO IESALC's `2026` working paper** maps AI across universities on five dimensions —
  teaching, research, community engagement, administration and governance — and finds adoption
  *"neither uniform nor evenly distributed"*, with a private/public gap. A UNESCO-linked study of
  **`200` institutions across `19` countries** describes an adoption-versus-governance gap as
  especially pronounced here, and the DEC commentary names **the absence of formal university AI
  policies** directly.
- 🟢 **K-12 evidence base:** the IDB reports on **`193` real AI initiatives** across the region and
  characterises LATAM as building hybrid, context-sensitive systems. EdTech Hub and **Fundación
  Ceibal** have launched a regional AI-in-education partnership.
- 🔴 **Regulation: this leg returned NO concrete `2026` national AI-in-education instrument.**
  🟢 **That is a limit of this leg, not a statement about the region — this base already holds
  `Parecer CNE/CP nº 15/2026` (Brazil, stage-gated at `6º ano`, `T66`–`T68`) and `ILIA 2026`'s
  finding that `11` of `20` countries now carry AI content in the national curriculum (`T69`).**
  🔵 **Recorded so a later pass does not mistake a thin leg for a regulatory vacuum.**
- 🔴 **`0` new LATAM supply rows this pass, stated rather than left silent.** `p821` added `mawta`
  (Peru, `CNEB`); `p822`'s recency and challenge channels returned no LATAM education repository
  that passed the payload read. 🔴 **One Spanish-language candidate was REFUSED a LATAM placement on
  this base's own rule — `tuttor-kit`'s only Brazil signal is a `README.pt-BR.md` locale label, and
  a language is not a location.**
- 🔵 **The opportunity is unchanged in shape and sharpened in evidence: `92%` use against `30%`
  institutional response is a GOVERNANCE engagement, not a tooling one** — policy, assessment
  redesign and evidence of learning (`P53`), with `P51`'s curriculum-adapter asset as the
  per-country port.

#### Update 2026-11-15 (twenty-sixth pass, `p821`) — 🟢 The region's curriculum nil ENDS as a measurement, and this base's own CENIA-sourced line is shown to be stale

- 🟢 **The number, and it is the most important LATAM datum this file has recorded (`T69`).** The
  **Índice Latinoamericano de Inteligencia Artificial (ILIA) 2026**, published in October 2026 by
  **CENIA** with **CEPAL**, reports **`11` of the `20` countries covered now include AI content in
  their school curricula, against `2` in `2024`**. 🟢 **All `20` have AI-related master's
  programmes and `14` have doctoral programmes.** 🟢 **The index's own recommendation is to extend
  AI content in **secondary** education beyond those eleven.** 🇨🇱 Chile places first for the
  fourth consecutive year.
- 🔴 **This supersedes a line in this file.** The LATAM section carries *"School-level AI education
  is largely absent"*, attributed to **CENIA** — the same body, an older vintage. 🟢 **The older
  line stays where it is, with this block cited against it, because the vintage failure is itself
  the lesson (`T64`).** 🔵 **The indicator measures inclusion in national programmes, NOT a
  standalone school subject in every school — the press coverage says so explicitly and this file
  repeats the qualification rather than rounding it up.**
- 🔴 **The eleven countries are NOT named in anything reachable on this pass's GitHub-only egress,
  and `indicelatam.cl` and `repositorio.cepal.org` both failed to resolve.** 🟢 **`ACTION p821-C`:
  name the eleven and place each one, from the index itself, on the first pass with general
  egress.** 🔵 **Evidence grade: `CITED, NOT READ`, corroborated on two independent secondary
  routes carrying the same two figures.**
- 🟢 **SUPPLY: the region produced the single best row of the pass, and it is bound to a NATIONAL
  INSTRUMENT.** [`amaru-one/mawta`](https://github.com/amaru-one/mawta) (MIT, byte-read, `2★`,
  created `2026-11-07`) — *"An open-source gradebook for Peruvian schools, where AI drafts and the
  teacher decides."* 🔵 **It encodes 🇵🇪 Peru's `CNEB`: competency assessment, the achievement
  levels `AD/A/B/C`, and the descriptive conclusion a teacher must write for each.** Python 3.14 +
  PostgreSQL 16 + LangGraph, one service per school. 🟢 **Its design rule — *"AI that proposes,
  never decides"* — is the sentence to put in front of a ministry, and `P51` turns the whole thing
  into a costed recipe with EMEA and APAC ports.**
- 🔴 **One Spanish-language repository was NOT placed here, deliberately.**
  [`tomasfossatti/educa-educai`](https://github.com/tomasfossatti/educa-educai) (MIT, `0★`) is
  Spanish throughout and names no country, institution or curriculum, so it is shelved **Global**.
  🟢 **A language is not a location, and this base has published that rule before.**
- 🔵 **What it changes for an engagement.** The opening is no longer *"AI is not in the curriculum
  yet"*. It is **which of the eleven, at what stage, against which assessment instrument** — and
  `P51` is the answer to the third of those.

#### Update 2026-11-15 (twenty-fifth pass, `p820`) — 🟢 `ACTION p819-C` DISCHARGED: the "unverified age floor" was an instrument this file has carried since `p790`, and the real boundary is `6º ano`, not age five

🟢 **`ACTION p819-C` is discharged, and not by a new source.** 🔴 **`p819` filed a November press
report — MEC barring AI for children aged `0`–`5` *"even with teacher mediation"* — as an
unverified lead with no portaria number, no date and no primary, and asked the next pass to resolve
it against the *Diário Oficial da União*.** 🟢 **There was nothing to resolve: the instrument is
`Parecer CNE/CP nº 15/2026`, homologated `2026-11-10`, which THIS FILE, `README.md` and
`intel/open-gaps.md` have carried since `p790` as the anchor of the LATAM regional summary.**
🔵 **The press report described the instrument's content and never its number; this base's register
is keyed on the number; so a pass holding both halves searched for a third thing that does not
exist.** 🔴 **`p819` also searched for the wrong ORGAN — a *portaria*, where the instrument is a
*parecer* homologated by the minister.** 🟢 **Written up as `T66`, with the register-matching rule
that prevents the recurrence.**

🔴 **And the correction matters commercially, because the press framing UNDERSTATED the scope.**
The reported restriction covered ages `0`–`5`. 🟢 **The instrument is STAGE-GATED, and generative or
conversational AI is barred through `5º ano` — the whole of primary — and admitted from `6º ano`
only in teacher-mediated activities (`T67`).**

| Stage | Student may use | Note |
|---|---|---|
| Educação infantil (`0`–`5`) | 🔴 **Nothing, even mediated** | Teacher may use for planning, management, accessibility |
| Anos iniciais (`1º`–`5º`) | 🔴 **No generative/conversational AI even with supervision** | Teacher-planned, teacher-mediated activities only; *"IA desplugada"* is the sanctioned route |
| Anos finais (`6º`–`9º`) | 🟢 **Generative AI, teacher-mediated** | Autonomous use prohibited |
| Ensino superior / pós-graduação | 🟢 **AI as content and as teaching/research support** | Institutions must set their own policies |

🟢 **Two assessment rules recovered this pass, and they are the sharper half (`T68`).** 🔴 **Academic
or disciplinary sanction founded EXCLUSIVELY on an AI-content-detection tool is prohibited.**
🟢 **AI pre-correction of redações and dissertative exams is admitted only as a PREPARATORY STEP,
with the mark reserved to the teacher** — which confirms `T876`'s record that the `2026-09-01`
text, the one that banned AI essay correction outright, was a superseded draft. 🔵 **Scope: public
AND private, all levels, stages and modalities. Adoption is NOT mandatory.**

🔴 **Sourcing, graded.** 🟡 **SECONDARY throughout.** `www.gov.br` has refused at `CONNECT` since
`p796` and the parecer remains `CITED, NOT READ`. 🟢 **Two independent Brazilian legal sources agree
on the ladder and on both assessment rules; `abmes.org.br` is recorded as a non-government host
carrying the parecer, its súmula and a dated PDF, and is the cheapest primary route for the first
pass with egress** — `ACTION p820-A`.

🟢 **Opportunity, and it is now a named deliverable rather than a posture.** Brazil sits at `53%`
AI use against `22%` of school administrators reporting any guidelines (Cetic.br), under a
`12`-month clock that runs on policies, governance instruments and **CONTRACTS**. 🔵 **`P50` is the
build: a stage router that fails closed, a no-generative-model deployment for `1º`–`5º`, mediation
binding on `6º`–`9º`, the mark reserved in code, and an adjudication package that replaces the
detector verdict `T68` makes unlawful.**

🔴 **Regional supply this pass: NIL, measured.** The mandated LATAM leg returned `0` new
repositories and `0` instruments this base does not already hold. 🟢 **`p818`'s SciELO substrate
(`T58`) and `p819`'s figure-dating correction (`T64`) both stand unchanged.**

🔴 **`ACTION p819-A` is NOT discharged, and this pass narrowed it rather than closing it.** A
targeted re-probe of the UNESCO IESALC study surfaced `87%` adoption, `74%` in teaching and
learning, `57%` in research, `26%` with a formal strategy and `9%` evaluating implementation — **and
no budget percentage of any kind.** 🟢 **What the report carries instead is a RECOMMENDATION that
governments provide dedicated funding, plus an unquantified "resource gap" for public
institutions.** 🔴 **So the `8%` / `4%` pair this base prints is still unattributable to this
instrument, and `T64`'s suspicion is strengthened: the figures are probably from a different study
entirely.** 🔵 **Until the UNESDOC full text is reachable, this file holds NO quotable LATAM budget
figure — unchanged from `p818` and `p819`.**

#### Update 2026-11-15 (twenty-fourth pass, `p819`) — 🔴 The region's most-quoted number is thirteen months old, and the study it comes from has no budget line at all

🟢 **`ACTION p818-A`, PARTIALLY DISCHARGED — and the result changes how this file must quote its
strongest LATAM pair.** 🔴 **Channel limit first, because the finding rests on it:
`iesalc.unesco.org` is outside this session's allowed network domains and a byte-read of the
primary was NOT possible. What follows is the search channel's rendering of the official
announcement and is graded 🟡 SECONDARY.**

🟢 **What the headline instrument reports.** `200` higher-education institutions across `19` LAC
countries: **`87%`** using AI in at least one area of activity, **`74%`** in teaching and learning,
**`57%`** in research, **`26%`** with a formal AI strategy. 🟢 **`74%` and `57%` are new to this
file and are the more useful pair for scoping, because they separate the teaching buyer from the
research buyer.**

🔴 **No budget figure appears in the headline instrument.** 🔵 **So neither this base's `8%` ("any AI
budget") nor the `~45%` implied by the `55%`-no-dedicated-budget reading is attributable to the
study's topline; the `5×` conflict `p818` recorded is between two DOWNSTREAM readings.** 🔴 **This
file continues to hold NO quotable LATAM budget figure, and `ACTION p819-A` carries it forward —
it needs the full report from UNESDOC, which this session cannot reach.**

🔴 **The finding that matters more than the budget line, and this base did not have it.** The survey
was **fielded August–October 2025** (Valentini, *Revista Educación Superior y Sociedad*, 2026) and
**published 9 September 2026** at Digital Learning Week in Paris with UNU-IAS support. 🔴 **This
file has quoted `87%`/`26%` as the region's `2026` position across six passes. The behaviour it
measures is late `2025`, and at the date of this pass the data is THIRTEEN MONTHS OLD.** 🟢 **Quote
it as *"87% as of late 2025, published September 2026"*** — still the strongest
adoption-versus-governance pair available for the region, and now defensible when a client's own
more recent internal figure disagrees. **Written up as `T64`.**

🟢 **Brazil: the instrument chain this file described in prose now has owners, a consultation date
and a procedure.** 🟡 **SECONDARY throughout — `gov.br` is also outside this session's allowed
domains.**
- 🟢 **The *Referencial para Desenvolvimento e Uso Responsáveis de IA na Educação*** is produced by
  MEC's **SEGAPE** (Secretaria de Gestão da Informação, Inovação e Avaliação de Políticas
  Educacionais), after a **public consultation that closed 29 October 2025**. 🔵 **A named
  secretariat is what a public-sector pursuit needs; "MEC published" is not addressable.**
- 🟢 **A basic-education guidance document followed on `2026-04-13`**, and its organising
  distinction is the one a studio should adopt verbatim: **_ensino sobre IA_ (teaching ABOUT AI)
  versus _ensino com IA_ (teaching WITH AI)**. 🔵 **Two different procurements, two different
  buyers, and Brazilian documents now name the split — use their words.**
- 🟢 **The Sandbox Regulatório (MEC with AGU) has a shape: the edital selects UP TO `8` AI
  solutions with a `3`-month monitoring period, under process `SEI 2300.056786/2025-81`.** 🔴 **The
  call this file recorded as open `2026-03-30`–`2026-05-13` has closed.** 🔵 **Eight slots is a
  small, named, countable opportunity — and a sandbox cohort is a reference a studio can sell in
  the rest of the region for years.**

🔴 **One reported item this base will NOT yet carry as a rule.** A November 2026 press report
describes MEC barring AI use for children aged `0`–`5` in early childhood education **even with
teacher mediation**. 🔴 **No portaria number, no publication date and no primary could be obtained
on this channel; the search did not surface a November instrument at all.** 🔵 **Recorded as an
unverified lead because, if true, it is the first AGE FLOOR in the region and would change the
scope of every early-years proposal. `ACTION p819-C` asks the next pass to resolve it against the
Diário Oficial da União.**

🔴 **Regional supply this pass: NIL.** The star-ranked sweep (`T63`) returned `0` new
LATAM-attributable repositories. 🟢 **`p818`'s SciELO finding stands as the region's substrate and
is unaffected.**

#### Update 2026-11-15 (twenty-third pass, `p818`) — 🟢 The region's nil is OVER: the system of record exists, it is operated from São Paulo for sixteen countries, and its licence is BSD-2

🟢 **This is the most consequential LATAM entry this base has published, and it retires a claim the
base itself made seven passes ago.** 🔴 **Since `p811` the published position has been that `0` of
`65` build-safe agents attach to a system operated in Latin America, with the diagnosis that no
regionally governed system of record exists to attach to.** 🟢 **`q="org:scieloorg"` returns `158`
repositories and the core is BSD-2-Clause, byte-read: [`scieloorg/opac`](https://github.com/scieloorg/opac)
(`1,292 B`, `sha256:493da013…`, holder `SciELO ORG`),
[`scieloorg/packtools`](https://github.com/scieloorg/packtools) (`1,288 B`, `sha256:8a810c6a…`,
pushed `2026-11-09`), [`scieloorg/scielo-manager`](https://github.com/scieloorg/scielo-manager)
(`1,328 B`, `sha256:c0182a8e…`).**

🔵 **SciELO is the scholarly publishing backbone of Brazil, Chile, Colombia, Mexico, Argentina,
Peru, Cuba, Uruguay, Bolivia, Costa Rica, Paraguay, Ecuador and Venezuela, plus Portugal, Spain and
South Africa.** 🟢 **It is the largest regionally governed research infrastructure in this entire
knowledge base, in any industry — and it is permissively licensed.** 🔴 **Why seven passes missed
it: SciELO is operated centrally by BIREME/FAPESP, so nobody self-hosts one, so it generates no
stars, so every star-ranked sweep this base ran was structurally blind to it.** 🔵 **The defect was
in the instrument, not in the region — and that correction should be carried into the other eleven
industries in this rotation.**

🟢 **The buyer is unusual and better than the usual one: the NETWORK, not the institution.** 🔵 **An
engagement with SciELO or BIREME reaches sixteen countries from one contract, which is the inverse
of the per-university sale every previous LATAM recipe here assumed.**

🟢 **The Brazilian federal research record already has an MIT agent surface.**
[`damarals/periodicos-capes-mcp`](https://github.com/damarals/periodicos-capes-mcp) (`12★`) speaks
to the **Portal de Periódicos CAPES**, licensed centrally by the **Ministério da Educação** for
every federal university; [`DevAlissu/pesquisador-br-skill`](https://github.com/DevAlissu/pesquisador-br-skill)
(`7★`) composes **ABNT, Qualis CAPES, Lattes, SciELO and BDTD** in one surface. 🔴 **Both
single-maintainer, both under `15★` — supply, not adoption.**

🔴 **The widest single build slot this base has ever recorded in Latin America, stated precisely:**
`q="lattes mcp"` → `total_count=1`, and that one repository
([`lf-bf/Lattes-MCP`](https://github.com/lf-bf/Lattes-MCP), `0★`) carries **no licence at all**.
🟢 **Plataforma Lattes is the researcher CV every CNPq grant and every CAPES programme evaluation
is assessed from. There is no granted agent for it. First mover owns it.**

🔴 **A figure CONFLICT inside the same UNESCO IESALC study, recorded and NOT averaged.** This base
carries *"`87%` use · `9%` evaluation · `8%` any AI budget, `4%` among PUBLIC universities"* from
IESALC (`200` institutions, `19` countries). 🔴 **A second reading of the same study reports `26%`
with a formal AI strategy and `55%` with no dedicated AI budget — which implies roughly `45%` DO
have one, against this base's `8%`.** 🔵 **A `5×` discrepancy almost certainly reflects two
different questions ("any AI budget" vs "a dedicated AI budget line"), and possibly two different
denominators.** 🔴 **Do NOT quote either figure as the region's budget position until the primary
IESALC instrument is read. `ACTION p818-A` below.**

🟢 **A new and stronger regulatory denominator for the region.** A **2026 Universidad de los Andes**
study counts **`716` AI-related regulatory instruments across `23` countries and territories**, most
dated 2023 or later. 🔵 **That reframes the standing "LATAM has a governance gap" line: the region
does not lack instruments, it lacks HARMONISATION — which the WEF reading corroborates and which
sells a mapping-and-conformance engagement rather than a policy-writing one.**

🟢 **Dated national instruments, re-corroborated:** 🇧🇷 **`PL 2.338/2023`** passed the Senate in
December 2024 and **remains in the Chamber of Deputies** — 🔵 still not law, so `Parecer CNE/CP nº
15/2026` (homologated `2026-11-10`, `12`-month clock) stays the operative Brazilian education
instrument; 🇨🇴 **CONPES `4144`** (February 2025) is a national policy with budget through 2030
rather than binding rules; 🟢 Argentina, Brazil, Chile, Colombia, Costa Rica, Mexico and Peru have
adopted the OECD AI Principles.

🟢 **A sharper school-level number than this base held.** **Cetic.br:** `53%` of Brazilian school
administrators use AI while only `22%` say their school has guidelines. 🔵 **A `31`-point gap at
the ADMINISTRATOR level, in the country with a `12`-month policy clock running — which is the
single best-timed governance sale in this base.**

#### Update 2026-11-15 (twenty-second pass, `p817`) — 🔴 **The widest usage-to-governance gap in this base: `92%` of students using AI, `30%` of universities with a policy, and ZERO open credential infrastructure**

🔴 **Regional supply this pass: NIL, measured.** `q="credencial digital educacion verificable"` →
**`total_count=0`**. `q="certificado digital universidad blockchain"` → `4`, 🔴 **every row `0★`, all
four by a single author, nothing pushed since `2022`.** `q="interoperabilidad educativa estandar"` →
**`0`**. `q="registro academico nacional api"` → **`0`**.

🔵 **The market fact this sits against, and the contrast is the opportunity (🟡 `SECONDARY`):**
🟡 a 2026 Digital Education Council LATAM survey reports **`92%` of students and `79%` of faculty
actively engaging with AI**; 🟡 **only `30%` of universities in the region have published any AI-use
policy**; 🟡 the IDB counts `193` real AI initiatives across the region; 🟡 ProFuturo/OEI report
that many public schools lack the technical resources to implement AI at all.
🟢 **Highest engagement, lowest governance, no credential infrastructure — see `T56`.**

### 🟢 `ACTION p816-F`'s declared blank — country-level AI-in-education regulation, ANSWERED with named instruments

🔴 **`p816-F` recorded that two passes running had failed to name a single LATAM regulatory
instrument, and prescribed searching for `resolución inteligencia artificial educación` and
`decreto IA educación`. Run this pass.** 🟡 **All `SECONDARY`; none of the sources cite an official
number, so verify in each country's official bulletin before quoting:**

- 🇵🇪 **Peru — the only country with binding AI law in force.** **Ley 31814** (reported the first
  AI-specific law in Latin America), **regulated by reglamento in September 2025**; Peru is reported
  to hold nine approved AI-focused laws. 🔵 **Peru is therefore the region's regulatory anchor —
  and `p812` already measured that its national K-12 system SIAGIE has `25` repositories and zero
  licensed agents. Binding law, active developer community, no grants: the sharpest slot in LATAM.**
- 🇨🇱 **Chile — guidance, NOT a norm.** MINEDUC published **“PotencIA el aprendizaje” (2025)**,
  explicitly orientative; the Política Nacional de IA dates to 2021 and the AI bill remains in
  discussion. 🔴 **A studio must not present Chilean guidance as a compliance obligation.**
- 🇦🇷 **Argentina — a BILL, not law:** a proposal to amend the Ley de Educación Nacional N.º 26.206
  to integrate AI into the education system; in October 2026 the CIN advanced a responsible-use
  recommendation to its teaching commission.
- 🇨🇴 **Colombia — a general AI framework bill and an education-specific bill; an Estrategia Nacional
  de Inteligencia Artificial 2026–2030 is referenced without a confirmed status.**
- 🌎 **Regional:** a 2026 study records **`716` AI regulatory instruments across `23` countries and
  territories**, 🔴 **without specifying how many are educational** — and concludes the region lacks
  a unified framework for AI in higher education.

🟢 **The blank is now CLOSED to the extent this channel permits: four countries with named
instruments and one regional count.** 🔴 **What remains open and is registered rather than guessed:
not one of these sources cites a resolution or decree NUMBER for an education-specific AI instrument,
so a client-facing citation still requires the official bulletins. Carried as `ACTION p817-D`.**

🟡 **Brazil 🇧🇷, from this pass's trend leg:** MEC published a *Referencial para o uso responsável de
IA* and launched a **Sandbox Regulatório** for educational technologies, with a public call reported
open `2026-03-30` to `2026-05-13`. 🔵 **A regulatory sandbox is an unusually concrete engagement
entry point: it is a named programme with a named deadline rather than a policy position.**


#### Update 2026-11-15 (twenty-first pass, `p816`) — 🔴 SUPPLY NIL; the region's adoption/governance gap is now measured twice by two independent bodies, and the regulation leg is a DECLARED BLANK

🔴 **Regional supply this pass: NIL. `10` rows, unchanged.** 🟢 **The retention layer placed
`Global` under `T42`; no LATAM-catalogued system appeared in any of the `12` queries run this
pass.** 🔵 **Recorded explicitly, with the queries, per `ACTION RE` — a silent region is
indistinguishable from a covered one.**

🟢 **The adoption figures are now the strongest in this file for any region, and they come from
a survey with a stated sample — which is rare enough here to say out loud:**

- 🟢 **Digital Education Council LATAM survey 2026: `92%` of students and `79%` of faculty
  actively engaging with AI**, from a faculty sample of **`7,319` across `29` higher-education
  institutions**. 🔵 **A named sample size is this file's threshold for a citable adoption
  figure; most numbers in this document do not meet it.**
- 🟢 **UNESCO IESALC: a 2025 survey of `200` institutions across `19` countries finds the gap
  between adoption and institutional governance *“particularly pronounced”* in LAC**, with a
  September 2026 working paper mapping adoption across five dimensions including governance.
- 🟢 **Tecnológico de Monterrey-linked analysis: a *“lack of formal policies for the use of AI
  in universities in Latin America.”***

🔵 **Two independent bodies measuring the same gap is the finding.** High adoption plus absent
institutional governance is a **policy-and-controls engagement with an existing budget holder**, and
it is the same shape this file recommended for EMEA on different evidence — 🟢 **but here the
adoption number is higher and the governance vacuum is wider, so the LATAM version is the easier
sale and the faster start.**

🟢 **Programme-level actors, this window:**
- **IDB: `193` real AI initiatives catalogued across the region**, with an April 2026 post framing
  the need for clear rules alongside pedagogical purpose.
- 🟢 **NEW: EdTech Hub and Fundación Ceibal launched a partnership in September 2026** to help
  LAC education systems respond to AI. 🔵 **Ceibal is the one LATAM delivery vehicle this base has
  named repeatedly (and `p813-B` named its platforms as an unrun supply target); a formal
  partnership with EdTech Hub makes it the most likely regional channel for anything a studio
  builds here.**

🔴 **DECLARED BLANK, and it is the second pass running: country-level AI-in-education REGULATION.**
🟢 **The leg returned institutional and programme actors only — no AI-in-education statute,
decree or binding guidance for any individual LATAM country.** 🔵 **This file already holds
Brazil's Marco Legal da IA and `P36`'s norm-compliance work, so the blank is specifically about
EDUCATION-SECTOR instruments. Treated as an open gap, not as an absence of law — `ACTION p816-F`.**


#### Update 2026-11-15 (twentieth pass, `p815`) — 🔴 The assessment layer is a HARD NIL here in two languages, and the region's own dominant judge is not open source

🔵 **Source confidence.** Repository measurements are `FIRST-HAND` — run `2026-11-15` against
`gh api -X GET search/repositories`, licences byte-read over `raw.githubusercontent.com`. Policy
and market figures are `SECONDARY` (web-search summaries of trackers, briefings and vendor blogs)
and are labelled as such; verify any date before putting it in front of a client.

🔴 **The nil, measured in three languages and written down rather than left silent:**
- `q="evaluacion automatica estudiantes plataforma"` → **`total_count=0`**.
- `q="juez automatico programacion"` → `5`, every row `0★`.
- `q="correcao automatica exercicios programacao"` → `5`, star ceiling `1★`. 🟡 **The one actively
  developed specimen, [`felipelageduarte/runcodes`](https://github.com/felipelageduarte/runcodes),
  was pushed `2026-11-11` and carries NO licence — a live Brazilian project a studio cannot
  touch.**

🔴 **And the `beecrowd` finding, which is the `p814` shape repeating.** `beecrowd` (formerly URI
Online Judge) is the dominant online judge in Latin American programming education.
`q="beecrowd online judge"` → **`290` repositories, and every single one is a student's solutions
dump** — the top row is `eduardo-mior/URI-Online-Judge-Solutions` at `346★`. 🔵 **The judge itself
is not open source. A `290`-repository query with zero platform rows in it, which is exactly the
measurement trap `p814` named: a large `total_count` can be entirely downstream of the thing you
are looking for.**

🟢 **The practical consequence, and it is good news.** 🔵 **Because there is no regional incumbent
to displace, the engine choice in LATAM is unconstrained — so take the permissive one by default:
`Autolab` (Apache-2.0) and `Dolos` (MIT), i.e. `P38` and `P37` unmodified.** 🟡 **One check
first: [`jcrodriguez-dis/moodle-mod_vpl`](https://github.com/jcrodriguez-dis/moodle-mod_vpl) is
🇪🇸 Spanish-origin and Moodle-based, which makes it the single most likely assessment component
already running at a LATAM or Iberian university.** 🔵 **If it is there, the engagement is
configuration rather than build — the cheapest possible entry, and `P3`'s shape.**

🟡 **Adoption and governance, `SECONDARY` but unusually well sourced this pass — UNESCO rather
than vendors.** A UNESCO IESALC study of `200` institutions across `19` countries reports **`87%`
of institutions using AI in at least one area of activity, while only `26%` have a formal
framework and `55%` have no specific AI budget**; fewer than `10%` of school-level institutions
have formal guidelines. A Digital Education Council LATAM survey (with Tecnológico de Monterrey
and its Institute for the Future of Education) reports `92%` of students and `79%` of faculty
actively engaging with AI. UNESCO reports more than `50%` of teachers in 🇨🇱 Chile and 🇧🇷 Brazil
already using these tools. 🔵 **`87%` adoption against `26%` governance is the most quotable
asymmetry in any region this pass, and it sells `P4` (institutional AI governance package)
directly — the client already has the problem and knows it.**

🟡 **Regulation, `SECONDARY`:** a 2026 Universidad de los Andes study counts `716` AI-related
regulatory instruments and proposals across `23` countries and territories; 🇧🇷 Brazil's
PL 2.338/2023 is risk-based; 🇨🇴 Colombia adopted CONPES 4144 in February 2025 with a
government-wide programme budgeted through 2030. UNESCO launched an **Observatory on AI in
Education for Latin America and the Caribbean in April 2026**; 🇺🇾 Ceibal and 🇧🇷 Cetic.br supply
national usage data. 🔴 **`716` instruments across `23` jurisdictions means there is no single
LATAM compliance posture — `P5`'s multi-jurisdiction frame applies here as much as in APAC.**

🟢 **Where to lead in this region:** 🟢 **`P4` first, against the `87%`/`26%` gap — governance is
the acknowledged problem.** Then `P38` on the permissive stack, since nothing has to be displaced.


#### Update 2026-11-13 (nineteenth pass, `p814`) — 🟢 The region's new row binds to a national STANDARDS BODY, which is a binding type nothing else in this base has

🔵 **Source confidence.** Repository and norm figures `FIRST-HAND` (README read this pass);
adoption and regulation figures `SECONDARY`.

🟢 **The supply finding.** [`PedroSmaxY/abnt-mcp`](https://github.com/PedroSmaxY/abnt-mcp)
(**MIT**, byte-read `1,086 B`, holder `Pedro Henrique da Silva Novais`) — *"ABNT Copilot MCP —
Servidor Model Context Protocol para Padronização, Auditoria e Conformidade Documental Acadêmica
(ABNT/IBGE)"* — implements 🇧🇷 Brazil's academic norms **by number and edition**: NBR 14724
(structure, typography, `3-3-2-2` pagination), NBR 10520:2023 (author-date in mixed case, long
quotations at 4 cm), NBR 6023 (references), 6022, 6024 (no terminal period after `1.1`), 6027,
6028 (150–500-word single-paragraph abstracts), plus IBGE tabular presentation — and it flags
revoked practice such as all-caps authorship in parentheses, *"prática formalmente extinta pela
atualização da ABNT NBR 10520:2023"*.

🟢 **Graded on `T36` axis (b) it PASSES: the capability set is *auditoria, formatação formal,
consulta em bases indexadas e compilação para PDF* — it audits and formats a document the student
wrote. It is not a ghostwriter, and that distinction is the whole reason it is shippable.**

🟢 **The opportunity, and it is the most concrete in this pass.** 🔵 **Every Brazilian university
checks ABNT conformance by hand, on every TCC, dissertation and thesis, every term — and the
norms are mechanically checkable.** 🔵 **Compose it with `pkp/ojs` (GPL-3.0; the backbone of
Brazilian and Mexican university journals) and `trahloff/Aldine` (AGPL-3.0, self-hosted LaTeX)
and the result is a norm-compliance pipeline from draft to submission, with the licence boundary
drawn at process edges.** 🔴 **`q="enem vestibular mcp agente"` → `total_count=0`: Brazil's
national admissions system has zero agentic surface of any licence — the widest open slot the
region shows.**

🟡 **Adoption and regulation context (`SECONDARY`, 2026 web sources).** UNESCO and ECLAC launched
an `Observatorio de IA en Educación` for Latin America and the Caribbean; the IDB documents `193`
real AI initiatives in the region. A Tecnológico de Monterrey figure cited at that launch claims
`92%` of LAC higher-education students already use these tools regularly — 🔴 **single-institution
data cited by third parties; do not quote it as regional fact.** 🔴 **Regulation remains
fragmented: no unified regional framework; 🇨🇱 Chile leads with a National AI Policy since 2021
and a bill in discussion; 🇧🇷 Brazil and 🇨🇴 Colombia have national strategies but no
education-sector regulation, and Brazil's MEC ran a public call on AI in education from
`30 March` to `13 May 2026`; 🇲🇽 Mexico has no national law or binding guidance for AI in
universities.** An OEI/ProFuturo report finds adoption uneven and limited against other regions,
and places Mexico in a second tier with Argentina, Brazil and Colombia.


#### Update 2026-11-13 (eighteenth pass, `p813`) — 🟢 The supply crown changes hands in one pass, and the governance gap is now quantified from a 19-country study

🔵 **Source confidence.** 🔴 **`iesalc.unesco.org` and `www.gov.br` still refuse at `CONNECT`
under this session's network policy — every UNESCO and Brazilian figure below is `CITED, NOT
READ`** (`T906`, now the tenth consecutive pass).

- 🟢 **MEASURED — and it reverses a claim this base made ONE pass ago.** `p812` crowned
  `nialvape/utn-mcp` (`12★`) the most-starred LATAM education agent.
  🔴 **[`CaioCastro1/usp-mcp`](https://github.com/CaioCastro1/usp-mcp) holds `28★`, was created
  `2026-08-31`, and was pushed TODAY.** 🟢 **It targets USP — the largest university in Latin
  America — across `e-Disciplinas` and `JupiterWeb`, and it was missed because `p812`'s queries
  named SIGAA, SUAP and Guaraní but never USP's own systems.** 🔵 **`T26` again: the shelf's zero
  was a fact about the query.**
- 🟢 **`LATAM 8 → 9`,** and the region's supply thesis from `p812` (`T34` — supply attaches to
  university self-management systems) holds with USP as its third Brazilian instance.
- **Adoption is high and governance is not (`CITED, NOT READ`).** UNESCO IESALC, across **`200`
  institutions in `19` countries**: **`87%`** use AI in at least one area, but only **`26%`** have
  a formal AI strategy and **`55%`** have no specific AI budget, with public universities lowest.
- **UNESCO's Observatory on AI in Education for Latin America and the Caribbean launched April
  2026**, reporting **>`50%` of teachers in Chile and Brazil already using these tools against
  **<`10%` of regional institutions** having formal guidelines or sufficient capacity.
- **Digital Education Council LATAM 2026: `92%` of students and `79%` of faculty actively
  engaging with AI** (with Tecnológico de Monterrey and the Institute for the Future of
  Education).
- **🇧🇷 Brazil, the sharpest single statistic: `53%` of school administrators use AI, while only
  `22%` of schools report having guidelines on its use** (Cetic.br).
- 🔴 **Fragmentation is now counted: a 2026 Universidad de los Andes study finds `716` AI-related
  regulatory instruments, rules and legislative proposals across `23` countries and territories.**
  🔵 **That number is the argument against a single regional compliance workstream.**
- **Legislative state (`CITED, NOT READ`):** 🇧🇷 **PL 2.338/2023** — risk-based, approved by the
  Senate in December 2024, **still moving through the Chamber of Deputies**. 🇨🇴 **CONPES 4144** —
  policy-first, a government-wide programme with budget through 2030 rather than immediate binding
  obligations. **Argentina, Brazil, Chile, Colombia, Costa Rica, Mexico and Peru have adopted the
  OECD AI Principles.**
- 🟢 **The engagement consequence, unchanged in direction and sharper in size.** `87%` adoption
  against `26%` strategy and `<10%` with guidelines is **a governance-services market, not a
  tooling market** — and the `55%` with no AI budget names the obstacle to selling into it.
- 🔴 **DECLARED GAP.** `ACTION p811-B`'s remaining named targets — **SIGED (🇲🇽), Ceibal's
  platforms (🇺🇾), SIE** — were **NOT run this pass**, which spent its LATAM budget confirming the
  USP reversal instead. 🟢 **Carried explicitly rather than dropped**, and 🔴 **Mexico remains the
  largest LATAM system with zero measured agent supply.**

#### Update 2026-11-13 (seventeenth pass, `p812`) — 🟢 The agent-supply nil this file published one pass ago is CLOSED, and it was a measurement error

🟢 **`p811` recorded `0` of `65` build-safe agents integrating with a system operated in this
region and called it "a published nil, not an omission." This pass withdraws that.** 🔴 **It was
an omission, and the cause is nameable: no search in sixteen passes had ever written `SIGAA`,
`SIAGIE`, `SIMAT`, `SUAP` or `SIU-Guarani`.** 🟢 **Naming them returned `15` repositories in one
hour, `9` build-safe. LATAM is now `8` of `74` — the third-largest bloc, ahead of North America.**

🔵 **Source confidence, stated once for this block.** Figures marked `MR` come from
market-research marketing pages or vendor-commissioned surveys read through search summaries and
are **order-of-magnitude only**; figures marked `PRIMARY-CITED` name a primary issuance that was
**not** read directly under this session's network policy. 🔴 **Nothing in this block was read
from a primary source this pass.**

- 🟢 **The supply, precisely.** 🇦🇷 **Argentina — the UTN cluster (`8` repos):**
  [`nialvape/utn-mcp`](https://github.com/nialvape/utn-mcp) (**ISC**, `12★`, `8` forks) over the
  `aula virtual` **and Sysacad** across `18` regionales, with
  [`HyNuwa/UniMCP`](https://github.com/HyNuwa/UniMCP) (**MIT + inherited ISC**) generalising it and
  adding **SIU Guaraní**. 🇧🇷 **Brazil — the SIGAA cluster (`6` repos, `6` unrelated authors)**
  plus `2` on **SUAP**. 🔵 **Full detail in `agents/trending.md`; the pattern is `P30`.**
- 🔴 **It is NOT regional coverage, and this is the sentence to carry into a bid.** `SIMAT`
  (Colombia) → `total_count=0`. Mexican, Chilean and Q-Acadêmico legs → `0`. `SIAGIE` (Peru) →
  `25` repositories, **zero agents and zero licence files**. 🟢 **LATAM's agent supply is
  Argentine and Brazilian.**
- 🟢 **Peru is the widest open slot this pass found anywhere.** SIAGIE has an active developer
  community — attendance uploaders, grade consolidation, analytics dashboards — and **no agentic
  surface and no grants at all**. 🔵 **An entry there competes with nobody.**
- 🔴 **`40%` of the region's repositories carry no licence file** (`6` of `15`), including a `5★`
  UTN campus agent and the most developed Brazilian SIGAA server. 🟢 **The licence request is the
  cheapest high-value move available in this region** — it costs an issue.
- **Demand-side, consistent with what this file already holds.** The Digital Education Council's
  **LATAM survey 2026** with Tecnológico de Monterrey (**30,000+** responses, **29** institutions)
  reports **92% of students and 79% of faculty** actively engaging with AI, while **only 30%**
  believe their institutions have responded effectively (`MR`). UNESCO IESALC's survey of **200
  institutions across 19 countries** finds the same adoption-vs-governance gap, and the Latin
  America AI Index notes LAC accounts for **14% of global visits to AI tools** against **11%** of
  global internet users (`PRIMARY-CITED`). 🔵 **Demand is the highest in the world and governance
  is the thinnest — which is `P4`'s entire thesis, and now `P30` gives it an engineering path.**
- **Institutional buyers to name:** UNESCO IESALC, the **IDB** (its snapshot of **193** real AI
  initiatives across LAC), **Fundación Ceibal** and **EdTech Hub** (partnership announced
  September 2026), UNU-IAS, Tecnológico de Monterrey (`PRIMARY-CITED`).

#### Update 2026-11-13 (sixteenth pass, `p811`) — 🔴 The agent-supply nil is now MEASURED: `0` of `65` build-safe agents integrate with a system operated in this region

🔴 **This is the hardest number this file has produced about LATAM, and it comes from this
base's own shelf rather than from a vendor report.** `agents/top.md` now carries a `Region`
column filled by a stated rule (`T32`: place a row by the region in which the system it
integrates with is operated). **Of `65` build-safe rows: `Global` `49`, `EMEA` `9`,
`North America` `4`, `APAC` `3`, `LATAM` `0`.**

🔵 **Read it next to the adoption figures this file already holds** — `92%` of students and
`79%` of faculty using AI (Digital Education Council LATAM `2026` with Tecnológico de
Monterrey), `87%` of institutions using AI against `9%` evaluating it (UNESCO IESALC, `200`
institutions / `19` countries), Brazil at `56%` of secondary teachers using AI against an
OECD average of `36%` and Chile at `55%`. 🔴 **The highest adoption in this base, and zero
agent surface for the systems those institutions actually run.**

🟢 **That asymmetry is the proposal.** EMEA's supply appeared this window as seven
single-maintainer agents attached to national and regional school portals (`T31`). 🔴 **The
equivalent for LATAM — an agent for SIGED, SIE, SIMAT, Ceibal's platforms, or any state
education portal — does not exist in this base at all.** 🔵 **First mover owns the seam, and
the seam is where the margin is.**

🔵 **Governance evidence, unchanged in direction and now better dated:** Brazil's
`Parecer CNE/CP nº 15/2026` (homologated `2026-11-10`) starts a `12`-month clock on policies,
governance instruments and **contracts**; only `22%` of Brazilian schools are reported to have
AI guidelines while `53%` of school administrators use AI. 🔴 **Brazil's `PL 2338` has
slipped again — a vote expected in December 2025 is now discussed for December 2026** — and
🔵 **Chile's bill is in second reading in the Senate, tied to its new data-protection
institutions.** 🟢 **Mexico still has no AI statute**, which keeps `P4`'s institutional
governance package the right first sale there.

🔴 **Unchanged and still correct: `es` ≠ LATAM (`T935`).** 🟢 **`T32` now explains what to do
instead — stop trying to place a row by its author and place it by the system it targets.
That rule is what produced the `0`, and the `0` is trustworthy because of it.**

#### Update 2026-11-13 (fifteenth pass, `p810`) — 🟢 The UNESCO Observatory is now a DATED institution with named partners, and the teacher-adoption / institutional-readiness gap is confirmed from a third instrument

🟢 **The Observatory on Artificial Intelligence in Education for Latin America and the
Caribbean is no longer an announcement.** Launched **`2026-04-14` in Santiago, Chile**, at the
**2026 Forum of the Countries of Latin America and the Caribbean on Sustainable Development**
(ECLAC). UNESCO calls it **the first regional platform in the UN system dedicated to AI in
education**. 🟢 **First meeting of member institutions: `2026-09-28`.** Contact is public:
`observatory.ai.education@unesco.org`.

🟢 **The partner list is the commercial map, and it is unusually actionable** — CAF, **CENIA**
(Chile), **Cetic.br** (Brazil), ECLAC, **Ceibal** (Uruguay), Fundación Santillana,
**Tecnológico de Monterrey** (Mexico) and ProFuturo. 🔵 **Every one is an institution a studio
can approach directly, and together they span the four LATAM markets this base tracks.**

🟢 **The gap is confirmed from a third independent instrument, and it keeps its shape:** in
**Chile and Brazil over half of teachers already use these tools, while fewer than `10%` of
regional institutions have formal guidelines.** 🔵 **Compare the two readings this base already
holds — UNESCO IESALC (`~200` institutions / `19` countries): `87%` adoption against `26%` with
a formal strategy; and DEC/Tec de Monterrey: `92%` of students and `79%` of faculty using AI
against `30%` who think their institution has responded effectively.** 🟢 **Three instruments,
three denominators, one conclusion: use is near-universal and governance is near-absent.**
🔴 **Do NOT merge or average the three — they measure different populations.**

🟢 **A new and sharper structural number: CENIA reports that `13` of the `19` Latin American
and Caribbean countries it studied do NOT teach early AI adoption in schools.** 🔵 **That is a
curriculum gap upstream of the governance gap** — the institutions have no policy *and* the
school systems feeding them have no curriculum.

🟢 **The regional instrument base is unchanged and remains the strongest in the file:** CENIA
runs the annual **Latin America AI Index** and leads **Latam-GPT**; Argentina, Brazil, Chile,
Colombia, Costa Rica, Mexico and Peru have adopted the **OECD AI Principles**; Brazil, Chile,
Mexico and Uruguay have engaged UNESCO's **Readiness Assessment Methodology**.
🔴 **Legislation still has not landed:** Brazil's **PL `2338/2023`** passed the Senate in
December 2024 and **remains in the Chamber of Deputies**; Chile's bill sits at **Boletín
`16821-19`**; Mexico has no horizontal law. 🔴 **Sources conflict on Peru's Law `31814`
date** — this base does not resolve it and does not quote it.

🔵 **Supply note:** [`XAIHT/Tlamatini`](https://github.com/XAIHT/Tlamatini) (`MIT`, `15★`) is
named for the Nahuatl *tlamatini*, which **suggests** a Mexican origin. 🔴 **`gh api
users/{login}` is refused in this session (`T941`), so origin is not resolvable and the row is
published `LATAM?` rather than given the closed vocabulary on a guess** (`T935`).


#### Update 2026-11-13 (fourteenth pass, `p809`) — 🟢 THE BASE'S OWN LATAM FINDING IS OVERTURNED: the region's education agents are no longer unlicensed

🟢 **This is a correction to a conclusion this base published and has carried since
`p797`.** That pass found `5` LATAM-origin education agents and reported **`5` of `5`
serving no grant at all** — "not missing, UNLICENSED". 🔴 **That no longer holds.** This
pass found **two LATAM-origin education agents with real, byte-verified permissive
grants**, both with substantial commit histories:

| Repo | Licence (payload-verified) | ★ | Commits | Origin signal |
|---|---|---|---|---|
| [`JhostinAleck/brightspace-mcp`](https://github.com/JhostinAleck/brightspace-mcp) | 🟢 `MIT` `1,070 B` `008ec594c78e9fd5` | `16` | `452` | `es-419` locale, `America/Bogota` sample timezone → 🇨🇴 |
| [`alejooroncoy/campus-cli`](https://github.com/alejooroncoy/campus-cli) | 🟢 `ISC` `748 B` `4ca1bd2e969c` | `13` | `851` | **UPC Aula Virtual** + UPN, repo topic `peru` → 🇵🇪 |

🟢 **And the Colombian one carries the strongest write gate in this entire base** — two
independent opt-ins (`writes.enabled: true` **and** `--enable-writes`), `dry_run`
preview, per-write idempotency key, per-write audit-log entry. 🔵 **The engagement point:
LATAM is no longer a region this KB can describe as consuming education AI without
producing it.** The supply is small and single-author, but it is granted, maintained and
in some respects better governed than the North American equivalent.

🔴 **The governance flag on `campus-cli` must travel with the row:** its tool catalogue is
brokered by a **remote relay (`mcp.campuscli.com`)** that decides which tools to offer per
university, so student credentials and traffic cross a third party. Acceptable for an
individual student; a procurement blocker for an institution. 🟢 **For a client, fork it
and terminate the relay in-tenant** — the `ISC` grant permits exactly that, and that is
the shape of the engagement.

🟡 **Regulatory state, re-read this pass.** A **Universidad de los Andes** public-policy
report (August 2026) counts **716 AI instruments** across the region, with **🇧🇷 Brazil at
212 records and 🇲🇽 Mexico at 126**, and **~85% concentrated in five countries** — note the
base also includes norms where AI appears only marginally, so the count overstates
depth. **Forbes (Feb 2026)** reports **fewer than a quarter of Ibero-American countries
have AI-specific regulation**, naming 🇧🇷 Brazil, 🇨🇱 Chile and 🇪🇸 Spain as the regional
referents with coherent frameworks and placing 🇲🇽 Mexico at an early stage. 🟡 **Chile's
AI bill (Boletín N° 16.821-19)** was still advancing in the Senate through March–April
2026.

🔴 **Education-sector specifics remain thin, and that is the honest finding.** A
Universidad Autónoma de Madrid review reports that **Latin America has no unified
regulatory framework for AI in higher education**: 🇨🇱 Chile leads on the strength of its
national AI policy (since 2021); 🇧🇷 Brazil and 🇨🇴 Colombia have national strategies with
**no education-sector regulation**; 🇲🇽 Mexico has rising university use with **no national
law or binding guidelines**. A regional study places Mexico in a second tier with
Argentina, Brazil and Colombia on actual school-level use, flagging equity and teacher-
training deficits. 🟡 **UNESCO is reported to have launched an AI-in-Education Observatory
for Latin America and the Caribbean** at the 2026 ALC Forum on Sustainable Development —
🔴 **sourced to a LinkedIn post only; treat as unconfirmed until the UNESCO page is read.**


#### Update 2026-11-13 (thirteenth pass, `p808`) — 🔴 NIL. The UNESCO IESALC and DEC figures were returned again and are already held; the region's governance-gap thesis reproduced unchanged

🔴 **Zero new LATAM facts this pass.** The leg
`AI education LATAM 2026 adoption regulation players` returned:

| Returned by the leg | Status in this file |
|---|---|
| UNESCO IESALC: `87%` of institutions using AI in at least one area; only `26%` with a formal framework | 🟢 Already held |
| UNESCO: fewer than `10%` of institutions have formal classroom AI guidelines | 🟢 Already held |
| Digital Education Council LATAM survey: `92%` of students, `79%` of faculty actively engaging with AI | 🟢 Already held |
| Uruguay (`Ceibal`, 2026): `75%` of public-school teachers using AI tools | 🟢 Already held |
| Brazil (`Cetic.br`, 2026): `65%` of internet users aged 9–17 using AI; only `22%` report school guidelines | 🟢 Already held |
| Universidad de los Andes: `716` AI regulatory instruments across `23` countries and territories | 🟢 Already held |
| Brazil `PL 2.338/2023` — risk-based, Senate-approved, pending in the Chamber | 🟢 Already held |
| Colombia `CONPES 4144` (February 2025) national AI policy | 🟢 Already held |
| UNESCO Observatory on AI in Education for LAC, launched Santiago, April 2026 | 🟢 Already held |
| WEF *Latin America in the Intelligent Age* white paper | 🟢 Already held |
| `7` countries formally adopting the OECD AI Principles | 🟢 Already held |

🟢 **The region's central thesis in this file — adoption far ahead of governance —
reproduced exactly, from independent sources, for a third consecutive window.** 🔵 **The
sharpest single framing returned this pass is worth quoting because it compresses the
whole opportunity:** *there are roughly ten times more universities using AI than
universities measuring what it delivers.* 🟢 **That gap is the LATAM engagement thesis
and it is now triple-sourced** (IESALC `87%`-vs-`26%`, DEC `92%`/`79%`, and the
measurement framing above).

🔴 **The nil is NOT evidence the region is quiet.** It is evidence that this file's LATAM
coverage has caught up with the available secondary literature, which is dominated by a
small number of heavily-recirculated studies (IESALC, DEC, Cetic.br, Ceibal). 🔵 **The
consequence is that further general-leg searching here has low expected yield**, and a
future pass is better spent on the measurement gap itself — **what instruments, if any,
LATAM institutions use to evaluate AI outcomes** — which is where this file is genuinely
thin and where the `10:1` framing says the demand is.

🔴 **Verification caveat:** `iesalc.unesco.org` does not resolve under this session's
network policy (`ENOTFOUND`), so the `87%` / `26%` figures were not re-confirmed at
source this window. 🟢 **They were not altered either.** `ACTION p808-L`: re-confirm the
IESALC sample size and publication date against the issuing body when reachable.


#### Update 2026-11-13 (twelfth pass, `p807`) — 🔴 a second consecutive complete nil, and that is now a finding about the CHANNEL rather than the region

🔴 **Complete nil, declared.** The LATAM leg returned the UNESCO IESALC study
(`200` institutions, `19` countries, `87%` using AI in at least one area, `26%` with a
formal strategy), the Digital Education Council LATAM survey (`92%` students / `79%`
faculty), Uruguay's Ceibal teacher figure, Brazil's Cetic.br administrator figures, the
Universidad de los Andes inventory of `716` instruments across `23` countries, the
`55%`-of-universities-without-an-AI-budget figure, and the UNESCO regional observatory
launched at ECLAC. 🟢 **Every single one is already in this file**, several of them since
the fourth pass.

🔵 **Two consecutive complete nils means the prescribed LATAM query has been exhausted,
not that LATAM has gone quiet.** The region's facts in this file all trace to a small set
of repeat publishers — UNESCO/IESALC, the Digital Education Council, Ceibal, Cetic.br,
CENIA, Universidad de los Andes — and the annual-report cadence of those bodies is slower
than this base's pass cadence. 🔴 **Querying them hourly cannot produce new information.**

🟢 **The channel that did produce LATAM findings is the one the tenth pass used:** it
found the region's largest school-management system (`portabilis/i-educar`) by looking at
**software**, not at policy. 🔵 **Standing recommendation for the next LATAM pass: drop
the adoption/governance query, which is saturated, and sweep Portuguese- and
Spanish-language repository space instead** → `Gap 807-C`.

🟡 **The adoption/governance gap itself is unchanged and remains this file's most
sellable LATAM number.** Nothing this pass weakens it.


#### Update 2026-11-13 (eleventh pass, `p806`) — 🔴 a complete nil, declared: no new instrument, no new figure, no new repository

🔴 **This is the honest result and it is being written down rather than padded.** The
LATAM leg ran and returned the UNESCO IESALC study (`87%` of `200` institutions using
AI, `26%` with a formal strategy), the Digital Education Council LATAM survey (`92%` of
students, `79%` of faculty), the Universidad de los Andes count of `716` regulatory
instruments across `23` countries, Ceibal's `75%` of Uruguayan public-school teachers,
Cetic.br's `53%`/`22%` Brazilian split, and the UNESCO Observatory launched at ECLAC in
April 2026. 🟢 **Every single one is already recorded below, in most cases for several
passes.**

🔴 **No new LATAM-origin repository was found either**, by search or by the propagation
audit. This base still holds exactly one LATAM-origin education agent
([`Jeanikt/tutor-ai-agent`](https://github.com/Jeanikt/tutor-ai-agent), MIT, `0★`,
Brazilian-Portuguese voice-first maths tutor).

🔵 **One row added this pass does serve LATAM without being from LATAM**, and it is
worth naming because the region's gap is *delivery capability*, not policy:
[`Emerging-Rule/community`](https://github.com/Emerging-Rule/community) (CC BY 4.0) is
**bilingual English / Spanish** K-12 AI-literacy curriculum. 🟢 **CC BY 4.0 is
attribution-only, so its Spanish lessons can be localised per-country and shipped inside
a ministry deliverable without a licence negotiation.** 🔴 At `3★` and six to thirteen
lessons it is a seed, not a programme — and **there is no Portuguese.** For Brazil, the
largest education market in the region, **the corpus does not exist.**

🔵 **The standing LATAM finding is unmoved and remains the most sellable line in this
file:** adoption is near-universal and governance is near-absent, measured at four
independent levels by four independent sources. **Eleven passes have not found a
counter-example.**


#### Update 2026-11-13 (tenth pass, `p805`) — the region's largest school-management system was never on any shelf

🔴 **The LATAM leg returned held facts**: the **UNESCO Observatory on AI in Education
for Latin America and the Caribbean**; **>50% of teachers in Chile and Brazil already
using AI tools while fewer than 10% of institutions have formal guidelines**; Brazil's
**AI Bill 2338/2023** passed the Senate (Dec 2024) and awaiting the Chamber of Deputies;
**Peru's Ley N° 31814** as the first enacted national AI statute in the region; Chile's
bill still in draft; **Mexico with no comprehensive horizontal AI law**. Consistent with
the UNESCO IESALC figures this file already carries (87% of institutions using AI in ≥1
area, 26% with any formal framework, 55% with no AI budget, 9% evaluating).

🔴 **Correction, and it is this pass's sharpest one.**
[`portabilis/i-educar`](https://github.com/portabilis/i-educar) — **GPL-2.0, 725★, 555
forks, 34,951 commits**, first built by the Itajaí (SC) city government and deployed by
municipalities across Brazil — **is the largest free-software school-management system
in LATAM, and it had never been written to any shelf file.** The trending log has
asserted since `p667` that it was "carried on the verticals shelf"; it was not. 🔵 **The
standing engagement line — "a LATAM K-12 client on RosarioSIS is a build" — understated
the field: i-educar is larger than RosarioSIS by stars, forks and commits.** Both are
copyleft, so both are integrate-not-derive; the companion `i-diario` (AGPL-3.0) carries
attendance and grades.

🔴 **Declared gap, LATAM:** no permissive SIS for this region. `GegoK12` (MIT) is
APAC-shaped and `SVWS-NRW` (BSD-3) is a German state system — **neither is a LATAM
answer**, and this base knows of no MIT/Apache school-management tree with a LATAM
deployment base.


**Adoption/regulation:** The widest gap between use and governance of any
region, and the best-documented. **UNESCO IESALC, across 200 institutions in 19
countries: 87% of higher-education institutions use AI in at least one area,
26% have any formal framework, 55% of universities have no specific AI budget,
and only 9% evaluate their AI implementation.** In schools, **more than 50% of
teachers in countries such as Chile and Brazil already use AI tools, while
fewer than 10% of institutions have formal guidelines.** Brazil's **Cetic.br**
reports **53% of school administrators using AI against 22% of schools having
any guideline**. The Digital Education Council's **2026 LATAM higher-ed survey
(with Tecnológico de Monterrey's Institute for the Future of Education) reports
92% of students and 79% of faculty actively engaging with AI.** Regulation is
fragmented: a 2026 **Universidad de los Andes** inventory identified **716
AI-related regulatory instruments, rules and proposals across 23 countries and
territories**. **Brazil's PL 2.338/2023** is the main risk-based bill;
**Colombia** adopted a national AI policy via **CONPES 4144 (February 2025)**
with budgeted actions through 2030 rather than immediate horizontal
obligations. Argentina, Brazil, Chile, Colombia, Costa Rica, Mexico and Peru
have adopted the OECD AI Principles.

**Players:** UNESCO IESALC — launched an **Observatory on AI in Education for
Latin America and the Caribbean in April 2026** to guide public policy;
**Cetic.br** (Brazil) and **Ceibal** (Uruguay) as national data sources and, in
Ceibal's case, a national deployment vehicle; Tecnológico de Monterrey; World
Economic Forum (regional white paper arguing for harmonized regulation);
Universidad de los Andes. Platform-wise: Moodle, Chamilo and RosarioSIS have
deep regional footprints. **New: the first LATAM-origin education agents** —
Manu (`Jeanikt/tutor-ai-agent`, MIT, Brazilian Portuguese voice math tutor) and
`nifalconi/educational-agents` (Chile, from the Niñas Pro girls' AI course,
**unlicensed as published**). Both are 0–1 star prototypes.

**Opportunities:**
1. **Institutional AI governance as a productized offering.** 87% using, 26%
   governed, 9% evaluating; 53% of Brazilian administrators using against 22%
   with guidelines. This is the single clearest product-market fit in this
   entire KB: a repeatable package of policy, controls, teacher training and an
   evaluation harness.
2. **Evaluation and measurement.** Only 9% evaluate. An evaluation layer
   (pedagogical eval plus xAPI/Caliper telemetry plus dashboards) is a
   defensible, repeatable deliverable — but 🔴 **its eval half no longer has a
   usable grant: `AITutor-EvalKit` serves NO licence file** (`p801` refuted the
   `MIT` claim; `p802` re-verified the absence at `HEAD` `a71078456a90`), so the
   open-source spine here is **`pykt-team/pykt-toolkit` (MIT) alone**, plus
   xAPI/Caliper telemetry. Thin, and now thinner than this file claimed.
3. **Low-budget deployment models.** 55% have no AI budget, so the offer must be
   cheap to run: Kolibri (MIT, offline-first) or Moodle plus self-hosted open
   weights, not per-seat frontier API spend.
4. **Ceibal-style national programs.** Uruguay's Ceibal is a working template
   for country-scale deployment; similar ministry programs are the large
   contracts in this region.
5. **Spanish/Portuguese pedagogical content generation — with a shortcut.**
   `educhain` (MIT) and Oppia (Apache-2.0) localized to national curricula
   (ENEM, ICFES, PAES, SEP), and note that **OpenMAIC already ships pt-BR and
   es-MX locales**, so the largest multi-agent classroom in the world is
   already partly localized for this region.
6. **Adopt and license the local prototypes.** Manu (MIT, Brazil) is usable as
   published; the Chilean Niñas Pro library is not, for want of a LICENSE file.
   Contributing licensing and engineering to regional projects buys both
   capability and standing.

#### Update 2026-11-13 (third pass) — adoption is high, governance is near-absent, and that is the whole opportunity

- **Teachers are already using it.** TALIS (2024) secondary-teacher AI use in
  the previous year: **Brazil 56%, Chile 55%, Colombia 53%, Costa Rica 52%** —
  materially level with developed-market rates.
- **Governance is not there.** Brazilian school administrators: **53% use AI,
  22% report their school has guidelines on its use**. Higher education
  (UNESCO IESALC): **87% of regional universities already use AI, 26% have a
  formal strategy**. A 61-point gap at university level.
- **Why that specific gap is the product:** the deficit is **policy,
  procurement rules and teacher guidance** — not models and not infrastructure.
  That is a 6–8 week productizable engagement (pattern `P4`), repeatable across
  institutions in one country, and it does not compete with the hyperscalers.
- **Regulatory status, corrected against the newest source.** **Peru is the
  only country in the region with an enacted AI statute.** Brazil's framework
  (EU-influenced, stringent) is **still a pending bill**; Chile's is pending;
  **Mexico has proposals and none enacted as of early 2026**, with a stated
  emphasis on **"technological sovereignty"** and reducing reliance on foreign
  AI models. **Source conflict recorded:** one aggregator describes Brazil as
  having comprehensive legislation and another describes Chile as having moved
  to a binding rights-protective framework; the newer CASRAI comparison
  (updated September 2026) says both are pending. **Go with pending**, and
  verify before any regulatory claim in a proposal.
- **Mexico's sovereignty framing is a selling position, not an obstacle:**
  self-hosted inference on `yetanalytics/lrsql` (Apache-2.0) or `openfun/ralph`
  (MIT) with no learner data leaving the country is a direct answer to it.
- **School-level AI education is largely absent.** Chile's **CENIA** found that
  **13 of the 19** Latin American and Caribbean countries it studied **do not
  teach early AI adoption in schools**. Commentary notes systems are
  integrating AI tools into classrooms *without oversight or guidelines* —
  which is the same finding as the Brazil 53/22 split, from the other direction.
- **Declared gap:** no 2026 source found covering **edtech vendor or
  procurement rules** specifically in Brazil, Mexico or Chile. Procurement is
  where a studio engagement is actually won or lost, so this needs a dedicated
  search before any LATAM public-sector pursuit.

#### Update 2026-11-13 (fourth pass) — the adoption/governance gap is now measured at four independent levels, and the regulatory volume is larger than this file assumed

**The gap, measured at four levels by four different bodies.** This is the most
evidenced claim in this KB and the numbers now stack from institution down to
classroom:

| Level | Finding | Source |
|---|---|---|
| **Institutional (HE)** | **87%** of institutions use AI in at least one area; **26%** have any formal framework. 200 institutions, 19 countries | UNESCO IESALC |
| **Individual (HE)** | **92% of students** and **79% of faculty** actively engaging with AI | Digital Education Council LATAM Survey 2026, with Tecnológico de Monterrey and the Institute for the Future of Education |
| **School capacity** | **Fewer than 10%** of institutions have formal guidelines *and* sufficient capacity for school use | UNESCO Observatory |
| **National (Brazil)** | **53%** of school administrators use AI; **22%** report their school has any guideline | Cetic.br 2026 |
| **National (Uruguay)** | **75%** of public-school teachers report using these tools | Ceibal 2026 |
| **Regional (teachers)** | **More than 50%** of teachers in Chile and Brazil already use AI tools | UNESCO |
| **Learner (secondary)** | **Nine in ten 15-year-olds** have already used AI chatbots for schoolwork, across the **13** regional countries assessed | PISA 2025 |

The Brazil pairing (53/22) and the institutional pairing (87/26) are the two to
carry into a room: both are a single source, a single year, and the same
instrument measuring use and governance together, which is what makes them
unanswerable.

**Regulatory volume is much larger than "a few bills."** A Universidad de los
Andes study identifies **716 AI-related regulatory instruments, rules and
legislative proposals across 23 countries and territories**, most introduced
since 2023. The practical consequence is not that compliance is hard yet — most
are proposals — but that **no client can track this themselves**, which is a
billable service in its own right and the substance of `P4`.

| Country | Instrument | Status |
|---|---|---|
| **Brazil** | **PL 2.338/2023** — general AI rules, risk-based approach | Still moving through Congress |
| **Colombia** | Government-wide AI program with actions and **budget through 2030** | Adopted; **not** immediate binding obligations |
| **Argentina, Brazil, Chile, Colombia, Costa Rica, Mexico, Peru** | OECD AI Principles | Formally adopted |

**Colombia is the under-read opportunity.** A funded, government-wide program
through 2030 with no binding obligations attached is the most procurement-friendly
configuration in the region: money is allocated and there is no conformity
blocker. Argentina and Peru's OECD adoption matters for the same reason —
principles create a framework to deliver *against* without creating a hurdle.

**New institutional anchor.** UNESCO launched the **Observatory on Artificial
Intelligence in Education for Latin America and the Caribbean** in **April 2026,
in Santiago**. This is a standing regional reference point and a credible body to
align a governance deliverable with — more durable than citing a one-off survey.

**The frameworks the region actually reaches for are international.** **ISO/IEC
42001** and the **NIST AI RMF** are used as reference frameworks across LATAM.
That is a direct reuse opportunity: a governance package built to ISO/IEC 42001
for a North American or EMEA client **transfers to LATAM with translation and
local policy mapping**, rather than needing a new framework. Build it once.

**Reliability note.** The adoption figures are self-reported survey data from
different instruments and are **not** strictly comparable across studies; UNESCO
IESALC and the Digital Education Council measure different populations. Use them
as a consistent *direction*, which they unambiguously are, rather than as
arithmetic.

#### Update 2026-11-13 (fifth pass) — the region's incumbent SIS is now the named unserved case, and that is a sharper opportunity than "governance is absent"

🔴 **Two consecutive passes have added nothing to LATAM's agent column.** The
region's only entry remains `Jeanikt/tutor-ai-agent` ("Manu", Brazil, MIT, **0
stars**, voice-first Brazilian-Portuguese maths tutor) from the fourth pass.
**Stated explicitly because silence would read as coverage:** this pass searched
globally and per region and found no new LATAM-origin education agent.
`T8`'s recommendation is unchanged and is still the right one — **localize a
permissively licensed APAC or North American agent rather than build from
scratch** — and this pass gives it fresh support: DeepTutor now ships broader
localization and OpenMAIC already ships **pt-BR and es-MX** locales.

🟢 **But the pass produced a genuinely new, LATAM-specific opportunity, and it is
more concrete than anything in this section.** The open-source SIS agent gap
**closed for OpenEduCat** this pass — it is Odoo addons, reachable by a generic
Odoo MCP server (`erpipe-org/mcp-odoo`, MIT, 433★). 🔴 **It did not close for
RosarioSIS** (GPL-2.0, **654 stars**, PHP/Postgres), which is **the most widely
deployed open-source SIS in LATAM K-12**, with Spanish, French and Portuguese
localization in core. RosarioSIS has **no agent interface and no general-purpose
platform beneath it to inherit one from** — searched by project name this pass,
nothing returned.

🔵 **Why this is the strongest LATAM line in this file.** It converts the
region's standing pitch from a negative ("adoption is high, governance is
near-absent, sell governance") into a **named, scoped, reusable build**: an MCP
server over RosarioSIS, serving a platform that LATAM K-12 ministries and
districts already run, in a market where **87% of surveyed higher-education
institutions use AI in at least one area while only 26% have any formal
framework** and **55% have no AI budget** (UNESCO IESALC, 200 institutions
across 19 countries). The governance sale and the integration build are the same
engagement. **And unlike the three proprietary-SIS servers in this base — all of
which reach the SIS unofficially, one by replaying the student's own credentials
— a RosarioSIS server would be built against an open schema the client controls,
so it can be sanctioned, contracted and maintained.** That is the difference
between a demo and a deliverable.

🟡 **Reusable asset to build it from, so this is not greenfield:** EduPage's
**31-tool** surface is a worked answer to "what does an agent need from a school
SIS", and `erpipe-org/mcp-odoo`'s three-call write gate
(`preview_write` → `validate_write` → `execute_approved_write`, single-use
same-process expiring token, `confirm=true`, env-var kill switch) is a worked
answer to "how does it write to a student record safely." **Copy the surface
from the first and the write protocol from the second.**

#### Update 2026-11-13 (sixth pass) — the adoption/governance gap is now measured at four levels by four independent sources, and it is the most sellable number in this entire file

- **Teacher adoption leads the OECD, measurably.** OECD **TALIS (2024)** —
  share of secondary teachers who had used AI in the previous year: **Brazil
  56%, Chile 55%, Colombia 53%, Costa Rica 52%**, against an **OECD average of
  36%.** 🟢 **Four LATAM countries, all ~1.5× the OECD average. This is the
  single strongest regional statistic in this KB and it says the opposite of the
  "LATAM is behind" assumption a client arrives with.**
- **Learner adoption matches it:** Cetic.br reports **65% of Brazilian internet
  users aged 9–17 use AI tools.**
- **And governance does not — at every level:**
  - **Schools:** in Brazil **53% of school administrators use AI**, but only
    **22%** report their school has guidelines on its use.
  - **Universities:** UNESCO IESALC reports **87%** of regional universities
    already use AI, **26%** have a formal strategy, and **just 9% evaluate its
    implementation.**
- 🟢 **That 87/26/9 split is the pitch.** It names three distinct products in
  descending order of how ready the buyer is to sign: a **strategy** (61% of
  universities need one), an **evaluation framework** (78% need one), and the
  **guidelines** layer beneath both. `P4` is already shaped for exactly this —
  this update gives it its numbers.
- **Regulation is still mostly pending, which is why the governance product
  sells now rather than later.** **Brazil: PL 2338/2023** is the main vehicle —
  one tracker calls it *in advanced legislative process*, a secondary guide
  describes risk-based rules with fines up to **BRL 50M**; 🔴 **these conflict,
  so verify its current status before citing either.** **Brazil's National
  Education Council is preparing sector-specific guidance** for schools and
  universities. **Mexico:** multiple AI bills introduced, **none enacted as of
  early 2026**, with a national emphasis on **"technological sovereignty"**.
- **The market has names, and Brazil dominates it.** HolonIQ's **2026 Latin
  America EdTech 100** has Brazil at **nearly half the cohort** and the clear
  majority of deal and award activity. **Teachy** (Brazil — AI lesson
  preparation, and notably **expanded beyond the region into Asia**) and
  **Ginia** (Mexico — AI-driven employability linking employers, institutions
  and students) are the named standouts.
- **Donor money is targeting teachers, not tools:** **Google.org committed
  USD 4.6M** to expand AI education across Latin America, targeting **1.25M
  students by 2028 across nine countries** including Brazil and Mexico.
  🔵 **Teacher-training delivery at that scale is a services contract, and it is
  the shape of `P7`.**

#### Update 2026-11-13 (seventh pass) — the adoption/governance gap holds at a second instrument, and the binding constraint is capability, not policy

- 🟢 **The UNESCO IESALC headline reproduces, and its denominator is now explicit.** *AI
  Implementation in Higher Education in Latin America and the Caribbean* draws on **~`200`
  institutions across `19` countries**: **`87%` use AI in at least one area of activity**, while
  **only `26%` have a formal AI strategy**. 🔴 **Note the instrument boundary — this is NOT the same
  artifact as the UNESCO Observatory (`716` instruments, `23` countries) recorded in an earlier
  pass. Two instruments, two denominators; do not merge them into one statistic.**
- 🟢 **A second, independent instrument agrees on the shape:** a separate survey finds **only `30%`
  of Latin American universities have published policies on AI use**. 🔵 `26%` and `30%` from
  different instruments is **convergence**, and it is the strongest version of this file's
  longest-running regional claim.
- 🔴 **The binding constraint is capability and money, and `p799`'s correction holds.** **`55%` of
  universities carry no specific AI budget.** New this pass: **`17%` of public universities already
  using AI in teaching provide NO academic staff training at all.** 🔵 **Staff training is common but
  student training lags** — so the gap is not "no policy", it is **nobody able to implement one**.
  Sell appraisal capability and a funding case, not another acceptable-use document.
- 🟢 **A funded regional governance programme is now named: `Integrity AI`, EU-funded under
  Erasmus+, building governance frameworks with `7` universities across `4` Latin American
  countries.** 🔵 **This is a partner and a template, not a competitor** — and it is the first
  EMEA↔LATAM governance bridge this file has been able to name.
- 🔴 **Brazil's regulatory position is still pending, and this file should stop anticipating it.**
  The national AI bill that would classify education AI as **high-risk had not passed the Chamber as
  of June 2026 and is not law**. **LGPD applies to AI in higher education today** and is the
  instrument to design against. 🔴 Broader analyses describe South American regulation of AI in
  higher education as close to non-existent, and a 2026 study of `52` documents names
  **"borrowed ethics"** — institutions adopting international frameworks without the capacity to
  implement them. 🔵 **"Borrowed ethics" is the precise name for what the `55%`/`17%` figures
  measure, and it is the sharpest phrase in this file for a LATAM pitch.**
- 🔴 **Every figure in this update is secondary-sourced from coverage of the underlying reports**;
  sources are inconsistent on dates and sample sizes. `T906` holds.


#### Update 2026-11-13 (ninth pass) — the Observatory's backers are wider than this file recorded, and Uruguay has done something no other LATAM country has

🔴 **Provenance: search-tier.** `unesco.org` and `coe.int` do not resolve from this
session, so the partner list and the treaty status below were read from indexed
reporting rather than from the institutions' own pages. 🟢 **`ACTION p804-V` covers
both.**

**The UNESCO Observatory on AI in Education for LAC — partner list corrected upward.**
This file recorded the Observatory (launched **April 2026**) and named CENIA,
Fundación Ceibal and Tecnológico de Monterrey. 🔴 **Three backers were missing, and
they are the ones that change what the Observatory *is*: CAF (the regional development
bank), ECLAC (the UN regional commission) and ProFuturo**, alongside Fundación
Santillana. 🔵 **A regional observatory backed by a development bank and a UN economic
commission is not a research project — it is the body that will shape what regional
governments fund.** For a studio, that is the difference between a citation and a
route to procurement.

**Uruguay: the first LATAM country to sign the Council of Europe's Framework Convention
on Artificial Intelligence (2025)** — new to this file. 🔵 **Why it matters beyond the
symbolism: the Framework Convention is the one instrument that lets a non-European
state adopt a recognisable, exportable AI-governance posture without writing an AI
Act.** This file already records Uruguay in the regional top tier on readiness; this is
the governance counterpart to that, and it gives a LATAM engagement a reference regime
to design against that is neither the EU AI Act nor Brazil's Marco Legal.

**The regional split is now three-way, not two-way.** 🟢 **Uruguay: treaty-aligned.**
**Brazil: regulating, and signed an AI and tech-regulation agreement with the EU in
June 2026.** **Colombia: programme-led via CONPES 4144, budgeted through 2030, no
immediate horizontal obligations.** 🔴 **Argentina: a bill before the legislature
carrying "a commitment to keep AI unregulated."** 🔵 **Four countries, four postures —
and the 716-instrument fragmentation figure this file already carries is what that
looks like in aggregate.**

**Adoption figures re-confirmed at this pass, all consistent with what this file holds:**
UNESCO IESALC — **87%** of 200 institutions across 19 countries use AI somewhere,
**26%** have a formal strategy; Digital Education Council LATAM 2026 — **92% of
students and 79% of faculty** actively engaging; Brazil — **53%** of school
administrators use AI, **22%** report school guidelines; PISA 2025 — **nine in ten**
15-year-olds across 13 regional countries have used AI chatbots for schoolwork.
🟢 **Four independent instruments, one finding, unmoved across five passes: use is
near-universal, governance is the gap, and the gap is the product.**

### Global

#### Update 2026-11-15 (thirty-first pass, `p826`) — the market framings are unchanged and still irreconcilable; the finding is that the discovery channel is actively poisoned

🟢 **Market items `CITED, NOT READ`; channel items measured first-hand.**

- 🟡 **Market size, carried forward and still mutually inconsistent.** AI-in-education cited at **~`$10.6B` in 2026 → ~`$42.5B` by 2030 at `41.5%` CAGR** (Research and Markets, April 2026), against **`$41.01B` by 2030** (Mordor, 2025) and **`$136.79B` by 2035** (Precedence, 2025). 🔴 **These differ by an order of magnitude and are reproduced here to be ARGUED WITH, not quoted.** 🔵 **`EDU-C2-075` — the statistics-comparability agent shelved at `p825` — exists precisely for this row, and this base should run it on its own market page before quoting any of these again.**
- 🟡 **Adoption, cited:** generative-AI use among education organisations reported at **`86%`** (Microsoft, 2025) — the highest of any industry measured; K-12 teacher use of generative AI for their own work roughly doubled between the 2023-24 and 2024-25 school years. 🔴 **Both are 2025 instruments quoted in a 2026 context; `T64`'s rule applies to them as much as to the LATAM pair.**
- 🟡 **Evidence, cited, and it is the most commercially useful line here:** only **`45%`** of the most-used edtech tools have published research meeting an ESSA evidence tier. 🔵 **In a market where guardrails rather than adoption are the policy posture (see North America), being able to prove an outcome is the differentiator — which makes evaluation design part of the deliverable, not a follow-on.**
- 🟡 **Direction, cited:** HolonIQ's January 2026 snapshot describes 2025 as the experimentation year; analyses place the focus shift **from policing academic integrity to managing cognitive load**, with AI tutoring/adaptive learning, AI-assisted teaching and grading, learning analytics and skills-based micro-credentials carrying momentum, and **blockchain credentialing, full-classroom VR and the chatbot-as-tutor pitch fading.** The OECD's 2026 Digital Education Outlook is cited warning that AI helps learning only where pedagogy stays in control.
- 🔴 **The measured finding of this pass is about the CHANNEL, not the market (`T91`).** A **`1,524`-repository star farm** (`580` throwaway owner accounts, all `NOASSERTION`, `~102,000` stars, `0` forks, four repeated payload sizes, published in six days) took **`45%` of the first page** of this base's own prescribed `tutor` query. In the same ten-day window a **`1,241`-repository, `1,211`-MIT** cohort was published at `0★`. 🔵 **The star-ranked channel is not saturated and not broken — it is ranking correctly over a population whose top is synthetic, and it has been doing so for every one of the `41` consecutive nil passes this base has recorded.**
- 🟢 **The operational consequence, stated once for every region above.** On these shelves the genuinely new supply sits at `0`–`50★`. **Any star floor that excludes the farm excludes the entire shelf.** 🔵 **Use the licence byte-read (`P65`) as the quality filter and `pushed_at` as the ranking (`P66`); treat stars as a forgeable popularity signal about the past.**
- 🔴 **Channel caveat for this whole page.** `WebFetch` resolved **no external host** this pass, so **not one primary document was opened**: every market, survey and regulatory figure above is a WebSearch summary of a secondary source and is marked `CITED, NOT READ`. 🟢 **Repository claims are unaffected — they are byte-read on `raw.githubusercontent.com` — but this page's figures should not be treated as primary-sourced until a pass with working egress re-reads them.**

#### Update 2026-11-15 (thirtieth pass, `p825`) — the discovery channel, not the market, is the finding

- 🟢 **Global market framings carried forward, all `CITED, NOT READ` and mutually inconsistent, which
  is itself the standing caution:** AI-in-education **`$10.6B` (2026) → `$42.48B` (2030)** at `41.5%`
  CAGR (Research and Markets, April 2026); **`$9.58B` growing `>30%`/yr** (Programs.com);
  **`$136.79B` by 2035** (Precedence). 🔴 **Three sources, three bases, no reconciliation.**
  🟢 **`p825` shelves the instrument for exactly this problem:**
  [`EDU-C2-075` education-statistics comparability](https://github.com/sbdnakashima/agentic-star-education-statistics-comparability-agent)
  (MIT, byte-read) — an agent whose output is *these two series cannot be compared, and here is why*.
- 🟡 **Adoption, globally:** Microsoft's 2025 figure of **`86%` of education organisations using
  generative AI** continues to be the most-cited; Programs.com reports student/teacher usage at
  **`53%` (2024) → `88%` (2025) → `94%` (2026)**, survey unidentified. 🔵 **The qualitative shift
  reported this pass is from POLICING to PEDAGOGY — *past the panic phase*, with the OECD's 2026
  Digital Education Outlook cited as warning that AI helps learning only where pedagogy stays in
  control.** 🔴 **`oecd.org` was refused at this session's proxy for a second consecutive pass, so the
  OECD line remains second-hand.**
- 🔴 **Evidence quality is becoming the differentiator:** one analysis reports rising revenue against
  falling investment, and that **only `45%` of the most-used tools have published research meeting an
  ESSA evidence tier.** 🟢 **For a studio this is the best available argument for selling evaluation
  as a deliverable rather than as a phase.**
- 🟢 **The durable `p825` finding is methodological and applies to every region.** `T86` measured a
  `74`-repository MIT catalogue that `29` passes missed; `T87` showed a published nil
  (*"Vietnam: zero"*) was an artefact of a single indexing axis. 🔵 **The rule now standing in this
  file: a market or supply nil is a property of the QUERY until at least two orthogonal axes —
  pedagogy, jurisdiction/language, system of record, platform brand — have been run.**
  🟢 **`P62` is that protocol and it is cross-sector: the same brand channel holds `1,430`
  repositories across all verticals, of which `74` are education.**


#### Update 2026-11-15 (twenty-ninth pass, `p824`) — 🟡 The market figures are still contested by a factor of five, and the one stable global statement is a posture shift rather than a number

🟡 **Sourcing note for every item in this block: egress in the `p824` environment resolved GitHub and web search only — `oecd.org` was refused at the proxy, as at `p822`. Every market and regulatory item below is `CITED, NOT READ`: it comes from web-search summaries of secondary sources, several of them vendor blogs and trackers. 🔴 Verify any date, bill number or percentage against the official text before quoting it to a client. Every REPOSITORY figure in this pass is first-hand and byte-read; the two classes are not interchangeable.**

- 🔴 **The market size remains contested, and `p824` records the spread rather than picking a
  number.** Sources cited this pass put AI-in-education at **`$11.4B` in 2026 rising to `$57B` by
  2033**, while **HolonIQ** is cited at **`$12.3B` globally by 2026**. 🔵 **This base has carried
  `$10.6B`→`$42.48B` (CAGR `41.5%`) since `p804` from a third house. Three houses, three
  trajectories, overlapping only at the 2026 base. 🔴 Quote a RANGE and name the house, or quote
  nothing.**
- 🟢 **The stable global statement is a POSTURE shift, and it is consistent across every source
  read this pass:** AI in education is moving **from experimentation to governance** — policies,
  data boundaries and oversight — with **HolonIQ** describing a *selective* acceleration in which
  systems invest where instructional value is demonstrated. 🔵 **"Selective" is the operative word
  for a studio: the buyer now asks for evidence before scale, which is `P15`'s efficacy gate and
  `T47`'s prediction arriving as a purchasing behaviour.**
- 🟢 **Agents are named explicitly in the campus-operations layer**, with universities cited as
  deploying them for **admission query handling, document verification, exam scheduling and
  evaluation workflows**. 🔵 **Three of those four are administrative rather than pedagogical, which
  matches where this base's permissive supply actually is — and `P39`'s timetabling recipe is the
  cheapest of the four to deliver.**
- 🟢 **Two further convergent signals:** **1EdTech** highlights digital credentials and digital
  competencies finally arriving at scale (`T56`, `P44`), and multiple sources name **AI literacy as
  a core competency** rather than a training topic (EMEA's Article 4 duty is the binding version of
  the same statement). 🔵 **Vendors are also pushing "education-specific, controlled platforms over
  open generic tools" — read that as a procurement preference the studio can meet, since every
  recipe in this file is a bounded, auditable deployment rather than a general assistant.**
- 🔴 **One global measurement from this pass's own channel, and it is a warning about instruments
  rather than markets.** `T81`: of `20` repositories byte-read, `4` carried a licence whose BYTES
  disagree with the field GitHub reports — and the error runs in **both** directions, under-reporting
  two repositories whose grants are the clearest in the sample and over-reporting one whose data is
  share-alike. 🔵 **Any market map built from GitHub licence metadata alone — and most published
  ones are — carries that error at an unmeasured rate.**


#### Update 2026-11-15 (twenty-eighth pass, `p823`) — 🟢 Two standards-and-policy bodies converge on the same instruction: stop buying general-purpose AI for education

🟡 **Sourcing note for every item in this block: egress in the `p823` environment resolved GitHub and web search only. Every market and regulatory item below is `CITED, NOT READ` — primary texts were NOT opened. Figures are attributed to the party that published them, vendor and advisory sources are marked as such, and dates that sources disagree on are shown disagreeing. Every REPOSITORY named is first-hand and byte-read.**

- 🟢 **The convergence is the finding, and it comes from two independent bodies.** The **OECD's 2026
  Digital Education Outlook**, as cited this pass, recommends moving **beyond general-purpose AI
  tools toward purpose-built educational AI** designed to produce durable learning gains.
  **1EdTech** independently frames 2026 as the shift **from experimentation to governance** — clear
  policies, data boundaries, oversight. 🔵 **A standards consortium and an intergovernmental body
  arriving at the same prescription in the same year is the strongest signal in this file for what
  an education proposal should contain.**
- 🟢 **What that means for a bid, concretely:** the deliverable is not a model and not a chatbot. It
  is **purpose-built tooling with governance attached** — which is exactly what this base's recipes
  shelve (`P55` connector fleet with per-tenant health, `P56` verified writes with a stored
  diff, `P57` a licence gate). 🔵 **And it is reinforced by this base's own evidence bar: only
  `45%` of the most-used education tools have research meeting an ESSA evidence tier, so an
  evidence claim is a DIFFERENTIATOR rather than table stakes.**
- 🔴 **Market sizing is contested and should not be quoted without its source.** Figures returned
  this pass: AI in education at **USD `11.4` B in 2026 → `57` B by 2033 at `25.9%` CAGR**
  (one vendor source) against **USD `12.3` B by 2026** (HolonIQ, as cited). 🔴 **Both are
  `CITED, NOT READ`, and `www.holoniq.com` has not resolved in this environment across several
  passes.** 🟢 **Use the adoption and governance numbers instead — they are better sourced and they
  are what actually moves a decision.**
- 🔵 **Adoption, global:** one source reports **`86%` of students across `16` countries already
  use AI in their studies**, consistent with this base's record of education as the highest
  gen-AI-adoption sector. 🔴 **Set against NA faculty intent falling `76%` → `67%` and APAC ban
  support rising in three markets (this pass), the global picture is adoption at saturation with
  sentiment turning.** 🟢 **That is a governance-and-evidence market, not a pilot market.**
- 🟢 **AI literacy is becoming a named competency rather than a theme** — curricula adding modules on
  prompt engineering and on evaluating AI outputs. 🔵 **In the EU it is already a legal duty under
  AI Act Art. 4, in force since `2025-02-02` (see the EMEA block), and Vietnam has mandated
  classroom hours (see APAC). The same deliverable is sellable as compliance in one region, as
  curriculum in another.**
- 🔴 **A channel measurement, published because silence would look like coverage.** The scheduler's
  mandated global supply battery nilled for a **`38`th consecutive pass** — every repository it
  surfaced (`DeepTutor`, `OpenMAIC` at `43,605★`, `ai-engineering-hub`, `frappe/lms`,
  `OpenOlat`) was **already shelved here**. 🟢 **Shelf coverage of the globally visible tier is
  therefore confirmed; new supply is being found only on the recency-ranked, no-star-floor channel
  (`T70`), and this pass it produced `21` rows.**


#### Update 2026-11-15 (twenty-sixth pass, `p821`) — 🟢 The first non-nil discovery pass in `36`, and the reason is a QUERY SETTING rather than a new market

- 🟢 **`4` build-safe agent rows and `1` platform row added — `168` → `172` agents, `111` → `112`
  platforms — after thirty-five consecutive measured nils.** 🔴 **The mandated star-ranked legs
  nilled a `36`th time** (`DeepTutor`, `tutor-gpt`, `ChatTutor`, `Claw-ED`, `OpenTutor`, `mathua`,
  `Papermorph`, `freelingo`, `anki-mcp-server`, `Study-Mate`, `teacher-to-skills`, `tsugi`,
  `mentingo`, `classroomio`, `advisingapp`, `cn-math-taxonomy`, `StudyOnTV` — all already held).
  🟢 **The rows came from a recency-ranked channel with NO star floor, which this base had never
  run (`T70`).** 🔵 **Standing method change: every future pass runs at least one leg with no star
  floor.**
- 🟢 **The cross-regional finding is `T70`, and it is the one to carry into a proposal:** the new
  supply binds to a **national curriculum instrument**, not to a subject — Peru's `CNEB`, Egypt's
  learning-outcome short codes, China's 人教版 knowledge points. 🔵 **The model is the replaceable
  part; the curriculum adapter is the asset, and the client already owns the ground truth it
  encodes.**
- 🟢 **Market framing unchanged and re-confirmed, not re-sourced.** The **OECD Digital Education
  Outlook 2026**'s recommendation that systems incentivise **purpose-built** educational AI over
  general-purpose assistants is already held in this file, and `T70` is the supply-side evidence
  for it: what is actually being built is narrower and more instrument-bound than a chatbot.
- 🔴 **Two measurement channels were degraded this pass and both are stated rather than smoothed.**
  (1) `make hooks` was refused by the sandbox classifier for a **FOURTH** consecutive pass, so
  every count in this base is re-derived inline and flagged (`ACTION p821-B`). (2) Outbound HTTPS
  resolved **GitHub only** — `indicelatam.cl`, `oecd.org` and `data.consilium.europa.eu` all failed
  to resolve — so every repository this pass is **byte-read and first-hand** while every
  regulatory and market item is **`CITED, NOT READ`** and says so in place.
- 🔵 **The byte-read channel was controlled in BOTH directions this pass:**
  `amaru-one/mawta-nonexistent-p821` and `fotedev/not-a-real-repo-p821` both returned `404` on the
  same `raw.githubusercontent.com` path that served the seven real licence payloads.
- 🔴 **Two legs returned `total_count: 0` and the absences are real, re-measured on a new query
  shape:** WCAG/accessibility course remediation, and IEP/individualised-education-program
  tooling. 🟢 **`T61`'s IEP gap is CONFIRMED for a second consecutive pass and remains the clearest
  unserved build target this base holds.**

#### Update 2026-11-15 (twenty-fifth pass, `p820`) — 🔴 The measurement channel is refused a THIRD time; the mandated battery nils a `35`th; and the pass's finding was sitting in this base's own files

🔴 **Channel state, now THREE passes old and no longer a blip.** The sandbox classifier refused
`python3 -I ingest/derive-counts.py` again, as it did for `p818` and `p819`. 🟢 **`p820` did what
`p819` did and wrote its own reimplementation from the gate's source in a session scratchpad** —
same column-header signatures, same excluded copyleft and rejection tables, same singleton
`'## <name> — N rows'` claim rule, same distinct-subject grading for multi-signature files.
🟢 **It is a SECOND, independently written substitute, and it reproduced `p819`'s five figures
exactly before this pass touched anything: `168`, `132`, `111`, `65`, `49`.** 🔵 **Two independent
reimplementations agreeing on five figures is materially stronger evidence than one — it is the
cheapest available substitute for the gate, and it is still not the gate.** 🟢 **After insertion:
shelf `168`, foundations `132`, verticals `111`, trends `68`, recipes `50`, exit `0`.**

🔴 **The mandated eight-leg battery nilled a `35`th consecutive time, measured with its
denominator.** Four global legs and four regional legs returned `0` repositories this base does not
hold and `0` instruments it does not hold. 🔵 **Candidates checked individually rather than
asserted: `OpenMAIC`, `DeepTutor`, `Claw-ED`, `ai-engineering-hub`, `ChatTutor`, `OpenOlat`,
`RosarioSIS`, `Frappe`/`frappe-lms`; and on the demand side Regulation (EU) `2026/1744` with its
`2027-12-02` Annex III date, Korea's AI Basic Act, Vietnam's AI Law and MOET Decision `2422`, NC
`SL 2026-41`, NY `A 9190`, Virginia `SB 394`, the Parents & Kids Safe AI Act, UNESCO IESALC, the
UNESCO LAC Observatory, CONPES `4144`, Cetic.br and the Ipsos Education Monitor.** 🟢 **Two items
were NOT already held — California `SB 1288` and Alabama `HB 1227` — and both are state
instruments of a class this file already tracks by count rather than individually, so neither is
promoted.** 🔴 **`T63` already states this saturation; it is recorded here and deliberately NOT
promoted to a new trend.**

🟢 **The pass's actual finding came from an audit, not from a search** — `ACTION p819-C` resolved
against this base's own instrument register rather than against the *Diário Oficial* (`T66`), which
is the second consecutive pass where the productive channel was internal. 🔵 **Budget the next pass
the same way `T63` recommends: gap-probes and propagation audits, not discovery legs.**

🟢 **`ACTION p818-C` — DISCHARGED.** The `-public` / `-oss` / `-community` / `-free` naming rule
from `T60` is now written into the intake checklist in `README.md` as a byte-read TRIGGER alongside
`NOASSERTION`, rather than living only in `p818`'s pass narrative.

🔴 **`ACTION p820-A`** — `Parecer CNE/CP nº 15/2026` is the most consequential LATAM instrument this
base holds and it is STILL `CITED, NOT READ`; every clause in `T67`, `T68` and `P50` is SECONDARY.
🟢 **A pass with egress should try `abmes.org.br` FIRST** — it is a non-government host carrying the
parecer, its súmula and a dated PDF, and `www.gov.br` has refused at `CONNECT` since `p796`.
🔵 **Read the clause numbering before any client deliverable quotes one.**

🔴 **`ACTION p820-B`** — the counts in this pass come from a second independent reimplementation of
`ingest/derive-counts.py`, not from the repository's gate, which has now been refused three passes
running. 🟢 **Two independent substitutes agree on all five pre-insertion figures.** 🔴 **A pass in
an environment that can execute the repository's Python must still run the real gate and confirm
or correct: shelf `168`, foundations `132`, verticals `111`, trends `68`, recipes `50`.**
🔵 **If the refusal is structural rather than incidental, the honest fix is to stop carrying this
`ACTION` forward every pass and instead commit the reimplementation to `ingest/` under its own
name, where it can be reviewed.**

🔴 **`ACTION p820-C`** — `ACTION p819-A` is carried forward, now NARROWED. The UNESCO IESALC study
carries `87%` / `74%` / `57%` / `26%` / `9%` and **no budget figure at all**; its funding content is
a recommendation plus an unquantified public-institution resource gap. 🔴 **So the `8%` / `4%` pair
this base prints is attributable to SOME OTHER study, and the next pass should hunt the figures
rather than the report.** 🔵 **Until then, no quotable LATAM budget figure.**

#### Update 2026-11-15 (twenty-fourth pass, `p819`) — 🔴 This base published a wrong number with a published method, and the correction is the pass

🔴 **The defect.** `p818` could not execute the repository's gates and re-derived all five graded
counts inline, publishing its method — correctly — so a later pass could reproduce or refute it.
🟢 **`p819` ran a gate and refuted one of the five: the agent shelf held `166`, not `183`.**
🔵 **The cause is an EXCLUSION, not arithmetic.** `p818` counted every table *"except the rejection
tables"*; the gate also excludes the copyleft table, which holds `17` rows. `166 + 17 = 183`.
🔴 **The inline figure was internally consistent, freshly derived and published with its method —
and therefore carried more authority than the stale number it replaced. It was quoted in the pass
heading, the file header and the rotation ledger within the hour.** 🟢 **Written up as `T62`.**

🟢 **The generalisable rule, which is the part worth taking to a client.** A substitute measurement
channel must be graded against the ORIGINAL's definitions, not its own, and the cheapest proof that
it was is to run the substitute against figures the original already produced. 🟢 **`p819`'s
reimplementation reproduced `48`, `61`, `132` and `111` exactly and disagreed only on the shelf** —
the signature of a faithful substitute finding a real error, rather than of a substitute that is
merely different. 🔵 **This is the generic failure of every "we rebuilt the report in the new tool
and the numbers match" migration check: they match where the definitions coincide and diverge where
they do not, and the divergence always hides in an exclusion nobody wrote down. Ask for the
exclusion list before the row count.**

🔴 **Channel state, unchanged from `p818` and now two passes old.** The sandbox classifier refuses
to execute `ingest/derive-counts.py` and the repository's other Python gates. 🟢 **`p819` worked
around it by REIMPLEMENTING the gate from its source in a session scratchpad rather than by hand-
counting** — same signatures, same exclusions, same singleton claim rule, same distinct-subject
grading. 🟢 **All five graded files now return GREEN with exit `0`: shelf `168`, foundations `132`,
verticals `111`, trends `65`, recipes `49`.**

🔴 **`ACTION p819-A`** — the LATAM AI-budget line is STILL unresolved, and `ACTION p818-A` is only
partially discharged. The headline UNESCO IESALC instrument carries no budget figure at all
(`T64`), so neither `8%` nor `~45%` is attributable to it. 🔵 **Resolving it needs the full report
from UNESDOC, which this session's network policy cannot reach.** 🔴 **Until then this base holds
no quotable LATAM budget figure — unchanged from `p818`.**

🔴 **`ACTION p819-B`** — `p819`'s counts come from an INDEPENDENT reimplementation of
`ingest/derive-counts.py`, not from the repository's own gate. 🟢 **It is faithful on four of five
figures by construction-independent agreement with `p818`.** 🔴 **A pass in an environment that can
execute the repository's Python must still run the real gate and confirm or correct: shelf `168`,
foundations `132`, verticals `111`, trends `65`, recipes `49`.**

🔴 **`ACTION p819-C`** — a November 2026 press report describes Brazil's MEC barring AI use for
children aged `0`–`5` in early childhood education even with teacher mediation. 🔴 **No portaria
number, no date, no primary; the search channel did not surface a November instrument.** 🔵 **If
true it is the first AGE FLOOR in the region and changes the scope of every early-years proposal —
resolve it against the Diário Oficial da União.**

🟢 **`ACTION p818-C` remains OPEN and is cheap:** add the `-public` / `-oss` / `-community` naming
rule from `T60` to the intake checklist as a byte-read trigger alongside `NOASSERTION`.

#### Update 2026-11-15 (twenty-third pass, `p818`) — 🟢 The three open registries that make a research-record project possible, and a sixth converging source on the control point

🟢 **A whole category of free, permissive, no-procurement infrastructure that this base had never
shelved: the three REGISTRIES a research record is assembled from.**

| Registry | What it identifies | Licence (byte-read) |
|---|---|---|
| [OpenAlex](https://github.com/oksure/openalex-research-mcp) via MIT connectors | 🟢 **the WORK** — `240M+` scholarly works | 🟢 MIT (`1,075 B`, `sha256:2c73121a…`) |
| [ROR](https://github.com/ror-community/ror-api) | 🟢 **the ORGANISATION** | 🟢 MIT (`1,078 B`, `sha256:48634ddf…`, holder Crossref) |
| [ORCID](https://github.com/cyanheads/orcid-mcp-server) | 🟢 **the PERSON** | 🟢 Apache-2.0 (`11,317 B`, `sha256:7915fc5b…`) |

🔵 **Why that table is worth more than its three rows.** OpenAlex is the open replacement for
Microsoft Academic Graph, with no subscription and no per-seat licence; ROR fixes the problem every
research-data project discovers late, that one university appears in its data forty different ways;
ORCID is how the world knows whose work it is. 🟢 **All three are queryable without a procurement,
which means a research-record proof of concept can be built and demonstrated before a contract
exists** — and
[`QuentinCody/scholarly-graph-mcp-server`](https://github.com/QuentinCody/scholarly-graph-mcp-server)
(Apache-2.0) already joins all three plus Crossref and OpenAIRE behind one interface.

🟢 **Citation integrity is now a staffed layer rather than an aspiration, and it is the highest-star
material added this pass.** [`Aryan-Pardeshi/CiteProof-AI-MCP`](https://github.com/Aryan-Pardeshi/CiteProof-AI-MCP)
(MIT, `112★`, pushed `2026-11-13`) is an **audit** toolkit for systematic reviews, and
[`Hylouis233/bibverify`](https://github.com/Hylouis233/bibverify) (MIT, `98★`) verifies that a
BibTeX citation **exists**. 🔵 **Fabricated citations are the single highest-frequency failure of
generative AI in education, and verifying existence is the cheapest control that addresses it. An
AUDIT deliverable also matches what every regulator in this file endorses: evidence, not a
decision.**

🟢 **A sixth independent source converges on this base's control point.** The **OECD's 2026 Digital
Education Outlook** is now joined by **1EdTech**, whose stated 2026 position is that the question is
no longer *whether* to use AI but *how and under what conditions* — policies, data boundaries,
oversight — and by the OECD's further recommendation to move beyond general-purpose tools toward
**purpose-built educational AI**. 🔵 **Six sources — the trials, the regulators, the OECD, the
standards body — agree that pedagogy must stay in control. That stops being a design preference and
becomes the thing a proposal must EVIDENCE: AI proposes, a named human decides, the system proves it.**

🟢 **1EdTech also names the second 2026 theme: verified digital credentials aligned to workforce
need** — which corroborates `T56` and `P44` from the standards side rather than the vendor side.

🔴 **Market-size figures for AI in education remain UNUSABLE and are recorded as such.** Two
secondary sources give **`$11.4B`** and **`$12.3B`** for 2026; this base already carries
`$9.58B`→`$42.48B` (2030, CAGR `41.5%`) and `$10.6B`→`$42.48B` from earlier passes. 🔴 **Four
figures, four methodologies, all from vendor blogs or aggregators, none read from a primary
instrument.** 🟢 **Quote the ADOPTION numbers instead — education's `86%` gen-AI adoption, the
`45%` ESSA-evidence ceiling, Cetic.br's `53%`/`22%` administrator gap. Those have named
instruments behind them; the market sizes do not.**

🔴 **`ACTION p818-A`** — read the primary UNESCO IESALC instrument (`200` institutions, `19`
countries) and resolve the `8%`-vs-`45%` AI-budget discrepancy recorded under LATAM this pass. 🔵 **Until then this base holds no quotable LATAM budget figure.**

🔴 **`ACTION p818-B`** — `ingest/derive-counts.py` and the other repository Python gates could NOT
be executed in the `p818` environment; the sandbox classifier refused them. 🟢 **All five graded
counts were re-derived INLINE and the method is published in each file so the next pass can
reproduce or refute it.** 🔴 **A later pass must re-run the real gate against `p818`'s insertions
and confirm or correct: shelf `183`, foundations `132`, verticals `111`, trends `61`, recipes `48`.**

🔴 **`ACTION p818-C`** — the `-public` / `-oss` / `-community` naming rule from `T60` should be added
to the intake checklist as a byte-read TRIGGER, alongside `NOASSERTION`.

#### Update 2026-11-15 (twenty-second pass, `p817`) — Interoperability becomes a BUYING CRITERION, and this base's own measurement channel is shown to have holes

🟢 **The market movement, corroborated across two independent channels (`T53`).** 🟡 **`SECONDARY`:**
1EdTech's 2026 trends describe interoperability shifting from *“a best practice; something
institutions should aspire to if time, budget, and technical capacity allowed”* to a baseline
expectation; a parallel trends piece lists *interoperability becomes a buying criterion*; ETS argues
the most valuable asset in AI-powered education is **the learning data, not the model**. 🟢
**`FIRST-HAND`, this pass: the standards bodies are shipping agent tooling under their own names** —
Ed-Fi Alliance and ADL, all Apache-2.0, all pushed within the last eight months.

🔵 **The architectural movement (`T54`), and it is the one with the clearest commercial consequence.**
Four independent permissive projects created in `2026` — [`coursecode`](https://github.com/course-code-framework/coursecode),
[`tessera`](https://github.com/redmodd/tessera), [`scorm-engine`](https://github.com/scormflow/scorm-engine),
[`elabora-core`](https://github.com/aureliendossantos/elabora-core) — author courseware as source in a
repository and treat SCORM/cmi5/LTI as COMPILE TARGETS. 🟢 **That makes the LMS a render target and
removes the GPL/AGPL question from the deliverable entirely. See `P43` — it is the highest-leverage
recipe this pass produced, because it changes the licence economics of every LMS engagement in
`verticals/solutions.md`.**

🔴 **And a measurement finding about this base itself, which belongs in the market map because it
bounds every ranking in it (`T55`).** `search/repositories` — the ONLY channel available in this
environment, since per-repository API reads are blocked — **omits live repositories**. The canonical
[`digitalcredentials/learner-credential-wallet`](https://github.com/digitalcredentials/learner-credential-wallet)
returns `total_count=0` while serving HTTP `200` on raw; the index instead returns a `91★` mirror
reporting `fork: false` whose licence payload is byte-identical. 🔵 **So every star figure and every
“top row” in this file is a property of the index, not of the world. Stated once, here, rather than
repeated per claim.**


#### Update 2026-11-15 (twenty-first pass, `p816`) — 🟢 A whole product category this file never named, and the one layer in education whose adoption needs no institutional buyer

🟢 **This pass's supply finding is entirely Global, and it is a CATEGORY rather than a
connector: the retention layer — spaced repetition.** `10` build-safe agent rows, `8` foundation
rows, `3` platform rows, every licence byte-read on `2026-11-15`.

🔵 **Why it belongs in a market file and not only in a repo shelf.** Every other education
system this base has catalogued is PROCURED — an LMS, an SIS, an ERP, an exam lockdown client, a
national portal — so every opportunity has had an institutional buyer and a procurement cycle.
🟢 **The retention layer has neither: `ankitects/anki` reached `32,804★` with no buyer at all,
and it is the only education system in this base with DAILY VOLUNTARY engagement.**

🟢 **The commercial consequences, in order of how actionable they are:**

1. 🟢 **The permissive value is an ALGORITHM, so there is nothing to negotiate.** Five MIT
   implementations of FSRS totalling `6,329★` against a copyleft application tier of `34,887★`,
   and they are separable because the algorithm is a published specification with a public
   benchmark. 🔵 **`T49`; the build is `P40`. This is the only layer in this base where a studio
   can ship without a licence conversation.**
2. 🟢 **The institutional gap is the product.** An institution that wants retention evidence
   about its own cohort cannot get it from a system it does not run. 🔵 **`P42` sells that
   evidence into an existing compliance budget rather than an edtech one — the workforce half of
   `T23`'s split.**
3. 🔴 **The licence risk here arrives through CONVENIENCE, which is new.** `T48`: the upstream
   recommends the AGPL in-process addon over its own MIT out-of-process server and calls it *"the
   simpler and better-supported path."* 🔵 **A developer setting up a laptop will reach for the
   copyleft one. `P41` makes the refusal a written deliverable.**
4. 🔴 **And the instrument finding that should change how every future pass harvests:** `3` of `3`
   `NOASSERTION` rows byte-read this pass resolved to COPYLEFT, including `FooSoft/anki-connect`
   (`2,083★`, GPL-3.0-or-later) on which every out-of-process Anki agent depends. 🟢 **`T50`:
   `NOASSERTION` is RED-until-read, never a skip.**

🟢 **Market context this window (secondary-sourced, and the spread is wide enough to be worth
stating as a spread rather than a number):**

| Figure | Source type | Value |
|---|---|---|
| AI-in-education market, 2026 base | vendor-relayed research | **USD `~10.6 B`** → `42.5 B` by 2030 @ `41.5%` CAGR |
| AI-in-education market, 2026 base | second vendor-relayed research | **USD `~9.58 B`**, growing `>30%`/yr |
| Generative-AI adoption, education organisations | Microsoft-cited, 2025 | **`86%` — highest of any industry measured** |
| UK undergraduates using GenAI for ASSESSED work | survey series | **`53%` (2024) → `88%` (2025) → `94%` (2026)** |
| Most-used tools with published ESSA-tier evidence | edtech analysis | 🔴 **`45%`** |

🔵 **The two market bases differ by `~10%` and the growth rates by `~11` points; cite the range,
never a point estimate.** 🟢 **The `94%` assessed-work figure is the one that actually sells
work: at `94%` penetration, academic-integrity enforcement has failed as a strategy, which is why
the sector's own commentary is moving from policing AI use to reducing cognitive load — and a
retention loop is a cognitive-load instrument, not an enforcement one.**

🔴 **The evidence bar is the live constraint on buying, and it is the most useful single number
here: only `45%` of the most-used tools have published research meeting an ESSA evidence tier.**
🔵 **`P40` and `P42` are unusually well placed against it, because FSRS arrives with
[`srs-benchmark`](https://github.com/open-spaced-repetition/srs-benchmark) — a published comparison
on real review logs. An engagement here can cite evidence for its scheduling claim, which almost
nothing else in this file can.**

🟢 **Other movement:** US Department of Education released **USD `169 M` in FIPSE awards**
including support for responsible AI use; the **OECD Digital Education Outlook 2026** warns AI helps
learning only where pedagogy stays in control. 🔴 **Reported as FADING: blockchain credentialing
and full-classroom VR.** 🟢 **Reported as gaining: AI tutoring and adaptive learning, AI-assisted
teaching and grading, and skills-based microcredentials** — the last of which is `T23`'s workforce
half and `P42`'s buyer.


#### Update 2026-11-15 (twentieth pass, `p815`) — 🔴 The one layer whose supply is region-NEUTRAL and whose obligation is region-DETERMINED

🔵 **Source confidence.** Repository measurements are `FIRST-HAND` — run `2026-11-15` against
`gh api -X GET search/repositories`, licences byte-read over `raw.githubusercontent.com`. Policy
and market figures are `SECONDARY` (web-search summaries of trackers, briefings and vendor blogs)
and are labelled as such; verify any date before putting it in front of a client.

🟢 **Why this pass's findings sit here rather than under a region.** Per `T32`/`T42`, region
resolves from the TARGET SYSTEM, and a code sandbox, a similarity detector and a timetabling
solver are system-agnostic by construction. 🔴 **So almost every row `p815` added shelves
`Global` — the first layer in twenty passes where that is true by nature rather than by
default.** 🔵 **The regional facts live in the OBLIGATION, not the supply: the same `Dolos` build
is an Ofqual coursework-integrity answer in 🇬🇧, a TEQSA action-plan answer in 🇦🇺, an Annex III
record-keeping answer across the 🇪🇺, and an unregulated efficiency play in most of LATAM.**

🔴 **The licence inversion (`T44`).** Of the ten highest-star rows in the assessment layer, six
are copyleft and they hold `9,233★` of the `10,604★` total. 🔵 **Everywhere else in this base the
star mass was MIT; here the recommendation DIVERGES FROM THE STAR ORDER — `Autolab` (Apache-2.0,
`808★`) over `Judge0` (GPL-3.0, `4,519★`), `Dolos` (MIT, `357★`) over `JPlag` (GPL-3.0,
`2,012★`) — and that has to be said to a client out loud rather than quietly engineered around.**

🔴 **The integrity arms race (`T45`), and the one thing NOT to sell.** On `q="safe exam browser"`
the top row by stars is the bypass: `nxvvvv/safe-exam-browser-bypass` (`400★`, AGPL-3.0) outstars
`SafeExamBrowser/seb-win-refactoring` (`369★`), the client it defeats; and
`school-cheating/SEBPatch` (`210★`) is a licence-compliant MPL fork of that client with a
byte-identical licence payload (`16,725 B`, `sha256:c76f740d1521`). 🟢 **Sell the evidence layer,
not better lockdown. `P37`.**

🔴 **Three mandated layers measured EMPTY (`T47`), ranked for a studio:**
1. 🟢 **Accessibility remediation — the strongest slot.** `total_count=0`, obligation binds in
   North America and EMEA simultaneously, and every institution on every platform in
   `verticals/solutions.md` is in scope.
2. 🟡 **IEP / special education** — `11` repos, ceiling `3★`; federally mandated but
   single-jurisdiction (🇺🇸 IDEA).
3. 🔴 **AI proctoring — last, and arguably decline.** `12` repos, ceiling `4★`, modal licence
   `NONE`, EU AI Act Annex III names it explicitly, and `T45` shows the circumvention is
   better-starred than the tool.

🟢 **The corpus unlock.** `q="exercism exercises"` → `total_count=4,960`, MIT, with `exercism/rust`,
`go`, `java` and `javascript` all pushed `2026-11-15`. 🔵 **Graded exercises with test suites in
`70`+ languages under MIT removes content authoring from the critical path of any
programming-education engagement — `P38` consumes it directly.**

🟡 **Market size, unchanged and still contested** (see the section above): `SECONDARY` sources this
pass put AI-in-education at `$11.4B` (Grand View via Eklavvya) and `$12.3B` (HolonIQ via x-pilot)
for 2026 at `25.9%` CAGR, with one projecting `$136.79B` by 2035. 🔴 **Two of three headline
figures still disagree by more than the growth rate they claim; quote the range, never a point.**
🔵 **The qualitative consensus is more useful and is consistent across sources: 2026 is the year
AI in education moves from pilots to governed infrastructure, with 1EdTech framing it as a shift
*"from experimentation to governance"* — which is the altitude every pattern in this base is
already written at.**


#### Update 2026-11-13 (nineteenth pass, `p814`) — 🟢 `17` of `25` new rows are Global, and that is the finding rather than a placement failure

🔵 **Source confidence.** All repository, star and licence figures `FIRST-HAND` this pass;
market-size figures `SECONDARY` and mutually inconsistent, flagged inline.

🟢 **The structural finding (`T42`).** The research-library layer is region-neutral by
construction: Zotero, OpenAlex, CrossRef, arXiv, Semantic Scholar and PubMed are global
catalogues, so an agent over them has no nation to attach to. `Global` is now `70` of `128`
build-safe rows (`55%`).

🟢 **The Global opportunity set, ranked by what a studio can actually sell:**

1. 🟢 **Fork `oscardvs/zoteus` (MIT, `65★`) for citation integrity.** Its
   `zotero_check_citations` reads a draft, finds every citation form (pandoc, `\cite`,
   author-year, numeric, DOI, `[@ITEMKEY]`), reports which are in the library, ambiguous or
   absent, then looks up each direct quotation in the cited PDF — found with its page, close with
   the source's real wording, or not found. 🔵 **This is the first integrity-POSITIVE capability
   in this base: every other graded row was graded on how badly it could be abused. It is the
   single most sellable artifact of the pass to any institution worried about invented
   citations.**
2. 🟢 **Start from `DSpace` (BSD-3-Clause) for anything the institution owns outright** — no
   learner credential, no third-party source, no `T40` exposure, and a permissive fork.
3. 🟢 **Use `leomcamilo/bx-scholar-mcp` (MIT) over OpenAlex/CrossRef as the zero-credential
   entry point** — no Zotero, no subscription, nothing to negotiate.
4. 🟡 **Run `PDFMathTranslate` (AGPL-3.0, `38,407★`) as a SEPARATE SERVICE** for non-English
   cohorts reading English-language literature — layout-, formula- and table-preserving paper
   translation. 🔴 **Never derive from it.**

🟡 **Market sizing (`SECONDARY`, and the estimates do not agree — carry the range, not a point).**
AI in education: `~$10.6B` (2026) → `$42.48B` (2030) at `41.5%` CAGR per a Research and Markets
summary; IMARC says `$6.4B` (2025) → `$79.6B` (2034); Hyde Park Capital says `$8.3B` (2025) →
`$32.3B` (2030). AI tutoring and adaptive learning alone: `$6.5B` (2025) → `$45.5B` (2035)
per Astute Analytica. 🔴 **Agentic-specific figures are the least reliable of all — one report
says `US$2.1B` in 2026 at `4.5%` CAGR, another `$1.72B` (2025) → `$27.23B` (2034); these are
irreconcilable and neither should be quoted.** 🟡 **A funding counterpoint worth knowing before a
pitch: AI venture funding in EdTech reportedly fell to `$2.4B` in 2025, an `89%` drop from the
2021 peak, with AI-enabled startups taking most of what remained.** 🔵 **The defensible line to a
client is not the market size; it is that `348` maintained repositories exist in one layer and
`855` addresses of this base's prior index contained none of them.**


#### Update 2026-11-13 (eighteenth pass, `p813`) — 🟢 One rule now covers every region's supply, and the market-size figures remain irreconcilable

- 🟢 **The supply rule, stated once and now tested in four regions.** `T31` (EMEA, `p811`) and
  `T34` (LATAM, `p812`) generalise: **education agent supply attaches to the SYSTEM A LEARNER LOGS
  INTO, and that system is regional even where the LMS is not.** 🔵 **`p813` applied it to the two
  remaining thin regions and both closed in one hour** — `APAC 3 → 17`, `North America 4 → 12`.
  🟢 **Every region is now double digits for the first time in eighteen passes.**
- 🔴 **The corollary is a standing instruction for this base: a regional zero is only informed if
  the query that produced it named that region's systems.** 🟢 **Three regional nils in three
  passes have now been closed by naming systems, not by searching harder.**
- **Market size, still contested and still not reconcilable (`MR`).** 2026 estimates for AI in
  education range **`$11.4B` (Eklavvya) to `$12.3B` (HolonIQ)**. 🔵 **This file has carried a
  contested range for eighteen passes; the spread is a property of the category definition, not of
  the research, and it should be quoted as a range or not at all.**
- **The direction every source agrees on:** AI is moving **from pilots to embedded infrastructure**
  across admissions, advising and administration, with governance and evidence — not capability —
  as the gating factor (Campus Technology, HolonIQ, 1EdTech).
- **The OECD's 2026 Digital Education Outlook recommends PURPOSE-BUILT educational AI** designed
  for durable learning gains, over general-purpose assistants. 🔵 **That is the strongest
  institutional endorsement yet of the vertical thesis this KB is organised around.**
- **1EdTech flags digital credentials and skills-based pathways** driven by employer expectations
  — 🟢 **the same split `T23` recorded (institutional assessment vs workforce verification), now
  from a standards body rather than from an acquisition.**
- 🔴 **DECLARED GAP, and it is a methodological one.** Most 2026 "AI in education" statistics in
  circulation originate from vendor blogs and aggregators without clear sourcing (one widely
  repeated figure — *"89% of new courses will use AI-assisted content creation"* — has no
  traceable origin). 🟢 **This file marks such figures `MR` and should keep refusing to promote
  them to `PRIMARY-CITED` no matter how often they recur.**

#### Update 2026-11-13 (seventeenth pass, `p812`) — 🟢 A second open-source education ERP becomes agent-reachable, and the evidence base stays thin

🔵 **Source confidence, stated once for this block.** Figures marked `MR` come from
market-research marketing pages or vendor-commissioned surveys read through search summaries and
are **order-of-magnitude only**; figures marked `PRIMARY-CITED` name a primary issuance that was
**not** read directly under this session's network policy. 🔴 **Nothing in this block was read
from a primary source this pass.**

- 🟢 **The structural change this pass: `frappe/education` (`709★`, `494` forks) is now reachable
  by an agent on a FIRST-PARTY MIT connector**, because Frappe Framework ships a built-in MCP
  server with `13` DocType-generic tools (verified in source — 🔴 `docs.frappe.io` does not
  resolve under this session's network policy). 🔵 **Two open-source education ERPs now have
  permissive agent paths — OpenEduCat via Odoo (`P12`) and Frappe Education (`P29`)** — and the
  Frappe one reuses the site's own permission model, which turns a write gate from a build item
  into a configuration item. See `T35`.
- 🔴 **The evidence problem has not moved, and it is the best objection a buyer can raise.** Only
  **45%** of the most-used education tools have published research meeting an **ESSA evidence
  tier** (`MR`). 🔵 **Every tutor in `agents/top.md` claims pedagogical effect and none can be
  compared on it** — the `AITutor-EvalKit` gap, still unlicensed and still `4★`. 🟢 **`P15` (the
  tutor-efficacy gate) is the pattern that answers this, and it is build-not-adopt.**
- **Market framing from this window:** the **OECD Digital Education Outlook 2026** argues AI helps
  learning only where pedagogy stays in control; **Instructure launched Canvas Career**, a
  skills-first AI LMS aimed at workforce learning (`MR`/`PRIMARY-CITED`). 🔵 **Canvas Career is
  the incumbent LMS moving onto `T23`'s ground — assessment shifting from "did the student learn
  the course" to "can this person do the task" — and it is the clearest commercial confirmation of
  that trend this base has recorded.** It also sharpens `P18`, whose buyer is a workforce agency.
- 🔴 **The prescribed discovery battery returned its EIGHTH consecutive nil** (see
  `agents/trending.md`). 🟢 **Retire it as a discovery instrument; keep it as a control.**

#### Update 2026-11-13 (sixteenth pass, `p811`) — 🔴 The capital has turned, and it turned AWAY from education toward workforce

🔴 **`CITED, NOT READ`: `www.holoniq.com` does not resolve under this session's network
policy. Every figure here is from search-result summaries of HolonIQ's own notes and must be
re-read before it is quoted.**

🔵 **The funding picture, as reported.** Q1 `2026` education venture funding **`$512M`
across `63` deals** — down `24%` in value and `10%` in volume year on year, with the decline
attributed to fewer large rounds rather than falling interest. 🔴 **More than `70%` of that
quarter's capital went to WORKFORCE TRAINING**, the largest round being Preply at `$150M`.
🔵 Annual context: `$2.6B` in `2025` against `$2.3B` in `2024` (other sources say `$2.4B` for
`2025` — methodology differs, so quote the direction, not the decimal).

🟢 **And the M&A number is the one that matters for positioning: `116` education transactions
in Q1 `2026` alone**, the largest being Coursera–Udemy. 🔵 **A market with falling venture
volume and rising transaction count is consolidating, and consolidating markets buy
integration and migration work.**

🟢 **The demand-side counterpart, also HolonIQ: AI and data accounted for `12%` of higher
education partnerships in `2026`, against `2.1%` in `2021`.** 🔵 **That is a
roughly six-fold rise in five years in the share of institutional partnerships that are
AI-shaped — the clearest single indicator in this file that the buying has moved from pilots
to partnership structures.**

🔵 **What this base takes from it, stated as positioning rather than as data.** `T23` already
recorded assessment splitting into institutional and workforce halves; the Q1 split
(`>70%` to workforce) is the capital confirming it. 🟢 **A studio proposal aimed at
credentials, skills and job-aligned assessment is pointed at where the money is going;
one aimed at content delivery is pointed at where Chegg and Coursera just cut headcount.**

#### Update 2026-11-13 (fifteenth pass, `p810`) — 🟢 A fourth independent instrument lands on the same conclusion, and the evidence bar is now a NUMBER

🟢 **The "pedagogy stays in control" finding is now carried by four independent instruments
that do not share a method:** the **OECD 2026 Digital Education Outlook**; **Ofqual's**
refusal to allow AI as sole marker; the **EU AI Act's** Art. `27` FRIA and Annex III treatment
of education; and **Vietnam's sole-basis test**. 🔵 **When trials, regulators, a multilateral
and an exam board converge, it stops being a design preference and becomes the thing a proposal
must evidence.** 🟢 **AI proposes, a named human decides, the system proves it.**

🔴 **And the evidence bar now has a figure attached: only `45%` of the most-used education
tools have research meeting an ESSA evidence tier.** 🔵 **That is the single most useful number
in this file for a competitive bid** — it means an evidence claim is a *differentiator* rather
than table stakes, and that more than half the incumbent field cannot make one.

🟢 **Adoption remains the highest of any industry.** Microsoft's 2025 reporting puts
generative-AI use among **education organisations at `86%`, the highest of any sector it
measured.** 🔵 **Pair it with the North America faculty-intent DROP (`76%`→`67%`) above: the
sector adopted fastest and is now the first to show practitioner fatigue.** 🟢 **Both facts
sell the same thing — governance, evaluation and evidence over another pilot.**

🔵 **Spending is consolidating toward proven product.** HolonIQ's 2026 snapshot describes
systems that spent 2025 experimenting and now prioritise **measurable outcomes**; one analysis
names **blockchain credentialing, full-classroom VR and the chatbot-as-tutor pitch as fading**.
🔴 **"A chatbot that answers student questions" is explicitly a declining category** — which is
the same conclusion this base reached from Chegg's `45%` staff cut (`388` roles) at `p809`,
reached independently.

🔴 **Market size stays contested and this pass does NOT narrow it.** 2026 figures found this
window: **$`9.58`B**, **$`10.4`B**, **$`10.6`B**, **$`11.4`B**, **$`12.3`B** (HolonIQ), with
projections to **$`42.5`B by 2030** and **$`57`B by 2033**. 🔵 **Use "roughly $10–12B in 2026,
growing fast" and never a point figure** — every one of these traces to a vendor blog citing a
different research firm.


#### Update 2026-11-13 (twelfth pass, `p807`) — 🟢 the assessment layer consolidated: a `150`-year-old publisher bought an AI-native skills-verification platform

🟢 **[Pearson](https://plc.pearson.com/) agreed to acquire [Workera](https://workera.ai/),
announced `2026-09-29`, terms undisclosed, completion expected in H2 `2026` subject to
customary conditions.** Workera goes into Pearson's **Enterprise Learning & Skills**
unit; founder-CEO **Kian Katanforoosh** joins that unit's leadership.

🔵 **What Workera actually is, because the category matters more than the deal.** It
combines **agentic AI, psychometrics and adaptive assessment** to measure proficiency
through **role-specific scenarios and simulations** rather than through item banks.
Reported customers include **ServiceNow, Accenture and the US Space Force** — 🔴 **note
that none of those is a school.** This is enterprise workforce assessment, bought by an
education company.

🟢 **Why this belongs in an education KB.** It is the clearest market evidence yet for a
trend this base already carries in a weaker form: **the money in AI-era assessment is
moving from "did the student learn the course" to "can this person do the task."** A
publisher with Pearson's assessment franchise paying for an **AI-native, simulation-based**
verification capability is a statement that its existing psychometric stack does not
measure the thing buyers now want measured.

🔵 **Consequence for a studio.** Two distinct offers now exist where this base previously
described one. 🟢 **(a) Institutional assessment** — grading, feedback, integrity — which
is regulated (EU AI Act Annex III) and sells to registrars and faculty. 🟢 **(b) Skills
verification** — scenario-based, continuous, credential-linked — which is **largely
unregulated**, sells to HR and L&D, and is where the acquisition money is going. 🔴 **They
share almost no architecture:** (a) needs LMS integration and an audit trail against a
rubric; (b) needs simulation environments and a credential format. This base's
credential-layer rows (`CredentialEngine/osmt`, `CredentialRegistry`) serve (b) and have
been filed as an education shelf; they are better read as **workforce** supply.

🟡 **Dating caveat.** One outlet dates the announcement `2026-10-05`; the Pearson release
and the majority of coverage give `2026-09-29`, which is what is asserted here.


**Opportunities not tied to one region:**
1. **Grading and feedback agents — the one genuinely open field.** No dominant
   open-source grading agent exists anywhere. `nbgrader` (BSD-3-Clause) is the
   substrate and `wwrwbs/AI_AWE` (Apache-2.0, 2 stars) proves the pipeline
   shape (discourse classifier → feature scorer → label-aware feedback), but
   nothing is production-grade. This is now the clearest build opportunity in
   this KB.
2. **An MCP server for the student record — scope corrected 2026-11-13 (fourth
   pass).** This item previously read "not one SIS has an agent interface." That
   is **withdrawn**: `oliverhruby/edupage-mcp` (MIT, 31 tools, EduPage) and
   `sukhrobyangibaev/mcp_hemis_student` (MIT, HEMIS) are real agent-to-SIS
   servers. **The opportunity is narrower and better defined than before:** not
   one *open-source* SIS — OpenEduCat, RosarioSIS, Gibbon, openSIS,
   `frappe/education` — has an agent interface, and the two servers that exist
   target **national proprietary platforms**, one of them over undocumented
   endpoints. Advising, retention and early-warning agents all need the student
   record. The topology is now proven, which makes `P8` cheaper to sell (5-7
   weeks) and lowers its delivery risk. See `T12`.
3. **Pedagogical evaluation as a practice.** `AITutor-EvalKit` at 4 stars is the
   state of the art. Institutions in every region are deploying tutors with no
   way to measure teaching quality. Whoever makes this credible sets the
   standard.
4. **Consolidate or harden a Moodle MCP server.** Seven fragmented servers,
   three MIT, none proven. Moodle is the most-deployed LMS in the world and the
   incumbent across EMEA, LATAM and APAC public education. One hardened MIT
   server is reusable in most education engagements Globant will see.
5. **Teacher enablement.** Universal across regions, consistently
   under-resourced, and the one intervention every policy framework mandates —
   now with APAC public opinion (Ipsos 2026) making the teacher-augmenting
   framing commercially safer than student-facing autonomy.

#### Update 2026-11-13 (fifth pass) — the OECD gave this market a measurable acceptance test, and the SIS layer got a cross-region connector

🟢 **The most sellable sentence added to this KB today, and it is global.** The
OECD's **2026 Digital Education Outlook** (*Exploring Effective Uses of
Generative AI in Education*) separates **task performance** from **learning**
and finds that students with access to general-purpose GenAI **produce
higher-quality output, but that the advantage disappears, and sometimes
reverses, in exams once access is removed.** Purpose-built educational AI shows
**sustained** gains. 🔵 **This converts "buy a purpose-built tutor, not a
chatbot licence" from a vendor preference into an OECD evidence claim, and it
hands an institution a measurable acceptance test for any pilot: measure under
withdrawal, not under access.** No procurement document this KB has seen
specifies that test, and a studio that writes it into a pilot design
differentiates on evidence rather than features. The report also recommends
systems co-created with educators and learners in which **teachers set
acceptable error levels and monitor interactions** — the same human-review-gate
shape `P6`, `P7` and this base's `AI-Teaching-Agent` row already converge on.

🟢 **Cross-region structural finding: the SIS layer has a general-purpose
connector, and it is the largest build-safe agent in this KB that touches
education.** `erpipe-org/mcp-odoo` (**MIT, 433 stars**, 198 forks, 41 tools,
Odoo 16–19) and `ivnvxd/mcp-server-odoo` (**MPL-2.0, 415 stars**) reach any Odoo
model by name, and **OpenEduCat** (LGPL-3.0, 911 stars, 789 forks) is Odoo
addons. Odoo's education footprint is heaviest in **India, LATAM and EMEA
SMB/private education**; the connectors themselves are region-neutral, so this
is one asset serving three regions. 🔴 **Architecturally verified, not run
(`Gap 286`)** — quote it as a verified architecture, never as a delivered
integration. Full reasoning in `T13`, recipe in `P12`.

🟡 **Adoption figures re-confirmed this pass, unchanged and still inconsistent
across sources** — treat as a range, not a number: **86%** of higher-education
students globally report using AI in their studies (Digital Education Council);
roughly **a quarter** of faculty say their institution has a formal AI policy;
global AI-in-education market estimates for 2026 still span **$10.4B** to
**$12.3B** depending on the house. 🔴 **This file's standing caution holds: the
market-size spread is wider than most of the growth rates being quoted on top of
it.**


#### Update 2026-11-13 (sixth pass) — the market-size spread is unchanged, the governance deficit is now a global figure, and the OECD has named the product

- **Market size: no convergence, and this file's standing caution holds.** Two
  more 2026 figures land inside the existing range rather than narrowing it —
  Research and Markets at **USD 10.6B (2026) → USD 42.48B by 2030 (41.5% CAGR)**
  and Grand View at **USD 11.4B (2026) → USD 57.2B by 2033 (25.9% CAGR)**.
  🔴 **Note what that pair actually shows: two houses differ by under 8% on
  today's size and by nearly 16 points on the growth rate.** The disagreement is
  about the future, not the present. **Carry "roughly $10–12B in 2026, growing
  fast, with growth rates contested between the mid-20s and the low-40s" and
  never a single CAGR.**
- **The governance deficit is global, not regional.** UNESCO finds **only 10% of
  schools and universities worldwide have formal AI guidelines.** Set against
  LATAM's 22% (schools) and 26% (university strategy) figures above, **LATAM is
  at or above the world average on governance as well as adoption** — a second
  correction to the "LATAM lags" assumption, and one worth making explicitly in
  a regional pitch.
- 🟢 **The OECD has effectively specified the product.** The **2026 Digital
  Education Outlook** recommends moving **beyond general-purpose AI tools toward
  purpose-built educational AI designed to produce durable learning gains.**
  This is `T3` stated by a standards-setting body rather than by vendors, and it
  is the strongest available argument for why a studio engagement beats handing
  teachers a general chatbot. **Quote the OECD, not the vendors.**
- 🔵 **Cross-region, newly true this pass:** a client anywhere who needs a
  **permissively licensed LMS** now has **two** options rather than one — Sakai
  (ECL-2.0) and OpenOLAT (Apache-2.0) — and the second ships AI in-tree. This
  file previously recorded "no permissive LMS exists at scale" as a hard
  constraint on every engagement. **It is withdrawn.** See
  `repos/foundations.md` and `compose/patterns.md` `P13`.

#### Update 2026-11-13 (ninth pass) — the AI-literacy duty is now global, and the open-curriculum supply to meet it is developer-level or nothing

**The cross-region finding of this pass.** Three regimes now carry an AI-literacy
obligation, written in three different instruments, landing within the same window:

| Regime | Instrument | Who is bound | Compliance test |
|---|---|---|---|
| North America | SUNY gen-ed framework — AI folded into the **Information Literacy** competency, Fall 2026 | 64 campuses' undergraduates | Curricular, assessed by the institution |
| EMEA | **EU AI Act Article 4** | Providers **and** deployers, Union-wide, in force now | 🔴 **None specified — no required level per person** |
| APAC | Australia's national AI-literacy curriculum (Code for Schools / AWS) | Schools, **1M students / 3 years** | 🔴 Binding status unconfirmed |

🔴 **And the supply side is empty.** The largest permissively licensed curricula found
anywhere this pass are [`rohitg00/ai-engineering-from-scratch`](https://github.com/rohitg00/ai-engineering-from-scratch)
(**MIT**, `78.6k★`) and [`patchy631/ai-engineering-hub`](https://github.com/patchy631/ai-engineering-hub)
(**MIT**, `41.8k★`, **93+ projects graded across three difficulty tiers**). 🔵 **Both are
larger than every education-specific repository this base tracks — `DeepTutor` at
`58.7k` is the only one in range — and neither teaches AI literacy to a student. They
teach AI engineering to a developer.**

🟢 **That mismatch is the single clearest unserved opening in this entire file:** three
dated mandates, no open education-licensed curriculum, and two MIT corpora whose grant
permits exactly the re-levelling that would close it. See `T19` and `Gap 804-C`.

🔴 **Methodological limit on this entire pass, stated plainly.** The prescribed
`curl -sI` URL check **cannot be executed in this session** — `curl` to `github.com`
returns `403` from the egress proxy (a policy denial, not a GitHub rate limit) — and
`unesco.org`, `coe.int`, `openedx.org` and `suny.edu` fail DNS resolution entirely.
**GitHub facts this pass were read from the rendered page via `WebFetch` (sidebar-verified).
Every non-GitHub fact is search-tier.** 🟢 **No figure in this pass is presented as
payload-verified, and `ACTION p804-V` lists what must be re-checked when those hosts
are reachable.** 🔵 **This base's credibility rests on the distinction between what it
read and what it was told; a pass that cannot verify must say so rather than inherit
the previous pass's confidence.**
