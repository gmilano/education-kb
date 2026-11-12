---
industry: education
region: Global
updated: 2026-11-12
---

# Globant AI Studios — Education KB

**Pass `p794` · `2026-11-12`** — `170` repository addresses measured on **three independent channels**, the
licence record cross-checked against GitHub's own classifier, and **the three regional gaps this base had
carried for several passes all closed**. 🔴 The two most valuable findings were not on the queue: a licence
rider on a `★158,480` row this base green-flagged, and three recommended repositories that are **archived
upstream** — a dimension this base had no field for. The two trending ledgers and the action ledger are
appended to, never rewritten.

## What this pass established

| | |
|---|---|
| 🟢 Addresses measured on all three instruments | **`170`** · 🟢 **`0` clone failures**, `170` blobless clones in **`22` seconds** |
| 🟢 Existence re-graded three-state (`p793-A`) | **`168` LIVE · `2` EMPTY · `0` ABSENT** — 🟢 **`0` corrections** |
| 🔴 **Recommended rows found ARCHIVED upstream** | 🔴 **`3`** — and the word *archived* appeared **`0` times** in this base (`T901`) |
| 🟢 Licence grades agreeing with GitHub's SPDX classifier | 🟢 **`118` of `118`** · `0` disagreements |
| 🟢 Rows where the **bytes** beat GitHub's `NOASSERTION` | 🟢 **`23`** |
| 🔴 **Licence grades CORRECTED** | 🔴 **`1`** — `open-webui/open-webui` (`T900`) |
| 🟢 Star counts re-measured **exactly** — the carried-forward limitation is lifted | 🟢 **`164` of `170`** |
| 🟢 Queued actions discharged | 🟢 **`6` of `7`** · `1` named as a scope limit |
| 🔴 Defects in **this pass's own instruments**, all caught before publication | 🔴 **`5`** — `4` of them the same mistake |

## 🟢 The three findings worth reading first

