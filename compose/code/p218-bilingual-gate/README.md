# `p218` — the bilingual `ACTION QL` gate, and the corrected pass-boundary test

Two instruments, both offline, both one file each.

## 1. `ql_gate_bilingual.sh` — `ACTION QL`'s precondition, made bilingual

`ACTION QL` (registered p216) says: *no action may be written on a claim of absence until the
shelves have been grepped for the token, slug or family it says is missing.* `T217-2` found the
grep was English and `1 087` lines of the corpus are Spanish.

```sh
compose/code/p218-bilingual-gate/ql_gate_bilingual.sh teacher mentoring licence
```

Each argument is looked up in `bilingual_tokens.tsv` and both halves are grepped over the 8
client-facing shelves. Exit `1` if **either** half returns a hit — i.e. the absence claim is
refuted. Arguments not in the table are grepped literally (that is the right behaviour for a
slug like `bycs-lp/moodle-block_ai_chat`, which has no translation).

**`p218`'s result:** the gate refutes `ACTION QS`'s own absence claim, and `ACTION QP`'s. See
[`evidence/ql-bilingual-register-sweep.2026-10-15-p218.tsv`](../../../evidence/ql-bilingual-register-sweep.2026-10-15-p218.tsv).

**Known limit, and it is the more general finding.** Language was one instance of a wider defect:
`p217` grepped the right tokens *bilingually* (`Profe Gabi`, `docentes noveles`, `induccion`) and
still reached a false conclusion, because the tokens were **entity-scoped** and the claim was
**axis-scoped**. The gate cannot fix that; a reviewer must compare the scope of what was grepped
against the scope of what is claimed. `T218-1`.

**Second limit:** `p415/clase_positiva_v2.py` is **Spanish-only** (`RE_RECHAZO` matches
`no cede|rechaz|sin licencia`). The gates in this corpus are monolingual in *different*
languages, so each is blind to the half the other covers.

## 2. `pass_boundary.sh` — the live/historical test, corrected

`p216` established *"0 live stale cells"* using the **enclosing level-2 heading**. On these
shelves `^## ` is not a pass boundary: the ingest spec itself mandates
`## Opportunities by region`, which appears **53 times** in `intel/market.md` alone.

```sh
compose/code/p218-bilingual-gate/pass_boundary.sh intel/market.md 5388
# HISTORICAL  l.5266: ## Pass 187 — 2026-10-14
#   the bare `^## ` test returns `## Opportunities by region` (l.5291) and calls it LIVE
```

`p216`'s verdict survives; its instrument does not. **`ACTION QO` must not be wired into
`make hooks` with a bare `^## ` test.** Measurements in
[`evidence/pass-boundary-heading-test.2026-10-15-p218.tsv`](../../../evidence/pass-boundary-heading-test.2026-10-15-p218.tsv).
