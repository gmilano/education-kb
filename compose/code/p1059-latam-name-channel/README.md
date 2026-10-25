---
industry: education
region: Global
updated: 2026-10-25
---

# `p1059-latam-name-channel` — pass 444's repository probe, and the leg that paid `Gap 443-B`

## `probe.sh` — the grant probe, through the git channel

No `curl`. The fetch half of `lib/probe_payload.sh` is network-denied on this host, so this
probe gets the same rows through git instead:

* existence and default branch from `git ls-remote --symref`
* **every** grant path from `git ls-tree -r` over a **blobless, no-checkout** clone (`p442`: the
  root row is not the whole grant), filtered by `lib/licence_path.sh`
* every payload measured **from the file** by `lib/measure`, so `P834`'s trailing-newline run
  survives into the published cell

`shard.sh` runs it in N parallel shards and merges, because serial the 321-slug shelf sweep is
clone-bound at ~20 s/slug (~1.8 h); six shards bring it to ~18 min.

## 🔴 Three defects in this probe, recorded

1. **`git` inside a `while read` loop reads the loop's stdin.** A `git clone` of a slug that
   404s does not fail — it **prompts for a username**, and that prompt swallowed the rest of the
   slug file in one read. → loop reads on **FD 3**, every `git` gets `</dev/null`, and
   `GIT_TERMINAL_PROMPT=0` makes a dead address fail fast and be *recorded* as absent.
2. **No completion assertion.** `lib/measure` exists so *"a pass cannot mistake a silent failure
   for a measurement of zero"*. This loop reintroduced exactly that one level up: the
   measurements were sound and the **population** was silently a fraction of what was asked for.
   → the probe now compares slugs asked to slugs reported and **exits 3** on a mismatch.
   🔵 **A guarantee at the cell level is not a guarantee at the sweep level.**
3. **Two probes, one output directory.** The first shelf attempt had two runs interleaving rows
   into one `probe.tsv`; that evidence was discarded rather than published. → each shard writes
   its **own** output directory and the merge is explicit.

## The legs

| file | what it probed |
|---|---|
| `slugs.txt` | Mexico (SIASE), Chile (UCampus), Peru (SIAGIE), Colombia (SIMAT) + the **negative control**, `dummerchen/Ucampus`, a 34 ★ *Chinese* product that outranks every real Chilean address on its own leg |
| `slugs-colombia.txt` | SIA UNAL — the country `Gap 443-B` recorded as a **nil** on the ministry leg |
| `slugs-br-cl.txt` | Brazil (SUAP) and Chile (U-Cursos), the platform the UCampus leg never reached |
| `slugs-verticals.txt` | the SUAP **ecosystem** leg, which returned the best address of the pass |

**Finding:** 6 of 8 **university**-operated platform legs pay; **0 of 5 ministry**-operated legs
do. And of 37 addresses verified first-hand, **18 (49 %) carry no grant at all.**
