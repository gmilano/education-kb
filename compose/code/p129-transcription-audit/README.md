# `p129-transcription-audit` — a published figure, checked against the evidence file that produced it

**Pass 129, 2026-10-11.** `./test_p129.sh` → **21 passed / 0 failed**, fully offline, 13 fixtures.

## What this instrument is for

p128 established a true rule about `git`: `ls-remote --tags` emits two lines per **annotated** tag,
`refs/tags/X` and `refs/tags/X^{}`, so counting lines inflates a release count by the number of
annotated tags. It then attributed this KB's wrong tag figures to that rule.

**The attribution was wrong, and the evidence was already in this repository.**
`compose/code/p108-release-identity/census.sh` subtracts dereferences — its committed
`result.2026-10-10.tsv` carries a `tags_uniq` column — and on **13 of 13** disputed addresses that
file agrees **exactly** with an independent re-measure taken today. The wrong numbers were typed
onto the pages.

So the defect class this instrument addresses is **transcription**, and the gate it provides is:
*diff what a page says against what the repository's own committed evidence says.* No network, no
API, no model.

## The parts

| file | what it is |
|---|---|
| `count_tags.sh` | The counting rule as a pure function over an `ls-remote --tags` dump on stdin → `lines⇥deref⇥real⇥latest`. Exists so the rule is testable with no network |
| `measure_tags.sh` | `count_tags.sh` against a live address over the git lane |
| `tag_date.sh` | A tag's commit date **without the GitHub API** (403 here): `git init` + `fetch --depth 1 refs/tags/X` + `log -1 --format=%cI`. This is how *"a dated release"* became a decidable explanation |
| `bind_tags.py` | Binds every `N tags` figure on a page to an ADDRESS and diffs it against an evidence TSV. Usage: `bind_tags.py <repo-root> <evidence.tsv>` |
| `holder.py` | Reads the HOLDER line out of a licence payload on stdin → `family⇥verdict⇥holder⇥n` |
| `repair_tags.py` | Writes a re-measured figure onto every live site and marks the old value |
| `out/*.tsv` | This pass's evidence: 79 + 15 tag measurements, 359 holder reads, 59 `NOTICE` probes |

## The four rules this instrument had to learn, each asserted in `test_p129.sh`

1. **The correction apparatus is a SCOPE, not a token.** A figure inside
   `⚠️ **was 194 tags**<!--corrected-->` is the record of a retracted claim and must never be read as
   a live one, nor re-corrected. Without this rule the diff reported **51** disagreements where
   there are **17**.
2. **The marker goes OUTSIDE the emphasis span it corrects.** `**108 tags ⚠️ **was 194 tags**…`
   closes the figure's own bold at the marker and renders as literal asterisks.
3. **A holder notice opens with a year or a bracketed field.** A bare `^copyright` pattern matches
   GPL-3's wrapped prose (*"copyright on the Program, and are irrevocable"*) and returns that
   sentence as the licensor.
4. **A licence text's own steward is not the work's licensor.** `Copyright (C) 2007 Free Software
   Foundation, Inc.` in a GPL payload is `DOCUMENT-TEXT` (p125's label), and the placeholder inside
   *"APPENDIX: How to apply the Apache License"* is instructions, not a grant — so the operative
   text is truncated at that boundary before the holder is read.

A fifth, learned the hard way: **a family detector must test the non-OSI families first.** BSL-1.1
names MIT as its *Change License*, so a scan for `"MIT License"` reads
[`sdv-dev/sdv`](https://github.com/sdv-dev/sdv) as MIT. This KB's own pages, which hold it as
BUSL-1.1 on nine sites, refuted the new instrument before it published anything.

## Order of operations — this matters and it cost p126 a pass

Run the repair **before** the pass prepends its sections. Prepending moves every coordinate below
the insertion, which is how p126's committed `path:line` evidence became unlocatable (`P126-A`).

```
bind_tags.py  <root> out/tags-measured.2026-10-11.tsv   # 1. diff pages against evidence
repair_tags.py <root> --apply                            # 2. repair, append-only pages refused
prepend the pass sections                                # 3. only now
bind_tags.py  <root> out/tags-measured.2026-10-11.tsv   # 4. self-audit
```

## Known limits, pre-registered rather than hidden

- 🔴 **`bind_tags.py` binds 207 of 470 figures (`P129-D`).** It needs an inline address in the same
  table cell. Blind to: a short name in backticks with no address, a bare figure in a tag column,
  and a slash-separated ordinal list (`26 / 6 / 23 tags`, where it binds `23` to a repository with
  **6**). The repair this pass shipped was therefore driven by `(project name, old value)` pairs
  over all live pages. **`ACTION AX`** fixes the binder with a clause forbidding regression on any
  of the 37 repaired sites.
- 🟡 **`holder.py` does not read source headers.** For the 46 Apache-2.0 / ECL addresses with no
  holder in `LICENSE` and no `NOTICE` at all, the licensor is probably in the file headers —
  **`ACTION AY`**, clause of 20 of 46.
- 🔵 **Two column spellings remain outside the correction-form vocabulary**: *"the section below
  says"* and *"the page said"* in some prose forms. This pass used only registered spellings
  (`published`, `stale`, `reads`, `measured`) rather than widen the vocabulary again.
