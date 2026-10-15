# p217 — `ACTION QL` root cause: the gate is monolingual, the corpus is not

## What this measures

`ACTION QL` requires that the shelves be grepped for a token, slug or family **before** an action
may be registered on a claim that it is missing. `ACTION QN` was registered on the claim that
`README` prose is *"the last unread channel"* on the ungranted population.

That claim is false, and the refutation is a line in this KB's own append-only history:

> `agents/trending.md` l.`19972` — `pase 126`, `2026-10-05`
>
> | [`alfredang/AI-LMS-TMS`] | 19 | 10 rutas + README | 🔴 **PROPIETARIO EXPLÍCITO** — README:
> *«proprietary software developed by Tertiary Infotech Pte Ltd. All rights reserved.»*

The channel was read `91` passes ago and the answer recorded. The row still travelled through
p211's `ABSENT` census, p215's recovery sweep and p216's remainder arithmetic as an unknown.

## Why the gate missed it

**It is in Spanish.** This KB's early history — through roughly `pase 126` — is written in
Spanish, and every propagation instrument it has built since (`ACTION QL`'s grep,
`qg_gate2.py`'s token table) matches English.

Measured over the `8` client-facing shelves
(`evidence/shelf-language-census.2026-10-15-p217.tsv`):

| token | lang | matching lines |
|---|---|---|
| `licencia` | ES | **`1 087`** |
| `barrido` | ES | `441` |
| `lectura` | ES | `227` |
| `sin licencia` | ES | `130` |
| `compuerta` | ES | `76` |
| `PROPIETARIO` | ES | `31` |
| `license` | EN | `4 257` |
| `no licence` | EN | `566` |

A gate grepping `no licence` and `proprietary` cannot see `sin licencia` or `PROPIETARIO`, and
there are `161` lines of exactly those two.

## The fix

A token table, in `tokens.py`. One concept per row; any member counts as a hit. `8` concepts, one
`grep` each, entirely offline, over files already on disk. Full recipe at `compose/patterns.md`
`P217-B`.

Run it as `ACTION QL`'s precondition. Had it run on `QN`, `QN` would have been registered on the
narrower and true claim — *"prose was read for `1` row at `pase 126`; the other `66` are
unread"* — and p217 would have started from the right place.

## Precedent this generalises

`agents/trending.md` l.`20019` registers `P421`: *«la señal NO-OSI puede no estar en inglés»* — a
Chinese-language proprietary EULA on `yuanjiusheng/cloud-learning-ce`
(`版权所有 … 保留所有权利`) that an English title list would pass as unlicensed.

So this KB diagnosed the language axis for the repositories it **reads**, and never turned the
same instrument on its **own shelves**. `P217-B` is `P421` pointed inward, and it is the more
expensive of the two, because the shelves are what the register greps.

`REFUSAL` in `P217-A`'s `grant_state()` carries the Spanish and Chinese forms for the same reason.
