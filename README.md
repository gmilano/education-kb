---
industry: education
region: Global
updated: 2026-11-16
---

# Globant AI Studios — Education KB

## Pass `p852` · `2026-11-16`

🟡 **`13` permissive rows filed, and NOT ONE of them is a new discovery: `13` of the `17`
addresses this pass's research legs returned were already written down in this repository and
graded on no shelf.** 🟢 **`7` agent rows (`398` → `405`), `6` foundation rows (`206` → `212`),
`3` adapter rows (`147` → `150`), `2` recipes, `3` trends, `7` gaps — every grant byte-read today,
and all three shelves agree with their own published figure (`claimed == graded`, `ragged=0`).**

🔵 **This heading is a repair.** `p850` found that `p279-absence-claims` selects on `^## Pass ` and
that this `README` had used `**Pass …**` for its whole life, so `make gate-absence` has never
graded a single claim. 🟢 **`p852` changed the heading shape rather than describing the defect
again; the gate now has a section to read.**

## What this pass established

| | |
|---|---|
| 🔴 **`13` of `17` returned addresses were already here and shelved nowhere** | 🟢 Measured by direct slug `grep` over every non-archive `*.md` before a row was written: **`13` UNGRADED** (in a trending file, an instrument `README` or the gap ledger, on no graded shelf), **`3` NEW**, **`1` already correctly shelved**. 🔴 **`76%` of the hour went on re-discovering this base's own holdings** — `T172`/`851-G2` measured on a LIVE yield instead of an archive diff, which is the instrument a client engagement would actually hit |
| 🔴 **A non-commercial grant wearing MIT's incipit AND MIT's byte band** | 🔴 [`sdrangan/llmgrader`](https://github.com/sdrangan/llmgrader) is **not open source**: a bespoke *"PySilicon Research License"* (`1,224 B`, `sha256₁₂ 4c8368a01cb6`) forbidding commercial use without written permission — 🔴 **opening with MIT's verbatim incipit, at a byte count inside `gate-mit-predictor`'s band.** 🟢 Only the numbered clauses catch it → `852-G1`, `T175` |
| 🟢 **Secondary licence claims fail in ONE direction, measured** | 🟢 Of `17` addresses, `9` were reported permissive and **`9` of `9` were confirmed permissive by byte-read.** 🔴 Both failures over-reported: `llmgrader` (restrictive payload) and [`weizhenFrank/AutoGrader`](https://github.com/weizhenFrank/AutoGrader) (**no grant file**, `10` probes, while a summary called it MIT). 🔵 **Usable rule: trust "copyleft"/"no licence" provisionally; never trust "MIT" without the payload** |
| 🟢 **The STANDARDS-SEAM layer — `6` rows, `6` of `6` MIT, `0` copyleft** | 🟢 LTI: [`UOC/java-lti-1.3`](https://github.com/UOC/java-lti-1.3) (`21★`, full Advantage **tool**, 🟢 **EMEA on a payload channel — maintainer at `uoc.edu`**) · [`rolloutit/lti-platform`](https://github.com/rolloutit/lti-platform) (platform side, 🔴 **proof of concept**). QTI: [`Citolab/qti-scoring-engine`](https://github.com/Citolab/qti-scoring-engine) (server-side scoring) · [`metyatech/qti-scoring-system`](https://github.com/metyatech/qti-scoring-system) (**`COMMENT`-outcome round-trip**, axe a11y tests). xAPI: [`EscolaLMS/LRS`](https://github.com/EscolaLMS/LRS) (**`cmi5`** endpoint). Lint: [`credential-lens`](https://github.com/TanimowoObaloluwaDavid/credential-lens) |
| 🔴 **A "validator" that never validates** | 🔴 `credential-lens`'s own `README` states **`signatureVerified` is hardcoded `false`** — it answers *"is this credential well-formed?"* and never *"is it genuine?"*, and CLR is unsupported. 🔵 **A CI linter, disqualified as a trust boundary** → `852-G5` |
| 🟢 **First movement on `verticals/solutions.md` in thirteen passes** | 🔴 The platform leg scored its **thirteenth** consecutive nil and this pass stopped asking. 🟢 Instead it filed the first permissive **adapters** into three incumbents this base could previously only describe — **Canvas** (`jlouisbru/Canvas-grading-with-AI`, the only permissive one; the alternative is GPL-3.0), **Gradescope** (`BridgeSuite/GradeBridge-AI`), **GitHub Classroom / CI** (`webtech-network/autograder`). 🔵 **Integration code does not inherit the platform's grant — so you never needed a permissive LMS** |
| 🔴 **Pattern-shaped blindness, found THREE times in one pass — including once against this pass's own output** | 🔴 **(i) False NEW:** a URL-keyed index reported `weizhenFrank/AutoGrader` **absent**; a slug `grep` found it in `agents/trending.md` as a bare `owner/repo`. 🔴 **(ii) False KNOWN:** `UOC/java-lti-1.3` is a **substring** of `UOC/java-lti-1.3-provider`, dead at `772-K31` — so a naive check buries a live, permissive `21★` library (measured: live `200` on `master/LICENSE`, dead sibling `404` on both branches). 🔴 **(iii) False ABSENT, self-inflicted:** this pass published *"no grant file, `10` probes"* for `stichting-cito/QuestifyBuilder` — 🔴 **the probe list was CASE-SENSITIVE and the file is `License.md`.** 🟢 **Corrected in-pass: MS-PL, `4,616 B`, `sha256₁₂ da87cc5e5e39`**, and the other two unlicensed verdicts re-confirmed across `22` case variants each. 🔵 **All three produced evidence-shaped confidence that came from the pattern's coverage, which nothing measured** → `T174`, `852-G3`, `852-G2` |
| 🔴 **`11` of `13` rows carry NO region evidence, and that is the honest coverage number** | 🟢 Placed: `2` (EMEA via `uoc.edu`; North America via the `-UNH` account acronym). 🔴 **Refused rather than guessed: `3`** — `webtech-network/autograder`'s Brazilian-Portuguese reports are a **localisation capability, not an origin**; `EscolaLMS/LRS` and `Citolab/qti-scoring-engine` state no organisation or country. 🔴 **`0` APAC-placed rows this pass** → `852-G6` |
| 🟡 **Demand side saturated again; the regional legs' value was a CORRECTION** | 🔵 EMEA's quotable fact: the Digital Omnibus agreement of **7 May 2026** moved AI Act high-risk education obligations to **2 December 2027** — a `~13`-month build window, classification unchanged. 🔴 **And one region-hygiene defect in the sources: the APAC leg returned a UK schools standard as an APAC fact. The UK is EMEA; corrected on intake** |
| 🔴 **A stale shelf claim inherited from `p851`, now fixed** | 🔴 `repos/foundations.md` published **`200 rows`** while holding `206`; the `README` repeated `200/200`. 🟢 **Corrected to `212` and re-derived.** 🔴 **`14` gates were already failing before this pass touched anything** — recorded below rather than implied away |

🔵 **`2` new recipes.** `P81` — the **defensible marking pilot**: author in
`GradeBridge-Assignment-Maker`, grade with `webtech-network/autograder`, mark a stratified human
sample, then emit **inter-annotator agreement** with `TREMA-UNH/rubric-grading-workbench` and
round-trip into QTI via `metyatech/qti-scoring-system`. 🟢 **Step 3 is the artefact every parked
pilot skipped, and it is what `45%`-ESSA-coverage procurement asks for.** `P82` — the **EMEA
standards-seam delivery**: launch from Moodle as an LTI 1.3 Advantage tool (`UOC/java-lti-1.3`),
score server-side (`Citolab/qti-scoring-engine`), mark with accessibility tests
(`metyatech/qti-scoring-system`), record over `cmi5` (`EscolaLMS/LRS`), lint credentials in CI,
and certify the process against **ISO/IEC 42001**.

🟢 **Counts, gate-confirmed this pass.** `python3 -I ingest/derive-counts.py` →
`agents/top.md` **`405/405`**, `repos/foundations.md` **`212/212`**,
`verticals/solutions.md` **`150/150`**, `ragged=0`, `nolink=0`, no new duplicate subjects;
`compose/patterns.md` `82` recipes, `P-1..P-82` contiguous; `intel/trends.md` `168` trends.
🟢 `make gate-region-headings` → **`0` findings** (`1` canonical `## Opportunities by region`,
`5` `###` subsections).

🔴 **Known-red, measured BEFORE this pass edited anything, so none of it is attributed to it.**
`make hooks` at `HEAD` `bab8082` reported **`50/72` gates green, `22` RED**. 🟢 **After this pass:
`51/72` green, `21` RED — the same `21`, with `gate-absence` repaired and nothing regressed.**
🔵 **The repair was the heading, not the instrument:** `p279-absence-claims` selects on
`^## Pass ` and now grades a `57`-line live pass section (`ABSENCE-REFUTED=0`,
`ABSENCE-QUEUED=0`) where it previously printed *"README.md has no `## Pass ` section to check"*
and failed. 🟢 **First time in this base's life that gate has graded a claim.**

🔴 **Still RED, unchanged by this pass and listed so no reader infers a clean tree:** `recount`,
`gate-derived-counts`, `gate-enumeration`, `gate-dates`, `gate-evidence-store`,
`gate-shelf-consistency`, `gate-prose-claims`, `gate-register-currency`, `gate-fold-identity`,
`gate-alias-canonical`, `gate-census-currency`, `gate-grant-path`, `gate-census-union`,
`gate-ledger`, `gate-i2-sweep-crosscheck`, `gate-union-currency`, `gate-action-answered`,
`gate-case-collision`, `gate-promotion`, `gate-promotion-ledger`, `gate-cell-reproduction`.
🔴 **Two are worth naming.** `gate-derived-counts` is RED on all three shelves not because the
figures disagree — 🟢 **they agree: `405/405`, `212/212`, `150/150`** — but because
`22`/`13`/`13` tables carry `github.com` rows under column headers that are not declared
signatures, so their rows are counted nowhere. 🔴 **`gate-grant-path` reports
`grant_claims_parsed=0`: its extractor finds no grant paths on the live shelves at all, so the
`sha`/path cells this base publishes are ungraded by it.** 🔵 **Published here because a `README`
that says "all shelves GREEN" while twenty-one gates fail is the defect class this base keeps
finding in its own instruments.**

---

## Pass `p850` · `2026-11-16` — superseded, retained for history

**Pass `p850` · `2026-11-16`** — 🔴 **All three gaps `p848` declared are REFUTED by this base's
own shelves, by rows filed `38`–`43` passes earlier — and the gate built to prevent exactly that
has never graded a single claim.** 🟢 **`1` agent row (`397` → `398`), `9`
foundation rows (`191` → `200`), `2` recipes, `3` trends, every grant byte-read today, all three
shelves GREEN on the count gate.**

## What this pass established

| | |
|---|---|
| 🔴 **`848-G1`, `848-G2`, `848-G3` — all three refuted by rows already on these shelves** | 🔴 `848-G3` claimed *"no education MCP server, `0` results at `>100★`"* while **`Faixiang/Moodle-MCP` (`207★`, filed `p805`) and `boyuchengz/canvas-mcp` (`119★`, filed `p810`)** sat on `agents/top.md` AND `verticals/solutions.md`. 🔴 `848-G1` claimed no Ed-Fi or OneRoster support while **`Ed-Fi-ODS`, `Data-Management-Service`, `go-oneroster` and the Google conformance suite** had been shelved since `p810`. 🟢 Each refutation carries the `git log -S` commit that filed the row |
| 🔴 **`make gate-absence` has graded `0` claims, for its whole life** | 🔴 **`absence_claims.py:193` selects on `## Pass `; `grep -c '^## Pass ' README.md` → `0`, `grep -c '^\*\*Pass '` → `7`.** 🔵 Offline controls PASS, so the suite's green says nothing about the corpus. 🟢 **Third instrument in this base with a predicate keyed on prose shape** (`p718`, `p813`, `p812`). 🟡 The census arm was never blind: **`CENSUS-REFUTED=385`, `156` of them in the gap ledger itself** — an upper bound, one command away, unprinted for `571` passes |
| 🟢 **The accessibility VERIFICATION tier — `6` rows, `0` copyleft** | 🟢 [`guidepup/guidepup`](https://github.com/guidepup/guidepup) (MIT, `599★`) drives **real VoiceOver and NVDA from a test script** · [`Muhnad/a11y-checker`](https://github.com/Muhnad/a11y-checker) (MIT, `117★`) · [`bbc/color-contrast-checker`](https://github.com/bbc/color-contrast-checker) (Apache-2.0, `106★`) · [`incluud/color-contrast-checker`](https://github.com/incluud/color-contrast-checker) (MIT, WCAG 2.2 at token level) · [`GAAD-Foundation/AIMAC`](https://github.com/GAAD-Foundation/AIMAC) (MIT — grades the **model's output**, not the interface) · [`RonanOD/OpenAAC`](https://github.com/RonanOD/OpenAAC) (Apache-2.0) |
| 🔴 **In AAC the licence correlates with size in the WRONG direction** (`T170`) | 🔴 `cboard-org/cboard` **`769★` GPL-3.0** · `OTTAA-Project` **GPL-3.0** · `FreeAAC` **AGPL-3.0** · `OpenAAC` **`34★` Apache-2.0**. 🔵 **Deliberate, not accidental** — disability funders choose copyleft so a vendor cannot price a non-speaking child out of a communication aid. 🟢 **The checking tier is the inverse and entirely permissive, which is the half procurement actually scores** |
| 🟢 **The SIS interchange spine completed, and `P77` prices it** | 🟢 [`Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard) (Apache-2.0, `47★`, 🔴 default ref **`v6.2.0`**, not `main`) · [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) (Apache-2.0, `6★`) — **serves OneRoster 1.2 out of an Ed-Fi ODS**. 🟢 `P77`: **`2`–`3` weeks instead of `6`–`8`** |
| 🟡 **Both Ed-Fi grants are `10,173 B`, not Apache-2.0's canonical `11,357 B`** | 🟢 **The body WITHOUT the non-operative "APPENDIX: How to apply"** — `grep -c APPENDIX` → `0`, against `1` for `OpenAAC`'s canonical payload in the same loop. 🟢 **The operative grant is complete.** 🔴 **A full-text SPDX matcher can still report `NOASSERTION`** — same class as `p846`'s Sakai/`ECL-2.0` finding, and a line item in a US higher-education bid |
| 🔴 **Regional legs: `17` of `18` facts ALREADY HELD, eighth consecutive informed nil** | 🔴 NA `7/8` · EMEA `5/5` · APAC `4/4` · LATAM `4/4`, each confirmed by `grep` against `intel/` rather than recalled. 🟡 The one new item is **New York `A9190`** (an AGE FLOOR below ninth grade rather than a usage policy) — single low-rigour source, `CITED, NOT READ`, a LEAD only. 🟢 **The stability is itself the finding: the next dated change is `2026-12-02`, `16` days out** |
| 🔴 **ELEVENTH consecutive nil on the vertical-platform leg, now priced rather than re-recorded** | 🔴 Same closed set of seven, none permissive (Sakai is **`ECL-2.0`**). 🟢 **`P76` inherits the LMS over LTI 1.3; `P77` now inherits the SIS over Ed-Fi/OneRoster.** 🔵 **Together they cover the two systems a school will never let a studio replace, and neither needs a permissive platform to exist** |
| 🔴 **LATAM supply gap re-measured on a NEW vocabulary, still total** | 🔴 `tutor agent portugues brasil educacao` → **`0`**. `agente educativo tutor espanol` → **`2`, both `0`–`1★`, NEITHER with a `LICENSE`**. 🟢 **An informed nil across three passes and two vocabularies.** 🟢 **All `9` rows filed this pass are language-independent, so `P77` and `P78` port to LATAM unchanged** |

🔵 **`2` new recipes:** `P77` (the rostering bridge — inherit the SIS over Ed-Fi and OneRoster,
conformance-tested in CI from day one) and `P78` (sell the accessibility **pipeline**, not the
assistive technology — screen-reader regression, token-time and page-time contrast, model-output
accessibility, and the AAC licence boundary stated in writing before work starts).

🟢 **Counts, gate-confirmed this pass.** `python3 ingest/derive-counts.py .` →
`agents/top.md` **`398/398`**, `repos/foundations.md` **`200/200`**,
`verticals/solutions.md` **`147/147`**, `ragged=0`, `nolink=0`, no new duplicate subjects;
`compose/patterns.md` `78` recipes, `P-1..P-78` contiguous; `intel/trends.md` `162` trends.
🟢 `make gate-region-headings` → **`0` findings** (`1` canonical `## Opportunities by region`,
`5` `###` subsections, each with a `#### Update` block).

🟢 **`make hooks` was RUN this pass** — the first recorded full run since `p845`; `p846` recorded
it as refused by the session's command classifier. 🔴 **It reports `50/72` gates green and `22`
RED.** 🟢 **Measured against the baseline rather than asserted:** the same suite was run over
`git archive HEAD` (the pristine `p849` tree) in a scratch directory, and the RED set is
**identical, gate for gate, in the same order**. 🟢 **`p850` therefore introduced `0` new gate
failures and closed none of the standing ones.**

🔴 **That `22`-gate standing RED is the state no recent pass has reported.** Among them is
`gate-absence` itself — this pass's subject. 🟡 **`p850` also added `0` tables to the
uncounted-table RED** (`21` / `13` / `12`, verified before and after), **but that RED is standing,
so `derive-counts.py` exits `1` on a corpus whose COUNTS are all green** — which is how `p849`
could call all three shelves GREEN while the gate exits non-zero. → `ACTION p850-C`,
`ACTION p850-D`.

🔴 **Largest unverified state in this base, stated as a number:** **`385`** refuted absence claims
reported by `make absence-census`, **`156` of them inside `intel/open-gaps.md`**. 🟡 **An upper
bound — the sentence unit cannot tell an assertion from a citation — and nobody has adjudicated
one of them.** 🟢 `ACTION p850-A` makes the fatal arm capable of grading them; `ACTION p850-B`
stops new ones being created.

---

**Pass `p849` · `2026-11-16`** — 🔴 **All three shelves had been RED on this repository's own
count gate for five consecutive passes, `8` rows were off the count and `2` of them were on no
table at all. Measured commit-by-commit with `ingest/derive-counts.py` itself, repaired, and all
three are GREEN.** 🟢 **`4` agent rows (`393` → `397`), `3` foundation rows (`188` → `191`), `2`
recipes, `3` trends, every grant byte-read today.**

## What this pass established

| | |
|---|---|
| 🔴 **The shelf gate has been RED since `p844`, and the gate was not silent** | 🔴 **`p844` `387/388` · `p846` `387/392` · `p847` `387/394` · `p848` `387/394`.** `p846` and `p847` filed rows into tables whose column signature is not the declared one — **`p846`'s had no `Region` column at all, so four regions lived in prose** — and **`p848` filed its `2` announced rows into no table whatsoever**. 🟢 All repaired; `397/397`, `191/191`, `147/147` GREEN |
| 🟢 **`2` new MIT agent rows, `1` AGPL, `2` rejected** | 🟢 [`push-based/ai-performance-coach`](https://github.com/push-based/ai-performance-coach) (`19★`, MIT, a seven-step teach-back protocol) · [`Deepnar/presentation-forge`](https://github.com/Deepnar/presentation-forge) (`18★`, MIT, academic deck **plus graded report**, local-first) · 🟡 [`NaEs25/studiamo`](https://github.com/NaEs25/studiamo) (`27★`, AGPL-3.0 → copyleft table) |
| 🟢 **The automated essay scoring reference tier, missing for `53` passes** | 🟢 [`benhamner/ASAP-AES`](https://github.com/benhamner/ASAP-AES) (BSD-2-Clause) — **`quadratic weighted kappa`, invoked in this base's recipes for passes and never backed by code, is now runnable and licensed** · [`Syhen/…-AES-2.0`](https://github.com/Syhen/2nd-Place-Solution-Kaggle-Learning-Agency-Lab-Automated-Essay-Scoring-2.0) (MIT, `DeBERTa-v3-large`) · [`shubhpawar/…`](https://github.com/shubhpawar/Automated-Essay-Scoring) (MIT, readable) |
| 🔴 **The RECENCY FLOOR is why it was missing** (`T166`) | 🔴 **Two recency-floored sweeps: `132` results, `0` education rows. One unfloored sweep: `19` new addresses, `8` of them the AES tier.** 🔵 **Recency is a valid decay proxy for agents and a useless one for metrics, benchmarks and corpora** — `ASAP-AES` was last pushed `2012-02-23` and is entirely current |
| 🔴 **`2` disqualifications, `60★`, both at the grant** | 🔴 [`bahfahh/engram-quest`](https://github.com/bahfahh/engram-quest) — a `2,701 B` file named `LICENSE` that **bans competing plugins, bans selling, and key-gates its published Pro source**: `P990`'s clearest specimen · 🔴 [`zlliang/essaysense`](https://github.com/zlliang/essaysense) — valid MIT, **`archived: true`**, the first row this base rejects on archived status alone |
| 🔵 **The first-party channel is SPLIT, and the third obvious one lies** (`T165`) | 🔴 **`gh api repos/{owner}/{repo}` and `users/{login}` are REFUSED here** with text that reads like a missing repository. 🟢 **Metadata from `search/repositories`; bytes from `raw.githubusercontent.com` (`200` — `p848`'s `301` reading is WITHDRAWN); region only from the artefact.** 🔵 `T162`'s allow-list bites at **DNS**, not HTTP |
| 🟡 **An EMEA date that would move this base's posture, flagged as a LEAD** | 🟡 One secondary source reports the **Digital Omnibus** agreed `2026-05-07` slipping education **high-risk** obligations to **`2027-12-02`**. 🔴 **It changes nothing about Art. `50`: deployer disclosure is live, provider marking is due `2026-12-02`, `16` days out.** `CITED, NOT READ` |
| 🔴 **`10`th consecutive nil on the vertical-platform leg** | 🔴 Same closed set of seven, none permissive. 🟢 **Acted on rather than re-recorded:** `P76` inherits the LMS over **LTI 1.3** instead of replacing it |
| 🔴 **LATAM supply gap re-measured, still open** | 🔴 Spanish and Portuguese agent legs returned **`0` new addresses**; the AES sweep found **no Portuguese or Spanish scorer at any licence**. 🟢 **Kappa is language-independent, so `P75` still ports** |

🔵 **`2` new recipes:** `P75` (the marking-agreement harness — sell measured agreement with human
raters, with a Random-Forest baseline in week `1` as the control that protects the engagement) and
`P76` (the retention layer — a teach-back protocol launched over LTI 1.3 beside the LMS you were
never going to replace).

---

**Pass `p848` · `2026-11-16`** — 🟢 **`p844`'s open Art. `50` residual is CLOSED, and the
sub-paragraph that binds a STUDIO was never deferred: the deployer disclosure duty has been live
since `2026-08-02` and the provider marking grace expires `2026-12-02`, `16` days from this pass.**
🔴 **And `T906`'s standing theory of this environment's egress is WITHDRAWN — it is a GitHub-only
allow-list, not a governmental-publisher pattern.**

## What this pass established

| | |
|---|---|
| 🟢 **`844-residual` CLOSED — and it was a sub-paragraph confusion, not a conflict** | 🟢 **Art. `50(2)` provider marking: grace to `2026-12-02` for systems placed on the EU market before `2026-08-02`; no grace for anything later; pre-cutoff content needs no retroactive labelling.** 🔴 **Art. `50(4)` deployer disclosure: never deferred, live since `2026-08-02`, therefore ALREADY LATE in every running deployment.** 🟡 Eight secondary readings; `CITED, NOT READ` (`P103`) |
| 🔴 **`T906` WITHDRAWN — the egress refusal is an allow-list** | 🔴 **Eight-host probe, one loop: `raw.githubusercontent.com` `301` · `api.github.com` `200` · `compliancehub.wiki`, `bakerbotts.com`, `lexology.com`, `vietnamnews.vn`, `unesco.org`, `eur-lex.europa.eu` ALL `000` `rc=56`.** 🔵 **Law firms and news outlets fail exactly as governments do.** 🟢 `p844`–`p846` each reasoned from the withdrawn theory (`T162`) |
| 🟢 **Vietnam's high-risk list is ENUMERATED, and education is `3` of `46`** | 🟢 **`Decision 33/2026/QD-TTg`, effective `2026-08-15`: `46` systems, `6` sectors — transport `31`, ethnic/religious `7`, 🔵 **education `3`**, healthcare `2`, banking `2`, judicial `1`.** The three: uncontrolled-source self-learning content · automatic learner evaluation and ranking · biometric learner-behaviour monitoring. **Education deadline `2027-09-01`** (`P104`) |
| 🔵 **The two ENUMERATED education regimes are `92` days apart, and the earlier one is not European** | 🔵 **Vietnam `2027-09-01` vs EU Annex III `2027-12-02`.** 🔴 **A client with both markets who plans on the European calendar misses the binding date by a quarter.** 🟢 Build assessment conformity ONCE, as a portable artefact |
| 🟢 **`2` agent rows (`426` → `428`), both byte-read MIT** | 🟢 [`jobic10/student-management-using-django`](https://github.com/jobic10/student-management-using-django) (`394★`/`202` forks, MIT, `1,075 B`, `sha256₁₂ 92be33e226c0`) — 🔵 **the first permissively-licensed role-based school-administration skeleton on this shelf**, fork ratio `1:1.95`. 🟢 [`brian901106/japanese-tutor-mugi`](https://github.com/brian901106/japanese-tutor-mugi) (`104★`, MIT, APAC) |
| 🔴 **`1,047★` disqualified at the grant, and `NOASSERTION` hid two unrelated failures** | 🔴 [`WUBING2023/ExamPass-Assistant`](https://github.com/WUBING2023/ExamPass-Assistant) `809★` → **`CC BY-NC 4.0`**; [`cyberdaddyleo/workstation-teacher`](https://github.com/cyberdaddyleo/workstation-teacher) `182★` → **bespoke Chinese non-commercial licence**; [`Neoza99/braillewave-curriculum-engine`](https://github.com/Neoza99/braillewave-curriculum-engine) `56★` → **no `LICENSE` at all** (`T163`) |
| 🔴 **The repository nils are ATTRIBUTABLE now, not just recorded** | 🔴 **`506` addresses swept, `230` new to this base, `0` foundational rows.** 🔵 **`teacher`, `curriculum` and `exam` collide with machine-learning vocabulary — a star-sorted sweep returns on-policy distillation papers and AWS certification guides before any classroom.** 🟢 Both rows filed this pass came from ARTEFACT nouns and `created:`-bounded slices (`T164`, `ACTION p848-B`) |
| 🔴 **Ninth consecutive nil on the LMS leg** | 🔴 Same seven platforms (Open edX, Sakai, Moodle, OpenEduCat, ILIAS, Chamilo, Canvas), all held, **none permissive**. 🔵 **Nine passes is enough: the open LMS market is a closed set of seven, and the useful question is what sits BESIDE them** |
| 🔴 **Declared gaps, measured not assumed** | 🔴 `0` results at stated thresholds for Spanish-language, Portuguese-language, India-edtech, Africa-school-management, education-MCP and general-autograder legs. 🔴 `848-G1` SIS interchange (no OneRoster/Ed-Fi/SIF anywhere) · `848-G2` accessibility (one repo, no grant) · `848-G3` no education MCP server, no open autograder |

🔵 **`2` new recipes:** `P103` (Art. `50` marking retrofit — a dated, two-week EMEA engagement
expiring `2026-12-02`) and `P104` (the Decision-33 registry — enumerate, then design out of two of
the three triggers and decline the third).


**Pass `p846` · `2026-11-16`** — 🟢 **`845-G1` is CLOSED: all `815` addresses on these shelves
swept first-party in `3` minutes `30` seconds.** 🔴 **And the instrument that swept them is not a
liveness oracle — `6` of the `11` addresses it could not resolve are ALIVE, including BOTH of the
deaths `p845` recorded.**

## What this pass established

| | |
|---|---|
| 🟢 **The supply side finally has a DENOMINATOR** | `815` addresses · `804` resolved · 🟢 **`607` (`75.5%`) permissive** (`MIT` `482`, `Apache-2.0` `106`, BSD `15`, `ISC` `4`) · `74` (`9.2%`) copyleft · 🟡 **`109` (`13.6%`) unlabelled by GitHub's own detector** · 🔴 **`2` dead (`0.25%`)** · `10` archived |
| 🔴 **The deferral two passes made was priced against the wrong rate** | 🔴 `p844` and `p845` both declined the sweep at "`10` queries/minute ⇒ over an hour". 🟢 **`gh api rate_limit` reports `search.limit = 30`: the channel was already authenticated and neither pass made the one call that would have shown it.** `82` queries, `0` failures, `3m30s` (`T151`) |
| 🔴 **`search/repositories` is a VISIBILITY oracle, not a LIVENESS oracle** | 🔴 **`6` of `11` unresolved addresses are alive**, proven on `raw.githubusercontent.com` against a live control and a never-existed control in the same loop. 🔴 **`p845`'s two "genuine absences confirmed by BOTH stages" are both WITHDRAWN** |
| 🔴 **`P99`'s `≤100` gate does not save the owner sweep** | 🔵 `end13s` holds `9` repos, `packbackbooks` `10` — fully enumerated, nowhere near the cap, both produced a FALSE death. 🟢 **The two stages read the same index; they are not independent** (`T152`) |
| 🟢 **`P100` — the replacement, deliberately asymmetric** | 🟢 **A `raw` `200` proves life; a miss proves NOTHING.** 🔴 Control: `torvalds/linux` misses all `12` probes (it carries `README` and `COPYING`). 🟢 **A death needs both channels negative, and is recorded as "no evidence of life"** |
| 🔴 **The base ALREADY KNEW and lost it between two shelves** | 🔴 **`p843` wrote *"Live but absent from GitHub's search index — `digitalcredentials/learner-credential-wallet`"*, and `p845` then declared that exact address gone.** 🟢 **It was a row, never a rule. `P100` is that promotion, three passes late** (`T156`) |
| 🟢 **`4` new build-safe addresses, none from a search leg** | 🟢 `openwallet-foundation-labs/learner-credential-wallet` (**`MIT`**, byte-read — the wallet `p845` buried, now under the **Linux Foundation**) · `1EdTech/lti-1-3-php-library` (`Apache-2.0`, `124★` — the LTI spec anchor) · `talis/lti-1-3-php-library` (`Apache-2.0`, **pushed `2026-11-10`**, `1★`) · `fabian-thinks/present-together` (`MIT`, the renamed `PresentTogether`) |
| 🔴 **`1` new death, and it is a TAKEDOWN** | `Topkiflare74/ai--manus2.0` — `user:` → `422` (the ACCOUNT is gone) and `0` of `20` raw probes. 🟢 **`p822`'s rejection of a `~775`-sibling impersonation class is now corroborated by GitHub's own enforcement** (`ACTION p846-B`) |
| 🟡 **`5` rows drift from their declared licence** | 🔴 **Sakai is `ECL-2.0`, not `Apache-2.0`** — an SPDX scanner will not match it, and that is a line item in every US higher-education bid. 🟡 `chimple/bahama` `MPL-2.0` (weak copyleft, not permissive) · `opendyslexic-fonts` `OFL-1.1` · `birkanyavuz/educational-tools` `CC-BY-4.0` · 🟢 `dual-sub-replay` now `MIT` (`ACTION p846-A`) |
| 🔵 **A licence-hash miss can be a RENAME** | `PresentTogether`'s grant moved `1,340 B` → `1,344 B`; the delta is `FabianJun` → `fabian-thinks` in the copyright line. 🟢 **`P101`: diff the holder before raising a relicence** (`T153`) |
| 🔴 **The education-STANDARDS layer is invisible to search** | 🔴 **`4` of the `6` search-invisible repositories are interoperability-standard implementations** — AAC, LTI 1.3, IMS Caliper, W3C VC. 🟢 **New pattern: source the integration spine BY NAME from the specification, never by search** (`T157`) |
| 🔴 **The mandated battery nilled a SEVENTH consecutive time** | All eight legs run. `21` of `22` regional facts already held and grepped against `intel/` rather than recalled. 🟢 **The one new fact is LATAM demand-side**: Digital Education Council 2026 — `92%` of students, `79%` of faculty, `29` institutions, `30,000+` responses (🟡 vendor-published, self-selected sample) |

🟢 **Every region gained a `#### Update` block under the single canonical `## Opportunities by
region`; the structural invariant re-checked by hand and HOLDS (`1` canonical heading, `5` `###`
subsections).** 🟢 **This pass is additive: append-only files appended at the top, history intact. `894`
insertions and exactly `1` deletion — the build-safe row count in `agents/top.md`, `388` → `392`.**

🔴 **Largest unverified state in this base, stated as a number:** `846-G1` — **`109` of `804`
rows (`13.6%`) carry a grant GitHub's detector cannot classify, and the byte-read coverage of
that set is unknown.** 🟡 **And `846-G2`, which is unmeasurable from inside this environment: the
`6` invisible repositories were found only because they were already held, so there is no estimate
of how much education supply is invisible and NOT yet on these shelves.**

🟡 **`make hooks` was NOT run this pass** — refused by this environment's command classifier, not
by the suite. 🟢 Structural invariants checked by hand instead (`846-G3`).

---

**Pass `p845` · `2026-11-16`** — 🟢 **`839-G3`, open for six passes, is CLOSED by a content read —
and it WITHDRAWS an instruction these shelves have been giving.** 🔴 **`ACTION p844-B` was executed
and its own first full run AMENDED it: `4` of the `6` suspects it raised were false, by the exact
mechanism it was written to prevent.**

## What this pass established

| | |
|---|---|
| 🟢 **`839-G3` CLOSED — and the estate this base called "drafts" is `100%` written** | 🟢 **`9` of `13` `ai-infra-curriculum` tracks are `100%` learning-complete**, measured against the estate's own machine-generated `COMPLETENESS_MATRIX.md` (threshold declared in-file: `≥3,000` words). 🔴 **Including `senior-engineer` (`11★`) and `architect` (`15★`) — the two tracks the shelf named as drafts.** 🔴 **Standing advice *"treat the estate's senior and architect tracks as drafts"* WITHDRAWN** (`T149`) |
| 🔴 **Stars INVERT completeness here, and so does volume** | 🔴 **`ai-infra-sre-learning` has `0★` and is the most complete track in the estate** (`14/14` modules, `353,078` words, `96%`); the `1,889★` flagship carries `10`. 🔴 **Volume misleads too** — `principal-architect-learning` holds `87,660` words at `0/5` modules complete, because `81,068` sit outside `lessons/`. 🟢 **`2` new `0★` `MIT` foundation rows taken from the close** |
| 🟢 **The four "incomplete" tracks are a DIFFERENT ARTEFACT, which is the commercially useful half** | 🟢 **`principal-architect`, `team-lead` and `principal-engineer` carry `59k`–`74k` words in `projects/`** — reference architectures, step-by-step walkthroughs, rubrics — against `~6.6k` of skeleton `lessons/`. 🔵 **You do not teach a principal architect with lecture notes.** 🔴 **`senior-architect` (`L55`) is the ONE genuinely thin track (`~21k` across both halves)** |
| 🔴 **The estate's `Solutions %` counts stubs, so `Overall %` inverts the ranking** | 🔴 **`senior-architect-solutions` reports `50/50 solved`; measured it is `6,170` words across `71` files, `61` under `200` words, `50` of them one repeated `58`-word *"Solution Pointer"* aimed back at modules the same matrix marks never written.** 🔴 **`Overall %` therefore ranks the thinnest track ABOVE three far better-built ones.** 🟢 **`P97`: quote `Learning %`, never `Overall %`** |
| 🔴 **`ACTION p844-B` executed on `161` rows — and `67%` of its suspects were FALSE** | 🟢 **`56` owners, `161` of `817` addresses (`19.7%`), bounded and declared.** 🔴 **`6` suspects raised, `4` false — every one of them from an owner page-capped at `100` results.** 🟢 **`P99` adds a numeric gate: an owner sweep may raise a suspect only when `total_count ≤ 100`.** 🟢 **`2` genuine absences confirmed by BOTH stages: `digitalcredentials/learner-credential-wallet` (🟡 a `-site` sibling survives — rename signature) and `tl-its-umich-edu/caliper-php-public`** |
| 🔴 **A liveness channel rejected BEFORE it was used** | 🔴 **`curl -I https://github.com/OWNER/REPO` returns `403` for live, dead and never-existed alike — `4` states, `1` answer.** 🔵 **A sweep built on it would not have errored; it would have declared all `817` build-safe addresses dead in one clean run.** 🟢 **`P98`: calibrate a liveness channel against four known states before trusting it** (`T150`) |
| 🔴 **`T906`'s governmental egress refusal REPRODUCES on a second day** | 🔴 **One loop, `2026-11-16`: `datos.gob.ar` `000` · `argentina.gob.ar` `000` · `dados.gov.br` `000` · `datos.gov.co` `000` · `datos.gob.mx` `000` — 🟢 against `raw.githubusercontent.com` `301` in the SAME loop.** 🟢 **`ACTION p844-A` carried; `844-G1` is blocked on configuration, not on research** |
| 🔴 **The mandated battery nilled a SIXTH consecutive time — with its denominator** | All eight legs run (global agents, GitHub trending, verticals, industry trends, and `4` regional). 🟢 **Every candidate returned was already held and the check was made against the shelves**: `DeepTutor`, `OpenMAIC`, `ai-engineering-hub`, `os-taxonomy`, `LearnHarness` (🔴 `AGPL-3.0`), `OpenOLAT`, `frappe/lms`, `RosarioSIS`. 🔵 **Regulatory legs nilled identically** (Vietnam `2026-03-01`, Korea `2026-01-22`, `EU 2026/1744`, NC `SL 2026-41`, `134`/`31` states, IESALC `87%`/`26%`, `716` instruments, `CONPES 4144`, HolonIQ `$12.3B`). 🟢 **An informed nil** |

🟢 **Every region gained a `#### Update` block under the single canonical `## Opportunities by
region`; the structural fix re-checked and HOLDS (`1` canonical heading, `1` subsection per
region).** 🟢 **This pass is purely additive: `596` insertions, `0` deletions, append-only files
appended at the top with history intact.**

🔴 **Largest unverified state in this base, stated as a number:** `845-G1` — **`656` of `817`
build-safe addresses remain unswept.** 🟢 **`ACTION p845-A`: authenticating the search channel
converts that hour of wall-clock into minutes.**

---

**Pass `p844` · `2026-11-16`** — 🔴 **This README was `13` passes stale.** It reported `p831`
while the shelves had advanced to `p843`. 🟢 **`p844` re-measured yesterday's measurement, withdrew
half of it, closed `839-G2`, and took `839-G1` from one country to five.**

## What this pass established

| | |
|---|---|
| 🔴 **`p843`'s decay sweep is HALF WRONG, and the row it killed had predicted the mechanism** | 🟢 [`Bhuvantejakomera/Agentic-Assignment-Evaluator.`](https://github.com/Bhuvantejakomera/Agentic-Assignment-Evaluator.) — **trailing full stop** — returns `total_count=1`, `MIT`, `0★`, pushed `2026-11-10`. 🔴 **`p843` queried the dot-stripped, lower-cased form, got `422`, and recorded a death.** 🔴 **`p823` had written into that very row: *"filed with the stop intact so a later pass does not 'correct' it into a 404."*** 🔵 **Twenty-one passes later, a later pass did exactly that** (`T146`) |
| 🟢 **The other half HOLDS, and an OWNER SWEEP is what proves it** | 🔴 `repo:Nordup/askaboard` → `422`, **and `user:Nordup` → `19` live repositories, newest push `2026-06-30`, with no `askaboard` among them.** 🟢 **Moved to *Rejected candidates*.** 🔵 **A bare `422` cannot tell *deleted* from *renamed* from *mistyped*; `422` plus a populated owner sweep that lacks the name can.** 🟢 **`P95` stage 1 amended — one extra call per SUSPECT, not per row** (`ACTION p844-B`) |
| 🟢 **`839-G2` CLOSED — and the base had held the answer for thirty-three passes** | 🟢 **`Regulation (EU) 2026/1744`** (OJ `2026-07-24`, in force `2026-07-27`): **Annex III stand-alone high-risk — education — `2026-08-02` → `2027-12-02`**; Annex I → `2028-08-02`; 🔴 **Art. `50` transparency NOT deferred, live since `2026-08-02`.** 🟢 Twelve independent secondary readings this pass. 🔴 **`p837`–`p839` each called it UNRESOLVED and told the reader to quote a RANGE, while `T939`/`p811` already had it** — `ACTION p800-A`'s defect class, recurring in the direction that costs money (`T147`) |
| 🟢 **`839-G1` — "the highest-value unfinished work" — goes from ONE country to FIVE, and the licences DISAGREE** | 🟢 **Chile `CC BY 3.0 CL` · Brazil (INEP) `CC BY` · Mexico Términos de Libre Uso MX — all attribution-only.** 🔴 **Colombia (ICFES Saber 11 / Saber Pro) is `CC BY-SA 4.0` — SHARE-ALIKE, so a derived dataset INHERITS it and cannot sit inside a closed data product.** 🔴 **Argentina UNRESOLVED — the `CC BY 2.5 AR` reading is a site footer, not a dataset field.** 🟡 ICFES separately requires express authorisation for its MARKS (`T148`, `P96`, `844-G1`) |
| 🟢 **The LATAM national education data layer opens, with `3` byte-read `MIT` rows** | 🟢 [`basedosdados/sdk`](https://github.com/basedosdados/sdk) (`MIT`, `1,070 B`, `sha256₁₂ ae8976e97616`, **`433★`**) — a BigQuery datalake with INEP tables already cleaned; the region's **only** production-grade asset. 🔵 **Also a RENAME caught PROSPECTIVELY: `basedosdados/mais` → `422`.** 🟢 Plus `censo-escolar-bi-analytics` and `saber11-brechas-educativas`. 🔴 **Everything else is coursework — `0–30★`, mostly unlicensed or copyleft — corroborating `839-W2` one layer down** |
| 🔴 **`T906`'s egress refusal is NOT European — it reproduces on a second continent** | 🔴 **One loop, `2026-11-16`: `eur-lex.europa.eu` `000` · `dados.gov.br` `000` · `www.datos.gov.co` `000` · `datos.gob.mx` `000` — 🟢 against `raw.githubusercontent.com` `301` in the SAME loop.** 🔵 **The pattern tracks the publisher being GOVERNMENTAL, not the jurisdiction being European.** 🟢 **So `839-G1`'s remainder is an ALLOW-LIST REQUEST, not a search** (`ACTION p844-A`) |
| 🔴 **This base's own action ledger went un-appended for FOUR passes** | 🔴 **`intel/open-gaps.md` is declared append-only and its last entry before this one was `p839`.** `p840`–`p843` added nothing — including `p843`, which created two live ACTIONs and recorded them only in `agents/top.md`. 🔵 **An action recorded in a shelf file is not in the ledger, so the next pass does not see it as owed** (`844-D1`) |
| 🔴 **The mandated agent battery nilled a FIFTH consecutive time** | `p840`, `p841`, `p842`, `p844`. Global legs returned only `DeepTutor` and `LearnHarness`, both already held — the latter re-measured at [`amosblomqvist/learnharness`](https://github.com/amosblomqvist/learnharness), 🔴 `AGPL-3.0`, **`9,634★`**, pushed `2026-11-12`. 🔵 **Copyleft: a demand signal, not a build input.** 🟢 **An informed nil; this pass's yield went to the data layer instead** |

🔴 **Counts: NOT gate-confirmed this pass.** `python3 -I ingest/derive-counts.py` was **refused by
this session's command classifier** — the third such session recorded, and exactly the
session-dependence the channel-discipline table below warns about. 🟡 **Independently derived by a
stated substitute** (`grep -c '^| .*github\.com/'` per file, which counts **every** table row
including pass narratives and is therefore **NOT comparable** to the gate's canonical shelf
figures): `agents/top.md` `521`, `repos/foundations.md` `221`, `verticals/solutions.md` `177`,
`intel/market.md` `#### Update` blocks `181`. 🔵 **Published as what they are — a different
measurement, not the gate's number.**

🟢 **Every region gained a `#### Update` block under the single canonical
`## Opportunities by region`; `p839`'s structural fix was re-checked and HOLDS (`1` canonical
heading, `1` subsection per region).**

---


**Pass `p831` · `2026-11-15`** — `p830` opened the SEN / inclusive-learner tier and closed by naming
its successor's job: repair `p773/grantprobe.sh`, which it had graded `CAPTURED-LIVE` and refused to
pin. 🟢 **`p831` did that repair, then found the hole the repair was sitting in, then opened the
tier the base had never touched.**

## What this pass established

| | |
|---|---|
| 🟢 **The FOUNDATIONAL-LEARNING tier exists and this base had `0` rows in it** | `grep -ric` over the six curated pages, run before anything was filed: `literacy` **`132`**, `STEM` **`592`**, `credential` **`196`** — against **`numeracy 0`**, **`phonics 0`**, **`preschool 0`**, **`kindergarten 0`**, **`early years 0`**, **`decoding 0`**. 🔴 **Thirty-five passes, and not one row for the years in which a child learns to read and count at all** |
| 🟢 **The productive search name is the FUNDING PROGRAMME, not the sector or the statute** | 🔴 The mandated star-ranked battery nilled a **`42`nd** consecutive time. 🟢 `Global Learning XPRIZE` and `EduApp4Syria` returned an entire field-trialled corpus under two GitHub organisations no sector sweep had ever reached — **a prize publishes its finalists' source as a condition of entry**, which is why the permissive supply here is clustered and dated (`T108`) |
| 🔴 **The tier is FIELD-TRIALLED AND FROZEN, and the layer beneath it is alive** | The whole `XPRIZE/GLEXP-*` tree carries a `15`-month Tanzanian RCT and has not been pushed since `2019`; `BloomDesktop` and `libpalaso` were pushed **`2026-11-15`**, `Tangerine` `2026-11-12`, Kolibri `studio` `2026-11-09`. 🟢 **Engagement rule: INHERIT the content and measurement pipelines, FORK the practice apps** (`T108`, `P71`) |
| 🔴 **The licence INDEX disagrees with the licence BYTES on the tier's `128★` leader** | `gh api` says `NOASSERTION` for `vgwb/Antura`, `Antura_arabic`, `Antura_assets` and `curiouslearning/FeedTheMonster`; all four are clean byte-read permissive grants. 🟢 **And one game ships THREE grants — BSD-2-Clause code, CC-BY-4.0 art, CC0-1.0 language data — so reading only the root `LICENSE.md` ships a client build whose ART is unattributed** (`T109`) |
| 🟢 **A promotion failure corrected** | `learningequality/studio` had been named `19` times in this base's trending pages and never shelved; `Tangerine` `6` times; `ricecooker` `4`; `BloomDesktop` `1`. 🔴 **Kolibri — the DELIVERY layer — was shelved and the CONTENT and MEASUREMENT layers under it were not.** All five are shelved now |
| 🔴 **The blocking gate suite reported `1` red. It has `18`** | 🟢 `make -k` on a pristine `git archive HEAD` export: `89` passing checks, **`18` RED BLOCKING GATES**, none of them in `DECLARED_RED`. 🔴 **A fail-fast suite reports a LOWER bound that reads like an upper bound, and here the bound was `1` and the quantity was `18`** (`T110`, `ACTION p831-B`) |
| 🟢 **Three instrument defects repaired, measured rather than asserted** | `p773/grantprobe.sh` measured grant payloads through a captured body: **`7` of `7` resolvable addresses were `1` byte short and `7` of `7` `sha256` values unreproducible.** `p773/probe.sh` was a genuine `CAPTURED-LIVE` that the census graded `BODY-ONLY`, because the body reached the measurement through a SECOND variable — **the lower bound the census documents, now with a named specimen.** And `D9`'s case-aware filename list had never been backported from `grantprobe.sh` to its sibling, which made `Kosudo/nextSIS` and `frappe/lms` read as ungranted |

🟢 **Net effect on the gates: `18` red at `HEAD` → `17` after this pass. `gate-offline` RED → GREEN.
The set difference in the other direction is EMPTY — no gate that was green at `HEAD` is red now.**

🟢 **Counts after this pass**: agents `370`, foundations `168`, verticals `140`, trends `110`,
recipes `71`, market `#### Update` blocks `154`. 🔵 All gate-confirmed with
`python3 ingest/derive-counts.py`; `ragged=0`, `nolink=0`.

**Pass `p811` · `2026-11-13`** — `p810` closed with a transform worth keeping (*"when this base
names a platform often and shelves nothing for it, that is a search instruction"*) and three
shelf gates reporting `RED — the table cannot be located`. 🟢 **`p811` pointed the prescribed
GitHub supply leg at the SYSTEM layer instead of the agent layer and the leg broke open: EMEA's
education agent supply exists, and it is attached to NATIONAL AND REGIONAL SCHOOL PORTALS rather
than to the LMS.** 🟢 **Eight agents added, one foundation, one vertical system of record, two
compose patterns, three trends, five regional market updates — and two long-standing gates taken
from RED to GREEN.** 🔴 **One phantom repository killed before it reached a shelf, and one probe
deliberately NOT run.**

## What this pass established

| | |
|---|---|
| 🟢 **`T31`: EMEA's agent supply arrived — at the LÄNDER, REGIÓN and MINISTRY layer** | 🟢 **Five national or regional school portals gained an MCP surface within five days, all MIT:** [`udondan/lanis`](https://github.com/udondan/lanis) (Schulportal Hessen 🇩🇪), [`udondan/dsbmobile`](https://github.com/udondan/dsbmobile) (DSBmobile 🇩🇪), [`andyswe/admentum-mcp`](https://github.com/andyswe/admentum-mcp) (Admentum 🇸🇪), [`boraita/ipasen_mcp`](https://github.com/boraita/ipasen_mcp) (iPasen/Séneca, Junta de Andalucía 🇪🇸), [`weirdapps/sch-mail`](https://github.com/weirdapps/sch-mail) (Greek School Network 🇬🇷) — plus `edu.by` 🇧🇾 and PRONOTE 🇫🇷 under copyleft. 🔵 **Four of the seven systems are operated by a STATE BODY, so the buyer is a ministry, the route is public tender, and the Art. 27 FRIA duty falls on the deployer because the deployer is public.** 🔴 **All are `0–2★` and single-maintainer: supply, not adoption** |
| 🟢 **`ACTION p802-B` half-discharged from the SUPPLY side** | 🔴 **This base has twice failed to find German classroom deployment STATISTICS.** 🟢 **`p811` found German classroom INTEGRATION CODE instead, at exactly the altitude `p810` predicted — the level of the Land.** 🔵 **Re-shaped once more, and now concretely: ask Hessen's Kultusministerium and an Andalusian *delegación territorial*, because the bodies that operate the portals are the bodies that publish the numbers** |
| 🟢 **Two gates taken from RED to GREEN, one of them blind since `p718`** | 🟢 **`agents/top.md` now carries the column-header signature `ingest/derive-counts.py` has been looking for and reports `derived=65 claimed=65 ragged=0 nolink=0 dupes=0 · GREEN`.** 🔴 **That gate reported `RED — the table cannot be located` on this file for EVERY pass since `p718`, so no pass in the interval could prove its own row count.** 🟢 **`compose/patterns.md` now carries the marked claim `derived recipes: **28**` and is machine-graded too.** 🔴 **`repos/foundations.md` and `verticals/solutions.md` stay RED BY STRUCTURE — they hold 14 and 10 tables respectively and the gate assumes one canonical shelf per file; that is published as a prescription, not fixed by force** |
| 🟢 **The shelf is now REGION-AWARE, by a stated rule (`T32`)** | 🟢 **A row is placed by the region in which the SYSTEM IT INTEGRATES WITH is operated**, read from the repository's own description. 🔴 **Never by the author's nationality.** **🔴 STALE AS WRITTEN AT `p811` — CORRECTED AT `p828` (`2026-11-15`).** The tally below was `Global 49 · EMEA 9 · North America 4 · APAC 3 · LATAM 0`. **That LATAM zero was broken at `p812` and was false for `17` passes.** Derived from `agents/top.md` at `p828`: **`Global` `172` · `APAC` `54` · `EMEA` `51` · `LATAM` `24` · `North America` `23`** (`324` build-safe rows). 🔴 **A count published in the README has no gate — `ingest/derive-counts.py` grades headings against their own page and structurally cannot see a cross-file tally. Either gate it or stop publishing it.** |
| 🔴 ~~**The LATAM zero is the hardest number this base has produced about the region**~~ — **RETRACTED at `p828`: broken at `p812`, see the corrected tally above** | 🔴 **`0` of `65` build-safe agents integrate with a system operated in Latin America** — in the region where this base records `92%` student and `79%` faculty AI use, and `87%` institutional use against `9%` evaluation. 🟢 **EMEA's equivalent gap closed itself this window with seven single-maintainer repos. The LATAM one has not, and the first mover owns the seam** |
| 🟢 **A probe that works, and was deliberately NOT run** | 🟢 **`gh api -X GET search/users -f q='user:LOGIN location:"PLACE"'` resolves a declared location without the blocked `users/{login}` endpoint** — positive control `user:torvalds location:Portland` → `1`. 🔴 **And it has a SILENT defect: an unquoted multi-word place parses as `location:Hong` plus a free-text term, so `location:Hong Kong` returns `0` for an account whose location IS Hong Kong.** 🔴 **Sweeping ~45 individual maintainers' locations is person-level data collection and was declined. Author origin stays unresolved BY CHOICE, and no later pass should "fix" it by running the sweep** |
| 🔴 **`T33`: copyleft in education agents is increasingly INHERITED, so "ask them to relicense" is not a remedy** | 🟢 [`sairo-cyber/pronoteConnect`](https://github.com/sairo-cyber/pronoteConnect) reads `NOASSERTION`; its `LICENSE` opens `SPDX-License-Identifier: GPL-3.0-or-later` **and states why**: *"compatible with the declared GPL-3.0-or-later license of the `@blockshub/pawnote-lts` dependency"*. 🔴 **PRONOTE is the dominant French secondary-school SIS and `pawnote` is the practical way to speak its protocol, so the agent's licence was decided one layer down.** 🟢 **A permissive French deployment needs a clean-room client — scoped and funded as its own deliverable, and a durable asset for whoever builds it** |
| 🔴 **A phantom repository, and the rule it produced** | 🔴 **`fffnite/go-oneroster` has a live `pkg.go.dev` page and does not exist**: the verification channel returns HTTP `422` — `T970`'s invented-address code — while `bgwdotdev/go-oneroster` returns `total_count=1`. 🟢 **A package registry can outlive its repository; a registry page is evidence that a module was PUBLISHED, never that the source still exists** |
| 🟢 **The OneRoster nil re-TESTED rather than restated, and `P27` built to it** | 🟢 **`gh search repositories "oneroster mcp"` → zero items (`2026-11-13`); a vendor connector page dated October 2026 independently states that neither 1EdTech nor ClassLink ships one.** 🔵 **Two channels, same answer.** 🟢 **And the gap is now buildable: [`LongsightGroup/oneroster`](https://github.com/LongsightGroup/oneroster) (`MIT`) covers REST *and* CSV — and US districts hand over CSV far more often than they stand up a REST endpoint** |
| 🟢 **`T30` goes from four jurisdictions to SIX, and `T20` from three implementations to FIVE** | 🟢 **🇺🇸 Florida (State Board, adopted `2026-09-16`, Rule `6A-14.0719`): default-deny on AI in graded work unless the instructor permits, no AI as *"a decision maker, absent human review"*, districts and charter boards to adopt policies by `2027-07-01`.** 🟢 **🇵🇭 CHED Memorandum Order No. `21` s.`2026`: no autonomous determination of academic outcomes without meaningful human review, across `2,366` HEIs / `188,261` faculty / `5.8M` students, `12` months extendable to `18`–`24`.** 🔵 **And the implementers agree without coordination: Andalusia and Belarus both state preview-then-confirm writes in their one-line descriptions** |
| 🟢 **A control worth copying, from Sweden** | 🟢 [`andyswe/admentum-mcp`](https://github.com/andyswe/admentum-mcp) serves a child's messages **ONE ITEM PER CALL** — a quantitative bound on how much of a minor's correspondence can enter a model context in a single tool call. 🔵 **A limit, not a prompt instruction. No other row in this base has it** |
| 🔴 **The capital turned, and it turned AWAY from education toward workforce** | 🔴 **Q1 `2026`: `$512M` across `63` deals, `-24%` in value, with `>70%` going to WORKFORCE TRAINING** (largest round Preply `$150M`). 🟢 **`116` education M&A transactions in Q1 alone.** 🔴 **Coursera–Udemy closed `2026-05-11` and Coursera announced a ~`10%` global workforce cut on `2026-11-09`, four days before this pass** — next to Chegg's `45%`. 🟢 **AI compressed the answer-delivery and catalogue businesses first; the proposal that survives sells governance, evaluation and integration.** 🔴 **All HolonIQ figures are `CITED, NOT READ` — `www.holoniq.com` does not resolve here** |
| 🔵 **A poisoned search token, recorded so it is not re-run** | 🔴 **`xapi mcp server` returns only X (Twitter) API and Xapian repositories.** 🟢 **On this channel `xapi` is not a usable token; use `experience api` or `learning record store`** |

### The p810 table, kept for the record


| | |
|---|---|
| 🔴 **`T27`: `NOASSERTION` is NOT a licence classification — it fails in BOTH directions, proven twice in one pass** | 🟢 [`webworn/openfoam-mcp-server`](https://github.com/webworn/openfoam-mcp-server) `129★` reads `NOASSERTION` and its bytes are **unmodified Apache-2.0** (`10,708 B`, blob `be1f2caa61c7`) — **build-safe, nearly rejected.** 🔴 [`affromero/Sotto`](https://github.com/affromero/Sotto) `35★` reads `NOASSERTION` and its bytes are **PolyForm Noncommercial 1.0.0** — *"Any noncommercial purpose is a permitted purpose"* — **commercially prohibited, and it calls itself "open source" in its own description.** 🔴 **Trusting the field would have rejected a usable repo AND shipped an unusable one, in the same hour** |
| 🟢 **`T28`: a STANDARDS BODY shipped an education agent, and it shipped the controls the vendors do not** | 🟢 **[`Ed-Fi-Exchange-OSS/Prototype-Semantic-Layer-with-MCP`](https://github.com/Ed-Fi-Exchange-OSS/Prototype-Semantic-Layer-with-MCP)** (`Apache-2.0`, pushed `2026-11-12`, **one day before this pass**) — the first education agent here from the body that authors the K-12 data standard. 🟢 **Keycloak OAuth → `get_my_scope` authorisation → Postgres role pinned `default_transaction_read_only = on` with `GRANT SELECT` on the analytics schema only → every tool names the tables it used.** 🔵 **Read-only is enforced at the DATABASE ROLE, not in the prompt — the difference between a control and a convention.** 🔴 README says "demonstration purposes only", so `P24` ships the pattern |
| 🟢 **`T29`: `p809`'s transform is promoted from slogan to INSTRUMENT, because it failed cleanly twice** | 🟢 **Succeeded 4×:** Sakai (`3,937` mentions → `2` agents), SCORM (`3,434` → `2` producers + a validator), Schoology/Infinite Campus (`168` → `3`), Canvas (→ `1` at `119★`). 🔴 **Failed 2×, and the two failures are DIFFERENT KINDS:** OneRoster (`3,043` mentions) returned an **empty result set** — a **supply** gap; PowerSchool (`382`) has **three** servers and **none with a usable grant** — a **licence** gap. 🔵 **Opposite responses: build one, or ask for a grant** |
| 🟢 **A new layer this base had named `3,043` times and shelved nothing for** | 🟢 **`## The rostering layer — OneRoster` is new to `repos/foundations.md`:** [`googleworkspace/oneroster-integration-conformance-tests`](https://github.com/googleworkspace/oneroster-integration-conformance-tests) (`Apache-2.0`, a conformance suite from a party with **no LMS to sell** — use it as a contractual acceptance gate), [`oat-sa/oneroster-import`](https://github.com/oat-sa/oneroster-import) (🔴 `GPL-2.0`, fork ratio `0.88`), [`bgwdotdev/go-oneroster`](https://github.com/bgwdotdev/go-oneroster) (`MIT`, 🔴 stale since `2020`). 🟢 **The asymmetry is the opening: the standard has tooling and NO agent** |
| 🔴 **A REAL regression was introduced and the CONTROL caught it, not the author** | 🔴 **First `make hooks`: `48/72` green. Stashed, pristine `HEAD`: `49/72`.** The extra RED was **`gate-author-key`**. 🔴 **Cause: a `P25` pipeline step labelled `1. Author` (the verb); `p349-keyed-authors` reads "Author" as the noun and demands an identity key.** 🟢 **Fixed to `1. Write`; gate re-run alone = `0` findings; full suite back to `49/72` with an IDENTICAL RED set.** 🔵 **Three runs, published in [`gate-baseline-control`](evidence/gate-baseline-control.2026-11-13-p810.txt)** |
| 🔴 **`D810-1`: the foundations count defect recurs a SEVENTH time — caught before publication** | 🔴 The first derivation compared rows (`69`) against slugs extracted **file-wide** (`73`) and would have published a `4`-row discrepancy as if rows had vanished. 🟢 **The `4` are PROSE links — three of them in the very sentence reporting the count.** 🔵 **`p807` diagnosed the cause and still prescribed a command that does not restrict to rows.** 🟢 **Prescription corrected: extract slugs from ROWS only.** Re-derived `69`/`69`, mapping `1:1` |
| 🟢 **`T970`: the scheduler's prescribed verification method still fails here, and a controlled replacement is now published** | 🔴 **`curl -sI` returns `403` for live AND invented addresses (`T923`) — it cannot verify existence.** 🟢 **`gh api search/repositories -f q="repo:OWNER/NAME"` can: `29/29` live addresses returned `total_count=1` with licence, stars, forks and push date; `2/2` INVENTED addresses returned HTTP `422`.** 🔵 **A `422` and a `1` are distinguishable; two `403`s are not.** Published as [`repo-verification-channel`](evidence/repo-verification-channel.2026-11-13-p810.tsv) |
| 🟢 **`T30`: four jurisdictions, a multilateral and an exam board converge — and England states it as a RULE** | 🟢 **Ofqual: AI may NOT be the sole marker in regulated qualifications, extended to NON-EXAM assessment.** 🔵 **The commercially useful part is that it names the OPEN territory: QA, marker training, moderation, second-marking are explicitly endorsed; sole-decider marking is closed.** 🟢 **`P26` is built to that line.** 🔴 **A reported DfE "progressive disclosure" standard could NOT be confirmed against any government source and is NOT carried** |
| 🟢 **One platform, two risk postures — a first for this base** | 🔴 [`jtayped/sakai-mcp`](https://github.com/jtayped/sakai-mcp) (`MIT`) includes **submission — it writes on the student's behalf.** 🟢 [`sayt25606-rgb/sakai-tasks-mcp`](https://github.com/sayt25606-rgb/sakai-tasks-mcp) (`Apache-2.0`) is **read-only and local.** 🔵 **Same platform, same week, opposite postures** — which answers the most common objection in an education pilot conversation |
| 🔴 **`137` tools is a governance object, not a feature** | 🔴 [`amirtds/cubite-mcp`](https://github.com/amirtds/cubite-mcp) exposes **`137` tools at the signed-in user's permission level** — `p792-D`'s unclaimed risk at nearly **twice** [`jeffercbs/chispa-mcp`](https://github.com/jeffercbs/chispa-mcp)'s `77`. 🟢 **The counter-example now exists in this base: the Ed-Fi prototype exposes SIX tools behind a read-only database role.** 🔵 **Tool count is a design choice, and the standards body chose six** |
| 🟢 **Every region gained an update block — the rotation's actual purpose** | 🟢 **`53` `#### Update` blocks: North America `12`, EMEA `12`, APAC `12`, LATAM `12`, Global `5`.** 🆕 🔴 **NA reverses this file's story: faculty intent to use AI in the US & Canada FELL `76%`→`67%`, the lowest of any region, with `55%` calling AI a serious risk to intellectual development.** 🟢 **Canada's "AI for All" (`2026-06-04`) and Mexico's National AI Plan 2026 finally give both countries named instruments** |
| 🔴 **`ACTION p802-B` fails a SECOND time, and the failure is now shaped well enough to act on** | 🔴 **Germany, France and the Nordics returned regulatory machinery and ZERO classroom deployment figures** — Bundesnetzagentur sandbox pilot `2026-03-17`; INESIA roadmap Feb `2026`; Nordic numbers that are **enterprise-wide, not education**, and that disagree `1.5×` on Denmark (`27.6%` vs `42.0%`). 🟢 **Re-shaped: these are federal/municipal systems, so the figures sit in Länder, académie and kommune publications, not national press releases** |
| 🟢 **India is the region's largest opportunity and it is a SERVICES engagement** | 🟢 **CBSE Circular `Acad-15/2026` (`2026-04-01`): Computational Thinking & AI for Classes III–VIII**, launched with an IIT Madras panel. 🟢 **`18,000`+ CBSE schools already run the `15`-hour SOAR module.** 🔴 **`10 million`+ teachers need training, via NISHTHA, against a named `2026-27` theme — and India is reported to lack the `1.2M`+ qualified professionals to do it.** 🔵 **That is content engineering plus assessment at national scale: `P25`** |
| 🟢 **LATAM's governance gap is confirmed from a THIRD instrument, and the partner list is the map** | 🟢 **UNESCO's Observatory is now dated and institutional: launched `2026-04-14` (Santiago, ECLAC Forum), first member meeting `2026-09-28`, public contact.** 🟢 **Partners are approachable institutions spanning all four markets: CAF, CENIA, Cetic.br, ECLAC, Ceibal, Fundación Santillana, Tecnológico de Monterrey, ProFuturo.** 🔴 **Over half of teachers in Chile and Brazil use AI; under `10%` of institutions have formal guidelines.** 🆕 **CENIA: `13` of `19` countries do not teach early AI adoption at all** 🔴 **Do NOT average the three instruments — different populations** |
| 🟢 **The evidence bar now has a NUMBER, and it is the most useful line here for a bid** | 🔴 **Only `45%` of the most-used education tools have research meeting an ESSA evidence tier.** 🔵 **So an evidence claim is a DIFFERENTIATOR, not table stakes — more than half the incumbent field cannot make one.** 🟢 Pair with education's `86%` gen-AI adoption (highest of any sector) and NA's falling faculty intent: **the sector adopted fastest and is first to show fatigue.** 🟢 **Both facts sell governance and evaluation, not another pilot** |
| 🔴 **Two gaps left OPEN and named, and one agent category negatively evidenced twice** | 🔴 **OneRoster: no agent exists at all.** 🔴 **PowerSchool: three servers, licences `NONE`, `NONE`, `GPL-3.0` — a licence request, not a build.** 🔴 **Curriculum alignment returned only `0★` unlicensed repos; NOTHING was shelved from it.** 🟢 **An informed nil is published rather than padded** |

## Regional summary

🟢 **`p811` delta by region, before the `p810` table below:** **North America** — Florida becomes
the fourth dated state obligation (Rule `6A-14.0719`, districts by `2027-07-01`) and the
consolidation reached headcount (Coursera `-10%`, `2026-11-09`). **EMEA** — the region's agent
supply appeared at the portal layer, five systems in five days, four of them state-operated.
**APAC** — CHED Memorandum Order No. `21` s.`2026` (`2,366` HEIs, `12`-month window) and
Australia's automated-decision transparency duty from `2026-12-10`. **LATAM** — the nil is now
measured: `0` of `65` agents attach to a system operated in the region. **Global** — Q1 `2026`
funding `$512M`, `>70%` to workforce training, `116` M&A transactions.


| Region | The opening | The named gap |
|---|---|---|
| **North America** | 🔴 **The densest legislative calendar in the world and still a pipeline rather than a market.** 🟡 **Three trackers, three counts, three definitions: `134` bills across `31` states (`p797`), *"nearly `100`"* state bills touching student AI use, `15`+ states having introduced or passed legislation — 🔵 quote the STATE and the bill number, never the national total.** 🟢 Dated obligations to sell against: NC `SL 2026-41` (`2026-12-31` → `2027-06-30` → `2028-06-30`), 🔴 **Ohio's districts must adopt an AI framework by `2026-07-01`**, 🟢 Mississippi embeds AI literacy for all incoming undergraduates from Fall `2026`. 🆕 🟡 **A California ballot initiative on AI and MINORS would bind education deployments through child-safety law rather than education law** | 🔴 **No spend figure for Canada or Mexico, FIFTH pass, because the mandated query says "North America" and returns US-only results.** 🟢 Specific enough to fix: name the countries. 🆕 🔵 **Chegg cut `45%` of staff (`388` roles) — the first thing AI destroyed here was the answer-delivery business, which is what "a chatbot that answers student questions" asks to become** |
| **EMEA** | 🟢 **`Regulation (EU) 2026/1744` dates everything, now FOUR-source corroborated (`T939`), and the SPLIT is the commercial point: Art. `50` transparency live since `2026-08-02` and NOT deferred, while Annex III standalone high-risk — education — moved to `2027-12-02`.** 🔵 The expensive work has `13` months of slack; the cheap work is already late. 🟢 Art. `5` prohibitions live (emotion recognition in education banned since Feb `2025`); Art. `27` FRIA owed by public deployers; 🆕 Commission Art. `6` draft guidelines `2026-05-19`. 🟢 **Still the best line in this base: `63%` of European teachers use AI and `16%` believe general-purpose AI improves outcomes** — a `47`-point gap is a market that tried the generic tool and rejected it | 🔴 **Spend unanswerable: `$2.11B`–`$5.86B`, a `2.8×` spread.** 🔴 **Still ONE European-origin open-source education agent at scale** ([`tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) 🇫🇷, ★`102`); 🆕 🟢 **`p798` adds three European permissive rows and NONE is at scale** — supply is appearing, adoption is not. 🔵 Same shape as LATAM, one tier up |
| **APAC** | 🔴 **The regional headline is still a warning: Korea `34.2%` → `5.2%` of schools in twelve months once the mandate became discretionary — 🔴 and `p798` could not reach the ministry to verify it.** 🟢 **The compellable obligations are where the money is:** 🇻🇳 education high-risk under the Law on AI (`2026-03-01`) requiring **pre-deployment registration**; 🇦🇺 **TEQSA compels an institutional generative-AI action plan from EVERY provider**; 🇰🇷 AI Basic Act in force `2026-01-22`. 🟢 🇨🇳 `教科信〔2026〕1号` with three nameable assets incl. the state-commissioned open-source `启悟学习社区` — 🔵 the only contribution-shaped entry route here. 🆕 🟢 **Ipsos `2026` finds LOWER support for banning AI in schools across Asian markets — permission to operate running AHEAD of regulation, the inverse of Europe** | 🔴 **`0` procurement documents for India, Singapore or Australia, FIFTH pass — a TENDER-access gap, not a discovery gap.** 🔴 **`0` new APAC-origin repositories this pass, while the two highest-starred rows in this base remain APAC university projects** (`DeepTutor` ★`58,622`, `OpenMAIC` ★`43,392`). 🆕 🟢 **A named place to look: the World Bank's Global EdTech Policy Academy on AI, Seoul, `2026-08-31`–`09-04`** |
| **LATAM** | 🆕 🔴 **`p820`: the clock's SCOPE was understated here, and the correction is larger than the fix.** The instrument is STAGE-GATED, not age-gated: generative and conversational AI is barred **through `5º ano` — the whole of primary** — and admitted from `6º ano` only under teacher mediation (`T67`). 🔴 **Two assessment rules recovered with it (`T68`): academic sanction founded EXCLUSIVELY on an AI detector is PROHIBITED, and AI pre-correction of redções is admitted only as a preparatory step with the mark reserved to the teacher.** 🟢 **`P50` is the build.** 🔵 **`ACTION p819-C` is discharged by `T66` — the "unverified age floor" was THIS instrument, held in three files since `p790` and never linked to the lead.** — 🟢 **Brazil's `12`-month clock is the anchor: `Parecer CNE/CP nº 15/2026`, homologated `2026-11-10`, prohibitions effective on publication, `12` months for policies, governance instruments and CONTRACTS** — 🔴 `CITED, NOT READ`, `www.gov.br` refused again. 🆕 🟢 **A second adoption instrument, and the strongest LATAM number this base holds: Digital Education Council LATAM `2026` with Tecnológico de Monterrey — `92%` of students and `79%` of faculty using AI against `30%` who believe their institution has responded effectively.** 🟢 The evaluation gap keeps its denominator (UNESCO IESALC, `200` institutions / `19` countries): `87%` use · `9%` evaluation · 🔴 **`8%` any AI budget, `4%` among PUBLIC universities.** 🆕 🟢 **Two named channels: the IDB's `193`-initiative LAC inventory, and EdTech Hub + Fundación Ceibal (Sept `2026`)** | 🔴 **The supply correction that reverses `p797`: `78.1%` ungranted against a `60.4%` English baseline, so grant hygiene is an intake rule rather than a regional programme — while `94.5%` zero stars and a ceiling of `5` is the real constraint** (`T940`). 🔴 **And `es` ≠ LATAM: two of this pass's best in-language rows are Spanish, `gh api users/{login}` is refused, so origin is not resolvable at scale and `LATAM?` is published rather than guessed** (`T935`) |
| **Global** | 🟢 **Five converging legs, and the fifth arrived from the multilateral channel this pass: the OECD's `2026` Digital Education Outlook says AI helps learning only when pedagogy stays in control** — 🔵 **the same conclusion as `T907`'s RCT reading and as every regulator here. When the trials, the regulators and the OECD agree on the control point, it stops being a design preference and becomes the thing a proposal must evidence.** 🟢 **AI proposes, a named human decides, the system proves it** | 🔴 The platform layer is copyleft while the agent layer is permissive — the same architectural decision in every engagement. 🔴 **And `p792-D` is still unclaimed with a sharper edge: no independent security or data-governance evaluation of any education MCP server exists, and [`jeffercbs/chispa-mcp`](https://github.com/jeffercbs/chispa-mcp) now exposes `77` classroom tools at the teacher's own permission level** |

## Files

| File | What it holds | Mode |
|---|---|---|
| [`agents/top.md`](agents/top.md) | 🟢 **`66` agents — `59` build-safe, `7` copyleft, `9` rejected.** 🟢 **`22` added, the largest single-pass addition recorded** · counts re-derived, not carried | prepended each pass |
| [`agents/trending.md`](agents/trending.md) | What is new per window · 🟢 **`NOASSERTION` resolved in both directions; the Ed-Fi control stack** | 🟢 **append-only** |
| [`repos/foundations.md`](repos/foundations.md) | 🟢 **`69` repos, `1:1` with rows** · 🟢 **`6` added, SIX-pass nil BROKEN** · 🟢 new **OneRoster rostering layer** · `runno` as the untrusted-code boundary | prepended each pass |
| [`repos/trending.md`](repos/trending.md) | Repo movement per window · 🔴 the `D810-1` count defect and its corrected prescription | 🟢 **append-only** |
| [`verticals/solutions.md`](verticals/solutions.md) | 🟢 **Sakai, Canvas, Schoology/Infinite Campus and Cubite gain agent surfaces** · 🟢 **one platform at TWO risk postures** · `FenixEdu` as the EMEA SIS | prepended each pass |
| [`intel/market.md`](intel/market.md) | 🟢 **`53` `#### Update` blocks — NA `12`, EMEA `12`, APAC `12`, LATAM `12`, Global `5`.** Every region gained one | rewritten each pass |
| [`intel/trends.md`](intel/trends.md) | 🟢 **`33` trends · `T31`–`T33` added** (EMEA's portal-layer supply · region-by-target-system · inherited copyleft) · 🟢 **`T30` extended to six jurisdictions**. Superseded: 🟢 **`30` trends · `T27`–`T30` added** (licence field · standards bodies · the transform as instrument · the sole-decider convergence) | prepended each pass |
| [`compose/patterns.md`](compose/patterns.md) | 🟢 **`28` patterns · `P27`–`P28` added** — the OneRoster agent nobody has built · the national-school-portal family agent · 🟢 **count now machine-graded**. Superseded: 🟢 **`26` patterns · `P24`–`P26` added** — FRIA-survivable early warning · Markdown→SCORM with a conformance gate · assessment shaped to Ofqual's OPEN categories | prepended each pass |
| [`intel/open-gaps.md`](intel/open-gaps.md) | Action ledger · `ACTION p810-A` (re-probe rows rejected on a blank licence signal alone) | 🟢 **append-only** |
| [`evidence/*2026-11-13-p811*`](evidence/) | 🟢 **The three machine outputs behind this pass** — [`repo-verification`](evidence/repo-verification.2026-11-13-p811.tsv) (14 addresses, 2 negative controls), [`origin-location-channel`](evidence/origin-location-channel.2026-11-13-p811.tsv) (the probe, its silent defect, and the declaration that it was not run at scale), [`websearch-legs`](evidence/websearch-legs.2026-11-13-p811.tsv) (every prescribed leg with its yield) | — |
| [`evidence/*2026-11-13-p810*`](evidence/) | 🟢 **The three machine outputs behind this pass** — the verification channel with its negative control, the licence byte reads, and the **three-run gate control that caught this pass's own regression** | — |

## 🔴 Channel discipline — read before quoting anything here

| Claim type | Status |
|---|---|
| Repository existence | 🟢 **Byte-verified on the blobless-clone channel: `25` addresses this pass, `0` failures.** 🔴 **`curl -sI` — the method the scheduler's prompt names — returns `403` for a live address AND for an invented one, so it cannot distinguish them here (`T923`).** 🔵 Read that instruction as *"verify existence"* and satisfy it with the clone |
| 🆕 🟢 **Rendered `github.com` HTML page** | 🟢 **The channel THIS pass ran on, and it is controlled: `200` with stars, licence classification, release and `forked from` for a live address; `404` for an invented one** (`T952`, [`html-channel-control`](evidence/html-channel-control.2026-11-12-p800.tsv)). 🔴 **It yields NO grant bytes, NO blob shas and NO dependency trees, and stars only as RENDERED (`58.6k`, not `58,622`). A discovery and triage channel — never a channel of record for a grant** |
| 🆕 🔴 **Fork and rename state** | 🔴 **Read the `forked from` notice BEFORE writing a row.** `p800` found `5` forks among `34` addresses (`15%`), `3` standing in for a materially larger canonical, and a `0`-star fork of `tutor-mcp` carrying a BYTE-IDENTICAL description to the `102`-star canonical (`T950`). 🟢 **An address absent from `search/repositories` but alive on clone is a FORK or a RENAME before it is anything else** |
| 🆕 🔴 **A settled fact that never reached a shelf** | 🔴 **`p606-K` settled `openedx/openedx-platform`; two shelves still write `openedx/edx-platform` with grant bytes attached to the stale slug.** 🟢 **`ACTION p800-A`: diff this ledger's oldest settled address facts against every shelf that writes them** |
| 🆕 **Per-repository metadata** | 🔴 **`gh api repos/{owner}/{repo}` and `gh api users/{login}` are REFUSED in this session; `gh api search/*` answers normally** (`T941`). 🔴 **A refused call returns a JSON body, and a JSON body is a string that fits in any TSV cell** — assert the shape of a cell before publishing it |
| Licence **grant** | 🟢 **Byte-verified by title line + clause text + byte size, with blob sha and HEAD commit sha beside every value.** 🔴 **The unit is the GRANT, not the file and not the repository** |
| 🆕 **Licence SCREENING** | 🔴 **`p795-A`'s byte-size band measures the length of the copyright holder's name: `4` byte-identical MIT payloads span `1,062`–`1,096 B` and `3` are flagged** (`T938`). 🟢 **Use [`p135`](compose/code/p135-licence-sha-identity/)'s copyright-stripped normalisation instead** |
| 🆕 🔴 **A repository NAME is a marketing string** | 🔴 **`-public`, `-oss`, `-community` and `-free` in a repository name trigger a BYTE-READ exactly as `NOASSERTION` does — they are never evidence of a grant.** 🟢 **`T60`'s specimen: [`dequelabs/axe-mcp-server-public`](https://github.com/dequelabs/axe-mcp-server-public), published by the author of the `axe` standard, licence field `NOASSERTION`, name ending `-public` — and the bytes (`1,049 B`, `sha256:05cf369f…`) open `Proprietary License` and state *"No license is granted to use, modify, or distribute."* Three signals said usable; only the bytes said otherwise.** 🟢 **Written into this checklist at `p820`, discharging `ACTION p818-C`** |
| Licence **restrictions** | 🔴 **Still the direction instruments fail in, and the LOCATION keeps moving:** a second licence file (`T914`), a different repository (`T925`), two grants in one file (`T915`), 🆕 **and the README under an unmodified MIT** (`T937`) |
| **Region placement** | 🔴 **A query LANGUAGE is not a region** (`T935`). 🔴 **The `es` leg returns Spain; the APAC leg returned the UAE.** 🟢 **Rows placed on language alone are published as `LATAM?`, and the closed vocabulary is never given a guess** |
| Star counts | 🟢 **Re-measured on `search/repositories`.** 🔴 A secondary source was off by `-23%` on this base's largest row at `p797` |
| 🔴 **Running this repository's own code — RE-CORRECTED at `p820`: it is SESSION-DEPENDENT, not a property of this repository** | 🔴 **REFUSED in `p818`, `p819` AND `p820` — three consecutive passes. The sandbox classifier declines `python3 -I ingest/derive-counts.py`, so all five graded counts are carried on independently written REIMPLEMENTATIONS of that gate (`ACTION p820-B`). Two such substitutes, written independently at `p819` and `p820`, agree on all five figures.** 🔵 **Read this row as: assume NOTHING about whether committed code will run — test it each pass and publish the result either way.** 🟡 **`p811` recorded the opposite and was right about `p811`:** 🟢 **It ran THERE. `make hooks` completed and `python3 -I ingest/derive-counts.py .` was used as a working control before and after every edit this pass.** 🔵 **So the claim below was true of `p800`'s session and is NOT a property of this repository.** 🔴 **Baseline failing-gate set at `HEAD` before this pass: `gate-absence`, `gate-dates`, `gate-derived-counts`, `gate-enumeration`, `gate-evidence-store`, `gate-offline`, `gate-shelf-consistency`, `recount` — carried pre-existing, and re-checked after this pass's edits.** Superseded text: 🔴 **REFUSED in this session.** An attempt to run one instrument's test suite was declined by the command classifier. 🔴 **So `make hooks`, `make commit-gates` and `ACTION p797-H` are undischargeable from here, and [`p135`](compose/code/p135-licence-sha-identity/) is cited from its README and source rather than from a run.** 🟢 **No claim in this pass depends on executing committed code** |
| Every market, adoption and regulatory figure | 🔴 **Search-channel testimony.** 🔴 **`T906` now names TEN domains that fail at `CONNECT`:** `eur-lex.europa.eu`, `oecd.org`, `unesco.org`, `op.europa.eu`, `iesalc.unesco.org`, `digital-strategy.ec.europa.eu`, `www.gov.br`, and 🆕 **`www.moe.go.kr`, `moe.go.kr`, `english.moe.go.kr`.** 🔵 **Every one is a government or multilateral publisher and no commercial domain has ever failed this way — a network POLICY, not an outage** |
| 🟢 **A numbered instrument** | 🟢 **Now tested rather than asserted: `Regulation (EU) 2026/1744` was challenged by this pass's own EMEA leg and held across four independent legal readings** (`T939`). 🔵 **`CITED, NOT READ` is usable because anyone can check a number in one lookup** |

🔵 **Four standing cautions now hold simultaneously, and `p798` earned the fourth by watching a
two-minute control leg overturn five passes of narrative.** 🟢 **`p795-G`: re-run a zero-returning
sweep on the finding that queued it.** 🔴 **`p796-G`: a control set must span the population's
KINDS.** 🔴 **`p797-A`: prefer a smaller DECLARED scope to a cleverer predicate.** 🆕 🟢 **`p798-G`:
when a finding is a RATE, measure that rate somewhere it should NOT hold — it is the cheapest of
the four and it is the one that would have caught `T931` before it shipped.**
