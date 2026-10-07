---
industry: education
region: Global
updated: 2026-10-07
---

# `p438-depth2-closure` — pass 25's action B: depth 2 doubles the closure and adds no new licence class

**Executes pass 24's pre-registered action B**, written as:

> Extend the closure to **depth 2** and date it, the hypothesis the closure's own README
> pre-registered.
> **Prediction:** expect the copyleft **count** to rise via `certifi` (MPL-2.0) but **no new
> copyleft class**; if no new class appears, depth 1 was sufficient and the gap closes.

## What it reads

The same two endpoints as depth 1 — **no new channel**:

```
pypi.org/pypi/<n>/json     -> info.requires_dist           (PEP 508 strings)
registry.npmjs.org/<n>     -> versions[latest].dependencies
```

Classification is delegated to `../dependency-licence-closure/dep_licence.py` and dating to
`../registry-recency-channel/registry_recency.py`: rule 1 of **P126** forbids re-deriving what
the repository already versions.

### Scope, stated because it bounds every figure below

- **Runtime dependencies only.** A PEP 508 string carrying `extra == "..."` is **optional** —
  `pip install requests` does not install it. npm `devDependencies`, `peerDependencies` and
  `optionalDependencies` are excluded for the same reason. Counting them would describe an
  installation nobody performs.
- **Markers other than `extra` are kept.** `python_version` and `sys_platform` dependencies do
  install on some machines, and a licence obligation that binds only on Windows is still an
  obligation.
- **Depth 2 means "required by a depth-1 package"**, not the transitive closure. Depth 3 is not
  measured and nothing here says anything about it.

## Measured, 2026-10-07

Input: the **268 distinct depth-1 names** resolved by `../p437-pinned-version`.

| | Depth 1 | **Depth 2 (new names only)** |
|---|---|---|
| distinct packages | 268 | 🔵 **276** |
| `PERMISSIVE` | — | **273** |
| `WEAK-COPYLEFT` | — | **2** |
| `STRONG-COPYLEFT` | — | 🟢 **0** |
| `NONCOMMERCIAL` | — | 🟢 **0** |
| proprietary | — | 🟢 **0** |
| `UNKNOWN` | — | **1** |

🔵 **The closure doubles: 268 declared, 276 more one level down.**

🟢 **No new licence class appears at depth 2, so the prediction's conclusion holds and the gap
closes: depth 1 is sufficient for the licence-class question.**

🔴 **Its mechanism does not.** The prediction named `certifi` (MPL-2.0) as the route. **`certifi`
is a *depth-1* dependency of this corpus**, so it could not raise a depth-2 count. The weak-copyleft
rows that actually appear are:

| Package | Licence | Reached via | Target |
|---|---|---|---|
| `tqdm` | MPL-2.0 AND MIT | `chromadb`, `huggingface-hub` | `towardsai/ai-tutor-app`, `huggingface/smolagents` |
| `mathquill` | MPL-2.0 | `equation-editor-react` | `CAHLR/OATutor` |

Both MPL-2.0 — file-level copyleft, the class already present at depth 1. Neither changes a
build's obligations beyond "do not modify these files in place without publishing the change".

### The `UNKNOWN` bucket resolved 4 → 1, and three of the four were classifier gaps

| Package | Why it read `UNKNOWN` | Resolved |
|---|---|---|
| `glob` (npm) | declares **`BlueOak-1.0.0`** — OSI-approved, permissive, and matched by no rule in `dep_licence.py` | 🟢 PERMISSIVE; rule added with controls |
| `sax` (npm) | same | 🟢 PERMISSIVE |
| `jupyterlab-pygments` (pypi) | its `license` field holds the **licence TEXT**, opening *"Copyright (c) 2015 Project Jupyter Contributors"*; the first 120 characters name no licence | 🟢 PERMISSIVE (BSD, from the classifier); `pypi_licence` now prefers the classifier when the field is text |
| `azure-core` (pypi) | **empty `license`, no `license_expression`, and no `License ::` classifier at all** | 🔴 **stays UNKNOWN — a real gap** |

🔴 **`azure-core` is reached only through `azure-cognitiveservices-speech`** — the single
**proprietary** depth-1 dependency pass 24 found in `oppia/oppia`. Its own transitive layer
publishes no machine-readable grant either. This does not add a new obligation; it adds a second
reason to take pass 24's advice and substitute `k2-fsa/sherpa-onnx` (Apache-2.0).

🔵 **The method point, which is pass 24's rule applied one level down:** `UNKNOWN` is a **parse**
class before it is a risk class. Three of four rows here were permissive all along.

## Dated: each level of the closure is older than the one above it

All on the **latest-release** basis, so the depth-1 column is pass 24's and the comparison is
like-for-like:

| Tier | n | median age | cold > 1 yr |
|---|---|---|---|
| what this KB **cites** (head commit) | 501 repos | **48 d** | 24.8% |
| installed **depth 1**, latest release | 327 rows | **57 d** | 27.2% |
| installed **depth 2**, latest release | 276 pkgs | 🔴 **177 d** | 🔴 **37.0%** |
| *(for scale)* installed depth 1, **pinned** | 327 rows | 🔴 **220 d** | 🔴 42.5% |

⚠️ **The depth-2 figure is a lower bound for the same reason pass 24's depth-1 figure was**: it
dates the latest release, while what a build installs is whatever the depth-1 package's own
specifier allows. **A pinned depth-2 tier is not measured here and would be older.**

Coldest at depth 2: `json-stringify-safe` **4,159 d**, `wicked-good-xpath` 3,841 d,
`mathquill` 3,768 d, `identity-obj-proxy` 3,717 d, `lodash.throttle` 3,707 d, `object-assign`
3,551 d — the npm micro-package layer under OATutor's 2020-era React front end, which is the
same finding `p437` reaches from the other direction.

🔴 **A date is still not a verdict.** `json-stringify-safe` at 4,159 days is eleven lines of
finished code. The dates make a component choice arguable, not automatic.

## The controls (`test_depth2.py`, 13/13, offline)

What this instrument can get wrong is its **scope**, not its arithmetic, so every control is a
scope control and each is paired with the case that must still be **kept**:

| Must be excluded | Must be kept |
|---|---|
| `PySocks; extra == "socks"` | `certifi>=2017.4.17` |
| `chardet; extra == "use-chardet-on-py3"` | `tomli; python_version < "3.11"` |
| `x; python_version < "3.11" and extra == "test"` | `pywin32; sys_platform == "win32"` |
| npm `devDependencies`, `peerDependencies`, `optionalDependencies` | npm `dependencies` of the **latest** version only |

Plus: a package with `requires_dist: null` expands to nothing, and a packument with a dangling
`dist-tag` does not raise.

## Run

```sh
python3 test_depth2.py                                        # 13/13, offline
python3 -I depth2.py depth1-names.2026-10-07.tsv 2026-10-07 > result.tsv
```

## Files

- `depth2.py` · `test_depth2.py`
- `depth1-names.2026-10-07.tsv` (268) · `result.2026-10-07.tsv` (**authoritative**)
