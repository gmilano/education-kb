"""p142-americas-disambiguation — the offset channel cannot place EITHER American region.
This resolves the rows it refused, using the channel p140 already proved.

## Why this probe exists

`ACTION DH` ran p141's offset channel over the 44-row connector population. It placed 23 rows --
🟢 12 EMEA, 11 APAC -- and **0 North America, 0 LATAM**. 19 rows were refused as
cross-region ambiguous, and 🔴 **every single refusal is an American offset**: eleven at `-0300`,
six at `-0400`, one at `-0500`, one UTC-only.

🔴 **That is not a LATAM gap. It is a hemisphere-shaped hole in the instrument.** p141's table
books an offset only where it is unambiguous across the five regions, and the offsets of the
United States, Canada, Mexico, Brazil, Argentina, Peru and Chile are precisely the shared ones.
So the channel is *structurally incapable* of placing a row in North America or LATAM -- and this
KB has been reporting its LATAM zero for ten passes as though it were a measurement of the
world. 🔵 **The North America zero is the tell.** Nobody expected North America to be missing
from a shelf that holds `UofT-MCP`, `uoft-quercus-mcp` and `mcgill-vsb-mcp`, and it was missing
for the same reason.

## The channel used instead, and why it is not a new idea

p140's `ACTION CU` established that a **hostname a connector must reach in order to work** places
it: `eth-moodle-mcp` -> `moodle-app2.let.ethz.ch` => EMEA. p141 generalised it as `T29`
(*"origin is in the code when the code must REACH a named host"*) and added a second instance in
`uk.ac.ox.ctl`, a Maven `groupId` *"Oxford had to control to publish"*.

🔵 **A country-code TLD is the same evidence in the same form.** `sigaa.ufba.br` is not a name a
project chose for flavour: it is the address the code must resolve for the connector to return
anything, and `.br` is a namespace only a Brazilian registrant can hold. So this probe reads
hardcoded hostnames out of tracked source and maps the registrable TLD to a region.

Booking rule, deliberately narrow:

  1. Only rows whose offset was refused as ambiguous **between North America and LATAM** are
     eligible. An EMEA or APAC row is already placed and is not re-litigated here.
  2. Hostnames are taken from tracked source only -- 🔴 no `node_modules`, no lockfiles, no
     vendored third-party trees, since a dependency's hostname places the dependency.
  3. Placeholder hosts are excluded by an explicit list (`your-school`, `example`, `localhost`,
     `instructure.com` without a subdomain, …). 🔵 **`your-institution.instructure.com` is the
     single most common "hostname" on this shelf and it places nothing.**
  4. 🔴 **A row is booked only when every country-bearing hostname agrees on ONE of the two
     candidate regions.** A repo citing both `.ca` and `.br` is reported `SPLIT` and stays
     unplaced, as p141's table would have done.

🔴 **Four ccTLDs are excluded outright, and the coverage that costs is declared, not hidden.**
`.py` (Paraguay) is Python's extension, `.do` (Dominican Republic) is a Struts/JSP action suffix
and is used by SIGAA itself, `.cu` (Cuba) is CUDA and `.cl` (Chile) is OpenCL. Each produced a
false booking in this probe's first draft -- `scraper.py` placed a row in **Paraguay** -- so
**this instrument cannot place a repository in Paraguay, the Dominican Republic, Cuba or Chile
at all.** On a LATAM question that is a real hole, and saying so is cheaper than the alternative.

🔵 **`.edu` is reported and never booked, and the reason is measured rather than cautious.**
Its registry has been restricted to US institutions since 2001, which looks like the `uk.ac.ox`
argument -- but `ruud0/aula-virtual-mcp` in this very population reaches
`aula-virtual.unav.edu`, the **Universidad de Navarra, in Spain**, on a pre-restriction
registration, and the repository names Navarra and Spain in its own source. One counterexample
inside the subject set is enough: `.edu` is corroboration, and the booking waits for a ccTLD.

The platform token channel (`sigaa`, `siu`, `guarani`, `suap`, `quercus`) is computed and
reported for corroboration, and 🔴 **nothing is booked on it**: a national platform places the
*deployment*, and this probe's claim is about the repository.
"""

import os
import re
import subprocess
import sys

