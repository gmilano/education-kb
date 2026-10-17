# `pass259-grant-location-class` — WHERE a grant was read, and what that entitles you to conclude

`ACTION YU` (registered by `p258`, highest priority) asked for a **code-header tier** on the
grant ladder, *"starting with `version.php` for Moodle plugins"*, with the falsifier *"fewer
than `5` of the `9` known Moodle rows resolve a family from a code header"*.

**`7` of `9` resolved, across two independent owners — `GPL-3.0-or-later` every time.**
Discharged, not refuted.

And then the pass found why the rows had looked grantless, which is not what the ACTION
assumed.

## The finding: `version.php` was already on the ladder

It is **Tier C, position 1**, and has been since the tier was built.

- [`p247-path-class`](../p247-path-class/) grades it `MANIFEST` — correctly.
- The `MANIFEST` contract says *"una DECLARACION, no un payload: la lee la gramatica de
  ecosistema, **nunca el clasificador de cuerpo**"*. That rule is right, and this base paid
  for it at `p246`.
- A Moodle `version.php` declares `$plugin->version`. It declares **no licence**. The grant is
  the comment **above** the declaration.

So the path was fetched, the manifest grammar found no licence field, and a complete
`GPL-3.0-or-later` notice was never graded. Two passes then widened the list of Tier-A path
**names** (`590` probes, `0` rows moved) looking for a file that was never missing.

🔴 And [`p222-ecosystem-bound-grammar`](../p222-ecosystem-bound-grammar/bound_grammar.py#L106)
has carried this line the whole time:

```python
'version.php':     'prose',       # Moodle's mandated GPL header
```

The answer `ACTION YU` asked for was written down in this base's own instrument, with that
exact comment, **four passes before the ACTION was registered**. Nothing consumed it. That is
`p251`'s *unwired knowledge* and `p253`'s *nothing consumes the wire*, now on a path rather
than a predicate.

**The defect was never a missing path. It was that one path carries two different KINDS of
evidence, and the ladder keys its contract on the path.** This module keys it on
`(path, payload)` instead, and `location_class("version.php")` with no body still answers
`ECO-MANIFEST` — because without the body that is genuinely all you know.

## What each location entitles a reader to conclude

Not uniform, and flattening it is how a bare `GPL-3.0` cell gets written over a notice that
says *"or (at your option) any later version"*.

| location class | family | bound | terms | the real row behind it |
|---|---|---|---|---|
| `LICENCE-FILE` | ✅ | ✅ | ✅ | `OS4ED/openSIS-Classic` `docs/License.txt`, `17 286` B |
| `CODE-HEADER` | ✅ | ✅ | ❌ | `bycs-lp/moodle-quizaccess_ai` `version.php` |
| `ECO-MANIFEST` | ✅ | ✅ | ❌ | `composer.json`, `pyproject.toml` — `p222` owns the grammar |
| `APP-MANIFEST` | ✅ | ❌ | ❌ | `nextcloud/live_transcription` `appinfo/info.xml` → `agpl` |
| `BARE-TOKEN` | ✅ | ❌ | ❌ | `frappe/education` `license.txt`, **`19` B**: `License: GNU GPL V3` |
| `UNKNOWN` | ❌ | ❌ | ❌ | a `README`, a placeholder repo, `src/license.go` |

`reading_strength()` returns the tuple, never a boolean. A consumer that collapses this to
*"has licence: yes/no"* reproduces `p258`'s Creative Commons defect one layer out.

## The four causes of a false `grantless`, each measured on a real row

| cause | the row | what actually happened |
|---|---|---|
| `BODY-NOT-GRADED` | `7` Moodle plugins | path fetched, contract forbade reading the body |
| `TIER-NOT-RUN` | `OS4ED/openSIS-Classic` | grant at `docs/License.txt` — **Tier B, which the reprobe did not run** |
| `CHANNEL-ABSENT` | `nextcloud` × `2` | `appinfo/info.xml` is on **no tier at all** |
| `ABSENCE-UNCONFIRMED` | `frappe/education` | `p258` recorded `404` at a Tier-A path holding a file committed **`2022-04-27`** |

🔴 **Of five causes, a longer list of path NAMES fixes exactly one.** `CAUSES_A_LONGER_PATH_LIST_FIXES`
is a constant so the next pass has to look at it.

## The absence predicate

`p258`: *a `403` from one **endpoint** was generalised to a whole channel.*
`p259`: **a `404` from one **attempt** was recorded as a property of the repository.**

`absence_verdict()` therefore refuses to emit an absence from a single observation:

- any `200` → `ABSENCE-REFUTED`
- two or more non-`200` → `ABSENCE-CONFIRMED`
- exactly one non-`200` → `ABSENCE-UNCONFIRMED`, **not publishable as an absence**

Measured rather than stipulated: `13` of `p258`'s `14` absences reproduced byte for byte on a
fresh Tier-A sweep. The ladder is sound; the single-observation rule was what was missing.

## The pointer that points nowhere

`OS4ED/openSIS-Classic`'s header carries a grant **and** `See license.txt.` in the same
comment — and there is **no `license.txt`**: `404` on six spellings at root, and absent from
the entire repository (verified in a full checkout; the only licence-named files are
**vendored** third-party grants under `assets/` and `libraries/`, which is `p247-path-class`'s
`BUNDLED` class).

`p254` established that *a pointer to a licence is not a grant*. `p259` adds the sharper case:
**a pointer may never defer a grant standing beside it**, because the target can be fiction.

## Running it

```
cd compose/code/pass259-grant-location-class && python3 test_grant_location.py
```

`60` controls, in `make hooks`. Every fixture is a payload read first-hand at `p259` over
`raw.githubusercontent.com` on an `ls-remote`-resolved ref (or, for `addheader.php`, from a
shallow clone). **`5` mutants run; each one fails `1`–`2` controls and the control count holds
at `60` for all five** — no silent skip.

🔵 The subject reuses [`p222`](../p222-ecosystem-bound-grammar/)'s `read_bound()` for prose
headers instead of writing a sixth family classifier. That is `P237`'s rule, and `P237` exists
because a pass that wrote its own classifier reintroduced the `GPL-3.0`/`AGPL-3.0` section-13
defect this base had already paid for.

## What it does NOT do

- It does **not** fetch. It grades `(path, payload)` pairs a prober already has.
- It does **not** re-grade the shelves. `ACTION YV`'s `828` content-licence cells are a
  separate population and stay open.
- `app_manifest_licence()` knows **one** application manifest (`appinfo/info.xml`). Odoo,
  WordPress and Drupal manifests are unassessed, not absent.
