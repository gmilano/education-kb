# `pass256-ladder-closure` — the ladder a pass TYPES must carry the paths this base has already PROVEN

**Pass 256 · 2026-10-17 · 38/38 controls · in `make hooks` · proven able to fail**

## 🔴 The finding, and it is about this base rather than about a repository

`P1057` (p189) published this, in its own README, as a closed finding:

> `openedx/XBlock` … **That verdict is refuted.** The file is `LICENSE.TXT` — uppercase
> extension — `11 358` B of verbatim Apache-2.0 … `raw.githubusercontent.com` is
> **case-sensitive**. A path list that spells the extension in one case has not looked for
> the file; it has looked for **one spelling** of the file.

🔴 **Sixty-seven passes later, `p256` probed [`openedx/xblock-sdk`](https://github.com/openedx/xblock-sdk) — a sibling repository in the SAME organisation — with `LICENSE`, `LICENSE.txt`, `LICENSE.md`, `LICENSE.rst`, `COPYING`, got `404` on all five, and was one keystroke from publishing `NO_LICENCE_FILE`** on a repository whose Apache-2.0 body is `11 358` B at `LICENSE.TXT`, `sha256`₁₆ `cfc7749b96f63bd3` — **byte-identical to [`openedx/edx-lint`](https://github.com/openedx/edx-lint)'s, which serves the same text at `LICENSE.txt`.**

🟡 **And the repository's own prose points at the path that `404`s.** `README.rst` line `160`
reads *"Please see `LICENSE.txt <LICENSE.txt>`_ for details."* A probe that trusts the
project's own documentation gets a `404` and a wrong verdict.

🟢 **Why it had not been found is the part worth carrying.** `P1057` was never lost: it
exists, it passes, it is in the gate. 🔴 **`LICENSE.TXT` was simply ABSENT from `p229`'s
`TIER_A` — the `41`-path ladder that `make reach` prints precisely so that "a list you
cannot print is a list that gets copied" (`T272`).** The knowledge was wired and nothing
consumed the wire: `p253`'s lesson, arriving through a path list instead of an exit status.

## 🟢 The second path, and it is new

[`openstax/fine_print`](https://github.com/openstax/fine_print) answers `404` at `LICENSE`
and at `LICENSE.txt` and serves its real MIT grant at **`MIT-LICENSE`** — `1 055` B,
`sha256`₁₆ `0a9ed2a2ba710b61`, `main` @ `3b75fbcbcfb0`. That is the Rails/Ruby gem
convention; `LICENSE-MIT` + `LICENSE-APACHE` is the Rust dual-grant one. 🔴 **Both were
invisible to `lib/licence_path.sh`'s `is_licence_path`, the shared `P441` predicate that is
in `make hooks` and is copied byte-for-byte into `p196-none-tree-reach/tree_reach.sh`** —
its globs are dot-anchored, so a hyphenated token cannot match.

🟢 **Fixed in both copies, identically** *(the suite's byte-for-byte identity control is
what makes it one predicate and not a fork)*, as a **FORM** rather than a list of tokens,
with a prose guard so `license-faq.md` and `third-party-license-report.json` stay out.
🟢 **Six new controls in `lib/test_licence_path.sh`, and all six FAIL against the
pre-`p256` predicate** *(`38/44`)* — which is what makes the extension a measured
correction rather than a preference.

## 🟢 What this instrument asserts

| control | what it holds |
|---|---|
| **CLOSURE** | every **ROOT-form** path that `lib/test_licence_path.sh` asserts to be a licence path is present in `p229`'s `TIER_A`. The suite is in the gate, so an omission is a **proven** case left out, not a guess |
| **AGREEMENT** | every `TIER_A` entry satisfies `is_licence_path`. The ladder and the predicate cannot drift apart |
| **REFUSAL** | a captured `404` body — `14` B, `404: Not Found`, `sha256`₁₆ `d5558cd419c8d46b` — is **not a grant**, at any path, however licence-shaped the path |
| **CASE** | `LICENSE.txt` and `LICENSE.TXT` are two **addresses**, not two spellings of one, and both are in the ladder |
| **EXEMPTION** | the one proven root form deliberately **not** in the ladder is named with its reason, as an exact set, so a later pass cannot quietly grow it |

🟢 **`TIER_A` `16` → `26`; the ladder `41` → `51` paths.** Seven of the ten additions were
already proven somewhere in this base before being added here. 🟡 **The cost is `10` more
requests per slug on the online ladder; the price of not having them was two false verdicts
in a single pass.**

## 🔴 The falsifier, and it is inside the suite

`closure_gaps` is run against the **pre-`p256` `TIER_A`** as a fixture and must name both
`LICENSE.TXT` and `MIT-LICENSE`. An **empty** ladder may not grade as closure either
(`p146`/`p542`'s empty-input floor). Removing one path from the live ladder was measured:
suite `37/38`, exit `1`; `--verify` exit `1`, naming the path.

🔵 *Refuted if a later pass finds that every grant on these shelves is reachable from the
pre-`p256` `16` names — in which case the closure is ceremony. `p256` measured the opposite
twice in one pass, in two different organisations' conventions.*

## 🟡 On the directory name

This directory is `pass256-`, not `p256-`. 🔴 **`ACTION YD` has asked for five passes that
the `pNNN` namespace collision be resolved** — `p441` and `p1057` are **rule** indices while
`p253-gate-propagation` is a **pass** index, and a reader cannot tell which from the name.
🟢 **The convention from here: a rule-derived instrument keeps `pNNN-`, a pass-derived one
takes `passNNN-`.** 🔴 **The ~`300` existing `pNNN-` pass directories are NOT renamed** —
every shelf links them by path, and a rename would break several hundred live links to buy
nothing. The collision is therefore **closed going forward and left standing behind**, which
is stated here rather than claimed as a full discharge.
