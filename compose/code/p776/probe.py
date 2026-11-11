#!/usr/bin/env python3
"""p776 prober -- written from scratch (execution of repo-held code is denied).

Channels, re-measured this pass:
  ref  https://github.com/{o}/{r}/info/refs?service=git-upload-pack  -> 200
  raw  https://raw.githubusercontent.com/{o}/{r}/{b}/{name}          -> 200
  api.github.com / github.com HTML / codeload                        -> 403

So: existence + default branch + HEAD sha come off the ref channel; grant bytes
+ sha256_12 come off the raw channel. No star count is emitted: its channel is 403.
"""
import hashlib, json, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

GRANT_NAMES = []
for stem in ("LICENSE", "LICENCE", "License", "Licence", "license", "licence"):
    for ext in ("", ".md", ".txt", ".rst"):
        GRANT_NAMES.append(stem + ext)
GRANT_NAMES += [
    "COPYING", "COPYING.txt", "COPYING.md", "copying", "Copying",
    "COPYING.LESSER", "COPYRIGHT", "COPYRIGHT.txt",
    "LICENSE-MIT", "LICENSE-APACHE", "MIT-LICENSE", "MIT-LICENSE.txt",
    "UNLICENSE", "LICENSE.LGPL", "LICENSE.GPL", "NOTICE",
    "LICENSE-2.0.txt", "LICENSE.docx", "LICENSE.rtf", "LICENSE.fandoc",
]
_s = set()
GRANT_NAMES = [n for n in GRANT_NAMES if not (n in _s or _s.add(n))]

SYMREF = re.compile(r"symref=HEAD:refs/heads/([^\s\x00]+)")
HEADSHA = re.compile(r"([0-9a-f]{40}) HEAD[\s\x00]")


def curl(url, max_bytes=600000, timeout=35):
    cmd = ["curl", "-sS", "-L", "--max-time", str(timeout),
           "-w", "\n__HTTP__%{http_code}", url]
    try:
        p = subprocess.run(cmd, capture_output=True, timeout=timeout + 25)
    except subprocess.TimeoutExpired:
        return None, "TIMEOUT"
    out = p.stdout
    i = out.rfind(b"\n__HTTP__")
    if i < 0:
        return None, "NO-CODE"
    code = out[i + 9:].decode("ascii", "replace").strip()
    return out[:i][:max_bytes], code


def ref_probe(owner, repo):
    body, code = curl(f"https://github.com/{owner}/{repo}/info/refs?service=git-upload-pack")
    if code != "200" or not body:
        return {"exists": False, "http": code, "branch": None, "head": None}
    t = body.decode("utf-8", "replace")
    m, h = SYMREF.search(t), HEADSHA.search(t)
    branch = m.group(1) if m else None
    if branch is None:                      # no symref advertised: fall back
        for cand in ("main", "master"):
            if f"refs/heads/{cand}" in t:
                branch = cand
                break
    return {"exists": True, "http": code, "branch": branch,
            "head": (h.group(1)[:12] if h else None)}


def grant_probe(owner, repo, branch):
    """Try every case-aware grant name at the tree root. Returns first hit + all hits."""
    hits = []
    for name in GRANT_NAMES:
        body, code = curl(
            f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{name}")
        if code == "200" and body is not None and body.strip():
            hits.append({
                "name": name,
                "bytes": len(body),
                "sha256_12": hashlib.sha256(body).hexdigest()[:12],
            })
    return hits


def probe(slug):
    owner, _, repo = slug.partition("/")
    r = {"slug": slug}
    r.update(ref_probe(owner, repo))
    if not r["exists"] or not r["branch"]:
        r["grants"] = []
        r["verdict"] = "ABSENT-OR-PRIVATE" if not r["exists"] else "NO-DEFAULT-BRANCH"
        return r
    hits = grant_probe(owner, repo, r["branch"])
    r["grants"] = hits
    r["verdict"] = "GRANT-FOUND" if hits else f"NO-GRANT-AT-ROOT after {len(GRANT_NAMES)} names"
    return r


if __name__ == "__main__":
    slugs = [l.strip() for l in sys.stdin if l.strip() and not l.startswith("#")]
    with ThreadPoolExecutor(max_workers=6) as ex:
        for r in ex.map(probe, slugs):
            print(json.dumps(r), flush=True)
