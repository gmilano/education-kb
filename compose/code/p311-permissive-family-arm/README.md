# p311 — the two most-published families, run at last; and the identity convention that was doing a licence's job

`ACTION p310-R` item 1, discharged, plus the defect that discharging it exposed.

## What was asked

> 🔴 **Pin a payload for `MIT` and `Apache-2.0` and run the arm.** They are the two
> most-published families on this base (**7 814 cells between them**) and **no dynamic arm has
> ever touched them**. 🟢 Every fixture needed is already in `evidence/` as a probed row; this
> is the single highest-value hour available.

## What came back

**Zero defects.** Nine declared classifiers × two families, on four payloads read first-hand
over `raw.githubusercontent.com` at the shas `p310`'s own prober had already recorded. Seven
`CORRECT`, one coarse-but-safe (`p191` answers `permissive-software`, its own axis, right in
effect), one `OUT-OF-DOMAIN` (`p129` reads holders).

🔵 **And the hour was still worth spending** — an unexecuted rung under 61 % of the published
cells is not something to leave asserted. But the *reason* item 1 was ranked first was wrong,
and that is this instrument's first finding.

## Finding 1 — the queue is sorted by blast radius and was read as a risk ranking

`family_coverage.py` prints its queue in descending cell order. Risk is `P(defect) × cost`, and
neither term points at the top of that queue.

`MIT` and `Apache-2.0` are the two families every rung on this base was authored and
hand-checked against. They were the implicit test corpus all along, which is *why* they are the
two biggest. 🟡 This instrument does **not** claim an inverse relationship from the history —
per family the rates are `2/4` above 1 000 cells against `4/6` below, which at `n=10` is **flat**,
and claiming a trend would be the unbounded claim `ACTION p310-R` item 3 exists to gate.

What is **not** flat is cost, and it is not a sample — it is a property of the grants:

| a wrong answer | costs |
|---|---|
| between permissive families | an attribution detail; the studio ships either way |
| weak copyleft read as permissive | a file-level obligation nobody priced |
| strong copyleft read as permissive | a whole-work source obligation nobody priced |
| 🔴 **noncommercial read as permissive** | 🔴 **the right to ship at all** |

🔴 **Every `DEFECT-COMMERCIAL` in this base's history was on a noncommercial family, and the two
noncommercial families still without a payload sit at positions 7 and 12 of the 12-long
uncovered queue.** `risk_order.py` prints both orderings, because a single-axis queue gets read
as a risk ranking whatever its author intended.

🟢 **The coverage metric moved too.** `p310` published `36 %` — 8 of 22 **families**. By **cells**,
which measures how much of the published data an arm has exercised, it was `24 %`. This pass takes
families to `55 %` (12 of 22) and cells to **`90 %`** (11 684 of 12 977). `MIT` alone is 43 % of all licence cells, so a
family-count average weights it equal to `CC-BY-NC-ND-4.0`'s 14.

## Finding 2 — `bytes` + `sha256_12` answers "same FILE?", and `p310` used it to answer "same GRANT?"

`p310` certified seven CC0 rows partly on *"six at the legalcode's exact `7 048` B"*. Both halves
of that instrument are refuted here, on real payloads, and each is a standing control:

| form | pair | raw | the whole difference | same grant? |
|---|---|---|---|---|
| **fixed document** | `noplag-engine` / `reference-audit` | `11 358` B `cfc7749b96f6` vs `11 357` B `c71d239df917` | 🔴 **one leading newline** (`a[1:] == b` exactly) | 🟢 **yes** |
| **fill-in slot** | `Open-Detector` / `GradeBridge` | `1 066` B `2e7c69b15c38` vs `1 100` B `6203d12e65d7` | 🔴 **the holder string** — 21 lines each, line 3 only, 34 B | 🟢 **yes** |

🔵 The split is exactly `p310`'s own holder-channel boundary (*fill-in slot → 13 of 13; fixed
document → 0 of 6*), carried from the HOLDER channel into the IDENTITY channel. For `MIT`, `BSD`
and `ISC`, byte length is a function of a field that is not the grant, so an exact-byte-length
test cannot certify the family **even in principle**.

