## 🆕 `p889` · 2026-11-18 — what changed on this shelf

🔴 **`0` new agent rows, and the reason is a category error this shelf was at risk of making.**
`p889` found a `46`-repository population that no previous pass had seen — the **EU AI Act
conformance-instrument layer** (full measurement in
[`agents/trending.md`](trending.md#-2026-11-18-p889)). It is tempting to shelve it here, because
`P4` and `P11` need it and because `12` of the `46` are MIT. It does not belong here: these are
checklist generators, risk classifiers and document emitters, not agents. Two rows are the
exception and are recorded as *adjacent*, not as education agents:

| Repo | ★ | Grant (byte-read `2026-11-18`) | `sha256₁₂` | Why it is agent-shaped |
|---|---|---|---|---|
| [`CSOAI-ORG/eu-cra-mcp`](https://github.com/CSOAI-ORG/eu-cra-mcp) | 0 | 🟢 `MIT` · `1,099 B` | `8e2d514c2809` | Exposes EU **Cyber Resilience Act** compliance over **MCP** — a regulatory corpus as an agent-callable tool surface. 🔵 A new shape for this base: not an agent, but the thing an agent calls. |
| [`leonkoellerwirth-arch/agentic-ai-governance-toolkit`](https://github.com/leonkoellerwirth-arch/agentic-ai-governance-toolkit) | 1 | 🟢 `MIT` · `1,080 B` | `a210993c213f` | Lifecycle governance artefacts **for agents** in regulated organisations — the governance side of the agents this shelf lists. |

🔵 **Neither is education-specific, neither has traction, and neither is proposed to a client as-is.**
They are recorded because `P31` (new in [`compose/patterns.md`](../compose/patterns.md)) names them
as starting scaffolds, and because the MCP-exposed-corpus shape is worth watching.

### 🔴 The trap row — and why "★ + metadata licence" is not a shelf cell

The highest-starred repository in that population is
[`Peaky8linders/specter-oss`](https://github.com/Peaky8linders/specter-oss) (9★). GitHub metadata
reports **`NOASSERTION`**. Its `LICENSE` is `2,260 B` — about double a stock MIT text — and byte-read
it is MIT **plus** a vendored-content section: the **OWASP APTS v0.1.0** catalogue shipped under
**`CC BY-SA 4.0`**, and an Article 15 control structure attributed to the **LatticeFlow ATLAS**
framework. 🔴 **A cell reading `specter-oss · 9★ · MIT` would have been wrong in the one direction
that costs a client money** — redistribution owes share-alike on the shipped catalogue. This is a
**third arity shape** (arity by vendoring, where reciprocity attaches to a data directory and not to
the code) and `T29`–`T31` do not cover it; `T34`–`T36` in [`intel/trends.md`](../intel/trends.md)
now do.

### 🟢 Declared gaps — searched this pass and not found

- 🔴 **No education-native conformance agent exists.** `46` repositories probed, `44` READMEs
  byte-read, **`0`** built for an education deployer — while education *is* the Annex III sector
  that owes Article 27 FRIAs. `23` of `44` contain an education keyword and **all `23` are
  false presences** (Annex III enumerations, "educational purposes only" disclaimers, an author's
  university email). Measured in [`trending.md`](trending.md#-2026-11-18-p889).
- 🔴 **No agent in the APAC or LATAM regulatory shape.** The population is entirely EU/UK-scoped.
  `0` rows address Vietnam's AI Law (in force `2026-03-01`, automated assessment named high-risk),
  Korea's AI Basic Act (`2026-01-22`) or India's content-labelling rules (`2026-02-20`).
- 🟡 **`5` of the `46` have no grant file** at `LICENSE`/`LICENSE.md`/`LICENSE.txt`/`COPYING` on
  either `main` or `master` — and **three of those five are the FRIA-specific ones**, so the
  obligation education deployers actually owe has the worst-granted tooling in the population.
- 🟢 **The eight prescribed legs ran and nilled for a TENTH pass on supply.** `90` previously
  unshelved education repositories were found via five new query shapes (including
  `教育 AI エージェント` and `agente educativo IA código abierto`); star ceiling among the
  education-native ones is `13`; **`0` earned a row.** The `18`-strong LMS-MCP bridge population was
  re-measured and is **entirely already held**.
