---
industry: education
region: Global
updated: 2026-10-12
---

# `p139-source-header-grant` — `ACTION CH`: the falsifier was fired, and it did not go off

**Executes p138's pre-registered `ACTION CH`**, written against p138's own headline finding:

> A licence-header read showing the grants live in source files rather than licence files, which
> would make **7 of 21 an overstatement of the defect and an understatement of the obligation**.
> 🔴 `ACTION CH` was registered for exactly this and has not run.

p138 measured that 9 of 21 published education-LMS connector packages ship **no licence file**. A
licence file is not the only place a grant can live: a great deal of real-world code carries its
grant in a per-file header instead. If these 9 did that, p138's defect count was wrong — and wrong
in the more interesting direction, because a header-borne AGPL grant still obligates.

## Verdict: **DISCHARGED, NOT REFUTED — 0 of 9**

| measurement | value |
|---|---|
| packages probed | **21** *(p138's census, re-run in full)* |
| tarballs sha1-verified against the registry's own `shasum` | 🟢 **21 of 21**, 0 mismatches |
| packages shipping no licence file *(p138's finding, re-measured)* | 🔴 **9** — agrees with p138 exactly |
| 🔴 **of those 9, how many carry their OWN grant in a source header** | 🔴 **0** |
| of those 9, how many carry a **third party's** notice in bundled output | **1** |
| packages on the whole shelf that practise per-file notice at all | 🔴 **1 of 21 — 5%** |

🔴 **So p138's `7 of 21` stands, and `T17` survives its registered falsifier.** The grants are not
hiding in the source files. In 8 of the 9 payloads there is no copyright line, no SPDX tag and no
operative licence sentence anywhere in any shipped text file — not in a header, not below one.

## The one apparent exception, and why it is the opposite of a refutation

`@owen-x-tech/canvas-mcp` **1.1.0** reported a `COPYRIGHT` grant on the first run. Read in place,
the notice is this:

```
/**
 * @license React
 * react-jsx-runtime.production.js
 *
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
```

🔴 **It is Meta's, for React**, at byte **1197** of a **572 657-byte** minified
`dist/ui/mcp-app.html`, hoisted there by a bundler. The package's own 6 authored text files carry
nothing. 🔵 **And the notice points at a `LICENSE file in the root directory` that the package does
not ship** — so the only licence text in the payload is a third party's, and it is itself a
dangling reference.

🔵 **This is why the probe reports `VENDORED` as a class of its own rather than as a grant.** A
bundler hoists its dependencies' notices to the *top* of what it emits, which puts them inside any
header window. **Position cannot attribute a notice.** The matcher therefore treats a notice in
machine-minified output (any line over 2 000 bytes) as the bundle's, never the package's.

## The row that does practise per-file notice — and it is 1 of 21

🟢 **`brightspace-mcp-server` 3.13.10** carries a notice in **100 of its 118** shipped text files:

```
/**
 * Brightspace MCP Server
 * Copyright (c) 2026 Rohan Muppa. All rights reserved.
 * Licensed under MIT — see LICENSE file for details.
 */
```

🟢 **And it ships the `LICENSE` those headers point to**, so the reference resolves. 🔵 **It is the
only row on the shelf whose notice survives file-level extraction** — copy one file out of it and
the grant travels with the file. In the other 20, a single extracted file is unattributable.

## The defect this probe produced before it produced a finding

🔴 **The matcher's first version missed the MIT grant it was built to find.** Real licence headers
are line-wrapped inside comment blocks, so the operative sentence arrives as
`free of\n * charge` — and a contiguous-phrase match returns nothing. The test suite caught it on
the first run, before any number was published. Comment leaders and whitespace runs are now
collapsed before any pattern is applied.

🔵 **Stated because the direction matters.** That bug would have produced *this probe's own
headline for the wrong reason*: a clean "no header grants anywhere" that was really a broken
matcher. The 0-of-9 above is only worth anything because the instrument demonstrably finds the
thing when it is there — which is what the `brightspace-mcp-server` row proves at 100 files.

## What a grant is, and what it is not

A mention of a licence is not a grant. The matcher counts five classes, ordered by obligation:

| class | what it matches |
|---|---|
| `COPYRIGHT` | a copyright line naming a year or a holder — `Copyright (c) 2026 X` |
| `SPDX` | an `SPDX-License-Identifier:` tag |
| `GRANT_MIT` | the operative sentence — *"Permission is hereby granted, free of charge"* |
| `GRANT_APACHE` | *"Licensed under the Apache License"* |
| `GRANT_GPL` | *"This program is free software"* / *"GNU (Affero) General Public License"* |
| `VENDORED` | 🔵 any of the above, inside minified output — **a bundled dependency's, not this package's** |

**24 tests, all passing** (`python3 -I test_headers.py`), half of them near-misses that must NOT
count: a `"license": "MIT"` manifest field, a `licenseKey` variable, a URL to a licence, a
`license-checker` import, prose about licensing, the bare word *copyright* with no year or holder,
and a grant sitting 40 KB inside a build artefact.

## Cross-layer confirmation, in one pass

🔵 **Through this KB's established raw-file lane — no new channel is claimed here.**
`agents/top.md` already documents `raw.githubusercontent.com/<owner>/<repo>/<branch>/LICENSE` as
the working substitute for the blocked REST API, and p136's evidence file used it. p138's script
comment is narrower than it reads: it records `api.github.com` and `codeload` as unavailable (the
former still answers `400` here) and simply did not use raw. 🔵 **What is new is that the payload
layer and the repository layer were measured in the same pass**, so the two can be set against each
other. Two repository-layer figures this KB published from other passes were re-verified
byte-exact:

| file | bytes | first line |
|---|---|---|
| `csmediapro/moodle-mcp-server@main/LICENSE` | 🟢 **34 523** | `GNU AFFERO GENERAL PUBLIC LICENSE` |
| `kstateome/lti-launch@master/License.txt` | 🟢 **7 651** | `GNU LESSER GENERAL PUBLIC LICENSE` |

🔴 **So the AGPL row is now confirmed on both layers in the same pass.**
`moodle-mcp-server-aql` **0.1.7** declares **AGPL-3.0**, ships **141 paths** and **71 text files**,
and carries **no grant in any of them** — while its repository carries the canonical 34 523-byte
AGPL text. 🔵 **The grant exists. The distribution drops it.** That is the one row on this shelf
where the finding should change a delivery decision rather than a note in a report.

## Why the question is asked of the payload and not the repository

Unchanged from p138, and reinforced: a client installs the tarball. The repository is evidence
about intent; the payload is the thing that arrives, and the thing a redistribution obligation
attaches to. This pass adds the second half — **the payload is also where attribution fails
silently**, because a bundler will happily carry someone else's notice into a package that has
none of its own.

## Reproduce

```sh
python3 -I test_headers.py        # 24 tests
./scan_headers.sh moodle-mcp-server-aql @owen-x-tech/canvas-mcp brightspace-mcp-server
```

Committed result: [`result.2026-10-12.tsv`](result.2026-10-12.tsv) — 21 rows, the full census.

## What would overturn this

🔴 **A grant living somewhere this probe does not look.** It reads the first 4 096 bytes of files
with a text extension. A grant in a `.d.ts` sourcemap, in an extensionless script, in a `LICENSE`
spelled in a way p138's path matcher misses, or below the header window in authored source would
all read as absent here. 🔵 The window is deliberate — it is what separates a package's own header
from a bundled dependency's text — but it is the assumption most likely to be wrong.
