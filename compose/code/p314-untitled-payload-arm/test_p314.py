#!/usr/bin/env python3
"""p314 — controls for the untitled-grant arm, step 0c, and `is_this_a_grant?`.

🔵 Run from this directory (`p355-cwd-portability`): every load is by explicit
path and nothing here does a bare `import fixtures`.

The suite follows this base's convention: each control names what it would catch,
and the ones pinning a MEASURED state name the action item that would change it
rather than asserting a value an open item means to move.
"""
import importlib.util
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.normpath(os.path.join(HERE, ".."))
P310 = os.path.join(CODE, "p310-family-coverage")
P311 = os.path.join(CODE, "p311-permissive-family-arm")
P312 = os.path.join(CODE, "p312-template-identity")


def _load(name, path, extra_path=None):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    if extra_path:
        sys.path.insert(0, extra_path)
    sink, sys.stdout = sys.stdout, io.StringIO()
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.stdout = sink
        if extra_path and extra_path in sys.path:
            sys.path.remove(extra_path)
    return mod


FX = _load("p314_fx", os.path.join(HERE, "fixtures.py"), HERE)
PID = _load("p314_pid", os.path.join(P311, "payload_identity.py"), P311)
ARM = _load("p314_arm", os.path.join(HERE, "run_untitled.py"), HERE)

CHECKS = []


def check(fn):
    CHECKS.append(fn)
    return fn


def _text(prefix):
    return FX.load(prefix)[0]


def _p312_fixture(prefix):
    """The `MPL-2.0` payload `p312` pinned, loaded BY PREFIX from p312's own
    directory. 🔵 Prefix, never a literal filename: `p283-ladder-case-audit`
    reads a spelled-out licence filename in a code string as a path rung."""
    fixdir = os.path.join(P312, "fixtures")
    hits = sorted(n for n in os.listdir(fixdir) if n.startswith(prefix))
    assert len(hits) == 1, "%s resolves to %d files" % (prefix, len(hits))
    with open(os.path.join(fixdir, hits[0]), encoding="utf-8") as fh:
        return fh.read()


# ── the pins themselves ──────────────────────────────────────────────────────

@check
def test_every_fixture_matches_the_bytes_in_its_own_filename():
    """A pin whose filename disagrees with its content is not evidence."""
    for prefix, _fam, _com, _why, _t, n, _sha in FX.declared():
        fn = os.path.basename(FX.resolve(prefix))
        declared = int(fn.rsplit("-", 1)[1].split(".")[0])
        assert declared == n, "%s: filename says %d B, file is %d B" % (fn, declared, n)


@check
def test_the_pins_replicate_p313s_first_hand_reads():
    """🟢 `p313` read five of these payloads over `curl` in a different session.
    This pass re-read them and they must agree to the byte and the sha —
    otherwise one of the two reads is not evidence of anything."""
    expect = {
        "bsd-3-clause-freecodecamp": (1513, "e2a20708d0fd"),
        "bsd-3-clause-jupyterhub": (1475, "7069c7e8d60e"),
        "cc-by-nc-nd-4.0-ud-portuguese-cintil": (224, "73c169eb6bbf"),
        "cc-by-nc-nd-4.0-mzyphur": (1470, "39b4d330a934"),
        "cc-by-nc-nd-4.0-shule-ai": (209, "9dd285c3704d"),
        "mpl-2.0-common-voice": (16726, "3f3d9e0024b1"),
    }
    for prefix, (n, sha) in expect.items():
        _t, got_n, got_sha = FX.load(prefix)
        assert (got_n, got_sha) == (n, sha), \
            "%s: p313 read %d B %s, this pass reads %d B %s" % (prefix, n, sha, got_n, got_sha)


# ── ACTION p313-R item 5, and the finding that widened it ────────────────────

@check
def test_both_bsd_shapes_are_pinned_and_they_are_different_documents():
    """🔴 `ACTION p313-R` item 5, in its own words: pin BOTH shapes and *"do not
    publish a coverage figure for the family off one of them"*. `301` cells.
    🔵 The control asserts they are genuinely two documents, so a future pass
    cannot satisfy the item by pinning one file twice."""
    pairs = FX.shape_pairs()
    assert pairs["BSD-3-Clause"]["titled"] and pairs["BSD-3-Clause"]["untitled"], \
        "item 5 needs BOTH shapes pinned; one slot is empty"
    texts = [_text(p) for slot in ("titled", "untitled")
             for p in pairs["BSD-3-Clause"][slot]]
    for i, a in enumerate(texts):
        for b in texts[i + 1:]:
            assert not PID.same_grant(a, b, "BSD-3-Clause"), \
                "two BSD pins are the same GRANT document — item 5 is not " \
                "satisfied by pinning one file twice"


