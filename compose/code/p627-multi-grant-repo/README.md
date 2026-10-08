# `p627-multi-grant-repo` — the shape of a repository's grant

**Pass 52, 2026-10-08.** Suite 🟢 **31/31, offline.** Run it from this directory:

```
cd compose/code/p627-multi-grant-repo && python3 test_grant_shape.py
```

🔴 **Never with `python3 -I`** — isolated mode drops the script's directory from
`sys.path` and the suite reports `ModuleNotFoundError` against its own module
(`Gap 255`, the harness defect indistinguishable from a broken instrument).

## What it measures

| | Proposition |
|---|---|
| `P627` | A repository's grant is a **set of (path, family) pairs**, not a value. `grant-mccurdy/instructional-ai-workflows` ships **three**: `LICENSE` (MIT, code), `LICENSE-CONTENT.md` (CC BY 4.0, docs/diagrams/charts), `LICENSE-DATA.md` (CC BY 4.0, synthetic datasets). |
| `P628` | `PROPRIETARY` is a **verdict**, not an absence, and must not collapse into `UNKNOWN`. `UNKNOWN` means *not read*; `PROPRIETARY` means *read, and it refuses*. Conflating them turns a refusal into a retry. |
| `P629` | A slug can **exist and ship no grant**. Measured two ways: a full `--filter=blob:none` tree enumeration and the six-filename probe (`P624`). |
| `P630` | A byte delta between MIT payloads decomposes into exactly two axes — **copyright-line length** and **final newline**. Extends `P621`. |

## Controls, kept deliberately red-capable

Each property carries the **defective instrument it refutes**, so the defect
stays detectable rather than being deleted along with the bug:

- `single_license_sweep()` still answers `MIT` for the three-grant repo — and
  the suite asserts that it still **misses** the CC BY obligations.
- `filename_keyed_classifier()` still answers *open* for the Curtin
  `LICENSE.md` — and the suite asserts that payload is **not** an open grant.
- `P510`'s negative control (`gmilano/education-kb-NEGATIVE-CONTROL-no-existe-52`
  → **0 refs**) runs in the same sweep as the live slugs, and a **404 path on a
  real repo** is asserted distinguishable from a dead slug.

## One defect this suite found in itself

🔴 The `P479` no-star-counts check was first written as `"star" not in
blob.lower()` and went **RED on its own clean data**:
`MicroPyramid/opensource-startup-crm` contains the substring `star`.
🟢 **A substring is not a token.** The check now tokenises and tests for `star`
/ `stars` as words plus the glyph, and the substring form is retained as a
control asserting it is still the wrong instrument. 🔵 Same class as `P409` —
an instrument whose regex was wrong for ~11 passes while appearing to pass.

## Properties, not cardinalities (`P399`)

No assertion freezes a corpus count. The three-payload claim is scoped to the
one slug that ships three; the byte claims assert a **decomposition identity**
(`cp + nl == measured delta`), which holds for any pair of MIT payloads.

## Data

| File | |
|---|---|
| `payloads.2026-10-08.tsv` | 13 payload reads, status + bytes + `sha256` prefix + lines + family |
| `refs.2026-10-08.tsv` | `git ls-remote` existence sweep with the negative control in the same run |
| `mit-bytes.2026-10-08.tsv` | the three MIT payloads, final byte and copyright-line length |

🔵 **Channel, measured this pass:** `github.com` HTML **403**, `api.github.com`
**403**, every non-GitHub host **000** at the egress proxy;
`raw.githubusercontent.com` and `git ls-remote` **200**. Every family above is
read from payload over one of the two that answer.
