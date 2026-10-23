#!/usr/bin/env python3
"""p401 — the plugin grant channel, and the title-vs-name classifier.

Two defects this pass measured, both reduced to pure functions so they can be
controlled OFFLINE:

  401-A  A LICENSE-path ladder is structurally blind to a family whose grant
         convention is a notice in the SOURCE FILE HEADER.  Measured over the
         60-address Moodle plugin family: channel P reads 51 grants, the
         LICENSE ladder reads 24.  27 of 51 are ladder-blind.

  401-B  A licence family must be identified by the TEXT'S TITLE, never by its
         name occurring anywhere in the payload.  GPL-3.0 section 13 is titled
         "Use with the GNU Affero General Public License", so a name-anywhere
         match grades every GPL-3.0 payload AGPL.  It did, 7 times, in this
         pass's own first run.

  401-C  `README.md` is not a universal branch control.  raw.githubusercontent
         is CASE-SENSITIVE, so a repository carrying `readme.md` grades
         ADDRESS_UNRESOLVED while being live.  p283's gate-ladder-case found
         this for one ladder family; the branch-control ladder still had it.

No network.  Lineage, so none of this is re-sold as new: p275 found the class
for manifests and docs/License.txt, p394 for CRAN DESCRIPTION
(philchalmers/mirt is already shelved as "grant lives only in DESCRIPTION").
p401 is the same class in the single largest untested family on this shelf.
"""

LADDER = ("LICENSE", "LICENSE.md", "LICENSE.txt", "COPYING")
# 401-C: a branch control must be a LADDER, and it must be case-folded.
BRANCH_CONTROL_LADDER = ("README.md", "readme.md", "README", "README.txt",
                         "README.rst", "version.php")

_TITLE_TOKENS = (
    ("AFFERO", "AGPL"),
    ("LESSER", "LGPL"),
    ("GENERAL PUBLIC LICENSE", "GPL"),
    ("MIT LICENSE", "MIT"),
    ("APACHE LICENSE", "Apache"),
    ("CREATIVE COMMONS", "CC"),
    ("MOZILLA PUBLIC", "MPL"),
    ("BSD", "BSD"),
)


def title_line(payload):
    """The first line that NAMES a licence.  This, and not the payload, is what
    the family is read from (401-B)."""
    for line in payload.splitlines():
        up = line.upper()
        if any(tok in up for tok, _ in _TITLE_TOKENS):
            return line.strip()
    return ""


def classify(payload):
    """Licence family from the TITLE LINE.  Returns 'UNKNOWN' for a payload
    that names no licence -- never a guess."""
    up = title_line(payload).upper()
    if not up:
        return "UNKNOWN"
    for tok, fam in _TITLE_TOKENS:
        if tok in up:
            base = fam
            break
    else:
        return "UNKNOWN"
    whole = payload.upper()
    if base in ("GPL", "AGPL", "LGPL"):
        if "VERSION 3" in whole:
            base += "-3.0"
        elif "VERSION 2.1" in whole:
            base += "-2.1"
        elif "VERSION 2" in whole:
            base += "-2.0"
        if "ANY LATER VERSION" in whole:
            base += "-or-later"
    elif base == "Apache" and "VERSION 2.0" in whole:
        base += "-2.0"
    elif base == "CC" and "NONCOMMERCIAL" in whole:
        base += "-NC"
    return base


def php_header_grant(payload):
    """A GNU GPL notice in a PHP file header -- the Moodle plugin convention."""
    whole = payload.upper()
    if "GNU GENERAL PUBLIC LICENSE" not in whole:
        return None
    ver = "?"
    for cand in ("EITHER VERSION 3", "EITHER VERSION 2"):
        if cand in whole:
            ver = cand.rsplit(" ", 1)[1]
            break
    grant = f"GPL-{ver}.0"
    if "ANY LATER VERSION" in whole:
        grant += "-or-later"
    return grant


def verdict(channel_L, channel_P, branch_control_ok):
    """The six-valued verdict.  LADDER_BLIND and CHANNEL_CONFLICT are kept
    apart because they license different actions: the first means re-probe,
    the second means adjudicate."""
    if not branch_control_ok:
        return "ADDRESS_UNRESOLVED"
    if channel_L is None and channel_P is None:
        return "NO_GRANT_EITHER_CHANNEL"
    if channel_L is None:
        return "LADDER_BLIND"
    if channel_P is None:
        return "LADDER_ONLY"
    famL = channel_L.split("-")[0]
    famP = channel_P.split("-")[0]
    return "BOTH_AGREE" if famL == famP else "CHANNEL_CONFLICT"
