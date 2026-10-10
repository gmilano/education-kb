---
industry: education
region: Global
updated: 2026-10-10
---

# `p996-promotion-ledger/` — the two audits that discharged `Gap 381` with no network and no code execution

**Pass 98, 2026-10-10.** 🔴 **Repository code was refused for a SIXTH consecutive pass**
(`Gap 383`, `[Code from External]`). 🟢 **These two audits were written and run anyway, because their
corpus is this repository's own committed text** — which is `P1004`, adopted this pass: *when the
instrument is refused, prefer the question whose corpus is the repository.*

🔴 **Neither script is a licence classifier.** `P237` stands: no replacement for
`grant-ladder-v4/lib/license_family.sh` was written. These read Markdown and emit counts.

## `reconcile_code_shelf.py` — `Gap 381`, discharged

**The question:** which slugs does `compose/code/` carry that no shelf page offers to a client?

```
slugs in compose/code: 1056   on shelf: 159   in code but NOT on shelf: 956
in code but not on shelf, carried by a NON-sweep (purpose-built) directory: 4
   juneyaooo/lineage-skill        ['aiact-50-2-marking', 'p725-readme-payload-sweep']
   o/r.git                        ['p791-registry-id-provenance', 'registry-recency-channel']
   safeexambrowser/seb-server     ['p725-readme-payload-sweep', 'proctoring-reach-audit',
                                   'seb-proctoring-validator', 'sebserver-mcp-gate']
   toshieji/moodle-grading-mcp    ['grading-draft-gate', 'p725-readme-payload-sweep']
```

🟢 **956 is not the defect.** The sweep-results directories record candidates by design, exactly as
`Gap 384`'s 1 119 does. 🔵 **The filter that matters is "a directory built FOR this repository", and
it narrows 956 → 4 → 3 real.** `o/r.git` is a parse artefact from a `git@github.com:o/r.git` usage
example — 🟢 **stated rather than silently dropped, because it is this script's regex limit.**

🔴 **The finding is `safeexambrowser/seb-server`: THREE purpose-built, tested directories since
pass 43, and no shelf page.** And `intel/trends.md` mentioned proctoring exactly once — as the place
the EU AI Act's emotion-recognition prohibition bites. 🔵 **A published exposure with no offer against
it is a missing SALE, not a missing row.**

All three were payload-verified this pass and are now shelved:

| slug | grant | bytes | ref · SHA-14 | tags |
|---|---|---|---|---|
| `SafeExamBrowser/seb-server` | 🟡 **MPL-2.0** | **16 725** | `master` · `7f45689f797337` | 🟢 **194**, `v3.0-latest` |
| `toshieji/moodle-grading-mcp` | 🟢 **MIT** | **1 120** | `main` · `5695878b4735ed` | 🔴 0 |
| `juneyaooo/lineage-skill` | 🟢 **Apache-2.0** | **11 358** | `main` · `7e2cbc5dc31713` | 🔴 0 |

## `build_ledger.py` — `Gap 384`, half discharged and inverted

**The question:** for each shelf row, what is the oldest dated section of the append-only history that
mentions it? That is a **bound** on the pass that promoted it — the column `Gap 384` says no page
carries.

```
shelf slugs: 159
history slugs: 1246
shelf rows with NO history mention: 6
```

🟢 **The orphan count reproduces pass 97's figure of 6 under an independently written regex** (159 /
1 246 here against 146 / 1 259 there — the denominators move with regex breadth, the orphan count
does not). 🟢 **And all six were re-read this pass at their published refs: 6 of 6 identical, byte for
byte.**

🔵 **`P996`: a shelf row absent from the history is NOT unwitnessed** — this KB publishes
`bytes · ref · sha7` inline, so the shelf row *is* an evidence record. 🔴 **`Gap 384`'s real remainder
is the missing *promotion pass* column**, which `promotion-ledger-pass98.tsv` now supplies as a bound
for 153 of 159 rows.

### Note on history ordering, because getting it backwards inverts the answer

The trending files are **append-only with the NEWEST section at the top**. So a slug's **oldest**
mention is its **highest line number**, and `build_ledger.py` takes `max(lineno)` per slug before
mapping it to the enclosing dated header. 🔴 **Taking the first match returns the most recent mention
and makes every row look newly promoted.**

## Files

| file | what it is |
|---|---|
| `reconcile_code_shelf.py` | `Gap 381`'s audit. Reads Markdown; no network. |
| `build_ledger.py` | `Gap 384`'s ledger. Reads Markdown; no network. |
| `promotion-ledger-pass98.tsv` | 159 shelf rows × (shelf pages, oldest history section, evidence location). |
| `payloads.2026-10-10.pass98.tsv` | The hand-run oracle map (`P970`) for this pass's candidate slugs: slug, ref/sha7, filename, bytes, first non-blank line. |

🔴 **`payloads.2026-10-10.pass98.tsv` contains one `NO-RESOLVE` row** —
`Datalab-AUTH/esco-skill-extractor`, named by a search summary as a distinct project, 🟢 **kept as
this pass's negative control.**
