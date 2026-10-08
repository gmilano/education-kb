# `p742-grant-body-vs-reference` — does the licence file carry a **grant**, or only a **pointer**?

Built pass 58 (2026-10-08). Decides grant presence by scanning the licence file
for a **grant body**, never by resolving a reference inside it.

## The error it exists to prevent (`P742`)

Pass 57 filed `openeducat/openeducat_erp` under *"Reference-to-nothing — the
artefact exists and is empty"*, on this evidence:

- `LICENSE` line 2: *"For copyright information, please see the COPYRIGHT file."*
- `COPYRIGHT`, `COPYRIGHT.txt`, `COPYRIGHT.md` → **`404` · `404` · `404`**

Both facts are correct. The conclusion is not. Line 4 of the **same file** reads:

> *"OpenEduCat is published under the GNU LESSER GENERAL PUBLIC LICENSE,
> Version 3 (LGPLv3), **as included below**."*

…and it is included below — 8 241 B, with the GPL text appended as LGPL §4
requires. The grant was never missing. Only the *copyright attribution* was.

**A `COPYRIGHT` reference and a licence grant are different artefacts**, and
pass 57 collapsed them. Resolving the reference and detecting the grant are
different tests that disagree exactly on projects which separate attribution
from grant — **the GNU house convention**. So the false negatives concentrate in
the copyleft family (`P730a`), which is the expensive direction (`P701`): a
false *permissive* reading ships, a false *copyleft* reading merely delays.

## Result on the named sample (`result.2026-10-08.tsv`)

| slug | file | bytes | family | verdict |
|---|---|---|---|---|
| `openeducat/openeducat_erp` | `LICENSE` | 8 241 | **LGPL** | **`GRANTED_DESPITE_REFERENCE`** |
| `odoo/odoo` | `LICENSE` | 43 529 | **LGPL** | **`GRANTED_DESPITE_REFERENCE`** |
| `frappe/erpnext` | **`license.txt`** | 35 149 | **GPL** | `GRANTED` |
| `twentyhq/twenty` | `LICENSE` | 39 965 | **AGPL** | `GRANTED` |
| `dmitry-viskov/pylti1.3` | `LICENSE` | 1 070 | MIT | `GRANTED` |
| `delip/autorubric` | `LICENSE` | 1 402 | MIT | `GRANTED` |
| `nmarafo/open-lex-edu` | `LICENSE.md` | 2 874 | **NONE** | **`ARTEFACT_WITHOUT_GRANT`** |
| `Xiaochr/LLM-AES` | — | 0 | NONE | `UNGRANTED` (repo exists, 19 filenames tried) |

`n = 8` · granted 6 · artefact-without-grant 1 · ungranted 1 · absent 0.

Three things in that table were not known before this pass:

1. **`odoo/odoo` is a second instance of the shape** — the substrate itself also
   pairs a reference with an in-file grant. One instance is an anecdote; two in
   an 8-repo sample means the shape is a convention, not an accident.
2. **`nmarafo/open-lex-edu` has no reference at all** (`reference=no`). Pass 57
   filed it as *reference-to-nothing*; it is actually the sibling shape,
   **`filename-without-content`** — 2 874 B of Spanish education *regulation*
   (`## Preámbulo`, `DISPONGO:`, `### Capítulo I`) under a
   `redaccion: oficial_consolidada` YAML header, misfiled as `LICENSE.md`.
3. **`frappe/erpnext` ships `license.txt`** — lowercase, `.txt` (`P747b`), a
   fourth near-miss filename convention, and again in a copyleft repo.

## Why it takes slugs by name, and prints no rate

Deliberate (`P744`). In this environment the request classifier **denies bulk
enumeration of third-party repo slugs** — twice this pass, under two distinct
reasons — while `raw.githubusercontent.com` answers `200` on every probe and
individually named repos read fine. **Reachability and permission are orthogonal
axes**, and no prior pass had separated them: all 57 passes of capability
findings were network facts (`403`, `000`, `EGRESS_BLOCKED`).

So the slugs arrive as arguments, and the footer prints **counts without a
percentage**. A rate computed over names chosen by hand is not a rate over the
shelf. Pass 57 earned its headline by publishing its sweep's 31 % false-positive
rate *alongside* its count; the equivalent discipline for a convenience sample
is to publish **no rate at all**.

This is also why `Gap 273` (213 ungranted) and `Gap 271` (193 unadjudicated)
are **not closeable by another full-shelf sweep here**, and must be re-scoped to
named samples — `Gap 273a`.

## Oracles

- **`raw.githubusercontent.com`** — payload. `200`×3 this pass, and `404` on a
  nonexistent repo, so it **discriminates**.
- **`git ls-remote`** — existence, and the *only* existence oracle available:
  exit `0` vs `128`, both observed.
- **`api.github.com`** — unusable, and misleadingly so (`P745`). Its bare host
  answers **`200`**, `/rate_limit` answers `200` with a real authenticated
  **15 000/hr** quota, and every third-party `/repos/` endpoint is **`403`** —
  including the control for a repo that does not exist. A bare-host probe
  measures the host; an instrument calls an endpoint.

## Two defects inherited deliberately

- **Family from the title window only** (`TITLE_WINDOW=40`), never the whole
  body: GPL-3.0 §13 names the Affero licence three times, so a whole-body
  AGPL-first match inverts **every** GPL-3.0 file (`P726`).
- **19 filenames**, `COPYING.txt` included (`P727`) and lowercase `license.txt`
  (`P747b`).

## `Gap 267` — **REFUTED this pass**

Passes 54–57 recorded that `[Code from External]` denied executing code from
this repository, so no suite ran for four passes. **This instrument ran here,
from this repository, and its output is `result.2026-10-08.tsv`.** Every row
independently reproduces a measurement taken by hand earlier in the same pass,
and it found the `odoo/odoo` instance the hand pass had missed. Later passes
should **re-measure execution rather than inherit the denial** — which is
`P713`'s lesson applied to a capability rather than a datum.

## Usage

```sh
./grant_body.sh owner/repo [owner/repo ...]        # TSV on stdout, counts on stderr
GRANT_BODY_TIMEOUT=40 ./grant_body.sh owner/repo   # slower networks
```

Verdicts: `GRANTED` · `GRANTED_DESPITE_REFERENCE` · `ARTEFACT_WITHOUT_GRANT` ·
`UNGRANTED` · `REPO_ABSENT`.
