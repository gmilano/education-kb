# licence-gate-terms-p732 — canonicalise the terms, not the whole file

Runnable implementation of **`P172`** (MIT) and **`P173`** (Apache-2.0), added at `p732`
(2026-11-10). Supersedes the line rule of `P164`/`P168` for MIT and whole-file canonicalisation
for Apache-2.0.

## Constants

| Family | Canonical | Measured across |
|---|---|---|
| MIT | **`1020 B` / `fe2a9817987f`** | `18 / 18` payloads read at `p732` |
| Apache-2.0 | **`8484 B` / `c7396247b0c2`** | `5 / 5` payloads read at `p732` |

## Why the previous rules were replaced

**MIT (`T272`).** The prior rule dropped **every line containing the substring `copyright`**. In a
stock MIT payload that is **three** lines:

| Line | Content | A term? |
|---|---|---|
| 3 | `Copyright (c) 2026 <holder>` | No — attribution metadata. Correct to drop. |
| 12 | `The above copyright notice and this permission notice shall be included in all` | **Yes — MIT's only condition.** |
| 18 | `AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER` | **Yes — part of the disclaimer.** |

So the old `870 B` / `3d87852cf34a` constant was computed over a text **missing MIT's single
condition and part of its disclaimer**, and was holder-invariant *because* of that deletion. A
tamper confined to one of those dropped lines was therefore invisible: a payload reading
`need NOT be included` certified at the exact stock constant.

The repair keeps every term and drops the holder line by its **shape**
(`^copyright\s*(\(c\)|©)?\s*\d{4}…`) rather than by the word appearing anywhere.

**Apache-2.0 (`T274`).** The APPENDIX is headed *"How to apply the Apache License to your work"* and
is boilerplate instructions, which the licence text places outside the terms. Hashing it caused a
false refusal of a stock grant: `evalle/dca` canonicalises whole-file to **exactly the stock
`9,478 B` length with a different hash**, and the entire difference is `"[]"` → `"{}"` inside the
appendix instructions. Truncating at `^APPENDIX:` yields one constant that accepts stock payloads,
`{}`-variant appendices and appendix-free payloads alike — including `uw-it-aca/myuw`, which `p731`
filed as an anomaly requiring a named exception. It is not anomalous; it is byte-identical to stock
on the terms.

## The limit, which cannot be removed

Holder-invariance and holder-line-tamper-detection **cannot both come from one hash**: the rule
discards the holder line, so a restriction appended to it
(`… <holder>. NONCOMMERCIAL USE ONLY.`) is invisible to the digest. `mit_gate()` therefore pairs
the hash with a **separate shape assertion** on the holder line. That assertion is not optional —
without it one control passes that should not.

## Usage

```bash
# fetch to a FILE, never through $(curl ...)  -- T143
curl -s -o LICENSE.probe https://raw.githubusercontent.com/{owner}/{repo}/HEAD/LICENSE

python3 -I gate_terms.py mit    LICENSE.probe
python3 -I gate_terms.py apache LICENSE.probe
```

Exit status is `0` when every payload passes, `1` when any is flagged.

## Controls

```bash
python3 -I test_gate_terms.py
```

Eight network-free controls built from an in-file stock payload, asserting both directions:

| Control | Change | Expected |
|---|---|---|
| `stock` | none | PASS |
| `newholder` | holder name replaced | PASS (invariance) |
| `cjk_holder` | holder containing CJK | PASS (invariance) |
| `year_range` | `(c) 2026` → `(c) 2023-2026` | PASS (invariance) |
| `attr_negated` | `shall be included` → `need NOT be included` | **FLAG** |
| `liable_flipped` | `BE LIABLE FOR ANY CLAIM` → `ARE FULLY LIABLE FOR EVERY CLAIM` | **FLAG** |
| `attr_deleted` | attribution clause removed outright | **FLAG** |
| `noncommercial` | `NONCOMMERCIAL USE ONLY.` appended to the holder line | **FLAG** (via shape assertion) |

All eight behave as specified at `p732`, and the stock payload reproduces the published constant.
Re-run this suite before trusting the constants in a later pass — `p729` recorded a gate that
*could not be run at all*, which is the failure this entry exists to prevent.

## `result.2026-11-10.tsv`

Every payload read at `p732`, with its family, canonical bytes, `sha256₁₂` and verdict.
`18` MIT and `5` Apache-2.0 subjects pass.

⚠️ One row flags by design: `puneet-chandna/vit-pyqps-paaji` is **`CC0-1.0`**, not Apache-2.0, so
checking it against the Apache constant correctly refuses it. It is recorded rather than removed,
because a gate that silently drops payloads it does not recognise is the defect in a different
disguise. `CC0-1.0` is a public-domain dedication and not a permissive software licence; it says
nothing about the copyright in the collected exam papers themselves.

## Scope

These gates certify that a payload's **terms** match stock MIT or Apache-2.0. They do not establish
that the repository's licence *metadata* agrees (the search index disagrees with the payload
regularly — see `repos/foundations.md`), nor that a file at `HEAD` was the licence at the commit a
client would vendor. Pin a commit for anything that ships.
