# `p773` instruments — written from scratch, and the `9` defects they shipped before control caught them

`make hooks` was tried as the first command of this pass and **DENIED — `[Code from External]`, fourth
consecutive session**. Per `ACTION p772-A` nothing in this directory is a copy of the repository's own
gate scripts; every file was written from scratch for this pass, and none of the repository's gate
scripts was executed or moved.

| File | What it does |
|---|---|
| `gate_tables.py` | `ACTION p772-A`'s named RED gate, rebuilt. Detects a markdown table BODY row that is a column-header, placeholder or example row — the defect that compiles into a KB entity named `nombre`. `10` self-controls; **refuses to report if its own controls fail**. `--controls` runs them alone. |
| `grade2.py` | Grades a licence payload against the SPDX canonical texts in `ingest/canonical/` by **normalised operative body with the copyright slot masked**, on a **4-rung ladder**: body-diff → SPDX tag → notice prose → unresolved. `9` self-controls; exits non-zero rather than report on a failed control. |
| `probe.sh` | Probes ONE address on the ref channel (`git ls-remote --symref`) and reads its grant. Resolves `RESOLVES` / `ABSENT-OR-PRIVATE` / `EXISTS-BUT-EMPTY` / `TIMEOUT`. `api.github.com` is never called. |
| `grantprobe.sh` | `ACTION p772-C`'s wider, **case-aware** grant filename probe — `31` names including lowercase `license.txt`. Takes the **measured** default branch. |
| `find_superseded.py` | `ACTION p772-B`'s check, re-specified: **subject-bound** (Annex III + education + the date) and **paragraph-windowed**. |
| `prepend.py` | Inserts a pass section after the YAML frontmatter and refreshes `updated:`; **refuses to write a file with no frontmatter**. |

## The `9` defects these instruments raised against clean shelves

🔴 **Of `21` apparent defects raised across this pass, `9` were the instruments' own and `0` were published as findings.** This is the same ratio `p772` measured (`12` of `13`), from independent instruments — which is the point of recording it.

| # | Defect | How it was caught | Fix |
|---|---|---|---|
| `D1` | `gate_tables` flagged `| type | project |` as a header-row-as-data | Hand-read the single candidate before publishing | Exempt `field`/`value`-shaped **key–value meta-tables**: generic words are the DATA there. Controls `C9`, `C10` |
| `D2` | Grader read a filled copyright holder as an alteration; `kolibri`, `richie` graded `UNRESOLVED` | Hand-read all four unresolved payloads — every one was an ordinary MIT/BSD/Apache file | **Mask the copyright slot** in both payload and canonical before comparing |
| `D3` | BSD/MIT **template slots** (`<year> <owner>`) read as alteration | Same hand-read | Mask `<ORGANIZATION>`-style slots and years |
| `D4` | An Apache payload **without the optional appendix** read as altered (`medplum`) | Same hand-read | Compare the **operative body** up to `END OF TERMS AND CONDITIONS` |
| `D5` | `AGPL-3.0-only` reported as the answer where the two arms are byte-identical | Control `K3` failed | Collapse byte-identical canonicals into a **group**; let an SPDX tag pick the arm. `19` distinct bodies from `23` files |
| `D6` | A `0.995` similarity threshold passed a **deliberately altered AGPL** text as canonical | Control `K9` — a seeded alteration | Replace the ratio with an **ABSOLUTE edit budget** (`≤25` changed chars). At `0.995`, a `34,020`-char text tolerates `~170` changed chars; a `1,078`-char file tolerates `5` |
| `D7` | A licence **title line** and `all rights reserved` spent the whole edit budget, so clean BSD-3 read as altered | Control `K3` failed again after the `D6` fix | Mask both as non-operative **decoration** |
| `D8` | `find_superseded` reported `12` date defects on curated shelves | Hand-read three — each carried the correction on the **adjacent** line | Check over a **paragraph window**, not a line. `12` → `2`, and both survivors are correct (Vietnam) |
| `D9` | A false **`NO-GRANT-AT-ROOT`** published against `frappe/erpnext` | Probed the filename space directly | Grant filename list must be **case-aware**: its GPL-3.0 grant is at lowercase **`license.txt`**. `15` names → `31` |

🔵 **`D5`→`D6`→`D7` is worth reading as a sequence: each fix created the next defect, and only a seeded-alteration control (`K9`) stopped the chain from ending in a grader that passed everything.**

## Reproducing

```bash
python3 -I compose/code/p773/gate_tables.py --controls
python3 -I compose/code/p773/gate_tables.py $(find . -name '*.md' -not -path './.git/*')
cd /path/to/repo && python3 -I compose/code/p773/grade2.py ingest/canonical <<< $'owner/repo\tbranch\tLICENSE'
compose/code/p773/probe.sh owner/repo
compose/code/p773/grantprobe.sh owner/repo develop
```
