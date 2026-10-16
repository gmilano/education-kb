---
industry: education
region: Global
updated: 2026-10-16
---

# `P251-B` — `ACTION XN`: the `maia` class, a truncation that lands on a **real** repository

Artefacts and suite of the **two-hundred-and-fifty-first pass (2026-10-16)**.
🟢 **`20`/`20` green under `python3 test_prefix_collision.py`.**

## Why the pass needed the instrument

`p250` measured the instance: [`TouchRefletz/maia`](https://github.com/TouchRefletz/maia)
and [`TouchRefletz/maia.edu`](https://github.com/TouchRefletz/maia.edu) are two
**different live repositories** whose existence, default branch, grant family,
licence byte count **and pinned licence sha** all agree — the sha because stock
`AGPL-3.0` text names no holder, so it collides across unrelated projects. No
payload-side gate in this repository can separate them. The only remaining
discriminator is the **shelf text**: one address is a strict prefix of the other.

## 🔴 `XN`'s own prescription is the wrong scope, and the suite proves it

XN asked for *"a harvested slug that is a strict prefix of another slug **on the
same line**"*. 🔴 **That rule does not trip its own falsifier.** On
[`agents/top.md`](../../../agents/top.md) the real row is line `44` and the
stump is line `45` — one address per table row, so **no line holds both**.

🟢 **So the scopes invert:** the **file** is where a collision is detected, and
the **line** is what *exempts* one, because a pass that documents a truncation
writes both forms on the same line, as `p250` did.

## The four-part conjunction, each part measured

A bare strict-prefix rule at file scope returns **`235`** pairs over these eight
shelves. The verdicts:

| verdict | count | what it is |
|---|---|---|
| `WARN` | `145` | a `-`/`_`/alnum continuation. `moodle/moodle` and `moodle/moodle-docker` are ordinarily two real repositories |
| `DOCUMENTED` | `47` | every occurrence of the stump shares a line with a longer form |
| `IGNORED-PATH-FRAGMENT` | `37` | a **branch** or a directory in the owner slot: `main/LICENSE` vs `main/LICENSE.md` is a raw-URL path, not a slug |
| 🟡 `REFUSE-ANNOTATED` | `6` | a bare stump on a line that says so in words (*"the stump"*, *"harvests to"*) |
| 🟢 `REFUSE` | **`0`** | an unannotated bare stump — **what the gate fails on** |

🟢 **`0` hard refusals means these shelves currently carry no live dot-truncation
of the `maia` class.** 🔵 The `6` annotated ones are `p250`'s own warning row
and `p247`'s many-to-one collapse note — the documentation of the defect, not
the defect.

## 🔴 The false positive this instrument had to be taught about

`published_as_url("JushBJJ/Mr", text)` is **`False`** even though
`"github.com/JushBJJ/Mr" in text` is **`True`**: the long address
`github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor` *contains* the stump. A terminator
lookahead is the fix, and the naive form is kept in the suite as a control so
the measurement cannot be re-introduced quietly.

## Runner

```
python3 sweep.py agents/top.md agents/trending.md ...   # TSV, counts on stderr
```
