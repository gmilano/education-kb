#!/usr/bin/env python3
"""p332 — the audit p327 prescribed, p331 found still unrun: evidence -> shelf delivery.

p235's `carried_index.py` answers "is this slug on the shelves?" and REFUSES to read
`evidence/` — deliberately, and that exclusion is right: a measurement is not a published
row. But nothing ever asked the symmetric question, which is the one that costs a client
a finding:

    this KB measured a row first-hand. Did it ever reach a shelf?

p331's own worked case: `lti-tool/lti-tool` was measured into
`evidence/p232-new-rows.2026-10-16-p232.tsv` line 17 on 2026-10-16 — MIT, 30 published
versions, marked `unplaced` — and was still absent from every shelf fourteen passes later,
while p330 published the claim that no permissive LTI implementation existed outside Python.
Discovery rate 100%, delivery rate 0%.

This reads the shelf index from p235 rather than rebuilding it, so the two directions can
never disagree about what "carried" means.

    python3 delivery_audit.py             # the report
    python3 delivery_audit.py --tsv       # one row per undelivered slug, ranked
    python3 test_delivery_audit.py        # the controls, offline
"""
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT_DEFAULT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))

# A TSV field that is EXACTLY owner/repo. Anchored: `schemas/lti13/ags` has three segments
# and must not match, `main/LICENSE` has two and is excluded by DENY below.
SLUG_FIELD = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")

# Field-shaped things that are not repositories. Measured against this corpus, not guessed:
# every entry below was a false positive in a real evidence row before it was excluded.
DENY_SECOND = {
    "license", "licence", "license.md", "licence.md", "license.txt", "licence.txt",
    "licenses", "readme.md", "package.json", "setup.py", "pyproject.toml", "copying",
    "notice", "unlicense", "composer.json", "pom.xml", "cargo.toml", "go.mod",
}
DENY_FIRST = {
    "main", "master", "blob", "tree", "raw", "refs", "heads", "tags", "http", "https",
    "npm", "pypi", "maven", "crates", "packagist", "rubygems", "nuget", "docs", "src",
    "lib", "test", "tests", "data", "schemas", "services", "packages", "evidence",
    # this repository's own shelf paths: `repos/trending.md` is a citation, not a row.
    "repos", "agents", "intel", "verticals", "compose", "archive", "api", "bin", "ingest",
}
# `n/a`, `n/m`, `s/n` — the empty-cell spellings this corpus uses. Measured, not guessed:
# `n/a` alone accounted for 205 sightings of a slug named "n/a" before this exclusion.
DENY_PLACEHOLDER = {"n", "s", "y", "na", "nd", "sn"}
# A second segment with a source-file extension is a path, not a repository.
DENY_SECOND_EXT = (".md", ".tsv", ".csv", ".py", ".sh", ".json", ".yaml", ".yml",
                   ".txt", ".lock", ".cfg", ".ini", ".toml")

# Seeded negative controls. `p208-seeded-error-audit/seed.sh` plants deliberately wrong cells
# in a SCRATCH copy of the shelves; `DecoyLex/ltix` is its one invented slug, and it is measured
# into evidence/ 25 times. It must never reach a shelf, so counting it as an undelivered row is
# the audit reporting a planted control as a failure. p332 measured this: before this exclusion
# `DecoyLex/ltix` was the single highest-sighting row in the defect class.
CONTROLS = {"decoylex/ltix"}

PERMISSIVE = ("mit", "apache", "bsd", "isc", "zlib", "mpl-2", "unlicense", "cc0")
COPYLEFT = ("gpl", "agpl", "lgpl", "odbl", "cc by-sa", "cc-by-sa", "eupl", "osl", "sspl")
UNGRANTED = ("no licence", "no license", "unlicensed", "no grant", "none found",
             "no licence file", "no license file", "sin licencia")

