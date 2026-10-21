---
industry: education
region: Global
updated: 2026-10-20
---

# `p349-keyed-authors` — `ACTION ZZ-ac`: an author count is not a number, it is a number AND a key

```sh
./keyed_authors.sh slugs.input.2026-10-20.txt          # one blobless clone per slug
python3 -I author_key_gate.py gate   <shelf files…>    # P349-UNKEYED-AUTHORS, live section
python3 -I author_key_gate.py census <shelf files…>    # the inherited backlog
python3 -I test_keyed_authors.py                       # 12 controls
```

Committed run: [`keyed-authors`](../../../evidence/keyed-authors.2026-10-20-p349.tsv).

🔵 **Namespace note, because this is the first pass where the two collide.** This directory is named for **pass 349**. `compose/code/p349-star-resolution-band/` is named for **finding `P349`** (pass 111's star-resolution band). The `p<N>-` prefix has carried both meanings on this base for a long time; it is written down here so a successor reading `make gate-alias-canonical` does not go looking for a star channel.

## What it answered

p348 could not re-derive its own published cell — *"2 815 commits, 18 authors"* for
`terracotta-education/terracotta`. Read at the pin `00fc046c181e`: **2 815 commits,
`%an` 14, `%ae` 18, `%an|%ae` 20.** 🟢 **The key is `%ae`**, and every figure re-derives
exactly. The figure was never wrong; it was unnamed.

🔴 **The hazard is directional.** p346's PII refusal pushes a successor towards `%an`,
which runs below `%ae` on every row measured — so all 220 unkeyed cells would read as
inflated and the KB would look like repositories shedding contributors.

**Census over the nine shelves: 230 author figures, 220 with no key (95.7 %).** A
backlog with a denominator; the gate binds only what a pass writes from here.

## 🔴 The defect this instrument's own first build shipped

Build 1 read the top timezone offset with `cut -d'×'`. **`cut` refuses a multibyte
delimiter** — *"the delimiter must be a single character"* — twice per row on stderr,
while the row printed a plausible `-` in both columns. `×` was this base's own choice of
separator in the histogram it had just written. 🔵 **A defect that writes a plausible
value is worse than one that crashes.** Fixed with bash parameter expansion, which is
byte-blind; asserted as `C9` (the parse) and `C10` (that `cut` still refuses it, so the
fix stays load-bearing).

## The three channels and their limits

* `commits` — exact and re-derivable.
* `an` / `ae` / `an_ae` — aggregate counts only. No name and no address is ever written
  out (p346's refusal).
* `tz_*` — author-time UTC offsets, a PLACEMENT channel and not a nationality. The whole
  histogram is printed so a mixed stream stays visible instead of collapsing into one
  verdict — which is why `OpenMined/PyDP` is published as **NOT PLACED** with 17 offsets
  rather than as APAC on its top one.
