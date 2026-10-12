---
industry: education
region: Global
updated: 2026-10-12
---

# `p149-common-title-licence` — `ACTION FC` refuted, and a grant ladder that two instruments order differently

> 🟡 **`ACTION FC`** — add the **common-title forms** (`Apache License 2.0`, `MIT License`,
> `GPLv2`, `GPL v3`, `BSD 3-Clause`) that name a licence without the token the current
> patterns require. Re-run over all **57** subjects.
> 🔴 *Refuted if no row changes class* — which would make `T72` a Fedena-specific artefact
> outside this shelf's population, and the census complete at 8 of 57 strict-unlicensed.

    python3 common_title.py <clone-root>...
    python3 test_common_title.py       # 27 tests, authored fixtures, offline

## 🔴 Refuted — 0 of 58 rows change class

🟢 **The extension works** — `title_licence` reads all eighteen title forms, and **27 tests**
pin them, including the two orderings that matter (*Affero* must not read as GPL, *Lesser*
must not read as GPL, and a row's own heading must beat a dependency notice further down).
🔴 **It changes nothing on this shelf.** Exactly **one** row is `UNIDENTIFIED` under both
rules, and it is not a title-form case:

| row | grant | why it stays unidentified |
|---|---|---|
| `eugeborzone/Auto_Grade_Guarani` | `README_ONLY` | 🔵 a Spanish licence **heading** with **no licence named under it** — `p147`'s language rule found the heading, and there is no title to read |

🟢 **So `T72` is confirmed as a Fedena-specific artefact**, outside this shelf's population,
exactly as the consequence clause said a refutation would mean. 🟢 **Strict-unlicensed
reproduces at 8**, and the eight are named: `MatheusMach/QuantoFalta`,
`P1ckle3/blackboard-mcp`, `Piyushtanwani/DAU-buddy`, `SIU-Toba/docker-guarani`,
`karkarkins/BlackboardAssistantMCP`, `ruud0/aula-virtual-mcp`,
`hesham0-0nasser/tutor-lms-mcp`, `@n35da/brightspace-mcp@0.4.0`.

🔵 **The matcher is kept anyway.** It costs nothing, it is tested, and the next shelf this KB
censuses will not be this one — 🟢 **a refuted extension that is cheap to carry is not the
same as a wrong one.**

## 🔴 The denominator is 58, not 57

🟢 **44 connectors + 8 npm + 6 agent-tier = 58**, all reached: 🟢 **`git clone` 50 of 50**,
🟢 **`npm pack` 8 of 8**. p148 quoted **57** for the same three tiers. 🔵 **The strict-unlicensed
figure is unaffected** — it is **8** either way, because every agent-tier row but
`hesham0-0nasser/tutor-lms-mcp` carries a `FILE` grant (`AGPL-3.0`, `MIT`, `MIT`,
`Apache-2.0`, `MIT`). 🔴 **Recorded as a one-row discrepancy to reconcile, not as an error
in p148**: the agent tier has no committed subject list, so the two counts cannot be
compared directly, and 🟢 **this module's population is the one its own TSV enumerates.**

## 🆕 🔴 `T74` — p145 and p147 order the grant ladder differently, and nobody could have noticed

🔴 **The pass's real licence finding, and it came out of a reproduction control.**

| module | ladder |
|---|---|
| `p145-licence-census` | `FILE` → 🟢 **`PKG_ONLY`** → `README_ONLY` → `NONE` |
| `p147-licence-language` | `FILE` → 🔴 **`README_ONLY`** → `PKG_ONLY` → `NONE` |

🔵 **p145's own docstring states the intended order** — *"`README_ONLY` the only mention is
prose in a README. **Weaker still**"* — weaker, that is, than a licence declared in a package
manifest. 🔴 **p147 silently inverted the two rungs.**

🟢 **And it was invisible on the population p147 ran**: over the 44 connectors the two
modules agree row for row, because 🔵 **no connector carries both a manifest licence field
and a README licence heading.** p147's base tally on the 44 (`FILE` 34, `NONE` 8, `PKG_ONLY`
1, `README_ONLY` 1) reproduces p145's on the same 44 exactly. 🔴 **p147 never ran on the npm
tier**, which is where rows carry both — and there it moves **3 of 8**:

| row | p145 | this run under p147's ladder | licence |
|---|---|---|---|
| `@owen-x-tech/canvas-mcp@1.1.0` | `PKG_ONLY` | 🔴 `README_ONLY` | **MIT** either way |
| `eth-moodle-mcp@1.3.3` | `PKG_ONLY` | 🔴 `README_ONLY` | **MIT** either way |
| `moodle-mcp-server-aql@0.1.7` | `PKG_ONLY` | 🔴 `README_ONLY` | **AGPL-3.0** either way |

🟢 **No licence identification changes** — all three READMEs carry a plain `## License`
heading over the same licence the manifest declares. 🔴 **What changes is the evidence class**,
and it changes in the **weakening** direction: a declared manifest field is demoted to a
prose mention. 🔵 **p145's order is the defensible one**, and this is a correction to make in
`p147-licence-language`, not here — 🔴 **deliberately not made this pass**, because changing
the ladder in the same pass that measures it would mean comparing a modified instrument
against published figures, which is the mistake `P145`/`ACTION EU` was built to avoid.
🟢 **`ACTION FE` is registered for it.**

## 🔴 The harness defect this module produced, and the control that caught it

🔴 **Its first run reported 7 of the 8 npm rows as `NONE/-`** against p145's published
`PKG_ONLY/MIT`. 🔵 **`npm pack` extracts into a single `package/` directory**, so pointing the
census at the extraction directory reads an empty root. 🟢 **`payload_root` now descends into
it**, pinned by four tests, and the npm rows reproduce. 🔵 **Recorded because the direction
matters**: the defect **understated** the shelf's licence coverage, which on this shelf reads
as a worse finding than the truth — 🟢 **and it was caught before publication by comparing
against a published figure**, not in review. 🟢 **`p147-npm-region`'s published `where` values
(`package/README.md`) had been saying the same thing for two passes.**

## Files

| file | what it is |
|---|---|
| `common_title.py` | the module; eighteen title forms, ordered |
| `test_common_title.py` | **27 tests**, authored fixtures, offline |
| `result.58.2026-10-12-p149.tsv` | all 58 subjects, base and extended side by side |
