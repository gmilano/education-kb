#### Update 2026-11-15 (thirty-third pass, `p828`) — the PRIVATE half of the Brazilian market gains its first row, the Q-Acadêmico and SUAP legs are filed, and the cluster's upstream is found UNMAINTAINED

🟢 **First-hand, byte-read `2026-11-15`. Four structural additions to a tier this base opened at
`p812`:**

- 🟢 **The private-sector half, for the first time.** Every LATAM row before this pass sat on a
  PUBLIC federal or state institution running SIGAA.
  [`Eduardozsw/cds-tools`](https://github.com/Eduardozsw/cds-tools) (MIT) is a read-only CLI and
  MCP for **Blackboard Ultra at Cruzeiro do Sul / Unipê** — one of Brazil's largest *private*
  university groups. 🔵 **Different buyer, different procurement, different LMS: the public tier's
  findings do not transfer to it unexamined.**
- 🟢 **The Q-Acadêmico leg, named here many times and never shelved.**
  [`adiel-calixto/IFAcademico`](https://github.com/adiel-calixto/IFAcademico) (Apache-2.0, `6★`) —
  Android client for the academic system used across the **Institutos Federais**.
- 🟢 **The SGA↔Moodle seam.**
  [`suap-ava-suite/djangoapp-integrador_ava`](https://github.com/suap-ava-suite/djangoapp-integrador_ava)
  (MIT, 🇧🇷 IFRN) is middleware joining **SUAP** natively — plus a generic profile for **SIGAA**
  and **Q-Acadêmico** — to **Moodle**. 🔴 **Its README declares it development-use-only at IFRN,
  so it is a SPECIFICATION, not a deployable.** 🟢 **It is nonetheless the only artefact on these
  shelves that joins the Brazilian system of record to the LMS — the exact seam a Brazilian
  engagement sits on.**
- 🔴 **And the risk under all of it.** [`GeovaneSchmitz/sigaa-api`](https://github.com/GeovaneSchmitz/sigaa-api)
  — MIT, `61★`, `22` forks — is the **upstream** of the cluster (`heitorsDev/sigaa-ifsc-mcp`
  states it ported navigation and extraction from it). 🔴 **Last push `2024-04-10`: roughly `19`
  months stale.** 🟢 **The whole Brazilian SIGAA tier's lineage traces to one unmaintained MIT
  library. Adopting the tier means inheriting it — and maintaining it is a small, cheap,
  nameable deliverable that would make a studio the de facto steward of the layer.**

🔴 **Regulatory and market, `CITED, NOT READ`** (WebSearch summaries, `2026-11-15`):

- 🇧🇷 **`PL 2338/2023`** — already held here — **classifies educational evaluation as HIGH-RISK and
  would require a prior algorithmic impact assessment**; passed the Senate (Dec 2024), still
  awaiting the Chamber of Deputies. 🔵 **Same direction of travel as Annex III, so a connector
  built to `P68`'s gated write path is being built to BOTH regimes at once.**
- 🇲🇽 **NEW to this base — the `Chapultepec Principles`**, a ten-point ethical framework for AI use
  and development presented by **SECIHTI and the ATDT on `2026-01-29`**. 🔴 Mexico still has **no
  enacted AI statute**; a bill introduced `2026-02-11` would create a specialised regulator able to
  classify systems by risk and impose sanctions. 🔴 **Sources conflict on whether 2026 amendments
  already create binding obligations — recorded as CONTESTED and not resolved this pass.**
- 🇲🇽 **NEW — capacity, not regulation: the Public AI Training Center** operated by **INFOTEC and
  TecNM** with `14` technology partners, targeting **`10,000` specialists graduated in 2026**.
  🔵 **This base has repeatedly recorded a LATAM talent deficit as the binding constraint; this is
  the first named state-run instrument aimed squarely at it, and it is a partnership surface.**
- 🇵🇪 **Peru remains the only country in the region with an enacted AI law**; UNESCO operates an
  AI-in-education observatory for Latin America and the Caribbean.

🔴 **The Spanish-speaking gap, re-measured and NOT closed.** Spanish-language LATAM supply exists
but is **unlicensed**: `sebassg/sia-unal-mcp` (🇨🇴 SIA UNAL),
`Anggelie/mcp-local-server-uvg` (🇬🇹 UVG), `JuancitoCozzeti24/santa-rita-escolar`
(🇵🇪 Google Classroom + **SieWeb**) and `KaioBorgesDev/siga-mcp` (🇧🇷 Centro Paula Souza) all carry
**NO licence file** and are therefore **not build-safe**. 🟢 **The remedy is not a rewrite — it is
a licence request to four named maintainers**, which is a far cheaper first task than it looks.
