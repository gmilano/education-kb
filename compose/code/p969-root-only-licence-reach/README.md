# `p969-root-only-licence-reach` — the grant ladder cannot see a per-directory licence

**Pass 93, 2026-10-10.** Evidence directory. 🔴 **No executable here, deliberately:** this session's sandbox
declines to run repository code, so this pass could not run `grant-ladder-v4/ladder.sh` **and did not write a
replacement** — `P237` forbids forking the shared classifier, and pass 91 measured what that costs. What is
committed instead is **the failing case, with bytes and SHAs**, so the next pass that can execute code has a
test ready rather than a claim to re-derive.

## The finding

`grant-ladder-v4` probes **24 candidate filenames at the repository root**. A repository can declare its code
licence at the root and its **data** licence one directory down. When it does, the ladder returns the root
answer and is confident about it.

### The row that proves it

[`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) — `main` · `daabd7d`. Its entire purpose is a
dataset: **1 721 BNCC learning objectives** in JSON / SQLite / CSV.

| oracle | verdict | mechanism |
|---|---|---|
| 24-filename ladder, repo root | 🔴 `MIT` | `LICENSE` = 1 073 B MIT, HTTP 200 |
| GitHub's own licence sidebar | 🔴 `MIT license` | GitHub also detects at the root |
| README + `dados/LICENSE.md` | 🟢 **data is CC BY 4.0**; MIT covers `pipeline/` | one directory down |

🔴 **Root `LICENSE-DADOS.md` → HTTP 404.** The data grant is not reachable by any root filename.

🔵 **Two independent oracles, one blind spot, one cause: root-only detection.** That is what makes this a
finding about the method rather than a defect in one script.

### Why it costs something

CC BY 4.0 is an **attribution obligation**. A studio that reads `MIT` and vendors the dataset into a closed
deliverable has taken on an attribution duty it does not know about — and the artefact of value in this
repository is **the data**, not the pipeline that the MIT grant actually covers.

🔵 **This is the same class as `P960`, one level up.** `P960` was a *classifier* returning the wrong family
for a payload it had read. `P969` is a *reach* defect: the payload that governs was never fetched, so no
classifier could have helped.

## The control, in the same publisher

🟢 **The fix is convention, not tooling, and the same organisation demonstrates it.**
`bncc-dev/bncc-pacotes` (`LICENSE`, 1 299 B) and `bncc-dev/bncc-benchmark` (`LICENSE`, 911 B) put a
**split-grant index at the root**: each names both families and scopes each one to explicit paths
(`packages/*/src/`, `python/bncc/*.py`, `mcp-worker/src/`, `harness/`, `test/` → MIT; `itens/`,
`resultados/`, `METODOLOGIA.md`, the datasets → CC BY 4.0), and each points at the full text.
**The ladder reads those two correctly.** GitHub's sidebar reports *"License and 2 other licenses found"* for
them, and plain *"MIT license"* for `bncc-dados`.

🟢 **So the discriminator is not the licensing model — all three repos are dual-licensed — it is whether the
declaration is at the root.**

## `P965`'s threshold holds on a payload it was not built on

Pass 92 set it from measurement: **a real grant names 0–2 licence families; a *framework* document names 3,
from three distinct lineages** (the shape of `learning-commons-org/knowledge-graph`'s `LICENSE.md`, which
grants nothing and ends at *"Gated content isn't yours to redistribute by default"*).

These index files name **2** families from two lineages, and they **are** real grants — both referenced texts
were fetched and verified present this pass:

| file | bytes | HTTP | content |
|---|---|---|---|
| `bncc-benchmark/LICENSE-CODIGO.md` | 1 286 | 200 | MIT full text |
| `bncc-benchmark/LICENSE-DADOS.md` | 577 | 200 | CC BY 4.0 **by reference** to `creativecommons.org/licenses/by/4.0/`, with the attribution clause naming **MEC/CNE** |

🔵 **Same document *shape* as the framework case, opposite usability — and the measured threshold separates
them correctly.** That is a real validation, not a restatement: this payload did not exist in pass 92's
corpus.

## For the next pass — the test to write

1. Wire `compose/code/p199-perfile-license/` (per-path probing, already in this repository, already run on
   `INGInious`) into `grant-ladder-v4` as a **second stage** that runs when the root verdict is reached.
2. Minimum reach for stage two: the 24 names **under each top-level directory**, plus `*/LICENSE*` and
   `*/LICENCE*`.
3. Assertions, with expected values from `pass93-resolved.tsv`:
   - `bncc-dev/bncc-dados` → **root `MIT` AND `dados/` `CC-BY-4.0`**. A single-verdict answer is a FAIL.
   - `bncc-dev/bncc-pacotes`, `bncc-dev/bncc-benchmark` → split grant detected **at the root** (these must
     not regress when stage two is added).
   - `eribean/girth` → `MIT` from **`LICENSE.txt`** (`LICENSE` is a 404) — a stage-one row that must still
     pass.
   - Negative control: a root-only MIT repo with **no** sub-directory licence must still return exactly one
     verdict. 🔴 **Without this control, stage two will manufacture split grants everywhere.**
4. 🔴 **Report the reach of stage two in `--reach`, as `P961` requires of stage one.** A two-stage probe whose
   second stage's denominator is unpublished is `P953` again.

## Honest limits of this directory

- 🔴 **`OS4ED/openSIS-Classic` was probed on 3 of 24 names, not 24.** It reproduces a verdict the shelf
  already held; **it does not independently establish a 24-name negative.** Recorded in the TSV as
  `NO-PAYLOAD/3-of-24-PROBED` rather than as a clean negative.
- 🟡 **The `moodle/moodle` control was byte-identical to pass 92 at the *same* SHA**, so it is a re-read of
  one object, not an independent eleventh reproduction. Stated in the TSV.
- 🔴 **13 slugs, not a census.** Pass 92's `grant-ladder-v4/pass92-results.tsv` (133 rows, 133 unique slugs)
  is **not** superseded by this file. `P966`.
- 🔴 **The family column here was read by a human, not computed.** It is evidence for a test, not a
  substitute for one. Every row carries its bytes, filename, ref and SHA precisely so v4 can disagree.
