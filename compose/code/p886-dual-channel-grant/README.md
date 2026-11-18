# `p886` — `885-G1`'s acceptance test, executed, scored, and found insufficient

## What this is

`885-G1` (RED, opened by `p885`) requires that **every shelved row carry a licence
verdict from two channels** — the `search/repositories` metadata field **and** the
licence bytes on the `--symref`-resolved default branch — "with disagreement
recorded as a finding rather than resolved toward either side". `p885` checked the
five highest-traffic rows and declared the rest unverified.

`p886` ran it over **all 163 rows** of `agents/top.md`, `repos/foundations.md` and
`verticals/solutions.md`.

## Result

```
population                   163 rows
AGREE                        144   88.3%
BYTES-ONLY (T14)              13    8.0%   metadata abstains; bytes carry a real grant
BOTH-ABSENT                    4    2.5%
DISAGREE                       1    0.6%   RWTH-OS/eduOS-rs
BYTES-UNRECOGNISED             1    0.6%   opendatalab/MinerU (bespoke title + rider)

FIELD-ASSERTS-PAYLOAD-DENIES   0           885-G1's OWN class does not recur on any live shelf row
default-branch disagreement    0 / 163     the symref channel and the metadata channel never differed
permissive share (BYTES)     128 / 163 = 78.5%
```

## 🔴 The two findings that matter, and neither is the one the gap expected

### 1. Eight disagreements: the gate lost 7, the shelf lost 1.

Every disagreement traced to an **instrument** defect, never to a shelf cell:

| Rows | Defect | Shelf already correct at |
|---|---|---|
| `openedx/XBlock`, `openedx/xblock-sdk` | `LICENSE.TXT` (uppercase extension) absent from `p885`'s path list → **manufactured absence** on Apache-2.0, 11,358 B, `sha256₁₂ cfc7749b96f6` | `repos/foundations.md:408-409`, and `:758` already names the trap |
| `portabilis/i-diario` | AGPL-3.0 body in **Portuguese**; English-only titles → abstention | `repos/foundations.md:582` |
| `withmarbleapp/os-taxonomy` | **ODbL-1.0** unknown to the classifier | `agents/top.md:790`, `repos/foundations.md:509` |
| `frappe/education` | 19-byte `license.txt` reading `License: GNU GPL V3` — a declaration, not a body | carried |
| `opendatalab/MinerU` | bespoke title incorporating Apache-2.0 by reference, plus a commercial rider | `agents/top.md:782` |
| `RWTH-OS/eduOS-rs` | **split-FILE** dual grant (`LICENSE-MIT` + `LICENSE-APACHE`); a first-hit ladder reports one half | `repos/foundations.md:666` |

🔴 **An unattended gate of that quality does not verify a shelf; it degrades it.**
Had `885-G1`'s test been run as specified and its output trusted, it would have
published "field asserts, payload denies" — the gap's own error class — against
six correct, byte-sourced cells. **The gate must be at least as good as the shelf
before its disagreements mean anything.** The repairs below close that distance.

🔴 **The eighth disagreement went the other way, and it is the expensive one.**
`OS4ED/openSIS-Classic` is published on three live shelves as *"no detectable
licence at all, treat as all rights reserved"*. Its grant is **GPL-2.0, 17,286 B,
`sha256₁₂ 224ac3d403e3`, at `master/docs/License.txt`** — and
`compose/code/pass275-grant-enumeration/enumeration_gate.py`'s own docstring names
**this repository and this path** as the case the `p275` gate was built on, ~611
passes ago. The gate passes; the shelves carried the false absence regardless. An
instrument error surfaces as a disagreement; a shelf error surfaces as *advice*.
See `886-G5`.

### 2. A clean `AGREE` does not mean the grant is known. Three rows prove it.

Both channels of `885-G1` are **single-valued**: one SPDX identifier, one root
licence file. A real grant can have **arity greater than one**, and when it does,
both channels agree with each other and both are incomplete.

| Row | Both channels say | The grant actually is | Arity |
|---|---|---|---|
| `ECNU/EduWork`, `ECNU/EduWork-ECNU` | `MulanPSL-2.0` | **`MulanPSL-2.0 AND MIT`** | conjunctive, by provenance |
| `sudosylabs/proctor` | `AGPL-3.0` | AGPL-3.0 root + `server/`; **Apache-2.0 `packages/*`**; BSD-3-Clause `server/internal/autocert` | per-directory |
| `iiab/iiab` | `GPL-2.0` | GPL-2.0 default for unmarked files; contributors **encouraged to use LGPL-2+** | per-file |

