# `p247-mit-tier-sweep` — `ACTION XB`: re-read the `MIT` tier's grants first-hand

`make gate-mit-tier` · **needs egress**, so it is NOT in `make hooks` · harvester only, no
classifier of its own (`P237`: it fetches and records; `lib/license_family.sh`,
`p246-payload-integrity` and `p247-keyed-grant` decide)

## The budget `ACTION XB` was written with was wrong

> *"the `2 762` `MIT` cells … the `MIT` tier is `9`× larger and has never been swept …
> Budget: ~`2 700` requests at `1` per slug — larger than `ACTION SK`'s, so split by rank
> across passes"*

Measured before spending one request: **`2 801` CELLS are `881` DISTINCT SLUGS.** The same
repository appears on up to eight shelves. **A cell is not a request**, the whole tier fits in
one pass, and no split was needed.

## What it measured

| | |
|---|---|
| distinct `MIT` slugs | `881` |
| payloads READ | **`821`** |
| `UNREAD` | **`60`** — 5 names × 2 **guessed** refs. **Not an absence** (`ACTION UK`) |
| cells CONFIRMED by their payload | **`805`** = `98.05`% |
| cells DISAGREEING | **`16`** = `1.95`% |
| `CONFLICTED` payloads | **`0`** — p246's `1`-in-`321` merge-conflict rate does **not** reproduce |
| source-available / non-commercial | **`3`** (`BUSL`, `fair-code`, `CC-BY-NC-SA-4.0`) → **`ACTION XB` limb `1` fires** |

Headline: **`sdv-dev/sdv` is `Business Source License 1.1`** (Licensor: DataCebo, Inc.) and was
published here as `MIT`. Before p247's hoist the shared classifier answered `MIT`/`ALLOWED` on
that payload; it now answers `BUSL`/`DENIED`. Measured both ways against a kept pre-hoist copy
of the classifier — which is also how the `leemonade/leemons` row was **withdrawn** from the
hoist's credit: it already read `FAIRCODE` before the change, so its `MIT` cell was simply a
wrong published cell.

## What this sweep deliberately does NOT do

It does not run `git ls-remote`, so **the ref is a guess** (`main`, then `master`) — the state
`p229` built its ref axis to eliminate. A repository whose default branch is `develop` or
`trunk` comes back `UNREAD`. `HeliumEdu/platform` is the proof: default branch `develop`, the
ladder reads it, this sweep does not. **`ACTION XH` (registered p247) holds those `60`**, to be
run through the ladder rather than the sweep.

The omission travels with the data: the denominator of every rate above is **payloads read**,
never slugs.

## Usage

```bash
make gate-mit-tier                                   # harvest the slug list, then sweep
compose/code/p247-mit-tier-sweep/sweep.sh slugs.txt out/ 12   # directly, 12-way parallel
#   → slug  READ    <ref>  <path>  <bytes>
#   → slug  UNREAD  -      5-paths-x-2-guessed-refs  -
```
