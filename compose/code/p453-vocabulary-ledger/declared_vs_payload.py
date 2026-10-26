#!/usr/bin/env python3
"""p453 -- Gap 453-A: does the registry's declared LICENCE VALUE match the
first-hand payload at HEAD?

p452's back-link sweep graded whether a registry record points at the right
ADDRESS (63/71 AGREE, 0 DISAGREE). It never graded the licence VALUE. These are
different questions: a record can back-link the correct repository and still
declare a different licence than the repository serves.
"""
import csv, hashlib, re, subprocess, sys, concurrent.futures as cf
sys.path.insert(0, "/tmp/education-kb/compose/code/p453-vocabulary-ledger")
from verify import family, fetch

LEDGER = "/tmp/education-kb/evidence/vocabulary-spend-ledger.2026-10-26-p453.tsv"
OUT = "/tmp/education-kb/evidence/declared-vs-payload.2026-10-26-p453.tsv"
PATHS = ["LICENSE", "LICENSE.md", "LICENSE.txt", "LICENCE", "COPYING",
         "license", "LICENSE-MIT", "MIT-LICENSE", "LICENSE.rst"]

# SPDX-ish normalisation so "Apache License 2.0" and "Apache-2.0" are one value,
# and so GPL-3.0-only / GPL-3.0-or-later collapse onto the family the payload
# title can actually attest.
def canon(s):
    if not s:
        return ""
    t = s.strip().strip('"').upper().replace("_", "-")
    t = re.sub(r"\s+", " ", t)
    t = re.sub(r"^THE ", "", t)
    if "APACHE" in t:
        return "APACHE-2.0"
    if "AGPL" in t or "AFFERO" in t:
        return "AGPL-3.0"
    if "LGPL" in t or "LESSER" in t:
        return "LGPL"
    if t.startswith("GPL") or "GENERAL PUBLIC" in t:
        return "GPL"
    if t.startswith("MIT"):
        return "MIT"
    if "BSD-3" in t or "BSD 3" in t:
        return "BSD-3-CLAUSE"
    if "BSD-2" in t or "BSD 2" in t:
        return "BSD-2-CLAUSE"
    if t.startswith("BSD"):
        return "BSD"
    if t.startswith("ISC"):
        return "ISC"
    if "MPL" in t or "MOZILLA" in t:
        return "MPL-2.0"
    if "CC0" in t:
        return "CC0-1.0"
    if t.startswith("CC-BY") or "CREATIVE COMMONS" in t:
        return "CC-BY"
    if "UNLICENSE" in t:
        return "UNLICENSE"
    if "SEE LICENSE IN" in t:
        return "POINTER-OUT-OF-REGISTRY"
    return t


def payload_of(slug):
    for p in PATHS:
        body, code, size = fetch(f"https://raw.githubusercontent.com/{slug}/HEAD/{p}")
        if code == "200" and body:
            return p, family(body), size, hashlib.sha256(body.encode()).hexdigest()[:12]
    return "", "NO_PAYLOAD", 0, ""


def grade(row):
    leg, term, verdict, pkg, addr, reach, lic = row[0], row[1], row[2], row[3], row[4], row[5], row[6]
    slug = "/".join(addr.split("/")[1:])
    path, fam, size, sha = payload_of(slug)
    d, p = canon(lic), canon(fam)
    if fam == "NO_PAYLOAD":
        v = "MANIFEST_ONLY" if d and d != "POINTER-OUT-OF-REGISTRY" else "NO_GRANT_ANYWHERE"
    elif not d:
        v = "REGISTRY_SILENT"
    elif d == "POINTER-OUT-OF-REGISTRY":
        v = "POINTER"
    elif fam == "UNREAD":
        v = "PAYLOAD_UNREAD"
    elif d == p:
        v = "AGREE"
    else:
        v = "DISAGREE"
    return [addr, pkg, lic, fam, path, str(size), sha, v, leg]


def main():
    rows = []
    with open(LEDGER) as f:
        for r in csv.reader(f, delimiter="\t"):
            if r and r[2] == "CANDIDATE" and r[5] == "LIVE":
                rows.append(r)
    print(f"population: {len(rows)} live candidates", file=sys.stderr)
    out = []
    with cf.ThreadPoolExecutor(max_workers=8) as ex:
        for i, res in enumerate(ex.map(grade, rows), 1):
            out.append(res)
            if i % 40 == 0:
                print(f"  {i}/{len(rows)}", file=sys.stderr)
    with open(OUT, "w") as f:
        f.write("address\tpackage\tdeclared_npm\tpayload_family\tpayload_path\t"
                "payload_bytes\tsha256_12\tverdict\tleg\n")
        for r in out:
            f.write("\t".join(r) + "\n")
    from collections import Counter
    c = Counter(r[7] for r in out)
    print("\n=== verdicts ===")
    for k, n in c.most_common():
        print(f"  {k:22s} {n:4d}  {100*n/len(out):5.1f}%")
    print("\n=== every DISAGREE, in full ===")
    for r in out:
        if r[7] == "DISAGREE":
            print(f"  {r[0]:50s} npm={r[2]:10s} payload={r[3]:14s} {r[5]:>7s} B  {r[6]}")
    print("\n=== MANIFEST_ONLY (declared grant, no payload at 9 paths) ===")
    for r in out:
        if r[7] == "MANIFEST_ONLY":
            print(f"  {r[0]:50s} npm={r[2]}")
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    main()
