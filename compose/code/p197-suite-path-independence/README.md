---
industry: education
region: Global
updated: 2026-10-14
---

# `p197-suite-path-independence` — the suite whose denominator depended on luck

**Pass `197`, `2026-10-14`.** Runs the action p196 pre-registered in
[`repos/foundations.md`](../../../repos/foundations.md) and in
[`agents/top.md`](../../../agents/top.md): *"make `lib/test_license_family.sh` resolve
fixtures from `${BASH_SOURCE[0]}` and re-run it from `3` directories — if the count is `207`
from every directory after the fix, the class closes; if some assertion is genuinely
CWD-dependent in substance, name it."*

🟢 **Limb `1` fires: `207`/`207` from every form, `0` SKIP, and the class closes.**
🔴 **And p196's diagnosis was wrong in a way that matters.**

## What p196 believed, and what is actually true

| | p196's reading | 🔴 measured here |
|---|---|---|
| the symptom | `207`/`207` from `lib/`, `179`/`181` *"from one directory up"* | **three** different denominators from six invocation forms: `207`, `183`, `163` |
| the cause | the **directory** the suite is invoked from | 🔴 **whether a RELATIVE `dirname` still happens to resolve after the suite's own `cd`** |
| the worst case | `26` assertions vanish | 🔴 **the classifier never loads at all and the suite still prints a total** — `19`/`163` through a symlink |

🔵 **The `cd` on the suite's own header line is what makes a relative `${BASH_SOURCE[0]}`
dangerous.** After it, `$(dirname "$0")/../p560-…` is read from inside `lib/`, so it points
at `lib/p560-…`, which does not exist. 🔴 **But `../lib/test_license_family.sh` from a sibling
directory passes `207`/`207` pre-fix** — `../lib/..` still lands on `compose/code` once the
cwd is `lib/`. **The pre-fix denominator was a coincidence of path arithmetic, not a property
of the directory**, which is why p196 could measure two numbers and infer the wrong rule
from both.

## The pre-fix suite, six forms *(the replica C1 builds, byte-for-byte the old header)*

| form | total | passed | FAIL | SKIP | verdict |
|---|---|---|---|---|---|
| `abs-from-tmp` | `207` | `207` | `0` | `0` | 🟢 `CLEAN` |
| `in-suite-dir` | `207` | `207` | `0` | `0` | 🟢 `CLEAN` |
| `rel-from-par` | `183` | `179` | `4` | `2` | 🔴 `SILENT-SKIP` |
| `rel-from-gpar` | `183` | `179` | `4` | `2` | 🔴 `SILENT-SKIP` |
| `rel-up-sibling` | `207` | `207` | `0` | `0` | 🟡 `CLEAN` **by luck** |
| `via-symlink` | `163` | `19` | `144` | `3` | 🔴 `SILENT-SKIP` — **the classifier is not loaded** |

Committed as [`result.prefix-replica.2026-10-14-p197.tsv`](result.prefix-replica.2026-10-14-p197.tsv).

## The same suite after the fix

| form | total | passed | FAIL | SKIP | verdict |
|---|---|---|---|---|---|
| `abs-from-tmp`, `in-suite-dir`, `rel-from-par`, `rel-from-gpar`, `rel-up-sibling`, `via-symlink` | 🟢 **`207`** | 🟢 **`207`** | `0` | 🟢 **`0`** | 🟢 **`CLEAN` ×6** |

Committed as [`result.2026-10-14-p197.tsv`](result.2026-10-14-p197.tsv).

## The fix, in three parts — and only the first one was pre-registered

1. **The script's own directory is resolved ONCE, to an absolute path, BEFORE the `cd`**, and
   every fixture root hangs off it — including the two (`fixtures-p551`, `fixtures-p613`) that
   were plain relative strings and only worked because of that `cd`.
2. 🆕 **It is resolved PHYSICALLY** (`readlink -f`), because `${BASH_SOURCE[0]}` names the
   **link**, not the file, and `./license_family.sh` is not next to a link.
3. 🆕 **Loading the classifier is now a hard gate**: the `source` is checked, and
   `family_of` is asserted to exist before the first case. Without it a failed `source`
   degrades into `144` failures **and a printed total**, which is a result and not an error —
   `P502`'s shape, one level up from where p196 found it.

🆕 **And the two silent blocks got the canary the other two already had.** `P854` and `T232`
each assert *"fixtures present"*; `P560`/`P561` and `P845` only echoed `SKIP` to stderr. They
now assert it too, so absence costs a **visible FAIL** instead of a quieter denominator. 🔵 It
does not make the run whole — `183` is still not `207` — **it makes it loud.**

## Suite — `test_runner.sh`, `19`/`19`, and four of its five cases are negative

🔴 **A runner that only ever reports `CLEAN` would report `CLEAN` on the defect it was
written to find.** So the cases hand it:

| case | what it is handed | what it must say |
|---|---|---|
| `C1` | a replica of the suite with **the exact pre-p197 header restored** | 🔴 `NOT PATH-INDEPENDENT`, **three** distinct totals, a `SILENT-SKIP`, and `in-suite-dir` still at `207` *(p196's reading, reproduced)* |
| `C2` | a replica with `p173` and `fixtures-p845` **deleted** | 🔴 rejected, **no form `CLEAN`**, and the p197 canaries visible as `FAIL` |
| `C3` | a path that **does not exist** | 🔴 `RUNFAIL` — never `0`, never a pass |
| `C4` | a script that runs fine and **prints no `N/M`** | 🔴 `RUNFAIL` |
| `C5` | 🟢 the committed suite | 🟢 `CLEAN` ×6, one total, `207`, `0` SKIP |

🔵 `C1` is the case that earned its keep: the first replica it built was **half-reverted**
(old paths, new source guard) and answered `RUNFAIL` on all six forms — a mutation that tests
the mutation, not the defect. The second was half-reverted the other way (`FIXP551` and
`FIXP613` left absolute against an undefined variable, so `set -u` aborted the whole suite).
**Only the third reproduces p196's two numbers**, and that is the only version whose verdict
means anything.

## What this recipe does NOT do

🔴 It does not read a licence, and it must not: `P237` forbids touching the classifier's
*logic* on a pass that did not pre-register it. The `207` assertions are p196's, unchanged —
the diff is path resolution, two canaries in `else` branches, and the load gate.
🔴 It does not sweep the other suites in `compose/code/` for the same defect. The mechanism is
now named and the instrument is `run_from_dirs.sh` with `SUITE_UNDER_TEST=`; the sweep is
pre-registered for p198.
