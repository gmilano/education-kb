---
industry: education
region: North America
updated: 2026-10-12
---

# `p142-dead-repo-recovery` — `ACTION DE`: the payload is terminal, the REGISTRY is not, and the README over-claims by 2.4×

## The action, as p141 wrote it

> Resolve what happened to `owentaylor/canvas-mcp`. Read `@owen-x-tech/canvas-mcp` 1.1.0's own
> tarball for any surviving pointer — CI config, source-map `sources` paths, `.npmignore`
> residue, issue or changelog URLs — and `git ls-remote` any candidate owner spellings.
> 🔴 *Refuted if the payload carries no pointer beyond the dead URL, which would make "declared
> repository unreadable" terminal for this row and would mean the 62-tool `MULTI_SURFACE`
> surface can never be audited anywhere but the tarball.*

## Verdict: 🔴 **DISCHARGED and REFUTED on the channel it named — and answered on one it did not**

| channel | result |
|---|---|
| payload URLs | 🔴 **one pointer, and it is the dead URL.** Everything else is a `w3.org` / `json-schema.org` namespace, Instructure's public API docs, or a `your-*.instructure.com` placeholder |
| source-map `sources` | 🔴 **`['../src/index.ts']`, relative, `sourceRoot` empty.** No absolute path, no author directory |
| CI config, `.npmignore`, changelog | 🔴 **none shipped.** The tarball is 12 files: README, `package.json`, `.env.example`, 8 build artefacts, 1 minified UI |
| `git ls-remote`, 8 owner spellings | 🔴 **all unreadable**, and the nonexistent control is unreadable identically |
| 🟢 **registry metadata** | 🟢 **`maintainers[0] = owen-x-tech <ogsoccer2006@gmail.com>`**, same `_npmUser` on both versions |

🔴 **So the falsifier fires: the payload is terminal.** "Declared repository unreadable" is the
end of the line for the artefact, and the 62-tool surface can be audited nowhere but the tarball.

🔵 **But the action scoped itself to the tarball, and the live pointer is one layer out.** The
npm *account* survives with a contactable address. It is free-mail and carries no institution,
so it places nothing and settles no region — 🔵 **it is a person who can be asked, which is a
different and more useful thing than a repository that can be read.** Worth separating, because
p141's `ACTION CY` concluded *"for four of six rows there is no reachable repository at all"* and
did not distinguish *no repository* from *no publisher*. Here there is a publisher.

## 🟢 62 tools, confirmed a THIRD time, by a third implementation

p139 measured 62 statically. p140 reimplemented and got 62. This pass extracts the `const tools =
[ … ]` array by bracket matching and counts name literals **inside it**:

| measure | value |
|---|---|
| name literals inside the `tools` array | 🟢 **62** |
| distinct | 🟢 **62** — no duplicates |
| name literals anywhere else in `index.js` | **0** |
| `tools.push` / `concat` / spread mutation | 🔴 **none** — the array is fixed at module load |

🟢 **Three independent measurements, one figure.** And it refines p140's reading: the array is
*static*; what is dynamic is the **registration loop** that walks it, which is why a
registration-site count returns 1 and `tools/list` returns 62.

## 🔴 The new finding: the README claims 150+ tools and the package serves 62

```
## Features
**150+ Tools** covering all major Canvas LMS resources:
```

🔴 **A 2.4× over-claim**, in the one document a buyer can still read now that the repository is
gone. 🔵 **And it inverts `P138-E`**, which concluded from the Moodle tier that description drift
*"under-documents rather than over-claims"*. That held where it was measured. It does not hold
here, and the row where it fails is the row with no repository to check it against.

🔵 The same README is internally consistent *below* the headline — its per-section counts read
"2 tools", "3 tools", "4 tools", "5 tools", "6 tools" and sum to something near 62. 🔴 **So the
150+ is a headline written separately from the body**, which is the ordinary shape of this error
and the reason a static count is worth publishing next to it.

## Reproduce

```sh
./recover.sh     # all five channels, control last
```

Committed: [`result.2026-10-12-p142.tsv`](result.2026-10-12-p142.tsv),
[`packument.2026-10-12-p142.json`](packument.2026-10-12-p142.json) (the registry metadata as read).