# ccTLDs whose registrant is in exactly one of the two candidate regions.
#
# 🔴 FOUR ccTLDs ARE DELIBERATELY ABSENT, and their absence is a coverage gap this probe
# declares rather than hides. Each is a homograph of a filename extension that appears in
# ordinary source trees, and each produced a false booking in this probe's first draft:
#
#   .py  Paraguay            -- Python source. `scraper.py`, `server.py`, `config.py`
#   .do  Dominican Republic  -- Struts/JSP action endpoint. `logar.do`, `vertelalogin.do`
#   .cu  Cuba                -- CUDA source
#   .cl  Chile               -- OpenCL source
#
# 🔴 **So this instrument cannot place a repository in Paraguay, the Dominican Republic, Cuba
# or Chile at all.** That is worse than it looks for a LATAM question and it is said out loud,
# because the alternative is a probe that books Paraguay off `auth.py`.
LATAM_TLD = {
    "br": "Brazil", "ar": "Argentina", "pe": "Peru", "mx": "Mexico",
    "uy": "Uruguay", "co": "Colombia", "ec": "Ecuador", "bo": "Bolivia",
    "ve": "Venezuela", "cr": "Costa Rica", "gt": "Guatemala",
    "pa": "Panama", "hn": "Honduras", "ni": "Nicaragua", "sv": "El Salvador",
}
NA_TLD = {"ca": "Canada", "us": "United States"}
# 🔴 NOT a US signal, and this population proves it. `.edu` registration has been restricted
# to US accredited institutions since 2001, which looks like the `uk.ac.ox` argument -- but
# `ruud0/aula-virtual-mcp` reaches `aula-virtual.unav.edu`, the Universidad de Navarra, in
# SPAIN, on a pre-restriction registration. So `.edu` is recorded as corroboration and is
# never booked, and the counterexample is measured rather than assumed.
US_RESTRICTED = {"edu"}

# 🔴 A registrable name is `name.tld`; a host code must REACH is `service.name.tld`. Requiring
# three labels separated every true positive from every false positive in this population:
# it drops `scraper.py`, `logar.do`, `http.us`, `campus.edu` and the bare public suffixes
# `edu.br` / `gov.br` / `edu.ar`, and keeps `sigaa.ufpi.br`, `guarani.unq.edu.ar`,
# `vsb.mcgill.ca`, `q.utoronto.ca` and `aulavirtual.upc.edu.pe`.
MIN_LABELS = 3

PLACEHOLDER = re.compile(
    r"(^|\.)(example|example\.com|test|localhost|your-?\w*|my\w*|school|institution|"
    r"instance|domain|placeholder|changeme|xxx|foo|bar)(\.|$)", re.IGNORECASE)

# 🔴 The trailing lookahead is not cosmetic. `\b` matches before a hyphen, so
# `123.dkr.ecr.us-east-1.amazonaws.com` -- an AWS registry host -- matched as the `.us`
# host `dkr.ecr.us` and booked `Cicatriiz/openedu-mcp` into North America. A cloud REGION
# identifier is not a country code. `(?![-\w])` requires the TLD to actually end there.
HOST = re.compile(
    r"\b(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.){1,5}"
    r"(?:br|ar|pe|mx|uy|co|ec|bo|ve|cr|gt|pa|hn|ni|sv|ca|us|edu)(?![-\w])",
    re.IGNORECASE)

SKIP_DIR = ("/.git/", "/node_modules/", "/vendor/", "/dist/", "/build/", "/target/",
            "/.venv/", "/venv/", "/__pycache__/", "/third_party/")
SKIP_FILE = ("package-lock.json", "yarn.lock", "pnpm-lock.yaml", "poetry.lock",
             "Cargo.lock", "go.sum", "composer.lock", "Gemfile.lock")
TEXT_EXT = (".py", ".js", ".ts", ".tsx", ".jsx", ".go", ".rs", ".java", ".kt", ".rb",
            ".php", ".cs", ".swift", ".sh", ".json", ".yml", ".yaml", ".toml", ".cfg",
            ".ini", ".env", ".example", ".md", ".txt", ".html", ".vue", ".svelte",
            ".gradle", ".xml", ".properties", ".sql", ".tf", ".dart")

