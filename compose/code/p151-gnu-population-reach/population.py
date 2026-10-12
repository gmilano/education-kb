#!/usr/bin/env python3
"""p151-gnu-population-reach — `ACTION FU`: `T77`'s reach over all **58**, not 28.

> 🟡 **`ACTION FU`** — measure `T77`'s reach over all **58** subjects rather than the 28
> trees p150 held, by reading every licence file's title line.
> 🔴 *Refuted if the GNU-family population is larger than seven* — which would mean
> `p145`'s census mis-sorted rows INTO non-GNU classes as well as within the GNU family,
> and every licence figure on this shelf needs re-deriving.

## Why the question was open

🔴 **p150 identified the GNU-family population FROM THE ARTEFACT UNDER SUSPICION.** It took
the seven rows the census had *published* as `AGPL-3.0`/`LGPL`/`GPL` and measured those.
🔵 **That is circular in one direction only** — it can find a row mis-sorted *within* the
GNU family, and it cannot find a row the body matcher sorted *out* of it. p150 said so and
registered this action rather than arguing the point: *"a row with no sibling mention
cannot be mis-sorted — an argument, not a measurement."*

🟢 **This module measures it.** It reads the title line of **every** licence file in the
population, independently of what the census published, and compares three things: what
the retired matcher said, what the title surface says, and whether the two disagree.

## The one direction a falsification could come from

For the population to be larger than seven, some row published as non-GNU would have to
carry a licence file whose TITLE is a GNU licence. 🔵 **That is a real shape**, not a
hypothetical: a `LICENSE` holding GPL text in a repository whose `package.json` says
`MIT` is a common mistake, and the body matcher *would* mis-sort it, because
`BODY_HINTS`' MIT rung (*"Permission is hereby granted, free of charge"*) is tried before
the GNU rungs and GPL text does not contain it — so the GNU rungs would in fact fire.
🔵 The reachable failure is the other order: an `Apache License` rung firing on a GNU file
that quotes Apache, which is why the Apache rung's position is asserted in the tests.

🟢 **Measured, 2026-10-12, pass 151: the population is SEVEN, by both surfaces
independently, over all 58 subjects.** `ACTION FU`'s falsifier is silent.

🟢 **And a second result the action did not ask for: coverage.** 39 of 58 subjects ship a
licence file, and **39 of 39 carry a readable title line** — so replacing the body matcher
with the title surface costs *nothing*. A narrower surface that answered less often would
have been a trade; this one is not.

🔴 **The eighth GNU-family row, named so it is not later discovered as a correction.**
`moodle-mcp-server-aql-0.1.7` DECLARES `AGPL-3.0` in `package.json` and ships no licence
file. It is GNU-family at the declaration layer and `T77` cannot touch it, because there
is no body to mis-read. **8 GNU-family ids across 58 rows; 7 of them read from a body.**

    python3 population.py /tmp/edu-trees /tmp/edu-npm/trees
"""
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                os.pardir, "lib"))
import licence_identity as LI  # noqa: E402

COLS = ("subject", "tier", "licfile", "naive", "title", "clause", "n_licence_files")


def read(path, limit=400000):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read(limit)
    except OSError:
        return ""


def row(root, subject, tier):
    """One subject's three readings.

    `naive` is `LI.retired_identify` — the WHOLE published ladder in its published order,
    not the single AGPL rung. 🔵 Using the single rung reported 37 differing rows where
    the census's real delta is 5; the comparison is only meaningful against the matcher
    that actually ran.
    """
    if not os.path.isdir(root):
        return dict(subject=subject, tier=tier, licfile="NO_CLONE", naive="-",
                    title="-", clause="-", n_licence_files=0)
    names = [f for f in sorted(os.listdir(root)) if LI.LICENCE_NAMES.match(f)]
    if not names:
        return dict(subject=subject, tier=tier, licfile="-", naive="-", title="-",
                    clause="-", n_licence_files=0)
    body = read(os.path.join(root, names[0]))
    return dict(subject=subject, tier=tier, licfile=names[0],
                naive=LI.retired_identify(body) or "-",
                title=LI.title_spdx(body) or "-",
                clause=LI.clause_licence(body) or "-",
                n_licence_files=len(names))


def population(rows):
    """The GNU-family population by each surface, and the rows where they differ.

    Returns a dict with `by_title`, `by_naive`, `differ`, `with_file`, `with_title`.
    🔵 `by_naive` is computed from the retired matcher so the two populations can be
    compared *as populations* — which is the thing p150 could not do.
    """
    with_file = [r for r in rows if r["licfile"] not in ("-", "NO_CLONE")]
    return dict(
        by_title=[r["subject"] for r in rows if LI.GNU_FAMILY.match(r["title"])],
        by_naive=[r["subject"] for r in rows if LI.GNU_FAMILY.match(r["naive"])],
        differ=[r["subject"] for r in with_file if r["naive"] != r["title"]],
        with_file=[r["subject"] for r in with_file],
        with_title=[r["subject"] for r in with_file if r["title"] != "-"],
    )


def walk(bases):
    rows = []
    for base, tier in bases:
        if not os.path.isdir(base):
            continue
        for name in sorted(os.listdir(base)):
            p = os.path.join(base, name)
            if os.path.isdir(p):
                rows.append(row(p, name, tier))
    return rows


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    bases = [(argv[1], "github-50")]
    if len(argv) > 2:
        bases.append((argv[2], "npm-8"))
    rows = walk(bases)
    print("\t".join(COLS))
    for r in rows:
        print("\t".join(str(r[c]) for c in COLS))
    p = population(rows)
    e = sys.stderr.write
    e("rows=%d\n" % len(rows))
    e("licence files=%d   with a readable TITLE line=%d\n"
      % (len(p["with_file"]), len(p["with_title"])))
    e("GNU-family by TITLE=%d: %s\n" % (len(p["by_title"]), ", ".join(p["by_title"])))
    e("GNU-family by RETIRED matcher=%d: %s\n"
      % (len(p["by_naive"]), ", ".join(p["by_naive"])))
    e("rows where the two surfaces DIFFER=%d\n" % len(p["differ"]))
    multi = [(r["subject"], r["n_licence_files"]) for r in rows
             if r["n_licence_files"] > 1]
    e("rows with more than one licence file=%d %s\n" % (len(multi), multi))
    # 🔴 The action's falsifier, evaluated in the module rather than in prose.
    e("ACTION FU falsifier (population > 7): %s\n"
      % ("FIRED" if len(p["by_title"]) > 7 else "SILENT"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
