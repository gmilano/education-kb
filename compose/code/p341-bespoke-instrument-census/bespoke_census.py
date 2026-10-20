"""`p341-bespoke-instrument-census` — T29's open question, with a denominator.

`p340` closed T25's falsifier and opened a question it explicitly recorded as
unmeasured:

    🟡 Open question nobody has measured: how many `LICENSE*` payloads on these
    shelves are bespoke instruments rather than stock texts?  `p1054-mit-plus-clause`
    exists for the added-restriction case; the fully-bespoke case has no census.

🔵 THIS FILE IS NOT A NEW CLASSIFIER.  `p340`'s fifth-named standing failure is
"instrument built, documented, not re-run", and the honest reading of T29 is that
the *detection* already exists in three places and the *census* exists nowhere:

  * `pass257-restriction-scan.scan()` — the unscoped restriction vocabulary, with
    `BENIGN_FAMILY_HITS` already absorbing the `GPL-3.0` §6 `noncommercially`
    trap that pass 15 of 2026-10-06 published four wrong rows from.
  * `p1054-mit-plus-clause.classify()` — the MIT-body-plus-a-clause rider.
  * `p241-blanket-denial.verdict()` — reserves rights, grants nothing.

So the grading limbs below DELEGATE.  What this file adds is the one axis none of
them carries, and it is the axis `AStheTECH/mewcp-google-classroom` turns on:

🟢 **THE TITLE FORM.**  `pass257.family_of` resolves a family from the title line
*or*, when the title named nothing, from an operative body anchor.  Both answers
arrive in one field, so a payload titled **"AStheTECH Community License"** whose
body recites a stock grant is indistinguishable, in that field, from a payload
titled "MIT License".  The distinction is the whole finding: a bespoke instrument
that recites a stock grant and then qualifies it reads as stock to every naive
"is it licensed?" check, which is exactly how `AStheTECH` passed.

🔴 WHY NOT `p312.identify`.  `p312-template-identity` answers "is this payload
byte-identical to a known template" and returns `UNKNOWN-TEMPLATE` otherwise.  Its
registry is DERIVED FROM ITS FIXTURES — MIT, Apache-2.0, BSD-2-Clause, MPL-2.0,
GPL-2.0 — so a verbatim `BSD-3-Clause` or `AGPL-3.0` payload, and a verbatim MIT
payload that merely wraps its lines differently, all return `UNKNOWN-TEMPLATE`.
Reading `UNKNOWN-TEMPLATE` as "bespoke" would report most of this corpus as
bespoke.  🔵 That is `p310`'s byte-band error in a new costume — *a band always
answers, and at the edges it answers wrongly and silently* — and p312's own
docstring says it returns `UNKNOWN-TEMPLATE` "never a nearest match".  Measured
here rather than argued: `test_p312_is_not_a_bespoke_detector`.

The census is therefore `title_form` × `pass257.scan().verdict`, over the live
decision shelves, every payload read first-hand.

Vocabulary, so a reader can print it (`T272`: a list you cannot print is a list
that gets copied):

    SPDX-TITLED      the title line names a family in `pass257.TITLE_ANCHORS`
    BESPOKE-TITLED   the title NAMES AN INSTRUMENT and no anchor matches it
    UNTITLED         no instrument-naming title line at all (`p314`'s class)

🔴 `UNTITLED` is deliberately NOT merged into `BESPOKE-TITLED`.  `p314` measured
the untitled class and found complete, stock `MIT` grants whose title line is
simply absent — `Priyamakeshwari/TeachGPT`, 1 057 B, cited in `pass257`'s own
`BODY_ANCHORS` comment.  An untitled stock grant and a bespoke instrument are
opposite findings and a census that fuses them answers nothing.
"""

import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_CODE = os.path.dirname(_HERE)

# Delegation, not re-implementation.  Each of these directories owns its own
# suite; nothing below re-derives a vocabulary one of them already holds.
sys.path.insert(0, os.path.join(_CODE, "pass257-restriction-scan"))
sys.path.insert(0, os.path.join(_CODE, "p1054-mit-plus-clause"))
sys.path.insert(0, os.path.join(_CODE, "p241-blanket-denial"))

import restriction_scan as p257      # noqa: E402
import mit_plus as p1054             # noqa: E402
import blanket_denial as p241        # noqa: E402

SPDX_TITLED = "SPDX-TITLED"
BESPOKE_TITLED = "BESPOKE-TITLED"
UNTITLED = "UNTITLED"

TITLE_FORMS = (SPDX_TITLED, BESPOKE_TITLED, UNTITLED)

# How many leading lines count as the title.  Held EQUAL to `pass257.TITLE_LINES`
# by assertion in the suite, not by copying the number: two instruments reading
# "the title" over different windows is a conflict that would surface as an
# unexplained disagreement between this census and the scanner it delegates to.
TITLE_LINES = p257.TITLE_LINES

