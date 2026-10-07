---
industry: education
region: Global
updated: 2026-10-07
---

# `p442-depth2-pinned` — pass 25's action B: the staleness gradient does not stop at depth 1

**Executes pass 25's pre-registered action B**, written as:

> Date the **pinned** depth-2 tier, which this pass measured only at the latest release.
> **Prediction:** expect the depth-2 pinned median to exceed the depth-1 pinned median of **220 d**;
> if it does not, the staleness gradient stops at depth 1 and the closure can stop there for recency
> as well as for licence.

## Why `p438` could not answer it

`p438` needed **names**, to ask a licence question, so it matched the PEP 508 name and discarded the
specifier. Without the specifier there is no pin to resolve — which is why this action needed a new
edge set rather than a re-read of `p438`'s TSV. Resolution, dating and specifier classification are
delegated to `p437-pinned-version` and `registry-recency-channel`: rule 1 of **P126** forbids
re-deriving what the repository already versions. **The only new thing here is the edge set.**

## Measured, 2026-10-07, reference date passed explicitly

**344 `(depth-1 package, depth-2 dependency)` edges over the 268 depth-1 names, 276 distinct depth-2
packages, 344 of 344 resolved, 0 failures.**

🟢 **Prediction confirmed. 334.5 d against 220 d.**

| Tier | basis | n | median | cold > 1 yr |
|---|---|---|---|---|
| what this KB **cites** | head commit | 501 repos | **48 d** | 24.8% |
| installed **depth 1** | latest release | 327 rows | 57 d | 27.2% |
| installed **depth 1** | 🔴 **pinned** | 327 rows | **220 d** | 42.5% |
| installed **depth 2** | latest release | 276 pkgs | 177 d | 37.0% |
| installed **depth 2** | 🔴 **pinned** | 276 pkgs | 🔴 **334.5 d** | 🔴 **48.6%** |

🟢 **The depth-2 latest-release column reproduces `p438`'s published 177 d and 37.0% exactly, on an
independent run.** That is the cross-run control for everything else in the table.

🔵 **The ladder is monotone on both axes and they are roughly additive:** one level down costs about
as much as resolving the pin, and doing both costs the sum. **Nearly half of what a build installs
two levels down is more than a year old.** The number a client is shown is always the one from the
top of that table.

## 🔴 The specifier-class distribution INVERTS between the tiers, and the prediction did not anticipate it

| Class | depth 1 (`p437`) | depth 2 (here) | median pinned, depth 2 | median latest, depth 2 |
|---|---|---|---|---|
| `EXACT` | **159 / 327 = 49%** | **73 / 344 = 21%** | 49 d | 49 d |
| `CAPPED` | 97 / 327 = 30% | **194 / 344 = 56%** | 🔴 **694 d** | 257 d |
| `FLOOR` | 51 | 62 | 71 d | 71 d |
| `ANY` | 19 | 15 | 201 d | 201 d |

🔴 **At depth 1 the effect lived in `EXACT`; at depth 2 it lives entirely in `CAPPED`, and `EXACT`'s
median delta is zero.** The reason is structural: a depth-1 manifest is an **application's**, and
applications pin exactly; a depth-2 specifier is a **library's** constraint on its own dependency,
and libraries publish ranges so that they can be co-installed.

🔵 **This is `p437`'s own warning coming true.** It wrote: *"52% of this corpus is exactly pinned.
That is why the effect is large here and why it would be near zero in a corpus of `>=` manifests.
Quote the class distribution with the ratio or the ratio does not transfer."* **Here is the corpus
where it does not transfer** — same shelf, one level down, and the mechanism changes while the
direction holds.

## The concentration: one depth-1 package owns the coldest pins

| Parent | cold pins > 1 yr | the worst of them |
|---|---|---|
| `react-scripts` | **38** | the CRA layer under `CAHLR/OATutor`'s 2020-era front end |
| `aws-sdk` (v2) | 10 | 🔴 `querystring==0.2.0` **4,964 d** · `url==0.10.3` 4,240 d · `sax==1.2.1` **3,854 d against a latest of 75 d** · `events==1.1.1` 3,759 d |
| `@material-ui/core` | 10 | `@material-ui/types==5.1.0`, 2,340 d |
| `pino-pretty` | 10 | |
| `@nestjs/*` | 8 | `iterare==1.2.1`, 2,314 d, shared by three NestJS packages |

