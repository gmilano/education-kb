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
    # 🔴 p310: `"has waived all copyright"` is the CC0 **DEED SUMMARY**'s wording.
    # The CC0 1.0 **LEGALCODE** — the 7 048 B file every CC0 row on this base
    # actually serves — says *"hereby overtly, fully, permanently, irrevocably and
    # unconditionally waives, abandons, and surrenders all of Affirmer's Copyright
    # and Related Rights"*, and contains the deed's phrase ZERO times. 🔵 **So the
    # CC0 rung in this list could never fire on a real CC0 payload: the clause was
    # written against a document the prober never fetches.** Found by running the
    # repaired prober over all SEVEN CC0 rows this base publishes — which is
    # `P310`'s rule proving itself inside one pass, because `CC0-1.0` was one of
    # the 15 families the coverage census had just reported as unexercised.
    "has waived all copyright",              # CC0 deed (kept: some repos ship it)
    "waives, abandons, and surrenders",      # CC0 1.0 legalcode, the operative verb
    "unconditionally waives",                # CC0 variants
    "grants you a worldwide, royalty-free",  # CC family
    # 🔴 p310: the source-available families grant in their OWN words and no
    # clause above reaches them. `cabbage2000-lab/paper-tutor-skills` (PolyForm
    # Noncommercial 1.0.0, 4 563 B `ffcca38841ad`) returned `NO-GRANT-CLAUSE`
    # while its §"Copyright License" reads *"The licensor grants you a copyright
    # license for the software"*. 🔵 A false NEGATIVE on the grant axis — and
    # this base has named FOUR PolyForm specimens BY HAND in earlier passes
    # (`itmir913/score-reporter`, `TrenTorch/TrenTorch`,
    # `lopentu/inside-the-scorer-paclic2026`, `lilialla/bandwise`) precisely
    # because this prober could never name one.
    "licensor grants you",                   # PolyForm / BUSL / Fair Source
    "grants you a non-transferable",         # ELv2-shaped
]
RESERVED_MARKERS = ["all rights reserved"]

# 🔴 p310 — `P250`, SETTLED 60 PASSES AGO AND NEVER WIRED INTO THIS FILE:
# *«familia de licencia y uso comercial son dos preguntas y se contestan en dos
# columnas.»* This prober answered one. For `aclascollege/aegis-graph`
# (CC-BY-NC-4.0) the family column said `CC0-1.0` — the most permissive token
# there is — and no column anywhere said *noncommercial*.
#
# 🔵 P250's rule is implemented exactly as written, INCLUDING the half that makes
# it safe: *«el detector de restricciones corre SÓLO cuando no hay familia que lo
# proteja.»* p250's own versioned negative control records what skipping that half
# costs — AGPL-3.0 §6 contains "noncommercially" and the Unlicense grants "for any
# purpose, commercial or non-commercial", so a bare marker scan condemned three
# AGPL rows and the most permissive licence in existence.
OSI_COMMERCIAL_OK = {
    "MIT", "ISC", "Apache-2.0", "BSD", "BSD-2-Clause", "BSD-3-Clause", "0BSD",
    "GPL", "GPL-2.0", "GPL-3.0", "LGPL", "LGPL-2.1", "LGPL-3.0", "AGPL-3.0",
    "MPL-2.0", "EPL-2.0", "ECL-2.0", "Unlicense", "CC0-1.0",
}
# Non-OSI, but commercial-safe by their own token: no scan needed either.
TOKEN_COMMERCIAL_OK = {"CC-BY-4.0", "CC-BY-3.0", "CC-BY-SA-4.0", "CC-BY-SA-3.0",
                       "CC-PDM"}
# Consulted ONLY where no family above protects the row.
NONCOMMERCIAL_MARKERS = [
    "noncommercial purposes", "non-commercial purposes",
    "polyform noncommercial", "business source license",
    "not for commercial use", "commercial use is prohibited",
    "any service or part of selling a service",   # the p250 specimen's own words
]


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

