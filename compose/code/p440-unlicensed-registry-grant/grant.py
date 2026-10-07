#!/usr/bin/env python3
"""p440 -- pass 25's action A: a repository with no LICENSE file may still carry a grant.

Pass 25 measured the licence PAYLOAD of all 503 slugs this KB cites and published
`87 UNLICENSED`: no file named by any of 14 probe names returns 200 at HEAD.  The
pre-registered action was:

    Run p436's four stages over the 87 UNLICENSED rows -- the slugs this shelf cites
    that ship no licence file at all -- and resolve each against its registry's
    declared licence field.
    Prediction: expect the registry to supply a licence for FEWER THAN HALF.  The
    interesting class is the opposite one: a repository with NO `LICENSE` whose
    published package declares MIT, which is a grant made in the registry and
    nowhere in the tree.

Two layers, and the whole point is that they can disagree:

    tree      raw.githubusercontent.com/<slug>/HEAD/<14 names>   -> p436: no file
    registry  the publisher's own declared `license` field       -> this instrument

Channels.  The first four are p436's; the last three are the registries pass 25
proved reachable for RELEASE DATES, used here for the first time to answer an
IDENTITY question:

    pypi       pypi.org/pypi/<n>/json                 info.license_expression | license | classifiers
    npm        registry.npmjs.org/<n>                 versions[latest].license | licenses
    packagist  repo.packagist.org/p2/<v>/<p>.json     packages[<p>][0].license[]
    maven      repo1.maven.org/maven2/<g>/<a>/<v>/<a>-<v>.pom   <licenses><license><name>
    hex        hex.pm/api/packages/<n>                meta.licenses[]

A grant read off a registry is only THIS repository's grant if the registry agrees
the package lives here.  The first build of this instrument omitted that check and
published two rows that prove why it cannot be omitted:

    pnp-v/bo-google-classroom-mcp-server  declares `"name": "class"`, and npm's
      `class` is an unrelated package.  Unguarded, this publishes somebody else's
      MIT grant as this repository's licence -- the same name-collision class
      p436's `kaorii-ako/Shiori-v1` control exists for.
    canvas-mcp-server  was resolved for BOTH `DMontgomery40/mcp-canvas-lms` and
      `plyght/canvas-mcp`.  One npm name cannot be owned by two repositories, so at
      most one of those two rows was ever a grant.

So the slug the registry declares is read in the same call and compared:

Verdicts:
    REGISTRY-GRANT   the registry names a licence the tree does not, AND names
                     THIS repository as the package's home                <- the finding
    FOREIGN-PACKAGE  a licence is declared, but the registry names a DIFFERENT
                     repository -- the grant is somebody else's
    GRANT-UNOWNED    a licence is declared and the registry names NO repository at
                     all, so ownership cannot be established either way
    REGISTRY-SILENT  the package exists and declares no licence
    REGISTRY-REFUSAL the registry declares `UNLICENSED`: an explicit NON-grant
    REGISTRY-DEFER   `SEE LICENSE IN <file>`: a pointer to a file that is not there
    NO-PACKAGE       a manifest exists, the registry 404s
    NO-CHANNEL       no manifest at the probed paths, or a `private` manifest

REGISTRY-REFUSAL and REGISTRY-DEFER exist as separate verdicts because collapsing
either into REGISTRY-GRANT publishes the OPPOSITE of the truth, and because
`../dependency-licence-closure/dep_licence.py` did exactly that until this pass:
its PERMISSIVE rule `r"UNLICENSE"` matches npm's `UNLICENSED` -- the documented
convention for "I grant you nothing" -- and returned the same class as `Unlicense`,
the public-domain dedication.  See `test_grant.py`, controls 1-4.

Classification of the string, once read, is delegated to `dep_licence.py`: rule 1
of P126 forbids re-deriving what the repository already versions.

TSV: slug, eco, package, verdict, licence_raw, field, class, declared_slug
"""
import json
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, "../dependency-licence-closure")
from dep_licence import classify_licence, npm_licence, pypi_licence  # noqa: E402

RAW = "https://raw.githubusercontent.com/{slug}/HEAD/{path}"
SLUG_RE = re.compile(r'github\.com[:/]+([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+?)(?:\.git)?(?:[/#?]|$)')

