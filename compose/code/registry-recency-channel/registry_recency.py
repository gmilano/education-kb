#!/usr/bin/env python3
"""registry-recency-channel — date the *installed* tier, not the citing tier.

`git-recency-channel` dates a repository this KB *cites* (head commit, via
`git fetch --depth 1`). It cannot date a dependency, because a dependency is a
**package name**, not a git URL. What a build installs is a *release*, so the
honest recency datum for the installed tier is the **upload date of the latest
release** in the registry that serves it.

That makes this a different instrument, not the same one pointed somewhere new,
and the two numbers are not interchangeable:

    citing tier   : head commit date      (any commit, including a typo fix)
    installed tier: latest release date   (a deliberate publication event)

A library can be committed daily and unreleased for two years; a library can be
released weekly from a repository with no commits in between (vendored builds).
Comparing the two populations is still informative, but it compares *commit
cadence* against *release cadence* and any claim built on it must say so.

Endpoints — both proven reachable from this environment (`api.github.com`,
`api.osv.dev`, `pypistats.org` and `api.npmjs.org` are 403 at the egress proxy):

    pypi.org/pypi/<name>/json      -> info.version + urls[].upload_time_iso_8601
    registry.npmjs.org/<name>      -> dist-tags.latest + time[<latest>]

Usage:
    python3 -I registry_recency.py <closure.tsv> [--ref YYYY-MM-DD] > recency.tsv

Output TSV: dep, ecosystem, latest_version, release_date, age_days, status.
status is OK | NOT-IN-REGISTRY | HTTP-<code> | NO-RELEASE-DATE | UNPARSEABLE.
NOT-IN-REGISTRY is not a defect on its own: see is_local_spec().
"""
import concurrent.futures as cf
import datetime as dt
import json
import sys
import urllib.parse
import urllib.request

TIMEOUT = 30

# Planted controls. Swept blind alongside the real names; every one of these
# MUST come back non-OK or the probe does not discriminate and the pass's
# negative results mean nothing. See README.
CONTROLS = [
    ("this-package-does-not-exist-xyz123-globant", "pypi"),
    ("@globant-kb/no-such-package-zzz999", "npm"),
    ("kolibri-oral-fluency-fake-probe-0000", "pypi"),
    ("moodle-mcp-nonexistent-control-4242", "npm"),
]


# A dependency whose *spec* is a path, a link or a git URL is never served by a
# registry, so a 404 for it is the registry answering correctly — not evidence
# that the package is missing. `CAHLR/OATutor` declares
# `"@common/global-config": "file:./common"`; reading its 404 as an absent
# package would have manufactured a supply-chain defect that does not exist.
LOCAL_SPEC_PREFIXES = ("file:", "link:", "workspace:", "portal:", "git+",
                       "git:", "github:", "http:", "https:", ".", "/")


def is_local_spec(spec):
    """True when a manifest spec resolves outside any package registry."""
    return str(spec or "").strip().lower().startswith(LOCAL_SPEC_PREFIXES)


def _get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "globant-kb-registry-recency"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except Exception as e:                      # noqa: BLE001 - the status IS the datum
        return getattr(e, "code", 0), ""


def pypi_release(doc):
    """(version, iso_date) for the latest release of a PyPI project."""
    ver = (doc.get("info") or {}).get("version") or ""
    stamps = [f.get("upload_time_iso_8601") for f in (doc.get("urls") or [])
              if f.get("upload_time_iso_8601")]
    if not stamps:                              # yanked/fileless latest: scan releases
        for files in (doc.get("releases") or {}).get(ver, []) or []:
            if files.get("upload_time_iso_8601"):
                stamps.append(files["upload_time_iso_8601"])
    return ver, (max(stamps) if stamps else "")


def npm_release(doc):
    """(version, iso_date) for the latest dist-tag of an npm package."""
    ver = ((doc.get("dist-tags") or {}).get("latest")) or ""
    times = doc.get("time") or {}
    return ver, (times.get(ver) or times.get("modified") or "")


def age_days(iso, ref):
    """Whole days between an ISO-8601 instant and the reference date."""
    if not iso:
        return ""
    try:
        d = dt.datetime.fromisoformat(iso.replace("Z", "+00:00")).date()
    except ValueError:
        return ""
    return (ref - d).days


def probe(item, ref):
    name, eco = item
    if eco == "npm":
        url = "https://registry.npmjs.org/%s" % urllib.parse.quote(name, safe="@/")
        parse = npm_release
    else:
        url = "https://pypi.org/pypi/%s/json" % urllib.parse.quote(name, safe="")
        parse = pypi_release
    st, body = _get(url)
    if st != 200:
        if st == 404:
            # Neutral wording on purpose: check the manifest spec with
            # is_local_spec() before reading this as a missing package.
            return (name, eco, "", "", "", "NOT-IN-REGISTRY")
        return (name, eco, "", "", "", "HTTP-%s" % st)
    try:
        ver, iso = parse(json.loads(body))
    except (ValueError, AttributeError):
        return (name, eco, "", "", "", "UNPARSEABLE")
    if not iso:
        return (name, eco, ver, "", "", "NO-RELEASE-DATE")
    return (name, eco, ver, iso, str(age_days(iso, ref)), "OK")


def ecosystem_of(manifest):
    """A manifest filename decides the registry that serves its dependencies."""
    return "npm" if manifest.endswith("package.json") else "pypi"


def read_closure(path):
    """Unique (dep, ecosystem) pairs from a dependency-licence-closure result."""
    seen, out = set(), []
    with open(path, encoding="utf-8") as fh:
        for i, line in enumerate(fh):
            if i == 0 or not line.strip():
                continue
            f = line.rstrip("\n").split("\t")
            if len(f) < 3 or f[2] == "-":
                continue
            key = (f[2], ecosystem_of(f[1]))
            if key not in seen:
                seen.add(key)
                out.append(key)
    return out


def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(__doc__, file=sys.stderr)
        return 2
    ref = dt.date.today()
    if "--ref" in argv:
        ref = dt.date.fromisoformat(argv[argv.index("--ref") + 1])
    items = read_closure(argv[1]) + CONTROLS
    print("\t".join(["dep", "ecosystem", "latest_version", "release_date",
                     "age_days", "status"]))
    with cf.ThreadPoolExecutor(max_workers=12) as ex:
        for row in ex.map(lambda it: probe(it, ref), items):
            print("\t".join(row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
