---
industry: education
region: Global
updated: 2026-10-14
---

# `p196-none-tree-reach` — p969's open limb, and the fifth recurrence of a defect this KB has named four times

**Pass `196`, `2026-10-14`.** Runs p195's fourth pre-registered action, **with a different
instrument than the one pre-registered, and the substitution is the finding.**

## What was pre-registered, and why it was already refuted

> *"Probe `docs/`, `legal/`, `.github/` for the `88` root-`NONE` rows (`p969`'s open limb).
> **Limb 1:** a material share have a grant one level down → `18.8`% is an artefact of
> root-only reach. **Limb 2:** they are genuinely unlicensed → `18.8`% stands."*

🔴 **Three named directories is a filename list with a `/` in it, and `P441` proved — three
times, against this same shelf — that widening a list cannot fix a list:**

| when | what the list missed | the widening that missed it again |
|---|---|---|
| p436 | `openedx/XBlock` ships `LICENSE.TXT` | its `14`-name list has no `LICENSE.TXT` |
| p440 | the same row | a **`41`-name** widening missed it a **third** time |
| p195 | the same row | a **`19`-name** ladder missed it a **fourth** time, and published it inside the `88` |
| 🔴 **p196's pre-registration** | the same row | 🔴 **`docs/` + `legal/` + `.github/` would have missed it a FIFTH time — `LICENSE.TXT` is at the ROOT** |

🟢 So this runs `P441`'s channel, which **sustains an absence** instead of failing to find a
presence:

```sh
git clone --filter=blob:none --no-checkout --depth 1   # commit + trees, no blobs
git ls-tree -r --name-only HEAD                        # the COMPLETE tree, unpaginated
```

## Measured, `2026-10-14`, over all `88` of p195's root-`NONE` rows

| verdict | n | share |
|---|---|---|
| `ABSENCE-ENUMERATED` — no path in the complete tree is a licence text | **`74`** | `84.1`% |
| 🔴 `OWN-GRANT-AT-ROOT` — a **root** licence the `19`-name ladder missed | **`3`** | `3.4`% |
| 🔴 `OWN-GRANT-IN-SUBTREE` | **`9`** | `10.2`% |
| `BUNDLED-GRANT-ONLY` — every grant found is a vendored dependency's | `2` | `2.3`% |
| `CLONE-FAILED` | 🟢 **`0`** | — |

🟢 **LIMB `1` FIRES. `12` of `88` rows (`13.6`%) do carry their own grant**, so `18.8`% is in
part an artefact of root-only reach. 🔵 **And it replicates `P441` independently**: `P441`
found `9` of `87` (`4` root, `5` subtree) on a different population; this pass finds `12` of
`88` (`3` root, `9` subtree). Two populations, one rate.

### 🔴 The three root filenames, named

| row | root filename | why the ladder missed it |
|---|---|---|
| 🔴 [`openedx/XBlock`](https://github.com/openedx/XBlock) | **`LICENSE.TXT`** *(+ `NOTICE.txt`)* | uppercase extension — **the row `P441` named, missed a 4th time** |
| 🔴 [`kstateome/lti-launch`](https://github.com/kstateome/lti-launch) | **`License.txt`** | mixed case **and** an extension |
| 🔴 [`open-spaced-repetition/fsrs4anki-helper`](https://github.com/open-spaced-repetition/fsrs4anki-helper) | **`License`** | mixed case, no extension |

🔵 All three are two or three characters away from a name the ladder already tried. That is
`P441`'s thesis restated by measurement, not argument.

### 🟢 `p969`'s own row CLOSES, as `p969` predicted

[`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) returns `OWN-GRANT-IN-SUBTREE`:
**`11` own licence texts below the root** (plus `11` vendored), which is the `docs/License.txt`
GPL-2.0 p195 read by hand and registered as an open limb. 🟢 **Now reached by instrument.**

### 🔴 And one of p195's published readings is REFUTED by reach

🔵 p195 wrote: *"`1EdTech`'s LTI example tool, `adlnet`'s SCORM→xAPI wrapper and
`Lumieducation/Lumi` all return **no licence at root**"* and drew from it *"the
interoperability layer grants nothing."*

🔴 [`Lumieducation/Lumi`](https://github.com/Lumieducation/Lumi) carries **`15` own licence
texts** in a `6 348`-path tree. The root probe was right and the **conclusion** was wrong:
`Lumi` grants something; p195 could not see it. The layer-wide claim needs re-reading row by
row, which this pass does not do — recorded as an open limb, not quietly dropped.

## 🆕 The case-variant proof that fell out of this run

[`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) and
`os4ed/openSIS-Classic` are **both** in the `88`, and the enumeration returns
**identical figures for both** — `5 656` paths, `11` subtree, `11` bundled. 🔴 **That is one
repository counted twice**, measured rather than assumed. See
[`p196-population-diff`](../p196-population-diff/) for the other four pairs.

## The corrected figure

| | rows |
|---|---|
| p195's root-`NONE` | `88` |
| 🔴 less one case-variant duplicate | `−1` → `87` distinct |
| 🔴 less rows with an own grant at any depth | `−11` distinct |
| 🟢 **genuinely without an own grant, absence ENUMERATED** | **`76`** |

🟢 **`76` of `468` = `16.2`%, not `18.8`%.** 🔴 And `468` is itself understated — the
population is `494` distinct repositories this pass.

## Suite

`test_tree_reach.sh` — **`24`/`24`**, offline, over the two pure predicates. The cases are the
rows `P441` and `p140` published as having **defeated** earlier lists (`LICENSE.TXT`,
`package/license`, `aoe-web-frontend/LICENSE`, `COPYING.txt`, `docs/License.txt`,
`NOTICE.txt`) — the external reference `P417` requires, not fixtures echoing the author.

🔴 **The suite refuted v1 of this instrument on its second case class.** v1 matched licence
texts by **basename**, so it could not see the REUSE/SPDX convention `LICENSES/<SPDX-ID>.txt`
— the basename there is the SPDX id, not the word *licence*. v2 added a directory rule; the
suite then refuted v2 on `licenses/README.md`, prose inside a `LICENSES/` directory. v3
excludes the directory's own prose and passes `24`/`24`. 🔵 **Recorded because `P441`'s lesson
is exactly this: my first two attempts were both list-widenings of my own.**

## Open limbs for p197

| action | 🟢 limb `1` | 🔴 limb `2` |
|---|---|---|
| Read the `3` root hits' bytes and classify the family | they are real grants → the shelf's licensed count rises by `3` and `16.2`% falls further | they are templates or stubs → `Gap 421`'s class absorbs them |
| Re-read p195's *"interoperability layer grants nothing"* row by row against `Lumi`'s `15` texts | the layer does grant, per row → retract the layer claim | the `15` are vendored or non-grants → the claim survives on better evidence |
| Promote the `19`-name ladder's callers to this tree channel, or record why not | the census is re-runnable tree-wide at `468` scale | the clone channel does not scale to `468` → the ladder stays, with this `13.6`% as its published error bar |
