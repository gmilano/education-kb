---
industry: education
region: Global
updated: 2026-10-07
---

# `p440-unlicensed-registry-grant` — pass 25's action A: the grant that exists only in the registry

**Executes pass 25's pre-registered action A**, written as:

> Run `p436`'s four stages over the **87 `UNLICENSED`** rows — the slugs this shelf cites that
> ship **no licence file at all** — and resolve each against its registry's declared licence field.
> **Prediction:** expect the registry to supply a licence for **fewer than half**. The interesting
> class is the opposite one: a repository with **no** `LICENSE` whose published package declares
> MIT, which is a grant made in the registry and nowhere in the tree.

## Measured, 2026-10-07, over all 87

| Verdict | n | What it is |
|---|---|---|
| `NO-CHANNEL` | **57** | 51 publish no manifest at all, 6 carry a `private` one. **The registry cannot see two thirds of this population**, and that bounds the whole approach |
| `REGISTRY-GRANT` | **8** | a licence the tree does not carry, on a package the registry agrees lives here |
| `NO-PACKAGE` | 12 | a manifest exists, the registry 404s |
| `FOREIGN-PACKAGE` | 4 | a licence is declared and the registry names a **different** repository |
| `GRANT-UNOWNED` | 3 | a licence is declared and the registry names **no** repository |
| `REGISTRY-SILENT` | 2 | the package exists and declares nothing |
| `UNREACHABLE` | 1 | Maven Central 429 — see the calibration below |

🟢 **Prediction confirmed, and by a wide margin: 8 of 87 is 9.2%, not "fewer than half".**

🟢 **The class it named exists and is exactly six repositories** — no licence file anywhere in an
enumerated tree (`p441`), and a published package declaring **MIT**:

