# `P1056` — the SPLIT-SCOPE licence: permissive CODE, CC-licensed CONTENT

**Pass 188 · 2026-10-14 · 16/16 tests passing · validated against live bytes**

## What it detects

A repository whose licence grant is split by SCOPE rather than narrowed in force:
the **code** is permissive (`MIT`/`Apache`/`BSD`) and the **content** — notebooks,
datasets, term lists, slides, schema — is `CC BY` or another Creative Commons licence.

The permissive body is verbatim and unnarrowed, so `P1054` correctly declines to call
such a row restricted. But publishing it as a bare `MIT` is still wrong, and wrong in
the half that matters for an education engagement.

## How it was found

`ACTION MW` ran `P1054` over all `46` rows this KB publishes as `MIT`. Exactly one fired
the SIZE signal with **no** restriction-vocabulary hit — the case `P1054`'s own docstring
predicted it could catch but not name:

```
ktwyw/python-for-engineers   LICENSE   1 328 B   MIT-BODY-PLUS:unclassified-addition   excess 178 B
```

Read over the raw channel, the `178` B is not a narrowing:

> Code in this repository (src/, tests/, *.py) is licensed under the MIT License.
> Teaching materials (notebooks, README files, cheatsheets, datasets created
> for this course) are licensed under CC BY 4.0.

A targeted probe for the same shape found a **second instance**, which declares the split
in a different PLACE — so the channel matters as much as the shape:

> `siskinskai/spedlex`, `README.md` → *"Code: [MIT](LICENSE). Data (everything in
> `data/`, `schema/` and the term lists in `sources/`): [CC BY 4.0](LICENSE-DATA)."*
> Measured: `LICENSE` `1 077` B (MIT) **+** `LICENSE-DATA` `17 023` B (full CC BY 4.0 text).

## Why this vertical needs it as an intake check, not a correction

Education repositories are code **plus** content by construction: a course is notebooks,
a tutor is an item bank, a de-identifier is a term list. **The split-scope licence is the
expected shape here.** And in both measured instances the half a studio actually wants —
the course notebooks, the SPED vocabulary — is the `CC BY` half, which carries an
irrevocable **attribution** requirement. It cannot be silently white-labelled into a
client deliverable.

## The three channels checked

| channel | instance |
|---|---|
| the licence file itself | `python-for-engineers` — split stated above the MIT body |
| a second licence file | `spedlex` — `LICENSE-DATA` holds the full CC BY text |
| the README only | `spedlex` — the `## License` section is where the split is stated |

`P1052`'s path list did **not** include `LICENSE-DATA`, which is why the second-licence
probe missed `spedlex` on its first run. That path is now in the list.

## Declared limits, measured not inferred

- A second licence FILE alone never manufactures a split verdict: a `CC` identifier must
  also be present. Tested.
- `P1056` says **nothing** about a restricted licence that does not borrow a permissive
  body — `No-Suggest/NoSuggest` (`417` B, *"personal non-commercial use only"*,
  *"All rights reserved"*) returns `SINGLE-SCOPE`. 🔴 **`P1054` is blind to it too**, because
  its restriction vocabulary only runs after the MIT-body marker matches. Neither
  instrument is a substitute for reading a sub-`1`kB licence file.
- It is a SCREEN. It prints the scope nouns and the matched second licence so a human
  reads the file.

## Run

```bash
python3 -I test_split_scope.py     # PASS 16/16 — P1056
```
