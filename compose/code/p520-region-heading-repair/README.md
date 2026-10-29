# `p520-region-heading-repair` — making the `P383` contract REPAIR itself

🔴 **What this closes.** `Gap 520-E` registered that the `P383` contract — *exactly one* bare
`## Opportunities by region`, the current pass's — had regressed **three times** (`p508`,
`p511`/`p514`, `p519`). Its diagnosis was structural rather than disciplinary: *"a fixed-position
contract inside a prepend-only file is structurally fragile"*, because every pass that prepends a
section must remember to demote the previous bare heading, and a detector that only **reports** the
breach leaves the work undone.

🟢 **Its named closure:** *"make the gate repair it rather than only detect it."* This does that.

## The rule

- The file is **prepend-only**, so the **first** bare canonical heading is the newest pass's. It stays.
- Every **later** bare one is demoted to ``## Opportunities by region — `pNNN` `` where `pNNN` is
  found by scanning **backwards** for the nearest ``## 🆕 `pNNN` `` section marker that owns it.
- 🔴 **Nothing is renumbered and nothing is guessed.** A bare heading with no pass marker above it
  is reported `UNREPAIRABLE` and left exactly as it was.
- 🟢 **Idempotent** — a repaired file is a fixed point, asserted after every write, so this can run
  on every pass.

## Relationship to the detector

🔵 `compose/code/p383-region-heading-gate/` still **judges** the contract and is unchanged: it
checks the closed five-value vocabulary, missing regions, multiple blocks and the LATAM-only shape.
🟢 This tool only fixes the one defect a prepend reliably creates. Run the repair **first**, then
the gate.

🔴 **The gate still catches what the repair cannot.** When `p520` prepended its own section, the
repair demoted `p519`'s heading correctly — and the gate then found a **different** real defect in
`p520`'s own prose: a `### 🔴 Declared gaps` subsection sitting inside the region block, outside
the closed vocabulary. The repair has no opinion about that; the gate does. **Both are needed.**

## Usage

```sh
python3 -I compose/code/p520-region-heading-repair/repair_headings.py intel/market.md           # report, exit 1 if repairs needed
python3 -I compose/code/p520-region-heading-repair/repair_headings.py intel/market.md --write    # apply
python3 -I compose/code/p520-region-heading-repair/test_repair_headings.py                       # 15 controls
```

🟢 **15/15 controls green** from the repository root and from this folder, including:

- a clean file proposes **zero** repairs (no churn on a correct file);
- a doubly-regressed file demotes **two** headings to their **owning** passes (`p519`, `p518`), not
  to the newest one;
- after applying, exactly **one** bare heading remains, and a re-plan is **empty** (idempotence);
- 🔴 a **refusal control** — an orphan heading with no pass marker above it is `UNREPAIRABLE`, and
  no pass id is invented for it;
- `owning_pass` reads the **nearest** marker above a line, not the first in the file.

## Demonstrated on the live file in the pass that built it

```
$ python3 -I repair_headings.py intel/market.md --write
file              bare_kept_line  repairs  unrepairable
intel/market.md   134             1        0
  REPAIR  line 367  -> p519
🟢 wrote 1 repair(s); re-plan is empty, so the file is a fixed point
```

🔵 `p520`'s own prepend created the **fourth** instance of the regression, and the tool repaired it
without a hand edit. That is the difference between a gap closed with content and a gap closed with
a promise.
