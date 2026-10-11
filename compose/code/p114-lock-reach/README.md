---
industry: education
region: Global
updated: 2026-10-11
---

# `p114-lock-reach` — a lockfile that does not reach the manifest is not a lock

**Pass 113.** Census window **2026-10-10 23:54 UTC → 2026-10-11 00:25 UTC** (the run
crossed midnight; the pass is dated by its publication date, and every result file
carries `2026-10-11`).

🟢 **`test_p114.sh` — 98 passed / 0 failed**, fully offline: real git repositories
committed on disk and served to the real `reach.sh` over `file://`. No mocks, no
network, no `api.github.com`.

🟢 **`reach.sh` read 296 of 296 shelf addresses in 4 m 09 s, `rc=0` on every one,
zero `UNREAD`** — plus **two full control runs over the same 296 addresses**, so both
of this pass's rule changes are measured rather than asserted.

## Why this axis, and why now

p112 published **107 of 296 rows (36.1 %) at `pinned`** and, in the same file, declared
the error that figure carries:

> **P112-E** — "An ecosystem counts as locked if ONE lockfile for it exists anywhere in
> the tree. In a monorepo with forty `package.json` files and one root
> `package-lock.json` that is generous. [...] every figure this script produces is an
> **UPPER BOUND** on pinning, said here rather than discovered later."

Stating an error is not measuring it. An upper bound whose gap is unknown cannot be
handed to a client team standing a platform up next quarter. **p114 measures the gap.**

It asks the resolver's question instead of the inventory's: not *does a lock exist*, but
**does a lock reach this manifest** — sitting in its own directory or an ancestor of it,
which is the only relation npm, pnpm, cargo and poetry actually honour.

Seventh axis in seven passes, third read from the TREE, and the first that can only ever
move rows **downward** — by construction (`P114-B`) no row reads more pinned here than
it did at p112.

## The headline

| figure | p112 | 🆕 p114 |
|---|---|---|
| unit of measurement | repository × ecosystem | 🟢 **manifest** (`P114-A`) |
| rows at the top verdict | 107 `pinned` (36.1 %) | 🔴 **102 `full-reach`** (34.5 %) |
| lockable **manifests** on the shelf | not reportable | **2 135** |
| manifests a lock actually reaches | not reportable | 🟢 **1 625 (76.1 %)** |
| manifests **orphaned** | not reportable | 🔴 **510 (23.9 %)** |
| rows whose **ROOT** manifest is orphaned | not reportable | 🔴 **88 of 296** |

**88 rows cannot reproducibly build the manifest you would actually build.** That is the
number this axis exists to produce: the root manifest is the entry point a client team
runs `install` against, and on 88 of 296 addresses no lock reaches it.

## The delta from p112 decomposes into TWO legs, not one

`P446` (pre-reset) established the discipline: *when a measurement walks a chain, every
leg's version is a parameter, and a chain with one leg unstated is not reproducible.*
This pass changed **two** things, so it reports both legs separately rather than
attributing the whole movement to reach.

| leg | rule | top verdict | moves |
|---|---|---|---|
| p112 as published | existence, repo-level stage B | 107 | — |
| **leg 1** — per-file stage B, existence rule kept | `result-flat.P112RULE-CONTROL` | **109** | 🔵 3 rows **up** |
| **leg 2** — positional reach (`P114-B`) | `result.2026-10-11` | 🔴 **102** | 🔴 7 rows **down** |

**Leg 1 is a divergence this pass found in p112's own stage B.** p112 accumulated
`real` and `pinned` across the *entire* `cat-file --batch` stream, so a repository was
credited only if **every** requirement line in **every** requirements file was pinned.
p114 reads each file separately, because `P114-C` needs the file's **directory**, not a
repo-level boolean. Three rows move up on that change alone:
`huggingface/transformers` and `nextcloud/translate2` (`floating` → `pinned`) and
`rohitg00/ai-engineering-from-scratch` (`floating` → `partial-pin`).

**Leg 2 is this pass's own axis.** The seven rows it moves, all `full-reach` →
`partial-reach`:

