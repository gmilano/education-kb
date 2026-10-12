#!/usr/bin/env python3
"""p153 -- ACTION FJ. Count licence DECLARATION SURFACES per subject, and decide
whether they AGREE.

ACTION FJ (re-registered four times): "audit the other three surface-bearing rows for a
third declaration surface. Count surfaces per row."
Falsifier: refuted if no other row declares more than two.

Four surfaces are read, in this order of authority:

  1. FILE      -- a root LICENSE/LICENCE/COPYING body, classified by distinctive marker.
                  This is what GitHub's own detector reads and what the sidebar shows.
  2. METADATA  -- a package manifest's declared licence field (package.json,
                  pyproject.toml, Cargo.toml, composer.json, setup.py).
  3. BADGE     -- a README shields.io badge or a "License: X" line.
  4. SPDX      -- an SPDX-License-Identifier header inside a source file.

The instrument deliberately does NOT guess an owner or a jurisdiction (T67/T70 forbid it).
It reads only what the subject itself declares, and it reports DISAGREEMENT rather than
resolving it -- resolution is a legal question, not a measurement.

Offline. Reads a directory tree; makes no network call.

    python3 surfaces.py <clones-dir> [subject ...]
"""
import json
import os
import re
import sys

# Distinctive body markers, longest/most-specific first. A GPL family body must be
# tested before the bare "GNU" fallbacks, and AGPL before GPL, because the AGPL body
# contains the string "GNU GENERAL PUBLIC LICENSE" in its own preamble references.
BODY_MARKERS = [
    ("AGPL-3.0", "GNU AFFERO GENERAL PUBLIC LICENSE"),
    ("LGPL-3.0", "GNU LESSER GENERAL PUBLIC LICENSE"),
    ("GPL-3.0", "GNU GENERAL PUBLIC LICENSE"),
    ("Apache-2.0", "APACHE LICENSE"),
    ("MPL-2.0", "MOZILLA PUBLIC LICENSE"),
    ("ECL-2.0", "EDUCATIONAL COMMUNITY LICENSE"),
    ("Unlicense", "THIS IS FREE AND UNENCUMBERED SOFTWARE RELEASED INTO THE PUBLIC DOMAIN"),
    ("MIT", "MIT LICENSE"),
    ("ISC", "ISC LICENSE"),
]

LICENCE_FILENAMES = (
    "LICENSE", "LICENCE", "COPYING",
    "LICENSE.md", "LICENCE.md", "COPYING.md",
    "LICENSE.txt", "LICENCE.txt", "COPYING.txt",
)

# A GPL-family body states its version separately from its name.
VERSION_RE = re.compile(r"\bVERSION\s+(\d)(?:\s*,|\s*$|\s)", re.I)

SPDX_RE = re.compile(r"SPDX-License-Identifier:\s*([A-Za-z0-9.\-+]+)")

# shields.io: .../badge/<label>-<message>-<colour>. The message escapes a literal
# hyphen as "--" and a space as "_", so "Apache--2.0-blue" means "Apache-2.0".
# p153 NOTE: an earlier non-greedy form captured "Apache" from "Apache--2.0" and
# published a FALSE DISAGREE on zavora-ai/mcp-student-records. Found before release.
BADGE_RE = re.compile(r"shields\.io/badge/[Ll]icen[sc]e-([^)\s\"?]+)")
# A plain "License: MIT" or "[![License: MIT]" line.
BADGE_TEXT_RE = re.compile(r"[Ll]icen[sc]e:\s*([A-Za-z0-9.\-+ ]{2,30}?)\s*[\]\)\|\n<]")

def decode_badge_message(tail):
    """Decode a shields.io badge tail into its licence message.

    The tail is "<message>-<colour>[.svg]" with "--" for a literal hyphen and "_" for a
    space. Returns None when nothing survives decoding."""
    if tail.endswith(".svg"):
        tail = tail[:-4]
    parts = re.split(r"(?<!-)-(?!-)", tail)
    message = "-".join(parts[:-1]) if len(parts) >= 2 else tail
    message = message.replace("--", "-").replace("_", " ").strip()
    return message or None


SOURCE_EXT = (
    ".py", ".js", ".ts", ".tsx", ".jsx", ".java", ".rb", ".go", ".rs", ".php",
    ".c", ".h", ".cc", ".cpp", ".hpp", ".cs", ".scala", ".kt", ".swift", ".sh",
)

VENDOR_PARTS = {
    "node_modules", "vendor", "third_party", "thirdparty", "dist", "build",
    ".git", "__pycache__", "site-packages", ".venv", "venv", "bower_components",
}


