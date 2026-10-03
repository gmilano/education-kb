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
import re, sys

DENY = re.compile(r"no right to create (?:modifications|derivatives)[^.]*", re.I | re.S)
REG = re.compile(r"registered user", re.I)
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
