#!/usr/bin/env python3
"""Offline controls for `probe_p307.classify_payload`.

Every fixture is an ABBREVIATED but verbatim fragment of a payload this base
has pinned by bytes, plus the three defects this instrument was caught on
before publication.  No network: runnable wherever `make hooks` runs.

Run from this directory (`p355-cwd-portability`): `python3 test_probe_p307.py`
"""
import sys
from probe_p307 import classify_payload as C

MIT = (b"MIT License\n\nCopyright (c) 2025 Someone\n\nPermission is hereby "
       b"granted, free of charge, to any person obtaining a copy\n")
APACHE_HEAD = (b"\n                                 Apache License\n"
               b"                           Version 2.0, January 2004\n"
               b"                        http://www.apache.org/licenses/\n\n"
               b"2. Grant of Copyright License. Subject to the terms, each "
               b"Contributor hereby\ngrants to You a perpetual, worldwide, "
               b"non-exclusive, no-charge, royalty-free\n")
GPL2 = (b"                    GNU GENERAL PUBLIC LICENSE\n"
        b"                       Version 2, June 1991\n\n"
        b"library.  If this is what you want to do, use the GNU Lesser "
        b"General\nPublic License instead of this License.\n")
AGPL3 = (b"                    GNU AFFERO GENERAL PUBLIC LICENSE\n"
         b"                       Version 3, 19 November 2007\n")
# p307's headline defect: this title, at 35 148 B, was carried as AGPL-3.0 for
# two passes because its LENGTH sat in a series the base had labelled AGPL.
GPL3 = (b"                    GNU GENERAL PUBLIC LICENSE\n"
        b"                       Version 3, 29 June 2007\n")
BSD3 = (b"BSD 3-Clause License\n\nRedistribution and use in source and binary "
        b"forms, with or without\nmodification, are permitted provided that "
        b"the following conditions are met:\n\n" + b"x" * 700 +
        b"\n* Neither the name of the copyright holder nor the names of its\n")
RESERVED = (b"Copyright (c) 2025 ShuyunYuan. All rights reserved.\n\n"
            b"This code is provided for portfolio and code-review purposes "
            b"only.\n\nTHE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY "
            b"OF ANY KIND\n")
POINTER_W3C = (b"All documents in this Repository are licensed by "
               b"contributors under the\n"
               b"[W3C Software and Document License]"
               b"(https://www.w3.org/Consortium/Legal/copyright-software).\n")
POINTER_CC = (b"Creative Commons Attribution-ShareAlike 4.0 International\n\n"
              b"This is a human-readable notice. The full legal terms are "
              b"available at:\nhttps://creativecommons.org/licenses/by-sa/4.0/"
              b"legalcode\n")
TREE_LISTING = (b"tree HEAD:Licenses\n\nApache License 2.0.pdf\nBSD License."
                b"pdf\nGNU General Public License.pdf\n"
                b"GNU Lesser General Public License.pdf\n")

CASES = [
    # (name, payload, verdict, family)
    ("MIT", MIT, "GRANT", "MIT"),
    # p307 defect 1 — the clause line-wraps; a raw-bytes matcher called this
    # a POINTER because "hereby" and "grants to You" straddle a newline.
    ("Apache-2.0 wrapped clause", APACHE_HEAD, "GRANT", "Apache-2.0"),
    # p307 defect 3 — GPL-2.0 recommends the Lesser licence in its own text.
    ("GPL-2.0 not LGPL", GPL2, "GRANT", "GPL-2.0"),
    ("AGPL-3.0", AGPL3, "GRANT", "AGPL-3.0"),
    ("GPL-3.0 not AGPL-3.0", GPL3, "GRANT", "GPL-3.0"),
    # BSD-3's discriminator is ~900 B in, behind BSD-2's shared sentence.
    ("BSD-3 not BSD-2", BSD3, "GRANT", "BSD-3-Clause"),
    # p305's trap: a reserved grant closing with MIT's warranty paragraph.
    ("reserved grant", RESERVED, "RESERVED", "—"),
    # p306's fourth class, and p307's finding that it is not rare.
    ("pointer (W3C)", POINTER_W3C, "POINTER", "—"),
    ("pointer (CC deed)", POINTER_CC, "POINTER", "—"),
]

def main():
    bad = 0
    for name, payload, want_v, want_f in CASES:
        v, f, note = C(payload)
        ok = (v == want_v and f == want_f)
        bad += not ok
        print(f"{'🟢' if ok else '🔴'} {name:28} -> {v}/{f}" +
              ("" if ok else f"  EXPECTED {want_v}/{want_f}"))
    # p307 defect 2 is structural, not a classifier case: `Licenses` is a
    # DIRECTORY and `git show` printed its index.  The control is that the
    # text of a tree listing must never be graded as a grant by accident --
    # it is recorded here so the next reader sees what the string looks like.
    v, f, _ = C(TREE_LISTING)
    tree_ok = v == "GRANT"
    print(f"{'⚠️' if tree_ok else '🟢'} {'directory index':28} -> {v}/{f}"
          "   (classifier CANNOT tell; the fix is blob-only ls-tree upstream)")
    print(f"\n{len(CASES) - bad}/{len(CASES)} classifier controls green")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main())
