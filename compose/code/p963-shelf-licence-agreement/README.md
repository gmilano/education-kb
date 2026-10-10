---
industry: education
region: Global
updated: 2026-10-10
---

# `p963-shelf-licence-agreement/` — `Gap 356` discharged, and it fails on first run

**Pass 92, 2026-10-10.** Offline except for the census TSV it reads. Single file on purpose (`Gap 300`).

```sh
./agree.sh <kb-root> [census.tsv]
```

## What this exists for

🔴 **`Gap 356` was declared in pass 86 and carried untouched through four passes**, each time with
the same note: *"it would have caught `P953` and `P957` — both are register/shelf/code disagreements
that a grep could have found."* 🔴 **Pass 92 is the pass where the absence stopped being cheap.**

The gap's cost this time was not an internal inconsistency. It was **a client recommendation built
on a licence this KB had already corrected**:

| file | what it says about `portabilis/i-educar` |
|---|---|
| `verticals/solutions.md` | 🔴 *"for a **Brazilian public-sector SIS** → `i-educar` (**LGPL-3.0**) — real municipal deployments; **link, don't absorb**"* |
| `verticals/solutions.md` | 🔴 *"none is permissive, but a substantial **linkable** one exists, and it is LATAM-origin"* |
| `agents/trending.md` | 🟢 `\| portabilis/i-educar \| LGPL \| **GPL-2.0** \| LATAM — Brazilian municipal school system \|` |

🔴 **Same slug, same repository, same commit, two families — and the advice that reached a reader was
built on the wrong one. You cannot "link, don't absorb" a GPL-2.0 codebase into a closed
deliverable.** 🟢 A grep could have found it. This is that grep.

## What it checks

| section | what it compares | fails the gate? |
|---|---|---|
| **(1)** | the **current** shelf files against **each other** | 🟢 yes |
| **(2)** | the **current** shelf files against the **census TSV** | 🟢 yes |
| **(3)** | the current shelf against **`*/trending.md`** | 🔴 **never** — informational only |

🔵 **Section (3) is why this check is buildable at all.** `agents/trending.md` and `repos/trending.md`
are **append-only history**: a superseded verdict living there is correct by construction. A naive
sweep over every `.md` drowns in its own archive and gets switched off. **Separating the current
shelf from its history is the design, not a shortcut.**

## It found a defect in itself on its first run — recorded, not quietly fixed

🔴 **The first draft harvested the first bolded licence family on a row. `agents/top.md` carries a
"what is widely claimed | what the payload says" refutation table:**

```
| `frappe/lms` | a comparison lists it as **MIT** | **AGPL-3.0**, `license.txt`, 33 893 B |
```

🔴 **A first-match harvest reads `MIT` — the *refuted* claim — and reports the shelf as disagreeing
with itself.** 🔵 **The refutation table is the shelf being careful, and the naive gate punished
exactly the rows that had done the work.** A gate with that failure mode gets disabled within a pass.

🟢 **The fix is the shelf's own convention, and it is mechanical: a verdict cell carries the
payload's byte count** (`**AGPL-3.0** · 33 893 B`), **and a cell quoting someone else's claim never
does.** So the harvest is **cell-aware**: split the row on `|`, keep only families in a cell that
also carries a byte figure, and take the last such. 🟢 `frappe/lms` cleared immediately and the
harvest fell from 122 claims to **113 real verdicts** over 87 slugs.

🆕 **`P967`: a consistency gate must distinguish a shelf's VERDICT from a claim the shelf is
refuting, or it penalises precision.**

## Split grants are exempted **explicitly**, in a committed file

🟡 `microsoft/autogen` is a verified multi-file split — `LICENSE` = **CC-BY-4.0** (18 650 B),
`LICENSE-CODE` = **MIT** (1 141 B), both re-read at `027ecf0` this pass. `agents/top.md` cites
**MIT**, which is correct for anyone shipping the code; a first-match census says `CC-BY-4.0`.
🟢 **The shelf is being more precise than the census, so it must not fail.** That exemption lives in
`splits.tsv` with its evidence, prints as `split-exempt`, and is auditable. 🔴 **Never a silent pass.**

## First-run result — the 4 defects it was built to find

```
claims harvested from CURRENT shelf files: 113   distinct slugs: 87
(1) current files disagreeing with each other ... none
(2) current shelf vs census
      split-exempt  microsoft/autogen         shelf=MIT       census=CC-BY-4.0
      MISMATCH      oat-sa/tao-core           shelf=LGPL-3.0  census=GPL-2.0   (repos/foundations.md)
      MISMATCH      oat-sa/tao-core           shelf=LGPL-3.0  census=GPL-2.0   (verticals/solutions.md)
      MISMATCH      portabilis/i-educar       shelf=LGPL-3.0  census=GPL-2.0   (compose/patterns.md)
      MISMATCH      portabilis/i-educar       shelf=LGPL-3.0  census=GPL-2.0   (verticals/solutions.md)
FAILURES: 4
```

🟢 **All four are corrected in this pass's commit, so the gate runs clean afterwards.** 🔵 **The point
of recording the failing run is that the gate's value is the four rows it caught, not the zero it
reports once they are fixed.**

## 🟢 And it caught a defect in **this pass's own new content**, which is the better proof

🔵 **A gate that only finds legacy defects is a one-off audit. This one failed on prose written minutes
earlier.** The new `P92-A` pattern in `compose/patterns.md` had a stack row reading:

```
| tutor turn | [`HKUDS/DeepTutor`](…) **or** [`fborrasumh/tutoria`](…) | **Apache-2.0** · `6cf793b` / **MIT** · 1 120 B · `65b2903` | … |
```

🔴 **One cell, two repos, two licences.** The harvest took the first slug and the byte-bearing family and
reported `HKUDS/DeepTutor` as **MIT** — it is **Apache-2.0**. 🔵 **The gate was right to fail: a cell that
pairs two repos with two grants is ambiguous to any checker and to a reader costing the stack.** 🟢 Fixed by
splitting it into *option A* / *option B* rows, which also reads better. **Final state: 0 failures.**

🔵 **This is the argument for running it inside the pass that writes, not as a later audit.** The four
legacy mismatches had survived a pass; this one survived about ten minutes.

## Stated limits

- 🔴 It compares **families**, not **versions-within-a-row-of-prose**: a row whose byte figure and
  family agree but whose *narrative* ("linkable", "permissive") contradicts the family is invisible
  here. **That is how `i-educar` read plausibly for two passes**, and it is the next gap.
- 🔴 It needs the family in **bold** and a **byte figure in the same cell**. A row written without
  bytes is skipped silently — the harvest count is printed so that skipping is visible.
- 🔴 It cannot see a licence this base has never measured; it is a *consistency* gate, not an oracle.
