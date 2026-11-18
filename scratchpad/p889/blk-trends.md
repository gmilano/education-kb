## `T34` — the obligation and its instruments are produced by different populations, and only one of them knows about education

🔴 **Measured, `2026-11-18`: `46` repositories in the EU AI Act conformance-instrument population;
`0` built for an education deployer.** Education is an **Annex III** high-risk sector. An education
deployer that is a public body, or a private provider of a public service, owes an **Article 27
Fundamental Rights Impact Assessment**; a provider owes **Annex IV** technical documentation. Those
obligations are the most concrete commercial hooks in this entire KB — and the open-source layer
that emits the evidence for them was invisible to `888` previous passes.

🟢 **The reason it was invisible is the reason it matters.** Every discovery leg this base has run
was scoped by *education* vocabulary. This layer is scoped by *regulatory* vocabulary — `eu ai act`,
`FRIA`, `annex`, `conformity assessment`, `iso 42001`. The vocabularies do not intersect. 🔴 **This
is the sharpest instance yet of `T-p885-2`** (*the channel that still pays is structural, not
lexical*): the nine-pass nil on keyword legs measured the exhaustion of one vocabulary, and was read
as the exhaustion of supply.

| Property of the population | Measured | Consequence for a studio |
|---|---|---|
| Repositories | `46` | A real layer, not a one-off. |
| Star ceiling | `9` | No row has a community. `28` sit at `0`. |
| Created in 2026 | `42` | Deadline-driven, not engineering-driven. |
| Pushed in last 60 days | `10` | `36` already dormant. |
| Ungranted or grant-empty | `6` | Three of four FRIA-specific repos among them. |
| Education-targeted | **`0`** | **The sector that owes the paperwork is served by none.** |

🟢 **So the verdict inverts this base's default.** These shelves exist to find what to adopt. Here
the measurement says **BUILD**: the obligation is binding, the supply ceiling is `9★`, four fifths
of it is dormant, and none of it addresses the sector. `P31` is that recipe. 🔵 The claim is
defensible to a client because it rests on a denominator, not on an absence of search results.

## `T35` — `T14`'s mirror: the FALSE-PRESENCE class, and a domain keyword can have `0%` precision

🔴 **`T14` taught this base that `NOASSERTION` is not a licence finding — a false *absence*. `p889`
found the mirror.** Probing `44` READMEs in the conformance population for education vocabulary:
**`23` hit — and all `23` are false presences.** Three independent generators, each byte-quoted:

| Generator | Count | What the keyword actually was |
|---|---|---|
| **Annex III enumeration** copied from the Act | ~`17` | *"the Act's list of high-stakes areas: employment, **education**, essential…"* — the Act's own text contains the word. |
| **"educational purposes only"** liability disclaimer | `2` | *"**Educational** use only. Not legal advice."* — here *educational* means *do not sue me*. |
| Author's **university affiliation** | `1` | `…@student.uva.nl`, *"University of Amsterdam – MSc Thesis Project"*. |

🟢 **Recall ~`52%`, precision ~`0%`.** A domain filter built on this keyword would have shelved `23`
rows and been wrong every time. 🔴 **The generalisation, which is not about education:** when a
population is defined by a *regulation*, the regulation's own enumerations inject every regulated
sector's vocabulary into every document in it. **A keyword cannot distinguish "this tool is for
sector X" from "this tool quotes a list that contains sector X."** 🟢 **Gate rule:** domain
targeting must be read from what the tool *does* — its inputs, its outputs, its named systems —
never from the presence of a sector noun. And where a sector noun appears, check first whether it
sits inside a quoted legal enumeration or a liability disclaimer.

## `T36` — a grant can incorporate its terms by URL, and then it is byte-read but unreadable

🟢 **`p886` established that a licence is a SET. `p887` found the set inside one file. `p888` split
`|set| > 1` into conjunctive and disjunctive. `p889` adds a property orthogonal to all three:
a grant may be COMPLETE and still not CONTAIN its own terms.**

`8infinitelabs/eucompliance` carries `781 B` at `LICENSE`: the EUPL-1.2 operative preamble, the
sentence *"The Work is provided under the terms of this Licence when the Licensor … has placed the
following notice … 'Licensed under the EUPL'"*, `SPDX-License-Identifier: EUPL-1.2`, and
`Full licence text: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12`. It is a valid
grant. Its binding body is a URL.

🟢 **This diagnoses `Gap 252` (EUPL misclassification), open and untouched for several passes.** The
mechanism is incorporation by reference: GitHub's classifier matches licence *text*, so a grant that
**cites** the `~13,827 B` EUPL body — the length `T918` recorded on `hedy` — instead of **quoting**
it presents as `NOASSERTION`. 🔴 **Every EUPL repository that cites rather than quotes reads as
ungranted**, and `EUPL-1.2` is the European family, so this misclassification is concentrated
exactly in the region whose procurement rules care most about it.

🔴 **And it compounds with the channel boundary.** `joinup.ec.europa.eu` does not resolve in this
session. The grant is read; its terms are not reachable. 🔴 **A notice set cannot be assembled from
a grant whose text is a link** — which is a direct, unbudgeted constraint on `P27` and `P30`.
🟢 **Gate rule:** classify a grant by its SPDX identifier and operative clause when present, treat
byte length as *evidence of form, never of validity*, and flag `incorporation-by-reference` as its
own state — distinct from both *granted-and-read* and *ungranted*.

### 🔴 `T906` corrected, and `T-p885-4` retired

🔴 **`T906` has said for ten passes that "government domains refuse at `CONNECT`". Both halves are
wrong.** Measured `2026-11-18` with `getent hosts` beside `curl`: `data.consilium.europa.eu`,
`eur-lex.europa.eu`, `www.unesco.org` and `www.multistate.us` **fail DNS resolution** — there is no
connection to refuse — and the last of those is a commercial tracker, so the failing set is not
governmental. **The correct statement: this session resolves GitHub hosts and nothing else.**

🟢 **`T-p885-4` (*"still no primary legal source, four passes running"*) is therefore RETIRED as
structurally unachievable rather than carried a fifth time.** It is a network-policy boundary, not a
research failure, and no later pass should spend budget on it. Every regulatory instrument on these
shelves is secondary-sourced **because it cannot be otherwise**, and must keep saying so at the row.
🔵 **The single channel that does exist:** regulatory text mirrored *into* a GitHub repository is
reachable and byte-readable — [`AI-Engineering-at/legal-scraper`](https://github.com/AI-Engineering-at/legal-scraper)
(MIT) aggregates EU/AT/DE/CH legal full text, and `Peaky8linders/specter-oss` vendors Article 15
control rows. That is the only primary-ish route this environment permits.
