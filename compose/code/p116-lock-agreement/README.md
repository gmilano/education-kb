---
industry: education
region: Global
updated: 2026-10-11
---

# `p116-lock-agreement` — a lock that reaches the manifest is not yet a lock that matches it

**Pass 116, 2026-10-11.** Second pass of this date. Census window
**2026-10-11 02:18 UTC → 02:33 UTC** (main run 02:18–02:23, then two controls).
The Gap 404 re-measurement ran 02:33–02:37 over all 296 addresses.

🟢 **`test_p116.sh` — 113 passed / 0 failed**, fully offline: real git repositories
committed on disk and served to the real `agree.sh` over `file://`. No mocks, no
network, no `api.github.com`.

🟢 **`agree.sh` read 134 of 134 addresses, `rc=0` on every one, zero `UNREAD`** — plus
**two full control runs** over the same 134, so both of this pass's exclusion rules are
measured rather than asserted.

## Why this axis, and why now

p114 closed by naming what its own figure still hid, in the trend table it published:

> | reach | p114 | 34.5 % `full-reach`; 76.1 % of manifests reached |
> | | | **what the figure hides: whether the pinned versions are any good** |

"Any good" has three halves and only one of them is decidable here. Whether a pinned
version is **current** needs a registry; whether it is **secure** needs an advisory feed.
Neither is on this channel (`P116-D`). But whether the lock and the manifest even
describe the **same dependency set** is decidable from committed bytes alone — and it is
the half with a hard failure mode:

```
npm ci does not install a stale lock. It exits 1 and installs nothing.
```

So p114's rows whose root manifest is reached are not yet rows that *build*. This pass
measures how many of them a resolver would actually accept.

Ninth axis in nine passes, fifth read from the TREE.

## The headline

| figure | value |
|---|---|
| denominator — p114 rows with a lockable root manifest a lock REACHES (`P116-A`) | **134** |
| rows where agreement is **decidable** from the root pair | **64** |
| rows where it is not (root manifest outside npm/composer/cargo) | 70 |
| declared dependencies compared | **3 100** |
| declared dependencies **present** in the reaching lock | 🟢 **3 100** |
| declared dependencies **missing** | 🟢 **0** |
| rows at `agree` | 🟢 **64 of 64 (100 %)** |
| rows at `drift` | 🟢 **0** |

🟢 **Where this shelf has a lock that reaches the manifest, the lock matches the
manifest. On this axis the shelf is clean — and it is the first axis in nine of which
that is true.**

## The result is a measurement, not an empty code path

A census that reports zero of the thing it looks for has to prove it could have found it.
This one does, twice.

| control | what it changes | result |
|---|---|---|
| `P116_PEER=1` | counts `peerDependencies`, which npm does **not** require in the lock tree | 🔴 **1 row drifts** — `thu-maic/dsh-openmaic`, declared 7 → 15, **7 missing** |
| `P116_NO_DEV=1` | drops `devDependencies` / `require-dev` | declared 3 100 → **1 902**; still **0 missing** |

The positive control emits `drift` on real shelf data through the same code path, so the
zero in the main run is a finding about the shelf. The second control shows what the zero
covers: **1 198 of the 3 100 compared dependencies (38.6 %) are dev-only**, and the locks
account for those too.

## What it cost to get a trustworthy zero — the part worth reading

🔴 **This axis produced THREE false `drift` findings before it produced a true zero, each
from a different real convention of the npm ecosystem.** Every one of them named a
prominent row, and every one would have been published as a defect of the repository.

| # | the convention | what the naive reading did | rule |
|---|---|---|---|
| 1 | yarn and pnpm **are** npm locks | called 22 rows "no lock at root" when they carry `yarn.lock` / `pnpm-lock.yaml` | `P116-I` |
| 2 | **yarn** keys an alias under the **alias** — `codemirror-v5.17.0@npm:codemirror@5.17.0` | split on the last `@`, so every aliased dep read as missing — hit `oppia/oppia` and `instructure/canvas-lms` | `P116-K` |
| 3 | **pnpm** keys an alias under its **target**, recording the alias only under `importers:` | read `packages:` alone and called `@typescript/native` missing — **the single `drift` row of the first clean census, on `PrairieLearn/PrairieLearn`** | `P116-Q` |
| 4 | a **workspace-local** dependency is absent from the lock **by design** | read `@instructure/canvas-media` and `@instructure/ready` as missing on `canvas-lms` | `P116-L` |
| 5 | an **empty** lock is not total drift | a zero-byte lock sniffed to the yarn grammar and read as *every* dep missing — the most alarming verdict the axis can emit, from a file that says nothing | `P116-N` |

