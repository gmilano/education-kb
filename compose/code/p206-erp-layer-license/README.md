# P206 — the ERP/administrative layer, measured by payload (pase 71 del 2026-10-03)

## What this asks

Pass 70 opened the SIS / school-platform category and found it dominated by strong copyleft,
with a single permissive candidate measurable only in a MIRROR. That verdict was drawn on the
SIS slice alone. The **ERP slice** — the system a school actually runs fees, admissions and HR
on — had never been enumerated, because the `open source platform education ERP CRM MIT Apache`
channel has collapsed onto OpenEduCat SEO for nine consecutive passes.

## Channel

`api.github.com` → **403** and `github.com` → **403** by curl in this environment, all pass.
Every byte count, `sha256` and holder below is read from **`raw.githubusercontent.com`**, which
is the payload channel **P172** prefers. No figure here comes from the API.

## The two defects this instrument shipped with, and what they cost

Both were caught before publication, by the controls this base already requires.

### D1 — the payload channel is CASE-SENSITIVE

The first build probed 7 names, all uppercase plus `LICENCE`. It returned **`NO-CESSION`** for
`frappe/education` and `frappe/erpnext`. Both carry **`license.txt` in lowercase**, HTTP 200.
Two false absences, and the class of error is the one pass 69 already paid for: *a single
filename probe fabricates tombstones.* Fixed by probing a **27-name case matrix**
(`names.case-matrix.txt`).

**Consequence beyond this sweep, and it is the finding of the pass:** every `NO-CESSION` /
`UNLICENSED` verdict this base has ever published was produced by an uppercase-only probe, so
each is **CONDITIONED ON CASE** — not necessarily wrong, but not closed either.

**Control run:** pass 70's `NO-CESSION` on `hesham0-0nasser/tutor-lms-mcp` was re-measured at
all 27 names. It is **still `NO-CESSION`**. The correction did not overturn that verdict; it
strengthened it.

### D2 — the family must be read from the TITLE, never from the body

The first build classified with an AGPL-first grep over the whole text. **GPL-3.0 section 13 is
headed *"Use with the GNU Affero General Public License"***, so every GPL-3.0 text matched AGPL
first. The build read `GibbonEdu/core` as AGPL-3.0 and was one commit away from publishing a
"correction" to pass 70 that was itself wrong — pass 70 had it right.

This is **P171** restated: classify on the **DECLARATION**, never on a body grep. Fixed by
consulting only the first 40 lines. `test_family.py` pins both directions, including the control
that a real AGPL-3.0 text still classifies AGPL-3.0 (so the fix did not overshoot).

## Files

| File | What it is |
|---|---|
| `sweep_erp.sh` | the instrument, carrying D1 and D2 fixes |
| `names.case-matrix.txt` | the 27 license filenames, generated across case variants |
| `targets.tsv`, `targets-round2.tsv`, `targets-agents.tsv`, `targets-all.tsv` | the slugs asked, declared before measuring |
| `result-D2corrected.2026-10-03.tsv` | **the publishable result** — the ERP layer after both fixes |
| `result-agents.2026-10-03.tsv` | the agent candidates of the pass |
| `result-casefix.2026-10-03.tsv` | the D1 re-measure, incl. the pass-70 tombstone retest |
| `result.2026-10-03.tsv`, `result-round2.2026-10-03.tsv` | **SUPERSEDED** — kept as the record of D1/D2, not as data |
| `test_family.py` | 5 regression assertions on D1 and D2 |

⚠️ **The two `SUPERSEDED` files are kept deliberately.** They are the evidence of what the
defects produced, which is why the corrections are legible. **They are not data.**

## Reproduce

```bash
./sweep_erp.sh frappe/erpnext      # GPL-3.0, license.txt, 35.148 B
./sweep_erp.sh GibbonEdu/core      # GPL-3.0  <- D2 regression guard
./sweep_erp.sh ClassroomIO/ClassroomIO   # AGPL-3.0 <- D2 control
python3 test_family.py             # 5/5
```
