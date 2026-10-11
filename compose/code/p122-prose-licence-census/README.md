# `p122-prose-licence-census` — ACTION R, S, T, U, and the carried C, D, V

**Pass 122 — 2026-10-11.** Ninth pass of this date (census window **07:3x → 08:4x UTC**).

`./test_p122.sh` — **50 passed / 0 failed**, fully offline, no network and no clock.

## What this instrument was asked to do

p121 pre-registered four actions and left two carried forward. A fifth, `ACTION V`, existed
**only in p121's own instrument README** — in neither the root `README.md` nor the ledger — which
is the drift `ACTION T` was pre-registered to detect. `ACTION T` found it on its first run.

| action | clause (verbatim from p121) | verdict |
|---|---|---|
| `ACTION R` | extend the licence census to **prose** claims. *Refuted if fewer than 3 prose licence claims across the live pages disagree with the tree* | 🟢 **DISCHARGED, NOT REFUTED — but only just: 3 verified claims, and all 3 are ONE address** |
| `ACTION S` | re-run discovery with edtech nouns. *Refuted if that set also returns zero genuinely new addresses* | 🟢 **DISCHARGED, NOT REFUTED — 3 genuinely new, verified** |
| `ACTION T` | assert mechanically that ledger, root README and newest instrument README name the same pass and the same open actions. *Refuted if all three already agree* | 🟢 **DISCHARGED, NOT REFUTED — they do not agree** |
| `ACTION U` | normalise slug case at every join. *Refuted if fewer than 2 addresses change verdict* | 🟢 **DISCHARGED, NOT REFUTED — 76 addresses were double-counted** |
| `ACTION C` | layer P, the reverse-DNS package namespace. *Refuted if it places fewer than 20* | 🔴 **DISCHARGED and REFUTED — 13 placements** |
| `ACTION D` | layer D, the API `description` field. *Requires placing ≥ 10; refuted otherwise* | 🔴 **DISCHARGED and REFUTED — 8 of 18** |
| `ACTION V` | replace the vocabulary correction guard with an explicit marker. *Refuted if fewer than 10 rows need back-filling* | 🟢 **MEASURED, NOT REFUTED — 57 rows, 1 marker exists** |

## 🔴 The pass's main result is about this instrument, not about the KB

`ACTION R` was built three times. Each build flagged defects; verification destroyed most of them.

| build | candidates | survived verification | false-positive rate |
|---|---|---|---|
| 1 — line-scoped, token anywhere on the line | 25 | 7 | 72 % |
| 2 — + correction guard, multi-token guard | 11 | 1 | 91 % |
| 3 — paragraph-unwrapped, proximity-attributed | 59 *(high-consequence subset)* | 3 | 95 % |

🔴 **The cause is the same every time, and it is structural: this KB records licences with
per-artifact precision, and any instrument that reduces a repository to ONE token is less precise
than the text it audits.** Verified examples of prose this census called wrong and which is right:

- `microsoft/autogen` — the page says *"MIT (`LICENSE-CODE`) · `LICENSE` is CC-BY-4.0 for docs"*.
  Both files exist and both readings are correct. A one-token scan reads `LICENSE` and reports MIT
  as a defect.
- `haolpku/K12-KGraph` — the page says *"MIT code / 🔴 CC BY-NC-SA data"*. Correct, and strictly
  more informative than either token alone.
- `qed42/ai-accessibility-checker` — the page says *"MIT badges over a 404"*. The scan read the
  404 and reported the badge as a false claim, which is what the sentence already said.
- `jcputney/scorm-again (354★)` — the `Apache-2.0` nearby belongs to `yetanalytics/lrsql`, the
  previous item in the same list. The page never claimed it.

🟢 **The reusable rule: before a census may report a defect rate, it must be scored against the
text it flagged, not only against the tree.** A census that has never been shown a correct row it
mishandled has not been calibrated, and its rate is a property of the instrument.

## 🟢 The one real defect, and why it is the worst kind

