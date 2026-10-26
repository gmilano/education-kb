#!/usr/bin/env python3
"""p454 -- Gap 453-A's prescribed closure: the 71 carried registry-sourced
licence cells have been swept for ADDRESS (p452: 63/71 AGREE, 0 DISAGREE) and
never for VALUE.

p453 swept VALUE over 166 *newly discovered* packages and found 3.0 % DISAGREE,
including one MIT-declared / AGPL-3.0-served address. That population was
novel, so its disagreement rate says nothing about what this base has already
PUBLISHED. This instrument grades the published cells.

Defects this instrument is built against, all of them earlier passes' own:
  * Gap 453-E (d) -- a 404 body was once measured as a 14-byte payload. Every
    read here gates on curl's own %{http_code}; a body is never consulted
    unless the code is 200.
  * Gap 450-C (a) -- family is read from the payload TITLE (verify.py::family),
    not a whole-body grep, because GPLv3's closing text recommends the LGPL.
  * Gap 450-C (b) -- byte counts come from %{size_download}, not len().
  * Gap 449-B -- raw.githubusercontent is case-sensitive on the path, so the
    path set carries both cases.
"""
import csv, hashlib, re, sys, os, concurrent.futures as cf
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "compose", "code", "p453-vocabulary-ledger"))
import importlib.util
_spec = importlib.util.spec_from_file_location(
    "p453verify", os.path.join(ROOT, "compose", "code", "p453-vocabulary-ledger", "verify.py"))
_m = importlib.util.module_from_spec(_spec)
_saved = sys.argv
sys.argv = [sys.argv[0]]          # verify.py reads sys.argv at import time
_spec.loader.exec_module(_m)
sys.argv = _saved
fetch = _m.fetch
# p454: the FAMILY reader is this pass's, not p453's. p453's 40-line window
# mis-grades GPLv2 as LGPL and reports three closed or pointer payloads as
# UNREAD -- measured at 5 of 179 carried payloads in family_delta.py.
_fspec = importlib.util.spec_from_file_location("p454f", os.path.join(HERE, "family_title.py"))
_fm = importlib.util.module_from_spec(_fspec)
_fspec.loader.exec_module(_fm)
family, pointer_target = _fm.family, _fm.pointer_target

POP = os.path.join(ROOT, "evidence", "backlink-agreement-sweep.2026-10-26-p452.tsv")
OUT = os.path.join(ROOT, "evidence", "carried-cell-licence-value.2026-10-26-p454.tsv")

PATHS = ["LICENSE", "LICENSE.md", "LICENSE.txt", "LICENCE", "LICENCE.md",
         "COPYING", "COPYING.txt", "license", "license.md", "LICENSE-MIT",
         "MIT-LICENSE", "LICENSE.rst", "LICENSE.html"]

canon = None  # bound below from p453's declared_vs_payload, re-implemented here

def _canon(s):
    """SPDX-ish normalisation. Re-implemented rather than imported so a defect
    in p453's copy cannot silently propagate; asserted against p453's own
    published values in controls.py."""
    if not s:
        return ""
    t = s.strip().strip('"').upper().replace("_", "-")
    t = re.sub(r"\s+", " ", t)
    t = re.sub(r"^THE ", "", t)
    if "SEE LICENSE IN" in t:
        return "POINTER-OUT-OF-REGISTRY"
    if "PROPRIETARY" in t or "UNLICENSED" == t:
        return "PROPRIETARY"
    if "APACHE" in t:
        return "APACHE-2.0"
    if "AGPL" in t or "AFFERO" in t:
        return "AGPL-3.0"
    if "LGPL" in t or "LESSER" in t:
        return "LGPL"
    if t.startswith("GPL") or "GENERAL PUBLIC" in t:
        return "GPL"
    if t.startswith("MIT"):
        return "MIT"
    if "BSD-3" in t or "BSD 3" in t:
        return "BSD-3-CLAUSE"
    if "BSD-2" in t or "BSD 2" in t:
        return "BSD-2-CLAUSE"
    if t.startswith("BSD"):
        return "BSD"
    if t.startswith("ISC"):
        return "ISC"
    if "MPL" in t or "MOZILLA" in t:
        return "MPL-2.0"
    if "CC0" in t:
        return "CC0-1.0"
    if t.startswith("CC-BY") or "CREATIVE COMMONS" in t:
        return "CC-BY"
    if "UNLICENSE" in t:
        return "UNLICENSE"
    return t


def canon_payload(fam):
    """Payload families carry classes a registry field can never hold. They must
    not be compared as if they were SPDX values."""
    if fam.startswith("NOT-OSI"):
        return "NOT-OSI"
    if fam.startswith("COMPOSITE"):
        return "COMPOSITE"
    if fam.startswith("POINTER_IN_REPO"):
        return "POINTER_IN_REPO"
    return _canon(fam)

canon = _canon

RAW = {"github.com": "https://raw.githubusercontent.com/{slug}/HEAD/{path}",
       "gitlab.com": "https://gitlab.com/{slug}/-/raw/HEAD/{path}"}


