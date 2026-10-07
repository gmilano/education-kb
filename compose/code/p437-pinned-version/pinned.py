#!/usr/bin/env python3
"""p437 — date the version a build actually INSTALLS, not the latest one published.

Pass 24 dated the installed tier with `registry-recency-channel`, which reads the
**latest** release of each dependency, and published the limit with the figures:

    "A manifest pinning `foo==1.0` is older than reported, never newer, so every
     age here is a LOWER BOUND on staleness."

Action C of pass 24 pre-registered the fix. This is it: resolve each manifest's
**version specifier** against the registry's release list, take the highest
release that satisfies it -- which is what pip and npm install -- and date THAT.

Pure functions below the fetch layer, so the resolver is testable offline.

Specifier classes, because the answer differs by class and the class is the finding:

    EXACT    `==1.2.3`, `1.2.3`            -> the pinned release, whatever its age
    CAPPED   `~=1.2`, `^1.2.3`, `<2`, `~1` -> highest release under the cap
    FLOOR    `>=1.2`, `>1.2`               -> the latest release; age equals pass 24's
    ANY      `*`, no specifier             -> the latest release; age equals pass 24's

Only EXACT and CAPPED can move a number. A corpus that is mostly FLOOR/ANY cannot
show the effect the action predicted, and saying so is part of the result.
"""
import json, re, sys, urllib.request, urllib.error
import datetime as dt
from concurrent.futures import ThreadPoolExecutor

TIMEOUT = 30
RAW = "https://raw.githubusercontent.com/{slug}/{ref}/{path}"


# ---------------------------------------------------------------- versions

_NUM = re.compile(r"\d+")


def vkey(v):
    """A comparable key for a version string. Pre-releases sort BELOW the release.

    Deliberately not a full PEP 440 / semver implementation. It compares the
    numeric release segments and demotes anything carrying a pre-release marker,
    which is the only distinction this instrument needs: installers do not pick a
    pre-release unless asked, and every candidate here comes from the registry's
    own list.
    """
    pre = bool(re.search(r"(a|b|rc|alpha|beta|dev|pre)\d*$|[-+]", v or ""))
    nums = [int(x) for x in _NUM.findall(v or "")][:5]
    nums += [0] * (5 - len(nums))
    return (tuple(nums), 0 if pre else 1)


def is_prerelease(v):
    return bool(re.search(r"(a|b|rc|alpha|beta|dev|pre)\d*$", v or "")) or "-" in (v or "")


def _cmp(a, b):
    ka, kb = vkey(a), vkey(b)
    return (ka > kb) - (ka < kb)


def satisfies_py(version, spec):
    """PEP 440-lite: comma-separated comparator clauses, all must hold."""
    for clause in (spec or "").split(","):
        clause = clause.strip()
        if not clause or clause == "*":
            continue
        m = re.match(r"(===|==|!=|>=|<=|~=|>|<)?\s*(.+)$", clause)
        if not m:
            return False
        op, want = m.group(1) or "==", m.group(2).strip()
        if want.endswith(".*"):
            base = want[:-2]
            if op in ("==", "==="):
                if not (version == base or version.startswith(base + ".")):
                    return False
                continue
            want = base
        c = _cmp(version, want)
        if op in ("==", "==="):
            if not (version == want or c == 0):
                return False
        elif op == "!=":
            if c == 0:
                return False
        elif op == ">=":
            if c < 0:
                return False
        elif op == "<=":
            if c > 0:
                return False
        elif op == ">":
            if c <= 0:
                return False
        elif op == "<":
            if c >= 0:
                return False
        elif op == "~=":
            # ~=1.4.2 means >=1.4.2, ==1.4.*
            if c < 0:
                return False
            parts = want.split(".")
            if len(parts) >= 2:
                base = ".".join(parts[:-1])
                if not (version == base or version.startswith(base + ".")):
                    return False
    return True


def satisfies_npm(version, spec):
    """semver-lite: `||` unions of comma/space-joined comparator clauses."""
    spec = (spec or "").strip()
    if not spec or spec in ("*", "x", "latest", "") or spec.startswith(("http", "git", "file:", "workspace:", "link:")):
        return True
    for alt in spec.split("||"):
        if _satisfies_npm_one(version, alt.strip()):
            return True
    return False


