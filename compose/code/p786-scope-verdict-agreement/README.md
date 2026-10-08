---
industry: education
region: Global
updated: 2026-10-08
---

# `p786-scope-verdict-agreement` — cross-run the two licence instruments, and **refuse to treat their agreement as a pass**

**Declared and closed pass 62, 2026-10-08.** `15/15` green, offline, run from this directory.

## Why it exists

🟢 **`p637` already cross-runs this KB's three *family classifiers* over one payload**, and its
lesson is written down in its own README: **it does not vote**, because the majority said `LGPL`
and the majority was wrong. 🔴 **Nothing carried that lesson up to the *verdict* layer**, where
two instruments answer a different question:

| Instrument | Channel | Emits |
|---|---|---|
| `p784-licence-scope-map` | 🔴 **16 ROOTED filenames** | `SINGLE` · `PARTITIONED` · `UNGRANTED` |
| `p441-tree-licence-enumeration` | 🟢 complete `git ls-tree -r` | `OWN-GRANT-AT-ROOT` · `BUNDLED-GRANT-ONLY` · `ABSENCE-ENUMERATED` |

## The finding that shaped the design — `P786`

🔴 **Agreement is not sufficient, and this is measured rather than argued.**

🟢 [`luisgf/openbadgeslib`](https://github.com/luisgf/openbadgeslib) `@e7736b6` is
**LGPL-3.0 library + BSD-2-Clause CLI**. 🔴 **The split is declared in
`wiki/Authors-License-and-FAQ.md` and nowhere else:**

| Surface | Says |
|---|---|
| `LICENSE.txt`, 7 650 B | 🔴 LGPL-3.0, alone |
| `pyproject.toml` | 🔴 `license = { text = "LGPLv3" }`, one classifier |
| PyPI metadata (v4.5.0, 2026-09-12) | 🔴 LGPLv3 |
| 🟢 `.py` headers | 🔴 **0 of 40 name BSD** |
| 🟢 `wiki/Authors-License-and-FAQ.md` | 🟢 **"the **library** → LGPLv3 … the **command-line wrapper tools** → **BSD 2-Clause**"** |

🔴 **`p784` returned `SINGLE — LGPL-3.0`. `p441` returned `OWN-GRANT-AT-ROOT / LGPL?`. They agreed,
and both were wrong about the repo.** 🟢 **No file-enumerating probe can find this partition, however
many filenames or however complete the tree — it is not in a file either one reads.**

🟢 **So every unanimous single-family verdict is emitted as `NEEDS-PROSE-READ`, not as a pass.**
🔵 **This instrument narrows *who* a human must read. It never replaces them**, and the cost of that
read is about two minutes per candidate — cheaper than either gate it wraps.

🔴 **And the cost of getting it wrong runs in the direction nobody guards against:** a team that
reads `LGPL-3.0` and walks away **forfeits five BSD-2-Clause CLI entry points it was entitled to
ship**; a team that reads the wiki and concludes "basically BSD" **links LGPL-3.0 into a closed
product**.

## The classes, and why direction is preserved rather than tallied

- **`DISAGREE-ABSENCE`** — `p784` sustains an absence the tree contradicts. 🔴 **Refuses a usable
  repo.** → `Gap 287`
- **`DISAGREE-PRESENCE`** — `p441` reports families `p784` never saw. 🔴 **Admits an unlicensed
  one**, which is the worse direction, so it is reported even when `p784` also found a grant. →
  `Gap 288`
- **`NEEDS-PROSE-READ`** — unanimous on one family. 🟡 **The exact shape in which a prose-only
  partition hides** (`P786`).
- **`PARTITIONED-DECLARED`** — the split is visible in files; read scope per path.
- **`ABSENCE-ENUMERATED`** — no grant at 16 root names **and** no licence path in the complete
  tree. 🟢 The only verdict a filename list could not reach on its own.
- **`UNREACHABLE`** — one or both channels did not resolve the slug.

🟢 **A coarse family that prefixes a fine one is not a disagreement** (`p441`'s `BSD` against
`p784`'s `BSD-3-Clause`) — that is `p637`'s `CONTRATO` class, and conflating it with a real
divergence turns the gate into noise. 🔴 **`GPL-3.0` is deliberately *not* a prefix of `LGPL-3.0`**,
which is the trap `P753`/`P773` names: every GNU text names its relatives.

## Measured, 2026-10-08, over 13 slugs

🟢 **Frame declared by name before either instrument ran** (`P744`): `slugs.input.2026-10-08.txt`.
🟢 **13 of 13 reachable.** Full rows in `result.2026-10-08.tsv`.

| Class | n |
|---|---|
| 🔴 `DISAGREE-ABSENCE` | **1** — `1EdTech/openbadges-specification` |
| 🟡 `NEEDS-PROSE-READ` | **12** — including `luisgf/openbadgeslib`, where unanimity was wrong |
| `DISAGREE-PRESENCE` · `ABSENCE-ENUMERATED` · `PARTITIONED-DECLARED` · `UNREACHABLE` | **0** each |

🔴 **2 of 13 rows are wrong and only ONE is a disagreement** — 🟢 **which is the result that
justifies the design: a disagreement counter would have caught half of it.**

🔴 **The `DISAGREE-ABSENCE` row, in full, because it is the ground truth for `Gap 287`:**
`p784` → `UNGRANTED` (0 of 16 root names). `p441` → `BUNDLED-GRANT-ONLY`, families
**`CC-BY;CC0-1.0`** drawn from `extensions/licenseExtension/…` — 🔴 **documentation of an Open Badges
*metadata field*, not a grant** — while putting the repo's two **real** grants in `rejected_paths`:
`ob_v3p0/license.md` (🟢 **`200`, 12 324 B**, *IMS Global Specification Document License*) and
`ob_v2p1/LICENSE-INPROGRESS.md` (🔴 *"for IMS Global Contributing Member and/or Invited Guests
only"*). 🟢 **Both failure modes live in one repo, so it is the fixture for both gaps.**

## Usage

```sh
python3 agree.py --self-test            # 15/15, offline, no network
python3 agree.py SLUGS_FILE             # one owner/repo per line; TSV on stdout
```

🔴 **It refuses empty input** — no arguments, an empty file and a missing file each exit non-zero
with a message naming the correct invocation. 🟢 That is `Gap 245` / `P541`'s defect class, asserted
in the suite rather than assumed.

🟢 **`P355`: every path is resolved from `__file__`**, so it runs from any working directory — unlike
`p441`, which inserts a **relative** `sys.path` entry and must be run from its own directory.
🔵 `p786` therefore invokes it with `cwd=` set, which is the wrapper's job, not the caller's.

## Known limits, stated

🔴 **It does not read prose.** `NEEDS-PROSE-READ` is a referral to a human, and 12 of 13 rows got
one — so on this frame the instrument's output is mostly *"go read twelve READMEs"*. 🟢 That is
honest rather than useless: before this pass the same 12 rows were reported as settled.
🔴 **It inherits both wrapped instruments' defects** and cannot correct them; it can only name the
direction. 🔴 **`p441` clones**, so a large frame is slow — the batch is one invocation for that
reason.
