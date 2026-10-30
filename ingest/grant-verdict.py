#!/usr/bin/env python3
"""grant-verdict.py -- the instrument Gap 552-B and Gap 552-D demanded (p553).

WHY THIS EXISTS
  p552 registered two asks against the grant layer and closed neither, because both
  need a reader that looks INSIDE the grant text rather than at its family name.

  552-D  `frappe/education`'s `license.txt` is 19 bytes in full: "License: GNU GPL V3".
         No copyright line, no permission clause, no warranty disclaimer -- a CLAIM
         about a grant, not a grant. Every reader on these shelves returned UNREAD for
         it, which is indistinguishable from a dead channel, so a 19-byte assertion and
         a 404 landed in the same cell. Ask: a GRANT-ASSERTED-NOT-CARRIED verdict,
         distinct from UNREAD.

  552-B  `Oriole-FDU/Wisepen` is BUSL-1.1 and its Additional Use Grant excludes
         "consulting deliverable" in those words -- Globant's own delivery model, named
         in the licence. No probe on these shelves separated it from a permissive row,
         because the exclusion lives in a BUSL PARAMETER BLOCK and not in the family
         name: two BUSL-1.1 repositories can differ completely on whether Globant may
         ship them. Ask: for any non-OSI source-available grant, parse and carry the
         Additional Use Grant and the Change Date, not just the family name.

🔴 WHAT THIS INSTRUMENT CANNOT DO, STATED FIRST
  1. It is NOT legal advice and its verdict is not a clearance. It reports what the
     grant file SAYS, first-hand, with byte counts and a HEAD sha so a successor can
     re-read the same bytes. A SHIPPABLE verdict means "no exclusion found in this
     text", never "cleared by counsel".
  2. The consultancy-exclusion scan is a KEYWORD scan over the grant body. It can only
     find an exclusion that is WORDED. A source-available licence that excludes
     integrators by construction without using any of these words reads SHIPPABLE here
     and is not. This is the same class of limit as Gap 552-A one layer down, and it is
     why the Additional Use Grant is PRINTED IN FULL rather than reduced to a flag --
     the text is the evidence; the flag is only an index into it.
  3. It cannot distinguish a stub that is a CONVENTION (the CRAN `MIT + file LICENSE`
     shape, Gap 542-H -- a real grant lives elsewhere) from a stub that is the WHOLE
     claim (552-D -- nothing lives elsewhere). It reports both as stubs and resolves
     them only by the union: a stub BESIDE a carried grant is 542-H, a stub ALONE is
     552-D. That rule is in the code, not in this prose.

WHAT IT GUARANTEES
  1. Default branch RESOLVED (git ls-remote --symref), never assumed -- Gap 509/516.
  2. Grant filenames probed with GENERATED case variants -- Gap 530.
  3. `license.txt` is on the list. Gap 552-C's miss cannot recur silently: the name
     list is printed with --names and its length is stamped into every UNRESOLVED.
  4. Byte counts are `len(payload)` over the WHOLE body, never a capped read -- p543.
  5. For every non-OSI family, the parameter block is parsed and CARRIED verbatim.

USAGE   python3 -I grant-verdict.py owner/repo [owner/repo ...]
        python3 -I grant-verdict.py --names          # print the probe list and exit
OUTPUT  TSV on stdout; full Additional Use Grant text on stderr-free stdout blocks
        when --params is passed.
"""
import concurrent.futures as cf
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

TIMEOUT = 25

