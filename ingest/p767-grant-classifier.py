#!/usr/bin/env python3
"""ACTION p764-E — classify a licence payload by OPERATIVE TEXT, never by byte count
or sha. p765 read eight distinct Apache-2.0 sizes (10,266-12,227 B) and five
AGPL-3.0 sizes (33,709-34,523 B) in one pass; size and sha heuristics are dead.

Three defects were found in this classifier's own first revision and are fixed here,
because each one produced a wrong verdict on a payload whose truth was already known:

  D1  Canonical GPL-3.0 names "GNU Affero General Public License" THREE times (sec 13 and
      the how-to-apply note), so a name match is not evidence of AGPL. Family is
      anchored on the TITLE LINE and confirmed by a discriminator clause
      ("Remote Network Interaction" is in AGPL-3.0 and absent from GPL-3.0).
  D2  LGPL-3.0 incorporates GPL-3.0 by reference and therefore contains the GPL
      name and "Version 3"; a partial match must never outrank a full one, and
      the title line settles it.
  D3  Both GPL-3.0 and AGPL-3.0 contain the word "noncommercial" in their own
      sec 5 / sec 7 text, so a whole-file noncommercial scan flags every copyleft
      payload. Composite and restriction flags are read from the TAIL ONLY —
      the bytes after the licence body's own terminator.
  D5  A regression introduced by the D4 fix and caught by the canonical controls:
      every copyleft family NAMES ITSELF in its own "How to Apply These Terms"
      appendix, so matching family names in the tail flagged canonical AGPL-3.0,
      GPL-3.0 and GPL-2.0 as composite — 18 false positives against 3 true ones.
      A family's own prose names are now excluded explicitly (SELF_NAMES), and
      `xeokit/xeokit-sdk` survives as a TRUE positive: AGPL-3.0 plus a bundled
      third-party notices block naming MIT and MPL-2.0 components.
  D4  Found by the one payload this classifier existed to catch. MIT and BSD have no
      "END OF TERMS AND CONDITIONS", so the tail was empty and a second grant appended
      after an MIT notice was invisible; and the composite detector matched only an
      English creativecommons.org URL, so a grant named in Spanish prose
      ("licencia Creative Commons Atribucion 4.0 Internacional") scored clean.
      The tail now starts after the matched family's OWN last operative clause, and
      second grants are matched by NAME, in prose, across languages.

usage: p765-grant-classifier.py FILE [FILE...]   -> TSV on stdout
"""
import re, sys, hashlib, os

# (family, title-line pattern, discriminator clauses that must ALL appear)
FAMILIES = [
    ("AGPL-3.0",        r"gnu affero general public license", ["remote network interaction"]),
    ("LGPL-3.0",        r"gnu lesser general public license",
                        ["version 3", "gnu general public license"]),
    ("LGPL-2.1",        r"gnu lesser general public license", ["version 2.1"]),
    ("GPL-3.0",         r"gnu general public license",
                        ["version 3", "how to apply these terms"]),
    ("GPL-2.0",         r"gnu general public license", ["version 2"]),
    ("Apache-2.0",      r"apache license",
                        ["grant of copyright license", "grant of patent license",
                         "disclaimer of warranty", "limitation of liability"]),
    ("MPL-2.0",         r"mozilla public license", ["exhibit a"]),
    ("CC-BY-NC-SA-4.0", r"attribution-noncommercial-sharealike 4\.0", []),
    ("CC-BY-NC-4.0",    r"attribution-noncommercial 4\.0", []),
    ("CC-BY-SA-4.0",    r"attribution-sharealike 4\.0", []),
    ("CC-BY-ND-4.0",    r"attribution-noderivatives 4\.0", []),
    ("CC-BY-4.0",       r"attribution 4\.0 international", []),
    ("CC0-1.0",         r"cc0 1\.0", []),
    ("BSD-3-Clause",    r"", ["redistributions of source code must retain",
                              "redistributions in binary form", "neither the name"]),
    ("BSD-2-Clause",    r"", ["redistributions of source code must retain",
                              "redistributions in binary form"]),
    # p767: ISC is OSI-approved, permissive and ubiquitous in the npm ecosystem, and
    # p765's family table had no entry for it -- node_modules/mapbox/LICENSE scored
    # UNRECOGNISED on a clean, well-known grant. Anchored on its own operative clause,
    # which no other family carries ("with or without fee").
    ("ISC",             r"", ["permission to use, copy, modify",
                              "with or without fee is hereby granted"]),
    ("0BSD",            r"", ["permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted"]),
    ("Unlicense",       r"", ["this is free and unencumbered software released into the public domain"]),
    ("SIL-OFL-1.1",     r"sil open font license", ["original version"]),
    ("MIT",             r"", ["permission is hereby granted, free of charge",
                              "without restriction, including without limitation",
                              'the software is provided "as is"']),
]
TERMINATOR = re.compile(r"end of terms and conditions", re.I)
# A standard appendix ("How to apply...") is part of the grant, not a second grant.
APPENDIX = re.compile(r"appendix: how to apply|how to apply these terms|"
                      r"exhibit a|end of the? ?(gnu|apache)", re.I)
