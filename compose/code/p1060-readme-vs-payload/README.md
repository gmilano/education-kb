---
industry: education
region: Global
updated: 2026-10-25
---

# `p1060-readme-vs-payload` — pass 444 closing `Gap 443-C`: does the README name a DIFFERENT grant from the file?

`Gap 443-C`, declared by `p443`: *"This base has no instrument that compares the README's stated
grant against the payload's. `ipti/br.tag` was caught by hand… which is the direction that
costs money when the README is the permissive one."*

## What is here

| file | what it is |
|---|---|
| `readme_claim.py` | the **README side**, the only half that did not already exist. `claims_in(text, repo_slug)` → `Claim(family, tier, context, evidence)` |
| `compare.py` | the **join**. Reads a `p1059/probe.sh` TSV + the README at the same commit, emits one verdict per repository |
| `test_readme_claim.py` | **43/43, offline**, fixtures captured first-hand |
| `fixtures/` | the two real READMEs the suite is anchored on |
| `shelf/final/probe.tsv` | the 321-row, 999-grant-path sweep this instrument was first run over |
| `shelf/verdicts.tsv` | its verdicts |

🔵 **The payload side is `lib/license_family.sh`'s `family_of` and is NOT reimplemented here.**
`P237`/`P197`: a sweep written from scratch re-imports every defect already paid for.

## The one idea

**A licence NAME is not a licence CLAIM.** A README saying *"unlike the GPL-3.0 projects in this
space"* names GPL-3.0 and claims nothing; a dependency table naming twelve licences claims none
of them. So every match must sit in a **claim context** — `BADGE`, `PROSE` (*"licensed under
X"*), or `SECTION` (under a `## License` heading) — and that gate **is** the instrument. Without
it the channel is a licence-word grep, and `p288`'s README channel already showed a word grep
cannot carry a verdict.

## Verdicts

| verdict | meaning |
|---|---|
| `AGREE` | a claim matches a grant in the tree |
| `README-SILENT` | a README that makes no claim of its own |
| `NO-README` / `NO-PAYLOAD` | no README; or a claim with no grant file to check it against |
| `DUAL-GRANT-DECLARED` | two grants in the tree and the README scopes them — a **correct** README |
| `PAYLOAD-FAMILY-UNMAPPED` | the tier map is missing an entry. **Accuses the map, never the repository** |
| 🔴 `README-MORE-PERMISSIVE` | **the expensive one.** The README's claim is a more permissive tier than the payload |
| `README-MORE-RESTRICTIVE` / `DIVERGE-SAME-TIER` | the cheap directions |

## 🔴 Six defects this instrument found in ITSELF, in one pass

Recorded because each was caught by **verifying a finding before publishing it**, and a false
accusation against a real project is the expensive failure for this channel.

1. **Subject-blind claims.** `jeanhrm/siagie-analytics` ships an unmodified **Laravel skeleton
   README**; *"The Laravel framework is open-sourced software licensed under the MIT license"*
   was read as the repository's claim. → **subject gate**, context `FOREIGN:<subject>`.
2. **A second surface form of the same question.** `withmarbleapp/os-taxonomy`'s exemplary
   multi-licence table closes with *"Bundled Three.js and Baloo 2 retain their separate MIT and
   OFL licenses"* — the MIT is three.js's. → `bundled_claim()`, and **per-line** section
   scanning so a bundled note mutes only its own table row, not the correct ODbL claim beside it.
3. **A dot inside a project name.** `bundled_claim`'s first regex used `[^.\n]` to stay inside
   one sentence, and could not cross **"Three.js"**. → stay on one *line*.
4. **Unmapped = severe.** `TIER.get(fam, 9)` made any unmapped payload family maximally
   restrictive, manufacturing two findings. → `tier_of()` returns `None`, verdict says the map
   is incomplete.
5. **Root-anchoring.** One row per repository "anchored on the root grant" hid
   `LICENSES/MIT-upstream.txt` (so `pengusto/google-classroom-mcp`'s honest dual grant read as a
   lie) and let a **vendored** `MPL-1.1` outvote `openSIS-Classic`'s own `docs/License.txt`.
   → claims are matched against **every** grant in the tree (`p442`).
6. **An anchor that preferred a PNG.** `is_licence_path` grades `assets/notice.png` as a grant
   path — correctly, by its `notice.*` glob — and a depth-only rank preferred it over
   `docs/License.txt`. → unreadable payloads sort last. Plus: a bare family root (`GPL`) matches
   any version of that root, but **never** `AGPL`/`LGPL`.

🔵 **The shape all six share: a DEFAULT standing in for a measurement.** Tier 9 for unknown, the
root for the whole tree, the most-permissive claim for a scoped one, a string compare for a
family question. That is `p443`'s lesson about nil results one level down — *silence reads
exactly like coverage*, and so does a default.

## Result of the first run

321/321 sell rows, 999 grant paths, 0 shard failures → **1** genuine `README-MORE-PERMISSIVE`
(`ipti/br.tag`, already caught by hand at `p443`), 151 `AGREE`, 2 correct `DUAL-GRANT-DECLARED`.
🟢 **The shelves' licence cells are sound.**
