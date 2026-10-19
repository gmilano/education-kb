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
    if family in FILL_IN_SLOT:
        body = _HOLDER.sub("copyright <HOLDER>", body)
    raw = body.encode("utf-8")
    return len(raw), _sha12(raw)


def same_grant(a, b, family=None):
    """Do two payloads carry the SAME grant document?"""
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
