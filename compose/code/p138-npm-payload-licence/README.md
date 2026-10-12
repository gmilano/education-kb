---
industry: education
region: Global
updated: 2026-10-12
---

# `p138-npm-payload-licence` — `ACTION CD`: the SPDX-id-without-text defect is a third of the tier

**Executes p137's pre-registered `ACTION CD`**, written as:

> Read the **npm tarball** of `mcp-canvas-lms` (`registry.npmjs.org` answers **200** in this
> channel, newly). 🔴 *Refuted if the published package carries the `LICENSE` the repository
> lacks — in which case `P137-J` is repository hygiene, not a distribution defect.*

## Verdict: **DISCHARGED, NOT REFUTED — and generalised from one row to nine**

The registered question was about one package. The lane that answered it answers for the whole
tier at the same cost, so the probe was widened to every education-LMS connector published on
npm that a registry search finds (21 packages, 4 platform families).

| measurement | value |
|---|---|
| packages probed | **21** |
| tarballs downloaded and **sha1-verified against the registry's own `shasum`** | 🟢 **21 of 21** |
| identity mismatches | 🟢 **0** |
| 🔴 **carry an SPDX identifier and ship NO licence file** | 🔴 **7 — 33%** |
| 🔴 carry **neither** an identifier nor a licence file | 🔴 **2 — 10%** |
| 🟢 carry a licence file in the payload | 🟢 **12 — 57%** |
| `mcp-canvas-lms` specifically — the registered target | 🔴 **18 paths, no licence file**, manifest `"license": "MIT"` |

🔵 **So `P137-J` was not repository hygiene and it was not one repository.** The class — *an SPDX
identifier without the text it names* — is **a third of the published education-connector shelf**.
A client told to "ship the notice" has nothing to ship, in 7 of 21 cases.

## The nine rows that ship no licence text

| package | version | published | manifest says | paths | class |
|---|---|---|---|---|---|
| 🔴 `moodle-mcp-server-aql` | 0.1.7 | 2026-10-01 | **`AGPL-3.0`** | **141** | 🔴 **copyleft grant, no text — the worst case on the shelf** |
| 🔴 `mcp-canvas-lms` | 1.0.5 | 2025-04-11 | `MIT`, `files: ["dist"]` | 18 | id without text *(the registered target)* |
| 🔴 `canvas-mcp-server` | 2.2.3 | 2025-06-27 | `MIT`, **`files` LISTS `LICENSE`** | 8 | 🔴 **names the file it does not ship** |
| 🔴 `@owen-x-tech/canvas-mcp` | 1.1.0 | 2026-02-23 | `MIT` | 12 | id without text |
| 🔴 `@ink-waffle/moodle-mcp` | 0.2.0 | 2026-09-17 | `MIT` | 38 | id without text |
| 🔴 `eth-moodle-mcp` | 1.3.3 | 2026-04-15 | `MIT` | 15 | id without text |
| 🔴 `@exhabition/brightspace-mcp` | 0.2.2 | 2026-10-01 | `MIT` | 3 | id without text |
| 🔴 `@imazhar101/mcp-canvas-server` | 2.1.3 | 2026-10-01 | **absent** | 71 | 🔴 **no licence signal at all, and no `repository` field** |
| 🔴 `@n35da/brightspace-mcp` | 0.4.0 | 2026-09-22 | **absent** | 22 | 🔴 **no licence signal at all, and no `repository` field** |

🔴 **`moodle-mcp-server-aql` is the row that should change a delivery decision.** It declares
**AGPL-3.0** — the strongest obligation on this shelf — across **141 shipped paths**, and the
payload contains no licence text. Its GitHub repository
([`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server)) **does** carry
a canonical 34 523-byte AGPL-3.0 `LICENSE`. 🔵 **The grant exists; the distribution drops it.**

🔴 **`canvas-mcp-server` 2.2.3 shows the mechanism exactly.** Its packed manifest reads
`files: ["build/**/*", "README.md", "LICENSE", "package.json"]` — it *names* `LICENSE` — and the
tarball's 8 paths contain none. `files` names a path that does not exist in the tree and npm omits
it silently. 🔵 **A manifest that lists a licence is not evidence that one shipped.**

## Why this is measured at the payload layer and not the repository layer

This KB has read licence files at four layers (root file, tree enumeration, source headers,
registry metadata). 🔵 **The payload is the fifth, and it is the only one a client actually
receives.** `npm install` does not clone a repository: it unpacks a tarball. A grant that lives
only at HEAD is not conveyed to the person who installs the package.

🟢 **Direction of the error is worth recording.** Every one of the nine is a case of the repository
being *better* than the distribution — not one package shipped a licence its repository lacked.
So the defect is packaging discipline, not false claims about licensing.

## Method, and what would falsify it

1. `registry.npmjs.org/<pkg>` → `dist-tags.latest`, its publish time, its tarball URL and `shasum`.
2. Download the tarball; **sha1 the bytes and compare to the registry's `shasum`**. A mismatch is
   published as `SHASUM_MISMATCH` and the row is not counted — a measurement of the wrong bytes is
   worse than no measurement.
3. `tar tzf` every path; match against `(^|/)(licen[cs]e|copying|notice)([.-][a-z0-9]+)?$`,
   case-insensitively.
4. Extract `package/package.json` **from the tarball** — the manifest as packed, not as served by
   the registry's abbreviated metadata, which omits `files`.

🔴 **The probe reads licence FILES only.** A grant in a source-file header is invisible to it, and
p137's `pipwerks` correction proved that case is real. 🔵 **So 7 is a floor, not a count** — the
same caveat `p137-foreign-holder-tree` carries, for the same reason. `ACTION CH` was registered to
close exactly this hole at the repository layer and **did not run this pass**.

🔴 **Scope limit, stated:** 21 packages found by registry search over four platform families
(Canvas, Moodle, Brightspace, EduBase). This is not the whole npm education surface, and PyPI,
Maven and crates were not probed. `moodler-mcp` — a Python connector on this KB's shelf — **is not
on PyPI at all (404)**, so for part of the shelf there is no payload layer to measure.

## Files

| file | what it is |
|---|---|
| `scan_npm_payload.sh` | the probe; takes package names, emits one TSV row each |
| `result.2026-10-12.tsv` | the committed 21-row measurement this README reports |
| `test_payload.py` | 7 tests: the path matcher against real and near-miss filenames, and the committed TSV against its own headline counts |

```sh
./scan_npm_payload.sh mcp-canvas-lms canvas-mcp-server
python3 -I test_payload.py
```
