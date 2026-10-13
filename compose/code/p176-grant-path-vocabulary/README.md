---
industry: education
region: Global
updated: 2026-10-13
---

# `P176-B` — one grant-path vocabulary, and the word *"exhaustive"* earned

Artefacts and suite of the **one-hundred-and-seventy-sixth pass (2026-10-13)**.
🟢 **`19`/`19` green under `python3 test_grant_paths.py`.**

## Why the pass needed the instrument

`ACTION KJ` was sent to settle `gap 133`: p175 found an `MIT` grant at the
British spelling `LICENCE` on `uccser/cs-field-guide` and concluded that every
*"no grant file — exhaustive"* verdict in this KB had been reached with an
incomplete probe.

🟢 **`0` verdicts converted.** Four published absence claims were re-probed at
`16` paths each — every British spelling and `COPYING.md` included:

| subject | hits | verdict |
|---|---|---|
| `JushBJJ/Mr.-Ranedeer-AI-Tutor` | 🟢 `0` of `16` | STANDS |
| `os4ed/openSIS-Classic` | 🟢 `0` of `16` | STANDS *(its `GPL-2.0` is at `docs/License.txt`, `T209`)* |
| `formalms/formalms` | 🟢 `0` of `16` | STANDS *(`GPL-2.0` at `html/license.txt`, `gap 116`)* |
| `spdx/license-list-data` | 🟢 `0` of `16` | STANDS |
| 🟢 **CONTROL** `uccser/cs-field-guide` | 🟢 **`1` of `16` — `LICENCE`, `1 128` B** | 🟢 **the instrument is validated by a positive it was required to find** |

## 🔴 But the census underneath the answer is the finding

🟢 **`76` grant-path probe lists in `compose/code/`:**

| property | count | share |
|---|---|---|
| carry `LICENSE` | `76` | `100%` |
| 🟡 **carry `LICENCE`** | 🟡 **`48`** | 🟡 **`63.2%`** |
| 🔴 **carry `COPYING.md`** | 🔴 **`3`** | 🔴 **`3.9%`** |

🆕 🔵 **`T272` — a probe list copied `76` times is not a list, it is `76` lists,
and extending it is a migration, not an edit.** p175's sentence
(*"`P50`'s probe list misses `LICENCE`"*) implied one list and one fix.
🟢 **`p120-unread-grant-resolution/probe.sh` has carried `LICENCE LICENCE.md`
all along — which is how this KB found `cs-field-guide` at all.** 🔵 **The defect
was never the spelling; it was that no two instruments agree on the vocabulary.**
🟢 **And `0` published verdicts change, so this is debt rather than error
(`gap 135`).**

## What the module does differently

🟢 **It makes an absence claim carry its own falsifier.**

```python
>>> absence_claim("JushBJJ/Mr.-Ranedeer-AI-Tutor", "main", 16, 0)
'…: 0 of 16 grant paths at ref main (vocabulary v1) — an absence AT THESE PATHS ON THIS REF'
```

🔵 **A claim written that way can be re-run when the vocabulary grows.
*"No grant file"* cannot.**

🔴 **`NOTICE` is in the vocabulary and flagged as NOT a grant**, probed last. An
`Apache-2.0` project with a `NOTICE` and no `LICENSE` has an attribution file
and no grant; a vocabulary that counted it as a hit would convert a true absence
into a false licence. 🟢 **Three tests hold that boundary.**

## 🟢 And the word *"exhaustive"*, earned for the first time

🔵 **Probing `16` paths does not earn it. Enumerating does.**
`exhaustive_claim()` renders the only claim entitled to the word, and p176 earned
it on the shelf row that had been carrying it since p169:

| branch | tracked files | grant-shaped paths |
|---|---|---|
| `main` | `12` | 🟢 `0` |
| `v2.6.2` | `12` | 🟢 `0` |
| `v2.6.3` | `13` | 🟢 `0` |
| `dev/v2.7` | `9` | 🟢 `0` |
| `Speedrun-Brother` | `9` | 🟢 `0` |

🟢 **`55` file-paths across all `5` branches the remote advertises, `0`
grant-shaped at any case.** 🔵 **Before p176 the word meant *"the default
branch"*. `enumeration_beats_probing()` names the threshold at which a tree
should be listed instead of probed — a judgement about cost, stated so it can be
argued with, not a measurement.**

## 🔴 One channel defect found by control, and it limits this instrument too

🔴 **On `raw.githubusercontent.com`, `master` is served as an alias of the
default branch for repositories that have no `master` — and `main` is NOT
aliased the same way (`T273`).** Controls: `verichalk/master/LICENSE` answers
`200` while `git ls-remote` advertises only `dev` and `main`;
`cs-field-guide/main/LICENCE` is `404` while `master` is `200`; a nonsense ref
`404`s on both.
🟢 **Consequence for this instrument, acted on: resolve the default branch with
`git ls-remote` and probe THAT ref by name.** `probe_spellings.sh` currently
guesses `main` then `master` by a `README` probe, and that is the weakest line
in it. 🔵 **`ACTION KJ`'s own results are unaffected — `0` of `16` at every path
on every ref tried, and the positive control confirmed on the ref
`git ls-remote` reports.**

## Files

| file | what |
|---|---|
| `grant_paths.py` | the versioned vocabulary, the `NOTICE` boundary, the claim renderers, the enumeration threshold |
| `probe_spellings.sh` | the `16`-path probe, with its own weakest line declared above |
| `test_grant_paths.py` | `19` offline tests — `6` vocabulary shape, `3` `NOTICE` boundary, `3` fabricated negatives, `4` claim rendering, `3` enumeration boundary |
| `result.probe.2026-10-13-p176.tsv` | the `5` subjects × `16` paths, with HTTP codes and byte counts |
| `result.probelist-census.2026-10-13-p176.tsv` | the `76` probe lists and which spellings each carries |

🟢 **Reproduce:**

```bash
python3 test_grant_paths.py                              # 19/19
python3 grant_paths.py                                   # print the vocabulary
bash probe_spellings.sh uccser/cs-field-guide master     # the known positive
```

🔴 **One limit, declared: nothing in this instrument has been WIRED into the
other `76` lists.** 🟢 **The migration is registered as `gap 135` rather than
claimed as done — this pass delivers the vocabulary and the tests, not the
`76` call-site edits.**