def payload_of(address):
    """Return (path, family, bytes, sha12, http_codes_seen). Forge-aware: a
    gitlab address is NOT reachable on raw.githubusercontent, and p452 carried
    one (gitlab.com/travo-cr/travo). A single-forge reader would have graded it
    MANIFEST_ONLY and published a phantom absence."""
    host = address.split("/")[0]
    slug = "/".join(address.split("/")[1:])
    tmpl = RAW.get(host)
    if not tmpl:
        return "", "FORGE_UNSUPPORTED", 0, "", ""
    for p in PATHS:
        body, code, size = fetch(tmpl.format(slug=slug, path=p))
        if code == "200" and body:
            fam = family(body)
            # Follow an in-repo pointer ONE hop. A pointer is the absence of a
            # grant at this path, not the refusal of one, so a reader that
            # stops here publishes a phantom absence.
            if fam.startswith("POINTER_IN_REPO"):
                tgt = pointer_target(body)
                b2, c2, s2 = fetch(tmpl.format(slug=slug, path=tgt))
                if c2 == "200" and b2:
                    return (f"{tgt} (via {p})", family(b2), s2,
                            hashlib.sha256(b2.encode()).hexdigest()[:12], c2)
            return p, fam, size, hashlib.sha256(body.encode()).hexdigest()[:12], code
    return "", "NO_PAYLOAD", 0, "", code


def grade(row):
    registry, pkg, claimed, addr_verdict, decl_repo, decl_lic, version, norm = (row + [""] * 8)[:8]
    if not norm:
        return [registry, pkg, addr_verdict, norm, decl_lic, "", "", "0", "",
                "NO_ADDRESS", canon(decl_lic), ""]
    path, fam, size, sha, code = payload_of(norm)
    d, p = canon(decl_lic), canon_payload(fam)
    if fam == "FORGE_UNSUPPORTED":
        v = "FORGE_UNSUPPORTED"
    elif fam == "NO_PAYLOAD":
        v = "MANIFEST_ONLY" if d and d not in ("POINTER-OUT-OF-REGISTRY",) else "NO_GRANT_ANYWHERE"
    elif not d:
        v = "REGISTRY_SILENT"
    elif d == "POINTER-OUT-OF-REGISTRY":
        v = "POINTER"
    elif fam == "UNREAD":
        v = "PAYLOAD_UNREAD"
    elif p == "NOT-OSI":
        # The registry declares an OSI grant and the payload refuses permission.
        # This is not an ordinary value disagreement; it is the one direction
        # that turns a shelf row into a liability.
        v = "DISAGREE_NOT_OSI"
    elif p == "COMPOSITE":
        v = "COMPOSITE" if d in fam.upper() else "DISAGREE_COMPOSITE"
    elif d == p:
        v = "AGREE"
    else:
        v = "DISAGREE"
    return [registry, pkg, addr_verdict, norm, decl_lic, fam, path, str(size), sha, v, d, p]


def main():
    rows = []
    with open(POP) as f:
        rd = csv.reader(f, delimiter="\t")
        next(rd)
        for r in rd:
            if r:
                rows.append(r)
    print(f"population: {len(rows)} carried registry-sourced cells", file=sys.stderr)
    out = []
    with cf.ThreadPoolExecutor(max_workers=6) as ex:
        for i, res in enumerate(ex.map(grade, rows), 1):
            out.append(res)
            if i % 20 == 0:
                print(f"  {i}/{len(rows)}", file=sys.stderr)
    with open(OUT, "w") as f:
        f.write("registry\tpackage\tp452_address_verdict\taddress\tdeclared_registry\t"
                "payload_family\tpayload_path\tpayload_bytes\tsha256_12\tvalue_verdict\t"
                "canon_declared\tcanon_payload\n")
        for r in out:
            f.write("\t".join(r) + "\n")
    c = Counter(r[9] for r in out)
    print("\n=== value verdicts over the carried cells ===")
    for k, n in c.most_common():
        print(f"  {k:20s} {n:4d}  {100*n/len(out):5.1f}%")
    print("\n=== every DISAGREE, in full ===")
    for r in out:
        if r[9] == "DISAGREE":
            print(f"  {r[3]:46s} {r[0]:10s} declared={r[10]:22s} served={r[11]:14s} "
                  f"{r[7]:>7s} B  {r[6]}  {r[8]}")
    print("\n=== POINTER / MANIFEST_ONLY / PAYLOAD_UNREAD / other ===")
    for r in out:
        if r[9] in ("POINTER", "MANIFEST_ONLY", "PAYLOAD_UNREAD", "REGISTRY_SILENT",
                    "NO_GRANT_ANYWHERE", "FORGE_UNSUPPORTED", "NO_ADDRESS"):
            print(f"  {r[9]:18s} {r[3] or '(no address)':46s} {r[0]:10s} "
                  f"declared={r[4][:40]!r} served={r[5]}")
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    main()
