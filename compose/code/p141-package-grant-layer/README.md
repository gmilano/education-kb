---
industry: education
region: North America
updated: 2026-10-12
---

# `p141-package-grant-layer` — `ACTION DA`: 🔴 NOT REFUTED. Six of six packages declare nothing at all

## The action, as p140 wrote it

> Check whether `openedx-core`'s **six consolidated top-level packages** each retain their own
> licence posture, or whether consolidation flattened them to one AGPL-3.0 grant. 🔴 *Refuted
> if any of the six carries a per-package licence differing from the distribution's
> `AGPL-3.0-only` — which would make `T18`'s per-file notice question live again at the package
> layer.*

## Verdict: 🔴 **DISCHARGED, NOT REFUTED. Zero of six differs — because zero of six declares anything.**

`openedx_core-1.9.1-py3-none-any.whl`, 358 188 bytes
([`result.2026-10-12-p141.tsv`](result.2026-10-12-p141.tsv)):

| package | `.py` files | licence files | SPDX headers | copyright lines | verdict |
|---|---|---|---|---|---|
| `openedx_catalog` | 12 | 🔴 **0** | 🔴 **0** | 🔴 **0** | 🔴 `SILENT` |
| `openedx_content` | **132** | 🔴 **0** | 🔴 **0** | 🔴 **0** | 🔴 `SILENT` |
| `openedx_core` | 1 | 🔴 **0** | 🔴 **0** | 🔴 **0** | 🔴 `SILENT` |
| `openedx_django_lib` | 7 | 🔴 **0** | 🔴 **0** | 🔴 **0** | 🔴 `SILENT` |
| `openedx_learning` | 29 | 🔴 **0** | 🔴 **0** | 🔴 **0** | 🔴 `SILENT` |
| `openedx_tagging` | 56 | 🔴 **0** | 🔴 **0** | 🔴 **0** | 🔴 `SILENT` |
| **total** | **237** | 🔴 **0** | 🔴 **0** | 🔴 **0** | — |

Against the distribution layer, one level up:

| layer | grant |
|---|---|
| 🟢 distribution | `License-Expression: AGPL-3.0-only` (PEP 639) + `dist-info/licenses/LICENSE.txt`, **35 139 bytes**, Metadata-Version 2.4 |
| 🔴 package | 🔴 **nothing, in any of the six** |
| 🔴 file | 🔴 **nothing, in any of 237** |

## 🔵 The question assumed the wrong failure mode, and that is the finding

p140 expected the interesting defect to be **disagreement** between layers — a subpackage
carrying a licence the distribution does not. The measured defect is **silence**. Consolidation
did not flatten six postures into one; there was never more than one, and it exists at exactly
one layer.

🔴 **That layer is not the one a studio copies from.** Nobody vendors a wheel. They lift
`openedx_tagging/` or `openedx_content/` into their own tree — and the moment a subtree leaves
`dist-info/`'s company it carries **no grant, no holder and no notice**, while
**AGPL-3.0-only** is the most reciprocal obligation anywhere on these shelves. 🔵 **The licence
is correct, current, complete and discoverable in precisely the one place the copy does not
come from.**

🟢 **p140's verdict on the distribution stands**: `openedx-core` is still the cleanest licence
*payload* this KB has measured, and `T21` is untouched — it ships the text it declares. 🔵 **The
two findings are about different layers and both are true.** A `T21`-clean artefact can be
`T18`-silent, and this one is the clearest example of it: the distribution does everything right
and tells a reader of any individual file nothing whatsoever.

## 🟢 One thing this probe confirms rather than discovers

`openedx_learning` survives as a **package name inside the distribution** even though the
*distribution* `openedx-learning` was retired to a shim (p140's `ACTION CS`). 🔵 **The name did
not die; it was demoted from distribution to subpackage** — and the 29 files under it are live
code at 1.9.1, not the 1 479-byte husk `openedx-learning` 0.33.1 publishes. A KB row keyed on
the string alone cannot tell those apart, which is why `T27` reads the `Development Status`
classifier.

## Reproduce

```sh
curl -sO https://files.pythonhosted.org/packages/95/c3/8d9b44052c00dfe36b587a518e08a46534b27844293199aa468ee696d14f/openedx_core-1.9.1-py3-none-any.whl
python3 -I grant_layer.py openedx_core-1.9.1-py3-none-any.whl
```

No extraction step: the wheel is read as a zip, so the measurement is of the published bytes.
