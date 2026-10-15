# `p228-shelf-gate` — the licence shelf, re-read against the repositories

**Pass 228, 2026-10-15.** Discharges `ACTION ST` (p228's registered highest priority) and
`ACTION SP`, and runs `ACTION SH`'s standing inbound gate on this pass's records.

## What `ACTION ST` asked, and what it got

p227 corrected six licence cells by hand and registered `ACTION ST` because it *"has no idea
how many remain"*. Limb `1` wanted **3+ further cells disagreeing with the repository**.

`520` distinct slugs were harvested off the three table shelves and `468` grants were read
first-hand off `raw.githubusercontent.com` — the first shelf-wide grant read in this KB's
history.

**The first draft reported `11` family disagreements. Nine were defects in this instrument.**

| verdict | cells |
|---|---|
| `AGREE` | **1 372** |
| `CELL-WITHOUT-GRANT` | 149 (45 slugs) — a REACH bound, not a defect count |
| `BOUND` | 26 — not decidable from a root `LICENSE` at all |
| `UNDECIDABLE-BODY` | 20 — reported, never converted to a defect |
| `NOTATION` | 13 |
| **`FAMILY`** | **2** — both `acanas/swad-core` |
| **`INCOMPLETE-DUAL`** | **1** — `Elgg/Elgg` |

Limb `1` fires at `3` cells on `2` entities — but barely, and the honest statement combines
both limbs: `1 372` of `1 375` decidable cells agree, so p227's hand sweep was far closer to
the population than it feared. The gate's standing value is **cheap verification, not cleanup**.

## The finding: a licence token has five subjects that are not a grant

This is the reusable part, and every class below cost a false finding before it was named.
It is p224's `T224-3` — *the unit is the grant's SUBJECT* — with the subject space enumerated.

| class | example from these shelves | why the token is not a grant |
|---|---|---|
| `DIRECTORY-SCOPED` | `pupilfirst \| 978 \| docs/** \| CC-BY-SA-4.0` | the row's own subject column is a PATH |
| `BODY-CONTENT` | *"`GPL-3.0` included by **value**"* (`odoo/odoo`) | names what the licence FILE CONTAINS |
| `CORRECTION-NARRATIVE` | *"was published `MIT` in"* (`towardsai/ai-tutor-app`) | the value being WITHDRAWN |
| `QUOTED-EXTERNAL-CLAIM` | *"reads \*'the `MIT` LMS'\*"* (`frappe/lms`) | evidence about a SOURCE |
| `UNLINKED-CO-SUBJECT` | *"`OpenEduCat`, Open edX (`AGPL-3`)"* | the grant belongs to the UNLINKED entity |

A naive audit that skips all five has an **82% false-positive rate** on this corpus. That number
is the selling point of `P228-R1` in [`compose/patterns.md`](../../patterns.md).

## The two real defects

- **`acanas/swad-core` is `AGPL-3.0`, published here as `GPL-3.0`.** `master/LICENSE`, `34 501` B,
  `sha256₁₂ 884b434957ba`; title at offset `0` is `GNU AFFERO GENERAL PUBLIC LICENSE`; version
  line `Version 3, 19 November 2007`; §13 is `Remote Network Interaction`. The body also contains
  the string `GNU GENERAL PUBLIC LICENSE` at offset `1 880` — the mirror of p227's `T227-V3`.
  This is the Gibbon error in the **permissive** direction, the one p227's table says a *client*
  pays for: a hosted SWAD build was told it had no network-use trigger.
- **`Elgg/Elgg` is DUAL.** `master/LICENSE.txt`, `17 173` B, `sha256₁₂ 7188c83d8764`: *"available
  under either MIT or GPLv2"*, with `/mod` plugins `GPL-2.0-only`. The shelf published
  `GPL-2.0-only` from `composer.json` — true but incomplete, and it dropped the half a studio
  wants. Reported as its own verdict, because such a cell is incomplete rather than wrong.

## Why bound is never decided here

p225 and p227 both established that GPL-family `or-later` lives in a **channel** — the project's
own preamble or a source header — and that neither the canonical body's §14 nor its *"How to Apply
These Terms"* appendix is one. A root `LICENSE` therefore cannot settle a bound, and
`classify_grant.py` reports `bound=UNSETTLED-FROM-LICENSE` rather than guessing. The `26` `BOUND`
cells are a statement about the CHANNEL, not about the shelves.

## `ACTION SP` — limb 2 fires, and STOP

`ACTION SP` asked for the EU AI Act subject to be bound to a jurisdiction token, since `3` of
p227's `7` near misses were Vietnamese text. Run offline against p227's own `66` records
(`narrow_subject.py`), the narrowing is **strictly worse on both sides**:

- it **drops a genuine EU record** — *"Education tools that evaluate learners or influence access
  to qualifications fall into the high-risk category"*, which is EU by the QUERY it came from and
  names no jurisdiction in its text; and
- it **gains an irrelevant one** — `\beu\b` matches *"EU enterprise AI adoption stood at 19.95%"*.

The unit is the `(query provenance, record text)` pair, not the record text alone. **The pattern
is left as it is**, and the better fix came from elsewhere.

## The real defect, found by running `ACTION SH` on p228's own records

The live subject pattern `(?i)(ai act|...)` matched **`ai act` inside the string `AI action plan`**
in a Bitkom record about German education policy. One word boundary fixes it, costs no genuine
match, and is applied in [`st-refuted-claims.2026-10-15-p228.tsv`](../../../evidence/st-refuted-claims.2026-10-15-p228.tsv).
Inbound near misses drop `3 → 2`, both correctly silent; HITS stay `0`.

This is p227's standing rule — *the unit of a licence family token is a word in a known section* —
applying to subject patterns too, which p227's own table did not do.

## Running it

```sh
# 1-2. harvest, then read the grants (network; ~1 request per slug)
python3 -I harvest_cells.py ../../../agents/top.md ../../../repos/foundations.md \
                            ../../../verticals/solutions.md > harvest.tsv
awk -F'\t' '$5=="LIVE"{print $3}' harvest.tsv | sort -u > slugs.txt
sh fetch_grants.sh slugs.txt ./bodies > reads.tsv

# 3-4. classify and gate (offline)
python3 -I classify_grant.py reads.tsv ./bodies > classified.tsv
python3 -I gate.py harvest.tsv classified.tsv > gate.tsv

# ACTION SP, offline
python3 -I narrow_subject.py ../p227-direction-gate/p227-raw-results.txt

# controls
python3 test_shelf_gate.py
```

## Controls

**30, all passing.** Three are marked REGRESSION and are defects this pass's own instrument had
before publishing:

- the first scope pattern excluded **553** cells by matching ordinary markdown emphasis across a
  table pipe, `openSIS`'s `docs/License.txt` among them;
- the dual-grant preamble lost to the earliest title, reporting `Elgg` as plain `MIT`;
- the non-grant subject classes overlapped, so a quotation was filed as a correction narrative.

The GPL/AGPL mirror pair is pinned in both directions, since each family's §13 names the other.

## What this instrument still cannot do

- **Non-root grants.** The ladder is `main`/`master` × `LICENSE`, `LICENSE.md`, `LICENSE.txt`,
  `license.txt`, `COPYING`, `LICENCE`, all at the root. `OS4ED/openSIS-Classic`'s real grant is at
  `master/docs/License.txt` (`17 286` B, `sha256₁₂ 224ac3d403e3`) and the shelves recorded it
  correctly before the gate could see it. `142` of `468` grants (`30.3%`) are not at
  `main/LICENSE`, so the ladder matters more than it looks.
- **Manifest channels.** `23` of the `45` no-grant slugs already carry their real channel on these
  shelves — a `package.json`, `composer.json`, `__manifest__.py`, `pyproject.toml` or `DESCRIPTION`
  field. The gate does not read manifests.
- **Withdrawn cells.** A cell behind a `<!--corrected-->` marker is skipped, which means a
  corrected cell is invisible to the gate built to check it — `8` cells, and on the one slug whose
  only cell is withdrawn (`pipwerks/scorm-api-wrapper`) the SHELF was the better evidence.
