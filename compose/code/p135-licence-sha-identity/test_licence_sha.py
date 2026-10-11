#!/usr/bin/env python3
"""Tests for the p135 licence-identity instrument.

Run: python3 -I -m pytest test_licence_sha.py -q
"""

import sys
from pathlib import Path

# `python3 -I` drops the script's own directory from sys.path, and this suite is
# meant to run isolated, so put it back explicitly.
sys.path.insert(0, str(Path(__file__).resolve().parent))

import licence_sha as m  # noqa: E402

MIT_TEMPLATE = b"""MIT License

Copyright (c) <year> <copyright holders>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
"""

MIT_REAL = b"""MIT License

Copyright (c) 2026 Some Actual Holder

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
"""

GNU_SNIPPET = b"""GNU AFFERO GENERAL PUBLIC LICENSE

See http://www.gnu.org/licenses/ for details.
"""


def canon():
    return {"MIT": m.hashes(MIT_TEMPLATE)}


def test_exact_match_on_identical_bytes():
    assert m.classify(MIT_TEMPLATE, canon()) == ("MIT", "EXACT")


def test_whitespace_variant_trailing_spaces_and_crlf():
    variant = MIT_TEMPLATE.replace(b"\n", b"  \n").replace(b"\n", b"\r\n")
    spdx, verdict = m.classify(variant, canon())
    assert (spdx, verdict) == ("MIT", "WHITESPACE_VARIANT"), (spdx, verdict)


def test_trailing_blank_lines_are_a_whitespace_variant():
    spdx, verdict = m.classify(MIT_TEMPLATE + b"\n\n\n", canon())
    assert (spdx, verdict) == ("MIT", "WHITESPACE_VARIANT")


def test_real_copyright_line_is_a_template_match_not_unmatched():
    """The whole point: a correctly applied MIT licence must be recognised even
    though its bytes can never equal the SPDX template."""
    assert m.classify(MIT_REAL, canon()) == ("MIT", "TEMPLATE_MATCH")


def test_added_clause_is_flagged_as_modified_superset():
    """The P134-F class: MIT plus an extra visible-attribution requirement."""
    modified = MIT_REAL + b"\nYou must display visible attribution in the UI.\n"
    assert m.classify(modified, canon()) == ("MIT", "MODIFIED_SUPERSET")


def test_unrelated_text_is_unmatched():
    spdx, verdict = m.classify(b"This is a proprietary licence. All rights reserved.\n", canon())
    assert verdict == "UNMATCHED" and spdx is None


def test_fsf_http_to_https_normalisation():
    """An old GNU payload differing only by the FSF's own http->https update
    must not read as a different licence."""
    old = GNU_SNIPPET
    new = GNU_SNIPPET.replace(b"http://www.gnu.org", b"https://www.gnu.org")
    assert m.normalise_ws(old) == m.normalise_ws(new)
    assert m.hashes(old)["ws"] == m.hashes(new)["ws"]


def test_interior_blank_lines_are_preserved_by_ws_normalisation():
    """Normalisation must not collapse structure, or two different licences
    could hash alike."""
    a = b"line one\n\nline two"
    b = b"line one\nline two"
    assert m.normalise_ws(a) != m.normalise_ws(b)


def test_strip_copyright_removes_only_copyright_lines():
    out = m.strip_copyright(m.normalise_ws(MIT_REAL))
    assert b"Copyright" not in out
    assert b"Permission is hereby granted" in out


def test_body_hash_is_equal_across_different_holders():
    """Cross-owner identity: the same licence body under two holders shares a
    body hash, which is why body-hash grouping needs the owner check that
    main() applies before calling anything a mirror."""
    other = MIT_REAL.replace(b"Some Actual Holder", b"A Different Holder")
    assert m.hashes(MIT_REAL)["body"] == m.hashes(other)["body"]
    assert m.hashes(MIT_REAL)["raw"] != m.hashes(other)["raw"]


def test_empty_payload_is_unmatched_and_does_not_crash():
    assert m.classify(b"", canon()) == (None, "UNMATCHED")


def test_superset_prefers_longest_canonical_body():
    """With two canonical texts where one's body contains the other's, the
    longer must win so a long licence is not reported as a short one."""
    short = b"Permission granted.\n"
    long_ = b"Permission granted.\nPlus many further conditions apply here.\n"
    c = {"SHORT": m.hashes(short), "LONG": m.hashes(long_)}
    spdx, verdict = m.classify(long_ + b"\nAnd one extra clause.\n", c)
    assert (spdx, verdict) == ("LONG", "MODIFIED_SUPERSET"), (spdx, verdict)


