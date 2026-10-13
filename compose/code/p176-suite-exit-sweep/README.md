---
industry: education
region: Global
updated: 2026-10-13
---

# `P176-A` — the full-suite exit-code sweep, and the flag that faked a third of it

Artefacts and suite of the **one-hundred-and-seventy-sixth pass (2026-10-13)**.
🟢 **`16`/`16` green under `python3 test_suite_sweep.py`.**

## Why the pass needed the instrument

`ACTION KL` asked for the full-suite non-zero rate in `compose/code/`, against
the **`9` of `28`** (`32.1%`) p175 measured on a five-instrument sample, with a
falsifier at `<10%` (*"p175's figure was a sampling artefact"*) and `>60%`
(*"`compose/code/` is not a suite at all"*).

🟢 **Measured: `665` script executions across `259` instruments.**

| invocation | non-zero | rate |
|---|---|---|
| 🔴 **`python3 -I`** — the command this repository's own READMEs prescribe | `293` of `665` | 🔴 **`44.1%`** |
| 🟢 **plain `python3`** | `260` of `665` | 🟢 **`39.1%`** |

🟢 **Both limbs SILENT: `39.1%` is neither under `10%` nor over `60%`, so
p175's sample was the right order of magnitude.** 🔵 **And `32.1%` turns out to
be very close to the share of executions that mean anything — see the last
table.**

## 🔴 The finding that outranks the rate: `-I` strips the script's own directory

`python3 -I` implies `-P` from Python `3.11`, so `sys.path[0]` is **not** the
script's directory. Every test here that imports the instrument beside it raises
`ModuleNotFoundError`.

| | `python3 -I` | plain `python3` |
|---|---|---|
| test scripts passing | `156` of `203` | 🟢 **`189` of `203`** |
| test scripts CRASHING | 🔴 **`36`** | 🟢 **`0` as a class** |

🔴 **`35` of the `36` crashes PASS without the flag.**
🆕 🔵 **`T271` — a sweep that runs one invocation measures its own argv.** The
rule this instrument now follows: run the sweep **both ways** and publish both
rates, because a single rate is a statement about the invocation and not about
the suite. 🔴 **It also means this repository's documented reproduce line —
`python3 -I test_x.py` — cannot run a whole class of its own tests, and
`rerun_dated.py` at `P175-A` used the same flag.**

## What a non-zero exit actually means, which the rate alone cannot say

The classifier reads what the script PRINTED and separates the classes. Full
rule, with its ordering, in the module docstring.

| class | instrument | test | means |
|---|---|---|---|
| 🟢 `ok` | `216` | `189` | — |
| 🟡 **`usage`** | 🟡 **`111`** | `0` | wanted a CLI argument. **Not broken — invoked wrongly by this sweep** |
| 🟡 `timeout` | `66` | `7` | did not finish in `12` s. Slow or networked, not necessarily broken |
| 🟡 `input` | `17` | `0` | an expected input file is absent |
| 🔴 **`assert`** | 🔴 **`1`** | 🔴 **`5`** | 🔴 **the instrument RAN and DISAGREES with the repository** |
| 🔴 **`crash`** | 🔴 **`4`** | `0` | 🔴 **cannot execute at all** |
| 🟡 `other` | `47` | `2` | non-zero, none of the above matched |

🟢 **So `10` of `665` executions (`1.5%`) mean something is actually wrong**, and
`128` are this sweep's own argv or the egress policy. 🔵 **The `39.1%` headline
and the `1.5%` that matters are both true, and only publishing both is honest.**

🔴 **The `10` that matter, named so they can be fixed:**

| class | instrument |
|---|---|
| 🔴 `assert` | `p351-star-digit-sweep/test_p351.py`, `p356-citation-origin/test_origin.py`, `grant-ladder/test_ladder.sh`, `p126-address-binding/test_p126.sh`, `p598-register-freshness-gate/test_freshness_gate.py`, `p399-census-order-gate/census_order.py` |
| 🔴 `crash` | `p141-schema-location/schema_location.py`, `p144-not-shipped-breadth/ds_readmit.py`, `p213-envelope-aad/vendored_crypto.py`, `p238-fork-testsuite-contradiction/check_contract.py` |

## The classifier was wrong first, and the record says so

🔴 **Iteration `1` left `88` exits as `other`.** Iteration `2` named `36` of
them:

- **`35`** shell scripts refusing a missing `$1` — `$1: unbound variable`,
  `line 26: 1: tokdir`. A POSIX shell prints none of the cues an `argparse` exit
  prints, so an English-`usage:`-only rule under-reads them as broken.
- **`4`** suites reporting their own score in PROSE — `7/10 controls passed` —
  which no `FAILED`-matching rule can see. 🔵 **This correction moved rows INTO
  `assert`, the only class that counts against the repository, so the second
  iteration was not merely flattering.**

🟡 **`49` rows remain `other`, and one class inside them is identified and NOT
fixed: `mcp-allowlist-gateway/gateway.py` prints its usage line in SPANISH
(`uso:`).** 🟢 **It is frozen as a fixture and asserted as a LIMIT, so the pass
that fixes it will see this suite change (`gap 137`).**

🟡 **The committed result files were produced by iteration `1` and are NOT
rewritten** — `result.reclassified.2026-10-13-p176.tsv` carries the correction
beside them, per `P175-A`'s rule against destroying dated evidence.

## 🔴 And the sweep's own side effects, measured

Running the suite rewrote **`11` committed files across `7` instruments** and
created `2` more. All were restored to `HEAD`.

🔴 **That is `7` instruments, where `ACTION KF` measured `1` on a five-instrument
sample** — so `gap 131`'s sibling is wider than p175 could see, and this
instrument must never be run against a tree with uncommitted work in
`compose/code/`.
🟢 **One of the created files is a gift:
`p120-unread-grant-resolution/evidence/..._LICENCE.md` — p120's own probe list
has carried the British spelling all along, which is how
`ACTION KJ` had a known positive to validate against.**

## Files

| file | what |
|---|---|
| `suite_sweep.py` | the sweep and the classifier; rule and ordering in the docstring, `--no-isolate` and `--slice=i/n` |
| `reclass.py` | iteration `2`, run only over iteration `1`'s `other` rows |
| `test_suite_sweep.py` | `16` offline tests — `4` positive, `3` for `T271` run both ways, `2` fabricated-negative, `2` known-limit, `5` rule-shape |
| `fixtures/` | the controls, each frozen from a real shape in this repository |
| `result.isolated.2026-10-13-p176.tsv` | `665` rows under `python3 -I` |
| `result.non-isolated.2026-10-13-p176.tsv` | `665` rows under plain `python3` |
| `result.reclassified.2026-10-13-p176.tsv` | iteration `2` over the `88` unnamed rows |

🟢 **Reproduce:**

```bash
python3 test_suite_sweep.py                                  # 16/16
python3 -I suite_sweep.py ../ --slice=0/4 --timeout=12        # one shard, isolated
python3 -I suite_sweep.py ../ --no-isolate --slice=0/4         # the same shard, not isolated
python3 -I suite_sweep.py ../ --summary                        # counts only
python3 -I reclass.py ../ result.non-isolated.2026-10-13-p176.tsv
git checkout -- . && git clean -fdq        # ALWAYS, afterwards
```

🔴 **Three limits, declared.** The sweep executes repository code; it does not
restore the tree itself, so the `git` line above is part of the procedure. It
invokes every script with NO arguments, which is why `usage` is the largest
non-zero class. And the `12`-second timeout is a choice, not a measurement — a
slower bound would move `73` rows and nothing else.
