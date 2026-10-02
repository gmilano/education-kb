"""Inject the Article 50(2) marking into an ALREADY BUILT SCORM package.

Pase 47, action 1 (gap 100). Pase 46 proved two things about the marker and
left a third unmeasured:

  * the marker is legal inside <metadata> of a SCORM **2004** manifest
    (``metadataType`` ends in ``grp.any`` -> ``xsd:any namespace="##other"
    processContents="lax"``), and
  * ``buildManifest``/``buildManifest12`` of ``scorm-mcp-server`` emit the
    manifest as a string literal with no extension parameter, so the generator
    cannot emit it -- hence this post-processor.

🔴 What pase 46 did NOT measure, and what this module had to: the SAME
generator emits TWO dialects, and their wildcards do not agree.

    schemas/imscp_v1p1.xsd        grp.any -> processContents="lax"
    schemas12/imscp_rootv1p1p2.xsd grp.any -> processContents="strict"

Under ``strict`` the validator MUST find a global element declaration for the
foreign element. A marker in a namespace nobody imported is therefore not
"unknown but tolerated" -- it is INVALID. Measured, verbatim:

    Element '{urn:globant:aiact:50-2}aiGenerated': No matching global element
    declaration available, but demanded by the strict wildcard.

So the marker needs a dialect-aware carrier, and this module ships both:

    CARRIER_FOREIGN  <m:aiGenerated> in its own namespace. Typed spans as
                     attributes. Validates in 2004 as shipped. In 1.2 it
                     validates ONLY if the validating schema set imports a
                     declaration for the namespace -- ``aiact-50-2.xsd``,
                     next to this file, is that declaration.
    CARRIER_LOM      <imsmd:lom><imsmd:classification> using ONLY elements the
                     IMS MD 1.2 schema declares. Needs no extra XSD. Spans are
                     encoded into keyword strings, so the structure is lost and
                     the consumer has to parse.

Only the standard library. See README.md for the measured matrix and for the
one-line upstream bug this turned up in ``scorm-mcp-server``'s own validator.
"""

from __future__ import annotations

import re
import xml.parsers.expat
import zipfile
from typing import Any, Iterable

#: Namespace of the foreign-element carrier. Declared in ``aiact-50-2.xsd``.
MARKER_NS = "urn:globant:aiact:50-2"

#: SCORM 2004 content-packaging namespace (``buildManifest``).
CP_NS_2004 = "http://www.imsglobal.org/xsd/imscp_v1p1"
#: SCORM 1.2 content-packaging namespace (``buildManifest12``).
CP_NS_12 = "http://www.imsproject.org/xsd/imscp_rootv1p1p2"
#: IMS Metadata 1.2, the namespace CARRIER_LOM rides in.
MD_NS_12 = "http://www.imsglobal.org/xsd/imsmd_rootv1p2p1"

CARRIER_FOREIGN = "foreign"
CARRIER_LOM = "lom"

#: Default carrier per dialect: the one that validates against the schemas the
#: dialect's own validator actually assembles.
DEFAULT_CARRIER = {"2004": CARRIER_FOREIGN, "1.2": CARRIER_LOM}

MANIFEST_NAME = "imsmanifest.xml"
PROFILE = "aiact-50-2/span/v1"


class PackageError(ValueError):
    """The package cannot carry a marking, and why -- never a silent rewrite."""


# --------------------------------------------------------------------------
# dialect
# --------------------------------------------------------------------------

def detect_dialect(manifest_xml: str) -> str:
    """``"2004"`` or ``"1.2"``, by content-packaging namespace.

    The namespace is the discriminator rather than ``<schemaversion>`` because
    the namespace is what the validator keys its schema set on.
    """
    if CP_NS_2004 in manifest_xml:
        return "2004"
    if CP_NS_12 in manifest_xml:
        return "1.2"
    raise PackageError(
        "%s declares neither the SCORM 2004 nor the SCORM 1.2 content-packaging "
        "namespace; refusing to guess a dialect." % MANIFEST_NAME
    )


# --------------------------------------------------------------------------
# where the marker goes
# --------------------------------------------------------------------------

