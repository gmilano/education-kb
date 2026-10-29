# `p519-liveness-fields` — which GitHub fields carry LIVENESS, and which one lies

🔴 **What it answers.** `p518` retracted [`microsoft/autogen`](https://github.com/microsoft/autogen)
after it had been shelved as live supply in **three consecutive** education cycles: it is archived.
`p519` found the same class again, in permissive LATAM-adjacent supply —
[`menthorlabs/menthor`](https://github.com/menthorlabs/menthor), **Apache-2.0**, **582★**,
`archived: true`, last `pushed_at` **`2024-04-21`** — and identified the field that hides it:
**`updated_at` was `2026-10-12`, seventeen days before the read.**

🔵 **The claim, stated as a rule.** `updated_at` moves when *metadata* moves — a star, a topic, a
description edit. It is **not** a maintenance signal. `archived` and `pushed_at` are. So
`classify()` deliberately **does not take `updated_at` as an input**, and
`updated_at_is_not_liveness()` exists only to *name the rows where reading it would have lied*.

## Files

| file | what it is |
|---|---|
| `liveness.py` | Pure functions: `classify()`, `updated_at_is_not_liveness()`, `permissive()`, `readable_grant()`, `days_between()`. No network, no imports beyond `datetime` |
| `test_liveness.py` | **21 controls**, including the `menthor` case, a live control (`kolibri`), a stale-but-not-archived case, an archived-with-a-fresh-push case, both 365-day boundaries, and a future-push channel error |
| `emit_evidence.py` | Emits `evidence/liveness-fields.2026-10-29-p519.tsv` from **one** saved GitHub search payload, and prints every count `p519`'s prose uses |

## Usage

```
python3 -I test_liveness.py                      # 21/21 controls
python3 -I emit_evidence.py <payload.json> <out.tsv>
```

🟢 **Runs from anywhere.** `test_liveness.py` puts its own directory on `sys.path` explicitly, so
it passes under `python3 -I` **from the repository root and from inside this folder** — the
`p355-cwd-portability` class the `Makefile` header says kept a working gate a one-off for eleven
passes.

🟢 **No egress.** Both entry points are offline: the grader is pure, and the emitter reads a
payload a caller already saved. `Gap 511`'s lesson — a refused channel is not a refused check.

## The two rules it is built around

- 🔵 **Licence assertion, not licence copy.** The TSV's `spdx_asserted` column records a
  **single-licence search assertion** per repo: a query that returns the repo *only if* GitHub's own
  classifier names that SPDX id. `p519` ran two such queries, each carrying a **negative control**
  (`chamilo/chamilo-lms` under MIT; `academico-sis/academico` under Apache-2.0). **Both were
  refused**, so the channel is known to discriminate rather than echo. 13 of 13 positive rows
  agreed.
- 🔴 **`NOASSERTION` is not a licence and is never graded.** `readable_grant()` returns `False` for
  it. `p519` could not read a served licence byte at all — `get_file_contents` is scoped to the
  session's own repositories — so two high-star rows are recorded `UNREADABLE` and shelved
  **nowhere**: not permissive, not blocked. See `Gap 520-B`.

## Derived counts (`2026-10-29`, 16-row payload)

```
rows_written 17   assert_ok 13   served_agrees_with_assertion 13/13
assert_refused_negative_controls 2   no_assertion_possible 2
permissive_and_live 12   archived 1   stale 0   updated_at_would_lie 1
grant_unreadable 2   region_unstated_or_unresolved 12/17
```

🔵 **`Gap 513-E`:** no count in `p519`'s prose was typed by hand — every one is a line of this
script's output.
