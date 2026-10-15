"""Step 4 of `ACTION ST` — compare every live shelf cell against the grant read first-hand.

A "disagreement" is NOT one thing, and conflating the three classes is how p227's
hand-sweep could report `7` without knowing whether that was the population:

  FAMILY     the cell names a different licence family than the repository's grant.
             A DEFECT. Decidable from a root LICENSE, and the only class that can
             mislead an engagement about what it may ship.
  BOUND      same family, different bound (`-only` / `-or-later` / bare).
             NOT DECIDABLE from a root LICENSE at all - p225 and p227 both
             established that GPL-family or-later lives in a channel the canonical
             body does not contain. Reported, never "fixed".
  NOTATION   same family and bound, different spelling (`GPL-3` vs `GPL-3.0`).
             Harmless to a reader and FATAL to a machine filter, which is why it
             is counted rather than ignored.
"""
import csv
import sys

# cell token -> (family, bound)
NORM = {
    "MIT": ("MIT", ""), "ISC": ("ISC", ""), "Unlicense": ("Unlicense", ""),
    "Apache-2.0": ("Apache-2.0", ""), "Apache 2.0": ("Apache-2.0", ""),
    "BSD-3-Clause": ("BSD-3-Clause", ""), "BSD-2-Clause": ("BSD-2-Clause", ""),
    "MPL-2.0": ("MPL-2.0", ""), "EPL-2.0": ("EPL-2.0", ""), "EUPL-1.2": ("EUPL-1.2", ""),
    "ECL-2.0": ("ECL-2.0", ""),
    "CC-BY-SA-4.0": ("CC-BY-SA-4.0", ""), "CC-BY-4.0": ("CC-BY-4.0", ""), "CC0-1.0": ("CC0-1.0", ""),
    "AGPL-3.0": ("AGPL-3.0", ""), "AGPL-3": ("AGPL-3.0", ""), "AGPLv3": ("AGPL-3.0", ""),
    "AGPL-3.0-only": ("AGPL-3.0", "only"), "AGPL-3.0-or-later": ("AGPL-3.0", "or-later"),
    "GPL-3.0": ("GPL-3.0", ""), "GPL-3": ("GPL-3.0", ""), "GPLv3": ("GPL-3.0", ""),
    "GPL-3.0-only": ("GPL-3.0", "only"), "GPL-3.0-or-later": ("GPL-3.0", "or-later"),
    "GPL-2.0": ("GPL-2.0", ""), "GPL-2": ("GPL-2.0", ""), "GPLv2": ("GPL-2.0", ""),
    "LGPL-3.0": ("LGPL-3.0", ""), "LGPL-3": ("LGPL-3.0", ""),
    "LGPL-3.0-only": ("LGPL-3.0", "only"), "LGPL-3.0-or-later": ("LGPL-3.0", "or-later"),
    "LGPL-2.1": ("LGPL-2.1", ""),
}


def verdict(cell, read):
    """Return (verdict, cell_family, read_family)."""
    if read in ("NO-GRANT",):
        return ("CELL-WITHOUT-GRANT", NORM.get(cell, (cell, ""))[0], read)
    if read in ("UNRECOGNISED", "GPL-?", "LGPL-?") or not read:
        return ("UNDECIDABLE-BODY", NORM.get(cell, (cell, ""))[0], read)
    if " OR " in read:
        # A DUAL grant. A cell naming one option is not wrong, it is INCOMPLETE --
        # and which half it drops decides who pays: naming only the copyleft option
        # excludes a repo a studio could have taken permissively (`Elgg/Elgg`).
        opts = [o.strip() for o in read.split(" OR ")]
        cf0 = NORM.get(cell, (cell, ""))[0]
        if cf0 in opts:
            return ("INCOMPLETE-DUAL", cf0, read)
        return ("FAMILY", cf0, read)
    cf, cb = NORM.get(cell, (None, ""))
    if cf is None:
        return ("CELL-TOKEN-UNMAPPED", cell, read)
    if cf != read:
        return ("FAMILY", cf, read)
    if cb:
        return ("BOUND", cf, read)
    if cell != read:
        return ("NOTATION", cf, read)
    return ("AGREE", cf, read)


def main(argv):
    harvest, reads = argv[1], argv[2]
    fam = {}
    for r in csv.DictReader(open(reads, encoding="utf-8"), delimiter="\t"):
        fam[r["slug"]] = r
    out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    out.writerow(["verdict", "slug", "file", "line", "cell", "cell_family",
                  "read_family", "ref", "path", "bytes", "sha12", "note"])
    for r in csv.DictReader(open(harvest, encoding="utf-8"), delimiter="\t"):
        if r["status"] != "LIVE":
            continue
        g = fam.get(r["slug"])
        if not g:
            continue
        v, cf, rf = verdict(r["cell"], g["family"])
        out.writerow([v, r["slug"], r["file"].split("/")[-1], r["line"], r["cell"], cf, rf,
                      g["ref"], g["path"], g["bytes"], g["sha12"], g["note"]])


if __name__ == "__main__":
    main(sys.argv)
