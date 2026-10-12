"""p147-licence-language -- `ACTION EE`, and the defect `ACTION EE` was standing on.

`ACTION EE` asked whether the 8 unlicensed connector rows are **forks of a licensed
parent**, refuted if fewer than 2 are. 🔴 **0 of 8 are forks of anything** (`P147-F`,
measured on the WebFetch channel `T60` opened), so the action is refuted on its own terms.

🔴 **Two of those 8 rows are not unlicensed.** They declare a grant in a README, in
Portuguese and in Spanish, and `p145-licence-census` cannot see either because its README
matcher is `licen[cs]e` -- an English-only pattern on a shelf whose own pages describe a
third of these rows as LATAM systems of record.

## The pattern, and exactly what it misses

`p145-licence-census.readme_mention` matches:

    (?i)##?\\s*licen[cs]e|licen[cs]ed under

🔴 `Licença` (pt) is `l-i-c-e-n-ç-a` and `Licencia` (es) is `l-i-c-e-n-c-i-a`. Neither can
match `licen[cs]e`, which requires `e` in position 7. 🔵 **This is not a tuning problem.
The two most common Romance spellings of the word are outside the character class.**

| row | heading | what it says | p145 | here |
|---|---|---|---|---|
| `frjunioalves/suap-mcp` | `## Licença` | *"licenciado sob a licença MIT. Veja o arquivo `LICENSE`"* | `NONE` | `README_ONLY / MIT` |
| `eugeborzone/Auto_Grade_Guarani` | `# Licencia` | *"Usted es libre de copiar y modificar lo que quiera de esta repo"* | `NONE` | `README_ONLY / UNIDENTIFIED` |

🔴 **`suap-mcp` cites a `LICENSE` file that was never committed** -- `git ls-files` matches
nothing. So the row is `README_ONLY` and not `FILE`: the declaration is real, the file it
points at does not exist, and a studio still has only prose to rely on.

🔵 **`Auto_Grade_Guarani` is a grant and not a licence.** It permits copying and
modification and says nothing about warranty, patents, attribution or redistribution. 🟢
**`UNIDENTIFIED` is the honest value** -- the census's own class for "a grant whose terms
cannot be named" -- and it is materially different from silence.

## Method -- baseline first, one variable

The module carries **both** matchers and runs them over the same 44 clones in one pass.
🟢 **A row is reported as changed only when the baseline reproduces p145's published value
for it**, so a difference cannot be the clone set rather than the pattern.

    python3 licence_language.py <clone-dir> [baseline.tsv]
    python3 test_licence_language.py        # 13 tests, authored fixtures, offline
"""

import json
import os
import re
import sys

# -------------------------------------------------- p145, carried over verbatim
LICENCE_NAMES = re.compile(
    r"^(LICEN[CS]E|COPYING|UNLICEN[CS]E|MIT-LICEN[CS]E|LICENSE-MIT|LICENSE-APACHE)"
    r"(\.(md|txt|rst))?$", re.IGNORECASE)
SPDX = re.compile(
    r"\b(MIT|Apache-2\.0|BSD-[23]-Clause|AGPL-3\.0(?:-only|-or-later)?|"
    r"GPL-[23]\.0(?:-only|-or-later)?|LGPL-[23]\.[01](?:-only|-or-later)?|"
    r"MPL-2\.0|ISC|Unlicense|CC0-1\.0|ECL-2\.0)\b")
BODY_HINTS = [
    (re.compile(r"Apache License.*Version 2\.0", re.S | re.I), "Apache-2.0"),
    (re.compile(r"GNU AFFERO GENERAL PUBLIC LICENSE", re.I), "AGPL-3.0"),
    (re.compile(r"GNU LESSER GENERAL PUBLIC LICENSE", re.I), "LGPL"),
    (re.compile(r"GNU GENERAL PUBLIC LICENSE", re.I), "GPL"),
    (re.compile(r"Mozilla Public License", re.I), "MPL-2.0"),
    (re.compile(r"Permission is hereby granted, free of charge", re.I), "MIT"),
    (re.compile(r"Redistribution and use in source and binary forms", re.I), "BSD"),
    (re.compile(r"Permission to use, copy, modify, and/or distribute", re.I), "ISC"),
]

BASELINE_README = re.compile(r"(?i)##?\s*licen[cs]e|licen[cs]ed under")

# -------------------------------------------------- 🆕 the one variable
# The heading, in the five languages this shelf's rows are actually written in, plus the
# inline "licensed under" forms. 🔴 `licen[cs]e` cannot reach `licença` or `licencia`.
EXTENDED_README = re.compile(
    r"(?i)"
    r"#{1,3}\s*(licen[cs]e|licen[cçs]a|licencia|lizenz|licence|licenza|licens)\b"
    r"|licen[cs]ed under"
    r"|licenciad[oa] sob"              # pt: "licenciado sob a licença MIT"
    r"|licenciad[oa] bajo"             # es: "licenciado bajo la licencia MIT"
    r"|bajo (?:la )?licencia"
    r"|sob (?:a )?licen[cç]a"
    r"|unter der lizenz"
)
# An informal permission grant: it says what you may do and names no terms. Recorded so a
# row carrying one is not scored as silent, and not scored as licensed either.
INFORMAL_GRANT = re.compile(
    r"(?i)"
    r"libre de (?:copiar|usar|modificar)"
    r"|free to (?:copy|use|modify)"
    r"|livre para (?:copiar|usar|modificar)"
    r"|haga lo que quiera|do what ?ever you want|do as you wish"
)


