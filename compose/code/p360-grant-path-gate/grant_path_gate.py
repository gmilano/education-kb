#!/usr/bin/env python3
"""p360 grant-path currency gate, second revision.

Revision 1 accused 5 cells and ALL 5 WERE CORRECT. Two causes, both in the
instrument:
  (a) a grant path can be `branch/DIR/FILE` -- ACTION ZZ-u's grant-at-depth --
      so splitting on the first slash invents a wrong branch;
  (b) a slug can contain a dot (`dmitry-viskov/pylti1.3`), and trailing-dot
      stripping truncated it into a dead address.
This revision resolves the cell against the LIVE default branch instead of
assuming the first segment is a branch.
"""
import concurrent.futures as cf
import re
import subprocess
import sys

LINK = re.compile(r"github\.com/([A-Za-z0-9_.-]{1,39}/[A-Za-z0-9_.-]{1,100})")
POSITIVE = re.compile(r"\b(MIT|Apache-2\.0|AGPL-3\.0|GPL-3\.0|GPL-2\.0|LGPL-3\.0|LGPL-2\.1|BSD-3-Clause|BSD-2-Clause|MPL-2\.0|ECL-2\.0|ISC|Unlicense|ODbL-1\.0|CC-BY)\b")
ABSENCE = re.compile(r"no grant|none found|there is no|no `LICEN|404s|nothing at any probed path|declared only in|not found at any|no tree|All rights reserved|unlicensed|carry no grant|grant-unresolved", re.I)
CELL = re.compile(r"`([A-Za-z0-9_.\-]+(?:/[A-Za-z0-9_.\-]+)*/(?:LICEN[SC]E|COPYING)[A-Za-z.\-]*)`")


def ls(slug):
    try:
        p = subprocess.run(["git", "ls-remote", "--symref",
                            f"https://github.com/{slug}", "HEAD"],
                           capture_output=True, text=True, timeout=40)
    except subprocess.TimeoutExpired:
        return None
    for line in p.stdout.splitlines():
        if line.startswith("ref:"):
            return line.split()[1].replace("refs/heads/", "")
    return None


def code(url):
    try:
        p = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}",
                            "--max-time", "25", url], capture_output=True,
                           text=True, timeout=35)
        return p.stdout.strip()
    except subprocess.TimeoutExpired:
        return "timeout"


def rows(files):
    seen, out = set(), []
    for fn in files:
        for ln, line in enumerate(open(fn, encoding="utf-8"), 1):
            if not line.lstrip().startswith("|"):
                continue
            c, l = CELL.search(line), LINK.search(line)
            if not (c and l):
                continue
            if not POSITIVE.search(line):   # ACTION ZZ-bk, right way round
                continue
            if ABSENCE.search(line):
                continue
            slug = l.group(1).rstrip(".")
            # a slug ending in a stripped dot-segment: keep the full match if the
            # trailing segment is numeric (pylti1.3), the ZZ-u/dot defect
            full = l.group(1)
            if re.search(r"\.\d+$", full):
                slug = full
            k = (slug, c.group(1))
            if k not in seen:
                seen.add(k)
                out.append((fn, ln, slug, c.group(1)))
    return out


def check(r):
    fn, ln, slug, cell = r
    live = ls(slug)
    if live is None:
        return (slug, cell, "DEAD", "-", fn, ln)
    # resolve: is the first segment the branch, or is the whole cell a path?
    parts = cell.split("/")
    cands = []
    if len(parts) > 1:
        cands.append((parts[0], "/".join(parts[1:])))
    cands.append((live, cell))
    for br, path in cands:
        if br != live:
            continue
        if code(f"https://raw.githubusercontent.com/{slug}/{br}/{path}") == "200":
            return (slug, cell, "OK", br, fn, ln)
    # cell names a branch that is not the live default
    if len(parts) > 1 and parts[0] != live:
        if code(f"https://raw.githubusercontent.com/{slug}/{live}/{'/'.join(parts[1:])}") == "200":
            return (slug, cell, f"BRANCH-STALE(live={live})", parts[0], fn, ln)
    return (slug, cell, "PATH-FAIL", live, fn, ln)


rs = rows(sys.argv[1:])
bad = []
with cf.ThreadPoolExecutor(max_workers=12) as ex:
    for r in ex.map(check, rs):
        if r[2] != "OK":
            bad.append(r)
            print("FAIL\t" + "\t".join(str(x) for x in r))
print(f"\nchecked={len(rs)} agree={len(rs)-len(bad)} fail={len(bad)}")
sys.exit(1 if bad else 0)
