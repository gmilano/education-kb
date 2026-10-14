#!/usr/bin/env python3
"""P1052 — a recorded absence may be STALE, and the cue may already be on the page.

Executes the enlarged `ACTION MK` (p185) after limb 2's own run produced an
overturn the suppressed lines did not contain.

p185 classified `Zenglian990/AI_Tutor_Release` as NO-badge-only, on a rule that
is legally correct — *a badge is a claim about a licence, not a licence*. The
rule was then used to CLOSE the row. This pass re-probed the row's licence
FILE and found `LICENSE`, 1 068 B, full MIT text. The badge was true.

So the rule is kept and its USE is changed: a licence badge is not a grant, it
is a CUE TO RE-PROBE. This instrument runs that re-probe over a whole
population, in two limbs:

  limb 1  FILE   — licence files by path, both default branches, case variants.
                   Catches a stale absence: the file exists now, or existed all
                   along and a root-anchored probe missed it (Gap 370).
  limb 2  MANIFEST — the ecosystem manifest, because several ecosystems put the
                   grant there and leave the licence file as a stub. The shape
                   is already recorded twice on this shelf: shmercer/writeAlizer
                   serves a 47 B LICENSE holding only YEAR/COPYRIGHT HOLDER with
                   `License: MIT + file LICENSE` in DESCRIPTION, and p83 measured
                   sonsoleslp/tna at 46 B. Never run as a population pass.

It is a SCREEN, not a verdict. It prints the bytes and the matched string so a
human reads them.
"""
import json, re, sys, urllib.request, urllib.error

BRANCHES = ["HEAD"]
LIC_PATHS = ["LICENSE", "LICENSE.md", "LICENSE.txt", "LICENCE", "LICENCE.md",
             "LICENSE-MIT", "COPYING", "COPYING.txt", "license", "license.md",
             "License", "License.md", "LICENSE.rst", "docs/LICENSE"]
MANIFESTS = ["DESCRIPTION", "package.json", "pyproject.toml", "setup.cfg",
             "setup.py", "Cargo.toml", "composer.json", "pom.xml",
             "pubspec.yaml", "build.gradle", "PKG-INFO"]

GRANT_TEXT = re.compile(
    r"Permission is hereby granted|Apache License|GNU GENERAL PUBLIC|GNU AFFERO"
    r"|GNU LESSER|Mozilla Public License|Redistribution and use in source"
    r"|Educational Community License|Creative Commons|THE SOFTWARE IS PROVIDED"
    r"|This is free and unencumbered software", re.I)

IDENT = re.compile(
    r"MIT License|Apache License,? Version 2\.0|Apache-2\.0|BSD[- ]?[23][- ]Clause"
    r"|AGPL-?3|GPL-?[23]|LGPL-?[23]|MPL-?2\.0|ISC|Unlicense|CC-?BY[A-Z-]*"
    r"|Educational Community License", re.I)

RAW = "https://raw.githubusercontent.com/{slug}/{br}/{path}"


def get(slug, br, path):
    try:
        with urllib.request.urlopen(RAW.format(slug=slug, br=br, path=path), timeout=30) as r:
            if r.status == 200:
                return r.read().decode("utf-8", "replace")
    except Exception:
        pass
    return None


def manifest_license(name, txt):
    """Return the licence string a manifest DECLARES, or None."""
    if name == "DESCRIPTION" or name == "PKG-INFO":
        m = re.search(r"^License:\s*(.+)$", txt, re.M | re.I)
        return m.group(1).strip() if m else None
    if name.endswith(".json"):
        try:
            d = json.loads(txt)
        except Exception:
            return None
        lic = d.get("license") or d.get("licence")
        if isinstance(lic, dict):
            lic = lic.get("type")
        if isinstance(lic, list):
            lic = ", ".join(str(x) for x in lic)
        return str(lic).strip() if lic else None
    if name in ("pyproject.toml", "Cargo.toml", "setup.cfg"):
        m = re.search(r'^\s*license\s*=\s*[\{"\']?\s*(?:text\s*=\s*")?([^"\'\}\n]+)', txt, re.M | re.I)
        return m.group(1).strip() if m else None
    if name == "setup.py":
        m = re.search(r'license\s*=\s*["\']([^"\']+)', txt)
        return m.group(1).strip() if m else None
    if name == "pom.xml":
        m = re.search(r"<licenses>.*?<name>([^<]+)</name>", txt, re.S | re.I)
        return m.group(1).strip() if m else None
    if name in ("pubspec.yaml", "build.gradle"):
        m = re.search(r"licen[sc]e\s*[:=]\s*['\"]?([^'\"\n]+)", txt, re.I)
        return m.group(1).strip() if m else None
    return None


if __name__ == "__main__":
    slugs = [l.strip() for l in open(sys.argv[1]) if l.strip() and not l.startswith("#")]
    print("slug\tlimb\twhere\tbytes\tgrant_text\tidentifier\tdeclared")
    for s in slugs:
        hit = False
        for br in BRANCHES:
            for p in LIC_PATHS:
                txt = get(s, br, p)
                if txt is None:
                    continue
                ident = IDENT.search(txt)
                print(f"{s}\tFILE\t{br}/{p}\t{len(txt.encode())}\t"
                      f"{'YES' if GRANT_TEXT.search(txt) else 'NO'}\t"
                      f"{ident.group(0) if ident else '-'}\t-", flush=True)
                hit = True
                break
            if hit:
                break
        if hit:
            continue
        for br in BRANCHES:
            for m in MANIFESTS:
                txt = get(s, br, m)
                if txt is None:
                    continue
                dec = manifest_license(m, txt)
                if dec:
                    print(f"{s}\tMANIFEST\t{br}/{m}\t{len(txt.encode())}\t-\t"
                          f"{dec[:60]}\t{dec[:80]}", flush=True)
                    hit = True
                    break
            if hit:
                break
        if not hit:
            print(f"{s}\tNONE\t-\t0\tNO\t-\t-", flush=True)
