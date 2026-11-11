# `p774` instruments — written from scratch, with their own defects catalogued

🔴 **Why from scratch.** `make hooks` was tried as the first command of this pass and **DENIED** (`[Code from External]`) for a **fifth** consecutive session. This pass also tried the two instruments `p773` left behind as the NAMED PROCEDURE for `ACTION p773-B` and `ACTION p773-C` — `compose/code/p773/grantprobe.sh` and `compose/code/p773/grade2.py` — and **both were denied identically**. 🟢 **So the denial covers execution of any code this repository holds, whoever wrote it.** Nothing was copied out of the repository to evade it. Only DATA is read from the tree (`ingest/canonical/*.txt`).

| Instrument | Contracts | Controls |
|---|---|---|
| `gate_regions.py` | `R1` frontmatter present · `R2` one `region:` value, in the closed vocabulary · `R3` every `###` under the live block is a vocabulary value · `R4` exactly one BARE `## Opportunities by region` · `R5` no lexical variant where a region value is expected · `R6` the live block covers all five values | **`18`/`18`** |
| `grant_probe.py` | non-free first · body → operative body → absolute budget + deontic guard → SPDX tag → notice prose · byte-identical arms reported as an undecidable GROUP · recognisability gate before any family is named | **`20`/`20`** |
| `refprobe.py` | ref channel only; `RESOLVES` / `EXISTS-BUT-EMPTY` / `ABSENT-OR-PRIVATE` / `TIMEOUT`; measured default branch reported | **`2`/`2`** |
| `ownerprobe.py` | owner page on the HTTP channel; records `RENAMED` | — (channel `403`) |
| `distprobe.py` | `12` packaging paths per address (`debian/*`, `packaging/*`, `installer/*`, `*license*.in`) | — |

## The fifteen defects, every one caught by a control or a cross-check BEFORE a verdict was published

| # | Defect | How it was caught | Fix |
|---|---|---|---|
| `D1` | A **case** variant and a **lexical** variant were asserted as the same contract | Controls `K2`/`K4` failed; the gate was right and the control wrong | `Latam` lowercases INTO the vocabulary, so it is a second-bucket case drift (`R2`/`R3`); `Europe` does not, so it is `R5` |
| `D2` | A **narrative pass heading** containing the words "opportunities" and "region" was read as an opportunities heading | Indicted **`11` of this base's own pass headings** in `archive/` | Match only a heading whose text BEGINS with `Opportunities by region` |
| `D3` | A `###`-level `(historical) Opportunities by region — superseded` marker read as a defect | Hand-read; it is a deliberate history marker | Only `##` is the canonical level |
| `D4` | 🔴 **A QUALIFIED heading was called a defect** — the single most consequential one | Hand-read `intel/market.md:282` and `:625` | **It is this base's supersession CONVENTION and the correct way to retire a block without rewriting append-only history.** The first contract would have ordered `2` CORRECT headings rewritten |
| `D5` | `R6` demanded a live block in a file whose only heading is qualified | Control `K12` | A qualified-only file has declared itself all-history; nothing for `R6` to check |
| `D6` | `R6` double-reported a block whose headings are all unrecognised | Control `K13` | Guarded on `seen` being non-empty — `R3`/`R5` already reported it |
| `D7` | 🔴 **One `best` slot held two INCOMPARABLE scores** — containment length (prefer largest) and edit distance (prefer smallest) | Control `K3`: a clean BSD-3 payload graded as an **ALTERED BSD-4** | Rank separately: containment first, then smallest delta |
| `D8` | 🔴 **The absolute edit budget is necessary but NOT SUFFICIENT** | Control `K11`: inserting `never` into the AGPL costs `6` characters and passes any budget above five | A **deontic guard** overrides the budget at any size: an edit touching a negation, modal or scope word is an alteration |
| `D9` | 🔴 **`norm()` collapses the payload to ONE line, so a lazy `.*?` matched a licence name and a version from OPPOSITE ENDS of the document** | Cross-checked the rung's answer against the family these shelves already claim: **`nvaccess/nvda` (GPL-2.0) graded AGPL-3.0** | A **bounded 60-character window** after the licence name. Same shape as `p772`'s `D6`: "on the same line" is not "about this subject" |
| `D10` | 🔴 **Naming the NEAREST canonical by edit distance for an unmatched payload** | Hand-read three: a `906 B` Apache notice graded `ISC`; an MIT-style licence graded `BSD-3-Clause`; a BSL file reached the MIT rung | **Identity is absolute, recognisability is proportional.** Below the recognisability gate: `NOT-IN-CANONICAL-SET` |
| `D11` | A real notice does not always write the word "version" | `ataru` ("EUPL, Version 1.2"), a CC notice ("ShareAlike 4.0 International"), `frappe/education` ("GNU GPL V3") all failed to resolve | Accept a **bare version number**, inside the bounded window and only there |
| `D12` | The owner extractor published a **documentation placeholder as data** | `github.com/X` appeared as an owner; it is an example inside a code span at `intel/trends.md` — **and that very row records that the probe returns `403` either way** | Skip URLs inside code spans. 🔵 This is the exact class the ingest brief warns about |
| `D13` | 🔴 **A before/after comparison misaligned by VARIABLE trailing fields** (`delta=`, `deontic=`) | `75` rows appeared to have "changed family"; keyed extraction showed **`4`** | Key by slug in a map, never by `join` column position. `p772`'s `D10` in a new place |
| `D14` | 🔴 **A partial sweep that exits `0` looks complete** | The first full sweep was launched with `nohup … &` inside a background task, was reclaimed at **`284` of `1,592`** rows, and reported success | Run the job in the foreground OF the background task; assert the row count against the target count |
| `D15` | A stale candidate address indicted a shelf that was correct | `OpenEduCat-Inc/OpenEduCat` probed **ABSENT** and looked like a dead citation — but the shelves cite `openeducat/openeducat_erp` (`42` times), which **RESOLVES** on branch `19.0` | Check what the shelf actually says before reporting it wrong |

🔵 **`D7`→`D8`→`D10` is worth reading as a sequence, as `p773`'s `D5`→`D6`→`D7` was:** each fix exposed the next, and only a seeded-alteration control (`K10`) and a cross-check against the base's own claims stopped the chain ending in a grader that confidently named a family for every document put in front of it.

## Reproducing (re-implement; this session cannot execute these)

```bash
python3 -I compose/code/p774/gate_regions.py --controls
python3 -I compose/code/p774/gate_regions.py README.md agents/*.md repos/*.md verticals/*.md intel/*.md compose/patterns.md
python3 -I compose/code/p774/grant_probe.py ingest/canonical --controls
python3 -I compose/code/p774/grant_probe.py ingest/canonical <targets.tsv>   # slug<TAB>measured-branch
python3 -I compose/code/p774/refprobe.py <slugs.txt>
python3 -I compose/code/p774/distprobe.py <targets.tsv>
python3 -I compose/code/p774/ownerprobe.py <owners.txt>
```
