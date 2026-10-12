# `p151-gnu-population-reach` — `ACTION FU`: `T77`'s reach over all **58**

🟢 **DISCHARGED, falsifier SILENT.** The GNU-family population is **SEVEN** at the licence-file
surface, measured over all 58 census subjects and independently of what the census published.

| measurement | value |
|---|---|
| subjects walked | **58** (50 github clones + 8 `npm pack` payloads) |
| subjects shipping a licence file | **39** |
| of those, carrying a readable TITLE line | 🟢 **39 — all of them** |
| GNU-family population by the TITLE surface | **7** |
| GNU-family population by the RETIRED matcher | **7** |
| rows where the two surfaces disagree | 🔴 **5** — and they are the five `T77` named |
| rows shipping more than one licence file | **0** |
| `ACTION FU` falsifier (population > 7) | 🟢 **SILENT** |

🔵 **Why p150 could not answer this.** It took the seven rows the census had *published* as
GNU and measured those — circular in one direction: able to find a row mis-sorted *within*
the family, unable to find one sorted *out* of it. p150 said so and registered the action
instead of arguing. This module reads every licence file's title line regardless of what
was published.

🟢 **The result the action did not ask for, and the more useful one: coverage.** 39 of 39
licence files carry a readable title line, so retiring the body matcher costs **nothing**.
A narrower surface that answered less often would have been a trade; this one is not.

🔴 **The eighth GNU-family row, named so it is not later found as a correction.**
`moodle-mcp-server-aql-0.1.7` declares `AGPL-3.0` in `package.json` and ships no licence
file. It is GNU-family at the *declaration* layer and `T77` cannot touch it — there is no
body to mis-read. **8 GNU-family ids across 58 rows; 7 of them read from a body.**

🔵 **The falsifier's mechanism is demonstrated, not just described.** `test_population.py`
builds the two shapes that would have fired it — a GPL `LICENSE` under an `MIT`
`package.json`, and a GNU file that quotes the Apache licence (which the retired ladder
sorts to `Apache-2.0`, *out* of the family). The module catches both. The shelf holds
neither; that is the measurement.

- instrument: [`population.py`](population.py) · **31 tests**, all offline, authored fixtures
- result: [`result.2026-10-12-p151.tsv`](result.2026-10-12-p151.tsv) ·
  [`summary.2026-10-12-p151.txt`](summary.2026-10-12-p151.txt)
- the shared surface it imports: [`../lib/licence_identity.py`](../lib/licence_identity.py)

```
python3 test_population.py
python3 population.py /tmp/edu-trees /tmp/edu-npm/trees
```
