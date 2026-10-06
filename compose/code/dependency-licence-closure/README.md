---
industry: education
region: Global
updated: 2026-10-06
---

# `dependency-licence-closure` — the licence of what the shelf INSTALLS, not of what the shelf IS

**Pass 21 of 2026-10-06. Channel new to this KB: the declared-dependency channel.**

```sh
python3 test_dep_licence.py          # 48/48, no network
python3 resolve.py targets.tsv       # the sweep; writes TSV to stdout, verdicts to stderr
```

## The question twenty passes never asked

This KB verifies every shelf licence from the repository's own `LICENSE` payload,
and it is rigorous about it: `p170`, `p172`, `p191`, `p283`, `p342` and a dozen
more directories exist to make that reading reproducible. **All of them answer
"what is this project?".** None answers **"what does this project install?"**

Those are different questions, and the second one is the one a client contract
turns on. `pip install deeptutor` does not install Apache-2.0 and stop. It
installs Apache-2.0 **and everything Apache-2.0 declared as a requirement**, and
a redistribution claim built on the repository licence alone has not looked at
the second half.

🔴 **Grep over all eight KB files before this pass was written, outside `archive/`:**

| Probe | Occurrences |
|---|---|
| `transitive` | **0** |
| `dependency licence` · `dependency license` | **0** |
| `copyleft dependency` | **0** |
| `lockfile` · `poetry.lock` · `package-lock` | **0** |

Manifests had been read — but for the project's *own* licence declaration
(`p283-manifest-named-license`) and for which model provider it calls
(`p257-provider-binding`). The dependency list was in front of every one of those
passes and none of them asked what it was licensed under.

## What it measures

Depth 1 — **declared direct runtime dependencies only**, read from the manifest
at a pinned ref, each resolved against its own registry:

| Layer | Endpoint | Reachable here |
|---|---|---|
| manifest | `raw.githubusercontent.com/<slug>/<ref>/<path>` | 🟢 200 |
| Python dep licence | `pypi.org/pypi/<name>/json` | 🟢 200 |
| npm dep licence | `registry.npmjs.org/<name>` | 🟢 200 |
| ~~advisories~~ | `api.osv.dev` | 🔴 403 at the egress proxy |
| ~~download counts~~ | `pypistats.org`, `api.npmjs.org` | 🔴 403 |
| ~~repo metadata~~ | `api.github.com` | 🔴 403 |

⚠️ **The ref is verified, not assumed.** A control request for
`definitely-not-a-branch-zzz9` returns **404**, so the channel discriminates
between refs; `main` and `master` on `huggingface/smolagents` both return 200 and
serve **byte-identical** payloads (same SHA-256), which is two live refs in
agreement rather than a proxy ignoring the ref.

## Five classes, and why the order matters

`NONCOMMERCIAL` → `STRONG-COPYLEFT` → `WEAK-COPYLEFT` → `PERMISSIVE` → `UNKNOWN`.

⚠️ **"AGPL-3.0", "GPL-3.0" and "LGPL-2.1" all contain the substring `GPL`.** A
naive sweep reports every copyleft licence as strong, which would put LGPL and
MPL dependencies — ordinary, shippable, linkable — in the same bucket as the one
finding that actually costs money. The ordering is asserted in the test suite, not
left to reading order.

**`UNKNOWN` is a finding, not a default.** It means the published grant is
unreadable at the registry layer, and this sweep found **four distinct causes** of
it, plus a fifth in its own code:

| Cause | Live example |
|---|---|
| a dual grant naming neither half | `python-dateutil` publishes exactly `"Dual License"` |
| the whole licence TEXT pasted into the field | `semver` → `"Copyright (c) 2013, Konstantine Rybnikov..."` |
| an explicitly proprietary classifier | `azure-cognitiveservices-speech` → `Other/Proprietary License` |
| a declared name that the registry does not serve | `CAHLR/OATutor` → `@common/global-config` → **404** |
| 🔴 **this instrument's own first version** | `defusedxml` publishes `PSFL`; the classifier knew only `PSF` and reported a false `UNKNOWN` on a clean package. Fixed, and asserted |

