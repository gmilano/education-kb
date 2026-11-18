## 🟢 `2026-11-18` (`p889`) — **a layer this KB has needed since `P4` was written, found for the first time: the EU AI Act conformance-instrument population. `46` repositories, star ceiling `9`, `42` of them created this year — and `0` of them are built for an education deployer, which is the finding, because education is the Annex III sector that owes the paperwork.**

🔵 **Channel:** `api.github.com/search/repositories` (`200` in this session) for discovery;
`raw.githubusercontent.com` (`200`) for every grant and every README, byte-read.
`api.github.com/repos/` is still `403`, so no row here depends on it.
Legs: `6` regulatory-keyword legs → `47` hits, `46` distinct repositories.
Grants byte-read: `25`. READMEs byte-read: `44`. Fetch failures: `0`.

### 🟢 Why this population was invisible to `888` previous passes

Every discovery leg this KB has ever run was scoped by **education** vocabulary. This layer is
scoped by **regulatory** vocabulary — `eu ai act`, `FRIA`, `annex`, `conformity assessment`,
`iso 42001`. The two vocabularies do not intersect: that is the whole explanation, and it is a
worked instance of `T-p885-2` (*the channel that still pays is structural, not lexical*). The
nine-pass nil on the prescribed keyword legs was never evidence that supply had stopped. It was
evidence that one vocabulary had been exhausted.

🔴 **The KB already held the obligations and none of the instruments.** `FRIA` and `Annex IV`
both appear on these shelves; `Article 27` appears once. Not one of the `46` repositories below
had ever been named here. `P4` (*EU AI Act conformance retrofit*) and `P11` (*AI-literacy duty
conformance pack*) are two of this base's highest-value sell patterns, and until this pass neither
named a single component that emits the evidence they promise.

### 🔴 The headline measurement: `0` of `46` target an education deployer

| Probe | Result |
|---|---|
| Repositories in population | `46` |
| READMEs byte-read | `44` (`2` have no README at any probed path) |
| Contain ≥1 education term | `23` (52%) |
| **Built for an education deployer** | **`0`** |

The `23` hits decompose, and every one of them is a non-targeting mention:

| Mechanism | Count | Evidence |
|---|---|---|
| `education` as an item inside a copied **Annex III enumeration** | ~`17` | `ShravaC/FRIA-O`: *"Anything used in an **Annex III** context — the Act's list of high-stakes areas: employment, education, essential…"* |
| **"educational purposes only"** liability disclaimer | `2` | `jessicavittorio-law/ai-governance-toolkit`: *"Educational use only. Not legal advice."* |
| Author's **university affiliation** | `1` | `Christospsa/…`: `christos.psaradellis@student.uva.nl`, *"University of Amsterdam – MSc Thesis Project"* |
| `schools` inside a **public-services enumeration** | `1` | `tjf-trojer/fria-editor`: *"private entities providing public services (contracted hospitals, schools,"* |

🔴 **So the keyword "education" has ~`52%` recall and ~`0%` precision over this population.** This
is the exact mirror of the false-absence class these shelves have tracked for dozens of passes: a
**false-presence** shape, and it has two independent generators. One is the Act's own text — every
conformance tool quotes Annex III, and Annex III contains the word *education*. The other is the
legal disclaimer every amateur compliance repo carries, in which *educational* means *do not sue
me*. A domain filter built on this keyword would have shelved `23` rows and been wrong `23` times.

### 🟢 The grants, byte-read — `21` resolved, `5` with no grant file at any probed path

