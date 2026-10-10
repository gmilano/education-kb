---
industry: education
region: Global
updated: 2026-10-10
---

# p112-dependency-closure — does it resolve to the same bytes twice

**Pass 112, 2026-10-10.** `test_p112.sh` → **109 passed / 0 failed**, fully offline
(real git repositories committed on disk and served to the real `depclosure.sh` over
`file://`; no mocks). `depclosure.sh` read **296 of 296** addresses in **4 m 41 s**,
`rc=0` on every one, **zero unread**, alongside a no-stage-B control run over the same
296 addresses.

## The question, and why p111 forces it

Six passes, and the first five could not reach this:

| pass | axis | reads | answers | cannot say |
|---|---|---|---|---|
| p107 | tag **count** | history | how much ref traffic | it inverts at the top of the shelf |
| p108 | release **identity** | history | *can I pin it* | whether the pin is from 2019 |
| p109 | commit **recency** | history | *is it alive* | who is keeping it alive |
| p110 | author **concentration** | history | *what if they stop* | whether I can take it over |
| p111 | verification **surface** | tree | *can I tell when I broke it* | **whether that check survives leaving GitHub** |
| **p112** | **dependency closure** | tree | *does it resolve the same twice* | whether the pinned versions are any good |

p111 put **115 of 296 rows (38.9 %)** at `checked`: a suite, a live CI system, a
`pull_request` trigger. But `checked` is a claim about a pipeline on **GitHub's
infrastructure**, and p110 found **200 of 296 rows are one person**, so two thirds of
this shelf must be vendored at a SHA and owned inside a client's estate. The moment the
suite moves off GitHub Actions, *"CI runs the suite"* decays into *"a suite ran once,
against whatever the registries served that morning"*.

**Result: of those 115 `checked` rows, 63 are `pinned`. So 21.3 % of this shelf — not
38.9 % — can both tell you when you broke it and give you the same dependency set
twice.**

## What it emits

Thirteen columns, one row per address:

```
slug  rc  files  vendor_stripped  manifests  ecosystems  lockable  locked
      lockfiles  deps_in_tree  reqs_pinned  deployable  verdict
```

### The verdict ladder

| verdict | meaning | rows | share of 296 |
|---|---|---|---|
| `UNREAD` | fetch failed — no claim made (`P1040`) | **0** | **0 %** |
| `no-manifest` | nothing declares dependencies → not applicable | 51 | 17.2 % |
| `foreign-build` | declared in bazel / odoo / moodle-plugin / cmake → no claim (`P112-N`) | 7 | 2.4 % |
| `floating` | manifests, no lock anywhere, nothing vendored | **68** | **23.0 %** |
| `partial-pin` | some lockable ecosystems locked, others not | 42 | 14.2 % |
| `self-pinned` | maven only — direct versions literal, transitives resolved (`P112-B`) | 16 | 5.4 % |
| `vendored` | no lock, but the dependency tree is COMMITTED (`P112-D`) | 5 | 1.7 % |
| `pinned` | every lockable ecosystem present is locked | **107** | **36.1 %** |

On the **238** rows that declare resolvable dependencies: `pinned` 45.0 %, `floating`
28.6 %, `partial-pin` 17.6 %.

## Channel

Anonymous git lane only, re-probed live this pass:

| endpoint | result |
|---|---|
| `git ls-remote` / `git fetch` | `rc=0` |
| `raw.githubusercontent.com/<slug>/HEAD/…` | `200` |
| `api.github.com` | `403` (`P107-A`, session scoping) |

So `/contents` and `/dependency-graph` cannot be read. The tree comes from a depth-1
blob-filtered fetch; requirement-file **bodies** come from a batched lazy blob fetch
against the same promisor remote — the mechanism p111 established at `P111-H`.

## The disciplines, each of which a draft of this pass got wrong

