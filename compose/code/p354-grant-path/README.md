---
industry: education
region: Global
updated: 2026-10-21
---

# `p354-grant-path` — a published grant path asserts a BRANCH and a FILE, and this base was checking one

**Pass 354, 2026-10-21.** 🔵 Fifth pass of this date (`p350`, `p351`, `p352` and `p353`
earlier today). Discharges **`ACTION ZZ-au`**, registered by `p353`.

## What `p353` found, and why it asked for a gate rather than care

`p353` re-read every grant on `agents/top.md`'s four live tiers. **30 of 31 returned the
published licence exactly.** One returned **404**:
[`sandraschi/classroom-mcp`](https://github.com/sandraschi/classroom-mcp), published as
**MIT, read at `main/LICENSE`**.

🟢 **The licence was real and the path was wrong.** The default branch is `master`; the grant
is stock MIT, `1 071 B`, holder `Sandra Schipal`, 2026.

🔴 **And it was a REGRESSION, not a discovery.** `agents/top.md:1316` — this shelf's own
carried history — already published *"🟢 **MIT**, 1,071 B (`master`)"*, the same byte count
read from the same branch. Some pass between then and now rewrote a correct `master` into an
assumed `main`.

> 🔵 **A grant path asserts two things — a branch and a file — and `raw.githubusercontent.com`
> carries no branch default.** A row whose branch is wrong fails **CLOSED**: a permissively
> licensed repository reads as ungranted. That is the opposite direction from `p351`'s
> `THIRD_PARTY_SCOPE`, which fails **open**.

🟢 That is the whole case for a gate. A reader cannot see the difference between
`main/LICENSE` and `master/LICENSE` by looking; the wrong one looks exactly like a repository
with no grant; and the pass that introduced it had the right value in its own file. Attention
had already failed once.

## What this instrument does

| arm | runs in | what it proves |
|---|---|---|
| `make gate-grant-path` | 🟢 `hooks` (offline) | the **extractor** still parses the live shelves, with a denominator and a branch histogram |
| `make gate-grant-path-online` | 🔴 needs egress | every published grant path resolves **`200`** |

🔵 **The offline arm is the extractor and that is deliberate.** It is the half that can be
wrong silently: a claim the parser fails to see is a claim the online arm never probes, so an
under-counting parser would make this gate report green over a corpus it never read — the
masking shape `p300`'s runner exists to prevent, pointed inwards. **43 controls bind the
parse.** Zero claims is a **FAIL**, never a pass.

🔵 The online arm **calibrates first**, in `p293`'s shape: a positive control (this base's
anchor row, `HKUDS/DeepTutor` at `main/LICENSE`) and a negative one (`p353`'s own documented
404). A channel answering 404 for everything would report every row dead, so a failed control
pair yields **no verdict** rather than a guess.

## The first run accused three CORRECT cells, and that is the better finding

🔴 This instrument's first run over the live tree reported **three defects, and all three were
its own fault.**

| cell | what it publishes | what a `branch/path` parser read |
|---|---|---|
| `agents/top.md:341` | `tests/stubs/LICENSE.md` — a stub, *"correctly not counted as a second grant"* | branch `tests` |
| `agents/top.md:386` | `canvas-lms-mcp/LICENSE` — the directory holding `@likr/canvas-lms-mcp` | branch `canvas-lms-mcp` |
| `agents/top.md:387` | `packages/xapi/LICENSE`, beside its `package.json` | branch `packages` |

🟢 **Every one is a true, first-hand, REPO-RELATIVE path.** Probed as raw URLs they 404, so
the gate accused three cells that were right.

🔵 **This is this base's own recurring shape, for the fourth consecutive pass:**

| pass | the token | what it actually belonged to |
|---|---|---|
| `p351` | a **licence** | `THIRD_PARTY_SCOPE` — something that is not the repository |
| `p352` | a **star figure** | the comparison named in the same cell |
| `p353` | a cell reading like a **table header** | a transposed key-value row where `repo` is a key |
| **`p354`** | a **path** | the tree, not a raw URL |

> 🔵 **A token's MEANING is given by the cell it sits in, never by its shape.**

🔴 **No regex can separate them.** `master/docs/License.txt` and `packages/xapi/LICENSE` are
the same shape and different claims. 🟢 **What separates them is the COLUMN.** The live tiers
publish a dedicated **`Grant read at`** column holding exactly a `branch/path` for a raw read;
a pass write-up's table has no such column and its path cells are tree-relative.

🟢 So the parse binds to the **header**, which is structural, cannot be fooled by prose, and
is precisely the set `ACTION ZZ-au` means by *"every published grant path"*. All three false
positives are pinned as controls (`TheColumnBinding`) so no successor re-introduces them.

### The one ambiguity this gate cannot remove, stated rather than hidden

