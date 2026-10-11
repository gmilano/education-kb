#!/usr/bin/env python3
"""ACTION AH — read a bulleted per-file exception list as a sequence of bindings.

p124's `ACTION AA` declares a SPLIT grant from bindings found inside one
window: a scope expression, a grant verb and a licence token in that order.
That works on prose ("Bundled plugins … are available only under the GPLv2
license. The remainder …") and fails on a LIST, because a list distributes
one introducing sentence over many items and no window spans it:

    The following included source code items use a license other than AGPL3:

    In the pylib folder:
     * statsbg.py: CC BY 4.0.

    In the qt folder:
     * mpv.py: MIT.
     * MathJax: Apache 2.
     * protobuf.js: BSD 3 clause

The verb is in the introducing sentence, the folder is in a sub-heading, and
the per-item scope and licence are in the bullet. So a binding is assembled
from THREE levels rather than matched in one window.

Every token then passes ACTION AG's scope gate, which is what stops this from
over-reading. The anki file names two licences that are NOT grants over its
tree:

  * "Binary distributions also include copies of Qt translation files (LGPL)"
    -> OUT-OF-TREE. The source tree does not contain them.
  * "without the need to license your work under an AGPL3-compatible license"
    -> a COMPATIBILITY CLASS, not a grant. This is a SIXTH instance of the
    class `ACTION AG` exists for, and it was not on p124's list of four.

Offline. usage: bullet_bindings.py FILE...
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scope_gate                                        # noqa: E402

# An item line: a bullet, a name that looks like a path/component, a colon or
# dash, then the licence. `protobuf.js: BSD 3 clause` has no trailing period,
# and `Anki's translations are a mix of BSD and public domain` has no colon --
# the second is deliberately NOT a binding (see MIXED below).
ITEM = re.compile(
    r"^\s*[*\-•]\s+(?P<scope>[^:\n]{1,60}?)\s*(?::|\s[–-]\s)\s*"
    r"(?P<rest>.+?)\s*\.?\s*$")
# A sub-heading that supplies a folder scope to the items under it.
SUBSCOPE = re.compile(
    r"^\s*In the (?P<dir>[\w./-]+) (?:folder|directory)\s*:\s*$", re.I)
# The introducing sentence: it carries the grant verb the bullets lack.
INTRO = re.compile(
    r"\b(?:use a licen[sc]e other than|are licen[sc]ed under|"
    r"use the following licen[sc]es|licen[sc]ed as follows|"
    r"the following .{0,40}items?\b)", re.I)
# "a mix of BSD and public domain" names no single grant for the item.
MIXED = re.compile(r"\ba mix of\b|\beither\b.{0,20}\bor\b", re.I)

# Canonical spellings, so `BSD 3 clause`, `BSD-3` and `BSD 3-Clause` are ONE
# token rather than three. p124's `ACTION AB` learned the same lesson for
# `GPL-3` vs `GPL-3.0`.
CANON = (
    (re.compile(r"^BSD[ -]?3([ -]?clause)?$", re.I), "BSD-3-Clause"),
    (re.compile(r"^BSD[ -]?2([ -]?clause)?$", re.I), "BSD-2-Clause"),
    (re.compile(r"^BSD$", re.I), "BSD"),
    (re.compile(r"^Apache[ -]?2(\.0)?$", re.I), "Apache-2.0"),
    (re.compile(r"^CC[ -]BY[ -]?4(\.0)?$", re.I), "CC-BY-4.0"),
    (re.compile(r"^CC[ -]BY[ -]SA[ -]?4(\.0)?$", re.I), "CC-BY-SA-4.0"),
    (re.compile(r"^AGPL3?$|^AGPL[ -]?3(\.0)?$", re.I), "AGPL-3.0"),
    (re.compile(r"^MIT$", re.I), "MIT"),
    (re.compile(r"^LGPL$", re.I), "LGPL"),
    (re.compile(r"^ISC$", re.I), "ISC"),
    # The long FSF/CC names and their abbreviations are ONE grant. Leaving
    # them unfolded reported `anki` with both `AGPL-3.0` and `GNU Affero
    # General Public License` -- a seven-token set where six is the truth.
    (re.compile(r"^GNU Affero General Public License$", re.I), "AGPL-3.0"),
    (re.compile(r"^GNU Lesser General Public License$", re.I), "LGPL"),
    (re.compile(r"^GNU General Public License$", re.I), "GPL"),
    (re.compile(r"^Apache License$", re.I), "Apache-2.0"),
    (re.compile(r"^Creative Commons Attribution(?: 4\.0)?$", re.I),
     "CC-BY-4.0"),
    (re.compile(r"^Creative Commons Attribution[- ]ShareAlike(?: 4\.0)?$",
                re.I), "CC-BY-SA-4.0"),
)


def canon(tok):
    t = tok.strip().rstrip(".")
    for pat, out in CANON:
        if pat.match(t):
            return out
    return t


def bindings(text):
    """[(scope, token, label, lineno)] -- every per-item binding, gated.

    `label` is ACTION AG's verdict on the token IN THE WHOLE DOCUMENT, so a
    bullet whose licence is named only to be excluded never becomes a grant.
    """
    lines = text.splitlines()
    # Byte offset of each line, so a token's position in the bullet maps to
    # its position in the document and the gate reads the real surrounding
    # clause rather than the bullet in isolation.
    offs, pos = [], 0
    for ln in lines:
        offs.append(pos)
        pos += len(ln) + 1

    out = []
    seen_intro = False
    sub = None
    for i, line in enumerate(lines):
        if INTRO.search(line):
            seen_intro = True
            continue
        m = SUBSCOPE.match(line)
        if m:
            sub = m.group("dir")
            continue
        if not line.strip():
            continue
        m = ITEM.match(line)
        if not m or not seen_intro:
            continue
        rest = m.group("rest")
        if MIXED.search(rest):
            continue            # no single grant for this item
        scope = m.group("scope").strip()
        if sub:
            scope = "%s/%s" % (sub.rstrip("/"), scope)
        for tm in scope_gate.TOKEN.finditer(rest):
            at = offs[i] + m.start("rest") + tm.start("tok")
            lab = scope_gate.label_span(text, at, at + len(tm.group("tok")))
            out.append((scope, canon(tm.group("tok")), lab, i + 1))
    return out


def token_set(text):
    """The repository's grant SET: list bindings plus prose-level grants."""
    toks = {}
    for scope, tok, lab, _ln in bindings(text):
        if lab == "GRANT":
            toks.setdefault(tok, []).append(scope)
    for tok, at in scope_gate.grants(text):
        toks.setdefault(canon(tok), [])
    return toks


def main(argv):
    for path in [a for a in argv if not a.startswith("-")]:
        with open(path, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        print("## %s" % path)
        for scope, tok, lab, ln in bindings(text):
            print("  %-5s L%-4d %-26s %s"
                  % ("GRANT" if lab == "GRANT" else "drop", ln, scope,
                     tok if lab == "GRANT" else "%s (%s)" % (tok, lab)))
        ts = token_set(text)
        print("  SET: %s" % ", ".join(sorted(ts)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