# p436's list, verbatim, so the "the tree has none" half of every REGISTRY-GRANT
# row is re-measured by the SAME probe that produced the 87, not a narrower one.
LICENSE_NAMES = ["LICENSE", "LICENSE.md", "LICENSE.txt", "COPYING", "COPYING.txt",
                 "license", "license.md", "license.txt", "LICENCE", "LICENCE.md",
                 "LICENSE-MIT", "LICENSE-APACHE", "LICENSE.rst", "LICENSE-MIT.txt"]

# npm's two reserved values.  Neither is a licence NAME and neither may be
# classified as one.  https://docs.npmjs.com/cli/configuring-npm/package-json#license
REFUSAL_RE = re.compile(r"^\s*unlicensed\s*$", re.I)
DEFER_RE = re.compile(r"^\s*see\s+licen[cs]e\s+in\s+(.+?)\s*$", re.I)


def get(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": "globant-kb-p440"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception:
        return 0, ""


def tree_has_licence(slug):
    """Re-run p436's probe at HEAD.  Returns the hit path, or None."""
    for fn in LICENSE_NAMES:
        code, _ = get(RAW.format(slug=slug, path=fn))
        if code == 200:
            return fn
    return None


# ---------------------------------------------------------------- manifests

def _toml_name(text):
    m = re.search(r'^\s*name\s*=\s*["\']([^"\']+)["\']', text, re.M)
    return m.group(1) if m else None


def pkg_name(slug):
    """(ecosystem, package coordinate) from the repo's own manifest.

    p436's four probes, then the three ecosystems whose registries pass 25 proved
    reachable.  A probe list that misses a layout returns the same string as a
    repository that genuinely publishes nothing -- the error class P183 is named for --
    so widening the list is the only way the NO-CHANNEL count means anything.
    """
    code, text = get(RAW.format(slug=slug, path="pyproject.toml"))
    if code == 200 and _toml_name(text):
        return "pypi", _toml_name(text)
    code, text = get(RAW.format(slug=slug, path="setup.py"))
    if code == 200:
        m = re.search(r'name\s*=\s*["\']([^"\']+)["\']', text)
        if m:
            return "pypi", m.group(1)
    code, text = get(RAW.format(slug=slug, path="setup.cfg"))
    if code == 200:
        m = re.search(r'^\s*name\s*=\s*([^\s#]+)', text, re.M)
        if m:
            return "pypi", m.group(1).strip('"\'')
    code, text = get(RAW.format(slug=slug, path="package.json"))
    if code == 200:
        try:
            j = json.loads(text)
            if isinstance(j, dict):
                if j.get("private") is True:
                    return "private", j.get("name") or "-"
                if j.get("name"):
                    return "npm", j["name"]
        except ValueError:
            pass
    code, text = get(RAW.format(slug=slug, path="composer.json"))
    if code == 200:
        try:
            j = json.loads(text)
            if isinstance(j, dict) and j.get("name"):
                return "packagist", j["name"]
        except ValueError:
            pass
    code, text = get(RAW.format(slug=slug, path="pom.xml"))
    if code == 200:
        co = pom_coordinates(text)
        if co:
            return "maven", co
    code, text = get(RAW.format(slug=slug, path="mix.exs"))
    if code == 200:
        m = re.search(r'app:\s*:([A-Za-z0-9_]+)', text)
        if m:
            return "hex", m.group(1)
    return None, None


def pom_coordinates(text):
    """`group:artifact` from a POM, ignoring every nested <dependency> block.

    A naive first-match scan over a POM returns the first <groupId> in the file,
    which in a POM that declares <parent> before its own coordinates is the
    PARENT's group -- and in a flattened POM is a dependency's.  Both publish a
    coordinate that resolves to somebody else's artifact.
    """
    body = re.sub(r"<(dependencies|build|profiles|dependencyManagement)\b.*?</\1>",
                  "", text, flags=re.S)
    parent = re.search(r"<parent\b.*?</parent>", body, re.S)
    own = body.replace(parent.group(0), "") if parent else body
    g = re.search(r"<groupId>\s*([^<\s]+)\s*</groupId>", own)
    a = re.search(r"<artifactId>\s*([^<\s]+)\s*</artifactId>", own)
    if not g and parent:
        g = re.search(r"<groupId>\s*([^<\s]+)\s*</groupId>", parent.group(0))
    if g and a:
        return f"{g.group(1)}:{a.group(1)}"
    return None


# ---------------------------------------------------------------- registries

def packagist_licence(payload, name):
    pkgs = (payload or {}).get("packages") or {}
    vers = pkgs.get(name) or next(iter(pkgs.values()), None) or []
    for v in vers:
        lic = v.get("license")
        if lic:
            return lic, "packages[0].license"
    return None, "absent"


def maven_licence(pom_text):
    """<name> of each <license> in the project's own <licenses> block."""
    body = re.sub(r"<(dependencies|build|profiles|dependencyManagement)\b.*?</\1>",
                  "", pom_text or "", flags=re.S)
    block = re.search(r"<licenses\b.*?</licenses>", body, re.S)
    if not block:
        return None, "absent"
    names = re.findall(r"<name>\s*(.*?)\s*</name>", block.group(0), re.S)
    names = [re.sub(r"\s+", " ", n).strip() for n in names if n.strip()]
    return (names, "pom.licenses") if names else (None, "absent")


def hex_licence(payload):
    lic = ((payload or {}).get("meta") or {}).get("licenses")
    return (lic, "meta.licenses") if lic else (None, "absent")


def first_slug(urls):
    """The first `owner/repo` in a list of candidate URLs, or None."""
    for u in urls:
        m = SLUG_RE.search(u or "")
        if m:
            return f"{m.group(1)}/{m.group(2)}"
    return None


def read_registry(eco, name):
    """(state, licence_raw, field, declared_slug).  state: `ok` | `404` | `unreachable`."""
    if eco == "pypi":
        code, body = get(f"https://pypi.org/pypi/{name}/json")
        if code == 404:
            return "404", None, "-", None
        if code != 200:
            return "unreachable", None, "-", None
        payload = json.loads(body)
        raw, field = pypi_licence(payload)
        info = payload.get("info") or {}
        urls = list((info.get("project_urls") or {}).values()) + [info.get("home_page") or ""]
        return "ok", raw, field, first_slug(urls)
    if eco == "npm":
        code, body = get(f"https://registry.npmjs.org/{name}")
        if code == 404:
            return "404", None, "-", None
        if code != 200:
            return "unreachable", None, "-", None
        payload = json.loads(body)
        raw, field = npm_licence(payload)
        repo = payload.get("repository") or {}
        if isinstance(repo, str):
            repo = {"url": repo}
        latest = ((payload.get("dist-tags") or {}).get("latest"))
        ver = ((payload.get("versions") or {}).get(latest)) or {}
        vrepo = ver.get("repository") or {}
        if isinstance(vrepo, str):
            vrepo = {"url": vrepo}
        urls = [vrepo.get("url") or "", repo.get("url") or "",
                ver.get("homepage") or "", payload.get("homepage") or ""]
        return "ok", raw, field, first_slug(urls)
    if eco == "packagist":
        code, body = get(f"https://repo.packagist.org/p2/{name}.json")
        if code == 404:
            return "404", None, "-", None
        if code != 200:
            return "unreachable", None, "-", None
        payload = json.loads(body)
        raw, field = packagist_licence(payload, name)
        vers = (payload.get("packages") or {}).get(name) or []
        urls = [((v.get("source") or {}).get("url") or "") for v in vers[:3]]
        urls += [(v.get("homepage") or "") for v in vers[:3]]
        return "ok", raw, field, first_slug(urls)
    if eco == "maven":
        group, artifact = name.split(":", 1)
        base = f"https://repo1.maven.org/maven2/{group.replace('.', '/')}/{artifact}"
        code, meta = get(f"{base}/maven-metadata.xml")
        if code == 404:
            return "404", None, "-", None
        if code != 200:
            return "unreachable", None, "-", None
        ver = re.search(r"<release>\s*([^<\s]+)\s*</release>", meta) or \
            re.search(r"<version>\s*([^<\s]+)\s*</version>", meta)
        if not ver:
            return "ok", None, "absent", None
        v = ver.group(1)
        # maven-metadata.xml carries NO licence element at all.  The grant lives in
        # the POM of a specific version, so a reader that stops at the metadata file
        # reports REGISTRY-SILENT for every Maven package on the shelf.
        code, pom = get(f"{base}/{v}/{artifact}-{v}.pom")
        if code != 200:
            # Maven Central answers 429 under load, and its 429 body is prose.  A
            # reader that folds every non-200 into "absent" publishes REGISTRY-SILENT
            # for a POM it never read -- the one verdict in this table that cannot be
            # distinguished from a real absence after the fact.  Measured on
            # 2026-10-07: `org.verapdf:verapdf-library` came back `absent@1.30.2` on
            # the first run purely because the POM fetch was rate-limited.
            return "unreachable", None, f"pom-http-{code}@{v}", None
        raw, field = maven_licence(pom)
        scm = re.search(r"<scm\b.*?</scm>", pom, re.S)
        urls = re.findall(r"<(?:url|connection|developerConnection)>\s*(.*?)\s*</",
                          scm.group(0), re.S) if scm else []
        urls += re.findall(r"<url>\s*(.*?)\s*</url>", pom, re.S)
        return "ok", raw, f"{field}@{v}", first_slug(urls)
    if eco == "hex":
        code, body = get(f"https://hex.pm/api/packages/{name}")
        if code == 404:
            return "404", None, "-", None
        if code != 200:
            return "unreachable", None, "-", None
        payload = json.loads(body)
        raw, field = hex_licence(payload)
        links = ((payload.get("meta") or {}).get("links") or {})
        urls = list(links.values()) if isinstance(links, dict) else []
        return "ok", raw, field, first_slug(urls)
    return "unreachable", None, "-", None


# ---------------------------------------------------------------- verdict

def verdict_of(raw):
    """(verdict, class) for a licence value read off a registry.

    The two npm reserved values are separated BEFORE classification, because
    `classify_licence` matches `UNLICENSE` inside `UNLICENSED` and would return
    PERMISSIVE for an explicit refusal to grant.
    """
    flat = raw
    if isinstance(flat, list):
        flat = next((x for x in flat if x), None)
    if isinstance(flat, dict):
        flat = flat.get("type")
    if flat is None or not str(flat).strip():
        return "REGISTRY-SILENT", "UNKNOWN"
    text = str(flat)
    if REFUSAL_RE.match(text):
        return "REGISTRY-REFUSAL", "NO-GRANT"
    if DEFER_RE.match(text):
        return "REGISTRY-DEFER", "UNKNOWN"
    return "REGISTRY-GRANT", classify_licence(raw)


def one(slug):
    eco, name = pkg_name(slug)
    if eco is None:
        return (slug, "-", "-", "NO-CHANNEL", "-", "no-manifest", "-", "-")
    if eco == "private":
        return (slug, "private", name, "NO-CHANNEL", "-", "private-manifest", "-", "-")
    state, raw, field, declared_slug = read_registry(eco, name)
    if state == "404":
        return (slug, eco, name, "NO-PACKAGE", "-", "-", "-", "-")
    if state == "unreachable":
        return (slug, eco, name, "UNREACHABLE", "-", "-", "-", "-")
    verdict, cls = verdict_of(raw)
    if verdict == "REGISTRY-GRANT":
        # Ownership BEFORE the grant is published.  A licence read off a package the
        # registry says lives somewhere else is that other repository's licence.
        if declared_slug is None:
            verdict = "GRANT-UNOWNED"
        elif declared_slug.lower() != slug.lower():
            verdict = "FOREIGN-PACKAGE"
        else:
            # The claim is "the registry grants what the tree does not".  Re-probe the
            # tree rather than inheriting p436's column: the two measurements are a day
            # apart at best and a repository can add a LICENSE between them.
            hit = tree_has_licence(slug)
            if hit:
                verdict = "TREE-HAS-LICENCE-NOW"
                field = f"{field}; tree={hit}"
    shown = raw if isinstance(raw, str) else json.dumps(raw, separators=(",", ":"))
    return (slug, eco, name, verdict, shown[:120].replace("\t", " ").replace("\n", " "),
            field, cls, declared_slug or "-")


def main():
    slugs = [l.strip() for l in open(sys.argv[1]) if l.strip()]
    if not slugs:
        sys.stderr.write("p440: empty denominator -- a path fault, not a clean sweep (P355)\n")
        sys.exit(2)
    print("slug\teco\tpackage\tverdict\tlicence_raw\tfield\tclass\tdeclared_slug")
    with ThreadPoolExecutor(max_workers=10) as ex:
        for row in ex.map(one, slugs):
            print("\t".join(row))


if __name__ == "__main__":
    main()
