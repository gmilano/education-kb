---
industry: education
region: Global
updated: 2026-10-20
---

# `p349-name-collision` — `ACTION ZZ-ag`, run at last, because the pre-filter is offline

```sh
python3 -I name_collision.py census  <shelf files…>   # denominators only
python3 -I name_collision.py probe   <shelf files…>   # the bounded probe list
./head_equality.sh probes.tsv                         # the online half
./canonical_address.sh addresses.txt                  # the HTML 301 channel (403 here)
python3 -I alias_gate.py <register.tsv> <shelf files…>
python3 -I test_name_collision.py                     # 16 controls
```

Committed run: [`alias-head-equality`](../../../evidence/alias-head-equality.2026-10-20-p349.tsv) ·
[`alias-register`](../../../evidence/alias-register.2026-10-20-p349.tsv) ·
[`alias-bounded-probe-list`](../../../evidence/alias-bounded-probe-list.2026-10-20-p349.tsv) ·
[`alias-canonical-html-channel`](../../../evidence/alias-canonical-html-channel.2026-10-20-p349.tsv).

🔵 **Namespace note, because this is the first pass where the two collide.** This directory is named for **pass 349**. `compose/code/p349-star-resolution-band/` is named for **finding `P349`** (pass 111's star-resolution band). The `p<N>-` prefix has carried both meanings on this base for a long time; it is written down here so a successor reading `make gate-alias-canonical` does not go looking for a star channel.

## Why ZZ-ag had gone unrun rather than unanswered

p348 asked for the HEAD-equality test over **all 2 462 folded addresses**. That is 2 462
network probes, which no pass has an hour for — so the action was, in practice,
unrunnable. 🟢 **The observation that made it runnable costs nothing:** every alias this
base has found shares its repository NAME, because an org transfer moves the owner and
keeps the name. Grouping offline by folded name and probing only names with two or more
distinct owners is **281 probes, 88.6 % fewer**.

| measured, this pass | |
|---|---|
| folded addresses on the nine shelves | **2 462** (re-derives p348's figure exactly) |
| names with two or more owners | **105** |
| addresses probed | **281** |
| alias groups found | 🔴 **21** (43 addresses; one group of three) |
| addresses that did not answer | 🟡 **17** — `ACTION ZZ-aj` |

## 🔴 The declared hole, which is asserted as `C5` and not left in prose

A transfer that **also renames** is invisible to the name pre-filter, exactly as a
renamed owner is invisible to a case fold. This instrument is a COST REDUCTION with a
known hole, never a proof of absence. The instrument with the opposite blind spot is
`p349-payload-digest`: a digest does not read the address at all.

## 🟡 The canonical question, and the channel that answers it here

HEAD-equality says *"one repository"* and stops. **Which address is current** is a
different question, and the obvious channel — `curl -I` on the HTML address, `301` with
`location:` — returned **`403` on all 43** to this session (`p313`'s binding, third
instance). The **search index's `full_name`** answers instead, and the five it resolved
are in the register. 🔵 **The register is committed, dated evidence rather than a
gate-time judgement, precisely because the channel that fills it can be shut.**
