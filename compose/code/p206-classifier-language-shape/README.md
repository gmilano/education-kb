# p206 — language- and shape-tolerant licence classification

Drop-in replacement for [`../p205-grant-classifier-fix/classify.sh`](../p205-grant-classifier-fix/classify.sh).

p205's finding — **a licence names itself on a line of its own, so classify on that line** — is
correct and is kept unchanged. What p206 adds is everything that line can be *wearing*.

## How the defects were found

Not by argument. `ACTION PI` asked for this KB's published licence column to be re-run end to end
with p205's classifier. 281 distinct repositories carrying a copyleft token in a published table
row were re-read from their own blobs at the `HEAD` ref across 22 path forms. The column came back
clean — **0 published cells change family** — but the *instrument* returned no determinate family
on **25 of 281 rows**. Those 25 are the fixtures below.

## The defects, each reproduced on a real body

| # | defect | p205 returns | truth | fixture |
|---|---|---|---|---|
| D1 | markdown heading breaks `^[[:space:]]*` — `### GNU GENERAL PUBLIC LICENSE` | `GPL-unversioned` | `GPL-3.0` | `cerpus/Edlib`, `idempiere/idempiere` |
| D2 | a `====` underline or blank line pushes `Version 3` to line 4; the window was 3 lines | `GPL-unversioned` | `GPL-3.0` | 13 Moodle-plugin rows, e.g. `cgrevisse/moodle-qbank_genai` |
| D3 | **the licence is not in English** — `LICENÇA PÚBLICA GERAL AFFERO GNU` | `UNRECOGNISED` | `AGPL-3.0` | `portabilis/i-diario`, `portabilis/pre-matricula-digital` |
| D4 | `Elastic License 2.0` is absent from the table — and it is **non-OSI** | `UNRECOGNISED` | `NON-OSI-Elastic-2.0` | `canyongbs/advisingapp` |
| D5 | narrative grant, no title line at all | `UNRECOGNISED` | `AGPL-3.0-STATEMENT` | `ankitects/anki` |
| D6 | 19 bytes: `License: GNU GPL V3` — a reference, not an instrument | `UNRECOGNISED` | `GPL-3.0-STATEMENT` | `frappe/education`, `UD_Spanish-AnCora` |
| D8 | a **UTF-8 BOM** sits between `^` and the title, and is not `[[:space:]]` | `GPL-unversioned` | `GPL-2.0` / `GPL-3.0` | `OS4ED/openSIS-Classic`, `Berserk-hub150/moodle-ai-skill-navigator` |
| D10 | a **wrapped prose line** puts a licence name at column 0 — `GNU General Public License for more details.` | `GPL-unversioned` | `GPL-3.0-STATEMENT` | `pawtograder/platform` |

`D7` is not a classifier defect and is recorded because **p206's own probe caused it**: an Apache
`NOTICE` is an attribution file, not a licence body. It carries a grant *statement* and belongs in
p204's channel taxonomy beside `package.json`. p206 added `NOTICE` to the body path list, got
`foradian/fedena` back, and **removed it again**. The body path list is 22 forms, not 23.

## What the fix is

1. **Fold accents and strip the BOM before matching.** `tr` and `grep -i` are byte-oriented here, so
   `LICENCA` case-folds and `LICENÇA` does not — the defect
   [`../p288-agpl-casefold/`](../p288-agpl-casefold/) first recorded, met again in a second
   alphabet. Folding first lets one ASCII pattern match every variant. Folding is done with
   per-character substitutions, **not** a bracket class: `[Çç]` would match the individual *bytes*
   of a UTF-8 sequence and corrupt the text instead of folding it.
2. **Undress the title line** — strip markdown hashes, bold stars, blockquote markers and inline HTML.
3. **Widen the window to six lines**, enough for title / underline / blank / version plus the FSF
   address block. Still a window: GPL §13 is ~600 lines down and can never reach it.
4. **Walk the candidate title lines and skip prose.** A title names the licence and stops; a wrapped
   prose line keeps going. Candidates carrying ` for `, ` as `, ` under `, ` published by `, ` more `
   and friends are skipped, and the first clean one wins.
5. **Add `Elastic License 2.0`**, and Portuguese/Spanish GPL and AGPL titles.
6. **Add a `-STATEMENT` class**, gated on the first 15 lines. It is load-bearing in exactly the way
   p205's `-DEED` is: it names the family without letting anyone quote the text as the licence.

## Result

| | p205 instrument | p206 instrument |
|---|---|---|
| `UNRECOGNISED` | `9` | 🟢 **`0`** |
| `GPL-unversioned` | `16` | 🟢 **`0`** |
| `CC-unversioned` | `1` | 🟢 **`0`** |

Full census: [`../../../evidence/pi-licence-column-census.2026-10-14-p206.tsv`](../../../evidence/pi-licence-column-census.2026-10-14-p206.tsv).
Row-by-row delta: [`../../../evidence/instrument-delta.2026-10-14-p206.tsv`](../../../evidence/instrument-delta.2026-10-14-p206.tsv).

**16 of the 25 had lost their GPL *version*, and that is the commercially load-bearing half.**
`GPL-2.0` and `GPL-3.0` are not interchangeable: no patent grant in `GPL-2.0`, no `Apache-2.0`
inbound compatibility, no anti-tivoization clause. A studio that reads `GPL-unversioned` and assumes
`GPL-3.0` has assumed a patent grant that is not there.

## Use

```bash
. ./classify.sh
classify_grant "$(curl -sS https://raw.githubusercontent.com/OWNER/REPO/HEAD/LICENSE)"
./test_classify.sh    # 20/20, offline, on 20 real bodies
```

`NO NETWORK` in the suite: every fixture is committed. The reads are performed inline by a pass,
per p203's seam.
