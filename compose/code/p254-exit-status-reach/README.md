# `p254-exit-status-reach` — `ACTION XZ`

**The question:** when a step fails, does anything hear it?

`p253` found `gate-offline` printing `ALL OFFLINE LICENCE CONTROLS PASS` with a failing suite
and registered `ACTION XZ` to ask the same of every other target. This is the discharge.

## What it found

```make
claims: ## ACTION UG — THE GATE: run before publishing any "there is no X"
	@$(PY) -I …/carried_index.py claims "$(TOKEN)" . || true
```

`carried_index.py claims` returns **1 exactly when the shelves already claim the token** —
exit 1 *is* the STOP signal, and it is the whole purpose of the recipe. `|| true` discarded
it. Measured:

| | |
|---|---|
| `carried_index.py claims moodle .` | prints `ALREADY CLAIMED … STOP`, **exits 1** |
| `make claims TOKEN=moodle` | prints the same `STOP`, **exits 0** |

`p253`'s gate could not HEAR its controls. This one could not SPEAK. Same shape: *a signal
exists, is correct, and nothing consumes it.*

`make carried` had the adjacent defect — `CARRIED` and `NEW` both exited 0 — which is why
`ACTION YB` ("make the carried-index check a GATE, not a grep") could not land. Both are
fixed; `CARRIED` → 1, `NEW` → 0.

## Grades

| grade | meaning | can the step fail? |
|---|---|---|
| `GUARDED` | ends in `\|\| exit 1` | yes |
| `CONSUMED` | plain command; make consumes the status | yes |
| `SWALLOWED-TRUE` | `\|\| true` | **no** |
| `SWALLOWED-PIPE` | an **instrument** piped into a formatter | **no** |
| `SWALLOWED-SUBST` | runs only inside `$(…)` in an `echo` | **no** |
| `IGNORED-PREFIX` | `-cmd` | **no** |
| `REPORT` | a pipeline that only formats a file an already-consumed step wrote | n/a — nothing to lose |
| `INERT` | `echo`, `cd -`, a comment | n/a |

`REPORT` exists because the first run of this instrument was **wrong**: it flagged `exists`
for its closing `awk … | sort | uniq -c`. Silencing a *formatter* costs nothing; silencing an
*instrument* costs the verdict. Both controls are pinned.

## Usage

```sh
python3 -I exit_reach.py Makefile            # the census
python3 -I exit_reach.py --verify Makefile   # exit 1 if a CONTRACTED line cannot fail
python3 -I test_exit_reach.py                # 19 controls
```

A target is `CONTRACTED` when it publishes a verdict something else may act on. `status`,
`reach`, `index` and `gate-mit-tier` are deliberately uncontracted — recorded here so a later
pass does not read their absence from the contract as an oversight.

Every negative control is reproduced **in bash**, so each grade is pinned to a measured
behaviour of the shell rather than to a reading of it. That rule is `p253`'s: two passes
audited the gate by reading the recipe and neither found the defect that one run exposed.
