---
industry: education
region: Global
updated: 2026-10-07
---

# `p459-unified-verdict` — one verdict from both classifiers, and the layer below the root

**P459: a shelf consulted by two classifiers needs one verdict function, and the layer
below the root is where nobody had looked with both.**

Pass 27 established that this KB has two licence classifiers and that **neither is a
superset of the other**. Pass 28 taught each the other's axis (`P453`–`P457`) and then
asked the question that remains: the 412 **roots** were re-measured, but every payload
**below** a root had been classified by `sweep_payload.family_of` alone — by `p441`'s
tree enumeration and `p444`'s root-vs-tree comparison, both of which call it and only it.

## The pre-registered prediction, and its falsification

> 🔴 *"Expect the **tree** payloads to carry **more** NC than the roots do, because a
> `docs/`, `data/` or `assets/` grant is where CC-BY-NC lives by convention. Prediction:
> **at least 3** further NonCommercial grants below the root, none of them currently
> flagged."*

🔴 **Falsified. There are ZERO NonCommercial grants below the root.**

| Layer | n | ALLOWED | PROHIBITED | UNDETERMINED |
|---|---|---|---|---|
| root | 412 | 394 | **11** | 7 |
| tree | 76 | 65 | **0** | 11 |

The reasoning behind the prediction was sound and the convention it named is real — it
simply is not in this corpus. The 76 tree payloads are where a project puts the grant for
a vendored dependency, not where it puts a content licence: 18 MIT, 15 Apache-2.0, 6
ECL-2.0, 4 GPL-2.0, 3 MPL-2.0, 3 CC-BY-4.0 (all four-clause-free), 4 EUPL.

🟢 **The root count, 11, matches `lib/license_family.sh`'s own independent count of
commercial-use-prohibited payloads exactly** — an unplanned cross-check of the
composition against the axis it composes.

## Two defects this instrument committed, both caught by its own suite or its own output

🔴 **1 — the negative went AFTER the gate, and that hid three rows.** The first cut asked
`if family == "UNDETERMINED"` first and answered `UNDETERMINED`, which suppressed three
root payloads whose family neither classifier can name and whose **text forbids commercial
use**: `AStheTECH/mewcp-google-classroom`, `Khan/tutoring-accuracy-dataset`,
`leemonade/leemons`. The symptom was visible in the output — `PROHIBITED` came out **8**
when the shell's own axis says **11**.

It is `P299`'s lesson committed *inside* a function written to compose the fix for it:
family and commercial use are **independent axes** (`P250`), so an unnameable family still
carries whatever its text restricts. *"We could not name this licence"* must never
overwrite *"this licence forbids what you want to do with it."*

🔴 **2 — `P460`: a markup container defeats the title rule, and that opens the token-match
path.** The only thing the tree sweep flagged was `OS4ED/openSIS-Classic` and
`OS4ED/openSIS-Responsive-Design`, both shipping the same 61,575-byte `docs/LICENSE.rtf`,
both reported commercial-use **PROHIBITED**. It is a **false positive** with three sound
links:

1. the payload is RTF, so its first two non-blank lines are `{\rtf1\adeflang1025\ansi…`
   and a font table — **the title block is markup**;
2. with no readable title every family probe declines, so the family is `UNCLASSIFIED`;
3. `P250`'s gate only short-circuits an **identified** family, so an `UNCLASSIFIED` one
   falls through to the token match over the body — and the body is GPL-2.0, whose
   **section 3(c)** reads *"this alternative is allowed only for noncommercial
   distribution"*.

⚠️ That phrase is a **condition on one distribution option**, not a restriction on the
licensee — which is exactly what `P250`'s own header already says about *"occasionally and
noncommercially"* in GPL-3.0 section 6. **The guarantee was in place; the container walked
around it.**

🟢 **Verified first-hand:** the same two repositories carry `docs/License.txt`, 17,286
bytes, opening on a plain `GNU GENERAL PUBLIC LICENSE / Version 2, June 1991`. The licence
is **GPL-2.0** and commercial use is **ALLOWED**, so the false positive cost an opportunity
on a real SIS platform rather than inventing a permission.

The fix **declines rather than guesses**: de-marking RTF well enough to recover a title
means parsing a font table, and a half-parsed container would reopen the very token-match
path this closes.

## 🔴 The finding worth more than the prediction was

`OS4ED/openSIS-Classic` and `OS4ED/openSIS-Responsive-Design` **have no root licence
payload at all** — they are absent from the 412, and `p441` files them
`OWN-GRANT-IN-SUBTREE`. **For these two the subtree is the only licence evidence that
exists.** And the family `p441` published for them was `LGPL?` — wrong, caused by `P459`,
and corrected by this pass to **GPL-2.0**.

So the tree layer carried no NonCommercial surprise, but it carried something the root
sweep structurally cannot: **the only grant two real platforms have, read wrong.**

## The verdict function

| Axis | Rule | Why |
|---|---|---|
| `family` | the **fine** classifier (shell) wins wherever it names one; the coarse one is the fallback | not because it is better — because neither is a superset (`P445`), so **declining** is the only safe reason to defer |
| `commercial` | **ALLOWED only if both sides allow it**, and the restriction is tested **before** the family gate | for a billable deliverable, one classifier saying *"you may not sell this"* is enough to stop |

Every row where the two sides disagree is **counted and printed**, never silently resolved.

## Run it

```bash
python3 test_unified.py                                    # 30/30, no network
python3 unified.py ../p444-root-vs-tree-family/payloads.licensed.2026-10-07.tsv \
                   treepaths.input.2026-10-07.tsv > result.2026-10-07.tsv
```

`treepaths.input.2026-10-07.tsv` is the union of every path `p441` and `p444` actually
read — `own_extra_paths` from `p444`, `confirmed_paths` and `rejected_paths` from `p441`:
**76 payloads across 48 slugs.**
