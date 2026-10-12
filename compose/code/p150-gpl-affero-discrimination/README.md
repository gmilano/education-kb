---
industry: education
region: Global
updated: 2026-10-12
---

# p150-gpl-affero-discrimination — `T77`: this shelf cannot see a GPL row

🔴 **Five of seven GNU-family rows on this shelf carry the wrong licence identifier**, and
the cause is one line of published code.

## The defect

`p145-licence-census.identify()` — copied verbatim into `p147-licence-language` and
`p149-common-title-licence` — carries this rung and applies it with `rx.search(body)`
over the **whole** licence text:

    (re.compile(r"GNU AFFERO GENERAL PUBLIC LICENSE", re.I), "AGPL-3.0"),

🔴 **GPL-3.0's own section 13 is titled *"Use with the GNU Affero General Public
License"***, and its body names the Affero licence twice more. So every verbatim GPL-3.0
file matches the AGPL rung before the GPL rung is reached.

🔴 **The same defect runs through the whole family.** GPL-2.0's preamble says *"you may
want to use the GNU Lesser General Public License instead"* — so a GPL-2.0 file matches
the **LGPL** rung. Each GNU licence names its siblings, which is exactly what a
body-substring test cannot survive.

🔵 **`T39`'s class again**: an instrument answering the question it was spelled to ask.
The phrase is right and the *test* is wrong, because the phrase occurs in the body of the
licence it is meant to exclude.

## Measured reach on this shelf

🔴 **`p145-licence-census` publishes `AGPL-3.0` 6 times, `LGPL` once, and `GPL` NEVER** —
on a shelf whose own pages describe several rows as GPL-3.0 by hand. 🔵 **A whole licence
class is invisible**, because the AGPL rung consumes every GPL-3.0 file first.

| row | published | measured | direction |
|---|---|---|---|
| `Agso-o/sigaa-calendar` | 🔴 `AGPL-3.0` | 🟢 **GPL-3.0** | 🔴 **OVERSTATED** |
| `despedite/siu-guarani` | 🔴 `AGPL-3.0` | 🟢 **GPL-3.0** | 🔴 **OVERSTATED** |
| `mhlavac/edupage-mcp` | 🔴 `AGPL-3.0` | 🟢 **GPL-3.0** | 🔴 **OVERSTATED** |
| `ahmedEid1/lumen` (agent tier) | 🔴 `AGPL-3.0` | 🟢 **GPL-3.0** | 🔴 **OVERSTATED** |
| `qxbao/qldt-hanu-mcp` | 🔴 `LGPL` | 🟢 **GPL-2.0** | 🔴 **WRONG FAMILY + no version** |
| `edwyj/ddl-killer` | 🟢 `AGPL-3.0` | 🟢 **AGPL-3.0** | 🟢 right |
| `fabrica-de-inovacao/expeditto` | 🟢 `AGPL-3.0` | 🟢 **AGPL-3.0** | 🟢 right |

🟢 **Two rows are genuinely AGPL-3.0**, which is why the defect survived: the matcher is
not always wrong.

🔵 **The direction is OVERSTATEMENT, which is the safe direction and still wrong.**
AGPL-3.0 obliges source disclosure to users interacting over a network; GPL-3.0 does not.
Three connector rows and one agent row have been presented to a studio as unusable behind
a hosted tutor when they are ordinary GPL. 🔴 **And `qldt-hanu-mcp` runs the other way**:
GPL-2.0 has **no patent grant** and no section 13 at all, and was filed as `LGPL`, the
most permissive member of the family.

## The fix: read the TITLE, confirm on the CLAUSE

A GNU licence states its identity on a **title line** in the first few lines. The name
must *be* the line, not appear somewhere in a window — otherwise the fix fails the same
way the defect does, only over fewer lines.

| surface | what it reads | why it is independent |
|---|---|---|
| **title** | the licence name as a whole line, plus the version on it or the next line | a sentence is never just a licence's name |
| **clause** | AGPL-3.0's §13 *"Remote Network Interaction"*, anchored to line start | this is the clause that *makes* AGPL different; a plain GPL file cannot contain it |

🟢 **`agree()` returns a verdict only when both surfaces say the same thing** and reports
`DISAGREE` otherwise, so a hand-edited or dual-licensed file is named rather than guessed
at. 🟢 **`spdx()` carries the version** where the family needs one — `GPL-2.0` and
`GPL-3.0` are different instruments, and this shelf had been publishing neither.

## Run it

    python3 run_gpl_affero.py <dir-of-clones> [<more dirs>] > result.2026-10-12-p150.tsv
    python3 test_gpl_affero.py      # 35 tests, authored fixtures, offline

🟢 **28 trees measured, 4 `OVERSTATED`.** The fixtures reproduce both licences at the only
two places that matter — the title line and section 13 — so the suite needs no clone and
no network.

## 🔴 What this does NOT do

- 🔴 **It does not re-publish the 44-row census.** The three copies of `identify()` in
  `p145`, `p147` and `p149` are **unchanged**, deliberately: correcting them in the pass
  that measures them is the mistake `ACTION EU` exists to avoid, and the mistake `ACTION
  FE` was registered to undo. 🔵 **Registered as `ACTION FN`.**
- 🔴 **It does not verify SPDX short-ids against a licence list.** `GPL-3.0` here means
  "the title says GPL and the version line says 3"; it does not distinguish
  `GPL-3.0-only` from `GPL-3.0-or-later`, which lives in the per-file headers, not the
  licence body. 🔵 **Registered as `ACTION FO`.**
- 🔴 **`moodle-mcp-server-aql`'s `AGPL-3.0` is untouched by this**: it is a `PKG_ONLY`
  row, read from a declared `package.json` string, not from a body match. 🟢 **Its value
  stands.**
