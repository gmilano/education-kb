---
industry: education
region: Global
updated: 2026-10-17
---

# `pass275-grant-enumeration` — `P275` applied to LICENCE paths, which is where it had never been applied

## 🔴 Read this first: the method here is NOT new to this base

[`compose/code/p275-tree-enumeration/`](../p275-tree-enumeration/) — **pase 93, `2026-10-04`** —
already states the principle, in its own words:

> **`P275`**: *para sostener una ausencia en un árbol hay que ENUMERARLO. Un canal que trunca
> sirve para HALLAR; un negativo suyo sólo vale con el tramo declarado.*

and already ships the instrument: `sweep_tree.sh`, a
`git clone --filter=blob:none --no-checkout --depth 1` plus `git ls-tree -d -r`. It even carries the
**`P278`** corollary, which describes this pass's defect exactly:

> **`P278`**: *un conteo de CERO sobre una ruta que no existe en esa ref mide la RUTA, no el contenido.*

🔴 **So the finding of pass 275 is not a method. It is that this base held the principle, the
corollary and the working code for ~180 passes and applied them only to DIRECTORY trees** — ILIAS
components, `frappe`, `openeducat` — **while the licence work went on extending path ladders.**

| domain | what the base did | result |
|---|---|---|
| **directory** trees (pase 93) | 🟢 enumerated, with a declared positive control | ILIAS *"no AI in core"* upgraded from *sostenido CON LÍMITE* to **closed** |
| **licence** paths (p267 → p274) | 🔴 extended a ladder to `19 paths × 4 refs`, then published the empty result as *"no grant"* | **two false negatives**, one of them carried three passes |

🔵 **`p274` wrote the diagnosis for this and did not apply it to itself:** *"a correction applied to
one instance is not a correction to the class."* `P275` was the correction; licences were a different
instance. This directory is the same correction, applied to the class it had been missing.

## What the two false negatives were

| row | carried verdict | enumeration found | why the ladder could not reach it |
|---|---|---|---|
| `ls1intum/Athena` | *"no grant across 76 path/ref probes over three passes; treat as all-rights-reserved; ask TUM in writing"* | **12 of 14 manifests declare `license = "MIT"`** | the ladder probed the **root** `pyproject.toml` — a **632 B** Poetry workspace stub with **zero occurrences of `license`**: the one manifest in the repo that is silent (`T47`) |
| `os4ed/openSIS-Classic` | *"no licence payload served on any path tried"* | **`docs/License.txt`** — verbatim GPL-2.0, **200**, **17 286 B** | the ladder tried `docs/LICENSE`. The file is **mixed case *and* `.txt` *and* under `docs/`** — straight `P278` |

🟢 **And `p274`'s actual request — `ls-remote` as a positive control — passed cleanly on all 13 slugs.**
`gegok12/gegok12` fails with `rc=128` exactly as a nonexistent repository does; every other
negative-verdict slug resolves. **The hypothesis it was testing was wrong, and buying it first was still
right**, because running it is what exposed the ladder.

## The two halves

| half | file | network | what it does |
|---|---|---|---|
| **online** | `enumerate.sh` | yes — `git` smart-HTTP | `ls-remote` for existence, then blobless clone + `git ls-tree -r` for **every** path. Emits `evidence/tree-enumeration.*.tsv`. Out of `make hooks` by the Makefile's own rule |
| **offline** | `enumeration_gate.py` | **no** | fails any shelf asserting an absent grant an enumeration refutes; **queues** every negative verdict never enumerated |

```
make gate-enumeration       # offline, in `make hooks`
make enumerate SLUGS=f.txt   # online, by hand
```

🔵 **Difference from `sweep_tree.sh`, and why this is a sibling rather than a duplicate:** that one
enumerates **directories** (`ls-tree -d`) to answer *"is there an AI component in the core"*. This one
enumerates **files** (`ls-tree` without `-d`) to answer *"is there a grant anywhere in this tree"*, and
then classifies what it finds — which a directory sweep cannot do.

## `candidate_grants()` — a licence-like path is not a grant

Three exclusions, each with a control, each drawn from this base's own rows:

- **vendored** dependency licences — openSIS alone carries **20** (ckeditor, PhpSpreadsheet, htmlpurifier);
- **source files** that merely carry the word — `LicenseService.java` in Artemis;
- **icon assets** — `kolibri-design-system` holds **7** licence-like paths and **all 7 are Vue icon
  components** (`KIcon/precompiled-icons/mdi/license.vue`). A naive grep calls that a grant.

## 🔴 Five corrections the gate earned by being RUN, not by being designed

Four share one root cause — **one line can carry two subjects**:

1. It reported **`ls1intum/Artemis`**, an MIT row with a root `LICENSE`, as **refuting itself**: the
   phrase on that line is about **Athena**, named four slugs later in the same cell.
2. Nearest-preceding-**slug** was still wrong where the subject is the bare word **Athena** in bold
   prose and the only hyperlink is Artemis. **A project need not be hyperlinked to be the subject** —
   and teaching it bare names found **2 further** live occurrences of the openSIS claim.
3. It flagged **this pass's own new row**, which opens *"**Artemis's** feedback-suggestion engine"*.
   **A possessive is a modifier, not a subject.**
4. 🔴 **A DEAD SLUG LAUNDERED A FALSE CLAIM.** `gegok12/gegok12` (dead) and `Gego-K12/gegok12` (real,
   MIT at root) share the basename `gegok12`; attributing to the dead one made **three** stale
   *"NOT ESTABLISHED"* restatements read as correctly-verified absences. **`p251-prefix-collision`'s
   class, one axis over.** Non-resolving slugs are now excluded from name attribution.
5. 🔴 **A SUPPRESSING PREDICATE MUST BE NARROWER THAN THE ROWS IT SUPPRESSES.** `states_a_grant()` — *a
   line cannot coherently assert "no grant" and publish the grant* — was added so correction prose would
   stop self-flagging. With a global `re.I`, its `\bLICEN[CS]E\b` alternative (meant to match a
   **filename in caps**) matched a vendor's marketing prose, *"free core is free forever under the MIT
   licence"*, and **silenced two live stale claims.** **Case is load-bearing: `LICENSE` is a filename,
   `licence` is a word.** A gate's own false negative is the worst kind — it reports `PASS`.

## State at `p275`

`REFUTED=0` · `VERIFIED-ABSENT=28` · `QUEUE-UNENUMERATED=124` · **30 controls**, including the **C3
positive control** `sweep_tree.sh`'s doctrine requires (*"un instrumento que no reproduce un positivo
conocido no sostiene una ausencia"*): the predicate must find both grants this pass read first-hand.

🔵 **`QUEUE-UNENUMERATED=124` is not a failure signal** — it is the honest size of the backlog, printed
on every `make hooks` run. **Two of the first thirteen rows enumerated were false**, which is the only
sample this base has of how wrong the ladder-shaped evidence is.

---

# `p276` — what WORKING this instrument's own backlog did to it

🔵 **`p275` closed by saying the queue was *"budget, not design."* It was both.** 30 of the 124 queued
rows were enumerated in two channels. All 30 slugs resolve, **9 negative verdicts were refuted, 7
positive controls passed, 18 absences are now sayable in both channels** — and the instrument failed
three ways on its own backlog.

## 🔴 D1 — the gate did not implement the finding that motivated it

`p275`'s headline was `ls1intum/Athena`: **no licence file in the tree**, `license = "MIT"` in **12 of 14
manifests**. It found that by hand — and then built a module that reads `git ls-tree` **file paths only.**

| row | file channel | manifest / registry channel |
|---|---|---|
| `DMontgomery40/mcp-canvas-lms` | 36 paths, none licence-like | `package.json` **MIT** + npm **MIT × 19 versions** |
| `meyerjp3/psychometrics` | 395 paths, none licence-like | `pom.xml` `<licenses>` **Apache-2.0** |
| `LearnPress/learnpress` | 1 985 paths, none licence-like | `readme.txt` **GPLv3** + `composer.json` **GPL-3.0-or-later** |

**Run as built, the gate would have stamped all three `VERIFIED-ABSENT`.** `load_manifest_ledgers()` now
reads `evidence/manifest-channel.*.tsv`, and an absence requires **both** channels empty.

🔴 **Sub-species worth keeping: two channels can agree because they share one blind spot.**
`ECNU-ICALK/EduChat` returned nothing on six path probes **and** `license: null` from GitHub's API —
because `LICENSE` is a **directory** there. Every probe hit a tree instead of a blob; the API's detector
failed for the same reason. **The agreement read as corroboration.**

## 🔴 D5 — bare-name attribution had no specificity test, and one ordinary row armed it

`p275` taught `attribute()` to match a **bare repository name** (Athena was named in bold prose with no
link). 🔴 **Enumerating `frappe/lms` then attributed FOURTEEN lines across FIVE shelves to it, and
THIRTEEN were about other projects** — `mcp-canvas-lms`, `canvas-lms-mcp`, `AI-LMS-TMS`, `tutor-lms-mcp`
(`\b` **does not stop at a hyphen**: `-` is itself a non-word character), plus the prose *"the LMS-side
MCP servers"* and *"a proprietary LMS"* (`re.I` makes **a noun a name**).

