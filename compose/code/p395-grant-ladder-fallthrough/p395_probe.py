#!/usr/bin/env python3
"""p395 probe - the 394-A / 394-B control flow, written fresh and run first-hand.

Two defects p394 pre-registered, fixed here as CONTROL FLOW rather than vocabulary:

  394-A  the licence ladder is FIRST-HIT-WINS. A year/holder stub at LICENSE
         (R's templated-licence convention) beats the real grant one position
         later at LICENSE.md. Fix: keep reading past a payload that yields no
         licence family, remember it, and only fall back to it if nothing better
         is found.

  394-B  the R grant lives in DESCRIPTION's `License:` field, which CRAN itself
         enforces. The gate had DESCRIPTION in neither path list, so five real
         GPL packages fell through to "all rights reserved until shown otherwise".
         Fix: a MANIFEST arm that reads DESCRIPTION verbatim.

  394-F  a README-only grant is a real (weakest) class. Included so the arm the
         base made standing ~100 passes ago is actually consulted here.

Fetching is curl, which is this session's measured-good channel; no interpreter
is pointed at the cloned tree. Output is a TSV on stdout.
"""
import hashlib
import re
import subprocess
import sys

RAW = "https://raw.githubusercontent.com/%s/%s/%s"
BRANCHES = ("main", "master", "develop")

# 394-A: order still matters, but position no longer decides.
LICENCE_PATHS = (
    "LICENSE", "LICENSE.md", "LICENSE.txt", "LICENSE.TXT",
    "LICENCE", "LICENCE.md", "LICENCE.txt",
    "LICENSE.rst", "COPYING", "COPYING.txt", "COPYING.md",
    "LICENSE-MIT", "LICENSE-APACHE", "License.md", "License.txt", "license",
)
MANIFEST_PATHS = ("DESCRIPTION", "package.json", "pyproject.toml", "Cargo.toml")
README_PATHS = ("README.md", "readme.md", "README.rst", "README.txt")

FAMILIES = (
    ("AGPL-3.0", ("GNU AFFERO GENERAL PUBLIC LICENSE",)),
    ("LGPL", ("GNU LESSER GENERAL PUBLIC LICENSE",)),
    ("GPL", ("GNU GENERAL PUBLIC LICENSE",)),
    ("Apache-2.0", ("Apache License",)),
    ("ECL-2.0", ("Educational Community License",)),
    ("MPL-2.0", ("Mozilla Public License",)),
    ("BSD", ("BSD ", "Redistribution and use in source and binary forms")),
    ("MIT", ("MIT License", "Permission is hereby granted, free of charge")),
    ("ISC", ("ISC License",)),
    ("Unlicense", ("This is free and unencumbered software",)),
)

# A 49-byte "YEAR: 2021 / COPYRIGHT HOLDER: ..." file is R's templated-licence
# stub. It is evidence of a grant elsewhere, never a grant itself.
STUB = re.compile(r"^\s*(YEAR|COPYRIGHT HOLDER|ORGANIZATION)\s*:", re.I | re.M)


def get(url):
    r = subprocess.run(["curl", "-s", "-w", "\n%{http_code}", "--max-time", "25", url],
                       capture_output=True, text=True)
    out = r.stdout.rsplit("\n", 1)
    if len(out) != 2:
        return 0, ""
    body, code = out
    try:
        return int(code), body
    except ValueError:
        return 0, ""


def family_of(text):
    """Title region only: AGPL's section 2 quotes the GPL, so a whole-payload
    scan mis-families copyleft. 1200 chars covers every title block seen."""
    head = text[:1200]
    for fam, probes in FAMILIES:
        for p in probes:
            if p.lower() in head.lower():
                return fam
    return None


def looks_like_stub(text):
    return len(text.strip()) < 400 and bool(STUB.search(text))


def manifest_grant(name, text):
    """394-B. DESCRIPTION is read verbatim because CRAN enforces the field."""
    if name == "DESCRIPTION":
        m = re.search(r"^License:\s*(.+)$", text, re.I | re.M)
        return m.group(1).strip() if m else None
    m = re.search(r'"license"\s*:\s*"([^"]+)"', text, re.I)
    if m:
        return m.group(1).strip()
    m = re.search(r'^license\s*=\s*[\{"]?\s*(?:text\s*=\s*")?([^"\}\n]+)', text, re.I | re.M)
    return m.group(1).strip() if m else None


README_GRANT = re.compile(
    r"(?:licen[cs]ed?\s+under|released\s+under|is\s+licen[cs]ed)\s+"
    r"(?:the\s+)?(MIT|Apache[- ]2\.0|BSD[- ]3[- ]Clause|BSD|GPL[- ]?3|AGPL[- ]?3|ISC)", re.I)


def probe(repo):
    """One address -> one row. Returns (state, family, path, bytes, sha16, note)."""
    stub_seen = None
    for b in BRANCHES:
        for name in LICENCE_PATHS:
            st, body = get(RAW % (repo, b, name))
            if st != 200 or not body.strip():
                continue
            fam = family_of(body)
            sha = hashlib.sha256(body.encode()).hexdigest()[:12]
            nbytes = len(body.encode())
            if fam:
                return ("LICENSED", fam, "%s/%s" % (b, name), nbytes, sha,
                        "grant read from payload")
            # 394-A: no family here. Record it and KEEP READING.
            if stub_seen is None:
                kind = "stub" if looks_like_stub(body) else "payload-no-family"
                stub_seen = ("%s/%s" % (b, name), nbytes, sha, kind)
    # 394-B: the manifest arm.
    for b in BRANCHES:
        for name in MANIFEST_PATHS:
            st, body = get(RAW % (repo, b, name))
            if st != 200 or not body.strip():
                continue
            dec = manifest_grant(name, body)
            if dec:
                sha = hashlib.sha256(body.encode()).hexdigest()[:12]
                note = "MANIFEST-ONLY: %s declares %r" % (name, dec[:40])
                if stub_seen:
                    note += " (+stub at %s)" % stub_seen[0]
                return ("MANIFEST-ONLY", dec[:40], "%s/%s" % (b, name),
                        len(body.encode()), sha, note)
    # 394-F: the README arm the base made standing at p288.
    for b in BRANCHES:
        for name in README_PATHS:
            st, body = get(RAW % (repo, b, name))
            if st != 200 or not body.strip():
                continue
            m = README_GRANT.search(body)
            sha = hashlib.sha256(body.encode()).hexdigest()[:12]
            if m:
                return ("README-ONLY", m.group(1), "%s/%s" % (b, name),
                        len(body.encode()), sha, "grant claimed in README prose only")
            if stub_seen:
                return ("STUB-ONLY", None, stub_seen[0], stub_seen[1], stub_seen[2],
                        "%s at licence path, no family anywhere" % stub_seen[3])
            return ("EXISTS-NOLICENCE", None, "%s/%s" % (b, name),
                    len(body.encode()), sha, "real repo, no grant on any arm")
    if stub_seen:
        return ("STUB-ONLY", None, stub_seen[0], stub_seen[1], stub_seen[2],
                "%s only" % stub_seen[3])
    return ("ABSENT", None, None, 0, None, "no licence, no manifest, no README")


def main():
    repos = sys.argv[1:]
    print("repo\tstate\tfamily\tpath\tbytes\tsha256_12\tnote")
    for r in repos:
        state, fam, path, nbytes, sha, note = probe(r)
        print("%s\t%s\t%s\t%s\t%s\t%s\t%s"
              % (r, state, fam or "-", path or "-", nbytes, sha or "-", note), flush=True)


if __name__ == "__main__":
    main()
