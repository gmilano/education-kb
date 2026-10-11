#!/usr/bin/env python3
"""The p126 repair: one missing column spelling, and the marks it unblocks.

`P126-B` found that p125's own defect table -- the one reporting three live
false claims -- is not recognised as a correction table at all. Its old column
is headed *"the page said"*, and `HDR_OLD` carries `this KB said`, `KB said`
and `pNNN said` but not that spelling. The table was copied onto nine pages,
so its quoted OLD values read as live claims and the corpus's own assertion
re-raises them.

The repair is three alternatives added to `HDR_OLD`. Nothing else changes: the
writer is p125's own `mark_forms.apply_marks`, which carries the `APPARATUS`
guard and the `_past_emphasis` rule.

🔴 `correction_form.apply_marks` is NOT the writer to use. It has no
`APPARATUS` guard, and run with this patch it marks p125's own prose ABOUT
the marker -- *"(`⚠️ **was 🟢 MIT**` inside the cell)"* -- which is the exact
false-positive class p125's fourth defect fixed. Two such lines were marked
and reverted before this module was pointed at `mark_forms`.

`--apply` writes; the default is a dry run.

usage: repair.py [--apply] PAGE...
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "p125-retraction-cue"))
import correction_form as cf                               # noqa: E402
import mark_forms                                          # noqa: E402

# The spellings p125 invented and did not teach its own recogniser. Named, so
# the next pass can see exactly what was added and why.
ADDED = (
    r"the page said",
    r"the (?:shelf|row|cell|table) said",
    r"as published",
)


def patch_header_vocabulary():
    cf.HDR_OLD = re.compile(
        cf.HDR_OLD.pattern + r"|\b(?:" + r"|".join(ADDED) + r")\b", re.I)


def main(argv):
    apply_ = "--apply" in argv
    pages = [a for a in argv if not a.startswith("-")]

    base = {p: len(mark_forms.table_hits(p)) for p in pages}
    patch_header_vocabulary()

    total, forms = 0, {}
    print("# %-26s %12s %12s %8s"
          % ("page", "tbl-before", "tbl-after", "marked"))
    for p in pages:
        after = len(mark_forms.table_hits(p))
        n, byform = mark_forms.apply_marks(p, dry=not apply_)
        total += n
        for k, v in byform.items():
            forms[k] = forms.get(k, 0) + v
        print("# %-26s %12d %12d %8d" % (p, base[p], after, n))
    print("# %-26s %12s %12s %8d" % ("TOTAL", "", "", total))
    print("# by form: %s"
          % ", ".join("%s=%d" % kv for kv in sorted(forms.items())))
    print("# mode = %s" % ("APPLIED" if apply_ else "dry run"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
