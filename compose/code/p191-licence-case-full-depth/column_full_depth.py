#!/usr/bin/env python3
"""p191 / `P1059` — the licence COLUMN at full depth, by enumeration instead of guessing.

What `ACTION NK` asked, and what this does instead
--------------------------------------------------
`ACTION NK` registered *"run the FULL `156`-variant `P1057` sweep over all `160` published
licence rows"*. 🔴 **Two things were wrong with that instruction, and both are findings.**

1. 🔴 **`156` variants is still a LIST.** `P1057` varies the CASE of a rooted stem, so it
   cannot reach `aoe-web-frontend/LICENSE` *(depth)*, `LICENSE/LICENSE.code` *(a licence
   DIRECTORY)*, `debian/copyright` *(packaging)* or `LICENSE.GPL` + `LICENSE.MPL` *(family
   suffix)*. `P441` already proved the generalisation in this KB — *a filename list can only
   FIND a licence; to sustain its ABSENCE you must ENUMERATE the tree* — and `ACTION NK` was
   written one instrument behind it. 🟢 **So the sweep runs over the TREE** via `P441`'s
   blobless-clone channel: every case variant at the root is a strict subset of it.
2. 🔴 **`160` was not the population.** `160` is what p190 happened to sweep. This module
   derives the population from the published pages themselves and finds
   **`1 246` slugs carrying a published licence id** — so p190's *"all published licence
   rows"* covered `13`% of them.

The question this answers is the one `ACTION NK` wanted answered: **does the licence this KB
PUBLISHES for a row survive reading that row's complete tree?**

Verdicts
--------
    AGREE                 an own grant is present and its family matches the published id
    CONTRADICTED          an own grant is present and NO published id matches it  🔴
    FAMILY-AMBIGUOUS      the own grant's payload NAMES more than one family (P441's `?`)
    TEXT-ABSENT           the tree holds no licence text at all, yet a licence is published
    BUNDLED-ONLY          every grant found belongs to a vendored dependency
    UNRESOLVABLE          the repository does not resolve over `git`

🔵 **`TEXT-ABSENT` is not `CONTRADICTED`.** A registry classifier, a README badge or a
`pyproject.toml` string can carry a true identifier with no text in the tree — `Gap 421`'s
whole family. Collapsing the two would turn this KB's own documented shapes into refutations.

Comparison is at FAMILY level, deliberately
-------------------------------------------
`family_of` answers `GPL`, not `GPL-3.0`, so a published `GPL-2.0` against a tree holding
GPL-3.0 text is `AGREE` here. 🔴 **That is a declared limit, not an oversight:** version
discrimination is `lib/licence_identity.title_version`'s job and `P613`'s, and asserting it
from a coarse family would manufacture contradictions this instrument cannot support.
"""
from __future__ import annotations

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
# `P355` is this KB's own cwd-portability rule, and `p441` imports `p436` with a RELATIVE
# path (`sys.path.insert(0, "../p436-fork-hypothesis")`), so running it from anywhere but
# its own directory raises `ModuleNotFoundError`. Absolute paths here, both of them.
_CODE = os.path.dirname(_HERE)
for _rel in ("p441-tree-licence-enumeration", "p436-fork-hypothesis"):
    sys.path.insert(0, os.path.join(_CODE, _rel))

from enumerate_licence import one  # noqa: E402  (p441, unchanged)

# published id -> the coarse family `family_of` can actually answer with.
PUBLISHED_FAMILY = {
    "AGPL-3.0": "AGPL-3.0", "AGPL-3.0-only": "AGPL-3.0",
    "GPL-3.0": "GPL", "GPL-3.0-only": "GPL", "GPL-2.0": "GPL",
    "LGPL-3.0": "LGPL", "LGPL-2.1": "LGPL",
    "Apache-2.0": "Apache-2.0", "MIT": "MIT",
    "BSD-3-Clause": "BSD", "BSD-2-Clause": "BSD",
    "MPL-2.0": "MPL-2.0", "EPL-2.0": "EPL", "EPL-1.0": "EPL",
    "ISC": "ISC", "Unlicense": "Unlicense",
    "CC0-1.0": "CC0-1.0", "CC-BY-4.0": "CC-BY", "CC-BY-SA-4.0": "CC-BY",
    "CC-BY-NC-4.0": "CC-BY", "EUPL-1.2": "EUPL", "EUPL-1.1": "EUPL",
    "ECL-2.0": "ECL-2.0", "MulanPSL-2.0": "MulanPSL",
    "CC-BY-NC-SA-4.0": "CC-BY",
}

