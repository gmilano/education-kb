# `p227-direction-gate` — the refuted-claims gate, made bidirectional, plus a GPL/AGPL family discriminator

**Pass 227, 2026-10-15.** Discharges `ACTION SO` (p227's registered highest priority) and runs
`ACTION SH`'s inbound gate, which has been a standing step of every pass since p226.

## Why it exists

p226 found that the refuted-claims gate's binding constraint was **coverage of subjects**: every
regex fired correctly when it had a subject to fire on, and the `frappe/lms` claim escaped only
because `frappe/lms` was not in the table.

`ACTION SO` asked whether that backlog was cleared. It is not, and the gap is deeper than a
missing subject list. **Every one of p226's six rows refutes a claim that was too PERMISSIVE** —
`MIT` claimed where `AGPL-3.0` is true. So every `refuted_pattern` is a permissive-token pattern,
and the table was *structurally unable to express* the opposite error: a claim too **restrictive**.

These shelves had already refuted seven such claims first-hand and tabled none of them.

## The finding that makes it urgent

`GibbonEdu/core` is `GPL-3.0`. Read first-hand this pass: `master/LICENSE`, `35 121` B,
`sha256₁₂ 93178a43d6d3`, title line `GNU GENERAL PUBLIC LICENSE`. Its three `AFFERO` tokens all
sit inside **section 13, "Use with the GNU Affero General Public License"** — GPL-3.0's
*compatibility* clause, which permits linking with AGPL work. It is not a grant of AGPL.

p171 diagnosed that mechanism. p214 corrected the cell. Neither was tabled. Four stale
`AGPL-3.0` cells survived — and at p226 the KB's own self-audit read those cells, judged its
*correct* `GPL` draft cell to be a defect "in the PERMISSIVE direction", and published
`AGPL-3.0` again.

> An untabled refutation does not merely fail to catch an inbound recurrence.
> It lets a later pass's **verification step** become the vector that reintroduces the error.

The same pass's inbound results, from the mandated vertical query, said *"Gibbon (GPL, PHP)"* —
which is **true**. The search surface had Gibbon right and this KB had it wrong.

## What the two functions do

| function | job | why it is separate |
|---|---|---|
| `inbound_gate()` | p226's gate, behaviour unchanged, now reading a table that also carries `RESTRICTIVE` rows | a subject/pattern/exempt match is a *text* question |
| `family_of()` | decide `GPL-3.0` vs `AGPL-3.0` from a licence body | a *body* question, and three methods for it are unsafe |

### Three unsafe channels for the GPL/AGPL family, and the one that survives

1. **Byte size** — the canonical bodies are **15 bytes apart**: `35 121` (GPL-3.0, read from
   `GibbonEdu/core`) vs `35 136` (AGPL-3.0, read from `openedx/openedx-platform`).
2. **A bare `affero` grep** — a GPL-3.0 body carries **3** such tokens, all in §13. Kept in the
   code as `naive_affero_grep()` so the defect stays demonstrable: it is *wrong* on Gibbon and
   *right* on Open edX, which is exactly how a broken method survives ~56 passes unnoticed.
3. **A whole-body search for the AGPL title** — **also unsafe, and it defeated this pass's own
   first draft.** The string `GNU Affero General Public License` appears *inside* a GPL-3.0 body,
   in §13. Searching the whole body finds it and inverts the answer. Three controls failed on
   this before publishing.
4. ✅ **The title read POSITIONALLY** — the first licence title in document order, with the AGPL
   title excluded from the GPL pattern so both cannot match at offset 0. Corroborated against
   §13's heading (`Use with the GNU Affero…` ⇒ GPL-3.0; `Remote Network Interaction` ⇒ AGPL-3.0),
   and a title/§13 disagreement is reported as a `conflict` rather than silently resolved.

## Backward compatibility

The table's columns `1–6` are identical in order and semantics to p226's `sh-refuted-claims`, so
every p224/p225/p226 instrument reads it unchanged. Column `7`, `direction`, is appended and new;
a p226-era six-column table loads here and defaults to `PERMISSIVE` — the only direction it could
express. A control pins that.

## Running it

```sh
python3 -I direction_gate.py ../../../evidence/so-refuted-claims.2026-10-15-p227.tsv p227-raw-results.txt
python3 -I test_direction_gate.py        # 19 controls
python3 -I validate_real_bodies.py       # the discriminator against the real bodies (2 requests)
```

Stdlib only and offline except `validate_real_bodies.py`, because `ACTION QO` wants this in
`make hooks`.

## This pass's run

`13` subjects (`9` PERMISSIVE, `4` RESTRICTIVE) against `66` records from `14` queries:
**`0` hits, `7` near misses.** All seven near misses are reported in
[`sh-inbound-gate-run`](../../../evidence/sh-inbound-gate-run.2026-10-15-p227.tsv); three of them
expose a defect in the *table*, not the gate — the EU AI Act subject pattern matches the bare
phrase `high-risk` and so fires on Vietnamese text. Registered as `ACTION SP` rather than
narrowed here, because narrowing a `subject_pattern` can only reduce what the gate sees and must
be done on evidence.

## Controls (19, all passing)

Both directions fire on a planted claim; the exempt column still protects a source that *reports*
an error; `"Gibbon (GPL)"` stays silent because it is **true**; a p226-era table still loads; the
family discriminator is right on both real bodies; and the naive method is pinned as *wrong* so
the defect cannot quietly stop being demonstrated.

## What this does NOT establish

- It does not re-verify any star count. `api.github.com` is `403` for the 21st pass.
- It does not settle `ACTION SK`'s 90 queued name collisions. It measures **one** entity
  (`OpenTutor`: 9 cited paths, 30 of 254 citations non-canonical) and that is a sample, not a census.
- `family_of()` covers the **GPL-3.0 / AGPL-3.0** pair only. LGPL, GPL-2.0 and the or-later
  bound are out of scope and stay with `ACTION RW`.
