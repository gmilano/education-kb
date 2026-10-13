---
industry: education
region: Global
updated: 2026-10-13
---

# `p173-apache11-family` — the shared classifier could not see `Apache-1.1`

**Pass 173, 2026-10-13. `ACTION JU`, `gap 120` / `T232` CLOSED — and the falsifier's first limb
FIRES, which means the defect is narrower than the gap claimed.**

p172 found that `compose/code/lib/license_family.sh` answers **`BSD`** for the Apache Software
License 1.1, including for the file named `apache1.1.license.txt`. The lib is a **shared hardened
control** sourced by **42** instruments and **14** test suites, so p172 registered it as a defect in
a control rather than a one-off.

## The mechanism, and why the existing Apache branch could not catch it

`Apache-1.1` **is not titled** *"Apache License"*. It is titled **"The Apache Software License,
Version 1.1"**, so it falls straight through the title-block anchor for `Apache-2.0`. It then
matches the **BSD grant phrase** — *"Redistribution and use in source and binary forms, with or
without modification"* — which `Apache-1.1` genuinely contains, because `Apache-1.1` **is
BSD-shaped**. `BSD` was the correct answer to the only question the classifier was asking.

**The direction of the error is not the dangerous one, and that bounds the damage:** `BSD` and
`Apache-1.1` are both permissive and both OSI, so `commercial_use_ok()` answers ALLOWED either way
and **no commercial verdict this KB published was wrong because of this**. What was lost is
**clause 3**: `Apache-1.1` requires an end-user-documentation acknowledgment —

> *"This product includes software developed by the Apache Software Foundation
> (http://www.apache.org/)."*

— and `BSD-3-Clause` requires none. A deliverable reporting `BSD` over an `Apache-1.1` component
**drops an attribution obligation the client has to meet**. It is attribution debt, not permission
debt, and it should be reported as such.

## The fix: two anchors, title then clause, and the order is load-bearing

| anchor | answer |
|---|---|
| title block says `Apache Software License` **and** `Version 1.1` | `Apache-1.1` |
| title block says `Apache Software License` **and** `Version 1.0` | `Apache-1.0` |
| title block says `Apache Software License`, **no version**, and the body carries the clause-3 acknowledgment | `Apache-1.x-UNVERSIONED` |

The third row follows `GPL-UNVERSIONED`, already in this lib: **do not invent a version number the
payload does not state.**

The branch sits **before** the BSD grant-phrase branch, because both match the same payload and the
first to return wins — this is `P845` again, in a new family.

**A payload carrying the acknowledgment but NOT the title stays `BSD`, deliberately.** The ASF
acknowledgment appears in BSD notices of projects that credit the ASF; a clause without a title
describes a courtesy, it does not grant. That is the `P304`/`P312` evidence rule applied here, and
it is the negative control the suite now pins.

## What changed, measured on two populations

| population | size | verdicts changed |
|---|---|---|
| `sakaiproject/sakai` `licenses/` at `88f8e09c0a38` | `86` paths | 🔴 **`25`** — all `BSD` → `Apache-1.1`, across `20` distinct blobs |
| 🟢 **every licence body committed in this repo's own fixtures** | `50` files | 🟢 **`0`** |

🔴 **`ACTION JU`'s first falsifier limb FIRES: the corrected classifier changes `0` verdicts outside
`Sakai`.** On the evidence available offline, `T232` is a property of **one 2005-era manifest**, not
a live defect in a shared control. The fix is still correct and still ships — a classifier that
cannot name a family it meets is wrong whether or not it has met it twice — but `gap 120`'s claim
that *"every instrument sourcing the shared lib inherits this"* is **true in principle and, so far,
empty in practice.** The honest statement is that it inherits a **latent** error.

🟢 **Second limb SILENT: `13` of `14` test suites that source the lib return byte-identical results
before and after**, and the `lib` suite itself goes from `199/199` to `207/207` with `8` new
assertions. The one difference is `p355-cwd-portability`, which fails in the *copy* used as the
pristine baseline and passes in the real tree both before and after (`T250`).

## The control: a re-read pinned by CONTENT, not by ref

p171 recorded its `Sakai` limb as an **UNCONTROLLED** re-read because the repository moved and the
git server **refused the pinned sha** in `want`. p173 hit the same refusal —
`fatal: couldn't find remote ref 88f8e09c0a38` — and got the controlled read anyway:

> **`raw.githubusercontent.com/<owner>/<repo>/<sha>/<path>` serves an arbitrary commit even when
> the git server will not negotiate it.** `86` of `86` bodies came back **byte-identical** to
> p172's recorded `sha256[0:12]`. `0` drift, `0` fetch failures.

🟢 **`T249` — a sha the git server refuses is not an unreachable sha.** Fetch the paths over the raw
channel and verify each body against the hash the earlier pass recorded; the hash **is** the
control, and it is stronger than a ref because it does not depend on the server's reachability
policy. This retires *"the repository moved, so the re-read is uncontrolled"* for any population
whose per-path hashes a previous pass wrote down.

## Files

| file | what it is |
|---|---|
| `sweep_family.sh` | classifies every file in a directory tree with the shared lib, one row per file. Sources the lib **relative to itself** |
| `fixtures/apache1.1-real-sakai-manifest.LICENSE` | the REAL body, `2 383` B, `sha256[0:12] = 705c81dd9e54`, read at the pinned sha |
| `fixtures/crafted-bsd3-plus-asf-acknowledgment.LICENSE` | **FABRICATED, and it says so in its name** — the real `BSD-3-Clause` of `YuanGongND/gopt` with the ASF acknowledgment appended and no Apache title. Must stay `BSD` |

🔴 **`T247` — and why this instrument exists instead of p172's.**
`p172-manifest-attribution/classify_bodies.sh` sources the lib from the **absolute** path
`/tmp/education-kb/compose/code/lib/license_family.sh`. This pass's clone is at
`/home/user/education-kb`, so p172's instrument **cannot run at all here**. An instrument that
hardcodes the clone location is not reusable, it is a transcript. This repository ships
`p355-cwd-portability` as a control for exactly this, and the control did not reach p172's script.

## Re-run it

```sh
cd compose/code/lib && ./test_license_family.sh          # 207/207
cd ../p173-apache11-family && ./sweep_family.sh <dir>    # one row per body
```
