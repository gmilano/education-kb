#!/usr/bin/env python3
"""p866 — discharge of `865-G4`: a sweep's candidate slugs, split THREE WAYS by one command.

WHY THIS EXISTS.  `865-G4` measured the same fact twice, two weeks apart, on
different veins: 76% of a sweep's candidates were already held (`p852`), then
77% (`p865`).  The rate is stable enough to be a planning constant.  What was
missing was not the measurement -- `compose/code/p853-slug-presence/presence.py`
already returns a per-slug verdict -- it was the AGGREGATION.  Every pass
re-derived the split by eye from a per-slug table, which is how the same number
got discovered twice instead of once and cited once.

WHAT IT IS NOT.  It is not a new presence check.  It imports `p853`'s scanner
unchanged, so the word-boundary semantics `852-G3`/`T174` fixed are inherited
rather than re-implemented -- `ingest/p587-crosspage-naive.py`'s docstring is
this base's standing warning about writing the fourth copy of an instrument it
already owns.

VERDICTS, straight from `p853`:
    SHELVED       on a curated shelf -- the base already SELLS this row
    UNGRADED      in the history only (README, trending, evidence) -- owned, unfiled
    FIXTURE-ONLY  named only inside compose/code/ -- an instrument's own fixture
    NEW           absent from the corpus

Usage:
    gh api ... --jq '.items[].full_name' | python3 -I ingest/p866-triage.py --root .
    python3 -I ingest/p866-triage.py --root . owner/repo owner/repo2
    ... --tsv evidence/candidate-triage.2026-11-17-p866.tsv
"""

import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# `python3 -I` strips the script's directory from sys.path (p355-cwd-portability,
# and the whole reason the Makefile `cd`s into every instrument).  p853 lives
# outside ingest/, so its directory is added explicitly and nothing else is.
sys.path.insert(0, os.path.join(HERE, "..", "compose", "code", "p853-slug-presence"))
import presence  # noqa: E402

ORDER = ["NEW", "UNGRADED", "SHELVED", "FIXTURE-ONLY"]


def normalise(raw: str) -> str:
    """Accept a URL, a bare slug, trailing .git, surrounding backticks."""
    s = raw.strip().strip("`,|").rstrip("/")
    if not s:
        return ""
    for pre in ("https://github.com/", "http://github.com/", "github.com/"):
        if s.lower().startswith(pre):
            s = s[len(pre):]
            break
    if s.endswith(".git"):
        s = s[:-4]
    parts = [p for p in s.split("/") if p]
    if len(parts) < 2:
        return ""
    return "/".join(parts[:2])


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="three-way split of sweep candidates (865-G4)")
    ap.add_argument("slugs", nargs="*", help="owner/repo or URL; omit to read stdin")
    ap.add_argument("--root", default=".", help="corpus root")
    ap.add_argument("--tsv", help="write the per-slug record here")
    ap.add_argument("--include-archive", action="store_true",
                    help="count archive/ as presence (default: live corpus only)")
    args = ap.parse_args(argv)

    raw = args.slugs if args.slugs else sys.stdin.read().split()
    slugs, dropped = [], []
    for item in raw:
        slug = normalise(item)
        if not slug:
            dropped.append(item)
        elif slug not in slugs:
            slugs.append(slug)
    if not slugs:
        print("🔴 no parseable owner/repo addresses on input", file=sys.stderr)
        return 2

    result = presence.scan(args.root, slugs, args.include_archive)
    buckets = {k: [] for k in ORDER}
    for slug in slugs:
        buckets[result[slug]["verdict"]].append(slug)

    n = len(slugs)
    held = n - len(buckets["NEW"]) - len(buckets["FIXTURE-ONLY"])
    print(f"candidates in       : {n}   (deduplicated from {len(raw)}; {len(dropped)} unparseable)")
    for k in ORDER:
        c = len(buckets[k])
        print(f"{k:<20}: {c:>3}   {100.0 * c / n:5.1f}%")
    print(f"{'HELD (SHELVED+UNGRADED)':<20}: {held:>3}   {100.0 * held / n:5.1f}%"
          f"   <- 865-G4's constant: p852 76%, p865 77%")
    print()
    for k in ORDER:
        if buckets[k]:
            print(f"{k}: " + " ".join(buckets[k]))
    if dropped:
        print("UNPARSEABLE: " + " ".join(dropped[:10]))

    if args.tsv:
        with open(args.tsv, "w", encoding="utf-8") as fh:
            fh.write("address\tverdict\tform\thits\twhere\n")
            for slug in slugs:
                rec = result[slug]
                where = ",".join(sorted({h[0] for h in rec["hits"]})[:4]) or "-"
                fh.write(f"{slug}\t{rec['verdict']}\t{rec['state']}\t{len(rec['hits'])}\t{where}\n")
        print(f"\nper-slug record -> {args.tsv}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
