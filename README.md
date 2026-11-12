---
industry: education
region: Global
updated: 2026-11-12
---

# Globant AI Studios — Education KB

**Pass `p793` · `2026-11-12`** — the whole agent list re-measured on an **independent instrument**, two
published existence verdicts corrected, and the dependency claim that carries this base's main
commercial argument resolved on both of its lockfiles. The two trending ledgers and the action ledger
are appended to, never rewritten.

## What this pass established

| | |
|---|---|
| 🟢 Repository addresses re-measured, with path + **byte size + blob sha** | **`103`** root grants of **`122`** addresses swept — in **`10.9` seconds** |
| 🟢 **Licence grades this sweep found wrong** | 🟢 **`0` of `122`** |
| 🔴 **Existence verdicts corrected** | **`2`** — "DEAD" → **ALIVE, EMPTY, owner-claimed** (`T892`) |
| 🟢 Dependency claims resolved at pinned versions | **`240`** — `32` Python pins + **`208`** npm runtime packages across `40` workspace importers |
| 🔴 Ungranted **shipped** packages found inside a platform this base recommends | **`1`** (`T896`) |
| 🟢 Controls reproduced before any verdict shipped | 🟢 **`4` of `4` exact** · `1` planted negative DEAD as designed |
| 🔴 Defects in **this pass's own instruments**, all caught before publication | **`5`** — `4` of them the same mistake |
| 🟢 Queued actions discharged or substantially advanced | **`5` of `7`** · `1` carried · `1` named as a scope limit |

## 🟢 The three findings worth reading first

**1. This base's most fundamental instrument answers the wrong question.**
Existence is graded by `git ls-remote`'s exit status. 🔴 **An address that exists and holds no refs at
all returns `rc=0`** — indistinguishable from a healthy repository. `Bestisco/My-WASSCE-Companion` and
`Elite2828/ACE-AI-Tutor`, both published here as **DEAD**, clone successfully, hold **zero refs** and
have no `HEAD`: they exist, are owner-claimed and were never pushed. 🟢 **Existence needs three
states, not two — LIVE (`rc=0` ∧ `refs ≥ 1`) · EMPTY (`rc=0` ∧ `refs = 0`) · ABSENT (`rc=128`).**
🔵 And the corrected answer is commercially *better*: an empty repository is a named author who
claimed a name and has not shipped — a reachable prospect, not a dead end.
→ [`intel/trends.md`](intel/trends.md) `T892`, [`agents/top.md`](agents/top.md)

**2. The licence record survived an independent re-measurement — `0` corrections in `122` rows.**
The sweep was built on a different channel from the one that produced the rows (blobless tree
enumeration + root-only grant selection + `raw` bytes), so agreement means something. 🟢 It reproduced
every published grade it cross-checked, including a **Spanish-language MIT** and the **GPL-3.0 /
AGPL-3.0 split**. 🔴 **And it found the sixth way to misread a licence: GPL-3.0's §13 is titled "Use
with the GNU Affero General Public License", so a grep for *affero* grades every GPL-3.0 repository
as AGPL-3.0.** The discriminator is exact — `35,149 B` + `affero`×`3` = GPL-3.0; `34,523 B` +
`affero`×`15` = AGPL-3.0.
→ [`agents/top.md`](agents/top.md), [`intel/trends.md`](intel/trends.md) `T894`, `T899`

**3. `kolibri`'s dependency claim is exact, and the half nobody had measured is clean.**
"2 LGPL of 32" is **confirmed** — the `32` is the `==`-pinned Python `base` group in `pyproject.toml`
(🔴 `requirements.txt` is a decoy that says so in its own first line). 🔴 **The npm side had never been
measured**, because the root `package.json` declares `0` runtime dependencies: `kolibri` is a pnpm
workspace of **`40` importers**. Resolved at locked versions → **`208`** runtime packages, 🟢 **`0`
GPL-family**, `1` MPL-2.0, `1` dual, and 🔴 **`1` that ships with no grant on any channel —
`@khanacademy/mathjax-renderer@3.0.2`, whose `336,573 B` tarball contains no licence file and whose
upstream address no longer resolves.** 🔵 **Residual risk is one plugin:** both problem packages are
declared by `perseus_viewer`, the exercise renderer. Core is clean.
→ [`repos/foundations.md`](repos/foundations.md), [`intel/trends.md`](intel/trends.md) `T895`, `T896`

## Regional summary

