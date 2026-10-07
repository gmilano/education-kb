---
industry: education
region: Global
updated: 2026-10-07
---

# `p441-tree-licence-enumeration` — stop enumerating filenames; enumerate the tree

**P441: a filename list can only FIND a licence. To sustain its ABSENCE you must ENUMERATE the
tree.** This is `P275`, which this KB proved and applied to *directory* listings, carried to the
licence layer, where it had never been applied.

## Why it exists: this KB has now found the same defect four times, and the fourth time in an instrument built one pass after it wrote the warning down

| When | What | The lesson it recorded |
|---|---|---|
| pass 52 | `@learninglocker/xapi-agents` ships `package/license` — lowercase, extensionless | the pass-51 tarball anchor was **case-sensitive** |
| pass 52 | trend 252 | *"a list of filenames is a cultural assumption"* — `COPYING.txt` in the GNU world |
| earlier | `openedx/XBlock` ships **`LICENSE.TXT`** | `repos/foundations.md`: *"Found at `LICENSE.TXT` — uppercase extension. A nine-name lowercase probe reports this [as ungranted]… two characters away from a name the probe already tried"* |
| **this pass** | `p436`'s **14-name** list still does not contain `LICENSE.TXT`, so XBlock was published `UNLICENSED` **again** — and `p440`'s **41-name widening missed it a third time** | 🔴 **widening a list cannot fix a list** |

`Opetushallitus/aoe` is the same hole on a different axis: its EUPL-1.2 grant is at
`aoe-web-frontend/LICENSE`, 303 B, in a **subdirectory**, and every probe in this KB is rooted.

## The channel

The one `P275` established, and it needs no API (`api.github.com` is 403 here):

```sh
git clone --filter=blob:none --no-checkout --depth 1   # the commit and trees, no blobs
git ls-tree -r --name-only HEAD                        # the COMPLETE tree, unpaginated
```

Over 87 repositories this takes **13 seconds** in total.

## Measured, 2026-10-07, over the 87 `UNLICENSED` rows

| Verdict | n | |
|---|---|---|
| `ABSENCE-ENUMERATED` | **76** | no path in the complete tree is a licence text. **This is the only verdict a filename list could not already reach** |
| `OWN-GRANT-AT-ROOT` | 4 | |
| `OWN-GRANT-IN-SUBTREE` | 5 | |
| `BUNDLED-GRANT-ONLY` | 2 | every confirmed grant belongs to a vendored dependency; the project's own is still absent |

🔴 **So 9 of the 87 do have their own grant, against 0 found by the 14-name list and 1 by the
41-name widening.**

