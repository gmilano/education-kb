"""p143-cctld-url-context -- `ACTION DN`: close the four-country hole.

p142's `americas.py` excluded four ccTLDs outright because each is a homograph of a
filename extension that occurs in ordinary source:

    .py  Paraguay           -- Python          (`scraper.py`)
    .do  Dominican Republic -- Struts/JSP      (`logar.do`, and SIGAA itself uses it)
    .cu  Cuba               -- CUDA
    .cl  Chile              -- OpenCL

🔴 **The cost was declared: this KB could not place a repository in Paraguay, the
Dominican Republic, Cuba or Chile at all.** On a LATAM question that is the largest hole
p142 opened, and Chile in particular matters -- it is the one LATAM country this KB
already cites a national AI policy for.

`ACTION DN` registered the fix: re-admit the four behind a **URL-context requirement**,
then re-run the 19-row eligible population.

🔴 **Falsifier as registered: refuted if requiring URL context loses any of the 16 rows
already placed** -- which would mean the two rules cannot both hold and the homograph
exclusion must stand as a permanent limit.

## The URL-context rule, stated exactly

A host bearing one of the four restricted ccTLDs is admitted ONLY when the matched text
is immediately preceded by `://` or by `www.`. Everything else about p142's booking rule
is unchanged: >= 3 labels, no placeholders, tracked source only, no `node_modules` or
lockfiles, and a row is booked only when every country-bearing host agrees on ONE region.

🔵 **Why this is the right discriminator and not just a tighter one.** `import scraper.py`
and `response.redirect("logar.do")` never carry a scheme. `https://www.una.py/sistema`
does. The scheme is the thing that makes a string an ADDRESS THE CODE MUST REACH, which
is exactly `T29`'s condition -- so the rule is not a heuristic bolted on, it is `T29`
applied literally to the four tokens that needed it.

🔴 **The 15 unrestricted ccTLDs keep p142's rule and do NOT require URL context**, because
`sigaa.ufpi.br` is unambiguous without one and requiring a scheme would drop it. That
asymmetry is deliberate and is the whole content of this probe.

Run: python3 -I cctld_urlctx.py subject=clone=offset ...
"""

import os
import re
import subprocess
import sys

LATAM_TLD = {
    "br": "Brazil", "ar": "Argentina", "pe": "Peru", "mx": "Mexico",
    "uy": "Uruguay", "co": "Colombia", "ec": "Ecuador", "bo": "Bolivia",
    "ve": "Venezuela", "cr": "Costa Rica", "gt": "Guatemala",
    "pa": "Panama", "hn": "Honduras", "ni": "Nicaragua", "sv": "El Salvador",
}
# 🆕 The four re-admitted this pass. Separate dict because they carry an extra condition.
RESTRICTED_TLD = {
    "py": "Paraguay", "do": "Dominican Republic", "cu": "Cuba", "cl": "Chile",
}
NA_TLD = {"ca": "Canada", "us": "United States"}
US_RESTRICTED = {"edu"}
MIN_LABELS = 3

PLACEHOLDER = re.compile(
    r"(^|\.)(example|example\.com|test|localhost|your-?\w*|my\w*|school|institution|"
    r"instance|domain|placeholder|changeme|xxx|foo|bar)(\.|$)", re.IGNORECASE)

ALL_TLDS = sorted(set(LATAM_TLD) | set(RESTRICTED_TLD) | set(NA_TLD) | US_RESTRICTED)

# One pattern for every TLD; the URL-context condition is applied AFTER matching so the
# restricted and unrestricted cases are measured by the same scanner.
HOST = re.compile(
    r"(?:(?P<scheme>://)|(?P<www>\bwww\.))?"
    r"(?P<host>(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.){1,5}"
    r"(?:" + "|".join(ALL_TLDS) + r"))(?![-\w])",
    re.IGNORECASE)

SKIP_DIR = ("/.git/", "/node_modules/", "/vendor/", "/dist/", "/build/", "/target/",
            "/.venv/", "/venv/", "/__pycache__/", "/third_party/")
SKIP_FILE = ("package-lock.json", "yarn.lock", "pnpm-lock.yaml", "poetry.lock",
             "Cargo.lock", "go.sum", "composer.lock", "Gemfile.lock")
TEXT_EXT = (".py", ".js", ".ts", ".tsx", ".jsx", ".go", ".rs", ".java", ".kt", ".rb",
            ".php", ".cs", ".swift", ".sh", ".json", ".yml", ".yaml", ".toml", ".cfg",
            ".ini", ".env", ".example", ".md", ".txt", ".html", ".vue", ".svelte",
            ".gradle", ".xml", ".properties", ".sql", ".tf", ".dart")

NA_LATAM_AMBIGUOUS = {"-0300", "-0400", "-0500", "-0600", "-0700"}


def _git(repo, *a):
    return subprocess.run(["git", "-C", repo, *a], capture_output=True, text=True,
                          timeout=180).stdout


def source_files(repo):
    out = []
    for rel in _git(repo, "ls-tree", "-r", "--name-only", "HEAD").splitlines():
        p = "/" + rel
        if any(s in p for s in SKIP_DIR):
            continue
        if os.path.basename(rel) in SKIP_FILE:
            continue
        if rel.lower().endswith(TEXT_EXT) or "." not in os.path.basename(rel):
            out.append(rel)
    return out