_BASE = [
    "LICENSE", "LICENSE.md", "LICENSE.txt", "LICENSE.rst",
    "LICENCE", "LICENCE.md", "LICENCE.txt",
    "COPYING", "COPYING.txt", "COPYING.md", "NOTICE", "NOTICE.txt",
    # non-OSI families keep the grant under their own name often enough to probe
    "LICENSE-BUSL", "LICENSE-BUSL.md", "BUSL-1.1", "BUSL.txt",
    # split code/data grants -- Gap 542-A
    "LICENSE-CODE", "LICENSE-CODE.md", "LICENSE-TEXT", "LICENSE-TEXT.md",
    "LICENSE-DATA", "LICENSE-DATA.md", "LICENSE-CONTENT", "LICENSE-CONTENT.md",
    "LICENSE-DOCS", "LICENSE-DOCS.md", "LICENSE-MIT", "LICENSE-APACHE",
    "LICENSE-CODIGO.md", "LICENSE-DADOS.md",
    # non-English
    "LICENCA", "LICENCA.md", "LICENÇA", "LICENÇA.md",
    "LICENCIA", "LICENCIA.md", "LIZENZ", "LIZENZ.md", "LICENZA", "LICENZA.md",
    "许可证", "开源协议.md", "LICENSE-CN", "LICENSE.zh",
    "ライセンス", "라이선스", "LISENSI", "ЛИЦЕНЗИЯ", "الترخيص",
]


def names():
    """Gap 530: GENERATED case variants, because the remote is case-sensitive on the
    whole filename including the extension and authors are not consistent. A
    hand-written list is exactly what failed in 530 and again in 552-C."""
    out = []
    for n in _BASE:
        for v in (n, n.upper(), n.lower(), n.lower().capitalize()):
            if not n.isascii():
                v = n
            if v not in out:
                out.append(v)
    return out


NAMES = names()

# ---- families -------------------------------------------------------------------
# A non-OSI family is one the OSI has NOT approved. Globant cannot ship these on the
# strength of the family name alone; the parameter block decides.
NON_OSI = {
    "BUSL-1.1": ("Business Source License 1.1", "BUSL"),
    "SSPL-1.0": ("Server Side Public License",),
    "Elastic-2.0": ("Elastic License 2.0",),
    "FSL": ("Functional Source License",),
    "PolyForm": ("PolyForm",),
    "SUL": ("Sustainable Use License",),
    "CommonsClause": ("Commons Clause",),
    "CC-NC": ("NonCommercial",),
}

# 552-B: the words that, inside a grant, shut a consultancy out. Printed, not hidden,
# because the scan can only find an exclusion that is WORDED (limit 2 above).
EXCLUSION_WORDS = [
    "consulting deliverable", "consultancy", "consulting service", "consulting services",
    "professional services", "system integrator", "systems integrator",
    "hosted service", "saas offering", "paid service", "commercial product",
    "revenue-generating", "revenue generating", "resell", "sublicense for a fee",
    "non-commercial", "noncommercial", "for commercial purposes",
]

# operative clauses: the things a real grant CARRIES, as opposed to asserts.
#
# 🔴 Gap 553-C -- THIS LIST IS THE VERDICT'S FALSE-POSITIVE SURFACE, and it produced a
# false NOT-CARRIED on this verdict's FIRST REAL USE. See `carried()`.
OPERATIVE = [
    # permissive / copyleft grant verbs
    "permission is hereby granted", "redistribution and use",
    "you may not use this file except in compliance",
    "this program is free software", "without warranty", "as is",
    "subject to the terms", "grants you", "hereby grants",
    "terms and conditions", "copying and distribution",
    "licensed work", "licensed under the",
    # p553 / Gap 553-C: PUBLIC-DOMAIN DEDICATION verbs. A CC0 grant does not "grant
    # permission" -- it WAIVES. None of the clauses above appear in a CC0 payload, so
    # every CC0 file on these shelves was one read away from being filed as a bare
    # assertion. The waiver IS the operative clause.
    "waives, abandons", "abandons, and surrenders", "surrenders all",
    "relinquish", "dedicated to the public domain", "no copyright",
    "waives all", "statement of purpose",
]

