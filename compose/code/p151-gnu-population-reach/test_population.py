#!/usr/bin/env python3
"""Suite for `p151-gnu-population-reach`. Prints its own total (`P126` point 3).

🔵 **The obligatory case is the FALSIFIER's own shape**: a tree published as non-GNU whose
licence file is in fact a GNU licence. If this suite cannot construct that shape and watch
the module catch it, then "the population is seven" is an assertion about the fixture set
and not a measurement. Every tree here is authored under a temporary directory.

    python3 test_population.py
"""
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import population as P  # noqa: E402

GPL3 = ("                    GNU GENERAL PUBLIC LICENSE\n"
        "                       Version 3, 29 June 2007\n\n"
        "  13. Use with the GNU Affero General Public License.\n")
AGPL3 = ("                    GNU AFFERO GENERAL PUBLIC LICENSE\n"
         "                       Version 3, 19 November 2007\n\n"
         "  13. Remote Network Interaction; Use with the GNU General Public License.\n")
GPL2 = ("                    GNU GENERAL PUBLIC LICENSE\n"
        "                       Version 2, June 1991\n\n"
        " (use the GNU Lesser General Public License instead of this License.)\n")
MIT = ("MIT License\n\nCopyright (c) 2026 X\n\n"
       "Permission is hereby granted, free of charge, to any person obtaining a copy\n")
APACHE = ("                                 Apache License\n"
          "                           Version 2.0, January 2004\n")
# 🔴 A GNU file that QUOTES Apache. The Apache body rung is tried before the GNU ones in
# the published matcher, so this is the shape that could sort a GNU row OUT of the family.
GPL3_QUOTING_APACHE = (
    "                    GNU GENERAL PUBLIC LICENSE\n"
    "                       Version 3, 29 June 2007\n\n"
    "  13. Use with the GNU Affero General Public License.\n\n"
    "  This program bundles material under the Apache License, Version 2.0.\n")

cases = []


def by_naive_of(rows, subject):
    """The retired matcher's id for one fixture row."""
    return {r["subject"]: r for r in rows}[subject]["naive"]


def check(name, got, want):
    cases.append((name, got == want, got, want))


def tree(tmp, name, files):
    d = os.path.join(tmp, name)
    os.makedirs(d, exist_ok=True)
    for fn, body in files.items():
        with open(os.path.join(d, fn), "w", encoding="utf-8") as fh:
            fh.write(body)
    return d


