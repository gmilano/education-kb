#!/usr/bin/env python3
"""Read the licence a Maven POM declares. Run: python3 -I pom_license.py <pom.xml>

Why this is not a `sed` one-liner, which is what the first draft of `scan_maven_payload.sh`
used:

    tr -d '\\n' | sed -n 's:.*<licenses>.*<license>.*<name>\\([^<]*\\)</name>.*:\\1:p'

Flattening the document and matching `.*<name>` is greedy, so on a real POM it ran past
`</licenses>` and returned the first `<name>` it could still reach — which is inside
`<developers>`. It published **`Braden Anderson`** as the licence of
`org.imsglobal:basiclti-util`, **`Toby Murray`** for `edu.ksu.ome.lti:lti-launch` and
**`Sakai Core Team`** for `org.sakaiproject.kernel:sakai-kernel-api`. All three are
developer names. A POM is XML and gets an XML parser.

Prints one line per declared licence: `name<TAB>url`, or `NONE_DECLARED`.
Maven POMs are namespaced (`http://maven.apache.org/POM/4.0.0`), and some omit it, so the
namespace is stripped rather than assumed.
"""
import sys
import xml.etree.ElementTree as ET


def _tag(el):
    """Local name, namespace stripped."""
    return el.tag.rsplit("}", 1)[-1] if "}" in el.tag else el.tag


def declared_licences(pom_path):
    """Licences declared in the POM's own <project><licenses>, parent POMs excluded.

    Only the direct `project/licenses` child counts. A `<licenses>` nested anywhere else --
    inside `<profiles>`, or a dependency's own metadata -- is not this artefact's grant.
    """
    try:
        root = ET.parse(pom_path).getroot()
    except (ET.ParseError, OSError) as exc:
        return [("PARSE_ERROR", str(exc)[:60])]

    out = []
    for child in root:
        if _tag(child) != "licenses":
            continue
        for lic in child:
            if _tag(lic) != "license":
                continue
            name = url = ""
            for field in lic:
                if _tag(field) == "name":
                    name = (field.text or "").strip()
                elif _tag(field) == "url":
                    url = (field.text or "").strip()
            if name or url:
                out.append((name or "UNNAMED", url))
    return out


def main(argv):
    if len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    lics = declared_licences(argv[1])
    if not lics:
        print("NONE_DECLARED")
        return 0
    for name, url in lics:
        print(f"{name}\t{url}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