# Canonical payload sizes of the full legal code, in bytes, measured from the grants
# read first-hand by this base. Used ONLY to flag abridgement -- Gap 553-C.
CANONICAL_BYTES = {
    "MIT": 1050, "Apache-2.0": 11350, "GPL-3.0": 35000, "GPL-2.0": 18000,
    "AGPL-3.0": 34500, "LGPL": 7600, "BSD-3-Clause": 1500, "BSD-2-Clause": 1300,
    "MPL-2.0": 16700, "ISC": 750, "CC0-1.0": 7000, "CC-BY-4.0": 18000,
    "CC-BY-SA-4.0": 19000, "BUSL-1.1": 4300, "ECL-2.0": 11500,
}


def normalise(body):
    """Gap 553-C, second limb. The file that defeated `carried()` writes `"AS-IS"`, and
    the list carries `as is`. A matcher that is literal about hyphens and quotes is
    measuring typography, not grants."""
    out = body.lower()
    for a, b in (("\u2019", "'"), ("\u2018", "'"), ("\u201c", '"'), ("\u201d", '"'),
                 ("\u2013", "-"), ("\u2014", "-")):
        out = out.replace(a, b)
    return out.replace("-", " ").replace("_", " ")


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "education-kb/p553"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.read()
    except (urllib.error.URLError, urllib.error.HTTPError, OSError):
        return None


def symref(slug):
    try:
        out = subprocess.run(
            ["git", "ls-remote", "--symref", f"https://github.com/{slug}", "HEAD"],
            capture_output=True, text=True, timeout=90).stdout
    except (subprocess.SubprocessError, OSError):
        return None, None
    br = sha = None
    for line in out.splitlines():
        if line.startswith("ref:"):
            br = line.split()[1].replace("refs/heads/", "")
        elif line.endswith("HEAD"):
            sha = line.split()[0][:12]
    return br, sha


def title_block(body):
    """p553 / Gap 553-A -- the window a family matcher may read.

    🔴 CAUGHT AGAINST THIS INSTRUMENT'S OWN FIRST RUN. `frappe/erpnext` carries plain
    GPL-3.0 on both `master` and `develop`, read first-hand. This instrument called it
    AGPL-3.0, because GPL-3.0 SECTION 13 IS TITLED "Use with the GNU Affero General
    Public License" and names AGPL in its body -- and a whole-payload matcher sees it.

    🔵 The mechanism is the important part: `probe-grant.sh` gets this case RIGHT, and
    gets it right BY ACCIDENT. It reads `head -c 4096`, and s13 of a 35 KB licence sits
    far outside that window. p543 correctly removed the 4 KB cap (it made a 35 KB grant
    measure 4096 B). Removing the cap was right AND it de-protected every whole-body
    keyword matcher in this base, because the cap had been acting as a title-block
    anchor nobody had declared. A licence that CITES another licence -- GPL s13 naming
    AGPL, BUSL naming Apache-2.0 as its Change License -- now matches both.

    So: the FAMILY is read from the title block only. Exclusion scanning still reads the
    whole payload, because an exclusion can live anywhere, but it is gated by family.
    """
    lines = [ln.strip() for ln in body.splitlines()]
    out, seen = [], 0
    for ln in lines:
        if ln:
            out.append(ln)
            seen += 1
        if seen >= 12 or sum(len(x) for x in out) > 700:
            break
    return "\n".join(out)


