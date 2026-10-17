#!/usr/bin/env python3
"""`ACTION ZE`'s ONLINE half: run the ladder that EXISTS over the rows that have no
grant, and record `tier_coverage()` per `(path, row)`.

Not in `make hooks` — it needs network.  The offline controls that hold its predicates
live in `test_current_state.py`, which is.

Per row, in this order, and never more:
  1. `git ls-remote --symref <url> HEAD`  — the REAL default branch and its SHA.  A ref
     is never guessed; `p229` established that a wrong ref answers `404` at every path
     and is indistinguishable from a grantless repository.
  2. `git clone --filter=blob:none --no-checkout --depth 1` — the repository's OWN tree.
     The ladder is then intersected with the tree, so a path that is ABSENT is known to
     be absent from the tree and not merely 404 at one attempt (`p259`'s rule).
  3. one payload fetch per ladder path the tree ACTUALLY CONTAINS, on the resolved ref.

usage: tier_run.py <population-file> <out.tsv>
"""
import concurrent.futures as cf
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "pass260-ecosystem-manifest-tier"))
import current_state as cs                      # noqa: E402
import manifest_tier as mt                      # noqa: E402

TIERS = cs.ladder_tiers()
LADDER = [(t, p) for t in ("TIER_A", "TIER_B", "TIER_C") for p in TIERS.get(t, ())]
MANIFEST_ECO = {"composer.json": "COMPOSER", "package.json": "NPM",
                "pyproject.toml": "PYPROJECT", "setup.py": "SETUPPY",
                "pom.xml": "MAVEN", "version.php": "MOODLE",
                "DESCRIPTION": "R-CRAN", "__manifest__.py": "ODOO",
                "Cargo.toml": "CARGO", "pubspec.yaml": "PUBSPEC",
                "setup.cfg": "SETUPCFG"}
HEADERS = ("slug", "ref", "head_sha", "tier", "path", "coverage", "bytes", "payload_sha16",
           "read_by", "token", "family", "note")


def run(cmd, timeout=180, cwd=None):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, cwd=cwd,
                           env={**os.environ, "GIT_TERMINAL_PROMPT": "0",
                                "GIT_ASKPASS": "/bin/true"})
        return r.returncode, r.stdout, r.stderr
    except subprocess.TimeoutExpired:
        return 124, "", "TIMEOUT"


def url_of(slug):
    host, path = slug.split(":", 1)
    return f"https://{host}/{path}", host, path


def raw_url(host, path, ref, filepath):
    if host == "github.com":
        return f"https://raw.githubusercontent.com/{path}/{ref}/{filepath}"
    return f"https://gitlab.com/{path}/-/raw/{ref}/{filepath}"


def resolve_ref(url):
    rc, out, _ = run(["git", "ls-remote", "--symref", url, "HEAD"], timeout=120)
    if rc != 0:
        return None, None
    ref, sha = None, None
    for line in out.splitlines():
        m = re.match(r"ref:\s+refs/heads/(\S+)\s+HEAD", line)
        if m:
            ref = m.group(1)
        m = re.match(r"([0-9a-f]{40})\s+HEAD", line)
        if m:
            sha = m.group(1)
    return ref, sha


def tree_of(url):
    tmp = tempfile.mkdtemp(prefix="p261-")
    try:
        rc, _, err = run(["git", "clone", "--filter=blob:none", "--no-checkout",
                          "--depth", "1", url, tmp + "/r"], timeout=480)
        if rc != 0:
            return None, err.strip().splitlines()[-1] if err.strip() else "CLONE-FAILED"
        rc, out, _ = run(["git", "-C", tmp + "/r", "ls-tree", "-r", "--name-only", "HEAD"],
                         timeout=180)
        if rc != 0:
            return None, "LS-TREE-FAILED"
        return out.splitlines(), ""
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def fetch(url):
    rc, out, _ = run(["curl", "-sS", "-L", "--max-time", "60", "-w", "\n%{http_code}", url],
                     timeout=90)
    if rc != 0:
        return None, "FETCH-FAILED"
    parts = out.rsplit("\n", 1)
    if len(parts) != 2:
        return None, "NO-STATUS"
    body, code = parts
    return (body, code) if code == "200" else (None, code)


def grade(tier, path, body):
    """(read_by, token, family, note).  Tier A/B are PAYLOADS and go to the shared
    classifier; Tier C is a DECLARATION and goes to its ecosystem's reader.  The two
    must not be swapped — `p247`'s `ACTION XC`, and `graduable_as_licence` is the
    predicate that says so."""
    base = os.path.basename(path)
    if tier == "TIER_C":
        eco = MANIFEST_ECO.get(base)
        if eco is None:
            return "NO-READER", "", "", f"tier-c path with no ecosystem: {base}"
        if mt.is_generated(body):
            return eco, "", "", "GENERATED-MANIFEST: fields never substituted"
        token, read_by = mt.read_declaration(eco, path, body)
        if token is None:
            return f"{eco}:{read_by}", "", "", read_by
        verdict, resolved = mt.manifest_verdict(token)
        return f"{eco}:{read_by}", token, (resolved or ""), verdict
    if mt.is_foreign(path):
        return "GUARD", "", "", "FOREIGN: a third party's grant"
    res = mt.reservation_verdict(body)
    fam = cs.family_of(body)
    note = "" if res != "RESERVED" else "RESERVED: no permissive grant follows"
    if res == "BOILERPLATE":
        note = "ALL-RIGHTS-RESERVED is BSD/MIT boilerplate, not a retraction"
    return "lib/license_family.sh", "", fam, note


def one(slug):
    rows = []
    url, host, path = url_of(slug)
    ref, sha = resolve_ref(url)
    if not ref:
        rows.append([slug, "", "", "", "", "NO-REF", "", "", "", "", "", "ls-remote found no HEAD"])
        return rows
    tree, err = tree_of(url)
    if tree is None:
        rows.append([slug, ref, sha or "", "", "", "NO-TREE", "", "", "", "", "", err])
        return rows
    tset = set(tree)
    for tier, p in LADDER:
        if p not in tset:
            continue
        body, code = fetch(raw_url(host, path, ref, p))
        if body is None:
            rows.append([slug, ref, sha or "", tier, p, "IN-TREE-UNFETCHED", "", "",
                         "", "", "", f"http {code}"])
            continue
        read_by, token, fam, note = grade(tier, p, body)
        rows.append([slug, ref, sha or "", tier, p, "RUN", str(len(body.encode())),
                     hashlib.sha256(body.encode()).hexdigest()[:16],
                     read_by, token, fam, note])
    if not any(r[5] == "RUN" for r in rows):
        rows.append([slug, ref, sha or "", "", "", "NO-LADDER-PATH-IN-TREE", "", "", "",
                     "", "", f"{len(tset)} paths in tree, none on the ladder"])
    return rows


def main(argv):
    pop = [l.strip() for l in open(argv[1]) if l.strip()]
    out = []
    with cf.ThreadPoolExecutor(max_workers=6) as ex:
        for rows in ex.map(one, pop):
            out.extend(rows)
            print(f"\r{len(out)} rows", end="", file=sys.stderr, flush=True)
    with open(argv[2], "w", encoding="utf-8") as fh:
        fh.write("\t".join(HEADERS) + "\n")
        for r in out:
            fh.write("\t".join(x.replace("\t", " ").replace("\n", " ") for x in r) + "\n")
    print(f"\nwrote {len(out)} rows to {argv[2]}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