| Slug | Package | Registry grant |
|---|---|---|
| [`3121n/nor-data-udir-mcp`](https://github.com/3121n/nor-data-udir-mcp) | npm `@nor-data/udir-mcp` | MIT |
| [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms) | npm `canvas-mcp-server` | MIT |
| [`DistrictAPI/districtapi-mcp`](https://github.com/DistrictAPI/districtapi-mcp) | PyPI `districtapi-mcp` | MIT |
| [`SalShah20/classroom_mcp`](https://github.com/SalShah20/classroom_mcp) | npm `@salshah20/google-classroom-mcp` | MIT |
| [`learningequality/kolibri-design-system`](https://github.com/learningequality/kolibri-design-system) | npm `kolibri-design-system` | MIT |
| [`zainf2327/mcp-classroom`](https://github.com/zainf2327/mcp-classroom) | PyPI `mcp-classroom` | MIT |

⚠️ **A registry grant is a grant, and it is weaker evidence than a file.** The publisher asserted
MIT in metadata they control and can change with the next release, and nothing in the tree records
it. For a client deliverable this is `P314` — usable, and worth one written confirmation from the
holder, citing the publisher's own metadata.

## 🔴 The ownership stage, which the first build did not have, removed 7 of 15 claimed grants

The first run published **15** grants. Seven were somebody else's:

| Slug | Package | The registry's own repository | Class |
|---|---|---|---|
| `pnp-v/bo-google-classroom-mcp-server` | npm **`class`** | `deadlyicon/class.js` — *"A simple yet powerful Ruby-like Class inheritance system"*, first published **2013** | name collision |
| `plyght/canvas-mcp` | `canvas-mcp-server` | `DMontgomery40/mcp-canvas-lms` | derivative |
| `lucanardinocchi/canvas-mcp` | `canvas-mcp` | `vishalsachdev/canvas-mcp` | derivative |
| `joshuasoup/d2l-mcp` | `d2l-mcp-server` | `general-mudkip/d2l-mcp-server` | derivative |
| `Opetushallitus/aoe` | npm **`aoe`** | **none declared** — v0.1.1, published **2016-01-05** by `exolution@163.com`, no description, declaring **GPL-3.0** | unowned |
| `ink-waffle/moodle-mcp`, `ink-waffle/sisu-mcp` | `@ink-waffle/*` | none declared | unowned |

🔴 **`Opetushallitus/aoe` is the row that justifies the stage.** Unguarded, this KB would have
recorded a **STRONG-COPYLEFT** obligation on the **Finnish National Agency for Education**'s
national OER library on the strength of a stranger's 2016 hobby package. `p441` then showed the
refusal was right for a second reason nobody predicted: the project's real grant is **EUPL-1.2**,
in `aoe-web-backend/LICENSE` and `aoe-web-frontend/LICENSE`, 303 B each.

🟢 **The four `FOREIGN-PACKAGE` rows reproduce `p436`'s declared slug 4 for 4**, on an independent
run. That is cross-channel calibration, not a new finding — `p436` had already classified all four,
and `agents/top.md` already carried the `deadlyicon/class.js` collision. ⚠️ **One of them is new to
this KB as a repository:** `general-mudkip/d2l-mcp-server`, which the mandatory query set has never
surfaced in sixteen passes.

🟢 **`general-mudkip/d2l-mcp-server` is reachable only through the registry channel**, which is the
same thing `p436` found for `Polygl0t/Polygl0t`: searching for "education" never returns it.

## Where the two channels can be compared, they agree

| Slug | Tree (`p441`) | Registry (here) | |
|---|---|---|---|
| [`SchoolUtils/WebUntis`](https://github.com/SchoolUtils/WebUntis) | **MIT**, root `License` | **MIT**, npm `webuntis` | 🟢 agree |
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | **Apache-2.0**, root `LICENSE.TXT` | **Apache-2.0**, PyPI `license_expression` | 🟢 agree |
| [`veraPDF/veraPDF-library`](https://github.com/veraPDF/veraPDF-library) | **GPL-3.0 + MPL-2.0** | 🔴 **`null`** | tree wins |
| [`Opetushallitus/aoe`](https://github.com/Opetushallitus/aoe) | **EUPL-1.2** | 🔴 GPL-3.0, unowned | tree wins |

🔵 **So the registry is the weaker channel of the two wherever both answer**, and its value is
precisely the six rows where the tree is silent.

## 🔴 Two defects this sweep found in instruments the repository already versioned

**1. `dep_licence.classify_licence` mapped npm's `UNLICENSED` to `PERMISSIVE`.** `UNLICENSED` is
npm's documented value for *"I do not wish to grant others the right to use a private or unpublished
package under any terms"*. The permissive rule carried the bare pattern `r"UNLICENSE"`, which
matches inside it, so an explicit **refusal** returned the same class as `Unlicense`, the
public-domain dedication — the two most opposite values in the table. Latent, not live: no published
row carried it, and the population where it was most likely to appear is exactly the 87 swept here.
Fixed with a `NO-GRANT` class probed first, and **eight controls**, each pairing the refusal with
the one-letter-different grant.

🔵 **And the string collision is worth naming: `UNLICENSED` is this KB's own status for "no licence
file" and npm's value for "no licence granted".** One spelling, two meanings, one of which is a
verdict about the publisher's intent.

**2. Maven Central's POM layer is not reliably reachable here.** Pass 25 declared Maven Central
reachable on the strength of `maven-metadata.xml`, which is correct — and that file carries **no
licence element at all**. The grant lives in a version's POM, and `repo1.maven.org` answered **429
for the same POM URL that answered 200 ten seconds earlier**, three times in a row during
calibration:

| attempt | `maven-metadata.xml` | `verapdf-library-1.30.2.pom` | `junit-4.13.2.pom` |
|---|---|---|---|
| 1 | 🟢 200 | 🟢 200 | 🟢 200 |
| 2 | 🟢 200 | 🟢 200 | 🔴 **429** |
| 3 | 🔴 **429** | 🔴 **429** | 🟢 200 |

🔴 **A single-shot probe therefore cannot distinguish "this POM declares no licence" from "this POM
was rate-limited"**, and the first build published `REGISTRY-SILENT` for `org.verapdf:verapdf-library`
for exactly that reason. Non-200 is now `UNREACHABLE` with the status in the field column, never
`absent`.

## Reservations

- ⚠️ **`NO-CHANNEL` at 57 of 87 is the headline number, not the 8.** For two thirds of this
  population the registry has nothing to say, and no amount of probing changes that: a repository
  that publishes no package has no registry metadata to read.
- ⚠️ **An npm scope that equals the GitHub owner is evidence a gate cannot use.** `ink-waffle/*`
  publish `@ink-waffle/*`, which a human reads as ownership immediately; the declared-repository
  field is empty, so the instrument must say `GRANT-UNOWNED`. Both rows are almost certainly the
  owner's own MIT grant, and this KB does not publish "almost certainly" as a licence.
- ⚠️ **The 12 `NO-PACKAGE` rows are not evidence of anything except non-publication.**

## The controls (`test_grant.py`, 30/30, offline)

Every fixture is a real payload captured 2026-10-07. The set is built so that an instrument
answering `REGISTRY-GRANT` always, or never, fails:

| Control | Why it is there |
|---|---|
| `MIT` → grant | the positive |
| `UNLICENSED` → `REGISTRY-REFUSAL` · `Unlicense` → grant | **the inversion**, and its one-letter neighbour |
| `SEE LICENSE IN <file>` (both spellings) → `REGISTRY-DEFER` | a pointer to a file that is not there |
| `None` · `""` · `[]` → `REGISTRY-SILENT` | three ways to say nothing, none of which is a grant of nothing |
| `GPL-3.0` → grant, `STRONG-COPYLEFT` | a copyleft grant must not be softened into a non-grant |
| npm `class` fixture | the **collision**: a real MIT declaration belonging to `deadlyicon/class.js` |
| npm `aoe` fixture | the **unowned** case: real GPL-3.0, no repository, 2016 |
| PyPI `XBlock` fixture | the **positive for ownership**: PEP 639 `license_expression` + PyPI naming this repo |
| npm `canvas-mcp-server` fixture | one package name, two citing repositories; the registry names one |
| `maven-metadata.xml` → `absent` | the metadata file carries no licence, so reading it answers nothing |
| real veraPDF POM → `absent` | and the released POM genuinely has none either |
| `<licenses>` inside `<dependencies>` → `absent` | a dependency's grant is not the project's |
| POM parent/own/dependency coordinate triplet | a first-match scan publishes the parent's or a dependency's artifact |
| empty denominator → **exit 2** | a path fault is not a clean sweep (**P355**) |
| wide-list ∩ narrow-list = ∅ | or the widening double-counts |

## Run

```sh
python3 test_grant.py                                        # 30/30, offline
python3 -I grant.py slugs.input.2026-10-07.txt > result.tsv
python3 -I widen.py slugs.input.2026-10-07.txt > widen.tsv   # the 41-name widening
```

## Files

- `grant.py` — manifest resolution over 7 ecosystems, registry read, ownership gate, verdict
- `widen.py` — the 41-name widening, **and its own negative result**: over the 87 it found
  **one** row the 14-name list missed (`veraPDF`, already recorded in `intel/trends.md`), which is
  why `p441` stops enumerating names and enumerates the tree instead
- `test_grant.py` + `fixtures/` — real payloads, not excerpts
- `slugs.input.2026-10-07.txt` (87) · `result.2026-10-07.tsv` · `widen.2026-10-07.tsv`
  — **authoritative**
