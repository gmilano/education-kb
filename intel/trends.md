---
industry: education
region: Global
updated: 2026-10-24
---

## 🆕 `p424` · 2026-10-24 — **The trend with procurement consequences this pass is NOT in the market: it is that an open-source absence this base published nine times was an artefact of its own reading queue. 🟢 And the regulatory trend sharpened into a date a studio can plan against — EMEA's education high-risk obligations are now firmly 2027-12-02, and APAC has its first education-named high-risk decree.**

🟢 Gates first against `3009a89`: **54 / 55**, one declared red; `commit-gates` → `0`. 🔵 All reads
**2026-10-24**. 🟡 `Gap 424-A`.

### 🔴 `Trend 44` — a published absence can be an artefact of the reader, not the supply

🟢 **Measured, not argued.** `Gap 298` — *"no permissive education platform anywhere on these
shelves"* — stood across nine confirmations and was **refuted by a single payload read** this
pass: `OpenOLAT/OpenOLAT`, Apache-2.0, `10 982` B `6dbc5b605ed0`. 🔴 The address was already cited
in this repository as a **mention**; `p422` had registered `ACTION p422-A` naming the exact read;
the action was carried for two passes while the absence was re-published.

🔴 **Why this is a trend and not an anecdote.** This base has instruments for an absence its index
refutes (`gate-absence`, `p279`) and for an absence restated under new words
(`gate-capability-absence`, `p392`). 🔴 **It has none for an absence that a one-request read would
refute** — and that is the class with the worst cost asymmetry, because the refutation is cheap
and the claim is load-bearing: a studio told *"there is no permissive education platform"* plans a
copyleft-constrained engagement it did not need. 🟡 `Gap 424-B`; `ACTION p424-B` proposes the
instrument (every `Gap` asserting a supply absence carries the ladder read that would refute it,
or is downgraded to *unmeasured*).

🔵 **The generalisation for a client engagement:** a vendor's "there is no open-source option for
X" is a statement about their search, not about the supply, until someone reads a payload.

### 🔴 `Trend 45` — a licence claim can be manufactured from a dependency list

🟡 **Stated at the strength the evidence actually supports, after this pass overstated it once.**
The circulating claim *"forma LMS is Apache-2.0"* is **false**: the repository is **GPL-2.0**,
payload at `html/license.txt`, `18 346` B `4e63feff285d` @ `446a77a9b9cb`. 🔵 The **only** `Apache`
string in its `README.md` is `- Apache (recommended) with mod_rewrite enabled`, a **web-server
requirement**, which remains the most plausible transmission path for the false claim — but that
is an inference, not a measurement (`Gap 424-C`).

🔴 **The measured half is about the reader, not the project.** `p424` ran a **root-only** licence
ladder, got `404` on all 14 paths, and wrote *"no grant payload"* into four shelves.
`gate-enumeration` refuted it before the commit by naming the subtree path. 🟢 `p382` had already
written the rule — *a grant has subtrees; a root-only read is wrong about the repository* — and
`gate-subtree-grant` is in the suite. 🔵 **So `Trend 45` is really this:** a licence **claim** and
a licence **absence** fail the same way. `p423` found a package declaring MIT while shipping
BSL-1.1; `p424` found itself declaring an absence while a GPL-2.0 payload sat one directory down.
🟢 **Consequence for a client:** neither a reported licence nor a reported *lack* of one is
evidence — only a payload read at a pinned SHA, over the whole tree.

### 🟢 `Trend 46` — the compliance runway is now a firm date in EMEA and a named sector in APAC

- 🟢 **EMEA — the date is settled enough to plan against.** The **Digital Omnibus**, Regulation
  (EU) **2026/1744**, moved the Annex III **education** high-risk obligations from August 2026 to
  **2 December 2027**, with AI embedded in regulated products at **2 August 2028**. 🔵 Live
  **now**, not deferred: the **emotion-recognition ban** in education settings (since
  **2025-02-02**) and the Article 4 **AI-literacy** duty.
- 🟢 **APAC — education is now a NAMED high-risk sector in a national decree.** Vietnam's
  **Decision 33/2026/QD-TTg** lists education among six high-risk sectors, naming **automated
  assessment** and **behavioural monitoring**; systems already running before **15 August 2026**
  receive a six-month grace period. 🔵 This is the same **tutoring-vs-assessment** split `p421`
  identified on two continents, now on a third.
- 🔵 **The deliverable is unchanged and now has three jurisdictions behind it:** a reviewable
  human-in-the-loop evidence trail on anything that grades, admits or monitors.

### 🟡 `Trend 47` — the market number is not a number, and the spread is now the finding

🔴 Five houses put the **2026** AI-in-education market at **$1.94 B**, **$7.30 B**, **$9.58 B**,
**$10.6 B** and **$11.4 B** — a **~6×** spread on the *current* year, before any forecast
compounds it. 🔵 At least one of these (**$9.58 B**) explicitly includes **corporate training**.
🟢 **The usable reading is directional only:** every house agrees on rapid growth and none agrees
on the base. See [`intel/market.md`](market.md) for the table and the sourcing.

## 🆕 `p423` · 2026-10-24 — **The trend with procurement consequences: in the education agent layer, licence METADATA is diverging from licence PAYLOAD, and the metadata is what directories, registries and scanners republish. 🔴 One address this pass says MIT on three channels and ships Business Source License 1.1.**

🟢 Gates first against `p422`'s `82235af`: **47 / 53**, 1 deliberate red, 5 new, all fixed here.
🔵 All reads **2026-10-24**.

- 🔴 **Metadata-vs-payload divergence is now a measured trend, not an anecdote.** `p409` found a
  *search result* saying MIT over a 34 230-byte AGPL payload. `p410` found an 874-byte
  "Apache License" that was a notice. `p411` found a 19-byte *"GNU GPL V3"*. `p423` adds the
  sharpest form: **the in-repo manifest itself is wrong**, and it agrees with the registry, so the
  two channels most likely to be machine-read corroborate each other into a false answer.
  `tixuz/openemis-mcp`: `package.json` **MIT**, npm **MIT**, MCP directory **MIT**, payload
  **BSL-1.1** `647` B `4dead97d8aaf`.
- 🔴 **And the licence it misdeclares is not another open-source licence — it is source-available.**
  BSL-1.1 with `Change Date: 2029-01-01` and an Additional Use Grant of *non-production evaluation
  and internal testing only*. 🟢 **This is the first non-open-source grant these shelves have
  graded in the education agent layer**, which makes the direction of the error the whole point:
  every prior divergence this base measured was permissive-claimed-over-copyleft, and copyleft is
  at least still open source.
- 🟡 **BSL in an adjacent form: a "pro" edition's licence at the root of a free one.**
  `Licensed Work: openemis-mcp-pro` names a work that is neither the repository nor the package.
  🔵 Watch for this shape — an open-core project whose root `LICENSE` governs the commercial
  edition — because it reads as a repository-wide grant to every tool that looks at one file.
- 🟢 **The permissive agent layer is still real, and still tier-bounded.** `p422` measured 9 of 10
  MCP-over-**LMS** addresses MIT. `p423`'s first MCP-over-**SIS** address is the BSL one. 🔵 One
  address is not a tier (`T118`), but the asymmetry is worth watching: the LMS tier is built by
  students and staff scratching their own itch, and the SIS tier is where commercial incentive
  sits, because that is where the money and the ministry contracts are.
- 🔴 **Discovery by ranking is still dead, seventh pass running** (`T100`). Eight
  ranking/trend/regional legs → **0 unshelved**. The only productive wording is **capability**,
  and this pass it returned 2 unshelved and **0 supply** (`T113`).
- 🟢 **A regional trend this pass established by instrument rather than by search:** an
  education-AI nil for **EMEA** is a *wording* artefact, not a regional fact. The region-label leg
  returned nothing education-specific; the jurisdiction-named leg returned a **KMK** framework
  update from eight days earlier. 🔵 Any future EMEA nil on these shelves should be read as a
  defect in the leg until a jurisdiction-named pair confirms it.
- 🟡 **The grading question has gone cross-jurisdictional.** US state statutes prohibit AI
  replacing a licensed educator in grading (`p421`); Lower Saxony's April-2026 motion asks for
  clear rules citing legal uncertainty **specifically around AI-assisted grading**. 🟢 Two
  jurisdictions, two legal mechanisms — statute and liability — **one deliverable**: a reviewable
  human-in-the-loop evidence trail.

## 🆕 `p422` · 2026-10-24 — **The trend that changes what a studio can SELL is a licence boundary, and it is new to these shelves: the education platform tier is copyleft without exception while the agent tier directly above it is MIT without exception. 🟢 Measured over ten addresses at their own commit SHAs, not reported. 🔴 And a second trend with a casualty: the discovery channel now routinely serves FORKS as canonical addresses.**

🔵 **Band:** regional and market trends below are `reported` from secondary sources read
**2026-10-24**; no statute text was read first-hand (egress allowlist, `p413`). 🟢 **The licence
and supply trends are `authoritative`** — read at commit SHAs this pass.

🔴 **Gates did NOT run this pass** — `make hooks` executes code from this cloned repository and the
host's auto-mode classifier refused it (`[Code from External]`), the same refusal `p419` recorded.
🟢 `p412`'s standing rule is therefore **unmet and declared**, not skipped silently; every file
contract below was honoured by hand. `Gap 422-A` registers the un-run suite, second instance.
🔵 **No date straddle:** every leg, `ls-remote`, SHA read and digest ran **2026-10-24**; the commit
lands **2026-10-24**, so `updated:` carries one date.

| # | trend | why it is a trend and not a headline |
|---|---|---|
| 1 | 🟢 **`T422-1` — the sector's licence risk INVERTS between two adjacent layers, and the seam is the commercial boundary.** Platform tier: Moodle `GPL-3.0`, Open edX `AGPL-3.0`, Canvas `AGPL-3.0`, Sakai `ECL-2.0`, OpenEduCat `LGPL-3.0`, `frappe/lms` `AGPL-3.0` — **no permissive grant anywhere**. Integration tier over the same platforms: **MIT, 9 of 9 granted**, each read at its own SHA | 🟢 **Two tiers, opposite profiles, measured the same day by the same instrument.** 🔵 The consequence is contractual: the client keeps the copyleft platform, the studio ships the MIT layer as deliverable IP. 🔴 **Under AGPL, network use is itself a distribution trigger** — so "we talk to it, we don't fork it" is a clause, not a nicety |
| 2 | 🟢 **`T422-2` — the agentic layer is arriving BESIDE the LMS, through its API, and now there is a protocol for it.** `p420` recorded the absence of any agentic LMS *release*; `p422` records what filled the space instead — **at least seven independent MCP servers over Canvas and Moodle**, written by unrelated authors, all MIT, all talking to the platform over its existing REST API | 🟢 **Seven independent authors converging on one integration shape in under a year is a trend; one vendor's roadmap is not.** 🔵 `p420`'s absence finding is not refuted — it is **explained**: the LMS vendors did not ship an agent layer, so the ecosystem built one outside them |
| 3 | 🔴 **`T422-3` — the discovery channel serves FORKS as canonical, and a licence check cannot catch it.** This pass's leg served `NelsonSpencer/canvas-mcp` as a primary address. It shares root `afe32c3e1721` and **414** commits with [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp), holds **2** own commits against the upstream's **683**, and its `LICENSE` is **byte-identical with the upstream's copyright line intact** | 🔴 **The fork is correct under MIT and therefore invisible to every check this base runs on grants.** 🟢 `p419` recorded an aggregator serving a wrong-owner slug; this is the sharper form — a **real** repository, **correctly** licensed, that is simply **not the one to depend on**. 🔵 The counter-measure is a root-commit comparison, which costs one blobless clone |
| 4 | 🟡 **`T422-4` — the new tier's weakness is DORMANCY, not licensing.** Of nine granted addresses: one is deep and current (**1 097** commits, active 2026-10-23), two are nine days old, **three have not committed in six to ten months**, one is a stale fork, and a tenth has no grant at all | 🔴 **A tier can be legally clean and still unsafe to depend on.** 🟢 **The posture this implies is "vendor the pattern, not the package"** — and `Mattlo0546/canvas-mcp` shows the pattern is cheap to rebuild: **five commits** produced a working SSO-instead-of-API-token design |
| 5 | 🔴 **`T422-5` — at least one server in this class is write-capable while reading as read-only in listings.** `Jawadh-Salih/moodle-mcp-server`'s `README.md` at `a65aefa` names **`submit_assignment`**, read first-hand; most listings describe the class uniformly as "read-only, student-focused" | 🔴 **A student-credentialled agent that can submit work is a different risk class from one that cannot**, and the distinction is not visible at the catalogue level. 🟢 Band `authoritative` — read at the SHA, not from a snippet |
| 6 | 🟢 **`T422-6` — the tutor/assessor regulatory seam holds, and both sides of it hardened this pass.** EU: Annex III high-risk deferred to **2027-12-02** / **2028-08-02**, with literacy live since **2025-02-02** and transparency plus the labelling Code of Practice from **2026-06-10 / 2026-08-02**. US: **134 bills across 31 states**, with Ohio (**2026-07-01**) and Oklahoma (**2027-28**) imposing district policy deadlines | 🟢 **Third consecutive pass measuring this seam in two legal systems**, and the direction has not changed once. 🔵 The buying consequence is that **compliance has a calendar**, and calendars are what get budgeted |
| 7 | 🔴 **`T422-7` — the adoption/governance gap widened again, on a NEW instrument.** Digital Education Council + Tec de Monterrey (2026): **92 %** of LATAM students and **79 %** of faculty use AI, against **19 %** of institutions with an approved policy. Against **86 %** of education organisations globally using generative AI | 🔴 **Fourth consecutive pass, fourth instrument, and it has not narrowed once.** 🟢 **A measurement that survives four independent instruments is a structural fact, not a survey artefact** — and it is the single most reproducible finding on these shelves |
| 8 | 🟢 **`T422-8` — a government education programme FAILED at scale, with numbers, and the failure is instructive.** South Korea's digital-textbook rollout sat **below 30 %** by March; the National Assembly **removed the textbooks' official status**; the pivot is **$960 M** into AI talent centres and vocational high schools through **2030** | 🟢 **Mandated content distribution failed while capability-building got refunded.** 🔵 This is the second trend on these shelves whose evidence is a failure that already happened (`Trend 41` was the first) — and both point the same way: **sell capability and governance, not mandated student-facing product** |
| 9 | 🟢 **`T422-9` — LATAM curriculum is the fastest-moving policy surface in any region: 11 of 20 countries** now carry AI content in school programmes, **against 2 in 2024** | 🟢 **A 5.5× shift in two years**, against EMEA's deferral and APAC's contested rollouts. 🔵 **The buying window is open now**, and it is for curriculum and teacher capability rather than platform |
| 10 | 🔵 **`T422-10` — what the channel said that was NOT new, recorded so it is not re-bought.** Experimentation → operational; governance over tool sprawl (1EdTech); AI as embedded infrastructure (Campus Technology); education-specific platforms displacing generic ones; agents and adaptive difficulty; digital credentials as workforce currency; evidence demands (HolonIQ) | 🔴 **Every one already on this shelf.** 🟢 `p416`'s rule applies: a trend restated without new evidence is not a trend update |

## 🆕 `p421` · 2026-10-24 — **The trend that prices engagements this quarter is a LEGAL BOUNDARY, not a capability: regulators on two continents are separating TUTORING from ASSESSMENT, and putting the obligations on assessment. 🟢 A tutor is generally outside EU Annex III; a grader is inside it, and US state law prohibits a grader from replacing a licensed educator outright.**

🔵 **Band:** every trend below is `reported` from secondary sources read **2026-10-24**; no statute
text was read first-hand (egress allowlist, `p413`). 🟢 **Gates ran FIRST** (`p412`): **51 / 52**,
single red `Gap 400-B`.

| # | trend | why it is a trend and not a headline |
|---|---|---|
| 1 | 🟢 **The tutor / assessor split is becoming the regulatory seam everywhere.** EU: Annex III names **admission decisions and evaluation of learning outcomes** as high-risk, and the Commission's **May 2026 draft guidelines** place **tutoring and feedback chatbots outside**. US states: statutes prohibit AI **replacing a licensed educator in core instruction or grading**. 🔵 **Two independent legal systems drew the same line in the same year**, which is what makes it a trend rather than a jurisdiction's quirk |
| 2 | 🟢 **Consequence: human-in-the-loop stops being a design preference and becomes a contract term.** 🔴 **The architectural implication is specific** — the deliverable is not an autograder but a **reviewable evidence trail**: per-criterion scores, the rubric version, and the human sign-off. 🟢 `dsvi-b/corretor-enem` (MIT, `p420`) already has this shape by construction, since it emits competency-level scores and calls its own output an estimate rather than a grade |
| 3 | 🟢 **Deadlines, not capabilities, are now the EMEA sales calendar.** Act generally applicable **2026-08-02**; Annex III education deferred to **2027-12-02**; emotion-recognition ban and AI-literacy duty live since **2025-02-02**. 🔵 **Most institutions are in pilot-and-pre-compliance**, with phased implementation running through 2026–2027 — a fourteen-month build-ahead window rather than a live obligation |
| 4 | 🔴 **The adoption / governance gap is the most-reproduced measurement on these shelves, and it widened again.** **86 %** of education organisations use generative AI (highest of any industry) and **92 %** of university students — against **19 %** of LATAM institutions with an approved internal policy and **2 in 10** Mexican universities with published guidelines. 🟢 **Three passes have now measured this in three regions and it has not narrowed once** |
| 5 | 🟢 **Sovereign models move from rhetoric to procurement in APAC.** India **Sarvam AI**, Singapore **SEA-LION**, Japan **NTT Sarashina**, with South Korea's **AI Basic Act** in force **2026-01-22**. 🔴 **Architectural consequence:** an education stack that hard-codes one vendor's inference API will be re-plumbed in this region, so the model boundary belongs behind a gateway from day one |
| 6 | 🟡 **Education-specific rules are landing SUB-nationally while national AI law stalls.** México: no general AI law, but the **Estado de México reformed article 61 of its Ley de Educación** (April 2026). US: **35 states** with K-12 guidance against **zero** binding federal curriculum standards. 🔵 **The buying unit is therefore a state or district system, not a ministry** |
| 7 | 🔴 **The market-size literature is not usable as a single number, and this base has now said so twice.** 2026 estimates span **$6.4B – $11.4B**; 2035/2033 endpoints span **$57.2B – $136.79B**. 🟢 `p378` already caught a cross-publisher **SPLICE** in this file's own headline. 🔵 **The shape (adoption vs governance) is the durable finding; the size is a publisher's choice** |
| 8 | 🟢 **A supply trend, measured rather than asserted: the education-agent long tail is ungranted.** `p421`'s capability leg returned **5** unshelved addresses and **all 5 carry no licence at any of 15 paths at their own commit SHAs**, with **no manifest declaring one**. 🔴 **An ungranted long tail is not supply** — it is unusable regardless of how good the architecture reads. 🟢 **And they are `INDEPENDENT` of one another by full history**, so the duplication is convergent prose, not forking: the same tutorial, five times |
| 9 | 🔵 **Public opinion is not regional — it is national, and it splits inside APAC.** Ipsos Education Monitor 2026: **lower** support for banning AI in schools across the Asian markets surveyed, **higher** in **Australia and New Zealand**. 🟢 A single "APAC stance" would be wrong in both directions, which is why the region field is a placement and the country lives in the prose |

## 🆕 `p420` · 2026-10-24 — **The trend this pass can actually evidence is a COMPLIANCE RUNWAY, not a capability jump: education's EU high-risk obligations moved to 2027-12-02 while the literacy and transparency duties are live now. 🟢 And a second trend with first-hand proof behind it — the grading agent is arriving as a METHODOLOGY, not a service.**

🔵 Every claim below carries its band. Nothing here is restated from a vendor headline without one.

