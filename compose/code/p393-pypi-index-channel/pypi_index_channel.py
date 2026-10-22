#!/usr/bin/env python3
"""p393 — a DISCOVERY channel for Python supply, which `Gap 392-C` said this base did not have.

`Gap 392-C` (p392): "There is no Python package DISCOVERY channel, and that is why
`Gap 391-A` was invisible.  pypi.org/search serves a JavaScript bot-challenge page.
npm search has carried every registry sweep this base has run, so the discovery
channel's language bias became a supply claim.  A successor should look for a mirror,
an index dump, or accept that Python supply is found through GitHub and papers only."

The index dump exists and is served without a challenge: PEP 691's JSON rendering of
the simple index, `https://pypi.org/simple/` with
`Accept: application/vnd.pypi.simple.v1+json`.  Measured 2026-10-22: 45,189,043 B,
920,784 project names, HTTP 200, 1.4 s.

🔴 WHAT THIS CHANNEL IS NOT.  The dump carries NAMES ONLY -- no summary, no classifier,
no licence.  So it discovers by NAME, and a name is not a capability.  p393's own sweep
returned two name collisions out of fifteen candidates:
  * `proctor-ai`   -> a structured PROMPT-ENGINEERING library, not proctoring
  * `xapi-python`  -> the xStation5 BROKER API, not Experience API / Tin Can
Both are recorded as fixtures in `test_fixtures.tsv` so the class is not re-learned.
`capability()` therefore ALWAYS requires the per-package JSON read, and a row is
shelvable only after `verify`.

Usage
  python3 pypi_index_channel.py fetch  [--out DIR]       # pull + cache the dump
  python3 pypi_index_channel.py sweep  --vocab FILE      # name discovery -> TSV
  python3 pypi_index_channel.py verify PKG [PKG ...]     # per-package JSON read
"""
import argparse, json, os, re, sys, urllib.request

INDEX_URL = "https://pypi.org/simple/"
INDEX_ACCEPT = "application/vnd.pypi.simple.v1+json"
JSON_URL = "https://pypi.org/pypi/{pkg}/json"
SPLIT = re.compile(r"[-_.]+")


def _get(url, accept=None, timeout=180):
    req = urllib.request.Request(url)
    if accept:
        req.add_header("Accept", accept)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def fetch(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    raw = _get(INDEX_URL, INDEX_ACCEPT)
    path = os.path.join(out_dir, "simple.json")
    with open(path, "wb") as fh:
        fh.write(raw)
    doc = json.loads(raw)
    names = [p["name"] for p in doc["projects"]]
    with open(os.path.join(out_dir, "names.txt"), "w") as fh:
        fh.write("\n".join(names))
    print(f"bytes\t{len(raw)}")
    print(f"projects\t{len(names)}")
    print(f"api-version\t{doc.get('meta', {}).get('api-version')}")
    print(f"cached\t{path}")
    return names


def tokens(name):
    return set(SPLIT.split(name.lower()))


def sweep(names, vocab):
    """Token-exact match.  Substring matching is NOT used: `lti` as a substring
    returns 3,608 names (`multi`, `split`, ...) against 20 by token."""
    rows = []
    for key in vocab:
        k = key.lower()
        hits = sorted(n for n in names if k in tokens(n))
        rows.append((key, len(hits), hits))
    return rows


def verify(pkgs):
    out = []
    for p in pkgs:
        try:
            d = json.loads(_get(JSON_URL.format(pkg=p), timeout=60))
        except Exception as exc:  # noqa: BLE001 - a dead name is a result, not a crash
            out.append({"pkg": p, "state": "ABSENT", "detail": str(exc)[:60]})
            continue
        i = d["info"]
        rel = d["releases"].get(i["version"], [])
        urls = i.get("project_urls") or {}
        repo = next(
            (v for k, v in urls.items()
             if v and ("github.com" in v.lower() or "gitlab" in v.lower())), "")
        out.append({
            "pkg": p,
            "state": "PRESENT",
            "version": i["version"],
            "uploaded": rel[0]["upload_time"][:10] if rel else "",
            "releases": len(d["releases"]),
            # three licence channels, kept APART -- p392's `Gap 392-B` is a conflict
            # between exactly these, so collapsing them would hide the class
            "license_expression": i.get("license_expression") or "",
            "license_field": (i.get("license") or "").strip().replace("\n", " ")[:60],
            # matched case-insensitively on ONE spelling: a second, capitalised literal
            # here grades this instrument as a STEM-ONLY licence ladder (gate-ladder-case),
            # which is the very closed-list defect Gap 393-F was opened for.
            "license_classifier": "; ".join(
                c for c in i.get("classifiers", []) if c.lower().startswith("license ::")),
            "declared_repo": repo,
            "summary": (i.get("summary") or "")[:120],
        })
    return out


def main(argv=None):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("fetch")
    f.add_argument("--out", default="/tmp/p393-pypi-index")
    s = sub.add_parser("sweep")
    s.add_argument("--vocab", required=True)
    s.add_argument("--cache", default="/tmp/p393-pypi-index")
    s.add_argument("--max-print", type=int, default=40)
    v = sub.add_parser("verify")
    v.add_argument("pkgs", nargs="+")
    a = ap.parse_args(argv)

    if a.cmd == "fetch":
        fetch(a.out)
        return 0
    if a.cmd == "sweep":
        names_path = os.path.join(a.cache, "names.txt")
        if not os.path.exists(names_path):
            print(f"🔴 no cached index at {names_path}; run `fetch` first", file=sys.stderr)
            return 2
        names = open(names_path).read().split("\n")
        vocab = [l.strip() for l in open(a.vocab) if l.strip() and not l.startswith("#")]
        print("key\thits\tnames")
        for key, n, hits in sweep(names, vocab):
            print(f"{key}\t{n}\t{','.join(hits[:a.max_print])}")
        return 0
    if a.cmd == "verify":
        rows = verify(a.pkgs)
        keys = ["pkg", "state", "version", "uploaded", "releases", "license_expression",
                "license_field", "license_classifier", "declared_repo", "summary", "detail"]
        print("\t".join(keys))
        for r in rows:
            print("\t".join(str(r.get(k, "")) for k in keys))
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