# 🔴 p310: THE CC RUNGS ARE NOT READ FROM THE BODY ANY MORE EITHER — and this is
# the same defect p309 repaired FIVE LINES ABOVE, one pass earlier, in this same
# ladder.
#
# The rung was `elif "cc0" in low or "public domain dedication" in low:` over the
# whole payload, ordered BEFORE the CC-BY/CC-BY-SA rungs. Every Creative Commons
# 4.0 legalcode on earth contains the string `CC0 Public Domain Dedication` ONCE,
# in its "Considerations for licensors" boilerplate, so NO CC 4.0 PAYLOAD COULD
# EVER REACH ITS OWN RUNG. Measured at p310 on first-hand payloads:
#   aclascollege/aegis-graph        19 347 B `41003d4a7474`  CC-BY-NC-4.0 -> CC0-1.0
#   Amey-Thakur/WRITING-SUPPORT     18 873 B `aa0d3c9d6a28`  CC-BY-4.0    -> CC0-1.0
#
# 🔴 And the remedy existed at p124, 186 passes earlier. `cc_version.resolve()`
# was BUILT on this exact defect — its first cut returned CC0 for 9 of 13 rows
# including `openstax/osbooks-college-physics-bundle`, which is CC-BY-NC-SA-4.0 —
# and its code says so in a comment at the rung: *"ZERO is NOT consulted here.
# 'CC0 Public Domain Dedication' appears in the boilerplate of every CC 4.0
# legalcode file, so outside the title and the URL it is evidence of nothing."*
# p124 also registered it as instance 3 of `ACTION AG`'s standing class, labelled
# `DOCUMENT-TEXT`.
#
# 🔵 So p309's conclusion — *"a classifier is canonical data too; import the
# discriminator, never restate it"* — was RIGHT and was applied to the family it
# was found in rather than to the mechanism. The CC family sat one `elif` below
# the rung p309 edited, with a prior refutation, a pinned fixture and a standing
# gate already naming it. The discriminator is IMPORTED here too.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "p124-correction-form-marker"))
from cc_version import resolve as _cc_resolve  # noqa: E402


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


def commercial_use(family, low):
    """`P250` — the SECOND question, answered in its own column.

    `OK` · `PROHIBITED` · `UNDETERMINED`. The marker scan runs only where no
    identified family protects the row, which is P250's rule verbatim and the
    half that keeps AGPL-3.0 §6 and the Unlicense out of the prohibited bucket.
    """
    if family in OSI_COMMERCIAL_OK or family in TOKEN_COMMERCIAL_OK:
        return "OK"
    if family and family.startswith("CC-"):
        # The CC token IS the answer: NC and ND are the restrictive elements.
        return "PROHIBITED" if "-NC" in family else "OK"
    if any(m in low for m in NONCOMMERCIAL_MARKERS):
        return "PROHIBITED"
    return "UNDETERMINED"


