# `p501` — abstention guard + canonical re-resolution

Two instruments, each closing one gap `p499` left open, each validated against a known-good **and**
a known-bad input before its results were used (`Gap 498-M`'s rule).

| script | closes | what it decides |
|---|---|---|
| `grade_abstain.py` | **`Gap 499-B`** | whether a licence payload may be **labelled at all** |
| `reresolve_canonical.py` | **`Gap 499-D`** | whether the retained canonical set still *is* what the manifest says |
| `fetch_lic.sh` | — | resolves a payload at a pinned SHA over the `raw.githubusercontent.com` gate |

Both print `rows_in` / `rows_out` and an explicit `ASSERT` line (`Gap 498-L`).

## `grade_abstain.py` — the guard is one clause

`p499` fed [`Wakoma/nimble`](https://github.com/Wakoma/nimble)'s **CERN-OHL-S-2.0** payload — a
licence **outside** the retained set — to a nearest-neighbour matcher and got back
`BSD-2-Clause, −90/+1947`. A grader with no way to decline will label anything put in front of it,
and a wrong family label on a shelf row is read by an engagement as a legal fact.

```
rel = (insertions + deletions) / canonical_operative_words
label   if rel <= BAND          # BAND = 0.15
ABSTAIN otherwise, naming the nearest family and its rel
```

It also carries **`p500`'s rule**: grade against *every* retained form of a family and keep the
**best** match, so the two legitimate Apache-2.0 forms cannot manufacture a phantom `−19`.

### Validation — the controls matter more than the results

| input | class | result |
|---|---|---|
| `Wakoma/nimble` `LICENSE.txt` (CERN-OHL-S-2.0, 13 419 B) | **known-bad** | 🟢 `ABSTAIN`, nearest `LGPL-3.0-only`, `rel=1.27` |
| `GeminiLight/SocialCoach` `LICENSE` (11 358 B) | **known-good** | 🟢 `Apache-2.0`, `0/0` |
| canonical `MIT.txt`, unmodified | identity | 🟢 `MIT`, `0/0` |
| canonical `MIT.txt` **minus the warranty clause** | **over-abstention control** | 🟢 still `MIT`, `rel=0.079` |

The last row is the one that makes the guard worth having: a band that refuses everything unfamiliar
is not a guard, it is a broken grader. A 13-word deletion inside MIT still labels **MIT**, and
carries its residual forward for a human to read.

🔴 **What the guard does not do.** `ABSTAIN` is not an identification. It says *"not any licence
this base holds a canonical for"* and nothing more — `nimble` is CERN-OHL-S-2.0 because its own
title block says so, not because this instrument worked it out. `BAND = 0.15` is **chosen, not
derived**; the controls show it separates these inputs, not that it is the right number
(`Gap 501-B`).

## `reresolve_canonical.py` — two checks, because the gap asked for the weaker one

`Gap 499-D` asked for *"one assertion per pass"* that the retained set has not drifted. A pinned URL
carries a commit SHA and **cannot** drift, so re-fetching the pin proves only **retention**.
Upstream **amendment** — the failure the set was built to catch — is visible only by reading the
*same path* at the publisher's **current** ref:

```
check A (retention)  pinned URL -> bytes + git blob SHA-1  ==  MANIFEST.tsv
check B (amendment)  HEAD URL   -> operative words         ==  pinned operative words
```

| run | result |
|---|---|
| live, 12 manifest rows | 🟢 **A: 12/12 PASS.** 🟢 **B: 11/11 PASS** (the apache.org row is not an SPDX path and is skipped) |
| negative control, 2 expectations tampered | 🟢 **A reports `DRIFT` on exactly those rows**, PASS elsewhere |

🔵 `spdx/license-list-data` HEAD resolves to **`f715b3660bb164c3d0b81cba9ce94e3c558c4048`** — the
very commit `p499` pinned. The pin **is** the publisher's current state, so check B is *true today
and vacuous today*: it establishes the oracle, it has not yet been tested against a real amendment.

### Two defects this instrument found in its own first run, both in the base

🔴 **`MANIFEST.tsv`'s last column is documented as a URL and does not always contain one.** The
`Apache-2.0.apache-org` row reads
`https://www.apache.org/licenses/LICENSE-2.0.txt (apache.org, the steward itself)` — URL plus
prose. Reading `$NF` as a URL yields `UNRESOLVED(0)`, which the first run reported as
*"Apache-2.0 is now single-sourced too"*. **It is not** — `www.apache.org` answered `200` on 3/3
direct probes. The instrument now parses the first whitespace-delimited token. 🔵 **A
"source unreachable" result is a claim about the fetcher before it is a claim about the world.**
Registered as `Gap 501-D`.

🔴 **This script's own year regex never compiled.** `\b(19|20)\d\2?\d` carries an invalid group
reference; it was never reached because the `(c)`/`©` test short-circuits first on every payload in
the set. Corrected to `\b(?:19|20)\d\d\b`, re-run, **output identical**. 🔵 A latent branch that
produces the expected answer by never executing is the failure mode `p499`'s README named: *a
plausible number is the expected number.*

🔴 **Operative word counts here are NOT comparable to `p499`'s or `p500`'s.** The cut is a
re-implementation, not their code — this base reads Apache-2.0/SPDX as **1408** operative words
where `p499` recorded 1426 and `p500` 1431. Only the *within-run* deltas (pinned vs HEAD,
payload vs canonical) are valid. 🔵 Three instruments, three counts, one licence: the number is an
artefact of the cut, which is why no shelf should ever quote it as a property of the licence
(`Gap 501-C`).

## Running them

```sh
python3 -I reresolve_canonical.py ../../evidence/canonical/MANIFEST.tsv main out.tsv
python3 -I grade_abstain.py ../../evidence/canonical in.tsv out.tsv   # in.tsv: name<TAB>local_path
```

🔴 Neither is gate-attested: `make hooks` was not run (`Gap 446-A`, **25 passes**).
