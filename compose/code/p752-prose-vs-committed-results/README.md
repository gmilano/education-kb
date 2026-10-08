# `p752-prose-vs-committed-results` — the cheapest gate on this KB, and the last one built

Built pass 58 (2026-10-08). Asks one question before a pass publishes a licence
claim: **does this repository already hold a committed, machine-readable answer
that contradicts it?**

`./check_claim.sh --self-test` → **4/4 green**, offline, run from this directory.

## Why it exists (`P752`)

Pass 57 published that `openeducat/openeducat_erp` has **no locatable licence
grant**, filing it under *"Reference-to-nothing — the artefact exists and is
empty."*

At that moment this repository already contained, **committed**:

| Source already on disk | What it held |
|---|---|
| `p445-classifier-divergence/result.2026-10-07.tsv` | `openeducat/openeducat_erp  LICENSE  8241  LGPL  LGPL-3.0  YES  **AGREE**` |
| `p269-provider-release-matrix/licenses.2026-10-04.tsv` | the payload quoted verbatim — *"OpenEduCat is published under the GNU LESSER GENERAL PUBLIC LICENSE, Version 3"* → **`LGPL-3.0`** |
| 🔴 **`licence-grant-gate/README.md:116`** | 🔴 **`\| openeducat/openeducat_erp \| LGPL-3.0 \| 'information, please see the COPYRIGHT file' \|`** |
| `p206-erp-layer-license/result.2026-10-03.tsv` | `LGPL  LICENSE  8240  sha256:8f4ce028f93d` |
| `p436-fork-hypothesis/holder.2026-10-07.tsv` | `LGPL  LICENSE  8241` |
| `p637-cross-instrument-licence-agreement/README.md` | uses the repo as the **fixture** for the LGPL-3.0 version read |
| `README.md` (pass 53) | *"la única plataforma LGPL del estante de `verticals/solutions.md`"* |

Run the gate and it counts **31 committed TSV lines naming `LGPL`** for that
slug (`evidence.openeducat.2026-10-08.txt`).

**The third row is the one that matters.** `licence-grant-gate` had already
recorded the *exact* `COPYRIGHT`-reference trap — the literal string
`information, please see the COPYRIGHT file` — **in the same table row as the
correct verdict `LGPL-3.0`**. The trap pass 57 fell into was not merely
knowable; it was documented and solved in this repository, by name, in a file
whose whole purpose is grant adjudication.

## What class of defect this is, and why it is different from `P725`–`P751`

Every other licence defect this KB has found needed **a better probe**: a
filename list (`P727`), a title window (`P726`), a registry identity step
(`P743`), an endpoint rather than a host (`P745`).

This one needed **a `grep` of files already on disk.** No network, no oracle, no
sweep. Pass 57 ran a 1 020-repo sweep across `raw.githubusercontent.com` and
published a result its own committed data contradicted 31 times over.

> **`P752`.** *This KB's failure mode has shifted. It is no longer
> under-measuring the world — pass 57's sweep was a genuine instrument and its
> census holds. It is now **under-reading itself**: the prose shelf regressed
> against the data shelf, and **nothing checked prose against committed
> results**. The data shelf has grown faster than any pass's ability to recall
> it, and at 138 instrument directories, recall is no longer a thing a pass can
> do from memory.*

## Scope, and why the `P744` constraint does not reach it

This instrument reads **only local committed files**. It enumerates nothing on
the network, so the bulk-enumeration denial that makes `Gap 273`'s full sweep
unperformable here (`P744`) does not apply. That is the sharpest irony
available: **the one verification layer this environment permits without
reservation is the one layer nobody had built.**

## Usage

```sh
./check_claim.sh owner/repo              # print every committed verdict held
./check_claim.sh owner/repo UNGRANTED    # exit 1 if the KB contradicts you
./check_claim.sh --self-test             # 4/4
```

Exit codes: `0` no contradiction · `1` **CONTRADICTION** or **DIVERGENCE** · `2`
usage.

Verdict classes:

- **`CONTRADICTION`** — you assert ungranted, committed data holds a family.
  This is the pass-57 shape and it is an error, not a judgement call.
- **`DIVERGENCE`** — you assert family *X*, committed data mostly says *Y*. Not
  necessarily wrong: a relicence (`P725b`) or a version read can explain it.
  **Say which, in the pass, rather than leaving the shelves disagreeing.**
- **`NO_PRIOR_EVIDENCE`** — the KB holds nothing; your measurement stands alone.

## Where it belongs in the pre-flight

**Step 0 of `P751`** — before the 19 filenames, before the title window, before
the registry. It is the only step that costs nothing and the only one that
catches an error the network cannot.

## Declared limits

- It matches families named **on the same line** as the slug in committed TSVs,
  so a column layout that separates them would be missed. The eight shelves'
  instruments happen to be line-oriented; a later pass changing that must
  revisit this.
- It cannot distinguish a **stale** committed verdict from a current one. A
  relicence makes the gate cry `DIVERGENCE` correctly and for the wrong reason —
  which is why `DIVERGENCE` asks for an explanation rather than a correction.
- `GPL` appears twice in the `openeducat` tally against `LGPL`'s 31: LGPL-3.0
  incorporates the GPL text by reference (LGPL §4), so substring overlap is
  expected. The gate reports the distribution rather than a single answer for
  exactly this reason.
