# p121 — stale tokens across pages, grant coverage, and the manifest/file diff

**Pass 121, 2026-10-11.** Discharges all four actions p120 pre-registered: **`N`, `O`, `P`, `Q`**.
`./test_p121.sh /tmp/education-kb` — **27 passed / 0 failed**, fully offline.

🔴 **Two of the four are REFUTED on their own clauses**, and both refuted figures were headline
numbers this KB published last pass.

## Verdicts

| action | clause | verdict | figure |
|---|---|---|---|
| `N` | probe the other 227 for tier-4/5 shapes; refuted if < 10 ungranted | 🔴 **REFUTED** | **4 / 227 = 1.8 %** (p120 implied 41 %) |
| `O` | word-boundary anchor the bare tokens; refuted if the claim count moves by < 3 | 🟢 **NOT REFUTED** | **3 402 → 3 349 = −53** |
| `P` | re-measure `was X` rows against OTHER pages; refuted if no second address carries a third value | 🟢 **NOT REFUTED** | `portabilis/i-educar`, **AGPL-3.0** vs truth GPL-2.0 vs named `was LGPL-3.0` |
| `Q` | diff manifest-declared licence against the committed file; refuted if < 15 % differ | 🔴 **REFUTED** | **10 / 104 = 9.6 %** (p120 measured 2/4 = 50 %) |

## Files

| file | what it is |
|---|---|
| `extract-noanchor.sh` | p120 v3 verbatim — the **control**, the sweep actually in use before this pass |
| `extract-v4.sh` | anchoring ALONE. 🔴 **Not recommended** — it drops 4 rows (`0BSD`, `LGPLv3`) |
| `extract-v5.sh` | anchor + widen. Recovers the 4 but adds a false `Apache 2.0` from a quoted ECL-2.0 preamble |
| `extract-v6.sh` | 🟢 **RECOMMENDED** — anchor + widen (minus the space spelling) + **fixed dedup guard** |
| `crosspage.py` | `ACTION P`. Pass a root; `all` as a 2nd arg widens the domain from the 35 corrected addresses to all 249 |
| `probe.sh` / `probe-n.sh` | live grant probe, 14 and 22 candidate paths, on the measured default branch |
| `fetch-manifests.sh` / `manifest_q.py` | `ACTION Q`. 249 addresses × 3 manifests, parallel; then the diff |
| `repair.py` / `repair2.py` | the 5 + 5 cells repaired, **structurally anchored**, idempotent |
| `verify.2026-10-11.tsv` | live re-read of all 8 `ACTION P` defect addresses |
| `action-{n,p,q}.tsv` | per-action results |
| `test_p121.sh` | 27 offline assertions |

🔵 **Transport, unchanged from `P117-A`:** `raw.githubusercontent.com` answers **200**;
`github.com` and `api.github.com` both **403** from this runner. Every measurement here is a raw
file read on the measured default branch.

## Own-instrument defects, recorded because they generalise

🔴 **1. Anchoring without widening moves the error, it does not remove it.** A word-boundary check
rejects `BSD` inside `0BSD` and `LGPL` inside `LGPLv3`, so v4 converted a *wrong token* into a
*missing row* — strictly worse. This is p118's `F5` one level up: the alternation cannot express
the spelling, and the guard then drops the row. 🟢 Anchor and widen together, never one alone.

🔴 **2. Every widening buys real rows and creates new false ones.** Adding `Apache 2.0` (space)
recovered exactly one row, and that row quotes the **ECL-2.0 preamble**: *"consists of the Apache
2.0 license, modified…"*. A licence name inside a quotation of another licence is not a claim.
🟢 Rejected; the suite asserts it stays rejected.

🔴 **3. The dedup guard could never fire.** `index(" " toks " ", " " t " ")` against a
**comma**-joined list matches only the first token. **49 surplus instances across 46 rows**, since
p118. 🟢 Delimiters must match the join character.

🔴 **4. A header-only correction guard misreads inline corrections as defects.** 6 of the first
run's 10 flagged rows were already correct, carrying `⚠️ **was 🟢 MIT**` *inside the cell* under an
ordinary header. 🟢 The guard now matches the inline marker too.

