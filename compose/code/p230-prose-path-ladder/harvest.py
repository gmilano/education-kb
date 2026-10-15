#!/usr/bin/env python3
"""p230 — ACTION TD (the greedy slug) and ACTION TA (the prose path list).

Two harvests over the same shelves, sharing one scanner.

ACTION TD — THE DEFECT, stated exactly.  p228's harvester reads

    github\\.com/([A-Za-z0-9][A-Za-z0-9_-]*)/([A-Za-z0-9][A-Za-z0-9_.-]*?)(?=[)\\s`,.;:'"\\]]|$)

The repository name is LAZY and the terminator class CONTAINS `.`.  A lazy
quantifier stops at the first position where the lookahead can match, so
`processing/p5.js` is harvested as `processing/p5` — a slug that does not
exist.  p229 measured the cost: 31 dotted names mangled, 24 of them never in
p228's 520 at all, and 4 rows published as "missing repositories" that were
the harvester's own truncations.

The fix is two characters of intent: the name is GREEDY and the terminator
drops `.`.  A sentence-final period is then stripped in post, which is a
different operation from stopping at one.

ACTION TA — the probe list a pass must not invent.  p229 probed 40 paths from
a vocabulary it wrote down, and `moodle/moodle` — the most load-bearing row on
these shelves — sat in the grantless class because `COPYING.txt` was not in
it.  These shelves ALREADY RECORD the path at which each grant was read, in
the `channel` column and in prose.  Harvest THOSE.
"""
import re
import sys
from pathlib import Path

# ACTION TD: greedy name, terminator without `.`.
SLUG_RE = re.compile(
    r"github\.com/([A-Za-z0-9][A-Za-z0-9_-]*)/([A-Za-z0-9][A-Za-z0-9_.-]*)(?=[)\s`,;:'\"\]]|$)"
)

# ACTION TA: a path token as these shelves write one — backticked, optionally
# `ref/`-prefixed, ending in a licence-ish basename.  Deliberately NOT a
# vocabulary: the basename is matched by SHAPE, so a name no pass has thought
# of is harvested the first time somebody writes it down.
PATH_RE = re.compile(
    r"`([A-Za-z0-9][A-Za-z0-9_./-]{0,80}?"
    r"(?:LICEN[CS]E|licen[cs]e|Licen[cs]e|COPYING|copying|Copying|NOTICE|notice|Notice)"
    r"[A-Za-z0-9_.-]{0,12})`"
)

SHELVES = ["agents", "repos", "verticals", "intel", "compose/patterns.md"]


def md_files(root: Path):
    for s in SHELVES:
        p = root / s
        if p.is_file():
            yield p
        elif p.is_dir():
            yield from sorted(p.glob("*.md"))


def slugs_on(line):
    """Every github slug on one line, p228's semantics plus ACTION TD's fix."""
    out = []
    for m in SLUG_RE.finditer(line):
        owner, repo = m.group(1), m.group(2)
        if "." in owner:          # T224-2: a dotted owner is a hostname
            continue
        repo = repo.rstrip(".")   # sentence-final period, stripped not stopped at
        if repo.endswith(".git"):
            # T230-1: a clone URL carries a `.git` suffix the repository name does not.
            # Greedy matching makes this visible for the first time; the lazy regex hid it
            # by truncating before it. Found in this instrument's own first output.
            repo = repo[:-4]
        if not repo or repo in {"md", "txt"}:
            continue
        if repo.endswith(".md") or repo.endswith(".txt"):
            # a documentation path that happens to sit under a slug-shaped URL
            repo = repo.rsplit(".", 1)[0]
            if not repo:
                continue
        out.append(f"{owner}/{repo}")
    seen, uniq = set(), []
    for s in out:
        if s not in seen:
            seen.add(s)
            uniq.append(s)
    return uniq


def paths_on(line, known_slugs=frozenset()):
    out = []
    for m in PATH_RE.finditer(line):
        tok = m.group(1).strip("/")
        if not tok or tok.count("/") > 3:
            continue
        # a ref prefix (`main/`, `master/`) is carried by the probe, not the path
        parts = tok.split("/")
        if parts[0] in {"main", "master", "develop", "trunk", "HEAD"} and len(parts) > 1:
            tok = "/".join(parts[1:])
            parts = tok.split("/")
        base = parts[-1]
        # T230-2: the shape that finds a licence FILE also finds instruments
        # (`lib/license_family.sh`, `p147-licence-language`), predicates
        # (`is_licence_path`), status tokens (`NO_LICENCE_FILE`) and a repository
        # (`spdx/license-list-data`). Each would be probed as a path and 404 forever.
        # A probe-list entry must be a path whose BASENAME NAMES THE GRANT and
        # nothing else, so: the basename starts with the licence word, carries no
        # code extension, and no segment is an instrument directory.
        if not re.match(r"(?i)^(licen[cs]e|copying|notice)\b", base):
            continue
        if re.search(r"(?i)\.(sh|py|js|ts|rb|php|json|ya?ml|lock|toml)$", base):
            continue
        if any(re.match(r"^p\d+-", seg) or seg in {"lib", "compose", "code"} for seg in parts):
            continue
        if re.search(r"(?i)[_-](file|path|payload|census|language|gate|audit)\b", base):
            continue
        if "." in parts[0] and len(parts) > 1:
            # T230-3: a hostname-first token is a URL, not a repository path
            # (`apache.org/licenses/LICENSE-2.0.txt`). Third defect in this
            # instrument's own output, found before publishing.
            continue
        if tok in known_slugs:
            # T230-4: a probe path that is ALSO a slug on these shelves is a
            # REPOSITORY (`spdx/license-list-data`). The cross-filter is the
            # cheapest discriminator available and needs no vocabulary.
            continue
        if tok:
            out.append(tok)
    return out


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    what = sys.argv[2] if len(sys.argv) > 2 else "slugs"
    slugs, paths = {}, {}
    known_slugs = set()
    for f in md_files(root):
        for line in f.read_text(encoding="utf-8").splitlines():
            known_slugs.update(slugs_on(line))
    for f in md_files(root):
        for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            for s in slugs_on(line):
                slugs.setdefault(s, []).append(f"{f.name}:{n}")
            for p in paths_on(line, known_slugs):
                paths.setdefault(p, []).append(f"{f.name}:{n}")
    if what == "slugs":
        for s in sorted(slugs):
            print(f"{s}\t{len(slugs[s])}\t{slugs[s][0]}")
    else:
        # T230-5: these shelves often write the FULL raw path, slug and ref included
        # (`moodle/moodle/main/COPYING.txt`). The probe list wants the part AFTER the
        # ref, since the probe supplies slug and ref itself. Fifth defect found in
        # this instrument's own output before publishing.
        norm = {}
        for tok, hits in paths.items():
            segs = tok.split("/")
            while len(segs) > 2 and f"{segs[0]}/{segs[1]}" in known_slugs:
                segs = segs[2:]
                if segs and (segs[0] in {"main", "master", "HEAD", "develop"}
                             or segs[0].startswith("nonexistent-")):
                    segs = segs[1:]
            key = "/".join(segs)
            if key:
                norm.setdefault(key, []).extend(hits)
        for p in sorted(norm, key=lambda k: (-len(norm[k]), k)):
            print(f"{p}\t{len(norm[p])}\t{norm[p][0]}")


if __name__ == "__main__":
    main()
