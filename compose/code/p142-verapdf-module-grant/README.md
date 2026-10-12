---
industry: education
region: Global
updated: 2026-10-12
---

# `p142-verapdf-module-grant` — `ACTION DF`: 🔴 REFUTED. The licence election is PER-MODULE, and `P20` step 2 is wrong as written

## The action, as p141 wrote it

> Resolve which licence `org.verapdf:core` and `org.verapdf:xmp-core` — the modules a consumer
> actually pulls — declare, and whether either ships licence text. 🔴 *Refuted if either declares
> its own licence differing from the parent's dual GPL-3.0 / MPL-2.0 offer, which would mean the
> election a studio has to make is per-module rather than per-project and `P20` step 2 is wrong
> as written.*

## Verdict: 🔴 **DISCHARGED and REFUTED**

The walker is p140's `pom_chain.py`, **executed unchanged**; only the coordinates are new.

| coordinate | own POM | inherits from | effective licence | depth | jar licence text |
|---|---|---|---|---|---|
| `org.verapdf:core:1.30.3` | 🔴 NONE | `org.verapdf:verapdf-parent:1.30.1` | **GPL-3.0 *or* MPL-2.0** | **4** | 🔴 `SILENT` (460 entries) |
| 🔴 **`org.verapdf:verapdf-xmp-core:1.30.3`** | 🟢 **BSD-3-Clause** | *(parent offers dual GPL/MPL)* | 🟢 **BSD-3-Clause** | 4 | 🔴 `SILENT` (78 entries) |
| `org.verapdf:validation-model:1.30.3` | 🔴 NONE | `org.verapdf:verapdf-parent:1.30.1` | **GPL-3.0 *or* MPL-2.0** | 4 | 🔴 `SILENT` (369 entries) |
| 🔴 `org.verapdf:xmp-core:1.30.3` | — | — | — | — | 🔴 **404 — never published** |

🔴 **`verapdf-xmp-core` declares BSD-3-Clause in its own POM**, against a parent offering dual
GPL-3.0 / MPL-2.0. The falsifier fires exactly as p141 wrote it: **the election is per-module.**

🔵 **And the direction is the opposite of the worry.** The XMP module is *more* permissive than
the project, not less — a studio that elects MPL-2.0 project-wide is over-complying on that
artefact, and one that assumes the project licence applies uniformly will mis-state its own
bill of materials in both directions.

🔴 **Three of three published jars ship no licence text at all** — `SILENT` across 907 entries.
So the grant exists only in a POM four levels up, and nothing a consumer unzips says anything.

## 🔴 `org.verapdf:xmp-core` does not exist, and the reason generalises

It is `404` on Central, checked in the same run in which `org.verapdf:core` answered `200`.
p141 took both names from `verapdf-library-1.30.3.pom`:

```xml
<modules><module>xmp-core</module><module>core</module></modules>
```

🔵 **A `<module>` entry is a path in the source tree, not an artifactId.** The directory
`xmp-core/` builds `verapdf-xmp-core`; the directory `core/` happens to build `core`, and that
coincidence is what made the other name look resolvable. Any probe that derives coordinates
from a `<modules>` block inherits this error, so `test_jar_licence.py` pins it.

## 🔴 A defect this probe found in its own first draft, in the inflating direction again

The first draft reported licence text in **every** jar it opened, and every hit was false. It
matched entry names case-insensitively against a substring list containing `MPL` — and `MPL` is
a substring of `IMPL`. 🔴 **`validation-model` returned 300-plus "licence files", all of them
compiled classes in `org/verapdf/gf/model/impl/`.**

The matcher now tests the **basename** against anchored patterns and skips code extensions, so a
token inside a package path cannot match. `org/verapdf/xmp/impl/XMPNode.class` is pinned as a
fixture that must not match. 🔵 **Third consecutive pass in which an instrument's first draft was
wrong in the inflating direction and the published figure is the smaller one** — p140's
`SERVER_CTOR`, p141's `CREATE TABLE … is not`, and now `IMPL`.

## Consequence for `P20`

`P20` step 2 instructs a studio to *elect* between GPL-3.0 and MPL-2.0 for veraPDF. 🔴 **That
step must be re-cut per coordinate**: the election applies to `core` and `validation-model`;
`verapdf-xmp-core` is BSD-3-Clause and no election arises; and the named umbrella coordinate
`verapdf-library` has no jar at all.

## Reproduce

```sh
python3 -I ../p140-pom-parent-chain/pom_chain.py org.verapdf:core:1.30.3 \
        org.verapdf:verapdf-xmp-core:1.30.3 org.verapdf:xmp-core:1.30.3
python3 -I jar_licence.py org.verapdf:core:1.30.3 org.verapdf:verapdf-xmp-core:1.30.3
python3 -I test_jar_licence.py    # 6 tests, including the IMPL regression
```

Committed: [`result.2026-10-12-p142.tsv`](result.2026-10-12-p142.tsv) (chain),
[`payload.2026-10-12-p142.tsv`](payload.2026-10-12-p142.tsv) (jar text),
[`chain.2026-10-12-p142.txt`](chain.2026-10-12-p142.txt) (every level as walked).
