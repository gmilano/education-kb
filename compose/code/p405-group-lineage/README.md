# `p405-group-lineage` — grading a WHOLE name-collision group by its full history

🔴 **The problem this closes, in the base's own words.**
[`intel/open-gaps.md`](../../../intel/open-gaps.md) item 3 asks *"whether that crowded supply is
many projects or a few forked many times, and **nothing on these shelves currently answers it**."*
🟢 `p402` answered the **identity** half for the largest group on the ref-set channel — 20 distinct
HEADs, 20 distinct fingerprints, 0 aliases — and wrote the limit itself: *"a distinct HEAD rules out
an alias and a non-divergent fork, and does **not** rule out a **divergent** fork — that needs the
**root commit**."* 🔴 **The lineage half stayed open for three passes, and the reason is cost.**

## 🟢 Why this is not `p404`'s instrument with a loop around it

🔴 [`p404-fork-direction`](../p404-fork-direction/README.md) grades one **pair** and clones **two**
repositories to do it. A group of `N` has `C(N,2)` pairs, so `canvas-mcp`'s 20 addresses cost
**190 pairs × 2 clones = 380 clones**. That is why `p404` ranked the sweep first and still scoped it
to *"named pairs in bounded batches of ~10"*.

🟢 **The fix is not a faster clone. It is that every fact a pair verdict needs is a property of ONE
repository** — its commit SHA set, its tree SHA set, its root commits and the commits reachable from
its HEAD. Measure those **once per address** and every pair is a set operation on cached data:

| | clones | verdicts |
|---|---|---|
| 🔴 `p404` pairwise over a group of 20 | **380** | 190 |
| 🟢 `p405` group-wise over the same 20 | **20** | 190 |

🟢 **The grading rule is NOT reimplemented.** `p404`'s `verdict.grade` is **imported**, so a group
verdict and a pair verdict on the same two addresses are the *same function call* and cannot drift
from the 11 controls that already pin it.

## 🟢 What a group adds over a pair, and why it needed its own instrument

| | |
|---|---|
| 🟢 **`N` projects is a group-level fact** | A pair sharing nothing is one measurement. `N` addresses sharing nothing **pairwise** is the answer item 3 asks for, and it can only be stated once **every** pair has been asked — with its denominator |
| 🟢 **Lineage is TRANSITIVE and a pair test is not** | If `a~b` and `b~c`, the three are one family even where `a` and `c` share nothing. The citable unit is therefore the **connected component**, not the pair. 🔵 This property did **not** bind on any of the four groups measured here — every within-family pair was directly related — and it is pinned as a control anyway, because an unexercised claim is the thing that rots |
| 🟢 **A facts cache re-grades without re-cloning** | `forkgroup.sh` writes one facts file per address and `run.py` grades from it, so the measurement is re-checkable offline and the controls need no network |

## 🔴 The two mistakes a plausible wrong instrument makes

1. 🔴 **Asking ancestry against `rev-list --all`.** That set includes unmerged branches, so a commit
   can be *in* a repository and **not** an ancestor of its HEAD. An instrument that tests membership
   in it reports a fork as a superset. 🟢 The real specimen is on these shelves:
   `bibo242/blackboard-mcp` carries **28** commits over all refs and `felipedias-ie/blackboard-mcp`
   **21** — and `felipedias-ie` is the **descendant**. 🔵 The side with *fewer* total commits is the
   current one, which is the reading a commit count alone gets backwards.
2. 🔴 **Guessing a content-copy direction.** The root-tree signal fires only when **exactly one**
   side's root tree is among the shared trees. Two shared root trees is not a direction, and an
   instrument that picks one anyway publishes a provenance claim it never measured.

## Run

```sh
./forkgroup.sh canvas-mcp vishalsachdev/canvas-mcp bartmassey-upstream/canvas-mcp ...   # 20 addresses
./forkgroup.sh moodle-mcp falkenslab/moodle-mcp G36maid/moodle-mcp ...                  # 11
./forkgroup.sh blackboard-mcp alanwtom/blackboard-mcp ...                               # 9
./forkgroup.sh brightspace-mcp-server RohanMuppa/brightspace-mcp-server ...             # 4
python3 run.py GROUP /path/to/facts-cache ADDR...   # re-grade a cache, no network
python3 test_group_lineage.py                       # 12 controls, 0 failures
```

## Measured 2026-10-23 — all four groups item 3 names, closed

| group | addresses | resolved | pairs | 🟢 **projects** | families |
|---|---|---|---|---|---|
| `canvas-mcp` | 23 | **20** | 190 | 🔴 **9** | **11** + **2** |
| `moodle-mcp` | 11 | **10** | 45 | 🟢 **10** | 🟢 **none** |
| `blackboard-mcp` | 9 | **8** | 28 | **6** | 2 + 2 |
| `brightspace-mcp-server` | 4 | **4** | 6 | 🔴 **2** | **3** |
| 🟢 **total** | 47 | **42** | **269** | 🟢 **27** | 5 families, 15 addresses absorbed |

🔴 **42 addresses are 27 projects — a 1.56× overstatement — and it is NOT uniform.** `canvas-mcp`
alone absorbs **11** of the 15, while `moodle-mcp` absorbs **none**. 🔵 **That non-uniformity is the
result**: no single-group answer could have produced it, and a census that assumed either extreme
would be wrong about three of the four groups.

Row-level evidence, 47 address rows and all 269 pair rows:
[`group-lineage.2026-10-23-p405.tsv`](../../../evidence/group-lineage.2026-10-23-p405.tsv).

## Scope and cost

🟡 **A full clone per address.** Cheap on the MCP tier measured here — 42 addresses, none over
1,089 commits — and it is the only channel that answers the question: `--depth 1` and `ls-remote`
both discard exactly the objects a verdict rests on, which is `p404`'s finding and is not
re-litigated.

🔴 **`refs_clonelocal` is NOT `p402`'s ref count.** It is `git show-ref` in a fresh full clone,
a different instrument over a different population. The column is **named** so it cannot be diffed
against `p402`'s `ls-remote` numbers, and that name is pinned by a control — `Gap 400-A` as a
meta-control rather than as a warning in prose.

🔵 **What it does not answer.** A shared tree or commit proves a relation; it does not grade
**quality**, and 7 of `canvas-mcp`'s 20 addresses are genuinely sole projects. Nor does it reach an
address that does not resolve: **5 of 47** are `UNRESOLVED`
(`eastarctica`, `owen-x-tech`, `owentaylor` on `canvas-mcp`, `nahuelalbornoz/moodle-mcp`,
`e9x/blackboard-mcp`) and they are recorded as such rather than dropped.
