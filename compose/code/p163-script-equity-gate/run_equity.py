#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Run the corpus through both gates and emit a TSV."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from corpus import CORPUS                      # noqa: E402
from script_equity import classify, gibberish_check, utf16_units  # noqa: E402


def fmt(v):
    return "-" if v is None else ("%.3f" % v if isinstance(v, float) else str(v))


def main():
    cols = ["tag", "script", "label", "utf16_len", "nonws_units", "letter_ratio",
            "ratio_verdict", "entropy", "entropy_verdict", "gibberish",
            "gib_reason", "words", "cjk_ratio", "branch", "tier"]
    print("\t".join(cols))
    for tag, script, label, text in CORPUS:
        rejected, reason, ratio, entropy = gibberish_check(text)
        tier, words, cjk_ratio, branch = classify(text)
        nonws = len(utf16_units("".join(text.split())))
        row = [
            tag, script, label,
            str(len(utf16_units(text))), str(nonws),
            fmt(ratio),
            "-" if ratio is None else ("PASS" if ratio >= 0.45 else "REJECT"),
            fmt(entropy),
            "-" if entropy is None else ("PASS" if entropy >= 1.5 else "REJECT"),
            "REJECTED" if rejected else "passed",
            reason or "-",
            str(words), fmt(cjk_ratio), branch, tier,
        ]
        print("\t".join(row))


if __name__ == "__main__":
    main()
