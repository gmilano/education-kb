"""p143-vendor-tenancy -- `ACTION DK`: the third host channel.

p142 placed 16 of 19 American-ambiguous rows on hardcoded ccTLD hosts. Three were left
`UNMAPPED`, and one of them for a reason an instrument could fix:
`karkarkins/BlackboardAssistantMCP` reaches `ncat.blackboard.com`, 🔵 **a vendor TENANCY
subdomain, which names an institution exactly and carries no country.**

`ACTION DK` registered: extract `*.blackboard.com`, `*.instructure.com`,
`*.brightspace.com` subdomains across the 44-row population and resolve only where the
subdomain is an institution's own registered abbreviation.

🔴 **Falsifier as registered: refuted if fewer than three ROWS yield a tenancy subdomain
that is not a placeholder** -- which makes this a one-row channel not worth an instrument,
and `ncat` should be hand-noted instead.

## The distinction the channel turns on, and it is not subtle

A string under `blackboard.com` is one of four things, and only the last places anything:

  VENDOR_INFRA   `developer.blackboard.com`, `files.blackboard.com`,
                 `basic-doc-viewer.eu.api.blackboard.com`. 🔴 **The vendor's own estate.**
                 It is the single most common match and it places NOTHING -- it is the
                 same trap as `your-institution.instructure.com`, one layer up.
  PLACEHOLDER    `example.blackboard.com`, `your-instance.blackboard.com`,
                 `school.instructure.com`.
  OPAQUE         `alt-5f0d0e6d23ee0.blackboard.com`. A tenancy, but the label is a hash
                 and names no institution. 🔵 **Reported, never resolved.**
  TENANCY        `ntnu.blackboard.com`, `ncat.blackboard.com`. 🟢 **A single label that is
                 an institution's own abbreviation.**

🔴 **A tenancy label is resolved ONLY against an explicit, hand-checked table in this
file.** There is no inference from the string: `ncat` is North Carolina A&T because that
is what it is, not because a rule derived it. 🔵 **An unrecognised tenancy label is
reported as `TENANCY_UNRESOLVED` and places nothing** -- which is the honest state for a
label this KB has not looked up, and keeps the channel from guessing an institution out
of three letters.

Run: python3 -I tenancy.py subject=clone ...
"""

import os
import re
import subprocess
import sys

VENDOR = r"(?:blackboard|instructure|brightspace|moodlecloud|schoology|canvaslms)"
HOST = re.compile(r"\b([a-z0-9][a-z0-9.-]*)\.(" + VENDOR + r")\.(com|net|org)\b",
                  re.IGNORECASE)

# 🔴 The vendor's own estate. Labels that belong to the VENDOR, not to a customer.
VENDOR_INFRA = {
    "developer", "api", "files", "community", "help", "docs", "doc", "support", "www",
    "status", "login", "content", "learn", "saas", "static", "cdn", "assets", "public",
    "app", "apps", "portal", "sandbox", "test", "demo", "training", "partner",
    "partners", "about", "blog", "news", "events", "library", "behind",
}
PLACEHOLDER_LABEL = re.compile(
    r"^(example|examples|your[-_]?\w*|my[-_]?\w*|school|schools|institution|"
    r"instance|university|college|domain|placeholder|changeme|xxx+|foo|bar|test\d*|"
    r"sample|tenant|customer|client|site|yourschool|yourdomain)$", re.IGNORECASE)
# `alt-5f0d0e6d23ee0` / long hex strings: a real tenancy whose label names nobody.
OPAQUE_LABEL = re.compile(r"^(alt-)?[0-9a-f]{10,}$", re.IGNORECASE)

# 🔴 Hand-checked, one entry per label this KB has actually looked up. NOT a heuristic.
TENANCY_INSTITUTION = {
    "ntnu": ("Norwegian University of Science and Technology", "Norway", "EMEA"),
    "ncat": ("North Carolina A&T State University", "United States", "North America"),
}

SKIP_DIR = ("/.git/", "/node_modules/", "/vendor/", "/dist/", "/build/", "/target/",
            "/.venv/", "/venv/", "/__pycache__/", "/third_party/")
SKIP_FILE = ("package-lock.json", "yarn.lock", "pnpm-lock.yaml", "poetry.lock",
             "Cargo.lock", "go.sum", "composer.lock", "Gemfile.lock")
TEXT_EXT = (".py", ".js", ".ts", ".tsx", ".jsx", ".go", ".rs", ".java", ".kt", ".rb",
            ".php", ".cs", ".swift", ".sh", ".json", ".yml", ".yaml", ".toml", ".cfg",
            ".ini", ".env", ".example", ".md", ".txt", ".html", ".vue", ".svelte",
            ".gradle", ".xml", ".properties", ".sql", ".tf", ".dart")


def source_files(repo):
    out = []
    listing = subprocess.run(["git", "-C", repo, "ls-tree", "-r", "--name-only", "HEAD"],
                             capture_output=True, text=True, timeout=180).stdout
    for rel in listing.splitlines():
        p = "/" + rel
        if any(s in p for s in SKIP_DIR):
            continue
        if os.path.basename(rel) in SKIP_FILE:
            continue
        if rel.lower().endswith(TEXT_EXT) or "." not in os.path.basename(rel):
            out.append(rel)
    return out