| Slug | Verdict | Family | Path, and the axis the list missed |
|---|---|---|---|
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | root | **Apache-2.0** | `LICENSE.TXT` — **extension case** |
| [`nvaccess/nvda`](https://github.com/nvaccess/nvda) | root | GPL-2.0+ *(see below)* | `copying.txt` — **lowercase `COPYING`**, which the list has only in uppercase |
| [`SchoolUtils/WebUntis`](https://github.com/SchoolUtils/WebUntis) | root | **MIT** | `License` — **a third capitalisation** |
| [`veraPDF/veraPDF-library`](https://github.com/veraPDF/veraPDF-library) | root | **GPL-3.0 + MPL-2.0** | `LICENSE.GPL`, `LICENSE.MPL` — **family suffix**, which a dual-licensed project is forced into |
| [`Opetushallitus/aoe`](https://github.com/Opetushallitus/aoe) | subtree | **EUPL-1.2** | `aoe-web-backend/LICENSE`, `aoe-web-frontend/LICENSE` — **depth** |
| [`cs341-illinois/coursebook`](https://github.com/cs341-illinois/coursebook) | subtree | **MIT + CC-BY** | `LICENSE/LICENSE.code`, `LICENSE.original`, `LICENSE.output` — **a licence directory holding three grants** |
| [`learningequality/kolibri-server`](https://github.com/learningequality/kolibri-server) | subtree | **GPL** | `debian/copyright` — **the packaging convention** |
| [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) · [`-Responsive-Design`](https://github.com/OS4ED/openSIS-Responsive-Design) | subtree | *(see limit)* | `docs/License.txt` |

🔵 **`cs341-illinois/coursebook` is worth a row of its own.** Three separate grants — **MIT** for the
code, **CC-BY** for the original content, and a third for the *output* — is the correct structure for
a course repository, and it is the structure a single `LICENSE` file cannot express. It is also
precisely why `LICENSE/` as a **directory** exists, and why a rooted filename probe reports a
teaching repository with exemplary licensing hygiene as having none.

## 🔴 Stage 2 exists because stage 1 overshoots, as symmetrically as the list undershoots

A pattern over paths is a **finding** channel and its positives are a reading list. The first build
published all 14 of its hits. Read, six were not the repository's grant:

| Row | The path | What it actually is |
|---|---|---|
| `learningequality/kolibri-design-system` | `lib/KIcon/precompiled-icons/material-icons/copyright/baseline.vue` | an **icon component** whose name is the word |
| `Kennisnet/edurep-xslt` | `copyrightandotherrestrictions.xsl` | an **XSLT transform** for a metadata field |
| `european-commission-empl/european-digital-credentials` | `edci-issuer/licence-EUPL 1.2-brightgreen.svg` | a **README badge image** |
| `mendezjerick/ReaDirect-V2` | `.corepack/v1/pnpm/10.34.5/LICENSE` | a vendored **package manager's** grant |
| `dini-ag-kim/school-curriculum-pg` | `src/ontology/utils/owl2shacl/LICENSE` | a vendored **tool's** grant |
| `foradian/fedena` | `public/javascripts/fckeditor/license.txt` | a vendored **editor's** grant |

So stage 2 **reads each candidate blob** and classifies it with the same `family_of` that `p436`
uses. A path whose payload classifies `UNKNOWN` is a name that merely contains the word.

🔵 **The Commission's `.svg` is the cleanest instance of `P342` this KB has measured** — *an
assertion of a licence is not a grant*. The badge says EUPL-1.2 and there is no licence text in the
tree; the correct verdict is `P314`, a grant to request in writing citing the publisher's own badge.

### And the own/bundled split needed DEPTH, not a vendor-name list

A segment denylist (`assets/`, `libraries/`, `plugins/`, `fonts/`…) let `foradian/fedena` and
`dini-ag-kim/school-curriculum-pg` through as their own grants, because neither path names a listed
segment. 🟢 **A project states its own licence at the root or one directory down** — `debian/`,
`docs/`, `LICENSE/`, `aoe-web-backend/` — **and nothing states its own licence four levels into a
static-assets tree.** `OWN_MAX_DEPTH = 2` plus the segment rule needs no vendor names and does not
grow.

## 🔴 The defect the controls found, which the sweep would have hidden

The first inventory rule was `(?:^|/)licenses?\.(?:json|xml|txt|csv|md)$` under `re.I`, meant to
exclude `licenses.json`. The `s?` and the `txt` together matched **`LICENSE.TXT`** — the single most
common licence filename there is, and the exact name this instrument was built to stop missing.
🔵 **The control caught it, the sweep did not: 87 trees would have come back one grant short and the
TSV would have looked clean.** An inventory is now **plural-only** and **data formats only**.

## 🔴 The limit that reordering cannot fix: a payload that NAMES other licences

`family_of` picks one family by probing in a fixed order, and this pass reordered it twice. The
reason is in the licence texts themselves:

| Payload | Names | Consequence before this pass |
|---|---|---|
| **MPL-2.0** §1.12 | defines *"Secondary License"* as the GNU **GPL-2.0, LGPL-2.1 and AGPL-3.0** | five MPL-2.0 repositories filed **GPL** |
| **EUPL-1.2** Appendix | lists **GPL-2.0, AGPL-3.0, LGPL-2.1, MPL-2.0, EPL-1.0** | every EUPL payload read **UNKNOWN** |
| **`nvaccess/nvda`** `copying.txt` | *"the GNU General Public License version 2 or later, **with two special exceptions**"*, and an exception names the **LGPL** | GPL-2.0 reads **LGPL** |

🟢 Reordering fixes the first two, because there the **granting** licence is identifiable from the
head. 🔴 **It cannot fix the third.** Deciding which named licence is *granted* and which is merely
*referenced* is a reading task, and a substring classifier structurally cannot do it. So
`family_marks()` does not guess — it **counts**, and a count above one marks the family with `?` and
lists the marks in `names_multiple`. That is the same move `p436` made for `UPSTREAM` and `p184` for
`HOLDER-UNRELATED`: where the instrument cannot decide, it hands over a reading list.

Rows marked this pass: `nvaccess/nvda` (GPL+LGPL), `veraPDF`'s `LICENSE.MPL` (GPL+MPL — correct, it
*is* dual), `libraries/htmlpurifier/LICENSE` (LGPL names GPL — correct, LGPL references it).

## Declared reading limits

- 🔴 **`docs/LICENSE.rtf` is RTF and is not read.** `family_of` takes plain text, so an RTF grant
  classifies `UNKNOWN` and lands in `rejected_paths`. Both `OS4ED/openSIS-*` rows carry one, and
  both are published with this limit attached rather than as unlicensed.
- ⚠️ **A confirmed path proves a licence text is present, not that the project intended it to govern
  the whole repository.** `veraPDF`'s `LICENSE-HEADERS.md` classifies GPL and is a style guide;
  harmless there because `LICENSE.GPL` and `LICENSE.MPL` sit beside it, recorded because the next
  tree may not be so forgiving.
- ⚠️ **`ABSENCE-ENUMERATED` is about the licence TEXT, not about the grant.** Six of the 76 declare
  a licence in their package registry instead — see `p440`.

## The controls (`test_enumerate.py`, 40/40, offline)

Pure functions, no network. 8 positives covering the four axes a filename list cannot reach
(extension case, lowercase `COPYING`, a third capitalisation, depth, family suffix, licence
directory, packaging convention, GNU's `COPYING.LESSER`); 11 negatives, **six of them rows the first
build actually published**; 7 for the own/bundled depth rule, each paired with the own-subtree path
it must not eat; 4 for the mark counter; 3 for the plural-inventory fix; and the empty-denominator
exit 2 (**P355**).

## Run

```sh
python3 test_enumerate.py                                             # 40/40, offline
python3 -I enumerate_licence.py slugs.input.2026-10-07.txt > result.tsv
```

## Files

- `enumerate_licence.py` — clone, enumerate, filter, confirm, split own from bundled
- `test_enumerate.py` — 40 controls, no network
- `slugs.input.2026-10-07.txt` (87) · `result.2026-10-07.tsv` — **authoritative**
