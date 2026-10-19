#!/usr/bin/env python3
"""p311 — payload IDENTITY, separated from payload BYTES.

🔴 THE DEFECT THIS ANSWERS.  This base pins every payload as `bytes` +
`sha256_12`, which is the right evidence format and makes a claim re-checkable.
`p310` then used it as a LICENCE INSTRUMENT: seven CC0 rows were certified partly
on *"six at the legalcode's exact `7 048` B"*.  🔵 Byte length and sha answer
*"is this the same FILE?"*.  They were read as answering *"is this the same
GRANT?"*, and those are two questions — `P250`'s lesson, in a third channel.

Measured on the two families this base publishes most:

  🔴 **fixed document.** `NoplagLabs/noplag-engine` serves the Apache-2.0
  legalcode at `11 358` B / `cfc7749b96f6`; `constructorfabric/reference-audit`
  serves it at `11 357` B / `c71d239df917`.  `noplag[1:] == reference-audit`
  exactly — **one leading newline** — and the two shas share no prefix.  An
  identical grant, and every byte-or-sha test calls them different documents.

  🔴 **fill-in slot.** `Open-Detector` (`1 066` B) and `GradeBridge` (`1 100` B)
  are the SAME 21-line MIT template; exactly one line differs and it is the
  `Copyright` line.  The 34-byte delta IS the holder string.  So for `MIT`,
  `BSD`, `ISC` and every other fill-in-slot family, byte length is a function of
  a field that is not the grant, and an exact-byte-length test cannot certify
  the family even in principle.

🟢 WHAT THIS MODULE DOES NOT DO.  It does not decide the family — `p198`,
`p150` and `p124` already own that channel and this file delegates rather than
restating them (`p309`: *"import the discriminator, never restate it"*).  It
answers exactly one question: **once the parts that are not the grant are
normalised away, is this the same grant document?**

🔵 The normalisation is deliberately MINIMAL and each step is named, because a
normaliser that keeps being widened until everything matches proves nothing.
`fixtures.py` carries a TRUE positive and a TRUE negative for the same grant so
the controls can show the oracle still separates them.
"""
import hashlib
import re

# 🔵 Step 1. Leading and trailing whitespace. This is the step the Apache pair
# needs and it is the whole of their difference.
# 🔵 Step 2. Line-ending form. Not exercised by this pass's four payloads (all
# LF) and declared anyway, because a CRLF copy of a legalcode is the same grant
# and this base has not yet met one. Stated as UNEXERCISED in the controls.
# 🔵 Step 3. The fill-in slot, and ONLY for the families that have one. The MIT
# holder line is REPLACED BY A MARKER, never deleted: a template whose holder
# line is missing entirely is a different document from one that carries it, and
# collapsing those two would be exactly the over-loosening this file warns about.
# 🔴 THE FIRST BUILD OF THIS LINE WAS `^\s*copyright\s*(?:\(c\)|©)?.*$` AND IT WAS
# A WHOLE-BODY SCAN WEARING AN ANCHOR. On the Apache-2.0 payloads it returned
# *"copyright notice that is included in or attached to the work"* — section 4(c)
# PROSE, matched because the line happens to begin with the word. 🔵 That is this
# base's most-repeated defect class in a new place (`p306`'s `"affero" in low`,
# `p306`'s `"cc0" in low`), met while BUILDING the instrument that complains about
# it, and it is kept as a named negative control rather than quietly corrected.
#
# 🟢 A copyright NOTICE is the word plus an identified YEAR. Requiring a 4-digit
# year separates all three cases on the payloads this pass pinned:
#   `Copyright (c) 2025 LI YUANJI`              -> a notice            ✅
#   `Copyright [yyyy] [name of copyright owner]` -> UNFILLED template  ❌
#   `copyright notice that is included in ...`   -> prose              ❌
# 🔵 And the middle case is the one that matters for agreement: `p310`'s prober
# graded both Apache rows `BLIND-FIXED-DOCUMENT` with holder `-`, so an oracle
# that read the unfilled appendix slot as a holder would silently disagree with
# the channel this base already publishes.
_HOLDER = re.compile(r"^\s*copyright\s*(?:\(c\)|©)?\s*\d{4}.*$", re.I | re.M)

