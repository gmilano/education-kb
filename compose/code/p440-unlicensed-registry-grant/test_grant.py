#!/usr/bin/env python3
"""Offline controls for p440. Every fixture is a real payload captured 2026-10-07.

Rule 2 of P126: a control set made only of agreeing cases never exercises the
detection. Each positive here is paired with the false positive that would make the
output unreadable, and four controls exist because the first build got them wrong.

Run: python3 test_grant.py
"""
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "dependency-licence-closure"))
import grant  # noqa: E402

FAIL = []


def check(label, got, want):
    if got != want:
        FAIL.append("%s: got %r want %r" % (label, got, want))


def fx(name):
    with open(os.path.join(HERE, "fixtures", name)) as f:
        return f.read()


# --- the verdict split, which is the whole instrument ------------------------
# The FIRST build had no REGISTRY-REFUSAL and no REGISTRY-DEFER, and `UNLICENSED`
# reached `classify_licence`, whose PERMISSIVE rule matched `UNLICENSE` inside it.
check("a plain licence name is a grant",
      grant.verdict_of("MIT"), ("REGISTRY-GRANT", "PERMISSIVE"))
check("npm's UNLICENSED is a REFUSAL, never a grant",
      grant.verdict_of("UNLICENSED"), ("REGISTRY-REFUSAL", "NO-GRANT"))
check("and `Unlicense` -- one letter apart -- IS a grant, the most permissive there is",
      grant.verdict_of("Unlicense"), ("REGISTRY-GRANT", "PERMISSIVE"))
check("SEE LICENSE IN <file> is a pointer, not a grant",
      grant.verdict_of("SEE LICENSE IN LICENSE.txt")[0], "REGISTRY-DEFER")
check("SEE LICENCE IN, the British spelling, is the same deferral",
      grant.verdict_of("SEE LICENCE IN COPYING")[0], "REGISTRY-DEFER")
check("an absent field is silence, not a grant",
      grant.verdict_of(None), ("REGISTRY-SILENT", "UNKNOWN"))
check("an empty string is silence too", grant.verdict_of("")[0], "REGISTRY-SILENT")
check("an empty LIST is silence, not a grant of nothing",
      grant.verdict_of([])[0], "REGISTRY-SILENT")
check("the legacy npm array form is read through",
      grant.verdict_of([{"type": "Apache-2.0"}]), ("REGISTRY-GRANT", "PERMISSIVE"))
check("a copyleft grant is still a grant, and must not be softened",
      grant.verdict_of("GPL-3.0"), ("REGISTRY-GRANT", "STRONG-COPYLEFT"))

# --- ownership: the stage the first build did not have ----------------------
# npm `class` is "A simple yet powerful Ruby-like Class inheritance system", first
# published 2013-08-15, declaring `deadlyicon/class.js`.  A Google Classroom MCP
# server whose package.json says `"name": "class"` resolves to it.  Without the
# ownership stage this instrument published that stranger's MIT as the repository's
# own licence -- and `p436` had already classified the same row a generic-name
# collision, so the two channels agree once the gate exists.
npm_class = json.loads(fx("npm-class-collision.json"))
raw, field = grant.npm_licence(npm_class)
check("the collision package really does declare MIT, which is why it is dangerous",
      raw, "MIT")
latest = npm_class["dist-tags"]["latest"]
ver = npm_class["versions"][latest]
check("and it names a repository that is NOT an education project",
      grant.first_slug([(ver.get("repository") or {}).get("url", "")]),
      "deadlyicon/class.js")

# npm `aoe` -- the NEGATIVE that stops ownership being treated as optional.  The
# Finnish National Agency for Education's AOE platform is cited by this KB; npm's
# `aoe` is version 0.1.1, published 2016-01-05 by `exolution@163.com`, with no
# description and no repository, and it declares GPL-3.0.  Published as a grant,
# this KB would have recorded a STRONG-COPYLEFT obligation on a national education
# platform on the strength of a stranger's 2016 hobby package.
npm_aoe = json.loads(fx("npm-aoe-no-repo.json"))
raw, _ = grant.npm_licence(npm_aoe)
check("the unowned package declares GPL-3.0", raw, "GPL-3.0")
aoe_latest = npm_aoe["versions"][npm_aoe["dist-tags"]["latest"]]
check("and names no repository at all, so ownership cannot be established",
      grant.first_slug([(aoe_latest.get("repository") or {}).get("url", "") or "",
                        aoe_latest.get("homepage") or ""]), None)

# The POSITIVE for ownership, and the prediction's named interesting class:
# `openedx/XBlock` ships no licence file under any of 22 probed names, and PyPI
# declares Apache-2.0 for it via PEP 639 `license_expression`.
xblock = json.loads(fx("pypi-xblock-grant.json"))
check("XBlock's grant lives in license_expression, not the legacy field",
      grant.pypi_licence(xblock), ("Apache-2.0", "license_expression"))
