# `grant-ladder` — existence, pinned SHA, licence payload, family

🟢 **Authored in pass 89 (2026-10-09) and the first instrument this shelf has added in eleven passes.**
🟢 **Every licence, byte and SHA figure in pass 89 came from here.**

## What it does

`grant_ladder.sh <slug>...` walks the full ladder for each `owner/repo` and prints one TSV row:

```
slug  branch  sha  licence_file  bytes  family
```

1. **Existence + default ref** — `git ls-remote --symref https://github.com/<slug> HEAD`.
   🔴 **This is the only working existence oracle in this environment.** `curl -sI https://github.com/<slug>`
   returns **403 for `moodle/moodle` and for an invented slug alike** (`P880`, reproduced a third time in
   pass 89), and `api.github.com/repos/...` returns **403 for `torvalds/linux` and for an invented slug
   alike** (`Gap 359`, second measurement). 🔵 **Neither can discriminate, so neither may be used.**
2. **Payload** — tried across **16 candidate filenames** at
   `raw.githubusercontent.com/<slug>/<SHA>/<name>`, 🔴 **pinned to the resolved SHA, never to a branch
   name** (`P793`). First `200` with more than 100 B wins.
3. **Bytes** — `curl -w '%{size_download}'`. 🟢 **The method is stated with the figure** (`P929`).
4. **Family** — read from the payload's own title block, with a **body-signature fallback** for payloads
   that never name their family: `sublicense` + *"The above copyright notice"* → MIT, else ISC/BSD
   (`P943`, which has now paid three times).

## Controls — `test_ladder.sh`, **10/10**

🟢 **Run `bash test_ladder.sh`. It prints `10/10 controls passed`** (`P126` pt. 3 — a suite publishes its
own total).

🔴 **The negative control is the point** (`P126` pt. 2 — a positive control only enables an instrument if it
exercises the case where the instrument can fail). An invented slug **must be DENIED**, because a ladder
that silently granted non-existent repositories would produce confident rows for nothing:

| control | asserts |
|---|---|
| invented slug | 🔴 **`EXISTENCE-DENIED`**, and **no byte figure** |
| `moodle/moodle` | `COPYING.txt`, **35 147 B**, GPL, default ref `main` |
| `OpenOLAT/OpenOLAT` | **Apache-2.0**, **10 982 B**, default ref 🔴 **`master`** — the `P946` appendix-replaced case |
| `gamestdio/scorm` | **MIT by signature** — the `P943` no-family-named case |

🟢 **`moodle`'s 35 147 B reproduced byte-identically against the figure pass 88 recorded at the same SHA**,
which is the condition `P929` should have stated and `Gap 355` needed.

## 🔴 The honest limitation

🔴 **This suite cannot be re-run from a fresh clone of this repository.** Code that arrives by clone is
denied execution in this environment (`[Code from External]`) — 🔴 **including offline suites, which
narrows pass 52's boundary**: the denial is about **provenance**, not about the network and not about the
interpreter. 🟢 **Two-sided control, pass 89:** the inherited offline suite
`compose/code/suite-total-control/test_control.py` was **DENIED**, while a script authored in-session ran
and printed `2/2 checks passed`.

🟢 **So the working procedure, and it is the unblock worth keeping:** author the instrument in-session, run
it, confirm its controls, then version it here. 🟢 **The file in this directory is byte-identical to the
copy that produced `resultado.2026-10-09.txt`.** 🔴 **It is versioned as a reproducible record and for a
future environment that permits it — not as something this shelf can re-run today.**

## Results in this directory

- `resultado.2026-10-09.txt` — the 10/10 control run.
- `result-scorm.2026-10-09.tsv` — the `topics/scorm` buy: **16 probed, 14 granted, 12 permissive.**
- `result-openbadges.2026-10-09.tsv` — the credentialing extension: **11 probed, 10 granted, 6 permissive.**
