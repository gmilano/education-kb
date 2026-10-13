---
industry: education
region: Global
updated: 2026-10-13
---

# `P169-A` step `0` — the fold, and why a licence gate needs one

Artifacts of **pass 169 (`2026-10-13`)**. Runs the half of `ACTION JE` that corrects the instrument
rather than the shelf.

## What went wrong first

`ACTION JE` ran `P168-A` step `2` — *canonical word diff* — across the `12` agent rows. One row came
back looking alarming:

| body | bytes | vs canonical | first reading |
|---|---|---|---|
| `plastic-labs/tutor-gpt` `LICENSE` | `35 149` | 🔴 **`71` added / `71` removed words** | 🔴 *"a `GPL-3.0` body that has been rewritten"* |

🔴 **It had not been rewritten. The canonical copy was the problem.**

SPDX publishes its licence texts reflowed and typeset: `246` curly quotation marks and `1` `©` glyph in
`GPL-3.0-only.txt`. The FSF's own ASCII body carries **`0` of each**. Every one of those glyphs becomes
a word-level difference, and `71` of them survive whitespace normalisation.

After folding the four typographic classes, the same comparison reads **`1` added / `1` removed** — and
the single word is `philosophy/why-not-lgpl.html` against `licenses/why-not-lgpl.html`.

🟢 **Which is exactly the hunk p168 identified, by a different instrument, on a different repository, as
the entire `2`-byte spread that defeated its band test.** Two passes, two methods, one answer.

## The script

```sh
./licence_fold.sh <canonical-file> <repo-body-file>   # -> added<TAB>removed
```

It normalises **four classes and nothing else**, so a real textual change still shows:

| class | from | to |
|---|---|---|
| curly double quotes | `U+201C` `U+201D` | `"` |
| curly single quotes | `U+2018` `U+2019` | `'` |
| copyright glyph | `U+00A9` | `(C)` |
| URL scheme | `http://` | `https://` |

That last one is p168's own finding: the FSF revised its text's URLs, so the scheme difference is a
revision marker, never a deviation.

## Results — unfolded against folded, on real bodies

See [`result.2026-10-13-p169.tsv`](result.2026-10-13-p169.tsv).

| body | unfolded | folded | verdict |
|---|---|---|---|
| `tutor-gpt` `GPL-3.0` | 🔴 `71` / `71` | 🟢 **`1` / `1`** | 🟢 **CLEAN — the one word is the FSF URL revision** |
| `penecho` `AGPL-3.0` | 🟡 `3` / `3` | 🟢 **`0` / `0`** | 🟢 **CLEAN — verbatim** |
| `Echo-Loop` `AGPL-3.0` | 🟡 `3` / `3` | 🟢 **`0` / `0`** | 🟢 **CLEAN — verbatim** |
| `ChatTutor` `AGPL-3.0` | 🟡 `3` / `3` | 🟢 **`0` / `0`** | 🟢 **CLEAN — so its `1`-byte spread from the other two is trailing whitespace** |
| `DeepTutor` `Apache-2.0` | 🔴 `40` / `29` | 🔴 **`40` / `29`** | 🔴 **DEVIANT — unchanged by the fold, which is the point (`T206`)** |
| `ai-shifu` `Apache-2.0` | 🟡 `2` / `5` | 🟡 **`2` / `5`** | 🟢 **CLEAN — `[yyyy]` and `[name of copyright owner]` filled in** |

## The tests exist to stop the fold from becoming a whitewash

🔴 **A fold that silences a real modification is worse than no fold at all**, because its output looks
authoritative. So `test_licence_fold.sh` is weighted toward controls:

```
ok    tutor-gpt GPL-3.0 is clean at one word          (1  1)
ok    penecho AGPL-3.0 verbatim                       (0  0)
ok    Echo-Loop AGPL-3.0 verbatim                     (0  0)
ok    ChatTutor AGPL-3.0 verbatim                     (0  0)
ok    DeepTutor Apache-2.0 still deviant after folding (40 29)
ok    ai-shifu Apache-2.0 placeholder only            (2  5)
ok    identity: canonical vs canonical                (0  0)

7 passed, 0 failed
```

🟢 **Cases `5`, `6` and `7` are the ones that matter.** Case `5` asserts that `DeepTutor`'s altered
section `4(d)` stays loud. Case `6` asserts that a filled-in placeholder stays visible as a small
bounded diff rather than being normalised away. Case `7` is identity.

Every fixture is a real body read at p169 from `raw.githubusercontent.com`, pinned at the HEAD sha
recorded in [`../../../evidence/agent-grant-surface.2026-10-13-p169.tsv`](../../../evidence/agent-grant-surface.2026-10-13-p169.tsv).

## What this does not fix

🔴 **Step `6` still cannot complete in this container.** `fsf.org` and `gnu.org` are unreachable
(`T211`), so `GPL`/`AGPL` pointers resolve to nothing — which must be recorded as **unresolved**, not
as broken.
🔴 **The fold says nothing about which licence a body IS**, only whether it matches the canonical text
you handed it. Step `1`'s title-line probe still chooses the canonical file, and choosing the wrong one
makes a clean body look substituted.