# 🟢 A CONTROL, not a convenience: the population extractor and this comparator each carry a
# licence vocabulary, and when they drifted apart a row published `ECL-2.0` was compared
# against the `Apache-2.0` its own prose explained it against. Two platform rows were
# published as contradicted on that drift. Fail at import, loudly, rather than in a verdict.
sys.path.insert(0, _HERE)
from published_rows import IDS as _EXTRACTOR_IDS  # noqa: E402

_MISSING = sorted(set(_EXTRACTOR_IDS) - set(PUBLISHED_FAMILY))
if _MISSING:
    raise AssertionError(
        "p191: vocabulary drift — the extractor emits ids this comparator cannot map: %s"
        % ", ".join(_MISSING))

# `family_of` answers these; anything else is a payload it could not classify.
KNOWN_FAMILIES = set(PUBLISHED_FAMILY.values()) | {"GPL", "LGPL", "MulanPSL"}


def families_of_cell(cell: str) -> list[str]:
    """`P441`'s families column -> families, with its `?` ambiguity mark kept."""
    if not cell or cell == "-":
        return []
    return [f for f in cell.split(";") if f]


def compare(published_ids: list[str], p441_row: tuple) -> tuple[str, str]:
    """(verdict, detail). Pure: the network already happened in `P441`.

    `p441_row` is `(slug, verdict, n_paths, confirmed, families, rejected, ambiguous)`.
    """
    _slug, verdict, _n, confirmed, families, _rej, ambiguous = p441_row
    if verdict == "UNRESOLVABLE":
        return "UNRESOLVABLE", "-"
    if verdict == "ABSENCE-ENUMERATED":
        return "TEXT-ABSENT", "tree enumerated, no licence text"
    if verdict == "BUNDLED-GRANT-ONLY":
        return "BUNDLED-ONLY", confirmed
    found = families_of_cell(families)
    want = {PUBLISHED_FAMILY.get(i, i) for i in published_ids}
    plain = {f.rstrip("?") for f in found}
    if any(f.endswith("?") for f in found):
        return "FAMILY-AMBIGUOUS", "%s names several families (%s)" % (
            confirmed, ambiguous)
    if plain & want:
        return "AGREE", "%s = %s" % (confirmed, ";".join(sorted(plain)))
    return "CONTRADICTED", "published %s; tree says %s at %s" % (
        ",".join(published_ids), ";".join(sorted(plain)), confirmed)


def sweep(rows: dict[str, list[str]], workers: int = 8):
    """rows: slug -> published ids. Yields (slug, published, verdict, detail, p441)."""
    from concurrent.futures import ThreadPoolExecutor

    slugs = list(rows)
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for slug, p441_row in zip(slugs, ex.map(one, slugs)):
            verdict, detail = compare(rows[slug], p441_row)
            yield (slug, ",".join(rows[slug]), verdict, detail, p441_row)


def main() -> int:
    if len(sys.argv) < 2:
        sys.stderr.write("usage: column_full_depth.py <rows.tsv>  "
                         "# slug<TAB>id,id  (from published_rows.py)\n")
        return 2
    rows: dict[str, list[str]] = {}
    with open(sys.argv[1], encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 2:
                continue
            rows[parts[0]] = [p for p in parts[1].split(",") if p]
    if not rows:
        # `P355`: an empty denominator is a path fault, not a clean column.
        sys.stderr.write("p191: empty population — a path fault, not a clean column\n")
        return 2
    print("slug\tpublished\tverdict\tdetail\tp441_verdict\tconfirmed_paths\tfamilies")
    sys.stdout.flush()
    for slug, pub, verdict, detail, p441_row in sweep(rows):
        print("\t".join([slug, pub, verdict, detail, p441_row[1],
                         p441_row[3], p441_row[4]]))
        sys.stdout.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
