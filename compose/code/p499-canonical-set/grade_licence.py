#!/usr/bin/env python3
"""p499 — grade a LONE licence payload against a retained canonical set.

Gap 498-B asked for a retained canonical set so that a single altered payload,
read with nothing to compare it to, can still be caught. Gap 498-M asked that a
gate be validated against a known-good AND a known-bad input before it is
trusted.

Why not bytes or blob SHA: the two legitimate canonical forms of Apache-2.0
(apache.org's own, 11 358 B, and SPDX's, 10 280 B) differ by 1 078 bytes of
pure centering whitespace and not one word. Size and SHA therefore cannot
grade a payload. This instrument normalises whitespace and compares the
WORD SEQUENCE, which is the operative body.
"""
import hashlib
import re
import sys
import os
import glob

CANON_DIR = os.environ.get("CANON_DIR", "evidence/canonical")


def git_blob_sha(b: bytes) -> str:
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()


def words(text: str):
    """Lowercase word sequence; whitespace and layout discarded."""
    return re.findall(r"[a-z0-9]+", text.lower())


# Apache-2.0 and the GNU family end with an instructed, fill-in-the-blank
# appendix ("How to apply..."). Replacing yyyy/name there is what the licence
# TELLS the licensor to do, so it is not an alteration. Only the span above it
# is operative. Grading the whole payload conflates the two and calls every
# correctly-applied Apache licence "deviant" -- which is a false positive rate
# of nearly 100%, since almost every real repo fills the placeholder in.
APPENDIX_MARKS = (
    "APPENDIX: How to apply the Apache License",
    "END OF TERMS AND CONDITIONS",
    "How to Apply These Terms to Your New Programs",
)


# MIT/BSD/ISC carry no appendix: their fill-in-the-blank is the copyright
# NOTICE LINE itself ("Copyright (c) <year> <copyright holders>"), which sits
# inside the body. Filling it in is instructed, so grading it as operative
# makes every correctly-applied MIT licence read DEVIANT. Drop notice lines
# from both sides before comparing.
# A notice line must look like a NOTICE: "Copyright (c) <year> <holder>".
# It must carry EITHER an explicit (c)/(C) marker OR a year/placeholder.
# Neither test alone is sound, and each unsound form was caught by a control:
#  * matching any line starting "copyright" deleted GPL-3.0 section 2's
#    operative sentence on 14 independent projects;
#  * additionally accepting a bare word after "copyright" (added to catch
#    Microsoft's yearless "Copyright (c) Microsoft Corporation.") deleted
#    GPL-2.0 section 1's wrapped line "copyright notice and disclaimer of
#    warranty; keep intact all the" on formalms, whose section 1 is in fact
#    word-for-word canonical.
# An earlier form of this stripper matched any line beginning with the word
# "copyright" and therefore deleted GPL-3.0 section 2's operative sentence
# ("...granted for the term of copyright on the Program, and are irrevocable
# provided the stated conditions are met"), which wraps onto its own line in
# the canonical payload. That produced a uniform -22-word "deletion" on
# FOURTEEN independent GPL/AGPL projects -- the tell that the instrument, not
# the projects, was wrong. Requiring a year or a placeholder on the line fixes
# it; the fourteen rows are re-graded IDENTICAL below.
COPYRIGHT_LINE = re.compile(
    r"^[\s>*#/-]*copyright\b[\s:]*"
    r"(?:"
    r"(?:\(c\)|©|\(©\))[\s,]*\S"      # an explicit (c)/(C) marker, then anything
    r"|(?:<[^>\n]{0,40}>|\d{4}|\[?year\]?|yyyy)"  # or a year / placeholder
    r")",
    re.IGNORECASE | re.MULTILINE)
ALL_RIGHTS = re.compile(r"^[\s>*#/-]*all rights reserved\.?\s*$",
                        re.IGNORECASE | re.MULTILINE)


