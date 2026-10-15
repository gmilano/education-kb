# `p213-grant-resolver` — the four grant shapes a path→family map cannot express

Pass 213 ran `P212-A`'s scope-aware licence gate against a new population and broke it four
times. This directory holds the acceptance fixtures and the probe that found them.

## Why `P212-A` is not enough

`P211-A` classified a grant as a scalar. `P212-A` upgraded it to `{path-glob → family}` after
[`pupilfirst/pupilfirst`](https://github.com/pupilfirst/pupilfirst) proved a title-anchored read
blocks an `MIT` platform. Four repositories read on 2026-10-15 are outside that model too.

| fixture | ★ | shape | what breaks |
|---|---|---|---|
| [`andymatuschak/orbit`](https://github.com/andymatuschak/orbit) | 1.8k | **router + election + tense + carve-out** | Root `LICENSE` is 457 B and grants nothing. Libraries are `Apache-2.0`; `packages/app` and `packages/backend` are `AGPL-3.0-or-later` **OR** `BUSL-1.1` at the licensee's choice; official compiled binaries are carved back to `Apache-2.0`; the `BUSL` converts to `Apache-2.0` after 3 years. A glob maps to a **set**, not a family. |
| [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) | 159 | **external authority** | Code `MIT`. Data is partitioned by **dataset identity and access tier** — `Open` (`CC-BY-4.0` majority, `CC0` minority), `Open + Gated` (split at download level), `Gated` (**no open licence**) — resolved from a remote catalog the file says can change between releases. The partition key is not in the repository. |
| [`codeforlife-education/aimmo`](https://github.com/codeforlife-education/aimmo) | 117 | **owner boundary** | A 115-byte `LICENSE.md` that names **no family at all**, pointing at `ocadotechnology/codeforlife-workspace` — which serves `AGPL-3.0`, 32 920 B. Reading only the repo's own blob records `ungranted`; the true answer is the strongest copyleft in this industry. |
| [`chipmates/agoracosmica`](https://github.com/chipmates/agoracosmica) | 149 | **tense** | Code `AGPL-3.0` (34 523 B). Content is **copyright now**, scheduled to `CC-BY-4.0` "within 6–12 months" of the May 2026 launch. A cached verdict is wrong on a schedule. |

## The `orbit` trap worth its own note

`orbit`'s root `LICENSE` names `LICENSE.Apache-2.0`, `LICENSE.AGPL-3.0-or-later` and
`LICENSE.BUSL1.1`. All three return `404`. The real files use **hyphens**:

```
LICENSE-Apache-2.0          10 142 B
LICENSE-AGPL-3.0-or-later   34 523 B
LICENSE-BUSL-1.1             3 893 B
```

A resolver that trusts a licence file's own cross-references gets three `404`s and emits a false
`ungranted` on a repository whose grant is fully shipped. **Try both separator spellings.**

## Pipeline (replaces `P212-A` steps 1–3)

1. Classify as today: riders first, then title-anchored, then `STATED`-not-`BODIED`.
2. **Router test, before accepting `UNRECOGNISED` or `ABSENT`.** A blob under ~800 B that names
   families, names sibling files, or contains a URL is a router — resolve it. Follow in-repo
   references (both separator spellings) and cross-owner references, recording the boundary.
3. **Emit a set** where the text says "your choice".
4. **Flag `TEMPORAL`** where a conversion or relicensing date is named.
5. **Flag `EXTERNAL`, refuse to cache**, where authority sits outside the repository.
6. Gate the paths you actually ship, against the resolved map.

## Acceptance test

The four fixtures above plus `pupilfirst` (`P212-A`) and `odoo` (`P211-A`). A gate correct on all
six is correct on every shape this KB has met in 213 passes.

## Files

- `fetch_grants.sh` — reads a licence blob at `HEAD` over 19 path forms, one slug per stdin line,
  emitting `repo, path_form, http, served_bytes`. Byte counts are the blob **as served**
  (`T208-8`), which is *not* `classify.py`'s `bytes` field — see `T213-8`, where the two diverge
  on 1 of 73 blobs by 200 B.
- Classification reuses `../p211-full-column-grant-audit/classify.py` unchanged.