CC_URL = re.compile(r"creativecommons\.org/licenses/([a-z-]+)/([0-9.]+)", re.I)
# D4: a second grant named in prose, in any of the languages these shelves meet.
CC_NAME = re.compile(
    r"creative\s+commons\s+"
    r"(?:attribution|atribuci[oó]n|atribui[cç][aã]o|namensnennung|attribution)"
    r"[-\s]*((?:non[-\s]?commercial|nocomercial|n[aã]ocomercial|nc)?)"
    r"[-\s]*((?:share[-\s]?alike|compartirigual|sa)?)"
    r"[-\s]*((?:no[-\s]?deriv\w*|sinderivadas|nd)?)"
    r"[-\s]*([0-9]\.[0-9])", re.I)
OTHER_FAMILY = re.compile(
    r"\b(apache licen[sc]e|mit licen[sc]e|bsd[- ][23][- ]clause|"
    r"mozilla public licen[sc]e|business source licen[sc]e|"
    r"gnu (?:lesser |affero )?general public licen[sc]e)\b", re.I)
# D5: the prose names a family uses for ITSELF, including in its appendix.
SELF_NAMES = {
    "AGPL-3.0": ["gnu affero general public license", "gnu general public license",
                 "gnu lesser general public license", "apache license"],
    "GPL-3.0":  ["gnu general public license", "gnu affero general public license",
                 "gnu lesser general public license", "apache license"],
    "GPL-2.0":  ["gnu general public license", "gnu lesser general public license"],
    "LGPL-3.0": ["gnu lesser general public license", "gnu general public license"],
    "LGPL-2.1": ["gnu lesser general public license", "gnu general public license"],
    "MPL-2.0":  ["mozilla public license", "gnu general public license",
                 "gnu lesser general public license"],
    "Apache-2.0": ["apache license"],
    "MIT": ["mit license"],
    "BSD-3-Clause": ["bsd"], "BSD-2-Clause": ["bsd"],
}
# Each family's own last operative sentence — where its body ends when there is no
# formal terminator line.
BODY_END = {
    "MIT": re.compile(r"other dealings in\s+the\s+software\.?", re.I),
    "BSD-3-Clause": re.compile(r"possibility of such damage\.?", re.I),
    "BSD-2-Clause": re.compile(r"possibility of such damage\.?", re.I),
}
RESTRICT = re.compile(r"noncommercial|non-commercial|not[- ]for[- ]profit|"
                      r"educational and research purposes only|research purposes only|"
                      r"excludes any service|noderivatives|no derivative works|"
                      r"may not be used for commercial", re.I)
BYREF = re.compile(r"(licensed under|is licensed under|released under).{0,120}"
                   r"(licen[sc]e)(.{0,120}(to view a copy|visit|see ))?", re.I | re.S)

QUOTES = str.maketrans({
    "\u2018": "'", "\u2019": "'", "\u201a": "'", "\u201b": "'",
    "\u201c": '"', "\u201d": '"', "\u201e": '"', "\u201f": '"',
    "\u00ab": '"', "\u00bb": '"', "\u2039": "'", "\u203a": "'",
    "\u00a9": "(c)", "\u2014": "-", "\u2013": "-", "\u00a0": " ",
})
def norm(t):
    # p767 / ACTION p766-D, THIRD AXIS: a grant's operative text must be matched
    # through its TYPOGRAPHY. Found by control: node_modules/debug and
    # node_modules/basic-auth are plain MIT written `'Software'` with SINGLE quotes,
    # and markbaker/complex writes `Copyright (c)` as `Copyright (c)`. The p765
    # discriminator `the software is provided "as is"` is quote-character-sensitive
    # and scored all three UNRECOGNISED. Quote class is not meaning.
    t = t.translate(QUOTES)
    t = re.sub(r"\s+", " ", re.sub(r"[`*_=#>|\[\]]", "", t)).lower()
    return re.sub(r"[\"']", '"', t)

