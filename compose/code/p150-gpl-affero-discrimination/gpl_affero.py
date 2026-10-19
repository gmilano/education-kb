"""p150-gpl-affero-discrimination — `T77`: a plain GPL-3.0 file matches the AGPL pattern.

🔴 **The defect.** `p145-licence-census.identify()` and the copies of it in
`p147-licence-language` and `p149-common-title-licence` carry this rung:

    (re.compile(r"GNU AFFERO GENERAL PUBLIC LICENSE", re.I), "AGPL-3.0"),

and apply it with `rx.search(body)` over the WHOLE licence text. 🔴 **GPL-3.0's own
section 13 is titled "Use with the GNU Affero General Public License"**, and its body
names the Affero licence twice more. So every verbatim GPL-3.0 file on this shelf
matches the AGPL rung before the GPL rung is ever reached.

🔵 **This is `T39`'s class again** — an instrument answering the question it was spelled
to ask. The pattern is correct as a *phrase* and wrong as a *test*, because the phrase
occurs in the body of the licence it is meant to exclude.

## The fix: read the TITLE, not the body

A GNU licence states its identity on a title line in the first few lines of the file.
`title_licence()` reads only that window. AGPL-3.0 is confirmed a second way, by its
operative clause — section 13 "Remote Network Interaction", which is the clause that
makes AGPL different from GPL and which a plain GPL-3.0 file does not contain.

🟢 **Two independent surfaces, and they must agree** — `agree()` returns the verdict
only when the title and the clause say the same thing, and names the disagreement
otherwise, so a hand-edited or dual-licensed file is reported rather than guessed at.
"""
import os
import re

# The title window: a GNU licence names itself on its FIRST non-blank line. 5 lines covers
# the title and version block and nothing else. 🔵 It must stay narrow: widen it far enough
# and it reaches section 13, which is the very text the fix exists to get away from.
TITLE_WINDOW_LINES = 5

TITLES = [
    (re.compile(r"GNU\s+AFFERO\s+GENERAL\s+PUBLIC\s+LICENSE", re.I), "AGPL-3.0"),
    (re.compile(r"GNU\s+LESSER\s+GENERAL\s+PUBLIC\s+LICENSE", re.I), "LGPL"),
    (re.compile(r"GNU\s+GENERAL\s+PUBLIC\s+LICENSE", re.I), "GPL"),
    (re.compile(r"Apache\s+License", re.I), "Apache-2.0"),
    (re.compile(r"Mozilla\s+Public\s+License", re.I), "MPL-2.0"),
    (re.compile(r"MIT\s+License", re.I), "MIT"),
    (re.compile(r"ISC\s+License", re.I), "ISC"),
    (re.compile(r"BSD\s+\d-Clause", re.I), "BSD"),
]

# AGPL-3.0's operative clause. 🔵 This is the *difference* between AGPL and GPL, so it
# is the right second surface: a plain GPL-3.0 file cannot contain it.
AGPL_NETWORK_CLAUSE = re.compile(r"^\s*13\.\s+Remote Network Interaction", re.M)

# GPL-3.0's section 13, which is what makes the naive body matcher fire.
GPL_SEC13_AFFERO = re.compile(r"^\s*13\.\s+Use with the GNU Affero", re.M)

# The rung as published, kept so the defect can be reproduced rather than asserted.
NAIVE_AGPL = re.compile(r"GNU AFFERO GENERAL PUBLIC LICENSE", re.I)


# 🔴 p311: A UTF-8 BOM SILENTLY DISABLED THIS WHOLE SURFACE, AND THE FALLBACK IT
# DROPPED CALLERS ONTO IS THE BODY LADDER THIS MODULE EXISTS TO REPLACE.
# `OS4ED/openSIS-Classic` serves `docs/License.txt` beginning `ef bb bf` — so its
# title line is `"\ufeffGNU GENERAL PUBLIC LICENSE"`, every `TITLES` pattern
# anchors at position 0, and `title_licence()` returned `None`.
# 🔵 `str.strip()` does NOT remove `U+FEFF`: Python does not classify the BOM as
# whitespace, so the existing per-line `.strip()` could never reach it.
# 🔴 The consequence is measured, not hypothetical: `p191-spec-license-sweep`
# imports this function, got `None`, fell through to its own body ladder and
# graded a **GPL-2.0** payload **`GPL-3.0`** — the exact version confusion this
# module's `GNU_FAMILIES` note was written to prevent, reached by disabling the
# instrument rather than by getting it wrong.
# 🟢 One invisible character, removed in one place, for every importer.
def strip_bom(body):
    """`body` without a leading byte-order mark. 🔵 Not `.strip()`'s job."""
    return body.lstrip("\ufeff")


