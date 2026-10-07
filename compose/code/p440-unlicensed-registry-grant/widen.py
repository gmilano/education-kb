#!/usr/bin/env python3
"""p440 stage 0 -- re-probe the 87 `UNLICENSED` slugs with a WIDER filename list.

Action A was pre-registered as "resolve the 87 UNLICENSED rows against the registry",
which takes the 87 as given.  It is not given.  `veraPDF/veraPDF-library` is in the 87,
and its released POM carries this header:

    The GNU General public license GPLv3+.
    You should have received a copy of the GNU General Public License along with
    veraPDF Validation Library as the LICENSE.GPL file in the root of the source tree.
    The Mozilla Public License MPLv2+.
    ... as the LICENSE.MPL file in the root of the source tree.

Both files are at HEAD and return 200.  Neither `LICENSE.GPL` nor `LICENSE.MPL` is in
p436's 14-name list, so a dual-licensed GPL-3.0/MPL-2.0 project was published as
shipping no licence at all -- and MPL-2.0 is the arm that decides whether this KB can
recommend the tool, so the error is not cosmetic.

This is the THIRD time this KB has found the same class of defect:

    pass 52  `@learninglocker/xapi-agents` ships `package/license`, lowercase and
             extensionless; the pass-51 tarball anchor was case-sensitive.
    pass 52  trend 252: "a list of filenames is a cultural assumption" -- `COPYING.txt`
             in the GNU world.
    this     `LICENSE.<FAMILY>`, the convention a DUAL-licensed project must use,
             because two grants cannot both live in a file called `LICENSE`.

So the names added here are not guesses.  Each is a convention with a named reason, and
the family suffix is the one p436's list structurally could not contain: a project with
one licence has no motive to suffix the file, so the missing names are concentrated
exactly in the multi-licensed population.

DELIBERATELY still excluded, carrying pass 52's rule forward: `LICENSES` and
`licenses.json` are licence INVENTORIES, not licence texts, and `node_modules` paths
are somebody else's grant.

Usage: python3 -I widen.py <slugs.txt> <14-name-result.tsv>
TSV: slug, verdict, hit_path, bytes, family
"""
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, "../p436-fork-hypothesis")
from sweep_payload import LICENSE_NAMES as NARROW, family_of  # noqa: E402

RAW = "https://raw.githubusercontent.com/{slug}/HEAD/{path}"

# The family-suffixed forms, which is what a dual-licensed project is forced into.
FAMILY_SUFFIXED = [
    "LICENSE.GPL", "LICENSE.MPL", "LICENSE.LGPL", "LICENSE.AGPL", "LICENSE.APACHE",
    "LICENSE.BSD", "LICENSE.MIT", "LICENSE.ISC", "LICENSE.EPL", "LICENSE.CC0",
    "LICENSE.GPL3", "LICENSE.GPLv3", "LICENSE.GPL-3.0", "LICENSE.MPL2",
    "LICENSE-GPL", "LICENSE-MPL", "LICENSE-BSD", "LICENSE-ISC",
    "MIT-LICENSE", "MIT-LICENSE.txt", "MIT-LICENCE",
]
# Other root spellings with a reason: GNU's LESSER split, the Unlicense's own
# filename, markup extensions, and the two words a project uses when it writes a
# licence page rather than a licence file.
OTHER_ROOT = [
    "COPYING.LESSER", "COPYING.md", "COPYING.LIB", "COPYRIGHT", "COPYRIGHT.txt",
    "UNLICENSE", "UNLICENSE.txt", "LICENSE.html", "LICENSE.markdown", "LICENCE.txt",
    "LICENSE.first_party", "LICENSE.code", "LICENSE.docs", "license.rst",
]
# One directory down, the two places a project moves the file when the root is
# reserved for a monorepo's own README.
SUBPATHS = ["docs/LICENSE", "docs/LICENSE.md", "LICENSE/LICENSE", "legal/LICENSE",
            ".github/LICENSE", "doc/LICENSE"]

WIDE = FAMILY_SUFFIXED + OTHER_ROOT + SUBPATHS

# The negative control runs in the sweep itself, not only in the test: a name no
# repository uses must 404 everywhere, or the probe is answering 200 to everything.
PLANTED = "LICENSE.globant-kb-p440-planted"


def get(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": "globant-kb-p440"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, b""
    except Exception:
        return 0, b""


def one(slug):
    hits = []
    for fn in WIDE:
        code, body = get(RAW.format(slug=slug, path=fn))
        if code == 200:
            hits.append((fn, len(body), family_of(body.decode("utf-8", "replace"))))
    code, _ = get(RAW.format(slug=slug, path=PLANTED))
    if code == 200:
        return (slug, "PROBE-UNSOUND", PLANTED, "0", "-")
    if not hits:
        return (slug, "STILL-UNLICENSED", "-", "0", "-")
    verdict = "FALSE-UNLICENSED-DUAL" if len(hits) > 1 else "FALSE-UNLICENSED"
    return (slug, verdict,
            ";".join(h[0] for h in hits),
            ";".join(str(h[1]) for h in hits),
            ";".join(h[2] for h in hits))


def main():
    slugs = [l.strip() for l in open(sys.argv[1]) if l.strip()]
    if not slugs:
        sys.stderr.write("p440/widen: empty denominator -- a path fault (P355)\n")
        sys.exit(2)
    overlap = set(WIDE) & set(NARROW)
    if overlap:
        sys.stderr.write("p440/widen: %r already probed by p436; the widening would "
                         "be double-counted\n" % sorted(overlap))
        sys.exit(3)
    print("slug\tverdict\thit_path\tbytes\tfamily")
    with ThreadPoolExecutor(max_workers=8) as ex:
        for row in ex.map(one, slugs):
            print("\t".join(row))


if __name__ == "__main__":
    main()
