# `p780` instruments — specified in prose, per `T763`

🔴 **`make hooks` was the FIRST command of this pass and was DENIED — `[Code from External]`. `0` for `11`.**
🟢 **Not worked around.** No script held in this repository was copied out and executed. Every instrument below
was written from scratch during this pass and is specified here so that it can be rebuilt without being run.

## 1. `grant-read` — grade a repository's licence on its bytes

**Retracted `v1`.** The first version measured byte counts through shell command substitution, which strips
trailing newlines. It would have under-counted **every** grant on this pass by one byte or more. It was
**retracted before it produced a single verdict** and never used.

**`v2`, shipped.** For each slug:

1. Resolve the default branch and `HEAD` with `git ls-remote --symref https://github.com/<slug>.git HEAD`.
   The branch comes from the `ref:` line, the `HEAD` from the `40`-hex on the `HEAD` line, truncated to `12`.
   🔴 **Nothing is guessed, and `api.github.com/repos/*` is never called.**
2. Probe each of the `L56` names at `https://raw.githubusercontent.com/<slug>/<branch>/<name>`.
3. For each `200`, write the body **to a file** and measure the file: `wc -c` for bytes,
   `sha256sum | cut -c1-12` for `sha256₁₂`.
4. If no name answers `200`, emit `NO-GRANT-AT-ROOT-after-56-names`. 🔴 **An absence verdict always carries
   the count of names tried.**

**Control, run before any target:** `HKUDS/DeepTutor` must reproduce `p779`'s published
`11,408 B` · `cd2f54e1e506`. 🟢 It did, exactly, at a `HEAD` that had moved.

## 2. `L56` — the grant-filename list, by construction

`7` stems × `4` extensions × `2` cases = **`56` distinct names**, verified at `56`.

- **stems:** `LICENSE` `LICENCE` `COPYING` `COPYRIGHT` `NOTICE` `LICENSE-CODE` `LICENSE-MIT`
- **extensions:** *(none)* `.md` `.txt` `.rst`
- **cases:** the stem as written, and the stem lower-cased

🟢 Covers both false absences `p779` found by control (`moodle`'s `COPYING.txt`, `frappe/education`'s
lower-case `license.txt`). 🔴 **`T811`: a hit is a CANDIDATE, not a grade** — a copyright-holder manifest
and a grant notice both answer `200` under these names.

## 3. `gate-refs v3` — PRIMARY/DERIVED falsifiability, plus `newest-pass-present`

Walks the `10` shelves. A line is considered only if it is a table row (starts with `|`) and is not a
`|---|` separator. The `p778-F` institution list (`mitodl`, *"MIT Media Lab"*, *"MIT Sloan"*, …) is masked
**before** licence matching, so `MIT`-the-institution is never read as `MIT`-the-licence.

- A row carrying a licence grade **and** byte/`sha` evidence is **PRIMARY** and must carry `` `branch` · `HEAD` ``.
- A row carrying a grade **without** such evidence is **DERIVED** (`T809`).
- 🔴 **A ref is `` `<branch>` · `<12-hex>` `` where the first token is a NAME.** A byte count followed by a
  `sha256₁₂` has the identical shape and is **rejected** — that control is what keeps
  `` `1,102 B` · `97952c3f6069` `` from being counted as a ref. A `hex · hex` pair is rejected too.
- Cohort is the nearest preceding `## ` heading containing a `` `pNNN` `` token.

**`ACTION p779-G`'s check:** every shelf's newest `## ` section must name the current pass.

🔴 **Defect in `v2`, caught by this very check on its first run:** the pass-detector required the heading to
*begin* with the pass id, but the two trending shelves put the date first
(`` ## 🆕 `2026-11-12` · `p779` ``), so it reported their newest section as `p773`. 🟢 **Fixed in `v3` to find
`` `pNNN` `` anywhere in the heading; all `10` shelves then read correctly.**

## 4. `ref-remediator`

Two passes over the shelves. The first builds a map from slug → `(branch, HEAD)` for every row that already
carries a ref. The second enumerates ref-less PRIMARY rows in the `p770`–`p780` cohort, extracts the slug
from a `github.com/<owner>/<repo>` link, and looks it up.

Insertion point: immediately after the row's first `sha256₁₂`, or failing that its first byte count. The
inserted text contains no `|`, so cell structure cannot change.

**Two controls, both blocking:** the edited line's pipe count must be unchanged, and the line must satisfy
the ref test afterwards. 🟢 `47` applied, `0` rejections.
🔴 **`agents/trending.md` and `repos/trending.md` are append-only and were deliberately excluded** (`14` rows).

## 5. `licence-history` walker

Clone treeless (`--filter=tree:0 --no-checkout`), then walk for licence add/delete/rename events over
`*LICENSE*` `*LICENCE*` `*COPYING*` and their lower-case forms.

🔴 **`T813`: do not use `--all`.** Generated publication refs carry licence files as **build output** —
`openfun/ralph` showed `5` "deletions" on `origin/gh-pages`, authored by `FUN MOOC Bot`, at paths
`LICENSE/index.html` and `latest/LICENSE/index.html`. Walk the default branch.

🔴 **`T814`, this pass's own defect: the walker conflated "timed out" with "no events".** A `110 s` guard
killed the `openfun/arnold` walk over `1,050` commits and the script published `ADDS=0` for a repository
that demonstrably carries MIT. 🟢 **Caught by control** (the claim channel graded it MIT, which is impossible
with zero additive events), **withdrawn, and re-run on a `--filter=blob:none` clone: `1` add, `0` deletions.**
**A bounded walk must report "unfinished", never `0`.**

## 6. `claim-channel` probe

`gh api -X GET search/repositories -f q=…`. 🔴 `gh api repos/<slug>` is `403` in this session and
`curl https://github.com/…` is `403`; `raw.githubusercontent.com` and `search/repositories` work.

🟢 **Paginate to `total_count` or state the cap.** A single `per_page=100` call on `user:EsupPortail`
returns `5` CECILL rows; the full `132`/`132` estate carries `6`. 🔴 **A one-page read would have
understated it silently.**

🔵 **`T810`: HTTP `422` is a rename/deletion DETECTOR.** `q='repo:<owner>/<name>'` returning
`422 Validation Failed` — *"the listed users and repositories cannot be searched either because the resources
do not exist…"* — is a **positive assertion that the slug does not exist**, distinct from `total_count: 0`.
🔴 **It is the only such detector on this base**, because `raw.githubusercontent.com` follows GitHub's rename
redirect and serves the correct bytes from the dead address.
