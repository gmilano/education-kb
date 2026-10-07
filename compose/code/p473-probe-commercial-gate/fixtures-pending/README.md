---
industry: education
region: Global
updated: 2026-10-07
---

# `fixtures-pending/` — the two fixtures `P480` says this gate is missing (pass 37, 2026-10-07)

## Why they are here and not in `fixtures/`

`P480` (pass 37): this instrument reports **9/9** over four fixtures — `Apache-2.0`, `MIT`,
`ECL-2.0`, `CC-BY-NC-4.0` — and holds **no GPL-3.0 and no AGPL-3.0 specimen**. That is the exact pair
**`P171`** exists to protect, and it has been reopened more than once (`P171` → `P288` casefold →
`P455` window). A gate that cannot regress the families where every historical failure of this KB's
classifier has occurred is not evidence about that classifier.

🔴 **These are staged, not installed, for one reason: this pass could not execute the suite.**
`discover_probe.sh --self-test` and every sourcing of `../../lib/license_family.sh` were **denied by
the session's auto-mode classifier as external code**. `self_test()` globs `fixtures/*.LICENSE`, so
dropping these two in would have moved the gate from `9/9` to an **unverified** `11/11`. 🔵 **Adding an
expectation that has never been run is the defect this instrument exists to prevent**, so the payloads
are parked one directory over, where the glob does not reach and the gate stays honest at `9/9`.

## The two specimens — real payloads, fetched 2026-10-07

| Fixture | Bytes | Title block (line 1) | `.expected` |
|---|---|---|---|
| `agpl-3.0-classroomio.LICENSE` | 34,523 | `GNU AFFERO GENERAL PUBLIC LICENSE` | `AGPL-3.0/OK` |
| `gpl-3.0-lmscloud.LICENSE` | 35,148 | `GNU GENERAL PUBLIC LICENSE` | `GPL-3.0/OK` |

Sources: [`classroomio/classroomio`](https://github.com/classroomio/classroomio) `main/LICENSE` and
[`lmscloud-io/moodle-mcp-server`](https://github.com/lmscloud-io/moodle-mcp-server) `main/LICENSE`.

## Why these two payloads and not any GPL text

🟢 **Both carry both tripwires at once**, which is what makes them regressions rather than samples:

| Tripwire | `agpl-3.0-classroomio` | `gpl-3.0-lmscloud` | Guards |
|---|---|---|---|
| §6 *"allowed only occasionally and **noncommercially**"* | 1 occurrence | 1 occurrence | **`P250`** / **`P455`** — a bare-word NonCommercial test returns `PROHIBIDO` on both |
| §13 naming the **Affero** GPL in the body | 15 occurrences | **3 occurrences** | **`P171`** / **`P288`** — a body-wide `affero` match reads the **GPL-3.0** payload as `AGPL-3.0` |
| §0 anchor, mutually exclusive | *"refers to version 3 of the GNU **Affero** General Public License"* | *"refers to version 3 of the GNU General Public License"* | the discrimination `P288` installed |

🔵 **`gpl-3.0-lmscloud` is the load-bearing one.** It is a **GPL-3.0** payload that contains the word
`affero` three times and `noncommercially` once — so it fails **both** historical defects
simultaneously, and a classifier that gets it right has demonstrably got both anchors in the right
order.

## How a pass that *can* execute should promote these

```bash
cd compose/code/p473-probe-commercial-gate
./discover_probe.sh --self-test                 # confirm the current 9/9 baseline first
mv fixtures-pending/*.LICENSE  fixtures-pending/*.expected  fixtures/
./discover_probe.sh --self-test                 # expect 11/11
```

🔴 **If it does not report `11/11`, do not edit the `.expected` files to make it green.** The
expectations were derived by reading `lib/license_family.sh`'s documented branch order against these
payloads' actual text — the §0 anchors above — **not by running it**. A mismatch means either the
derivation is wrong or the classifier is, and **which one it is, is the finding**. Record it before
changing anything.

## Still open after this

⚠️ **`LGPL` has no fixture either**, and `OpenEduCat/openeducat_erp` (LGPL, 8,240 B,
`master/LICENSE`) is on these shelves. `P171`'s own comments record that **LGPL-3.0's text also says
the "GNU GPL" refers to version 3 of the GNU General Public License**, so probing the GPL sentence
first captures every LGPL — measured on `untisapi/untis4j`. 🔵 **A third fixture closes the family, and
the payload for it is already shelved.**