def test_rewrapped_licence_is_recognised():
    """THE case this instrument exists for: SPDX wraps at ~105 columns, real
    LICENSE files at ~72. Same words, different hard breaks."""
    rewrapped = MIT_TEMPLATE.replace(
        b"to any person obtaining a copy\nof this software",
        b"to any person obtaining\na copy of this software")
    spdx, verdict = m.classify(rewrapped, canon())
    assert (spdx, verdict) == ("MIT", "REFLOWED"), (spdx, verdict)


def test_real_mit_at_72_columns_is_a_template_match():
    """A real MIT file differs from the template by BOTH wrap width and the
    copyright line; it must still resolve to MIT. Rewrapped on word boundaries,
    as a real text editor would -- breaking mid-word changes the words."""
    import textwrap

    paras = MIT_TEMPLATE.decode().split("\n\n")
    rewrapped = "\n\n".join(
        "\n".join(textwrap.wrap(" ".join(p.split()), width=72)) for p in paras if p.strip()
    ).replace("<year> <copyright holders>", "2026 A Holder")
    spdx, verdict = m.classify(rewrapped.encode(), canon())
    assert spdx == "MIT" and verdict == "TEMPLATE_MATCH", (spdx, verdict)


def test_reflow_preserves_paragraph_boundaries():
    """Reflow must not merge paragraphs, or two licences differing only in
    structure would collide."""
    a = m.reflow(b"alpha beta\n\ngamma delta")
    b = m.reflow(b"alpha beta gamma delta")
    assert a != b
    assert a == b"alpha beta\n\ngamma delta"


def test_reflow_does_not_equate_different_words():
    assert m.reflow(b"permission granted") != m.reflow(b"permission denied")


def test_reflow_is_idempotent():
    once = m.reflow(b"one   two\nthree\n\nfour")
    assert m.reflow(once) == once


GNU_HEADER = b"""GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it is not allowed.

Preamble text follows here.
"""


def test_copyright_strip_does_not_eat_its_paragraph_neighbour():
    """Regression for the bug that made six GPL-3.0 payloads read UNMATCHED.

    The GNU header puts the copyright notice and the "Everyone is permitted"
    sentence in ONE paragraph. Stripping after reflow deletes both; stripping
    before reflow deletes only the notice."""
    body = m.hashes(GNU_HEADER)["_body"]
    assert b"Copyright (C) 2007" not in body
    assert b"Everyone is permitted" in body, body
    assert b"changing it is not allowed" in body


def test_gnu_header_matches_across_different_wrap_widths():
    """The same GNU header rewrapped must still resolve to the same body."""
    rewrapped = GNU_HEADER.replace(
        b"verbatim copies\nof this license document",
        b"verbatim\ncopies of this license document")
    assert m.hashes(GNU_HEADER)["body"] == m.hashes(rewrapped)["body"]


def test_strip_copyright_drops_emptied_paragraphs_keeps_others():
    out = m.strip_copyright(m.reflow(b"Copyright (c) 2026 X\n\nalpha\n\nbeta"))
    assert out == b"alpha\n\nbeta", out


def test_continuation_line_starting_with_copyright_is_not_deleted():
    """Regression: a 72-column Apache payload breaks mid-sentence before the
    word "copyright", and a line-based strip deleted that licence text.

    Observed on Cvmcosta/ltijs and 1EdTech/digital-credentials-public-validator:
    "...must include a readable / copyright notice that is included in..."
    """
    wrapped = (b"You must retain, in the Source form, a readable\n"
               b"copyright notice that is included in or attached to the work.")
    body = m.hashes(wrapped)["_body"]
    assert b"copyright notice that is included" in body, body


def test_notice_sharing_a_paragraph_with_licence_text_keeps_the_text():
    """The other direction, on the real GNU header shape."""
    body = m.hashes(GNU_HEADER)["_body"]
    assert b"Copyright (C) 2007" not in body
    assert b"Everyone is permitted" in body, body


def test_mit_placeholder_angle_brackets_do_not_cut_the_notice_early():
    """MIT's template notice contains <year> <copyright holders>; the span must
    swallow both, or the template and a real MIT file stop matching."""
    body = m.hashes(b"MIT License\n\nCopyright (c) <year> <copyright holders>\n\nPermission.")["_body"]
    assert b"copyright holders" not in body, body
    assert b"Permission." in body


