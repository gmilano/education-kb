# `p454-apac-registry` — `Gap 453-D`, the regions that had never been searched

`Gap 453-D` recorded the institution-registry layer as *"two regions deep and three
never searched"*, naming **Global** and **APAC beyond India (Japan, Indonesia, the
Philippines)**, and called it the best-value leg available.

## Result

**Indonesia closes.** Dapodik (*Data Pokok Pendidikan*) is the Ministry's single
register of schools, teachers and students — closed, no open core — and its client
layer is **MIT at three strata in three languages**:

| repo | grant (first-hand, `HEAD`) | stratum |
|---|---|---|
| `ardianryan/dapodik-sdk` | MIT · 1 739 B `29e7d361ee3d` | register, typed TS/JS SDK |
| `adereksisusanto/dapodik-api-php` | MIT · 1 105 B `ce39902853af` | register, PHP client |
| `smantriplw/vervalpd-node` | MIT · 1 068 B `0ae5076b1e03` | student identity (VerValPD) |
| `bantenprov/dapodik-data-guru` | MIT · 1 072 B `3508ba25c5ad` | provincial teacher aggregate |
| `pipeworx-io/mcp-estat-japan` | MIT · 1 070 B `42501667035e` | Japan e-Stat, **general** statistics |

Fabricated control `nope-p454-dapodik/nope-p454` dead on all 15 probed paths.

## What the leg yields measure, and why it matters more than the rows

`Gap 453-B`'s shelf rule was *"prefer a named system of record"*. Tested here over
4 legs × 3 registries, it holds **with an amendment**:

| term | shape | candidates | education assets | precision |
|---|---|---|---|---|
| `dapodik` | long, distinctive proper name | 4 | 4 | **100 %** |
| `e-stat` / `gakko kihon chosa` | named service | 47 | 1 | 2 % |
| `deped` | **5-letter acronym** | 59 | 0 | **0 %** |
| `psa` | **3-letter acronym** | — | 0 | **0 %** |

`deped` matches the substring `dep` across all of Packagist — `deptrac`, `php-di`,
`symfony/dependency-injection`. `psa` matched ConnectWise PSA, PureScript `psa`,
Oracle `oci-psa`.

**Amended rule:** a system-of-record name only beats a common noun when it is
**orthographically distinctive**. `dapodik`, `vervalpd`, `ecoledirecte`, `pronote`
qualify; `deped`, `psa`, `npsn`, `uis`, `isced` do not, and a leg spent on them buys a
homonym list.

## The Philippines is an informed absence, not a silence

No Philippine *school*-registry asset surfaced; the cause is the term, not the country.
What did surface is a different stratum — the **PSGC** administrative-geography layer
(`pcofilada/psgc`, `jobuntux/psgc`, `anthonygacis/psgc-js`, `aivangogh/ph-address`) —
whose grants were **not** read first-hand and are therefore **not** celled. The DepEd
register (EBEIS/LIS) is not reachable from any package registry searched, and the
unambiguous term for it has **not** been identified. That is the actionable half.

## Channel note

The GitHub **search** API is deliberately not used: this session's scope permits reads
of the attached repositories only, and a repository-discovery search would reach outside
it. That is a **scope** limit, not the host `403` earlier passes recorded — stated so a
later pass does not re-attribute it.