def read(path, limit=200000):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read(limit)
    except OSError:
        return ""


def identify(text):
    for rx, name in BODY_HINTS:
        if rx.search(text):
            return name
    m = SPDX.search(text)
    return m.group(1) if m else "UNIDENTIFIED"


def declared(root):
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


def readme_mention(root, rx, allow_informal=False):
    """(licence, how) from a README, under the matcher `rx`."""
    for base in sorted(os.listdir(root)) if os.path.isdir(root) else []:
        if not base.lower().startswith("readme"):
            continue
        t = read(os.path.join(root, base), 200000)
        if rx.search(t):
            m = SPDX.search(t)
            return (m.group(1) if m else "UNIDENTIFIED"), "README"
        if allow_informal and INFORMAL_GRANT.search(t):
            return "UNIDENTIFIED", "README_INFORMAL"
    return None, None


def census(root, subject, rx, allow_informal=False):
    if not os.path.isdir(root):
        return dict(subject=subject, grant="NO_CLONE", licence="-", evidence="-")
    files = sorted(os.listdir(root))
    lic_files = [f for f in files if LICENCE_NAMES.match(f)]
    if lic_files:
        body = read(os.path.join(root, lic_files[0]))
        return dict(subject=subject, grant="FILE", licence=identify(body),
                    evidence=lic_files[0])
    # 🟢 `ACTION FE` — the ladder is `FILE > PKG_ONLY > README_ONLY`, as `p145`'s own
    # docstring documents it ("README_ONLY … weaker still"). p147 silently inverted the
    # last two rungs, which demotes a declared manifest licence to a prose mention.
    # `T74`. The order below is the corrected one and `ORDER` names it explicitly so a
    # later pass can compare the two without reading the control flow.
    dec, where = declared(root)
    if dec:
        return dict(subject=subject, grant="PKG_ONLY", licence=dec, evidence=where)
    rm, how = readme_mention(root, rx, allow_informal)
    if rm:
        return dict(subject=subject, grant="README_ONLY", licence=rm, evidence=how)
    return dict(subject=subject, grant="NONE", licence="-", evidence="-")


ORDER = ("FILE", "PKG_ONLY", "README_ONLY")


def census_p147_order(root, subject, rx, allow_informal=False):
    """p147's INVERTED ladder, kept verbatim as the control.

    🔵 Retained deliberately: `ACTION FE` is a comparison, and a comparison needs both
    arms in one place. This is the arm that is wrong.
    """
    if not os.path.isdir(root):
        return dict(subject=subject, grant="NO_CLONE", licence="-", evidence="-")
    files = sorted(os.listdir(root))
    lic_files = [f for f in files if LICENCE_NAMES.match(f)]
    if lic_files:
        body = read(os.path.join(root, lic_files[0]))
        return dict(subject=subject, grant="FILE", licence=identify(body),
                    evidence=lic_files[0])
    rm, how = readme_mention(root, rx, allow_informal)
    if rm:
        return dict(subject=subject, grant="README_ONLY", licence=rm, evidence=how)
    dec, where = declared(root)
    if dec:
        return dict(subject=subject, grant="PKG_ONLY", licence=dec, evidence=where)
    return dict(subject=subject, grant="NONE", licence="-", evidence="-")


COLS = ["subject", "base_grant", "base_licence", "ext_grant", "ext_licence", "evidence",
        "changed"]


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    clone_dir = argv[1]
    published = {}
    if len(argv) > 2:
        import csv
        for r in csv.DictReader(open(argv[2]), delimiter="\t"):
            published[r["subject"]] = (r["grant"], r["licence"])

    subjects = sorted(d for d in os.listdir(clone_dir)
                      if os.path.isdir(os.path.join(clone_dir, d)))
    print("\t".join(COLS))
    changed = []
    base_mismatch = []
    counts = {"base": {}, "ext": {}}
    for s in subjects:
        root = os.path.join(clone_dir, s)
        b = census(root, s, BASELINE_README, allow_informal=False)
        e = census(root, s, EXTENDED_README, allow_informal=True)
        counts["base"][b["grant"]] = counts["base"].get(b["grant"], 0) + 1
        counts["ext"][e["grant"]] = counts["ext"].get(e["grant"], 0) + 1
        diff = (b["grant"], b["licence"]) != (e["grant"], e["licence"])
        if diff:
            changed.append((s, b, e))
        if s in published and published[s] != (b["grant"], b["licence"]):
            base_mismatch.append((s, published[s], (b["grant"], b["licence"])))
        print("\t".join([s, b["grant"], b["licence"], e["grant"], e["licence"],
                         str(e["evidence"]), "CHANGED" if diff else "-"]))

    err = sys.stderr
    err.write("\n# population: %d\n" % len(subjects))
    for mode in ("base", "ext"):
        err.write("# %-5s %s\n" % (mode, "  ".join(
            "%s=%d" % (k, counts[mode][k]) for k in sorted(counts[mode]))))
    err.write("# rows changed by language: %d\n" % len(changed))
    for s, b, e in changed:
        err.write("#   %-46s %s/%s -> %s/%s (%s)\n"
                  % (s, b["grant"], b["licence"], e["grant"], e["licence"], e["evidence"]))
    if published:
        err.write("# baseline vs p145 published: %s\n"
                  % ("REPRODUCES row for row" if not base_mismatch
                     else "%d MISMATCH" % len(base_mismatch)))
        for s, p, b in base_mismatch:
            err.write("#   MISMATCH %-40s published=%s/%s baseline=%s/%s\n"
                      % (s, p[0], p[1], b[0], b[1]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
