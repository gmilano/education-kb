---
industry: education
region: Global
updated: 2026-10-11
---

# `p135-licence-sha-identity` — `ACTION BP` discharged, and its premise refuted

**Pass 135, 2026-10-11.** `ACTION BP` asked for substring licence detection to be replaced with
"**sha256 matching against canonical licence texts**, normalising trailing whitespace and the FSF's
`http`→`https` update", and predicted it would be refuted *"if fewer than 2 corpus payloads are
whitespace-variant copies — but three are already known."*

🔴 **ZERO of the 26 payloads measured are whitespace variants.** The premise is wrong, and the reason
is worth more than the instrument: **a licence payload differs from its canonical text by LINE WRAP
WIDTH, not by whitespace.** SPDX wraps at ~105 columns; a real `LICENSE` file wraps at ~72. Same
words, different hard breaks, so a raw sha256 — and a whitespace-normalised one — never match.

## What it measures

Five progressively normalised forms, reporting **which one matched**, so the strength of every
identification is visible rather than assumed:

| level | normalisation | verdict when it matches |
|---|---|---|
| `raw` | none | `EXACT` |
| `ws` | CRLF→LF, per-line trailing whitespace, trailing blank lines, FSF URL updates, typographic punctuation | `WHITESPACE_VARIANT` |
| `flow` | + each paragraph reflowed to one line | `REFLOWED` |
| `body` | + copyright notices removed as spans | `TEMPLATE_MATCH` |
| `collapsed` | + all paragraph breaks collapsed | `WHITESPACE_COLLAPSED` |

`MODIFIED_SUPERSET` means the whole canonical body is present **plus** extra clauses — the `P134-F`
class (*"MIT + a visible-attribution clause"*). `UNMATCHED` rows carry a `nearest` column
(`SPDX:ratio`) so that an unresolved row reads as *"probably a steward edit not yet in the table"*
rather than as *"unusual licence"* — the bias `P134-F` warned about.

## Result on this corpus — 21 of 26 resolved by hash

```
TEMPLATE_MATCH 14 · WHITESPACE_COLLAPSED 4 · REFLOWED 2 · WHITESPACE_VARIANT 1 · UNMATCHED 5
```

The five classes of difference that actually defeat hash identity, in order of how often they bit:

1. **Line wrap width** — every payload. The whole reason a naive sha256 lane reports nothing.
2. **Typographic punctuation** — SPDX's canonical GPL-3.0 uses curly quotes `“ ”`; the `COPYING`
   file shipped in real repositories uses ASCII `"`. Five payloads differed by that alone.
3. **Steward-side edits to the licence's own text** — two are now known for GNU: the `http`→`https`
   change `ACTION BP` anticipated, and 🔴 **a second this pass found: the FSF moved
   `why-not-lgpl.html` from `/licenses/` to `/philosophy/`.** After wrapping and punctuation were
   normalised, that one URL path was the entire remaining difference on five GPL-3.0 payloads.
4. **Appendix instantiation** — `Citolab/qti-convert` fills GNU's "How to Apply" appendix with its
   real program name and holder, which is correct practice and makes the text non-canonical.
   🟢 **It also discloses the holder: `Stichting Cito Instituut voor Toetsontwikkeling, Arnhem`.**
5. **Undated notices** — `dhodges47/SCORM-LearningManagementSystem` carries
   `Copyright (c) David Hodges dba Outermost Software, LLC` with no year at all.

The 5 `UNMATCHED` rows, each with a named cause — 🟢 **two of them are correctly unmatched:**

