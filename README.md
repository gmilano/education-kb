---
industry: education
region: Global
updated: 2026-11-12
---

# Globant AI Studios — Education KB

**Pass `p787` · `2026-11-12`** — a full rewrite of the six curated files, with the two trending
ledgers and the action ledger appended to (never rewritten).

## What this pass established

| | |
|---|---|
| 🟢 Agents listed with a **byte-verified** grant | **23** — `22` permissive (MIT/Apache-2.0), `1` copyleft flagged |
| 🟢 Foundational repos with a **byte-verified** grant | **35** — 🟢 `15` permissive · 🔴 `18` copyleft · 🟡 `2` EUPL-1.2 |
| 🟢 Regions placed, with supply **and** regulation | **`5` of `5`** — North America, EMEA, APAC, LATAM, Global |
| 🟢 Controls reproduced before any verdict shipped | 🟢 **`4` of `4` exact** · `2` planted negatives DEAD as designed |
| 🔴 Defects found in **this pass's own probe**, fixed before use | **`3`** — `2` previously unrecorded (`T848`, `T849`) |
| 🔴 Probed and rejected | **`3`** agents (1 ungranted, 1 fork, 1 dead address) + `8` repos still grant-less or bespoke |
| 🟢 Dead addresses repaired to live canonical owners | **`4`** |

## 🟢 The three findings worth reading first

**1. In education, the famous platforms are copyleft and the permissive layer is narrow.**
Moodle (GPL-3.0), Open edX · Canvas · Frappe LMS (AGPL-3.0), H5P, ERPNext, Gibbon, Mahara, Anki —
all copyleft. The repos Globant can link into client code are a different, smaller set: **Kolibri
(MIT), Oppia (Apache-2.0), Sakai (ECL-2.0), OpenOLAT (Apache-2.0), Opencast (ECL-2.0), Tsugi
(Apache-2.0), Perseus (MIT), OATutor (MIT), nbgrader/JupyterHub (BSD-3), DSpace (BSD-3).**
🟢 **`csev/tsugi` (Apache-2.0) is the most useful licensing component in the sector** — LTI across a
process boundary lets permissive code serve a copyleft LMS without becoming a derivative work of it.
→ [`repos/foundations.md`](repos/foundations.md), [`verticals/solutions.md`](verticals/solutions.md)

**2. The sector's two leading agents are both permissive, and both APAC-origin.**
`HKUDS/DeepTutor` (Apache-2.0, `58.5k★`, HKU) and `THU-MAIC/OpenMAIC` (MIT, `43.4k★`, Tsinghua).
🟢 So the state of the art needs no licensing negotiation. 🔴 But capability sits in **APAC** while
regulation sits in **EMEA** and **North America** — engagements in the regulated regions will largely
consist of wrapping APAC-origin agents in regional governance.
→ [`agents/top.md`](agents/top.md), [`intel/trends.md`](intel/trends.md) `T850`

**3. Assessment is the regulated surface in every jurisdiction that regulates at all**, and one
architecture satisfies all of them: **AI proposes, a named human decides, the system proves it.**
EU Annex III (grading, admissions, proctoring) · Vietnam (automated assessment) · Oklahoma (AI used
*solely* for grading, discipline or promotion) · New York A 9190 · India's provenance rules.
→ [`compose/patterns.md`](compose/patterns.md) `P787-1`, [`intel/trends.md`](intel/trends.md) `T854`

## Regional summary

| Region | The opening | The named gap |
|---|---|---|
| **North America** | Regulated grading, **live now** — NC model policy due `2026-12-31`, Ohio in force, Oklahoma's "solely" clause; US DoE prioritised AI education grants `2026-04-13` | 🔴 Tracker counts disagree (`134`/`31` vs `68`/`27`) — **cite the instrument, never the count** |
| **EMEA** | The compliance deadline: Annex III high-risk for education moved to **`2027-12-02`** by Regulation (EU) 2026/1744 — 13 months of runway, with Art. 5's emotion-recognition ban **already in force** | 🔴 **No European-origin open-source education agent found.** Europe built the substrate (OpenEuroLLM, SOOFI, GPT-NL, Apertus) and not the education layer |
| **APAC** | Strongest permissive agent supply anywhere; weakest binding regulation. Vietnam is the one hard hook (education high-risk, citing automated assessment) | 🔴 Every APAC agent verified here is China/HK-origin — **no Japan, Korea or India permissive agent layer** |
| **LATAM** | Teachers **out-adopt the OECD by ~20 points** (BR `56%`, CL `55%` vs OECD `36%`) while `87%` of universities use AI, `26%` have a strategy, `9%` evaluate it | 🔴 **No AI-in-education statute found for Brazil, Mexico or Chile** — soft governance only, so there is no deadline to sell against |
| **Global** | Assessment architecture ports across all four regions | 🔴 The platform layer's copyleft forces the same architectural decision in every engagement |

## Files

| File | What it holds | Mode |
|---|---|---|
| [`agents/top.md`](agents/top.md) | `22` education agents, grant read from the bytes | rewritten each pass |
| [`agents/trending.md`](agents/trending.md) | What is new per window · **`370` dated sections** | 🟢 **append-only** |
| [`repos/foundations.md`](repos/foundations.md) | `35` foundational repos, permissive/copyleft split | rewritten each pass |
| [`repos/trending.md`](repos/trending.md) | Repo movement per window · **`370` dated sections** | 🟢 **append-only** |
| [`verticals/solutions.md`](verticals/solutions.md) | LMS, SIS, assessment and interop platforms to build on | rewritten each pass |
| [`intel/market.md`](intel/market.md) | Market range and **Opportunities by region** (`5` subsections) | rewritten each pass |
| [`intel/trends.md`](intel/trends.md) | `T850`–`T859` | rewritten each pass |
| [`compose/patterns.md`](compose/patterns.md) | `P787-1`–`P787-7`, concrete recipes | rewritten each pass |
| [`intel/open-gaps.md`](intel/open-gaps.md) | Action ledger · `p786` disposition + `p788` queue | 🟢 **append-only** |
| `archive/2026-11-12-p787-pre-rewrite/` | Prior versions of every rewritten file | — |

## 🔴 Channel discipline — read before quoting anything here

| Claim type | Status |
|---|---|
| Repository existence, `HEAD` sha | 🟢 **Byte-verified** — `git ls-remote`, exit status read **directly**, never through a pipe |
| Licence grant | 🟢 **Byte-verified** — served `LICENSE` bytes graded by **clause presence**, in `4` languages |
| Star counts | 🟡 **Page-channel** reads of github.com, rounded exactly as GitHub renders them |
| Every market, adoption and regulatory figure | 🔴 **Search-channel testimony.** `eur-lex.europa.eu`, `oecd.org`, `unesco.org`, `arxiv.org`, `wikipedia.org` and `gov.za` are **not byte-reachable** from this session (`T844`) |

🔴 **Five recorded ways to misread a licence, every one found by a control on a row this base had
already published** — case-blindness (`T842`), title-line insufficiency (`T847`), length-as-integrity
(`T845`), **language-blindness (`T848`, new)**, **appendix contamination (`T849`, new)**. 🟢 The gate
that closes all five is [`compose/patterns.md`](compose/patterns.md) → `P787-7`, and `p787` made it
the **probe** rather than the record — discharging `ACTION p786-A`.

🔵 **Both new failure modes are biased in a direction that matters commercially:** language-blindness
under-reports **LATAM**, and appendix contamination mis-grades **the EU's own licence**. A probe
written in English against American licence conventions will quietly under-report exactly the two
regions this base is told to serve.
