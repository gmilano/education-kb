import re, sys

# p197 FIX.  Two traps, same shape, different families:
#   TRAP 1 (known, GPL-3.0): section 13 names the AGPL  -> a BODY grep returns AGPL-3.0.
#   TRAP 2 (NEW, GPL-2.0):  the PREAMBLE names the Lesser GPL ("(Some other Free Software
#           Foundation software is covered by the GNU Lesser General Public License instead.)")
#           -> a 40-LINE-HEAD grep returns LGPL.  This is what mislabelled OS4ED/openSIS-Classic.
# The fix for both is the same: classify on the TITLE LINE, not on a window.
TITLES = [
    (r"gnu affero general public license",            "AGPL"),
    (r"gnu lesser general public license",            "LGPL"),
    (r"gnu library general public license",           "LGPL"),
    (r"gnu general public license",                   "GPL"),
    (r"educational community license",                "ECL"),
    (r"apache license",                               "Apache"),
    (r"mozilla public license",                       "MPL"),
    (r"eclipse public license",                       "EPL"),
    (r"european union public licence",                "EUPL"),
    (r"attribution[- ]sharealike",                    "CC-BY-SA"),
    (r"attribution[- ]noncommercial",                 "CC-BY-NC"),
    (r"^attribution 4\.0 international",              "CC-BY-4.0"),
    (r"^attribution 3\.0",                            "CC-BY-3.0"),
    (r"creative commons",                             "CC"),
    (r"^the unlicense",                               "Unlicense"),
    (r"^mit licen[cs]e",                              "MIT"),
    (r"^isc licen[cs]e",                              "ISC"),
    (r"bsd \d-clause",                                "BSD"),
]
def _version(line, nxt):
    ctx = (line + " " + nxt).lower()
    m = re.search(r"version\s+(\d+(?:\.\d+)?)", ctx)
    return m.group(1) if m else None

def family(text):
    lines = [l.strip() for l in text.replace("﻿", "").splitlines()]
    nonempty = [(i, l) for i, l in enumerate(lines) if l]
    # The title is the FIRST line that matches a licence title pattern.  Scanning in document
    # order (not pattern order) is what defeats both traps: the real title always precedes the
    # preamble sentence or the section that names a different licence.
    for idx, (i, l) in enumerate(nonempty):
        ll = l.lower()
        for pat, fam in TITLES:
            if re.search(pat, ll):
                nxt = nonempty[idx + 1][1] if idx + 1 < len(nonempty) else ""
                v = _version(l, nxt)
                if fam == "AGPL":   return f"AGPL-{v}.0" if v == "3" else "AGPL?"
                if fam == "LGPL":
                    if v == "3": return "LGPL-3.0"
                    if v in ("2.1",): return "LGPL-2.1"
                    if v == "2": return "LGPL-2.0"
                    return "LGPL?"
                if fam == "GPL":
                    if v == "3": return "GPL-3.0"
                    if v == "2": return "GPL-2.0"
                    if v == "1": return "GPL-1.0"
                    return "GPL?"
                if fam == "ECL":    return "ECL-2.0" if v == "2.0" else "ECL?"
                if fam == "Apache":
                    if v == "2.0": return "Apache-2.0"
                    if v == "1.1": return "Apache-1.1"
                    return "Apache?"
                if fam == "MPL":    return "MPL-2.0" if v == "2.0" else "MPL?"
                if fam == "EPL":    return f"EPL-{v}" if v else "EPL?"
                if fam == "EUPL":   return f"EUPL-{v}" if v else "EUPL?"
                return fam
    full = re.sub(r"\s+", " ", text).lower()
    if "permission is hereby granted, free of charge" in full: return "MIT"
    if "redistribution and use in source and binary forms" in full:
        return "BSD-3-Clause" if ("neither the name" in full or "endorse or promote" in full) else "BSD-2-Clause"
    return "NO-FAMILY"

GRANT_EN = ["permission is hereby granted", "redistribution and use",
            "licensed under the apache license", "terms and conditions for use, reproduction",
            "everyone is permitted to copy and distribute verbatim copies",
            "you may not use this file except in compliance",
            "this license applies to any program"]
def is_grant(text):
    full = re.sub(r"\s+", " ", text).lower()
    if any(p in full for p in GRANT_EN): return "GRANT"
    # DECLARED LIMIT: the grant detector is ENGLISH-ONLY.  A translated licence body scores
    # NON-GRANT here, which is a property of this instrument, not of the document.
    if len(text.encode()) > 5000: return "GRANT?-NON-EN"
    return "NON-GRANT"

if __name__ == "__main__":
    t = open(sys.argv[1], encoding="utf-8", errors="replace").read()
    print(f"{family(t)}\t{is_grant(t)}\t{len(t.encode('utf-8'))}")
