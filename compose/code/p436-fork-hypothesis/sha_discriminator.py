#!/usr/bin/env python3
"""p436 — the head SHA is what separates a RENAME from a FORK, and it costs one call.

`resolve_homepage.py` returns UPSTREAM whenever the registry names a slug other
than the one this KB cites.  Measured on 2026-10-07, that class mixes four
different things, and three of them are not lineage:

    rename / transfer   github.com redirects the old path; ONE repository, two names
    fork / mirror       two repositories, one derived from the other
    name collision      the manifest's `name` is a common word already on the registry
    vendoring           the manifest was copied in with the vendored code

The discriminator for the first is exact and needs no API:

    git ls-remote <old> HEAD  ==  git ls-remote <new> HEAD   ->  SAME REPOSITORY

A redirect serves the identical ref.  A fork diverges on its first commit, and
even an untouched fork of a moving upstream falls behind within a day.

Reads the UPSTREAM rows of a `resolve_homepage.py` TSV on stdin or from argv[1].
TSV out: cited, declared, cited_sha, declared_sha, verdict
"""
import subprocess, sys
from concurrent.futures import ThreadPoolExecutor


def head_sha(slug):
    try:
        r = subprocess.run(["git", "ls-remote", f"https://github.com/{slug}", "HEAD"],
                           capture_output=True, text=True, timeout=70)
        return r.stdout.split("\t")[0].strip() if r.returncode == 0 and r.stdout else ""
    except (subprocess.TimeoutExpired, OSError):
        return ""


def one(pair):
    a, b = pair
    sa, sb = head_sha(a), head_sha(b)
    if not sa or not sb:
        v = "UNRESOLVED"
    elif sa == sb:
        v = "SAME-REPOSITORY"
    else:
        v = "DISTINCT-REPOSITORIES"
    return (a, b, sa[:7] or "-", sb[:7] or "-", v)


def main():
    src = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
    pairs = []
    for line in src:
        p = line.rstrip("\n").split("\t")
        if len(p) >= 5 and p[3] == "UPSTREAM":
            pairs.append((p[0], p[4]))
    with ThreadPoolExecutor(max_workers=8) as ex:
        for r in ex.map(one, pairs):
            print("\t".join(r))


if __name__ == "__main__":
    main()
