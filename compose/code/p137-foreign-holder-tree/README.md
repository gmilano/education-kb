---
industry: education
region: Global
updated: 2026-10-11
---

# `p137-foreign-holder-tree` — `ACTION BY`: the licence FAMILY is usually right; the OWNERSHIP usually is not

**Executes p136's pre-registered `ACTION BY`**, written as:

> Enumerate the file trees of the 20 largest rows on `repos/foundations.md` and count those
> carrying a **foreign** licence header (a holder other than the repo's own).
> 🔴 *Refuted if under 5% carry one — in which case slug-level licence verdicts are good enough
> and `T15` is four unlucky examples rather than a trend.*

## Verdict: **DISCHARGED, NOT REFUTED — by a factor of ten**

| measurement | value |
|---|---|
| rows probed (the 20 largest on `repos/foundations.md`) | **20** |
| tree paths enumerated | **224 591** |
| licence-shaped paths **outside the root** | **316** |
| of those, payloads that really are grants | **242** |
| rows carrying ≥1 **foreign-holder** grant in the tree | 🔴 **10 — 50%** |
| refutation threshold | 5% |
| rows whose root licence file is the whole story (`ROOT_ONLY`) | 🟢 **8** |

🔵 **Read together with [`p444-root-vs-tree-family`](../p444-root-vs-tree-family/README.md), which
measured the other half of the same question and got the opposite-looking answer: the licence
FAMILY read from the root file is the tree's family 92% of the time.** Both are true, and together
they are the finding: *a root licence cell predicts what you may do; it does not predict whom you
owe.* Family agrees 92% of the time; ownership is incomplete in 50% of the largest rows.

## What the foreign holders actually are

| class | examples measured this pass |
|---|---|
| front-end vendoring | Fonticons (Font Awesome) in `moodle` and `OpenOLAT`; Twitter's Bootstrap and Tiny Technologies' editor in `OpenOLAT`; Michael Bostock's d3 and Ivan Sagalaev's highlight.js in `chamilo-lms`; Adobe's cmaps, the PDFium Authors, Google's Liberation data and Mozilla in `openedx-platform` |
| 🔴 **a permissive library inside a copyleft platform** | `instructure/canvas-lms` is AGPL-3.0 at the root and ships **`gems/lti-advantage/LICENSE.txt` — MIT, held by a named individual (Nathan Mills)**. The LTI Advantage implementation inside the dominant North-American LMS is the permissive part of it |
| 🆕 **agent-skills packs, vendored** | `classroomio/classroomio` (AGPL-3.0) carries **10** MIT `skills/*/LICENSE` files held by three outside individuals. A 2026-shaped obligation: the skills are the part a client redistributes |
| institutional notices | `sakaiproject/sakai` carries **The Trustees of Columbia University**, the Apache Software Foundation and AOL LLC; `kolibri` carries a Debian maintainer's packaging copyright |
| the licence steward's own text | the FSF appears as a holder **21 times** across the corpus — a vendored copy of the licence body, not a third-party grant. Counted, because a notice obligation attaches to it too |

## Why the instrument is split in three files

`probe.sh` collects paths; `foreign_holder.py` classifies; `run.py` joins them. The split exists
because the classification must be testable **offline**, and because of two defects this pass
produced and then fixed:

1. 🔴 **An empty path list counted as one path.** `printf '%s\n' "$empty" | grep -c ''` returns 1.
   The first run reported a non-root licence file for **seven** repositories that have none —
   seven wrong rows out of twenty, all wrong in the direction of a finding. `empty_in_empty_out`
   is the regression test.
2. 🔴 **`sakaiproject/sakai`'s `content-copyright` i18n bundles matched on the WORD "copyright"**
   and produced 7 false grants in translated strings. A licence-shaped path is only a grant if its
   payload carries a recognisable licence family or a copyright line with a year
   (`i18n_bundle_is_not_a_grant`).

🔵 **And a third defect, found in the same pass by a different probe:** a four-filename sweep over
16 candidate rows reported `kstateome/lti-launch` as having **no licence file**. Tree enumeration
found **`License.txt`** — LGPL-3.0, 7 651 B. The filename probe's absence verdict was wrong 1 time
in 2 this pass (2 absences claimed, 1 false). `casefold_is_the_point` is the regression test, and
it is `p288-agpl-casefold` biting this KB for the second time.

## Running it

```bash
./probe.sh trees.tsv owner/repo [owner/repo ...]     # blobless depth-1 clones, trees only
python3 -I run.py trees.tsv result.tsv               # fetches payloads, publishes verdicts
python3 -I test_foreign_holder.py                    # 12 tests, own runner (pytest absent)
```

Committed artefacts: `trees.2026-10-11-p137.tsv` (20 rows, 224 591 paths),
`result.2026-10-11-p137.tsv` (per-row verdicts and foreign-holder samples).

## Limits, stated

- 🔴 **Only licence-shaped FILES are read.** A third-party header inside a source file — the
  `pipwerks` case p136 corrected, where the grant lives in `SCORM_API_wrapper.js` lines 11–12 — is
  invisible to this instrument. So **50% is a floor, not an estimate.**
- 🔴 **`openeducat/openeducat_erp` shows 14 licence-shaped non-root paths and 0 grants**: the
  payloads carry neither a family anchor nor a dated copyright line. That is a measured
  *unreadable* class, not a measured absence.
- 🔴 **A container-composition repository defeats the whole method.**
  `Crosstalk-Solutions/project-nomad` is `ROOT_ONLY` with 664 paths, and it composes Kiwix,
  Kolibri and Ollama **as images**. Its third-party obligations are real and are not in its tree.
- 🟡 `HEAD` is whatever the default branch points at on the day of the probe; no ref is pinned.