# A title line that NAMES AN INSTRUMENT.  Deliberately narrow: these are the
# words a document uses to call itself a licence.  A bare copyright line, a
# project name or a `#` heading carries none of them and is `UNTITLED`.
#
# 🔴 BARE `agreement` WAS IN THIS TUPLE AND IS REMOVED, by measurement rather
# than by taste.  `pass257`'s `usc-academic-1812` fixture — a real non-commercial
# academic licence — opens on a copyright line whose SECOND line reads
# "… without fee and without a written agreement is hereby granted".  Over a
# 4-line window, bare `agreement` matched that body prose and typed the payload
# `BESPOKE-TITLED` on the strength of a phrase that is not a title at all.
# 🟢 Nothing is lost by dropping it: `graspful`'s "O'Saasy License Agreement"
# still matches on `license`, and the `usc` row is still `needs_a_human` through
# its restriction hits — which is the point of keeping the limbs separate.
_INSTRUMENT_WORDS = (
    "license",
    "licence",
    "terms of use",
    "terms and conditions",
)

# 🟢 A TITLE IS SHORT.  The second half of the same repair, and the one that
# generalises: the instrument word must appear in a line that is SHAPED like a
# title, not merely within the first few lines of the document.
#
# Measured against every titled payload this base has pinned: `MIT License` (11),
# `Apache License` (14), `GNU GENERAL PUBLIC LICENSE` (26),
# `# O'Saasy License Agreement` (27), `# AStheTECH Community License (ACL)` (35),
# `# OpenGaokao Source-Available License 1.0` (41) — and against the prose lines
# that must NOT qualify: `usc-academic`'s permission sentence (221 B),
# `uchicago`'s "BY DOWNLOADING THE STUDENT EARLY WARNING SYSTEM …" (139 B) and
# `cc-by-nc-nd`'s "The treebank is licensed under the Creative Commons …" (224 B).
# 🔵 `60` sits in a gap between 41 and 139 that is wide enough that no pinned
# payload is near the boundary — stated because a threshold with a fixture ON it
# is a threshold that will move, and `p310`'s byte-band lesson applies to every
# constant, including this one.
#
# 🔴 SCOPE, and it is deliberate: this constraint governs the INSTRUMENT-WORD
# limb only.  The SPDX-anchor limb keeps `pass257`'s own 4-line window verbatim,
# because two instruments reading "the title" over different windows is exactly
# the channel conflict `p278` exists to forbid.
TITLE_MAX_BYTES = 60

# 🔵 Stripped before the anchor test, never before the instrument test.  A
# markdown heading marker and surrounding punctuation are typography; the words
# are the claim.
_DECORATION = re.compile(r"^[\s#*_=\-]+|[\s#*_=\-]+$")


def title_lines(text):
    """The leading non-blank lines that count as the title, verbatim, in order."""
    raw = text if isinstance(text, str) else text.decode("utf-8", "replace")
    return [ln for ln in raw.splitlines() if ln.strip()][:TITLE_LINES]


def _title_blob(text):
    return "\n".join(_DECORATION.sub("", ln) for ln in title_lines(text)).lower()


def titled_family(text):
    """The family the TITLE names, or None — the title stage of `pass257` alone.

    🔵 This exists because `pass257.family_of` fuses two stages into one answer
    by design (correctly: a caller asking "what family is this" wants either).
    The census needs the stages SEPARATED, so it re-asks the first one over the
    same vocabulary object rather than over a copy of it.
    """
    head = _title_blob(text)
    for anchor, fam in p257.TITLE_ANCHORS:
        if anchor in head:
            return fam
    return None


def title_shaped_lines(text):
    """The leading lines that are SHAPED like a title: short, after decoration.

    🔵 Returned as a list rather than folded into a boolean so a census row can
    name the line it matched on.  An unexplained class is a class the next pass
    re-derives.
    """
    out = []
    for ln in title_lines(text):
        stripped = _DECORATION.sub("", ln)
        if len(stripped.encode("utf-8")) <= TITLE_MAX_BYTES:
            out.append(stripped)
    return out


def names_an_instrument(text):
    """Does a TITLE-SHAPED leading line call itself a licence/terms document?"""
    blob = "\n".join(title_shaped_lines(text)).lower()
    return any(w in blob for w in _INSTRUMENT_WORDS)


def title_form(text):
    """`SPDX-TITLED` / `BESPOKE-TITLED` / `UNTITLED`.

    🔴 Order is load-bearing.  A payload titled "GNU General Public License"
    both matches an anchor AND names an instrument; it is SPDX-titled, and
    asking the instrument question first would type every stock licence bespoke.
    """
    if titled_family(text) is not None:
        return SPDX_TITLED
    if names_an_instrument(text):
        return BESPOKE_TITLED
    return UNTITLED


