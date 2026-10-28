# `p514-branch-grant-probe` — a licence absence enumerated over BRANCHES, not over one resolved default

🔴 **What it answers.** `Gap 512-D` (`T42`) stated the defect and named its own closure:
*"Every `NONE-OF-N-PATHS` verdict this base holds was computed on one branch and means **unread**,
not **unlicensed**. Closes by re-running the negative verdicts with `git ls-remote --heads`
enumeration first."* This is that re-run.

## The two rules it is built around

- 🔵 **`Gap 509-B` byte rule.** `curl -o` then `wc -c` — **never** `$(curl …)`, which strips the
  trailing newline and makes every byte count exactly 1 low on a newline-terminated payload.
- 🔵 **`Gap 509-B` control rule.** A known-good **and** a known-bad probe gate every verdict. The
  script **exits 2 and publishes nothing** if `HKUDS/DeepTutor HEAD/LICENSE` is not `200` or
  `HKUDS/DeepTutor HEAD/p514_control_absent_xyz` is not `404`. A malformed channel and an empty
  world are then distinguishable, which is `Gap 512-F`'s lesson applied to the raw channel.

## Usage

```
./branch_grant_probe.sh OUT.tsv slug [slug ...]
```

For each slug it enumerates **every** head with `git ls-remote --heads`, then probes **20** licence
paths per head on `raw.githubusercontent.com`. It records only `200`s, plus the control row.

## What it found at `p514`

| | |
|---|---|
| addresses | **19** (the whole negative-verdict population on the live shelves) |
| heads enumerated | **92** |
| paths per head | **20** |
| probes | **1,840** |
| control pair | 🟢 **GOOD `200` 11,408 B / BAD `404`** |
| addresses with a recovered grant | 🔴 **3 of 19** |
| addresses whose nil is now **enumerated** rather than unread | 🟢 **16 of 19** |

🔴 **Three negative verdicts were wrong**, and the two causes are different:

- **`ictinnovations/ICTSchool`** — the genuine **branch** instance. **GPL-3.0**, `LICENSE`,
  **35,149 B**, `sha256₁₆ 3972dc9744f6499f`, on `ictschool-laravel-5.5` **only**; its shipped
  default branch `main` serves no grant at any of the 20 paths.
- **`projectfedena/fedena`** and **`foradian/fedena`** — the **path-set** class (`Gap 501-F`),
  not a branch problem: the grant is on the **default** branch at **`NOTICE`**, a path this base's
  probe never had.

🟢 **The 16 nils are now the strongest this base has published.** `jaltekruse/Free-Math` alone was
probed over **65 heads × 20 paths = 1,300** addresses and serves no payload at any of them.

🔵 **Scope limit, stated rather than implied.** 20 paths at the root plus `docs/`, `doc/` and
`.github/`. It does **not** walk whole trees, so `gate-subtree-grant` (`p382`) is not satisfied by
this instrument and a deep-subtree grant would still be missed.
