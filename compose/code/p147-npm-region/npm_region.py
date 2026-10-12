"""p147-npm-region -- `ACTION EK`: can an npm row be placed without a git tree?

`T59` found that **16 of 35** traversing instruments on this shelf read only
`git ls-tree`/`ls-files`, and that **the entire region-placement lane is among them**. A
published npm package is not a git tree, so this shelf's **8 npm rows are structurally
unplaceable on the region axis** -- which is a gap in the instrument, not in the evidence.

> 🔴 **`ACTION EK`** -- can any npm row be region-placed by **non-git** evidence?

The commit-timezone channel (`p142-origin-census`) needs history and there is none in a
tarball. 🟢 **What a tarball does carry** is the shipped payload, and `P144-V` already
settled which evidence wins when two channels disagree:

> *"`ruud0/aula-virtual-mcp` → EMEA (Spain) on `server.py:19`'s hardcoded
> `BASE_URL = "https://aula-virtual.unav.edu"` -- Universidad de Navarra. The author
> channel disagrees and is weaker: `+0200` in May, `-0400` in September. The institution is
> where it deploys; the author is wherever they were sitting."*

🔵 **That rule needs no git.** This probe applies it to the tarball:

| channel | strength | why |
|---|---|---|
| hardcoded institution host in the payload | 🟢 **strongest** | where the server is pointed, committed as code |
| ccTLD in any payload URL | 🟡 **a lead** | a `.br` in a comment is weaker than a `BASE_URL` |
| a bare `.edu` | 🔴 **weakest national signal** | grandfathered non-US registrations exist -- see `GRANDFATHERED_EDU` |
| `homepage` / `repository` host | 🟡 **a lead** | the publisher's own site, not the deployment |
| `author` email domain | 🔴 **weakest** | `P144-V`'s losing channel, carried for contrast |

🔴 **A ccTLD is not a region on its own.** `.io` and `.ai` are sold worldwide, `.ch` is not,
and the map here holds only the ccTLDs that are in fact restricted or overwhelmingly
national. 🟢 **Rows with no national evidence are returned `UNPLACED`**, which is the
answer `ACTION EK` is entitled to and is not the same as `Global`.

## 🔴 Three false positives this probe produced before publication

Its first run "placed" two rows on `moodle.example.edu` and `d2l.myschool.edu`, and its
second still placed one on `moodle.your-university.edu`. 🔴 **All three are sample values
out of an `*.example.json` or a README config block, and all three failed in the
reassuring direction** -- a placement looks like progress on the region axis, which is this
shelf's declared weakest column. 🟢 **The vocabulary is now token-based and split on `-` as
well as `.`**, and each of the three is pinned as a test.

    python3 npm_region.py <extracted-package-root>...
    python3 test_npm_region.py        # 15 tests, authored fixtures, offline
"""

import json
import os
import re
import sys

# A ccTLD -> region map restricted to suffixes that are nationally bound in practice.
# 🔴 Generic and repurposed suffixes (.io .ai .co .me .tv .cc .to) are deliberately absent.
CCTLD = {
    "br": "LATAM", "ar": "LATAM", "mx": "LATAM", "cl": "LATAM", "pe": "LATAM",
    "uy": "LATAM", "py": "LATAM", "bo": "LATAM", "ec": "LATAM", "ve": "LATAM",
    "gt": "LATAM", "cr": "LATAM", "pa": "LATAM", "do": "LATAM", "cu": "LATAM",
    "es": "EMEA", "pt": "EMEA", "fr": "EMEA", "de": "EMEA", "ch": "EMEA",
    "at": "EMEA", "nl": "EMEA", "be": "EMEA", "it": "EMEA", "pl": "EMEA",
    "cz": "EMEA", "sk": "EMEA", "hu": "EMEA", "ro": "EMEA", "gr": "EMEA",
    "se": "EMEA", "no": "EMEA", "dk": "EMEA", "fi": "EMEA", "ie": "EMEA",
    "uk": "EMEA", "za": "EMEA", "ng": "EMEA", "ke": "EMEA", "eg": "EMEA",
    "ma": "EMEA", "tr": "EMEA", "il": "EMEA", "ae": "EMEA", "sa": "EMEA",
    "ru": "EMEA", "ua": "EMEA", "si": "EMEA", "hr": "EMEA", "rs": "EMEA",
    "bg": "EMEA", "lt": "EMEA", "lv": "EMEA", "ee": "EMEA",
    "in": "APAC", "cn": "APAC", "jp": "APAC", "kr": "APAC", "tw": "APAC",
    "hk": "APAC", "sg": "APAC", "my": "APAC", "th": "APAC", "vn": "APAC",
    "ph": "APAC", "id": "APAC", "au": "APAC", "nz": "APAC", "pk": "APAC",
    "bd": "APAC", "lk": "APAC", "np": "APAC",
    "us": "North America", "ca": "North America",
}
# Academic second-level labels. An `.edu` is US by registry policy; `ac.<cc>` and
# `edu.<cc>` are the national academic namespaces.
ACADEMIC = re.compile(r"(?:^|\.)(?:ac|edu)\.([a-z]{2})$")