def hosts_in(repo):
    """-> (admitted {host: kind}, rejected_restricted {host: count})

    `kind` is 'PLAIN' for the 15 unrestricted ccTLDs and 'URLCTX' for one of the four
    restricted ones admitted on a scheme or www. prefix.
    """
    admitted, rejected = {}, {}
    for rel in source_files(repo):
        full = os.path.join(repo, rel)
        try:
            if os.path.getsize(full) > 2_000_000:
                continue
            text = open(full, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        for m in HOST.finditer(text):
            h = m.group("host").lower().strip(".")
            if PLACEHOLDER.search(h):
                continue
            if h.count(".") + 1 < MIN_LABELS:
                continue
            tld = h.rsplit(".", 1)[-1]
            has_ctx = bool(m.group("scheme") or m.group("www"))
            if tld in RESTRICTED_TLD:
                if has_ctx:
                    admitted[h] = "URLCTX"
                else:
                    rejected[h] = rejected.get(h, 0) + 1
            else:
                admitted.setdefault(h, "PLAIN")
    return admitted, rejected


def classify(hosts):
    latam, na, edu = {}, {}, []
    for h in hosts:
        tld = h.rsplit(".", 1)[-1]
        if tld in LATAM_TLD:
            latam.setdefault(LATAM_TLD[tld], []).append(h)
        elif tld in RESTRICTED_TLD:
            latam.setdefault(RESTRICTED_TLD[tld], []).append(h)
        elif tld in NA_TLD:
            na.setdefault(NA_TLD[tld], []).append(h)
        elif tld in US_RESTRICTED:
            edu.append(h)
    return latam, na, edu


COLS = ["subject", "offset", "eligible", "region", "evidence_kind", "countries",
        "urlctx_hosts", "rejected_no_urlctx", "note"]


def row(subject, clone, offset):
    if not os.path.isdir(os.path.join(clone, ".git")):
        return dict(zip(COLS, [subject, offset, "NO", "UNMAPPED", "NO_CLONE",
                               "-", "-", "-", "no readable clone"]))
    if offset not in NA_LATAM_AMBIGUOUS:
        return dict(zip(COLS, [subject, offset or "-", "NO", "NOT_ELIGIBLE", "-",
                               "-", "-", "-",
                               "offset not ambiguous between North America and LATAM"]))
    admitted, rejected = hosts_in(clone)
    latam, na, edu = classify(admitted)
    urlctx = sorted([h for h, k in admitted.items() if k == "URLCTX"])
    countries = ";".join("%s(%d)" % (c, len(v)) for c, v in
                         sorted(list(latam.items()) + list(na.items()))) or "NONE"
    rej = ",".join("%s x%d" % (h, n) for h, n in sorted(rejected.items())) or "NONE"

    if latam and na:
        reg, kind, note = "UNMAPPED", "SPLIT", "hosts name both candidate regions"
    elif latam:
        reg, kind = "LATAM", ("CCTLD_URLCTX" if urlctx and not
                              [h for h, k in admitted.items() if k == "PLAIN"
                               and h.rsplit(".", 1)[-1] in LATAM_TLD]
                              else "CCTLD_IN_SOURCE")
        note = "every country-bearing host is LATAM: " + ", ".join(sorted(latam))
    elif na:
        reg, kind = "North America", "CCTLD_IN_SOURCE"
        note = "every country-bearing host is North America: " + ", ".join(sorted(na))
    elif edu:
        reg, kind, note = "UNMAPPED", "EDU_ONLY", "only .edu hosts — never booked alone"
    else:
        reg, kind, note = "UNMAPPED", "NO_HOST", "no country-bearing host in source"
    return dict(zip(COLS, [subject, offset, "YES", reg, kind, countries,
                           ",".join(urlctx) or "NONE", rej, note]))


def main(argv):
    rows = []
    for spec in argv:
        p = spec.split("=")
        rows.append(row(p[0], p[1], p[2] if len(p) > 2 else ""))
    print("\t".join(COLS))
    for r in rows:
        print("\t".join(str(r[c]) for c in COLS))

    elig = [r for r in rows if r["eligible"] == "YES"]
    by = {}
    for r in elig:
        by.setdefault(r["region"], []).append(r["subject"])
    print("\n# eligible: %d" % len(elig), file=sys.stderr)
    for reg in ("LATAM", "North America", "UNMAPPED"):
        print("# %-14s %2d  %s" % (reg, len(by.get(reg, [])),
                                   ", ".join(sorted(by.get(reg, []))) or "-"),
              file=sys.stderr)
    newly = [r["subject"] for r in elig if r["evidence_kind"] == "CCTLD_URLCTX"]
    print("#\n# 🆕 rows placed ONLY because a restricted ccTLD was re-admitted: %d  %s"
          % (len(newly), ", ".join(newly) or "-"), file=sys.stderr)
    anyrej = [r for r in elig if r["rejected_no_urlctx"] != "NONE"]
    print("# rows where a restricted ccTLD appeared WITHOUT url context (correctly "
          "refused): %d" % len(anyrej), file=sys.stderr)
    for r in anyrej:
        print("#    %-50s %s" % (r["subject"], r["rejected_no_urlctx"][:110]),
              file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
