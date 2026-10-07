#!/usr/bin/env python3
"""p443 -- pass 25's action C: ask every repository how IT spells its own name.

The pre-registered action, verbatim:

    Re-run `p439`'s canonical resolution as a POSITIVE sweep, not a collision gate: ask
    the registry or the self-link for the canonical spelling of all 494 repositories, not
    only the 9 that collided.
    Prediction: expect MORE THAN 9 slugs to be spelled differently from their own
    publisher's spelling -- a collision needs two spellings *in this KB*, and one wrong
    spelling used consistently is invisible to the gate.

The prediction's reasoning is the point. `p439` fires when the KB contains `X/y` AND
`x/y`. A repository this KB has only ever miscapitalised ONE way produces no collision and
no finding, while a compiler still keys it under a spelling its publisher does not use.

## There is no case oracle on this host, and that was measured, not assumed

Every channel GitHub serves here resolves `owner/repo` case-insensitively, so none of them
can be asked "what is the real spelling?". Measured 2026-10-07:

    raw.githubusercontent.com/{learningequality,LearningEquality,LEARNINGEQUALITY}/...
                                                          -> 200, 200, 200
    git ls-remote https://github.com/LEARNINGEQUALITY/KOLIBRI HEAD  -> resolves
    github.com (rendered, would 301 to the canonical path)          -> 403
    codeload.github.com                                            -> 403

So the oracle has to be the publisher's own DECLARATION, which is exactly the order
`p439` wrote and this sweep now runs over the whole shelf:

    1. the package registry's declared repository URL   (`pypi.org`, `registry.npmjs.org`)
    2. the repository's own self-link, in `README.md` / `README.rst` / `package.json`
    3. no oracle -- reported as `NO-ORACLE`, never silently passed

⚠️ **A self-link is weaker evidence than a registry homepage**, and the TSV says which
channel decided every row. A README is hand-written and can miscapitalise its own
repository; a registry URL was resolved by the publisher's own tooling at publish time.

🔴 **And neither is proof of the CANONICAL spelling, which is the action's premise and
is only partly sound.** A publisher's declaration is evidence of the spelling that
publisher typed, in that artefact. GitHub's canonical spelling is knowable only from a
channel that 301-redirects the wrong case, and every such channel is 403 here. So a
disagreement measured by this sweep is REAL -- the channels do preserve case, which is
controlled below -- but it cannot by itself say which side is wrong.

Hence `CHANNELS-DISAGREE` is a verdict of its own. Where the registry and the self-link
contradict each other, a single dissenting channel is not evidence against the KB, and
collapsing that row into `SPELLING-DIFFERS` would publish a correction on the weaker of
two sources.

🟢 **The control that makes any of this readable: each channel CAN carry mixed case.**
Among the rows where the publisher's spelling matches this KB's, 18 came from npm, 23
from PyPI and 95 from a self-link with MIXED-CASE spellings. So a lowercase answer is
the publisher's own, not an artefact of the channel -- without this, every `DIFFERS` row
would be indistinguishable from a channel that normalises.

Verdicts:
    SPELLING-MATCH     every channel that answered agrees with this KB
    SPELLING-DIFFERS   every channel that answered disagrees with this KB
    CHANNELS-DISAGREE  the registry and the self-link contradict each other
    NO-ORACLE          neither channel answers -- this KB's spelling is UNVERIFIABLE
                       from this host, and that is the largest class

TSV: slug, kb_spelling, publisher_spelling, verdict, channel
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "p439-case-collision-gate"))
from case_gate import LIVE, REF, normalise  # noqa: E402

RAW = "https://raw.githubusercontent.com/{slug}/HEAD/{path}"
SELF_DOCS = ["README.md", "README.rst", "readme.md", "README", "package.json",
             "docs/README.md"]
SLUG_RE = re.compile(r"github(?:usercontent)?\.com/(?:[a-z-]+/)??"
                     r"([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")
# A shields.io badge carries the slug too, and in the publisher's own spelling.
BADGE_RE = re.compile(r"(?:img\.shields\.io/github/[a-z/-]+|api\.codeclimate\.com"
                      r"|codecov\.io/gh|travis-ci\.(?:org|com)|app\.codacy\.com)/"
                      r"(?:[a-z-]+/)??([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")


def get(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": "globant-kb-p443"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception:
        return 0, ""


def kb_slugs(root):
    """Every distinct repository the six non-append-only shelf files cite.

    The denominator is `p439`'s, imported rather than re-derived, so a change to the
    reserved-path list or the `.git` rule moves both instruments together.
    """
    out = {}
    for rel in LIVE:
        path = os.path.join(root, rel)
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as f:
            for raw in REF.findall(f.read()):
                slug = normalise(raw)
                if slug:
                    out.setdefault(slug.lower(), slug)
    return out


def matching_spelling(text, slug):
    """The spelling THIS text uses for `slug`, case-insensitively matched, or None."""
    want = slug.lower()
    for pat in (SLUG_RE, BADGE_RE):
        for found in pat.findall(text):
            cand = normalise(found)
            if cand and cand.lower() == want:
                return cand
    return None


def from_registry(slug):
    """(spelling, channel) from the package registry the repo publishes to."""
    code, text = get(RAW.format(slug=slug, path="package.json"))
    if code == 200:
        try:
            j = json.loads(text)
            if isinstance(j, dict) and j.get("name") and j.get("private") is not True:
                code2, body = get("https://registry.npmjs.org/%s" % j["name"])
                if code2 == 200:
                    found = matching_spelling(body, slug)
                    if found:
                        return found, "npm"
        except ValueError:
            pass
    for manifest, pat in (("pyproject.toml", r'^\s*name\s*=\s*["\']([^"\']+)["\']'),
                          ("setup.py", r'name\s*=\s*["\']([^"\']+)["\']'),
                          ("setup.cfg", r'^\s*name\s*=\s*([^\s#]+)')):
        code, text = get(RAW.format(slug=slug, path=manifest))
        if code != 200:
            continue
        m = re.search(pat, text, re.M)
        if not m:
            continue
        code2, body = get("https://pypi.org/pypi/%s/json" % m.group(1).strip('"\''))
        if code2 == 200:
            found = matching_spelling(body, slug)
            if found:
                return found, "pypi"
        break
    return None, None


def from_self_link(slug):
    for doc in SELF_DOCS:
        code, text = get(RAW.format(slug=slug, path=doc))
        if code != 200:
            continue
        found = matching_spelling(text, slug)
        if found:
            return found, "self-link:%s" % doc
    return None, None


def one(item):
    _, kb = item
    reg, reg_ch = from_registry(kb)
    slf, slf_ch = from_self_link(kb)
    pub, channel = (reg, reg_ch) if reg else (slf, slf_ch)
    if pub is None:
        return (kb, kb, "-", "NO-ORACLE", "-")
    if reg and slf and reg != slf:
        # Two channels, two answers.  Neither is canonical, and the row names which one
        # sides with this KB rather than silently preferring the registry.  Three rows
        # on 2026-10-07: `GoogleChrome/lighthouse`, `OHF-Voice/piper1-gpl` and
        # `RohanMuppa/brightspace-mcp-server` -- in all three the self-link agrees with
        # this KB and only the registry's lowercased URL dissents, so reporting them as
        # SPELLING-DIFFERS would have published a correction on the weaker source.
        agrees = "kb" if kb in (reg, slf) else "neither"
        return (kb, kb, "%s|%s" % (reg, slf), "CHANNELS-DISAGREE",
                "%s vs %s; agrees-with=%s" % (reg_ch, slf_ch, agrees))
    verdict = "SPELLING-MATCH" if pub == kb else "SPELLING-DIFFERS"
    return (kb, kb, pub, verdict, channel)


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "..", "..")
    slugs = kb_slugs(root)
    if not slugs:
        sys.stderr.write("p443: empty denominator -- a path fault, not a clean shelf "
                         "(P355)\n")
        sys.exit(2)
    print("slug\tkb_spelling\tpublisher_spelling\tverdict\tchannel")
    with ThreadPoolExecutor(max_workers=10) as ex:
        for row in ex.map(one, sorted(slugs.items())):
            print("\t".join(row))


if __name__ == "__main__":
    main()