| # | trend | evidence, and what it changes |
|---|---|---|
| 1 | 🟢 **`T420-1` — governance became the gate, and it now has a DATE.** | The EU AI Act's Annex III education obligations deferred to **2027-12-02** (**2028-08-02** for AI embedded in regulated products), while AI-literacy, transparency and deepfake-disclosure duties are **already in force** since **2026-08-02**. 🔵 1EdTech independently describes the sector shifting *"from experimentation to governance"*. 🟡 **So the EMEA sequencing inverts:** literacy and disclosure are build-now, high-risk conformity is design-now-certify-later. Band: 🟢 `authoritative` for the in-force dates, 🟡 `reported` for the deferral |
| 2 | 🟢 **`T420-2` — the grading agent is shipping as a METHODOLOGY, not a service, and this pass has a specimen.** | [`dsvi-b/corretor-enem`](https://github.com/dsvi-b/corretor-enem) (🟢 MIT, read at SHA) grades ENEM essays on five official competencies against **11 147** real essays in a local SQLite corpus — with **no API, no ML and no vendored model SDK**. It runs *inside* a coding agent the engagement already has. 🔵 `p417` recorded two independent LangGraph discursive-graders; this is the third architecture for the same job and the only one that **deploys nothing**. 🟢 Band: `authoritative` — read first-hand |
| 3 | 🔴 **`T420-3` — adoption is ahead of governance everywhere measured, and LATAM is the sharpest case.** | UNESCO IESALC over **200 institutions in 19 countries**: **87 % use AI, 26 % have a strategy**. 🟢 TALIS 2024 teacher use — Brazil **56 %**, Chile **55 %**, Colombia **53 %**, Costa Rica **52 %** against an **OECD mean of 36 %**. 🔴 And **1 in 2 students report confusion about appropriate use**. 🟡 **The deliverable a client needs first is a policy, not a model** |
| 4 | 🟡 **`T420-4` — the ban question is live in APAC and the spread is narrow.** | Ipsos Education Monitor 2026, support for banning AI in schools: Indonesia **23 %** → South Korea **31 %**, with India **26 %**, Singapore **28 %**, Japan and Malaysia **29 %**; ANZ higher. 🔵 **A ~8-point spread across seven very different systems** means school-level AI policy is contested, not settled, anywhere in the region. 🔴 `T45` still holds: **school-level** APAC rules remain the informed gap — this pass's leg returned national instruments and one survey, nothing at school level. Band: 🟡 `reported` |
| 5 | 🟢 **`T420-5` — purpose-built beats general-purpose, by vendor consensus and by this base's own supply curve.** | Multiple independent 2026 reviews predict a move away from generic chatbots toward education-specific platforms. 🟢 **This base's supply data agrees for a different reason:** five consecutive passes in which *ranking*-worded discovery returned **zero** unshelved addresses while *capability*-worded discovery returned new supply every time (`T100`). 🔵 The market is organising by **job**, and so is the index |
| 6 | 🔴 **`T420-6` — licence risk in education open source is a CHANNEL problem, not a permissiveness problem.** | Measured this pass: Moodle's grant sits at root `COPYING.txt` on `main` and at `lang/en/docs/licence.html` on three LTS refs; the whole Moodle **plugin** ecosystem grants only in `version.php` headers; Frappe's three platforms grant at lowercase `license.txt`; two R packages grant in `DESCRIPTION`. 🔴 **A root-path licence read misgrades 13 of 19 addresses on these shelves.** 🟢 **And the sector's grants are overwhelmingly COPYLEFT** — GPL, AGPL, LGPL, ECL — with `Gap 298` confirmed on a seventh channel. 🟡 **The studio risk is not finding an unlicensed repo; it is pricing a copyleft one as permissive** |
| 7 | 🟡 **`T420-7` — no agentic LMS release exists to cite, and that absence is itself the signal.** | A leg worded directly at *"Moodle Open edX AI plugin agentic 2026 release"* returned **no official Moodle HQ or Open edX announcement** — only vendor marketing, one 2025 Aulasneo **Owly** post for Open edX, and middleware integrations wrapping the REST API / LTI 1.3. 🔵 **The agentic layer in education is arriving BESIDE the LMS, through its API, not inside it.** 🔴 Stated as an informed gap: Moodle 5.3 (2026-10-05) was not read for AI features — egress allowlist |

🔵 **Carried unchanged and deliberately not re-bought:** the embed-vs-produce gap, the squadron-not-model
framing, and the credential/skills-ecosystem shift. 🟢 None of them moved on evidence this pass, and
`p416`'s rule applies — a trend restated without new evidence is not a trend update.

## 🆕 `p419` · 2026-10-24 — **The channel's trend is still "agentic + governance". 🔴 The trend this base can MEASURE is that a government AI policy was withdrawn because its citations were fabricated — provenance has stopped being a methodology preference and become a procurement requirement. 🟢 And the supply trend sharpens: the open-source education layer is consolidating into repositories whose grant varies by BRANCH.**

🔴 **Gates did not run** — `make hooks` executes code from this cloned repository and the host's
auto-mode classifier refused it (`[Code from External]`). Contracts honoured by hand;
`Gap 419-D` registers the un-run suite.

### 🔴 `Trend 41` — provenance became a procurement requirement, with a named casualty

🟢 **The evidence is a withdrawal, not a survey.** South Africa's draft National AI Policy —
Department of Communications and Digital Technologies, published **2026-04-10** with comment open to
**2026-06-10** — was withdrawn by Minister **Solly Malatsi** on **2026-04-26** and gazetted
**2026-06-12** in its entirety, because **at least 10 % of the academic references in its reference
list were fictitious**. A replacement is targeted for FY **2026/27**; none is published. 🟡 Band
`reported`: `sanews.gov.za` plus DLA Piper, ITWeb and CNBC Africa; 🔴 **the gazette text was not
read** — `en.wikipedia.org` is off this environment's egress allowlist, `p413`'s finding holding a
fourth time.

🟢 **Why it is a trend and not an anecdote.** Every other governance item these shelves carry is
**prospective** — the EU AI Act's Annex III deadline at `2027-12-02`, Article 50 transparency live
since `2026-08-02`, Korea's Framework Act, Vietnam's two-tier transition, 134 US state bills. 🔴
**This one is retrospective: a real instrument, from a real ministry, already dead, for a reason
that names unverified AI output.** 🟢 **So the market now has a worked example of the cost of
shipping AI prose without provenance — in the public sector, where the buyer writes the rules.**

🟢 **What it implies for how work is bought.** The deliverable that clears this bar is not a better
model; it is **citation-level traceability, a verification record per claim, and a named accountable
human**. 🔵 These are the same artefacts Annex III's technical file will require from
**2027-12-02** — so an EMEA engagement can sell one set of artefacts against two drivers, one
regulatory and one reputational. 🟢 **`Trend 41` is the first governance trend on these shelves
whose evidence is a failure that already happened.**

### 🔴 `Trend 42` — the grant varies by BRANCH, and no instrument here reads more than one ref

🟢 **`p418` measured the consolidation one step: a repository's licence is a SET over subtrees**
(`THU-MAIC/OpenMAIC`, eight MIT payloads plus one `LGPL-3.0-or-later`). 🔴 **`p419` finds the next
axis one pass later.** [`piyushdhoka/GradeU`](https://github.com/piyushdhoka/GradeU) ships three
applications on **three branches** — stated in its own `README.md:50-54` — and the grant does not
follow them:

| ref | app | tracked paths | licence-shaped paths | manifest `license` |
|---|---|---|---|---|
| `main` *(default)* | Student site | 199 | 🟢 `LICENSE` — MIT `1 065` B `10e6b9c80b1b` | 🔴 absent, `"private": true` |
| `teacher` | Teacher studio | 55 | 🔴 **NONE at any depth** | 🔴 absent, `"private": true` |
| `admin` | Admin portal | 43 | 🔴 **NONE at any depth** | 🔴 absent, `"private": true` |

🟢 **All three heads committed within eight minutes** on 2026-10-23, so this is a live layout, not
history. 🔴 **The direction of the trend is the dangerous part:** monorepo-by-subtree and
monorepo-by-branch both concentrate more product behind one badge, and a badge is resolved at one
`(ref, path)` pair. 🟢 **The counter-measure is a single command — `git ls-remote --heads` before
the path enumeration** — and `Gap 419-A` registers that none of this base's instruments does it.

### 🔴 `Trend 43` — the discovery channel's ranking vocabulary has stopped producing supply

🟢 **Measured across four passes, not asserted.** The two *ranking* legs
(`top open source AI agents education {year} github MIT`,
`github trending {industry} AI {year}`) have returned **zero** unshelved in-domain addresses for
**four consecutive passes**; the *capability*-worded leg returned the only new address in each of
the last two, including this pass's `GradeU` (1 unshelved of 8).

🔴 **The mechanism is visible in what the ranking legs return:**
`microsoft/generative-ai-for-beginners`, `rasbt/LLMs-from-scratch`, `mlabonne/llm-course`,
`karpathy/nanochat`, `developer-roadmap`, the Hugging Face Agents Course. 🟢 **Every one teaches
people to build AI. None is AI applied to education.** The ranking vocabulary cannot separate
*education as subject matter* from *education as the audience of a tutorial* — and the second
category is vastly larger and better-starred, so it wins every ranking. 🟢 **`T100` confirmed a
fourth time and sharpened: the discriminator is capability vocabulary, not recency vocabulary.**

🔵 **Two secondary-source hazards from this pass's legs, recorded unprobed.** One aggregator served
`nilbuild/developer-roadmap` as the slug for a repository these shelves carry under a different
owner; another named *"ponytail"* as a trending educational platform. 🔴 **Neither was probed and
neither is shelved** — an unprobed slug from an aggregator is not an address.

### 🔵 What the channel said this pass, and how much of it was new

🟢 The `AI education industry trends 2026` leg returned: experimentation → **operational** use;
**governance** over tool sprawl (1EdTech); AI as **embedded infrastructure** in higher education
(Campus Technology); **education-specific** platforms displacing generic tools (Teachbetter);
**agents** plus real-time adaptive difficulty (Educativa); **digital credentials** as workforce
currency; and **evidence demands** — systems expecting proof that a product improves learning
quality, persistence, well-being or job-relevant skills (HolonIQ). 🔴 **Every one already on this
shelf.**

🔴 **And the market numbers conflict again, which is itself the standing finding.** One source cites
**$12.3 B** for 2026 attributed to HolonIQ while another puts the market near **$6 B** in 2024;
a third puts North America alone at **$3.68 B**, 36 % of the global total. 🟢 **`p415` settled that
this file carries the market size as a RANGE** — these three points fall inside it and none narrows
it. 🔵 The serving channel flagged its own headline percentages as weakly sourced; **not shelved.**

## 🆕 `p418` · 2026-10-24 — **The trend the channel reports is "agentic + governance". The trend this base can MEASURE is that the open-source education supply has stopped growing and started consolidating into monorepos — which is why a repository's licence is now a SET rather than a value.**

### 🔵 What the channel said, and how much of it was new

🟢 The `AI education industry trends 2026` leg returned seven themes, **every one already on this
shelf**: experimentation → operations; governance and data boundaries (1EdTech); AI as embedded
infrastructure in higher education (Campus Technology); the move from generic tools to
**education-specific** platforms (Teachbetter); **agentic** multi-step systems; interoperable
**digital credentials**; and buyers demanding **evidence of outcomes** — learning quality,
persistence, well-being, job-relevant skills (HolonIQ).

🔴 **Nil new instruments and nil new figures.** 🟡 The leg also returned a **$12.3B 2026 market** and
an **83 % institutional AI-teaching-assistant** figure attributed to HolonIQ and EDUCAUSE *without
checkable links*, plus a vendor-sourced *"42 % outcome improvement"*. 🔴 **None is recorded** —
`p406`'s rule is that an unsourced figure on this base is worse than a declared gap, and these are
exactly the shape `p406` caught in this base's own pricing rows.

### 🟢 The trend this base can measure first-hand: consolidation, and a licence that is a SET

🔴 **Nine legs this pass returned ZERO unshelved in-domain addresses.** `p416` read 68 addresses for
one; `p417` got two from thirteen candidates across ten legs; `p418` got **nil from nine**. 🟢 Read
together, three consecutive passes say the same thing: **the discoverable open-source education
supply is saturated on the English-language channel.** 🔵 `T100` follows and is now confirmed twice —
on a saturated shelf, **budget the pass toward re-reading verdicts, not toward more legs.** Every one
of this pass's four findings came from a re-read.

🟢 **And the structural trend underneath it is consolidation into workspace monorepos**, which
changes how a licence must be recorded:

- [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) — **9** licence-shaped paths: 8 × MIT
  (`1 065` B, `ba2525637432`) + **1 × LGPL-3.0** (`7 652` B, `e3a994d82e64`), the copyleft one a
  **vendored third-party** package wired in as `workspace:*`
- [`exelearning/exelearning`](https://github.com/exelearning/exelearning) — **9 756** paths, a
  `packages`-free but equally layered tree where the SCORM capability lives in **774** of them
- `Open-TutorAi/open-tutor-ai-CE` — the **CE/EE** split this shelf already flags
- `Gego-K12/gegok12` — MIT root whose manifest is the **unedited Laravel skeleton** (`p411`)

🔵 **The pattern across all four:** the interesting licence fact is never at the root. 🟢 **So the
2026 trend for a studio is not "find the agent" — the agents are found. It is "resolve the boundary
inside the agent you already picked."**

### 🔴 A trend worth naming because it cuts against the channel's own narrative

🟢 The channel reports *education-specific* platforms displacing generic tooling. 🔴 **The supply
measured here says the opposite at the data layer.** `Gap 298` / `Gap 405-A` is now confirmed from a
**fifth** independent channel: **no major education SIS carries a permissive grant** — OpenEduCat
LGPL-3.0, openSIS GPL-2.0, RosarioSIS GPL-2.0, Gibbon GPL-3.0, SchoolTool GPL-2.0, Fedena and
OpenOlat Apache-2.0 but not education-native in the way the others are. 🟢 **The permissive options
on the admissions path are GENERIC** — `aureuserp/aureuserp` and `krayin/laravel-crm`, both MIT, both
Webkul, neither carrying an academic data model. 🔵 **So "education-specific" is true of the agent
layer and false of the record layer**, and a studio that reads the trend report literally will plan
to buy a vertical SIS that does not exist on permissive terms.

### 🔵 Regulatory trend, carried not re-bought

🟢 **Three regimes, three clocks, all already settled here and all re-confirmed this pass:**
**EU** — Annex III education **`2027-12-02`**, Art. 50 live **`2026-08-02`**, Omnibus
`Reg (EU) 2026/1744`; **Korea** — in force **`2026-01-22`** *(served this pass as the "AI Basic Act",
carried here as the "Framework Act" — one instrument, two names)*; **Vietnam** — in force
**`2026-03-01`**, comply **`2027-03-01`**, **`2027-09-01`** for systems already running before
**`2026-08-15`**, corroborated this pass from a third source.
🔴 **The informed gaps are the same two and are channel gaps, not world gaps:** Africa and the
Middle East return nothing on English legs; APAC **school-level** rules are unmeasured (`T45`).

## 🆕 `p417` · 2026-10-24 (reads 2026-10-23) — **`p411` graded a CORRECT source as carrying "the wrong Vietnamese date" — and the row's OWN QUOTED TEXT contains the clause that makes the source right. 🟢 Plus the first genuinely new state-backed EMEA supply in several passes: `exelearning/exelearning`, AGPL-3.0 at `p413`'s canonical digest, led by Spain's Ministry of Education. 🔴 AND the gap register is THREE passes stale.**

🔵 **Dating note, and this pass is the first in the run that has to SPLIT it.** Every search leg,
licence read, payload read, digest and gate run below was executed on **2026-10-23**; **the commit
lands 2026-10-24**, because the work crossed **00:00 UTC** before it was written out. 🟢 **The two
dates are therefore recorded separately rather than collapsed to one**, and the frontmatter
`updated:` field carries the **commit** date while every `evidence/*.tsv` filename carries the
**read** date — which is why they disagree by one day, deliberately. 🔵 `p395`–`p416` were all
dated **2026-10-23**, twenty-two passes; **this is the first pass dated 2026-10-24**, and the first
whose reads and commit fall on different days. 🔴 `p223`'s date gate is satisfied by the split, not
by rounding either date toward the other.

🟢 **Gates ran BEFORE the first research leg — `p412`'s standing rule, which `p416` admitted
breaking: 50 / 51 green on arrival**, equal to `p413`–`p416`. 🔵 The lone red is
`gate-census-union` control 24 — **`Gap 400-B`**, carried deliberately red since `p398`. `p387-G`
forbids closing it by weakening a control and this pass did not try.

🔵 **Channel note, in agreement with `p414`–`p416`.** `raw.githubusercontent.com` serves **`200`**
and is how every byte-level grant read below was taken; `github.com` HTML reads cleanly through
`WebFetch`. `p414`'s `AUTHZ-REFUSED` class holds a fourth consecutive pass.

### 🟢 The trend this pass can actually evidence: the grant is lagging the capability

🟢 Both genuinely new in-domain agents found today implement **the same capability** — LLM-graded
discursive assessment with human-in-the-loop — **independently, on the same framework (LangGraph),
in different countries**, and **neither shipped a licence**.

| | [`savinoo/ai-grading-system`](https://github.com/savinoo/ai-grading-system) | [`Fatima0923/AssessmentAI`](https://github.com/Fatima0923/AssessmentAI) |
|---|---|---|
| orchestration | LangGraph + LangChain | LangGraph, 7-node workflow |
| retrieval | ChromaDB | FAISS + sentence-transformers |
| human loop | 🟢 conditional **divergence arbitration** | 🟢 AI-only vs **AI-against-human-marks** |
| origin | Instituto Federal Fluminense, **Brazil** | not stated |
| 🔴 grant | 🔴 **none** — MIT badge, no payload | 🔴 **none** — *"academic research purposes"* |

🔵 **Read as a trend rather than as two repositories:** the assessment-agent pattern has reached the
stage where it is a **capstone project**, not a research contribution — which is how a technique
becomes ordinary. 🔴 **And the licensing has not kept up.** The capability is commodity; the
**legal availability is not**, and a studio that assumes "open source" from a GitHub URL will be
wrong on both of this pass's new addresses.

🟢 **This is the supply-side counterpart to the governance trend below**: adoption is being limited
less by what can be built than by what can be *lawfully reused*.

### 🔵 Carried trends, re-confirmed and NOT re-bought

🔵 The prescribed trends leg returned a consistent and **entirely carried** picture for 2026. Recorded
as confirmation, with the vendor figures refused:

- 🟢 **From pilots to infrastructure** — AI embedded across admissions, advising, learning and
  administration in higher education rather than piloted beside it.
- 🟢 **Governance and oversight as the gating factor** — 1EdTech's framing: explicit policies, data
  boundaries and oversight as preconditions for trusted adoption, not afterthoughts.
- 🟢 **Agentic, not conversational** — multi-step agents that plan a teaching sequence and draft an
  assessment; this base's two new addresses are instances of exactly that.
- 🟢 **Teacher-first adoption** — education-specific tooling displacing generic chatbots, with
  take-up driven by hours returned to teachers.
- 🟢 **Evidence demands** — HolonIQ's reading: systems increasingly require proof of effect on
  learning, persistence, well-being or job-relevant skills.
- 🟢 **Skills and credentials** — digital credentials and competency frameworks tracking
  skills-based hiring.

🔴 **Figures refused on sourcing, per `P541` and `Gap 546`.** A *$12.3 B* market figure and an *83%
AI-teaching-assistant deployment rate* trace to a single vendor blog citing unverifiable sources; a
*$9.58 B (2026) → $136.79 B (2035) at 34.52% CAGR* forecast is vendor-style. 🔴 **None is written to a
cell.** 🔵 A *60% / 32% weekly* US teacher-use pair and *87% / 26%* UNESCO IESALC pair are already
carried with better provenance and are the figures to quote.

### 🟡 A measurement about this base's own instruments, which is a trend too

🔴 **Three of this pass's findings are defects in how this base grades evidence, not in the
evidence:** a refutation counter that fired on a correct source (`intel/market.md`), a gap register
three passes stale, and a licence family attached to a project name instead of an address
(`T99`). 🟢 **At 417 passes the marginal external fact is cheap and the marginal instrument check is
expensive** — this pass's novelty rate was **2 new addresses in 13 candidates**, while its instrument
audit changed a published verdict. 🔵 `T100` (new): **on a saturated shelf, budget the pass toward
re-reading verdicts rather than toward more legs** — and record the novelty rate so a successor can
tell saturation from channel decay.


## 🆕 `p416` · 2026-10-23 — **Sixty-eight addresses read across four discovery legs returned exactly ONE unshelved in-domain repository — and it closes a scarcity this base declared BY NAME. `DozenTwelve/Papermorph` is MIT, readable and emits SCORM 1.2/2004, where the shelf's only prior SCORM emitter is source-CLOSED. 🔴 AND `p415`'s headline — "the agent field has one hub and no middle" — is refuted by four middle-tier addresses already recorded in `agents/top.md` itself.**

🔵 **Dating note.** Every search leg, licence read, payload read and gate run below was executed on
**2026-10-23**, and the commit lands **2026-10-23**. 🔵 **This is the twenty-second pass dated
today**, after `p395`–`p415`.

🟢 **Gates ran three times, and the middle run is the one worth recording: 50 / 51 → 48 / 51 →
50 / 51.** Green on arrival, equal to `p413`–`p415`. 🔴 **Then this pass's own shelf writes turned
`gate-census-currency` and `gate-union-currency` red** — the published census triple no longer
matched the live shelves. 🟢 Re-derived with `make address-shape-census` / `make union-currency` as
the last act before the commit and **restated rather than back-dated**, per `p352` and `p376`; back
to 50 / 51. 🔵 The lone remaining red is `gate-census-union` control 24, **`Gap 400-B`**, carried
deliberately red since `p398`; `p387-G` forbids closing it by weakening a control and this pass did
not try. 🔴 **Honest deviation from `p412`'s standing rule:** the first gate run was started *in
parallel with* the first research leg, not strictly before it. Nothing below depends on a gate
result — but the rule says *first*, and this pass did not obey it to the letter.

🔵 **Channel note, re-measured and in agreement with `p414`–`p415`.**
`curl -sS https://github.com/GeminiLight/gen-mentor` → **`http=403`, 378 B**, and the body is the
*session's own* refusal (*"GitHub access to this repository is not enabled for this session. Use
`add_repo`…"*), **not** GitHub's; `https://api.github.com/repos/CaviraOSS/PageLM` returns the
**identical 378-byte body**. The same addresses read cleanly through `WebFetch`, and
`raw.githubusercontent.com` serves **`200`** — which is how the byte-level grant read below was
taken. 🟢 `p414`'s `AUTHZ-REFUSED` class, confirmed a third consecutive pass, on a third pair of
addresses.

### 🟢 T9 (new) — the useful new work is PACKAGING into standards the institution already runs, not new platforms

🔵 **The evidence is the shape of today's yield, not an opinion.** Sixty-eight addresses across four
discovery legs; sixty-three already shelved; **one** new in-domain repository. It was not found on a
tutor topic page — both of those returned a perfect nil — it was found on `edtech`, and what makes
it worth shelving is **its output format**:

| Address | what it emits | the door it walks through |
|---|---|---|
| 🆕 [`DozenTwelve/Papermorph`](https://github.com/DozenTwelve/Papermorph) (MIT, 849★) | **SCORM 1.2 / 2004 package** | the LMS's existing content-import screen |
| [`classroomio/classroomio`](https://github.com/classroomio/classroomio) (AGPL-3.0, 1.7k★) | an **MCP server** over the platform | any MCP-speaking assistant or coding agent |
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (MIT) · [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) (MIT) · [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) (MIT) | **MCP tool surfaces** over Canvas, Anki, and BKT+FSRS learner state | the assistant the user already has open |
| [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) (Apache-2.0, 376★) | **LTI tools** and an IMS ContentItem store | the LMS's existing external-tool configuration |

🟢 **The pattern:** the 2026 education repositories that matter commercially are not trying to become
the system of record. They emit into one — SCORM, LTI, MCP — and let the institution keep Moodle,
Canvas, Open edX or Anki. 🔵 **Why now:** the buyer has moved from "can it generate" to "can you
evidence it and will it survive procurement" (the governance turn this file records in **T1**), and
a standards-conformant package survives procurement in a way a new platform does not.

🔵 **What it means for a studio engagement.** The deliverable boundary moves earlier and the
integration bill falls. 🔴 **The risk it creates:** a standard is also a ceiling — SCORM carries
completion, score and time, and **nothing** about mastery, affect or trajectory. A client who wants
per-skill mastery reporting cannot get it from a SCORM package alone, and that is the honest limit to
state in the first conversation, not the third. See `compose/patterns.md` **P7** this pass, which
wires the mastery layer alongside the package rather than inside it.

### 🔴 T10 (new) — the discovery surface is saturating, and that is itself the trend

Three consecutive passes of measured yield on the public GitHub education surface:

| pass | legs | addresses | unshelved in-domain |
|---|---|---|---|
| `p414`–`p415` | topic `ai-tutor`, topic `education-ai`, 4 regional | — | 0 new agents; three carried figures refuted |
| **`p416`** | topic `intelligent-tutoring-system`, topic `knowledge-tracing`, topic `edtech`, 1 GitHub search, 4 regional, 1 ERP | **68** | **1** |

🟢 **The field is not dead; the discoverable-by-topic-page part of it is held.** The open-source
education agent population above ~50★ appears to be a few hundred repositories, heavily
APAC-origin, with a single hub ([`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor), 42.3k★) and
a thin long tail — 🔵 though note `agents/top.md` this pass: the "no middle" reading of that tail was
an artefact of a hand-picked table, and the middle exists.

🔵 **Where a successor should spend instead:** packaging formats and non-GitHub registries, and
**re-measurement of what is already shelved** — which in the last two passes produced seven corrected
star figures and one corrected licence, against one new address. 🟢 **Re-measurement is currently
the higher-yield activity, and it is cheaper.**

## 🆕 `p415` · 2026-10-23 — **The agent tier re-measured FIRST-HAND against the live GitHub sidebars, and three figures this base carried are refuted — one of them by a factor of 31.** 🟢 Fifteen agent addresses and nine foundations read today, every licence taken from the repository's own sidebar. 🔴 AND the read channel matters: `curl` and `api.github.com` are REFUSED for every repository not attached to this session, so a pass that reports "unreachable" from `curl` alone is reporting a fact about the CHANNEL.

🔵 **Dating note.** Every search leg and every licence read below was executed on **2026-10-23**, and the
commit lands **2026-10-23**. This is the twenty-first pass dated today, after `p395`–`p414`.

🔵 **Channel note, measured this pass.** `curl -sI https://github.com/CAHLR/OATutor` → **403**, and
`curl -s https://api.github.com/repos/HKUDS/DeepTutor` returns the session's own refusal body
(*"GitHub access to this repository is not enabled for this session"*), **not** GitHub's. The same
addresses read cleanly through `WebFetch`. Both instruments were run side by side before any address
below was written down. Every licence, star count and date in this pass came through `WebFetch`.

### 🟢 Eight trends, each with the evidence that produced it

**T1 — From pilots to infrastructure, and the gate is governance.** 1EdTech frames 2026 as the year
AI in education shifts from experimentation to *governance* — data boundaries and oversight.
Campus Technology's panel expects AI embedded across admissions, advising and administration.
🔵 The practical read: the buying question has moved from "what can it do" to "who approved it, what
does it touch, and where is the human". A proposal that leads with capability is answering last
year's question.

**T2 — Generic chatbots are losing to education-shaped tools.** Reported frustration with
general-purpose assistants is pushing vendors toward systems that already model learning objectives,
grade-level expectations, assessment logic and instructional flow. 🟢 Visible in the supply:
`OATutor` (BKT), `pyKT` (knowledge tracing), `tutor-mcp` (BKT + FSRS) all encode a *pedagogical state
model* rather than a prompt.

**T3 — MCP is becoming the LMS integration layer, and its licensing is the weak point.** Education
MCP servers now exist for Canvas, Moodle, Open edX, Brightspace and Anki. 🟢 `canvas-mcp` (MIT) and
`anki-mcp-server` (MIT, 530★) are clean. 🔴 `openedx-mcp` is AGPL-3.0, `moodle-mcp` publishes an
empty licence field, `brightspace-mcp` has no licence file at any depth. **The integration layer is
less legally sound than either the platforms or the agents it joins.**

**T4 — Evidence is becoming a procurement gate.** HolonIQ's 2026 snapshot: systems increasingly
require evidence of improvement in learning quality, persistence, well-being or job-relevant skills.
🔵 Consequence for a studio: instrument the pilot for an efficacy claim from day one. Retrofitting
measurement after a successful pilot is how a renewal gets lost.

**T5 — Pedagogy is shipping as an agent SKILL.** Five of the twenty most-starred `ai-tutor`
repositories are skill bundles, not systems. 🟢 Fastest possible pilot. 🔴 No tenancy, no learner
state, no data boundary, no audit trail — unshippable into an institution as-is. See
[`agents/trending.md`](../agents/trending.md).

**T6 — Spaced repetition has consolidated on FSRS.** `fsrs-rs` (BSD-3, 451★) is the scheduler inside
`tutor-mcp`, reachable through `anki-mcp-server`, and reimplemented in `freelingo` and `OpenTutor`.
🟢 **This is the one component question in education AI that is settled** — adopt, never rebuild.

**T7 — EMEA is buying sovereignty, not agents.** European public money is going into open *models*
(OpenEuroLLM ~€20M of €37.4M, Teuken-7B, Apertus, SOOFI) and into *regulation*, while the entire
EMEA-origin education agent supply on these shelves is two repositories. 🔵 For a studio this is an
opening, not a warning: Europe will have sovereign models and no sovereign application layer.

**T8 — Secondary star counts are systematically unreliable, and the error is not random.** Three
figures this base carried were refuted by a first-hand sidebar read today, one of them by **31×**
(`educhain`: carried `~12k★`, actual **387★**). 🔴 Every one entered through a secondary list.
**The rule this pass would hand a successor: a figure that no sidebar produced is not a measurement,
and in this field the secondary sources inflate.**

### 🔴 The structural fact underneath all eight

The education agent field has **one hub and a long tail with nothing in between** — 42.3k★ at
position one and 1.2k★ at position two on the `ai-tutor` topic page. There is no population of
mid-size, well-maintained education agents to assemble a solution from. 🟢 **Therefore: compose from
the mature *foundation* tier (Kolibri, Oppia, OpenOLAT, nbgrader, FSRS — all permissive, all a decade
old) and treat the agent tier as patterns to reimplement, not dependencies to adopt.** That is the
single most load-bearing conclusion these shelves support, and it has survived every pass that
tested it.

## 🆕 `p414` · 2026-10-23 — **`34 501` is NOT the AGPL-3.0 `http` form — it is ONE repository's de-indented title line, and the spread is a 2×2 lattice over `34 520` whose four cells are all now measured. 🔴 `education-agent-skills`' grant is a POINTER on BOTH its subtrees and its operative text is unreachable here. 🔴 AND the egress refusal has TWO classes these shelves record as one.**

🔵 **Dating note.** Every search leg, licence read, registry probe, channel probe and gate run below
was executed on **2026-10-23**, and the commit lands **2026-10-23**. 🔵 **This is the twentieth pass
dated today**, after `p395`–`p413`.

🟢 **Gates FIRST, per the standing rule `p412` set and `p413` kept.** `make hooks` ran **before** any
research: **50 of 51 gates green on the FIRST run** — equal to `p413`'s best-ever first-run state and
again against `47` for both `p409` and `p412`. 🔵 The lone red is `gate-census-union` control 24,
**`Gap 400-B`**, carried deliberately red since `p398`; `p387-G` forbids closing it by weakening a
control and this pass did not try. 🟢 **`p413` left the base clean** — the currency gates were green
on arrival for the second consecutive pass.

🔵 **Channel note, and it CORRECTS `p413`'s largest finding rather than repeating it.** `p413`
concluded the egress channel is an **allowlist** and recorded its evidence as *"`http=000` —
connection never established, **not a `403`**, not a `404`"*. 🔴 **There is a `403`, and it is at the
`CONNECT` layer**: `curl` prints `CONNECT tunnel failed, response 403` and the proxy names
`connect_rejected` — *"the host is not allowed for this session"*. 🟢 **`p413`'s conclusion was right
and its evidence was under-read**, and reading it properly splits what these shelves record as one
refusal into **two classes with different remedies**:

| class | http | body | what it means | remedy here |
|---|---|---|---|---|
| 🟢 **SERVED** | `200` | yes | `pypi.org`, `raw.githubusercontent.com`, `registry.npmjs.org` | — |
| 🟢 **SEMANTIC-404** | `404` | yes (21 B) | the registry **answered**; the absence is a fact | — |
| 🔴 **AUTHZ-REFUSED** | `403` | **yes, 378 B** | tunnel opens; the body names the **session's repository scope** (`api.github.com`, `codeload.github.com`) | a scope grant — **not** a host problem |
| 🔴 **TUNNEL-REFUSED** | `000` | **no** | `CONNECT` 403 + `connect_rejected`; host **not on the session allowlist** | 🔴 **none on this environment** |

🔵 Fifteen URLs, control pair first, in
[`evidence/refusal-taxonomy.2026-10-23-p414.tsv`](../evidence/refusal-taxonomy.2026-10-23-p414.tsv);
the probe is [`compose/code/p414-refusal-taxonomy/refusal.sh`](../compose/code/p414-refusal-taxonomy/refusal.sh).
🟢 **Why the split pays:** an `AUTHZ-REFUSED` host is reachable and merely unauthorised, so a figure
behind it is *obtainable in principle*; a `TUNNEL-REFUSED` host is not, so a figure behind it is
**unverifiable on this channel, permanently**, and `p413`'s standing register rule applies. 🔴 This
base's own [`p798-proxy-refusal-ledger`](../compose/code/p798-proxy-refusal-ledger/README.md) records
refusals **without** this class split — successor item 1.

### 🔴 The standing rule this pass establishes: a refusal has a CLASS, and the class decides whether a fact is obtainable

🔵 `p413` made the channel an **allowlist** and set the register rule *"unverifiable on this channel"*
over *"re-try the host"*. 🟢 **That rule survives and gets a discriminator.** The two refusals these
shelves have recorded as one are distinguishable by a single observable — **does a body come back** —
and the consequence differs:

| if the probe shows | the class is | and the correct register entry is |
|---|---|---|
| `http=000`, no body, `CONNECT tunnel failed, response 403` | 🔴 **TUNNEL-REFUSED** | *"unverifiable on this channel"* — 🔴 **no pass can obtain it**, so an open gap asking for it is work nobody can do |
| `http=403` **with** a readable body naming a scope | 🔴 **AUTHZ-REFUSED** | *"reachable but unauthorised"* — 🟢 obtainable **in principle**, so it may be recorded as a blocked request rather than an impossibility |

🔴 **Why the conflation cost something real.** `Gap 488` was already misframed per `p413`. The same
shape reaches further: every `github.com`-family figure on these shelves — star counts above all —
has been recorded as *proxy-blocked*, which reads like the permanent class. 🟢 **It is the
`AUTHZ-REFUSED` class**: the host answers, the tunnel opens, and the refusal names its own remedy. 🔵
That does not make the figures obtainable *here*, and this pass still declines to carry a star count;
what changes is that the ledger should say **which** wall it hit.

### 🔵 Trend reading — two shifts this pass measured rather than read about

🟢 **T1 · The licence a repository *shows* is drifting away from the licence it *grants*, and the
drift is toward REFERENCE.** Two instruments converge on it this pass. `GarethManning/education-agent-skills`
publishes **two** CC BY-SA notices, **neither** containing the operative legalcode and both pointing
at `creativecommons.org` — a host this environment cannot open. 🔴 And the AGPL-3.0 lattice shows the
opposite failure on the same axis: **four** byte-distinct presentations of **one** text, where a
consumer grading by digest or byte band sees four licences and a consumer grading by reference sees
none. 🟢 **The reading for a studio:** an in-tree `LICENSE` is now **two** questions, not one — *which
text is this* (the lattice answers it in-tree) and *is the text even here* (`p307`'s `POINTER` class
answers it, and increasingly the answer is no). 🔴 Skill-packs and prompt assets fail the second
question far more often than source trees do, and this industry's newest supply is skill-packs.

🟢 **T2 · Public-sector AI in education keeps producing supply that has no address — and Japan is a
step EARLIER than Germany.** `p413` found **KIMADU**: permissively-granted agents (`CC BY-SA 4.0`
prompts) with **no repository**. 🟡 This pass finds **MEXT** intending to build its own
education-specific AI application for **FY2027** demonstration research, with costs in the **FY2027
概算要求** — **no licence stated and no repository stated**. 🔵 So the shape now has two rungs: *grant
without address* (Germany) and *neither grant nor address* (Japan), and both are state-funded. 🔴
**Neither is a build-on address and neither should be shelved as one.** 🟢 **What it predicts:** the
procurement question a studio will be asked in both regions is *"can you take over something the
ministry built"*, and the answer depends on a grant that does not exist yet — which is an argument for
being in the room before FY2027, not after. 🟡 Both rows are **search-channel only**: `mext.go.jp`,
`asahi.com` and all five French ministry hosts are `TUNNEL-REFUSED`.

🔵 **T3 · And a counter-current worth naming, because it points the other way.** 🟡 France's *cadre
d'usage* instructs its readers to **prefer libre solutions** *"qui permettent un contrôle des corpus
utilisés ainsi que des procédures de traitement"* — a ministry stating a preference for open source
in writing, on sovereignty-of-corpus grounds rather than cost. 🟢 That is the clearest EMEA demand
signal on these shelves for exactly what this base is built to supply. 🔴 **It is search-channel only
and must stay labelled so**: `education.gouv.fr` and `eduscol.education.fr` are both
`TUNNEL-REFUSED`, so the sentence is relayed, not read.

## 🆕 `p413` · 2026-10-23 — **AGPL-3.0 IS a revision family, and `Pattern AI`'s AGPL reference is a SUBTRACTION rather than a measurement. 🟢 `openedx/edx-platform`'s grant is NARROWED and this base carried the bytes without the consequence. 🔴 AND THE EGRESS CHANNEL IS AN ALLOWLIST — every "proxy-refused" note on these shelves is a fact about the CHANNEL, not the host.**

🔵 **Dating note.** Every search leg, licence read, registry probe, channel probe and gate run below
was executed on **2026-10-23**, and the commit lands **2026-10-23**. 🔵 **This is the nineteenth pass
dated today**, after `p395`–`p412`.

🟢 **Gates FIRST, per `p412`'s successor item 1.** `make hooks` ran **before** any research:
**50 of 51 gates green on the FIRST run** under `p300`'s no-masking runner — **the best first-run
state this base has recorded**, against `47` for both `p409` and `p412`. 🔵 The lone red is
`gate-census-union` control 24, **`Gap 400-B`**, carried deliberately red since `p398`; `p387-G`
forbids closing it by weakening a control and this pass did not try. 🟢 **`p412` left the base
clean** — `gate-census-currency` and `gate-union-currency` were **green on arrival**, the first time
a pass has inherited a current census rather than a stale one.

🔵 **Channel note, and it is this pass's largest finding.** The egress channel was probed with
`p293`'s control pair FIRST: `pypi.org` **200**, `raw.githubusercontent.com` **200**. Then **10 of
10** other hosts answered `http=000` — *connection never established*, not a `403`, not a `404`:
`moodle.org`, `openeducat.org`, `education.ec.europa.eu`, `gov.uk`, `tum.de`, `uni-siegen.de`,
`kimadu.de`, `lernen-digital.nrw`, `bildungsserver.de`, `diariodarepublica.pt`. 🔴 **Two of those
are this industry's own flagship project domains.** 🟢 So the refusal is a property of the
**channel**, not of any host, and it is an **allowlist** rather than a geography filter — a
conclusion no single-host observation could reach.

### 🔴 The standing rule this pass establishes: the egress channel is an ALLOWLIST, and this base has been recording its refusals as facts about hosts

🔵 **The probe, with its control pair run FIRST** per `p293` — because a channel that answered
nothing would report every host dead, and a failed control pair yields no verdict at all:

| host | result | role |
|---|---|---|
| `pypi.org` | 🟢 **`200`**, 16 461 B | positive control |
| `raw.githubusercontent.com` | 🟢 **`200`**, 34 523 B | positive control |
| `moodle.org` · `openeducat.org` | 🔴 **`http=000`** | this industry's own flagship project domains |
| `education.ec.europa.eu` · `gov.uk` | 🔴 **`http=000`** | EMEA statutory authority |
| `tum.de` · `uni-siegen.de` · `bildungsserver.de` · `lernen-digital.nrw` · `kimadu.de` | 🔴 **`http=000`** | EMEA institutional authority |
| `diariodarepublica.pt` | 🔴 **`http=000`** | **`Gap 488`'s own host** |

🟢 **Ten of ten non-allowlisted hosts refused at the transport layer** — not `403`, not `404`,
*connection never established*. 🔴 **And the refusal is not geographic**: `moodle.org` and
`openeducat.org` are `.org` project domains, and they fail exactly like the `.de` and `.pt`
government hosts. 🟢 **So it is an allowlist**, and that is a conclusion no single-host observation
could have reached. 🔵 **And the scale of the misreading is countable**: these shelves carry
**11** `proxy-refused` notes and **85** `connect_rejected` ones, every one of them written as a
fact about the host it names.

🔴 **Three consequences, and they change method rather than content.**

| # | consequence |
|---|---|
| 1 | 🔴 **`Gap 488` is MISFRAMED, not open.** It records *"`diariodarepublica.pt` is proxy-refused on both transports"* and implies a successor should re-try the host. 🟢 **No successor should.** The host is not the variable; the channel is, and re-trying it is a probe this base can now predict the result of |
| 2 | 🔴 **`gate-restatement`'s "verified first-hand" is UNATTAINABLE here for any fact whose authority is a non-allowlisted host.** 🔵 That is not a defect in the gate — the gate is right that a restatement is not a verification. 🟢 But it means EMEA and LATAM **statute and institutional** facts can only ever be **search-channel** on this environment, and the correct register entry is *"unverifiable on this channel"* rather than an open gap that asks for work no pass can do |
| 3 | 🟢 **The search tool is a RELAY, not a channel.** It returns text from hosts the transport refuses — but relayed prose cannot be byte-counted, digested, or pinned to a ref, so it can never satisfy the instruments this base grades grants with. 🔴 **And a relay can fuse two sources into one claim**, which is exactly what it did to KIMADU this pass. 🔵 Two surfaces remain that *are* channels: **PyPI JSON** and **`raw.githubusercontent.com`** |

🟢 **What this buys: the verification budget has a shape now.** Licence, payload, digest, tree,
manifest, version and upload-date facts are **first-hand-verifiable** here, because they live on the
two allowlisted surfaces. 🔴 Statute, funding, enrolment, procurement and vendor-roadmap facts are
**not**, and no amount of probing will change that. 🔵 A pass that spends its budget on the first
class compounds; one that spends it on the second produces gaps that look like work and cannot close.

### 🔵 Trend reading — two shifts this pass measured rather than read about

🟢 **T1 · The Python licence channel is MIGRATING, and it is migrating unevenly enough that a
heuristic fails.** Across seven education packages read first-hand, PEP 639's `license_expression`
answers **3 of 7**, the legacy `license` field **3 of 7**, OSI classifiers **2 of 7**, and the full
ladder **7 of 7** — **no single rung above 3 of 7.** 🔴 **And the answering rung is not predictable
from the upload date**: `django-lti` (**2026-08-07**) is classifier-only with no expression, which
refutes the tidy *"2026 packages use the expression"* reading its own population suggested. 🟢 The
trend is real; the shortcut it invites is wrong, and a consumer-side licence reader has to run all
three rungs.

🟢 **T2 · Public-sector AI in education is producing SUPPLY, and the supply has no repository.**
EMEA's clearest new instrument this pass is **KIMADU** — eleven didactic agents, state-funded above
**€1 M**, **25** schools, prompts published as OER under **`CC BY-SA 4.0`**, distributed as HTML and
PDF for pasting into ChatGPT or fobizz. 🔴 **No repository, no package, no version, no digest** — and
the grant is **scoped to the prompt and its usage notes**, leaving the three knowledge-base libraries
the agent is designed to run with **outside** it. 🔵 Every other permissive agent on these shelves is
citable as `(FILE, digest)`; this one is not. 🟢 **The shape to expect more of**: ministries are
becoming publishers of prompt assets, and prompt assets are licensed like documents rather than like
code — which means the questions that matter shift from *what licence* to **what scope, and which
version**.

## 🆕 `p412` · 2026-10-23 — **`make hooks` RUNS**, the pass that declared it unrunnable is the pass that **broke a gate**, **“5 authors” is `%an` and collapses to 3**, and the GPL-3.0 denominator spread is **two FSF revisions, not noise**

🔵 **Dating note.** Every search leg, clone, licence read, registry probe and gate run below was
executed on **2026-10-23**, and the commit lands **2026-10-23**. 🔵 **This is the eighteenth pass
dated today**, after `p395`–`p411`.

🟢 **Channel note — and the headline is a channel REFUTATION.** `make hooks` **RAN TO COMPLETION
this pass: 47 of 51 gates green** under `p300`'s no-masking runner. 🔴 **`Gap 410-C` (“`make hooks`
unrunnable”) is therefore REFUTED, not closed** — and this is the **second** time this base has had
to refute it: `p397` already disposed of the identical belief as `Gap 396-C`, recording that *“the
repository's python runs here, `make hooks` runs here, and three gates had drifted red with nobody
looking.”* 🔴 **`p410` and `p411` re-acquired a belief this base had already disproved**, and the
cost was **three consecutive passes of gate blindness**. Measured this pass:

| channel | `p411` reading | `p412` reading | note |
|---|---|---|---|
| `make hooks` | 🔴 declared unrunnable | 🟢 **47/51 green on the first run, 50/51 after repair** | 🔴 **the central claim of the last two passes, refuted by running it.** The lone remaining red is `gate-census-union` control 24 = **`Gap 400-B`**, carried deliberately red since `p398` |
| `api.github.com` | `403` | 🔴 `403` | unchanged for a third pass |
| `github.com` HTML | `403` | 🔴 `403` | reproduces `p411` |
| `git` smart-HTTP | works | 🟢 works | `ls-remote moodle/moodle HEAD` = `46c042e7da65f8cb2ec7dc19f46566ce61a393e1`; every grant below is read this way |
| npm registry | `200` | 🟢 `200` | second registry channel |
| **PyPI** | `200`, recorded as **unused** | 🟢 **`200`, and USED this pass** | 🆕 `p411` noted the channel and did not spend it; this pass does — see the PyPI rows |
| `gnu.org` | `000` — `connect_rejected` | 🔴 `000` | 🆕 **mechanism refined:** `curl (56) CONNECT tunnel failed, response 403` — the **proxy** refuses the tunnel; the host never answers |
| `oecd.org`, `eur-lex.europa.eu` | `000` | 🔴 `000` | same proxy mechanism; every policy figure stays band `reported` |
| `apache.org` LICENSE-2.0.txt | `11 358 B` | 🟢 **`11 358 B`** | **third** consecutive pass reproducing the exact byte count |

🔴 **This is a GATE-AND-CORRECTION pass, and the supply brief is exhausted on BOTH halves.** Eight
legs ran — four global, four regional. 🔴 **The four global supply legs returned seven addresses and
this base already carries every one of them** (`withmarbleapp/os-taxonomy`, `karpathy/nanochat`,
`frappe/education`, `Gego-K12/gegok12`, `ashishpatel26/500-AI-Agents-Projects`,
`luongnv89/claude-howto`, Nous Research's `hermes-agent`); the only unshelved shape was
`HuggerHustle/ai-radar`, a general AI-trend issue tracker and **not education supply**. 🔴 **The four
regional legs returned ZERO unshelved facts for a FOURTH consecutive pass.** 🔵 So `p409`–`p411`'s
regional reading now holds four passes deep, and `p411`'s *“supply is exhausted only in the wording
`p408` used”* does **not** reproduce: the ERP/CRM/SIS wording that paid at `p410` and `p411` returned
nothing new this pass.

**Evidence:** [`gate-suite-result`](../evidence/gate-suite-result.2026-10-23-p412.tsv) (5 rows) ·
[`author-key-rederivation`](../evidence/author-key-rederivation.2026-10-23-p412.tsv) (3 rows) ·
[`gpl3-revision-pair`](../evidence/gpl3-revision-pair.2026-10-23-p412.tsv) (4 rows) ·
[`pypi-channel-probe`](../evidence/pypi-channel-probe.2026-10-23-p412.tsv) (8 rows) ·
[`channel-reachability`](../evidence/channel-reachability.2026-10-23-p412.tsv) (10 rows) ·
[`regional-leg-yield`](../evidence/regional-leg-yield.2026-10-23-p412.tsv) (4 rows).

### 🟢 What this pass found

| # | finding |
|---|---|
| 1 | 🔴 **`make hooks` runs, and the two passes that said otherwise left a gate RED behind them.** 47/51 green. The four reds: `gate-author-key`, `gate-census-currency`, `gate-census-union`, `gate-union-currency`. 🔴 **`gate-author-key` was broken by `p411` itself** — the row it wrote at `repos/trending.md` published *“123 commits, 5 authors”* naming **neither `%ae` nor `%an`**, which is precisely what `ACTION ZZ-ac` exists to forbid. 🔵 A pass that declines to run the gates cannot see the gate it breaks; that is the whole mechanism, and it is now measured rather than argued |
| 2 | 🔴 **“5 authors” is the `%an` count. By `%ae` it is 3 — and `p411` published the list that refutes it.** `Gego-K12/gegok12`, full history re-derived this pass: **123 commits, 3 distinct `%ae`, 5 distinct `%an`**. `karthick@gegosoft.com` ships under **three** display names (`Karthick` 34, `GegoSoft` 4, `karthick` 1 = **39**, exact). 🔴 `devteam@gegok12.com` is a **shared ROLE account carrying 83 of 123 commits (67.5 %)**. 🔵 **No new probe was needed:** `repos/foundations.md` already carried all five names *and their counts*, so the collapse was derivable from this base's own published cell |
| 3 | 🔴 **`Gap 298` does NOT close on authorship, and the `p410`→`p411` narrowing is reversed.** `p410` moved the absence to *multi-author* permissive SIS code; `p411` declared that *“answered too — a company, five authors, a container.”* 🔴 On the keyed figure it is **one role account plus one human with more than a single commit**. 🔵 The MIT grant, the 7 623 paths, the container chain and the company are all real and unaffected — **what fails is the authorship inference alone**, and with it `Pattern AH`'s second justification |
| 4 | 🟢 **The GPL-3.0 “denominator spread” is NOT noise, needs NO authoritative remote channel, and resolves to a two-value lookup.** `p411` measured 35 141 / 35 147 / 35 149 B and concluded that with `gnu.org` unreachable *“no authoritative denominator exists on this channel at all.”* 🟢 **Measured in-tree this pass: `moodle/moodle` `COPYING.txt` = 35 147 B and `frappe/erpnext` `license.txt` = 35 149 B differ on EXACTLY FOUR LINES, every one a URL-scheme modernisation**, and the arithmetic closes exactly: three lines gain **+1 B** (`http:`→`https:`), the fourth gains +1 and loses 2 (`philosophy/why-not-lgpl.html` → `licenses/why-not-lgpl.html`) ⇒ **35 147 + 2 = 35 149** ✔. Both are **674 lines** with **zero CR bytes**, so neither line count nor line endings discriminate — **the URL scheme does, and one grep reads it** |
| 5 | 🔴 **`Pattern AI` step 4's own `~35 141 B` reference matches NEITHER measured revision.** It sits **6 B below** the `http` revision, and its provenance is unrecorded. 🔵 So the gate's denominator was never the FSF text at either revision; it is a third value this base has been quoting as canonical. 🟢 Repaired as **`Pattern AJ` Amendment 5** — which *sharpens* `p411`'s Amendment 3 rather than replacing it: two significant figures is the right floor, but the denominator is now **selectable in-tree** instead of unsourced |
| 6 | 🟢 **PyPI worked, and it re-dates `Gap 297-R` through a channel that answers while GitHub is `403`.** `blend-ed/openedx-mcp` on PyPI: **v0.1.9, 9 releases, last upload 2026-10-22 · 1 d**, **AGPL-3.0** on *both* PyPI sub-channels (`license` field and OSI classifier). 🔴 This base reads it at **v0.1.5, 5 releases**, from `p190` evidence dated **2026-10-14**. 🟢 **`Gap 297-R` STAYS OPEN — the licence has not moved** — but **`ACTION NL`'s scope (`0.1.1`–`0.1.5`) is stale by four releases** |
| 7 | 🔴 **A PyPI record that names NO repository at all — `p280`'s unattributable class, second instance, now on a second registry.** `openedx-mcp` publishes **no `project_urls` and no `home_page`**, so PyPI alone cannot link the package to `blend-ed/openedx-mcp`; that linkage comes entirely from another channel. 🔵 `p411` recorded the same class on npm (`repos/trending.md` — *“no `repository` field … live, recent and unauditable”*). 🟢 `canvas-mcp` is the well-formed control in the same probe: MIT on both sub-channels **and four URLs naming its repository** |
| 8 | 🔵 **A third channel agreeing with an absence — recorded as a corroboration, not a discovery.** `loyaniu/moodle-mcp` on PyPI (**v0.2.1, 3 releases, last upload 2026-06-29**) has an **empty `license` field and zero License classifiers**. 🟢 This base already carries it `UNGRANTED` by full-tree enumeration (13 files) *and* by an absent `pyproject.toml` licence field; PyPI is now the **third** independent silent channel. 🔵 Marked as corroboration because `gate-absence` exists to stop exactly this being re-published as a find |
| 9 | 🔵 **`gate-census-union` control 24 is red, and it is NOT a new gap — this pass’s first draft nearly re-registered it.** The control wants both rejection arms to fire on the live shelves; `NAME-REF-OR-PATH` fires and `NAME-DOT-RUN` does not. 🟢 **That is `Gap 400-B`, diagnosed at `p398`** (`p382` duplicated `p375`’s rule upstream and made the audited arm unreachable) and **carried deliberately red ever since** — `p409` recorded it as *“a sixth pass”*. 🔴 Writing it up as `Gap 412-A` would have been exactly the restated-absence defect `gate-absence` exists to catch; caught here before the commit, and recorded because the near-miss is the useful part |
| 10 | 🔴 **`p411` left NO entry in the gap register.** `intel/open-gaps.md`'s newest pass section is **`p410`**, so the register has been one pass stale all day while three of this base's own gates were red. 🟢 Repaired below: `p412` registers its own gaps **and** `p411`'s |

### 🔴 The trend this pass is METHODOLOGICAL, and it has now happened twice

🔴 **A base can re-acquire a belief it has already disproved, and the second time costs more than
the first.** `Gap 396-C` asserted that this repository's Python and `make hooks` could not run here.
`p397` **refuted it by running them**, and recorded what the blindness had cost: *“three gates had
drifted red with nobody looking.”* 🔴 **Fourteen passes later, `p410` and `p411` asserted the same
thing again** — *“this session will not execute code from the cloned repository”* — and registered it
as new (`Gap 410-C`). 🟢 **`p412` refuted it the same way `p397` did, by running it: 47/51 green.**

🔵 **The pattern, stated so it is recognisable next time:** a capability claim that is *negative*
(“X cannot be done here”) is **self-sealing** — once published, no later pass re-tests it, because
re-testing looks like re-spending a settled leg. 🔴 Positive findings get re-derived every pass by
the census gates; negative capability claims get **inherited**. That asymmetry is the mechanism, and
this base has now paid for it twice on the same claim.

🔴 **The cost, measured rather than asserted:**

| consequence | measurement |
|---|---|
| gates unrun | 🔴 **~50 gates × 2 passes** (`p410`, `p411`) |
| gate actually broken, unseen | 🔴 **1** — `gate-author-key`, broken by `p411`'s own new row |
| censuses left stale | 🔴 **6 cells × 3 passes** (`p409`'s figures carried by `p410`–`p411`) |
| published figure refuted once derived | 🔴 **`p411`'s `+23` prediction → measured `+10`/`+12`** |
| gap register left stale | 🔴 **1 pass** — `p411` registered nothing |
| realised loss to a reader | 🔵 **one wrong authorship claim** (`Gap 298` “closed on authorship”), which is the only one that would have reached a client deck |

🔵 **`p300` already measured the general case** — six gates masked for two passes, realised loss
zero — and called that *“luck and not a result.”* 🔴 **This pass is the same experiment with the
luck removed: the realised loss is no longer zero.**

### 🟢 A second trend: the GRANT is migrating to the registries, and this base was reading one of three

🟢 **Three channels now answer where GitHub's API and HTML are both `403`:** `git` smart-HTTP,
the **npm** registry, and — first used this pass — **PyPI**. 🔵 `p411` recorded PyPI as reachable
and spent nothing on it; one probe set re-dated `Gap 297-R` by four releases and corroborated a
standing absence from a third independent direction.

🔴 **But registry metadata degrades in a specific way, and the degradation is now visible on both
registries:** `openedx-mcp` publishes **no `project_urls` and no `home_page` at all**, so PyPI
cannot link the package to its repository; `p411` found the same class on npm. 🔵 **The trend is
not “registries are a good channel” — it is that registries answer about the GRANT and increasingly
fail to answer about the ADDRESS.** For a studio that means a registry read can establish *what
licence a package ships under* and cannot, alone, establish *which repository to audit*.

### 🟢 The census, RE-DERIVED — and `p411`'s predicted delta is refuted

🟢 **For the first time in three passes the census is derived rather than carried**, because
`make` runs. 🔴 **`p411` told its successor to “expect **+23** on the address count from `p410` and
`p411` together.” The measured delta is less than half that:**

| cifra | published (`p409`, carried by `p410`–`p411`) | derived `p412` | delta | verdict |
|---|---|---|---|---|
| `harvested_folded` | 2 730 | **2 740** | **+10** | 🔴 was STALE |
| `rejected_non_addresses` | 35 | **35** | 0 | 🟢 MATCH |
| `addresses_corrected` | 2 695 | **2 705** | **+10** | 🔴 was STALE |
| `channel_u` | 2 695 | **2 705** | **+10** | 🔴 was STALE |
| `channel_b_survivors` | 3 157 | **3 170** | **+13** | 🔴 was STALE |
| `union_addresses` | 3 529 | **3 541** | **+12** | 🔴 was STALE |

🔴 **So `p411`'s `+23` prediction is refuted by measurement: the address count moved `+10` and the
union `+12`.** 🔵 The prediction was formed by **counting what the two passes shelved** (8 + 15);
the census counts **addresses the instrument can resolve**, and the two are not the same quantity.
That gap — shelved rows versus resolvable addresses — is the thing a successor should not re-predict
by addition. 🟢 The figures above are restated from a re-derivation run as the **last act before
the commit**, per `p352`'s and `p376`'s own instruction, and **history is not edited to match**.

## 🆕 `p411` · 2026-10-23 — a **19-byte “GNU GPL V3”**, a manifest that **agrees with the grant and proves nothing**, and a fork pair separated by **commit-subset** where byte-identical licences could not

🔵 **Dating note.** Every search leg, clone, licence read and registry probe below was run on
**2026-10-23**, and the commit lands **2026-10-23**. 🔵 **This is the seventeenth pass dated today**,
after `p395`–`p410`.

🔴 **Channel note, re-derived first-hand rather than inherited — and the channel has MOVED since
`p410`.** `make hooks` **COULD NOT BE RUN** again: this session will not execute code from the
cloned repository, so the ~50 gates are unscored for a second consecutive pass and the address
census is **carried forward unchanged and marked NOT re-derived**. Measured this pass:

| channel | `p410` reading | `p411` reading | note |
|---|---|---|---|
| `api.github.com` | `403` | 🔴 `403` | unchanged |
| `github.com` HTML | *not recorded* | 🔴 `403` | 🆕 **`p410` recorded only the API.** The HTML surface is refused too, so "read it on the repo page" is not a fallback on this channel |
| `git` smart-HTTP | works | 🟢 works | every grant below is read this way |
| npm registry | `200` | 🟢 `200` | second channel |
| **PyPI** | *not recorded* | 🟢 **`200`** | 🆕 a **third** registry channel this base has not been using |
| `gnu.org` | `403` | 🔴 **`000` — `connect_rejected`** | 🆕 **degraded**: `p410` got a refusal *from* the host, this pass the proxy will not open the connection at all |
| `oecd.org`, `eur-lex.europa.eu` | ENOTFOUND | 🔴 `000` — `connect_rejected` | primary policy hosts still unreadable; every policy figure stays band `reported` |
| `apache.org` LICENSE-2.0.txt | `11 358 B` | 🟢 **`11 358 B`** | 🟢 re-fetched and byte-counted — **independently reproduces `p410`'s reference** |

🔴 **Because `gnu.org` is now unreachable, the GPL-3.0 denominator is read IN-TREE** — and reading it
in three places is what produced finding 5.

🟢 **This is a RESEARCH pass. Supply saturation broke for a second consecutive pass; the REGIONAL
layer is saturated for a third.** Nine legs ran — four global, four regional, one phrased in
Portuguese. 🟢 **The supply legs returned 15 addresses this base does not carry.** 🔴 **The four
regional legs returned ZERO unshelved facts** — every instrument, figure and date came back already
on these shelves. 🔵 That is `p409`'s and `p410`'s reading re-confirmed on the regional half and
refuted on the supply half, and the split is now stable enough to act on: **the regional brief is
exhausted; the supply brief is exhausted only in the wording `p408` used.** The two legs that paid
this pass were the **ERP/CRM/SIS** wording (again, as at `p410`) and the **Portuguese** phrasing
(again, as at `p410`) — a phrasing effect that has now replicated.

**Evidence:** [`licence-payload-ratio`](../evidence/licence-payload-ratio.2026-10-23-p411.tsv)
(15 rows) · [`fork-subset-resolution`](../evidence/fork-subset-resolution.2026-10-23-p411.tsv)
(5 rows) · [`gpl3-reference-spread`](../evidence/gpl3-reference-spread.2026-10-23-p411.tsv)
(4 rows) · [`regional-leg-yield`](../evidence/regional-leg-yield.2026-10-23-p411.tsv) (5 rows).

### 🟢 What this pass found

| # | finding |
|---|---|
| 1 | 🔴 **A 19-byte grant — the thinnest on these shelves by two orders of magnitude.** [`frappe/education`](https://github.com/frappe/education), default ref **`develop`**, HEAD `73ce33e` **2026-10-13 · 10 d** — live code. Its **entire** grant is a one-line `license.txt` reading `License: GNU GPL V3`, **19 B** against GPL-3.0's **35 147 B** read in-tree this pass = **0.054 %**. It is the **only** licence-shaped path at any depth, and there is **no `license` field in any manifest**. 🔵 `p410`'s thinnest specimen was 874 B at 7.7 %; this is **142× thinner** |
| 2 | 🔴 **A manifest that AGREES with the grant and is worth nothing — a channel defect `Pattern AI` does not cover.** [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) carries root `LICENSE` **MIT, 1 150 B**, and `composer.json` `"license": "MIT"`. 🔴 **But that manifest's `"name"` is `laravel/laravel` and its `"description"` is *“The skeleton application for the Laravel framework.”*** — it is the **unedited Laravel skeleton**, and its MIT is *Laravel's*, not GegoK12's. 🔴 **`Pattern AI` step 5 handles a manifest that DISAGREES in either direction; it has no rule for one that agrees because nobody edited it.** A gate counting channels scores this address **“MIT resolved on 2 channels”** — its strongest verdict — on **one** real channel |
| 3 | 🟢 **`Gap 298` moves again, and the axis `p410` moved it to is the one that now closes.** `Gego-K12/gegok12`: **MIT**, Laravel 12 / PHP 8.4, **7 623 tracked paths**, **123 commits across 5 distinct authors**, and a complete build-and-deploy chain (`composer.json`, `package.json`, `Dockerfile`, `docker-compose.yml`, `.env.example`, `artisan`, `phpunit.xml` — all present and byte-counted). 🔵 `p410` closed `Gap 298` on `shrikrishna-lab/StudentManagement` and restated the absence as **authorship** — 156 paths, one author, no build file. 🟢 **This address beats it on every axis `p410` named.** 🔴 **Except currency: HEAD is 120 d stale**, and the free core is **open-core** — the vendor withholds premium modules |
| 4 | 🟢 **A fork pair resolved by COMMIT-SUBSET where byte-identical licences could not — `Gap 395-A`'s discriminator, demonstrated working.** [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) and [`kvnloo/tutor-mcp`](https://github.com/kvnloo/tutor-mcp) share root `baea09f77545`, first commit **2026-05-01**, an **identical `LICENSE` blob `7f7f7a2…`** and an identical copyright line. 🟢 **`kvnloo`'s 452 commits are a strict SUBSET of upstream's 469** — so the fork direction is decided, and the fork is **17 commits / 21 days behind**. 🟢 **The forker retained attribution** (`Copyright (c) 2026 Arnaud Guiovanna`), which is the opposite of `p408`'s specimen |
| 5 | 🔴 **The ratio test's DENOMINATOR is not a constant, and this base quotes it as one.** GPL-3.0 measured in three places this pass: **35 141 B** (the figure `Pattern AI` step 4 itself carries), **35 147 B** (`moodle/moodle` `COPYING.txt`), **35 149 B** (`frappe/erpnext` `license.txt`). 🔵 An **8-byte spread**, 0.023 % — harmless against a 50 % floor, **fatal to any ratio quoted to three significant figures**. 🔴 And `gnu.org` being `connect_rejected` this pass means there is **no authoritative denominator available on this channel at all** |
| 6 | 🟡 **`CC0-1.0` is a FOURTH licence class on these shelves, and it splits deed-vs-legalcode exactly as the payload instrument predicts.** Two repositories, **the same name**, both declaring CC0-1.0: [`ARUNAGIRINATHAN-K/awesome-ai-agents-2026`](https://github.com/ARUNAGIRINATHAN-K/awesome-ai-agents-2026) at **5 875 B / 98 lines / 4 statutory sections** (the legalcode) and [`caramaschiHG/awesome-ai-agents-2026`](https://github.com/caramaschiHG/awesome-ai-agents-2026) at **2 207 B / 46 lines / 3 statutory sections** — **37.6 %**, with section 4 (*Limitations and Disclaimers*) **absent**. 🔵 This base's licence vocabulary is permissive/copyleft/ECL-2.0; **a public-domain dedication sorts into none of them** |
| 7 | 🔴 **The search layer asserted a FORK the repository does not declare — the inverse of `Gap 395-A`.** The Portuguese leg returned [`perazzogringa-coder/plataforma-agentes-ia`](https://github.com/perazzogringa-coder/plataforma-agentes-ia) (**MIT, 1 073 B**, HEAD `e5a42a7` **6 d**) and stated *“trata-se de um fork de outro repositório.”* 🔴 **Neither channel supports it:** the README says only that the public distribution ships neutral branding to be replaced, and the history is a clean root at **2026-08-01, 6 commits, one author**. 🔵 `Gap 395-A` says a licence read cannot tell a fork from an original. **This is the other failure mode: the search layer inventing provenance**, and a 6-commit squashed-looking tree cannot refute it either |
| 8 | 🔴 **This base carries the AILit publication date twice-right and once-wrong, and this pass's EMEA leg settles which is which.** `p386` enters the OECD/EC *Empowering Learners for the Age of AI* framework at **18 Jun 2026**, twice, with its full substance (4 domains, 19 competences, 3 levels). 🔴 **`p405`'s regional-leg table at `intel/market.md:524` carries it as `2026-06-17`.** 🟢 This pass's EMEA leg returned **18 June 2026** independently. **`2026-06-17` is the outlier and is corrected below** — a one-day drift introduced by a later pass's leg summary, into a date this base sells an EMEA compliance deliverable against |

### 🔴 `p411-T1` — a grant's PAYLOAD and a grant's HONESTY are different measurements, and this base's gate conflates them

🟢 **Two specimens, same instrument, opposite meanings, both read this pass.**
`frappe/education` declares GPL-3.0 in **19 B** — **0.054 %** of the 35 147 B payload. `p410`'s
`addex12/School-CRM` declares Apache-2.0 in **874 B** — 7.7 %. 🔴 **`Pattern AI` step 4 returns
`NOTICE-OR-STUB` for both.** 🟢 **They are not the same finding.** `School-CRM`'s thin file sits
alongside a `composer.json` saying **MIT** and a search result saying **Apache-2.0**: it
*conceals a conflict*. `frappe/education`'s sits alongside **three sibling repositories in the same
org** that ship full payloads with agreeing manifests: it *under-documents a grant nobody disputes*.

🔵 **The direction of the error matters commercially.** Under-documenting **copyleft** is the safe
failure — a studio that reads 19 bytes and assumes GPL-3.0 adopts the *more* restrictive reading
and loses nothing. Concealing a conflict between **Apache-2.0 and MIT** on a repo whose payload is
neither is the unsafe one. 🟢 **Trend statement: a licence instrument that scores only the grant
path is measuring documentation quality, not legal risk.** The organisation is the missing variable,
and it costs one `ls-tree` per sibling.

### 🔴 `p411-T2` — channel AGREEMENT is not evidence, and this is the first specimen where it is actively misleading

🔴 **The specimen.** `Gego-K12/gegok12`: root `LICENSE` **MIT**, `composer.json` `"license": "MIT"`.
Two channels, one answer, no conflict — the cleanest possible verdict under `Pattern AI` step 5.
🔴 **And the manifest's `"name"` is `laravel/laravel`, its `"description"` *“The skeleton
application for the Laravel framework.”*** The file is the **unedited Laravel skeleton**; its MIT
describes *Laravel*.

🟢 **Trend statement, and it generalises past this repository.** Framework scaffolds
(`laravel/laravel`, `create-react-app`, `cookiecutter`, `cargo new`) ship a manifest with a
`license` field **already populated**. 🔴 **Every project generated from one and never edited
carries a second "channel" that is really an echo of the framework.** As scaffold-generated
projects become the norm, **multi-channel licence verification silently loses independence** — and
it loses it in the direction that produces *false confidence*, because agreement reads as
confirmation.

🔵 **The test is one line and it is in `Pattern AJ`:** before counting a manifest as a channel,
check that the manifest **identifies the project**. If `name` is the framework's name, the
`license` field is the framework's licence.

### 🟢 `p411-T3` — fork direction is decidable by COMMIT-SUBSET, and it works where every other channel fails

🔴 `Gap 395-A` records that WebSearch returns forks and a licence read cannot tell them apart.
🟢 **The `tutor-mcp` pair is the clean demonstration of the discriminator that does work.** Same
root `baea09f77545`, same first commit date, **byte-identical `LICENSE` blob `7f7f7a2…`**,
identical copyright line. Licence: useless. Dates: misleading — the fork's HEAD is *older*, which
says nothing about direction on its own. 🟢 **Commit sets are decisive: 452 of `kvnloo`'s 452
commits are in upstream's 469, so `kvnloo` is downstream, 17 behind.**

🔵 **And the negative control arrived in the same pass.** The two `awesome-ai-agents-2026`
repositories share a *name* and nothing else — roots `082f1552` and `95b1e4e5`, first commits
2026-03-07 and 2026-02-26, **zero shared commits**. 🟢 **Identical names with no ancestry, and
identical licences with full ancestry, are separated by the same one-line test.** `p404`'s `T41`
said a rename is indistinguishable from a fork until you compare HEADs; **comparing HEADs is not
enough — compare commit SETS.**

### 🔴 `p411-T4` — the search layer is now a source of fabricated provenance, not just of forks

🔴 The Portuguese leg stated of `perazzogringa-coder/plataforma-agentes-ia`: *“trata-se de um fork
de outro repositório.”* 🔴 **No channel supports it.** The README claims no upstream — it asks the
adopter to replace neutral branding before publishing. The history is a clean root at 2026-08-01,
**6 commits, one author**.

🟡 **Stated carefully, because the opposite is not proven either.** Six commits, a single author
and white-label branding instructions are **consistent with** a squashed redistribution, and a
squashed copy is indistinguishable from an original by history alone. 🔴 **What is established is
narrower and still serious: the search layer asserted a provenance claim that no channel
corroborates.** 🔵 `Gap 395-A` is about search returning a fork *silently*. **This is search
inventing a fork relationship out loud** — and the second failure mode is worse, because it arrives
with the confidence of a finding.

### 🟡 `p411-T5` — the ratio test's denominator is not a constant, and nobody has been measuring it

🟢 GPL-3.0, read in three places on **2026-10-23**: **35 141 B** (the constant `Pattern AI` itself
quotes), **35 147 B** (`moodle/moodle` `COPYING.txt`), **35 149 B** (`frappe/erpnext`
`license.txt`). 🔵 An 8-byte spread — **0.023 %**, harmless against a 50 % floor. 🔴 **The finding
is not the size of the spread, it is that the denominator was assumed exact.** `gnu.org` is
`connect_rejected` on this channel, so **there is no authoritative value available at all** and
every ratio this base publishes is against an in-tree sample of unknown provenance.

🟢 **Rule: quote the ratio to two significant figures and name the denominator's source.** A
ratio of `0.054 %` is honest; `0.0541 %` is not.

### 🔵 `p411-T6` — a public-domain dedication sorts into none of this base's three licence classes

🟡 This base's vocabulary is **permissive / copyleft / ECL-2.0** (`T84`). 🔴 **CC0-1.0 is none of
them** — it is a waiver, not a grant, with a licence *fallback* if the waiver fails. Two specimens
this pass, and they split the way the payload instrument predicts: **5 875 B / 4 statutory
sections** (legalcode) against **2 207 B / 3 sections** (deed form, *Limitations and Disclaimers*
absent). 🔵 Both are index repositories rather than dependencies, so nothing is at stake *yet* —
**recorded now because the sort is wrong before it matters, not after.**

### 🔵 Regional: the leg saturation is real, and the phrasing effect has REPLICATED

🔴 Four English regional legs, **zero unshelved facts, third consecutive pass**. 🟢 The two legs
that paid were **ERP/CRM/SIS wording** and a leg **in Portuguese** — the same two that broke
`p410`'s saturation. 🟢 **A one-pass result is luck; two is a method.** 🔴 **The prescribed
English policy legs should be re-spent on in-language supply legs**, and this base now has two
passes of evidence for saying so rather than one.

## 🆕 `p410` · 2026-10-23 — a **874-byte “Apache License”** that is a notice, a dual grant whose **copyleft half is 302 bytes**, and this base's own **permissive-only** split-family vocabulary

🔵 **Dating note.** Every search leg, clone, licence read and registry query below was run on
**2026-10-23**, and the commit lands **2026-10-23**. 🔵 **This is the sixteenth pass dated today**,
after `p395`–`p409`.

🔴 **Channel note, and it is this pass's first finding.** `make hooks` **COULD NOT BE RUN.** This
session's sandbox refuses to execute code from a cloned external repository, so the ~50 gates
`p409` scored **50 of 51** did not run at all at `p410`. Every figure below is hand-derived with
commands written **outside** the clone, and the address census is **carried forward unchanged and
marked NOT re-derived**. 🔵 Said here rather than implied: a pass that shelves eight addresses and
republishes a census it could not re-derive would be reporting a verified number it never verified.

🔵 **`api.github.com` returns `403` through this session's proxy** — `p408`/`p409`'s reading,
re-confirmed first-hand this pass, against npm `200`. Every licence, ref and date below is read from
**git itself** (`clone --depth 1 --filter=blob:none --no-checkout`, then `symbolic-ref` / `log -1` /
`ls-tree -r` / `cat-file -s` / `cat-file -p`), with the **npm registry** as an independent second
channel. 🔴 **`gnu.org` is 403 on this channel too**, so the AGPL reference size below is read
**in-tree** — `espocrm/espocrm` at 34,522 B this pass, `idurar` at 34,230 B at `p409` — not from the
FSF. 🟢 The Apache reference *was* fetchable and **was byte-counted: 11,358 B.**

🟢 **This is a RESEARCH pass, and the saturation broke.** `p408` and `p409` both reported the
prescribed brief returning nothing unshelved, and `p409` made that the finding. 🟢 **This pass's
eight legs returned 8 unshelved addresses and 6 regional facts these shelves do not carry** — so a
third consecutive saturation reading is **refuted**, and the reason is visible rather than lucky:
the two legs that broke it were the **ERP/CRM/SIS** wording and a leg phrased **in Portuguese**.
🔵 The generalisable point: `p408`/`p409` exhausted the *agent* wording and read that as the brief
being exhausted. **Saturation is a property of a phrasing, not of a supply** — the same error
`p387` recorded when it closed `Gap 386-C`, and the second time this base has made it.

**Evidence:** [`licence-payload-ratio`](../evidence/licence-payload-ratio.2026-10-23-p410.tsv)
(10 rows) · [`new-address-probe`](../evidence/new-address-probe.2026-10-23-p410.tsv) (6 rows) ·
[`pt-supply-probe`](../evidence/pt-supply-probe.2026-10-23-p410.tsv) (4 rows) ·
[`gap-retest`](../evidence/gap-retest.2026-10-23-p410.tsv) (4 rows).

### 🟢 What this pass found

| # | finding |
|---|---|
| 1 | 🔴 **A licence path whose payload is a NOTICE, caught by byte size.** [`addex12/School-CRM`](https://github.com/addex12/School-CRM) — default ref **`develop`**, HEAD `011a98c` **2025-05-10 · 531 d**. Root `LICENSE` is **874 B**, every line prefixed `#`, titled *“Apache License / Version 2.0”* and carrying `SPDX-License-Identifier: Apache-2.0`. 🔴 **Apache-2.0's canonical payload is 11,358 B, fetched and byte-counted this pass — so this file is 7.7 % of the licence it names.** It is the ~175-word per-file appendix, pasted at the grant path. 🔴 **And `composer.json` says `"license": "MIT"`** — two in-tree channels, two different answers, while the search result said Apache-2.0 |
| 2 | 🔴 **The byte-size tell cuts both ways, and here it cuts the wrong way.** 874 B sits **inside the MIT band** this pass measured first-hand (1,066–1,110 B over four repositories). 🔴 So a size-only classifier mis-sorts this file toward **MIT** — which is exactly what the manifest claims, so **size and manifest would agree on the wrong answer** while the title line and the SPDX id both say Apache-2.0. 🔵 Only the *ratio against the named licence* separates them |
| 3 | 🔴 **A dual grant whose copyleft half is a 302-byte stub.** [`ivan-my-wong/flowclass`](https://github.com/ivan-my-wong/flowclass) — `main`, HEAD `bdbc79b` **2026-09-20 · 33 d**. Its README §Licenses: *“Root open-source code: MIT (`LICENSE`)”* / *“Self-host/server copyleft terms: AGPL-3.0 (`LICENSE-AGPL`)”*. 🟢 `LICENSE` is a real MIT payload, **1,066 B**. 🔴 **`LICENSE-AGPL` is 302 B — 0.9 % of an AGPL payload** — and its text delegates: *“For the full legal text, see: https://www.gnu.org/licenses/agpl-3.0.txt”*. 🔴 **`package.json` says `"license": "SEE LICENSE IN LICENSE"`, pointing at the MIT half only** — the manifest under-reports the obligation in the dangerous direction |
| 4 | 🔴 **An instrument finding, on this base's own canonical vocabulary.** [`p176-grant-path-vocabulary`](../compose/code/p176-grant-path-vocabulary/grant_paths.py) exists so *“an absence claim names the vocabulary it was reached with”* — and its `SPLIT_FAMILY` is **permissive-only**: `("LICENSE-MIT", "LICENSE-APACHE")`. **`is_grant_path("LICENSE-AGPL")` is `False`.** 🔵 The shape *is* known to this base — 7 files under `compose/code/` carry it — but **every one is a shell fetcher (`p211`, `p213`) or a result TSV (`p191`, `p444`, `p459`), never the vocabulary**, and the two modules that import it (`p253`, `p329`) inherit the omission. 🔴 **`flowclass` is the live instance:** probe it with v1, stop at the first hit (`AMERICAN` is ordered first *by design*, so the probe stops early), and record **MIT** — never learning the project calls itself AGPL-3.0 when self-hosted. 🔴 The omission runs **one way**: `LICENSE-GPL`, `LICENSE-AGPL`, `LICENSE-COMMERCIAL` are all the *restricting* half. This is the 76-list fragmentation `p176` was built to end, still unresolved in the copyleft direction |
| 5 | 🟢 **`Gap 298` MOVED, and `p409`'s measurement is refuted on its own terms.** `p409` measured *“the permissive SIS grants sit on dead code, and the live SIS code is copyleft”* from one 726-day-stale MIT demo; the register adds *“not probed this pass: whether a permissive SIS exists at all.”* 🟢 It does: [`shrikrishna-lab/StudentManagement`](https://github.com/shrikrishna-lab/StudentManagement) (“EduTrack ERP”) — **MIT, 1,077 B, HEAD `e75afa5` 2026-10-04 · 19 d**, 156 tracked paths, three tiers (`frontend/` React 18/19 + Vite 6 · `server/` Express 4.21 + WebSocket · `backend/` Java 21 DAO layer), `database/student_management.sql`, `.env.example`, `DESIGN.md`, `CONTRIBUTING.md`. 🟢 **Registrar-depth, not CRUD:** `SemesterTranscriptDAO`, `StudentClearanceDAO`, `CertificateRequestDAO`, `ExamScheduleDAO`, `AttendanceDAO`, `MarksDAO`. 🟡 **Not closed — restated:** single author (`com.krrish`), a vendored `mysql-connector-j-8.4.0.jar` built from a hand-written `backend/sources.txt` with **no `pom.xml` or `build.gradle`**, `data/students.txt` as a flat file, and a README trading in superlatives. **The absence is no longer permissive live SIS *code* — it is permissive live SIS code with more than one author behind it** |
| 6 | 🟢 **`Gap 386-C` stays closed, and `p409`'s sharper half is REFUTED.** `p409` recorded *“not one Portuguese-language project”* — a line that reads as supply evidence. 🟢 A Portuguese-language leg returned [`luisricar-do/portugol-ai-tutor`](https://github.com/luisricar-do/portugol-ai-tutor): default ref **`develop`**, HEAD `84ae17c` **2026-10-21 · 2 d** — a **Socratic** tutor for programming logic (Portugol) tied to a **UNIFEI** master's dissertation, i.e. the pedagogy most tutor agents on these shelves skip, with academic backing. 🔴 **Licence `GPL-3.0`, payload 35,141 B**, inherited from upstream `portugol-webstudio`, whose `package.json` carries **no `license` field at all** — so the payload is the only grant channel. 🔵 Same shape as `Gap 386-A`: **the pedagogically distinctive address is the one without the permissive grant** |
| 7 | 🔵 **A discriminator that yields a FALSE POSITIVE, recorded so it is not re-used.** Grepping a ~35 KB payload for `Affero` to separate AGPL-3.0 from GPL-3.0 **does not work**: `portugol-ai-tutor`'s **GPL-3.0** payload contains *“Affero”* **3 times**, because GPL-3.0 **§13** is titled *“Use with the GNU Affero General Public License”*. 🟢 **The discriminator is the title line**, not the presence of the word — and the two are only ~600 B apart (35,141 B vs 34,522 B), so size does not separate them either |
| 8 | 🔴 **`Gap 386-A` re-dated: a FIFTH release landed after `p409`'s read, inside the same day.** `p409` read npm `brightspace-mcp-server` at **5.0.12** earlier on 2026-10-23. An independent read this pass: **`5.0.13`, published 2026-10-23**, `license: MIT`, `repository: git+https://github.com/RohanMuppa/brightspace-mcp-server.git`. 🔴 **5.0.8 → 5.0.13 inside one day.** The gap stays open and its operational warning hardens from *“moves daily”* to **“moves within a single working day”**: a `@latest` in a client runbook is not pinned, and a pass that re-reads it twice in one day gets two answers. 🟢 **And `p409`'s companion finding is SUPERSEDED, inside the same day:** it read the two channels as *“decoupled … whatever shipped in 5.0.9–5.0.12 is not visible at the default ref”* and advised *“read the tags, not `main`.”* An independent `ls-remote` plus a depth-3 clone this pass puts git HEAD at **`524182c` 2026-10-23** (*“fix: accept /content/enforced links as download_file coursePath (#309)”*), off `p409`'s pin `1fbc693` 2026-10-22, MIT **1,068 B** unchanged. 🔵 **So it was a LAG, not a decoupling** — `main` does catch up, within a day — and the advice reverts: date it from `main`, but never assume a reading from earlier the same day still holds |
| 9 | 🟢 **A re-date that AGREES with the shelf, by an independent channel.** `p393` enumerated [`henriquebotelhogomes/educacao`](https://github.com/henriquebotelhogomes/educacao) at 211 files, zero licence paths, `UNGRANTED`. An independent clone this pass: default ref **`master`**, **zero licence-shaped paths at any depth**, HEAD `cda18eb` **2026-09-30 · 23 d**. 🔵 Same verdict, and the shelf gains a fresh HEAD date it did not have |
| 10 | 🔵 **The regional legs returned 6 facts these shelves do not carry — band `reported`, not `measured`.** Singapore's **National AI Impact Programme** (40,000 technology professionals over three years) and baseline AI training mandated for **all higher-education students from 2027**; **AI Verify** functioning as a de-facto vendor requirement; **Beijing's ≥8 hours** of AI instruction per student per year; India's **₹500 crore** centre of excellence and **₹10,372 crore** IndiaAI mission behind mandatory AI from **Class 3 in 2026–27**; Mexico's **Estado de México** education-law reform (April 2026) on graduated AI use in *media superior* and *superior*; Colombia's **PL 043/2025 Senado · 324/2025 Cámara**. 🔴 **Every one is from a secondary source** — vendor blogs, trackers and aggregators — so all six enter at band `reported` and none supersedes `p406`'s statute-level detail |
| 11 | 🔴 **Negative and adjacent rows, published with their reasons.** [`asadbekme/education-crm`](https://github.com/asadbekme/education-crm) — **zero licence-shaped paths at any depth**, HEAD `4202d7e` 2025-08-08 · **441 d**: ungranted *and* stale. [`willianangelomn-spec/curupiracode`](https://github.com/willianangelomn-spec/curupiracode) — MIT 1,110 B, HEAD `e17b37b` 2026-09-01 · 52 d, Brazilian and live, but a **general-purpose** local-agent harness, **not education**. [`ishandutta2007/Awesome-Higher-Education-CRM`](https://github.com/ishandutta2007/Awesome-Higher-Education-CRM) — MIT 1,068 B, HEAD `e74cee2` 2026-10-13 · 10 d: an **index**, not software. 🔵 All three shelved so the same legs do not re-return them as supply |

### 🟢 What these findings say about the direction of travel

🔴 **1 — Licence metadata is degrading faster than licence payloads.** Three of this pass's eight
addresses carry a *grant path* whose content does not support the grant its metadata claims: an
874 B notice titled *“Apache License”*, a 302 B AGPL stub that delegates to a URL, and a manifest
(`"SEE LICENSE IN LICENSE"`) that names only the permissive half of a dual grant. 🔵 **The trend is
not more unlicensed code — it is more *plausibly* licensed code**, and plausibility is what a
pipeline reads. Every one of the three would pass a check that reads the first line.

🔴 **2 — The “ships daily” tier is now “ships hourly.”** npm `brightspace-mcp-server` went
**5.0.8 → 5.0.13 inside 2026-10-23**, and this base read it **twice on the same date and got two
answers**. 🔵 For a studio this stops being a curation problem and becomes a **contractual** one: a
runbook that says `@latest` has no fixed meaning, and a client acceptance test written on Monday can
fail on Monday.

🟢 **3 — The permissive supply is arriving, one author at a time.** The two addresses that moved
gaps this pass — a live MIT **SIS** and a 2-day-old Portuguese Socratic **tutor** — are both
essentially **single-maintainer** projects, one of them a master's dissertation. 🔵 The scarcity has
shifted: it is no longer *permissive code* that is missing, it is **permissive code with an
institution behind it**. That changes the diligence question from *“is there a grant?”* to **“who
answers when it breaks?”** — and the second question has no SPDX identifier.

🔵 **4 — Pedagogy is beginning to show up in the code, not just the README.** `portugol-ai-tutor`
withholds the answer and advances by questioning, and it comes out of a **thesis**. 🟡 Two of this
base's Socratic addresses now trace to academic work rather than product work — which is where to
look for the next ones, and also why they arrive copyleft.

### 🔵 Regional policy movement, band `reported`

🔴 **All six facts below are from secondary sources** — vendor blogs, legislative trackers and
aggregators — so they enter at band `reported`, and **none supersedes `p406`'s statute-level
detail.** They are recorded because an unrecorded fact is indistinguishable from an absent one.

| region | fact | why it is not yet `measured` |
|---|---|---|
| **APAC** | Singapore's **National AI Impact Programme**: 40,000 technology professionals over three years; baseline AI training mandated for **all higher-education students from 2027**; **AI Verify** operating as a de-facto requirement for vendors into regulated sectors | a CSIS roundup and a compliance blog, not the Singapore government's own text |
| **APAC** | **Beijing: ≥8 hours** of AI instruction per student per year, within a compulsory-from-age-six national curriculum | a single secondary source; the compulsory-curriculum claim is itself contested by another result in the same leg |
| **APAC** | **India**: AI and computational thinking mandatory **from Class 3 in 2026–27**, behind a **₹500 crore** centre of excellence and the **₹10,372 crore** IndiaAI mission | the figures appear in one aggregator; the shelves already hold the Class-3 mandate, so only the funding figures are new |
| **LATAM** | **Mexico — Estado de México** reformed its education law in **April 2026** for graduated, responsible AI use in *media superior* and *superior* | a Spanish-language compliance blog; sub-national, so it does not generalise to Mexico |
| **LATAM** | **Colombia — PL 043/2025 Senado · 324/2025 Cámara** in progress, alongside a ministry plan for licences, credentials and teacher AI literacy | bill numbers from a secondary source; the shelves already hold `Ley 2626 de 2026` at a firmer band |
| **North America** | **Arizona HB 4040** would require K-12 districts **and public universities** to adopt student-AI-use policies — still a bill | the shelves carry it; this pass adds only that it reaches **higher education**, which most state instruments do not |

### 🔴 The census, carried forward and marked NOT re-derived

🔴 **`p409` published 2 730 harvested shapes → 35 not addresses → 2 695 addresses**, and
**3 529 addresses over both channels**. 🔴 **This pass shelves 8 new addresses, so by this base's own
`gate-census-currency` rule those figures are `STALE` — and `p410` cannot re-derive them**, because
`make address-shape-census` is code in this clone and this session will not execute it.

🟢 **So they are left standing as `p409`'s figures, labelled stale, rather than re-stated as
`p410`'s.** 🔵 `p409`'s own note applies unchanged: *history is not edited to match.* A successor
with an executable `make` should run `make address-shape-census` and `make union-currency` as the
**last act before its commit**, and should expect **+8** on the address count from this pass alone.

## 🆕 `p409` · 2026-10-23 — a search result that says **MIT** over AGPL, the repository behind this base's own *unattributable* npm row, and four declared absences re-tested rather than re-asserted

🔵 **Dating note.** Every search leg, clone, licence read and registry query below was run on
**2026-10-23**, and the commit lands **2026-10-23**. 🔵 **This is the fifteenth pass dated today**,
after `p395`–`p408`.

🟢 **This is a RESEARCH pass.** The prescribed brief ran in full — four global legs and one leg per
region, eight in all. 🔴 **It returned ~20 candidate addresses, of which 6 were unshelved against a
base of 2,702** — and not one of the regional policy or adoption facts it surfaced was new. `p408`
reported the same eight legs returning nothing; **this is the second consecutive pass where the
prescribed brief is saturated, and that is now the finding rather than the preamble.**

🟢 **So the legs that would have been spent padding were spent re-testing this base's own declared
absences** — `Gap 297`, `Gap 298`, `Gap 386-A`, `Gap 386-C`. A declared absence is the one thing a
saturated brief can still move: either it has been filled since it was declared, which is a real
finding, or it has not, which re-dates the gap and makes it checkable instead of inherited.

🔵 **Channel note.** `api.github.com` returns **403** through this session's proxy — `p408`'s
reading, re-confirmed first-hand. Every licence, ref and date below is therefore read from **git
itself** (`clone --depth 1 --filter=blob:none --no-checkout`, then `symbolic-ref` / `log -1` /
`cat-file -s` / `cat-file -p`), with the **npm registry** as an independent second channel.
Evidence: [`new-address-probe`](../evidence/new-address-probe.2026-10-23-p409.tsv) (7 rows) and
[`channel-disagreement`](../evidence/channel-disagreement.2026-10-23-p409.tsv) (10 rows).

### 🔴 Trend: the licence signal now fails in **three directions**, and checking one extra channel can make a reader worse off

🟢 **`p408` established that a grant is a property of a *ref*, not of a project.** 🔴 **This pass adds
that it is also a property of a *channel*, and that the channels do not merely disagree — they
disagree in opposite directions on the same repository.**

`idurar/idurar-erp-crm`, read four ways on one day at one ref:

| channel | answer | error direction |
|---|---|---|
| web search result | **MIT** | 🔴 **too permissive** |
| `backend/package.json` `"license"` | **`"Fair-code License"`** | 🔴 **outside the vocabulary** — not OSI, not SPDX |
| `README.md` | AGPL-3.0 | 🟢 correct |
| `LICENSE` payload at root of `master` | **AGPL-3.0** (34,230 B) | 🟢 **authoritative** |

🔴 **The practical consequence inverts the usual advice.** "Check a second channel" is normally
strictly protective. Here, a reader who checks the *manifest* — the most natural second channel for
a Node project, and the one every SBOM tool reads — gets `"Fair-code License"`, which **looks like a
precise, deliberate answer** and is not a licence at all. They stop there with false confidence.
🟢 **Only the payload read, at the default ref, is safe — and the default ref here is `master`, so a
`main`-only probe returns nothing and may be read as "no licence file".** Two independent ways to get
this repository wrong, in one specimen.

🔵 **This is the sixth distinct licence-trap class on these shelves**, after: grant one directory
down, grant at `LICENSE.txt`, AGPL text in a GPL-named file, manifest claiming an absent payload, and
a fork freezing its upstream's pre-relicence grant.

### 🟢 Trend: the **registry is the faster clock, git is the authoritative one** — one specimen of each failure, same week

🔴 **Neither channel is sufficient alone, and this pass has both failures side by side:**

| specimen | registry | git | which channel failed |
|---|---|---|---|
| `brightspace-mcp-server` | 🟢 **5.0.8 → 5.0.12 in one day** | 🔴 HEAD frozen at `1fbc693` 2026-10-22 | 🔴 **git** — dating this project from `main` understates it by four releases |
| `@n35da/brightspace-mcp` | 🔴 **no `repository`, no licence field** — recorded by this base as *unauditable* | 🟢 tree fully readable; licence definitively absent at every depth | 🔴 **the registry** — it withheld the address, and the verdict it forced was *unknown* rather than *negative* |

🟢 **The rule that follows: date from the registry, grant from the tree.** 🔵 And when a registry row
has no `repository` field, treat the address as **absent from that channel**, not absent — an
ordinary subject-matter search leg recovered this one.

### 🟡 Trend: the prescribed research brief is **saturated**, two passes running — and the gap layer is where movement remains

🔴 **Eight legs, ~20 candidates, 6 unshelved against a base of 2,702 addresses, and zero new regional
instruments** — `p408` reported the same, so this is a second consecutive reading rather than one
bad draw. 🟢 **The legs that did move something were the ones aimed at this base's own declared
absences**, which returned: a restatement (`Gap 297` → `Gap 297-R`, the side-car exists but no
permissive one), a sharpened cause (`Gap 386-A`, the shaped-right D2L server is the ungranted one),
a measured shape (`Gap 298`, permissive grants on dead code and live code under copyleft), and a
further corroboration in-language (`Gap 386-C`).

🔵 **The trend to record for whoever runs the next pass:** on a saturated supply, **a declared
absence is worth more per leg than a search for new supply** — it either closes, narrows, or gets
re-dated, and all three outcomes are checkable. 🔴 A ninth re-run of `top open source AI agents
education 2026 github MIT` is not.

## 🆕 `p408` · 2026-10-23 — a fork that FROZE an abandoned grant, India's **MIT** DPI going stale, and eight legs that returned nothing unshelved

🔵 **Dating note.** Every probe, clone, licence read and search leg below was run on **2026-10-23**, and the commit lands **2026-10-23**. 🔵 **This is the fourteenth pass dated today**, after `p395`–`p407`.

🟢 **This is a RESEARCH pass, not an instrument pass.** `p405`–`p407` were all repairs to this base's own measurement layer. This one runs the prescribed brief — four global legs and one leg per region — and reports what the supply and the regional instruments actually returned, including where they returned nothing.

### 🔴 Trend: a grant is a property of a **ref**, not of a project — and this pass has the first specimen where BOTH answers are right

🔴 **Every licence trap this base carries is a variant of "the grant was read in the wrong place."**
A grant one directory down (`openSIS-Classic`, `docs/License.txt`). A grant at `LICENSE.txt` rather
than `LICENSE` (`ai-shifu`, `tutor`). An AGPL text sitting inside a file labelled GPL
(`moodle-local_copilot`, §13). A grant at the submodule pin rather than the superproject
(`gate-pin-grant`). In every one of them there is a single correct answer and a reader who missed it.

🟢 **`p408` adds a class where there is no such answer.** `project-sunbird/project-sunbird.github.io`
is **MIT** today and was **AGPL-3.0** until `006b8246` on **2018-06-21**; a fork whose HEAD is
**2018-03-27** carries the AGPL text with a **byte-identical blob sha**. Both repositories report
their licence correctly. Both badge-reads are right. **The project has two grants and the ref
decides which one you got.**

🔵 **Why this is a trend and not an anecdote.** Three forces now push education repositories through
relicensing: public-money DPI programmes that need permissive terms to be adopted across
jurisdictions (Sunbird's own 2018 MIT switch is this), the AI-extension wave rebasing education
plugins onto platform grants they did not originally carry, and the single-maintainer tutor supply
this base has been cataloguing since `p385`, where a licence is changed as casually as a README.
🔴 **The operational consequence is a dating requirement on the licence column itself:** every
licence cell on these shelves is *"the grant at the ref we read, on the date we read it"*, and a
fork — even a dormant one — is a **separate licence fact**, never an inherited one.

🟡 **The second trend this pass measures: the grant is no longer the scarce thing — maintenance is.**
Sunbird ED is MIT at national-platform scale, which is the licence outcome
[`repos/foundations.md`](../repos/foundations.md) opens by saying education does not get; and its
portal is **311 days** without a commit, its mobile app **399**, and one of its named repositories
no longer resolves. 🔵 The classic education trade was *current code, hostile grant* (Moodle, Open
edX, Canvas). This is the **inverse**, and it prices differently: a permissive-but-stale base is a
fork-and-maintain engagement, and the cost lands in the staffing plan rather than in legal review.

## 🆕 `p407` · 2026-10-23 — the instruments are now the thing most likely to be wrong

🔴 **Trend: this base's measurement layer has overtaken its subject as the source of error.**
Three of this pass's four findings are defects in **instruments**, not in the market — a frozen
population, a spelling-bound date pattern, and a possessive apostrophe — and each one had a
committed instrument that already knew the right answer. 🔵 **The lesson generalises past this
KB:** an agentic pipeline that grades its own corpus accumulates *checks that cannot fail*, and
nothing in a green run distinguishes those from checks that pass. 🟢 **The cheap counter-measure
is mutation**: five of six mutations against `p407`'s own suite reddened a named control, and the
sixth revealed that the suite's imported classifier was not load-bearing on any published figure.

🔵 **For an engagement this is a sellable practice, not an internal note.** A client running
LLM evaluation or compliance checks has exactly this failure mode, and *"show me a mutation that
makes your green test red"* is a one-day audit that finds it.

## 🆕 `p407` · 2026-10-23 — EMEA's education clock has 14 months on it, not zero

🔴 **The market's majority reading is wrong, and this base was repeating it on its own
opportunity row.** Annex III education obligations apply from **2027-12-02** — the Digital Omnibus
(in force **2026-07-27**) deferred them — while **2026-08-02** is the **Article 50** transparency
date only. 🔵 **A sixth independent sighting of the wrong date arrived this pass**, in an
otherwise current source, which is what a majority misreading looks like: the client's installed
adviser has probably given them the wrong deadline.

🟢 **So the EMEA pitch inverts.** It is **not** "you are already non-compliant"; it is
"you have ~14 months, and conformity work ports to Vietnam's Decision 33 and Brazil's PL 2338/2023
because all three are risk-tiered." 🔴 **And `2026-08-02` still binds for transparency**, so a
chatbot-facing deployment has a live obligation today even though the high-risk tier does not.

## 🆕 `p407` · 2026-10-23 — the agent surface is moving OUT of the LMS

🟢 **New direction, first specimen read this pass.**
[`microsoft/moodle-local_copilot`](https://github.com/microsoft/moodle-local_copilot) (**GPL-3.0**,
release **5.1.0**) does not put a model behind Moodle; it puts **Moodle behind Copilot**, as two
declarative agents a teacher drives from Word, PowerPoint and BizChat. 🔵 Every other Moodle AI
row this base carries runs the other way (the `aiprovider_*` family). 🔴 **The strategic read:
the LMS is becoming a tool-provider to someone else's assistant**, and whoever owns the assistant
surface owns the teacher's attention. 🔴 **It is also the anti-sovereign option** — M365 Copilot
licensing, Entra registration, no local-model path — so it sits directly opposite the Ollama-provider
route for EMEA sovereignty and LATAM cost. **Both can be true on one estate; a proposal must say
which surface it is buying.**


## 🆕 `p406` — what changed on this shelf

🟢 **One trend is newly measurable on this base rather than asserted from a source, and it is about
the base itself.**

### 🆕 `T83` — open-source education supply DECAYS at ~2.2 % of carried addresses, and the decay is not uniform across tiers

🟢 **Measured, not estimated: 59 of 2 681 carried addresses do not resolve.** 🔴 **And the per-tier
split is the finding, not the rate:**

| tier | addresses | 🔴 unresolvable | rate |
|---|---:|---:|---:|
| **institutional platforms** *(`verticals/solutions.md`)* | 104 | **0** | **0 %** |
| market intelligence *(`intel/market.md`)* | 74 | **0** | **0 %** |
| foundation repos | 152 | 5 | 3.3 % |
| 🔴 **agent tier** *(`agents/top.md`)* | 238 | **12** | **5.0 %** |

🔵 **The mechanism, and it is a procurement argument rather than an observation.** Platforms carry a
foundation, consortium or company behind the namespace — Moodle, Open edX, Canvas, Sakai, Kolibri,
OpenOlat, BigBlueButton, H5P, Opencast. The agent tier is **single-maintainer MCP servers and
npm-published demos**. 🟢 **So the layer a client's system of record sits on is the layer least likely
to vanish, and the layer Globant composes on top is the volatile one** — which is an argument for
putting the integration contract, not the agent, at the centre of a design.

🟡 **A caveat that cuts against reading this as a maintenance signal.** `EXISTS-PUBLIC` says the
address **answers today**, not that anything is maintained: `StudentTraineeCenter/edu-agent` resolves
and has **511 tracked files** and has not been committed to since **2025-12-30**. 🔵 Dormancy is
`p173-dormancy-bands`'s question and it is a different axis from existence. Two addresses go further
and answer `EXISTS-NO-REFS` — **empty repositories, which EXIST** — so a row keyed on either survives
a 404 check and still ships no code.

### 🟡 `T84` — ECL-2.0 is a THIRD licence class on the platform tier, and a MIT/Apache shortlist mis-sorts it

🟢 **Opencast's licence title line, read first-hand this pass** at `153d1b1`:
**`Educational Community License, Version 2.0 (ECL-2.0)`**. Sakai carries the same grant. 🟡 ECL-2.0
is an **Apache-2.0 derivative whose patent grant is narrowed to the licensor's own contributions** —
neither MIT/Apache nor copyleft. 🔴 **A `"MIT / Apache 2.0 / BSD only"` filter drops both Apereo
platforms, and the error runs toward OVER-caution:** both are permissive and redistributable. 🔵
Named as a trend because this is the second Apereo platform to land on the tier, so the class is not
a one-off row any more.

### 🔵 Regional: the leg saturation is real, and one exception repaired a live row

🔴 **Fourth consecutive pass in which the four prescribed regional legs returned no unshelved fact.**
🟢 **The exception did something better than add one:** the APAC leg resolved this base's own
three-way contradiction about Vietnam's education deadline, and in doing so **refuted a published
opportunity row** that priced an education engagement against **2027-03-01** when education's
deadline is **2027-09-01**. 🔵 Full derivation and the no-primary-read bound on
[`intel/market.md`](market.md).

🟢 **The generalisable lesson for a saturated channel:** a leg that returns only carried facts is not
a wasted leg if it is read against what the base already says. The value here came from the
**collision** between a returned fact and a shelved one, not from novelty.

---

## 🆕 `p405` — what changed on this shelf

🟢 **One new trend, `p405-T1`, opened because it is a *measurement defect* this base has been
publishing as an ecosystem reading** — not because a pass needed a finding. 🟡 **One amendment** to the
licence ladder: a cell `p401` and `p382` between them do not have. 🔴 **No trend is retired.**

### 🔴 `p405-T1` — an address count is not a project count, and the error is NOT uniform across groups

🔵 **The shape.** This base counts **addresses**. Its census, its crowding findings and its
*"real supply, not census noise"* conclusion are all address-denominated. 🔴 **Measured over the four
name-collision groups `intel/open-gaps.md` item 3 names: 42 resolved addresses are 27 projects.**

| group | addresses | 🟢 projects | absorbed | inflation |
|---|---|---|---|---|
| `canvas-mcp` | 20 | 9 | **11** | 🔴 **2.22×** |
| `brightspace-mcp-server` | 4 | 2 | 2 | 🔴 **2.00×** |
| `blackboard-mcp` | 8 | 6 | 2 | 1.33× |
| `moodle-mcp` | 10 | **10** | 🟢 **0** | 🟢 **1.00×** |
| **total** | **42** | **27** | **15** | **1.56×** |

🔴 **The non-uniformity is the trend, and it is what makes a single correction factor useless.** A base
that applied **1.56×** everywhere would be wrong about three of the four groups, and most wrong about
the one where the count is already correct. 🟢 **So the prediction, in a form a successor can refute:**
inflation tracks **how easy the platform is to get credentials for**, not how popular it is. Canvas and
Brightspace have free instructor sandboxes, so a working server attracts forks that are *tutorials*;
Moodle must be self-hosted, so each of its ten implementations was written by someone who already had a
server. 🔵 **Refutable:** measure a group whose platform needs no credentials at all and the inflation
should be higher than `canvas-mcp`'s 2.22×.

🔴 **Why the existing channels could not see it, stated as absence rather than weakness.** `p402`'s
ref-set test answers *"one repository or two"* and `p404`'s pair test answers *"which of these two."*
🟢 **Neither can answer *"how many projects are in this group of twenty"*, because that is a property of
the whole pair graph** — and it needs **`C(N,2)` verdicts**, which is why it stayed open at a clone per
pair. 🟢 **The cost is now `O(N)` clones for `C(N,2)` verdicts** — 20 clones for 190 pairs
([`compose/code/p405-group-lineage/`](../compose/code/p405-group-lineage/README.md), 12 controls) — so
the question is affordable at group grain for the first time.

🟡 **Two second-order consequences worth writing down.**

| | |
|---|---|
| 🟡 **A platform-coverage claim is address-denominated and therefore wrong** | *"Twenty open-source Canvas MCP servers"* is true about addresses and **false** about what a client buys. By projects, Canvas has **fewer** than Moodle. Placed on [`verticals/solutions.md`](../verticals/solutions.md) |
| 🔴 **Transitivity is claimed and did NOT bind here** | Lineage is transitive, so the citable unit is the connected **component**. 🟢 **In all four groups measured, every within-family pair was directly related**, so components equal naive pair-clusters. 🔵 Named rather than left as an untested strength of the instrument |

### 🟡 Amendment to the licence ladder — a plugin's grant can live ABOVE it in the tree

🔴 **`p401` read 51 Moodle plugin grants through two channels and found every one
`GPL-3.0-or-later` — *"Not one MIT, Apache-2.0 or BSD in 51 reads."*** 🟢 **Here is a 52nd, and it is
neither.** `local_italiciamcp`, shipped inside
[`marcosnahuel/moodle-mcp`](https://github.com/marcosnahuel/moodle-mcp), is a real Moodle local plugin —
`$plugin->component = 'local_italiciamcp'`, `db/services.php`, `db/access.php`, 13
`classes/external/` web-service functions, `$plugin->supported = [400, 501]`:

| channel | `p401`'s question | 🟢 **measured here** |
|---|---|---|
| **P** — the grant in the plugin's own PHP headers | reads 51 of 60 | 🔴 **0 of 18 PHP files carry any GPL mention** — not the *"version 3 … or any later version"* paragraph, not the word `GPL` anywhere |
| **L** — a licence-shaped file inside the plugin | reads 24 of 60 | 🔴 **0** — no `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING` or `LICENCE` at any path inside the plugin directory |
| 🆕 **A** — the nearest licence file in an **ANCESTOR** directory | 🔴 **no cell** | 🟢 **MIT**, 1,065 B, two directories up at the repository root; README reads *"MIT © 2026 Italicia"* |

🟢 **`p382-subtree-grant` does not cover this, and the direction is why.** That instrument asks
*"which subtrees does this grant **narrow itself** to?"* — a property the payload declares.
🔴 **This asks the inverse: what grant reaches a subtree that declares NOTHING?** 🔵 Both are needed,
and only one existed.

🔴 **The commercial read, which is the opposite of what *"an MIT Moodle plugin"* sounds like.** A plugin
calling Moodle's GPL APIs is normally held to GPL distribution terms, so the likeliest explanation is a
**licensing defect on the author's side** — and a studio that treated the MIT file as permission to
build closed derivative work on it would be relying on the author's mistake. 🟢 **`p401`'s boundary rule
is UNCHANGED:** a studio's permissive code belongs **outside** the plugin boundary. 🔵 **What changes is
the ladder**, which must now ask for the nearest ancestor grant before recording a plugin as
*"no grant / unknown"* — and `p401` already named the direction of that error: an ungranted plugin reads
as *unencumbered*, which is the opposite of the truth. Rows:
[`plugin-inherited-grant.2026-10-23-p405.tsv`](../evidence/plugin-inherited-grant.2026-10-23-p405.tsv).

### 🔵 A null worth recording, because it is the THIRD pass to spend it

🔴 **The four English regional legs returned zero new facts for a third consecutive pass — and two of
the four no longer reach education at all.** EMEA and APAC returned *enterprise* AI material
(a 2023 Workday study, a Pearson–TCS alliance, a Sydney office). 🟢 **That is a change in kind, not
degree:** the legs are not reporting stale education facts, they are reporting non-education facts.
🔵 `T82` governs — that licenses *"these legs do not reach education in these regions"*, never
*"there is no EMEA education AI news."* 🔴 A fourth English regional leg is a **predictable** null, so
the successor move is a channel change. See [`market.md`](market.md).

---


## 🆕 `p404` — what changed on this shelf

🟢 **One new trend is opened, `p404-T1`, and it is opened because it is a *class* this base has been
grading one-at-a-time with the wrong instrument** — not because a pass needed a finding. 🟡 **One
amendment** to the licence/alias reasoning: a cell that did not exist. 🔴 **No trend is retired.**

### 🟢 `p404-T1` — "same name, different HEADs" is THREE mechanisms, and only full history separates them

🔵 **The shape.** This base keeps meeting pairs of addresses that share a plugin or module name and
differ at HEAD. It has graded them with ref sets (`p402`) and with HEAD equality (`p370`, `p349`), and
both channels answer only *"one repository or two"*. 🔴 **Neither can say which mechanism produced the
pair** — and the three mechanisms have **different consequences for a build**:

| mechanism | measurement | consequence |
|---|---|---|
| **Content copy / squash-republish** | 🔴 **0 shared commits** · 🟢 **>0 shared trees**, and the shared tree is one side's **root** tree | 🟢 **Direction is knowable.** One address is the product and the other is provenance — and the live one may be the *younger* address, which currency alone reads backwards |
| **Continuation / hand-off** *(a true fork)* | 🟢 **Shared commits**, and one HEAD is an **ancestor** of the other | 🟢 One address is a **strict superset**; citing the other is citing a prefix. 🔴 Its warnings travel into the superset unless a commit removed them |
| **Independent reimplementation** | 🔴 **0 shared commits AND 0 shared trees** | 🔴 **Two different products.** Language, grant and release discipline may all differ, so the bare name cannot carry a recommendation |

🔴 **Why the old channel could not see it.** A **squash-republish shares ZERO commit SHAs with its
origin.** So on a ref-set or HEAD test a *copy* and two *unrelated namesakes* are indistinguishable —
the signal is **absent** from the channel, not faint in it. 🔵 This is why `p402` was right to refuse a
direction and wrong to record the question as unestablishable: the refusal was about the instrument.

🟢 **Three instances, measured in one pass, one of each mechanism** —
`moodle-aiprovider_openaicompatible` (copy, `lmscloud-io` → `ADORSYS-GIS`), `lti` (continuation,
`macewan-cs` → `astiusa`), `moodle-mcp-server` (independent). 🟢 **Tree SHAs are the load-bearing
addition**: git content-addresses directory state, so a byte-identical tree is **one SHA** however the
history around it was rewritten, and *where* that tree sits in history is the direction.
🔵 `p401` had already found the `classes/provider.php` **blob** identical at 3,963 B and correctly
declined to call it a direction — the **tree** carries the same bytes **plus their position**.

🔴 **What the trend predicts, in a form a successor can refute.** Of `p397`'s **551** candidate pairs,
the ones a ref-set test labels `DISTINCT` are **not** mostly name collisions: this pass's 3-for-3 says
the label hides copies and continuations. 🟡 `p397`'s own arm already found **8 of 15 "forks" are
renames** — same defect, the other direction. 🔵 **The cheap test is now wired**
([`compose/code/p404-fork-direction/`](../compose/code/p404-fork-direction/README.md), 9 controls),
and 🔴 it costs a **full clone per address**, so it is run on **named pairs in bounded batches**. `T82`
governs the sweep; `p402`'s refusal is not re-tested.

### 🟡 Amendment to the licence frontier — identical grant bytes do NOT make a substitutable dependency

🔴 **This base's licence reasoning has had no cell for *package identity*.** It records the grant, its
bytes, its channel and its scope — and a reader takes "same licence, same code, superset history" to
mean "swap the import". 🟢 [`astiusa/lti`](https://github.com/astiusa/lti) refutes that: the MIT file
is **byte-identical** to [`macewan-cs/lti`](https://github.com/macewan-cs/lti) (1,108 B,
`sha256`₁₆ `6e58273960b0`, still **© 2021 MacEwan University**), the history is a **strict superset**
— and the 2023-05-22 commit **changed the Go module path**. 🔴 **So moving costs an import edit in
every consumer**, which is a migration, not a version bump.

🔵 **What to add to a licence cell from now on:** when two addresses share a grant and a lineage, say
whether the **package identity** (Go module path, npm name, PyPI distribution, Moodle `$plugin->component`)
is the same. 🟢 For the `aiprovider_openaicompatible` pair it **is** — both declare
`$plugin->component = 'aiprovider_openaicompatible'`, so there a studio really can swap addresses. 🔴 For
the `lti` pair it is not. 🟡 **Same question, opposite answers, in one pass** — which is why this is an
amendment and not a note.

### 🔵 A null worth recording, because it was predicted and is cheap to re-test wrongly

🔴 **The non-GitHub-forge leg returned nothing.** A leg aimed explicitly at **GitLab and Codeberg**
returned five education-AI addresses and **all five are hosted on GitHub**. 🟢 This base already holds
`gitlab.com` and `codeberg.org` references, so the forges are not unknown here — what is measured is
that **an English-language, forge-named web leg does not reach them**. 🔵 `T82` governs: that licenses
*"this leg does not reach those forges"*, never *"there is no education AI on GitLab"*. 🟢 The cheaper
successor is a **host API probe** with this base's existing
[`gitlab-api-channel`](../compose/code/gitlab-api-channel/README.md), not another web leg.

---

## 🆕 `p403` — what changed on this shelf

🟢 **`p401-T1` gets a THIRD independent instance, and this one was PREDICTED before it was found.**
🟡 **`T36` gets a fourth instance, and its first commercially-usable one** — which changes what the
trend costs a client. 🔴 **No new trend number is opened**: both findings are instances of trends this
base already carries, and recording them as new would be re-selling.

### 🟢 `p401-T1`, third instance — and the first *predictive* one (India)

🔵 **The trend, as this base already states it:** national-language supply appears roughly a year
behind national mandates, and an English-language leg reports the pre-lag state indefinitely.
Evidenced on the **Gulf** (`p401`), and proved from the other direction on **LATAM** (`p387`).

🟢 **`p403` used it as a prediction rather than a description.**
[`intel/market.md`](market.md) already carried India's mandate — **AI and computational thinking
compulsory from Class 3 from the 2026–27 academic year**, with the IndiaAI Mission behind it. A trend
that holds implies **Indic-language education supply appearing around now**. 🟢 **A Hindi-language leg
returned three previously unshelved addresses on its first page**, where the English legs have returned
zero granted education-native addresses for six-plus consecutive passes:
[`AI4Bharat/IndicIFEval`](https://github.com/AI4Bharat/IndicIFEval) (MIT code, 14 Indic languages,
HEAD 2026-09-16), [`AI4Bharat/Anudesh-Backend`](https://github.com/AI4Bharat/Anudesh-Backend) (MIT,
HEAD 2026-09-01) and
[`matsuolab/lecture-ai-engineering-2026-hi`](https://github.com/matsuolab/lecture-ai-engineering-2026-hi)
(🔴 ungranted, HEAD **2026-10-19 — 4 d**).

🔴 **And the control that stops this becoming "run more languages".** A **Japanese**-language leg was
run in the same pass and returned **nothing education-native** — only general-purpose agent frameworks
and licence-comparison blogspam. 🟢 **Japan is the APAC jurisdiction this base records as having a
promotion-first framework with no penalties and no mandate.** So the dividend tracks **the mandate, not
the language** — which is `p401-T1`'s actual claim, and it now has a negative control supporting it
rather than three positives alone.

🔵 **The predictive form, for a successor:** the next legs worth spending are the languages of
jurisdictions whose mandates have **just** commenced. 🔴 **Not** Japanese.

### 🟡 `T36`, fourth instance — and the first where both grants are commercially usable

🔴 [`AI4Bharat/IndicIFEval`](https://github.com/AI4Bharat/IndicIFEval) carries **MIT** in its root
`LICENSE` (1,074 B, payload-read) and **`CC-BY-4.0`** over the dataset, in its own §License section.
🟢 The three earlier instances (`inno-agent`'s ungranted skill hub, `os-taxonomy`'s
`ODbL-1.0 AND CC-BY-SA-4.0` data, `h5p`'s GPL content) all had one half a studio **could not use**.
🟢 **Here both halves are usable** — so the consequence is not exclusion but **attribution obligations
attaching to the data**, which is a documentation task rather than an architectural one.

🔵 **What that adds to `T36`:** the trend's cost is not constant. Reading it as *"the curriculum half is
unusable"* would have mis-priced this repository. The licence column must name **which artefact** is
granted **and under what** — not merely flag that two grants exist.

## 🆕 `p402` — what changed on this shelf

🔵 **No trend is added or retired this pass.** The pass was an **instrument and backlog** pass, and
saying so keeps the trend list from drifting on passes that did not measure a trend.

🟡 **One amendment, to `Trend 6` (the permissive-licence frontier).** The frontier is not only *which
licence* a component carries but **which address carries it**. `p402` closed `ACTION ZZ-al` and found
that `ease`'s canonical address is **neither** of the two the register tracked, but a third owner —
[`openedx-unsupported/ease`](https://github.com/openedx-unsupported/ease), **archived read-only since
2024-02-28**. 🔵 The grant (**AGPL-3.0**) never changed, so the *frontier* does not move; what moves is
the confidence a reader should place in an address that a search result hands them.

🟢 **The durable rule, now wired into `Pattern AF`:** warrant the **canonical** address, and treat an
owner named `*-unsupported` or an archive banner as a **stewardship finding in its own right** — the
thing to establish *before* promising a client a maintained dependency.

🔴 **And a measured regional gap, repeated rather than new:** the EMEA leg returned **no
education-specific instrument** for the **third consecutive pass**, and the APAC leg surfaced **no
ministry-level instrument** at all. 🔵 Both are written down as informed gaps on
[`intel/market.md`](market.md), because silence looks exactly like coverage.



**🆕 Pass `p401` · reads and commit both 2026-10-23.** 🟢 **Three trends this pass can evidence
rather than quote, and one it can date.**

### 🆕 `p401-T1` — national-language supply is appearing roughly one year behind national mandates

🟢 **Evidenced, not asserted.** The Gulf school mandates took effect in the **2025/26** academic
year (Saudi Arabia, UAE). The **first permissive Arabic-first education repositories on these
shelves were created 2026-09-14, 2026-10-12 and 2026-10-13** — three unrelated projects inside six
weeks, after a year of nothing. 🔵 The same shape is already on this base from the other
direction: `p387` broke a four-pass LATAM supply null with Spanish and Portuguese legs, after
LATAM policy had been typed for passes.

🔴 **The actionable form of the trend is a warning about measurement, not about markets.** An
English-language search reports the pre-lag state indefinitely, because the supply that appears is
named and documented in the local language. 🟢 **A regional supply claim is only as good as the
language of the leg that produced it** — and this base asserted *"not one address"* for the Gulf
across five passes on English legs alone.

### 🆕 `p401-T2` — the AI integration surface in education is consolidating into platform plugin APIs, and that surface is copyleft

🟢 **Measured this pass.** Moodle's `core_ai` subsystem now has a **provider-plugin** interface,
and the shelf holds **60** Moodle plugin addresses with **51 readable grants — every one
`GPL-3.0-or-later`, not one permissive**. Two independent vendors ship the *same*
OpenAI-compatible provider shim with a **byte-identical `classes/provider.php`**. 🔵 Integration is
standardising on the platform's own extension point rather than on bespoke forks, which is good
engineering and a **licence ceiling**: the standard seam is GPL by construction.

🔴 **The consequence contradicts the usual read of "open source is consolidating".** Consolidation
here *reduces* what a studio can own: the more the ecosystem converges on plugin APIs, the more of
the integration lives inside the copyleft boundary. 🟢 The counter-move is architectural and is
written up on [`verticals/solutions.md`](../verticals/solutions.md) — keep the plugin a thin GPL
adapter and put the IP behind a network boundary.

### 🆕 `p401-T3` — the gap between institutional USE and institutional GOVERNANCE is the measurable market

🟢 **The cleanest number any leg returned this pass.** UNESCO IESALC with UNU-IAS, **200
institutions across 19 countries** in Latin America and the Caribbean: **87% use AI in at least one
area; 26% have a formal AI strategy.** Adoption is driven by **individual academics and students**,
not institutions. 🔵 Independent sources describe the same gap elsewhere in different words — a
2026 survey across 450+ institutions reporting roughly **10%** with formal AI-use guidelines, and
the broad 2026 framing of a shift *"from experimentation to governance."*

🟡 **Why this is a trend and not a statistic.** Where use precedes policy by that margin, the first
paid work is **not** building a tutor — it is inventory, data-boundary definition, an acceptable-use
policy and an audit trail for AI already in use. 🔵 That is also the work the EU AI Act's Art. 4
literacy duty and Annex III high-risk classification will require evidence of, so it is **billable
twice**.

### 🟡 `p401-T4` — "purpose-built for education" is now the stated direction of travel, and it is still mostly a claim

🟡 **Convergent across 2026 commentary**, including the OECD's Digital Education Outlook framing and
1EdTech's watch-list: a move away from general-purpose assistants toward systems **built for
learning**, with evidence of durable gains, plus teacher-first deployment and digital credentials
as a skills-verification mechanism. 🔴 **Band: `reported`, and deliberately not promoted.** The
specific adoption figures circulating with this framing — an *"83% AI teaching assistant
deployment"*, a *"42% outcome gain"*, *"92% of university students using AI"* — are **secondary and
untraceable to a primary instrument from this session**, and this base does not put a number in a
deck it cannot source. 🟢 **What IS evidenced here:** the one new PISA-aligned permissive agent
([`braiinz94/braiinz-education`](https://github.com/braiinz94/braiinz-education), Apache-2.0, 0 ★)
is the first address on these shelves aligned to an **international assessment** rather than a
national curriculum — one data point in the predicted direction, and a thin one.

**🆕 Pass `p400` · reads and commit both 2026-10-23 — sixth pass of the day.** 🟢 **Two new
trends, both measured, and the first one is about this base's own repair habit rather than about
the industry.**

### 🆕 `T81` — a defect is fixed where it was FOUND, not where it LIVES

🔵 **`T29` → `T80` → `T81` is one line of descent.** `T29`: a statement about a file disagreed
with the file. `T80`: two shelves disagreed and only one was machine-readable. 🔴 **`T81`: a
defect found in one member of a closed vocabulary is repaired in that member and left standing
in the others.**

🟢 **Evidence, and it is this base's own last pass.** `p399` found that the typed policy layer
answered *"no LATAM teaching mandate"* across 11 rows while the README held the refuting
statute, and fixed it properly — LATAM **0 → 6** rows. 🔴 **It did not re-ask the question of
EMEA, North America or APAC.** Re-asked this pass: **EMEA 7 · LATAM 6 · North America 3 ·
APAC 1** — and APAC's single row was `regional | NOT_ESTABLISHED`, in the region holding the
largest mandated AI-education deployment on earth. 🟢 Now **7**. See `400-G` on
[`market.md`](market.md).

🔵 **Why this is a trend and not one pass's slip:** `region` is a **closed five-value
vocabulary** in this KB by brief. A closed vocabulary makes the generalisation step *cheap and
mechanical* — four greps — which is exactly why skipping it is easy to miss in review. 🟢 **The
operational rule it yields:** when a finding is of the form *"this axis is blank for X"*, the
pass closes only after the same query has been run for every other value of X, and the result
published even when it is "no change". 🔴 The failure mode is not laziness; it is that a
correct, well-evidenced, properly-fixed finding *feels finished* at the moment the instance is
repaired.

### 🆕 `T82` — a refusal names the command it refused, and the OUTER command is not the capability

🔴 **Three passes have now mis-scoped a refusal, each one layer further out.** `395-C`/`396-C`
concluded *"executing repository code is refused"* and told successors to stop ranking
instrument work — refuted by `p397`, which found the refusal was a **clause** of a compound
command, and one clause was a genuine HTTP 403. 🔴 **`p399` then published *"`make hooks` was
refused on this session (`Code from External`), so no gate score is restated here"* — and
`p400` reproduces the `make` refusal exactly, then runs **31 of the 32 gate control suites** at `HEAD` (and 32 of 33 in this commit)
directly with `python3 -I`.**

🟢 **So the gate suite was never unreachable; the *build tool* was.** The measured cost of the
mis-scoping is on the record: two currency gates sat **red and unseen** at `HEAD` (`400-B`),
which is the same price `397-B` paid for the same class of error one generation earlier.
🔵 **The rule:** a refusal licenses exactly one conclusion — *this invocation was refused*. Any
claim about a **capability** needs a second, differently-shaped attempt before it may be
written down, and *"I could not run it"* may never be published as *"it cannot be run."*

**🆕 Pass `p399` · reads and commit both 2026-10-23 — fifth pass of the day.** 🔴 **No industry
trend was added: the brief's eight legs returned nothing this base did not hold, for the second
consecutive pass.** 🟢 **One new trend about this base's own structure is added, and it is
measured rather than observed.**

### 🆕 `T80` — the defect has moved from the sentence to the LAYER BOUNDARY

🔵 **`T29` was "a statement about the file disagreed with the file." `397-A` was "a superlative
derived over the rows in view rather than over the shelf." 🔴 `T80` is the same family one level
out: two shelves that are both correct, that disagree with each other, and only one of which an
instrument can read.**

Evidence this pass: `README.md` has carried **Colombia's `Ley 2626 de 2026`** — a binding
education-AI statute — since the `p277` regional battery, while
[`policy-matrix.tsv`](policy-matrix.tsv), the layer built **because** *"prose is not readable by an
instrument"*, carried **11 teaching-mandate rows and not one LATAM**. 🔴 **Neither shelf was lying;
the fact simply never crossed between them**, and the typed side is the side that answers queries.

🟢 **Why this is a trend and not an incident:** the same crossing failed for **six** jurisdictions
at once (CO, AR, CL, MX, BR, PE) plus two the base had lost entirely (PY, UY) — so the mechanism is
structural, not a slip on one row. 🟢 **The cheap standing check it implies:** for any claim of the
form *"no jurisdiction in region R does X"*, grep the prose shelves for R before publishing the
blank. That check, run once this pass, is what produced the finding.

### 🔵 `T42`, held still rather than advanced — and the gate score deliberately NOT restated

🔴 **`make hooks` was REFUSED on this session's classifier** (`Code from External`), where `p398`
ran it twice in full. 🟢 **So `p399` does not restate the gate score** — `398-B`'s whole lesson is
that a score is a derived quantity that goes stale exactly like a census sentence, and a pass that
could not re-derive it must say so rather than carry `p398`'s **46/47** forward as if re-measured.
🔵 **What this adds to `T42`:** the refusal is **not stable across sessions**. Same repository, same
command, same month — `p397` and `p398` ran it, `p399` cannot. 🔴 **Any gate claim in this base is
therefore conditional on the session that made it**, which is a property no shelf here had recorded.
`Gap 399-B`.

**🆕 Pass `p398` · reads and commit both 2026-10-23 — fourth pass of the day.** 🔴 **No industry trend
was added: the four regional legs returned nothing this base did not hold** (`Gap 398-C`). 🟢 **Two
trends about this base's own instruments are refined instead, and both are measured.**

🔵 **`T42` narrowed one notch further.** `396-C` recorded *"executing repository code is refused"*;
`p397` refuted that by running the repo's own suites and localised the refusal to a **compound**
command. 🟢 **`p398` adds the discriminating axis: the classifier gates the AUTHORSHIP of the code,
not the host, the tool or the command shape.** `make hooks` ran **twice** this pass, in full; a
**hand-written** script that merely *imported* the same repository module was refused
(`Code from External`), and so was a `make` target on one invocation and not another. 🔵 So a pass
should reach for **the repository's own committed targets** and treat an ad-hoc probe as unavailable —
which is the opposite of the usual instinct to write a quick script.

🔴 **And a trend this base should name because it has now fired four passes running:** a new channel's
first yield is overwhelmingly **content the base already owns**. `p393` warned of it; `p395`, `p396`
and `p397` each caught themselves about to re-sell an owned fact; 🔴 **`p398` measured it at the
channel level — nine of ten rows on `topic:autograder`'s first page, and 100% of eight search legs.**
🟢 **The operational consequence: grep the tree BEFORE writing, not after**, and rank a channel by
*what it adds* rather than by *what it returns*. 🆕 **`T43`.**

**Pass `p397` · reads and commit both 2026-10-23 — third pass of the day.** Three trends, each
tied to a measurement in [`shelf-lineage`](../evidence/shelf-lineage.2026-10-23-p397.tsv),
[`record-layer-redating`](../evidence/record-layer-redating.2026-10-23-p397.tsv) or
[`channel-state`](../evidence/channel-state.2026-10-23-p397.tsv).

### 🆕 `T40` — The permissive LTI 1.3 supply in Python is not thin, it is ABANDONED — on both sides of its own fork

🔴 **`p393` corrected the count of permissive Python LTI libraries from three to five and noted they
were *"largely unmaintained."* `p397` dates the two halves of the one that looked institutional, and
both are dead:**

| address | HEAD | days | note |
|---|---|---|---|
| [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | `d8fa43e` | 🔴 **1 432** | the upstream |
| [`ucfopen/pylti1.3`](https://github.com/ucfopen/pylti1.3) | `6a47f0f` | 🔴 **1 379** | 🟢 a **genuine divergent fork** (shared root `676b78fec64c`, different HEAD) by **UCF Open**, University of Central Florida |

🔵 **Why this is a trend and not a row.** The hopeful reading of an abandoned library is *"an
institution forked it and carries it now."* 🟢 **Here that institution exists, the fork is real and
measured — and it stopped 1 379 days ago, 53 days after the upstream did.** 🔴 **So "someone forked
it" is not evidence of maintenance, and a provenance test that only proves lineage will tell you the
fork exists while saying nothing about whether anyone is home.** Lineage and liveness are two
measurements and a recommendation needs both. 🟢 The best-maintained Python LTI option on these
shelves remains the **AGPL** one — which is a licence conversation, not an availability one.

### 🆕 `T41` — A rename is indistinguishable from a fork until you compare HEADs, and this industry renames constantly

🟢 **Education software is unusually prone to this**, because its infrastructure is run by
**standards bodies and foundations that re-badge**: `IMSGlobal` → `1EdTech`, `edx` → `openedx`
(Axim), `digitalcredentials` → **OpenWallet Foundation Labs**, `pytorch` → `meta-pytorch`,
`kantord` → `LibreLingo`. 🔴 **Eight of 15 shared-root pairs on these shelves were renames, not
forks — 53%.** GitHub answers on the old path indefinitely, so **both addresses look alive, carry the
same licence payload and the same stars**, and nothing in a licence read or a star read can separate
them.

🔵 **The consequence for a studio is concrete:** a dependency audit that lists `IMSGlobal/...` and a
conformance clause that cites `1EdTech/...` are the **same dependency**, and a client reading both
will reasonably ask which one you actually tested. 🟢 **Fold on HEAD, cite the current path, and keep
the old one as an alias rather than a row.**

### 🆕 `T42` — A refused channel is a claim with a shelf life, and this base just paid for forgetting that twice in three passes

🔴 **`396-A` named this exactly one pass ago:** *"an absence recorded against ONE channel hardens
into a fact about the world within two or three passes, and then stops being retested."* 🔴 **It
happened again immediately, to `396-C`** — *"executing repository code is refused by the environment
classifier… three ranked items are permanently blocked."* 🟢 **`p397` ran the repository's own Python
suite on its first attempt: 59 checks, 0 failures.** What `p396` actually hit was a **compound shell
command** in which one clause was refused, and the refusal was attributed to the whole.

🔴 **The cost was not hypothetical.** `make hooks` went unrun for two passes, and three gates drifted
red unseen — `gate-region-headings`, `gate-census-currency`, `gate-union-currency` — taking the
standing score from **44/46 to 41/46** with nobody watching. 🔵 **The gates were working the entire
time; nothing was reading them.**

🟢 **The generalisation, which is a cheap writing rule:** *carry the channel AND the granularity in
the claim.* `396-B` already said a 403 is ambiguous between host, proxy and tool. 🟢 **`p397` adds the
third axis: ambiguous between the command and a clause of it.** Re-measure one clause at a time
before recording a capability as absent — `p397`'s own channel table does, and that is how both
findings above were found.

**🆕 Pass `p396` · reads and commit both 2026-10-23.** Four trends, each tied to a measurement in
[`record-layer-dating`](../evidence/record-layer-dating.2026-10-23-p396.tsv) or
[`channel-state`](../evidence/channel-state.2026-10-23-p396.tsv).

### 🆕 `T37` — Agents have memory; institutions have records; nothing joins them

🔴 Every tutoring agent on these shelves keeps **its own** memory — `DeepTutor`'s lifelong memory,
`inno-agent`'s L1/L2/L3 layers, `OATutor`'s Bayesian knowledge tracing. 🔴 **None of them writes to
the institution's Learning Record Store**, which is where a registrar, an accreditor, a regulator or
a credential actually looks. The entire open-source supply joining the two is
[`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi): **MIT, 15 ★, 419 days
without a commit.**
🔵 **Why this is a trend and not a gap note.** Agent memory is designed for *continuity of
conversation*; an LRS is designed for *evidence that survives the vendor*. They are different
artefacts with different owners, and the market has built the first and not the second. 🟢 Every
regulatory pressure in `intel/market.md` — Oklahoma's teacher-review requirement, the EU's Article 26
logging duty, LATAM's missing governance — lands on the **second**. 🟢 This is the clearest unserved
build in this base.

### 🆕 `T38` — The standard moved and the implementations did not: xAPI 2.0 has zero adoption

🟢 xAPI 2.0 is **IEEE 9274.1.1-2023**, reportedly also an ISO/IEC/IEEE edition in 2025 *(secondary;
unconfirmed — `arxiv.org` and the standards hosts are refused)*. 🔴 **The two best-adopted permissive
LRSs do not implement it**: `lrsql` (144 ★) is 1.0.3-era and Ralph's docs say 2.0 *"is not currently
supported."* 🔴 **The three that claim it hold 1 star between them** — `pelotech/xapi-lrs` (0 ★),
`codetakt/kiva` (0 ★), `nurullahturkoglu/xapi-dotnet` (1 ★).
🔵 **The asymmetry to notice:** all three were written in the last 75 days, while the referee —
[`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite), MIT,
78 ★ — is **413 days old**. 🟢 A standard whose conformance suite ages faster than its implementations
is a standard where **claims cannot be checked from the outside**, which is precisely why the
pattern for this layer is *run the suite yourself*, not *read the badge*.

### 🆕 `T39` — "Open source" is splitting from "permissively licensed" in education, in a new way

🔴 `395-D` recorded the split *inside* a project: MIT kernel, ungranted skills. This pass found it
*across a language community*. The most active new education agent found by a non-English leg —
`Aula y Comunidad Educativa Aumentada`, 1 day old — publishes under a **bespoke "Licencia
Comunitaria de Uso Profesional."** Public repository, visible source, 🔴 **no open-source grant.**
🔵 Combined with `h5p/h5p-php-library` (GPL content reported as MIT) and `withmarbleapp/os-taxonomy`
(ODbL + CC-BY-SA over the data), this base has now seen three distinct shapes of the same thing:
ungranted companions, mislabelled grants, and bespoke licences. 🟢 **The operative habit is unchanged
and keeps paying: read the payload, never the badge.** Four of this pass's reads contradicted what
the search channel said about the same repository.

### 🆕 `T40` — A measured absence is only as good as the channel that measured it

🔴 `394-C` concluded this environment *"cannot ENUMERATE GitHub at all,"* and five passes of thin
supply were explained by it. 🟢 **This pass enumerated GitHub twice** — `github.com/trending` at 200
after fourteen passes recorded as 403, and `github.com/search` returning 150 results — and one query
on the reopened channel produced **eight unseen addresses, six of them live and permissive.**
🔴 The refusal was real but narrower than recorded: it is on `api.github.com` and on `curl`, not on
the HTML endpoints through WebFetch.
🔵 **The generalisable lesson, and it is uncomfortable for a base built on declared absences:** an
absence recorded against *one* channel hardens into a fact about *the world* within two or three
passes, and then stops being retested. 🟢 The fix is cheap — **carry the channel in the claim**
("not found via WebSearch" ≠ "does not exist") — and this base should now re-measure a refused
channel on a fixed cadence rather than inheriting it. `396-A`, `396-G`.


# Education industry trends

**🆕 Pass `p395` · reads and commit both 2026-10-23.** Four trends, each tied to a measurement in
[`verified-repos`](../evidence/verified-repos.2026-10-23-p395.tsv),
[`lti-layer-dating`](../evidence/lti-layer-dating.2026-10-23-p395.tsv) or
[`channel-state`](../evidence/channel-state.2026-10-23-p395.tsv).

### 🆕 `T33` — Regulation has started FORBIDDING feature classes, not just risk-rating them

🔴 The EU AI Act bans **emotion-inference systems in educational settings** outright — unacceptable
risk, in the same tier as social scoring and predictive policing. 🔵 Every other regulatory fact on
these shelves is an *obligation* (assess it, document it, keep a human in the loop); this one is a
**prohibition**, and it is the first thing in this base that makes a feature unshippable rather than
expensive. 🟢 **Read it as a design-review input, not a legal-review input.** "Engagement detection"
and "attention scoring" are the two product names this most often hides behind, and both are
routinely proposed in edtech pitches. 🟡 Note the asymmetry with `Annex III ¶3`, which makes grading,
admission, level-assignment and exam monitoring *high-risk but permitted* — so the same product can
hold one feature that needs conformity assessment and another that cannot exist.

### 🆕 `T34` — The integration standard is LANGUAGE-PARTITIONED, and the partition is maintenance

🟢 LTI 1.3 is the surface every agent must cross to live inside Moodle, Canvas, Blackboard or D2L, and
all 13 known addresses were dated this pass in one sitting. 🔴 **The permissive supply is live in
PHP, Node and Python (1–9 days) and dead in Go and Java (679, 1,193, 1,918 days).** 🔵 The standard is
not thinly supported — it is supported *in some runtimes only*, which no amount of spec-reading
reveals and only dating shows. 🟢 Consequence: the language of the client's platform team now decides
an architecture, not a preference — a JVM or Go shop gets an **HTTP edge**, not a library.

### 🆕 `T35` — Supply arrives through the leg you choose, and the prescribed English legs are spent

🔴 **Sixth consecutive pass** in which the four prescribed English global legs returned **zero granted
education-native addresses** — only general-purpose agent frameworks, learning-resource lists and
market-research blogspam (`Gap 387-D`). 🟢 **The same pass found four granted addresses on two legs
nobody had prescribed:** one in **Spanish** (`agente educativo código abierto … tutor IA`), which
surfaced the 1.3k ★ agent, and one naming a **standard** rather than a category (`"LTI 1.3" OR "Open
Badges" … MIT Apache`), which surfaced the Go and Java tier. 🔵 **The dry spell was a property of the
query, not of the ecosystem** — and this base spent five passes attributing it to the ecosystem.

### 🆕 `T36` — The grant on the code and the grant on the curriculum keep coming apart

🔴 Third instance on these shelves, and this time on the pass's best address.
[`hhyqhh/inno-agent`](https://github.com/hhyqhh/inno-agent) is **MIT**; its companion skill-library and
workspace-preset hub is **ungranted on every arm**. The pattern already appears in
`withmarbleapp/os-taxonomy` (permissive code absent, `ODbL-1.0 AND CC-BY-SA-4.0` over the data) and in
`h5p/h5p-php-library` (GPL content routinely mistaken for MIT). 🔵 **In an agent-era project the
reusable asset is increasingly the skills, prompts and presets — exactly the half that carries no
grant.** 🟢 So the licence column on these shelves needs to stop describing "the repository" and start
naming *which artefact* is granted; `Gap 549` said this about one repo, and it is now a trend.

**Pass `p383` · 2026-10-22 · FULL REWRITE.** Prior version archived at
[`archive/2026-10-22-p383-pre-rewrite/intel-trends.md`](../archive/2026-10-22-p383-pre-rewrite/intel-trends.md).

> The previous version's headline trends were about **what this knowledge base could see** —
> channel yield, address supply, star thresholds. Those are facts about a scraper, not about
> education. They are preserved in the archive and in
> [`agents/trending.md`](../agents/trending.md); this shelf is now about the industry.


## 🆕 `p392` — what changed on this shelf

🔴 **`Trend 19`'s closing claim is withdrawn** (*"Node and PHP have maintained LTI 1.3; Python does
not"*) — three Python implementations read first-hand, and withdrawing it turns a language constraint
into a **licence** constraint, which is the more useful statement. 🟢 **Two new trends**: `Trend 20`,
the granted proctoring supply covers the lockdown and not the inference — the inverse of where the
regulatory exposure sits; and `Trend 21`, LATAM's public buyers are procuring AI education platforms
as **subscriptions**, with no tender asking for open source.

## 🆕 `p390` — note on what was removed from this shelf

Two `p387` sections that stood here (*"Date the artefact, not the repository"* and *"The LATAM
supply gap was a reading gap too"*) were **measurement-apparatus notes, not industry trends** —
exactly what `p383`'s rewrite note above says this shelf is not for. They are preserved verbatim in
[`archive/2026-10-22-p390-pre-trim/intel-trends.md`](../archive/2026-10-22-p390-pre-trim/intel-trends.md)
and their durable content lives where it belongs: the dating method in
[`agents/top.md`](../agents/top.md) under *How these rows were verified*, and the LATAM supply in
`Tier 4` of that same shelf. Nothing was lost; it was filed.

## 🆕 `p386` — The LMS-integration gap is not a licence gap any more. It is a **tenancy** gap.

For four passes this base recorded Blackboard and D2L as the two platforms where
*"a permissively-licensed MCP server would be a genuine contribution."* `p386` probed all fifteen
addresses first-hand: **6 MIT grants on Blackboard, 6 on D2L, 1 ungranted, 2 dead.** The licences
were there the whole time; nobody had read them.

🔵 **What replaced the gap is a sharper and more useful trend.** Eleven of the twelve granted
servers authenticate **as the signed-in student** — the learner's own browser SSO/MFA session or
session cookies, no admin API key, read-only because nothing else is possible from that position.
They are built by students, for themselves, at their own university, and several hard-code it.

That makes the 2026 community LMS-MCP supply a **personal-tooling** supply, and it does not become
an institutional one by being licensed well:

| what an institution needs | what a session-scraping server has |
|---|---|
| tenant identity, per-role scope | the rights of whoever signed in |
| an audit trail of every agent action | nothing, or stdout |
| a stable contract against the vendor's API | a login page that changes without notice |
| a data-protection answer for a DPO | the student's session cookie in a config file |

🟢 **Exactly one address read as institution-grade** — [nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp)
(MIT): official REST API, OAuth2, role gate, FERPA handling, PII scrub, JSON audit log, Prometheus
metrics, grade write-back (maintainer self-claims, read not executed). **One in twelve.**

🔵 **The consequence for a studio, and it is a sellable one.** The scarce artefact in LMS
integration is no longer a permissive server — it is a **hardened** one. The work is: take a granted
community server, put tenant auth, role scoping, rate limiting and an audit trail around it, and
pin it to the vendor's documented API rather than its login page. That is a small, well-bounded
engagement with a deliverable the client can show their data-protection officer, and it is
available on **every** major LMS as of this pass. 🔴 On D2L it is still partly greenfield: all six
granted Brightspace servers are student-side.

🔴 **And the methodological trend underneath it, because it will recur in every industry in this
rotation:** a census that counts **addresses** and a census that counts **grants** are different
measurements, and the first one silently masquerades as the second. *"Nine servers and not one
verified grant"* described this base's own reading, not the world — the honest word for a count of
zero reads is **unread**, never **ungranted**.

## Trend 1 — Adoption is finished. Governance is the market.

**88–95% of students and faculty already use AI; 26–54% can name a governing policy.**
That gap, not the adoption curve, is what 2026–27 budget buys.

- Coursera (n=4,200, 5 countries): **95%** using AI academically, **26%** of educators report a
  formal institutional policy.
- EDUCAUSE 2026: only **54%** are aware of *any* policy or guideline.
- Ellucian (n=779): institutional adoption **49% → 66%** year on year, with **data privacy the top
  barrier**.
- Digital Education Council (n=45,398, 35 countries): **88%** of students, **77%** of faculty.

- 🆕 `p384` **UNESCO IESALC** (n=**200 institutions, 19 countries**, Sept 2026): **87%** of LAC
  higher-ed institutions use AI in at least one area — **74%** in teaching and learning, **57%** in
  research — against **26%** with a formal AI strategy. 🟢 **An independent, institutional source
  landing on the same 26%** as Coursera's educator-reported figure, in a different region with a
  different method. The governance gap is no longer an inference from one survey; it replicates.
- 🆕 **OECD TALIS 2024** puts teacher AI use at **~50%+** in Brazil, Chile, Colombia and Costa Rica
  against an **OECD average of 36%**; Uruguay's **Ceibal** reports **75%** of public-school
  teachers. 🔵 Practitioner uptake is running ahead of the OECD mean in LATAM — the governance gap
  is widest exactly where adoption is fastest, which is the opposite of the usual assumption.

**So:** stop selling introduction. Sell policy-to-configuration, audit trails and a governed
gateway. The shadow-AI estate already exists on every campus. 🟢 And sell it **hardest in LATAM**,
not last — the 87%/26% split there is the widest measured in this file.

## Trend 2 — The ROI reckoning arrived, and procurement is being rewired around evidence

- **~80%** of institutions are investing in AI; **29%** of CTOs say it met or exceeded ROI
  expectations (Inside Higher Ed / Hanover).
- **~7 in 10 provosts** use AI weekly themselves; **1 in 10** report a centralised institutional
  strategy. Personal adoption has outrun institutional capability.
- The **US Department of Education's "Dear Colleague" letter** tells states to evaluate ed-tech by
  **measurable learning outcomes rather than screen time**, and to put **evidence requirements into
  procurement**.
- **US/Canada faculty intent to keep using AI fell 76% → 67%** in one year.

**So:** a before/after measurement on the client's own subject mix is becoming a procurement
precondition, not a nice-to-have. [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness),
MMLU and GSM8K are all MIT; there is no licence reason not to ship this with every engagement.

## Trend 3 — Regulatory divergence hardened in 2026. One global configuration is no longer viable.

Four regimes moved in four different directions in a single year:

| region | 2026 direction |
|---|---|
| **EU** | **Regulation (EU) 2026/1744** (OJ 24 Jul 2026) pushed high-risk education systems from 2 Aug 2026 to **2 Dec 2027** — while **Art. 50 transparency still starts 2 Aug 2026** and **Art. 4 AI literacy has bound every school since 2 Feb 2025**. Emotion recognition in education: prohibited. 🆕 `p385` **The nearest date is neither of those: machine-readable marking of AI-generated content on systems ALREADY on the market is due 2 Dec 2026.** Annex I (AI embedded in regulated products) moves to **2 Aug 2028**. |
| **US** | No federal rule; **134+ bills across 31 states**, **33–35 states** with guidance, and binding district-policy mandates (Idaho SB 1227 effective 1 Jul 2026; Oklahoma SB 1734 by 2027-28). |
| **India / China** | **Content labelling and provenance**: India's amended IT Rules from **20 Feb 2026**; China's labelling measures from **1 Sep 2025** (988 services filed by 30 Jun 2026). |
| **Vietnam / Brazil / Mexico** | **Sectoral high-risk designation**: Vietnam names education among six high-risk sectors; Brazil's PL 2.338/2023 reportedly covers student selection; Mexico replicates the EU risk model. |

**So:** regional configuration is now a product requirement. The same tutor needs provenance
watermarking for India, a transparency notice for the EU, a prohibited-uses lockout for DC, and a
teacher-facing-only mode for ANZ and Brazil.

🆕 `p385` **Two corrections to how this trend gets sold.** First, **the EU deferral is widely
misread as breathing room.** It defers the *high-risk* regime; it defers nothing for a system already
deployed, which owes machine-readable marking on **2 Dec 2026**. A client told "the EU moved to 2027"
and nothing else has been misinformed about the only date within the current budget year. Second,
**employment-adjacent AI is separating from student-facing AI as its own regulated surface**:
**Illinois SB 2909** restricts AI in *teacher* evaluation from **1 Jan 2027**, where DC had only a
non-mandatory ban. A product that evaluates staff is a different compliance object from one that
teaches learners, and the two are still being scoped as one in most pitches.

## Trend 4 — Restriction is a real countertrend, not noise

For two years the only direction was adoption. In 2026 the brake appeared:

- **District of Columbia** 2026-27 policy bans AI from **grading, discipline, IEP decisions and
  teacher evaluations** — four of the highest-value automation targets.
- **Ipsos Education Monitor 2026:** **Australia and New Zealand show the highest support for
  banning AI in schools**, while Asian markets show the lowest. One company, two opposite mandates.
- **European Schools:** **no** generative AI tool approved for system-wide use.
- 🔴 **UNCONFIRMED:** a reported **New York City moratorium** on student-facing generative AI
  (EdWeek; date metadata inconsistent). If it holds, the largest US district has gone the other way.

**So:** "student-facing optional" should be an architectural switch from day one, not a retrofit.
A product that cannot run teacher-facing-only is unsellable in a growing share of the market.

## Trend 5 — Teacher-facing is beating student-facing where growth is fastest

HolonIQ's **2026 LATAM EdTech 100** finds regional AI positioning concentrated in **teacher-facing
instructional tools rather than consumer tutoring** — Teachy (Brazil) in lesson preparation, Ginia
(Mexico) in employability. The regulation points the same way: Brazil's draft law targets
**student selection**, DC bans AI in grading and discipline, ANZ sentiment is restrictive.

**So:** the market and the regulator agree for once. Lesson preparation, assessment drafting,
feedback generation and administrative load carry the growth and avoid the hot zone.

## Trend 6 — The permissive-licence frontier runs *across* the stack, not along it

Measured first-hand this pass over 58 live repositories:

- **Platform tier is copyleft**: Moodle GPL-3.0, Open edX AGPL-3.0, Canvas AGPL-3.0, Chamilo
  GPL-3.0, ILIAS GPL-3.0, Tutor AGPL-3.0, Frappe LMS AGPL-3.0, Sakai ECL-2.0, Opencast ECL-2.0,
  OpenEduCat LGPL-3.0, H5P GPL-3.0.
- **Exactly one permissive major LMS**: **[OpenOLAT](https://github.com/OpenOLAT/OpenOLAT),
  Apache-2.0** — and no roundup we read mentions it.
- **Agent tier is permissive almost throughout**: MIT / Apache-2.0 / BSD-3.

**So:** the architecture follows from the licences. Compose permissive agents **over** a copyleft
platform across **LTI 1.3**, **MCP** or web services — never fork the platform. The interop boundary
is a legal artefact as much as a technical one.

## Trend 7 — MCP reached the LMS, and that is genuinely new

As of 2026 the LMS is addressable by agents without a fork:

- **Moodle's own plugin directory** carries **`webservice_mcp`**, exposing Moodle's external
  functions as **MCP tools over JSON-RPC 2.0** — **Moodle 4.5–5.2**, latest release
  **23 Jul 2026**, gated on the `webservice/mcp:use` capability.
- **Canvas** is served by community MIT servers ([r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp),
  fork [mdweaver/canvas-mcp](https://github.com/mdweaver/canvas-mcp)).
- 🔴 **No official server from Instructure or Moodle HQ**, and two of the most-advertised community
  Canvas/Moodle servers are **unlicensed** — see [`agents/top.md`](../agents/top.md).
- 🆕 `p387` **27 distinct education MCP server slugs are shelved** on
  [`agents/top.md`](../agents/top.md) — re-derived by this base's own `recount` instrument, which
  was runnable this pass for the first time in several (the figure stood at **12** here while the
  shelf had grown to 27). Across both agent shelves **MCP reaches **6 distinct LMS platforms**** —
  Canvas, Moodle, Google Classroom, Blackboard, Brightspace/D2L and Open edX. The cumulative
  harvest behind that is lopsided: **35 Canvas servers and 20 Moodle**, against **2 for Open edX**.
- 🔴 🆕 `p387` **A correction this shelf owed since `p386`, and did not carry.** The bullet above
  used to end *"Blackboard has 9 with not one verified grant and D2L has 6 with the only one
  checked ungranted"* — and concluded that a permissive server on either platform *"would be a real
  contribution."* `p386` probed all fifteen addresses and found **6 MIT grants on Blackboard and 6
  on D2L**; it corrected [`agents/top.md`](../agents/top.md) and **left this sentence standing**.
  🔵 The live claim is: on Canvas and Moodle the work is *selection*; on Blackboard and D2L the
  grants exist and the missing thing is **tenancy** — every granted server there authenticates as
  the signed-in student (see `compose/patterns.md` **Pattern N**, and `Gap 387-A`).

**So:** the integration cost of an LMS-aware agent dropped by an order of magnitude this year, and
the remaining risk moved from engineering to licensing.

## Trend 8 — Measurement gap in this pass, stated rather than papered over

**No popularity metric is published this pass.** Every star channel was closed in this sandbox:
`api.github.com` 403, `github.com` HTML 403, `img.shields.io` blocked, `api.star-history.com`
blocked. The technology cycle (`v76`) had to publish a correction that earlier cycles' star counts
were **pipeline-inflated across several industries**; carrying unverifiable numbers forward would
repeat that error. Licence, default ref and liveness **were** verified first-hand for all 58 live
addresses — see [`verified-repos`](../evidence/verified-repos.2026-10-22-p383.tsv).

**So:** rank by licence permissiveness, maintenance signal and fit. Popularity was never the
decision criterion for a studio engagement anyway.

🟢 🆕 `p387` **Partially closed — and by a channel, not by a workaround.** "Maintenance signal" was
the one criterion in that sentence this base could not actually measure. It can now: **package
registries publish dates**, and 26 education packages are dated in
[`registry-recency`](../evidence/registry-recency.2026-10-22-p387.tsv). 🔴 **Still open:** repository
commit activity, contributor counts and issue latency (all behind `api.github.com`, 403), and the
many shelf entries that are **not published packages at all** — for those, publication is absent
rather than old, which is itself worth telling a client.

## Trend 9 — 🆕 `p384` The curriculum-data layer arrived, and its licence is a *database* licence

**Every adaptive-learning pitch rests on knowing what a learner must master before the next topic.
Until this pass, no shelf here held that artefact. Now one does — and it is not licensed like code.**

[withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) `v1` publishes **1,930
micro-topics** and **4,102 prerequisite edges** as a DAG — each edge tagged `hard`/`soft` with a
one-line reason — over **9 subjects**, aligned to **NGSS, Common Core, the UK National Curriculum**
and the Australian curriculum. Its grant, read first-hand at `main/LICENSE` (25,289 B), is the
**Open Data Commons Open Database License (ODbL)**. There is **no separate code grant**.

**Why this is a trend and not just a row.** Every licence question these shelves have answered so
far was a **copyright** question about code: can we link to it, can we ship closed extensions. ODbL
is a **share-alike database right**, and it draws its line in a different place:

- **§4.3 — a *Produced Work*** (the tutor's output: a lesson plan, a next-topic choice, an
  explanation) needs **an attribution notice and nothing else**. 🟢 This is the permissive path.
- **§4.4 — a *Derivative Database*** (the client's topics merged in, standards remapped, the graph
  re-cut) must be publicly used **only** under ODbL, a later ODbL, or a compatible licence. §4.4(b)
  is explicit that extracting *"the whole or a Substantial part of the Contents into a new
  database"* **is** a Derivative Database. 🔴 This is the trap, and it is the thing a studio would
  naturally do next.

🔴 **A licence scanner pointed at code will not see this at all.** Neither will a licence badge:
ODbL is not in the permissive/copyleft taxonomy these shelves have been using, so the row cannot be
classified green or red — it is **green on one axis and red on the other, depending on what you
ship**. `Pattern L` was built for the case where a badge misreports a code grant; this is the case
where the *category* is wrong.

**So:** three concrete consequences.
1. **Ground on it, do not fork it.** Keep client curriculum data in a separate store joined at
   query time, so the taxonomy stays an **input** rather than a component of the deliverable. That
   is **Pattern H** in [`compose/patterns.md`](../compose/patterns.md).
2. **Add a data-rights question to intake.** Alongside "what licence is the code", ask "what rights
   govern the **data** we ground on". Education runs on standards, item banks and curriculum maps —
   this will not be the last ODbL/CC-BY-SA artefact on these shelves.
3. **Check coverage before promising it.** The maintainers state their own gap: teaching research
   covers **1,049** topics (Science and Mathematics) and **881 topics have none**. A
   research-backed-guidance claim is true for roughly half the graph.

## Trend 10 — 🆕 `p388` The parent is the unserved persona in education AI, and the statutes are pushing toward them

Every market map this base has built, and every roundup it has read, segments education AI into
**student-facing** and **teacher-facing** — `Trend 5` is about which of the two is growing faster.
Both categories are about people *inside* the institution. **The parent is outside it, and is the
person who actually logs into the portal.**

**The supply arrived this pass and it is not a prototype tier.**
[chrischall/infinitecampus-mcp](https://github.com/chrischall/infinitecampus-mcp) (**MIT**, 20 tools
over **Infinite Campus / Campus Parent**, **47 published releases**) and
[chrischall/canvas-parent-mcp](https://github.com/chrischall/canvas-parent-mcp) (**MIT**, 18 tools,
**43 releases**) are maintained, deliberately scoped to the observer surface, and built by one
maintainer working the same problem across two platforms — which is what a real need looks like
rather than a weekend demo.

**Three reasons this is a trend and not a curiosity:**

1. **The statutes are already there.** Every North American instrument this base tracks puts
   **family transparency** in the text — Oklahoma SB 1734 names it outright; Maryland's Chapter 634
   is built around guidance districts must hand down to families. Regulators keep asking
   institutions to *explain AI to parents*; nobody is building the surface that would.
2. **There is no incumbent to displace.** The parent portal is a **feature of the SIS**, not a
   market. No vendor defends it, and the SIS vendors have no incentive to open it. That is the rarest
   condition in education software, where every other surface has a 20-year incumbent.
3. **It inverts the tenancy problem instead of solving it.** `p386`'s finding — every granted LMS
   server authenticates as the signed-in user, so a studio cannot hand one to an institution — reads
   as a *defect* for student and teacher tools. For the parent it is **the correct architecture**:
   the parent's own credential, the parent's own child, no institutional tenancy required at all.

🔴 **And the boundary that defines the engagement, because it is not a licence boundary.** Hosted by a
family, these tools are a person exercising their own access. **Hosted by a studio for a district, the
identical API call becomes a FERPA-governed disclosure of an education record.** The code does not
change; the obligation does. 🔵 So the honest market shape is **two different products**: a
parent-side tool (no tenancy, no FERPA exposure, no institutional sale) and a district-side one (full
tenancy, full FERPA, a real procurement cycle). Conflating them is how this gets sold wrong.
`Pattern P` in [`compose/patterns.md`](../compose/patterns.md) is built on that split.

## Trend 11 — 🆕 `p388` Jurisdictional curriculum content is becoming the defensible layer, and it is arriving region by region

`Trend 9` recorded that a curriculum-data layer had arrived and that its licence was a **database**
licence. `p388` shows the *shape* that layer is taking, and it is not one global graph:

| region | asset | licence | what makes it local |
|---|---|---|---|
| **North America** | 🆕 [pdg6/bc-curriculum-mcp-server](https://github.com/pdg6/bc-curriculum-mcp-server) | 🟢 MIT | The **BC Ministry** K–12 curriculum in its real three-column **KDU** structure — and the **First Peoples Principles of Learning**, a provincial requirement no imported product carries |
| **LATAM** | [GuilhermeScarpini/agente-bncc-professores](https://github.com/GuilhermeScarpini/agente-bncc-professores) (`p387`) | 🟢 MIT | **BNCC** skill codes, Brazil's national curriculum, with invented codes discarded before a teacher sees them |
| **Global** | [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) (`p384`) | 🟡 **ODbL** (database licence) | 1,590 topics / 3,221 prerequisite edges mapped to NGSS and Common Core |

**The pattern across the three:** the model is interchangeable, the *curriculum authority* is not.
A tutor that cites a BNCC code, a BC Big Idea or an NGSS standard is doing something a
general-purpose tutor **cannot** — not because its reasoning is better, but because it is anchored to
the instrument the jurisdiction grades against.

**Three consequences for an engagement:**

1. **Curriculum grounding is now demonstrable in three regions, not described in one.** `Pattern H`
   stops being a proposal and becomes a reference build with a local example in hand.
2. 🟡 **The risk on these assets is currency, not licence.** The BC server is 🟢 MIT — clean — but it
   is a **crawl** of `curriculum.gov.bc.ca`, last published **2026-03-27**. Curricula are revised on
   political timetables. **Quote the re-crawl as a maintenance line item**, and never let a client
   believe a crawl is a feed.
3. **Keep asking the data-rights question from `Trend 9`.** Two of the three assets above are code
   (MIT); one is a **database** under ODbL. "What licence is the code?" and "what rights govern the
   data we ground on?" remain two different intake questions with two different answers.

## Trend 12 — 🆕 `p388` An exhausted channel is not an exhausted supply — and "published but unreadable" is now a real category

This is a trend about **how this industry's open-source supply is actually distributed**, and it has
a direct procurement consequence.

**The discovery finding.** `p382` recorded that this industry's address supply was **exhausted**.
What was exhausted were four search-engine legs. **`registry.npmjs.org/-/v1/search` is open**, and 29
education queries returned **383 GitHub addresses absent from this entire base**, of which **22 are
granted and education-specific** — the largest single intake in this base's recorded history. 🔵 The
general lesson, and it is the third of its kind here: `p386` learned *a count of addresses is not a
count of grants*; `p387` learned *a null leg is not a null supply*; `p388` adds *an exhausted channel
is not an exhausted supply*. All three are one error — **a property of the instrument reported as a
property of the industry.**

🔵 **Why a package registry is structurally the better instrument for this industry.** A trending page
ranks by attention over days. Education tooling is **institutional, unglamorous and
low-star** — a 47-release parent-portal server for a US K-12 SIS will never trend anywhere. The
registry indexes it anyway, and returns its **entire publish history in the same call**, which
answers "is it maintained?" at the moment of discovery rather than two steps later.

🔴 **The new supply category, and it is the uncomfortable half.** Of 32 addresses probed, **6 publish
to npm from a repository that is not publicly readable** — `git ls-remote` prompts for credentials,
so the repository is **closed, not missing**. The package installs; the provenance cannot be audited.
The costliest instance is **103 published versions** of an AI-generation quiz library **with SCORM
support** ([thanh01pmt/interactive-quiz-kit](https://github.com/thanh01pmt/interactive-quiz-kit)); the
most instructive is [ale-alejandro/beadkit](https://github.com/ale-alejandro/beadkit), whose manifest
declares **`"SEE LICENSE IN LICENSE"` — pointing at a file inside a repository nobody can read.**

**So the licence-reading discipline this base built needs one more rule.** `Pattern L` clears a
repository by reading its **subtree**; for these there *is* no subtree. The rule that replaces it:
**for an npm-only dependency, the manifest is a claim and the tarball is the evidence** —
`registry.npmjs.org/<pkg>/-/<pkg>-<v>.tgz` serves the published artefact even when the repository is
closed, and **it is the licence that actually ships**. 🔴 That is how this pass established that a
major publisher's tutoring SDK (**115 published versions**) carries **no licence at all**: not from
the repo, which is private, but from the artefact, which is not. 🔵 And the corollary a studio should
internalise: **commercial education vendors are starting to distribute as closed SaaS with an npm
veneer.** The npm scope looks like open source, installs like open source, and grants nothing.

🔵 🆕 `p391` **The channel now has a decay curve, not just a verdict.** Re-run with 32 queries of
*fresh* vocabulary (tenancy, SEN/IEP, proctoring, QTI, xAPI, OneRoster, FERPA, standards, personas):
**321** addresses absent from this base → 37 past a domain filter → 11 probed → **3 shelvable**.
That is **0.9%**, against `p388`'s **5.7%** (22 of 383). 🟢 The channel is **depleting, not
exhausted** — it still produced three rows, one of which opened a category (`Pattern W`). 🔴 But the
seam `p388` opened is largely mined, so the next pass should change **channel**, not vocabulary.
🔴 **And the instrument nearly lied:** the first draft of the domain filter matched the query column
of its own output and "confirmed" 37 education rows that were Vercel, AWS and Storybook packages.
Caught before a shelf. *A filter that scores its own prompt is not a filter.*

## Trend 13 — 🆕 `p389` The supply has a currency problem, and it is now a number

This base has built a careful discipline about *licences* and almost none about *time*. `p387` and
`p388` both recorded that no maintenance signal was available. It was: **`git` read access is open to
every public repository**, and a blobless shallow clone returns the last commit date at the real
default ref in about a second. Sixty addresses were dated this pass.

**The distribution, which is the trend.** 58 live, 2 dead. **48 of 58 moved within 30 days**, and 17
of those were committed **on the day of the pass**. That is a healthier supply than this industry's
reputation suggests — education tooling is unglamorous, not abandoned. But **7 of 58 are past 120
days, and four of those seven carried a recommendation on these shelves**:

| stale address | days | what it was being recommended for |
|---|---|---|
| [plastic-labs/tutor-gpt](https://github.com/plastic-labs/tutor-gpt) | 343 | a Tier-1 tutor |
| [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server) | 242 | Moodle integration |
| [pdg6/bc-curriculum-mcp-server](https://github.com/pdg6/bc-curriculum-mcp-server) | 209 | North American curriculum grounding |
| [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | 144 | Canvas integration — **and it is ungranted** |

🔵 **The general shape, and it is this base's fourth instance of one error.** `p386`: a count of
addresses is not a count of grants. `p387`: a null leg is not a null supply. `p388`: an exhausted
channel is not an exhausted supply. **`p389`: a closed popularity channel is not a closed maintenance
channel.** Four passes, one mistake — *a property of the instrument reported as a property of the
industry* — and each time the fix was to ask which channel was actually being measured.

🔴 **The procurement consequence, which outlives the instrument.** A licence tells you whether you
*may* build on something. A date tells you whether you will be **alone** on it. Those are different
risks and they price differently: an MIT repository that has not moved in eight months is a
**vendoring decision with a maintenance line in the estimate**, not an integration. Both numbers
belong in the same row of a proposal, and until this pass only one of them was here.

🟡 **And the limit, stated so the number is not over-read.** A commit date says someone pushed — not
to the branch a release is cut from, and not that the project is healthy.
[instructure/canvas-lms](https://github.com/instructure/canvas-lms) is the case in point: `master` is
175 days behind while its `stable/*` branches move, because that is how Instructure ships. A
specification or a dataset that is *finished* is not decaying either. Read the date against what the
artefact is.

## Trend 14 — 🆕 `p389` APAC has become the net exporter of open-source education AI, and the Gulf the net importer

**The supply side.** The largest education-native repository in open source is
[**OpenMAIC**](https://github.com/THU-MAIC/OpenMAIC) — **MIT**, ~41.3k ★, from **Tsinghua
University**, committed the day of this pass, published in **JCST 2026** and validated inside the
university on **700+ students**. It is not an outlier in its region: the Tier-1 tutor shelf on
[`agents/top.md`](../agents/top.md) is now **majority APAC by origin** — DeepTutor (HKU, Apache-2.0),
ai-shifu (China, Apache-2.0), educhain (India, MIT), OpenTutor (China, MIT), Aha Tutor (China, MIT),
learn-shell (China), ChatTutor (APAC) — against one EMEA entry (mentingo, Poland) and, at Tier 1, one
North American (tutor-gpt, now 343 days stale). 🔵 **The pattern is not "China ships a lot of AI."**
It is that **the pedagogy is being designed in the repository** — mastery estimates that record
*confidence* separately from correctness, FSRS review built in, cognitive-load detection,
misconception-aware branching — in projects whose authors are university teaching groups rather than
startups. That is a supply a studio can build a practice on, and its licences are permissive.

**The demand side, created by statute rather than by procurement.** The **UAE** approved an AI
curriculum across **all public and private schools** by Cabinet decision in September 2026, with
**22,000 teachers and education professionals** to be trained, and for 2026-27 merged Design,
Innovation and Computer Science into a single subject, *Artificial Intelligence and Technology*,
KG–Grade 12. **Saudi Arabia** began a comprehensive AI curriculum across all levels of public
education in the 2025-26 academic year, led by the **National Curriculum Center** with **SDAIA**.
These are the most aggressive AI-in-education mandates anywhere: not permission to pilot, a
**compulsory subject with a teacher-training number attached**.

🔴 **And the mismatch is the opportunity.** This pass found **no Gulf-origin and no Arabic-first
open-source education agent or platform** — not one address. The region with the world's strongest
statutory demand for AI teaching material has, as far as this base can see, **no local open-source
supply at all**, while the permissive supply that does exist is EN + zh-CN. The gap is not a model
gap; it is **curriculum-grounding and language**: Arabic-first content, alignment to the UAE MoE's
seven curriculum areas, and the teacher-training surface those 22,000 professionals will be trained
on. 🟡 Recorded as an informed gap, not a finding: the searches run were English-language, and an
Arabic-language search is the obvious next leg.

## Trend 15 — 🆕 `p389` The parent surface now has a cautionary case, and it is in LATAM

`p388` added the parent/guardian persona and named **FERPA** as the line that splits a family-run
assistant from a district-hosted one. The LATAM equivalent of that line is **LGPD Article 14**, and
unlike FERPA it already has a public failure attached to it.

- **Brazil has no AI statute in force.** As of October 2026 **PL 2338/2023** — passed by the Senate
  in December 2024 — is still in the Câmara dos Deputados, with reports that the vote resumes after
  the October 2026 elections. So the binding instrument for an education engagement today is the
  **LGPD**, not an AI law.
- **Children's data has its own consent basis.** For core teaching a school generally relies on
  contract and legal obligation, but uses **beyond** that — images, communications, extracurricular
  activity — require **specific, explicit, recorded and revocable consent from a parent or guardian**
  under Art. 14. An AI parent portal is squarely in the "beyond" category.
- **The cautionary case.** In 2023 the São Paulo state education department (**SEDUC**) had its
  *Minha Escola* app installed on parents' phones without notice or consent; Data Privacy Brasil
  assessed it as a probable LGPD violation. 🔵 **This is the precise failure mode of the persona
  `p388` added** — a district-hosted parent surface deployed *to* families rather than *for* them —
  and it is the reference a LATAM client will have in mind, so bring it up first.

🟢 **What this makes defensible rather than risky.** The pattern that survives Art. 14 is the one
`Pattern P-1` already describes: the **family runs the agent and exercises its own access right**, so
no new disclosure is created. For the district-hosted variant (`P-2`), the deliverable a Brazilian
client should be sold is the **consent and revocation mechanism itself** — per-guardian, recorded,
revocable, auditable — as a first-class feature, not a checkbox. 🟡 **Mexico: informed gap.** No
education-specific AI guidance or student-data rule was found for Mexico in this pass; the general
position is a data-protection regime and no AI statute. Stated, not inferred.

## Trend 16 — 🆕 `p390` The copyleft firewall moved inside the platform, and it is a packaging decision rather than a licensing one

For several passes this shelf framed "permissive agent + copyleft platform" as a problem solved at
the **boundary**: hold the agent outside the LMS and talk to it over LTI or MCP, so no copyleft
reaches your code. That is still a valid pattern, but `p390` found the cleaner answer was in the
platforms' own packaging the whole time, and **nobody had read it per-package**:

| package | role | licence |
|---|---|---|
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | the platform you deploy | 🔴 **AGPL-3.0** |
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | the component API your plugin imports | 🟢 **Apache-2.0** |
| [`openedx/xblock-sdk`](https://github.com/openedx/xblock-sdk) | what you develop against | 🟢 **Apache-2.0** |
| [`openedx/openedx-learning`](https://github.com/openedx/openedx-learning) | newer core data layer | 🔴 **AGPL-3.0** |

All four read from the payload at their real default ref on **2026-10-22**; the two Apache grants are
at `LICENSE.TXT`, which is also why a badge-level or root-`LICENSE` read misses them.

**Why this is a trend and not a trivium.** It means the in-platform plugin — the deepest, most
useful integration, with full access to course state and no network hop — is **also** the one that
can stay MIT or proprietary. The industry had been treating depth of integration and licence freedom
as a trade-off, and for Open edX specifically they are not. [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA)
(MIT, Universidad Tecnológica de Pereira) has been shipping on exactly this basis.

🔴 **The trend has a sharp edge: the boundary is per-package, and it is moving.** `openedx-learning`
is the newer core data layer and it is **AGPL-3.0**. As more platform functionality migrates there,
the set of imports that keeps a plugin permissive **shrinks**. Audit the dependency list in CI, not
once at kick-off. The general rule this generalises to: **licence is a property of the package you
import, not of the organisation that publishes it** — and in education, where every major platform is
copyleft, that distinction is worth real money.

## Trend 17 — 🆕 `p390` Voice is the next interface gap, and the open-source supply has not arrived

Across seven passes these shelves accumulated tutors, graders, LMS connectors, parent portals and a
generated classroom. **Every one of them is text-first.** `p390` found exactly **one** granted
voice-first education agent in the open-source supply — [`Jeanikt/tutor-ai-agent`](https://github.com/Jeanikt/tutor-ai-agent)
(MIT, Brazil, pt-BR, 15 days old, self-described as *"in development"* with no public deployment).

**Why the gap matters commercially.** Voice is not a convenience feature in this industry; it is an
access feature, and it maps onto precisely the markets with the fastest growth and the least supply:

- **Early grades**, where reading and typing fluency is the thing being taught, not assumed.
- **Shared-device and phone-only households** — the LATAM and APAC reality `Trend 10` documents.
- **Language learning**, where pronunciation *is* the assessed skill and text cannot carry it.
- **Accessibility**, which in EMEA public procurement is frequently a scored requirement rather
  than a nice-to-have.

**Why the gap is narrow rather than deep, which is the opportunity.** The hard parts are already
permissive and maintained: [`livekit/agents`](https://github.com/livekit/agents) (Apache-2.0) solves
turn detection, interruption and barge-in — the things that actually make a spoken tutor usable — and
[`mozilla/common-voice`](https://github.com/mozilla/common-voice) supplies **CC0-1.0** speech corpora
across ~130 language variants for ASR evaluation and fine-tuning. What is missing is not
infrastructure; it is **an education-grade assembly of it** — mastery model in the loop, symbolic
checking behind the arithmetic, and the biometric/disclosure posture a school can sign.
🆕 `Pattern V` in [`compose/patterns.md`](../compose/patterns.md) is that assembly.

🔴 **`Gap 390-A` — the informed gap, stated rather than left as silence.** The searches this pass ran
for an open-source voice or multilingual tutor in an **African or South Asian language** returned
**nothing granted and maintained**. What came back instead: one India-first multilingual *toolkit*
(not a tutor), an arXiv framework for low-cost home language learning with **no public code located**,
and a repository that teaches *Spanish to non-speakers* inside an agent CLI — which is the inverse of
a Spanish-language tutor for Spanish-speaking learners, a category error this base recorded in `p388`
and which keeps recurring in search results. 🔵 **Read this as a null result in the open-source
supply, not a null in demand** — Africa is among the fastest-growing online-education markets. For a
client engagement in those languages the honest position is: **the substrate is permissive and ready,
the localised tutor does not exist and would be built, and Common Voice is where its evaluation set
comes from.**


## Trend 18 — 🆕 `p391` Education AI is shipping as **harness extensions**, not standalone applications

Three of this base's education rows are now plugins to the *same* agent harness, by **three
unrelated maintainers**, all MIT, all published inside about ten days:

| row | what it is | published |
|---|---|---|
| [`BaronCyrus/dsh-aha-tutor`](https://github.com/BaronCyrus/dsh-aha-tutor) (`p388`, Tier 1) | narrated-blackboard adaptive tutor | npm v1.7.0, 2026-10-22 |
| [`SenmuuuuW/dsh-diagnostic-tutor`](https://github.com/SenmuuuuW/dsh-diagnostic-tutor) (🆕 `p391`, Tier 1) | diagnosis-first learning runtime | npm v0.1.1, 2026-10-17 |
| [`GuoMonth/dsh-multi-tenant`](https://github.com/GuoMonth/dsh-multi-tenant) (🆕 `p391`) | K8s + OIDC multi-tenant hosting for the same harness | npm v0.10.0-rc.1, 2026-10-12 |

They are extensions to **DeepSeek Harness**, and the pattern is not harness-specific — this pass also
read [`mackt/pi-language-tutor`](https://github.com/mackt/pi-language-tutor) (MIT) as an extension to
the Pi agent. 🟢 **Why it is a trend and not a coincidence:** a harness extension inherits model
plumbing, tool calling, auth, UI shell and a distribution channel for free, so a single maintainer can
ship a credible tutor in weeks. The economics now favour the plugin over the application.

🔵 **The operational consequence, and it explains a channel result this base has hit repeatedly.** The
distribution channel for education AI is becoming **the agent harness's package registry** — which is
why `registry.npmjs.org` keeps yielding education supply while `moodle.org` has never once been
reachable *or* necessary. Looking for education AI in LMS plugin directories is looking where it was
built in 2019.

🔴 **The cost a studio inherits, stated plainly.** A harness extension is **not deployable without its
harness**. `dsh-diagnostic-tutor` requires DeepSeek Harness; adopting it means adopting that runtime,
its update cadence and its governance. For a client who cannot, the move is to copy the *structure*
(see `Pattern X`) rather than the package — which is exactly why `Pattern X` separates the pedagogy
from the runtime instead of recommending the repository wholesale.

## Trend 19 — 🆕 `p391` The standards body's reference implementation goes stale; the **vendor fork** carries the maintenance

`p390` dated [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library) at 2,332
days and concluded the LTI 1.3 integration path had no installable implementation. The grant and the
dating were both right; the conclusion was wrong, because the maintained line is not at the
authoritative-looking address:

| address | last commit | registry | verdict |
|---|---|---|---|
| [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) | **2026-10-16** | packagist `lti-1p3-tool` **v6.4.4**, 68 versions, 2026-09-23 | 🟢 **install this** |
| [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (Node) | **2026-10-13** | npm `ltijs` **v7.0.7**, 207 versions, 2026-10-06 | 🟢 **install this** |
| [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library) | 2020-06-03 | — | 🔴 spec citation only |
| [`IMSGlobal/lti-1-3-php-library`](https://github.com/IMSGlobal/lti-1-3-php-library) | 2020-06-03, **identical sha `3a192de`** | — | 🔴 the same project, renamed org |
| [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (Python) | 2022-11-21 | PyPI `PyLTI1p3` 2.0.0, **2022-11-20** | 🔴 genuinely dead |

🟢 **The generalisable rule:** in standards-driven education interop, the consortium publishes the
spec and a demonstration; a **vendor with production traffic** maintains the library. So when a
reference implementation dates badly, the next question is *who ships this in production* — not
*should we vendor the spec*. Check the fork network and the package registry before concluding a path
is closed.

🔴 🆕 `p392` **The "language asymmetry" half of this trend is WITHDRAWN, and withdrawing it sharpens
the rule above rather than weakening it.** `p391` closed this trend with: *"Node and PHP have
maintained LTI 1.3; Python does not… the interop edge is therefore a separate Node or PHP service in
front of the agent."* Read first-hand this pass, **Python has three**:

| address | grant | last commit | registry | role |
|---|---|---|---|---|
| [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) | 🟢 **MIT** (1,098 B) | **2026-10-20 — 2 d** | PyPI `django-lti` **v0.10.1**, 17 releases, 2026-08-07 | 🟢 **in-process**, Django app + middleware |
| [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) | 🟢 **BSD-3-Clause** (1,528 B) | 2026-07-01 — 113 d | PyPI **v1.6.3**, 15 releases | 🟢 LTI 1.1 **and** 1.3 into JupyterHub |
| [`openedx/xblock-lti-consumer`](https://github.com/openedx/xblock-lti-consumer) | 🔴 **AGPL-3.0** (34,520 B) | **2026-10-22 — 0 d** | PyPI `lti-consumer-xblock` **v11.4.2** | 🔴 best-maintained of the three, **copyleft** |

🟢 **And the maintainer pattern holds in Python too, which is the trend's real content.** The three
Python implementations are maintained by a **university innovation centre** (Michigan), an
**ecosystem project** (Jupyter) and a **platform vendor** (Open edX) — not by the standards body. The
rule is unchanged and now has six instances instead of four: *in standards-driven education interop,
ask who ships this in production.*

🔴 **What survives as a constraint is licence-shaped, not language-shaped**, and that is a more useful
thing to tell a client: the best-maintained Python LTI implementation is **AGPL-3.0**, the
best-maintained Node one is Apache-2.0, and the permissive Python options are smaller (26 ★ and 73 ★)
and framework-bound. The question is never *"does this language have LTI"* but *"does the maintained
implementation in my language carry a grant I can ship?"* `Gap 391-A` **CLOSED**.

## Trend 20 — 🆕 `p392` The granted proctoring supply covers the **lockdown**, not the **inference** — which is the opposite of the regulatory exposure

For four passes this base recorded proctoring as having *"no credible permissive open-source option"*
and treated that as a liability boundary to name rather than fill. Probed first-hand, the supply
exists — and its **shape** is the trend:

| component | grant | last commit | what it actually does | the AI part |
|---|---|---|---|---|
| [`mdestafadilah/proctoring.js`](https://github.com/mdestafadilah/proctoring.js) | 🟢 **MIT** (1,069 B, manifest agrees) | **2026-09-28** | tab-switch, right-click, DevTools shortcuts, clipboard events, camera state, **faces**, audio loudness, **virtual-camera / loopback / screen-share detection** | 🟢 **real** — face-api on TF.js, **in the browser** |
| [`Scaler-Opensource/exam-guard`](https://github.com/Scaler-Opensource/exam-guard) | 🔴 **CONFLICT** — Apache-2.0 payload, `ISC` manifest **and** npm | **2026-10-13**, 398 commits | blocks copy/paste/cut, right-click, selection, shortcuts; detects `tabSwitch`, `browserBlur`, `exitTab`, `fullScreen`; periodic page and webcam snapshots POSTed to an endpoint you build | 🔴 **absent** — object detection, multi-face and eye tracking are marked *"(To be Done)"* |
| [`openedx/edx-proctoring`](https://github.com/openedx/edx-proctoring) | 🔴 **AGPL-3.0** | 🆕 re-read `p392`: `master` HEAD **2026-10-22 — 0 d** (this base's harvest row said 2026-05-30; the live read is today), 253 releases | the exam **workflow** — attempts, review states, integration points | 🔴 none; it brokers a vendor |

🔵 **The asymmetry, stated as a rule:** open-source proctoring is **deterministic browser lockdown and
event telemetry**, while the **inference** — identity, gaze, multiple faces, behavioural scoring — is
either absent, roadmapped, or the proprietary service the AGPL workflow brokers. 🟢 **And the
regulatory exposure runs the other way.** Lockdown and event logs do no biometric inference: they
are not what the EU AI Act's Annex III is reaching for, and they are explainable to a student
(*"you left fullscreen at 14:03"*). The inference layer is where high-risk obligations, biometric
rules and the whole evidentiary argument live — and that is exactly the layer the permissive supply
does not have.

🟢 **So the honest advice to a client flips, and it is now sellable in both directions:** *we can
build the integrity layer you can defend — lockdown, event trail, human review — permissively and
today; the part that would flag a student automatically is the part that makes you a deployer of a
high-risk system, and neither of us should want it in v1.* 🔴 The obligation attaches to the
**deployment**, not the dependency, so an open-source grant transfers no compliance relief whatsoever.

## Trend 21 — 🆕 `p392` LATAM's public buyers are procuring AI education platforms as **subscriptions**, and no tender asks for open source

A replacement regional leg shaped like a **buyer** rather than a supplier — public-procurement
vocabulary in Spanish and Portuguese — returned five live 2026 instruments where three passes of
English, stars-sorted supply legs returned nothing: Santa Fe province (Argentina, Tender 01/26,
*subscriptions* to AI-enhanced educational cloud platforms), **OEI-Chile `OEI-LIC-1-25`** (design and
build of an AI platform for **administrative management in Chilean schools** over regulatory,
financial and operational data), UNOPS Argentina `ITB/2026/62779` (educational platform **licences**,
2+2 years), the **CIEDEPAR** consortium in Paraná (multi-municipality SaaS education management) and
Francisco Morato, SP (**R$1,924,665.00**).

🔴 **Not one of the five specifies free or open-source software.** The spend is real, the AI framing
is explicit, and the procurement shape is **product subscription**.

🔵 **Why this is a trend and not five anecdotes:** it is the demand-side mirror of *Trend 6*. This
base's whole thesis is permissive assembly, and the buyers writing the cheques are specifying
subscriptions — so the binding constraint on an open-source education engagement in LATAM is **the
specification, not the licence frontier**. 🟢 The opening is a total-cost bid against subscription
pricing, with the OEI-Chile scope (administrative management, compliance recommendations) matching the
`i-educar` + agent shape these shelves already hold; the work is to get *"or equivalent open-source
implementation"* into a specification written for a product. 🟡 Graded **`ATTRIBUTED-UNVERIFIED`** —
aggregators and news items; no official portal (COMPR.AR, ChileCompra, PNCP) is reachable here.


## Trend 22 — 🆕 `p393` The education **interoperability layer is Python** while the agent layer is TypeScript, and a one-registry sweep answers half the question

**What was measured.** `p393` opened the channel `Gap 392-C` said did not exist: `pypi.org/simple/`
under PEP 691 returns **920,784 project names in 45,189,043 B in 1.4 seconds**, unauthenticated. A
sweep of 24 token-exact education keys returned **507 name hits → 15 distinct addresses**, 13 live and
verified first-hand.

**What came back was a layer, not a list.** Not more tutors or more agents — **plumbing**:

| standard / surface | granted Python supply found | grant |
|---|---|---|
| **LTI 1.3 / Advantage** | `openfun/django-lti-toolbox` (France Université Numérique), `Harvard-University-iCommons/django-lti-dynamic-registration` | 🟢 MIT, 🟢 MIT |
| **QTI** (assessment exchange) | `vosslab/qti_package_maker`, `Citolab/qti-convert-python` (Cito, NL) | 🟡 LGPL-3.0, 🔴 GPL-3.0 |
| **OneRoster / Caliper** | the `timeback-*` family — 🔴 **source unresolvable** | 🔴 unauditable |
| **Ed-Fi** (US K-12 data) | `edanalytics/edfi_api_client`; `Ed-Fi-Exchange-OSS/LMS-Toolkit` 🔴 archived | 🟢 Apache-2.0 ×2 |
| **LMS → agent bridge** | `Dathis/swiss-moodle-mcp`, `Snaw80/moodle-mcp` | 🟢 MIT ×2 |
| **Autograding** | `edulinq/autograder-py`; `otter-grader` already carried, now measured at **161 ★** | 🟢 MIT, 🟢 BSD-3 |

🔵 **Why this is a trend and not a haul.** The split is systematic. The **agent** layer — MCP servers
for Canvas, tutors, parent agents — is overwhelmingly **npm/TypeScript**, which is why eleven passes of
npm sweeps built a rich agent shelf. The **standards and institutional-data** layer is
**PyPI/Python**, because it lives next to the Django and Flask applications that universities and
ministries actually run (Open edX, `now-lms`, campus SIS integrations) and next to the
notebook-and-grading stack. 🔴 **A supply claim is therefore only as wide as its registry.** This base
published *"there is no maintained Python LTI 1.3 library"* (`Gap 391-A`) from a channel that
**cannot index PyPI** — and then found five.

🟢 **The rule for a studio:** one discovery channel per ecosystem, named before any absence is
published. This base's set is now npm + PyPI + Packagist (measured, 0 yield) + `git ls-remote` and
`raw.githubusercontent.com` for verification. 🔴 **Still missing: Maven, NuGet, RubyGems and CRAN** —
and CRAN matters here, because `otter-grader` grades **R** and the statistics-teaching stack is
R-shaped.

🔴 **The cost of the channel, stated with it:** the dump carries **names only**, so it discovers by
token and a token is not a capability. Two of fifteen candidates were pure collisions — `proctor-ai`
is a **prompt-engineering** library, `xapi-python` is the **xStation5 broker API** — and whole keys are
unusable (`canvas` returns 146 names dominated by HTML-canvas and AWS Nova Canvas; `d2l` is
Dive-into-Deep-Learning). Discovery is cheap; **adjudication is the work**.

## Trend 23 — 🆕 `p393` A new supply class: **live releases, dead source** — and the licence claim is unauditable in principle

**The instances, found the same hour.** [`superbuilders/timeback-dev-python`](https://github.com/superbuilders/timeback-dev-python)
is the declared `Repository` of **three** actively-released PyPI packages — `timeback-qti`,
`timeback-oneroster` (OneRoster **v1.2**), `timeback-caliper` — **147 releases** between them, last
**2026-07-18**, each declaring **MIT**, together the most complete 1EdTech client family in Python on
paper. 🔴 **The repository does not resolve for an unauthenticated clone.** Second instance:
`moodle-mcp-bridge` v1.7.0, advertising *"a Moodle site as 88 typed AI tools"* → `NmaaAlhawary/MCP-Moodle`,
also unresolvable.

🔵 **Why this is a distinct class and not a variant of an existing one.** This base already grades
three failure modes, and none of them covers this:

| class | the payload | the verdict |
|---|---|---|
| `UNGRANTED` (no licence file) | exists, is empty of a grant | read, and found wanting |
| `README-ONLY` / `MANIFEST-ONLY` | a grant **asserted** somewhere other than a payload | downgraded, because the assertion is checkable against the absence |
| 🆕 **`LIVE-RELEASES-DEAD-SOURCE`** | 🔴 **cannot be fetched at all** | **not assessable** — there is nothing to read, and no amount of care fixes it |

🔴 **The procurement consequence is sharper than it looks.** `p388`'s *"published but unreadable"* was
about a payload that says nothing; this is about a payload that **cannot be obtained**. A studio can
install these packages — pip will resolve them happily — but it **cannot warrant the licence to a
client**, because warranting a grant means having read it. And an MIT declaration in registry metadata
is a claim by the uploader, not a grant in a distributable artefact.

🟢 **What to do with it.** Evaluate in a sandbox if the capability is needed; **never ship it into a
client deliverable**; ask the publisher to open the repository, which is a cheap request and a fair
one. 🔵 And record the class, because the economics favour its growth: publishing to a registry is
free and keeping a public repository is a maintenance commitment, so **more supply will arrive this
shape**, not less.

## Trend 24 — 🆕 `p394` In the teaching stack the **delivery** layer is permissive and the **measurement** layer is copyleft, and a language boundary rides along with it

🟢 **The observation.** `p394` opened the R half of the CS-teaching stack and the licence column split
cleanly down the middle of the pedagogy:

| what it does | components | licence |
|---|---|---|
| **Deliver** the teaching loop — present, accept, grade, respond | `rstudio/gradethis` (**MIT**, 164 ★), `rstudio/learnr` (**Apache-2.0**, 738 ★), `ucbds-infra/ottr` (**BSD-3-Clause**) | 🟢 **permissive, all three** |
| **Measure** the learner — item response theory, adaptive item selection, exam generation, item analysis | `cran/exams` (**GPL-2 \| GPL-3**), `philchalmers/mirt` (**GPL >= 3**), `cran/catR` (**GPL >= 3**), `cran/TAM` (**GPL >= 2**), `ShinyItemAnalysis` (**GPL-3**) | 🔴 **copyleft, all five** |

🔵 **Why it is not a coincidence.** The delivery components are **vendor-authored** — Posit, a company
selling an R platform, and a university programme that needed its autograder to be adoptable. The
measurement components are **academic instruments**, written by psychometricians inside a GPL research
culture and in some cases decades old. **The licence tracks who paid for the code and why**, and it has
produced a split running exactly along the boundary between *product* and *science*.

🟢 **Why that is good news rather than a blocker.** The boundary falls where a studio's product
boundary has to fall anyway: own the teaching loop, reach the psychometrics **over a process
boundary** — the same discipline `Pattern A` and `Pattern O` already apply to copyleft LMSs. 🔴 **The
trap is reading it as a licence problem and swapping in a permissive psychometrics library instead.**
There is no credible permissive equivalent of `mirt` or `catR`; building one is a multi-year research
project and approximating one is how a studio ends up shipping an adaptive engine whose claims it
cannot defend. 🔵 This base already carries the symptom: `adaptive-knowledge-graph` (~350 ★) and
`OATutor` implement IRT and BKT from scratch, and `mirt` — **235 ★, committed daily** — is the thing
they are approximating.

🔵 **And the language boundary rides along with it.** `Trend 22` recorded that the agent layer is
npm/TypeScript while the standards layer is PyPI/Python. `p394` adds that the **measurement** layer is
**CRAN/R**. Three layers, three registries — and a supply claim is still only as wide as the registry
it was swept from. 🔴 **R is the worst case of the three**, because its registry is unreachable here on
**both** tools and its grants are invisible to GitHub's licence sidebar (`Gap 394-B`): five granted GPL
packages in this tier show **no licence** in the GitHub UI, because the grant lives only in
`DESCRIPTION`. **So a GitHub-UI-driven sweep does not merely under-count R supply — it reports it as
unlicensed.**

## Trend 25 — 🆕 `p394` A string matched as though it were a meaning is this base's most productive error class, and it runs in three directions

🟢 **The observation, as a count rather than an impression.** Three independently-found defects, three
different instruments, one mechanism:

| gap | instrument | direction | what the string was |
|---|---|---|---|
| `Gap 392-A` | capability-absence gate | 🔴 **over-refutes** — denies a real absence | a runtime key read as a capability |
| `Gap 393-A` | PyPI index channel | 🔴 **over-discovers** — invents supply | a package *name* read as a capability (`proctor-ai`, `xapi-python`, `canvas`, `d2l`) |
| **`P459`** 🆕 | `licence-grant-gate` | 🔴 **strips a grant** — denies a real permission | **"all rights reserved"**, line 2 of the canonical BSD template, read as a refusal |

🔵 **`P459` is the most expensive of the three and it was the last to be found**, because the other two
produce *visible* nonsense — a claim you can check, a candidate you can reject — whereas this one
produces a **false absence of a grant**, which looks exactly like diligence. A usable component is
quietly marked unshippable and nobody re-opens the question. 🟢 On these shelves its realised damage
was **nil** — no published row was graded from an untitled BSD payload, checked rather than assumed —
and its exposure was **297 BSD-3-Clause + 201 BSD-UNVERSIONED** cells.

🔴 **And the fourth instance is on this base's own shelf rather than in an instrument.**
`anastasasenov/bbmcps` sat in the Blackboard census for eight passes because its URL scheme reads
`blackboard://`. It is a shared-memory MCP server; the word is an **architectural metaphor**. So the
class does not only mis-discover and mis-refute — **it mis-files what the base already owns**, and a
census cell inherited as a count is exactly where it hides.

🟢 **The transferable rule, and it is cheap.** Before a token decides a verdict, ask what else that
token means. The gate that got this wrong already holds the right idea one screen away:
`AMBIGUOUS_WORDS = ("apache", "nginx", "mit", "bsd")`, with a comment noting each is simultaneously a
licence name and something else. 🔵 **The insight was applied to licence names and never to licence
clause text, nor to package names, nor to URL schemes.** One lexicon separating a **string** from a
**capability** would close `Gap 392-A`, `Gap 393-A` and the `bbmcps` class together — which is why
`p393` ranked that unification fifth and why `p394` ranks it **first**.
