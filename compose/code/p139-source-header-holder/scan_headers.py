#!/usr/bin/env python3
"""p139-source-header-holder — `ACTION CJ`: do the SOURCE FILES name a holder the root
licence file does not?

    python3 -I scan_headers.py <clone-dir> <slug> <own-name>[,<own-name>...] [...]

Reads paths from `git ls-tree -r HEAD --name-only` and blobs from `git cat-file`, so
the working directory — and therefore `.git/hooks/*.sample`, which carries git's own
copyright and which an earlier draft of this probe published as a finding — is never
read at all.

Emits two TSVs on stdout, separated by a blank line: a per-row summary and a
per-holder detail table. Classification lives in `header_holder.py` and is tested.
"""
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import header_holder as hh  # noqa: E402

# Text extensions that carry source headers. Deliberately NOT a licence-filename
# pattern: p137 already enumerated licence FILES and found none outside these roots.
SOURCE_SUFFIXES = {
    ".py", ".js", ".mjs", ".cjs", ".ts", ".tsx", ".jsx", ".vue", ".php", ".java",
    ".rb", ".go", ".rs", ".c", ".h", ".cpp", ".cs", ".css", ".scss", ".less",
    ".sh", ".bash", ".xml", ".html", ".htm", ".sql", ".yml", ".yaml", ".toml",
    ".cfg", ".ini", ".txt", ".md", ".json",
}

MAX_BLOB_BYTES = 4_000_000   # a built front-end bundle can be large; cap the read
HEAD_WINDOW = 120            # a header lives at the top of a file, not in its body

# Licence FILES are p137's instrument, not this one, and reading them here mixes the
# two measurements: the AGPL body in `frappe/lms/license.txt` contains eight lines
# with the word "copyright" in them, and the first run of this probe reported five of
# them as foreign holders of the repository. `ACTION CJ` is about SOURCE headers.
LICENCE_FILENAME = re.compile(
    r"^(licen[cs]e|copying|notice|copyright)([._-][a-z0-9.+-]*)?$|\.licen[cs]e$",
    re.IGNORECASE,
)


def is_licence_file(path):
    return bool(LICENCE_FILENAME.match(Path(path).name))


def git(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args],
                          capture_output=True, text=True, errors="replace").stdout


def scan(repo, own_names):
    paths = [p for p in git(repo, "ls-tree", "-r", "HEAD", "--name-only").splitlines() if p]
    considered = 0
    licence_files = 0
    holders = {}          # holder -> {"class":..., "paths":[...], "count":n}
    for path in paths:
        if hh.is_vcs_artifact(path):      # cannot happen from ls-tree; asserted anyway
            continue
        if is_licence_file(path):
            licence_files += 1
            continue
        if Path(path).suffix.lower() not in SOURCE_SUFFIXES:
            continue
        considered += 1
        blob = git(repo, "show", f"HEAD:{path}")
        if not blob or len(blob) > MAX_BLOB_BYTES:
            # A bundle over the cap still gets its header window read.
            blob = blob[:MAX_BLOB_BYTES]
        for line in blob.splitlines()[:HEAD_WINDOW]:
            if "opyright" not in line:
                continue
            holder = hh.extract_holder(line)
            if holder is None:
                continue
            cls = hh.classify(holder, own_names)
            if hh.is_steward(holder):
                cls = "STEWARD"
            rec = holders.setdefault(holder, {"class": cls, "paths": [], "count": 0})
            rec["count"] += 1
            if len(rec["paths"]) < 3:
                rec["paths"].append(path)
    return len(paths), considered, licence_files, holders


def main(argv):
    if len(argv) < 4 or (len(argv) - 1) % 3 != 0:
        print(__doc__, file=sys.stderr)
        return 2
    summary, detail = [], []
    triples = [argv[i:i + 3] for i in range(1, len(argv), 3)]
    for clone, slug, own_csv in triples:
        own = [n.strip() for n in own_csv.split(",") if n.strip()]
        total, considered, licence_files, holders = scan(clone, own)
        foreign = {h: r for h, r in holders.items() if r["class"] == "FOREIGN"}
        steward = {h: r for h, r in holders.items() if r["class"] == "STEWARD"}
        own_h = {h: r for h, r in holders.items() if r["class"] == "OWN"}
        verdict = "FOREIGN_HEADER_IN_SOURCE" if foreign else (
            "OWN_HEADERS_ONLY" if own_h else "NO_HEADER_AT_ALL")
        summary.append("\t".join([
            slug, str(total), str(considered), str(licence_files), "|".join(own),
            str(len(own_h)), str(len(foreign)), str(len(steward)),
            str(sum(r["count"] for r in foreign.values())), verdict,
        ]))
        for holder, rec in sorted(holders.items(), key=lambda kv: -kv[1]["count"]):
            detail.append("\t".join([
                slug, holder, rec["class"], str(rec["count"]), ";".join(rec["paths"]),
            ]))

    print("slug\ttree_paths\tsource_paths_read\tlicence_files_skipped\town_names\town_holders\t"
          "foreign_holders\tsteward_holders\tforeign_header_lines\tverdict")
    print("\n".join(summary))
    print()
    print("slug\tholder\tclass\tlines\tsample_paths")
    print("\n".join(detail))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