def normalise_id(raw):
    """Map a declared string onto a comparable SPDX-ish id. Never invents a licence."""
    if raw is None:
        return None
    s = raw.strip().strip('"').strip("'").replace("%20", " ").strip()
    if not s:
        return None
    u = s.upper().replace("_", "-").replace(" ", "-")
    u = u.rstrip("-")
    aliases = {
        "MIT": "MIT",
        "MIT-LICENSE": "MIT",
        "APACHE-2.0": "Apache-2.0",
        "APACHE2.0": "Apache-2.0",
        "APACHE-2": "Apache-2.0",
        "APACHE-LICENSE-2.0": "Apache-2.0",
        "GPL-3.0": "GPL-3.0", "GPLV3": "GPL-3.0", "GPL3": "GPL-3.0",
        "GPL-3.0-ONLY": "GPL-3.0-only", "GPL-3.0-OR-LATER": "GPL-3.0-or-later",
        "AGPL-3.0": "AGPL-3.0", "AGPLV3": "AGPL-3.0",
        "AGPL-3.0-ONLY": "AGPL-3.0-only", "AGPL-3.0-OR-LATER": "AGPL-3.0-or-later",
        "LGPL-3.0": "LGPL-3.0", "LGPLV3": "LGPL-3.0",
        "BSD-3-CLAUSE": "BSD-3-Clause", "BSD-2-CLAUSE": "BSD-2-Clause",
        "MPL-2.0": "MPL-2.0", "ECL-2.0": "ECL-2.0",
        "ISC": "ISC", "UNLICENSE": "Unlicense",
    }
    return aliases.get(u, s)


def family(spdx):
    """The comparable family, so GPL-3.0-only and GPL-3.0-or-later do not read as a
    disagreement. The -only/-or-later election is T81's question, not FJ's."""
    if spdx is None:
        return None
    base = spdx.replace("-only", "").replace("-or-later", "")
    return normalise_id(base) or base


def classify_body(text):
    """Classify a licence body by its distinctive marker. Returns an SPDX id or None."""
    head = text[:4000].upper()
    for spdx, marker in BODY_MARKERS:
        if marker in head:
            if spdx in ("GPL-3.0", "AGPL-3.0", "LGPL-3.0"):
                m = VERSION_RE.search(head[head.index(marker):head.index(marker) + 200])
                if m and m.group(1) != "3":
                    return spdx.replace("3.0", m.group(1) + ".0")
            return spdx
    return None


def read_text(path, limit=200000):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            return fh.read(limit)
    except OSError:
        return ""


def surface_file(root):
    """Surface 1 -- the root licence body."""
    for name in LICENCE_FILENAMES:
        p = os.path.join(root, name)
        if os.path.isfile(p):
            spdx = classify_body(read_text(p))
            if spdx:
                return {"surface": "FILE", "spdx": spdx, "where": name}
            return {"surface": "FILE", "spdx": None, "where": name}
    return None


def surface_metadata(root):
    """Surface 2 -- package manifests at the root AND one level into a monorepo's
    apps/packages dirs, because that is where lumen declares its contradiction."""
    found = []
    candidates = [root]
    for holder in ("apps", "packages", "services", "src"):
        hp = os.path.join(root, holder)
        if os.path.isdir(hp):
            try:
                for entry in sorted(os.listdir(hp))[:20]:
                    ep = os.path.join(hp, entry)
                    if os.path.isdir(ep):
                        candidates.append(ep)
            except OSError:
                pass
    for base in candidates:
        rel = os.path.relpath(base, root)
        pj = os.path.join(base, "package.json")
        if os.path.isfile(pj):
            try:
                data = json.loads(read_text(pj))
                lic = data.get("license") or data.get("licence")
                if isinstance(lic, dict):
                    lic = lic.get("type")
                if isinstance(lic, str) and lic.strip():
                    found.append({"surface": "METADATA", "spdx": normalise_id(lic),
                                  "where": os.path.join(rel, "package.json")})
            except (ValueError, TypeError):
                pass
        for fname, pat in (
            ("pyproject.toml", r'^\s*license\s*=\s*(?:\{\s*text\s*=\s*)?["\']([^"\']+)["\']'),
            ("Cargo.toml", r'^\s*license\s*=\s*["\']([^"\']+)["\']'),
            ("setup.py", r'license\s*=\s*["\']([^"\']+)["\']'),
        ):
            fp = os.path.join(base, fname)
            if os.path.isfile(fp):
                m = re.search(pat, read_text(fp), re.M)
                if m:
                    found.append({"surface": "METADATA", "spdx": normalise_id(m.group(1)),
                                  "where": os.path.join(rel, fname)})
        cj = os.path.join(base, "composer.json")
        if os.path.isfile(cj):
            try:
                data = json.loads(read_text(cj))
                lic = data.get("license")
                if isinstance(lic, list):
                    lic = lic[0] if lic else None
                if isinstance(lic, str) and lic.strip():
                    found.append({"surface": "METADATA", "spdx": normalise_id(lic),
                                  "where": os.path.join(rel, "composer.json")})
            except (ValueError, TypeError):
                pass
    return found


