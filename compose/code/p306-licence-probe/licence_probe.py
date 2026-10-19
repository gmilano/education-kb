#!/usr/bin/env python3
"""p306 licence prober — reads licence files from raw.githubusercontent.com as PAYLOADS.

Implements p305's permission-clause rule (the replacement for p304's refuted
`bytes < 400` length rule) and records byte length + sha256_12 for every payload,
which is this base's standing evidence format.

Usage: licence_probe.py slugs.txt out.tsv
"""
import hashlib
import os
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


sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "p150-gpl-affero-discrimination"))
from gpl_affero import title_licence as _title_licence  # noqa: E402
from gpl_affero import title_version as _title_version  # noqa: E402


def _titled_family(text):
    """The title-line licence WITH its version, e.g. `GPL-3.0`, or None.

    🔴 p150's `title_licence()` returns the bare family `GPL` for both GPL-2.0 and
    GPL-3.0, and the version is not cosmetic: GPL-2.0 has no patent grant and no
    section 13 at all, which `p150`'s own notes record against `qxbao/qldt-hanu-mcp`.
    The two reads compose; neither alone is a licence identifier.
    """
    fam = _title_licence(text)
    if fam is None:
        return None
    if "-" in fam:          # AGPL-3.0 already carries its version
        return fam
    ver = _title_version(text)
    return "%s-%s" % (fam, ver) if ver else fam


def classify(text):
    """p305 clause rule. Returns (verdict, family)."""
    low = text.lower()
    has_grant = any(c in low for c in GRANT_CLAUSES)
    reserved = any(m in low for m in RESERVED_MARKERS)
    if not has_grant:
        return ("RESERVED-NO-GRANT" if reserved else "NO-GRANT-CLAUSE"), "-"
    # 🔴 p309: THE GNU RUNGS ARE NOT READ FROM THE BODY ANY MORE.
    #
    # This function carried `elif "affero" in low:` ordered BEFORE the GPL rung,
    # over the whole lowercased payload.  GPL-3.0 §13 is TITLED "Use with the GNU
    # Affero General Public License" and the body names the Affero licence three
    # times (lines 552/556/559 of the 35 191 B payload pinned in
    # `p309-affero-rung-census/fixtures/`), so NO GPL-3.0 PAYLOAD COULD EVER REACH
    # THE GPL RUNG.  Measured at p309: of the four AGPL-3.0 verdicts this prober
    # has emitted in its life, all four at p309, TWO were GPL-3.0 by title —
    # `GatorEducator/gatorgrader` (35 191 B) and `five-plus-one/AI-Marker-Suite`
    # (35 154 B).
    #
    # 🔴 And the fix already existed.  `p150-gpl-affero-discrimination` refuted
    # this exact test, named `p145`/`p147`/`p149` as its carriers, and shipped
    # `title_licence()`.  `p306` was written LATER and restated the refuted body
    # test.  🔵 `p308` learned "import the canonical list, never restate it" for
    # SHELF DATA; this is the same rule for CLASSIFIERS, and this is what skipping
    # it cost.  The discriminator is IMPORTED, never copied.
    fam = "unknown"
    titled = _titled_family(text)
    if titled:
        return "GRANT", titled
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
