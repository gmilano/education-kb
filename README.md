---
industry: education
region: Global
updated: 2026-11-12
---

# Globant AI Studios — Education KB

**Pass `p798` · `2026-11-12`** — `p797` found five LATAM-origin education agents, none of them
licensed, and concluded that the region's constraint was grant hygiene. 🟢 **`p798` gave that claim
a denominator and a control leg, and it does not survive either.** 🔴 **Ungranted is the default for
a young repository in ANY language — `78.1%` in-language against `60.4%` in English.** 🔴 **What is
specific to the in-language population is that nobody has adopted any of it: `94.5%` sit at zero
stars and the whole population's ceiling is `5`.** 🟢 **Four of this pass's seven findings are an
instrument pointed at the wrong unit, and in two cases the right instrument was already in this
repository and had fallen out of use.** The two trending ledgers and the action ledger are appended
to, never rewritten.

## What this pass established

| | |
|---|---|
| 🔴 **The LATAM recommendation reverses, nine days after it was given** | 🔴 **Not a search (`p797`), not a licensing campaign (`p798` corrects that): localise a global permissive base and read the in-language repositories as DESIGN EVIDENCE** |
| 🟢 **The census that did it** | 🟢 **`73` in-language addresses · `149` English control addresses · `16` query legs · `222` deduplicated rows** |
| 🔴 **The gap that is real but modest** | 🔴 **`78.1%` vs `60.4%` ungranted — `1.29×`** |
| 🔴 **The gap that is categorical** | 🔴 **`94.5%` vs `19.5%` at ZERO stars · population max `5` vs `4,912` · `0` rows above `20` stars vs `16`** |
| 🟢 `7` agents added, every grant byte-verified | 🟢 **Blob sha + HEAD commit sha on every row** (`T927`'s rule), `0` clone failures on `15` addresses |
| 🟢 **`ACTION p797-G` discharged — and the answer is a shape, not a price** | 🔴 **Moodle's partner fees, royalties and trademark grants are NOT published.** 🟢 Two tiers, `101`+ partners, scope known |
| 🔴 **`ACTION p797-F` discharged, negative** | 🔴 **Korea's ministry is the 8th, 9th and 10th domain `T906` names** |
| 🟢 **`ACTION p797-E` discharged as a measurement and reframed as a deliverable** | 🟢 **A selection rule (`3` tests) + `4` new drafts out of `57` candidates** — and the row the rule REJECTS is the instructive one |
| 🟢 **The EMEA anchor survived a direct challenge** | 🟢 **`Regulation (EU) 2026/1744` — four independent legal readings concur on the number and the dates** |
| 🔴 **A new session-policy limit, measured not assumed** | 🔴 **Executing committed repository code is refused here, so `make hooks` and `ACTION p797-H` are undischargeable from this session** |
| 🔴 Defects in this pass's own instrument, caught before publication | 🔴 **`1`** — a refused API call's JSON body shipped as data in `16` rows of two columns. 🟢 Both versions published |

## 🟢 The three findings worth reading first

**1. A rate without a denominator reversed five passes of regional strategy, and one control leg
cost two minutes.**
🔴 `p797` reported *"`5` of `5` LATAM-origin agents serve no grant"* and `T931` read it as a regional
pathology. 🟢 **`p798` ran the same question on `gh api search/repositories` across `10` in-language
legs and `6` English control legs: `78.1%` of `73` in-language rows are ungranted — against `60.4%`
of `149` English rows.** 🔵 **So "no licence" is a property of a YOUNG repository, not of a region,
and a LATAM licensing campaign is aimed at the wrong variable.** 🔴 **The thing that IS regional is
adoption: `94.5%` of the in-language population has zero stars, its maximum is `5`, and not one row
clears `20` — against `16` English rows above `20` and a maximum of `4,912`.** 🟢 **The engagement
consequence, stated plainly because it reverses advice this base gave nine days ago: take a global
permissive base, localise it, and read the in-language repositories as a REQUIREMENTS DOCUMENT.**
🔵 **They are worth reading precisely because nobody starred them — what a regional teacher builds
with no audience is offline-capable, LMS-attached, messaging-delivered and teacher-gated.**
→ [`agents/top.md`](agents/top.md), [`intel/trends.md`](intel/trends.md) `T940`, [`compose/patterns.md`](compose/patterns.md) `P798-1`

**2. An instrument library this size can regress by ADDING something.**
🔴 **`p795-A` screens MIT grades by byte size against a `1,066`–`1,072 B` band. Four MIT payloads
measured this pass span `1,062`–`1,096 B` and their clause text is byte-identical** — md5
`aeb812008e99` once the copyright line is removed. 🔴 **The `34`-byte spread is
`Copyright (c) 2026 jeffercbs` against
`Copyright (c) 2026 Scientific Learning Skills Contributors`, and nothing else: `3` of `4` clean
rows are flagged, and the flag rate rises with the length of the author's name.** 🟢 **And this base
built the exact instrument `660` passes ago:
[`compose/code/p135-licence-sha-identity/`](compose/code/p135-licence-sha-identity/) states the
problem in its own README and answers it with a `body` normalisation level that removes copyright
notices as spans, plus `MODIFIED_SUPERSET` for the `MIT + visible-attribution` rider class
`p795-A` exists to catch.** 🔵 **Before building a screen, grep the library for the measurement it
approximates.** 🔴 **Same pass, same shape, twice more: the README-vs-payload read `T937` needed
already exists at [`p1060-readme-vs-payload`](compose/code/p1060-readme-vs-payload/), and the origin
read `T935` needs exists at [`p800-region-provenance`](compose/code/p800-region-provenance/).**
→ [`repos/foundations.md`](repos/foundations.md), [`intel/trends.md`](intel/trends.md) `T938`

**3. An author wrote the content carve-out this base has been asking for, in `571` bytes.**
🔴 `T916` established that on a code/content split GitHub's classifier reports the CODE licence and
silently drops the CONTENT licence — and in education the content licence governs the curriculum.
🟢 **[`danielgalanv/oral-ia`](https://github.com/danielgalanv/oral-ia)'s `NOTICE` does it unprompted:
the Apache-2.0 grant covers the code, tests, specifications and its own documentation, and does NOT
cover the teaching material, the third-party document texts used in the pilot, or the language
models — each keeping its own holders' conditions.** 🔵 **Every deliverable in this base mixes those
same four layers with four different owners and almost none of them says so.** 🟢 **It is now a
week-one deliverable with a real precedent to copy instead of a lawyer to brief.**
→ [`verticals/solutions.md`](verticals/solutions.md), [`compose/patterns.md`](compose/patterns.md) `P798-2`

## Regional summary

| Region | The opening | The named gap |
|---|---|---|
| **North America** | 🔴 **The densest legislative calendar in the world and still a pipeline rather than a market.** 🟡 **Three trackers, three counts, three definitions: `134` bills across `31` states (`p797`), *"nearly `100`"* state bills touching student AI use, `15`+ states having introduced or passed legislation — 🔵 quote the STATE and the bill number, never the national total.** 🟢 Dated obligations to sell against: NC `SL 2026-41` (`2026-12-31` → `2027-06-30` → `2028-06-30`), 🔴 **Ohio's districts must adopt an AI framework by `2026-07-01`**, 🟢 Mississippi embeds AI literacy for all incoming undergraduates from Fall `2026`. 🆕 🟡 **A California ballot initiative on AI and MINORS would bind education deployments through child-safety law rather than education law** | 🔴 **No spend figure for Canada or Mexico, FIFTH pass, because the mandated query says "North America" and returns US-only results.** 🟢 Specific enough to fix: name the countries. 🆕 🔵 **Chegg cut `45%` of staff (`388` roles) — the first thing AI destroyed here was the answer-delivery business, which is what "a chatbot that answers student questions" asks to become** |
| **EMEA** | 🟢 **`Regulation (EU) 2026/1744` dates everything, now FOUR-source corroborated (`T939`), and the SPLIT is the commercial point: Art. `50` transparency live since `2026-08-02` and NOT deferred, while Annex III standalone high-risk — education — moved to `2027-12-02`.** 🔵 The expensive work has `13` months of slack; the cheap work is already late. 🟢 Art. `5` prohibitions live (emotion recognition in education banned since Feb `2025`); Art. `27` FRIA owed by public deployers; 🆕 Commission Art. `6` draft guidelines `2026-05-19`. 🟢 **Still the best line in this base: `63%` of European teachers use AI and `16%` believe general-purpose AI improves outcomes** — a `47`-point gap is a market that tried the generic tool and rejected it | 🔴 **Spend unanswerable: `$2.11B`–`$5.86B`, a `2.8×` spread.** 🔴 **Still ONE European-origin open-source education agent at scale** ([`tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) 🇫🇷, ★`102`); 🆕 🟢 **`p798` adds three European permissive rows and NONE is at scale** — supply is appearing, adoption is not. 🔵 Same shape as LATAM, one tier up |
| **APAC** | 🔴 **The regional headline is still a warning: Korea `34.2%` → `5.2%` of schools in twelve months once the mandate became discretionary — 🔴 and `p798` could not reach the ministry to verify it.** 🟢 **The compellable obligations are where the money is:** 🇻🇳 education high-risk under the Law on AI (`2026-03-01`) requiring **pre-deployment registration**; 🇦🇺 **TEQSA compels an institutional generative-AI action plan from EVERY provider**; 🇰🇷 AI Basic Act in force `2026-01-22`. 🟢 🇨🇳 `教科信〔2026〕1号` with three nameable assets incl. the state-commissioned open-source `启悟学习社区` — 🔵 the only contribution-shaped entry route here. 🆕 🟢 **Ipsos `2026` finds LOWER support for banning AI in schools across Asian markets — permission to operate running AHEAD of regulation, the inverse of Europe** | 🔴 **`0` procurement documents for India, Singapore or Australia, FIFTH pass — a TENDER-access gap, not a discovery gap.** 🔴 **`0` new APAC-origin repositories this pass, while the two highest-starred rows in this base remain APAC university projects** (`DeepTutor` ★`58,622`, `OpenMAIC` ★`43,392`). 🆕 🟢 **A named place to look: the World Bank's Global EdTech Policy Academy on AI, Seoul, `2026-08-31`–`09-04`** |
| **LATAM** | 🟢 **Brazil's `12`-month clock is the anchor: `Parecer CNE/CP nº 15/2026`, homologated `2026-11-10`, prohibitions effective on publication, `12` months for policies, governance instruments and CONTRACTS** — 🔴 `CITED, NOT READ`, `www.gov.br` refused again. 🆕 🟢 **A second adoption instrument, and the strongest LATAM number this base holds: Digital Education Council LATAM `2026` with Tecnológico de Monterrey — `92%` of students and `79%` of faculty using AI against `30%` who believe their institution has responded effectively.** 🟢 The evaluation gap keeps its denominator (UNESCO IESALC, `200` institutions / `19` countries): `87%` use · `9%` evaluation · 🔴 **`8%` any AI budget, `4%` among PUBLIC universities.** 🆕 🟢 **Two named channels: the IDB's `193`-initiative LAC inventory, and EdTech Hub + Fundación Ceibal (Sept `2026`)** | 🔴 **The supply correction that reverses `p797`: `78.1%` ungranted against a `60.4%` English baseline, so grant hygiene is an intake rule rather than a regional programme — while `94.5%` zero stars and a ceiling of `5` is the real constraint** (`T940`). 🔴 **And `es` ≠ LATAM: two of this pass's best in-language rows are Spanish, `gh api users/{login}` is refused, so origin is not resolvable at scale and `LATAM?` is published rather than guessed** (`T935`) |
| **Global** | 🟢 **Five converging legs, and the fifth arrived from the multilateral channel this pass: the OECD's `2026` Digital Education Outlook says AI helps learning only when pedagogy stays in control** — 🔵 **the same conclusion as `T907`'s RCT reading and as every regulator here. When the trials, the regulators and the OECD agree on the control point, it stops being a design preference and becomes the thing a proposal must evidence.** 🟢 **AI proposes, a named human decides, the system proves it** | 🔴 The platform layer is copyleft while the agent layer is permissive — the same architectural decision in every engagement. 🔴 **And `p792-D` is still unclaimed with a sharper edge: no independent security or data-governance evaluation of any education MCP server exists, and [`jeffercbs/chispa-mcp`](https://github.com/jeffercbs/chispa-mcp) now exposes `77` classroom tools at the teacher's own permission level** |

## Files

| File | What it holds | Mode |
|---|---|---|
| [`agents/top.md`](agents/top.md) | `137` addresses · 🟢 **`7` added, every grant byte-verified with blob + HEAD sha** | prepended each pass |
| [`agents/trending.md`](agents/trending.md) | What is new per window · **`939` `##` sections** | 🟢 **append-only** |
| [`repos/foundations.md`](repos/foundations.md) | Foundational repos · 🔴 **`0` added this pass, and the scope statement that says why** | prepended each pass |
| [`repos/trending.md`](repos/trending.md) | Repo movement per window · **`937` `##` sections** · 🔴 the channel census | 🟢 **append-only** |
| [`verticals/solutions.md`](verticals/solutions.md) | LMS, SIS, assessment and interop platforms · 🟡 **the Moodle Partner route, as far as the public record goes** | prepended each pass |
| [`intel/market.md`](intel/market.md) | Market range and **Opportunities by region** (`5` subsections) | rewritten each pass |
| [`intel/trends.md`](intel/trends.md) | `T935`–`T941` | prepended each pass |
| [`compose/patterns.md`](compose/patterns.md) | `P798-1`–`P798-4` — LATAM localisation · the `571`-byte content boundary · an education-MCP gate · EMEA Art. `50`-first | prepended each pass |
| [`intel/open-gaps.md`](intel/open-gaps.md) | Action ledger · `p797` disposition + `p799` queue | 🟢 **append-only** |
| [`intel/licence-requests/`](intel/licence-requests/) | 🟢 **`9` drafts + the `3`-test SELECTION RULE** (`ACTION p797-E`) | 🔴 drafted, NOT sent |
| [`ingest/p798-latam-grant-census.sh`](ingest/p798-latam-grant-census.sh) | 🟢 The in-language census, ONLINE | — |
| [`ingest/p798-grant-byte-verify.sh`](ingest/p798-grant-byte-verify.sh) | 🟢 The blobless-clone grant byte channel, ONLINE | — |
| `evidence/*2026-11-12-p798*` | The six machine outputs behind this pass, 🔴 **including one UNCORRECTED first run** | — |

🔴 **One artefact published deliberately in its WRONG form, so the correction can be re-derived
rather than taken on trust:**
[`candidate-grant-bytes-UNCORRECTED-v1`](evidence/candidate-grant-bytes-UNCORRECTED-v1.2026-11-12-p798.tsv)
carries a JSON error blob in its `archived` and `pushed` columns on all `16` rows, because the
instrument called `repos/{owner}/{repo}` per address and that call is refused in this session.

## 🔴 Channel discipline — read before quoting anything here

| Claim type | Status |
|---|---|
| Repository existence | 🟢 **Byte-verified on the blobless-clone channel: `25` addresses this pass, `0` failures.** 🔴 **`curl -sI` — the method the scheduler's prompt names — returns `403` for a live address AND for an invented one, so it cannot distinguish them here (`T923`).** 🔵 Read that instruction as *"verify existence"* and satisfy it with the clone |
| 🆕 **Per-repository metadata** | 🔴 **`gh api repos/{owner}/{repo}` and `gh api users/{login}` are REFUSED in this session; `gh api search/*` answers normally** (`T941`). 🔴 **A refused call returns a JSON body, and a JSON body is a string that fits in any TSV cell** — assert the shape of a cell before publishing it |
| Licence **grant** | 🟢 **Byte-verified by title line + clause text + byte size, with blob sha and HEAD commit sha beside every value.** 🔴 **The unit is the GRANT, not the file and not the repository** |
| 🆕 **Licence SCREENING** | 🔴 **`p795-A`'s byte-size band measures the length of the copyright holder's name: `4` byte-identical MIT payloads span `1,062`–`1,096 B` and `3` are flagged** (`T938`). 🟢 **Use [`p135`](compose/code/p135-licence-sha-identity/)'s copyright-stripped normalisation instead** |
| Licence **restrictions** | 🔴 **Still the direction instruments fail in, and the LOCATION keeps moving:** a second licence file (`T914`), a different repository (`T925`), two grants in one file (`T915`), 🆕 **and the README under an unmodified MIT** (`T937`) |
| **Region placement** | 🔴 **A query LANGUAGE is not a region** (`T935`). 🔴 **The `es` leg returns Spain; the APAC leg returned the UAE.** 🟢 **Rows placed on language alone are published as `LATAM?`, and the closed vocabulary is never given a guess** |
| Star counts | 🟢 **Re-measured on `search/repositories`.** 🔴 A secondary source was off by `-23%` on this base's largest row at `p797` |
| 🆕 **Running this repository's own code** | 🔴 **REFUSED in this session.** An attempt to run one instrument's test suite was declined by the command classifier. 🔴 **So `make hooks`, `make commit-gates` and `ACTION p797-H` are undischargeable from here, and [`p135`](compose/code/p135-licence-sha-identity/) is cited from its README and source rather than from a run.** 🟢 **No claim in this pass depends on executing committed code** |
| Every market, adoption and regulatory figure | 🔴 **Search-channel testimony.** 🔴 **`T906` now names TEN domains that fail at `CONNECT`:** `eur-lex.europa.eu`, `oecd.org`, `unesco.org`, `op.europa.eu`, `iesalc.unesco.org`, `digital-strategy.ec.europa.eu`, `www.gov.br`, and 🆕 **`www.moe.go.kr`, `moe.go.kr`, `english.moe.go.kr`.** 🔵 **Every one is a government or multilateral publisher and no commercial domain has ever failed this way — a network POLICY, not an outage** |
| 🟢 **A numbered instrument** | 🟢 **Now tested rather than asserted: `Regulation (EU) 2026/1744` was challenged by this pass's own EMEA leg and held across four independent legal readings** (`T939`). 🔵 **`CITED, NOT READ` is usable because anyone can check a number in one lookup** |

🔵 **Four standing cautions now hold simultaneously, and `p798` earned the fourth by watching a
two-minute control leg overturn five passes of narrative.** 🟢 **`p795-G`: re-run a zero-returning
sweep on the finding that queued it.** 🔴 **`p796-G`: a control set must span the population's
KINDS.** 🔴 **`p797-A`: prefer a smaller DECLARED scope to a cleverer predicate.** 🆕 🟢 **`p798-G`:
when a finding is a RATE, measure that rate somewhere it should NOT hold — it is the cheapest of
the four and it is the one that would have caught `T931` before it shipped.**