# 🔵 p314 / step 0c, below. Deliberately the narrowest form that answers the
# measured case: the scheme token of an absolute URL, nothing else. It does NOT
# touch a bare host, a `mailto:`, or any other scheme — a widening with no
# payload behind it is what this module refuses.
_URL_SCHEME = re.compile(r"\bhttps://", re.I)

# Kept so a control can assert the refuted BOM-blind normalisation is still blind.
def _canonical_strip_only_REFUTED_P311(text):
    """The first build's normalisation: `strip()` with no BOM step. Kept live as a
    negative control — see `canonical_identity`'s step 0."""
    import hashlib as _h
    body = text.strip().replace("\r\n", "\n").replace("\r", "\n")
    return _h.sha256(body.encode("utf-8")).hexdigest()[:12]


# Kept so a control can assert the refuted form is still refuted.
_HOLDER_REFUTED_P311 = re.compile(r"^\s*copyright\s*(?:\(c\)|©)?.*$", re.I | re.M)

# 🔵 Fill-in-slot families, from p310's own holder-channel measurement:
# fill-in slot -> 13 of 13 holder lines read; fixed document -> 0 of 6.
FILL_IN_SLOT = {"MIT", "BSD-3-Clause", "BSD-2-Clause", "ISC", "0BSD"}


def _sha12(raw):
    return hashlib.sha256(raw).hexdigest()[:12]


def raw_identity(text):
    """`(bytes, sha256_12)` — the file, exactly as this base already pins it."""
    raw = text.encode("utf-8")
    return len(raw), _sha12(raw)


def canonical_identity(text, family=None):
    """`(bytes, sha256_12)` of the GRANT, with the non-grant parts normalised.

    `family` is optional and only selects whether the fill-in slot is masked.
    🔴 Passing a family this module does not list as fill-in-slot leaves the
    holder line INTACT, which is correct for `Apache-2.0`: its appendix slot is
    not part of the grant body and is normally unfilled, so masking there would
    be a change with no payload to justify it.
    """
    # 🔴 Step 0, and it was MISSING from the first build of this module — found
    # when `gate-enumeration` refuted a different claim and handed this pass
    # `OS4ED/openSIS-Classic`'s `docs/License.txt`, whose first three bytes are
    # `ef bb bf`. 🔵 `str.strip()` does NOT remove `U+FEFF`: Python does not
    # classify the BOM as whitespace, so a BOM'd copy and a BOM-less copy of one
    # grant produced two different canonical shas — `9bd1685b5dad` against
    # `5f42dc1e0231`. 🔴 **An invisible one-character prefix defeating an identity
    # is the exact case this module was built for, and it was built with the case
    # open.** The Apache pair's leading newline was caught because a newline IS
    # whitespace; the BOM is not, and nothing in the first build noticed the
    # difference between "invisible" and "whitespace".
    body = text.lstrip("\ufeff")
    body = body.strip()
    body = body.replace("\r\n", "\n").replace("\r", "\n")
    # \ud83d\udd34 Step 0b, added at `p312`, and it is step 0's own lesson one position
    # further in. `p311` wrote that *"nothing in the first build noticed the
    # difference between 'invisible' and 'whitespace'"* and repaired the case
    # where the invisible byte is a PREFIX. \ud83d\udd34 It is not always a prefix. Two
    # `MPL-2.0` payloads on this base \u2014 `aesophor/hacklympics` (`16 725` B
    # `1f256ecad192`) and `SafeExamBrowser/seb-win-refactoring` (`16 726` B
    # `fab3dd6bdab2`) \u2014 carry the SAME grant and differ by **one trailing space
    # before a newline at offset 1 282**: `"...with other material, in \n"`
    # against `"...with other material, in\n"`. \ud83d\udd35 `strip()` cannot reach it
    # because it is INTERIOR, so `same_grant()` returned **False** for a single
    # document \u2014 a FALSE NEGATIVE on grant identity, which inflates a family's
    # apparent variability and is exactly what feeds the byte-band confusion
    # `P312-T` is about. \ud83d\udfe2 Trailing whitespace on a line is never part of a
    # grant, and hand-editing a licence file is how it gets there.
    body = "\n".join(line.rstrip() for line in body.split("\n"))
    # 🔵 Step 0c, added at `p314` — `ACTION p313-R` item 2a, and it is step 0b's
    # lesson one layer further out: the difference that is not in the grant need
    # not be whitespace at all. 🔴 MEASURED on a single document.
    # `SafeExamBrowser/seb-win-refactoring` and `mozilla/common-voice` both serve
    # the `MPL-2.0` legalcode at **exactly `16 726` B** — and they are DIFFERENT
    # FILES (`fab3dd6bdab2` against `3f3d9e0024b1`). After step 0b the sole
    # residual difference is the URL SCHEME in the *Exhibit A* notice: one cites
    # the licence over `http`, the other over `https`. 🔵 `same_grant()` returned
    # **False** for one grant — a FALSE NEGATIVE, the same direction as 0b's.
    #
    # 🟢 WHY THE STEP IS SAFE AND BOUNDED, which matters because this module's own
    # docstring warns against a normaliser widened until everything matches: it
    # rewrites the SCHEME of an `https` URL and nothing else. 🔴 No two licence
    # families differ solely by the transport scheme of a URL they cite, so the
    # step cannot merge two distinct grants, and the TRUE-negative control in
    # `test_p311.py` asserts the oracle still separates them.
    # 🔴 And the residual risk is named rather than normalised away: the operative
    # text can LIVE at that URL (`p313`'s finding on the four noncommercial
    # notices), so making two citations of one resource compare equal does not
    # make that resource's content known.
    body = _URL_SCHEME.sub("http://", body)
    if family in FILL_IN_SLOT:
        body = _HOLDER.sub("copyright <HOLDER>", body)
    raw = body.encode("utf-8")
    return len(raw), _sha12(raw)