def classify(text):
    """p305 clause rule + p310's commercial axis. Returns (verdict, family).

    Verdict vocabulary, which is `ACTION p309-R` item 2's three-valued POINTER
    class with `P250`'s axis crossed over it:

      `GRANT`                a grant this payload states, commercial use OK
      `GRANT-NONCOMMERCIAL`  a real grant that excludes the only use a studio has
      `POINTER`              NO grant clause, but the payload NAMES its licence —
                             a grant BY REFERENCE. 🔵 Open as `ACTION p306-R`
                             item 2 for four passes: `GarethManning/education-agent-skills`
                             (`LICENSE` 1 230 B `f952182df4eb`, CC-BY-SA-4.0) read
                             `NO-GRANT-CLAUSE`, which is indistinguishable from
                             all-rights-reserved and is the opposite answer.
      `POINTER-NONCOMMERCIAL`  the same, pointing at a restricted licence
      `RESERVED-NO-GRANT`    "all rights reserved" and no grant
      `NO-GRANT-CLAUSE`      no grant and no family: genuinely unreadable
    """
    low = text.lower()
    has_grant = any(c in low for c in GRANT_CLAUSES)
    reserved = any(m in low for m in RESERVED_MARKERS)
    if not has_grant:
        # 🟢 p310: before giving up, ask whether the payload NAMES a licence.
        # A pointer is a third value, not a missing one.
        named = _titled_family(text) or _cc_resolve(text)
        if named and named not in ("CC-UNVERSIONED",):
            nc = commercial_use(named, low) == "PROHIBITED"
            return ("POINTER-NONCOMMERCIAL" if nc else "POINTER"), named
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
        return _grant_verdict(titled, low), titled
    # 🟢 p310: the CC family is DELEGATED, before any body rung can reach it.
    # `cc_version.resolve()` reads the title line first and the canonical URL
    # second, and consults the CC0 marker on NEITHER channel — on purpose.
    cc = _cc_resolve(text)
    if cc and cc != "CC-UNVERSIONED":
        return _grant_verdict(cc, low), cc
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
    # 🔴 p310: the three CC rungs that used to sit here are GONE. They read
    # `"cc0" in low or "public domain dedication" in low` FIRST, and the CC 4.0
    # boilerplate names CC0 in every file, so `CC-BY-NC-4.0` and `CC-BY-4.0`
    # both graded `CC0-1.0`. The family is resolved above by `p124`'s module,
    # which is the canonical reader for it. Nothing replaces them here: a rung
    # that cannot be reached correctly should not exist.
    elif "polyform noncommercial" in low:
        fam = "PolyForm-Noncommercial-1.0.0"
    elif "redistribution and use in source and binary" in low:
        fam = "BSD"
    elif "isc license" in low:
        fam = "ISC"
    # a grant clause AND a reserved marker = read the body by hand
    if reserved and fam in ("unknown", "MIT"):
        fam += "?CHECK-RESERVED"
    return _grant_verdict(fam, low), fam


# 🔵 p310 — `ACTION p309-R` item 4: THE COPYRIGHT-LINE REGION CHANNEL, with its
# blindness DECLARED per row instead of discovered per pass.
#
# p309 added this channel by hand, measured `1` placement in `5` payloads, and
# recorded the blindness as *"the stock copyleft payloads carry the FSF's
# copyright, so the channel is blind to all four copyleft rows."* 🟢 Measured
# again at p310 over 18 payloads, the boundary is WIDER than copyleft and it is a
# property of the licence FORM: the channel works exactly where the licence text
# has a FILL-IN holder slot, and is blind wherever the text is a FIXED DOCUMENT
# that merely uses the word "copyright" in its own prose.
#
#   MIT / BSD / ISC         fill-in slot  → 13 of 13 payloads yielded a holder
#   Apache-2.0             fixed document → 0 of 3.  The first match is Apache's
#                          own definition, *"'Licensor' shall mean the copyright
#                          owner or entity authorized by..."* — not a holder
#   CC 4.0 legalcode       fixed document → 0 of 2
#   PolyForm               fixed document → 0 of 1  (`## Copyright License`)
#   GPL / AGPL stock       fixed document → p309's four rows, FSF boilerplate
#
# 🔴 AND THE YIELD THAT MATTERS IS LOWER THAN THE MATCH RATE. A personal name
# places nobody — p309's own standard. Of the 13 holder lines, exactly TWO are
# INSTITUTIONAL: `The Regents of the University of California`
# (`BridgeSuite/GradeBridge-Student-Submission` → North America) and
# `Sejong University` (`MORSHEDMDMONOARUL/ExamShield` → APAC). 🟢 **2 of 18 =
# 11 % first-hand institutional placement**, and the other 11 are `PERSON`, which
# is reported as such rather than as a region.
FIXED_DOCUMENT_FAMILIES = ("Apache-2.0", "CC-", "CC0", "PolyForm", "GPL", "LGPL",
                           "AGPL", "MPL-2.0", "EPL-2.0", "ECL-2.0")

