"""p215 ACTION QD: read candidate grant blobs and classify by TITLE WINDOW.

Title-window rule (P214-1): GPL-3.0 §13 is titled "Use with the GNU Affero General
Public License" and says Affero 3x in the body, so a whole-body matcher flips
GPL-3.0 -> AGPL-3.0. Classify from the first ~400 chars of meaningful text only.
"""
import json
import subprocess
import sys

RAW = "https://raw.githubusercontent.com/{slug}/HEAD/{path}"


def fetch(slug, path):
    url = RAW.format(slug=slug, path=path)
    p = subprocess.run(["curl", "-sS", "-m", "45", "-w", "\n%{http_code}", url],
                       capture_output=True, text=True)
    out = p.stdout
    if "\n" not in out:
        return None, "000", 0
    body, code = out.rsplit("\n", 1)
    return body, code.strip(), len(body.encode())


def title_window(text):
    """First meaningful lines, where a licence names itself."""
    lines = [l.strip() for l in text.splitlines()]
    lines = [l for l in lines if l and not l.startswith(("#", "<!--"))]
    return " ".join(lines[:6])[:400]


def classify(text):
    w = title_window(text).lower()
    full = text.lower()
    # order matters: most specific first, title window only
    if "affero" in w:
        return "AGPL-3.0"
    if "lesser general public" in w:
        return "LGPL-3.0" if "version 3" in w else "LGPL-2.1"
    if "general public license" in w:
        if "version 3" in w:
            return "GPL-3.0"
        if "version 2" in w:
            return "GPL-2.0"
        return "GPL-?"
    if "apache license" in w:
        return "Apache-2.0" if "2.0" in w else "Apache-?"
    if "mit license" in w or "permission is hereby granted, free of charge" in w:
        return "MIT"
    if "bsd" in w or "redistribution and use in source and binary" in w:
        return "BSD"
    if "mozilla public license" in w:
        return "MPL-2.0"
    if "creative commons" in w or "attribution" in w:
        return "CC-*"
    if "unlicense" in w or "public domain" in w:
        return "Unlicense/PD"
    if "eclipse public license" in w:
        return "EPL"
    # fall back to a body hint, but FLAG it as body-derived
    for tok, name in (("affero general public", "AGPL-3.0?"),
                      ("apache license", "Apache-2.0?"),
                      ("mit license", "MIT?")):
        if tok in full:
            return "BODY:" + name
    return "UNCLASSIFIED"


def manifest_grant(slug, path, text):
    """Extract a license field from a manifest."""
    base = path.split("/")[-1].lower()
    try:
        if base in ("package.json", "composer.json"):
            d = json.loads(text)
            lic = d.get("license") or d.get("licenses")
            if isinstance(lic, list):
                lic = ",".join(
                    (x.get("type") or x.get("name") or str(x)) if isinstance(x, dict) else str(x)
                    for x in lic)
            if isinstance(lic, dict):
                lic = lic.get("type") or lic.get("name")
            return lic
    except Exception:
        pass
    # textual manifests: look for a license line
    for line in text.splitlines():
        ll = line.lower()
        if "license" in ll and any(c in line for c in ":=") and len(line) < 160:
            return line.strip()[:120]
    return None


def main():
    mode = sys.argv[1]           # 'lic' or 'man'
    infile = sys.argv[2]
    rows = []
    with open(infile) as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line:
                continue
            slug, paths = line.split("\t", 1)
            for path in [p for p in paths.split(";") if p][:6]:
                body, code, nb = fetch(slug, path)
                if code != "200" or body is None:
                    rows.append((slug, path, code, nb, "FETCH_" + code))
                    continue
                if mode == "man":
                    g = manifest_grant(slug, path, body)
                    rows.append((slug, path, code, nb, g or "NO_LICENSE_FIELD"))
                else:
                    rows.append((slug, path, code, nb, classify(body)))
    with open(infile.replace(".txt", "_grants.tsv"), "w") as fh:
        fh.write("repo\tpath\thttp\tbytes\tgrant\n")
        for r in rows:
            fh.write("\t".join(str(x) for x in r) + "\n")
    for r in rows:
        print("\t".join(str(x) for x in r))


main()
