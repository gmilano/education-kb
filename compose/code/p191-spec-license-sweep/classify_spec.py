#!/usr/bin/env python3
"""P191 -- is a license file a SOFTWARE grant or a SPECIFICATION DOCUMENT license?

Pass 67 found that `1EdTech/openbadges-specification` cedes the IMS Global SPECIFICATION
DOCUMENT LICENSE, whose operative sentence is:

    "No right to create modifications or derivatives of IMS documents is granted
     pursuant to this license."

That is a harder gate than any copyleft this KB has measured: ShareAlike (P178) makes the
derivative inherit terms; this one does not grant the derivative AT ALL.

The classifier answers one question with a quoted sentence, never a guess:

  SPEC-NO-DERIVATIVES  the text denies the right to create modifications or derivatives
  REGISTERED-USERS     the grant is conditioned on membership/registration status
  PERMISSIVE-SOFTWARE  a recognised OSI-permissive software grant (Apache/MIT/BSD/ISC/CC0)
  COPYLEFT-SOFTWARE    GPL/AGPL/LGPL family
  UNCLASSIFIED         none of the above matched -> READ IT, do not infer

A file can carry two marks (the IMS license denies derivatives AND conditions on
registration).  They are emitted together because they are different obligations.
"""
import os
import re, sys

DENY = re.compile(r"no right to create (?:modifications|derivatives)[^.]*", re.I | re.S)
REG = re.compile(r"registered user", re.I)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "p150-gpl-affero-discrimination"))
from gpl_affero import title_licence as _title_licence  # noqa: E402
from gpl_affero import title_version as _title_version  # noqa: E402


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

FAMS = [
    ("PERMISSIVE-SOFTWARE", "Apache-2.0", re.compile(r"Apache License\s*,?\s*Version 2\.0", re.I)),
    ("PERMISSIVE-SOFTWARE", "MIT", re.compile(r"^\s*MIT License", re.I | re.M)),
    ("PERMISSIVE-SOFTWARE", "0BSD", re.compile(r"BSD Zero Clause", re.I)),
    ("PERMISSIVE-SOFTWARE", "ISC", re.compile(r"ISC License", re.I)),
    ("PERMISSIVE-SOFTWARE", "CC0", re.compile(r"CC0 1\.0|Creative Commons Zero", re.I)),
    ("COPYLEFT-SOFTWARE", "AGPL-3.0", re.compile(r"GNU AFFERO GENERAL PUBLIC LICENSE", re.I)),
    ("COPYLEFT-SOFTWARE", "GPL-3.0", re.compile(r"GNU GENERAL PUBLIC LICENSE", re.I)),
    ("PERMISSIVE-SOFTWARE", "CC-BY-4.0", re.compile(r"Creative Commons Attribution 4\.0", re.I)),
]

def classify(text):
    marks, quote, fam = [], "", "-"
    m = DENY.search(text)
    if m:
        marks.append("SPEC-NO-DERIVATIVES")
        quote = " ".join(m.group(0).split())[:160]
        fam = "SPEC-LICENSE"
    if REG.search(text):
        marks.append("REGISTERED-USERS")
    # 🔴 p309: the GNU half of `FAMS` is a body search, and its AGPL rung —
    # `re.compile(r"GNU AFFERO GENERAL PUBLIC LICENSE", re.I)` — is the pattern
    # `p150-gpl-affero-discrimination` pins as `NAIVE_AGPL`, its own NEGATIVE
    # control.  Ordered before the GPL-3.0 rung, it grades every GPL-3.0 payload
    # `AGPL-3.0`, because GPL-3.0 §13 is titled "Use with the GNU Affero General
    # Public License".  Measured at p309 against the real 35 191 B payload:
    # `('COPYLEFT-SOFTWARE', 'AGPL-3.0')`.  🟢 The title read is IMPORTED from
    # p150 and tried FIRST; the body ladder still answers for everything else.
    if not marks:
        titled = _titled_family(text)
        if titled:
            cls = ("COPYLEFT-SOFTWARE" if titled.startswith(("GPL", "AGPL", "LGPL"))
                   else "PERMISSIVE-SOFTWARE")
            return cls, titled, quote
    if not marks:
        for cls, name, rx in FAMS:
            if rx.search(text):
                marks.append(cls); fam = name; break
    if not marks:
        marks.append("UNCLASSIFIED")
    return "+".join(marks), fam, quote

if __name__ == "__main__":
    body = sys.stdin.read()
    verdict, fam, quote = classify(body)
    print(f"{verdict}\t{fam}\t{len(body.encode())}\t{quote}")
