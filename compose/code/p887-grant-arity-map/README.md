# `p887-grant-arity-map` — `886-G1`'s acceptance test, executed over the 15 rows `p886` left open

## What it answers

`886-G1` asks that every shelf row carry **(a)** a grant **map** from path to family — derived by
`git clone --depth 1 --filter=blob:none --no-checkout` + `git ls-tree -r`, not by probing a path
list — and **(b)** an `AND`/`OR` determination read from any `LICENSING.md` / `NOTICE` /
`THIRD_PARTY_NOTICES.md`, recorded with its byte count and `sha256₁₂`.

`p886` completed 4 of 19 rows (`EduWork`, `EduWork-ECNU`, `proctor`, `iiab`). This instrument did
the remaining **15**.

## `886-G2(a)` compliance record, filed because the gap requires it

`make ladder-audit` was run **before a line of this instrument was written**: **919 ladders across
510 instruments**, of which **37** are already `TREE-ENUMERATED`
([`record`](../../../evidence/ladder-audit-886G2.2026-11-18-p887.tsv)).

| | |
|---|---|
| **Reused, unmodified** | `p370-git-tree-payload/probe_tree.sh` — the transport (blobless partial clone, depth 1, no checkout) |
| **Reused, unmodified** | `p427-conjunctive-grant::classify` — the AND/OR call (`886-G1` part b) |
| **Reused, unmodified** | `p228-shelf-gate::classify` — family per payload |
| **NOT reused, with the reason** | `p370`'s enumeration is `ls-tree --name-only HEAD`, **root only**; `886-G1` needs a path-keyed map, which a root listing cannot express. `-r` added; nothing else changed. |
| **No new ladder** | Selection is a **regex filter over names git reported**. *A ladder can only refute the paths it tried; an enumeration has no paths to miss.* |

🔴 **And it recurred anyway.** The reused `p228` classifier is earliest-title-wins, and
`repos/foundations.md`'s own note records `p880` misclassifying `apereo/java-cas-client` with exactly
that approach. This instrument returned `BSD-3-Clause` on a payload that grants under **Apache-2.0
AND BSD-3-Clause**. See `887-G1`.

## The two numbers, and why both are needed

- **`arity_own`** — distinct families among `OWN` grants. **This is what a licence cell may be
  derived from.**
- **`arity_all`** — distinct families across the whole tree, vendored included. **This is the
  notice-obligation surface.**

🔴 **The first run reported only the second and called it "the arity".** It gave `6 / 15` rows at
`arity > 1`, and the number was meaningless: `HKUDS/DeepTutor` carries `web/vendor/thinking-orbs/`
(MIT) and **is** Apache-2.0; `deepseek-ai/deepseek-harness` carries fourteen vendored MIT copies and
**is** MIT; `OpenVidu/openvidu`'s second family is a bundled **font** licence. Publishing any of
those as a two-family grant would be a wrong cell on a client-facing shelf. Corrected: `arity_own > 1`
on **`1 / 15`**.

## Two defects this instrument found in itself, before any cell was written

1. **A filter that accepted `src/license_checker.go` as a licence grant** — `_checker` matched its
   suffix group and `.go` its extension group. Control `R-5` failed. Fixed with a **type filter on
   the final dotted segment** that **fails closed**.
2. **Every `NOTICE` read as a grant payload** — `notice` was in `GRANT_NAME` and `is_payload` was
   tested *before* `POLICY_NAME`. `apereo/phpCAS` (3,914 B) and `yetanalytics/lrsql` (19,985 B) both
   came back `arity=2 Apache-2.0+BSD-3-Clause`; both are Apache-2.0 at root. Fixed: policy first,
   `notice` out of the grant filter.

🔵 **And the exception that proves a blanket exclusion would be wrong:** `phpCAS`'s `NOTICE` really
does carry a second grant — a full New BSD body © 2003-2007 The ESUP-Portail consortium. Read, not
assumed (`886-G4`'s rule).

## Run

```
python3 test_arity_map.py                                    # 45 offline controls
python3 -I arity_map.py --slugs slugs-886G1-remaining.txt \
        --out ../../../evidence/arity-map-886G1.2026-11-18-p887.tsv \
        --work /tmp/p887-work                                # ONLINE: 15 blobless clones
```

A cached clone in `--work` is reused, so a re-run costs no network.
