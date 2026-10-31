---
industry: education
region: Global
updated: 2026-10-31
---

## 🆕 `p561` — `2026-10-31` — **🟢 `560-C` CLOSED, AND IT CLOSES BY RETIRING THE INSTRUMENT IT ASKED FOR: canonical digests are now pinned for **five** families from **14 sources** — but 🔴 **a byte digest is the wrong gate in four of the five**, and the proof is that the **stage at which a family's sources converge under normalisation is what classifies the family**. 🟢 Apache-2.0 converges at `ws` **3 of 3**; GPL-3.0 at `punct` **3 of 3**; 🔴 AGPL-3.0 **never converges** and its residual is edX Inc.'s RPC clause; 🔴 LGPL-3.0 never converges and its residual is a **form**; 🔴 BSD-3-Clause is **3 of 3 distinct at every stage** — no canonical digest exists. 🔴 **Stage 4 rejected by its own data.****

🟢 **`560-C` asked for:** *"pin canonical digests for the other families this shelf grades
against — AGPL-3.0, GPL-3.0, MIT, CC0, BSD-3 — each from two independent sources, since one
source is how `559-C` got it wrong."* 🟢 **Done, at three sources where three exist**, and the
answer is better than the question: two sources are not enough to *pin* a digest, because for
four of five families the two sources **legitimately disagree**.

Instrument committed at
[`../compose/code/p561-grant-normaliser/`](../compose/code/p561-grant-normaliser/README.md);
full census at
[`../evidence/canonical-grant-normalisation.2026-10-30-p561.tsv`](../evidence/canonical-grant-normalisation.2026-10-30-p561.tsv).

### 🟢 `561-A` — the pin table, by convergence stage