🔴 **5. Coarse truth manufactures contradictions.** p118 recorded some committed licences as the
bare family (`BSD`, `CC-BY`). A page or manifest naming `BSD-3-Clause` against a truth of `BSD` is
**more precise, not contradictory**. Unfixed this produced ~120 of 145 rows in the widened `ACTION
P` sweep and 8 of the first 20 `ACTION Q` contradictions. 🟢 Both scorers now treat a bare family
as a wildcard within it.

🔴 **6. A verdict naming a proprietary SUBDIRECTORY is not an ungranted repository.**
`"AGPL-3.0 (CE) + MIT (portions) + proprietary ee/"` grants two licences. Substring-matching
`PROPRIETARY` flagged 5 correct `PrairieLearn` rows. 🟢 A verdict is ungranted only if it names an
ungranted shape **and** names no licence.

🔴 **9. The guard needed widening for THIS pass's own tables, which is `P121-B` recurring
immediately.** The `ACTION Q` contradiction tables written this pass head their columns
`manifest says` / `committed file says`, and their rows disclose the defect in prose inside the
cell (*"no licence file — author claim only"*, *"README says only \"GPL\""*, *"`package.json`
declares MIT"*). The guard flagged **4 of this pass's own correct rows** on the first re-run.
🟢 Both vocabularies widened and a regression fixture added. 🔵 **The structural point: a census
that recognises corrections by VOCABULARY needs every future pass's vocabulary added to it. That
is a maintenance burden, not a fix** — `ACTION V` is pre-registered to replace the vocabulary
guard with an explicit machine-readable marker.

🔵 **7. `p120/score.py` hardcodes `/home/user/education-kb`** and is unrunnable from any other
checkout. 🟢 `crosspage.py` takes the root as a parameter.

🔵 **8. Reading every row before believing it changed both headlines.** `ACTION Q`'s first run said
**20 contradictions (19.2 %) — a PASS**; reading all 20 cut it to **10 (9.6 %) — a REFUTATION**.
`ACTION P`'s first run said 10 defects; reading all 10 cut it to 4. 🔴 **Had either number been
published from its first run, this pass would have reported a pass on a clause its own data
refutes.**

## Scope limits, stated

🔴 **`ACTION P`'s domain is TABLE ROWS and CORRECTED addresses.** Widening it to all 249 addresses
(`crosspage.py <root> all`) leaves **23 candidate rows across 14 addresses** after the coarse-truth
fix; **5 were verified live and repaired**, and the remaining 18 were read and found to be
correct disclosures (paper-claim rows, vendored sub-trees, rows more precise than the truth
table). 🔴 **Prose claims are outside every census this KB has built** — `ACTION R`.

## Pre-registered for p122, each with its refutation clause

🟢 **`ACTION R` — extend the census to PROSE licence claims.** 🔴 *Refuted if fewer than 3 prose
claims disagree with the tree.*

🟢 **`ACTION S` — test whether `Gap 402` is a QUERY defect**, re-running discovery with
edtech-specific nouns (`LMS`, `SIS`, `autograder`, `learning analytics`, `proctoring`,
`gradebook`). 🔴 *Refuted if that set also returns zero new addresses.*

🟢 **`ACTION T` — assert mechanically that `intel/open-gaps.md`, the root `README.md` pass log and
the newest instrument README name the same pass and the same open actions.** 🔴 *Refuted if the
three already agree.*

🟢 **`ACTION V` — replace the vocabulary-based correction guard with an explicit marker.**
Every pass so far has taught the guard new words (p120: headers; p121: inline markers, then its
own table headers). Emit a machine-readable token (e.g. a trailing `<!--corrected-->`) on every
repaired row instead. 🔴 *Refuted if fewer than 10 existing rows would need the marker
back-filled.*

🟢 **`ACTION U` — normalise slug case at every join**, then re-run p118's and p120's joins. 🔴
*Refuted if fewer than 2 addresses change verdict.*

🟡 **`ACTION C` and `ACTION D` — CARRIED FORWARD, clauses verbatim, now pending FOUR passes.**
Layer P (reverse-DNS package namespace) and layer D (the API `description` field). Neither has
been attempted since p117 pre-registered them; `P121-G` explains how they fell out of the record.
