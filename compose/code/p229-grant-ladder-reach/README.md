---
industry: education
region: Global
updated: 2026-10-15
---

# `p229-grant-ladder-reach` — the 45 "grantless" slugs, and what was actually wrong

**Pass 229, 2026-10-15, 20:4x → 21:3x UTC.** ⏱️ **Second pass of this date** (p228 ran
earlier the same day). Stated because this shelf pins SHAs, and two passes sharing a date
is exactly what a later pass reads as a contradiction.

Discharges `ACTION SW` (p229's registered highest priority), `ACTION SX`, `ACTION SY`,
`ACTION SZ`, and the standing `ACTION SH`, `ACTION RE` and `ACTION PD`.

```sh
make hooks                                   # the standing offline gate, 28 controls
./ladder.sh --reach                          # the probe vocabulary, printable (T272)
./ladder.sh slugs.txt out/                   # the network limb
python3 test_grant_ladder_reach.py           # every control, offline
```

## `ACTION SW` — limb `1` fires at `23` against a threshold of `5`

p228 reported `149` cells across `45` slugs as `CELL-WITHOUT-GRANT`, with the note
`6 paths x 2 refs`. That note was the hypothesis, and it was right: the class was a REACH
bound, not a grantless population.

| state | slugs | what it means |
|---|---|---|
| 🟢 `RESOLVED` | **23** | a grant read first-hand AND attributable to this repository |
| 🟡 `GRANT-BY-REFERENCE` | 2 | `NOTICE` names the licence and links it; the body is not served |
| 🔴 `FOREIGN-MANIFEST` | 4 | the manifest declares a DIFFERENT project (`T229-M2`) |
| 🟡 `CHANNEL-SILENT` | 4 | `200` on a manifest that declares no licence at all |
| 🔴 `NO-GRANT` | 6 | genuinely silent at 40 paths × up to 3 refs |
| 🔴 `ABSENT` | 6 | the slug does not resolve AT ALL — a state p228 could not express |

The ladder was extended on **both** axes, and the second one is new here:

- **PATH** — 40 names in three tiers: root licence names, the non-root paths these shelves
  already record (`docs/License.txt` for openSIS, `html/license.txt` for formalms,
  `public/` for Moodle 5.0 per `P973`), and the manifest channels of p222's grammar table.
- **REF** — the REAL default branch from `git ls-remote --symref`, not the guess
  `main|master`. One request returns existence, default branch and HEAD SHA, so the ref
  stops being a guess and the SHA gets pinned.

**The single most load-bearing row on these shelves was in the grantless class.**
`moodle/moodle` serves the canonical `GPL-3.0` body at `COPYING.txt` — `35 147` B, title at
offset `0`. p228 missed it because its six names included `COPYING` and not `COPYING.txt`.

## 🔴 `T229-1` — the harvester truncates a repository name at its first dot

The `ABSENT` class is not six dead repositories. Four of the six are the harvester's own
output. `p228-shelf-gate/harvest_cells.py` carries:

```python
SLUG_RE = re.compile(r"github\.com/([A-Za-z0-9][A-Za-z0-9_-]*)/([A-Za-z0-9][A-Za-z0-9_.-]*?)(?=[)\s`,.;:'\"\]]|$)")
```

The repository half **allows** `.` inside the name and the lookahead **terminates** on `.`,
and the quantifier is **non-greedy** — so the lookahead wins at the first dot:

| cited on the shelves | harvested as | truth |
|---|---|---|
| [`processing/p5.js`](https://github.com/processing/p5.js) ×3 | `processing/p5` | 🟢 **`LGPL-2.1`**, `license.txt`, `24 480` B |
| [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) ×25 | `dmitry-viskov/pylti1` | 🟢 **`MIT`**, `1 070` B |
| [`jdolny/OneRoster.NET`](https://github.com/jdolny/OneRoster.NET) ×8 | `jdolny/OneRoster` | 🟢 **`MIT`**, `1 066` B |
| [`nakafaai/nakafa.com`](https://github.com/nakafaai/nakafa.com) ×4 | `nakafaai/nakafa` | 🔴 **NON-OSI, noncommercial**, `7 705` B |
| [`JushBJJ/Mr.-Ranedeer-AI-Tutor`](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor) ×36 | `JushBJJ/Mr` | 🟡 genuinely grantless — **confirms p176** |

`31` dotted names are cited across the live shelves, `122` mentions in all, and the
collapse is **many-to-one**: four distinct `UOC/java-lti-1.3*` repositories all harvest to
`UOC/java-lti-1`, and three `dmitry-viskov/pylti1.3*` repositories to one slug.

🟢 **The honest bound, measured rather than feared: `0` of `12` truncations resolve to a
DIFFERENT real repository.** So the defect costs SILENCE — a readable grant reported as
grantless — and never a wrong licence attributed to the wrong subject. It is the mirror of
p224's `T224-2`: that pass taught the harvester to reject a dotted OWNER as a hostname, and
the same dot in the REPOSITORY half has been truncating names ever since.

## 🔴 `T229-M2` — the foreign manifest, a seventh non-grant subject

p228 enumerated five subjects a licence token can have that are not a grant. The extended
ladder's gate produced exactly **one** disagreement against the live cells, and it is a
sixth-and-seventh:

[`alfredang/ai-mms`](https://github.com/alfredang/ai-mms) carries a cell reading `MIT`. Its
root `composer.json` declares `"license": ["OSL-3.0", "AFL-3.0"]` — a live, expensive defect
in the permissive direction, until the same file's **second line** is read:

```json
"name": "openmage/magento-lts"
```

The repository is a Magento fork serving UPSTREAM's manifest at its root. The licence is
real, first-hand and correctly parsed, and it is **not a statement about this repository**.
`4` of the `20` manifest declarations are foreign — two of them unrenamed `laravel/laravel`
skeletons. The control is nearly free and nothing in this base had it: **a manifest's `name`
is a claim about whose manifest it is, so compare it with the slug before attributing.**

> 🟢 **With that one withdrawn, the extended ladder's verdict on the live shelves is
> `124` cells CONFIRMED and `0` wrong.** The gate's standing value is cheap verification,
> exactly as p228 concluded — and this pass is the second independent measurement of it.

## `ACTION SX` — limb `2`: the marker is safe, and the gate that doubted it was not

**Mechanism, named:** `harvest_cells.NARRATIVE_RE` matches the word `corrected`, and the
marker IS the string `<!--corrected-->`. **The marker matches the pattern that suppresses
the cell.** `106` marked lines sit on the live shelves and p228 gated none of them.

The fix is one distinction the predicates never drew — an HTML comment is METADATA about
the line, not prose on it — after which p228's five predicates run unchanged. `54` cells
gate; `9` controls hold the behaviour, `6` of which must not fire.

🔴 **And then this instrument produced fifteen findings, and every one was its own.**

| rule | findings | what survived reading the line |
|---|---|---|
| draft: the LAST token outside the comment | 24 | — |
| 🆕 `T229-SX1`: the FIRST token (positional) | 10 | — |
| reading all ten on their lines | — | 🟢 **`0`** |

Every survivor was an **`AUDIT-ROW-STRUCK-VALUE`**: a row whose *purpose* is to display a
wrong value beside its correction, so the marker sits on the WITHDRAWN value by design.

```
| `frappe/frappe` | 🟢 MIT ⚠️ was GPL-3.0<!--corrected--> |
| `acanas/swad-core` | 🔴 AGPL-3.0 <!--corrected--> | ... this shelf published GPL-3.0 until p228 |
```

Reading the last token inverts both rows and republishes the value the pass withdrew.
`classify_grant.py` already held the answer — *the earliest title in document order decides* —
and a table row obeys the same order: the licence COLUMN precedes the commentary.

🟢 **So p228's exclusion was RIGHT, for a reason p228 did not state.** It excluded these
cells because the marker tripped a narrative pattern; the real reason they are safe is that
they are audit rows. All `8`+ corrected values hold. The marker is not a hiding place.

## `ACTION SY` — limb `1` at `6` of `14`

Six Moodle plugins settle their bound at `version.php`'s mandated GPL header, carrying
`9` of the `26` `BOUND` cells to `GPL-3.0-or-later`, read first-hand.

🔴 **The easiest false positive this pass could have published, and the rule that stopped
it:** `bigbluebutton/bigbluebutton`'s `main/LICENSE` is `7 652` B of **canonical LGPL-3.0
body**, whose own text says *"any later version"* twice. p225 and p227 both established
that the canonical body is NOT a channel for the project's bound. Rejected.

The remaining eight stay `-only` under p227's conservative precedent, resting on ABSENCE
and saying so.

## `ACTION SZ` — limb `1`: the unit is the `(query, record)` pair

p228's `ACTION SP` tried to narrow the EU AI Act subject by demanding a jurisdiction token
in the RECORD and fired limb `2` (STOP): it dropped a genuine EU record — EU by the question
that produced it, jurisdiction-free in its own words — and gained an irrelevant one.

Keying on the QUERY's jurisdiction instead re-admits that record and still drops all five
Vietnamese ones. `6`/`6` controls. An UNSCOPED query falls back to SP's record test, so `SZ`
never sees less than `SP` did.

🔵 **`ACTION RE` has required the verbatim query beside every finding for ten passes, so the
pair was already on disk. This instrument just stops throwing half of it away.**

## 🔴 Two defects this pass found in its own work before publishing

- **`T229-M1`, the unreachable bound.** The Moodle reader's first draft wrote the or-later
  clause as a trailing OPTIONAL group behind a LAZY `.{0,120}?`. A lazy quantifier stops at
  the earliest position where the rest can match, and a trailing optional group matches the
  empty string right there — so the clause was unreachable and every Moodle plugin read
  `unspecified`. 🟢 **It is the same shape as `T229-1` upstream: a lazy quantifier against a
  permissive terminator always stops early.** Two instances, one pass, two instruments.
- **A control built on a truncation.** An `ACTION SZ` control quoted a record cut off at
  `27 July 2026` and asserted it must fire. It did not, and the CONTROL was wrong: the
  subject token sat in the clause the truncation removed. Recorded rather than quietly
  lengthened — it is `ACTION RE`'s rule one layer down.

## Why `make hooks` was possible this pass and not the eleven before it

🔴 **The suites only pass from their own working directory.**
`python3 -I compose/code/p228-shelf-gate/test_shelf_gate.py` dies on
`ModuleNotFoundError: classify_grant` because `-I` strips the script's directory from
`sys.path`; the same file passes `30`/`30` from inside its folder. That is
`p355-cwd-portability`'s class, and it is why a working gate stayed a one-off for eleven
passes: it could not be invoked from the place a hook runs. Every `Makefile` recipe `cd`s
into its instrument, and the ONLINE half is kept out of `hooks` so the check still runs
where there is no egress.

## Reach, printed rather than copied (`T272`)

`tierA=15 tierB=15 tierC=10 total=40 byte-floor=1B ref=ls-remote-default+main+master`

🔴 **And the reach is still bounded, with two measured proofs.** `ACTION SX` turned up two
cells whose grants my 40 paths miss and the shelves already record:
`anthropics/prompt-eng-interactive-tutorial` at `AmazonBedrock/LICENSE` and
`ProjectsAndPrograms/school-management-system` at `student_panel/LICENSE` — both `200`.
🟢 **A grant can sit in an ARBITRARY subdirectory, so no fixed vocabulary closes this class.
The paths this KB has already recorded beat any list a pass invents** → `ACTION TA`.
