# `p772-sweep` — the dedicated address-and-grant sweep `ACTION p771-B`/`p771-I` asked for

Written from scratch at `p772`, after `make hooks` was **denied for a third consecutive
session** (`[Code from External]`). Nothing here is copied from this repository's own gate
suite; `ACTION p771-A` forbids that and it was not done.

## What each instrument is

| File | What it does |
|---|---|
| `extract_addresses.py` | Harvests every **displayed** GitHub address (markdown links only) from the live shelves, and asserts `link_text == url_path` for `owner/repo`-shaped link text |
| `probe_one.sh` | Probes ONE address on the ref channel (`git ls-remote --symref`). Three-valued: `RESOLVES` / `ABSENT-OR-PRIVATE` / `EXISTS-BUT-EMPTY` |
| `claims.py` | Extracts `(address, CLAIMED licence family)` pairs from table rows — the population where a grant cell can be wrong |
| `fetch_one.sh` | Byte-reads a grant payload on `raw.githubusercontent.com`, probing 10 filenames at the **measured** default branch |
| `grade.py` | `ACTION p771-C` body-diff against SPDX canonicals + `ACTION p771-D` family-aware ownership |
| `refine.py` | Splits `body:ALTERED` into appended / template-slot / pointer / genuinely-altered |
| `gate_dates.py` | `gate-dates`, bare-date form — **kept as the proof that the form is unimplementable** (see below) |
| `gate_claims.py` | `gate-dates`, subject-bound form — the form that works |

## How to run it

```sh
git ls-files '*.md' | grep -vE '^(archive|scratchpad|evidence|compose/code)/' > /tmp/shelves.txt
python3 -I compose/code/p772-sweep/gate_claims.py /tmp/shelves.txt     # the working date gate
python3 -I compose/code/p772-sweep/extract_addresses.py /tmp/shelves.txt /tmp/links.json /tmp/slugs.txt
xargs -a /tmp/slugs.txt -I{} -P 12 compose/code/p772-sweep/probe_one.sh {} > /tmp/sweep.tsv
```

Every script runs with `python3 -I` from the repository root. They take their input paths as
arguments and import nothing from this repository, so `p355-cwd-portability`'s class of
defect — a suite that only passes from its own directory — cannot occur here.

## 🔴 Nineteen defects in these instruments, each caught by a control before a verdict was published

This is the honest record of the pass. **Every single apparent finding against this base
dissolved under verification except one.**

| # | Defect | How it was caught |
|---|---|---|
| `D1` | A file path as link text (`db/…schema.go`) read as an `owner/repo` claim | Reading the 4 flagged sites before writing a verdict |
| `D2` | A **trailing dot is part of a real repository name** (`…-Toolkit.`); the dotless form is ABSENT | Probing both forms |
| `D3` | `comm` on files sorted under different collations — reported `5,671` probes against a population of `5,646` | The count exceeded the population |
| `D4` | 12-way parallel appends tore one line (`OLVES`) | A slug not present in the population |
| `D5` | `topics/<tag>` is a GitHub **topic page**, not a repository — 28 of them read as absent repositories | Recognising the URL form |
| `D6` | 🔴 treated as a refutation verb; and "same line" is not "about this date" in a 2,000-character paragraph | `817` refuted date records was implausible |
| `D7` | A future **legal** date (an Act applying from `2027-12-02`) counted as a future **measurement** date | `133` future dates was implausible |
| `D8` | Subject pattern `statutory guidance` is not specific — England has several | Reading the 4 sites: they were the **allergy** guidance, published `2026-07-06` |
| `D9` | `${slug//\//~}` — the `~` replacement was **tilde-expanded to `/root`**, so every `200` response was written to a non-existent directory and silently discarded | `0` payloads fetched from `1,625` addresses |
| `D10` | A row's licence cell attached to **every** link on the row, not to the row's subject — invented **9** false `MISDECLARED` verdicts | Reading each flagged row: `links-on-line=2` or `3` |
| `D11` | LGPL-3.0 **ships the GPL-3.0 text** by reference, so a body-diff cannot separate the pair | `odoo/odoo` flagged while its payload says LGPLv3 in line 3 |
| `D12` | A filled BSD `<ORGANIZATION>` slot is template **completion**, not alteration | A `delta=1` cluster across `vivo-project`, `dhis2`, `scieloorg` |
| `D13` | The family vocabulary omitted `GPL-2.0`, `CC-BY-*`, `EPL`, `LGPL-2.1` — any row whose true licence was outside it got a wrong claimed family | `oat-sa/*` flagged Apache while the shelf correctly said **GPL-2.0** |
| `D14` | A `MISDECLARED` verdict is only as good as the canonical set held — `CC-BY-NC-4.0` was absent, so it graded as the nearest held text | The payload's first line read `Attribution-NonCommercial` |
| `D15` | Distinct branch **names** counted as **addresses** — reported `419` non-`main`/`master` defaults against a true `330` | Re-deriving the count from the sweep rather than from a `uniq -c` listing's row count |
| `D16` | Generalised *"not one Moodle MCP server serves code"* from the dead subset, without measuring the live one — **`67` of the `78` resolve** | Querying the sweep for the whole category instead of the flagged rows |
| `D17` | Line numbers from the **pre-insertion** scan applied to the **post-insertion** files, so the absence-marker check read the wrong lines — scored `47`/`32` where the truth is `34`/`45` | Re-extracting addresses from the files as they now stand |
| `D18` | The template-row check flagged legitimate Markdown **header** rows, then **transposed-table** field names, then the **separator** rows themselves: `268` → `50` → `6,164` → `0` | Reading the flagged lines at each iteration |
| `D19` | The first draft of the row documenting the `SikhshaBox` display defect **reproduced that defect**, by linking the short display text | Re-running the `link_text == url_path` contract over this pass's own output |

🔴 **`D6`/`D7`/`D10`/`D13` each produced a number that, if published, would have been a
fabricated indictment of this base: `2,994` date violations, `11` misdeclared grants, `144`
altered licence bodies.** 🟢 The verified figures are `128` subject-bound date assertions,
**`1`** misdeclared grant and **`39`** payloads that are not the single canonical family text.
