"""p140-pom-parent-chain — `ACTION CR`: does a Maven artefact declaring NO licence
inherit one from its parent POM?

p139 (`ACTION CM`) measured Maven Central and found two of this shelf's artefacts
declaring nothing at all:

    net.oauth.core:oauth                      20100527
    org.sakaiproject.kernel:sakai-kernel-impl 23.3

p139 recorded both as `NONE_DECLARED` and pre-registered `ACTION CR` with an explicit
falsifier: *"Refuted if either inherits a `<licenses>` block from its parent -- which
would move it out of the 'no signal' class and RAISE the declared-but-absent denominator,
against this pass's own finding."*

🔵 **That falsifier cuts against the pass that wrote it, which is why it is worth running.**
A POM inherits `<licenses>` from its parent under Maven's own model, so "the POM declares
nothing" is not the same claim as "the artefact has no declared licence", and p139 made the
first measurement while reporting the second.

## Method

Walk the `<parent>` chain from the artefact's own POM upward, fetching each POM from Maven
Central by coordinate. At each level record whether a `<licenses>` block is present and
what it names. The first level carrying one is what the artefact effectively declares,
because Maven merges the nearest definition. Stop at the root (no `<parent>`), at a POM
Central does not hold (404), or at a depth limit.

`<licenses>` is read with an XML parser rather than a substring test, so that a block
appearing inside `<profiles>`, `<pluginManagement>` or a comment is not mistaken for the
project's own declaration -- only a `<licenses>` that is a DIRECT child of `<project>`
counts, which is what Maven inherits.

Central answers `429` under load through this environment's proxy; every fetch retries
with backoff and a failure is reported as a failure rather than as an absence.
"""

import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

CENTRAL = "https://repo1.maven.org/maven2"
POM_NS = "{http://maven.apache.org/POM/4.0.0}"
MAX_DEPTH = 12


def pom_url(group, artifact, version):
    return "%s/%s/%s/%s/%s-%s.pom" % (
        CENTRAL, group.replace(".", "/"), artifact, version, artifact, version)


def fetch(url, attempts=4):
    """Text of `url`, or None. 429 is load, not absence -- it is retried, then reported."""
    last = None
    for i in range(attempts):
        try:
            with urllib.request.urlopen(url, timeout=40) as r:
                return r.read().decode("utf-8", "replace"), None
        except urllib.error.HTTPError as e:
            last = "HTTP %d" % e.code
            if e.code == 404:
                return None, last
        except Exception as e:  # noqa: BLE001 - network shape varies
            last = type(e).__name__
        time.sleep(3 * (i + 1))
    return None, last


def _text(node, tag):
    el = node.find(POM_NS + tag)
    if el is None:
        el = node.find(tag)
    return el.text.strip() if el is not None and el.text else None


def _find(node, tag):
    el = node.find(POM_NS + tag)
    return el if el is not None else node.find(tag)


def read_pom(text):
    """(parent_coord_or_None, [licence names], own_group, own_version)."""
    root = ET.fromstring(text.encode("utf-8"))
    parent = _find(root, "parent")
    pcoord = None
    if parent is not None:
        pcoord = (_text(parent, "groupId"), _text(parent, "artifactId"),
                  _text(parent, "version"))

    # Only a `<licenses>` that is a DIRECT child of `<project>` is the project's own
    # declaration and the thing Maven inherits.
    names = []
    lics = _find(root, "licenses")
    if lics is not None:
        for lic in list(lics):
            nm = _text(lic, "name") or "(unnamed)"
            url = _text(lic, "url") or ""
            names.append("%s%s" % (nm, " <%s>" % url if url else ""))

    group = _text(root, "groupId") or (pcoord[0] if pcoord else None)
    version = _text(root, "version") or (pcoord[2] if pcoord else None)
    return pcoord, names, group, version


def chain(group, artifact, version):
    """Levels from the artefact upward, each a dict."""
    levels, seen = [], set()
    coord = (group, artifact, version)
    while coord and len(levels) < MAX_DEPTH:
        if coord in seen:
            levels.append({"coord": "%s:%s:%s" % coord, "error": "cycle"})
            break
        seen.add(coord)
        url = pom_url(*coord)
        text, err = fetch(url)
        if text is None:
            levels.append({"coord": "%s:%s:%s" % coord, "error": err or "unfetchable",
                           "url": url})
            break
        try:
            pcoord, names, _, _ = read_pom(text)
        except ET.ParseError as e:
            levels.append({"coord": "%s:%s:%s" % coord, "error": "parse: %s" % e})
            break
        levels.append({
            "coord": "%s:%s:%s" % coord,
            "licenses": names,
            "declares": bool(names),
            "parent": "%s:%s:%s" % pcoord if pcoord else None,
            "url": url,
        })
        coord = pcoord
    return levels


def verdict(levels):
    if not levels:
        return "NO_POM"
    if levels[0].get("declares"):
        return "DECLARES_OWN"
    for lv in levels[1:]:
        if lv.get("declares"):
            return "INHERITS_FROM_PARENT"
    if any("error" in lv for lv in levels):
        return "NO_SIGNAL_CHAIN_INCOMPLETE"
    return "NO_SIGNAL_ROOT_REACHED"


TARGETS = [
    ("net.oauth.core", "oauth", "20100527"),
    ("org.sakaiproject.kernel", "sakai-kernel-impl", "23.3"),
    # p139 read these two as declaring; carried along as controls, so that a
    # chain-walk bug would show up as a changed verdict on a known row.
    ("org.sakaiproject.kernel", "sakai-kernel-api", "25.2"),
    ("edu.ksu.ome.lti", "lti-launch", "1.4.7"),
]

COLS = ["coordinate", "own_declaration", "inherited_from", "inherited_licenses",
        "chain_depth", "verdict"]


def main(argv):
    targets = TARGETS
    if argv:
        targets = [tuple(a.split(":")) for a in argv]
    print("\t".join(COLS))
    for g, a, v in targets:
        levels = chain(g, a, v)
        own = levels[0].get("licenses") or [] if levels else []
        src, inh = "-", []
        for lv in levels[1:]:
            if lv.get("declares"):
                src, inh = lv["coord"], lv["licenses"]
                break
        print("\t".join([
            "%s:%s:%s" % (g, a, v),
            "; ".join(own) or "NONE",
            src,
            "; ".join(inh) or "NONE",
            str(len(levels)),
            verdict(levels),
        ]))
        for lv in levels:
            note = lv.get("error") or ("declares: " + "; ".join(lv["licenses"])
                                       if lv.get("declares") else "no <licenses>")
            print("    %-60s %s" % (lv["coord"], note), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