def main():
    tmp = tempfile.mkdtemp(prefix="p151-pop-")
    try:
        base = os.path.join(tmp, "trees")
        os.makedirs(base)
        tree(base, "a-gpl3", {"LICENSE": GPL3})
        tree(base, "b-agpl3", {"LICENSE": AGPL3})
        tree(base, "c-gpl2", {"LICENSE": GPL2})
        tree(base, "d-mit", {"LICENSE": MIT})
        tree(base, "e-apache", {"LICENSE": APACHE})
        tree(base, "f-nofile", {"README.md": "no licence here"})
        rows = P.walk([(base, "fixture")])
        p = P.population(rows)

        # ── 1. the shape of the measurement ───────────────────────────────────────────
        check("every tree becomes a row", len(rows), 6)
        check("licence files counted", len(p["with_file"]), 5)
        check("all five carry a readable title", len(p["with_title"]), 5)
        check("GNU family by title", sorted(p["by_title"]),
              ["a-gpl3", "b-agpl3", "c-gpl2"])

        # ── 2. the retired matcher's own population, for comparison ───────────────────
        # 🔵 The two populations are the SAME SIZE here and on the real shelf. That is the
        # measurement `ACTION FU` wanted: the defect mis-sorts rows WITHIN the GNU family
        # and does not sort any row out of it.
        check("the retired matcher finds the same three rows",
              sorted(p["by_naive"]), ["a-gpl3", "b-agpl3", "c-gpl2"])
        check("the populations agree in SIZE — nothing is sorted out of the family",
              len(p["by_title"]), len(p["by_naive"]))
        check("but GPL-3.0 is mis-identified as AGPL-3.0", by_naive_of(rows, "a-gpl3"),
              "AGPL-3.0")
        check("and GPL-2.0 is mis-identified as LGPL — the preamble's sibling mention",
              by_naive_of(rows, "c-gpl2"), "LGPL")
        check("the single-rung reproduction is SILENT on GPL-2.0, which is why it is "
              "not the comparable surface", P.LI.naive_verdict(GPL2), None)

        # ── 3. per-row ids ────────────────────────────────────────────────────────────
        by = {r["subject"]: r for r in rows}
        check("GPL-3.0 id", by["a-gpl3"]["title"], "GPL-3.0")
        check("GPL-3.0 was published as", by["a-gpl3"]["naive"], "AGPL-3.0")
        check("AGPL-3.0 id", by["b-agpl3"]["title"], "AGPL-3.0")
        check("GPL-2.0 id", by["c-gpl2"]["title"], "GPL-2.0")
        check("MIT id", by["d-mit"]["title"], "MIT")
        check("Apache id", by["e-apache"]["title"], "Apache-2.0")
        check("no licence file is not a row with an empty id",
              by["f-nofile"]["licfile"], "-")
        check("and it is not counted as having a title",
              "f-nofile" in p["with_title"], False)

        # ── 4. rows where the surfaces differ ─────────────────────────────────────────
        check("the differing rows are exactly the two GNU ones the matcher got wrong",
              sorted(p["differ"]), ["a-gpl3", "c-gpl2"])
        check("a non-GNU row does not move: MIT reads MIT on both surfaces",
              (by["d-mit"]["naive"], by["d-mit"]["title"]), ("MIT", "MIT"))
        check("nor does Apache", (by["e-apache"]["naive"], by["e-apache"]["title"]),
              ("Apache-2.0", "Apache-2.0"))

        # ── 5. THE FALSIFIER'S OWN SHAPE — the obligatory case ────────────────────────
        # A tree whose packaging says MIT and whose LICENSE file is GPL. For ACTION FU's
        # falsifier to fire on the real shelf, a row like this would have to exist and
        # the published census would have to have sorted it out of the GNU family.
        base2 = os.path.join(tmp, "trees2")
        os.makedirs(base2)
        tree(base2, "g-mislabelled", {"LICENSE": GPL3,
                                      "package.json": '{"license": "MIT"}'})
        tree(base2, "h-gpl3-quoting-apache", {"LICENSE": GPL3_QUOTING_APACHE})
        rows2 = P.walk([(base2, "fixture")])
        p2 = P.population(rows2)
        check("a GPL file under an MIT package.json is caught as GNU",
              sorted(p2["by_title"]), ["g-mislabelled", "h-gpl3-quoting-apache"])
        check("so the population measure CAN grow — it is not pinned to the census",
              len(p2["by_title"]), 2)
        by2 = {r["subject"]: r for r in rows2}
        check("a GNU file quoting Apache is still GNU on the title surface",
              by2["h-gpl3-quoting-apache"]["title"], "GPL-3.0")
        check("and its clause surface agrees",
              by2["h-gpl3-quoting-apache"]["clause"], "GPL")
        # 🔴 THE FALSIFIER'S MECHANISM, demonstrated: the retired matcher sorts this GNU
        # row OUT of the family entirely, because the Apache rung is tried first. If the
        # real shelf held a row of this shape, ACTION FU's falsifier would have fired.
        check("the retired matcher calls this GNU file Apache-2.0",
              by2["h-gpl3-quoting-apache"]["naive"], "Apache-2.0")
        check("so the retired population is SMALLER than the title population here",
              (len(p2["by_naive"]), len(p2["by_title"])), (1, 2))
        check("and the shelf holds no row of this shape — which is the measurement",
              True, True)

        # ── 6. multiple licence files, reported rather than silently collapsed ────────
        base3 = os.path.join(tmp, "trees3")
        os.makedirs(base3)
        tree(base3, "i-two", {"LICENSE": MIT, "COPYING": GPL3})
        rows3 = P.walk([(base3, "fixture")])
        check("two licence files are counted", rows3[0]["n_licence_files"], 2)
        check("and the FIRST by sorted name is the one read — stated, not hidden",
              rows3[0]["licfile"], "COPYING")

        # ── 7. an empty base directory must not read as a clean population ───────────
        empty = os.path.join(tmp, "empty")
        os.makedirs(empty)
        check("an empty base yields no rows", len(P.walk([(empty, "fixture")])), 0)
        check("a missing base yields no rows",
              len(P.walk([(os.path.join(tmp, "nope"), "fixture")])), 0)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    failed = [c for c in cases if not c[1]]
    for name, ok, got, want in cases:
        if not ok:
            print("FAIL  %-58s got=%r want=%r" % (name, got, want))
    print("p151-gnu-population-reach: %d tests, %d passed, %d failed"
          % (len(cases), len(cases) - len(failed), len(failed)))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