info = xblock["info"]
check("and PyPI names THIS repository, so the grant is attributable",
      grant.first_slug(list((info.get("project_urls") or {}).values())),
      "openedx/XBlock")

# One npm name, two repositories citing it.  `canvas-mcp-server` declares
# `DMontgomery40/mcp-canvas-lms`; `plyght/canvas-mcp` carries the same manifest.
# At most one of those two rows was ever a grant, and the registry says which.
cms = json.loads(fx("npm-canvas-mcp-server.json"))
cms_ver = cms["versions"][cms["dist-tags"]["latest"]]
check("the contested npm name resolves to exactly one repository",
      grant.first_slug([(cms_ver.get("repository") or {}).get("url", "") or "",
                        cms_ver.get("homepage") or ""]),
      "DMontgomery40/mcp-canvas-lms")

# --- Maven: the licence is in the POM, and the POM is not maven-metadata.xml --
check("maven-metadata.xml carries NO licence element, so reading it answers absent",
      grant.maven_licence(fx("maven-verapdf-metadata.xml")), (None, "absent"))
check("and the released POM genuinely has no <licenses> block either",
      grant.maven_licence(fx("maven-verapdf-1.30.2.pom")), (None, "absent"))
check("a <licenses> block inside <dependencies> is a dependency's grant, not the "
      "project's",
      grant.maven_licence("<project><dependencies><dependency><licenses><license>"
                          "<name>GPL-2.0</name></license></licenses></dependency>"
                          "</dependencies></project>"),
      (None, "absent"))
check("the project's own <licenses> block is read",
      grant.maven_licence("<project><licenses><license><name>Apache License, "
                          "Version 2.0</name></license></licenses></project>"),
      (["Apache License, Version 2.0"], "pom.licenses"))

# POM coordinates.  A first-match scan returns the PARENT's groupId in a POM that
# declares <parent> first, and a DEPENDENCY's in a flattened one.  Both publish a
# coordinate belonging to somebody else.
check("the project's own coordinates win over its parent's",
      grant.pom_coordinates("<project><parent><groupId>org.parent</groupId>"
                            "<artifactId>par</artifactId></parent>"
                            "<groupId>org.mine</groupId><artifactId>mine</artifactId>"
                            "</project>"), "org.mine:mine")
check("an inherited groupId falls back to the parent's, which is what Maven does",
      grant.pom_coordinates("<project><parent><groupId>org.parent</groupId>"
                            "<artifactId>par</artifactId></parent>"
                            "<artifactId>mine</artifactId></project>"),
      "org.parent:mine")
check("a dependency's coordinates never win",
      grant.pom_coordinates("<project><groupId>org.mine</groupId>"
                            "<artifactId>mine</artifactId><dependencies><dependency>"
                            "<groupId>org.other</groupId><artifactId>o</artifactId>"
                            "</dependency></dependencies></project>"), "org.mine:mine")
check("the real veraPDF root POM resolves to its own coordinates",
      grant.pom_coordinates(fx("pom-verapdf-root.xml")), "org.verapdf:verapdf-library")
check("and its <scm> names the repository, which is the ownership datum",
      grant.first_slug(["https://github.com/veraPDF/veraPDF-library/"]),
      "veraPDF/veraPDF-library")

# --- scope: a zero denominator is a path fault, not a clean sweep (P355) -----
for script in ("grant.py", "widen.py"):
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
        empty = f.name
    r = subprocess.run([sys.executable, "-I", os.path.join(HERE, script), empty,
                        os.devnull], capture_output=True, cwd=HERE)
    os.unlink(empty)
    check("%s exits 2 on an empty denominator" % script, r.returncode, 2)

# --- the widening's own guard ------------------------------------------------
import widen  # noqa: E402
check("the wide list and p436's narrow list do not overlap, or the widening would "
      "double-count", sorted(set(widen.WIDE) & set(widen.NARROW)), [])
check("LICENSE.GPL -- the name that made veraPDF read as unlicensed -- is in the "
      "wide list", "LICENSE.GPL" in widen.WIDE, True)
check("a licence INVENTORY is still excluded, carrying pass 52's rule forward",
      any(n in ("LICENSES", "licenses.json") for n in widen.WIDE), False)
check("the planted name is not a real convention, so a 200 on it means the probe "
      "answers 200 to everything", widen.PLANTED.startswith("LICENSE.globant-kb"),
      True)

TOTAL = 30
if FAIL:
    print("FAIL (%d of %d)" % (len(FAIL), TOTAL))
    for f in FAIL:
        print("  -", f)
    sys.exit(1)
print("%d/%d assertions pass, no network" % (TOTAL, TOTAL))
