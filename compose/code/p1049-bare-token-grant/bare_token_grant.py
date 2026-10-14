#!/usr/bin/env python3
"""P1049 — the BARE-TOKEN grant pass.

p184 found a repository whose entire licence is the bare word `MIT` under a
`## License` heading in README.md.  Two instruments on this shelf reported
"no grant" and both were wrong:

  * the per-path file probe  (P170) looks for LICENSE/COPYING/... files
  * the grant-TEXT matcher   (P179) looks for cession markers
    ("Permission is hereby granted", "Grant of Copyright License", ...)

A bare identifier under a heading has neither a file nor grant text.  This
instrument reads README.md over the raw channel and classifies what sits
under every licence-ish heading, plus licence badges.

Channel: raw.githubusercontent.com (the ONLY github read channel that answers
200 in this environment; api.github.com and codeload.github.com both 403).

Verdicts
  BARE_TOKEN  a licence identifier under a licence heading, with no grant text
  BADGE_ONLY  a shields.io/licence badge carries the only identifier
  GRANT_TEXT  the README embeds real licence text (a grant, in the README)
  PROSE_TERMS a licence heading with terms in prose but no SPDX-ish token
  HEADING_EMPTY   a licence heading with nothing identifiable under it
  NO_HEADING  no licence heading and no badge
  NO_README   the raw channel has no README at any probed name
"""
import re, sys, json, urllib.request, urllib.error

RAW = "https://raw.githubusercontent.com/{slug}/{ref}/{path}"
README_PATHS = ["README.md", "README.MD", "readme.md", "README.rst", "README.txt", "README_EN.md", "README-en.md"]
REFS = ["HEAD", "main", "master"]

# Licence identifiers, longest-first so Apache-2.0 wins over the bare word.
TOKENS = [
    r"AGPL[- ]?3\.0", r"AGPLv3", r"Affero General Public License",
    r"Apache[- ]?2\.0", r"Apache License 2\.0", r"Apache-2",
    r"LGPL[- ]?[23](\.[01])?", r"GPL[- ]?[23](\.0)?", r"GPLv[23]",
    r"General Public License",
    r"BSD[- ]?[23][- ]Clause", r"BSD[- ]?licen[cs]e", r"BSD\b",
    r"MPL[- ]?2\.0", r"Mozilla Public License",
    r"CC[- ]?BY(?:[- ]?(?:NC|ND|SA)){0,3}(?:[- ]?[0-9]\.[0-9])?",
    r"\bCC0\b", r"\bUnlicense\b", r"\bWTFPL\b", r"\bISC\b", r"\bEPL[- ]?2\.0\b",
    # p185: a LEADING boundary is mandatory. Without it "MIT\b" matches "sub|mit " and
    # "CC0" matches the hex id "…bcc0-66af…". Both were measured, both were false positives.
    r"\bMIT\b",
]
TOKEN_RE = re.compile("(" + "|".join(TOKENS) + ")", re.I)

# Real grant text — if this is present the README IS a licence, not a token.
GRANT_TEXT = re.compile(
    r"Permission is hereby granted|Grant of Copyright License|Grant of Patent License|"
    r"THE SOFTWARE IS PROVIDED|Redistribution and use in source|"
    r"everyone is permitted to copy and distribute|TERMS AND CONDITIONS FOR USE",
    re.I)

HEADING = re.compile(r"^\s{0,3}(#{1,6})\s*(.+?)\s*#*\s*$")
LICENCE_HEADING = re.compile(r"licen[cs]e|licencia|licensing|版权|许可|著作權|ライセンス", re.I)
BADGE = re.compile(r"!\[[^\]]*\]\((https?://[^)]*(?:shields\.io|badgen\.net|img\.shields)[^)]*licen[cs]e[^)]*)\)", re.I)
BADGE_ALT = re.compile(r"\[!\[[^\]]*licen[cs]e[^\]]*\]\(([^)]+)\)", re.I)
# an explicit non-grant
RESERVED = re.compile(r"all rights reserved|proprietary", re.I)


def fetch(slug):
    """Return (ref, path, text) for the first README that answers 200."""
    for ref in REFS:
        for path in README_PATHS:
            url = RAW.format(slug=slug, ref=ref, path=path)
            try:
                with urllib.request.urlopen(url, timeout=30) as r:
                    if r.status == 200:
                        return ref, path, r.read().decode("utf-8", "replace")
            except urllib.error.HTTPError:
                continue
            except Exception:
                continue
        # HEAD resolves for every live repo; only retry other refs if HEAD had no README
    return None, None, None


def sections(text):
    """Yield (heading, body) for every licence-ish heading."""
    lines = text.split("\n")
    idx = [(i, HEADING.match(l)) for i, l in enumerate(lines)]
    heads = [(i, m.group(1), m.group(2)) for i, m in idx if m]
    for n, (i, hashes, title) in enumerate(heads):
        if not LICENCE_HEADING.search(title):
            continue
        end = heads[n + 1][0] if n + 1 < len(heads) else len(lines)
        yield title, "\n".join(lines[i + 1:end]).strip()


def classify_text(slug, text, ref="HEAD", path="README.md"):
    """The verdict, given README text. Separated from the fetch so it is testable offline."""
    secs = list(sections(text))
    for title, body in secs:
        if GRANT_TEXT.search(body):
            tok = TOKEN_RE.search(body)
            return dict(slug=slug, ref=ref, readme=path, verdict="GRANT_TEXT",
                        token=(tok.group(1) if tok else "-"), heading=title,
                        excerpt=flat(body)[:160])
        tok = TOKEN_RE.search(body)
        if tok:
            return dict(slug=slug, ref=ref, readme=path, verdict="BARE_TOKEN",
                        token=tok.group(1), heading=title, excerpt=flat(body)[:160])
        if RESERVED.search(body):
            return dict(slug=slug, ref=ref, readme=path, verdict="PROSE_TERMS",
                        token="RESERVED", heading=title, excerpt=flat(body)[:160])
        if body:
            return dict(slug=slug, ref=ref, readme=path, verdict="PROSE_TERMS",
                        token="-", heading=title, excerpt=flat(body)[:160])
        return dict(slug=slug, ref=ref, readme=path, verdict="HEADING_EMPTY",
                    token="-", heading=title, excerpt="-")
    b = BADGE.search(text) or BADGE_ALT.search(text)
    if b:
        tok = TOKEN_RE.search(b.group(1))
        return dict(slug=slug, ref=ref, readme=path, verdict="BADGE_ONLY",
                    token=(tok.group(1) if tok else "-"), heading="(badge)",
                    excerpt=flat(b.group(1))[:160])
    return dict(slug=slug, ref=ref, readme=path, verdict="NO_HEADING", token="-",
                heading="-", excerpt="-")


def classify(slug):
    ref, path, text = fetch(slug)
    if text is None:
        return dict(slug=slug, ref="-", readme="-", verdict="NO_README", token="-",
                    heading="-", excerpt="-")
    return classify_text(slug, text, ref, path)


def flat(s):
    return re.sub(r"\s+", " ", s).strip()


if __name__ == "__main__":
    slugs = [l.strip() for l in open(sys.argv[1]) if l.strip() and not l.startswith("#")]
    cols = ["slug", "ref", "readme", "verdict", "token", "heading", "excerpt"]
    print("\t".join(cols))
    for s in slugs:
        r = classify(s)
        print("\t".join(str(r[c]).replace("\t", " ") for c in cols), flush=True)
