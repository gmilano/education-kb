#!/usr/bin/env python3
"""p452 — Gap 451-A back-link agreement sweep.

p451 established the standing rule: a registry record is evidence for a GitHub
address only when its OWN metadata back-links to that exact `owner/repo`.
p451 also recorded that no instrument enforces it and that the carried
population had never been swept.  This is the sweep.

For each (registry, package, claimed_slug) carried on the shelves it reads the
registry record first-hand and emits one of:

  AGREE      declared repository normalises to the claimed owner/repo
  DISAGREE   declared repository normalises to a DIFFERENT owner/repo
  ABSENT     record exists, no repository field at all  (zero bits either way)
  NO_RECORD  registry returns 404 for the package name

Controls run in BOTH directions in the same process (P249): a pair whose
agreement is known, and a fabricated package that must come back NO_RECORD.
"""
import json, re, subprocess, sys

UA = "globant-kb-education/p452 (back-link agreement sweep)"

def get(url):
    p = subprocess.run(
        ["curl", "-sS", "-A", UA, "-w", "\n%{http_code}", "--max-time", "35", url],
        capture_output=True, text=True)
    out = p.stdout.rsplit("\n", 1)
    if len(out) != 2:
        return None, 0
    body, code = out
    try:
        code = int(code.strip())
    except ValueError:
        code = 0
    return body, code

# p452 — the v1 normaliser matched `github.com` ONLY, and that is a FALSE-NEGATIVE
# generator, not a conservative choice: `travo` back-links
# `https://gitlab.com/travo-cr/travo.git/` — an EXACT, correct back-link — and v1
# called it ABSENT. A forge-blind back-link checker manufactures absences on every
# project that is not on GitHub. The forge is therefore part of the identity.
FORGES = ('github.com', 'gitlab.com', 'bitbucket.org', 'codeberg.org',
          'git.sr.ht', 'gitee.com', 'salsa.debian.org', 'framagit.org')
SLUG = re.compile(
    r'(' + '|'.join(f.replace('.', r'\.') for f in FORGES) +
    r')[:/]+([A-Za-z0-9._-]+)/([A-Za-z0-9._-]+?)(?:\.git)?/?(?:[/#?].*)?$')

# p452 — a GitHub *Pages* URL is NOT a back-link, and it is the trap a naive
# `grep -i github` falls into: PyPI `tincan` declares only
# `http://rusticisoftware.github.io/TinCanPython/`, which asserts a published
# SITE, not a repository, and the owner segment of a Pages host need not equal
# the repository owner. It is graded PAGES_ONLY — a hint, never evidence.
PAGES = re.compile(r'https?://([A-Za-z0-9-]+)\.github\.io/([A-Za-z0-9._-]+)/?', re.I)

def norm(url):
    """Normalise a declared repository URL to lowercase forge/owner/repo, or None.

    Returns a 'forge:owner/repo' string so that two different forges holding the
    same owner/repo pair can never be scored as agreeing.
    """
    if not url:
        return None
    url = url.strip()
    url = re.sub(r'^(git\+|git:|ssh://|hg\+)', '', url)
    url = re.sub(r'^github:', 'github.com/', url)
    m = SLUG.search(url)
    if m:
        forge = m.group(1).lower()
        return f"{forge}/{m.group(2).lower()}/{m.group(3).lower()}"
    # bare "owner/repo" shorthand, as npm permits, means GitHub by npm's own rule
    if re.fullmatch(r'[A-Za-z0-9._-]+/[A-Za-z0-9._-]+', url):
        return f"github.com/{url.lower()}"
    return None

def is_pages(url):
    return bool(url and PAGES.match(url.strip()))

def norm_claim(claimed):
    """A claimed address may be forge-qualified ('gitlab.com/a/b') or bare."""
    if not claimed:
        return None
    c = claimed.strip().lower()
    if c.startswith(FORGES):
        return c.rstrip('/')
    return f"github.com/{c}"

