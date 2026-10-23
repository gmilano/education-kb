# `p404-fork-direction` — grading a same-name pair by its FULL history

🔴 **The problem this closes.** `p402` built [`p402-alias-direction`](../p402-alias-direction/README.md)
and recorded, in its own *"What it did NOT establish"* section, that for
`moodle-aiprovider_openaicompatible`, `pylti1.3`, `lti` and `moodle-mcp-server` *"the HEADs differ, so
the pairs are **not** aliases — and the fork direction stays **unestablished**."* 🟢 **It is
establishable, and not by a better ref-set test.** A ref set is derived from the current refs; fork
direction is a fact about **history**, and `--depth 1` clones and `ls-remote` both discard exactly the
objects that carry it.

🔴 **Why this is not a smaller version of `p402`'s instrument.** A **squash-republish shares ZERO
commit SHAs with its origin** — so a ref-set test grades a copy and two unrelated namesakes
*identically*. That is not a sensitivity problem to tune; the signal is absent from the channel.

## The rule

| measurement | verdict | what it means |
|---|---|---|
| 0 shared commits **and** 0 shared trees | `INDEPENDENT` | two implementations that share a name |
| 0 shared commits **and** >0 shared trees | `CONTENT-COPY` | content republished with fresh history. 🟢 **Direction**: the side whose **root** commit carries a shared tree is the copy — a root commit cannot hold content that did not already exist |
| shared commits, one HEAD an ancestor of the other | `SUPERSET` | continuation / hand-off; the descendant side is current |
| shared commits, neither HEAD an ancestor | `DIVERGED-FORK` | shared past, both sides moved |

🔵 **Tree SHAs are the load-bearing addition.** Git content-addresses directory state, so a byte-identical
tree is one SHA no matter how the history around it was rewritten. `p401` had already found the
`classes/provider.php` **blob** identical at 3,963 B and correctly refused to call it a direction; the
**tree** carries the same evidence *plus* its position in history, and position is the direction.

## Run

```sh
./forkdir.sh ADORSYS-GIS/moodle-aiprovider_openaicompatible lmscloud-io/moodle-aiprovider_openaicompatible
./forkdir.sh astiusa/lti macewan-cs/lti
./forkdir.sh lmscloud-io/moodle-mcp-server peancor/moodle-mcp-server
python3 -m unittest -v test_verdict      # 9 controls, 0 failures
```

## Reproduced, end-to-end from clean clones, 2026-10-23

```
ADORSYS-GIS/…openaicompatible  lmscloud-io/…openaicompatible  35  17   0   1  False False  CONTENT-COPY  a
astiusa/lti                    macewan-cs/lti                 91  89  89  89  True  False  SUPERSET      a
lmscloud-io/moodle-mcp-server  peancor/moodle-mcp-server       10  11   0   0  False False  INDEPENDENT   None
```

🟢 **Three pairs, three different verdicts, one channel** — and the three are precisely the pairs
`p402` left open. Row-level evidence:
[`fork-direction.2026-10-23-p404.tsv`](../../../evidence/fork-direction.2026-10-23-p404.tsv).

## Controls

🟢 **9 controls, 0 failures** in [`test_verdict.py`](test_verdict.py). The three measured pairs are
pinned as controls, and the load-bearing negative is
`test_independence_is_not_claimed_from_commits_alone`: **0 shared commits with shared trees must never
report `INDEPENDENT`**, which is the exact mistake a commit-only test makes. Two impossible inputs are
refused rather than graded.

## Scope and cost

🟡 **A full clone per address**, against `--depth 1` for the ladder channel. Cheap on the plugin tier
(the six addresses here are 10–91 commits) and 🔴 **not** affordable across `p397`'s **551** candidate
pairs / **324** addresses in one pass. 🔵 `T82` still governs the sweep: this instrument is run on
**explicitly named pairs**, in bounded batches, and `p402`'s refusal is not re-tested here.

🔴 **What it still does not establish.** `CONTENT-COPY` names the copy, not the **motive** — a
hand-off, a vendor rebrand and an unattributed lift all measure the same. 🟢 For this pass's pair the
**author identity is the same in both root commits**, so a hand-off is the reading the evidence
supports; that is a corroboration, not an output of the rule.
