# `p278-channel-conflict` — the CONFLICT class, and the pass it was already built in

## What was asked for, and what was actually missing

`p277` ranked one item **first**, at zero searches:

> 🔴 **Build the payload-vs-metadata CONFLICT class**, then sweep the metadata-grade rows — a
> conflict is only visible when **both** channels are read, and most rows have only ever had one.

and justified it:

> this base has **a grade for *payload* and a grade for *metadata* and no class at all for
> CONFLICT.** Declared for `p278`.

🔴 **The class already existed.** `p121` (2026-10-11, `ACTION Q`) built it, measured it at
scale, and published it in [`repos/trending.md`](../../../repos/trending.md):

| what `p121` measured | value |
|---|---|
| census addresses probed | 249 |
| manifests fetched (HTTP 200) | 161 |
| manifests declaring a licence | 104 |
| 🔴 **contradict the committed file** | 🔴 **10 — 9.6 %** |
| direction axis | **four values**, with the asymmetry measured: 7 of 10 overstate |

…and it wrote the operational rule this instrument now enforces: *"a manifest licence field
is a **HINT**. The committed licence file is the **grant**."*

🔴 **And the instance `p277` reported as a NEW defect class is row 8 of that table.**
`Open-TutorAi/open-tutor-ai-CE`, payload BSD-3-Clause vs `pyproject.toml` MIT — `p121` had it,
with the identical verdict (*"both permissive, wrong name"*).

🔵 **The gate for this error exists, and was not run.** Both arms verified this pass:

```
$ make claims TOKEN=conflict
ALREADY CLAIMED	conflict	STOP — read these cells before publishing an absence:
	repos/trending.md	26
	…
$ echo $?    # 1  — the STOP signal
$ python3 -I .../carried_index.py claims zzqqxx-not-a-real-token .
NOT CLAIMED	zzqqxx-not-a-real-token	(a "there is no X" claim about this is establishable)
$ echo $?    # 0
```

The Makefile documents that recipe as *"**THE GATE**: run before publishing any 'there is no
X'"*. **A pass that ranks a BUILD first without running the gate spends the pass rebuilding
what the base owns.** That is this instrument's real subject, and it is why the write-up leads
with it rather than with the code.

## So what `p278` owes: the half `p121` never built

`p121`'s census was a **one-off, by hand, at one moment**, with each verdict **typed per row**.
A typed verdict rots two ways a row-count gate cannot see: a later pass updates the family cell
and leaves the direction cell alone, or the direction was wrong when typed.

🔴 **Both are live.** This pass's sweep read `cccareers/open-source-curriculum` first-hand:
the payload is **`CC-BY-NC-SA-4.0`** (`LICENSE.md`, `1 891` B) — **non-commercial**. `p121`'s
row glosses it as *"🟡 **CC-BY** family"* and types *"permissive over attribution-share"*.
**Attribution-share reads as "ship it with credit". NC forbids the deliverable outright.** On a
*curriculum* repository — exactly what a studio reuses — that is the expensive kind of wrong.

| file | half | what it does |
|---|---|---|
| `direction.py` | OFFLINE | `direction(manifest_family, payload_family) -> (verdict, severity, prose)`. A permissiveness **tier**, not an equality test, because the two directions do not cost the same |
| `test_direction.py` | OFFLINE | **66 controls.** `p121`'s ten reproduced as fixtures, its measured 7/1/2 asymmetry asserted as a property, every negative arm, and the defects this instrument shipped with |
| `conflict_gate.py` | OFFLINE | Re-derives **every published direction** in `p121`'s table from its own family cells. Wired into `make hooks` as `make gate-conflict` |
| `test_conflict_gate.py` | OFFLINE | **31 controls** over the gate's PARSING — where it failed first |
| `sweep.sh` | **ONLINE** | Reads BOTH channels per slug at a pinned ref. `make conflict-sweep SLUGS=f`. Out of `hooks` |

## Why a tier and not an equality test

`p121` measured that **7 of 10 contradictions declare something more permissive than the
repository commits**, and named the consequence: **every licence gate in a client's CI reads the
manifest.** `npm ls --json`, `pip-licenses`, most SBOM generators and most SCA scanners report
the declared field. The directions are therefore not symmetric:

* manifest **more** permissive than payload → the client's gate returns *pass* and the copyleft
  or commercial obligation **ships undetected**. 🔴 This is the one that bills.
* manifest **less** permissive than payload → the gate over-blocks. 🟡 `p121` called it *"the
  harmless direction"*, and that is right: it costs a conversation, not a breach.

Equality cannot express "dangerous in which direction", so the table carries tiers 0–5 and the
verdict is derived from their comparison.

## The three defects this instrument shipped with, measured rather than confessed

This base's new instruments keep failing their **first honest sweep**. These were found that
way, before any finding was written up.

1. 🔴 **A green run over an empty input.** `sweep.sh` documented a `<slugs-file>` argument and
   implemented `while read` over **stdin** — it copied `enumerate.sh`'s stdin shape and kept its
   own usage line. Under `nohup`, stdin is `/dev/null`: the sweep printed its header, read
   **zero** slugs and **exited 0**. That is `p252`'s silent-zero class (`ACTION XR`) arriving in
   a harvester instead of a suite, so the remedy is the same: the input is resolved explicitly,
   **and an empty read now exits 1**, because a sweep that measured nothing must not look like a
   sweep that found nothing.
2. 🔴 **The most expensive row went `UNPLACEABLE`.** The shared classifier emits `FAIRCODE`;
   this table spelled it `FAIR-CODE`. `leemonade/leemons` — the grant that bills **€100 000 past
   1 000 users plus 5 %** — was the row that fell through. 🟢 Fixed, and bound: `TIERS` now
   covers **every token `lib/license_family.sh` can emit**, and a control asserts it, so adding
   a family there fails the suite here until it is placed.
3. 🔴 **`MITIGATED` placed as permissive.** The first `tier_of()` normalised any unknown family
   onto a known **prefix**, so `MITIGATED` → tier 0, `MIT-plus-clause` → tier 0, and —
   worst — **`Apache-2.0-with-Commons-Clause` → tier 0**, when the Commons Clause **removes the
   right to sell**. 🔵 The fix was already written one library over: `__decl`'s `P299`, *"A
   licence token is a word or it is noise"*, after `mit` matched inside permit/submit/limit.
   **Same class, one layer up** — there the token was a word, here a family name, and the noise
   was an arbitrary suffix. A restriction marker now outranks any base name, and a prefix
   normalises **only** onto a version or an SPDX scope suffix.

🔵 **And one defect left standing, named.** `sweep.sh` reads **root** manifests only, so
`ls1intum/Athena` returned `NO-CHANNEL` — while `p275` established that **12 of Athena's 14
manifests declare MIT**, all in subdirectories. *"A monorepo declares its grant per package"* is
`p275`'s own sentence, and this instrument re-committed the error it corrects. The per-package
manifest walk is registered, not built.

## What `UNPLACEABLE` is for

`UNCLASSIFIED`, `CC-UNSPECIFIED` and `MULTI-GRANT-FRAMEWORK` are **deliberately** unplaceable.
Each is what the shared classifier emits when it HAS read a payload and cannot decide the
question asked here. Giving them a tier converts *unknown* into a permission or a prohibition,
and both are inventions. 🔴 `UNCLASSIFIED` sat at tier 5 in this file's first cut, which reads
as *proprietary* — it is not; it means the text could not be identified. An **absent** grant
(`NONE`) is a measurement and stays at tier 5. Unreadable text is not.
