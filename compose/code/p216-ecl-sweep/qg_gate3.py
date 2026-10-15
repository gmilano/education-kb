#!/usr/bin/env python3
"""p216 — the QG gate, with its SCOPE as the variable under test.

Two jobs in one instrument, because they share a reader:

  (1) ACTION QI's error measurement — what do the shelves publish for the 8 Apereo-family
      repositories whose licence blob reads `Educational Community License, Version 2.0`?
  (2) ACTION QG's placement step — p215's gate
      (`p215-lstree-grant-recovery/qg_gate2.py`) declares its own file list:

        CURRENT_STATE = agents/top.md, repos/foundations.md, verticals/solutions.md,
                        intel/market.md, compose/patterns.md, intel/trends.md
        APPEND_ONLY   = agents/trending.md, repos/trending.md

      That is 8 files. This KB publishes current-state grant claims in TEN: `intel/open-gaps.md`
      and `README.md` carry them too. If stale cells for p215's OWN 25 recoveries survive in the
      two unswept files, then QG's 23/7 result measured its scope, and wiring the same gate into
      `make hooks` unchanged would inherit the blind spot.

Run from the KB root.
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))          # compose/code/p216-ecl-sweep
KB = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))  # the KB root

SWEPT_BY_P215 = ["agents/top.md", "repos/foundations.md", "verticals/solutions.md",
                 "intel/market.md", "compose/patterns.md", "intel/trends.md"]
APPEND_ONLY = ["agents/trending.md", "repos/trending.md"]
NOT_SWEPT_BY_P215 = ["intel/open-gaps.md", "README.md"]

GRANT = re.compile(r"(MIT|Apache-2\.0|AGPL-3\.0|GPL-3\.0|GPL-2\.0|LGPL-3\.0|LGPL-2\.1|"
                   r"ECL-2\.0|BSD-[23]-Clause|MPL-2\.0|ISC|Unlicense)", re.I)
ABSENCE = re.compile(r"(sin licencia|no licence|no license|\bABSENT\b|ungranted|"
                     r"NONE\b|none found|sin archivo|NO grant|without a grant|"
                     r"no public grant|absent `?LICENSE|NOASSERTION)", re.I)


def read_truth(path):
    truth = {}
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) >= 2 and "/" in parts[0]:        # skip the column header row
                truth[parts[0]] = parts[1]
    return truth


def cells(truth, files):
    out = []
    for rel in files:
        p = os.path.join(KB, rel)
        if not os.path.exists(p):
            sys.stderr.write(f"missing {rel}\n")
            continue
        with open(p, encoding="utf-8", errors="replace") as fh:
            for i, line in enumerate(fh, 1):
                low = line.lower()
                for slug in truth:
                    if slug.lower() not in low:
                        continue
                    g = sorted({m.group(0).upper() for m in GRANT.finditer(line)})
                    a = sorted({m.group(0) for m in ABSENCE.finditer(line)})
                    if not g and not a:
                        continue                        # a mention, not a grant cell
                    fam = truth[slug].split()[0].upper()
                    verdict = "RIGHT" if fam in g else ("WRONG-ABSENCE" if a else "WRONG-FAMILY")
                    out.append((rel, i, slug, truth[slug], verdict, g, a, line.strip()[:300]))
    return out


def report(label, truth, files):
    rows = cells(truth, files)
    tally = {}
    for r in rows:
        tally[r[4]] = tally.get(r[4], 0) + 1
    print(f"\n### {label}")
    print(f"files: {len(files)}   repos: {len(truth)}   grant-claim lines: {len(rows)}")
    print(f"tally: {tally}")
    print("file\tline\tslug\ttruth\tverdict\ttokens\tabsence\ttext")
    for rel, i, slug, t, v, g, a, text in rows:
        if v != "RIGHT":
            print(f"{rel}\t{i}\t{slug}\t{t}\t{v}\t{','.join(g)}\t{','.join(a)}\t{text}")
    return rows


def main():
    ecl = read_truth(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ecl_truth.tsv"))
    p215 = read_truth(os.path.join(os.path.dirname(os.path.abspath(__file__)), "p215_truth.tsv"))

    print("=" * 78)
    print("JOB 1 — ACTION QI: what the shelves publish for the 8 ECL-2.0 repositories")
    print("=" * 78)
    report("ECL truth, over ALL TEN files", ecl,
           SWEPT_BY_P215 + APPEND_ONLY + NOT_SWEPT_BY_P215)

    print()
    print("=" * 78)
    print("JOB 2 — ACTION QG placement: is p215's 8-file gate scope sufficient?")
    print("=" * 78)
    a = report("p215's 25 recoveries, in the 8 files p215 SWEPT", p215,
               SWEPT_BY_P215 + APPEND_ONLY)
    b = report("p215's 25 recoveries, in the 2 files p215 did NOT sweep", p215,
               NOT_SWEPT_BY_P215)
    wrong_b = [r for r in b if r[4] != "RIGHT"]
    print(f"\n>>> stale/contradicting cells OUTSIDE p215's gate scope: {len(wrong_b)}")
    print(f">>> (inside its scope, after p215's own corrections: "
          f"{len([r for r in a if r[4] != 'RIGHT'])})")


if __name__ == "__main__":
    main()