INSTITUTION_MARKERS = ("university", "universit", "institute", "college", "school",
                       "regents", "universidad", "universidade", "universität",
                       "hochschule", "polytechnic", "akademie", "academy",
                       "ministry", "foundation", "laborator", "research cent",
                       "inc.", "ltd", "gmbh", "b.v.", "corporation", "s.a.")


def holder_line(text, family):
    """(`grade`, `line`) for the copyright-line region channel.

    Grades: `INSTITUTION` (a placeable holder) · `PERSON` (a holder that places
    nobody) · `BLIND-FIXED-DOCUMENT` (the family's text has no holder slot, so a
    "copyright" match is the licence's own prose) · `NO-LINE`.

    🔵 The blindness is decided from the FAMILY, before the text is searched, so
    the output can never pass off a boilerplate sentence as a holder — which is
    what a bare grep does on every Apache-2.0 payload.
    """
    if family and any(family.startswith(f) or f in family
                      for f in FIXED_DOCUMENT_FAMILIES):
        return "BLIND-FIXED-DOCUMENT", "-"
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if "copyright" not in line.lower():
            continue
        low = line.lower()
        grade = ("INSTITUTION" if any(m in low for m in INSTITUTION_MARKERS)
                 else "PERSON")
        return grade, line[:120]
    return "NO-LINE", "-"


def _grant_verdict(family, low):
    """`GRANT` or `GRANT-NONCOMMERCIAL` — P250's axis, on an established grant."""
    return ("GRANT-NONCOMMERCIAL"
            if commercial_use(family, low) == "PROHIBITED" else "GRANT")


def main():
    slugs = [l.strip() for l in open(sys.argv[1]) if l.strip() and not l.startswith("#")]
    out = open(sys.argv[2], "w")
    out.write("slug\tbranch\tfile\thttp\tbytes\tsha256_12\tverdict\tfamily"
              "\tholder_grade\tholder_line\n")
    for slug in slugs:
        found = False
        for branch in BRANCHES:
            if found:
                break
            for name in NAMES:
                code, body = fetch(slug, branch, name)
                # 🔴 p310 — `EMPTY-GRANT-FILE`, a class this base had not recorded,
                # found by the clone channel rather than by this prober.
                # `danialtranz/sentinel-agent-proctoring` serves `LICENSE` at
                # `main` with **HTTP 200 and ZERO BYTES** (sha256 `e3b0c44298fc`,
                # the empty-string digest). The guard below was `if code == "200"
                # and body:` — an empty body is falsy, so the row fell through
                # every remaining candidate and was written to the evidence store
                # as `404 / NO_PAYLOAD`. 🔴 **That cell was FALSE**: the resource
                # exists and returns 200.
                #
                # 🔵 And the distinction is not pedantry. A repository with a
                # zero-byte `LICENSE` reads as LICENSED to GitHub's UI and to any
                # "is there a licence file?" check, while granting nothing at all
                # — the `p304` class (*"a file named LICENSE that withholds every
                # right"*) in its degenerate form. A studio screening by file
                # presence would clear it.
                if code == "200" and not body:
                    row = (f"{slug}\t{branch}\t{name}\t200\t0\t"
                           f"e3b0c44298fc\tEMPTY-GRANT-FILE\t-\tNO-LINE\t-")
                    print(row, flush=True)
                    out.write(row + "\n")
                    found = True
                    break
                if code == "200" and body:
                    text = body.decode("utf-8", "replace")
                    verdict, fam = classify(text)
                    hgrade, hline = holder_line(text, fam)
                    sha = hashlib.sha256(body).hexdigest()[:12]
                    row = (f"{slug}\t{branch}\t{name}\t200\t{len(body)}\t{sha}"
                           f"\t{verdict}\t{fam}\t{hgrade}\t{hline}")
                    print(row, flush=True)
                    out.write(row + "\n")
                    found = True
                    break
        if not found:
            row = f"{slug}\t-\t-\t404\t-\t-\tNO_PAYLOAD\t-\tNO-LINE\t-"
            print(row, flush=True)
            out.write(row + "\n")
    out.close()


if __name__ == "__main__":
    main()