🔴 **`aws-sdk` v2 exact-pins nine packages more than two years old**, and `sax` is the sharpest: it
pins **1.2.1 from 3,854 days ago** while `sax`'s current release is **75 days old** — a **51×** gap,
on an XML parser. 🟢 **Actionable and narrow: move to the modular `@aws-sdk/client-*` v3 packages.**
This is the same OATutor/CRA micro-package layer `p438` reached from the licence direction, so two
independent instruments now name the same component tier.

## 🟢 The NEWER-at-pin exception reproduces at depth 2, in a different ecosystem

`p437` found exactly one row of 327 where the pin is **newer** than the latest stable release:
`oppia/oppia` pinning `webapp2==3.0.0b1`, a pre-release that postdates the last stable. One row of
344 does the same here:

| Parent | Dependency | Pin | Latest stable |
|---|---|---|---|
| `@material-ui/core` | `popper.js` | `1.16.1-lts`, **2,375 d** | `1.16.1`, **2,450 d** |

🔵 **So pass 24's rule — *"every age published is a lower bound on staleness"* — holds in 343 of 344
rows here and 326 of 327 there, and in both corpora the single exception is a SUFFIX-TAGGED release
that postdates the last plain one.** Two independent corpora, two ecosystems, one mechanism: the
exception is structural, not a one-off.

## Reservations

- ⚠️ **A depth-2 pin is a weaker claim than a depth-1 pin.** A depth-1 pin sits in a manifest this KB
  has read. A depth-2 pin is the depth-1 *package's* constraint, and a real solver resolves it
  jointly with every other constraint on the same name — which can only move the chosen version
  **down**. These figures remain **lower bounds**.
- ⚠️ **Manifests, not lock files.** Where a `package-lock.json` or `poetry.lock` exists it is more
  authoritative and is not read here.
- ⚠️ **Depth 2 means "required by a depth-1 package"**, not the transitive closure. Depth 3 is not
  measured and nothing here says anything about it.
- ⚠️ **Runtime only**, identical to `p438`'s scope, so the tiers compare row-for-row.

## The controls (`test_depth2_pinned.py`, 21/21, offline)

What this instrument can get wrong is its **edge set**, not its arithmetic — resolution and dating
carry `p437`'s 47 controls. So every control is a scope or parse control, each paired with the case
that must still be kept, so that a reader returning everything and a reader returning nothing both
fail:

| Must be excluded | Must be kept |
|---|---|
| `PySocks>=1.5.6; extra == "socks"` | `tomli>=1.1.0; python_version < "3.11"` |
| `x>=1; python_version < "3.11" and extra == "test"` | `pywin32>=1.0; sys_platform == "win32"` |
| npm `devDependencies`, `peerDependencies`, `optionalDependencies` | npm `dependencies` of the **latest** version only |
| the environment marker, before the specifier is read | the **specifier**, which `p438` discarded |
| the `[extras]` bracket | the specifier **after** it — `pyjwt[crypto]>=2.8,<3` |

Plus: a dangling `dist-tag` and `requires_dist: null` both expand to nothing without raising; the
name is lowercased for the depth-1 subtraction; `extras-require>=1.0` is not a marker; and an empty
denominator exits **2** (**P355**).

## Run

```sh
python3 test_depth2_pinned.py                                                 # 21/21, offline
python3 -I depth2_pinned.py depth1-names.2026-10-07.tsv 2026-10-07 > result.tsv
```

## Files

- `depth2_pinned.py` — the edge set, with the specifier kept
- `test_depth2_pinned.py` — 21 controls, no network
- `depth1-names.2026-10-07.tsv` (268, `p438`'s) · `result.2026-10-07.tsv` (344) — **authoritative**