def classify_label(label):
    """-> (class, note). `label` is everything left of the vendor domain."""
    if "." in label:
        # multi-label: vendor infrastructure or a regional shard, never a tenancy
        return "VENDOR_INFRA", "multi-label host under the vendor domain"
    low = label.lower()
    if PLACEHOLDER_LABEL.match(low):
        return "PLACEHOLDER", "documentation placeholder"
    if OPAQUE_LABEL.match(low):
        return "OPAQUE", "tenancy whose label is a hash and names no institution"
    if low in VENDOR_INFRA:
        return "VENDOR_INFRA", "the vendor's own estate"
    if low in TENANCY_INSTITUTION:
        return "TENANCY", "resolved against the hand-checked table"
    return "TENANCY_UNRESOLVED", "single-label tenancy this KB has not looked up"


def scan(repo):
    """-> {host: (vendor, label, cls, note, [files])}"""
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
            label, vendor = m.group(1).lower(), m.group(2).lower()
            host = m.group(0).lower()
            cls, note = classify_label(label)
            e = found.setdefault(host, [vendor, label, cls, note, set()])
            e[4].add(rel)
    return found


COLS = ["subject", "tenancy_hosts", "institution", "country", "region",
         "vendor_infra", "placeholder", "opaque", "unresolved", "verdict"]


def row(subject, repo):
    if not os.path.isdir(os.path.join(repo, ".git")):
        return dict(zip(COLS, [subject] + ["-"] * 8 + ["NO_CLONE"]))
    found = scan(repo)
    ten, infra, ph, op, unres = [], [], [], [], []
    for host, (_v, label, cls, _n, _f) in sorted(found.items()):
        {"TENANCY": ten, "VENDOR_INFRA": infra, "PLACEHOLDER": ph,
         "OPAQUE": op, "TENANCY_UNRESOLVED": unres}[cls].append((host, label))
    insts = sorted({TENANCY_INSTITUTION[l][0] for _h, l in ten})
    ctys = sorted({TENANCY_INSTITUTION[l][1] for _h, l in ten})
    regs = sorted({TENANCY_INSTITUTION[l][2] for _h, l in ten})
    if not found:
        verdict = "NO_VENDOR_HOST"
    elif ten and len(regs) == 1:
        verdict = "PLACED_" + regs[0].replace(" ", "_").upper()
    elif ten:
        verdict = "SPLIT — tenancies name more than one region"
    elif unres:
        verdict = "TENANCY_UNRESOLVED"
    else:
        verdict = "VENDOR_HOST_ONLY — places nothing"
    return dict(zip(COLS, [
        subject,
        ",".join(h for h, _l in ten) or "NONE",
        "; ".join(insts) or "-", "; ".join(ctys) or "-",
        regs[0] if len(regs) == 1 else ("SPLIT" if regs else "-"),
        ",".join(h for h, _l in infra) or "NONE",
        ",".join(h for h, _l in ph) or "NONE",
        ",".join(h for h, _l in op) or "NONE",
        ",".join(h for h, _l in unres) or "NONE",
        verdict]))


def main(argv):
    rows = []
    for spec in argv:
        p = spec.split("=")
        rows.append(row(p[0], p[1]))
    print("\t".join(COLS))
    for r in rows:
        print("\t".join(str(r[c]) for c in COLS))

    withvendor = [r for r in rows if r["verdict"] != "NO_VENDOR_HOST"
                  and r["verdict"] != "NO_CLONE"]
    placed = [r for r in rows if r["verdict"].startswith("PLACED_")]
    unres = [r for r in rows if r["tenancy_hosts"] == "NONE"
             and r["unresolved"] != "NONE" and r["unresolved"] != "-"]
    infra_only = [r for r in rows if r["verdict"].startswith("VENDOR_HOST_ONLY")]
    print("\n# rows scanned                        : %d" % len(rows), file=sys.stderr)
    print("# rows with ANY vendor-domain host     : %d" % len(withvendor),
          file=sys.stderr)
    print("# 🟢 rows PLACED by a resolved tenancy  : %d" % len(placed), file=sys.stderr)
    for r in placed:
        print("#      %-46s %-22s %s" % (r["subject"], r["tenancy_hosts"],
                                         r["region"]), file=sys.stderr)
    print("# rows with an UNRESOLVED tenancy label: %d" % len(unres), file=sys.stderr)
    for r in unres:
        print("#      %-46s %s" % (r["subject"], r["unresolved"]), file=sys.stderr)
    print("# 🔴 rows whose only vendor hosts are the VENDOR'S OWN: %d" % len(infra_only),
          file=sys.stderr)
    for r in infra_only:
        print("#      %-46s %s" % (r["subject"], r["vendor_infra"][:80]),
              file=sys.stderr)
    print("#\n# FALSIFIER: registered as 'fewer than three rows yield a non-placeholder "
          "tenancy'", file=sys.stderr)
    nonph = len(placed) + len(unres)
    print("# rows yielding a non-placeholder tenancy subdomain: %d  => %s"
          % (nonph, "FALSIFIER SILENT" if nonph >= 3 else "FALSIFIER FIRES"),
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
