#!/usr/bin/env python3
"""`P238-1` — the provenance gate the grant ladder cannot be.

p228-p237 built an eleven-pass instrument establishing that a licence must be read
first-hand from the payload and never taken from the GitHub `license` field.  p238
found the limit of that programme: a DELIBERATELY labelled repository.  Thirteen
repositories named for real education products (`Moodle`, `Google Classroom`,
`PRONOTE`, ...) each carry `license: MIT` AND serve a `LICENSE` at HTTP 200, so
they pass a first-hand grant read.  The grant is real; the repository is a lure.

The missing predicate is not about licences at all.  A grant is a PERMISSION and
never a PROVENANCE claim, so provenance needs its own four checks:

  1. NAME     — a release-channel word (`Full-Version`, `Unlocked`, `Crack`) in the
                name of something that is supposed to BE source, not a download of it.
  2. FUNNEL   — the README's external links concentrate on a single host.  A real
                project's links spread over its own docs, its CI, its registry.
  3. BADGE    — the licence badge is a remote image on that same funnel host rather
                than a shields.io query of the repository.  A PICTURE of a badge.
  4. COLDNESS — 0 stars AND 0 forks AND pushed within the last few days.  Any one of
                these is ordinary for a new project; all three together is a profile.

No model, no network beyond the README this KB already fetches, no star threshold
that would exclude the genuine 0-star LATAM and APAC rows p238 published - which is
why COLDNESS alone never fires and is only ever corroborating.

usage:  lure_signature.py <name> <readme-path> [stars] [forks] [days_since_push]
        lure_signature.py --selftest
"""
import os
import re
import sys
from collections import Counter

# Release-channel vocabulary.  These words describe a DISTRIBUTION of software, so in
# the name of a source repository they are a category error, not a style choice.
CHANNEL_WORDS = (
    "full-version", "fullversion", "full_version",
    "unlocked", "cracked", "crack", "keygen", "activator",
    "serial-key", "license-key", "licensekey",
    "free-download", "freedownload", "download-latest",
    "portable-edition", "repack", "pre-activated", "preactivated",
)

# Hosts that legitimately serve badges, so a badge pointing at them is NOT a forgery.
BADGE_HOSTS = (
    "img.shields.io", "shields.io", "badgen.net", "badge.fury.io",
    "github.com", "raw.githubusercontent.com", "codecov.io",
    "api.codeclimate.com", "travis-ci.org", "travis-ci.com",
    "circleci.com", "coveralls.io", "snyk.io", "pepy.tech",
)

# Hosts whose links are infrastructure rather than destinations; excluded from the
# funnel count so a normal project is not scored as funnelling to github.com.
INFRA_HOSTS = BADGE_HOSTS + (
    "pypi.org", "npmjs.com", "www.npmjs.com", "crates.io", "rubygems.org",
    "pkg.go.dev", "hub.docker.com", "gnu.org", "www.gnu.org",
    "opensource.org", "apache.org", "www.apache.org", "spdx.org",
    "en.wikipedia.org", "arxiv.org", "doi.org", "creativecommons.org",
    "eur-lex.europa.eu", "gitlab.com", "bitbucket.org", "stackoverflow.com",
)

LINK_RE = re.compile(r'https?://([^/\s)"\'<>]+)', re.I)
IMG_RE = re.compile(r'!\[[^\]]*\]\(\s*(https?://[^)\s]+)', re.I)
LICENSE_BADGE_RE = re.compile(r'(licen[cs]e|licencia)', re.I)


def _host(url):
    m = LINK_RE.match(url)
    return m.group(1).lower() if m else ""


def _strip_www(h):
    return h[4:] if h.startswith("www.") else h


def name_hit(name):
    """Predicate 1 — a release-channel word in the repository name."""
    low = str(name).lower()
    return sorted({w for w in CHANNEL_WORDS if w in low})


def _norm(s):
    """Reduce a name or host label to its alphanumeric skeleton for comparison."""
    return re.sub(r"[^a-z0-9]", "", str(s).lower())


# P240 (pase 240): un host de LOOPBACK o de red privada no puede ser un embudo.
# Encontrado corriendo esta misma compuerta sobre el suministro fresco de p240:
# `Barbarossa2711/GRAPHIT` (MIT, leida de primera mano) marco SUSPECT con
# «FUNNEL: 60% of 5 external links point at localhost:8077».  Son las instrucciones de
# arranque de su propio JupyterLab.  La premisa de FUNNEL es que un embudo CONCENTRA al
# lector en un host de un tercero; `localhost` concentra al lector en SU PROPIA maquina,
# que es la negacion exacta de la premisa.  p238 construyo la exencion de SELF-HOST (el
# dominio del dueno) y no la de LOOPBACK, porque sus 43 filas no traian instrucciones de
# desarrollo -- el mismo patron que T240-A: el control era adecuado para el estante que
# habia.
_LOOPBACK_HOSTS = ("localhost", "127.0.0.1", "0.0.0.0", "::1", "[::1]", "host.docker.internal")
_PRIVATE_PREFIXES = ("192.168.", "10.", "169.254.")


def is_local_host(host):
    """True for loopback, link-local, RFC1918 and `.local` hosts.

    Port is stripped first: `localhost:8077` and `127.0.0.1:3000` are the shapes a README
    actually carries.
    """
    h = str(host).lower().strip()
    if h.startswith("[") and "]" in h:          # bracketed IPv6, with or without a port
        h = h[: h.index("]") + 1]
    else:
        h = h.split(":", 1)[0]
    if h in _LOOPBACK_HOSTS or h.endswith(".local") or h.endswith(".localhost"):
        return True
    if any(h.startswith(p) for p in _PRIVATE_PREFIXES):
        return True
    if h.startswith("172."):                    # 172.16.0.0/12, not 172.0.0.0/8
        part = h.split(".")
        if len(part) > 1 and part[1].isdigit() and 16 <= int(part[1]) <= 31:
            return True
    return False