def spdx_of(body):
    # Gap 553-A: match the family on the TITLE BLOCK, never the whole payload.
    b = title_block(body)
    u = b.upper()
    if "BUSINESS SOURCE LICENSE" in u:
        return "BUSL-1.1"
    if "SERVER SIDE PUBLIC LICENSE" in u:
        return "SSPL-1.0"
    if "ELASTIC LICENSE 2.0" in u:
        return "Elastic-2.0"
    if "FUNCTIONAL SOURCE LICENSE" in u:
        return "FSL"
    if "POLYFORM" in u:
        return "PolyForm"
    if "SUSTAINABLE USE LICENSE" in u:
        return "SUL"
    if "COMMONS CLAUSE" in u:
        return "CommonsClause"
    if "GNU AFFERO GENERAL PUBLIC" in u:
        return "AGPL-3.0"
    if "GNU LESSER GENERAL PUBLIC" in u:
        return "LGPL"
    if "VERSION 3, 29 JUNE 2007" in u:
        return "GPL-3.0"
    if "VERSION 2, JUNE 1991" in u:
        return "GPL-2.0"
    if "GNU GENERAL PUBLIC LICENSE" in u:
        return "GPL-?"
    if "APACHE LICENSE" in u:
        return "Apache-2.0"
    if "MOZILLA PUBLIC LICENSE" in u:
        return "MPL-2.0"
    if "EDUCATIONAL COMMUNITY LICENSE" in u:
        return "ECL-2.0"
    if "ISC LICENSE" in u:
        return "ISC"
    if "CC0" in u or "CREATIVE COMMONS ZERO" in u:
        return "CC0-1.0"
    if "ATTRIBUTION-SHAREALIKE" in u:
        return "CC-BY-SA-4.0"
    if "ATTRIBUTION-NONCOMMERCIAL" in u:
        return "CC-BY-NC-4.0"
    if "CREATIVE COMMONS" in u:
        return "CC-BY-4.0"
    if "MIT LICENSE" in u or "PERMISSION IS HEREBY GRANTED, FREE OF CHARGE" in u:
        return "MIT"
    if "REDISTRIBUTION AND USE IN SOURCE AND BINARY FORMS" in u:
        return "BSD-3-Clause" if "NEITHER THE NAME" in u else "BSD-2-Clause"
    if "UNLICENSE" in u or "PUBLIC DOMAIN" in u:
        return "Unlicense"
    return "unknown-text"


def params(body):
    """552-B: carry the parameter block, not the family name. BUSL/FSL state their
    terms as `Key: value` lines; the value may wrap over several lines until the next
    key or a blank-line-then-key. Returns dict of the keys that decide shippability."""
    want = ("licensor", "licensed work", "additional use grant",
            "change date", "change license", "change licence")
    found, key, buf = {}, None, []
    for raw in body.splitlines():
        line = raw.strip()
        head = line.split(":", 1)
        cand = head[0].strip().strip("*_ ").lower() if len(head) == 2 else ""
        if cand in want:
            if key:
                found[key] = " ".join(buf).strip()
            key, buf = cand, [head[1].strip()]
        elif key:
            if not line:
                continue
            if line.lower().startswith(("terms", "notice", "-----")):
                break
            buf.append(line)
    if key:
        found[key] = " ".join(buf).strip()
    return found


# OSI-approved families cannot carry a non-commercial restriction -- it is
# incompatible with the OSD. Gap 553-B.
OSI_FAMILIES = {
    "MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC", "MPL-2.0",
    "ECL-2.0", "GPL-2.0", "GPL-3.0", "GPL-?", "AGPL-3.0", "LGPL", "Unlicense",
    "CC0-1.0",
}


def exclusions(body, family):
    """🔴 SECOND DEFECT CAUGHT AGAINST THIS INSTRUMENT'S OWN FIRST RUN (Gap 553-B).

    The first run returned NOT-SHIPPABLE-NONCOMMERCIAL-TERMS for `frappe/erpnext`.
    GPL-3.0 contains the token `noncommercially` exactly once -- in s6(d), where it
    describes a PERMITTED mode of conveying, not a restriction on one. A keyword scan
    cannot tell a permission from a prohibition, so the scan is GATED: an OSI-approved
    family is never scanned for non-commercial exclusions, because the OSD forbids them.

    🔵 What this still cannot do: find an exclusion that is not WORDED (limit 2 in the
    module docstring). The gate narrows the false positives; it does not widen recall.
    """
    low = body.lower()
    hits = [w for w in EXCLUSION_WORDS if w in low]
    if family in OSI_FAMILIES:
        hits = [w for w in hits if "commercial" not in w and "resell" not in w]
    return hits


