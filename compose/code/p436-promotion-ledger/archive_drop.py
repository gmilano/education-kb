#!/usr/bin/env python3
"""p436 — Gap 435-B leg 1: measure silently-dropped rows across archive/ snapshots.

A slug present in an archived snapshot of a shelf and absent from the LIVE
counterpart of that shelf is a candidate drop.  A candidate that is absent from
the ENTIRE live corpus is a confirmed drop; one that is present elsewhere was
MOVED, which is not a defect.
"""
import os
import re
import sys

SLUG = re.compile(r"github\.com/([A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?)/([A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?)")
# archived basename -> live path
MAP = {
    "agents-top.md": "agents/top.md",
    "agents-trending.md": "agents/trending.md",
    "repos-foundations.md": "repos/foundations.md",
    "repos-trending.md": "repos/trending.md",
    "verticals-solutions.md": "verticals/solutions.md",
    "intel-market.md": "intel/market.md",
    "intel-trends.md": "intel/trends.md",
    "compose-patterns.md": "compose/patterns.md",
}
LIVE_CORPUS = sorted(set(MAP.values()))


def slugs(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    out = {}
    for owner, repo in SLUG.findall(text):
        repo = repo.rstrip(".")
        if repo.endswith(".git"):
            repo = repo[:-4]
        out.setdefault("%s/%s" % (owner, repo), 0)
        out["%s/%s" % (owner, repo)] += 1
    return out


def main(argv):
    if len(argv) != 1:
        sys.stderr.write(
            "usage: archive_drop.py REPO_ROOT\n"
            "  REPO_ROOT is the education-kb checkout to measure.\n")
        return 2
    root = argv[0]
    if not os.path.isdir(os.path.join(root, "archive")):
        sys.stderr.write("archive_drop.py: no archive/ under %s\n" % root)
        return 2

    live = {}
    for rel in LIVE_CORPUS:
        p = os.path.join(root, rel)
        live[rel] = slugs(p) if os.path.exists(p) else {}
    live_any = set()
    for d in live.values():
        live_any |= set(d)

    rows = []
    snapshots = sorted(
        d for d in os.listdir(os.path.join(root, "archive"))
        if os.path.isdir(os.path.join(root, "archive", d)))
    read = 0
    for snap in snapshots:
        sdir = os.path.join(root, "archive", snap)
        for base in sorted(os.listdir(sdir)):
            rel = MAP.get(base)
            if rel is None:
                continue
            read += 1
            for slug in sorted(slugs(os.path.join(sdir, base))):
                if slug in live[rel]:
                    continue
                verdict = "MOVED" if slug in live_any else "DROPPED"
                where = ""
                if verdict == "MOVED":
                    where = ";".join(r for r in LIVE_CORPUS if slug in live[r])
                rows.append((snap, base, rel, slug, verdict, where))

    if not read:
        sys.stderr.write("archive_drop.py: 0 mapped files read under %s/archive\n" % root)
        return 2

    print("snapshot\tarchived_file\tlive_file\tslug\tverdict\tpresent_in")
    for r in rows:
        print("\t".join(r))
    dropped = sorted({r[3] for r in rows if r[4] == "DROPPED"})
    moved = sorted({r[3] for r in rows if r[4] == "MOVED"})
    sys.stderr.write(
        "read=%d mapped files over %d snapshots; rows=%d; "
        "distinct DROPPED=%d; distinct MOVED=%d\n"
        % (read, len(snapshots), len(rows), len(dropped), len(moved)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