| Repo | ★ | Grant (bytes read `2026-11-18`) | `sha256₁₂` | `B` | Pushed | What it actually is |
|---|---|---|---|---|---|---|
| [`Peaky8linders/specter-oss`](https://github.com/Peaky8linders/specter-oss) | 9 | 🔴 **MIT + vendored `CC BY-SA 4.0`** (metadata said `NOASSERTION`) | `3452606d6753` | `2,260` | `2026-07-27` | AI Act compliance toolkit: ontology, taxonomy, LLM-as-judge, grounded Q&A. **See the arity note below — do not read this row as "MIT".** |
| [`AbdelStark/eu-ai-act-toolkit`](https://github.com/AbdelStark/eu-ai-act-toolkit) | 8 | 🟢 `MIT` (stock) | `1126322e2cc8` | `1,056` | `2026-03-31` | Risk classification + conformity checklists. Highest-starred *clean* grant in the population. |
| [`uk-ai-compliance-os/iso42001-uk-eu-rapid-compliance`](https://github.com/uk-ai-compliance-os/iso42001-uk-eu-rapid-compliance) | 5 | 🔴 **NO GRANT** — `90 B`, two copyright lines, one an unfilled template placeholder | `b6b5b9cf5b0c` | `90` | `2026-06-10` | ISO 42001 + AI Act templates for UK companies. **Unusable — see below.** |
| [`Killerz007/cra-readiness-skill`](https://github.com/Killerz007/cra-readiness-skill) | 5 | 🟢 `Apache-2.0` (full text) | `c71d239df917` | `11,357` | `2026-11-02` | Agent-neutral skill for EU **Cyber Resilience Act** (Reg. 2024/2847) readiness. Adjacent instrument, not AI Act. |
| [`NISD2/eu-compliance-resources`](https://github.com/NISD2/eu-compliance-resources) | 3 | 🟡 `CC0-1.0` (Creative Commons Legal Code) | `a2010f343487` | `7,048` | `2026-06-24` | Curated index of EU cyber/data-protection compliance resources. Content, not code. |
| [`sjgant80-hub/fall-euaiact`](https://github.com/sjgant80-hub/fall-euaiact) | 3 | 🟢 `MIT` | `0ddf3b67a14a` | `1,067` | `2026-11-17` | Single-file browser compliance tool. **Live** — pushed the day before this pass. |
| [`8infinitelabs/eucompliance`](https://github.com/8infinitelabs/eucompliance) | 2 | 🔴 **`EUPL-1.2` by reference** (metadata said `NOASSERTION`) | `cb63267549d2` | `781` | `2026-04-08` | Bridges AI Act **and European Accessibility Act** — the only row touching the accessibility seam `P10` sells. |
| [`plusultra-tools/ai-act-conformity-pack`](https://github.com/plusultra-tools/ai-act-conformity-pack) | 2 | 🟢 `MIT` | `d0ed63bd2b39` | `1,071` | — | Emits **Annex IV** technical-documentation + **FRIA** evidence-pack scaffolds. Closest thing in the population to what `P4` needs. |
| [`tjf-trojer/fria-editor`](https://github.com/tjf-trojer/fria-editor) | 1 | 🔴 **`CC BY 4.0`** on a software repo (metadata said `NOASSERTION`) | `0f4efc167660` | `793` | `2026-07-18` | Reviews draft **Article 27 FRIAs**. A content licence on an editor — read before shipping. |
| [`pJijesh/ai-governance-toolkit`](https://github.com/pJijesh/ai-governance-toolkit) | 1 | 🟢 `MIT` | `91d440e19d27` | `1,080` | `2026-11-15` | Control matrix mapping **ISO/IEC 42001 + EU AI Act + NIST AI RMF**. Live. |
| [`leonkoellerwirth-arch/agentic-ai-governance-toolkit`](https://github.com/leonkoellerwirth-arch/agentic-ai-governance-toolkit) | 1 | 🟢 `MIT` | `a210993c213f` | `1,080` | `2026-09-02` | Lifecycle governance artefacts for **agents** in regulated organisations. |
| [`AI-Engineering-at/legal-scraper`](https://github.com/AI-Engineering-at/legal-scraper) | 3 | 🟢 `MIT` (branch `master`) | `108eaf63f414` | `1,071` | — | EU/AT/DE/CH legal aggregation with full-text search. |
| [`delschlangen/RegReady`](https://github.com/delschlangen/RegReady) | 2 | 🟢 `MIT` | `7131b83d49a0` | `1,070` | — | Translates regulatory text into engineering requirements. |
| [`JK-G/ai-content-labels`](https://github.com/JK-G/ai-content-labels) | 2 | 🟢 `MIT` | `62d22e90b07d` | `1,061` | — | **Article 50** AI-content labelling with the official EU icons. |
| [`portable-genai/ai-act-conformity-pack`](https://github.com/portable-genai/ai-act-conformity-pack) | 0 | 🟢 `Apache-2.0` (full text) | `ff0475891692` | `11,344` | `2026-11-14` | Maps each deployed agent in a registry to its obligations. 🔴 **Same repo NAME as the `plusultra-tools` row above, different owner, different grant** — do not conflate the two. |
| [`CSOAI-ORG/eu-cra-mcp`](https://github.com/CSOAI-ORG/eu-cra-mcp) | 0 | 🟢 `MIT` | `8e2d514c2809` | `1,099` | `2026-10-08` | Exposes CRA compliance **over MCP** — compliance as an agent-callable surface. New shape. |
| [`Authlyxio/sentinel-act`](https://github.com/Authlyxio/sentinel-act) | 0 | 🟢 `MIT` | `2c5aaf5d7eea` | `1,070` | `2026-09-18` | AI Act readiness toolkit. *"Not legal advice."* |
| [`jessicavittorio-law/ai-governance-toolkit`](https://github.com/jessicavittorio-law/ai-governance-toolkit) | 0 | 🟢 `MIT` | `21583c771fd3` | `1,073` | `2026-10-27` | Risk tiers + policy template. Lawyer-authored, explicitly educational-use-only. |
| [`gclottey/ai-governance-compliance-toolkit`](https://github.com/gclottey/ai-governance-compliance-toolkit) | 0 | 🟢 `MIT` | `9c9a2a1c61cf` | `1,065` | `2026-08-12` | Framework mapped to EU AI Act + NIST AI RMF + ISO. |
| [`sjgant80-hub/fall-euaiact-sdk`](https://github.com/sjgant80-hub/fall-euaiact-sdk) | 0 | 🟢 `MIT` — byte-identical to its sibling above | `0ddf3b67a14a` | `1,067` | `2026-11-17` | SDK half of `fall-euaiact`. Same grant bytes, same hash. |
| [`fatihsoysalcom/ai-system-risk-classifier`](https://github.com/fatihsoysalcom/ai-system-risk-classifier) | 0 | 🟡 `MIT` per metadata, not byte-read this pass | — | — | `2026-07-30` | Interactive Annex III risk-tier script. 🔵 Declared unverified rather than published as verified. |

🔵 **No grant file at any of `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING` on either `main` or
`master`:** `Ankit-Uniyal/eu-ai-act-compliance-toolkit` (7★), `RDNordic/eu-ai-compliance-toolkit`,
`ShravaC/FRIA-O`, `sabuhi-huseynli-grc/High-Risk-Deployer-FRIA-Governance-Toolkit.` (note the
trailing `.` in that slug — it is part of the name), `Christospsa/ai-act-ontology-compliance-framework`.
🔴 **Three of those five are the FRIA-specific ones** — the obligation an education deployer
actually owes under Article 27 has the worst-granted tooling in the population.

### 🔴 The row that must not be read as "MIT, 9★": arity introduced by VENDORING

`Peaky8linders/specter-oss` is the highest-starred repository in this population and its `LICENSE`
is `2,260 B` — roughly double a stock MIT text. The excess is not boilerplate. Byte-read, the file
carries the MIT grant **and then a second section**:

- the **OWASP APTS v0.1.0** catalogue shipped under `specter/apts/data/` is *"© OWASP Foundation and
  licensed under **CC BY-SA 4.0**"*;
- the Article 15 control structure in `specter/data/article_15_controls.py` *"follows the
  **LatticeFlow ATLAS** EU AI Act Article 15 framework"*, attributed but not granted;
- the Regulation (EU) 2024/1689 citations are asserted to be public-domain regulatory text.

🔴 **This is a THIRD arity shape, and `T29`–`T31` do not cover it.** `p886` found arity across
files, `p887` found it inside one file (conjunctive), `p888` found the disjunctive case. This is
arity introduced by **vendored data under share-alike**, where the reciprocal obligation attaches
to a *data directory* and not to the code at all. The consequence is commercial and concrete: a
Globant redistribution of this toolkit owes **share-alike on the shipped catalogue**, while the
code around it stays MIT. 🔴 **And the metadata channel said `NOASSERTION` — it gave no warning of
any of it.** A row that read `specter-oss · 9★ · MIT` would have been the most dangerous cell on
these shelves.

### 🔴 A `LICENSE` file that grants nothing, with the placeholder still in it

`uk-ai-compliance-os/iso42001-uk-eu-rapid-compliance` (5★) has a `LICENSE` of `90 B`. In full:

```
Copyright (c) 2026 [Your Name or Organisation]

Copyright (c) 2026 UK-EU AI Compliance OS
```

That is two copyright assertions and **no permission grant of any kind** — no MIT body, no licence
name, no SPDX identifier. One of the two lines is the **unfilled template placeholder**. GitHub's
metadata channel reports `NONE` and is right. 🔴 **The probe this refutes is this base's own
cheapest one: "a `LICENSE` exists at a probed path, therefore there is a grant."** Existence is not
a grant, and `200` on `raw.githubusercontent.com` is not a licence. The gate must read the bytes and
look for an operative permission clause, not a filename.

### 🟢 `Gap 252` (EUPL misclassification) — an instance, and the MECHANISM

`8infinitelabs/eucompliance` carries `781 B` at `LICENSE`. Byte-read it is unambiguous: the EUPL-1.2
operative preamble, the sentence *"The Work is provided under the terms of this Licence when the
Licensor … has placed the following notice … 'Licensed under the EUPL'"*, a pointer
`Full licence text: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12`, and
`SPDX-License-Identifier: EUPL-1.2`. The metadata channel reports **`NOASSERTION`**.

🟢 **So `Gap 252` is now diagnosed, not merely observed.** The mechanism is **incorporation by
reference**: GitHub's classifier matches licence *text*, and this grant supplies an SPDX identifier
plus a URL in place of the `~13,827 B` body that `T918` recorded on `hedy`. A valid, SPDX-declared
EUPL grant is therefore structurally invisible to the metadata channel. Every EUPL repository that
cites rather than quotes will present as ungranted.

🔴 **And it opens something worse.** The binding terms of that grant live at a
`joinup.ec.europa.eu` URL. This session **cannot resolve that host** (see the channel note below).
The grant is byte-read and its full terms are **unreadable here** — which matters directly, because
the notice set `P27`/`P30` exist to produce cannot be assembled from a grant whose text is a link.

### 🔴 Channel state, `p889` — and a sharpening of `T906` that changes what it means

| Host | DNS | HTTPS |
|---|---|---|
| `api.github.com` | ✅ resolves | `200` |
| `raw.githubusercontent.com` | ✅ resolves | `301`→`200` on file paths |
| `api.github.com/repos/{slug}` | ✅ resolves | 🔴 `403` (unchanged since `p882`) |
| `data.consilium.europa.eu` | 🔴 **does not resolve** | `000` |
| `eur-lex.europa.eu` | 🔴 **does not resolve** | `000` |
| `www.unesco.org` | 🔴 **does not resolve** | `000` |
| `www.multistate.us` | 🔴 **does not resolve** | `000` |

🔴 **`T906` has been recorded for ten passes as *"government domains refuse at `CONNECT`"*. That is
the wrong diagnosis and the wrong scope.** Measured this pass with `getent hosts` and `curl`
side by side: these hosts **fail DNS resolution entirely** — there is no connection to refuse. And
the set is not governmental. `www.multistate.us`, a commercial legislative tracker, fails
identically. The correct statement is: **this session resolves GitHub hosts and nothing else.**

🟢 **This retires a standing open action rather than deferring it again.** `T-p885-4`
(*"still no primary legal source, four passes running"*) is **not a research failure and no future
pass can close it by trying harder**. It is a network-policy boundary. Under the present
environment the only primary bytes reachable are those hosted on GitHub; every regulatory
instrument on these shelves is secondary-sourced **because it cannot be otherwise**, and must keep
saying so at the row. 🔵 **The one route that does exist:** regulatory text mirrored *into* a
GitHub repository is reachable and byte-readable. `Peaky8linders/specter-oss` vendors Article 15
control rows and AI Act citations; `AI-Engineering-at/legal-scraper` (MIT) aggregates EU/AT/DE/CH
legal full text. That is a GitHub-hosted primary-ish channel, and it is the only one this
environment permits.

### 🔴 The eight prescribed legs: run, and saturated — now MEASURED rather than asserted

All eight legs ran (4 global + 4 regional, current year computed as `2026`, never hardcoded). They
returned a large, genuinely useful body of demand-side facts. `p889` then tested `16` of the most
specific against the shelves **before** writing any of them:

`Regulation (EU) 2026/1744` · `Digital Omnibus` · `MOET Decision 2422` · `NC Session Law 2026-41` ·
`716 instruments / 23 countries` · `ST-14902-2026` · UNESCO LAC `Observatory` · `IESALC` ·
`134 bills` · `31 states` · `Ipsos` Education Monitor · `Berkeley Law` · Pearson/`Workera` ·
`2 December 2027` (Annex III) · `Idaho` · `Florida`.

🔴 **`16` of `16` were already held.** Not one is new. `p887`'s conclusion — that these legs are a
**policy instrument rather than a discovery one** — is now a measurement with a denominator, and it
holds for a tenth consecutive pass. 🟢 **The legs should keep running** (they confirm nothing has
*changed*, which is information) **but no pass should budget discovery against them.**

### 🟡 Supply side, five novel query shapes including two non-English — `90` new rows, `0` shelf-worthy

Beyond the regulatory legs, `p889` ran education-scoped shapes this KB had not used, including
`教育 AI エージェント`, `plataforma educativa inteligencia artificial` and
`agente educativo IA código abierto`, plus standards and MCP shapes. Result: **`90` repositories not
previously on these shelves.** The star ceiling among the education-native ones is `13`; the
overwhelming majority sit at `0`–`3` and are individual coursework projects
(`socratic-tutor`, `curriculum-generator`, `GradeOps` — the last of which appears **three times
under three different owners**, at `0`–`1★`, as independent reimplementations of the same idea).
🔴 **`0` earned a shelf row.** 🟢 **This corroborates `T12` from a new direction:** the long tail is
not a discovery deficit, it is the shape of the field. Non-English query shapes did not reveal a
hidden regional supply — they revealed the same long tail in other languages, which is itself the
answer to a question these shelves have asked for several passes.

🔵 **The LMS-MCP bridge population was re-measured and is fully held:** `18` distinct
Canvas/Moodle/Brightspace MCP servers surfaced (ceiling `boyuchengz/canvas-mcp`, 118★, MIT), and
**every one of them was already on these shelves or in `intel/open-gaps.md`**. No new bridge.

### 🔴 Two defects in `p889`'s OWN instruments, both caught before a cell was written

1. **`sort -t'\t' -k2,2nr -u` deduplicates on the KEY, not the line.** Run over the `47`-row sweep
   it returned `8` rows, silently collapsing every repository that shared a star count — and since
   `28` of `46` sit at `0★`, it destroyed most of the population. The output looked like a clean
   small result set, which is exactly why it was nearly published. 🟢 **Rule: `sort -u` first on the
   whole line, then sort by key. Never combine `-u` with a restricted `-k`.**
2. **A shell `sleep` inside a paced loop is killed in this harness.** Two paced sweep scripts died
   silently after `2`–`3` of `16`–`19` legs and **exited `0`**. The exit status was clean, the log
   was short, and nothing announced the truncation. 🟢 **Rule: pace inside a single interpreter
   process (`time.sleep` in one Python run), and verify a sweep by its LEG COUNT in the log, never
   by its exit status.** 🔵 This is the probable cause of any earlier pass whose sweep "nilled" —
   a truncated sweep and an empty channel are indistinguishable from the exit code alone.

### Controls

🔵 `0` fetch failures across `25` grant reads and `44` README reads. 🔵 Every grant in the table
above was read from `raw.githubusercontent.com` on `2026-11-18` and is recorded with its
`sha256₁₂` and byte length, so any later pass can detect drift without re-reading. 🔵 One row
(`fatihsoysalcom/ai-system-risk-classifier`) is published as **metadata-only and declared
unverified** rather than promoted to verified. 🔵 `0` rows in this pass carry a star count from a
blog or aggregator; all are from `search/repositories`.
