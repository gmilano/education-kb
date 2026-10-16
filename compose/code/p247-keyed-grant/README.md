# `p247-keyed-grant` — the ENFORCEMENT axis, the WINDOWLESS name channel, and the PARAMETER-FILE state

`86` controls · `python3 -I test_keyed_grant.py` from any directory · wired into `make hooks`

## Why it exists

`ACTION XA` (p246) asked for one thing: fix the anchor ORDER in `lib/license_family.sh` so the
`BUSL` branch stops being dead code. p247 did that (`P1062`). **The discharge then falsified
its own sufficiency**, and this instrument is the half the order cannot reach.

Three real source-available payloads were read first-hand. They have **three different causes**
for the same `commercial_use_ok` → `ALLOWED`:

| cause | payload | the number that proves it | fixed by the hoist? |
|---|---|---|---|
| **ORDER** | `IAGA-TEAM/IAGA-Sentinel` — BSL 1.1, `4 913` B | name at offset `0`; the `Change License:` parameter names an OSI licence and every OSI anchor sat above the `BUSL` one | **yes** |
| **VOCABULARY** | `cockroachdb/cockroach` — CockroachDB Software License, `8 766` B | name at offset `0`, inside the window, and **no anchor in this base knows the string** | **no** |
| **WINDOW** | `redpanda-data/common-go` — Redpanda Community License, `27 204` B | own name at offset `2`; its real `Business Source License v.1.1` reference at offset **`4 969`** of `24 661`, beyond `osi_family_of`'s `4 000`-character truncation | **no** |

## The three questions it answers

### 1. `keyed_grant(text)` — is the permission tied to an artefact the licensor issues or monitors?

The `CockroachDB Software License` contains the word **"commercial" zero times**. It does not
restrict commercial use in words at all; it conditions the grant on artefacts —

> *"You will not operate the Software or a Modified Version **without a License Key** except
> for Limited Non-Production Use."*
> *"You will not circumvent, remove, disable, block or alter any technical countermeasures,
> Telemetry requirements …, License Key requirements, or other elements … designed to enforce
> the terms of this Agreement (collectively, the **"Protective Measures"**)."*

so every matcher that enumerates ways of saying "restricted" returns `ALLOWED` on it **by
construction** — the class `p241` named. `p241-blanket-denial` does not catch it either, and
correctly so: the CSL **does** grant something (`GRANT-PRESENT`, grants=1 denials=0). The grant
axis and the restriction axis are both blind to a grant that is real and **metered**.

So the question is POSITIVE, in the shape p241 prescribed. Four artefact kinds —
`LICENCE-KEY`, `TELEMETRY`, `COUNTERMEASURE`, `ENTITLEMENT` — each required to appear in a
sentence that also carries a **conditioning** cue. A definitions-only mention is not a
condition.

**The vocabulary is deliberately BROAD and paid for with shields, not omission.** It includes
the GNU spelling `authorization key`, so without a shield it would call the GPL a keyed grant:
`GPL-3.0`'s own text contains `authorization key` once, `Installation Information` four times
and `technological measures` twice. Both GNU contexts are the **inverse** of a keyed grant —
§6 compels the distributor to hand the keys over, §3 waives the licensor's anti-circumvention
power — so the shield is gated on those sentences' own words, and the real `gpl-3.0.txt` and
`agpl-3.0.txt` payloads are in the suite.

**It found its own false positive inside the same pass.** `microsoft/autogen`'s root `LICENSE`
is `CC-BY-4.0`, and its §2(a) *"You may not … apply any Effective Technological Measures"*
fired `COUNTERMEASURE`. Same waiver shape as GPL §3, so the fix was a new shield clause gated
on the CC wording — not an exception list — with that payload as a fixture.

### 2. `name_anywhere(text)` — windowless, per-name offsets

A **closed** list of source-available / proprietary licence names, each anchored on the full
multi-word name, never a bare acronym (`BSL` alone matches a statute, a bank and a bootloader).
Returns `(name, offset)` pairs in whitespace-squeezed coordinates — the same coordinates
`osi_family_of` truncates at `4 000` — so `offset >= 4000` says, as a number, that no anchor at
any position could have fired. **Per-name** and not a single `min()`, because `common-go`
carries its own name at `2` and a BSL reference at `4 969`, and a minimum would have hidden
exactly the finding.

It is a **signal, never a family stamp**: the family stays the shared classifier's to decide.

### 3. `parameter_file(text)` — is this payload the parameters rather than the grant?

Measured in the `ACTION XB` sweep: **`5` of the `6` `UNCLASSIFIED` payloads in the `821`-payload
MIT tier are `45`–`61` byte files containing only `YEAR:` and `COPYRIGHT HOLDER:`** — the CRAN
`License: MIT + file LICENSE` convention, verified first-hand on `rstudio/ggcheck`. **All five
shelf cells are CORRECT**, and a payload-only gate would have "corrected" five correct cells to
`UNCLASSIFIED`, the branch that falls to the token match. So the shape gets a NAMED state.

## The negative verdict is `NO-KEYED-CONDITION`, not `OPEN`

p241's lesson, applied to this file: the absence of this signal is not a permission. A reader
who wants a permission verdict must go and get one. This file refuses to be a default-permit
exit, and a control asserts that the string is never `OPEN`, `ALLOWED` or `PERMISSIVE`.

## Usage

```bash
python3 -I keyed_grant.py <payload-file> [...]   # TSV: verdict kinds names beyond_window reach
python3 -I keyed_grant.py --vocabulary           # print the probe lists (T272)
python3 -I test_keyed_grant.py                   # 86 controls, from any directory
```

`ACTION XE` (registered p247) asks for the name list and the windowless scan to be wired into
`lib/license_family.sh` itself — a WIRING task, since both already exist and are controlled
here. Its hazard is named in the register: a new family string that `commercial_use_ok` does not
list falls to that function's default arm, and the arm must be proven to DENY before any name is
added.
