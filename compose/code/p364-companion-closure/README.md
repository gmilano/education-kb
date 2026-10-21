# `p364-companion-closure` — `ACTION ZZ-bo`: the dependency closure of a shelved platform

**Pass 364 · 2026-10-21.**

## Why it exists

🔴 **Every grant instrument on this base takes ONE repository's bytes.** `p362` proved that
is not enough with `QingdaoU/OnlineJudge` — **MIT** in the headline, **SATA** in the two
components that execute student code, **no grant at all** in the documented deploy
repository — and opened `ACTION ZZ-bo` with its scope recorded as *unmeasured*.

## What it measures

- `companion_closure.py` — the extractor. Given a README payload and the row's own slug, it
  returns every shape-valid GitHub address the README names **except the row itself**, each
  tagged `SAME-OWNER` (the component candidate) or `THIRD-PARTY`. Addresses are folded and
  shape-filtered through `p351-address-shape`, **imported, never reimplemented**.
- `probe_companions.sh` — the online leg: `ls-remote --symref` for the default ref, a
  case- and extension-closed README ladder over `raw.githubusercontent.com`, then the
  extractor. One platform row per invocation, so a single failure cannot poison the sweep.
- `test_companion_closure.py` — **20 offline controls**, wired into `HOOK_GATES` as
  `gate-companion-closure`.

## What it found (2026-10-21)

**60** platform rows → 60 live, 60 with a README → **25 (41.7 %) name a companion** → **91
edges** (46 `SAME-OWNER`, 45 `THIRD-PARTY`) → 🔴 **72 absent from 2 550 addresses** = **69
distinct repositories**, graded from payload: **33 permissive**, **19 copyleft-or-worse**,
🔴 **12 with no grant at any probed path**, **3 that are not addresses at all**.

Headline shelf correction: `openfun/marsha`, published **MIT / reach None**, has a
same-owner component at **AGPL-3.0**.

## 🔴 Two limits, stated

1. **The edge has no DIRECTION** (`ACTION ZZ-bs`). *Named in a README* over-collects:
   `judge0/judge0` names 20 third-party repositories and **19 are adopters, not
   dependencies**. The `SAME-OWNER`/`THIRD-PARTY` column is enough to refuse promotion to a
   component and **not** enough to grade exposure. The manifest is the discriminator.
2. **A grant read here is read at a BRANCH** (`ACTION ZZ-br`). `davidjbradshaw/iframe-resizer`
   is **GPL-3.0-or-commercial** at `master` and **MIT** at `v3.5.13`. This instrument does
   not read tags, and neither does any of this base's 299 grant claims.
