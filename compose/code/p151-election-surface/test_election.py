#!/usr/bin/env python3
"""Suite for `p151-election-surface`. Prints its own total (`P126` point 3).

🔵 **The obligatory case is the TRAP**: a tree whose only statement of the election is the
one inside the GNU licence's own appendix. The module must read that tree as `SILENT`, and
the control must still fire on it. A suite without that case would pass with the licence
file included in the walk, which is the whole defect (`T81`).

    python3 test_election.py
"""
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import election as E  # noqa: E402

# GPL-3.0's appendix, verbatim in shape — the text that makes a body read fire.
GPL3_BODY = """                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

  13. Use with the GNU Affero General Public License.

            How to Apply These Terms to Your New Programs

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
"""
HDR_LATER = """/*
 * This file is part of thing.
 * Licensed under the GNU General Public License as published by the Free
 * Software Foundation, either version 3 of the License, or (at your option)
 * any later version.
 */
function thing() {}
"""
HDR_ONLY = """# Licensed under the GNU General Public License version 3 of the License only.
def thing():
    pass
"""
HDR_SPDX_ONLY = """// SPDX-License-Identifier: GPL-3.0-only
int main(void) { return 0; }
"""
HDR_SPDX_LATER = """// SPDX-License-Identifier: AGPL-3.0-or-later
int main(void) { return 0; }
"""
HDR_SPDX_BARE = """// SPDX-License-Identifier: GPL-3.0
int main(void) { return 0; }
"""
PLAIN = "export function plain() { return 1 }\n"

cases = []


def check(name, got, want):
    cases.append((name, got == want, got, want))


def tree(base, name, files):
    d = os.path.join(base, name)
    os.makedirs(d, exist_ok=True)
    for fn, body in files.items():
        p = os.path.join(d, fn)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(body)
    return d


def main():
    tmp = tempfile.mkdtemp(prefix="p151-elect-")
    try:
        base = os.path.join(tmp, "trees")
        os.makedirs(base)

        # ── 1. THE TRAP — the obligatory case ─────────────────────────────────────────
        trap = tree(base, "trap", {"LICENSE": GPL3_BODY, "src/a.js": PLAIN})
        r = E.measure(trap)
        check("the licence appendix does NOT make the tree OR_LATER", r["election"],
              "SILENT")
        check("and the licence file is not even scanned", r["scanned"], 1)
        check("the control fires on the very file the measurement excluded",
              E.control(trap), (1, 1))

        # ── 2. a real per-file header ─────────────────────────────────────────────────
        later = tree(base, "later", {"LICENSE": GPL3_BODY, "src/a.js": HDR_LATER})
        check("a per-file or-later notice is read", E.measure(later)["election"],
              "OR_LATER")
        check("and it names the file it came from",
              E.measure(later)["later"], [os.path.join("src", "a.js")])

        # ── 3. an -only election ──────────────────────────────────────────────────────
        only = tree(base, "only", {"LICENSE": GPL3_BODY, "m.py": HDR_ONLY})
        check("an -only notice is read", E.measure(only)["election"], "ONLY")

        # ── 4. the SPDX surface ───────────────────────────────────────────────────────
        s1 = tree(base, "spdx-only", {"LICENSE": GPL3_BODY, "a.c": HDR_SPDX_ONLY})
        check("SPDX -only", E.measure(s1)["election"], "SPDX_ONLY")
        s2 = tree(base, "spdx-later", {"LICENSE": GPL3_BODY, "a.c": HDR_SPDX_LATER})
        check("SPDX -or-later", E.measure(s2)["election"], "SPDX_LATER")
        s3 = tree(base, "spdx-bare", {"LICENSE": GPL3_BODY, "a.c": HDR_SPDX_BARE})
        check("a BARE SPDX id states no election and must not be promoted",
              E.measure(s3)["election"], "SILENT")
        check("and it is not counted as an election", len(E.measure(s3)["spdx"]), 0)

        # ── 5. a conflict is reported, not resolved ───────────────────────────────────
        both = tree(base, "both", {"LICENSE": GPL3_BODY, "a.js": HDR_LATER,
                                   "b.py": HDR_ONLY})
        check("two different elections are a reported CONFLICT",
              E.measure(both)["election"], "BOTH_CONFLICT")

        # ── 6. the walk's exclusions, asserted ────────────────────────────────────────
        ex = tree(base, "excl", {"LICENSE": GPL3_BODY, "COPYING": GPL3_BODY,
                                 "docs/LICENSE.md": GPL3_BODY,
                                 "node_modules/dep/x.js": HDR_LATER,
                                 "target/gen.rs": HDR_LATER,
                                 "src/ok.js": PLAIN, "logo.png": "binary-ish"})
        rex = E.measure(ex)
        check("a licence file at depth is excluded too", rex["election"], "SILENT")
        check("node_modules and target are not walked", rex["scanned"], 1)
        check("a non-text file is not scanned", "logo.png" in str(rex), False)
        check("the control counts every licence file at any depth", E.control(ex)[1], 3)
        # 🔴 A BADGE IMAGE named license.svg is not a licence file, and counting it once
        # made the control report 7 of 8 on the real shelf.
        badge = tree(base, "badge", {"LICENSE": GPL3_BODY,
                                     "docs/license.svg": "<svg/>", "a.js": PLAIN})
        check("license.svg is not counted as a licence body", E.control(badge), (1, 1))
        check("and the tree is still SILENT", E.measure(badge)["election"], "SILENT")

        # ── 7. the verdict function in isolation ──────────────────────────────────────
        check("verdict: later wins alone", E.verdict(["a"], [], []), "OR_LATER")
        check("verdict: only wins alone", E.verdict([], ["a"], []), "ONLY")
        check("verdict: both is a conflict", E.verdict(["a"], ["b"], []),
              "BOTH_CONFLICT")
        check("verdict: prose beats SPDX when both are present",
              E.verdict(["a"], [], ["GPL-3.0-only"]), "OR_LATER")
        check("verdict: nothing is SILENT", E.verdict([], [], []), "SILENT")

        # ── 8. an empty tree must not read as an answer ───────────────────────────────
        empty = tree(base, "empty", {})
        re_ = E.measure(empty)
        check("an empty tree is SILENT with zero scanned", (re_["election"],
                                                            re_["scanned"]),
              ("SILENT", 0))
        check("and its control cannot fire, which the runner must notice",
              E.control(empty), (0, 0))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    failed = [c for c in cases if not c[1]]
    for name, ok, got, want in cases:
        if not ok:
            print("FAIL  %-58s got=%r want=%r" % (name, got, want))
    print("p151-election-surface: %d tests, %d passed, %d failed"
          % (len(cases), len(cases) - len(failed), len(failed)))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
