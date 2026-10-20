#!/usr/bin/env python3
"""
p329-grant-link-resolution -- pass 329.

Measures ONE thing, and it is the thing p328's rule cannot see: whether a licence declaration made
INSIDE a repository resolves to a grant file that the repository actually ships.

Why it exists. The licence ladder on this base, in order:
  p322 -- README declares X, the shipped LICENSE says Y. Two files present, disagreeing.
  p314 -- a complete MIT grant that never says "MIT".
  p324 -- the licence file is not the grant in either direction.
  p328 -- a third-party comparison blog asserts a grant the repo does not ship. Its rule:
          "a licence asserted by anything other than the repository's own grant file is a LEAD."
  p329 -- the repository's OWN README declares MIT and links to its OWN `LICENSE`, and that path
          does not exist in any branch. p328's rule sends the reader to "the repository's own grant
          file", which is precisely where the README points -- at nothing.

So the test p328 wrote is not quite the right test. The test is not "is the claim IN the
repository". The test is "is the claim THE GRANT". That distinction is what this file encodes.

Two controls that matter, both learned the hard way on this base:

P275/P278 -- an absence needs ENUMERATION, not a path ladder: "a count of ZERO over a path that
does not exist in that ref measures the PATH, not the content". So `classify` takes the FULL
enumerated tree (git ls-tree -r --name-only, every branch), never a probe list. Passing an empty
tree is a caller error and raises, because "no paths" means "you did not enumerate", not "no grant".

P126/P151 -- when an input is missing, the verdict is UNKNOWN and NOT a convenient default. A repo
with no README is not an unlicensed repo; it is a repo this instrument cannot speak about.

A note on badges, because it is the trap. `img.shields.io/badge/License-MIT-yellow.svg` is a STATIC
IMAGE URL: a string the author typed. It is not a licence lookup and it renders green forever,
including for a repository with no licence at all. So a badge is recorded as a CLAIM and never as
evidence -- same tier as prose.

Does no network: it receives README text and an already-enumerated tree, exactly like the
instruments of passes 62 and 63.
"""
import os
import re
import sys

# P441: a PATH predicate is NOT rewritten as a name list, and P237: a classifier is not rewritten.
# This instrument's first draft defined its own `licen[cs]e|copying` regex and the p329 ladder
# ratchet caught it immediately -- STANDING:CASE-UNVARIED rose to 8 against a ceiling of 7. That
# was the correct catch: a private ladder is how the eight spellings drift apart. The grant-name
# question is asked ONCE, in `lib/licence_identity.LICENCE_NAMES`, and imported here.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                os.pardir, "lib"))
import licence_identity as _LI  # noqa: E402

# `LICENCE_NAMES` anchors on a BASENAME (`^...$`), so a nested path is tested on its last segment.
# Attribution files are the one thing this instrument must name itself, because the shared
# predicate deliberately does not treat them as grants and neither does p329: an Apache-2.0
# `NOTICE` is an attribution requirement, not a licence grant. Kept as a short, explicit list and
# NOT as a second licence ladder -- it never names a licence spelling.
ATTRIB_RE = re.compile(r'^(notice|copyright|authors)(\.(md|txt|rst|html))?$', re.I)

BADGE_RE = re.compile(
    r'!\[[^\]]*\]\(\s*(?P<url>https?://[^\s)]*(?:shields\.io|badgen\.net|img\.shields\.io)[^\s)]*)\s*\)'
    r'(?:\(\s*(?P<href>[^\s)]+)\s*\))?', re.I)
# `[![License: MIT](badge-url)](link-target)` -- the badge wrapped in a link.
LINKED_BADGE_RE = re.compile(
    r'\[\s*!\[[^\]]*\]\(\s*(?P<url>[^\s)]*(?:shields\.io|badgen\.net)[^\s)]*)\s*\)\s*\]'
    r'\(\s*(?P<href>[^\s)]+)\s*\)', re.I)
# A markdown link whose text mentions a licence: `[MIT License](LICENSE)`.
LICENCE_LINK_RE = re.compile(r'\[(?P<text>[^\]]*licen[cs]e[^\]]*)\]\(\s*(?P<href>[^\s)]+)\s*\)', re.I)
SPDX_RE = re.compile(r'\b(MIT|Apache-2\.0|Apache 2\.0|BSD-[23]-Clause|GPL-3\.0|AGPL-3\.0|LGPL-3\.0|MPL-2\.0)\b', re.I)


