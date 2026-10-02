"""Pase 47, action 1 (gap 100). Only the standard library.

    python3 test_pack.py                       # structural checks
    SCORM_SCHEMAS=.../scorm-mcp-server/schemas \
    SCORM_SCHEMAS12=.../scorm-mcp-server/schemas12 \
      python3 test_pack.py --with-xmllint      # + the real conformance matrix

The four assertions action 1 asked for are tagged [A1]..[A4]. Everything after
them is the dialect matrix, which is where this pass's finding lives.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pack_marking import (  # noqa: E402
    CARRIER_FOREIGN,
    CARRIER_LOM,
    MARKER_NS,
    PackageError,
    detect_dialect,
    inject_into_manifest,
    iter_entries,
    mark_package,
    marked_spans,
    read_manifest,
)

HERE = os.path.dirname(os.path.abspath(__file__))
PASSED = 0
FAILED: list[str] = []


def check(label: str, cond: bool, detail: str = "") -> None:
    global PASSED
    if cond:
        PASSED += 1
        print("  ok   %s" % label)
    else:
        FAILED.append(label)
        print("  FAIL %s %s" % (label, detail))


# --------------------------------------------------------------------------
# fixtures: the manifests scorm-mcp-server's buildManifest/buildManifest12
# actually emit, copied shape for shape from src/converter.ts (lines 509 and
# 566 at the HEAD read on 2026-10-02).
# --------------------------------------------------------------------------

M2004 = """<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="PKG-1" version="1.0"
  xmlns="http://www.imsglobal.org/xsd/imscp_v1p1"
  xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_v1p3"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.imsglobal.org/xsd/imscp_v1p1 imscp_v1p1.xsd \
http://www.adlnet.org/xsd/adlcp_v1p3 adlcp_v1p3.xsd">
  <metadata>
    <schema>ADL SCORM</schema>
    <schemaversion>2004 4th Edition</schemaversion>
  </metadata>
  <organizations default="ORG-1">
    <organization identifier="ORG-1">
      <title>Curso</title>
      <item identifier="ITEM-1" identifierref="RES-1" isvisible="true">
        <title>Curso</title>
      </item>
    </organization>
  </organizations>
  <resources>
    <resource identifier="RES-1" type="webcontent" adlcp:scormType="sco" href="index.html">
      <file href="index.html"/>
    </resource>
  </resources>
</manifest>
"""

M12 = """<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="PKG-1" version="1.2"
  xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2"
  xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_rootv1p2"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.imsproject.org/xsd/imscp_rootv1p1p2 \
imscp_rootv1p1p2.xsd http://www.adlnet.org/xsd/adlcp_rootv1p2 adlcp_rootv1p2.xsd">
  <metadata>
    <schema>ADL SCORM</schema>
    <schemaversion>1.2</schemaversion>
  </metadata>
  <organizations default="ORG-1">
    <organization identifier="ORG-1">
      <title>Curso</title>
      <item identifier="ITEM-1" identifierref="RES-1" isvisible="true">
        <title>Curso</title>
      </item>
    </organization>
  </organizations>
  <resources>
    <resource identifier="RES-1" type="webcontent" adlcp:scormtype="sco" href="index.html">
      <file href="index.html"/>
    </resource>
  </resources>
</manifest>
"""

# A manifest with NO course-level <metadata>, but WITH one on the resource --
# the case that makes "insert before the first </metadata>" wrong, not just
# unlucky. Must be rejected, not stapled to the resource.
M_RESOURCE_ONLY = M2004.replace(
    """  <metadata>
    <schema>ADL SCORM</schema>
    <schemaversion>2004 4th Edition</schemaversion>
  </metadata>
