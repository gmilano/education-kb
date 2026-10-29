"""Title-block-anchored grant classifier (p525).

WHY THIS EXISTS
  `ingest/probe-grant.sh` is this base's STANDING grant probe (built p517 to close
  Gap 516-A).  Its `spdx_of()` classifies on a BODY SCAN of the first 4 KB.  p490
  already recorded the rule that defeats a body scan -- "anchor the family on the
  title block" -- and fixed it in a different, one-off reader.  The standing probe
  never got the fix, and p525 measured the consequence on the three grants p520
  REFUSED for paid client work:

    CaviraOSS/PageLM          -> probe says `MIT`          (it is a bespoke licence
                                 that PROHIBITS redistribution and demands revenue
                                 share; the MIT branch matches its opening sentence)
    xiaoyang111222/cn-math-taxonomy
                              -> probe says `CC-BY-4.0`    (title line reads
                                 "Attribution-NonCommercial 4.0 International")
    canyongbs/advisingapp     -> probe says `unknown-text`  (title line reads
                                 "Elastic License 2.0")

  One cause, three instances: the family is ON THE TITLE LINE in all three cases and
  the probe never reads it.  The GNU branches in `spdx_of()` survive only by accident
  -- their patterns are UPPERCASE and bash `case` is case-sensitive, so they match a
  title block and not a mixed-case preamble cross-reference.  Remove that accident
  (`shopt -s nocasematch`, or a lowercasing pre-pass) and every GPL-2.0 payload on
  these shelves grades LGPL.

WHAT IT GUARANTEES
  1. The family is read from the TITLE BLOCK (first 200 bytes, p490's anchor) first.
  2. A title block naming a licence outside the canonical permissive/copyleft set is
     reported as BESPOKE-*, never as a canonical SPDX id.  A grant may open with the
     MIT sentence and then revoke it; the title line is what it calls itself.
  3. NonCommercial is read as part of the family, not dropped.
  4. When there is NO title line -- expertiza's grant is MIT with no title (T43) --
     it falls back to the body and says so: `MIT (BY-BODY)`, a lower-confidence
     verdict, never silently equal to a title-attested MIT.
  5. It abstains (`UNREADABLE`) rather than guessing.
"""

CANONICAL_TITLES = [
    # (needle on the title block, family)  -- ORDER MATTERS, longest/most specific first
    ("attribution-noncommercial-sharealike", "CC-BY-NC-SA-4.0"),
    ("attribution-noncommercial",            "CC-BY-NC-4.0"),
    ("attribution-sharealike",               "CC-BY-SA-4.0"),
    ("gnu affero general public license",    "AGPL-3.0"),
    ("gnu lesser general public license",    "LGPL"),
    ("gnu library general public license",   "LGPL"),
    ("gnu general public license",           "GPL"),
    ("apache license",                       "Apache-2.0"),
    ("mit license",                          "MIT"),
    ("bsd 3-clause",                         "BSD-3-Clause"),
    ("bsd 2-clause",                         "BSD-2-Clause"),
    ("mozilla public license",               "MPL-2.0"),
    ("elastic license 2.0",                  "Elastic-2.0"),
    ("elastic license",                      "Elastic-2.0"),
    ("server side public license",           "SSPL"),
    ("business source license",              "BUSL-1.1"),
    ("the unlicense",                        "Unlicense"),
    ("creative commons zero",                "CC0-1.0"),
    ("cc0 1.0",                              "CC0-1.0"),
    ("attribution 4.0 international",        "CC-BY-4.0"),
]

# A title line that contains one of these AND no canonical family is a bespoke grant.
BESPOKE_MARKERS = ("license", "licence", "licencia", "licença", "lizenz", "terms")

NC_MARKERS = ("noncommercial", "non-commercial", "not for commercial")

GPL_VERSIONS = (("version 2, june 1991", "-2.0"), ("version 3, 29 june 2007", "-3.0"))


def title_block(payload: str, nbytes: int = 200) -> str:
    """p490's anchor: the first 200 bytes, markdown heading marks stripped."""
    head = payload[:nbytes]
    lines = [l.strip().lstrip("#").strip().strip("*").strip()
             for l in head.splitlines()]
    return "\n".join(l for l in lines if l)


def _version_suffix(family: str, payload: str) -> str:
    if family not in ("GPL", "LGPL", "AGPL-3.0"):
        return family
    low = payload[:4000].lower()
    for needle, suffix in GPL_VERSIONS:
        if needle in low:
            return (family + suffix) if family != "AGPL-3.0" else family
    return family + "-?" if family in ("GPL", "LGPL") else family


def classify(payload: str):
    """-> (family, confidence, why).  Never raises on odd input."""
    if not payload or not payload.strip():
        return ("UNREADABLE", "none", "empty payload")

    tb = title_block(payload)
    tb_low = tb.lower()

    for needle, family in CANONICAL_TITLES:
        if needle in tb_low:
            fam = _version_suffix(family, payload)
            # NC can sit outside the matched needle (e.g. a CC title spread over lines)
            if fam.startswith("CC-BY") and "nc" not in fam.lower():
                if any(m in tb_low for m in NC_MARKERS):
                    fam = fam.replace("CC-BY", "CC-BY-NC")
            return (fam, "title-attested", f"title block matched {needle!r}")

    # Title block exists and calls itself a licence, but names no canonical family:
    # this is a bespoke grant.  REFUSE to emit a canonical SPDX id for it, however
    # the body opens.  (PageLM opens with the MIT sentence and then revokes it.)
    first = tb.splitlines()[0] if tb.splitlines() else ""
    if any(m in first.lower() for m in BESPOKE_MARKERS):
        nc = any(m in payload[:9000].lower() for m in NC_MARKERS)
        tag = "BESPOKE-NONCOMMERCIAL" if nc else "BESPOKE"
        return (tag, "title-attested", f"title names a non-canonical grant: {first!r}")

    # No usable title line.  expertiza's MIT has none (T43).  Fall back to the body,
    # and SAY SO -- a body verdict is not a title verdict.
    body = payload[:4000]
    if "Permission is hereby granted, free of charge" in body:
        nc = any(m in payload[:9000].lower() for m in NC_MARKERS)
        if nc:
            return ("BESPOKE-NONCOMMERCIAL", "body-only",
                    "MIT sentence present but payload restricts commercial use")
        return ("MIT (BY-BODY)", "body-only", "MIT grant sentence, no title line")
    if "Redistribution and use in source and binary forms" in body:
        fam = "BSD-3-Clause" if "Neither the name" in body else "BSD-2-Clause"
        return (f"{fam} (BY-BODY)", "body-only", "BSD conditions, no title line")
    return ("UNREADABLE", "none", f"no canonical title and no known grant sentence; title block={first!r}")


if __name__ == "__main__":
    import sys
    for path in sys.argv[1:]:
        with open(path, encoding="utf-8", errors="replace") as fh:
            fam, conf, why = classify(fh.read())
        print(f"{path}\t{fam}\t{conf}\t{why}")
