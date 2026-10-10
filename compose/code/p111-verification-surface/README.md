---
industry: education
region: Global
updated: 2026-10-10
---

# p111-verification-surface — can the tree tell you when you broke it

**Pass 111, 2026-10-10.** `test_p111.sh` → **66 passed / 0 failed**, fully offline
(real git repositories committed on disk and served to the real `vsurface.sh` over
`file://`; no mocks).

## The question, and why p110 forces it

Four passes have measured this shelf's maintenance, and **all four read the history**:

| pass | axis | answers | cannot say |
|---|---|---|---|
| p107 | tag **count** | how much ref traffic | it inverts at the top of the shelf |
| p108 | release **identity** | *can I pin it* | whether the pin is from 2019 |
| p109 | commit **recency** | *is it alive* | who is keeping it alive |
| p110 | author **concentration** | *what happens if they stop* | whether I can take it over |
| **p111** | **tree** verification surface | *can I tell when I broke it* | whether the suite is any good |

p110's result is what makes this the next question rather than one of many.
**200 of 296 rows (67.6 %) are `solo`**, so for two thirds of this shelf the engagement
decision is not *depend on it* — it is *vendor it at a SHA and own it*. Owning a tree is
only tractable if the tree can tell you when you have broken it.

So p111 is **the first axis on this shelf read from the TREE rather than from the
history**, and that has a methodological consequence worth more than the numbers
(`P111-B`).

## What it emits

Twelve columns, one row per address:

```
slug  rc  files  vendor_stripped  src_files  test_files  test_cfg
      ci_files  ci_systems  ci_names_runner  ci_on_pr  verdict
```

### The verdict ladder

| verdict | meaning |
|---|---|
| `UNREAD` | fetch failed — no claim made (`P1040`) |
| `no-code` | no source files at HEAD → verification not applicable (`P111-F`) |
| `bare` | has source, no suite, no CI → you are on your own |
| `tests-only` | suite present, no CI → runnable, but nobody runs it |
| `ci-only` | CI present, no suite → the pipeline builds; nothing verifies |
| `fossil-ci` | suite present, but the only CI is a dead service (`P111-D`) |
| `partial` | suite + live CI, but no runner named **or** no PR trigger |
| `checked` | suite + live CI naming a runner **and** triggering on `pull_request` |

## Channel

Anonymous git lane only, re-probed live this pass:

| endpoint | result |
|---|---|
| `git ls-remote` / `git fetch` | `rc=0` |
| `raw.githubusercontent.com/<slug>/HEAD/…` | `200` |
| `api.github.com` | `403` (`P107-A`, session scoping) |

So `/contents` and `/actions` cannot be read. The tree comes from a depth-1
blob-filtered fetch; CI file **bodies** come from a batched lazy blob fetch against the
same promisor remote (`P111-H`).

## Nine disciplines, each of which a draft of this script got wrong

- **`P111-A` a path COMPONENT, never a substring.** `grep -i test` over a tree matches
  `docs/testimonials.rst`, `src/latest.py`, `contest/`, `protest.js`, `greatest.h` and
  `lib/attestation.go`. All six shapes are on this shelf — `overhangio/tutor` alone
  carries `docs/testimonials.rst`. Directory matches are component-exact; filename
  matches are separator-anchored (`test_`, `test-`, `_test.`, `.test.`), never a bare
  `test*` prefix.

- **`P111-B` depth 1 is enough, and deeper would be wrong.** This **inverts `P110-D`
  deliberately.** p110 measured a property of *history*, so its window was load-bearing
  and — because `--depth` is a *generation* limit, not a commit count — its windows were
  **not comparable across rows**. A tree property needs exactly one commit, every row is
  read at exactly the same depth, so **p111's rows are comparable to each other in a way
  p110's never were.** That is the first axis on this shelf for which cross-row
  arithmetic is sound without a caveat.

