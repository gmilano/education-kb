"""p140-origin-evidence — `ACTION CU`: book a region from evidence that is not a name.

p139 pre-registered this as the hardest of its six actions, and framed the falsifier as a
restatement rather than a refutation:

> **Book ONE region on measured evidence.** Pick a single row and establish its origin
> from something that is not a name: a `pom.xml` `<organization>`, a funding file, an
> institutional email domain in `git log`, a university host in a tool description.
> 🔴 *Refuted if no row on this shelf yields origin evidence of that kind -- in which case
> the nine-pass ownership gap should be restated as "this shelf does not carry origin
> metadata" rather than "this KB has not looked".*

🔵 **The answer is that both halves are true of different layers, and separating them is
the finding.** The npm *metadata* layer carries almost no origin signal: 5 of 8 payloads
declare no author at all and the two that do give a `gmail.com` address. The *code* layer
carries it plainly -- hardcoded institutional hostnames, which an author field cannot fake
into a different country because the server has to reach the real host to work.

So the gap was a failure of looking, at the layer where looking works.

## What counts as origin evidence here

Only artefacts, never names. A package called `eth-moodle-mcp` is a name and proves
nothing; `https://moodle-app2.let.ethz.ch` compiled into its request path is a binding,
because the code does not function pointed anywhere else.

  `HOST_IN_CODE`    an institutional hostname in shipped source or a tool description
  `EMAIL_DOMAIN`    an institutional email domain in package or distribution metadata
  `POM_ORG`         a `<organization>` or `<developers>` organisation in a Maven POM
  `FUNDING`         a funding file naming an institution

Placeholder hosts are excluded explicitly. `moodle.your-university.edu` is documentation,
and counting it would book a region off a worked example -- the exact class of error p139's
`T24` was published to prevent. The exclusion list is data, and the tests pin it.

## Region mapping

A closed vocabulary of five values, as `intel/market.md` requires: `North America`, `EMEA`,
`APAC`, `LATAM`, `Global`. Mapping runs from the domain's registry suffix and a small table
of known institutional domains. 🔴 **A suffix this table does not hold is reported as
`UNMAPPED` rather than guessed** -- a wrong region is worse than a missing one, because the
filter it feeds reads as coverage.
"""

import json
import re
import sys
from pathlib import Path

# Hostnames that are documentation, not deployment. Counting one books a region off a
# worked example -- the exact class of error p139's `T24` was published to prevent.
#
# 🔴 The first draft of this probe used a hand-written list of placeholder hosts and
# BOOKED NORTH AMERICA THREE TIMES off `d2l.myschool.edu`, `school.edu` and
# `moodle.example.edu`. A hand list cannot work: every README invents its own placeholder.
# What distinguishes one is not its spelling but its SHAPE -- a generic noun standing where
# an institution's name belongs. So the rule is structural and the tests pin it.
PLACEHOLDER_LABELS = {
    "example", "examples", "sample", "samples", "test", "testing", "demo", "dev",
    "placeholder", "changeme", "foo", "bar", "baz", "qux",
    "your", "yours", "yourschool", "yourdomain", "youruniversity", "yourcompany",
    "yourmoodle", "yourcanvas", "yourinstance", "yoursite", "yourorg",
    "myschool", "mycompany", "myuniversity", "mymoodle", "mysite", "myorg", "mydomain",
    "school", "schools", "university", "universities", "college", "institution",
    "instance", "domain", "host", "hostname", "site", "server", "company", "org",
    "localhost", "subdomain", "tenant", "customer", "client",
}
# RFC 2606 / RFC 6761 reserved names: never a real deployment.
RESERVED_TLDS = {"example", "invalid", "test", "localhost", "local", "internal"}
IPV4 = re.compile(r"^\d{1,3}(?:\.\d{1,3}){3}$")

# Hosts that are vendor or infrastructure, carrying no origin signal about the AUTHOR.
INFRA_SUFFIXES = (
    "github.com", "githubusercontent.com", "npmjs.com", "npmjs.org", "nodejs.org",
    "json-schema.org", "opensource.org", "apache.org", "gnu.org", "fsf.org",
    "modelcontextprotocol.io", "anthropic.com", "openai.com", "schema.org",
    "w3.org", "pypi.org", "python.org", "instructure.com", "moodle.org",
    "d2l.com", "brightspace.com", "mozilla.org", "typescriptlang.org",
    "registry.npmjs.org", "unpkg.com", "jsdelivr.net", "shields.io",
    "creativecommons.org", "semver.org", "keepachangelog.com", "maven.apache.org",
    "sonatype.org", "oracle.com", "eclipse.org", "readthedocs.io", "readthedocs.org",
)

