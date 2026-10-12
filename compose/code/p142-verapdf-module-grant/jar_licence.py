"""p142-verapdf-module-grant — `ACTION DF`: which licence do the modules a CONSUMER pulls declare,
and does either ship licence text?

p141 pre-registered:

> Resolve which licence `org.verapdf:core` and `org.verapdf:xmp-core` -- the modules a consumer
> actually pulls -- declare, and whether either ships licence text. 🔴 *Refuted if either declares
> its own licence differing from the parent's dual GPL-3.0 / MPL-2.0 offer, which would mean the
> election a studio has to make is per-module rather than per-project and `P20` step 2 is wrong
> as written.*

🔴 **REFUTED.** `verapdf-xmp-core` declares **BSD-3-Clause in its own POM**. The election is
per-module.

🔴 **And `org.verapdf:xmp-core` -- the coordinate p141 named -- does not exist.** It is `404` on
Central, checked against `org.verapdf:core` which is `200` on the same channel in the same run.
p141 read the two module names out of `verapdf-library-1.30.3.pom`:

    <modules><module>xmp-core</module><module>core</module></modules>

🔵 **A `<module>` entry is a path in the source tree, not an artifactId.** The directory
`xmp-core/` builds the artefact `verapdf-xmp-core`; the directory `core/` happens to build `core`,
which is why one of the two names resolved and made the other look plausible. Any probe that
derives coordinates from a `<modules>` block inherits this error, so it is pinned as a test.

## The licence-text half, and the defect this probe found in its own first draft

🔴 **The first draft of this probe reported licence text in every jar it opened, and every hit was
false.** It matched entry names case-insensitively against a substring list that included `MPL` --
and `MPL` is a substring of `IMPL`, so `org/verapdf/xmp/impl/XMPNode.class` was read as evidence
of a Mozilla Public License. 🔵 **`validation-model` returned 300+ "licence files", all of them
compiled classes in an `impl` package.**

The matcher now tests the **basename** of each entry against anchored patterns, so a token inside
a package path cannot match, and `test_jar_licence.py` pins `org/verapdf/xmp/impl/XMPNode.class`
as a fixture that must NOT match.
"""

import re
import sys
import urllib.error
import urllib.request
import time
import zipfile
import io

CENTRAL = "https://repo1.maven.org/maven2"

# Anchored on the BASENAME. `MPL-2.0.txt` matches; `.../xmp/impl/X.class` does not.
LICENCE_NAME = re.compile(
    r"^(?:(?:un)?licen[cs]e|copying|notice|gpl|lgpl|agpl|mpl|apache|bsd|mit|eupl|epl)"
    r"[._-]?.*$",
    re.IGNORECASE,
)
CODE_EXT = (".class", ".java", ".kt", ".scala", ".so", ".dll", ".dylib")


def licence_entries(names):
    out = []
    for n in names:
        if n.endswith("/"):
            continue
        base = n.rsplit("/", 1)[-1]
        if base.lower().endswith(CODE_EXT):
            continue
        if LICENCE_NAME.match(base):
            out.append(n)
    return out


def fetch(url, attempts=5):
    last = None
    for i in range(attempts):
        try:
            with urllib.request.urlopen(url, timeout=120) as r:
                return r.read(), None
        except urllib.error.HTTPError as e:
            last = "HTTP %d" % e.code
            if e.code == 404:
                return None, last
        except Exception as e:  # noqa: BLE001
            last = type(e).__name__
        time.sleep(4 * (i + 1))
    return None, last


COLS = ["coordinate", "jar_http", "entries", "licence_text_entries", "verdict"]


def probe(group, artifact, version):
    g = group.replace(".", "/")
    url = "%s/%s/%s/%s/%s-%s.jar" % (CENTRAL, g, artifact, version, artifact, version)
    blob, err = fetch(url)
    coord = "%s:%s:%s" % (group, artifact, version)
    if blob is None:
        return dict(zip(COLS, [coord, err or "unfetchable", "-", "-", "NO_JAR"]))
    try:
        z = zipfile.ZipFile(io.BytesIO(blob))
    except zipfile.BadZipFile:
        return dict(zip(COLS, [coord, "200", "-", "-", "NOT_A_ZIP"]))
    names = z.namelist()
    hits = licence_entries(names)
    return dict(zip(COLS, [
        coord, "200", str(len(names)),
        ",".join(hits) or "NONE",
        "SHIPS_TEXT" if hits else "SILENT",
    ]))


def main(argv):
    targets = [tuple(a.split(":")) for a in argv]
    print("\t".join(COLS))
    for g, a, v in targets:
        r = probe(g, a, v)
        print("\t".join(r[c] for c in COLS))
        print("# %-44s %s" % (r["coordinate"], r["verdict"]), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
