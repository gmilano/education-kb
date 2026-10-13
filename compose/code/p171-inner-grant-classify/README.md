---
industry: education
region: Global
updated: 2026-10-13
---

# `p171-inner-grant-classify` — `P171-A`, and the four formatting defects that shaped it

**Pass 171, 2026-10-13.** `ACTION JK`: classify the inner grant BODIES that `P170-A` counts, by
family, deduplicated by blob.

`P170-A` step `2` decides **IF** a candidate carries a grant. This is the step after it: **WHICH**
grant, and is it compatible with the outer one.

## What it answered

| repo | `P170-A` paths | source-file over-read | DOCUMENT bodies | blobs | hostile |
|---|---|---|---|---|---|
| `sakaiproject/sakai` | `129` | **`0`** | **`129`** | `72` | **`0`** |
| `moodle/moodle` | `193` | **`105`** | **`88`** | `80` | **`0`** |

`0` bodies in either repository withhold commercial use or redistribution. `gap 115`'s anxiety was
procedural.

## The four defects, all caught by the regression tests rather than by the tally

Every one was **formatting, not law** — which is `T224`, and the reason the tests exist:

1. **A family name matched anywhere in the body** read `LGPL-2.1` as dual `GPL+LGPL`, because
   LGPL-2.1 §`3` offers relicensing under the ordinary GPL **in prose**. A prose reference is not a
   second grant. → families now come from a **line-anchored TITLE**; prose references go in a
   separate `prose_mentions` column.
2. **`licenses/junit-3.8.1.license.txt`** was read as `GPL+MPL+Python`. It is the **IBM Public
   License 1.0** — a family the predicate did not know, so every hit was a prose reference inside
   IPL's own comparison clauses. Wrong on all three families at once. → `IPL-1.0`, `CPL-1.0`,
   `CDDL`, `EPL`, `MPL` named explicitly.
3. **Hard wrapping.** Legal text wraps at ~`70` columns, so LGPL-2.1 contains
   `GNU General Public\nLicense` and a flat phrase search **misses** it. The regression test caught
   this when the fixture matched nothing the real body did. → whitespace normalised before any
   phrase match; titles stay line-anchored.
4. **Markdown.** `# Apache License` (Moodle's bundled `aws-sdk`) and
   `[GNU General Public License ...](http://...)` (Moodle's bundled TinyMCE, a `300` B `license.md`)
   defeated the line-anchored and phrase patterns respectively. → Markdown heading markers and
   emphasis stripped before title matching; GNU **short-form** notices added as grant sentences.

Plus one carve-out that is not a defect but a trap: **GPL-3.0 §`6(b)`** permits one alternative
conveying method *"only occasionally and noncommercially"*. That is a condition on a distribution
**method**, not a non-commercial restriction — and it made `4` of Moodle's `6` raw hostile hits,
**Moodle's own `COPYING.txt` among them**. Every full GPL-3.0 body trips a naive search.

## Files

| file | what it is |
|---|---|
| `classify.py` | the predicate. `FAMILY_TITLES` (line-anchored), `FAMILY_SENTENCES` (grant-is-the-sentence), `MENTIONS` (prose, informational), `HOSTILE`, and the GPL §`6(b)` carve-out |
| `extract.sh` | the driver. Applies `P170-A` step `2` verbatim so the denominator reproduces p170's count, and emits NUL-delimited `path\0blob\0body\0`. Works against a `--filter=blob:none` partial clone, so blobs are fetched for candidates only |
| `test_classify.py` | **`10` of `10`**, offline. The first five cases are the five this instrument first got **wrong** |

## How to run it

```sh
git clone --filter=blob:none --no-checkout --depth 1 https://github.com/moodle/moodle /tmp/moodle
./extract.sh /tmp/moodle > moodle.records
python3 -I classify.py "moodle/moodle" "GPL-3.0" < moodle.records
```

## What it does NOT do

- It does not read a **dependency closure** — only the grant documents present in the tree.
- It does not decide whether a third-party **notice** in a `licenses/` manifest constitutes
  *"copyleft inside the repository"*. `Sakai`'s `3` reciprocal bodies all sit there and `0` copyleft
  grant governs Sakai's own code; whether that satisfies `ACTION JK`'s falsifier is **counsel's
  reading**, and the artifact records it as fired-on-the-letter rather than declaring it silent.
- It does not check that the component named in a manifest **filename** matches what that component
  actually ships. It does not, and `gap 117` exists because `3` of Sakai's do not.
