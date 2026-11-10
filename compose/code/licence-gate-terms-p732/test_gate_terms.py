#!/usr/bin/env python3
"""Controls for gate_terms.py (p732). Run: python3 -I test_gate_terms.py

Builds the seven p732 controls from an in-file stock MIT payload so the suite
needs no network, and asserts the two directions that matter:
  - a tamper CONFINED TO A DROPPED LINE must be caught (the T272 defect);
  - a benign holder change must NOT be flagged (holder-invariance preserved).
"""
import os, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gate_terms import mit_gate, apache_gate, MIT_LEN, MIT_SHA

STOCK_MIT = '''MIT License

Copyright (c) 2026 Jason Tangen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

CASES = [
    ("stock",         lambda s: s, True),
    ("newholder",     lambda s: s.replace("Jason Tangen", "Globant SA"), True),
    ("cjk_holder",    lambda s: s.replace("Jason Tangen",
                                          "speechlab0210 (蝦說 AI / 小金)"), True),
    ("year_range",    lambda s: s.replace("(c) 2026", "(c) 2023-2026"), True),
    # tampers confined to lines the OLD rule discarded -> must FLAG
    ("attr_negated",  lambda s: s.replace("shall be included in all",
                                          "need NOT be included in all"), False),
    ("liable_flipped", lambda s: s.replace(
        "BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER",
        "ARE FULLY LIABLE FOR EVERY CLAIM, DAMAGE OR LOSS"), False),
    ("attr_deleted",  lambda s: s.replace(
        "The above copyright notice and this permission notice shall be included in all\n"
        "copies or substantial portions of the Software.\n", ""), False),
    # restriction appended to the holder line -> caught by the shape assertion
    ("noncommercial", lambda s: s.replace("Jason Tangen",
                                          "Jason Tangen. NONCOMMERCIAL USE ONLY."), False),
]


def run():
    failures = []
    d = tempfile.mkdtemp()
    for name, mutate, want_pass in CASES:
        p = os.path.join(d, name + ".txt")
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(mutate(STOCK_MIT))
        probs, n, sha = mit_gate(p)
        got_pass = not probs
        ok = (got_pass == want_pass)
        want = "PASS" if want_pass else "FLAG"
        note = "" if ok else f"   (wanted {want})"
        print(f"{'ok  ' if ok else 'FAIL'} {name:<16} "
              f"{'PASS' if got_pass else 'FLAG'} {n}B/{sha}{note}")
        for x in probs:
            print(f"       -> {x}")
        if not ok:
            failures.append(name)

    # the stock payload must reproduce the published constant exactly
    p = os.path.join(d, "stock.txt")
    _, n, sha = mit_gate(p)
    if (n, sha) != (MIT_LEN, MIT_SHA):
        print(f"FAIL constant drift: {n}B/{sha} != {MIT_LEN}B/{MIT_SHA}")
        failures.append("constant")
    else:
        print(f"ok   constant         {MIT_LEN}B/{MIT_SHA}")

    print()
    if failures:
        print(f"{len(failures)} control(s) failed: {', '.join(failures)}")
        return 1
    print(f"all {len(CASES)} controls + constant check behave as specified")
    return 0


if __name__ == "__main__":
    sys.exit(run())