| repo | nearest | why it does not match |
|---|---|---|
| `OpenOLAT/OpenOLAT` | Apache-2.0 `0.916` | 🔴 **Genuinely modified.** Apache-2.0 core terms verbatim, with `END OF TERMS` and the appendix **replaced by two attribution statements** — for the original olat.org base (OLAT Zentrum, University of Zurich) and for openolat.org (frentix GmbH). Permissive in effect; the notices must be preserved. |
| `cybercussion/SCOBot` | `0.068` | 🔴 **Not a licence text at all.** 837 B of the **CC-BY-SA-4.0 human-readable deed** ("You are free to: Share — … Adapt — …"), not the legal code. A ShareAlike content licence, applied to code. |
| `Citolab/qti-convert` | GPL-3.0 `0.998` | GPL-3.0 with the appendix instantiated (class 4 above). |
| `adaptlearning/adapt_framework` | GPL-3.0 `0.998` | GPL-3.0; residual difference inside the instantiated appendix. |
| `CoopCodeCommun/pyopenbadges` | LGPL-2.1 `0.996` | LGPL-2.1 with a reordered header sentence. 🔴 Copyleft — read before building. |

## 🔴 Two bugs its own tests caught, and the rule they produced

Line-based copyright stripping is **wrap-dependent in both possible orders**, and each order
silently deleted real licence text rather than failing loudly:

- **Strip after reflow** → the GNU header puts the notice and *"Everyone is permitted to copy and
  distribute verbatim copies…"* in ONE paragraph; reflowing first makes that paragraph a single line
  beginning with `Copyright`, so the strip removed the licence sentence with it. Six GPL-3.0
  payloads read `UNMATCHED`.
- **Strip before reflow** → Apache-2.0 contains *"…must include a readable copyright notice that is
  included in or attached to the work"*. At 72 columns the line break lands before `copyright`, so a
  line-based strip deleted that clause. `Cvmcosta/ltijs` and
  `1EdTech/digital-credentials-public-validator` regressed from a clean match to `UNMATCHED`.

🟢 **The rule:** remove a copyright notice as a **span inside an already-reflowed paragraph**,
anchored at the paragraph start and required to carry a year or an SPDX placeholder — or, if the
paragraph *is* nothing but a notice, without a year. The bare word "copyright" mid-sentence is
licence text, not a notice.

## Cross-owner payload identity — a stronger mirror detector than shared timestamps

Grouping by `body` hash across distinct owners is reported separately. On this corpus it finds the
expected benign groups (12 owners sharing the MIT body; 4 sharing Apache-2.0) — 🔵 **a shared
licence body is NOT evidence of mirroring**, which is why the grouping is a lead and never a verdict.

The decisive test is a **non-licence payload**: `api_enem_microdados` exists under four distinct
owners with **byte-identical `README.md` (sha256 `fea59dc854f35eac9cb72f14`, 1 842 B)**, identical
descriptions, and `fork: false` on all four. See `agents/trending.md` → Pass 135.

## Declared limitations

- 🔴 **The steward-edit table grows every time a licence steward edits its own text.** Two such
  edits are known for GNU. A payload predating a third will read `UNMATCHED` with a `~0.999`
  nearest score, which should be read as a table gap, not as a modified licence.
- A copyright notice **wrapped across lines inside a larger paragraph** leaves a continuation
  fragment, reported as `MODIFIED_SUPERSET`. Over-reporting an unusual licence is the safe direction.
- `collapsed` hides paragraph structure. Word order must still match exactly, so two different
  licences cannot collide there, but its verdict is reported separately rather than as a clean match.
- 4 of 30 targets have **no licence file at all** under 8 probed filenames: `educredentials/ec-issuer`,
  `pipwerks/scorm-api-wrapper` (391★), `adlnet/SCORM-to-xAPI-Wrapper` (archived), `lsloan/udp-notebooks`.
  Measured absent, not assumed permissive.

## Run it

```sh
./fetch_licences.sh targets.tsv /tmp/licences          # payload lane, 8 filenames per repo
python3 -I test_licence_sha.py                         # 33 tests, no pytest required
python3 -I licence_sha.py <canonical_dir> /tmp/licences
```

Canonical texts come from `spdx/license-list-data` (`text/<SPDX-ID>.txt`) plus
`github/choosealicense.com` for LGPL-3.0's short form, whose YAML frontmatter is stripped on load.
🔵 **This environment has no `pytest`**, so the suite ships its own runner and needs only a bare
interpreter.