def strip_notice(text: str) -> str:
    """Delete only whole lines that are copyright NOTICES."""
    out = []
    for line in text.splitlines():
        if COPYRIGHT_LINE.match(line) or ALL_RIGHTS.match(line):
            continue
        out.append(line)
    return "\n".join(out)


def split_operative(text: str):
    """Return (operative_span, appendix_span). Cut at the first appendix mark."""
    cut = len(text)
    for m in APPENDIX_MARKS:
        i = text.find(m)
        if i != -1:
            cut = min(cut, i)
    return strip_notice(text[:cut]), text[cut:]


def load_canon():
    canon = {}
    for p in sorted(glob.glob(os.path.join(CANON_DIR, "*.txt"))):
        raw = open(p, "rb").read()
        txt = raw.decode("utf-8", "replace")
        op, ap = split_operative(txt)
        canon[os.path.basename(p)[:-4]] = {
            "path": p, "bytes": len(raw),
            "blob": git_blob_sha(raw),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "words": words(txt),
            "op_words": words(op),
            "has_appendix": bool(ap),
        }
    return canon


def grade(payload: bytes, canon, expect=None, operative_only=True):
    txt = payload.decode("utf-8", "replace")
    key = "op_words" if operative_only else "words"
    w = words(split_operative(txt)[0]) if operative_only else words(txt)
    out = []
    for name, c in canon.items():
        if expect and not name.startswith(expect):
            continue
        cw = c[key]
        if w == cw:
            out.append((name, "IDENTICAL", 0, 0, []))
            continue
        # longest common subsequence is overkill; use a difflib opcode walk
        import difflib
        sm = difflib.SequenceMatcher(None, cw, w, autojunk=False)
        ratio = sm.ratio()
        dele, ins, notes = 0, 0, []
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == "delete":
                dele += i2 - i1
                notes.append("DELETED from canonical: " + " ".join(cw[i1:i2])[:160])
            elif tag == "insert":
                ins += j2 - j1
                notes.append("INSERTED not in canonical: " + " ".join(w[j1:j2])[:160])
            elif tag == "replace":
                dele += i2 - i1
                ins += j2 - j1
                notes.append("REPLACED canonical '%s' -> '%s'"
                             % (" ".join(cw[i1:i2])[:80], " ".join(w[j1:j2])[:80]))
        out.append((name, "DEVIANT" if ratio < 1.0 else "IDENTICAL", dele, ins, notes[:6]))
    out.sort(key=lambda r: (r[1] != "IDENTICAL", r[2] + r[3]))
    return w, out


def main():
    canon = load_canon()
    if not canon:
        sys.exit("no canonical payloads found in %s" % CANON_DIR)
    if len(sys.argv) < 2:
        print("retained canonical set — %d payloads in %s" % (len(canon), CANON_DIR))
        print("%-26s %9s  %-40s %s" % ("licence", "bytes", "git blob sha1", "words"))
        for n, c in canon.items():
            print("%-26s %9d  %-40s %d" % (n, c["bytes"], c["blob"], len(c["words"])))
        return
    for path in sys.argv[1:]:
        raw = open(path, "rb").read()
        w, res = grade(raw, canon, operative_only=True)
        best = res[0]
        _, resf = grade(raw, canon, operative_only=False)
        bestf = [r for r in resf if r[0] == best[0]][0]
        print("\n=== %s" % path)
        print("    %d B  blob %s  %d operative words" % (len(raw), git_blob_sha(raw), len(w)))
        print("    closest canonical : %s" % best[0])
        print("    OPERATIVE BODY    : %s (-%d words, +%d words)" % (best[1], best[2], best[3]))
        for n in best[4]:
            print("      ! " + n)
        print("    whole payload     : %s (-%d, +%d)  <- placeholder fills land here"
              % (bestf[1], bestf[2], bestf[3]))


if __name__ == "__main__":
    main()
