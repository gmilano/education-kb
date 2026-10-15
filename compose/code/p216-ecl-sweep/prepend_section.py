#!/usr/bin/env python3
"""Insert a pass section directly after a shelf's YAML frontmatter, and bump `updated:`.

The frontmatter is load-bearing: the compiler reads `industry`, `region` and `updated` to build
typed entities, and `region` is a CLOSED vocabulary (North America | EMEA | APAC | LATAM |
Global). This script never touches the three keys' names or the region value — it only rewrites
the `updated:` date — and it never reorders or rewrites the body, so the two append-only shelves
keep their history intact below the new section.

usage: prepend_section.py <shelf.md> <section.md> <YYYY-MM-DD>
"""

import sys

VALID_REGIONS = {"North America", "EMEA", "APAC", "LATAM", "Global"}


def main(shelf, section, date):
    with open(shelf, encoding="utf-8") as fh:
        text = fh.read()
    with open(section, encoding="utf-8") as fh:
        new = fh.read().rstrip("\n") + "\n"

    if not text.startswith("---\n"):
        sys.exit(f"{shelf}: no YAML frontmatter — refusing to write")
    end = text.index("\n---\n", 3) + len("\n---\n")
    fm, body = text[:end], text[end:]

    region = None
    for line in fm.splitlines():
        if line.startswith("region:"):
            region = line.split(":", 1)[1].strip()
    if region not in VALID_REGIONS:
        sys.exit(f"{shelf}: region {region!r} is outside the closed vocabulary — refusing")

    out = []
    for line in fm.splitlines():
        out.append(f"updated: {date}" if line.startswith("updated:") else line)
    fm = "\n".join(out) + "\n"

    with open(shelf, "w", encoding="utf-8") as fh:
        fh.write(fm + "\n\n" + new + body.lstrip("\n"))
    print(f"{shelf}: +{len(new.splitlines())} lines, region={region}, updated={date}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
