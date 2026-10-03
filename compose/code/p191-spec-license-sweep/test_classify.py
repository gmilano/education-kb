#!/usr/bin/env python3
"""Suite for P191's classifier.  The negative controls matter more than the positives here:
a permissive software grant must NEVER be marked SPEC-NO-DERIVATIVES, because that mark is
what tells a studio it cannot publish a derived profile."""
import sys
from classify_spec import classify

IMS = ("IMS GLOBAL LEARNING CONSORTIUM, INC. SPECIFICATION DOCUMENT LICENSE\n"
       "Use of this specification is subject to this license. Registered Users may ...\n"
       "No right to create modifications or derivatives of IMS documents is granted "
       "pursuant to this license.\n")
APACHE = "Apache License\nVersion 2.0, January 2004\nhttp://www.apache.org/licenses/\n"
MIT = "MIT License\n\nCopyright (c) 2026 bunizao\n\nPermission is hereby granted,\n"
AGPL = "GNU AFFERO GENERAL PUBLIC LICENSE\nVersion 3, 19 November 2007\n"
CCBY = "Creative Commons Attribution 4.0 International Public License\n"
ZBSD = "BSD Zero Clause License\n\nCopyright (c) 2025 Bjorn Pagen\n"

CASES = [
    ("IMS spec license -> denies derivatives AND registration", IMS,
     "SPEC-NO-DERIVATIVES+REGISTERED-USERS", "SPEC-LICENSE"),
    ("Apache-2.0 must NOT be marked spec", APACHE, "PERMISSIVE-SOFTWARE", "Apache-2.0"),
    ("MIT must NOT be marked spec", MIT, "PERMISSIVE-SOFTWARE", "MIT"),
    ("AGPL is copyleft, not spec", AGPL, "COPYLEFT-SOFTWARE", "AGPL-3.0"),
    ("CC BY 4.0 is permissive data, not spec", CCBY, "PERMISSIVE-SOFTWARE", "CC-BY-4.0"),
    ("0BSD recognised (the @eduware/oneroster payload)", ZBSD, "PERMISSIVE-SOFTWARE", "0BSD"),
    ("empty text is UNCLASSIFIED, never guessed", "", "UNCLASSIFIED", "-"),
    ("prose mentioning derivatives WITHOUT the denial is not the mark",
     "You may create derivatives of this work freely.\nMIT License\n", "PERMISSIVE-SOFTWARE", "MIT"),
]

def main():
    bad = 0
    for name, text, exp_v, exp_f in CASES:
        v, f, q = classify(text)
        ok = (v == exp_v and f == exp_f)
        if not ok: bad += 1
        print(f"{'PASS' if ok else 'FAIL'}  {name}\n      got=({v}, {f})  expected=({exp_v}, {exp_f})")
    if bad:
        print(f"\n{bad} FAILED"); sys.exit(1)
    print(f"\nall {len(CASES)} cases pass")

if __name__ == "__main__":
    main()
