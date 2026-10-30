#!/usr/bin/env python3
"""delivery-fitness.py -- grade a licence against GLOBANT'S DELIVERY MODEL (p556).

WHY THIS EXISTS, AND WHY IT IS NOT ANOTHER LICENCE CLASSIFIER
  This base already reads licences well: `grant-verdict.py` says WHAT a grant is,
  and `platform-channel.py` says whether four channels agree about it.  Neither
  answers the question a studio actually asks, which is not "what licence is
  this" but "can we put it in a client deliverable".  p552 found the sharpest
  case -- `Oriole-FDU/Wisepen`, BUSL-1.1, whose excluded-use clause names
  "consulting deliverable" in so many words -- and p556 found that the
  fastest-growing education agent on the whole shelf (`amosblomqvist/learnharness`,
  4 231 stars at fourteen days old) is AGPL-3.0.  Both are discoveries about
  DELIVERY, and in both cases the licence field alone reads as "open source" and
  tells a proposal-writer nothing.

  So this maps an SPDX id to one of five delivery verdicts.  It is deliberately
  coarse: the point is to put the right question in front of a human early, not
  to replace counsel.

  BUILD-ON        permissive.  May be modified and shipped inside a closed
                  deliverable.  Attribution and (Apache-2.0) NOTICE still apply.
  LINK-ONLY       weak copyleft (LGPL/MPL/EPL).  The library may be linked, but
                  modifications to the library itself come back out.
  SELF-HOST-ONLY  strong or network copyleft (GPL/AGPL).  Deployable for a client
                  who runs it themselves; NOT foldable into a proprietary product,
                  and AGPL s.13 reaches users over a network, which is what most
                  education pilots are.
  BLOCK           no grant at all, an unclassifiable grant (`NOASSERTION`), a
                  non-commercial clause, or a source-available licence with a
                  competing-use carve-out.  Never enters a proposal unshelled.
  ASK             a real licence this table does not yet know.  Not a pass.

  `NOASSERTION` is BLOCK, not ASK, and that is the load-bearing choice.  It means
  GitHub found a licence file and could not classify it -- a bespoke grant.  p556
  measures six of those on the live shelf, including three repositories in the
  top twenty by stars.  A bespoke grant is MORE dangerous than a missing one,
  because the sidebar still renders a licence and a reader stops looking.

OFFLINE BY CONSTRUCTION
  Reads a harvest TSV; makes no network call.  p550's lesson is that the
  instruments which survive the gate denials are the ones that need no network.

USAGE
  python3 -I ingest/delivery-fitness.py evidence/platform-harvest.2026-10-30-p556.tsv
  python3 -I ingest/delivery-fitness.py HARVEST.tsv --tsv > out.tsv
  python3 -I ingest/delivery-fitness.py HARVEST.tsv --max-verdict BUILD-ON
      exit 1 if any row grades worse than BUILD-ON -- the gate form.
"""
import sys

BUILD_ON = {
    "MIT", "MIT-0", "Apache-2.0", "BSD-3-Clause", "BSD-2-Clause", "BSD-1-Clause",
    "ISC", "Unlicense", "CC0-1.0", "0BSD", "Zlib", "PostgreSQL", "MS-PL",
    "ECL-2.0", "AFL-3.0", "Artistic-2.0", "BSL-1.0", "NCSA", "Python-2.0",
    "CC-BY-4.0", "CC-BY-3.0",
}
LINK_ONLY = {
    "LGPL-2.1", "LGPL-3.0", "LGPL-2.0", "MPL-2.0", "MPL-1.1", "EPL-1.0",
    "EPL-2.0", "CDDL-1.0", "OSL-3.0",
}
SELF_HOST_ONLY = {
    "GPL-2.0", "GPL-3.0", "AGPL-3.0", "SSPL-1.0", "EUPL-1.2", "EUPL-1.1",
    "CC-BY-SA-4.0", "CC-BY-SA-3.0", "GFDL-1.3",
}
# Everything here renders as a licence and is NOT deliverable.
BLOCKED = {
    "NOASSERTION": "bespoke grant GitHub could not classify -- read the file by hand",
    "NONE": "no grant at all: default copyright, all rights reserved",
    "": "no grant at all: default copyright, all rights reserved",
    "BUSL-1.1": "source-available with a competing-use carve-out (p552: names 'consulting deliverable')",
    "Elastic-2.0": "source-available: no managed-service or hosted resale",
    "SSPL-1.0-only": "source-available: service-source obligation",
    "CC-BY-NC-4.0": "NonCommercial: excludes paid delivery outright",
    "CC-BY-NC-SA-4.0": "NonCommercial + ShareAlike: excludes paid delivery outright",
    "CC-BY-NC-ND-4.0": "NonCommercial + NoDerivatives: excludes paid delivery outright",
    "SUL-1.0": "Sustainable Use Licence: internal use only, not OSI-approved",
}
RANK = {"BUILD-ON": 0, "LINK-ONLY": 1, "SELF-HOST-ONLY": 2, "ASK": 3, "BLOCK": 4}

