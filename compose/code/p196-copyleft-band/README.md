---
industry: education
region: Global
updated: 2026-10-14
---

# `p196-copyleft-band` — the band generalises to copyleft, and finds that nothing on this shelf is narrowed

**Pass `196`, `2026-10-14`.** Runs p195's second pre-registered action.

## What was pre-registered

> *"Derive byte bands for `AGPL-3.0` / `GPL-3.0` / `ECL-2.0` and run `delivery_verdict` over
> the `77` copyleft rows. **Limb 1:** a band exists and flags narrowed copyleft → the control
> generalises beyond permissive. **Limb 2:** copyleft payloads are too variable to band → the
> control is **permissive-only**, and say so."*

## 🔴 First, the population was `83`, not `77`

p195's gap note named three unbanded families *(`AGPL-3.0`, `GPL-3.0`, `ECL-2.0`)* and a count
of `77`. `77` = AGPL `41` + GPL-3.0 `29` + GPL-2.0 `5` + ECL-2.0 `2`. 🔴 **It silently drops
the `6` weak-copyleft rows that p195's own families table lists and that its own
`band_of_family` also returned `NO-BAND` for** — `LGPL-3.0` ×`4`, `LGPL-2.1` ×`1`,
`MPL-2.0` ×`1`. The unbanded copyleft population is **`83`**.

🔵 Those `6` are not a rounding detail: they contain `odoo/odoo` and
`bigbluebutton/bigbluebutton`, and the family whose shape forced this pass's mechanism change.

## 🟢 LIMB `1` FIRES on the mechanism — but the change is structural, not a table row

🔴 **A single `lo`/`hi` interval per family is WRONG for `LGPL-3.0`, and the reason is in the
licence, not the corpus.** `LGPL-3.0` is published in **two legitimate forms**:

| form | bytes | what it is |
|---|---|---|
| **short** | `7 651` | the LGPL preamble alone, incorporating `GPL-3.0` **by reference** |
| **full** | `42 098` | `GPL-3.0` included **by value** — SPDX's own text, read this pass |

🟢 Both appear on this shelf: `bigbluebutton` `7 652` and `luisgf/openbadgeslib` `7 650`
against **`odoo/odoo` `43 529`**. 🔴 **A one-interval band must call one of the two
legitimate forms "narrowed."** So **a band is a SET of intervals**, and p195's
single-interval families are the one-element case. `odoo/odoo` is 🟢 **IN-BAND, not an
anomaly** — a reading a one-interval band would have got backwards.

## The anchors are EXTERNAL (`P417`)

Two independent anchors per family, neither produced by this instrument:

- **SPDX** `license-list-data` `text/<id>.txt`, fetched this pass over the raw lane
- the **modal size** in p195's own `468`-slug census

Committed as [`evidence/licence-pristine-anchors.2026-10-14-p196.tsv`](../../../evidence/licence-pristine-anchors.2026-10-14-p196.tsv).
🔵 `gnu.org` and `mozilla.org` are both **`403` at this session's proxy**, so the canonical
upstream texts were not reachable; SPDX over the raw lane is the substitute, and it is named
rather than hidden. The band spans both anchors **±`10`%**, and the `10`% is **inherited from
p195's published `MIT` band** (`1 000`–`1 200` B around a `1 071` B median) — not tuned until
this pass's answer looked tidy.

## Measured, `2026-10-14`, over all `83`

| band verdict | n |
|---|---|
| 🟢 `IN-BAND` | **`79`** |
| 🔴 `UNDER` | **`4`** |
| `OVER` | 🟢 `0` |

[`evidence/copyleft-band.2026-10-14-p196.tsv`](../../../evidence/copyleft-band.2026-10-14-p196.tsv).

## 🔴 And the HYPOTHESIS behind the limb is REFUTED: all `4` are false positives

p195's own rule — *"the band is a TRIGGER TO READ, never a verdict by itself"* — so all four
were fetched and read. Byte sizes reproduced p195's census exactly on all four.

### `3` of `4` are the GNU **short-notice** form — a legitimate third shape

