# `p237-grant-payload-shapes` — three grants whose FRAME is the defect, not the licence

`ACTION UU`. Every row p237 shelved was grant-read first-hand off `raw.githubusercontent.com`.
Three of those payloads are correctly-licensed and still wrong-shaped:

| payload | shape defect | why it is kept as a fixture |
|---|---|---|
| [`Lu-Yu-Zhen/KongMeng-Agent`](https://github.com/Lu-Yu-Zhen/KongMeng-Agent) `LICENSE` | 🔴 **UTF-8 BOM (`ef bb bf`) before `Apache License`** | a classifier anchored on a **prefix** reads three invisible bytes and falls through |
| [`telekom/ki-in-schulen`](https://github.com/telekom/ki-in-schulen) `LICENSE` | 🟡 **no copyright line at all** | these shelves print a holder in every grant cell; here there is none to print |
| [`schild-report/schild.report`](https://github.com/schild-report/schild.report) `LICENSE` | 🟡 **`Copyright (c) hmt`** — holder, no year | the field exists, is readable, and is undated |

## The one that could have cost a verdict

`osi_family_of` anchors on a **substring** (`grep -qi 'Apache License'`), so the BOM does not
reach it. That was **luck until this file asserted it**. The fixture also keeps the hazard
visible: `head -1` on it does *not* start with `Apache License`, and the test fails if that
ever stops being true — so the fixture cannot quietly stop demonstrating the thing it is for.

## The two that are not misgrants

A holderless `MIT` and a year-less `MIT` are both `MIT`. 🔵 **The correct cell reads
`holder *unknown*`; a cell that infers a holder from the org handle is the defect.** p235 found
that `GPL-2.0` has no holder field to read at all; these two show the field can be **absent**
or **undated** inside a licence that does have one — so "no holder printed" is three different
facts and these shelves had one word for it.

Run: `bash test_payload_shapes.sh` *(9 controls, offline, standing in `make gate-offline`)*.
It `cd`s to its own directory first — `p355-cwd-portability`'s lesson, per the Makefile header.
