#!/usr/bin/env python3
"""ACTION QI — sweep every Apereo/Sakai-family row for ECL-2.0 published as Apache-2.0.

T215-8: `ECL-2.0` — the Educational Community License, an Apache-2.0 derivative and the Apereo
house licence — appears NOWHERE on these shelves before p215, because a title-window matcher
looking for "apache license" does not match "Educational Community License". The classifier
p215 shipped (`p215-lstree-grant-recovery/read_grants.py`) has no ECL token at all: confirmed by
reading it, and reproduced below as `classify_p215`.

Limb 1: 2+ rows currently reading `Apache-2.0` (or `ABSENT`) are in fact `ECL-2.0` -> an
education-sector licence family has been invisible to this KB's classifier for 214 passes and
needs a permanent token. Limb 2: 0-1 -> `SakaiXAPI-Provider` is an isolated instance.

Method: for each Apereo-family slug lifted from the shelves, fetch the licence blob through the
one channel that answers here (`raw.githubusercontent.com`, see ACTION PD), then classify it
TWICE — once with p215's classifier verbatim, once with the same classifier plus an ECL token.
The DELTA between the two is the measurement: it is the population the instrument could not see.
"""

import subprocess
import sys

RAW = "https://raw.githubusercontent.com/{slug}/HEAD/{path}"
PATHS = [
    "LICENSE", "LICENSE.txt", "LICENSE.md", "license.txt", "License.txt", "License",
    "COPYING", "copying.txt", "NOTICE", "LICENSE-2.0.txt", "licence.txt",
    "pom.xml", "package.json", "composer.json",
]


def fetch(slug, path):
    url = RAW.format(slug=slug, path=path)
    p = subprocess.run(
        ["curl", "-sS", "-m", "45", "-w", "\n%{http_code}", url],
        capture_output=True, text=True,
    )
    out = p.stdout
    if "\n" not in out:
        return None, "000"
    body, code = out.rsplit("\n", 1)
    return body, code.strip()


def title_window(text):
    lines = [l.strip() for l in text.splitlines()]
    lines = [l for l in lines if l and not l.startswith(("#", "<!--"))]
    return " ".join(lines[:6])[:400]


def classify_p215(text):
    """p215's classifier, reproduced verbatim for the delta. NOTE: no ECL token."""
    w = title_window(text).lower()
    if "affero" in w:
        return "AGPL-3.0"
    if "lesser general public" in w:
        return "LGPL-3.0" if "version 3" in w else "LGPL-2.1"
    if "general public license" in w:
        if "version 3" in w:
            return "GPL-3.0"
        if "version 2" in w:
            return "GPL-2.0"
        return "GPL-?"
    if "apache license" in w:
        return "Apache-2.0" if "2.0" in w else "Apache-?"
    if "mit license" in w or "permission is hereby granted, free of charge" in w:
        return "MIT"
    if "bsd" in w or "redistribution and use in source and binary" in w:
        return "BSD"
    if "eclipse public license" in w:
        return "EPL"
    return "UNCLASSIFIED"


def classify_p216(text):
    """p215's classifier with the ECL token T215-8 requires, tested BEFORE the Apache token.

    ECL-2.0's own title line is "Educational Community License, Version 2.0"; its body is
    Apache-2.0's text with clause 4 amended, so a body matcher and a late-ordered title matcher
    both return Apache-2.0. The token must therefore come FIRST.
    """
    w = title_window(text).lower()
    if "educational community license" in w:
        return "ECL-2.0" if "2.0" in w else "ECL-1.0"
    return classify_p215(text)


def main(slugs):
    print("slug\tpath\thttp\tp215_says\tp216_says\tdelta")
    for slug in slugs:
        hit = False
        for path in PATHS:
            body, code = fetch(slug, path)
            if code != "200" or not body:
                continue
            a, b = classify_p215(body), classify_p216(body)
            # a manifest may name ECL in an SPDX-ish field the title window never sees
            extra = ""
            low = body.lower()
            if "educational community license" in low or '"ecl-2.0"' in low or ">ecl-2.0<" in low:
                extra = "ECL-STRING-PRESENT"
            print(f"{slug}\t{path}\t{code}\t{a}\t{b}\t"
                  f"{'DIFFERS' if a != b else 'same'}{(' ' + extra) if extra else ''}",
                  flush=True)
            hit = True
            if path not in ("pom.xml", "package.json", "composer.json"):
                break
        if not hit:
            print(f"{slug}\t-\tnone-of-{len(PATHS)}\t-\t-\tNO-BLOB", flush=True)


if __name__ == "__main__":
    with open(sys.argv[1]) as fh:
        main([l.strip() for l in fh if l.strip() and not l.startswith("#")])