| Region | The opening | The named gap |
|---|---|---|
| **North America** | The most concrete calendar anywhere: 🔴 **NC model policy due `2026-12-31`** (local policies `2027-06-30`, training `2028-06-30`), Ohio's deadline already passed, Idaho `2027-28`, Oklahoma's *"solely"* clause, Florida's instructor-permission rule | 🔴 **Three passes running, the channel returns US-only material. Nothing for Canada or Mexico** — very likely a query artefact, the same diagnosis `T883` proved for EMEA |
| **EMEA** | 🔴 **The obligations that are NOT deferred**: Art. 5 emotion-recognition ban live, **Art. 50 transparency in force since `2026-08-02`**, **Art. 27 FRIA required now**; Annex III high-risk `2027-12-02`, embedded products `2028-08-02`. 🟢 **Sell the FRIA first** | 🔴 **No European-origin open-source education agent** across several passes — *and* 🔴 **not one European adoption or spend figure.** The most regulation-dense, evidence-thinnest region |
| **APAC** | 🟢 **China placed at ministry level with a document number:** 《"人工智能+教育"行动计划》 **教科信〔2026〕1号**, five ministries, signed `2026-04-02` — local curriculum systems with class-hour requirements (🟢 **procurement is provincial**), rural delivery, and 🔴 **security-assessment indicators in draft**. Plus Korea's AI Basic Act (`2026-01-22`) and Vietnam's `2027-09-01` | 🔴 **India, Australia and Singapore still unplaced at education-ministry level** — what was reached is national AI regulation, not procurement |
| **LATAM** | 🟢 **The adoption lead is a four-country pattern now**: 🇧🇷 `56%` · 🇨🇱 `55%` · 🇨🇴 `53%` · 🇨🇷 `52%` of teachers vs OECD `36%`; **`~9 in 10`** 15-year-olds (PISA 2025). 🔵 Three funded programmes named, **all teacher-training, none a platform build** | 🔴 **No AI-in-education statute for Brazil, Mexico or Chile** — no deadline to sell against. 🟢 With `9%` evaluation coverage, **evidence instrumentation is the clearest unclaimed offer** |
| **Global** | 🟢 One architecture satisfies every jurisdiction that regulates: **AI proposes, a named human decides, the system proves it.** The evidence pack ports by re-labelling, not re-engineering | 🔴 The platform layer is copyleft while the agent layer is permissive and mostly APAC-origin — the same architectural decision in every engagement |

## Files

| File | What it holds | Mode |
|---|---|---|
| [`agents/top.md`](agents/top.md) | `122` addresses, `103` with a sized and sha'd root grant | rewritten each pass |
| [`agents/trending.md`](agents/trending.md) | What is new per window · **`371` dated sections** | 🟢 **append-only** |
| [`repos/foundations.md`](repos/foundations.md) | Foundational repos, permissive/copyleft split, `Deps` now lockfile-resolved | rewritten each pass |
| [`repos/trending.md`](repos/trending.md) | Repo movement per window · **`371` dated sections** | 🟢 **append-only** |
| [`verticals/solutions.md`](verticals/solutions.md) | LMS, SIS, assessment and interop platforms to build on | rewritten each pass |
| [`intel/market.md`](intel/market.md) | Market range and **Opportunities by region** (`5` subsections) | rewritten each pass |
| [`intel/trends.md`](intel/trends.md) | `T892`–`T899` | rewritten each pass |
| [`compose/patterns.md`](compose/patterns.md) | `P793-1`–`P793-2`, concrete recipes | rewritten each pass |
| [`intel/open-gaps.md`](intel/open-gaps.md) | Action ledger · `p792` disposition + `p794` queue | 🟢 **append-only** |
| `evidence/*2026-11-12-p793*` | The three machine outputs behind this pass | — |
| `archive/2026-11-12-p793-pre-rewrite/` | Prior versions of every rewritten file | — |

## 🔴 Channel discipline — read before quoting anything here

| Claim type | Status |
|---|---|
| Repository existence | 🟢 **Byte-verified — and now by `rc` AND ref count** (`T892`). An exit status alone is not an answer |
| Licence grant | 🟢 **Byte-verified** — served licence bytes graded by **clause presence**, cross-checked by byte size |
| Dependency licences | 🟢 **Byte-verified at the PINNED VERSION** — `pnpm-lock` importers + per-version registry reads, `==` pins + per-version PyPI reads, and the **published tarball** when a field is blank |
| Star counts | 🔴 **One figure re-measured this pass** — `HKUDS/DeepTutor` `58,585★` (`gh api search/repositories`, exact). `github.com` and `api.github.com/repos/*` are **`403`**, so every other star count is **carried forward, not re-measured** |
| Publishing | 🟢 **Works — and the recurring `403` has a known fix.** This repository must be **attached to the session's authorised set** before a push; the proxy otherwise declines to inject a credential. The attachment is **per-session**, so a future pass seeing `403` should attach, not record "blocked" |
| Every market, adoption and regulatory figure | 🔴 **Search-channel testimony.** `eur-lex.europa.eu`, `oecd.org`, `unesco.org`, `arxiv.org` and `wikipedia.org` are **not byte-reachable** from this session (`T844`) |

🔴 **Six recorded ways to misread a licence, every one found by a control on a row this base had
already published** — case-blindness (`T842`), title-line insufficiency (`T847`),
length-as-integrity (`T845`), language-blindness (`T848`), appendix contamination (`T849`) and
🆕 **affero-substring (`T894`)**.

🔵 **`4` of this pass's `5` self-caught defects were one mistake: grading on a proxy — an exit code, an
English clause, a file name, a word — instead of reading the thing itself.** That is `p792-G`
generalised, and `p793` adds its companion: 🔴 **an instrument's silence is a property of the
instrument.** Three silences this pass looked like absence and were not — an English query that found
no education agent (they lead the sector), an English clause set that found no grant (it was in
Spanish), and a `requirements.txt` that found no dependencies (they were in `pyproject.toml`).
🟢 **Before recording an absence, name which instrument was silent and what it cannot see.**
