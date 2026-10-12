# `p144-not-shipped-breadth` — `ACTION DS`

> Test whether `NOT_SHIPPED` is itself over-broad. Re-run all three tiers with each
> `NOT_SHIPPED` directory re-admitted one at a time.
> 🔴 *Refuted if re-admitting any single directory changes a verdict on a row other than
> `librus-mcp`.*

## Verdict: 🟢 **DISCHARGED, falsifier SILENT — but the list is nine-elevenths decoration**

🟢 **No row other than `krzysztofbury/librus-mcp` changes under any re-admission.** The
exclusion list is not doing hidden work, and `T37`'s remedy is not quietly reshaping this
shelf's verdicts.

🔴 **9 of the 11 excluded directory names are completely inert on this population** — 16
subjects across four tiers, and re-admitting them changes nothing at all.

| re-admitted | rows changed | effect |
|---|---|---|
| `legacy_reference` | 🔴 **1** — `librus-mcp` | `BOUNDED_STATIC` 35 literal → 🔴 **`DYNAMIC_UNBOUNDED`, 56 literal + 1 dynamic** |
| `scripts` | 🟡 **1** — `librus-mcp` | 35 → **37 literal**, verdict UNCHANGED (`BOUNDED_STATIC`) |
| `legacy`, `examples`, `example`, `docs`, `doc`, `benchmarks`, `bench`, `samples`, `fixtures`, `tests_native` | 🟢 **0** | 🟢 inert |

🟢 **The baseline reproduces p143 to the row** — librus 35, `edupage-mcp` 31, `DAU-buddy` 40,
`soongpt-plugin` 20, `global-education-mcp` 10 — so the sweep is measuring the same thing p143
published.

## 🔴 `ACTION DS`'s own premise, tested rather than assumed

`ACTION DS` was registered on a specific worry: *"It excludes `scripts/`, and `scripts/` is
where `global-education-mcp` keeps `tool_signatures.py`."*

🟢 **The premise is true**: `scripts/tool_signatures.py` exists in that repository.
🔴 **The inference from it is false**: the file contains **zero** registration sites. It is a
*generator* of signatures, not a site of registration, so re-admitting `scripts/` cannot move
that row and does not.

## 🔴 And the remedy `ACTION DS` proposed would break the row it was built for

> *"…it must be narrowed to `legacy_reference/` alone."*

🔴 **Narrowing to `legacy_reference` alone re-admits `scripts/` and takes librus-mcp from 35 to
37**, because `scripts/qualify_native.py` declares two `@server.tool(...)` sites inside a
throwaway qualification harness. 🟢 **The minimal correct list is
`{legacy_reference, scripts}`** — two names, not one and not eleven.

🔵 **The other nine are retained as unexercised rather than deleted**, and that is now a
recorded fact about them instead of an assumption: a population this shelf has not yet
measured may well ship an `examples/` tree that registers tools.

## Run

```bash
python3 -I ds_readmit.py <subject>=<path> [...]   # JSON: baseline + per-directory changes
```