| id | discipline |
|---|---|
| `P112-A` | A manifest is an exact **basename**, never a substring. `docs/requirements.rst` is prose about a curriculum and it is on this shelf; so are `package.json.sample` and `go.mod.txt`. |
| `P112-B` | **Ecosystems differ in whether the manifest itself pins.** maven writes literal versions for direct deps and has no lockfile in ordinary use → `self-pinned`, never counted as locked. go.mod names exact versions and go.sum carries their hashes → go is lockable with go.sum as the lock. |
| `P112-C` | A vendored tree is stripped before any arithmetic (inherits `P111-C`) — **and counted**, because committing it is the strongest form of this property, not an absence of it. |
| `P112-D` | **A committed dependency tree needs no registry at all.** `vendor/`, `node_modules/`, `Pods/`, `Godeps/`, `third_party/` earn `vendored`. Build residue (`.venv`, `site-packages`, `.tox`, `*.egg-info`) is stripped **without** that credit: a machine's leftovers are not a declaration. |
| `P112-E` | **Lock reach is not measured, and the error direction is stated.** One lockfile anywhere counts its ecosystem as locked, so every figure here is an **upper bound** on pinning — it can only make a row look more reproducible than it is. |
| `P112-F` | **A `requirements.txt` pinned with `==` throughout IS a lock**, and no filename can tell you which kind you have. Stage B reads the bodies. Measured against the control run: **14 of 296 rows change verdict** (9 `floating→pinned`, 4 `partial-pin→pinned`, 1 `vendored→pinned`). Without it this KB publishes 93 `pinned` instead of 107. |
| `P112-G` | **A library that floats its dependencies is behaving correctly** — pinning is the application's job. `deployable` separates rows shipping a deployment artefact from rows that do not: **21** rows ship a deployment and float everything; **47** floating rows ship none. |
| `P112-H` | **The batch stream carries headers that look like requirements.** `git cat-file --batch` interleaves `<sha> blob <size>` lines; they are not comments, do not start with `-`, carry no `==`, and a naive line scan reads every one as an *unpinned requirement* — so a perfectly pinned repo reports `floating`, with the error growing as the number of requirement files grows. Dropped on an anchored 40-hex pattern. |
| `P112-I` | Inherited from `P111-I`: `set -o pipefail` plus an early-exiting reader inverts a signal. Bodies go to a **file** and every probe reads the file. |
| `P112-J` | **A vacuous file is not a pinned file.** A requirements file holding only `-r base.txt` has no unpinned line in it; promoting a row on that is promoting it on a file that declares nothing. |
| `P112-K` | **A lockfile is evidence only about an ecosystem the repo declares.** A stray `Gemfile.lock` with no `Gemfile` is reported in `locks=` and never credited in `lockedcnt`. |
| `P112-L` | **The regional placement is a committed file** (`orgs.region.tsv`), not an undocumented derivation. p111's map of 93 rows was not written down and cannot be re-run or corrected; this one can. |
| `P112-M` | Three orgs are recorded **contested** and excluded from every regional total rather than silently assigned: `Apereo-Learning-Analytics-Initiative` (p111 placed it EMEA; the Apereo Foundation is US-registered), `opencast` (multi-country consortium), `huggingface` (US company, large FR base). |
| `P112-N` | **A declaration this instrument cannot resolve is not an absent one.** The first draft reported `oppia/oppia-android` (1 213 source files, Bazel), `OpenEduCat/openeducat_erp` (Odoo `__manifest__.py`), `microsoft/o365-moodle` (352 source files, Moodle plugin `version.php`) and four further Moodle plugins as declaring **nothing**. They are `foreign-build`, which claims nothing in either direction. |
| `P1040` | An unread row is never zero: `rc!=0` emits `UNREAD` with empty metrics. |

## The cross-checks this pass produced

**Agreement.** All **31** rows p111 called `no-code` come back `no-manifest` here — 31 of
31, from a different file set entirely (p111 read source extensions and CI configs; p112
reads manifests and lockfiles). Two independent tree axes agree exactly on which rows of
this shelf are not software.

**The mechanism.** Pinning falls monotonically with the number of lockable ecosystems in
the tree — **54.5 %** at one (n=134), **42.3 %** at two (n=78), **12.5 %** at three
(n=8), **0 %** at five and at nine — and mean ecosystem count rises with bench size
(`broad` 1.64, `small` 1.59, `pair` 1.41, `solo` 1.30). That is why p110's bands appear
to invert on this axis: `broad` is the worst `pinned` band (20 %) not because big teams
are sloppier but because they ship more ecosystems, and each one is another lockfile
somebody has to own.

## Files

| file | what it is |
|---|---|
| `depclosure.sh` | the census driver; `P112_BASE`, `P112_WORK`, `P112_NO_BODY` |
| `manifests.awk` | the path classifier, driven directly by the tests as well as through the driver |
| `addresses.txt` | the 296 shelf addresses, carried from p111 unchanged |
| `orgs.region.tsv` | the committed regional placement map (`P112-L`, `P112-M`) |
| `test_p112.sh` | 109 assertions, fully offline, real git repos over `file://` |
| `result.2026-10-10.tsv` | the census |
| `result-nostageB.NEGATIVE-CONTROL-2026-10-10.tsv` | the same census with stage B disabled — what makes `P112-F` a measurement |

## Reproduce

```sh
./test_p112.sh                                   # 109 passed / 0 failed, offline
./depclosure.sh addresses.txt > result.tsv       # ~4m41s over 296 addresses
P112_NO_BODY=1 ./depclosure.sh addresses.txt     # the negative control
```
