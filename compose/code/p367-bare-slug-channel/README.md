# `p367-bare-slug-channel` — `ACTION ZZ-bv`: the second address channel

**Pass 367 · 2026-10-21.**

## Why it exists

🔴 **`p366` measured the defect and registered it for a successor:** *"every 'absent from N
addresses' figure this base has published, `p364`'s 79% included, is an over-estimate by the
size of its bare-slug class, and the rate measured on `p366`'s own population is 8.2%."*

🔵 **The blindness is one line.** `p348-fold-identity` harvests addresses with
`github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)`, and **every** census, identity and absence
instrument here imports `slugs_in` from it rather than reimplementing. 🟢 That is the right
rule — it is why this base has no second channel disagreeing with itself — and 🔴 it is
exactly why a repository written as a bare backticked slug is invisible to all of them at
once.

## What it measures

- `bare_slug_channel.py` — channel **B**. Harvests backticked one-slash tokens, folds them
  (`.git` stripped), rejects through `p351-address-shape` (**imported, never
  reimplemented**) plus four arms of its own, and reports the survivors that channel **U**
  does not already hold. `census` / `candidates` / `reject`.
- `probe_slugs.sh` — the online leg. `adjudicate` resolves each candidate with
  `git ls-remote --symref`; `refset` fingerprints **all** refs, which is what separates
  `SAME-REF-SET` from `SAME-HEAD-ONLY` where `p366`'s test could only compare `HEAD`.
- `test_bare_slug_channel.py` — **22 offline controls**, wired into `HOOK_GATES` as
  `gate-bare-slug-channel`.

## What it found (2026-10-21)

**4 772** backticked candidates → **1 727** rejected offline → **823** not in channel U →
🟢 **518 LIVE** (**62.9%** survivor precision), plus **4** from the `GLUED-SLUG`
sub-channel (159 candidates, **2.5%** precision, reported separately for that reason).
Minus **26** sha collisions with channel U → 🔴 **496 net-new live repositories = 16.3% of a
true corpus of 3 038.**

🟢 **The offline arms are measured, not trusted: 120 of the 1 727 rejected candidates were
probed and 0 are live.**

🔴 **The two worst omissions are this base's own binding constraints** —
`kristopherkyle/TAALED` (`Gap 239`/`246`'s NonCommercial blocker) and `nilc-nlp/nilcmetrix`
(`Gap 239`'s AGPL oracle), each mentioned 3 times with **0** `github.com/` occurrences.

## 🔴 Three defects in this instrument's own drafts, and what each would have published

1. **`.git` not folded.** 7 spelling artefacts as distinct live repositories and 7 false
   identity rows. 🟢 It did **not** move the net-new count, because each artefact collided
   with its own de-suffixed form — the only reason a reader would not have been misled.
2. **The empty-input guard fired on the per-slug CHILD.** `xargs` re-invokes this script with
   a slug in `$2`, not a file, so `[ ! -s "$arg" ]` was true 823 times. 🔴 `P541`'s own class
   arriving through the guard built to prevent it. 🟢 Caught because it was loud; a guard
   exiting `0` would have published an empty adjudication as a clean result.
3. **The false-rejection control word-split its own input.** Default `xargs -a` splits on
   spaces; rejected candidates legitimately contain spaces. It reported **two** live rows
   among the rejected — which read exactly like two false rejections and were nothing of the
   kind: both are fragments, and both addresses are **already carried as URLs**. 🟢 The
   fragments are how the `GLUED-SLUG` class was found. Input is now newline-delimited.

## 🔴 Four limits, stated

1. **The backtick is required.** A repository named in running prose cannot be told from an
   English word pair (`pass/fail`, `spanish/portuguese`) by any rule this file could carry
   honestly — so **this channel cannot be proven complete.** It can only be shown to have
   found more than the URL channel did.
2. **`SAME-REF-SET` is not a redirect.** Identical ref sets mean one repository *or* a fork
   nobody has pushed to. `treeverse/dvc` ≡ `iterative/dvc` is the specimen: `treeverse` is
   lakeFS's organisation, so a DVC rename is implausible and `ls-remote` cannot tell.
3. **A live address is not a shelf row, and the slug is not the domain.** 2 of the 5
   permissively-licensed rows graded this pass are a different field wearing an education
   name (`google/caliper` is a Java microbenchmark harness; `python-adaptive/adaptive` is
   numerical function sampling). A **40%** trap rate — `Gap 475`.
4. **This module is NOT wired into `p348`.** Doing so would change every denominator this
   base has ever published in one commit with no pass able to verify the result — `Gap 474`.

## 🟡 The gate that caught this instrument, and the two wrong remedies

`make gate-ladder-case` graded this file `SINGLE-SPELLING` on entry, breaching `p286`'s
ratchet. 🟡 Case-closing the literals (`p352`'s and `p354`'s remedy) did not clear it.
🔴 Deleting the grant-family words was refuted by measurement — six non-addresses leaked in.
🟢 **The cause was this file's own identifiers:** `p283`'s `BARE` pattern read the constant
`LICENCE_TOKEN` and the status value `"LICENCE-PAIR"` as licence *path* spellings.
Renamed `GRANT_ID_TOKEN` / `GRANT-ID-PAIR`; the grade clears. 🔵 The channel-B population was
re-measured after each attempt and is byte-identical at all four points — **823** candidates.
A gate fix that moves the measurement is a different instrument wearing the same name.
