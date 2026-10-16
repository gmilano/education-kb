# `p247-path-class` — what KIND of thing did the ladder just fetch?

`59` controls · `bash test_path_class.sh` · wired into `make hooks` · emitted by
`p229-grant-ladder-reach/ladder.sh` as column `10`

## Why it exists (`ACTION XC`, p246)

p246 published **three of its ten raw `NOT-APACHE` verdicts as category errors of its own**:

- `foradian/fedena` and `projectfedena/fedena` were graded on a **`NOTICE`** file — and
  Apache-2.0 distinguishes `LICENSE` from `NOTICE` in its own text;
- `openedx/XBlock` on **`pyproject.toml`** — a manifest `license` field is a CLAIM, not a payload.

The ladder's Tier A **contains** `NOTICE` and its Tier C is **all** manifests, so a consumer
cannot deduce the class from the tier. p246 wrote the column by hand and registered that the
next pass take it from the ladder. This is that.

## Why it is not in `lib/licence_path.sh`

That file's body is a **byte-identical copy** of `p196-none-tree-reach/tree_reach.sh`, and its
own suite fails if it differs by one byte (`P441`/`P237`). Editing it to add a class would turn
it into a fork with another name — the exact defect that control exists to prevent. So
`path_class()` **composes** the shared predicate; the predicate still decides "is this a grant
path?".

## And composing it measured a new error class

`is_licence_path()` answers **YES** on `src/v/security/license.h` and on `license.go` — a C
header and a Go file, because the basename is `license.*`. Not hypothetical: p247's GitHub code
search returned those two exact paths from `redpanda-data/redpanda` as "licence hits". A payload
of C++ graded by a licence classifier answers `UNCLASSIFIED`, and `UNCLASSIFIED` is the branch
that falls to `commercial_use_ok`'s token match (`P171`). So the class is not cosmetic: it is
another route to the same `ALLOWED`.

`SOURCE-FILE` is a **rescue** of the shared predicate, not a file-type classifier: the extension
is only consulted when the predicate has already claimed the path. That is what keeps
`src/main.py` in `OTHER` — a code file that is *not* named like a licence was never at risk.

## The classes

| class | what it tells a consumer |
|---|---|
| `LICENCE-PATH` | gradeable as grant text |
| `NOTICE` | **not** gradeable — Apache-2.0 distinguishes it from its own licence |
| `EULA` | gradeable, but not an open licence; separated so a reader does not count it as one |
| `MANIFEST` | a DECLARATION (`license: MIT`), read by `p222`'s ecosystem grammar, never by the body classifier |
| `SOURCE-FILE` | code named `license.*` — the error class measured above |
| `BUNDLED` | a VENDORED grant: someone else's, not the repository's |
| `OTHER` | none of the above |

`graduable_as_licence <path>` is the one predicate a caller should ask before passing a body to
`family_of`. It exists with its own name precisely because p246 reconstructed that decision at
three call sites and got it wrong at all three.

## Split-scope siblings (p247)

`LICENSE-CODE`, `LICENSE-MIT`, `LICENSE-APACHE` and their variants are classified
`LICENCE-PATH` even though `is_licence_path` does not see them. Measured on `microsoft/autogen`:
root `LICENSE` is `CC-BY-4.0` (the docs, `18 650` B) and `LICENSE-CODE` is `MIT` (the code,
`1 141` B). `ACTION XF` holds the remaining half — a first-match ladder structurally cannot
report a **pair**, and reporting one of two grants is still a category error.

## Usage

```bash
. compose/code/p247-path-class/path_class.sh
path_class "NOTICE"                      # NOTICE
path_class "pyproject.toml"              # MANIFEST
path_class "src/v/security/license.h"    # SOURCE-FILE
graduable_as_licence "LICENSE" && echo "grade it"
bash test_path_class.sh                  # 59 controls
```
