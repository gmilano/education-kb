# `p678-filing-gate` — assert every "filed to" claim against the file it names

**Discharges `ACTION p677-B`.** `p677-A` found that `p597`'s promotion ledger named a shelf
file for `11` addresses and was wrong about `7` of them — `6` absent from all shelves, `1` on a
different shelf than claimed — with one address claimed-as-filed by two passes `25` days apart
while absent the whole time. Nothing in the pipeline had ever read the destination file.

This is that check. No network, no model, no API: it reads the ledger and `grep`s each address
against the path its own `filed_on` cell names.

## Run

```bash
python3 -I compose/code/p678-filing-gate/gate.py          # whole ledger
python3 -I compose/code/p678-filing-gate/gate.py p678     # one pass's own filings
```

Exit `0` = every claim true. Exit `1` = at least one false, each printed with its reason.

## Result at p678

| Scope | Claims checked | True | False |
|---|--:|--:|--:|
| p678's own filings | `9` | **`9`** | `0` |
| whole ledger, first run | `403` | `396` | `7` |
| whole ledger, after the parser fix below | `403` | `402` | **`1`** |
| whole ledger, after correcting that cell | `402` | **`402`** | **`0`** |

## Two things this gate taught at p678, both worth keeping

🔴 **1. Five of the first seven "failures" were the gate's own defect, not false claims.**
A `filed_on` cell may read `agents/top.md:p661-correction` — a path *plus an anchor note*. The
first version treated the whole cell as a path, got `FileNotFoundError`, and reported
`SHELF FILE MISSING` against five rows whose filings were in fact correct. **A gate that reports
a false positive teaches the pipeline to ignore it**, so the anchor is now stripped
(`cell.split(':', 1)[0]`) before the path is opened. This is the same lesson as `p647-L` /
`667-B` — a scorer needs its own controls — applied to a publication gate rather than a search leg.

🟢 **2. The one surviving failure was real, and it is `p677-A`'s rarest class.**
`learningequality/kolibri-design-system` claimed `compose/patterns.md,repos/foundations.md`.
The second half is true; the first is false. **A multi-shelf claim is several claims, and they
fail independently** — so the remedy was to drop the false half, not to repoint the whole cell.
Corrected at p678.

## Controls

The gate asserts both signs before reporting, and fails loudly if either control breaks:

- **positive** — a known-filed address (`moodlehq/wiki-rag`, filed to `agents/top.md` at p678)
  must be found;
- **negative** — a nonsense address (`zzqxnonsense/p678-control`) must not be found.

Without these, a gate that silently read an empty string would report `0 FALSE` and look like success.

## Standing recommendation

Run it before every commit. It is `O(shelves)` file reads with the shelf bodies cached, costs
nothing, and it is the only check in this base that reads the **destination** rather than the
measurement.