# 🔴 A bare `.edu` is NOT a US signal. EDUCAUSE restricted the TLD to US institutions in
# 2001 and GRANDFATHERED the non-US registrations already held, so the suffix carries a
# registration date rather than a country. 🔴 **This shelf contains a counterexample the KB
# itself placed the other way**: `P144-V` placed `ruud0/aula-virtual-mcp` as **EMEA
# (Spain)** on `BASE_URL = "https://aula-virtual.unav.edu"` -- Universidad de Navarra,
# Pamplona. A rule reading `.edu` as North America contradicts a standing placement.
#
# 🔵 So `.edu` is demoted to a LEAD: it places a row only when nothing stronger exists, it
# is reported with its own weak `how`, and the known grandfathered domains are refused
# outright. 🔴 **This list is not complete and cannot be** -- it holds the ones this shelf
# has met.
GRANDFATHERED_EDU = {
    "unav.edu",          # Universidad de Navarra, Spain -- `P144-V`
    "ie.edu",            # IE University, Spain
    "esade.edu",         # ESADE, Spain
    "iese.edu",          # IESE Business School, Spain
    "unicamp.edu",       # UNICAMP, Brazil
    "cst.edu.cn",        # kept for shape; the `edu.<cc>` branch already handles it
}

URL = re.compile(r"https?://([A-Za-z0-9.\-]+)")
# A host committed as the server's target, not merely mentioned.
BASE_ASSIGN = re.compile(
    r"""(?ix)
    \b(?:BASE_URL|BASEURL|API_URL|API_BASE|MOODLE_URL|CANVAS_URL|LMS_URL|
       INSTANCE_URL|SITE_URL|HOST|ENDPOINT|DOMAIN)\b
    \s*[:=]\s*
    ["'`]?\s*(?:https?://)?([A-Za-z0-9.\-]+\.[A-Za-z]{2,})""")

SRC_EXT = {".js", ".mjs", ".cjs", ".ts", ".tsx", ".py", ".php", ".go", ".json",
           ".md", ".txt", ".env", ".example", ".yml", ".yaml", ".toml"}

# 🔴 A placeholder host carries a real-looking ccTLD and places nothing. The first run of
# this probe "placed" two rows on `moodle.example.edu` and `d2l.myschool.edu`, both out of
# an `*.example.json` -- a false positive in the reassuring direction, found by reading the
# output before publishing it. Any host carrying one of these labels is refused.
PLACEHOLDER_LABEL = {"example", "myschool", "yourschool", "mycollege", "yourcollege",
                     "myuniversity", "youruniversity", "school", "university", "demo",
                     "test", "sample", "placeholder", "changeme", "yourdomain",
                     "mydomain", "institution", "tenant", "foo", "bar", "acme",
                     "my", "your", "our"}

GENERIC = {"localhost", "example.com", "example.org", "github.com", "npmjs.com",
           "registry.npmjs.org", "schema.org", "json-schema.org", "nodejs.org",
           "modelcontextprotocol.io", "anthropic.com", "opensource.org",
           "www.gnu.org", "gnu.org", "www.apache.org", "apache.org", "canvas.instructure.com",
           "instructure.com", "moodle.org", "docs.moodle.org", "www.npmjs.com",
           "creativecommons.org", "spdx.org", "tools.ietf.org", "www.w3.org"}


