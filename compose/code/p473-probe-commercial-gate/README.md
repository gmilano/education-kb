---
industry: education
region: Global
updated: 2026-10-07
---

# P473 — a discovery probe is a shelf instrument (pass 36, 2026-10-07)

## What happened

Pass 36 swept candidate repositories with a **fresh, throwaway probe**, because sweeping is what a
discovery pass does. It reported
[`CRSS-AI/agentic-se-course-early-2026`](https://github.com/CRSS-AI/agentic-se-course-early-2026) as
**`GRANTED … UNKNOWN`** on an 822-byte `main/LICENSE`.

The payload is **Creative Commons Attribution-NonCommercial 4.0**:

> *"NonCommercial — You may not use the material for commercial purposes."*

| Classifier | Family | Commercial use |
|---|---|---|
| The throwaway probe | `UNKNOWN` | **not asked** |
| `../lib/license_family.sh` (shared, hardened) | **`CC-BY-NC-4.0`** | **`PROHIBIDO`** |

## Why the existing controls did not stop it

They were in the tree and they were correct. They were not **in the path**.

- **`P237`** — do not rewrite the licence classifier; source the shared one. Hardened on the *shelf*
  instruments (`p114`, `p170`, `p206`, `p211`, `p230`).
- **`P250`** — *family* and *commercial use* are two questions in two columns, because `UNKNOWN` is
  indistinguishable from "commercial use is PROHIBITED", and those are **opposite answers to the only
  question this KB exists to answer**. Also hardened on the shelf instruments.

Neither said anything about the **throwaway script that feeds the shelf**, so a new sweep sat outside
both. 🔵 **A control that is not in the path of new code is documentation, not a control** — the same
shape as `P471`, where a gate passing 27/27 judged nothing at all.

## The rule

> **`P473`.** A discovery probe **is** a shelf instrument. It must emit `P250`'s **commercial-use
> column** from the shared classifier, or its `GRANTED` rows are **not shelf-ready** and must not be
> written up as findings. *"Has a `LICENSE` file"* is a statement about a **filename**, not about a
> **grant**.

**Run this instead of writing a new sweep.** That is the entire point of the file.

## Why education raises the prior

This KB shelves **curricula, lesson plans, item banks and courseware**, not only code — and the **OER
tier is where `CC BY-NC` actually lives**. A Creative Commons NC licence sits at `LICENSE`, at an
ordinary size, in the ordinary place, and is **invisible to a filename-based probe**. For code, "has a
permissive-looking licence file" is nearly always a permissive grant; **for content it often is not.**

## `P475` is folded in

The **existence** check decides whether a repo is **real**, so it gets the same case-variation the
licence check gets. The original probe tried **16 licence filenames × 2 branches** but only **3 README
spellings**, and [`dikshant182004/MathTutor`](https://github.com/dikshant182004/MathTutor)'s README is
**`master/Readme.md`**. Had its licence not resolved first, a real repository would have earned
**`NO-PAYLOAD`** — the same verdict as the fabricated negative control.

## Usage

```bash
./discover_probe.sh owner/repo [owner/repo ...]   # TSV: slug, status, family, commercial, hit_path, bytes
./discover_probe.sh --self-test                   # 9/9
```

`status` ∈ `LICENSED` · `UNGRANTED` (real, no licence payload) · `NO-PAYLOAD` (nothing resolved —
treat as "may not exist"). `commercial` ∈ `OK` · `PROHIBIDO` · `SIN-DETERMINAR`.

## Self-test — 9/9

Fixtures are **real payloads** fetched 2026-10-07, not synthesised:

| Fixture | Bytes | Expected |
|---|---|---|
| `cc-by-nc-4.0-crss-ai.LICENSE` | 822 | `CC-BY-NC-4.0` / **`PROHIBIDO`** — the regression that defines this instrument |
| `mit-bandup.LICENSE` | 1,071 | `MIT` / `OK` — the inverse: a real grant must not be suppressed |
| `ecl-2.0-sakai.LICENSE` | 11,120 | `ECL-2.0` / `OK` — **not `Apache-2.0`** (`P476`) |
| `apache-2.0-osss.LICENSE` | 11,363 | `Apache-2.0` / `OK` |

Plus three assertions that `README.md`, `readme.md` and `Readme.md` are all in the existence list
(`P475`).

## Live run, 2026-10-07 — `result.2026-10-07.tsv`

| slug | status | family | commercial | hit_path |
|---|---|---|---|---|
| `dikshant182004/MathTutor` | LICENSED | MIT | OK | `master/LICENSE` |
| `CRSS-AI/agentic-se-course-early-2026` | LICENSED | **CC-BY-NC-4.0** | 🔴 **PROHIBIDO** | `main/LICENSE` |
| `sakaiproject/sakai` | LICENSED | **ECL-2.0** | OK | `master/LICENSE` |
| `ZeydSaeed/SIS` | UNGRANTED | — | SIN-DETERMINAR | `main/package.json` |
| `totally-fake-org-zzz9/nope-repo-abc` | NO-PAYLOAD | — | SIN-DETERMINAR | — |

Three behaviours demonstrated in one run: the NC trap is caught, Sakai resolves to **ECL-2.0** rather
than Apache, and a real-but-ungranted repo stays distinguishable from the negative control.

## Known limits

- **Reachability is not licence absence.** `UNGRANTED` means *no payload at the probed names on the
  probed branches from this environment*. `github.com` and `api.github.com` are **403** here, so there
  is no API fallback — `P470` (`formalms/formalms`) remains unresolved for exactly this reason.
- **No star counts**, by the same block.
- **Default branch is assumed to be `main` or `master`.** A repo on `develop` or `trunk` reads as
  `NO-PAYLOAD`.
- **Monorepo and open-core carve-outs are not detected.** A repo-level permissive payload can coexist
  with a proprietary `ee/` subtree — the shelf already records that case (ClickHouse-held `ee/`
  directories), and it needs a path-aware read this probe does not do.