🔵 **Four stages.** `raw` = the bytes (`560-A`'s adopted convention). `ws` = every whitespace run
collapsed to one space, stripped — dissolves **reflow**. `punct` = curly quotes and dashes folded to
ASCII, `©`→`(C)`, `fsf.org`/`gnu.org` URL schemes normalised — dissolves **typography**.
`case` = lowercased.

| family | sources | distinct `raw` | distinct `ws` | distinct `punct` | 🟢 **canonical pin** | class |
| --- | :-: | :-: | :-: | :-: | --- | --- |
| 🟢 **Apache-2.0** | 3 | 2 | 🟢 **1** | 1 | **`0ffddef9e48f`** · `ws` · **10 221 B** | **A** reflow-equivalent |
| 🟢 **GPL-3.0** | 3 | 3 | 2 | 🟢 **1** | **`cd83b5f465e5`** · `punct` | **A** typographic |
| 🔴 **AGPL-3.0** | 3 | 3 | 2 | 🔴 **2** | **`2cd0fb7883a3`** · `punct` · *2 of 3 sources* | **D** one source **modified** |
| 🔴 **LGPL-3.0** | 2 | 2 | 2 | 🔴 **2** | **two pins, by form** — see `561-C` | **B** multi-form |
| 🔴 **BSD-3-Clause** | 3 | 3 | 3 | 🔴 **3** | 🔴 **none exists** | **C** filled template |

🟢 **Apache-2.0 is settled, and by a third source.** `apache.org` **11 358 B** `cfc7749b96f6`,
[`oppia/oppia`](https://github.com/oppia/oppia) `develop/LICENSE` **11 358 B** `cfc7749b96f6`
(byte-identical, independently), and SPDX **10 280 B** `074e6e32c86a` — 🟢 **all three collapse to
`0ffddef9e48f` at `ws`.** 🔴 **The 1 078 B SPDX delta is whitespace, nothing else.** 🔵 Worth
stating plainly because this pass's own first hypothesis was that the delta was the *appendix*
(`560-D`'s territory) and 🔴 **that hypothesis was wrong** — measurement, not inference, settled it.
🟢 `560-C`'s re-pin of `11 358` / `cfc7749b96f6` at `raw` **holds, now at three sources**.

🟢 **GPL-3.0 needed stage 3, and the mechanism is punctuation.** SPDX ships
`“ ”`, `©` and `https://fsf.org/`; the repositories ship `" "`, `(C)` and `http://fsf.org/`.
A sentence-level diff of the normalised texts returns **232 → 232 units with zero sentences added
or removed** — the entire `ws`-stage disagreement is character-width.

| source | `raw` B | `sha256/12` `raw` | `ws` B | `punct` |
| --- | --- | --- | --- | --- |
| 🟢 [`moodle/moodle`](https://github.com/moodle/moodle) `main/COPYING.txt` | **35 147** | `8ceb4b9ee5ad` | 34 281 | 🟢 `cd83b5f465e5` |
| 🟢 [`h5p/h5p-php-library`](https://github.com/h5p/h5p-php-library) `master/LICENSE.txt` | **35 146** | `c53a65c2fd56` | 34 281 | 🟢 `cd83b5f465e5` |
| 🟢 SPDX `GPL-3.0-only.txt` | 34 674 | `fb981668c18a` | 34 448 | 🟢 `cd83b5f465e5` |

🟢 **And this dissolves a `560-A` artefact at last.** Moodle and h5p differ by **exactly 1 raw
byte** — the trailing newline that `559-A` pinned a whole convention around. 🟢 **At `ws` they are
the same number (34 281) and at `punct` the same digest.** 🔵 `560-A`'s labelling rule stays
(publish `raw`, name the convention); 🟢 **but the convention question stops being load-bearing the
moment the comparison is normalised.**

### 🔴 `561-B` — AGPL-3.0 does not converge, and that is the instrument working

🔴 **Three sources, three raw figures, and *two* that survive every stage.** SPDX **34 020 B**
`d8a6cc31abc1` and [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms)
`master/LICENSE` **34 520 B** `57c8ff33c9c0` 🟢 **collapse together** at `ws` (33 687 B
`0a7e77a9ebe3`) — so canvas-lms ships **stock AGPL-3.0, differently wrapped**.
🔴 [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) `master/LICENSE`
**35 136 B** `e12d78569742` does **not**: `ws` **34 302 B** `186d8f7758cb`, `punct`
`de41de5bdd96`. 🔴 **A residual of +615 `ws` bytes that no stage removes.**

🟢 **A sentence-level diff names it — three units, all added, all operative:**

| # | added text (abridged) |
| --- | --- |
| 1 | `edX Inc.` |
| 2 | *"wishes to state, in clarification of the above license terms, that any public, independently available web service offered over the network and communicating with edX's copyrighted works by any form of inter-service communication, including but not limited to Remote Procedure Call (RPC) interfaces,"* |
| 3 | *"\"Corresponding Source\" of this work … do not include source code files for programs used solely to provide those public, independently available web services."* |

🟢 **This base already held the clause** — `repos/trending.md` carries *"+616-byte edX Inc. RPC
scope clarification"*. 🟢 **It is the same fact, and the two numbers now reconcile under `560-A`:**
**+616** is `raw` against canvas-lms (35 136 − 34 520); **+615** is `ws` against the canonical
(34 302 − 33 687). 🔵 Neither was wrong; **neither was labelled**, which is precisely the defect
`560-A` registered.

🟢 **Why this is the pass's load-bearing result.** Five families went through the same four stages
blind. 🟢 **Four converged or failed for *formatting* reasons; exactly one failed for a *clause*,
and it is the one clause on this shelf that changes a delivery obligation.** 🔵 The instrument was
not told which family to flag — **its failure to converge is the signal**, and the signal landed on
the right row. That is a negative control this base did not have before.

### 🔴 `561-C` — LGPL-3.0 has two legitimate forms, and normalisation cannot reconcile them

| source | `raw` B | `ws` B | `punct` | what it is |
| --- | --- | --- | --- | --- |
| 🟢 [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) `v4.0.x-develop/LICENSE` | **7 652** | **7 317** | `690578875bea` | 🟢 **rider-only** — the GNU-published shape, which *incorporates* GPL-3.0 by reference |
| 🟢 SPDX `LGPL-3.0-only.txt` | **42 098** | **41 761** | `05e49932344e` | 🟢 **rider + GPL-3.0 concatenated** |

🔴 **5.7× apart at every stage**, and both are correct. Their first lines are the same instrument
(`GNU LESSER GENERAL PUBLIC LICENSE / Version 3, 29 June 2007`); 🟢 the difference is whether the
publisher inlined the GPL text it points at. 🔴 **So for LGPL-3.0 the pin must name the form**, and
a scanner that holds one form will report `NOASSERTION` on the other.

🔵 **This is not academic for this shelf.** `odoo` and `openeducat_erp` are `LGPL-3.0-only` — the
two ERP bases `557`'s gap-closure moved out of `BLOCK` — and BigBlueButton is the shelf's
conferencing row. 🟢 All three are gradeable; 🔴 **none of them against a single digest.**

### 🔴 `561-D` — BSD-3-Clause has no canonical digest, by construction

| source | `raw` B | `ws` B | `punct` |
| --- | --- | --- | --- |
| SPDX `BSD-3-Clause.txt` | 1 460 | 1 453 | `65e7987f847f` |
| [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) `main/LICENSE` | **1 512** | 1 492 | `1aa7d784220b` |
| [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) `main/LICENSE` | **1 475** | 1 469 | `33df044acb3a` |

🔴 **3 distinct at `raw`, 3 at `ws`, 3 at `punct`.** The template carries `<year>` and `<owner>`
placeholders that every project fills differently, 🟢 **so there is nothing to pin and no amount of
normalisation creates one.** 🟢 `560-C`'s own parenthesis about MIT — *"which has no single
canonical form, so the existing fold constant is the right instrument there"* — 🟢 **generalises to
BSD-3-Clause, now measured rather than assumed.** 🔵 Both are **class C**: fold-constant families.

### 🔴 `561-E` — stage 4 is rejected, by this pass's own data

🔴 **Case folding earned nothing.** It reduced **no** family's distinct-digest count below stage 3
(Apache 1→1, GPL 1→1, AGPL 2→2, LGPL 2→2, BSD-3 3→3), 🔴 **and it destroys the one typographic
signal that carries legal meaning** — capitalisation is how these instruments mark a defined term,
so `"This License"` and `this license` must not hash alike. 🟢 **Stage 4 stays in the committed
instrument so the negative result reproduces, and is not used for grading.** 🔵 Recorded here
rather than quietly dropped, because a four-stage instrument whose fourth stage is inert is a
finding about the instrument.

### 🟢 Reproduction — 10 of 10 raw figures match the shelf

🟢 **Ten grants were read first-hand this pass, through branch resolution and status gating, with
no reference to what this base already held.** 🟢 **Every `raw` byte count and digest that the
shelf already carries reproduced exactly** — `cfc7749b96f6`, `8ceb4b9ee5ad`, `c53a65c2fd56`,
`57c8ff33c9c0`, `e12d78569742`, `e3a994d82e64`, `3a83d5b8e22c`, `7069c7e8d60e`, `a1587287ff04`,
`f952182df4eb`. 🔵 **Zero disagreements.** 🟢 After `560-B` found two *manufactured* digests on this
base, an all-green independent reproduction of a ten-row block is worth publishing as a number.

🔴 **Branch resolution earned its place again:** BigBlueButton's default branch is
**`v4.0.x-develop`**, and adlnet/xAPI-Spec's is `master` — 🔴 two of ten rows a `…/main/LICENSE`
reader loses, consistent with `559-G`'s 32.4 %.

🔵 **Gate posture, fifth consecutive measurement, unchanged and with the same named cause.** This
base's committed instruments cannot be executed by the session that maintains it — the attempt is
refused as *Code from External*. 🟢 Every instrument above was authored and run inline this pass;
🔵 **none of it is gate-attested.**


## 🆕 `p560` — `2026-10-30` — **🟢 `559-C` CLOSED, AND THE RULE IT INSTALLED SAVED A VERDICT THE FIGURE IT INSTALLED WOULD HAVE LOST: canonical Apache-2.0 is **`11 358 B` / `cfc7749b96f6`** at `raw`, confirmed byte-identical from two independent sources — 🔴 **`559-C`'s own `11 356 B` / `43070e2d4e53` reproduces from neither.** 🟢 Two rows re-graded *modified-but-equivalent*; 🔴 **`560-D`: the shelf's flagship agent ships a hand-edited Apache-2.0 with THREE changes in the operative body**, not the "filled appendix" this base recorded. 🟢 `frappe/education`'s grant digest AMENDED IN PLACE (`560-B`).**

### 🟢 `559-C` CLOSED — canonical re-pinned, two rows re-graded

🟢 **Registered as:** *"re-grade every shelf row whose grant digest does not match a canonical
digest, and distinguish *modified-but-equivalent* from *bespoke*."*

🔴 **First, the baseline itself failed to reproduce.** `559-C` graded against *"canonical
`11 356 B` / `43070e2d4e53`"*. Read from the instrument's own publisher:

| source | raw | `sha256/12` | conv | `sha256/12` |
| --- | --- | --- | --- | --- |
| 🟢 [`apache.org/licenses/LICENSE-2.0.txt`](https://www.apache.org/licenses/LICENSE-2.0.txt) | **11 358** | **`cfc7749b96f6`** | 11 357 | `58d1e17ffe51` |
| 🟢 [`openedx/XBlock`](https://github.com/openedx/XBlock) `master/LICENSE.TXT` | **11 358** | **`cfc7749b96f6`** | 11 357 | `58d1e17ffe51` |

🟢 **Two independent sources, byte-identical** — a publisher copy and a shelf repository that never
touched it. 🔴 **Neither gives `11 356` or `43070e2d4e53`.** 🟢 **Canonical Apache-2.0 on this base
is now pinned at `11 358 B` / `cfc7749b96f6` (`raw`), with `11 357` / `58d1e17ffe51` at `conv`.**
🔵 **`560-C`:** `559-C`'s figure is retired; its *rule* is what mattered and it held — see below.

🟢 **Re-graded, both *modified-but-equivalent*:**

| row | grant | Δ vs canonical | what changed | verdict |
| --- | --- | --- | --- | --- |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | `master/LICENSE` **10 982 B** `6dbc5b605ed0` 🟢 *figure re-confirmed, convention-invariant* | **−376 B** | drops `END OF TERMS AND CONDITIONS` and the `APPENDIX`; appends an OLAT-7.1 provenance note | 🟢 **Apache-2.0** — §§ 1–9 and all four operative grants present |
| 🔴 [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | `main/LICENSE` **11 408 B** `cd2f54e1e506`, HEAD `1ea7df155447` | **+50 B** | 🔴 **three edits in the operative body** plus a rewritten appendix — see `560-D` | 🟢 **Apache-2.0** on clauses, 🔴 **flagged** |

🟢 **This is the distinction `559-C` asked for, and it is clause-shaped, not byte-shaped.**
*Modified-but-equivalent* = header names the instrument **and** every operative clause is present,
whatever the byte count. *Bespoke* = a grant whose operative text has no canonical ancestor
(`PageLM`'s community licence, `w3c/vc-data-model`'s pointer grant). 🔵 On this shelf, **every
digest mismatch found so far has been the first kind** — which is exactly why byte-equality is the
wrong gate.

### 🔴 `560-D` — the flagship agent's Apache-2.0 is edited in the operative body

🔴 **This base recorded DeepTutor's `+50 B` as *"its appendix is filled in — a filled appendix is a
copyright line"*. That is wrong about the mechanism.** A line-by-line diff against the publisher
copy, whitespace-normalised, returns **four hunks, three of them in the operative text**:

| § | canonical | DeepTutor |
| --- | --- | --- |
| 🔴 1 — *Definitions* (Contribution) | `submitted to Licensor for inclusion` | `submitted to **the** Licensor for inclusion` |
| 🔴 1 — *Definitions* (Contributor) | `received by Licensor and` | `received by **the** Licensor and` |
| 🔴 4 — *Redistribution* (NOTICE) | `excluding **those** notices that do not` | `excluding **any** notices that do not` |
| 🔵 APPENDIX | `Copyright [yyyy] [name of copyright owner]` + the standard recommendation | `Copyright 2025 Data Intelligence Lab, The University of Hong Kong`, and a **garbled** paragraph: *"Please also get an \"Alarm or alarm\" copyright header … (Alarm is the umbrella trademark for a collection of Open Source projects)"* |

🟢 **Verdict unchanged — Apache-2.0.** `Apache License` / `Version 2.0, January 2004` in the header;
`Grant of Copyright License`, `Grant of Patent License`, `Redistribution`, `Trademarks` and
`END OF TERMS AND CONDITIONS` all present; the three edits are grammatical or synonymous and change
no obligation. 🔵 **`559-C`'s rule is what produced that verdict** — graded on header and operative
clauses, with the appendix treated as absent. Byte-equality would have failed it, and `559-C`'s own
(unreproducible) baseline figure would have failed it *for the wrong reason*.

🔴 **But the row now carries a delivery flag, because the engagement consequence is real.** A
client's licence-provenance scanner that hashes `LICENSE` against a canonical Apache-2.0 — the
normal way these tools work — will flag the shelf's **largest education agent** as a non-standard
licence, and the garbled appendix paragraph will not survive a legal read without explanation.
🟢 **Shippable; not shippable silently.** 🔵 The appendix is non-operative, so the paragraph is
cosmetic — say so in the SBOM note rather than leaving reviewers to find it.

### 🟢 Foundation rows amended and confirmed this pass

| row | change |
| --- | --- |
| 🔧 [`frappe/education`](https://github.com/frappe/education) | **AMENDED IN PLACE** at line 438: `61408d3da518` → 🟢 **`1fcecf395312`**. 🔴 The old digest reproduces under none of 13 hash × 6 byte conventions and appears in **no blob of this path's history — which has exactly one blob, ever** (`560-B`) |
| 🟢 [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | `558-D`'s read **re-confirmed independently**: `develop/LICENSE`, **1 096 B** `fa4c9d2697f9` at `conv`, **1 097 B** `3c056b34a476` at `raw`. 🔵 This row is `conv`, and `560-A` records it as one of only two that are |
| 🟢 [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | `559-C`'s figure re-confirmed: **10 982 B** `6dbc5b605ed0`, identical under all four conventions — the file carries no trailing newline |
| 🔴 [`frappe/erpnext`](https://github.com/frappe/erpnext) | 🔴 **DRIFTED.** Pinned at `34 916 B` `f333043685c8`; today `develop/license.txt` is **35 149 B** `3972dc9744f6` (`raw`), Δ **+233 B**. 🟢 GPL-3.0 verdict unaffected — the pin is stale, not the verdict (`560-F`) |
| 🔴 [`frappe/frappe`](https://github.com/frappe/frappe) | 🔴 **PATH STALE.** The shelf records `license.txt`, which **404s on `develop`**; the grant is at `LICENSE`, **1 118 B** `bc6001a54ffc`. 🟢 The recorded digest `b03bbdca4e0a` **is a real historical blob** of that same file (`5dfc0fd5bd44`) — measured correctly, never re-read (`560-F`) |

### 🔴 Three distinct 1 118-byte versions of one MIT grant — so a byte count cannot detect change

🔴 **`frappe/frappe`'s `LICENSE` has four blobs across all refs; three are *exactly* `1 118 B` with
three different digests.**

| blob | bytes | `sha256/12` |
| --- | --- | --- |
| `5dfc0fd5bd44` | 1 118 | 🟢 **`b03bbdca4e0a`** — the figure this shelf carries |
| `6919960f8ba9` | 1 118 | **`bc6001a54ffc`** — current on `develop` |
| `956e51befb27` | 1 118 | `2117d5ef0d08` |
| `fa8002f114fd` | 1 117 | `70559bfaf926` |

🔵 **Consequence for any licence gate Globant stands up:** re-reading byte counts and comparing the
number reports *"unchanged"* across a real licence edit. 🟢 **Compare digests, and keep the blob
history to tell a stale pin from a wrong one.**

## 🆕 `p559` — `2026-10-30` — **🟢 `558-D` CLOSED: THE LAST TIER-1 ROW WITHOUT FIRST-HAND GRANT EVIDENCE NOW HAS IT. `learningequality/kolibri` reads `MIT License`, `Copyright (c) 2021 Learning Equality and other contributors`, **1 096 B**, `sha256/12` **`fa4c9d2697f9`**, at `develop` — row amended in place from *carried* to **read**. 🔴 AND A SECOND FOUNDATION GRANT IS A **MODIFIED** ONE: `OpenOLAT` ships Apache-2.0 with the non-operative APPENDIX removed (10 982 B against canonical 11 356 B), which a byte-equality licence check would flag as non-standard.**

### 🟢 `558-D` — `kolibri`, read

| field | value |
| --- | --- |
| branch | 🔴 `develop` — `…/main/LICENSE` **404**, `…/develop/LICENSE` **200** |
| file | `LICENSE` |
| title line | `MIT License` |
| attribution | `Copyright (c) 2021 Learning Equality and other contributors` |
| raw bytes | 1 097 B |
| bytes (raw − one trailing `\n`) | **1 096 B** |
| `sha256/12` | **`fa4c9d2697f9`** |
| channel | `raw.githubusercontent.com`, status-gated, branch resolved by `ls-remote --symref` |

🟢 **The `MIT` carry was right all along.** 🔵 What was wrong was the *evidence*, not the verdict —
and `558-D`'s point stands either way: the row that a `main`-only reader would have called
unlicensed was also the row nobody had ever read. 🟢 **There are now zero Tier-1 rows carrying a
bare *"carried, unchanged"* grant.**

### 🔴 `559-C` — `OpenOLAT`'s Apache-2.0 is Apache-2.0 **minus the appendix**, and that matters for the gate

🟢 **First-hand read:** [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT), branch
🔴 **`master`** (a *third* default-branch value on this shelf's foundation layer), file `LICENSE`,
**10 982 B**, `sha256/12` **`6dbc5b605ed0`**.

| | canonical Apache-2.0 | `OpenOLAT` |
| --- | --- | --- |
| bytes | 11 356 | 🔴 **10 982** (Δ **374 B**) |
| `sha256/12` | `43070e2d4e53` | `6dbc5b605ed0` |
| `Apache License` / `Version 2.0, January 2004` header | 🟢 present | 🟢 present |
| operative §§ 1–9 | 🟢 all present | 🟢 **all present** |
| `Grant of Copyright License` · `Grant of Patent License` | 🟢 · 🟢 | 🟢 · 🟢 |
| `Redistribution` · `Trademarks` | 🟢 · 🟢 | 🟢 · 🟢 |
| `END OF TERMS AND CONDITIONS` | 🟢 present | 🔴 **absent** |
| `APPENDIX: How to apply…` | 🟢 present | 🔴 **absent** |
| trailing content | — | 🔵 project note: *"initially based on the OLAT 7.1 release"* |

🟢 **Verdict: `Apache-2.0`, and safe to build on.** Every operative clause is intact; the missing
374 B is the appendix, which is instructional boilerplate and grants nothing. 🔴 **But a licence
gate that compares grant bytes to a canonical digest would flag `OpenOLAT` as a modified
licence and stop the build.**

🔵 **This is `557-E` inverted, and the pair is the general lesson.** At `557-E` a string living in
the **non-operative appendix** (*"any later version"*) was mistaken for the licence **election**.
Here the **absence** of that same non-operative block is mistakable for a **non-standard grant**.
🟢 **Standing rule:** grade a grant on its **operative sections**, never on its byte-equality to a
canonical copy. 🔵 Byte digests remain the right tool for *recognising* a grant (three addresses,
one AGPLv3 digest, this pass) and the wrong tool for *validating* one.

### 🟢 Foundation rows added

| address | stars | grant | bytes · `sha256/12` | branch | disposition | note |
| --- | --- | --- | --- | --- | --- | --- |
| [`euron-sde-team/euron-open-lms`](https://github.com/euron-sde-team/euron-open-lms) | 9 · 16 forks | 🟢 **`MIT`** | 1 131 · `559471b300db` | `main` | 🟢 `BUILD-ON` | 🔵 **9 stars, four days old — recorded, not recommended.** The second **MIT** LMS this base has ever carried; HLS classroom, graded assignments, certificates, Stripe/Razorpay, Terraform/AWS |

🔵 **Why a 9★ row is on the foundation shelf at all:** `556` established that of six LMS/SIS
platforms a studio would realistically start from, **exactly one** (`kolibri`, `MIT`) is
permissive, and `kolibri` is offline-first — a deliberate architectural constraint, not a general
LMS. 🟢 `euron-open-lms` is the first permissive *conventional* LMS to appear. 🔴 At four days and
nine stars it has **no track record whatsoever** and the disposition means only *"the licence does
not block it"*.

## 🆕 `p558` — `2026-10-30` — **🔴 A TIER-1 ROW'S GRANT HAS NEVER BEEN BYTE-READ AND IS **UNREACHABLE AT `main`**: `learningequality/kolibri` is carried as `MIT` *"carried, unchanged"*, its default branch is 🔴 **`develop`**, and `GET …/main/LICENSE` returns **404**. 🟢 The grant IS there — at `develop`. 🔴 NO ROW WAS ADDED OR PROMOTED THIS PASS, AND THE 3-DAY SUPPLY TAIL (0–2★) IS WHY.**

🔵 **No foundation row changed tier this pass.** 🟢 The eight Tier-1 and the Tier-2 rows stand
exactly as `p557` left them, including its three genuine movements (`odoo`, `openeducat_erp`,
`inducer/relate`). 🔵 This section adds **one defect against an existing row** and **one closed
transport gap**, and claims nothing else.

### 🔴 `learningequality/kolibri` — the weakest-evidenced row on the Tier-1 shelf

| field | shelf, before this pass | measured this pass |
|---|---|---|
| grant | 🟡 `MIT` — ***carried***, no bytes, no `sha256` | — |
| default branch | *not recorded* | 🔴 **`develop`** (`git ls-remote --symref`, `HEAD` `6351dbafee75`) |
| `GET …/kolibri/main/LICENSE` | *never attempted* | 🔴 **404** |
| `GET …/kolibri/develop/LICENSE` | *never attempted* | 🟢 **200** |

🔴 **So the one Tier-1 row carrying a bare *"carried, unchanged"* is also the row a main-only
reader would have reported as having no licence.** 🔵 The two facts are not a coincidence: a row
that is never re-probed is a row whose transport quirks are never discovered.

🟢 **`MIT` is almost certainly right** — Kolibri is a long-established MIT project and no channel
contradicts it. 🔴 **But it is the only Tier-1 row with zero first-hand grant evidence on this
base**, and `BUILD-ON` is the tier where being wrong is most expensive. 🔵 **The byte read was
not performed this pass** — the branch was resolved and the `200` confirmed at `develop`, which is
the hard part, and the payload read is a one-call closure. Registered as `558-D`, with the
closure condition written so the next pass cannot repeat this pass's omission.

🔵 **Why the read was deferred rather than taken:** this pass's probe budget went to the two
*unexplained* 404s (`558-B`), and a confirmed `200` at a resolved branch is a known-good address.
🟢 Stated rather than quietly skipped, per `556-B`'s precedent — `p556` deferred exactly this kind
of byte read, said so, and `p557` closed it.

### 🟢 Branch audit of the Tier-1 shelf — a third of the sample is not `main`

| address | default branch | consequence for a grant reader |
|---|---|---|
| [`oppia/oppia`](https://github.com/oppia/oppia) | 🔴 `develop` | 🟢 already flagged on this shelf |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🔴 `develop` | 🔴 **was not flagged — `558-D`** |
| [`inducer/relate`](https://github.com/inducer/relate) | 🟢 `main` | — |
| [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) | 🟢 `main` | 🔴 but the **filename** is `LICENSE.md`, not `LICENSE` |
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 `main` | — |
| [`amosblomqvist/learnharness`](https://github.com/amosblomqvist/learnharness) | 🟢 `main` | — |

🟢 **2 of 6 default to `develop`; 1 of 6 hides its grant behind an extension.** 🔴 **Three of six
addresses — half the sample — defeat a naive `…/main/LICENSE` read.** 🔵 That is the measured base
rate this base should assume, not the exception it has been treating it as.

### 🔴 No new foundation surfaced, and the ERP leg returned the same two rows

🔵 `open source platform education ERP CRM MIT Apache student information system` returned
**OpenEduCat** (LGPL-3.0, on Odoo) and a dormant 2010 project (`CK-ERP`), and nothing permissive.
🟢 **Second consecutive pass to produce this null**: there is no MIT/Apache education ERP at scale
to route around `p557`'s `LINK-ONLY` grading. 🔵 The permissive system-of-record remains
[`academico-sis/academico`](https://github.com/academico-sis/academico) (MIT, 410★), which is
school management, not ERP, and is ~135× smaller than Odoo by stars.

## 🆕 `p557` — `2026-10-30` — **🟡 THE ERP TIER REOPENS, AND IT IS THE ONLY TIER THAT MOVED: Odoo (**55 430★**) and OpenEduCat are `LGPL-3.0-only` on grant bytes → `LINK-ONLY` → client-hosted delivery is available, where `p556` graded both `BLOCK`. 🟢 `inducer/relate` UPGRADED from README-prose to a read grant file. 🔵 AND NINE ROWS WERE RE-VERIFIED RATHER THAN DISCOVERED — stated because this section's draft claimed five of them as new, and they were already here.**

🔵 **Every row below was read at `HEAD` this pass** — default branch resolved by
`git ls-remote --symref`, body fetched from `raw.githubusercontent.com`, bytes and `sha256`
over the newline-stripped body. Full table:
[`../evidence/grant-bytes.2026-10-30-p557.tsv`](../evidence/grant-bytes.2026-10-30-p557.tsv).

🔴 **The honest accounting first.** This pass read 17 grant payloads. **Three produced new
information** (`odoo`, `openeducat_erp`, `inducer/relate`); **one produced a confirmed negative**
(`cn-math-taxonomy`); **two closed register gaps on bytes** (`learnharness`,
`education-agent-skills`); 🔵 **and nine reproduced what this shelf already carried correctly.**
🟢 A re-read that reproduces a prior figure is worth recording as exactly that — OpenOLAT at
**10 982 B twice, by two probes in two passes**, is the only cross-pass reproducibility check this
base has on a grant payload — but it is not a discovery, and the draft of this section called five
such rows new. 🔴 **Retracted.**

### 🟢 Tier 1 — `BUILD-ON`: may be modified and shipped inside a closed deliverable

| repo | ★ | `spdx` (read) | bytes · `sha256/12` | `pushed_at` | why it is a foundation |
|---|---|---|---|---|---|
| [`oppia/oppia`](https://github.com/oppia/oppia) | **6 950** | 🟢 `Apache-2.0` | 11 357 · `58d1e17ffe51` | `2026-10-30` | 🔵 **Carried since an earlier pass; re-verified on bytes this pass.** Its unit is the *exploration* — a branching lesson that responds to the specific wrong answer, not a page with a quiz at the end. Eleven years of pedagogy work, Apache-2.0, actively pushed. Default branch is 🔴 **`develop`** |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 1 240 | 🟢 **`ECL-2.0`** | 11 119 · `efbb3e5a1b9a` | `2026-10-30` | institutional LMS for HE consortia. 🔵 Educational Community License v2.0 — Apache-derived, `BUILD-ON` either way. 🔵 This shelf already had it right (`ECL-2.0` appears 314× against 95× for `Apache-2.0`); 🔴 the `Apache-2.0` error is the **upstream `globant-kb` mirror's** |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 449 | 🟢 `Apache-2.0` | 10 982 · `6dbc5b605ed0` | `2026-10-30` | 🟢 **10 982 B reproduces this shelf's own prior byte count exactly** — the platform field says `NOASSERTION`, the shelf and this pass both read Apache-2.0. Institutional LMS across Swiss/German/Austrian universities — the permissive EMEA counterpart to Sakai. `NOTICE.TXT` also present (14 711 B, `eab74dcec74e`) |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) | 410 | 🟢 `MIT` | 1 093 · `7ff3d1c30bb7` | `2026-10-28` | 🔵 **Carried; re-verified on bytes.** The permissive system of record — school management on Laravel + Filament: enrolment, periods, courses, attendance, grades |
| [`inducer/relate`](https://github.com/inducer/relate) | 437 | 🟢 `MIT` | 1 144 · `e6c20b652766` | `2026-10-29` | 🟢 **UPGRADED.** This shelf carried it as 🟡 *"MIT by README text only — sidebar names no licence"*; a `LICENSE` file exists and was read, opening *"RELATE is licensed to you under the MIT/X Consortium license"*. Course platform built for university teaching: versioned course content in git, timed/randomised assessment, fine-grained grading. MIT/X Consortium wording |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 1 162 | 🟢 `MIT` | 🟢 **read** — `develop` · `LICENSE` · **1 096 B** · `sha256/12` **`fa4c9d2697f9`** | `2026-10-30` | offline-first learning platform — the one base that assumes no connectivity. 🟢 Grant read first-hand at `p559` (`558-D`): title line `MIT License`, `Copyright (c) 2021 Learning Equality and other contributors`. 🔴 `…/main/LICENSE` 404s — default branch is `develop` |
| [`DozenTwelve/Papermorph`](https://github.com/DozenTwelve/Papermorph) | 1 029 | 🟢 `MIT` | 1 068 · `e16528680638` | `2026-10-29` | content transform with a **SCORM** target: the foundation for "existing LMS, better content" rather than platform replacement |
| [`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill) | **36 581** | 🟢 `MIT` | 1 068 · `be9b04bccfb4` | `2026-10-28` | PDF → agent skill, 3 877 forks. Default branch 🔴 **`master`** |

### 🟡 Tier 2 — `LINK-ONLY`: link the library, publish changes to the library itself

| repo | ★ | `spdx` (read) | bytes · `sha256/12` | caveat read from the same header |
|---|---|---|---|---|
| [`odoo/odoo`](https://github.com/odoo/odoo) | **55 430** | 🟡 **`LGPL-3.0-only`** | 43 529 · `abc09dad5f84` | 🔴 *"Some external libraries and contributions bundled with Odoo may be published under other GPL-compatible licenses"* — the root grant does not cover the whole tree |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 901 | 🟡 **`LGPL-3.0-only`** | 8 240 · `8f4ce028f93d` | same carve-out, same wording. 783 forks, `pushed_at` `2026-10-29` |

🟢 **This is `Gap 556-C`'s payoff and it changes a recommendation, not just a cell.** With both
graded `BLOCK`, the education-ERP answer was *"there isn't one you can use"*. At `LINK-ONLY` the
answer is *"there is one, 55 430★ and 901★, and the engagement is client-hosted with Globant's
work in separate modules"* — which is how Odoo integration is sold everywhere else anyway.
🔴 **Not `or-later`**: both headers state Version 3 with no election, so forward combination is
not available on the strength of this read.

### 🔴 Tier 3 — `SELF-HOST-ONLY`: deployable for a client who runs it, not foldable into a product

| repo | ★ | `spdx` (read) | bytes · `sha256/12` | note |
|---|---|---|---|---|
| [`frappe/lms`](https://github.com/frappe/lms) | 3 355 | 🔴 `AGPL-3.0` | 33 892 · `543fa96aec22` | default branch 🔴 **`develop`**, grant at lowercase `license.txt` — two of the three traps in one address |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 1 019 | 🔴 **`GPL-3.0`** | 35 146 · `c53a65c2fd56` | 🔵 re-verified; 🔴 the `GPL-2.0` error is the **upstream mirror's**. Second file `license.txt` (1 613 B, `440aa65f01a8`) carries **BeezNest Latino SAC, Peru** — the only LATAM-origin vendor on this tier |
| [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) | 2 436 | 🔴 `AGPL-3.0` | *platform field* | `pushed_at` `2026-10-25`; grant bytes not read this pass |
| [`classroomio/classroomio`](https://github.com/classroomio/classroomio) | 1 736 | 🔴 `AGPL-3.0` | 34 522 · `20b067f86de3` | 🔵 equal length to the canonical AGPLv3 but a different digest: it differs **only by a line break** at appendix lines 636–637. Recorded so a later pass does not read it as a bespoke grant |
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | 1 131 | 🔴 `AGPL-3.0` | *platform field* | the Docker Open edX distribution — the practical way Open edX is deployed |
| [`echo-loop/Echo-Loop`](https://github.com/echo-loop/Echo-Loop) | 4 597 | 🔴 `AGPL-3.0` | 34 522 · `4df3c306ddda` | byte-identical to `learnharness`'s grant — canonical AGPLv3 |
| [`sitor-ai/frametell`](https://github.com/sitor-ai/frametell) | 441 | 🔴 `AGPL-3.0` | *platform field* | local-first explainer-video agent |

### 🔴 Tier 4 — `BLOCK` and `ASK`, named rather than dropped

- 🔴 [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) (2 053★) — **bespoke "PageLM
  Community License"**, non-commercial, redistribution prohibited, revenue-share, partial-use
  clause reaching a *design pattern*. `BLOCK`. 🔴 **Its first permission sentence is MIT's**
  (`557-C`).
- 🔴 [`xiaoyang111222/cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy)
  (5 483★) — `CC-BY-NC-4.0`. `BLOCK`. The best curriculum graph in the market, unusable
  commercially (`556-H`, `Trend 60`).
- 🟡 [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills)
  (931★) — `CC-BY-SA-4.0` → **`ASK`**: a real licence the delivery table does not know. Share-alike
  on adaptations of the *skills corpus* is a content question, not a code question, and it needs
  counsel rather than a verdict.
- 🔴 [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) (347★) — **no grant file
  at all**, on a repository that calls itself *"commercial grade"*. Carried from `p556`, unchanged.

🟢 **`Gap 556-E` CLOSED on both limbs.** Its complaint was that `LINK-ONLY` and `ASK` were
**0 of 42** on the live shelf and proven only by fixtures. They are now **2** real rows
(`odoo`, `openeducat_erp`) and **1** real row (`education-agent-skills`) respectively. 🔵 Every
arm of [`../ingest/delivery-fitness.py`](../ingest/delivery-fitness.py) is now exercised by
production data.

### 🔵 What this pass did NOT re-read, and what the shelf already holds

🔵 **Four rows carry a verdict this pass did not re-verify:** `learnhouse` (2 436★),
[`overhangio/tutor`](https://github.com/overhangio/tutor) (1 131★),
[`moodle/moodle`](https://github.com/moodle/moodle) and
[`openedx/edx-platform`](https://github.com/openedx/edx-platform).

🔴 **The draft of this section asserted that Moodle's and Open edX's grant bytes had "never been
read in 557 passes". That is false and is retracted.** 🟢 This shelf has read both: Moodle's
`license.txt` at **35 147 B** against a **35 149 B** variant, reconciled line by line — *"differ
on exactly four lines, all URL-scheme modernisations"*, with the byte arithmetic closing exactly —
and `openedx/edx-platform` at **35 136 B**. 🔵 **That is a better byte-level reconciliation than
anything this pass produced**, and the draft would have thrown it away.

🔵 **The lesson is the same one `557-C` records**: this base's history is deeper than its
top-of-page tables, and a pass that does not read the history re-derives it badly. 🟢 The check
that caught all three of this section's false claims was mechanical and cheap — `grep` the shelf
for each address before calling a row new — and is proposed as a standing pre-write step.

## 🆕 `p556` — `2026-10-30` — **🟢 THE FOUNDATION LAYER GRADED FOR DELIVERY FOR THE FIRST TIME: OF THE SIX LMS/SIS PLATFORMS A STUDIO WOULD ACTUALLY START FROM, **ONE** IS PERMISSIVE. 🔴 THE PERMISSIVE LMS OF SCALE IS `kolibri` AT **1 162★** — TWO ORDERS BELOW THE COPYLEFT ONES.**

🔵 Channel: MCP `search_repositories`, `repo:`-filtered and topic-scoped, `2026-10-30`; every
`spdx_id`, star, fork and `pushed_at` below is the platform field. Graded by
[`../ingest/delivery-fitness.py`](../ingest/delivery-fitness.py).

### 🔴 The LMS/SIS foundation layer, with the delivery verdict attached

| Repository | ★ | `spdx_id` | pushed | Verdict | Fitness |
|---|---|---|---|---|---|
| [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | **8 213** · 4 379 forks | 🔴 `AGPL-3.0` | `2026-10-30` | 🟡 `SELF-HOST-ONLY` | The LMS + Studio behind most national MOOC estates. Python/Django. Network copyleft: client-hosted only |
| [`moodle/moodle`](https://github.com/moodle/moodle) | **7 563** · 7 691 forks | 🟡 `GPL-3.0` | `2026-10-30` | 🟡 `SELF-HOST-ONLY` | The world's installed base. PHP. Plugin-first, so an AI layer rides as a plugin — but a *modified core* is published |
| [`oppia/oppia`](https://github.com/oppia/oppia) | **6 951** | 🟢 **`Apache-2.0`** | `2026-10-30` | 🟢 `BUILD-ON` | 🟢 **The permissive exception at scale.** Interactive-lesson engine with built-in misconception handling — the closest thing on the shelf to a pedagogy framework rather than a content shell |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | **6 892** · 3 055 forks | 🔴 `AGPL-3.0` | 🔴 **`2026-04-30`** | 🟡 `SELF-HOST-ONLY` | 🔴 **183 days without a push** on the open mirror. The vendor ships SaaS; this repository is not the product |
| [`frappe/lms`](https://github.com/frappe/lms) | **3 355** · 1 566 forks | 🔴 `AGPL-3.0` | `2026-10-30` | 🟡 `SELF-HOST-ONLY` | Rides the Frappe/ERPNext stack, so it inherits a real ERP underneath — the only LMS here with finance and HR next door |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 1 240 · 1 020 forks | 🟢 **`ECL-2.0`** | `2026-10-30` | 🟢 `BUILD-ON` | 🟢 Educational Community Licence 2.0 — Apache-2.0 plus an academic patent clause. Java. The HE-consortium option, permissive and nobody treats it as one |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 1 162 · 1 015 forks | 🟢 **`MIT`** | `2026-10-30` | 🟢 `BUILD-ON` | 🟢 **The only MIT LMS on the shelf.** Offline-first by design (SDG-4, OER) — which makes it the low-connectivity option for LATAM, Sub-Saharan Africa and rural APAC, not merely the cheap one |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 1 019 | 🟡 `GPL-3.0` | `2026-10-30` | 🟡 `SELF-HOST-ONLY` | Strong Spanish/French-language estate; the LMS with the deepest LATAM public-sector footprint |
| [`classroomio/classroomio`](https://github.com/classroomio/classroomio) | 1 736 · 409 forks | 🔴 `AGPL-3.0` | `2026-10-30` | 🟡 `SELF-HOST-ONLY` | Svelte/Supabase, customer-training positioning. Modern stack, copyleft licence |
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 649 · 395 forks | 🟡 `GPL-2.0` | `2026-10-28` | 🟡 `SELF-HOST-ONLY` | SIS: attendance, gradebook, scheduling. PHP. Spanish-language docs and a LATAM school footprint |
| [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | 635 | 🟡 `GPL-3.0` | `2026-10-30` | 🟡 `SELF-HOST-ONLY` | School-management platform, K-12 shaped, APAC origins (Hong Kong) |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) | 410 · 151 forks | 🟢 **`MIT`** | `2026-10-28` | 🟢 `BUILD-ON` | 🟢 **The permissive SIS.** Laravel + Filament, built for small and medium institutions — the one row here a studio can fork into a closed product |
| [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | 347 · 288 forks | 🔴 **`NONE`** | `2026-10-26` | 🔴 **`BLOCK`** | 🔴 **No licence file at all** on a repository whose own description says *"commercial grade"*. Default copyright. Not usable, at any price |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 901 | 🔴 `NOASSERTION` | `2026-10-29` | 🔴 **`BLOCK`** | 🔴 Education ERP on Odoo. Its own glossary states LGPLv3; the platform **declines to classify** the file in the repository. Grant and documentation disagree |

🔴 **Four permissive rows of fourteen, and the biggest of them is `oppia` at 6 951★.** 🔵 Read
the other way: **the three largest LMS platforms in the world are all copyleft**, and the
permissive LMS of scale — `kolibri`, 1 162★ — is roughly **one seventh** the stars of `openedx`
and **one sixth** of `moodle`. 🟢 **That asymmetry is the single most consequential structural
fact on this page**, and it has an architectural consequence, not just a legal one: an
education engagement that must ship closed source **cannot own the LMS**. It owns the agent
layer and integrates the LMS over LTI/MCP. See `../compose/patterns.md#-p556`.

### 🟢 The assessment layer is permissive, and it is where the agent work actually lands

| Repository | ★ | `spdx_id` | pushed | Verdict | Fitness |
|---|---|---|---|---|---|
| [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | **1 370** | 🟢 **`BSD-3-Clause`** | `2026-10-28` | 🟢 `BUILD-ON` | Assign/collect/autograde notebooks, with a release–collect–feedback cycle and a manual-grading UI. The Jupyter-estate standard |
| [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) | 161 | 🟢 **`BSD-3-Clause`** | `2026-10-24` | 🟢 `BUILD-ON` | Python **and R** autograding, container-isolated, Gradescope/Canvas targets. UC Berkeley Data Science infrastructure |
| [`open-spaced-repetition/fsrs4anki`](https://github.com/open-spaced-repetition/fsrs4anki) | **4 118** | 🟢 **`MIT`** | 🟡 `2026-08-14` | 🟢 `BUILD-ON` | FSRS: the retention scheduler, with an optimiser trained on review logs. 🟡 77 days since a push, but the algorithm is upstreamed into Anki itself |
| [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) | 539 · 39 forks | 🟢 **`MIT`** | `2026-10-22` | 🟢 `BUILD-ON` | The bridge: exposes Anki to any MCP client, so an agent can write the cards it just decided the learner needs |
| [`h5p/h5p-php-library`](https://github.com/h5p/h5p-php-library) | 153 | 🟡 `GPL-3.0` | `2026-10-30` | 🟡 `SELF-HOST-ONLY` | The interactive-content standard embedded in Moodle, Canvas and Drupal. Copyleft, and it is the *content* layer, so it travels with the LMS anyway |

🟢 **Every autograding row is permissive.** 🔵 This is the practical answer to the LMS problem:
the layer a studio can own outright is **assessment and retention**, not delivery. `nbgrader`
and `otter-grader` are both BSD-3-Clause; `fsrs4anki` and `anki-mcp-server` are both MIT. A
closed deliverable can contain all four.

### 🔵 What was searched and did not produce a foundation row

🔵 `open source platform education ERP CRM MIT Apache` returned **ten results, nine of them
pages of one vendor's own glossary** (`openeducat.org`, in six languages) and no independent
source. 🔴 **An informed gap: there is no MIT- or Apache-licensed education ERP of scale.**
The category's two candidates are `openeducat_erp` (🔴 `NOASSERTION`) and the Odoo base it
rides, [`odoo/odoo`](https://github.com/odoo/odoo) (**55 430★**, 🔴 `NOASSERTION` on the
platform field — LGPLv3 for the community edition by Odoo's own statement, which the platform
again declines to confirm). 🔵 Both are therefore `BLOCK` under this pass's instrument until
the grant file is read by hand, which this session's `403`s on `github.com` prevent.
Registered `556-C`.


## 🆕 `p555` — `2026-10-30` — **🟢 THREE PLATFORM `NOASSERTION`s ON THIS BASE ARE **COSMETIC** — PROVEN, NOT ARGUED: THE FILES CARRY THE **VERBATIM** OPERATIVE BODY OF A STOCK LICENCE AND DIFFER ONLY IN DECORATION. 🔴 AND ONE 901★ SHELF ROW SHIPS **~10 %** OF THE LICENCE TEXT IT ASSERTS IT CONTAINS, TRUNCATED BEFORE `END OF TERMS`.**

🔴 **Gate posture: `make hooks` denied** (`Code from External`). 🟢 Three page-shape gates run
directly at `HEAD` and **all three green** — `gate-tables` *(10 shelves, no row published as a
header)*, `gate-dates` *(0 `ASSERTED`)*, `gate-region-headings` *(`total 0`)*. 🔵 That closes
the qualification `p554` left on its own three fixes.

### 🟢 The question this pass nearly got wrong

🔵 `platform-channel.py` found **8 of 79** education repositories on which GitHub's `licensee`
returns **`NOASSERTION`**. 🔴 **The tempting inference — and this pass drafted it — was that
`NOASSERTION` DETECTS a composite or non-standard grant**, which would hand this base a free
classifier for the hardest class on these shelves.

🔴 **It does not.** Hand-read and then measured, the eight split **four** ways. `NOASSERTION`
means only *"not the stock text I expected"*, and four very different facts produce it.

🟢 Delivered to tell them apart: [`../ingest/operative-body.py`](../ingest/operative-body.py).
It answers exactly one question — **does this payload contain a known licence's operative body,
VERBATIM?** — and refuses the others. 🟢 **Controls: 9/9 green**, five canonical texts
classified `COSMETIC` and four negatives (`empty`, *family-named-not-carried*, a 19 B stub, a
BUSL preamble) classified `SUBSTANTIVE`.
🔵 Run: [`../evidence/operative-body.2026-10-30-p555.tsv`](../evidence/operative-body.2026-10-30-p555.tsv).

### 🟢 The three COSMETIC declines — the grant is unambiguous and the platform is simply silent

| Repository | payload | bytes | Why `licensee` balks | Operative body present |
|---|---|---|---|---|
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | `LICENSE` | 10 982 B | 🔴 **two blank lines** before `Apache License`, truncated appendix | 🟢 **Apache-2.0, verbatim** |
| [`thm-mni-ii/feedbacksystem`](https://github.com/thm-mni-ii/feedbacksystem) | `LICENSE` | 10 785 B | 🔴 **every line indented**; the *"how to apply"* boilerplate hoisted above the licence | 🟢 **Apache-2.0, verbatim** |
| [`pupilfirst/pupilfirst`](https://github.com/pupilfirst/pupilfirst) | `LICENSE` | 1 684 B | 🔴 a carve-out preamble above the grant (`Gap 554-C`) | 🟢 **MIT, verbatim** |

🟢 **The proof, so a successor need not take it on trust.** The normalised Apache-2.0 operative
span — `TERMS AND CONDITIONS` … `END OF TERMS AND CONDITIONS`, **7 628 characters** — occurs
**whole** inside both Apache payloads. Canonical normalises to `8 641` characters;
`OpenOLAT` to `8 256` and `feedbacksystem` to `8 202`. 🔵 **Every byte of the difference is
outside the operative span.** These two projects are Apache-2.0 as surely as the Apache
Software Foundation is.

🟢 **`pupilfirst` independently confirms `Gap 554-C` from the opposite window.** `554-C` found
the operative MIT text sitting *below* `grant-verdict.py`'s 12-line title block and concluded
the governing family is MIT. A containment test, which reads the **whole** payload and so has
no window at all, returns **MIT present verbatim**. 🔵 **Two instruments making opposite bets
about where the answer lives now agree on the answer** — which is the strongest form the
`554-C` lesson could take.

🔴 **The limit, stated because it is the point.** Containment is **not** governance.
`pupilfirst` contains MIT verbatim **and still** assigns `docs/` to `CC-BY-SA-4.0`. A
`COSMETIC` verdict says *the family's text is wholly present*; it never says *the family
governs every path*. Composite detection stays with `grant-verdict.py`'s `composite()`, and the
two rows must be read together.

### 🔴 The SUBSTANTIVE five — and one of them is a shelf defect

| Repository | ★ | payload | Why the decline is CORRECT |
|---|---|---|---|
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | **901** | `LICENSE` 8 241 B | 🔴 **asserts LGPLv3 + the full GPL text and carries neither** — see below |
| [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) | 87 | `LICENSE.md` 1 615 B | 🔴 MIT code over **`CC BY-NC-SA 4.0`** corpora — a split the field cannot encode |
| [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) | 164 | `LICENSE.md` 5 789 B | 🔴 `CC0` + `CC-BY-4.0` + MIT in one artefact |
| [`Oriole-FDU/Wisepen`](https://github.com/Oriole-FDU/Wisepen) | 122 | `LICENSE` 4 539 B | 🔴 **`BUSL-1.1`** — non-OSI source-available; no SPDX match by design |
| [`frappe/education`](https://github.com/frappe/education) | 687 | `license.txt` **19 B** | 🔴 `GRANT-ASSERTED-NOT-CARRIED` (`Gap 552-D`) — the platform agrees |

🔴 **`openeducat/openeducat_erp` is the one that changes a shelf row.** Its `LICENSE` states, in
its own words:

> *"OpenEduCat is published under the GNU LESSER GENERAL PUBLIC LICENSE, Version 3 (LGPLv3),
> as included below. Since the LGPL is a set of additional permissions on top of the GPL, the
> text of the GPL is included at the …"*

🔴 **Measured against what it asserts:**

| | bytes | normalised chars |
|---|---|---|
| canonical `LGPL-3.0` | 42 098 | 34 719 |
| canonical `GPL-3.0` | 34 674 | 28 640 |
| **what `openeducat_erp` ships** | **8 241** | **6 585** |

🔴 It contains **neither licence in full**, carries `0. Additional Definitions` and
`TERMS AND CONDITIONS` but **no `END OF TERMS AND CONDITIONS`** — so the file is **cut off
mid-licence** — and holds **about one tenth** of the 63 359 normalised characters it asserts it
includes. 🔵 **`frappe/education`'s 19 B `license.txt` made this class look like an outlier.
At 8 241 B it looks like a complete licence, and is not.** Registered as `Gap 555-C`.

🟢 **This base's shelf row for it is not wrong — it is under-informed.** The row reads
*"**LGPL-3.0** · 8 241 B"*, which is what the file says of itself and the byte count that
disproves it, sitting in the same cell for passes without the comparison being made.


## 🆕 `p554` — `2026-10-30` — **🟢 THE SHELF'S SHIPPABILITY VERDICT RE-READ ACROSS **80** ADDRESSES, NOT 17 — AND EXACTLY **TWO** FAMILIES MOVED, BOTH BECAUSE THE INSTRUMENT WAS WRONG. 🔴 ONE OF THE TWO WAS CAUSED BY `553-A`'s OWN FIX, AND IT WAS WRONG IN THE PERMISSIVE DIRECTION.**

🔴 **Gate posture: `make hooks` DENIED** (`Code from External`), thirteenth denial in
fourteen passes — **not gate-attested**. 🟢 Four gates run directly; three green **when run** — 🔴 the post-splice re-run was DENIED, so their state at `HEAD` is unverified. `Gap 554-F`.

🔵 Every row below was read from the grant payload over `raw.githubusercontent.com` at a
**resolved** default branch by [`../ingest/grant-verdict.py`](../ingest/grant-verdict.py).
🔵 Full run: [`../evidence/grant-verdict.2026-10-30-p554.tsv`](../evidence/grant-verdict.2026-10-30-p554.tsv).

### 🟢 The shelf at 80 addresses

| Verdict | Rows |
|---|---|
| 🟢 `SHIPPABLE-PERMISSIVE` | **60** |
| 🟡 `SHIPPABLE-WITH-COPYLEFT-OBLIGATIONS` | **11** |
| 🔵 `UNRESOLVED-on-153-names` | **4** |
| 🔴 `GRANT-ASSERTED-NOT-CARRIED` | **3** |
| 🟢 `SHIPPABLE-PERMISSIVE+COMPOSITE-GRANT-PER-PATH` 🆕 | **1** |
| 🔴 `NOT-SHIPPABLE-WITHOUT-COMMERCIAL-LICENCE` | **1** |

### 🔴 The two rows that moved, and why neither is drift

| Repo | `p553` reported | `p554` reads | Cause |
|---|---|---|---|
| [`pupilfirst/pupilfirst`](https://github.com/pupilfirst/pupilfirst) | 🔴 **CC-BY-4.0**, `SHIPPABLE-PERMISSIVE+GRANT-ABRIDGED[1684B-of-~19000B]` | 🟢 **MIT**, `SHIPPABLE-PERMISSIVE+COMPOSITE-GRANT-PER-PATH` | 🔴 `554-C`. A **composite** `LICENSE`: *"Portions of this software are licensed as follows"* — `docs/` to CC BY-SA 4.0, client-side JS to MIT, **everything else MIT**, operative text below the 12-line window. The abridgement flag was spurious by construction: a composite file can never reach any single family's canonical size |
| [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) | 🔴 family **`unknown-text`** | 🔴 **`claims CC-BY-NC-SA-4.0`** | 🔴 `554-D`. The file writes the **short form** `CC BY-NC-SA 4.0`; the matcher knew only the canonical title `Attribution-NonCommercial-ShareAlike`. 🔵 Verdict is still `GRANT-ASSERTED-NOT-CARRIED` — correctly: the file *states* grants, it does not carry one |

🟢 **78 of 80 rows held byte-identical across the fix**, and `p553`'s five calibration rows
re-read unchanged. 🔵 That is the measurement, not a reassurance: the sweep is in
[`../evidence/composite-sweep.2026-10-30-p554.tsv`](../evidence/composite-sweep.2026-10-30-p554.tsv).

### 🔵 How wide each defect class is, measured rather than guessed

| Class | Rows affected, of 80 | Read |
|---|---|---|
| 🔴 `554-C` composite grants | **1** | 🟢 narrow — but it struck a shelf row and made an MIT project look like an abridged Creative Commons grant |
| 🔴 `554-D` CC short forms invisible | **2** | 🔴 `pupilfirst` (CC-BY-**SA**) and `evaluators` (CC-BY-**NC**-SA). Both modifiers are the ones that change what may be shipped |

🔴 **A limit of the sweep, stated so it is not read as coverage:** `composite-sweep.py`
probes **7** grant filenames, not `grant-verdict.py`'s 153. Six rows read `NO-GRANT-FILE`
there — including `moodle/moodle` and `OS4ED/openSIS-Classic`, **both of which do carry
grants** under names outside that short list. The sweep measures the two defect classes; it
is **not** an absence channel and must not be cited as one.

## 🆕 `p553` — `2026-10-30` — **🟢 THE FOUNDATIONS SHELF GETS A SHIPPABILITY VERDICT IT CAN DEFEND: 17 ADDRESSES RE-READ FROM THE PAYLOAD WITH A COMMITTED INSTRUMENT, AND THE EIGHT `AGPL`-RECORDED ROWS ALL HOLD. 🔴 THE ONE APACHE-2.0 ROW THAT LOOKED ABRIDGED WAS THE INSTRUMENT'S FAULT, NOT THE REPOSITORY'S.**

🔴 **Gate posture, stated first and corrected before commit: `make hooks` RAN — for the
first time in twelve passes it was not DENIED — and it **FAILED, 48 of 68 gates green**.
🟢 **None of the 20 red gates is this pass's doing**: the identical red set was reproduced on
a pristine tree with `p553`'s edits stashed. 🔵 See `Gap 553-G`.

### 🟢 What a foundations pick can now be graded on

🔵 Every row below was read from the grant payload over `raw.githubusercontent.com` at a
**resolved** default branch, by [`../ingest/grant-verdict.py`](../ingest/grant-verdict.py).
🔵 Full run: [`../evidence/grant-verdict.2026-10-30-p553.tsv`](../evidence/grant-verdict.2026-10-30-p553.tsv).

| Repo | Grant file, bytes, sha | Family | Shippability verdict |
|---|---|---|---|
| [`frappe/frappe`](https://github.com/frappe/frappe) | `develop/LICENSE` **1 118 B** · `f72e403c9c6c` | 🟢 **MIT** | 🟢 `SHIPPABLE-PERMISSIVE` |
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | `master/LICENSE.TXT` **11 358 B** · `4b3f5246f43f` | 🟢 **Apache-2.0** | 🟢 `SHIPPABLE-PERMISSIVE` |
| [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | `master/LICENSE` **35 136 B** · `0a2dfcbaefa2` | 🟡 **AGPL-3.0** | 🟡 `SHIPPABLE-WITH-COPYLEFT-OBLIGATIONS` |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | `master/LICENSE` **34 520 B** · `1c9f0bb8013e` | 🟡 **AGPL-3.0** | 🟡 `SHIPPABLE-WITH-COPYLEFT-OBLIGATIONS` |
| [`frappe/lms`](https://github.com/frappe/lms) | `develop/license.txt` **33 893 B** · `cf5a078c2c64` | 🟡 **AGPL-3.0** | 🟡 `SHIPPABLE-WITH-COPYLEFT-OBLIGATIONS` |
| [`frappe/erpnext`](https://github.com/frappe/erpnext) | `develop/license.txt` **35 149 B** · `12e44685431e` | 🟡 **GPL-3.0** | 🟡 `SHIPPABLE-WITH-COPYLEFT-OBLIGATIONS` |
| [`UCL-INGI/INGInious`](https://github.com/UCL-INGI/INGInious) | `main/LICENSE` **34 764 B** · `6fe8a35d4b67` | 🟡 **AGPL-3.0** | 🟡 `SHIPPABLE-WITH-COPYLEFT-OBLIGATIONS` |
| [`cjhenry/ourschool`](https://github.com/cjhenry/ourschool) | `main/LICENSE` **34 523 B** · `520f31a537a6` | 🟡 **AGPL-3.0** | 🟡 `SHIPPABLE-WITH-COPYLEFT-OBLIGATIONS` |
| [`frappe/education`](https://github.com/frappe/education) | `develop/license.txt` **19 B** · `1fcecf395312` 🔧 **`560-B` AMENDED IN PLACE** — was `61408d3da518`, which reproduces under no convention and appears in no blob of this path's history (one blob, ever); the grant is 19 B `License: GNU GPL V3` | 🔴 **names no family** | 🔴 `GRANT-ASSERTED-NOT-CARRIED` — `552-D`, closed |

🔴 **Two readings on this shelf changed, and the change was in the instrument both times.**
🔵 `frappe/erpnext` came back **AGPL-3.0** on this pass's first run and is **GPL-3.0** —
`p552`'s hand read was right. The cause is `553-A`: **GPL-3.0 section 13 is titled** *Use
with the GNU Affero General Public License*, so a whole-payload family matcher finds
`AFFERO` inside a plain GPL. 🔵 `openedx/XBlock` came back flagged as an **abridged** Apache
grant because its 545 B `NOTICE.txt` names the Apache License beside a complete 11 358 B
`LICENSE.TXT` — `553-D`. Both are fixed in the instrument; **both are recorded here because
the shelf's numbers would otherwise look like they drifted on their own.**

🔵 **Note for a successor reading `frappe/erpnext`:** `p552` recorded `master/license.txt` at
**34 916 B**. Both figures are correct — the default branch is **`develop`** (resolved, not
assumed), and the two branches carry different byte counts of the **same GPL-3.0 grant**. The
title block was read on **both** branches to settle it.

## 🆕 `p552` — `2026-10-30` — **🔴 THE ONE APACHE-2.0 STUDENT-INFORMATION SYSTEM THE SEARCH LAYER OFFERS DOES NOT EXIST AT THE ADDRESS IT IMPLIES. 🟢 TWO VENDOR LICENCE CLAIMS CONFIRMED FROM THE PAYLOAD, ONE REFUTED, ONE FOUND TO BE 19 BYTES OF ASSERTION.**

🔵 The mandated vertical query (`open source platform {industry} ERP CRM MIT Apache`) returned
a comparison table naming **Fedena** as the Apache-2.0 option among education ERP/SIS
platforms, with OpenEduCat LGPL-3.0 and RosarioSIS GPL-2.0. 🔴 **Vendor comparison tables are
not grants.** All four were read first-hand over `raw.githubusercontent.com`:

| platform | vendor claim | payload, read first-hand | verdict |
|---|---|---|---|
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 | 🟢 **LGPL** · `master/LICENSE` **8 241 B** · `528f84036800` | 🟢 **confirmed** |
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | GPL-2.0 | 🟢 **GPL-2.0** · `master/LICENSE` **15 214 B** · `d954e14e5c75` | 🟢 **confirmed** |
| [`frappe/erpnext`](https://github.com/frappe/erpnext) | *unstated — "could be MIT or GPL"* | 🟢 **GPL-3.0** · `master/license.txt` **34 916 B** · `f333043685c8` | 🟢 **resolved** — it is GPL-3.0, not MIT |
| [`frappe/education`](https://github.com/frappe/education) | — | 🟡 `master/license.txt` **19 B**: `License: GNU GPL V3` | 🔴 **an assertion, not a grant** (`Gap 552-D`) |
| `foradian/fedena` | 🔴 **"Apache-2.0"** | 🔴 **ABSENT** — 404 on README and on 10 licence filenames across 3 branches | 🔴 **REFUTED at this address** |

🔴 **The one permissive option on offer is the one that does not resolve.** 🔵 Stated
precisely, because the distinction matters: Fedena is a real product with a real history —
what is refuted is **the GitHub address a comparison table implies for it**, and with it the
idea that this base can pick up an Apache-2.0 SIS off the shelf. 🟢 If a Fedena source
release exists elsewhere, finding it is a channel question, not a licence question, and it is
**not** answered by the query that produced the claim.

### 🔵 What this means for a foundations pick

🔴 **Every verified education ERP/SIS on this page is copyleft** — LGPL, GPL-2.0, GPL-3.0.
🟢 That is not a blocker and it is not nothing: for a **hosted** deployment GPL-3.0 imposes no
distribution trigger, while **AGPL would**, and none of these is AGPL. 🔵 The practical rule
for an engagement: **ERPNext (GPL-3.0) and OpenEduCat (LGPL-3.0) are safe to deploy and
customise for a client; they are not safe to embed in a proprietary product Globant resells.**
LGPL-3.0 makes OpenEduCat the more permissive of the two for linked-module work.

🔵 Evidence:
[`../evidence/grant-probe.2026-10-30-p552.tsv`](../evidence/grant-probe.2026-10-30-p552.tsv).

## 🆕 `p551` — `2026-10-30` — **🟢 THIS PAGE'S DENOMINATOR NOW CARRIES A RULE *REVISION*, WHICH IS WHAT `Gap 549-B` SAID IT NEEDED TO BE REPRODUCIBLE AT ALL. 🟢 THE ATTENDANCE LAYER GAINS THREE MIT-GRANTED FOUNDATIONS — AND TWO OF THEM CANNOT BE DEPLOYED IN EMEA AS WRITTEN.**

🔵 **`Gap 551-A` (six registrations lost), the `Gap 549-B` closure and this pass's retraction
are on [`../agents/top.md`](../agents/top.md#-p551--2026-10-30); the supply-channel finding
is on [`../agents/trending.md`](../agents/trending.md#-p551--2026-10-30).** This entry
carries this page's **denominator** and its **foundational additions**.

### 🟢 The denominator, stamped

🟢 **`Gap 549-B` asked that every derived figure carry its rule name *and* a revision**,
because `p546` and `p547` published **176** while `p543`–`p548` re-measure at **175** under
the rule's current revision — *"both figures are right; neither is reproducible without its
revision"*. 🟢 This page's figure now reads:

| page | at `p550` `HEAD` | **after this pass** | rule revision |
|---|---|---|---|
| `repos/foundations.md` | 176 | **179** | `pairs_in_table_rows_deduped@dcfa99c9666c` |

🟢 **The `+3` is this pass's three MIT attendance foundations, below — and the cell is edited
rather than announced**, which is `Gap 550-A`'s shelf rule 21 applied to this page's own
denominator.

🟢 Re-derive with [`../ingest/address-count.py`](../ingest/address-count.py); re-derive the
stamp with [`../ingest/rule-revision.py`](../ingest/rule-revision.py); check a carried stamp
with `--verify`, which exits **1** and says *"the figure is not wrong — it is not
reproducible under the current rule"*. 🔴 **The stamp does not cover the extraction regexes**
— `Gap 551-B`.

### 🟢 Three MIT foundations for a layer this page had thin

🟢 **Attendance is the one administrative substrate every school system needs and this page
carried almost nothing permissive for it** — `openSIS-Classic` (GPL), `rosariosis` (GPL) and
`OpenEduCat` (LGPL) all put a copyleft conversation in front of a client fork. These three
do not:

| repo | licence, read first-hand at the title block | signal | what it is, and what it is *for* here |
|---|---|---|---|
| [`kmhmubin/Face-Recognition-Attendance-System`](https://github.com/kmhmubin/Face-Recognition-Attendance-System) | 🟢 **MIT** — `LICENSE` **1 068 B**, `MIT License · Copyright (c) 2019 K.M.H.Mubin`, at `master` `0e87a9a7ded5` | **584★** · 203 forks · updated **`2026-10-28`** | Python/OpenCV roll-call: Haar-cascade detection, LBPH recognition, CSV register, `yagmail` notification. 🟢 **Seven years old and touched two days ago** — the maturity profile this page prefers over a new repo with the same star count. 🔴 **`Gap 551-C` applies** |
| [`aashishrai3799/Automated-Attendance-System-using-CNN`](https://github.com/aashishrai3799/Automated-Attendance-System-using-CNN) | 🟢 **MIT** — `LICENSE` **1 071 B**, `MIT License · Copyright (c) 2019 aashishrai3799`, at `master` `ed8ce0410055` | **127★** · 40 forks · updated `2026-09-17` | End-to-end TensorFlow CNN face identification. 🟢 The **model-training** half that the OpenCV repo does not have; the two compose rather than compete. 🔴 **`Gap 551-C` applies** |
| [`GeoCoderDev/SIASIS`](https://github.com/GeoCoderDev/SIASIS) | 🟢 **MIT** — `LICENSE` **1 084 B**, `MIT License · Copyright (c) 2024 Juan Manuel Chavez Saldaña`, at `master` `c38da88d30bd` | 🔴 stars **`UNREAD(screen-unindexed)`** — **`Gap 549-C` 3rd instance** | Next.js 14 + PostgreSQL (Neon) + Resend + Google Drive. 🟢 **The non-biometric alternative**, and the only one of the three with a **notification and escalation** layer: automatic alerts to guardians on detected tardiness patterns, Excel reports to Drive, bulk CSV intake. 🟢 **Voice-command and hotkey operation for blind users**, built in |

🔴 **The qualification that belongs on the row and not in a footnote.** The two best-starred
of the three are **biometric**, and this base carries — across six files — that **emotion
recognition in schools is prohibited under the EU AI Act since `2025-02-02`** and that
**Annex III point 3** makes education systems high-risk where they assess or monitor. Neither
repository has a retention policy, a template-storage boundary, an on-device constraint or a
human-confirm step. 🟢 **They are foundations, not products**, and the gap between the two is
exactly `Gap 551-C` — *granted, permissive, runnable, not deployable* — with recipe
**`P604`** on [`../compose/patterns.md`](../compose/patterns.md#-p551--2026-10-30) as the
mitigation path. 🟢 **`SIASIS` is the one of the three that carries no biometric at all**,
which is why it earns a row despite an unreadable star count.

🔴 **Four further addresses from the same channel are `UNRESOLVED-on-180-names`** —
[`AzeemIdrisi/QR-Attendance-System`](https://github.com/AzeemIdrisi/QR-Attendance-System),
[`HarryFoster1812/AttendEase`](https://github.com/HarryFoster1812/AttendEase),
[`gopi-c-k/smart-attendance-app`](https://github.com/gopi-c-k/smart-attendance-app),
[`sandeeep-prajapati/Vidra`](https://github.com/sandeeep-prajapati/Vidra). All four are
**LIVE** with resolved default branches. 🔵 `p517`'s rule holds: **absence on a name list is
not absence of a grant**, so they are recorded *unread* and are neither graded nor rejected.

## 🆕 `p550` — `2026-10-30` — **🟢 THE CANONICAL COUNTER RAN AND THIS PAGE IS `176`, NOT `175` — AND `p549` PREDICTED BOTH THE NUMBER AND THE REASON. 🟢 ONE FOUNDATIONAL ROW RE-ATTESTED EXACTLY, AND IT IS THE ROW THAT CAUGHT THIS PASS'S OWN INSTRUMENT LYING.**

🔵 **The velocity instrument, `Gap 550-A` and the full retraction are on
[`../agents/top.md`](../agents/top.md#-p550--2026-10-30).** This entry carries this
page's **denominator** and its **re-attestations**.

### 🟢 The denominator, from the instrument instead of from arithmetic

🟢 [`../ingest/address-count.py`](../ingest/address-count.py) **was not denied this
pass** — first time in eighteen passes, after seventeen denials by name. All four rules
reported, `2026-10-30`:

| Rule | `repos/foundations.md` |
|---|---|
| `markdown_link_text_is_owner_repo` | 99 |
| `pairs_anywhere_on_page_deduped` | 193 |
| 🟢 **`CANONICAL :: pairs_in_table_rows_deduped`** | 🟢 **176** |
| `table_data_rows` | 262 |

🔴 **`176` does not reproduce `p549`'s `175` — and that is `Gap 549-B` working, not
failing.** `p549` wrote that re-running *today's* rule over *yesterday's* bytes returns
175 where `p546`/`p547` correctly published **176**, because `p548` added `x` and `y` to
the rule's `PLACEHOLDER` set. 🟢 **The figure is correct under the rule it names, and the
rule's revision is what makes the two numbers comparable rather than contradictory.**
🔵 Every count on this page from here on carries `pairs_in_table_rows_deduped` and the
commit it was derived at, per `549-B`.

🔴 **`Gap 548-E` is still open and this pass makes it worse, as registered.** `176`
counts re-attestation rows and rejected candidates as "addresses". The
`shelf_addresses` / `documented_addresses` split remains **unbuilt**; named so the
number is not read as a shelf size.

### 🟢 `CAHLR/pyBKT` — re-attested exactly, and it earned its keep twice

| Row | This base published | 🟢 Exact, `p550` | Verdict |
|---|---|---|---|
| [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | **291** | **291** · **90 forks** · MIT · pushed `2026-10-28` | 🟢 **exact match** |

🟢 **And this row is the one that caught this pass's own instrument manufacturing a
defect.** Its description cell reads *"the same lab behind
[OATutor](https://github.com/CAHLR/OATutor)"*. `rev4` of this pass's velocity rule matched
**this** row for the address `CAHLR/OATutor`, took **pyBKT's 291**, compared it against
OATutor's own **274**, and reported that this base was publishing two figures for one
repository. 🔴 **It was not. The rule was wrong.** Both cells on this base are exactly
right: **pyBKT 291, OATutor 274**, measured independently.

🔵 **Registered as `Gap 550-D`: citation is not attribution.** Fixed as
`declared_star_cell/rev5` — the address must appear **before** the `Stars` column, in the
row's identity columns, not in its prose. 🟢 **This page is the reason the fix exists**,
because cross-referencing rows is precisely what makes it valuable: *"the same lab
behind…"* is the sentence that makes `pyBKT` legible next to `OATutor`, and any
instrument reading these pages must distinguish a row's **subject** from its
**citations**. 🔴 `rev4` would have mis-attributed a figure to **every** address this base
cross-references, and the richer the prose, the more wrong it would have got.

### 🟢 Knowledge tracing, re-stated with figures rather than adjectives

🟢 The knowledge-tracing stack on this page is the sector's best-evidenced foundational
layer, and all three rows now carry exact counters:

| Repo | Licence | 🟢 Exact, `p550` | Role |
|---|---|---|---|
| [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | MIT | 453 *(held, not re-measured this pass)* | Benchmark library for deep knowledge tracing; standard datasets and prediction scenarios |
| [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | MIT | 🟢 **291** · 90 forks | Bayesian Knowledge Tracing and extensions, C++ core, Berkeley CAHLR |
| [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | MIT | 🟢 **274** · 164 forks | The **tutor** that puts BKT in front of a learner — ReactJS/Firebase |

🔵 **The shape worth naming for an engagement:** these three are one lab's stack at three
altitudes — the **model library** (`pyBKT`), the **benchmark harness** (`pykt-toolkit`),
and the **deployed tutor** (`OATutor`) — all MIT, all from or adjacent to UC Berkeley.
🟢 **A mastery-estimation engagement does not need to choose between them**; it takes
`pyBKT` as the estimator, `pykt-toolkit` to justify the choice against baselines, and
`OATutor` as the reference integration. 🔴 **What none of them ships is the
prerequisite *graph*** — they infer mastery over a skill set that someone else must
declare, which is exactly the gap [`miuuyy/Clew`](https://github.com/miuuyy/Clew) fills
and is why it was shelved this pass.

### 🟢 Velocity now applies to this page's rows too

🟢 `Gap 549-E` is closed by
[`../compose/code/p550-star-velocity/`](../compose/code/p550-star-velocity/README.md),
which reads **this page's committed bytes** as a time series. Rows measured here:

| Repo | Observations | Series | Sustained |
|---|---|---|---|
| [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | 2 | `281 → 291` over 29 d | +0.3 ★/day |
| [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 133 | `265 → 274` over 29 d | +0.3 ★/day |

🔴 **`Gap 550-E`:** the series covers **15 addresses of this page's 176**. The instrument
costs roughly `addresses × commits × pages` `git show` calls and a 15-address run over 709
commits takes minutes, so a full-shelf sweep needs a **per-commit blob cache** before it is
affordable. 🔵 Named rather than left as an implied "all rows measured" — which is the
`Gap 544-E` defect class (a carried figure standing in for an unmeasured population).

### 🔴 What `p550` did NOT do on this page

- 🔴 **No new foundational repo was added.** The platform leg returned only held, copyleft
  systems; the one new platform (`ilios`, MIT) is a **product**, not a library, and is
  filed on [`../verticals/solutions.md`](../verticals/solutions.md#-p550--2026-10-30).
- 🔴 **`pykt-toolkit` was not re-measured.** Its `453` is carried from an earlier pass and
  is labelled as carried, not as exact.
- 🔴 **The 176 − 15 = 161 addresses on this page have no velocity series and no staleness
  check.** That is the honest size of `Gap 550-E`.

## 🆕 `p549` — **the denominator is `175` and it was `175` at every one of the last six commits — but only under *this* rule revision. `p546` and `p547` were right too, under theirs.**

🟢 **Re-derived inline from [`../ingest/address-count.py`](../ingest/address-count.py)'s own
source** — the script is **denied by name** (`Code from External`, **seventeenth denial in
eighteen passes**) but **reading** it is not denied, so the canonical rule was reproduced
from the text rather than from recollection:

| Page | `p543` | `p544` | `p545` | `p546` | `p547` | `p548` |
|---|---|---|---|---|---|---|
| `repos/foundations.md` | **175** | **175** | **175** | **175** | **175** | **175** |
| [`../agents/top.md`](../agents/top.md) | 118 | 122 | 123 | 123 | 124 | 125 |

🟢 **Row 2 reproduces `p548`'s published table cell for cell.** 🔴 **Row 1 does not**, and the
reason is not a defect in `p546`, `p547` or `p548`:

🔵 `p548` added `x` and `y` to the rule's `PLACEHOLDER` set — its own fix for `Gap 547-I`
recurring on this page. 🟢 So re-running **today's** rule over **yesterday's** bytes returns
`175` where `p546` and `p547` correctly published `176` under the rule **of their day**.
🟢 **Both figures are right. Neither is reproducible without its rule revision.**

🔴 **Registered as `Gap 549-B`:** every derived count on this base must carry the rule
**name** *and* its **revision**, because the history tables on
[`../agents/trending.md`](../agents/trending.md) and on this page currently mix revisions and
so invite exactly the dispute `547-F` and `548-E` spent two passes resolving. 🔵 The cheap
form is a rule hash: `pairs_in_table_rows_deduped@<sha of PLACEHOLDER+NOT_A_REPO>`.

### 🔴 A retraction `p549` owes against itself, caught inside the same pass

🔴 **This pass's first count of [`../agents/top.md`](../agents/top.md) was `124`. It is
`125`.** The inline re-implementation selected table rows with `^|`, where the canonical rule
selects them with `ln.lstrip().startswith("|")` — so **every indented table row was dropped**,
uniformly, across every commit measured. 🟢 **Fixed by reading the script instead of assuming
it**, which is the whole lesson: **the gate stops execution, not comprehension.**

### 🟢 One new foundational address

| Repo | Grant | Why it is foundational rather than an agent |
|---|---|---|
| 🆕 [`PKulal/LMS`](https://github.com/PKulal/LMS) | 🟢 **Apache-2.0**, root `LICENSE` 11 362 B complete title block — **and 762 of 854 tracked files carrying in-header `SPDX-License-Identifier`**, declared to **REUSE spec 3.3** via `REUSE.toml` / `.reuse/` / `LICENSES/` / `NOTICE` | A **multi-tenant LMS platform**, not a tutor: Django 6 + DRF + PostgreSQL + React 19 + a Flutter client, with `accounts` / `organizations` / `rbac` / `curriculum` / `analytics` / `gamification` as separable apps. 🟢 **It is the most rigorously granted artefact on this base** — the grant is machine-checkable with `reuse lint`, which no other row here supports. 🔴 **Zero git tags**, so pin a commit. 🔴 **Unindexed by GitHub search** (`Gap 549-C`), so no star counter exists on any open channel — recorded **UNMEASURABLE**, not `0`. Full attestation on [`../verticals/solutions.md`](../verticals/solutions.md) |

🔵 **Counting note, per `544-E`:** this section adds that one address plus the addresses in
the tables above it, so the page's `documented` figure moves while its `shelf` figure moves
by **one**. 🟢 That divergence is `Gap 548-E`, and it is now visible on three pages in one
pass — which is the argument for `548-E`'s two-figure remedy rather than its marker remedy.

## 🆕 `p548` — **this page's denominator was **176** for one pass because the table explaining the rule *matched the rule*. It is **175**, and `p546` was right all along**

🟢 **Re-derived with the canonical rule after the fix: `repos/foundations.md` carries
**175** addresses.** 🔴 `p547` published **176** and treated the `+1` over `p546`'s **175**
as an unexplained rule disagreement (`Gap 547-F`). 🟢 **It was not a disagreement. It was
one phantom address, and this page had written it itself.**

### 🔴 The phantom, named

🔴 In the `Gap 546-B` table below, `p546` documented its five extraction rules and spelled
the pattern as **`github.com/X/Y`** — inside **table rows**. 🔴 The canonical rule extracts
`github.com/⟨owner⟩/⟨repo⟩` pairs **from table rows**, and `X` is not in
[`../ingest/address-count.py`](../ingest/address-count.py)'s `PLACEHOLDER` set, so **`X/Y`
was compiled as a real repository address.**

🟢 **Git dates it exactly.** The canonical rule, same code, over the committed page:

| `p545` commit | `p546` commit | `p547` commit | `p548` worktree |
|---|---|---|---|
| **175** | 🔴 **176** | 176 | 🟢 **175** |

🔵 **The increment landed in `p546`'s own commit — the commit that published `175`.** 🟢 So
`p546` measured the page correctly and then inflated it by one in the act of explaining
how. 🔴 `p547` read the inflated page and recorded the difference as a defect in the row
definition; there was never a row definition at issue.

### 🟢 Fixed in two places, because either alone regresses

🟢 Exactly as `Gap 547-I` prescribed when it caught the identical defect on
[`../agents/top.md`](../agents/top.md):

1. 🟢 **On this page** — the rule table now writes `github.com/⟨owner⟩/⟨repo⟩` with bracket
   glyphs, which the extractor cannot match.
2. 🟢 **In the code** — single-letter metavariables (`x`, `y`, `z`, `n`, `a`, `b`) plus
   `test`, `demo` and `placeholder` are added to `PLACEHOLDER` in
   [`../ingest/address-count.py`](../ingest/address-count.py), with the reason in a comment
   beside them.

🔵 **Third instance on this base of the `| Nombre | Repo | Licencia |` class — a header or
example row compiled as data — and every one of the three was committed by prose
*documenting* an extraction rule, never by a real data row.** 🟢 Stated as a rule for later
passes: **documentation of an extraction rule must never be placed where that rule can
match it.**

### 🟢 One address on this page is now live for a different reason than it was

🟡 [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) (347★, 288 forks,
pushed **2026-10-26**) was carried across this base as **⛔ no grant**. 🟢 **`p548` read the
payload: GPL-2.0.** The complete GNU GPL v2 sits at `docs/License.txt` — **17 286 B**,
`sha256 224ac3d403e3…b8ba` — declared in `README.md` **L49–51**, with root `LICENSE`
returning **404**. 🔴 Every probe this base ran against it (5 filenames at `p529`, **159
variants** at `p547`) was **root-scoped**. 🔵 Attestation on
[`../verticals/solutions.md`](../verticals/solutions.md); the recipe is `P601` on
[`../compose/patterns.md`](../compose/patterns.md).

## 🆕 `p547` — **`Gap 546-B` is CLOSED: this page's denominator is reproducible, by running [`ingest/address-count.py`](../ingest/address-count.py) rather than by trusting a sentence**

🔴 **The defect, as `p546` stated it.** `p545` published *"162 shelf addresses"* for this
page. `p546` tried five extraction rules and got **100 / 169 / 175 / 191 / 191** — *"none of
the five yields 162 … it is a claim that **nobody can tell**."*

🟢 **The number this page now carries, with its rule attached:**

| | |
|---|---|
| **Addresses on `repos/foundations.md`** | 🟢 **176** (at `p547`, after this pass's edits) |
| Rule | `pairs_in_table_rows_deduped` — every GitHub `⟨owner⟩/⟨repo⟩` pair inside a table row, case-folded, trailing `.git` stripped, non-repository and placeholder owners excluded. 🔴 **The rule is written here with bracket glyphs on purpose:** spelling the literal pattern inside a table row makes the row itself match it, and the first draft of this section did exactly that — see `Gap 547-I` |
| Where the rule lives | 🟢 [`ingest/address-count.py`](../ingest/address-count.py), designated `CANONICAL` **in the source** |
| How to disagree with it | 🟢 `python3 ingest/address-count.py repos/foundations.md` |
| Shelf **rows** (`Gap 544-E`, still derivable) | **156** |

🔴 **It disagrees with `p546`'s 175 by one, and with `p546`'s `agents/top.md` figure of 98
by twenty-five.** 🔵 **Neither delta is offered as a correction.** `p546` described its rule
in prose; this pass's rule is that prose plus three decisions the prose leaves open
(case-folding, `.git` stripping, the non-repository owner set). 🔴 **The `+25` is too large
to be those three**, so the two row definitions genuinely differ and **`p547` does not yet
know where** — registered as `Gap 547-F`, to be settled by diffing the extracted **address
sets** rather than their counts. 🟢 **The gap closes anyway**, because what `546-B` asked
for was not a better figure but a figure anyone can re-derive and contest in one command.

🔵 **Full instrument record, the negative controls and the retired `github.com` read
channel are on [`trending.md`](trending.md#-p547--2026-10-30).**

🔴 **No new foundational repository was shelved at `p547`.** The English repo and vertical
legs returned **OpenEduCat, RosarioSIS, openSIS, ERPNext and SchoolTool** — every one
already held. The six new systems this pass found are **agents**, they are on
[`../agents/trending.md`](../agents/trending.md#-p547--2026-10-30), and **five of the six
carry no grant Globant can build on**.

🟡 **One disagreement on this page's own subject matter is left OPEN rather than resolved
in either direction:** the English vertical leg returned **openSIS** as GPL in one source
and **Apache-2.0** in a comparison table. 🔴 `p547` did not probe it first-hand and so
records **neither value**. 🔵 It is named because a comparison table is exactly the channel
`p455` proved unreliable for licences, and the next pass should read `OS4ED/openSIS-Classic`
at `HEAD` instead of re-reading the table.

## 🆕 `p546` — every address on this page is now **dated**, and the page's own denominator is **not reproducible**

🟢 **`Gap 544-C` closed.** All **175** addresses extracted from this page's table rows
were dated by blobless bare clone — **175/175, zero failures, 39 seconds**. Method and
negative controls are on [`trending.md`](trending.md#-p546--2026-10-30); the field itself
is one row per address in
[`../evidence/staleness-foundations.2026-10-30-p546.tsv`](../evidence/staleness-foundations.2026-10-30-p546.tsv).

🔴 **The field's first result is about this page: 28 of 175 addresses — 16.0 % — have had
no commit in over a year, and six have had none in over six years.** `p545` reported
`162/162 LIVE` and read it as slow decay. 🔵 **`LIVE` meant the address resolves. It did
not mean anyone is there.**

### 🔴 The dead tail, named rather than summarised

| Address | Last commit | Age |
|---|---|---|
| [`Apereo-Learning-Analytics-Initiative/lap-sakai-extractor`](https://github.com/Apereo-Learning-Analytics-Initiative/lap-sakai-extractor) | `2014-12-02` | 🔴 **11.9 y** |
| [`Apereo-Learning-Analytics-Initiative/LearningAnalyticsProcessor`](https://github.com/Apereo-Learning-Analytics-Initiative/LearningAnalyticsProcessor) | `2016-05-04` | 🔴 **10.5 y** |
| [`jupyterhub/jupyterhub-tutorial`](https://github.com/jupyterhub/jupyterhub-tutorial) | `2018-02-01` | 🔴 8.7 y |
| [`Apereo-Learning-Analytics-Initiative/OpenLRW`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW) | `2020-02-06` | 🔴 6.7 y |
| [`Apereo-Learning-Analytics-Initiative/OpenDashboard-legacy`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenDashboard-legacy) | `2020-02-17` | 🔴 6.7 y |
| [`Apereo-Learning-Analytics-Initiative/OpenDashboard-api`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenDashboard-api) | `2020-03-09` | 🔴 6.6 y |
| [`KualiCo/rice`](https://github.com/KualiCo/rice) | `2020-07-01` | 🔴 6.3 y |
| [`dougpenny/SwiftyPSCore`](https://github.com/dougpenny/SwiftyPSCore) | `2022-03-22` | 🔴 4.6 y |
| [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | `2022-11-21` | 🔴 3.9 y |
| [`jdolny/OneRoster.NET`](https://github.com/jdolny/OneRoster.NET) ≡ [`theopenem/OneRoster.NET`](https://github.com/theopenem/OneRoster.NET) | `2023-10-13` | 🔴 3.0 y *(both halves of `p545`'s alias pair)* |
| [`jupyterhub/wrapspawner`](https://github.com/jupyterhub/wrapspawner) | `2024-04-08` | 🔴 2.6 y |
| [`open-spaced-repetition/fsrs.js`](https://github.com/open-spaced-repetition/fsrs.js) | `2024-04-10` | 🔴 2.6 y |
| [`classroom-resources/autograding-python-grader`](https://github.com/classroom-resources/autograding-python-grader) · [`…/autograding-io-grader`](https://github.com/classroom-resources/autograding-io-grader) | `2024-05-01` | 🔴 2.5 y |

🔴 **`Apereo-Learning-Analytics-Initiative` is five of those rows and the whole family is
dead** — the learning-analytics layer this page offers is the layer a studio must not
start from. 🟢 **`p545` found the `OneRoster.NET` alias pair; `p546` adds that both halves
have been still for three years**, so the alias is not merely redundant, it is redundant
*and* abandoned.

🟡 **Two distinctions the age column must not flatten:**

- 🟡 [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec) (**1.3 y**) is a **ratified
  specification**. A spec that stops changing is finished, not abandoned. 🔴 Its
  **reference implementation** [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS)
  (**1.4 y**) is running code, and that is a liability rather than a feature.
- 🟡 [`jupyterhub/jupyterhub-tutorial`](https://github.com/jupyterhub/jupyterhub-tutorial)
  (**8.7 y**) is **teaching material**, not a dependency. The age is still worth stating —
  an eight-year-old tutorial for a project that ships monthly is wrong, not merely old.

🟢 **And the live majority is the headline this page should actually lead with: 105 of 175
addresses — 60 % — committed within the last 30 days, 76 of them within 7 days.** The
succession table on [`trending.md`](trending.md#-p546--2026-10-30) names the maintained
replacement for every stale standards implementation above.

### 🔴 `Gap 546-B` — this page's address count is not reproducible

`Gap 544-E` made the **row** count derivable (**156** `SHELF` rows). 🔴 **The address count
reported beside it — `162` — is not derivable by any rule `p546` could construct**, and it
is the denominator of `p545`'s `162/162 LIVE`:

| Extraction rule | Addresses |
|---|---|
| markdown link **text** is `owner/repo` | **100** |
| one address per table data row (row subjects) | **169** |
| 🟢 **all `github.com/⟨owner⟩/⟨repo⟩` pairs inside table data rows, deduped** — `p546`'s rule | 🟢 **175** |
| all `github.com/⟨owner⟩/⟨repo⟩` pairs anywhere on the page, deduped | **191** |
| …excluding non-repository owner paths (`topics`, `orgs`, …) | **191** |
| 🔴 `p545` reported | 🔴 **162** |

🔵 **This is not a claim that `162` was wrong — it is a claim that nobody can check it**,
which on a derived figure is `544-E`'s defect one level up. 🟢 **`p546` states its rule
with its number**, and every figure on this page's `p546` sections uses **175**.

# Foundational Education Repos

**Pass `p545` · 2026-10-30.** Load-bearing systems an education engagement is
likely to inherit, extend or integrate against — not agents (those are in
[`../agents/top.md`](../agents/top.md)), but the platforms, standards and
toolkits the agents must live beside.

🟢 **derived shelf rows: **156** · distinct addresses: **162** · distinct systems: **161**.**
All three are produced by
[`../ingest/derive-foundations.py`](../ingest/derive-foundations.py) from the tables
themselves against a declared disposition per table
([`../ingest/foundations-disposition.tsv`](../ingest/foundations-disposition.tsv)) and a
declared alias relation ([`../ingest/foundations-alias.tsv`](../ingest/foundations-alias.tsv)),
and the gate fails if this sentence and the tables disagree. 🔵 **This is the first total
this page has been allowed to quote**, and the header's standing prohibition on quoting one
is lifted with it. 🔵 **Three quantities, never conflated:** a *row* may name an upstream
and its fork; an *address* may be an alias of another; a *system* is what an engagement
actually inherits.

🟢 **And all 162 were probed this pass, not assumed: `162 / 162 LIVE`**, zero dead, zero
private ([`../evidence/shelf-alias-branch-sweep.2026-10-30-p545.tsv`](../evidence/shelf-alias-branch-sweep.2026-10-30-p545.tsv)).
🔵 Worth stating beside `p539`'s backlog figure of **96.2 % live**: **a curated shelf decays
more slowly than the queue it was drawn from**, which is the first direct evidence this base
has that curation is doing work.

🔴 **`p544` filed no new row here, and the reason is worth more than a row would
have been.** The four-region sweep and four language legs returned **no
foundational system this page does not already hold**. 🟢 **The one new address
measured — [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library)
— was deliberately NOT filed**, and the measurement says why: it is Apache-2.0 at
**`11 343` B, `sha256₁₂ 78b49eeaddbf`**, which is **byte- and digest-identical**
to [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library),
already on this page. 🔵 **The grant is inherited unchanged across the fork — under
a different filename (`LICENSE` vs `LICENSE.md`), which is exactly why the probe
walks a filename ladder and a single-filename probe would have read the fork as
ungranted.** 🔴 The spec body's original is frozen at HEAD `3a192de99f37`, last
commit **2020-06-03** — the same HEAD `p390` recorded — while the fork ships
**v6.4.4 (2026-09-23)**. Neither is archived. 🟢 **Identical grant, five years of
divergence in maintenance: the maintained fork is the right row and a second
address for a held grant is a duplicate, not supply** (registered alias relation
`397-F`).

### 🟢 `Gap 544-E` / `Gap 534-E` — CLOSED at `p545`, and the carried number was wrong by more than 2×

🔴 **The figure this header carried for eleven passes — *"seventy-two"* — was never a
count. It was pass arithmetic** (*"fifty-eight + eleven (`p533`) + three (`p534`)"*),
**frozen at `p534`, while `p535`…`p543` filed rows below it and none of them touched the
sentence.** 🟢 **Derived from the tables, the figure is `156`.** The carried number
understated this page by **84 rows**.

🔵 **Why it could not be derived before, and what changed.** `p544`'s
[`../ingest/derive-counts.sh`](../ingest/derive-counts.sh) found **175 distinct GitHub
addresses** in this page's table rows and **abstained**, correctly: several sections here
are **censuses**, and a census row was never a load-bearing-system row. `544-E` asked for
**a row-level disposition marker**. 🟡 **Measured at `p545`, the unit is wrong by one
level:** the page holds **180 data rows in 31 tables**, and **no table mixes dispositions**
— disposition is a property of the *table*. A per-row marker would have been **180 edits
encoding 31 facts**, each one a place to drift. 🟢 **Declared per table instead**, in
[`../ingest/foundations-disposition.tsv`](../ingest/foundations-disposition.tsv), and
derived by [`../ingest/derive-foundations.py`](../ingest/derive-foundations.py):

| Disposition | Rows | What it means |
|---|---|---|
| 🟢 **`SHELF`** | **156** | Load-bearing systems this page files. **These, and only these, are counted.** |
| 🔴 `CENSUS` | 13 | The Moodle MCP census — a 13-row sample of **222** addresses. An enumeration of a population, not supply this page filed. |
| 🔴 `METRIC` | 5 | `p539`'s backlog measurement (LIVE/DEAD/grant-gate rates). Carries no repository rows at all. |
| 🔴 `SUMMARY` | 7 | The licence-band map (4) and `p534`'s three-platform refutation (3) — both **restate rows filed elsewhere on this page**, so counting them double-counts. |
| | **180** | every data row on the page, accounted for |

🟢 **An undeclared table is an error, not a default:** the gate exits `2` and names it, so a
section added by a later pass **cannot** silently re-break the count. 🟢 **And the
declarations are re-resolved by heading *text* at run time**, not by the line numbers the
manifest is written with, so ordinary editing does not re-point a declaration at a
different section.

🔴 **One thing this closure does NOT deliver, stated so it is not read into it.** 🔴 **The
gate did not run under `make hooks`**, which was refused `Code from External` for the
**twelfth time in thirteen passes**; it was run directly. **A green gate that the
gate-runner never ran is evidence, not attestation** (`Gap 545-D`).

🟢 **Three negative controls were run, because a gate that has never failed is not known to
work:** the header figure falsified `156→157` → `RED`, exit `1`; a declared table deleted
from the manifest → `RED`, names `## Platform cores`, exit `2`; a manifest key renamed off
the page → `RED`, exit `2`. Restored, the gate returns `GREEN`, exit `0`.

### 🟢 `Gap 545-C` — named and closed in the same pass, and the sweep paid for itself twice

🔵 **`544-D` asks that a prescription be `grep -rF`'d against `ingest/` before it is
registered. Applied here, it changed the outcome:** the instrument `545-C` would have asked
for — [`../ingest/alias-sweep.sh`](../ingest/alias-sweep.sh) — **already existed since
`p543`** and had simply never been run over this page. 🟢 **So the gap was closed rather
than registered.** All 162 shelf addresses were swept with `git ls-remote --symref`:

| Result | Figure |
|---|---|
| 🟢 LIVE | **162 / 162 — 100 %** |
| 🔴 DEAD / PRIVATE | **0** |
| 🟡 Alias pairs (identical HEAD sha) | **1** — [`jdolny/OneRoster.NET`](https://github.com/jdolny/OneRoster.NET) ≡ [`theopenem/OneRoster.NET`](https://github.com/theopenem/OneRoster.NET), both `4f96365d3108` |
| 🟢 **Distinct systems** | **161** |

🔴 **And the sweep's second result is the one an engagement will feel: only `94` of `162`
shelf repositories default to `main` — `42 %` do not.**

| Default branch | Count |
|---|---|
| `main` | 94 |
| `master` | 46 |
| `develop` | 12 |
| `dev` | 2 |
| 🔴 one-offs | 8 — `v4.0.x-develop` · `release_11` · `release` · `development` · `mobile` · `java11` · `2.12` · `19.0` |

🟢 **This independently confirms `p543`'s closure of `542-B` as WRONG REMEDY and
strengthens it.** `542-B` proposed a fixed branch list and `p543` measured it failing on
**19 %** of the shelf; measured here against *default branches actually served*, a fixed
list fails on **42 %**, and **8 of those branches (`v4.0.x-develop`, `java11`, `2.12`,
`19.0`) are values no list would ever guess.** 🔵 **The rule for any probe on this base:
resolve the default branch, never enumerate candidates.**

> 🟢 **`p530` adds a layer this file did not have: the e-learning standards
> implementations.** Twelve repos — SCORM runtimes, xAPI learning record stores,
> LTI frameworks, knowledge-tracing libraries and autograders. 🔴 **None of them
> is new to this base.** Every one was already in its append-only history, some
> across twenty passes, and none had ever reached a curated file. They surfaced
> only once `Gap 529-A`'s index existed
> ([`../ingest/address-ledger.py`](../ingest/address-ledger.py)).
>
> 🔵 **Why this layer decides engagements.** An institution does not buy a tutor;
> it buys something that plugs into the LMS it already runs. These twelve are how
> you plug in, and **eleven of the twelve are MIT, Apache-2.0 or BSD** — against
> a platform-core layer below that is almost entirely copyleft. 🔴 **The
> permissive surface of this sector is the integration layer, not the
> platforms.**
>
> 🔴 **One retrieval failure worth naming, because the search channel stated it
> as a capability gap.** Asked for an open-source grader this pass, generic
> search replied *"I found no open-source agent that grades students."* This base
> already owned **three permissive autograders totalling 2 337★**. The gap was
> never in the world.

> 🆕 **`p529` changed one section of this file and nothing else — the same
> section, again, and this time the correction runs the other way.** The GitHub
> search API became reachable this pass (see
> [`../agents/top.md`](../agents/top.md)), and it reports **`total_count: 222`**
> for the Moodle MCP field. `p528`'s census of eleven was not a census; it was a
> sample of what a search engine surfaced. 🔴 **The ceiling, the star total and
> the licence spread are all corrected below.** The platform-core and
> administration rows above were not re-read this pass except where the API
> corroborated them — `fsrs4anki` (**MIT, 4,119★**), `openeducat_erp` (**LGPL**,
> 900★ / **782 forks**) and `rosariosis` (**GPL-2.0**, 648★) all **confirmed**.

> 🆕 **`p528` changed one section of this file and nothing else.** The Moodle MCP
> census below was re-probed from scratch — existence first, then the licence
> file's title block — and `p527`'s reading of that field ("roughly three real
> codebases") is **corrected to eleven**. The platform-core rows were not
> re-read this pass and carry `p527`'s verification; their dates and digests are
> `p527`'s, not this pass's.

> **Every licence in this file was re-read this pass from the licence file's own
> title block**, fetched from `raw.githubusercontent.com` (reachable, while
> `github.com` and `api.github.com` return HTTP 403 through the session proxy).
> Star counts remain rounded page values. This changed one cell, and it was the
> cell `p526` flagged red — see the Frappe Education row.

> **Licence reality for this sector, stated plainly and confirmed again:** the
> mainstream education platforms are **copyleft**, not permissive. Moodle is
> GPL-3.0, Open edX and Canvas are AGPL-3.0. A targeted search for a mainstream
> Apache/MIT LMS returned none. This is not a gap in the research — it is the
> shape of the market, and it drives the architecture: **build permissive agents
> that integrate across a process or network boundary** (LTI, xAPI, REST, MCP)
> rather than forking an AGPL core and inheriting its obligations.

## 🆕 `p543` — the teaching-corpus layer gains two rows, and one of them pays a 190-mention promotion debt

🔵 **Why these belong here and not on the agent shelf.** A course corpus is not
an agent: it is the **curriculum substrate** an engagement reuses when the
client's ask is capability-building rather than a deployed tutor. This base
already holds `ocademy-ai/machine-learning` and `rasbt/LLMs-from-scratch` in
that layer; these two extend it, and one of them extends it **in a language
other than English**, which no row in this layer did before.

| Repo | Licence, read as bytes | Scale | What it is | Region |
|---|---|---|---|---|
| [`rohitg00/ai-engineering-from-scratch`](https://github.com/rohitg00/ai-engineering-from-scratch) | **MIT** (holder `Rohit Ghumare`) | ~75k★ per secondary sources, **not read first-hand this pass** | End-to-end AI-engineering curriculum — build, train and deploy — the English upstream of the row below. | **Global** |
| [`kmkarakaya/btk_rag_bot_egitimi`](https://github.com/kmkarakaya/btk_rag_bot_egitimi) | **MIT**, `LICENSE` @`main`, **1 071 B** | **20★, 12 forks, 43 commits** | Turkish course corpus for **BTK** (Türkiye's ICT authority), course code **514**: *"Erişim Destekli Üretim (RAG) Tabanlı Sohbet Botları"* — **9 h 22 m, 9 sections, 55 lessons**, Colab notebooks, Gemini API, Gradio front ends. A complete, licensed, state-authority RAG curriculum. | **EMEA** (Türkiye) |
| [`komunite/ai-engineering`](https://github.com/komunite/ai-engineering) | **MIT**, `LICENSE` @`main`, **1 070 B**, holder **`Rohit Ghumare`** — *the upstream's holder, not this repo's owner* | **8★, 1 fork, 1 147 commits** | 🟡 **Turkish localisation, and labelled as one.** 435 lessons / 20 phases / ~320 h, declared by GitHub as *"forked from rohitg00/ai-engineering-from-scratch"*. HEAD `4f6cbe73a12f` vs upstream `fe6c657dfb8d` — **diverged, not an alias.** | **EMEA** (Türkiye) |

🔴 **The first row is the finding, and it is a promotion-debt finding, not a
discovery one.** `rohitg00/ai-engineering-from-scratch` appears **190 times in
this base's trending history and zero times on any curated page** — graded
`HISTORY` by [`../ingest/claim-role.sh`](../ingest/claim-role.sh), built this
pass. 🟢 **`p543` found it only because a Turkish fork of it walked in the
front door**, which is `Gap 529-A`'s debt reproducing itself a third way: p541
found it in an `UNKNOWN` residue, p542 found it on the regional legs, and p543
found it **by following a localisation back to an upstream nobody had filed.**
🔵 Its star figure is carried from secondary sources and marked as such — this
pass read its **grant** first-hand and its **traction** not at all.

🟢 **The localisation row earns its place for a reason beyond completeness.**
It is this base's first measured instance of **an education curriculum being
translated rather than re-invented**, and that is the shape an EMEA
capability-building engagement actually takes: the pedagogy is upstream, the
**language and the institutional framing** are the local work. 1 147 commits
is not a translation pass, it is a maintained fork.

## 🆕 `p542` — one framework row off the French leg, and the Intel education suite read down to its components

🟢 **One row filed.** [`Intelligent-Internet/ii-agent`](https://github.com/Intelligent-Internet/ii-agent)
was **absent from this base entirely** — not in trending history, not on a
live page — and it arrived on the **French** leg, which is the clearest single
demonstration of `p542`'s corpus finding on
[`../agents/trending.md`](../agents/trending.md#-p542--2026-10-30).

| Repo | Licence (read as bytes) | Stars | Region (origin) | Why it is load-bearing here |
|---|---|---|---|---|
| 🆕 [`Intelligent-Internet/ii-agent`](https://github.com/Intelligent-Internet/ii-agent) | 🟢 **Apache-2.0** — `LICENSE` @`main`, **11 357 B**, canonical title block `Apache License / Version 2.0, January 2004` | **3.4k** · 524 forks | 🟡 Global — organisation `Intelligent-Internet`; country not stated on the page | *"II-Agent: a new open-source framework to build and deploy intelligent agents."* 156 commits. 🔵 **Filed as a foundation, not an agent, and the distinction is the point:** it is general agent infrastructure with **no education semantics at all**, which is precisely what an engagement wants underneath a tutor — the education-specific repos on this base are mostly *applications*, and swapping an application is expensive. **Apache-2.0 with its patent grant** puts it in the small set this base can hand a client without a licence conversation. ⚠️ **Not education-validated:** nothing on its page mentions teaching, tutoring or learners, so it is a substrate candidate on licence and generality, and **no pedagogy claim is made for it here.** |

### 🔵 `p542` — `open-edge-platform/education-ai-suite`, read down to its components

This base has carried the row since `p533` on licence and star count alone.
Read first-hand this pass, it is more actionable than its **2 stars** suggest,
and the shape of its numbers is the reason:

- **2 stars against 14 forks.** 🟢 A forks-to-stars ratio **above 1** is the
  signature of a repo being *derived from* rather than *bookmarked* — the
  inverse of the entire rest of this page — and `p540` built a forks-per-star
  ranking precisely to find this shape. **481 commits** behind it.
- **Named components, as the tree lists them:** `ai-teaching-assistant`,
  `smart-classroom`, `teacher-assistant-claw-demo`, `utils/flutter`. 🔵 The
  README's two applications are **Smart Classroom** — *"an extensible framework
  for processing, analyzing, and summarizing classroom sessions"*, with
  classroom statistics, student re-identification and classroom summaries — and
  **Teaching Assistant**, *"voice-first assistance in studying"* for
  self-directed learning.
- **Runtime:** audio and video pipelines *"accelerated with the OpenVINO™
  toolkit"*, targeting Intel CPUs, integrated GPUs and **NPUs**. 🟢 That makes
  it the only artefact on this page that is **on-premise by construction** —
  which is the EMEA data-residency and LATAM connectivity answer, in hardware
  rather than in policy.
- ⚠️ **Its own disclaimer, carried verbatim:** the applications are *"intended
  for reference and demonstration, not production."* It is a starting point and
  a benchmark harness, **not a deployable product**, and no pattern on this
  base should imply otherwise.
- 🔴 **One correction to how it is addressed.** The parent monorepo
  [`open-edge-platform/edge-ai-suites`](https://github.com/open-edge-platform/edge-ai-suites)
  (Apache-2.0, `LICENSE` @`main` **11 351 B**, 140★ / **170 forks**) is
  **absent from this base**, and it does **not** contain the education suite —
  its README states the Education AI Suite *"is developed in its own
  repository"*. 🔵 Worth knowing beyond this KB: the same monorepo carries
  **Metro, Manufacturing, Retail, Robotics, Health and Life Sciences, and
  Federal and Aerospace** AI suites under one Apache-2.0 grant, so five of
  Globant's other industry KBs have a verified, permissive reference body
  sitting at an address none of them hold.

### 🔴 `p542` — the probe shape that lost a grant, stated here because it is this page's risk too

[`ocademy-ai/machine-learning`](https://github.com/ocademy-ai/machine-learning)
has **two** root grants — `LICENSE-CODE` (MIT, 1 122 B) and `LICENSE-TEXT`
(CC-BY-4.0, 18 649 B) — and **nothing at `LICENSE`**. Twelve probes across
`LICENSE`/`.md`/`.txt`/`COPYING` × `main`/`master` return 404. 🟢 **Adding
`LICENSE-CODE` and `LICENSE-TEXT` to the probe surface is the whole fix.**
🔴 **The exposure is concentrated on this page rather than the agent shelf,**
because split-by-material-type grants are what *courseware and standards
bodies* use, and that is what a foundations page collects. **Every "no grant
found" verdict on a content-bearing repo here should be re-read as "not yet
probed".** Full working in
[`../agents/top.md`](../agents/top.md#-p542--the-licence-probes-shape-produced-one-false-negative-and-one-unnamed-grant-and-both-are-fixable).


## 🆕 `p540` — six rows off the gate-to-600, and the first forks-per-star ranking this base has run

🟢 **`Gap 539-B` asked for exactly this:** *"run the grant gate to 600 and rank
the permissive residue by forks-per-star."* Both halves delivered. 450 further
`LIVE` backlog addresses were probed at their resolved default branch (**600 of
3 869 now gated**; 3 269 remain), and the permissive residue was ranked.
Every row below was then read first-hand on `github.com` for its star and fork
counts — none is from memory, and none is gate-attested, because `make hooks`
was denied again (`Gap 540-E`).

| Repo | Licence | Stars · forks | **f/★** | Why it is foundational |
|---|---|---|---|---|
| [dspace/dspace](https://github.com/dspace/dspace) | 🟢 BSD-3-Clause | 1.1k · **1.5k** | 🟢 **1.364** | *"(Official) The DSpace digital asset management system that powers your Institutional Repository."* **More forks than stars** — the strongest institutional signal this base has measured. Every university that runs DSpace runs *its own* DSpace, which is what the ratio detects. The repository layer is where theses, datasets and OER already live, so it is the corpus an institutional RAG grounds on **before** anyone builds a tutor. |
| [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) | 🟢 BSD-3-Clause | 8.4k · 2.1k | 0.250 | *"Multi-user server for Jupyter notebooks."* 🟢 **`Gap 539-D` closed by this row** — named in **44** of this base's files since `p531` and never carrying a measured star count until now. The standard way an institution gives every student an isolated, resourced compute environment; the substrate under every "AI teaching assistant in a notebook" pattern on [`../compose/patterns.md`](../compose/patterns.md). |
| [ucfopen/canvasapi](https://github.com/ucfopen/canvasapi) | 🟢 MIT | 681 · 192 | 0.282 | *"Python API wrapper for Instructure's Canvas LMS. Easily manage courses, users, gradebooks, and more."* Maintained by the University of Central Florida. Canvas itself is AGPL-3.0, so this is the **process-boundary** route this file's licence rule prescribes: integrate across the API, do not fork the core. 🟡 **Default branch is `develop`**, not `main` or `master` — pin accordingly. |
| [yetanalytics/xapipe](https://github.com/yetanalytics/xapipe) | 🟢 Apache-2.0 | 17 · 9 | 0.529 | *"LRSPipe is an xAPI Statement forwarding/middleware process governed directly by xAPI Profiles."* The piece between a Learning Record Store and everything downstream: filter, transform and forward learner statements under a declared Profile rather than ad-hoc code. 🟢 Completes the xAPI leg `learnmcp-xapi` opened on the agent shelf — that one *writes* statements, this one *routes* them. 🔴 17★: small, and the Profile governance is the reason to take it, not the community. |
| [EducationalTestingService/skll](https://github.com/EducationalTestingService/skll) | 🟢 BSD-3-Clause | 561 · 69 | 0.123 | *"SciKit-Learn Laboratory (SKLL) makes it easy to run machine learning experiments."* From **Educational Testing Service** — the organisation behind TOEFL and the GRE. Configuration-driven experiment running with the reproducibility discipline assessment work demands; the pairing for the efficacy layer `p535` filed. 🟡 Graded `UNKNOWN` by the title gate because its payload reads *"New BSD License"*. |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) | 🟢 Apache-2.0 | 30.1k · 3.2k | 0.106 | *"🤗 smolagents: a barebones library for agents that think in code."* 🟢 **`Gap 539-D` closed by this row** — named in **24** of this base's files and never measured. The minimal agent loop to reach for when LangGraph or CrewAI is more framework than a single tutoring or grading task needs. |

### 🔵 How to read the `f/★` column — and its two stated limits

Fourteen points were classed **first by what the software is** (does an
institution run its own copy, or import it as a dependency?) and only then
ordered by forks-per-star. Evidence:
[`../evidence/forks-per-star-rank.2026-10-30-p540.tsv`](../evidence/forks-per-star-rank.2026-10-30-p540.tsv).
🟢 **The classes separated with an empty band between them**: every
deploy-per-institution point at **≥ 0.250**, every import-as-dependency point at
**≤ 0.182**, no instance in between. Star counts do not do this —
`smolagents` (30.1k) and `jupyterhub` (8.4k) are both large and land on opposite
sides.

> **f/★ ≥ 0.25 → fork it.** Institutions run their own copy. Budget for
> carrying a fork: migrations, upgrades, local schema.
> **f/★ ≤ 0.15 → pin it.** It is a dependency. Budget for version drift.
> **Between, or under ~50 stars → the ratio says nothing.** Read the repository.

🔴 **Limit one: n = 14, one sector, one hour.** A boundary fitted to fourteen
points is a hypothesis. → `Gap 540-C` re-measures at n ≥ 60 before any recipe
may depend on the threshold.

🔴 **Limit two, demonstrated on the ranking's own output: the ratio ranks, it
does not vet.** [`Apereo-Learning-Analytics-Initiative/OpenLRS`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRS)
(ECL-2.0, 47★ · 38 forks) scored **0.809** — second of fourteen — and its
repository description is the single word **"Deprecated"**. Forks-per-star
measures how software *was* used, which is past tense. A liveness read stays
mandatory before promotion, and this row is **not filed** above.

### 🔴 What the gate found that does not become a row — and why it matters more than the rows

37 of the 450 addresses served a grant file whose title the matcher could not
name. 🟢 **Every one resolved on a hand read** — not one was unnameable — across
**twelve** dialects. 🔴 **23 of 37 (62 %) are not buildable permissively**,
against ~0 % in the named-permissive buckets. `UNKNOWN` is not noise; it is
where this sector's non-buildable grants concentrate, at roughly eight times the
base rate. Full table and evidence on
[`trending.md`](trending.md#-p540--2026-10-30) and
[`../evidence/unknown-residue-graded.2026-10-30-p540.tsv`](../evidence/unknown-residue-graded.2026-10-30-p540.tsv).

🟡 **One dialect is a regional bias against the region this base exists to
serve.** [`portabilis/pre-matricula-digital`](https://github.com/portabilis/pre-matricula-digital)
is ordinary AGPL-3.0, graded `UNKNOWN` **only because its licence text is in
Portuguese**. An English-keyed classifier under-grades LATAM supply, and
"no grant found" reads downstream as "no supply". → `Gap 540-B`.

## 🆕 `p539` — the backlog's head was never obscure, it was the field's own infrastructure

🔴 **The measurement that reframes this file.** `p538` left the promotion queue
empty and set its successor a choice: generate a new queue from the `HISTORY`
bucket — **4 120 distinct addresses against 262 filed** — or find an unused
channel. `p539` built the queue
([`../ingest/history-backlog.py`](../ingest/history-backlog.py)) and then
gated it in bulk
([`../ingest/backlog-gate.py`](../ingest/backlog-gate.py)), and the result is
not a list of obscure repositories:

| | Value |
|---|---|
| `HISTORY` − `FILED` (the backlog) | **3 869** |
| 🟢 LIVE (`git ls-remote --symref`, all 3 873 probed) | **3 725 — 96.2 %** |
| 🔴 DEAD / PRIVATE | 148 — 3.8 % |
| Grant-gated at the ranked head | 147 of 150 live, **67 MIT · 18 Apache-2.0 · 2 BSD · 1 ISC · 1 ECL-2.0** |
| 🔴 UNRESOLVED on 46 grant filenames | 17 |

🔵 **So the 6.8 % filing rate is a promotion deficit, not a graveyard.** Only
3.8 % of the backlog is dead. The top of it — ranked by how many of this base's
own files name an address and never file it — reads
`openedx/edx-platform` (**59 files, 243 mentions**), `jupyterhub/jupyterhub`
(44 files), `plastic-labs/tutor-gpt` (37), `INGInious/INGInious` (34),
`frappe/erpnext`, `apache/ofbiz-framework`, `huggingface/smolagents`,
`Ed-Fi-Alliance-OSS/Ed-Fi-ODS`. **This base has been describing the education
field's load-bearing infrastructure in prose for hundreds of passes without
putting it in a table row a successor can paste.**

🟢 **Filed this pass, every figure read first-hand from the repository page:**

| Repo | Licence | Stars · forks | Region | Why it is foundational |
|---|---|---|---|---|
| [AnubisLMS/Anubis](https://github.com/AnubisLMS/Anubis) | 🟢 **MIT** (`LICENSE` at `main`) | **382** · 54 | 🟢 **North America (USA)** — *stated*: *"battle tested at **NYU Tandon** for several semesters"* | *"Distributed LMS for automating Computing Science Courses From NYU."* Autogrades by running tests when a student pushes to their assignment repo, and serves browser **Cloud IDEs** (Theia) on **Kubernetes**. Topics `k8s` · `cloud-ide` · `learning-management-system`. 🟢 The only row here that is an LMS **and** an autograder **and** a per-student sandbox — the three pieces a code course needs and that this base has otherwise only had separately. |
| [inducer/relate](https://github.com/inducer/relate) | 🟡 **MIT by README text only** — sidebar names **no** licence; README carries MIT-style permission text, `Copyright (C) 2014-15 Andreas Kloeckner` | **437** · 125 | 🟡 unplaced — no institution named on the page | *"RELATE is an Environment for Learning And TEaching."* Django courseware: content authored in **YAML + Markdown under git**, so an instructor previews new content while students still see the old version; sandboxed code questions with autograding plus optional human second-stage marking; grade book, class calendar, live in-class quizzes. 🔵 **The git-versioned-content model is the asset** — it is the only row here where course material is a reviewable commit. |
| [Ed-Fi-Alliance-OSS/Ed-Fi-ODS](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) | 🟢 **Apache-2.0** (`LICENSE.txt` at `main`) | **28** · 48 | 🟢 **North America** — Ed-Fi Alliance, LLC in the copyright notice; the standard is US K-12 | *"The core code for the Ed-Fi Operational Data Store (ODS) and Ed-Fi ODS API."* 🟢 **The K-12 data substrate a US district engagement inherits whether or not anyone chose it.** 48 forks against 28 stars is the signature of an implementation base, not an audience — people deploy it, they do not admire it. 🔵 Pair with `1EdTech` for the standards layer: Ed-Fi carries the records, LTI/Caliper carry the events. |
| [DFE-Digital/teaching-vacancies](https://github.com/DFE-Digital/teaching-vacancies) | 🟢 **MIT** (`LICENSE` at `main`) | **27** · 23 | 🟢 **EMEA (England)** — *stated*: *"a free job-listing service from the **Department for Education**"*, covering *"schools or trusts in England"* | **19 739 commits** on a live national government service, integrating **GOV.UK One Login** and DWP *Find a Job*. 🟢 **And it ships `AGENTS.md`, `CLAUDE.md` and `GEMINI.md` plus a documentation section titled *"Guidance for AI coding agents"*** — a state education department publishing its agent conventions in the open. 🔵 Read it for the conventions, not the domain: it is the clearest public example of how a public-sector education body expects agents to work inside its codebase. |
| [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | 🟢 **MIT** (`LICENSE` at `main`) | **6 500** (page rounds to 6.5k) · 1 100 | ⚪ Global | *"Policy enforcement, zero-trust identity, execution sandboxing, and reliability engineering for autonomous AI agents. Covers 10/10 OWASP Agentic Top 10."* Sits between an agent and the actions it takes; every tool call or data access is checked against policy first, with agent identity, isolated execution and audit records. SDKs in several languages plus framework adapters and a CLI. 🔴 **Education is not mentioned anywhere on the page, and that is stated rather than glossed.** 🟢 It is filed here because the 2026 education story is *governed* adoption — an Annex III high-risk assessment tool needs exactly an audit record and a policy gate, and this is the only permissive artefact on this base that provides them. **Public preview.** |

🔴 **Two rows the gate attested and this pass did NOT read first-hand**, recorded
as such so a successor does not mistake a gate for a page read:
[`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub)
(**BSD-3-Clause**, `LICENSE` at `main`) and
[`huggingface/smolagents`](https://github.com/huggingface/smolagents)
(**Apache-2.0**, `LICENSE` at `main`). Both are grant-attested from the licence
file's own bytes at the resolved default branch; **neither has a star count
measured this pass**, so none is written. `jupyterhub` is named in **44** of
this base's files and `smolagents` in **24**, and both remain unfiled on the
platform tables above — the single largest piece of promotion debt left.

🟢 **`apache/ofbiz-framework` proved the default-branch rule still earns its
keep.** Its default branch is **`trunk`**, not `main` or `master`. `p509` found
that defect, `p517` fixed it in
[`../ingest/probe-grant.sh`](../ingest/probe-grant.sh), and the bulk gate
inherits the fix — a probe that assumed `main` would have filed a top-20
backlog address as UNRESOLVED.

## 🆕 `p541` — eighteen rows off the promotion debt, and the EMEA public-sector layer this base never filed

🔵 **Where these came from.** Not from a search. p540 resolved the 37
`UNKNOWN` grants in its residue into twelve dialects **in prose** and filed
none of them. Graded against the committed tree by
[`gate-restated-presence`](../compose/code/p541-restated-presence/),
**32 of those 37 appear only in trending history** — measured, named, never a
row. That is `Gap 529-A`'s promotion debt with a number on it. Every grant
below was re-read first-hand this pass as **bytes at
`raw.githubusercontent.com`** (`github.com` HTML answers 403 through this
session's proxy) and the byte count is given so a successor can re-measure.

### 🟢 The Apereo sector layer — `ECL-2.0`, a real OSI licence both classifiers now name

🔵 **`ECL-2.0` is the Educational Community License**, Apache-2.0 with a
patent clause rewritten for university consortia. It is permissive and
Globant can build on it. It is also the single most common grant in this
residue, which says something about where education's institutional code
actually lives.

| Repo | Grant (bytes read) | What it is | Reuse |
|---|---|---|---|
| [`Apereo-Learning-Analytics-Initiative/LearningAnalyticsProcessor`](https://github.com/Apereo-Learning-Analytics-Initiative/LearningAnalyticsProcessor) | 🟢 **ECL-2.0** (9,919 B) | The LAP batch engine: pulls from an LRS and a SIS, runs risk models, writes scores back | 🟢 The reference pipeline for dropout-risk work |
| [`Apereo-Learning-Analytics-Initiative/OpenDashboard-api`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenDashboard-api) | 🟢 **ECL-2.0** (9,919 B) | The API half of the analytics dashboard | 🟢 Serve LAP output to an LMS |
| [`Apereo-Learning-Analytics-Initiative/OpenDashboard-legacy`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenDashboard-legacy) | 🟢 **ECL-2.0** (9,919 B) | The dashboard UI, explicitly `legacy` | 🟡 Read for the data contract, not to deploy |
| [`Apereo-Learning-Analytics-Initiative/lap-sakai-extractor`](https://github.com/Apereo-Learning-Analytics-Initiative/lap-sakai-extractor) | 🟢 **ECL-2.0** (11,087 B) | Extracts Sakai activity into the LAP schema | 🟢 The pattern to copy for a Moodle/Canvas extractor |
| [`KualiCo/rice`](https://github.com/KualiCo/rice) | 🟢 **ECL-2.0** (11,106 B) | Kuali Rice — the middleware under Kuali's higher-ed administration suite (workflow, identity, business rules) | 🟡 Large and institutional; take the workflow engine, not the suite |

🔴 **One warning carried from p540's ranking, not re-measured here:**
`Apereo…/OpenLRS` is already on this base and its GitHub description reads
**"Deprecated"**. The sector licence does not make a dead project live.

### 🟢 Assessment and standards

| Repo | Grant (bytes read) | What it is | Reuse |
|---|---|---|---|
| [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) | 🟢 **BSD-3-Clause** (2,058 B — *"The QTIWorks source code is distributed under the 3-clause BSD licence"*) | A **QTI 2.1** assessment engine — delivery, response processing, scoring | 🟢 **The permissive QTI implementation this base has wanted.** Standards-compliant item banks without an AGPL obligation |
| [`UCL-INGI/INGInious`](https://github.com/UCL-INGI/INGInious) | 🟡 **AGPL-3.0, SCOPED** (34,764 B; the file opens *"Most of the files in INGInious are distributed under the GNU AGPL"*) | Automated grading of programming assignments, container-isolated, from UCLouvain | 🔴 **Copyleft and the grant is not repository-wide.** `p382`'s subtree class: "most of the files" obliges a per-path read before any reuse |

### 🟢 The ladder's own blind spot — three MIT grants one rung further along

🔴 **Each of these three serves a two-line template fill-in at `LICENSE`** —
`YEAR: 2021 / COPYRIGHT HOLDER: …`, 45–47 B, written by R's
`usethis::use_mit_license()` — **and the real MIT text at `LICENSE.md`.** A
ladder that probes `LICENSE` and stops reads the fill-in and reports nothing.
🔵 `p275` taught this base that *"the LADDER, not the slug, is the defect"*;
this is that lesson in a shape its authors had not seen — **the file exists
and is not a grant.** All three `LICENSE.md` reads were confirmed **200,
`# MIT License`** this pass.

| Repo | Grant | What it is |
|---|---|---|
| [`rstudio/ggcheck`](https://github.com/rstudio/ggcheck) | 🟢 **MIT** (at `LICENSE.md`; `LICENSE` is a 45 B stub) | Inspects student `ggplot2` code for automated grading of data-viz exercises |
| [`rstudio/tblcheck`](https://github.com/rstudio/tblcheck) | 🟢 **MIT** (at `LICENSE.md`; `LICENSE` is a 46 B stub) | The table equivalent — grades student data frames against an expected result |
| [`shmercer/writeAlizer`](https://github.com/shmercer/writeAlizer) | 🟢 **MIT** (at `LICENSE.md`; `LICENSE` is a 47 B stub) | Automated scoring of **student writing quality** from scored corpora |

🔵 **Why these three are worth a row:** automated grading of *statistics and
writing* is the assessment case this base has otherwise only held for code.

### 🟢 EMEA, public sector — `opetushallitus`, seven national registries under `EUPL`

🟢 **This is the largest single block of **state-operated** education software
on this base, and it was entirely unfiled.** The Finnish National Agency for
Education publishes its production registries in the open. 🔴 **The grant is
licensed *by reference*, not reproduced**: each `LICENSE` is a ~650 B English
notice naming the **EUPL, Version 1.1 or subsequent** and pointing at
`joinup.ec.europa.eu` for the text. 🔵 **The version matters and the base had
it wrong by implication** — the only EUPL title either classifier carries is
**1.2**, and six of these seven say **1.1**.

| Repo | Grant (bytes read) | What it is |
|---|---|---|
| [`opetushallitus/koski`](https://github.com/opetushallitus/koski) | 🟡 **EUPL-1.1+** by reference (654 B notice) | The **national study-rights and completed-studies register**. 23★ · 12 forks |
| [`opetushallitus/eperusteet`](https://github.com/opetushallitus/eperusteet) | 🟡 **EUPL-1.1+** by reference (632 B) | The **national curriculum** service — the machine-readable core curriculum |
| [`opetushallitus/ehoks`](https://github.com/opetushallitus/ehoks) | 🟡 **EUPL-1.1+** by reference (632 B) | Personal competence-development plans for vocational students |
| [`opetushallitus/oppijanumerorekisteri`](https://github.com/opetushallitus/oppijanumerorekisteri) | 🟡 **EUPL-1.1+** by reference (632 B) | The national **learner-identifier** registry |
| [`opetushallitus/organisaatio`](https://github.com/opetushallitus/organisaatio) | 🟡 **EUPL-1.1+** by reference (632 B) | The register of educational **institutions** |
| [`opetushallitus/valtionavustus`](https://github.com/opetushallitus/valtionavustus) | 🟡 **EUPL-1.1+** by reference (653 B) | State **grant administration** for education providers |
| [`opetushallitus/ataru`](https://github.com/opetushallitus/ataru) | 🟡 **EUPL-1.2** by reference (296 B — the one that says 1.2) | The national **application and admissions** system |

🔴 **EUPL is reciprocal.** It is a copyleft licence with an EU-law
jurisdiction clause, so these are **reference architectures and integration
targets, not components to vendor into a client's proprietary stack.** 🟢
What they are worth is the **data model**: a working, legally published,
national-scale set of schemas for learners, institutions, curricula and
admissions — the thing every EMEA public-sector education engagement has to
invent otherwise.

### 🟢 Two general-purpose rows the residue also returned

| Repo | Grant (bytes read) | Note |
|---|---|---|
| [`crewAIInc/crewAI`](https://github.com/crewAIInc/crewAI) | 🟢 **MIT** (1,055 B, **untitled** body) | The multi-agent framework. 🔵 Filed because its grant was in the `UNKNOWN` residue for `p314`'s untitled-payload reason, not because this base lacked the name |
| [`hcengineering/platform`](https://github.com/hcengineering/platform) | 🟡 **EPL-2.0** (14,197 B) | Huly platform — project/knowledge management. 🟡 **Weak copyleft**: file-level reciprocity, so it is usable alongside proprietary code but not inside it |

### 🟢 Two Spanish-language curriculum repos, with a split grant worth reading as a model

| Repo | Grant (bytes read) | Note |
|---|---|---|
| [`CaminosMarina/curso-ia`](https://github.com/CaminosMarina/curso-ia) | 🟡 **SPLIT — content `CC BY-SA 4.0`** (`LICENSE`, 1,900 B) **and code `MIT`** (`LICENSE-CODE`, 1,534 B, confirmed 200) | A Spanish self-study AI curriculum running LLM fundamentals → agents → **MCP** → n8n automation. 🟢 **The licence structure is the lesson**: it separates the course text from the scripts, names third-party material as retaining its own terms, and says so in the file. 🔴 A roundup described this repo as "MIT"; MIT covers `scripts/` and lesson snippets only |
| [`thalisantunes/eecri-2026-ia-artesanato`](https://github.com/thalisantunes/eecri-2026-ia-artesanato) | 🟢 **MIT** (1,080 B, titled, `Copyright (c) 2026 Thalis Antunes de Souza`) | Workshop material from I EECri 2026 (Nova Porteirinha, MG, Brazil): slides, scripts, a prompt sheet, OpenSCAD models, and **blind prompt tests across five models**. 🔵 Thin on education-platform relevance; filed for the **blind-test methodology**, which is a reusable evaluation harness |

### 🔴 What the residue returned that must NOT become a row

🔵 Recorded so a successor does not re-discover them as finds. Seven payloads
are genuinely outside the stock table and **none is a permissive software
grant**: [`heronerar/OpenGaokao`](https://github.com/heronerar/OpenGaokao)
(*OpenGaokao Source-Available License 1.0*),
[`nakafaai/aksara`](https://github.com/nakafaai/aksara) (*Nakafa Source
Available 2.0*), [`sodadata/soda-core`](https://github.com/sodadata/soda-core)
(*Elastic License 2.0*),
[`AStheTECH/mewcp-google-classroom`](https://github.com/AStheTECH/mewcp-google-classroom)
(*AStheTECH Community License*),
[`Khan/tutoring-accuracy-dataset`](https://github.com/Khan/tutoring-accuracy-dataset)
(*Evaluation Dataset License* — field-of-use limited to evaluation),
[`aclascollege/polymath`](https://github.com/aclascollege/polymath) (**ODbL**,
a database share-alike and not a code grant), and
[`yuanjiusheng/cloud-learning-ce`](https://github.com/yuanjiusheng/cloud-learning-ce)
(**all rights reserved**, in Chinese). 🔴 Plus the six **bespoke-over-stock**
traps listed on [`../agents/top.md`](../agents/top.md#-p541--the-licence-traps-in-p540s-residue-and-why-gap-540-bs-own-remedy-is-unsafe).

## Platform cores

| Repo | Licence | Stars | Why it is foundational |
|---|---|---|---|
| [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | 9.3k | "A complete web conferencing system for virtual classes." README names **BigBlueButton 4.0**; default branch `v4.0.x-develop`. The default synchronous-classroom layer, already integrated into Moodle, Canvas and Open edX. LGPL is the friendliest copyleft here. |
| [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | AGPL-3.0 | 8.2k | The Open edX LMS + Studio authoring core. *(`openedx/edx-platform` now redirects here — use the `openedx-platform` address.)* The reference choice for MOOC-scale and large corporate-training deployments. |
| [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 | 7.6k | "The world's open source learning platform." PHP, `main` branch, 123k+ commits. **Largest plugin ecosystem in the sector by a wide margin** — which makes the plugin boundary the cheapest place to attach anything new, and makes the missing Moodle MCP server (see below) the loudest gap on this base. |
| [oppia/oppia](https://github.com/oppia/oppia) | **Apache-2.0** | 7.0k | "A free, online learning platform to make quality education accessible for all." Python + Angular on App Engine. **The largest permissively licensed learning platform found** — the one core on this shelf a studio can fork without copyleft consequences. |
| [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | AGPL-3.0 | 6.9k | "The open LMS by Instructure, Inc." Dominant in North American higher ed. Caveat worth repeating to any client: the open-source codebase is **not** equivalent to Instructure's full commercial feature set. |
| [frappe/lms](https://github.com/frappe/lms) | AGPL-3.0 | 3.4k | "Easy to Use, 100% Open Source Learning Management System." Title block read this pass: `GNU AFFERO GENERAL PUBLIC LICENSE Version 3`. Lighter and newer than Moodle, sitting on the Frappe/ERPNext stack — the natural LMS when the client already runs Frappe for administration. |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | **ECL-2.0** | 1.2k | Higher-ed teaching, research and collaboration platform. Title block: `Educational Community License, Version 2.0 (ECL-2.0)` — an Apache-2.0 derivative with a patent-grant tweak for academic consortia, **permissive in practice**. Page lists 25.2 and 23.5 as community-supported. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** | 1.2k | "The offline app for universal education." Python + JS, `develop` branch, ~39.8k commits. **The only MIT-licensed full learning platform on this shelf**, and the only one designed for intermittent or absent connectivity — the deciding constraint for LMIC and rural deployments in LATAM, Africa and South/Southeast Asia. |
| [overhangio/tutor](https://github.com/overhangio/tutor) | AGPL-3.0 | 1.1k | "The Docker-based Open edX distribution designed for peace of mind." In practice nobody should deploy Open edX by hand; this is the supported path, and the plugin system is where customisation belongs. |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | 1.0k | LMS focused on ease of use and accessibility; install docs reference **v2.0.3**. Strong footprint in Spanish- and French-speaking deployments with small or no technical staff — relevant for LATAM public-sector work. |

## Administration, records and integrity

| Repo | Licence | Stars | Why it is foundational |
|---|---|---|---|
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 | 900 | "Comprehensive Open Source ERP for Educational Institutes", built as Odoo modules; branch `19.0`. Admissions, timetabling, attendance, fees, library, hostel. The ERP counterpart to the LMS cores above. |
| 🔵 [frappe/education](https://github.com/frappe/education) | **GPL-3.0** — *resolved this pass* | 685 | "Open source education / school management system." **`p526` left this red:** the repository page renders no licence type and a `license.txt` is present but unnamed. Fetched directly this pass, the file is three lines of front matter — `--- / License: GNU GPL V3 / ---` — so it is **GPL-3.0**: strong copyleft, *not* permissive, and **not the same licence as Frappe LMS**, which is AGPL-3.0. Two apps, same stack, two different copyleft regimes; a deliverable spanning both inherits both. 472 forks. |
| [portabilis/i-educar](https://github.com/portabilis/i-educar) | GPL-2.0 | 722 | **LATAM anchor.** School-management software described on its own page as "the largest free education software in Brazil" — originally built by the municipal government of **Itajaí, Santa Catarina**, released on the Brazilian federal Public Software Portal in 2008, now stewarded by Portábilis. Any Brazilian public-sector education engagement meets this system. |
| [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | GPL-2.0 | 648 | "RosarioSIS Student Information System for school management." PHP/PostgreSQL, modular, widely deployed in small and mid-size schools; strong Spanish/French/Portuguese localisation. Origin is not stated on the repo page. |
| [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | 505 | **EMEA anchor.** German non-profit-governed LMS, branch `release_11`. The usual choice for compliance-heavy European public-sector and government training, where governance provenance matters as much as features. |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** | 449 | **EMEA, permissive.** Swiss web-based LMS covering teaching, learning, assessment and communication. Apache-2.0 plus a European governance story is a rare combination on this shelf — the best base for an EMEA engagement that needs to ship proprietary extensions. |
| [dodona-edu/dolos](https://github.com/dodona-edu/dolos) | **MIT** | 355 | "Source code plagiarism detection" — finds similar or modified solutions to programming exercises. Copyright line reads `Team Dolos <dolos@ugent.be>`, i.e. **Ghent University (EMEA)** — read from the licence file, not inferred. No LLM in it, and that is the point: assessment-integrity findings have to be explainable to an appeals board. |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | GPL-3.0 | 152 | Framework-independent PHP library for H5P interactive content; grant at **`LICENSE.txt`**. H5P is the de facto interoperable format for interactive exercises across Moodle, Canvas, Open edX and Drupal — the cheapest way to make generated content portable. |
| [oat-sa/tao-core](https://github.com/oat-sa/tao-core) | GPL-2.0 | 64 | QTI-standard computer-based assessment core. The right base when items must interoperate with national testing infrastructure. |
| [openfun/ralph](https://github.com/openfun/ralph) | **MIT** | 51 | "The ultimate Learning Record Store (and more!) for your learning analytics." Python/FastAPI/Pydantic; copyright line reads `France Université Numérique` (**EMEA**). Fifty-one stars and genuinely load-bearing: it is the **xAPI/LRS seam** where agent-generated learning events get stored in a standard shape instead of a vendor's private table. |
| [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | **MIT** | 4.1k | FSRS (Free Spaced Repetition Scheduler). The retention primitive — use it instead of inventing a review interval, because the scheduling problem is solved and the solution is permissive. |

## 🆕 The Moodle MCP census — 🔴 **222 addresses, not eleven; ceiling 52★ and ungranted**

> 🔴 **`p529` correction, read this before the table.** The heading of this
> section used to read *"eleven codebases, 37 stars, no convergence"*. The API
> reports **222** matching addresses; `p529` read the **top 80 by stars**, which
> alone total **352★**. The field's ceiling is **not** `G36maid` at 27★ — it is
> [`loyaniu/moodle-mcp`](https://github.com/loyaniu/moodle-mcp) at **52★**, and
> ⛔ **it has no licence file** (no `license` key from the API; no file at five
> paths on `main`). The permissive ceiling is
> [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server),
> **MIT, 45★**, last pushed **22 Feb 2026**. Licence spread over the 80 read:
> **MIT 44 · none 18 · GPL-3.0 7 · `NOASSERTION` 4 · Apache-2.0 4 · AGPL-3.0 2 ·
> WTFPL 1** → **60% permissive, 27.5% with no usable grant** — not *"ten of
> eleven MIT"*.
>
> 🔵 **And the conclusion changes with the number.** `p528` recommended
> consolidating eleven codebases. **You cannot consolidate 222 repositories whose
> purpose is to be institution-specific** — 14 of the top 26 bridge one named
> university each, and LATAM and APAC ship five apiece while **North America
> ships none**. The asset is a **bridge generator**, not a merged bridge. Full
> census, regional placement and reasoning in
> [`trending.md`](trending.md); the recipe is `P558` in
> [`../compose/patterns.md`](../compose/patterns.md).
>
> ⚠️ **The table below is `p528`'s thirteen-address census, kept as-is**, because
> its tool counts and read/write analysis are first-hand and the API exposes
> neither. **Read it as a deep sample of the field, not as the field.**

⚠️ **This section is corrected and widened this pass.** `p527` wrote that the
Moodle MCP field is *"eight search results, roughly three real codebases"*. That
was wrong, and it was wrong in the direction that matters: the field is not
small, it is **fragmented**. `p528` probed **twelve addresses first-hand** —
existence first (`README.md` on `main` and `master`), then the licence file's
title block — for a census of **thirteen**. ⚠️ The thirteenth,
`triffon/moodle-mcp`, is **carried from `p527`** as a confirmed duplicate of
`falkenslab` and was *not* re-probed this pass; its row is marked. The thirteen
resolve to **eleven independent codebases plus two forks**.

| Repo | Licence (title block) | Stars | Lang | Tools | Reads / writes |
|---|---|---|---|---|---|
| [G36maid/moodle-mcp](https://github.com/G36maid/moodle-mcp) | **MIT** | **27** | Rust (`rmcp`) | 22 (20 typed + 2 escape hatches, opt-in via `MOODLE_ENABLE_WS_FUNCTION`) | Web Services; courses, assignments, forums, grades, files-as-markdown. **Verified live against Moodle 3.7, 4.5 and 5.2** — the only one on this list that names three tested versions. |
| [thc1006/moodle-mcp](https://github.com/thc1006/moodle-mcp) | MIT (`© G36maid`) | 0 | Rust | 22 | ⛔ **Fork of the above**, stated on the page; the copyright line confirms it. |
| 🆕 [GhaithAlHallak8/moodler-mcp](https://github.com/GhaithAlHallak8/moodler-mcp) | **MIT** (`© Ghaith AlHallak`) | 3 | Python 3.14+ | **40** (32 read / 8 write) | Writes **off by default** behind two separate flags (`MOODLER_ALLOW_STUDENT_WRITES`, `MOODLER_ALLOW_TEACHER_GRADING`); destructive calls require `confirm=true`. Playwright/Chromium sign-in, SQLite cache, ships as a `.mcpb` bundle. 🟢 **The best-governed write model in the census.** |
| 🆕 [Faixiang/moodle-mcp](https://github.com/Faixiang/moodle-mcp) | **MIT** | 2 | Python 3.8+, **stdlib only** | 8 | Read-only against Moodle (the one exception, `moodle_download_week`, writes to local disk). Single `server.py`, zero dependencies, docs in 10 languages, verified against Moodle 4.3.6. ⚠️ `v1.3.0` dated 2026-10-27 — **and all four changelog entries, 1.0.0 through 1.3.0, carry that same date.** Treat the version history as a self-claim. ⚠️ Its own "Why this exists" section still says *"six read-only tools"* against a table of eight. |
| 🆕 [leshamblin/MoodleMCP](https://github.com/leshamblin/MoodleMCP) | **MIT** | 2 | Python 3.10+, FastMCP | **70 claimed / 67 counted** | Read *and* write, with the clearest safety story: read-only by default, writes confined to `MOODLE_DEV_COURSE_WHITELIST`, `MOODLE_PROD_ALLOW_WRITES=false` recommended, token in a local `.env`. Writes cover grading, enrolment, messages and forum posts. |
| [falkenslab/moodle-mcp](https://github.com/falkenslab/moodle-mcp) | **MIT** | 2 | — | **~230 claimed** | Drives a logged-in **browser session** rather than Web Services; README claims grading-with-rubrics and quiz construction for Moodle 4.5/5.x. ⚠️ Largest tool claim in the census and the least verifiable; a search summary said 140, the README says ~230, **neither is verified by use.** |
| [triffon/moodle-mcp](https://github.com/triffon/moodle-mcp) | MIT (`© Falkenslab`) | — | — | ~230 | ⛔ **Same code as `falkenslab`** — identical copyright holder and description. Not an independent project. |
| 🆕 [Jawadh-Salih/moodle-mcp-server](https://github.com/Jawadh-Salih/moodle-mcp-server) | **MIT** | 0 · 2 forks | **Go** | 14 | 13 read + `submit_assignment` (write) + `login`. Also exposes a REST mode for ChatGPT and Gemini. Student-facing. README examples use a `uom.lk` domain (University of Moratuwa, **Sri Lanka**) — 🟡 *inferred*, not stated. |
| 🆕 [sonstellar969/open-moodle](https://github.com/sonstellar969/open-moodle) | **MIT** — 🔴 **but see the dependency** | 0 | Python | 14 | Read-mostly CLI + MCP server; SQLite FTS5 search. 🔴 **Its own page states that PyMuPDF, its PDF-extraction dependency, is AGPL-3.0.** A repo-level licence probe grades this buildable; the shipped artefact carries network copyleft. ⚠️ Also notes its `moodle_mobile_app` token *can* permit writes on some sites — so "read-only" here is a property of the deployment, not of the code. |
| 🆕 [AnonymousOnyx22/moodle-student-mcp](https://github.com/AnonymousOnyx22/moodle-student-mcp) | **MIT** | 0 | TypeScript / Node 20+ | 12 | Read-only by construction — *"can never submit, edit or delete anything."* States *"Not affiliated with Moodle Pty Ltd."* |
| [duck-5/moodle-mcp](https://github.com/duck-5/moodle-mcp) | **MIT** | not read | — | — | Independent small implementation; existence and grant re-confirmed `p528`, star count not read. |
| ⚠️ [csmediapro/moodle-mcp-server](https://github.com/csmediapro/moodle-mcp-server) | 🔴 **AGPL-3.0** (title block: *"GNU AFFERO GENERAL PUBLIC LICENSE"*) | 1 | TypeScript / Node | — | The most *visible* in search results and **the one that is not permissive.** Read-only by design, no plugin install needed. AGPL-3.0 §13 on an integration server a hosted deliverable calls is an architecture decision, not a detail. |
| ⛔ [tosuki/moodle-mcp](https://github.com/tosuki/moodle-mcp) | **none** | — | — | — | A search result called it *"MIT licensed."* Repository **resolves**; **no licence file at any of six common paths on `main`.** ⛔ Ungranted — `p527`'s call, re-confirmed this pass. |

**The read, corrected.** Thirteen addresses, **eleven independent codebases**,
**four languages**, tool counts spanning **8 → ~230**, and **37 stars in total
across every codebase whose counter was read this pass** — less than one eighth
of [canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) alone (**308★**), for
the *larger* install base.

🟢 **Ten of the eleven independent codebases are MIT.** That is the finding that
changes the build decision. The gap is not a licensing problem and not an
absence — it is 🔴 **a convergence problem**: no two of these agree on a tool
vocabulary, nobody is above 27★, and the one project with real traction is
written in Rust while the mass of the field is Python.

🔵 **So the build is a consolidation, not a greenfield.** The pieces to take, all
MIT, all verified this pass: **G36maid's typed-tool surface and tested version
matrix**, **moodler-mcp's two-flag write gate with `confirm=true`**,
**leshamblin's course-whitelist boundary**, **Faixiang's zero-dependency
posture**. The thing none of them has is a **shared tool vocabulary** — and that,
not another server, is what would make this the sector's bridge. See
[`../compose/patterns.md`](../compose/patterns.md) **P553**.

⚠️ **One caveat on the whole census:** every star count here is a rounded page
value read through the session proxy, and every tool count is the repository's
own claim. Three of them contradict themselves on that claim (Faixiang 6 vs 8,
leshamblin 70 vs 67, falkenslab 140 vs ~230). **Tool counts in this field are
marketing, not measurement.**

## 🆕 Standards, records and assessment — the integration layer (`p530`)

Grants read from the licence file's own title block; counters exact from the API
this pass. **Passes unfiled** is from
[`../evidence/address-ledger.tsv`](../evidence/address-ledger.tsv) — how many
distinct passes described the address before anything filed it.

| Repo | Licence | Stars | Passes unfiled | Why it is foundational |
|---|---|---|---|---|
| [adlnet/xAPI-Spec](https://github.com/adlnet/xAPI-Spec) | Apache-2.0 | 956 | — | The xAPI specification itself, from US DoD ADL — the vocabulary every learning-record claim in this sector is written against. 402 forks. 🟡 Apache-2.0 on a *specification document* is deliberate, not a category error: the patent grant is the point. |
| [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | Apache-2.0 | 144 | 🔴 **19** | A SQL-backed xAPI Learning Record Store. Clojure, runs on Postgres/SQLite. **This is where agent-generated learning events belong** — an institution will ask where the data lands, and an LRS is the standards-compliant answer. |
| [adlnet/ADL_LRS](https://github.com/adlnet/ADL_LRS) | Apache-2.0 | 334 | — | ADL's own reference LRS, Python. 156 forks. 🟡 Pushed **2025-11-14** — the reference implementation, not the one to deploy; `lrsql` is the live option. |
| [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | MIT | 361 | 🔴 **20** | A modern SCORM JavaScript runtime (SCORM 1.2 / 2004 / AICC), offline-first, cross-frame. TypeScript. **The bridge to every legacy course package an institution already owns**, and the reason an AI layer need not discard existing content. |
| [tsugiproject/tsugi](https://github.com/tsugiproject/tsugi) | Apache-2.0 | 377 | 🔴 **14** | LTI tool framework — build a tool once, launch it inside Moodle, Canvas, Sakai or Open edX. 267 forks. **The cheapest route to putting an agent inside an LMS an institution will not replace.** |
| [packbackbooks/lti-1-3-php-library](https://github.com/packbackbooks/lti-1-3-php-library) | Apache-2.0 (`LICENSE.md`) | 54 | — | IMS-certified LTI 1.3 tool-provider library, PHP. 🔴 **A fork, so GitHub repository search does not return it** — see shelf rule 10. Certification is what matters here, not the star count. |
| [openedx/XBlock](https://github.com/openedx/XBlock) | Apache-2.0 | 471 | 🔴 **15** | The Open edX component SDK: the supported way to add a custom learning component to an AGPL-3.0 platform **without touching the platform's code**. 231 forks. 🔵 Note the grants differ — the SDK is Apache-2.0 while the core is AGPL-3.0. |
| [CAHLR/pyBKT](https://github.com/CAHLR/pyBKT) | MIT | 291 | — | Bayesian Knowledge Tracing and extensions, from Berkeley's CAHLR — the same lab behind [OATutor](https://github.com/CAHLR/OATutor) on the agent shelf. C++ core with Python bindings. **Mastery estimation that a faculty board will accept**, because it predates the LLM era and has a literature. |
| [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | MIT | 453 | — | pyKT: benchmark library for deep knowledge tracing, with standard datasets and prediction scenarios. **The way to show an adaptive claim is measured rather than asserted.** |
| [jupyter/nbgrader](https://github.com/jupyter/nbgrader) | BSD-3-Clause | 1 370 | — | Assigning and grading Jupyter notebooks — release, collect, autograde, manual-grade, return feedback. 345 forks. **The highest-starred permissive grading system in this sector.** |
| [Submitty/Submitty](https://github.com/Submitty/Submitty) | BSD-3-Clause | 806 | — | Homework submission, automated grading and TA grading, from RPI. **1 118 forks against 806 stars** — a deployment-heavy system, i.e. institutions actually run it. |
| [ucbds-infra/otter-grader](https://github.com/ucbds-infra/otter-grader) | BSD-3-Clause | 161 | — | Python *and* R autograding, container-based, from Berkeley Data Science. The lighter alternative to Submitty when only the grading half is wanted. |

🔴 **What this layer does not contain: an agent.** Every row above is
infrastructure an agent would *drive*. The composition is in
[`../compose/patterns.md`](../compose/patterns.md).

## 🆕 Serving the course — the JupyterHub deployment family (`p531`)

🔴 **This is the single largest coherent layer this base has ever been missing,
and it was not missing from the world — it was missing from this file.** Every
row below sat in an `archive/` snapshot and **nowhere in the live corpus**: they
are part of the **349** addresses `Gap 530-A` measured as dropped by a rewrite.
`p531` read the grant of all 349 first-hand and these came back **BSD-3-Clause,
every one**, title block `BSD 3-Clause License · Copyright (c) 2016/2017,
Project Jupyter Contributors`.

🔵 **Why it is foundational and not plumbing.** This file already carries
[`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) (1 370★) — how you
*grade* notebooks. It carried nothing about how a university *serves* them to
500 students, authenticated out of the LMS they already log into, on hardware
they already have. That is the whole gap between a notebook demo and a course,
and it is **nine live repositories, 2 309★, all permissive**.

| Repo | Licence | Stars | Forks | Last push | What it is for |
|---|---|---|---|---|---|
| [jupyterhub/kubespawner](https://github.com/jupyterhub/kubespawner) | **BSD-3-Clause** | **611** | 308 | 2026-10-27 | Spawns each student's notebook server as a Kubernetes pod. **The default answer for a cohort of any size**, and the one that makes per-student resource limits a config value rather than a project. |
| [jupyterhub/dockerspawner](https://github.com/jupyterhub/dockerspawner) | **BSD-3-Clause** | **543** | 305 | 2026-10-27 | The same, in Docker containers on one host. 🟢 The right choice for a single-department pilot, and the cheapest credible demo in this layer. |
| [jupyterhub/oauthenticator](https://github.com/jupyterhub/oauthenticator) | **BSD-3-Clause** | **443** | 367 | 2026-10-27 | OAuth2 sign-in — Google, GitHub, Globus, generic OIDC. The institutional-identity half for any tenant that already runs SSO. |
| [jupyterhub/ldapauthenticator](https://github.com/jupyterhub/ldapauthenticator) | **BSD-3-Clause** | **214** | 177 | 2026-08-20 | LDAP/AD sign-in. 🔵 Named separately because in public-sector and EMEA university estates **this, not OAuth, is what the directory speaks**. |
| [jupyterhub/ltiauthenticator](https://github.com/jupyterhub/ltiauthenticator) | **BSD-3-Clause** | 73 | 55 | 2026-07-01 | 🔴 **The row that connects this layer to the rest of the file.** Launch the hub *from inside Moodle, Canvas or Brightspace* over LTI, so the student never sees a second login. Known to this base since `p13` and described in **13 separate passes** without ever being filed. |
| [jupyterhub/batchspawner](https://github.com/jupyterhub/batchspawner) | **BSD-3-Clause** | **207** | 137 | 2026-07-17 | Spawns into Slurm/PBS/LSF batch queues. **The HPC route** — the deciding row wherever the client's compute is a research cluster, which in higher education it usually is. |
| [jupyterhub/systemdspawner](https://github.com/jupyterhub/systemdspawner) | **BSD-3-Clause** | 101 | 45 | 2026-10-24 | systemd units with real resource limits, no container runtime. The answer when Docker is not permitted on the box. |
| [jupyterhub/wrapspawner](https://github.com/jupyterhub/wrapspawner) | **BSD-3-Clause** | 65 | 60 | 🟡 2025-08-16 | Lets the *student* pick a spawner/profile at launch. 🟡 Fourteen months stale — read it, pin it, do not assume maintenance. |
| [jupyterhub/sudospawner](https://github.com/jupyterhub/sudospawner) | **BSD-3-Clause** | 52 | 39 | 2026-08-05 | Spawns as the student's own Unix user via a narrow sudo rule. The shape a university's own sysadmins will ask for. |

🔴 **Two members of the family are archived by their owner and are read-only
history:** [`jupyterhub/yarnspawner`](https://github.com/jupyterhub/yarnspawner)
(19★, Hadoop/YARN) and
[`jupyterhub/jupyterhub-tutorial`](https://github.com/jupyterhub/jupyterhub-tutorial)
(**202★**). 🔵 The second is worth naming precisely because it is the thing a
reader would reach for first: **the official deployment tutorial is archived**,
so an engagement should budget its own runbook rather than cite that one. 🟡
[`jupyterhub/kerberosauthenticator`](https://github.com/jupyterhub/kerberosauthenticator)
(12★, BSD-3-Clause, live) completes the authenticator set for Kerberos estates.

## 🆕 The LTI libraries this base has described 55 times and never filed (`p531`)

🔴 **`p530` built the integration layer above and filed the PHP LTI library
while leaving the Node and Python ones unfiled.** These are the **#1 and #2
most-described unfiled permissive addresses in the entire live corpus**, by the
base's own ledger:

| Repo | Licence | Stars | Forks | Passes unfiled | Why it is foundational |
|---|---|---|---|---|---|
| [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | **Apache-2.0** | **373** | 86 | 🔴 **28** | *"Turn your application into a fully integratable LTI 1.3 tool provider."* TypeScript/Node. **The reference implementation of the Node LTI stack** — the one an agent written in TypeScript attaches to any LMS with. Pushed 2026-10-13. |
| [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) | **MIT** | **138** | 84 | 🔴 **27** | LTI 1.3 Advantage tool for Python, with Django/Flask adapters. 🟢 The Python counterpart, and therefore the one that sits in front of a Python agent without a language boundary. Pushed 2026-09-10. |
| [LongsightGroup/qti3](https://github.com/LongsightGroup/qti3) | **MIT** | 6 | 3 | 11 | Dependency-light, framework-neutral TypeScript reference implementation of **QTI 3** assessment items. 🔵 QTI is how an assessment moves between systems; this is the only permissive, current QTI 3 implementation this base has found. |
| [jdolny/OneRoster.NET](https://github.com/jdolny/OneRoster.NET) | **MIT** | 6 | 8 | 12 | OneRoster API client. 🔵 OneRoster is **rostering** — the standard a district uses to tell a tool who is in which class. Thin, .NET-only, and the only permissive client on record. |
| [1EdTech/openbadges-validator-core](https://github.com/1EdTech/openbadges-validator-core) | **Apache-2.0** | 61 | 31 | 12 | Open Badges validation, Python, **from the standards body itself**. The credential half: if a deliverable issues badges, this is what says whether they are well-formed. |
| [Apereo-Learning-Analytics-Initiative/OpenLRW](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW) | **ECL-2.0** | 62 | 25 | 12 | Apereo's Learning Record Warehouse — Caliper/xAPI ingestion with a OneRoster-shaped model. 🟡 ECL-2.0 behaves as permissive (Apache-2.0 with an academic patent tweak), which this base has already graded on `sakaiproject/sakai`. |

## 🆕 Assessment science, and the licence-compliance instruments (`p531`)

| Repo | Licence | Stars | Forks | What it is for |
|---|---|---|---|---|
| [douglasrizzo/catsim](https://github.com/douglasrizzo/catsim) | **BSD-3-Clause** | **153** | 37 | **Computerised Adaptive Testing** simulator: item-response theory, item selection, ability estimation, stopping rules. 🟢 **The only permissive CAT/IRT implementation on this base**, and the thing that separates "an LLM asks harder questions" from a defensible adaptive assessment. Author in Brazil — **LATAM-origin psychometrics**. Pushed 2026-10-28. |
| [open-spaced-repetition/fsrs.js](https://github.com/open-spaced-repetition/fsrs.js) | **MIT** | **180** | 14 | FSRS — the scheduler that superseded Anki's SM-2. The retention half of any tutoring deliverable, as a library rather than a prompt. |
| [VienDinhCom/supermemo](https://github.com/VienDinhCom/supermemo) | **MIT** | **337** | 24 | SM-2 in JS/TS. 🔵 Filed beside FSRS deliberately: SM-2 is simpler, auditable in an afternoon and still what a client's existing flashcard data was scheduled with. |
| [aboutcode-org/scancode-toolkit](https://github.com/aboutcode-org/scancode-toolkit) | **Apache-2.0** (code) · 🟡 **CC-BY-4.0** (licence datasets) | **2 656** | 831 | 🔴 **`Gap 528-C` closes here, with a retrieval instead of a build.** Its own README states it *"detects licenses, copyrights, package manifests, **direct dependencies**"* and *"can process packages, build manifest and lockfile formats"* — which is exactly the dependency-grant enumerator `528-C` had scoped as new work for four passes. 🟡 **Read the dual grant before shipping:** the engine is Apache-2.0, the reference licence data is CC-BY-4.0, so redistributing the rule set carries attribution duties. |
| [oss-review-toolkit/ort](https://github.com/oss-review-toolkit/ort) | **Apache-2.0** | **2 109** | 393 | The orchestrated form of the same job: an *Analyzer* that *"determines the dependencies of projects and their metadata, abstracting which package managers are actually being used"*, plus an Evaluator for policy-as-code. 🟢 Pick `ort` when the client wants a **gate in CI**; pick `scancode` when they want the **evidence**. |
| [anchore/syft](https://github.com/anchore/syft) | **Apache-2.0** | **9 792** | 1 031 | SBOM generation from images and filesystems (SPDX, CycloneDX). The deployed-artefact view, where the other two read the source tree. |

🔵 **Five of the six rows above came out of a drop set, and the sixth off the
live promotion queue** — `catsim` had been described in **10** separate passes
and never filed; `ort`, `syft`, `fsrs.js` and `supermemo` are in the **349**
archive-only addresses `p531` triaged; `scancode` is in `archive-drops`, the
691-row looser bound. 🔴 **Four licence/SBOM instruments — `scancode`, `ort`,
`syft`, [`CycloneDX/cyclonedx-cli`](https://github.com/CycloneDX/cyclonedx-cli)
(Apache-2.0, 552★) — were owned, dropped, and then re-scoped as a build.** That
is `Gap 528-C`'s whole history, and it is a retrieval failure, not a supply gap.

## 🆕 Two platform rows the drop set also returned (`p531`)

| Repo | Licence | Stars | What it is |
|---|---|---|---|
| [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | **MIT** | **823** | *"Interactive Learning with Automated Feedback"*, from **TU München**. Programming, modelling, text and quiz exercises with automated assessment and an exam mode, in production across European universities. 🔴 **MIT, 823★, 395 forks, pushed today — and this base had no row for it.** The strongest permissive assessment platform in EMEA, and the natural alternative to bolting autograding onto Moodle. Ansible collection: [`ls1intum/artemis-ansible-collection`](https://github.com/ls1intum/artemis-ansible-collection) (MIT). |
| [opensacorg/learning-blocks](https://github.com/opensacorg/learning-blocks) | **MIT** | 6 | 🟢 **A second permissive Student Information System.** `p529` published *"zero permissive SIS"*; `p530` falsified it with `academico-sis/academico` (MIT, 409★). This is the third reading: the field is small and thin, but it is **not empty and not copyleft-only**. 22 forks against 6★ — more forks than stars, the signature of a system people deploy rather than star. Python. Pushed 2026-09-21. |

## 🆕 The LMS agent-bridge layer completes — Blackboard was the hole (`p532`)

Every row below came off the **ranked** promotion queue
([`../evidence/promotion-queue.2026-10-29-p532.tsv`](../evidence/promotion-queue.2026-10-29-p532.tsv)),
not off a search, and every grant was read this pass from the licence file's own
title block over `raw.githubusercontent.com`.

> 🔴 **The hole this closes.** This base has carried a Canvas bridge since `p490`
> (`canvas-mcp`, MIT, 308★), filed a Brightspace bridge at `p531`
> (`brightspace-mcp-server`, MIT, 60★), and censused the Moodle MCP field twice
> — while saying nothing about **Blackboard Learn**, which is one of the four
> LMS platforms a Western higher-ed engagement actually meets. The bridge
> existed, MIT-licensed, and this base had described it in **8 separate
> passes**.
>
> 🟡 **Read the star counts honestly.** `bb-mcp` is **2★** and
> `MarcosNahuel/moodle-mcp` is **1★**. These are not adopted projects; they are
> *correct starting points with a permissive grant*, which in this layer is the
> scarce thing — `p529` measured the Moodle MCP field at **222 addresses with a
> 52★ ceiling that is ungranted**. A studio forks one of these; it does not
> depend on it.

| Repo | Licence (title block) | Stars | Passes unfiled | Why it is foundational |
|---|---|---|---|---|
| [nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp) | 🟢 **MIT** — `MIT License · Copyright (c) 2026 nitsuah` (1 063 B, `e024d09e682a`) | 2 | 🔴 **8** | **The Blackboard Learn bridge this shelf had no row for.** A *standalone* MCP server wrapping the Blackboard Learn REST API — its README argues the case explicitly: *"the integration logic lives here, not in the client… build it once, use it everywhere."* Any MCP client (Claude Desktop, Cursor, agent-board) attaches unchanged. 🔵 With this row the agent-bridge layer covers **all four** major LMS platforms: Canvas, Brightspace, Moodle and Blackboard. |
| [MarcosNahuel/moodle-mcp](https://github.com/MarcosNahuel/moodle-mcp) | 🟢 **MIT** — `MIT License · Copyright (c) 2026 Italicia` (1 065 B, `f27341a8425b`) | 1 | 🔴 **9** | **The most capable Moodle MCP this base has read, and the field's own census said the ceiling was ungranted.** Wrapper **v0.5.2** + a companion Moodle plugin **v0.5.0**, exposing **40 high-level facades** plus one `ws_raw` escape hatch, over Moodle Web Services, with *idempotency guarantees* — its README claims ~80% of a course teaching workflow operable from an agent. 🟡 Spanish-language file paths and an `Italicia` copyright; **no country stated**, so unplaced. |
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 🟢 **MIT** — `MIT License · Copyright (c) Microsoft Corporation` (1 141 B, `c2cfccb812fe`) | 🔴 **78.1k** | 🔴 **23** | **Courseware, not an agent — and filed here for exactly that reason.** 18 lessons on building AI agents, with runnable Python on Microsoft Agent Framework and Foundry. For an education engagement this is the *reference curriculum artefact*: the thing to fork when a client wants an AI-literacy track with working code, and the thing to point at when asked what a well-structured 18-lesson technical course looks like. 🔴 **The single largest promotion debt in this base's history** — described in 23 passes, filed in none until now. |

## 🆕 The materiality-ranked queue's first eleven rows (`p533`)

Every row below came off
[`../evidence/promotion-queue.2026-10-29-p533.tsv`](../evidence/promotion-queue.2026-10-29-p533.tsv)
— the queue `Gap 532-B` asked for, gated on grant and liveness and ranked by
**measured** stars rather than by how often this base had mentioned the address.
Grants marked 🟢 were read this pass from the licence file's own title block over
`raw.githubusercontent.com`; the rest are API SPDX ids, flagged as such per shelf
rule 8.

> 🔴 **The queue's own headline: recall ranked an unusable address first and the
> largest permissive asset in this sector eighteenth.** See
> [`trending.md`](trending.md). The three A-band rows below had been described in
> this base **5, 7 and 7 separate passes** and filed in none.

| Repo | Licence | Stars | What it is, and why it is here |
|---|---|---|---|
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 🟢 **BSD-3-Clause** (`main/LICENSE.md`) | 🔴 **458,181** | *"freeCodeCamp.org's open-source codebase and curriculum."* 🔴 **The largest permissive asset this base has ever touched, by a factor of 32 over the next-largest unfiled address**, and it sat at recall rank 18. 🟡 **Read what it is before costing it in:** this is a **curriculum plus the platform that delivers it**, not a library — the reusable parts are the curriculum corpus, the challenge/test format and the certification model. BSD-3-Clause means all of it may be reused with attribution. 🔵 For an engagement that needs *content* rather than a tutor, this is the starting point, and `Gap 533-C` is the note that stars alone would overstate it. |
| [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | 🟢 **MIT** (`main/LICENSE`) | **14,372** | *"A framework for building, orchestrating and deploying AI agents and multi-agent workflows."* The successor line to AutoGen and Semantic Kernel. 🔵 Filed on the foundations leg rather than the agent shelf because it is **horizontal** — nothing in it is education-specific — but it is the orchestration layer most of this base's multi-agent patterns (`P549`, `P553`, `P558`) actually need, and it is MIT. |
| [frappe/frappe](https://github.com/frappe/frappe) | 🟢 **MIT** (`master/LICENSE`) | **11,024** | *"Low code web framework for real world applications, in Python and JavaScript."* 🔴 **The licence distinction this base has needed since `p526`:** the **framework** is MIT, while **Frappe Education and Frappe LMS on top of it are GPL-3.0 and AGPL-3.0** respectively (see the licence map below). So the platform is copyleft and the thing underneath it is not — which means a studio can build an education app *on Frappe* without inheriting Frappe Education's grant. 🔵 That is a genuinely different architecture decision from the one the licence map implied while only the apps were filed. |
| [autolab/Autolab](https://github.com/autolab/Autolab) | 🟢 **Apache-2.0** (`master/LICENSE`) | 808 | *"Course management service that enables auto-graded programming assignments."* From **Carnegie Mellon**. 🟢 **The autograder layer, which this base had no row for at all** — and it is permissive, which the rest of the layer is not (see `judge0` below). Ruby on Rails, with language-agnostic grading in containers. 🔵 Pairs directly with `Artemis`/`EduTelligence` as the North American analogue of the same idea; see `P567`. |
| [uPortal-Project/uPortal](https://github.com/uPortal-Project/uPortal) | 🟢 **Apache-2.0** (`master/LICENSE`) | 287 | *"Enterprise open source portal built by and for the higher education community."* Java. 🔵 The **student-facing front door** — the layer that aggregates LMS, SIS, calendar and announcements into one authenticated surface. For an engagement where the ask is *"one place where the student sees everything, with an agent in it"*, this is the permissive host, and nothing else on this base occupies that position. |
| [judge0/judge0](https://github.com/judge0/judge0) | 🔴 **GPL-3.0** (`master/LICENSE`) | **4,498** | *"Robust, fast, scalable, and sandboxed open-source online code execution system for humans and AI"* — its own topics include `ai-agent-tools` and `ai-agents`. 942 forks. 🔴 **Copyleft, and filed here anyway because the architecture answer is specific:** GPL-3.0 is **not** AGPL-3.0, so running Judge0 as a **separate self-hosted network service** that a proprietary deliverable calls over HTTP does not pull copyleft onto the deliverable, where `classroomio` (AGPL-3.0) would. 🔵 **Any agent that grades, runs or tests student code needs a sandbox, and this is the field's default one.** Deploy it beside the product, never inside it. |
| [webtech-network/autograder](https://github.com/webtech-network/autograder) | 🟢 **Apache-2.0** (`main/LICENSE`) | 62 | *"Flexible, Consistent and Powerful Autograding Tool that grades and generates feedback."* 🟢 The permissive, small-footprint alternative to the two rows above when the ask is grading *with feedback* rather than a full course-management system. |
| [opensalt/opensalt](https://github.com/opensalt/opensalt) | 🟢 **MIT** — 🔴 **ledger carried `GPL-3.0\|Apache-2.0`; corrected this pass** | 47 | *"Standards Alignment Tool."* Authoring, hosting and aligning academic standards (CASE/CFItem). 🔵 This is the repository that makes *"which standard does this question assess?"* answerable as data rather than as a prompt — the same job `corretor-enem` does for ENEM and `bncc-dev` for the BNCC, generalised. 🟢 **The grant correction matters:** it moved from "copyleft, check carefully" to permissive on one title-block read. |
| [1EdTech/OpenCASE](https://github.com/1EdTech/OpenCASE) | `Apache-2.0` (API) | 11 | *"Implementations of CASE Server and Editor"*, from **1EdTech** itself — the standards body. The reference implementation behind the row above. |
| [Ed-Fi-Alliance-OSS/Data-Management-Service](https://github.com/Ed-Fi-Alliance-OSS/Data-Management-Service) | `Apache-2.0` (API) | 12 | *"Code and design documentation for the Ed-Fi API Platform, successor to the Ed-Fi ODS/API."* 🔵 **North America's K-12 data-interoperability layer**, and the successor generation of it — the row to start from when an engagement's first problem is *"the student data is in six systems."* Its sibling [Ed-Fi-Alliance-OSS/edfi-oneroster](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) (Apache-2.0, 6★) serves a **OneRoster 1.2** API over an Ed-Fi ODS, and [theopenem/OneRoster.NET](https://github.com/theopenem/OneRoster.NET) (🟢 **MIT**, `master`) is the .NET client — 🔴 **one of the three addresses the API silently dropped this pass**, see shelf rule 14. |
| [open-edge-platform/education-ai-suite](https://github.com/open-edge-platform/education-ai-suite) | 🟢 **Apache-2.0** (`main/LICENSE`) | 2 | *"The Education AI Suite is a collection of open-source reference applications."* 🔵 **Two stars and worth more than its band suggests**, which is why `Gap 533-C` exists: this is **Intel's** `open-edge-platform`, so it is edge-and-on-premise reference architecture under a permissive grant, pushed **2026-10-29**. For `P600` (the disconnected classroom, `P565` until `p548`) and for any EMEA sovereignty engagement, vendor-backed on-prem reference code is scarcer than stars. |

🟡 **Also measured, also unfiled, and deliberately *not* promoted:**
[`tl-its-umich-edu/my-learning-analytics`](https://github.com/tl-its-umich-edu/my-learning-analytics)
(Apache-2.0, 37★, Univ. of Michigan — a learning-analytics dashboard, useful but
not a foundation), [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player)
(MIT, 30★, QTI 3 item player — a renderer, listed under the standards leg
already), and the three `learning-commons-org` repositories
([`knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph)
164★, [`evaluators`](https://github.com/learning-commons-org/evaluators) 87★),
which return **`NOASSERTION`** and so are **not yet graded** — per shelf rule 8
that means *the title block has not been read*, not that a grant exists. 🔴 They
are the highest-starred ungraded addresses left on the queue and the obvious
first read for `p534`.

## 🆕 `p534` — the institutional AI toolchain, off `Gap 533-A`'s org enumeration

`Gap 533-A` said this base's "is it filed?" test matches on the **address**, so
an institution that ships its platform in one repository and its intelligence in
another reads as *filed* the moment the platform is. 🟢 **Nine orgs already
cited on these pages were enumerated this pass** —
[`../evidence/org-layer-diff.2026-10-29-p534.tsv`](../evidence/org-layer-diff.2026-10-29-p534.tsv)
— and the three rows below are what came back that belongs on *this* page rather
than on the agent shelf. Grants read first-hand from the licence file's title
block, bytes and sha256 recorded in
[`../evidence/grant-reads.2026-10-29-p534.tsv`](../evidence/grant-reads.2026-10-29-p534.tsv).

| Repo | Licence (title block) | Stars | Fitness | Why it is foundational |
|---|---|---|---|---|
| 🆕 [mitodl/agent-kit](https://github.com/mitodl/agent-kit) | 🟢 **BSD-3-Clause** — `BSD 3-Clause License · Copyright (c) 2026, Tobias Macey` (1 499 B, `8afd1cd502a7`, `main` `431fde4`) | 5 | `infrastructure` | **The agent platform a real university's AI team actually runs.** Three `witan` packages — `witan-council` (work coordination), `witan-code` (a code graph for coding agents) and `witan-core` (shared memory) — plus the `agent-config-kit` CLI, reusable skills (`creating-skills`, `dependency-updates`, `deploy-verification`), custom agent definitions for **Claude Code and GitHub Copilot**, MCP install helpers (`witan-council`, `witan-code`, `toolhive-swe`) and six environment profiles. **551 commits**, docs on Read the Docs. 🔵 Education logic lives in [`mitodl/learn-ai`](https://github.com/mitodl/learn-ai); *this* is the plumbing under it, and BSD-3-Clause makes it the most permissively licensed institutional agent toolkit on this base. |
| 🆕 [Ed-Fi-Alliance-OSS/AI-Tools-for-Ed-Fi-SDLC](https://github.com/Ed-Fi-Alliance-OSS/AI-Tools-for-Ed-Fi-SDLC) | 🟢 **Apache-2.0** (11 357 B, `c71d239df917`, `main` `d42adc2`) | 🔴 0 | `reference-implementation` | *"Prompts, Skills, Hooks, Agents, etc. for use in the Ed-Fi Alliance software development lifecycle."* 🔵 Its value is **whose** SDLC it is: Ed-Fi governs the data standard that US K-12 student records move on, so this is the standards body publishing how it uses agents on its own codebase — a citable precedent for the governance conversation, which is the part of an education engagement that has no open-source answer anywhere else on this page. 🔴 Zero stars, pushed 2026-09-08. |
| 🆕 [pguso/agents-from-scratch](https://github.com/pguso/agents-from-scratch) | 🟢 **MIT** — `MIT License · Copyright (c) 2025 AI Agents from Scratch Contributors` (1 091 B, `f78cc6bf1d57`, `main` `da3f9df`) | **~1.1k** (page-rounded) · 262 forks | `curriculum` | **Twelve lessons building an agent from a single local LLM call** — text in/out, tools, the agent loop, memory, planning, **evals and telemetry** — with no frameworks, no cloud APIs and no hidden reasoning. Topics include `ai-education` and `open-source-education`. 🔴 **Filed as a `curriculum`, and the distinction is the point:** there is nothing here to deploy for a client. It ramps a studio team, on a local model, without an API budget. 🔴 **It is also the only new address generic web search has produced in seven passes** — and the search snapshot's **796★** against the page's **~1.1k** is a ~38 % disagreement, which is why no star figure on these pages is search-sourced. |

## 🆕 `p534` — a register claim this base has **refuted**, recorded rather than restored

🔴 **`make gate-prose-claims` reports `NO-PERMISSIVE-PLATFORM` as `CLAIM-LOST`**
— *"a declared gap that three patterns choose their base on"* — and asks this
file to carry the sentence **"No permissive education platform exists"**.

🟢 **It is recorded here as RETIRED, not restored, because this base's own
shelves disprove it.** Three permissive full learning platforms are filed on
this page:

| Platform | Grant | Stars |
|---|---|---|
| [oppia/oppia](https://github.com/oppia/oppia) | 🟢 **Apache-2.0** | 7.0k |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | 449 |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT** | 1.2k |

plus [sakaiproject/sakai](https://github.com/sakaiproject/sakai) under
**ECL-2.0**, an Apache-2.0 derivative that is permissive in practice.

🔵 **Why this is written down instead of simply dropped.** `p494` established
that a deleted claim is indistinguishable from coverage — so the honest
discharge of a refuted claim is a **dated retraction in the file that owed it**,
naming the evidence that killed it. 🔴 **And the register row should now be
retired**, because a gate that demands a false sentence will eventually be
satisfied by someone re-asserting it. → noted in
[`../intel/open-gaps.md`](../intel/open-gaps.md) under `Gap 534-I`.

## 🆕 `p535` — the efficacy layer: **causal inference**, which this base argued for and never held

🔵 **This section exists because of a contradiction inside this KB, not because of a
search.** [`../intel/trends.md`](../intel/trends.md) Trend 3 has argued since early passes
that *"pedagogy is becoming measurable and almost nobody is measuring it"*, and `p535`
added Trend 21: the **procurement gate is becoming causal evidence**, on a reported
review in which only ~**20 of 800+** K-12 AI studies produced strong causal evidence.
🔴 **Asked what it could hand a buyer who demands an effect estimate, this base held
nothing**: `openfun/ralph` (xAPI event capture) appears in it **157 times**, and
causal-inference libraries appeared **zero** times. Capturing events is not estimating
an effect, and the distinction is the whole of Trend 21.

| Repo | Grant (title block) | Stars | Fitness | What it is for here |
|---|---|---|---|---|
| [`py-why/dowhy`](https://github.com/py-why/dowhy) | 🟢 **MIT** | **8.4k** | `dependency` | Makes the causal **assumptions explicit and testable** — you state the graph (who got the tutor, what else differs between cohorts), and it refutes or survives that statement. This is the part a funder or ministry reviewer actually interrogates. |
| [`py-why/EconML`](https://github.com/py-why/EconML) | 🟢 **MIT** 🔴 *page names no licence; bytes do* | **4.8k** | `dependency` | **Heterogeneous** treatment effects — *who* did it help. In education this is the finding that matters: a null average effect that hides a large gain for the lowest-attaining quartile is a success story the average destroys. |
| [`comet-ml/opik`](https://github.com/comet-ml/opik) | 🟢 **Apache-2.0** | **23.0k** | `infrastructure` | Tracing and automated evaluation for the agent itself, so an effect estimate can be tied to **a known model, prompt and retrieval version**. 🔴 Filed only now: `p534` recorded Opik **by name** inside [`mitodl/learn-ai`](https://github.com/mitodl/learn-ai)'s production stack and never filed the repository. |

🟢 **All three are permissive, and that is the point.** An efficacy claim has to be
auditable by the buyer, which means the client must be able to **run and inspect** the
estimation code — MIT and Apache-2.0 allow that without the copyleft conversation the
rest of this sector forces. 🔵 They sit *beside*, not inside, the LMS: the estimation
runs on exported xAPI records, so the copyleft boundary this file keeps insisting on
(see the licence map below) is not touched.

🔴 **What this layer does not give you.** None of these three makes a weak design strong.
Observational estimation on a cohort that self-selected into using a tutor will produce a
confident, wrong number — which is plausibly how a field accumulates 800 studies and 20
credible ones. The design (assignment, a control arm, a pre-registered outcome) is
`P571`'s subject in [`../compose/patterns.md`](../compose/patterns.md); these libraries
are what you run **once the design is sound**.

## 🆕 `p536` — the institutional data plane, and the instruments that grade it

🔵 **None of these rows came from a search for a repository.** Three came from
enumerating an organisation this base has cited since `p1`, nine came from the
prose-address queue (`Gap 535-E`'s instrument,
[`../ingest/prose-address-ledger.py`](../ingest/prose-address-ledger.py)), and
four came from two topic-qualified API queries that replace the four mandated
global queries `Gap 535-A` retired. Every grant below was read from the licence
payload's **title block** over `raw.githubusercontent.com`, with the ref that
answered recorded —
[`../evidence/grant-title-block.2026-10-29-p536.tsv`](../evidence/grant-title-block.2026-10-29-p536.tsv).

### The Learning Commons stack — three repositories, three different grants

🔴 **Shelf row 3 of [`../agents/top.md`](../agents/top.md) is
`anthropics/k12-teacher-skills`, built *"with Learning Commons"*, and this base
filed none of Learning Commons' own repositories across 535 passes.** The
`agent-skills` third is shelved as an agent; the other two are here, and the
reason they are *here* rather than *there* is that neither is an agent — they are
the **rubric layer** and the **content layer** that an agent is pointed at.

| Repo | Grant (title block) | Stars | Fitness | What it is for here |
|---|---|---|---|---|
| 🆕 [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) | 🔵 **MIT code; data per-dataset — Open / Open + Gated / Gated.** Title line is *"This page explains the licensing framework…"*, 5 788 B at `main`. **API: `NOASSERTION`** | **164** · 23 forks | `dependency` | *"The data layer for smarter educational AI. Integrate trusted instructional content and research directly into your AI-powered tools."* 🟢 **The thing every tutor on the agent shelf needs and none of them ships**: academic standards, curriculum and instructional materials with provenance. 🔴 **Not vendorable as a corpus** — see the fifth verdict band on [`../agents/top.md`](../agents/top.md); treat it as an external data dependency with a per-row access type, which is `P572`. Pushed 2026-10-28. |
| 🆕 [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) | 🔵 **Code MIT · rubric content CC BY 4.0 · annotated corpora CC BY-NC-SA 4.0.** **API: `NOASSERTION`** | **87** · 17 forks | `dependency` | *"Evaluation for AI outputs against trusted educational rubrics."* 🟢 **This is the instrument Trend 3 has asked for since early passes** — research-backed rubrics a buyer can audit, in TypeScript, with 25 open issues and a push **inside this pass's own window**. 🔴 **The non-commercial half is the useful half for calibration**: annotated **CLEAR Corpus** and **PERSUADE 2.0** are the marked ground truth, and they are `CC BY-NC-SA`. Ship the rubrics, licence the corpora separately, or calibrate against `pedagogy-benchmark` instead. |

🔵 **Read the three grants together and the org's intent is legible**: the
*code* is permissive everywhere, the *rubrics* are permissive with attribution,
and the *marked corpora* are not. That is a rational position for a non-profit
holding licensed instructional content — and it means a studio can build the
pipeline and must negotiate the data.

### The efficacy layer gains its missing half: **assignment**

`p535` filed the estimation libraries (`dowhy`, `EconML`) and said in terms what
they do not give you: *"None of these three makes a weak design strong… The
design (assignment, a control arm, a pre-registered outcome) is `P571`'s
subject."* 🟢 **That component exists, it is Apache-2.0, and it runs inside the
LMS.**

| Repo | Grant (title block) | Stars | Fitness | What it is for here |
|---|---|---|---|---|
| 🆕 [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta) | 🟢 **Apache-2.0** — `Apache License Version 2.0, January 2004`, 11 323 B at `main`; **API agrees** | **21** · 9 forks | `dependency` | *"Tool for Education Research with RAndomized COnTrolled TriAls"* — an **LTI plug-in** that differentiates assignment content into experimental conditions and **randomises pupils to them inside the LMS they already use**, with informed consent hidden from the teacher, non-consenting participants filtered from summaries and exports, and student identifiers stripped on export. Java, default branch `development`, pushed **2026-10-29**. 🟢 **The randomisation, the consent handling and the de-identification are the three things a studio would otherwise build by hand and get wrong** — and the privacy design is what makes an RCT survive an EU AI Act Art. 10 conversation. 🔴 21★: fitness, not popularity. |
| 🆕 [`bydeng01/ability-levels-audit`](https://github.com/bydeng01/ability-levels-audit) | 🟢 **MIT** — `MIT License · Copyright (c) 2026 Shuyi Fan, Boyuan Deng, Mengyu Xu, Xinh…`, 1 153 B at **`master`**. 🔴 **API said `NOASSERTION`** | 4 | `reference implementation` | *"Code and frozen data for a pre-registered LLM-judge audit, with exploratory analysis of spurious DiD effects from bounded ratings."* **NeurIPS 2026 NewInML Workshop, arXiv:2608.27309.** 🟢 **The methodological warning a studio needs before it believes its own dashboard**: when the outcome is a bounded rating, difference-in-differences manufactures effects that are not there. 🔵 Pre-registered, with frozen data — reproducible in a way almost nothing in this sector is. |
| 🆕 [`bydeng01/conv-vs-ped-tutor`](https://github.com/bydeng01/conv-vs-ped-tutor) | 🟢 **MIT**, 1 149 B at `main`. 🔴 **API said `NOASSERTION`** | 3 | `reference implementation` | *"A pre-registered audit of LLM-judged helpfulness, answer leakage, and student independence across tutor models."* **arXiv:2607.28128**, LangGraph. 🟢 **`answer leakage` and `student independence` are the two failure modes every tutor on the agent shelf can exhibit and none of them measures**, and the repo's topics name `reward-hacking` outright: an LLM judge scoring *helpfulness* rewards the tutor that simply gives the answer. 🔵 Pair it with `evaluators` and `pedagogy-benchmark` and the eval story stops being a single judge's opinion. |
| 🆕 [`sonsoleslp/tna`](https://github.com/sonsoleslp/tna) | 🟡 **MIT — declared in the *manifest*, not the payload.** `DESCRIPTION`: `License: MIT + file LICENSE`; `LICENSE` is **45 B** of template parameters. 🔴 **API said `NOASSERTION`** | 13 | `dependency` | **CRAN** package `tna` **1.3.1**, *Transition Network Analysis*: models learning as **transitions between states over time** (Markov) rather than as a score, which is how you show a tutor changed a learner's *process*. R. 🔴 **The row that produced shelf rule 16** — three of this base's instruments disagree about it and all three are wrong. 🔵 Learning analytics and psychometrics ship in R; this is not the last CRAN grant this base will have to read. |
| 🆕 [`tl-its-umich-edu/my-learning-analytics`](https://github.com/tl-its-umich-edu/my-learning-analytics) | 🟢 **Apache-2.0**, 11 378 B, read at **`master`** (404 on `main`) | **37** · 39 forks | `dependency` | **MyLA** — the University of Michigan's student-facing learning-analytics dashboard, in production, **98 open issues against 39 forks**. 🟢 **More forks than stars, which on this base reads as institutions deploying it.** 🔴 A `main`-only reader grades it ungranted: second `Gap 535-C` instance of the pass. Python. |
| 🆕 [`edulinq/autograder-py`](https://github.com/edulinq/autograder-py) | 🟢 **MIT** — `Copyright (c) 2023 Eriq Augustine`, 1 070 B at `main` | 16 | `dependency` | The Python client for the EduLinq autograder server, **21 forks against 16 stars**, pushed 2026-10-02. 🟢 Completes the autograder layer `p533` opened: the server was filed, the interface students and CI actually call was named in a sentence on [`../intel/market.md`](../intel/market.md) and filed nowhere. |
| 🆕 [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | 🟢 **MIT** — `Copyright (c) 2022-2024 Amp-up.io, LLC`, 1 075 B at `main` | 30 | `dependency` | A 100 % JavaScript **QTI 3 item player** — the *delivery* half of the standards stack whose *authoring* half `p533` built an emitter for (`compose/code/p533-qti3-template-emitter/`). 🟢 Named in a sentence on this very file and filed in no table on it. 🟡 Pushed 2025-06-21 — 16 months stale; the standard moves slowly, so read that as settled rather than abandoned, and verify against your QTI version. |
| 🆕 [`CycloneDX/cyclonedx-cli`](https://github.com/CycloneDX/cyclonedx-cli) | 🟢 **Apache-2.0**, 11 340 B at `main`; **API agrees** | **552** · 86 forks | `infrastructure` | SBOM analysis, merging, diffing and format conversion. 🟢 **This is the instrument `Gap 528-C` has been costed against for eight passes** — the gap that says every 🟢 on these pages is a *repository-level* grant and this base has no way to enumerate **dependency** grants. `open-moodle` (MIT repo, AGPL-3.0 PyMuPDF in the artefact) is the standing proof it matters. 🔴 Named on this file and on [`../intel/market.md`](../intel/market.md) and filed in no table row. Pushed 2026-10-19. |

### The national data plane — four countries, four grants, all permissive

🔵 **This is the layer Trend 12 implies and this base has only ever held the
*product* end of.** An education agent that answers a question about a school
system needs that system's own data, and in four countries it is published as a
permissive repository.

| Repo | Grant (title block) | Stars | Region | What it is for here |
|---|---|---|---|---|
| 🆕 [`nso-india/esankhyiki-mcp`](https://github.com/nso-india/esankhyiki-mcp) | 🟢 **MIT** — `Copyright (c) 2026 Ministry of Statistics and Prog…`, 1 115 B at `main` | **147** · 28 forks | 🟢 **APAC (India)** — *stated in the copyright line*: the **Ministry of Statistics and Programme Implementation** | An **official government MCP server** over the eSankhyiki national statistics platform, pushed 2026-10-27. 🟢 **The first row on this base where a national statistical office ships the MCP itself** — not a third party scraping it. 🔵 For an engagement that must ground claims about enrolment, attainment or expenditure in the government's own figures, this is the shape to ask every ministry for, and the precedent to cite when asking. |
| 🆕 [`hantang/smartedu-dl-go`](https://github.com/hantang/smartedu-dl-go) | 🟢 **MIT** — `Copyright (c) 2024 hantang`, 1 063 B at `main` | **207** · 45 forks | 🟢 **APAC (China)** — *stated by the product* | Multi-platform downloader for the **国家中小学智慧教育平台** (national K-12 smart-education platform): textbooks as PDF, courseware, audio and video. Go. 🟢 **The largest-starred national-curriculum *ingest* tool on this base** — and the ingest step is the one `P560` and `lineage-skill` both assume someone else solved. 🟡 It is an access tool, not a licence: what it downloads carries the platform's own terms, which this base has **not** read and does not claim. |
| 🆕 [`cortega26/chile-hub`](https://github.com/cortega26/chile-hub) | 🟢 **MIT** — `Copyright (c) 2026 Carlos Ortega`, 1 069 B at `main` | **136** · 12 forks | 🟢 **LATAM (Chile)** — *stated by the product* | *"Datos públicos de Chile curados, normalizados y validados: geografía…"* — curated, normalised, validated Chilean public data, pushed 2026-10-26. 🟢 Pairs with the Colombian agent [`startin-lab/brujula-educativa`](https://github.com/startin-lab/brujula-educativa) (agent shelf) as the data half of the same pattern, and with the Chilean exam data already behind `pedagogy-benchmark`. |
| 🆕 [`openeduhub/edu-sharing-python-client`](https://github.com/openeduhub/edu-sharing-python-client) | 🟢 **Apache-2.0**, 11 348 B at `main` | 🔴 0 | 🟢 **EMEA (Germany)** — Open Edu Hub | Python client and connectors for the **edu-sharing** API — the OER repository layer German states run (WirLernenOnline). 🟢 Zero stars and the only permissive client for a national OER infrastructure on this base. 🔵 Filed on the attachment point, per `Gap 534-C`: a star gate cannot see a public-sector integration layer. |
| 🆕 [`openfun/arnold`](https://github.com/openfun/arnold) | 🟢 **MIT** — `Copyright (c) 2018-present GIP FUN MOOC`, 1 077 B, read at **`master`** | 41 · 10 forks | 🟢 **EMEA (France)** — *stated*: **GIP FUN MOOC**, France Université Numérique | Kubernetes deployment tooling for the FUN MOOC stack, pushed 2026-10-28. 🟢 Completes the `openfun` family already here (`ralph` LRS, `richie` CMS): CMS, learning-record store **and** the deployment that runs them, all MIT, all from the French national MOOC operator. 🔴 Third `Gap 535-C` instance of the pass. |
| 🆕 [`Turkish-AI-Community/hsd-agu-egitim`](https://github.com/Turkish-AI-Community/hsd-agu-egitim) | 🟢 **MIT** — `Copyright (c) 2026 Enes Fehmi Manan`, 1 072 B at `main` | 33 | 🟡 **EMEA (Türkiye)** — *inferred* from the org name and Turkish-language material | *"From Model to Agent"* mini-bootcamp project and teaching documents, Abdullah Gül University. 🟢 **Filed as a curriculum, explicitly not as an education-sector product** — the same honest classification `p534` gave `pguso/agents-from-scratch`. 🔵 It is the only Türkiye-origin address on this base, which is itself the finding: EMEA on these pages has meant Western Europe plus Morocco. |
| 🆕 [`RozhakDev/EduPintarIPAS`](https://github.com/RozhakDev/EduPintarIPAS) | 🟢 **MIT** — `The MIT License (MIT) · Copyright (c) 2025 Rozhak`, 1 092 B at `main` | 20 | 🟢 **APAC (Indonesia)** — *stated by the product* | Web chatbot for **IPAS** (integrated science) for Indonesian primary pupils. 🟡 Pushed 2025-08-10 — 14 months stale. 🔵 Filed beside `naufaldi/teacher-exam` (agent shelf, Indonesia): two Indonesian artefacts, one teacher-facing and one pupil-facing, both MIT, both naming the national curriculum by its own acronym — which is the texture Trend 12 predicts and a global query never returns. |

🔴 **Four rows this pass are copyleft or network-copyleft and are recorded here
rather than filed as buildable**, because an unstated exclusion looks like an
oversight: [`Schlaflied/Plot-Ark`](https://github.com/Schlaflied/Plot-Ark)
(**AGPL-3.0**, 13★ — curriculum operations over xAPI and Moodle, the closest
thing to `P558`'s output anyone has shipped),
[`brownplt/LTLTutor`](https://github.com/brownplt/LTLTutor) (**GPL-3.0**, 12★ —
Brown PLT, a *misconception*-based tutor, which is a sharper pedagogy than any
permissive row here), [`avps82/mentar`](https://github.com/avps82/mentar)
(**AGPL-3.0**, 0★ — local-first child tutor, *"no cloud, no accounts, no child
data leaving the device"*) and `openedx/openedx-ai-extensions` (AGPL-3.0,
carried from `p534`). 🔵 **All four are usable behind a service boundary and none
is vendorable into a proprietary deliverable** — Trend 14's point, four more
times, and note that **three of the four are 2026 projects**: the sector's
copyleft is a present-tense choice, not a legacy.

## Licence map, for the architecture decision

| Band | Repos |
|---|---|
| **Permissive — fork freely** | 🆕 **freeCodeCamp (BSD-3-Clause, 458k★)**, 🆕 **frappe/frappe (MIT)**, 🆕 **microsoft/agent-framework (MIT)**, 🆕 **Artemis + EduTelligence (MIT, TU München)**, 🆕 **Autolab (Apache-2.0, CMU)**, 🆕 **uPortal (Apache-2.0)**, 🆕 **webtech-network/autograder (Apache-2.0)**, 🆕 **opensalt (MIT)**, Oppia (Apache-2.0), OpenOLAT (Apache-2.0), Sakai (ECL-2.0), Kolibri (MIT), Dolos (MIT), Ralph (MIT), FSRS (MIT), 🆕 **ten of the eleven Moodle MCP codebases (MIT)** — G36maid, moodler-mcp, Faixiang, leshamblin, falkenslab, Jawadh-Salih, open-moodle*, moodle-student-mcp, duck-5 |
| **Weak copyleft — link across a boundary** | BigBlueButton (LGPL-3.0), OpenEduCat (LGPL-3.0) |
| **Strong copyleft — integrate, do not fork** | Moodle, Chamilo, ILIAS, H5P (GPL-3.0); 🔵 **Frappe Education (GPL-3.0)** — 🆕 but **`frappe/frappe`, the framework underneath it, is MIT**, so the copyleft is in the app, not the platform; i-educar, RosarioSIS, TAO (GPL-2.0); 🆕 **Judge0 (GPL-3.0)** — 🟢 **deploy it as a separate network service and the copyleft does not reach your deliverable**, because GPL-3.0 has no §13 |
| **Network copyleft — integrate, do not fork, and read §13** | Open edX, Canvas, Frappe LMS, Tutor, csmediapro/moodle-mcp-server (AGPL-3.0); **PyMuPDF (AGPL-3.0)** — reached *transitively* by the MIT-licensed `sonstellar969/open-moodle`; 🆕 **classroomio/classroomio (AGPL-3.0, 1,735★)** — the contrast that makes the Judge0 row's distinction concrete |

🔴 \* **`open-moodle` is MIT and still lands in the network-copyleft row in
practice**, because it links AGPL-3.0 PyMuPDF for PDF extraction. 🔵 **The rule:
the grant you ship is the union of the grants you link** — a repo-level licence
probe cannot see this, and this is the first instance of it recorded on the
platform legs.

AGPL-3.0 §13 reaches users interacting over a network, which is precisely the
hosted-SaaS shape most engagements want. **The integration seams — LTI 1.3, xAPI
via Ralph, H5P content, Canvas/Moodle REST, MCP servers — are where permissive
code belongs.**

## Searched and not found

- **No mainstream Apache/MIT-licensed LMS** beyond Oppia and OpenOLAT. Searched
  explicitly again; the sector is copyleft and that is the finding.
- **No permissively licensed SIS.** Every student-information system found is
  GPL-2.0 or GPL-3.0 — and `frappe/education`, the one genuinely unresolved cell
  on this file, resolved to **GPL-3.0** this pass rather than to something
  permissive. The AI-native advising option
  ([canyongbs/advisingapp](https://github.com/canyongbs/advisingapp)) is
  Elastic-2.0 and unusable as a hosted base.
- 🔴 **No credible Moodle MCP server — but not for lack of attempts.** See the
  census above: **eleven independent codebases, ten of them MIT, 37 stars
  between them, a 27★ ceiling** on the sector's biggest LMS. 🔵 Corrected from
  `p527`, which read the same field as *"roughly three real codebases."*
- 🆕 🔴 **No shared tool vocabulary for Moodle.** Eight tools in one server, ~230
  in another, and no two naming the same operations the same way. This is the
  actual missing artefact, and it is a specification rather than a product.
- **No APAC-origin platform core surfaced on the platform legs this pass.** APAC's
  open-source strength in education is on the *agent* legs (DeepTutor, OpenMAIC,
  lineage-skill, Educhain) — see [`../agents/top.md`](../agents/top.md). Moodle's
  Perth origin is historical and its governance is now global.
- **No LATAM-origin platform beyond i-educar and RosarioSIS's localisation.**

## 🆕 Gulf-origin supply — `Gap 536-D` answered, and the hole is a **grant** hole (`p537`)

`Gap 536-D` registered this base's largest adoption-to-supply gap: `p535` measured the
**UAE at ~75 % of teachers using AI in their work** — the highest figure in the whole
TALIS set this base holds — against **zero Gulf-origin repositories** in any curated
table. The gap prescribed `org:` and region-qualified search against named Gulf
institutions (KAUST, KFUPM, Khalifa, NYU Abu Dhabi, MBZUAI). 🟢 **It was run, it
returned supply, and the supply inverts the gap's premise.**

🔴 **The Gulf is not short of published education repositories. It is short of
ones a studio may build a product on.** Every grant below was read first-hand at the
resolved default branch.

| Address | Stars | Licence — read first-hand | Origin | Pushed | What it is |
|---|---|---|---|---|---|
| [`KAUST-Academy/Artificial-Intelligence-Courses`](https://github.com/KAUST-Academy/Artificial-Intelligence-Courses) | **443** · 88 forks | 🔴 **GPL-3.0** — `GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007`, **35 128 B** at `main` | 🟢 **EMEA (Saudi Arabia — KAUST Academy)** | 2026-10-22 | **The largest Gulf-origin education asset this base has found.** Jupyter-notebook AI curriculum, ~3.2 GB of tree. Taught with King Khalid University; the org's teaching line, not a research dump. 🔴 **GPL-3.0 on courseware is the hard case**: the grant binds derivative *teaching materials*, so a client-branded fork of this curriculum is a GPL-3.0 distribution |
| [`KAUST-Academy/2025_Artificial-Intelligence-Summer`](https://github.com/KAUST-Academy/2025_Artificial-Intelligence-Summer) | **279** | 🔴 **GPL-3.0** — 35 128 B at `main` | 🟢 **EMEA (Saudi Arabia)** | 2025-09-10 | The 2025 summer-school edition. Same grant, no longer maintained |
| [`KAUST-Academy/2026_Introduction_To_AI`](https://github.com/KAUST-Academy/2026_Introduction_To_AI) | **80** | 🔴 **GPL-3.0** — 35 128 B at `main` | 🟢 **EMEA (Saudi Arabia)** | 2026-01-16 | Current-year introductory track |
| [`KAUST-Academy/2026_Advanced_AI`](https://github.com/KAUST-Academy/2026_Advanced_AI) | **57** | 🔴 **GPL-3.0** — 35 128 B at `main` | 🟢 **EMEA (Saudi Arabia)** | 2026-02-07 | Current-year advanced track |
| [`KAUST-Academy/2026_KASP_Summer_School`](https://github.com/KAUST-Academy/2026_KASP_Summer_School) | 24 | ⛔ **No grant at 21 probed paths** on the resolved default branch | 🟢 **EMEA (Saudi Arabia)** | 2026-08-20 | Live, current, and **unusable** — absence of a grant is not permission |
| [`KAUST-Academy/weekly-ai-brief`](https://github.com/KAUST-Academy/weekly-ai-brief) | 18 | ⛔ **No grant at 21 probed paths** | 🟢 **EMEA (Saudi Arabia)** | 2026-10-27 | An automated weekly AI report, mailed on a schedule. 🔵 Interesting as a *pattern* (an institution running agentic content ops), unusable as a *dependency* |
| [`KAUST-Academy/2025_Advanced-Ai`](https://github.com/KAUST-Academy/2025_Advanced-Ai) | 47 | ⛔ **No grant at 21 probed paths** | 🟢 **EMEA (Saudi Arabia)** | 2025-03-13 | Prior-year advanced track, ungranted |
| [`mbzuai-oryx/groundingLMM`](https://github.com/mbzuai-oryx/groundingLMM) | **969** | 🟢 **Apache-2.0** — 11 356 B at `main` | 🟢 **EMEA (UAE — MBZUAI, Oryx lab)** | 2026-09-05 | **The one permissive Gulf asset of real size here.** GLaMM, a grounded large multimodal model (CVPR 2024). Not education-built — it is the *capability* layer a diagram-grading or worked-example tutor would sit on |
| [`mbzuai-oryx/OpenEarthAgent`](https://github.com/mbzuai-oryx/OpenEarthAgent) | **131** | ⛔ **No grant at 21 probed paths** | 🟢 **EMEA (UAE — MBZUAI)** | 2026-10-26 | ECCV 2026 tool-augmented geospatial agent framework. Pushed three days before this read and still ungranted |

🔴 **The measured shape, and it is the finding `536-D` was really asking for.**
Across the two leading Gulf AI institutions' public output, education-relevant supply is
**courseware under GPL-3.0** or **research code under no grant at all**. Of the nine rows
above, **one** (`groundingLMM`) carries a permissive grant, and it is not an education
project. 🔵 **So the Gulf engagement does not look like the LATAM or EMEA ones on
these pages.** There is no permissive vertical platform to fork and no MIT agent to
compose. What exists is:

1. **Curriculum under copyleft** — integrate and attribute, or license separately from
   the institution; do not fork into a client-branded product. This is the `Moodle` posture
   applied to *content* rather than code, and `Trend 41`'s adapter inversion applied to
   a syllabus.
2. **A capability model under Apache-2.0** — `groundingLMM` is buildable, and it is the
   only thing here that is.
3. **A grant-hygiene gap wide enough to be a service line.** Four of nine Gulf
   repositories, including two pushed within the last ten weeks, serve no licence at any
   probed path. 🟢 An institution that wants its work adopted and has not noticed
   this is a conversation, not a blocker.

🔵 **Declared gap, stated rather than left silent.** `Khalifa University`,
`KFUPM` and `NYU Abu Dhabi` were in `536-D`'s named list and returned **no
education-relevant repository** through the channels run here. A separate full-text leg
for Arabic-language education tooling returned **noise only** — twenty hits, of which the
single Arabic-specific one,
[`h9-tec/Awesome_Arabic_NLP`](https://github.com/h9-tec/Awesome_Arabic_NLP) (**258★**),
is a link list serving **no grant at 21 probed paths**, and is not Gulf-origin. 🔴
**There is no Arabic-language intelligent-tutoring repository on this base and this pass
did not find one.** That is an informed gap, not coverage.

## 🆕 Nine platform rows promoted off the prose queue — and two are archived upstream (`p537`)

Every row below was named in a *sentence* on a curated page and filed in **no** table
row on any of them. Grants read first-hand at the resolved default branch; stars, forks
and the **archived** flag from the repository-search channel.

| Address | Stars | Licence — read first-hand | Upstream state | What it is |
|---|---|---|---|---|
| [`jupyterhub/jupyterhub-tutorial`](https://github.com/jupyterhub/jupyterhub-tutorial) | **202** · 56 forks | 🟢 **BSD-3-Clause** — `BSD 3-Clause License · Copyright (c) 2017, Project Jupyter Contributors`, 1 527 B at **`master`** | 🔴 **ARCHIVED, read-only** | Deployment tutorial for JupyterHub. 🔴 **Do not start here in 2026** — it is filed so the next pass stops re-finding it, and the archived flag is the row's point |
| [`jupyterhub/yarnspawner`](https://github.com/jupyterhub/yarnspawner) | 19 · 14 forks | 🟢 **BSD-3-Clause** — `Copyright (c) 2018, Jim Crist`, 1 491 B at **`master`** | 🔴 **ARCHIVED, read-only** | Spawns single-user notebook servers into Hadoop/YARN containers. Dead, and only relevant to an on-prem Hadoop estate |
| [`jupyterhub/kerberosauthenticator`](https://github.com/jupyterhub/kerberosauthenticator) | 12 · 8 forks | 🟢 **BSD-3-Clause** — `Copyright (c) 2019, Jim Crist`, 1 491 B at `main` | 🟢 Live (pushed 2026-08-01) | Kerberos auth for JupyterHub. 🔵 **The row that earns its place in this trio**: Kerberos is what a university IT department actually runs, and this is the supported bridge to it |
| [`classroom-resources/autograding-python-grader`](https://github.com/classroom-resources/autograding-python-grader) | 11 · 14 forks | 🟢 **MIT** — `Copyright (c) 2023 GitHub`, 1 062 B at `main` | 🟢 Live | GitHub Classroom's Python autograder action. 🟢 **North America origin (GitHub), and vendor-maintained** — the cheapest credible grading substrate for a CS course, with no model call in it at all |
| [`classroom-resources/autograding-io-grader`](https://github.com/classroom-resources/autograding-io-grader) | 7 · 8 forks | 🟢 **MIT** — `Copyright (c) 2023 GitHub`, 1 062 B at `main` | 🟢 Live | Its stdin/stdout sibling: language-agnostic I/O grading |
| [`Ed-Fi-Alliance-OSS/Ed-Fi-AdminApp`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-AdminApp) | 🔴 **0** · 5 forks | 🟢 **Apache-2.0** — 11 356 B at `main` | 🟢 Live (pushed 2026-10-28) | Administrator UI for Ed-Fi Technology Suite deployments. 🟢 **North America (Ed-Fi Alliance)** — zero stars and actively developed on the same day it was read, which is what vendor-internal tooling looks like. Completes the Ed-Fi row set beside `Fiona` on the agent shelf |
| [`brownplt/LTLTutor`](https://github.com/brownplt/LTLTutor) | 12 | 🔴 **GPL-3.0** — `GNU GENERAL PUBLIC LICENSE Version 3`, **35 148 B** at `LICENSE.txt`, `main` | 🟢 Live (2026-07-28) | Misconception-based tutor for Linear Temporal Logic, from Brown University's PLT group. 🔵 **The research-grade exemplar of the only tutoring design this base rates**: it models *specific wrong beliefs*, not a generic mastery score. 🔴 GPL-3.0 — integrate, do not fork |
| [`Schlaflied/Plot-Ark`](https://github.com/Schlaflied/Plot-Ark) | 13 | 🔴 **AGPL-3.0** — `GNU AFFERO GENERAL PUBLIC LICENSE Version 3`, 34 522 B at **`master`** | 🟢 Live (2026-09-12) | *"Evidence-driven curriculum operations: turn learning signals into reviewable course changes, then track outcomes over time with knowledge graphs and long-term memory."* Moodle + xAPI + LightRAG + human-in-the-loop. 🔴 **AGPL-3.0 §13 — a hosted SaaS built on this owes source to its users** |
| [`avps82/mentar`](https://github.com/avps82/mentar) | 🔴 **0** | 🔴 **AGPL-3.0** — 34 522 B at `main` | 🟢 Live (2026-10-01) | *"OSS-first, local-first AI tutor for children — supplements school, never replaces it. No cloud, no accounts, no child data leaving the device."* Ollama / llama.cpp, Bayesian knowledge tracing. 🔵 **The child-data posture is the asset**, and it is the one an EU AI Act deployer or a COPPA-exposed district can actually defend. 🔴 Zero stars; AGPL-3.0 rules out a hosted product |

🔵 **The pattern across all nine, and it is why this section is not padding:** the
queue's residue is not junk — seven of nine are live and six carry a grant this base can
act on — but **two of nine were archived upstream and no instrument here would have said
so**. A promotion queue without an `archived` column promotes dead projects as
foundations. `Gap 537-A`.


## 🆕 Nine platform rows — the prose queue emptied, and placed in all four regions (`p538`)

`p537` left **twenty** addresses in the promotion queue. `p538` read every one
first-hand and filed the non-agent half here; the seven agent-grade ones went to
[`../agents/top.md`](../agents/top.md). 🔵 **Read the region column before the
star column.** This base's standing complaint is that its supply is APAC-heavy
and LATAM-thin, and this residue is the first promotion set that places rows in
**all four regions** — because a queue built from sentences inherits whatever
the sentences were about, and this base writes about every region.

⚠️ **Grants here are read from the repository page's own sidebar and title
block**, not from a licence-file probe: `curl` and the GitHub API are both
refused for this session, so the channel is the rendered page. A row marked
*"README only"* means the sidebar carried **no** licence entry.

| Address | Stars | Licence — read first-hand | Region (basis) | What it is |
|---|---|---|---|---|
| [`alterem/knowledge-grab`](https://github.com/alterem/knowledge-grab) | 🟢 **567** · 52 forks | 🟢 **MIT** — sidebar `MIT license` | APAC (China — Chinese-language description, targets a PRC national platform) | 🟢 **The highest-starred row this queue has produced, and it is a *data acquisition* tool, not an agent.** A Tauri + Vue 3 desktop app that downloads from 国家中小学智慧教育平台 (`basic.smartedu.cn`), the PRC's national K-12 resource platform: e-textbooks, course video and courseware, with video decryption and ffmpeg merge to MP4. 🔵 **Why it is load-bearing:** every tutoring agent needs a grounded corpus, and this is the only tool on this base that acquires a *national curriculum* corpus at scale. Pair it with a RAG stack and the curriculum-grounding pattern stops being hypothetical. ⚠️ Downloading from a state platform has terms this base has **not** read — the licence covers the *tool*, not the content. |
| [`h9-tec/Awesome_Arabic_NLP`](https://github.com/h9-tec/Awesome_Arabic_NLP) | **258** · 42 forks | 🟡 **CC BY 4.0 — README badge only.** The sidebar carries **no licence entry**; the grant is a badge reading `License: CC BY 4.0`. 🔵 **Fourth verdict band** — granted, but not under a code licence | 🟢 **EMEA (Gulf / Arabic-speaking)** — subject matter | *"The most comprehensive, up-to-date collection of Arabic NLP resources on the internet"* — models, datasets, tools, research and companies, with a dedicated **🎓 Tutorials & Learning Resources** section. 🟢 **The index `Gap 536-D` implied and the Gulf set did not supply.** `p537` found Gulf *code* to be copyleft or ungranted; this is the region's **map**, and at 258★ it is the most-used Arabic-NLP entry point in the open. 🔵 A content grant is right for an index and wrong for a dependency: cite it, do not vendor it. |
| [`oas114/EduShield`](https://github.com/oas114/EduShield) | 11 · 2 forks | 🟢 **MIT** — sidebar `MIT license` | APAC (Taiwan — Traditional-Chinese description) | 教育隱私保護系統 — *"Zero-Trust Data Anonymization Shield for AI."* De-identifies student text **before** it reaches a model and re-identifies the output after, as **a single static HTML file with no backend**, with an optional local-LLM scan via Ollama. 🟢 **The architecture is the finding.** Every data-protection pattern on this base assumes a service to deploy and an institution to run it; this one assumes neither, which is exactly the posture a school with no IT department can adopt. 🔵 **Composes with anything** — it sits in front of a model, so it is licence- and vendor-neutral. |
| [`dougpenny/SwiftyPSCore`](https://github.com/dougpenny/SwiftyPSCore) | 6 · 0 forks | 🟢 **MIT** — sidebar `MIT license` | 🟢 **North America** (PowerSchool is the dominant US K-12 SIS) | *"Swift interface for the PowerSchool API"* — a pure-Swift client handling authentication and response decoding against the PowerSchool SIS API. 🟢 **The first permissively granted SIS access layer on this base**, against a gap that has read *"no open-source SIS/advising agent under a permissive licence"* for many passes. 🔴 **It is a client, not an agent**, so it narrows that gap without closing it — the only full candidate (`advisingapp`) is still Elastic-2.0. ⚠️ README states it *"is not endorsed, sponsored, or affilitated with PowerSchool in any way"* (sic). Swift is also a constraint: an agent runtime in Python or TypeScript cannot link it directly. |
| [`shishiv/EDUCA`](https://github.com/shishiv/EDUCA) | 🔴 **1** · 0 forks | 🟢 **MIT** — sidebar `MIT license` | 🟢 **LATAM (Brazil)** — Portuguese-language README, targets *secretarias de educação* | *"A planilha da secretaria de educação não aguenta mais. O EDUCA aguenta"* — "the spreadsheet your school district runs on doesn't scale; EDUCA does." Schools, students, guardians, classes, enrolment and attendance in one place, with district-staff dashboards. TypeScript / Next.js. 🔵 **It names the actual LATAM baseline, which is a spreadsheet** — and that framing is more useful to an engagement than the code is. ⚠️ README states it is a **synthetic-data-only pilot foundation, not approved for real student data or production**. A reference implementation. |
| [`guruduan/SIMG`](https://github.com/guruduan/SIMG) | 🔴 **1** · 0 forks | 🟢 **MIT** — sidebar `MIT license` | APAC (Indonesia — Indonesian-language description) | A **Moodle plugin** (PHP 8.2) for school administration: teaching journals, homeroom-teacher journals, student leave letters, attendance recaps, counselling (BK) services and extracurriculars, with WhatsApp notifications through the Wablas API. 🟢 **Evidence for a claim this base makes and rarely substantiates: that Moodle's value is its plugin ecosystem.** This is a *national administrative practice* — BK counselling, Indonesian leave letters — encoded as a Moodle plugin under MIT. 🔵 **WhatsApp as the notification channel is the regional lesson**, not an implementation detail. |
| [`mizcausevic-dev/state-ai-disclosure-state-tracker`](https://github.com/mizcausevic-dev/state-ai-disclosure-state-tracker) | 🔴 **0** · 0 forks | 🟢 **MIT** — sidebar `MIT license`, README agrees | 🟢 **North America** (US state statutes) | *"Hash-chained per-state lifecycle record + reference verifier for EdTech AI products."* A v0.1 draft schema for an append-only per-state status record, plus a verifier. Names **Illinois SOPPA**, **California AB 1584** and **AB 2876**, **Texas HB 18** and **NY Ed Law 2-d**. ⚠️ Its own words: *"EdTech-readiness scaffolding, not certification."* The worked example covers **three** states. |
| [`mizcausevic-dev/pii-student-vault-contract-profile`](https://github.com/mizcausevic-dev/pii-student-vault-contract-profile) | 🔴 **1** · 0 forks | 🟢 **MIT** — sidebar `MIT license`, README agrees | 🟢 **North America** (FERPA / COPPA) | An EdTech profile of an *AI Procurement Decision Card* vault contract: maps **FERPA's 7 PII categories** and **COPPA's 10 PI categories** to vault targets, each with default retention and redaction rules and a **four-doctrine consent taxonomy**. Ships a `profile.json` and one example deployment. ⚠️ Same disclaimer — scaffolding, not compliance. |
| [`mizcausevic-dev/student-data-access-audit-stream`](https://github.com/mizcausevic-dev/student-data-access-audit-stream) | 🔴 **0** · 0 forks | 🟢 **MIT** — sidebar `MIT license` | 🟢 **North America** (FERPA §99.32) | *"Hash-chained event schema + reference verifier for AI tool reads of student records"* — a tamper-evident log of which tool read which record, when, under what legal basis and under which authorising Decision Card. A small Node verifier checks the hash chain and enforces tokenised student IDs and **FERPA §99.32** logging consistency. |

🟢 **The three `mizcausevic-dev` repositories are one asset, and this base has
nothing else like it.** Every US-regulation finding on
[`../intel/market.md`](../intel/market.md) — 134 bills across 31 states, the
amended COPPA rule's 22 Apr 2026 compliance date, Ohio's 1 Jul 2026 deadline —
is **demand-side intelligence with no supply-side answer**. These three are the
answer's shape: a per-state status record, a PII-category vault contract, and an
access audit stream, all MIT, all hash-chained, all composing into one
compliance spine. 🔴 **And all three are 0–1★ v0.1 drafts by a single author
with no adoption whatsoever.** 🔵 **So the correct use is as a specification,
not a dependency** — the FERPA-7 / COPPA-10 category mapping and the
§99.32 logging rule are the reusable parts, and they are the parts an engagement
would otherwise derive from statute by hand. Recipe in
[`../compose/patterns.md`](../compose/patterns.md).

🔵 **The pattern across all nine, and it is the one `p537` asked for.** `p537`
closed on `Gap 537-A`: a promotion queue with no `archived` column promotes dead
projects. 🟢 **None of these nine is archived** — every page rendered live. But
the sharper observation is about *region*: these nine place **3 in North
America, 3 in APAC, 1 in EMEA, 1 in LATAM** with one global index, against a
base whose supply has been APAC-dominated for its whole history. 🔵 **A queue
built from sentences inherits the regional spread of the prose, and this base's
prose is more balanced than its tables are.** That is a cheaper way to fix a
regional gap than another regional search leg — which this pass ran, four times,
and which returned nothing unfiled.
