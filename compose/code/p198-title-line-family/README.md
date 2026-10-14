# `P197` — Classify a licence on its TITLE LINE, not on a window

## The defect this closes

Two traps, same shape, different families. Both make a *window* classifier name the wrong
licence, and both are properties of the **canonical** text, so no amount of corpus curation
avoids them:

| trap | family | the sentence that does it | a window classifier returns |
|---|---|---|---|
| `§13` *(known — `P171`, `p206` D2, pass `77`)* | `GPL-3.0` | *"13. Use with the GNU Affero General Public License."* | `AGPL-3.0` |
| **preamble** *(NEW, `p197`)* | `GPL-2.0` | *"(Some other Free Software Foundation software is covered by the GNU Lesser General Public License instead.)"* | `LGPL?` |

The second is **inside the first 40 lines**, so it is not reachable by shrinking the window:
widening or narrowing a window cannot fix a window, for the same reason `P441` holds that
widening a filename list cannot fix a list.

## The rule

Scan lines in **document order** and classify on the FIRST line that matches a licence-title
pattern. The real title always *precedes* the preamble sentence or the section that names a
sibling licence, so document order defeats both traps with one rule.

Pattern order must NOT decide the answer. The pre-`p197` control in this directory checks
`lesser` before `general`, which is why it mislabels every pristine `GPL-2.0`.

## Negative controls (required cases, all from SPDX `license-list-data` over the raw lane)

| fixture | bytes | pre-`p197` control | 🟢 `p197` |
|---|---|---|---|
| `GPL-3.0-only` | `34 674` | `GPL-3.0` | `GPL-3.0` |
| `GPL-2.0-only` | `17 337` | 🔴 **`LGPL?`** | 🟢 **`GPL-2.0`** |
| `AGPL-3.0-only` | `34 020` | `AGPL-3.0` | `AGPL-3.0` |
| `LGPL-3.0-only` | `42 098` | `LGPL-3.0` | `LGPL-3.0` |
| `LGPL-2.1-only` | `26 001` | `LGPL-2.1` | `LGPL-2.1` |
| `MIT` | `1 078` | `MIT` | `MIT` |
| `Apache-2.0` | `10 280` | `Apache-2.0` | `Apache-2.0` |
| `ECL-2.0` | `11 111` | `ECL-2.0` | `ECL-2.0` |

`GPL-2.0` is a **required** case here, exactly as `GPL-3.0` is in `lib/test_license_family.sh`:
a classifier validated only on the families it already gets right scores 100% while broken.

## Declared limits — read these before reusing it

1. **The grant detector is ENGLISH-ONLY.** A translated licence body scores `GRANT?-NON-EN`,
   which is a property of this instrument, not of the document. `formalms`' Italian, French,
   German, Spanish and Portuguese texts all land there.
2. **One file, one family.** A file carrying SEVERAL notices (`foradian/fedena`'s bundled
   `fckeditor/license.txt`, `66 467` B, tri-licensed `GPL`+`LGPL`+`MPL`; `H5P.CKEditor`'s
   `2 167` B) gets the FIRST title only. `P441`'s `names_multiple` column exists for this and
   is still the right channel for it.
3. **Byte counts must come from a BINARY read** — see the `p198` addendum below.
4. It reads **one path**. Choosing *which* path to read is not this instrument's job — see
   `p198-root-licence-sweep/` for why a first-match filename list gets that wrong.

## Why this is re-derived rather than reused

`lib/license_family.sh` is the canonical classifier and `lib/test_license_family.sh` its
suite. 🔴 **Neither could be EXECUTED this pass** — `bash <repo script>` is denied by the
session's permission classifier *(`[Code from External]`)*. `P0a` found the prior art and it
was cited, not re-invented; the re-derivation is forced by the lane, not by failing to read
the register. The fix below belongs in `lib/license_family.sh` and a `GPL2_PREAMBLE` case
belongs in its suite, **both unrun and therefore not shipped into `lib/` this pass.**

## 🆕 `p198` addendum — read the file in BINARY

🔴 **A byte count taken through Python text mode is LF-normalised, not the file's size.**
Universal newlines collapse `\r\n` to `\n`, so a CRLF licence loses one byte per line:

```
  Lumi H5P.BranchingScenario-1.8/src/fonts/LICENSE.txt
    wc -c      = 11 560
    text mode  = 11 358      <- what this instrument first published
    CRLF count =    202      <- exactly the delta
```

Found by **cross-validation**: a concurrent pass read `11 560` where this one said `11 358`.
`true_bytes.py` in this directory is the fix — it reads `rb`, reports `len(raw)`, and reports
the CRLF count alongside the family so a reflowed text is visible **as reflowed** instead of
surfacing later as an unexplained band failure.

**Blast radius, measured rather than assumed: one row.** Every other text read that pass is LF
with `delta 0`, and the three `OWN-GRANT-AT-ROOT` payloads were independently confirmed
byte-for-byte by the concurrent pass. The band table in `intel/trends.md` therefore stands —
but it was computed from text-mode counts, which is why this fix matters more than the one row
it corrected.
