# `p441` — `Gap 440-A` bought, and its prescription refuted in the buying

**2026-10-25.** `Gap 440-A` asked for a **variant-aware BSD profile**, with the variant
*"resolved from the clause structure, not from the length"*, and named one published row as
the reason: [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE)
is shelved **BSD-3-Clause** on `agents/top.md` and was unscreened by the screening rule.

Both halves of that framing turned out to be wrong, and the measurements are below.

## 1. The structural resolver is unsound, and the asymmetry is why

BSD-2 and BSD-3 are separated by exactly one piece of text — the non-endorsement clause —
and that clause is also one the instrument **grades**. Resolve the variant from it and a
**BSD-3 payload truncated at that clause** resolves as a BSD-2, is graded against BSD-2's
profile, and returns 🔴 `GRANT-PRESENT`: a false pass on precisely the shape the instrument
exists to catch. `C26` keeps that reproducible — `C26g` asserts the payload really is
complete under BSD-2's profile, so the defect cannot be quietly dropped.

🟢 **What is sound is the asymmetry.** *Presence* of the discriminator is proof (no lesser
variant contains it); *absence* is ambiguous between "a complete BSD-2" and "a BSD-3 cut
short". So `resolve_bsd_variant()` reads the payload's own **declaration** first — the
title line, the only BSD signal independent of the graded clauses and the analogue of GPL's
`version 3` — lets the structural arm answer **only** in the direction that cannot be
wrong, and declines everywhere else (`P250`).

The byte half of the gap was right and is kept: the 11 BSD payloads on this tree span
**164 B → 2 058 B**, so no single floor separates a truncated BSD-3 from a valid BSD-0.

## 2. The row the gap named is UNTITLED, so a BSD profile could never have reached it

| population | measured |
|---|---|
| live BSD rows this base publishes | **12 payloads across 11 repositories**, probed first-hand this hour |
| of those, **no title line at all** | 🔴 **5** — `Open-TutorAi/open-tutor-ai-CE` (1 531 B), `jupyter/nbgrader` (1 512 B), `jupyterhub/jupyterhub` (1 475 B), `open-webui/open-webui` (2 819 B), `ucbds-infra/ottr`'s 108 B stub. Four of the five are **complete BSD-3 grants** |
| `GRANT-PRESENT` after this pass | 🟢 **11 of 12** |

`bespoke_census.titled_family()` answers from the **title**, by construction, so all five
return `None` and `grant_presence` never reaches a clause. 🟢 The remedy is not a second
family classifier here — `P171` gives that question a hardened owner, `lib/license_family.sh`,
which answered `BSD` for all five the same hour — it is `--family`, which lets that owner's
answer be passed in. `C27e`/`C27f` exercise it **through `main()`**, because mutation testing
showed `C27c` alone did not: deleting the whole `--family` limb left 82 of 82 controls green.

## 3. `Gap 440-A`'s denominator was 27 % high

It enumerated *"BSD 14"*. Three of those 14 are **KB markdown tables** that name a licence
in a cell (`md-form4-italic.md`, `md-shortname-binding.md`, `md-page-said-header.md`) — not
licence payloads. The real figure was **11**. They are named in `grade_bsd.py`, not filtered
by a byte floor, and they still grade `GRANT-UNCALIBRATED`, which is the right answer for a
table.

## 4. Two defects in this pass's own instruments, recorded rather than quietly fixed

1. 🔴 **`probe_bsd_shelves.sh` reported `NO-PAYLOAD` for all eleven repositories** on its
   first run, while a bare `curl` returned `200` and 1 516 B in the same shell. The cause
   was mine: it restored `set -u` after sourcing `lib/probe_payload.sh`, which uses unset
   variables by design and says so in its own header. A nil reads exactly like coverage —
   eleven rows of *"this base sells licences it cannot reach"* — and nothing in the output
   said the option was the reason. The option now stays off for the **calls**, with the
   measurement written into the file.
2. 🔴 **I over-accused this base's own shelf before checking its evidence store.** The probe
   returned `ucbds-infra/ottr` → `LICENSE`, **108 B**, `UNCLASSIFIED` — an R
   `YEAR:` / `COPYRIGHT HOLDER:` stub — against a published row reading *"BSD-3-Clause
   (1,555 B, `1677c5307530`)"*, and my first reading was that the row did not reproduce.
   🟢 **The row is right.** `evidence/verified-repos.2026-10-22-p394.tsv:13` records exactly
   this shape, enumerated from the tree per `Gap 393-F`: `LICENSE.md` (text) **+** `LICENSE`
   (108 B stub) **+** `DESCRIPTION: BSD_3_clause + file LICENSE`. `LICENSE.md` re-read at the
   pinned commit `693b3df` this hour is **1 555 B · `1677c5307530`** — the recorded digest,
   to the byte.

   🔵 What the episode actually found is in the probe, not the shelf: **`lib/probe_payload.sh`
   takes the FIRST filename-ladder hit**, and on an R-convention repository that is the stub
   while the grant sits one spelling away. `Gap 393-F`'s rule — enumerate the tree, never
   guess filenames — is implemented in `p394`'s evidence run and **not in the shared
   library**, so every pass that sources the library inherits the guess. Registered as
   `Gap 441-A`.

## 5. Scope boundary, stated as a control

[`open-webui/open-webui`](https://github.com/open-webui/open-webui) is stock BSD-3 **plus** a
branding restriction and a Contributor Licence Agreement, and it grades `GRANT-PRESENT`
because every clause really is present. **`GRANT-PRESENT` is not `GRANT-UNMODIFIED`.** This
instrument answers *is the grant here*; the addition axis is `Gap 438-A` / `Gap 439-A`, and
`agents/top.md` carries that warning by hand. `C30` pins it so the boundary is visible to
the next reader instead of being rediscovered.

## Files

| file | what it is |
|---|---|
| `probe_bsd_shelves.sh` | the live probe, sourcing the shared loop. TSV → `probe.2026-10-25.tsv` |
| `grade_bsd.py` | the measurement target, both populations. **Always exits 0** (`Gap 435-A`) → `make bsd-variant-census` |
| `grade.2026-10-25.tsv` | this hour's run |
| `payloads/` | every payload graded, as fetched |

The code is in `../p439-grant-presence/grant_presence.py` (profiles `BSD-2`, `BSD-3`,
`resolve_bsd_variant`, `VARIANT_FAMILIES`, `--family`) and the controls — **87, up from
46** — in `../p439-grant-presence/test_grant_presence.py` (`C23`–`C34`).

## Mutation testing

A control that cannot fail is not a control, so each arm was removed and the suite re-run:

| mutation | controls that go red |
|---|---|
| resolve the variant from the clause structure (**what the gap prescribed**) | **8** |
| one undifferentiated `BSD` profile | 2 (`C24`, `C26g`) |
| drop the reversed declaration word order | 3 (`C29c`, `C29e`, `C29f`) |
| drop the `--family` limb | 1 (`C27f`) — **0 before `C27e`/`C27f` were added** |
| key the discriminator on the licence NAME instead of the clause (`P171`'s shape) | 5 |
