"""Step 3 of `ACTION ST` — name the FAMILY of a licence body read first-hand.

Positional, per p227's surviving channel: the EARLIEST licence title in document
order decides, because every unsafe channel these shelves tried failed on a
substring that sits LATER in the body than the real title.

  p227 `T227-V3`  the AGPL title appears inside a GPL-3.0 body, in §13
                  ("Use with the GNU Affero General Public License")
  and the mirror  the GPL title appears inside an AGPL-3.0 body, in ITS §13
                  ("Remote Network Interaction; Use with the GNU GPL")
  p227            byte size is unsafe: the canonical GPL/AGPL bodies are 15 B apart
  p227 `T227-V2`  `GPL-3.0` is a substring of `AGPL-3.0`

The three GNU titles cannot overlap as strings — `AFFERO` and `LESSER` sit between
`GNU` and `GENERAL` — so the earliest-title rule is sound rather than merely lucky.

BOUND IS DELIBERATELY NOT DECIDED HERE. p225 and p227 both established that
GPL-family `or-later` lives in a CHANNEL (the project's own preamble or a source
header), and that neither the canonical body's §14 nor its "How to Apply These
Terms" appendix is one. A root LICENSE therefore cannot settle a bound, and this
classifier reports `bound=UNSETTLED-FROM-LICENSE` rather than guessing.
"""
import hashlib
import re
import sys

# (family, pattern). Order is irrelevant: the EARLIEST match in the body wins.
TITLES = [
    ("AGPL-3.0", r"GNU\s+AFFERO\s+GENERAL\s+PUBLIC\s+LICENSE"),
    ("LGPL",     r"GNU\s+LESSER\s+GENERAL\s+PUBLIC\s+LICENSE"),
    ("LGPL",     r"GNU\s+LIBRARY\s+GENERAL\s+PUBLIC\s+LICENSE"),
    ("GPL",      r"GNU\s+GENERAL\s+PUBLIC\s+LICENSE"),
    ("Apache-2.0", r"Apache\s+License\s*\n?\s*Version\s+2\.0"),
    ("MPL-2.0",  r"Mozilla\s+Public\s+License\s+Version\s+2\.0"),
    ("EPL-2.0",  r"Eclipse\s+Public\s+License\s+-\s+v\s+2\.0"),
    ("EPL-1.0",  r"Eclipse\s+Public\s+License\s+-\s+v\s+1\.0"),
    ("EUPL-1.2", r"EUROPEAN\s+UNION\s+PUBLIC\s+LICENCE\s+v\.?\s*1\.2"),
    ("ECL-2.0",  r"Educational\s+Community\s+License,?\s+Version\s+2\.0"),
    ("CC-BY-SA-4.0", r"Creative\s+Commons\s+Attribution-ShareAlike\s+4\.0"),
    ("CC-BY-4.0",    r"Creative\s+Commons\s+Attribution\s+4\.0"),
    ("CC-BY-NC-SA-4.0", r"Creative\s+Commons\s+Attribution-NonCommercial-ShareAlike\s+4\.0"),
    ("CC0-1.0",  r"CC0\s+1\.0\s+Universal"),
    ("Unlicense", r"This\s+is\s+free\s+and\s+unencumbered\s+software\s+released\s+into\s+the\s+public\s+domain"),
    ("MIT",      r"\bMIT\s+Licen[cs]e\b"),
    ("MIT",      r"Permission\s+is\s+hereby\s+granted,\s+free\s+of\s+charge"),
    ("ISC",      r"\bISC\s+Licen[cs]e\b"),
    ("ISC",      r"Permission\s+to\s+use,\s+copy,\s+modify,\s+and(/or)?\s+distribute\s+this\s+software"),
    ("BSD",      r"Redistribution\s+and\s+use\s+in\s+source\s+and\s+binary\s+forms"),
    ("Zlib",     r"zlib\s+Licen[cs]e"),
    ("WTFPL",    r"DO\s+WHAT\s+THE\s+FUCK\s+YOU\s+WANT\s+TO\s+PUBLIC\s+LICENSE"),
    ("Artistic-2.0", r"The\s+Artistic\s+License\s+2\.0"),
    ("BSL-1.0",  r"Boost\s+Software\s+License\s+-\s+Version\s+1\.0"),
    ("Ms-PL",    r"Microsoft\s+Public\s+License"),
    ("CDDL-1.0", r"COMMON\s+DEVELOPMENT\s+AND\s+DISTRIBUTION\s+LICENSE"),
    ("PolyForm", r"PolyForm\s+\w+\s+License"),
    ("BUSL-1.1", r"Business\s+Source\s+License\s+1\.1"),
    ("SSPL-1.0", r"Server\s+Side\s+Public\s+License"),
    ("Proprietary", r"All\s+Rights\s+Reserved\s*$"),
]
_COMPILED = [(fam, re.compile(pat, re.I)) for fam, pat in TITLES]

