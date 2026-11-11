## 🆕 `p769` — **The foundation layer of this register is the strongest open-source substrate this base has measured in any vertical — and its root grant is a lie by omission in both directions. `9` foundation rows byte-read over complete trees; `EnergyPlus` carries `27` grant paths and `9` families across `11,712` files, including `GPL-2.0`, `GPL-3.0` and `LGPL-2.1`, and the exposure is removable with one compile flag the upstream publishes.**

Every grant located by **complete-tree enumeration** and read with `cat-file blob`; no path guessed, no licence taken from the index.

| Repository | ★ | Grant, byte-read `2026-11-11` | Path | Branch | Region | What it contributes to this register |
|---|---|---|---|---|---|---|
| [`NatLabRockies/EnergyPlus`](https://github.com/NatLabRockies/EnergyPlus) | `1,622` | 🟢 **BSD-3-Clause** · `3,169 B` · `6056c6243093` | `LICENSE.txt` | `develop` | North America | 🟢 **The engine, and it is permissive at the root.** The US DOE's whole-building energy simulation program — the reference implementation every other row on this shelf wraps. `11,712`-file tree, pushed `2026-11-11`. 🔴 **`27` grant paths, `9` families — see the exposure analysis below** |
| [`NatLabRockies/OpenStudio`](https://github.com/NatLabRockies/OpenStudio) | `658` | 🟢 **BSD-3-Clause** · `2,624 B` · `25ae267f7da9` | `LICENSE.md` | `develop` | North America | 🟢 **The SDK, and the layer an agent should actually target.** Cross-platform tooling over EnergyPlus with a measure system — a *measure* is a scriptable, parameterised model edit, which is the natural unit for an agent to emit. 🔵 `copyright.txt` is a **`56,225 B` aggregated third-party notice** (`MIT`+`BSD-3-Clause`), not the project grant |
| [`SEED-platform/seed`](https://github.com/SEED-platform/seed) | `121` | 🟢 **BSD-3-Clause** · `4,610 B` · `630588a10340` | `LICENSE.md` | `develop` | North America | 🟢 **The register's system of record, and it is permissive.** The **Standard Energy Efficiency Data** platform — a web application for managing building performance data at portfolio scale, built for exactly the jurisdictional benchmarking duty described in `intel/market.md`. `1,721`-file tree, pushed `2026-11-11`. 🔵 `docs/source/license.rst` is a `69 B` Sphinx `.. include::` **pointer**, not a grant (`769-D4`) |
| [`SEED-platform/py-seed`](https://github.com/SEED-platform/py-seed) | `4` | 🟢 **MIT *and* BSD-3-Clause in one payload** · `3,416 B` · `03f585916ddc` | `LICENSE` | `develop` | North America | 🟢 **Usable under either.** The API client for the row above — the seam an agent writes through |
| [`NatLabRockies/alfalfa`](https://github.com/NatLabRockies/alfalfa) | `63` | 🟢 **BSD-3-Clause** · `1,679 B` · `6969322757e0` | `LICENSE.md` | `develop` | North America | 🟢 **Usable, and it is the piece that makes a simulation interactive.** A web service for runtime interaction with a running building model — so an agent can *act on* a model mid-simulation rather than only batch-run it. 🔵 A vendored Project Haystack `License.fandoc` in the tree is **unread: `.fandoc` is a format this base's reader does not parse**, and it is vendored |
| [`BBSR-GEG-Portal/webservice-fuer-energieausweise`](https://github.com/BBSR-GEG-Portal/webservice-fuer-energieausweise) | `5` | 🟢 **MIT** · `1,153 B` · `0f9ca359cef6` | `LICENSE` | `main` | EMEA | 🟢 **The duty artefact itself, published permissively by the regulator — and the only time this base has seen that.** The German federal institute **BBSR/BBR**'s own web service for `GEG` energy certificates, with its owner named *inside* the payload. 🔵 Dual: `GPL-3.0` also offered at `LICENSE_GPLv3` |
| [`traccar/traccar`](https://github.com/traccar/traccar) | `8,113` | 🟢 **Apache-2.0** · `11,358 B` · `cfc7749b96f6` | `LICENSE.txt` | `master` | Global | 🟢 **Carried forward from `p768` and re-verified as a control on a second register.** `p768`'s telematics spine is also this register's metering-ingest spine: the same device-protocol and time-series machinery that reads a tachograph reads a sub-meter. 🟢 **Length and `sha256₁₂` reproduce exactly** |
| [`jkbrzt/rrule`](https://github.com/jkbrzt/rrule) | `3,752` | 🟢 **BSD-3-Clause** · `3,493 B` · `6c12f89b62fc` | `LICENCE` | `master` | Global | 🟢 **The cadence engine, re-verified as a known-truth control.** `T661`'s rule holds on a reporting duty: *"DEC annual above 1,000 m²"*, *"定期報告 by 31 July"*, *"ENCE level A from 2027"* are all RFC 5545 recurrences. 🔵 Grant at the British stem `LICENCE` |
| [`getodk/collect`](https://github.com/getodk/collect) | `804` | 🟢 **Apache-2.0** · `10,494 B` · `d1ee81266b96` | `LICENSE.md` | `master` | Global | 🟢 **The field-capture layer, re-verified as a known-truth control for the third consecutive pass.** `p768`'s recorded length and `sha256₁₂` reproduce exactly. A meter reading, a nameplate photo and a floor-area check are form definitions |

### 🔴 The exposure analysis the root grant hides — and the remedy the upstream publishes

`EnergyPlus`'s root is **BSD-3-Clause**. Enumerating the complete tree returns **`27` grant paths across `9` distinct families**, and three of them are copyleft:

| Path | Family, byte-read | What it actually is |
|---|---|---|
| `third_party/eigen/COPYING.GPL` | 🔴 **GPL-3.0** · `35,147 B` · `8ceb4b9ee5ad` | Eigen's legacy licence *option* |
| `third_party/eigen/COPYING.LGPL` | 🔴 **LGPL-2.1** · `26,530 B` · `dc626520dcd5` | Eigen's legacy licence *option* |
| `third_party/eigen/bench/btl/COPYING` | 🔴 **GPL-2.0** · `18,109 B` · `b8d0e2bcbf36` | A benchmark harness, not built into the product |
| `third_party/eigen/COPYING.MPL2` | 🟢 **MPL-2.0** · `16,726 B` · `fab3dd6bdab2` | **Eigen's actual primary grant** |

🟢 **And `third_party/eigen/COPYING.README` is an upstream-published prose licence map that ships its own remedy:**

```
Eigen is primarily MPL2 licensed. See COPYING.MPL2 ...
Some files contain third-party code under BSD or LGPL licenses ...
If you want to guarantee that the Eigen code that you are #including is licensed
under the MPL2 and possibly more permissive licenses (like BSD), #define this
preprocessor symbol:  EIGEN_MPL2_ONLY
```

🟢 **So the copyleft exposure in the register's foundational engine is real, enumerable, and removable with one compile flag that causes a build error if any LGPL header is included.** 🔵 **This is the first time on this base that a copyleft finding came with a mechanical, checkable remedy rather than an architectural quarantine.** `P353` carries it as a build-gate assertion rather than a sentence in a report (`T709`).

🔴 **But the classifier correctly refuses `COPYING.README` itself** — it is a prose map with no operative clause. **A fourth by-reference form, and unlike DEP-5 it is not machine-parseable** (`ACTION p769-D`).

### 🔴 Two grant paths that contain no grant, and a third that is the wrong grant

| Finding | Payload | Why it matters |
|---|---|---|
| 🔴 **An unfilled template is not a licence** | `OpenStudio` carries **three** `LICENSE.md` files whose entire content is `Insert your license here` — `24 B` · `0d980364ebe9`, in BCL measure templates | 🔴 **A probe that asks *"does a `LICENSE` path exist?"* counts all three as licensed.** Stronger cousin of `ACTION p768-B`: there a canonical payload carried no *ownership*; here the payload carries no *grant at all* (`769-D8`, `T710`) |
| 🔴 **The source grant is not the distribution grant** | `EnergyPlus` carries `cmake/license.in.txt` — `9,407 B`, an **END USER LICENSE AGREEMENT** with `@CMAKE_VERSION_MAJOR@` substitution placeholders | 🔴 **A CMake-templated EULA that ships with the *binary installer*.** The repository is BSD-3-Clause for the source; the artefact a client installs carries a EULA. **For a studio that redistributes a built binary these are two different questions, and this base has only ever asked the first** (`T711`, `ACTION p769-E`) |
| 🟢 **A permissive family with no name in its own text** | `third_party/penumbra/vendor/glfw/LICENSE.md` — `904 B` · `149704059b5d` | 🟢 **Zlib.** The payload never states the licence's name, so a family-name matcher cannot see it and it graded `UNRECOGNISED`; the discriminator must be the *as-is warranty plus altered-source-marking* clause pair (`769-D7`) |

### 🔴 The refusals at the foundation tier

| Repository | ★ | Grant, byte-read `2026-11-11` | Verdict |
|---|---|---|---|
| [`ladybug-tools/honeybee-energy`](https://github.com/ladybug-tools/honeybee-energy) | `—` | 🔴 **AGPL-3.0** · `34,523 B` · `8486a10c4393` at `LICENSE`, branch `master` | 🔴 **REFUSE for a hosted deliverable, and this one is a trap.** The Ladybug Tools stack is the most frequently recommended building-energy toolchain in tutorials and teaching material, and its root grant is **network copyleft**. 🔵 Its own `tests/measure/` tree vendors BSD-3 and MIT measures, so a path-scoped read finds permissive files inside an AGPL project |
| [`BIM2SIM/bim2sim`](https://github.com/BIM2SIM/bim2sim) | `101` | 🔴 **LGPL-3.0** · `7,632 B` · `f97bc4bb9b7a` at `LICENSE`, branch `development` | 🔴 **Behind a process boundary only.** BIM-to-simulation model generation (RWTH Aachen) — the IFC-to-energy-model bridge a school estate with BIM records would want. Weak copyleft: linkable, not embeddable. 🔴 **Default branch is `development`** |
| [`Urban-Informatics-Lab/Open-Data-Benchmarking`](https://github.com/Urban-Informatics-Lab/Open-Data-Benchmarking) | `4` | 🔴 **AGPL-3.0** · `32,367 B` · `a116939ba717` at `LICENSE.txt`, branch `master` | 🔴 **REFUSE.** Research code on the feasibility of benchmarking from open data — read the paper, do not take the code. Last pushed `2019-11-06` |
| [`bsl546/energym`](https://github.com/bsl546/energym) | `88` | 🔵 **BSD-3-Clause *and* CC-BY-4.0 in one payload** · `1,790 B` · `a897ed774836` at `LICENSE.txt`, branch `master` | 🔵 **Usable with care.** A building simulation library for control benchmarking. **The code is BSD-3; the accompanying data/models carry CC-BY-4.0 attribution**, which is an obligation on the deliverable's documentation, not on its source. Last pushed `2021-11-17` |
| [`ChangyangOpenSource/carbon-energy-management`](https://github.com/ChangyangOpenSource/carbon-energy-management) | `58` | 🟢 **Apache-2.0** · `11,357 B` · `c71d239df917` at `LICENSE`, branch `main` | 🟢 **Usable.** A Chinese 能碳管理平台 — energy-and-carbon management with statistics. 🔴 **The payload is the GitHub licence-picker template, byte-identical to `mechyai/RL-EmsPy`'s and to `zhitan-ems`'s gateway grant: three repositories, three continents, one fingerprint. It carries no ownership information** (`ACTION p768-B`) |

### 🟢 `ACTION p768-B` corroborated a third time — and its positive complement stated

`11,357 B` · `c71d239df917` appeared **three times this pass**, on a Chinese commercial carbon platform, a US hobby RL wrapper and a Chinese EMS gateway. 🟢 **`evidence/apache-baseline-pair.2026-10-27-p486.tsv` records this fingerprint as the GitHub licence-picker template**, and `p768` proved it byte-identical across a Japanese ministry repository and an abandoned German hobby project. **The prohibition stands and is now evidenced on five unrelated repositories.**

🟢 **The complement, which `p768-B` did not state: a NON-canonical length may carry ownership, and here one does.** BBSR's MIT payload is `1,153 B` — not the `1,063`/`1,069`/`1,070`-ish canonical MIT lengths this base has censused — because the copyright line was **filled in**: `Copyright 2026 Bundesinstitut für Bau-, Stadt- und Raumforschung (BBSR) im Bundesamt für Bauwesen und Raumordnung (BBR)`. 🟢 **Procedure: a grant payload's deviation from the canonical length is the signal that it may be read for ownership; a match to the canonical length is the signal that it may not** (`T712`, `ACTION p769-B`).
