#!/usr/bin/env python3
"""Fetch the licence payload of every slug on a list, HEAD-ref based.

Same question as `p170-headref-license-sweep`, same filename list, same three-way
outcome -- rewritten as one concurrent process because the shell version is one
`curl` per filename per slug and this pass's denominator is 503 slugs, not 200.

The family vocabulary is DELIBERATELY the coarse p170 one (GPL, CC-BY, UNKNOWN),
not the fine one in `../lib/license_family.sh`, so the TSV this writes is
comparable row-for-row with `p170-headref-license-sweep/result.2026-10-03.tsv`.

TSV: slug \t status \t hit_path \t bytes \t family
"""
import sys, re, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor

LICENSE_NAMES = ["LICENSE", "LICENSE.md", "LICENSE.txt", "COPYING", "COPYING.txt",
                 "license", "license.md", "license.txt", "LICENCE", "LICENCE.md",
                 "LICENSE-MIT", "LICENSE-APACHE", "LICENSE.rst", "LICENSE-MIT.txt"]
README_NAMES = ["README.md", "README.rst", "readme.md", "README", "README.markdown",
                "docs/README.md", "package.json", "setup.py"]
RAW = "https://raw.githubusercontent.com/{slug}/HEAD/{path}"


def get(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": "globant-kb-p436"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, b""
    except Exception:
        return 0, b""


def family_of(text):
    """Coarse family, matching the p170 published vocabulary."""
    t = text[:4000].lower()
    head = "\n".join(text.splitlines()[:6]).lower()
    if "gnu affero general public license" in t:
        return "AGPL-3.0"
    if "gnu lesser general public license" in t:
        return "LGPL"
    if "gnu general public license" in t:
        return "GPL"
    if "apache license" in t and "version 2.0" in t:
        return "Apache-2.0"
    if "mozilla public license" in t:
        return "MPL-2.0"
    if "eclipse public license" in t:
        return "EPL"
    if "educational community license" in t:
        return "ECL-2.0"
    if "mit license" in head or "permission is hereby granted, free of charge" in t:
        return "MIT"
    if "redistribution and use in source and binary forms" in t:
        return "BSD"
    if "permission to use, copy, modify, and/or distribute this software" in t:
        return "ISC"
    if "creative commons" in t and "cc0" in t:
        return "CC0-1.0"
    if "creative commons" in t:
        return "CC-BY"
    if "this is free and unencumbered software released into the public domain" in t:
        return "Unlicense"
    if "mulan" in t:
        return "MulanPSL"
    return "UNKNOWN"


def one(slug):
    for fn in LICENSE_NAMES:
        code, body = get(RAW.format(slug=slug, path=fn))
        if code == 200:
            text = body.decode("utf-8", "replace")
            return (slug, "LICENSED", fn, str(len(body)), family_of(text)), text
    for rm in README_NAMES:
        code, _ = get(RAW.format(slug=slug, path=rm))
        if code == 200:
            return (slug, "UNLICENSED", "-", "0", f"(reachable via {rm})"), ""
    return (slug, "UNREACHABLE", "-", "0", "-"), ""


def main():
    slugs = [l.strip() for l in open(sys.argv[1]) if l.strip()]
    outdir = sys.argv[2]
    with ThreadPoolExecutor(max_workers=16) as ex:
        results = list(ex.map(one, slugs))
    with open(f"{outdir}/payloads.tsv", "w") as f:
        for row, _ in results:
            f.write("\t".join(row) + "\n")
    # JSON, not TSV: a licence payload may contain a bare CR, which splits a TSV
    # line and makes the slug column unparseable.  The first build hit exactly that.
    import json
    with open(f"{outdir}/payloads.body.json", "w") as f:
        json.dump({row[0]: text for row, text in results if row[1] == "LICENSED"}, f)


if __name__ == "__main__":
    main()