# p333 — THE DEFECT THIS BLOCK EXISTS TO STOP. Until p333 every token above was tested with
# a bare `tok in row`, against the WHOLE row. A licence family name is three letters long and
# English is full of them, so the test graded rows on words that are not grants:
#
#   `isc` inside d-ISC-overy, d-ISC-harged, d-ISC-losure   (326 spurious matches)
#   `mit` inside com-MIT-s, com-MIT-tee, per-MIT-ted,      (403 spurious matches)
#         rate_li-MIT, and the owner name d-MIT-ry-viskov
#
# Measured over this repository's own `evidence/` at p333: 610 rows across 259 evidence files
# — 5.7% of every row that matched any permissive token — were graded permissive on an
# embedded substring and nothing else (`evidence/p333-substring-grant-census...tsv`). Two carriers deserve naming. `commits`/`committed` is the ACTIVITY vocabulary p329
# introduced to these shelves, so the measurement added at p329 silently re-graded the grant
# column at p332; and `dmitry-viskov` grades a repository MIT by the maintainer's first name.
# The dangerous direction is real and was found in the wild: the AGPL-3.0 row
# `pdfmathtranslate/pdfmathtranslate`, recorded CORRECTLY as AGPL-3.0 by p154, read back as
# `permissive` because the filename it cites — `api-di(sc)overy-overlap...` — contains `isc`.
#
# 🔵 This KB already held the guard. `compose/code/licence-grant-gate/grant_gate.py:112`
# declares `AMBIGUOUS_WORDS = ("apache", "nginx", "mit", "bsd")` and reasons about exactly this
# ambiguity. It was never applied here — p329's shape again: capability present, not exercised.
#
# The rule: a token counts when it is not preceded by an alphanumeric and not followed by two
# or more letters. The right-hand allowance of ONE letter is deliberate and load-bearing —
# `GPLv3` and `MPL-2.0` are real spellings a stricter boundary would discard, while
# `apachecon`, `mitigation` and `discovery` are not grants.
_TOKEN_RE = {}


def token_present(tok, low):
    """Is `tok` a licence mention in `low`, or a substring of a longer word?"""
    rx = _TOKEN_RE.get(tok)
    if rx is None:
        rx = re.compile(r"(?<![a-z0-9])" + re.escape(tok) + r"(?![a-z]{2})")
        _TOKEN_RE[tok] = rx
    return rx.search(low) is not None


# p333 — the audit's OWN OUTPUT is a derived artefact, not a measurement, and re-reading it is
# how one pass's grade becomes the next pass's evidence. It is also the single largest carrier
# of the substring defect above: 109 of the 610 flipped rows live in
# `p332-delivery-audit.2026-10-20-p332.tsv`, because every row in it cites the evidence
# filename it came from and those filenames carry `disc`, `commit` and friends. Excluded by
# name so the loop cannot close.
DERIVED_EVIDENCE = ("delivery-audit",)

# Dispositions that mean a pass LOOKED and SAID NO. An undelivered row carrying one of these
# is not a delivery failure — it is a recorded refusal, and re-promoting it would be the bug.
REFUSED = ("dead", "archived", "below bar", "below the bar", "not embeddable", "unusable",
           "fork", "downstream", "abandoned", "refused", "reject", "stale", "no grant",
           "unlicensed", "no licence", "no license", "watch list", "descartad", "muerto")
# Dispositions that mean a pass looked and DEFERRED. These are the defect class.
PENDING = ("unplaced", "pending", "unread", "not read", "to place", "sin ubicar", "por leer")


