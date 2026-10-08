#!/usr/bin/env python3
"""p620 -- the header window of `P419` is measured against PLAIN TEXT, and degrades
silently on `.md` / `.html` licence payloads.

`p419`'s rule is right and this folder does not touch it: the family is read from the
HEADER (title + `Version N`), never from the body, because a pristine licence text
NAMES its relatives. The window is `n=2` non-empty lines, and `p419`'s own suite
refuted a wider one -- at `n=6` the GPL-3.0 section 13 heading re-enters the window and
the instrument commits the very defect it was built to fix.

🔴 What `n=2` never had to survive is a payload that is not plain text. A `LICENSE.md`
opens with `<center>` or `# `; a `license.html` opens with markup and a *different*
licence's name. Either way the two lines the window admits are NOT `TITLE` +
`Version N`, so the version line falls OUTSIDE the window and a plainly-versioned
payload comes back `GPL-?` -- "names GPL without a version, not inferred (`P286`)".

The verdict is not wrong, it is ABSENT, which is why no suite went red: `GPL-?` is a
legal answer. It is also the answer that stops a commercial verdict, because GPL-2.0
and GPL-3.0 differ on patent grant and on compatibility.

This probe measures the defect and the repair on the same payloads, and reports both,
so the claim is a measurement rather than an assertion. The repair is a PRE-STAGE --
strip markup, then hand the text to `p419`'s unmodified `familia()` -- so `P419`'s rule
keeps naming the family and this folder only changes what counts as a "line".
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "p419-copyleft-identity"))
from identidad_copyleft import familia  # noqa: E402  -- P126: import, do not rewrite


# Markup that can occupy a line WITHOUT carrying licence text. Kept deliberately
# narrow: an HTML tag on its own line, and Markdown heading/emphasis/rule markers.
# It must NOT strip words, because the words are what `familia()` reads.
_TAG_ONLY = re.compile(r"^\s*</?[a-zA-Z][^>]*>\s*$")
_MD_LEAD = re.compile(r"^\s*(?:#{1,6}\s*|[*_]{1,3}\s*|>\s*)")
_MD_RULE = re.compile(r"^\s*(?:[-=*_]\s*){3,}$")
_INLINE_TAG = re.compile(r"</?[a-zA-Z][^>]*>")


def unwrap(texto):
    """Return `texto` with markup-only lines dropped and lead markers removed.

    🔴 The order matters and is measured, not chosen: inline tags are stripped BEFORE
    the empty test, because `<pre>Copyright (C) 1989` carries text *and* a tag, and
    dropping the whole line would lose the copyright holder that `P184` reads.
    """
    out = []
    for raw in texto.splitlines():
        if _TAG_ONLY.match(raw) or _MD_RULE.match(raw):
            continue
        line = _INLINE_TAG.sub("", raw)
        line = _MD_LEAD.sub("", line)
        if line.strip():
            out.append(line)
    return "\n".join(out)


def read(texto):
    """(family_raw, family_unwrapped) -- the defect and the repair, side by side."""
    return familia(texto)[0], familia(unwrap(texto))[0]


def classify(texto):
    """The verdict this folder publishes for one payload.

    AGREE              both reads give the same family -- no markup in the window
    REPAIRED           the raw read lost the version, the unwrapped read recovers it
    WINDOW-STILL-SHORT 🔴 the repair moved the read FORWARD but the version is still
                       outside the window. This is the DECLARED BLIND SPOT of this
                       folder, not a case to tune away: it happens when the payload
                       NAMES A SECOND LICENCE before its own version line, so the two
                       lines `P419` admits are two titles. Widening the window to n=3
                       would admit body text and reintroduce `P419`'s original defect,
                       which that pass's own suite already refuted. Published as a
                       limit, measured, rather than cured by a wider window.
    DIVERGENT          the two reads disagree on the FAMILY, not just the version
    """
    raw, un = read(texto)
    if raw == un:
        return "AGREE", raw, un
    raw_fam, un_fam = raw.split("-")[0], un.split("-")[0]
    if raw.endswith("-?") and not un.endswith("-?") and un_fam == raw_fam:
        return "REPAIRED", raw, un
    if un.endswith("-?"):
        return "WINDOW-STILL-SHORT", raw, un
    return "DIVERGENT", raw, un


def main(argv):
    if len(argv) < 2:
        print("usage: probe_window.py <payload-file> [...]", file=sys.stderr)
        return 2
    print("file\tverdict\traw\tunwrapped")
    for path in argv[1:]:
        with open(path, encoding="utf-8", errors="replace") as fh:
            texto = fh.read()
        verdict, raw, un = classify(texto)
        print("%s\t%s\t%s\t%s" % (os.path.basename(path), verdict, raw, un))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
