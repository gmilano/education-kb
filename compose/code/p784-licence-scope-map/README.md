# `p784` — licence **scope** map (`Gap 282`'s remedy), and `Gap 281`'s fixture

**Declared** pass 60 · **closed** pass 61.

## The defect it closes

Every licence probe on this shelf answers **"*where* does the grant hide?"** — `p759`'s four
layers are file → below-reference → manifest → headers — and returns a **scalar** family.

🔴 **Measured counter-example, pass 60:**
[`haolpku/K12-KGraph`](https://github.com/haolpku/K12-KGraph) `@865bc35` ships **two** licence
files with **different scopes**:

| path | family | bytes | scope, per the README |
|---|---|---|---|
| `LICENSE` | 🔴 **CC BY-NC-SA 4.0** | 2 244 | the **dataset** |
| `LICENSE-CODE` | 🟢 **MIT** | 1 075 | the **code** |

🔴 A probe that **breaks on the first** of the 16 filenames reads `LICENSE`, returns NC and
**wrongly rejects usable MIT code**. 🔴 One that happened to order `LICENSE-CODE` first
returns MIT and **wrongly admits an NC dataset**. **Both directions are wrong**, and the
repo is honest — the README states the split.

🟢 **So this probe does not break.** It enumerates **all 16** names and emits a
`{path → family}` map with a verdict: `SINGLE` · `PARTITIONED` · `UNGRANTED`.

## Usage

```sh
bash probe.sh haolpku/K12-KGraph 865bc35   # -> PARTITIONED, exit 3
bash probe.sh moodle/moodle                # -> SINGLE GPL-3.0, exit 0
bash test_scope_map.sh                     # 17 assertions, offline
bash test_scope_map.sh --live              # + the two network fixtures
```

Exit status: `0` SINGLE · `3` **PARTITIONED** · `4` UNGRANTED · `5` unreachable.

## 🟢 `Gap 281` — closed here, with a real instance and a real fix

Pass 60 declared that the shared classifier's GPL-2.0 protection is **case-dependent** and
said **no uppercased GPL-2.0 payload had been located**. 🟢 **Pass 61 derived one from the
real payload and the gap has an instance.**

🔴 **The defect, measured not supposed.** `lib/license_family.sh:323` gates LGPL with a
**case-sensitive `case` glob over the WHOLE payload**. GPL-2.0's preamble names the LGPL —
*"(Some other Free Software Foundation software is covered by the GNU Lesser General Public
License instead.)"* — at **byte offset 849** of the real 18 092 B `leogaggl/lxHive` payload.

| payload | gate 323 (`case` glob, whole payload) | emitted |
|---|---|---|
| real `lxHive` (title-cased) | 🟢 misses — mention is mixed-case | **GPL-2.0** ✅ |
| same payload, `tr`-uppercased | 🔴 **hits** — mention is now in caps | **LGPL** ❌ |

🔵 **So the instrument that exists to prevent `P753` commits `P753` internally**, and
survives only by the *accident* that real GPL-2.0 payloads are title-cased. 🔴 The mutation
class is **not** synthetic: `p288/fixtures/agpl-3.0-kuali-kfs-reflowed.LICENSE` is a real
reflowed GNU payload already on this shelf.

🟢 **The fix is not a case-insensitive variant** — that is strictly worse, since it would
then match the mixed-case original too. 🟢 **The fix is to scope the gate to the title
block.** This probe uppercases a copy and applies the LGPL gate to the **first 400 B**; the
offending mention sits at **849**, outside it. Both payloads classify **GPL-2.0**.

🆕 **`P781`: a gate that tests for a *relative's name* must be scoped to the title block.
Casefolding changes which accident protects you; scoping removes the accident.**

## 🔴 One measurement artifact, recorded because it cost a reconciliation

🔴 **`probe.sh` reports bytes via `$(curl …)`, and command substitution strips trailing
newlines** — so its byte counts run **1 low for any payload ending in `\n`**, and exactly
right for any payload that does not. Measured both ways this pass: `lxHive` `18091` vs
`18092`, `xapijs/cmi5` `1070` vs `1070`. 🟢 **The prose rows in this KB carry the
`curl | wc -c` value**, which is the true size; 🔵 a reader diffing them against probe
output should expect the off-by-one and not treat it as a contradiction.
