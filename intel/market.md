---
industry: education
region: Global
updated: 2026-10-09
---

## 🟢 Seventy-sixth pass, 2026-10-09 — the regional limbs are **saturated for a fourth pass (18/18 shelved)**, the EMEA channel is again **behind the shelf** on the same instrument, and `P849` stops this pass from inventing a LATAM channel it already holds

⏱️ **Eighth pass of this date.** Pass 75 closed earlier today. **Append-only: this section is new; nothing below it was rewritten. The live `## Opportunities by region` block is the one in this section; pass 75's has been retitled *superseded* per this file's convention.**

### 🟢 The channel audit, as a number, continuing pass 75's

| Probe class | Candidates returned | 🔴 Already shelved | 🟢 Unshelved |
|---|---|---|---|
| Repositories / agents (4 global queries) | **12** | **12** | 🔴 **0** |
| Regional players and institutions (4 regional queries) | **6** | **6** | 🔴 **0** |
| Regulatory / market / adoption facts | ~**26** | ~**26** | 🔴 **0** |
| 🆕 **Dependency closures of already-shelved components** | **8** | **4** | 🟢 **4** |

🔵 **The last row is new and it is the pass's methodological finding:** 🟢 **the only unshelved licence-bearing components this pass found came from CLOSURES, not from searches** — `jwcrypto`, `guzzle`, `phpseclib`, `php-jwt`, all at **0** prior occurrences, all one hop from libraries this shelf has held for dozens of mentions.

### 🔴 `P849` discharged, and it stopped a fabrication rather than a false gap

🔵 Pass 75's `P839` stopped a pass from declaring an EMEA gap the shelf refuted. 🔴 **This pass's failure mode was the opposite and worse: it was about to declare a LATAM channel NEW.**

🟢 This pass's LATAM limb returned the **IDB** technical note *An Enabling Regulatory Framework for Artificial Intelligence in Latin America and the Caribbean*, and the shelf-grep answered **`0 files, 0 hits`**. 🔴 **One keystroke from "the Inter-American Development Bank is a new channel for this shelf."**

🟢 **The grep was broken, not the shelf.** The probe passed a basic-`grep` alternation (`IDB\|Inter-American`) to `grep -E`, where `\|` is a **literal pipe**. 🟢 **Correctly run: `IDB` **22** hits, `iadb` **158** hits** — one of this shelf's most-cited LATAM sources.

🟢 **`P849`: validate a shelf-grep against a token known to be PRESENT before believing its zero.** 🔴 **A zero from a malformed pattern and a zero from an absent fact are indistinguishable, and they have opposite consequences** — the first manufactures a finding, the second records a gap.

### 🔴 The EMEA channel is behind the shelf, on the same instrument, for the seventh time

🟡 This pass's EMEA query returned: *"From 2 August 2026, the AI Office and national authorities started to enforce the AI Act"*, *"the Digital Omnibus on AI came into force in July 2026"*, and an older guide still treating **August 2026** as the high-risk deadline.

🟢 **All three are stale or imprecise against what this shelf holds, verified by three channels in pass 58:** 🔵 the **Digital Omnibus** is **`Regulation (EU) 2026/1744` of 8 July 2026**; the **Annex III high-risk** clock (which is the one education sits on) is **deferred to 2027-12-02**; and **Article 50 was NOT touched** — its clock runs unchanged. 🔴 **"General application 2 August 2026" is the exact stale claim this KB corrected in its nineteenth pass** (`P505`).

🟢 **Recorded as a re-confirmation of channel quality, not as a finding**, and 🔴 **`Gap 308` is not re-dated on it:** `eur-lex.europa.eu` refused a **ninth** time this pass (**000**, gateway 403 to CONNECT).

### 🟢 What the pass adds regionally: the transitive-licence finding, placed

🔵 **The substantive measurement is in `repos/foundations.md`** — the LTI 1.3 adapter's three implementation routes carry three different licence obligations, and the Python route is the only one with copyleft in its closure. 🟢 **It lands differently per region, and that is the part a regional engagement can use.**

## Opportunities by region

### North America

🟢 **Regulatory posture (all already shelved, re-confirmed this pass):** **35+ states** have AI guidance from their education departments; **134 bills** across **31 states** in 2026; **Ohio** required every district to adopt an AI policy by **2026-07-01**; **Maryland**'s 24 districts by **fall 2026**; **Oklahoma** `S.B. 1734` before **2027-28**; **Oklahoma and Maryland require human oversight and bar AI from high-stakes student decisions**; **Oregon** `S.B. 1546` adds minor-protection design duties; **NYC**'s red tier bars AI from grading, discipline and counselling.

🟢 **Opportunity — the approval gate is the sellable artefact, not the tutor.** 🔵 Two states mandate human oversight and one large district bars AI grading outright. 🟢 **`P850`'s step 2 is exactly that control in code:** `mcp-allowlist-gateway/gateway.py` with `putGrade` **floored** — refused *and never advertised*, so the model cannot even see the capability. 🔴 **A "teacher reviews it" policy is a slide; a floored tool is a measurement**, and the suite that proves it is 34/34.

🟡 **Opportunity — district-contract diligence.** State leaders recommend a data-usage-restriction clause in district contracts. 🟢 **`P851` produces the obligations memo and notices file that such a clause requires**, in 2–3 days for a ~40-dependency stack.

### EMEA

🟢 **Regulatory posture (shelved, re-confirmed):** education is **Annex III high-risk** under the EU AI Act when AI affects access, progression or assessment; the **Annex III clock is deferred to 2027-12-02** by `Regulation (EU) 2026/1744`; **Article 50** transparency is untouched. Proctoring with biometric identification carries bias-testing, human-oversight and notification duties.

🟢 **Opportunity — the deferral is a build window, and it is the strongest regional argument on this shelf.** 🔵 A client has until **2027-12-02** on Annex III but Article 50 is already running. 🟢 **Route A of `P850` is the compliance-shaped build:** Apache-2.0/BSD/MIT end to end, a floored grade-write for the human-oversight duty, and a notices file of four rows.

🔴 **And the licence route matters more here than anywhere.** 🟡 EMEA public-sector education procurement frequently requires source disclosure. 🟢 **Copyleft in the closure is less of a blocker for a public client — but `jwcrypto`'s LGPL-3.0 relinking duty still has to be ANSWERED, and Route A removes the question rather than arguing it.**

### APAC

🟢 **Regulatory posture (shelved, re-confirmed):** **Vietnam**'s AI law (passed 2025-12-10, effective **2026-03-01**) names education among six high-risk sectors, specifically **automated assessment and behavioural monitoring**; **South Korea**'s AI Framework Act took effect **2026-01-22** with 2026 as a pilot year and a one-year grace on penalties; **Taiwan**'s AI Basic Act passed December 2025; **China** enforces generative-AI measures plus synthetic-content labelling; **Singapore and Japan** remain voluntary-guideline.

🟢 **Opportunity — one codebase, per-jurisdiction policy, and the gate is the seam.** 🔵 Vietnam names *automated assessment* high-risk; Singapore does not regulate it; Korea is in a grace period. 🔴 **A per-country fork is the expensive answer.** 🟢 **The cheap one is `P850` with the allowlist/floor as configuration:** the same adapter ships everywhere and the **floor set** is the jurisdiction variable — `putGrade` floored in Vietnam, advertised in Singapore.

🟡 **Honest gap, declared rather than left silent:** 🔴 **no APAC-specific school or university ADOPTION rate was returned by this pass's channel**, and the market figures it offered (an "APAC AI market ≈ USD 102 bn" aggregate, and a vendor list naming Google, Microsoft, IBM, Pearson and Byju's) are 🔴 **commercial-report single-channel and are NOT adopted.**

### LATAM

🟢 **Regulatory and adoption posture (shelved, re-confirmed):** UNESCO **IESALC**'s September 2026 study of **200 institutions in 19 countries** — **87%** use AI in at least one area, **74%** in teaching, 🔴 **only 26% have any formal framework** (private non-profits **84%** vs public **68%**); secondary-teacher use **Brazil 56% · Chile 55% · Colombia 53% · Costa Rica 52%** against an **OECD average of 36%** (TALIS 2024); **Uruguay** reports **75%** of public-school teachers. 🟡 Legislation is unfinished: **Brazil** `PL 2.338/2023` through the Senate and in the Chamber; **Chile**'s bill in committee; **Colombia** policy-first via **CONPES 4144**. Named actors: UNESCO IESALC and its **Observatory on AI in Education** (launched 2026-04-14), the **IDB**, the Digital Education Council's LATAM survey, **Ceibal** (Uruguay), FLACSO Ecuador.

🟢 **Opportunity — the 87%/26% gap is a governance engagement, and this pass gives it a deliverable.** 🔵 Adoption is near-universal and frameworks are not. 🟢 **`P851` is the artefact that closes it concretely:** a payload-read obligations memo plus notices file, which an institution with no framework can adopt as its first one. 🔵 **The IDB's own argument — enabling regulation as catalyst, and the warning that purely national approaches fragment a ~650 million-person market — is the pitch for doing it once regionally.**

🟡 **And the licence route is a procurement argument here specifically:** 🟢 public universities buying under constrained budgets reuse deliverables across institutions, 🔴 **which is exactly when a copyleft relinking duty in the closure surfaces.** 🟢 Route A ships with four permissive rows and no question to answer.

### Global

🟢 **Market figures, carried unchanged and still disputed between sources:** AI-in-education **USD 10.6 bn (2026) → USD 42.48 bn (2030), CAGR 41.5%** (Research and Markets), against a vendor-sourced **USD 12.3 bn by 2026**; Europe **USD 2.64 bn (2026) → USD 8.0 bn (2030), CAGR 31.9%** 🟡 (single-channel, methodology unverified, **not adopted as this shelf's figure**). 🟢 **86%** of education organisations use generative AI while most lack a policy; **54%** of K-12 and **92%** of university students use AI; weekly-using teachers report **~5.9 h/week** saved.

🟢 **Opportunity — the cross-region constant.** 🔵 Every region above regulates the same two acts: **automated assessment** and **human oversight of it**. 🟢 **So the one component worth building once and reselling everywhere is the gated AGS writer of `P850`** — the jurisdiction changes the floor set, not the architecture.

## 🟢 Seventy-fifth pass, 2026-10-09 — the battery is **saturated on the regional limbs too** (13/13 shelved); 🔴 **the regional figures' internal consistency does NOT survive a fourth channel**; `P839` stops this pass from declaring an EMEA gap the shelf itself refutes

⏱️ **Seventh pass of this date.** Pass 74 closed earlier today. **Append-only: this section is new; nothing below it was rewritten. The live `## Opportunities by region` block is the one in this section; pass 74's has been retitled *superseded* per this file's convention.**

### 🟢 The channel audit, as a number, continuing pass 74's

| Probe class | Candidates returned | 🔴 Already shelved | 🟢 Unshelved |
|---|---|---|---|
| Repositories / agents (4 global queries) | **7** | **7** | 🔴 **0** |
| Regional players and institutions (4 regional queries) | **6** | **6** | 🔴 **0** |
| Regulatory / market / adoption facts | ~**22** | ~**19** | 🟢 **3** |

🟢 **The three genuinely absent:** the **North American 2029 forecast** below, the **Carnegie Mellon / Gates Foundation $55 million** courseware commitment, and **Baker McKenzie** as a named channel on LATAM regulatory fragmentation (0 occurrences; it *confirms* a position this shelf already holds rather than adding one).

### 🔴 `P839` discharged, and it stopped a false gap before it was written

🔵 **This pass's EMEA query returned almost nothing education-specific** — CompTIA's IT outlook, a Workday study from its **2023** edition, a general enterprise-AI barriers report. 🔴 **The tempting write-up was "no EMEA education material found this pass."** 🟢 **`P839` requires grepping the shelf before declaring a gap, and the shelf refutes it flatly:**

| what the shelf holds on EMEA | measured |
|---|---|
| `### EMEA` blocks in this file | 🟢 **dozens**, one per pass |
| `Annex III` | 🟢 **10 files** |
| `GDPR` | 🟢 **9 files** |
| France / Germany / Nordic / Gulf / UAE / Saudi | 🟢 **10 / 7 / 7 / 8 / 9 / 4 files** |
| the EU AI Literacy Framework, OECD Digital Education Outlook 2026 | 🟢 held, pass 74 |

🔴 **And the decisive one, which this shelf had already written down:** line **54** of this file records that the query `AI education EMEA Europe 2026 adoption regulation players` — **verbatim from the prompt that schedules these passes** — was already run and already recorded as spent. 🟢 **So the thinness is a property of the CHANNEL, not of the region and not of the shelf.** 🔵 **Pass 73 made precisely this mistake on APAC and `P839` was written to stop it; this is the first pass where it actually fired.** 🟢 **No EMEA gap is declared. EMEA remains the best-documented regulatory region on this shelf.**

### 🔴 The regional figures were praised for cross-checking. A fourth channel breaks that

🔵 Pass 73 recorded the regional figures as *"the first on this shelf that are internally consistent with each other"* — **North America $3.68B in 2026**, claimed **36 %** of global, implying ~$10.2B global, within 4 % of the Research-and-Markets $10.6B. 🟢 **That cross-check was real and is not withdrawn.**

🔴 **This pass's channel gives a North American series that cannot be reconciled with it:**

| source | North America | year | horizon |
|---|---|---|---|
| shelf (pass 73, two channels) | 🟢 **$3.68B** | 2026 | $32B by 2030 |
| this pass's channel | 🔴 **$951M** | 2024 | 🔴 **$2 303.2M by 2029**, 15.9 % CAGR |

🔴 **The second series puts 2029 at $2.30B — below what the first puts 2026 at, and an order of magnitude below its 2030.** 🟢 **No reconciliation is attempted and no figure is adopted.** 🔵 **What this changes is a claim about the shelf's own confidence, which is why it is recorded rather than dropped:** regional figures are **not** better-behaved than global ones — pass 73's two happened to agree, and a third disagrees by ~14× at the horizon. 🟡 **`Gap 308` is a global-figure gap in its wording and a regional one in fact.** 🟢 The same channel also restated the global spread at **$6.4B (2025) → $79.6B (2034)**, **$8.3B → $11.4B (2026)** and **$7.52B → $10.6B (2026)** — 🔴 **three mutually inconsistent series in one result set**, which is the eighth pass in a row this has happened.

### 🟢 The one genuinely new North American datum worth a studio's attention

🟢 **Carnegie Mellon University and the Gates Foundation have committed $55 million to AI courseware targeting gateway college courses** (the high-failure first-year courses that gate degree progression), and 🟡 **OpenAI is reported to have launched a country-level education programme with eight national partners in Q1 2026.** 🟡 **Both single-channel and secondary; neither is adopted as a market figure.** 🔵 **The first is directionally important because gateway courses are exactly where an auditable, human-in-the-loop assessment pipeline is both pedagogically justified and legally exposed** — the artefact this shelf has been describing for ten passes.

## Opportunities by region — superseded (the live block is at the top of this file)

### North America

🟢 **The standing position is unchanged and this pass makes it cheaper to quote.** The oversight cluster — **Ohio** (every K-12 district on a formal AI-use policy, deadline **2026-07-01**, now past), **Oklahoma SB 1734**, **Connecticut**'s human-oversight requirement for AI-assisted grading, plus piecemeal **Colorado** and **Texas** requirements — is a **product requirement**, and the component exists on this shelf (`littlecookie0722/AI-Teaching-Agent`'s contract-specified review gate).

🟢 **New this pass, and it removes a contingency rather than adding a feature:** 🟢 **the LMS-seam library's licence closure is now measured clean** — `ltijs@7.0.7` Apache-2.0 over **10 runtime dependencies, 9 payload-verified MIT, zero copyleft, zero sourceless** (`repos/foundations.md`). 🔵 **An oversight-and-audit engagement built on it can be quoted without a licence contingency**, which is the first time that is true of any protocol hop on this shelf. 🔴 **One named exception to carry into the SOW:** `sprightly` ships no copyright notice, so the deployment's third-party notices file must be populated by hand.

🟡 **The demand-side caution carried from pass 74, unchanged and still single-channel:** faculty intent fell **76 % → 67 %** (2025→2026), with only **22 %** of higher-education faculty regular AI users against **83 %** of K-12 teachers. 🔵 **Sell K-12 and administration before faculty-facing tooling.**

### EMEA

🟢 **Still the best-documented regulatory region on this shelf, and no gap is declared** (see `P839` above). 🟢 **Not in dispute:** the EU AI Act classifies AI used in educational access, progression and assessment — admissions, evaluation, exam scoring, proctoring — as **high-risk under Annex III**. 🔴 **In dispute, for the eighth pass:** whether those obligations bite at **2026-08-02** or are deferred to **2027-12-02** / **2028-08-02** by the Digital Omnibus, `Regulation (EU) 2026/1744` of **8 July 2026** — `Gap 308`, refused again this pass on two channels and the proxy's own ledger.

🟢 **Where the studio sells, unchanged:** **Annex III conformity work** — documentation, logging, human oversight, accuracy and robustness evidence — built once and shared with North America, whose oversight mandates ask for the same artefact. 🔵 **The 57 %-of-students-report-inadequate-assessment-guidance figure is the assessment-policy engagement**, procurable today and independent of the date dispute. 🟡 **MEA named rather than folded into "Europe":** UAE **National AI Strategy 2031**, Saudi **SDAIA**; Kenya, South Africa and Nigeria drafting. 🔴 **No education-specific MEA instrument on this shelf yet** — and that gap *is* grep-verified, unlike the EMEA one this pass declined to invent.

### APAC

🟢 **Holds the clearest education-specific AI regulation anywhere.** **Vietnam's high-risk list names education explicitly** — automated assessment and behavioural monitoring (**33/2026/QD-TTg**, decree **142/2026/ND-CP**). 🟢 **Curriculum mandates:** **India — AI and computational thinking compulsory from Class 3** in **2026-27**, backed by the IndiaAI Mission; China's reported compulsory-from-age-6 programme. 🟡 **Readiness order:** Singapore, then Australia, Korea, Taiwan.

🟡 **This pass's channel adds commercial rather than regulatory signal, all of it already shelved:** the **TCS × Pearson** multi-year learning alliance, **LearnUpon**'s Sydney HQ with `Create+` AI authoring, **NIIT MTS**, **Alteryx** Academy, and **OpenAI**'s ANZ policy appointment as Canberra tightens AI governance and copyright rules. 🔴 **Singapore's current consultation is on AI in FINANCIAL institutions, not education** — recorded because it is easy to miscount as an education instrument.

🔴 **Pass 74's standing limb is re-confirmed and stays open:** there is still **no APAC education-ministry instrument on student DATA specifically** — the one limb of pass 73's withdrawn gap that survived. 🟡 This pass's governance datum is enterprise-wide, not education: **87 %** of organisations encourage AI-agent use, **47 %** have governance for it.

🟢 **Where the studio sells:** **Vietnam and Korea** remain the two most tractable compliance engagements — Vietnam because the obligation is in force and names assessment, Korea because the grace period makes 2026 the year to build before penalties attach. 🔵 **Sovereignty is the infrastructure constraint** (~half of APAC firms), which favours the self-hostable permissive stack this shelf curates over hosted vendors.

### LATAM

🟢 **Still the best-evidenced region, and the evidence is institutional rather than vendor.** 🟢 **UNESCO IESALC with UNU-IAS, 200 higher-education institutions across 19 countries (surveyed Aug–Oct 2025): 87 % use AI in at least one area; only 26 % have any formal framework; teaching leads at 74 %.** 🟡 Re-confirmed by this pass's channel, which also dates the publication to **September 2026** — 🟢 consistent with the shelf.

🟡 **Regulation is general-purpose, not education-specific**, and this pass adds a fourth channel saying so: **Baker McKenzie** reports most LATAM countries without harmonised AI law, with privacy, consumer-protection, labour, cybersecurity and IP regimes already constraining deployments. 🟢 **Brazil's PL 2.338/2023** sits in the Chamber of Deputies; 🟢 **ANPD's AI-and-data-protection regulatory sandbox runs through December 2026** — the only compliance on-ramp in the region a studio can actually enter. 🟡 **CENIA**: the region is the third-largest market worldwide for generative-AI application downloads.

🟢 **Where the studio sells:** 🟢 **the 87 %-use / 26 %-framework gap — 61 points — is the offer, and it is a governance engagement before it is a build.** 🟢 **Public institutions are the underserved half.** 🔴 **Caveat carried forward:** the 200-institution UNESCO sample and the 29-institution Digital Education Council survey are **not comparable** and are not compared here.

### Global

🟢 **Cross-regional, and it is what places the rest:** all four regions want the **same** artefact — an auditable, human-in-the-loop assessment and feedback pipeline a regulator or accreditor can inspect. North America mandates the oversight in at least five states, EMEA classifies it high-risk, APAC legislates it by name in Vietnam, LATAM needs it as governance.

🔴 **The blocker is identical in all four and it is two-sided:** of every LMS and SIS this shelf has censused — Moodle **GPL-3.0**, Canvas **AGPL**, Open edX **AGPL-3.0**, OpenEduCat **LGPL-3.0** — 🔴 **0 of 6 are permissive**, and the permissive agents never reach for the protocol (`DeepTutor`: **0 LTI / 0 xAPI / 0 Caliper / 0 SCORM / 0 OneRoster** across 3 763 files).

🟢 **What moved this pass:** the **licence** half of that seam is now measured, not assumed. 🟢 **`ltijs` — the one library this shelf says closes the hop — carries an Apache-2.0 grant in its published artefact over a closure of 10 dependencies that is 9/10 payload-verified MIT and free of copyleft.** 🔵 **So the remaining cost of the seam is engineering only** (`Gap 316(i)`'s wiring limb, still the highest-value unmeasured number here) **with no licence contingency behind it** — and that is a materially more sellable position than the one this shelf carried into today.

## 🟢 Seventy-fourth pass, 2026-10-09 — the prescribed search battery is **measurably saturated**: **0 unshelved repositories in 17 probed** and 2 unshelved facts in ~45; 🔴 **pass 73's declared APAC gap is contradicted by pass 72's own block, 70 lines below it in this file**; `Gap 308` refused a **seventh** time on a **wider** spread

⏱️ **Sixth pass of this date.** Pass 73 and its correction `73-C` closed earlier today (commit `7ce7b79`). **Append-only: this section is new; nothing below it was rewritten. The live `## Opportunities by region` block is the one in this section; pass 73's has been retitled *superseded* per this file's convention.**

### 🔴 The finding that matters most, and it is about this shelf rather than the market

🔴 **Pass 73's `### APAC` subsection declares:** *"The gap, stated plainly: this pass found no APAC education-ministry policy, no national AI-in-schools curriculum, and no student-data rule specific to the region."*

🔴 **That gap was already filled, in this same file, seventy lines below the sentence that declares it.** Pass 72's `### APAC` block (line 110) reads:

> **India**: AI and computational thinking become **mandatory from Class 3** across government and private schools in **2026-27**, backed by the IndiaAI Mission

🟢 **Measured, not asserted:** `grep -rlF "Class 3" --include=*.md` returns **6 files**, among them `intel/market.md` itself at lines **110**, **4 579**, **4 713** and **5 170**, with a ₹500 crore centre of excellence and the ₹10 372 crore India AI Mission attached. 🔴 **A national AI-in-schools curriculum, for the largest school system in the region, recorded by at least four prior passes of this very file.**

🔵 **This is `73-C`'s failure in its second shape, and the rule it breaks is the one `73-C` wrote.** `P835` says *grep the shelf for the candidate before writing a row as new.* 🔴 **The symmetric case was never stated and is the one that bit here: grep the shelf before declaring something ABSENT.** A false "new row" costs a duplicate; a false "informed gap" costs worse, because this shelf treats a declared gap as a research instruction and pass 73 pointed the next pass at ministry-direct research it did not need. 🟢 **`P839` adopted** — see `intel/open-gaps.md`.

🟡 **What survives of pass 73's APAC caveat, narrowed to what is actually missing:** the shelf holds national *curriculum* instruments (India, China) and binding *AI* law naming education (Vietnam, Korea). 🔴 **What it still does not hold is an APAC education-ministry instrument on student DATA specifically.** 🟢 That third limb is a real gap; the first two were not.

### 🔴 `Gap 308` — market size **refused for a seventh pass, and the spread widened**

🟢 **Re-probed on the global channel this pass.** 🔴 **The disagreement did not narrow — it grew:**

| Source | 2026 figure | Horizon |
|---|---|---|
| (shelf, carried six passes) | **$1.94B** — low end | — |
| Precedence Research | **$9.58B** | $136.79B by 2035 |
| Research and Markets | **$10.6B** | $42.48B by 2030 @ 41.5 % |
| 🆕 Grand View Research | **$11.40B** | — |
| 🆕 unattributed, same channel | **$10.4B** | $32.27B by 2030 @ 31.2 % |

🔴 **$1.94B – $11.40B is a 5.9× spread**, against the 5.5× this shelf has refused since the sixty-eighth pass. 🟢 **Grand View's $11.40B is the first figure to move the TOP of the range**, and it moves it the wrong way for anyone hoping the channel converges. 🔵 **One channel even reports its own spread: four firms priced 2026 between $6.4B and $11.4B.** 🟢 **No global figure adopted, for the seventh consecutive pass. Nothing on this shelf is sized by one.**

🟡 **The one sub-segment figure that behaves:** higher education at **$4.09B** (2026) → **$13.46B** by 2030 @ **34.7 %**. 🟡 Against the implied ~$10.2B global this shelf computed last pass, that is ~40 % of the market in higher ed alone — 🔴 **which is high enough to suggest the sub-segment and the global figure use different definitions.** 🟢 Recorded as a definitional warning, not adopted.

### 🟢 The channel audit, stated as a number so the next pass can price the channel

🟢 **Every candidate the prescribed battery returned was grepped against the shelf per `P835` before anything was written:**

| Probe class | Candidates returned | 🔴 Already shelved | 🟢 Unshelved |
|---|---|---|---|
| Repositories / agents | **17** | **17** | 🔴 **0** |
| Regulatory, market and adoption facts | ~**28** | ~**26** | 🟢 **2** |

🟢 **The two that were genuinely absent:** **Squirrel AI** (0 occurrences — a *closed* Chinese adaptive-learning vendor used in classrooms, so a market-map player and not a build-on candidate) and **Connecticut** (0 occurrences — reported to require human oversight of AI-assisted grading, which extends a rule this shelf already holds for Oklahoma, Maryland and Virginia).

🔴 **And the channel returned material BEHIND the shelf.** Asked for the EMEA regulatory position, it reported the Digital Omnibus as *"still awaits publication in the Official Journal"*. 🟢 **This shelf has held it as `Regulation (EU) 2026/1744` of **8 July 2026** since a prior pass** — a named, dated, published instrument. 🔵 **A channel that reports a superseded status as current cannot be used to re-date `Gap 308`, which is exactly what six passes have tried to do with it.**

🔴 **The most economical evidence that this battery is spent:** the query `AI education EMEA Europe 2026 adoption regulation players` — **verbatim from the prompt that schedules these passes** — is already recorded in `repos/trending.md:6616` with its result. 🟢 **The battery is now a re-confirmation instrument, not a discovery one, and should be priced as one.**

## Opportunities by region — superseded (the live block is at the top of this file)

### North America

🟢 **The regulatory surface is still the opportunity, and this pass adds a fourth state to the oversight cluster.** 🟢 **Ohio** remains the first state to require every K-12 district to adopt a formal AI-use policy (deadline **2026-07-01**, now past); **Oklahoma SB 1734** carries educator supervision, no high-stakes AI decisions, annual parent disclosure and a written policy before **2027-28**; **Maryland** runs a 24-district / 120-day rolling clock; **Virginia** requires human oversight of AI-assisted grading; 🆕 **Connecticut is reported in the same posture** — human oversight of any AI-assisted grading. 🔵 **California AB 1159** would bar student data from training models absent direct school benefit. 🟡 **Alabama HB 329** makes an AI-inclusive CS course a graduation requirement.

🔴 **The new signal this pass, and it is negative:** 🔴 **faculty intent to use AI in the US and Canada fell 9 points, from 76 % (2025) to 67 % (2026)**, and 🔴 **only 22 % of higher-education faculty are regular AI users against 83 % of K-12 teachers.** 🟡 **Both are single-channel and secondary-sourced; this shelf had neither recorded.** 🟢 **If it holds, it is the first *falling* adoption series on this shelf** and it inverts the usual sales motion: the K-12 teacher is ahead of the professor.

🟢 **Where the studio sells:** 🟢 **the human-oversight mandate is a product requirement and the component exists on this shelf** — `littlecookie0722/AI-Teaching-Agent`'s review gate is contract-specified (`publishBlockedUntilApproved: true`, `autoPublishAllowed: false`) and exercised by real tests (`Gap 323`). 🔵 **Five states' "no high-stakes AI decisions" language is satisfiable by that one gate and demonstrable to a procurement committee.** 🔴 **The faculty-intent decline says higher education is the harder sell of the two in 2026**; the K-12 district, with a statutory policy deadline, is the warmer one. 🟡 **District-level bans remain a design constraint, not an excluded market:** teacher-facing and administrative workflows are untouched by the NYC K-8 student-facing moratorium.

### EMEA

🟢 **The obligation's content is settled on this shelf and its date is not** — `Gap 308`, refused a seventh time. 🟢 **Not in dispute:** the EU AI Act classifies AI used in educational access, progression and assessment — admissions, student evaluation, exam scoring, proctoring — as **high-risk under Annex III point 3**, and it reaches **non-EU systems whose outputs affect EU-located students**. 🟢 **Also not in dispute, and it binds today:** **emotion recognition in an education institution has been prohibited since 2026-02-02**, and the Article 4 AI-literacy duty is live.

🔴 **In dispute, still:** whether the high-risk obligations bite at **2026-08-02** or are deferred to **2027-12-02** (standalone) and **2028-08-02** (embedded in regulated products) by the Digital Omnibus — `Regulation (EU) 2026/1744` of **8 July 2026**. 🟡 **This pass's channel added a fourth variant** — transparency obligations at **2026-11-02** rather than **2026-08-02**. 🔴 **No date adopted.** 🔵 **And the channel that offered the new variant simultaneously reported the Omnibus as unpublished, which this shelf knows to be false — so it is recorded as a conflict, not as evidence.**

🟢 **Direction of travel, institutional rather than vendor:** 🟢 **the European Commission and the OECD, with G7 endorsement, have a draft AI Literacy Framework for primary and secondary education**, and 🟢 **the OECD's 2026 Digital Education Outlook recommends moving from general-purpose AI to purpose-built educational AI** — this shelf's own thesis, from a standards body.

🔴 **The demand-side constraint is measured and it is not technical:** **88 %** student adoption across 35 countries (Digital Education Council 2026), against **57 %** of students saying their assessments come with inadequate AI guidance and **77 %** reporting no formal AI training at all (Microsoft, six countries). 🟡 **Funding is cooling:** edtech venture funding **$1B in H1 2026, down 26 %** from $1.35B in H1 2025 (HolonIQ).

🟡 **Middle East and Africa, named rather than folded into "Europe":** the UAE's **National AI Strategy 2031**, Saudi Arabia's **SDAIA** framework; Kenya, South Africa and Nigeria are drafting AI policies. 🔴 **No education-specific instrument was found for any MEA country this pass either.** 🟢 **Second consecutive pass declaring this gap, and it is declared rather than left silent.**

🟢 **Where the studio sells:** 🟢 **Annex III conformity work** — documentation, logging, human oversight, accuracy and robustness evidence — built once and shared with North America. 🔵 **The 57 %-inadequate-guidance figure is the assessment-policy engagement**, and it is procurable today regardless of which of the four dates is right, because it is institutional policy rather than statutory compliance. 🔴 **Carry the caveat: this shelf cannot date the obligation and will not quote one of four contested dates.**

### APAC

🟢 **This region holds the clearest *education-specific* AI regulation anywhere, and — contrary to pass 73 — the clearest national curriculum mandates too.** 🟢 **Vietnam's high-risk AI list names education explicitly** — automated assessment and behavioural monitoring (**33/2026/QD-TTg**, six sectors; decree **142/2026/ND-CP**); its Law on Artificial Intelligence passed **2025-12-10** and took effect **2026-03-01**. 🟡 **South Korea's AI Basic Act took effect 2026-01-22**, with a signalled **one-year grace period on penalties**. 🟡 **Taiwan** passed an AI Basic Act in December 2025. 🔴 **China** enforces binding rules on algorithms, deep synthesis and generative AI. 🟢 **Japan** stays light-touch — the **AI Promotion Act** plus a second **AI Basic Plan** approved **14 July 2026**, a strategy document rather than law.

🟢 **The curriculum limb, restored from this shelf's own record:** 🟢 **India — AI and computational thinking mandatory from Class 3** across government and private schools in **2026-27**, backed by the IndiaAI Mission (₹10 372 crore) and a ₹500 crore centre of excellence; ~**10 M teachers** need training against **15 %** AI-fluent in a 2025 survey. 🟡 **China — AI reported as compulsory from age 6, with Beijing schools owing every student ≥8 hours a year.** 🔴 **Single secondary channel for the China figures; not adopted as fact.**

🟡 **Readiness and acceptance, two axes worth separating:** implementation readiness runs **Singapore, then Australia, Korea, Taiwan**, with Japan, India and China behind on diffusion despite scale. 🔴 **Japan's constraint is measured and severe:** generative-AI use among the Japanese public was **26.7 % (2024)** against **68.8 %** in the US and **81.2 %** in China, per Japan's Ministry of Internal Affairs and Communications. 🟡 **Public acceptance (Ipsos Education Monitor 2026)** — support for banning AI in schools runs Indonesia **23 %**, India **26 %**, Singapore **28 %**, Japan **29 %**, Korea **31 %**, i.e. 🟢 **lower resistance than Australia and New Zealand**. 🟡 **Players:** `Embibe` (India, AI tutoring) and 🆕 **`Squirrel AI`** (China, adaptive learning in classrooms) — 🔴 **both closed; neither is a build-on candidate.**

🟢 **Where the studio sells:** 🟢 **Vietnam and Korea remain the two most tractable compliance engagements on this shelf** — Vietnam because the obligation is in force and names assessment specifically, Korea because the grace period makes 2026 the year to build before penalties attach. 🔵 **Both want the same artefact as EMEA and North America: an auditable human-in-the-loop assessment pipeline.** 🟢 **India is the volume play and it is a teacher-training problem before it is a product problem** — 10 M teachers against 15 % fluency, with a curriculum deadline already set. 🔴 **The gap that is actually still open: no APAC education-ministry instrument on student DATA specifically.** 🟢 Narrowed from pass 73's three limbs to this one.

### LATAM

🟢 **Still the best-evidenced region, and the evidence is institutional rather than vendor.** 🟢 **UNESCO IESALC, 200 higher-education institutions across 19 countries: 87 % use AI in at least one area; only 26 % have any formal framework.** 🟢 **Teaching leads at 74 %.** 🟡 **By sector:** private non-profit **84 %**, public **68 %**, private for-profit **52 %**. 🟢 **School level:** TALIS 2024 put Brazil, Chile, Colombia and Costa Rica **above the OECD average of 36 %** for secondary-teacher AI use; **Ceibal (2026) reports 75 % of Uruguayan public-school teachers** using these tools. 🟡 **The IDB's review of 193 initiatives** found **59 %** using generative AI, **27 %** language models and **24 %** NLP, with Rio de Janeiro's education secretariat automating school-invoice validation — 🔵 **an administrative use case, which is where the region's near-term money actually is.**

🟡 **Regulation is general-purpose, not education-specific:** Brazil's **PL 2.338/2023** sits in the Chamber of Deputies; 🟢 **Brazil's ANPD runs a pilot AI-and-data-protection regulatory sandbox through December 2026** — 🔵 **a compliance on-ramp, and the only one in the region a studio can actually enter**; Chile's bill is in its first constitutional stage; 🟢 **Colombia took a policy-first route with CONPES 4144 (February 2025)**, budgeted through 2030. 🟢 **UNESCO's regional Observatory on AI in Education for LAC launched 14 April at ECLAC in Santiago**, with a Mexico pilot alongside **CONALEP and DGETI**. 🟡 **Google.org committed $4.6M across nine countries including Brazil and Mexico, targeting 1.25 M students by 2028.**

🟢 **Where the studio sells:** 🟢 **the 87 %-use / 26 %-framework gap is the offer, and it is a governance engagement before it is a build** — 61 points of institutions using AI with no framework, on a clock set by reputational risk rather than statute. 🟢 **Public institutions are the underserved segment** (68 % vs 84 %). 🟡 **Uruguay is the standout pilot market** at 75 % teacher adoption with Ceibal as a national counterparty; 🟡 **Brazil is the volume market** at **45 %** of HolonIQ's LATAM EdTech 100, with **54 %** of teachers having had recent digital-technology training and GenAI course enrolments up **425 %** year on year.

🔴 **One honest caveat, carried forward:** the 200-institution UNESCO sample and the 29-institution Digital Education Council survey are **not comparable** and are not compared here.

### Global

🟢 **Cross-regional, and this is what places the rest:** all four regions want the **same** artefact — an auditable, human-in-the-loop assessment and feedback pipeline a regulator or accreditor can inspect. 🟢 **North America mandates the oversight in at least five states, EMEA classifies it high-risk under Annex III, Vietnam names assessment explicitly, LATAM has 61 points of ungoverned adoption to remediate.** 🟢 **Built once, sold four times.**

🔴 **And the blocker is identical in all four: the LMS seam, which is two-sided.** 🟢 **The licence side was re-confirmed this pass from an independent channel and it did not move:** of every LMS and SIS the channel named — Moodle **GPL-3.0**, Canvas **AGPL**, Open edX **AGPL-3.0**, Frappe LMS **AGPL-3.0**, OpenEduCat **LGPL-3.0**, Sakai **ECL-2.0** — 🔴 **not one is MIT, Apache-2.0 or BSD.** 🔴 **The implementation side was measured last pass:** `DeepTutor` (Apache-2.0, 3 763 files) and `OpenTutor` (MIT, 890 files) hold **zero** LTI, xAPI, Caliper, SCORM or OneRoster paths between them. 🔵 **So the permissive tutors do not reach for the protocol and the protocol-speaking platforms are all copyleft.** 🟢 `ltijs` (Apache-2.0) remains the one-hop closer — see `compose/patterns.md`.

## 🟢 Seventy-third pass, 2026-10-09 — **all four regions return substantive material for the first time in this file's history**, and the regional figures are the first on this shelf that are internally consistent with each other

⏱️ **Fifth pass of this date.** Pass 72 closed earlier today (commit `e99be83`). **Append-only: this section is new; nothing below it was rewritten. The live `## Opportunities by region` block is the one in this section; pass 72's has been retitled *superseded* per this file's convention.**

### 🔴 Market size — **refused for a sixth pass**, but the regional figures behave better than the global ones

🟢 The global spread this shelf has recorded for six passes is unchanged: **$1.94B – $10.6B** for 2026, a **5.5×** spread on the same nominal market. 🟢 **No single global figure is adopted.**

🟡 **New this pass — two regional figures that at least cross-check:**

| Region | 2026 figure | Horizon | Cross-check |
|---|---|---|---|
| North America | **$3.68B**, claimed **36 %** of global | $32B by 2030 | 🟡 $3.68B ÷ 0.36 ≈ **$10.2B implied global** — within 4 % of the Research-and-Markets $10.6B |
| EMEA (Europe) | **$2.64B** | $8.0B by 2030 @ 31.9 % | 🟡 ≈ 26 % of the same implied global; NA + Europe ≈ 62 %, which is plausible for this sector |

🟢 **This is the first time two independently sourced regional figures on this shelf have been arithmetically compatible with a third global one.** 🔴 **It does not make any of them right** — all three are market-research products with undisclosed method, and the 36 % share is itself a vendor claim. 🟢 **Recorded as a consistency observation, not as an adopted size. Nothing on this shelf is sized by it.**

## Opportunities by region — superseded (the live block is at the top of this file)

### North America

🟢 **The regulatory surface is the opportunity here, and it is unusually concrete.** 🟡 **134 bills** on AI in education introduced across **31 states** in 2026; **30+ states** have guidance documents; 🟢 **Ohio is the first state to require every K-12 district to adopt a formal AI-use policy, by 2026-07-01.** 🟢 **Oklahoma and Maryland require human oversight and bar AI from high-stakes decisions about students.** 🔵 California's **AB 1159** would bar student data from training models absent direct school benefit; Idaho's **SB 1227** mandates a statewide framework. 🟡 Federal movement is slower: **H.R. 8747** (K-12 AI Literacy and Readiness Act of 2026) advanced from committee markup on 2026-07-21.

🟢 **Adoption is real, not pilot-stage:** **60 %** of US K-12 teachers used AI tools in the 2024-25 school year, **32 %** at least weekly. 🟡 A vendor-sourced claim puts **86 %** of North American education organisations on generative AI.

🟢 **Where the studio sells:** 🟢 **the human-oversight mandate is a product requirement, and this shelf now has the component for it** — `littlecookie0722/AI-Teaching-Agent`'s review gate is specified in a contract (`publishBlockedUntilApproved: true`, `autoPublishAllowed: false`) and exercised by real tests (pass 72, `Gap 323`). 🔵 **Oklahoma/Maryland-style "no high-stakes AI decisions" is satisfiable by that gate and demonstrable to a procurement committee.** 🟡 **District-level bans are a live constraint to design around, not a market to ignore:** Katy ISD (TX) bars generative chatbots K-6; NYC has a one-year student-facing moratorium through grade 8. 🟢 **Teacher-facing and administrative workflows are unaffected by both**, which is where the near-term work is.

### EMEA

🔴 **The single most load-bearing date for this region is contested across three secondary channels, and this shelf cannot resolve it** — `Gap 308`, now refused six times. 🟢 **What is not in dispute:** the EU AI Act classifies AI used in educational access, progression and assessment — admissions, student evaluation, exam scoring — as **high-risk (Annex III)**, and it reaches **non-EU systems whose outputs affect EU-located students**. 🔴 **What is in dispute is when the obligations bite:** one channel says the Digital Omnibus defers them from 2026-08-02 to **2027-12-02**; a second, quoting the Commission's own page, says the omnibus amendments entered into force **2026-07-27** and that enforcement **began 2026-08-02**; a third dates the Council/Parliament provisional agreement to **2026-05-07**. 🟢 **No date is adopted. Every EMEA estimate on this shelf is marked secondary-sourced and contested.**

🟢 **Adoption and players:** Finland, Estonia and the Netherlands lead K-12 integration; the UK invested **£4M** in AI lesson-planning and marking tools; 🟢 **the OECD's 2026 Digital Education Outlook explicitly recommends moving from general-purpose AI to purpose-built educational AI** — which is this shelf's thesis stated by a standards body. 🔴 **Institutional readiness is the gap:** a claimed **10 %** of 450+ institutions have formal AI-use guidelines.

🟡 **Middle East and Africa, named explicitly rather than folded into "Europe":** regulation is nascent but moving — the UAE's **National AI Strategy 2031** and AI Ethics Guidelines, Saudi Arabia's **SDAIA** framework; **Kenya, South Africa and Nigeria are actively drafting AI policies.** 🔴 **No education-specific instrument was found for any MEA country this pass.** 🟢 **That is an informed gap, recorded as one.**

🟢 **Where the studio sells:** 🟢 **Annex III conformity work is the offer** — documentation, logging, human oversight, accuracy and robustness evidence. 🔵 The oversight component is the same one North America needs, so it is built once. 🔴 **Honest caveat to carry into any EMEA conversation: this shelf cannot currently date the obligation, and says so rather than quoting one of the three figures.**

### APAC

🟢 **This region has the clearest *education-specific* AI regulation anywhere, and it is not the EU.** 🟢 **Vietnam's high-risk AI list names education explicitly — automated assessment and behavioural monitoring (33/2026/QD-TTg, six sectors); its Law on Artificial Intelligence passed 2025-12-10 and took effect 2026-03-01.** 🟡 **South Korea's AI Basic Act took effect 2026-01-22** with its enforcement decree, but the regulator has signalled 2026 as a pilot year with a **one-year grace period on penalties**. 🟡 **Taiwan** passed an AI Basic Act in December 2025. 🔴 **China** enforces binding rules on algorithms, deep synthesis and generative AI. 🟢 **Singapore and Japan** rely on voluntary guidelines over existing law. 🟡 **Australia**'s AI Safety Institute was announced for early-2026 operation.

🟢 **Adoption:** China, India and Japan dominate regional spend, with China leading on government backing. 🟡 Named incumbents (vendor-sourced, indicative only): Google, Microsoft, IBM, Pearson, Byju's.

🟢 **Where the studio sells:** 🟢 **Vietnam and Korea are the two most tractable compliance engagements on this shelf** — Vietnam because the obligation is already in force and names assessment specifically, Korea because the grace period makes 2026 the year to build before penalties attach. 🔵 **Both want the same artefact as EMEA: an auditable human-in-the-loop assessment pipeline.** 🔴 **The gap, stated plainly: this pass found no APAC education-ministry policy, no national AI-in-schools curriculum, and no student-data rule specific to the region.** 🟢 **Ministry-direct research is the named next step, not an assumption that nothing exists.**

### LATAM

🟢 **The best-evidenced region in this pass, and the evidence is institutional rather than vendor.** 🟢 **UNESCO IESALC, 200 higher-education institutions across 19 countries: 87 % use AI in at least one area; only 26 % have any formal framework.** 🟢 **Teaching is the leading use at 74 %** (lesson planning, grading). 🟡 **Uptake is uneven by sector:** private non-profit **84 %**, public **68 %**, private for-profit **52 %**. 🟢 **School level:** TALIS 2024 put Brazil, Chile, Colombia and Costa Rica **above the OECD average of 36 %** for secondary-teacher AI use; **Ceibal (2026) reports 75 % of Uruguayan public-school teachers using these tools.**

🟡 **Regulation is general-purpose, not education-specific:** Brazil's **PL 2.338/2023** sits in the Chamber of Deputies and can still change; Chile's government bill is in its first constitutional stage; 🟢 **Colombia took a policy-first route with CONPES 4144 (February 2025)** — a budgeted, government-wide programme through 2030 rather than immediate horizontal obligations. 🟢 **UNESCO launched a regional Observatory on AI in Education for LAC on 14 April at ECLAC in Santiago**, and has run AI-regulation and ethics training for officials in Ecuador and Chile.

🟢 **Where the studio sells:** 🟢 **the 87 %-use / 26 %-framework gap is the offer, and it is a governance engagement before it is a build.** 🔵 **61 points of institutions are already using AI without a framework — that is remediation work with a deadline set by reputational risk rather than by statute.** 🟢 **The public/private split (68 % vs 84 %) says public institutions are the underserved segment.** 🟡 **Uruguay is the standout pilot market** at 75 % teacher adoption with Ceibal as a national counterparty.

🔴 **One honest caveat on the numbers:** the 200-institution UNESCO sample and the 29-institution Digital Education Council survey are **not comparable** and are not compared here.

### Global

🟢 **Cross-regional, and this is the finding that places the rest:** every one of the four regions above wants the **same** artefact — an auditable, human-in-the-loop assessment and feedback pipeline that a regulator or an accreditor can inspect. 🟢 **North America mandates the oversight, EMEA classifies it high-risk, Vietnam names assessment explicitly, LATAM has 61 points of ungoverned adoption to remediate.** 🟢 **So the oversight component is built once and sold four times, which is the strongest regional argument this file has recorded.**

🔴 **And the blocker is identical in all four: the LMS seam.** 🟢 **This pass measured it from the open-source side for the first time** — `DeepTutor` (Apache-2.0, 3 763 files) and `OpenTutor` (MIT, 890 files) hold **zero** LTI, xAPI, Caliper, SCORM or OneRoster paths between them. 🟢 **No region's engagement ships without that adapter, and no permissive component currently provides it.** 🔵 `ltijs` (Apache-2.0) remains the one-hop closer — see `compose/patterns.md`.

## 🟢 Seventy-second pass, 2026-10-09 — regional regulation re-measured on four channels; **the single most load-bearing compliance date on this shelf may have moved sixteen months**, and the market-size figure is **refused on a 5.5× spread**

⏱️ **Fourth pass of this date.** Pass 71 closed earlier today (commit `1fe734a`). **Append-only: this section is new; nothing below it was rewritten. The live `## Opportunities by region` block is the one in this section; pass 71's has been retitled *superseded* per this file's convention.**

### 🔴 Market size — **refused**, and the spread is the reason

🟢 Five published 2026 figures for AI-in-education, collected this pass:

| Source | 2026 figure | Horizon |
|---|---|---|
| Research and Markets | $10.6B | $42.48B by 2030 @ 41.5% |
| Precedence Research | $9.58B | ~$136.79B by 2035 |
| Future Data Stats | $7.50B | $25.70B by 2033 @ 19.2% |
| The Business Research Company *(higher-ed only)* | $4.09B | $13.46B by 2030 @ 34.7% |
| MarketReportsWorld | $1.94B | — |

🔴 **$1.94B to $10.6B is a 5.5× spread on the same year and the same nominal market.** 🟢 **A median of that is not a number, it is an average of incompatible definitions** — segment boundaries, whether hardware and services count, and whether "AI in education" includes AI-taught-as-a-subject all move it by multiples. 🔴 **Several are syndicated reports with undisclosed method.** 🟢 **Nothing on this shelf is sized, ranked or prioritised by any of them, and no single figure is adopted.** 🔵 Consistent with this shelf's refusal of third-party star counts for the same reason.

🟢 **What *is* usable, because it is a measured behaviour rather than a modelled market:** 🟢 **OECD TALIS secondary-teacher AI use — Brazil 56%, Chile 55%, Colombia 53%, Costa Rica 52%, against an OECD average of 36%.** 🔵 Survey, dated 2024, method published. 🟢 **Technavio's institution-wide AI implementation in higher education at 66%** is directionally useful but vendor-sourced.

## Opportunities by region — superseded (the live block is at the top of this file)

### North America

🟢 **The measurable fact is legislative volume, and it is high.** 🔴 **Two trackers disagree on the count — 134 bills across 31 states versus 68 across 27 — because they use different inclusion methods**, so this shelf records the spread rather than picking one. 🟢 **35+ states carry official AI guidance as of June 2026**; 🟢 **the federal Department of Education finalised its AI grant-priority rule on 2026-04-13.**

🟢 **The engagement-shaped signal is the mandate pattern, not the volume.** Four states require **both** state guidance **and** mandatory district-level policy adoption — **Idaho** (S.B. 1227: privacy, procurement, transparency, academic integrity, AI literacy), **Oklahoma** (S.B. 1734: every district, written policy before the 2027-28 school year), **Maryland** (AI Ready Schools Act: 24 districts, 120 days from state guidance), and **Virginia**. 🟢 **In higher education Florida is the clearest mover:** the Board of Governors has noticed intent to require universities to address faculty AI disclosure, student AI disclosure and permitted coursework use; separately all **28 Florida College System institutions** are to adopt AI-use policies covering **academic integrity and grading**.

🟢 **Opportunity:** policy-to-implementation is the gap. Hundreds of districts and 28 state colleges must produce, evidence and audit an AI-use policy on a deadline. 🟢 **`AI-Teaching-Agent`'s contract-declared `WAITING_REVIEW` gate is the artefact that turns a written policy into something demonstrable** (see `compose/patterns.md`, `P23`). 🔴 **Curriculum mandates are a second, separate line** — Alabama H.B. 329 requires a CS course including AI instruction for graduation, with Georgia and Mississippi adding AI-inclusive CS credits later this decade — and that is a content and teacher-training engagement, not a platform one. 🔴 **Student-data-for-training is the live constraint**: California A.B. 1159 would bar using student data to train models absent direct school benefit. 🔵 **Thin channel declared:** this pass found **nothing substantive on Canada or Mexico** education AI policy; the regional read is effectively US-only and is labelled as such rather than generalised.

### EMEA

🔴 **The most important finding of this pass sits here, and it is unverified.** 🟢 **Already in force and not in dispute:** EU AI Act **Article 4** (AI literacy) since **2025-02-02**, and **Article 5**, which **bans AI inferring emotions in education institutions** outside narrow medical and safety exceptions. 🔴 **That second one is a present-tense prohibition** — any engagement touching engagement-detection, attention-tracking or affect-aware tutoring is non-compliant **today**, not in 2027.

🔴 **The disputed date:** Annex III high-risk covers **admissions, grading and exam proctoring** — the education bucket. 🔴 **Secondary sources report the Digital Omnibus postpones these obligations from 2026-08-02 to 2027-12-02**, on a European Parliament vote of **2026-06-16**, with **Council adoption unconfirmed**. 🟢 **Other secondary sources still state August 2026.** 🔴 **This shelf cannot resolve it: `Gap 308` records a fifth consecutive refusal of every EU institutional host this session can reach.** 🟢 **Recorded as contested, with both dates named, because a sixteen-month swing in the high-risk date is the difference between a compliance scramble and a design runway — and a KB that silently picked one would be worse than useless.**

🟢 **Opportunity:** the sovereignty-plus-compliance posture this shelf has built toward. 🟢 **`ec-issuer`'s Open Badges 3.0 + European Learner Model + OID4VCI coverage is the natural credential spine for learner mobility** — 🔴 **blocked on `Gap 325`, its missing licence file, which is a question for counsel and not an engineering cost.** 🟢 **Policy demand signal:** the European Commission with the OECD, G7-endorsed, has proposed a draft **AI Literacy Framework** for primary and secondary education to align national approaches; a classroom pilot that began in **Italy, Portugal and Spain** has expanded to **Albania, Bulgaria, Czechia, France, Greece, Romania and Ukraine**. 🔵 That expansion is sponsored content and is flagged as such.

### APAC

🟢 **The region has the clearest statutory hook for education AI anywhere on this shelf.** 🟢 **South Korea's AI Basic Act took effect 2026-01-22**, applies **extraterritorially** to systems affecting Korean users, and names **education** among its "high-impact" sectors — requiring **meaningful human monitoring and intervention at any time.** 🔴 **That is a human-in-the-loop requirement written into statute**, which makes a demonstrable approval gate a procurement precondition rather than a nice-to-have.

🟢 **China holds the most binding rule set** — generative AI measures, algorithm registration, and **mandatory synthetic-content labelling since 2025-09** — and, with the UAE, is reported as one of only two countries running a **compulsory national AI curriculum**, from the 2025-26 school year. 🟢 **India moves fastest on curriculum:** AI and computational thinking become **mandatory from Class 3** across government and private schools in **2026-27**, backed by the IndiaAI Mission; IT Rules amendments covering AI-generated content took effect **2026-02-20**, and in **July 2026** the government signalled dedicated, risk-based AI legislation. 🟡 **Japan stays light-touch** — a 2025 framework law, an AI Strategic Headquarters chaired by the prime minister, voluntary and sectoral; 🔵 **no national school-level AI mandate was found, declared rather than assumed.**

🔴 **The cautionary case is Korea's, and it is the most useful thing in this subsection.** Seoul planned mandatory AI textbooks from 2025; **adoption sat below 30% by March**, and that **August the National Assembly stripped them of official status** after unions said the pace had outrun preparation. 🟢 **The lesson prices an engagement correctly:** teacher readiness, not model quality, is the binding constraint, and a rollout that skips it gets reversed. 🟢 **Opportunity:** Korea-compliant human-oversight architecture (the AI Basic Act's intervention requirement, served by a `WAITING_REVIEW` gate) plus the teacher-enablement track the Korean reversal proves is mandatory.

### LATAM

🟢 **This is the region where measured behaviour is strongest and institutional readiness weakest — and the gap is the business.** 🟢 **OECD TALIS: 56% of secondary teachers in Brazil, 55% in Chile, 53% in Colombia and 52% in Costa Rica used AI in the prior year, against an OECD average of 36%.** 🔴 **Teachers are ahead of their institutions by roughly twenty points.** 🟢 **UNESCO records institutional frameworks not keeping pace with adoption**, and 🔴 **CENIA finds 13 of 19 LAC countries studied do not teach early AI in schools at all.**

🟢 **Regulation, by country:** 🟡 **Brazil** — principles-based federal bill (operator duty to give clear, accessible information on exercising user rights; collective claims permitted), plus **ENIA** national strategy since 2022. 🟡 **Mexico** — a bill with a digital-rights chapter including a right to interact through AI systems; otherwise sectoral. 🟡 **Colombia** — **CONPES 4144** (adopted 2025-02), a government-wide programme with budget through 2030 and **no horizontal obligations**; 🟢 **sectoral regulators and public buyers read it as procurement template anyway**, which is what makes it commercially real. 🟢 **Chile** — risk-classified uses with supervision tied to a **data protection authority still being set up**; **ranked first in LATAM on the ILIA 2025 AI maturity index.** 🔴 **No dedicated 2026 education-specific AI regulation was found in any of the four** — declared as a gap, not read as permission.

🔴 **The constraint that actually binds a grading agent here:** 🟢 **Chile and Mexico both recognise limits on decisions made solely by automated processing**, prohibiting it where it produces unwanted legal effects or significantly affects rights — and a published grade is exactly that. 🟢 **So the human-approval gate is a legal requirement in LATAM too, arrived at from data-protection law rather than AI law.** 🟢 **Opportunity:** this converges with North America's policy-evidence need, EMEA's Article-5-era caution and Korea's statutory intervention duty — 🟢 **one architecture, four regulatory rationales**, which is the strongest cross-regional case this shelf has assembled. 🔵 Data protection remains the region's most mature layer and the right place to anchor a compliance story.

## 🟢 Seventy-first pass, 2026-10-09 — the regulatory picture resolves into **one rule that binds today** (EU Article 4) and **one jurisdiction that names education as high-risk in a binding instrument** (Vietnam); `Gap 308` refused by a **fourth** probe

⏱️ **Third pass of this date.** Pass 70 closed earlier today (commit `cf5c9bf`). **Append-only: this section is new; nothing below it was rewritten.**

### 🔴 `Gap 308` — OPEN. **Fourth consecutive refusal**, and the diagnosis is now stable

| Egress path | Host | Result this pass |
|---|---|---|
| Bash via agent proxy | `eur-lex.europa.eu` | 🔴 **HTTP `000`** |
| Bash via agent proxy | `digital-strategy.ec.europa.eu` | 🔴 **HTTP `000`** |
| Bash via agent proxy | `artificialintelligenceact.eu` | 🔴 **HTTP `000`** |
| control | `api.github.com` | 🟢 `200` |
| control | `raw.githubusercontent.com` | 🟢 `301` |

🟢 **The allowlist excludes EU institutional hosts generally; the controls answer normally.** 🔴 **Every EU AI Act date on this shelf therefore still rests on secondary channels only.** 🟢 **Remedy unchanged and still the cheapest high-value item in the registry: one fetch of `eur-lex.europa.eu/eli/reg/2026/1744/oj/eng` from any session with egress to that host.**

### 🟢 The regulatory frame, re-stated so the **live** obligation is not buried under the deferred ones

🔴 **The deferrals get quoted; the thing that binds today does not.** 🟢 **Stated first, therefore:**

| Obligation | Status | Who it binds |
|---|---|---|
| 🟢 **EU AI Act Article 4 — AI literacy** | 🔴 **IN FORCE since `2025-02-02`. No deferral.** | 🔴 **School and university *deployers*, now** |
| EU AI Office + national authorities | 🟢 Enforcing from `2026-08-02` | — |
| High-risk **Annex III** (incl. education) | 🟡 Deferred to **`2027-12-02`** by Reg. (EU) **2026/1744** | Providers / deployers of high-risk systems |
| High-risk **Annex I** | 🟡 Deferred to **`2028-08-02`** | — |
| AI omnibus amendments | 🟡 Adopted June 2026; Council final approval **`2026-06-29`**; reported entry into force **`2026-07-27`** | — |

🟡 **One conflation to keep flagged:** channels blur *entry into force* with *deferred application*. 🔴 **They are different things**, and with `Gap 308` unresolved this shelf cannot settle it from primary text. 🟢 **Five independent secondary channels agree on the two deferral dates; none is primary.**

🟢 **The commercially useful consequence, and it is the opposite of what "deferred to 2027" sounds like:** 🔴 **an EMEA education engagement has a live compliance obligation in 2026** (Article 4 literacy, binding on the institution as deployer) **and a two-year runway on the high-risk conformity work.** 🟢 **Sell the literacy and governance layer now; design the assessment layer to Annex III and ship it before `2027-12-02`.** 🟡 `Gap 310` rides unchanged: whether routine learner progress-tracking is *profiling* and so high-risk with no Article 6(3) filter — 🟢 **design as if it is.**

### 🟢 Market size — recorded with its disagreement intact

| Figure | Source class | Note |
|---|---|---|
| **$10.6B (2026) → $42.48B (2030), CAGR ~41.5%** | Commercial research house | 🟢 The figure this shelf has carried for several passes; consistent across cycles |
| $12.3B (2026) | Secondary, attributed to an analyst firm | 🔴 **Conflicts with the above by ~16%** |
| Europe ≈ **$2.64B (2026)** | Statistics aggregator | 🟡 **Indicative only** |
| APAC AI market ≈ **$102B (Mar 2026)** | Vendor report | 🔴 **Economy-wide, not education. Do not use in an education deck** |

🔴 **Two independent 2026 estimates differ by 16% and neither publishes its methodology at the point of citation.** 🟢 **Quote the range, never a point estimate, and attribute it.**

## Opportunities by region — superseded (the live block is at the top of this file)

### North America

🟢 **The regulatory shape is 50-state, and it has converged on two themes that are both buyable:** **student-data protection** and **mandatory human oversight**.

🟢 **Measured regulatory surface:** **134 AI-in-education bills across 31 states** in the 2026 session. California **AB 1159** would bar using student data to train AI models. Idaho **SB 1227** requires privacy protections and directs the state education department to build a generative-AI framework covering procurement safeguards and academic integrity, with aligned district policies. **Oklahoma** and **Maryland** require human oversight and bar AI from high-stakes decisions about students. **Ohio** and **Tennessee** push policy down to districts — 🔴 **Ohio's district deadline was `2026-07-01`; Oklahoma's falls before the 2027-28 school year.** **35+ states** now publish education-department AI guidance. New York City's guidance uses a traffic-light system whose 🔴 **red tier bars AI from grading, discipline and placement decisions.** Federally, the **K-12 AI Literacy and Readiness Act of 2026 (H.R. 8747)** advanced out of committee — 🔴 **not enacted.**

🟢 **The opportunity, named concretely:** 🔴 **a district under Ohio's or Oklahoma's mandate must produce an AI policy and evidence of human oversight — and the permissive stack can now demonstrate that oversight in code**, not in a Word document. `P14-R` wires `AI-Teaching-Agent`'s review gate (MIT) ahead of any grade write, which is precisely the NYC red-tier and Oklahoma/Maryland requirement. 🟢 **Sell policy-to-implementation, with the gate as the artefact.**

🔵 **Competitive field:** Google (ISTE+ASCD partnership targeting AI literacy for ~6M US teachers and faculty), Microsoft, OpenAI (**ChatGPT for Teachers**, free to verified educators from Nov 2025), Anthropic (free teacher offering from Jul 2026), Amazon, IBM; **60+ companies** under the White House AI education pledge; MagicSchool, SchoolAI, Buddy among startups; Pearson (Salesforce partnership, May 2026), McGraw Hill, Carnegie Learning; the **AFT's National Academy for AI Instruction**, a **$23M** partnership with three AI companies. 🔴 **Counter-signal worth pricing in:** Berkeley Law bans AI for all exams and credited coursework, and UChicago Law removes electronic devices from core 1L classes from fall 2026 — 🟢 **elite-institution restriction is a real segment, and "AI-free assessment integrity" is a sellable brief too.**

🔴 **Declared gap:** searches returned **essentially nothing on Canada or Mexico** — no federal or provincial education-AI instrument, no adoption data. 🟢 **This is a gap in the shelf, not evidence of inactivity**, and it should not be read as coverage.

### EMEA

🟢 **The binding instrument is the EU AI Act, and education sits in Annex III when a system affects access, progression or assessment.** 🟢 **The live obligation is Article 4 (above).** 🔴 **Obligations reach non-EU providers whose outputs affect EU-located students** — so a LATAM- or APAC-built tutor sold into the EU is in scope.

🟢 **National signals:** **Finland, Estonia and the Netherlands** are reported as leading K-12 AI integration. The **UK** invested **£4M** in AI tools for lesson planning and homework marking. **Germany** has a **€20bn** AI commitment (2025-2030) — 🟡 **economy-wide, not education.** In the **Gulf**, the **UAE** and **Saudi Arabia** run national AI strategies with heavy infrastructure spend. 🟢 **UNESCO** has issued generative-AI-in-education guidance; the **OECD 2026 Digital Education Outlook** recommends moving beyond general-purpose tools toward **purpose-built educational AI**.

🔴 **The quantified governance gap, and it is the opportunity:** across **450+ institutions** surveyed, only **~10% have established formal AI-use guidelines.** 🟢 **Combined with a live Article 4 duty, that is a compliance-led sale with a deadline that has already passed** — the institution is non-compliant today, not in 2027.

🟢 **Technical fit is unusually good here:** [`open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) (BSD-3) ships **Arabic, French and English** and an **Ollama** provider, so a Gulf or Francophone deployment can run **sovereign inference with no data egress** — see `P24` in `compose/patterns.md`. 🟢 For an AWS-region engagement, OATutor's **Bedrock** provider (`Gap 321`) is the in-region path.

🔴 **Declared gap:** no **primary-source** EMEA education adoption data was obtainable — the one regional market figure is an aggregator's, and `Gap 308` blocks the EU legal text itself.

### APAC

🟢 **APAC holds the single most education-specific binding instrument found anywhere this pass.**

🟢 **Vietnam — Law on Artificial Intelligence (Law No. 134/2025/QH15)**, passed `2025-12-10`, effective `2026-03-01`. 🔴 **An accompanying decision identifying high-risk AI systems names education among six sectors, explicitly including automated assessment and behavioural monitoring.** 🟡 One channel names a different instrument (*Digital Technology Industry Law*), so **the exact title needs primary confirmation.** 🟢 **South Korea — AI Basic Act** in force `2026-01-22` with its enforcement decree; **foreign providers above revenue or user thresholds must appoint a domestic representative**; 🟢 MSIT signals 2026 as effectively a pilot year with a **one-year grace period on penalties**. **Taiwan** passed an AI Basic Act in Dec 2025. **China** enforces binding rules on algorithms, deep synthesis and generative AI. **Singapore** and **Japan** rely on voluntary guidelines backed by existing law. **Australia** established an **AI Safety Institute** (Nov 2025) and released a **National AI Plan** (Dec 2025). **ASEAN** maintains a voluntary **AI Governance Guide** (updated 2026).

🟢 **The opportunity:** 🔴 **a vendor selling an assessment tool into Vietnam is building a declared high-risk system, and into Korea may need a domestic representative.** 🟢 **Neither is a blocker; both are billable compliance scope**, and the Korean grace period makes 2026 the right year to enter rather than the wrong one. 🟢 **Technical fit:** [`biswal-prem-5677/Autonomous-Exam-Proctoring-Grading-Agent`](https://github.com/biswal-prem-5677/Autonomous-Exam-Proctoring-Grading-Agent) (MIT) runs **with no external AI APIs**, which is the cleanest answer to a behavioural-monitoring rule — 🟡 **though note that under Vietnam's decision, proctoring is the *named* high-risk use, so local execution reduces data-transfer exposure without removing the high-risk classification.**

🔵 **Three of the eight new agents censused this pass are APAC-origin** — `zijinz456/OpenTutor`, `littlecookie0722/AI-Teaching-Agent`, `Li-Evan/Bloom` (the last two bilingual zh/en). 🟢 **The region is producing permissive education agents, not only consuming platforms.** 🔵 Named incumbents in secondary reports: Google, Microsoft, IBM, Pearson, Byju's.

🔴 **Declared gaps:** **no APAC-wide education AI rulebook exists**; no education-specific regulator was named in any channel; and **no school-level adoption metrics** were obtainable for the region.

### LATAM

🟢 **LATAM has the best adoption evidence of any region on this shelf, and it says adoption is broad and shallow.**

🟢 **The Digital Education Council's *AI in Higher Education LATAM Survey 2026*** — **30 000+ respondents across 29 institutions**, delivered with the **Institute for the Future of Education** and **Tecnológico de Monterrey**, with outreach via **AIGEN** and **RIE360**:

| Measure | Value |
|---|---|
| Student AI use | 🟢 **92%** (up from 86% in the 2024 global student survey) |
| Faculty AI use | 🟢 **79%** |
| 🔴 Faculty reporting only **minimal-to-moderate** engagement | 🔴 **88%** |
| Faculty concerned about student over-reliance | **76%** (**63%** strongly) |

🔴 **So 79% faculty adoption is not 79% faculty capability** — 88% of those users are at the surface. 🟢 **UNESCO** separately flags that many higher-education institutions across Latin America and the Caribbean **lack policies governing generative AI use**.

🟢 **The opportunity, and it is a different sale from EMEA's:** 🔴 **there is no binding regional regulation forcing the purchase** — so the wedge is not compliance, it is **faculty enablement plus institutional policy**, against a measured 88% shallow-usage figure and a 76% concern figure that gives the brief its urgency. 🟢 **The buyer is the provost, not the compliance officer.** 🔵 The **Latin American Index of AI (ILIA)**, third edition, ranks countries as **Pioneers / Adopters / Explorers** across enabling factors, research-and-adoption and governance — 🟢 **usable as the regional maturity frame in a pitch.**

🔴 **Declared gaps, stated explicitly because silence would read as coverage:** 🔴 **no country-level binding education-AI regulation was found for Mexico, Colombia or Argentina.** 🔴 **Brazil and Chile are reported as "advancing" by a single vendor blog whose own figures are incomplete — not corroborated, and not usable.** 🔴 **No LATAM edtech vendor with a named 2026 AI programme was identified**, and no ministry-level programme behind the adoption figures was found. 🟢 **The adoption data is strong; the regulatory and vendor map is empty, and that emptiness is this shelf's, not the region's.**

## 🟢 Seventieth pass, 2026-10-09 — the AI Act deferral reaches a **fifth** independent channel and is refused by a **third** egress path; and the pass's commercial finding re-maps the market into **three** licence tiers, which moves where a permissive build has least competition

⏱️ **Second pass of this date.** Pass 69 closed earlier today (commit `abf91da`, 00:07 UTC). **Append-only: this section is new; nothing below it was rewritten. The live `## Opportunities by region` block is the one in this section; pass 69's has been retitled *superseded* per this file's convention.**

### 🟡 The AI Act dates — a fifth agreeing channel, a third refused path, and one new date conflict

🟢 **The correction itself is unchanged:** Regulation (EU) **2026/1744** (Digital Omnibus on AI) deferred the **Annex III high-risk** regime from `2026-08-02` to **`2027-12-02`**, and **Annex I** (high-risk embedded in regulated products) to **`2028-08-02`**.

🆕 **A fifth independent secondary channel agrees, and adds the procedural step the prior four omitted:** the **Council gave final approval on `2026-06-29`**, and the revised dates are *"2 December 2027 for stand-alone high-risk systems and 2 August 2028 for systems embedded in regulated products."* 🟢 **Five channels, no disagreement on either date.**

🆕 **Two further dates, new to this shelf:**
- 🟢 **Article 4 (AI literacy) was *not* changed and has applied since `2025-02-02`.** 🔴 **It is live now, it binds deployers including schools and universities, and it is the one AI Act obligation in education with no deferral between it and a client.**
- 🟢 **The AI Office and national authorities began enforcing from `2026-08-02`.**

🔴 **And a new conflict, recorded rather than resolved:** the Commission's own policy page is reported to list the Omnibus as **entering into force `2026-07-27`**, while another guide had it still awaiting Official Journal publication as of a July update. 🟡 **Entry into force and the deferred application dates are different things and the channels blur them** — 🔴 **unverifiable here, folded into `Gap 308`.**

🔴 **A third independent egress path was tried and refused — the gap is not closing for want of trying:**

| Egress path | Host | Result |
|---|---|---|
| Bash via agent proxy | `eur-lex.europa.eu` | 🔴 DNS **FAIL**, HTTP `000` |
| 🆕 Bash via agent proxy | `digital-strategy.ec.europa.eu` | 🔴 **DNS FAIL**, HTTP `000` — **new host tried this pass** |
| Bash via agent proxy | `artificialintelligenceact.eu` | 🔴 DNS **FAIL**, HTTP `000` |
| control | `api.github.com`, `raw.githubusercontent.com` | 🟢 resolve and serve `200` |

🟢 **So the block is EU-host-wide, not `eur-lex`-specific** — pass 69 had two paths to one host family and this pass adds a second host. 🔴 **`Gap 308` stays open with the same cheapest remedy: one fetch of `eur-lex.europa.eu/eli/reg/2026/1744/oj/eng` from any session with egress to that host.**

🟢 **What is live and commercially dated regardless:** **Article 50** was untouched by the Omnibus and its marking grace expires **`2026-12-02`** — 🔴 **eight weeks out.** 🔵 Education uses named high-risk under Annex III — **admissions screening, assessment, proctoring** — are the ones that move to `2027-12-02`; 🔴 **facial recognition and behaviour analysis in remote proctoring are flagged by multiple channels as the sharpest exposure.** 🟡 **Whether routine learner progress-tracking counts as *profiling*, and is therefore high-risk with no Article 6(3) filter, remains unread (`Gap 310`). 🟢 Design as if it does.**

### 🆕 The pass's commercial finding: **three licence tiers, not two** — and the open seam moved

🔵 **Pass 69's map was two-tiered:** closed vendors hold the capability, open source does not have it. 🟢 **Pass 70 measured a third tier and the map is now:**

| Tier | Who | LTI 1.3 + AGS? | Usable in a closed client deliverable? |
|---|---|---|---|
| 🔴 **Closed commercial** | EduGears AI, LearnWise, ibl.ai, campusmind.ai, Asyntai, edusageai | 🟢 **yes — sold, with a teacher-approval gate** | 🔴 licence//buy, not build |
| 🆕 🟡 **AGPL** | `HugeCatLab/ChatTutor`, `24kchengYe/human-skill-tree` | 🔴 no | 🔴 **no** — network copyleft (🟡 except `human-skill-tree`'s `skills/`, dual MIT) |
| 🟢 **Permissive** | OATutor (MIT), DeepTutor (Apache-2.0), Open TutorAI CE (BSD-3), `lti-ai-grader` (Apache-2.0) | 🔴 **no — 2 of 2 with an LTI layer are on 1.1** | 🟢 **yes** |

🟢 **Why this is the commercially useful version of the finding.** 🔴 **The gap is no longer "no open education agents exist"** — three permissive and two AGPL were read from payload in a single pass. 🟢 **The gap is one protocol hop wide:** every permissive component stops at **LTI 1.1 + `replaceResult`**, and the capability six vendors monetise is **LTI 1.3 + AGS behind a human-approval gate**. 🔵 **That is the narrowest, best-evidenced build opportunity in this KB**, and `P12` is pointed exactly at it.

🟢 **And the permissive tier is better stocked than pass 69 could see:** OATutor brings **Bayesian Knowledge Tracing in-tree** — mastery estimation that `lti-ai-grader` does not have — 🔵 so the port can now start from a component that already models the learner.

## Opportunities by region — superseded (the live block is at the top of this file)

### North America

🟢 **Market:** the largest regional market — reported at **36% share, ≈$3.68B in 2026, rising toward $32B by 2030**. 🟡 Vendor-research figures; direction is firmer than the level.

🔴 **The regulatory surface is state-level and it is now a compliance market in its own right:** **134 AI-in-education bills across 31 states** in 2026; **more than 30 states** have AI guidance documents. 🆕 **Ohio is the first state to require every K-12 district to adopt a formal AI use policy, by `2026-07-01`.** 🔵 Federal: the **K-12 AI Literacy and Readiness Act of 2026 (H.R. 8747)** advanced in committee in July 2026.

🔴 **The constraints that shape a build:** **California AB 1159** would bar using student data to train AI models unless it directly benefits the school; **Idaho SB 1227** requires privacy protections for AI tools in schools; **Oklahoma and Maryland** require human oversight and **ban AI from high-stakes decisions about students**. 🟡 District-level divergence is real: **NYC** has a one-year moratorium on student-facing AI through grade 8; **Katy ISD (TX)** bans generative chatbots for K-6.

🟢 **The opportunity, stated as work Globant can sell:** 🔴 *"human oversight required, no AI high-stakes decisions"* is **the teacher-approval gate `P12` already specifies** — in Oklahoma and Maryland it is law, not a preference. 🟢 **Build the approval gate as the product, not as a feature:** an LTI 1.3 + AGS grading surface whose grade return is **structurally impossible without a recorded human approval** is directly saleable into these states. 🟢 **Second line: district AI-policy compliance tooling** — Ohio's mandate creates ~600 districts needing a policy and an evidence trail on a hard date. 🔵 **OATutor is the natural permissive base here** — MIT, and from UC Berkeley, which is a credible provenance in US higher ed.

🟡 **Incumbent to design around:** **Google Gemini for Education** deployed across **1 000+ US colleges and universities** (August 2025) — 🟢 **assume the LLM layer is already chosen and sell the LMS seam, the approval gate and the audit trail.**

### EMEA

🆕 **The strongest single datum this pass, and it is a demand signal pointing straight at purpose-built tooling:** the **Sanoma Learning 2026 European Teacher Survey** — **20 000+ teachers, 14 countries** — reports **63% teacher AI use**, up from **49%** intent in the 2023–2025 surveys, with confidence in generative tools up **28% → 42%**. 🔴 **But only 16% think general-purpose AI improves learning outcomes**, **three in four** are concerned about risks to education quality, and **only one in three** support students using it at school — 🔴 **a figure flat since 2023.**

🟢 **Read that as a market structure, not a mood:** **adoption is high and trust in general-purpose tools is low and not improving.** 🔵 **The survey's own framing — teachers *"want tools built for education"* — is the EMEA thesis in one line.** 🟢 **A purpose-built, LMS-integrated, human-gated tool is not a nice-to-have in EMEA; it is the stated gap.**

🔴 **Regulatory:** the AI Act is the binding frame; **admissions screening, assessment and proctoring are Annex III high-risk**; enforcement began **`2026-08-02`**; the high-risk application dates deferred to **`2027-12-02`** / **`2028-08-02`**. 🔴 **Article 4 AI-literacy binds now** (since `2025-02-02`) and 🔴 **Article 50 marking binds `2026-12-02`**. 🟡 The Council of Europe's education ministers note **GDPR applies to AI-processed learner data** and that few non-binding frameworks address **psychological harm**.

🟢 **The opportunity:** 🔴 **the deferral is a sales window, not a reprieve** — an institution procuring in 2026 will run that system into the 2027 regime. 🟢 **Sell AI Act readiness as the differentiator against the six closed vendors:** Article 50 structural marking (this KB's `aiact-50-2-{marking,pack}`, **23/23** and **27/27**), a declared signature seam (`MarkLLM`), Article 4 literacy evidence, and a documented Annex III posture. 🔵 **`Open TutorAI CE` (BSD-3, R2D-dev) and `lti-ai-grader` (Apache-2.0, UPV Spain) are both EMEA-provenanced permissive bases** — useful in public procurement where local provenance scores.

### APAC

🟢 **Market:** Grand View reports **US$2 282.9M in 2025** rising to a projected **US$18 214.1M by 2033**, **CAGR 28.1% (2026–2033)**. 🟡 Vendor forecast.

🔴 **APAC is the region where education is named in binding AI law, which is the opposite of the "guidance only" picture elsewhere:**
- 🆕 **South Korea — the `Basic Act on the Development of AI and the Establishment of Trust` (AI Basic Act) takes effect January 2026**, and its *"high-impact AI"* category **explicitly includes education**. 🔴 **This is the single hardest education-AI compliance surface measured anywhere this pass.**
- 🆕 **Vietnam — `Law No. 134/2025/QH15` on Artificial Intelligence, effective `2026-03-01`.**
- 🔵 **China:** algorithm filings, **synthetic-content labelling**, security review for public models — already enforced. **Japan:** light-touch, voluntary. **Singapore:** frameworks and toolkits (**AI Verify**). **Indonesia:** sectoral soft framework, **education named a priority sector**.
- 🔴 **Readiness is uneven:** UNESCO notes China and Singapore have AI-in-education policies while other countries are *"still struggling to meet basic educational needs."* 🔴 Brookings: Laos, Myanmar, Brunei, Cambodia and Timor-Leste have less developed frameworks.

🟡 **A sentiment split worth pricing:** the **Ipsos Education Monitor 2026** finds **lower** support for banning AI in schools across the Asian markets examined, but **Australia and New Zealand record higher support for banning** — 🟢 **so ANZ should be sold as a conservative, consent-first market and not bundled with the rest of APAC.**

🟢 **The opportunity:** 🟢 **Korea's "high-impact" classification is a compliance engagement with a date on it** — conformity documentation, human oversight, risk management for education deployers, saleable now. 🟢 **China's synthetic-content labelling rhyme with EU Article 50 means one marking implementation can serve both** — 🔵 this KB's `aiact-50-2-pack` is the reusable asset. 🟢 **`HKUDS/DeepTutor` (Apache-2.0, HKU) is the APAC-provenanced permissive base.** 🔴 **For the low-readiness ASEAN markets, lead with Kolibri-style offline-first delivery, not agents** — infrastructure precedes intelligence.

### LATAM

🟢 **Adoption is the highest measured anywhere and governance the thinnest — and both numbers are now from named, primary-ish studies:**
- 🆕 **UNESCO IESALC** — **200 higher-education institutions, 19 countries**: **87% use AI in at least one area**, while *"governance frameworks and institutional strategies are struggling to keep pace."*
- 🆕 **Digital Education Council LATAM survey** — **30 000+ responses, 29 institutions**, with the Institute for the Future of Education and **Tecnológico de Monterrey**: **79% of faculty use AI in teaching**, but **88% report "minimal" to "moderate" engagement**. 🔴 **The lowest adoption is in assessment — cheating detection and feedback generation.**

🟢 **That last line is the commercial centre of gravity for LATAM, and it matches `P12` exactly.** 🔴 **Assessment is simultaneously the least-adopted use case and the one faculty engage with most shallowly** — 🟢 **and assessment feedback with a human gate is precisely what the permissive tier cannot yet do over LTI 1.3.**

🔵 **Institutional landscape:** UNESCO launched the **Observatory on AI in Education for Latin America and the Caribbean** on **`2026-04-14` at ECLAC, Santiago**, with **CAF, CENIA (Chile), CETIC.br, ECLAC, Fundación Santillana, Tecnológico de Monterrey, ProFuturo, Universidad del Desarrollo, Fundación Ceibal (Uruguay)** and **IRCAI**. 🔵 **Digital Learning Week 2026 (`09-08`–`09-11`):** 25+ education ministers adopted a joint statement on education as a human right in the age of AI.

🔴 **Regulation is general-purpose, not education-specific:** **Uruguay** was the first LATAM country to sign the Council of Europe **Framework Convention on AI** (2025); **Peru** has a risk-classified framework; **Colombia** adopted national AI policy via **CONPES 4144** (February 2025); **Mexico**'s federal bill is still at Senate stage, converging on an unacceptable/high/lower-risk taxonomy.

🟢 **The opportunity:** 🟢 **sell institutional AI governance together with the build** — 87% adoption against *"governance struggling to keep pace"* means the policy artefact is a billable deliverable, not overhead, and the UNESCO Observatory's partner list is the credibility channel. 🟢 **Then take the assessment gap:** a permissive, human-gated feedback-and-grading surface, Spanish- and Portuguese-first. 🔵 **`lti-ai-grader` already ships multi-language HTML templates**, which lowers that cost. 🟢 **Tecnológico de Monterrey appears in both the Observatory and the DEC survey — it is the single highest-leverage LATAM reference account in this file.**

## 🟢 Sixty-ninth pass, 2026-10-09 — the AI Act correction **holds at four channels and stays unverifiable**, now refused by **two independent egress paths**; and the pass's commercial finding is a **market structure**: the education agent layer is populated and **closed**, which is where a permissive build has least competition

⏱️ **First pass of this date (pass 68 closed 2026-10-08; the date rolled over during this pass's measurements, which are dated by their publication here). Append-only: this section is new; nothing below it was rewritten. The live `## Opportunities by region` block is the one in this section; pass 68's has been retitled *superseded* per this file's convention.**

### 🔴 The AI Act dates, re-stated with their channel count — because that is the only honest way to state them

🟢 **Pass 68's correction stands unchanged:** Regulation (EU) **2026/1744** (Digital Omnibus on AI) deferred the **Annex III high-risk regime** from `2026-08-02` to **`2027-12-02`**, and Annex I to **`2028-08-02`**. 🟡 **It rests on four independent secondary channels in agreement**, including two law-firm client notes, a research note and a EUR-Lex record title returned by search.

🔴 **It is still unverified against primary text, and this pass tried harder and failed more precisely:**

| Egress path | Result |
|---|---|
| Bash via agent proxy → `eur-lex.europa.eu` | 🔴 **`CONNECT tunnel failed, response 403`**; `getent hosts` also fails |
| `WebFetch` → the same URL | 🔴 **`getaddrinfo ENOTFOUND eur-lex.europa.eu`** |
| control: `api.github.com` from the same shell | 🟢 resolves, serves `200` |

🔵 **Two independent instruments now agree, and the proxy's own answer identifies an allowlist denial rather than a DNS fault** — pass 68 had one path and called it `DNS_BLOCKED`. 🔴 **`artificialintelligenceact.eu` also fails to resolve.** 🟢 **`Gap 308` stays open with the cheapest high-value remedy in the registry: one fetch of `eur-lex.europa.eu/eli/reg/2026/1744/oj/eng` from any session with egress to that host.**

🔴 **What is live, and the date that actually matters commercially:** **Article 50** was left untouched by the Omnibus, and its marking grace expires **`2026-12-02`** — 🔴 **eight weeks out.** 🟢 **`P11` is the shelf's only dated recipe, and `Gap 313` closed this pass by measuring exactly how far the shelf is from that obligation** (0 of 3 third-party components mark content; the shelf's own marking is structurally green at 23/23 + 27/27 with its **signature seam declared and empty**).

🟡 **Single-channel and still not built on:** public-authority high-risk deferral to `2030-08-02`; sandbox obligation to `2027-08-02`. 🔴 **Whether routine learner progress-tracking counts as *profiling* — and therefore always high-risk, with no Article 6(3) filter — remains unread (`Gap 310`) and rides with `Gap 308`.** 🟢 **Design as if it does.**

### 🆕 The pass's commercial finding: the agent layer is **not empty, it is captured**

🔴 **Twenty consecutive weeks of the control query (`top open source AI agents education {year} github MIT`) have returned zero education components** — every "education" row is a repository that teaches AI to developers.

🟢 **A targeted query returned a populated field on the first attempt, and it is almost entirely commercial:** **EduGears AI** (Moodle/Canvas/Blackboard/Brightspace over **LTI 1.3**, AI grading posted via **AGS** behind a teacher-approval gate), **LearnWise**, **ibl.ai** (*"Tutoring Agent"*, *"Faculty Agent"*; Canvas, Blackboard, Brightspace, Moodle, Sakai), **campusmind.ai**, **Asyntai**, **edusageai**. 🔴 **Several sell precisely the capability the permissive tier lacks.**

🟢 **The permissive exceptions are narrow:** Moodle-only plugins (**MooChat Block**, **MAICI**, **Teaching Assistant Block**), 🟡 several OpenAI-only for model support — and **one** real cross-LMS find, [`moocupv/lti-ai-grader`](https://github.com/moocupv/lti-ai-grader) (Apache-2.0, **EMEA/UPV Valencia**), 🔴 **on LTI 1.1 / Basic Outcomes rather than 1.3 / AGS**.

🔵 **Read commercially, this is the most useful thing the pass found.** 🟢 **The open tier's weakness is a map of where a Globant build has least competition and most leverage: a permissive, LTI 1.3 + AGS, human-in-the-loop grading and tutoring surface does not exist in open source, and six vendors are monetising its absence.** 🔴 **Unmeasured: how many such vendors, how funded, whether any publishes a permissive core — `Gap 317`.**

### 🟡 Market size — four channels, four incompatible numbers, recorded as a range and never as a figure

| Channel | Claim |
|---|---|
| The Business Research Company | **$7.52B (2025) → $10.6B (2026)**, CAGR **40.9%** |
| IMARC-derived | **$6.4B (2025) → $79.6B (2034)** |
| a third analysis | **~28%/yr, 2026–2036**, arguing institutional purchasing lags consumer adoption |
| AI-tutors sub-segment | **$1.63B (2024) → $7.99B (2030)** |

🔴 **A 2026 figure of $10.6B and a 2025 figure of $6.4B cannot both sit on a path to $79.6B by 2034 under one definition** — 🟢 **so the definitions differ, and no single number may be quoted as *the* market size.** 🟢 **Quote the range, the channel and the date, or quote nothing.** 🔵 **Segment structure is more durable than the totals:** K-12 is the largest adopter segment at **45.62%**, language learning the fastest-growing, cloud delivery **71.22%** share (2024). 🟡 **One analysis rates sector maturity 35/100 against competition 85/100** — 🔵 **pilots everywhere, incumbents everywhere, which is consistent with everything above.**

## Opportunities by region — superseded (the live block is at the top of this file)

### North America

🟢 **Measured:** the region holds **~36%** of global share and one channel sizes it **$951M (2024) → $2 303.2M (2029)**, CAGR **15.9%** — 🟡 **notably slower than the global CAGRs above, which is itself a finding: North America is the largest and most mature, not the fastest.**

🔴 **The governance vacuum is the opportunity.** Only **10%** of institutions have formal AI guidelines and **71%** of US teachers lack AI training. One channel describes education AI as operating in *"a relative regulatory vacuum"* with *"no equivalent to the FDA"*, where adoption is decided school-by-school or district-by-district. 🟡 **State-level fragmentation is asserted (Colorado, Texas named) and not verified here.**

🟢 **Money is moving and is nameable:** a **$169M** government commitment to responsible AI in higher education (Q1 2026); **Carnegie Mellon + Gates Foundation, $55M** into AI courseware for gateway college courses; **OpenAI's country-level education programme with eight national partners** (Q1 2026). 🟡 **Each single-channel and unconfirmed against an official source.**

🟢 **The engagement shape:** 🔵 institutions here can buy, have no policy, and face no binding sector regulation. 🟢 **Sell governance as the product, not as the compliance overhead** — an AI deliverable that ships with its own policy scaffold, audit trail and human-approval gate is differentiated in exactly the way the market is weak. 🟢 **`P11`'s marking machinery is reusable here as evidence-of-diligence even though Article 50 does not bind US deployments.**

### EMEA

🔴 **This is the region where the regulation is the engagement.** 🟢 The **EU AI Act** is the binding layer and reaches non-EU providers whose outputs affect EU-located students. 🔴 **Annex III high-risk is deferred to `2027-12-02` (four-channel, unverified — quote it with its channel count), while Article 50's marking grace expires `2026-12-02`.**

🟢 **Adoption is high and institutionally unsupported, and this pass has a non-vendor instrument for it.** The CESGA-led **"AI Act(ing)"** study across six European countries found **>90%** of Spanish respondents using AI in their work and **all** Belgian participants doing so — while **nearly half of Spanish respondents did not know whether their institution had AI guidelines**, and Spain, Belgium and Greece showed *"an urgent need for clearer organizational rules."* 🔵 **Data protection, bias, over-reliance and academic integrity recurred across all six countries.**

🟢 **Soft law to cite in a proposal:** **UNESCO**'s generative-AI guidance for education as the main international reference; **OECD AI Principles**, non-binding but referenced by most national education ministries; **Luxembourg/OPOCE (2026)** updated ethical-and-data-responsible-use guidelines, which themselves note the AI Act's implications for education. 🟡 **OECD's *"metacognitive laziness"* finding** — over-reliance diminishing deep learning — 🔵 **pushes assessment toward the learning *process* rather than the final product, which is an argument for xAPI/LRS evidence architecture and therefore for this shelf's own recipes.**

🟢 **The region also supplied two of this pass's repositories:** [`moocupv/lti-ai-grader`](https://github.com/moocupv/lti-ai-grader) (Apache-2.0, UPV Valencia) and [`FenixEdu/fenixedu-academic`](https://github.com/FenixEdu/fenixedu-academic) (LGPL-3.0, IST Lisbon). 🔵 **EMEA higher education builds and publishes its own systems** — a partnership surface, not only a sales one.

🟢 **The engagement shape:** 🟢 **lead with the `2026-12-02` Article 50 marking deadline, which is eight weeks out and binds generative deployments now**, and treat `2027-12-02` Annex III as the programme behind it. 🔴 **Present `P11` as a readiness programme, never as a compliance guarantee** (`Gap 313`, `P803`).

### APAC

🟡 **Sized at $591.6M (2024) → $1 848.1M (2029), CAGR 20.9%** by one channel, while another calls APAC **the fastest-growing region at 35.3% CAGR**. 🔴 **The two cannot both be right; both are recorded, neither is quoted alone.** 🟢 **Drivers named consistently: large student populations, rising disposable incomes, and acute teacher shortages addressed through automation** — 🔵 **the teacher-shortage driver is the one that favours agentic deliverables most directly.**

🔴 **Regulation is fragmented by design, and that is the planning fact.** Forrester describes *"a fragmented landscape for AI legislation, unlike the EU's unified approach"*: **Singapore** relies on mature guidelines, **China** on laws against algorithmic misconduct, **India** on existing criminal law. 🟡 **The ASEAN Guide on AI Governance and Ethics is early-stage**, so compliance must be tailored country by country. 🔴 **Governance is lagging implementation** (Diligent Institute).

🔴 **An informed gap, stated explicitly rather than left as silence: the channel named no education-sector players, vendors or ministries for this region.** 🔵 **Every APAC result returned was general enterprise AI or market sizing.** 🟢 **This is a real coverage hole in this KB, not evidence of an empty market** — remedy is a per-country query (China's and Singapore's education-ministry AI guidance; Southeast Asian tutoring vendors) rather than a regional one.

🟢 **The engagement shape:** 🔵 **multi-jurisdiction by default.** 🟢 Build the policy layer as configuration, not as code — one deliverable, per-country policy nodes — because the regulatory divergence here is permanent rather than transitional. 🟡 **APAC also owns the shelf's two LGPL-3.0 SIS options' centre of gravity (OpenEduCat, India), which makes the `P750` proprietary-addon shape regionally relevant.**

### LATAM

🟢 **The best-instrumented region in this pass, and the only one with a non-vendor institutional census.** **UNESCO IESALC**, across **200 institutions in 19 countries**: **87%** use AI in at least one area, 🔴 **but only ~26% have any formal framework.** By area: **teaching and learning 73.5%**, research **57.0%**, administration **34.1%**, community engagement **20.0%**. By institution type: private non-profit **84%** > public **68%** > private for-profit **52%**.

🟢 **Corroborated by a second, independent survey with a very large sample:** the **Digital Education Council** LATAM 2026 study (**>30 000 responses, >29 institutions**, incl. Tec de Monterrey, UNAM, UPC Peru, PUC Chile) — **92% of students** and **79% of faculty** actively engaging with AI. 🔴 **And the actionable asymmetry: 50% of students support AI-assisted feedback on assignments while only 19% of faculty currently use AI that way.**

🔵 **That 50/19 gap is the most directly sellable number in this file.** 🟢 **Demand exists, faculty capability is the bottleneck, and the bottleneck is addressable with exactly the component this pass found (a permissive AI grader with a human-approval gate) plus training.**

🔴 **Regulation: no regional framework.** **Chile** leads (National AI Policy since 2021, a law under discussion); **Brazil** and **Colombia** have advanced national strategies **without** education-specific regulation; **Mexico** has no binding rules — SEP, ANUIES and Observatorio IA recommendations *"lack binding force."* 🟡 **Only ~30% of LATAM universities have published AI-use policies.** 🟢 **The IDB's ILIA index tracks readiness, adoption and governance across 19 countries** and is the instrument to cite in a regional proposal.

🟢 **The engagement shape:** 🟢 **institutional policy plus faculty enablement, delivered together with the tooling** — the surveys say adoption is already won and governance is not. 🔵 **Cost sensitivity favours this shelf's recommended architecture** (copyleft SIS unmodified + permissive build beside it over LTI 1.3, evidence to `lrsql`), 🔵 **and the absence of binding sector regulation means an EMEA-grade governance layer can be offered here as differentiation rather than obligation.**

### 🟢 What is true in every region, and it is this pass's own measurement

🔴 **No permissive student system of record exists** — **six read from payload, six copyleft** (`Gap 309`). 🔴 **The one Apache-2.0 substrate, Ed-Fi DMS, has no OneRoster rostering and no change feed** (`docs/PRD-v8.1.md`), and 🔴 **adopting it is a data migration, not an in-place cutover** (**NFR-OPS-2**, `Gap 303` closed).

🟢 **So the same commercial boundary holds in North America, EMEA, APAC and LATAM:** 🟢 **everything Globant builds can be permissive; the student record it reads from will be copyleft, and LTI 1.3 plus xAPI keep that record at arm's length across a process boundary.** 🔴 **Never quote a closed fork of a GPL SIS, and never quote OneRoster as something this shelf supplies.**

## 🔴 Sixty-eighth pass, 2026-10-08 — **CORRECTION: the EU AI Act's education high-risk regime is NOT in enforcement.** Regulation (EU) 2026/1744 (the Digital Omnibus on AI) deferred it from `2026-08-02` to **`2027-12-02`** — a sixteen-month move that pass 67 reported the wrong side of. What *is* live is **Article 50**, whose marking grace expires **`2026-12-02`** — eight weeks from this pass

⏱️ **Twenty-second pass of this date. Append-only: this section is new; nothing below it was rewritten. The live `## Opportunities by region` block is the one in this section; pass 67's has been retitled *superseded* per this file's convention.**

### 🔴 The correction, stated before anything is built on it

🔵 **What pass 67 wrote:** *"the EU AI Act is **in enforcement** (since `2026-08-02`), education's
high-risk trigger is read **as a four-part test**."*

🟢 **The four-part test is correct and survives.** Annex III **point 3** covers: **(a)** determining
access, admission or assignment to education and vocational training institutions; **(b)**
evaluating learning outcomes; **(c)** assessing the appropriate level of education an individual will
receive; **(d)** monitoring prohibited behaviour of students during tests.

🔴 **The enforcement date is wrong, and it was wrong when it was written.**

| | Pass 67 recorded | 🆕 Measured this pass |
|---|---|---|
| **Annex III high-risk (incl. education, point 3)** | 🔴 *"in enforcement since `2026-08-02`"* | 🟢 **applies `2027-12-02`** — deferred **16 months** |
| **Annex I (AI embedded in regulated products)** | not recorded | 🟢 **`2028-08-02`** (from `2027-08-02`) |
| **Article 50 transparency** | not separated | 🟢 **applies since `2026-08-02` — did NOT move** |
| **Article 50(2) machine-readable marking**, systems already on market before `2026-08-02` | not recorded | 🔴 **grace expires `2026-12-02`** 🆕 |
| **Prohibited practices** | not recorded | 🟢 enforceable since **`2025-02-02`** |

🟢 **The instrument:** **Regulation (EU) 2026/1744** — *of 8 July 2026, amending Regulation (EU)
2024/1689* — published in the Official Journal **`2026-07-24`**, in force **`2026-07-27`**. 🔵 It
replaced the AI Act's proposed **standards-conditional trigger** for Annex III with **fixed calendar
dates**, which is why a date that once depended on harmonised standards is now simply a date.

🟡 **🆕 One substantive change beyond timing, and it cuts *against* education:** the Omnibus makes
**profiling always high-risk** — a profiling system does not get the Article 6(3) filter that would
otherwise let a narrow use case out. 🔴 **Ordinary learner progress-tracking is the obvious
question**, and no source read this pass settles whether it counts (`Gap 310`). 🟢 **For a
deliverable, assume the filter is unavailable wherever the system builds a learner profile.**

### 🔴 The confidence attached to this correction — stated, not assumed

🔴 **Every European primary-source host failed DNS resolution in this session:**
`eur-lex.europa.eu`, `digital-strategy.ec.europa.eu`, `artificialintelligenceact.eu` — while
`raw.githubusercontent.com` and `api.github.com` resolved normally. 🔵 **Recorded as `DNS_BLOCKED`,
a fourth instrument state** (see `compose/patterns.md` `P807`); it is a *network* fact about this
session, not a claim about the documents.

🟢 **So this pass verified code and could not verify statute.** The correction rests on **four
independent secondary channels in agreement** on the two load-bearing dates (`2027-12-02` Annex III,
`2028-08-02` Annex I) — including two law-firm client notes, a research note, and a EUR-Lex record
*title* returned by search (*"Regulation (EU) 2026/1744 … of 8 July 2026 amending Regulations (EU)
2024/1689 …"*). 🟡 **Lower-confidence, single-channel items, carried as such and not built on:**
high-risk systems operated by **public authorities** deferred to `2030-08-02`; the national
**regulatory sandbox** obligation moved to `2027-08-02`.

🟢 **Why the correction is published anyway rather than held:** 🔴 **the direction of the error is
the dangerous one.** Pass 67 told a reader an obligation was live that is not. A client who acted on
it would have bought a conformity assessment **sixteen months early** — real money against a regime
whose implementing standards are not finished. 🔵 **And the reverse error is now the live risk:**
`2027-12-02` is a deferral, **not a repeal** (`P808`). 🟢 **`Gap 308` records the unverified-against-
primary-text status so a later pass with DNS can close it in one fetch.**

### 🟢 🆕 The deadline that is actually imminent, and this shelf already built for it

🔵 **Article 50 did not move.** 🔴 **Article 50(2) marking grace ends `2026-12-02` — eight weeks from
this pass** — for providers of generative systems placed on the market before `2026-08-02`. Systems
placed from `2026-08-02` onward got **no grace at all**. 🟡 Content generated *and published* before
`2026-08-02` needs no retroactive marking; content generated before but **published on or after**
that date **does**.

🟢 **This shelf's `compose/code/aiact-50-2-*` tier — four directories, built across passes 60–66 —
targets exactly this obligation.** 🔵 **The pass-67 prose was wrong about high-risk while the code
was right about Article 50**, and the Omnibus has made the code the more valuable of the two.
🟢 **`P11` this pass turns it into a dated, deliverable recipe** (`compose/patterns.md`).

🟡 **Two supporting instruments, both non-binding and both useful in a client file:** Commission
interpretive guidelines on Article 50 (**`2026-07-20`**) and the AI Office's voluntary **Code of
Practice on transparency of AI-generated content** (**`2026-07-31`**).

### 🟢 Market size — carried forward, with its provenance unchanged

🟡 **$10.6B (2026) → $42.48B (2030), CAGR 41.5%** (commercial market-research publisher; the figure
this shelf has carried since pass 54). 🔴 **A competing estimate puts 2026 at $12.3B**, and a third
set of regional splits below does not sum to either. 🔵 **Treat all three as order-of-magnitude.**
🟢 The non-vendor numbers are the ones to quote: **86% of education organisations use generative AI
and most lack a policy**, and **teachers who use AI weekly report ~5.9 hours/week saved**.

## Opportunities by region — superseded (the live block is at the top of this file)

🔵 **One `###` per region, closed vocabulary. Where a channel returned nothing for a region, that is
written down as a gap rather than left silent** — an informed gap is information; silence looks like
coverage.

### North America

🟢 **Measured this pass.** 🔵 **134 bills on AI in education across 31 states** in the 2026 session,
concentrated on **student-data privacy, classroom-use limits and curriculum**. 🟢 Named instruments:
**California AB 1159** (bars student data from training AI models unless the school directly
benefits); **Idaho SB 1227** (statewide framework); **Oklahoma and Maryland** (require human
oversight; bar AI from high-stakes decisions about students); **Oregon SB 1546** (design duties for
minors, including reducing compulsive use); **Ohio** — **the first state to require every K-12
district to adopt a formal AI policy, deadline `2026-07-01`, now passed**. 🟡 Federal: **H.R. 8747**,
the *K-12 AI Literacy and Readiness Act of 2026*, advanced out of House Education and Workforce on
**`2026-07-21`**. 🔵 **NASBE: 30+ states** now hold AI guidance, with 2026 work shifting to
*refinement*. 🟡 **NYC** runs a **one-year moratorium on student-facing AI through grade 8**.
🔵 Adoption: **60% of US K-12 teachers** used AI tools in 2024-25, **32% weekly**; the region is
~**36% of the global market** at ~**$3.68B (2026)**.

🟢 **The opportunity, and it follows from the policy shape rather than from the adoption rate:**
**human-oversight-of-record**. Oklahoma, Maryland and the CCSD-style district policies all forbid AI
as the *sole basis* for placement, discipline or special-education decisions. 🟢 **That is a
build:** a decision-logging layer that makes the human reviewer's involvement *provable* — xAPI to
an Apache-2.0 LRS (`lrsql`), competencies in MIT **OpenSALT**, the SIS left untouched behind
**LTI 1.3**. 🔵 **Ohio's passed deadline and 30+ state guidance documents mean the buyer already has
a written policy and no instrument to evidence it.** 🟢 Second opportunity: **AB 1159-shaped data
boundaries** — "no student data leaves for model training" is an architecture, and the permissive
substrate tier is how you build it.

🔴 **Declared gap:** the North America channel returned **US material only**. **Canada and Mexico
produced nothing** — no federal or provincial education-AI instrument, no adoption figure.
🔵 Mexico appears below under **LATAM**, which is where this shelf places it. 🔴 **Canada is
genuinely unplaced and should not be sold as covered.**

### EMEA

🔴 **This is where the pass's correction lands, and it changes the sales motion.** 🟢 Annex III
education obligations apply **`2027-12-02`**, not August 2026. 🔴 **Article 50 has applied since
`2026-08-02`, and the 50(2) marking grace expires `2026-12-02`.**

🟢 **So the EMEA opportunity has inverted in urgency.** 🔵 The high-risk conformity-assessment work —
which a pass-67 reader would have treated as overdue — is a **2027 programme** with time to build
properly. 🔴 **The Article 50 marking work is a 2026 Q4 emergency** for any provider with a
generative education product already on the EU market. 🟢 **`P11` is the recipe, and this shelf's
`aiact-50-2` code is the implementation.**

🟡 Adoption, low-confidence single-channel: **Europe ~$2.64B (2026) → ~$8.0B (2030), CAGR 31.9%**,
with **Finland, Estonia and the Netherlands** named as K-12 leaders. 🟢 Concrete public spend: the
**UK invested £4M** in AI for lesson planning and marking. 🟢 **The OECD's 2026 outlook recommends
moving beyond general-purpose tools toward purpose-built educational AI** — which is the same
conclusion this shelf reached by measurement (see `intel/trends.md`).

🟢 **Sovereignty remains the EMEA-specific shape** and the permissive substrate tier serves it
directly: self-hostable **`lrsql`** (Apache-2.0), **OpenSALT** (MIT), **Ed-Fi DMS** (Apache-2.0) —
no component in that chain requires a US cloud.

🔴 **Declared gaps, and they are large.** 🔴 **No country-level education-AI rule outside the EU was
returned** — the UK, Switzerland and Norway produced nothing beyond the £4M spend. 🔴 **The Middle
East and Africa returned nothing at all**: no instrument, no adoption figure, no player. 🔵 EMEA on
this shelf currently means **EU + a UK line item**, and a deck that implies Gulf or African coverage
would be overstating this file.

### APAC

🟢 **The region with the most *education-specific* statute, which is the opposite of the usual
picture.** 🔵 **Vietnam — Law No. 134/2025/QH15**, enacted **`2026-03-01`**, with **extraterritorial
reach** over foreign technology companies in Vietnamese AI activity, and a high-risk list that
**names education**, citing **automated assessment and behavioural monitoring**. 🟡 The qualifier
matters commercially: many systems are high-risk **only when their output is the sole basis for a
decision without meaningful human review**. 🟡 Compliance timing for high-risk education systems
reported as **September 2027** — **single commercial channel, low confidence, do not quote**.
🟢 **South Korea — AI Framework Act in force `2026-01-22`**, with a **domestic-representative
requirement** for non-Korean providers over revenue/user thresholds. 🟢 **Taiwan** passed its **AI
Basic Act** in **December 2025**. 🟢 **Australia** stood up an **AI Safety Institute** (November
2025) and released a **National AI Plan** (December 2025). 🟡 Singapore and Japan are working through
**governance toolkits and assurance frameworks**; China through **binding content regulation**.
🔵 Adoption: **Singapore leads at 60.9% AI diffusion** among working-age adults; **only 1 in 10 APAC
enterprises** call themselves "very mature"; **~1% have fully operationalised responsible AI**.
🟡 Market-research view of key players: **Google, Microsoft, IBM, Pearson, Byju's**, with **China,
India and Japan** dominating and China leading on state backing.

🟢 **The opportunity is the one Vietnam's qualifier creates: *meaningful human review* as a
product.** 🔵 Vietnam names education high-risk, and then **exempts systems with real human review in
the loop**. 🟢 **So the same oversight-evidence layer that North America's state laws demand is, in
Vietnam, a route out of the high-risk classification itself** — the strongest cross-region reuse this
file has recorded. 🟡 Second opportunity: **Korea's domestic-representative rule** is a recurring
compliance-operations engagement for any non-Korean edtech provider.

🔴 **Declared gaps:** 🔴 **no education-specific adoption figures for APAC schools or universities**
were returned — the diffusion and enterprise-maturity numbers are economy-wide, not education.
🔴 **No country-level education regulation beyond Vietnam** — China, India and Japan were named as
*markets* and never as *regulators of education AI*. 🔵 Treat APAC education policy as **Vietnam and
Korea measured, the rest unread**.

### LATAM

🟢 **The best-measured adoption data on this shelf, from non-vendor sources.** 🔵 **UNESCO IESALC,
launched September 2026: 87% of institutions use AI in at least one area**, across **200 higher
education institutions in 19 countries** — with the explicit finding that **governance frameworks and
institutional strategies are not keeping pace**. 🟢 **Digital Education Council LATAM survey 2026**
(with Tecnológico de Monterrey's Institute for the Future of Education): **92% of students and 79% of
faculty actively engage with AI**; 🟡 but **88% of faculty report only minimal-to-moderate
engagement**, and 🔴 **the lowest adoption of any use case is assessment**. 🔵 **61% of students fear
AI misuse by peers** — an integrity and fairness concern, not a capability one.

🟡 Policy: **Uruguay** was the **first LATAM state to sign the Council of Europe Framework Convention
on AI** (2025); **Peru**'s framework includes **regulatory sandboxes**; **Mexico** has a federal AI
bill in the Senate on a risk-based structure with a proposed oversight authority; **Colombia** went
the policy route first with **CONPES 4144** (February 2025). 🟢 **UNESCO is the region's most active
institutional actor**: its **Observatory on AI in Education for Latin America and the Caribbean**
launched **14 April**, with a **Mexico pilot alongside CONALEP and DGETI** building centres of
excellence, plus ethics-and-regulation capacity work in **Ecuador and Chile**. 🟡 **WEF with
McKinsey** published a regional **AI Competitiveness Roadmap**.

🟢 **The opportunity is a gap between two measured numbers, and it is the sharpest in this file:
87% institutional adoption against governance that "lags behind", with assessment the least-adopted
use case.** 🔵 **The demand is not for more AI; it is for the governance layer underneath the AI
already deployed.** 🟢 **That is a deliverable this shelf can build entirely permissively** — an
institutional AI-use register, oversight logging to an Apache-2.0 LRS, competency mapping in MIT
OpenSALT, no copyleft anywhere (`P8`/`P10`). 🟡 **And the assessment gap is a sequencing gift:**
institutions have not yet automated assessment, which is precisely the use case every high-risk
regime targets — so a LATAM engagement can **build the oversight layer before the exposure exists**,
rather than retrofitting it.

🔴 **Declared gap:** 🔴 **nothing specific to K-12 was returned for LATAM in 2026** — every adoption
figure above is **higher education**. 🔵 School-sector adoption and any K-12 rule are **unread on
this shelf**.

### Global

🟢 **The pass's cross-region result is a licensing law, and it determines what can be sold in every
region equally** (`P809`, `repos/foundations.md`): **the grant follows the author class.** Standards
bodies and alliances publish **permissively** (Ed-Fi DMS Apache-2.0, 1EdTech OpenCASE Apache-2.0,
OpenSALT MIT, the xAPI-LRS tier); **sector product communities publish copyleft** — the
system-of-record tier read this pass is **5 of 5 non-permissive**; **credential issuers are AGPL to a
repo**.

🟢 **So the globally portable engagement shape is the same everywhere:** build on the **substrate**,
integrate with the **product** across **LTI 1.3**, and keep the client's code permissive on their
side of that boundary. 🔵 **The regional variable is not the architecture — it is which obligation
pays for it:** oversight evidence in North America, Article 50 marking then 2027 conformity in EMEA,
meaningful-human-review as a high-risk exit in APAC, and institutional governance catch-up in LATAM.


## 🟢 Sixty-seventh pass, 2026-10-08 — the EU AI Act is **in enforcement** (since `2026-08-02`), education's high-risk trigger is read **as a four-part test**, Vietnam becomes the **second jurisdiction to name education on a statutory high-risk list**, and the new **CASE/LER tier** makes a skills-side deliverable buildable in every region

⏱️ **Twenty-first pass of this date. Append-only: this section is new; nothing below it was rewritten. Pass 66's `## Opportunities by region` block is marked superseded in place; the live block is in this section.**

🔵 **All four regions were probed and all four returned substance this pass** — which has not been
true of every pass, and is stated first because an unprobed region and an empty one look identical
later.

### 🟢 🆕 The pass's principal finding: the EU AI Act moved from *dated obligation* to *live enforcement*, and this shelf was still carrying it as a future date

🔴 **What this KB held:** future compliance positions at **`2027-12-02`** (three channels, passes
64–66) and a second date for embedded systems.

🟢 **What this pass measured, from the European Commission's own digital-strategy pages:**

| Date | Event | Status |
|---|---|---|
| **`2026-08-02`** | 🟢 **The AI Office and national authorities STARTED ENFORCING the AI Act** | 🟢 **in force — past, not future** |
| **`2026-07-27`** | 🟢 The **"AI omnibus"** targeted amendments **entered into force** (proposed Nov 2025, adopted June 2026) | 🟢 in force 🆕 |
| `2027-12-02` | Previously held position | 🟢 unchanged, still ahead |

🔵 **Why this is the most consequential correction of the pass:** every regional opportunity below
changes tense. 🔴 **A proposal written on the old reading sells "preparation for a 2027 deadline."**
🟢 **The correct reading sells remediation against a regime whose supervisor has been operating for
over two months**, with **67 days** of enforcement elapsed at this pass.

### 🟢 🆕 Education's high-risk trigger, read as a **four-part test** rather than a label

🔵 Prior passes recorded "education is Annex III high-risk" as a category. 🟢 **This pass reads the
trigger as four distinct functional limbs**, which is what makes it checkable against a client's
actual system:

| # | Limb | What it catches |
|---|---|---|
| 1 | 🔴 **Evaluates learners** | automated marking, scoring, formative assessment used for record |
| 2 | 🔴 **Assigns them to programmes** | placement, streaming, admissions triage |
| 3 | 🔴 **Detects prohibited behaviour during assessments** | 🟢 **proctoring, named explicitly** |
| 4 | 🔴 **Influences access to qualifications** | progression gates, credential award decisions |

🟢 **Consequence named in the same source:** a system hitting any limb needs a **conformity
assessment — internal, or third-party audit — *before* being placed on the market or put into
service.** 🔴 **Before, not after**, which makes it a gate on the engagement, not a deliverable of
it.

🟢 **Extraterritorial reach, restated:** scope attaches to **any company placing an AI product on
the European market, or deploying one that affects EU students or learners, regardless of where the
company is headquartered.** 🔵 **This is the sentence that makes the EU limb a North America and
LATAM concern too**, and it is why the regional sections below are not independent.

🔴 **The conflation this shelf must refuse, stated here as well as in `agents/top.md`:** the
**standards**-conformance harness found this pass (`conform-ed`, MIT) is **not** an AI Act
conformity assessment. 🔵 Different regime, different assessor. 🟢 It produces interoperability
evidence that belongs *in* the file; it does not produce the file.

### 🟢 🆕 Vietnam — the **second** jurisdiction on this shelf to name education on a statutory high-risk list

| Jurisdiction | Instrument | Status | Education position |
|---|---|---|---|
| 🇪🇺 **EU** | AI Act | 🟢 **enforcing since `2026-08-02`** | 🔴 Annex III high-risk, four-limb test above |
| 🇻🇳 **Vietnam** | **Law on Artificial Intelligence** | 🟢 passed **`2025-12-10`**, **in force `2026-03-01`** | 🔴 **high-risk list names education explicitly — *"automated assessment and behavioural monitoring"*** 🆕 |
| 🇰🇷 **South Korea** | **AI Basic Act** | 🟢 in force **January 2026**; 🟡 **2026 is a pilot year, one-year grace on penalties** (MSIT) | 🟡 general high-risk regime 🆕 |
| 🇹🇼 **Taiwan** | AI Basic Act | 🟢 passed **December 2025** | 🟡 framework law 🆕 |

🟢 **The convergence is the datum:** two jurisdictions on two continents have now written
**automated assessment** and **behavioural monitoring during assessment** into binding high-risk
law, in nearly the same words. 🔵 **That is no longer a European peculiarity to be waited out** — it
is the emerging global default, and it lands on exactly the two functions an education AI pilot
reaches for first.

🟡 **Source conflict recorded, not smoothed:** one channel described Vietnam's instrument as a
*Digital Technology Industry Law* effective 2026; a second, more specific channel named a
**standalone Law on Artificial Intelligence** with the dates above. 🟢 **The more specific reading
is carried**, and 🔴 **it is not confirmed from the statute text — this session cannot reach it.**
🟢 **`Gap 304` opened.**

### 🟢 Market sizes, with the conflicts left visible

| Scope | Figure | Source class | Confidence |
|---|---|---|---|
| Global AI-in-education, 2026 | **$10.6 B** → **$42.48 B** (2030), **CAGR 41.5 %** | market-research house | 🟡 held across four passes |
| Global, 2026 | **$12.3 B** | vendor citing HolonIQ | 🔴 **conflicts with the above by ~16 %** |
| **North America**, 2026 | **$3.68 B**, **36 %** of global | aggregator | 🟡 🆕 |
| **EMEA (Europe)**, 2026 | **$2.64 B** → **$8.0 B** (2030), **CAGR 31.9 %** | 🔴 vendor-style aggregator, research origin unnamed | 🔴 **low** 🆕 |

🔴 **The spread is the datum.** Two figures for the same year and same global scope differ by
$1.7 B. 🔵 **A deck that quotes one without the other is quoting a choice, not a measurement.**
🟡 **The regional figures sum to roughly $6.3 B against a $10.6 B global**, which is consistent only
if APAC and LATAM together are ~40 % — 🔴 **neither was given a 2026 figure by any channel this
pass**, so the sum is not reconcilable. 🟢 **`Gap 305` opened.**

## Opportunities by region — superseded (the live block is at the top of this file)

🔵 **Framing, per `P790`/`P769`: each opportunity names a protocol or a function, never a brand.**
🔵 **Every component named below is a row this shelf has payload-read at a pinned ref.**
🟢 **New this pass:** the **permissive CASE/LER tier** — `opensalt/opensalt` (🟢 MIT, 1 080 B,
`develop`·`db41cc4`), `infosign/compeito` (🟢 Apache-2.0, `main`·`0656e10`), `1EdTech/OpenCASE`
(🟢 Apache-2.0, `main`·`97d0373`) — plus the cross-protocol conformance harness
`conform-ed/conform-ed` (🟢 MIT, `main`·`3596bb5`). 🟢 **Together with pass 66's Apache xAPI store
tier, a skills-and-evidence deliverable is now buildable, permissively, in every region.**
🔴 **What is still NOT buildable permissively anywhere: badge issuance (AGPL) and CLR aggregation
(empty).** That constraint applies to all four regions below and is not repeated in each.

### North America

🟢 **Adoption is real but uneven, and the honest figures disagree with the headline one.**
🟡 **86 %** of education organisations reported using generative AI (market-research claim, held
four passes); 🟢 **60 % of US K-12 teachers used AI tools in the 2024–25 school year and 32 % used
them at least weekly** (survey-class, 🆕 this pass). 🔴 **The gap between 86 % and 32 % weekly is
the sales-qualification question** — organisational access is not teacher practice.

🟢 **Opportunity 1 — the competency/LER registry, and this region is where it is funded.**
🟢 **New this pass:** the **CASE** tier is permissive **and North American in provenance** —
OpenSALT is built by **Public Consulting Group with its public-sector clients**, and it is the
codebase **1EdTech's own CASE Registry is based on**. 🔵 **So a state agency buying a competency
registry is buying a deployment of an MIT codebase, not a bespoke build.**
🟢 **Build:** CASE 1.1 registry (`opensalt`, MIT) as the system of record for standards and
competencies, **CSV/CASE import** from existing state standards documents (`compeito`'s importer
reads **OpenSALT-compatible CSV** and pulls frameworks **from a live OpenSALT CFPackages URL** —
measured, not claimed), **OneRoster 1.2** for enrolment (`edfi-oneroster`, Apache-2.0), **xAPI**
evidence into `lrsql` (Apache-2.0).

🟢 **Opportunity 2 — Ed-Fi migration, newly urgent and newly dated.** 🟢 **`Data-Management-Service`
has a shipped `v8.0.0` tag (`d911abb`) and its README states it replaces the legacy ODS/API and ODS
Admin API.** 🔵 **Every US district and state agency on `Ed-Fi-ODS` now has a migration ahead of it**
— .NET 10, PostgreSQL, Data Standard 5.2 — and the whole path stays **Apache-2.0**.
🔴 **Whether it is a data migration or a no-op is unmeasured (`Gap 303`)**, and a proposal must
price the discovery rather than assume either.

🟢 **Opportunity 3 — student-data-provenance controls, on a live legislative trigger.**
🟢 **California A.B. 1159** would **prohibit student data from being used to train AI models unless
doing so directly benefits the school** (🆕 this pass). 🔵 **This is a data-lineage requirement, not
a policy document** — it asks which records entered which training run, which is answerable from an
**xAPI store** plus provenance marking, and not answerable from a PDF.
🟡 **A.B. 1159 is proposed, not law** — pipeline.

🟡 **Vendor signal, recorded once:** **Microsoft updated its Education AI Toolkit with agentic
capabilities in April 2026** (multi-step administrative workflow automation and tutoring).
🔵 **Read as the incumbent defining the category's default shape**, which is what a differentiated
proposal must answer.

🔴 **Counter-signal, unchanged and still bounding:** the student-facing tutor remains the hardest
sell. **At least 12 US law schools are split between device bans and mandatory AI courses**;
**UChicago Law pilots device-free 1L classes from fall 2026**. 🟢 **The administrative and
evidentiary layer is the easy sell; the tutor is not.**

🔴 **Gap, restated because it did not improve:** the channel is **saturated with US policy
trackers**. 🔴 **Canada and Mexico returned nothing at all again this pass**, and the US readings
above do **not** cover them despite sharing this region bucket. 🔵 **This is a measured hole, not
coverage.**

### EMEA

🟢 **This is the region where the regulatory clock has already struck**, and that reframes every
deliverable here from preparation to remediation (see the enforcement table above).

🟢 **Opportunity 1 — conformity-assessment preparation for the four-limb test, as the lead offer.**
🔵 Any client system that marks work, places students, watches them during an assessment, or gates a
qualification is in scope, **and the assessment must precede going into service**.
🟢 **Build:** the **Apache-2.0 evidence spine** (`ltijs` launch → `TinCanPython` emit → `lrsql`
store) so that *what the system did and who reviewed it* is a queryable record; **CASE** to make the
competency being judged explicit and citable; **`conform-ed`** for interoperability regression
evidence. 🔴 **Named limit: this assembles the technical file; it is not the conformity assessment,
and the proposal must name the assessor.**

🟢 **Opportunity 2 — the governance deficit is the widest here of any region.** 🔴 **Only 10 % of
450+ surveyed schools and universities have established formal AI guidelines** — against a live
enforcement regime. 🔵 **10 % governance under enforcement is a materially worse position than
LATAM's 26 % without one.**

🟢 **Opportunity 3 — national-programme integration, because EMEA buys through ministries.**
🟢 **Country instruments read this pass (OECD Digital Education Outlook 2026):** **Italy** 2025
guidelines on safe and conscious generative-tool adoption; **Ireland** 2025 education-specific
responsible-GenAI principles; **Slovakia** a strategic plan with dedicated initiatives on **AI
assistants for teachers** and personalised learning; **France** AI literacy via the **Pix**
platform; **Czechia** embeds generative AI inside **mandatory digital competence across subjects**;
**Netherlands** school agreements on generative AI via **Kennisnet**. 🔵 **Five of these six are
curriculum-and-competence instruments** — 🟢 **which is precisely what a CASE registry models**, and
is the cleanest fit between this pass's new tier and a regional buying pattern.

🟡 **Middle East and Africa, stated separately because the maturity is different.** 🟡 Regulation is
**nascent but fast-moving**: **UAE National AI Strategy 2031** + **AI Ethics Guidelines**, Saudi
Arabia's **SDAIA** framework; **Kenya, South Africa and Nigeria are actively drafting** national AI
policy. 🔴 **The channel carrying this was an insurance-sector overview — its education relevance is
indirect and it is carried as weak.** 🔴 **No education-specific MEA instrument was read.**

🔴 **Gaps:** 🔴 **no EMEA-specific education *adoption rate* was found**; 🔴 **the UK returned no
education-specific rules**; 🔴 **how the AI Act's delayed high-risk timelines apply specifically to
schools was not resolved.** 🟢 **`Gap 306` opened** for the UK hole, which is conspicuous for a
market this size.

### APAC

🟢 **Opportunity 1 — multi-jurisdiction compliance as the product, because divergence is the
regional condition.** 🔵 APAC does not have one regime; it has at least six postures:
🔴 **binding** (China: algorithms, deep synthesis, generative AI), 🟢 **statutory with education
named** (Vietnam, in force `2026-03-01`), 🟡 **statutory in grace** (South Korea, in force Jan 2026,
**pilot year with a one-year penalty grace**), 🟡 **framework** (Taiwan, Dec 2025),
🟡 **voluntary-plus-existing-law** (Singapore, Japan), 🟡 **institutional** (Australia: **AI Safety
Institute** + **National AI Plan**, Dec 2025), plus the voluntary **ASEAN AI Governance Guide**
(updated 2026).
🟢 **Build:** policy-as-configuration — one evidence spine, per-jurisdiction rule nodes. 🔵 **The
`LangGraph` policy-node shape this shelf already carries is the right skeleton**, with the
jurisdiction's limbs as the branch conditions.

🟢 **Opportunity 2 — Korea's grace year is a dated, closing window.** 🟡 **2026 is explicitly a
pilot year with limited enforcement and a one-year grace on penalties.** 🔵 **So remediation bought
in 2026 is cheap and remediation bought in 2027 is not** — the clearest timing argument available in
any region this pass.

🟢 **Opportunity 3 — maturity is the constraint, which favours foundation work over pilots.**
🟡 **Over 50 % of APAC digital-native businesses remain at the "repeatable" stage of AI maturity**
(March 2026). 🔵 **A repeatable-stage buyer cannot absorb an agentic deliverable** — the sellable
work is the substrate: rostering, telemetry, competency definitions.

🟡 **Named incumbents:** **Google, Microsoft, IBM, Pearson, Byju's**; **China, India and Japan**
reported as dominating regional spend, China on heavy state backing, India through online-education
platforms. 🔴 **Market-research class, directional only.**

🔴 **Gaps:** 🔴 **no APAC 2026 market figure** was returned by any channel (see `Gap 305`); 🔴 **no
education-specific adoption percentage** for any APAC country; 🔴 **Vietnam's statute text was not
reachable** (`Gap 304`). 🔵 **Education-specific AI rules in APAC are thin by measurement** —
education appears as a high-risk *category* inside general AI law, not as its own instrument.

### LATAM

🟢 **The strongest first-party evidence base of any region this pass, and it is institutional
rather than vendor.** 🟢 **UNESCO IESALC surveyed 200 higher-education institutions across 19
countries:** 🟢 **87 % use AI in at least one area**, 🔴 **only 26 % have a formal framework.**
🟢 **Supported by UNU-IAS.**

🟢 **The sector split, which is the targeting datum:** 🟢 **84 %** of **private non-profit**
universities use AI, **68 %** of **public** institutions, **52 %** of **private for-profit**.
🔵 **Private non-profit is the warm segment; private for-profit is the cold one** — the inverse of
what a commercial prior would assume.

🟢 **And the use is concentrated exactly where the high-risk limbs are:** 🔴 **74 % use it for
teaching tasks including lesson planning and *grading assessments*.** 🔵 **Grading is limb 1 of the
EU test and is named in Vietnam's statute** — 🟢 **so LATAM's dominant current use is the function
two jurisdictions have already made high-risk**, and EU extraterritoriality reaches any LATAM
institution serving EU learners.

🟢 **Teacher-level adoption runs far above the OECD average (TALIS 2024):** **Brazil 56 %**,
**Chile 55 %**, **Colombia 53 %**, **Costa Rica 52 %**, against an **OECD average of 36 %**;
**Uruguay reports 75 % of public-school teachers** (Ceibal). 🔵 **Country in the prose, region in
the field** — `P769`.

🟢 **Opportunity 1 — governance retrofit at scale, and it is the region's defining gap.**
🔴 **87 % adoption against 26 % frameworks** is a 61-point deficit across 19 countries.
🟢 **Build:** the Apache-2.0 evidence spine plus a **human-review checkpoint** on anything that
becomes a grade — which is the artefact both the EU test and UNESCO's own warning ask for.
🔵 **UNESCO's position is quotable in a proposal:** institutional frameworks **do not match the
speed of adoption**, and the absence of guidelines **increases the risk of misuse**.

🟢 **Opportunity 2 — competency and pathway registries for skills-based workforce programmes.**
🟢 **New this pass and a genuine fit:** OpenSALT models **competencies, credentials, learning
opportunities, jobs and pathways** together, under **MIT**, and aligns to **Credential Engine CTDL**
and **W3C VCs**. 🔵 **LATAM's workforce-reskilling programmes are the clearest buyer of a
competency-to-occupation join**, and it is now permissive.
🔴 **Priced limit: badge issuance remains AGPL-only** — so the lawful shapes are an arm's-length
hosted issuer or a written one (`P9`).

🟢 **Opportunity 3 — regulatory-readiness advisory against three live national tracks.**
🟡 **Brazil PL 2.338/2023** — risk-based, **Senate approved Dec 2024, now in the Chamber of
Deputies, text can still change**; 🟡 **Chile** — government bill unified with an earlier
parliamentary initiative, **first constitutional stage** in the Chamber's Commission on Future,
Science and Technology; 🟢 **Colombia CONPES 4144** — adopted **February 2025**, a government-wide
programme **with actions and budget through 2030**. 🔵 **Colombia is the only one with money
attached**, which makes it the first door.

🟢 **Institutional players to engage, all first-party:** **UNESCO IESALC** (the 2026 study);
**UNESCO's Observatory on AI in Education for Latin America and the Caribbean**, launched
**14 April** at **ECLAC headquarters, Santiago**; UNESCO's **Quito and Chile offices** running AI
regulation and ethics courses for officials; **Ceibal** (Uruguay); **Digital Education Council**
(2026 LATAM survey, **30 000+ responses across 29 institutions**); **Argentina's UIA** responsible-
AI guide. 🔵 **Institutional leaders surveyed named staff training and internal AI advocates as the
most important adoption drivers** — 🟢 **which makes enablement a sellable line item, not overhead.**

🔴 **Gap:** 🔴 **no LATAM 2026 market figure** from any channel this pass (`Gap 305`); 🔴 **no
dedicated education-AI law exists anywhere in the region** — general AI law and national policy
apply instead, which is itself the finding. 🟡 **Brazilian and Chilean bill statuses are carried
from a May 2026 source and were not re-confirmed against a legislative tracker.**

### 🟢 Region coverage of this pass, stated plainly

| Region | Probed | Returned | Honest verdict |
|---|---|---|---|
| **North America** | 🟢 yes | 🟢 substantial | 🟡 **US-only** — Canada and Mexico **empty again** |
| **EMEA** | 🟢 yes | 🟢 substantial | 🟡 **EU-strong**, 🔴 UK empty, 🟡 MEA weak and indirect |
| **APAC** | 🟢 yes | 🟢 substantial on regulation | 🔴 **no adoption or market figures** |
| **LATAM** | 🟢 yes | 🟢 **strongest first-party evidence** | 🟡 no market figure |

🟢 **Four of four regions probed and four of four returned usable intelligence.** 🔴 **Three
distinct holes are recorded above as holes — Canada/Mexico, the UK, and APAC/LATAM market sizing —
because an unprobed region and an empty one are indistinguishable six passes later.**


## 🟢 Sixty-sixth pass, 2026-10-08 — the **governance deficit is now quantified in all four regions by four independent instruments**, and the EU's `2027-12-02` position gets a third channel plus a **new second date** for embedded systems

⏱️ **Twentieth pass of this date. Append-only: this section is new; nothing below it was rewritten.**

🟡 **Every figure in this section is channel-reported.** 🔴 **Not one was read at a primary source.**
🔵 **And the instrument note changed this pass:** passes 64–65 established `EGRESS_DENIED
(allowlist)` for every analyst and policy host, pass 65 confirming it from the gateway's own failure
ledger (`P798`). 🔴 **This pass could not re-read that ledger** — the probe was declined by the
**local auto-mode classifier**, not by the egress gateway. 🟢 **Recorded as a distinct instrument
state with a distinct remedy:** the allowlist gap is unchanged as far as anything here shows, but
**this pass has no first-party record of it**, so the `EGRESS_DENIED` attribution is carried forward
from pass 65 rather than re-measured.

### 🟢 🆕 The pass's principal finding: adoption outruns governance **in every region, measured four different ways**

🔵 Pass 65 paired two instruments on this (K-12 Academics' 86 %-without-policy and UNESCO IESALC's
87 %/26 % LATAM split) and called it the strongest corroboration it had. 🟢 **This pass completes the
map — all four regions now carry a governance figure, from four unrelated surveys of four different
populations.**

| Region | Adoption | Governance | Instrument |
|---|---|---|---|
| **Global / US K-12** | 🟢 **86 %** of education organisations use gen-AI | 🔴 **most lack any policy**; teacher use roughly **doubled in a year** (**60 %** in 2024–25) | K-12 Academics, *State of AI in Education 2026* |
| **LATAM** (higher ed) | 🟢 **87 %** of institutions use AI in ≥1 area — **200 institutions, 19 countries** | 🔴 **26 %** have any formal framework | UNESCO IESALC 2026 (with UNU-IAS) |
| **EMEA** | 🟡 not given in the same instrument | 🔴 **10 %** of **450+** schools and universities have established formal AI guidelines | survey via channel 🆕 |
| **APAC** | 🟡 "governance lagging adoption across the region" | 🔴 **1 %** of organisations have **fully operationalised responsible AI** | WEF-based finding via channel 🆕 |

🟢 **Four populations, four methodologies, one direction, no exceptions.** 🔵 **This is the most
robust claim in this KB**, and it is not a market-size claim — it is the claim that the **binding
constraint on education AI is institutional governance capacity, not model capability or budget.**
🔴 **The numbers are not comparable to each other** (different denominators, different definitions of
"policy" and "framework", different years) 🟢 **and they do not need to be**: every one of them is a
single-digit-to-low-double-digit governance rate against a high-double-digit adoption rate.

🟢 **The engagement consequence, stated once and applicable to all four regions:** the deliverable a
client can actually absorb is **governance scaffolding around AI that is already in use** — policy,
audit trail, human-review checkpoints, evidence of effect — **not another AI feature**. 🔵 This is
exactly what the trend channels independently predicted (see `intel/trends.md`, where OECD now makes
a fifth converging voice).

### 🟢 EU AI Act — a third channel for `2027-12-02`, and a **new** date this KB did not hold

🟢 **Held position, now triple-sourced:** the **Digital Omnibus on AI** received final Council
approval, revising application to **`2027-12-02` for stand-alone high-risk AI systems**. 🔵 Passes 64
and 65 each had one channel for this; **this pass is the third**, and it is the first to pair it with
its sibling date.

🟢 🆕 **New datum: `2028-08-02` for high-risk AI systems *embedded in regulated products*.** 🔵 **Why
this matters more than a second date normally would:** an AI tutor shipped as a feature of a
regulated product is on a **different clock** from the same tutor shipped stand-alone — an
eight-month gap that is a legitimate sequencing lever in an engagement plan.

🟡 **Other dates in circulation, recorded with their conflict intact:** one guide still says high-risk
obligations apply from **August 2026**; the Commission's own page says the amendments were **adopted
June 2026 and entered into force 2026-07-27**; and **from `2026-08-02` the AI Office and national
authorities began enforcing** the AI Act. 🔴 **These are not all reconcilable from the channel alone**
— enforcement commencing is not the same event as high-risk obligations applying. 🟢 **The KB's
position stays `2027-12-02` / `2028-08-02` for high-risk application**, with enforcement machinery
live since `2026-08-02`. 🔴 **Confirm against the Official Journal before any client commitment** —
this shelf cannot reach it.

🟢 **Education's classification is unchanged and is the reason any of this is on this shelf:** AI used
in **education access and assessment** — admission decisions, student evaluation, exam scoring — is
**high-risk**, carrying risk management, data governance, **human oversight**, transparency and
conformity-assessment obligations before deployment. 🟢 Vendors must additionally **collect
performance data, report serious incidents to national authorities, and update on defect**.

### 🟢 🆕 The convergent legal test: *"sole basis, without meaningful human review"*

🟢 **Vietnam's high-risk list includes education explicitly** — automated assessment and behavioural
monitoring — and qualifies it: **many listed systems count as high-risk only when the AI output is
the sole basis for a decision without meaningful human review.** 🔵 **That is the same hinge the EU
AI Act turns on (human oversight) and the same hinge US state law is converging on** — Oklahoma and
Maryland reportedly **require human oversight and bar AI from high-stakes decisions about students**;
NYC's red tier **prohibits** AI for grading, discipline and IEP development.

🟢 **Three jurisdictions on three continents, written independently, landing on one architectural
requirement.** 🔵 **So human-in-the-loop is not a compliance nicety to be added late — it is the
single design decision that determines a system's regulatory class in every major market at once.**
🟢 **This is the most portable finding of the pass**: build the review checkpoint first, and the same
architecture clears NA, EMEA and APAC.

### 🟢 Market sizes, with the conflicts left visible

| Scope | Figure | CAGR | Source class |
|---|---|---|---|
| **Global** AI in education | **$10.6 B (2026) → $42.48 B (2030)** | **41.5 %** | 🟡 Research and Markets — held since pass 54, re-confirmed this pass |
| **EMEA / Europe** 🆕 | **$2.64 B (2026) → $8.0 B (2030)** | **31.9 %** | 🟡 channel-reported, single source |
| **LATAM** | **$1.5 B → $4.2 B** | **~45 %** | 🟡 held from prior passes, **not** re-measured this pass |
| **APAC** | 🔴 **no figure obtained** | — | 🔴 a report exists (Ken Research, AI in Education to 2030) but **returned no size through this channel** |

🔴 **One figure is explicitly rejected, not recorded:** a **$12.3 B** market size attributed to
HolonIQ via a vendor blog, whose headline claims (*42 % better outcomes*, *83 % of institutions
planning AI teaching assistants*) **trace to no primary study** and whose attribution **HolonIQ's own
snapshot did not corroborate**. 🟢 **Named here so it is not re-admitted next pass.**

🔵 **The arithmetic worth noting:** Europe at **31.9 %** against a global **41.5 %** means **Europe is
forecast to grow more slowly than the world** — 🟢 consistent with a high-risk regulatory regime
whose obligations land in **2027–2028**, and a reason to read EMEA engagements as **compliance-led
rather than adoption-led**.

## Opportunities by region — superseded (the live block is at the top of this file)

🔵 **Framing, per `P790`/`P769`: each opportunity names a protocol or a function, never a brand.**
🔵 **Every component named below is a row this shelf has payload-read at a pinned ref.**
🟢 **New this pass:** the **Apache-2.0 xAPI store tier** (`yetanalytics/lrsql` `main`·`cb794e4`;
`pelotech/xapi-lrs` `main`·`4d18e0c`) makes an **evidence-and-audit** deliverable buildable in a
closed engagement **in every region** — which is what all four governance figures above are asking
for.

### North America

🟢 **The market is legislating faster than it is buying, and it is legislating about *records*.**
**134 bills across 31 states** in the 2026 session; **33–35 state departments of education** plus
Puerto Rico now publish official AI guidance.

🟢 **Opportunity 1 — district AI-policy compliance tooling, on a statutory deadline.**
**Oklahoma SB 1734** requires **every district** to adopt a written AI policy **before the 2027–28
school year**; **Ohio** and **Tennessee** require districts to author their own policies (Ohio's
requirement effective **2026-07-01**); **Maryland's 24 districts** must adopt by **fall 2026**.
🔵 **These are thousands of institutions with a dated obligation and no internal capacity** — the
clearest procurement trigger in any region this pass.
🟢 **Build:** policy-as-configuration over an **xAPI statement store** (`lrsql`, Apache-2.0) with
**LTI 1.3** launch (`Cvmcosta/ltijs`, Apache-2.0, `master`·`0ec24fe`) — the audit trail *is* the
compliance artefact.

🟢 **Opportunity 2 — human-review checkpoints for the prohibited tier.**
**NYC's red tier bans AI for grading, discipline and IEP development**; **Oklahoma and Maryland**
require human oversight on high-stakes student decisions. 🔵 **The ban is on unreviewed
automation, not on assistance** — so the sellable artefact is a **reviewable workflow** that records
who decided what, on what evidence, and when. 🟢 **`P8` is this, end to end, under Apache-2.0.**

🟢 **Opportunity 3 — AI literacy delivery against federal and state funding.**
**H.R. 8747 (K-12 AI Literacy and Readiness Act)** advanced through committee **2026-07-21**, which
would let schools spend federal funds on AI curriculum; the **US Department of Education finalised a
grant-priority rule on 2026-04-13** favouring projects that expand AI understanding or ethical use;
**Alabama HB 329** makes a CS course including AI instruction a **graduation requirement**.
🟡 **H.R. 8747 passed committee largely along party lines and is not law** — treat as pipeline.

🔴 **Counter-signal, recorded because it bounds the above:** adoption is deliberately cautious and in
places reversing. **Berkeley Law bans generative AI on exams and credited coursework from summer
2026**; **UChicago Law** is piloting device-free 1L classes; a **one-year moratorium on
student-facing AI through eighth grade** is being urged on districts after NYC's example. 🟢 **The
student-facing tutor is the hardest sell in North America; the administrative and evidentiary layer
is the easy one.** 🟡 **Student-authored framing exists too** — the **STUDENTS FIRST Act of 2026**
(AASA / Day of AI, **2026-08-03**, students from all 50 states) rejects both a blanket ban and
unrestricted adoption.

🔴 **Gap:** the vendor and courseware-publisher side of North America **returned nothing usable this
pass** — the channel is saturated with policy trackers. **Canada and Mexico returned nothing at
all**, and are **not** covered by the US readings above despite sitting in this region.

### EMEA

🟢 **The region's defining fact is a dated regulatory cliff with a slower market behind it.**
High-risk application at **`2027-12-02`** (stand-alone) and **`2028-08-02`** (embedded in regulated
products); enforcement machinery live since **`2026-08-02`**; market **$2.64 B → $8.0 B (2030)** at
**31.9 %**, *below* the global 41.5 %.

🟢 **Opportunity 1 — conformity-assessment readiness as the engagement, 12–18 months ahead of the
deadline.** Education access and assessment is **high-risk**: risk management, data governance,
human oversight, transparency, conformity assessment **before deployment**, plus **performance-data
collection and serious-incident reporting** afterwards. 🔵 **Only 10 % of 450+ institutions have
formal guidelines** — the gap between that and a conformity file is the whole opportunity.
🟢 **Build:** the **Apache-2.0 telemetry spine** (`P8`) supplies the performance data and incident
evidence the Act requires; nothing in it is copyleft, so it ships inside a client deliverable.

🟢 **Opportunity 2 — sovereign, self-hosted deployment.** 🔵 Unchanged from prior passes and
reinforced by this one: the entire spine (**`lrsql` / `xapi-lrs` / `ltijs` / `TinCanPython`**) is
self-hostable with **SQLite or Postgres** and no managed dependency, so data residency is a
deployment choice rather than a vendor negotiation.

🟢 **Opportunity 3 — national-programme delivery.** **Finland, Estonia and the Netherlands** are named
as K-12 AI-integration leaders; the **UK's AI Opportunities Action Plan** is a principles-based
regime (and the UK government has invested in AI tools for teachers); in the **Gulf, the UAE and
Saudi Arabia** are running national AI strategies with heavy infrastructure spending. 🔵 **Two
distinct engagement shapes in one region** — EU-regulated compliance work, and Gulf greenfield
build-out with no comparable regime.
🟡 **The Netherlands also supplies the region's only education-credential codebase read this pass** —
**SURF's `edubadges-server`** (`develop`·`9775cc2`) 🔴 **AGPL-3.0**, so reference architecture only.

🔴 **Gap:** **no authoritative EMEA-wide adoption survey exists** in this channel. The 10 %/450+
figure is **single-sourced**. **UNESCO guidance** and the **OECD Digital Education Outlook 2026** are
named but were **not read**; all policy hosts remain unreachable from here.

### APAC

🟢 **The region is the one that has moved from guidance to binding law, and it did so without
converging on a single model.**

🟢 **Opportunity 1 — extraterritorial compliance for anyone serving APAC users.**
**South Korea's AI Framework Act (AI Basic Act) took effect `2026-01-22`** and **reaches foreign
providers serving Korean users**, with a **domestic-representative requirement above revenue or user
thresholds**. **Vietnam's AI law** (effective **`2026-03-01`** per the channel) also has
**extraterritorial reach** over foreign companies participating in AI activities in Vietnam.
🔵 **This is a market-entry gate, not a local-market opportunity** — and it applies to any global
edtech product, including ones built elsewhere.

🟢 **Opportunity 2 — the human-review architecture, which is literally the statutory test.**
**Vietnam's high-risk list names education** (automated assessment, behavioural monitoring) and
makes high-risk status **conditional on the AI output being the sole basis without meaningful human
review**. 🔵 **A documented review checkpoint can move a system out of the high-risk class
outright.** 🟢 **That is the highest-leverage architectural decision available in this region**, and
`P8`'s evidence trail is what makes the review auditable rather than merely asserted.

🟢 **Opportunity 3 — responsible-AI operationalisation, into an almost empty field.**
🔴 **1 % of organisations in the region have fully operationalised responsible AI.** 🔵 Against
binding law in **Korea, Vietnam and Taiwan** (AI Basic Act, **December 2025**), **Australia's AI
Safety Institute** (**November 2025**), **China's** binding content regulation, and **Singapore's and
Japan's** governance toolkits and assurance frameworks, **a 1 % operationalisation rate against
multiple live statutes is the largest governance gap measured anywhere this pass.**

🟡 **Demand-side, channel-reported and commercial:** **China, India and Japan dominate** APAC AI in
education — China with heavy government backing, India through online-education platforms. Named
incumbents: **Google, Microsoft, IBM, Pearson, Byju's**. 🔴 **This comes from a commercial research
report, not audited data**, and **no APAC market size was obtained.**

🔴 **Gap:** **no APAC education-ministry-level AI regulation** was found — education obligations here
arrive **through general AI law**, not through education policy. Vietnam's effective date is
reported inconsistently across sources (**1 March 2026** in two phrasings), and **grace periods for
education systems could not be verified**.

### LATAM

🟢 **The region with the best-measured adoption and the thinnest governance — and the measurements
are specific enough to build against.**

🟢 **Opportunity 1 — institutional AI frameworks for the 74 % of institutions already using AI for
teaching work.** **UNESCO IESALC (200 institutions, 19 countries): 87 % use AI in at least one area,
26 % have any formal framework, 74 % use it for lesson planning and grading.** 🔵 **The 74 % figure
names the exact workflow** — planning and assessment — so the governance artefact is not abstract: it
is a reviewable record of how a grade or a lesson plan was produced. 🟢 **`P8`'s xAPI spine stores
exactly that**, Apache-2.0, self-hosted, no copyleft.

🟢 **Opportunity 2 — differentiated by institution type, which the data supports.** Adoption splits
**84 % private non-profit / 68 % public / 52 % private for-profit**. 🔵 **The public sector is
twenty-two points behind the private non-profits and is also where the Moodle installed base and the
procurement budgets are** — 🟢 the largest single addressable pocket in the region, and `P7`'s
Moodle-at-arm's-length pattern is already built for it.

🟢 **Opportunity 3 — teacher-facing, because the teachers are already there.** **TALIS 2024: 56 % of
secondary teachers in Brazil, 55 % Chile, 53 % Colombia, 52 % Costa Rica** used AI in the prior year
against an **OECD average of 36 %** — 🔵 **LATAM teachers out-adopt the OECD by roughly twenty
points.** **Uruguay (Ceibal, 2026): 75 % of public-school teachers** report using these tools. 🟢
**The teacher-first rollout the trend channel recommends globally is already the factual situation
here**; the missing piece is institutional sanction, not user willingness.

🟢 **Policy counterparties, all named and dated:** **Brazil PL 2.338/2023** still moving in the
**Chamber of Deputies** (🟡 text can still change); **Chile's** risk-based government bill in its
**first constitutional stage** (Commission on Future, Science and Technology); **Colombia CONPES
4144** adopted **February 2025**, a government-wide programme with **budget through 2030**;
**Uruguay's Ceibal** as an operating national programme. **UNESCO's Latin America Observatory on AI
in Education launched `2026-04-14` in Santiago**; the **IESALC study launched at Digital Learning
Week 2026 in Paris**; **UNESCO regulatory training** has reached senior officials in **Ecuador**
(Ombudsman's Office, Economic Superintendency, Personal Data Protection Superintendency).
🟡 A **Digital Education Council LATAM survey 2026** exists but rests on **29 institutions** — 🔴 too
small to carry a regional claim and not used as one here.

🔴 **Gap:** **no regional AI-in-education law exists** — binding rules come from general AI bills and
national policies, country by country. 🔴 **The LATAM market size ($1.5 B → $4.2 B) is carried
forward from prior passes and was not re-measured.** 🔴 **UNESCO IESALC and Times Higher Education
report the same 2026 study — they are one instrument, not two**, and are counted once above.
🔴 **Adoption here is explicitly uneven across the region**, and the 19-country aggregate hides that.

## 🟢 Sixty-fifth pass, 2026-10-08 — the policy channel is **saturated** (10 of 12 probed data points already held), the EU's `2027-12-02` position gets its **second independent channel**, and `Gap 293`'s closure is re-confirmed from the refusing layer's **own ledger**

⏱️ **Nineteenth pass of this date. Append-only: this section is new; nothing below it was rewritten.**

### 🟢 `Gap 293` re-confirmed, and the evidence class is upgraded

🟢 Pass 64 closed it by a **control** (Wikipedia refused identically to four policy hosts → the
variable is the allowlist). 🆕 **This pass read the refusing layer's own record.**
`$HTTPS_PROXY/__agentproxy/status` → `recentRelayFailures` carries, per host, a **timestamp and a
mechanism**:

```
connect_rejected · "gateway answered 403 to CONNECT (policy denial or upstream failure)"
en.wikipedia.org:443 · digital-strategy.ec.europa.eu:443
www.iesalc.unesco.org:443 · www.multistate.us:443          2026-10-08T19:52:0?Z
```

🟢 **So every policy citation below is `EGRESS_DENIED (allowlist)` — a reading of a first-party
record, not a deduction from a pattern** (🆕 `P798`, suite in `compose/code/p798-proxy-refusal-ledger/`,
9/9 green). 🔴 **Nothing in this section was verified at a primary source**, and that is a property
of this environment, **not** of the sources.

🔴 **And a correction this pass owes its own instrument map:** `pypi` and `npm` sit in the proxy's
**`noProxy`** list, so they **never traverse the gateway that refused those four hosts**. 🔵 **Their
clean 200/404 behaviour is therefore not evidence that the allowlist is broad** — two instruments,
two network paths. A map that conflated them over-read every registry datum it took.

### 🟢 The EU `2027-12-02` position — **second independent channel, same answer**

🟡 `market.md:359` has carried this as *"reported, single-channel."* 🟢 **A fresh channel this pass
reports the same shift:** the **Digital/AI Omnibus** postpones **Annex III** stand-alone high-risk
obligations — education among them — from `2026-08-02` to **`2027-12-02`**, with the amendments
entering into force **2026-07-27** and AI Office/national-authority **enforcement machinery live
from `2026-08-02`**.

🟢 **Upgraded: single-channel → two-channel, independent, agreeing.** 🔴 **Still not primary** — the
Official Journal is `EGRESS_DENIED`.

🔴 **And the superseded date is still circulating.** One source this pass asserted Annex III
compliance by **`2026-08-02`** *"with no extension available."* 🔵 **`P785` vindicated a third time:**
a channel that is current on one entry is not current on all of them, and the KB's rule — **prefer
the position with the later legislative act attached** — is what separated them. 🟡 The conflicting
source is recorded here precisely so it is not re-read as a finding.

### 🔴 The policy channel is **saturated** for this KB, and that is a result

🟢 **Twelve data points from four regional sweeps, probed against this tree:**

| Already held (10) | New (2) |
|---|---|
| Korea AI Basic Act · Vietnam `134/2025/QH15` · UNESCO IESALC · California AB 1159 · Idaho SB 1227 · Ohio district-policy mandate · Colombia CONPES 4144 · Uruguay Ceibal · OECD TALIS · US H.R. 8747 | 🆕 **India MeitY** synthetic-content due-diligence duties for intermediaries, in force **`2026-02-20`** · 🆕 **US: 134 AI-in-education bills across 31 states** in the 2026 session |

🔵 **Ten of twelve already recorded is the first time this shelf has measured its own policy
coverage**, and the reading is that **regional policy sweeps have reached diminishing returns** —
the marginal hour is now better spent on components than on jurisdictions. 🔴 **`P744` holds: 10 of
12 is a count on one sweep, not a coverage rate**; it does not license *"the policy layer is done."*

🟡 **India `2026-02-20` is carried with a caveat:** it is an **intermediary** duty under the IT
rules, **not an education-specific instrument**, and it does not get a `policy-matrix.tsv` row on a
single channel. 🔵 It matters to an education product only where that product publishes
AI-generated content to Indian users.

### 🟢 Market size — the spread is the datum, not any single figure

🟡 **Every figure below is channel-reported; no vendor report was reachable** (`EGRESS_DENIED`).

| 2026 AI-in-education market | source class |
|---|---|
| **$10.6 B → $42.48 B by 2030 (41.5 % CAGR)** | Research and Markets, repeated by two independent channels this pass |
| $11.4 B (2026) | second market-research house |
| $9.58 B (2026) | third market-research house |
| $136.79 B by 2035 | long-horizon house, different methodology |
| APAC: **$2 282.9 M (2025), 28.1 % CAGR 2026–2033** | Grand View |

🔴 **Three houses give three different 2026 values for the same market, spanning ~19 %.** 🔵 **So the
honest client sentence is the band, not the point:** *"independent houses put 2026 between roughly
**$9.6 B and $11.4 B**, with CAGRs from **26 % to 41 %**."* 🔴 **A proposal quoting one figure to two
decimals is quoting a methodology it has not read.**

## Opportunities by region — superseded (the live block is at the top of this file)

### North America

🟢 **The posture: regulation is dense, state-level, and now MANDATES work this shelf can do.**
🔴 **134 AI-in-education bills across 31 states** in the 2026 session; **33–35 state education
departments plus Puerto Rico** publish official AI guidance. 🔵 **The buying trigger is a deadline,
not a vision:** **Ohio and Tennessee require districts to write their own AI policies** (Ohio's
deadline **2026-07-01**, now past), which is a per-district compliance artefact at scale.
🟢 **Hard prohibitions to design around, not sell past:** **California AB 1159** bars using student
data to train models; **Idaho SB 1227** mandates privacy protections; **Oklahoma and Maryland**
require human oversight and ban AI from high-stakes student decisions; **New York City** prohibits AI
for grading, discipline, promotion/graduation and IEP/504 development, with a reported student-facing
moratorium through grade eight. 🔴 **FERPA is the baseline on every row in `agents/top.md`.**
🟢 **The fit:** the four Canvas side-cars plus this pass's Moodle rows are **read-scoped by
configuration** — `canvas-mcp`'s withheld-tool design (pass 64) is the single most sellable control
in this KB against the NYC/Oklahoma/Maryland prohibition shape.
🟡 **Federal is slower and should not anchor a proposal:** the Department of Education's AI
grant-priority rule was finalised **2026-04-13**; **H.R. 8747** (K-12 AI Literacy) is **in committee
only**.

### EMEA

🟢 **The posture: one regime, a known date, and a window that is open right now.**
🔴 **Annex III** makes education high-risk where a system determines access or admission, evaluates
learning outcomes, steers an educational path, or monitors behaviour in proctoring. 🟢 **Obligations
land `2027-12-02`** (two channels, above) — 🔵 **which is the opportunity, not relief:** ~14 months to
build conformity in, versus retrofitting it. 🟢 **Article 4 AI-literacy duty is already in force**,
and **public schools owe a FRIA as deployers** under Art. 27 while private providers do not — a
distinction that changes who buys.
🟢 **The component fit is the best of any region:** **OpenOLAT (Apache-2.0)** 🆕 is a university-grade
LMS a closed derivative may build on; **`educredentials/ec-issuer`** is EMEA-placed (SURF, NL) and
speaks the **European Learner Model**; **credential-lens (MIT)** 🆕 verifies OB 3.0 offline, with
**zero dependencies** — 🔵 which is exactly the supply-chain story a European procurement asks for.
🔴 **The blocker is `Gap 294`:** the credential **issuer** edge has no provable permissive grant, and
ELM/OB 3.0 issuance is the EMEA-specific demand. 🟢 **One email to `ec-issuer` remains the
highest-value hour on this shelf.**
🟡 **Named supervisors** (reported, unverified list): Germany **Bundesnetzagentur**, France **CNIL**
on fundamental rights, Spain **AESIA**. 🟢 **Also in frame:** Digital Education Action Plan,
Convention 108+.

### APAC

🟢 **The posture: no single regime — the region is a compliance MATRIX, and that is the service.**
🔴 **Korea's AI Basic Act is in force from January 2026** and names **education** a *high-impact*
sector: disclosure that the user is interacting with AI, and **a local representative for foreign
providers** — 🔵 a market-entry obligation, not just a product one. 🔴 **Vietnam** enacted
**Law No. 134/2025/QH15** (2026-03-01) with **Decree 142/2026/ND-CP** naming education high-risk and
requiring providers to **self-classify** into one of three tiers before deployment.
🟡 **India** is light-touch (MeitY under the IT rules), with synthetic-content due diligence from
**`2026-02-20`**. 🟢 **China** enforces algorithm filings, synthetic-content labelling and security
review for public models. 🟡 **Singapore** governs by framework and toolkit (**AI Verify**) and leads
the ASEAN AI governance working group; **Japan and Taiwan** are drafting while standing up testing
institutes; **Australia/New Zealand** are light-touch — and 🔴 **ANZ records the region's
*highest* public support for banning AI in schools**, which is a sales-cycle fact.
🔴 **Least developed frameworks: Laos, Myanmar, Brunei, Cambodia, Timor-Leste.** The **Philippines**
plans a regional framework under its **2026 ASEAN chairmanship**.
🟢 **The fit:** `LangGraph` policy-node per jurisdiction (pattern P6, earlier pass) is the right
shape; 🔵 **and `policy-matrix.tsv` is the asset** — a (function × jurisdiction) verdict table is
precisely what a multi-country APAC engagement cannot assemble in a sprint.
🔴 **Readiness is uneven in infrastructure, not just policy** (UNESCO): connectivity and teacher
training gate deployment regardless of licence.

### LATAM

🟢 **The posture: the region's defining number is a GOVERNANCE GAP, and it is a deliverable.**
🟢 **UNESCO IESALC, 200 institutions across 19 countries: 87 % use AI in at least one area, and only
26 % have any formal framework.** 🔵 **That 61-point spread is the engagement** — the adoption
already happened and the policy did not.
🟢 **Adoption splits by sector in a way that targets a pitch:** **84 %** private non-profit,
**68 %** public, **52 %** private for-profit. 🟢 **Teachers are ahead of their institutions:** TALIS
2024 puts **Brazil, Chile, Colombia and Costa Rica at ~50 %+** against an **OECD average of 36 %**,
and **Uruguay reports 75 %** of public-school teachers (Ceibal, 2026).
🟡 **Regulation is at bill/policy stage, not in force:** **Brazil PL 2.338/2023** is in the Chamber of
Deputies (text can still change); **Chile** has a risk-based government bill; **Colombia** went
policy-first with **CONPES 4144** (Feb 2025), funded through 2030. 🔵 **So LATAM is the one region
where a framework can be designed before a statute constrains it** — the inverse of EMEA.
🟢 **Institutional anchors:** UNESCO's **Observatory on AI in Education** for the region launched
**2026-04-14** at **ECLAC, Santiago**; IESALC published with UNU-IAS at **Digital Learning Week 2026**.
🟢 **The fit:** **Kolibri (MIT)** for offline-first deployment where connectivity is the constraint,
plus **Moodle** — dominant across the region — now with **four MIT side-car options** from this pass.
🔴 **Declared gap:** the LATAM sweep returned **no commercial edtech vendor names, no national
curriculum AI mandates, and nothing education-specific for Mexico, Argentina or Peru.** 🔵 **Stated
so it is not read as coverage** — this is the thinnest vendor map of the four regions.

### 🟢 Region coverage of this pass, stated plainly

🟢 **All four regional sweeps returned relevant material. No region is an informed gap this pass** —
which has not been true in every pass, and is the reason it is written down. 🔴 **The gaps are
*within* regions**: LATAM vendors (above), APAC's five least-developed frameworks, and North
America's bill-status verification (trackers, not bill text).


## 🟢 Sixty-fourth pass, 2026-10-08 — **`Gap 293` CLOSES**: the refusal is at the proxy, the proxy says so **in its own words**, and an unimpeachable control proves it is an **allowlist** rather than a fact about policy hosts

⏱️ **Eighteenth pass of this date. Append-only: this section is new; nothing below it was rewritten.**

🟢 **Oracle map re-measured before any datum (`P713`, `P745`, `P791`), from calibration pairs:** `raw`
discriminates **four ways on one repository** — real file **200** / invented path **404** / invented
**branch** **404** / invented **repo** **404**; `pypi` **200 / 404**; `npm` **200 / 404**;
`ls-remote --symref` discriminates **and resolves the default ref**. 🔴
`api.github.com/repos/{third-party}` **403** — **no star counts** (`P745`).

### 🟢 `Gap 293` — **CLOSED**, and the closure corrects fifteen passes of band language

🔴 **`Gap 293` said: "the policy band blames hosts for a refusal that happens at the proxy."** 🟢 **It
is now measured, on a second channel, with a control that cannot be explained away.**

🟢 **Measured this pass, `n = 5`, one allow and four denies, in the same minute:**

| Host probed | Channel | Result | What it proves |
|---|---|---|---|
| `raw.githubusercontent.com` | fetch channel | 🟢 **payload returned and read** | 🟢 **the channel works** — the denies below are not an outage |
| `www.iesalc.unesco.org` | fetch channel | 🔴 **`EGRESS_BLOCKED`** — *"Access to www.iesalc.unesco.org is blocked by the network egress proxy"* | 🟢 the refusal **names its own author** |
| `digital-strategy.ec.europa.eu` | fetch channel | 🔴 **`EGRESS_BLOCKED`**, identical structure | 🟢 same, `n = 2` |
| `www.multistate.us` | fetch channel | 🔴 **`EGRESS_BLOCKED`**, identical structure | 🟢 same, `n = 3` |
| 🔴 **`en.wikipedia.org`** | fetch channel | 🔴 **`EGRESS_BLOCKED`**, identical structure | 🔴 **THE CONTROL, and it is the finding** |

🔵 **Wikipedia is the whole argument.** 🔴 **It is not a policy host, not a regulator, not a vendor
report, not rate-limiting this KB, and certainly not down.** 🟢 **It is refused with the identical
structured error.** 🔵 **Therefore the variable is the *channel's allowlist*, and not any property of
`unesco.org`, `eur-lex.europa.eu`, `ec.europa.eu`, `nasbe.org`, `multistate.us` or any other host this
file has named in a band since pass 57.**

🔴 **So this file has been writing a true sentence for a false reason.** 🟢 Passes 57–60 wrote *"6 of 6
primary policy hosts at `000`"* and concluded the policy channel was closed — **the conclusion was
right**. 🔴 **But `000` is a curl-shaped token for "no response reached me", and placing it in a column
headed by a *hostname* asserts something about that host.** 🟢 **Nothing about those hosts was ever
measured.** 🔵 **Pass 59's lesson was to `grep` before announcing a property; this is the same lesson
for an *error code*: a transport failure is a fact about the transport until something names the
author.**

🆕 **`P797` — a refusal must be attributed to the layer that issued it.** 🟢 **Write
`EGRESS_DENIED (allowlist)` and never `000` against a hostname.** 🔵 The two differ in what a later
pass may conclude: `000` invites "retry, the host may be up" and licenses a reader to doubt the source;
🟢 `EGRESS_DENIED (allowlist)` is terminal in this environment and says **the source is fine and this
environment may not read it** — which is the sentence a client-facing citation actually needs.

🟢 **Consequence for every band in this file, applied from here forward:** the primary-source channel
is **closed by configuration, not by the sources**, so every regulatory and survey figure below stays
`reported` / single-channel — 🟢 **but its *reliability* is no longer in question on account of
reachability.** 🔵 **The sources are good. This environment is fenced.** 🔴 **What remains unmeasured
is the figures themselves, and that is a different gap.**

🔴 **One claim this pass did NOT make:** no allowlist was enumerated. 🟢 Five hosts were probed and
five results recorded; 🔴 **four of five denied is not a rate** (`P744`), and nothing here says which
hosts *would* be allowed.

### 🟢 Regional intelligence, gathered this pass — band stated once, applying to every figure below

🟡 **Band (`P784`, and now `P797`):** every regulatory, adoption and market figure in this section is
🟡 **`reported`, single-channel, via the search channel's summaries** — 🔴 **because every primary host
is `EGRESS_DENIED (allowlist)`, measured above.** 🟢 **Every repository, licence, ref and SHA cited
anywhere in this pass is payload-read.** 🔵 **The asymmetry is the shelf's standing shape:**
`intel/` is a **lead shelf**, `repos/` is an **evidence shelf**.

🔴 **Three circulating figures this pass explicitly DECLINES to carry**, because the channel itself
flagged them as unattributable: a *"$12.3B globally by 2026"* market figure attributed to HolonIQ that
the channel could not confirm against HolonIQ's own material; *"83 % of institutions plan AI teaching
assistant deployment"* attributed to EDUCAUSE with no verifiable primary link; and a *"42 %
learning-outcome improvement"*. 🟢 **Declining is an answer** (`P460`).

### 🟢 The cross-region pattern this pass found, and it is the most sellable sentence in the file

🔵 **Two regions, two different instruments, same shape: adoption has outrun believed efficacy.**

| Region | Adoption | Believed efficacy | The gap |
|---|---|---|---|
| **EMEA** | 🟡 **63 %** of teachers use AI — Sanoma Learning, **20 000+ teachers, 14 European countries** | 🔴 **16 %** believe general-purpose AI improves learning outcomes. 🔴 **3 in 4** remain concerned about risks to education quality; only **1 in 3** support student use at school | 🔴 **63 → 16** |
| **LATAM** | 🟡 **79 %** of faculty use AI in teaching — Digital Education Council | 🔴 **19 %** use it for assignment feedback; **88 %** report *minimal* to *moderate* engagement; assessment is the **weakest** area | 🔴 **79 → 19** |

🟢 **Measured by unrelated surveys, on different continents, with different questions — and the gap
runs the same direction and nearly the same width.** 🔵 **What it means commercially:** the market is
not short of AI *usage*; it is short of AI anyone believes in. 🟢 **So the sellable unit is not
"adoption" — it is *evidence*, in the specific places general-purpose chat is known to fail: feedback
on student work, assessment, and curriculum alignment.** 🔵 **It also explains the 2026 trend the
channel reports from several directions at once** — a movement away from generic chatbots toward
purpose-built education tooling (`intel/trends.md`). 🟢 **The 63-vs-16 figure is the strongest single
piece of evidence this KB holds for that thesis, and it is new this pass.**

🟡 **Method caveat kept visible, and it is a real one:** the LATAM figures in this file have been
cited from two different samples — **>30 000 respondents across 29 institutions** (already on this
shelf) and **7 319 faculty** (this pass's channel). 🔴 **These are not the same instrument and their
headline percentages must not be averaged or presented as one survey.** 🟢 **Both are recorded; neither
is reconciled**, and reconciling them needs a primary read that this environment cannot perform.

## Opportunities by region — superseded (the live block is at the top of this file)

### North America

🟡 **Adoption, `reported`:** the largest regional market — ~**36 %** of global AI-in-education spend,
**$3.68 B** in 2026 toward **$32 B** by 2030. **60 %** of US K-12 teachers used AI tools in 2024-25
and **32 %** at least weekly; teacher use roughly **doubled** year on year. **86 %** of education
organisations use generative AI 🔴 **and most lack a policy.** Weekly-using teachers report saving
**~5.9 hours/week**.

🟡 **Regulation, `reported` — the venue is the state legislature, and the volume is the point:**
**134** AI-in-education bills across **31** states this session; **30+** states now have guidance
documents. Named instruments: **California AB 1159** (would bar using student data to train AI
models), **Idaho SB 1227** (privacy protections for school AI tools), **Oklahoma** and **Maryland**
(human oversight required; AI barred from high-stakes decisions about students), **Ohio** (every
district must adopt a formal AI-use policy by **2026-07-01**), **Georgia** and **Mississippi** (AI
instruction inside CS credits). Federal: **H.R. 8747**, the *K-12 AI Literacy and Readiness Act of
2026*, cleared a House committee in July on a largely party-line vote 🔴 **and no evidence was found
that it passed the full House.** Local: 🔴 **New York City's one-year moratorium on student-facing AI
through eighth grade**, which other districts are being urged to copy.

🟢 **The opportunity, and it follows from the regulation rather than the market size:** 🔴 **a
patchwork of 31 states with 30+ non-identical guidance documents and at least one outright local
prohibition is a *compliance* market before it is a *product* market.** 🟢 **The sellable asset is a
policy-gate that answers "may this function run, in this jurisdiction, for this age band" from data** —
which is what `compose/code/p782-policy-gate/` already is. 🔵 **Ohio's hard date is the clearest
near-term wedge on this shelf: every district in one state needed an adopted policy by 2026-07-01, and
"most lack a policy" is the measured national baseline.** 🔴 **And NYC is the standing warning: the
grading and student-facing tiers of this KB's shelf are *prohibited*, not *conditioned*, in that
district — `P764`, no human-in-the-loop converts a prohibition into a condition.**

🟢 **Buildable here, payload-verified this pass:**
[`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster)
(**Apache-2.0**, `main` · `6de5476`) for OneRoster 1.2 over an Ed-Fi ODS — Ed-Fi is the North American
data-standard substrate, and this is the licence-clean bridge off it;
[`zhenghh04/canvas-mcp`](https://github.com/zhenghh04/canvas-mcp) (**MIT**, `main` · `0ef723f`) for the
instructor-side agent edge, whose three-tier capability gating is the FERPA-shaped control this region
needs; [`songsterq/gradebook-mcp`](https://github.com/songsterq/gradebook-mcp) (**MIT**, `main` ·
`27bcdaf`) for the parent-facing, read-only-by-construction pattern.

### EMEA

🟡 **Adoption, `reported`:** **63 %** of teachers across **14 European countries** use AI
(Sanoma Learning, **20 000+** respondents) 🔴 **while only 16 % believe general-purpose AI improves
learning outcomes**, **3 in 4** are concerned about quality risk, and **1 in 3** support student use.

🟡 **Regulation, `reported`, and the timeline MOVED:** the **EU AI Act** remains the anchor, with
education in **Annex III** as high-risk where a system determines access, assesses learning outcomes,
or influences an educational path — admissions screening and proctoring are the named examples. 🆕
**A digital omnibus received final Council approval on `2026-06-29`, resetting the high-risk
application dates to `2027-12-02` for stand-alone high-risk systems and `2028-08-02` for high-risk
systems embedded in regulated products.** 🔴 **The Article 4 AI-literacy obligation was NOT changed and
has applied since `2025-02-02`.** 🟢 **The AI Office and national authorities began enforcing from
`2026-08-02`.** Also in frame: **Convention 108+** on data protection, and a Council of Europe survey
finding only **4 of 23** responding member states had AI policies or regulations as of 2022.

🟢 **The opportunity:** 🔵 **the deferral is runway, not relief** — this shelf's standing phrase, and
it now has a date attached. 🔴 **The duty that is already live is the one nobody is selling against:
Article 4 AI literacy, in force since 2025-02-02, with no deferral.** 🟢 **And the 63-vs-16 gap says
what to build:** European teachers are using general-purpose AI and do not believe it works, so
*purpose-built, curriculum-aligned* tooling has an unusually well-evidenced demand case here — 🟢 **with
the compliance clock on the high-risk functions pushed to late 2027, which is exactly enough time to
build one properly.**

🟢 **Buildable here, payload-verified this pass:**
[`educredentials/ec-issuer`](https://github.com/educredentials/ec-issuer) (`main` · `8bafc99`) — 🟡
**MIT in README prose only**, 🔴 **no licence file, no manifest key, unpublished on pypi** — the only
reachable issuer that speaks the **European Learner Model**, and therefore the best-fit and
least-provable component on this shelf's new credential edge. 🟢 **Resolve its grant before quoting
it.** Fallback: [`Schroedinger-Hat/certo`](https://github.com/Schroedinger-Hat/certo) (🔴 **AGPL-3.0**,
`main` · `6fd0a11`), self-host only.

### APAC

🟡 **Regulation, `reported`, and this is the region where the law is furthest ahead of the market:**
**South Korea's AI Basic Act took effect January 2026**, naming **education** among its *high-impact*
domains, requiring that high-impact systems **allow meaningful human monitoring and intervention at any
time**; 🟢 **2026 is a limited-enforcement pilot year with a one-year grace period on penalties.**
**Vietnam's Law No. 134/2025/QH15 took effect `2026-03-01`** with **extraterritorial reach** over
foreign technology companies operating in Vietnam, and a follow-on decision names **automated
assessment and behavioural monitoring** as high-risk in education. **Taiwan** passed an AI Basic Act in
**December 2025**. **Singapore and Japan** rely on voluntary guidelines backed by existing law.
**China** has binding algorithm and generative-AI rules. **Australia** has no AI-specific statute;
its 2024 proposal paper floated mandatory guardrails for high-risk uses including education.
**Indonesia** is proposing a soft, sector-based framework naming education.

🟡 **Adoption, `reported`:** highly uneven — China and Singapore have established AI-in-education
policies while other countries are still meeting basic educational needs; UNESCO stresses that policy
without IT infrastructure, connectivity and teacher training does not land. **South Korea** delivered
~**$740 M** across 2024-2026 to train teachers on AI tools and methods. 🔵 **Public sentiment splits
inside the region:** Ipsos Education Monitor 2026 finds **lower** support for banning AI in schools
across the Asian markets examined and **higher** support in **Australia and New Zealand**.

🟢 **The opportunity:** 🔵 **Korea's grace period is a dated, closing window** — a 2026 engagement can
build the human-monitoring and intervention surface that the Act requires *before* penalties begin,
which is a far easier sale than retrofitting it in 2027. 🔴 **Vietnam's extraterritoriality means a
delivery centre outside Vietnam does not put a client outside the law**, and the two functions its
decision names — automated assessment, behavioural monitoring — are precisely this KB's
highest-exposure tiers. 🟢 **The regional asset to build is an intervention-and-audit layer:
human-in-the-loop checkpoints, a tamper-evident decision log, and per-jurisdiction function gating.**
🔵 **And the AU/NZ sentiment split is a product-boundary signal, not a market-size one** — the same
product needs a stricter default posture there.

🟢 **Buildable here, already on this shelf:** the Sunbird DPI tier —
[`project-sunbird/sunbird-lms-service`](https://github.com/project-sunbird/sunbird-lms-service) (MIT)
with [`Sunbird-Ed/SunbirdEd-portal`](https://github.com/Sunbird-Ed/SunbirdEd-portal) (MIT) — remains
the region's licence-clean public-sector LMS base.

### LATAM

🟡 **Adoption, `reported`, and it is the best-evidenced region on this shelf:** UNESCO IESALC surveyed
**200 higher-education institutions across 19 countries** and found **87 %** use AI in at least one
area of activity, teaching and learning most commonly, 🔴 **with governance frameworks and institutional
strategies explicitly failing to keep pace.** A Digital Education Council survey of **7 319 faculty**
found **79 %** use AI in teaching 🔴 **but 88 % report only minimal-to-moderate engagement**, and
🔴 **assessment is the weakest area — the lowest adoption is in exactly the assessment-related use
cases (feedback generation, integrity checking).**

🟡 **Regulation, `reported` — general AI law, not education-specific:** **Uruguay** became the first
country in the region to sign the **Council of Europe Framework Convention on AI** (2025). **Colombia**
adopted a national AI policy via **CONPES 4144** (February 2025). **Mexico** has a 2024 federal AI bill
proposing an oversight authority. 🔵 Across the region legislatures are converging on an
unacceptable / high / lower risk taxonomy. 🔴 **No binding education-specific AI rule was found.**

🟡 **Institutional landscape, `reported`:** **UNESCO launched the Observatory on AI in Education for
Latin America and the Caribbean in April 2026**, with partners including **CAF**, **CENIA** (Chile),
**ECLAC**, **Fundación Ceibal** (Uruguay), **Tecnológico de Monterrey**, and **Fundación Santillana /
ProFuturo**. UNESCO has run AI ethics and regulation training for officials in **Ecuador** and
**Chile**. At **Digital Learning Week 2026 (8–11 September)**, **25+** education ministers adopted a
joint statement that education must remain a human right and common good in the AI era.

🟢 **The opportunity, and it is the sharpest in this file because the gap is *named by the surveys
themselves*:** 🔴 **87 % institutional adoption with governance that lags, and 79 % faculty use with
assessment as the weakest area.** 🟢 **Those are two halves of one sale:** the **governance layer** the
institutions do not have, wrapped around the **assessment function** the faculty are not using. 🔵 **A
proposal that leads with "AI adoption" here is selling something 87 % of the market already bought.**
🟢 **A proposal that leads with *governed assessment* — feedback generation and integrity checking with
an auditable policy gate — is selling the two things measured absent.** 🔵 **And the Observatory's
partner list is the distribution channel**: CENIA, Ceibal and Tec de Monterrey are institutional
anchors, not just names.

🟢 **Buildable here, already on this shelf:** the `latam-gpt` evaluation tier —
[`latam-gpt/lm-evaluation-harness`](https://github.com/latam-gpt/lm-evaluation-harness) (**MIT**,
`main` · `9fa381a`) and [`latam-gpt/syco-bench`](https://github.com/latam-gpt/syco-bench) (🟢
**`MIT-0`**, `main` · `5ecc005` — **re-confirmed on a second channel this pass: payload first line
*"MIT No Attribution"*, ~895–903 B**), plus
[`eduagarcia/lm-evaluation-harness-pt`](https://github.com/eduagarcia/lm-evaluation-harness-pt)
(`ab24923`) for Portuguese. 🔵 **A regional evaluation harness is what turns "governed assessment" from
a slide into a deliverable.**

### Global

🟡 **Market size, `reported`, and the estimates disagree:** **$10.6 B in 2026 → $42.48 B by 2030 at a
41.5 % CAGR** (Research and Markets) is the figure this shelf already carries and the one with a named
publisher. 🔴 **Competing figures circulate and are declined above.** 🟢 **Treat the CAGR as
directional and never as a forecast quoted to a client without its publisher attached.**

🟡 **The structural trend, `reported` from several independent directions:** 2026 is the year AI in
education moves **from experimentation to governance** (1EdTech), with clear policies, data boundaries
and oversight as the condition of adoption — and with **digital credentials becoming a core mechanism
for skills-based learning and hiring.** 🔵 **That last clause is why this pass opened the
credential-issuance edge in `verticals/solutions.md`** — 🔴 **and why its finding matters: the edge
1EdTech puts at the centre of 2026 is the one edge on this shelf with no permissive, file-grant
implementation.**


## 🟢 Sixty-third pass, 2026-10-08 — **all four regional queries returned education-specific material** (pass 62 had two empty), and the band line itself was measured wrong: the policy channel is blocked **at the proxy**, not at the hosts

⏱️ **Seventeenth pass of this date. Append-only: this section is new; nothing below it was rewritten.**
🟢 **Per the convention, pass 62's `## Opportunities by region` heading is retitled *superseded*; the live block is below.**

🟢 **Oracle map re-measured before any datum (`P713`, `P745`), `n = 2`:** `raw` **200** against a
404-discriminating control (real file 200 / invented 404 / **invented *branch* 404**), `pypi`
**200 × 2**, `npm` **200 × 2**, `maven` **200 × 2**, `packagist` **200 × 2 against its own
calibration pair**, `api.nuget.org` **200 × 2**, `ls-remote` discriminates **and resolves the
default ref**. 🔴 `api.github.com/repos/{third-party}` **403 × 2** — **no star counts** (`P745`).

### 🔴 The band, corrected — and the correction is the same defect as the oracle-map line this pass refutes

🔴 **Policy and report hosts: `000`, 8 of 8** — `www.unesco.org`, `www.iesalc.unesco.org`,
`www.digitaleducationcouncil.com`, `www.worldbank.org`, `www.multistate.us`, `dig.watch`,
`www.lw.com`, `www.1edtech.org`. 🟢 **Twice the denominator pass 62 used, same verdict.**

🔴 **But pass 62 wrote it as "policy and report hosts are `000`"** — a statement about the
**hosts**. 🟢 **What the wire says, on two independent channels, is narrower and different:**

| Channel | What it returned | What it licenses you to say |
|---|---|---|
| `curl` | `CONNECT tunnel failed, response 403`, 8 of 8 hosts × 2 | the **egress proxy** refused the tunnel |
| `WebFetch` | `EGRESS_BLOCKED`, naming the domain | the **egress proxy** refused the fetch |

🔵 **No request reached any of those eight hosts, so nothing was measured about any of them.**
🔵 **This is `P791` in a second place:** a code produced by an **intermediary** is not a fact about
the **endpoint**, exactly as a code produced by a **target id** is not a fact about the **host**.
🟡 **The practical band is unchanged — every regulatory and survey figure below is `reported`,
single-channel, per `P784`** — 🟢 but the reason is now correct, and it is a reason that will not
change when a host comes back up.

🟢 **Every repo, licence, ref and registry date in this pass is payload-read.**

### 🟢 The regional channel recovered — 4 of 4 returned education-specific material

🔴 **Pass 62 recorded two of four regional queries returning nothing about education at all.**
🟢 **This pass all four returned education-specific regulation, adoption figures and named
programmes.** 🔵 So `P785` holds and is worth restating: *"this channel is saturated" is the most
expensive conclusion a pass can record* — the regional channel was not saturated, it was quiet for
one window.

🟢 **And the EMEA channel defect did not recur.** 🔴 Pass 59 recorded one query serving the
**superseded `2026-08-02`** Annex III date. 🟢 This pass the channel served the **current**
position: Annex III high-risk obligations **postponed to `2027-12-02`** under the Digital Omnibus,
Council final green light **`2026-06-29`**, 🟡 **still awaiting Official Journal publication** —
which is why the date is `reported` and carries a conditional, not a deadline.

## Opportunities by region — superseded (the live block is at the top of this file)

🔵 **Framing, per `P790`/`P769`: each opportunity names a protocol or a function, never a brand.**
🔵 **Every component named below is a row this shelf has payload-read at a pinned ref.**

### North America

🟡 **What the market is doing (`reported`, single-channel):** two trackers disagree on the
denominator — **134 bills across 31 states** in the 2026 session on one count, **68 across 27** on
another, 🔵 **and the disagreement is the finding: the category is defined differently, so neither
number is a rate.** 🟢 **What both agree on is the shape:** guidance outruns statute —
**33–35 state departments of education plus Puerto Rico** publish official AI guidance, while
`OH HB 96` and `TN SB 1711` push the obligation down to districts to write their own policy.

🟡 **The binding constraints, named:** `CA AB 1159` prohibits using student data to train AI
models; `ID SB 1227` requires privacy protections for AI tools in schools; **Oklahoma and Maryland
require human oversight and bar AI from high-stakes decisions about students**; `MD SB 720`
requires the state to offer teachers AI professional development; `AL HB 329` makes an approved CS
course that includes AI instruction a graduation requirement. 🟡 Federally, the Education
Department finalised a rule prioritising grants for projects on AI understanding and ethical use,
and `H.R. 8747` (K-12 AI Literacy and Readiness Act) advanced in committee in July 2026.

🔴 **The constraint that decides the product, and it is this shelf's `P764`:** NYC's guidance of
**2026-03-24** puts grading, promotion, discipline, advising, crisis intervention, IEP/504
assembly and academic placement in the **red** tier — **a prohibition, not a condition.**
🔴 **No amount of human-in-the-loop converts a prohibited use into a permitted one**, so in US
public K-12 **the grading pipeline is not the product**; the green teacher-facing tier is.

🟢 **Where the engagement lands:** the **district-policy obligation** created by `OH HB 96` and
`TN SB 1711` is a build, not a memo — a per-district policy register wired to the function-level
red/yellow/green classification this shelf already encodes, with `CA AB 1159`'s training-data
prohibition expressed as a **data-flow** constraint rather than a clause. 🟢 The permissive
substrate exists: **Ed-Fi Data Standard v6** (`Ed-Fi-Alliance-OSS/Ed-Fi-ODS`,
`-ODS-Docker`, `-API-Publisher`, Apache-2.0 at pinned refs) is the US student-record layer, and
**`grantholle/powerschool-api`** is a payload-read **MIT** PHP client for the dominant SIS,
package `grantholle/powerschool-api` **v4.5, 2026-03-18** — 🟢 re-measured this pass at its real
default ref `main` (`f54e292`), manifest and licence file agreeing on MIT.

🔴 **Declared gap, and it is a gap in the *region*, not in the shelf:** **nothing on Canada or
Mexico returned.** 🔵 "North America" in this pass's evidence means the United States. 🟢 A Canadian
or Mexican engagement is **not** served by the rows above, and saying so costs one line while
pretending otherwise costs a proposal.

### EMEA

🟡 **The regulatory shape (`reported`, single-channel):** the AI Act's **Annex III** makes
education high-risk for four named functions — determining **access or admission**, **assigning**
people to institutions, **evaluating learning outcomes where those outcomes steer the learning
process**, and **monitoring prohibited behaviour during tests**. 🔴 **Emotion recognition in
education institutions is prohibited outright** (from `2025-02-02`, medical/safety exception
aside). 🟡 **Article 4** AI-literacy duties on staff have been in force since February 2025 and
supervision and enforcement rules apply from **August 2026**; 🟡 **Annex III high-risk obligations
are postponed to `2027-12-02`** under the Digital Omnibus (Council green light `2026-06-29`,
awaiting OJ publication). 🟡 Public schools additionally owe an **Article 27 Fundamental Rights
Impact Assessment**.

🔵 **Read as engineering, that list is a specification, which is what `P710` already knows how to
build:** four conditioned functions, one prohibited function, one assessment artefact, and a
literacy obligation with a date already past. 🔵 **The `2027-12-02` shift is not relief** — it moves
the conformity deadline, not the Article 4 duty or the emotion-recognition ban.

🟢 **Where the engagement lands:** the **assessment** edge, because it is the one Annex III
conditions and the one this shelf can now build permissively on both sides.
🆕 **Measured this pass: the QTI 3 layer splits by licence.** `oat-sa/qti-sdk` is **GPL-2.0-only**
(manifest, `master`) — 🔴 it cannot sit inside a client deliverable — while
**`Kennisnet/php-qti3`** is **MIT** on both layers, package `wikiwijs/php-qti3` **v0.7.0,
2026-09-22**, default ref `main` (`0ba4f78`), 🟢 **the freshest permissive assessment component on
this shelf.** 🟢 Beside it, `LongsightGroup/qti3` (MIT) authors and banks items and
`amp-up-io/qti3-item-player` (MIT) delivers them. 🔵 **So "evaluate learning outcomes" can be built
with a permissive chain end to end, and the `-only` copyleft is avoidable rather than merely
disclosed.**

🟡 **Named programmes and players (`reported`):** a Commission/OECD draft **AI Literacy Framework**
for primary and secondary education, G7-endorsed; **AI-ENTR4YOUTH** running applied AI student
projects in **10 European countries** over three years, coordinated by JA Europe with Intel and
Commission support; vendor lists that recur include Kahoot!, Sanoma Learning, Century Tech,
Pearson and Bridge-U alongside the hyperscalers. 🟡 **Teacher readiness, not procurement, is the
reported bottleneck**, and education policy stays national while the Act is union-wide.

### APAC

🟡 **The region has no single framework, and that is the engineering fact (`reported`):**

| Jurisdiction | Instrument | Status as reported | What it binds |
|---|---|---|---|
| South Korea | **AI Basic Act** | in force **2026-01-22**; MSIT pilot year, one-year penalty grace | AI-generated content must be **labelled** so origin is recognisable |
| Vietnam | **Law on Artificial Intelligence** | passed **2025-12-10**, effective **2026-03-01** | education among **six high-risk sectors**, naming **automated assessment** and **behavioural monitoring** |
| Taiwan | **AI Basic Act** | passed December 2025 | framework |
| China | algorithm, deep-synthesis and generative-AI rules | enforced | binding, at the strict end |
| Singapore · Japan | voluntary guidelines over existing law | in force | guidance, not statute |
| Australia | AI Safety Institute (Nov 2025) · National AI Plan (Dec 2025) | established | institutional |

🔴 **So a regional platform crosses at least three incompatible regimes**, and
🔵 **Vietnam's wording matters most to this shelf: it names exactly the function the EU
conditions and NYC prohibits.** 🟢 **Three jurisdictions, three postures, one function** — which is
why the policy layer belongs in a **per-jurisdiction policy node** rather than in a config flag.
🟢 Korea's labelling duty is the cheapest of the three to satisfy and the only one that is a
**provenance** requirement: it wants a marking on the artefact, which is the shape
`compose/code/aiact-50-2-marking/` already emits.

🟡 **Players (single vendor report, no second channel):** Google, Microsoft, IBM, Pearson and
Byju's named for the APAC AI-in-education market, with China, India and Japan reported as
dominating it and China credited with the heaviest state backing.

🔴 **Declared gap:** **no dedicated APAC report on school or university AI adoption returned** —
the regulatory channel answered well and the adoption channel did not. 🔵 So the regimes above are
placed and the **adoption rates are not**; an APAC engagement can be scoped against regulation
this pass but not sized against uptake.

### LATAM

🟢 **This is the region with the strongest *measured* numbers this pass — and every one of them is
`reported`, single-channel, because all four report hosts were refused at the proxy.**

| Figure | As reported | Source channel |
|---|---|---|
| **87%** of institutions use AI in **at least one** area · **26%** have a formal AI strategy | 200 institutions, **19 countries** | UNESCO IESALC + UNU-IAS |
| **92%** of students · **79%** of faculty actively engaging with AI | **>30 000** responses, **29** institutions | Digital Education Council LATAM 2026 |
| **53%** of school administrators use AI · **22%** report school guidelines | Brazil | Cetic.br, 2026 |
| **75%** usage in high socio-economic class vs **42%** in low | Argentina | Kids Online Argentina, 2025 |

🔴 **The 87 / 26 pair is the whole opportunity in two numbers:** adoption is near-universal and
**governance is absent in three institutions out of four.** 🔵 The gap between them is not a
training problem, it is an **artefact** problem — a policy register, a function-level
classification, and a record of which system touched which decision.

🟢 **Named programmes and players:** the **UNESCO Observatory on AI in Education for Latin America
and the Caribbean**, launched **14 April** with a **2026–2029** roadmap; UNESCO–**CENIA** (Chile)
on AI literacy; a **Tecnológico de Monterrey**–UNESCO agreement (March 2026); **Nvidia AI Week
LATAM 2026** extending to Mexico and Chile beside Colombia, hosted at universities rather than at
trade venues. 🟡 **In Peru**, a World-Bank-documented programme with **uDocz, Anthropic and
Microsoft** reached **85 public schools and ~4 500 fifth-year secondary students in Lima since
March 2026**.

🟡 **Regulation, and it is converging on precisely this shelf's constraint:** Brazil's bill is
reported as the region's most developed and is modelled on the EU Act with tiered risk and civil
liability; Chile's draft is built on transparency, fairness and human oversight; 🔴 **Peru's draft
would classify educational admissions and student evaluations as high-risk** — the Annex III
functions again, a third continent; Colombia and Paraguay have proposals naming education;
Argentina has momentum and no formal law.

🟢 **Where the engagement lands, and LATAM is the one region where the *substrate* is local:**
**`portabilis/i-educar`** is Brazil's municipal school system, and this pass re-measured it at its
**real** default ref — 🔴 **not `master`:** `ls-remote --symref` resolves `refs/heads/2.12`
(`cd1da68`), and `raw` only served `master` because `master` is a **pseudo-ref** for the default
(`P793`). 🔴 **Its licence lands copyleft on both layers but not the same copyleft:** the licence
file at `2.12` is bare **GPL-2.0** ("Version 2, June 1991") while `composer.json` declares
**`GPL-2.0-or-later`**. 🔵 **The `-or-later` exists only in the manifest**, and it is the difference
between a substrate frozen at v2 and one that can be combined forward — so the integration
boundary has to be read from the manifest layer, not from the file.

🟢 **So the LATAM shape is: a copyleft local substrate, a permissive edge, and a governance
artefact that three institutions in four do not have.** 🔵 Globant's deliverable sits on the edge
and in the artefact, never inside the substrate — which is `P747a`, now with a Brazilian instance.

🟢 **And the regional model is NOT a gap — this shelf already holds two of its repositories, and
re-measuring them this pass turned up a label that is wrong.** 🔵 **The `latam-gpt` GitHub org
resolves**, and `agents/top.md` has carried two rows from it since pass 60:

| Repository | Default ref · HEAD | Licence payload, re-read this pass | Shelf label |
|---|---|---|---|
| [`latam-gpt/lm-evaluation-harness`](https://github.com/latam-gpt/lm-evaluation-harness) | `main` · **`9fa381a`** | 🟢 `LICENSE.md`, 1 067 B, *"MIT License"* | 🟢 **MIT — correct** |
| [`latam-gpt/syco-bench`](https://github.com/latam-gpt/syco-bench) | `main` · **`5ecc005`** | 🔴 `LICENSE`, 903 B, *"**MIT No Attribution**"* | 🔴 **recorded as "MIT" — it is `MIT-0`** |

🟢 **Both cited SHAs match the oracle exactly**, so the provenance was right and only the licence
*name* was wrong. 🔵 **`MIT-0` is *more* permissive than MIT, not less** — it drops the attribution
condition — 🔴 **so the correction creates no exposure and still has to be made**, because a KB
whose licence column is approximate cannot be used as a pre-flight (`P443`'s lesson about
spellings, applied to licence identifiers).

🔴 **What genuinely did not resolve is a *model* repository.** 🔵 Three conjectured slugs were tried
against `ls-remote` and none resolved, 🔴 **and per `P253` that is a fact about the three guesses,
not about the project.** 🔵 **Bounded remedy: resolve it from the org's own repository listing or
from the Observatory's payload (`P780`), not from more spellings** — and note that the two rows
above were found by **grepping this shelf**, which is the cheaper channel and the one pass 59
already told this KB to try first.

### Global

🟢 **One opportunity is genuinely cross-regional, and this pass is the reason it can be stated:
the *same function* is now regulated on three continents, and the regimes disagree.**

| Function | EU | Vietnam | Peru (draft) | South Korea | NYC public K-12 |
|---|---|---|---|---|---|
| **automated assessment / scoring** | 🟡 **conditioned** (Annex III) | 🟡 **conditioned** (high-risk sector) | 🟡 **conditioned** (`reported`) | 🟡 **labelling** | 🔴 **PROHIBITED** |
| **admissions / placement** | 🟡 conditioned | 🟡 conditioned | 🟡 conditioned | 🟡 labelling | 🔴 **PROHIBITED** |
| **affect / emotion inference** | 🔴 **PROHIBITED** since `2025-02-02` | — | — | — | 🔴 red tier |
| **teacher-facing draft generation** | 🟢 clear | 🟢 clear | 🟢 clear | 🟡 labelling | 🟢 **green tier** |

🔵 **Read across the rows and the product is already decided:** the **bottom** row is clear
everywhere this pass measured, and every row above it is conditioned somewhere and prohibited
somewhere. 🟢 **So the globally deployable artefact is the teacher-facing draft plus the record of
who decided what** — and the per-jurisdiction difference is a **policy node in the control flow**,
not a feature flag (`R63a`).

🟢 **The permissive chain that implements it is global too**, because none of it is
jurisdiction-specific: **LTI 1.3** launch (Apache-2.0), **QTI 3** authoring and delivery
(MIT throughout, freshest release `2026-09-22`), **xAPI** records (MIT), **Open Badges 3.0 / W3C
VC** credentials (BSD-3-Clause + MIT), with the copyleft LMS substrate left untouched (`P747a`).
🔴 **The one edge that is globally missing is analytics** — `Gap 284`, whose only reachable
implementation is `proprietary` in two layers of three and nine years stale.

🟡 **The one global *market* number this pass can place, and it is placed loosely:** reports put AI
in education at **USD ~10.6B in 2026** rising to **~USD 42.5B by 2030** on one publisher's figures,
with other publishers giving materially different totals. 🔴 **`reported`, single-channel, and the
publishers disagree by more than the growth they project**, so it is a direction and not a number.
🔵 **The adoption figures are the better global signal:** on the surveys above, student and faculty
use is already near-universal while formal institutional strategy sits around a quarter —
🔵 **the gap between use and governance is the engagement, in every region this pass measured.**

## 🟢 Sixty-second pass, 2026-10-08 — **two of the four regional queries returned nothing about education at all**, and that is written down; LATAM returned the figures `Gap 242` has been asking for since pass 44

⏱️ **Sixteenth pass of this date. Append-only: this section is new; nothing below it was rewritten.**
🟢 **Per the convention, pass 61's `## Opportunities by region` heading is retitled *superseded*; the live block is below.**
🟡 **Band, stated once and applying to every regulatory and survey sentence in this section:** 🔴 policy and report hosts are **`000`, 4 of 4** this pass — `unu.edu`, `www.digitaleducationcouncil.com`, `ess.iesalc.unesco.org`, `www.ed-fi.org` — so every figure below is **`reported`, single-channel**, per `P784`. 🟢 **Every repo, licence and ref is payload-read.**

> 🔵 **Opening hypothesis: that pass 61's refutation of saturation would repeat, and all four
> regional queries would again yield named instruments. 🟡 HALF REFUTED, and the half that failed
> failed in a way worth more than a yield.** 🔴 **EMEA and APAC returned *enterprise* AI content
> with no education sector in it at all** — not thin education data, *no* education data. 🟢 **LATAM
> returned the primary-source figures `Gap 242` named as its remedy.**

### 🔴 The two empty channels, named explicitly so silence is not read as coverage

🔴 **`AI education EMEA 2026 adoption regulation players`** returned CompTIA's EMEA IT outlook,
a **2023** Workday study, a Bandwidth/Cavell enterprise report and a Google Cloud EMEA engineering
lead. 🔴 **No school, university, ministry, edtech vendor or education regulator appears in the
result set.** 🔴 **`AI education APAC 2026 adoption regulation players`** returned APAC enterprise
tech priorities, Singapore's **financial-sector** AI consultations, an OpenAI ANZ policy hire and a
OneTrust governance survey. 🔴 **No education ministry, no school policy, no national AI-in-schools
programme.**

🟢 **This is a property of the query, not of the regions** — and this KB can prove it, because it
already holds APAC school-sector instruments from earlier passes (**PH DepEd Order 003 s. 2026**,
**CHED CMO 21 s. 2026**, **SG MOE Student Learning Space**, **VN decree 142/2026/ND-CP**). 🆕
**`P790`: the four-region query template mixes an industry term with a region term, and `P769`
already established that the industry term is the part that fails.** 🔵 **The remedy is the one
this KB found two months ago on the repo channel: name the *function* or the *instrument*, not the
industry.** 🟢 **Demonstrated in the same pass** — a targeted re-query of the EMEA channel
(`EU AI Act high-risk education`, `micro-credentials Europass`) returned the richest EMEA
regulatory and demand material of the last four passes, in the `### EMEA` block below.

### 🟢 `Gap 242` ADVANCES — the IESALC figures are quoted for the first time, and the contradiction it was opened for narrows

🔵 **What the gap said.** Pass 44: the UNESCO IESALC + UNU-IAS working paper is *"located and named,
**NOT read** — no figure from it is quoted anywhere this pass"*, so the Digital Education Council's
regional ordering stays unusable in a pitch.

🟢 **Quoted now, from a frame whose sampling is stated:** **200 higher-education institutions across
19 countries**, fielded **August–October 2025**. 🟢 **Adoption by area:** teaching and learning
**73.5 %**, research **57.0 %**, administration **34.1 %**, community engagement **20.0 %**.
🟢 **By sector:** private non-profit **84 %**, public **68 %**, private for-profit **52 %**.
🔴 **And the figure that matters commercially: 87 % use AI somewhere, 26 % have any formal AI
framework.**

🔴 **Still open, and the reason is the channel, not the search:** `unu.edu` and
`ess.iesalc.unesco.org` are both **`000`**, so this is a search-backend summary of the paper, not a
read of it. 🟡 **And a second figure contradicts it at the margin** — a Tec de Monterrey-linked
source says **30 %** of LATAM universities have published AI policies against IESALC's **26 %**,
which is the same definitional looseness `Gap 242` was opened about. 🟡 **So the gap narrows from
"no figure" to "figures from one channel, with one unresolved variant"** and stays open.

## Opportunities by region — superseded (the live block is at the top of this file)

### North America

🟢 **The placed, payload-read opportunity this pass is `Ed-Fi`, and it is specifically North
American:** the **US K-12 student-record standard**, five repos, **all Apache-2.0**, read at pinned
refs (`repos/foundations.md`). 🔵 **It is the only edge on this shelf whose adopters are *state
education agencies*** — which makes it a public-procurement motion, not a campus-by-campus one.
🔴 **And the constraint is measured: there is no public first-party package surface** — the
Alliance's own `.nuspec` names `EdFi.OdsApi.Sdk` and that id is absent from the reachable registry,
`api.github.com` is 403 and `ed-fi.org` is 000 (🆕 **`Gap 286`**). 🟢 **Quote it as a
source-and-installer build from `Ed-Fi-ODS-Docker`, not a package pull.**

🟢 **The credential stack is also North American in origin** — `digitalcredentials/*`, the MIT-hosted
Digital Credentials Consortium, **four MIT and one BSD-3-Clause**, payload-read. 🔵 So a US or
Canadian engagement can take both the record substrate and the credential edge from permissive,
US-originated code.

🟡 **Market and adoption, `reported`:** North America **~$951 M (2024) → ~$2 303 M (2029), 15.9 %
CAGR**; **36 %** of regional adoption share. 🔴 **~10 % of institutions have formal AI guidelines**
and **71 % of US teachers lack AI training** — the same governance deficit LATAM shows, in a
wealthier market. 🟡 Named: **IBM, Microsoft, Google**; an **OpenAI** country-level education
programme with **8 national partners (Q1 2026)**; **Carnegie Mellon + Gates Foundation, $55 M** for
AI courseware in gateway college courses.
🔴 **One figure refused:** a **"$169 M for responsible AI in higher education, Q1 2026"** claim whose
source **does not name the government** — unusable in a pitch (`P476`), recorded so a later pass
does not launder it.

🟡 **Regulation is a vacuum with a patchwork over it:** no federal equivalent of a product
regulator for educational technology, adoption decided school-by-school and district-by-district,
with **Colorado** and **Texas** named as introducing piecemeal requirements. 🔵 **Commercial
consequence: in North America the binding constraint is procurement and institutional policy, not
statute** — the inverse of EMEA, and it changes who the buyer is in the room.

### EMEA

🟢 **The strongest regional finding of the pass, and it is a demand signal that lines up with a
permissive stack found in the same hour.** 🟡 `reported`: the **2022 Council Recommendation on a
European approach to micro-credentials** is the policy base, and **European Digital Credentials for
Learning (EDC)** is described as *a central product of Europass* — issuing qualifications,
certificates and micro-credentials in tamper-resistant, EU-comparable digital form. 🟡 Named
alongside it: **ELM v3**, **ESCO** competence alignment for EQF portability, and **EBSI**-compliant
credential infrastructure in the **Erasmus+ MCEU** pilot. 🟡 In practice: the **University of
Padua** issues Europass digital credentials into a Europass wallet after professional-development
courses; 🔴 a German Higher Education Forum analysis reports that **providers still struggle with
the issuing process**.

🔵 **That last sentence is the opportunity, stated plainly: the policy mandates the credential, the
standard exists, and the issuing step is where institutions are failing** — and this pass put four
permissive implementations of exactly that step on the shelf (`digitalcredentials/vc` BSD-3-Clause,
`verifier-core` MIT, `issuer-coordinator` MIT, `1EdTech/openbadges-validator-core` Apache-2.0).
🔴 **The one thing this KB cannot yet say is whether issuing a credential is a gated function
anywhere** — `p782` has no `credential_issuance` row in any jurisdiction (🆕 **`Gap 289`**), and
`NO ROW` is not a permission (`P476`).

🟢 **Regulatory position, re-corroborated and unchanged** — recorded as corroboration, not news,
because this KB already holds it: **Reg. (EU) 2026/1744 (*Digital Omnibus on AI*)**, Parliament
**2026-06-16**, Council **2026-06-29**, in force **2026-07-27**, moving **Annex III stand-alone
high-risk — education access, assessment and exam proctoring named explicitly — from 2026-08-02 to
2027-12-02**, and Annex I embedded to **2028-08-02**. 🟢 **Article 50 transparency did not move and
is live since 2026-08-02.** 🟢 **Article 5 prohibitions are live since 2025-02-02, and emotion
recognition in an education institution is among them.** 🔴 **Primary text still unverifiable:
`eur-lex.europa.eu` → `000`.** 🔵 **The deferral is runway, not relief** — one source this pass puts
it at roughly **17 months** from the June 2026 vote.

### APAC

🔴 **The mandated regional query returned no education-sector content whatsoever this week** — see
the named-channel finding above. 🟢 **The school-sector instruments this KB relies on for APAC are
from earlier passes and are unchanged**: **PH DepEd Order 003 s. 2026** and **CHED CMO 21 s. 2026**
(AI is *supplementary*, not a replacement for teachers), **SG MOE Student Learning Space**
(Primary 4 AI tools **teacher-supervised**, reached through the SLS), **VN decree 142/2026/ND-CP**
(grading **gated**). 🔴 **Nothing new was measured about them this pass, and nothing is asserted
about them as if it had been.**

🟡 **What the channel did return is the *corporate upskilling* market, not the school sector** —
and it is worth separating rather than discarding: a **TCS–Pearson** multi-year AI learning alliance
aimed at employer skills gaps; **LearnUpon** opening a Sydney HQ with `Create+` AI course authoring;
**Alteryx** relaunching its Academy with personalised AI learning paths and credentials; **NIIT MTS**
on Training Industry's Top 20 custom content developers for 2026. 🔵 **Three of those four are
credentialing or authoring plays**, which is the same edge the EMEA block names — so the
credential layer is the one axis with a signal in two regions this pass.

🟡 **Adoption constraints, `reported` and enterprise-wide rather than education-specific:** **49 %**
of APAC businesses cite insufficient infrastructure for real-time data processing as an AI barrier;
**87 %** of organisations encourage AI-agent use while only **47 %** have governance and controls
for them. 🟡 Regulators are described as converging on shared principles applied locally, with
success tied to tuning for **local data, language and social context** — 🔵 which for this shelf is
an argument for the `P736` architecture (build beside the substrate, speak the protocol) over a
single regional product.

### LATAM

🟢 **The richest channel of the pass, and the one that advanced a gap.** 🟡 `reported`, from the
**UNESCO IESALC + UNU-IAS** mapping of **200 institutions across 19 countries** (fielded Aug–Oct
2025): adoption is **73.5 %** in teaching and learning, **57.0 %** in research, **34.1 %** in
administration, **20.0 %** in community engagement; **84 %** of private non-profit universities
versus **68 %** public and **52 %** private for-profit. 🟡 From the **Digital Education Council**
LATAM 2026 survey (**30 000+ responses, 29 institutions**): **92 %** of students and **79 %** of
faculty actively engage with AI.

🔴 **The governance deficit is the opportunity, and it is the largest measured anywhere this pass:
87 % of institutions use AI and 26 % have any formal framework.** 🔵 **So the first deliverable in
a LATAM higher-education engagement is frequently not a model — it is the institutional AI policy,
the oversight surface and the evidence trail**, and this KB can price that from artefacts it
already holds.

🟢 **The sharpest single opportunity in the data is a named function gap:** **50 % of students
support AI-assisted feedback on assignments and only 19 % of faculty use AI that way.** 🔵 **That is
a 31-point gap on one function, with demand on the student side** — and it is actionable rather
than merely interesting because this shelf has both halves: the tutoring/knowledge-tracing rows
from pass 60, and the policy gate that says what the function costs. 🔴 **The gate's warning applies
directly: assignment feedback is `assessment_grading`, which `p782` reports GATED in the EU and in
Vietnam** — so a LATAM-built feedback product is **not** portable to an EMEA engagement without the
oversight artefact, which is the `P782` design rule rather than a surprise.

🟡 **Regulation is heterogeneous, and the ranking matters for sequencing:** **Chile** is the
frontrunner with a national AI policy since **2021** and a bill under discussion; **Brazil** and
**Colombia** have national strategies with **no education-sector rules**; 🔴 **Mexico's SEP and
ANUIES have issued recommendations that are expressly non-binding.** 🟢 Instruments worth holding:
the **IDB** regulatory-framework paper for LAC, and the **ILIA index** (3rd edition, 19 countries)
for readiness, adoption and governance. 🔵 **Sequencing consequence: Chile for a
regulated-reference engagement, Mexico and Brazil where the absence of binding rules makes the
institution the whole buyer** — and in Mexico the non-binding status is a selling point for
governance work, not an obstacle to it.

### Global

🟢 **What the four regions say together and none says alone: the governance deficit is universal and
the numbers are close.** 🔴 **LATAM: 87 % use AI, 26 % have a framework. North America: ~10 % of
institutions have formal AI guidelines and 71 % of US teachers lack AI training.** 🔵 **So the
"institutions are behind their own users" finding is not a LATAM story that a North American
engagement can skip** — it is the same gap in both regions, and the artefact that closes it (an
oversight surface, a policy, an evidence trail) is the same artefact the EU's Annex III human-
oversight obligation will require from **2027-12-02**. 🟢 **Build it once, sell it in four regions.**

🟢 **The credential edge has a signal in two regions in the same pass, which no edge on this shelf
has had before**: EMEA as **public policy** (Council Recommendation 2022, European Digital
Credentials for Learning as a central Europass product, institutions failing at the *issuing* step)
and APAC as **corporate demand** (three of the four named APAC education players are credentialing
or authoring plays). 🟢 **And the implementations are North American and permissive**
(`digitalcredentials/*`, four MIT and one BSD-3-Clause, payload-read). 🔵 **A permissive US
implementation against an EU public mandate and an APAC corporate pull is the cleanest
cross-regional shape this KB has recorded.**

🔴 **The global constraint on all of it is the evidence layer, unchanged from pass 61 and not
re-measured here: 11 of 23 (48 %) of this shelf's benchmark and evaluation repos cannot go into a
paid deliverable.** 🔴 **And this pass weakened that count's floor rather than its ceiling** — the
8 "no grant at all" rows were judged by `p784` alone, which is now measured returning a false
absence (`Gap 285` / `Gap 287`).

## 🟢 Sixty-first pass, 2026-10-08 — `Gap 270` is **RE-POSED**: the regulatory shelf's problem was never the hosts, it is that this session has **one** policy channel and **zero** direct-fetch channels — and the four-region sweep **refutes `P777`'s saturation claim**

⏱️ **Fifteenth pass of this date. Append-only: this section is new; nothing below it was rewritten.**
🟢 **Per the convention, pass 60's `## Opportunities by region` heading is retitled *superseded*; the live block is below.**

> 🔵 **Opening hypothesis: that the four regional queries were saturated, as pass 60's `P777`
> concluded, and that this pass's yield would be in instruments rather than regional data.
> 🔴 REFUTED.** 🟢 **APAC and LATAM each returned named, dated regulatory instruments this KB
> does not hold** — and the EMEA date pass 60 carried as settled turns out to rest on a vote
> whose **Council adoption this pass could not confirm**.

### 🟢 `Gap 270` — **RE-POSED**, which is worth more than a fifth confirmation

🔴 **Passes 57–60 each recorded "6 of 6 primary policy hosts at `000`" and concluded the policy
shelf has no oracles.** 🟢 **The measurement was right every time. The diagnosis was incomplete**,
and this pass measured the difference:

| host | `curl -sI` | kind |
|---|---|---|
| EUR-Lex · artificialintelligenceact.eu · EC digital-strategy · UNESCO | `000` | policy |
| PH DepEd · PH CHED · SG MOE · VN gazette · IL General Assembly · Idaho Legislature | `000` | policy |
| 🔴 **`example.com` · `google.com` · `en.wikipedia.org`** | 🔴 **`000`** | 🔴 **control, unimpeachably up** |
| 🟢 `raw.githubusercontent.com` · `pypi.org` · `registry.npmjs.org` · `repo1.maven.org` | 🟢 `200` | code / registry |

🟢 **12 of 12 policy hosts at `000` — and so are three controls that are certainly reachable from
the internet at large.** 🟢 **The proxy names the mechanism itself**, from
`$HTTPS_PROXY/__agentproxy/status`: **`connect_rejected`, "gateway answered 403 to CONNECT (policy
denial or upstream failure)"**, listed per host. 🟢 **And `pypi.org` / `registry.npmjs.org` appear
literally in the proxy's own `noProxy` allowlist** — so the hosts that answer are exactly the
code-and-package hosts, by configuration.

🔴 **`WebFetch` against the same policy hosts returns `EGRESS_BLOCKED`** — the second channel is
shut too.

🆕 **`P784`, replacing `P731` as stated:** 🔴 **it is not that regulatory sources refuse this KB.
It is that this session has exactly ONE policy channel — a search backend's server-side fetch —
and ZERO direct-fetch channels.** 🟢 **Three consequences that change how every policy row must be
written:**

1. 🔴 **No policy datum here can ever be *payload-read*.** The 🟡 band on every policy row is
   permanent in this environment, not a backlog item.
2. 🔴 **No policy datum can be cross-checked against a second *independent* oracle**, because
   there is only one. 🟢 **So a 🟢 band on a policy row in this KB is a *defect*** — and that is now
   asserted in code, in `p782`'s README and matrix header.
3. 🟢 **It is a property of the *session*, like `P771`'s `[Code from External]` denial — and must be
   re-measured per environment, not inherited.** 🔵 In a session whose egress policy admits
   `eur-lex.europa.eu`, these rows become verifiable the same day.

### 🔴 `P777` — **PARTLY REFUTED**: the regional channel was not saturated

🔴 **Pass 60 concluded the four regional queries "returned nothing this KB does not already hold".**
🟢 **This pass ran the same four and they returned, in named-and-dated form:** Philippines
**DepEd Order 003 s. 2026** (basic education) and **CHED Memorandum Order 21 s. 2026** (higher
education); Vietnam's implementing decree **142/2026/ND-CP, issued 2026-04-30**, which lists
**education** among high-risk sectors and names **automated assessment** and **behavioural
monitoring**, with **three risk tiers and provider self-classification before deployment**;
Singapore **MOE**'s rule that Primary 4 AI tools be **structured, teacher-supervised and reached
through the Student Learning Space, not open platforms**; the **UNESCO Observatory on AI in
Education for Latin America and the Caribbean**, launched **2026-04-14**; a **UNESCO + CONALEP +
DGETI** centres-of-excellence pilot in Mexico, **2026-08-18**; Illinois **HB 316 → Act 964**,
law without signature **2026-06-25**, effective **2026-08-01**; Ohio's district AI-policy deadline
of **2026-07-01**; and Idaho **SB 1227**, framework reported approved **mid-August 2026**, which
**prohibits AI from replacing human teachers**.

🟢 **All of it is 🟡 reported** — `P784` says it can be nothing else here. 🔵 **The lesson is about
the *query*, not the region: `P777` generalised from four queries in one pass, and four queries is
not a sample frame.** 🆕 **`P785`: "the channel is saturated" needs a frame and a second pass
before it is written down, because it is the one conclusion that stops future work.**

### 🟢 `Gap 278` — **CLOSED**: the policy axis is now **data plus an instrument**, not prose

🟢 **`intel/policy-matrix.tsv` — 31 rows, 4 regions, 7 columns** — and
**`compose/code/p782-policy-gate/gate.sh`**, which reads it and answers *"may this **function** be
deployed in this **jurisdiction**?"*. 🟢 **21 assertions, offline, green.**

🟢 **Exit status is the verdict:** `4` PROHIBITED · `3` GATED · `5` PROPOSED · `0` clear ·
🔴 **`6` no row — which is NOT `0`.** 🔵 **That last one is the whole point of building it**: four
assertions pin that an unmeasured `(function, jurisdiction)` pair returns **"never measured"** and
not **"allowed"** (`P476`). 🟢 **And the region vocabulary fails loudly** — `--region Latam` exits
`2` with a message, rather than returning an empty set that reads exactly like *"nothing is
regulated there"*.

🟢 **The row that justifies the build (`P764`):** `bash gate.sh assessment_grading` returns
**GATED**, spanning **EU** (Annex III pt 3), **Vietnam** (decree 142/2026/ND-CP) and **Brazil**
(PROPOSED only) — for a function exposed by an **MIT** repo that clears every licence gate this KB
has ever written.

## Opportunities by region — superseded (the live block is at the top of this file)

🟡 **Band note, applying to every regulatory sentence below: `reported`, single channel, per
`P784`.** 🟢 **The repo and licence rows are payload-read.**

### North America

🟢 **The buyer is the district and the binding layer is the *state*, not the federal government.**
🟡 No federal statute located; reported **31 state education departments** had issued K-12 AI
guidance by **Jan 2026**, within **~100** K-12 AI bills this session out of **>1 500** AI bills.

🟢 **Three dated obligations that are already live, and each is a service line:**
**Ohio** required districts to *adopt an AI-use policy* by **2026-07-01** — 🔵 every district now
has a policy document, and a policy nobody can implement is a procurement waiting to happen.
**Illinois Act 964** mandates **AI literacy, grades 6–12**, effective **2026-08-01** — 🔵 curriculum
and teacher-training work, not platform work. **Maryland SB 720** requires a **non-instructional
central-office AI coordinator** per local system, with AI literacy in standards by **June 2027** —
🔴 **status contested between trackers; verify before planning.**

🔴 **The constraint to design around: Idaho SB 1227 prohibits AI from replacing human teachers.**
🔵 Combined with the Philippine and Singaporean rules below, *teacher-in-the-loop is not a
positioning choice in this market — in a growing number of jurisdictions it is the law*, and an
architecture that cannot show the human in the loop is unsellable in them.
🟡 **Also pending: California** (bar student data from training models absent direct school
benefit) and **Vermont HB 650** (edtech vendor registration + annual privacy certification) —
🔵 both would make *vendor-side evidence* a deliverable.
🔴 **Named gap: no Canadian provincial or Mexican federal K-12 source was located this pass**, so
"North America" here means the United States. 🟢 Stated rather than left to look like coverage.

🟢 **Payload-read assets placed here:** `jcputney/scorm-again` **MIT**, npm **v3.4.5 2026-10-05**;
`adlnet/CATAPULT` **Apache-2.0** (cmi5 conformance — 🔵 the evidence artefact a public buyer asks
for); `Khan/tutoring-accuracy-dataset` — 🔴 **bespoke evaluation-only licence, no training, no
production (`P783`)**.

### EMEA

🟡 **The timetable, and it moved:** the AI Act reported generally applicable **2026-08-02**, with
**Annex III** high-risk obligations — education among them — **postponed to 2027-12-02** by the
Digital Omnibus. 🔴 **Parliament's vote is reported as 2026-06-16; Council adoption could not be
confirmed this pass.** 🟢 **`P718` stands and is now the planning rule: `2027-12-02` is a backstop,
not a start.**

🔴 **What already binds, and is the sharpest line in any region:** **emotion recognition in
education institutions is prohibited** — reported from **2025-02-02**, medical/safety exception
only. 🔵 **This is the one place where a whole product category is simply off the table**, and
"engagement detection" in a proctoring or classroom-analytics pitch is that category under another
name. 🟢 **Also live: the AI-literacy duty** (🟡 the 2026 omnibus reported to have dropped the
"sufficient level" wording), and 🟢 **an Article 27 Fundamental Rights Impact Assessment for public
schools as deployers** — 🔵 a deliverable Globant can produce, and one private providers do not owe.

🟢 **Annex III pt 3 covers four functions:** admissions/access, assessment of learning outcomes,
steering an educational path, and proctoring. 🔵 **So the EMEA pre-flight is mechanical:** if the
agent touches any of those four, it is high-risk, and bias testing, human oversight and user
notification are scope items rather than nice-to-haves.

🟢 **Payload-read assets placed here:** `DFE-Digital/education-benchmarking-and-insights` **MIT**
(🔵 a national education ministry publishing benchmarking code permissively — the reference for a
public-sector conversation), `openfun/ralph` **MIT** (LRS, EU-funded provenance, 🔵 which is the
data-residency answer), `PerfectlyNormal/scorm` **MIT** (Norway), `AI-for-Education/*` **MIT**
(🔵 incl. Luganda benchmarks — Africa-facing, and 🔴 the Luganda repo is **ungranted**).
🔴 `eth-lre/mathtutorbench` (Switzerland) is **ungranted**.

### APAC

🟢 **The region moved furthest this pass, and it is the only one where a *national* instrument
names education as high-risk in statute.**

🔴 **Vietnam — decree `142/2026/ND-CP`, issued 2026-04-30.** Education is a high-risk sector;
**automated assessment** and **behavioural monitoring** named. **Three risk tiers, and the
*provider* self-classifies before deployment.** 🔵 **Self-classification is a billable artefact** —
somebody must write the justification, and getting the tier wrong is the provider's exposure, not
the school's.

🟢 **Philippines — `DepEd Order 003 s. 2026`** (basic education) and **`CHED Memorandum Order 21
s. 2026`** (higher education), both positioning AI as **supplementary, not a replacement for
teachers or critical thinking**. 🟢 **Singapore — MOE**: Primary 4 AI tools must be **structured,
teacher-supervised and delivered through the Student Learning Space, not open platforms.**
🔵 **Singapore's is a *channel* constraint, which is the most architecturally specific rule in
any region — it dictates the integration surface, and an SLS-reachable tool is a different build
from a web app.**

🟡 **Japan and South Korea:** reported to be introducing education AI data-protection rules by
**one weak secondary source only** — 🔴 **carried as a gap, not a row.** 🟡 Korea is separately
widening an AI Korean-language platform to immigrant-background students.
🟡 **Sentiment, which cuts against the regulation:** the Ipsos Education Monitor 2026 reports
**Australia and New Zealand with higher support for banning AI in schools** than the Asian markets
examined. 🔵 **So ANZ is the APAC market where the obstacle is consent, not compliance** — a
different sale entirely.
🟡 Reported regional share: Asia growing from **25 % of the AI-in-education market in 2026 to 38 %
by 2036**. 🔴 APAC market-size figures disagree by more than 2× between firms (**USD 987 M** vs
**USD 2 282.9 M**) and 🟢 **neither should be quoted.**

🟢 **Payload-read assets placed here:** `indobenchmark/indonlu` **Apache-2.0** (Indonesia),
`haolpku/K12-KGraph` — 🟡 **MIT code / CC BY-NC-SA data**, the curriculum-aligned KG a ministry
conversation asks for, 🔴 **evaluable but not resellable**; `leogaggl/lxHive` **GPL-2.0**
(Australia). 🔴 **Ungranted:** `malaysia-ai/malaysian-dataset`. 🔴 **CC BY-NC 4.0, commercial use
"strictly prohibited":** `Yunfeng-Wan/CSTutorBench`.

### LATAM

🔴 **No AI statute is in force anywhere in the region, and that is the finding — not an absence of
one.** 🟡 **Brazil `PL 2.338/2023`**: Senate-approved **Dec 2024**, now in the **Chamber of
Deputies**, so the text can still change; risk-based, with an **Algorithmic Impact Assessment** for
high-risk deployers, and education named a priority in the **2024** strategy revision.
🟡 **Mexico:** no AI law enacted as of early 2026; bills pending; early-2026 copyright/labour/film
amendments awaiting Official Gazette publication; government stresses **"technological
sovereignty"**; reported **6th in LATAM on government AI readiness**. 🟡 **Chile** reported at an
advanced legislative stage; 🟡 **Argentina and Colombia** rely on **general data protection only**.

🟢 **Two concrete, dated public-sector entry points — the most actionable LATAM items this pass:**
the **UNESCO Observatory on AI in Education for LAC**, launched **2026-04-14**, the first
UN-anchored regional platform on this axis; and a **UNESCO + CONALEP + DGETI** centres-of-excellence
pilot in Mexico, **2026-08-18**. 🔵 **CONALEP and DGETI are federal technical-and-vocational
systems with hundreds of campuses** — a centres-of-excellence model there is a reference engagement
with a ready replication path.

🟢 **And LATAM is the region whose *open-source* position is strongest on this shelf, which inverts
the usual framing:** 🟢 **`latam-gpt/lm-evaluation-harness` (MIT)** and 🟢 **`latam-gpt/syco-bench`
(MIT)**, plus 🟢 **`eduagarcia/lm-evaluation-harness-pt` (MIT)** for Portuguese — **three permissive,
regionally-authored evaluation assets**, where APAC's equivalents are NC or ungranted.
🔵 **Read with `P782`: LATAM is the one region where the evaluation layer is permissively licensed
by the people who built it**, so a Spanish/Portuguese assessment engagement can be evidenced
without a licence negotiation. 🔵 **Combined with no statute in force, LATAM is the lowest-friction
region to *build* in and the highest-uncertainty region to *commit* in** — the sandbox in Brazil
being the one supervised route.
🔴 **Named gap, unchanged from pass 60 and searched again: no classroom or university AI adoption
*metric* for Brazil or Mexico, and no named regional edtech vendor, was located.**

## 🟢 Sixtieth pass, 2026-10-08 — the four-region **regulatory** shelf is re-queried and comes back **correct on every date**, so this pass's market finding is about the **oracle**, not the data

⏱️ **Fourteenth pass of this date. Append-only: this section is new; nothing below it was rewritten.**
🟢 **Per the convention, pass 59's `## Opportunities by region` heading is retitled *superseded*; the live block is below.**

### 🟢 `P777` — four regional queries returned **nothing this KB does not already hold**, and that is a positive result about the shelf

🟢 **The four mandated regional queries were run** (`AI education {region} 2026 adoption regulation
players`, for North America, EMEA, APAC, LATAM). 🟢 **Every regulatory instrument they returned was
already shelved, at equal or finer resolution:**

| Instrument the query returned | Already held? | KB's value, and it is confirmed |
|---|---|---|
| EU AI Act Annex III high-risk, education | 🟢 yes | **`2027-12-02`** — Digital Omnibus, Parliament 2026-06-16, Council 2026-06-29, **Reg. (EU) 2026/1744** in force **2026-07-27** |
| Korea AI Basic / Framework Act | 🟢 yes | in force **`2026-01-22`**, 2026 a pilot year, **one-year penalty grace** |
| Vietnam AI law + high-risk list | 🟢 yes | live **`2026-03-01`**, extraterritorial, **Decision 33/2026/QD-TTg**, education among six high-risk sectors |
| Taiwan AI Basic Act | 🟢 yes | **Dec 2025** |
| Ohio district AI-policy mandate | 🟢 yes | **ORC 3301.24**, due **`2026-07-01`** |
| California **AB 1159** | 🟢 yes | bars student data for model training, **private right of action** |
| **H.R. 8747** K-12 AI Literacy Act | 🟢 yes | advanced in committee **July 2026** |
| UNESCO IESALC higher-ed study | 🟢 yes | 200 institutions / 19 countries, **87 %** use AI, **~26 %** have a framework |
| UNESCO LAC **Observatory** | 🟢 yes | launched **April 2026**, ECLAC Santiago |
| Uruguay **Ceibal** | 🟢 yes | **75 %** of public-school teachers |

🔴 **One query served the *superseded* `2026-08-02` Annex III date again** — the EMEA channel defect
`P718` / `Gap 270` predicts, now observed in a third consecutive pass. 🟢 **The planning rule is
unchanged: `2027-12-02` is a *backstop*, not a start, and Article 50 marking duties are live now.**

🔴 **And the oracle blockade is confirmed for a fourth pass, `n = 2` each:** `digital-strategy.ec.europa.eu`,
`artificialintelligenceact.eu`, `eur-lex.europa.eu`, `iesalc.unesco.org`, `unesco.org`,
`multistate.us` — **6 of 6 at `000`**. 🟢 **`P731` restated: the repository shelf has four working
oracles and the regulatory shelf has none, so every regulatory row here is 🟡 *reported* by
construction** — and the right response is to re-query for *contradiction*, which is what this pass
did and found none.

### 🟡 Market sizing — two new regional figures, both low-confidence, neither displacing the shelf

🟡 **EMEA:** one forecast puts Europe at **USD 2.11 bn (2026) → 19.97 bn (2034), CAGR 32.47 %**.
🟡 **APAC:** another puts the region at **USD 2 282.9 m (2025)**. 🔴 **Both are single-vendor
forecasts and they conflict with the global series this KB already carries** (**USD 10.6 bn 2026 →
42.48 bn 2030**) and with the North America share (**36 %**, **USD 3.68 bn 2026**). 🟢 **Recorded as
range evidence only**: the shelf's rule stands — *use the global series for scale and the regional
share for mix; never add two vendors' regional numbers together.*

## Opportunities by region — superseded (the live block is at the top of this file)

### North America

🟢 **The interop edge is now permissively covered, and this is where it pays first.** OneRoster is a
**1EdTech / US-origin** standard and US K-12 rostering is where it is actually enforced in
procurement. 🟢 **Two MIT clients measured this pass** —
[`longsightgroup/oneroster`](https://github.com/longsightgroup/oneroster) (`8c14777`, TS, REST + CSV)
and [`TCI/OneRoster`](https://github.com/TCI/OneRoster) (`5f8a15a`, Ruby) — plus **two US-origin
permissive LRS rows**, [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) (Apache-2.0)
and [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) (Apache-2.0, from the body that wrote
xAPI).

🔵 **The offer, placed:** the binding constraints here are **policy**, not capability — Ohio's
district-policy mandate (`2026-07-01`, passed), Oklahoma's educator-supervision rule landing before
2027-28, **AB 1159**'s no-training-on-student-data default, NYC's Pre-K–8 generative-AI moratorium.
🟢 **Every one of them is satisfied by evidence, and an LRS is the evidence layer**: an Apache-2.0
SQL LRS gives a district an auditable record of what the AI did, per learner, on infrastructure it
already runs. 🔴 **`P764` still governs the function axis** — a grading connector can be MIT and
**prohibited**; the licence gate never answers the policy question.

### EMEA

🟢 **The permissive, EU-origin row landed this pass:**
[`openfun/ralph`](https://github.com/openfun/ralph) — **MIT**, `53cc58c`, from **France Université
Numérique**: an LRS *plus* a learning-analytics toolkit. 🔵 **Why its provenance is part of the
offer:** a public-sector EU buyer weighing data residency and procurement defensibility gets an
EU-funded, MIT-licensed record store rather than a US-hosted SaaS.

🟢 **Timing, restated:** **Annex III stand-alone high-risk reaches `2027-12-02` as a backstop**,
Article 50 marking is **live**, Article 4 AI-literacy duties are **in force** (the 2026 Omnibus
dropped the "sufficient level" wording but kept the obligation), and **emotion recognition in
education is prohibited outright** since 2025-02-02. 🟢 **The sellable artefact is the Annex III
technical file** — a conformity dossier a vendor can hand its client — and the LRS is where its
human-oversight and logging evidence comes from. 🔴 **Only ~10 % of 450+ institutions have formal AI
guidelines**, so the policy-to-practice gap is the same product as in North America, against a
harder instrument.

### APAC

🟢 **This region supplied the most *technical* substance this pass, and it is all research-grade:**
[`wwrwbs/AI_AWE`](https://github.com/wwrwbs/AI_AWE) (**Apache-2.0**, Fudan — essay scoring,
`Gap 272` closed), [`haolpku/K12-KGraph`](https://github.com/haolpku/K12-KGraph) (**MIT code**,
Peking University — curriculum-aligned KG benchmark), `tswsxk/TKT` and `tswsxk/XKT` (**MIT**,
knowledge tracing), and the GPL-2.0 Australian LRS
[`leogaggl/lxHive`](https://github.com/leogaggl/lxHive).

🔵 **The offer, placed:** APAC has the hardest **binding** instruments and the most usable code.
**Vietnam** (live `2026-03-01`, extraterritorial, education high-risk where the output is the sole
basis without meaningful human review) is the clearest written specification of an
assessment-governance build anywhere; **Korea**'s penalty grace makes 2026 the cheap year to become
compliant. 🟢 **An Apache-2.0 scorer plus a curriculum-aligned benchmark plus a human-review gate is
exactly Vietnam's trigger condition, satisfied in code.** 🔴 **Both regional corpora are
non-commercial** (PERSUADE 2.0 and K12-KGraph's data are CC BY-NC-SA 4.0) — **the architecture
travels, the data does not**.

### LATAM

🔴 **Stated explicitly, because silence would look like coverage: this pass found no new LATAM
repository, no new LATAM instrument, and no new LATAM figure.** 🟢 **The four-region query ran for
LATAM and returned only material already shelved** — UNESCO IESALC (87 % adoption / ~26 % with a
framework), the LAC Observatory (April 2026), Ceibal's 75 %, TALIS 2024 teacher rates above the OECD
average in Brazil, Chile, Colombia and Costa Rica, and the still-pending bills (Brazil **PL
2.338/2023** in the Chamber, Chile's bill in its first constitutional stage, Colombia **CONPES
4144** running to 2030).

🔵 **So the LATAM opportunity is unchanged and it is now sharper by contrast with the other three
regions:** LATAM is the only region of the four with **high measured adoption and no binding
education-AI instrument**. 🟢 **That makes the deliverable governance-first, not compliance-first** —
an institution-level AI framework for the **~74 %** of universities that have none, with the
**61-point** adoption-to-governance gap as the stated baseline. 🔴 **And the asset gap is real: of
the 19 repositories measured this pass, zero are LATAM-origin.** 🟡 **The nearest shelved
Spanish-language asset remains `0xnavarro/IA-PARA-TODOS` (Apache-2.0), which is enablement material,
not a runtime** — so a LATAM engagement composes North American and APAC code against a
Spanish/Portuguese-language gap that nobody on this shelf has filled. 🔵 **That absence has now been
recorded for enough consecutive passes to be a market observation rather than a search failure.**

## 🔴 Fifty-ninth pass, 2026-10-08 — the four-region assessment constraint has **two modes, not one**: the largest US district does not *gate* AI grading, it **prohibits** it — and no human-in-the-loop engineering satisfies a prohibition

⏱️ **Thirteenth pass of this date. Append-only: this section is new. One declared edit below:
pass 58's `## Opportunities by region` heading is retitled *superseded*, per the convention
passes 56–58 each applied to their predecessor.**

> 🔵 **Opening hypothesis: that a primary source would be reachable this pass and `Gap 270` could
> finally be closed first-hand.
> 🔴 REFUTED, 6 of 6.** 🟢 **Every row in this file remains 🟡 reported** (`P748`), and `P731` now
> has its third consecutive confirmation.

### 🔴 `P764` — the governance picture is **not** a single spectrum, and this KB has been publishing it as one

🟢 **Measured across the four regional channels, the constraint on automated assessment takes two
structurally different forms:**

| Mode | Instrument | What it demands | Can engineering satisfy it? |
|---|---|---|---|
| **Gated** | 🟡 EU AI Act Annex III (education access, evaluation, exam scoring = high-risk) | risk management, data governance, human oversight, transparency, conformity assessment *before* deployment | 🟢 **Yes** — this is a build spec, and it is what `P710` was designed against |
| **Gated** | 🟡 Vietnam high-risk list — education named, incl. automated assessment and behavioural monitoring (law passed 2025-12-10, effective **2026-03-01**) | trigger-condition compliance | 🟢 **Yes** |
| **Gated** | 🟡 Korea AI Basic Act, in force **2026-01-22**; 2026 run as a pilot year with a one-year penalty grace | staged obligations | 🟢 **Yes** |
| **PROHIBITED** | 🟡 **NYC Public Schools**, guidance of **2026-03-24** | AI **may not** decide grades, promotion, discipline, counselling, crisis intervention, IEP/504 development, or academic placement — the "red light" tier | 🔴 **No.** A prohibition is not a control to implement; it removes the use case. |

🔴 **This is the correction:** `P705` recorded "automated assessment is constrained in all four
regions" and every recipe since has read *constrained* as *gated*, i.e. as a human-oversight
engineering requirement. 🟢 **In the largest school district in the United States — ~1 M students —
the grading use case is simply unavailable, and a better audit trail does not change that.**

### 🔴 `P764a` — and NYC went further six months later

🟡 **2026-09-02: a one-year moratorium on all student-facing generative-AI software for grades
2K–8** (announced by Mayor Mamdani). 🟡 **Companion chatbots prohibited across all grades.**
🟡 **Teachers retain AI for instructional planning and operational tasks — explicitly not for
grading or assessment.** 🟡 **High-school use permitted in a limited way, for AI literacy and
career readiness.**

🔵 **The direction of travel matters for a 12-month engagement pipeline:** between March and
September, the student-facing surface **narrowed** while the teacher-facing surface stayed open.
🟢 **That is the opposite of the "adoption outruns governance" trend (`P749`)** — in this one
jurisdiction, governance moved first and moved twice.

### 🟢 `P765` — the cross-region finding that survives comparison, and it is a coincidence worth naming

🟡 **LATAM (UNESCO IESALC, launched Sept 2026, 200 institutions / 19 countries): 87 % of
institutions use AI in at least one area, and the report's headline is that governance frameworks
lag adoption.** 🟡 **Digital Education Council LATAM survey (29 institutions, with Tec de
Monterrey): 79 % of faculty use AI in teaching, but 88 % describe their use as minimal to
moderate — and the *lowest* adoption of all is in assessment: cheating detection and feedback
generation.**

🟢 **So the function regulators target hardest in three regions is the function LATAM faculty have
adopted least, in the region with the least education-specific AI regulation.** 🔵 **Read as
opportunity rather than as irony: LATAM is the one region where an assessment build would not be
retrofitting against an installed base of ungoverned practice** — the practice is not installed
yet. 🔴 **Read as risk: there is no local instrument to design against, so a LATAM assessment
build should be specified against EU Annex III anyway, because that is the only written standard
available and it travels.**

### 🟡 The global market numbers — spread, not consensus (`P748`: all 🟡 reported)

| Source | 2026 | Horizon | CAGR |
|---|---|---|---|
| 🟡 Research and Markets | ~$10.6 B | ~$42.5 B by 2030 | — |
| 🟡 secondary aggregator | — | ~$32 B by 2030 (from ~$6 B in 2024) | — |
| 🟡 vendor blog | $12.3 B | — | — |

🔴 **The spread between the low and high 2030 figures is larger than the entire 2026 market**, and
🟢 **no figure in this table was verifiable first-hand from this environment** (`P731`).
🔵 **Use them for direction, never for a business case.**

## Opportunities by region — superseded (the live block is at the top of this file)

### North America

🟡 **Posture: guidance-and-bills, few mandates — and the mandates that exist are about *having a
policy*, not about what it says.**

- 🟡 **Ohio is the sharpest instrument:** HB 96 (the 2025 budget) created **ORC 3301.24**, requiring
  **every** district, community (charter) and STEM school to adopt an AI policy by
  **2026-07-01** — a deadline now passed. ODEW had to publish a model policy by 2025-12-31 and
  released it in early January 2026. 🟢 **It mandates adoption only: it does not dictate content,
  does not require teaching AI, and does not require using AI.**
- 🟡 **Oklahoma SB 1734** requires a written district AI policy before the 2027-28 school year.
- 🟡 33–35 state education departments plus Puerto Rico publish official AI guidance; 🟡 ~134
  AI-in-education bills across 31 states this session (single outlet — treat as indicative).
- 🟡 **Data and decision limits:** California **AB 1159** bars using student data to train AI
  models; Idaho **SB 1227** requires privacy protections for school AI tools; Oklahoma and Maryland
  require human oversight and bar AI from high-stakes student decisions; Oregon **SB 1546** mandates
  minor-protective design including anti-compulsive-use measures.
- 🟡 **Curriculum and capacity:** Alabama **HB 329** makes an approved CS course including AI
  instruction a graduation requirement; Maryland **SB 720** requires state-provided teacher PD.
- 🟡 **District layer is where prohibitions live:** NYC (`P764`, `P764a`); Chicago, Denver and
  Charlotte-Mecklenburg have issued their own policies. 🟡 In higher ed, UChicago Law is piloting
  devices out of core 1L classes from fall 2026 and Berkeley Law has barred AI for exams and
  credited coursework.

🟢 **Globant opportunity, placed:** the **policy-to-practice gap** is the product. Ohio created
~1 000 adopted policies with no required content and no implementation obligation; the sellable work
is turning an adopted policy into enforced configuration — tool inventories and approval
workflows, vendor data-processing review, the green-tier teacher productivity surface
(translation, lesson planning, family communications), and audit evidence. 🔴 **Do not lead with
automated grading in US K-12 public: `P764` makes it unavailable in the largest district and
restricted in at least two states.**

### EMEA

🟡 **Posture: the only region with a binding, written, education-specific standard.**

- 🟡 **EU AI Act:** education access and assessment — admission decisions, student evaluation, exam
  scoring — are **Annex III high-risk**, carrying risk management, data governance, human oversight,
  transparency and pre-deployment conformity assessment.
- 🟡 **Enforcement by the AI Office and national authorities began 2026-08-02.** 🟡 **The "AI
  omnibus" amendments were adopted in June 2026 and reported as entering into force 2026-07-27.**
  🔴 **`Gap 270` is NOT closed: the Commission pages asserting this are `000` from this
  environment, 6 of 6 primary hosts.** 🟢 **`P718` stands as the planning rule — `2027-12-02` is a
  **backstop**, not a start, so the Annex III runway is not guaranteed.**
- 🟡 Market: Europe ~$2.64 B in 2026 → ~$8.0 B by 2030 at ~31.9 % (aggregator). 🟡 Finland, Estonia
  and the Netherlands lead K-12 integration. 🟡 UK: £4 M into AI lesson-planning and marking tools.
- 🟡 **Readiness lags badly: ~10 % of 450+ surveyed institutions have formal AI guidelines.**
- 🟡 **MEA:** rules nascent but moving — UAE National AI Strategy 2031 and AI Ethics Guidelines;
  Saudi **SDAIA** national data-and-AI governance framework; Kenya, South Africa and Nigeria
  actively drafting.
- 🟡 **UAE curriculum (`Gap 266`, resolved — see `intel/trends.md` `P767`):** AI as an official
  subject KG–Grade 12 in **public** schools from **2025-26**, delivered inside the existing
  "Computing, Creative Design and Innovation" course with **no written exams** and 1 000 trained
  teachers; from **2026-27** a **standalone** subject, "Artificial Intelligence and Technology",
  replacing CCDI and extended to **private schools following the MoE curriculum**. 🔴 Private
  schools on other curricula (ADEK, KHDA, SPEA) are outside the federal mandate.
- 🟡 **Unverified and flagged:** a claim that the UAE Cabinet approved AI curriculum for *all*
  public and private schools on 2026-09-02 with 22 000 teachers trained. 🔴 **No official release
  located; do not plan on it.**

🟢 **Globant opportunity, placed:** EMEA is the only region that will **pay for conformity
artefacts**, because they are legally required. Annex III work — technical documentation, data
governance records, human-oversight design, post-market monitoring — is billable here and nowhere
else. 🔵 **Second, specific to the public tier: the EUPL band** (eight Finnish national education
services carry it, per `dependency-licence-closure`) is a procurement precondition European buyers
state and this KB's classifiers only recently learned to read.

### APAC

🟡 **Posture: no single framework; education is reached through high-risk categories and general
data/safety law.**

- 🟡 **Vietnam is the most education-explicit instrument anywhere:** its high-risk AI list names
  education directly, including **automated assessment and behavioural monitoring**. Law passed
  **2025-12-10**, effective **2026-03-01**.
- 🟡 **South Korea:** AI Basic Act in force **2026-01-22**; the regulator has signalled 2026 as a
  pilot period with a one-year grace on penalties.
- 🟡 **Taiwan:** AI Basic Act passed December 2025. 🟡 **China:** binding rules on algorithms, deep
  synthesis and generative AI. 🟡 **Singapore and Japan:** voluntary guidelines over existing law.
  🟡 **Australia:** AI Safety Institute announced November 2025, safety-focused rather than
  education-focused.
- 🟡 Market (single report, treat as indicative): China, India and Japan dominate AI-in-education;
  named players Google, Microsoft, IBM, Pearson, Byju's. 🟡 APAC AI market overall ~$102 B, with
  India the fastest-growing at ~38.9 % CAGR.

🟢 **Globant opportunity, placed:** Vietnam's trigger condition is the clearest written
specification of an assessment-governance build in existence (`P706`), and Korea's grace year is a
dated window — a system delivered during 2026 is specified against a live statute whose penalties
have not yet attached. 🔵 **The behavioural-monitoring half of Vietnam's listing is the under-served
side: proctoring is where this KB has measured licence risk concentrating (`R57c`), and it is now
also where APAC regulation points.**

### LATAM

🟡 **Posture: the widest adoption measured anywhere, and the thinnest governance.**

- 🟡 **UNESCO IESALC, launched September 2026 — 200 institutions, 19 countries: 87 % use AI in at
  least one area of activity; the report's own headline is that governance and institutional
  strategy lag adoption.**
- 🟡 **Digital Education Council LATAM survey (29 institutions, with Tec de Monterrey): 79 % of
  faculty use AI in teaching — 18 points above the 2025 global figure — but 88 % call their use
  minimal to moderate, and adoption is lowest in assessment** (cheating detection, feedback
  generation).
- 🟡 **Institutional layer is real and names its partners:** UNESCO launched the **Observatory on
  Artificial Intelligence in Education for Latin America and the Caribbean** on **2026-04-14**, with
  CAF, CENIA (Chile), CETIC.br (Brazil), ECLAC, Fundación Santillana, Tecnológico de Monterrey,
  ProFuturo and Fundación Ceibal (Uruguay); plus a Mexico pilot with CONALEP and DGETI.
- 🟡 **General AI law, not education law:** Uruguay is the first Latin American signatory of the
  Council of Europe AI Framework Convention (2025); Peru's law creates regulatory sandboxes with
  differentiated timelines for micro and small enterprises; Mexico's Senate received a federal
  risk-based AI bill in 2024; Colombia adopted CONPES 4144 in February 2025.
- 🔴 **Explicit gap, written down rather than left silent:** **no 2026 regulation specifically
  governing AI in schools or universities was located in the region.** 🟢 **What exists is soft
  guidance and capacity-building** (UNESCO ethics training for officials in Ecuador and Chile).
  🔵 **Searching in Spanish and Portuguese, and reading the Brazilian, Mexican and Chilean ministry
  sites directly, is the named next step — all are `000` from this environment.**

🟢 **Globant opportunity, placed, and it is the strongest regional fit on this shelf:** 87 %
adoption with lagging governance is a **governance-retrofit** market, and Globant's LATAM delivery
footprint sits inside it. The product is the institutional AI framework — acceptable-use policy,
tool inventory, academic-integrity process, faculty enablement — sold to institutions that have
already adopted the tools. 🔵 **And `P765` is the differentiator: because assessment adoption is
still *low* here, a LATAM institution can be taken straight to a governed assessment design
specified against EU Annex III, without unwinding an installed ungoverned practice first.**


## 🟢 Fifty-eighth pass, 2026-10-08 — `Gap 275` **CLOSED**: every row below carries an **evidence-class marker**, and the cross-region finding is that **adoption outruns governance everywhere it is measured**

⏱️ **Twelfth pass of this date. Append-only: this section is new; nothing below it was rewritten.**

> 🔵 **This pass's opening hypothesis was that the regional channels would yield comparable market pictures.
> 🟡 CONFIRMED for LATAM and North America, REFUTED for EMEA and APAC** — 🔴 **both returned *enterprise* AI material with no education-specific content, and this pass writes that down as a gap rather than padding it with proxies.**

### 🟢 `P748` — the evidence-class marker, which `Gap 275` asked for

🔴 **Pass 57 (`P731`) measured that this KB has no first-hand verification path for any market or regulatory row, while the repo shelf has five oracles — and then noted that 57 passes had published both classes in the same visual register.** 🟢 **`Gap 275` asked for a marker. Here it is, used on every row in this section:**

| Marker | Meaning | Verifiable here? |
|---|---|---|
| 🟢 **`[M]` measured** | Read first-hand this pass from a reachable oracle | 🟢 **Yes** |
| 🟡 **`[A]` attributed** | Channel reports it **and names a primary source** this KB cannot open | 🔴 No — 🟡 **but falsifiable later** |
| 🔴 **`[U]` unattributed** | Channel reports it with **no named source**, or the source is a vendor page | 🔴 **No — treat as a lead** |

🟢 **Zero `[M]` rows exist in this section, and that is the point:** 🔴 **every regulatory and market host remains `000`/`EGRESS_BLOCKED` (`P731`, re-confirmed `n=3` this pass).** 🔵 **So `intel/market.md` is a **lead shelf**, and `repos/` is an **evidence shelf** — the marker makes the asymmetry legible instead of implicit.** 🟢 **`Gap 275` → CLOSED on `intel/market.md`.** 🆕 **`Gap 280` — the other seven shelves still carry no marker; `intel/trends.md` is next in line.**

### 🔴 The global market numbers, and why their **spread** is the only honest headline

🟡 **`[A]`/🔴`[U]` — three vendor forecasts for the same market, same year:**

| Source class | 2025/26 base | Forecast | CAGR |
|---|---|---|---|
| 🟡 `[A]` IMARC-based | **USD 6,4 B** (2025) | **USD 79,6 B** by 2034 | **31,35 %** |
| 🔴 `[U]` second firm | **USD 8,3 B** (2025) | **USD 57,2 B** by 2033 | **25,9 %** |
| 🔴 `[U]` third firm | **USD 7,52 B** (2025) → **10,6 B** (2026) | — | **40,9 %** |

🔴 **A 2025 base that ranges 6,4–8,3 B (**30 % spread**) and a CAGR that ranges 25,9–40,9 % are not three estimates of one number; they are three different definitions of the market.** 🟢 **Usable conclusion: direction only — strong growth, and **no figure from this shelf belongs in a client deck without its source attached**.** 🟡 **`[A]` One commentary rates sector maturity at **35/100**, *"most institutions are still in pilot mode"* — 🔵 **which is the most decision-relevant global number here, and it points the opposite way from the CAGRs.**

🟡 **`[A]` Segment splits, single-source each:** cloud deployment **71,22 %** of the AI-tutor market (2024) · K-12 **45,62 %** of adoption · STEM **34,78 %** of revenue, language learning fastest-growing · AI tutors **USD 1,63 B (2024) → 7,99 B (2030)**. 🔴 **`[U]`** student AI usage **66 % (2024) → 92 % (2025)** — 🔴 **one source attributes this to UK data while presenting it as global; do not use it as a worldwide figure.**

### 🟢 `P749` — the finding that **does** survive cross-region comparison: the governance gap, measured twice

🟢 **Two independent regional studies, different methods, same shape:**

| Region | Institutions **using** AI | Institutions with a **formal framework** | 🔴 **Gap** |
|---|---|---|---|
| 🟡 `[A]` **LATAM** (UNESCO IESALC + UNU-IAS, 200 institutions, 19 countries, Aug–Oct 2025) | 🟢 **87 %** | 🔴 **~26 %** | 🔴 **~61 pts** |
| 🟡 `[A]` **North America** (2026 statistics roundup) | 🟢 high — **92 %** student usage reported | 🔴 **10 %** have formal AI guidelines | 🔴 **~82 pts** |
| 🟡 `[A]` **APAC** (regional survey) | 🟡 **57 %** of Asian organisations use AI in ≥1 area | 🔴 *"governance gaps widen"* — **not quantified** | 🔴 **direction only** |

> 🟢 **`P749`.** *The single most consistent, most actionable fact across all four regions is **not** market size — it is that **institutional AI use has outrun institutional AI governance everywhere it has been measured**, by 61 points in LATAM and ~82 in North America.* 🔵 **For Globant this inverts the obvious engagement: the scarce deliverable is not another tutor, it is the **framework, policy and assurance layer** an institution needs before it can safely keep the tools it is already using.* 🟢 **And it joins directly to this KB's licence work: an institution with no AI framework has no licence-compliance step either — which is exactly how a repo like `kamlendras/OpenProctor` (README MIT, payload **AGPL-3.0** with §13, `P725a`) reaches production in a hosted proctoring service.**

## Opportunities by region — superseded (the live block is at the top of this file)

### North America

🟡 **`[A]`/🔴`[U]` Market & adoption:** largest regional market on most estimates — **37,5 %** global share (2025) 🟡`[A]`; one analysis puts the region at **USD 951 M (2024) → ~2,3 B (2029), 15,9 % CAGR** 🔴`[U]`, while a separate report cites a **41,7 %** regional growth figure 🔴`[U]` — 🔴 **a 26-point CAGR disagreement between two vendor reports on the same region, which is itself the finding.** 🟡 `[A]` **36 %** share of regional adoption; 🔴 **only 10 %** of institutions have formal AI guidelines; 🔴 **71 %** of U.S. teachers lack AI training.

🟡 **`[A]` Regulation — fragmented by design:** education AI described as operating in *"a relative regulatory vacuum"*, with adoption decided by individual districts and universities; state-level piecemeal requirements named in **Colorado** and **Texas**. 🔴 **No federal framework surfaced.** 🔴 **`[U]`** the same source claimed the EU AI Act's high-risk classification for education with an August 2026 timing it could not stand behind — 🔵 **cross-filed to EMEA below, and `Gap 270`'s Official-Journal question stays open (`P731`).**

🟡 **`[A]` Named players & money:** **Carnegie Mellon + Gates Foundation — USD 55 M** into AI courseware for gateway college courses · **OpenAI** country-level education programme with **8 national partners** (Q1 2026) · **Pearson** student-interaction analysis. 🔴 **`[U]`** a **USD 169 M** public commitment to responsible AI in higher education (Q1 2026) — 🔴 **the source does not name the government, so this is a lead, not a datum.**

🟢 **Opportunity for Globant:** 🟢 **the governance gap is widest here (~82 pts), and procurement is **institution-level**, so the sellable unit is a repeatable *AI-governance-plus-integration* package per district or university** — not a national programme. 🔵 **Pair it with the LTI 1.3 boundary (`R57a`/`P736`): North American institutions overwhelmingly run Canvas (**AGPL-3.0**, `P734`), so a tool that integrates without touching platform source is the only safely hostable shape.**

### EMEA

🔴 **DECLARED GAP — the mandated regional query returned no education-specific material.** 🟢 **Stated explicitly so silence is not read as coverage:** `AI education EMEA 2026 adoption regulation players` returned **enterprise** AI content (CompTIA IT-strategy outlook, a Workday enterprise-adoption study, a communications-sector report, Google Cloud's Applied AI EMEA team). 🔴 **The channel conceded it in its own words:** *"The search didn't return anything specifically about AI in education in EMEA in 2026."* 🔴 **Not one education provider, ministry or regulator was named.**

🔴 **What the channel offered instead, and why each is unusable as an education datum:** **94 %** of organisations likely to invest in AI training in 2026 🔴`[U]` — 🔴 **US survey sample, presented in an EMEA-titled piece**; **38 %** of EMEA organisations *"yet to begin piloting"* 🔴`[U]` — 🔴 **from a study that appears in both 2023 and later versions, so the figure is dated and cross-sector.** 🟡 `[A]` **EU AI Act** remains the regulatory anchor, with education AI reported as **high-risk** — 🔴 **timing unverified, every primary host (`eur-lex.europa.eu`, `digital-strategy.ec.europa.eu`) `000` here (`P731`).**

🟢 **Opportunity for Globant, stated from the gap rather than despite it:** 🟢 **EMEA is the one region where the *binding* constraint is known (AI Act high-risk duties for educational use) while the *market* is unmeasured on this shelf.** 🔵 **That asymmetry favours a compliance-led entry: the AI Act work this KB already has executable (`compose/code/aiact-50-2-*` — marking, spans, exposure, packing) is the asset, and it is strongest precisely where the market intel is weakest.** 🆕 **`Gap 281` — EMEA education-market intel has now failed to materialise from the mandated query for two consecutive passes; a country-level query (Germany, France, Nordics, Gulf) is the untried shape.**

### APAC

🔴 **PARTIAL GAP — no education ministry policy, national AI-in-schools programme or student-data rule surfaced for 2026.** 🟢 **The channel said so:** *"I found no education-specific ministry policies, national AI-in-schools programmes, or student-data rules for 2026."* 🟢 **What it did return is corporate and real:**

🟡 **`[A]` Named players:** **Pearson + TCS** — multi-year AI learning alliance aimed at closing employer skills gaps · **LearnUpon** — new **Sydney** HQ and `Create+` AI course-authoring, explicit APAC push · **Alteryx** — Academy relaunched with personalised AI learning paths and new credentials. 🔵 **All three are *workforce / corporate* learning, not K-12 or higher ed — which is the shape of the APAC education opportunity as this channel sees it.**

🟡 **`[A]` Regulation:** **Australia** tightening AI governance and copyright rules, with OpenAI appointing an ANZ policy lead · **Singapore** consulting on AI in financial institutions — 🔴 **finance, not education; recorded so no later pass mis-files it** · one forecast expects APAC to *"harmonize on common principles: safety, transparency, accountability — yet be executed in ways unique to each market."* 🟡 `[A]` **Adoption:** **57 %** of Asian organisations use AI in ≥1 area; 🔴 **49 %** cite insufficient real-time data infrastructure as a barrier. 🟡 `[A]` **AI sovereignty** named as the pace-setter for the region in 2026.

🟢 **Opportunity for Globant:** 🟢 **corporate reskilling is where APAC's named demand actually is**, and 🔵 **the two constraints the channel names — data infrastructure (49 %) and sovereignty — both argue for the self-hosted stack this KB already assembles** (local inference + permissive integration layer), not a SaaS tutor. 🔴 **Per-market execution is explicit in the regulatory forecast, so a single APAC offer will not travel; the unit is per-jurisdiction.**

### LATAM

🟢 **The best-evidenced region on this shelf, and the only one with a named primary study — though still `[A]`, since `iesalc.unesco.org` and `publications.iadb.org` are `000` here (`P731`).**

🟡 **`[A]` Adoption, UNESCO IESALC + UNU-IAS — 200 institutions, 19 countries, Aug–Oct 2025:** teaching & learning **73,5 %** · research **57,0 %** · administration **34,1 %** · community engagement **20,0 %**; 🟢 **87 %** use AI somewhere, 🔴 **only ~26 %** have any formal framework. 🟡 **`[A]` By institution type:** private non-profit **84 %** · public **68 %** · private for-profit **52 %**.

🟡 **`[A]` Digital Education Council, *AI in Higher Education LATAM Survey 2026* — >30 000 respondents across 29 institutions:** **92 %** of students and **79 %** of faculty actively engage with AI, 🔴 **but only 19 %** of faculty use AI for assignment feedback. 🔵 **That 79 %-vs-19 % split is the most specific product signal in this entire section: faculty are using AI, and *not* for the task Globant's grading stack addresses.** 🟡 **Method caveat kept visible:** the two studies are **not comparable** — 200 institutions vs 29 — so their headline percentages must not be averaged.

🟡 **`[A]` Regulation — no unified framework:** **Chile** national AI policy (2021) · **Brazil** and **Colombia** national strategies with **no education-sector rules** · **Mexico**: SEP, ANUIES and Observatorio IA recommendations that *"carecen de carácter vinculante"* (non-binding). 🟡 **IDB** weighs EU-style risk-based models against sectoral ones for the region; its **ILIA** index covers 19 countries.

🟡 **`[A]` Named institutions:** Tecnológico de Monterrey (+ its Institute for the Future of Education) · UNAM · **UPC Peru** — *"más de setecientos"* teachers in weekly AI training · Pontificia Universidad Católica de Chile.

🟢 **Opportunity for Globant:** 🟢 **the 19 % faculty-feedback figure against 79 % general faculty use is a measured, named, unserved gap** — and it is exactly where this KB's `autorubric` + `rubric` two-scorer cross-check with a human-review gate (`P720`, `R57a`) applies. 🔵 **The 61-point governance gap means the framework sells *with* the tool, not after it.** 🔴 **And the regulatory patchwork is an advantage here, not a hazard: with no binding sectoral rule in Brazil, Colombia or Mexico, an institution's own framework is the governing document — so whoever writes it shapes the procurement.**

---


## 🟢 Fifty-seventh pass, 2026-10-08 — the market shelf and the repo shelf are **different evidence classes**, and only one of them is verifiable here

> 🔵 **This pass's opening hypothesis was that `Gap 270` (EU Official-Journal publication status)
> could be resolved by reaching a primary source.
> 🔴 **REFUTED, and the refutation generalises.** 🟢 **Measured: **every** candidate primary host is
> unreachable from this environment, while **five** repo oracles answer `200` on three probes each.
> 🔴 **So this KB has been publishing payload-verified repo rows and prose-only regulatory rows in
> the same visual register, with the same emphasis marks, for 57 passes.**

### 🔴 `P731` — the market channel has **no** first-hand verification path, and the repo channel has five

🟢 **Measured this pass, `n ≥ 2` per host:**

| Channel | Hosts probed | Reading |
|---|---|---|
| 🟢 **Repo / registry** | `raw.githubusercontent.com` · `pypi.org` · `registry.npmjs.org` · `repo.packagist.org` · `gitlab.com/api/v4` · `git ls-remote` | 🟢 **`200` / exit `0`, ×3 each** |
| 🔴 **Primary regulatory & market** | `digital-strategy.ec.europa.eu` · `eur-lex.europa.eu` · `unesco.org` · `iesalc.unesco.org` · `publications.iadb.org` · `nasbe.org` · `multistate.us` · `lw.com` · `timeshighereducation.com` · `nearshoreamericas.com` | 🔴 **`000` ×2 on all ten**; `WebFetch` returns **`EGRESS_BLOCKED`** |
| 🔴 GitHub web / API | `github.com` · `api.github.com` | 🔴 **`403` ×3** |
| 🔴 Model hub | `huggingface.co/api` | 🔴 **`000` ×3** |

🟡 **An authenticated GitHub channel exists in this environment but is scoped to this session's own
repositories**, so it is not a metadata oracle for third-party repos. 🔵 **Recorded so no later pass
reads the `403` as the whole story.**

> 🔴 **`P731`.** *Two evidence classes, and they are not comparable. 🟢 **A repo row on this KB is
> payload-verified: a byte count, a SHA, a licence title read first-hand.** 🔴 **A regulatory or
> market row is, in this environment, **irreducibly second-hand** — a search engine's summary of a
> source nobody here can open.** 🟢 **The remedy is not to stop publishing market rows — they are the
> mandate — it is to **mark the class**, so a reader can tell a measured date from a reported one.***
> 🆕 **`Gap 275` — no shelf on this KB carries an evidence-class marker, and `intel/market.md` is
> where it matters most.**

### 🟡 `Gap 270` — **NARROWED**, in the affirmative, and still not first-hand

🔴 **Pass 56 left open whether Official-Journal publication of the Digital Omnibus had completed,
noting that until it did, `2026-08-02` arguably remained the legal baseline.** 🟢 **This pass's EMEA
query returned a specific answer attributed to the Commission's own page:**

| Element | Reported this pass | Class |
|---|---|---|
| Council approval of the Digital Omnibus on AI | **June 2026** | 🟡 second-hand |
| 🟢 **Amendments entered into force** | 🟢 **`2026-07-27`** | 🟡 second-hand, attributed to the Commission page |
| Enforcement by AI Office + national authorities | from **`2026-08-02`** | 🟡 second-hand |
| Annex III stand-alone high-risk (education) | **`2027-12-02`** | 🟢 fifth pass confirmed |
| Annex I embedded | **`2028-08-02`** | 🟢 confirmed |

🟢 **If entry into force was `2026-07-27`, it preceded `2026-08-02` and the deferral was already
operative when the old baseline would have bitten — which resolves `Gap 270`'s ambiguity in the
affirmative.** 🔴 **But the page asserting it is `EGRESS_BLOCKED` here, so this is a *narrowing on
reported evidence*, not a closure.** 🟢 **`P718` stands unchanged and is the planning rule:
`2027-12-02` is a **ceiling** that harmonised standards can pull forward, and **Article 50 marking
is live now** with its backstop at `2026-12-02` — **eight weeks out** as of this pass.**

### 🟢 Regional channel — run independently, and it **reproduced the shelf**

🟢 **All four mandated regional queries run. 🔴 **Zero new instruments in any region.** 🔵 **Recorded
as calibration, which is a stronger statement than "saturated": an independent re-run reproducing
pass 56's regional table is evidence the table is **complete**, not evidence the channel failed.**

| Region | Re-confirmed independently this pass | Status |
|---|---|---|
| **North America** | **134 bills / 31 states**; **30+** states with guidance; **Ohio** first state to require a district AI policy, due **`2026-07-01`**; **California AB 1159** (bars student data for model training); **Oklahoma** and **Maryland** human-oversight / no-high-stakes-AI; **Oregon SB 1546** (compulsive-use design limits for minors); **Alabama** model procurement clause; **H.R. 8747** K-12 AI Literacy Act advanced in committee **July 2026**; teacher use **60 %** in 2024-25, **32 %** weekly | 🟢 all shelved |
| **EMEA** | EU AI Act Annex III **`2027-12-02`**, Art. 50 **live** (`P718`, `Gap 270` narrowed); remote-exam platforms using **facial recognition or behaviour analysis** carry bias-testing, human-oversight and notification duties; UNESCO GenAI guidance; 🔴 **only ~10 %** of 450+ institutions have formal AI guidelines | 🟢 all shelved |
| **APAC** | **Vietnam** AI law live **`2026-03-01`**, first standalone AI statute in SEA, **Decision 33/2026/QD-TTg** names **education** among six high-risk sectors with **automated assessment** and **behavioural monitoring** as the examples; **South Korea** AI Basic Act live **`2026-01-22`**, **one-year penalty grace** so 2026 is effectively a pilot year; **Taiwan** AI Basic Act **Dec 2025**; China binding algorithm/GenAI rules; Singapore & Japan voluntary | 🟢 all shelved |
| **LATAM** | 🔴 **still no binding education-AI instrument** — Brazil **PL 2.338/2023** in the Chamber, Chile's bill in first constitutional stage, Colombia **CONPES 4144** (budget to **2030**); **UNESCO IESALC: 200 institutions / 19 countries, 87 % use AI, only 26 % have any formal framework**, teaching use **74 %**, private non-profit **84 %** > public **68 %**; TALIS 2024 teachers Brazil **56 %** / Chile **55 %** / Colombia **53 %** / Costa Rica **52 %** vs OECD **36 %**; Uruguay **Ceibal 75 %**; UNESCO LAC **Observatory** launched **April 2026**; **IDB TN-3241** | 🟢 all shelved |

🟡 **Canada and Mexico again returned nothing education-specific in this channel** — 🟢 **an informed
gap, stated explicitly, not coverage.** 🟡 **Middle East and Africa likewise returned nothing
education-specific beyond the observation that parts of the region have no AI framework at all**, and
🔴 **the UAE mandate date (`Gap 266`) remains unresolved for a second pass.**

## Opportunities by region — superseded (the live block is at the top of this file)

🟢 **One `###` per region, closed vocabulary (`P265` / `p383-region-heading-gate`). 🔵 Country names
in the prose; the region is the field.** 🟢 **This pass adds one opportunity that is **new and
derived from measurement**, not from the channel: the proctoring licence trap (`P725a`).**

### North America

🟢 **The buyer is a district or state **ordered to produce a policy** with no engineering to
implement it** — Ohio's deadline has passed, Oklahoma's lands before 2027-28.
🟢 **Sell the human-review gate as an auditable artefact**: Oklahoma bars AI from high-stakes
decisions, Illinois requires an **opt-out of AI grading**, NYC bars student-facing generative AI
below grade 9. 🔵 **Each is a *logged decision boundary* — build the log, not the model.**
🟢 **`AB 1159` makes **no-training-by-default** a saleable default**, and its private right of action
makes it a liability control rather than a feature.
🔴 **New this pass — the proctoring licence trap.** 🔴 **`kamlendras/OpenProctor` says MIT in its
README and is **AGPL-3.0** in its payload (`P725a`).** 🔵 **Proctoring is the single most
licence-dangerous category in education software, because AGPL §13 triggers on *hosting* and a
proctoring service is hosted by definition.** 🟢 **A ten-line licence provenance check, run over a
client's existing edtech stack, is a saleable engagement on its own** — and this KB now has the
instrument (`compose/code/p725-readme-payload-sweep/`).
🟡 **Canada and Mexico: nothing in this channel. Informed gap.**

### EMEA

🟢 **The buyer is an institution that will be a *deployer* of a high-risk system with **no**
governance — ~90 % of 450+ institutions have no formal guideline.**
🔴 **`P718` sets the pitch: stop selling "you have until December 2027".** 🟢 **Sell "the date is a
ceiling that harmonised standards can pull forward, and **Article 50 marking is live now** with its
backstop eight weeks out."**
🟢 **Sell the conformity technical file as a deliverable**, with **standards-neutral** evidence
tooling — benchmarks that do not exist yet cannot be coded against, so build the evidence *pipeline*
and leave the criteria pluggable.
🔴 **The proctoring finding lands hardest here.** 🔵 **Remote-exam platforms using facial recognition
or behaviour analysis are squarely Annex III *and* the category where the AGPL trap sits** — so a
single engagement can carry both the conformity file and the licence remediation.
🟢 **And `P734` changes the build recommendation**: if permissive is a hard constraint, **Sakai
(ECL-2.0)** and **Kolibri (MIT)** are the education-native starting points — not a general ERP with
an education layer written from scratch.

### APAC

🟢 **The buyer is a vendor with **extraterritorial exposure it has not modelled**.** 🔴 **Vietnam's
Decision 33/2026/QD-TTg names education high-risk and gives **automated assessment** and
**behavioural monitoring** as its examples** — which is to say, it names *exactly* the two product
categories this shelf tracks.
🟢 **Korea's one-year penalty grace makes 2026 the cheap year to get compliant**, and its
domestic-representative threshold is a **corporate-structure** question, not a software one — flag
it early, because engineering cannot fix it.
🔵 **Vietnam's high-risk trigger is narrow in a useful way (`P706`): it bites where the output is the
**sole basis** without meaningful human review.** 🟢 **So the same human-review gate sold in North
America is the APAC compliance artefact too** — one build, two regulatory markets.
🟢 **Behavioural monitoring being named explicitly makes the proctoring licence check an APAC
opportunity as much as an EMEA one.**

### LATAM

🔴 **The asymmetry is still the whole opportunity: three regions constrain automated assessment by
instrument; LATAM constrains it by nothing while adopting it fastest.** 🟢 **87 % of institutions
use AI and 26 % have any framework — a 61-point governance gap, measured.**
🟢 **The buyer is a university or ministry that has already adopted and has no policy**, and the
sellable artefact is the **framework itself**, not a model: an institutional AI policy, an
AI-grading opt-out, a human-review log, and a staff training path.
🔵 **The public/private split (**68 %** vs **84 %**) says where the budget is and where the need is,
and they are not the same place** — private non-profits adopt faster, public institutions carry more
students.
🟢 **Uruguay's Ceibal (**75 %** of public-school teachers) is the reference deployment to cite in
any public-sector pitch in the region**, and the UNESCO LAC Observatory is the policy counterpart to
align to.
🟢 **`P734` matters most here:** 🔵 **Kolibri is MIT **and offline-first**, which is the correct
technical answer to uneven connectivity across the region** — permissive, education-native, and
built for exactly this constraint.

## 🟢 Fifty-sixth pass, 2026-10-08 — the EU deadline this KB beat the channel on four times is a **ceiling, not a floor**, and that inverts the runway

> 🔵 **This pass's opening hypothesis was that the mandated regional channel would again yield
> instruments already shelved, making the pass a confirmation.
> 🟡 That hypothesis is CONFIRMED for the instruments and REFUTED for their reading.** 🟢 **The four
> regional queries returned nothing this shelf did not hold — but the EU date it holds turns out to
> have a *mechanism* nobody recorded, and the mechanism points the opposite way from the comfort the
> deferral implied.**

### 🟢 `P718` — `2027-12-02` is the **backstop**, not the start, so the Annex III runway is **not guaranteed**

🔴 **The channel claimed, again, that education high-risk duties "apply from August 2026".** 🟢 **This
KB's `2027-12-02` is confirmed correct for the fifth pass running** — August 2026 is the
**pre-Omnibus baseline**, superseded. 🟢 **But the newly measured detail is the conditionality:**

| Element | Reading obtained this pass |
|---|---|
| 🟢 Annex III stand-alone high-risk (where education sits) | **moved `2026-08-02` → `2027-12-02`** by the Digital Omnibus |
| 🔴 **Nature of that date** | 🔴 **an absolute backstop** — *"absolute backstop dates are set regardless … December 2, 2027 for Annex III"* |
| 🔴 **Can it bite earlier?** | 🔴 **Yes** — the deferral is **tied to publication of harmonised standards**; obligations can begin **sooner** if standards publish sooner |
| 🟢 Annex I embedded products | **2028-08-02** |
| 🟢 **Article 50 transparency / marking** | 🟢 **NOT deferred — live since `2026-08-02`**, with the already-deployed backstop at **`2026-12-02`** |
| 🟢 Prohibited practices | enforceable since **2025-02-02** |

🟡 **Sources disagree on whether Official-Journal publication has completed**; one holds that until
it does, `2026-08-02` remains the technical legal baseline. 🔵 **Recorded as a live ambiguity, not
resolved — `api`/EUR-Lex primary text was not reachable from this environment
(`digital-strategy.ec.europa.eu` and law-firm hosts are both egress-blocked).**

> 🟢 **`P718`.** *This shelf has repeatedly read the Annex III deferral as **runway**, and paired it
> with the opportunity that *"harmonised standards are not ready, so standards-neutral evidence
> tooling holds value"*. 🔴 **That opportunity is right and the runway framing is wrong**: the same
> standards whose absence created the deferral are the trigger that **ends** it, so progress on
> standards **shortens** the window rather than extending it. 🟢 **The correct planning assumption is
> "Annex III duties can arrive before `2027-12-02`", and `2026-12-02` Article 50 is unaffected and
> three weeks out.*** 🆕 **`Gap 270`: the OJ publication status is unresolved from this environment.**

### 🟢 Regional measures re-confirmed this pass

🟢 **Four mandated regional queries run. 🔴 **Zero new instruments** — every one returned is already
shelved, which at pass 56 is the correct outcome and is recorded as confirmation:**

| Region | Instruments re-confirmed | Adoption measured |
|---|---|---|
| **North America** | **134 bills / 31 states**; **35+** states with departmental guidance; **Ohio** district AI policy due **2026-07-01**; **Oklahoma SB 1734** (educator supervision, no high-stakes AI, annual parent disclosure, written policy before 2027–28); **California AB 1159** (bars student data for model training, private right of action); **Illinois SB 3735** (family opt-out of AI grading); **Alabama HB 329** (CS+AI required to graduate); US DoE AI grant priority final **2026-04-13** | **NYC**: generative-AI moratorium Pre-K–8, ~**600 000** students, HS AI-literacy required; **Boston**: first major district to mandate HS AI literacy |
| **EMEA** | **EU AI Act** Annex III — 🟢 **`2027-12-02` backstop (`P718`)**, Art. 50 **live**; UNESCO GenAI guidance; **OECD 2026 Digital Education Outlook** (move beyond general-purpose to purpose-built educational AI); UK AI Opportunities Action Plan | 🔴 **only 10 %** of 450+ institutions have formal AI guidelines; Finland / Estonia / Netherlands lead K-12 integration; UK **£4 m** for lesson-planning and marking tools |
| **APAC** | **South Korea AI Basic Act** live **2026-01-22** + enforcement decree (foreign providers need a domestic representative above thresholds); **Vietnam AI law** live **2026-03-01**, extraterritorial, **education among six high-risk sectors** (automated assessment, behavioural monitoring), high-risk **only where output is the sole basis without meaningful human review** (`P706`); **Taiwan AI Basic Act** Dec 2025 | **>50 %** of APAC digital-native businesses still at "repeatable" AI maturity; China / India / Japan lead investment |
| **LATAM** | 🔴 **no binding education-AI instrument anywhere in the region** — Brazil **PL 2.338/2023** in the Chamber, Chile's risk-based executive bill, Colombia **CONPES 4144** (policy-first, budget to **2030**); **IDB TN-3241** argues for enabling regulation | 🟢 **UNESCO IESALC, 200 institutions / 19 countries: 87 % use AI in ≥1 area, only 26 % have any formal framework** (private non-profit **84 %** > public **68 %** > private for-profit **52 %**); TALIS 2024 teachers: Brazil **56 %**, Chile **55 %**, Colombia **53 %**, Costa Rica **52 %** vs OECD **36 %**; Uruguay **Ceibal 75 %** (2026); UNESCO LAC **Observatory** launched **2026-04-14** at ECLAC Santiago |

🔵 **The four-region convergence on assessment (`P705`) holds, and `P718` sharpens its EMEA leg:**
🟢 **three regions constrain automated assessment by instrument, LATAM constrains it by nothing while
adopting it fastest** — and that asymmetry is the whole regional opportunity map below.

## Opportunities by region — superseded (the live block is at the top of this file)

🟢 **One `###` per region, closed vocabulary. 🔵 Country names live in the prose; the region is the
field.**

### North America

🟢 **The buyer is a district or state that has been *ordered to produce a policy* and has no
engineering to implement it.** 🔴 **Ohio's deadline (`2026-07-01`) has passed and Oklahoma's lands
before 2027–28, so the demand is immediate and procedural, not visionary.**
🟢 **Sell: the human-review gate as an auditable artefact.** Oklahoma requires educator supervision
and bars AI from high-stakes decisions; Illinois requires an **opt-out of AI grading**; NYC bars
student-facing generative AI below grade 9. 🔵 **Each of those is a *logged decision boundary* —
build the log, not the model.** 🟢 **`AB 1159`'s bar on training from student data makes
**no-training-by-default** a saleable default, and its private right of action makes it a liability
control rather than a feature.** 🟡 **Canada and Mexico returned nothing in this channel — an
informed gap, not coverage.**

### EMEA

🟢 **The buyer is an institution that will be a *deployer* of a high-risk system and has **no**
governance — 90 % of 450+ institutions have no formal guideline.** 🔴 **`P718` changes the pitch:
stop selling "you have until December 2027" and sell "the date is a ceiling that standards can pull
forward, and Article 50 marking is live now with its backstop on `2026-12-02`."**
🟢 **Sell: the conformity technical file as a deliverable** — Annex III duties attach to systems that
evaluate learners or affect access to qualifications, and a vendor who can hand a client a
pre-assembled technical file plus **standards-neutral** evidence tooling is selling the scarce
thing. 🔵 **Standards-neutral is the operative word: benchmarks that do not exist yet cannot be
coded against, so build the evidence *pipeline* and leave the criteria pluggable.** 🟢 **OECD's
"purpose-built over general-purpose" line is the EMEA procurement argument in one sentence.**

### APAC

🟢 **The buyer is a vendor with extraterritorial exposure it has not modelled.** 🔴 **Korea and
Vietnam both reach foreign providers; Korea additionally requires a **domestic representative**
above revenue thresholds, which is a corporate-structure question, not a software one — flag it
early.**
🟢 **Sell the `P706` lever, which is unique to this region: Vietnam classifies education AI as
high-risk *only where its output is the sole basis for a decision without meaningful human review*.**
🔵 **That makes human review **classification-determining**, not merely a control inside a high-risk
regime — the opposite of the EU, where Annex III status attaches to the use case regardless.** 🟢 **So
in APAC a well-placed, well-logged human-review gate can keep a system **out** of the high-risk tier
entirely; in EMEA the same gate is a requirement *within* it.** 🔴 **Build the gate once, claim
different things with it per region — and never claim the EU benefit.**

### LATAM

🟢 **The buyer is a university with **87 % adoption and 26 % governance** — the widest
adoption-to-governance gap measured anywhere this pass, and the only region with no binding
instrument to anchor a procurement.** 🔴 **That means no compliance deadline to sell against, so
compliance framing fails here.**
🟢 **Sell institutional capability instead: the framework itself** — policy, inventory, review
workflow, teacher-facing guardrails — because **74 %** of institutions must build one and almost
none has staff for it. 🔵 **Segment by control type: private non-profit (84 % adoption) buys
capability, public (68 %) buys through ministries and UNESCO/IDB programmes, private for-profit
(52 %) buys cost reduction.** 🟢 **Entry points are named and funded: UNESCO's LAC **Observatory**
(ECLAC Santiago, since `2026-04-14`), **CONPES 4144** with budget to 2030, Uruguay's **Ceibal**
(75 % teacher use — the most mature public deployment in the region), and **IDB TN-3241**'s
enabling-regulation agenda.** 🔵 **Teacher-side adoption already exceeds the OECD average in four
countries, so the pitch is *govern what is already happening*, not *adopt AI*.**


## 🟢 Fifty-fifth pass, 2026-10-08 — **automated assessment is now constrained in all four regions by four unrelated instruments**, and the region with no rule is the one already doing it

> 🔵 **This pass's opening hypothesis was that pass 54's `P648` grading pipeline was an EMEA+LATAM
> pattern.
> 🟢 It is CONFIRMED and under-stated.** 🟢 **Four regions, four independent legal instruments, one
> engineering requirement** — and the convergence was not visible until the four mandated regional
> queries were read **against each other** rather than filed separately.

### 🟢 `P705` — the four-region convergence on **assessment**, each with its own instrument

| Region | Instrument | Status | What it does to automated grading |
|---|---|---|---|
| **EMEA** | **EU AI Act**, Annex III | 🟡 **2027-12-02** (stand-alone high-risk); Art. 50 marking **live now** | Education is high-risk where AI affects **access, progression or assessment**; conformity assessment required **before** placing on market |
| **APAC** | **Vietnam's AI law** + its 2026 decree | 🔴 **LIVE since 2026-03-01** | Decree names **education among six high-risk sectors**, giving **automated assessment** and **behavioural monitoring** as the examples; **applies to foreign providers** |
| **North America** | **NYC DOE** preliminary guidance (+ Charleston County) | 🔴 **live district policy** | **Red tier bars AI outright** from grading, discipline, promotion and special-education planning; Charleston bars AI as **sole basis** for high-stakes decisions |
| **LATAM** | 🔴 **none specific to education** | 🔴 **absent** | 🔴 **And it is the region already grading with AI at scale** — see `P706` |

🔵 **Why this is one finding and not four.** 🟢 **The instruments disagree on form — a regulation, a
decree, a district memo, nothing — and agree on the object: a grade a machine produced without a
human in the loop.** 🔴 **A studio that treats this as four compliance workstreams will build four
things; it is one architecture.**

### 🟢 `P706` — the **trigger condition** is the lever, and Vietnam states it in the clearest words any of the four use

🟢 **Vietnam's decree flags these systems, per the reading obtained this pass, only where their
output drives decisions *without meaningful human review*.** 🔵 **That is not a caveat, it is the
design specification** — and it is the same hinge as NYC's red tier (AI *may not be* the decider)
and Charleston's *sole basis* language and the EU's *affects access/progression*.

> 🟢 **`P706`.** *In all four regions the risk class is attached to **autonomy**, not to **capability**.
> An AI that **proposes** a grade with a rubric trace, a cited span and a named human approver is a
> different regulatory object from one that **returns** a grade — and the second is the only one
> anyone forbids.* 🟢 **So human-in-the-loop is not a compliance tax on the pipeline; it is the thing
> that moves the pipeline out of the prohibited class in four jurisdictions at once.**

🔴 **And LATAM is where this bites hardest, because the exposure is inverted from the regulation.**
🟢 **UNESCO IESALC, 200 institutions across 19 countries:**

| Measure | Value |
|---|---|
| Institutions using AI in ≥ 1 area | 🔴 **87 %** |
| Of those, with a **formal framework** | 🔴 **~25 %** |
| Using it in teaching & learning — explicitly incl. **grading assessments** | 🔴 **74 %** |
| Private **non-profit** / **public** / private **for-profit** adoption | **84 %** / **68 %** / **52 %** |

🔵 **Read with `P705`: the one region with no assessment rule is the one where three quarters of
institutions already grade with AI and one quarter have any governance.** 🟢 **That is the clearest
commercial opening in this file, and it is a *governance* engagement before it is an AI one.**

### 🟢 Regional measures recorded this pass

🟢 **Teacher-level AI use, OECD TALIS 2024 (OECD average **36 %**):** Brazil **56 %**, Chile **55 %**,
Colombia **53 %**, Costa Rica **52 %** — 🟢 **every LATAM country measured is above the OECD average.**
🟢 **Uruguay, Ceibal 2026: 75 %** of public-school teachers. 🔵 **Country in the prose, region in the
field, per the closed vocabulary.**

🟡 **EMEA, from the regional channel:** European AI-in-education market **$2.64 B** in 2026;
**Finland, Estonia, Netherlands** lead K-12 integration; UK **£4 M** into lesson-planning and
marking tools; 🔴 **only 10 %** of 450+ institutions surveyed have formal AI guidelines. 🔵 **Vendor
and market-data pages — directional, and labelled as such.**

🟢 **EMEA / Middle East & Africa — ministry-level, and the first substantial MEA material this KB has
carried** (`P707`):

| Country | Measure |
|---|---|
| **Saudi Arabia** | 🟢 AI curriculum live in **2025-26** for **6 M+** general-school students; built by the National Centre for Curriculum + Ministry of Education + MCIT + **SDAIA**, which also issued generative-AI guidance for general education |
| **UAE** | 🟢 **Standalone subject** from **2026-27**: *Artificial Intelligence and Technology*, merging Design, Innovation & Computer Science with the AI curriculum across all three cycles; **7 domains**; **22 000** teachers to be trained; 🟢 **no written exams — assessment is practical** |
| **Ghana** | 🟢 AI, coding and programming into the **national curriculum, KG → junior high** |
| **Rwanda** | 🟢 AI and data-science curricula at **secondary** level, under the Smart Rwanda Master Plan |
| **Kenya** | 🟢 Digital-literacy programme expanded; coding and CS into primary and secondary |
| **South Africa** | 🟡 **Draft National AI Policy 2026** — STEAM curricula and community AI centres |
| **Continental** | 🟢 **AU Continental AI Strategy** (adopted July 2024) + **2025 Africa Declaration on AI** |

🔵 **The UAE detail worth keeping next to `P705`:** 🟢 **the one jurisdiction that made AI a
mandatory school subject chose to assess it *without written exams*** — a state deciding that this
subject is demonstrated rather than tested, while four other jurisdictions restrict machines from
doing the testing.

🟢 **North America — the legislative picture, US-centric by the channel's own admission:** 35+ states
carry official education-department AI guidance; **Ohio** is the first state to require **every
district** to adopt an AI-use policy (by **2026-07-01**); **Oklahoma SB 1734** requires written
district policies before 2027-28; **California AB 1159** would bar training models on student data;
**Idaho SB 1227** mandates privacy protections; **Oregon SB 1546** targets compulsive-use design for
minors; **Alabama HB 329** makes an AI-inclusive CS course a graduation requirement; **Boston**
mandated AI literacy for all high schoolers. Federally: an Education Department grant priority was
finalised **2026-04-13**, and the **K-12 AI Literacy and Readiness Act (H.R. 8747)** advanced in
committee **2026-07-21** — 🔴 **not enacted.**

🔴 **Two bill counts, irreconcilable, and both recorded rather than averaged:** one tracker says
**68 bills across 27 states, 10 enacted in 2026**; another says **134 bills across 31 states**.
🔵 **`P469` applies — neither is adopted as this KB's number, and the disagreement is the datum.**

🟢 **APAC regulation, ranked by how binding:** **China** (binding rules on algorithms, deep synthesis,
generative AI) → **Vietnam** (AI law **2026-03-01**, education high-risk) · **South Korea** (**AI Basic
Act, in force 2026-01-22** with its enforcement decree; non-Korean providers may need a **domestic
representative** above revenue/user thresholds) · **Taiwan** (AI Basic Act, Dec 2025) → **Singapore**,
**Japan** (voluntary guidelines on existing law) → **Australia**, **New Zealand** (light-touch;
Australia's **AI Safety Institute** expected operational early 2026). 🟡 **Named APAC market players:
Google, Microsoft, IBM, Pearson, Byju's; China, India and Japan reported as dominating.**

## Opportunities by region — superseded (the live block is at the top of this file)

### North America

🟢 **The opening is the policy mandate, not the model.** Ohio requires **every** district to have an
AI-use policy and Oklahoma requires one before 2027-28 — 🟢 **thousands of districts must produce a
governed artefact, and NYC's red tier shows what a defensible one looks like.** 🔵 **Sell the
policy-plus-pipeline pair:** an assessment workflow whose human-approver step is the thing that
satisfies the district's own policy. 🟡 **Second opening: AI-literacy curriculum delivery**, which
Alabama's graduation requirement and Boston's mandate turn into procurement.

### EMEA

🟢 **Two distinct markets, and conflating them loses both.** 🟢 **In the EU the product is the
conformity file**: Annex III bites **2027-12-02**, and a vendor that can hand a client the technical
documentation, the rubric trace and the Art. 50 marking **already live** is selling readiness on a
known date. 🟢 **In the Gulf the product is delivery at national scale** — Saudi's 6 M students and
the UAE's 22 000-teacher training programme are **implementation** contracts, and the UAE's
no-written-exams choice means **practical-assessment tooling**, not test banks. 🟡 **In Africa the
opening is earlier and cheaper**: Ghana, Rwanda and Kenya have curriculum mandates without the
platform layer beneath them, and South Africa's policy is still in draft — 🔵 **influence is
available at the standards stage, which it no longer is in the EU.**

### APAC

🟢 **The highest-urgency region, because Vietnam's rule is live *now* while the EU's is fourteen
months out.** 🟢 **Any client serving Vietnamese learners with automated assessment or behavioural
monitoring is in scope today, foreign incorporation notwithstanding** — and `P706`'s human-review
trigger is the remedy. 🟢 **Korea adds a structural, non-technical deliverable**: the domestic-
representative requirement above revenue/user thresholds is a market-entry checklist item.
🔵 **Build the pipeline once against Vietnam's decree and the EU file is mostly written** — the two
instruments name the same object.

### LATAM

🟢 **The strongest opening in this file, and it is governance-first** (`P706`): **87 % adoption
against ~25 % frameworks**, with **74 %** of institutions already using AI on assessment. 🟢 **The
sellable unit is the framework plus the auditable grading pipeline**, in that order — the demand
already exists and the governance does not. 🟡 **Regulation is coming and is risk-based, so the work
is not wasted:** Brazil's **PL 2.338/2023** passed the Senate **2024-12-10** and sits in the Chamber
of Deputies (text can still change), Chile has a government-sponsored risk-based bill, and Colombia
runs **CONPES 4144** (Feb 2025) with budget through **2030**. 🟢 **Institutional entry points are
named and active:** UNESCO's **Observatory on AI in Education for LAC** (launched 14 April, hosted
with ECLAC), UNESCO IESALC, and the **IDB** (technical note **IDB-TN-3241**), which warns that
national-only approaches fragment a **650 M-person** market. 🔵 **Adoption skews private non-profit
(84 %) over public (68 %)** — that is the segment with budget and without a framework.

### Global

🟢 **Market frame, unchanged and still consistent across sources:** AI-in-education **$10.6 B**
(2026) → **$42.48 B** (2030), **41.5 % CAGR**. 🟡 **The cross-cutting trend both the OECD's 2026
Digital Education Outlook and the trend channel name is the move from general-purpose AI to
purpose-built education AI with durable learning gains** — 🔵 **which is the same argument as
`P706` from the pedagogy side: provable, traceable output beats capable output.** 🔴 **Governance is
the global gap, not capability: 86 % of education organisations use generative AI and most have no
policy**, and the EMEA survey's **10 %-with-guidelines** figure is the same hole measured elsewhere.

## 🟢 Fifty-fourth pass, 2026-10-08 — the regional channel yields **real national material in EMEA** for the first time in four passes, and the KB beats the channel on the AI Act date for the fourth

> 🔵 **This pass's opening hypothesis was that EMEA's thin regional yield was a property of the
> region's reporting. 🔴 REFUTED — it was a property of the query.** 🟢 **The mandated regional form
> (`AI education EMEA 2026 adoption regulation players`) returns enterprise-AI commentary because
> *EMEA* is a vendor's sales region, not a term education ministries use about themselves.** Asking
> by **country** returned four national frameworks in one search.

### 🟢 `P646` — the channel returned a **stale** AI Act date; this KB's record stands and is finer

🔴 **One of this pass's searches returned:** *"General obligations take effect on August 2, 2026, and
high-risk systems on August 2, 2027."* 🔴 **That is wrong, and it is wrong in the direction that
would cost a client a year of planning.**

| | Channel this pass | 🟢 This KB's held record |
|---|---|---|
| Annex III **stand-alone** high-risk (where education sits) | 🔴 *"2 Aug 2027"* | 🟢 **2027-12-02** |
| Annex I **embedded** high-risk | — | 🟢 **2028-08-02** |
| Art. 50 transparency / marking | — | 🟢 **2026-08-02 — live now** |
| Instrument | — | 🟢 **Reg. (EU) 2026/1744**, omnibus in force **2026-07-27** |

🟢 **Fourth consecutive pass the channel is behind this KB on this date**, and the second where it
supplied a *specific wrong* date rather than vagueness. 🔵 **Recorded as a channel-quality datum, not
a correction to the file** — the live block was already right, and `P469` says say so rather than
re-derive it. 🟡 **A second search this pass independently confirmed the KB's reading** (*"Annex III
stand-alone high-risk systems … now have until 2 December 2027"*, Digital Omnibus law
**2026-06-29**), so the conflict is between two secondary sources and the KB sides with the one that
matches the Regulation it already cites.

### 🟢 `P647` — the regional channel, counted name by name: **6 of 20**

🟢 **All four mandated regional queries were run, plus four sharper ones.** 🔴 **20 named
instruments, bodies, repos and figures came back; 6 had zero prior reference in this KB.**

| New to this KB | Cell |
|---|---|
| `emorynlp/LLM-Grading`, `wenjing1170/llm_grader`, **Autorubric**, **AutoSCORE** | 🟢 assessment / scoring |
| **Noodle Factory** (SG), **Codestral-22B** grading result | 🟡 APAC vendor, open-weight scoring |

🟢 **The six cluster into one layer — assessment — which is why one pass could close it.** 🔵 **A
clustered yield is more actionable than a scattered one of the same size.**

## Opportunities by region — superseded (the live block is at the top of this file)

### North America

🟢 **Measured position.** Market **$951 M (2024) → $2.30 B (2029)**, **15.9 % CAGR** (one firm);
a second firm projects **45 % CAGR 2025–2030** for the same geography. 🔴 **The two disagree by a
factor of three — both are published as directional, neither as a plan input.**

🔴 **The gap that is the opportunity:** **10 %** of institutions have formal AI guidelines and
**71 %** of US teachers report no AI training. 🔴 **And there is no sectoral regulator** — the
channel's own framing, *"no equivalent to the FDA exists for educational technology"* — so adoption
is decided school-by-school and district-by-district with minimal external oversight. **FERPA** plus
state law is the whole governing frame.

🟡 **Regulatory direction is contested, which is itself the sellable fact.** A **December executive
order** directs the Attorney General to challenge state AI laws conflicting with a *"minimally
burdensome national policy framework"*; the channel's read is that its effect unfolds slowly because
it works through litigation and funding rather than pre-emption, leaving **states as the primary
drivers**. Named: **Texas TRAIGA**, **New York RAISE Act** (neither education-specific).

🟢 **Globant opportunity.** **AI-governance scaffolding as a product**, not a policy deck: a district
or system can adopt a guideline template, an inventory of which tools touch admissions / grading /
proctoring, and a teacher-training track. 🟢 **The 10 % / 71 % pair is the business case** and both
numbers are the client's own sector. 🟢 **`P640`'s rubric layer is directly useful** — a district
defending a grading decision needs a *stated* rubric with bias mitigation, which Autorubric provides
under MIT.

🔴 **Declared gap:** the channel named **no** North American edtech vendors by name beyond
conference and research-firm references (ASU+GSV Summit). 🔴 **Vendor market share in this region is
unmeasured in this KB**, and two single-source claims (Boston Public Schools AI-literacy mandate;
Maryland and Oklahoma restricting AI-made high-stakes decisions without human oversight) come from
**one unofficial digest** and are **not shelved as facts**.

### EMEA

🟢 **The gap pass 53 declared is narrowed, and by changing the query rather than waiting a week.**
🔴 **The mandated `EMEA` form returned enterprise-AI commentary again** (Workday 2023, CompTIA's
US-respondent 2026 outlook, a Bandwidth-Cavell enterprise report) — 🔴 **zero education-specific
2026 data, fourth pass running.** 🟢 **Asking by country returned four national frameworks at once:**

| Country | Instrument | Status, as read this pass |
|---|---|---|
| 🇬🇧 **England** | **DfE** AI guidance for schools | 🟢 live; modules **updated 2026-05-19**; **GenAI product safety standards updated Jan 2026** (a procurement reference); roadmap claims AI tutoring could reach **450 000** disadvantaged pupils |
| 🇫🇷 **France** | Ministry **framework on AI use** (Jun 2025) | 🟢 live; students **4e and above** may use AI autonomously in class; ministry developing a **sovereign AI** for teachers. 🔴 **A formal national plan was due Spring 2026 — unconfirmed whether published** |
| 🇳🇱 **Netherlands** | 🔴 **no ministry-level school guidance found** | 🟢 **NOLAI** (government + academia + industry + schools co-designing educational GenAI) is the national vehicle; **TU Delft**'s institutional rule is *"using AI is permitted, unless"* — per-course declaration, undisclosed use treated as fraud |
| 🇩🇪 **Germany** | **DigitalPakt 2.0** (to **2030**) + *AI in Higher Education Strategy* | 🟡 framed as **funding**, not pedagogy guidance; Germany has established an **AI Safety and Security Institute** |

🟢 **Cross-cutting:** **OECD *Digital Education Outlook 2026*** (published Jan 2026) is the regional
baseline document; a law-firm reading holds that universities are obliged to develop internal AI
guidelines, train staff and set up expert committees under the AI Act. 🟡 **That is a legal
interpretation, flagged as such.**

🟢 **Globant opportunity.** 🔴 **The four countries have four different shapes** — England regulates
**procurement** (product safety standards), France builds **sovereign tooling**, the Netherlands
works through **co-design consortia**, Germany moves **money**. 🟢 **So the EMEA engagement is not one
offer: it is Annex III conformity work with a known deadline (`2027-12-02`) plus a country-shaped
delivery route.** 🟢 **Art. 50 marking is live now (2026-08-02)**, so disclosure and AI-content
labelling is immediate, billable work regardless of the high-risk deferral.

🟢 **`P640` lands here hardest.** 🔴 **Annex III names assessment**, and an Annex III technical file
needs a per-component licence line plus a documented, bias-mitigated scoring method. 🟢 **Autorubric
(MIT) supplies the second and `P643`'s first-hand grants supply the first** — including the warning
that `education-agent-skills` is **CC-BY-SA-4.0** and cannot be vendored into a conformity artefact
(`Gap 262`).

🔴 **Declared gap, unchanged:** no EMEA EdTech **vendor market share** figures, and no 2026 adoption
*rate* for EMEA schools or universities — only frameworks. 🟢 **Frameworks found, adoption not.**

### APAC

🟢 **The region's most useful 2026 datum is a reversal, and it is a warning rather than an
opportunity.** 🔴 **South Korea's AI digital textbook programme was dismantled**: planned for most
subjects by 2028, scaled back late 2024 (Korean and home economics dropped; social studies and
science deferred to 2027), adopted by only **~30 %** of elementary schools in year one, then
**removed from the national curriculum** by legislation and **reclassified as "supplementary
materials"**, leaving schools and vendors **without funding**. 🟡 **Sources differ on the exact legal
mechanism** (an amended 2024 law that had earlier been vetoed) and **no reliable 2026 status report
was found** — so the 2025 reversal is the latest confirmed state.

🟢 **Singapore is the opposite posture and the better reference.** **MOE** states an *"intentional,
age- and developmentally-appropriate"* approach: **lower primary stays print-first**, AI introduced
gradually. In **Feb 2026** the Education Minister said the ministry **lacks Singapore-specific data**
linking AI use to learning outcomes and is studying it. A **2026-05-06** parliamentary question
asked about introducing AI from **Primary 4** under *"low exposure"* with close teacher supervision.
MOE's own tools sit in the **Singapore Student Learning Space**, with stated safeguards against
overreliance. 🟡 **Two further claims are secondary and unverified against MOE:** a **Teacher AI
Literacy Roadmap** making one module compulsory by end-2026 (two more encouraged by end-2027), and
**AI competency modules compulsory across universities, polytechnics and ITE by 2027** — the latter
reported by **Noodle Factory**, a Singapore vendor, and 🔴 **not confirmed on MOE's site.**

🟡 **Commercial and governance context:** **Pearson + TCS** multi-year AI learning alliance (global,
not APAC-specific); **LearnUpon** APAC expansion with a Sydney HQ and *Create+* AI course authoring;
**Alteryx** Academy relaunch with personalised AI learning paths; **NIIT MTS** citing AI-led design.
**57 %** of Asian organisations have AI in at least one operational area while **governance frameworks
lag** (Diligent Institute). **OpenAI** appointed an ANZ policy lead as Canberra tightens AI
governance and copyright rules. 🔵 **Regional expectation is harmonised principles — safety,
transparency, accountability — executed per market.**

🟢 **Globant opportunity.** 🟢 **Korea's reversal is the asset**: it is a documented, publicly-funded
failure of a **device-and-textbook-first** rollout, and the lesson sells the alternative — start from
**teacher workload and assessment**, keep the learner surface conservative, and prove outcomes before
scaling. 🟢 **Singapore's stated evidence gap ("we lack data linking AI use to outcomes") is a
measurement engagement**, which is the cheapest credible way into a cautious ministry and is exactly
what a rubric layer with calibration and bias mitigation (`P640`) is for.

🔴 **Declared gap:** the mandated APAC query returned **no education-specific regulation** — no
ministry curriculum rules, no student-data provisions. 🟢 **Every education datum above came from the
sharper country-level query, not the mandated regional one** — the same `P647` effect as EMEA.
🔴 **China and India returned nothing in any search this pass**, and that is a gap, not coverage.

### LATAM

🟢 **The best-measured region this pass, and the only one with a primary multi-country study.**
**UNESCO IESALC**, with UNU-IAS: **200 higher-education institutions across 19 countries**, surveyed
**Aug–Oct 2025**. 🔴 **The headline is a governance gap, not an adoption gap:** **87 %** of
institutions use AI in at least one area while only **26 %** have **any formal AI framework**.

🟢 **Where it is used:** teaching and learning **73.5 %**, research **57.0 %**, administration
**34.1 %**, community engagement **20.0 %**. 🟢 **Adoption by institution type:** private non-profit
**84 %**, public **68 %**, private for-profit **52 %**.

🟢 **A second, independent sample agrees on the shape.** The **Digital Education Council** LATAM
survey (with **Tecnológico de Monterrey** and its Institute for the Future of Education): **92 %** of
students and **79 %** of faculty actively engaging with AI, and a **sharp asymmetry on assessment** —
**50 %** of students support AI-assisted feedback on assignments while only **19 %** of faculty use
AI that way. 🟡 **A third figure conflicts mildly:** Tec de Monterrey's coverage quotes *"only 30 % of
universities in Latin America have published policies"* against UNESCO's **26 %** for formal
frameworks. 🟢 **Both published, neither reconciled — they measure slightly different objects.**

🟡 **Regulation is uneven and nowhere education-specific.** 🔴 **No unified regional framework.**
**Chile** leads with a **National AI Policy since 2021** and a bill under discussion (🔴 **current
status of that bill not found this pass**); **Brazil** and **Colombia** have advanced national
strategies **without education-sector regulation**; **Mexico**'s guidance from **SEP**, **ANUIES**
and the Observatorio IA is **non-binding**. The **IDB** publishes on balancing rights, innovation and
sovereignty, and its **ILIA** index tracks readiness, adoption and governance across **19 countries**.

🟢 **Globant opportunity.** 🟢 **The 87 % / 26 % pair is the sharpest engagement hook in any region
this pass**: the technology is already in use, so the sale is **governance retrofitted onto live
deployments** — an AI-use inventory, a published institutional policy, and an assessment pipeline
whose scoring is defensible. 🟢 **The 50 % / 19 % assessment asymmetry names the wedge precisely:**
students want AI feedback and faculty will not give it, and the blocker is defensibility, not
appetite. 🟢 **That is `P640` deployed as a product** — a rubric service with documented position- and
verbosity-bias mitigation, under MIT, that a faculty member can stand behind. 🔵 **And LATAM has no
Annex III deadline forcing it**, so the driver is institutional trust, which favours a transparent
open-source scoring layer over a vendor black box.

🟢 **Named, reachable counterparties:** UNESCO IESALC, UNU-IAS, IDB, Digital Education Council,
Tecnológico de Monterrey, UNAM, UPC (Peru), Pontifical Catholic University of Chile, ANUIES.

### Global

🟢 **Market, with its spread published rather than a single number:** AI-in-education is put at
**$10.6 B (2026)** growing **40.9 %** from $7.52 B in 2025 by one firm; **$11.4 B (2026) → $57.2 B
(2033)** by another; and **$6.4 B (2025) → $79.6 B (2034)** by a third. 🔴 **Three firms, three bases,
three trajectories — the disagreement is the datum.** 🟢 **AI tutors specifically: $1.63 B (2024) →
$7.99 B (2030), 30.5 % CAGR**; cloud deployment led 2024, **K-12 is the largest share**, language
learning the fastest-growing segment.

🟡 **Student adoption, reported globally but probably UK-sourced:** **66 % (2024) → 92 % (2025)**.
🔵 **The same 92 % appears in the LATAM survey for students**, which is either convergence or one
figure travelling — 🟢 **flagged, not merged.**

🟢 **The structural finding this pass adds (`P641`):** the assessment layer's **research** channel is
busy — AAAI, COLM, four arXiv preprints in this window — while its **licensed** channel holds
**one** library. Open-weight models are already competitive at the task (**Codestral-22B** reaches
**85 %** micro-accuracy against instructor rubrics on code **with no fine-tuning**; a 2026 paper
reports **88.56 %** per-criterion accuracy and **0.78** Pearson on UML diagrams **using only
open-source models**). 🔴 **So capability is not the constraint and licensing is.** 🟢 **That is a
global opportunity with a regional deadline attached in EMEA.**

### 🔴 Declared gaps — stated so silence is not mistaken for coverage

🔴 **No education agent originated in EMEA, APAC or LATAM** appeared in any of this pass's eight
searches — **fifth consecutive week.**
🔴 **No vendor market-share data** in any region.
🔴 **No EMEA 2026 adoption *rate*** — frameworks found, adoption not.
🔴 **No education-specific APAC regulation** from the mandated query; **China and India returned
nothing at all.**
🔴 **No 2026 status** for South Korea's post-reversal position, France's Spring 2026 plan, or Chile's
AI bill.
🔴 **No star counts anywhere this pass** — `github.com` and `api.github.com` both `403`.
🔴 **No instrument was run** (`Gap 261`): the sandbox denied executing this repository's code, so
every verdict is a direct measurement or a static reading, never a suite result.

## 🟡 Fifty-third pass, 2026-10-08 — the regional channel yields **2 of 42**, both second-hand by force; and this file's supersession marker was being applied to the blocks nobody scrolls to

> 🔵 **This pass's opening hypothesis was that the AI-omnibus deferral might still be mis-stated
> somewhere live in this file. 🔴 REFUTED — the live block is correct and was correct before this
> pass.** 🟢 **What the check did find is `P636`: the marker that tells a reader which block is
> live was missing from the one block that competes with it.**

### 🔴 `P636` — of 27 `## Opportunities by region` blocks, exactly **two** were bare: the live one and the one directly beneath it

🟢 **Measured, heading by heading — and the first count this pass made was wrong, so the method is
recorded with the result.** A sweep that treated every heading without the word *superseded* as
unmarked reported **16 unmarked**. 🔴 **That was an artefact**: 13 of those carry a
self-identifying suffix (`— thirty-third-pass update, 2026-10-07`, `— twenty-third-pass
additions`, …) and cannot be read as current. 🟢 **Re-measured by suffix:**

| Heading suffix, before this pass | Count | Readable as live? |
|---|---|---|
| `— superseded (the live block is at the top of this file)` | **12** | 🟢 no |
| a pass number and/or date (`— thirty-sixth-pass update, 2026-10-07`, …) | **13** | 🟢 no |
| 🔴 **bare — nothing at all after the heading** | 🔴 **2** | 🔴 **yes, both** |

🔴 **And the two bare ones were the live block and pass 51's, adjacent.** 🟢 **So the defect was
not "most of this file is unmarked" — it was the sharper thing: the *only* two headings a reader
cannot tell apart were the current one and its immediate predecessor.** 🔵 **This is `P582`'s class
— a *positional* defect in an append-only file, not a status error** — and the remedy is the same:
a marker at the point of competition, never a rewrite.

🔵 **`P469` is why the corrected count is published instead of the first one**: a number asserted
from a convenient sweep is not measured.

🟢 **Landed this pass:** pass 52's and pass 51's blocks are both now marked `— superseded`, so
**exactly one bare `## Opportunities by region` heading exists in this file, and it is the live
one.** 🟢 **Verified after the edit**: 28 blocks, 14 superseded, 13 pass-labelled, **1 bare.**

### 🟡 `P637` — the regional channel, counted name by name: **2 of 42**

🟢 **All four mandated regional queries were run.** 🔴 **42 named instruments, bodies and figures
came back; 2 had zero prior reference in this KB.**

| Region | New to this KB this pass | Verdict |
|---|---|---|
| **North America** | 🔴 **none of 14** | saturated |
| **EMEA** | 🔴 **none of 11** | saturated |
| **APAC** | 🟡 **1 of 9** — *Australian AI Safety Institute*, announced **2025-11** | near-saturated |
| **LATAM** | 🟡 **1 of 8** — Brazil's ***`ConectAI`***, Microsoft-funded, 26 partners, target **5 M** learners by end **2027** | near-saturated |

🔴 **Neither is first-hand and neither can be**: every non-GitHub host answers `000` in this
environment, and `github.com` HTML answers `400` to a `HEAD`. 🟢 **Both are recorded as
second-hand with the channel's own date, and neither is promoted to a shelf row.**

🟢 **The more useful result is a falsification that failed.** On the two dates this KB has been
burned on before, the channel reported them **less** precisely than this KB already holds them:

| | Channel said | This KB holds | |
|---|---|---|---|
| EU high-risk education | *"August 2026"* in older guides; *"2 Dec 2027 / 2 Aug 2028"* in current ones | **2027-12-02** stand-alone, **2028-08-02** Annex I, Art. 50 live **2026-08-02** | 🟢 **KB correct, and finer** |
| Korea | *"one-year grace period, 2026 a pilot year"* | Act **2026-01-22**, decree **2026-07-21**, fines deferred ~**2027-07-21**, 🔴 **labelling duty with no grace at all** | 🟢 **KB correct, and finer** |

🔵 **A channel this KB has out-measured is a channel to run for falsification, not discovery.**

## Opportunities by region — superseded (the live block is at the top of this file)

🔵 **One `###` per region, the five-value closed vocabulary, and the country in the prose rather than
in the field.** 🔴 **Each opportunity below names the licence constraint that decides whether it can
be delivered**, because `P631` (`verticals/solutions.md`) measured that this shelf is **never both
permissive and educational**.

### North America

🟢 **The opportunity is compliance plumbing, not tutoring, and it is unchanged this pass.**
🔴 **134 bills across 31 states**, with OK and MD banning AI from high-stakes decisions about
students, CA **A.B. 1159** restricting training on student data, ID **SB 1227** mandating a
statewide framework, and OH obliging **every district** to hold a formal AI policy from
**2026-07-01**. 🟢 **A district cannot buy one product that satisfies 31 statutes, so the
deliverable is a policy-parameterised layer**: `grant-mccurdy/instructional-ai-workflows` (MIT,
🟢 **re-verified reachable this pass**) supplies the human-review-at-every-stage shape the OK/MD
oversight rules require.
🆕 **New this pass, and it is a counter-signal worth selling against:** the restriction trend is
real — **NYC's one-year pause on student-facing AI through grade 8** is being copied (Nebraska),
so 🔵 **the K-8 pitch is teacher-facing tooling and governance, never student-facing tutoring.**
🔵 **Pitch against the 60 % of US K-12 teachers already using AI informally** (32 % weekly) — the
gap is governance, not adoption. 🔴 **Federal timing stays a watch item:** H.R. 8747 cleared
committee **2026-07-21** and is **not** enacted.
🔴 **Constraint: if the client's SIS is ERPNext or Moodle, the AI runs *beside* it as a side-car,
never linked in.**

### EMEA

🟢 **The opportunity is Annex III conformity work with a known deadline.** Education sits in the
**stand-alone high-risk** class deferred to **2027-12-02** (Annex I, embedded in regulated
products: **2028-08-02**), which is far enough out to build properly and close enough to sell now.
🔴 **Article 50 transparency already applies (2026-08-02)**, and AI Office enforcement began the
same day, so marking and disclosure is immediate work. 🔵 **The deferral came from the *AI omnibus*
(in force 2026-07-27), which is why four independent secondary channels have quoted the superseded
August-2026 date** — 🟢 **a client who scoped to the old date is over-spending by 16 months, and
that is a conversation opener.**
🟢 **Only 10 % of 450+ institutions have formal guidelines** — that is the addressable gap.
🟢 **`P634` is directly useful here:** an Annex III artefact needs a per-component licence line, and
this KB's gate can now derive **`LGPL-2.1` vs `LGPL-3.0`** instead of recording a family — 🔴 **the
distinction an auditor asks about when the SIS is `openeducat`.**
🔵 **The UK is a different sale**: its instrument is the *AI Opportunities Action Plan*,
principles-based, so the deliverable there is **assurance** rather than conformity.
🔴 **The EMEA permissive-education gap is unchanged:** the one EMEA-origin higher-ed assessment
framework on any shelf here (`macsnoeren/genai-open-assessment`, NL) is **GPL-3.0**.

### APAC

🟢 **Vietnam remains the sharpest single opportunity this KB holds, in any region.** Its AI law
(passed **2025-12-10**, effective **2026-03-01**) names education among six high-risk sectors and is
explicit about **automated assessment and behavioural monitoring** — and treats a system as
high-risk *only where its output is the sole basis for a decision without meaningful human review*.
🟢 **That is a statutory description of an architecture**, and it is the one
`grant-mccurdy/instructional-ai-workflows` implements. 🔵 **Education's compliance date is
**2027-09-01***, grouped with health and finance — 18 months later than general application, which
is the runway.
🔵 **Korea is the second sale**: Framework Act in force **2026-01-22**, enforcement decree
**2026-07-21**, and fact-finding investigations and administrative fines deferred roughly to
**2027-07-21** — 🔴 **but the generated-content labelling duty has no grace period at all**, so
marking is work today. 🔴 **Korea requires a domestic representative for foreign providers**, a
structuring question before a technical one.
🆕 **New this pass:** the **Australian AI Safety Institute** (announced **2025-11**) alongside the
**National AI Plan** (**2025-12**) — 🔵 **an assurance-shaped counterpart to the UK**, recorded
second-hand.
🔴 **Declared gap, unchanged: no APAC school-level *adoption* rate.** Ministry-level policy for
China, India and Japan returned nothing measurable this pass; the one APAC maturity figure
(>50 % at *"repeatable"*) is about businesses, not schools. 🟢 **Named rather than back-filled.**

### LATAM

🟢 **The opportunity is the governance gap, measured.** UNESCO IESALC: **87 %** of 200 institutions
across 19 countries use AI in at least one area, **74 %** in teaching — but **only ~25 % have a
formal AI framework**. 🔵 **TALIS puts LATAM teacher adoption far above the OECD average** (Brazil
56 %, Chile 55 %, Colombia 53 %, Costa Rica 52 % vs **36 %**), and Ceibal reports **75 %** of
Uruguayan public-school teachers using these tools. 🔵 **Adoption also splits by institution type**
— 84 % private non-profit, 68 % public, 52 % private for-profit — 🟢 **so the buyer with budget and
the buyer with the gap are not the same institution.**
🔴 **Adoption is not the problem here; almost nobody has written the rules.** 🟢 **So the
deliverable is an institutional AI framework plus the technical controls that make it auditable**,
composing with **Latam-GPT** (via UNESCO–CENIA) and the Observatory's partner network (CAF, CENIA,
CETIC.br, ECLAC, Tec de Monterrey, ProFuturo, Ceibal, Fundación Santillana).
🆕 **New this pass:** Brazil's **`ConectAI`** — Microsoft-funded, 26 official partners, target
**5 M** learners by end **2027**, 🔵 **a skilling channel rather than a procurement channel, and so
a route to practitioners rather than to budget.** Recorded second-hand.
🔴 **Regulation is still pending everywhere that matters** — Brazil's **PL 2.338/2023** is in the
Chamber, Chile's bill in first constitutional stage, Colombia's **CONPES 4144** a programme to 2030
rather than an obligation — 🟢 **which means a framework built now is a differentiator, not a
compliance cost.**

### Global

🟢 **Cross-region, the one thing every channel agreed on: the market is moving from experimentation
to governance.** 🔵 **Market figures, with their disagreement published rather than averaged:**
$10.6 B → **$42.48 B by 2030 at 41.5 % CAGR** (Research and Markets); **$12.3 B by 2026** (HolonIQ);
**$136.79 B by 2035** (Azumo); North America **$3.68 B → $32 B by 2030** (36 % of the global market);
EU **$2.64 B → $8.0 B by 2030 at 31.9 % CAGR**. 🔴 **These rest on different definitions and are not
reconcilable** — quoted as a range, never as a point.
🟢 **The durable, licence-independent demand across all five regions is the same: purpose-built
education AI with a human in the loop and an audit trail**, which is why `P632` and 🆕 **`P637`**
(`compose/patterns.md`) wire exactly that — the second one so the audit trail's licence column is
derived twice and independently.

### 🔴 Declared gaps

- 🔴 **No instrument in this file is first-hand this pass, and none can be** — all non-GitHub egress
  is `000` and `github.com` HTML is `400`.
- 🔴 **No APAC education *adoption* rate was found**, for the fifth consecutive pass.
- 🔴 **No LATAM instrument has been enacted**, so the region's regulatory column is still
  forward-looking in every country this KB tracks.
- 🟡 **The IESALC formal-framework figure is held as `~25 %` here and reported as `26 %` by this
  pass's channel.** 🔵 **Recorded as a ±1 pp disagreement rather than silently overwritten** — the
  primary study could not be re-read first-hand (`000`).

## 🟡 Fifty-second pass, 2026-10-08 — the regional channel yields **2 instruments and 2 bodies out of 51**, which is the first non-zero yield in five passes, and every one of them is **second-hand by force**

⏱️ **Sixth pass of this date.** Four regional queries ran verbatim, one per region. **Every named
instrument was checked term by term against the tree before being called new.** No star counts
(`P479`).

### 🔴 Channel integrity, stated before any figure

🔴 **Every non-GitHub host measured `000` at the egress proxy this pass** — `gov.uk`, `unesco.org`,
`creativecommons.org`, `multistate.us` — and `WebFetch` returned `EGRESS_BLOCKED` by name for
`multistate.us`. 🟢 **`raw.githubusercontent.com` and `git ls-remote` answer 200.** 🔴 **So no
instrument below is first-hand, and none can be made first-hand from this environment.** It is
recorded as a channel limit, not as a confidence level: a legislature's own bill page was *attempted*
and is unreachable, which is different from not having been tried.

### 🟡 The regional yield, with its denominator

🔵 **Denominator stated, because `intel/trends.md` publishes a different one for this same channel:**
this table counts **instruments, bodies *and* market/adoption figures** (**51** = 16 + 12 + 10 + 13);
`intel/trends.md` counts **instruments and bodies only** (**42**), excluding the **9** market and
adoption figures (NA 2, EMEA 2, APAC 1, LATAM 4). 🟢 **Same channel, same
result — 🟡 4 new in both — and both denominators are published so neither reads as a contradiction.**

| Region | What the channel named | 🟢 Already held | 🆕 New |
|---|---|---|---|
| **North America** | **134 bills across 31 states** (MultiState), CA **A.B. 1159**, ID **SB 1227**, OR **SB 1546**, **H.R. 8747** (committee 2026-07-21, *not enacted*), OK + MD human-oversight bans, **NYC** K-8 moratorium, GA + MS CS credits, Alabama model procurement clause, North Carolina DPI guidance, AASA / *STUDENTS FIRST Act of 2026*, UChicago Law 1L device pilot, NEA + AFT frameworks, 60 % of US K-12 teachers using AI in 2024-25, **$3.68 B → $32 B by 2030** | 🟢 **15 / 16** | 🟡 **1 — WA `HB 2225`** |
| **EMEA** | EU AI Act **Annex III** education high-risk, **Art. 50** transparency, **Art. 4** AI literacy, AI omnibus (in force **2026-07-27**), revised dates **2027-12-02** stand-alone / **2028-08-02** embedded, OECD *Digital Education Outlook 2026*, UNESCO GenAI guidance, FI/EE/NL leading K-12, EU market **$2.64 B**, **10 %** of 450+ institutions with formal guidelines, UK **principles-based** regime | 🟢 **11 / 12** | 🟡 **1 — UK *AI Opportunities Action Plan* (published Jan 2025)** |
| **APAC** | Korea **AI Framework Act** in force **2026-01-22** (+ MSIT pilot year, one-year penalty grace), **Vietnam** AI law passed **2025-12-10**, effective **2026-03-01**, education among six high-risk sectors (automated assessment, behavioural monitoring), Taiwan **AI Basic Act** (Dec 2025), Australian **AI Safety Institute** (announced Nov 2025), China binding algorithm / deep-synthesis / generative rules, Singapore + Japan voluntary guidance, >50 % of APAC digital natives at *"repeatable"* AI maturity, Google / Microsoft / IBM / Pearson named | 🟢 **9 / 10** | 🟡 **1 — Byjus**, named as an APAC market player. 🔴 **A vendor, not an instrument** |
| **LATAM** | UNESCO **IESALC** study (200 HEIs, 19 countries; **~25 %** with a formal AI framework, **87 %** using AI, **74 %** in teaching), **TALIS** (BR 56 %, CL 55 %, CO 53 %, CR 52 % vs OECD 36 %), Digital Education Council LATAM survey (**92 %** students / **79 %** faculty), Observatory on AI in Education for LAC (**April 2026**), UNESCO–CENIA + **Latam-GPT**, **Ceibal** 75 % of Uruguayan public-school teachers, Brazil **PL 2.338/2023**, Chile's executive bill, Colombia **CONPES 4144**, **ILIA** third edition, AI Week LATAM 2026 (SoftServe + NVIDIA), CAF / CETIC.br / ECLAC / Tec de Monterrey / ProFuturo | 🟢 **12 / 13** | 🟡 **1 — Fundación Santillana**, as an Observatory partner. 🔴 **A body, not an instrument** |

🟢 **Written down explicitly because an informed gap is information and silence looks exactly like
coverage.** 🔴 **No region returned nothing. All four returned material; all four returned material
this KB overwhelmingly already held.** 🟡 **But the yield is 4/51 rather than pass 51's 0/33, and the
honest reading is that two of the four are *not* instruments** — a vendor name and a foundation name.
🔴 **The instrument yield is 2 / 51.** 🔵 **The channel is saturated, not broken, and the denominator
is how that stays distinguishable.**

### 🟡 The two genuinely new instruments

| | 🆕 Washington **HB 2225** | 🆕 UK ***AI Opportunities Action Plan*** |
|---|---|---|
| Region | **North America** | **EMEA** |
| What the channel says | Adds **reporting requirements** for AI tools in the context of minors' use, alongside Oregon **SB 1546** (which targets *compulsive* use by minors and this KB already held) | The instrument behind the UK's **principles-based** rather than statutory approach; **published January 2025** |
| 🔴 Channel status | 🔴 **Second-hand.** `app.leg.wa.gov` measured `000`; no bill text read | 🔴 **Second-hand.** `gov.uk` measured `000`; no publication read |
| 🟢 Why it is still recorded | 🟢 It completes a **pair**: OR + WA are the first two states this KB holds that regulate the *minor's pattern of use* rather than the *school's decision* | 🟢 It explains a gap this KB had been recording as absence — the UK has **no education-specific AI statute** because its instrument is a plan, not a law |

🔴 **Both are filed as *named and unverified*.** 🔵 **`P237`: a convention a pass has to remember is
not a control** — so they carry the channel in the row rather than in a footnote.

### 🔴 The EMEA date defect did **not** recur this pass, and that is worth recording

🟢 **Four consecutive passes recorded a source dating the AI Act's full effect to *August 2026*.**
🔵 **This pass's EMEA channel got it right**: it reported enforcement beginning **2026-08-02**, the
omnibus **in force 2026-07-27**, and the revised application dates **2027-12-02** (stand-alone
high-risk — the class education sits in: access, assessment of learning outcomes, educational path,
exam monitoring) and **2028-08-02** (embedded in regulated products). 🔴 **It also flagged that the
revision *"still awaits publication in the Official Journal"***, and 🔴 **`eur-lex.europa.eu` is
unreachable from here**, so the OJ citation remains second-hand by channel and first-hand only by
repetition across passes. 🟢 **Article 50 transparency was not moved and runs from 2026-08-02.**

## Opportunities by region — superseded (the live block is at the top of this file)

🔵 **One `###` per region, the five-value closed vocabulary, and the country in the prose rather than
in the field.** 🔴 **Each opportunity below names the licence constraint that decides whether it can
be delivered**, because `P631` (`verticals/solutions.md`) measured that this shelf is **never both
permissive and educational**.

### North America

🟢 **The opportunity is compliance plumbing, not tutoring.** 🔴 **134 bills across 31 states**, with
OK and MD banning AI from high-stakes decisions about students, CA A.B. 1159 restricting training on
student data, and now OR **SB 1546** + WA **HB 2225** regulating minors' *use patterns* and reporting.
🟢 **A district cannot buy one product that satisfies 31 statutes, so the deliverable is a
policy-parameterised layer**: `grant-mccurdy/instructional-ai-workflows` (MIT) supplies the
human-review-at-every-stage shape that OK/MD-style oversight rules require, and the audit trail is
what Alabama's model procurement clause asks a vendor to produce. 🔵 **Pitch against the 60 % of US
K-12 teachers already using AI informally** — the gap is governance, not adoption. 🔴 **Constraint:
if the client's SIS is ERPNext or Moodle, the AI runs *beside* it as a side-car, never linked in.**

### EMEA

🟢 **The opportunity is Annex III conformity work with a known deadline.** Education sits in the
**stand-alone high-risk** class deferred to **2027-12-02**, which is far enough out to build properly
and close enough to sell now. 🔴 **Article 50 transparency already applies (2026-08-02)**, so marking
and disclosure is immediate work. 🟢 **Only 10 % of 450+ institutions have formal guidelines** —
that is the addressable gap. 🔵 **The UK is a different sale**: its instrument is the *AI
Opportunities Action Plan*, principles-based, so the deliverable there is **assurance** rather than
conformity. 🟢 **Sovereignty favours the permissive stack** (local inference + a permissive
orchestration layer) because data-residency arguments are easier when nothing phones home.

### APAC

🟢 **Vietnam is the sharpest single opportunity this KB holds, in any region.** Its AI law (passed
**2025-12-10**, effective **2026-03-01**) names education among six high-risk sectors and is explicit
about **automated assessment and behavioural monitoring** — and treats a system as high-risk *only
where its output is the sole basis for a decision without meaningful human review*. 🟢 **That is a
statutory description of an architecture**, and it is the one
`grant-mccurdy/instructional-ai-workflows` implements: reviewer packets and remediation actions with
a human in each stage. 🔵 **Korea is the second sale**, with the Framework Act in force
**2026-01-22** and MSIT running 2026 as a pilot year with a one-year penalty grace — 🟢 **a window
for building compliant systems before enforcement bites**. 🔴 **Caution: Korea requires a domestic
representative for foreign providers**, which is a structuring question before it is a technical one.

### LATAM

🟢 **The opportunity is the governance gap, measured.** UNESCO IESALC: **87 %** of 200 institutions
across 19 countries use AI in at least one area, **74 %** in teaching — but **only ~25 % have a
formal AI framework**. 🔵 **TALIS puts LATAM teacher adoption far above the OECD average** (Brazil
56 %, Chile 55 %, Colombia 53 %, Costa Rica 52 % vs **36 %**), and Ceibal reports **75 %** of
Uruguayan public-school teachers using these tools. 🔴 **Adoption is not the problem here either; it
is that almost nobody has written the rules.** 🟢 **So the deliverable is an institutional AI
framework plus the technical controls that make it auditable**, and the regional assets to compose
with are **Latam-GPT** (via UNESCO–CENIA, being integrated into ministry-facing tools) and the
Observatory's partner network (CAF, CENIA, CETIC.br, ECLAC, Tec de Monterrey, ProFuturo, Ceibal and
🆕 **Fundación Santillana**). 🔴 **Regulation is still pending everywhere that matters** — Brazil's
**PL 2.338/2023** is in the Chamber, Chile's bill in first constitutional stage, Colombia's
**CONPES 4144** a programme to 2030 rather than an obligation — 🟢 **which means a framework built now
is a differentiator, not a compliance cost.**

### Global

🟢 **Cross-region, the one thing every channel agreed on: the market is moving from experimentation to
governance.** 🔵 **Market figures, with their disagreement published rather than averaged:** $10.6 B
→ **$42.48 B by 2030 at 41.5 % CAGR** (Research and Markets); **$12.3 B by 2026** (HolonIQ);
**$136.79 B by 2035** (Azumo); North America **$3.68 B → $32 B by 2030**; EU **$2.64 B**. 🔴 **These
rest on different definitions and are not reconcilable** — quoted as a range, never as a point.
🟢 **The durable, licence-independent demand across all five regions is the same: purpose-built
education AI with a human in the loop and an audit trail**, which is why `P632`
(`compose/patterns.md`) wires exactly that.

### 🔴 Declared gaps

- 🔴 **No instrument in this file is first-hand this pass, and none can be** — all non-GitHub egress
  is `000`.
- 🔴 **No APAC education *adoption* rate was found** — ministry-level school AI policy for China,
  India and Japan returned nothing, and the one APAC maturity figure (>50 % at *"repeatable"*) is
  about businesses, not schools. 🟢 **Named as a gap rather than back-filled from a global figure.**
- 🔴 **No LATAM instrument has been enacted**, so the region's regulatory column is still
  forward-looking in every country this KB tracks.

## 🔴 Fifty-first pass, 2026-10-08 — the regional channel yields **zero** for the fourth consecutive pass, counted name by name, and EMEA reproduced a superseded date for the **fourth** time

⏱️ **Fifth pass of this date.** Four regional queries ran verbatim, one per region. **Every named
instrument was checked term by term against the tree before being called new.** No star counts
(`P479`).

### 🔴 The regional yield, with its denominator

🔵 **Denominator stated, because `intel/trends.md` publishes a different one for this same channel:**
this table counts **instruments, bodies *and* market figures** (33); `intel/trends.md` counts
**instruments and bodies only** (31), excluding the two EMEA market figures. 🟢 **Same channel, same
result — 🔴 1 new in both — and both denominators are published so neither reads as a contradiction.**

| Region | Instruments / figures the channel named | 🟢 Already held | 🆕 New |
|---|---|---|---|
| **North America** | Ohio's mandatory district AI policy (by **2026-07-01**), CA **A.B. 1159** (no training on student data unless it benefits the school), ID **SB 1227**, **H.R. 8747** (committee **2026-07-21**, *not enacted*), OK + MD human-oversight bans on high-stakes decisions, **NYC** one-year K-8 student-facing moratorium, GA + MS CS credit requirements, AASA student-authored framework | 🟢 **8 / 8** | 🔴 **0** |
| **EMEA** | EU AI Act **Annex III** education high-risk, **Art. 50** transparency, **Art. 4** AI literacy, Digital Omnibus (Council **2026-06-29**), OECD *Digital Education Outlook 2026*, UNESCO GenAI guidance, UK **£4 M** lesson-planning/marking, FI/EE/NL leading K-12 integration, EU market **$2.64 B → $8.0 B at 31.9 %**, **10 %** of 450+ institutions with formal guidelines | 🟢 **10 / 10** | 🔴 **0** |
| **APAC** | Korea **AI Framework Act** in force **2026-01-22** (+ foreign-provider domestic representative), **Vietnam**'s AI law listing education high-risk — *automated assessment and behavioural monitoring*, high-risk only where output is the sole basis without meaningful human review, effective **2026-03-01**, extraterritorial — Taiwan **AI Basic Act** (Dec 2025), Singapore **60.9 %** diffusion, **1 in 10** APAC enterprises "very mature", Sarvam / SEA-LION / HyperCLOVA X / TAIDE | 🟢 **7 / 7** | 🔴 **0** |
| **LATAM** | UNESCO **Observatory on AI in Education for LAC** (announced **April 2026**), Mexico centres-of-excellence pilot with **CONALEP** and **DGETI** (Aug 2026), **Tec de Monterrey** PPP, Brazil **PL 2.338/2023** (still in the Chamber; ANPD sandbox to **Dec 2026**), Chile's executive bill, Colombia **CON-IA**, Mexico's enacted 2026 amendments, UNESCO competency frameworks | 🟢 **7 / 7** | 🔴 **0** |
| 🔵 **The only thing not held** | **Nebraska** — advocates pushing for NYC-style K-8 limits | — | 🟡 **1, and it is not an instrument.** Advocacy, no bill number, no date. Recorded here and **not** shelved as regulation |

🟢 **Written down explicitly because an informed gap is information and silence looks exactly like
coverage.** 🔴 **No region returned nothing. All four returned material, and all four returned
material this KB already held — which makes the channel *saturated*, not *broken*, and the
denominator is how that stays distinguishable.**

🔴 **EMEA's date defect, fourth occurrence.** A source again dated the Act's full effect to *August
2026*. 🟢 **This KB's record is unchanged and is the one to quote:** enforcement from **2026-08-02**
with the AI omnibus in force **2026-07-27**, and Reg. (EU) **2026/1744** deferred **Annex III
stand-alone** high-risk — the class education sits in: access, assessment of learning outcomes,
educational path, exam monitoring — to **2027-12-02**, with Annex I embedded to **2028-08-02**.
🟢 **Article 50 transparency was not moved and runs from 2026-08-02.** 🔴 **`eur-lex.europa.eu` and
`gnu.org` are both unreachable from this environment (403 at the proxy), so the OJ citation remains
second-hand by channel and first-hand only by repetition across passes — stated, not hidden.**

## Opportunities by region — superseded (the live block is at the top of this file)

### North America

🟢 **The licence-provenance pack is still the sellable artefact, and this pass makes it cheaper and
more defensible.** OK and MD require **human oversight** of high-stakes student decisions, CA
**A.B. 1159** restricts training on student data, and Ohio now obliges **every district** to hold a
formal AI policy. 🟢 **`P620` adds a column that pack was silently missing: the licence *version*,
recovered for five components whose grant ships as Markdown.** 🔴 **GPL-2.0 vs GPL-3.0 is not a
cosmetic difference in an auditable artefact — GPL-2.0 carries no patent grant and is
Apache-2.0-incompatible** — and four Moodle AI plugins a US K-12 engagement would plausibly reach for
(`moodle-mod_maici`, `moodle-qbank_genai`, `moodle-local_aiquestions`, `moodle-local_aiid`) had no
version on this shelf until this pass. 🔵 **Offer: per-artefact grant, read at the **pinned ref**,
with HTTP status, byte count *and file format* recorded.**
🔵 **Federal timing stays a watch item, not a plan:** H.R. 8747 cleared committee **2026-07-21** and
is **not** enacted.

### EMEA

🟢 **Scope Annex III stand-alone education high-risk to 2027-12-02, not August 2026** — 16 months of
runway that four independent secondary channels would now have spent for a client (`P617`, and this
pass is the fourth occurrence). 🟢 **And scope Article 50 transparency as live today**, because the
channels conflate the two obligations into one sentence.
🟢 **`P622` is directly useful in EMEA.** An admissions/CRM layer for an EU institution can now be
built on **two independent permissive suppliers** — `MicroPyramid` (MIT, 1,068 B) alongside
`Webkul`'s Krayin/AureusERP — where pass 46 proved the shelf had only one vendor wearing two names.
🔵 **Vendor independence is a procurement requirement in EU public tenders far more often than it is
a technical one**, so the second supplier is commercially load-bearing even though neither has an
education domain model.
🔴 **The EMEA permissive-education gap is unchanged:** the one EMEA-origin higher-ed assessment
framework on any shelf here (`macsnoeren/genai-open-assessment`, NL) is **GPL-3.0**.

### APAC

🟢 **Vietnam is the most actionable instrument in this region and the wording is the opportunity.**
Education is on its high-risk list specifically as **automated assessment and behavioural
monitoring**, and many listed systems are high-risk **only where the output is the sole basis for a
decision without meaningful human review**. 🟢 **That is a design constraint a studio can satisfy by
architecture rather than by paperwork: keep a human decision step in the loop and the system leaves
the high-risk class.** 🔴 **The law is extraterritorial (effective 2026-03-01), so it binds a
Globant delivery team serving Vietnamese learners from anywhere.**
🟢 **Korea's AI Framework Act (in force 2026-01-22) adds a concrete, billable obligation**: a
non-Korean provider serving Korean users directly must designate a **domestic representative**.
🔵 **Sovereign-model integration remains the region's distinguishing engagement shape** (SEA-LION,
Sarvam, HyperCLOVA X Think, TAIDE), and it is an integration brief, not a licence brief.

### LATAM

🟢 **The UNESCO LAC Observatory (April 2026) is the region's convening body, and the Mexico pilot
names the counterparties** — **CONALEP** and **DGETI**, with **Tec de Monterrey** in a public-private
partnership. 🟢 **Those are nameable doors for a studio, which is rarer in this region's channel than
market figures.**
🔴 **Adoption is ahead of rules here, stated by the channel in as many words** — *"education systems
are quietly integrating AI tools into classrooms, often without oversight or guidelines"* — and
Brazil's **PL 2.338/2023** is still in the Chamber, so the text can still change. 🟢 **The sellable
consequence: a governance-first engagement sells in LATAM on the strength of the EU Act's
extraterritorial reach plus the ANPD sandbox (to Dec 2026), without waiting for a local statute.**
🔵 **And the EU's 2027-12-02 Annex III date is the planning anchor for LATAM edtech selling into
Europe**, which is where the `P514` correction earns money a second time.

### Global

🟢 **This pass's transferable product is `P624`'s format-aware grant read** (`compose/patterns.md`),
and it is not education-specific: it applies to any dependency whose licence is probed by **filename**
rather than enumerated from the **tree**. 🔴 **The evidence it is needed is a project that ships its
grant twice and answers 404 to six standard filenames** (`idempiere/idempiere`), plus **26 of 412
shelf rows (6.3 %)** whose grant is Markdown or HTML — five of which were carrying a licence *family*
with no *version*.
🔴 **And the control it retires: byte count as licence identity.** Five GPL-3.0 payloads read today
span **34,674 → 35,151 B**, two *different* payloads sit at exactly **35,148 B**, and the ±1 B
"trailing-newline tolerance" this KB had been using decomposes into three unrelated edits that happen
to sum to 1 (`P621`). 🟢 **`P420`'s rule — size is a tell-tale, never an identifier — now has
evidence from both directions, and `Dolibarr/dolibarr` `develop/COPYING` is named as the
SPDX-conformant GPL-3.0 specimen to stage in future.**

## 🔴 Fiftieth pass, 2026-10-08 — the regional channel yields **zero** for the third consecutive pass, and the EMEA channel reproduced a superseded date for the **third** time

⏱️ **Fourth pass of this date.** 🔵 **All market and regulatory figures below are secondary and carry
their source.** The four mandated regional queries ran verbatim, plus the global trends query.

### 🔴 `P616` — measured name by name, and the one channel that returned something returned it **wrong**

🔵 **Measured, not estimated.** Each named instrument, body, statistic and actor returned by the five
queries was checked by name against the live tree:

| Region | Named items returned | Already held | New |
|---|---|---|---|
| **North America** | 134 bills / 31 states, CA A.B. 1159, ID SB 1227, OK/MD human-oversight rules, H.R. 8747 (committee, 2026-07-21 markup), GA + MS CS-credit-with-AI, NYC K-8 moratorium, NC DPI guidance, *STUDENTS FIRST Act of 2026* (non-binding student framework), 86% org adoption, 60% US K-12 teacher use | 🟢 **all** | 🔴 **0** |
| **EMEA** | EU AI Act Annex III education high-risk, Art. 50 transparency, Art. 4 AI literacy, *Digital Omnibus* (Council 2026-06-29), OECD *Digital Education Outlook 2026*, UNESCO GenAI guidance, EU market $2.64 B → $8.0 B at 31.9%, FI/EE/NL leading, UK £4 M, 10% of 450+ institutions with formal guidelines | 🟢 **all** | 🔴 **0** |
| **APAC** | KR AI Basic Act (in force 2026-01-22), VN Law on AI (effective 2026-03-01, education high-risk), TW AI Basic Act (Dec 2025), CN *"AI + Education"* mandatory K-12 + Beijing 8 h/yr, AU AI Safety Institute + National AI Plan, SG MOE teacher-supervised P4, IN AI from Grade 3 (2026-27), Ipsos *Education Monitor 2026* | 🟡 **all but 3 figures** | 🟡 **3, all secondary** |
| **LATAM** | UNESCO LAC Observatory (2026-04-14), IESALC/UNU-IAS 200 HEIs / 19 countries / 87% / 26% / 74% / 57% / 84-68-52% split, TALIS 2024 (BR 56 / CL 55 / CO 53 / CR 52 vs OECD 36), UNESCO–CENIA, IADB 193 solutions, Ceibal, Digital Education Council LATAM survey, MarketsandMarkets $105.6 M (2024) → $204.7 M (2029) | 🟢 **all** | 🟡 **2, both secondary** |

🔵 **Pass 48 measured 23 of 24 held; pass 49 measured 24 of 24; pass 50 measures saturation again with
five low-value secondary residuals.** 🟢 **Three consecutive passes at or near total saturation is a
settled finding about the channel, not a run of bad luck:** the secondary regional-policy channel for
education is **fully harvested for this window**, and `P601`'s prediction — *"the next new regional
datum will come from a primary source or not at all"* — 🟢 **held for a second pass.**

### 🔴 `P617` — the EMEA channel served the **superseded** enforcement date again, and this is the third instance

🔴 **Returned this pass, verbatim from a secondary source:** *"the AI Office and national authorities
started to enforce the AI Act from 2 August 2026"*, with education access and assessment named
high-risk.

🟢 **This KB holds the correction and holds it with the instrument number:** **Regulation (EU)
2026/1744** (*Digital Omnibus on AI*) — Parliament **2026-06-16**, Council **2026-06-29**, OJ
**2026-07-24**, in force **2026-07-27** — deferred **Annex III stand-alone** high-risk, *education
named explicitly*, from **2026-08-02** to **2027-12-02**, and Annex I embedded from 2027-08-02 to
**2028-08-02**. 🟢 **Article 50 transparency was NOT touched: its clock still runs from 2026-08-02.**

| Instance | Pass | What the channel said |
|---|---|---|
| 1st | ~32 → caught at 58 | *"full enforcement from August 2026"* — and this KB's own sections had **reverted** to it |
| 2nd | 49 (`P505` lineage) | same superseded date, re-served |
| 🔴 **3rd** | **50** | same superseded date, re-served again |

🔴 **Three instances is a property of the channel, not an accident.** 🟢 **The commercial consequence,
stated so it can be quoted in a pitch:** an EMEA engagement scoped to *"Annex III conformity
assessment required before August 2026"* is scoped **16 months early** for stand-alone high-risk
education systems — 🔴 **but an engagement that therefore relaxes Article 50 transparency is wrong in
the other direction**, because Art. 50 is live **now**, 67 days in as of this pass.

⚠️ **Primary still refused.** `eur-lex.europa.eu` (CELEX 32024R1689) and
`digital-strategy.ec.europa.eu` were re-probed in this run — 🔴 **both `000`.** `Gap 56` / `Gap 241`
stay open for that reason and no other.

### 🟡 `P618` — the five secondary residuals, named and ranked rather than padded into the tables

🔵 **These are the only items the five queries returned that are not in the live tree.** 🔴 **All five
are secondary, none is a repository or an instrument, and none changes a verdict.** They are recorded
so that a later pass does not re-pay for the search:

| Datum | Region | Source class | Why it is not in a table |
|---|---|---|---|
| World Bank: AI maths tutor + career coach, **85 public schools**, ~**4 500** fifth-year secondary students, **Lima**, since **2026-03** | **LATAM** | World Bank *results* page (secondary) | 🟡 **The most useful of the five** — a named, sized, dated public-sector deployment. 🔵 Distinct from `eai6/ai-tutor` (MIT, World Bank Group holder), which this KB already holds and which is **Seychelles/EMEA** |
| Google.org **AI Opportunity Fund**: +$10 M APAC, $37 M cumulative | **APAC** | vendor blog | 🔴 funding, not capability; no artefact to probe |
| UNESCO LAC Observatory partners **ProFuturo**, **IRCAI** | **LATAM** | UNESCO (primary-ish) | 🟡 two partner names missing from an otherwise complete partner list already held |
| KenResearch: APAC AI-in-education **$2.85 B (2026)**, **35.3% CAGR**; players incl. Byju's | **APAC** | commercial research | 🔴 unverifiable forecast; the CAGR figure already appears in this KB from another vendor |
| Charlotte-Mecklenburg district AI policy | **North America** | policy tracker | 🔴 one more district in a list already held at Chicago and Denver |

🟢 **Written down explicitly because an informed gap is information and silence looks exactly like
coverage.** 🔴 **No region returned nothing: all four returned something, and four of four returned
material this KB already had.**

## Opportunities by region — superseded (the live block is at the top of this file)

### North America

🟢 **The `P613` finding is the sellable one here, and it is a compliance artefact, not a feature.**
State rules now require **human oversight** for high-stakes decisions (OK, MD) and restrict training
on student data (CA A.B. 1159, ID SB 1227). 🔴 **A licence verdict that names the wrong GPL version is
a defect in exactly the artefact those rules make auditable.** Offer: a **licence-provenance pack**
per deliverable — per-artefact grant, read at the **pinned ref**, with HTTP status and byte count —
which is cheap to produce once (`P619`, `compose/patterns.md`) and is the evidence an oversight
requirement actually consumes.
🔵 **Federal timing stays a watch item, not a plan:** H.R. 8747 passed committee on **2026-07-21** and
is **not** enacted.

### EMEA

🔴 **The date correction is worth money twice.** Scope **Annex III stand-alone** education high-risk
to **2027-12-02** — not August 2026 — which buys a client 16 months of runway that three independent
secondary channels would have spent for them (`P617`). 🟢 **And scope Article 50 transparency as live
today**, because the Omnibus did not move it and the channels conflate the two.
🟢 **`P609` is directly commercial in EMEA.** A Spanish-language deliverable for a public institution
in Spain no longer has to choose between GPL-3.0 and a reimplementation: **AnCora `r2.9`+ is CC BY
4.0** (`P611`), so the permissive route is a **retrain**, not a rewrite.

### APAC

🟢 **Mandate-driven curriculum work is the live demand** — CN mandatory K-12 AI with Beijing at 8 h/yr,
IN from Grade 3 in 2026-27, KR's AI-focused secondary pipeline — against **SG**'s explicitly cautious,
teacher-supervised posture. 🔵 **The regulatory spread is the constraint to design for:** KR's AI Basic
Act is in force (2026-01-22) with a foreign-provider domestic-representative duty, and **VN** names
education among its high-risk sectors (effective 2026-03-01), with high-risk generally conditioned on
the AI output being the **sole** basis for a decision without meaningful human review.
🟢 **So the architecture that sells across APAC is the one with a human-decision seam**, documented —
the same seam OK/MD require in North America.

### LATAM

🟢 **The region's own measured defect is the opening: 87% of 200 HEIs across 19 countries use AI in at
least one area, and only 26% have a formal framework** (UNESCO IESALC/UNU-IAS). 🟢 **That is a
governance engagement, not a tooling one**, and it is the gap UNESCO's LAC Observatory
(**2026-04-14**, Santiago, roadmap 2026–2029) exists to close.
🟢 **`P609`/`P611` land hardest here.** Spanish is the delivery language for most of the region, and
the finding converts *"the Spanish NLP pipeline is GPL"* into *"the Spanish corpus is **CC BY 4.0**
and the shipped model is pinned to a 2021 tag."* 🔴 **For public-sector work GPL-3.0 is usually
acceptable anyway** — but the client's own procurement rules often are not aware of that, and now
there is a permissive answer when they are not.
🔵 **The World Bank Peru deployment (`P618`: 85 schools, ~4 500 students, Lima, since 2026-03) is the
nearest public-sector reference case**, flagged secondary.

### Global

🟢 **The pass's own transferable product is `P619`'s pre-flight** (`compose/patterns.md`): read every
third-party licence **at the ref the consuming artefact pins**, and read the default branch too, and
**compare**. 🔴 **`P612` is the evidence it is needed** — two independent reads agreed on "GPL" and the
agreement was an accident of a five-year-old sentence. 🔵 **This is not an education-specific control**;
it applies to any dependency whose grant is read once and inherited thereafter, which is all of them.

## 🔴 Forty-ninth pass, 2026-10-08 — the regional channel's new-information yield this window is **zero**, measured name by name

⏱️ **Third pass of this date.** 🔵 **All market and regulatory figures below are secondary and carry
their source.** The four mandated regional queries ran verbatim, plus the global trends query.

### 🔴 `P601` — every distinct datum the five queries returned was **already in this KB**, to the figure

🔵 **Measured, not estimated.** Each named instrument, body, statistic and actor returned by the
five queries was checked by name against the live tree:

| Region | Named items returned | Already held | New |
|---|---|---|---|
| **North America** | Ohio first-state AI-policy mandate (2026-07-01), CA A.B. 1159, OK/MD human-oversight rules, H.R. 8747 (committee), 134 bills / 31 states, NYC K-8 moratorium | 🟢 **all** | 🔴 **0** |
| **EMEA** | EU AI Act Annex III education high-risk, Art. 50 transparency, Art. 4 AI literacy, enforcement from 2026-08-02, OECD *Digital Education Outlook 2026*, UNESCO GenAI guidance | 🟢 **all** | 🔴 **0** |
| **APAC** | KR AI Basic Act (in force 2026-01-22, grace year), VN Law on AI (effective 2026-03-01, education among six high-risk sectors), TW AI Basic Act, AU AI Safety Institute + National AI Plan | 🟢 **all** | 🔴 **0** |
| **LATAM** | UNESCO LAC Observatory (2026-04-14, roadmap 2026–2029), IESALC/UNU-IAS 200 HEIs / 19 countries / 87% / 26%, TALIS 2024 (BR 56 / CL 55 / CO 53 / CR 52 vs OECD 36), Cetic.br (BR 53% admins / 22% guidelines), UNESCO–CENIA, IADB EduIA Lab / Gestão Presente, Ceibal | 🟢 **all** | 🔴 **0** |

🔵 **Pass 48 measured 23 of 24 already held and its one new datum failed verification (`Gap 251`).
🔴 Pass 49 measures 24 of 24.** 🟢 **Two consecutive passes at or near total saturation is a finding
about the channel**: the secondary regional-policy channel has been fully harvested for this window,
and the next new regional datum will come from a **primary** source or not at all.

### 🔴 `P602` — the seven blocked primaries were re-probed and **all seven are still refused**

🔵 **Re-probed rather than assumed, because a network policy can change between passes.** One
`curl -sSI` per URL, same run:

| Primary | Gap it blocks | HTTP |
|---|---|---|
| `eur-lex.europa.eu` (CELEX 32024R1689) | `Gap 56`, **`Gap 241`** | 🔴 **000** |
| `digital-strategy.ec.europa.eu` | **`Gap 241`** (the amending instrument) | 🔴 **000** |
| `alison.legislature.state.al.us` | **`Gap 251`** | 🔴 **000** |
| `billtrack50.com` | **`Gap 251`** | 🔴 **000** |
| `cs4alabama.org` | **`Gap 251`** | 🔴 **000** |
| `purl.imsglobal.org` (QTI 3 ASI XSD) | `Gap 240` | 🔴 **000** |
| `docs.moodle.org` | `Gap 92` | 🔴 **000** |

🟢 **Control in the same run:** `raw.githubusercontent.com` → **200**, so the refusals are the
egress policy and not a dead network. 🔴 **`Gap 241` is the costly one**: this pass's EMEA run
surfaced a Commission page stating the AI Act amendments were *"adopted in June 2026"* and entered
into force *"27 July 2026"* — 🔴 **which is exactly the identifier `Gap 241` needs, from a domain
this environment cannot read.** 🔵 **So the date must still not appear in a client deliverable as
settled law.**

## Opportunities by region — superseded (the live block is at the top of this file)

### North America

🟢 **Governance instrumentation, sold as a control rather than a policy document.** 134 bills across
31 states means every multi-state district group now has a conformance surface, and Ohio's mandate
(every district with a formal AI policy by **2026-07-01**) has already passed its deadline — so the
market is **audit**, not authoring. 🔵 **What this KB can put behind it:** the human-decision gate
(`compose/code/grading-draft-gate/`) satisfies the OK/MD human-oversight rules and NYC's red tier
directly. 🔴 **Licence note that decides the build:** an English-language scorer can be assembled
**permissively end to end** — `en_core_web_*` is **MIT** (`P595`) and `wwrwbs/AI_AWE` is Apache-2.0
with permissive closure. 🟢 **North America is the one region where the essay-scoring chain has no
licence blocker.**

### EMEA

🟢 **AI Act conformance packaging, with the Article 50 marking instruments this KB already holds**
(`compose/code/aiact-50-2-marking/`, `-pack/`, `-exposure/`). 🔵 Education sits in Annex III
high-risk, so admissions, evaluation and exam scoring carry risk management, data governance, human
oversight and conformity assessment. 🔴 **Sell the Article 4 AI-literacy and Article 50 transparency
work now and treat the Annex III deferral date as unsettled** — `Gap 241`/`P602`: the deferral to
December 2027 is consistent across every secondary source and **citable from none of them primarily
from this environment**. 🟢 **The cheapest governance artefact on offer here is the supersession
marker for ADRs and compliance logs** (`P582`, and `P598` now mechanises it).

### APAC

🟢 **Multi-jurisdiction policy routing, and it is the region where regulation is genuinely ahead of
the tooling.** Vietnam's Law on AI (effective **2026-03-01**, the first standalone AI statute in
South-East Asia) names **education** among six high-risk sectors and reaches **automated assessment
and behavioural monitoring** by name; Korea's AI Basic Act is in force (**2026-01-22**) with a
stated grace year. 🔵 **The deliverable is a policy-node architecture** — one assessment pipeline,
per-jurisdiction gates — because a single compliance posture cannot satisfy KR, VN, TW, CN, SG, JP
and AU simultaneously. 🔴 **No new APAC *repository* this pass or in the last nine**; the region
imports its software and writes its own rules.

### LATAM

🟢 **The governance gap is the whole opportunity, and it is now a two-source measurement.**
IESALC/UNU-IAS: **87%** of 200 HEIs across 19 countries run AI in at least one area, **26%** have
any formal framework. Cetic.br: **53%** of Brazilian school administrators use AI, **22%** have
guidelines. 🔵 **Institutions are already running AI; almost none can describe how** — that is a
framework-and-audit engagement, not a build.

🔴 **And this pass adds the licence constraint that changes a Spanish-language proposal.** `P595`:
`es_core_news_*` is **GNU GPL 3.0** (inherited from `UD_Spanish-AnCora`), against Portuguese's
CC BY-SA 4.0 and English's MIT. 🔴 **So a Spanish assessment product cannot ship permissively on the
default NLP pipeline at all** — one tier *earlier* than `Gap 237`'s rubric-and-corpus problem bites.
🟢 **Portuguese remains the viable LATAM build** (ShareAlike is restrictive but publishable, and
`lplnufpi/essay-br` is MIT); 🔴 **Spanish needs either a licensed pipeline, a reimplementation, or a
copyleft-accepting delivery model — priced before the pitch, not after.** 🟢 **Declared `Gap 254`.**

### Global

🟢 **The cross-region deliverable this pass makes concrete: a licence-by-language pre-flight for any
assessment or language product.** 🔴 **`P596` is the reason it is not optional** — "the library is
MIT" is true of spaCy's code and **false of the artefact a non-English product ships**, and the
licence gets *more* restrictive one tier down, not less. 🔵 **The check is three lines of work and
belongs in the first week of any engagement**: read the model artefact's own metadata, then its
`sources[]` corpora, then each corpus's own `LICENSE`.

| Target language | Pipeline artefact | Can the product ship permissively? |
|---|---|---|
| English | `en_core_web_*` 🟢 **MIT** | 🟢 **yes**, end to end |
| Portuguese | `pt_core_news_*` 🟡 **CC BY-SA 4.0** | 🟡 **publishable, but ShareAlike travels** |
| Spanish | `es_core_news_*` 🔴 **GPL-3.0** | 🔴 **no** — needs a licensed pipeline, a reimplementation, or copyleft delivery |

🔵 **And the governance artefact that sells in every region, because it is cheap and this pass
mechanised it:** append-only logs — ADRs, compliance registers, risk logs, incident timelines — are
*correct by construction and misleading by ordering*. 🔴 **Every entry is true as of its date, so
nothing is ever wrong, and a reader who stops at the first match is nonetheless misinformed.**
🟢 **`compose/code/p598-register-freshness-gate/` is the control**, and `P597` is this KB paying the
cost in its own register before selling the fix.

## 🔴 Forty-eighth pass, 2026-10-08 — the regional channel returned **one** datum this KB did not hold, and it does not survive verification

⏱️ **Second pass of this date.** 🔵 **All market and regulatory figures below are secondary and carry
their source.** The four mandated regional queries ran verbatim, plus the global trends query.

### 🔴 `P586` — the single new regional datum fails verification, so it enters no table

🔵 **The channel's yield was measured, not estimated.** Every distinct named instrument, body,
statistic and actor the five queries returned was checked by name against the live tree:
**23 of 24 were already recorded.** 🔴 **The one new item does not hold up.**

The claim, from a US state-policy tracker: *"Alabama's HB 329 requires an approved CS course that
includes AI instruction to graduate from high school."* Three defects, each of which alone would
keep it out of a table:

| # | The claim | What the sources actually say |
|---|---|---|
| 1 | 🔴 reads as **law in force** | It is a **bill**. Passage and enactment **unconfirmed** in every source reached |
| 2 | 🔴 bill number given as `HB 329` | One committee summary of the same proposal calls it **`HB 332`**. 🔴 **The identifier is contested** |
| 3 | 🔴 presented as a **2026 AI mandate** | The graduation requirement **predates the bill**: 2024 Alabama Administrative Code updates, effective **class of 2032**. The bill *codifies* what the State Board already did. The lead secondary article is dated **2025-04-02**, not 2026 |

🔴 **Why this would have reached a client.** An engagement planning to "an Alabama 2026 AI curriculum
mandate" would be planning to the wrong instrument **and six years early** — the requirement bites
with the **class of 2032**, with voluntary implementation first and required implementation in
**2027–28** per the State Board's course of study. 🟢 **Declared as `Gap 251` rather than recorded as
a fact.**

### 🔴 `P587` — three primaries blocked, so `Gap 251` cannot be closed from this environment

| Primary attempted | Result |
|---|---|
| `alison.legislature.state.al.us` (the bill text itself) | 🔴 **`EGRESS_BLOCKED`** by the network egress proxy |
| `billtrack50.com` (status and last action) | 🔴 **`EGRESS_BLOCKED`** |
| `cs4alabama.org` (the administrative-code instrument) | 🔴 **`EGRESS_BLOCKED`** |

🔵 **Same class as `Gap 56`** (`eur-lex.europa.eu`), **`Gap 92`** (`docs.moodle.org`) and **`P533`**
(`purl.imsglobal.org`) — a primary source refused by policy, **recorded rather than silently
replaced by a secondary**. 🔴 **Three secondaries that disagree with each other are not a
substitute for one primary**, and this pass does not treat them as one.

### 🔵 What the regional runs confirmed (already held, re-read this pass)

🟢 **Confirmation is not nothing** — these are the figures a proposal quotes, and they were returned
again by an independent run this pass. **No figure below is new to this KB.**

- **EU AI Act, education = high-risk** (admissions, evaluation, exam scoring); high-risk obligations
  from **2026-08-02**, with the **AI omnibus** adopted June 2026 and in force **2026-07-27** having
  moved the high-risk timeline. 🔴 **Obligation dates must be re-checked against the official text**
  — and `Gap 56` is exactly why this KB cannot do that here.
- **APAC:** Vietnam's **Law on AI** (passed 2025-12-10, effective **2026-03-01**), the first
  standalone AI statute in SE Asia, whose high-risk list **includes education** — automated
  assessment and behavioural monitoring. Korea's **AI Basic Act** in force Jan 2026 with 2026 as a
  pilot year and a one-year grace on penalties. Taiwan's AI Basic Act (Dec 2025). Australia's AI
  Safety Institute + National AI Plan (Dec 2025).
- **LATAM:** UNESCO **IESALC** — 200 HEIs across 19 countries, **87%** using AI in ≥1 area, **26%**
  with any formal framework; 84% private non-profit / 68% public / 52% private for-profit. TALIS 2024
  teacher use: Brazil 56%, Chile 55%, Colombia 53%, Costa Rica 52% vs **OECD 36%**. Uruguay
  (**Ceibal**) 75% of public-school teachers. Brazil **PL 2.338/2023** in the Chamber of Deputies;
  Colombia **CONPES 4144**; Chile's risk-based bill tied to its forthcoming DPA.
- **North America:** 134 bills / 31 states on one tracker vs 68 bills / 27 states / 10 enacted on
  another — 🔴 **the methodology conflict is itself the finding and is already recorded**. California
  **AB 1159**, Idaho **SB 1227**, Oklahoma **SB 1734**, Maryland's AI Ready Schools Act, NYC's
  traffic-light guidance (Mar 2026, red tier bars AI grading), ED's AI grant-priority rule
  (2026-04-13), **H.R. 8747** advanced in committee 2026-07-21, 35+ states with official guidance.

## Opportunities by region — superseded (the live block is at the top of this file)

🔵 **One heading, five subsections, every region answered — including the ones where the answer is
"nothing new this pass".** An unplaced finding is worth less than a placed one, and a region left
silent is indistinguishable from a region covered.

### North America

🟢 **The opportunity is the conflict, not the count.** Two reputable trackers disagree on how many
AI-in-education bills exist (134/31 states vs 68/27 states), and **35+ states** now publish
guidance. 🟢 **Sell the reconciliation:** a per-state obligations matrix an institution can act on,
anchored on the instruments that are unambiguous — **AB 1159** (no student data for model training),
**SB 1734** (written district AI policy before 2027–28), NYC's **red tier** (no AI grading,
discipline, promotion, placement, IEP/504). 🔴 **The red tier is the architectural constraint**: a
grading agent sold into a US district must be advisory-only with a human decision point, which is
precisely the shape `compose/patterns.md`'s draft-gate recipe already has.

### EMEA

🟡 **The timeline is the risk and the billable work.** High-risk obligations from **2026-08-02**, and
the **AI omnibus** (in force 2026-07-27) moved that timeline. 🔴 **No two secondaries in this
channel agree on the current dates, and the primary is blocked (`Gap 56`).** 🟢 **That is a
conformance-readiness engagement, not a compliance claim** — scope it as *evidence assembly*
(bias testing, human oversight, user notification for proctoring) which is required under every
reading of the dates. 🔵 **Outside the EU the picture is genuinely thin** — Gulf national AI
strategies drive spend (UAE, Saudi) and parts of MEA have **no framework at all**, which is an
opportunity to arrive before the regulation does, and a risk to price accordingly.

### APAC

🟢 **Vietnam is the sharpest named opportunity in this channel.** Its Law on AI is **in force since
2026-03-01** and its high-risk list **names education** — automated assessment and behavioural
monitoring. 🟢 **So an assessment product sold in Vietnam needs the high-risk evidence pack now, not
in 2027**, and almost nobody has built one for that statute. Korea's pilot year with a penalty grace
is a **window to deploy and document before enforcement bites**; Singapore and Japan remain
voluntary-guidance, so the differentiator there is proof of learning gain rather than compliance.

### LATAM

🟢 **The gap between adoption and governance is the engagement, and it is measured:** **87%** of
HEIs using AI, **26%** with a formal framework. 🟢 **The 61-point spread is the proposal** — an AI
governance framework for a university system, with UNESCO IESALC's own instrument as the baseline so
the client is not buying a bespoke standard. 🔵 **Teacher adoption is already above OECD average**
(Brazil 56%, Chile 55%, Colombia 53%, Costa Rica 52% vs 36%; Uruguay 75%), so this is **not** an
enablement sell — the tools are in use and ungoverned. 🔴 **Pair it with cost discipline:** the
local-first, permissive stack on this KB's shelf (Kolibri, OpenTutor, Ollama defaults) exists because
LATAM budgets and connectivity make the hosted-API architecture the wrong one.

### Global

🟢 **The OECD 2026 Digital Education Outlook's recommendation — move beyond general-purpose AI to
purpose-built educational AI with durable learning gains — is the thesis this KB's whole shelf
serves**, and 1EdTech's read (experimentation → governance) says the buyer is now procuring evidence
and policy, not demos. 🟢 **The parametric-assessment chain is the clearest global offer**, because
it is now complete end to end on permissive components for the first time — see `P594` in
`compose/patterns.md`. 🔴 **Market sizing stays contradictory and is quoted as a range, never a
number:** $10.6B (2026) → $42.48B (2030) at 41.5% from one house, $12.3B (2026) → $136.79B (2035)
from another, Europe $2.64B (2026) → $8.0B (2030) at 31.9%. 🔵 **Three incompatible definitions of
the same sector; cite the range and the disagreement.**

## 🔵 Forty-seventh pass, 2026-10-08 — LATAM is the best-measured region in this channel, and that is a fact about the other three channels

⏱️ **First pass of this date.** The four mandated regional queries ran verbatim
(`AI education {region} 2026 adoption regulation players`). 🔵 **Every figure below is secondary and
carries its source type, per `P515`** — most of this channel is vendor and market-research pages
whose numbers contradict each other. 🟢 **The canonical `## Opportunities by region` block below was
refreshed by this pass; it remains the file's single block (`P383`).**

### 🔴 The market-size channel still does not agree with itself, and this pass adds three more readings

| Source type | Base | Horizon | CAGR |
|---|---|---|---|
| market-research blog | ~**$6.4B** (2025) | **$79.6B** by 2034 | **31.35%** |
| market-research report | **$8.3B** (2025) → **$11.4B** (2026) | **$57.2B** by 2033 | — |
| market-research report | **$7.52B** (2025) → **$10.6B** (2026) | — | **40.9%** |

🔴 **$79.6B by 2034 and $57.2B by 2033 are not reconcilable with each other**, and neither is
reconcilable with North America's own regional forecast (**~$951M (2024) → ~$2.3B (2029), CAGR
15.9%**) given that the same channel puts North America at **~36% of the market**. 🔵 **A region
holding a third of a market cannot compound at 15.9% while the market compounds at 31–41%.** 🟢 **At
least one of those two series is wrong; this KB does not know which, and records the spread rather
than averaging three vendor estimates into a fourth.** This is `P515`'s standing finding, with three
new readings attached.

### 🔴 `P580` — the channel's sharpest contradiction is about MATURITY, and it resolves into a measurable gap

Two 2026 outlooks, same run, opposite claims: one frames the year as *"transitioning from pilot
programmes to mainstream deployment"*; the other scores the market **35 / 100** on maturity, stating
**most institutions are still in pilot mode**.

🟢 **Both are true, because they are measuring different populations.** Individual adoption is
mainstream and institutional adoption is not — and the two LATAM surveys in this pass measure the
two populations **separately**, which is what lets the contradiction be resolved rather than
averaged:

| Population | Measured | Source |
|---|---|---|
| **Students** | **92%** actively engaging with AI | Digital Education Council, 30 000+ responses |
| **Faculty** | **79%** actively engaging | same |
| **Institutions** with any formal framework | 🔴 **26%** | UNESCO IESALC, 200 institutions / 19 countries |

🔵 **That is the whole opportunity, stated as one number: institutions are running AI at 87% and
governing it at 26%.** 🟢 **Every regional subsection below is written against that gap**, because it
is the one finding this pass can place in all four regions with evidence rather than inference.

🔵 **Sampling caveat, for every figure in this pass:** these are **self-reported institutional
surveys**, and the DEC sample is **not random**, so it skews toward engaged institutions. 🔵 **The
LATAM numbers being better measured does not mean LATAM is ahead** — it means the other three
regional channels returned less, which is recorded as a gap in each.

## 🟡 Forty-sixth pass, 2026-10-07 — the regional channel returns a **vendor-concentration** signal in North America, and it is the same shape as the licence finding on the ERP shelf

⏱️ **Thirteenth pass of this date.** 🔵 **Every figure below is secondary and carries base year, scope
and publisher, per `P515`.** 🔴 **`eur-lex.europa.eu` and `data.europa.eu` remain blocked by the proxy
(`Gap 56`), so no EU date below is cited as primary — `Gap 241` stands unchanged from pass 45, and
`P555`'s contradiction is NOT resolved.**

🔵 **The canonical `## Opportunities by region` block of this file was REFRESHED IN PLACE, not
duplicated** — eight accumulated copies is the defect `P546` cleared, and the `p383` gate reports
🟢 **0 findings** on this file after this pass's edit.

### 🟡 `P567` — North America's education-AI supply side is **consolidating**, and the free tier is now four-way

🔵 **No new market denominator surfaced this pass** (the seven of `P554`/`P515` stand, and they still
disagree: Research and Markets **USD 10.6 B** 2026 → **42.48 B** 2030 @ **41.5 %**; IMARC **USD 6.4 B**
2025 → 79.6 B 2034 @ 31.35 %; HolonIQ **USD 12.3 B** 2026 — all "AI in education", global, via
secondary). 🟢 **What is new is structural, and structure is more usable in a proposal than a
denominator nobody agrees on.**

| Signal, 2026 | What it is | Reading |
|---|---|---|
| 🆕 **McGraw Hill → TeachFX** | a curriculum publisher **completed** the acquisition of an AI-native teacher-coaching platform | 🔴 **consolidation**: the AI layer is being bought by the incumbent content layer, not competing with it |
| 🆕 **Free teacher tier, now four-way** | OpenAI *ChatGPT for Teachers* (Nov 2025), Anthropic *Claude for Teachers* (Jul 2026), plus Google and Amazon giving tools to students/teachers | 🔴 **the entry-level tool market is being priced to zero** by four firms at once |
| 🆕 **AFT National Academy for AI Instruction** | **USD 23 M**, the union's New York City affiliate and **three** AI companies | 🟡 **teacher training is being funded by the vendors whose tools are taught** |
| **Gates Foundation** | **USD 1 B** commitment to equitable AI tools, **40 %** to education | 🟢 philanthropic demand-side money, incl. AI tutoring |
| **White House pledge** | **60+** companies committing funding, curriculum and PD to K-12 | 🟡 a channel, not a market |

🔴 **The commercial consequence for a studio is specific and it is not "compete with the free
tier".** When the generic assistant is free from four directions, the billable work is **everything
the free tier cannot do**: institutional data boundaries, the academic domain model, conformity
evidence, and integration into a student information system. 🟢 **Which is precisely the shelf this
KB has been assembling** — and precisely what `verticals/solutions.md` measures this pass: the
education domain model exists only under copyleft, so building it on a permissive base is *work*,
and work is what a studio sells.

### 🔵 The same shape, twice, in one pass

🟢 **Worth stating because the two findings came from unrelated channels and agree.** On the supply
side of the market, four firms give away the entry tier and an incumbent buys the AI layer:
**plurality that resolves to concentration.** On this KB's own ERP/CRM shelf, the two "independent
MIT options" a studio would pick for licence diversity — `krayin/laravel-crm` and
`aureuserp/aureuserp` — ship a **byte-identical** 1 077 B licence file held by the **same vendor**
(`Webkul Software`, `P564`). 🔵 **A shelf can look plural and have one supplier behind it, and the
only way to find out is to read the payload rather than the list.**

### 🔴 What the regional channel did NOT produce this pass, stated rather than left blank

| Region | This pass |
|---|---|
| North America | 🟢 **new**: the consolidation signals above |
| EMEA | 🟡 **one weak addition** — the OECD's *2026 Digital Education Outlook* is reported (via aggregator, **not** read first-hand) to recommend **purpose-built educational AI over general-purpose tools**. 🔴 **UK, Gulf and African education regulation returned nothing again — fifth consecutive pass.** `Gap 241` and `P555`'s date contradiction both stand |
| APAC | 🟡 **one addition**: **Australia** released a **National AI Plan** and announced an **AI Safety Institute** (December 2025) — 🔵 **safety-and-risk framing, NOT education-specific; do not cite it as education regulation** (the `P524` rule, applied) |
| LATAM | 🔴 **nothing new.** The channel reproduced what pass 45 already holds (UNESCO IESALC **87 %** of **200** institutions across **19** countries; TALIS 2024 teacher use Brazil **56 %** / Chile **55 %** / Colombia **53 %** / Costa Rica **52 %** vs OECD **36 %**; PISA 2025 nine in ten 15-year-olds in 13 countries; Brazil **53 %** of administrators using AI against **22 %** with guidelines). 🔵 **Reproduction is confirmation, not a finding** |

🔴 **Zero education-native AI agents in all four regions, for the fourteenth consecutive pass.**
🔵 **That is now a stable property of the channel rather than a gap waiting to close**, and it is
recorded as such in `agents/top.md` and `intel/trends.md`.

## 🟢 Forty-fifth pass, 2026-10-07 — the regional channel delivers a **binding education instrument** in the region that had none, and a seventh market denominator

⏱️ **Twelfth pass of this date.** 🔵 **Every figure below is secondary and carries base year, scope
and publisher, per `P515`.** 🔴 **`eur-lex.europa.eu` and `data.europa.eu` remain blocked by the proxy
(`Gap 56`), so no EU date below is cited as primary — `Gap 241` stands, and this pass makes it
worse rather than better (see `P555`).**

### 🟢 `P554` — a seventh denominator, and the spread is unchanged in character

| Publisher | Base year | Figure | Horizon | CAGR | Scope as stated |
|---|---|---|---|---|---|
| 🆕 Research and Markets | 2026 | **USD 10.6 B** | **USD 42.48 B** by 2030 | **41.5 %** | "AI in education", global |
| IMARC (pass 44) | 2025 | USD 6.4 B | USD 79.6 B by 2034 | 31.35 % | "AI in education", global |
| HolonIQ (via secondary) | 2026 | **USD 12.3 B** | — | — | "AI in education", global |

🔴 **Three publishers, three different 2026-ish base values (6.4 / 10.6 / 12.3 B), and horizons that
do not meet.** 🔵 **`P515`'s conclusion is reinforced, not revised:** the denominators disagree
because the *scope* differs, so a single number is not usable in a proposal. 🟢 **What IS usable is
the direction all seven agree on** plus the governance gap below, which is measured per institution
rather than per dollar.

### 🟢 `P555` — the EU education date now has **two mutually exclusive secondary readings**, and that is the finding

🔵 **Pass 42 recorded the Annex III education deferral; pass 44 carried it as ~December 2027.** 🔴 **This
pass the channel returned both of these, from different publishers, in the same run:**

| Source type | Reading |
|---|---|
| European Commission policy page (digital-strategy.ec.europa.eu) | AI Office + national authorities **enforcing from 2026-08-02**; "AI omnibus" adopted **June 2026**, in force **2026-07-27** |
| Education-sector compliance guide | Council final approval **2026-06-29**; revised high-risk dates **2027-12-02** (stand-alone) and **2028-08-02** (embedded in regulated products) |

🔴 **These cannot both describe the obligation that binds a school in 2026, and this environment
cannot adjudicate them** — the primary channel is proxy-blocked. 🟢 **So the instruction to a client
engagement is to quote the CONFLICT, not a date**, and to design to the earlier reading. 🔵 **This is
`Gap 241` widening rather than closing, and it is recorded as such**: six passes of secondary sources
have now produced a contradiction rather than a convergence, which is itself evidence about the
channel.

### 🟢 `P556` — the governance gap, finally measured on a large institutional denominator

🔵 **This KB has carried "adoption has outrun governance" as a near-universal claim for twelve
passes, resting mostly on student-usage percentages.** 🟢 **UNESCO IESALC supplies the institutional
version for LAC — 200 institutions, 19 countries:**

| Measure | Value |
|---|---|
| Institutions using AI in ≥1 area of activity | **87 %** |
| Institutions with **any** formal framework | 🔴 **26 %** |
| Private **non-profit** universities that have implemented AI | **84 %** |
| **Public** institutions | 68 % |
| Private **for-profit** institutions | 52 % |

🔵 **The ordering is counter-intuitive and worth carrying into a pitch**: private non-profits lead
and for-profits trail, which inverts the usual assumption about who moves first. 🟢 **Corroborated at
the teacher level by an independent instrument** — TALIS 2024: Brazil 56 %, Chile 55 %, Colombia
53 %, Costa Rica 52 % vs an OECD average of 36 %, and Uruguay at 75 % of public-school teachers
(Ceibal, 2026). 🔵 **Two instruments, two units of analysis, same direction** — that is the first time
this claim has had that on this KB.

### 🟢 `P557` — the regional channel's thirteen-pass scorecard, stated so the nils are not read as coverage

| Region | Agents returned | Policy/adoption returned | This pass's new instrument |
|---|---|---|---|
| North America | 🔴 **0** | 🟢 dense (state legislatures, federal bill, teacher surveys) | Ohio's **2026-07-01** district policy mandate |
| EMEA | 🔴 **0** | 🟡 EU-dense, **UK/Gulf/Africa effectively empty** | 🔴 a date *contradiction* (`P555`) |
| APAC | 🔴 **0** | 🟢 now dense | 🟢 **Vietnam names education high-risk** (in force 2026-03-01) |
| LATAM | 🔴 **0** | 🟢 dense and education-native | 🟢 UNESCO IESALC institutional denominator |

🔴 **Zero agents in four regions over thirteen passes.** 🟢 **But the channel is not unproductive — it
is productive on a different axis than the one it is queried for**, and three of four regions
produced a *binding or mandated* instrument this pass. 🔵 **The declared EMEA gap is real:** UK, Gulf
and African education regulation did not surface, so "EMEA" in the block below means **EU** until a
named national instrument says otherwise.

## 🔴 Forty-fourth pass, 2026-10-07 — this file has carried **8** canonical opportunity blocks where the contract allows **one**, and the reason nobody saw it is `P541`

⏱️ **Eleventh pass of this date.** 🔵 **Every figure below is secondary and carries base year, scope
and publisher, per `P515`.** 🔴 **`eur-lex.europa.eu` and `data.europa.eu` remain blocked by the proxy
(`Gap 56`), so no EU date below is cited as primary — `Gap 241` stands.**

### 🔴 `P546` — the `p383` gate has been reporting **14 findings on this file** and no pass acted, because the gate was being run with no arguments

🟢 **This is `Gap 243`'s premise paying off in the exact way the gap predicted** — *"it would tell
this KB how much of its own evidence is real."*

`p383-region-heading-gate` encodes the contract: opportunities live under **one** `## Opportunities by
region` block, with one `###` per region from the closed five-value vocabulary. 🔴 **Run against this
file for the first time, it exits `1` with 14 findings:**

| Finding | n | What it means here |
|---|---|---|
| `P383-MULTIPLE-BLOCKS` | 7 | 🔴 **8 canonical blocks**, one per pass since pass 37 — the contract allows **one** |
| `P383-MISSING-REGION` | 7 | 🔴 every block omits **`Global`**, so the five-value vocabulary was never complete |

🔵 **Why it was invisible, and it is not that nobody looked.** `P541` (pass 43) caught this very gate
printing `total 0` and exiting `0` **when invoked with no arguments** — indistinguishable from a clean
tree. 🔴 **Every earlier reading of "p383: clean" was a reading of an empty measurement.** Pass 43
fixed the gate; this is the first pass to actually hand it the corpus, and the backlog surfaced
immediately. 🟢 **Acted on, not merely recorded**: the 7 historical blocks are marked **superseded**
(content untouched, headings renamed so they are no longer canonical), and the single live block below
carries all five vocabulary values. 🟢 **`p383` now exits `0` on this file.**

### 🟢 `P547` — two more 2026 denominators, and `P515`'s spread is now **12×** at the 2034 horizon

| Publisher | Base year | Figure | Horizon | CAGR | Scope as stated |
|---|---|---|---|---|---|
| IMARC | 2025 | **USD 6.4 B** | **USD 79.6 B** by 2034 | **31.35 %** (2026-2034) | "AI in education", global |
| (Korean market-research reseller) | 2025 | **USD 8.3 B** → **11.4 B** (2026) | **USD 57.2 B** by 2033 | — | "AI in education", global |
| *carried from `P529`* | 2025/2026 | four publishers, **6×** spread | — | — | — |

🔴 **Same named market, same base year, and the 2025 figures differ by 30 % between these two
alone** (6.4 vs 8.3). 🔵 **At the far horizon the published endpoints span 57.2–79.6 B on
non-matching end years**, which is why this KB quotes a denominator **with its publisher attached or
not at all**. 🟢 **The commercial consequence is unchanged and is the usable part**: direction and
ordering are safe to pitch; a single headline number is not.

### 🟢 `P548` — a candidate fix for `Gap 242`, and it is a better instrument than the one that opened it

`Gap 242` is an unresolved contradiction **inside one publisher** (the Digital Education Council's
summary says EMEA has the lowest intent while its own coverage reports EMEA 89 % and US & Canada
67 %). 🟢 **Named this pass as the replacement instrument: the UNESCO IESALC + UNU-IAS working paper
(September 2026)** — a survey of **200 higher-education institutions across 19 countries**, fielded
**August-October 2025**, mapping AI use across teaching and learning, research, community engagement,
administration and governance. 🔵 **Why it is better than the DEC survey**: its sampling frame,
fielding window and country list are stated, which is exactly what `Gap 242` needs in order to be
settled rather than re-quoted. 🔴 **Not yet read in full — the paper is named, located and
unmeasured**, so no figure from it is quoted here. 🔵 **This narrows `Gap 242`'s remedy from "obtain
the primary DEC report" to "read a named, better-documented instrument."**

### 🔵 Regional positions measured this pass

| Region | Measured this pass | Channel verdict |
|---|---|---|
| **North America** | 🔴 **only 10 % of institutions have formal AI guidelines**; **71 % of US teachers lack AI training**; NA holds the largest share (~36 %); regulation described as a *"relative regulatory vacuum"* with state-level pieces (**Colorado**, **Texas**) and no education-specific federal instrument | 🟢 productive — policy **and** adoption |
| **EMEA** | the **Council of Europe Education Department** is the clearest education-specific regulatory actor (working conferences on regulating AI in education); EU AI Act remains the binding anchor; CompTIA's 2026 outlook puts regulatory pressure at the centre of regional IT planning | 🔴 **thin** — see `P546`'s sibling finding below |
| **APAC** | 🔴 **no education-specific AI rule found**; Singapore's consultations are **financial-sector**; **OpenAI appointed an ANZ policy lead** as Canberra tightens AI governance and copyright; corporate upskilling moves instead (**Pearson + TCS** alliance, **LearnUpon** Sydney HQ); "AI sovereignty" is the region's 2026 pacing theme; 57 % of Asian organisations use AI in ≥1 area (Diligent/SID/GIA) | 🔴 **thin for education** |
| **LATAM** | **no unified regional framework for AI in higher education**; **Chile** leads with a national AI policy since 2021 plus a bill in discussion; **Brazil** and **Colombia** have national strategies but no education-specific rules; **Mexico** has non-binding recommendations only (**SEP**, **ANUIES**, Observatorio IA); **Brazil and Argentina are diverging** on AI policy outright (June 2026); **Peru** has filed the most AI bills; **Latam-GPT** (CAF + AWS) status still unconfirmed | 🟢 **richest channel of the four** |

### 🔴 `P546`'s sibling — the region-acronym defect is **asymmetric**, and that is actionable

`P513` established that `EMEA` and `APAC` are **trade jargon education sources do not use about
themselves**. 🟢 **This pass measures something `P513` did not: the defect is not uniform across the
four regions.**

| Acronym as queried | What the education channel returned | Why |
|---|---|---|
| **LATAM** | 🟢 education-native sources: UNESCO IESALC, UNU-IAS, SciELO, an Ibero-American comparative analysis, IDB, Brookings | the Spanish/Portuguese academic and multilateral literature **does** write about *América Latina* as a unit |
| **North America** | 🟡 market research plus a usable regulatory read | a real, if vendor-heavy, channel |
| **EMEA** | 🔴 enterprise IT: CompTIA, Workday, a telecoms research note — with the channel stating outright it found **no education-specific adoption data** | nobody in education calls their system "EMEA" |
| **APAC** | 🔴 enterprise IT and board-governance material, explicitly **no education-specific rules** | same |

🟢 **The operational rule this leaves written:** run the regional probe **as prescribed for LATAM and
North America**, and for EMEA and APAC **substitute the national instrument** (ministry, Council of
Europe, MOE, national curriculum authority) before concluding anything. 🔵 **Two of the four regions
are cheap and two need a different query — knowing which is which is worth more than running all four
identically.**

## Opportunities by region — superseded (the live block is at the top of this file)

🔵 **The file's single canonical block (`P383`), refreshed by pass 47 on 2026-10-08.** Every
subsection states what the regional channel returned **and what it did not** — an informed gap is
information, while a blank subsection looks exactly like coverage.

### North America

- 🟡 **Regional forecast: ~$951M (2024) → ~$2.3B (2029), CAGR 15.9%** (market-research). 🔴 **See
  `P515` above: that CAGR cannot be reconciled with the global 31–41% series while the same channel
  puts this region at ~36% of the market.**
- 🟢 **Adoption:** student usage **86% across 16 countries**; the region holds **~36%** of market
  share.
- 🔴 **The governance gap is the offer: ~10% of institutions have formal AI guidelines and ~71% of
  U.S. teachers report no AI training.** Enablement and policy work, not model work.
- 🟡 **Regulation is a vacuum with state-level patches** — Colorado and Texas named as introducing
  piecemeal requirements; no federal clearance regime comparable to FDA device review. Decisions sit
  with individual districts and universities.
- 🟢 **Funders are moving:** Carnegie Mellon with the Gates Foundation put **$55M** into AI courseware
  for gateway college courses; a **$169M** public commitment to responsible AI in higher education was
  reported in Q1 2026. 🟡 **The source does not name the government, so this is not citable as US
  federal spend.** OpenAI launched a country-level education programme with eight national partners.
- 🟢 **Studio opening:** institutional **AI policy + staff enablement** priced against the 10%/71%
  gap, with the licence-regime map in `verticals/solutions.md` deciding what can be shipped closed.
  🟢 **`P576` matters here:** Sakai (`ECL-2.0`) is the one LMS on this shelf a studio can build closed
  work on.

### EMEA

- 🟢 **The one hard regulatory deadline in any region this pass: the EU AI Act classifies education
  AI as high-risk, with full effect in August 2026.** 🔵 **Secondary reading only — `eur-lex.europa.eu`
  and `data.europa.eu` remain proxy-blocked (`Gap 56`), so no EU date here is primary, and `Gap 241` /
  `P555`'s date contradiction stands unresolved.**
- 🔴 **Declared gap — the channel is thin AND stale.** The mandated EMEA query returned enterprise-AI
  material, a Workday study from **2023**, and a Council of Europe working conference from **October
  2024** presented as current. 🔴 **No 2026 EMEA data on adoption in schools or universities was
  returned.** 🔵 **Recorded explicitly: a hole in the channel, not coverage.** Next probe named:
  national ministry AI-in-schools programmes and the Europe EdTech 200 list.
- 🟡 **What is current:** a February 2026 enterprise report on mounting regulatory, data-privacy and
  stakeholder-trust pressure; **38% of EMEA organisations have not begun piloting**; GDPR as the
  structural constraint on deployment shape.
- 🟢 **UK, named players:** government as funder with **£200M+** committed at its AI Adoption Summit,
  and **Cisco, IBM, BT and Rolls-Royce** as delivery partners for AI skills.
- 🟢 **Studio opening:** **AI Act Article 50 conformance for education providers**, and this KB already
  ships executable instruments for it — `compose/code/aiact-50-2-marking/`, `-spans/`, `-pack/`,
  `-exposure/`. Pair with **ECL-2.0 Sakai** where the deliverable must stay closed, and avoid Open edX
  (`AGPL-3.0`) for hosted closed work.

### APAC

- 🔴 **Declared gap: the education-specific channel returned almost nothing.** The mandated APAC query
  returned enterprise AI and board-governance material. 🔵 **Reproduced on a fresh run and recorded as
  absence.** Next probe named: ministries of education in Singapore, Australia, India and China
  directly, since the regional-aggregate channel does not carry education.
- 🟡 **What did return is CORPORATE LEARNING, not education providers — and that distinction is the
  finding.** Named: **Pearson + TCS** multi-year AI learning alliance for employer skills gaps;
  **LearnUpon** new Sydney HQ with `Create+` AI course authoring; **Alteryx** Academy relaunch with
  AI learning paths; **NIIT MTS** on Training Industry's 2026 top-20 custom content list.
- 🟡 **Governance:** **57% of organisations in Asia** already use AI in at least one area, with
  frameworks struggling to keep pace (Diligent Institute, with Singapore and Australian governance
  bodies). **OpenAI appointed an ANZ policy lead** as Australia tightens AI governance and copyright
  rules. Singapore's consultations on AI in financial institutions are the template regulators are
  reusing.
- 🟢 **Sovereignty is the regional frame** — Forrester expects a shift from pilots to
  *"sovereign-by-design"* execution. 🟢 **Studio opening:** self-hosted, sovereign-by-default stacks;
  the offline-capable rows on this shelf (Kolibri) and a local-inference tier matter more here than in
  any other region.

### LATAM

- 🟢 **The best-measured region in this channel this pass, from two independent surveys.**
- 🟢 **UNESCO IESALC with UNU-IAS — 200 higher-education institutions across 19 countries** (fielded
  Aug–Oct 2025): **87%** use AI in at least one area and **74%** for teaching tasks such as lesson
  planning and grading, but only **26%** have any formal framework.
- 🟢 **By institution type — a three-way split no other region reports, and it is directly
  targetable:** private non-profit **84%**, public **68%**, private for-profit **52%**.
- 🟢 **Digital Education Council — 30 000+ responses across 29 institutions** (with Tecnológico de
  Monterrey's Institute for the Future of Education): **92% of students and 79% of faculty** actively
  engaging. 🔴 **Only 19% of faculty use AI for assignment feedback while 50% of students support it**
  — a measured product gap, not an inferred one.
- 🟡 **Regulation: no unified regional framework.** Chile leads with a National AI Policy since 2021
  and a bill under discussion; Brazil and Colombia have national strategies but **no education-sector
  rules**; Mexico's SEP, ANUIES and Observatorio IA have issued **non-binding** recommendations only.
  The IDB's **ILIA** index measures readiness, adoption and governance across 19 countries.
- 🔴 **Two sources disagree on the same quantity:** UNESCO reports **26%** with a formal framework,
  while a conference summary claims **30%** of universities have published AI policies. 🔵 **Both
  recorded; neither averaged.**
- 🟢 **Named players:** UNESCO IESALC, IDB, Digital Education Council; Tecnológico de Monterrey, UNAM,
  UPC (Peru), Pontificia Universidad Católica de Chile.
- 🟢 **Studio opening:** the **26% / 87%** framework gap is the clearest single opportunity in any
  region this pass — governance scaffolding for institutions already running AI without it — then the
  **19% / 50%** feedback gap as a product.

### Global

- 🟢 **The one finding that places in all four regions with evidence: institutions run AI at ~87% and
  govern it at ~26%.** Every regional subsection above is written against that gap.
- 🔴 **The agent shelf is saturated for the fifteenth consecutive pass.** The mandated agent query
  returns the **horizontal** shelf plus curricula and catalogues, in every region. 🔵 **No
  education-native agent exists to recommend**, which is why the composable value is in the
  **verticals** (`verticals/solutions.md`) plus a horizontal agent, not in an education agent.
- 🟡 **The licence regime, not the model, decides what a studio can sell** — and this pass corrected
  it in both directions (`P571`–`P579`). Sakai is `ECL-2.0` and permissive; Moodle is `GPL-3.0`, not
  `AGPL-3.0`; Open edX is `AGPL-3.0` and unsuitable for closed hosted work.
- 🔵 **Market size is a spread, not a number:** 2026 base readings of **$10.6B** and **$11.4B**, 2033–34
  horizons between **$57.2B** and **$79.6B**, CAGRs from **15.9%** (North America) to **41%** (global).
  🔵 **Carried as a range with source types, per `P515`.**
- 🟡 **Segment shape (2024 bases, secondary):** cloud deployment **71.22%** share; STEM **34.78%** of
  revenue; **language learning the fastest-growing** segment.

## 🟢 Forty-third pass, 2026-10-07 — the region channel finally returns a **single comparable instrument** across all four regions, and it reorders them against this KB's assumption

⏱️ **Tenth pass of this date.** 🔵 **Every figure below is secondary and carries base year, scope and
publisher, per `P515`.** 🔴 **`eur-lex.europa.eu` and `data.europa.eu` remain blocked by the proxy
(`Gap 56`), so no EU date below is cited as primary — see `P538` in `intel/trends.md`.**

### 🟢 `P539` — one survey, four regions, the same question: the first comparable regional measurement this file has held

🔵 **Why this is worth a finding of its own.** Ten passes of regional sweeps returned *different*
instruments per region — a national curriculum mandate here, a teacher-use percentage there — and
`P513` already recorded why (the acronyms `EMEA`/`APAC` are trade jargon education sources do not use
about themselves). 🔴 **Incomparable measurements cannot be ranked, so this file has never been able to
say which region leads.** 🟢 **The Digital Education Council's 2026 global survey asks one question of
all four: 45,398 responses across 35 countries.**

| Measure | Value | 🔵 Note |
|---|---|---|
| Students using AI (global) | **88%** | |
| Faculty using AI (global) | **77%** | |
| Students who believe instructors are **well equipped to guide** AI use | 🔴 **29%** | 🔴 **The gap this file should be selling into**: near-universal use, and a 59-point confidence deficit against it |

**Faculty intent to use AI in teaching, by region — and the order is not the one this KB assumed:**

| Region | Faculty intent | 🔵 Note |
|---|---|---|
| **LATAM** | 🟢 **94%** | 🟢 **Highest of the four.** This file has priced LATAM as a follower region for ten passes |
| **APAC** | 92% | |
| **EMEA** | 89% | |
| **North America** | 🔴 **67%** | 🔴 **Lowest by 22 points** |

🔴 **One conflict recorded rather than resolved.** A summary from the same publisher states EMEA has
*"the lowest future AI adoption intent among all regions"*, which contradicts the 89% / 67% figures in
the survey coverage. 🔵 **Either the summary refers to a different metric or to a different regional
definition. The figures are quoted; the summary's claim is not.** → **`Gap 242`**.

🟢 **The commercially useful reading, stated plainly:** demand intent is **inverse** to regulatory
burden. The region with the heaviest binding obligations (EMEA, and APAC per `P530`) does not have the
weakest intent — **North America does**, with the lightest federal framework of the four. 🔴 **So
"regulation suppresses adoption" is not what this measurement shows**, and a studio pitch built on
that premise is built on nothing.

### 🔵 Regional regulatory and adoption positions measured this pass

🔵 **Restated in full so silence is not read as coverage** (`P479`'s sibling rule). Each row names its
instrument, because `P513` is this file's record of what happens when a region returns a different
kind of fact from its neighbour.

| Region | Instrument measured this pass |
|---|---|
| **North America** | 🟡 **Fragmented and sub-federal.** Over half of US states had enacted K-12 AI guidance by early 2026. **Binding**: Idaho SB 1227 (statewide framework, AI literacy standards, prohibits AI replacing teachers); Ohio (districts to adopt AI-use policies by 2026-07-01). **Introduced, not law**: California AB 1159 (bars training on student data absent direct school benefit), New York A.9190 (would prohibit most classroom AI below grade 9), Arizona HB 4040 (policies for schools *and* public universities). Vermont HB 650 requires ed-tech providers to register and certify privacy compliance annually. Federal action is **guidance, not rules** — a Dept. of Education Dear Colleague Letter urging outcome-based evaluation of AI tools; HR 8747 advanced in committee only. 🔴 **One claim NOT corroborated and therefore not carried: a "$2.5 B federal AI grant programme", single low-quality source** |
| **EMEA** | 🔴 **The clock moved — see `P538`.** Annex III high-risk education obligations **deferred to December 2027**; **Article 50** transparency **still 2026-08-02**; **Article 4** AI-literacy in effect with relaxed scope. Education policy otherwise remains **national**; the Commission with the OECD has issued a draft **AI Literacy Framework** for primary and secondary education to align national approaches. 🔵 Non-EU EMEA: South Africa's draft National AI Policy is in progress |
| **APAC** | 🟢 **The earliest binding obligations, confirming `P530`.** **South Korea**: AI Basic Act in force **2026-01-22**, and education is named a **high-impact** domain, so it carries the heaviest duties — MSIT has signalled 2026 as a pilot year with a **one-year grace period on penalties**. **China**: binding generative-AI measures, algorithm registration, and mandatory synthetic-content labelling since 2025-09; compulsory national AI curriculum since the 2025-26 school year. **India**: AI and computational thinking **mandatory from Class 3** across government and private schools from 2026-27, with a ₹500 crore centre of excellence and the ₹10,372 crore India AI Mission; IT Rules amendments on AI-generated content in force **2026-02-20**; dedicated AI legislation **signalled but not adopted**. **Japan**: promotional framework law (May 2025), voluntary training-data disclosure still proposed. 🔴 **Korea's textbook rollout is the cautionary case**: mandatory AI textbooks planned from 2025 sat **below 30% adoption** by March, and in August the National Assembly **stripped them of official status** after unions said the pace had outrun preparation |
| **LATAM** | 🟢 **Highest faculty intent of the four (94%), and the teacher-use data agrees.** TALIS 2024: secondary teachers who had used AI in the previous year — **Brazil 56%, Chile 55%, Colombia 53%, Costa Rica 52%**, against an **OECD average of 36%**. Brazilian youth: **65%** of internet users aged 9–17 use AI tools (Cetic.br, 2026). **Regulation**: Brazil's comprehensive AI bill is **not passed**; ANPD runs a **pilot regulatory sandbox for AI and data protection until December 2026**; further bills address mental health, age warnings and AI-content labelling. **Mexico has no education-specific AI rules**; 2026 amendments to copyright, labour and criminal law are pending publication in the DOF, and Mexican courts have held AI-generated content lacks copyright. **Funding**: Google.org is funding AI education across **nine countries** (AR, BR, CL, CO, DO, SV, MX, PE, UY), targeting **1.25 M students by 2028**, on curriculum co-developed with Google DeepMind and the Raspberry Pi Foundation. **UNESCO** has launched the first UN-anchored **regional observatory on AI in education** for LAC, with a Mexican pilot (CONALEP, DGETI) and an agreement with Tec de Monterrey. **IDB** reviewed **193** regional AI initiatives: **59%** used generative AI, 27% language models, 24% NLP. 🔴 **The readiness counterweight, carried because it contradicts the intent figure**: CENIA found **13 of 19** LAC countries do not teach early AI adoption in schools |

## Opportunities by region — superseded (the live block is at the top of this file)

### North America

🔴 **The lowest faculty intent of the four regions (67%) is the fact to build on, not around.** The
demand is not for more capability — it is for **defensibility**. Three concrete openings:

- 🟢 **Vendor-accountability packaging.** Vermont's annual registration-and-certification duty and the
  FERPA/security questionnaires now standard in higher-ed procurement make *compliance documentation*
  a product feature. 🟢 `P533`'s emitter is relevant here in an unobvious way: a **parametric item
  bank** is the cheapest answer to an integrity-and-assessment review, because every student sees a
  different instance.
- 🟡 **Scaffolded-access policy implementation.** Districts are landing on grade-banded rules (K-6
  prohibited, 8-12 permitted with teacher authorisation and mandatory citation). That is a
  **configuration problem** across an LMS estate, and it recurs per district.
- 🔴 **Not an opportunity**: single-state compliance products. With rules split across states and most
  of the strictest bills still only *introduced*, a product keyed to one statute has no second buyer.

### EMEA

🟢 **The sixteen-month Annex III deferral (`P538`) is a timing opportunity and a trap.**

- 🟢 **The real window is conformity-assessment readiness, not relief.** A system sold in 2026 into
  admissions or assessment must be conformant by **December 2027**, and conformity is a property of
  the system. 🟢 **Build the technical file while the deadline is soft; that is the engagement.**
- 🟢 **Article 50 is live now (2026-08-02) and did not move.** Disclosure-and-marking work is
  immediately billable, and this KB already holds the instruments for it
  (`compose/code/aiact-50-2-*`).
- 🟢 **Article 4 AI-literacy, plus the Commission/OECD draft AI Literacy Framework**, makes staff
  capability a procurement line item across national systems that otherwise share no policy.
- 🔴 **Stated gap**: with eur-lex blocked (`Gap 56`), this KB cannot cite the amending instrument
  primarily. 🔴 **Do not put the December 2027 date in a client deliverable without pinning it.**

### APAC

🟢 **The earliest binding clock of the four regions, and the largest compulsory-curriculum demand.**

- 🟢 **Korea is the nearest-term regulated market**: education is a named **high-impact** domain under
  an Act already in force, with a grace period that ends. 🟢 **High-impact classification work has a
  deadline and a statutory hook** — the clearest compliance engagement in any region.
- 🟢 **India is the largest volume opportunity in this file**: AI mandatory **from Class 3** from
  2026-27 across government *and* private schools, with state funding attached. The bottleneck is
  **teacher capability and content at national scale**, not platform.
- 🔴 **Read Korea's textbook reversal as a design constraint, not a footnote.** Mandated adoption with
  sub-30% uptake, reversed by the legislature after union pressure, is what happens when rollout pace
  outruns teacher preparation. 🟢 **Sell the preparation programme as part of the platform or expect
  the same reversal.**
- 🟡 **China's compulsory curriculum is real but the market is largely closed** to a foreign studio;
  treat the synthetic-content labelling regime as the exportable lesson.

### LATAM

🟢 **Highest faculty intent of the four regions (94%) and the highest teacher use against the OECD
average — and a readiness deficit that contradicts both.** That contradiction is the opportunity.

- 🔴 **The binding constraint is not willingness; it is that 13 of 19 LAC countries do not teach early
  AI adoption at all** (CENIA). 🟢 **So the sellable unit is curriculum-plus-enablement, and there is
  already third-party money in it**: Google.org across nine countries to 1.25 M students by 2028, and
  UNESCO's LAC observatory as the convening body with CONALEP/DGETI and Tec de Monterrey.
- 🟢 **Portuguese-language assessment is the one place this KB holds a genuine asset advantage**:
  `essay-br` (MIT, human-graded on ENEM C1–C5, `P524`) plus — new this pass — the **Apache-2.0
  reference implementation** `wwrwbs/AI_AWE` (`P535`). 🔴 **The scorer still does not exist in
  Portuguese (`Gap 236`) and the feature layer is English-locked (`Gap 239`)**, so this is a build,
  not an integration — but it is now a *retarget* rather than a greenfield build.
- 🔴 **Spanish-language essay scoring is NOT the symmetric opportunity, and `P537` is why.** Chile's
  PAES has **no essay component**, so there is no rubric to automate. 🔵 **Qualify by whether the
  country's exam grades writing against a published rubric before scoping any Spanish essay work.**
- 🟡 **Regulatory timing favours moving now**: Brazil's comprehensive bill is unpassed and the ANPD
  sandbox runs only to December 2026 — a participation window, and it closes.

## 🟢 Forty-second pass, 2026-10-07 — a fourth market denominator widens `P515`'s spread to 6×, and the regulatory clock this KB has been reading off the EU calendar is **not** the earliest one

⏱️ **Ninth pass of this date.** 🔵 **Every figure below is secondary and carries base year, scope and
publisher, per `P515`'s rule: that rule is the reason this section is readable, and it is applied to the
figures this pass found *and* to the one this file already carries.**

### 🔴 `P529` — four publishers, four 2026 denominators, a **6× spread**; and this KB's standing figure is one of them

🔵 **`P515` found three irreconcilable denominators. A fourth has been measured, and the spread is now
wide enough that the number is meaningless without its series.**

| Publisher | Base year | 2026 value | Terminal value | CAGR | 🔵 Note |
|---|---|---|---|---|---|
| **Grand View Research** | 2025 ($8.3 B) | 🔴 **$11.4 B** | $57.2 B by 2033 | 25.9% | 🔴 **The highest 2026 figure and the *lowest* growth rate** |
| **Research and Markets** (report dated Feb 2026) | 2025 | **$10.6 B** | $42.48 B by 2030 | 41.5% | 🟢 **This is the series this KB has carried since pass 2** — now identified by publisher |
| **Precedence Research** | 2025 ($7.05 B) | **$9.58 B** | $136.79 B by 2035 | 34.52% | 🔵 Longest horizon, so least comparable |
| **Market Reports World** | 2025 | 🔴 **$1.94 B** | — | 42.95% | 🔴 **Lowest 2026 figure — 5.9× below Grand View for the same year** |
| **Technavio** | 2025 | 🔴 **not a total** | *incremental* growth of $3.37 B, 2025–2030 | 45% | 🔴 **Measures an increment, not a market. Not comparable, and is quoted as though it were** |
| **The Business Research Company** | 2025 | $4.09 B *(higher-ed only)* | $13.46 B by 2030 | 34.7% | 🔵 **A sub-segment**, correctly scoped and often cited as the whole |

> **`P529`.** 🔴 **Four publishers put 2026 between $1.94 B and $11.4 B — a 5.9× spread for a year
> already three quarters elapsed.** 🟢 **Grand View and Market Reports World are the useful pair: they
> disagree 5.9× on the level and sit within 17 points on the growth rate, which is the signature of
> **different scope definitions**, not different forecasting.** 🔵 **`P515` said `P477` was necessary and
> not sufficient; this adds what is sufficient — carry the publisher, the base year, **and whether the
> figure is a total, an increment or a segment**, because two of the six above are not totals and both
> circulate as if they were.** 🟢 **This file's standing $10.6 B → $42.48 B is Research and Markets,
> 2025 base, whole-market scope, and it sits mid-spread — so it is retained, now attributed, and
> 🔴 **never to be quoted as "the" market size.**

### 🟢 `P530` — the earliest binding education-AI obligation is **APAC's**, not the EU's, and this KB has been pricing engagements off the wrong calendar

🔵 **The instruments below are already held in this file. What is new is the comparison, and it inverts
the framing eight passes have used** — `P505` and `P514` both treated the **EU Annex III** date as *the*
regulatory clock, and corrected it twice for staleness without ever asking whether it was the earliest.

| Region | Instrument | Status on 2026-10-07 | 🔵 Education treated as |
|---|---|---|---|
| 🟢 **APAC** | **South Korea, AI Basic Act** | 🔴 **IN FORCE since 2026-01-22** — grace period through 2026 focused on guidance over penalties | 🔴 **"high-impact"** |
| 🟢 **APAC** | **Vietnam**, high-risk list | 🔴 **In force** | 🔴 **Named explicitly** — automated assessment and behavioural monitoring |
| 🟡 **EMEA** | **EU AI Act, Annex III** | 🟡 **DEFERRED to 2027-12-02** by the Digital Omnibus (OJ 2026-07-24, effective ~2026-07-27) | 🔴 High-risk: access, assessment of learning outcomes, educational path, exam monitoring |
| 🟢 **EMEA** | **EU AI Act, Articles 50 + GPAI enforcement** | 🟢 **IN FORCE since 2026-08-02** — *not* deferred | transparency duties apply now |
| 🔵 **NA** | federal | 🔴 **No binding federal AI curriculum standard.** The *K-12 AI Literacy and Readiness Act of 2026* advanced on a July markup and 🔴 **is not enacted**; Aug-2026 Dept. of Education guidance is 🔵 **non-binding** | — |
| 🟢 **NA** | states | 🟢 **Binding and live** — 134 AI-in-education bills across 31 states in 2026; **40 states + Puerto Rico** have guidance as of Sept 2026 | 🔴 Oklahoma and Maryland **bar AI from high-stakes decisions about students** and require human oversight |
| 🔴 **LATAM** | Brazil **PL 2.338/2023** | 🔴 **Still pending** (Senate approved versions 2024-12-10), risk-based | 🔵 **Education not clearly singled out in the sources read** |
| 🟢 **LATAM** | Brazil **LGPD** | 🟢 **In force** | 🟢 **Already bites**: a right to request review of decisions made *solely* by automated processing |

> **`P530`.** 🔴 **A studio sequencing compliance work off the EU calendar is ~23 months late for Korea
> and misses that the EU's own transparency duties are already live.** 🟢 **The correct ordering of
> binding obligations today is: **Korea and Vietnam now → US states now → EU transparency now → EU
> Annex III 2027-12-02 → Brazil when PL 2.338 passes.** 🔵 **And the deferral is not relief: the EU
> obligations themselves did not change, the FRIA is still required before a high-risk system goes into
> use, and the Article 4 AI-literacy duty remains — softened by the Omnibus from achieving a defined
> staff competence level to taking *"measures supporting"* AI literacy.** 🔴 **The one place the deferral
> genuinely matters is exam scoring, and `P514` already fixed that date at 2027-12-02.**

### 🔵 Regional adoption measured this pass

| Region | Figure | Series |
|---|---|---|
| 🔴 **APAC** | Faculty **future** AI-adoption intent **fell 76% → 67%** between 2025 and 2026 — 🔴 **the lowest of any region** | Digital Education Council, *AI in Higher Education Global Survey 2026* |
| 🟢 **APAC** | India: AI and computational thinking **mandatory from Class 3** in 2026–27; ~**10 M teachers** need training against **15%** AI-fluent in a 2025 survey | 🔵 Secondary; the teacher-capacity ratio is the operative number |
| 🟢 **LATAM** | **>50% of teachers in Chile and Brazil already use AI tools**, while 🔴 **<10% of regional institutions have formal guidelines and the capacity to apply them** | UNESCO |
| 🟢 **LATAM** | **193 AI initiatives** catalogued across LAC — 🔵 **mostly administrative rather than pedagogical** (e.g. Rio de Janeiro's education secretariat automating school-invoice validation) | IDB |
| 🟢 **NA** | 54% of students and 53% of teachers used AI for school in 2025 | RAND, cited secondarily |

🔵 **The LATAM pair is the most actionable figure in this table**: teacher adoption above 50% against
institutional readiness below 10% is 🟢 **a governance gap, not a technology gap** — the demand already
exists and the thing missing is policy, capacity and defensibility.

## Opportunities by region — superseded (the live block is at the top of this file)

### North America

🟢 **Sell the audit trail, not the model.** Oklahoma and Maryland bar AI from high-stakes student
decisions and require human oversight; 40 states plus Puerto Rico now have guidance; and 🔴 **there is no
federal standard to converge on**, so a district's exposure is **state-shaped**. The buyable artefact is
a **human-in-the-loop evidence layer** over whatever scoring a district already runs: who decided, on
what evidence, which human reviewed it, and the record to show a state auditor. 🔵 **California's A.B.
1159 adds a second hook** — restricting use of student data to train models — which makes
**train-on-your-own-corpus, keep-it-in-district** a compliance feature rather than an engineering
preference, and `P524`'s corpus-plus-open-weights pattern is exactly that shape in a language the US
market does not need. 🔴 **Not a market for a sealed proprietary scorer.**

### EMEA

🟢 **2027-12-02 is a delivery date, and the work that fills it is evidence production.** Annex III
deferral did not change the obligations: a **FRIA before deployment**, technical documentation, and
defensible assessment decisions. 🟢 **Two things are already live and are the near-term sale**: Article 50
transparency duties and the Article 4 AI-literacy duty (now *"measures supporting"* AI literacy — 🔵 a
lower bar, and still a programme someone must run). 🟢 **The permissive shelf is strongest exactly here**:
`KernEqWPS` (MIT, `P508`) and `EqUMP` for comparability evidence, and the 1EdTech-certified QTI 3 delivery
tier. 🔴 **And `P527` prices the one honest gap** — the QTI writer cannot author parametric variants, so
an item-bank engagement must budget the emitter or hand-author the template XML.

### APAC

🟢 **The most urgent region, and the one this KB has been treating as the least.** Korea's AI Basic Act
has been **in force since 2026-01-22** with education as high-impact and its guidance-focused grace
period **expiring at the end of 2026** — so a Korean engagement needs compliance evidence *now*, not in
2027. Vietnam names automated assessment and behavioural monitoring in its high-risk list. 🔵 **India is
a capacity engagement, not a compliance one**: mandatory AI from Class 3 in 2026–27 against ~10 M
teachers needing training — **teacher-facing tooling and training pipelines at national scale**. 🔴 **The
contrarian signal to respect: faculty intent to adopt *fell* 9 points to 67%, the lowest of any region**,
so higher-ed buying here is sceptical and a pilot must prove itself against human marking rather than
assert a productivity claim.

### LATAM

🟢 **The clearest opportunity in this file, and this pass made it concrete.** Demand is proven (>50% of
teachers in Chile and Brazil already using AI) and readiness is absent (<10% of institutions with
guidelines and capacity) — 🔵 **the gap is governance, and governance is a services engagement.** 🟢
**Brazil specifically now has a buildable stack**: `essay-br` (**MIT**, human-graded against the ENEM
C1–C5 rubric, `P524`) + an open-weight model + calibration + LanguageTool as an ownable C1 feature source
(`P525`, `P526`), wired in `compose/patterns.md` (`P532`). 🔴 **And the competitive fact that makes it
worth doing: the entire incumbent Portuguese corretor tier is *ungranted* (`P522`), so there is no open
competitor to displace — six readable design references and not one shippable starting point.** 🟢
**LGPD's review right for solely-automated decisions makes the human-in-the-loop design mandatory rather
than optional**, which suits a studio and disadvantages a pure-product vendor. 🔴 **Spanish-speaking
LATAM is *not* the same opportunity** — `P531` found no graded corpus and no national rubric to
standardise on, so there the first deliverable is the rubric, not the model.

## 🟢 Forty-first pass, 2026-10-07 — the regional channel's defect is the **acronym**, and fixing it placed national policy instruments in the two regions that had returned nothing for eight passes

⏱️ **Eighth pass of this date.** 🔵 **Every figure here is secondary and carries its series (`P477`).**

🔴 **Channel state, declared rather than implied.** `api.github.com` **403**; `github.com` HTML **403 for
every input including the negative control** (`P510`); `eur-lex.europa.eu` unreachable since pass 32;
`www.marketsandmarkets.com` and `unu.edu` `EGRESS_BLOCKED` at pass 39; `planbe.eco` at pass 40. 🔴 **This
pass adds five:** `cran.r-project.org`, `docs.moodle.org`, `oecd.ai`,
`eurydice.eacea.ec.europa.eu`, `publications.iadb.org` — **all `000`/`403 CONNECT`, negative control
included, so uniformly blocked rather than selectively**. 🔴 **No market figure and no regulatory date
below is first-hand verifiable; every one is read from search summaries rather than fetched pages.**

### 🟢 `P513` — the **region acronym** is the defect: `EMEA` and `APAC` are trade jargon that education sources do not use about themselves

🔴 **For eight consecutive passes the mandated `AI education {region} 2026 adoption regulation players`
sweep has returned, for two of four regions, either nothing new or nothing about education.** 🔵 **Pass
40 recorded that honestly and read it as saturation.** 🔴 **It was not saturation. It was the query.**

| Query shape | EMEA returned | APAC returned |
|---|---|---|
| 🔴 **Mandated, acronym** — `AI education EMEA\|APAC 2026 adoption regulation players` | 🔴 **Zero education content.** Enterprise AI: *94% likely to invest in AI training*, *60% of EMEA finance teams piloting-to-mature* | 🔴 **Zero education content.** *48% of governance leaders*, *57% of Asian organisations*, *sovereign-by-design*. 🟢 **The summary said so itself**: *"focus primarily on enterprise AI adoption rather than education-specific information"* |
| 🟢 **Country-named** — `AI schools Germany France Netherlands Finland 2026 policy…` / `AI education policy Japan Singapore India South Korea 2026…` | 🟢 **Named national instruments** — see below | 🟢 **Named national instruments** — see below |

> **`P513`.** 🟢 **`EMEA` and `APAC` are *vendor territory* labels. Education policy is made by
> **ministries**, published by **countries**, and indexed under country names — so an acronym query
> retrieves the corpus that uses the acronym, which is enterprise IT marketing.** 🔵 **`P503` found that
> query *shape* beats query *topic* on a saturated library shelf; `P513` is the same mechanism on the
> **regional** channel, and it is the more expensive of the two, because eight passes of apparent
> regional silence were a retrieval artefact.** 🟢 **`LATAM` and `North America` escaped it only
> partially — both returned content, and the LATAM acronym query still missed every national policy
> instrument that the Spanish country-named query returned on one attempt.**

🔵 **The standing remedy, for every later pass: run the mandated acronym sweep (it is mandated, and
recording it is how silence is distinguished from coverage) and then *always* run a country-named sweep
per region. The acronym sweep is the control; the country sweep is the measurement.**

### 🔴 `P514` — `P505`'s stale Annex III date is **not EMEA-confined**; it leaked into the NA and LATAM channels

| Sweep | Stale claim returned this pass |
|---|---|
| 🔴 **North America** | *"the EU AI Act, taking full effect in **August 2026**, classifies both healthcare and education AI as **high-risk**"* |
| 🔴 **LATAM** | *"the AI Act, whose regulatory framework progressively entered into force from **August 2026**, establishing four risk levels"* |
| EMEA | 🔵 Returned *"The EU AI Act's general application date is **2 August 2026**"* — **true as stated**, and 🔴 **one sentence away from the false claim**, which is why the error propagates |

🟢 **The dates this shelf holds, unchanged and still the commercial fact of the quarter:**

| Obligation | Applies from | Status |
|---|---|---|
| 🟢 **Article 50 transparency** (AI disclosure, synthetic-content marking) | 🟢 **2026-08-02** | 🟢 **In force. Did not move** |
| 🔴 **Annex III stand-alone high-risk** — education access, student evaluation, exam scoring | 🟢 **2027-12-02** | 🔴 **Deferred 16 months by the Digital Omnibus** |
| **Annex I embedded** high-risk | **2028-08-02** | Deferred 12 months |

> **`P514`.** 🔴 **`P505` scoped the staleness to the EMEA channel. It is a property of the *corpus*, not
> of a region's sweep** — the Act's **general application** date (2026-08-02, true) and its **Annex III
> high-risk** date (2027-12-02, deferred) are routinely collapsed into one sentence, and that collapsed
> sentence is now reproducing in regions that have no reason to discuss EU law. 🟢 **Consequence for a
> studio: a North America or LATAM engagement can arrive with the EU error already installed in the
> client's own deck.** 🔵 **Correcting it is a credibility win on first contact, in regions where no one
> expects the adviser to know EU dates better than the EU-focused briefing did.**

### 🔴 `P515` — three mutually inconsistent 2025/2026 market denominators, two of them **in the same summary**

| Series | 2025 base | Trajectory | CAGR |
|---|---|---|---|
| A | **$6.4 B** | → **$79.6 B (2034)** | **31.35%** |
| B | 🔴 **$7.52 B** | → **$10.6 B (2026)** | 🔴 **40.9%** |
| C (North America only) | **$951 M (2024)** | → **$2,303.2 M (2029)** | 🔴 **15.9%** |
| Held series (pass 33–40) | — | NA **$3.68 B (2026) → $32 B (2030)**, NA = **36%** of global | — (🔴 `P489` adjudicated **against** the $32 B) |

🔴 **A and B were returned by the same sweep, in the same summary, and differ by 17% on the same year.**
🔴 **C cannot be reconciled with the held NA figure at all: $951 M (2024) growing at 15.9% does not reach
$3.68 B by 2026, and a region that is 36% of a $6.4 B global market is ~$2.3 B, not $951 M — unless the
two sources scope "AI in education" differently, which neither states.**

> **`P515`.** 🔵 **This shelf's rule (`P477`) is that every figure carries its series. 🔴 **That rule is
> necessary and no longer sufficient**: it prevents mixing series across passes, but it does not stop a
> *single* summary from containing two incompatible bases, which is what happened here.** 🟢 **The
> addition: a market figure is quotable to a client only with its **base year, its scope definition and
> its publisher**. None of A, B or C arrived with a scope definition, so 🔴 **none of them should appear
> in a client deliverable** — the honest line is *"published estimates for 2025 range from $6.4 B to
> $7.52 B and regional splits do not reconcile; here is why the range exists."* 🔵 **That sentence is
> worth more than a fabricated point estimate and is defensible under questioning.**

## Opportunities by region — superseded (the live block is at the top of this file)

🔵 **Four subsections, one per region, as this file's contract requires.** 🟢 **Every item below is placed
in the region whose instrument creates it.** 🔴 **Where a region's evidence is thin this pass, it says so.**

### North America

🟢 **New this pass:** a **$169 M** government commitment to responsible AI in higher education (**Q1
2026**); **OpenAI**'s country-level education programme with **eight national partners** (Q1 2026).
**Held:** **134 bills across 31 states** in the 2026 session; **CA AB 1159** (no training on student
data); **ID SB 1227**; **Oklahoma** and **Maryland** requiring human oversight and barring AI from
high-stakes decisions about students; the **K-12 AI Literacy and Readiness Act of 2026**; **60%** of US
K-12 teachers using AI tools in 2024-25, **32%** weekly. 🆕 **Colorado** and **Texas** named this pass as
piecemeal state requirements. Named players: **IBM, Microsoft, Google**.

| Opportunity | Why it is live here, specifically |
|---|---|
| 🟢 **A 50-state "AI in student decisions" compliance matrix as a product, not a slide** | 🔴 **There is no federal floor** — the sweep's own phrasing is *"no FDA equivalent for educational technology"*, and adoption decisions sit with individual districts. 🟢 **134 bills / 31 states means a district operating in two states has two different rule sets**, and Oklahoma's and Maryland's *human-oversight* requirements are an **architectural** constraint, not a policy document: they decide whether a model may be in the decision path at all |
| 🟢 **Human-in-the-loop evidence for high-stakes decisions** | 🟢 **The evidence layer this KB has been building since pass 33 — calibration, comparability (`P508`), DIF (`difair`, `aequitas`) — is exactly what "we did not let AI decide this alone" is demonstrated *with*.** 🔵 **Sell it as audit evidence, not as psychometrics** |
| ⚠️ **Teacher-facing tooling, with the adoption gap named** | **60%** used AI but only **32%** weekly: 🔵 **the gap between trial and habit is the deliverable** — workflow integration, not another tool |

### EMEA

🟢 **New this pass, and the first national instruments this region has yielded in eight passes
(`P513`):** **Germany** — the **Conference of Ministers of Education of the Länder (KMK)** adopted a
*"Recommendation for action for the education administration on the use of artificial intelligence in
school education processes"* (**October 2024**), covering **teacher training** and **clear legal
requirements protecting students' personal rights**. **Finland** — the Ministry of Education and Culture
with the National Agency for Education is developing **recommendations on AI in education**, framed on
**equal opportunity to benefit**. **Netherlands** — **Strategic Action Plan for AI (2019)** and **Vision
on Generative AI (2024)**. 🟢 **Ten of 27 member states show advanced public AI-Act implementation
evidence: Ireland, Spain, Lithuania, Finland, France, Germany, Netherlands, Poland, Cyprus, Italy.**
**Held:** EU market **$2.64 B (2026) → $8.0 B (2030) at 31.9%**; UK **£4 M** for lesson-planning and
marking tools; **OECD 2026 Digital Education Outlook**; only **10%** of 450+ institutions with formal AI
guidelines against **93%** of educators saying regulation is needed. 🆕 **Council of Europe** 2nd working
conference on the regulatory dimensions of AI in education (**October**); 🆕 a Nordic study of how AI use
is regulated across Nordic higher-education institutions.

| Opportunity | Why it is live here, specifically |
|---|---|
| 🟢 **Article 50 marking now, Annex III conformity staged to 2027-12-02** | 🟢 **Two engagements in the right order (`P514`).** 🔴 **A competitor selling emergency Annex III conformity today is selling against a date that moved** |
| 🟢 **The *Länder* are the buying unit in Germany, not the federation** | 🟢 **KMK issues a *recommendation*; sixteen Länder implement it sixteen ways.** 🔵 **That is a repeatable-engagement shape — build once against the KMK text, deliver per Land — and it is invisible to anyone selling to "EMEA"** |
| 🟢 **Guideline-writing as a wedge into platform work** | **10% with formal guidelines vs 93% wanting regulation** is 🟢 **a near-total addressable gap at the *governance* layer**, and governance documents are how a studio earns the platform engagement behind them |
| 🟢 **Standards-neutral evidence tooling** | 🟢 **The Annex III deferral's stated rationale was that harmonised standards were not ready.** 🔵 **A buyer cannot demonstrate conformity against benchmarks that do not exist, so the work that holds value through the deferral is calibration/comparability/DIF — standards-neutral by construction** |

### APAC

🟢 **New this pass (`P513`):** **Singapore** — a national initiative for AI literacy among students and
teachers, with **training on AI in education offered to teachers at all levels, including those in
training, by 2026**. **South Korea** — **AI coursework in the national curriculum across all grade
levels**, beginning with high school, and **AI "digital textbooks"** in selected grades and subjects
(**English, mathematics, coding**) from 2025; **KERIS** designing and piloting teacher development.
**India** — **AI education for children aged 8+ from mid-2026**, with the stated intent of making AI a
foundational, universal skill; 🔴 **experts named insufficient teacher training and hardware shortages as
the binding constraints**; `Embibe` named as a domestic edtech using AI for concept clarification and
performance prediction. **Japan** — ethical AI literacy and human-centred design, data literacy across
**all** university programmes, targeting **2,000 trained data scientists annually**. **Held:** **Vietnam's
Law on AI** (**2026-03-01**) naming education among six high-risk sectors — *automated assessment and
behavioural monitoring* — with National AI Database pre-registration, conformity assessment, human
oversight and **72-hour** incident reporting; **South Korea's AI Basic Act** (**2026-01-22**); **Taiwan's
AI Basic Act** (**2025-12**); APAC fastest-growing by GenAI revenue, **~65% YoY**.

| Opportunity | Why it is live here, specifically |
|---|---|
| 🟢 **Vietnam conformity is the hardest *and* earliest bar in the world for assessment AI** | 🟢 **In force since 2026-03-01, naming *automated assessment* explicitly, with pre-registration and 72-hour incident reporting.** 🔵 **A studio that can produce a Vietnam conformity dossier has, as a by-product, most of an EU Annex III dossier 21 months early** |
| 🟢 **India's constraint is teachers and hardware, not models** | 🔴 **The binding constraints are named by the country's own experts.** 🟢 **That points at offline-first and low-spec delivery — `Kolibri` (MIT) is the asset this KB already holds for exactly this** — and at teacher-enablement at national scale, which is curriculum work, not model work |
| 🟢 **South Korea's digital textbooks are an adaptive-content supply chain** | 🟢 **A national mandate across English, maths and coding** needs item banks, calibration and comparability across editions — 🔵 **the assessment chain in `verticals/solutions.md`, sold as content infrastructure** |
| 🟢 **Teacher-training delivery as the Singapore shape** | **All teachers including trainees by 2026** is 🔵 **a procurement with a deadline inside the current year** |

### LATAM

🟢 **New this pass (`P513`, Spanish-language country-named sweep):** **Colombia** — **National AI Policy
approved February 2025** with six strategic objectives including digital-talent formation, ethical
governance and institutional development; 🟢 **the first AI Faculty in Latin America at Universidad de
Caldas, a US$10.2 M investment**; **Los Andes**, **Icesi** and **UDI** adapting via advisory committees,
implementation plans and curriculum redesign. **Chile** — **National AI Policy since 2021**, with a **law
under discussion**. **Brazil** — described as the **regional reference** for having robust and coherent
normative and institutional frameworks. **Mexico** — 🔴 **no national law or binding regulation**;
**SEP** and **ANUIES** recommendations are explicitly **non-binding**; 🟢 **Tec de Monterrey redesigning
44+ degree programmes to integrate AI by 2026**. 🟢 **Across the three countries analysed, students are
required to declare AI use, with sanctions for fraudulent use and, in some cases, prompts submitted as
documentation.** 🆕 **UNU working paper** — a survey of **200 higher-education institutions across 19
countries**, fielded **August–October 2025** (🔴 `unu.edu` `EGRESS_BLOCKED`; known only from the summary).
🆕 **IADB**, *An Enabling Regulatory Framework for AI in Latin America and the Caribbean* (🔴
`publications.iadb.org` `EGRESS_BLOCKED`). **99%** of LATAM startups using some AI, **85%** integrating
it natively, **edtech among the most disruptive sectors**. **Held:** DEC LATAM survey — **92%** of
students, **79%** of faculty engaging, **30,000+** responses across **29** institutions; **ILIA 2025**.

| Opportunity | Why it is live here, specifically |
|---|---|
| 🟢 **"Declare your AI use" is an infrastructure requirement disguised as an academic-integrity rule** | 🟢 **Three countries now require declaration, with prompts sometimes submitted as documentation.** 🔵 **Somebody has to capture, store, link and audit prompt provenance against a submission — that is the `aiact-50-2` provenance work this KB already has patterns for (`compose/code/aiact-50-2-*`), and it is **required in LATAM now** while it is a 2026-08-02 Article 50 obligation in the EU.** 🟢 **The same component sells into both regions, earlier here** |
| 🟢 **Mexico's non-binding vacuum is a design-partner opening** | 🔴 **No national law, and SEP/ANUIES recommendations lack binding force.** 🟢 **Institutions must therefore set their own defensible standard** — and **Tec de Monterrey's 44-programme redesign** is a named, dated, in-flight programme of exactly that kind |
| 🟢 **Colombia has budget and an institutional anchor** | **US$10.2 M** and a **named faculty** is 🔵 **a concrete counterparty**, not a market-size estimate; the policy's *digital-talent formation* objective is a procurement category |
| ⚠️ **Baseline measurement is contested and that is sellable** | 🔴 **Two instruments now cover LATAM higher education with different denominators (DEC: 29 institutions; UNU: 200 institutions / 19 countries), and this pass could fetch neither.** 🟢 **An institution that wants to know where *it* stands cannot read that off either survey** — a measured institutional baseline is the first deliverable of any engagement here |

## 🟢 Fortieth pass, 2026-10-07 — the regulatory clock is the market fact of this pass, and the EMEA channel got it wrong again

⏱️ **Seventh pass of this date.** 🔵 **Every figure here is secondary and carries its series (`P477`).**
🔴 **Channel state, declared rather than implied: `api.github.com` is `403`; `eur-lex.europa.eu` has been
unreachable since pass 32; `www.marketsandmarkets.com` and `unu.edu` were `EGRESS_BLOCKED` at pass 39; and
this pass adds `planbe.eco` as `EGRESS_BLOCKED`.** 🔴 **So no market figure and no regulatory date below is
first-hand verifiable, and every one is read from search summaries rather than fetched pages.**

### 🔴 `P505` is a market fact, not just a hygiene fact — the high-risk clock moved and the channel keeps un-moving it

🟢 **The date that prices every assessment-AI engagement in EMEA:**

| Obligation | Applies from | Status |
|---|---|---|
| 🟢 **Article 50 transparency** (AI disclosure, synthetic-content marking) | 🟢 **2026-08-02** | 🟢 **In force. Did not move** |
| 🔴 **Annex III stand-alone high-risk** — *education access, student evaluation, exam scoring* | 🟢 **2027-12-02** | 🔴 **Deferred 16 months by the Digital Omnibus** |
| **Annex I embedded** high-risk | **2028-08-02** | Deferred 12 months |

🔵 **Commercially this is the difference between two different sales motions**, and getting it wrong in
either direction costs:

| If a pass believes… | The engagement looks like | 🔴 The cost of the error |
|---|---|---|
| 🔴 **(stale) Annex III bites 2026-08-02** | 🔴 **Emergency conformity work, now** | **Over-sells urgency.** A buyer who discovers the real date stops trusting the adviser |
| 🟢 **(true) Annex III bites 2027-12-02, Article 50 bites now** | 🟢 **Article 50 marking now; conformity programme staged to Dec 2027** | 🟢 **Two engagements instead of one, in the right order** |

🟢 **The deferral's stated rationale is itself the opportunity: harmonised standards were not ready.** 🔵 **A
buyer cannot demonstrate conformity against benchmarks that do not exist — so the work that holds value
through the deferral is the **evidence layer** (calibration, comparability, DIF), which is standards-neutral,
rather than a conformity dossier written against a draft that will change. 🟢 **That is precisely the tier
this KB has been building since pass 33, and `P499` just made its comparability half permissive in Python.**

### 🔵 Regional figures returned this pass — all previously held, restated so silence is not read as a gap

| Region | Series as published | Status in this file |
|---|---|---|
| **North America** | **36%** of global market · **$3.68 B (2026) → $32 B (2030)** · 60% of US K-12 teachers used AI in 2024-25, 32% weekly | 🔴 **The `$32 B` figure is the one `P489` adjudicated *against* at pass 39** — a third series sided against it. 🔵 **Carried here as *returned*, not as *accepted*** |
| **EMEA** | **$2.64 B (2026) → $8.0 B (2030) at 31.9% CAGR** | 🔵 Held. Consistent with the 2026 global range **$8.98 B – $12.3 B** across five series |
| **APAC** | Fastest-growing region by GenAI revenue, **~65% YoY** | 🔵 Held |
| **LATAM** | No new sizing returned this pass — the LATAM channel returns **adoption and governance**, not market size | ⚠️ **Informed gap, eighth consecutive pass: no LATAM-specific AI-in-education market sizing has been found in any channel.** 🔵 **Stated explicitly because an unstated gap reads as coverage** |
| **Global** | **$6.4 B (2025) → $79.6 B (2034) at 31.35%**; and a second series **$7.52 B (2025) → $10.6 B (2026) at 40.9%** | 🔴 **The 40.9% series remains the one `P489` found irreconcilable with the NA trajectory.** 🔵 No new adjudication this pass |

## Opportunities by region — superseded (the live block is at the top of this file)

🔵 **Each subsection names what this pass's evidence supports, and marks what is inference.**

### North America

🟢 **The sellable asset is *human-oversight evidence*, because the legislation names it.** **134 bills
across 31 states** in the 2026 session, and the enacted pattern is consistent: **Oklahoma** and
**Maryland** require human oversight and **bar AI from high-stakes decisions about students**; **Idaho**
provides that **no AI may replace or eliminate a human teacher**; **CA AB 1159** prohibits training on
student data. 🟢 **None of that is satisfiable by a grading agent; all of it is satisfiable by a
grading agent plus an auditable measurement trail.**

🔵 **Concrete motion:** the `compose/patterns.md` chain — generate → calibrate (`py-irt`, MIT) →
check for subgroup gaps (`difair`, MIT) → **link to a reference scale (`EqUMP`, MIT — new this pass)** —
produces exactly the record a human-oversight statute asks a district to keep. 🔴 **Fragmentation is the
delivery risk: 31 states is 31 evidence formats, so the per-state mapping is the billable layer, not the
pipeline.**

### EMEA

🟢 **Two engagements, staged, and the staging is the advice.** **Article 50 is live now (2026-08-02)**:
disclosure and synthetic-content marking, which this KB already holds instruments for
(`compose/code/aiact-50-2-*`). 🟢 **Annex III conformity for education is 2027-12-02** — far enough out to
build properly, close enough to start.

🔴 **The binding constraint is that harmonised standards are not ready** — that is the deferral's own
rationale. 🟢 **So the work that does not get thrown away is standards-neutral evidence**: item
calibration, DIF, and comparability between exam variants. 🔵 **`EqUMP` (MIT) makes the comparability half
an in-product component rather than a GPL side-car — which for a vendor selling into EMEA is the
difference between shipping it and shelling out to it (`P504`).** ⚠️ **Only **10%** of 450+ institutions
have formal AI guidelines while **93%** of educators say regulation is needed: the governance gap is the
demand signal. **Finland, Estonia, Netherlands** lead K-12 integration and are the natural first market.

### APAC

🟢 **The regulatory thesis this KB has carried since pass 33 is now the strongest-evidenced regional
claim it has: high-risk classification of education AI is no longer an EU peculiarity.** Three statutes in
force — **Vietnam's Law on AI (2026-03-01)**, which names education among six high-risk sectors for
*automated assessment and behavioural monitoring* and requires **National AI Database pre-registration,
conformity assessment, human oversight and 72-hour incident reporting**; **South Korea's AI Basic Act
(2026-01-22)**, scoping *"high-impact AI"* in education; **Taiwan's AI Basic Act (2025-12)**.

🟢 **Vietnam's obligations bite *now*, where the EU's bite in December 2027** — so APAC is the region where
conformity work is not deferrable, and the one where a reference implementation earns its keep first.
🔵 **A placement worth noting: `EqUMP`'s four maintainers correspond by maintainer-address channel to the
Republic of Korea.** ⚠️ **Stated as inference from a `naver.com` maintainer address and a Korean-language
authorship pattern, not from any repo-declared affiliation — the repo itself does not resolve (`P501`).
Recorded as a weak placement rather than a confident one.** 🔴 **If it holds, the one permissive
comparability library in Python originates in the region whose education-AI statutes bite earliest, which
is a coherent story but is **not** evidence for either fact.** Named commercial players: Google,
Microsoft, IBM, Pearson, Byju's.

### LATAM

🟢 **The number that defines the opportunity is a gap, and it is unchanged and large.** Digital Education
Council LATAM survey 2026: **92%** of students and **79%** of faculty actively engaging with AI across
**29** institutions and **30,000+** responses — against **88%** of faculty reporting only *minimal to
moderate* engagement, and (pass-33 record) **87%** of institutions using AI in at least one area while
**only 26% have a formal AI strategy**.

🔵 **Adoption is done; governance is not started.** 🟢 **That is an advisory-plus-platform engagement, not a
tooling sale.** The regulatory map is **fragmenting at different speeds** — **Brazil's** AI bill,
**Chile's** framework, **Colombia's CONPES**, **Mexico's** sectoral rules — so a portable evidence layer
beats a jurisdiction-specific dossier. **Chile, Costa Rica, Peru, Uruguay, Panama and the Dominican
Republic** stand out in GenAI adoption and are the credible first markets; **Uruguay** is the first LATAM
signatory of the Council of Europe Framework Convention on AI (pass-33 record).

⚠️ **Two honest gaps.** 🔴 **No LATAM AI-in-education market sizing exists in any channel this KB has
reached, eighth consecutive pass.** ⚠️ **And the DEC faculty denominator differs between this pass's
summary (30,000+ total responses) and the pass-33 record (7,319 faculty) — compatible as total-vs-subset,
but not reconciled first-hand, because the DEC page was not fetched.**

---

## 🟢 Thirty-ninth pass, 2026-10-07 — `P489` is adjudicated: a third series sides against the $32 B figure, and one series fails arithmetic inside a single sentence

⏱️ **Sixth pass of this date.** 🔵 **Every figure here is secondary and carries its series (`P477`).**
🔴 **Channel state, declared rather than implied: `api.github.com` is `403`, `eur-lex.europa.eu` was
unreachable at pass 38, and this pass adds two more — `www.marketsandmarkets.com` and `unu.edu` are both
`EGRESS_BLOCKED` by the session proxy.** 🔴 **So no market figure and no regulatory date below is
first-hand verifiable, and the two sources new to this pass were read from **search summaries, not
fetched pages**.**

### 🔴 `P489` adjudicated — pass 38 said *"at least one of the two is wrong and nothing says which"*. A third series says which

🟢 **Pass 38 found series A's global CAGR (40.9%) irreconcilable with series B's North America
trajectory ($3.68 B in 2026 → $32 B in 2030), and correctly refused to pick.** 🟢 **A third series, new to
this file, is independently published for the same region:**

| Series | Scope | Figures as published | 2026 NA, implied |
|---|---|---|---|
| **B** (pass 36–38) | North America | **$3.68 B** (2026) → **$32.0 B** (2030); **36%** of global | **$3.68 B** |
| 🆕 **F** | North America | **$951 M** (2024) → **$2,303.2 M** (2029), stated CAGR **15.9%** | 🔴 **$1.28 B** |

🔴 **The two disagree by 2.7–2.9× on a year two years away, and by ~14× on 2030:**

| Comparison | B | F | B ÷ F |
|---|---|---|---|
| NA **2026** | **$3.68 B** | **$1.28 B** (at F's stated 15.9%) | 🔴 **2.88×** |
| NA **2026**, F read at its own implied rate | **$3.68 B** | **$1.35 B** (19.35%, see below) | 🔴 **2.72×** |
| NA **~2030** | **$32.0 B** | **$2.30 B** | 🔴 **13.9×** |
| NA **CAGR** | 🔴 **71.7%** (B's own figures, pass 38) | **15.9%** (published) | 🔴 **55.8 points apart** |

🟢 **Adjudication, and it is as far as the evidence goes:** 🔴 **series B's North America trajectory is the
outlier of the three, and `$32 B by 2030` should not be quoted at all.** 🔵 **Two independent series —
A's global ceiling and F's regional level — are each inconsistent with it, in the same direction. B's
2026 *share* (36%) remains quotable; **its levels and its 2030 do not.**

> 🔵 **Upgrade to `P489`, not a new finding.** The test pass 38 prescribed (project both and check the
> implied *share*) flagged the pair correctly but could not break the tie. 🟢 **What breaks a tie is a
> **third** series on the **same region**, which costs one extra search.** 🔴 **Two series disagreeing is a
> warning; three series with two agreeing is a verdict.**

### 🔴 `P495` — series F fails arithmetic **inside a single published sentence**, and this class is new to this file

🔵 **Every series defect passes 36–38 found was *between* series. This one is *within* one**, and needs no
second source to detect — only division:

| Published in one sentence | Value |
|---|---|
| North America, **2024** | **$951 M** |
| North America, **2029** | **$2,303.2 M** |
| Stated CAGR | **15.9%** |

🔴 **The three cannot all be true.** Measured:

| Check | Result |
|---|---|
| CAGR implied by the two endpoints over **5** years (2024→2029) | 🔴 **19.35%**, not 15.9% |
| $951 M grown at the **stated 15.9%** for 5 years | 🔴 **$1,988.8 M**, not $2,303.2 M |
| Years of growth that **15.9%** needs to get 951 → 2,303.2 | 🔴 **5.995 — exactly 6** |

🟢 **The defect is almost certainly an off-by-one on a year label**: either the base is **2023**, or the
endpoint is **2030**. 🔴 **Nothing in the summary says which, and the page itself is `EGRESS_BLOCKED`, so
this pass cannot resolve it.**

> **`P495`.** 🔵 **Check a series against *itself* before comparing it to anything.** Three published
> numbers — base, endpoint, CAGR — are **one equation with no free variables**, so any market figure
> quoting all three is **arithmetically falsifiable at zero cost**. 🔴 **For a deliverable: never quote a
> level and a CAGR from the same source without dividing them first.** 🟢 **And when the check fails,
> quote the **endpoints** and drop the CAGR — the endpoints are what the research was for; the CAGR is a
> derived number someone typed.**

### 🔴 The 2025 base year — two series disagree by 17.5% about a year that has already happened

🆕 **Series E**, new this pass: global **$6.4 B in 2025** → **$79.6 B by 2034**, growth **31.35%** stated
for **2026–2034**.

| Series | Global **2025** | Global **2026** |
|---|---|---|
| **A** (this file's working series) | **$7.52 B** | **$10.6 B** |
| 🆕 **E** | 🔴 **$6.4 B** | 🔴 **$8.98 B** *(derived: $79.6 B discounted at E's own 31.35% over 8 years)* |
| **B** (implied) | — | **$10.22 B** |
| **C** | — | **$11.4 B** · **$12.3 B** |

🔴 **A and E differ by 17.5% on 2025 — an elapsed year.** 🔵 **This is a different and worse signal than a
forecast disagreement.** Two forecasters may legitimately differ about 2030; **2025 is not a forecast**,
and a 17.5% spread on it means at least one series is not measuring a market but **back-casting it from a
model**. 🔴 **E is also internally loose**: $6.4 B (2025) → $79.6 B (2034) implies **32.3%**, not the
stated 31.35%.

🔴 **The full 2026 global range now on this file's shelves is $8.98 B – $12.3 B — a 37% spread across five
published series.** 🟢 **This file continues to use **A** end to end (`$10.6 B`, CAGR 40.9%), unchanged,
and now records that the choice is a **convention**, not a finding.**

### 🟢 Adoption and regulation measured this pass, by region

🔵 **Scope labels matter here and this pass enforces them.** 🔴 **Several regional figures returned by the
mandated searches are **cross-industry enterprise** numbers, not education-sector numbers, and are marked
as such** — mixing the two is the same class of error as mixing series.

| Region | Adoption | Regulatory state |
|---|---|---|
| **North America** | 🟢 **36%** of the global market (series B, share only). 🟢 **60%** of US K-12 teachers used AI tools in 2024-25, **32% weekly** (pass 38, unchanged). 🆕 **$169 M** committed to responsible AI in higher education in **Q1 2026**; 🆕 **OpenAI launched a country-level education programme with eight national partners, Q1 2026** | 🟡 **134 bills across 31 states** in 2026; **California AB 1159** bars training on student data; **Oklahoma** and **Maryland** require human oversight. 🆕 **Colorado** and **Texas** add piecemeal requirements. 🔴 **One source characterises the sector as a *"relative regulatory vacuum — no FDA equivalent for edtech"*, with adoption decided school by school** — 🔵 consistent with 134 bills and **no federal statute in force** |
| **EMEA** | 🟡 **Pilot-and-pre-compliance.** 🔴 **New figures this pass are cross-industry, not education**: **94%** of organisations likely to invest in AI training in 2026; **38%** have not begun piloting; **60%** report siloed data. 🆕 **UK AI Adoption Summit committed £200 M+**, delivered via government-as-funder + Big Tech (Cisco, IBM, BT, Rolls-Royce) + unions + **Skills England** setting curriculum | 🔴 **EU AI Act (Reg. (EU) 2024/1689)**: education **admissions, assessment, scoring, proctoring and path-steering personalisation** are **high-risk**. 🔴 **Date conflict, unresolved:** a source new this pass states the Act *"takes full effect in August 2026"*, which **contradicts** this file's pass-38 record that the **July 2026 AI Omnibus deferred standalone high-risk to 2027-12-02**. 🔴 **`eur-lex.europa.eu` is unreachable, so neither date is first-hand verified — do not quote either without the other.** 🟢 **Art. 4 AI-literacy has applied since 2025-02-02** and is not in dispute. 🆕 **Council of Europe held a 2nd working conference on the regulatory dimensions of AI in education in October** |
| **APAC** | 🟢 **Deepest mandate anywhere, unchanged:** China — AI **compulsory from age 6**; India — AI + computational thinking compulsory **from Class 3, 2026-27** (IndiaAI Mission); Singapore leads implementation, then Australia, Korea, Taiwan. 🔴 **New figures this pass are cross-industry**: **48%** of APAC governance leaders rank AI a top 2026 priority; **57%** of Asian organisations have AI in ≥1 area. 🆕 **Corporate-learning players moving in**: LearnUpon (new Sydney HQ, *Create+* AI authoring), **TCS–Pearson** multi-year AI learning alliance | 🔴 **Three divergent models, unchanged.** Binding risk-based: **Korea's Basic AI Act** (provisions from H2 2026), Vietnam. Targeted: **China's GenAI Measures**, enforced since Aug 2023. Voluntary: **Japan's AI Promotion Act** (soft law, March 2026), Singapore, Australia. 🔵 **Singapore's live consultations on AI assurance are in *financial services*, not education** — 🔴 do not cite them as education regulation |
| **LATAM** | 🔴 **The gap is governance, not usage**, and this pass strengthens the evidence. **>50%** of teachers in Chile and Brazil already use AI tools; 🔴 **<10% of institutions have formal guidelines**. 🆕 **A UNU/UNESCO working paper surveys 200 higher-education institutions across 19 countries (fieldwork August–October 2025)** on five dimensions — teaching and learning, research, community engagement, administration, **governance**. 🔴 **`unu.edu` is `EGRESS_BLOCKED`: cited from a search summary, not fetched — the paper's own percentages are NOT in this file and should not be invented.** 🟢 Live at scale, unchanged: **Lottus Education (Mexico)** — LucIA, 90,000 students / 45 campuses, feedback from ~2 months to **15 minutes**; **PUC-PR (Brazil)** — AvalIA, **270,000+** comments auto-classified. 🆕 **Ednova (Chile)** named among regional edtech | 🟡 **Brazil PL 2.338/2023** — horizontal, risk-based, Senate-approved 2024-12-10, **now in the Chamber of Deputies, text can still change**. Mexico's bill adds a **"digital rights"** chapter. 🟢 **UNESCO AI-in-Education Observatory for LAC launched April 2026**. 🆕 **IADB has published a regional framework paper** (*An Enabling Regulatory Framework for AI in LAC*) — 🔵 the first regional-bank-level instrument this file has recorded |

### 🟢 Figures this file will carry forward, and the ones it will not

| Use | Figure | Series |
|---|---|---|
| 🟢 **Global 2026 market** | **$10.6 B** | **A** — 🔵 a **convention**, chosen end to end; the published range is $8.98–12.3 B |
| 🟢 **Regional share, 2026 only** | NA **36%** | **B** — 🔵 share only |
| 🔴 **NA 2030 = $32 B** | 🔴 **Do not quote. Adjudicated against** by series A and F | **B** |
| 🔴 **NA $951 M → $2,303.2 M at 15.9%** | 🔴 **Quote the endpoints, drop the CAGR** (`P495`) | **F** |
| 🔴 **Global 2025 = $6.4 B** | 🔴 **Do not quote beside A.** 17.5% below A's elapsed-year figure | **E** |
| 🟢 **AI-tutors sub-segment** | $3.55 B (2025) → $6.45 B (2030) | **D** — 🔵 label it a sub-segment |
| 🟢 **Student adoption** | **66%** (2024) → **92%** (2025); **86%** of HE students using AI as primary research partner at the start of 2026 | 🔵 usage, not market — safe to quote beside any series |

## Opportunities by region — superseded (the live block is at the top of this file)

🔵 **The opportunity this pass creates is the same instrument everywhere — the **comparability and
fairness** evidence layer (`P496`, `compose/patterns.md`) — and what differs by region is **who is
obliged to produce it, and when**. 🔴 **The tooling itself is jurisdiction-neutral (`P474`): no region
produced a region-specific permissive implementation, and all four regional searches are declared empty on
that point in `repos/foundations.md`.**

### North America

🟢 **The buyer is an exam board, a state testing programme or a university assessment office, and the
driver is **professional standards and litigation exposure**, not a statute.** 🔴 **There is no federal AI
statute in force**, and one source calls the sector a *"regulatory vacuum"* — 🔵 **but DIF analysis has
been standard practice in US large-scale testing for decades**, so the requirement already exists in
procurement language and in the AERA/APA/NCME *Standards*. 🟢 **That makes this the easiest region to sell
into: nobody has to be convinced the evidence is needed, only that it can be produced permissively and
on-premise.** 🔵 **The constraint to design for is state data law** — **California AB 1159** bars training
on student data, which is exactly why `difair_studio.html`'s no-network, in-browser path matters. 🔴 **The
measured gap: 134 bills across 31 states means 31 different compliance targets, and nothing in this pass
found a vendor-neutral mapping between them.**

### EMEA

🔴 **The strongest regulatory driver anywhere, and the one with a disputed clock.** Education assessment
and scoring are **Annex III high-risk** under Reg. (EU) 2024/1689, and the obligation that bites is
**accuracy, robustness and documented performance (Annex IV)** plus **bias examination** — 🟢 **which are
psychometric properties, and `P496` produces them.** 🔴 **The date is in dispute** (August 2026 full
effect vs the Omnibus deferral to 2027-12-02) and `eur-lex` is unreachable, 🟢 **so the commercially safe
framing is the earlier date**: build the evidence pack on the assumption it is needed sooner.
🟢 **Art. 4 AI-literacy already applies to every school.** 🔵 **The live channel is institutional:** the
Council of Europe convened a second working conference on AI-in-education regulation in October, and the
UK is funding **AI skills** through Skills England with £200 M+ — 🔴 **note that the UK money is skills
delivery, not assessment integrity, so it is adjacent, not the same budget.**

### APAC

🟢 **The largest assessment volume on earth and the clearest mandate** — China from age 6, India from
Class 3 in 2026-27 — 🟢 **and volume is precisely the prerequisite `P496` cannot substitute for** (~500
responses per item). 🔵 **So APAC is the region where this chain is *most* buildable and *least*
required**: the three regulatory models diverge (Korea binding, China targeted, Japan/Singapore/Australia
voluntary), and none of them yet names item-level fairness evidence as an obligation. 🔴 **Declared gap,
and it is this pass's sharpest regional asymmetry: the region with compulsory national AI curricula
produced **zero** permissive open-source measurement tooling that any of this pass's searches could
find.** 🟢 **The opening is therefore a ministry-scale engagement — national curriculum, national item
bank, equating across annual cohorts — rather than a compliance sale.**

### LATAM

🔴 **Usage is ahead of governance and the gap is measured, not inferred**: >50% of teachers in Chile and
Brazil use AI tools, <10% of institutions have formal guidelines, and the new UNU/UNESCO survey covers
**200 institutions in 19 countries** with **governance** as one of its five dimensions. 🟢 **That shape
favours an instrument over a product**: the binding constraint is not tooling but the absence of an
institutional policy to point the tooling at. 🔵 **The regional scaffolding arrived this year** — UNESCO's
LAC observatory (April 2026) and now an **IADB** regulatory-framework paper — 🟢 **which is what a
Globant engagement can anchor to: implement the observatory's categories as an actual audit, with
`P496`'s outputs as the evidence.** 🔴 **Brazil's PL 2.338/2023 is still in the Chamber and its text can
change, so build to the obligation, not to the draft article numbers.** 🔵 **Two references already exist
at scale and should be cited in any LATAM pitch — Lottus (Mexico) and PUC-PR (Brazil).** 🔴 **And the
honest caveat: `unu.edu` is proxy-blocked from this session, so the survey's actual percentages are not in
this KB and must be obtained before any deck quotes them.**

---

## 🟢 Thirty-eighth pass, 2026-10-07 — base-year agreement hid a growth assumption that puts North America at 77% of the world

⏱️ **Fifth pass of this date.** 🔵 **Every figure here is secondary and carries its series (`P477`).
`api.github.com` is gated and `eur-lex.europa.eu` is unreachable from this session (`P479`), so no
market figure and no regulatory date below is first-hand verifiable.**

### 🔴 `P489` — two series agreed on 2026 to within 3.6% and implied an impossible 2030

🟢 **The figures, as published, each with its series attached:**

| Series | 2026 | Growth claim | Note |
|---|---|---|---|
| **A** — "AI in education", global | **$10.6 B** | 🔴 **CAGR 40.9%** (from $7.52 B in 2025) | the series this file has been using |
| **B** — regional split, global implied | **$10.22 B** *(derived)* | 🔴 **NA to $32 B by 2030** | **NA = $3.68 B = 36% of global** |
| **C** — alternative globals | **$11.4 B** · **$12.3 B** | — | two further published 2026 globals |
| **D** — "AI tutors" sub-segment | **$3.55 B** (2025) | → **$6.45 B by 2030** | 🔵 a **sub-segment**, not comparable to A–C |

🟢 **A and B agree on the base year, which is why they looked like one series.** B's $3.68 B at a stated
36% share implies a global of **$10.22 B**, only **3.6%** below A's **$10.6 B**.

🔴 **Projected forward they are irreconcilable:**

| Projection | Value | Consequence |
|---|---|---|
| A's global 2026 at A's own 40.9% CAGR → **2030** | **$41.8 B** | — |
| B's **North America 2030** | **$32.0 B** | 🔴 **= 76.6% of A's 2030 global**, up from **36%** in 2026 |
| B's implied **NA CAGR** 2026→2030 | 🔴 **71.7%** | vs A's global **40.9%** |
| Global CAGR required for NA to **hold** 36% | 🔴 **70.2%** | 🔴 **A's own CAGR would have to be wrong by 29 points** |

🔵 **North America does not go from a third of this market to three quarters of it in four years while
APAC has compulsory AI from age six and India adds it from Class 3.** 🔴 **So at least one of the two
published numbers is wrong, and nothing in either source says which.**

> **`P489`.** **Base-year agreement is not series identity.** Two series that match on the current year
> to within a few percent can encode growth assumptions that differ by **30 CAGR points**, and the
> disagreement is invisible until both are projected. 🔵 **The test is not to compare levels — it is to
> project both and check the implied *share*.** A share trajectory that is not credible condemns the
> pair, and a deck quoting *"$3.68 B today, $32 B by 2030"* beside *"40.9% CAGR"* is quoting a
> contradiction.

🔵 **This is the third consecutive pass to find a series defect, and the class is now stable.** Pass 36
found the file mixing a region from one series with a global from another; pass 37 found a third series
agreeing on 2026 to within 2% while implying a 2030 **29% higher**; this pass finds base-year agreement
masking a **71.7% vs 40.9%** growth split. 🟢 **The lesson for a deliverable: quote one series end to
end, name it, and never let a regional figure and a global CAGR come from different reports.**

### 🟢 Figures this file will carry forward, and the one it will not

| Use | Figure | Series |
|---|---|---|
| 🟢 **Global 2026 market** | **$10.6 B** | **A** — stated with its own CAGR only |
| 🟢 **Regional shares, 2026 only** | NA **36%** | **B** — 🔵 share, not level; the level divides across series |
| 🔴 **NA 2030 = $32 B** | 🔴 **Do not quote alongside series A** | **B** — quotable **only** with B's own global, which is not published |
| 🟢 **AI-tutors sub-segment** | $3.55 B (2025) → $6.45 B (2030) | **D** — 🔵 label it a sub-segment or it reads as a contradiction of A |

### 🟢 Adoption and regulation measured this pass, by region

| Region | Adoption | Regulatory state |
|---|---|---|
| **North America** | 🟢 **60%** of US K-12 teachers used AI tools in 2024-25; **32% weekly**. **36%** of the global market | 🟡 **134 bills across 31 states** in 2026. **California AB 1159** bars training models on student data; **Oklahoma** and **Maryland** require human oversight and bar AI from high-stakes decisions. Federal **K-12 AI Literacy and Readiness Act of 2026** advanced out of committee |
| **EMEA** | 🟡 **Pilot-and-pre-compliance**, not full enforcement | 🔴 **EU AI Act (Reg. (EU) 2024/1689)**: education **admissions, assessment, scoring, proctoring, AI-detection in assessment and path-steering personalisation** are **high-risk**. 🟡 **July 2026 AI Omnibus deferred standalone high-risk to 2027-12-02.** 🔴 **Art. 4 AI-literacy has applied since 2025-02-02 to every organisation using AI — every school, now** |
| **APAC** | 🟢 **Deepest mandate anywhere.** China: AI **compulsory from age 6**. India: AI + computational thinking compulsory **from Class 3, 2026-27**, via the IndiaAI Mission. Singapore leads implementation, then Australia, Korea, Taiwan | 🔴 **Three divergent models.** Binding risk-based: **Korea's Basic AI Act (provisions from H2 2026)**, Vietnam. Targeted: **China's GenAI Measures, operationally enforced since Aug 2023**. Voluntary: **Japan's AI Promotion Act (soft law, March 2026)**, Singapore, Australia |
| **LATAM** | 🔴 **The gap is governance, not usage.** **>50%** of teachers in Chile and Brazil already use AI tools; 🔴 **<10% of institutions have formal guidelines**. Live at scale: **Lottus Education (Mexico)** — LucIA, 90,000 students across 45 campuses, feedback cycle from ~2 months to **15 minutes**; **PUC-PR (Brazil)** — AvalIA, **270,000+** student comments auto-classified | 🟡 **Brazil PL 2.338/2023** — horizontal, risk-based, Senate-approved 2024-12-10, **now in the Chamber of Deputies, text can still change**. Mexico's bill adds a **"digital rights"** chapter. 🟢 **UNESCO launched an AI-in-Education Observatory for LAC in April 2026** |

## Opportunities by region — superseded (the live block is at the top of this file)

🔵 **Framing this pass: the new asset is a *measurement* layer (`repos/foundations.md`), and it is
jurisdiction-neutral by construction (`P474`, `T3`). So it is placed below by *which regulator makes it
mandatory*, not by where it was written.**

### North America

🟢 **The buy is defensibility against a human-oversight rule, and the rule is already in force.**
Oklahoma and Maryland bar AI from high-stakes decisions about students. 🔵 **The compliant architecture
is therefore not "a human approves the AI grade" — it is *the AI never makes the decision*: it produces
a calibrated measurement and a human holds the determination.** 🟢 **`py-irt` (MIT) + the MIT QTI chain
builds exactly that**, and `P51` (pass 37) already covers the assistive-grading shape.

🟢 **Second, specific opening: California AB 1159 bars training on student data.** 🔵 **An IRT
calibration is fitted on *response patterns*, not on student text, and it never leaves the
institution** — so the measurement layer is a feature that is *architecturally* compatible with AB 1159
rather than a policy promise about it.

🔴 **The federal AI-literacy funding line (K-12 AI Literacy and Readiness Act) is a curriculum
opportunity, not a platform one** — and this KB's curriculum tier is where `CC BY-NC` traps live
(`P473`). 🟡 **Qualify the licence before quoting courseware.**

### EMEA

🔴 **The deferral to 2027-12-02 is the single most mis-read fact in this market.** 🔵 **Two obligations,
two clocks**: high-risk conformity moved to **December 2027**, but **Art. 4 AI-literacy has been in
force since February 2025** for every organisation that uses AI. 🟢 **So there is a live obligation to
sell against today and a 14-month window to build conformity into systems rather than bolt it on.**

🟢 **The high-value engagement is the conformity pack for an assessment system**, and `P49` (pass 37)
already specifies it. 🆕 **What this pass adds is the evidence that pack was missing**: Annex IV wants
accuracy and robustness documentation, and *"the model is a good tutor"* is not that. 🔵 **An item
parameter table with standard errors is.**

🟢 **Licence fit is unusually good here.** The calibration chain is **MIT + MIT + MIT + BSD-3** with no
copyleft, so it ships **inside** a product sold to European institutions — unlike the LMS and proctoring
tiers, which are GPL/AGPL and have to be side-cars (`T4`, passes 33–37).

### APAC

🟢 **The only region where the obligations are binding *now*, and the region with the deepest mandate.**
China's compulsory-from-age-6 and India's Class-3 rollout create assessment volume at national scale;
Korea's Basic AI Act brings tiered compliance from **H2 2026**.

🟢 **Two concrete openings.** (1) **Jurisdiction-gated, on-premise delivery** — `P50` (pass 37) covers
the multi-agent classroom shape, and `OpenMAIC` (MIT, Tsinghua) runs fully local via Lemonade + FunASR.
🆕 (2) **Adaptive testing at national scale**: `catsim` (BSD-3) plus a calibrated bank is the
architecture a ministry-scale testing programme needs, and 🟢 **the regional research shelf is already
here** — `bigdata-ustc` (USTC, Hefei): `EduCDM`, `EduKTM`, `EduCAT`, `EduNLP`, and 🆕 `CAT4AI` (MIT,
1,062 B, verified this pass).

⚠️ **The honest caveat on that shelf: it is published but mostly old** (`P260` — `EduCAT` has one
release, 2024-01-24). 🔵 **Quote it as a research foundation and a credibility signal with a named
institution, not as maintained infrastructure.**

### LATAM

🟢 **The inversion this KB has recorded for several passes holds and sharpens: adoption is high,
governance is absent.** >50% of teachers in Chile and Brazil use AI; **<10%** of institutions have
guidelines. 🔵 **So the sell is not "adopt AI" — it is "you have already adopted it; here is the
governance layer", and that is a services engagement by nature.**

🟢 **Two placed, verifiable reference points to quote** — **Lottus Education** (Mexico, 90,000 students,
45 campuses, 15 minutes) and **PUC-PR** (Brazil, 270,000+ comments). 🔵 **Both are *text-understanding at
institution scale*, which is `P52` (pass 37), and both are peer references rather than vendor claims.**

🟡 **Brazil PL 2.338/2023 is pending in the Chamber and its text can still change**, so the defensible
posture is architectural, not compliance-mapped: 🟢 **a calibrated, on-premise measurement layer is
robust to whichever version passes**, because accuracy evidence is required under every risk-based draft
reviewed.

🔴 **And the gap stated outright, since silence looks like coverage: this pass found no LATAM-origin
open-source education artefact.** 🔴 **`catsim`'s author publishes from a `.com.br` domain and `P474`
forbids placing the artefact on that basis** — a CAT engine has no jurisdiction in its domain model. 🔵
**The Brazilian-Portuguese Socratic-tutor benchmark pass 37 recorded as an unresolved lead
(`slm-socratic-tutor-ptbr`) remains unresolved: no owner slug recoverable from any channel reachable
here.** 🟢 **UNESCO's LAC Observatory (April 2026) is the most likely future source and is not fetchable
from this session.**

## 🟢 Thirty-seventh pass, 2026-10-07 — the five-way split mapped onto this KB's four-region vocabulary, and a third series that agrees on 2026 and diverges 29% by 2030

⏱️ **Measured 2026-10-07 from secondary sources** (market-research houses, state legislative trackers,
Digital Education Council, UNESCO, IDB/IADB, OECD, EDUCAUSE, law-firm regulatory trackers).
🔴 **Every market and regulatory domain cited here was re-tested for reachability and every one is
blocked from this environment: `eur-lex.europa.eu`, `arxiv.org`, `aclanthology.org`, `huggingface.co`,
`multistate.us`, `excelined.org` → `000` (CONNECT tunnel refused).** ⚠️ **Nothing in this file is
first-hand.** Figures are corroborated only by agreement across independent search results — a weaker
channel than payload, and any deliverable must say so.

### 🟢 The find: pass 36's five-way split, reconciled to the closed region vocabulary — and it still sums

🔴 **Pass 36 obtained a coherent five-region split, but it was published as `North America / APAC /
Europe / LATAM / Middle East & Africa` — and this KB's `region` field is a closed five-value
vocabulary in which `Europe` and `Middle East & Africa` do not exist.** 🔵 **So the best market series
this file has ever held was unusable by the very filter the frontmatter exists to drive.** Mapped
(`EMEA = Europe + MEA`):

| Region (🟢 closed vocabulary) | 2026 | Share | 2030 (published CAGRs) |
|---|---|---|---|
| **North America** | **$3.68B** | **35.4%** | $10.87B |
| 🆕 **EMEA** = Europe $2.64B + MEA $0.56B | 🆕 **$3.20B** | 🆕 **30.8%** | 🆕 **$9.81B** |
| **APAC** | **$2.85B** | **27.4%** | $9.55B — 🟢 **fastest, 35.3% CAGR** |
| **LATAM** | **$0.67B** | **6.4%** | $2.13B |
| 🟢 **Sum** | 🟢 **$10.40B** | **100.0%** | 🟢 **$32.36B** |

🟢 **The four-region sum is still exactly the published global 2026 of `$10.4B`, and the 2030 sum lands
0.3% from the published global 2030 of `$32.27B`.** 🔵 **The reconciliation costs nothing in accuracy
and makes the series filterable — EMEA is the **second-largest** region once Europe and MEA are added,
ahead of APAC, which the five-way presentation obscured.**

### 🔴 A third series entered this pass. It agrees on 2026 to within 2% and implies a 2030 that is 29% higher

| Series | 2025 | 2026 | CAGR | 2030 implied |
|---|---|---|---|---|
| **A** — the shelf's reconciled series | — | **$10.40B** | **32.8%** | **$32.36B** |
| 🆕 **B** — AI-in-education, 2026 report | **$7.52B** | **$10.6B** | 🔴 **40.9%** | 🔴 **$41.78B** |
| Divergence | | 🟢 **1.9%** | 🔴 **8.1 pts** | 🔴 **+29.1%** |

🟢 **Series B is internally consistent** — `7.52 × 1.409 = 10.60`. 🔴 **So two independent houses agree
almost exactly on the 2026 base and disagree by nearly a third on where it lands in four years.**

> 🔵 **The operational rule, and it is the useful output of this table: quote the 2026 base, never the
> CAGR.** The base year is corroborated across series; the growth rate is the single least stable
> number in this file, and it is the one that compounds into every deck's headline. 🔴 **Pass 36's
> finding was that this file had been mixing two series; the correction is not "pick the right one" —
> it is to stop projecting at all and cite a dated base.**

### Market-mechanics figures worth carrying (all secondary)

| Claim | Figure | Why it matters to a build |
|---|---|---|
| AI tutoring effect size | 🟢 **0.3–0.5 SD** learning gains, comparable to human 1:1 on specific skills | 🔵 **The only outcome number in this file with a defensible unit.** It is *per skill*, not per course — scope pilots to a skill |
| Assessment generation | **84.7%** accuracy correlation with expert consensus; **>99%** reduction in creation time | 🔴 **The time saving is the sellable number; the 84.7% is the reason a human stays in the loop** |
| Grading posture | **AI-assisted grading outperforms fully autonomous grading** as a deployment model (OECD; EDUCAUSE 2026) | 🟢 **Converges with regulation** — NA states and the EU both bar autonomous high-stakes decisions. Assistive is both better *and* legal |
| Fastest deployers | Tutoring and test-prep businesses, hybrid model: **AI drills between sessions, humans hold relationship, motivation and assessment** | 🔵 **The division of labour a client will recognise** |

---

## Opportunities by region — superseded (the live block is at the top of this file)

### North America

🔵 **The regulatory text has become a product specification, and it is unusually explicit about what
software may not do.**

- **134 AI-in-education bills across 31 states** in the 2026 session; **35+ states** carry official
  department-of-education AI guidance as of June 2026.
- **NYC Public Schools, March 2026 — "Traffic Light Framework"** (Green / Yellow / Red). 🔴 **Red —
  never permitted: grading, discipline, promotion and graduation decisions, behavioural surveillance.**
- **Oklahoma and Maryland** require human oversight and **bar AI from high-stakes decisions about
  students**. **Maryland's AI Ready Schools Act** gives all **24 districts 120 days** from state
  guidance to adopt aligned policies.
- **California AB 1159** prohibits using student data to train AI models; **Idaho SB 1227** mandates
  data-privacy protections for AI tools in schools.
- **Georgia and Mississippi** fold AI into computer-science graduation credit.

🟢 **Opportunity — the compliance-shaped assistive product.** $3.68B, 35.4% of the market, and a
written list of prohibited functions. 🔵 **Build the assistive-grading and early-warning layer that is
*architecturally* incapable of the Red-list actions** — recommendation surfaces with a mandatory human
commit step, decision provenance, and an auditable record that no promotion/discipline outcome was
machine-emitted. **`AB 1159` additionally forecloses the "improve the model on client data" clause**,
so an on-premise or no-train posture is a *requirement*, not a differentiator. 🟢 **`OSSS`
(Apache-2.0) is the natural substrate** — districts are its top-level tenant and board governance,
accounting and transportation are already modelled.

⚠️ **Per-district policy divergence is the delivery risk**: 24 districts in one state × 120-day clocks
means a *policy-parameterised* product, not one deployment.

### EMEA

🔴 **The EU AI Act's high-risk obligations for education became fully applicable on 2 August 2026 —
roughly two months before this measurement — and the sector is, by its own assessments, not ready.**

- **Regulation 2024/1689**, in force 1 Aug 2024, **full applicability 2 Aug 2026**. ⚠️ **Secondary
  sourced; `eur-lex.europa.eu` is `000` here — verify against the Official Journal before any
  deliverable.**
- 🔴 **Education is explicitly high-risk**: admission decisions, evaluation of learning outcomes, exam
  scoring. Obligations: **risk management, data governance, human oversight, transparency, conformity
  assessment before deployment**.
- Published evaluations find a **documented gap between regulatory expectation and institutional
  readiness**, and recommend ministerial operational guidance, inter-institutional capacity building,
  and AI-governance indicators inside national quality-assurance systems.
- Phased implementation continues through 2026–2027; most institutions remain in **pilot and
  pre-compliance** posture.

🟢 **Opportunity — and on the reconciled series EMEA is the second-largest region at $3.20B (30.8%),
not the third.** 🔵 **The sellable asset is the conformity-assessment artefact, not the model.** A
high-risk education system needs a technical file, a data-governance record, a human-oversight design
and transparency documentation — **deliverables, repeatable across institutions, that nobody's LLM
produces as a by-product**. 🟢 **`OpenOLAT` (Apache-2.0, Zurich) is the one LMS that can carry an
in-product compliance layer without a copyleft conversation**, and the KB already holds an
`aiact-50-2-*` instrument family for the marking/provenance side.

🔴 **The readiness gap is the engagement.** Obligations are live and institutions are in
pre-compliance: that is a remediation market with a statutory deadline already behind it.

### APAC

🔵 **The fastest-growing region, the only one that produced a new placed repository this pass, and the
most fragmented regulatory map of the four.**

- 🔴 **South Korea's AI Basic Act took effect January 2026** and names **education** as a
  **high-impact** domain — risk management and disclosure obligations attach.
- **China** has the most developed binding AI regulation in APAC. **Japan** runs a deliberately
  light-touch, voluntary governance model. **India** still has **no dedicated AI statute**, relying on
  privacy, cybersecurity and consumer law.
- **Japan and South Korea** impose education-specific data-protection duties — **student-data
  encryption with penalties for non-compliance**.
- Market **$2.85B (27.4%), 35.3% CAGR — the fastest of the four**.

🟢 **Opportunity — the on-premise multi-agent classroom, and the asset for it landed this pass.**
🆕 **`THU-MAIC/OpenMAIC` (MIT, Tsinghua MAIC)** is a full multi-agent classroom — AI teachers *and* AI
classmates, whiteboard, live discussion, one-click slides/quizzes/simulations — with **Lemonade local
inference and FunASR local ASR**, so 🟢 **the entire classroom runs inside the institution**. 🔵 **That
is precisely the shape Korea's high-impact disclosure duties and Japan/Korea's encryption mandates
reward**, and MIT means it ships in-product.

⚠️ **Four jurisdictions, four regimes: this is a policy-node product.** The KB's existing pattern of
LangGraph policy nodes per jurisdiction applies directly — one graph, per-market gates.

### LATAM

🔴 **The region's defining number is not adoption. It is the distance between adoption and depth.**

- 🟢 **79% of LATAM faculty report using AI in teaching** (Digital Education Council, 2026) — **18
  points above the 2025 global figure**.
- 🔴 **88% report only "minimal" to "moderate" engagement.** In Brazil and Chile **>50% of teachers
  already use these tools**, yet 🔴 **fewer than 10% of institutions in the region have formal
  guidelines**.
- **Brazil's PL 2.338/2023** remains the region's bellwether horizontal, risk-based statute —
  transparency plus a supervisory architecture, with training-data disclosure still contested.
- **UNESCO launched the Observatory on AI in Education for Latin America and the Caribbean on 14 April
  2026**; **Google.org committed $4.6M** targeting **1.25M students by 2028 across nine countries**
  (Argentina, Brazil, Chile, Colombia, Dominican Republic, El Salvador, Mexico, Peru, Uruguay); the
  **IDB** has published lessons from **193 solutions** across the region.
- 🟢 **Named production deployments, which is rare in this file:** **Lottus Education (Mexico)** —
  `LucIA` processes feedback from **90,000 students across 45 campuses in 15 minutes**, previously
  nearly two months; **PUC-PR (Brazil)** — `AvalIA` classifies **270,000+ student comments** across
  didactic / technical / behavioural categories; **Universidad Panamericana (Mexico)** — `SyllabUP`,
  an **agent architecture** validating curricular programmes and gathering accreditation evidence.
- Market **$0.67B (6.4%), 33.5% CAGR** — the smallest of the four.

🟢 **Opportunity — governance-as-a-product, and offline-first delivery.** 🔵 **79% usage against <10%
institutional guidelines is not a gap in tooling, it is a gap in policy infrastructure** — and the
three named deployments show what sells: **institution-scale text understanding** (feedback,
comments, syllabus validation, accreditation evidence), not student-facing tutoring. 🟢 **`Kolibri`
(MIT) is the only platform on these shelves whose architecture already assumes intermittent
connectivity**, which is the default condition in public education across the region, and it is
permissive enough to ship the AI layer inside.

⚠️ **This pass placed no new LATAM repository.** It searched for one; the single candidate — a
Brazilian-Portuguese Socratic-tutor benchmark over 8 open SLMs ≤3.8B, offline — **appears only in
secondary prose with no recoverable owner slug**. 🔴 **Recorded as an informed gap.** The region's
verified asset on these shelves remains pass 36's **`eduagarcia/lm-evaluation-harness-pt`** (MIT,
CEIA / Federal University of Goiás) — 🔵 **a Portuguese evaluation harness, which is the right
foundation for exactly the governance work the guidelines gap implies.**

## 🟢 Thirty-sixth pass, 2026-10-07 — the five-region denominator closes, and it shows this file has been mixing two market series

⏱️ **Measured 2026-10-07 from secondary sources** (market-research houses, state legislative trackers,
law-firm regulatory trackers, EdTech Hub, Ipsos, ECLAC/CEPAL, Thomson Reuters Institute).
🔴 **Every market and regulatory domain cited here was tested for reachability and every one is blocked:**
`multistate.us`, `excelined.org`, `azumo.com`, `education.ohio.gov`, `finance.yahoo.com`,
`eur-lex.europa.eu`, `arxiv.org`, `aclanthology.org` → **000**. ⚠️ **Nothing in this section is
first-hand. Figures are corroborated only by agreement across independent search results, which is a
weaker channel than payload and must be labelled as such in any deliverable.**

### 🟢 The find: a complete five-region 2026 split, and it sums

Every prior pass of this file carried **one** regional row. The header said so outright: *"Market size —
global and the one region with a published split."* 🟢 **This pass obtained all five**, and the first thing
worth doing with five numbers is adding them up.

| Region | 2026 | Share of regional sum | CAGR (published) | 2030 implied by that CAGR |
|---|---|---|---|---|
| **North America** | **$3.68B** | **35.4%** | 31.1% | $10.87B |
| **APAC** | **$2.85B** | **27.4%** | **35.3%** — fastest | $9.55B |
| **Europe** | **$2.64B** | **25.4%** | 31.9% | $7.99B |
| **LATAM** | **$0.67B** | **6.4%** | 33.5% | $2.13B |
| **Middle East & Africa** | **$0.56B** | **5.4%** | 34.3% | $1.82B |
| 🟢 **Sum** | 🟢 **$10.40B** | 100% | **32.8%** implied | 🟢 **$32.36B** |

🟢 **The sum is exactly the published global 2026 figure of `$10.4B` — to the cent, 0.0% error.** And the
CAGR-implied 2030 sum, **$32.36B**, lands **0.3%** from the published global 2030 of **$32.27B**. 🔵 **Five
regional figures, five independent growth rates, and both the base year and the terminal year close.
That is a genuinely coherent series, and this KB has never had one before.**

### 🔴 Which means this file has been comparing a region from one series against a global from another

| | 2026 | 2030 | CAGR |
|---|---|---|---|
| 🟢 **Series A** — the regional series, now closed | **$10.40B** | **$32.27B** | **31.2%** |
| 🔴 **Series B** — this KB's canonical global row since cycle 2 | **$10.6B** | **$42.48B** | **41.5%** |

🔴 **They are different series from different houses and they are not interchangeable.** Series B's 2030
figure is **32% higher** than Series A's on a 2026 base only 1.9% higher — the divergence is almost
entirely in the growth assumption (41.5% vs 31.2%).

🔵 **This vindicates the earlier ruling and corrects its arithmetic.** This file already caught that a
`$32B` North America in 2030 was impossible and already published the internally consistent repair:

> *"**$10.8B** is the internally consistent figure, implying NA share *falling* to ~25% by 2030."*

🟢 **The `$10.8B` is right** — this pass independently derives **$10.87B** from NA's own 31.1% CAGR, and
confirms the `$32B` row is almost certainly **the global total transcribed into the North America cell**
(it is 99.2% of Series A's global 2030, and 2.9× NA's own CAGR-implied value). 🔴 **But the share
conclusion drawn from it is wrong, and wrong for a structural reason**: `$10.8B` is a **Series A** number
and it was divided by **`$42.48B`, a Series B** number. Corrected inside Series A:

| NA share of global | 2026 | 2030 |
|---|---|---|
| 🔴 As this file states it (`$10.8B / $42.48B`, series-mixed) | 36% | **~25%** |
| 🟢 Within Series A (`$10.87B / $32.36B`) | **35.4%** | 🟢 **33.6%** |

🟢 **North America's share is roughly flat — it falls about 1.8 points over four years, not eleven.** 🔵 **The
strategic reading changes with it.** "NA share collapsing to a quarter of the market by 2030" is a
reason to shift investment out of North America; "NA holding a third while APAC adds two points" is not.
🔴 **A series-mixing error of this shape does not look like an error — it produces a plausible number that
points the wrong way.**

> **`P477`.** Never divide a figure from one market series by a figure from another. Record the **series**
> (house, base year, terminal year, CAGR) as part of every market datum, and do arithmetic only **within**
> a series. A sum that closes to 0.0% is the evidence that identifies which series a figure belongs to —
> **so compute the sum before trusting any share.**

🟢 **What survives untouched:** the prior inference that *mature markets grow below the global rate* holds
in Series A on its own terms — NA **31.1%** and Europe **31.9%** are both below the **32.8%** implied
global rate, while **APAC (35.3%), MEA (34.3%) and LATAM (33.5%)** are all above it. 🔵 **The conclusion
was right; only the arithmetic under it was borrowed from the wrong series.**

✅ **Instruction for a deck, superseding the previous one.** Quote **2026** figures — they are the coherent
part and both houses agree within 2% on the global. For **2030**, quote **one series and name it**: Series
A ($32.27B global, NA $10.9B) or Series B ($42.48B global), never a region from one against a global from
the other. **Never quote the `$32B` North America 2030 figure at all** — it is a transcription artefact
that both this pass and the fifth pass independently identified.

### 🟢 Regulation — the one jurisdiction that moved from guidance to mandate

🔵 **Pass 35 established the sequencing fact that governs a multi-region roadmap: the EU deferred
education high-risk to 2 Dec 2027 while South Korea (22 Jan 2026) and Vietnam (1 Mar 2026) are already
live.** That stands. What this pass adds is the **sub-national** layer in North America, where the binding
instrument is state statute rather than a national act.

| Jurisdiction | Instrument | Status | Corroboration |
|---|---|---|---|
| 🇺🇸 **Ohio** | 🔴 **House Bill 96** — **every** K-12 public district must adopt an AI-use policy | 🔴 **Deadline 1 July 2026 — passed.** State model policy was due 31 Dec 2025 and released early Jan 2026; districts may adopt it or a locally developed policy aligned to it | 🟢 **Four independent outlets agree**, and the primary source (`education.ohio.gov` Ed-Connection, 6 Jan 2026) is identified — though 🔴 **blocked from this environment (000)** |
| 🇺🇸 **States, aggregate** | AI-in-education bills | ⚠️ **Counts disagree across trackers: "134 bills across 31 states" vs "52 bills across 25 states."** Different windows and inclusion rules; **the range is the finding, not either endpoint** | ⚠️ both secondary, both blocked |
| 🇺🇸 **States, guidance** | Department-of-education AI guidance | **35+ states** as of June 2026 | ⚠️ secondary |

🔵 **Ohio is the structurally important row and not because Ohio is large.** It is the **first** US state to
convert AI guidance into a **mandate with a date that has now passed** — so every Ohio district is, as of
1 July 2026, a client with a board-adopted AI policy already in force. 🟢 **That inverts the usual
engagement opening**: the question is no longer "help us form a position", it is "our policy exists and
our tooling does not comply with it yet." 🔴 **And the statute deliberately does not say what the policy
must contain, nor require teaching or using AI** — so the policies differ district by district, and a
product shipping into Ohio must read **each district's** policy, not the state model.

⚠️ **The named bill specifics below are secondary and single-sourced; treat as leads, verify before use.**
California **AB 1159** (prohibits using student data to train AI models) · Idaho **SB 1227** (data-privacy
requirements for school AI tools) · **Oklahoma** and **Maryland** (human oversight required; AI barred
from high-stakes decisions about students) · **Georgia** and **Mississippi** (CS credit including AI
instruction, late 2020s).

## Opportunities by region — thirty-sixth-pass update, 2026-10-07

### North America

🟢 **Market: $3.68B in 2026, 35.4% of the regional sum — the largest single region, and its share is
roughly flat to 2030 (33.6%), not collapsing (`P477`).** Adoption: 60% of US K-12 teachers used AI tools
in 2024-25, 32% at least weekly.

- 🟢 **Compliance retrofit against policies that already exist.** Ohio's HB 96 deadline **passed on 1 July
  2026**: districts hold board-adopted AI policies today, written locally and therefore inconsistent. 🔵 **The
  sellable unit is an audit-and-remediate engagement against *this district's* policy text** — not an AI
  strategy workshop. Hardest constraint to satisfy, and the one that recurs: **human oversight and a bar
  on AI making high-stakes student decisions** (Oklahoma, Maryland pattern).
- 🟢 **The permissive SIS pilot is newly possible here.** `rubelw/OSSS` (Apache-2.0, three channels) models
  **US district structure** — districts, transportation, accounting, board governance — so it is
  region-fit by construction. ⚠️ **Pilot and reference only: its workflow/state-machine logic is
  self-declared unfinished.** Pair it as the *architecture* with an existing SIS as the *system of record*.
- 🟢 **Student-data-training prohibitions (California AB 1159 pattern) make local/open-weight inference a
  compliance feature, not a cost decision.** The `bandup` architecture — local by default, explicit
  on-screen warning the moment data leaves the machine — is directly transferable, and its provenance
  (APAC) is irrelevant to its fitness here.

### EMEA

🟢 **Market: Europe $2.64B (25.4%) at 31.9%; Middle East & Africa $0.56B (5.4%) at 34.3% — the second-fastest
regional growth rate in the set, off the smallest base.** 🔴 **Still no region-wide EMEA adoption
percentage found** — a gap this file has carried for three passes and did not close.

- 🟢 **The 2 Dec 2027 deferral is a build window, not a holiday.** Article 50 transparency applies from Aug
  2026 regardless, and the substantive obligations are unchanged — risk management, data governance,
  technical documentation, human oversight, post-market monitoring. 🔵 **Sell the documentation and
  oversight scaffolding now, while the deadline is far enough away to be a design input rather than a
  remediation.**
- 🟢 **The in-tree permissive stack is EMEA-origin and that is a procurement argument, not just a technical
  one.** `OpenOLAT` (Apache-2.0, Univ. Zurich → frentix GmbH) and `qtiworks` (BSD-3-Clause, Edinburgh),
  now joined by **`lesson-plan-parse-mbsse` (MIT, Sierra Leone MBSSE)**. Sakai adds **ECL-2.0** and the
  Apereo higher-ed consortium model — 🔴 **ECL-2.0, not Apache-2.0: the patent grant differs and a legal
  review will ask (`P476`)**.
- 🟢 **MEA splits hard and the split is the targeting instruction.** Advanced national strategies and
  large-scale programmes in **Saudi Arabia, UAE, Qatar**; capacity-building via public-private
  partnership in **Egypt, Morocco, Jordan**; 🔴 **infrastructure and stability barriers in Yemen,
  Mauritania, Syria, Lebanon**. Regional players to know: **Classera** (Saudi/Egypt/Syria), **Abwaab**
  (Jordan/Saudi/Iraq). **Rwanda–Anthropic three-year MoU (Feb 2026)** covers health, education and
  public sector — ⚠️ secondary, single-sourced.
- 🟢 **`lesson-plan-parse-mbsse` is the template for the low-resource tier, and the template is the
  valuable part.** A national ministry's curriculum turned into structured JSON, **corpus shipped**, with
  rule-based parsing and LLMs confined to cleaning. 🔵 **Repeatable against any ministry that publishes
  lesson plans as PDF, which is most of them.**
- 🔴 **Channel blindness, re-confirmed:** nine European and public-sector forges (`code.europa.eu`,
  `codeberg.org`, `joinup.ec.europa.eu`, and six more) return **000**. **The EUPL tier is invisible from
  here.** ⚠️ **Scope: this is a statement about the instrument, never about the industry (`P469`).**

### APAC

🟢 **Market: $2.85B (27.4%), growing at 35.3% — the fastest region in the set, adding ~2 share points by
2030.** Ipsos Education Monitor 2026: lower support for banning AI in schools across the Asian markets
surveyed — 🔴 **but Australia and New Zealand record *higher* support for banning it, the one place in
this dataset where "APAC" splits in two.**

- 🔴 **This is the region where education AI obligations are already enforceable, and both statutes name
  exactly what an education deliverable does.** South Korea's **AI Basic Act** (in force 22 Jan 2026)
  treats education as **high-impact**; Vietnam's **Law on AI** (in force 1 Mar 2026) names education among
  six high-risk sectors, explicitly including **automated assessment** and **behavioural monitoring**. 🔵 **A
  grading or proctoring deliverable shipping into Seoul or Hanoi is in scope *today* — sixteen months
  before Brussels.** China: the most comprehensive framework in the region — mandatory registration,
  content-labelling, penalties to ¥50M. Japan: voluntary and innovation-friendly, may pivot. India:
  sectoral and privacy law for now.
- 🟢 **The two most transferable new assets in this pass are both APAC and both jurisdiction-shaped.**
  `bandup` (MIT) marks **named Singapore papers** against their own band descriptors; `MathTutor` (MIT)
  targets **India's JEE** with a 14-node LangGraph pipeline and a **critic agent that verifies its own
  answers**. 🔵 **Neither is a general tutor with a locale setting, and that is the point** — the rubric is
  the product.
- 🟢 **Self-verification is the compliance bridge, and it is already built.** Korea's high-impact and
  Vietnam's automated-assessment provisions both push toward demonstrable human oversight.
  `MathTutor`'s critic agent and `bandup`'s *"bands are unofficial"* framing plus tracked-changes
  evidence trail are **architectural answers to a regulatory requirement** — reusable far outside APAC.

### LATAM

🟢 **Market: $0.67B (6.4%) at 33.5% — above the implied global rate, smallest base of the five.** Adoption
is deep and governance is thin: **79%** of faculty use AI in teaching (**+18 points** vs the global 2025
figure) and **87%** of institutions use AI in at least one area, but 🔴 **88%** of faculty report only
*minimal to moderate* engagement and 🔴 **only 26%** of institutions have a **formal AI strategy**.
Enterprise AI deployment regionally: **47%**; Brazil (65.89), Chile (63.19), Uruguay (62.21) the only
LATAM entries in the global top 50; region ranks **7th** on AI readiness (avg 42.99).

- 🟢 **The 87%-using / 26%-with-a-strategy pair remains the single most actionable number in this file, and
  it names the product: governance, not technology.** 🔵 **Institutions here do not need to be sold AI;
  they are already running it without a policy.** Sequence governance first and the technical work follows
  with a mandate attached.
- 🟢 **`lm-evaluation-harness-pt` (MIT, CEIA / UFG Brazil) is the measurement layer this region lacked.**
  Portuguese task suite, **direct-response** evaluation so instruction-tuned chat models are measurable,
  **vLLM and LiteLLM on one harness** so a local open-weight model and a hosted API are compared on
  identical footing. 🔵 **This converts "which model for Brazil?" from a vendor claim into a measurement**
  — and it is exactly the artefact a 26%-strategy institution needs to write its first policy against.
- 🟢 **Brazil is the regulatory bellwether: PL 2.338/2023**, horizontal and risk-based, with a chapter on
  the rights of affected individuals and an obligation to provide *"clear and accessible information"* on
  exercising those rights. Mexico's bill adds a **"digital rights"** chapter including a right to interact
  and communicate through AI systems. ⚠️ Both **still bills**; dates secondary and unverifiable here.
- 🔴 **The constraint to plan around is talent, and it is worsening.** ECLAC/CEPAL: advanced AI training is
  concentrated in a few countries and the **talent gap against the global average has widened since
  2022**, with accelerating brain drain. CIOs in Bogotá, Mexico City and São Paulo report dozens of PoCs
  with **fewer than a third producing measurable P&L impact**. 🔵 **Staffing assumption: plan for
  build-and-transfer with documented handover, not for a client team that can take over cold.**
- 🔴 **Mexico gap, stated explicitly so silence is not read as coverage:** searched this pass
  (`open source education AI project Brazil Mexico Latin America github 2026`) and **no Mexico-origin
  permissive education asset surfaced**. LATAM representation on these shelves is **Brazil and Chile**
  (`lm-evaluation-harness-pt`, UFG; `Latam-GPT`/CENIA). ⚠️ **Scope: a claim about these queries, not about
  Mexico.**

## 🔴 Thirty-fifth pass, 2026-10-07 — the regulatory binding constraint moved out of Europe

⏱️ **Measured 2026-10-07 from secondary sources** (market-research houses, law-firm and
privacy-practice regulatory trackers, Council of the EU reporting, state legislative trackers,
UNESCO/IESALC, ECLAC, Digital Education Council, Ipsos Education Monitor 2026).
⚠️ **These are published estimates and reported survey results, not first-hand measurements.**
🔴 **Primary legal texts remain unreachable: `eur-lex.europa.eu` → 000 this pass, as in the previous
two.** **Every AI Act date below is secondary-sourced and must be re-verified against the Official
Journal before it enters a client deliverable.** `joinup.ec.europa.eu` and `codeberg.org` → **000**.

### 🔴 The headline: the EU deferred education high-risk by sixteen months, and APAC did not wait

For the whole life of this KB, the EU AI Act has been the date that governed an education AI roadmap.
🔴 **That is no longer true.**

| Jurisdiction | Instrument | Education status | In force / due |
|---|---|---|---|
| 🇪🇺 **EU** | AI Act, Annex III stand-alone high-risk | Education **access and assessment** — admission decisions, student evaluation, exam scoring — classified **high-risk** | 🔴 **deferred from 2 Aug 2026 to 2 Dec 2027** by the **Digital Omnibus**, given final Council approval **29 June 2026** |
| 🇪🇺 **EU** | AI Act, Annex I (AI embedded in regulated products) | — | **2 Aug 2028** |
| 🇪🇺 **EU** | AI Act **Article 50** (transparency) | Applies to education deployments | 🟢 **in force from Aug 2026 regardless of the deferral** |
| 🇰🇷 **South Korea** | **AI Basic Act** | Education named a **"high-impact"** domain alongside healthcare, finance, employment, essential services | 🔴 **in force 22 Jan 2026** |
| 🇻🇳 **Vietnam** | **Law on Artificial Intelligence** | Education is one of **six** high-risk sectors, explicitly incl. **automated assessment** and **behavioural monitoring** | 🔴 **in force 1 Mar 2026** |
| 🇹🇼 **Taiwan** | **AI Basic Act** | framework statute | passed **Dec 2025** |

🔵 **Read that table as a sequencing fact, not a compliance summary.** A multi-region education
platform shipping in 2026–27 now hits **enforceable obligations in Seoul and Hanoi before Brussels** —
and the Korean and Vietnamese statutes name **automated assessment** and **behavioural monitoring**,
which is exactly what an AI grading or proctoring deliverable is. 🔴 **The common error this creates:
treating the EU deferral as sixteen months of global breathing room.** It is not; it is sixteen months
of European breathing room during which two APAC statutes are already live.

⚠️ **And the deferral changes the date, not the work.** Reporting is consistent that the underlying
obligations — risk management, data governance, technical documentation, human oversight,
post-market monitoring — are **unchanged in substance**. 🔵 **Article 50 transparency applying from
Aug 2026 regardless** means a 2026 European deployment still has a live obligation today.

### 🟢 Market size — global and the one region with a published split

| Scope | 2025 | 2026 | Later | CAGR |
|---|---|---|---|---|
| **Global AI in education** | ~**$7.52B** | ~**$10.6B** | ~**$42.48B** by 2030 | **40.9%** → 41.5% |
| **North America** | — | ~**$3.68B** (**36%** of global) | ~**$32B** by 2030 | **31.1%** |

🔴 **This KB already resolved this conflict and I nearly re-derived it — which would have been
`P469` a third time.** The canonical `## Opportunities by region` block of this file closed it on
**internal-consistency arithmetic** at the fifth pass, and that ruling stands unchanged by anything
measured today:

> A $32B North America in 2030 against this KB's own $42.48B global row would put NA at **~75% of the
> entire global market**, contradicting the **36%** share asserted in the same breath. **$10.8B** is
> the internally consistent figure, implying NA share *falling* to ~25% by 2030 — consistent with the
> EMEA finding that mature markets grow below the global rate.

✅ **So the instruction to carry into a deck is the existing one, not a new one: quote `$3.68B` for
2026 (both houses agree) and give 2030 as `$10.8B–$32B`, source-dependent, naming the uncertainty.**
🔵 **The $32B figure I read this pass is the *higher* of the two already-recorded sources, not new
evidence** — the secondary tier is simply still republishing it. ⚠️ `grandviewresearch.com` remains
blocked by this environment's egress proxy, so the conflict stays **recorded, not resolved**.

### 🟢 Adoption depth, where it is measured

| Region | Adoption | Depth / governance |
|---|---|---|
| **North America** | **60%** of US K-12 teachers used AI tools in the 2024-25 school year; **32%** at least weekly | Governance is arriving through **state statute**, not institutional policy |
| **LATAM** | **79%** of faculty use AI in teaching — **+18 points** against the global 2025 figure; **87%** of institutions use AI in at least one area | 🔴 **88%** of faculty report only **"minimal" to "moderate"** engagement, and **only 26%** of institutions have a **formal AI strategy** |
| **APAC** | Ipsos Education Monitor 2026: **lower** support for banning AI in schools across the Asian markets surveyed | 🔴 **Australia and New Zealand record *higher* support for banning AI in schools** — the one place in this dataset where "APAC" splits in two |
| **EMEA** | 🔴 **no comparable region-wide adoption percentage found this pass** | Most deployments reported on OpenAI or Anthropic APIs; districts with strict **data-residency** requirements self-host open-weight models |

🔵 **The LATAM pair — 87% using, 26% with a strategy — is the single most actionable number in this
file**, and it is a governance gap, not a technology gap.

## Opportunities by region — thirty-fifth-pass update, 2026-10-07

### North America

- 🟢 **Policy-to-implementation work has a statutory deadline.** **Ohio is the first state to require
  every K-12 district** to adopt a formal AI use policy — the state model or a locally developed
  policy aligned to it — **by 1 July 2026**. **134 AI-in-education bills across 31 states** in 2026.
  🔵 **Thousands of districts need the artefact, not the advice**: policy instantiation, staff
  training, an audit trail.
- 🟢 **"No student data trains a model" is now an architectural requirement, not a preference.**
  **California AB 1159** prohibits using student data to train AI models; **Idaho SB 1227** mandates
  data-privacy protections for school AI tools. 🔵 This makes the **self-hosted / retrieval-only**
  architecture — Ollama or vLLM behind a local index, no training feedback loop — a **compliance
  position** a vendor API cannot match. Pairs directly with the permissive substrate on these shelves.
- 🟢 **Human-in-the-loop as a product feature.** **Oklahoma and Maryland** require human oversight and
  bar AI from high-stakes student decisions. 🔵 Grading and proctoring deliverables need the
  **override path, the reviewer queue and the decision log** as first-class components.
- 🟡 **Curriculum delivery:** **Georgia and Mississippi** require computer-science credit including AI
  instruction from the late 2020s — a slower, larger content opportunity.

### EMEA

- 🟢 **A sixteen-month conformity window with a known end date.** Annex III education obligations due
  **2 Dec 2027**. 🔵 **The deferral is the opportunity**: risk-management files, data-governance
  documentation, human-oversight design and post-market monitoring can now be built *before*
  enforcement rather than retrofitted under it. ⚠️ **Sell it as a programme with a date, not as
  urgency** — and verify the date against the Official Journal, which this KB cannot reach.
- 🟢 **Article 50 transparency is live now.** A 2026 European deployment has an obligation today,
  independent of the 2027 deferral. 🔵 **The nearest-term EMEA engagement on this shelf.**
- 🟢 **Data residency is the technical differentiator**, with a permissive stack to serve it — and as
  of this pass, **an EMEA-origin permissive platform to anchor it**: **OpenOLAT** (Apache-2.0, Zurich
  / frentix, **in-tree extensible**) and **qtiworks** (BSD-3-Clause, Edinburgh) — see `P469`.
- 🔴 **Declared gap, stated rather than left silent:** no region-wide EMEA adoption statistic was
  found this pass, and **nine European public-sector forges return 000** from this environment.
  🔵 **Never quote this KB's EMEA shelf as market evidence** — ask the client's procurement which
  national forge they publish to.

### APAC

- 🟢 **The most urgent compliance work in this file, because it is already enforceable.** Korea's AI
  Basic Act (**22 Jan 2026**, education = *high-impact*) and Vietnam's AI Law (**1 Mar 2026**,
  education incl. **automated assessment** and **behavioural monitoring**). 🔵 **Any assessment or
  proctoring product sold into these markets is in scope now**, not in 2027.
- 🟢 **Multi-jurisdiction architecture is the differentiating capability.** China enforces binding
  rules on algorithms, deep synthesis and generative AI; Korea, Vietnam and Taiwan have comprehensive
  statutes with enforcement teeth; **Singapore and Japan rely on voluntary guidelines backed by
  existing law**. 🔵 **No single compliance posture covers APAC** — the deliverable is a
  **policy-per-jurisdiction** design, which is `compose/patterns.md` **`P46`**.
- 🟢 **Named national programmes:** **Japan's** transition to official **digital textbooks**;
  **Korea's** expansion of **AI language tools for foreign families**. Both are content-and-platform
  work, not model work.
- ⚠️ **Do not treat APAC as one market on sentiment either.** **Australia and New Zealand show higher
  support for banning AI in schools** than the Asian markets surveyed — the same product needs a
  different posture in Sydney than in Seoul.

### LATAM

- 🟢 **The clearest commercial opening in this file: 87% of institutions use AI, 26% have a strategy.**
  🔵 Governance and strategy work — AI policy, academic-integrity frameworks, faculty enablement —
  **before** platform work. UNESCO's finding is the same: institutions are using generative AI for
  teaching, learning and research **without clear policies to govern it**.
- 🟢 **Depth, not adoption, is the gap.** 79% of faculty use AI but **88% report minimal-to-moderate
  engagement**, concentrated in producing teaching materials, multimedia and administrative support.
  🔵 **The upsell is assessment, feedback and analytics** — the uses that need the governance above.
- 🟢 **Regional institutions to anchor a bid:** **Uruguay** is the **first Latin American country to
  sign the Council of Europe Framework Convention on AI** (a legally binding treaty); UNESCO launched
  the **Observatory on AI in Education for Latin America and the Caribbean** on **14 April**;
  **Latam-GPT** is led by Chile's **CENIA** with **30+ institutions across 8 countries**.
- 🟡 **Maturity tiers for territory planning:** **Chile, Brazil, Uruguay** are consolidated pioneers;
  **Colombia, Ecuador, Costa Rica, the Dominican Republic** and four others are *adopters*.
  **ECLAC**: adoption is accelerating while **investment, talent and governance** lag.

### Global

- 🟢 **The cross-region product thesis for 2026, consistent across every source read this pass:**
  purpose-built education platforms are displacing generic AI tools, because pedagogical structure —
  learning objectives, grade-level expectations, assessment logic, instructional flow — has to be
  **in the system**, not in a prompt.
- 🟢 **Teacher-first is the measurable adoption predictor.** Reporting converges on **5–10 hours saved
  per teacher per week** as the threshold that predicts retention of an AI tool in a school.
  🔵 **Instrument that metric in the deliverable** — it is the renewal argument.
- 🟡 **Digital credentials and the skills economy** keep gaining: real-time skills visibility,
  competency frameworks, career-navigation tools across K-12, post-secondary and workforce. This KB
  already holds the permissive standards tier for it (Open Badges, European Learning Model, CASS, ESCO).

## 🔴 Thirty-fourth pass, 2026-10-07 — funding is down 44% on a like-for-like window, and that is worse than this KB recorded

⏱️ **Measured 2026-10-07 from secondary sources** (market-research houses, state and national
legislative trackers, Ipsos Education Monitor 2026, UNESCO/ECLAC, Digital Education Council,
law-firm regulatory trackers, the Latin American AI Index). ⚠️ **These are published estimates and
reported survey results, not first-hand measurements.** 🔴 **Primary legal texts remain unreachable:**
`eur-lex.europa.eu` → **000** this pass, as last pass. **Every AI Act date below is secondary-sourced
and must be re-verified against the Official Journal before it enters a client deliverable.** This
pass additionally measured `code.europa.eu` → **000** (see `repos/foundations.md`, `P467`).

### 🔴 The funding scissor, re-measured on a like-for-like window

Pass 32 recorded funding "fell 26%". A like-for-like comparison this pass gives a **worse** number:

| Window | Raised | Deals | Average deal |
|---|---|---|---|
| **January–July 2025** | ~**$774M** | **37** | ~$20.9M |
| **January–July 2026** | ~**$435M** | **24** | ~$18.1M |
| **Change** | 🔴 **−43.8%** | 🔴 **−35.1%** | 🔴 **−13.4%** |

🔵 **Capital is down far more than deal count, and deal count is down more than deal size.** The
market is not repricing rounds downward so much as **doing fewer of them** — fewer companies are
clearing the bar at all. A separate count puts AI-education startups at **$232.07M across 32
disclosed rounds for Aug 2025 – Sep 2026**, consistent in direction.

⚠️ **This is the single most important slide in a commercial conversation, and it cuts both ways.**
Against: nobody is funding a new education AI product. For: **47% of higher-education institutions
now use AI structurally** in teaching and administration while capital retreats — which is the
definition of a services market rather than a product market. The buyer is the institution, the
budget is operational, and the deliverable is integration into what they already run.

### Global market size — the disagreement is still the finding

| Source type | 2026 value | Forward |
|---|---|---|
| Spread across four research houses | **$6.4B – $11.4B** | — |
| One house, explicit | **$10.6B** (2026) | **$42.48B by 2030**, 41.5% CAGR |
| Precedence Research | — | **$136.79B by 2035** |
| Whole EdTech market (context) | **$404B**, 16.3% CAGR | AI the fastest segment at **+42%/yr** |

🔴 **A 78% spread between the low and high 2026 estimate.** Quote the range, never a point. The only
defensible framing: *"the AI-in-education market is somewhere between $6B and $11B in 2026, and it is
the fastest-growing segment of a $404B sector."*

## Opportunities by region — thirty-fourth-pass update, 2026-10-07

### North America

📊 **Measured:** **134 AI-in-education bills introduced across 31 states** in the 2026 session;
**35+ states** now publish official AI guidance through their departments of education (as of June
2026); one tracker counts **68 bills across 27 states with 10 already enacted** in 2026.

🔵 **The legislative content has converged on three things**, and each is a buildable deliverable:

| What states are legislating | Example | The engagement it creates |
|---|---|---|
| **Student data must not train models** | **California AB 1159** prohibits using student data to train AI models | A **data-boundary architecture**: local inference or contractual no-train guarantees, provable. This is `P38`/`P40` territory — the client must be able to *show* the data never left. |
| **Human oversight on high-stakes decisions** | **Oklahoma** and **Maryland** require human oversight and **ban AI from high-stakes decisions about students** | A **gated-decision workflow**: AI proposes, a named human disposes, and the gate is logged. This is `P11` (one oversight gate), and it is now a statutory requirement rather than a nicety. |
| **AI in the curriculum itself** | **Georgia** and **Mississippi** require computer-science credits including AI instruction | **Curriculum and teacher-enablement** work — content generation plus training, `P6` and `P8`. |

🟡 **Higher education is behind K-12 on policy and knows it.** State officials are now setting rules
for universities, and the open questions are explicitly: **must faculty disclose AI use, must students
disclose AI use, and what uses are permitted.** 🔵 **That is a policy-and-tooling engagement, not a
model engagement** — the deliverable is a disclosure workflow wired into the LMS submission path, and
`ucfopen/canvasapi` (added this pass) is the MIT layer for the Canvas half of it.

🟢 **Sell into North America:** the **data-boundary proof** and the **logged human gate**. Both are
now compliance line items in named statutes, which means they have a budget owner.

### EMEA

📊 **Measured:** the **EU AI Act (Regulation (EU) 2024/1689)** classifies AI used in education for
**admission decisions, assessment of learning outcomes, evaluation of students and steering of an
individual's educational path** as **high-risk** (Annex III). Schools and universities that *use*
third-party AI are **deployers** with their own obligations — not bystanders. The Act also imposes an
**AI-literacy duty** on providers and deployers for staff who operate AI systems. Secondary sources
place full enforcement of the relevant provisions at **August 2026**. 🔴 **Date secondary-sourced —
`eur-lex` 000.**

🔵 **The deployer obligation is the commercial key, and it is widely missed.** A school that buys an
essay-grading tool cannot discharge its duties by pointing at the vendor: it owes risk management,
data governance, **human oversight**, transparency to students, and documented AI literacy for staff.
Every one of those is a documentation-and-process deliverable Globant can produce, and none of them
requires building a model.

| Obligation | Deliverable |
|---|---|
| Human oversight, documented | The `P11` oversight gate with an audit trail that names the human |
| Data governance | Local-first deployment (`P4`, `P40`); `coqui-tts` MPL / `faster-whisper` MIT keep the speech tier clean |
| Transparency to the student | Explainable scoring — **evidence breakdown, not a bare percentage** |
| AI literacy for staff | `P6` enablement, and the MIT `promptster-ai/rubric` taxonomy as a scorecard starting point |
| Conformity before deployment | The AI Act education profile already in `P13` |

🔴 **And a standing caveat this pass sharpened:** this KB's EMEA *repository* shelf is thin, and
**`P467` shows that is partly because every European public-sector forge is unreachable from this
instrument** (`code.europa.eu`, `gitlab.opencode.de`, `forge.apps.education.fr`, Codeberg, Framagit,
FSFE — all 000). 🔵 **Do not present EMEA open-source thinness to a client as market evidence.** One
EMEA-origin asset did arrive this pass: `macsnoeren/genai-open-assessment` (Netherlands, **GPL-3.0**),
an auditable rubric-driven grader for open questions — exactly the Annex III shape, in the wrong
licence for embedding and the right one for a standalone.

🟢 **Sell into EMEA:** **deployer compliance as a service**. The regulation creates the obligation,
the institution carries it, and almost none of them have the documentation.

### APAC

📊 **Measured — three binding statutes landed inside twelve months:**

| Jurisdiction | Instrument | Status |
|---|---|---|
| **Vietnam** | Law on Artificial Intelligence | 🔴 **in force 2026-03-01** |
| **South Korea** | AI Basic Act | 🔴 **in force 2026-01-22** |
| **Taiwan** | AI Basic Act | passed **December 2025** |
| **India** | dedicated AI legislation, risk-based | **signalled July 2026** — not yet law |
| **Singapore, Japan** | voluntary guidelines on existing law | no AI statute |

📊 **Adoption is led by Singapore at a 60.9% AI diffusion rate** among working-age adults, with
**South Korea posting the world's largest gain in H2 2025**; Australia, Korea and Taiwan follow, with
Japan, India and China measured as relatively behind on diffusion.

📊 **And the public has already decided.** Support for *banning* AI in schools (Ipsos Education
Monitor 2026): **Indonesia 23%, Thailand 25%, India 26%, Singapore 28%, Japan 29%, Malaysia 29%,
South Korea 31%.** 🟢 **No APAC market measured has even a third of the public behind a ban** — the
social licence to deploy exists, which is not true everywhere.

🔵 **The hard part in APAC is not permission, it is jurisdictional multiplicity.** A regional client
spans a binding Vietnamese law, a binding Korean act, a Taiwanese framework act, voluntary Singapore
and Japanese guidance, and an Indian regime that does not exist yet. 🟢 **That is `P6`/`P9`/`P16`
territory and the pattern is policy-as-configuration:** one agent architecture, per-jurisdiction
policy nodes, so adding a country is a config change rather than a rebuild.

📊 **Every major APAC economy is building a sovereign model:** India's **Sarvam AI**, Malaysia's
**ILMU**, Indonesia's **Sahabat AI**, Singapore's **SEA-LION**, South Korea's **HyperCLOVA X Think**,
Japan's **NTT Sarashina**. 🔴 **This KB cannot verify a single one of their weights licences —
`huggingface.co` is 000** (see `intel/trends.md`, standing limit). 🔵 **Treat "sovereign model
available" as a client-supplied input, never as a KB finding.**

🟢 **Sell into APAC:** the **multi-jurisdiction policy layer**, and **integration against a sovereign
model the client chooses** — with the model licence as the client's representation, in writing.

### LATAM

📊 **Measured:** **more than 50% of teachers in Chile and Brazil already use AI tools, while fewer
than 10% of institutions in the region have formal guidelines.** Regional enterprise AI deployment
sits at **47%**, with only **Brazil (65.89), Chile (63.19) and Uruguay (62.21)** inside the global
top 50. **UNESCO launched the Observatory on AI in Education for Latin America and the Caribbean on
2026-04-14** at ECLAC headquarters in Santiago.

🔴 **The teacher/institution gap is the sellable work, and it is a governance gap, not a technology
gap.** Over half of teachers are using these tools inside institutions that have written nothing
down. This is consistent in direction with the 87%-adoption-against-26%-strategy figure pass 33
recorded, and it is the same shape measured a different way. 🔵 **The first LATAM deliverable is
almost never a model. It is an acceptable-use policy, a data-handling boundary, and a teacher
enablement programme** — then the tooling.

📊 **Regulation is converging on the EU risk-based model, and none of it is finished:**

| Country | Instrument | Distinctive feature |
|---|---|---|
| **Brazil** | **PL 2.338/2023** — horizontal statute | The regional bellwether: risk-based, transparency duties, a supervisory architecture. Brazil also **signed an AI and tech-regulation agreement with the EU in June 2026**, which makes EU-shaped compliance work directly reusable. |
| **Chile** | government-sponsored bill (executive draft **2024-05-07**) | Supervision tied to Chile's forthcoming data-protection authority. **ILIA 2025 ranks Chile 1st in LATAM**, "pioneer" tier. |
| **Mexico** | federal bill in the Senate (2024) | Explicit **"technological sovereignty"** framing — reducing dependence on foreign models is a stated policy goal, not a preference. |

🟢 **Latam-GPT** remains the regional anchor: led by **CENIA (Chile)** with **30+ institutions across
8 countries**, trained on regional corpora. 🔵 **Mexico's sovereignty framing plus Latam-GPT plus a
Brazil–EU regulatory alignment is a coherent sales story:** build on regional models, with EU-shaped
governance, deployable on infrastructure the client owns — which is `P5`, `P40` and `P42`.

🟢 **Sell into LATAM:** **governance first, on top of adoption that already happened.** The region has
the highest teacher uptake and the least institutional documentation of any region measured here.

### 🔵 Cross-region read, thirty-fourth pass

| Region | Binding regime | Adoption | The gap you are paid to close |
|---|---|---|---|
| **North America** | 🟡 state-by-state, 10 statutes enacted 2026 | high, policy-led | **Provable data boundaries + logged human gates** |
| **EMEA** | 🔴 hardest (AI Act Annex III, deployer duties) | moderate | **Deployer compliance documentation** |
| **APAC** | 🟡 three binding statutes, diverging | led by Singapore | **One architecture, many jurisdictions** |
| **LATAM** | 🟢 lightest, all bills pending | **highest teacher uptake** | **Governance for adoption that already happened** |

🔵 **The regions are not at different stages of the same journey; they are solving different
problems.** EMEA buys compliance, LATAM buys governance, North America buys provable boundaries, APAC
buys portability. **A single pitch deck will fail in three of four.**

## 🔴 Thirty-third pass, 2026-10-07 — LATAM's number is 87% adoption against 26% strategy, and that 61-point gap is the sellable work

⏱️ **Measured 2026-10-07 from secondary sources** (market research houses, legislative trackers,
Digital Education Council, UNESCO/IESALC, law-firm regulatory trackers). ⚠️ **These are published
estimates and reported survey results, not first-hand measurements.** 🔴 **Primary legal texts could
not be reached this pass:** `eur-lex.europa.eu` → **000** (egress-blocked), so every AI Act date below
is corroborated across independent secondary sources but **not read from the Official Journal**.

### 🔴 The EMEA date this KB had reverted on

| Instrument | Date | Status |
|---|---|---|
| **Article 50** transparency (labelling, machine-readable marking) | **2026-08-02** | 🔴 **In force. Not deferred by the Omnibus** |
| Article 50(2) backstop for systems deployed before 2026-08-02 | **2026-12-02** | ⏳ weeks away |
| **Annex III §3 stand-alone high-risk — education** | **2027-12-02** | deferred from 2026-08-02 by Reg. (EU) 2026/1744 |
| Annex I embedded high-risk | **2028-08-02** | deferred from 2027-08-02 |

🔴 **This pass corrected a regression inside this KB, not the open web.** Three pass-32 sections —
`compose/patterns.md` P38, `intel/trends.md` and this file — had reverted to *"full enforcement from
August 2026"*, a claim this KB had already corrected as `P284`. **The stale date was in the freshest
layer**, at the top of the files a reader opens first, while the correct dates sat deeper in the same
files. 🔵 **A KB that only grows forward re-acquires its own corrected errors** every time a pass
drafts a new top section from search summaries instead of from the tree below it.

🟢 **Independent corroboration gained this pass:** the Council's final approval of the Digital Omnibus
on **2026-06-29**, and education named explicitly among the deferred Annex III categories, from
sources independent of those used when `P284` was recorded.

🔵 **The commercial read is unchanged and still counter-intuitive: the near-term EMEA deliverable is
the small one.** Clients who heard *"the high-risk deadline moved to 2027"* have usually deferred the
**labelling** work too — and that duty is live now, with the already-deployed backstop at
**2026-12-02**. **Sell the Article 50 marking engagement this quarter; schedule Annex III conformity
for the 2027 cycle.**

## Opportunities by region — thirty-third-pass update, 2026-10-07

### North America

🟢 **The policy surface is now dense enough to sell against by name.** As of **September 2026**,
**40 states plus Puerto Rico** have official AI guidance or policy frameworks for education, and the
PIE Network tracked **~100 state bills** touching students' use of AI in K-12.

| Instrument | State | What it does |
|---|---|---|
| **AI in schools act** (enacted, March) | **Idaho** | Requires **local district and charter AI policies**, state **AI-literacy standards** and training, and provides that **no AI replaces or eliminates a human teacher** |
| Enacted this session | **Utah** | K-12 AI education law |
| **RAISE Act** (enacted late 2025) | **New York** | the earliest of the current wave |
| **A.B. 1159** (live) | **California** | would bar student data from training AI models **unless the school benefits** |
| **HB 650** (live) | **Vermont** | edtech providers must **register and certify privacy compliance annually** |
| **S.B. 1546** (enacted) | **Oregon** | minor-protective **design** duties, including reducing compulsive use for presumed-child users |
| **S.B. 394** (enacted) | **Virginia** | directs the state agency to issue guidance covering **teacher training** |

🟢 **Four more states now require districts to adopt AI policies.** 🔵 **The opportunity is the
district-level policy-to-implementation gap.** A mandate to *have* a policy is not capacity to
implement one: Idaho's AI-literacy standards and Virginia's teacher-training guidance both create
work no district has staff for. **Sell policy-conformant implementation and teacher enablement, per
district, against a named statute** — and note that the **human-teacher guarantee** in Idaho's law
makes assistive, human-gated designs the only compliant shape, which is precisely the local-first
explainable stack on this KB's shelves.

### EMEA

🟡 **Two-phase, and the near phase is weeks away** — see the table above. **Article 50 transparency is
live since 2026-08-02**, the backstop for already-deployed systems lands **2026-12-02**, and
**Annex III education conformity is due 2027-12-02**.

🔵 **Opportunity, in order of how soon it can be invoiced:**

1. **Article 50 marking and classification sweep** — inventory every AI touchpoint, label outputs,
   emit machine-readable provenance. **Due now; most clients think it was deferred.** 🟢 The highest
   urgency-to-effort ratio in any region this pass.
2. **Annex III conformity evidence** for assessment and admissions systems — technical
   documentation, risk management, data governance, human-oversight records. **2027-12-02.**
3. **The AI-literacy obligation** (live since 2025-02-02 and never deferred) — staff training for
   every organisation that *uses* AI, not just those that build it.

⚠️ **Do not quote any of these dates to a client without a EUR-Lex check**, which **this environment
cannot perform** (`eur-lex.europa.eu` → **000**).

### APAC

🟢 **Three comprehensive AI statutes came into force within four months, and education is named in
the scope of at least two.**

| Jurisdiction | Instrument | Status | Education relevance |
|---|---|---|---|
| **South Korea** | **AI Basic Act** | in force **2026-01-22** | scopes *"high-impact AI"* in healthcare, **education**, finance, employment and essential services |
| **Vietnam** | **Law on Artificial Intelligence** | effective **2026-03-01** | with **Decree 33** (in force 2026-08-15) classifying biometric learner-behaviour analysis as high-risk |
| **Taiwan** | **AI Basic Act** | passed **2025-12** | framework legislation |

**Adoption: 65–75% (2025) → 80–90% (2026 projected).** Named incumbents: **Google, Microsoft, IBM,
Pearson, Byju's.** China, India and Japan dominate regional spend.

🔵 **The opportunity is that APAC now has three different compliance regimes and no portability
layer between them.** A vendor selling into Korea, Vietnam and Taiwan needs one system that can
evidence conformity under three statutes with different definitions of high-risk. 🟢 **Build the
evidence layer once, parameterised by jurisdiction** — the same artefact set that satisfies EU
Annex III largely satisfies Korea's high-impact duties, and Vietnam's biometric clause is the
strictest, so design to it and the others follow. ⚠️ **"No education agent layer on an APAC
sovereign model" remains open** — `aisingapore/sealion` still serves **no licence payload**, so the
regional-model pedagogy layer is still unbuilt and still unavailable to build on.

### LATAM

🔴 **The number that defines the region this pass: 87% of institutions use AI in at least one area,
and only 26% have a formal AI strategy.** A **61-point governance gap** is the clearest single
commercial signal in any region on this shelf.

| Signal | Value | Source shape |
|---|---|---|
| Faculty holding positive/very positive views of AI | **72%** (vs **57%** globally) | Digital Education Council, **7,319 faculty, 29 institutions** |
| Faculty using AI in teaching | **79%** | same survey |
| 🔴 Faculty reporting only *minimal to moderate* engagement | **88%** | same survey |
| Institutions using AI in ≥1 area | **87%** | regional study |
| 🔴 Institutions with a **formal AI strategy** | **26%** | same study |

🟢 **LATAM is the most AI-positive region measured and the least governed.** Enthusiasm is 15 points
above global, usage is high, depth is shallow (**88% minimal-to-moderate**), and three in four
institutions are running AI with no strategy behind it. 🔵 **That is not a technology sale, it is a
governance-and-depth sale** — and it is the inverse of EMEA, where the regulation forces the
governance and the appetite lags.

**Regional infrastructure that changed this pass:**

- **UNESCO launched its Observatory on AI in Education for Latin America and the Caribbean on
  2026-04-14** — a regional platform to help states integrate AI into education systems. 🟢 **A
  citable, neutral anchor for a governance engagement**, which the region previously lacked.
- **Uruguay** became the **first LATAM country to sign the Council of Europe's Framework Convention
  on AI** — the first hard regional commitment to an external standard, and a template for others.
- **Latam-GPT** (CENIA Chile, **60+ institutions across 15 countries**, ~**$550k**, funded largely by
  **CAF**): 🟢 tooling permissively licensed (**MIT**/**MIT-0**, verified from payload this pass),
  🔴 weights reported under the **non-OSI Llama 3.1 Community Licence** and **unverifiable from this
  environment**. ⚠️ **Not one of the three code grants is held by CENIA or any partner institution**
  (`P463`).

🔵 **The sharpest LATAM offer, assembled only from things verified this pass:** take the **87%/26%**
gap as the diagnosis, the **UNESCO Observatory** as the external framework, and
[`latam-gpt/anonymization-filter`](https://github.com/latam-gpt/anonymization-filter) (**MIT**) as
the first technical deliverable — Spanish/Portuguese PII scrubbing in front of whatever the
institution already deployed without a strategy. **It is a small, concrete, compliance-retiring build
on top of an installed base that is already there**, which is exactly what a market with 26% strategy
coverage and constrained capital can fund.

## 🔴 Thirty-second pass, 2026-10-07 — adoption is near-saturated, funding fell 26%, and that gap is the whole commercial story

⏱️ **Measured 2026-10-07 from secondary sources** (market research houses, legislative trackers,
UNESCO IESALC). ⚠️ **These are published estimates, not first-hand measurements**, and where two
houses disagree this pass records **both numbers and the disagreement** rather than picking one.

### Global market size — and a disagreement worth carrying

| Metric | Value | Source shape |
|---|---|---|
| AI in education, 2025 | **$7.52B** | market-research baseline |
| AI in education, 2026 | **$10.6B** | ~**40.9% CAGR** off 2025 |
| AI in education, 2030 | **$42.48B** | ~**41.5% CAGR** 2026→2030 |
| North America share, 2026 | **36%**, ≈ **$3.68B** | largest single region |
| APAC, 2026 | ≈ **$2.85B** | fastest-growing region |
| 🔴 APAC CAGR | **35.3%** *or* **28.1%** | ⚠️ **two houses, two answers** |
| APAC, 2033 | **$18.21B** | the 28.1% series |
| Edtech VC funding, H1 2026 | **$1B, −26% YoY** | 🔴 **down while adoption rises** |

🔴 **The APAC CAGR disagreement is not noise and should not be averaged.** One series puts APAC at
**35.3%** growth off a $2.85B 2026 base; another projects **28.1%** to 2033. Different base years and
different scope definitions produce materially different 5-year numbers, and a deck that quotes one
without the other is quoting a coin flip. **Carry the range, name the uncertainty.**

### The adoption/funding scissor — read this before any pricing conversation

| Signal | Value |
|---|---|
| Students using AI in their studies (16 countries) | **86%** |
| Educational organisations having adopted generative AI | **86%** — 🟢 **the highest of any industry** |
| US K-12 teachers who used AI tools in 2024–25 | **60%** (**32%** at least weekly) |
| Edtech venture funding, H1 2026 | **$1B, −26% YoY**, smaller and more selective cheques |

🔵 **Adoption is near-saturated and capital is retreating. Those two facts together define the
engagement.** When 86% of institutions have already adopted *something*, there is no greenfield
"introduce AI" project left to sell — the work is **consolidation, governance and proving value on
what is already in the building**. And because funding is down 26%, the buyer cannot fund a
speculative platform build; they can fund **a bounded project that retires a specific compliance or
cost risk**. 🟢 **This is precisely why the permissive local-first stack added to
`repos/foundations.md` this pass matters commercially:** `education-ai-suite` (Apache-2.0, OpenVINO,
**with hardware benchmarking**) + `prometheus-eval` (Apache-2.0, open weights) + `rubric` (MIT)
replaces recurring per-seat API spend with a one-time integration on hardware the client already
owns. In a −26% funding market, "lower your run-rate and pass your audit" sells and "transform your
institution" does not.

⚠️ **The honest counterweight:** an 86% adoption figure counts *any* generative-AI use, including a
teacher using a consumer chatbot unsanctioned. It is a measure of **diffusion, not of deployed
institutional capability**, and the gap between the two is where the governance work lives. Do not
quote 86% as 86% of institutions having a governed AI programme — they do not.

## Opportunities by region — thirty-second-pass update, 2026-10-07

### North America

**Regulation turned from guidance into mandate, with dated deadlines.**

- 🔴 **Ohio is the first state to require every K-12 district to adopt a formal AI use policy** —
  either the state model or a locally developed policy aligned to it — **by 1 July 2026**.
- **Oklahoma S.B. 1734** requires every district to adopt a written AI policy **before the 2027–28
  school year**.
- **~100 state bills in 2026** touch students' use of AI directly; **1,500+** AI-related bills were
  introduced nationwide.
- **Idaho S.B. 1227** — statewide K-12 AI framework, mandated local policies, AI-literacy standards,
  educator training, data-privacy requirements, and an explicit prohibition on **AI replacing human
  teachers**.
- **California A.B. 1159** (proposed) — would bar student data from training AI models **unless
  doing so directly benefits the school**.
- **Oregon S.B. 1546** — design-feature requirements protecting minors, including measures reducing
  **compulsive use** when the user is known or presumed to be a child.
- **Virginia S.B. 394** — directs the state education agency to issue guidance including teacher
  training.

🟢 **The opportunity: policy-to-implementation, with a deadline attached.** Hundreds of districts
must have a *written, defensible* AI policy by a fixed date, and a policy document alone does not
satisfy it — someone has to show the tools in use match the policy. That is an inventory,
a data-flow map, a control set and an evidence trail. 🔵 **A.B. 1159 and Idaho's data-privacy clause
specifically favour the local-inference stack**: if student work never leaves district
infrastructure, the "is our data training someone's model?" question answers itself, and
`prometheus-eval`'s open weights plus `education-ai-suite`'s on-device pipelines are the
implementation. ⚠️ **Oregon S.B. 1546 is the one that catches engagement teams off guard** — it
regulates *engagement mechanics*, so an adaptive tutor with streaks and nudges can be a compliance
problem in Oregon while being the product requirement everywhere else. `DeepTutor`'s proactive
Heartbeat check-ins are exactly the pattern that needs review there.

### EMEA

**The hardest compliance regime, and this KB's thinnest repo shelf — second pass running.**

- **EU AI Act: Annex III conformity duties due 2 December 2027.** ⏸️ **[pass 33, 2026-10-07: this
  line read *"full enforcement by August 2026"* — superseded by Regulation (EU) 2026/1744 (*Digital
  Omnibus on AI*, CELEX 32026R1744). **Article 50 transparency was not deferred** and applies from
  2026-08-02. See `P284`.]** Adopted 2024, phased through 2026–28.
- 🔴 **Education is HIGH-RISK under Annex III** where AI determines **access** (admissions), performs
  **assessment** of learning outcomes, or influences a person's **educational path** — plus exam
  scoring and proctoring. High-risk obligations attach **before deployment**: risk management, data
  governance, human oversight, transparency, and **conformity assessment**.
- **AI-literacy duty**: providers *and deployers* must ensure a sufficient level of AI literacy among
  staff operating the systems.
- Schools are now accountable for auditing their own AI use for safety, fairness and transparency.

🟢 **The opportunity is conformity assessment as a delivery product, not a PDF.** Annex III makes
grading and admissions the regulated core of edtech, which means the artefacts an engagement must
produce are known in advance: a documented risk-management file, data-governance lineage, a
demonstrable human-in-the-loop, and reproducible evidence for every automated decision. 🔵 **This is
the direct commercial case for `rubric` (MIT) + `prometheus-eval` (Apache-2.0):** a weighted rubric
held as a **data structure** rather than a prompt makes each scoring decision replayable and
inspectable, which is what a conformity file needs; open evaluator weights mean the deployer can
actually audit the model instead of citing a vendor. ⚠️ **And the AI-literacy duty is billable and
usually forgotten** — it is a *legal obligation* with no technical deliverable, which maps onto the
Spanish/English enablement assets on this shelf (`IA-PARA-TODOS`, Apache-2.0, added this pass;
plus the Microsoft and Hugging Face courses already shelved).

🔴 **The gap, stated as a gap:** searched for EUPL/Apache/BSD **EMEA-origin** education repos and
found none this pass, for the second consecutive pass. Found only institutional news (Central
European University × GitHub, April 2026, open AI teaching materials). **EMEA has the strictest
requirements and the least local open-source supply** — the engagement will be built on Global repos
configured for EU constraints, not on EU-origin code. Plan the sovereignty conversation accordingly.

### APAC

**The widest spread between national ambition and classroom reality — including one reversal.**

- **China and the UAE are the only nations running compulsory, national AI curricula**, since the
  2025–26 school year.
- 🟢 **India is the largest single bet:** AI and computational thinking **mandatory from Class 3**
  across government and private schools, backed by the **₹10,372 crore IndiaAI mission**. **DIKSHA**
  (Ministry of Education digital public infrastructure) already ships AI for *inclusion*: keyword
  search inside video, read-aloud for visually impaired students.
- 🔴 **South Korea is the cautionary tale.** Seoul mandated AI textbooks from 2025; adoption sat
  **below 30%** by March, and in **August the National Assembly stripped them of official textbook
  status** after unions said the pace had outrun teacher preparation. Korea is also the **second
  jurisdiction after the EU** to enact comprehensive AI legislation.
- **Japan** moves slowly and deliberately: digital textbooks may gain official status **as early as
  the 2030 school year**.
- Market: ≈**$2.85B** in 2026; **$18.21B by 2033** on the 28.1% series. ⚠️ CAGR disputed (above).

🟢 **The opportunity is teacher-readiness infrastructure, and Korea is the proof.** A national
mandate failed at **under 30% adoption** not for lack of technology or funding but because
preparation lagged — and the legislature then reversed it. That is the most actionable fact in this
the region: the binding constraint on APAC AI-in-education is **teacher capability and
trust, not product**. Engagements that lead with training, classroom-evidence collection and staged rollout
survive; engagements that lead with a platform repeat Korea. 🔵 **India's DIKSHA is the better
template and the better integration target** — it treats AI as *accessibility* (read-aloud,
in-video search) rather than as replacement, which is both politically durable and technically
modest. `project-sunbird/sunbird-lms-service` (MIT, the stack behind DIKSHA) is already on this
shelf from pass 31, which makes this a buildable regional play rather than a thesis. ⚠️ **China and
the UAE are curriculum-delivery opportunities but not open-source supply:** no permissively licensed
APAC-origin education agent was added this pass, and `datawhalechina/hello-agents` — the notable
APAC curriculum repo — is **CC BY-NC-SA 4.0, unusable in a client deliverable** (pass 31).

### LATAM

🟢 **Gap closed on supply this pass, and the real constraint is now named precisely: licences.**

- **UNESCO IESALC: adoption is widespread across LAC higher education while governance lags.**
- **UNESCO Observatory on AI in Education for Latin America and the Caribbean** convenes **33
  Ministries of Education** and their learning ecosystems.
- **Mexico: 73% of university students use AI for coursework**, while **over 80% of Mexican higher
  education institutions have no clear normative framework** governing ethical or academic use.
- **Chile leads on policy** — National AI Policy since 2021, with a law under discussion.
- **Brazil and Colombia** have national AI strategies but **no education-sector-specific
  regulation**.
- 🟢 **Supply:** [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) — **MIT**, Universidad
  Tecnológica de Pereira, Colombia: an Open-edX-native tutor agent for **rural** higher education,
  with TTS, avatar and a teacher analytics panel.
- 🔴 **But 3 of the 4 LATAM repos found this pass carry no licence at all**:
  `a-bobadilla/Asistente-Pedagogico-IA` (Canvas, competency-based lesson planning, Spanish),
  `henriquebotelhogomes/educacao` (Brazil — LangChain + Llama 3/Groq + Docling + Qdrant RAG tutor),
  `virginiandujar/educa-ia`.

🟢 **The opportunity: the 73%/80% inversion is a governance engagement with a number on it.** Nearly
three quarters of Mexican students already use AI for coursework while four fifths of institutions
have no framework — the demand has already happened and the institution is the part that is missing.
Academic-integrity policy, assessment redesign that assumes AI availability, and a sanctioned
institutional tool are the deliverables, and the Observatory's 33 ministries make this
**procurable at ministry scale**, not one campus at a time. 🔵 **`TutorIA` is the credible regional
reference**: Colombian, public-university, rural-first, MIT, and it demonstrates the Apache-2.0
XBlock side-car shape against an AGPL Open edX core (`repos/foundations.md`). ⚠️ **And the licence
finding is itself a service offering**: three LATAM teams shipped real, relevant work that **no
client can legally use**. Getting a grant added upstream costs one file; it converts unusable
regional work into a reusable asset, and it is the cheapest regional contribution Globant could
make.

### 🔵 Cross-region read, thirty-second pass

| Region | Binding constraint | What to sell |
|---|---|---|
| North America | **dated policy mandates** (Ohio 1 Jul 2026) | policy→implementation evidence; local inference answers A.B. 1159 |
| EMEA | **Annex III high-risk, Aug 2026** | conformity assessment as deliverable + the AI-literacy duty |
| APAC | **teacher readiness** (Korea reversed at <30%) | training-led staged rollout; DIKSHA/Sunbird accessibility pattern |
| LATAM | **governance vacuum** (73% use / 80% no framework) | ministry-scale policy + assessment redesign; `TutorIA` as reference |

🔴 **One thing is true in all four regions and is the strongest claim this pass can make:** the
regulated object is **assessment**. EU Annex III names it, US states legislate the student data that
feeds it, Korea's reversal was about trusting it, and LATAM's vacuum is academic integrity in it.
🟢 **A rubric held as auditable data, scored by weights the client controls, is therefore the single
highest-leverage technical asset in this industry** — and as of this pass the permissive stack for
it is complete and verified: `rubric` (MIT) + `prometheus-eval` (Apache-2.0) +
`education-ai-suite` (Apache-2.0). ⚠️ Every number in this section is a **published estimate**, two
of them disagree by 7 CAGR points, and none was measured first-hand.

# Market Intelligence — Education

## Global market size

| Metric | Value | Source basis |
|---|---|---|
| AI in education market, 2025 | $7.52B | Research and Markets, AI in Education Market Report 2026 |
| AI in education market, 2026 | $10.6B | same; 40.9% CAGR 2025→2026 |
| Projected 2030 | $42.48B | 41.5% CAGR |
| Alternative long-range series, 2025 | $6.4B | A second house's base year — **lower than the $7.52B above for the same year** |
| Alternative long-range series, 2034 | $79.6B | 31.35% CAGR 2026–2034, same house |
| 🔴 **Third series, 2025** | **$8.3B** | A third house — **higher** than both base years above |
| 🔴 **Third series, 2026** | **$11.4B** | same house; **25.9%** CAGR |
| 🔴 **Third series, 2033** | **$57.2B** | same house |

🔴 **The third series was added to this file by the seventeenth pass and never reached this table —
corrected in the twenty-first pass of 2026-10-06.** That pass read it, named it *"Forecast A"*,
called the pair *"two incompatible growth models"* and wrote the right prescription. ⚠️ **But it wrote
all of that inside its own pass-scoped section ~3,600 lines down, while the table at the top of the
file — the one a reader actually quotes — went on presenting the 40.9% series as settled.** The
twenty-first pass re-ran the mandatory trends query, got the third series back, and **spent most of a
finding re-discovering what this file already knew.** 🔵 **Measured: `40.9%` appears 19 times and
`42.48` 12 times across the non-archive files, against 10 for `11.4B` and 6 for `25.9%`.**

⚠️ **This is the third reproduction of one propagation failure.** The nineteenth pass corrected a
stale AI Act date and the twentieth found it surviving in two further locations; here a recorded
conflict failed to reach the summary table above it. 🟢 **The rule it earns: a correction that lands
only in a pass-scoped section has not been applied — it has been filed.** When a pass corrects a
figure, it must edit the table that publishes that figure, in the same pass.

**Two incompatible series, re-checked in the sixth pass of 2026-10-06.** One house
puts 2025 at **$7.52B** growing at ~41% CAGR to **$42.48B by 2030**; another puts
2025 at **$6.4B** growing at **31.35%** to **$79.6B by 2034**. They disagree on the
base year by **$1.1B** and on the growth rate by **ten points**. **Quote one series
with its source attached, or quote the direction only.** A deck that mixes the
$6.4B base with the 41% CAGR is producing a number nobody published.

**Segment splits worth quoting** (single-source, so attribute them): cloud-based
delivery held **71.22%** share in 2024; **K-12 is 45.62%** of total adoption; STEM
captured **34.78%** of revenue; and **language learning is the fastest-growing
segment** — which is the segment the sixth pass's language and speech shelf serves
directly. Student AI usage is reported rising from **66% in 2024 to 92% in 2025**,
with ~**86% of higher-education students** using AI as a primary research and
brainstorming partner entering 2026.

🆕 **New segment figure, thirtieth pass of 2026-10-07, filed here rather than only in a
pass-scoped section** (this file's own rule, earned above): the **North America AI-for-Kids** market,
**USD 482M (2024) → USD 1,082M (2034), 12.5% CAGR**. ⚠️ **Read the boundary before quoting it: this
is adjacent to the AI-in-education series, not inside it**, and at **12.5%** it is a far slower curve
than any of the three head series in the table above (40.9%, 31.35%, 25.9%). 🔵 **Which makes it
useful precisely as a brake:** the children's-product segment of the market grows at roughly a third
the rate of the institutional one, so a deck that justifies a K-12 consumer play with the
institutional CAGR is overstating its own case by ~3×.

Growth is real but the composition is shifting: the defining movement of 2026 is
**away from generic AI tools and toward platforms purpose-built for education**,
and from experimentation toward governance. Budget is moving to whoever can show
instructional value and a defensible oversight story — which is a services
opportunity more than a licensing one.

## Opportunities by region — thirtieth-pass update, 2026-10-07

🔴 **Execution of this tree's instruments was DENIED this pass** (`[Code from External]`), so nothing
here is a re-measurement (`P107`); the regional queries were run and every figure below was checked
against this file by string. 🔴 **All four regional queries returned 0 new repositories to this
run** — so what each region gets below is the *demand* side, plus an explicit statement of what is
still missing. ⚠️ **Renumbered from "twenty-ninth" at merge time:** the concurrently-running pass 29
landed first, and its three new repositories (all **enablement assets**, not education products, and
all Global rather than regional) are recorded in `repos/trending.md`. **The drought in education
*product* repositories stands at eighteen passes; a flat "0 new" does not.**

### North America

🟢 **The one genuinely new figure of the pass, and it is NA's:** AI-for-Kids, **USD 482M (2024) →
USD 1,082M (2034), 12.5% CAGR** — filed with its boundary in the segment paragraph above. Held and
re-confirmed: **$951M → $2,303.2M by 2029 at 15.9%**, **36%** of global adoption share, **10%** of
institutions with formal AI guidelines, **71%** of teachers untrained, Colorado and Texas legislating
piecemeal.

- **Opportunity.** The gap between **36% of adoption** and **10% with a written policy** is the whole
  offer: governance-as-deliverable, not model work. The **71% untrained** figure is the same
  opportunity expressed as enablement.
- ⚠️ **The structural asymmetry to quote carefully:** education AI in the US faces **no sector
  regulator** — there is no FDA-equivalent for edtech, and adoption is decided school by school.
  Compare the EU, where the AI Act classifies education AI as **high-risk**. A single product cannot
  be sold into both on one compliance story.

### EMEA

**0 new repositories, and every demand figure held by string:** **94%** of organisations likely to
invest in AI-specific training in 2026, against **38% that have not begun piloting** and **60%**
reporting siloed data; the Council of Europe's education-sector instrument work continues under the
Framework Convention.

- **Opportunity.** The **94% / 38%** pair is the sharpest number in this file for EMEA: near-universal
  intent, with more than a third of the market not past the starting line. That is a
  first-pilot-delivery business, and the AI Act's high-risk classification makes the compliance
  artefacts part of the product rather than overhead.
- 🔴 **Declared gap, unchanged and specific:** no EMEA-origin *permissive* education agent has
  surfaced from the mandatory query set in eighteen passes. The EMEA public-sector tier this KB does
  hold is **EUPL** and **GPL-2.0** (see pass 28's nine `UNKNOWN → EUPL` corrections), which is a
  licence-posture finding, not an absence of code.

### APAC

**0 new repositories; demand figures held:** **48%** of governance leaders putting AI adoption among
their top 2026 priorities, **57%** of Asian organisations already using AI in at least one area,
Singapore's financial-sector AI consultations as the regional template, LearnUpon's Sydney HQ, the
TCS–Pearson learning alliance.

- 🆕 **The frame that moved this pass: "sovereign-by-design."** APAC 2026 coverage has shifted from
  pilots to sovereignty, which is expected to shape infrastructure choices for roughly **half** of
  APAC firms. Recorded as an org-level signal only.
- **Opportunity.** Sovereignty is an architecture requirement Globant can meet with the shelf this KB
  already holds — on-premise inference, local model weights, no cross-border inference calls — and it
  converts a procurement obstacle into a reason to choose a systems integrator over a SaaS vendor.
- ⚠️ **Not recorded as evidence:** the OpenAI ANZ policy appointment behind much of this coverage is
  an anthroponym, and an anthroponym is not a finding (`P135`).

### LATAM

**0 new repositories; demand figures held:** third-largest market worldwide for generative-AI
application downloads, **99%** of LATAM startups using AI internally and **85%** embedding it in the
product, OpenAI integrated by **89%**, UNESCO IESALC's survey of **200 higher-education institutions
across 19 countries**, the IADB's enabling-regulatory-framework paper, **Ednova (Chile)** as the named
standout edtech.

- **Opportunity.** Highest adoption against lowest capital access remains the regional signature: the
  demand is proven and the constraint is delivery capacity, which is the one thing a studio sells.
  Regulatory fragmentation across LATAM makes a **portable** compliance layer worth more here than a
  jurisdiction-specific one.
- 🟢 **The gap this KB already closed, and it stays closed:** the claim of *"zero LATAM-origin
  repositories"*, published four passes running in the pre-reset lineage, was **refuted** by this
  KB's own index — **12 repositories located in LATAM**, among them `LabSirius/TutorIA` (**MIT**,
  Universidad Tecnológica de Pereira, SNCTI-funded) and `portabilis/i-educar` (Brazilian municipal
  school system). ⚠️ **Note its licence posture:** `i-educar` is one of pass 28's `LGPL → GPL-2.0`
  corrections, so it is a *link-against* risk, not a permissive base.

## Market map

**Proprietary incumbents.** Khan Academy (Khanmigo — publicly funded at state
level in the US), Instructure (Canvas), Anthology/Blackboard, Pearson, Duolingo,
Google for Education, Microsoft Education. These own the buyer relationship.

**Open source platform layer.** Moodle (GPL-3.0), Open edX (AGPL-3.0), Canvas LMS
(AGPL-3.0), Chamilo (GPL-3.0), Sakai (ECL-2.0), ILIAS (GPL-3.0), Frappe LMS
(AGPL-3.0), Kolibri (MIT), Oppia (Apache-2.0). See `verticals/solutions.md`.

**Open source AI layer.** DeepTutor (Apache-2.0, 40.8k★) is the only
education-native agent project with real gravity. Below it, and substantially
re-measured in the third pass of 2026-10-06: **StudyMate** (MIT, 624★, China),
**anki-mcp-server** (MIT, 506★, 53 tools — the largest education MCP server),
**OpenTutor** (MIT, 130★, FSRS 4.5 + knowledge graph + local-first), **Mentingo**
(MIT, 91★, the first permissive AI-native LMS), OATutor (MIT, the auditable mastery
model), Educhain (MIT, content generation), canvas-mcp and moodle-mcp-server (MIT,
integration), plus a cluster of MIT **Agent Skills** at 100–300★
(universal-examprep-skill, algo-sensei, universal-diagnostic-tutor-skill,
kaogong-skill, education-skills). General frameworks — MAF, smolagents, LangGraph,
pydantic-ai, all MIT/Apache-2.0 — supply the rest.

**The layer is no longer thin, and that changes the pitch.** Three passes on
2026-10-06 took the permissive education shelf from "DeepTutor plus fragments" to
roughly 30 verified permissive projects, including a full MIT LMS. The
differentiator is shifting from *finding* the open source parts to **composing,
licensing and governing** them — which is also the part a client cannot do from a
listicle.

**Where Globant fits.** The platform layer is copyleft and the AI layer is thin.
The reusable, defensible position is the **permissive side-car**: agent services
that integrate over LTI 1.3 and MCP, carry Globant's own license, and work
against whichever LMS the client already runs.

## Opportunities by region — superseded (the live block is at the top of this file)

### North America

- **Largest regional share: 36% of the global market, $3.68B in 2026**, declining
  to **~25% by 2030** as APAC grows faster. **The 2030 figure is $10.8B.** The
  fourth pass recorded it as disputed and unresolved; the **fifth pass closed it
  on internal-consistency arithmetic** — see "Fifth pass" below, and stop quoting
  a range.
- **SIZING CONFLICT, flagged in the fourth pass of 2026-10-06 — do not quote
  "$32B by 2030" unqualified.** Earlier passes of this KB recorded NA 2030 at
  **$32B**. A second source puts NA at **$3.68B (2026) → $10.8B (2030), 31.1%
  CAGR**. The two cannot both be right, and **the lower one is the more internally
  consistent**: this KB's own global row is $42.48B in 2030, and 36% of that is
  ~$15.3B, so a $32B North America would be **~75% of the entire global market** —
  contradicting the 36% share asserted in the same breath. $10.8B implies NA share
  *falling* to ~25% by 2030, which is consistent with the KB's EMEA finding that
  mature markets grow below the global rate.
  **How to use it:** quote **$3.68B for 2026** (both sources agree) and give 2030
  as **$10.8B–$32B, source-dependent**, naming the uncertainty. The primary
  source could not be re-read this pass — `grandviewresearch.com` is blocked by
  this environment's egress proxy — so the conflict is **recorded, not resolved**.
  Same treatment this KB already applies to MEA.
- Adoption is already broad: **60% of US K-12 teachers used AI tools in the
  2024–25 school year; 32% used them at least weekly.** The sale is no longer
  "should you use AI" — it is governance, procurement and integration.
- **Regulation is the demand driver.** 134 AI-in-education bills introduced
  across 31 states in 2026. Concretely:
  - California **AB 1159** — the **Learner Personal Information Protection Act
    (CALPIPA)**, **signed by Governor Newsom on 10 September 2026**. Bars
    companies from using **identifiable** student data to train generative AI or
    build AI systems, and extends protection to **reproductive-health and
    immigration** records. **Its higher-education provisions begin 1 July 2027** —
    a dated, known-in-advance procurement trigger for every university vendor in
    the state. Put it in the pipeline now.
  - Idaho **SB 1227** — the **Generative Artificial Intelligence in Education
    Act**, and it is much more than a data-privacy bill. It requires a **statewide
    K-12 AI framework**, local district policies, **AI literacy standards and
    educator training**, data-privacy requirements for AI tools, and it
    **prohibits AI from replacing human teachers** — the statute's own test is
    that **"human judgment remains the final authority."** The training mandate is
    a **billable enablement line**, not just a constraint.
  - Oklahoma **SB 1734** — AI permitted **only under educator supervision with
    human review**, barred from high-stakes decisions, state guidance plus
    district policies required, and **annual disclosure to parents**. That last
    item is a recurring reporting obligation, which means a recurring deliverable.
  - Maryland **Artificial Intelligence Ready Schools Act** — all **24** local
    districts must adopt aligned policies within **120 days of MSDE releasing its
    guidance**. Note the shape: a **rolling deadline keyed to a state
    publication**, not a fixed calendar date, so the buying window opens when MSDE
    publishes.
  - **Ohio HB 96** (the 2025–2027 operating budget) — **the first state to mandate
    AI frameworks in every public K-12 district.** DEW published its model policy
    by **31 December 2025**; every district had to adopt a written AI policy by
    **1 July 2026**. **That deadline has now passed**, so Ohio's 600+ districts are
    no longer buying policy documents — they are in the **implement-and-audit**
    phase, which is the more valuable engagement and the one with no incumbent.
  - **Georgia and Mississippi** require computer science credits including AI
    instruction from the late 2020s.
  - **New York City DOE** issued guidance in March 2026 built on a "Traffic
    Light Framework," informed by Google and OpenAI.
  - **North Carolina SB 1006** — the **K-12 Innovation and Transformation Act**,
    which creates an **AI Academic Support Program** letting public school units
    contract with Khan Academy for **Khanmigo in grades 6–12**. Two details change
    how you read it: the money is **more than $10M in *recurring* state funding**,
    not a one-off pilot, and it was **directed to a single vendor without
    competitive bidding** (defended publicly by sponsor Senator Michael Lee,
    R-New Hanover, in June 2026). **Read-across:** states will fund AI tutoring as
    a standing line item, and a sole-source award of that size invites both
    procurement challenges and copycat RFPs in neighbouring states. The opening is
    the **integration, oversight and evidence layer around** such a contract — not
    competing with the tutor itself.
- **Opportunity:** policy-to-implementation work. Districts now have mandates and
  no capability. Offer: AI policy implementation, a human-oversight gate wired
  into the grade path, student-data-boundary architecture (AB 1159 means
  no-training-on-student-data must be *provable*), and Canvas integration via
  canvas-mcp. Sell the audit trail, not the chatbot.

**New this pass (2026-10-06):**

- **All 50 states** have now introduced AI legislation — the 134 bills across 31
  states specific to education sit inside a universal legislative wave. There is
  no national stance to design against; the unit of compliance is the state.
- **States have split into two camps, and they need opposite offers.** One camp is
  building procurement pipelines with real budget behind adoption (North Carolina's
  $10M for Khanmigo is the template). The other is applying brakes — bans,
  moratoriums and strict consent requirements. Qualify which camp a district sits
  in before pitching: in camp one you sell deployment, in camp two you sell
  governance, assurance and an auditable oversight gate, and a deployment pitch
  will lose.
- **Idaho SB 1227** joins California AB 1159 on student-data protection for AI
  tools in schools — the no-training-on-student-data requirement is now a
  multi-state pattern, not a California quirk, so build the data boundary once and
  evidence it everywhere.
- **Students are now a stakeholder with a published position.** In August 2026,
  students from all 50 states produced a **national framework for AI in America's
  schools** (via AASA). Student-body buy-in is becoming part of the procurement
  conversation; cite the framework in proposals rather than being surprised by it.

**Third pass (2026-10-06) — channel saturated, nothing net new.** The North America
query was re-run and returned the same facts already recorded above: 36% share /
$3.68B in 2026 (2030 **disputed: $10.8B–$32B**, see the sizing conflict above);
60% of K-12 teachers using AI in 2024–25 with 32% weekly; 134 bills across 31
states; California AB 1159 and Idaho SB 1227; Oklahoma and Maryland human-oversight
requirements; Ohio's July 2026 policy deadline; North Carolina's $10M Khanmigo
earmark; the AASA student framework from all 50 states (created at America's Youth
AI Festival in July 2026).

**The "saturated" verdict recorded here in the third pass was premature, and the
fourth pass of 2026-10-06 withdraws it.** That pass claimed the open-web channel
was exhausted for North America and that only procurement portals and state
trackers could add depth. Re-running general searches returned **materially more
per bill** without touching a single procurement portal: a **statute name and
signing date** for AB 1159 plus a **1 July 2027 higher-education trigger** nobody
had recorded; Idaho SB 1227's real scope (**an AI-literacy and educator-training
mandate with a "human judgment is final" test**, not a privacy bill); a **bill
number** for Oklahoma (**SB 1734**) and its **annual parent-disclosure**
obligation; Maryland's **24 districts / 120-day rolling** mechanism; Ohio's
**HB 96** vehicle and the fact its deadline is now **past**; and North Carolina's
funding being **recurring and sole-sourced**.

**The lesson is about the claim, not the region.** "Saturated" conflated *no new
entities* with *no new information*. The entity list barely moved; the
**mechanisms, dates and bill numbers** — which are what make a finding sellable —
were mostly absent. Before declaring a channel exhausted, ask whether the next
pass would add **rows** or **precision**, and treat the second as worth a pass on
its own. Procurement portals and state trackers remain the right instrument for
going deeper still.


#### Fifth pass, 2026-10-06 — the sizing conflict resolves, and it resolves in favour of the lower figure

The fourth pass recorded the NA 2030 figure as **disputed and unresolved**, with
the primary source unreachable. It can now be closed on arithmetic alone, using
this KB's own global row, and the conclusion is **$10.8B, not $32B**:

| Check | Figure | Verdict |
|---|---|---|
| Global 2026 (this KB's own row) | **$10.6B** | — |
| NA 2026 at the asserted 36% share | 36% × $10.6B = **$3.82B** | matches the recorded **$3.68B** to within rounding. **The 2026 figures are mutually consistent** |
| Global 2030 (this KB's own row) | **$42.48B** | — |
| NA 2030 at **$32B** | would be **75%** of global | **incoherent** with a 36% share asserted on the same page |
| NA 2030 at **$10.8B** | **25%** of global; implies **31.1% CAGR** | **coherent** — and it sits almost exactly on EMEA's independently sourced **31.9%** CAGR |

**Quote $3.68B (2026) → $10.8B (2030), ~31% CAGR, and say NA's share declines
from 36% to ~25% as APAC grows faster.** That last clause is the sellable part:
it is the arithmetic consequence of a 41.5% global CAGR against a 31% North
American one, and it is the reason an NA-only account strategy loses ground even
while the NA number triples.

**Retire the $32B figure.** It is not a range endpoint; it is an outlier that
fails an internal-consistency check against two of this KB's own rows and against
EMEA's independently sourced growth rate.

**One NA entity added this pass:** the **STUDENTS FIRST Act of 2026**, drafted by
students representing all 50 states at America's Youth AI Festival in July 2026
and published through **AASA** (the School Superintendents Association) in August
2026. It proposes protections for authentic learning, student privacy, fairness,
**human judgment** and relationships. It is not law and will not become law in
this form — its value is that it is **student-authored and superintendent-amplified**,
which makes it the cheapest available legitimacy artefact for a district-facing
oversight proposal. It also converges on the same "human judgment is final" test
this KB records as the one testable rule US state law has settled on.



#### Sixth pass, 2026-10-06 — the voice and language layer

**Market position re-read this pass.** North America was **$951M in 2024** heading
to **$2,303.2M by 2029 (15.9% CAGR)** on one house's numbers, and is quoted
elsewhere as **41.7% of the global opportunity** with a **45% CAGR for 2025–2030**
— a spread wide enough that only the direction is safe to quote. It leads regional
adoption at **36% share**; **66% of students** use ChatGPT; and **AI literacy is
LinkedIn's #1 skill for 2026, carrying a 56% wage premium**.

**The regulatory asymmetry is the sales point.** Education AI here operates in a
**relative regulatory vacuum — there is no FDA equivalent for educational
technology**, and adoption decisions sit with individual districts and
universities with minimal external oversight. State law is piecemeal (Colorado,
Texas). Meanwhile the **EU AI Act takes full effect in August 2026** and
classifies education AI as high-risk. **A North American client selling into
Europe inherits the stricter regime**, so build to P13 and sell the compliance
posture as a feature rather than waiting for a US mandate.

**What this pass opens here:**

- **Oral reading fluency (P17) is the strongest single opportunity in this
  region.** US literacy screening is a large, mandated, recurring spend and
  **every system doing it is proprietary** — FLORA, Literably (IES-funded),
  Amplify Text Reading Online, SoapBox Labs, none with a public repository. The
  permissive components are now all shelved and a **public dataset with a
  published baseline** exists. An open, auditable WCPM assessor with teacher
  override satisfies the "human judgment is final" rule US state law has converged
  on (trend 16) and has no open competitor.
- **Spanish-language instruction is now servable from permissive components.**
  The English-language-learner population is the region's largest underserved
  segment, and `sherpa-onnx` (Apache-2.0) plus `idiap/coqui-ai-TTS` (MPL-2.0)
  cover Spanish speech in and out, on-premises, with no student audio leaving the
  district — which is also the FERPA-friendly architecture.

#### Seventh pass of 2026-10-06 — the federal bill, and a trending repo you cannot ship

**Net new to this file: there is now federal legislation moving.** The **House
Education Committee advanced the K-12 AI Literacy and Readiness Act of 2026
(H.R. 8747)**, which would amend the Elementary and Secondary Education Act to
let schools **spend federal funds on AI curriculum and literacy programmes**.
This KB had the state-level picture in detail (134 bills across 31 states;
California AB 1159 barring student data from model training; Idaho SB 1227;
Oklahoma and Maryland requiring human oversight; North Carolina's $10M Khanmigo
earmark) and nothing at the federal level.

**Why it matters more than most bills: it is a funding authorisation, not a
restriction.** Every other instrument this KB tracks for North America
*constrains* deployment. This one would create a **federal budget line for
exactly the enablement work Globant already sells** — teacher and student AI
literacy, curriculum integration — on top of the state procurement pipelines
already funded. It has advanced from committee only; treat it as pipeline
intelligence, not as a closed sale.

**A procurement caution from the repository side of this pass.**
[cs341-illinois/coursebook](https://github.com/cs341-illinois/coursebook) — an
open systems-programming textbook from **UIUC** — gained **~1,626★ in one week**,
the fastest-growing education repository seen in any pass of this KB, and it has
**no `LICENSE` payload**. North American higher-ed clients will bring
repositories like this to the table as "open" course material. **Trending
velocity, institutional provenance and the word "open" are all orthogonal to
whether rights were granted.** Probe before promising, and expect to have this
conversation with a university client who believes their own repo is usable.


#### Eighth pass, 2026-10-06 — nothing new found for this region, and that is the finding

The eighth pass ran the mandated North America sweep (`AI education North
America 2026 adoption regulation state law`) and it returned **only material
this file already holds**: the 134 bills across 31 states, California **AB
1159** (prohibiting the use of student data to train models), Idaho **SB 1227**,
the Oklahoma and Maryland human-oversight statutes, Ohio **HB 96** and the
district-level-policy approach, plus the federal K-12 AI task force.

**One new item, and it is small:** Tennessee **SB 1711** joins Ohio HB 96 in the
*delegate-to-districts* column rather than the statewide-rule column. That
matters only because it strengthens a pattern already recorded here — in the US
the buyer of AI governance is increasingly **the district**, not the state, which
is a procurement shape (many small buyers, each needing a policy artefact) rather
than a product shape.

**Recorded as a saturation signal, not as coverage.** Four consecutive passes
have now returned the same North America facts from a general-language search.
The channel is exhausted; the next North America finding will have to come from
a different one — district RFP language, state education-agency procurement
portals, or the vendor-side filings, none of which this KB has swept.

#### Ninth pass, 2026-10-06 — the procurement channel opens, and it is the strongest North America finding in five passes

**Channel.** The eighth pass declared this region's general-language channel
exhausted and named the required replacement: *"district RFP language, state
education-agency procurement portals, or vendor filings — none of which this KB
has ever swept."* Two of the three were swept this pass.

⚠️ **Tier 2 throughout this subsection.** Every figure, date and statutory
reference below comes from **corroborated search summaries, not primary
documents.** `k12-ai-infrastructure.org`, `digitalpromise.org`, `cosn.org`,
`marylandpublicschools.org`, `excelined.org`, `njsba.org`, `web.ped.nm.gov` and
`marketbrief.edweek.org` are all **EGRESS_BLOCKED** in this environment. **No RFP
and no state guidance document was read.** Confirm each citation against the
primary source before it reaches a client deliverable.

##### 1. The supply side is being bought, with a permissive licence floor

**The K-12 AI Infrastructure Program** — **$26M**, multi-year, led by **Digital
Promise** with core partners **Learning Data Insights**, **DrivenData**, the
**Massive Data Institute at Georgetown University** and **Catalyst @ Penn GSE**.
**Gates Foundation**-funded, and the Foundation manages proposal review and award
monitoring directly. Launched **3 Nov 2025**; first cycle opened **4 Feb 2026**.

| Instrument | Size | Scope | Dates |
|---|---|---|---|
| **EDU AI** — Open Source AI Model for Tutoring | **up to $8M**, one award | Open-source education-specific model(s) + research, to make **K-12 math tutoring as effective as human experts** | Released 1 Jun 2026; **closed 31 Jul 2026**; work from **Nov 2026**; 30–36 months |
| **T&L Benchmarks and Datasets** | not established | **Three** standalone open-source **K-12 instructional data corpora** + an **AI benchmark** for adaptive learning | Open |
| Cohort 1 grants | 4 awards, 6–12 months | Learning Equality (science misconceptions); Princeton (simulated student models); **National Tutoring Observatory / Cornell** (ASR leaderboards); Stanford (**KB-TutorBench**, formative assessment) | Announced **29 Jun 2026** |
| Cohort 2 grants | **8 awards**, 6–12 months | **Formative assessment** focus, plus math, literacy and writing; outputs stated to be **openly licensed** | Announced **21 Sept 2026** |

**The licence condition is the commercially material fact:** all funded
developments must be released under a licence **at least as permissive as
CC-BY-4.0 (content) or Apache-2.0 (code/models)**, with Apache-2.0 recommended
for software and code *including evaluations, models and applications*.

**What this means for a North America engagement.** The region's open-source
education AI supply is, for the first time, **a funded pipeline with named owners
and dates** rather than an organic shelf. Twelve projects are in flight; none has
published code yet (measured: `KB-TutorBench` → 0 repositories; `learningequality`
filtered on `benchmark` → 0 repositories). **The opportunity is positional**:
design client architectures now so Apache-2.0 benchmarks and models drop in as
they land through 2027 — pattern **P23** — and approach the grantees as
integration partners. **Learning Equality is both a grantee and the maintainer of
Kolibri (MIT)**, which this KB already recommends.

##### 2. The demand side now specifies the architecture, through procurement rubrics

The regulatory frame in this region had been *"state law says human judgment is
final"* (trend 16). The procurement layer is more specific, and it is what a
vendor actually has to satisfy:

- **Maryland SB 720** (effective **1 Jun 2026**) — the state department must
  publish guidance **and an AI-tool evaluation rubric**; each local school system
  must adopt an aligned policy **within 120 days** and designate an **AI
  coordinator**. Reported as **24 districts** required to adopt AI policies by
  **Fall 2026**. State AI guidance was published **Feb 2026**.
- **Vermont** (guidance **23 Jan 2026**) — an evaluation-process rubric for AI
  tools covering **educational value, data-privacy compliance, usability and
  accessibility, cost, scalability, vendor reputation and age restrictions.**
- **Idaho, Maryland, Alabama** — statutory requirements that LEAs conduct
  **structured capability assessments**, **verify pre-training standards**, and
  **prohibit vendor training on student records.**
- **Contract language** is converging on a clause prohibiting unauthorised use of
  school data to train models, with explicit documentation and approval for any
  AI system training.
- **CoSN, *U.S. State of EdTech 2026*: 39% of districts include
  interoperability in their RFP evaluation rubrics.** This is the first
  *procurement-side* number this KB has for its trend 4 (MCP/LTI as the
  integration layer) — interoperability is no longer an engineering preference,
  it is a scored criterion in two of five district solicitations.

**Live tutoring procurements** (useful as demand evidence and as RFP-language
samples): **NJSBA RFP 2026-02** — Virtual Tutoring Services, optionally Virtual
High-Impact Tutoring and **outcomes-based contracting**, proposals due 2 Jun 2026;
**New Mexico PED RFP 27-92400-00002** — statewide **high-impact tutoring for
reading and math** under **House Bill 2**, with **SY2026-27 the first
implementation year.**

##### 3. The gap inside the rubrics, which is the sellable one

The rubrics are converging on privacy, accessibility and human oversight. What
most of them reportedly **do not** require: that vendors supply **auditable
records of user interactions**, **disclose how the system generates outputs**, or
**demonstrate that the tool was evaluated for bias, accuracy and reliability.**

**That is the differentiator.** A deliverable that ships an interaction audit
log, an output-provenance statement and an evaluation report **exceeds every
rubric described above** and pre-empts the obvious next revision of them. It is
also, almost exactly, the artefact set the EU AI Act profile already forces
(**P13**) — so the same evidence pack sells in both regions, which is the
cross-region arbitrage this KB has been looking for in North America.

##### 4. Market sizing, unchanged in direction and still conflicted in magnitude

This pass surfaced **North America at $951M (2024) → $2,303.2M (2029), 15.9%
CAGR**, with the region holding **~36%** of the global market — alongside global
claims of **$7.52B (2025) → $10.6B (2026) at 40.9% CAGR**. These are not
reconcilable on any consistent definition. **The fifth pass resolved this KB's
position in favour of the lower, more conservative figures and that position
stands**; a 15.9% regional CAGR and a 40.9% global CAGR in the same market is a
scope difference, not a growth difference. Quote the regional figure, state the
definition, and never blend the two in one chart.

#### Tenth pass of 2026-10-06 — the funded pipeline gains two more names, and the integration tier becomes sellable

**The oral-reading project is named, and it is the most on-target funded work this
KB has seen.** Two further Cohort 2 grantees of the **$26M K-12 AI Infrastructure
Program** (Tier 2, search-summary corroborated):

| Grantee | Lead | Project |
|---|---|---|
| **Harvard University** | Ying Xu | **OpenLiteracy: An Open-Source AI Infrastructure Suite for Advancing Speech Foundation Models for Early Word Reading Assessment and Instruction** |
| **University of Maryland, College Park** | Jing Liu | *Enhancing Two Multimodal Classroom Datasets to Advance R&D on Formative Assessment* |

Three of the eight Cohort 2 grantees are now named here (with MMSA & TERC from the
ninth pass); **five remain unnamed.**

**And nothing has shipped — measured, Tier 1, 6 Oct 2026:**

| Probe | Result |
|---|---|
| `OpenLiteracy` | **0 repositories** |
| `tutoring quality evaluation benchmark license:apache-2.0` | **0 repositories** (unchanged) |
| `formative assessment dataset classroom` | **0 repositories** |

**The opportunity, sharpened.** OpenLiteracy targets early word reading
assessment. The whole existing permissive shelf for that capability is **two
repositories** — [qazasd2518995/prosody](https://github.com/qazasd2518995/prosody)
(MIT, 0★, 1 commit, Whisper + Levenshtein alignment) and
[mendezjerick/ReaDirect-V2](https://github.com/mendezjerick/ReaDirect-V2) (no
licence payload). A client who needs oral reading fluency assessment **this**
school year cannot wait for Harvard's suite; the engagement is to build the
harness around `prosody`'s approach now and swap the funded artefacts in when they
land (**P23**, **P25**).

**A named partner with a 238-repository MIT estate.** Learning Equality — Cohort 1
grantee, Kolibri maintainer — holds **238 repositories**, of which this KB had
recorded three. Newly verified MIT: **morango** (15★, peer-to-peer Django DB
replication with certificate-based auth) and **le-utils**. Two others
(`kolibri-design-system`, `kolibri-server`) returned **no licence payload** — so
the diligence is per-repository, not per-organisation. The partnership case is
unchanged and stronger: the organisation funded to produce an openly-licensed
benchmark already ships MIT infrastructure this KB can build on.

**The integration tier is now a sellable line item.** Against the ninth pass's
**39% of districts scoring interoperability in RFP rubrics**, the permissive shelf
is verified and small: `ltijs` (Apache-2.0, 373★, Node), `1EdTech/lti-1-3-php-library`
(Apache-2.0, 124★), `Unicon/tool13demo` and `oxctl/spring-security-lti13`
(Apache-2.0, JVM), `theopenem/OneRoster.NET` (MIT, rostering only, **no
gradebook**). **No Caliper Analytics implementation on a permissive licence.**
🔵 **CORRECTED, twenty-fourth pass of 2026-10-07: the "no Python LTI 1.3 library at all" half of
this sentence was false.** [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) is **MIT**,
head commit **2 d**, PyPI `django-lti` **v0.10.1 (61 d)**. **Caliper remains the contribution
opening with a procurement-scored buyer attached; Python LTI 1.3 no longer is**, except in its
narrow framework-agnostic form. 🔵 **NARROWED, twenty-fifth pass of 2026-10-07 — "none" is now "one alpha".** [`CNIT-Organization/ltitoolkit`](https://github.com/CNIT-Organization/ltitoolkit) (MIT) **vendors `PyLTI1p3`, rebranded** — its README says so — and publishes it as [`ff-ltitoolkit`](https://pypi.org/project/ff-ltitoolkit/) **0.1.0, 2026-06-26 (103 d), one release ever**; head commit **63 d**; **0★**; `Development Status :: 3 - Alpha` with the FastAPI adapter and token minting **unbuilt**; and its `LICENSE` holder is **`Dmitry Viskov`, not its own authors**. **Not "no option", and not a safe dependency either.** Full row in `repos/foundations.md`.


#### Eleventh pass, 2026-10-06 — the benchmarks are American, the licences are not open

| Finding | Value | Instrument |
|---|---|---|
| Share of the global AI-in-education opportunity 2026–2030 | **41.7%** | Tier 2, market-research summary |
| Regional market share | **36%** of global AI-in-education | Tier 2 |
| Institutions with formal AI guidelines | **10%** | Tier 2 |
| US teachers lacking AI training | **71%** | Tier 2 |
| State-level AI requirements for education | **Colorado** and **Texas** have introduced piecemeal requirements; no federal instrument | Tier 2 |

**The opportunity this pass actually adds.** The two leading tutoring-evaluation
benchmarks are North American and European institutional work — **Khan Academy**
(`Khan/tutoring-accuracy-dataset`, 57★) and **ETH Zurich**
(`eth-lre/mathtutorbench`, 43★) — and **neither is OSI-licensed** (Tier 1, payloads
read 2026-10-06). Khan's custom *Evaluation Dataset License* permits internal,
non-commercial evaluation **and explicitly permits evaluating products intended for
commercial use and commercially exploiting the insights gained**, while prohibiting
redistribution, model training and production use.

That is a billable position, and it is specific to this region: **a US district or
university buyer can be shown a measured pedagogical-quality number from Khan
Academy's own dataset, without that dataset ever entering the deliverable.** The
regulatory vacuum here (10% with guidelines, no FDA-equivalent, 41.7% of the money)
means the buyer has no mandated evaluation to point at — so the vendor who arrives
with one sets the standard. The harness is **Inspect** (MIT, 2,945★, UK AISI). The
pattern is **P27**.

**And the data tier is Apache-2.0 and already in the RFP.**
`Ed-Fi-Alliance-OSS/Ed-Fi-ODS` (Apache-2.0, Tier 1) is the reference implementation
of the Ed-Fi K-12 data standard — the student-data model North American district
procurement assumes a vendor already speaks. It was dropped from this KB's live files
by the reset and is reinstated this pass.

#### Twelfth pass, 2026-10-06 — the deadline is a date now, and the permissive estate under the rubric is Apache-2.0

**Sizing read this pass.** North America holds the **largest regional share of the
global AI-in-education market at 36%** — **$3.68B in 2026**, forecast to **$32B by
2030**. Teacher-level adoption: **60% of US K-12 teachers used AI tools during the
2024–25 school year, 32% at least weekly.** Adoption is no longer the question in this
region; governance and procurement are.

**The regulatory surface, counted.** **134 AI-in-education bills introduced across 31
states** in the 2026 legislative session. The clusters that change a deliverable:

| Instrument | What it binds |
|---|---|
| **California AB 1159** | **Prohibits using student data to train AI models.** The sharpest constraint in the region on a tutoring product's data loop — it rules out the default fine-tuning architecture. |
| **Idaho SB 1227** | Requires data-privacy protections for AI tools used in schools. |
| **Oklahoma, Maryland** | Require **human oversight** and bar AI from making high-stakes decisions about students. Trend 16's "human judgment is final" rule, still converging. |
| **Georgia, Mississippi** | Computer-science credit requirements **that include AI instruction**, phased in from the late 2020s. Curriculum-mandate demand (trend 13). |
| 🆕 **Ohio** | **Every public school district must have a written AI policy by a July 2026 deadline.** A date, state-wide, already passed at the time of this pass. |
| 🆕 **North Carolina** | Lawmakers **defended a $10M earmark** funding **Khanmigo** for participating districts state-wide. A funded, named, proprietary deployment. |

🆕 **Ohio and North Carolina are two different engagement shapes, and both are live.**
Ohio is a **compliance artefact** at district scale: ~600 districts needing a written
policy, an inventory of what AI is actually running, and a human-oversight procedure
that matches Oklahoma/Maryland-style rules. North Carolina is the opposite — a **funded
proprietary tutor already deployed**, which creates demand for the work around it:
integration into the district's SIS, evidence that it conforms, and an exit path that is
not a second procurement.

🆕 **And the permissive estate sitting under the procurement rubric is Apache-2.0.** This
pass recovered and verified it (details in `repos/foundations.md`):

- **The Ed-Fi stack** — [Ed-Fi-Data-Standard](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard)
  (Apache-2.0, branch `v6.2.0`), [edfi-oneroster](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster)
  (Apache-2.0), [Ed-Fi-Clever-Integration](https://github.com/Ed-Fi-Exchange-OSS/Ed-Fi-Clever-Integration)
  (Apache-2.0). The standard US K-12 interoperability rubrics name, plus the bridge to
  **Clever**, the rostering provider most districts actually run. ⚠️ The **Ed-Fi MCP
  side-car is dead** — agent access over MCP is a build.
- **The xAPI chain** — profile, pipe, store and **conformance test suite**, all MIT or
  Apache-2.0, and authored by **ADL**, a US Department of Defense initiative. A
  conformance run is procurement *evidence*, not an assertion.
- **[datakind/student-success-tool](https://github.com/datakind/student-success-tool)**
  (MIT, branch `develop`) — predictive advising with explicit bias-reduction and an
  advisor in the loop, **Google.org**-funded, with **John Jay College** reporting a 32%
  rise in senior graduation over two years. The permissive answer to a retention brief,
  with an outcome number attached.
- **[openedx/XBlock](https://github.com/openedx/XBlock)** (Apache-2.0, 470★) — the
  plugin seam that lets a district-specific component be built and kept while the Open edX
  platform stays AGPL.
- ⚠️ **[ucfopen/UDOIT](https://github.com/ucfopen/UDOIT)** (GPL-3.0) — UCF's WCAG
  scanner for Canvas. Accessibility is a hard US public-education procurement requirement
  and this is the installed-base tool; it is copyleft, so pair it with `canvas-mcp`'s MIT
  scanner when the deliverable must be permissive.

**Also recorded:** students from **all 50 states** produced a **national framework for AI
in America's schools** at America's Youth AI Festival in July 2026, proposing protections
for authentic learning, student privacy, fairness, human judgment and relationships. Not
binding — and a useful legitimacy artefact to cite in a district-facing proposal, because
it is the student constituency asking for the same human-oversight rule the state statutes
impose.

**The North America opportunity, stated as work:** (1) district **AI-policy and
inventory** packages against Ohio-style deadlines; (2) **Ed-Fi + OneRoster + xAPI
conformance** as a scored-procurement evidence pack, buildable entirely on Apache-2.0;
(3) **retention/advising** on the DataKind base, which already carries a published
outcome; (4) **integration and exit-path work around funded proprietary tutors** such as
the North Carolina Khanmigo deployment. ⚠️ Architect (1)–(3) so **no student data trains a
model** — California AB 1159 makes that a design constraint, not a policy preference.

#### Thirteenth pass, 2026-10-06 — re-verified, nothing new

🔵 **Every North America figure and instrument this KB carries was re-run this pass against
the search index and came back unchanged.** Market share **36%**, **$3.68B in 2026** rising
to **$32B by 2030**; **134 AI-in-education bills across 31 states**; **Ohio** the first
state to mandate written district AI policy (**July 2026**); **California AB 1159** barring
student data from model training; **North Carolina**'s **$10M** Khanmigo earmark; the
50-state student-authored national framework; the split between states building
procurement pipelines and states imposing moratoria.

⚠️ **No new North America opportunity is recorded this pass, and that is the finding.**
The regional intelligence here is **saturated at the level this channel can measure**. The
pass spent its probes on supply (new repositories, new languages, new forges) rather than
on demand, and the demand picture did not move in a day. **P24** (procurement-rubric-ready
delivery) and **P25** (the interoperability tier) remain the standing North America plays,
unchanged.

🟢 **One supply-side item does land here, indirectly.** The avatar/animated-pedagogical-agent
research front is **predominantly North American and Chinese academic work** (the VTutor
cluster, `arXiv:2502.04103` / `2505.06676` / `2505.07736`), and it has produced **no
obtainable permissive implementation** — the named `VTutorTools` organisation exists with
**zero public repositories**. The only shippable avatar capability on this shelf is
**Moroccan** (`open-tutor-ai-CE`, BSD-3-Clause). For a North America engagement that wants
an animated tutor, the component comes from EMEA and the research citations come from home.


#### Fourteenth-pass additions, 2026-10-06 — the integration tier is measured, and the K-12 administrative one is empty

**Market figures read this pass.** North America **$951M (2024) → $2,303.2M (2029), CAGR
15.9%**, and **36%** of the global AI-in-education market — the largest regional share, on
the slowest regional growth rate in this file. Segment splits, global but
North-America-weighted: **K-12 45.62%** of adoption, **STEM 34.78%** of revenue, **cloud
delivery 71.22%** (2024), with language learning the fastest-growing subject.

🔵 **The opportunity this pass measured is a supply vacuum, not a demand claim.** Counting
open-source integration repositories per platform (GitHub REST `total_count`, one platform
name per query, licences read from payloads — full table in `verticals/solutions.md`):

| Platform | Open-source integration repos | Best permissive server |
|---|---|---|
| Canvas LMS | 117 | MIT, 278★ |
| Brightspace / D2L (Canadian vendor) | 23 🆕 | MIT, 57★, on npm |
| **Google Classroom** | **17** | MIT, **6★** |
| Blackboard Learn | 5 | MIT, 2★ |
| 🔴 **PowerSchool** (dominant US K-12 SIS) | **0** | **none** |

**K-12 is 45.62% of adoption and its two defining platforms have an integration tier of 17
repositories and zero repositories.** Higher education — Canvas, Brightspace — is served:
adopt there, and sell configuration, governance and pedagogy rather than connectors. The
build is K-12 administration, and the reason it is empty is the reason it is defensible: a
hobbyist cannot obtain credentials to a district student information system, and an
enterprise integrator can.

⚠️ **The regulated surface and the empty tier are the same tier.** What a Classroom or
PowerSchool integration touches is student records, guardians, enrolment and
**accommodations** — and accommodations is a legal obligation, not a feature. The one asset
found this pass that even names it is `GarphenGate/moltline-mcp` (MIT, 8 skills across
curriculum, classroom, accommodations and exam prep). Price the governance artefacts into
the statement of work from day one (P24, P25).

🔵 **The school-data layer already exists — as hosted endpoints nobody can audit.** The MCP
Registry census this pass found a dense US cluster with **no source repositories**:
`ai.edusignal/districts` (K-12 districts, all 50 states), `dev.districtapi/districtapi-mcp`
(ungranted repo), `co.schoolscope/mcp` and `ai.sacs/sacs-mcp` (California school finance and
CDE data), `com.olyport/nces-education` and `com.olyport/college-scorecard` (federal NCES and
College Scorecard). **The open, inside-the-boundary equivalent of that cluster is an
engagement**, and the public data underneath it is already free.

**Regulatory read, unchanged in direction and worth restating with this pass's framing:**
there is no FDA-equivalent for educational technology, and adoption is decided school by
school, district by district, university by university, with minimal external oversight —
while the EU classifies the same systems as high-risk. That asymmetry is why the
procurement rubric, not the regulator, remains the specification in this region (trend 26),
and why an artefact pack that clears the EU clears a US district by construction.


#### Twentieth pass of 2026-10-06 — the transition-provision channel: North America is this pass's declared gap

⚠️ **There is no transition article to read in this region, because there is no binding federal
high-risk AI statute to carry one.** That is the finding, and it is written down rather than left as
an empty section: the channel that produced dated extensions in EMEA, APAC and LATAM returned
**nothing** here.

🔵 **What exists instead, re-read this pass.** The region holds **36% of the global AI-in-education
market, $3.68B in 2026**, rising toward **$32B by 2030**. **134 bills across 31 states** in the 2026
session; **60% of US K-12 teachers** used AI tools in 2024-25 and **32% weekly**; the **K-12 AI
Literacy and Readiness Act of 2026 (H.R. 8747)** advanced at a **21 July** markup; **30+ states**
have AI guidance and the 2026 movement is its evolution rather than its creation.

🔴 **State duties attach at enactment, with no transition regime** — California **AB 1159** (student
data may not be used to train models), Idaho **SB 1227** (data-privacy protections for AI tools in
schools), Oklahoma and Maryland (human oversight, no high-stakes automated decisions about students).
**There is nothing to grandfather into.**

🟢 **The one real date in the region is the one already recorded: the DOJ ADA Title II interim final
rule — 2027-04-26** for public entities serving ≥50,000 and **2028-04-26** below that. 🔵 **So North
America's version of `P-TRANSITION-EVIDENCE` is the accessibility half plus the procurement-rubric
artefact pack (P24)**, not a conformity extension — and the evidence tier in
`repos/foundations.md` is what both consume. ⚠️ **Do not pitch a "transition plan" here.** The buyer
has no extension to protect; what they have is a rubric to score against and a remediation backlog
with a date.

#### Twenty-second pass of 2026-10-06 — the zero-egress classroom, and why state law is now the pitch

**The 2026 legislative picture, as the trackers describe it:** more than **1,500 AI-related bills**
were introduced across the states this year, and roughly **100 state bills** bear directly on
students' use of AI (PIE Network count). Four instruments decide architecture rather than policy:

| Instrument | What it obliges | Why it changes the build |
|---|---|---|
| **Ohio** — first state to require **every** K-12 district to adopt a formal AI-use policy (state model or locally aligned) **by 2026-07-01** | a policy per district | the deadline has passed; districts now need **evidence of conformance**, not advice |
| **Maryland** — *Artificial Intelligence Ready Schools Act* | state guidance, aligned district policies, a named **AI coordinator** per district | a named owner per district is a named buyer per district |
| **California** — statewide guidance of **January 2026** | raises expectations for AI integration in public schools | the largest single K-12 market has a written bar to clear |
| **California A.B. 1159** (proposed) | would **bar student data from training AI models** unless the use directly benefits the school | 🔴 **this is an architecture constraint, not a policy line.** A SaaS tutor cannot prove it; a self-hosted stack proves it by construction |
| **Oregon S.B. 1546** (enacted) | design duties protecting minors, incl. **reducing compulsive use** when the user is known or presumed to be a child | engagement-maximising UX becomes a legal risk in a learning product |

🟢 **The opportunity this pass actually adds: a classroom stack where no student artefact leaves the
institution.** [`travo-cr/travo`](https://gitlab.com/travo-cr/travo) (**BSD-3-Clause**, active
2026-10-06) is a **Université Paris-Saclay × Université du Québec à Montréal** collaboration — so it
is already a North American production tool — and it runs against **any** GitLab instance, including
one the district or university hosts itself, with **nbgrader** (BSD-3-Clause, 1.4k★) doing automatic
and manual notebook grading. Add [`cjaikaeo/elabsheet`](https://gitlab.com/cjaikaeo/elabsheet)
(**BSD-2-Clause**) for non-notebook exercises and nothing in the assessment loop is a third-party
service.

⚠️ **Sell it as the evidence, not the software.** The deliverable a district's counsel buys is a
one-page data-flow statement saying *student submissions never leave your tenancy*, which this stack
can make true in week one. Full wiring: **`P-ONPREM-CLASSROOM`** in `compose/patterns.md`.
### EMEA

- **The EU AI Act is the whole conversation.** AI used in education access and
  assessment — admissions, student evaluation, exam scoring — is classified
  **high-risk** under Annex III.
- **Timeline matters and buys time:** high-risk obligations for stand-alone
  systems are **deferred to 2 December 2027**; high-risk AI embedded in
  already-regulated products to **2 August 2028**. The European AI Office
  implements the general-purpose AI provisions. In 2026 the EU agreed amendments
  clarifying overlap with machinery rules.
- **Deployment reality:** schools are running parent-facing and admin chatbots on
  commercial APIs, but districts with strict data-residency requirements
  **self-host open-weight models** (Llama, Mistral) instead.
- **Opportunity:** a sovereign, high-risk-ready stack delivered well before the
  2027 deadline — on-prem Ollama/vLLM, typed outputs, checkpointed audit trails,
  explainable mastery estimation, and a documented human-oversight gate. The
  deferral is the window: a system designed for Annex III now avoids a forced
  rebuild in 2027. Germany/Austria/Switzerland additionally skew toward ILIAS and
  SCORM compliance training.

**New this pass (2026-10-06):**

- **Sized at last: the European AI-in-education market is $2.64B in 2026.** That
  is the regional number the earlier passes were missing — roughly 25% of the
  $10.6B global market, against North America's 36% / $3.68B.
- **The leaders are small, digitally mature states, not the large economies:**
  **Finland, Estonia and the Netherlands** lead European K-12 AI integration. For
  a reference deployment, these are the markets where the institutional appetite
  and the digital baseline already exist. Treat them as the proof-point tier.
- **Timeline precision matters.** The AI Act's **general application date is
  2 August 2026** — already passed. What is deferred is the *high-risk* obligation
  set: stand-alone Annex III systems to **2 December 2027**, high-risk AI embedded
  in already-regulated products to **2 August 2028**. So the general-purpose and
  transparency regime is live now, while the education-specific high-risk regime
  is the design window. Do not tell a client "the AI Act does not apply yet."
- **Most European institutions are in pilot-and-pre-compliance mode**, deploying
  AI in administration and teacher support first, keeping humans in the loop on
  consequential decisions, documenting deployments, and disclosing to students and
  parents what is AI-decided versus human-decided. That sequence — admin first,
  assessment last — is the lowest-friction entry path in the region.
- **Africa enters this KB.** Earlier passes treated EMEA as Europe. South Africa's
  **Draft National Artificial Intelligence Policy (2026)** is in progress, and
  **GenAITEd Ghana** — a context-aware, curriculum-aligned conversational AI agent
  for *teacher education* — is a published, first-of-its-kind African education
  agent (research, not a product shelf). Africa is a genuine greenfield in the
  EMEA bucket: policy forming, almost no deployed open source education AI, and
  teacher capability the binding constraint.

**New in the third pass (2026-10-06):**

- **NARROWED (fourth pass, 2026-10-06): Africa now has a code shelf, and it is
  ministry-engaged.** Every earlier pass recorded "no deployed open source African
  education AI shelf to recommend from." That is no longer accurate.
  [`AI-for-Education`](https://github.com/AI-for-Education) is a GitHub
  organisation whose mission is to democratise AI in education across **low- and
  middle-income countries**, and — unusually for anything on this shelf — its work
  is **placed in named countries**: a lesson-plan parser built for **Sierra
  Leone's MBSSE** (Ministry of Basic and Senior Secondary Education) and
  **Luganda linguistic benchmarks** for **Uganda**. Five of its six repositories
  are **MIT by payload** (`pedagogy-benchmark` 12★, `fabdata-llm` 9★,
  `edu-qurating` 3★, `fabdata-parsedoc` 2★, `voice-ai-evaluation-framework` 1★);
  the sixth is unlicensed. See `repos/foundations.md`.
  **Size it honestly: 1–12★ is research-grade code, not a product shelf.** The
  finding is not "Africa is served" — it is that the entry point is **specific,
  permissive and already connected to a ministry**, which is a far better place to
  start a conversation than greenfield. It also supplies the two capabilities the
  continent's constraints actually demand and that this KB had no entry for
  anywhere: **voice-interface evaluation** (where literacy and device cost bind)
  and **local-language benchmarking** (Luganda). Teacher capability remains the
  binding constraint, unchanged.
- **Europe now has a growth curve, not just a 2026 number: $2.64B in 2026 →
  $8.0B by 2030 at 31.9% CAGR.** Note what that means — Europe is growing
  *materially slower* than the global 41.5% CAGR, so its 25% share of the market
  shrinks over the forecast period. The AI Act is both the demand driver and the
  brake, and a regional plan should assume Europe is the **compliance-depth**
  market rather than the growth market.
- **Middle East & Africa is sized for the first time in this KB: $0.56B in 2026 →
  $1.6B by 2030 at 34.3% CAGR** — small in absolute terms, and growing faster than
  Europe. Africa stops being a declared gap and becomes a sized opportunity.
- **Two sources disagree about MEA by two orders of magnitude, and the honest
  answer is a range.** Against the $0.56B regional figure, MarketsandMarkets sizes
  the **UAE** AI-in-education market at **$7.4M in 2024 → $21M by 2029 (19.1%
  CAGR)** and "Rest of Middle East" at 18.9% CAGR. A region cannot be $560M while
  its most advanced country is $7.4M, so the two are not reconcilable: they are
  almost certainly measuring different scopes (platform spend vs total AI-adjacent
  education technology). **Quote MEA as a range and name the uncertainty** rather
  than picking the flattering number — a client who checks will find the other one.
- **MEA has AI strategies, not AI statutes.** Saudi Arabia, the UAE, Egypt,
  Nigeria, Kenya, Rwanda, Morocco and South Africa all have published national AI
  strategies, and **none has an AI-specific binding statute yet.** That is the
  mirror image of the EU engagement: in Europe you sell conformity against a law
  that exists; in MEA you sell governance design *before* the law arrives, which is
  a shorter sales cycle and a weaker procurement trigger. Price and sequence
  accordingly.
- **The UAE has mandated AI in every public school, and this is the single most
  concrete demand signal in the region.** Approved by **Cabinet decision in May
  2025**, mandatory AI runs from **Kindergarten (age 4) to Grade 12** starting in
  the **2025–26 academic year**. The design details are the commercially useful
  part:
  - it is **woven into an existing subject** (Computing, Creative Design and
    Innovation) **without extending school hours** — so the deliverable is
    integrated curriculum material, not a new timetable slot;
  - it is taught by **specially trained teachers** — teacher enablement is funded
    and mandatory, not discretionary;
  - it is organised around **seven areas**: foundational concepts; data and
    algorithms; software use; **ethical awareness**; real-world applications;
    innovation and project design; and **policies and community engagement**.
  Two of the seven areas are governance and civics rather than technique, which
  means the content pipeline has to produce age-appropriate *ethics and policy*
  material, not only technical exercises. See the new pattern P9 in
  `compose/patterns.md`.


#### Fifth pass, 2026-10-06 — the compliance clock moved 16 months, and the near-term deliverable changed with it

**This is the most consequential single finding of this pass, and it rewrites the
EMEA engagement calendar.**

**Regulation (EU) 2026/1744** — the *Digital Omnibus on AI* — amends the AI Act.
Legislative trail, corroborated across multiple independent legal and vendor
analyses: European Parliament approval **16 June 2026**, Council final adoption
**29 June 2026**, signature **8 July 2026**, published in the Official Journal
**24 July 2026**, **entered into force 27 July 2026**. CELEX identifier
**32026R1744**.

| Obligation | Was | Now |
|---|---|---|
| **Annex III stand-alone high-risk** — including **education**: admission and access, evaluation of learning outcomes, student level placement, and **exam or behaviour monitoring** | 2 August 2026 | **2 December 2027** (+16 months) |
| **Annex I embedded high-risk** (AI inside regulated products) | 2 August 2027 | **2 August 2028** (+12 months) |
| **Article 50 transparency**, including the **watermarking / synthetic-content marking** deadline | 2 December 2026 | **unchanged — 2 December 2026** |

**Read the third row again.** The heavy Annex III work — technical
documentation, conformity assessment, CE marking, EU-database registration —
moved out 16 months. The **transparency obligations did not move at all**, and
the watermarking deadline is **2 December 2026**. So in EMEA, as of this writing:

- The deliverable that is **weeks away** is Article 50: disclosure that a learner
  is interacting with an AI system, and marking of AI-generated content. For an
  education client that is **labelling every generated lesson, item and feedback
  artefact**, and disclosing the tutor. It is small, concrete, and nearly
  everyone has deferred it along with the Annex III work, because the two were
  discussed as one deadline.
- The deliverable that is **14 months away** is Annex III conformity — and the
  deferral is explicitly **not a compliance holiday**: the obligation to
  *classify* systems against Annex III and Annex I, and to begin compliance
  planning, is immediate.

**How to sell this.** The engagement shape is now two-phase and the first phase
is fundable this quarter: **(1) classify and label by December 2026; (2) build the
Annex III conformity evidence by December 2027.** A client who believes the
August 2026 deadline passed and nothing happened is in the worst position —
unlabelled and unclassified — and that is a very easy conversation.

**Caveat on sourcing, stated because this claim is load-bearing.** The primary
texts (EUR-Lex, the Commission's own notice) are **unreachable from this
environment** — the egress proxy denies both. The regulation number, OJ date,
entry-into-force date and all three deadlines above are corroborated across
several independent law-firm and compliance-vendor analyses, and the CELEX id is
given so a reader can verify in one step. **Verify against EUR-Lex before it goes
in a client deliverable.**

**EMEA market sizing, added this pass:** **$2.64B in 2026 → $8.0B by 2030, 31.9%
CAGR**, with **Finland, Estonia and the Netherlands** named as the K-12 AI
integration leaders. The UK's £4M investment in AI lesson-planning and marking
tools is small in absolute terms and useful as a procurement precedent.

**And the compliance toolkit is no longer a gap.** See `repos/foundations.md`:
[AbdelStark/eu-ai-act-toolkit](https://github.com/AbdelStark/eu-ai-act-toolkit)
is **MIT** and already carries the risk-tier decision tree, 61 conformity
checklist items and 8 document templates — with **no education content**. The
Annex III point 3 profile is the billable piece and it is days of work, not
months. Pattern **P13**.



#### Sixth pass, 2026-10-06 — the voice and language layer

**The regulatory clock is the demand driver, confirmed again.** The **EU AI Act
takes full effect in August 2026**, with education AI classified **high-risk** and
a four-tier risk structure (unacceptable / high / limited / minimal). The
**Council of Europe** convened its **2nd working conference on the regulatory
dimensions of AI in education in October 2026**, so the standards conversation is
live rather than settled. The **UK's AI Adoption Summit committed £200m+** with
Cisco, IBM, BT and Rolls-Royce as delivery partners. **94% of organisations** are
at least somewhat likely to invest in AI-specific training in 2026 — while **38%
of EMEA organisations have yet to begin piloting** anything. That split is the
addressable market: funded intent, no implementation.

**What this pass opens here:**

- **Africa has a permissive language layer for the first time.**
  [SunbirdAI/salt](https://github.com/SunbirdAI/salt) (**Apache-2.0**) ships
  translation, ASR and **studio-recorded TTS by professional voice actors** across
  **Luganda, Swahili, Ateso, Lugbara, Acholi and Runyankole**, and
  [masakhane-mt](https://github.com/masakhane-io/masakhane-mt) (**MIT**) carries
  continental MT from a 30-country community. The fourth pass had to **reject**
  this KB's only Uganda-placed asset for having no licence; **the Apache-2.0
  sibling covers six languages**. Mother-tongue delivery in East Africa is now a
  shelf capability.
- **Two of the layer's maintainers are in EMEA, which matters for sovereignty
  conversations.** The live Coqui TTS fork is maintained at the **Idiap Research
  Institute (Switzerland)**; **Tucano 2** is developed under the **University of
  Bonn** Polyglot initiative (Apache-2.0). A client who must point at a European
  maintainer for a core dependency can.
- **Voice plus sovereignty is now one answer, not two.** `sherpa-onnx`
  (Apache-2.0) runs STT, TTS, diarization and VAD with **no Internet connection**,
  so spoken assessment can be offered with data residency guaranteed by
  architecture rather than by contract — the P4 posture, extended to voice.
- **Watch the Piper licence trap in public-sector bids.** The permissive Piper is
  **archived**; the maintained one is **GPL-3.0**. A procurement that forbids
  copyleft and a technical spec that names Piper are in silent conflict.

#### Seventh pass of 2026-10-06 — MEA's constraint is licensing hygiene, not capability

This KB has recorded MEA as its thinnest region through four passes. The seventh
pass searched **in Arabic** — a channel never used before — and the result
sharpens the diagnosis rather than changing the size.

[781991937/TOFAN-AI-2026](https://github.com/781991937/TOFAN-AI-2026) is the most
substantial Arabic-language education agent found in seven passes: ingests lesson
files, extracts and analyses content, generates summaries and interactive tests;
FastAPI backend, installable PWA front end. **It has no `LICENSE` payload.**

Set against the rest of the MEA shelf:

| Asset | State |
|---|---|
| `AI-for-Education` org (MIT — Sierra Leone MBSSE lesson-plan parser, Uganda) | Real, ministry-engaged, and **1–12★ research-grade code** |
| `AI-for-Education/Luganda-linguistic-benchmarks` | **Unlicensed** |
| [`SunbirdAI/salt`](https://github.com/SunbirdAI/salt) (Apache-2.0) | Real and usable — but a **corpus**, not a product |
| `781991937/TOFAN-AI-2026` (Arabic) | Real, well-shaped, **unlicensed** |

**MEA is the only region in this KB with zero shippable permissive education
assets, and the binding constraint is not interest, funding or capability — it is
licensing hygiene.** Two of the four rows above are good work with no grant
attached.

**Why this is good news commercially.** A capability gap takes a year to close
and a funding gap is not Globant's to close. **A licensing gap closes with three
`LICENSE` files**, and asking for one is a free, high-visibility upstream
contribution that creates a relationship with the maintainer — in two cases, a
maintainer already working with an education ministry. This is now the cheapest
high-value upstream action identified anywhere in this KB, ahead of the
pedagogy-evaluation asks from the fourth and fifth passes.

**Market context for sizing:** MEA is **$0.56B in 2026 growing at 34.3% CAGR to
$1.6B by 2030** — the fastest-growing and smallest regional market here — with
the **UAE** one of only two jurisdictions worldwide running a compulsory national
AI curriculum, and Egypt, Morocco and Jordan building capacity through
public–private partnerships. The demand is funded and the open supply is
unlicensed, which is an unusually favourable asymmetry for a services business.


#### Eighth pass, 2026-10-06 — no new EMEA finding; the sweep returned enterprise-AI material, not education

The mandated EMEA sweep (`AI education EMEA 2026 adoption regulation players`)
returned **general enterprise AI-adoption commentary** — CompTIA's EMEA IT
outlook, Workday's adoption study, AI-fluency training statistics — and **no
education-specific regulatory or supply development** beyond what this file
already records for the EU AI Act and Annex III point 3.

**The one education-specific signal is an event, not a rule:** the **Council of
Europe** is convening its **second working conference on the regulatory
dimensions of AI in education** in October. This file already records the
Council of Europe's role; the conference is worth tracking as the venue where
sub-AI-Act education guidance for the 46 member states is likely to be shaped,
and it is a legitimate forum for Globant to monitor rather than a market change.

**Explicit gap:** this KB still has **no EMEA-origin permissive education agent
added in the last three passes**, and the eighth pass did not change that. The
EMEA supply picture remains what the earlier passes measured — strong platform
estate, mostly copyleft (Moodle, Chamilo, ILIAS), with ECL-2.0 and LGPL-3.0
as the permissive-adjacent exceptions.

#### Ninth pass, 2026-10-06 — the UK ministry publishes its national estate under MIT

**Channel new to this KB: the education-ministry engineering organisation.** Nine
passes swept ministries *by name* in search of policy; none had looked at a
ministry's own GitHub org for code.

**`DFE-Digital`, the UK Department for Education, runs live national education
services in the open under MIT.** Payload-verified this pass (full table and star
counts in `repos/foundations.md`): `apply-for-teacher-training` (38★),
`teaching-vacancies` (27★), `get-into-teaching-app` (25★),
`publish-teacher-training` (12★), `register-trainee-teachers` (12★),
`get-information-about-schools` — GIAS, the national schools register (9★), and
`education-benchmarking-and-insights` (5★).

**Why this changes the EMEA picture.** This KB had characterised EMEA through two
things: the **EU AI Act compliance clock** (trend 17, and the sixteen-month move
recorded in the fifth pass) and a **licensing-hygiene problem** in MEA (seventh
pass). Neither described a *supply* of permissive, production, government-grade
education software. That supply exists, and a state maintains it.

**The asymmetry is the opening.** The DfE's **administrative** tier is production
MIT. Its **AI** tier is five prototypes at **0–1★ with no licence payload** —
including `rsd-ai-libs`, described as *".NET library for building and evaluating
Azure AI Foundry agents with guardrails, Azure AI Search, and **MCP server
support**."* A national education ministry independently arrived at this KB's MCP
side-car architecture and left it unlicensed at zero stars.

So the EMEA public-sector proposition is not *"you need a platform"* — they built
one — but: **"your administrative estate is a licensed national asset and your AI
estate is unlicensed prototypes; we build the second on top of the first, under
the licence you already publish."** That is a concrete, evidenced, ministry-scale
entry point, and it is reusable as a *precedent* across every EMEA education
ministry that asks whether open source is credible at national scale.

**Also recorded, because the regional sweep returned it and it is not education:**
the mandated EMEA query returned **enterprise** AI-adoption material — 94% of
organisations likely to invest in AI training in 2026, 38% of EMEA organisations
not yet piloting, 60% reporting siloed data, the UK's **£200m+** AI Adoption
Summit commitment, and a Council of Europe working conference on the regulatory
dimensions of AI in education (October). The **AI-skills funding** signal is real
and relevant to enablement engagements (**P6**); the rest is enterprise
cross-industry material in an education query. **Second consecutive pass in which
this region's general query failed to return education-specific findings** — the
ministry-org channel is what worked, and it should be the EMEA default from here.

#### Tenth pass of 2026-10-06 — EMEA is writing the evaluation rule that North America is funding the artefact for

The generalist regional query failed for the **third consecutive pass**, returning
enterprise AI-governance and corporate-training material (94% of organisations
likely to invest in AI training; 38% of EMEA organisations not yet piloting; 60%
reporting siloed data; UK AI Adoption Summit with £200m+ committed to AI
adoption). Useful context, **not education findings.** The generalist query is
retired for this region; what worked in the ninth pass was a named institution,
and what worked this pass is the same.

**The channel: the Council of Europe education directorate** — a treaty body, not
a search term. **Tier 2, corroborated across two independent summaries.**

The Council of Europe has established a **Committee of Experts on AI and
Education (EDU IA)** and introduced the **Council of Europe Compass for AI and
Education**, presented at a third working conference, *"Ensuring quality education
in the AI era."* The **Committee of Ministers adopted a text in Munich** placing
education at the centre of Europe's response to AI, implementing **Article 20 of
the Framework Convention on Artificial Intelligence, Human Rights, Democracy and
the Rule of Law.**

The **2026–2027 work programme** names four deliverables:

| Deliverable | Why it is a market event |
|---|---|
| A proposal for a **legal instrument to regulate the use of AI systems in education** | A sector-specific instrument on top of the EU AI Act's horizontal duties — a second compliance surface for the same deployment |
| A **European Reference Framework for the Evaluation of Educational Technologies** | **The EMEA twin of the $26M North American benchmark programme** — same void, different instrument |
| A **Policy Toolbox** on teaching and learning about AI | Ministry and institutional advisory demand |
| **Draft guidelines on the use of education data and analytics** | Lands directly on the learning-analytics layer, where this KB found **no permissive Caliper implementation** |

**The read, and it is the most useful cross-region statement in this file.**
North America is **buying the artefact** — $26M, twelve projects, an Apache-2.0
floor, benchmarks and datasets. EMEA is **writing the rule** — a reference
framework for evaluating educational technology, and a proposed legal instrument
behind it. A client deploying in both regions faces one gap expressed two ways,
and the EMEA expression is the harder one to retrofit, because conformance
evidence cannot be generated after the fact. **An evaluation harness built now
(P23) serves the US benchmark swap-in and the European conformance file at the
same time**, and it gives the EU AI Act profile work (**P13**) a named successor
instrument to track rather than a horizontal regulation alone.

**The competitive fact for the same buyers.** OpenAI's **Education for Countries**
programme (Tier 2; launched at Davos 2026) is working directly with ministries of
education, and its named EMEA participants are **Estonia, Greece, Italy (CRUI, the
rectors' conference), Slovakia, the UAE and Jordan.** Six EMEA national or
sector-wide bodies are being onboarded to a single proprietary vendor at the
ministry tier — in the region that is simultaneously drafting a legal instrument
on AI in education and a framework for evaluating it. **Sovereignty, auditability
and data residency are not abstract selling points here; they are the subject of
the instrument being drafted.**


#### Eleventh pass, 2026-10-06 — EMEA is not only writing the rule, it is shipping the tooling

The tenth pass framed the region as the one *"writing the rule"* while North America
*"buys the artefact."* **That framing was incomplete and the correction is
commercially significant.**

| Asset | Origin | Licence (Tier 1, payload read 2026-10-06) | Scale |
|---|---|---|---|
| [UKGovernmentBEIS/inspect_ai](https://github.com/UKGovernmentBEIS/inspect_ai) | **UK AI Security Institute** (`aisi.gov.uk`) | **MIT** | **2,945★**, 779 forks, pushed 2026-10-06 |
| [eth-lre/mathtutorbench](https://github.com/eth-lre/mathtutorbench) | **ETH Zurich**, Learning & Reasoning group, EMNLP 2025 Oral | 🔴 **no payload**; README claims **CC BY 4.0** *and* **CC BY-SA 4.0** | 43★ |
| [openfun/richie](https://github.com/openfun/richie) | **France Université Numérique** | **MIT** | 316★ |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | Switzerland | **Apache-2.0** | 446★, pushed 2026-10-06 |
| [digillab-lmu/smart-rag](https://github.com/digillab-lmu/smart-rag) | **LMU Munich** | ⚠️ **`NOASSERTION`** — unresolved | 2★ |

**A European government body maintains the most-starred MIT evaluation framework on
these shelves**, and two European universities publish the pedagogy benchmarks — one
of them without a usable grant. Combined with the Council of Europe's **European
Reference Framework for the Evaluation of Educational Technologies** (tenth pass,
Tier 2) and the **EU AI Act taking full effect in August 2026 with education AI
classified high-risk** (Tier 2, re-corroborated this pass), the region now supplies
*all three* layers of the conformance story: the rule, the reference framework, and
an MIT-licensed harness to run it in.

**Market context re-corroborated this pass (Tier 2):** AI uptake rose ~30% year on
year, with roughly five businesses per minute adopting AI, and **94% of organisations
at least somewhat likely to invest in AI-specific training in 2026**. Among
enterprises that considered and declined AI in 2025, the barriers were **lack of
expertise (70.9%)**, **uncertainty about legal consequences (52.5%)** and **data
protection concerns (48.8%)** — the second and third of which are precisely what an
Inspect-based conformance harness is for. Structural brakes named: inconsistent
implementation across member states, a shortage of mainstream digital skills, and
limited late-stage capital.

**The opportunity, stated as a sentence:** in EMEA the deliverable is not a tutor, it
is a **tutor plus its conformance evidence**, and the evidence pack can be built from
EMEA's own MIT-licensed tooling. That is an easier sale to a ministry than any
import.

#### Twelfth pass, 2026-10-06 — the rule is in force, and the public sector's own code has no grant

**Sizing read this pass.** The European AI-in-education market is **$2.64B in 2026**,
forecast to **$8.0B by 2030** at a **31.9% CAGR** — roughly **72% of North America's
current size and growing more slowly**, which is the ratio to carry into a regional
investment case. **Finland, Estonia and the Netherlands** lead K-12 AI integration. The
**UK government invested £4M** in AI tools for lesson planning and homework marking.

**The compliance clock has struck.** From **2 August 2026 the AI Office and national
authorities began enforcing** the EU AI Act. Education remains squarely in scope: AI used
for **access and assessment** — admission decisions, student evaluation, exam scoring —
is **high-risk**, requiring risk management, data governance, human oversight,
transparency and conformity assessment **before deployment**. Phased implementation runs
through 2026–2027, so most institutions are in **pilot-and-pre-compliance** rather than
full enforcement. That gap *is* the engagement window, and it is closing on a published
schedule.

🆕 **The finding of this pass is about EMEA's public-sector supply, and it is not
flattering.** Of the public-sector and standards-body repositories probed from this
repository's archive, **four of five carry no licence grant at all**, measured against
30+ filename variants on the real default branch:

| Repository | Body | Licence state |
|---|---|---|
| [european-commission-empl/European-Learning-Model](https://github.com/european-commission-empl/European-Learning-Model) | **European Commission**, DG EMPL | **EUPL-1.2** — and declared only by a **README badge linking to a third party's repository**; the grant itself sits in a root file named `license` (lowercase, no extension). |
| `european-commission-empl/european-digital-credentials` | **European Commission**, DG EMPL | 🔴 **Ungranted.** |
| `FWU-DE/schulfach-ontologie`, `FWU-DE/schulart-ontologie` | **FWU** — the German federal states' media institute | 🔴 **Ungranted.** School-subject and school-type ontologies: exactly the vocabulary a German curriculum alignment needs. |
| `dini-ag-kim/school-curriculum-pg` | **DINI-AG-KIM**, German metadata group | 🔴 **Ungranted.** |

**Two consequences, and they point in opposite directions.**

First, **the EU's own learning-data model is EUPL-1.2** — OSI-approved but **reciprocal**,
operating through a compatibility list rather than a permissive grant. A deliverable built
on the European Learning Model is a **published deliverable**. That is priceable for a
public client and must not be quoted as permissive.

Second, **the ungranted repositories are an unusually cheap unblock.** A ministry or
standards body can attach a licence in **one commit**; the reason these have none is
almost always that nobody asked. 🆕 **"Can you put a licence on this?" belongs in the
first fortnight of any EMEA public-sector engagement** — it converts an unusable
vocabulary into a reusable one at essentially zero cost, and it is the kind of ask that
positions a studio as a steward rather than a vendor.

**The usable EMEA estate verified this pass:**

- **[UOC/java-lti-1.3-provider-example](https://github.com/UOC/java-lti-1.3-provider-example)**
  (**MIT**, Spain) — a working LTI 1.3 Advantage tool on the Universitat Oberta de
  Catalunya's own LTI libraries. The Java counterpart to a Python tier that is **four
  repositories deep in total** (see `repos/foundations.md`), so for a Java-shop client in
  EMEA this is the healthier path.
- **[nextcloud/assistant](https://github.com/nextcloud/assistant)** and
  **[nextcloud/context_chat](https://github.com/nextcloud/context_chat)** (**AGPL-3.0**,
  Germany) — on-premises assistant and RAG-over-documents. The self-hosted European answer
  where data residency binds. AGPL does not obstruct a **deployment and integration**
  engagement; it obstructs shipping a proprietary derivative.
- **[cerpus/Edlib](https://github.com/cerpus/Edlib)** (GPL-3.0, Norway) — interactive
  content authoring, H5P-adjacent.
- **[Citolab/qti-convert](https://github.com/Citolab/qti-convert)** (GPL-3.0,
  Netherlands) — QTI conversion from **Cito**, the Dutch national assessment institute.
  Pair with the **ISC-licensed** [pie-qti](https://github.com/pie-framework/pie-qti)
  player when the deliverable must be permissive: **assessment is the high-risk
  classification under the AI Act**, so QTI conformance and the AI Act conformity file are
  the same workstream.
- ⚠️ **[leemonade/leemons](https://github.com/leemonade/leemons)** (Spain) — open-core
  split **by directory**, not one grant. Per-directory review before any reuse.

**The EMEA opportunity, stated as work:** (1) **AI Act conformity files for assessment and
admission systems** — now enforcement-era work, not preparatory; (2) **data-residency
deployments** on the Nextcloud AI stack for institutions that cannot send student data
abroad; (3) **QTI + conformity** as a single assessment workstream, permissive via `pie-qti`;
(4) **licence-hygiene stewardship** with ministries and standards bodies — the cheapest
high-trust opening available in the region, and it unblocks the vocabulary layer everything
else needs.

#### Thirteenth pass, 2026-10-06 — the most capable permissive AI-native platform on this shelf is African and state-funded

🟢 **This is the EMEA opportunity this pass adds, and it is a reference, not a forecast.**

[`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) —
**BSD-3-Clause**, 108★ / **192 forks** — comes from the **IRF-SIC Laboratory at Ibn Zohr
University in Agadir, Morocco**, with the **Regional Centre for Education and Training
Professions (CRMEF) Souss-Massa**, and is funded by Morocco's **Ministry of Higher
Education, Scientific Research and Innovation**, the **Digital Development Agency (DDA)**
and the **CNRST**.

Why it is an opportunity rather than a curiosity:

- 🟢 **It is a government-funded sovereign-stack tutoring platform.** It ships **local
  RAG** and serves **Ollama** as a configuration option alongside hosted APIs. The EMEA
  data-residency posture this KB has specified component-by-component since **P4** is, here,
  a setting. **P33** (added this pass) is the delivery shape.
- 🟢 **It is the strongest public-sector reference this KB can offer an EMEA buyer.** A
  ministry, a national digital agency and a national research council already stand behind
  it. In a procurement conversation that outranks a vendor pilot.
- 🟢 **It reframes the Africa position.** This KB's fourth pass recorded its *first*
  Africa-placed repositories. This pass places, in Africa, the **most capable AI-native
  education platform on the entire permissive shelf** — ahead of the European, Indian,
  Singaporean and Brazilian entries on the same axis. **Africa is a supply region for this
  industry, not only a demand region**, and a Globant EMEA engagement can be built on
  Moroccan public-sector IP.
- 🔴 **Two diligence items travel with it.** The payload's copyright holder — *"Mohamed El
  hajji On behalf of all **R2D-dev**"* — names an entity that appears in **no public
  artefact of the project**, and the project is **open core** with a paid Enterprise
  Edition. Both go in the diligence pack before it is proposed. Full write-up in
  `verticals/solutions.md`.

🔵 **Re-verified unchanged this pass:** Europe at **$2.64B in 2026** → **$8.0B by 2030**
(**31.9% CAGR**); **Finland, Estonia and the Netherlands** leading K-12 integration; the
UK's **£4M** lesson-planning and marking investment; and the **Digital Omnibus**
(Regulation (EU) 2026/1744) deferral of Annex III stand-alone high-risk obligations to
**2 December 2027** and Annex I embedded to **2 August 2028**, with **Article 50
transparency duties live since 2 August 2026**. 🟢 **This pass confirms the Omnibus dates
from an independent sweep** — Council final approval **29 June 2026** — so the KB's
eleventh- and twelfth-pass reading stands. The near-term billable deliverable remains
**labelling and transparency**, not Annex III conformity.

🔴 **A declared EMEA blind spot, newly measured.** The European-sovereignty forge
**`codeberg.org`** and the European Commission's own open-source catalogue
**Joinup / OSOR** are **unreachable from this environment** (403 at the egress proxy).
Two named Codeberg education projects — **`lerntools`** (German, privacy-focused digital
education) and **`lmemsm/delightful-educational-games`** — were surfaced and **could not be
licence-verified, so they are on no shelf.** The forge most likely to hold EU-hosted,
EU-licensed public-sector education software is exactly the one this KB cannot see. Treat
the EMEA supply picture as **GitHub-only and therefore understated**.


#### Fourteenth-pass additions, 2026-10-06 — the ministry tier is real, and a treaty body is writing the evaluation framework

🟢 **The most consequential EMEA finding this pass is a shape, not a number: a national
curriculum published as an open API and wrapped, permissively, as an agent-callable server.**

| Authority | Wrapper | Licence (payload read) | What it exposes |
|---|---|---|---|
| **Skolverket**, Swedish National Agency for Education | [isakskogstad/Skolverket-MCP](https://github.com/isakskogstad/Skolverket-MCP), 12★ | 🟢 **MIT** (1,093 B) | *All* of Skolverket's open APIs: **Läroplan / syllabus**, **Skolenhetsregistret** school-unit register, Planned Educations. In the official MCP Registry. |
| **Udir**, Norwegian Directorate for Education | [3121n/nor-data-udir-mcp](https://github.com/3121n/nor-data-udir-mcp) | 🔴 **none** (0 of 20 filenames) | School (NSR) and kindergarten (NBR) registries. |
| **Smartschool**, dominant LMS in Flemish education (Belgium) | [MauroDruwel/Smartschool-MCP](https://github.com/MauroDruwel/Smartschool-MCP), 5★ | 🟢 **MIT** (1,069 B) | Platform integration; PyPI package, CI, codecov. |

**Why this is an opportunity and not a curiosity:** in this region *"aligned to the national
curriculum"* is a procurement requirement, and it has been a consulting deliverable — someone
reads the syllabus and writes a mapping. Where the authority publishes an API and a
permissive wrapper exists, it becomes **a tool call inside the product**, re-checked on every
run. That is the input P15 was missing.

⚠️ **Two diligence items, both of which an MIT badge hides.** Skolverket-MCP's copyright line
reads **"Skolverket Syllabus MCP Contributors"**, not the agency: the grant covers the
**wrapper**, and the **agency's own terms govern the data**. And Udir is the counter-case in
the same region — same idea, same quality of public data, **no grant at all**. So the
engagement shape is *"check for a wrapper, expect to write one"*, and writing one against a
public national API is a small, well-bounded, highly reusable piece of work.

🆕 **A European evaluation framework for educational technology is being written by the
Council of Europe, not by a market.** Its Education Department convened the **2nd Working
Conference on the regulatory dimensions of AI in education (October 2026)**, covering AI
governance in education, teaching and learning with AI, and **a European evaluation framework
to assess educational technologies**. Read alongside the EU AI Act — full effect from August
2026, education systems **high-risk** — this is a second, softer instrument aimed at the one
question the Act does not answer: *is the thing any good pedagogically.*

🔵 **The commercial consequence is a deliverable, available now.** This KB has recorded for
several passes that the pedagogy-evaluation tier is either absent or licensed shut (trends
27, 31, 32; pattern P23). A treaty body drafting an evaluation framework means the
**artefact** — a documented, re-runnable evaluation of an education AI system against stated
pedagogical criteria — becomes procurement-relevant **before** any benchmark is settled.
Build the socket, as P23 says; the EMEA engagement is now the socket plus the paperwork.

**Demand-side number read this pass:** **94%** of organisations are at least somewhat likely
to invest in AI-specific training in 2026, and the EMEA framing is explicit that AI fluency
has to reach business leaders, legal and compliance teams and frontline staff — not only data
scientists and developers. That is enablement scope (P6) sold to three audiences, one of
which is the client's own legal function and is also the audience for the governance
artefacts above.


#### Twentieth pass of 2026-10-06 — the transition-provision channel: the public-authority date is 2030, and most education buyers qualify

🟢 **The opportunity this channel found is four years long and this KB had never recorded it.**
Article 111 of the AI Act: a high-risk system lawfully placed on the market before the high-risk
rules apply may continue **without retrofit or additional certification, provided its design remains
unchanged**; and **providers and deployers of high-risk AI intended to be used by public authorities
must comply by 2 August 2030.** AI inside **Annex X** large-scale IT systems placed before
**2027-08-02** has until **2030-12-31**.

🔵 **Why this is a European education finding specifically.** Annex III §3 covers admissions and
access, evaluation of learning outcomes, level placement and monitoring for prohibited behaviour
during tests — and in EMEA the operators of those systems are predominantly **ministries, regional
authorities and state universities**, which is to say **public authorities**. ⚠️ **The same
engagement is worth four years to a state university and until 2027-12-02 to a private tutoring
company** — so the buyer's legal form, not its size or sector, sets the value of the work.

🔴 **And the condition is what makes it sellable rather than reassuring: the extension dies on a
change in design.** A tutor bolted onto a legacy LMS, an agent wired into an SIS, a model replacing
a rules-based placement engine — each ends it. 🟢 **The offer is therefore
`P-TRANSITION-EVIDENCE`: a non-modifying mandate that banks the extension** — design-stability
attestation, corpus manifest, behaviour and fairness baseline, accessibility queue — **followed by a
priced modification register** that tells the ministry what each item on its roadmap costs in
conformity terms before it commits.

⚠️ **Pair it with the gap the nineteenth pass established and do not let it get lost: as of
2026-07-20 no version of EN 301 549 had been cited in the Official Journal under the European
Accessibility Act.** The EAA has been in force since **2025-06-28**, so in EMEA **the obligation is
live and the safe harbour is not** — conformance cannot be discharged by naming a standard, which is
precisely why the deliverable in this region is evidence. 🔵 **Market frame: Europe $2.64B in 2026 at
31.9% CAGR toward $8.0B by 2030; MEA $0.56B at 34.3%**, with Finland, Estonia and the Netherlands
leading K-12 integration and the **UAE** one of only two countries worldwide running a compulsory
national AI curriculum since 2025-26.

#### Twenty-second pass of 2026-10-06 — the forge where European public-sector education code actually lives

**Measured, not asserted: 11 of the 18 rows this pass added are EMEA-origin — 5 verified from the
project's own README (Saxion, TIB Hannover, RWTH Aachen, Paris-Saclay, and SAM LMS's own "African"),
6 inferred from a namespace or an author name and marked as such** — Netherlands
(Saxion's `lms42`), Germany (TIB Hannover's OERSI plugin, RWTH Aachen's OmiLAXR, Particify's LMS
connector, GitClassrooms, the Münster OER toolchain), France (Travo), Switzerland (OpenOLAT's second
host), Greece (Universis EduAPI), and an Africa-targeted LMS. **One sweep of a forge this KB had
never searched returned a European public-institution estate.**

🔵 **Why that is a sovereignty signal and not a trivium.** The institutions whose code this sweep
returned — a university of applied sciences, a national library of science and technology, a
technical university's learning-technologies group, a Greek higher-education consortium — are
exactly the buyers who must demonstrate that teaching data stays in their own infrastructure. They
are not publishing to GitHub. **A supply map built on one forge missed them entirely.**

🔴 **And the honest half: the European supply is more copyleft than this KB's GitHub shelf.** Of
those 10 EMEA rows, **4 are copyleft** — AGPL-3.0 (`lms42`, `omilaxr`, MoodleNet) and LGPL-3.0
(`eduapi`, the 1EdTech **EduAPI** implementation). The interoperability layer trend 28 named as
missing turns out to exist in Europe and to be **weak-copyleft**, which means *linkable, not
foldable*: the LGPL-3.0 route is the one this KB already documents for Odoo/OpenEduCat.

**The regulatory frame is unchanged and now closer.** AI systems that determine access to education
or assess learning outcomes sit in **Annex III** of Regulation (EU) 2024/1689; schools and
universities that deploy them are **deployers** with their own duties, including the **AI-literacy**
obligation for staff operating the systems. Risk management, data governance, human oversight,
transparency and conformity assessment are pre-deployment, not post-hoc.

🟢 **Two concrete lines that follow:**

1. **Procurement-grade interoperability.** [`kbarbounakis/eduapi`](https://gitlab.com/kbarbounakis/eduapi)
   (LGPL-3.0) is a **1EdTech EduAPI** implementation in production use by a university consortium —
   the first in this KB. It is the answer to the scored interoperability line item, with a licence
   conversation attached rather than a build.
2. **Public-institution OER discovery.** [`TIBHannover/oer/wordpress-oersi-plugin`](https://gitlab.com/TIBHannover/oer/wordpress-oersi-plugin)
   (**MIT**, committed 2026-10-02) puts the German **OERSI** index behind a WordPress front end. MIT,
   maintained by a national institution — the cheapest credible OER search tier in this KB.
### APAC

- **Largest absolute AI market: ~USD 102B as of March 2026** (all sectors, not
  education alone).
- **India is the fastest-growing APAC AI market at 38.9% CAGR**, anchored by the
  IndiaAI Mission and ~2.6M STEM graduates a year. In **July 2026 the Indian
  government signalled it may pursue dedicated, risk-based AI legislation.**
  India's DPDP Act obligations are now in force for systems processing personal
  data.
- **South Korea's AI Basic Act takes effect January 2026**, giving roughly a year
  to build compliance frameworks for high-impact systems. **China maintains the
  region's most restrictive framework**, built on three foundational laws.
- **Sovereign model build-out is universal:** India's Sarvam AI, Malaysia's ILMU,
  Indonesia's Sahabat AI, Singapore's SEA-LION, Korea's HyperCLOVA X Think,
  Japan's NTT Sarashina. These are base models — **none ships an education agent
  layer**, which is precisely the gap.
- **Cultural tailwind:** the Ipsos Education Monitor 2026 finds *lower* support
  for banning AI in schools across the Asian markets surveyed — while **Australia
  and New Zealand record higher support for banning AI in schools**, a real
  split inside the region.
- **Opportunity:** education agent layers on top of sovereign models — the models
  exist, the pedagogy layer does not. Multi-jurisdiction architecture is the hard
  part and the differentiator: one deployment must satisfy Korea's AI Basic Act,
  India's DPDP and China's framework simultaneously. Treat ANZ as a separate,
  more restrictive sub-market.

**New this pass (2026-10-06):**

- **Singapore published the world's first governance framework for agentic AI**,
  at Davos in **January 2026** (IMDA Model AI Governance Framework for Agentic AI,
  updated again in June 2026). This is the single most useful regulatory document
  in this KB, because it governs *agents* specifically, and its four dimensions
  are effectively a build checklist:
  1. assess and bound risk upfront — choose appropriate agentic use cases and
     place explicit limits on an agent's powers;
  2. make humans **meaningfully** accountable — define the checkpoints that
     require human approval;
  3. technical controls and process across the whole agent lifecycle;
  4. enable end-user responsibility through transparency **and training** — where
     an agent assists a user in their workflow, the framework expects education on
     its capabilities, common failure points and risks.
  Dimension 4 is a services line item: the regulator is asking for exactly the
  teacher-and-student enablement work Globant already sells. Design to this
  framework and the resulting artefacts largely satisfy EU Annex III and the US
  human-oversight statutes too.
- **Korea's AI Framework Act took effect 22 January 2026** (precise date; earlier
  passes recorded only "January 2026").
- **Vietnam has a dedicated AI law: Law No. 134/2025/QH15, in force 1 March
  2026** — net new to this KB, and evidence the binding-regulation wave now
  extends well beyond Korea, Singapore and China.
- **Named incumbents in APAC education:** Google, Microsoft, IBM, Pearson and
  **Byju's**, with China, India and Japan dominating regional spend. The buyer
  relationship is held by global platforms plus one regional giant.
- **More sovereign base models, still no pedagogy layer:** add **BharatGen**
  (IndiaAI Mission, ~$1.2B state investment), Japan's **Fugaku-LLM**, and Korea's
  National Sovereign AI Initiative champions (LG AI Research, SK Telecom, Naver
  Cloud, NC AI, Upstage). Sovereign *inferencing platforms* with in-country data
  residency are also being commercialised (e.g. NxtGen in India). The gap is
  unchanged and widening: the models and now the hosting exist; the education
  agent layer does not.

**New in the third pass (2026-10-06):**

- **The scale number this KB was missing: approximately 530 million K-12 students
  in Asia (2024).** Every per-learner cost, licence and inference decision changes
  shape at that denominator. It is also the reason offline-capable and
  small-model deployments matter in APAC and not only in LATAM.
- **Regional AI adoption is projected to move from 65–75% in 2025 to 80–90% in
  2026.** Adoption is not the constraint anywhere in APAC.
- **China's AI-education mandate is provincial, specific, and includes a
  restriction that directly constrains the architecture.** Earlier passes recorded
  China as having a "compulsory national AI curriculum"; probed precisely, the
  mandates are issued at provincial level:
  - **Beijing:** every primary and secondary school must deliver **at least 8 hours
    of AI lessons per year**, from **1 September 2025** — compulsory from age six.
  - **Guangdong:** **6 hours annually** in lower grades, rising to **one hour a
    fortnight in grades 10 and 11**.
  - The curriculum progresses from voice-recognition basics in early grades to
    machine learning, **misinformation detection** and applied projects by high
    school.
  - **Primary-school pupils are barred from independent generative-AI use, and
    teachers are prohibited from substituting AI for their core instructional
    duties.**
  That last point is a build requirement, not a policy footnote: a compliant K-12
  deployment in China needs **age-gated capability** (younger cohorts get
  teacher-mediated AI only) and a teacher-in-the-loop design that is enforced by the
  system rather than by guidance. It is also the strictest form of the
  human-oversight requirement that EMEA and North America express more loosely, so
  **a design that satisfies Beijing satisfies the others**. Pattern P9 in
  `compose/patterns.md` builds to it.
- **Regulatory posture, stated per country rather than per region:** Korea's
  Framework Act in force **22 January 2026**; **Vietnam's Law No. 134/2025/QH15 in
  force 1 March 2026 — Southeast Asia's first dedicated AI law**; China the most
  assertive regulator while also leading on deployment; **Japan deliberately
  light-touch and voluntary** to favour innovation; **India and Australia still
  without a national framework in force**, both working on one. A single APAC
  compliance story does not exist, and "APAC-ready" is not a claim you can make.

- **Supply side, fourth pass of 2026-10-06: APAC is now the region that *exports*
  education AI.** Every other region in this KB is a buyer. APAC publishes — and
  the pass added **Tsinghua University's
  [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) (MIT, 40.0k★,
  v1.2.0-rc.1 2026-10-04)**, now **the largest permissively licensed asset in this
  KB**: document-or-topic → a full generated lesson (slides, quizzes, HTML
  simulations, PBL scenes) taught by AI teacher *and* AI classmate agents, with
  PostgreSQL-backed server-side generation.
  **Two consequences.** First, the **China-plus-Hong-Kong concentration gets
  sharper, not softer**: a 40k★ flagship from Tsinghua sits alongside DeepTutor
  (HKUDS, 40.8k★), while **no India-, Japan-, Korea- or ASEAN-origin permissive
  education project** has surfaced in any channel — searched by name this pass.
  "APAC-ready" remains a claim you cannot make; the regulatory map (Korea
  22 Jan 2026, Vietnam 1 Mar 2026, Japan voluntary, India and Australia with no
  national framework in force) and the supply map **both** fracture along national
  lines.
  Second, for every other region the practical consequence is the same: **the
  default starting point for a lesson-generation build is now Chinese-origin code
  under MIT.** That is fine legally and a live question for a public-sector buyer
  in EMEA or North America — so the **provenance conversation, data-residency
  posture and a reviewed fork** belong in the first week of the engagement, not
  the last.


#### Fifth pass, 2026-10-06 — three binding regimes, one accreditation lever, and a licence trap

Earlier passes recorded APAC regulation as "heterogeneous and moving toward
binding frameworks." It has largely arrived. Dated and specific:

| Jurisdiction | Instrument | Status | What it requires that bears on education |
|---|---|---|---|
| **South Korea** | **AI Basic Act** (Act on the Development of Artificial Intelligence and Establishment of Trust) | **In force 22 January 2026** | Transparency, risk assessment, **human oversight** and documentation for **high-impact** systems. Education decisions sit squarely in the high-impact concept — the same substance as EU Annex III, arriving **23 months earlier** |
| **Vietnam** | **Law No. 134/2025/QH15 on Artificial Intelligence** | **Effective 1 March 2026** | A dedicated national AI law. First-mover compliance work in a market with no incumbent AI-governance services base |
| **Australia** | **TEQSA** (national higher-education regulator) | Active requirement | **Every** higher-education provider must submit an **institutional action plan** addressing generative-AI risks. This is an **accreditation** lever, not a fine — it is the sharpest procurement trigger in the region |
| **China** | Generative AI Services Management Measures; synthetic-content identification rules (**effective 1 September 2025**) | In force | Consent, data quality, **content labelling**, user rights, complaint handling. Compounds the age-gating and teacher-substitution rules this KB already records |

**The Australia item is the one to act on first.** A regulator requiring a written
institutional action plan from every provider in a country creates a bounded,
repeatable, nationally-scoped deliverable with a known buyer and a deadline that
is not negotiable, because accreditation depends on it. There is no equivalent
single-document, single-regulator trigger in any other region in this KB.

**South Korea reorders the global compliance calendar.** With the EU's Annex III
obligations now at December 2027 (see EMEA above) and Korea's AI Basic Act **in
force since January 2026**, **Korea — not the EU — is now the binding constraint
for a multi-jurisdiction education product.** Build to the Korean high-impact
requirements and the EU conformity work becomes largely a documentation exercise.
This is the reverse of how this KB and most of the market have sequenced it.

**Sovereign-model landscape, updated:** **MaLLaM**, Malaysia's sovereign LLM built
with NVIDIA, natively handling Malaysian Bahasa and colloquial dialects, deployed
to **3M+ users** via YTL/Yes mobile; **Gemma-SEA-LION-v4-27B-VL**, a
vision-language member of the SEA-LION v4 family, released **March 2026**.

**And the licence trap, because this is where an APAC engagement will hit it:**
[aisingapore/sealion](https://github.com/aisingapore/sealion) (424★) has **no
repository-level `LICENSE` payload**. Its README states terms vary with the
underlying base model — Llama3-derived variants carry commercial-use
restrictions, Gemma-derived variants differ — and directs you to each **Hugging
Face model card**. **Rights must be cleared per model and per release, not per
repository.**

**Singapore is the region's reference deployment and it is closed.** AICET (AI
Singapore, funded by the Smart Nation and Digital Government Office, working with
the Ministry of Education) runs Codaveri, Softmark and ScholAIstic at ministry
scale with no public repositories — while the LMS beneath Codaveri,
[Coursemology](https://github.com/Coursemology/coursemology2), is **MIT with
15,802 commits**. See `verticals/solutions.md`.



#### Sixth pass, 2026-10-06 — the voice and language layer

**Adoption is high and governance is lagging, by the region's own accounting.**
**48% of APAC governance leaders** make AI adoption a top strategic priority for
2026 and **57% of organisations in Asia** already run AI in one or more areas,
while **49% cite insufficient infrastructure for real-time data processing** as
the barrier. **AI sovereignty will shape infrastructure choices for roughly half
of APAC firms**, and regulators are moving (Singapore's consultations on AI use in
financial institutions are the template for transparency and accountability
expectations). Named commercial movement in education: **LearnUpon** opened a
Sydney HQ with Create+ AI course authoring; **NIIT MTS** made Training Industry's
Top 20 custom content developers for 2026 on AI-led design; **TCS and Pearson**
announced a multi-year AI learning alliance.

**What this pass opens here — and APAC now splits cleanly in two.**

- **India: the only all-MIT national stack in this KB (P16).** Sunbird (**MIT**,
  38,046 commits, deployed as **DIKSHA**, a recognised **Digital Public Good**,
  18+ languages, NCERT/CBSE/SCERT) plus AI4Bharat's **MIT** layer — translation
  across **all 22 scheduled languages**, TTS in 13, ASR pretrained on 40, and the
  Shoonya annotation platform for the teacher-review gate. **Platform, language,
  orchestration and review, every component MIT.** In a public procurement that
  removes the licence conversation entirely, and it directly answers the
  sovereignty concern half the region reports.
- **ASEAN: the licence is per checkpoint, and that is a billable service.**
  [SEA-LION](https://github.com/aisingapore/sea-lion) has **no repository-level
  licence**; its grant is deferred to each HuggingFace **model card** because terms
  vary with the base model (Llama-derived variants may carry Meta's commercial
  restrictions). Combined with the fifth pass's finding that ASEAN's ministry-scale
  products are closed while the LMS beneath them is MIT, the position is:
  **integration surfaces are permissive, model rights are not.** Offer
  per-checkpoint licence review as a recurring engagement line, not a one-off gate.

#### Seventh pass of 2026-10-06 — Vietnam's education rules, and the ASEAN language shelf that exists

**Vietnam: Decree 33 is the instrument that makes Law 134/2025/QH15 operational
for education, and this KB did not have it.** Signed **2026-06-30**, in force
**2026-08-15**; lists **46 high-risk AI systems** across six sectors, **three of
them in education**:

| # | Education high-risk category | EU Annex III point 3 equivalent? |
|---|---|---|
| 1 | AI providing **self-learning content from uncontrolled data sources** | **No equivalent.** Regulates the tutor by **corpus provenance**, not by any decision it makes |
| 2 | AI that **automatically evaluates results and ranks learners** | Yes — evaluation of learning outcomes, level placement |
| 3 | AI that **monitors and analyses learner behaviour using biometric data** | Partly — Annex III covers exam/behaviour monitoring **without** the biometric qualifier, so Vietnam is **narrower** here |

Obligations: **report the risk level to the Ministry of Science and Technology
before use**; **conformity assessment** before deployment and maintained
throughout; designated systems assessed by a **registered or recognised
conformity assessment body**, others **self-assessed** by the provider.
Transition: education systems already in operation — grouped with **healthcare
and banking** — have until **2027-09-01**; all other existing high-risk systems
until **2027-03-01**.

**Commercial read, three points.**

- **Category 1 is the one to price into every Vietnam proposal.** A RAG tutor
  that only explains — no grading, no ranking, no monitoring — is **still
  high-risk** if its corpus is uncurated. The deliverable that answers it is a
  **source manifest** (what was ingested, from where, under what rights, reviewed
  by whom), which is billable work and is also the artefact a conformity
  assessment consumes. See **P20**.
- **The 2027-09-01 education transition is a defined sales window.** Education,
  healthcare and banking got the **longest** runway of any sector, so incumbent
  deployments have ~11 months beyond the general deadline to be brought into
  conformity. That is remediation work with a statutory date on it.
- **Vietnam is looser than the EU on analytics.** Because category 3 is qualified
  to **biometric** data, non-biometric engagement analytics — time on task,
  attempt counts, mastery curves — sit outside it. **First instance in this KB of
  an APAC regime being less restrictive than Annex III on a specific axis**, and
  it favours analytics-led products.

⚠️ **Provenance:** every legal-publisher domain carrying this decree is
**EGRESS_BLOCKED** here (6/6 refused: `allenandgledhill.com`,
`vietnam-briefing.com`, `vietnamnews.vn`, `thuvienphapluat.vn`, `vietanlaw.com`,
`ed.events`). The three categories are recorded from **two independently-phrased
searches that agreed on all three**; the biometric qualifier appeared in only
one. **Confirm against the decree text before using this in a deliverable.**

**The ASEAN language substrate exists, and the sixth pass said it did not.** This
KB recorded ASEAN as having no permissive language layer because it searched for
sovereign models and found [SEA-LION unlicensed](https://github.com/aisingapore/sea-lion).
Searching in Bahasa, Thai and Vietnamese returns a real shelf — **Vietnamese
`underthesea` (Apache-2.0, 1.8k★), Thai `pythainlp` (Apache-2.0, 1.2k★, 6,649
commits), Malay `malaya` + `malaya-speech` (both MIT), Indonesian `nusa-crowd`
(Apache-2.0, 143 datasets)**. Full shelf in `repos/foundations.md`.

**What that changes for an ASEAN engagement.** The fifth pass's finding was that
ASEAN's mature education AI is **closed** (AICET's Codaveri, Softmark,
ScholAIstic) over an **MIT substrate** (`Coursemology/coursemology2`) — a good
commercial position. Add the language shelf and the position improves again: the
**LMS substrate is MIT, the language substrate is Apache-2.0/MIT, and the
pedagogy layer in a national language is unbuilt by anyone, open or closed.**
That is the clearest build-and-own opportunity in APAC outside India. **P19.**

**Caveat on the opportunity, so it is not oversold:** only `malaya-speech` covers
voice. Thai, Vietnamese and Indonesian have text-layer coverage only, so spoken
practice in those languages routes through `sherpa-onnx` or Whisper and needs
per-language accuracy testing before it is promised.


#### Eighth pass, 2026-10-06 — no new APAC education rule; sovereignty is the operative frame

The mandated APAC sweep returned **sovereignty and governance-gap material**
rather than education regulation: 48% of APAC governance leaders naming AI
adoption a top 2026 priority, 57% of Asian organisations with AI in at least one
area, Singapore's consultations on AI in financial institutions, and a
*"sovereign-by-design"* framing for 2026 regional execution. **No new education
instrument** beyond the Korea **AI Framework Act** (in force 2026-01-22) and
Vietnam's **Decree 33** (in force 2026-08-15) that this file already carries.

**Why "sovereign-by-design" is the APAC education opportunity and not a
slogan.** It is the one region where the buyer's stated preference — run it in
our jurisdiction, on our data, under our rules — aligns exactly with what a
permissive self-hosted stack delivers and a SaaS tutor cannot. The seventh
pass's ASEAN language shelf (`pythainlp`, `underthesea`, `malaya`, `nusa-crowd`,
all permissive) is the supply side of that preference, and it is the
best-licensed regional language layer in this KB — **a direct contrast with
LATAM's indigenous layer below, where the same capability exists without
grants.**

**Explicit gap, unchanged:** no **Korea**-origin permissive education *agent*
(the seventh pass found course material, not an agent), which remains the widest
distance in this KB between regulatory maturity and open supply.

#### Ninth pass, 2026-10-06 — APAC's own education-evaluation benchmark exists, and it has no grant

**One education-specific finding, and it is a rejection.**
[AI-EDU-LAB/E-EVAL](https://github.com/AI-EDU-LAB/E-EVAL) — **33★**, *"Official
github repo for E-Eval, a Chinese K12 education evaluation benchmark for LLMs"*,
Python — has **no licence payload** under `LICENSE{,.md,.txt}`, `COPYING`,
`LICENCE{,.md,.txt}` or `COPYRIGHT`, on either branch.

**This matters more than its star count.** The thing E-Eval does — evaluating
LLMs against K-12 education criteria — is precisely the capability the **$26M
North American programme is spending millions to create under Apache-2.0** (see
the North America subsection). **APAC already built it, and did not license it.**
The region is not behind on capability; it is behind on **redistributability**,
which is the third region in which this KB has now recorded that exact shape
after MEA's Arabic tutor (seventh pass) and LATAM's indigenous-language layer
(eighth pass).

**The engagement consequence is specific:** for a China or wider APAC education
engagement, E-Eval is a **capability you can read and reimplement but not
vendor**. Reimplementing an evaluation benchmark from a published description is
tractable work — far more tractable than building one from nothing — and the
resulting harness is yours to license. Alternatively, a single `LICENSE` file
contributed upstream would change the regional answer, which is the same cheap
remedy the seventh pass proposed for MEA and the eighth pass found an event's
rules could deliver at scale.

**Declared: no new APAC education regulation was found this pass.** The mandated
regional query returned **enterprise governance** material — 48% of APAC
governance leaders prioritising AI adoption for 2026, 57% of Asian organisations
with AI in at least one operational area, 49% citing insufficient real-time data
infrastructure, Singapore's financial-sector AI consultations, and a general
convergence on safety/transparency/accountability with **AI sovereignty** as the
2026 frame. **None of it is education-specific.** The binding education regimes
for this region remain the ones recorded in the fifth and seventh passes
(including **Vietnam's Decree 33**, still the strictest on corpus provenance) and
the sovereignty framing from the eighth. **Second consecutive pass in which the
general APAC query returned enterprise rather than education material** — like
EMEA, this region needs a channel change, and the ministry-org channel that
worked for the UK this pass is the obvious candidate.

#### Tenth pass of 2026-10-06 — a ministry already has a vendor, and it says it is still shopping

The generalist regional query failed for the **third consecutive pass**, returning
enterprise material (48% of APAC governance leaders making AI adoption a top 2026
priority; 57% of Asian organisations with AI in at least one area; Singapore's
consultations on AI in financial institutions; corporate LMS and upskilling
announcements). **Not education findings.** Retired for this region, as for EMEA.

**What worked was the ministry-programme channel**, the APAC analogue of the UK
DfE sweep. **Tier 2.**

**Singapore's Ministry of Education was welcomed into OpenAI's Education for
Countries on 20 May 2026** at the Education World Forum in London. OpenAI is
supporting use cases developed by **MOE and GovTech** teams, including
personalised learning and **mother tongue language learning**. **Kazakhstan** is
also named in the programme's first cohort.

**The opening is in Singapore's own framing.** MOE is described as *"exploring
various AI tools from different partners to meaningfully support teaching and
learning."* A ministry that states a **multi-partner** posture while onboarding one
vendor is a ministry that will evaluate alternatives — and GovTech's involvement
means the counterparty is an engineering organisation that can assess an open,
auditable, data-resident stack on its merits. **That is a different sales motion
from displacing an incumbent, and it is open now.**

**The mother-tongue use case is the one to lead with.** It is precisely where this
KB's language substrate shelves (sixth, seventh and eighth passes) hold
permissive, regionally-placed assets, and precisely where a single global vendor is
weakest.

**Tier 1 confirmation, and it is a negative.**
[AI-EDU-LAB/E-EVAL](https://github.com/AI-EDU-LAB/E-EVAL) — the Chinese K12 LLM
education evaluation benchmark (33★), the region's most on-target evaluation asset
— was **re-probed this pass across 20 URLs** (both `LICENCE`/`LICENSE` spellings,
both `main` and `master`). **Still no licence payload.** The repository exists;
`main/README.md` resolves. The ninth pass's *built, published, benchmarked,
ungranted* finding for APAC **survives a full re-probe** and is no longer
attributable to a spelling or branch defect in this KB's method. **APAC has the
evaluation benchmark the US is funding and the licence that makes it unusable.**
A grant request to the maintainers is a cheaper route to a regional evaluation
asset than building one.


#### Eleventh pass, 2026-10-06 — the region's red-team harness is Apache-2.0, and its national stack is MIT and dormant

| Asset | Origin | Licence (Tier 1, payload read 2026-10-06) | Scale |
|---|---|---|---|
| [aiverify-foundation/moonshot](https://github.com/aiverify-foundation/moonshot) | **AI Verify Foundation** — Singapore IMDA's AI-testing community | **Apache-2.0** | 355★, 72 forks, pushed 2026-10-06 |
| [project-sunbird/sunbird-lms-mw](https://github.com/project-sunbird/sunbird-lms-mw) | **Sunbird** — the stack under India's **DIKSHA** | **MIT** | 6★ / **41 forks**, 🔴 last push 2024-08-30 |
| [project-sunbird/sunbird-analytics](https://github.com/project-sunbird/sunbird-analytics) | Sunbird | **MIT** | 3★ / 28 forks, 🔴 2023-02-08 |

**Two findings that pull in opposite directions.**

1. **Singapore exports the evaluation instrument.** Moonshot evaluates *and
   red-teams* any LLM application, Apache-2.0, maintained. For an education
   deployment the red-team half is not optional — the adversary is a student with
   unlimited attempts and no deadline. This is the only permissive red-teaming
   harness in this KB, and it comes from the same regulator-adjacent body whose
   guidelines the region's buyers already cite.
2. **India's national stack is the most permissive in the world and nobody is
   pushing to it.** Sunbird is **MIT** at national tier — more permissive than
   Moodle, Open edX, or anything else of comparable deployment — and its GitHub
   activity stopped in 2024, with one component **archived**. The fork-to-star ratio
   (41:6) says deployed-and-forked, not abandoned-and-ignored; but a KB must not
   read it as an upstream. **Reference architecture and licence-clean base, not a
   maintained dependency.**

**Market context re-corroborated this pass (Tier 2):** **56% of APAC businesses have
already deployed chatbots, copilots or AI assistants — outpacing both Europe and
North America** — and **48% of governance leaders name AI adoption a top strategic
priority for 2026**. Regulation stays **fragmented by design**: a common APAC-wide
framework remains distant, with Singapore running mature responsible-AI guidelines,
China legislating against algorithmic misconduct, and India applying existing
criminal law. **Sovereignty will shape infrastructure choices for roughly half of
APAC firms.**

**The opportunity:** fragmentation plus sovereignty plus the highest deployment rate
means the sellable artefact is a **per-jurisdiction policy layer over one
architecture** — and both the harness (Inspect, MIT) and the red-team tooling
(Moonshot, Apache-2.0) can be run inside the client's own boundary, which is the
condition sovereignty actually imposes.

**Declared, so it is not mistaken for coverage:** the generalist APAC repository
probe `education AI tutor India OR China OR Indonesia OR Japan language stars:>50`
returned **`total_count` 0**. That is an **instrument limit, not an absence** —
GitHub repository search ANDs free-text terms, so a five-term query collapses. The
region's assets above were found by **named organisation**, which is now the third
consecutive pass in which naming the institution worked and the generalist query
did not.

#### Twelfth pass, 2026-10-06 — the only region where the regulator's own conformance harness is permissive and extensible

**The binding regimes, as read this pass.** APAC's regulatory environment is
heterogeneous and is converging on binding frameworks rather than guidance:

| Jurisdiction | Instrument | Status |
|---|---|---|
| **South Korea** | **AI Basic Act** (Act on the Development of AI and Establishment of Trust) | **In force 22 January 2026.** Transparency, risk assessment, **human oversight** and documentation obligations for high-impact AI systems. |
| **Vietnam** | **Law No. 134/2025/QH15 on Artificial Intelligence** | **In force 1 March 2026.** A dedicated national AI law. |
| **China** | Generative AI Services Management Measures + **synthetic-content identification** rules | Enforced. Consent, data quality, **content labelling**, user rights, complaint handling. |
| **Australia** | **TEQSA** (national higher-education regulator) | **Requires all higher-education providers to submit institutional action plans** addressing generative-AI risk. |

**The market shape.** China, India and Japan dominate regional AI-in-education spend,
with China leading on heavy government backing. The named market leaders are **Google,
Microsoft, IBM, Pearson and Byju's** — **all proprietary**, which is the same ministry-tier
pattern trend 30 records across three regions.

🆕 **The finding of this pass: APAC is the only region where the regulator's own
conformance instrument is permissively licensed *and* designed to be extended.**

| Repository | Body | Licence (payload) | ★ |
|---|---|---|---|
| [aiverify-foundation/aiverify](https://github.com/aiverify-foundation/aiverify) | **AI Verify Foundation**, under **IMDA** (Singapore's Infocomm Media Development Authority) | **Apache-2.0** | 98 (32 forks) |
| [aiverify-foundation/aiverify-developer-tools](https://github.com/aiverify-foundation/aiverify-developer-tools) | same | **Apache-2.0** | — |
| [aiverify-foundation/moonshot-data](https://github.com/aiverify-foundation/moonshot-data) | same | **Apache-2.0** | — |
| `aiverify-foundation/LLM-Evals-Catalogue` | same | 🔴 **Ungranted** | — |

**Why the `developer-tools` row is the strategically interesting one.** AI Verify is a
governance *testing framework* that validates AI systems against internationally
recognised principles through standardised tests — and `aiverify-developer-tools` is the
**plugin and test-widget kit for adding your own tests to it**. There is no
education-specific test suite in it today. That means an **education conformance profile
can be contributed into a government-recognised harness** rather than built alongside one.

**Contrast the three regions, because the engagement shape differs in each:**

| Region | Where the specification lives | What the deliverable is |
|---|---|---|
| **North America** | The **procurement rubric** (trend 26) | Evidence that scores well against it — Ed-Fi, OneRoster, xAPI conformance. |
| **EMEA** | The **statute** — EU AI Act. 🔵 **Corrected in the twentieth pass:** Article 50 **transparency** duties are in force from **2026-08-02**, but the **Annex III high-risk** set where education lives was deferred to **2027-12-02** by Reg. (EU) 2026/1744. ⚠️ **The cell previously read *"in force 2 Aug 2026"*, which over-claims the high-risk duty** | A conformity file for a high-risk system — due 2027-12-02, or **2030-08-02** where the deployer is a public authority (Art. 111, trend 46). |
| **APAC** | The **regulator's own open-source harness** | A test plugin inside that harness — permissive, contributable, and citable as the regulator's instrument rather than the vendor's claim. |
| **LATAM** | 🟢 **The *reglamento*, in one market only** — Peru's **DS 115-2025-PCM** under law **31814**, whose education-sector obligations **activated 2026-09-10**, requiring algorithmic-transparency mechanisms for high-risk systems. 🔴 **Brazil has no AI statute in force** (PL 2338/2023 still in the Chamber) | An algorithmic-transparency mechanism plus the evidence behind it — and in every other LATAM market, the same pack sold as **readiness**, not compliance (twentieth pass). |

That third shape is the most defensible of the four, and it is available only in APAC.

🔵 **Why this table gained a LATAM row in the twentieth pass, and why it needed a correction at the
same time.** It had published **three of four regions** — which, read from outside, is
indistinguishable from having measured four and found three. 🔴 **And the EMEA cell carried the exact
stale date the nineteenth pass corrected elsewhere in this file**, which is the propagation failure
that pass named, found a second time in a second summary table. ⚠️ **A summary table is where a stale
date does the most damage, because it is the cell a proposal quotes.**
⚠️ **With one caveat already visible in the table:** `LLM-Evals-Catalogue` sits in the same
government foundation's organisation and carries **no licence at all**. Organisation-level
licence inference is unsafe even inside a regulator's foundation — read each payload.

**The India/national-scale estate, re-addressed.** The reset had dropped the Sunbird
client addresses; this pass restored them with verified grants:
**[SunbirdEd-mobile-app](https://github.com/Sunbird-Ed/SunbirdEd-mobile-app)** (**MIT**,
offline **and** online consumption, 12,921 commits),
**[SunbirdEd-consumption-ngcomponents](https://github.com/Sunbird-Ed/SunbirdEd-consumption-ngcomponents)**
(MIT) and **[sunbird-telemetry-sdk](https://github.com/project-sunbird/sunbird-telemetry-sdk)**
(MIT). ⚠️ **Read the mobile client's ratio, not its stars: 10★ against 92 forks.** Forks
are what national and state implementers produce; stars are what GitHub browsers produce.
A 10★ repository with 92 forks and ~13k commits is a deployment artefact, and judging it
by star count is the error. Sunbird's telemetry SDK also means an Indian deployment has a
**native MIT event model** and does not have to adopt xAPI to get analytics.

**The APAC opportunity, stated as work:** (1) an **education test plugin for AI Verify**,
Apache-2.0, contributed upstream — the only route in any region to compliance evidence
carried by the regulator's own instrument; (2) **Korea and Vietnam readiness work** against
two laws that came into force in the first quarter of 2026, where human-oversight and
documentation duties map directly onto the artefacts trend 16 already specifies;
(3) **TEQSA institutional action plans** for Australian higher education — a defined,
repeatable, regulator-mandated document; (4) **Sunbird implementation and extension** at
state scale on an MIT base, including the AI layer the platform does not ship.

#### Thirteenth pass, 2026-10-06 — two languages tried, and the supply door did not open

🔵 **Re-verified unchanged:** Korea's **AI Framework Act** in force **22 January 2026** with
a **one-year enforcement grace period** making 2026 a pilot year; **Vietnam**'s
**Law No. 134/2025/QH15** on AI effective **1 March 2026**; China's generative-AI measures
and **synthetic-content labelling** obligations; Google, Microsoft, IBM, Pearson and Byju's
as the commercial players, with China, India and Japan as the dominant national markets.

🔴 **The new measurement is a negative one, and it is worth as much as a find.** This pass
searched for APAC education AI supply **in Japanese and Korean** — the first time this KB
has searched in either.

- **Japanese returned nothing education-specific at all.** `教育 AI エージェント オープン
  ソース GitHub MIT ライセンス 2026` returned the **generalist** agent layer (Dify, LangGraph,
  CrewAI, OpenHands, OpenClaw star tables) plus one unrelated privacy tool. ⚠️ **Japanese is
  not an untried door onto Japanese education software; it is the same door as English.**
- **Korean returned five candidates and one licence.** Four were ungranted
  (`rlaalstn1504/langchain-ai-agent-edu`, `edu-agent-lab/edu-agent-lab`,
  `Choonholic/jpub_ai_agent`, `roomedia/ax-trend`) — all individual or coursework
  repositories, which is **exactly the publisher class trend 35 predicts will be
  ungranted**. The one licensed find, [`HKUDS/ClawTeam`](https://github.com/HKUDS/ClawTeam)
  (**MIT, 5.5k★**), is **agent-swarm infrastructure for software engineering, not education**
  — and is on no education shelf.

🔵 **What this means for an APAC engagement.** The region's **regulatory** surface is the
richest in the world and this KB tracks it well; its **permissive open-source education
supply** remains thin in a way that **two additional languages did not fix**. The standing
APAC plays are therefore unchanged and still rest on assets found through other channels:
**Sunbird** (MIT, India/DIKSHA, nine-figure scale), **Coursemology** (MIT,
NUS/Singapore), **AI Verify** (Singapore) via **P31**, the **AI4Bharat** and **SEA-LION**
language stacks, and **P26** for intermittent connectivity.

🔴 **`gitee.com` — the China-domestic forge, and the single most likely home of Chinese
education software — is unreachable from this environment** (403 at the egress proxy).
Any statement this KB makes about Chinese open-source education supply is made **without
access to the forge where it would live**. Declared, not inferred.


#### Fourteenth-pass additions, 2026-10-06 — five placed assets, and the sovereignty constraint priced

🟢 **APAC was the highest-yielding region of this pass, and the channel was the platform's
own name** (`agents/trending.md`, fourteenth pass). Five assets, placed by the institution
they integrate with:

| Asset | Licence (payload) | Country | Why it matters here |
|---|---|---|---|
| [ictinnovations/ictexam-mcp](https://github.com/ictinnovations/ictexam-mcp), 16★ | 🟢 **MIT** | Pakistan | **A vendor shipping MIT into the auto-grading gap.** Exam authoring, delivery and auto-grading; reads exams, gradebooks, per-question item analysis; **writes off unless explicitly enabled**. Corporate holder (ICT Innovations), on npm. |
| [SonAIengine/ku-portal-mcp](https://github.com/SonAIengine/ku-portal-mcp), 13★ | 🟢 **MIT** | Korea | Korea University's KUPID portal. On PyPI. |
| [kc0506/ntucool](https://github.com/kc0506/ntucool), 10★ | 🟢 **MIT** | Taiwan | NTU COOL: one binary = CLI + MCP + SDK, **plus a Claude Code plugin**. ⚠️ Self-declared unofficial. |
| [haanhtuandev/vgu-mcp](https://github.com/haanhtuandev/vgu-mcp), 10★ | 🔴 **none** | Vietnam | Vietnamese-German University. Ungranted. |
| [kesaruhasun/mcp-sliit-courseweb](https://github.com/kesaruhasun/mcp-sliit-courseweb), 6★ | 🔴 **none** | Sri Lanka | SLIIT. Ungranted. |

🔵 **Three of five carry a grant, and the two that do not are both university portals in
emerging markets.** That is the regional licensing-hygiene pattern this KB has recorded
twice before, reproduced a third time with new addresses — and it is still a one-commit ask.

⚠️ **The auto-grading asset is the commercially significant one.** Trend 7 has carried
assessment as *the regulated frontier and the tooling gap* for the whole life of this KB. A
company — not a student — has now published an MIT MCP server for a commercial auto-grading
platform **with writes gated by default**. The gated-write design is the thing to copy
whether or not the client ever touches ICTExam.

**Adoption and constraint figures read this pass:**

| Metric | Value |
|---|---|
| APAC governance leaders naming AI adoption a top 2026 priority | **48%** |
| Organisations in Asia with AI in one or more areas of operations | **57%** |
| APAC businesses citing **insufficient infrastructure for real-time data processing** as the barrier | **49%** |
| Share of APAC firms whose infrastructure choices sovereignty is expected to shape | **~half** |

🔵 **Read those two middle rows together and the regional opportunity is an architecture, not
a product.** Adoption is majority-done; the stated blocker is infrastructure, and sovereignty
is what decides the infrastructure. That is the same stack this KB already specifies for
EMEA — open-weight inference, retrieval in-region, no student data leaving the institution —
sold into APAC against a **capacity** argument rather than a compliance one. **P16 (the
all-MIT national/state stack) and P19 (ASEAN mother-tongue tutor) are the patterns; this
pass adds the portal-wrapper channel that places them at a named institution.**

**Regulatory direction, as measured this pass:** APAC is converging on common principles —
safety, transparency, accountability — with governments taking cues from early movers, and
Singapore's consultations on AI use in financial institutions (transparency, accountability,
risk oversight) read as the template other sectors will be held to. Education-specific rules
remain thinner than the enterprise ones, so **the compliance instrument in this region is
still the client's own governance committee** rather than a regulator — which is why the
artefact, not the certificate, is what closes the deal.


#### Twentieth pass of 2026-10-06 — the transition-provision channel: Vietnam gives education 2027-09-01, and Korea splits its own deadline

🟢 **Vietnam's education date is eighteen months later than the one this KB's summary tables
carried.** The law (**134/2025/QH15**) is in force from **2026-03-01**, but the transition regime
gives **existing systems until 2027-03-01**, and **health, education and finance until
2027-09-01**.

🔵 **The instrument set, now recorded properly** — and this corrects a terminology error in
`agents/top.md`, which calls it "Decree 33":

| Instrument | What it is | Dates |
|---|---|---|
| **Decision 33/2026/QĐ-TTg** | a *Quyết định* of the **Prime Minister** carrying the list of **46 high-risk AI systems across six sectors** | issued **2026-06-30**, effective **2026-08-15** |
| **Decree 142/2026/ND-CP** | a *Nghị định* of the **Government**: one-stop portal, national AI database, three-tier classification and conformity assessment, labelling and watermarking, three-level sandbox — 8 chapters, 46 articles | issued **2026-04-30**, effective **2026-05-01** |

🔴 **Education is three of the 46**: AI providing **self-learning content from uncontrolled data
sources**; AI that **automatically assesses, grades or ranks students**; and AI that **monitors or
analyses learner behaviour using biometric data** — facial recognition, eye tracking. The six
sectors are education (3), ethnic and religious affairs (7), healthcare (2), banking (2), judicial
proceedings (1) and transportation (31).

🔴 **One Vietnamese deadline has already passed, and it is procedural: Decree 142 required a notice
plus a transition plan filed on the one-stop portal within 60 days of 2026-05-01 — before
2026-06-30.** ⚠️ **So a client in this market may believe it has until 2027-09-01 while already
having missed the gate that preserves it.** 🟢 **For a Vietnamese engagement the first week is not
planning, it is establishing what was filed and what was not** — which is a discovery deliverable
with a clear scope and an obvious follow-on.

🔵 **Korea splits in a way that changes sequencing.** The Framework Act took effect **2026-01-22**;
the **enforcement decree and amendment effective 2026-07-21** turned high-impact duties into real
duties; **fact-finding investigations and administrative fines are deferred at least one year**
(→ ~**2027-07-21**, maximum fine KRW 30m ≈ US$21k). 🔴 **But the labelling duty for generated content
has no grace period at all.** ⚠️ **So in Korea the labelling limb ships now and the governance limb
is a 2027 programme** — and because the fine is small, the grace period is worth more than the
penalty it defers, which is an argument for doing the work on the schedule rather than against it.

#### Twenty-second pass of 2026-10-06 — two permissive APAC rows from one sweep, and the ceiling has not moved

This KB's fifth pass found the first India-, LATAM- and ASEAN-placed permissive education projects
and recorded that **all three sat at 0–9★** — the finding being the ceiling, not the discovery. One
GitLab sweep adds two more, and the ceiling holds:

| Row | Licence (payload) | ★ · activity | Country | What it is |
|---|---|---|---|---|
| [`cjaikaeo/elabsheet`](https://gitlab.com/cjaikaeo/elabsheet) | 🟢 **BSD-2-Clause** | **14** · 2026-09-19 | Thailand | Exercise/exam platform with **automatic grading**, holders named in the payload. 🟢 The most permissive assessment asset in this KB |
| [`yoockh-group/Edusaku`](https://gitlab.com/yoockh-group/Edusaku) | 🟢 **Apache-2.0** | 0 · 2026-05-18 | Indonesia | **Offline-first** AI education assistant for remote areas, React Native, on-device model |

🔵 **Why BSD-2 in particular matters here.** APAC's buying criterion in this KB's record is
**sovereignty**: a ministry wants to fork, localise and run a system without publishing the result or
asking anyone. BSD-2-Clause is the shortest grant that allows exactly that — shorter than MIT in
obligations and with no patent clause to negotiate. **A ministry-scale grading platform can be built
on `elabsheet` without a single licence conversation.** ⚠️ Against that: **14★, two named
maintainers, 2013 copyright line.** Treat it as a specification and a working reference, and budget
to own the fork.

**The regulatory and model picture this pass re-read:** India signalled in **July 2026** that it may
pursue **dedicated AI legislation** on a risk-based model; Japan's promotion-style **Act on
Promotion of R&D and Utilization of AI-Related Technologies** (May 2025, in force June 2025) remains
the light-touch pole; China's **labelling measures for AI-generated content** have been effective
since **September 2025**. Singapore leads regional diffusion and has committed to AI-in-education
training for teachers at all levels **by 2026**. Every major APAC economy now runs a domestic LLM
programme — **Sarvam** (India, 105B, 22 Indian languages), **SEA-LION** (Singapore), **ILMU**
(Malaysia), **Sahabat AI** (Indonesia), **HyperCLOVA X Think** (Korea), **NTT Sarashina** (Japan) —
which is why the mother-tongue tutoring patterns in `compose/patterns.md` have a model layer in this
region and not in LATAM.
### LATAM

- **Teacher adoption is ahead of institutional readiness, sharply.** In Chile and
  Brazil **more than 50% of teachers already use AI tools, while fewer than 10%
  of institutions in the region have formal guidelines and sufficient capacity**
  to integrate them with clear criteria. That gap is the engagement.
- **UNESCO launched the Observatory on Artificial Intelligence in Education for
  Latin America and the Caribbean on 14 April 2026** — a regional platform to
  help states integrate AI with a focus on equity and quality. A credible anchor
  partner and a source of procurement momentum.
- **Enterprise AI deployment regionally sits at 47%.** Only Brazil (65.89), Chile
  (63.19) and Uruguay (62.21) place in the global top 50.
- **Regulation:** Brazil is the regional bellwether with **PL 2.338/2023**, a
  comprehensive horizontal, risk-based statute with transparency and supervisory
  architecture. **Mexico** added an opt-out requirement for automated
  decision-making in its latest data protection law, and its Congress is pushing
  labour and copyright amendments covering image rights and AI.
- **Constraints are structural, per CEPAL/ECLAC:** gaps in talent, investment and
  governance, with advanced AI training concentrated in a few countries and the
  **talent gap relative to the global average widening since 2022.**
- **Opportunity:** institutional capability, not just software — governance
  frameworks for the >90% of institutions that lack them, teacher enablement at
  scale, and low-cost deployments that respect connectivity and budget reality
  (Kolibri + ricecooker, fully MIT; Chamilo for Spanish-first public sector).
  Brazil's PL 2.338 readiness work mirrors the EU AI Act engagement and the
  artefacts transfer.

**New this pass (2026-10-06):**

- **Hard survey numbers for higher education, from the Digital Education Council
  AI in Higher Education LATAM Survey 2026:** **92% of students** and **79% of
  faculty** are actively engaging with AI, and **94% of faculty** expect to use it
  in future teaching. Adoption is effectively universal — but **88% of faculty
  report only "minimal" to "moderate" engagement**, i.e. adoption has not become
  pedagogical integration.
- **That 92/79 vs 88 split is the sharpest opportunity statement in this KB.**
  The region does not need an adoption campaign; it needs depth — curriculum
  redesign, assessment redesign and faculty capability. Selling "get your teachers
  using AI" into LATAM higher ed is selling something they already have.
- **Anchor institutions for a regional play:** the survey was run by the Digital
  Education Council with the **Institute for the Future of Education at
  Tecnológico de Monterrey**, supported by the **AI Global Education Network
  (AIGEN)** and the **Educational Innovation Network (RIE360)**. With UNESCO's LAC
  Observatory (14 April 2026), these are the credible doors into regional
  procurement.
- **The regulatory map is fragmenting, not converging** — Brazil's PL 2.338/2023,
  Chile's framework, Colombia's CONPES and Mexico's sectoral rules are all moving
  at different speeds. Plan per-country, not per-region.
- **Colombia is further ahead than its profile suggests:** it adopted a national
  AI policy via **CONPES 4144 (February 2025)** — a government-wide programme with
  budgeted actions through 2030 covering capacity building, adoption and ethical
  guardrails. A funded national programme is a procurement signal; Colombia
  belongs on the target list alongside Brazil, Chile and Mexico.
- **UNESCO's warning is the sales argument:** LAC higher-education institutions
  are increasingly using generative AI for teaching, learning and research while
  lacking policies to govern it, and the agency has flagged that the absence of
  institutional guidelines raises misuse risk and leaves staff uncertain about
  acceptable use. Governance is the entry engagement; the platform work follows.

**New in the third pass (2026-10-06):**

- **The governance gap now has an institutional number, and it is the sharpest
  single statistic in this KB: 87% of LATAM higher-education institutions use AI in
  at least one area of their activities, and only 26% have a formal AI strategy.**
  Earlier passes carried "fewer than 10% have formal guidelines and sufficient
  capacity", which is a different and stricter measure. Use both and say which is
  which: **87/26** is the strategy gap, **>50% of teachers in Chile and Brazil vs
  <10% of institutions ready** is the capability gap. The second is the harder
  problem and the longer engagement.
- **LATAM faculty are measurably more positive about AI than the global average:
  72% report "positive" or "very positive" views, against 57% globally.** Combined
  with 79% of faculty using AI in teaching — **18 points above the global figure
  recorded in 2025** — the region is an *enthusiasm-rich, governance-poor* market.
  That is an unusual and favourable shape: the resistance that slows EMEA
  engagements is largely absent, and what is missing is structure.
- **Uruguay became the first Latin American country to sign the Council of Europe's
  Framework Convention on Artificial Intelligence and Human Rights, Democracy and
  the Rule of Law (2025).** This matters more than its market size: a Council of
  Europe convention signatory is committing to a governance vocabulary that is
  **interoperable with the EU's**, so compliance artefacts built for an EU AI Act
  engagement transfer to Uruguay with far less rework than to Brazil's PL 2.338 or
  Mexico's sectoral rules. Uruguay is small (62.21, third in the region's global
  top-50 placings) and is now the **cheapest bridgehead for reusing EMEA
  compliance IP in LATAM.**
- **The regional pioneer set is consistent across sources:** Chile, Brazil and
  Uruguay, on data availability, governance frameworks and infrastructure — with
  **Chile the standout through CENIA**, the national AI centre behind Latam-GPT.
- **The supply side is still empty, and the fourth pass of 2026-10-06 both
  weakened and re-established that claim.** LATAM demand is the best-shaped in this
  KB; **indigenous open-source supply remains zero.** Two updates:
  **(1) The gap's strongest single piece of evidence has been withdrawn as
  unsound.** Three passes cited `planejaia/OpenMAIC-Brasil` — a "Brazil-origin
  multi-agent classroom" that 404s — as lead evidence. The upstream is
  **Tsinghua's [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC), MIT,
  40.0k★**. The name was never Brazilian, so it was never evidence about LATAM. **A
  `-Brasil` suffix is a string an author typed, not a provenance claim.**
  **(2) The gap survives anyway, on a channel that does not depend on a filename.**
  The same pass searched in **Spanish and Portuguese** — a language channel no
  earlier pass had used — and returned **zero LATAM-origin projects**. Four
  independent channels now agree. A finding that outlives the removal of its best
  evidence is the firmest kind in this KB.
  **Commercially:** the region buys and adapts rather than publishes, so a LATAM
  engagement starts from **Chinese, US and European permissive code plus
  localisation**, and there is no local community to co-develop with. The
  Portuguese/Spanish localisation layer over OpenMAIC is an **unclaimed, concretely
  sized build** — and the one place where contributing upstream would make Globant
  the originating voice in a vacuum it has now confirmed four times.


#### Fifth pass, 2026-10-06 — the governance gap is now measured, and it is the engagement

This KB has argued the LATAM opportunity from adoption anecdotes and an absent
code shelf. Both are now replaced by primary-research numbers, and they size the
opportunity far more precisely than anything recorded before.

**UNESCO IESALC regional study**, launched **9 September 2026** during **UNESCO
Digital Learning Week 2026** — **200 higher-education institutions across 19
Latin American and Caribbean countries**:

| Measure | Value |
|---|---|
| Institutions using AI in at least one area of activity | **87%** |
| Institutions with a **formal AI strategy** | **26%** |
| Institutions with clear policies, governance structures and monitoring/evaluation frameworks | **fewer still** |
| Institutions reporting formal AI guidance — **LAC** | **45%** |
| Institutions reporting formal AI guidance — **Europe and North America** | **70%** |

**Digital Education Council, AI in Higher Education LATAM Survey 2026** —
delivered with the **Institute for the Future of Education at Tecnológico de
Monterrey**, with outreach through **AIGEN** and **RIE360**:

| Measure | Value |
|---|---|
| Students actively engaging with AI | **92%** |
| Faculty actively engaging with AI | **79%** |
| Faculty expecting to use AI in future teaching | **94%** |
| Faculty self-reporting **"minimal" to "moderate"** engagement | **88%** |

**Read the two together and the engagement writes itself.** Adoption is
near-universal and *shallow* — 92% of students using AI against 88% of faculty
still at surface-level engagement — and **61 percentage points separate the
institutions using AI from the institutions with a strategy for it**. That is not
a technology gap. It is a **governance-and-capability gap**, in a region where
only 45% of institutions have formal guidance against 70% in Europe and North
America.

**The sellable shape, and it is not a tutor.** A LATAM higher-education
engagement should lead with **AI governance enablement** — institutional policy,
oversight structures, faculty capability, monitoring and evaluation — with the
technology build following it. This is the opposite of how this KB's patterns are
ordered, and the numbers say so clearly. **Pattern P6 (client capability build) is
the LATAM entry point; P1 follows it.** Both UNESCO IESALC and the Digital
Education Council are citable, independent, and dated inside the last month —
which makes this the best-evidenced regional claim in this KB.

**National policy, dated:** **Chile** has classified AI uses by risk with
governance measures scaled to risk and a supervisory model tied to its
forthcoming **data protection authority** — the first LATAM regime structurally
comparable to EU Annex III tiering. **Colombia** adopted national AI policy via
**CONPES 4144** in **February 2025**, a government-wide programme with actions
and **budget through 2030**. Colombia is the one LATAM jurisdiction where both a
funded national policy and a publicly-funded permissive education project (see
below) now exist.

**And the code gap has an address.** The firmest gap in this KB — "no LATAM-origin
permissive open source education project" — **is refuted**:
[LabSirius/TutorIA](https://github.com/LabSirius/TutorIA), **MIT**, Universidad
Tecnológica de Pereira, Sirius research group, funded under Colombia's **SNCTI**,
specifying an Open edX side-car tutor for **rural higher education in Risaralda**.
It has **4 commits and every code path in its own documented tree returns 404**.

**So the gap was never about interest — it was about delivery capacity.** A
Colombian public university, with public science funding and a named pedagogical
director, independently specified **this KB's default pattern P1** and has not
built it. That is a partnership lead, a validation of the P1 shape, and the single
most concrete LATAM entry point this KB has ever recorded. **Do not fork it.**



#### Sixth pass, 2026-10-06 — the voice and language layer

**Adoption is genuinely high; the constraint is capital and infrastructure, not
appetite.** Latin America is the **third-largest market worldwide for generative
AI application downloads** despite less access to capital. **99% of LATAM startups
use AI in internal operations and 85% integrate it natively** into their main
product, while **fewer than 25% build their own models** — OpenAI (89%), Gemini
and Claude dominate integrations, with **edtech named among the most disruptive
sectors** (Ednova cited). For higher education specifically, **UNESCO IESALC**
surveyed **200 institutions across 19 countries between August and October 2025**
over five dimensions — teaching and learning, research, community engagement,
administration and governance — which is the most credible regional baseline
available and worth citing directly in proposals.

**Regulation is fragmented and that cuts both ways.** Multiple countries operate
under differing or absent frameworks, with the IADB arguing for an enabling
regional framework; the **EU AI Act's progressive entry from August 2026** is
becoming the de facto reference for cross-border operators. Fragmentation creates
opportunity and **normative inconsistency risk** for anything sold across borders.

**What this pass opens here:**

- **Offline voice tutoring is deliverable in Spanish and Portuguese today
  (P18).** `sherpa-onnx` (**Apache-2.0**) supplies STT, TTS, diarization and VAD
  on a Pi, a low-end laptop or an Android tablet **with no connectivity**, on top
  of Kolibri (**MIT**). Given that <25% of the region's players build their own
  models and the dominant pattern is a paid API call, **a voice tutor with no
  per-token cost and no connectivity requirement is a genuine differentiator**, not
  a parity feature.
- **The Portuguese-language asset is still Apache-2.0 — but it is no longer
  LATAM-maintained, and the KB should say so.**
  [Tucano](https://github.com/Nkluge-correa/Tucano) was Brazil-origin, Apache-2.0
  and peer-reviewed in *Patterns*; it was **archived on 2026-02-24**. **Tucano 2**
  (0.5–3.7B, Apache-2.0) continues under the **University of Bonn** Polyglot
  initiative. The model remains usable for a Brazil engagement; **the maintainer,
  funding and roadmap are now European.** "LATAM-origin" was true of Tucano 1 and
  is not true of Tucano 2 — do not carry the old label forward.
- **The pattern across two passes is consistent: LATAM demand is real, LATAM
  supply of permissive assets is not.** The fifth pass found the region's first
  permissive education project (Colombia's TutorIA, MIT) to be **a README and a
  licence with no code**; this pass finds its Portuguese model archived and
  succeeded from Germany. **The regional opportunity is to be the builder**, with
  SALT (Uganda) as the worked example of how a region built its own corpus and
  licensed it properly.

#### Seventh pass of 2026-10-06 — declared: no new LATAM code, and the reason is the channel

**Stated explicitly, because silence looks exactly like coverage.** This pass's
new channel was **native-language search**, and the languages added were
**Japanese, Korean, Arabic, Bahasa, Thai and Vietnamese**. **Spanish and
Portuguese were not re-run**, because the fourth pass had already used that
channel and the seventh pass's purpose was to open an unused one.

**So this pass contributes no new LATAM repository, and that is a scope decision
rather than a measurement.** It is not evidence for or against the LATAM gap.
The state of the region is unchanged from the sixth pass and should be quoted
from there:

- [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) — MIT, Universidad
  Tecnológica de Pereira, Colombia, SNCTI-funded, specifies this KB's **P1**
  architecture, and **every code path in its own documented tree 404s**. A
  partnership lead and an existence proof; **never a fork target**.
- [`Nkluge-correa/Tucano`](https://github.com/Nkluge-correa/Tucano) — Apache-2.0,
  Portuguese-native, peer-reviewed in *Patterns*, **archived 2026-02-24**;
  Tucano 2 continues under the **Bonn-hosted** Polygl0t initiative. Portuguese
  open modelling did not die, it **relocated to EMEA**.
- Earlier passes located **12 repositories in LATAM** against a "zero
  repositories" claim this KB had carried for four passes, and the fifth pass
  recorded LATAM as the **most saturated** region on the intel axis — 7 probes,
  0 new facts.

**The actionable read is unchanged and worth repeating, because it is the
commercial one.** LATAM demand is measured and large — **79% of faculty using
AI**, **87% of institutions** using it in at least one area, and only **26% with
a formal AI strategy**, with fewer than **10% of institutions** holding formal
guidelines. **The regional opportunity is governance, localisation and
deployment, not upstream code** — and the governance deficit is now the
best-evidenced commercial fact about the region in this KB.

**For the next pass:** the LATAM channel to open is **not** another
Spanish-language repository search, which has been run twice and saturated. It is
the one this pass used for APAC — **search the language substrate**, for the
indigenous and regional languages (Guaraní, Quechua, Nahuatl, Aymara) that a
ministry engagement would actually ask about. That noun has never been queried
for LATAM, and in APAC changing exactly that noun falsified a standing gap.


#### Eighth pass, 2026-10-06 — the regional diagnosis changes: the constraint is licence reliability, not supply

Four passes told a client *"nothing exists upstream in this region; we build."*
**That line is now wrong, and the replacement is more useful.**

**What the eighth pass established (full evidence in `agents/trending.md`):**

| Asset | Licence | Maturity | Where |
|---|---|---|---|
| `LabSirius/TutorIA` | **MIT** © Grupo Sirius | **13-page requirements spec + 5-layer architecture; no code** | Universidad Tecnológica de Pereira, **Colombia** |
| `caiuc/equipo-19` (EduFlow) | **MIT** © CAi UC *(holder flagged)* | **Running code**, 8-hour build, 1★ | Pontificia Universidad Católica de **Chile** |
| `neuralmind-ai/portuguese-bert` (BERTimbau) | **MIT** © NeuralMind | **886★, genuinely adopted** | NeuralMind, **Brazil** |
| `Llamacha/IWSLT2023_Quechua_data` | payload Apache-2.0 / README **CC BY-NC-ND** | Corpus, scope-conflicted | Llamacha, **Peru** |
| **Latam-GPT** | **Llama 3.1 Community License** © Meta — **not OSI** | Open-weights, 70B | CENIA, **Chile**, 60+ institutions / 15 countries |

**The opportunity, stated as an engagement shape.** The region has published
**the design and the licence, not the product.** So a LATAM engagement is a
**productionisation** engagement with citable local provenance — which prices and
positions very differently from a greenfield build, and gives Globant two named
partnership leads (**UTP Pereira**, **PUC Chile**) where it previously had an
absence.

**Three region-specific facts that are new to this file and are directly
billable:**

1. **Colombia's data-protection anchor, from TutorIA's own RNF-05:** student
   personal data, learning profiles and interaction history must be protected
   *"conforme a la **Ley 1581 de 2012 (Habeas Data)**"*, with **TLS** in transit
   and **AES-256** at rest. Processing minors' data without a compliant policy
   exposes the institution to **Superintendencia de Industria y Comercio (SIC)**
   enforcement. Pair this with **CONPES 4144** (already recorded here) and
   Colombia becomes the most *specifiable* LATAM jurisdiction in this KB —
   good news for a fixed-scope compliance workstream.
2. **A hard low-resource envelope, also from TutorIA:** **2 GB RAM, 3G
   connectivity** as acceptance criteria. This file previously described LATAM
   rural access with adjectives; it now has numbers a proposal can be tested
   against, and **EduFlow demonstrates they are achievable** (~8 KB per
   10-exercise assignment, IndexedDB + Service Worker, auto-sync).
3. **Latam-GPT is not open source, and nearly every account of it says it is.**
   Usable and valuable for Spanish/Portuguese regional grounding; **not
   relicensable, not presentable to a client as open source**, and it inherits
   Meta's Acceptable Use Policy and the 700M-MAU clause into the client's
   product. *Provenance caveat: single-source — `huggingface.co`,
   `latamgpt.org`, EC OSOR and `opensourceforu.com` are all EGRESS_BLOCKED here
   (4/4), so the model card was not read. Confirm before any deliverable.*

**The governance gap, re-read against this supply picture.** UNESCO IESALC
(already recorded here: 200 institutions, 19 countries, **87%** using AI, **26%**
with a formal strategy, **45%** with institutional guidance against **70%** in
Europe and North America) has until now been read as a demand signal for
policy work. **It now reads as the same failure as the licensing gap, one level
up:** the region produces the capability and omits the governing document —
whether that document is an institutional AI policy or a `LICENSE` file.

**And the eighth pass found the cheapest intervention in this KB.** **CAi UC**
(PUC Chile) made an **OSI licence and a root `LICENSE` file a condition of
evaluation eligibility** in HaCAIthon 2026, and **20 licensed team repositories
appeared in eight hours** — 19 MIT, one AGPL-3.0, four of them education-track.
Meanwhile the region's indigenous-language layer — AmericasNLP corpora for
Aymara, Nahuatl and Quechua, ASR for five languages, MT for Peru — has **nine of
eleven repositories with no `LICENSE` payload at all**, including **three
AmericasNLP editions**.

**So: sponsoring or co-writing the licence clause in a university hackathon's
rules — in São Paulo, Lima, Bogotá, and on the same argument in Nairobi — is a
concrete, low-cost, prospective fix for the one constraint that blocks both LATAM
and MEA.** It is cheaper than filing upstream `LICENSE` issues one repository at
a time, and it works on repositories that do not exist yet. Caveat worth
carrying into any such sponsorship: CAi UC's template put **the organiser's name
in the copyright line**, which is the wrong holder — a sponsored clause should
make the authoring team the holder.

#### Ninth pass, 2026-10-06 — the governance gap is now measured by a multilateral instrument, across 19 countries

For four passes this KB asserted a LATAM **adoption-versus-governance** gap, and
the fifth pass called it *"measured"* on the strength of national-level material.
It is now measured properly, by a UN-system survey, and the numbers are worse
than the KB's own framing implied.

**UNESCO IESALC + UNU-IAS working paper**, *AI Implementation in Higher Education
in Latin America and the Caribbean*, Arianna Valentini, published **1 September
2026** — a regional survey of **200 higher education institutions across 19 LAC
countries**, fielded **August–October 2025**, mapping five dimensions: teaching
and learning, research, community engagement, administration, governance.

| Dimension | Institutions adopting |
|---|---|
| Teaching and learning | **73.5%** |
| Research | **57.0%** |
| Administration | **34.1%** |
| Community engagement | **20.0%** |

| Governance condition | Institutions with it |
|---|---|
| A formal AI strategy | **26.0%** |
| Institution-wide AI policies | **18.5%** |
| A **dedicated AI budget** | **8.0%** |
| **Formal evaluation mechanisms** | **9.0%** |

⚠️ **Tier 2.** `unu.edu` is **EGRESS_BLOCKED** here, so the paper itself was
**not read**; these figures are consistent across two independent search
summaries. Confirm against the paper before use in a client deliverable.

**Read the two columns against each other, because that is the engagement.**
**73.5%** of institutions have AI in teaching and learning. **18.5%** have a
policy covering it. **9%** can evaluate whether it works. **8%** have money
allocated to it. This is not an adoption problem and not an awareness problem —
it is **deployment without governance, at scale, measured, and published by a
UN-system body the client's own ministry will recognise.**

**What it changes for this KB.** Three things:

1. **The LATAM diagnosis gets its number.** The eighth pass reframed LATAM as a
   *productionisation* region — *"the region has published the design and the
   licence, not the product."* These figures place the missing layer precisely:
   not engineering capability, but **strategy, policy, evaluation and budget.**
   The first three are consulting deliverables. The fourth is the thing a
   business case has to create.
2. **The 9% figure is the sharpest sales instrument in this KB.** *Nine percent of
   LAC universities can tell whether their AI works.* Pair it with the measured
   fact that **no Apache-2.0 tutoring-quality evaluator exists today** (0
   repositories, this pass) and the gap is not the client's failing — it is a
   market-wide absence with a funded fix arriving in 2027. That reframes an
   evaluation engagement from remedial to leading.
3. **It is citable in Spanish and Portuguese, from a multilateral source.**
   UNESCO IESALC is the region's own higher-education institute. For a ministry
   or rectorate audience this outranks any vendor report, and it is the kind of
   citation that survives a procurement committee.

**The engagement shape, stated plainly:** lead with **governance and evaluation**,
not with a tutor. The region has the adoption (73.5%) and lacks the instruments
(18.5% / 9% / 8%). A LATAM engagement that delivers an AI strategy, an
institution-wide policy aligned to the regional evidence base, and an evaluation
harness designed to accept Apache-2.0 benchmarks as they land (**P23**) is selling
into a measured deficit rather than a speculative one — and the **productionisation**
posture from the eighth pass (TutorIA's MIT specification, EduFlow's MIT offline
core, PUC Chile and UTP Pereira as named leads) is how you build on top of it.

#### Tenth pass of 2026-10-06 — the governance numbers get sharper, and a Caribbean ministry gets a vendor first

**The UNESCO IESALC / UNU-IAS survey, extended.** The ninth pass recorded part of
this instrument; the full set is now corroborated at Tier 2 — **200 higher
education institutions across 19 countries of Latin America and the Caribbean,
surveyed August–October 2025**:

| Adoption, by domain | Share |
|---|---|
| Teaching and learning | **73.5%** |
| Research | **57.0%** |
| Administration | **34.1%** |
| Community engagement | **20.0%** |

| Governance | Share |
|---|---|
| Formal AI strategy | **26.0%** |
| Institution-wide AI policy | **18.5%** |
| **Formal evaluation mechanisms** | **9.0%** |
| Dedicated AI budget | **8.0%** |

**73.5% adoption against 9.0% evaluation and 8.0% budget.** The new figure this
pass is **26.0% with a formal AI strategy** — which sits *above* the 18.5% with an
actual institution-wide policy, so roughly a third of institutions that have
written a strategy have not turned it into policy. The engagement that follows
from this table is **governance-and-evaluation first**, and it is buyable: it needs
an evaluation harness, an audit trail and a policy instrument, not a model.

**A Caribbean ministry is in a national AI-education programme with a proprietary
vendor.** **Trinidad & Tobago** is named in the first cohort of OpenAI's
**Education for Countries** (Tier 2) — the programme working directly with
ministries of education. This is the first LATAM/Caribbean national AI-education
engagement this KB has recorded, and it arrives in the region measured at **9%
formal evaluation mechanisms.** The vendor is arriving before the governance
capacity. **That ordering is the opportunity and the risk in one sentence**: the
region will be deploying national AI education programmes without the institutional
machinery to evaluate them, which is exactly the work an open, auditable
alternative can be sold as — and exactly the condition under which a closed one
becomes entrenched.

**Tier 1 confirmation, and it is a negative that now holds under a stricter
probe.** Nine of the 41 repositories re-probed this pass are the LATAM-placed
indigenous-language and hackathon repositories — the `AmericasNLP` shared-task
datasets (2021, 2023, 2024), `Llamacha/IWSLT2025_Quechua_data`,
`aoncevay/mt-peru`, `aoncevay/quechua-nlp`, `monirome/asr-indigenous-languages`,
`caiuc/proyectos-hacaithon-2026` and `vilcaaguilerandrea-oss/carrera-lectora`.
Every one was re-probed across **20 URLs** including both spellings of "licence"
and both `main` and `master`. **Not one carries a licence payload.**

The eighth pass's LATAM finding — *the capability is there, the grant is not* —
**survives a full retroactive re-probe** and can no longer be attributed to this
KB's own query defects. For a region whose indigenous-language capability is its
most distinctive technical asset, the blocker is **licensing, not capability, and
not this KB's ability to see it.** Obtaining grants on two or three of these
datasets is a higher-leverage regional action than any further search.


#### Eleventh pass, 2026-10-06 — measured in Spanish, the regional shelf does not exist, and that is the opportunity

**Measured, Tier 1, GitHub REST search, 2026-10-06:**

| Probe | `total_count` | What came back |
|---|---|---|
| `educación inteligencia artificial estudiantes plataforma stars:>5` | **0** | — |
| `educación IA aprendizaje` | **10** | **Every result 0–1★.** Highest: `Edwin1719/AvatarAcademy` (**1★**, **MIT**, payload verified — GPT-4o plus Tavus avatars for video tutors). The rest are coursework, a PE lesson generator, and `FreeHelado/neurax-ia`, **a satirical fake-documentary art project about a fictional AI-education company** — not software. |

**The Spanish-language education-AI repository channel on GitHub contains no
production asset.** Ten repositories, maximum one star, one of them deliberately
fictional. This is the fifth consecutive pass measuring the LATAM-origin shelf at
0–9★, and the first to measure it with a count rather than a ranked search page.

**The one real regional platform, and it is a good one.**
[`portabilis/i-educar`](https://github.com/portabilis/i-educar) — **GPL-2.0** (Tier 1,
payload read from branch **`2.12`**; `main` serves nothing), **718★ and 547 forks**,
Laravel/PHP, *"o maior software livre de educação do Brasil"*, tagged
`software-publico`. It is the most-forked platform on these shelves and it was
**missing from this KB's live files** until this pass. **GPL-2.0 carries no network
clause**: hosting a modified i-educar for a municipality triggers nothing, and a
public-sector buyer who wants the source is asking for exactly what the licence
delivers.

**Governance context re-corroborated this pass (Tier 2):** across 200 institutions in
19 LAC countries, AI adoption leads in **teaching and learning at 73.5%**, then
research 57.0%, administration 34.1%, community engagement 20.0% — while only **26%
have a formal AI strategy, 18.5% an institution-wide policy, 8% a dedicated AI
budget, and 9% any formal evaluation mechanism.** Regulation: **no unified regional
framework**; **Chile** leads with a National AI Policy since 2021 and pending
legislation; **Brazil** and **Colombia** have national strategies without sectoral
education regulation; most universities operate in a normative vacuum. Chile's
**CENIA** publishes the regional AI index and leads **Latam-GPT**.

**The opportunity, stated so it can be sold.** 73.5% are already using AI in teaching
and 9% can evaluate it. **The gap between adoption and evaluation is wider here than
in any other region in this KB, and the instruments that close it are free and
permissive** — Inspect (MIT) and Moonshot (Apache-2.0). The LATAM engagement is not
"adopt the regional shelf," because there is no regional shelf. It is: **deliver the
global permissive shelf with Spanish and Portuguese as first-class, offline-tolerant
by construction, data-resident by default, and with the evaluation mechanism the
other 91% do not have** — on i-educar or Moodle where the client is public sector,
and with the licence register written in the client's language.

#### Twelfth pass, 2026-10-06 — measured in Portuguese for the first time, the shelf is not thin, it is empty

The eleventh pass concluded: *"measured in Spanish, the regional shelf does not exist,
and that is the opportunity."* This pass **re-measured it in Spanish and then measured it
in Portuguese**, with `total_count` rather than a ranked page:

| Query | `total_count` | What came back |
|---|---|---|
| `tutor IA educación aprendizaje` (**Spanish**) | **3** | All **0–1★**. One **MIT** (`Edwin1719/AvatarAcademy`, 1★), one **AGPL-3.0** (`Elmaldelego/OPEN-TUTOR-IA`, 0★), and one that **does not resolve at all** (`junjie1005/Plataforma-IA-Educativa-Rutas-Personalizadas` — the index lists it, `git ls-remote` cannot reach it). **The live Spanish-language shelf is 2 repositories.** |
| `tutor inteligência artificial educação aprendizagem` (**Portuguese**) | 🆕 **0** | Nothing. |

🔴 **This is the sharpest LATAM finding this KB has recorded, and it is a language
finding, not a regional one.** Brazil is the largest education system in Latin America,
and **the Portuguese-language permissive AI-tutoring shelf does not exist** — it is not
sparse, not immature, not 0–9★. It is **zero**. Five previous passes measured "LATAM" and
found 0–9★; none of them measured the half of the region that does not speak Spanish, so
"thin" was the wrong word for a condition that is, in Portuguese, **absence**.

**What Brazil does have is copyleft and specific**, all verified from payloads this pass:

| Repo | Licence | What it is |
|---|---|---|
| [yunger7/enem-api](https://github.com/yunger7/enem-api) | **GPL-2.0** | An API over **ENEM** — Brazil's national secondary-school exam, the gateway to higher education. The highest-stakes assessment artefact in the region, and it is copyleft. |
| [caiocarvalhofre/moodle-mod_maici](https://github.com/caiocarvalhofre/moodle-mod_maici) | **GPL-3.0** | AI chat activity module for Moodle, Brazilian-authored. |
| `portabilis/i-educar` (recorded pass 11, branch `2.12`) | **GPL-2.0** | Brazil's largest free school-management platform. |
| [thiagoluzin/pemara-edu-mira](https://github.com/thiagoluzin/pemara-edu-mira) | **MIT** | 🟢 **The only Portuguese-language permissive asset in this KB.** 0★. Local classroom authoring and presentation for Brazilian basic education (6th-grade history first), **designed to run on a school LAN rather than the public internet**, with optional AI. Node 24 + Express + React + PostgreSQL. 0★ and a one-person project — but the *architecture* is the regionally correct one, and it is MIT. |

**The demand side is the inverse of the supply side, and that is the whole LATAM case.**
The 2026 Digital Education Council LATAM survey — **30,000+ responses across 29
institutions**, run with the **Institute for the Future of Education at Tecnológico de
Monterrey**, with **AIGEN** and **RIE360** — reports:

- **92% of students** and **79% of faculty** actively engaging with AI;
- **94% of faculty** expect to use AI in future teaching, consistently across experience levels;
- **61% of students fear AI misuse by peers**, raising fairness and academic-integrity concerns.

And **UNESCO** warns that higher-education institutions across Latin America and the
Caribbean are increasingly using generative AI **while lacking institutional policies to
govern it** — raising misuse risk and leaving academic staff uncertain about permitted use.

Nationally the map is **fragmenting rather than converging**: **Brazil's AI bill**,
**Chile's framework**, **Colombia's CONPES on AI** and **Mexico's sectoral rules** are all
moving at different speeds. Unlike the EU's single statute or Singapore's single harness,
there is **no regional instrument to build one compliance artefact against**.

🆕 **The structural read, stated so it can be falsified:** LATAM has **near-universal
adoption (92%), no governance layer, no regional instrument, and — in Portuguese — no
permissive code at all.** Every other region in this file has at least one of those four
filled in. The constraint is **not demand** and it is **not capability**; it is that
nothing reusable has been *published* in the region's second language.

**The LATAM opportunity, stated as work:**

1. 🟢 **Publish the Portuguese-language permissive asset.** `total_count: 0` means a
   competent MIT-licensed Portuguese tutoring or lesson-generation component has **no
   competitor to displace**. Globant is LATAM-rooted and Brazil is its largest regional
   market; this is the cheapest durable position available anywhere in this KB. The
   architecture to copy is `pemara-edu-mira`'s — **school-LAN deployment, offline-capable,
   optional AI** — because that is what the infrastructure actually supports.
2. **Institutional AI governance, at scale and at speed.** 92% adoption with no policy is a
   repeatable engagement per institution, and UNESCO's warning is the citable framing. The
   artefacts are the same ones Ohio's districts need — inventory, permitted-use rules,
   human-oversight procedure, integrity policy — which means the North America compliance
   package **ports**, translated.
3. **Academic integrity as the named deliverable.** 61% of students fear peer misuse. That
   is a student-demanded, faculty-supported workstream, and it is distinct from governance
   paperwork.
4. ⚠️ **Price the copyleft correctly rather than avoiding it.** ENEM tooling and `i-educar`
   are GPL-2.0; for a Brazilian public-sector client, publishing the fork is usually
   **acceptable and often preferred** (see pattern P28). The licence is not the obstacle in
   this region — **licence hygiene is**: two of the LATAM repositories probed this pass
   (`Kaiman-p/tutor-adaptativo-ia`, `mietiainvestigacion-creator/API-EduAdapt`) carry **no
   grant at all**, which is the same failure this KB has recorded in the region for five
   passes.

#### Thirteenth pass, 2026-10-06 — the Portuguese channel yields two MIT assets, at 2★ and 0★

🔵 **Re-verified unchanged:** the **Digital Education Council LATAM survey 2026** —
**92% of students** and **79% of faculty** actively using AI, **30,000+ responses across 29
institutions**, with **88% of faculty** reporting only *minimal* to *moderate* engagement;
**UNESCO's Observatory on AI in Education for Latin America and the Caribbean**, launched at
**ECLAC headquarters in Santiago**; **Chile's** risk-classified draft AI bill tied to its
forthcoming data-protection authority; **Colombia's CONPES 4144** national AI policy with
budgeted actions through 2030. The survey was delivered with the **Institute for the Future
of Education at Tecnológico de Monterrey**, **AIGEN** and **RIE360** — the named
institutional entry points for a LATAM engagement.

🟢 **New supply, honestly sized.** This pass ran the mandatory queries **in Portuguese**,
which had never been tried (passes 5–12 used Spanish). It produced **four candidates, two
licensed**:

| Repo | Licence | ★ | What it is |
|---|---|---|---|
| [`armandokeller/SAEP2026-Agentes-IA-e-Ferramentas`](https://github.com/armandokeller/SAEP2026-Agentes-IA-e-Ferramentas) | **MIT** | **0** | 8-step agent-engineering curriculum, **cloud-free** (Qwen 3.5-4B via LM Studio), MCP + human-in-the-loop. **Unisinos, Brazil.** |
| [`bonafe/inteligencia-aberta`](https://github.com/bonafe/inteligencia-aberta) | **MIT** | **2** | FastAPI + LangGraph + Qdrant + PostgreSQL multi-tenant agent platform, source traceability as a design goal. Brazil. **Not education** — shelved as a reference architecture. |

⚠️ **Two MIT assets at 2★ and 0★ is the LATAM finding, restated with a fourth language
behind it.** This KB's **trend 37** — *"measured by language rather than by region, the
LATAM supply gap is absence, not thinness"* — was derived from a **two-language**
instrument. Adding Portuguese did not overturn it; it **confirmed it on harder evidence**.
The region produces education AI work; it does not produce **licensed, adopted, reusable**
education AI work.

🟢 **And that remains the LATAM opportunity, now with a sharper edge.** Where there is no
incumbent permissive component, the first credible one sets the default — the position
**P32** (the Portuguese-language permissive component) was written for. Two things this
pass adds to it:

1. **`SAEP2026` is a usable enablement asset today**, star count notwithstanding. A
   **cloud-free, MIT, Portuguese-language** agent curriculum running a 4B model on a laptop
   is precisely shaped for a LATAM engagement where cloud spend and connectivity are the
   constraints — and for client-staff upskilling where data cannot leave the building.
2. **`inteligencia-aberta` is a worked sovereign stack by Brazilian authors**, independently
   arriving at the architecture **P5** and **P26** specify. Read it as a design review of
   this KB's own LATAM pattern.

🔵 **The region to watch for supply is not LATAM.** The most capable permissive AI-native
education platform found in thirteen passes is **Moroccan and state-funded**
(`open-tutor-ai-CE`, BSD-3-Clause — see EMEA above). A LATAM public-sector buyer asking for
a sovereign Spanish- or Portuguese-language tutoring platform is best served by
**localising that platform** — it already serves Ollama and local RAG — rather than waiting
for a LATAM-origin equivalent that this pass's evidence says is not coming soon.


#### Fourteenth-pass additions, 2026-10-06 — the supply measurement this pass failed to make, stated as a failure

🔴 **This pass did not measure LATAM's platform-integration tier, and the reason was a method
error, not an absence.** The probe was run as a single Boolean query —
`sigaa OR suap OR siga mcp server` — and returned **`total_count: 160,659`**: the generalist
MCP layer (`awesome-mcp-servers` 95.9k★, `headroom`, `private-gpt`, `playwright-mcp`).
**Boolean `OR` in GitHub repository search destroys specificity**, because the two
highest-volume words in the query (`mcp`, `server`) dominate the ranking. Every other region
in this pass was measured one platform name per query; LATAM was not.

**Writing this down rather than reporting the 160,659 as a result**, because an unmeasured
tier that looks measured is worse for an engagement than a declared gap. **SIGAA** and
**SUAP** — the academic and administrative systems of Brazil's federal universities and
federal institutes — are the region's real entry points into this channel, and they are the
first item of LATAM work for the next pass.

🔵 **The one LATAM asset the pass did surface, and it fails twice over.**
[`vnschneider/suap-mcp`](https://github.com/vnschneider/suap-mcp) — a SUAP integration,
Brazil — carries **no licence payload under 20 filenames**, and its `pyproject.toml` declares
**`AGPL-3.0-or-later`**. Both halves matter: there is **no grant to rely on today**, and if
the payload ever lands it is a **copyleft constraint**, not a permissive win. It is the only
Brazilian federal-systems wrapper found, and it is the only asset in this pass's entire set
whose *declared* licence would restrict a Globant deliverable.

🔴 **LATAM in the MCP Registry: zero of 102.** The registry census this pass
(`repos/trending.md`, fourteenth pass) filtered 11,505 unique servers down to 102 with
education vocabulary. **Not one is LATAM-placed.** The single Brazilian entry,
`br.com.lensas/optical-intelligence`, is optometry training — not education software. This is
the fourth instrument in this KB's history to return absence rather than thinness for the
region, and it is consistent with trend 37.

🟢 **The honest opportunity read, which is better than it sounds.** The region's dominant
platform is **Moodle**, and Moodle has the **second-deepest integration tier measured this
pass: 86 repositories**, led by permissive, payload-backed servers (`peancor/moodle-mcp-server`
MIT; `1alexandrer/moodle-mcp` MIT, 18★ 🆕; `Snaw80/moodle-mcp` MIT 🆕). **So the LATAM
engagement does not need a LATAM-origin asset to be well served** — it needs the MIT Moodle
side-car tier, which exists and is global, plus the offline-first delivery stack this KB
already specifies (P5, P21, P26).

**What the region's own supply gap does cost** is the thing a local asset would have carried:
Portuguese- and Spanish-language pedagogy, local curriculum alignment, and the
institution-specific administrative surface. Those stay **build**, and this pass's EMEA
finding says exactly how to price that build — a thin permissive wrapper over a public
national API (the Skolverket shape) is small, bounded and reusable, and nothing about it is
Nordic.

**Demand-side figures read this pass:**

| Metric | Value |
|---|---|
| LATAM startups using some AI solution (2026) | **99%** |
| LATAM startups with AI integrated **natively** into their main product | **85%** |
| Most disruptive applied-AI sectors named | fintech, healthtech, **edtech** (e.g. Ednova, Chile) |
| UNU / UNESCO working paper: higher-education institutions surveyed | **200 HEIs across 19 countries**, Aug–Oct 2025, five dimensions: teaching and learning, research, community engagement, administration, governance |

⚠️ **Regulatory fragmentation is the standing constraint for cross-border delivery**, and it
is structural rather than a phase: multiple countries operating under different or absent
frameworks, against an EU AI Act that took effect progressively from August 2026 with four
risk levels. For a studio this is a **portability requirement** on the governance artefacts,
not a reason to wait — build the pack once to the strictest regime in scope and re-use it per
country, which is what P13 and P24 already do.


#### Twentieth pass of 2026-10-06 — the transition-provision channel: Peru has a live, education-naming obligation, and Brazil has no statute

🟢 **This is the pass's regional surprise, and it cuts against this KB's standing LATAM posture that
the driver is a programme rather than a rule.**

| Market | Instrument | Status read this pass |
|---|---|---|
| **Peru** | Law **31814** + *reglamento* **DS 115-2025-PCM** | Reglamento published in *El Peruano* **2025-09-09**, in force **2026-01-22**. 🔴 **Sector obligations for health, EDUCATION, justice, security, economy and finance activated 2026-09-10.** Staged compliance **1–4 years from September 2025**, by sector and organisation size. Algorithmic-transparency mechanisms required for high-risk systems |
| **Brazil** | **PL 2338/2023** | ⚠️ **Still not law.** Senate approved **2024-12-10**; in the Chamber with status *"Aguardando Parecer"*, latest entry **2026-09-02**; rapporteur **Aguinaldo Ribeiro (PP-PB)** said on **2026-08-24** the vote comes **after the October elections** |
| **Uruguay** | Council of Europe Framework Convention on AI | First LATAM signatory — a commitment instrument, not a compliance deadline |

🔵 **What it gives a LATAM engagement that it did not have.** Exactly one market where a compliance
deliverable sells against **a date that has already bitten**, with **education named in the activated
set** — and in that one narrow respect Peru is **ahead of the EU**, whose Annex III §3 duties wait
until 2027-12-02.

⚠️ **It does not generalise, and a pitch that treats "LATAM regulation" as one thing will be wrong in
the region's largest market.** Brazil has no AI statute in force, so there the offer is **readiness**
— the same evidence pack, framed as what makes a later filing cheap rather than what discharges a
current duty. 🟢 **That framing is honest and it is also durable**: the pack is built once and
re-filed per country, which is the economics this KB already recorded for P13 and P24.

🔵 **The demand side, re-read this pass, is the reason the offer lands.** UNESCO/IESALC: **87% of
Latin American and Caribbean institutions use AI in at least one area of their activity, and only
26% have a formal AI strategy**; the Digital Education Council finds **79% of LATAM faculty using AI
in their teaching** while **88% report minimal-to-moderate engagement**. 🔴 **An 87%-adoption,
26%-strategy gap is a governance deficit, not a technology deficit** — and governance is the
deliverable this channel produces.

#### Twenty-second pass of 2026-10-06 — the LATAM gap, now measured in three languages instead of one

🔴 **This is a declared absence with a denominator, and it is the most useful thing this pass found
about the region.**

| Sweep | Terms | Unique projects | LATAM-origin education projects with a licence payload |
|---|---|---|---|
| English | 25 | **534** | **0** — one LATAM-*plausible* row, [`elizeubarbosaabreu/leitor-de-gabaritos`](https://gitlab.com/elizeubarbosaabreu/leitor-de-gabaritos) (**AGPL-3.0**), placed by Portuguese-language naming only, not by any declaration |
| **Spanish + Portuguese** | **16** | **141** (140 of them invisible to the English sweep) | 🔴 **0** |
| total | **41** | **674** | **0 permissive, 1 copyleft, placement inferred** |

⚠️ **The second sweep was run because the first one's terms were English-only — that was a real
defect in this pass's own instrument, and fixing it changed the answer's shape but not its
direction.** 140 of the 141 Spanish/Portuguese results were new, so the English sweep *was* blind to
the region. What the region returned is the finding:

| Candidate | What it is | Licence |
|---|---|---|
| [`ccsl-ufpa/educacaovigiada-org-br`](https://gitlab.com/ccsl-ufpa/educacaovigiada-org-br) | **"Educação Vigiada"** — the Federal University of Pará free-software centre's project on surveillance in education. Real, academic, Brazilian, five years old | 🔴 **none** |
| [`angeelrdz-group/nova-aula`](https://gitlab.com/angeelrdz-group/nova-aula) | Spanish-language full-stack education platform: courses, quizzes, analytics, Stripe. Committed 2026-10-05 | 🔴 **none** |
| [`evertonwilliam/plataforma-de-educacao`](https://gitlab.com/evertonwilliam/plataforma-de-educacao) | Portuguese AI-guided software-engineering training track | 🔴 **none** |

🔴 **So the LATAM supply gap is not an absence of building — it is an absence of *granting*.** Three
real Spanish- and Portuguese-language education projects, one of them from a federal university,
**not one carrying a licence payload.** That is trend 24's licence-hygiene finding with a regional
signature, and it is actionable in a way an empty result never is: these projects cannot be adopted,
contributed to, or resold by anyone — including their own institutions' partners — until someone adds
one file.

**Against the market context, the contradiction is sharp.** Brazil and Mexico lead regional AI
adoption at **76%** and **70%** of digital users; **38% of Latin American organisations already use
open-source AI** (Mexico **65%**, Brazil **46%**); **Brazil ranks 4th globally in open-source
contribution**. Regulation is converging — Brazil's **PL 2338/2023** AI framework approved with
transparency, impact-assessment and high-risk registration duties, and a **Q2-2026** wave across
**Chile** (law in process), **Colombia** (MinTIC guidelines), **Mexico** (INAI directives) and
**Argentina** (draft law). 🟢 **A region that contributes that heavily to open source and uses
open-source AI that widely is not short of capability.** 🔴 **It is short of licensed education
assets, measured now across 674 projects and three languages.**

🟢 **The engagement that follows, and it is small and immediately sellable:** a **licence-grant
clinic** — for a university or ministry partner, add the grant, the holder line and a `LICENSES/`
directory to the education code they already run, and the asset becomes reusable across the region.
One of the three above is a federal university's own project. ⚠️ Pre-registered as the next pass's
LATAM action: sweep the **national forges** (`gitlab.com` self-hosted instances at `.edu.br`,
`.edu.mx`, `.cl`) that this channel cannot see at all.
### Global

Opportunities that are **not** regional — sold on the same terms in all four regions above,
because the constraint they answer is the licence and the codebase rather than a jurisdiction.
Added in the twenty-ninth pass of 2026-10-07, which also closes a standing `P383` gate
failure: this block declared four of the five vocabulary regions, and the fifth, `Global`, had
no subsection even though the file's own frontmatter is `Global`.

- 🟢 **The two-reader licence gate (`P37`).** Measured on 412 education repositories across
  two concurrent passes: two independently hardened licence classifiers disagreed on **43
  (10.4%)**; after repairs on both sides, **10 (2.4%)** — and the **5 rows that can put a
  non-commercial asset into a billable deliverable are still open**, because each run fixed
  the classifier it happened to be looking at. Every engagement that ships, resells or embeds
  open-source education components eventually has to answer *"which licences does this
  carry"* in writing, and the near-universal current answer is one scanner, once, and a green
  tick. A **named list of contested rows** is a sellable, week-long, repeatable deliverable
  with no regional dependency.
- ⚠️ **Container-delivered licences as a due-diligence line item.** A licence shipped only as
  RTF or PDF puts markup where a title belongs, so every scanner on both sides of a
  procurement conversation is guessing. Two platforms on this shelf have **no root licence
  file at all** — their grant lives at `docs/License.txt` — so a client's root-only
  procurement scan reports a correctly-licensed GPL-2.0 platform as unlicensed. Asking the
  vendor for plain text is free and is itself a finding.
- 🟢 **The licence-grant clinic, generalised.** The LATAM section above proposes it for a
  university or ministry partner; the need is global. **173 of 496 cited education
  repositories (34.9%) are referenced by nothing** — no registry, no self-link, no peer
  repository — and a third of a shelf being un-depended-on is a condition of open-source
  education everywhere, not of one region.
- 🟢 **Enablement on permissively licensed curriculum.** The three assets added this pass
  ([`awesome-llm-apps`](https://github.com/Shubhamsaboo/awesome-llm-apps) Apache-2.0,
  [`Made-With-ML`](https://github.com/GokuMohandas/Made-With-ML) MIT,
  [`Hands-On-LLMs`](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models) Apache-2.0)
  can be forked, rebranded and **left with the client** — the difference between enablement
  and a course licence, and it travels to every region unchanged.

## Cross-region read

Two patterns hold in every region, which makes them safe to build once and sell
four times:

1. **Human oversight on any consequential decision** — required by Oklahoma and
   Maryland statute, by EU AI Act Annex III, by Brazil's PL 2.338 risk tiers, and
   by Korea's high-impact classification. It is also forced by the technical
   gap: no permissive open source auto-grader exists.
2. **Data residency and student-data boundaries** — California AB 1159, EU data
   residency practice, India's DPDP, and LATAM connectivity constraints all point
   at the same architecture: on-prem or in-region open-weight inference.

3. **Agent-specific governance is now a named requirement, not an extrapolation
   from general AI rules.** Singapore's Model AI Governance Framework for Agentic
   AI (January 2026, updated June 2026) is the first regulator-issued document
   that governs autonomous planning and action directly: bound the agent's powers,
   define human approval checkpoints, control the whole agent lifecycle, and train
   the end user. Those four dimensions also discharge most of what EU Annex III,
   the Oklahoma/Maryland oversight statutes and Korea's high-impact classification
   ask for. **Use the Singapore framework as the build checklist in every region**,
   because it is the most specific and the most agent-aware of the four.

4. **Curriculum mandates are now a funded demand driver, and they come with
   architectural constraints.** Two jurisdictions have made AI instruction
   compulsory with published specifics: the **UAE** (Cabinet, May 2025 — KG to
   Grade 12 from the 2025–26 school year, seven content areas, woven into an
   existing subject without extra school hours, specially trained teachers) and
   **China at provincial level** (Beijing: ≥8 hours a year for every primary and
   secondary school from 1 September 2025; Guangdong: 6 hours in lower grades
   rising to an hour a fortnight in grades 10–11). This is different in kind from
   the regulation in points 1 and 2: a mandate creates a **budgeted obligation to
   deliver content and train teachers**, not merely a constraint on how you deploy.
   It also hands you the two hardest requirements for free as design inputs:
   **age-gated capability** (Beijing bars primary pupils from independent
   generative-AI use) and **enforced teacher-in-the-loop** (teachers may not
   substitute AI for core instruction). Build to the mandate and the oversight
   obligations in points 1 and 2 are largely discharged as a side effect.

The deliverable that satisfies the first three is the same side-car. Build it once.
The fourth needs one more thing on top — a curriculum-alignment and age-gating
layer — which is pattern P9 in `compose/patterns.md`.

## What changed in this pass — read this if you read nothing else

| Finding | So what |
|---|---|
| Europe sized at **$2.64B** in 2026; leaders are Finland, Estonia, Netherlands | the EMEA reference deployment belongs in a small digitally mature state, not a large economy |
| AI Act **general application already live (2 Aug 2026)**; only high-risk deferred to Dec 2027 / Aug 2028 | stop telling clients the Act does not apply yet |
| Singapore's **agentic-AI** framework (Jan 2026, world first) | the cross-region build checklist, and its dimension 4 is a billable enablement line |
| **Vietnam** AI law in force 1 Mar 2026; **Korea** exactly 22 Jan 2026 | the APAC binding-regulation wave is wider than Korea/Singapore/China |
| LATAM: **92% students / 79% faculty** adopting, but **88% of faculty shallow** | sell depth and integration, not adoption |
| **Colombia CONPES 4144** — funded national AI programme through 2030 | add Colombia to the LATAM target list |
| **All 50 US states** legislating; states split into buyers vs brakers | qualify the camp before choosing the pitch |
| **Africa** enters the KB: South Africa draft national AI policy, GenAITEd Ghana | genuine EMEA greenfield; teacher capability is the constraint |
| Several popular education **MCP servers are unlicensed** (see `agents/top.md`) | a licence probe belongs in the engagement's first week |
| **OpenEduCat is LGPL-3.0** — proprietary modules permitted | on the admin side, a module is a viable commercial shape, not only a side-car |

## What changed in the third pass of 2026-10-06

| Finding | So what |
|---|---|
| **UAE: AI compulsory KG→Grade 12** from 2025–26 (Cabinet May 2025), 7 content areas, inside an existing subject, trained teachers | a budgeted content-and-enablement mandate, not just a constraint. Two of the seven areas are ethics and policy, so the pipeline must produce governance material too |
| **China: Beijing ≥8 h/year from 1 Sep 2025; Guangdong 6 h → 1 h/fortnight (grades 10–11)**; primary pupils barred from independent generative-AI use; teachers may not substitute AI for core instruction | **age-gated capability and enforced teacher-in-the-loop are build requirements.** Satisfy Beijing and you satisfy EMEA/NA oversight |
| Europe: **$2.64B (2026) → $8.0B (2030), 31.9% CAGR** — slower than the 41.5% global rate | Europe is the compliance-depth market, not the growth market; its share shrinks over the forecast |
| **MEA sized for the first time: $0.56B (2026) → $1.6B (2030), 34.3% CAGR** — but a second source puts the **UAE** at $7.4M (2024) → $21M (2029) | irreconcilable scopes. **Quote MEA as a range and name the uncertainty** |
| MEA: Saudi, UAE, Egypt, Nigeria, Kenya, Rwanda, Morocco, South Africa all have AI **strategies, none has a binding AI statute** | mirror image of the EU sale: governance design *before* the law, shorter cycle, weaker procurement trigger |
| APAC: **~530M K-12 students** (2024); adoption 65–75% (2025) → 80–90% (2026) | the denominator that makes small-model and offline deployment an APAC concern, not only a LATAM one |
| APAC law, per country: Korea 22 Jan 2026 · **Vietnam 1 Mar 2026, SEA's first** · Japan deliberately voluntary · **India and Australia still have no national framework in force** | "APAC-ready" is not a claim you can make |
| LATAM: **87% of institutions use AI, 26% have a formal AI strategy**; **72% of faculty positive vs 57% globally** | enthusiasm-rich, governance-poor — the most favourable shape for a governance-led engagement in this KB |
| **Uruguay is the first LATAM signatory of the Council of Europe AI Framework Convention** (2025) | the cheapest bridgehead for reusing EMEA compliance IP in LATAM — an interoperable governance vocabulary |
| North America channel **saturated — no net new findings**, explicitly stated | further depth needs procurement portals and state trackers, not another general search |
| The permissive open source layer went from "DeepTutor plus fragments" to **~30 verified projects incl. a full MIT LMS** | the differentiator moves from *finding* the parts to **composing, licensing and governing** them |

## What changed in the fourth pass of 2026-10-06

Channels new to this KB this pass: **paper-to-repository tracing** (arXiv / ACL
Anthology), a **GitHub-organisation sweep**, and a **Spanish/Portuguese-language
search**. Two of the five findings below are **corrections to this KB's own
claims**, which is the point of recording them.

| Finding | So what |
|---|---|
| **OpenMAIC is Tsinghua's, MIT, 40.0k★** — and `OpenMAIC-Brasil`, cited for three passes as evidence of a missing LATAM project, was a **fork-shaped name**, not a Brazilian project (re-probed: 404 on all four branches) | the **largest permissive asset in this KB** arrives, and the lesson-generation starting point for every region becomes **Chinese-origin MIT code**. Put provenance and data residency in week one. And **never attribute a region from a repository slug** |
| **NA 2030 sizing is disputed: $10.8B vs the $32B this KB recorded.** $32B would make NA ~75% of the KB's own global 2030 figure while the same page asserts a 36% share | **quote $3.68B for 2026 and 2030 as a range**, naming the uncertainty. Internal consistency favours the lower figure. Primary source unreachable — conflict recorded, not resolved |
| The third pass called North America **"saturated"**; re-running general searches added **statute names, bill numbers, mechanisms and dates** on six states — incl. **CA AB 1159's 1 July 2027 higher-ed trigger**, Idaho SB 1227 as an **AI-literacy and teacher-training mandate**, Oklahoma **SB 1734's annual parent disclosure**, Maryland's **24 districts / 120-day rolling** clock, **Ohio HB 96's deadline now past**, and NC's funding being **recurring and sole-sourced** | **"saturated" conflated no-new-entities with no-new-information.** Precision is what makes a finding sellable, and it was mostly missing. Ohio's 600+ districts are now in **implement-and-audit**, which is the better engagement |
| **Africa gets its first code shelf: `AI-for-Education`**, 5 of 6 repos MIT, built for **Sierra Leone's MBSSE** and **Uganda** (Luganda) — plus the only **voice-evaluation** and **pedagogical model-selection** tooling in this KB | Africa stops being greenfield-with-nothing and becomes **greenfield with a specific, permissive, ministry-connected entry point**. At 1–12★ it is research-grade: a conversation starter, not a product shelf |
| **A fourth licence failure mode: the grant that exists only in the paper.** `AITutor-EvalKit` (peer-reviewed EACL 2026, "released under an MIT license") has **no `LICENSE` payload on either branch**. Separately, **Open TutorAI** calls itself open source and is **CC BY-NC-SA 4.0** | **a peer-reviewed licence claim is evidence of intent, never of rights.** Probe the payload. Re-implement `AITutor-EvalKit`'s MI/ML/PG/AC rubric rather than vendoring it, and **file an issue asking for a `LICENSE`** — the cheapest high-value upstream contribution available here |

## What changed in the fifth pass of 2026-10-06

Channel new to this KB this pass: **institution-first search** — funding bodies,
ministries, universities and research groups queried by name, in English and
Spanish, instead of by GitHub topic or star count. Three of the six findings
below are **corrections to this KB's own claims**.

| Finding | So what |
|---|---|
| **The EU compliance clock moved 16 months.** Regulation (EU) 2026/1744 (*Digital Omnibus on AI*, OJ 24 July 2026, in force 27 July 2026, CELEX 32026R1744) pushes **Annex III stand-alone high-risk — education included — from 2 August 2026 to 2 December 2027**, and Annex I embedded to 2 August 2028. **Article 50 transparency did not move: the watermarking deadline is still 2 December 2026** | **The EMEA engagement is now two-phase and the near-term phase is the small one.** Label and classify by **December 2026**; build Annex III conformity evidence by **December 2027**. Clients who heard "the deadline was delayed" have deferred the labelling work too, and that one is weeks away. Primary texts unreachable from this environment — **verify against EUR-Lex before client use** |
| **The NA 2030 sizing conflict is resolved, in favour of $10.8B.** 36% × $10.6B global = $3.82B ≈ the recorded $3.68B for 2026, so the 2026 figures cohere. At 2030, $32B would be **75%** of this KB's own $42.48B global row; $10.8B is **25%**, implying 31.1% CAGR — within a point of EMEA's independently sourced 31.9% | **Retire $32B; quote $3.68B → $10.8B at ~31%.** And lead with the consequence: NA's share falls from 36% to ~25% while the absolute number triples, which is the arithmetic case for an APAC-weighted account strategy |
| **LATAM's opportunity is now measured, not inferred.** UNESCO IESALC (launched **9 September 2026**, UNESCO Digital Learning Week; **200 institutions, 19 countries**): **87% use AI, 26% have a formal AI strategy**; **45%** have formal guidance against **70%** in Europe and North America. Digital Education Council LATAM Survey 2026 (with Tec de Monterrey's Institute for the Future of Education): **92% of students and 79% of faculty** using AI, **88% of faculty still at minimal-to-moderate engagement** | **A 61-point gap between using AI and having a strategy for it is a governance engagement, not a tutor engagement.** Lead LATAM higher education with **pattern P6 (capability build)** and let P1 follow. Two independent, citable, month-old primary sources — the best-evidenced regional claim in this KB |
| **APAC regulation has arrived and reorders the build sequence.** Korea's **AI Basic Act in force 22 January 2026** (transparency, risk assessment, human oversight, documentation for high-impact systems); **Vietnam's Law No. 134/2025/QH15 effective 1 March 2026**; **Australia's TEQSA requires an institutional genAI action plan from every higher-education provider** | **Korea, not the EU, is now the binding constraint** for a multi-jurisdiction education product — its substance matches Annex III and it is live 23 months earlier. Build to Korea and EU conformity becomes documentation. **And TEQSA is the sharpest procurement trigger in this KB**: one mandatory document, one regulator, every provider in a country, enforced through accreditation |
| **Three regional "no permissive project exists" gaps refuted in one pass** — India ([microsoft/shiksha-copilot](https://github.com/microsoft/shiksha-copilot), MIT, MSR India/VELLM), ASEAN ([Coursemology](https://github.com/Coursemology/coursemology2), MIT, **15,802 commits**, NUS/AICET), LATAM ([LabSirius/TutorIA](https://github.com/LabSirius/TutorIA), MIT, UTP Colombia, SNCTI-funded). **All were found at 0–158★** | **The gaps were true of the discoverable shelf and false of the world.** Topic pages and star-sorted search are popularity-ordered and structurally cannot see a four-commit project from a public university in Risaralda. **When a gap survives several passes, change the channel — and pick one that is not ordered by stars** |
| **Singapore is the region's reference deployment and it is closed.** AICET (AI Singapore, Smart Nation and Digital Government Office funding, working with the Ministry of Education) runs **Codaveri** (30,000+ feedback items since 2024), **Softmark** (70,000+ scripts in 2025) and **ScholAIstic** (educator-authored chatbots across Social Work, Law and Nursing at NUS since June 2024) with **no public repositories** — on top of an **MIT** LMS | **The architecture this KB recommends is validated at ministry scale and cannot be forked.** Cite AICET as proof the shape works; build the shape from the permissive substrate. **ScholAIstic is the gap worth naming**: non-technical educators authoring and publishing their own roleplay training agents has **no permissive equivalent anywhere in this KB** |

### The method correction, stated plainly

The fourth pass concluded with "never attribute a region from a repository slug."
The fifth pass adds the complement, and it is the more expensive mistake:
**never conclude a region is empty from a popularity-ordered channel.** Every
regional gap this KB has stated most confidently was produced by sweeping topic
pages and star-sorted searches — both of which rank by adoption, and neither of
which can surface a new, unstarred, institutionally-backed project. Three such
projects existed the whole time. One query shape found all three.

## What changed in the sixth pass of 2026-10-06

The pass swept the **speech and low-resource-language substrate** rather than
education products — a layer that had **zero** entries in this KB. 26 repositories
probed, 26 resolved, every licence read from its own `LICENSE` payload.

**Four things changed in the commercial picture:**

1. **Voice stopped being a proprietary dependency.** `k2-fsa/sherpa-onnx`
   (**Apache-2.0**, 15.1k★) delivers STT, TTS, diarization and VAD in one
   permissive tree **with no Internet connection**, on phones, Raspberry Pi and
   RISC-V. Spoken practice and oral assessment reprice from a recurring
   per-token cost to a one-off build on hardware the client already owns.
2. **Mother-tongue delivery is a two-region capability.** India (AI4Bharat, all
   **MIT**, 22 scheduled languages) and East Africa (`SunbirdAI/salt`,
   **Apache-2.0**, six Ugandan languages with studio TTS; Masakhane, **MIT**).
   **Everywhere else the permissive layer does not exist** — which makes corpus
   building a fundable first phase rather than a blocker.
3. **India is the only all-MIT national stack in this KB.** Sunbird (**MIT**,
   38,046 commits, **DIKSHA**, Digital Public Good) plus the AI4Bharat layer plus
   MIT orchestration — see **P16**. In public procurement this removes the licence
   conversation entirely.
4. **The highest-volume assessment task in primary education has no open
   implementation.** Oral reading fluency is owned by closed products with no
   public repositories, while the permissive components and a **public dataset
   with a published baseline** both now exist — **P17**.

**Three named rejections, recorded so they are not re-proposed:**
`facebookresearch/seamless_communication` is **CC BY-NC-4.0** (non-commercial);
`rhasspy/piper` is **MIT but archived**, its maintained successor **GPL-3.0**;
`aisingapore/sea-lion` has **no repository-level licence**, deferring the grant to
each model card.

**And one correction to this KB's own regional labelling.** Tucano, recorded as a
Brazil-origin Apache-2.0 asset, was **archived 2026-02-24**; its successor Tucano 2
is developed at the **University of Bonn**. The model is still usable for Brazil
work, but **its maintainership moved to EMEA** and the KB should not keep calling
it LATAM-origin.

### The method note, stated plainly

The fifth pass learned that **low star counts hide real assets**. This pass found
the inverse: **high star counts hid dead ones.** On this shelf, 46.1k★ Coqui is
abandoned while its 2.3k★ Idiap fork has **641 more commits**; 11.3k★ Piper is
frozen. The fields that carried the signal were **archive status, the successor
notice, and commit count** — none of them popularity.

**Check whether a repository is alive before checking how popular it is.**

## What changed in the seventh pass of 2026-10-06

New channel: **native-language search** (Japanese, Korean, Arabic,
Bahasa/Thai/Vietnamese), plus a **function-scoped MCP sweep** and a
**consistency audit** of the shelves against the trending logs. **18
repositories probed, 18 resolved**; every licence from payload.

| Finding | Why it matters |
|---|---|
| **Vietnam's Decree 33** (signed 2026-06-30, in force 2026-08-15): 46 high-risk systems, **3 in education** | Category 1 — *self-learning content from uncontrolled data sources* — **regulates the corpus, not the decision**. No Annex III equivalent. Every RAG tutor in this KB is in scope in Vietnam on provenance alone ⇒ **P20** |
| Vietnam's behaviour-monitoring trigger is qualified to **biometric** data | **First APAC regime in this KB that is *looser* than Annex III** on a specific axis. Non-biometric analytics sit outside it |
| Education's Decree 33 transition runs to **2027-09-01** (with healthcare and banking) | The **longest** runway of any sector — a remediation window with a statutory date |
| **ASEAN has a permissive language shelf**: Vietnamese, Thai, Malay ×2, Indonesian ×2 | **Falsifies trend 21's "two-region" claim.** Combined with MIT `coursemology2`, ASEAN now has an MIT LMS substrate **and** an Apache-2.0/MIT language substrate under an unbuilt pedagogy layer ⇒ **P19** |
| **MEA's constraint is licensing hygiene, not capability** — the one real Arabic education agent is unlicensed | Turns the region's weakest finding into the **cheapest** one to act on: three `LICENSE` files change the regional answer |
| **H.R. 8747** advanced from House committee — federal funds for AI curriculum and literacy | The only **funding** instrument among the North American rules this KB tracks; everything else constrains |
| **Japan gap refuted — by this KB, passes ago.** `toshieji/moodle-grading-mcp` (MIT, © WACA + Toshiaki Ejiri) | `agents/top.md` asserted a gap its own trending log had already disproved. **Internal consistency, not coverage, is now the binding constraint on this KB's accuracy** |
| **Korea's first permissive education asset** — `yongsoojoo/esd2026-agent-workflow` (MIT + CC BY 4.0, Kookmin University) | Course material, not an agent. The **agent** gap stands, against an AI Framework Act in force since 22 Jan 2026 |
| **No licensed open proctoring agent exists** — the one candidate has no payload | A regulated category (Annex III point 3; Decree 33 category 3) with **no open competitor** |
| **No new LATAM code this pass, and the reason is declared** | The channel opened was non-Iberian by design. Not evidence about the LATAM gap either way |

### The method note, stated plainly

Three passes have now refuted a regional gap, each by changing a different thing:
the **channel** (fifth — institution-first), the **layer** (sixth — substrate
rather than product), and the **noun** (seventh — toolkit rather than sovereign
model). **Not one was refuted by running the original search harder.** When a
gap survives its second probe, change the probe.

And the cheapest two corrections of this pass required no search at all — they
were this KB disagreeing with itself, found with `grep`. **A pass is finished
when the shelf, the gap list, the trends file and the patterns agree with the
log, not when the log entry is written.**

## What changed in the eighth pass of 2026-10-06

**The LATAM read is replaced, not extended.** For four passes this file's LATAM
position rested on *"no LATAM-origin permissive education project"*. That gap is
**fully refuted on origin, licence and design** and survives **only on
maturity**: the region has published the design (TutorIA's MIT 13-page
specification, Colombia) and working code (EduFlow, MIT, Chile) and an adopted
language model (BERTimbau, MIT, 886★, Brazil) — and nothing at production scale.

**The commercial consequence is a different engagement shape.** A LATAM
engagement is a **productionisation** engagement with citable local provenance
and two named academic partnership leads, not a greenfield build.

**Three facts new to this file:** Colombia's **Ley 1581 de 2012 (Habeas Data)**
with TLS/AES-256 acceptance criteria and SIC enforcement exposure; a hard
**2 GB RAM / 3G** low-resource envelope with a working demonstration that it is
achievable; and **Latam-GPT's licence** — **Llama 3.1 Community, not OSI
approved**, despite the EC's own Open Source Observatory and the trade press
calling it open source.

**One cross-region finding, and it is the most actionable thing in the pass.**
The seventh pass diagnosed MEA: *the binding constraint is licensing hygiene,
not capability.* The eighth pass found the **identical** shape in LATAM's
indigenous-language layer (9 of 11 repositories ungranted, including three
AmericasNLP editions) **and a remedy that works prospectively**: CAi UC made an
OSI licence a condition of hackathon evaluation and 20 licensed repositories
appeared in eight hours. **Sponsoring that one clause is cheaper than any
upstream-issue campaign and is the pass's recommended action for both regions.**

**North America, EMEA and APAC returned nothing new, and each is recorded as
such above rather than left silent.** North America's general-language channel
is now **saturated** — four consecutive passes, identical facts — and the next
finding there must come from district RFP language or state procurement portals,
which this KB has never swept. EMEA returned enterprise-AI commentary and one
event (the Council of Europe's second working conference on AI-in-education
regulation). APAC returned sovereignty framing, which is read here as the
region's actual opportunity shape rather than as a miss.

### The method note, stated plainly

**This file's regional claims are only as good as the probe's vocabulary, and
this pass is the fourth consecutive demonstration of it.** The LATAM gap was
refuted not by searching LATAM harder — four passes had done that — but by
probing a repository for a **specification** instead of for **code**, and by
sweeping an **institutional event** instead of a topic page.

**And the licence column in every table in this KB now carries a known
ceiling.** Eight passes treated the `LICENSE` payload as ground truth. It is
wrong about `Llamacha` in the permissive direction, silent about CAi UC's
inherited holder, and says nothing about the label-versus-grant gap that makes
Latam-GPT look open. **Three points, not one: payload, asset scope, holder.**

## What changed in the ninth pass of 2026-10-06

**Channel: the funder and procurement channel**, plus the
**education-ministry engineering organisation** — both named as necessary by the
eighth pass, neither ever swept by this KB.

1. **North America's supply of permissive education AI is now a funded pipeline
   with a licence floor.** The **$26M K-12 AI Infrastructure Program** (Digital
   Promise + Gates Foundation, with Learning Data Insights, DrivenData,
   Georgetown's Massive Data Institute, Catalyst @ Penn GSE) requires all funded
   work to be **at least as permissive as CC-BY-4.0 (content) / Apache-2.0
   (code and models)**. **Twelve projects are funded and named**; the **$8M EDU
   AI** award for an open-source K-12 math tutoring model closed 31 Jul 2026 with
   work starting Nov 2026. **Nothing has shipped yet** — measured as 0
   repositories for the two most specific artefacts.
2. **The oldest gap in this KB acquired a date instead of closing.** No
   Apache-2.0 tutoring-quality evaluator exists today (measured, licence-filtered,
   0 results). Three or more of the twelve funded projects target exactly that,
   through 2027. The engagement line changes from *"this does not exist"* to
   *"build the harness now, swap the benchmarks in as they land"* (**P23**).
3. **Procurement rubrics became the region's real specification.** Maryland
   **SB 720** (rubric + 120-day local policy + AI coordinator), Vermont's
   seven-criterion rubric, Idaho/Maryland/Alabama statutory capability
   assessments and the prohibition on training vendors' models on student
   records. **CoSN: 39% of districts score interoperability in RFP rubrics** —
   the first procurement-side number for trend 4. And the gap *inside* the
   rubrics — no required interaction audit trail, output-provenance disclosure or
   bias/accuracy evaluation — **is the differentiator, and it is the same
   artefact set the EU AI Act profile already forces (P13).**
4. **EMEA gained a permissive, production, government-maintained estate.** The UK
   DfE (`DFE-Digital`) publishes its national teacher-training, vacancies,
   schools-register and benchmarking services under **MIT** — while its own AI
   repositories sit at 0–1★ with **no licence payload**. That asymmetry is the
   public-sector opening, and it is a precedent usable with any EMEA ministry.
5. **LATAM's governance gap is now measured by a UN-system instrument.** UNESCO
   IESALC + UNU-IAS, 200 institutions, 19 countries: **73.5%** adoption in
   teaching and learning against **18.5%** institution-wide policy, **9%** formal
   evaluation mechanisms and **8%** dedicated AI budget. **Nine percent is the
   sharpest number in this KB**, and it points at an engagement the region can
   buy.
6. **APAC built the evaluation benchmark the US is now funding, and did not
   license it.** `AI-EDU-LAB/E-EVAL` (33★, Chinese K12 LLM education evaluation)
   has **no payload** — the third region showing *built, published, benchmarked,
   ungranted*.
7. **Two regional queries failed for the second consecutive pass.** The mandated
   EMEA and APAC sweeps returned **enterprise** AI-governance material, not
   education. Both regions now need the channel change that worked for the UK
   this pass. Recorded as exhausted channels, not as regional stability.

### The method note, stated plainly

This pass accepted **Tier 2 evidence into the durable files for the first time at
scale.** Fourteen hosts carrying the primary documents — the RFPs, the grantee
announcements, the state guidance, the UNESCO paper, the arXiv preprints — are
**EGRESS_BLOCKED** in this environment, so **no primary document was read.**
Every funder, dollar, date and statutory claim above is corroborated across two or
more independent search summaries and is labelled Tier 2 wherever it appears.

That is a real lowering of this KB's evidentiary bar, and it is deliberate: a
funded pipeline known at Tier 2 is worth more to an engagement than a silent gap
known at Tier 1 — **provided nobody mistakes which is which.** The tiering is
written into every table rather than into a footnote, and the repository and
licence facts in this pass remain **Tier 1, payload-verified**, as they have been
for nine passes.

The counterweight is that the Tier 1 method itself was found defective this pass:
**three of the UK ministry's six MIT grants are in a file spelled `LICENCE`** — a
spelling pattern **P22**'s gate already lists and no recorded sweep has ever
run. See `agents/top.md`, ninth-pass method
note — four government repositories would have been recorded as ungranted by a
query that could not have found their grant.

## What changed in the tenth pass of 2026-10-06

**Channel: the KB's own reject pile, re-probed** — plus the **interoperability
shelf** that the ninth pass's procurement finding pointed at, the **Council of
Europe education directorate** for EMEA, and the **ministry-programme channel**
for APAC and LATAM. The generalist regional query was retired for EMEA and APAC
after a third consecutive failure.

1. **North America's funded pipeline gained two more named projects and a third
   measured zero.** Harvard (Ying Xu) is funded for **OpenLiteracy**, an
   open-source speech-foundation-model suite for early word reading assessment —
   which lands exactly on this KB's sixth-pass oral reading fluency gap. Maryland
   (Jing Liu) is funded for multimodal classroom formative-assessment datasets.
   **`OpenLiteracy` returns 0 repositories on GitHub.** Three funded, named,
   dated projects; three measured zeros. Five of eight Cohort 2 grantees still
   unnamed.
2. **EMEA is writing the evaluation rule that North America is funding the
   artefact for.** The Council of Europe has a **Committee of Experts on AI and
   Education (EDU IA)**, a **Compass for AI and Education**, a Committee of
   Ministers text adopted in **Munich** implementing **Article 20 of the Framework
   Convention on AI**, and a 2026–27 programme containing a **proposed legal
   instrument to regulate AI systems in education** and a **European Reference
   Framework for the Evaluation of Educational Technologies**. One gap, two
   regions, two instruments — and the European one arrives as conformance, which
   cannot be retrofitted.
3. **The proprietary ministry channel is simultaneously in all three non-US
   regions.** OpenAI's **Education for Countries** names **Estonia, Greece, Italy
   (CRUI), Slovakia, UAE, Jordan** (EMEA), **Kazakhstan, Singapore** (APAC) and
   **Trinidad & Tobago** (LATAM). Nine ministries or sector bodies, one vendor,
   national tier. Singapore's own framing — *"exploring various AI tools from
   different partners"* — is the opening, and **Trinidad & Tobago is a Caribbean
   ministry acquiring a national programme in a region measured at 9% formal
   evaluation capacity.**
4. **LATAM's governance table is now complete and sharper.** UNESCO IESALC /
   UNU-IAS, 200 institutions, 19 countries: **73.5%** teaching-and-learning
   adoption, **57.0%** research, **34.1%** administration, **20.0%** community
   engagement — against **26.0%** with a formal AI strategy, **18.5%** with
   institution-wide policy, **9.0%** with formal evaluation mechanisms and
   **8.0%** with a dedicated AI budget. The new figure, 26.0% strategy above
   18.5% policy, says a third of institutions that wrote a strategy never turned
   it into one.
5. **The integration tier became a priceable deliverable.** Against **39% of
   districts scoring interoperability in RFP rubrics**, the permissive shelf is
   verified and small: four Apache-2.0 LTI 1.3 libraries (Node, PHP, two JVM) and
   one MIT OneRoster client (**rostering only, no gradebook**). **No permissive
   Caliper Analytics implementation.** 🔵 **CORRECTED, twenty-fourth pass of 2026-10-07 — "No
   Python LTI 1.3 library at all" was false.** [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti)
   is **MIT**, head commit **2 d**, PyPI `django-lti` **v0.10.1 (61 d)**; Python is where the AI
   layer lives and it is now served, provided the AI tier is Django.
6. **A named North American partner turned out to have a 238-repository MIT
   estate.** Learning Equality, Cohort 1 grantee and Kolibri maintainer. New
   verified MIT: **morango** (peer-to-peer Django DB replication with
   certificate-based auth — the sync engine under the offline story) and
   **le-utils**. Two sibling repositories returned **no payload**, so diligence
   stays per-repository.
7. **Three negatives were re-tested and held, which makes them usable.** APAC's
   `E-EVAL` benchmark and nine LATAM-placed indigenous-language and hackathon
   repositories were re-probed across **20 URLs each** — both spellings of
   "licence", both branch names. **Not one carries a payload.** Those regional
   findings can no longer be attributed to this KB's own query defects.

### The method note, stated plainly

This pass **audited the KB against itself**, and the audit cost it two of its own
conclusions.

The ninth pass's headline method fix — probing the British spelling `LICENCE` —
**flipped nothing** when run backwards over the 41 repositories this KB had
recorded as ungranted. It is a house style at one UK government organisation that
was written up as a general defect in the KB's reach. The defect that *was*
general was never announced: **the KB had only ever probed one branch name.** The
single flip in 41 (`jdolny/OneRoster.NET`, MIT) sits on `master/LICENSE`, and three
of the six validation controls do too.

The finding to carry forward is worse, and it is about market intelligence as much
as code: **GitHub's rendered licence field reported "License: Not specified" for a
repository carrying a complete MIT grant** (`qazasd2518995/prosody`). Every
licence-filtered zero-result measurement in this KB — including three in this very
pass, used above to show that funded projects have not shipped — inherits that
error. The zeros remain the best available measurement. **They are evidence of
absence as GitHub's licence index sees it, not evidence of absence**, and the
distinction has to survive into any client deliverable that quotes them.

**And the environment is now a measured constraint rather than a series of
accidents.** Nine further hosts were attempted this pass and **all nine returned
`EGRESS_BLOCKED`**: `digitalpromise.org`, `www.coe.int`, `rm.coe.int`,
`www.prnewswire.com`, `www.gse.upenn.edu`, `www.eunews.it`, `www.sec.gov`,
`ess.iesalc.unesco.org`, `openai.com` — including **three syndicated mirrors tried
specifically to route around a blocked primary host.** With the ninth pass's
fourteen, that is **23 distinct hosts across two passes with zero reachable.**
`github.com` and `raw.githubusercontent.com` are the only origins this environment
serves.

Two consequences for the next pass. **The vendor-filings channel is not unswept,
it is unreachable** — `www.sec.gov` is blocked, so McGraw Hill's and Workday's
FY2026 open-source and copyleft-risk disclosures are available at Tier 2 only, and
that channel needs a different host rather than a better query. And **every market,
funder, regulatory and procurement figure in this file remains Tier 2**: dollar
amounts, dates, percentages and licence clauses are corroborated across independent
search summaries, never read from the primary document. **Confirm each one against
its source before it enters a client deliverable.**

## What changed in the eleventh pass of 2026-10-06

**One instrument change produced every market finding below.** The GitHub REST
search API is reachable in this environment through the session's GitHub MCP server —
`curl https://api.github.com/search/repositories` returns **403** and
`/repos/{owner}/{repo}` is refused, which is why ten passes recorded the API as
blocked. Through the MCP path it returns `total_count` and real metadata, so this
KB's *absences* can now be counted rather than inferred from a ranked search page.

| What the KB said | What this pass measured | Consequence for a proposal |
|---|---|---|
| *"No permissive evaluation harness exists; build the socket and wait for the artefact"* (P23, three passes) | **Inspect** (MIT, **2,945★**, UK AI Security Institute) and **Moonshot** (Apache-2.0, 355★, Singapore IMDA's AI Verify Foundation), both pushed 2026-10-06 | **Stop quoting harness-building as the deliverable.** The harness is free, permissive and government-maintained. Quote the *rubric*, the *dataset handling* and the *conformance pack*. |
| *"`tutoring quality evaluation benchmark` → 0 results"* | Drop one word: **20 results**, led by **Khan Academy** (57★) and **ETH Zurich** (43★) | The benchmarks exist. **None is OSI-licensed** — the constraint is legal, not technical. |
| *"No Python LTI 1.3 library on the permissive shelf"* (tenth pass) | **`dmitry-viskov/pylti1.3`, MIT, 138★** — the **second-largest runtime** on the permissive interoperability shelf | The integration tier priced in P25 was priced against a hole that was not there. |
| *"The regional flagship is not open source"* / LATAM has no platform | **`portabilis/i-educar`, GPL-2.0, 718★ / 547 forks**, Brazil, `software-publico` | A LATAM public-sector engagement has a real, licence-appropriate base. |

### The market read that follows from the licensing wall

The money and the measurement are in different places, and the licence is what
separates them:

- **North America funds the datasets** — $26M philanthropic K-12 AI infrastructure
  programme with an Apache-2.0-or-better floor (ninth pass) — and its two best
  existing benchmarks come from **Khan Academy** and are **not** openly licensed.
- **EMEA supplies the harness** — UK AI Security Institute's Inspect, **MIT** — and
  the rule (Council of Europe reference framework; EU AI Act full effect August 2026,
  education AI high-risk).
- **APAC supplies the red-team tooling** — Singapore IMDA's Moonshot, **Apache-2.0** —
  and the highest deployment rate (**56%** of businesses already running assistants).
- **LATAM supplies the demand and almost none of the supply** — **73.5%** using AI in
  teaching and learning against **9%** with any formal evaluation mechanism.

**The sellable asset across all four is the same one and it is not a model.** It is
an evaluation and conformance capability assembled from permissive components, with
the non-permissive benchmarks **borrowed at measurement time and never shipped**.
Every region's buyer wants it for a different stated reason — procurement rubric in
North America, AI Act conformance in EMEA, sovereignty in APAC, institutional
credibility in LATAM — and the architecture is identical. That is the most
transferable finding this KB has produced.

### The method note, stated plainly

Three zeros were wrong this pass and each was wrong for a different reason: a **ranked
web surface** is not a count; a **`repo:` qualifier excludes forks by default**
(`repo:mitodl/open-learning-ai-tutor` → 0, with `fork:true` → 1, and that fork is MIT
Open Learning's production tutor); and a **keyword-heavy query measures the filter**,
not the world.

A fourth was wrong for a reason that has nothing to do with search: **this
repository's reset earlier on 2026-10-06 dropped 172 real repository addresses**
(627 live vs 678 archived, 7 of the 179 differences being placeholders), and the
tenth pass declared one of them — `pylti1.3` — a gap while it sat in
`archive/2026-10-06-pre-reset/` with its licence and star count intact. **A gap claim
made after a reset is not publishable until it has been diffed against the archive.**

## What changed in the thirteenth pass of 2026-10-06

**One opportunity moved, in EMEA, and it moved because of provenance rather than
discovery.**

[`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) was
already in this KB — the twelfth pass recorded it in `repos/trending.md` with the right
licence (**BSD-3-Clause**) and the right figures (**108★ / 192 forks**). What was missing is
the only part a client conversation turns on: **who stands behind it.** It is from the
**IRF-SIC Laboratory, Ibn Zohr University, Agadir, Morocco**, funded by Morocco's
**Ministry of Higher Education**, the **Digital Development Agency** and the **CNRST**.
`Agadir` and `Ibn Zohr` returned **zero** matches across this KB before this pass.

**That makes the most capable permissive AI-native education platform on this shelf an
African, government-sponsored project** — ahead of the European, Indian, Singaporean and
Brazilian entries on the same axis. It is now shelved in `agents/top.md` and
`verticals/solutions.md`, and **P33** is the delivery shape.

### The method note, stated plainly

🔵 **A row recorded in a trending log is not a shelved asset, and this KB had been
treating it as one.** The twelfth pass did the hard part — found it, probed the payload,
corrected a catalogue that mislabelled it Apache-2.0, and spotted the fork inversion — and
then left it in an append-only log that nobody reads to answer *"what do we build on?"*.
For a day, the best permissive AI-native platform available to this practice was invisible
to the shelves that exist to surface it.

🟢 **The rule that follows: a payload-verified asset gets shelved in the same pass that
verifies it.** The trending log records *how and when* it was found; `agents/top.md`,
`repos/foundations.md` and `verticals/solutions.md` record *that it exists and what it is
for*. The twelfth pass's own closing instruction was to take the education MCP cluster
next; that remains right, and it should be read alongside this one — **probe the cluster,
then shelve what the probe grants, before moving on.**

⚠️ **Second method note: the demand side is saturated at this channel's resolution.** Every
market figure and regulatory instrument in all four regions was re-run this pass and came
back **unchanged** — NA at $3.68B/36% share with 134 bills across 31 states; Europe at
$2.64B → $8.0B at 31.9% CAGR with the Digital Omnibus dates independently reconfirmed
(Council approval 29 June 2026); Korea's AI Framework Act and Vietnam's Law 134/2025/QH15
in force; the DEC LATAM survey at 92%/79% and UNESCO's Santiago observatory. **Nothing in
the demand picture moves in a day.** Future passes should spend their probe budget on
**supply** — repositories, licences, provenance — and re-run the demand queries only to
catch a regime change, which is the same discipline this KB already applies to the
generalist GitHub query.

🔴 **Third, and it bounds every regional claim above: three forges are unreachable.**
`codeberg.org` (the EU sovereignty forge), `gitee.com` (the China-domestic forge) and the
European Commission's **Joinup / OSOR** catalogue all return **403 at the egress proxy**.
Every licence fact in this KB rests on `raw.githubusercontent.com` because it is the only
code-hosting payload this environment can read. **The EMEA and APAC supply pictures are
GitHub-only and therefore understated**, and two named Codeberg education projects were
surfaced and left off every shelf because they could not be payload-verified. Declared, not
inferred.

## What changed in the fourteenth pass of 2026-10-06

**The supply side of this file got a measurement it has never had: the integration tier,
counted per platform, with the licence read from the payload.** That is a market fact, not a
repository fact, because it decides whether an engagement is an adoption or a build.

| Platform the client runs | Open-source integration repos | Engagement verdict |
|---|---|---|
| Canvas LMS | 117 | adopt |
| Moodle | 86 | adopt (from outside the GPL tree) |
| Brightspace / D2L 🆕 | 23 | adopt |
| Google Classroom 🆕 | 17 (best dedicated server **6★**) | **build** |
| Blackboard Learn 🆕 | 5 | build on the best of five |
| Open edX | 1 (AGPL-3.0) | copyleft all the way down |
| 🔴 **PowerSchool** 🆕 | **0** | **build — the tier does not exist** |

🔵 **The single sentence to carry out of this pass:** open-source integration coverage tracks
the **higher-education** install base and ignores **K-12 administration** — Canvas and Moodle
hold 203 of the 249 repositories measured, while K-12 is **45.62% of adoption** and its two
defining platforms (Google Classroom, PowerSchool) have 17 and 0. The empty tier and the
regulated tier are the same tier, and that is what makes it defensible for an enterprise
integrator rather than a hobbyist.

**New regional facts, each in its own region's section above, none of them LATAM-only:**

- **North America** — $951M (2024) → $2,303.2M (2029), **CAGR 15.9%**, **36%** of the global
  market: the largest share on the slowest growth. Segment splits: K-12 **45.62%** of
  adoption, STEM **34.78%** of revenue, cloud **71.22%**. A dense US school-data cluster
  exists in the MCP Registry as **hosted endpoints with no source** — the open,
  inside-the-boundary equivalent is an engagement.
- **EMEA** — the **ministry tier is real**: Sweden's Skolverket curriculum, school-register
  and planned-educations APIs are wrapped **MIT** and in the official MCP Registry; Belgium's
  Smartschool likewise; Norway's Udir equivalent is **ungranted**. And the **Council of
  Europe** convened its 2nd Working Conference on the regulatory dimensions of AI in
  education (October 2026), including **a European evaluation framework to assess educational
  technologies** — a treaty body writing the pedagogy-evaluation instrument the market has
  not settled.
- **APAC** — the highest-yielding region of the pass: five placed assets, three with
  permissive payloads, including **MIT auto-grading from a commercial vendor with writes
  gated by default** (Pakistan). Adoption is majority-done (**57%** of Asian organisations),
  the stated blocker is **infrastructure** (**49%**), and **sovereignty shapes roughly half**
  of infrastructure choices — so the regional sale is an architecture, not a product.
- **LATAM** — **99%** of startups use AI, **85%** natively, edtech named among the most
  disruptive sectors; UNU/UNESCO surveyed **200 HEIs across 19 countries**. 🔴 And two honest
  negatives: **zero of the registry's 102 education servers are LATAM-placed**, and this pass
  **failed to measure the region's platform tier** because it OR'd SIGAA and SUAP into one
  query and collapsed into the generalist layer. The region is nonetheless well served
  today — its dominant platform is Moodle, whose 86-repository MIT side-car tier is global.

### The method note, stated plainly

🔴 **Three instrument failures this pass, and two of them would have produced published
numbers that were wrong.**

1. **Boolean `OR` in GitHub repository search destroys specificity.** `sigaa OR suap OR siga
   mcp server` → **`total_count: 160,659`**, all generalist. One platform name per query, or
   no count.
2. **The MCP Registry's `?q=` parameter returns HTTP 200 and the unfiltered page** — a silent
   no-op. `?search=` fails at the connection (000) and is therefore the safe failure. A pass
   that trusted `q=` would have published a fabricated per-platform count with a 200 beside
   it.
3. **A record is not a server.** The registry is version-rowed: **31,300 records = 11,505
   unique servers**, a 2.7× overstatement. And the figure is a **floor**, because the page
   loop ended on an empty body at page 313.

⚠️ **One standing caution, re-earned.** A registry listing is not an existence proof: one of
six sampled entries points at a repository `ls-remote` cannot reach. The same rule this file
already applies to GitHub's `total_count` — an index count is an **upper bound** — applies to
the registry.

## What changed in the fifteenth pass of 2026-10-06

**One instrument completed across all four regions, one carried figure contradicted, and one
arithmetic trap closed.** The global market query reproduced the series this file already
carries ($7.52B → $10.6B → $42.48B at ~41%; the rival $6.4B → $79.6B at 31.35%; the 71.22% /
45.62% / 34.78% segment splits; 66% → 92% student usage). **Nothing new globally — the
divergence this file already documents is unchanged.** What is new is regional.

### The geography instrument, now complete — and LATAM is its slowest-growing region

The fourteenth pass recorded North America from one house's geography series. This pass
retrieved the other three entries of **the same series**, so for the first time the four
regions are comparable on one instrument:

| Region | 2024 | 2029 | CAGR |
|---|---|---|---|
| **North America** | $951.0M | $2,303.2M | **15.9%** |
| **APAC** | $591.6M | $1,848.1M | **20.9%** 🆕 |
| **LATAM** | $105.6M | $204.7M | **11.7%** 🆕 |
| *— of which "Rest of Latin America"* | $18.2M | $36.0M | 12.1% 🆕 |
| **EMEA** | 🔴 **not retrieved** | — | — |

🟢 **APAC is the growth region and North America is the money region** — APAC compounds five
points faster from 62% of the base. That ordering is consistent with everything else this
file carries about APAC.

🔴 **And LATAM is the slowest-growing region in this instrument at 11.7%** — which
contradicts a figure this KB has carried since its second cycle: *"LATAM $1.5B → $4.2B,
CAGR 45%."* The two cannot both be about the same thing: **they differ by a factor of
roughly 20–40 on the base and by 33 points on the rate.**

⚠️ **Do not reconcile them. Do not average them. Quote one, with its instrument named.**
The most likely explanation is scope — a narrow "AI in education software" definition
against a broad "AI-enabled edtech" one — but this pass did not establish that, and an
unverified reconciliation is how a wrong number gets into a deck with a citation attached.

🔴 **EMEA could not be retrieved from this instrument: the publisher's domain is blocked by
this environment's egress proxy** (`EGRESS_BLOCKED`, `www.marketsandmarkets.com`), so the
three figures above come from search-result snippets rather than the pages themselves. A
*different* house puts Europe at **$2.64B growing 31.9% to $8.0B by 2030** — which is not
comparable to the table above and must not be dropped into it.

### 🔴 The arithmetic trap, stated so nobody repeats it

Sum the geography instrument's 2024 regional values: **$951.0M + $591.6M + $105.6M ≈
$1.65B**, three regions of four. The global series in this file puts 2025 at **$6.4B–$7.52B**.

**The regional instrument is roughly four to five times smaller in scope than the global
one.** Therefore:

- ❌ **Never compute "region as % of global" by dividing a figure from one instrument by a
  figure from the other.** It produces a number that is wrong by a factor of four and looks
  perfectly plausible — LATAM would come out at ~1.5% of a market it does not measure.
- ❌ Never add a regional CAGR to the global narrative ("the market grows 41%, and LATAM
  grows 11.7% of it") — they are growth rates of different quantities.
- ✅ Use the geography series **only** for region-against-region comparison, which is the one
  thing it is internally valid for, and say which house it came from.

### Opportunities by region — fifteenth-pass additions

The supply-side findings this pass are placed by country by construction (the platform-name
channel returns an institution, and an institution is in a country). Full rows in
`agents/top.md`.

#### North America

🔴 **The headline is a *negative* commercial finding and it is worth more than a positive
one.** The US K-12 SIS integration tier exists (PowerSchool 590 repositories, Infinite
Campus 43) and is substantially MIT — and it is **not a production path**, because Infinite
Campus's Terms of Use forbid access by means other than publicly supported interfaces,
naming scraping and AI training explicitly. The one MIT MCP server for the platform says in
its own README that it likely violates that ToU, and adds FERPA and COPPA on top.

🟢 **The opportunity that follows:** the engagement is **procurement plus integration, not
integration alone.** A US K-12 district engagement must budget for the vendor's official API
entitlement (OneRoster) before any agent work is scoped — and a studio that says so in week
one differentiates itself from every competitor that discovers it in month three. This is
also the strongest argument in this KB for leading North American K-12 conversations with
the **interoperability tier** rather than the tutor tier.

⚠️ Regulatory context re-confirmed this pass, unchanged: a **relative regulatory vacuum** —
no FDA-equivalent for edtech, adoption decided school-by-school, with Colorado and Texas
named again as the states with piecemeal requirements. **36%** of global adoption share.

#### EMEA

🟢 **The deepest permissive integration supply in this pass is European, and it is placed by
country**: PRONOTE (FR, 907 repositories, `pronotepy` MIT at 241★), WebUntis (DE/AT, 401,
MIT and BSD-2 clients plus an MIT Flutter client with an **on-device** AI assistant),
Magister and SOMtoday (NL, MIT clients). **France, Germany/Austria and the Netherlands each
have a payload-backed permissive client for their dominant school platform.**

🔴 **The UK is the exception, and it is a clean gap**: `bromcom` 36 repositories with nothing
above 2★, `"arbor mis"` 7 with nothing above 0★, `"capita sims" school` **0**. The UK has the
strongest *government* open-source estate in this KB (the DfE MIT estate, ninth pass) and
**no permissive MIS integration layer at all**. Build, don't adopt — and the one UK asset
found, [`DPlazma/assessapp`](https://github.com/DPlazma/assessapp) (MIT, Arbor MIS + AI
tagging), is a 0★ sketch of exactly the product that is missing.

⚠️ **Regulatory clock, as reported this pass:** the EU AI Act became applicable **2 August
2026**, with education classified high-risk (Annex III) requiring human oversight and data
protection. ⚠️ **This conflicts with the December 2026 / December 2027 split this KB models
in P13** — two different readings of the same instrument. P13 was built from a closer
reading and is not overturned by a search snippet; **flagging the conflict, not resolving
it.** Also reported: **94%** of EMEA organisations likely to invest in AI-specific training
in 2026, and a January 2026 competency framework defining **15 competencies across 5
dimensions** for national teacher-training programmes.

#### APAC

🟢 **Fastest-growing region on the completed geography instrument (20.9%)**, and the
governance posture matches: **48%** of APAC governance leaders rank AI adoption their top
2026 priority — ahead of growth (45%), cybersecurity (39%) and geopolitical risk (32%) — and
**57%** of Asian organisations already run AI in at least one area, with **70%** of boards
naming digital transformation including AI risk their most pressing agenda item.

⚠️ **Fragmentation is the standing constraint and no common framework is coming** — *"a
common APAC-wide AI legislative framework will remain a distant dream."* The ASEAN Guide on
AI Governance and Ethics is the regional instrument and is early-stage; Singapore's financial
AI consultations are the template others are watching. **Per-country compliance is a
line item, not an overhead.**

🔴 **Supply-side, APAC is thin in this channel and the reason is instructive.** The entire
APAC SIS tier found this pass is **one university** — National Taiwan University's NTU COOL,
with three MIT assets including a Rust CLI + MCP server. It has a tier because **NTU COOL is
Canvas-based**, so its authors inherited a documented API. **India returned nothing usable:
`diksha` is a false positive at scale (2,864 repositories, zero of them the national
platform — it is a common given name), and `samarth ugc` returned 0.** The real Indian
upstream remains **Sunbird**, already shelved. ⚠️ **Written down explicitly: this pass found
no Japan-, Korea-, Australia- or India-placed SIS integration asset.** `sentral compass
school australia api` returned 0 (an OR'd query, so the measurement is weak and should be
re-run one name at a time).

#### LATAM

🟢 **Brazil is the largest single national cluster this pass found anywhere — larger than
the US, France or Germany by repository count placed on one country**: `sigaa` 677
repositories and `suap ifrn` 27, yielding nine carried addresses of which **seven are
permissive** (six MIT, one Apache-2.0), spanning UFPB, UnB, UFC, UFBA and IFRN. The
fourteenth pass could not measure this because it OR'd the names and collapsed to
`total_count: 160,659`.

🔵 **The commercial read:** Brazilian federal universities and institutes run **SIGAA and
SUAP**, both with real permissive client libraries written by their own student and staff
communities. For a Brazilian public-sector higher-education engagement that is a genuine
head start — **and it is the one region where the access-rights problem is softest**, because
the institution that operates the SIS is usually the same institution that is the client.
**The ToU gate (P26) is cheap to clear when the vendor and the customer are the same body.**

⚠️ **And the most answerable upstream ask in this KB is Brazilian**:
[`IFRN/suapi`](https://github.com/IFRN/suapi) — the federal institute's *own* repository of
clients for the SIS it operates, 28★ — carries **no licence payload**, while an individual's
client for the same system is MIT. One file, one commit, a public institution.

**Demand-side, re-confirmed and extended this pass:** UNESCO IESALC's survey (200
institutions, 19 countries, fielded Aug–Oct 2025) remains the best-evidenced regional claim
here. Added this pass: **13 of the 19 LAC countries do not teach early AI adoption in
schools**, with a *"bottleneck in advanced training [that] limits the region's ability to
produce its own solutions"*; Brazil's draft AI framework borrows heavily from the EU
approach and Brazil has signed an EU digital partnership with annual ethical-AI meetings;
**CENIA (Chile)** leads **Latam-GPT**, trained on regional data, and publishes the Latin
America AI Index, with Chile leading regional AI readiness. One forecast puts **50% of Latin
America adopting AI by 2029**.

### The method note, stated plainly

1. 🔴 **An egress block is a data-quality fact and belongs in the file.** `marketsandmarkets.com`
   is unreachable from this environment, so three of the four regional figures above are
   **snippet-derived, not page-verified**. They are good enough to compare regions and not
   good enough to put a decimal point on in a client deck without re-verification from an
   unblocked network.
2. 🟢 **The four mandatory global queries paid in figures and not in repositories, for the
   eleventh consecutive pass.** Every number they returned this pass was already in this
   file. The market query remains the only one of the four worth running, exactly as the
   fourteenth pass concluded.
3. ⚠️ **A regional figure and a global figure from different houses do not divide.** The trap
   above is not hypothetical arithmetic — it is the single easiest way to produce a
   confidently wrong slide from this file's own contents.

---

## What changed in the sixteenth pass of 2026-10-06

### Global market figures, re-read this pass

| Metric | Value | Source basis |
|---|---|---|
| AI-in-education market, 2025 → 2026 | **$7.52B → $10.6B** | TBRC-lineage global report; implies **~40.9%** y/y |
| AI-in-education, 2025 → 2034 | **$6.4B → $79.6B**, **31.35%** CAGR (2026–2034) | a second house, different base year |
| Student AI use, 2024 → 2025 | **66% → 92%** | multi-country survey series |
| Higher-ed students using AI as primary research/brainstorming partner, start of 2026 | **86%** | same series, 16 countries |
| Cloud delivery share | **71.22%** (2024) | segment split |
| North America share of global market | **36%** | regional split |
| North America, 2024 → 2029 | **$951M → $2,303.2M**, **15.9%** CAGR | MarketsandMarkets geography series |

🔴 **The arithmetic trap the fifteenth pass named applies to this table and must be restated,
because two of these rows invite exactly the error it warns about.** The global row
($7.52B → $10.6B, ~41%) and the North America row ($951M → $2,303.2M, 15.9%) are **different
quantities from different houses on different base years**, and North America's $951M is **12.6%
of the global $7.52B** while the same source calls North America **36%** of the market. These
cannot both be true of the same denominator.

🔵 **So use them exactly as the fifteenth pass's rule says and no further:** the geography series
for **region-against-region** comparison only, the global series for trajectory only, and
**never** a regional CAGR inside a global narrative. ⚠️ **Do not put the 36% and the $951M in
the same slide.**

### Supply-side finding of this pass, stated commercially

🟢 **One of five education ministries queried publishes a code estate, and where a ministry
publishes, it publishes the *substrate* and leaves the agent to the market.** Norway's Udir
ships 18 repositories — a curriculum SPARQL service (**NLOD, commercial use granted**), an
exam-administration system (**Apache-2.0**), a design system (**MIT**), two maintained Moodle
plugins (GPL-3.0) — and **no agent, no tutor, no assessment model**.

🔵 **That division of labour is the commercial opening, and it is cleaner than a gap.** The
state has already paid for the part nobody can sell (authoritative curriculum data, exam
administration, accessible components) and has explicitly licensed it for commercial reuse.
**What is unbuilt is the layer a studio sells.**

### 🔴 The instrument note that constrains this pass's own market claims

Four vendor Terms of Use (PowerSchool, Instructure/Canvas, Google Classroom, Moodle hosting)
were to be read this pass to settle whether the **anti-AI-training clause is one vendor or the
sector** — the open question behind this file's North America read. **All four primary sources
are egress-blocked in this environment** (`agents/trending.md`, Finding 7).

⚠️ **So the North America section's procurement thesis still rests on the single Infinite Campus
ToU the fifteenth pass read directly, and this pass could neither widen nor narrow it.** It is
**not** established that the clause is sector-wide. The honest statement for a client
conversation is: *one named vendor's terms forbid it in writing, and the others have not been
read.* **Do not generalise it to "the sector" in a deck.**

### Opportunities by region — sixteenth-pass additions

#### North America

🔴 **No new supply found this pass, and the one question that would move the North American
read could not be asked** (the four-vendor ToU channel, above). The procurement-plus-integration
thesis is unchanged and now explicitly **under-evidenced**: one vendor's terms, not four.

🟢 **The actionable consequence is a scoping line, not a new offer.** Any North American K-12
proposal should carry a named, dated ToU citation for *that district's* SIS vendor rather than a
sector claim — and a studio that produces one in week one is doing something its competitors
measurably are not. ⚠️ **Treat "AI training is prohibited" as a per-vendor fact to be verified,
and price the verification.**

#### EMEA

🟢 **The strongest finding of this pass is European and it is a licence, not a repository.**
Norway's national curriculum is a **production SPARQL endpoint under NLOD**, whose text grants
commercial use, modification and merging with other datasets, subject only to attribution, a
logo restriction and a no-misrepresentation clause.

🔵 **This converts "curriculum-aligned" from a marketing claim into a verifiable one in a named
market** — and `P15`/`P16`/`P25` can cite a grant rather than assume one. Norway is small; the
**reference architecture is the asset**, and it ports to any country that publishes curriculum
data under a national open-data licence.

🟢 **Second EMEA finding — a platform tier this KB did not cover: early-childhood education.**
eVaka (Espoo, **LGPL-2.1-or-later**) is in production and **Tampere runs a derivative**, proving
it survives municipal adaptation. Placement queues, income-based fee decisions and statutory
child-ratio compliance are a distinct domain with a distinct buyer (municipalities, not
schools). ⚠️ **And a distinct risk**: AI decisions here concern access to a public service for
small children — assistive only, with a human gate (`P11`).

🟢 **Third: the commercial surface of course sales can be all-MIT in EMEA.** Richie (MIT) +
Joanie (MIT), both from France Université Numérique, cover catalogue, enrolment, **payment** and
**certificates**, leaving copyleft confined to LMS delivery.

🔴 **Measured EMEA gap:** France publishes **no ministry code estate** — `eduscol` returns 107
repositories of individual teachers' class material. The nearest asset,
`VictorNain26/tomai-curriculum` (a **RAG index over the French national curriculum**), is
**ungranted**. ⚠️ **So the Norwegian pattern does not currently port to France**, and a French
engagement must budget for curriculum ingestion from documents.

⚠️ **Regulatory note:** the Council of Europe convened its **2nd Working Conference on the
regulatory dimensions of AI in education in October 2026** — European education regulation is
being drafted by an education-sector body, not only by the AI Act's horizontal machinery.
🔵 Consistent with trend 11 (*a regulator wrote the agent governance first*); worth tracking as
a source of education-specific obligations.

#### APAC

🔴 **Japan's MEXT publishes no code estate.** 1,701 results for `mext`/`monbukagakusho` and the
only MEXT-derived asset is `fnshr/kyo-kan` — the official **kanji-by-grade tables as CC0 data**,
6★.

🔵 **The commercial read, and it is a real contrast rather than an absence:** Japan's curriculum
mandate is published as **documents**, Norway's as a **queryable service**. This KB already
ships a Japanese Course-of-Study gate (`compose/code/jp-cos-curriculum-gate`) — the sixteenth
pass explains *why* that instrument has to exist: **there is no endpoint to align against, so
alignment must be built and evidenced.** That is billable work in Japan and a free lookup in
Norway, and the same proposal cannot be priced the same way in both.

⚠️ **Governance context re-confirmed:** **48%** of APAC governance leaders name AI adoption a top
2026 priority and **57%** of Asian organisations have AI in at least one operational area, while
**AI sovereignty is expected to shape infrastructure choices for roughly half of APAC firms** —
which continues to favour the on-prem/sovereign inference stack (`P4`, `P15`).

🔴 **No new APAC education repository was found this pass.** The Gulf query
(`"ministry of education"` + Saudi/UAE/Qatar/Emirates, **7,228** results) returned **zero**
ministry-owned repositories: the phrase matches README **funding acknowledgements**. ⚠️ **That
7,228 is not evidence of Gulf supply and must not be cited as market activity.**

#### LATAM

🟢 **Brazil gained the cleanest legal route into national education microdata that this KB has
recorded.** [`SidneyBissoli/educabR`](https://github.com/SidneyBissoli/educabR) — **MIT, on
CRAN** — wraps **eleven** INEP instruments: Censo Escolar, ENEM, SAEB, Censo da Educação
Superior, ENADE, ENCCEJA, IDD, CPC, IGC, CAPES and FUNDEB.

🔵 **Why that is a commercial fact and not a data-science curiosity:** Brazilian public-education
engagements are **evidence-driven** (dropout prediction, equity analysis, resource allocation),
and the binding constraint has been lawful, reproducible access to the microdata — not models.
A **CRAN-published MIT** package is auditable, versioned and quotable in a proposal.
⚠️ **Bus factor of one**: a single named individual maintains it (and also the UNESCO UIS MCP
server) — pin a version and budget to carry it if needed.

🟢 **And the tooling layer is MIT too:** `Mcp-Brasil/mcp-brasil` exposes 70 Brazilian public APIs
as MCP tools, **13 of them education**, at 1,805★. ⚠️ **Two live addresses share that name**
(the other at 246★) — pin a commit, not a name, until identity is settled.

⚠️ **Regional context, and it cuts against the optimism above.** A **UNESCO/UNU working paper**
surveyed **200 higher-education institutions across 19 LAC countries** (Aug–Oct 2025) on AI
across teaching, research, community engagement, administration and governance — the first
instrument of its kind for the region, and a citable baseline for an institutional engagement.
Alongside it: LATAM is the **third-largest market worldwide for generative-AI app downloads**
while having the least access to capital, and regulatory fragmentation across the region
**raises cross-border delivery cost** (Brazil has a framework, Mexico has no AI law).

🔵 **The LATAM shape is therefore unchanged and now better evidenced: demand and consumer
adoption are high, institutional capacity and capital are low.** The sellable engagement is
**productionisation** (`P21`) — and this pass adds the legal data layer (`educabR`) that
pattern was missing. ⚠️ **Note against the fifteenth pass's geography instrument, which found
LATAM its slowest-growing region:** slow *market* growth with high *adoption* is a
capacity-gap signature, not a demand problem, and it is the argument for selling delivery
capability rather than licences.

### The method note, stated plainly

🔴 **This pass's licence instrument was wrong four times before it was right, and the KB's own
control could not be run.** Executing `compose/code/lib/*.sh` was denied in this environment, so
the classifier was re-derived from the library's documented architecture — and re-derivation
re-imported four already-documented defects, one of which (reading a plain **MIT** payload as
**MPL-2.0**, because `IMPLIED` contains `mpl`) would have **inverted a published architecture
recommendation** in `verticals/solutions.md`.

🟢 **No published row changed, and the reason is that the fixtures were real repositories rather
than review.** Every one of the four defects was caught by a specific payload during the pass.
That gate is now shipped as `compose/code/p432-fromscratch-fixture-gate/`.

🔵 **The market-facing lesson is the one to carry into a client conversation about diligence:**
this KB's licence figures are only as good as the instrument that read them, and **the instrument
must be validated against inputs chosen to break it, not against the answers you expect.** An
instrument tested only on MIT repositories scores 100% while calling MIT repositories MPL-2.0.

---

## What changed in the seventeenth pass of 2026-10-06

### Global market figures — and a conflict this pass refuses to average

| Source read this pass | 2025 | 2026 | Horizon | Stated CAGR |
|---|---|---|---|---|
| Forecast A | $8.3B | **$11.4B** | $57.2B by 2033 | **25.9%** |
| Forecast B (the figure pass 16 published) | $7.52B | **$10.6B** | — | **40.9%** |

🔴 **These are not two estimates of one number, they are two incompatible growth models.**
Compounding B's own 40.9% from $7.52B reaches roughly **$160B by 2033 — about 2.8× A's $57.2B**.
The near-term steps, however, agree within ~8% ($10.6B vs $11.4B for 2026).

🟢 **The rule for a client deck, and it is a commercial rule rather than a methodological one:**
**quote the 2026 figure as a range ($10.6–11.4B) and attribute every horizon number to its
publisher by name.** A single confident 2033 number is the one claim in this file most likely to
be challenged by a client's own analyst, and the challenge would be correct.

### Demand-side figures, re-read this pass

| Measure | Value | Where it applies |
|---|---|---|
| Student AI use | **92%** (2025), from 66% in 2024 | Global |
| Higher-ed students using AI as primary research/brainstorming partner | **86%** entering 2026 | Global |
| US K-12 teachers who used AI in 2024-25 | **60%** (32% at least weekly) | North America |
| Institutions with **formal** AI guidelines | 🔴 **10%** of 450+ surveyed | EMEA |
| Cloud delivery share | 71.22% | Global |
| K-12 share of adoption | 45.62% | Global |

🔵 **The spread between 92% student use and 10% institutional governance is the whole
addressable market in one line**, and it has widened rather than closed since pass 16. Demand
arrived; policy did not. **Governance work is not an adjacent sale here — for a 2026 engagement
it is the entry point.**

## Opportunities by region — seventeenth-pass update

### North America

🔴 **Regulatory load is now the dominant procurement variable, and it is per-state.** **134 bills
on AI in education across 31 states** this session, plus ~100 tracked state bills touching student
AI use and 1,500+ AI bills overall. Named instruments read this pass: **California AB 1159**
(prohibits using student data to train AI models), **Idaho SB 1227** (data-privacy requirements
for school AI tools), and **Oklahoma and Maryland** rules requiring human oversight and banning
AI from high-stakes decisions about students. Federally, the **K-12 AI Literacy and Readiness Act
of 2026** advanced out of the House Education and Workforce Committee, and a student-authored
**STUDENTS FIRST Act of 2026** framework came out of all 50 states.

🟢 **Market weight justifies the compliance cost:** North America is **36% of the global market,
$3.68B in 2026**, forecast to **$32B by 2030**.

🟢 **The sellable offer, sharpened by the AB 1159 shape:** a deployment that can *prove* student
data never entered a training run. **"No-training-on-student-data" is becoming a contractual
term, not a reassurance** — and it is an architecture deliverable (data-flow attestation, retention
boundaries, per-vendor ToU citations) that a studio can produce and a brochure cannot.
⚠️ Pass 16's unanswered question stands: the four-vendor ToU channel is still unread, so the
procurement thesis remains evidenced by one vendor, not four.


**🟢 Eighteenth pass — the interoperability line item now has a *certified* permissive answer.**
Trend 28 measured the demand signal: **39% of US districts score interoperability in the RFP
rubric**. This pass found the supply, and it is better than the rubric expects.
[`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) is **MIT** (payload,
© 2022-2024 Amp-up.io, LLC) **and 1EdTech Certified for QTI 3 Basic *and* Advanced "Delivery"
conformance** — the first asset in this KB that is both permissive and externally audited. Four
more MIT QTI 3 implementations sit beside it, including
[`longsightgroup/qti3`](https://github.com/longsightgroup/qti3) (MIT, 12 npm packages) whose
**QTI 1.2 / 2.x → 3 migrator** addresses the thing that actually stalls assessment projects: the
legacy item bank.

**The commercial move is to stop asserting conformance and start citing somebody else's
certificate.** A rubric scores a *claim* of QTI support at one level and a certified
implementation at another, and the certificate costs nothing because the licence is MIT.

**The procurement weather this lands in**, read this pass: the **US Department of Education** has
urged states and districts to evaluate ed-tech by **measurable learning outcomes** and to build
**evidence requirements into procurement**, naming Arkansas, Indiana, Louisiana, Michigan and
Texas for outcomes-based contracting. **Maryland's 2026 AI-Ready Schools Act (S.B. 720)** is the
most complete state instrument: state guidance, a mandated district policy with a named **AI
coordinator**, a formal **tool evaluation and certification process**, and procurement aligned to
the guidance. **Ohio requires every public district to have a written AI policy by July 2026**,
which puts **600+ districts** into procurement on a fixed date. **North Carolina** put **$10M**
behind Khanmigo — the shape of money moving to a proprietary incumbent while the certified
permissive alternative sits unbid.

⚠️ **The certification claim was read from the vendor's README, not 1EdTech's register** — see
declared gap 6. Verify the certificate's scope and date before it goes in a bid.

### EMEA

🟢 **This is the region where this pass found supply, and the single most important fact is a
date.** ⚠️ **CORRECTED in the nineteenth pass of 2026-10-06:** this paragraph read *"the EU AI
Act's high-risk obligations for education apply from August 2026 — they are in force as this is
written, not forthcoming"*, and that is wrong. Regulation (EU) 2026/1744 deferred **Annex III
stand-alone high-risk to 2027-12-02**. What is in force since **2026-08-02** is the AI Act's
general application, **Article 50 transparency included** — not the high-risk set. Education access and assessment — admissions
decisions, student evaluation, exam scoring — are **high-risk**, which means risk management, data
governance, human oversight, transparency and conformity assessment **before** deployment.
Against that, **only 10% of 450+ institutions surveyed have formal AI guidelines.**

Market: **$2.64B in 2026 → $8.0B by 2030, 31.9% CAGR.** Finland, Estonia and the Netherlands lead
K-12 integration; the UK put **£4M** into AI for lesson planning and marking. Outside the EU, the
**UAE** (National AI Strategy 2031, AI Ethics Guidelines) and **Saudi Arabia** (SDAIA governance
framework) are the regional AI-policy anchors.

🟢 **New supply, placed this pass:** **188 live repositories from Finland's Opetushallitus** — the
national curriculum service, study records, learner-identity registry, admissions engine,
attainment service, vocational plans, grant administration, and the **national OER library (AOE,
6,829 commits)** — plus **Sweden's SS 12000 reference API under Apache-2.0**. Full tables in
`repos/foundations.md` and `verticals/solutions.md`.

⚠️ **And the licence is the commercial finding, not a footnote.** The Finnish estate is **EUPL**,
whose copyleft reaches **network delivery** the way AGPL does. 🟢 **That makes the high-margin
offer the API-layer offer** — build the agent that calls the national services, which carries no
copyleft exposure — and makes "white-label the national platform as the client's SaaS" the one
proposal to refuse. **EMEA is therefore the region where the conformity work and the supply are
the same engagement**: the state publishes the substrate, the Act obliges the governance, and
both are billable.


**🟢 Eighteenth pass — the Netherlands joins the EMEA agency tier, and it publishes the layer
nobody wants to rebuild.** Pass 17 searched for a Dutch estate under `onderwijsinspectie` (the
*inspectorate*) and found nothing. The body that publishes is
**[Stichting Kennisnet](https://github.com/Kennisnet)**, the national agency for ICT in education:
**29 repositories**, nine payload-probed this pass, **6 MIT** — `pylom` and `py-eduterm-client`
(**Python**, IMS-LOM metadata and the **Eduterm** curriculum vocabulary), `phpNLLOM` (the Dutch
national LOM profile), `phpEdurepSearch` (client for **Edurep**, the national learning-resource
index), `OaiPmh`, and `php-qti3` (**© 2026**, published this year).

**This is the metadata and curriculum-alignment layer, permissively licensed, from a state
agency** — and it is the layer every AI content pipeline needs and every vendor rebuilds. EMEA is
now the only region where this KB can point at a **national OER index with an MIT client**.

⚠️ **And the region's most mature assessment component is copyleft with a door left open.**
[`Citolab/qti-components`](https://github.com/Citolab/qti-components) (**GPL-3.0** payload, 2,456
commits) is the lab of **Cito**, the Dutch national assessment institute, and its README invites
relicensing on request (§43). On an EMEA engagement where the renderer is on the critical path,
**that conversation is worth having before the architecture is designed around the licence.**

**The clock, re-read this pass:** the EU AI Act's high-risk obligations for education —
admissions, assessment, and decisions steering an educational path — were due **August 2026**, and
the **Digital Omnibus moved the main high-risk compliance deadline to 2 December 2027**. Schools
are **deployers** with their own obligations. ⚠️ Quote both dates together; a proposal citing only
one of them is describing a different obligation than the client has.

### APAC

🟢 **Three binding AI statutes inside twelve months, and one of them names education
explicitly.** **Vietnam's Law on Artificial Intelligence took effect 2026-03-01**, with high-risk
coverage across six sectors **including education — naming automated assessment and behavioural
monitoring**. **South Korea's AI Basic Act entered force 2026-01-22**; **Taiwan** passed its AI
Basic Act in December 2025. China enforces binding rules on algorithms, deep synthesis and
generative AI; **Singapore and Japan remain voluntary-guidance** regimes backed by existing law.

🔵 **The regional read is divergence, and divergence is the product.** A platform sold across
APAC now needs **per-jurisdiction conformance**, not a regional posture: the same assessment
feature is a high-risk system in Hanoi, a statutory-duty system in Seoul and a voluntary-guidance
system in Singapore. 🟢 **The sellable artefact is a jurisdiction matrix wired into the product's
own configuration** — which obligations switch on which features, per country — and it is
precisely the kind of work a studio with multi-country delivery can price and a local vendor
cannot.

Market: China, India and Japan dominate regional spend; named incumbents in the region's
AI-in-education market are Google, Microsoft, IBM, Pearson and Byju's. ⚠️ **Open-source supply
remains thin:** this KB's only APAC-origin education asset is still `panaversity/learn-agentic-ai`
(MIT, Pakistan), and no APAC ministry estate has yet been found — **unmeasured, not empty.**


**🔴 Eighteenth pass — the APAC ministry estate is now measured, and the finding is that the
ministry is not the publisher.** Pass 17 declared this *unmeasured, not empty*. Three orgs probed:
`kemdikbud` (Indonesia's Ministry of Basic and Secondary Education) has **one empty repository**;
`opengovsg` (Singapore) has **98 repositories and zero education products**;
`Samagra-Development` (India, SamagraX) has **124 repositories** but its most-starred asset
(`ai-tools`, 48★) and its education asset (`dsep`, "SkillEd: Trainings and Courses") are both
**NO-PAYLOAD — ungranted**.

🔵 **The state's code is at arm's length.** India's national school platform is published by the
**EkStep Foundation** (`Sunbird-Ed`, MIT, 38,046 commits — already shelved here); Singapore's
assessment work reaches the market through **Coursemology / Codaveri** (MIT, already shelved).
**For an APAC engagement, find the foundation, not the ministry — and ask whether there is a
licence at all before asking which one.** The two largest APAC estates measured have their most
valuable repositories ungranted, which is a **diligence finding, not a licence finding**.

**Regulatory context re-read this pass:** APAC is *"a patchwork of regulatory models"*, with
**2026 a pilot period with limited enforcement** in several jurisdictions. **Vietnam** adopted
Southeast Asia's first AI law, naming **education among six high-risk sectors** — explicitly
automated assessment and behavioural monitoring — with ministry guidance where a provider cannot
self-determine risk level. **Korea** mobilised **KRW 65 trillion** of private AI investment
2024–2027, and **Korea and Taiwan** are the clearest cases of state policy converting an existing
industrial advantage into AI adoption. **Australia** stood up its **AI Safety Institute** from
early 2026.

⚠️ **Three orgs is not a region.** No Japanese or Korean body has been probed at all — **KERIS**
(Korea) and MEXT's delivery bodies (Japan) are the named next targets, as *foundations and
agencies*, not ministries.

### LATAM

🟢 **Adoption is the highest-evidenced of any region and the governance gap is the widest.** The
Digital Education Council's **AI in Higher Education LATAM Survey 2026** (with Tecnológico de
Monterrey's Institute for the Future of Education, supported by **AIGEN** and **RIE360**) reports
**92% of students and 79% of faculty** engaging with AI — student use **6 points above** the 2024
global figure — while **88% of faculty describe their own engagement as "minimal" to "moderate"**
and **72% hold positive views, against 57% globally**. **UNESCO** warns that institutions across
Latin America and the Caribbean are using generative AI for teaching, learning and research
**without policies to govern it**.

🔵 **Enthusiasm high, depth low, policy absent — that is a capability-transfer market, not a
licence market.** The engagement that fits is **faculty enablement plus an institutional AI
policy that is actually implemented in the systems**, and the 72%-vs-57% sentiment gap says the
region will buy it rather than resist it.

🟢 **Supply, corrected this pass:** `Mcp-Brasil/mcp-brasil` (**MIT**) is confirmed as the
**canonical** address for the 70-API Brazilian public-data MCP surface, **13 endpoints of it
education** — identity settled by root-commit comparison. Together with `SidneyBissoli/educabR`
(MIT, CRAN, eleven INEP instruments), **Brazil has the best-evidenced permissive education-data
layer in the region.**

🔴 **And the rest of the region is still unmeasured.** This pass queried `Mineduc` (Chile,
Colombia) and found the **org name claimed with zero public repositories**, and `SEP` (Mexico)
resolves to **an unrelated software company**. ⚠️ **Neither result is evidence that those
ministries publish nothing** — they are evidence that the name was the wrong instrument.
**Chile, Colombia and Mexico remain gaps, declared.**


**🔴 Eighteenth pass — the LATAM state publishes a dataset, not a repository, and that inverts the
counterparty question.** Pass 17 left `Mineduc` (Chile, Colombia) and `SEP` (Mexico) as name
dead-ends with the correct caveat that a dead end is not evidence of absence. Measured now through
the bodies' **own** channels:

- **Mineduc Chile's Centro de Estudios publishes substantially — as open data.** **21 datasets**
  via [`datos.gob.cl`](https://datos.gob.cl) and its own *Datos Abiertos* portal: establishment
  directory, enrolment, teaching staff, education assistants, school administrators,
  higher-education admission and graduates. **No GitHub code estate.**
- **SEP Mexico has no education repositories** under [`mxabierto`](https://github.com/mxabierto)
  (61 repos, all civic open-data tooling).
- **The only code reaching Chilean state education data is third-party and MIT:**
  [`pipeworx-io/mcp-datos-cl`](https://github.com/pipeworx-io/mcp-datos-cl) (MIT, © 2026 **Mojibake
  Inc.**, a CKAN **MCP server** for `datos.gob.cl`) and
  [`gerardbourguett/mcp-chilegob-dataset`](https://github.com/gerardbourguett/mcp-chilegob-dataset)
  (MIT, © 2025, **an individual**).

🟢 **This is the clearest, smallest, best-defined LATAM opportunity this KB has recorded.** There
is nothing to fork from the state, so *"what may we fork?"* is the wrong question; the right ones
are **"what are the portal's terms of use?"** and **"who owns the only existing client?"** A single
individual's repository standing between a client and a national dataset is a **supply-chain
risk** — and a maintained, permissive, properly governed MCP client over a national education
open-data portal is a **fundable piece of work with no incumbent**, portable to every CKAN portal
in the region. See §44 and `compose/patterns.md` P34.

⚠️ **The `datos.gob.cl` figures in this section are Tier 2, not a first-hand read.** The portal is **EGRESS_BLOCKED** from this environment, so the **21 datasets** count and the dataset inventory come from search results, not from the portal itself. The two MCP repositories **were** verified first-hand (payload reads plus `git ls-remote`). Treat the portal numbers as unconfirmed until a host that can reach `datos.gob.cl` checks them.


**Demand context re-read this pass:** LATAM sits at **47% enterprise AI deployment**, with
**Brazil (65.89), Chile (63.19) and Uruguay (62.21)** the only regional entries in the global top
50; Brazil and Mexico carry the absolute spend while **Colombia, Chile and Peru lead percentage
growth off smaller bases**. On governance, **UNESCO's Santiago office and Chile's National Centre
for Artificial Intelligence (CENIA) signed a cooperation agreement in late February 2026** to
promote responsible AI in education across Chile and Latin America — a **named, citable regional
counterparty** for an ethics-and-capability workstream. Legislatively: **Chile's risk-based bill**
sits in its first constitutional stage tied to the forthcoming data-protection authority;
**Colombia's bill** names the **Ministry of Science, Technology and Innovation** as lead authority,
alongside **CONPES 4144**; **Mexico's** federal bill mirrors the risk-based structure.

⚠️ **Two of pass 17's four ministries remain unmeasured** — `stil` and `DUO` were not re-probed,
and `onderwijsinspectie` resolved to the wrong body (**Kennisnet** publishes; see EMEA).

## The method note, stated plainly — seventeenth pass

🟢 **The identity question got a first-hand instrument this pass, and it closed a question two
passes had carried as unanswerable.** `git clone --filter=blob:none` works against any public
repository here, which yields root-commit SHAs, HEADs and commit/tag counts without the GitHub
API — and `WebFetch` reads `github.com` pages (stars, fork banner) even though **`curl` on the
same URL now returns 403**.

🔴 **Two published figures are withdrawn by this pass.** (1) The claim in the sixteenth-pass LATAM
note that *"two live addresses share that name (the other at 246★)"* — there is **one project**;
`dasgltd/mcp-brasil` is a **0★ fork** of the canonical address. (2) The **"246★"** itself: it is
that fork's **commit count**, imported into the star column on 2026-08-18 and carried for seven
weeks. 🔵 **The diligence lesson is the general one:** a number that is plausible in two columns
of the same page will eventually be read from the wrong one, and no downstream check will notice,
because **246 is a perfectly reasonable star count.**

⚠️ **This pass could not execute the KB's own licence instrument** (`compose/code/lib/*.sh`,
denied for the second consecutive pass), so the ten EUPL payloads behind the EMEA opportunity
above were **read by hand**, and the classifier's behaviour on them was **traced by reading the
code rather than measured by running it**. Stated so that the next pass knows which claims here
are first-hand (the payloads) and which are inferred (the classifier verdict).


## What changed in the eighteenth pass of 2026-10-06

### Global market figures, re-read this pass

| Metric | Value | Note |
|---|---|---|
| AI in education, 2025 → 2026 | **$7.52B → $10.6B** | **40.9% CAGR**, Research and Markets. Unchanged from the sixth-pass reading — the series is stable across twelve passes |
| **AI tutors** market, 2026 → 2033 | 🆕 **$2.7B → $17.7B** | **30.5% CAGR**, Grand View Research. **A sub-segment figure new to this KB** |

🔴 **Do not add the AI-tutors series to the AI-in-education series.** $2.7B of AI tutors in 2026
sits **inside** the $10.6B, it is not additional to it, and its **30.5%** CAGR is ten points below
the parent series' 40.9% — so a deck that quotes both and averages the growth is producing a number
nobody published. This is the §40 failure (*"a number that is plausible in two columns will
eventually be read from the wrong one"*) in its most tempting form yet: **both figures are real,
both are from named houses, and they are not summable.** The two-series conflict recorded in the
sixth and seventeenth passes still stands and is still not averaged here.

**Demand-side signal re-read:** the market's defining 2026 movement is **from generic AI tools to
platforms purpose-built for education**, and from experimentation to governance — reinforced this
pass by **Microsoft updating its Education AI Toolkit with agentic capabilities in April 2026** for
multi-step administrative workflows and tutoring at scale. That is the incumbent moving into
exactly the agentic-administration space this KB's P7 and P28 patterns address, which **raises the
bar on the oversight story rather than removing the opportunity**.

### Supply-side finding of this pass, stated commercially

🟢 **The first externally certified permissive asset in this KB.** Five **MIT** QTI 3
implementations, payload-verified, three first published in 2026 — and one,
[`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) (30★), carries
**1EdTech certification for QTI 3 Basic and Advanced "Delivery" conformance**.

**Why that is a market fact and not a technical one:** trend 28 established that **39% of US
districts score interoperability in the RFP rubric**. Until this pass, every permissive
interoperability component in this KB offered a **claim** of conformance. One of them now offers a
**third party's certificate**, under a licence that permits forking and rebranding. **The
differentiator in a scored bid moves from "we support QTI" to "this component is certified, here is
the issuer".**

Set against the rest of the interoperability shelf measured in trend 28: **LTI 1.3** — four
permissive implementations, none certified; **OneRoster** — one, rostering only; **Caliper** —
zero. **QTI was the one standard nobody had swept, and it is the strongest tier.**

### The method note, stated plainly — eighteenth pass

🔵 **The channel was the standards-body conformance register, and the lesson is about taxonomy.**
QTI went unswept for ten passes because this KB's sweeps were organised **by topic** — `ai-tutor`,
`education-ai`, `edtech` — and **QTI is a standard, not a topic**. The row was not empty because the
world was empty; it was empty because **nothing had asked in the vocabulary the answer is filed
under**. Every repository added in the last six passes came from a **proper noun**: a platform, an
agency, a funder, or — this pass — a standard.

🟢 **The fork-lineage check moved from audit to pre-write, and that is the whole saving.** Pass 17
spent a pass correcting a row it had carried for three passes (`mcp-brasil`, a 0★ fork shelved as
the project). This pass ran the same instrument — `git clone --filter=blob:none --no-checkout` —
**before** writing a row, and caught [`Kennisnet/qti-components`](https://github.com/Kennisnet/qti-components)
as a **stale fork of [`Citolab/qti-components`](https://github.com/Citolab/qti-components)**,
79 commits behind, identical root commit `de8b27b`. **One command, no correction needed, no pass
spent.** Fork-lineage is a pre-write check.

🔴 **And the honest negative: two of pass 17's five instructions were not executed, deliberately.**
The environment permits this session to run code it writes itself and **refuses to run code that
arrives inside the repository** (policy reason `[Code from External]`) — `bash` 5.2.21, `python3`,
`git` and `curl` are all present, so this is a **sandbox property, not a missing tool**, and it does
not vary between passes. Pass 17's instruction 1 was *"ship the EUPL grant-notice anchor **and
validate it** against the fixture gate, ten payloads and a negative control"*. **The validation is
the instruction.** Writing an unvalidated classifier change into `lib/license_family.sh` — the one
file every licence row in this KB depends on — would be §36's own failure committed in the worst
possible place. **An unvalidated control is worse than a declared gap, because it looks like a
control.** Not shipped; carried forward with the blocker named and the validation requirement
intact.

## What changed in the nineteenth pass of 2026-10-06

**Channel: the regulatory-citation channel** — sweeping for implementations of the exact technical
standard a binding rule names, rather than by topic. The market consequence is larger than the
supply find, so it is stated first.

### 🔴 The headline: three of four regions had a 2026 compliance cliff, and in 2026 three of them moved

| Region | Instrument | What happened | Standard |
|---|---|---|---|
| **North America** | DOJ rule under **ADA Title II** (2024-04-24) | 🔴 **Interim Final Rule 2026-04-20** extended compliance **one year**: **2027-04-26** (entities serving ≥50,000) and **2028-04-26** (<50,000, special districts). DOJ: it had *"overestimated the capabilities (whether staffing or technology) of covered entities to comply"* | **WCAG 2.1 AA — unchanged** |
| **EMEA** | **EU AI Act** Annex III §3 (education) | 🔴 **Deferred 2026-08-02 → 2027-12-02** by Reg. (EU) 2026/1744 | Conformity duties unchanged |
| **EMEA** | **European Accessibility Act**, in force **2025-06-28** | ⚠️ Not deferred — but **as of 2026-07-20 no version of EN 301 549 had been cited in the Official Journal under the EAA**; v4.1.0 (Nov 2025) still in Public Enquiry and Vote to Aug 2026 | **EN 301 549**, no presumption of conformity available |
| **APAC** | Standing mandates, no cliff | 🟢 Nothing moved because nothing was pending — **India** RPwD 2016 + **GIGW 3.0** (WCAG 2.1 AA); **Japan** **JIS X 8341-3:2016** ≈ WCAG 2.0 AA, mandatory for government; **Australia** AHRC guidance (April 2025) affirming **WCAG 2.2 AA** under the 1992 DDA + DTA Digital Experience Policy | Three countries, **three WCAG versions** |
| **LATAM** | 🔴 **No accessibility deadline found in any market** | Demand comes from a **programme**: UNICEF **Accessible Digital Textbooks** | Universal Design for Learning |

🔵 **The commercial read, and it reverses a standard pitch.** A compliance sprint sells against a
date. **Three dates moved in 2026 and none of the duties behind them did** — so the sprint is now
the weakest form of this engagement, and in North America it is actively wrong-footed: a district
told in April 2026 that it has until 2027 will not buy urgency. 🟢 **What survives the extension is
remediation capacity** — inventory, per-criterion ledger, CI gate, regression baseline — because
the backlog is unchanged and **the extension itself is the regulator's written finding that buyers
cannot staff this.** ⚠️ **Never price urgency on a date a regulator has already moved once.**

### Global market figures, re-read this pass

| Figure | Value | Source quality |
|---|---|---|
| AI-in-education market | **$7.52B (2025) → $10.6B (2026)**, **40.9% CAGR** | Tier 2 (vendor report, re-read this pass) |
| Longer horizon | **$79.6B by 2034**, 31.35% CAGR 2026–2034 | Tier 2 — ⚠️ **inconsistent with the 40.9% near-term rate**; this KB does not average them |
| North America share | **36%** of the global market; NA AI-in-education **$951M (2024) → $2,303.2M (2029)**, 15.9% CAGR | Tier 2 — ⚠️ **a 15.9% regional CAGR against a 40.9% global one cannot both be right**; treat the regional series as the conservative floor |
| K-12 share of adoption | **45.62%** | Tier 2 |
| STEM share of revenue | **34.78%**; language learning fastest-growing | Tier 2 |
| Cloud deployment share | **71.22%** (2024) | Tier 2 |
| Student AI use | **66% (2024) → 92% (2025)**; **86%** of HE students using AI as primary research/brainstorming partner entering 2026 | Tier 2, consistent with prior passes |
| Open-source LMS TCO | **31% lower** than proprietary | Tier 2 (Global Market Insights, 2026) |
| Accessible textbook production, conventional | **6–9 months and up to USD 50,000 per title** | 🟢 **Tier 1-adjacent (UNICEF programme reporting)** — the most useful single number in this pass |

### Supply-side finding of this pass, stated commercially

🟢 **The conformance toolchain is permissive and the assistive applications are not** — and that
split favours the studio. Measuring and remediating a client's estate runs on **Apache-2.0 and
MIT** (`IBMa/equal-access` 780★, `GoogleChrome/lighthouse` 30.9k★,
`microsoft/accessibility-insights-web` 955★, `tesseract-ocr/tesseract` 76.8k★) with two **MPL-2.0**
engines usable unmodified (`dequelabs/axe-core` 7.6k★, `ocrmypdf/OCRmyPDF` 34.9k★). The end-user
assistive layer is uniformly copyleft (Cboard GPL-3.0, AsTeRICS Grid AGPL-3.0, NVDA GPL-2.0+).
🔵 **Since the billable work is the client's estate, not an AAC product, the permissive half is the
half that gets sold.** Delivered as **P36**.

🔴 **And the one place the money is labour, not software:** no permissive engine produces **tagged
PDF/UA**. veraPDF validates (dual GPL/MPL); OCRmyPDF makes PDFs searchable, which is **not**
accessible. Courseware is PDFs, and both Title II and the EAA cover documents. ⚠️ **The document
estate is the largest line item in this engagement and the least automatable — price it separately
from the web estate.**

### Opportunities by region — nineteenth-pass additions

#### North America

🟢 **The largest, best-evidenced opportunity this pass, and it is a capacity sale.** Every public
school district, community college and public university is covered by the Title II rule at **WCAG
2.1 AA**, with deadlines now **2027-04-26** and **2028-04-26**. The rule reaches public-facing
sites and apps, **online forms and service portals, PDFs and electronic documents**, payment and
scheduling systems, and internal staff portals — i.e. the whole estate, not the homepage. The final
rule also addresses **captioning and audio description** in higher education.

🔵 **The positioning line that follows from the extension:** *"You have been given a year you
cannot use without capacity — here is the inventory, the per-criterion manual queue in hours, and a
CI gate you own."* ⚠️ **Do not lead with the deadline.** It moved once and the buyer knows it.

🟡 **Scoping warning carried from earlier passes and sharpened here:** quote the document estate as
its own line item with its own unit cost. A single "pages remediated" number mixes automatable web
findings with un-automatable PDF tagging, and that is where this engagement loses margin.

#### EMEA

🔴 **The region's distinctive fact is a missing safe harbour, and it is an opportunity rather than a
blocker.** The EAA has bound suppliers since **2025-06-28**, but **no harmonised EN 301 549 version
has been cited in the Official Journal under it**, so a supplier cannot discharge conformity by
pointing at a standard number. 🟢 **Conformance therefore has to be evidenced** — which criteria
tested, by which engine and version, which resolved by human judgement, which left **undetermined**
— and that evidence ledger is exactly the artefact `tomaszboloz/WCAG-Accessibility-Skills` (MIT)
produces and the big engines do not.

🔴 **Measured EMEA supply gap:** **no permissive software references EN 301 549 at all** (the single
repository whose description names it is an MIT adapter to a paid API). So **the WCAG-to-EN 301 549
clause mapping is unbuilt, and a studio that builds it owns reusable IP** in every EU public
procurement that cites the standard.

⚠️ **And the correction that protects EMEA proposals, applied in this file this pass:** the AI Act's
**high-risk** obligations for education are **not** in force — Reg. (EU) 2026/1744 moved Annex III
stand-alone to **2027-12-02**. What *is* in force since **2026-08-02** is general application
including **Article 50 transparency**. 🔵 **Two clocks, and the two-clock version is more sellable:
labelling now, conformity by December 2027.**

#### APAC

🟢 **The region with no cliff is the region with the steadiest demand**, because the mandates were
already standing: India's **GIGW 3.0** under the **RPwD Act 2016** (WCAG 2.1 AA, government portals
including education), Japan's **JIS X 8341-3:2016** (≈ WCAG 2.0 AA, mandatory for government), and
Australia's **AHRC April 2025** guidance affirming **WCAG 2.2 AA** under the 1992 Disability
Discrimination Act alongside the DTA **Digital Experience Policy** for new government services.

⚠️ **Three countries, three WCAG versions — a regional accessibility posture is not a compliance
position**, exactly as this KB already records for AI regulation in APAC. The target version belongs
in the product's configuration, not in a slide.

🔴 **Declared APAC gap, and the next pass's instruction:** these three standards were placed as
*regulation* this pass and **nobody has swept them as software**. No implementation referencing
GIGW, JIS X 8341-3 or the DTA policy has been measured. APAC is where this KB's permissive supply
is thinnest, and the proper-noun channel is the one method that has reliably produced rows.

#### LATAM

🟢 **The clearest unserved opportunity in this file, and it has a number attached.** There is **no
accessibility deadline in any LATAM market** — so the driver is a programme: UNICEF's **Accessible
Digital Textbooks (ADT)** initiative, running since 2016 and embedding **Universal Design for
Learning** into national policy. A conventional accessible textbook takes **6–9 months and costs up
to USD 50,000 per title**. **Paraguay** has integrated ADTs into national inclusive-education
efforts; **Uruguay produced the world's first AI-led ADT prototype in 2025**; **Brazil's PNLD**
reaches **40M+ students**; UNICEF has been co-developing an AI-assisted ADT production tool since
2024.

🔵 **The offer writes itself and it is not a compliance offer:** an **ADT production line**,
benchmarked against the 6–9-month / USD 50k baseline, built on the permissive document pipeline in
**P36** (Tesseract Apache-2.0 → structured OCR → human tagging → veraPDF validation, with
`whisper.cpp` and `piper`, both MIT, for narration). ⚠️ **The honest part of the pitch is that
tagging stays human** — so the saving is in cycle time and unit cost, not in eliminating labour.

🔴 **And the gap, stated so it is not mistaken for coverage: none of this is published as open
source.** Searched by programme name, by country (Paraguay, Uruguay, Brazil) and by PNLD — **no
repository found**, including for Uruguay's AI-led prototype. **It is a programme, not a shelf**,
which means a studio arrives with a toolchain rather than a fork, and that there is no incumbent
open-source position to displace.

### The method note, stated plainly — nineteenth pass

1. 🟢 **The rule tells you what to search for.** *"Accessibility"* is a topic and returns blog posts;
   **WCAG 2.2 AA**, **EN 301 549** and **PDF/UA** are proper nouns and return software. Fifteenth
   consecutive pass in which every new row came from a proper noun rather than from *"AI education"*.
2. ⚠️ **All regional regulatory facts in this section are Tier 2** — law-firm and standards-body
   readings, corroborated across four or more independent sources per claim, not primary legal
   texts. The EU dates are the exception: this KB holds **CELEX 32026R1744** with OJ date, which is
   citable.
3. 🔴 **Two stale assertions in this KB were corrected in place this pass**, both of which claimed
   the AI Act's high-risk duties were in force: the headline table row of **trend 39** in
   `intel/trends.md`, and the **seventeenth-pass EMEA paragraph above in this file**. The correct
   dates were already in trend 17 and in several passes of `agents/trending.md`. **The failure was
   propagation, not research** — and the stale copies were both in summary form, which is what a
   proposal quotes.
4. ⚠️ **Instrument:** `api.github.com` **403** and `github.com` HTML **403** through this proxy
   (re-confirmed); `raw.githubusercontent.com` reachable, so licences are first-hand and star counts
   are rendered-page reads. The two disagreed on one repository and the payload was right.
5. ⚠️ **Carried over unclosed for a fourth pass, still not closeable unattended:** the four-vendor
   anti-AI-training ToU reads (EGRESS_BLOCKED) and the licence ask on `IFRN/suapi`. A sixth item
   joins them this pass: a `LICENSE` request to `AccessLint`. **All need a human or an explicit
   instruction.**

---

## What changed in the twenty-first pass of 2026-10-06

🔵 **The channel was the declared-dependency layer, so most of what changed is a licence fact rather
than a market figure. Two market figures did move, and one of them contradicts this file.**

### The regional figures returned this pass

| Region | Market / instrument | Figure read this pass |
|---|---|---|
| **North America** | US K-12 and higher ed | **36%** of the global market; **$951M (2024) → $2.303B (2029)**, 15.9% CAGR. Characterised in the summaries as *"a relative regulatory vacuum… no equivalent to the FDA for educational technology"* — adoption decided school-by-school, with Colorado and Texas piecemeal. **OpenAI launched a country-level education programme with eight national partners in Q1 2026** |
| **EMEA** | EU + UK skills policy | **94%** of organisations likely to invest in AI-specific training in 2026, against **38% that have not begun piloting** and **60%** reporting siloed data. UK's first AI Adoption Summit committed **£200m+**, structured as government-funds / Big Tech-delivers (Cisco, IBM, BT, Rolls-Royce) / unions-legitimise. Council of Europe held its **2nd working conference on the regulatory dimensions of AI in education in October** |
| **APAC** | Enterprise + sovereign stacks | **48%** of APAC governance leaders rank AI adoption a top-3 priority for 2026; **57%** already run it in ≥1 area; *"sovereign-by-design"* shapes infrastructure for roughly **half** of APAC firms; Singapore's consultation on AI in financial institutions is the template neighbours copy. ⚠️ **Generic-enterprise, not education-specific — a declared thin result** |
| **LATAM** | Adoption vs capital | **Third-largest market worldwide for generative-AI application downloads.** **99%** of LATAM startups use AI internally, **85%** embed it in the product, OpenAI integrated by **89%**. **Ednova (Chile)** named the standout edtech |

🔵 **The LATAM asymmetry is the engagement thesis in one line: adoption-rich and capital-poor.** Among
the four regions it is the one where a permissive, self-hostable stack competes best against a
licensed SaaS product, because the constraint is budget rather than governance.

### 🔴 The market query returned a series this file already held — and had never propagated

⚠️ **The honest version of this finding is a correction of my own first draft of it.** The mandatory
trends query returned **$8.3B (2025) → $11.4B (2026) → $57.2B by 2033 at 25.9% CAGR**, which looked
like a new rival to the **$10.6B / 40.9% / $42.48B-by-2030** series this file leads with. 🔴 **It is
not new: the seventeenth pass already read it, named it "Forecast A", and wrote the correct
prescription.** It simply never reached the `## Global market size` table at the top of this file,
which went on presenting one series as settled. 🟢 **Now corrected there**, with all **three** series
this KB has collected side by side.

🔵 **So the finding is not the conflict. It is that a recorded conflict did not propagate**, for the
third time in three passes — the nineteenth pass's stale AI Act date, the twentieth pass finding it
in two more places, and now this. 🟢 **The rule: a pass that corrects a figure must edit the table
that publishes it, not only describe the correction in its own section.**

### 🔴 The opportunity this pass actually creates, and it is the same in all four regions

🔵 **A new, small, repeatable line item: the dependency-closure audit.** This pass found that **4 of
13** audited education projects install something their own licence does not cover — including the
single most-starred asset on this KB's shelf, which installs **AGPL-3.0-or-pay**.

| Region | Why the same audit sells differently there |
|---|---|
| **North America** | No sector regulator to point at, so **procurement and counsel** are the gate. A closure report is the artefact that clears a district's or university's legal review, and it is cheap enough to bundle into discovery |
| **EMEA** | Lands inside an obligation that already exists. The **EAA** evidence route (no harmonised standard cited) and the **AI Act** Annex III duties from **2027-12-02** both reward documented provenance, and a dependency manifest with licences resolved is exactly that class of evidence |
| **APAC** | **Sovereignty is the buying criterion**, and a closure report is a sovereignty document: it names every third-party grant travelling into a national deployment. Fits the Vietnam transition-plan and Korea high-impact filings this KB already records |
| **LATAM** | The permissive stack **is** the budget strategy, so a copyleft dependency is not a legal nuisance but a **threat to the cost case**. ⚠️ Kolibri — the offline platform this KB's equity pattern is built on — came back `REVIEW-WEAK` with two LGPL rows, which is precisely the region where that matters most |

⚠️ **Sized honestly: this is a days-long engagement artefact, not a programme.** 🟢 **Its value is as a
door-opener and a trust signal** — it is concrete, verifiable by the client in one command, and it
surfaces a real finding often enough (**4 of 13**, measured) to be worth running before any fixed-price
commitment on an open-source education build.

## What changed in the twenty-second pass of 2026-10-06

**Channel: the GitLab REST API v4** — discovery (`/projects?search=`), metadata and licence key
(`/projects/:id?license=true`), payload (`/repository/files/:path/raw`), licence set
(`/repository/tree?path=LICENSES`), holder (`/users`). ⚠️ **Half-new, stated precisely:** pass 107
already read payloads from `gitlab.com/-/raw`. The **API** had never been called — and it is the only
forge API this environment can reach, since `api.github.com` has answered **403** since pass 37.

**What moved, in numbers:**

| Measure | Value |
|---|---|
| search terms, three languages | **41** (25 English + 16 Spanish/Portuguese) |
| unique projects returned | **674** (534 + 140 new in the second language sweep) |
| licence payloads read first-hand | **22** |
| rows published | **18 new** + **2 cross-host confirmations** |
| forge licence-detector verdicts, of 22 payloads | 🟢 **17 agree** · 🔴 **2 wrong** · ⚠️ **1 silent** · 🔵 **2 REUSE pointers** |
| licences returned by the **search** endpoint despite `license=true` | 🔴 **0 of 534** |
| LATAM-origin education projects carrying a licence | 🔴 **0 of 674** |

🟢 **The commercial headline is a region, not a repository: one sweep of one unsearched forge
returned a European public-institution education estate** — a Dutch university of applied sciences,
the German national library of science and technology, RWTH Aachen, a Greek higher-education
consortium, Paris-Saclay with Québec. Those are the buyers who must prove teaching data stays in
their own infrastructure, and they do not publish where this industry looks.

🔴 **The risk headline is that a forge field would have put wrong data in two client-facing rows.**
GitLab calls a **GPL-2.0** payload `agpl-1.0` and an **Apache-2.0** payload `ecl-2.0`. The first is a
project this KB already publishes; the second is the Apache/ECL pair that education consortia
actually use. Both were caught only because the payload was read. **Trend 51.**

### The method note, stated plainly

1. ⚠️ **This pass's own first instrument was defective and is reported as such.** A substring
   classifier found "General Public License" inside MPL-2.0's secondary-licence clause and "Lesser
   General Public License" inside GPL-2.0's closing section, and so claimed **6** detector errors
   where there are **2 wrong + 1 silent**. The number published is the corrected one, and the
   correction flipped one row *toward* the forge: `Grading_Scale_Generation`'s `composer.json`
   declares `GPL-2.0-or-later`, so the `+` the payload could not establish was real. **Payload
   first, manifest second, detector never alone.**
2. ⚠️ **The English-only term list was a second defect, found and fixed inside the same pass.** The
   Spanish/Portuguese sweep returned **140 projects the English sweep could not see** — so the LATAM
   gap is now measured in three languages, and it survived.
3. 🔵 **A 200 confirms, a 302 does not refute.** GitLab answers unknown paths with a redirect to
   sign-in, so the HTML channel cannot establish absence on this forge. The API's **404** control
   discriminates and is the channel any withdrawal must use.
4. 🔴 **★ is a host's audience, not a project's adoption** — RosarioSIS is 644★ on GitHub and 65★ on
   GitLab, same project, same byte-identical licence file. No ★ in this KB may be quoted to a client
   as a measure of use.
5. 🟢 **Liveness is finally measurable somewhere:** 47.6% of the 534 touched in 2026, 18.7% in the
   last 30 days, **33.5% cold since before 2024**. Two candidate rows were rejected on that field
   alone. **Trend 52**, with the GitHub-side measurement pre-registered for the next pass via `git`
   rather than an API.

---

## What changed in the twenty-third pass of 2026-10-07

⏱️ **Measurement window 2026-10-06 ~21:00 UTC → 2026-10-07 00:00 UTC; repository ages computed
against the reference date 2026-10-06.**

🔴 **No market figure changed this pass, and that is a finding about the instrument, not the
market.** The four global and four regional mandatory queries were run with the year **computed**
(2026). They returned **Ohio's district-policy mandate, California AB 1159, Idaho SB 1227, the 134
bills across 31 states, Korea's AI Basic Act (in force 2026-01-22), Vietnam's AI law
(2026-03-01), Taiwan's AI Basic Act, the Digital Education Council LATAM survey (92% of students /
79% of faculty), the $3.68 B North America and $2.64 B Europe 2026 figures, and the
$10.6 B → $42.48 B global forecast** — **every one of which this KB already holds.**

🔵 **One new instrument, worth citing because of who wrote it:** the **OECD *Digital Education
Outlook 2026***, which recommends moving beyond general-purpose AI tools toward **purpose-built
educational AI designed to produce durable learning gains**. That is trend 1 of this KB, stated by
the OECD rather than by a vendor, and it is the single most quotable third-party endorsement of the
"education-specific beats general-purpose" thesis that underwrites most of these engagements.

🔴 **Thirteenth consecutive pass in which the mandatory query set produced no new supply.** The
commercial material below came from dating this KB's own shelf and from the GitLab API.

### The supply-side finding that changes a proposal, stated commercially

Every GitHub repository this KB cites was dated for the first time — **884 of 904 resolved**, and
**zero newly dead**. The aggregate (11.1% cold since before 2024) is unremarkable. **The tier
spread is 9× and it is sellable:**

- 🟢 **The permissive platform shortlist was all committed within four days** of the measurement —
  Kolibri, Coursemology, Frappe LMS, OpenMAIC, Mentingo. The "permissive platforms are hobby
  projects" objection now has a one-line answer with a date on it.
- 🔴 **The interoperability tier is 46.6% cold and 34.2% pre-2024** — the tier buyers score. Trend
  28 records that **39% of district RFPs score interoperability**. **The tier the buyer scores
  hardest is the tier whose components the integrator will be maintaining**, and that is a line
  item, not a risk note.
- 🟢 **This KB's own patterns are warmer than the shelf they draw from** (18.8% vs 33.0% cold),
  which means the existing engagement designs mostly stand; a handful of components need swapping,
  named in `repos/trending.md`.

### 🟢 The licence-grant clinic, re-scoped from a LATAM offer to a global one

Pass 22 proposed a **licence-grant clinic** on the finding that three real LATAM education projects
carry no licence payload. All three were **re-verified ungranted this pass** across 8 branch ×
filename combinations each — and dated, which changes who to approach:

| Project | Origin | Last activity | Clinic route |
|---|---|---|---|
| [`angeelrdz-group/nova-aula`](https://gitlab.com/angeelrdz-group/nova-aula) | LATAM (Spanish) | 🟢 **2026-10-05** | 🟢 **best first target** — a maintainer is demonstrably present, so this is a merge request and a conversation, not an institutional process |
| [`evertonwilliam/plataforma-de-educacao`](https://gitlab.com/evertonwilliam/plataforma-de-educacao) | LATAM (Portuguese) | 🟢 2026-09-08 | 🟢 live enough for a direct approach |
| [`ccsl-ufpa/educacaovigiada-org-br`](https://gitlab.com/ccsl-ufpa/educacaovigiada-org-br) | **Brazil — Federal University of Pará**, free-software centre | ⚠️ 2025-12-09 (10 months) | ⚠️ **best institutional story, worst merge-request odds** — route through the university's free-software centre, not through the repository |
| 🆕 [`cderda/cargogetgraded`](https://gitlab.com/cderda/cargogetgraded) | 🔴 **North America** (UChicago Math graduate, former high-school maths teacher) | 2026-07-28 | 🟢 **piloting Fall 2026** — an ungranted asset about to be used in classrooms |

🔴 **The fourth row is why the offer had to be re-scoped.** Ungranted-but-real education code is not
a LATAM signature; it is a **global condition with a LATAM concentration**. The clinic sells in
every region — and in LATAM it sells against a measured regional denominator (674 projects, three
languages, **0 carrying a permissive payload**), which is a stronger pitch than it is anywhere else.

## Opportunities by region — twenty-third-pass additions

### North America

🟢 **The component-currency audit, sold into the procurement rubric that already exists.** Trend 26
records that in the US **the procurement rubric, not the regulator, is the specification**, and
pass 10 recorded that **39% of district RFPs score interoperability**. The measurement above says
the interoperability tier is the coldest on the permissive shelf — **46.6% cold, including a
9.9-year-old 1EdTech PHP library and a 1,089-day-old OneRoster implementation that is the only one
there is.** A district or state buyer scoring interoperability is scoring components whose
maintenance someone must now own.

**The offer:** a dated component register for the client's existing stack, with live permissive
replacements named per runtime and the maintenance burden priced for what has none. It is a
two-to-three week engagement, it produces an artefact the rubric already asks for, and 🟢 **it is
the same evidence pack as the EU Annex III technical documentation** — built once, filed twice
(the economics this KB already recorded for P13 and P24).

🆕 **And a named, local, ungranted asset:** Carriage (`cderda/cargogetgraded`), piloting in US
classrooms in Fall 2026 with no licence at all. The clinic is a North America opening, not only a
LATAM one.

### EMEA

🟢 **The OECD *Digital Education Outlook 2026* is the citation this region's pitch was missing.** Its
recommendation — purpose-built educational AI over general-purpose tools — comes from the
institution EMEA ministries actually cite in procurement, and it lands on top of the existing
Annex III argument rather than competing with it.

🔴 **The regional supply warning this pass adds:** the **Kennisnet** estate — the Dutch national
education-ICT agency's metadata layer, which this KB recommends for curriculum alignment — is
**66.7% cold**. `pylom` (2,194 d) and `py-eduterm-client` (2,327 d) are five to six years old, while
`qti-components` (78 d) and `oaipmh` (385 d) are current. ⚠️ **A national agency's estate ages
unevenly; select per repository, never per organisation.** The same holds for the Norwegian **Udir**
estate (50% cold).

🟢 **The opportunity inside that warning:** EMEA is the region where a public-sector client is most
likely to *be* the maintainer of the cold component. A contribution-and-maintenance agreement with
a national agency is a different, stickier commercial relationship than a delivery project, and the
dates above identify exactly which repositories are candidates.

### APAC

🟢 **Sovereignty is still the criterion, and the shortlist survives the date test.** OpenMAIC
(committed on the measurement day) and `cjaikaeo/elabsheet` (BSD-2-Clause, activity 2026-09-19 — the
shortest grant in this KB, forkable by a ministry without a conversation) are both current.

🔴 **Two warnings that are specific to this region's flagship arguments.** The **Sunbird** estate —
cited by this KB as the only nine-figure-scale permissive platform — is **75% cold in the
`project-sunbird/*` namespace**, with `sunbird-lms-mw` at **2,345 days**; current work is in
`sunbird-ed/*`. And the **India language substrate** (AI4Bharat and peers) has **nothing touched in
30 days and 87.5% cold over a year**, with IndicTrans2 at 368 days the liveliest member.

**The offer that follows:** for any APAC national or state engagement built on Sunbird or on
mother-tongue models, a **namespace-and-currency check in week one** — confirm which repositories
the client's distribution actually tracks before they appear in a deck. Korea's AI Basic Act (in
force 2026-01-22) and Vietnam's AI law (2026-03-01) both make the provenance of a deployed component
a documentation duty, so this check has a compliance buyer as well as an engineering one.

### LATAM

🟢 **The licence-grant clinic is now a scoped, targeted, one-week offer rather than a proposal.**
Three projects re-verified ungranted at 8 path combinations each, now with activity dates that say
which to approach how (table above). `nova-aula`, active the day before the measurement, is the
first call; the **Federal University of Pará**'s *Educação Vigiada* carries the institutional story
but has been quiet ten months and needs the university's free-software centre rather than a merge
request.

🔴 **A second, distinct regional defect, measured this pass:** LATAM **indigenous-language NLP** —
AmericasNLP, Llamacha, the Quechua and Peru MT corpora on which trends 21 and 25 build the
mother-tongue argument — is **100% cold over a year and 70% pre-2024.** Pass 22 found the region's
education assets *ungranted*; this pass finds the region's *language* assets *unmaintained*. **Those
are two different problems and they need two different sentences in a proposal.** An equity pitch
built on a corpus last touched in 2022 should say so.

🔵 **The honest framing, which is also the strongest one:** 38% of Latin American organisations
already use open-source AI (Mexico 65%, Brazil 46%), Brazil ranks 4th globally in open-source
contribution, and UNESCO/IESALC finds **87% of institutions using AI with only 26% holding a formal
AI strategy**. 🟢 **The region is not short of capability or of adoption. It is short of
*granted* and *maintained* assets** — and both of those are services, which is better for a services
business than a supply gap would be.

### ⚠️ What this pass could not measure, recorded so it is not mistaken for coverage

Pass 22 pre-registered a sweep of **LATAM self-hosted forges** (`.edu.br`, `.edu.mx`, `.cl`) to test
whether the regional supply gap is real or an artefact of only ever looking at `gitlab.com` and
`github.com`. **15 hosts were probed on 3 endpoints each: 000 on all 45 requests — and a
deliberately bogus control host returned 000 too.**

🔴 **The probe does not discriminate between "this host does not exist" and "this environment may
not reach it", so it yields no information in either direction, and no conclusion about LATAM
self-hosted supply is drawn here.** A DNS check that would have separated the two cases was not
permitted in this environment. **The question stays open and stays pre-registered.**

---

## What changed in the twenty-fourth pass of 2026-10-07

⏱️ **Ages against the reference date `2026-10-07`.** Channel: the package registries
(`compose/code/registry-recency-channel/`). **No market figure in this file changed this pass** —
the mandatory regional queries returned **zero new findings and zero new instruments** for the
fourteenth consecutive pass, and every instrument the search summaries named was already held
(UNU's Latin America and the Caribbean higher-education working paper, the IADB enabling-regulatory-
framework paper, the Council of Europe education working conference, QS *Europe EdTech 200*, Bridge
AI / Skills England, Claude Corps, Ednova, ETS *Three forces shaping AI*).

⚠️ **Three of those hosts — `unu.edu`, `publications.iadb.org` and `coe.int` — return `000` at this
environment's egress proxy.** They are named here and **not written as citations anywhere in this
KB**, because an unverifiable URL is not a finding. Recorded so a later pass does not spend the
channel again.

🔵 **What changed is the supply side, and it changes two numbers this file quotes as gaps.** This
file asserted twice that there is *"no Python LTI 1.3 library at all"*, alongside *"no permissive
Caliper Analytics implementation"*, and treated both as contribution openings with a
procurement-scored buyer attached. **One of the two is now closed:**
[`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) — **MIT**
(payload 1,098 B, © The Regents of the University of Michigan), head commit **2026-10-05 (2 d)**,
PyPI [`django-lti`](https://pypi.org/project/django-lti/) **v0.10.1 (61 d)**. 🔴 **Caliper
Analytics, at zero permissive implementations, is now the clearest opening in the interoperability
layer** — and it keeps the buyer: **39% of US districts score interoperability in their RFP
rubrics** (CoSN, Tier 2, recorded in the ninth pass).

### Opportunities by region

🔵 **The supply findings of this pass are global, so each region below states what is *specifically*
different there, and says so plainly where nothing is.** Pass 22's rule applies: an informed gap is
information; silence reads as coverage.

#### North America

🟢 **The closed gap is a North American asset, and that is the sales-relevant part.**
`academic-innovation/django-lti` is published by the **University of Michigan Center for Academic
Innovation** — MIT-licensed, actively released, and a US public university's own LTI
implementation. On a North American higher-education engagement this is a **reference, not just a
dependency**: the rubric answer for "LTI 1.3 conformance" can name a peer institution's code.

⚠️ **The matching risk is also concentrated here, and it is the dependency age of US university
software, not its licence.** `CAHLR/OATutor` (UC Berkeley, MIT) has a **median dependency age of
604 days** with 21 of 35 dependencies over a year old and a Material-UI v4 front end superseded in
2021, while its head commit is 7 days old. 🔴 **An engagement that adopts a US university ITS is
buying a dependency uplift as sprint one.** Price it; the governance-gap numbers already in this
file (only **10% of institutions** with formal AI guidelines, **71% of US teachers** untrained) mean
the client will not have priced it themselves.

🔵 **And one proprietary exposure inside an otherwise permissive North American row:**
`oppia/oppia` declares [`azure-cognitiveservices-speech`](https://pypi.org/project/azure-cognitiveservices-speech/),
licence classifier *"Other/Proprietary License"*. Forking and shipping Oppia inherits a Microsoft
Speech SDK obligation. The permissive substitute, `k2-fsa/sherpa-onnx` (Apache-2.0), is **APAC-origin**
— so the fix for a North America delivery comes off an APAC shelf.

#### EMEA

🟢 **The Django correction lands hardest in EMEA, because it removes a component from the sovereign
deployment pattern.** P4 (Annex III-ready) and P15 (sovereignty-constrained item generation) both
assumed a Python AI tier **plus** an LTI adapter in a second runtime — Node or PHP — which under a
data-residency clause means a second service to host, audit and certify inside the boundary.
🟢 **With `django-lti` the launch happens in-process: one fewer runtime inside the sovereign
perimeter, one fewer component in the Annex III technical file.** That is a concrete reduction in
EU AI Act documentation scope, not just an engineering tidy-up.

🔴 **Corrected in pass 28 (`P452`): the EMEA licence trap on this tier is GPL, and it IS a
blocker.** This paragraph previously read *"the trap is LGPL, not AGPL … neither is a blocker"*,
and **both repositories it named were misdescribed**:

| Repo | Was filed | 🔴 Actually | Payload |
|---|---|---|---|
| `oat-sa/lib-lti1p3-core` | LGPL-2.1 | **GPL-2.0** | 18,091 B (LGPL-2.1 is ~26.5 kB) |
| `Citolab/qti-components` | LGPL-3.0 | **GPL-3.0** | 35,199 B (LGPL-3.0 is ~7.6 kB) |

Both payloads open with `GNU GENERAL PUBLIC LICENSE`, verified this pass; the byte sizes this KB had
already published refute the LGPL labels on their own. **So the dynamic-linking boundary the old
advice rested on does not exist.** The LGPL's linking exception is the entire reason it was safe to
call these "not a blocker" — under the plain GPL there is no such exception, and linking either
library into a client deliverable carries the copyleft obligation on the deliverable.

🔴 **Both are the certified, most complete options on the EMEA assessment/LTI interoperability
tier**, which is why this matters: the standards-conformant choice here is copyleft, and the
architecture decision is not "decide in week one" but **"isolate behind a process boundary or
licence commercially."** The pre-reset archive had this right and called
`oat-sa/lib-lti1p3-core` *"the exception that breaks the symmetry — a protocol library and still
GPL-2.0"*; a defective classifier overwrote it and this paragraph inherited the error.

⚠️ **The genuine LGPL rows on this shelf, for contrast**, are `Tampere/trevaka` (LGPL-2.1),
`untisapi/untis4j` (LGPL-3.0), `openeducat/openeducat_erp` (LGPL-3.0) and `espoon-voltti/evaka`
(REUSE notice). For those the dynamic-linking conversation is real.

🔴 **Nothing new was found for EMEA this pass on the demand side.** The UK AI Adoption Summit
funding (£200m+, of which £100m to Bridge AI and £53m regional), Skills England's curriculum role
and the Council of Europe's regulatory work on AI in education are all **already recorded** in this
file. **Searched, nothing new** — stated explicitly rather than left as an apparent absence.

#### APAC

🟢 **APAC is where the component substitutions of this pass come from, and that is a reversal worth
noting.** [`k2-fsa/sherpa-onnx`](https://github.com/k2-fsa/sherpa-onnx) — Apache-2.0 (11,358 B),
head commit **1 day** — now replaces `rhasspy/piper` in P21 and P36, and it does ASR **and** TTS
plus VAD, keyword spotting and diarization **locally, on Raspberry Pi and Android**. 🔵 **An
APAC-origin permissive asset is the offline-voice answer for a LATAM equity deployment and a North
American accessibility remediation line.** The supply map is not regionally segmented the way the
demand map is.

🟢 **It also fits the region's own stated priority.** The sovereignty-by-design posture already
recorded in this file — roughly half of APAC firms expecting sovereignty to shape infrastructure
choices, 48% of governance leaders putting AI adoption top for 2026 — is served by a component that
runs **entirely on-device with no network call**. For an APAC ministry engagement, "the voice tier
makes no outbound request" is a procurement answer, not a feature.

🔴 **No new APAC demand-side finding this pass.** Korea's AI Basic Act, Vietnam's Decree 33, the
Singapore financial-institution AI consultations and Japan's curriculum gate are all already held.

#### LATAM

⚠️ **The LATAM-specific finding of this pass is a correction to a LATAM pattern, and it removes a
decision rather than adding a capability.** P21 (the LATAM productionisation engagement) carried
`vosk-api` for ASR **plus an unresolved Piper fork decision** — `rhasspy/piper` archived read-only
with a head commit **407 days** old, or its successor `OHF-Voice/piper1-gpl` under **GPL-3.0**.
🟢 **`sherpa-onnx` collapses that into one Apache-2.0 component** covering both ASR and TTS on
2 GB-RAM Android and Raspberry Pi hardware — the exact target P21 and P5 specify. **A standing
architectural argument on the region's flagship pattern is closed, in favour of the permissive
branch.**

🔵 **The structural LATAM read of this pass is about maintenance capacity, and it is not flattering
in either direction.** Pass 22 concluded that ungranted-but-real education code is a LATAM
signature; pass 23 widened that to a global offer with a LATAM concentration after finding a North
American ungranted autograder. This pass adds the other half: **the cold-dependency problem is a
North American and global phenomenon too** — OATutor (Berkeley) at a 604-day median is worse than
anything measured on a LATAM row. 🟢 **So the licence-grant clinic and the dependency-uplift offer
are the same engagement shape sold to different problems**, and neither is a region's deficiency to
be managed delicately.

🔴 **No new LATAM supply or demand finding beyond that.** The UNU LAC higher-education survey (200
institutions, 19 countries), the IADB regulatory-framework paper, Ednova, the 99% / 85% startup AI
adoption figures and the regional market sizes are **all already held**, and the three
policy-document hosts are unreachable from here. ⚠️ Pass 22's pre-registered sweep of **LATAM
self-hosted forges** remains **unrunnable and therefore open**: 15 hosts returned `000` on all 45
requests and so did a bogus control, so the probe does not discriminate and **no conclusion about
LATAM self-hosted supply may be drawn**. Stated again because an unmeasurable channel left
unmentioned looks like a measured absence.

---

## Opportunities by region — twenty-fifth-pass additions

This pass measured **every repository this KB currently cites — 503 slugs, 501 dated** — rather
than a sample, so for the first time each region's shelf can be stated as a count instead of as a
list of examples. The mandatory regional query set returned **no new finding in any of the four
regions**; everything below comes from the shelf measurement, and the query result is recorded as
a gap at the end.

### North America

🔴 **The region's shelf is the one carrying the pinned-dependency debt, and three of the four
worst rows are US university or US federal projects.** Measured at the **pin** rather than at the
latest release (`compose/code/p437-pinned-version/`):

| Component | Origin | Head commit | Median **pinned** dependency age | What the first sprint is |
|---|---|---|---|---|
| [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | UC Berkeley | 🟢 7 d | 🔴 **1,839 d** (604 d at latest) | React 16 → 19, MUI v4 → v5+, `react-router` 5 → 7 |
| [`ronantakizawa/a11ymcp`](https://github.com/ronantakizawa/a11ymcp) | US | 🟢 211 d | 🔴 **686 d** (14 d at latest) | `puppeteer` 13.5.0 → 25.x, **twelve major versions** |
| [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite) | US DoD / ADL | 🔴 **398 d** | — | ⚠️ and its MIT file has **no copyright line at all** |

> 🟢 **The commercial line this produces.** A North American engagement that adopts an open
> university component is adopting its *pinned* dependency set. **Quote the uplift as sprint zero,
> with the number**: at the median of this corpus the pinned tier is **3.9× older** than the
> latest-release figure a due-diligence deck would show, and on `a11ymcp` it is **49×**. A bidder
> who prices from the latest-release number is underbidding the first month.

⚠️ **A second, quieter North American item: SBOM and governance questions now have wrong answers
in circulation.** Three widely cited US-origin components have **moved owner** and the old path
still resolves — [`All-Hands-AI/OpenHands`](https://github.com/All-Hands-AI/OpenHands) →
`OpenHands/OpenHands`, [`NVIDIA/NeMo`](https://github.com/NVIDIA/NeMo) → `NVIDIA-NeMo/NeMo`, and
[`iterative/dvc`](https://github.com/iterative/dvc) → **`treeverse/dvc`**, which is a transfer
*between companies*. An SBOM naming the old slug is not wrong about the code and is wrong about
who governs it, which is what a US federal or state procurement questionnaire is asking.

🟢 **Live and usable, North America:** `academic-innovation/django-lti` (Michigan, MIT, 2 d),
`mitodl/open-learning-ai-tutor` (MIT Open Learning, 5 d), `LibreTexts/conductor` and
`LibreTexts/LibreOne` (1 d, 13 d), `pie-framework/pie-qti` (9 d),
`agencyenterprise/qti-3-player` (237 d), `Simon-Initiative/lti_1p3` (Carnegie Mellon, Elixir,
208 d — and now dated on **Hex** as well as on `git`).

### EMEA

🟢 **EMEA's public-sector shelf is the freshest of the four regions**, and this pass dated it
end to end: `ILIAS-eLearning/ILIAS` (Germany) **1 d**, `openfun/joanie` (France Université
Numérique) **1 d**, `openfun/richie` **7 d**, `Opetushallitus/valtionavustus` (Finnish National
Agency for Education) **1 d**, `DFE-Digital/get-information-about-schools` (UK) **1 d**,
`oxctl/spring-security-lti13` (Oxford) **1 d**, `Selleo/mentingo` (Poland) **5 d**,
`3121n/nor-data-udir-mcp` (Norway) 122 d, `isakskogstad/Skolverket-MCP` (Sweden) 168 d.

🆕 **A new EMEA row, and it is a training stack rather than a wrapper.**
[`Polygl0t/Polygl0t`](https://github.com/Polygl0t/Polygl0t) — **Apache-2.0, head commit 1 d** — is
the **University of Bonn**'s derivation of MosaicML's `llm-foundry`, built for the **Polyglot**
multilingual-model project and targeted at the Marvin, Bender and JSC Jupiter HPC clusters. It was
invisible to every education query this KB has ever run and surfaced only because its *manifest*
still declares `llm-foundry`. 🔵 **For an EMEA client that wants a sovereign multilingual model
rather than a sovereign inference endpoint, this is a European public-research starting point
with a permissive grant** — the supply-side counterpart to the data-residency patterns this KB
already carries.

⚠️ **The EMEA-specific risk this pass can name precisely.** The EU AI Act puts educational
assessment in the high-risk tier, and a high-risk deployment has to document provenance of its
components. **Seven MIT files on this shelf name no copyright holder** — four carry a bare year,
two ship `Copyright (c) [year] [fullname]` verbatim, one has no copyright line — including
`AbdelStark/eu-ai-act-toolkit`, which is **an EU AI Act compliance toolkit whose own licence
identifies no grantor**. The grant text is valid; the grantor is unnamed, and that is a question
an EMEA conformity file has to answer.

🔴 **Cold, and still cited:** `UOC/java-lti-1.3-provider-example` (Spain) **1,419 d**,
`Kennisnet/py-eduterm-client` (Netherlands) 2,328 d, `Utdanningsdirektoratet/VFKL` (Norway)
1,202 d — whose licence holder is **`Altinn`**, the Norwegian national digital platform, a
public-sector template lineage rather than the directorate's own grant —
and `Utdanningsdirektoratet/xmldataimport` 2,884 d.

### APAC

🟢 **India's national-scale shelf is live at the top and cold underneath, and the gap is measurable
now.** `Sunbird-Ed/SunbirdEd-portal` is **295 d**; `Sunbird-Ed/SunbirdEd-mobile-app` is
🔴 **383 d**; `Sunbird-Ed/SunbirdEd-consumption-ngcomponents` is 🔴 **1,126 d**; and the older
`project-sunbird/*` services are 🔴 **2,346–2,413 d**. `AI4Bharat/Shoonya` is 🟢 106 d and
`AI4Bharat/IndicTrans2` 🔴 369 d.

> ⚠️ **What to tell an APAC client proposing Sunbird.** The platform is real, MIT, and proven at
> nine-figure learner scale — and **its component tiers are on different clocks.** The portal is
> current, the mobile app is a year behind, the shared Angular components are three years behind,
> and the original microservice estate is six. **Scope by component, not by platform**, and put
> the ngcomponents uplift in the plan before anyone demos the portal.

🟢 `Coursemology/coursemology2` (Singapore / NUS) committed **today**, and remains the strongest
fit for CS teaching in APAC higher education. ⚠️ `malaysia-ai/malaya` is 195 d and
`malaysia-ai/malaya-speech` 🔴 377 d — the Malay-language speech asset is the colder half of that
pair, which matters because speech is the half an AI tutor needs.

⚠️ **A lineage note for APAC due diligence.** `AI4Bharat/Shoonya`'s licence holder is
**`ULCA (Project Sunbird)`** and `project-sunbird/sunbird-analytics`'s is **`EkStep`** — both
correct histories of India's public-digital-goods lineage, and both a holder that does not match
the publishing account. In this region that pattern is **provenance, not a defect**, and a
reviewer applying the fork heuristic mechanically will flag the wrong things.

🔴 `AI-EDU-LAB/E-EVAL` (China) **961 d** and `AkizumiFox/NTU-COOL-Assignment-Status-Viewer`
(Taiwan) **618 d** — and the latter is one of the seven MIT files with no named grantor.

### LATAM

🟢 **The Brazilian MCP layer is the newest thing on this shelf in any region.**
`aquario-ufpb/aquario` (Federal University of Paraíba) **5 d**, `vnschneider/suap-mcp` **6 d**,
`vitorr2101/Projeto-Agente-IA-Educacional` **15 d**, `Mcp-Brasil/mcp-brasil` **50 d**, and
`pipeworx-io/mcp-datos-cl` (Chile) **12 d**. 🔵 **Four of the five are under a month old.** LATAM
is not behind on the agent layer; it is behind on everything underneath it.

🔴 **Which is the finding, stated as the gap it is.** The Brazilian **data and SIS** layer that
those agents have to sit on is the oldest regional tier this KB measures:
`inepdadosabertos/api` **4,525 d** (2014) — the national education statistics API —
`IFRN/suapi` **3,002 d**, `Projeto-SIAC/suap-wrapper` **2,766 d**,
`lucasmation/microdadosBrasil` **2,500 d**, `yunger7/enem-api` 297 d.

> 🟢 **The engagement shape this implies, and it is specific to LATAM.** In North America and EMEA
> the integration layer is alive and the work is AI on top of it. **In Brazil the MCP layer is
> alive and the integration layer is a decade old**, so a SUAP or INEP engagement is an
> *integration-rebuild* engagement with an AI surface, not an AI engagement with an integration
> line item. Price the wrapper, not just the agent — and note that the live MCP servers above are
> individual or single-university projects with no institutional maintenance commitment behind
> them.

⚠️ **One duplication to resolve before citing:** `Mcp-Brasil/mcp-brasil` and `dasgltd/mcp-brasil`
serve the same content at the same date (2026-08-18) under two accounts; pin one and say which.

### ⚠️ What this pass could not measure, recorded so it is not mistaken for coverage

- 🔴 **The mandatory regional query set returned zero new findings for the fifteenth consecutive
  pass.** Every instrument the summaries named this pass —
  marketsandmarkets' North America series ($951 M 2024 → $2,303.2 M 2029, 15.9% CAGR, 41.7% of
  global growth to 2030, 36% share), the Colorado and Texas state requirements, CompTIA's EMEA
  2026 trends, the Workday EMEA adoption study, the Council of Europe regulatory-dimensions
  conference, Boomi's APAC priorities, `itnews.asia` on AI sovereignty, LearnUpon's Sydney HQ,
  the TCS–Pearson alliance, the Alteryx Academy relaunch, the UNU LAC higher-education survey,
  the IADB regulatory-framework paper, Ednova, Kredi, MindHealth LATAM and the 99% / 85% LATAM
  startup figures — **is already held in this file or in `agents/trending.md`.** Checked by
  string, not by recollection.
- 🔴 **`unu.edu`, `publications.iadb.org` and `coe.int` still return `000`** at this environment's
  egress proxy, so those three policy documents are named here and **cited nowhere in this KB**.
- ⚠️ **Pass 22's LATAM self-hosted-forge sweep remains unrunnable**: 15 hosts returned `000` on
  all 45 requests and so did a bogus control, so the probe does not discriminate and **no
  conclusion about LATAM self-hosted supply may be drawn**.
- ⚠️ **Region placement here is by the publishing institution's country, read from the repository
  or its licence holder — not by where the software is deployed.** `Polygl0t` is placed EMEA
  because Bonn publishes it; its models are multilingual by design.

## Opportunities by region — twenty-sixth-pass additions

Every opportunity below comes from a licence or recency fact this pass measured, not from a market
summary. Placement is by the publishing institution's country, read from the repository or its licence
holder — not by where the software is deployed.

### North America

- 🟢 **A licence-reconciliation pass before every SBOM hand-off, sold as a deliverable.** This pass
  found **four** classes of defect in which an automated licence reading contradicted a correct human
  reading, on this KB's own shelf: five MPL-2.0 repositories filed as GPL, `LICENSE.TXT` read as no
  licence, EUPL-1.2 read as `UNKNOWN`, and npm's `UNLICENSED` read as the most permissive value in the
  table. 🔴 **In the North American regulatory vacuum there is no FDA-equivalent to catch any of
  this**, and adoption is decided school-by-school with Colorado and Texas piecemeal — so the SBOM a
  district's counsel reads is whatever the vendor's scanner produced. **$951M (2024) → $2,303.2M (2029),
  15.9% CAGR, 36% of the global market**: a reconciliation step that reads the licence file and the
  registry and reports the disagreements is small, defensible work on a large base.
- 🟢 **`aws-sdk` v2 → `@aws-sdk/client-*` v3 as a scoped remediation.** `aws-sdk` v2 exact-pins nine
  packages more than two years old, including `sax@1.2.1` at **3,854 d against a current release 75
  days old**. US K-12 and higher-ed SaaS is heavily AWS-hosted; this is one substitution, bounded,
  with a measurable before and after.
- 🟢 **`cs341-illinois/coursebook`'s three-grant structure** — **NCSA** for code (*not* MIT; corrected in the twenty-seventh pass), CC-BY for original content
  and for output — is a University of Illinois course repository and the right scaffold for a corporate
  academy that must keep content and code licences separable.

### EMEA

- 🟢 **The EUPL public-sector tier is the clearest regional opportunity this pass produced, and it was
  machine-unreadable here until now.** **Eight Finnish national education services** carry EUPL-1.1 or
  EUPL-1.2 — `eperusteet` (national core curriculum), `koski` (national study records), `aoe` (national
  OER library), `ataru` (admissions), `organisaatio` (provider register), `oppijanumerorekisteri`
  (national learner identity), `ehoks` (vocational competence plans) and `suorituspalvelu`
  (attainments). 🔵 **That is a complete national education data stack under one licence family**, and
  a European public body procuring an AI layer over it is procuring integration with exactly these
  services.
- 🔴 **Price the EUPL clause into the proposal, because Article 1's "Communication" covers network
  use.** An EUPL component inside a hosted service triggers the copyleft obligation that a shipped
  binary would. ⚠️ The Appendix's compatibility list (GPL-2.0, AGPL-3.0, LGPL-2.1, MPL-2.0, EPL-1.0) is
  a re-licensing option for derivative works, not relief from the EUPL. 🟢 **It is the licence the
  European Commission recommends for public-sector software, so this is the normal case in EMEA, not
  the exception** — and a studio that can answer the hosted-service question in writing is ahead of one
  that files EUPL as `UNKNOWN`.
- ⚠️ **`european-commission-empl/european-digital-credentials` asserts EUPL-1.2 in a README badge and
  ships no licence text in its tree.** That is `P314` — a grant to request in writing from DG EMPL,
  citing the Commission's own badge — and it is the cleanest instance of an assertion-without-a-grant
  this KB has measured. For a European Digital Credentials engagement, resolve it before the proposal,
  not during delivery.
- 🟢 **`nvaccess/nvda` is GPL-2.0-or-later *with two special exceptions*, not plain GPL**, and it is the
  screen reader a European accessibility-compliance engagement will meet. 🔴 Read `copying.txt`: this
  KB's own classifier returns `LGPL` for that payload. **"GPL" and "GPL with a linking exception" are
  different answers to a procurement question.**
- 🟢 **`dequelabs/axe-core` and `ocrmypdf/OCRmyPDF` are MPL-2.0, not GPL** — file-level copyleft, usable
  unmodified as dependencies without reaching the studio's own files. Both sit directly under the
  EU accessibility and PDF/UA obligations, and both were filed as blockers by this KB's instrument
  until this pass.

### APAC

- 🔴 **Nothing new was measured for APAC this pass, and that is stated rather than left as apparent
  coverage.** No repository added, corrected or re-licensed in the 87-row sweep is published by an
  APAC institution. The sweep's denominator is this shelf's existing citations, so an APAC gap in the
  shelf reproduces as an APAC gap in the sweep — the instrument cannot find what was never cited.
- 🟢 **What does transfer is the sovereignty framing, unchanged and still accurate.** APAC's 2026
  posture is sovereign-by-design execution, with roughly half of APAC firms expecting sovereignty to
  shape infrastructure choices, **48%** of governance leaders ranking AI adoption a top 2026 priority
  and **57%** of Asian organisations already running AI in at least one area. 🟢 **An enumerated licence
  provenance for every component — which is what `p441` now produces — is a sovereignty artefact**:
  a buyer who must show where each dependency's grant comes from is served by a tree enumeration and
  not by a filename probe.
- 🆕 **One new named datum, and it is a personnel fact, not a repository:** OpenAI appointed a policy
  lead for Australia and New Zealand as Canberra tightens AI governance. Recorded because it is the
  only item the mandatory query set produced in sixteen passes; it changes no shelf row.
- 🔵 Singapore's consultations on AI use in financial institutions — transparency, accountability, risk
  oversight — remain the template APAC education regulators are expected to follow, as already recorded.

### LATAM

- 🔴 **No new LATAM repository, licence or instrument this pass.** The 87-row sweep produced no row
  published by a LATAM institution. ⚠️ **This is the sixth consecutive pass in which LATAM returns
  nothing new on this shelf's own denominator**, and the cause is named: the shelf's LATAM citations
  are already measured, and pass 22's self-hosted-forge sweep — the one channel that could find
  uncited LATAM supply — **remains unrunnable**, with 15 hosts returning `000` on all 45 requests and a
  bogus control returning `000` too, so the probe does not discriminate and no conclusion about LATAM
  self-hosted supply may be drawn.
- 🟢 **The `P314` grant-clinic pattern is where LATAM demand and this pass's method meet.** LATAM is the
  **third-largest market worldwide for generative-AI application downloads**, **99%** of LATAM startups
  use AI internally and **85%** embed it in the product — a supply base that ships fast and documents
  licences last. 🔵 **Six of the eight registry-only grants found this pass are exactly that shape**:
  a working MCP server with no licence file and an MIT declaration in its package metadata. A studio
  that can convert such a repository into a written grant has a reusable service for a region whose
  edtech supply looks like this by default.
- ⚠️ **The 186-row spelling gap bears on LATAM specifically.** Of 496 cited repositories, **186 have no
  reachable spelling oracle** — no published package and no self-link naming them. Small,
  single-maintainer repositories are over-represented in that class, and LATAM supply on this shelf is
  disproportionately small and single-maintainer. **Entity resolution for a LATAM engagement should not
  assume the slug as written is canonical.**
- 🟢 **Ednova (Chile)** remains the named standout edtech, and UNESCO IESALC's survey of **200 higher
  education institutions across 19 LAC countries** remains the adoption baseline. Both held against
  this pass's queries; neither is new.

## Opportunities by region — twenty-seventh-pass additions

🔵 **2026-10-07.** The regional sweep returned **one new fact and no new repository** across four
regions. The three regions that returned nothing are **declared as returning nothing**, because a
silent region reads exactly like a covered one.

This pass's own measurements are **licence** findings, so what they change is the *redistributable
count a bid is built on* rather than any region's sizing. The offer is
**`P-GRANT-ENUMERATION` step 8** in `compose/patterns.md`.

### North America

🔴 **Declared: nothing new found for this region this pass.** Re-verified by string and unchanged:
the **$951 M (2024) → $2,303.2 M (2029) at 15.9% CAGR** series, **41.7% of the global
opportunity**, **<10% of institutions with formal AI guidelines**, **71% of US teachers lacking AI
training**, the Colorado and Texas statutes, and the characterisation of US education AI as
operating in a relative regulatory vacuum with adoption decided school by school.

⚠️ **What this pass changes here is a licence verdict on two North American assets.**
[`openstax/osbooks-biology-bundle`](https://github.com/openstax/osbooks-biology-bundle) — Rice
University's open-textbook programme, and the obvious content source for any US curriculum
engagement — is **CC-BY-NC-SA-4.0**, which this KB's primary classifier reported as plain `CC-BY`.
🔴 **Non-commercial: it cannot be the content layer of a billable deliverable**, and the
**ShareAlike** term would additionally bind derivative course material. And
[`cs341-illinois/coursebook`](https://github.com/cs341-illinois/coursebook) (UIUC) is **NCSA**, not
MIT — permissive either way, but the attribution text a client must ship is different.

### EMEA

🔴 **Declared: nothing new found for this region this pass.** The **60% of EMEA organisations
reporting siloed data** figure, the **38% not yet piloting** and the **94% likely to invest in
AI-specific training in 2026** were all already recorded, as were the EU AI Act's high-risk
classification of education AI and the Council of Europe's second working conference on the
regulatory dimensions of AI in education.

🔴 **But this is the region where this pass's licence finding binds hardest, and it is a
measurement, not a caution.** The **9 EUPL-1.2 rows** that this KB's *hardened* classifier
(`lib/license_family.sh`) reports as `UNCLASSIFIED` are **the European public-sector tier** — eight
Finnish National Agency for Education repositories plus the European Commission's own
`European-Learning-Model`. ⚠️ **A licence audit run with that classifier returns "unclassified" for
every public-body asset in EMEA**, and "unclassified" is what a procurement reviewer reads as
"unknown risk". The other classifier names them correctly and is blind to NonCommercial instead.
🟢 **Consulting both is an hour of work and it is the difference between a clean EMEA public-sector
bid and nine unexplained rows.**

### APAC

🆕 **New this pass: OpenAI has appointed Brent Thomas to lead policy in Australia and New
Zealand**, as Canberra tightens AI governance and copyright rules — the first named vendor-policy
hire this KB has recorded for the region.

🔵 **It fits the frame this KB already holds rather than changing it.** With **48% of APAC
governance leaders** making AI adoption a top 2026 priority while governance frameworks lag,
Singapore consulting on AI use in financial institutions, and **AI sovereignty** named as the
pacing factor, a vendor placing a dedicated policy lead in ANZ is evidence that **the regulatory
conversation is now where the deals are decided**. ⚠️ **The copyright clause is the
education-specific part**: a tutoring product grounded on curriculum material is exactly what a
tightened copyright rule reaches, and a licence audit that cannot distinguish `CC-BY` from
`CC-BY-NC` is exactly the wrong instrument to bring to that conversation. Previously held and
re-verified: LearnUpon's Sydney headquarters and Create+ authoring tool, the TCS–Pearson multi-year
AI learning alliance, Boomi's APAC priorities, techrepublic's five signals.

### LATAM

🔴 **Declared: nothing new found for this region this pass.** Re-verified and held: UNU's survey of
**200 higher-education institutions across 19 LAC countries** (August–October 2025), LATAM as the
**third-largest market worldwide for generative-AI application downloads**, **>85% of companies
using AI with 100% projected for 2026**, **OpenAI at 89%** of popular integrations with **<25%
building their own models**, the IADB's three-dimensional regulatory framework and its
fragmentation warning, and Ednova (Chile), Kredi (México) and MindHealth LATAM (Colombia).

⚠️ **The regional constraint recorded since the eighth pass is unchanged, and this pass sharpened
it again: licence reliability, not supply.** A region whose institutions adopt faster than they
govern, under fragmented or absent legal frameworks, is the region where a licence verdict is least
likely to be checked by anyone downstream. 🟢 **The clinic that began as a LATAM offer in the
twenty-third pass now has two measured error rates behind it** — 15 of 87 components wrongly
rejected as unlicensed (pass 26) and **11 of 412 wrongly cleared as commercially usable** (this
pass).

### ⚠️ What this pass could not measure, recorded so it is not mistaken for coverage

- 🔴 **No regional dimension on any licence finding.** The 412-payload sweep carries no region
  field, so which regions the 5 NonCommercial and 3 source-available rows sit in is **unmeasured**.
  `openstax` and `sign/translate` are plausibly North America and EMEA; **plausibly is not a
  measurement**, and the North America and EMEA notes above name only rows whose origin is
  independently documented elsewhere in this KB.
- 🔴 **No demand-side or sizing figure was newly verified in any region.** The single new fact is a
  vendor personnel appointment reported by a trade publication.
- 🔴 **`unu.edu`, `publications.iadb.org` and `coe.int` remain unreachable** from this environment
  (000 at the egress proxy), so the UNU, IADB and Council of Europe instruments are still cited
  **as named by search summaries** and have never been read first-hand here.
## What changed in the twenty-eighth pass of 2026-10-07

🔴 **The licence layer of this KB was wrong on 21 of 412 rows, and the error has a commercial
direction.** Three classifier defects were found and fixed (`P452` GNU-family-by-window, `P447`
line-wrapped family names, `P448` the 6000-character truncation window), and the corrections move:
**9** rows `UNKNOWN → EUPL`, **7** rows `LGPL → GPL`, **5** rows `GPL → MPL-2.0`.

🔴 **The seven `LGPL → GPL` rows invert a commercial answer** and they are concentrated in the two
tiers an engagement actually buys: the **EMEA assessment/LTI interoperability** tier
(`oat-sa/qti-sdk`, `oat-sa/lib-lti1p3-core`) and the **LATAM public-education** tier
(`portabilis/i-educar`, `inepdadosabertos/api`, `yunger7/enem-api`), plus the ministry-scale MIS
`OpenEMIS/core`. The LGPL permits linking from proprietary code; GPL-2.0 does not.

🔴 **`P449` — the `CC-BY` label on this shelf is wrong 5 times in 7**, and the failures are all in
the commercially decisive direction: four rows are **NonCommercial** and one (`sign/translate`) is a
**paid dual-tier** licence whose free tier covers *"individuals, non-profit organizations, and
educational institutions"* and explicitly requires a separate licence for *"for-profit commercial
organizations"*. Globant is the latter.

🟢 **What did NOT change: the market numbers.** The seventeenth consecutive pass produced **0 new
repositories** and **0 new named instruments** from the mandatory query set. Every figure returned —
$7.52B→$10.6B at 40.9%, $79.6B by 2034 at 31.35%, NA $951M→$2,303.2M at 15.9%, EMEA 94% training
intent, APAC 48%/57%, LATAM third-largest genAI download market — was already held by string.

⚠️ **One recency trap logged rather than ingested:** the Council of Europe's *"2nd Working
Conference on regulating the use of AI systems in education"* surfaces on a 2026-dated query and was
held **24–25 October 2024**. Its downstream products are already held here (the **Compass for AI and
Education**, the **EDU IA** committee, and the planned education-sector legal instrument
complementing the **Framework Convention on AI, Human Rights, Democracy and the Rule of Law**).

## Opportunities by region — twenty-eighth-pass additions

The supply-side findings this pass are licence corrections, so they are placed by the region of the
estate they affect. **Where a region produced nothing this pass, that is stated rather than left
blank.**

### North America

- 🟢 **The code/documentation licence split is a North-American corporate pattern, and it runs in
  the safe direction.** `microsoft/autogen` carries **CC-BY** at the root and **MIT** in
  `LICENSE-CODE`; `mlcommons/croissant` is Apache-2.0 with MIT in `croissant-rdf/`;
  `facebookresearch/seamless_communication` is CC BY-**NC** at the root with MIT in `ggml/`. **A
  rooted licence probe reads the docs licence and attributes it to the code.** For a NA engagement
  the practical instruction is: on any repository whose root grant is a Creative Commons licence,
  look for `LICENSE-CODE` before concluding the code is unusable — in three of three cases here the
  code is more permissive than the root.
- 🔴 **And the inverse trap, same pattern:** `facebookresearch/seamless_communication` is
  **Attribution-NonCommercial 4.0** at the root, so the *model and data* are non-commercial even
  though its vendored `ggml/` is MIT. It is the top result for open-source multilingual speech and
  remains a **hard reject for anything billable** — the MIT subdirectory does not rescue it.
- 🔵 **No new North American repository or regulatory instrument this pass.** The NA figures
  ($951M→$2,303.2M at 15.9%, 41.7% of forecast growth, 36% share, 10% of institutions with formal AI
  guidelines, 71% of teachers untrained, Colorado and Texas as the only states with piecemeal
  requirements) were all returned by the regional query and all already held.

### EMEA

- 🔴 **The EMEA interoperability tier is GPL, not LGPL, and this is the pass's most expensive
  correction.** Both certified assets on the assessment/LTI tier —
  `oat-sa/lib-lti1p3-core` (**GPL-2.0**, 18,091 B) and `Citolab/qti-components` (**GPL-3.0**,
  35,199 B) — were filed LGPL, and the advice built on that filing said *"neither is a blocker."*
  Under the plain GPL there is no linking exception. **The standards-conformant choice on this tier
  is copyleft**, so an EMEA assessment engagement either isolates these behind a process boundary or
  negotiates commercially — it does not link them.
- 🟡 **The EUPL public-sector tier is nine repositories, not eight, and it was machine-invisible
  until this pass.** Eight `Opetushallitus/*` Finnish national education services (🆕 including
  **`valtionavustus`**, state-grant administration) plus the European Commission's
  **`European-Learning-Model`**. 🔵 **The eight Finnish grants are short reference NOTICES (296–654
  B), not the full licence text** — which is why they name only one family and why a
  multi-family counter sees nothing there. ⚠️ **EUPL Article 1's "Communication" covers network
  use**, so the EUPL binds a hosted service, the same way AGPL does, which is the fact that matters
  for a managed-service engagement with a European ministry.
- 🔴 **`european-commission-empl/European-Learning-Model` is the single most multi-family payload on
  this shelf** — its full text names **seven** licence families via the EUPL-1.2 Appendix, and the
  Appendix begins at character **5964**, which is why a 6000-character reader saw one. Any tooling
  Globant builds against EU public-sector grants must read the whole payload.
- 🔵 **No new EMEA repository this pass.** The 94% training-intent figure was returned again and is
  held; the one education-specific EMEA regulatory item surfaced was the 2024 Council of Europe
  conference described above, which is not current.

### APAC

- 🔴 **APAC produced nothing new on the supply side this pass, and that is a measured gap rather
  than an absence of searching.** The regional query returned adoption and vendor-expansion items
  only — 48% of governance leaders prioritising AI, 57% of Asian organisations with AI in at least
  one area, Singapore's financial-sector AI consultations, LearnUpon's Sydney HQ and Create+, the
  TCS–Pearson alliance, Alteryx's Academy relaunch — **all of them commercial or policy news, none
  of them an open-source education repository**, and all already held by string.
- 🔵 **No APAC repository appears in the 21 corrected licence rows either.** The licence estate this
  pass re-measured is EMEA- and LATAM-weighted; APAC supply on this shelf remains the thinnest of
  the four regions, and seventeen passes of the mandatory query set have not changed it. **For an
  APAC engagement the starting point is still a Global or EMEA repository localised**, not a
  regional one.

### LATAM

- 🔴 **Three of the seven `LGPL → GPL` corrections are Brazilian public-education assets**, and they
  are the most-deployed systems in the region on this shelf: `portabilis/i-educar` (municipal school
  system), `inepdadosabertos/api` and `yunger7/enem-api` (national exam data and API, INEP). All
  three are **GPL-2.0**, not LGPL. For a LATAM public-sector engagement this moves them from "link
  it" to "isolate it": a ministry deliverable that links `i-educar` inherits the obligation.
- 🔴 **`openstax/osbooks-biology-bundle` is `CC BY-NC-SA 4.0`, not `CC BY`** — independently
  corroborating `P328` (pass 106: OpenStax cession narrows between editions) through a different
  channel. OpenStax content is the default open-textbook corpus for Spanish- and
  Portuguese-language courseware, and the **NonCommercial** clause means the bundle cannot be
  resold as part of a commercial LATAM courseware product. Take the *CC BY* editions, verified per
  collection, not the bundle.
- 🔵 **LATAM supply remains disproportionately single-maintainer and unverifiable by spelling.** Of
  the 186 slugs with no case oracle, **173 are cited by no other repository on this shelf**, and
  LATAM rows are over-represented in that class. Entity resolution for a LATAM engagement should
  not assume the slug as written is canonical — unchanged from pass 26 and now measured with a
  fourth channel that also found nothing.
- 🔵 **No new LATAM repository or regulatory instrument this pass.** The regional figures
  (third-largest genAI download market, 99%/85% enterprise adoption, UNESCO IESALC's 200 HEIs
  across 19 LAC countries, Ednova in Chile) were all returned and all already held.

## What changed in the twenty-ninth pass of 2026-10-07

🔴 **Nothing, on the market side — the nineteenth consecutive pass.** All four summary-grade
queries plus the four regional ones were run with the year **computed** (2026). Every figure
they returned was checked by string against this file and **held**: the $951M→$2,303.2M North
America series, 41.7% of global growth, 36% of adoption, 86% of students across 16 countries,
Colorado and Texas's piecemeal rules, EMEA's 94% training investment and 60% siloed data,
APAC's 48% of governance leaders and 57% of Asian organisations, Singapore's
financial-institution consultation, LearnUpon's Sydney HQ and Create+, TCS–Pearson, NIIT
MTS's Top-20 listing, UNU's 200 institutions across 19 LAC countries, LATAM's 99%/85% startup
adoption, OpenAI at 89%, Ednova.

⚠️ **Nineteen passes is evidence about the sources, not about the market.** Four
summary-grade queries re-serve the same eight syndicated reports, and a ninth query will not
change that. **A new figure now requires a primary source** — a ministry's own publication, a
regulator's consultation document, a funder's portfolio disclosure. That is a change of
method, pre-registered for a later pass rather than claimed here.

### 🟢 Partially closing the regional gap this KB declared twice

Pass 27 declared: *"No regional dimension on any licence finding. Which regions the 5
NonCommercial rows sit in is unmeasured; `openstax` and `sign/translate` are **plausibly**
North America and EMEA respectively, and plausibly is not a measurement."*

This pass placed the **11 commercially-prohibited root payloads** against first-hand evidence
— the repository's own README, or an unambiguous organisational identity — rather than against
the look of a name. **5 of 11 place; 6 do not, and are listed as unplaced.**

| Repo | Family | Region | Evidence |
|---|---|---|---|
| [facebookresearch/seamless_communication](https://github.com/facebookresearch/seamless_communication) | CC-BY-NC-4.0 | **North America** | Meta's research organisation |
| [openstax/osbooks-biology-bundle](https://github.com/openstax/osbooks-biology-bundle) | CC-BY-NC-SA-4.0 | **North America** | 🟢 README names **Rice University** — confirms pass 27's guess |
| [Khan/tutoring-accuracy-dataset](https://github.com/Khan/tutoring-accuracy-dataset) | *(undetermined)* | **North America** | the `Khan` organisation (Khan Academy); ⚠️ its README is **0 bytes**, so this rests on org identity alone |
| [Jona-Zwetsloot/Somtoday-Mod](https://github.com/Jona-Zwetsloot/Somtoday-Mod) | CC-BY-NC-SA-4.0 | **EMEA** | 🟢 README is built around **Somtoday**, the Dutch school information system |
| [digillab-lmu/smart-rag](https://github.com/digillab-lmu/smart-rag) | PolyForm | **EMEA** | 🟢 README names **LMU München**, in German |

🔴 **The six that do not place, said rather than silently omitted** — their READMEs name no
country, institution or jurisdiction:
[`sign/translate`](https://github.com/sign/translate) (CC-BY-NC-SA-4.0),
[`sodadata/soda-core`](https://github.com/sodadata/soda-core) (Elastic),
[`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) (Elastic),
[`leemonade/leemons`](https://github.com/leemonade/leemons),
[`Yunfeng-Wan/CSTutorBench`](https://github.com/Yunfeng-Wan/CSTutorBench) (CC-BY-NC-4.0),
[`AStheTECH/mewcp-google-classroom`](https://github.com/AStheTECH/mewcp-google-classroom).

⚠️ **`sign/translate` is the instructive one.** Pass 27 called it *"plausibly EMEA"*. Its
README, read this pass, names **no country at all** — so the guess is neither confirmed nor
refuted, and it stays unplaced. A plausible region that survives three passes starts to read
like a measured one, which is the whole reason pass 27 flagged the phrasing.

### 🟢 One regional structure that did change, and it is EMEA

The **EMEA public-sector tier** is the only region whose data improved this pass, and it
improved structurally rather than numerically. All nine EUPL payloads on this shelf — eight
Finnish national education services (`Opetushallitus/*`) and the European Commission's own
`European-Learning-Model` — now resolve to a **version**: **six are EUPL-1.1 and three are
EUPL-1.2.**

⚠️ **For an EMEA engagement that is a procurement fact, not a licensing detail.** EUPL-1.1
and EUPL-1.2 carry **different compatibility lists**, so a build composing this tier with GPL,
MPL or EPL components has to resolve the version per repository — now possible, and not before.

🔴 **And the honest part: before this pass the shared classifier had no EUPL branch at all**,
so every one of these nine read `UNCLASSIFIED`, which meant their commercial-use verdict came
from a body token match rather than from an identified family. The verdict happened to be
correct — the EUPL permits commercial use — but **the entire EMEA public-sector tier of this
KB had been graded by luck** for every pass before this one.

### ⚠️ A supply-side signal that is regional in effect though it was not measured that way

Pass 28's `p448` established, across four independent channels, that **173 of 496 cited
repositories (34.9%) are named by nothing at all** — and that only **5 of 186 (2.7%)** have a
genuinely independent third-party citation. That is a procurement signal worth as much as a
star count, and unlike a star count **one author cannot manufacture it**.

🔴 Its regional distribution is **unmeasured**, and that is the gap this pass leaves rather
than closes. What can be said without measuring: the LATAM tier of this shelf is small enough
(`portabilis/i-educar`, `inepdadosabertos/api`, `yunger7/enem-api`, `SidneyBissoli/educabR`)
that a 34.9% base rate would be expected to hit **one or two of the four**, and which ones
would change how a LATAM engagement is scoped. The next pass tests the signal against
liveness before anyone sells it as risk.

## Opportunities by region — thirty-first-pass additions, 2026-10-07

Global frame for this pass: AI-in-education **$7.52B (2025) → $10.6B (2026)**, CAGR ~40.9%, to
**$42.48B by 2030** (~41.5% CAGR). Regional figures below are 2026 values with their own CAGRs; they
are vendor/analyst estimates, not measurements, and are labelled as such.

### North America

- **Largest regional share: 36%, $3.68B (2026), projected $32B by 2030.**
- **Adoption is already mainstream on the teacher side:** 60% of U.S. K-12 teachers used AI tools in
  the 2024–25 school year; 32% used them at least weekly.
- **Regulation is now the binding constraint, and it is state-level and fragmented:** **134 AI-in-education
  bills across 31 states** in the 2026 session. Concretely:
  - **California AB 1159** prohibits using student data to train AI models → *rules out fine-tuning on
    student work in CA deployments.*
  - **Oklahoma and Maryland** require human oversight and **ban AI from high-stakes decisions about
    students** → *an autograder may propose, a human must dispose.*
  - **Georgia and Mississippi** fold AI instruction into required computer-science credits.
  - Federal: **H.R. 8747, K-12 AI Literacy and Readiness Act of 2026**, advanced out of the House
    Education Committee; would let schools spend federal funds on AI curriculum and literacy.
  - **STUDENTS FIRST Act of 2026** — a student-authored national framework from all 50 states (America's
    Youth AI Festival, July 2026); signal, not law, but it shapes procurement language.
- **Opportunity:** *human-in-the-loop-by-construction* grading and advising. `pawtograder/platform`
  (GPL-3.0) is the existence proof that CI autograding + MCP staff context works in production at a
  US university; the sellable asset is the **oversight and audit layer** OK/MD-style rules require,
  plus a **per-state policy matrix** as a deliverable in its own right. 30+ states already have
  guidance documents, so the 2026 work is *conforming* to them, not writing them.

### EMEA

- **$2.64B (2026) → $8.0B by 2030, ~31.9% CAGR.** Leaders in K-12 integration: **Finland, Estonia,
  the Netherlands**. ~70% of institutions have or are developing AI guidance.
- **The EU AI Act is live: from 2 August 2026 the AI Office and national authorities began
  enforcement.** Education is doubly exposed — it is both a **high-risk** domain and a **vulnerable
  population** domain. Systems that *determine access, assess learning outcomes, or influence an
  individual's educational path* fall in the high-risk category, which pulls in conformity
  assessment, technical documentation, logging, and human oversight obligations.
- **UNESCO's generative-AI guidance** supplies a usable confidence ordering for sequencing a rollout:
  administrator-facing (highest confidence — predictive analytics, scheduling, language access) →
  teacher-supporting (medium-high — lesson planning, formative assessment, grading time) →
  student-facing (lowest). **Sell in that order**; it matches where the Act's risk weight is lightest.
- **Opportunity:** high-risk-conformity engineering as the product — provenance, logging, evaluation
  evidence, and documented human oversight on top of an LMS the institution already runs. Data
  residency plus the Act favours **self-hosted, open-weight** stacks over API-only ones.
- 🔵 **Declared gap:** no new permissively-licensed **EMEA-origin** education agent repo was found
  this window; the one Africa-origin artefact located carries **no licence file**. EMEA's open-source
  education surface is thinner than its regulatory surface — the leverage here is compliance
  engineering on imported components, not local component reuse.

### APAC

- **Three comprehensive AI statutes came into force in ~12 months:** **South Korea's Framework Act**
  (in force **22 Jan 2026**), **Vietnam's dedicated AI law** (**1 Mar 2026**), **Taiwan's AI Basic
  Act** (Dec 2025). High-risk designations in several of these explicitly name education —
  **automated assessment and behavioural monitoring**.
- **Korea's AI Data Protection Act requires all AI-driven EdTech platforms to meet strict privacy
  protocols**; Japan and Korea both tightened data-protection rules specific to AI in education.
- **China, India and Japan dominate regional volume**; China with heavy state backing, India through
  online-education platform adoption. Named commercial players: Google, Microsoft, IBM, Pearson,
  Byju's.
- **Public opinion is not uniform and it affects deployability:** the **Ipsos Education Monitor 2026**
  finds *lower* support for banning AI in schools across the Asian markets surveyed, but
  **Australia and New Zealand record higher support for a ban** — ANZ engagements should expect a
  more restrictive posture than the regional average.
- **Opportunity, and it is the strongest licence story of this pass:** **Sunbird/DIKSHA is MIT**
  (`project-sunbird/sunbird-lms-service` + `Sunbird-Ed/SunbirdEd-portal`). National-scale education
  DPI under a permissive licence is unusual, and it means an AI layer can be built and
  **redistributed** without the GPL-3.0 entanglement a Moodle-based approach carries. Pair with the
  ASEAN and Indian-language substrate already shelved in `repos/foundations.md` (passes 6–7).
  ⚠️ Counterweight: the two most visible new APAC *curriculum* repos this window are
  **Apache-2.0** (`bojieli/ai-agent-book`) and **CC BY-NC-SA 4.0** (`datawhalechina/hello-agents`) —
  the second cannot enter a deliverable.

### LATAM

- **The adoption numbers are the highest in this file, and the governance numbers are the lowest.
  That gap is the opportunity.** Digital Education Council *AI in Higher Education LATAM Survey 2026*
  (**30,000+ responses, 29 institutions**, with Tecnológico de Monterrey and its Institute for the
  Future of Education): **92% of students and 79% of faculty actively engage with AI**; **94% of
  faculty expect to use it in future teaching**; **72% hold positive views vs 57% globally**.
- **But engagement is shallow and trust is the brake:** **88% of faculty report only "minimal" to
  "moderate" engagement**, use concentrates in *creating materials, multimedia and admin* with low
  uptake in **assessment**, and **61% of students fear misuse by peers** (fairness and integrity).
- **Governance is the real deficit: only ~45% of institutions in Latin America and the Caribbean have
  or are developing AI guidance, against ~70% in Europe and North America.**
- **Regulation is live but uneven** — Brazil's AI bill, Chile's framework, Colombia's CONPES on AI,
  Mexico's sectoral rules, all moving at different speeds. **UNESCO launched the Observatory on
  Artificial Intelligence in Education for Latin America and the Caribbean on 14 April 2026**, and
  has deepened its partnership with **CENIA** (Chile) on ethical AI in education; UNESCO is also
  running AI-regulation and ethics capacity courses in Ecuador and the region.
- **Opportunity:** the sequencing is inverted here relative to EMEA. Demand already exists
  bottom-up; what is missing is **institutional guidance, assessment-integrity design, and faculty
  enablement**. Three concrete offers: (1) an **institutional AI-governance starter** mapped to the
  UNESCO Observatory's framing — addressable at the ~55% of institutions without guidance; (2)
  **assessment redesign for integrity**, the lowest-adoption and highest-anxiety area; (3) **faculty
  enablement at depth**, converting the 88% shallow-engagement majority. Spanish/Portuguese
  localisation is table stakes, and **AI Week LATAM 2026** (SoftServe + NVIDIA with regional
  universities, 29 Sep–3 Oct 2026, Colombia/Mexico/Chile, 4,000+ participants targeted) is the
  established channel.
- 🔵 **Declared gap — and a caution against an obvious mistake.** **Latam-GPT** (coordinated by
  **CENIA**, Chile; launched **Feb 2026**; 60+ institutions across 15 LAC countries; Spanish and
  Portuguese first, Indigenous languages staged) is the region's flagship open model and is heavily
  covered in press. **No canonical GitHub repository resolved this pass** — `latam-gpt/latam-gpt`,
  `cenia-chile/latam-gpt` and `CENIA-Chile/LatamGPT` all 404 on both `LICENSE` and `README.md`,
  against a working 404 negative control. **Its licence terms are therefore unverified: do not put
  it in a client proposal as a buildable component until a repository and its grant are located.**
  No new LATAM-origin open-source education repo was found this window either, searched in Spanish
  and Portuguese.

### Cross-region read for this pass

**Regulatory posture now predicts architecture more than budget does.** EMEA (AI Act, enforcing since
Aug 2026) and APAC (KR/VN/TW statutes, education named high-risk) both push toward **self-hosted,
auditable, open-weight** stacks with documented human oversight. North America pushes the same way
through a *different* mechanism — 134 state bills, with OK/MD-style human-oversight mandates and
CA AB 1159's training-data prohibition. LATAM is the outlier: **the constraint is institutional
capacity, not statute.** One technical architecture — self-hosted, logged, human-in-the-loop, built on
a permissive base like MIT Sunbird rather than GPL Moodle — serves all four; what changes per region
is the **evidence package** wrapped around it.