def test_fsf_moved_path_is_normalised():
    """The FSF moved why-not-lgpl.html from /licenses/ to /philosophy/. A
    GPL-3.0 COPYING committed before that move is otherwise identical, and this
    one path was the whole remaining difference on five payloads."""
    old = b"please read <https://www.gnu.org/licenses/why-not-lgpl.html>."
    new_ = b"please read <https://www.gnu.org/philosophy/why-not-lgpl.html>."
    assert m.normalise_ws(old) == m.normalise_ws(new_)


def test_punctuation_folding_handles_curly_quotes():
    """SPDX's GPL-3.0 uses typographic quotes; real COPYING files use ASCII."""
    curly = "the \u201cProgram\u201d means".encode()
    plain = b'the "Program" means'
    assert m.normalise_ws(curly) == m.normalise_ws(plain)


def test_punctuation_folding_does_not_change_words():
    assert b"Program" in m.normalise_ws("the \u201cProgram\u201d".encode())


def test_collapsed_level_absorbs_paragraph_placement():
    """Same words and order, different paragraph breaks -> matched, but only at
    the weakest level, and the verdict must say so."""
    a = b"GNU LESSER GENERAL PUBLIC LICENSE\n\nVersion 2.1\n\nterms follow"
    b = b"GNU LESSER GENERAL PUBLIC LICENSE Version 2.1\n\nterms follow"
    spdx, verdict = m.classify(b, {"X": m.hashes(a)})
    assert (spdx, verdict) == ("X", "WHITESPACE_COLLAPSED"), (spdx, verdict)


def test_collapsed_level_still_rejects_different_words():
    a = b"alpha beta\n\ngamma"
    b = b"alpha beta\n\ndelta"
    spdx, verdict = m.classify(b, {"X": m.hashes(a)})
    assert verdict == "UNMATCHED", (spdx, verdict)


def test_nearest_reports_a_candidate_for_unmatched():
    """An UNMATCHED row with no nearest reads as "unusual licence" -- the
    P134-F bias. It must report what it resembles."""
    c = {"MIT": m.hashes(MIT_TEMPLATE)}
    spdx, ratio = m.nearest(m.hashes(MIT_REAL + b"\n\nExtra clause here.\n"), c)
    assert spdx == "MIT" and ratio > 0.8, (spdx, ratio)


def test_frontmatter_is_stripped():
    raw = b"---\ntitle: X\nspdx-id: Y\n---\nREAL LICENCE TEXT\n"
    assert m.strip_frontmatter(raw) == b"REAL LICENCE TEXT\n"
    assert m.strip_frontmatter(b"no frontmatter here") == b"no frontmatter here"


def test_undated_whole_paragraph_notice_is_stripped():
    """dhodges47/SCORM-LearningManagementSystem: "Copyright (c) David Hodges
    dba Outermost Software, LLC" -- a real notice with no year at all."""
    payload = b"MIT License\n\nCopyright (c) David Hodges dba Outermost Software, LLC\n\nPermission."
    body = m.hashes(payload)["_body"]
    assert b"David Hodges" not in body, body
    assert b"Permission." in body


def test_undated_notice_rule_does_not_eat_prose_about_copyright():
    """The year requirement still protects prose; only a paragraph that IS a
    notice is dropped."""
    prose = b"Copyright law in your jurisdiction may grant you further rights which this paragraph discusses at some length and which must be preserved in the body."
    body = m.hashes(prose)["_body"]
    assert b"jurisdiction" in body, body


def test_gnu_appendix_bracket_style_is_folded():
    """GPL-3.0's appendix placeholders appear as <...> and as {...}."""
    angles = b"<one line to give the program's name> Copyright (C) <year> <name>"
    braces = b"{one line to give the program's name} Copyright (C) {year} {name}"
    assert m.normalise_ws(angles) == m.normalise_ws(braces)


def _run():
    """Dependency-free runner: this environment has no pytest, so the suite
    must be executable with a bare interpreter. Kept pytest-compatible."""
    import traceback
    fns = [(n, f) for n, f in sorted(globals().items())
           if n.startswith("test_") and callable(f)]
    failed = 0
    for name, fn in fns:
        try:
            fn()
            print(f"PASS {name}")
        except Exception:
            failed += 1
            print(f"FAIL {name}")
            traceback.print_exc()
    print(f"\n{len(fns) - failed}/{len(fns)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(_run())
