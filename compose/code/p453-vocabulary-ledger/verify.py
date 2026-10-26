#!/usr/bin/env python3
"""First-hand grant verification at HEAD for p453 promotion candidates.

Byte counts are taken from curl's own -w '%{size_download}', never from shell
command substitution, which strips the trailing newline and makes every count
run one short (Gap 450-C defect (b), measured at 13 of 394 cells in p452).
Licence FAMILY is read from the payload TITLE, not a whole-body grep, because
GPLv3's closing paragraph recommends the LGPL and a body grep calls every
GPLv3 file LGPL (Gap 450-C defect (a)).
"""
import hashlib, re, subprocess, sys

CANDIDATES = [s.strip() for s in sys.argv[1:]]
PATHS = ["LICENSE", "LICENSE.md", "LICENSE.txt", "LICENCE", "COPYING",
         "license", "LICENSE-MIT", "MIT-LICENSE"]


def fetch(url):
    r = subprocess.run(["curl", "-s", "--max-time", "25",
                        "-w", "\n__M__%{http_code} %{size_download}", url],
                       capture_output=True, text=True)
    if "__M__" not in r.stdout:
        return None, "000", 0
    body, meta = r.stdout.rsplit("\n__M__", 1)
    code, size = (meta.split() + ["0", "0"])[:2]
    return body, code, int(size)


def family(text):
    """Title-anchored family read (first 40 non-empty lines only)."""
    head = "\n".join([l for l in text.splitlines() if l.strip()][:40])
    h = head.lower()
    if "apache license" in h and "version 2.0" in h:
        return "Apache-2.0"
    if re.search(r"\bgnu lesser general public license\b", h):
        return "LGPL"
    if re.search(r"\bgnu affero general public license\b", h):
        return "AGPL-3.0"
    if re.search(r"\bgnu general public license\b", h):
        return "GPL"
    if h.lstrip().startswith("mit license") or re.search(r"^mit license", h, re.M):
        return "MIT"
    if "permission is hereby granted, free of charge" in h:
        return "MIT (body form, no title)"
    if "redistribution and use in source and binary forms" in h:
        n = "BSD-3-Clause" if "neither the name" in text.lower() else "BSD-2-Clause"
        return n
    if "isc license" in h or "permission to use, copy, modify, and/or distribute" in h:
        return "ISC"
    if "mozilla public license" in h:
        return "MPL-2.0"
    # Content/data licence classes. A data shelf (an institution registry, a
    # curriculum corpus) is normally granted under a CC instrument, and a
    # code-licence-only grader reports those as UNREAD -- which p453's own
    # first cut did for a CC0 payload of 7 048 B.
    if "cc0 1.0 universal" in h:
        return "CC0-1.0"
    if "creative commons" in h:
        # The clause tokens are NOT abbreviated by truncation: "sharealike"[:2]
        # is "SH", and p453's own first cut published "CC-BY-SH-4.0", which is
        # not an SPDX identifier and would not match any licence filter.
        ABBR = {"sharealike": "SA", "noncommercial": "NC", "noderivatives": "ND"}
        clauses = [ABBR[k] for k in ("noncommercial", "noderivatives", "sharealike") if k in h]
        ver = "4.0" if "4.0" in h else ("3.0" if "3.0" in h else "")
        return "-".join(["CC-BY"] + clauses + ([ver] if ver else []))
    if "open data commons" in h or "odbl" in h:
        return "ODbL"
    if "the unlicense" in h or "unlicense" in h.split("\n")[0]:
        return "Unlicense"
    return "UNREAD"


for slug in CANDIDATES:
    found = False
    for p in PATHS:
        body, code, size = fetch(f"https://raw.githubusercontent.com/{slug}/HEAD/{p}")
        if code == "200" and body is not None:
            sha = hashlib.sha256(body.encode()).hexdigest()[:12]
            # size_download is the authoritative byte count; len(body) is a cross-check
            print(f"{slug:52s} {p:14s} {family(body):22s} {size:7d} B  sha256_12={sha}"
                  f"{'  [len-mismatch %d]' % len(body.encode()) if len(body.encode()) != size else ''}")
            found = True
            break
    if not found:
        print(f"{slug:52s} {'--':14s} {'NO_GRANT_PAYLOAD':22s}       0 B")