## The field migration that makes a naive reader wrong

🔴 **PEP 639 moved the value.** Modern packages leave `info.license` **null** and
carry `info.license_expression` instead. `pypdf` is the live control: `license` is
`null`, `license_expression` is `BSD-3-Clause`. A reader that knows only the old
field classifies a clean BSD package as `UNKNOWN`. `pypi_licence()` reads
`license_expression` → `license` → `classifiers`, in that order, and **returns
which field it used** so a verdict can be traced to its source.

## The manifest you can fetch is not always the dependency surface

🔴 **Five of 17 targets parsed zero dependencies, and not one was a parser bug.**
Four distinct shapes, all worth recording because each one makes a filename-keyed
sweep return a confident wrong answer:

| Shape | Target | What a naive sweep concludes |
|---|---|---|
| **empty sink file** — `requirements.txt` exists, returns 200, declares nothing; real set is in `[dependency-groups] base`, resolved by `make staticdeps`, while `[project].dependencies` is literally `[]` | `LearningEquality/kolibri` | 🔴 "Kolibri has zero dependencies" |
| **workspace root** — root manifest carries only `devDependencies` + pnpm config; runtime deps live in `apps/*` | `Selleo/mentingo`, `zijinz456/OpenTutor` | 🔴 "no runtime dependencies" |
| **meta-package indirection** — one dep, `agent-framework-core[all]==1.20.0`; the closure is a level down | `microsoft/agent-framework` | ⚠️ "1 dependency" (true, and useless) |
| 🟢 **genuine zero** | `tomaszboloz/WCAG-Accessibility-Skills` | 🟢 **correct** — and it independently confirms this KB's own prose claim in `agents/top.md` that the project has *"no production dependencies"* |

🔵 **That last row is the positive control.** An instrument that reports zero for
everything is useless; this one reports zero where zero is the truth, and names a
structural reason everywhere else.

⚠️ **Kolibri is listed twice in `targets.tsv` on purpose** — once as
`requirements.txt` to record that the file is a 200 that declares nothing, once as
`pyproject.toml#base` where the runtime set actually lives.

## What this is NOT

⚠️ **Depth 1 is not the closure, and this directory does not claim to be a
licence-compliance verdict.**

- **Transitive dependencies are not measured.** A permissive direct dependency can
  pull copyleft of its own. `certifi` (MPL-2.0) is in nearly every Python
  deployment on earth and surfaced here only in `oppia/oppia`, which happens to
  declare it directly.
- **Linkage is not analysed.** Whether importing an AGPL library creates a
  derivative work of the importer is a legal question about how the code is used
  and distributed, not something a licence string answers.
- **`REVIEW-*` means "a lawyer should look here", not "this is a violation".**
  `BLOCKER` means a non-commercial grant, which no linkage argument rescues.

🔵 **The deliverable is a short, specific list of places to look, replacing an
unexamined assumption that the repository licence covered the question.**

## Pre-registered for a later pass, falsifiably

1. **Measure depth 2 on the two `REVIEW-STRONG` targets only.** Hypothesis: the
   copyleft count **rises**, because `certifi`'s MPL-2.0 is transitive almost
   everywhere. If depth 2 adds no new copyleft *class*, the direct layer was
   sufficient and this instrument can stay at depth 1.
2. **Resolve the six `UNKNOWN` rows at the repository layer**, where this KB
   already has a working licence channel. Prediction: `python-dateutil` resolves
   permissive (its repo carries a dual Apache-2.0 / BSD-3-Clause grant) and
   `azure-cognitiveservices-speech` stays proprietary. ⚠️ **Prediction recorded
   before the measurement so it can be scored.**
3. **Add the `apps/*` manifests** for the two workspace roots. Hypothesis: the
   runtime closure appears there and both come back measurable.
