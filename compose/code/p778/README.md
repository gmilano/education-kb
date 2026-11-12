---
industry: education
region: Global
updated: 2026-11-12
---

# `p778` instruments — specified in prose, per `T763`

🔴 **`make hooks` was tried as the FIRST command of this pass and DENIED — `[Code from External]`. NINTH consecutive session, `0` for `9`.** 🟢 **Not worked around.** No script held in this repository was copied out and executed. Every instrument below was **written from scratch this pass** and is specified here in prose so the next pass can rebuild it without running anything.

## 1. The ref/raw prober

Resolves a repository's default branch and `HEAD` **without** `api.github.com/repos/*`, which is `403` for this session (re-measured this pass).

- **ref channel:** `GET https://github.com/{owner}/{repo}.git/info/refs?service=git-upload-pack`. The git smart-HTTP advertisement carries the capability string `symref=HEAD:refs/heads/<branch>`; parse the branch out of it, then take the `40`-hex sha advertised against `refs/heads/<that branch>`. 🔵 **This is why the prober finds default branches that are not `main`/`master`** — it reads the advertised symref rather than guessing. It found `elgg/elgg` on `7.x`, `learnosity/learnosity-qti` on `develop`, `opencast/opencast` on `develop` and `openeducat/openeducat_erp` on `19.0` this pass.
- **raw channel:** `GET https://raw.githubusercontent.com/{owner}/{repo}/{sha}/{name}` over **`56` case-aware candidate names** — the cross product of `LICENSE`, `LICENCE`, `COPYING`, `LICENSE-MIT`, `MIT-LICENSE`, `NOTICE`, `COPYRIGHT` with the suffixes `""`, `.md`, `.txt`, `.rst`, each in as-written and lower-case form. First `200` with a non-empty body wins.
- **Grade recorded:** `branch · HEAD[:12]`, grant filename, exact byte length, and `sha256[:12]` of the grant bytes. A candidate that exhausts all `56` names is `NO-GRANT-AT-ROOT` (**not** "no licence" — the grant may live below the root). A `401`/non-`200` on the ref channel is `ABSENT-OR-PRIVATE` and, per `T779`, is **not evidence about the organisation**.

### Control, run BEFORE any verdict was published
Four rows `p777` published were re-derived from scratch and reproduced **byte-for-byte** — branch, `HEAD`, filename, byte count and digest all identical: `claim-additional-payments-for-teaching` (MIT `1,099 B` · `7d38b1b17881`), `apply-for-teacher-training` (`1,094 B` · `1018ba112e86`), `teaching-vacancies` (`1,092 B` · `c561ea849ed6`), and `check-free-school-meals-eligibility-parent` (`NO-GRANT-AT-ROOT`). 🟢 `frappe/education`'s `19 B` pointer also reproduced (`1fcecf395312`). **Five independent reproductions, zero contradictions.**

## 2. The claim channel

`gh api -X GET search/repositories -f q='<query>'`, which **works** for public repositories in this session while `gh api repos/<slug>` does not. Fields taken: `license.spdx_id`, `stargazers_count`, `pushed_at`, `created_at`, `archived`, `fork`, `language`, `description`.

🔴 **Standing contract (`T799`), obeyed this pass: the claim channel may NEVER override a body grade.** A disagreement is a row to **re-read on the bytes**, never a row to rewrite. All `5` disagreements this pass were re-read on their own bytes before anything was published about them.

🟢 **Owner-batched enumeration, the efficiency fix this pass added.** A per-slug query costs one call per repository; `q='user:<owner>'` returns up to `100` of that owner's repositories in **one** call. Sweeping the `152` owners that hold `≥3` shelved repositories captured **`8,507`** repository rows for `152` calls instead of thousands. 🔵 This is what made `p777-B` affordable at all.

## 3. `gate-headings` — the gate `p777-A` named

Pure local computation, no network. For each of the `9` curated shelves, read every line that begins `## `. A **structural LIVE-marker** heading (the known instance is `## Opportunities by region`) must appear **exactly once in bare form**; every superseded copy must be qualified, by convention with `— \`pNNN\` (historical section; the live one is at the top of this file)`. Verdicts: `OK` (exactly one bare), `DEFECT-ZERO-BARE`, `DEFECT-n-BARE`.

🟢 **Result: `0` defects.** `intel/market.md` carried exactly `1` bare copy and `7` qualified ones. `p777`'s correction held, and this gate is now what keeps it holding.

## 4. `gate-claims-table` — `p776-E`'s fix, implemented and measured

Table-aware rather than line-aware, which is what `p776-E` asked for: a markdown table row is parsed into **cells**, a row is **one unit**, and a licence identifier is attributed to a repository only when both appear in the **same row of the same table**. Table boundaries are detected on the `|---|---|` separator line, so two adjacent tables are never merged.

Two variants were run, and both numbers are reported rather than only the flattering one:

- **same-row:** `42,175` table row units scanned, `4,280` distinct slugs carrying an in-row licence claim, **`526`** in-row contradictions.
- **strict, single-slug rows only:** `13,815` single-slug rows and `472` multi-slug rows; `4,135` slugs; **`376`** contradictions.

🔵 The decomposition of the `376`, and the decision it forced, are on [`intel/open-gaps.md`](../../intel/open-gaps.md) under `ACTION p777-E`.

## 5. URL verification, and a channel trap recorded for the next pass

🔵 All `38` distinct `github.com/<owner>/<repo>` addresses introduced by `p778` were verified before commit.

🔴 **Trap: `curl -sI https://github.com/<owner>/<repo>` returns `403` for EVERY repository in this session** — including `postgis/postgis` and `moodle/moodle`, which unquestionably exist. **This is the agent proxy refusing HTML `HEAD` requests to `github.com`; it is NOT a `404` and it is NOT evidence that an address is dead.** A pass that verifies URLs this way will conclude its entire supply is broken.

🟢 **Verify on the ref channel instead:** `curl -o /dev/null -w "%{http_code}" "https://github.com/<owner>/<repo>.git/info/refs?service=git-upload-pack"`. **Result this pass: `38`/`38` return `200`, `0` fail.** 🔵 The claim channel (`search/repositories`) is the second independent confirmation, and every row published this pass resolved on at least one of the two.

## 6. The header-as-data gate

🔵 A standing quality rule in this base is that a table header row must never be ingested as an entity. Two checks were run over all `9` shelves:

- **Header-shaped first cell without a following `|---|` separator:** `43` instances, **all in pre-existing history and `0` in `p778`'s own sections.** 🟢 Read in context these are **transposed label:value tables** (`| Licence | 🟢 **MIT** |`) — a legitimate two-column format, not a defect. Recorded rather than "fixed", because rewriting them would damage correct rows (`T788`).
- **Rows in which EVERY cell is a header word** — the actual failure mode, where a row like `| Nombre | Repo | Licencia |` compiles to an entity named *"nombre"*: 🟢 **`0` across all `9` shelves.**
