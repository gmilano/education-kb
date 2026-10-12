---
industry: education
region: Global
updated: 2026-10-12
---

# `p145-not-shipped-property` — `ACTION EA`: the falsifier is silent across 52 repositories

🟢 **`ACTION EA` DISCHARGED, falsifier silent.** Over **52 repositories** — including the
**28 that are not among this shelf's 16 surface subjects** — there are **46
`NOT_SHIPPED`-named trees**, and only **two** bear a tool registration. 🟢 **Both are
`legacy_reference` and `scripts`, both in `krzysztofbury/librus-mcp`**, the one row that
motivated the list in the first place.

## What was registered

> 🟡 **`ACTION EA`** — apply `T39` to the `NOT_SHIPPED` list properly. For each of the nine
> inert names, state the property-bearing test: could a tree with that name ever hold a
> shipped tool registration? Replace the blanket list with the two names `P144-H` proves
> are load-bearing plus an explicit rule.
> 🔴 *Refuted if any of the nine names can be shown to bear a registration in a real
> repository outside this shelf's 16 subjects* — which would mean the list is a sound
> heuristic that this population simply does not exercise, and it should be kept whole.

🟢 **The falsifier named a population this KB already holds.** The 44-row origin census
includes 28 repositories outside the 16 subjects, so the condition is evaluated on evidence
rather than on the rows that produced the hypothesis.

## Result, per name

| name | trees found | bearing a registration | verdict |
|---|---|---|---|
| `legacy_reference` | 1 | 🔴 **1** | 🔴 **LOAD-BEARING** (`librus-mcp`) |
| `scripts` | **22** | 🔴 **1** | 🔴 **LOAD-BEARING** (`librus-mcp`) |
| `docs` | **13** | 🟢 **0** | inert across 13 trees |
| `fixtures` | 6 | 🟢 **0** | inert |
| `examples` | 2 | 🟢 **0** | inert |
| `benchmarks` | 1 | 🟢 **0** | inert |
| `tests_native` | 1 | 🟢 **0** | inert |
| `bench`, `doc`, `example`, `legacy`, `samples` | 🔴 **0** | — | 🔴 **never appear at all** |

🔴 **Five of the twelve names do not occur once in 52 repositories.** They are not
heuristics this population fails to exercise — they are names nobody uses. 🟢 **`docs` at
13 trees and `scripts` at 22 are a real sample**, and `docs` bears nothing in any of them.

## 🟢 The rule that replaces the list

🔵 **`P144-I` already proved the minimal correct list is `{legacy_reference, scripts}`.**
This probe adds the reason it is correct, and the reason generalises past this list:

> **A tree is excluded only when it does not bear the property being measured — and that
> is a question to test, not a name to match.**

🔴 **The blanket list stands in for that test, and 10 of its 12 names stand in for
nothing.** But the list is not merely redundant: 🔴 **`scripts` is load-bearing and inert
at the same time** — it carries a registration in `librus-mcp` and in none of the other 21
trees that bear the name. A name-based rule cannot express that; a property-based one can.

🟢 **And `P145`'s `SKIP_DIRS` finding is the same rule failing in the other direction.**
`dist`/`build` were excluded by name, and on 7 of 8 npm packages the excluded tree was the
only tree there was. 🔵 **One rule, two lists, opposite errors: naming a tree is not
measuring it.**

### What the rule looks like in code

`surface_gate3.py` implements the positive half — `payload_trees()` admits a built tree
when, and only when, the package's own declared entry point resolves inside it. 🟡 **The
negative half is not yet implemented**: `NOT_SHIPPED` is still a name list, now known to
need only two entries. Replacing it with reachability from the declared entry point is
registered for p146 rather than asserted here, because it would change `librus-mcp`'s
published 35 and that change needs its own falsifier.

## Limits

- 🟡 **`is_mcp_server` is not applied per tree.** A `docs/` tree bearing a registration in
  a repository that is not an MCP server at all would read `YES` here. 🟢 **No tree bore
  one, so the question did not arise** — stated because a different population would
  make it matter.
- 🔴 **Registration is detected, reachability is not.** A `scripts/` tree can bear a
  registration that nothing ever runs; that is exactly `librus-mcp`'s shape and exactly
  why the list was introduced.

## Run it

```
python3 not_shipped_property.py "<subject>=<path>" …
```

Results: [`result.2026-10-12-p145.tsv`](result.2026-10-12-p145.tsv),
summary: [`summary.2026-10-12-p145.txt`](summary.2026-10-12-p145.txt).