def manifest_metadata_end(manifest_xml: str) -> int:
    """Byte offset of ``</metadata>`` of the MANIFEST-level ``<metadata>``.

    ``<metadata>`` is legal on ``organization``, ``item``, ``resource`` and
    ``file`` too (nine ``grp.any`` extension points, nine ``<metadata>``
    slots), so "the first ``</metadata>``" is not a safe target: a package whose
    only metadata sits on a resource would get the course-level marking stapled
    to one file. expat is used instead of a regex because it gives the real byte
    index and because a malformed manifest must fail here rather than later.
    """
    hits: list[int] = []
    stack: list[str] = []
    parser = xml.parsers.expat.ParserCreate(namespace_separator=" ")

    def start(name: str, _attrs: dict[str, str]) -> None:
        stack.append(name)

    def end(name: str) -> None:
        # depth 2 == direct child of <manifest>; expat fires end AFTER popping
        # is our job, so the element being closed is still on the stack.
        if len(stack) == 2 and name.split(" ")[-1] == "metadata":
            hits.append(parser.CurrentByteIndex)
        stack.pop()

    parser.StartElementHandler = start
    parser.EndElementHandler = end
    try:
        parser.Parse(manifest_xml.encode("utf-8"), True)
    except xml.parsers.expat.ExpatError as exc:
        raise PackageError("%s is not well-formed XML: %s" % (MANIFEST_NAME, exc))

    if not hits:
        raise PackageError(
            "%s has no manifest-level <metadata> element, so there is nowhere "
            "to put the Article 50(2) marking. Refusing to synthesise one: "
            "<metadata> is optional in the schema but its position is not, and "
            "a package that never declared <schema>/<schemaversion> is not a "
            "package this module should be the first to touch." % MANIFEST_NAME
        )
    return hits[0]


# --------------------------------------------------------------------------
# the two carriers
# --------------------------------------------------------------------------

def _ranges(artifact: dict[str, Any]) -> list[tuple[int, int]]:
    """Synthetic spans, as ``(start, end)``, in document order.

    Mirrors ``synthetic_ranges`` of ``../aiact-50-2-marking/marking.py`` so the
    two modules cannot drift on what counts as a synthetic span.
    """
    out = []
    for span in artifact.get("spans") or ():
        if span.get("synthetic"):
            out.append((int(span["start"]), int(span["end"])))
    return sorted(out)


def _generated(artifact: dict[str, Any]) -> bool:
    """The OR over the spans -- measured, not assumed.

    ``turn_pipeline.py`` of OpenTutor pins ``generated=True`` on the agent path
    and so cannot represent a turn that only quotes; this follows the spans.
    """
    if artifact.get("spans") is not None:
        return bool(_ranges(artifact))
    return bool(artifact.get("generated"))


def fragment_foreign(artifact: dict[str, Any], indent: str = "    ") -> str:
    """CARRIER_FOREIGN: typed spans in our own namespace."""
    spans = "".join(
        '\n%s  <m:span start="%d" end="%d"/>' % (indent, a, b)
        for a, b in _ranges(artifact)
    )
    return (
        '%s<m:aiGenerated xmlns:m="%s" value="%s" profile="%s">%s\n%s</m:aiGenerated>\n'
        % (
            indent,
            MARKER_NS,
            "true" if _generated(artifact) else "false",
            artifact.get("marking_profile") or PROFILE,
            spans,
            indent,
        )
    )


def fragment_lom(artifact: dict[str, Any], indent: str = "    ") -> str:
    """CARRIER_LOM: only elements IMS MD 1.2 declares, so ``strict`` resolves.

    ``classificationType`` is ``purpose?``, ``taxonpath*``, ``description?``,
    ``keyword*``, ``grp.any``. 🔴 Its ``grp.any`` is ``##any`` + ``strict``, so
    a foreign element is no more welcome INSIDE the LOM than outside it: the
    span list has to become strings.
    """
    kw = ['ai-generated:%s' % ("true" if _generated(artifact) else "false")]
    kw += ["ai-generated-span:%d-%d" % (a, b) for a, b in _ranges(artifact)]
    kw.append("ai-marking-profile:%s" % (artifact.get("marking_profile") or PROFILE))
    lines = [
        '%s<imsmd:lom xmlns:imsmd="%s">' % (indent, MD_NS_12),
        "%s  <imsmd:classification>" % indent,
        "%s    <imsmd:purpose>" % indent,
        '%s      <imsmd:source><imsmd:langstring xml:lang="x-none">%s'
        "</imsmd:langstring></imsmd:source>" % (indent, MARKER_NS),
        '%s      <imsmd:value><imsmd:langstring xml:lang="x-none">aiGenerated'
        "</imsmd:langstring></imsmd:value>" % indent,
        "%s    </imsmd:purpose>" % indent,
    ]
    for k in kw:
        lines.append(
            '%s    <imsmd:keyword><imsmd:langstring xml:lang="x-none">%s'
            "</imsmd:langstring></imsmd:keyword>" % (indent, k)
        )
    lines += ["%s  </imsmd:classification>" % indent, "%s</imsmd:lom>" % indent]
    return "\n".join(lines) + "\n"