@check
def test_the_untitled_payloads_carry_no_title_line():
    """The property the whole arm rests on. 🔴 If a future fetch returns a file
    whose first line DOES name the family, this arm is measuring nothing and the
    control must say so rather than reporting a clean pass."""
    for fam, slots in FX.shape_pairs().items():
        tok = ARM._TOKEN[fam]
        for prefix in slots["titled"]:
            line = ARM._title_line(_text(prefix))
            assert re.search(tok, line, re.I), \
                "%s titled control %s: first line %r does not name the family" \
                % (fam, prefix, line)
        for prefix in slots["untitled"]:
            line = ARM._title_line(_text(prefix))
            assert not re.search(tok, line, re.I), \
                "%s untitled payload %s: first line %r NAMES the family" \
                % (fam, prefix, line)


@check
def test_the_untitled_mit_payload_contains_no_mit_token_at_all():
    """🔴 THIS PASS'S HEADLINE, as a standing control. `crewAIInc/crewAI` serves
    the complete MIT grant and the family name is not in the file — on the family
    that holds more than a third of every licence cell this base publishes."""
    text = _text("mit-crewai")
    assert not ARM._token_present("mit", text), \
        "the untitled MIT payload now contains the token `MIT` as a word"
    assert "permission is hereby granted, free of charge" in text.lower(), \
        "the payload must still BE the MIT grant, or it is not evidence of blindness"


@check
def test_the_untitled_shape_reaches_the_education_vertical_and_costs_usable_supply():
    """🔴 The finding that makes this class matter to an engagement rather than to
    an instrument. `open-tutorai/open-tutor-ai-ce` is an EDUCATION-SPECIFIC AI
    tutoring platform whose grant is PERMISSIVE `BSD-3-Clause` — the supply this
    base exists to find — and its payload names **no licence family at all**.

    🔵 So the cost of the untitled shape is not abstract. Under `P250` an
    abstention is indistinguishable from `PROHIBITED`, which means an automated
    screen drops a permissive education platform a studio could have built on.
    🟢 That is the direction of the loss, stated as a control: usable supply
    excluded, never a wrong licence shipped."""
    text = _text("bsd-3-clause-open-tutor-ai-ce")
    for tok in ("mit", "bsd", "apache", "mozilla", "gnu"):
        assert not re.search(r"\b%s\b" % tok, text, re.I), \
            "the payload now names the %r family — it is no longer token-free" % tok
    # 🔴 it must still BE a 3-clause BSD grant, or it is not evidence
    low = text.lower()
    assert "redistribution and use in source and binary forms" in low
    assert "endorse or promote" in low, \
        "without the endorsement clause this is 2-Clause, not 3-Clause"
    # 🟢 and it must be permissive on the axis that decides shippability
    verdict, _why = PID.is_this_a_grant(text, "BSD-3-Clause")
    assert verdict == "GRANT"


@check
def test_the_substring_form_matches_the_untitled_mit_payload_by_accident():
    """🔴 The accident channel, kept live. This base's single most-repeated defect
    class is the unanchored substring (`p306`'s `"affero" in low`, `"cc0" in
    low`), and until now it has only ever been a POSSIBILITY. Here it is a
    measured false friend: `"mit" in low` is True on a payload with no `MIT`
    token, because it matches inside other words.
    🔵 The control pins the mechanism, not just the boolean — a classifier that
    is right here is right by accident, and that must stay visible."""
    text = _text("mit-crewai")
    assert ARM._substring_says("mit", text), \
        "the substring form no longer matches — the accident is gone and so is the lesson"
    carriers = {m.group(0).lower() for m in re.finditer(r"\w*mit\w*", text, re.I)}
    carriers.discard("mit")
    assert carriers, "the substring must match INSIDE other words, or it is not an accident"


