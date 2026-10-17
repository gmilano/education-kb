---
industry: education
region: Global
updated: 2026-10-17
---

# `p276-two-channel-enumeration` — the three tools `p276` actually ran, committed so the pass is reproducible

🔵 **Why these are here and not folded into `pass275-grant-enumeration/`:** `p276` ran under a sandbox
that **refuses to execute scripts from a cloned repository**. That refusal was respected, so the pass
could not run `make hooks`, `make enumerate`, or the gate. These three files are what it ran **instead** —
written fresh, from outside the repo, using plain `git`, `curl` and the standard library.

| file | what it does | network |
|---|---|---|
| `enum.sh` | the enumeration: `git ls-remote` as a positive control, then `clone --depth 1 --filter=blob:none --no-checkout`, then `ls-tree -r`. **Nothing from any cloned tree is ever executed** — `--no-checkout` means no working tree exists | yes (git smart-HTTP) |
| `queue.py` | an **independent reimplementation** of `pass275-grant-enumeration`'s predicates, written from the committed source | no |
| `simgate.py` | runs the *patched* predicates over the shelves and the ledgers, and reports what `make gate-enumeration` should report | no |

## 🟢 The positive control that makes the simulation worth anything

`sweep_tree.sh`'s doctrine (pase 93): *"un instrumento que no reproduce un positivo conocido no sostiene
una ausencia."* Applied to a **reimplementation**, the known positive is **the original's own published
output**:

```
$ python3 -I queue.py /path/to/education-kb
# REFUTED=0 VERIFIED-ABSENT=28 QUEUE-UNENUMERATED=124 DISTINCT-SLUGS=102
```

🟢 **Which is exactly what `p275` published.** A mirror that disagreed would have been measuring itself.

## ⚠️ What this is NOT

🔴 **These do not replace the gate, and they are not in `make hooks`.** They are evidence of how `p276`
reached its numbers, so `p277` can check the reasoning without re-deriving it. **`p277` must still run
the real instruments** — `make hooks` and `python3 -I test_enumeration_gate.py` from
`compose/code/pass275-grant-enumeration/`. Expected:
**`REFUTED=0 · VERIFIED-ABSENT=48 · QUEUE-UNENUMERATED=70`**, `47/47` controls.

🔵 **If the real gate disagrees with `simgate.py`, trust the gate and treat the difference as the finding** —
a mirror is only ever as good as its last positive control.

## The second channel, which is the point of the pass

`enum.sh` answers *"is there a licence FILE in this tree"*. That is **one** channel, and `p275`'s own
headline case (`ls1intum/Athena`) had its grant in a **manifest**. So every row the file channel called
absent was followed up by reading its manifests at the pinned SHA — `package.json`, `pyproject.toml`,
`pom.xml`, `composer.json`, `readme.txt` — and, where one existed, its **package registry**.

**3 of 19 carried a grant no file enumeration can see.** Ledger:
[`evidence/manifest-channel.2026-10-17-p276.tsv`](../../../evidence/manifest-channel.2026-10-17-p276.tsv).
