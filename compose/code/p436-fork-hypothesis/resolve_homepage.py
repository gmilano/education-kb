#!/usr/bin/env python3
"""p436 — resolve a repository's DECLARED UPSTREAM through the package registry.

Pass 24 (2026-10-07) closed with a rule it could not yet execute:

    A licence holder that does not match the publishing account is a fork signal.
    Resolve the upstream before citing, and prefer the repository the package
    registry names as its homepage.

This is that resolution step.  It needs no `api.github.com` (403 here) and no
rendered `github.com` page (403 here): a package's own metadata carries the
repository URL its publisher declared.

Channel, per ecosystem:
    PyPI  https://pypi.org/pypi/<name>/json   -> info.project_urls / info.home_page
    npm   https://registry.npmjs.org/<name>   -> repository.url / homepage

Verdicts:
    SELF        the registry names THIS slug           -> original, or the fork that publishes
    UPSTREAM    the registry names a DIFFERENT slug    -> fork hypothesis, with the candidate
    NO-PACKAGE  a manifest exists, the registry 404s   -> not published; git is the only channel
    NO-MANIFEST no manifest found at the probed paths
    PRIVATE-MANIFEST  `"private": true` -> the name is local, the registry is not its registry

Three DISTINCT ways a declared slug differs from the cited one, all measured on
2026-10-07 and only the first of which is a fork:

    fork lineage      `ucfopen/pylti1.3`   -> `dmitry-viskov/pylti1.3`   (real upstream)
    multi-repo publisher  `langfuse/langfuse` -> `langfuse/langfuse-js`  (sibling SDK repo)
    name collision    `kaorii-ako/Shiori-v1` -> `shiorijs/shiori`        (unrelated package)

So UPSTREAM is a READING LIST, exactly as P184's HOLDER-UNRELATED is: it shortens
the list, it does not decide it.

TSV: slug, ecosystem, package, verdict, declared_slug
"""
import json, re, sys, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor

RAW = "https://raw.githubusercontent.com/{slug}/HEAD/{path}"
SLUG_RE = re.compile(r'github\.com[:/]+([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+?)(?:\.git)?(?:[/#?]|$)')


def get(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": "globant-kb-p436"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception:
        return 0, ""


def pkg_name(slug):
    """(ecosystem, package name) from the repo's own manifest, or (None, None)."""
    c, t = get(RAW.format(slug=slug, path="pyproject.toml"))
    if c == 200:
        m = re.search(r'^\s*name\s*=\s*["\']([^"\']+)["\']', t, re.M)
        if m:
            return "pypi", m.group(1)
    c, t = get(RAW.format(slug=slug, path="setup.py"))
    if c == 200:
        m = re.search(r'name\s*=\s*["\']([^"\']+)["\']', t)
        if m:
            return "pypi", m.group(1)
    # setup.cfg -- the classic setuptools layout, where `pyproject.toml` carries only
    # tool config and the package metadata lives in `[metadata]`.  Omitting it was a
    # coverage defect in the first build, caught by the SELF control:
    # `academic-innovation/django-lti` ships a `pyproject.toml` with NO `[project]`
    # table at all and was reported NO-MANIFEST, i.e. "no channel" for a package that
    # is on PyPI.  A probe list that misses a layout returns the same string as a repo
    # that genuinely publishes nothing, which is the error class P183 is named for.
    c, t = get(RAW.format(slug=slug, path="setup.cfg"))
    if c == 200:
        m = re.search(r'^\s*name\s*=\s*([^\s#]+)', t, re.M)
        if m:
            return "pypi", m.group(1).strip('"\'')
    c, t = get(RAW.format(slug=slug, path="package.json"))
    if c == 200:
        try:
            j = json.loads(t)
            # `"private": true` means the manifest is a workspace root that is NEVER
            # published.  Its `name` is a LOCAL label and collides freely with the
            # registry.  Measured case: `kaorii-ako/Shiori-v1` declares
            # `"name": "shiori", "private": true`; npm's `shiori` is "a lightweight
            # discord library made for NodeJS" pointing at `shiorijs/shiori`, a slug
            # that does not resolve over `git`.  Resolving that manifest produced a
            # fork hypothesis against a DELETED repository for an UNRELATED project.
            # Honouring `private` is what keeps the UPSTREAM class readable.
            if isinstance(j, dict) and j.get("private") is True:
                return "private", j.get("name") or "-"
            if isinstance(j, dict) and j.get("name"):
                return "npm", j["name"]
        except ValueError:
            pass
    return None, None


def declared(eco, name):
    """The repository slug the REGISTRY says the package lives at, or None."""
    if eco == "pypi":
        c, t = get(f"https://pypi.org/pypi/{name}/json")
        if c != 200:
            return "404", None
        info = json.loads(t)["info"]
        urls = list((info.get("project_urls") or {}).values()) + [info.get("home_page") or ""]
    else:
        c, t = get(f"https://registry.npmjs.org/{name}")
        if c != 200:
            return "404", None
        j = json.loads(t)
        repo = j.get("repository") or {}
        if isinstance(repo, str):
            repo = {"url": repo}
        urls = [repo.get("url") or "", j.get("homepage") or ""]
    for u in urls:
        m = SLUG_RE.search(u or "")
        if m:
            return "ok", f"{m.group(1)}/{m.group(2)}"
    return "ok", None


def one(slug):
    eco, name = pkg_name(slug)
    if not eco:
        return (slug, "-", "-", "NO-MANIFEST", "-")
    if eco == "private":
        return (slug, "private", name, "PRIVATE-MANIFEST", "-")
    state, d = declared(eco, name)
    if state == "404":
        return (slug, eco, name, "NO-PACKAGE", "-")
    if d is None:
        return (slug, eco, name, "NO-REPO-URL", "-")
    v = "SELF" if d.lower() == slug.lower() else "UPSTREAM"
    return (slug, eco, name, v, d)


def main():
    slugs = [l.strip() for l in open(sys.argv[1]) if l.strip()]
    with ThreadPoolExecutor(max_workers=12) as ex:
        for r in ex.map(one, slugs):
            print("\t".join(r))


if __name__ == "__main__":
    main()