def carried(body):
    """552-D: does this file CARRY a grant, or only ASSERT one?
    A grant that is carried states an operative clause. A 19-byte `License: GNU GPL V3`
    states a family and nothing else.

    🔴 Gap 553-C -- CAUGHT ON THIS VERDICT'S FIRST REAL USE, AGAINST THE ONE LATAM
    ARTEFACT THIS BASE HAS FOUND IN FOUR PASSES.
    `juanmoisesd/ai-educational-impact-latin-america-dataset` carries a 1 259 B CC0
    payload whose operative sentence is *"Affirmer hereby overtly, fully, permanently,
    irrevocably and unconditionally waives, abandons, and surrenders all of Affirmer's
    Copyright and Related Rights"*. That is a grant, read first-hand. This function
    called it an ASSERTION, for two reasons that are both typography and neither law:
      1. no CC0 verb was on OPERATIVE -- the list was written from permissive and
         copyleft grants only, and a dedication waives where a licence permits;
      2. the payload writes `"AS-IS"` and the list carried `as is`.

    🔵 Why this is worth a gap and not a silent fix: 552-D asked for a verdict that
    separates a 19-byte claim from a dead channel, and it got one. The SYMMETRIC error
    -- a real grant filed as a claim because its vocabulary is not on a hand-written
    list -- is the same defect class one sign flipped, and it is WORSE for this base,
    because NOT-CARRIED reads as a disqualification. It would have struck the only
    LATAM row in four passes off the shelf on a hyphen.
    """
    low = normalise(body)
    return any(p in normalise(p) and normalise(p) in low for p in OPERATIVE)


def abridged(body, family):
    """Gap 553-C, third limb: a grant can be CARRIED and still be INCOMPLETE.

    The LATAM payload holds CC0's title, disclaimer, Statement of Purpose and the
    waiver sentence -- and not s2 (Waiver), s3 (Public License Fallback) or s4
    (Limitations and Disclaimers) of the 7 KB legal code. 🔵 s3 is the clause that
    makes CC0 work where a waiver is not recognised in law, which is most of LATAM's
    civil-law jurisdictions. So the abridgement is not cosmetic for the one region this
    row is placed in. Reported as a third band, never folded into NOT-CARRIED."""
    want = CANONICAL_BYTES.get(family)
    if not want:
        return None
    if len(body) < want * 0.6:
        return f"ABRIDGED[{len(body)}B-of-~{want}B-canonical]"
    return None


def verdict(hits):
    """One verdict per repo, over the UNION of grant files found.
    The stub rule (limit 3): a stub BESIDE a carried grant is the 542-H CRAN
    convention and is dropped from the union; a stub ALONE is 552-D."""
    if not hits:
        return f"UNRESOLVED-on-{len(NAMES)}-names", "", ""
    real = [h for h in hits if h["carried"]]
    assertions = [h for h in hits if not h["carried"]]
    if not real:
        if assertions:
            fams = sorted({h["spdx"] for h in assertions if h["spdx"] != "unknown-text"})
            claim = ("claims " + "/".join(fams)) if fams else "names no family"
            return "GRANT-ASSERTED-NOT-CARRIED", claim, ""
        return f"UNRESOLVED-on-{len(NAMES)}-names", "", ""
    fams = sorted({h["spdx"] for h in real})
    nonosi = [f for f in fams if f in NON_OSI]
    excl = sorted({w for h in real for w in h["exclusions"]})
    pb = {}
    for h in real:
        pb.update(h["params"])
    if nonosi:
        aug = pb.get("additional use grant", "")
        cd = pb.get("change date", "")
        cl = pb.get("change license", pb.get("change licence", ""))
        tag = "NOT-SHIPPABLE-WITHOUT-COMMERCIAL-LICENCE" if excl else "SOURCE-AVAILABLE-NO-WORDED-EXCLUSION"
        detail = f"AUG={aug or '(none in payload)'} | CHANGE-DATE={cd or '-'} | CHANGE-LICENSE={cl or '-'}"
        return tag, "+".join(nonosi), detail
    copyleft = [f for f in fams if f.startswith(("GPL", "AGPL", "LGPL")) or f in ("CC-BY-SA-4.0",)]
    if any(f in ("CC-BY-NC-4.0",) for f in fams) or "non-commercial" in excl or "noncommercial" in excl:
        return "NOT-SHIPPABLE-NONCOMMERCIAL-TERMS", "+".join(fams), ""
    if copyleft:
        return "SHIPPABLE-WITH-COPYLEFT-OBLIGATIONS", "+".join(fams), ""
    return "SHIPPABLE-PERMISSIVE", "+".join(fams), ""


