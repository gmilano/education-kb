---
industry: education
region: Global
updated: 2026-10-12
---

# p147-provisional-reverdict — `ACTION EI`, and the five rows are cleared

`P146-B` showed `p141-agent-surface-gate/surface_gate.py` can return
`NOT_AN_MCP_SERVER (0 'mcp' tokens, no SDK import)` from a walk of **zero files**, and p146
named five published rows carrying that verdict. 🔴 **It could not test any of them: every
`git clone` was refused in that session.**

🟢 **The channel is open in this one** (`T65`), so the question is answered with the payload.

    python3 reverdict.py <payload-root>...      # TSV; the two counts are the measurement
    python3 test_reverdict.py                   # 10 tests, authored fixtures, offline

## Result — 🟢 `ACTION EI` DISCHARGED, 0 of 5 are `T42` artefacts

| row | files walked (excl) | files walked (all) | verdict |
|---|---|---|---|
| `zijinz456/OpenTutor` | **726** | 726 | 🟢 reproduces, **CONFIRMED** |
| `BetterSEQTA/BetterSEQTA-Plus` | **488** | 488 | 🟢 reproduces, **CONFIRMED** |
| `BetterSEQTA/DesQTA` | **427** | 427 | 🟢 reproduces, **CONFIRMED** |
| `Agso-o/sigaa-calendar` | **10** | 10 | 🟢 reproduces, **CONFIRMED** |
| `juliancasaburi/siu-guarani-promedio-extension` | **6** | 6 | 🟢 reproduces, **CONFIRMED** |

🟢 **Every one had real input, and the published verdict reproduces to the token.** 🔵 **The
exclusion `P146-B` indicts never fired on any of them**: `git ls-files` matches **0** paths
under `dist/` or `build/` on all five. The provisional flag is lifted.

## 🆕 `ACTION EB` answered on the way — `T62`

The same rule run over all **16** non-npm census rows: **14 `SOURCE`, 2 `PAYLOAD`**. 🟢 **So
`ACTION EB` is NOT refuted** — the payload rule is not an npm-tier special case and `T42`
stays shelf-wide.

🔴 **But both `PAYLOAD` rows name a tree that is not in the artefact being measured.**
`divyarthjain/vtop-bhopal-mcp` (`main`, `bin`×2, `exports` → `dist/`) and `nitsuah/bb-mcp`
(`main`, `bin` → `dist/`) both **gitignore `dist/`** and commit **0** files there. 🔵 **The
mode is read from `package.json`, which travels with the source; the tree it names is a
build output.** On a clone, `PAYLOAD` is decided and unsatisfiable, and re-admitting the
tree adds zero files — so the mode column describes the package's intent, not the measured
artefact. 🆕 **`T62`.**

🔴 **13 of 16 declare no entry point in `package.json`**, so `SOURCE` is reached by default rather than
by the rule. 🔵 **The rule is undecidable on most of this shelf**, which no pass had said.

## 🔴 A limit of this probe, recorded because it nearly cost a finding

🔴 **`artefact_mode` reads `package.json` only.** So it reports *"no declared entry point"*
for every Python, Rust or PHP row on the shelf — including `krzysztofbury/librus-mcp`,
which declares `[project.scripts] librus-mcp = "librus_mcp.cli:main"` in `pyproject.toml`
and ships a 16-item `only-include` allowlist.

🔵 **That reading is why `ACTION EC` looked unrunnable and nearly went unreported.** It is
in fact runnable and 🟢 **discharged**: registration sites inside the manifest-declared
package sum to **exactly 35**, matching `MCP_CONTRACT.md`. 🔴 **23 further sites sit in
`legacy_reference` and 2 in `scripts`, both outside the allowlist** — naive inclusion reads
**60**.

🔴 **So of the 13 rows this probe reports as having no declared entry point, an unknown
number DO declare one in a manifest it does not read.** 🟢 **`ACTION EV` is registered to
generalise the manifest-allowlist rule across `pyproject.toml` and `package.json` alike**,
and until it runs, 🔴 **`T62`'s "13 of 16 declare no entry point" must be read as
"13 of 16 declare no entry point *in `package.json`*."**
