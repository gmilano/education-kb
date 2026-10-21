#!/usr/bin/env python3
"""p360 verification instrument. Kept outside the clone deliberately.

Two channels only, because they are the two that are open:
  liveness + default branch : git ls-remote --symref
  licence                   : raw.githubusercontent.com payload

ACTION ZZ-q  : licence path ladder covers orthography (LICENCE/LICENSE) and extension.
ACTION ZZ-bg : classification keys on the TITLE AND VERSION LINE, never on a keyword
               that can appear inside another licence's prose (GPL-2.0's preamble
               names the Lesser GPL -- that is the defect ZZ-bg exists to prevent).
ACTION ZZ-y/ZZ-be : the copyright-holder line is captured as a field so a renamed
               stale copy can be caught by holder string.
"""
import concurrent.futures as cf
import re
import subprocess
import sys

PATHS = [
    "LICENSE", "LICENSE.md", "LICENSE.txt", "LICENSE.MD",
    "LICENCE", "LICENCE.md", "LICENCE.txt",
    "license", "license.md", "license.txt", "licence", "licence.md",
    "COPYING", "COPYING.txt", "COPYING.md",
    "LICENSE-MIT", "LICENSE-APACHE", "MIT-LICENSE", "MIT-LICENSE.txt",
    "docs/LICENSE", ".github/LICENSE",
]


def run(cmd, timeout=40):
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return p.returncode, p.stdout, p.stderr
    except subprocess.TimeoutExpired:
        return 124, "", "timeout"


def lsremote(slug):
    rc, out, _ = run(["git", "ls-remote", "--symref",
                      f"https://github.com/{slug}", "HEAD"])
    if rc != 0 or not out.strip():
        return None, None
    branch, sha = None, None
    for line in out.splitlines():
        if line.startswith("ref:"):
            branch = line.split()[1].replace("refs/heads/", "")
        elif "\tHEAD" in line:
            sha = line.split()[0]
    return branch, sha


def fetch(slug, branch, path):
    url = f"https://raw.githubusercontent.com/{slug}/{branch}/{path}"
    rc, out, _ = run(["curl", "-sfL", "--max-time", "25", url])
    if rc != 0 or not out.strip():
        return None
    # a 404 page would not be served by raw with -f, but guard anyway
    if out.lstrip().startswith("404"):
        return None
    return out


TITLE_RULES = [
    # (regex over the title block, required version regex or None, spdx)
    (r"GNU\s+AFFERO\s+GENERAL\s+PUBLIC\s+LICENSE", r"Version\s+3", "AGPL-3.0"),
    (r"GNU\s+LESSER\s+GENERAL\s+PUBLIC\s+LICENSE", r"Version\s+3", "LGPL-3.0"),
    (r"GNU\s+LESSER\s+GENERAL\s+PUBLIC\s+LICENSE", r"Version\s+2\.1", "LGPL-2.1"),
    (r"GNU\s+GENERAL\s+PUBLIC\s+LICENSE", r"Version\s+3", "GPL-3.0"),
    (r"GNU\s+GENERAL\s+PUBLIC\s+LICENSE", r"Version\s+2", "GPL-2.0"),
    (r"Apache\s+License", r"Version\s+2\.0", "Apache-2.0"),
    (r"\bMIT\s+License\b", None, "MIT"),
    (r"Mozilla\s+Public\s+License", r"Version\s+2\.0", "MPL-2.0"),
    (r"\bThe\s+Unlicense\b", None, "Unlicense"),
    (r"BSD\s+3-Clause", None, "BSD-3-Clause"),
    (r"BSD\s+2-Clause", None, "BSD-2-Clause"),
    (r"ISC\s+License", None, "ISC"),
    (r"Creative\s+Commons", None, "CC-see-payload"),
    (r"Do\s+What\s+The\s+F.*Public\s+License", None, "WTFPL"),
]


def classify(text):
    """Key on the title block: the first 12 non-empty lines, stripped of
    markdown heading marks. Never on a keyword found anywhere in the file."""
    lines = [l.strip().lstrip("#").strip() for l in text.splitlines()]
    nonempty = [l for l in lines if l][:12]
    title_block = "\n".join(nonempty)
    for name_rx, ver_rx, spdx in TITLE_RULES:
        if re.search(name_rx, title_block, re.I):
            if ver_rx is None or re.search(ver_rx, title_block, re.I):
                return spdx
    # MIT boilerplate with no title line at all
    if re.search(r"Permission is hereby granted, free of charge", text, re.I):
        return "MIT"
    if re.search(r"Redistribution and use in source and binary forms", text, re.I):
        return "BSD-family"
    return "UNCLASSIFIED"


HOLDER_RX = re.compile(
    r"^\s*(?:#\s*)?(?:Copyright|Copyright\s*\(c\)|\(c\))\s*(?:\(c\)\s*)?"
    r"(?:©\s*)?([^\n]{0,120})", re.I | re.M)


def holder(text):
    m = HOLDER_RX.search(text)
    if not m:
        return ""
    h = m.group(1).strip()
    h = re.sub(r"^\(c\)\s*", "", h, flags=re.I)
    h = re.sub(r"^\s*[\d\-,\s]{4,}", "", h).strip()
    h = re.sub(r"\s*All rights reserved\.?$", "", h, flags=re.I).strip()
    return h[:80]


def probe(slug):
    branch, sha = lsremote(slug)
    if branch is None:
        return dict(slug=slug, live="DEAD", branch="", sha="", path="",
                    licence="", holder="")
    for path in PATHS:
        text = fetch(slug, branch, path)
        if text:
            return dict(slug=slug, live="LIVE", branch=branch, sha=sha[:12],
                        path=path, licence=classify(text), holder=holder(text))
    return dict(slug=slug, live="LIVE", branch=branch, sha=sha[:12],
                path="-", licence="NO-GRANT", holder="")


def main():
    slugs = [l.strip() for l in open(sys.argv[1]) if l.strip()
             and not l.startswith("#")]
    rows = []
    with cf.ThreadPoolExecutor(max_workers=8) as ex:
        for r in ex.map(probe, slugs):
            rows.append(r)
            print("\t".join([r["slug"], r["live"], r["branch"], r["sha"],
                             r["path"], r["licence"], r["holder"]]),
                  flush=True)
    live = [r for r in rows if r["live"] == "LIVE"]
    grant = [r for r in live if r["licence"] not in ("NO-GRANT", "UNCLASSIFIED")]
    sys.stderr.write(
        f"\nprobed={len(rows)} live={len(live)} dead={len(rows)-len(live)} "
        f"grant={len(grant)} grant_rate={100*len(grant)//max(1,len(live))}%\n")


if __name__ == "__main__":
    main()