NOTE = {
    "BUILD-ON": "may ship inside a closed deliverable; keep attribution/NOTICE",
    "LINK-ONLY": "link only; changes to the library itself must be published",
    "SELF-HOST-ONLY": "client-hosted only; the whole derivative work is published",
    "ASK": "licence not in this table -- read it before it reaches a proposal",
}
# The network-copyleft arm is NOT the same obligation as plain GPL, and p556's own
# first run printed the AGPL s.13 reason over the five plain-GPL rows.  Hosting a GPL work
# for a client triggers nothing extra; hosting an AGPL work triggers s.13, which
# is the clause a hosted education pilot actually meets.  Keeping them in one
# verdict with one reason string loses exactly the distinction the verdict is for.
NETWORK_COPYLEFT = {"AGPL-3.0", "SSPL-1.0", "EUPL-1.2", "EUPL-1.1"}
NETWORK_NOTE = ("client-hosted only; network copyleft (AGPL s.13 / equivalent) "
                "reaches users served over a network, which is what a hosted pilot is")


def grade(spdx):
    key = (spdx or "").strip()
    norm = key.upper() if key.upper() in ("NOASSERTION", "NONE", "") else key
    if norm in BLOCKED:
        return "BLOCK", BLOCKED[norm]
    if key in BUILD_ON:
        return "BUILD-ON", NOTE["BUILD-ON"]
    if key in LINK_ONLY:
        return "LINK-ONLY", NOTE["LINK-ONLY"]
    if key in SELF_HOST_ONLY:
        if key in NETWORK_COPYLEFT:
            return "SELF-HOST-ONLY", NETWORK_NOTE
        return "SELF-HOST-ONLY", NOTE["SELF-HOST-ONLY"]
    return "ASK", NOTE["ASK"]


def read_harvest(path):
    rows = []
    with open(path, encoding="utf-8") as fh:
        header = None
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            cells = line.rstrip("\n").split("\t")
            if header is None:
                header = cells
                continue
            rows.append(dict(zip(header, cells)))
    return rows


def main(argv):
    if len(argv) < 2:
        print(__doc__.strip().splitlines()[-4].strip(), file=sys.stderr)
        return 2
    path = argv[1]
    as_tsv = "--tsv" in argv
    ceiling = None
    if "--max-verdict" in argv:
        ceiling = argv[argv.index("--max-verdict") + 1]

    rows = read_harvest(path)
    out, tally = [], {}
    for r in rows:
        verdict, why = grade(r.get("spdx_id"))
        tally[verdict] = tally.get(verdict, 0) + 1
        out.append((r.get("slug", "?"), r.get("stars", "-"), r.get("spdx_id", "-"),
                    verdict, why))

    if as_tsv:
        print("slug\tstars\tspdx_id\tverdict\twhy")
        for row in out:
            print("\t".join(str(c) for c in row))
    else:
        width = max(len(r[0]) for r in out) if out else 10
        for slug, stars, spdx, verdict, why in sorted(
                out, key=lambda r: (-RANK[r[3]], -int(r[1]) if str(r[1]).isdigit() else 0)):
            print(f"{slug:<{width}}  {str(stars):>6}  {spdx:<14}  {verdict:<15}  {why}")
        print()
        print(f"{len(out)} row(s) graded from {path}")
        for v in sorted(tally, key=lambda k: RANK[k]):
            pct = 100.0 * tally[v] / len(out)
            print(f"  {v:<15} {tally[v]:>3}   {pct:5.1f} %")

    if ceiling:
        worst = max((RANK[r[3]] for r in out), default=0)
        if worst > RANK.get(ceiling, 4):
            over = [r[0] for r in out if RANK[r[3]] > RANK[ceiling]]
            print(f"\nFAIL: {len(over)} row(s) worse than {ceiling}: "
                  f"{', '.join(over[:8])}{' …' if len(over) > 8 else ''}",
                  file=sys.stderr)
            return 1
        print(f"\nOK: every row grades {ceiling} or better.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
