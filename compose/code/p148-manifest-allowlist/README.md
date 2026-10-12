---
industry: education
region: Global
updated: 2026-10-12
---

# p148-manifest-allowlist — `ACTION EV` refuted, and one manifest has two allowlists

`ACTION EC` (p147) found the `NOT_SHIPPED` rule already written in `librus-mcp`'s own
`pyproject.toml`, and `T39` was vindicated. `ACTION EV` asked whether that generalises.

> 🟡 **`ACTION EV`** — read the package manifest's include allowlist as the `NOT_SHIPPED`
> rule across all 16 surface subjects, replacing the name list entirely.
> 🔴 *Refuted if any subject has no manifest allowlist to read.*

    python3 manifest_allowlist.py <clone-dir> [subject ...]
    python3 test_manifest_allowlist.py    # 12 tests, authored fixtures, offline

## 🔴 Result — refuted by eleven of sixteen

| verdict | n of 16 | meaning |
|---|---|---|
| 🟢 `ALLOWLIST` | **5** | an allowlist exists and was read |
| 🔴 `MANIFEST_NO_ALLOWLIST` | **7** | a manifest exists and declares none |
| 🔴 `NO_MANIFEST` | **3** | no package manifest of any kind |
| 🔴 **`NO_ALLOWLIST_CONCEPT`** | **1** | 🔴 **the format CANNOT express one** |

🔵 **`NO_ALLOWLIST_CONCEPT` is what makes this structural.** `Agso-o/sigaa-calendar` is Go,
and `go.mod` has no include key — the module is the unit. 🔴 **No author diligence would give
it one.** 🟢 **That is `T39` applied to itself: a property-based exclusion is sound only where
the property exists.** So the name list stays as a fallback, exactly as the action's
consequence clause specified.

## 🆕 🔴 `T68` — `librus-mcp` declares TWO allowlists, and they disagree

🔴 **The sharper finding, and it corrects p147's prose.**

| target | key | items | 🔴 `.tool(` sites inside it |
|---|---|---|---|
| **wheel** | `packages` | **1** — `src/librus_mcp` | 🟢 **35** |
| **sdist** | `only-include` | **16** — incl. `tests_native`, `scripts/qualify_native.py` | 🔴 **39** |

🔴 **p147 named the 16-item `only-include` as the rule and published 35, the wheel figure.**
🟢 **35 is correct** — it is what the installable package contains and it matches
`MCP_CONTRACT.md` to the token. 🔴 **The rule cited for it yields 39**, because the sdist
allowlist admits `scripts/qualify_native.py` (2 sites) and `tests_native` (2 sites).

🔵 **So "read the manifest's include allowlist" is underdetermined: a pass must say WHICH
TARGET.** 🟢 **For a tool surface the wheel is right**, because that is the artefact a
consumer installs.

🟢 **p147's other librus figures reproduce exactly.** Whole tree **60** = **35**
(`src/librus_mcp`) + **21** (`legacy_reference`) + **2** (`scripts`) + **2**
(`tests_native`). 🔵 p147 reported *"23 in `legacy_reference` + 2 in `scripts`"*, folding
`tests_native`'s two into `legacy_reference`; the total is identical and **no published
figure changes**.

## The five rows that DO have an allowlist

| row | items | source |
|---|---|---|
| `krzysztofbury/librus-mcp` | **1** | `[tool.hatch.build.targets.wheel] packages` |
| `malkreide/global-education-mcp` | **1** | same key |
| `yourssu/soongpt-plugin` | **1** | same key |
| `divyarthjain/vtop-bhopal-mcp` | **4** | `package.json files` |
| `nirholas/ai-tutor-mcp` | **4** | `package.json files` |

## The 12 tests

Eight pin one manifest shape each (hatchling `only-include` and `packages`, setuptools,
poetry's array-of-inline-tables, npm `files`, Cargo `include`, `MANIFEST.in`, multi-line TOML
arrays). Four pin the distinctions that matter: an **empty** `files` array is not an
allowlist; a manifest with no allowlist key is **not** the same as no manifest; `go.mod` is
`NO_ALLOWLIST_CONCEPT`; and 🔴 **two targets in one file are both readable** — with a stated
limit that `measure()` reports the first it finds.

    12/12 passed
