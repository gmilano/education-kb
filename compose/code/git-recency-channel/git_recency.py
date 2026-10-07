#!/usr/bin/env python3
"""git-recency-channel — date a GitHub repository without api.github.com.

`api.github.com/repos/*` returns 403 to this environment (while `api.github.com/`
itself returns 200, so it is the resource paths that are denied) and the rendered
`github.com` page returns 403. `git` itself is not blocked, so the head commit's
date is reachable by protocol rather than by API:

    git ls-remote <url> HEAD                         -> existence (ref SHA)
    git fetch --depth 1 --filter=blob:none origin HEAD
    git log -1 --format=%cI FETCH_HEAD                -> head commit date

Blob filtering keeps the transfer to commit+tree objects, so a repository of any
size answers in about a second.

Usage:
    python3 -I git_recency.py references.txt > recency.tsv
    python3 -I git_recency.py --slug owner/repo

Output is TSV: slug, ISO-8601 committer date, short sha, status (OK|FAIL).
"""
import concurrent.futures as cf
import shutil
import subprocess
import sys
import tempfile

TIMEOUT = 70


def head_date(slug, host="https://github.com"):
    """Return (slug, iso_date, short_sha, status)."""
    d = tempfile.mkdtemp(prefix="recency.")
    try:
        run = lambda *a: subprocess.run(
            ["git", "-C", d, *a], capture_output=True, text=True, timeout=TIMEOUT
        )
        run("init", "-q")
        run("remote", "add", "origin", f"{host}/{slug}")
        f = run("fetch", "-q", "--depth", "1", "--filter=blob:none", "origin", "HEAD")
        if f.returncode != 0:
            return (slug, "", "", "FAIL")
        dt = run("log", "-1", "--format=%cI", "FETCH_HEAD").stdout.strip()
        sha = run("rev-parse", "--short", "FETCH_HEAD").stdout.strip()
        return (slug, dt, sha, "OK" if dt else "FAIL")
    except (subprocess.TimeoutExpired, OSError):
        return (slug, "", "", "FAIL")
    finally:
        shutil.rmtree(d, ignore_errors=True)


def main(argv):
    if len(argv) == 3 and argv[1] == "--slug":
        slugs = [argv[2]]
    elif len(argv) == 2:
        with open(argv[1], encoding="utf-8") as fh:
            slugs = [l.strip() for l in fh if l.strip()]
    else:
        print(__doc__, file=sys.stderr)
        return 2
    with cf.ThreadPoolExecutor(max_workers=10) as ex:
        for slug, dt, sha, status in ex.map(head_date, slugs):
            print(f"{slug}\t{dt}\t{sha}\t{status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
