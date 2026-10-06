---
industry: education
region: Global
updated: 2026-10-06
---

# p432 — the from-scratch fixture gate

**Run this before you trust a licence instrument you just wrote. Four requests.**

## Why this exists

`compose/code/lib/license_family.sh` is the control for licence-family classification, and
`lib/probe_payload.sh` is the control for the loop around it. `lib/README.md` states the rule:
**source them, do not rewrite them.** The rule has now been broken three times:

| Pass | What was rewritten | Defect re-imported |
|---|---|---|
| 77 (2026-10-03) | the family classifier | P171 — GPL-3.0 §13 is *titled* "Use with the GNU Affero GPL", so every GPL-3.0 read as AGPL-3.0 |
| 15 (2026-10-06) | the probe loop | GPL-3.0 §6 contains "noncommercially", so four GPL/AGPL payloads read as CC/NonCommercial |
| **16 (2026-10-06)** | **both** | **four defects at once — see the table below** |

Pass 15 wrote: *"A third recurrence should be treated as evidence that documentation cannot
carry this and only tooling can."* Pass 16 is the third recurrence, and it adds the reason
the earlier diagnosis did not predict:

> 🔴 **The library was found, read and deliberately copied — and the environment refused to
> execute it.** Running the repository's own `*.sh` was denied as *"code from external"*.
>
> An architecture can be copied from prose. **Branch order cannot.** All four defects below are
> branch-order or anchoring bugs.

So the control is **environment-dependent**, and in an environment that will not run `lib/`,
this KB has documentation rather than a control — the exact state pass 15 said must not be
relied on.

## The fix this file is

A fixture list needs no interpreter, no sourcing and no trust: a human or an agent reads four
rows and checks four answers. Each row is a real repository chosen because it is the **only
kind of input on which a specific defect is visible**.

| Fixture | Expected | Catches |
|---|---|---|
| `openfun/richie` | **MIT** | substring match — `IMPLIED` ⊃ `mpl` (**P299**) |
| `inepdadosabertos/api` | **GPL-2.0** | preamble *mentions* the Lesser GPL (**P171**) |
| `fnshr/kyo-kan` | **CC0-1.0** | CC0 nested inside the CC-BY gate, unreachable |
| `espoon-voltti/evaka` | **UNCLASSIFIED** | a REUSE pointer accepted as a grant; no size floor |

**Coverage is the point, and it is pass 15's lesson restated:** an instrument validated only on
the family you care about scores 100% while broken. `richie` is a **required** case precisely
because MIT is the family everyone tests and the one the defect corrupts.

The fourth fixture's pass condition is **refusing to answer.** An instrument that names a
family for `evaka`'s 1,001-byte pointer is wrong even when it guesses `LGPL-2.1`, because it
read prose, not a grant.

## Usage

    python3 -I probe.py < <(cut -f1,2 fixtures.tsv | grep -v '^#')

`probe.py` is the instrument pass 16 actually used, **after** all four defects were fixed. It
emits TSV: `repo, branch, filename, bytes, family, holder`. It also carries two things the
bash library does not, both found in pass 16:

* **`DESCRIPTION` fallback** — R/CRAN packages keep a `YEAR`/`COPYRIGHT HOLDER` stub in
  `LICENSE` and the real grant in `DESCRIPTION`'s `License:` field (measured on
  `SidneyBissoli/educabR`: a 61-byte `LICENSE`, and the package is MIT).
* **`size_check()`** — the size floor, as a function rather than a remembered rule.

⚠️ **`probe.py` is not a replacement for `lib/`.** Where `lib/*.sh` can be executed, it is the
control and it is better tested (41/41). This is the portable fallback and the gate that
catches a fallback gone wrong.

## Two grant locations this gate does NOT cover

Found in pass 16, recorded so the next instrument plans for them:

* **REUSE / FSFE** (`espoon-voltti/evaka`) — grant in `LICENSES/<SPDX-ID>.txt` plus per-file
  SPDX headers. Spreading through EU public-sector code, which is exactly the population this
  KB tracks.
* **Odoo** (`JayVora-SerpentCS/OdooEduERP`) — grant in `<module>/__manifest__.py` as
  `"license": "AGPL-3"`. Top level is NO-PAYLOAD, so the platform reads as *unlicensed* while
  actually being **AGPL-3.0**. The expensive direction to be wrong in.
