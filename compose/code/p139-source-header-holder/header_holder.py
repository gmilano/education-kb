"""p139-source-header-holder — classify a copyright header line by HOLDER.

`p137-foreign-holder-tree` asked which repositories carry a foreign licence FILE
outside the root. Eight rows came back `ROOT_ONLY`: one licence file, nothing else
licence-shaped in the tree. `ACTION CJ` asks the next question down — whether the
SOURCE FILES of those rows name a holder the root file does not.

The classifier is separate from the collector for two reasons:

1.  It is testable offline, and the first draft of this probe published a foreign
    holder (`Junio C Hamano`) that came from `.git/hooks/pre-rebase.sample` — git's
    own sample hook, shipped by the clone, not content of the repository. The
    collector now walks `git ls-tree -r HEAD` so that `.git/` cannot be read at all,
    and `is_vcs_artifact` keeps a second guard in testable code.
2.  "Foreign" is a judgement about legal identity, not a string comparison. It is
    made against an explicit, recorded list of the row's own holder names, so that
    a reader can disagree with the list rather than having to re-derive it.
"""

import re

# A header line, not a licence body.
#
# The marker is REQUIRED: a `(c)`/`©` sign, a year, or both. Without that requirement
# the pattern reads the AGPL's own prose as holders -- `"Copyright" also means
# copyright-like laws that apply to other kinds of` yields the "holder"
# `also means copyright-like laws…`, and five such lines were published by the first
# run of this probe against `frappe/lms`'s `license.txt`. Every real header fixture
# in `test_header_holder.py` carries a marker; none of the prose fixtures does.
#
# `copyright\b` also stops `copyrightable` and `copyright-like` from matching at all.
_YEAR = r"(?:19|20)\d{2}(?:\s*[-–,]\s*(?:(?:19|20)\d{2}|present|TODAY|Today|today))?"
_HEADER = re.compile(
    r"copyright\b[\s:]*"
    r"(?:"
    r"(?:\(c\)|\(C\)|©)\s*,?\s*(?:" + _YEAR + r")?"   # (c) with an optional year
    r"|" + _YEAR +                                      # or a bare year
    r")"
    r"\s*,?\s*(?P<holder>[^\n]{2,120})",
    re.IGNORECASE,
)

# The JSDoc form, where the year TRAILS the holder: `@copyright Chen, Yi-Cyuan 2014-2023`
# (js-sha256, vendored into academico-sis/academico). Requiring the marker to PRECEDE the
# holder dropped this real foreign holder, so the trailing-year form is matched too. A
# year is still mandatory, which is what keeps the eight AGPL prose lines out: none of
# them contains one.
_HEADER_TRAILING_YEAR = re.compile(
    r"copyright\b[\s:]*(?P<holder>[^\n]{2,80}?)\s*,?\s*" + _YEAR + r"\s*$",
    re.IGNORECASE,
)

# Sentence machinery. A holder is a name; these words mean the match is licence prose.
_PROSE = re.compile(
    r"\b(?:that|which|than|means|except|unless|whether|shall|may|must|"
    r"notice|notices|holder|holders|law|laws|work|works|permission|"
    r"licensed under|provided|displays|assert|offer)\b",
    re.IGNORECASE,
)

# Tails that are part of the notice, not part of the holder's name.
# NOTE: an `Inc`/`Ltd` suffix is part of the holder's legal name and must survive.
# An earlier draft stripped from `inc(` onward and reported `OpenEduCat Inc(<http://…>)`
# as `OpenEduCat`, losing the incorporation — so the URL parenthetical is what gets
# matched here, not the word before it.
_TAIL = re.compile(
    r"\s*(?:all rights reserved|and contributors?|and its contributors?|"
    r"& contributors?|and project contributors?|et al\.?|"
    r"\(?\s*<[^>]*>|\(\s*https?://[^)]*\)?|https?://\S+)\s*.*$",
    re.IGNORECASE,
)

# Comment punctuation and decoration that brackets a header in source files.
# The trailing class includes `(` so that a stripped URL parenthetical leaves no stub.
_DECOR = re.compile(r"^[\s*#/<!;%\-\"'=|.]+|[\s*#/<>!;%\-\"'=|,.()]+$")

# Paths that a clone creates or vendors but that are not the repository's own source.
_VCS_ARTIFACT = re.compile(r"(^|/)\.git(/|$)")


def is_vcs_artifact(path):
    """True for paths inside a `.git` directory.

    The collector never emits these, because it reads `git ls-tree -r HEAD` rather
    than the working directory. This stays as a second guard in tested code: the
    first draft of this instrument reported `Junio C Hamano` as a foreign holder of
    `openeducat/openeducat_erp` on the strength of `.git/hooks/pre-rebase.sample`.
    """
    return bool(_VCS_ARTIFACT.search(path))


def extract_holder(line):
    """Return the normalised holder named in a copyright header, or None.

    None means "this line is not a holder-bearing header" — including the bare
    licence-body line `Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>`
    reduced to an empty holder, and prose such as `copyright notices during`.
    """
    if line is None:
        return None
    m = _HEADER.search(line) or _HEADER_TRAILING_YEAR.search(line)
    if not m:
        return None
    holder = m.group("holder")
    holder = _TAIL.sub("", holder)
    holder = _DECOR.sub("", holder)
    holder = re.sub(r"\s+", " ", holder).strip(" ,.;:-")
    if len(holder) < 3:
        return None
    # Prose that mentions the word but names nobody: "copyright notice for the Library",
    # "copyright & licensing details" (OpenEduCat's own file-reference line).
    if re.match(r"^(notice|notices|information|holder|holders|statement|details|"
                r"and|or|the|is|in|to|for|of|&)\b", holder, re.IGNORECASE):
        return None
    if _PROSE.search(holder):
        return None
    # A name starts with a letter or digit, not with a conjunction or punctuation stub.
    if not re.match(r"^[A-Za-z0-9]", holder):
        return None
    return holder


def classify(holder, own_names):
    """OWN if the holder matches one of the row's recorded own names, else FOREIGN.

    `own_names` is explicit and recorded in the result, not inferred from the slug:
    `frappe/lms` is held by both `Frappe` and `FOSS United`, and no slug says so.
    Matching is case-insensitive containment either way, so that `Frappe` matches
    `Frappe Technologies Pvt. Ltd.` and vice versa.
    """
    if holder is None:
        return None
    h = holder.casefold()
    for name in own_names:
        n = name.casefold()
        if n and (n in h or h in n):
            return "OWN"
    return "FOREIGN"


# The licence steward's own text, vendored. A notice obligation attaches to it, but it
# is not a third party's grant over the row's code, and p137 counted it separately.
_STEWARD = (
    "free software foundation",
    "fsf",
    "open source initiative",
)


def is_steward(holder):
    if holder is None:
        return False
    h = holder.casefold()
    return any(s in h for s in _STEWARD)