🔵 **Four of the five were caught by reading a repository by hand. The fifth (`P116-N`)
was caught by the suite.** Items 2, 3 and 4 are not bugs in a parser so much as three
mutually inconsistent conventions for the same fact, and an instrument that models none
of them reports drift on the shelf's biggest monorepos.

🔴 **The transferable warning: a supply-chain gate that compares a manifest to a lock by
name will report false defects on aliased and workspace-local dependencies unless it
models all three conventions — and the false positives land on exactly the large,
well-maintained repositories a studio is most likely to adopt.** That is the finding of
this pass that generalises past this shelf.

## Disciplines

| | |
|---|---|
| `P116-A` | **Denominator.** p114's result TSV, rows with `lockable_man > 0` **and** `root_orphan == 0`. Rows p114 already failed are not re-failed here: this axis is a tightening of p114's positive class, not a new census of the shelf. |
| `P116-B` | **Root-only is not a shortcut.** The root manifest has no ancestor, so the only lock that can reach it is a lock **at** the root. Reading the root pair is p114's `root_orphan == 0` condition re-read, not a narrower sample of it, and the suite asserts that a drifting manifest in a SUBdirectory does not move the verdict. |
| `P116-C` | **Names, not versions.** A resolver fails closed on a name absent from the lock; a version that has drifted still installs. The name set is also the only part decidable from committed bytes, which is why this axis runs offline at all. |
| `P116-D` | **Declared out of scope.** Version currency and known vulnerabilities need a registry and an advisory feed. Neither is reachable on this channel. Not measured, not estimated. |
| `P116-E` | `peerDependencies` excluded — npm does not require them in the lock tree. Measured by the positive control: the exclusion suppresses exactly **1** row. |
| `P116-F` | composer platform pseudo-packages (`php`, `hhvm`, `ext-*`, `lib-*`, `composer-*`) excluded — they have no lock entry by design. |
| `P116-I` | All three npm lock flavours count: `package-lock.json` / `npm-shrinkwrap.json`, `yarn.lock`, `pnpm-lock.yaml`. |
| `P116-J` | Non-registry specs (`workspace:`, `link:`, `file:`, `portal:`, relative paths) excluded — nothing fetches them. |
| `P116-K` | yarn keys an alias under the alias; `@npm:` is split before the last `@`. |
| `P116-L` | A workspace-local dependency is one whose name is the `name` of another `package.json` **in this tree**. Read from the tree, never glob-matched against the `workspaces` field, because the globs are not required to be accurate and the names are. |
| `P116-M` | Lock flavour is decided by the file's **bytes**, with the basename as a hint only. Dispatching on the name alone made the grammar untestable except through fixtures named exactly like the real thing. |
| `P116-N` | An empty or whitespace-only lock is its own verdict, never drift. |
| `P116-O` | Workspace names are resolved **lazily**, only for a row that already shows drift. Doing it eagerly fetches every sub-manifest in every tree — `canvas-lms` has 596 — and the first draft managed **3 rows in four minutes** before it was restructured. |
| `P116-Q` | pnpm keys an alias under its **target** in `packages:` and the alias under `importers:`; both blocks are read, and nothing outside them is, because junk in the `have` set can only ever **mask** real drift. |
| 🔴 `P116-R` | **STATED ERROR, in this pass's own figures.** npm name extraction takes the segment after the last `node_modules/`, so a package present only as a NESTED install credits a top-level declaration. The error direction is one-way: it can only ever make a row read **more** agreeable. **Every figure here is therefore a LOWER bound on drift**, said here rather than discovered later. |

## `P116-P` / Gap 404 — closed, and p114's sizing was exact

p114 opened `Gap 404`: the anchored requirement-file rule
`^requirements([-_.]<suffix>)?\.txt$` — carried in **two** copies, p112's `manifests.awk`
and p114's `positions.awk` — refuses the prefixed half of its own convention
(`dev_requirements.txt`, `latest_requirements.txt`, `system_requirements.txt`). p114
sized it (198 files seen, 8 missed, 5 rows affected, **exactly one verdict**) and
deliberately did not fix it, because `P237` forbids forking a shared classifier.