def _load_carried_index():
    """Import p235's module by path. Reuse, not reimplementation: if p235's notion of a
    shelf or its case-folding ever changes, this audit changes with it."""
    path = os.path.join(HERE, "..", "p235-carried-index", "carried_index.py")
    spec = importlib.util.spec_from_file_location("carried_index", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def fold(slug):
    return slug.rstrip(".,)").lower()


def slug_fields(row):
    """Every field of a TSV row that is shaped like, and plausibly is, a repo slug."""
    out = []
    for field in row.split("\t"):
        f = field.strip().strip("`*|").rstrip(".,)")
        if not SLUG_FIELD.match(f):
            continue
        first, second = f.split("/", 1)
        if first.lower() in DENY_FIRST or second.lower() in DENY_SECOND:
            continue
        if first.lower() in DENY_PLACEHOLDER:
            continue
        if second.lower().endswith(DENY_SECOND_EXT):
            continue
        if len(first) < 2 or len(second) < 2:
            continue
        if "." in first:  # a.b/c is a hostname, not an owner
            continue
        if second.lower().endswith(".git"):   # clone-URL spelling, same repository
            f = first + "/" + second[:-4]
        out.append(f)
    return out


def classify_grant(row):
    low = row.lower()
    if any(t in low for t in UNGRANTED):
        return "ungranted"
    perm = any(token_present(t, low) for t in PERMISSIVE)
    copy = any(token_present(t, low) for t in COPYLEFT)
    # Both present is `mixed`, and it must be tested BEFORE either single verdict. p332's own
    # control suite caught this: ordering the single verdicts first made `mixed` unreachable,
    # and the shelf's `withmarbleapp/os-taxonomy` row — MIT code, CC BY-SA corpora — is
    # exactly that shape. It would have been filed as plain copyleft.
    if perm and copy:
        return "mixed"
    if perm:
        return "permissive"
    if copy:
        return "copyleft"
    return "unknown"


def classify_disposition(row):
    low = row.lower()
    if any(t in low for t in PENDING):
        return "pending"
    if any(t in low for t in REFUSED):
        return "refused"
    return "silent"


def harvest_evidence(root=None, evidence_dir="evidence"):
    """-> {folded_slug: [(file, lineno, grant, disposition)]}. Comment lines are skipped:
    a `#` header is prose about the pass, not a measurement."""
    root = root or ROOT_DEFAULT
    found = {}
    base = os.path.join(root, evidence_dir)
    if not os.path.isdir(base):
        return found
    for name in sorted(os.listdir(base)):
        if not name.endswith((".tsv", ".csv")):
            continue
        if any(d in name for d in DERIVED_EVIDENCE):   # p333 — see DERIVED_EVIDENCE
            continue
        with open(os.path.join(base, name), encoding="utf-8", errors="replace") as fh:
            for n, row in enumerate(fh, 1):
                if row.lstrip().startswith("#") or not row.strip():
                    continue
                for s in slug_fields(row):
                    found.setdefault(fold(s), []).append(
                        (name, n, classify_grant(row), classify_disposition(row)))
    return found


# p250's `ACTION XN` asked for a rule that refuses a slug which is a strict prefix of another,
# and named its own falsifier: `TouchRefletz/maia` vs `maia.edu`. p332 probed all 27 candidates
# first-hand on the raw channel and the falsifier fires — BOTH resolve, and so do
# `autolab/autolab` and `autolab/autolab.github.io`. The prefix rule is therefore not a refusal
# rule; it is a QUESTION, and only an existence probe answers it. These two pairs are the
# measured exceptions, recorded so no later pass re-spends the probe.
PREFIX_BUT_DISTINCT = {"touchrefletz/maia", "autolab/autolab"}


def truncations(slugs):
    """The p332 finding. This corpus carries `dmitry-viskov/pylti1` 21 times beside
    `dmitry-viskov/pylti1.3` 39 times, and `juliapluto/pluto` beside `JuliaPluto/Pluto.jl`.
    Dropping a repo name's extension yields a slug that DOES NOT RESOLVE on GitHub, and
    p235's fold() normalises case but not truncation — so a truncated evidence spelling can
    never match its own shelf row. It reads as undelivered when it is delivered, and if it
    ever reaches a shelf it is a dead link in front of a client.

    -> {truncated_slug: [full_slugs it is a prefix of]}"""
    out = {}
    folded = set(slugs)
    for s in folded:
        if s in PREFIX_BUT_DISTINCT:
            continue
        longer = sorted(t for t in folded if t != s and t.startswith(s + "."))
        if longer:
            out[s] = longer
    return out


def audit(root=None):
    root = root or ROOT_DEFAULT
    ci = _load_carried_index()
    shelf = ci.harvest(root)
    # Read the shelves ONCE. The name channel is a substring test over 9 MB; doing it per
    # candidate re-read the corpus 1,400 times and did not finish.
    shelf_text = ""
    for sh in ci.SHELVES:
        try:
            with open(os.path.join(root, sh), encoding="utf-8", errors="replace") as fh:
                shelf_text += fh.read().lower()
        except FileNotFoundError:
            continue
    measured = harvest_evidence(root)
    rows = []
    for slug, sightings in measured.items():
        if slug in CONTROLS:
            continue
        if ci.carried(slug, shelf):
            continue
        # p235 indexes github.com URLs, not prose names. p332 measured three rows
        # (`qtiworks`, `bnlp`, `uniroster-server`) that are discussed on the shelves by NAME
        # with no URL beside them, and a URL-only index calls all three undelivered. Fall
        # through to the name channel before reporting a miss.
        if slug.split("/", 1)[1] in shelf_text:
            continue
        grants = {g for _, _, g, _ in sightings}
        disps = {d for _, _, _, d in sightings}
        # Most-informative grant wins; a row measured permissive once is permissive.
        grant = ("permissive" if "permissive" in grants else
                 "mixed" if "mixed" in grants else
                 "copyleft" if "copyleft" in grants else
                 "ungranted" if "ungranted" in grants else "unknown")
        disp = ("pending" if "pending" in disps else
                "refused" if "refused" in disps else "silent")
        rows.append({
            "slug": slug, "grant": grant, "disposition": disp,
            "sightings": len(sightings),
            "first": min(sightings, key=lambda s: s[0])[0],
        })
    trunc = truncations(set(measured) | set(shelf))
    return {"shelf_slugs": len(shelf), "measured_slugs": len(measured),
            "controls_excluded": sorted(CONTROLS),
            "undelivered": rows, "truncations": trunc,
            "truncations_on_shelf": {s: v for s, v in trunc.items() if s in shelf}}


def rank(rows):
    """The defect class first: permissive grant, and no pass ever wrote it off.
    A `refused` row at the bottom is working as intended."""
    order = {"pending": 0, "silent": 1, "refused": 2}
    grant_order = {"permissive": 0, "mixed": 1, "unknown": 2, "copyleft": 3, "ungranted": 4}
    return sorted(rows, key=lambda r: (order[r["disposition"]], grant_order[r["grant"]],
                                       -r["sightings"], r["slug"]))


def main(argv):
    root = ROOT_DEFAULT
    if "--root" in argv:
        root = argv[argv.index("--root") + 1]
    res = audit(root)
    rows = rank(res["undelivered"])
    if "--tsv" in argv:
        print("slug\tgrant\tdisposition\tsightings\tfirst_evidence_file")
        for r in rows:
            print(f"{r['slug']}\t{r['grant']}\t{r['disposition']}\t{r['sightings']}\t{r['first']}")
        return 0
    measured = res["measured_slugs"]
    delivered = measured - len(rows)
    print(f"slugs on the shelves          : {res['shelf_slugs']}")
    print(f"slugs measured into evidence/ : {measured}")
    print(f"  of those, delivered to a shelf: {delivered}"
          f"  ({100.0 * delivered / measured:.1f}%)" if measured else "")
    print(f"  of those, NEVER on a shelf    : {len(rows)}")
    print()
    for disp in ("pending", "silent", "refused"):
        sub = [r for r in rows if r["disposition"] == disp]
        perm = [r for r in sub if r["grant"] in ("permissive", "mixed")]
        print(f"  {disp:8} {len(sub):5}   of which permissive/mixed: {len(perm)}")
    print()
    tr = res["truncations"]
    print(f"PREFIX PAIRS, `.git` normalised and the two measured-distinct pairs removed: "
          f"{len(tr)}")
    print(f"  of those also present ON A SHELF (a dead link to a client): "
          f"{len(res['truncations_on_shelf'])}")
    for s_, v in sorted(tr.items())[:12]:
        mark = "SHELF" if s_ in res["truncations_on_shelf"] else "     "
        print(f"  [{mark}] {s_:50} -> {', '.join(v)}")
    print()
    print("THE DEFECT CLASS — measured, permissive, deferred, never delivered:")
    defect = [r for r in rows if r["disposition"] == "pending"
              and r["grant"] in ("permissive", "mixed")]
    if not defect:
        print("  (none — every deferred permissive row reached a shelf)")
    for r in defect[:40]:
        print(f"  {r['slug']:55} {r['grant']:10} {r['sightings']:3} sighting(s)  {r['first']}")
    return 1 if defect else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
