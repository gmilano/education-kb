---
industry: education
region: Global
updated: 2026-11-12
---

# `p779` instruments — specified in prose, per `T763`

🔴 **`make hooks` was tried as the FIRST command of this pass and DENIED — `[Code from External]`. TENTH consecutive session, `0` for `10`.** 🟢 **Not worked around.** No script held in this repository was copied out and executed. Every instrument below was **written from scratch this pass** and is specified here in prose so the next pass can rebuild it rather than run it.

## Channels, re-measured this pass

| Channel | How it is addressed | State at `p779` |
|---|---|---|
| Claim channel | `gh api -X GET search/repositories -f q='repo:<slug>'` / `q='user:<owner>'` | 🟢 Works. `q='user:<owner>'` returns up to `100` rows per call, which is what makes an estate census affordable |
| `gh api repos/<slug>` | direct REST | 🔴 `403` — *"GitHub access to this repository is not enabled for this session"*, re-measured |
| Ref channel | `git ls-remote --symref https://github.com/<slug> HEAD` | 🟢 Works. The only honest source of `default_branch` · `HEAD` |
| Body channel | `raw.githubusercontent.com/<slug>/<branch>/<file>` | 🟢 Works, **and accepts the literal ref `HEAD`**, which removes one `ls-remote` per repository on bulk sweeps. Verified against `sakai` (`11,120 B`) and `opencast` (`11,340 B`) before use |
| Tree channel | `git clone --no-checkout --filter=blob:none` | 🟢 Works. Gives a complete path listing and full commit history without fetching blobs |
| `github.com` **HTML** | `curl` of a repository's web page | 🔴 **Uniform `403` — all `43` URLs this pass introduced.** A channel artefact, **not `43` dead links**: the same `43` resolve `43`/`43` on the ref channel with matching `branch` · `HEAD`. 🔵 **URL verification must go through `git ls-remote`, never an HTTP GET of the page** ([`evidence/url-refcheck.2026-11-12-p779.tsv`](../../evidence/url-refcheck.2026-11-12-p779.tsv)) |
| `www.apache.org` | canonical Apache-2.0 | 🟢 **In the allowlist.** `LICENSE-2.0.txt` = `11,358 B`, which reproduces this base's canonical figure independently |
| `www.gnu.org` | canonical GPL-2.0 | 🔴 **BLOCKED** — `connect_rejected` by the egress proxy. Canonical GPL-2.0 was routed via `spdx/license-list-data` instead |

## `gate_refs.py` — the named gate for `ACTION p778-A`

**What it answers.** `T804` established that a licence grade is unfalsifiable without `branch` · `HEAD` beside it. This measures how large that unfalsifiable population is, per shelf. **It does not re-grade anything.**

**Specification.** Walk the `11` shelves. A row is considered only if it is a table data row — a leading `|`, not a `|---|` separator. Such a row is **licence-asserting** if it carries either a POSITIVE grade (a licence identifier in licence form, from a closed list of `38`-plus SPDX forms) or an **ABSENCE** grade (`NO-GRANT`, `no licence at root`). The two are counted separately, because an absence grade depends even more sharply than a positive one on which tree was read.

**`MIT` is matched to the `p778-F` specification.** It must appear in licence form (`MIT License`, `` `MIT` ``, `**MIT**`, `MIT-0`), and the institutional uses are stripped before matching: `mitodl`, *"MIT Open Learning"*, *"MIT Media Lab"*, *"MIT App Inventor"*, *"Harvard and MIT"*, *"MIT Sloan"*, *"MIT Press"*, *"MIT OpenCourseWare"*, *"MIT Solve"*. `p778-F` recorded this as a specification rather than a task; this is the first gate to implement it.

**A row counts as falsifiable** only if it cites a ref: a backticked ref-like name followed by ` · ` and a backticked `12`-hex code. **The `12`-hex body digest that follows a byte count is deliberately rejected** (`` `1,102 B` · `97952c3f6069` ``), because it identifies the blob and not the tree the blob was read from. This distinction is the whole point of the gate and it is the one thing a careless implementation gets wrong.

**Controls (`7`, all passed).** A hand-built control shelf carries: a row asserting MIT **with** a ref; the same row **without**; a row asserting `Apache-2.0` with no ref; an absence grade with a ref; an absence grade without; a row naming `mitodl` and *"MIT Media Lab"* and **no** licence; and a row whose only `12`-hex code follows a byte count. Required behaviour: `4` positive rows of which `1` has a ref, `2` absence rows of which `1` has a ref, the institutional row **not counted at all**, and the byte-digest row **flagged**. All seven behaved as specified before the gate was pointed at the base.