""",
    "",
).replace(
    '      <file href="index.html"/>',
    """      <metadata>
        <schema>ADL SCORM</schema>
      </metadata>
      <file href="index.html"/>""",
)

#: One quoted span, one tutor inference, one learner observation -- the same
#: three-span turn ../aiact-50-2-marking/test_marking.py uses, so the two
#: modules agree on a single fixture.
ARTIFACT = {
    "text": (
        "El teorema dice que la suma de los angulos interiores es 180 grados. "
        "Eso implica que en tu triangulo el tercer angulo mide 35 grados. "
        "Yo medi 34 con el transportador."
    ),
    "spans": [
        {"start": 0, "end": 67, "provenance": "direct_source", "synthetic": False},
        {"start": 67, "end": 131, "provenance": "mentor_inference", "synthetic": True},
        {"start": 131, "end": 165, "provenance": "learner_observation", "synthetic": False},
    ],
}

ARTIFACT_QUOTE_ONLY = {
    "text": "El teorema dice que la suma de los angulos interiores es 180 grados.",
    "spans": [
        {"start": 0, "end": 67, "provenance": "direct_source", "synthetic": False}
    ],
}


def build_pkg(path: str, manifest: str) -> None:
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("imsmanifest.xml", manifest)
        z.writestr("index.html", "<!doctype html><title>Curso</title><p>Hola")
        z.writestr("assets/logo.svg", "<svg xmlns='http://www.w3.org/2000/svg'/>")
        z.writestr("stored.txt", "no compression", zipfile.ZIP_STORED)


# --------------------------------------------------------------------------
# xmllint plumbing
# --------------------------------------------------------------------------

SCHEMAS = os.environ.get("SCORM_SCHEMAS")
SCHEMAS12 = os.environ.get("SCORM_SCHEMAS12")
WITH_XMLLINT = "--with-xmllint" in sys.argv

WRAPPER_12 = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">\n'
    '  <xsd:import namespace="http://www.imsproject.org/xsd/imscp_rootv1p1p2"'
    ' schemaLocation="imscp_rootv1p1p2.xsd"/>\n'
    '  <xsd:import namespace="http://www.adlnet.org/xsd/adlcp_rootv1p2"'
    ' schemaLocation="adlcp_rootv1p2.xsd"/>\n'
    "</xsd:schema>\n"
)
#: 🟢 The one-line upstream fix: the third bundled namespace, which
#: scorm-mcp-server ships in schemas12/ and its own wrapper never imports.
IMPORT_MD = (
    '  <xsd:import namespace="http://www.imsglobal.org/xsd/imsmd_rootv1p2p1"'
    ' schemaLocation="imsmd_rootv1p2p1.xsd"/>\n'
)
IMPORT_MARKER = (
    '  <xsd:import namespace="urn:globant:aiact:50-2"'
    ' schemaLocation="aiact-50-2.xsd"/>\n'
)


def validate(manifest_xml: str, dialect: str, extra_imports: str = "") -> tuple[bool, str]:
    """Run the real xmllint, assembling the schema set the dialect needs."""
    tmp = tempfile.mkdtemp(prefix="aiact-pack-")
    try:
        src = SCHEMAS if dialect == "2004" else SCHEMAS12
        for name in os.listdir(src):
            if name.lower().endswith(".xsd"):
                shutil.copy(os.path.join(src, name), tmp)
        shutil.copy(os.path.join(HERE, "aiact-50-2.xsd"), tmp)
        if dialect == "1.2":
            root = os.path.join(tmp, "wrapper12.xsd")
            with open(root, "w") as fh:
                fh.write(WRAPPER_12.replace("</xsd:schema>", extra_imports + "</xsd:schema>"))
        else:
            root = os.path.join(tmp, "imscp_v1p1.xsd")
        man = os.path.join(tmp, "imsmanifest.xml")
        with open(man, "w") as fh:
            fh.write(manifest_xml)
        proc = subprocess.run(
            ["xmllint", "--noout", "--schema", root, man],
            capture_output=True, text=True,
        )
        return proc.returncode == 0, (proc.stderr or "").strip()
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# --------------------------------------------------------------------------
print("== dialect detection ==")
check("2004 manifest detected as 2004", detect_dialect(M2004) == "2004")
check("1.2 manifest detected as 1.2", detect_dialect(M12) == "1.2")
try:
    detect_dialect("<manifest/>")
    check("a dialect-less manifest is refused", False)
except PackageError as exc:
    check("a dialect-less manifest is refused", "refusing to guess" in str(exc))

print("== [A4] a package with no course-level <metadata> is REJECTED ==")
try:
    inject_into_manifest(M_RESOURCE_ONLY, ARTIFACT)
    check("[A4] rejected with a clear error", False, "no exception raised")
except PackageError as exc:
    msg = str(exc)
    check(
        "[A4] rejected with a clear error",
        "no manifest-level <metadata>" in msg and "Refusing" in msg,
        msg[:90],
    )
check(
    "[A4] and it is NOT the 'first </metadata>' that was found",
    "<metadata>" in M_RESOURCE_ONLY,
)

print("== [A3] re-injection is idempotent ==")
for name, manifest in (("2004", M2004), ("1.2", M12)):
    once = inject_into_manifest(manifest, ARTIFACT)
    twice = inject_into_manifest(once, ARTIFACT)
    check("[A3] %s: inject(inject(x)) == inject(x)" % name, once == twice)
    check(
        "[A3] %s: marker appears exactly once" % name,
        twice.count(MARKER_NS) == once.count(MARKER_NS) == 1,
        "%d vs %d" % (twice.count(MARKER_NS), once.count(MARKER_NS)),
    )
    thrice = inject_into_manifest(twice, ARTIFACT_QUOTE_ONLY)
    check(
        "[A3] %s: re-injection UPDATES the spans, it does not append" % name,
        marked_spans(thrice) == [] and thrice.count(MARKER_NS) == 1,
        marked_spans(thrice),
    )

print("== spans survive the manifest round trip ==")
check(
    "2004 carrier reports the one synthetic span",
    marked_spans(inject_into_manifest(M2004, ARTIFACT)) == [(67, 131)],
    marked_spans(inject_into_manifest(M2004, ARTIFACT)),
)
check(
    "1.2 carrier reports the same span through keyword strings",
    marked_spans(inject_into_manifest(M12, ARTIFACT)) == [(67, 131)],
    marked_spans(inject_into_manifest(M12, ARTIFACT)),
)
check(
    "a quote-only turn marks generated=false in 2004",
    'value="false"' in inject_into_manifest(M2004, ARTIFACT_QUOTE_ONLY),
)
check(
    "a quote-only turn marks ai-generated:false in 1.2",
    "ai-generated:false" in inject_into_manifest(M12, ARTIFACT_QUOTE_ONLY),
)

print("== the ZIP: everything that is not the manifest is untouched ==")
work = tempfile.mkdtemp(prefix="aiact-pack-zip-")
try:
    src = os.path.join(work, "course.zip")
    dst = os.path.join(work, "course-marked.zip")
    build_pkg(src, M2004)
    report = mark_package(src, dst, ARTIFACT)
    check("report names the dialect and carrier",
          report["dialect"] == "2004" and report["carrier"] == CARRIER_FOREIGN, report)
    check("report counts the synthetic spans", report["synthetic_spans"] == 1, report)
    check("entry names and order are preserved",
          [n for n, _ in iter_entries(src)] == [n for n, _ in iter_entries(dst)])
    check("per-entry compress_type is preserved (stored stays stored)",
          dict(iter_entries(src)) == dict(iter_entries(dst)))
    with zipfile.ZipFile(src) as a, zipfile.ZipFile(dst) as b:
        same = [n for n in a.namelist() if n != "imsmanifest.xml"]
        check("every non-manifest payload is byte-identical",
              all(a.read(n) == b.read(n) for n in same))
        check("the manifest DID change", a.read("imsmanifest.xml") != b.read("imsmanifest.xml"))
    check("[A1-pre] the marked manifest is still well-formed XML",
          detect_dialect(read_manifest(dst)) == "2004")
    check("the marked package can be read back and re-marked",
          mark_package(dst, os.path.join(work, "again.zip"), ARTIFACT)["synthetic_spans"] == 1)
    with zipfile.ZipFile(dst) as b:
        check("re-marking stays at one marker in the ZIP too",
              b.read("imsmanifest.xml").decode().count(MARKER_NS) == 1)

    bad = os.path.join(work, "notscorm.zip")
    with zipfile.ZipFile(bad, "w") as z:
        z.writestr("index.html", "x")
    try:
        mark_package(bad, os.path.join(work, "never.zip"), ARTIFACT)
        check("a ZIP with no imsmanifest.xml is refused", False)
    except PackageError as exc:
        check("a ZIP with no imsmanifest.xml is refused", "not a SCORM package" in str(exc))
    check("and no output file was left behind",
          not os.path.exists(os.path.join(work, "never.zip")))

    nometa = os.path.join(work, "nometa.zip")
    build_pkg(nometa, M_RESOURCE_ONLY)
    try:
        mark_package(nometa, os.path.join(work, "nometa-out.zip"), ARTIFACT)
        check("[A4] a package without course metadata writes NOTHING", False)
    except PackageError:
        check("[A4] a package without course metadata writes NOTHING",
              not os.path.exists(os.path.join(work, "nometa-out.zip")))
finally:
    shutil.rmtree(work, ignore_errors=True)

# --------------------------------------------------------------------------
print("== [A1][A2] the conformance matrix (xmllint) ==")
if not WITH_XMLLINT:
    print("  skipped: pass --with-xmllint with SCORM_SCHEMAS and SCORM_SCHEMAS12")
elif not (SCHEMAS and SCHEMAS12 and os.path.isdir(SCHEMAS) and os.path.isdir(SCHEMAS12)):
    print("  skipped: SCORM_SCHEMAS / SCORM_SCHEMAS12 do not both point at a directory")
else:
    ok, err = validate(M2004, "2004")
    check("[A2] control: the UNMARKED 2004 manifest validates", ok, err[:120])
    ok, err = validate(M12, "1.2")
    check("[A2] control: the UNMARKED 1.2 manifest validates", ok, err[:120])

    ok, err = validate(inject_into_manifest(M2004, ARTIFACT), "2004")
    check("[A1] 2004 + foreign marker validates (lax wildcard)", ok, err[:160])

    ok, err = validate(inject_into_manifest(M12, ARTIFACT, CARRIER_FOREIGN), "1.2")
    check(
        "🔴 1.2 + foreign marker FAILS against the wrapper as shipped",
        (not ok) and "strict wildcard" in err,
        err[:160],
    )
    ok, err = validate(
        inject_into_manifest(M12, ARTIFACT, CARRIER_FOREIGN), "1.2", IMPORT_MARKER
    )
    check("1.2 + foreign marker validates once aiact-50-2.xsd is imported", ok, err[:160])

    ok, err = validate(inject_into_manifest(M12, ARTIFACT, CARRIER_LOM), "1.2")
    check(
        "🔴 1.2 + LOM carrier ALSO fails against the wrapper as shipped",
        (not ok) and "strict wildcard" in err,
        err[:160],
    )
    ok, err = validate(inject_into_manifest(M12, ARTIFACT, CARRIER_LOM), "1.2", IMPORT_MD)
    check("🟢 1.2 + LOM carrier validates with the one-line wrapper fix", ok, err[:160])

    # The control that makes the bug a bug: the LOM shape is not ours, it is
    # what SCORM 1.2 itself prescribes for inline metadata.
    plain_lom = M12.replace(
        "  </metadata>",
        '    <imsmd:lom xmlns:imsmd="http://www.imsglobal.org/xsd/imsmd_rootv1p2p1">\n'
        "      <imsmd:general>\n"
        '        <imsmd:title><imsmd:langstring xml:lang="es">Curso</imsmd:langstring>'
        "</imsmd:title>\n"
        "      </imsmd:general>\n"
        "    </imsmd:lom>\n"
        "  </metadata>",
    )
    ok, err = validate(plain_lom, "1.2")
    check(
        "🔴 and so does a package carrying ONLY standard SCORM 1.2 LOM metadata",
        (not ok) and "strict wildcard" in err,
        err[:160],
    )
    ok, err = validate(plain_lom, "1.2", IMPORT_MD)
    check("🟢 which the same one-line fix repairs", ok, err[:160])

    ok, err = validate(inject_into_manifest(M2004, ARTIFACT, CARRIER_LOM), "2004")
    check("the LOM carrier also validates in 2004 (so it is the portable one)", ok, err[:160])

print()
print("%d/%d checks passed" % (PASSED, PASSED + len(FAILED)))
for name in FAILED:
    print("  failed: %s" % name)
sys.exit(1 if FAILED else 0)
