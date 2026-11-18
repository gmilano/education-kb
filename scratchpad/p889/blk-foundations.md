## 🆕 `p889` · 2026-11-18 — what changed on this shelf

🔴 **A whole layer entered this base's field of view, and this shelf's verdict on it is DO NOT
ADOPT.** `p889` discovered the **EU AI Act conformance-instrument population** — `46` repositories,
`25` grants byte-read, `0` fetch failures (full measurement in
[`repos/trending.md`](trending.md#-2026-11-18-p889)). `P4` and `P11` have promised Annex IV and FRIA
evidence for several passes without naming a component that emits it. This is that component layer.
It is not foundation-grade, and the numbers are the argument:

| Property | Measured `2026-11-18` | Why it disqualifies the layer |
|---|---|---|
| Star ceiling | **`9`** | No row has a user community. `28` of `46` sit at `0`. |
| Created in 2026 | **`42` of `46`** | The layer is a reaction to a regulatory deadline, not an engineering tradition. |
| Pushed in the last 60 days | **`10` of `46`** | `36` are already dormant, months after creation. |
| No grant at any probed path | **`5`** | Includes **three of the four FRIA-specific repos**. |
| Grant present but **empty of permission** | **`1`** | `uk-ai-compliance-os/…` — `90 B`, see below. |
| Built for an education deployer | **`0`** | The sector that owes the paperwork is served by none of them. |

🟢 **The four rows a studio may touch, with the condition attached.** These are scaffolds to read and
adapt, not dependencies to take:

| Repo | ★ | Grant (byte-read `2026-11-18`) | `sha256₁₂` · `B` | Live | What it gives you |
|---|---|---|---|---|---|
| [`AbdelStark/eu-ai-act-toolkit`](https://github.com/AbdelStark/eu-ai-act-toolkit) | 8 | 🟢 `MIT` (stock) | `1126322e2cc8` · `1,056` | `2026-03-31` | Risk classification + conformity checklists. The cleanest grant in the population. |
| [`plusultra-tools/ai-act-conformity-pack`](https://github.com/plusultra-tools/ai-act-conformity-pack) | 2 | 🟢 `MIT` | `d0ed63bd2b39` · `1,071` | — | **Annex IV** technical documentation + **FRIA** evidence-pack scaffolds. Closest in the population to what `P4` needs. 🔴 Do not confuse with [`portable-genai/ai-act-conformity-pack`](https://github.com/portable-genai/ai-act-conformity-pack) — same repo NAME, different owner, `Apache-2.0` (`ff0475891692`, `11,344 B`). |
| [`pJijesh/ai-governance-toolkit`](https://github.com/pJijesh/ai-governance-toolkit) | 1 | 🟢 `MIT` | `91d440e19d27` · `1,080` | `2026-11-15` | Control matrix mapping **ISO/IEC 42001 + EU AI Act + NIST AI RMF** — the three-framework crosswalk a multi-region client asks for. |
| [`AI-Engineering-at/legal-scraper`](https://github.com/AI-Engineering-at/legal-scraper) | 3 | 🟢 `MIT` (branch **`master`**) | `108eaf63f414` · `1,071` | — | EU/AT/DE/CH legal full-text aggregation + search. 🔵 **Operationally the most interesting row on this page** — see the channel note. |

### 🔴 `90 B` at `LICENSE`, and it grants nothing

[`uk-ai-compliance-os/iso42001-uk-eu-rapid-compliance`](https://github.com/uk-ai-compliance-os/iso42001-uk-eu-rapid-compliance)
(5★) has a `LICENSE` file whose entire contents are two copyright lines — one of them the
**unfilled template placeholder** `Copyright (c) 2026 [Your Name or Organisation]` — and **no
permission clause of any kind**. 🔴 **This refutes this base's cheapest grant probe:** *"a `LICENSE`
exists at a probed path, therefore there is a grant."* `200` on `raw.githubusercontent.com` is file
existence, not permission. 🟢 **Rule for every later pass: a grant verdict requires an operative
permission clause in the bytes, not a filename and not a status code.**

### 🟢 The only primary-source channel this environment permits, and it is GitHub

🔴 **`T906` has been recorded for ten passes as "government domains refuse at `CONNECT`". That
diagnosis is wrong and its scope is wrong.** Measured this pass with `getent hosts` beside `curl`:
`data.consilium.europa.eu`, `eur-lex.europa.eu`, `www.unesco.org` and the commercial tracker
`www.multistate.us` **all fail DNS resolution** — there is no connection to refuse, and the failing
set is not governmental. **This session resolves GitHub hosts and nothing else.**

🟢 **So `T-p885-4` ("still no primary legal source") is retired as structurally unachievable**, not
deferred for a fifth pass. No amount of effort closes it; it is a network-policy boundary, and every
regulatory row on these shelves is secondary-sourced because it cannot be otherwise. 🔵 **The one
exception, and the reason `legal-scraper` is on the table above:** regulatory text mirrored *into* a
GitHub repository is reachable and byte-readable. That is the only primary-ish channel available
here.

🔴 **And it bites the licence channel too.** `8infinitelabs/eucompliance` carries a valid
`EUPL-1.2` grant in `781 B` that incorporates its terms **by reference** —
`SPDX-License-Identifier: EUPL-1.2` plus a pointer to `joinup.ec.europa.eu`, a host this session
cannot resolve. The grant is byte-read and its **full terms are unreadable here**, which directly
blocks the notice set `P27`/`P30` exist to assemble. 🟢 **This also diagnoses `Gap 252` (EUPL
misclassification): the mechanism is incorporation by reference.** GitHub's classifier matches
licence *text*; a grant that cites the `~13,827 B` EUPL body instead of quoting it presents as
`NOASSERTION`. Every EUPL repository that cites rather than quotes will read as ungranted.

### 🔴 Declared BUILD gap — the shelf entry this layer actually earns

There is **no permissive, maintained, education-scoped Annex IV / Article 27 evidence emitter**.
`46` repositories were probed for one and none exists. 🟢 **This is the rare case where the correct
studio verdict is BUILD, not ADOPT**, and it is defensible to a client with the numbers above:
the obligation is binding on education deployers, the OSS supply has a star ceiling of `9`, `36` of
`46` are dormant, and `0` address the sector. Recipe: `P31` in
[`compose/patterns.md`](../compose/patterns.md).
