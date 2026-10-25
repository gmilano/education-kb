# `p427` — a grant may carry two families CONJUNCTIVELY

## The specimen

`HyNuwa/UniMCP`, `LICENSE`, **`1 980` B `sha256₁₂ 727b864af003`**, read from a shallow
clone at HEAD **`2916cce7a726`** on **2026-10-25**:

```
MIT License

Copyright (c) 2026 MaxiFG
…
---------------------------------------------------------------------------

Portions of this software are derived from utn-mcp and remain under its
original license:

ISC License

Copyright (c) 2026 Joaquín Peñalva
…
```

Both grants are **live and simultaneous**. Nothing is chosen: MIT governs the work, ISC
governs the derived portions, and a distributor owes **both** notices.

🟢 **The payload names its own parent**, and `p427` verified that parent independently in
the same pass: `nialvape/utn-mcp`, **ISC**, `748` B `sha256₁₂ 2ad14eb14513`, © *Joaquín
Peñalva* — the same holder the ISC segment names. The lineage is **declared in the
grant**, which is the correctly-attributed form of the thing `p426`'s `T129` caught
undeclared.

## Why a new scope, rather than a bug report

Measured at `p427`, **nine** instruments on this base answer `MIT` on this payload and
**not one** reports the ISC segment. Six are family classifiers and are right within
their channel (`p198` `p306` `p228` `p211` `p191` `p419` → `MIT`). The other three are
purpose-built multi-grant readers, and each misses it **by construction**:

| instrument | its subject | on this payload |
|---|---|---|
| `p228.dual_grant` | a **CHOICE** — "available under either MIT or GPLv2" | `None` — the payload offers no choice |
| `p202.scope_reader` | a **PATH** — `skills/` AGPL-3.0, `app/` AGPL-only | `split_scope=False`, and it emits the `-----` separator as a spurious scope row |
| `p419.menciones_cruzadas` | copyleft parentage — needles `affero`, `lesser general public` | `[]` — a permissive-to-permissive cross-grant is outside its vocabulary |

So the taxonomy is **three** shapes, not two:

1. **DISJUNCTIVE** — two families, one chosen → `p228`
2. **PATH-SCOPED** — two families, split by directory → `p202`
3. **DERIVATION-SCOPED** — two families, split by provenance, no path named → **this gate**

## 🔴 The cost passes every tier check

Both families are permissive, so `commercial_use` is unaffected and **no licence gate on
this base goes red**. The defect is an **understated notice obligation**: the cell says
`MIT`, which owes one notice; the payload owes **two**, and the second is a named third
party's copyright. `notice_obligation()` returns that count, and it is the number the
shelf cell got wrong.

That is also why this is checked by **shape** rather than inferred from the tier verdict:
the tier verdict is correct and the obligation is still understated.

## 🔵 Both guards are load-bearing, and both were calibrated on a real payload

Stock **GPL-3.0** (`35 149` B, as carried by `EduardoKrausME/moodle-local_mcp`) defeats
the naive form of *both* detectors at once:

- it names `13. Use with the GNU Affero General Public License.` — a second family, in a
  title-shaped sentence, inside its own §13
- it contains `at your option` **twice** and `either` **ten** times

**Guard 1** — a family counts only as a **standalone title line** (the stripped line *is*
the title). The §13 sentence is prose; `ISC License` on its own line is not.
**Guard 2** — a CONJUNCTIVE verdict additionally requires a **scope sentence** (`portions
of`, `derived from`, `remain under`, …) in the six lines above the second title. Stock
GPL-3.0 contains **none** of those markers.

`C7`–`C10` hold stock GPL-3.0 out; `C20`–`C23` exercise each guard in isolation, including
the pair of payloads that differ **only** by the scope sentence and so land on opposite
verdicts.

🔵 **A third guard emerged from the holder channel.** A holder notice must carry a real
four-digit year. That one requirement excludes all three contaminants measured in these
payloads — MIT/ISC wrapped prose (`copyright notice and this permission notice appear…`),
GPL-3.0 clause text (§8 `copyright holder, and you cure…`), and the GPL-3.0 appendix
placeholder `Copyright (C) <year>  <name of author>` — rather than needing a case each.

## Run it

```
make gate-conjunctive-grant   # 24 controls, blocking, no network
make conjunctive-census       # the population arm; a measurement, never a failure
```

## Population, at this commit

**265** licence payloads committed to this base, **0** unreadable:

| mode | count |
|---|---|
| CONJUNCTIVE | **1** — this specimen |
| DISJUNCTIVE | 2 — `human-skill-tree`'s split notice (already registered by `p200`/`p202`) and this suite's synthetic control |
| SINGLE | 262 |

🔴 **One in 265 is not a trend.** The number is here so a successor can see whether the
class grows, and because `p427` found it in the **first ten addresses it read** — which
is a different statement about incidence than the corpus figure, and the two should not
be conflated.

## Fixtures

Every fixture but one is a payload read first-hand at a SHA on 2026-10-25. The single
synthetic is named `disjunctive-SYNTHETIC-elgg-shape.LICENSE` so it can never be
mistaken for a read; it reproduces the shape `p228` documents on `Elgg/Elgg`, because
`p427` read no disjunctive payload of its own and must not imply otherwise.