VER3 = re.compile(r"Version\s+3,?\s+29\s+June\s+2007", re.I)
VER2 = re.compile(r"Version\s+2,?\s+June\s+1991", re.I)
VER21 = re.compile(r"Version\s+2\.1,?\s+February\s+1999", re.I)
S13_AGPL_CLAUSE = re.compile(r"13\.\s*Use\s+with\s+the\s+GNU\s+Affero", re.I)
S13_NETWORK = re.compile(r"13\.\s*Remote\s+Network\s+Interaction", re.I)
BSD3 = re.compile(r"Neither\s+the\s+name", re.I)


DUAL_RE = re.compile(
    r"available under either\s+([\w.+-]+)\s+or\s+([\w.+-]+)"
    r"|dual[- ]licen[cs]ed under\s+([\w.+-]+)\s+(?:and|or)\s+([\w.+-]+)"
    r"|licen[cs]ed under either(?: the)?\s+([\w.+-]+)\s+or(?: the)?\s+([\w.+-]+)", re.I)

SPDX_ALIAS = {"mit": "MIT", "gplv2": "GPL-2.0", "gplv3": "GPL-3.0", "apache": "Apache-2.0",
              "lgplv3": "LGPL-3.0", "agplv3": "AGPL-3.0", "bsd": "BSD-3-Clause",
              "gpl-2.0": "GPL-2.0", "gpl-3.0": "GPL-3.0", "apache-2.0": "Apache-2.0"}


def dual_grant(body):
    """A body whose own preamble offers a CHOICE is a DUAL grant, and the earliest
    title is then ONE OPTION rather than the licence.

    This is the positional-title rule's first real limit, found on `Elgg/Elgg`:
    its file opens "The remainder of the project is available under either MIT or
    GPLv2", and the MIT title that follows at offset 346 is the first of two
    options. Reading the title alone reports `MIT` and silently drops the GPLv2
    half; reading only the package manifest reports `GPL-2.0-only` and silently
    drops the MIT half -- which is the half a studio wants.
    """
    m = DUAL_RE.search(body)
    if not m:
        return None
    opts = [g for g in m.groups() if g]
    if len(opts) < 2:
        return None
    named = [SPDX_ALIAS.get(o.lower().strip(". "), o.strip(". ")) for o in opts[:2]]
    return " OR ".join(named)


def classify(body):
    """Return (family, channel, note). Earliest title in document order wins."""
    dual = dual_grant(body)
    if dual:
        return (dual, "dual-grant preamble", "earliest title is ONE OPTION, not the grant")
    best = None
    for fam, rx in _COMPILED:
        m = rx.search(body)
        if m and (best is None or m.start() < best[1]):
            best = (fam, m.start())
    if best is None:
        return (None, None, "no recognised licence title")
    fam, off = best

    # Resolve the GNU families to an exact identifier on their version line.
    if fam in ("GPL", "LGPL", "AGPL-3.0"):
        if fam == "LGPL":
            if VER3.search(body) or re.search(r"Version\s+3,?\s+29\s+June\s+2007", body, re.I):
                fam = "LGPL-3.0"
            elif VER21.search(body):
                fam = "LGPL-2.1"
            else:
                fam = "LGPL-?"
        elif fam == "GPL":
            fam = "GPL-3.0" if VER3.search(body) else ("GPL-2.0" if VER2.search(body) else "GPL-?")
        # §13 cross-check, reported and never silently preferred (p227's rule).
        if fam == "GPL-3.0" and S13_NETWORK.search(body):
            return (None, "conflict", "GPL-3.0 title but §13 is the AGPL network clause")
        if fam == "AGPL-3.0" and S13_AGPL_CLAUSE.search(body) and not S13_NETWORK.search(body):
            return (None, "conflict", "AGPL-3.0 title but §13 is the GPL compatibility clause")
        s13 = "§13 agrees" if (S13_NETWORK.search(body) or S13_AGPL_CLAUSE.search(body)) else "§13 absent"
        return (fam, "title line @%d" % off, s13)

    if fam == "BSD":
        fam = "BSD-3-Clause" if BSD3.search(body) else "BSD-2-Clause"
    return (fam, "title line @%d" % off, "")


def main(argv):
    print("\t".join(["slug", "ref", "path", "bytes", "sha12", "family", "channel", "note"]))
    for line in open(argv[1], encoding="utf-8"):
        parts = line.rstrip("\n").split("\t")
        if len(parts) < 6 or parts[3] != "200":
            slug = parts[0] if parts else "?"
            print("\t".join([slug, "-", "-", "-", "-", "NO-GRANT", "404 on every path", "6 paths x 2 refs"]))
            continue
        slug, ref, path, _b, _s = parts[0], parts[1], parts[2], parts[3], parts[5]
        key = slug.replace("/", "__") + ".body"
        try:
            raw = open(argv[2] + "/" + key, "rb").read()
        except OSError:
            continue
        body = raw.decode("utf-8", "replace")
        fam, chan, note = classify(body)
        print("\t".join([slug, ref, path, str(len(raw)),
                         hashlib.sha256(raw).hexdigest()[:12],
                         fam or "UNRECOGNISED", chan or "-", note]))


if __name__ == "__main__":
    main(sys.argv)
