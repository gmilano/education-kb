---
industry: education
region: Global
updated: 2026-10-20
---

# `p348-scope-provenance` — a grant has a SCOPE and a PROVENANCE, and neither is a path blacklist

Discharges `ACTION ZZ-z` (pin + tree + scope grading), `ACTION ZZ-u` (a grant at depth
licenses its package, not the repository), `ACTION ZZ-y` (the copyright-holder line as a
placement channel), `ACTION ZZ-ab` (`NCSA` in the family vocabulary, `ECL-2.0`
re-checked) and `ACTION ZZ-w` (the byte-order-mark axis).

## Why it is not another ladder rung

`ACTION ZZ-q` closed the rung question at p347: **the axis list is unbounded.** Case,
spelling, extension, depth, and `LICENSE` existing as a **directory** were five axes
found in one pass, and the sixth was not predicted. Two reads dissolve all of them:

```sh
git ls-remote --symref https://github.com/<slug> HEAD   # the pin.  Kills the ref axis.
git clone --filter=blob:none --no-checkout --depth 1    # commit + trees, no blobs
git ls-tree -r --name-only HEAD                         # the COMPLETE tree
```

`p441` already does that much. **What it cannot do is say what a grant at DEPTH
governs**, and `ACTION ZZ-u` is the cost: `likr/canvas-lms-agent` carries two licence
files and the first in path order is `.agents/skills/skill-creator/LICENSE.txt` — a
vendored tool's own grant. `p441`'s answer to that class is `EXCLUDE_DIR_RE`, a
directory blacklist holding `node_modules`, `vendor`, `third_party`, `.corepack`; and
`.agents/skills/` is not in it. **It could be added. The next one would not be** — which
is the defect `p441`'s own docstring names in its first paragraph: *widening a list
cannot fix a list.*

## So provenance is decided by the payload

| verdict | means | decided by |
|---|---|---|
| `REPOSITORY-GRANT` | an own-holder licence text at the ROOT | position |
| `PACKAGE-GRANT-ONLY` | own-holder grants exist, all in subtrees | position + holder |
| `FOREIGN-GRANT-ONLY` | every licence text names another holder | **the holder line** |
| `ABSENCE-ENUMERATED` | no licence-shaped path in the complete tree at the pin | the tree |
| `UNRESOLVED` | the address does not answer | `ls-remote` |

Verified live: `safytech/ulearn`'s TinyMCE **LGPL** at
`public/backend/curriculum/js/plugins/tinymce/.../license.txt` → **FOREIGN**, beside an
own **MIT** root; `AcademicsToday/academicstoday-django`'s **Twitter** Bootstrap grant →
**FOREIGN**, beside an own **Apache-2.0** root; `dodona-edu/dolos`'s `cli/`, `core/` and
`lib/` grants → **OWN**, which a blacklist cannot distinguish from vendored code.

## 🔴 The defect this instrument's own first build shipped

Build 1 of the holder channel read every line **containing** the word `copyright`. In an
MIT payload that is three lines and two are boilerplate present in every MIT grant on
GitHub, so the token set of every MIT file carried `{notice, permission, shall, holders,
liable, claim, damages}` and **any two MIT payloads "agreed" on their holder.** It graded
Twitter's vendored Bootstrap grant as `AcademicsToday/academicstoday-django`'s own —
precisely the `ZZ-u` over-grant this instrument exists to prevent.

Two conditions fix it: the line must **begin** with `Copyright`, and it must carry a
**four-digit year** (which drops Apache-2.0's appendix form `Copyright [yyyy] [name of
copyright owner]` — a FORM, not a holder). Both are controls.

**A channel that reads licence PROSE measures the licence, never its subject.** Third
surface of that error after the README badge and the manifest declaration, and the first
where this base wrote the detector itself.

## 🔴 `ACTION ZZ-ab` found the UNSAFE direction

p347 recorded the risk as detection **abstaining** on university licences. An abstention
fails safe under `P250`. **The first-hand read refutes it:** the real NCSA payload at
`cs341-illinois/coursebook` → `LICENSE/LICENSE.code` (1 698 B, HTTP 200) was graded
**`MIT`** by the canonical `p436.family_of`, because **NCSA's permission clause is
MIT-phrased** and the MIT rung sits above the BSD rung that would have caught its
three-clause body. NCSA carries a no-endorsement clause naming the University of Illinois
and NCSA; MIT carries only the notice — so the published cell **understated what a client
owes.** Fixed in both detectors, probed before MIT, pinned by controls in both directions.

The ECL leg of the same action found **nothing**: `sakaiproject/sakai`'s actual 11 120-byte
`LICENSE` names *"apache license"* zero times. One action, one axis, one real defect and
one false alarm — which is the argument for reading the payload rather than reasoning
about the licence.

## Usage

```sh
python3 -I scope_provenance.py slugs.input.2026-10-20.txt     # TSV to stdout
make gate-grant-scope                                          # 28 offline controls
```

## Declared limits

- The holder channel needs a holder LINE. `HOLDER-ABSENT` at the ROOT is still the
  repository's grant, because root **position** carries it.
- Token agreement is a **sufficient** test, never a necessary one. A holder line naming an
  institution in full (`Technical University of Munich`) does not agree with an owner
  handle carrying only its initialism (`ls1intum`), and no token folding fixes that — which
  is why the ROOT comparison runs first and why a subtree `FOREIGN` verdict is a reading
  list rather than a conclusion.
- `api.github.com` is 403 here and so is `github.com` over `curl`, so this instrument
  reports **no star count**. Commits, authors and timezones come from the blobless clone's
  own `git log`.