def title_window(body):
    """The first `TITLE_WINDOW_LINES` non-blank lines of a licence file."""
    lines = [ln for ln in strip_bom(body).splitlines() if ln.strip()]
    return "\n".join(lines[:TITLE_WINDOW_LINES])


# A title is a LINE, not a substring. 🔴 Scanning a window for the name anywhere in it
# fails the same way the body matcher does, only over fewer lines: GPL-2.0's preamble
# says "the GNU Lesser General Public License instead", so a window wide enough to hold
# the preamble reads GPL-2.0 as LGPL. The licence name must BE the line.
TITLE_TAIL = re.compile(r"[\s,]*(?:Version\s+[\d.]+.*)?$", re.I)


def title_licence(body):
    """The licence named on the file's TITLE LINE, or None.

    The name must occupy the whole line, optionally followed by a version. 🔵 This is
    what makes the surface independent of the body: no sibling mention inside a sentence
    can satisfy it, because a sentence is never just the licence's name.
    """
    lines = [ln.strip() for ln in strip_bom(body).splitlines() if ln.strip()]
    for line in lines[:TITLE_WINDOW_LINES]:
        for rx, name in TITLES:
            m = rx.match(line)
            if m and TITLE_TAIL.fullmatch(line[m.end():]):
                return name
    return None


VERSION_LINE = re.compile(r"Version\s+(\d+)(?:\.(\d+))?", re.I)

# The GNU family states its version on the line after the title. 🔵 It is load-bearing:
# `qxbao/qldt-hanu-mcp` is GPL-**2.0**, which has no patent grant and no section 13 at
# all, and this shelf published it as `LGPL` with no version.
GNU_FAMILIES = ("GPL", "LGPL", "AGPL-3.0")


def title_version(body):
    """The version stated in the title block, as a string like "3.0", or None."""
    m = VERSION_LINE.search(title_window(body))
    if not m:
        return None
    major, minor = m.group(1), m.group(2)
    return "%s.%s" % (major, minor if minor else "0")


def spdx(body):
    """The SPDX id from the TITLE surface, version included where the family needs one."""
    name = title_licence(body)
    if name is None:
        return None
    if name in ("GPL", "LGPL"):
        ver = title_version(body)
        return "%s-%s" % (name, ver) if ver else name
    return name


def clause_licence(body):
    """AGPL-3.0 or GPL, read from the operative section 13, or None if neither."""
    if AGPL_NETWORK_CLAUSE.search(body):
        return "AGPL-3.0"
    if GPL_SEC13_AFFERO.search(body):
        return "GPL"
    return None


def naive_verdict(body):
    """What the published matcher says. Reproduces the defect."""
    return "AGPL-3.0" if NAIVE_AGPL.search(body) else None


def agree(body):
    """(verdict, surfaces, status) over the two independent surfaces.

    `status` is `AGREE` when both surfaces answer and answer the same, `TITLE_ONLY` when
    only the title answers (a non-GNU licence has no section 13), `DISAGREE` when the two
    answer differently, and `UNDETERMINED` when neither does.
    """
    t = title_licence(body)
    c = clause_licence(body)
    if t and c:
        # GPL's clause surface returns the family "GPL"; the title carries the precision.
        if t == c or (c == "GPL" and t in ("GPL", "LGPL")):
            return t, (t, c), "AGREE"
        return t, (t, c), "DISAGREE"
    if t:
        return t, (t, None), "TITLE_ONLY"
    return None, (None, c), "UNDETERMINED"


LICENCE_NAMES = re.compile(r"(?i)^(LICEN[CS]E|COPYING)(\.[A-Za-z0-9]+)?$")


def read(path, limit=400000):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read(limit)
    except OSError:
        return ""


def census(root, subject):
    """One row: what the published matcher said, what the two surfaces say, and the delta."""
    if not os.path.isdir(root):
        return dict(subject=subject, naive="-", fixed="-", status="NO_CLONE", delta="-")
    names = [f for f in sorted(os.listdir(root)) if LICENCE_NAMES.match(f)]
    if not names:
        return dict(subject=subject, naive="-", fixed="-", status="NO_LICENCE_FILE",
                    delta="-")
    body = read(os.path.join(root, names[0]))
    nv = naive_verdict(body) or "-"
    _fam, _surfaces, status = agree(body)
    fx = spdx(body) or "-"
    delta = "OVERSTATED" if (nv == "AGPL-3.0" and not fx.startswith("AGPL")) else "-"
    return dict(subject=subject, naive=nv, fixed=fx, status=status, delta=delta)
