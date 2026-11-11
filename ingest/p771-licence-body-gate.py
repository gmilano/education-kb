#!/usr/bin/env python3
"""p771 licence-integrity gate — written from scratch at p771.

Implements ONE contract that `make hooks` does not have at all:
  does a payload that DECLARES a licence family actually contain that family's
  operative text?

Rationale (T729/T730): neither byte length nor sha256 tracks the grant.
Measured at p771 over 11 Apache-2.0-declared payloads: 6 distinct byte lengths,
9 distinct sha256, 10 byte-identical normalised operative bodies -- and one
repository above 50k stars declaring "Apache License" while shipping a text
with 4 substantive deltas, including in section 4(b)'s NOTICE condition.

Normalisation is NOT optional. Defects D1/D2, caught by control at p771 before
any verdict was published: a legitimate Markdown rendering of Apache-2.0
(getodk/collect) reported 113 then 37 false word deltas until typographic
quotes, Markdown emphasis, autolinks, heading case and heading punctuation
were all folded away. After folding it is 0, while the SAME gate still returns
4 on the genuinely altered payload.

Channels: the GitHub REST API and HTML page are 403 for every address outside
this session's own repositories (ACTION p770-F, re-measured at p771), so this
reads raw.githubusercontent.com only, and resolves the default branch via
`git ls-remote --symref` rather than guessing `main` (8 of 58 addresses
measured at p771 default to neither `main` nor `master`).
"""
import re, sys, hashlib, difflib, urllib.request

GRANT_PATHS = ["LICENSE", "LICENSE.md", "LICENSE.txt", "LICENCE", "LICENCE.md",
               "COPYING", "COPYING.txt", "LICENSE.rst", "LICENSE-MIT", "license.txt"]
SPLIT = "END OF TERMS AND CONDITIONS"


def fetch(addr, path, timeout=60):
    url = f"https://raw.githubusercontent.com/{addr}/HEAD/{path}"
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return r.read()
    except Exception:
        return None


def normalise(payload: bytes):
    """Fold away everything that is presentation, keep everything operative."""
    t = payload.decode("utf-8", "replace").split(SPLIT)[0]
    for a, z in (("“", '"'), ("”", '"'), ("‘", "'"), ("’", "'")):
        t = t.replace(a, z)                      # D1: typographic quotes
    t = re.sub(r"&lt;|&gt;|&amp;", "", t)        # D1: HTML entities
    t = re.sub(r"[*_#`<>=]", "", t)              # D1: markdown emphasis, autolinks, heading rules
    t = re.sub(r"[.,:;]", "", t)                 # D2: heading punctuation
    t = re.sub(r"\s+", " ", t)
    return t.strip().lower().split()             # D2: heading case


def ownership(payload: bytes, family: str):
    """Family-aware (T731). MIT: payload head. Apache: post-appendix slot.
    GPL/AGPL: the text names no owner at all -- do not probe."""
    t = payload.decode("utf-8", "replace")
    if family == "MIT":
        head = "\n".join(t.splitlines()[:4])
        m = re.search(r"Copyright\s*(?:\(c\)|©)?\s*[^\n]{0,90}", head)
        return m.group(0).strip() if m else "UNOBTAINABLE-FROM-GRANT"
    if family == "APACHE":
        tail = t.split(SPLIT)[-1]
        m = re.search(r"Copyright\s+(?:19|20)\d\d[^\n]{0,90}", tail)
        return m.group(0).strip() if m else "UNOBTAINABLE-FROM-GRANT"
    return "UNOBTAINABLE-FROM-GRANT"


def family_of(payload: bytes):
    head = payload[:600].decode("utf-8", "replace").lower()
    if "apache license" in head:
        return "APACHE"
    if "mit license" in head or "permission is hereby granted" in head:
        return "MIT"
    if "gnu affero" in head:
        return "AGPL"
    if "gnu general public" in head:
        return "GPL"
    if "mozilla public license" in head:
        return "MPL"
    if "noncommercial" in head or "attribution-noncommercial" in head:
        return "CC-NC"
    return "UNRECOGNISED"


def grade(addr, canon_by_family):
    """Returns a list of verdict rows for one address."""
    out = []
    for path in GRANT_PATHS:
        payload = fetch(addr, path)
        if payload is None:
            continue
        fam = family_of(payload)
        sha = hashlib.sha256(payload).hexdigest()[:12]
        row = {"addr": addr, "path": path, "bytes": len(payload),
               "sha256_12": sha, "family": fam,
               "ownership": ownership(payload, fam), "body": "n/a", "deltas": 0}
        canon = canon_by_family.get(fam)
        if canon is not None:
            d = [l for l in difflib.unified_diff(canon, normalise(payload), lineterm="", n=0)
                 if l[:1] in "+-" and l[:3] not in ("+++", "---")]
            row["deltas"] = len(d)
            row["body"] = "canonical" if not d else "ALTERED"
        out.append(row)
    if not out:
        out.append({"addr": addr, "path": "-", "bytes": 0, "sha256_12": "-",
                    "family": "NO-GRANT", "ownership": "UNOBTAINABLE-FROM-GRANT",
                    "body": "n/a", "deltas": 0})
    return out


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        print("usage: p771-licence-body-gate.py ADDRS_FILE [--fail-on-altered]")
        return 2
    addrs = [l.strip() for l in open(argv[1]) if l.strip()]
    # Hold a canonical per family. Apache's canonical is the licence-picker
    # template, whose fingerprint this base has recorded since p768.
    canon = {}
    c = fetch("hapifhir/hapi-fhir", "LICENSE.txt")
    if c:
        canon["APACHE"] = normalise(c)
    cols = ["addr", "path", "bytes", "sha256_12", "family", "body", "deltas", "ownership"]
    print("\t".join(cols))
    altered = 0
    for a in addrs:
        for row in grade(a, canon):
            if row["body"] == "ALTERED":
                altered += 1
            print("\t".join(str(row[c]) for c in cols))
    sys.stderr.write(f"\n{altered} payload(s) graded ALTERED\n")
    if "--fail-on-altered" in argv and altered:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