@check
def test_a_title_only_classifier_is_blind_on_the_untitled_grant():
    """🔴 The arm's standing finding: at least one declared classifier reads the
    family on the titled payload and ABSTAINS on the same family's grant when the
    title line does not name it. 🔵 `p313` INFERRED this from the payload's shape
    and could not run a classifier; this is the measurement."""
    out = io.StringIO()
    sink, sys.stdout = sys.stdout, out
    try:
        rc = ARM.main()
    finally:
        sys.stdout = sink
    assert rc == 0, "the arm reports a DEFECT:\n%s" % out.getvalue()
    assert "TITLE-ONLY" in out.getvalue(), \
        "no classifier is title-dependent any more — the finding has been repaired " \
        "and this control should be retired with a note, not left asserting"


@check
def test_p313s_inference_that_no_channel_can_read_the_untitled_bsd_is_refuted():
    """🔴 `p313` wrote, of `jupyterhub/jupyterhub`: *"no automated channel here
    can read it"* and *"every body ladder keyed on a family name returns
    nothing"*. 🟢 MEASURED FALSE. Several classifiers read it correctly — not off
    the family name, which is absent, but off the CLAUSE STRUCTURE.
    🔵 That is the distinction this arm exists to make, and it is the one `p313`
    could not make without the code channel."""
    text = _text("bsd-3-clause-jupyterhub")
    assert not ARM._token_present("bsd", text)
    assert not ARM._substring_says("bsd", text), \
        "the untitled BSD payload must contain no `bsd` substring either"
    readers = []
    for relpath, callable_name in ARM.ENTRY_POINTS:
        if relpath in ARM.OUT_OF_DOMAIN:
            continue
        try:
            mod = ARM._arm._load(relpath)
            got = ARM._answer(getattr(mod, callable_name)(text))
        except Exception:                               # noqa: BLE001
            continue
        if got and ARM.grade("BSD-3-Clause", got) in ("CORRECT", "COARSE"):
            readers.append((relpath, got))
    assert readers, \
        "p313's inference would now be correct — no classifier reads the untitled " \
        "BSD payload. Record that as a CHANGE, not as a passing control."


# ── ACTION p313-R item 2a ────────────────────────────────────────────────────

@check
def test_two_payloads_of_equal_length_are_different_files():
    """🔴 `ACTION p313-R` item 2a asks for this control in its own words: *"two
    payloads of EQUAL length can differ — a bytes-and-sha ledger never puts those
    two rows side by side"*.
    🔵 It is the sharper converse of `p311`'s rule. `p311` established that equal
    GRANTS can have different bytes; this is two different FILES at identical
    bytes, so byte length does not even answer *"is this the same file?"*."""
    a = _p312_fixture("mpl-2.0-safeexambrowser")
    b = _text("mpl-2.0-common-voice")
    na, sa = PID.raw_identity(a)
    nb, sb = PID.raw_identity(b)
    assert na == nb, "the pair must be the same byte length (%d vs %d)" % (na, nb)
    assert sa != sb, "the pair must be different files"


@check
def test_step_0c_makes_the_scheme_only_pair_one_grant():
    """🔴 The measured false negative item 2a names: after `p312`'s step 0b the
    pair's only residual difference is the URL scheme in the *Exhibit A* notice,
    and `same_grant()` returned False for a single document."""
    a = _p312_fixture("mpl-2.0-safeexambrowser")
    b = _text("mpl-2.0-common-voice")
    assert PID.same_grant(a, b, "MPL-2.0"), \
        "step 0c no longer reconciles the scheme-only pair"


@check
def test_the_residual_difference_really_was_only_the_scheme():
    """🔵 The control that keeps step 0c HONEST. A normalisation step is only
    justified by the difference it was built for, and this asserts that the pair
    differed on exactly one line and that the line's difference was the scheme —
    not that some normalisation somewhere made two files match."""
    a = _p312_fixture("mpl-2.0-safeexambrowser")
    b = _text("mpl-2.0-common-voice")

    def through_0b(t):
        body = t.lstrip("﻿").strip().replace("\r\n", "\n").replace("\r", "\n")
        return "\n".join(l.rstrip() for l in body.split("\n")).split("\n")

    la, lb = through_0b(a), through_0b(b)
    assert len(la) == len(lb)
    diff = [(x, y) for x, y in zip(la, lb) if x != y]
    assert len(diff) == 1, "expected exactly one differing line, got %d" % len(diff)
    x, y = diff[0]
    assert x.replace("http://", "https://") == y, \
        "the one difference is not the URL scheme: %r vs %r" % (x, y)


