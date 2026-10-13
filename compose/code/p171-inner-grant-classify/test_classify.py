#!/usr/bin/env python3
"""Regression tests for P171-A. Every case here is a body p171 actually read in Sakai or Moodle,
and the first three are the three the first attempt got WRONG."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import classify  # noqa: E402


def fam(body):
    return classify.classify(body)[0]


def mentions(body):
    return classify.classify(body)[3]


LGPL21 = """                  GNU LESSER GENERAL PUBLIC LICENSE
                       Version 2.1, February 1999

 Copyright (C) 1991, 1999 Free Software Foundation, Inc.

  This license, the Lesser General Public License, applies to some
specially designated software packages.

  3. You may opt to apply the terms of the ordinary GNU General Public
License instead of this License to a given copy of the Library.
"""

IPL10 = """IBM Public License Version 1.0
THE ACCOMPANYING PROGRAM IS PROVIDED UNDER THE TERMS OF THIS IBM PUBLIC LICENSE
1. DEFINITIONS
"Contribution" means:
Programs licensed under the Mozilla Public License or the Common Public License
are not covered by this Agreement.
"""

MIT = """Copyright (c) 2011 Example
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction.
"""

APACHE_FULL = """                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
"""

GPL2 = """                    GNU GENERAL PUBLIC LICENSE
                       Version 2, June 1991

 Copyright (C) 1989, 1991 Free Software Foundation, Inc.
"""

NONCOMMERCIAL = """Copyright (c) 2020 Example Corp
This font may be used for non-commercial purposes only.
All Rights Reserved.
"""


def test_lgpl_is_not_also_gpl():
    """The defect that made this rewrite necessary: LGPL-2.1 section 3 names the ordinary GPL."""
    assert fam(LGPL21) == ["LGPL"], fam(LGPL21)
    assert "GPL" in mentions(LGPL21), mentions(LGPL21)


def test_wrapped_phrase_is_still_found():
    """The second defect, caught by this test file: legal text is hard-wrapped, so the phrase
    "GNU General Public License" appears split across a line break. A flat search misses it."""
    wrapped = LGPL21.replace("ordinary GNU General Public\nLicense",
                             "ordinary GNU General Public\nLicense")
    assert "GNU General Public\nLicense" in wrapped
    assert "GPL" in mentions(wrapped), mentions(wrapped)


def test_ipl_is_recognised_and_not_mpl_or_cpl():
    """junit-3.8.1.license.txt. The first attempt said GPL+MPL+Python; it is IPL-1.0."""
    assert fam(IPL10) == ["IPL-1.0"], fam(IPL10)
    assert set(mentions(IPL10)) >= {"MPL", "CPL"}, mentions(IPL10)


def test_mit_sentence_grant():
    assert fam(MIT) == ["MIT"], fam(MIT)


def test_apache_full_text_by_title():
    assert fam(APACHE_FULL) == ["Apache-2.0"], fam(APACHE_FULL)


def test_real_gpl_still_detected():
    """Guard the other direction: suppressing GPL inside LGPL must not blind the gate to real GPL."""
    assert fam(GPL2) == ["GPL"], fam(GPL2)


GPL3_S6 = """                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

  b) Convey the object code in, or embodied in, a physical product
  accompanied by a written offer. This alternative is allowed only
  occasionally and noncommercially, and only if you received the object
  code with such an offer.
"""


def test_gpl3_section6_is_not_a_noncommercial_restriction():
    """4 of Moodle's 6 raw hostile hits were this clause, Moodle's own COPYING.txt among them."""
    fams, hostile, _e, _m = classify.classify(GPL3_S6)
    assert fams == ["GPL"], fams
    assert hostile == [], hostile


MD_APACHE = """# Apache License
Version 2.0, January 2004

## 1. Definitions.
"License" shall mean the terms and conditions for use, reproduction, and distribution.
"""

MD_GPL_SHORTFORM = """# Software License Agreement

**TinyMCE**
Copyright (c) 2024, Ephox Corporation

Licensed under the terms of [GNU General Public License Version 2 or later](http://gnu.org/).
"""


def test_markdown_heading_title_is_found():
    """Moodle's bundled aws-sdk/LICENSE is Apache-2.0 written as Markdown."""
    assert fam(MD_APACHE) == ["Apache-2.0"], fam(MD_APACHE)


def test_gnu_short_form_notice_is_a_grant():
    """Moodle's bundled TinyMCE: a 300-byte license.md pointing at gnu.org."""
    assert fam(MD_GPL_SHORTFORM) == ["GPL"], fam(MD_GPL_SHORTFORM)


def test_hostile_noncommercial_flagged():
    _f, hostile, _e, _m = classify.classify(NONCOMMERCIAL)
    assert "non-commercial" in hostile, hostile


if __name__ == "__main__":
    passed = failed = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"PASS {name}")
                passed += 1
            except AssertionError as e:
                print(f"FAIL {name}: {e}")
                failed += 1
    print(f"\n{passed} passed, {failed} failed")
    raise SystemExit(1 if failed else 0)