# 🔵 p314 / `ACTION p313-R` item 4. The legalcode lengths this base has measured
# first-hand, as a floor per family. Each is the SHORTEST payload this base has
# read and confirmed to be the operative text, less a margin — never a published
# constant from elsewhere.
#   `CC-BY-NC-SA-4.0` ≈ 19 KB · `CC-BY-NC-ND-4.0` ≈ 18 KB   (p313, by inspection)
#   `CC-BY-NC-4.0`      19 347 B                            (p310 dynamic arm)
#   `CC-BY-4.0`         18 873 B · `CC0-1.0`  7 048 B       (p310 dynamic arm)
# 🔴 The floors are per FAMILY because they differ by a factor of three, and a
# single global floor would either miss `CC0-1.0` notices or condemn its grant.
_LEGALCODE_FLOOR = {
    "CC-BY-NC-SA-4.0": 15000,
    "CC-BY-NC-ND-4.0": 15000,
    "CC-BY-NC-4.0": 15000,
    "CC-BY-SA-4.0": 15000,
    "CC-BY-ND-4.0": 15000,
    "CC-BY-4.0": 15000,
    "CC0-1.0": 5000,
}

# 🟢 A pointer is what these payloads have INSTEAD of terms, and the phrasing is
# remarkably stable across all four `p313` read: a deed summary disclaims itself
# in those words, and a bare notice sends the reader to a URL.
_POINTER_RE = re.compile(
    r"human-readable summary of|not a substitute for|"
    r"complete license text is available|full (?:text|license) (?:is )?(?:available|at)",
    re.I)