@check
def test_step_0c_still_separates_different_grants():
    """🔴 The TRUE NEGATIVE. This module's docstring warns that *"a normaliser
    that keeps being widened until everything matches proves nothing"*, so every
    step must ship with the control showing the oracle still discriminates."""
    mpl = _text("mpl-2.0-common-voice")
    mit = _text("mit-educhain")
    bsd = _text("bsd-3-clause-freecodecamp")
    assert not PID.same_grant(mpl, mit, None)
    assert not PID.same_grant(mit, bsd, "MIT")
    assert not PID.same_grant(mpl, bsd, None)


@check
def test_step_0c_touches_only_the_scheme_and_not_the_rest_of_a_url():
    """🔵 The bound on the step, as a control rather than a comment. It must
    rewrite the scheme token and leave host and path alone, or it is a wider
    change than the payload justifies."""
    # 🟢 the scheme is reconciled …
    assert PID.same_grant("see https://example.org/a/b",
                          "see http://example.org/a/b")
    # 🔴 … and nothing else about the URL is. Host, path and query must each
    # still separate two documents, or the step has become a URL eraser.
    assert not PID.same_grant("see https://example.org/a/b",
                              "see https://example.com/a/b")
    assert not PID.same_grant("see https://example.org/a/b",
                              "see https://example.org/a/c")
    assert not PID.same_grant("see https://example.org/a/b?v=2",
                              "see https://example.org/a/b?v=3")
    # 🔵 a scheme this step does not claim must survive untouched, in both
    # directions: it neither reconciles nor conflates them.
    assert not PID.same_grant("write to mailto:x@example.org",
                              "write to mailto:y@example.org")
    assert not PID.same_grant("fetch ftps://example.org/a",
                              "fetch ftp://example.org/a")


# ── ACTION p313-R item 4 ─────────────────────────────────────────────────────

@check
def test_all_four_noncommercial_payloads_grade_as_notices():
    """🔴 `ACTION p313-R` item 4. `p313` pinned four `CC-BY-NC-*` payloads as
    `bytes` + `sha` and only then noticed, by READING them, that not one was an
    operative grant. Every one pinned cleanly, because a pin records the bytes
    and never asks what the bytes are.
    🟢 This is the cheaper question underneath, and it closes the class."""
    graded = {}
    for prefix, fam, _com, _why, text, _n, _s in FX.declared():
        if not fam.startswith("CC-BY-NC"):
            continue
        verdict, why = PID.is_this_a_grant(text, fam)
        graded[prefix] = (verdict, why)
    assert len(graded) == 3, "expected this pass's three NC pins, got %d" % len(graded)
    for prefix, (verdict, why) in graded.items():
        assert verdict == "NOT-A-GRANT", "%s graded %s (%s)" % (prefix, verdict, why)


@check
def test_the_deed_summary_is_caught_by_its_own_disclaimer():
    """🟢 The fourth payload, pinned in this tree for many passes before `p313`
    found it: the Creative Commons DEED SUMMARY, whose own line 5 reads *"This is
    a human-readable summary of (and not a substitute for) the full license."*
    🔵 It is caught by the pointer channel rather than the length floor, which is
    why item 4 needs both: at `1 891` B it is above two of the floors."""
    ladder = os.path.join(CODE, "grant-ladder-v4", "fixtures")
    hits = sorted(n for n in os.listdir(ladder) if n.startswith("cccareers-"))
    assert len(hits) == 1, "the deed fixture no longer resolves uniquely"
    with open(os.path.join(ladder, hits[0]), encoding="utf-8") as fh:
        text = fh.read()
    verdict, why = PID.is_this_a_grant(text, "CC-BY-NC-SA-4.0")
    assert verdict == "NOT-A-GRANT", "the deed summary graded %s" % verdict
    assert "pointer phrase" in why, \
        "the deed must be caught by the POINTER channel, not only by length: %s" % why