`p353`'s repaired cell names **two** paths, and the second is named in order to be refuted:

> `🔴 **`master/LICENSE`** — corrected at p353; this cell read `main/LICENSE`, which is **404**`

🔴 A parser taking the last, or all, would probe `main/LICENSE`, get the 404 `p353`
documented, and **report a defect against the one cell that was just repaired.** 🟢 The rule
is **FIRST-WINS inside the bound cell**: the asserted value leads and the commentary follows.

🔵 **Bound honestly: FIRST-WINS is a rule about cell ORDER, not about truth.** A pass that
wrote the refuted path first would be mis-parsed, and no gate here can catch that. What this
gate guarantees is that whatever a cell asserts **first** is reachable.

## Scope, stated rather than implied

🟢 The two append-only shelves — `agents/trending.md`, `repos/trending.md` — are **excluded
whole**. Every section in them is a dated record of what was true when measured, and nothing
in them is ever rewritten; a gate demanding a 2026-10-06 row's path resolve today would force
exactly the retro-editing this base's `dated-by-measurement` convention forbids. This is
`p352`'s *"only the live occurrence is judged"*, applied to a whole file.

🟢 Each of the six rewritable shelves is cut at its own marker — `## ⏷ Carried history …` —
matched on the **token**, because the pass number in it varies by file (339 on five shelves,
340 on `compose/patterns.md`) and will move again.

🔴 **A shelf with no marker is judged WHOLE rather than skipped.** The alternative fails open:
a pass that dropped the heading would silently remove its file from this gate's scope, and a
gate whose coverage shrinks when a line is deleted is not a gate.

## The result, and a figure `p353` published five times too small

🟢 **`ACTION ZZ-au` DISCHARGED. 47 of 47 published grant paths resolve `200`.** Calibration
pair reproduced exactly (`200` and `404`). Zero rows in a grant-bearing table lack a path.
Evidence: [`grant-path-liveness`](../../../evidence/grant-path-liveness.2026-10-21-p354.tsv).

🔴 **`p353` wrote:** *"`2` of the `31` rows on these tiers are `master`-default, so the `main`
assumption is wrong about **6 %** of the time."* 🔴 **Re-derived over every live grant row this
base publishes, the share is `16` of `47` — **34.0 %**, more than five times `p353`'s figure.**

| shelf | live grant rows | `main` | `master` | `master` share |
|---|---:|---:|---:|---:|
| `agents/top.md` | 29 | 26 | 3 | 10.3 % |
| `repos/foundations.md` | 18 | 5 | **13** | 🔴 **72.2 %** |
| **all live shelves** | **47** | **31** | **16** | 🔴 **34.0 %** |

🔵 **Two separate things make `p353`'s 6 % wrong, and both are worth keeping.**

🔴 **First, it is the `p352` ordering defect on a new quantity.** `p353` counted `2` of `31`
*before* writing its own correction — and its correction is what made
`sandraschi/classroom-mcp` a `master` row. Its own shelf, as committed, carries **3**.
`gate-census-currency` binds the address census; **nothing binds a ratio stated in prose**, so
the same mechanism `p352` built a gate against recurred one pass later on a different number.

🟢 **Second, and the more useful half: the hazard is not uniform, and it correlates with
repository AGE.** GitHub's default moved to `main` in 2020. `repos/foundations.md` is this
base's pre-2020 cohort almost exactly — `oppia`, `kolibri`, `ltijs`, `OpenOLAT`, `sakai`,
`opencast`, `edx-platform`, `frontend-app-learning`, `canvas-lms`, `chamilo-lms`, `ILIAS`,
`h5p-php-library` — and **13 of its 18 rows are `master`** once `judge0` joins them.

> 🔴 **The `main` assumption is most wrong exactly where this KB's most-recommended rows are.**
> Education's foundation layer is old software — six of eight Tier-1 learning platforms are
> GPL or AGPL institutional systems — so the branch default a 2026 pass reaches for by habit
> is wrong on **72.2 %** of that shelf.

🟢 **The cheap guard remains `--symref`**, as `p353` said: derive the branch, never assume it.
🟢 **The standing guard is this gate**, which would have caught the regression in the pass that
introduced it.

## What a successor should know

🟡 **`rows_without_a_path` is `0` today and is not asserted.** A gate pinning the denominator
would go red every time a pass adds a row, which is noise rather than a finding — and `p352`
settled that a census stated in the pass that writes it is stale by construction. What
`hooks` proves is that the extractor still runs and still sees claims; the `200`s are the
online arm's, by `ACTION ZZ-au`'s own wording.

🔴 **Registered as `ACTION ZZ-aw`:** no gate binds a RATIO published in prose. `p353`'s 6 %
is the second instance of the `p352` ordering class (after `p351`'s denominator), and the
first on a quantity that is not an address count.