All four rows scored **`AGREE`**. The test passed them and the test was wrong.

**Exposure, measured:** `19 / 163` rows (**11.7%**) carry a licence-policy document
neither channel reads — `10` × `NOTICE`, `4` × `THIRD_PARTY_NOTICES.md`,
`4` × `LICENSING.md`, `2` × `NOTICE.txt`
([`record`](../../../evidence/licence-policy-docs.2026-11-18-p886.tsv)).

🔴 **And the policy document is not self-verifying either.** `proctor`'s
`LICENSING.md` asserts that *"every comment-capable code … file carries a
human-readable copyright and license notice together with an SPDX license
identifier."* Under `packages/`, **0 of 65 files carry an SPDX identifier**; 6
carry a `Copyright` line and 5 a `Licensed under` line. A third channel made of
prose inherits prose's failure mode.

## The structural fix was already in this repository — which is the finding

Every path-guessing ladder this KB has built — `p213`, `p885`, and the widened one
in `licence_paths.sh` below — fails the same way: it can only find filenames
somebody thought of.

🔴 **`p886`'s first draft called tree enumeration "a channel this KB had never
used". That was wrong, and `make ladder-audit` says so:**

```
91   committed instruments use  git clone --filter=blob:none
104  committed instruments use  git ls-tree
57   of 919 graded ladders are  TREE-ENUMERATED   (919 ladders, 510 instruments)
     compose/code/p215-lstree-grant-recovery/     exists
     make enumerate                               ships since p275
     gate-enumeration      (p275) PASS   "a ladder can only ever refute the paths it tried"
     gate-ladder-case      (p283) PASS   "which path ladders can find an uppercase extension?"
     gate-subtree-grant    (p382) PASS   19 controls
     gate-conjunctive-grant(p427) PASS   24 controls
```

🔴 **`p885` shipped a new 8-path root-only ladder anyway, and it failed in exactly
the two ways those two gates exist to catch. `p886` reused it and inherited both.**
The defect is not missing knowledge — it is 919 ladders across 510 instruments that
no pass reads before adding ladder 920 (`886-G2`).

`/repos/{owner}/{repo}` is `403` here, so REST tree listing is unavailable, but
**a blobless clone is open and exact**:

```sh
git clone --depth 1 --filter=blob:none --no-checkout https://github.com/OWNER/REPO d
git -C d ls-tree -r --name-only HEAD | grep -iE '(^|/)(LICENSE|LICENCE|NOTICE|COPYING)'
git -C d cat-file -p HEAD:packages/vfs/LICENSE     # bytes, no checkout needed
```

On `sudosylabs/proctor` this enumerated **3,288** tracked paths and found every one
of the six licence payloads, including the three in `packages/` that no path list
contained. It is how the per-directory grant above was byte-verified rather than
taken from the policy document's word.

## Files

| File | What it is | Controls |
|---|---|---|
| `grant_titles_x.py` | Iberian (PT/ES) GNU titles, ODbL/ODC-BY, bare-token grants (`-DECLARED` suffix), additional-terms rider | — |
| `test_grant_titles_x.py` | **18 controls, all passing**, incl. `p872`'s measured false-positive set as a regression | `18/18` |
| `licence_paths.sh` | case-complete licence-path ladder (adds `LICENSE.TXT`, `LICENSE.rst`, …) | — |
| `test_licence_paths.sh` | order, duplicate and no-regression controls | `12/12` |
| `classify2.py` | `p228` gate with `p886`'s rows layered on, earliest-title rule preserved globally | — |
| `join_channels.py` | runs and scores the two-channel comparison | — |

Run: `python3 test_grant_titles_x.py && ./test_licence_paths.sh`

## 🔴 What this module does NOT do

It does **not** resolve grant arity automatically. It detects and repairs the
*single-valued* failures and it **measures** the multi-valued ones; deciding that
`EduWork` is `MulanPSL-2.0 AND MIT` required reading a 3,048-byte policy document
in two languages, and no classifier here does that. The honest state is: arity is
now a declared, measured property of `19` rows, and `886-G1` carries the work.