def npm(pkg):
    body, code = get(f"https://registry.npmjs.org/{pkg.replace('/', '%2f')}")
    if code == 404:
        return "NO_RECORD", None, None, None
    if code != 200:
        return f"HTTP_{code}", None, None, None
    d = json.loads(body)
    latest = (d.get("dist-tags") or {}).get("latest")
    v = (d.get("versions") or {}).get(latest, {})
    repo = v.get("repository") or d.get("repository")
    if isinstance(repo, dict):
        repo = repo.get("url")
    elif isinstance(repo, list) and repo:
        repo = repo[0] if isinstance(repo[0], str) else (repo[0] or {}).get("url")
    lic = v.get("license") or d.get("license")
    if isinstance(lic, dict):
        lic = lic.get("type")
    return None, repo, lic, latest

def pypi(pkg):
    body, code = get(f"https://pypi.org/pypi/{pkg}/json")
    if code == 404:
        return "NO_RECORD", None, None, None
    if code != 200:
        return f"HTTP_{code}", None, None, None
    info = json.loads(body).get("info", {})
    urls = info.get("project_urls") or {}
    repo = None
    # prefer keys that assert a code location, in declared order of strength
    for k in ("Repository", "Source", "Source Code", "Code", "Homepage", "homepage", "GitHub"):
        for kk, vv in urls.items():
            if kk.lower() == k.lower() and norm(vv):
                repo = vv
                break
        if repo:
            break
    if not repo and norm(info.get("home_page")):
        repo = info.get("home_page")
    # p452 self-check: PAGES_ONLY was unreachable in the first cut of this file,
    # because a Pages URL fails norm() and so was never carried out of here to be
    # graded. A verdict class that cannot fire is worse than no class — it reads as
    # "no project ever did this". The candidate is kept so the grader can see it.
    if not repo:
        for vv in list(urls.values()) + [info.get("home_page")]:
            if is_pages(vv):
                repo = vv
                break
    lic = info.get("license") or None
    if lic and len(lic) > 60:            # some projects paste the whole text
        lic = lic[:57].replace("\n", " ") + "..."
    if not lic:
        for c in info.get("classifiers") or []:
            if c.startswith("License ::"):
                lic = c.split("::")[-1].strip()
                break
    return None, repo, lic, info.get("version")

def packagist(pkg):
    body, code = get(f"https://packagist.org/packages/{pkg}.json")
    if code == 404:
        return "NO_RECORD", None, None, None
    if code != 200:
        return f"HTTP_{code}", None, None, None
    d = json.loads(body).get("package", {})
    repo = d.get("repository")
    vers = d.get("versions") or {}
    lic, ver = None, None
    for name, meta in vers.items():
        if name.startswith("dev-"):
            continue
        ver = name
        lic = ", ".join(meta.get("license") or []) or None
        break
    return None, repo, lic, ver

FETCH = {"npm": npm, "pypi": pypi, "packagist": packagist}

def sweep(rows):
    out = []
    for registry, pkg, claimed in rows:
        err, repo, lic, ver = FETCH[registry](pkg)
        if err:
            out.append((registry, pkg, claimed, err, repo or "", lic or "", ver or "", ""))
            continue
        got = norm(repo)
        want = norm_claim(claimed)
        if got is None:
            verdict = "PAGES_ONLY" if is_pages(repo) else "ABSENT"
        elif want and got == want:
            verdict = "AGREE"
        elif want and got.split('/', 1)[0] != want.split('/', 1)[0]:
            verdict = "FOREIGN_FORGE"
        else:
            verdict = "DISAGREE"
        out.append((registry, pkg, claimed, verdict, repo or "", lic or "", ver or "", got or ""))
    return out

if __name__ == "__main__":
    rows = [tuple(l.rstrip("\n").split("\t")) for l in open(sys.argv[1]) if l.strip() and not l.startswith("#")]
    res = sweep(rows)
    print("registry\tpackage\tclaimed_slug\tverdict\tdeclared_repository\tdeclared_licence\tversion\tnormalised")
    for r in res:
        print("\t".join(r))