def is_this_a_grant(text, family=None):
    """`GRANT`, or `NOT-A-GRANT` with the reason — asked BEFORE `same_grant`.

    🔵 The second verdict is spelled `NOT-A-GRANT` and not the obvious English
    word, which would read better here and would be wrong: that word is the
    `p283-ladder-case-audit` PATH vocabulary for a repository's own
    distribution-notice rung, and putting it in a code string — as opposed to a
    comment — regrades this file from `COMMENT-ONLY` to `SINGLE-SPELLING` and
    moves the STANDING ratchet for a module that probes no paths at all.
    🔴 That is `ACTION p311-R` item 4's class, met for the third time on this
    base and the first time while the ratchet was watching: `p311`'s own
    `fixtures.py` records losing a licence TITLE to it, and the audit caught this
    one within the hour. 🟢 The ratchet was right and the token was renamed
    rather than the ceiling raised.

    🔴 `ACTION p313-R` item 4, and `p313` is the pass that earned it. It pinned
    four `CC-BY-NC-*` payloads as `bytes` + `sha` and only then noticed, by
    reading them, that **not one was an operative grant**: a deed summary that
    disclaims itself in its own line 5, a hand-written paraphrase carrying terms
    the legalcode does not contain, and two bare notices of `224` B and `209` B.
    🔵 Every one of them pinned cleanly, because a pin records the bytes and never
    asks what the bytes ARE.

    🟢 This is the cheaper question underneath `p311`'s rule, and it closes the
    CLASS rather than the four instances: *bytes and sha answer «is this the same
    FILE?»; `same_grant()` answers «is this the same GRANT?»; neither of them
    answers «is this a grant AT ALL?»* — and the third question needs no new
    channel, because this base already stores the byte count that settles it.

    🔴 The control is deliberately ASYMMETRIC, and that is the whole design.
    Returning `GRANT` means only *"not caught by a floor or a pointer phrase"* —
    it is the absence of a refutation, never a certification. The other verdict
    is the load-bearing answer: under `P250` an incompletely perfected grant is
    `UNDETERMINED`, which is indistinguishable from `PROHIBITED`, so this
    function can only ever move a payload toward the SAFE verdict.
    """
    body = text.lstrip("﻿").strip()
    n = len(body.encode("utf-8"))
    floor = _LEGALCODE_FLOOR.get(family)
    hit = _POINTER_RE.search(body)
    if hit:
        return "NOT-A-GRANT", \
            "carries a pointer phrase, not terms: %r" % (hit.group(0),)
    if floor is not None and n < floor:
        return "NOT-A-GRANT", (
            "%d B is below the %s legalcode floor of %d B — a payload this short "
            "is a bare citation or a deed summary, not the operative text"
            % (n, family, floor))
    return "GRANT", "no floor or pointer refutation (NOT a certification)"


def same_grant(a, b, family=None):
    """Do two payloads carry the SAME grant document?

    🔵 `p314`: callers that care whether the answer is MEANINGFUL should ask
    `is_this_a_grant()` first — two notices citing one URL are the same FILE and
    tell you nothing about the terms. This function deliberately does not fold
    that question in, because `same_grant` has one job and `P250`'s lesson on
    this base is that two questions in one answer is how a channel goes wrong.
    """
    return canonical_identity(a, family)[1] == canonical_identity(b, family)[1]


def holder_line(text):
    """The `Copyright` line as written, or `None`. 🔵 p129 owns the HOLDER
    question; this returns the raw line so a caller can hand it to p129 rather
    than re-deriving a grade here."""
    m = _HOLDER.search(text)
    return m.group(0).strip() if m else None


def report(rows):
    """`rows` = [(name, family, text)] -> printable identity table."""
    out = []
    for name, fam, text in rows:
        rn, rs = raw_identity(text)
        cn, cs = canonical_identity(text, fam)
        out.append((name, fam, rn, rs, cn, cs, holder_line(text)))
    return out


def _load_fixtures():
    """🔵 Loaded BY PATH, never `import fixtures`. Two reasons, both already
    paid for on this base: `-I` strips the script's own directory from
    `sys.path` (`p355-cwd-portability`, and the whole reason a working gate
    stayed a one-off for eleven passes), and `fixtures` is a name three
    instruments here use, so first loader wins (`p150-identifier-collision`,
    met again by `p310`'s arm)."""
    import importlib.util
    import os
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures.py")
    spec = importlib.util.spec_from_file_location("p311_fixtures", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


if __name__ == "__main__":
    rows = [(n, f, t) for n, f, _c, _w, t, _b, _s in _load_fixtures().declared()]
    print("# p311 — raw identity (what this base pins) vs CANONICAL identity")
    print("# %-30s %-11s %18s %18s" % ("payload", "family", "RAW", "CANONICAL"))
    for name, fam, rn, rs, cn, cs, hold in report(rows):
        print("  %-30s %-11s %6d B %s   %6d B %s" % (name, fam, rn, rs, cn, cs))
        print("  %-30s %-11s holder: %s" % ("", "", hold or "— (fixed document)"))
    print()
    groups = {}
    for name, fam, _rn, rs, _cn, cs, _h in report(rows):
        groups.setdefault((fam, cs), []).append((name, rs))
    print("# 🟢 grouped by CANONICAL sha — one row per distinct GRANT:")
    for (fam, cs), members in sorted(groups.items()):
        print("  %-11s %s  <- %d payload(s), raw shas: %s"
              % (fam, cs, len(members), ", ".join(s for _n, s in members)))