def classify(path):
    raw = open(path, "rb").read()
    b, sha = len(raw), hashlib.sha256(raw).hexdigest()[:12]
    txt = raw.decode("utf-8", "replace")
    body = norm(txt)
    title = norm(next((l for l in txt.splitlines() if l.strip()), ""))[:120]

    titled, untitled = [], []
    for fam, tpat, discs in FAMILIES:
        if not all(d in body for d in discs):
            continue
        if tpat and re.search(tpat, title):
            titled.append(fam)
        elif tpat and re.search(tpat, body):
            untitled.append(fam)        # family named, but not as the title
        elif not tpat:
            untitled.append(fam)        # MIT/BSD have no canonical title line
    if titled:
        fam, basis = titled[0], "title+clauses"
    elif untitled:
        fam, basis = untitled[0], "clauses-only"
    else:
        fam, basis = "UNRECOGNISED", "none"

    # D3: flags from the TAIL ONLY — after the licence body's own terminator.
    ends = [m.end() for m in TERMINATOR.finditer(txt)]
    if ends:
        tail = txt[ends[-1]:]
    else:
        be = BODY_END.get(fam)
        m = list(be.finditer(txt))[-1] if (be and be.search(txt)) else None
        tail = txt[m.end():] if m else (txt if b < 1024 else "")
    tail = APPENDIX.sub(" ", tail)
    found = {f"CC-{m.group(1).upper()}-{m.group(2)}" for m in CC_URL.finditer(tail)}
    for m in CC_NAME.finditer(tail):
        parts = ["CC", "BY"]
        if m.group(1): parts.append("NC")
        if m.group(2): parts.append("SA")
        if m.group(3): parts.append("ND")
        found.add("-".join(parts) + "-" + m.group(4))
    selfnames = SELF_NAMES.get(fam, [])
    found |= {m.group(0).strip() for m in OTHER_FAMILY.finditer(tail)
              if m.group(0).strip().lower() not in selfnames}
    extra = sorted(x for x in found if x.upper() != fam.upper())
    flags = []
    if extra: flags.append("COMPOSITE:" + ",".join(extra))
    r = RESTRICT.search(tail) or (RESTRICT.search(txt) if fam.startswith("CC-") else None)
    if r: flags.append("RESTRICTED:" + r.group(0).lower())
    form = "by-reference" if (b < 1024 and BYREF.search(txt)) else "verbatim"
    return (os.path.basename(path), b, sha, fam, basis, form, ";".join(flags) or "-")


# ---- p767: ACTION p766-D(ii) -- path-scoped, multi-family per repository -------------
# A repository does not have "a" licence. It has a MAP from path scope to grant.
# A root grant governs the repo; a non-root grant governs its own subtree only and
# is usually a VENDORED third party. Reporting one family per repository is the
# defect p766-D named (Metabase: AGPL outside enterprise/, commercial inside it).
import glob
def scope_of(p):
    d = os.path.dirname(p)
    return "<root>" if d in ("", ".") else d + "/"
def vendored(p):
    return bool(re.search(r"(^|/)(vendor|node_modules|third[_-]?party|external|deps|"
                          r"libraries|assets|lib|packages|site-packages)/", p, re.I))
print("repo\tpath\tscope\tvendored\tbytes\tsha12\tfamily\tbasis\tform\tflags")
for d in sorted(sys.argv[1:]):
    repo = os.path.basename(d.rstrip("/")).replace("~", "/", 1)
    gp = os.path.join(d, "grantpaths.txt")
    paths = [l.rstrip("\n") for l in open(gp)] if os.path.exists(gp) else []
    if not paths:
        print(f"{repo}\t-\t-\t-\t-\t-\tNO_GRANT_PATH_IN_TREE\tenumerated\t-\t-")
        continue
    for p in paths:
        blob = os.path.join(d, "blobs", p.replace("/", "~"))
        if not os.path.exists(blob):
            print(f"{repo}\t{p}\t{scope_of(p)}\t{vendored(p)}\t-\t-\tBLOB_UNREAD\t-\t-\t-")
            continue
        try:
            _f, b, sha, fam, basis, form, flags = classify(blob)
            print(f"{repo}\t{p}\t{scope_of(p)}\t{vendored(p)}\t{b}\t{sha}\t{fam}\t{basis}\t{form}\t{flags}")
        except Exception as e:
            print(f"{repo}\t{p}\t{scope_of(p)}\t{vendored(p)}\t-\t-\tERROR\t-\t-\t{e}")
