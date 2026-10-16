# `p246-payload-integrity` — ROLE and STATE, asked before any family verdict is trusted

Pass `246`, `2026-10-16`. `60` controls, wired into `make hooks`.

Two questions no instrument on these shelves asked until this pass:

1. **ROLE** — is the licence name the classifier matched the licence that *governs* this payload,
   or a licence named in a **parameter**, applying later or elsewhere?
2. **STATE** — is this payload **one resolved grant**, or an unresolved merge of two?

## Why it exists

### The ROLE finding — the `BUSL` branch is dead code by construction

`lib/license_family.sh::family_of` answered `Apache-2.0` on
[`IAGA-TEAM/IAGA-Sentinel`](https://github.com/IAGA-TEAM/IAGA-Sentinel) (`196`★, `4 913` B), and
`commercial_use_ok` then answered **ALLOWED**. The payload is **Business Source License 1.1** —
source-available, not OSI — whose `Additional Use Grant` forbids offering the work *"to third
parties as a hosted or managed service"*, with a `Change Date` of **`2030-05-03`**.

The classifier is **not** missing a `BUSL` branch. It has one, at line `646`, and it is
unreachable: `BSL 1.1` carries a **mandatory** `Change License:` parameter naming the licence the
work converts to, and every OSI anchor sits above it —

```
EUPL 154 · MPL 244 · EPL 253 · GPL/AGPL/LGPL 313-371 · Apache 378 · BSD 459 · MIT 503
CC 565 · ................................................... BUSL 646   <- never reached
```

Measured both ways, so the claim is not Apache-specific:

```
Change License: Apache License, Version 2.0        -> family_of = Apache-2.0   ALLOWED
Change License: GNU General Public License, v2.0+  -> family_of = GPL-2.0      ALLOWED
```

> **The class: a licence name in a PARAMETER position is not this payload's grant.**
> `Change License` names the grant this work does *not* carry yet. Same family of defect as
> `p240` (language), `p241` (absence of restriction vocabulary) and `P250`/`P312`
> (family-implies-commercial): *a matcher that reads a token and never asks what role the token
> plays in the document.*

Blast radius, measured: **`0` of `308`** carried `Apache-2.0` payloads re-read first-hand contain
the string `Business Source License`. No published row flips. See **`ACTION XA`** for the fix to
the shared classifier's ordering — this instrument is the gate, not the repair.

### The STATE finding — a `LICENSE` containing an unresolved merge conflict

[`0xnavarro/IA-PARA-TODOS`](https://github.com/0xnavarro/IA-PARA-TODOS) ships a root `LICENSE` of
`11 471` B whose appendix is an unresolved `git` conflict carrying **both** holder forms:

```
<<<<<<< HEAD
   Copyright 2024 0xnavarro - IA-PARA-TODOS      <- the real holder
=======
   Copyright [yyyy] [name of copyright owner]    <- the untouched ASF template
>>>>>>> 32db549aa17acfc812d4175d983a95945a02b728
```

`p245-apache-canonical` grades it **`CANONICAL`** (title, grant sentence and all three deviation
anchors are intact — the conflict is *after* the terms). `holder_of` answers **`NOT-APPLICABLE`**
on a payload that plainly carries a holder: that is `p241`'s own fix inverted, because `p241`
taught `holder_of` to exclude the ASF template-bracket form and a conflicted payload contains the
template form *and* the real form at once.

Attribution is exactly what `Apache-2.0` §4 obliges a redistributor to preserve, and this payload
does not say whom to attribute. Base rate: **`1` of `321`** payloads read first-hand this pass.

## Interface

```python
conflicted(text)              -> bool      # requires BOTH an opening and a closing marker
conflict_sides(text)          -> int       # hunk count, 0 when resolved
holder_ambiguous(text)        -> bool      # real holder AND ASF template both present
parameter_roles(text)         -> [(label, value)]   # change-license, change-date, alternative-licence
governing_family(text)        -> "BUSL"|"Elastic"|"PolyForm"|"SSPL"|"CAL"|None
names_but_does_not_grant(text)-> [licence names mentioned but not granted]
verdict(text)                 -> "EMPTY" | "CONFLICTED:hunks=N[;holder-ambiguous]"
                                 | "SOURCE-AVAILABLE:<fam>[;names-but-does-not-grant=...]"
                                 | "SINGLE-RESOLVED-GRANT"
```

`CONFLICTED` outranks the role axis: a payload that is two payloads has no single grant for
anything downstream to read.

`governing_family()` returns `None` for every real OSI payload — this instrument then **defers to
`lib/license_family.sh`**, which remains the family authority. `P237`'s rule is kept: there is no
family classifier in this file.

## Running it

```bash
make hooks                                                        # 60 controls, offline
python3 -I compose/code/p246-payload-integrity/test_payload_integrity.py
python3 -I compose/code/p246-payload-integrity/payload_integrity.py <payload-file> [...]
```

Runs from any cwd (`p355-cwd-portability`): the module is loaded by path, never by `import`,
because `python3 -I` strips the script directory from `sys.path`.

## Fixtures

Every fixture is a real payload read first-hand from `raw.githubusercontent.com` on `2026-10-16`,
at the branch `git ls-remote --symref` reported, with its `HEAD` pinned — no synthetic strings
except the three marker-discipline controls and the `GPL` change-licence variant, which are
derived from a real payload by one documented substitution.

| fixture | slug | ref | bytes |
|---|---|---|---|
| `ia-para-todos.conflicted-apache.txt` | `0xnavarro/IA-PARA-TODOS` | `main` | `11 471` |
| `iaga-sentinel.busl-1.1.txt` | `IAGA-TEAM/IAGA-Sentinel` | `main` | `4 913` |
| `mvps-cenia.apache-one-deviation.txt` | `CENIA-DEV/mvps-cenia` | `main` | `11 361` |
| `euconform.mit.txt` | `Hiepler/EuConform` | `main` | `1 073` |
| `opensalt.mit-published-apache.txt` | `opensalt/opensalt` | `develop` | `1 080` |
| `ifes-academico.gpl3-published-apache.txt` | `MuriloCalegari/Ifes-Academico` | `QAcad` | `35 149` |
| `govllm.eupl-1.2.txt` | `JehanneDussert/govllm` | `main` | `13 599` |
| `apache-2.0.canonical.txt` | apache.org | — | `11 358` |

The last two `ref` values are the point of the `p229` ref axis: `opensalt` and `Ifes-Academico`
answer `404` at all `40` paths on a `main|master` guess, and both carry a licence cell that was
wrong on these shelves until this pass read them at `develop` and `QAcad`.
