#!/usr/bin/env python3
"""Controls for `p245-apache-canonical`.

Runs from ANY cwd (`p355-cwd-portability`): the module is loaded from this file's own
directory by path, never by `import`, because `python3 -I` strips the script directory from
`sys.path` and `make hooks` is not run from here.

Every Apache fixture is a REAL payload read first-hand on 2026-10-16, not a synthetic string.
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_FIX = os.path.join(_HERE, "fixtures")

# Load the instrument by path, not by import.
_src = os.path.join(_HERE, "apache_canonical.py")
_ns = {"__name__": "apache_canonical_under_test", "__file__": _src}
with open(_src, "r", encoding="utf-8") as _fh:
    exec(compile(_fh.read(), _src, "exec"), _ns)  # noqa: S102
verdict = _ns["verdict"]
deviations = _ns["deviations"]
is_apache = _ns["is_apache"]

_FAILED = []
_RUN = 0


def check(label, expected, actual):
    global _RUN
    _RUN += 1
    if expected != actual:
        _FAILED.append("%s\n    expected: %r\n    actual:   %r" % (label, expected, actual))


def fixture(name):
    with open(os.path.join(_FIX, name), "r", encoding="utf-8") as fh:
        return fh.read()


CANONICAL = fixture("apache-2.0.canonical.txt")
NOMAD = fixture("project-nomad.two-deviations.txt")
CENIA = fixture("mvps-cenia.one-deviation.txt")
TANK = fixture("tank-royale.canonical-no-appendix.txt")
MIT = fixture("quizweaver.mit.txt")

# ── the canonical text is canonical ────────────────────────────────────────────────────────
check("apache.org canonical -> CANONICAL", "CANONICAL", verdict(CANONICAL))
check("canonical has no deviations", [], deviations(CANONICAL))

# ── THE FINDING: a real payload, three deviations, one of them operative ───────────────────
check(
    "project-nomad -> all three markers, in anchor order",
    "NON-CANONICAL:the-Licensor,received-by-the-Licensor,any-notices",
    verdict(NOMAD),
)
check("mvps-cenia -> exactly the one marker", "NON-CANONICAL:the-Licensor", verdict(CENIA))
check("CENIA does NOT carry the 4(d) deviation", ["the-Licensor"], deviations(CENIA))

# 🔴 THE CONTROL FOR THE BUG THIS PASS WROTE AND THEN CAUGHT.
# "excluding those notices that do not pertain" appears TWICE in canonical Apache: §4(c) for
# the Source form, §4(d) for the NOTICE file. The variant alters only §4(d). A presence/absence
# test on the bare phrase therefore finds it still present (from §4(c)) and reports clean.
_flat_nomad = " ".join(NOMAD.split())
check("the bare phrase survives in nomad (from the untouched 4(c))", 1,
      _flat_nomad.count("excluding those notices"))
check("...and the 4(d) deviation is present alongside it", 1,
      _flat_nomad.count("excluding any notices"))
check("so the naive test would have reported clean - the anchored one does not", True,
      "any-notices" in deviations(NOMAD))
check("canonical carries the phrase exactly twice", 2,
      " ".join(CANONICAL.split()).count("excluding those notices"))

# ── THE CONTROL THAT MATTERS MOST: a dropped APPENDIX is not a deviation ───────────────────
# Apache's appendix instructs the reader to replace it with their own notice. A later pass
# must not be able to "harden" this instrument into flagging that practice.
check("tank-royale dropped the appendix and is CANONICAL", "CANONICAL", verdict(TANK))
check("...and reports no markers", [], deviations(TANK))
check("the appendix really is absent from that fixture", False, "APPENDIX: How to apply" in TANK)
check("...while the canonical fixture keeps it", True, "APPENDIX: How to apply" in CANONICAL)

# ── reflowing is not rewriting ─────────────────────────────────────────────────────────────
check("hard-wrap collapsed: one long line is still CANONICAL", "CANONICAL",
      verdict(" ".join(CANONICAL.split())))
check("leading blank line is not a deviation", "CANONICAL", verdict("\n\n" + CANONICAL))
check("trailing whitespace is not a deviation", "CANONICAL",
      verdict("\n".join(l + "   " for l in CANONICAL.splitlines())))

# ── not-Apache stays not-Apache (no false family claims) ───────────────────────────────────
check("an MIT payload is NOT-APACHE", "NOT-APACHE", verdict(MIT))
check("the empty payload is NOT-APACHE, never CANONICAL", "NOT-APACHE", verdict(""))
check("whitespace-only is NOT-APACHE", "NOT-APACHE", verdict("   \n\t\n  "))
check("None-safe", "NOT-APACHE", verdict(None))

# `P971`: a LICENSE file carrying Apache's header NOTICE instead of Apache's terms names the
# licence and version but carries no grant sentence. It must not be graded for canonicality.
_NOTICE_ONLY = (
    "Copyright 2026 Example Holder\n\n"
    "Licensed under the Apache License, Version 2.0 (the \"License\");\n"
    "you may not use this file except in compliance with the License.\n"
    "You may obtain a copy of the License at\n\n"
    "    http://www.apache.org/licenses/LICENSE-2.0\n"
)
check("P971: NOTICE boilerplate is NOT-APACHE, not CANONICAL", "NOT-APACHE", verdict(_NOTICE_ONLY))
check("...and is_apache agrees", False, is_apache(_NOTICE_ONLY))

# ── an UNKNOWN rewrite is not reported as a known marker ───────────────────────────────────
# The instrument claims only the deviations it enumerates. A sentence rewritten some third
# way matches neither fragment and must stay silent rather than guess.
_THIRD_WAY = CANONICAL.replace(
    "submitted to Licensor for inclusion in the Work",
    "submitted to the licensing party for inclusion in the Work",
)
check("a third-way rewrite reports NO marker (no guessing)", [], deviations(_THIRD_WAY))

# ── the deviation must be detected through a hard wrap, which is how it really ships ───────
check("deviations survive collapsing (they are matched on collapsed text)",
      "NON-CANONICAL:the-Licensor,received-by-the-Licensor,any-notices",
      verdict(" ".join(NOMAD.split())))

# ── the two payloads this pass found identical really are identical ────────────────────────
# Measured in evidence/p245-apache-variant: project-nomad and rohitg00/k8sgames differ only in
# the copyright holder line. Asserting it on the one fixture kept in-tree.
check("nomad fixture holds the Crosstalk copyright line", True,
      "Copyright 2024-2026 Crosstalk Solutions LLC" in NOMAD)

if _FAILED:
    print("FAIL (%d of %d controls)" % (len(_FAILED), _RUN))
    for f in _FAILED:
        print("  - " + f)
    sys.exit(1)
print("PASS %d controls" % _RUN)
