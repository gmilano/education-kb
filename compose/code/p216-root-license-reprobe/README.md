# p216 — `ACTION QH`: testing the 18-form root probe instead of trusting it a nineteenth time

## What this measures

p211 recorded **94** shelf repositories as `ABSENT` — no licence blob at `HEAD` after 18 root path
forms. p215's `ACTION QD` recovered **25** of them through `git ls-tree`. `T215-2` then observed two
repositories that serve a **plain `LICENSE` at root** and were nevertheless recorded `ABSENT`,
which would mean the probe has a loss mode *independent of path reach*.

`ACTION QH`'s falsifier: re-probing the remainder at plain root `LICENSE` alone recovers **2+** →
every `ABSENT` figure this KB ever published measured the **instrument**. `0`–`1` → the two were
transient and the form list is sound.

## Method — deliberately one variable

1. `git ls-remote --symref https://github.com/<slug> HEAD` → the **true** default branch.
   (p205's `ACTION PC` established that guessing `main`/`master` is itself a loss mode; this pass
   found 3 repositories that do not resolve at all this way.)
2. **One** `GET` of `raw.githubusercontent.com/<slug>/<branch>/LICENSE`.

No case variants, no extensions, no subdirectories, no manifests — those channels are p215's.

## Result — limb 2 fires

| status | rows |
|---|---|
| `404` | **66** |
| `NO-SYMREF` | 3 |
| `200` | **0** |

So `ABSENT` was a root-only artefact (`P215-1`) and **nothing more**: the 18 forms do not
additionally lose a plain `LICENSE` that is present.

The 3 `NO-SYMREF` rows are p215's 3 recorded failures, reproduced on a **different** channel
(`ls-remote`, where p215 used `clone`): `cdweaver1992/edfi-mcp-server`, `jakerains/scormplayer`,
`openfresno/edgenuity-aeries-grade-passback`. Two channels agreeing means they are **unresolvable
addresses**, not ungranted repositories.

## Two defects this found in the action that commissioned it

1. **The anchor was already discharged.** Both rows `T215-2` cites — `thm-mni-ii/feedbacksystem`
   and `skhdemo/uoft-quercus-mcp` — are in p215's **own** recovered 25
   (`evidence/lstree-grant-recovery.2026-10-15-p215.tsv`), so neither was in the population `QH`
   was asked to re-probe. They were evidence that the instrument had been *fixed*, read as evidence
   that it was still broken.
2. **The population was mis-stated.** `open-gaps.md` says "re-probe the **63** remaining ungranted
   rows". `audit_arithmetic.py` recomputes it from the two committed evidence files: `94` − `25` =
   **69** raw (set-verified: 25 of 25 recovered slugs are inside the 94, 0 outside), **68** distinct
   after the one owner-case duplicate pair in the remainder, **67** after removing
   `os4ed/openSIS-Classic`, whose variant p215 already recovered as `GPL-2.0`. p215's own prose
   composition reaches `64`. See `T216-1` and `ACTION QM`.

## Run

```sh
cd /home/user/education-kb
python3 -I compose/code/p216-root-license-reprobe/audit_arithmetic.py
python3 -I compose/code/p216-root-license-reprobe/build_worklist.py > compose/code/p216-root-license-reprobe/worklist.txt
python3 -I compose/code/p216-root-license-reprobe/reprobe.py compose/code/p216-root-license-reprobe/worklist.txt
```

~69 `ls-remote` calls plus ~69 `GET`s, sequential, a few minutes. No clone.

## Evidence

- [`evidence/root-license-reprobe.2026-10-15-p216.tsv`](../../../evidence/root-license-reprobe.2026-10-15-p216.tsv) — summary and the adjudication
- [`evidence/root-license-reprobe-rows.2026-10-15-p216.tsv`](../../../evidence/root-license-reprobe-rows.2026-10-15-p216.tsv) — one row per repository

## What to do next on this population

**Not another filename guess.** The obvious path is now excluded by measurement, and p215 excluded
licence files and manifests. The one unread channel is the repository's own `README` licence
*section*, read as text — registered as `ACTION QN`, with the standing caveat that prose is not a
grant (`LICENSE-CLAIMED-IN-PROSE-ONLY`).
