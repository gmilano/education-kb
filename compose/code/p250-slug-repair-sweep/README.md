# p250-slug-repair-sweep — `ACTION XJ` + `ACTION XK`

`probe.sh <slugs-file> <A|AB|ABC>` — one existence request plus a licence-path ladder per slug.

## Why it exists

`ACTION XJ` asked for the component that truncates slugs, not another hand repair. It is
`p228-shelf-gate/harvest_cells.py:17` (a lazy quantifier whose terminator lookahead contains
`.`), a second site at `p129-transcription-audit/bind_tags.py:9`, and — the reason both
survived — `p230-prose-path-ladder/lazy_lint.py`, which **detected them on every `make hooks`
run and returned `0` regardless**. All three are fixed; the lint now fails.

This script is the online half: it reads what the fix made reachable.

## The channels, calibrated before any negative was believed

| channel | good | absent |
|---|---|---|
| `github.com/<slug>/info/refs?service=git-upload-pack` | `200` EXISTS | `401` ABSENT |
| `raw.githubusercontent.com/<slug>/HEAD/<path>` | `200`, `≥1` B | `404` |

🔴 The `401` is new at `p250`. `p249`'s channel map recorded only the `200`, so no pass could
separate an absent repository from a grantless one in a single request.

## Rules it enforces

- **Tier C is a CLAIM, not a payload** (`p246`/`p247` path_class). A manifest `license` field
  is reported as `MANIFEST-CLAIM-NOT-A-PAYLOAD` and never as the grant.
- **`byte-floor=1B`** (`p1058`): a `0`-byte payload is an absence, not a grant.
- **`ABSENT` always means absent-at-the-paths-probed** (`p222`), never "unlicensed".
- 🔴 **A grant-sha collision proves one row ONLY in the holder-embedding tier.** Short `MIT`
  payloads (`~1 070` B) carry a copyright line and discriminate. Stock texts do not: `AGPL-3.0`
  at `34 523` B collided across two *unrelated* repositories this pass
  (`TouchRefletz/maia` vs `TouchRefletz/maia.edu`). See `ACTION XN`.

## Results it produced

- `p250-slug-repair-sweep.2026-10-16-p250.tsv` — 30 recovered + 26 stumps, read first-hand.
- `p250-xk-tier-bc.2026-10-16-p250.tsv` — the 11 LMS connectors at 41 paths each, which
  overturned `p249`'s "the connector layer has no grant".
