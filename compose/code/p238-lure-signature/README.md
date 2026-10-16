# `p238-lure-signature` — the provenance gate the grant ladder cannot be

**Why this exists.** `p228`–`p237` built an eleven-pass programme establishing that a
licence must be read **first-hand from the payload** and never taken from the GitHub
`license` field. `p238` found that programme's limit: **a deliberately labelled
repository passes a first-hand grant read.**

One query — `FERPA OR COPPA student education in:name,description,readme license:mit
pushed:>2026-06-01` — returned `13` repositories named for real education products
with `Full-Version` / `Unlocked` appended: `Moodle`, `Google Classroom`, `PRONOTE`,
`CmapTools`, `Packet Tracer`, `Stellarium`, `Childsplay`, `Complete Anatomy`,
`Adobe Presenter`, `GeoEnZo`, `WordFox`, `CubeTest`, `DiagramPainter`. Every one
carries `license: MIT`; every one serves a `LICENSE` at `HTTP 200`; every one funnels
its `README` links to a single download host.

> **A grant is a permission. It was never a provenance claim.**

Reading the payload defeats a repository that is *carelessly* labelled. It does
nothing against one that is *deliberately* labelled. The missing predicate is not
about licences at all.

## The four predicates

| # | predicate | fires when | discriminator |
|---|---|---|---|
| 1 | `NAME` | a release-channel word is in the repository name | those words describe a **distribution**; in the name of source they are a category error |
| 2 | `FUNNEL` | ≥`60`% of non-infrastructure external `README` links point at one host (≥`5` links) **that is not the project's own** | registries/CI/badge hosts are excluded as infrastructure |
| 3 | `BADGE` | a **licence** badge is a remote image off both the badge services and the project's own host | a real badge is a `shields.io` *query*; a forged one is a **picture** |
| 4 | `COLDNESS` | `0`★ **and** `0` forks **and** pushed ≤`7`d | 🔴 **corroborating only, never counted toward the verdict** |

`LURE` at ≥`2` substantive predicates · `SUSPECT` at `1` · `CLEAR` at `0`.

**Coldness deliberately cannot convict.** `p238` published `9` genuine rows at `0`★,
several pushed the same day. A gate that downgrades those is worse than no gate.

## The self-host exemption — the one false-positive mode, found and fixed in-pass

Six real projects scored `60`–`93`% link concentration on **their own documentation
domains**: `docs.snath.ai`, `ai-sdlc.io`, `attestix.io`, `arkforge.tech`, and two
`*.github.io` pages. `is_self_host()` skeleton-matches host labels against the owner
and repository name, so `ark-forge` → `arkforge.tech` and `ai-sdlc` → `ai-sdlc.io`
are exempt.

🟢 **It removed all six without weakening either conviction**, because a lure's funnel
host bears no relation to its owner (`rockstar49summer` → `softyne.com`). **That
asymmetry is the whole discriminator.** `11` controls cover it.

## Usage

```bash
python3 -I compose/code/p238-lure-signature/lure_signature.py \
        <owner/repo> <readme-path> [stars] [forks] [days_since_push]
python3 -I compose/code/p238-lure-signature/test_lure_signature.py   # 45 controls
make gate-offline                                                    # standing check
```

Exit `0` on `CLEAR`, `1` otherwise. No network; it reads a `README` from disk.
Runnable from its own directory **and** under `-I` from the repository root
(`p355-cwd-portability` — the reason `p229`'s gate stayed a one-off).

## What was measured, not asserted

| run | result |
|---|---|
| controls | 🟢 `45`/`45`, both invocation paths |
| the two lures, `README`s read first-hand (`11 604` B, `10 722` B) | 🔴 `LURE`, all four predicates, `100`% of `18`/`24` links on `softyne.com` |
| `p238`'s own `43` published rows | 🟢 `43`/`43` `CLEAR` — zero false positives |
| every slug on every shelf (`2 188`, `NAME` predicate, offline) | 🟢 `2` hits, both the lures this pass documents |

## What it does not do

🔴 It cannot see a lure with a plausible name, spread links and a `shields.io` badge.
🟡 `ACTION VE` keeps the online limb open: `FUNNEL` and `BADGE` over all `2 188`
shelf slugs needs `2 188` `README` fetches and has not been run.