## `gate_refs_cohort.py` — the same gate resolved by pass

**Why it exists.** The base-wide number alone would have been misread. These shelves are append-only: a row written at `p300` could not have followed a convention invented at `p777`. This splits every shelf at its `## ` boundaries, attributes each section to the pass number in its own heading, and reports the falsifiable share per cohort. **If the convention is real the share must be high in recent cohorts and near zero in old ones; if it is aspirational it is low everywhere.** The prediction is therefore falsifiable, and the measurement is what separates "the convention is failing" from "the convention is young".

## `extract_apache.py` — the sweep population for `ACTION p778-B`

Extracts every repository slug whose **own table row** grades it `Apache-2.0`. Slug and grade must come from the *same* row, or a licence named anywhere on a line would attach to a repository named anywhere else on it. Emits `927` unique slugs.

## `band_sweep.sh` — measure the grant length of all `927`

For each slug, `curl -sSI` (headers only) against `raw.githubusercontent.com/<slug>/HEAD/<file>`, trying `LICENSE`, `LICENSE.txt`, `LICENSE.md`, `LICENCE`, `COPYING`, `LICENSE-APACHE` in that order and stopping at the first `200`. Reads `Content-Length`, never a body. A slug where every candidate `404`s is emitted as `NOFILE`, so an absence is a measurement and not a silent gap. `10`-way parallel.

## `ecl_decide.sh` — **the bytes decide** (`T799`)

For each of the `599` band members, a **ranged** read of the first `200` bytes (`curl -r 0-199`) and a classification of the title line. This is sound because `ECL-2.0` announces itself in its first `52` bytes — `Educational Community License, Version 2.0 (ECL-2.0)` — while canonical Apache-2.0 opens with a centred `Apache License` / `Version 2.0, January 2004`. Verified against both known-ECL prints and a known-Apache print before the sweep. Anything matching neither is emitted as `OTHER` and is a finding in its own right rather than a silent pass. A ranged read makes a `599`-repository byte decision cost about `120 kB`.

## `worddiff.py` — the operative-word differ for `ACTION p778-D`

Tokenises each print to lowercase word tokens, diffs the two token streams, and reports the delta, which **deontic operators** appear in the changed runs, and — given a named appendix marker — whether the whole delta is accounted for by that appendix, with the operative bodies compared separately. A deontic operator is what makes a licence term operative (`must`, `shall`, `may`, `not`, `except`, `unless`, `granted`, `provided`, `warranty`, …): **if none differ, the two prints grant and forbid the same things**, whatever the byte counts say.

**Controls (`2`, both passed).** A file against itself must give ratio `1.000000`, `0` changed runs and `NONE`/`NONE`. Two known-different licences (`MIT` against `GPL-2.0`) must give a low ratio and deontic differences in both directions — measured `0.0548`, `48` runs, operators present both ways.

## `estate_census.py` — the second and third estates for `ACTION p778-E`

Pages `search/repositories` with `q='user:<owner>'` until `total_count` is reached, then cross-tabulates grant rate by **repository-name family** (the leading hyphen/underscore token, which is how a delivery team's cookiecutter stamps its output), by language and by archived state. `T800`'s own named test is whether grant rate clusters by name family rather than by subject, so the cross-tab is the test and not decoration.

## `verify_row.sh` — write rows that can be re-read

Produces a falsifiable row for one repository on **all three channels at once**: claim-channel `spdx_id`/stars/`pushed_at`, ref-channel `default_branch` and `HEAD`, and body-channel filename, bytes, `sha256₁₂` and title line — with the body read **at the resolved branch, never at `HEAD`**, so the row names the tree it came from. `gate-refs` exists because rows without `branch` · `HEAD` cannot be re-read; this is the instrument that stops this pass adding to that population.

## The licence-history test for `ACTION p778-H`

`git clone --no-checkout --filter=blob:none`, then, for each repository: the current tree's licence paths, the licence paths **in the first commit**, and `git log --all --diff-filter=ADR` and `--diff-filter=D` over `*LICENSE*`, `*LICENCE*`, `*COPYING*`. The deletion count is the decisive number: **a withheld grant and a never-granted one look identical in the current tree and differ in the history.** `p778-H` asked for a distinction between a policy and an oversight, and this is the only channel in which that distinction leaves a trace.
