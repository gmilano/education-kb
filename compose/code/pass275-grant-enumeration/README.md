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