def grade(text):
    """One payload, fully graded, with every limb's own answer kept separate.

    Nothing here collapses two limbs into a verdict.  `p278`'s rule is that a
    conflict between channels must stay VISIBLE, and the interesting rows in
    this census are exactly the ones where the limbs disagree — a bespoke title
    over a body the scanner reads as `PERMISSIVE` is a row a human must read.
    """
    raw = text if isinstance(text, str) else text.decode("utf-8", "replace")
    s = p257.scan(raw)
    tf = title_form(raw)
    tfam = titled_family(raw)

    return {
        "title_form": tf,
        "titled_family": tfam,
        # `pass257`'s fused answer, kept so the census can show WHERE the family
        # came from: a family with no titled family came from a body anchor.
        "scan_family": s["family"],
        "family_channel": (
            "TITLE" if tfam is not None
            else ("BODY" if s["family"] is not None else "NONE")
        ),
        "scan_verdict": s["verdict"],
        "effective_hits": s["effective_hits"],
        "benign_hits": s["benign_hits"],
        "bytes": s["bytes"],
        "language": s["language"],
        # The two delegated limbs, verbatim.
        "p1054_verdict": p1054.classify(raw).get("verdict"),
        "p241_verdict": p241.verdict(raw),
        "title_line": (title_lines(raw) or [""])[0].strip()[:80],
        "stock": is_stock(raw),
        "needs_a_human": needs_a_human(raw),
    }


def is_stock(text):
    """True only for a payload this census is willing to call a stock text.

    🟢 Stated as a CONJUNCTION of things measured, and deliberately conservative
    in the same direction `P250` requires — a payload this returns False for is
    not thereby unusable, it is a payload whose instrument a human must read.

    The three conditions:
      1. the TITLE names a family (`SPDX-TITLED`), so the document's own claim
         about its identity is a stock one;
      2. `pass257` finds no EFFECTIVE restriction (benign family hits excluded,
         so verbatim `GPL-3.0` still qualifies);
      3. the family the title names is one `pass257` grades, permissive or
         copyleft — an unknown-but-titled family is not a stock text here.

    🔴 Condition 1 is why `AStheTECH` fails this and why `graspful` fails it even
    though its operative paragraph is MIT's word for word.
    """
    raw = text if isinstance(text, str) else text.decode("utf-8", "replace")
    tfam = titled_family(raw)
    if tfam is None:
        return False
    if p257.scan(raw)["effective_hits"]:
        return False
    return tfam in p257.PERMISSIVE_FAMILIES or tfam in p257.COPYLEFT_FAMILIES


def needs_a_human(text):
    """The rows a consultancy must not clear from a scanner's output alone.

    🔵 This is the census's deliverable, not `is_stock`.  A count of stock texts
    is interesting; a NAMED LIST of payloads whose instrument has to be read by
    someone is what an engagement can act on.
    """
    raw = text if isinstance(text, str) else text.decode("utf-8", "replace")
    s = p257.scan(raw)
    if s["effective_hits"]:
        return True
    if title_form(raw) == BESPOKE_TITLED:
        return True
    if s["verdict"] == p257.VERDICT_UNREADABLE:
        return True
    return False


def census(rows):
    """`rows` = iterable of (slug, text).  Returns counts and the named lists.

    🟢 Returns the NAMES, not only the numbers.  `p275`'s lesson is that a count
    without its population is a ladder: the next pass cannot re-check it and the
    one after that restates it.
    """
    by_form = {f: [] for f in TITLE_FORMS}
    by_verdict = {}
    stock, human = [], []
    graded = {}

    for slug, text in rows:
        g = grade(text)
        graded[slug] = g
        by_form[g["title_form"]].append(slug)
        by_verdict.setdefault(g["scan_verdict"], []).append(slug)
        if g["stock"]:
            stock.append(slug)
        if g["needs_a_human"]:
            human.append(slug)

    return {
        "n": len(graded),
        "graded": graded,
        "by_title_form": by_form,
        "by_scan_verdict": by_verdict,
        "stock": stock,
        "needs_a_human": human,
    }


def tsv_header():
    return "\t".join((
        "slug", "bytes", "title_form", "titled_family", "scan_family",
        "family_channel", "scan_verdict", "stock", "needs_a_human",
        "effective_hits", "p1054_verdict", "p241_verdict", "title_line",
    ))


def tsv_row(slug, g):
    return "\t".join(str(x) for x in (
        slug, g["bytes"], g["title_form"], g["titled_family"] or "-",
        g["scan_family"] or "-", g["family_channel"], g["scan_verdict"],
        "YES" if g["stock"] else "no",
        "YES" if g["needs_a_human"] else "no",
        ",".join(g["effective_hits"]) or "-",
        g["p1054_verdict"] or "-", g["p241_verdict"] or "-",
        g["title_line"] or "-",
    ))


def main(argv):
    """Grade payload FILES named on the command line.  Offline."""
    rows = []
    for path in argv[1:]:
        with open(path, "rb") as fh:
            rows.append((os.path.basename(path),
                         fh.read().decode("utf-8", "replace")))
    if not rows:
        print("usage: bespoke_census.py PAYLOAD [PAYLOAD ...]", file=sys.stderr)
        return 2
    print(tsv_header())
    for slug, text in rows:
        print(tsv_row(slug, grade(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
