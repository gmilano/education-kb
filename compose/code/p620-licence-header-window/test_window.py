#!/usr/bin/env python3
"""Suite for `p620`. No network: every case is a literal payload fragment.

Each case states what it is FOR. The two that matter most are the negative controls,
because a repair that strips markup can always be made to "work" by stripping more,
and the way it breaks is by eating the words `familia()` needs.
"""
import sys

from probe_window import classify, unwrap

# GPL-2.0, the shape `idempiere/idempiere` ships at `HEAD/LICENSE.md`: the title is a
# Markdown heading, the version line follows, and the copyright block is inside <pre>.
MD_GPL2 = """<center>

# GNU General Public License

Version 2, June 1991

<pre>Copyright (C) 1989, 1991 Free Software Foundation, Inc.
59 Temple Place - Suite 330, Boston, MA  02111-1307, USA
  </pre>
</center>

## Preamble

(Some other Free Software Foundation software is covered by the GNU Library General
Public License instead.)  You can apply it to your programs, too.
"""

# The same project's `HEAD/license.html`, whose FIRST named licence is not the grant.
HTML_TWO_NAMES = """<html><body>
<h2>Compiere Public License</h2>
<h2>GNU General Public License</h2>
<p>Version 2, June 1991</p>
<p>Copyright (C) 1989, 1991 Free Software Foundation, Inc.</p>
"""

# Plain text, the shape the window was measured on. Must be untouched by the repair.
PLAIN_GPL3 = """                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>

  13. Use with the GNU Affero General Public License.
"""

PLAIN_MIT = """MIT License

Copyright (c) 2017 MicroPyramid

Permission is hereby granted, free of charge, to any person obtaining a copy
"""

# NEGATIVE CONTROL 1 -- the repair must not manufacture a version that is not there.
MD_GPL_NO_VERSION = """<center>

# GNU General Public License

<pre>Copyright (C) 1989, 1991 Free Software Foundation, Inc.</pre>
</center>
"""

# NEGATIVE CONTROL 2 -- `P419`'s own defect must stay detectable through the repair.
# A pristine GPL-3.0 names AGPL in section 13; if the repair widened the window, the
# body would re-enter it and this case would come back AGPL.
MD_GPL3_MENTIONS_AGPL = """# GNU General Public License

Version 3, 29 June 2007

## 13. Use with the GNU Affero General Public License

Notwithstanding any other provision of this License, you have permission to link or
combine any covered work with a work licensed under version 3 of the GNU Affero
General Public License into a single combined work.
"""

CASES = [
    # (label, payload, expected verdict, expected raw, expected unwrapped)
    ("markdown-wrapped GPL-2.0 (idempiere LICENSE.md shape): version is OUTSIDE the "
     "n=2 window, and the repair recovers it",
     MD_GPL2, "REPAIRED", "GPL-?", "GPL-2.0"),
    # 🔴 Measured, and WORSE than this suite first predicted. The raw read does not
    # merely lose the version: the two lines it admits are `<html><body>` and the
    # Compiere title, so NO family matches and the answer is UNCLASSIFIED. The repair
    # moves the read onto two licence TITLES, which still leaves `Version 2` outside
    # the window. This is the folder's declared blind spot, kept red-flagged rather
    # than cured by widening the window.
    ("HTML payload naming TWO licences (idempiere license.html shape): raw answers NO "
     "family at all; the repair reaches GPL but the version is STILL outside the window",
     HTML_TWO_NAMES, "WINDOW-STILL-SHORT", "UNCLASSIFIED", "GPL-?"),
    ("plain-text GPL-3.0: the shape the window WAS measured on -- the repair is a no-op",
     PLAIN_GPL3, "AGREE", "GPL-3.0", "GPL-3.0"),
    ("plain-text MIT: a permissive payload must survive the repair unchanged",
     PLAIN_MIT, "AGREE", "MIT", "MIT"),
    ("NEGATIVE CONTROL -- markdown GPL with NO version line anywhere: the repair must "
     "return GPL-? and must NOT invent a version (`P286`)",
     MD_GPL_NO_VERSION, "AGREE", "GPL-?", "GPL-?"),
    # 🔵 This case also CORRECTS what this folder first claimed the defect was. A `#`
    # heading does NOT break the window: `_encabezado` collapses whitespace and the
    # version line is still the second non-empty line, so the raw read already answers
    # GPL-3.0. The defect needs a markup line BEFORE the title -- `<center>` in
    # idempiere's real `LICENSE.md` -- which is what case 1 carries. Markdown as such
    # is not the axis; an extra non-empty line between title and version is.
    ("NEGATIVE CONTROL -- markdown GPL-3.0 whose BODY names AGPL (`P419`'s defect): "
     "both reads must answer GPL-3.0, proving the repair did not widen the window",
     MD_GPL3_MENTIONS_AGPL, "AGREE", "GPL-3.0", "GPL-3.0"),
]


def main():
    ok = 0
    total = 0
    for label, payload, exp_v, exp_raw, exp_un in CASES:
        verdict, raw, un = classify(payload)
        for got, exp, what in ((verdict, exp_v, "verdict"),
                               (raw, exp_raw, "raw"),
                               (un, exp_un, "unwrapped")):
            total += 1
            if got == exp:
                ok += 1
            else:
                print("🔴 %-9s got %-10r expected %-10r  -- %s" % (what, got, exp, label))
        if (verdict, raw, un) == (exp_v, exp_raw, exp_un):
            print("🟢 %-9s raw=%-8s unwrapped=%-8s  %s" % (verdict, raw, un, label))

    # The repair must not INVENT words, and must not DELETE licence-naming ones.
    # 🔴 The first version of this control split on whitespace and went red on every
    # markup case -- wrongly. `<pre>Copyright` is ONE whitespace token before the
    # strip and `Copyright` after it, so a legitimate strip looks like an invention.
    # The control was mis-specified, not the code: words are `[A-Za-z]+` runs, which
    # is what `familia()` actually matches on, and tag-splitting is invisible to that.
    import re as _re
    words = lambda t: set(w.lower() for w in _re.findall(r"[A-Za-z]+", t))  # noqa: E731
    for label, payload, _, _, _ in CASES:
        before, after = words(payload), words(unwrap(payload))
        total += 1
        if after <= before:
            ok += 1
        else:
            print("🔴 unwrap INVENTED words %r -- %s" % (sorted(after - before), label))
        # And the words that decide a family must survive the strip.
        total += 1
        keep = {w for w in before if w in {
            "general", "public", "license", "licence", "affero", "lesser", "apache",
            "mozilla", "eclipse", "mit", "version", "copyright"}}
        if keep <= after:
            ok += 1
        else:
            print("🔴 unwrap DELETED family words %r -- %s" % (sorted(keep - after), label))

    print("\n%d/%d assertions green" % (ok, total))
    return 0 if ok == total else 1


if __name__ == "__main__":
    sys.exit(main())
