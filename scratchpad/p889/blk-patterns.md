## P31 — the Annex III education deployer's evidence pack: the one recipe where the verdict is BUILD

🔵 **Why this pattern exists, and why it is different from every other recipe on this page.** Every
other pattern here starts by adopting open source. `P31` starts by **refusing to**, and the refusal
is measured rather than asserted. `p889` discovered the EU AI Act conformance-instrument population
— `46` repositories reached by *regulatory* rather than *education* vocabulary, invisible to `888`
prior passes — and probed it for the one thing an education client needs
([`repos/trending.md`](../repos/trending.md#-2026-11-18-p889), `T34`):

| Probe | Result |
|---|---|
| Repositories in the population | `46` |
| Star ceiling | `9` (`28` rows at `0★`) |
| Created in 2026 / dormant 60+ days | `42` / `36` |
| No usable grant (missing, or present-but-empty) | `6` |
| FRIA-specific repos **with no licence file at all** | `3` of `4` |
| **Built for an education deployer** | **`0` of `46`** |

🔴 **So the obligation is binding and the supply is not there.** Education is an **Annex III**
high-risk sector. A deployer that is a public body — or a private provider of a public service,
which is how most contracted schools and many universities sit — owes an **Article 27 FRIA**. A
provider owes **Annex IV** technical documentation. 🟢 **This is the rare engagement where "we will
build this for you" is the honest answer and the defensible one**, because it rests on a denominator.

### Who this is sold to

An **EMEA** education deployer: a ministry, a public university, a school group, or an EdTech vendor
placing a product into them. 🔴 **Do not transplant it.** North America has no FRIA analogue — sell
the state-framework crosswalk there instead. LATAM has `716` instruments and almost no binding
education duty — sell readiness, not conformity. APAC has three binding instruments
(Vietnam `2026-03-01`, Korea `2026-01-22`, India `2026-02-20`) and `0` tooling for any of them, which
is a separate build with a per-jurisdiction column. See the regional sections in
[`intel/market.md`](../intel/market.md#opportunities-by-region).

### Stack — every grant byte-read `2026-11-18`, every hash recorded

| Layer | Component | Grant · `sha256₁₂` · `B` | Role |
|---|---|---|---|
| Document shapes | [`plusultra-tools/ai-act-conformity-pack`](https://github.com/plusultra-tools/ai-act-conformity-pack) | 🟢 `MIT` · `d0ed63bd2b39` · `1,071` | Annex IV technical-documentation + FRIA evidence-pack scaffolds. **Read and adapt — 2★, do not vendor as a dependency.** |
| Risk tiering | [`AbdelStark/eu-ai-act-toolkit`](https://github.com/AbdelStark/eu-ai-act-toolkit) | 🟢 `MIT` (stock) · `1126322e2cc8` · `1,056` | Annex III classification + conformity checklists. Cleanest grant in the population. |
| Multi-framework crosswalk | [`pJijesh/ai-governance-toolkit`](https://github.com/pJijesh/ai-governance-toolkit) | 🟢 `MIT` · `91d440e19d27` · `1,080` | ISO/IEC 42001 + EU AI Act + NIST AI RMF control matrix. The column structure a multi-region client asks for. |
| Agent governance | [`leonkoellerwirth-arch/agentic-ai-governance-toolkit`](https://github.com/leonkoellerwirth-arch/agentic-ai-governance-toolkit) | 🟢 `MIT` · `a210993c213f` · `1,080` | Lifecycle artefacts for agents in regulated orgs — needed the moment the deployment is agentic. |
| Obligations as a tool surface | [`CSOAI-ORG/eu-cra-mcp`](https://github.com/CSOAI-ORG/eu-cra-mcp) | 🟢 `MIT` · `8e2d514c2809` · `1,099` | Pattern reference only: a regulatory corpus exposed **over MCP**, so an agent can query obligations. Built for the CRA; the shape is what you copy. |
| Evidence spine | `P14`'s measurement spine | — | The FRIA needs *outcomes*, not intentions. Reuse it rather than rebuilding it. |
| Integration surface | `P29`'s standards stack (LTI 1.3, xAPI/cmi5) | — | Where the student-facing evidence is actually generated. |

🔵 **Deliberately excluded, with the reason at the row** — these are the traps, and naming them is
part of the deliverable:

| Excluded | Why |
|---|---|
| [`Peaky8linders/specter-oss`](https://github.com/Peaky8linders/specter-oss) (9★, the population's most-starred) | GitHub says `NOASSERTION`; bytes say MIT **+ vendored OWASP APTS catalogue under `CC BY-SA 4.0`** + a LatticeFlow ATLAS attribution. Redistribution owes **share-alike on shipped data**. Usable only after a `P30` arity triage prices that. |
| [`uk-ai-compliance-os/iso42001-uk-eu-rapid-compliance`](https://github.com/uk-ai-compliance-os/iso42001-uk-eu-rapid-compliance) (5★) | `LICENSE` is `90 B`: two copyright lines, one an **unfilled template placeholder**, and **no permission clause**. There is no grant. |
| [`8infinitelabs/eucompliance`](https://github.com/8infinitelabs/eucompliance) | **`EUPL-1.2` by reference** — reciprocal, and its binding text sits at a host unreachable here. Read it for the AI-Act↔Accessibility-Act mapping (`P10`); do not depend on the code. |
| [`tjf-trojer/fria-editor`](https://github.com/tjf-trojer/fria-editor) | Byte-read **`CC BY 4.0`** — a *content* licence on a software repo (metadata said `NOASSERTION`). |
| `ShravaC/FRIA-O`, `RDNordic/eu-ai-compliance-toolkit`, `Ankit-Uniyal/eu-ai-act-compliance-toolkit`, `sabuhi-huseynli-grc/High-Risk-Deployer-FRIA-Governance-Toolkit.` | **No licence file** at `LICENSE`/`.md`/`.txt`/`COPYING` on `main` or `master`. Three of them are the FRIA-specific ones. |

### How to wire it — six steps, and step 2 is the one that is actually hard

1. **Scope the deployer, not the model.** Establish on paper whether the client is a *deployer* or a
   *provider*, and whether it is a public body or a private provider of a public service. This single
   determination decides whether **Article 27** applies at all. Get it in writing from client counsel.
2. 🔴 **Build the evidence emitter.** Take the document shapes from
   `plusultra-tools/ai-act-conformity-pack` and the tiering logic from `AbdelStark/eu-ai-act-toolkit`,
   and write a generator that emits an Annex IV dossier and an Article 27 FRIA **from the running
   system's own telemetry** — not from a questionnaire. This is the reusable IP and the billable core;
   everything else on this page is scaffolding around it.
3. **Wire the crosswalk.** Load `pJijesh/ai-governance-toolkit`'s control matrix and add the client's
   jurisdiction column. For a multi-region client this is where ISO 42001 certification work and AI
   Act conformity stop being two projects.
4. **Attach the measurement spine (`P14`).** An FRIA that asserts fairness without outcome data is
   the artefact that fails first under scrutiny. The spine is not optional and must not be quietly
   dropped from the quote.
5. **Run the `P30` arity triage over the whole shipped tree** before anything leaves the studio, and
   emit the notice set `P27` defines. 🔴 **Expect it to fail on at least one component** — `p889`
   found a `CC BY-SA 4.0` data directory inside an "MIT" repo and a grant whose text is a URL.
6. **Hand over the regeneration path.** The dossier is worthless if it is a PDF from one afternoon.
   Ship it as a pipeline the client re-runs each release, with the generated artefacts under version
   control.

### What the client gets, and what to charge for

🟢 A regenerable Annex IV dossier and Article 27 FRIA bound to real system telemetry; a
jurisdiction-mapped control matrix usable for ISO 42001 at the same time; a licence notice set that
survives a procurement review; and a named, dated register of what was deliberately *not* used and
why. 🔵 **Charge for the emitter and the spine** (steps 2 and 4) — the checklists are commodity and
the client can read them on GitHub for free. 🔴 **Say plainly that the open-source layer is not
production-grade**: `46` repositories, ceiling `9★`, `36` dormant, `0` education-targeted. That
honesty is the differentiator, because the client's alternative vendor is quoting one of those `46`
as a product.

### 🔴 Two limits to state in the proposal, not after it

- **Every regulatory date in this KB is secondary-sourced**, and `p889` measured why: this
  environment resolves GitHub hosts and nothing else — `eur-lex.europa.eu`,
  `data.consilium.europa.eu`, `www.unesco.org` and even a commercial legislative tracker all fail
  DNS resolution. `T906` is corrected to that effect and `T-p885-4` retired as structurally
  unachievable. 🟢 **Operationally: client counsel verifies every date against EUR-Lex before the
  pack ships.** That is a line item, not a disclaimer.
- **The Annex III commencement date is contested across sources** (see
  [`intel/market.md`](../intel/market.md)), and the Digital Omnibus moved it. 🔵 Scope the engagement
  to the *obligation*, which is stable, and let the *date* be a client-counsel input — so a
  timetable change does not invalidate the deliverable.