def region_of_host(host):
    """(region, how) for a host, or (None, None)."""
    host = host.lower().rstrip(".")
    if host in GENERIC or not host:
        return None, None
    # Labels are split on `-` as well as `.`: the second round of this probe still placed
    # `moodle.your-university.edu`, whose placeholder label is hyphenated.
    tokens = {t for label in host.split(".") for t in label.split("-")}
    if tokens & PLACEHOLDER_LABEL:
        return None, None
    m = ACADEMIC.search(host)
    if m:
        cc = m.group(1)
        if cc in CCTLD:
            return CCTLD[cc], "academic ns .%s" % m.group(0).lstrip(".")
    if host.endswith(".edu"):
        for g in GRANDFATHERED_EDU:
            if host == g or host.endswith("." + g):
                return None, None
        return "North America", "bare .edu (LEAD -- grandfathered non-US exist)"
    tld = host.rsplit(".", 1)[-1]
    if tld in CCTLD:
        return CCTLD[tld], "ccTLD .%s" % tld
    return None, None


def payload_files(root):
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in {".git", "node_modules"}]
        for f in files:
            if os.path.splitext(f)[1].lower() in SRC_EXT or f.startswith(".env"):
                yield os.path.join(base, f)


def read(path, limit=400000):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read(limit)
    except OSError:
        return ""


def evidence(root):
    """All four channels, each as a list of (host, region, how, where)."""
    out = {"hardcoded": [], "cctld": [], "publisher": [], "author": []}
    pkg = None
    for base, _d, files in os.walk(root):
        if "package.json" in files:
            pkg = os.path.join(base, "package.json")
            break
    for p in payload_files(root):
        t = read(p)
        rel = os.path.relpath(p, root)
        for m in BASE_ASSIGN.finditer(t):
            host = m.group(1)
            r, how = region_of_host(host)
            if r:
                out["hardcoded"].append((host, r, how, rel))
        for m in URL.finditer(t):
            host = m.group(1)
            r, how = region_of_host(host)
            if r:
                out["cctld"].append((host, r, how, rel))
    if pkg:
        try:
            with open(pkg, encoding="utf-8", errors="replace") as fh:
                meta = json.load(fh)
        except (OSError, ValueError):
            meta = {}
        for key in ("homepage", "repository"):
            v = meta.get(key)
            if isinstance(v, dict):
                v = v.get("url")
            if isinstance(v, str):
                for m in URL.finditer(v):
                    r, how = region_of_host(m.group(1))
                    if r:
                        out["publisher"].append((m.group(1), r, how, key))
        a = meta.get("author")
        if isinstance(a, dict):
            a = a.get("email") or ""
        if isinstance(a, str):
            m = re.search(r"@([A-Za-z0-9.\-]+)", a)
            if m:
                r, how = region_of_host(m.group(1))
                if r:
                    out["author"].append((m.group(1), r, how, "author"))
    return out


def place(root):
    ev = evidence(root)
    for channel in ("hardcoded", "cctld", "publisher", "author"):
        hits = ev[channel]
        if not hits:
            continue
        regions = {h[1] for h in hits}
        if len(regions) == 1:
            r = hits[0]
            return dict(region=r[1], channel=channel, host=r[0], how=r[2], where=r[3],
                        conflict="-")
        best = sorted(regions)
        return dict(region="CONFLICT", channel=channel, host=hits[0][0], how=hits[0][2],
                    where=hits[0][3], conflict="|".join(best))
    return dict(region="UNPLACED", channel="-", host="-", how="-", where="-",
                conflict="-")


COLS = ["subject", "region", "channel", "host", "how", "where", "conflict"]


def main(argv):
    roots = argv[1:]
    if not roots:
        print(__doc__)
        return 2
    print("\t".join(COLS))
    placed = 0
    for root in roots:
        root = root.rstrip("/")
        r = place(root)
        r["subject"] = os.path.basename(root)
        if r["region"] not in ("UNPLACED", "CONFLICT"):
            placed += 1
        print("\t".join(str(r[c]) for c in COLS))
    sys.stderr.write("\n# %d of %d row(s) placed by non-git evidence\n"
                     % (placed, len(roots)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