def _satisfies_npm_one(version, spec):
    for clause in re.split(r"\s+", spec.strip()):
        if not clause:
            continue
        m = re.match(r"(\^|~|>=|<=|>|<|=)?\s*v?(.+)$", clause)
        if not m:
            return False
        op, want = m.group(1) or "=", m.group(2).strip()
        if want in ("*", "x"):
            continue
        c = _cmp(version, want)
        if op == "=":
            if version != want and c != 0:
                return False
        elif op == ">=":
            if c < 0:
                return False
        elif op == "<=":
            if c > 0:
                return False
        elif op == ">":
            if c <= 0:
                return False
        elif op == "<":
            if c >= 0:
                return False
        elif op == "^":
            # ^1.2.3 -> >=1.2.3 <2.0.0 ; ^0.2.3 -> >=0.2.3 <0.3.0 ; ^0.0.3 -> =0.0.3
            if c < 0:
                return False
            w = [int(x) for x in _NUM.findall(want)][:3] + [0, 0, 0]
            v = [int(x) for x in _NUM.findall(version)][:3] + [0, 0, 0]
            if w[0] > 0:
                if v[0] != w[0]:
                    return False
            elif w[1] > 0:
                if v[0] != 0 or v[1] != w[1]:
                    return False
            else:
                if v[:3] != w[:3]:
                    return False
        elif op == "~":
            # ~1.2.3 -> >=1.2.3 <1.3.0 ; ~1.2 -> >=1.2.0 <1.3.0 ; ~1 -> >=1.0.0 <2.0.0
            if c < 0:
                return False
            w = [int(x) for x in _NUM.findall(want)]
            v = [int(x) for x in _NUM.findall(version)][:3] + [0, 0, 0]
            if len(w) >= 2:
                if v[0] != w[0] or v[1] != w[1]:
                    return False
            elif len(w) == 1:
                if v[0] != w[0]:
                    return False
    return True


def spec_class(spec, eco):
    s = (spec or "").strip()
    if not s or s in ("*", "x", "latest"):
        return "ANY"
    if s.startswith(("http", "git", "file:", "workspace:", "link:", "npm:")):
        return "NON-REGISTRY"
    if eco == "pypi":
        if re.search(r"(^|,)\s*===?\s*[\d]", s) and "*" not in s:
            return "EXACT"
        if re.search(r"[~<]", s):
            return "CAPPED"
        if re.search(r">", s):
            return "FLOOR"
        if re.match(r"^\s*[\d]", s):
            return "EXACT"
        return "ANY"
    if re.match(r"^\s*v?\d", s):
        return "EXACT"
    if re.search(r"[\^~<]", s):
        return "CAPPED"
    if re.search(r">", s):
        return "FLOOR"
    return "ANY"


# ---------------------------------------------------------------- manifests

def _bracketed(text, key):
    """The body of `key = [ ... ]`, matched by BRACKET DEPTH, not by `.*?\]`.

    A non-greedy scan to the first `]` is wrong and the control caught it: the
    very first dependency of the repo that motivated this instrument is
    `"pyjwt[crypto]>=2.8,<3"`, whose EXTRA bracket closes the match before a
    single complete quoted string exists, so the parser returned an empty list
    for a manifest with five dependencies. Quoted brackets are skipped here.
    """
    m = re.search(r"^[ \t]*" + re.escape(key) + r"\s*=\s*\[", text, re.M)
    if not m:
        return None
    i, depth, q = m.end(), 1, None
    while i < len(text):
        ch = text[i]
        if q:
            if ch == q and text[i - 1] != "\\":
                q = None
        elif ch in "\"'":
            q = ch
        elif ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
            if depth == 0:
                return text[m.end():i]
        i += 1
    return None


def parse_pyproject(text):
    """(name, spec) for [project].dependencies and [tool.poetry.dependencies]."""
    out = []
    m = _bracketed(text, "dependencies")
    if m:
        # Match a quoted string as a WHOLE, double-quote branch first.  A
        # character-class pattern like `["\']([^"\']+)["\']` splits
        # `"faiss-cpu>=1.8.0; python_version < \'3.14\'"` at the INNER single
        # quotes and emits `3.14` as a dependency of its own -- which is what the
        # first run of this instrument reported for HKUDS/DeepTutor.
        for dq, sq in re.findall(r'"([^"]*)"|\'([^\']*)\'', m):
            item = dq or sq
            item = item.split(";")[0].strip()
            n = re.match(r"([A-Za-z0-9][A-Za-z0-9._-]*)(\[[^\]]*\])?\s*(.*)$", item)
            if n:
                out.append((n.group(1).lower(), (n.group(3) or "").strip()))
    pm = re.search(r"\[tool\.poetry\.dependencies\](.*?)(\n\[|\Z)", text, re.S)
    if pm:
        for line in pm.group(1).splitlines():
            n = re.match(r'\s*([A-Za-z0-9][A-Za-z0-9._-]*)\s*=\s*["\']([^"\']+)["\']', line)
            if n and n.group(1).lower() != "python":
                out.append((n.group(1).lower(), n.group(2).strip()))
    return out


