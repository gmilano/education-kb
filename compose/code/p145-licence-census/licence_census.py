"""p145-licence-census -- `ACTION DX`: how many of these rows ship NO licence at all?

> 🟢 **`ACTION DX`** -- count how many of the 44 connector rows are UNLICENSED. `P144-Q`
> found two by accident while verifying something else, and one of them is the largest
> tool surface on its tier. Read the licence file at HEAD for all 44 rows and all 8 npm
> packages.
> 🔴 *Refuted if fewer than 4 rows are unlicensed* -- which would make `DAU-buddy` and
> `aula-virtual-mcp` a coincidence rather than a property of this population.

## What counts as a grant, and why the test is not `ls LICENSE`

🔴 **A licence IDENTIFIER is not a licence** -- `P138` established that and this probe
keeps the distinction in its output rather than collapsing it:

  `FILE`        a licence file exists at the repository root. This is a grant.
  `PKG_ONLY`    `package.json` (or `pyproject.toml`) declares `license: MIT` and no
                licence file is present. 🔴 **A declaration without a text is not a
                grant** -- it names terms nobody shipped.
  `README_ONLY` the only mention is prose in a README. Weaker still.
  `NONE`        no licence file, no declaration, no prose. 🔴 **No grant, no build.**

🔵 **`PKG_ONLY` and `NONE` are reported separately and summed separately**, because the
registered question ("unlicensed") has two defensible readings and this probe should not
quietly pick one.
"""

import json
import os
import re
import sys

LICENCE_NAMES = re.compile(
    r"^(LICEN[CS]E|COPYING|UNLICEN[CS]E|MIT-LICEN[CS]E|LICENSE-MIT|LICENSE-APACHE)"
    r"(\.(md|txt|rst|html))?$", re.IGNORECASE)

SPDX = re.compile(
    r"\b(MIT|Apache-2\.0|BSD-[23]-Clause|GPL-[23]\.0(?:-only|-or-later)?|AGPL-3\.0"
    r"(?:-only|-or-later)?|LGPL-[23]\.[01]|MPL-2\.0|ISC|Unlicense|CC0-1\.0|"
    r"CC-BY-(?:SA-)?4\.0|EPL-2\.0|BSL-1\.0|Zlib|NOASSERTION)\b", re.IGNORECASE)

BODY_HINTS = [
    (re.compile(r"Apache License.*Version 2\.0", re.S | re.I), "Apache-2.0"),
    (re.compile(r"GNU AFFERO GENERAL PUBLIC LICENSE", re.I), "AGPL-3.0"),
    (re.compile(r"GNU LESSER GENERAL PUBLIC LICENSE", re.I), "LGPL"),
    (re.compile(r"GNU GENERAL PUBLIC LICENSE", re.I), "GPL"),
    (re.compile(r"Mozilla Public License", re.I), "MPL-2.0"),
    (re.compile(r"Permission is hereby granted, free of charge", re.I), "MIT"),
    (re.compile(r"Redistribution and use in source and binary forms", re.I), "BSD"),
    (re.compile(r"This is free and unencumbered software released into the public"
                r" domain", re.I), "Unlicense"),
    (re.compile(r"Permission to use, copy, modify, and/or distribute", re.I), "ISC"),
]


def read(path, limit=200000):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read(limit)
    except OSError:
        return ""


def identify(text):
    """The licence a file's BODY is, preferring body text over any identifier in it."""
    for rx, name in BODY_HINTS:
        if rx.search(text):
            return name
    m = SPDX.search(text)
    return m.group(1) if m else "UNIDENTIFIED"


def declared(root):
    """A licence identifier declared in packaging metadata, with no file behind it."""
    pj = os.path.join(root, "package.json")
    if os.path.isfile(pj):
        try:
            with open(pj, encoding="utf-8", errors="replace") as fh:
                meta = json.load(fh)
            lic = meta.get("license") or meta.get("licence")
            if isinstance(lic, dict):
                lic = lic.get("type")
            if isinstance(lic, str) and lic.strip():
                return lic.strip(), "package.json"
        except (OSError, ValueError):
            pass
    for name in ("pyproject.toml", "setup.cfg", "setup.py", "Cargo.toml", "go.mod"):
        p = os.path.join(root, name)
        if not os.path.isfile(p):
            continue
        t = read(p, 40000)
        m = re.search(r"""(?im)^\s*licen[cs]e\s*[:=]\s*["']?\{?\s*text\s*=?\s*"""
                      r"""["']?([A-Za-z0-9.\-+ ]{2,40})""", t)
        if m:
            return m.group(1).strip().strip('"\'' + "}"), name
        m = SPDX.search(t)
        if m and re.search(r"(?i)licen[cs]e", t):
            return m.group(1), name
    return None, None


def readme_mention(root):
    for base in os.listdir(root) if os.path.isdir(root) else []:
        if base.lower().startswith("readme"):
            t = read(os.path.join(root, base), 200000)
            if re.search(r"(?i)##?\s*licen[cs]e|licen[cs]ed under", t):
                m = SPDX.search(t)
                return m.group(1) if m else "UNIDENTIFIED"
    return None


def census(root, subject):
    if not os.path.isdir(root):
        return dict(subject=subject, grant="NO_CLONE", licence="-", evidence="-")
    files = sorted(os.listdir(root))
    lic_files = [f for f in files if LICENCE_NAMES.match(f)]
    if lic_files:
        text = read(os.path.join(root, lic_files[0]))
        return dict(subject=subject, grant="FILE", licence=identify(text),
                    evidence=lic_files[0])
    dec, where = declared(root)
    if dec:
        return dict(subject=subject, grant="PKG_ONLY", licence=dec, evidence=where)
    rm = readme_mention(root)
    if rm:
        return dict(subject=subject, grant="README_ONLY", licence=rm, evidence="README")
    return dict(subject=subject, grant="NONE", licence="-", evidence="-")


COLS = ["subject", "tier", "grant", "licence", "evidence"]


def main(argv):
    rows = []
    for spec in argv:
        parts = spec.split("=")
        r = census(parts[1], parts[0])
        r["tier"] = parts[2] if len(parts) > 2 else "-"
        rows.append(r)
    print("\t".join(COLS))
    for r in rows:
        print("\t".join(str(r[c]) for c in COLS))

    by = {}
    for r in rows:
        by[r["grant"]] = by.get(r["grant"], 0) + 1
    print("", file=sys.stderr)
    for k in ("FILE", "PKG_ONLY", "README_ONLY", "NONE", "NO_CLONE"):
        print("# %-12s %d" % (k, by.get(k, 0)), file=sys.stderr)
    strict = by.get("NONE", 0)
    wide = strict + by.get("PKG_ONLY", 0) + by.get("README_ONLY", 0)
    print("# UNLICENSED strict (no file, no declaration): %d of %d" % (strict, len(rows)),
          file=sys.stderr)
    print("# NO SHIPPED GRANT (strict + declaration-only): %d of %d" % (wide, len(rows)),
          file=sys.stderr)
    copyleft = [r["subject"] for r in rows
                if re.match(r"(?i)(a?gpl|lgpl)", str(r["licence"]))]
    print("# COPYLEFT rows: %d  %s" % (len(copyleft), ", ".join(copyleft)),
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
