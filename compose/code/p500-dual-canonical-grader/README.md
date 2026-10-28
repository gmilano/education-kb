# `p500-dual-canonical-grader`

Three scripts, written because `p500` found that grading an Apache-2.0 payload against **one**
canonical form manufactures false deviations.

## Why

`p499` retained twelve canonical payloads, including **two legitimate forms of Apache-2.0** —
SPDX's (`Apache-2.0.txt`) and the steward's own (`Apache-2.0.apache-org.txt`). It then graded
against SPDX. Measured this pass, the two forms differ by **exactly 19 operative words**
(1431 vs 1412). Every repository that ships the steward's copy therefore scores a phantom
**−19 DEVIANT**.

That is not hypothetical. `ably-labs/realtime-quiz-framework` scored −19 and is in fact
**word-identical to the steward's form**. `HKUDS/DeepTutor`, which `p499` recorded at **−17**,
is **+2** from the steward's form — so most of that −17 was the artifact, not the repository.

## The rule this encodes

> Grade against **every** canonical form held for the licence, take the **best** match, and
> inspect the residual. Never report a delta against a single form as a deviation.

## Scripts

| script | what it does |
|---|---|
| `grade.sh` | reads `repo<TAB>ref` on stdin; resolves the pinned commit SHA with `git ls-remote`, fetches the licence at that SHA from `raw.githubusercontent.com`, classifies it, and grades the operative body |
| `census.sh` | joins an enumerated band against the three curated shelves and reports which rows are genuinely unshelved |
| `verify-permissive.sh` | byte-reads the licence of every permissive row in a band TSV across 7 candidate paths |

## Known limitations, stated rather than discovered later

- `grade.sh` **abstains** (`NOT-GRADEABLE`) on split-licence and non-OSI payloads rather than
  returning a nearest-neighbour label. This is the guard clause `Gap 499-B` asked for, but it is
  implemented only for the licences the canonical set actually holds.
- The operative/appendix cut still relies on literal markers, so `Gap 499-E` is **not** closed.
  `OpenOLAT/OpenOLAT` carries **no** `APPENDIX` heading and instead appends attribution prose;
  the cut finds nothing to remove and grades that prose as operative (+99). The grader cannot
  currently tell appended attribution from an appended restriction — a human read the residual
  this pass.
- `git ls-remote` is a sound **SHA** oracle and **not** an existence oracle: a nonexistent repo
  and a private one both fail by prompting for a username. Existence is established with
  `raw.githubusercontent.com` (200/404).
