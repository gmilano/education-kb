#!/usr/bin/env python3
"""p209 - rank the never-auditable (NO-MASKED) census rows by client-deliverable exposure.

p208 proved the p205-p208 licence comparator cannot fail on a row whose true grant family is
printed at more than one site: 152 of 179 rows (85%) are masked by construction. Discovery is
saturated (six readings), so the remaining value is in reading masked rows against their own
repositories. This picks the batch that matters most: exposure in compose/patterns.md, because
recipes are what a client engagement reads, and p208's one true positive lived there.

Offline. Reads the p208 census and the recipe shelf; writes nothing.

  python3 rank_masked.py --limit 10 --skip-verified
"""
import argparse
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
KB = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
CENSUS = os.path.join(KB, "evidence", "comparator-reach.2026-10-14-p208.tsv")
RECIPES = os.path.join(KB, "compose", "patterns.md")
VERIFIED = os.path.join(KB, "evidence", "masked-class-sample.2026-10-14-p209.tsv")


def read_census(path):
    """Masked rows only: the ones the comparator cannot see."""
    rows = []
    with open(path, encoding="utf-8") as fh:
        for rec in csv.DictReader(fh, delimiter="\t"):
            if rec.get("detectable", "").startswith("NO"):
                rows.append((rec["repo"], rec["truth"], int(rec["sites_with_truth"])))
    return rows


def read_done(path):
    """Repos already read first-hand, so a batch never re-spends on them."""
    done = set()
    if not os.path.exists(path):
        return done
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or line.startswith("repo\t"):
                continue
            parts = line.rstrip("\n").split("\t")
            if parts and parts[0]:
                done.add(parts[0])
    return done


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--skip-verified", action="store_true",
                    help="exclude repos already read first-hand in p209")
    args = ap.parse_args()

    for path in (CENSUS, RECIPES):
        if not os.path.exists(path):
            sys.exit("missing input: %s" % path)

    recipes = open(RECIPES, encoding="utf-8").read()
    done = read_done(VERIFIED) if args.skip_verified else set()

    ranked = []
    for repo, truth, sites in read_census(CENSUS):
        if repo in done:
            continue
        # count(repo) is the exposure that matters: how often a recipe names it.
        ranked.append((recipes.count(repo), sites, repo, truth))
    # Most recipe-exposed first; shelf sites breaks ties; name keeps it deterministic.
    ranked.sort(key=lambda r: (-r[0], -r[1], r[2]))

    print("recipe_sites\tshelf_sites\trepo\tshelf_says")
    for row in ranked[:args.limit]:
        print("%d\t%d\t%s\t%s" % row)

    unexposed = sum(1 for r in ranked if r[0] == 0)
    print("# masked rows pending: %d (of which %d appear in NO recipe)"
          % (len(ranked), unexposed), file=sys.stderr)


if __name__ == "__main__":
    main()
