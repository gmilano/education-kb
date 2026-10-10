# p1035 — re-grant recheck, the holder split, and WHICH ECL text

Authored and executed in **pass 105, 2026-10-10**. Three limbs, one per
pre-registered lead of pass 104. `test_p1035.sh` is offline and must pass
before any limb is believed: **33 passed, 0 failed**.

## Limb A — `regrant.sh` (lead #2)

Re-probes the 23 `LIVE-NOGRANT` and 3 `LIVE-NOCONTROL` rows of
`p1029-lost-address-recovery/result.2026-10-10.tsv`, with the identical
filename list and 200-control discipline, so the diff is mechanical.

**Result: `probed=26 absent=0 grant_appeared=0 still_nogrant=23 still_nocontrol=3`.**
Zero of 26 changed. Two instruments, two passes, one set of numbers — which
is a *calibration* of pass 104 and a negative answer to the lead. A licence
does not appear in the hours between two passes of the same date; the useful
re-probe cadence for this limb is **days, not intra-day passes**.

## Limb B — `holder.sh` (lead #1)

Pass 104 found eight Spanish/Portuguese-NAMED rows and refused to call them a
LATAM finding, because a repository's name is not its region. This limb reads
the tree: a copyright holder line, an institutional marker in the README, and
a country word, and reports **which string did the placing**.

| slug | placed by | region |
|---|---|---|
| `xgabrielcv/auto-matricula-sigaa-unb` | `SIGAA` | LATAM |
| `dreathward/sistema-de-aprendizaje-en-linea` | `uan.edu.co` | LATAM |
| `mietiainvestigacion-creator/api-eduadapt` | country word `Colombia` | LATAM |
| `kaiman-p/tutor-adaptativo-ia` | — | UNPLACED |
| `alvarogregori/moodle-ai-graded-assignment` | — | UNPLACED |

**Answer: 3 LATAM, 0 EMEA, 2 unplaceable** — not the 5 pass 104 would not
claim, and not the 2 it feared.

### The bug this limb found in itself

The first `place_string` placed any `universidad de ...` string in **EMEA**.
`api-eduadapt` names **Universidad de Córdoba**, which exists in Córdoba,
**Spain** *and* Córdoba, **Colombia**. The rule did not read a region; it
invented one. Corrected: an institution name alone returns `UNPLACED`, and
only a ccTLD, a country word, or a nationally unique system name (`SIGAA`,
`UNAM`) places a row. `api-eduadapt` is now LATAM **by the country word in its
own README**, and the `placed_by` column says so on every row.

This is `P1005` — read the payload, do not infer from the label — applied to
**region** instead of to licence.

## Limb C — `ecl.sh` (lead #3)

Pass 104 recorded four Apereo-lineage byte counts for one declared licence and
noted that `P1025` forbids treating size as identity. This limb pins each
payload by full `sha256` and reports what the text itself declares.

| payload | bytes | sha256 (16) | repos |
|---|---|---|---|
| A | 11 120 | `0688f62d04f14e4b` | `sakaiproject/sakai` |
| B | 11 340 | `76a975068930323e` | `opencast/opencast` |
| C | 11 087 | `a9ea5cca8da2c8d5` | `lap-sakai-extractor` |
| D | 9 919 | `fb10d1260ddc8dff` | `LearningAnalyticsProcessor`, `OpenDashboard-api`, `OpenDashboard-legacy` — **byte- and `sha256`-identical** |

**Six repositories, four distinct texts, and all six declare ECL 2.0 of April
2007.** Payload D is one text shared by three repositories, not three.

### The finding that matters more than the identities

`classify_payload` — the classifier every recent census of this KB runs on —
returns **`UNRECOGNISED`** for all six. Measured cause: **the ECL-2.0 text
contains zero occurrences of the string `Apache License`.** It names the
"Apache 2.0 license" in lower case. So the classifier does **not** mislabel ECL
as Apache; it fails to see it at all, and a **permissive** row then lands in
*neither* the permissive nor the copyleft bucket.

`classify_ecl` is added here as the correct reading. ECL-2.0 is the Apache-2.0
text with section 3's patent grant narrowed to education: **permissive, and
buildable on.**

## Files

- `regrant.sh`, `holder.sh`, `ecl.sh` — the three limbs
- `classify.sh` — copied unmodified from `p1029`, so the audit tests the
  classifier this KB actually runs
- `test_p1035.sh` — offline tests, including regressions for **both** bugs this
  pass found in its own code
- `result.regrant.2026-10-10.tsv`, `result.holder.2026-10-10.tsv`,
  `result.ecl.2026-10-10.tsv`
- `lost-addresses.*.txt` — the three input lists. Named into the pattern
  `p1026`'s census guard already excludes, and each declares itself an
  instrument input on line 1 (`P1034`).
