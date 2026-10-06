#!/usr/bin/env python3
"""Network half: fetch a manifest, resolve each direct dependency's licence.

  python3 resolve.py targets.tsv > result.tsv

targets.tsv columns: slug <TAB> ref <TAB> manifest <TAB> ecosystem(pypi|npm)

Reads only endpoints proven reachable from this environment:
  raw.githubusercontent.com  (manifest)     -> 200
  pypi.org/pypi/<n>/json     (dep licence)  -> 200
  registry.npmjs.org/<n>     (dep licence)  -> 200
api.github.com, api.osv.dev, pypistats.org and api.npmjs.org are NOT reachable
(403 at the egress proxy); no code path depends on them.
"""
import json
import os
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dep_licence import (classify_licence, pypi_licence, npm_licence,
                         parse_requirements, parse_pyproject,
                         parse_package_json, parse_dependency_group, verdict)

TIMEOUT = 30
_CACHE = {}


def get(url):
    if url in _CACHE:
        return _CACHE[url]
    req = urllib.request.Request(url, headers={"User-Agent": "globant-kb-dep-audit"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            body = r.read().decode("utf-8", "replace")
            out = (r.status, body)
    except Exception as e:                       # noqa: BLE001 - status is the datum
        code = getattr(e, "code", 0)
        out = (code, "")
    _CACHE[url] = out
    return out


def dep_licence(name, eco):
    if eco == "pypi":
        st, body = get("https://pypi.org/pypi/%s/json" % name)
        if st != 200:
            return None, "http-%s" % st
        try:
            return pypi_licence(json.loads(body))
        except ValueError:
            return None, "unparseable"
    st, body = get("https://registry.npmjs.org/%s" % name)
    if st != 200:
        return None, "http-%s" % st
    try:
        return npm_licence(json.loads(body))
    except ValueError:
        return None, "unparseable"


PARSERS = {"pyproject.toml": parse_pyproject,
           "requirements.txt": parse_requirements,
           "package.json": parse_package_json}


def main(path):
    rows = []
    print("\t".join(["slug", "manifest", "dep", "licence_raw", "field", "class"]))
    for line in open(path):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        slug, ref, manifest, eco = line.split("\t")[:4]
        # "pyproject.toml#base" means: read the PEP 735 dependency group "base"
        # instead of [project].dependencies. See parse_dependency_group.
        path, _, group = manifest.partition("#")
        st, body = get("https://raw.githubusercontent.com/%s/%s/%s" % (slug, ref, path))
        if st != 200:
            print("\t".join([slug, manifest, "-", "-", "manifest-http-%s" % st, "NO-MANIFEST"]))
            continue
        if group:
            deps = parse_dependency_group(body, group)
        else:
            deps = PARSERS[os.path.basename(path)](body)
        if not deps:
            print("\t".join([slug, manifest, "-", "-", "parsed-zero", "NO-DEPS"]))
            continue
        classes = []
        for d in deps:
            raw, field = dep_licence(d, eco)
            cls = classify_licence(raw)
            classes.append(cls)
            flat = (str(raw).replace("\t", " ").replace("\n", " ")[:60]
                    if raw is not None else "")
            print("\t".join([slug, manifest, d, flat, field, cls]))
        rows.append((slug, manifest, len(deps), verdict("PERMISSIVE", classes)))
    sys.stderr.write("\n== verdicts ==\n")
    for slug, manifest, n, v in rows:
        sys.stderr.write("%-46s %-16s %3d deps  %s\n" % (slug, manifest, n, v))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "targets.tsv")