# Country-code and institutional suffixes -> region. Closed vocabulary.
SUFFIX_REGION = {
    # North America
    ".edu": "North America", ".ca": "North America", ".us": "North America",
    ".gov": "North America",
    # EMEA
    ".ethz.ch": "EMEA", ".ch": "EMEA", ".ac.uk": "EMEA", ".uk": "EMEA",
    ".de": "EMEA", ".fr": "EMEA", ".nl": "EMEA", ".es": "EMEA", ".it": "EMEA",
    ".se": "EMEA", ".no": "EMEA", ".fi": "EMEA", ".dk": "EMEA", ".pl": "EMEA",
    ".pt": "EMEA", ".ie": "EMEA", ".at": "EMEA", ".be": "EMEA", ".cz": "EMEA",
    ".gr": "EMEA", ".tr": "EMEA", ".il": "EMEA", ".ae": "EMEA", ".sa": "EMEA",
    ".za": "EMEA", ".ke": "EMEA", ".ng": "EMEA", ".eu": "EMEA",
    # APAC
    ".cn": "APAC", ".jp": "APAC", ".kr": "APAC", ".in": "APAC", ".au": "APAC",
    ".nz": "APAC", ".sg": "APAC", ".hk": "APAC", ".tw": "APAC", ".vn": "APAC",
    ".id": "APAC", ".my": "APAC", ".th": "APAC", ".ph": "APAC", ".pk": "APAC",
    ".ac.jp": "APAC", ".ac.in": "APAC", ".edu.au": "APAC", ".edu.cn": "APAC",
    # LATAM
    ".br": "LATAM", ".mx": "LATAM", ".ar": "LATAM", ".cl": "LATAM",
    ".co": "LATAM", ".pe": "LATAM", ".uy": "LATAM", ".ec": "LATAM",
    ".cr": "LATAM", ".gt": "LATAM", ".bo": "LATAM", ".py": "LATAM",
    ".ve": "LATAM", ".do": "LATAM", ".pa": "LATAM",
}

# Named institutional domains whose suffix alone would mislead. `axim.org` is a `.org`,
# which maps nowhere; Axim Collaborative is a US non-profit, and that is a fact about the
# organisation rather than about the suffix, so it is recorded here as data.
KNOWN_DOMAINS = {
    "axim.org": ("North America", "Axim Collaborative (US non-profit, Open edX steward)"),
    "ethz.ch": ("EMEA", "ETH Zürich (Switzerland)"),
    "let.ethz.ch": ("EMEA", "ETH Zürich, Lehrentwicklung und -technologie"),
    "safari.ethz.ch": ("EMEA", "ETH Zürich SAFARI course platform"),
    "k-state.edu": ("North America", "Kansas State University"),
    "ksu.edu": ("North America", "Kansas State University"),
    "sakaiproject.org": ("North America", "Sakai / Apereo Foundation (US)"),
    "apereo.org": ("North America", "Apereo Foundation (US)"),
    "imsglobal.org": ("North America", "1EdTech, formerly IMS Global (US)"),
    "1edtech.org": ("North America", "1EdTech (US)"),
    "overhang.io": ("UNMAPPED", "Overhang.IO — `.io` carries no country signal"),
}

# Personal mail hosts: present, but no origin signal.
PERSONAL_MAIL = {
    "gmail.com", "googlemail.com", "outlook.com", "hotmail.com", "yahoo.com",
    "proton.me", "protonmail.com", "icloud.com", "me.com", "qq.com", "163.com",
    "users.noreply.github.com",
}

URL_HOST = re.compile(r"https?://([A-Za-z0-9](?:[A-Za-z0-9.-]*[A-Za-z0-9])?)")
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,})")

TEXT_SUFFIXES = {".js", ".mjs", ".cjs", ".ts", ".mts", ".cts", ".json", ".md",
                 ".txt", ".yml", ".yaml", ".xml", ".cfg", ".toml", ".py"}