**A `REFUTED` row FAILS the gate**, so the ledger would have turned `make hooks` red on thirteen claims
about six other projects. 🔵 **The fix is `p275`'s own sentence** — *"case is load-bearing: `LICENSE` is a
filename, `licence` is a word"* — **applied to the predicate that ASSIGNS rows instead of the one that
SUPPRESSES them.** Case-sensitive matching, a token-boundary guard rejecting `[-_/A-Za-z0-9]` on either
side, and `MIN_BARE_NAME = 4`. **27 → 11 refutations; all 16 removed were false.**

## 🔴 D2 — `candidate_grants()` had no SCOPE test

A licence-like path was counted as *the repository's grant* whatever it actually covered:

- **asset-scoped** — `mendezjerick/ReaDirect-V2` carries **22** licence-like paths and **all 22 licence
  art** (CC0 sprites, OFL fonts, generated-asset attributions);
- **dataset-scoped** — `open-spaced-repetition/srs-benchmark`'s `dataset/LICENSE` is **`144` B** and says
  *"request permission"* — **the inverse of a grant**;
- **translation** — forma.lms ships `license_english.txt` … `license_tamil.txt`, **twelve translations of
  one GPL-2.0** whose real payload is `html/license.txt`.

Unpatched, the first two report **REFUTED**. `SCOPED` and `TRANSLATION` now exclude them, each with a
control. ⚠️ **`debian/copyright` is deliberately still a grant** — it is scope-limited (DEP-5 `Files:`
stanzas naming five paths) but real, and the ledger records the scope in prose rather than dropping it.

## 🔴 D3 — the grant-evidence vocabulary was written from an idea of the house style, not measured against it

`GRANT_EVIDENCE` is meant to recognise a line that **publishes** a grant, so a correction does not read as
a live negative verdict. Three gaps, all measured:

| gap | mechanism | corpus-wide |
|---|---|---|
| **D3a** | the house writes byte counts as `` `1 531` B `` — the **backtick sits between the digits and the unit**, and the token could not cross it | **361** lines carry a count it could not see; **4** reach the gate |
| **D3b** | the house also asserts a first-hand read in **prose** (*"the payload is the verbatim BSD-3 form"*); only *"read at payload"* was listed | 2 lines |
| **D3c** | a row whose grant lives in metadata publishes it by **naming the manifest** (*"`pom.xml` `<licenses>`"*, *"MIT (metadata)"*) — **D1's defect inside the vocabulary** | 3 rows that are **right** read as live negative verdicts |

🔵 **Both numbers are published because conflating them would be the inflation this base polices:** the
latent gap is 361 lines, the live effect is 6.

🟢 **A hypothesis tested and REFUTED, recorded because an informed negative is information:** *"the queue
is inflated by BSD boilerplate, since `NEGATIVE` matches `all rights reserved` and that is line 2 of the
BSD form."* **Measured: 2 of 124 rows (1.6%).** The queue is overwhelmingly genuine (115/124, 92.7%).

## 🔴 A self-correction earned by running this against the live shelves

`load_manifest_ledgers()` first tested `key not in ("-", "<no license key>")` — **an equality test on a
free-text cell.** `Nasus20202/MoodleMCP`, whose cell reads *"<no license key in any>"* (it has five
`package.json` files), was read as a **declared grant**. **An absence marker must be matched by
predicate**, or the gate manufactures a presence out of prose. `ABSENT_KEY` now does that.

## ⚠️ STATE, AND WHAT IS NOT VERIFIED

**Expected after this patch: `REFUTED=0 · VERIFIED-ABSENT=48 · QUEUE-UNENUMERATED=70`, `47/47` controls.**

🔴 **Nothing here was EXECUTED.** The sandbox hosting `p276` refuses to run scripts from a cloned
repository, and that refusal was respected rather than circumvented. The patch was validated **as data**
(`ast.parse`; every module-level regex literal extracted and compiled; all 18 new controls checked against
an independent reimplementation of the predicates that reproduces `p275`'s published state exactly).
**`p277` must run `make hooks` and `python3 -I test_enumeration_gate.py` before trusting any of it** — see
`intel/open-gaps.md`, Gap 1.

🔴 **And one known regression, declared rather than hidden:** `states_a_grant()` is **line-scoped** while
`attribute()` is **subject-scoped**, so on `repos/trending.md:1358` — which carries both `EduChat`
(a false absence) and `sitor-ai/frametell` (`AGPL-3.0`, `34 523` B) — D3a reads *frametell's* byte count
and silences *EduChat's* false claim. `p275` fixed this exact *"one line, two subjects"* shape in
`attribute()` and left it in `states_a_grant()`. **Scoping the suppression to its subject's span is
`p277`'s ranked #1 for this instrument**, and was deliberately not attempted unrun.