def grant_paths(tree):
    """
    The grant-shaped paths in an enumerated tree.

    The name test is `lib/licence_identity.LICENCE_NAMES` (P441/P237 -- asked once, imported, never
    re-spelled here), applied to each path's BASENAME because that regex is basename-anchored.
    """
    return sorted(p for p in tree if _LI.LICENCE_NAMES.match(os.path.basename(p)))


def attribution_paths(tree):
    """Attribution files. NOT grants -- held apart on purpose (p329)."""
    return sorted(p for p in tree if ATTRIB_RE.match(os.path.basename(p)))


def declared_licences(readme_text):
    """Every SPDX-ish identifier the README asserts, deduplicated, upper-cased."""
    if readme_text is None:
        return None
    out, seen = [], set()
    for m in SPDX_RE.finditer(readme_text):
        v = m.group(1).upper().replace('APACHE 2.0', 'APACHE-2.0')
        if v not in seen:
            seen.add(v)
            out.append(v)
    return out


def _is_remote(href):
    return bool(re.match(r'^(https?:)?//|^[a-z][a-z0-9+.-]*:', href, re.I))


def claim_links(readme_text):
    """
    The link targets by which a README points at its own grant.

    Only REPO-RELATIVE targets are returned: a link to choosealicense.com or opensource.org is a
    pointer at the licence TEXT on the web, which is not a grant by this repository and never was.
    """
    if readme_text is None:
        return None
    hrefs = []
    for rx in (LINKED_BADGE_RE, LICENCE_LINK_RE):
        for m in rx.finditer(readme_text):
            h = m.groupdict().get('href')
            if h and not _is_remote(h):
                hrefs.append(h.split('#')[0].lstrip('./'))
    seen, out = set(), []
    for h in hrefs:
        if h and h not in seen:
            seen.add(h)
            out.append(h)
    return out


def has_static_badge(readme_text):
    """A shields.io-style badge is a typed string, not a lookup. Recorded as a claim only."""
    if readme_text is None:
        return None
    return bool(BADGE_RE.search(readme_text) or LINKED_BADGE_RE.search(readme_text))


def classify(readme_text, tree):
    """
    The verdict. `tree` MUST be a full enumeration (P275); an empty tree raises.

    Verdicts:
      GRANT_PRESENT        -- the repo ships a grant file. (Whether its TEXT matches the README's
                              claim is p322's question and a different instrument's job.)
      DEAD_LINK_GRANT      -- the README declares a licence AND points at a repo-relative path,
                              and no grant file exists in the tree. The p329 case.
      CLAIM_WITHOUT_GRANT  -- the README declares a licence, points nowhere resolvable, and no
                              grant file exists. Same commercial consequence, weaker evidence of
                              intent.
      NO_CLAIM_NO_GRANT    -- silent in both channels. All-rights-reserved by default.
      UNKNOWN_NO_README    -- no README supplied. NOT an answer about the licence (P126/P151).
    """
    if not tree:
        raise ValueError(
            "empty tree: P275 -- an absence must be ENUMERATED. Pass the full "
            "`git ls-tree -r --name-only` output, not a probe list.")

    grants = grant_paths(tree)
    attribs = attribution_paths(tree)

    if readme_text is None:
        return {
            'verdict': 'UNKNOWN_NO_README', 'grants': grants, 'attribution_only': attribs,
            'declared': None, 'claim_links': None, 'static_badge': None, 'usable': bool(grants),
        }

    declared = declared_licences(readme_text)
    links = claim_links(readme_text)
    badge = has_static_badge(readme_text)

    if grants:
        verdict = 'GRANT_PRESENT'
    elif declared and links:
        verdict = 'DEAD_LINK_GRANT'
    elif declared:
        verdict = 'CLAIM_WITHOUT_GRANT'
    else:
        verdict = 'NO_CLAIM_NO_GRANT'

    return {
        'verdict': verdict, 'grants': grants, 'attribution_only': attribs,
        'declared': declared, 'claim_links': links, 'static_badge': badge,
        # The only field a sourcing decision should read.
        'usable': bool(grants),
    }
