#!/usr/bin/env python3
"""p779: extract every shelved repository slug whose row grades it Apache-2.0.

These are the sweep population for p778-B: T801 showed sakai and opencast were
graded Apache-2.0 when their bytes say ECL-2.0, so every Apache-2.0 row whose
grant lands in the 11.0-11.5 kB band is a suspect. Slug and grade must come from
the SAME table row, or a licence named anywhere on a line would attach to a
repository named anywhere else on it.
"""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gate_refs import SHELVES, is_data_row

SLUG = re.compile(r"github\.com/([A-Za-z0-9][\w.\-]*)/([\w.\-]+?)(?=[)\s`,:;\"'\]]|/|$)")
APACHE = re.compile(r"(?i)\bApache-2\.0\b")
BAD = {"","."}

def main(root):
    found = {}
    for sh in SHELVES:
        p = os.path.join(root, sh)
        if not os.path.exists(p): continue
        for i, line in enumerate(open(p, encoding="utf-8", errors="replace"), 1):
            if not is_data_row(line): continue
            if not APACHE.search(line): continue
            for o, r in SLUG.findall(line):
                r = r.rstrip(".")
                if r in BAD or o in BAD: continue
                if r.lower().endswith(".git"): r = r[:-4]
                found.setdefault(f"{o}/{r}", []).append(f"{sh}:{i}")
    for slug in sorted(found):
        print(f"{slug}\t{len(found[slug])}\t{found[slug][0]}")
    print(f"# unique slugs on Apache-2.0 rows: {len(found)}", file=sys.stderr)

main(sys.argv[1])