def is_infra(host):
    h = host.lower()
    return any(h == s or h.endswith("." + s) for s in INFRA_SUFFIXES)


def is_placeholder(host):
    """True when the host is documentation rather than a deployment.

    Structural, not a spelling list: a placeholder puts a generic noun where an
    institution's name belongs. `d2l.myschool.edu` is one; `moodle-app2.let.ethz.ch`
    is not, and neither is `canvas.ust.hk`.
    """
    h = host.lower().rstrip(".")
    if IPV4.match(h) or "." not in h:
        return True
    labels = h.split(".")
    if labels[-1] in RESERVED_TLDS:
        return True
    for label in labels:
        # `your-university`, `my-school` and `your_org` are the same token as the
        # unhyphenated spelling, so compare on the squashed form too.
        squashed = label.replace("-", "").replace("_", "")
        if label in PLACEHOLDER_LABELS or squashed in PLACEHOLDER_LABELS:
            return True
        if squashed.startswith("your") or squashed.startswith("myown"):
            return True
    return False


def map_domain(domain):
    """(region, note) for a domain, or ('UNMAPPED', reason)."""
    d = domain.lower().rstrip(".")
    if d in KNOWN_DOMAINS:
        return KNOWN_DOMAINS[d]
    for known, val in KNOWN_DOMAINS.items():
        if d.endswith("." + known):
            return val
    # Longest matching suffix wins, so `.ac.uk` beats `.uk` and `.edu.au` beats `.au`.
    best = None
    for suf, region in SUFFIX_REGION.items():
        if d.endswith(suf) and (best is None or len(suf) > len(best[0])):
            best = (suf, region)
    if best:
        return best[1], "suffix %s" % best[0]
    return "UNMAPPED", "no country signal in %r" % d


def scan_payload(pkg_dir):
    """Origin evidence in one extracted payload."""
    hosts, emails = {}, {}
    for p in Path(pkg_dir).rglob("*"):
        if not p.is_file() or p.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if any(part in {"node_modules", ".git"} for part in p.parts):
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        rel = p.name
        for m in URL_HOST.finditer(text):
            h = m.group(1).lower().rstrip(".")
            if is_placeholder(h) or is_infra(h):
                continue
            hosts.setdefault(h, {"count": 0, "files": set()})
            hosts[h]["count"] += 1
            hosts[h]["files"].add(rel)
        for m in EMAIL.finditer(text):
            d = m.group(1).lower()
            if d in PERSONAL_MAIL or is_infra(d) or is_placeholder(d):
                continue
            emails.setdefault(d, {"count": 0, "files": set()})
            emails[d]["count"] += 1
            emails[d]["files"].add(rel)
    return hosts, emails


def evidence_rows(pkg_dir, label=None):
    hosts, emails = scan_payload(pkg_dir)
    label = label or Path(pkg_dir).name
    rows = []
    for host, info in sorted(hosts.items()):
        region, note = map_domain(host)
        rows.append({
            "subject": label, "kind": "HOST_IN_CODE", "evidence": host,
            "occurrences": info["count"], "where": ",".join(sorted(info["files"]))[:70],
            "region": region, "note": note,
        })
    for dom, info in sorted(emails.items()):
        region, note = map_domain(dom)
        rows.append({
            "subject": label, "kind": "EMAIL_DOMAIN", "evidence": dom,
            "occurrences": info["count"], "where": ",".join(sorted(info["files"]))[:70],
            "region": region, "note": note,
        })
    if not rows:
        rows.append({
            "subject": label, "kind": "NONE", "evidence": "-", "occurrences": 0,
            "where": "-", "region": "UNMAPPED",
            "note": "no institutional host or email in payload",
        })
    return rows


COLS = ["subject", "kind", "evidence", "occurrences", "region", "note", "where"]


def main(argv):
    rows = []
    for d in argv:
        rows.extend(evidence_rows(d))
    print("\t".join(COLS))
    for r in rows:
        print("\t".join(str(r[c]) for c in COLS))
    booked = {}
    for r in rows:
        if r["kind"] != "NONE" and r["region"] != "UNMAPPED":
            booked.setdefault(r["region"], set()).add(r["subject"])
    print("\n# regions booked on measured evidence", file=sys.stderr)
    print(json.dumps({k: sorted(v) for k, v in booked.items()}, indent=2), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