This pass fixed it where the rule lives. [`lib/reqname.awk`](../lib/reqname.awk) now holds
**one** definition, widened to
`^([a-z0-9._-]+[-_.])?requirements([-_.][a-z0-9._-]+)?\.txt$`, loaded by both passes with
a second `-f`. `lib/test_reqname.sh` — **22 passed / 0 failed** — pins every case,
including the `myrequirements.txt` exclusion that stops the prefix group swallowing any
word ending in the literal string.

Neither consuming pass regressed: **`test_p114.sh` 98 / 0** and **`test_p112.sh` 109 / 0**
against the shared rule.

🟢 **Re-measured over all 296 addresses, p114's prediction holds to the file and to the
verdict:**

| p114 figure | as published | 🆕 restated | delta |
|---|---|---|---|
| rows at `full-reach` | 102 (34.5 %) | 🟢 **103 (34.8 %)** | **+1** |
| lockable manifests | 2 135 | **2 143** | **+8** — the 8 missed files, exactly as sized |
| manifests reached | 1 625 (76.1 %) | **1 633 (76.2 %)** | +8 |
| manifests orphaned | 510 (23.9 %) | **510 (23.8 %)** | **0** |
| rows whose ROOT manifest is orphaned | 88 | 🟢 **87** | **−1** |
| rows that moved | — | 🟢 **`sdv-dev/sdv` `no-reach` → `full-reach`** | exactly one |

🔵 **The orphan count does not move at all**: all 8 newly-visible files are pins that
*add* coverage, so the numerator and denominator rise together. That is the direction
`lib/reqname.awk` predicts in its own header — widening can only add a file the old rule
refused — and it is why no row lost a verdict it held.

Evidence: `result-P116P-REQNAME-RESTATED-2026-10-11.tsv` (296 rows, from p114's own
`reach.sh` under the widened shared rule). p114's committed
`result.2026-10-11.tsv` is left untouched as the historical record, and the narrow rule
is kept verbatim in `positions.PRE-P116-CONTROL-2026-10-11.awk` and
`manifests.PRE-P116-CONTROL-2026-10-11.awk` so the delta is reproducible.

## Channel, probed live this pass

| lane | result |
|---|---|
| `git ls-remote` / `git fetch` → github.com | 🟢 `rc=0` |
| `raw.githubusercontent.com/<slug>/<ref>/…` | 🟢 `200` |
| `api.github.com` | 🔴 `403` (unchanged since `P107-A`) |
| `github.com` HTML | 🔴 `403` |
| 🔴 **every non-GitHub domain, `curl` **and** the fetch tool** | 🔴 **`ENOTFOUND`** |

🔴 **The last row bounds what this pass may claim.** Repository facts are verified on the
git lane, which works. **Non-GitHub URLs could not be probed at all**, so no page written
this pass presents a non-GitHub link as verified; those sources are named in prose
instead, with the search that produced them recorded in `intel/market.md` under `P116-M`.

## Files

| file | what it is |
|---|---|
| `agree.sh` | the census driver: fetch, root pair, batched lazy blob read, worst-wins per row |
| `agree.py` | the comparator — one ecosystem's manifest against one reaching lock |
| `wsnames.py` | one process for a whole tree's sub-manifest `name` fields (`P116-O`) |
| `addresses.txt` | the 134-row denominator, derived from p114's result per `P116-A` |
| `orgs.region.tsv` | p112's committed regional map, carried unchanged (`P112-L`) |
| `test_p116.sh` | 113 tests, fully offline, real git repos over `file://` |
| `result.2026-10-11.tsv` | the census |
| `result-PEER.POSITIVE-CONTROL-2026-10-11.tsv` | `P116_PEER=1` — the positive control |
| `result-NODEV.CONTROL-2026-10-11.tsv` | `P116_NO_DEV=1` — the dev-dependency contribution |
| `result-P116P-REQNAME-RESTATED-2026-10-11.tsv` | p114's reach census under the widened shared rule (296 rows) |

## Reproduce

```sh
cd compose/code/p116-lock-agreement
./test_p116.sh                      # 113 / 0, offline, no network
./agree.sh addresses.txt            # the census
P116_PEER=1   ./agree.sh addresses.txt     # positive control
P116_NO_DEV=1 ./agree.sh addresses.txt     # dev-dependency contribution

cd ../lib && ./test_reqname.sh      # 22 / 0, the shared rule Gap 404 closed
cd ../p114-lock-reach && ./test_p114.sh    # 98 / 0, unregressed
cd ../p112-dependency-closure && ./test_p112.sh  # 109 / 0, unregressed
```
