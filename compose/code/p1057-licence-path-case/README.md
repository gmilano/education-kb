# `P1057` — licence-path CASE closure, and the manifest field that names the file

**Pass 189 · 2026-10-14 · 16/16 tests passing · validated against live bytes**

## The row that caused it

`ACTION MZ` fetched licence bytes for `64` rows over the raw channel using this KB's
standing path list — `LICENSE`, `LICENSE.txt`, `LICENSE.md`, `COPYING`. Seven returned
nothing. One was [`openedx/XBlock`](https://github.com/openedx/XBlock), which this KB
publishes as:

> 🔴 **`NO_LICENCE_FILE`** … 🟡 **Apache-2.0 ASSERTED — and no licence TEXT anywhere in the tree**
> *(`repos/foundations.md`)*

**That verdict is refuted.** The file is `LICENSE.TXT` — uppercase extension — `11 358` B
of verbatim Apache-2.0, HTTP `200` at
`raw.githubusercontent.com/openedx/XBlock/HEAD/LICENSE.TXT`.

`raw.githubusercontent.com` is **case-sensitive**. A path list that spells the extension
in one case has not looked for the file; it has looked for **one spelling** of the file.

🔵 Why it matters commercially: `XBlock` is the permissive entry point this KB recommends
into AGPL Open edX. The caveat the wrong verdict forced onto every engagement using it —
*"usable, but the grant is a NOTICE not a LICENSE"* — was never real.

## Two channels, in cost order

| # | channel | authority | measured coverage |
|---|---|---|---|
| `1` | **the manifest NAMES the file** — PEP 639 `license-files` *(`pyproject.toml`)*, npm `licenseFile` | 🟢 **authoritative** — no guessing | 🔴 **`1` of `64` rows** *(`openedx/XBlock`)* |
| `2` | **case variants** of stem and extension | 🟡 heuristic | the generalisable fix, because `1` is ~`2`% |

```
openedx/XBlock, pyproject.toml, HEAD, 3 344 B:   license-files = ["LICENSE.TXT"]
```

🔴 **A licence STRING is not a licence PATH.** `license = { text = "AGPL-3.0" }` and
`"license": "MIT"` declare a licence and say nothing about where its text lives — both are
tested as negatives, because treating them as paths is the obvious wrong turn.

## The yield, which is the honest half

| sweep | probes | further grants found |
|---|---|---|
| `16` case variants × `14` grant-absent rows | **`224`** | 🟢 **`0`** |

🟢 **So the `XBlock` miss was ISOLATED, not systemic.** Every other grant-absent verdict
this KB publishes survives the sweep. A probe that finds one real error in `64` rows and
then nothing in `224` further requests has measured its own precision, and that number
belongs on the page beside the correction.

## Also settled this pass: the `/HEAD/` ref

🟢 `raw.githubusercontent.com/<owner>/<repo>/**HEAD**/<path>` resolves the default branch
*(verified `200` on `blend-ed/tutor-contrib-openedxmcp` and `HKUDS/DeepTutor`)*. Earlier
passes probed `main` **and** `master` and reported "`404` at `N` paths" verdicts built on a
branch guess. 🔵 `HEAD` removes the guess and halves the probe cost. Every fetch in p189
uses it.

## Interface

```python
probe_plan(manifest_text="", limit=None)
  -> {"declared": [...],   # paths the manifest NAMES — fetch these first
      "variants": [...],   # case-varied candidates, LICENSE first
      "order":    [...],   # declared + variants
      "channel":  "manifest" | "case-variants"}
```

No network: the caller supplies the manifest text and does the fetching
*(`gap 139` — this harness cannot install dependencies)*. This emits **paths**. Whether
the bytes at a path are a grant is `P1054` / `P1056` / `P1049`'s job.

## Run

```
python3 test_path_case.py     # PASS 16/16 — P1057
```
