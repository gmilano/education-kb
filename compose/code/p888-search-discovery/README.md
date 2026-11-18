# `p888-search-discovery` — the re-scoped discovery channel (`887-G4`)

`887-G4` asked for a discovery channel that is not the eight prescribed WebSearch legs, which
nilled for nine consecutive passes. This instrument is that channel.

## What it found that nine passes of legs could not

`api.github.com/search/repositories` **answers `200` in this session.** Every prior pass recorded
star counts as unmeasurable across four routes and concluded *"No star figure appears anywhere in
this KB."* That conclusion was measured against `api.github.com/repos/{slug}` (403), `github.com`
HTML, `gh` CLI on a named repo, and `gh api search/repositories` returning an empty set. **The
search endpoint under `gh api -X GET` with an explicit `-f q=` returns full payloads**, including
`stargazers_count`, `forks_count`, `pushed_at`, `archived`, `fork`, `default_branch` and
`license.spdx_id`.

So this instrument is not only a discovery channel. **It is the first star-count channel this KB
has had**, and the first channel that returns licence metadata and liveness in the same call that
returns the candidate.

## Files

| File | Job |
|---|---|
| `sweep.py` | Sweep 1 — 20 broad legs, `sort=stars`. **Kept as the negative control; see below.** |
| `sweep2.py` | Sweep 2 — 22 precise education-native legs, mostly `sort=updated` |
| `sweep3.py` | Sweep 3 — 14 in-language regional legs, region declared per leg |
| `verify.py` | Byte-reads every licence-ish path per row; families, bytes, `sha256₁₂`, 12-month commits |
| `subsume_test.py` | 9 controls over family detection, including the regression that caught this pass's own defect |

## Two defects this instrument found in ITSELF, both recorded rather than quietly fixed

**1. `sort=stars` over a broad keyword leg does not return education repositories.** Sweep 1's
`lms-ai` leg (`moodle OR canvas OR openedx AI plugin`) matched **23,570** repositories and its
star-sorted first page is `awesome-go`, `gin`, `frp`, `NextChat`. The education signal is in the
**mid-tail**, not the head: of 215 new permissive live rows from sweep 1, **178 carried no
education token at all**. Sweep 2 drops broad `OR` legs and sorts by `updated`.

**2. A bare `learning` token is poisoned, and it is what made defect 1 invisible.** `learn|learning`
matches *machine learning*, *deep learning*, *reinforcement learning*. Sweep 1's relevance gate used
it and admitted ML tutorials as education software. **`learn`/`learning` are excluded from the
strong-token set**; `ML_CTX` is retained in the source as the record of why.

**3. Family signatures are not mutually exclusive, and presence-matching therefore invents a second
family.** `verify.py` first reported `slp-lab-research/higraph` and `ICICLE-ai/curriculum-generator`
as **conjunctive** `BSD-2-Clause + BSD-3-Clause`. Both are single-family BSD-3-Clause. **BSD-2's
signature — *"Redistributions in binary form must reproduce the above copyright"* — is clause 2 OF
BSD-3-Clause**, a strict textual subset.

> 🔵 **The rule: family detection must test for SUBSUMPTION, not presence.** `subsume_test.py`
> encodes `SUBSUMES = {"BSD-3-Clause": {"BSD-2-Clause"}}` and keeps the failing case as a named
> regression control.

This is the exact mirror of `p887`'s finding. `p887`'s classifier was **first-title-wins** and
**missed a real second family**. `p888`'s was **presence-matching** and **invented one**. Both
errors are in the same place — the step between bytes and a family label — and they fail in opposite
directions.

## Honouring `887-G1`

`887-G1` records that **a shelf note is an instrument's test oracle, and no acceptance test says to
read it.** `verify.py` was run against rows this KB does *not* already carry, so no shelf note
existed to be the oracle. The substitute control was the **metadata channel**: every row's byte
verdict was diffed against `license.spdx_id` from the search payload, and the one disagreement
(`ad1-kamath/coursecraft`) was chased to its declaration in `Cargo.toml`. That diff is the column
`api_spdx` vs `bytes_families` in `evidence/grant-verify-888.2026-11-18-p888.tsv`.

## Reproduce

```sh
cd compose/code/p888-search-discovery
python3 -I subsume_test.py          # 9/9 controls, offline
python3 -I sweep2.py                # needs gh auth; ~22 search calls at 30/min
python3 -I verify.py                # needs to-verify.json; byte-reads each row
```