def probe_one(slug, name, branch):
    enc = urllib.parse.quote(name, safe="")
    body = get(f"https://raw.githubusercontent.com/{slug}/{branch}/{enc}")
    if not body:
        return None
    nb = len(body)
    if nb == 0:
        return None
    txt = body.decode("utf-8", "replace")
    if txt.startswith("404: Not Found"):
        return None
    fam = spdx_of(txt)
    return {"name": name, "bytes": nb, "spdx": fam, "abridged": abridged(txt, fam),
            "carried": carried(txt), "exclusions": exclusions(txt, fam),
            "params": params(txt), "text": txt}


def run(slug, show_params=False):
    branch, sha = symref(slug)
    if not branch:
        return f"{slug}\tDEAD-OR-PRIVATE\t-\t-\t-\t-\t-", None
    hits = []
    with cf.ThreadPoolExecutor(max_workers=16) as ex:
        futs = {ex.submit(probe_one, slug, n, branch): n for n in NAMES}
        for f in cf.as_completed(futs):
            h = f.result()
            if h:
                hits.append(h)
    hits.sort(key=lambda h: -h["bytes"])
    tag, fams, detail = verdict(hits)
    files = ",".join(
        f"{h['name']}[{h['bytes']}B"
        f"{'' if h['carried'] else ':ASSERTION-ONLY'}"
        f"{':' + h['abridged'] if h.get('abridged') else ''}]"
        for h in hits) or "-"
    # 🔴 Gap 553-D -- THE ABRIDGED BAND'S OWN FALSE POSITIVE, caught on first run.
    # `openedx/XBlock` carries full Apache-2.0 at `LICENSE.TXT` (11 358 B) AND a 545 B
    # `NOTICE.txt` that names the Apache License in its opening lines. The band read
    # the NOTICE as an abridged Apache grant and flagged a repo whose grant is complete.
    # 🔵 The fix is the rule this module already applies to stubs (542-H) and failed to
    # apply to its own new band: resolve ABRIDGEMENT OVER THE UNION, not per file. A
    # family is abridged only if NO file of that family reaches canonical size. Writing
    # the union rule in a docstring did not make it apply to the next band added.
    full = {h["spdx"] for h in hits if h["carried"] and not h.get("abridged")}
    ab = [h["abridged"] for h in hits
          if h.get("abridged") and h["carried"] and h["spdx"] not in full]
    if ab and tag.startswith("SHIPPABLE"):
        tag = f"{tag}+GRANT-{ab[0]}"
    row = f"{slug}\tLIVE\t{branch}\t{sha}\t{files}\t{fams or '-'}\t{tag}\t{detail or '-'}"
    block = None
    if show_params and hits:
        pb = {}
        for h in hits:
            pb.update(h["params"])
        if pb:
            block = f"\n### {slug} -- parameter block read first-hand\n" + "\n".join(
                f"  {k}: {v}" for k, v in pb.items())
    return row, block


def main():
    args = [a for a in sys.argv[1:] if a != "--params"]
    show = "--params" in sys.argv
    if not args or args[0] == "--names":
        print(f"# {len(NAMES)} grant filenames probed, case variants generated")
        for n in NAMES:
            print(n)
        return
    print("repo\tlive\tdefault_branch\thead_sha\tgrant_files\tfamilies\tverdict\tparameters")
    blocks = []
    for slug in args:
        row, block = run(slug, show)
        print(row, flush=True)
        if block:
            blocks.append(block)
    for b in blocks:
        print(b)


if __name__ == "__main__":
    main()
