#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Three follow-up probes. The corpus showed nothing REJECTED; these measure
how far each script sits from a rejection, which is the part that transfers
to answers this corpus does not contain."""
import os
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from corpus import CORPUS                                   # noqa: E402
from script_equity import classify, gibberish_check, utf16_units, code_points_of, is_java_letter  # noqa: E402

MIN_LETTER_RATIO = 0.45

print("=" * 78)
print("PROBE 1 -- letter-ratio margin, and the critical combining-mark density")
print("=" * 78)
print("Analytic: whitespace is stripped first, so ratio = letters/units.")
print("With a mark fraction m (marks are NOT Java letters), ratio = 1 - m.")
print("A reject needs ratio < %.2f, i.e. m > %.2f.\n" % (MIN_LETTER_RATIO, 1 - MIN_LETTER_RATIO))
print("%-10s %8s %8s %9s %9s %9s" % ("tag", "units", "marks", "mark_frac", "ratio", "margin"))
for tag, script, label, text in CORPUS:
    if tag.startswith("CTRL"):
        continue
    norm = "".join(text.split())
    units = utf16_units(norm)
    cps = code_points_of(units)
    marks = sum(1 for cp in cps if unicodedata.category(chr(cp)) in ("Mn", "Mc", "Me"))
    ratio = sum(1 for cp in cps if is_java_letter(cp)) / len(units)
    print("%-10s %8d %8d %9.3f %9.3f %9.3f"
          % (tag, len(units), marks, marks / len(cps), ratio, ratio - MIN_LETTER_RATIO))

print("\nEmpirical check -- add full tashkeel to the UNVOCALISED Arabic answer")
print("by marking a rising fraction of its letters, and find where it rejects:")
ar = [t for tag, s, l, t in CORPUS if tag == "ar"][0]
norm_ar = "".join(ar.split())
HARAKAT = "َُِّْ"  # fatha kasra damma sukun shadda
for per_letter in (1, 2):
    for pct in (40, 60, 80, 100):
        out, k = [], 0
        for ch in norm_ar:
            out.append(ch)
            if is_java_letter(ord(ch)):
                k += 1
                if (k * 100 // max(1, len(norm_ar))) * 100 // 100 <= pct or (k % 100) < pct:
                    out.append(HARAKAT[k % len(HARAKAT)] * per_letter)
        s = "".join(out)
        rejected, reason, ratio, _e = gibberish_check(s)
        print("   %d mark(s)/letter on %3d%% of letters -> ratio %.3f  %s"
              % (per_letter, pct, ratio, "REJECTED (" + reason + ")" if rejected else "passed"))

print()
print("=" * 78)
print("PROBE 2 -- the astral-Han margin, and how little punctuation closes it")
print("=" * 78)
extb = "".join(chr(0x20000 + i) for i in range(18))
print("18 CJK Ext B ideographs, no punctuation:")
r = gibberish_check(extb)
print("   letters=18 (code points)  units=%d (UTF-16)  ratio=%.3f  -> %s"
      % (len(utf16_units(extb)), r[2], "REJECTED" if r[0] else "passed"))
print("   An equivalent BMP-Han answer of 18 ideographs would score ratio 1.000.")
print("\nNow add ideographic full stops (U+3002), one unit each, not a letter:")
for p in range(0, 8):
    s = extb + "。" * p
    rejected, reason, ratio, _e = gibberish_check(s)
    print("   +%d punctuation -> units=%2d ratio=%.3f  %s"
          % (p, len(utf16_units(s)), ratio, "REJECTED (" + reason + ")" if rejected else "passed"))

print()
print("=" * 78)
print("PROBE 3 -- the word-count branch, and the scripts that fall off it")
print("=" * 78)
PURE_EXTA = "".join(chr(0x3400 + i) for i in range(40))
PURE_COMPAT = "".join(chr(0xF900 + i) for i in range(40))
PURE_JAMO = "각" * 15
cases = [
    ("BMP Han x40", "好" * 40),
    ("Ext A Han x40 (U+3400+)", PURE_EXTA),
    ("Compatibility Han x40 (U+F900+)", PURE_COMPAT),
    ("Hangul Jamo, NFD x45", PURE_JAMO),
]
print("%-34s %7s %10s %-18s %s" % ("case", "words", "cjk_ratio", "branch", "tier"))
for name, s in cases:
    tier, words, ratio, branch = classify(s)
    print("%-34s %7d %10.3f %-18s %s" % (name, words, ratio, branch, tier))

print("\nThe Thai consequence, measured: one valid answer, then the same answer repeated.")
th = [t for tag, s, l, t in CORPUS if tag == "th"][0]
for mult in (1, 5, 20, 100):
    s = " ".join([th] * mult)
    tier, words, ratio, branch = classify(s)
    print("   Thai x%-4d chars=%6d  words=%4d  branch=%-17s tier=%s"
          % (mult, len(utf16_units(s)), words, branch, tier))
print("\n   For comparison, the English answer repeated to a similar length:")
en = [t for tag, s, l, t in CORPUS if tag == "en"][0]
for mult in (1, 5, 20):
    s = " ".join([en] * mult)
    tier, words, ratio, branch = classify(s)
    print("   Eng  x%-4d chars=%6d  words=%4d  branch=%-17s tier=%s"
          % (mult, len(utf16_units(s)), words, branch, tier))
