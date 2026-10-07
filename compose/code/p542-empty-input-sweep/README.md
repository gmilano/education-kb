---
industry: education
region: Global
updated: 2026-10-07
---

# `p542-empty-input-sweep/` — `Gap 243`, closed with code

**What it proves:** that **23 of 187** invocation points in `compose/code/` **report success over an
empty input** — they exit `0` having judged nothing — and that the other 164 do not, each for a
*named* reason rather than by omission.

**Why it exists:** `Gap 243` was declared at pass 43 after `P541` caught `p383-region-heading-gate`
printing `total 0` and exiting `0` **having read no files at all**, which is indistinguishable from a
clean tree. The gap prescribed the remedy in one line — *"one pass, one loop — invoke every
argument-taking instrument with no arguments and assert a non-zero exit"* — and priced it as the gap
that *"would tell this KB how much of its own evidence is real"*. This directory is that loop.

## 🔴 The loop as prescribed produces false accusations, and the run proved it twice

The gap's one-line remedy is **not sufficient**, and this is the finding rather than a caveat. Three
shapes exit `0` on empty input **correctly**, and a sweep that cannot tell them from a false pass is
committing the error class of `P502` — an instrument that cannot distinguish *"no licence file"* from
*"no repository"*.

| Shape | Exits `0` with no input | Why that is correct | Found how |
|---|---|---|---|
| **Self-discovering gate** | yes | resolves its corpus from `__file__`, not `argv` — the `p355` lesson. `p243-frontmatter-coverage` measures **146** files this way | known before the run |
| **Library module** | yes | no `__main__` block; its suite *imports* it. Invoking it is a no-op **by design** | 🔴 **the run** — 24 of the first 49 accusations |
| **stdin filter** | yes | reads `sys.stdin` / `while read`; given EOF it correctly does nothing, like `cat < /dev/null` | 🔴 **the run** — found by hand-checking **one** accusation before publishing 34 |

🔵 **Both self-inflicted defects are now mutants in the suite** (`ignora_invocable`,
`ignora_filtro`), so the regression is covered and not merely corrected — this is the `P480` lesson,
where a new instrument inherited the shared classifier's code but not its regression coverage.

## The two oracles, and the one that is weaker

| | Oracle | Applies to | Strength |
|---|---|---|---|
| **A** | `readcount.py` runs the instrument under `sys.addaudithook` and counts the **non-code files under the repo it opens**. `0` opens with exit `0` is the `P541` class **proved** | `.py` | 🟢 direct — measures the read itself |
| **B** | **silence**: exit `0` with **zero bytes on stdout *and* stderr** | `.sh` | 🟡 indirect — a weaker claim, marked as such |

🔴 **Why not a tracer.** `strace` is installed and works, but wrapping the cloned tree's code in a
tracer is not permitted in this environment. The audit hook is pure Python, runs in the
instrument's own process, and measures the open itself rather than a proxy for it.

🔴 **A `.sh` run that exits `0` and prints 13 777 bytes of real table is NOT accused** — it becomes
`P542-UNADJUDICATED-OUTPUT`, a declared gap, not an absolution. 🔵 **The sweep prefers to
under-accuse**, so every class boundary resolves in the instrument's favour.

## The result, 2026-10-07 — `result.2026-10-07.tsv`

| Class | n | Reading |
|---|---|---|
| `REFUSES` | 43 | 🟢 exits non-zero — correct, does not fake success |
| `P542-STDIN-FILTER` | 35 | 🔵 filter given EOF — not judgeable by this harness |
| `P542-NOT-A-GATE` | 31 | 🔵 library module, no entry point |
| `P542-UNADJUDICATED-OUTPUT` | 31 | 🟡 shell that emitted something — **needs oracle A for shell** |
| 🔴 **`P541-FALSE-PASS`** | **16** | 🔴 exit `0`, **zero** judged files opened — proved |
| `MEASURES` | 15 | 🟢 exit `0` and read real input (self-discovering) |
| 🔴 **`P541-SILENT-SUCCESS`** | **7** | 🔴 exit `0`, zero bytes on both streams |
| `P542-UNADJUDICATED-TIMEOUT` | 9 | 🟡 did not finish in 12 s — nothing is asserted |
| **total** | **187** | **23 confirmed defects** |

🔴 **The two most uncomfortable rows are this KB's own gap gates.** `p370-gap-gate/gap_gate.py` and
`p471-gap-gate-language/gap_language.py` both print their own header and exit `0` when invoked with
no arguments. 🔵 **The instruments that exist to catch undeclared gaps cannot themselves tell an
empty invocation from a clean tree.**

## Invocation

```sh
python3 sweep_empty_input.py <dir_compose_code> [raiz_repo]   # ~3 min, 187 invocations
python3 test_sweep_empty_input.py                             # 42/42, offline, no network
```

🟢 **This instrument does not have the defect it detects:** `sweep_empty_input.py` and
`readcount.py` both **refuse** empty input with exit `2`, and the suite asserts it.

## What this does **not** close

🔴 **Oracle A does not reach shell**, so the 31 `UNADJUDICATED-OUTPUT` rows are unjudged — a shell
instrument that exits `0` after printing a table *may* have measured nothing and printed a header.
🔵 **Remedy: a PATH shim** that logs `grep`/`cat`/`curl`/`git` invocations, or a tracer if one is ever
permitted here. 🔴 **9 timeouts are also unjudged** — raising the 12 s plazo does not fix the ones
that wait on the network. → **`Gap 244`**.

## 🔴 Side effect of running this sweep, stated because it mutates the tree

🔴 **Invoking 187 instruments with no arguments is not read-only.** A self-discovering instrument
that *writes* its result will write it: `p294-pom-in-production/sweep_pom_production.sh` resolves a
hardcoded slug list, **fetches live**, and emits `result.<date>.tsv`. 🟢 **Check `git status` after a
sweep and remove artefacts the pass did not intend** — this pass removed one, and `P545`
(`repos/foundations.md`) records what it showed before deletion: a **one-byte** difference from pass
39's run, in `pom_bytes`, an **upstream** property.

## The rule this directory leaves written

🔴 **A gate's exit code is a claim about a corpus. If the gate read no corpus, exit `0` is a lie
about an empty set** — and `total 0` is how it reads in a transcript. 🟢 **Every gate in this tree
that takes input by argument must refuse an empty argument list**, and 23 of them still do not.