`payload_identity.py` is the normalising oracle this implies. Six pinned payloads → **four
distinct grants**. 🟢 It is deliberately minimal, every step is named, and
`test_the_normaliser_still_separates_different_grants` exists because a normaliser widened until
everything matches proves nothing.

## Finding 3 — the defect, and it was not where the queue pointed

A side probe over the `proctoring` axis returned an `MPL-2.0` payload
([`aesophor/hacklympics`](https://github.com/aesophor/hacklympics), `16 725` B `1f256ecad192`).
Pinned opportunistically, it turned the gate red:

🔴 **`p153-declaration-surfaces/classify_body` read every `MPL-2.0` payload as `GPL-3.0`.**

`MPL-2.0` §1.12 defines *«Secondary License»* as *«either the GNU General Public License,
Version 2.0, the GNU Lesser General Public License, Version 2.1, the GNU Affero General Public
License, Version 3.0»*. `BODY_MARKERS` is ordered GNU-family-first — correctly, and its comment
says why — and the loop then took the first marker present **anywhere in 4 000 characters**.

Measured: `MOZILLA PUBLIC LICENSE` at character **0**; the GNU phrase at character **2 341**.
🔴 **List order beat document position.**

🔵 **Third instance of one class in three instruments**, after `p306`'s `elif "affero" in low:`
(`p309`) and `"cc0" in low` (`p310`): *a whole-document substring scan with a hand-ordering
standing in for a located channel.*

🟢 **Fixed by scoring markers on POSITION, with the existing most-specific-first order kept only
as the tie-break** — `p198`'s settled channel (*a licence declares its family in its title*)
expressed as the one line the function needed. All 36 of `p153`'s own controls still pass, and
the `AGPL-3.0` and both `GPL-3.0` payloads `p309` fought over are unchanged.

🔴 **Direction:** `MPL-2.0` is file-level copyleft, `GPL-3.0` whole-work, so this **over-stated**
the obligation — like `p309`'s it excluded usable supply (an opportunity cost) rather than
admitting unusable supply (a client cost). **161 published cells.**

🔵 **And this is the pass's argument confirmed by its own accident.** The `7 884` cells the queue
ranked first were clean. The one real defect was in a `161`-cell family at position 5 of the
uncovered queue, found because a probe on an unrelated axis happened to return it.

## Finding 4 — ONE INVISIBLE BYTE SWITCHED THE TITLE CHANNEL OFF, AND THE FALLBACK WAS THE LADDER IT REPLACES

🔵 **This one arrived as a refutation of this pass's own writing, which is the best way it could
have arrived.** The pass wrote on the shelves that
[`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) (345★) *"serves no licence
payload at any probed rung"*, on the strength of a root-ladder `404`. 🟢 **`gate-enumeration`
(`p275`) went red, walked the tree and named two candidate grants under `docs/`.** The row is
**`GPL-2.0`**, `17 286` B · `224ac3d403e3` — and that payload begins `ef bb bf`.

| instrument | with the BOM | without it |
|---|---|---|
| `p150.title_licence()` — the canonical title reader | 🔴 **`None`** | 🟢 `GPL` |
| `p191.classify_spec()` — IMPORTS that reader | 🔴 **`GPL-3.0`** | 🟢 `GPL-2.0` |
| 🔴 **this module's own `canonical_identity()`** | 🔴 **two shas for one grant** | 🟢 one |

🔴 **`str.strip()` does not remove `U+FEFF`.** Python does not classify the BOM as whitespace, so
every per-line `.strip()` in the chain passed it through. The title line was
`"\ufeffGNU GENERAL PUBLIC LICENSE"` and every `TITLES` pattern anchors at position 0.

🔵 **Why this shape is worse than the three defects before it.** `p309`'s, `p310`'s and finding 3's
were instruments **answering wrongly**. Here the instrument **did not answer at all** — the title
channel built specifically to replace body-substring ladders was silently switched off, and the
caller fell back onto the exact ladder it exists to replace. 🔴 **A channel that fails closed is
indistinguishable from a channel that was never consulted**, and the wrong answer carries no signal
that the good channel was skipped. 🔴 Not cosmetic either: `GPL-2.0` has no patent grant and no
§13, and GPL-2.0-only code cannot be combined with GPL-3.0 code.

🟢 **Fixed once, in `p150` (`strip_bom()`, applied in `title_licence()` and `title_window()`), for
every importer.** All 35 of `p150`'s controls still pass. 🔴 **And the same byte had already
defeated this module** — an oracle built to collapse invisible prefixes, built with an invisible
prefix defeating it. The Apache pair's newline was caught only because a newline *is* whitespace.

🟢 **Two gains from one refuted claim:** `GPL-2.0` was the largest uncovered family (443 cells), and
it is now pinned.

## Finding 5 — a 23rd family, and the battery fails safe on it

[`HalidCisse/Matrix`](https://github.com/HalidCisse/Matrix) serves the **`DBAD` public licence
v1.1** (`1 127` B `65569613b0b7`) — a real grant, served as markdown, whose operative clause is
*«Do whatever you like with the original work, just don't be a dick»* with a list that is
explicitly *«not limited to»*. It also carries a resale prohibition (1b) and an unquantified
expectation of payment on commercial success (2).

🔴 **It passes a "has a `LICENSE` file?" screen and a star screen.** It is the first grant on this
base that is **unclassifiable by design**: a studio cannot bound its obligations under an
open-ended subjective condition.

🟢 **All eight payload readers abstain on it, and `p306` returns
`commercial_use=UNDETERMINED`** — which under `P250` is indistinguishable from PROHIBITED, the
correct posture. Nothing reads it as permissive. It is pinned as a **positive control**, because a
battery that fails safe on a family it has never seen is a property worth a standing gate.
🔴 `risk_order.py` grades it `CRITICAL`, not `LOW`: an unknown family is one whose obligations
nobody has bounded.

## Files

| file | what it is |
|---|---|
| `fixtures/` | seven payloads, each with its byte length in its own filename |
| `fixtures.py` | the pins and the canonical answer for each, with why each is in the set |
| `payload_identity.py` | the normalising identity oracle — finding 2 |
| `run_permissive.py` | the dynamic arm. 🔵 `ENTRY_POINTS`, `grade`, `_answer` all **imported** from `p310` |
| `risk_order.py` | both orderings, the cell/family metrics, and the history with its `n` stated |
| `test_p311.py` | **32 controls** |

Run: `make gate-permissive-arm` · `make permissive-arm` · `make risk-order` · `make family-coverage`

## What this instrument does NOT establish

- 🔴 **No benchmark, no legal opinion.** The consequence classes in `risk_order.py` are a
  studio-risk ordering, not advice. `DBAD-1.1`'s `CRITICAL` is a *get-counsel* flag.
- 🟡 **The `n=10` history is not a trend** and the file says so twice.
- 🔴 **10 of the 22 published families still have no payload**, `BSD-3-Clause` (301 cells) the
  largest and the two noncommercial ones (`CC-BY-NC-SA-4.0` 132, `CC-BY-NC-ND-4.0` 21) the most
  expensive. `DBAD-1.1` is a 23rd family the shelves do not yet publish, so it is pinned but not
  counted in that denominator.
- 🟡 **No BOM sweep was run.** `U+FEFF` blindness was repaired in the two places it was OBSERVED;
  **nothing here establishes that the other seven readers are not blind the same way**, and the
  failure mode is silence rather than a wrong answer → `ACTION p311-R` item 2b.
- 🟡 **Neither defect's realised loss was measured** — no `MPL-2.0` or `GPL-2.0` shelf cell was
  re-probed against the repaired classifiers.
- 🟡 **CRLF normalisation is declared and UNEXERCISED** — all seven payloads are LF. Stated rather
  than claimed.
- 🔴 **`p283-ladder-case-audit` reads a licence TITLE in a code string as a licence PATH rung.**
  This file hit it, worked around it by not spelling the title, and registered it as
  `ACTION p311-R` item 4 rather than editing a third standing instrument in one pass.