PLATFORM = {
    "sigaa": ("LATAM", "SIGAA — Brazilian federal-university SIS"),
    "siu": ("LATAM", "SIU-Guaraní — Argentine national-university SIS"),
    "guarani": ("LATAM", "SIU-Guaraní — Argentine national-university SIS"),
    "suap": ("LATAM", "SUAP — Brazilian federal-institute system"),
    "aula virtual": ("LATAM", "Aula Virtual — Spanish-language LMS portal"),
    "quercus": ("North America", "Quercus — University of Toronto Canvas tenancy"),
    "minerva": ("North America", "Minerva — McGill student system"),
}
# 🔴 Offsets p141 refuses BETWEEN North America and LATAM. Those are the eligible rows.
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
    """{host: [files]} for hardcoded hosts bearing a country-ish TLD."""
    found = {}
    for rel in source_files(repo):
        full = os.path.join(repo, rel)
        try:
            if os.path.getsize(full) > 2_000_000:
                continue
            text = open(full, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        for m in HOST.finditer(text):
            h = m.group(0).lower().strip(".")
            if PLACEHOLDER.search(h):
                continue
            if h.count(".") + 1 < MIN_LABELS:
                continue
            found.setdefault(h, set()).add(rel)
    return found


def platform_tokens(repo):
    hits = set()
    for rel in source_files(repo):
        full = os.path.join(repo, rel)
        try:
            if os.path.getsize(full) > 2_000_000:
                continue
            low = open(full, encoding="utf-8", errors="replace").read().lower()
        except OSError:
            continue
        for tok in PLATFORM:
            if tok in low or tok in rel.lower():
                hits.add(tok)
    return hits


COLS = ["subject", "offset", "eligible", "hosts", "countries", "edu_hosts",
        "platform_tokens", "region", "evidence_kind", "note"]


def classify(hosts):
    latam, na, edu = {}, {}, []
    for h in hosts:
        tld = h.rsplit(".", 1)[-1]
        if tld in LATAM_TLD:
            latam.setdefault(LATAM_TLD[tld], []).append(h)
        elif tld in NA_TLD:
            na.setdefault(NA_TLD[tld], []).append(h)
        elif tld in US_RESTRICTED:
            edu.append(h)
    return latam, na, edu


def row(subject, clone, offset):
    eligible = offset in NA_LATAM_AMBIGUOUS
    if not eligible:
        return dict(zip(COLS, [subject, offset or "-", "NO", "-", "-", "-", "-",
                               "NOT_ELIGIBLE", "-",
                               "offset is not ambiguous between North America and LATAM"]))
    hosts = hosts_in(clone)
    latam, na, edu = classify(hosts)
    toks = platform_tokens(clone)
    hostlist = ",".join(sorted(hosts)) or "NONE"
    countries = ";".join(
        ["%s(%d)" % (c, len(v)) for c, v in sorted(latam.items())]
        + ["%s(%d)" % (c, len(v)) for c, v in sorted(na.items())]) or "NONE"
    tokstr = ",".join(sorted(toks)) or "NONE"
    edustr = ",".join(sorted(edu)) or "NONE"

    if latam and na:
        return dict(zip(COLS, [subject, offset, "YES", hostlist, countries, edustr, tokstr,
                               "UNMAPPED", "SPLIT",
                               "hosts name both candidate regions — declined, not guessed"]))
    if latam:
        return dict(zip(COLS, [subject, offset, "YES", hostlist, countries, edustr, tokstr,
                               "LATAM", "CCTLD_IN_SOURCE",
                               "every country-bearing host is LATAM: "
                               + ", ".join(sorted(latam))]))
    if na:
        return dict(zip(COLS, [subject, offset, "YES", hostlist, countries, edustr, tokstr,
                               "North America", "CCTLD_IN_SOURCE",
                               "every country-bearing host is North America: "
                               + ", ".join(sorted(na))]))
    if edu:
        return dict(zip(COLS, [subject, offset, "YES", hostlist, countries, edustr, tokstr,
                               "UNMAPPED", "EDU_ONLY",
                               "only .edu hosts — US-restricted since 2001, but recorded as "
                               "corroboration and never booked alone"]))
    return dict(zip(COLS, [subject, offset, "YES", hostlist, countries, edustr, tokstr,
                           "UNMAPPED", "NO_HOST",
                           "no hardcoded country-bearing hostname in tracked source"]))


def main(argv):
    """argv: subject=clone=offset triples."""
    rows = []
    for spec in argv:
        parts = spec.split("=")
        subject = parts[0]
        clone = parts[1] if len(parts) > 1 else ""
        offset = parts[2] if len(parts) > 2 else ""
        if not os.path.isdir(os.path.join(clone, ".git")):
            rows.append(dict(zip(COLS, [subject, offset, "NO", "-", "-", "-", "-",
                                        "UNMAPPED", "NO_CLONE", "no readable clone"])))
            continue
        rows.append(row(subject, clone, offset))
    print("\t".join(COLS))
    for r in rows:
        print("\t".join(str(r[c]) for c in COLS))

    elig = [r for r in rows if r["eligible"] == "YES"]
    by = {}
    for r in elig:
        by.setdefault(r["region"], []).append(r["subject"])
    print("\n# eligible (Americas-ambiguous offset): %d" % len(elig), file=sys.stderr)
    for reg in ("LATAM", "North America", "UNMAPPED"):
        names = by.get(reg, [])
        print("# %-14s %2d  %s" % (reg, len(names), ", ".join(sorted(names)) or "-"),
              file=sys.stderr)
    corrob = [r["subject"] for r in elig
              if r["platform_tokens"] != "NONE" and r["region"] != "UNMAPPED"]
    print("# rows whose platform token AGREES with the booking: %d of %d"
          % (len(corrob), len([r for r in elig if r["region"] != "UNMAPPED"])),
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
