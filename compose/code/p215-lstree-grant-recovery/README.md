# `p215` — recovering a grant from the whole tree, without downloading the tree

Discharges **`ACTION QD`** *(registered by p214, which re-scoped p211's `ACTION QA` after finding
that `QA`'s prescribed method would publish `foradian/fedena` as `MIT` from a vendored file)* and
**`ACTION QG`** *(make the correction, not the discovery, the unit of work)*.

## The channel

`p211` recorded `94` shelf repositories as `ABSENT`: serving no licence blob at `HEAD` after `18`
path forms. Every one of those forms was a **root** path. The question `QD` asks is whether
`ABSENT` has been a root-only artefact all along.

```bash
git clone --filter=blob:none --no-checkout --depth 1 https://github.com/<slug> <dir>
git -C <dir> ls-tree -r HEAD --name-only
```

A **treeless** clone transfers commit and tree objects only — **no file contents**. The result is
the repository's complete path inventory for a few KB, after which the candidate blobs are read
individually over `raw.githubusercontent.com`. `p214` measured `4 568` and `5 321` paths this way
in seconds; this pass ran it over `94` repositories.

## Scripts

| file | does |
|---|---|
| `qd_sweep.sh` | treeless-clones each slug, `ls-tree`s it, and bins every licence- or manifest-shaped path into **own** / **ambiguous** / **vendored** |
| `read_grants.py` | fetches the candidate blobs and classifies each from the **title window**, not the body |
| `remeasure.sh` | re-measures every recovered blob **binary-safe** and records its line endings |
| `qg_gate2.py` | the `ACTION QG` gate: for every repo whose grant changed, re-reads **every** current-state cell that mentions it |

## Four rules the instrument encodes, each from a defect that shipped

1. **Classify from the title window.** `P214-1`: `GPL-3.0` §13 is *titled* "Use with the GNU Affero
   General Public License" and the body says `Affero` three times, so a whole-body matcher reads
   `GPL-3.0` as `AGPL-3.0`.
2. **A path is not a grant.** Three ways it is not — see
   [`evidence/lstree-traps-and-nongrants.2026-10-15-p215.tsv`](../../../evidence/lstree-traps-and-nongrants.2026-10-15-p215.tsv):
   every match vendored (`alfredang/ai-mms`, `5` paths, `0` its own); the filename a **domain
   noun** (`mn-mde-edfi`'s `LicenseTypeDescriptorsApi.cs` is about *teacher certification*); or
   licence text shipped **as data** (`spdx/license-list-data`).
3. **Measure bytes binary-safe.** A text-mode pipe strips `CR`, so a `CRLF` blob reads one byte
   short **per line**. `formalms/formalms`' `html/license.txt` is `18 346` B with `340` `CR`s; read
   through a text pipe it measures `18 006`. Use `curl -o file` then `wc -c`, per `T208-8`.
4. **Propagate in the same pass.** `qg_gate2.py` is rule `4`: it exists so a correction cannot be
   published to one cell and left out of the other six.

## The vendored-path filter is NOT a one-liner, and `QD` got it wrong in both directions

`QD` prescribed rejecting `vendor/`, `lib/`, `node_modules/`, `third_party/`,
`public/javascripts/`. Measured against real trees that filter is:

- **too narrow** — it passes `libraries/htmlpurifier/`, `inc/libraries/`, `js/tiny_mce/`,
  `app/code/community/Stripe/`, `source/fonts/`, `html/appCore/addons/` and a bare top-level
  `phpmailer/`, all genuinely third-party;
- **too broad** — it rejects `lib/`, and `p214`'s *genuine* `formalms` recovery was
  `html/lib/System/license/license_english.txt`.

So path shape alone cannot decide ownership. The discriminator that did work: **a licence file is
the project's own when the manifest or `README` points at it, or when its copyright holder is the
project or its author** — which is why `read_grants.py` reads the manifest channel alongside the
file channel rather than falling back to it.

## Result

`25` of `94` recovered an own grant — `13` from a licence file in the tree, `12` from a manifest.
`ACTION QD` limb `1` fires *(threshold `15`)*. `23` current-state cells were corrected in the same
pass under `ACTION QG`, and `7` cells that already held the right answer were deliberately left
alone — the latter is the more useful number, because the same shelves carried both.