@check
def test_a_real_legalcode_is_not_graded_a_notice():
    """🔴 The control that makes item 4 safe to use. A floor-and-pointer test that
    condemned real grants would exclude usable supply, which is the SAME cost
    direction as the blindness this pass is measuring."""
    for prefix in ("mpl-2.0-common-voice", "mit-educhain",
                   "bsd-3-clause-freecodecamp", "mit-crewai"):
        _p, fam = prefix, dict((p, f) for p, f, _c, _w in FX.DECLARED)[prefix]
        verdict, why = PID.is_this_a_grant(_text(prefix), fam)
        assert verdict == "GRANT", "%s graded NOT-A-GRANT (%s)" % (prefix, why)


@check
def test_is_this_a_grant_is_asymmetric_and_says_so():
    """🔵 `GRANT` is the absence of a refutation, never a certification, and the
    docstring must keep saying so — a caller that reads it as a clean bill of
    health has the same bug `p310` had when it read `bytes` + `sha` as a licence
    instrument."""
    doc = PID.is_this_a_grant.__doc__ or ""
    assert "never a certification" in doc
    _v, why = PID.is_this_a_grant(_text("mit-educhain"), "MIT")
    assert "NOT a certification" in why, \
        "the GRANT verdict's own reason string must carry the caveat: %r" % why


@check
def test_the_floor_is_per_family_because_the_legalcodes_differ_threefold():
    """🔴 A single global floor would either miss `CC0-1.0` notices or condemn its
    grant: `CC0-1.0` is `7 048` B against ~`19 KB` for `CC-BY-NC-4.0`, both read
    first-hand by `p310`'s arm."""
    floors = PID._LEGALCODE_FLOOR
    assert floors["CC0-1.0"] < floors["CC-BY-NC-4.0"]
    assert floors["CC0-1.0"] < 7048, "the CC0 floor must sit below its own legalcode"
    # 🟢 and the CC0 legalcode itself must pass the floor it is below
    assert max(floors.values()) < 19347, \
        "a floor at or above a measured legalcode length would condemn a real grant"


@check
def test_the_verdict_token_avoids_the_path_vocabulary_that_moves_the_ratchet():
    """🔴 `ACTION p311-R` item 4's class, met a third time and caught within the
    hour by `p283-ladder-case-audit` rather than at the next pass.

    `is_this_a_grant`'s second verdict was first written as the plain English
    word for a distribution notice. That word is `p283`'s PATH vocabulary, and
    putting it in a CODE string rather than a comment regraded
    `payload_identity.py` from `COMMENT-ONLY` to `SINGLE-SPELLING` — moving the
    STANDING ratchet for a module that probes no paths at all. `p283`'s own
    control C16 is exactly this negative arm.
    🟢 The ratchet was right. The token was renamed, not the ceiling raised, and
    this control keeps it renamed: a future edit that reaches for the natural
    word will fail here instead of in the standing suite."""
    verdicts = set()
    for prefix, fam, _com, _why, text, _n, _s in FX.declared():
        verdicts.add(PID.is_this_a_grant(text, fam)[0])
    assert verdicts, "no verdicts produced"
    forbidden = {"notice", "readme", "copying", "licence", "license"}
    for v in verdicts:
        assert v.lower() not in forbidden, \
            "verdict %r is p283 path vocabulary — it will move the ladder ratchet" % v


@check
def test_a_bare_citation_pins_as_cleanly_as_a_legalcode():
    """🔴 The point of the whole item, stated as a control: the pinning channel
    cannot tell these apart. `209` B and `35 136` B pin identically well, so no
    amount of care with `bytes` + `sha` would ever have surfaced `p313`'s
    finding."""
    for prefix in ("cc-by-nc-nd-4.0-shule-ai", "mpl-2.0-common-voice"):
        text, n, sha = FX.load(prefix)
        assert n > 0 and len(sha) == 12
        assert PID.raw_identity(text) == (n, sha)


def main():
    failed = 0
    for fn in CHECKS:
        try:
            fn()
        except AssertionError as exc:
            failed += 1
            print("🔴 FAIL %s\n       %s" % (fn.__name__, exc))
        except Exception as exc:                        # noqa: BLE001
            failed += 1
            print("🔴 ERROR %s\n       %s: %s" % (fn.__name__, type(exc).__name__, exc))
    print("# %d controls, %d failed" % (len(CHECKS), failed))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