`P122-A` — [`FWU-DE/ais-chat`](https://github.com/FWU-DE/ais-chat) is **AGPL-3.0**
(`main/LICENSE`, 34 523 B, AGPL title line; no second licence file; confirmed independently on
the rendered page). This KB says AGPL-3.0 in **47** cells — and still carried a permissive claim
in **3** places, all repaired this pass:

| where | what it said | why it matters |
|---|---|---|
| `compose/patterns.md` prose | *"MIT, so a closed derivative is permitted"* | 🔴 **two lines under a table in the same section reading 🔴 AGPL-3.0.** The sentence tells a studio the exact opposite of the truth, inside a buildable pattern |
| `compose/patterns.md` ASCII diagram | `fwu-de/ais-chat (MIT, broker: …)` | 🔴 inside a fenced block, which every census from p118 to p121 **skips by design** |
| `intel/market.md` | *"the live permissive EMEA shelf, **measured this pass**"* | 🔴 an AGPL-3.0 repository listed as permissive under the words "measured this pass" |

🔵 **Two of the three were invisible to earlier censuses for reasons of scope, not of effort: one
sits in prose, one sits in a code fence. A licence claim is wherever a reader finds one.**

## 🟢 New channels this pass established

| channel | result |
|---|---|
| `git ls-remote --symref` | 🟢 **Resolves existence AND the real default branch in ONE call.** p120 needed **462** probes to read 52 files because it guessed `main` then `master`; 410 came back 404 and a 404 cannot distinguish wrong-branch from wrong-path from no-such-repo |
| `github.com` HTML via WebFetch | 🟢 **Readable** — returns description, licence and stars. `curl` gets **403** through this session's proxy, and `api.github.com` gets **403**. p118 recorded the `description` field as reachable only through the MCP relay's SEARCH endpoint; it is also reachable here |
| `raw.githubusercontent.com` | 🟢 the only `curl`-readable channel, and it cannot see repository metadata |

🔴 **`P122-G` — why the existence channel matters more than efficiency.** Three addresses this pass
would otherwise have published as "no licence file" **do not exist**:
`studip/studip`, `OpenEduCat-Inc/OpenEduCat`, `Opigno/opigno_lms` — all **404**. Each was
constructed from a product NAME in vendor prose, because the searches returned products
(Stud.IP, OpenEduCat, Opigno) and never their addresses. 🟢 **A plausible-looking address
assembled from a product name is a fabrication, and `NO-FILE` was hiding it behind a finding.**

## Files

| file | what it does |
|---|---|
| `classify_licence.py` | text → SPDX-ish token. Title-anchored, body-aware, split-grant aware. Pure function, no I/O |
| `extract_claims.py` | prose claims by paragraph-unwrap + proximity attribution (`WINDOW=90`) |
| `join_claims.py` | `verdict()`, `norm()`, `fold()` (slug case), `is_correction()` |
| `verdict_prose.py` | scores extracted claims against measured tokens |
| `scan_licences.sh` | licence probe over `raw.githubusercontent.com` |
| `resolve_head.sh` | existence + default branch via `git ls-remote --symref` |
| `probe_namespace.sh` | `ACTION C` — `pom.xml` `<groupId>` / Gradle `group` |
| `place_namespace.py` | `ACTION C` — namespace → country/region, closed vocabulary |
| `check_consistency.py` | `ACTION T` + `ACTION U` |
| `test_p122.sh` | **50 assertions, fully offline** |
| `fixtures/` | 13 real licence files, each one a defect class that broke an earlier build |

### The fixtures are the point

Every fixture is a file that a substring matcher gets wrong:

| fixture | the trap |
|---|---|
| `gpl2-preamble-names-lesser.txt` | GPL-2.0's **own preamble** names the Lesser GPL, at byte 853 of 18 092 |
| `epl2-secondary-names-gpl2.txt` | EPL-2.0's secondary-licence clause names *"GNU General Public License, version 2.0"* |
| `mpl2-secondary-names-gpl.txt` | MPL-2.0 names GPL and LGPL in its secondary-licence section |
| `mit-split-grant-names-cc.txt` | split grant; `docs/` is CC-BY-SA-4.0, the primary is MIT |
| `split-grant-portuguese.txt` | the split marker is **pt-BR** (*"usa duas licenças"*) |
| `faircode-sustainable-use.txt` | a **non-OSI** "Fair Code" grant that must never read as copyleft |
| `lgpl3-headerless.txt` | LGPL-3.0 committed **without its title line** |
| `r-stub-licence.txt` | R/CRAN stub: `YEAR:` + `COPYRIGHT HOLDER:` only; grant lives in `DESCRIPTION` |
| `split-unmarked-code-vs-content.txt` | three grants, unmarked; the third is **NonCommercial** |

## 🟢 Pre-registered for p123 — written into all THREE records, per `ACTION T`

🟢 **`ACTION W`** — calibrate every census in this KB the way `ACTION R` was forced to be:
for each instrument, score it against a set of rows known to be CORRECT and publish the
false-positive rate beside the defect count. 🔴 *Refuted if no existing instrument's rate exceeds
20 %.*

🟢 **`ACTION X`** — re-run `ACTION R`'s verification over the **216 remaining candidates**
(242 defect claims − 26 verified or dismissed this pass), in table cells as well as prose, using
the multi-file grant reader rather than one token per address. 🔴 *Refuted if fewer than 5 survive
verification.*

🟢 **`ACTION Y`** — replace every guessed branch in this KB's toolchain with
`resolve_head.sh`, and re-probe the **56 `NO-FILE`** addresses from this pass's sweep to
separate "no grant" from "no repository". 🔴 *Refuted if fewer than 3 of the 56 do not exist.*

🟢 **`ACTION Z`** — read `LICENSE-CODE`, `LICENSE-DOCS`, `LICENSE-DADOS` and `DESCRIPTION`
wherever `LICENSE` disagrees with the page, and record a repository's grant as a SET of
(path → token) pairs rather than one token. 🔴 *Refuted if fewer than 8 addresses carry more than
one grant file.*

🟡 **`ACTION V`** — **carried forward, clause verbatim** (p121, measured but not implemented by
p122): emit a machine-readable `<!--corrected-->` marker on every repaired row instead of
teaching the guard new vocabulary. **57 rows need back-filling; 1 marker exists.**

🔴 **`ACTION C` and `ACTION D` are CLOSED as refuted, not carried.** Both were pending five
passes. Their verdicts are recorded above and their reach is now characterised rather than
assumed — layer P is an EMEA public-sector detector (13 of 13 placements EMEA), and layer D
places only via national language or a named agency. Neither should be re-listed as open.