- **`P111-C` a vendored suite is not this repo's suite.** `node_modules/`, `vendor/`,
  `third_party/`, `site-packages/`, `Pods/`, `.tox/` carry thousands of *upstream* test
  files. Left in, the one repo with a committed dependency tree reads as the
  best-tested row on the shelf. Vendor paths are dropped before any arithmetic and
  **counted**, so the drop is auditable rather than silent.

- **`P111-D` a CI config for a service that no longer runs is not CI.** Travis CI ended
  its free open-source tier; a `.travis.yml` is a fossil, not a check. Counting "has CI"
  across all systems overstates the shelf, so `ci_systems` is emitted per row and the
  ladder refuses to call a travis-only row `checked`.

- **`P111-E` runner config is not a test, and a build manifest is not runner config.**
  `tox.ini` / `phpunit.xml` / `jest.config.js` are evidence a suite is *meant* to be run,
  so they get their own column instead of inflating the test count.
  `pyproject.toml`, `package.json` and `setup.cfg` are **not** counted: they merely *can*
  carry a `[tool.pytest]` table, and counting them makes nearly every Python and Node row
  on this shelf read as having a suite.

- **`P111-F` "no tests" is not a defect in a repo with no code.** This shelf holds
  specifications, awesome-lists, curriculum datasets and corpora. A spec with no suite is
  correctly bare and is **not** a risk, so `src_files` gates the verdict: a row with no
  source files is `no-code`, not `bare`. Without this gate the headline figure is both
  wrong and alarmist — the failure mode this KB has flagged in its own prior passes most
  often.

- **`P111-G` a check that does not run on a pull request does not check a fork.** This is
  the whole point of the axis. p110 says two thirds of this shelf must be forked. A
  workflow triggered only by `push` to the *upstream's* own branches never runs on a
  contributor's topic branch, nor on the PR that carries it back. Such a row has CI and a
  suite and still cannot tell a forker whether their change is sound.

- **`P111-H` the CI body is read, not inferred from its filename.**
  `.github/workflows/test.yml` is a filename, not a guarantee; `ci.yml` and `main.yml`
  routinely hold the only test job. Bodies are read through a single **batched**
  `git cat-file --batch` per repo against the promisor remote — 8 blobs in 2.6 s
  measured, versus one round trip each. The read is **textual** and this script claims
  nothing more: it reports that a config *names* a test runner and *mentions* a
  `pull_request` trigger. It does not execute the workflow graph, so a runner named
  inside a job that is gated off still counts. **The direction of that error is known and
  stated: it can only make a row look MORE checked than it is, never less.** Every
  headline figure below is therefore an upper bound.

- **`P111-I` `set -o pipefail` + `grep -q` inverts an EARLY match.**
  `printf '%s' "$body" | grep -q PAT` is **false when `PAT` matches early**: `grep` exits
  at the first hit, the writer takes `SIGPIPE` (141), and `pipefail` makes *that* the
  pipeline's status. This was **measured, not reasoned about**: `oppia/oppia` contains
  `pull_request` 39 times, first in the opening workflow, and the piped form reported
  `ci_on_pr=0` while the runner probe — whose term appears *late* in the same bytes —
  reported `1`. The first draft of this instrument shipped that bug and it graded
  `oppia/oppia`, one of the best-tested repositories on this shelf, as `partial`.
  Every body probe therefore greps a **file**. The failure is silent, it points the wrong
  way, and **it is worst exactly where the signal is strongest** — which is the
  transferable part.

`P1040` is carried: **an unread row is never zero.** `rc!=0` emits `UNREAD` with empty
metrics, so a fetch failure is never arithmetically indistinguishable from a repo that
genuinely ships no tests.

## Reproducing

```sh
./test_p111.sh          # 66 assertions, offline, no network
./vsurface.sh           # the full shelf -> result.<date>.tsv
P111_NO_BODY=1 ./vsurface.sh    # stage B withheld, to measure its contribution
```

`P111_BASE` redirects every address at a different transport (the test suite points it at
`file://`). `P111_NO_BODY=1` withholds the body read; like `P110_MERGES` it exists so a
discipline's contribution can be **measured** on this shelf rather than asserted, and is
never the mode a reported figure comes from.
