# p832 evidence (2026-11-15, thirty-seventh pass)

## Instruments
- `grantprobe832.sh` — P834-safe probe (body written to a FILE, never `$( )`), case-aware filename
  list, tries `main`/`master`/`develop`. Calibrated against `p831`'s repaired figure for
  `sillsdev/libpalaso` (`1,082 B` / `b716617149f3`) before use.
- `resolve-probe.sh` — **D832-1 repair**: resolves heads from `git ls-remote --heads` BEFORE the
  filename loop, then calls the committed `compose/code/p773/grantprobe.sh` unmodified.
  `grantprobe.sh` takes the branch as `$2` and has no resolution step, so one wrong guess 404s all
  31 filenames and prints a verdict byte-identical to a true absence.

## Data
- `known.txt` — 7,125 slugs already held by this base (dedup set, built from all .md).
- `absent.txt` — the 38 addresses adjacent to a standing absence claim in the three graded shelves.
- `sweep.tsv` — those 38 re-probed WITH branch resolution. 3 false absences found.
- `claims.tsv` — all 442 `(address, bytes, sha256)` triples pinned in the three graded shelves.
- `sample.tsv` — reproducible 1-in-7 sample (`awk 'NR%7==1'`), n=64.
- `recheck.tsv` / `verdicts.tsv` — the re-measurement. 38 EXACT, 24 SHORT-BY-1, 2 unresolved.
  Residue 24/62 resolvable = 38.7%; ~171 of 442 extrapolated.

## The decisive test (T111)
A `+1` byte delta is equally consistent with an ordinary upstream edit, so it was not assumed.
Strip the trailing-newline run from today's bytes — exactly as `$( )` would — and hash the
remainder. If the pinned sha returns, the file never changed and the figure is a capture artefact.
**12 of 12 tested reproduced.** Reverse control: `nialvape/utn-mcp`, one of the 8 addresses p831
re-measured by hand, is EXACT. The discriminator is re-measurement, not repair.