def surface_badge(root):
    """Surface 3 -- a README badge or a 'License: X' line."""
    for name in ("README.md", "README.rst", "README.txt", "readme.md", "README"):
        p = os.path.join(root, name)
        if not os.path.isfile(p):
            continue
        text = read_text(p)
        m = BADGE_RE.search(text)
        if m:
            line = text[:m.start()].count("\n") + 1
            return {"surface": "BADGE",
                    "spdx": normalise_id(decode_badge_message(m.group(1))),
                    "where": "%s:%d" % (name, line)}
        m = BADGE_TEXT_RE.search(text)
        if m:
            line = text[:m.start()].count("\n") + 1
            return {"surface": "BADGE", "spdx": normalise_id(m.group(1)),
                    "where": "%s:%d" % (name, line)}
        return None
    return None


def surface_spdx(root, cap=4000):
    """Surface 4 -- an SPDX-License-Identifier header in first-party source."""
    seen = {}
    n = 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in VENDOR_PARTS]
        for fn in filenames:
            if not fn.endswith(SOURCE_EXT):
                continue
            n += 1
            if n > cap:
                break
            head = read_text(os.path.join(dirpath, fn), 2000)
            m = SPDX_RE.search(head)
            if m:
                spdx = normalise_id(m.group(1))
                rel = os.path.relpath(os.path.join(dirpath, fn), root)
                seen.setdefault(spdx, rel)
        if n > cap:
            break
    return [{"surface": "SPDX", "spdx": k, "where": v} for k, v in sorted(seen.items())]


def audit(root):
    out = []
    f = surface_file(root)
    if f:
        out.append(f)
    out.extend(surface_metadata(root))
    b = surface_badge(root)
    if b:
        out.append(b)
    out.extend(surface_spdx(root))
    return out


def verdict(surfaces):
    """SINGLE / AGREE / DISAGREE / NONE / UNCLASSIFIED.

    DISAGREE is decided on the FAMILY, so a -only/-or-later election is not a
    disagreement. A surface whose body could not be classified is UNCLASSIFIED and
    never silently counted as agreement."""
    ids = [s["spdx"] for s in surfaces if s["spdx"]]
    fams = {family(i) for i in ids}
    if not surfaces:
        return "NONE"
    if not ids:
        return "UNCLASSIFIED"
    if len(surfaces) == 1:
        return "SINGLE"
    if len(fams) > 1:
        return "DISAGREE"
    return "AGREE"


def authoritative(surfaces):
    """What the FILE surface says -- the one GitHub detects and the one that governs.
    Returns None when the subject ships no licence file at all."""
    for s in surfaces:
        if s["surface"] == "FILE":
            return s["spdx"]
    return None


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    base = argv[1]
    subjects = argv[2:] or sorted(
        d for d in os.listdir(base) if os.path.isdir(os.path.join(base, d))
    )
    rows = []
    print("subject\tsurfaces\tdistinct_families\tverdict\tfile_says\tdeclarations")
    for subj in subjects:
        root = os.path.join(base, subj)
        if not os.path.isdir(root):
            print("%s\t-\t-\tMISSING\t-\t-" % subj)
            continue
        surfaces = audit(root)
        v = verdict(surfaces)
        fams = sorted({family(s["spdx"]) for s in surfaces if s["spdx"]})
        decl = " | ".join("%s=%s@%s" % (s["surface"], s["spdx"], s["where"])
                          for s in surfaces)
        print("%s\t%d\t%d\t%s\t%s\t%s" % (
            subj, len(surfaces), len(fams), v, authoritative(surfaces) or "NONE", decl))
        rows.append((subj, len(surfaces), v))
    multi = [r for r in rows if r[1] > 2]
    dis = [r for r in rows if r[2] == "DISAGREE"]
    print("\n# subjects=%d  with_more_than_two_surfaces=%d  DISAGREE=%d"
          % (len(rows), len(multi), len(dis)))
    print("# FJ falsifier: 'refuted if no other row declares more than two' -> %s"
          % ("SILENT (rows exceed two)" if multi else "FIRED (none exceeds two)"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
