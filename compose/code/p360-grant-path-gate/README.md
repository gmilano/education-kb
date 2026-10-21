# `p360` — the grant-path currency gate, and the four revisions that were wrong

**What this answers.** For every row on these shelves that claims a grant at a path,
does that path still exist on the repository's **live default branch**, and does it
serve? A grant-path cell is the one assertion on this base that silently rots: the
repository stays live, the licence stays unchanged, and the *branch* gets renamed.

## Channels

Two, because they are the two that are open (`api.github.com` has been **403** for five
consecutive passes):

| Channel | Used for |
|---|---|
| `git ls-remote --symref` | liveness, and the **live** default branch |
| `raw.githubusercontent.com` | the licence payload, and whether a path serves 200 |

## The rule, and why the first four were wrong

A row asserting *"there is no `LICENSE`"* and a row asserting *"the grant is at
`main/LICENSE`"* contain the same words. Four revisions tried to separate them by
vocabulary and all four failed:

| Rev | Rule | False accusations | Real defects |
|---|---|---:|---:|
| 1 | split the cell on its first slash | 5 | 0 |
| 2 | resolve the cell against the live default branch | 7 | 0 |
| 3 | exclude rows whose prose asserts an absence | 2 | 0 |
| 4 | require a positive SPDX token in the row | 2 | 0 |
| **5** | **structural: a grant path is `` `branch/FILE` ``** | **0** | **0** |

Revision 1 broke on `master/canvas-lms-mcp/LICENSE` — a grant **at depth**, which is
`ACTION ZZ-u`'s shape — and on `dmitry-viskov/pylti1.3`, whose slug ends in a dot
segment that trailing-dot stripping turned into a dead address.

Revision 4 is the instructive failure: the licence token it required sits **inside the
refuted claim** (`本项目采用 MIT License`, `Apache-2.0, Ruby on Rails`), so requiring it
selects exactly the rows it should skip.

**Revision 5 needs no keyword list.** This base writes a real grant as
`` `branch/FILE` ``, always with a slash; a bare backticked `` `LICENSE` `` is always
prose — a path asked for, or a path probed and 404.

## Running it

```sh
python3 -I grant_path_gate.py agents/top.md repos/foundations.md \
    verticals/solutions.md compose/patterns.md intel/market.md
```

Exit status is non-zero if any cell fails. Result at `p360`:
**215 of 215 canonical cells agree, 0 failures, 0 false accusations.**

`probe_address.py` is the companion discovery instrument: liveness, default branch,
licence read from the payload over an orthography/extension ladder (`ACTION ZZ-q`),
classification keyed on the **title and version line** (`ACTION ZZ-bg`), and the
copyright-holder line captured as a field (`ACTION ZZ-be`).

```sh
python3 -I probe_address.py slugs.txt      # one owner/repo per line
```

## Two cautions carried from `p360`'s own use of these

- 🔴 **The holder field is wrong, not blank, on GPL-family rows.** It returns
  `Free Software Foundation, Inc.` because the GPL text carries the FSF's copyright on
  the licence document ahead of any project notice. A comparison keyed naively on that
  string reports every AGPL row as a copy of every other one.
- 🔴 **`UNCLASSIFIED` is a result, not a failure.** `sira313/rapkumer` carries a bespoke
  Indonesian non-commercial licence; the classifier refusing to guess is what kept it
  out of a permissive count.