**1. A row this base recommends as a client delivery surface cannot carry the client's name.**
[`open-webui/open-webui`](https://github.com/open-webui/open-webui) (`★158,480`) is published here twice as
🟢 `BSD-3-Clause`. 🔴 **Canonical BSD-3-Clause has three numbered clauses; the served `LICENSE` has four**, and
clause `4` makes altering, removing or replacing *"Open WebUI" branding* a **material breach**. 🔴 **So it
cannot be delivered white-labelled** — the one thing a delivery surface is for. 🔵 The trap is three files
deep: the repository also ships `LICENSE_HISTORY`, which grades as **clean** BSD-3-Clause. 🟢 **GitHub's
`NOASSERTION` was more honest than this base's hand grade — the one row in `141` where that is true.**
🔵 `T900` is the **seventh** recorded way to misread a licence here and the first that is **additive**: the
family matches perfectly and something has been appended to it. 🟢 **Match the family, then count the clauses.**
→ [`intel/trends.md`](intel/trends.md) `T900`, [`verticals/solutions.md`](verticals/solutions.md)

**2. `ARCHIVED` is an existence state no instrument here has ever read, and three recommendations are in it.**
🟢 `p793` replaced exit-status grading with LIVE · EMPTY · ABSENT, and `p794` reproduced that across `170`
addresses with **`0` corrections**. 🔴 **It is still not enough: an archived repository returns `rc=0` with refs
and a valid `HEAD`** — identical to a healthy one. 🔴 **[`MaharaProject/mahara`](https://github.com/MaharaProject/mahara)**
(the ePortfolio recommendation, last push **`2023-11-16`**), 🔴 **[`MyScript/MyScriptJS`](https://github.com/MyScript/MyScriptJS)**
(the maths-input primitive, **"Rescued"** at `p786`, last push **`2021-01-04`**) and
🟡 **[`european-commission-empl/European-Learning-Model`](https://github.com/european-commission-empl/European-Learning-Model)**
(the EMEA credential vocabulary, **`2024-02-14`**). 🔵 Two lessons sharper than the finding: 🔴 **resolving
canonicity is not resolving maintenance** — this base correctly moved `mahara/mahara` → `MaharaProject/mahara`
and the canonical address is the archived one; and 🔴 **a licence rescue is not a viability rescue.**
🟢 **Existence needs four states, and `archived` is free in the call that returns the star count.**
→ [`intel/trends.md`](intel/trends.md) `T901`

**3. The strongest trial ever run on an AI tutor says the scarce component is not the tutor.**
A two-year cluster-randomised trial of Khanmigo across `18` Tennessee middle schools: 🟢 **`96%` of assigned
students used it**, 🔴 **the median student messaged it on about `⅓` of practice days**, and the two-year
intent-to-treat effect was **`≈0.06` SD** (Year 1 alone: 🔴 **`0.020` SD, indistinguishable from zero**) against
`0.2`–`0.4` SD for high-dosage human tutoring. 🟢 **Khan Academy's own 2026 fix was to stop waiting to be
invoked and auto-activate during practice.** 🔵 **That is a scheduling failure, not a capability failure, and no
model upgrade repairs it.** 🟢 Corroborated from two directions: the deployment literature finds effects only
where the role is *narrow and educator-controlled*, and a `474`-study scoping review finds pedagogical design
still poorly connected to technical capability. 🟢 **Thirteen passes of this base have ranked tutors; `P794-1`
ranks the trigger instead.**
→ [`intel/trends.md`](intel/trends.md) `T907`, [`compose/patterns.md`](compose/patterns.md) `P794-1`

## Regional summary

| Region | The opening | The named gap |
|---|---|---|
| **North America** | 🟢 **`p793-E` DISCHARGED — Canada and Mexico placed for the first time.** 🇨🇦 Ontario has made **"Cyber Safety and Artificial Intelligence" a mandatory `2026-27` Professional Activity topic** pointing at the Ontario Trustworthy AI Framework, with 🔴 **no province-wide policy memorandum** — so the buyer is the board, and there are `72` of them. 🇲🇽 **SEP has told every university to write its own AI guidelines and `~8` in `10` of their students cannot find them.** 🇺🇸 The calendar still leads: **NC model policy `2026-12-31`**, Ohio passed, local policies `2027-06-30` | 🔴 **No spend figure for Canada or Mexico** — both placements are policy and adoption, not budget. 🔴 And the Ontario board-policy percentage rests on a secondary source |
| **EMEA** | 🟢 **`p793-F` DISCHARGED and overshot. `63%` of European teachers use AI and `16%` believe general-purpose AI improves learning outcomes** (Sanoma Learning 2026, `>20,000` teachers, `14` countries). 🔵 **A `47`-point gap between use and believed benefit is the whole commercial thesis** — this market has tried the generic tool and rejected it. Plus **`52%`** asking for guidelines, 🔴 **`10` of `23` ministries with any GenAI position**, and the obligations that are **not** deferred: Art. 5 live, **Art. 50 since `2026-08-02`**, **Art. 27 FRIA now** | 🔴 **Spend is still unanswerable** — `2026` European estimates span `$2.11B`–`$5.86B`, a **`2.8×`** spread. 🔴 Still **no European-origin open-source education agent** at scale: `p794` adds the first in several passes, [`tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) 🇫🇷, 🟡 **but `★102` is a seed, not a sector** |
| **APAC** | 🟢 **`p793-D` DISCHARGED for India and Singapore.** 🇮🇳 **NCERT with CBSE has introduced a Computational Thinking + AI curriculum for Classes `III`–`VIII` from `2026-27`**, Grade `9`–`12` finalised, governance named down to the committee chair. 🇸🇬 **MOE built its own tools inside SLS and its Minister said in February 2026 that it lacks outcome data** — 🟢 **a ministry asking for evaluation, not another tutor.** 🇦🇺 Product expectations and an RAI standard are **both in pilot right now**. 🇨🇳 carried: 教科信〔2026〕1号, provincial procurement | 🔴 **`0` procurement documents reached for India, Singapore or Australia.** Curriculum, ministry statements and standards-in-pilot were reached; **tenders were not** — GeBIZ and state tender portals are the named channel |
| **LATAM** | 🟢 **The adoption lead now has a primary-ish instrument** — IADB **Nota CIMA `37`** from TALIS 2024: 🇧🇷 `56%` · 🇨🇱 `55%` · 🇨🇴 `53%` · 🇨🇷 `52%`, with AI training the **first**-ranked PD need in Chile and Costa Rica. 🟢 **And the region's reference deployment is found: PUC Chile runs `194` pedagogical agents across ~`100` courses.** 🟢 New and funded: 🇨🇱 **"Futuros Docentes en IA"** (March 2026, Ministerio de Ciencia + CRUCH + UMCE + CENIA + Kodea) | 🔴 **No AI-in-education statute in Brazil, Mexico or Chile — no deadline to sell against**, so the sale must be made on evidence. 🔴 **And PUC Chile's own stated gap is outcome measurement.** 🟢 With `9%` evaluation coverage region-wide, **evidence instrumentation is still the clearest unclaimed offer, and now it has a `194`-agent proof of demand** |
| **Global** | 🟢 **Three independent sources now converge on one architecture:** regulators require a named human decision-maker, the best RCT shows the limit is engagement under teacher control, and the deployment literature finds effects only where scope is narrow and educator-controlled. 🟢 **AI proposes, a named human decides, the system proves it** — the evidence pack ports by re-labelling, not re-engineering | 🔴 The platform layer is copyleft while the agent layer is permissive and mostly APAC-origin — the same architectural decision in every engagement. 🔴 And **no independent security or data-governance evaluation of any education MCP server has been published** (`p792-D`, still unclaimed) |

## Files

| File | What it holds | Mode |
|---|---|---|
| [`agents/top.md`](agents/top.md) | `126` addresses, `4` added this pass, stars re-measured | rewritten each pass |
| [`agents/trending.md`](agents/trending.md) | What is new per window · **`935` sections across `54` distinct dates** (measured) | 🟢 **append-only** |
| [`repos/foundations.md`](repos/foundations.md) | Foundational repos, permissive/copyleft split, 🔴 **archived rows now labelled** | rewritten each pass |
| [`repos/trending.md`](repos/trending.md) | Repo movement per window · **`933` sections across `47` distinct dates** (measured) | 🟢 **append-only** |
| [`verticals/solutions.md`](verticals/solutions.md) | LMS, SIS, assessment and interop platforms to build on | rewritten each pass |
| [`intel/market.md`](intel/market.md) | Market range and **Opportunities by region** (`5` subsections) | rewritten each pass |
| [`intel/trends.md`](intel/trends.md) | `T900`–`T907` | rewritten each pass |
| [`compose/patterns.md`](compose/patterns.md) | `P794-1`–`P794-4`, one per region | rewritten each pass |
| [`intel/open-gaps.md`](intel/open-gaps.md) | Action ledger · `p793` disposition + `p795` queue | 🟢 **append-only** |
| `evidence/*2026-11-12-p794*` | The five machine outputs behind this pass | — |
| `archive/2026-11-12-p794-pre-rewrite/` | Prior versions of every rewritten file | — |

🔴 **One carried figure removed rather than reproduced:** the previous README reported **`371` dated sections** in each trending ledger. 🔴 **That number does not reproduce under any heading pattern** — the ledgers hold `935` and `933` `##` sections across `54` and `47` distinct dates. 🔵 Same class as `T905`: a published count nobody could re-derive. 🟢 Replaced with measured values.

## 🔴 Channel discipline — read before quoting anything here

| Claim type | Status |
|---|---|
| Repository existence | 🟢 **Byte-verified three-state** (`rc` + ref count), `170` of `170`. 🔴 **But three states are not enough — `ARCHIVED` reads as healthy** (`T901`) |
| Repository **maintenance** | 🔴 **NEW and mostly unmeasured.** `archived` and `pushed_at` were read for `164` rows this pass; `3` archived rows found. 🔵 Treat any row without a last-push date as unassessed |
| Licence grant | 🟢 **Byte-verified**, graded by clause presence on the served bytes, 🟢 **cross-checked against GitHub's SPDX classifier: `118/118`**. 🔴 **But check for riders** — family matching cannot see what is appended (`T900`) |
| Licence **restrictions** | 🔴 **The direction instruments fail in.** NonCommercial in Spanish and a branding rider in English both returned a *more usable* answer than the truth (`T902`, `T900`). 🔵 Restriction vocabulary, in every language, before grant vocabulary |
| Dependency licences | 🟢 **Byte-verified at the PINNED VERSION** where measured — 🔴 **but only `3` rows have been; every other `Deps` cell is a claim about a version nobody identified** (`p794-C`) |
| Byte sizes | 🟢 **Reproducible — `8` of `8` exact across two independent passes** |
| 🔴 **`sha=` values** | 🔴 **NOT reproducible and not one hash function.** The column mixes git blob sha1, `sha256` and values matching neither; one `19`-byte file carries **three** published hashes (`T905`). 🔵 **Treat every carried `sha=` as unverified.** `p794`'s are `git rev-parse HEAD:<path>`, truncated to `12` |
| Star counts | 🟢 **Re-measured exactly, `164` of `170`** — `gh api search/repositories` takes `10` × `repo:` per call. 🔴 **`6` addresses are absent from the search index and all `6` clone and serve refs** (`T903`) — a search index is a view, not a census |
| Publishing | 🟢 **Works.** This repository must be **attached to the session's authorised set** before a push; the proxy otherwise declines to inject a credential. The attachment is **per-session**, so a future pass seeing `403` should attach, not record "blocked" |
| Every market, adoption and regulatory figure | 🔴 **Search-channel testimony.** 🟢 **And now diagnosed:** `eur-lex`, `oecd.org`, `unesco.org`, `op.europa.eu`, `ec.europa.eu`, `pib.gov.in`, `moe.gov.sg`, `ontario.ca` and `edresearch.edu.au` are refused with a **gateway `403` at `CONNECT` — a network-POLICY denial, not an unreachable site** (`T906`). 🔵 Positive controls passed in the same minute. **A human can fix this in one place → `p794-F`** |

🔴 **Seven recorded ways to misread a licence, every one found by a control on a row this base had already
published** — case-blindness (`T842`), title-line insufficiency (`T847`), length-as-integrity (`T845`),
language-blindness (`T848`), appendix contamination (`T849`), affero-substring (`T894`) and
🆕 **additive riders (`T900`)**.

🔵 **`4` of this pass's `5` self-caught defects were one mistake: grading on a proxy — a filename, a clause
set, a family, an English token — instead of reading the thing itself.** 🟢 **And the instrument that caught
most of them was this base's own published record, which disagreed with my probe and was right every time.**
🔴 `p794` adds the companion caution to `p793-G`: **check which direction your instrument errs in, and never
let it err toward "usable"** (`p794-G`).