def parse_requirements(text):
    out = []
    for line in (text or "").splitlines():
        line = line.split("#")[0].split(";")[0].strip()
        # A hash-pinned requirements.txt continues each requirement onto its own
        # `--hash=` lines with a trailing backslash.  Leaving the backslash on the
        # specifier makes `==0.5.1 \\` the published spec; it still RESOLVED here
        # only because the comparator is numeric, which is luck, not design.
        line = line.rstrip("\\").strip()
        if not line or line.startswith("-"):
            continue
        n = re.match(r"([A-Za-z0-9][A-Za-z0-9._-]*)(\[[^\]]*\])?\s*(.*)$", line)
        if n:
            out.append((n.group(1).lower(), (n.group(3) or "").strip()))
    return out


def parse_package_json(text):
    try:
        j = json.loads(text)
    except ValueError:
        return []
    return [(k, str(v)) for k, v in (j.get("dependencies") or {}).items()]


# ---------------------------------------------------------------- network

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "globant-kb-p437"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception:
        return 0, ""


def releases(name, eco):
    """{version: upload_date} for every release the registry serves."""
    if eco == "pypi":
        c, t = get(f"https://pypi.org/pypi/{name}/json")
        if c != 200:
            return None
        d = json.loads(t)
        out = {}
        for v, files in (d.get("releases") or {}).items():
            ds = [f.get("upload_time_iso_8601") for f in files if f.get("upload_time_iso_8601")]
            if ds:
                out[v] = min(ds)[:10]
        return out
    c, t = get(f"https://registry.npmjs.org/{name}")
    if c != 200:
        return None
    d = json.loads(t)
    times = d.get("time") or {}
    return {v: times[v][:10] for v in (d.get("versions") or {}) if v in times}


def resolve(name, spec, eco, ref):
    rel = releases(name, eco)
    if rel is None:
        return (name, eco, spec, spec_class(spec, eco), "", "", "", "", "NOT-IN-REGISTRY")
    sat = satisfies_py if eco == "pypi" else satisfies_npm
    cands = [v for v in rel if not is_prerelease(v) and sat(v, spec)] or \
            [v for v in rel if sat(v, spec)]
    latest = max((v for v in rel if not is_prerelease(v)), key=vkey, default=None) or \
             max(rel, key=vkey, default=None)
    if not cands or latest is None:
        return (name, eco, spec, spec_class(spec, eco), "", "", latest or "",
                rel.get(latest, "") if latest else "", "NO-SATISFYING-RELEASE")
    pick = max(cands, key=vkey)
    age = lambda d: (ref - dt.date.fromisoformat(d)).days if d else ""
    return (name, eco, spec, spec_class(spec, eco), pick, str(age(rel[pick])),
            latest, str(age(rel[latest])), "OK")


# ---------------------------------------------------------------- driver

MANIFEST_PARSERS = {
    "pyproject.toml": parse_pyproject,
    "requirements.txt": parse_requirements,
    "package.json": parse_package_json,
}


def parser_for(path):
    base = path.split("#")[0].split("/")[-1]
    return MANIFEST_PARSERS.get(base)


def main():
    targets, ref = sys.argv[1], dt.date.fromisoformat(sys.argv[2])
    rows = []
    for line in open(targets):
        if line.startswith("#") or not line.strip():
            continue
        slug, gref, manifest, eco = line.rstrip("\n").split("\t")[:4]
        path = manifest.split("#")[0]
        p = parser_for(manifest)
        if not p:
            continue
        c, t = get(RAW.format(slug=slug, ref=gref, path=path))
        if c != 200:
            print(f"# UNFETCHED\t{slug}\t{manifest}\t{c}", file=sys.stderr)
            continue
        for name, spec in p(t):
            rows.append((slug, manifest, name, spec, eco))
    seen, work = set(), []
    for slug, manifest, name, spec, eco in rows:
        k = (slug, manifest, name)
        if k in seen:
            continue
        seen.add(k)
        work.append((slug, manifest, name, spec, eco))
    def run(w):
        slug, manifest, name, spec, eco = w
        return (slug, manifest) + resolve(name, spec, eco, ref)
    print("slug\tmanifest\tdep\teco\tspec\tspec_class\tpinned_version\tpinned_age\t"
          "latest_version\tlatest_age\tstatus")
    with ThreadPoolExecutor(max_workers=12) as ex:
        for r in ex.map(run, work):
            print("\t".join(str(x) for x in r))


if __name__ == "__main__":
    main()
