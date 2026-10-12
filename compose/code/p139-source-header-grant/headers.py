#!/usr/bin/env python3
"""p139-source-header-grant — the matcher behind ACTION CH.

Reads every shipped TEXT file in an extracted npm payload and decides whether it
carries a licence GRANT in its header, as distinct from a mere mention.

The distinction is the whole probe. "license" appearing in a variable name, an npm
manifest field, a URL, or a dependency's name is NOT a grant. A grant is one of:

  SPDX        a `SPDX-License-Identifier:` tag
  COPYRIGHT   a copyright line naming a year or a holder
  VENDORED    any of the above, but inside minified build output, so it is a
              bundled dependency's notice and NOT this package's grant
  GRANT_MIT   the operative MIT sentence ("Permission is hereby granted")
  GRANT_APACHE the operative Apache sentence ("Licensed under the Apache License")
  GRANT_GPL   the operative (A)GPL sentence ("This program is free software")

Only the first HEADER_BYTES of each file are read: a grant that is not in the header
is not a header grant, and a bundled dependency's licence text deep inside a
concatenated build artefact would otherwise be counted as the package's own.
"""
import os
import re
import sys

HEADER_BYTES = 4096

# A bundler hoists its dependencies' licence notices to the TOP of the artefact it
# emits, so a vendored notice lands inside the header window and reads exactly like
# the package's own. Position is therefore not sufficient to attribute a grant.
# A file whose longest line exceeds this is machine-minified output, and a notice
# found in one belongs to whatever was bundled into it -- not to this package.
MINIFIED_LINE = 2000

# Real licence headers are line-wrapped inside comment blocks, so the operative
# sentence arrives as "free of\n * charge". Matching the raw bytes therefore MISSES
# the very grants this probe exists to find -- a defect the test suite caught before
# this probe published a number. Comment leaders and runs of whitespace are collapsed
# to single spaces before any pattern is applied.
NORMALISE = re.compile(r"(?m)^[\s]*(?:[/*#;-]+|//+|<!--)\s*")
WHITESPACE = re.compile(r"\s+")


def normalise(text):
    return WHITESPACE.sub(" ", NORMALISE.sub(" ", text))


# Ordered weakest -> strongest obligation, which is what `strongest` reports.
CLASSES = [
    ("COPYRIGHT",    re.compile(r"copyright\s*(\(c\)|©|\d{4})", re.I)),
    ("SPDX",         re.compile(r"SPDX-License-Identifier\s*:\s*[A-Za-z0-9.+-]+")),
    ("GRANT_MIT",    re.compile(r"permission is hereby granted,? free of charge", re.I)),
    ("GRANT_APACHE", re.compile(r"licensed under the apache license", re.I)),
    ("GRANT_GPL",    re.compile(r"this program is free software|gnu (affero )?general public license", re.I)),
]

# Text extensions only. A grant cannot be read out of a sourcemap or a PNG, and a
# .map file is machine output that embeds the source it was built from.
TEXT_EXT = {
    ".js", ".mjs", ".cjs", ".ts", ".mts", ".cts", ".jsx", ".tsx",
    ".py", ".java", ".php", ".rb", ".go", ".rs", ".sh", ".css", ".html",
    ".md", ".txt", ".json", ".yml", ".yaml",
}
SKIP_NAMES = {"package.json", "package-lock.json"}


def is_minified(path):
    """True if this file is machine-minified output rather than authored source."""
    try:
        with open(path, "rb") as fh:
            for line in fh:
                if len(line) > MINIFIED_LINE:
                    return True
    except OSError:
        return False
    return False


def classify(path):
    """Return the set of grant classes in this file's header.

    A grant is only attributed to the package when it sits in authored source. The
    same bytes inside a minified bundle are reported as VENDORED, because they are
    some dependency's notice that a build step carried in.
    """
    try:
        with open(path, "rb") as fh:
            head = fh.read(HEADER_BYTES)
    except OSError:
        return set()
    if b"\x00" in head:          # binary despite the extension
        return set()
    text = normalise(head.decode("utf-8", "replace"))
    found = {name for name, rx in CLASSES if rx.search(text)}
    if found and is_minified(path):
        return {"VENDORED"}
    return found


def main(root):
    text_files = 0
    with_grant = 0
    seen = set()
    vendored = 0
    for dirpath, _dirs, files in os.walk(root):
        for fn in files:
            if fn in SKIP_NAMES:
                continue
            if os.path.splitext(fn)[1].lower() not in TEXT_EXT:
                continue
            text_files += 1
            got = classify(os.path.join(dirpath, fn))
            if got == {"VENDORED"}:
                vendored += 1
                seen |= got
            elif got:
                with_grant += 1
                seen |= got
    order = ["VENDORED"] + [c for c, _ in CLASSES]
    classes = ",".join(sorted(seen, key=order.index)) or "NONE"
    own = seen - {"VENDORED"}
    strongest = max(own, key=order.index) if own else "NONE"
    print(f"{text_files}\t{with_grant}\t{classes}\t{strongest}\t{vendored}")


if __name__ == "__main__":
    main(sys.argv[1])
