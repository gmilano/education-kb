#!/usr/bin/env python3
"""Group `payload_digest.sh` output by digest. SHARED = one payload at two addresses."""
import collections
import sys


def group(rows):
    by = collections.defaultdict(list)
    for r in rows:
        if r.get("state") != "OK":
            continue
        by[r["sha256_16"]].append(r)
    shared, unique = {}, 0
    for d, rs in by.items():
        if len({r["slug"] for r in rs}) > 1:
            shared[d] = rs
        else:
            unique += 1
    return shared, unique


def read(path):
    with open(path, encoding="utf-8") as fh:
        head = fh.readline().rstrip("\n").split("\t")
        return [dict(zip(head, l.rstrip("\n").split("\t"))) for l in fh if l.strip()]


def main(argv):
    # P541: refuse an empty argument list — `total 0` with no input is not a clean tree.
    if not argv:
        sys.stderr.write("p349-payload-digest: no result file given — refusing (P541)\n")
        return 2
    rows = []
    for p in argv:
        rows += read(p)
    shared, unique = group(rows)
    print("digest\tslugs\tpath_per_slug\tbytes")
    for d, rs in sorted(shared.items()):
        print("%s\t%s\t%s\t%s" % (d, ",".join(sorted({r["slug"] for r in rs})),
                                  ";".join("%s:%s" % (r["slug"], r["path"]) for r in rs),
                                  rs[0]["bytes"]))
    print("#\tshared_digests\t%d" % len(shared))
    print("#\tunique_digests\t%d" % unique)
    print("#\tnot_ok_rows\t%d" % sum(1 for r in rows if r.get("state") != "OK"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