| row | orphaned / lockable | deepest | the orphan |
|---|---|---|---|
| [`Submitty/Submitty`](https://github.com/Submitty/Submitty) | 1 / 5 | 🔴 **root** | `pyproject.toml` |
| [`huggingface/transformers`](https://github.com/huggingface/transformers) | 🔴 **21 / 22** | 🔴 **root** | `pyproject.toml`, 20 × `requirements.txt` |
| [`european-commission-empl/european-digital-credentials`](https://github.com/european-commission-empl/european-digital-credentials) | 3 / 6 | 5 | `edci-viewer/package.json` + 2 |
| [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) | 3 / 8 | 2 | `demos/python/requirements*.txt` |
| [`cortezaproject/corteza`](https://github.com/cortezaproject/corteza) | 1 / 14 | 2 | `def/protobuf/package.json` |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 1 / 2 | 6 | `src/main/webapp/static/js/milkdown/package.json` |
| [`saylordotorg/moodle-local_ai_course_assistant`](https://github.com/saylordotorg/moodle-local_ai_course_assistant) | 1 / 2 | 2 | `tests/a11y/package.json` |

## What the controls measure

| run | rule changed | top verdict | what it isolates |
|---|---|---|---|
| `result.2026-10-11.tsv` | — (published) | 102 `full-reach` | the measurement |
| `result-flat.P112RULE-CONTROL-2026-10-11.tsv` | `P114_FLAT=1` restores p112's existence rule | 109 | **leg 2**: position is worth 7 rows / 53 manifests |
| `result-nostageB.NEGATIVE-CONTROL-2026-10-11.tsv` | `P114_NO_BODY=1` disables the body read | 88 | **`P114-C`**: reading requirement bodies is worth 14 rows |
| `result-P114K-reqname-gap.2026-10-11.tsv` | — (no verdict) | — | **`P114-K`**: the blind spot this pass found in its own classifier |

The stage-B control is not a formality. **16 rows depend on it**, and one of them is
`oppia/oppia` — a 🟢 recommendation on three pages of this KB, whose `full-reach` verdict
rests entirely on a pinned `requirements.txt` and not on a lockfile at all.

## The disciplines

Stated in the code beside what they govern. `P114-A/B/G` are in `cover.awk`,
`P114-K` in `gap_reqname.sh`, the channel and stage-B notes in `reach.sh`.

| id | discipline |
|---|---|
| `P114-A` | the unit is the (manifest, directory) pair, not the repository |
| `P114-B` | coverage is an ANCESTOR relation, not proximity — and still generous, so reach is itself an upper bound, a strictly tighter one than p112's |
| `P114-C` | a pinned `requirements.txt` is a lock **where it sits** |
| `P114-D` | a committed dependency tree makes reach **inapplicable**, not zero |
| `P114-E` | no claim is made where p112 made none (maven, bazel/odoo/moodle-plugin) |
| `P114-F` | a lock is evidence only about a manifest it can reach — subsumes `P112-K` and adds the case p112 cannot see |
| `P114-G` | a requirements-file credit covers its own directory only; a real lockfile covers its subtree |
| `P114-H` | the control is p112's own rule, so the delta is measured |
| `P114-K` | 🔴 `*_requirements.txt` is invisible to `P112-A` — found, sized, and bounded below |
| `P1040` | an unread row is never zero (inherited) |

### `P114-G` is the rule that moved the most, and the first draft had it wrong

The first draft gave stage B's credit the same ancestor reach as a `package-lock.json`.
A root `requirements.txt` pinned with `==` then certified every unpinned requirements
file beneath it — including a `dev/requirements-dev.txt` reading `black`. The suite
caught it (`reqmixed`), and the fix is not a fudge but the difference between the two
artefacts: **a lockfile is output** — a resolver produced it from a manifest at that
directory and, in the workspace ecosystems, enumerates the members it resolved; **a
pinned requirements.txt is input** — a list that pins itself and resolves nothing below
it.

## `P114-K` — the blind spot this pass found in its own inherited classifier

Found while verifying the `Submitty/Submitty` row **by hand**, not by the instrument.
Submitty carries four requirement files; the classifier sees one. `P112-A` matches an
anchored basename `^requirements([-_.]<suffix>)?\.txt$` — correct against
`docs/requirements.rst`, which is prose about a curriculum and is on this shelf — but it
does not match the other half of the convention.

Sized over all 296 addresses rather than left as an anecdote:

| | |
|---|---|
| requirement files **seen** by the anchored rule | 198 |
| requirement files **missed** | 🔴 **8** |
| repositories affected | 5 |
| **verdicts that would change if fixed** | 🔴 **exactly 1** |

The one is [`sdv-dev/sdv`](https://github.com/sdv-dev/sdv): its **root**
`latest_requirements.txt` is pinned on all 11 of its lines (`cloudpickle==3.1.2`,
`numpy==2.5.3`, …), so under a corrected rule it is a root lock and the row moves
`no-reach` → `full-reach`. The other four cannot move a verdict: Submitty's three live
in `.setup/pip/`, which holds no manifest, so **its root `pyproject.toml` stays
orphaned**; `elgg/elgg`'s `docs/pip-requirements.txt` is unpinned (`docutils<0.18`);
transformers' and ai-engineering-from-scratch's sit in directories whose only in-rule
manifest would be the missed file itself.

**Error direction, stated as `P114-B`'s is:** an unseen requirement file can only cost a
row coverage it has earned, never grant coverage it has not. So on this axis every reach
figure here is a **lower** bound — the opposite direction from `P114-B`'s generosity.
The two are reported separately and never netted against each other.

🔵 **The classifier is NOT forked to fix it in-pass.** `P237` forbids forking a shared
classifier, and the correction belongs with the rule p112 and p114 share. What is
committed instead is the measurement, the bound, and the one row it moves — so the next
pass decides against a number rather than a guess.

## Running it

```sh
./test_p114.sh                    # 98 passed / 0 failed, offline
./reach.sh addresses.txt          # the census (4 m 09 s over 296 addresses)
P114_FLAT=1    ./reach.sh         # p112's rule, the leg-2 control
P114_NO_BODY=1 ./reach.sh         # stage B off, the P114-C control
./gap_reqname.sh addresses.txt    # the P114-K gap probe (no verdict)
VERBOSE=1 ./test_p114.sh          # print every assertion
```

`P114_BASE=file:///path` swaps the transport, which is how the suite drives this same
code against real repositories with no network.

## Files

| file | what it is |
|---|---|
| `positions.awk` | stage 1 — path → (kind, ecosystem, **directory**); p112's tables, copied verbatim and deliberately not re-derived |
| `cover.awk` | stage 2 — the reach rule, and p112's rule under `-v flat=1` |
| `reach.sh` | the driver: fetch, positions, stage B bodies, verdict |
| `gap_reqname.sh` | the `P114-K` probe |
| `test_p114.sh` | 98 assertions in 5 layers |
| `addresses.txt` | the 296 shelf addresses (as p112 left them) |
| `orgs.region.tsv` | org → region, for the regional cross-tab |
| `result*.tsv` | the census and its three controls |
