# `p230-prose-path-ladder` — four registered actions, one scanner

`33` controls, all offline. Wired into `make hooks`.

```
cd compose/code/p230-prose-path-ladder && python3 -I test_prose_path_ladder.py
```

The suite inserts its own directory on `sys.path`, so unlike every earlier
instrument here it passes **from anywhere**, including under `python3 -I`.
That is p229's `ACTION QO` finding fixed at the source rather than worked
around in the recipe.

## What is in here

| file | action | what it does |
|---|---|---|
| `harvest.py` | `TD` + `TA` | one scanner, two harvests: every slug on the shelves (greedy name), and the grant paths the shelves' own prose records |
| `lazy_lint.py` | `TB` | expands a lazy quantifier's target class and its terminator class and intersects them |
| `probe.sh` | `TA` + `TD` | resolves the real default branch, then probes the harvested paths on `raw` |
| `exists.sh` | `TC` | one `git ls-remote --symref` per slug — existence, branch and `HEAD` in a single request |

## `ACTION TD` — the defect, stated exactly

```
p228   ([A-Za-z0-9][A-Za-z0-9_.-]*?)(?=[)\s`,.;:'"\]]|$)     LAZY, terminator holds `.`
p230   ([A-Za-z0-9][A-Za-z0-9_.-]*)(?=[)\s`,;:'"\]]|$)       GREEDY, terminator drops `.`
```

A lazy quantifier stops at the first position where the lookahead can match.
The terminator class contained `.`, which a repository name may legitimately
contain, so `processing/p5.js` harvested as `processing/p5`. Nothing errored —
a shorter, wrong answer was simply returned, which is why eleven passes did
not see it.

`25` dotted names now harvest; `24` were never in p228's `520` at all.

## `ACTION TA` — why a probe list must not be invented

p229 probed `40` paths from a vocabulary it wrote down, and `moodle/moodle` —
the most load-bearing row on these shelves — sat in the grantless class
because `COPYING.txt` was not in it. So p230 harvests the paths these shelves
**already record**, by shape rather than by name.

It worked as a harvester and **refuted its own premise as a ladder**: see
`T230-A1`. A path a shelf recorded is a path at which somebody read *a*
licence. It is not a path at which *this repository* grants.

## Defects found in this instrument before publishing — `8`

| # | what | where it would have shown |
|---|---|---|
| `T230-1` | a clone URL's `.git` suffix read as part of the name | `bruchris/canvas-lms-mcp.git` harvested as a slug |
| `T230-2` | the licence-path shape also matches instruments, predicates and status tokens | `lib/license_family.sh`, `is_licence_path`, `NO_LICENCE_FILE` probed as paths |
| `T230-3` | a hostname-first token read as a path | `apache.org/licenses/LICENSE-2.0.txt` |
| `T230-4` | a probe path that is also a slug on these shelves | `spdx/license-list-data` |
| `T230-5` | the shelves write the FULL raw path, slug and ref included | `moodle/moodle/main/COPYING.txt` probed verbatim |
| `T230-6` | the lint's lookahead capture stopped at `)` — and the terminator class it hunts **begins** with `)` | the first draft scored `0` findings, including on its own positive control |
| `T230-7` | the lint read its own docstring as code | flagged the two lines that explain the defect |
| `T230-8` | a single-line triple-quoted fixture opens and closes its fence on one line, so the docstring tracker lets it through | the lint reported its own positive control as a finding. A fixture now DECLARES itself with `# lazy-lint: fixture` — guessing would be the same class of error the lint hunts |

`T230-6` is the one worth carrying: the first draft of a lint for a
truncation defect was itself truncated, by the same family of mistake, on the
very character the defect is made of.