FRAGMENTS = {CARRIER_FOREIGN: fragment_foreign, CARRIER_LOM: fragment_lom}

# Idempotency: both carriers are recognised by the marker namespace appearing
# as a namespace declaration (foreign) or as a classification source (LOM).
_EXISTING = {
    CARRIER_FOREIGN: re.compile(
        r"[ \t]*<(\w+:)?aiGenerated\b[^>]*>.*?</(\w+:)?aiGenerated>\n?", re.S
    ),
    CARRIER_LOM: re.compile(
        r"[ \t]*<(\w+:)?lom\b[^>]*>(?:(?!</(?:\w+:)?lom>).)*?"
        + re.escape(MARKER_NS)
        + r".*?</(\w+:)?lom>\n?",
        re.S,
    ),
}


def strip_marking(manifest_xml: str) -> str:
    """Remove any marking this module wrote. Makes re-injection idempotent."""
    out = manifest_xml
    for pattern in _EXISTING.values():
        out = pattern.sub("", out)
    return out


def inject_into_manifest(
    manifest_xml: str, artifact: dict[str, Any], carrier: str | None = None
) -> str:
    """Return ``manifest_xml`` with the marking spliced into ``<metadata>``.

    Re-injection is idempotent: any previous marking is stripped first, so
    ``inject(inject(x)) == inject(x)`` byte for byte.
    """
    dialect = detect_dialect(manifest_xml)
    carrier = carrier or DEFAULT_CARRIER[dialect]
    if carrier not in FRAGMENTS:
        raise PackageError("unknown carrier %r" % (carrier,))

    base = strip_marking(manifest_xml)
    cut = manifest_metadata_end(base)
    indent = re.search(r"([ \t]*)$", base[:cut]).group(1) or "    "
    fragment = FRAGMENTS[carrier](artifact, indent=indent)
    return base[:cut] + fragment.lstrip("\n") + indent + base[cut:].lstrip()


# --------------------------------------------------------------------------
# the package
# --------------------------------------------------------------------------

def read_manifest(zip_path: str) -> str:
    with zipfile.ZipFile(zip_path) as zf:
        names = [n for n in zf.namelist() if n.lower() == MANIFEST_NAME]
        if not names:
            raise PackageError(
                "%s is not a SCORM package: no %s at the archive root."
                % (zip_path, MANIFEST_NAME)
            )
        return zf.read(names[0]).decode("utf-8")


def mark_package(
    src: str, dst: str, artifact: dict[str, Any], carrier: str | None = None
) -> dict[str, Any]:
    """Rewrite ``src`` into ``dst`` with ``imsmanifest.xml`` marked.

    Every other entry is copied byte for byte, in its original order and with
    its original ``compress_type`` -- an LMS that checksums the assets must see
    the same assets. Nothing is written to ``dst`` until the new manifest is
    built, so a rejected package leaves no half-written output behind.
    """
    manifest = read_manifest(src)
    dialect = detect_dialect(manifest)
    carrier = carrier or DEFAULT_CARRIER[dialect]
    marked = inject_into_manifest(manifest, artifact, carrier)  # may raise

    with zipfile.ZipFile(src) as zf:
        infos = zf.infolist()
        blobs = {i.filename: zf.read(i.filename) for i in infos}

    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as out:
        for info in infos:
            data = (
                marked.encode("utf-8")
                if info.filename.lower() == MANIFEST_NAME
                else blobs[info.filename]
            )
            keep = zipfile.ZipInfo(info.filename, date_time=info.date_time)
            keep.compress_type = info.compress_type
            keep.external_attr = info.external_attr
            out.writestr(keep, data)

    return {
        "dialect": dialect,
        "carrier": carrier,
        "generated": _generated(artifact),
        "synthetic_spans": len(_ranges(artifact)),
        "entries": len(infos),
    }


def marked_spans(manifest_xml: str) -> list[tuple[int, int]]:
    """Read the spans back out of either carrier -- the round trip."""
    foreign = re.findall(r'<(?:\w+:)?span start="(\d+)" end="(\d+)"', manifest_xml)
    if foreign:
        return [(int(a), int(b)) for a, b in foreign]
    lom = re.findall(r"ai-generated-span:(\d+)-(\d+)", manifest_xml)
    return [(int(a), int(b)) for a, b in lom]


def iter_entries(zip_path: str) -> Iterable[tuple[str, int]]:
    with zipfile.ZipFile(zip_path) as zf:
        for info in zf.infolist():
            yield info.filename, info.compress_type
