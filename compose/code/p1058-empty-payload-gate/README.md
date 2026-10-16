---
industry: education
region: Global
updated: 2026-10-16
---

# `p1058-empty-payload-gate` — the licence file that exists, answers `200`, and is empty

**Pass 243 · 2026-10-16 · 29/29 controls · every fixture a payload read first-hand**

## What it detects

Three defects, all measured this pass on real payloads, all of the same shape:
*the family question has an answer and the answer is useless.*

| verdict | what it means |
|---|---|
| `EMPTY-PAYLOAD` | a `200` at the declared licence path with **zero bytes** (or whitespace only) — never a family, never usable |
| `UNREADABLE` | the path did not answer `200`; a refusal to clear, never a permission |
| `SELF-REFERENCE` | a family token is present **only inside the payload's own canonical body** — not evidence |
| `QUALIFIED-GRANT` | a restriction sits in the clause that **qualifies the grant verb**, before it |

## Why it exists

### 1. `rine77/meineschule-digital` — three channels, three answers

The README says *"MIT – siehe [LICENSE](LICENSE)"*. `LICENSE` exists at that exact
path, answers `200`, and is **`0` bytes** — `sha256` `e3b0c442…`, the hash of the
empty string, identical for every repository on earth.

| channel | answer |
|---|---|
| README claim | 🟢 `MIT` |
| GitHub API `license` | 🔴 `{"key":"other","spdx_id":"NOASSERTION"}` |
| the payload at the declared path | 🔴 `0` bytes |
| `p1058` | 🔴 `EMPTY-PAYLOAD` → **not usable** |

Every grant ladder on these shelves documents `byte-floor=1B` and records this
response as `FOUND`, because the **code** is authoritative and the byte count is
recorded beside it rather than instead of it. That rule is right, and it is why
the byte count needs a gate of its own.

### 2. `EdupageAPI/edupage-api` — `P171`, for the fourth time

`GPL-3.0`'s **section 13 is titled *"Use with the GNU Affero General Public
License"***. A token classifier written for this pass — without reading
`lib/license_family.sh` first — returned `AGPL-3.0` on a `GPL-3.0` payload, on the
**highest-star row of the harvest** (`102`★).

p242 recorded this defect class three times and wrote *"every classifier on these
shelves that greps a licence BODY for a token eventually reads the licence's own text
as an addition"*. 🔴 **An independent reimplementation reproduced it on its first
run, which makes it a property of the METHOD and not of one codebase.**

The fix is the structural one p242 required, not a deleted token: establish
whether the payload **is** a canonical body first, and if it is, its own words are
its terms. `test_gpl3_section13_still_in_payload` asserts the offending word is
**still in the payload**, so deleting the guard fails the suite.

### 3. `123xiaojun/student-management-system` — the narrowing placed *before* the verb

> *"For **non-commercial purposes**, permission is hereby granted, free of charge, to
> any person obtaining a copy of this software …"*

The MIT sentence is **verbatim**. Nothing is added after it. So the instruments that
read **additions** (`p242-grant-delta`) or **byte excess over a size ceiling**
(`p1054-mit-plus-clause`) are not the channel that catches it — the restriction is in
the four words that qualify the grant verb. 🔵 **`p1054` does catch this payload, by
its restriction-token scan; what it does not do is say WHERE the restriction sits, and
the position is what distinguishes a narrowed grant from a licence with a second
section.**

The window is deliberately short (`120` chars) and exercised from both sides, so a
restriction belonging to another clause is not attributed to the grant.

## Run

```
cd compose/code/p1058-empty-payload-gate && python3 -I test_empty_payload_gate.py
python3 -I empty_payload_gate.py fixtures/*          # the report over all 8 fixtures
```

Wired into `make hooks` (`gate-offline`) — no network, safe in a hook and in a
sandbox without egress.

## Fixtures

All eight read first-hand at pass 243 from `raw.githubusercontent.com`, at the branch
`git ls-remote --symref` reported, with the head pinned in
[`p243-verified-rows`](../../../evidence/p243-verified-rows.2026-10-16-p243.tsv) and
[`p243-withheld`](../../../evidence/p243-withheld.2026-10-16-p243.tsv).

| fixture | bytes | why it is here |
|---|---|---|
| `meineschule-digital.LICENSE.empty` | `0` | the headline |
| `edupage-api.LICENSE.gpl3` | `35 148` | `P171`'s fourth occurrence |
| `123xiaojun.LICENSE.mit-prefixed-nc` | `4 569` | the prefix narrowing |
| `campus-cli.LICENSE.isc` | `748` | a permissive grant that is **not** MIT/BSD/Apache (`ISC`) |
| `nfc-attendance-reader.LICENSE.mit-plus-scope` | `1 325` | MIT + a trailing scope note about hardware files |
| `webuntis-ha.LICENSE.mit-truncated` | `797` | MIT, **holderless**, warranty clause cut off mid-paragraph |
| `aula.LICENCE.polyform-nc` | `4 563` | `PolyForm-Noncommercial-1.0.0`, found only because the path vocabulary carries the British `LICENCE` |
| `hogwarts.LICENSE.sspl` | `30 645` | `SSPL-1.0` — the highest-star SIS of the harvest, not OSI |

## What it does NOT do

`P237`'s rule is kept: **this file decides no licence family.** It reports whether the
family question may be asked at all, and hands the payload to
`lib/license_family.sh`.
