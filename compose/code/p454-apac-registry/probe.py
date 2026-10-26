#!/usr/bin/env python3
"""p454 -- Gap 453-D: the institution-registry layer is two regions deep and
three have never been searched. Open and unsearched: Global, and APAC beyond
India (Japan, Indonesia, the Philippines).

Vocabulary follows Gap 453-B's shelf rule verbatim -- prefer a NAMED SYSTEM OF
RECORD over an English common noun, because `pedagogy`, `special-education` and
`vocational` returned 0 % precision over 61 candidates and `kindergarten`
returned an authorization library. Every term below is the proper name of a
national education data system or its identifier:

  Indonesia   Dapodik (Data Pokok Pendidikan), NPSN (school national ID)
  Philippines DepEd, EBEIS/LIS, PSA school ID
  Japan       MEXT, gakko kihon chosa (School Basic Survey), e-Stat
  Global      UIS (UNESCO Institute for Statistics), ISCED

Channel: the public package registries (npm, PyPI, Packagist). The GitHub
search API is NOT used -- this session's scope permits reads of the attached
repositories only, and a repository-discovery search would reach outside it.
That is a SCOPE limit, not the host 403 earlier passes recorded, and it is
stated so a later pass does not re-attribute it.
"""
import json, subprocess, sys, urllib.parse, concurrent.futures as cf

TERMS = {
    "indonesia": ["dapodik", "npsn", "sekolah kemdikbud", "data pokok pendidikan"],
    "philippines": ["deped", "ebeis lis deped", "philippine school id psa"],
    "japan": ["mext school", "gakko kihon chosa", "e-stat school japan"],
    "global": ["unesco uis education", "isced level", "edu-sharing oer"],
}


def sh(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    return r.stdout


def npm(term):
    u = ("https://registry.npmjs.org/-/v1/search?size=20&text="
         + urllib.parse.quote(term))
    try:
        d = json.loads(sh(["curl", "-s", "--max-time", "30", u]))
    except Exception:
        return []
    out = []
    for o in d.get("objects", []):
        p = o["package"]
        out.append(("npm", term, p["name"], p.get("links", {}).get("repository", ""),
                    p.get("description", "")[:110]))
    return out


def pypi(term):
    # PyPI has no JSON search endpoint; the simple index is not searchable
    # either. The sound substitute is the project JSON for an exact name, so a
    # term is probed as a candidate NAME. A miss here is a miss on NAME only
    # and must not be published as "nothing exists".
    out = []
    for cand in {term.replace(" ", "-"), term.split()[0]}:
        u = f"https://pypi.org/pypi/{urllib.parse.quote(cand)}/json"
        body = sh(["curl", "-s", "--max-time", "30", "-w", "\n__C%{http_code}", u])
        if "__C200" not in body:
            continue
        try:
            d = json.loads(body.rsplit("\n__C", 1)[0])
        except Exception:
            continue
        i = d["info"]
        urls = i.get("project_urls") or {}
        repo = next((v for k, v in urls.items()
                     if "github" in str(v).lower() or "gitlab" in str(v).lower()), "")
        out.append(("pypi", term, i["name"], repo,
                    (i.get("summary") or "")[:110]))
    return out


def packagist(term):
    u = ("https://packagist.org/search.json?per_page=15&q="
         + urllib.parse.quote(term))
    try:
        d = json.loads(sh(["curl", "-s", "--max-time", "30", u]))
    except Exception:
        return []
    return [("packagist", term, r["name"], r.get("repository", ""),
             (r.get("description") or "")[:110]) for r in d.get("results", [])]


def main():
    jobs = []
    for leg, terms in TERMS.items():
        for t in terms:
            jobs.append((leg, t))
    rows = []
    with cf.ThreadPoolExecutor(max_workers=6) as ex:
        futs = {}
        for leg, t in jobs:
            for fn in (npm, pypi, packagist):
                futs[ex.submit(fn, t)] = (leg, t, fn.__name__)
        for fu, (leg, t, ch) in futs.items():
            try:
                for r in fu.result():
                    rows.append((leg,) + r)
            except Exception as e:
                print(f"  ERR {leg} {t} {ch}: {e}", file=sys.stderr)

    seen = set()
    print(f"{'leg':12s} {'chan':10s} {'package':38s} {'repo'}")
    n = 0
    for leg, chan, term, name, repo, desc in sorted(rows):
        k = (chan, name)
        if k in seen:
            continue
        seen.add(k)
        n += 1
        print(f"{leg:12s} {chan:10s} {name[:37]:38s} {repo[:58]}")
        print(f"{'':23s} term={term!r} :: {desc}")
    print(f"\n{n} distinct candidates over {len(jobs)} terms x 3 channels", file=sys.stderr)
    for leg in TERMS:
        c = len({(r[1], r[3]) for r in rows if r[0] == leg})
        print(f"  {leg:12s} {c:3d} candidates", file=sys.stderr)


if __name__ == "__main__":
    main()
