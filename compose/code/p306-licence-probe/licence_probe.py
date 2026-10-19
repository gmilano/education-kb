#!/usr/bin/env python3
"""p306 licence prober — reads licence files from raw.githubusercontent.com as PAYLOADS.

Implements p305's permission-clause rule (the replacement for p304's refuted
`bytes < 400` length rule) and records byte length + sha256_12 for every payload,
which is this base's standing evidence format.

Usage: licence_probe.py slugs.txt out.tsv
"""
import hashlib
import subprocess
import sys

BRANCHES = ["main", "master", "dev", "develop", "development"]
NAMES = ["LICENSE", "LICENSE.md", "LICENSE.txt", "license.txt", "LICENCE", "COPYING"]

# p305's rule: the OPERATIVE GRANT SENTENCE is the discriminator, not length.
GRANT_CLAUSES = [
    "permission is hereby granted",          # MIT / ISC
    "hereby grants to you a perpetual",      # Apache-2.0
    "hereby grants you a",                   # variants
    "permission to use, copy, modify",       # BSD-ish
    "redistribution and use in source and binary",  # BSD
    "everyone is permitted to copy and distribute",  # GPL family
    "has waived all copyright",              # CC0
    "grants you a worldwide, royalty-free",  # CC family
]
RESERVED_MARKERS = ["all rights reserved"]


def fetch(slug, branch, name):
    url = f"https://raw.githubusercontent.com/{slug}/{branch}/{name}"
    r = subprocess.run(
        ["curl", "-sS", "-m", "25", "-w", "\n%{http_code}", url],
        capture_output=True, text=False,
    )
    if r.returncode != 0:
        return None, None
    body = r.stdout
    nl = body.rfind(b"\n")
    code = body[nl + 1:].decode("ascii", "replace").strip()
    return code, body[:nl]


def classify(text):
    """p305 clause rule. Returns (verdict, family)."""
    low = text.lower()
    has_grant = any(c in low for c in GRANT_CLAUSES)
    reserved = any(m in low for m in RESERVED_MARKERS)
    if not has_grant:
        return ("RESERVED-NO-GRANT" if reserved else "NO-GRANT-CLAUSE"), "-"
    fam = "unknown"
    if "apache license" in low:
        fam = "Apache-2.0"
    elif "mit license" in low or "permission is hereby granted, free of charge" in low:
        fam = "MIT"
    elif "affero" in low:
        fam = "AGPL-3.0"
    elif "lesser general public" in low:
        fam = "LGPL"
    elif "gnu general public" in low:
        fam = "GPL"
    elif "cc0" in low or "public domain dedication" in low:
        fam = "CC0-1.0"
    elif "attribution-sharealike" in low:
        fam = "CC-BY-SA-4.0"
    elif "creative commons" in low:
        fam = "CC-other"
    elif "redistribution and use in source and binary" in low:
        fam = "BSD"
    elif "isc license" in low:
        fam = "ISC"
    # a grant clause AND a reserved marker = read the body by hand
    if reserved and fam in ("unknown", "MIT"):
        fam += "?CHECK-RESERVED"
    return "GRANT", fam


def main():
    slugs = [l.strip() for l in open(sys.argv[1]) if l.strip() and not l.startswith("#")]
    out = open(sys.argv[2], "w")
    out.write("slug\tbranch\tfile\thttp\tbytes\tsha256_12\tverdict\tfamily\n")
    for slug in slugs:
        found = False
        for branch in BRANCHES:
            if found:
                break
            for name in NAMES:
                code, body = fetch(slug, branch, name)
                if code == "200" and body:
                    text = body.decode("utf-8", "replace")
                    verdict, fam = classify(text)
                    sha = hashlib.sha256(body).hexdigest()[:12]
                    row = f"{slug}\t{branch}\t{name}\t200\t{len(body)}\t{sha}\t{verdict}\t{fam}"
                    print(row, flush=True)
                    out.write(row + "\n")
                    found = True
                    break
        if not found:
            row = f"{slug}\t-\t-\t404\t-\t-\tNO_PAYLOAD\t-"
            print(row, flush=True)
            out.write(row + "\n")
    out.close()


if __name__ == "__main__":
    main()
