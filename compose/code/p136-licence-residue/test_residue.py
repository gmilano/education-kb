"""Tests for p136-licence-residue (`ACTION BV`).

The three real payloads are 26-35 KB each and are not committed here; the fixtures
below are the EXACT residue runs the instrument reported against them on
2026-10-11, plus controls. `result.2026-10-11-p136.tsv` holds the full run.

Run: python3 -I test_residue.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from residue import (residue, summarise, normalise,
                     SIGN_TRANSLITERATION, PLACEHOLDER_DELIMITER,
                     APPENDIX_INSTANTIATION, STEWARD_DIVERGENCE, ADDED_CLAUSE,
                     RESOLVED, MODIFIED)

FAILS = []


def check(name, got, want):
    if got != want:
        FAILS.append(f"{name}: got {got!r}, want {want!r}")


# A miniature GNU-shaped text: body plus the "How to Apply" appendix.
CANON = """GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

Copyright © 2007 Free Software Foundation, Inc. <http://fsf.org/>

Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.

How to Apply These Terms to Your New Programs

    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


def test_citolab_shape_resolves():
    """`Citolab/qti-convert`: the sign in ASCII and the appendix filled in.
    Measured ratio 0.998672, 3 opcodes, verdict RESOLVED."""
    payload = (CANON.replace("© 2007", "(C) 2007")
                     .replace("<one line to give the program's name and a brief idea of what it does.>",
                              "@citolab/qti-convert")
                     .replace("<year>  <name of author>",
                              "2024 Stichting Cito Instituut voor Toetsontwikkeling, Arnhem"))
    verdict, ratio, ops = residue(payload, CANON)
    check("citolab/verdict", verdict, RESOLVED)
    check("citolab/no-added-clause", any(k == ADDED_CLAUSE for k, _, _ in ops), False)
    check("citolab/sign", SIGN_TRANSLITERATION in summarise(ops), True)
    check("citolab/appendix", APPENDIX_INSTANTIATION in summarise(ops), True)
    # The miniature fixture is ~90 words, so one 9-word holder substitution costs
    # far more of its ratio than it does of the real 35 196-byte payload (measured
    # 0.998672). The assertion is scaled to the fixture, not to the real file.
    check("citolab/ratio-high", ratio > 0.85, True)


def test_adapt_shape_resolves_including_brace_delimiters():
    """`adaptlearning/adapt_framework`: every `<...>` rewritten as `{...}`, plus the
    appendix filled in. Measured ratio 0.997431, 11 opcodes, verdict RESOLVED."""
    payload = (CANON.replace("© 2007", "(C) 2007")
                     .replace("<http://fsf.org/>", "{https://fsf.org/}")
                     .replace("<one line to give the program's name and a brief idea of what it does.>",
                              "adapt_framework")
                     .replace("<year>  <name of author>", "2013 ADAPT LEARNING")
                     .replace("<https://www.gnu.org/licenses/>", "{https://www.gnu.org/licenses/}"))
    verdict, _, ops = residue(payload, CANON)
    check("adapt/verdict", verdict, RESOLVED)
    kinds = summarise(ops)
    check("adapt/delimiter-class-seen", PLACEHOLDER_DELIMITER in kinds, True)
    check("adapt/no-added-clause", ADDED_CLAUSE in kinds, False)


def test_pyopenbadges_steward_divergence_is_named_not_hidden():
    """`CoopCodeCommun/pyopenbadges`: the payload says "a brief idea", SPDX's
    LGPL-2.1 text says "an idea". Neither wording is the project's choice."""
    canon = "a line to give the library's name and an idea of what it does."
    payload = "a line to give the library's name and a brief idea of what it does."
    verdict, _, ops = residue(payload, canon)
    check("pyopenbadges/verdict", verdict, RESOLVED)
    check("pyopenbadges/steward", summarise(ops).get(STEWARD_DIVERGENCE), 1)


def test_a_real_added_clause_is_still_caught():
    """The control. `P134-F`'s class -- a permissive body plus a visible-attribution
    clause -- must NOT resolve, or this instrument launders licence risk."""
    payload = CANON.replace(
        "license document, but changing it is not allowed.",
        "license document, but changing it is not allowed.\n\nYou must display the "
        "phrase 'Powered by Acme' on every screen of any derivative work.")
    verdict, _, ops = residue(payload, CANON)
    check("control/verdict", verdict, MODIFIED)
    check("control/added-clause", summarise(ops).get(ADDED_CLAUSE), 1)


def test_fsf_url_edits_are_not_project_edits():
    """p135's `P135-F`: the FSF moved why-not-lgpl.html out of /licenses/. A payload
    committed before that move must not read as modified."""
    canon = "see <https://www.gnu.org/philosophy/why-not-lgpl.html>."
    payload = "see <http://www.gnu.org/licenses/why-not-lgpl.html>."
    verdict, ratio, ops = residue(payload, canon)
    check("fsf/verdict", verdict, RESOLVED)
    check("fsf/zero-opcodes", len(ops), 0)
    check("fsf/ratio", ratio, 1.0)


def test_normalise_is_line_wrap_insensitive():
    """p135's finding: payloads differ from canonical texts by WRAP WIDTH. The word
    sequence has to be identical across wrap widths or nothing else works."""
    a = "the quick brown fox jumps over the lazy dog"
    b = "the quick brown fox\njumps over\nthe lazy dog"
    check("wrap/identical", normalise(a), normalise(b))


def test_typographic_quotes_do_not_count():
    canon = "the “Program” means"
    payload = 'the "Program" means'
    verdict, _, ops = residue(payload, canon)
    check("quotes/verdict", verdict, RESOLVED)
    check("quotes/zero-opcodes", len(ops), 0)


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for t in tests:
        t()
    if FAILS:
        print(f"FAILED {len(FAILS)} check(s) across {len(tests)} tests:")
        for f in FAILS:
            print("  -", f)
        sys.exit(1)
    print(f"ok -- {len(tests)} tests, all checks passed")