def is_self_host(host, slug):
    """A project's OWN domain is not a funnel.

    p238 measured this as the gate's only false-positive mode: six real projects
    scored 60-93% link concentration on `docs.snath.ai`, `ai-sdlc.io`,
    `attestix.io`, `arkforge.tech` and two `*.github.io` pages -- their own
    documentation sites.  A lure's funnel host bears no relation to its owner
    (`rockstar49summer` -> `softyne.com`), and that is the discriminator.

    Matches when a label of the host and the owner or repository name share an
    alphanumeric skeleton by containment, which covers `ark-forge` -> `arkforge`,
    `ai-sdlc` -> `aisdlc` and `<owner>.github.io`.
    """
    if not slug:
        return False
    owner, _, repo = str(slug).partition("/")
    names = [_norm(x) for x in (owner, repo) if x]
    names = [n for n in names if len(n) >= 4]
    if not names:
        return False
    labels = [_norm(l) for l in _strip_www(str(host).lower()).split(".")]
    for lab in labels:
        if len(lab) < 4 or lab in ("github", "gitlab", "readthedocs", "pages", "netlify", "vercel"):
            continue
        for n in names:
            if lab == n or lab in n or n in lab:
                return True
    return False


def funnel_hit(readme, slug=None, threshold=0.60, min_links=5):
    """Predicate 2 — external links concentrate on one non-infrastructure host.

    Returns (host, share, count) when one host holds `threshold` or more of the
    non-infrastructure external links, else (None, share, count).
    """
    hosts = []
    for h in LINK_RE.findall(readme or ""):
        h = _strip_www(h.lower())
        if not h or h in [_strip_www(x) for x in INFRA_HOSTS]:
            continue
        if is_self_host(h, slug) or is_local_host(h):
            continue
        hosts.append(h)
    if len(hosts) < min_links:
        return (None, 0.0, len(hosts))
    host, n = Counter(hosts).most_common(1)[0]
    share = n / float(len(hosts))
    return ((host, share, len(hosts)) if share >= threshold
            else (None, share, len(hosts)))


def badge_hit(readme, slug=None):
    """Predicate 3 — a licence badge served as a remote image off a non-badge host.

    A real badge is a shields.io query of the repository; a forged one is a picture
    the operator uploaded.  Returns the offending image URLs.
    """
    out = []
    for url in IMG_RE.findall(readme or ""):
        host = _strip_www(_host(url))
        if not host or host in [_strip_www(x) for x in BADGE_HOSTS]:
            continue
        if is_self_host(host, slug) or is_local_host(host):
            continue
        if LICENSE_BADGE_RE.search(url):
            out.append(url)
    return sorted(set(out))


def coldness_hit(stars, forks, days_since_push):
    """Predicate 4 — CORROBORATING ONLY.  Never fires on its own.

    0 stars and 0 forks and pushed in the last 7 days.  p238 published genuine rows
    at 0 stars, so this is deliberately not a filter.
    """
    try:
        stars = int(stars)
        forks = int(forks)
    except (TypeError, ValueError):
        return False
    if days_since_push is None:
        return False
    try:
        days = float(days_since_push)
    except (TypeError, ValueError):
        return False
    return stars == 0 and forks == 0 and days <= 7


def classify(name, readme, stars=None, forks=None, days_since_push=None):
    """Return (verdict, reasons).

    LURE     — 2+ of the three substantive predicates fire.
    SUSPECT  — exactly 1 substantive predicate fires.
    CLEAR    — none fires.

    Coldness is recorded in `reasons` but is never counted toward the verdict, so a
    genuine new 0-star project is never downgraded by its newness alone.
    """
    reasons = []
    names = name_hit(name)
    if names:
        reasons.append("NAME: release-channel word(s) %s in repository name" % ", ".join(names))
    host, share, total = funnel_hit(readme, name)
    if host:
        reasons.append("FUNNEL: %d%% of %d external links point at %s"
                       % (round(share * 100), total, host))
    badges = badge_hit(readme, name)
    if badges:
        reasons.append("BADGE: licence badge is a remote image off-platform: %s" % badges[0])
    substantive = sum(1 for x in (names, host, badges) if x)
    if coldness_hit(stars, forks, days_since_push):
        reasons.append("COLDNESS (corroborating only): 0 stars, 0 forks, pushed <=7d ago")
    verdict = "LURE" if substantive >= 2 else ("SUSPECT" if substantive == 1 else "CLEAR")
    return verdict, reasons


def main(argv):
    if len(argv) >= 2 and argv[1] == "--selftest":
        import test_lure_signature  # noqa: F401  (kept adjacent; see test file)
        return 0
    if len(argv) < 3:
        sys.stderr.write(__doc__.rsplit("usage:", 1)[-1])
        return 2
    name, path = argv[1], argv[2]
    stars = argv[3] if len(argv) > 3 else None
    forks = argv[4] if len(argv) > 4 else None
    days = argv[5] if len(argv) > 5 else None
    if not os.path.exists(path):
        sys.stderr.write("no such README: %s\n" % path)
        return 2
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        readme = fh.read()
    verdict, reasons = classify(name, readme, stars, forks, days)
    print("%s\t%s" % (verdict, name))
    for r in reasons:
        print("  - %s" % r)
    return 0 if verdict == "CLEAR" else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
