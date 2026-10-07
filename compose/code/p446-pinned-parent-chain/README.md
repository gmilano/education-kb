---
industry: education
region: Global
updated: 2026-10-07
---

# `p446-pinned-parent-chain` — the depth-2 edge set has an unstated parameter, and it is worth 3.4×

**P446: when a measurement walks a chain, every leg's version is a parameter. A chain
with one leg unstated is not reproducible — and here that one leg moves the answer 3.4×.**

## The disagreement

`p442-depth2-pinned` answered pass 25's action B and published **334.5 d** against depth
1's 220 d, concluding *"the ladder is monotone on both axes"* — **trend 63**.

🔴 **The same question, with one leg changed, gives 97 d.** The ladder is not monotone;
depth 2 is **younger** than depth 1.

## The two chains, and the one line that differs

Both resolve the depth-2 **specifier** identically — both import `p437`'s resolver, so
the second leg is the same code. They differ on **whose dependency list the specifier
is read from**:

| | first leg | endpoint |
|---|---|---|
| `p442` | the depth-1 package's **latest** release | `info.requires_dist` · `versions[dist-tags.latest]` |
| **`p446`** | the depth-1 package's **pinned** version | `/pypi/<name>/<PINNED>/json` · `versions[<PINNED>]` |

🔵 **A build installs the pinned depth-1 package, so the dependency list it installs is
the pinned one's.** `p437` had already resolved those pins. Reading `latest`'s list
describes a tier that is installed only where a pin happens to equal latest — which
`p437` measured at **62%**.

🟢 **So for the question as pass 25 wrote it — *"date the pinned depth-2 tier"* — the
pinned-parent chain is the faithful one.** `p442`'s number answers a different and also
real question: *"how old would the current depth-1 releases install?"* **Neither is
wrong. Quoting either without naming the parent version is.**

## Measured, 2026-10-07, reference date passed explicitly

**990 rows: 891 resolved, 99 parents declaring no runtime dependencies, 0 unreadable.**

| | `p442` (latest parent) | **`p446` (pinned parent)** |
|---|---|---|
| rows | 344 edges / 276 pkgs | **891 edges / 410 pkgs** |
| **median pinned age** | **334.5 d** | 🟢 **97 d** |
| mean pinned age | — | 571 d |
| `EXACT` share | 21% | **11%** |
| `EXACT` median | 49 d | 🔴 **1,553 d** |
| `CAPPED` share | 56% | **58%** |
| `CAPPED` median | 🔴 **694 d** | 62 d |
| pin == latest | — | 718 of 891 (**81%**) |

### 🔴 The two instruments disagree about WHICH CLASS carries the staleness, and both are right about their own corpus

- With **latest** parents, the `CAPPED` rows are current libraries' wide ranges, which
  resolve to the newest release **under a cap that may itself be years old** — 694 d.
- With **pinned** parents, the `CAPPED` rows mostly resolve to **current** releases
  (62 d), because the cap is satisfied by today's version — while the `EXACT` rows
  become catastrophically old (**1,553 d ≈ 4.3 years**), because **an old pinned parent
  exact-pins whatever was current when it shipped**.

🔵 **So the headline reverses with the parameter.** `puppeteer-core` pinned at **13.5.0**
(2022) contributes **24** of the 100 `EXACT` depth-2 rows and drags in `rimraf 3.0.2`
(**+2,199 d** behind its own latest), `https-proxy-agent 5.0.0` (**+2,313 d**) and
`pkg-dir 4.2.0` (**+2,207 d**). `puppeteer-core` **at latest** contributes none of it.

⚠️ The single oldest install reachable from this shelf is `wicked-good-xpath 1.3.0` at
**3,841 d — 10.5 years**, through a **pre-release** parent
(`speech-rule-engine 5.0.0-alpha.8`) on the math-speech, and therefore the
**accessibility**, path.

🟢 **`popper.js 1.16.1-lts` reproduces `p437`'s single exception at depth 2**: a pin
**newer** than the latest stable (2,375 d against 1.16.1's 2,450 d). The same class,
independently reached.

### What this means for the closure

🔵 **Depth 1 remains the number to quote, and now for a reason that survives either
chain.** Under `p442`'s chain depth 1 is the *younger* tier and under this one the
*older*, so **depth 1 is the only tier both agree is worth measuring** — and it is the
one a client's manifest actually controls. ⚠️ **What does not survive is trend 63's
monotone ladder**, which holds only for the latest-parent chain and is corrected in
place in `intel/trends.md`.

## Scope, inherited from `p438`/`p442` so the three stay comparable

- **Runtime dependencies only.** `extra == "..."` markers, npm `devDependencies`,
  `peerDependencies` and `optionalDependencies` excluded. ⚠️ This is the exclusion that
  most affects the headline: dev dependencies are numerous and freshly ranged, so
  counting them would pull the median **down** and manufacture this result. Control:
  `test_only_the_dependencies_field_is_read`.
- **Markers other than `extra` are kept.**
- **Depth 2 means "required by a pinned depth-1 package"**, not the transitive closure.
- ⚠️ **Edges, not distinct packages.** 891 rows over 410 distinct names: a package
  reached from two parents is counted twice, because it is installed under two
  different constraints. `p442` deduplicated to packages. **That is a second, smaller
  difference between the two instruments, and it is stated rather than reconciled
  away** — it cannot explain a 3.4× gap, since the duplicated rows are the
  freshly-`CAPPED` ones and dropping them would move the median *up*, not down.

## Run

```sh
python3 test_parent_chain.py                                              # 25/25, offline
python3 -I parent_chain.py ../p437-pinned-version/result.2026-10-07.tsv 2026-10-07
```

The reference date is a **required argument**, never `today()`, so every age reproduces.
Two controls assert the claim itself: `test_it_diverges_from_p442_and_the_cause_is_the_FIRST_LEG`
(if the two ever agreed, the parameter would not be load-bearing) and
`test_the_second_leg_is_SHARED_so_only_the_first_can_explain_it` (both import `p437`'s
resolver, so the specifier logic cannot be the cause).
