#!/usr/bin/env python3
"""p438 — the SECOND level of the dependency closure, licensed and dated.

Pass 24's action B, pre-registered with its prediction:

    "Extend the closure to depth 2 and date it, the hypothesis the closure's own
     README pre-registered.  Expect the copyleft COUNT to rise via `certifi`
     (MPL-2.0) but NO NEW COPYLEFT CLASS; if no new class appears, depth 1 was
     sufficient and the gap closes."

Depth 1 reads the manifests this KB's targets commit.  Depth 2 reads what those
dependencies themselves require, from the registry's own metadata -- the same
two endpoints, no new channel:

    pypi.org/pypi/<n>/json     -> info.requires_dist   (PEP 508 strings)
    registry.npmjs.org/<n>     -> versions[latest].dependencies

Scope, stated because it bounds every figure here:

  * RUNTIME dependencies only.  A PEP 508 string carrying `extra == "..."` is an
    OPTIONAL dependency and is NOT installed by a plain `pip install <pkg>`;
    counting it would inflate the closure with packages no build pulls.  npm
    `devDependencies` are excluded for the same reason and `peerDependencies`
    because the consumer, not the package, decides them.
  * Environment markers other than `extra` (`python_version`, `sys_platform`)
    are KEPT: they are installed on some platforms, and a licence obligation
    that only binds on Windows is still a licence obligation.
  * Depth 2 means "required by a depth-1 package", not the transitive closure.
    Depth 3 is not measured and nothing here is a statement about it.

Reuses `dependency-licence-closure/dep_licence.py` for classification and
`registry-recency-channel/registry_recency.py` for dating: P126 rule 1 forbids
re-deriving what the repository already versions.

Usage: python3 -I depth2.py <depth1-names.tsv> <YYYY-MM-DD> > depth2.tsv
  where depth1-names.tsv is `name<TAB>ecosystem`, one per line.
TSV out: parent, eco, dep, licence_raw, field, class, version, release_date, age_days, status
"""
import datetime as dt
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "dependency-licence-closure"))
sys.path.insert(0, os.path.join(HERE, "..", "registry-recency-channel"))
from dep_licence import classify_licence, npm_licence, pypi_licence   # noqa: E402
from registry_recency import age_days, npm_release, pypi_release      # noqa: E402

TIMEOUT = 30
_PEP508_NAME = re.compile(r"^\s*([A-Za-z0-9][A-Za-z0-9._-]*)")


def get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "globant-kb-p438"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.status, json.loads(r.read().decode("utf-8", "replace"))
    except Exception as e:                      # noqa: BLE001 - the status IS the datum
        return getattr(e, "code", 0), None


def doc_url(name, eco):
    if eco == "npm":
        return "https://registry.npmjs.org/%s" % urllib.parse.quote(name, safe="@/")
    return "https://pypi.org/pypi/%s/json" % urllib.parse.quote(name, safe="")


def is_extra_only(req):
    """True when a PEP 508 requirement is gated behind `extra == "..."`.

    These are the OPTIONAL dependencies.  `pip install requests` does not install
    them; `pip install requests[socks]` does.  Including them would make the
    closure describe an installation nobody performs.
    """
    marker = req.split(";", 1)[1] if ";" in req else ""
    return bool(re.search(r'\bextra\s*==', marker))


def runtime_deps(name, eco, doc):
    if eco == "pypi":
        out = []
        for req in (doc.get("info") or {}).get("requires_dist") or []:
            if is_extra_only(req):
                continue
            m = _PEP508_NAME.match(req)
            if m:
                out.append(m.group(1).lower())
        return sorted(set(out))
    latest = ((doc.get("dist-tags") or {}).get("latest")) or ""
    ver = ((doc.get("versions") or {}).get(latest)) or {}
    return sorted((ver.get("dependencies") or {}).keys())


def describe(name, eco, ref):
    """(licence_raw, field, class, version, date, age, status) for one package."""
    st, doc = get_json(doc_url(name, eco))
    if st != 200 or doc is None:
        return ("", "", "UNKNOWN", "", "", "",
                "NOT-IN-REGISTRY" if st == 404 else "HTTP-%s" % st), []
    raw, field = (pypi_licence(doc) if eco == "pypi" else npm_licence(doc))
    ver, iso = (pypi_release(doc) if eco == "pypi" else npm_release(doc))
    return ((str(raw) if raw is not None else ""), field, classify_licence(raw),
            ver, (iso or "")[:10], str(age_days(iso, ref)) if iso else "", "OK"), \
        runtime_deps(name, eco, doc)


def main():
    src, ref = sys.argv[1], dt.date.fromisoformat(sys.argv[2])
    depth1 = []
    for line in open(src):
        if not line.strip() or line.startswith("#"):
            continue
        n, eco = line.rstrip("\n").split("\t")[:2]
        depth1.append((n, eco))
    d1 = set(depth1)

    # Level 1 expansion: what does each depth-1 package require?
    def expand(item):
        n, eco = item
        _, deps = describe(n, eco, ref)
        return n, eco, deps
    edges = []
    with ThreadPoolExecutor(max_workers=12) as ex:
        for n, eco, deps in ex.map(expand, depth1):
            for d in deps:
                edges.append((n, eco, d))

    # Level 2 description: the NEW names only.
    new = sorted({(d, eco) for _, eco, d in edges} - {(n, e) for n, e in d1})
    info = {}
    with ThreadPoolExecutor(max_workers=12) as ex:
        for (n, eco), res in zip(new, ex.map(lambda x: describe(x[0], x[1], ref)[0], new)):
            info[(n, eco)] = res

    print("parent\teco\tdep\tlicence_raw\tfield\tclass\tversion\trelease_date\tage_days\tstatus")
    for parent, eco, dep in sorted(set(edges)):
        if (dep, eco) in d1:
            continue
        r = info.get((dep, eco))
        if not r:
            continue
        # Some projects dump their entire licence TEXT into the `license` field,
        # newlines and all, which splits a TSV row.  Collapse all whitespace.
        print("\t".join([parent, eco, dep, " ".join(r[0].split())[:120],
                         r[1], r[2], r[3], r[4], r[5], r[6]]))


if __name__ == "__main__":
    main()
