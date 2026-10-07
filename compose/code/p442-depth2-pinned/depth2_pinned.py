#!/usr/bin/env python3
"""p442 -- pass 25's action B: date the PINNED depth-2 tier.

The pre-registered action, verbatim:

    Date the **pinned** depth-2 tier, which this pass measured only at the latest
    release.
    Prediction: expect the depth-2 pinned median to exceed the depth-1 pinned median of
    220 d; if it does not, the staleness gradient stops at depth 1 and the closure can
    stop there for recency as well as for licence.

`p438` dropped the specifier on purpose -- it needed names, to ask a LICENCE question --
so its depth-2 figure (177 d median) dates each package's LATEST release.  That answers
"is this library maintained".  It does not answer "what lands on the disk", because a
depth-1 package pinning `foo==1.0` installs 1.0 however many releases have shipped since.

This instrument keeps the specifier.  Resolution, dating and specifier classification are
delegated to `../p437-pinned-version/pinned.py` and the age arithmetic to
`../registry-recency-channel`: rule 1 of P126 forbids re-deriving what the repository
already versions.  What is new here is only the EDGE SET -- (depth-1 package, its
declared specifier on a depth-2 package) -- which `p438` never emitted.

## The scope, restated because it bounds every figure

- **Runtime only.** A PEP 508 string carrying `extra == "..."` is optional, and npm
  `devDependencies`, `peerDependencies` and `optionalDependencies` likewise. Identical to
  `p438`'s scope, so the two tiers are comparable row-for-row.
- **Depth 2 means "required by a depth-1 package"**, not the transitive closure.
- ⚠️ **A depth-2 pin is a WEAKER claim than a depth-1 pin.** A depth-1 pin is in a
  manifest this KB has read. A depth-2 pin is the depth-1 PACKAGE's constraint on its own
  dependency, and a real solver resolves it jointly with every other package's constraint
  on the same name -- which can only move the chosen version DOWN. So these figures, like
  `p437`'s CAPPED rows, remain lower bounds on staleness.

TSV: parent, eco, dep, spec, spec_class, pinned_version, pinned_age,
     latest_version, latest_age, status
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
sys.path.insert(0, os.path.join(HERE, "..", "p437-pinned-version"))
sys.path.insert(0, os.path.join(HERE, "..", "p438-depth2-closure"))
from pinned import resolve  # noqa: E402

TIMEOUT = 30
# A PEP 508 requirement: name, optional [extras], then the specifier, then `; marker`.
_PEP508 = re.compile(r"^\s*([A-Za-z0-9][A-Za-z0-9._-]*)\s*(?:\[[^\]]*\])?\s*(.*)$")


def get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "globant-kb-p442"})
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
    """`extra == "..."` marks an OPTIONAL dependency; `pip install x` skips it."""
    marker = req.split(";", 1)[1] if ";" in req else ""
    return bool(re.search(r'\bextra\s*==', marker))


def runtime_edges(doc, eco):
    """[(dep_name, specifier)] for the LATEST release, runtime only.

    This is the one thing `p438` does not produce: it returns names, having discarded
    the specifier at the `_PEP508_NAME` match.  Without the specifier there is no pin
    to resolve, which is why the action could not simply re-read p438's TSV.
    """
    out = []
    if eco == "pypi":
        for req in (doc.get("info") or {}).get("requires_dist") or []:
            if is_extra_only(req):
                continue
            # Drop the environment marker before reading the specifier: the marker
            # contains quoted version numbers of its own (`python_version < "3.14"`)
            # and carrying it in made `3.14` resolve as a constraint on the package.
            body = req.split(";", 1)[0]
            m = _PEP508.match(body)
            if m:
                out.append((m.group(1).lower(), m.group(2).strip()))
        return out
    latest = ((doc.get("dist-tags") or {}).get("latest")) or ""
    ver = ((doc.get("versions") or {}).get(latest)) or {}
    return sorted((ver.get("dependencies") or {}).items())


def main():
    src, ref = sys.argv[1], dt.date.fromisoformat(sys.argv[2])
    depth1 = []
    for line in open(src):
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.rstrip("\n").split("\t")
        depth1.append((parts[0], parts[1]))
    if not depth1:
        sys.stderr.write("p442: empty denominator -- a path fault (P355)\n")
        sys.exit(2)
    d1names = {(n.lower(), e) for n, e in depth1}

    def expand(item):
        name, eco = item
        st, doc = get_json(doc_url(name, eco))
        if st != 200 or doc is None:
            return name, eco, []
        return name, eco, runtime_edges(doc, eco)

    edges = []
    with ThreadPoolExecutor(max_workers=12) as ex:
        for name, eco, pairs in ex.map(expand, depth1):
            for dep, spec in pairs:
                # A name already AT depth 1 is not a depth-2 row -- the same
                # subtraction `p438` performs, kept identical so the tiers compare.
                if (dep.lower(), eco) in d1names:
                    continue
                edges.append((name, eco, dep, spec))

    edges = sorted(set(edges))
    with ThreadPoolExecutor(max_workers=10) as ex:
        res = list(ex.map(lambda e: resolve(e[2], e[3], e[1], ref), edges))

    print("parent\teco\tdep\tspec\tspec_class\tpinned_version\tpinned_age\t"
          "latest_version\tlatest_age\tstatus")
    for (parent, eco, dep, spec), r in zip(edges, res):
        print("\t".join([parent, eco, dep, spec or "*", r[3], r[4], r[5], r[6], r[7],
                         r[8]]))


if __name__ == "__main__":
    main()