| row | bytes | what the bytes are |
|---|---|---|
| [`andremadstop/learning-nc`](https://github.com/andremadstop/learning-nc) | `723` | 🟢 the FSF's prescribed **short notice**: *"This program is free software… either version 3 of the License, or (at your option) any later version"* + a pointer to `gnu.org` |
| [`24kchengYe/human-skill-tree`](https://github.com/24kchengYe/human-skill-tree) | `1 134` | 🟢 the same short notice, **plus a split scope** |
| [`solin-repo/moodle-block_atrisk`](https://github.com/solin-repo/moodle-block_atrisk) | `703` | 🟢 the same, and it elects **`GPL-3.0-or-later`** explicitly |

🟢 **These are valid grants by incorporation by reference, and `P419`'s `n=2` header window
got the family RIGHT on all three.** 🔴 **They are NOT `Gap 421`.** `Gap 421`'s registered
shapes are sub-`1`kB payloads that **grant nothing** — a title and a copyright line, or
`talentcoach`'s view-only negation of `MIT`'s verb list. These grant everything the full text
grants. **Same size class, opposite legal content**, which is why size is a trigger and never
a verdict.

🔵 **The mechanism is the SAME one `LGPL-3.0` forced**: a GNU family has a full-text form and
a notice form, so its band set needs a third interval. Not added this pass — adding it from
`3` observations would be fitting the band to the corpus. **Pre-registered for p197 instead.**

🔵 Two further axes the census's `family` column drops, both delivery-relevant:
`24kchengYe/human-skill-tree` dual-licenses `skills/*.md` as **AGPL-3.0 OR MIT** while `app/`
stays AGPL-3.0 — 🔵 **already registered as `P1056` (split scope); cited, not re-derived.**
And `moodle-block_atrisk` is **`-or-later`**, which a flat `GPL-3.0` label does not carry.

### `1` of `4` is a **missing appendix**, not a narrowed grant

[`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) — `15 214` B
`GPL-2.0`, only **`389` B** below the band edge, the one hit that could have been real
narrowing.

| | SPDX `GPL-2.0` | `rosariosis` |
|---|---|---|
| lines | `117` *(reflowed)* | `276` *(hard-wrapped at ~`72` cols)* |
| words | `2 910` | `2 496` |
| ends at | the Ty Coon signature block | 🔵 **`END OF TERMS AND CONDITIONS`** |

🟢 **Every operative section `0`–`12` is present; the `414` missing words are entirely the
non-operative *"How to Apply These Terms to Your New Programs"* appendix.** 🟢 **The grant is
complete. `GPL-2.0` stands, unchanged.**

🆕 🔵 And `rosariosis` carries *"GNU **Library** General Public License"* where SPDX's text
reads *"**Lesser**"* — the FSF's pre-`1999` wording. **`rosariosis` ships the authentic 1991
text and SPDX ships a modernised one**, so the `389` B is partly SPDX's edit, not the
repository's.

## The verdict, split honestly

| | |
|---|---|
| 🟢 **the control generalises** | a band is derivable for every copyleft family on this shelf; `79`/`83` land in it; `0` `OVER` |
| 🔴 **the band has a false-positive CLASS** | `4`/`83` = `4.8`%, and **`4` of `4` are false positives for narrowing.** Cause known for all four |
| 🟢 **the shelf's answer** | 🟢 **`0` of `83` copyleft rows carry a narrowed grant.** A negative, measured, and worth more than a find |
| 🔴 **what it still cannot do** | `P420`: size does not identify. Three AGPL-3.0 texts here are `34 523` B exactly with different digests. Identity stays `P392`'s *(FILE, digest)* pair; family stays `P419`'s header read |

🔵 **So `delivery_verdict`'s `GO-SUBJECT-TO-FAMILY` can become `GO` for `79` rows** — but the
`41` `AGPL-3.0` rows' *delivery* constraint was never the band. It is network-use disclosure,
and that is a fact about the family, which no byte count changes.

## Suite

`band_copyleft.sh --self-test` — **`32`/`32`**, offline, no network. It carries **p195's seven
permissive assertions unchanged as a regression control** (`P237`: do not fork the shared
classifier — the permissive intervals are p195's, byte for byte), flips the two p195 asserted
as `NO-BAND`, pins the bimodal `LGPL-3.0` **including the trough between its two forms**, and
asserts `P420`'s warning as a test: two distinct payloads at `34 523` B both land `IN-BAND`
and the band says nothing about which is which.

## Pre-registered for p197

| action | 🟢 limb `1` | 🔴 limb `2` |
|---|---|---|
| Add a **notice-form** interval to each GNU family's band set, derived from a corpus WIDER than this shelf's `3` rows | the form has a stable size range → the `4.8`% false-positive class closes | the notice form is free-text and unbandable → the band is **full-text-only**, and the `3` rows are a permanent exclusion list |
| Run the band over the `5` `UNCLASSIFIED` and `2` `NONCOMMERCIAL-NOT-OSI` rows | a band places them → the families are recoverable from size + header | it does not → they need body reads, as `P47` says |
