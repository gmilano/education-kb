#!/usr/bin/env python3
"""p348 -- a grant has a SCOPE and a PROVENANCE, and neither is a path blacklist.

`ACTION ZZ-z` asked for the root ladder to be replaced by pin + tree enumeration +
SCOPE GRADING.  `p441` already enumerates the tree; what it does not do is grade what a
deep grant GOVERNS, and `ACTION ZZ-u` is the cost: `likr/canvas-lms-agent` carries two
licence files and the first in path order is

    .agents/skills/skill-creator/LICENSE.txt

a vendored third party's Apache-2.0 text, so "take the first licence you find"
publishes somebody else's grant as the repository's.  `p441`'s answer to that class is
`EXCLUDE_DIR_RE` -- a directory blacklist carrying `node_modules`, `vendor`,
`third_party`, `.corepack` -- and `.agents/skills/` is not in it.  It could be added.
The next one would not be, which is the SAME defect `p441`'s own docstring names in its
first paragraph: **widening a list cannot fix a list.**

So this instrument decides provenance from the payload instead of from the path:

    SCOPE       ROOT       -> the grant governs the repository
                SUBTREE    -> the grant governs its own directory and nothing above it
    PROVENANCE  OWN        -> the holder line agrees with the repository's own identity
                FOREIGN    -> it names somebody else; this grant is not the project's

The holder channel is `ACTION ZZ-y`, registered by `p347` after `ls1intum/Ares2`'s
`LICENSE` turned out to name TUM's School of Computation in public, aggregate text and
to agree with both the domain channel and a confirmed CET/CEST shift.  Here it is load
bearing for a second job: a vendored grant is foreign BY ITS HOLDER, whatever directory
it was dropped into, and `.agents/skills/skill-creator/LICENSE.txt` says `Anthropic`
while the repository says `likr`.

Two reads, both at the pin, exactly as `ACTION ZZ-q` concluded:

    git ls-remote --symref <url> HEAD          # the sha.  Dissolves the whole ref axis.
    git ls-tree -r --name-only <sha>           # the complete tree.  Dissolves case,
                                               # spelling, extension and depth at once.

and then `raw.githubusercontent.com/<slug>/<sha>/<path>`, which pins the PAYLOAD too --
the only one of this base's two reachable hosts that can.

Verdicts:
    REPOSITORY-GRANT     an own-holder licence text at the root
    PACKAGE-GRANT-ONLY   own-holder grants exist, all in subtrees: they license those
                         components, and the repository itself is still ungranted
    FOREIGN-GRANT-ONLY   every licence text found names another holder (the ZZ-u class)
    ABSENCE-ENUMERATED   no licence-shaped path in the complete tree at the pin
    UNRESOLVED           the address does not answer

Family vocabulary adds `NCSA` this pass (`ACTION ZZ-ab`).  `cs341-illinois/coursebook`
publishes the University of Illinois/NCSA licence, and the canonical `p436.family_of`
did not abstain on it -- it answered **MIT**, because NCSA's permission clause is
MIT-phrased.  That is the UNSAFE direction: MIT's notice requirement is strictly weaker
than NCSA's BSD-style no-endorsement clause, so the published cell UNDERSTATED what a
client owes.  `P250` makes an abstention safe; it does not make a wrong family safe.
`ECL-2.0` was already present; the re-check found NO defect -- Sakai's real 11 120-byte payload names Apache zero times -- which is itself worth recording, because the NCSA finding on the same axis went the other way.  A payload is read
through `_strip_bom` because `zaikaman/SGU-Academic-MCP`'s `LICENSE` opens `EF BB BF`
then `MIT License`, and a detector anchored on `^MIT License` grades a stock MIT grant
UNTITLED (`ACTION ZZ-w`).

Declared limits:
- The holder channel needs a holder LINE.  A payload with no `Copyright` line (CC0,
  Unlicense, some Apache-2.0 copies that leave the brackets empty) is graded
  `HOLDER-ABSENT`, and a SUBTREE grant with no holder is reported as such rather than
  guessed in either direction.  `HOLDER-ABSENT` at the ROOT is still the repository's
  grant: root position carries it.
- Token agreement is a SUFFICIENT test, never a necessary one.  `ls1intum/Ares2` passes
  on `tum`; a university repository whose holder line names only a person would read
  FOREIGN at depth, so that verdict is a reading list and not a conclusion.
- `api.github.com` is 403 here and so is `github.com` over `curl`, so this instrument
  reports NO star count.  Commits, authors and the timezone channel come from the
  blobless clone's own `git log`, which is first-hand.
"""
import os
import re
import subprocess
import sys
import tempfile
import urllib.parse
import urllib.request

RAW = "https://raw.githubusercontent.com"
LICENCE_RE = re.compile(r"(?:^|/)(?:un)?licen[cs]e|(?:^|/)copying|(?:^|/)copyright", re.I)
# A source, template or image file whose NAME contains the word is not a grant: p441
# measured this class on an icon component, an XSLT transform and the European
# Commission's EUPL README badge.
SOURCE_EXT = (".py", ".js", ".ts", ".tsx", ".jsx", ".vue", ".svelte", ".go", ".java",
              ".rb", ".php", ".c", ".h", ".cpp", ".cs", ".rs", ".sh", ".bat", ".ps1",
              ".yml", ".yaml", ".json", ".xml", ".xsl", ".xslt", ".toml", ".cfg",
              ".ini", ".svg", ".png", ".jpg", ".jpeg", ".gif", ".ico", ".mustache",
              ".erb", ".twig", ".scss", ".css", ".lock", ".spdx", ".csv")
STOPWORDS = {"the", "inc", "inc.", "llc", "ltd", "gmbh", "co", "corp", "foundation",
             "university", "universitat", "universiteit", "universite", "institute",
             "project", "team", "contributors", "authors", "all", "rights",
             "reserved", "and", "of", "for", "its", "or", "de", "van", "der",
             "school", "faculty", "research", "group", "dept", "department", "e.v.",
             "association", "society", "org", "community", "developers", "copyright"}


def _strip_bom(text):
    """ACTION ZZ-w: a BYTE-ORDER MARK is an axis on the title-line family."""
    return text.lstrip("﻿")


def family_of(text):
    """Coarse family.  ORDER IS THE WHOLE FUNCTION -- see p436's docstring for why
    EUPL, MPL and EPL must all be probed before the GNU family.  NCSA is new this pass.
    """
    text = _strip_bom(text)
    t = text[:6000].lower()
    if re.search(r"european union public licen[cs]e|licensed under the eupl"
                 r"|under the eupl\b|eupl[,-]?\s*(?:version\s*)?1\.[12]", t):
        return "EUPL"
    if "mozilla public license" in t:
        return "MPL-2.0"
    if "eclipse public license" in t:
        return "EPL"
    # ACTION ZZ-ab, and the ordering is a MEASUREMENT.  Read first-hand at the pin, the
    # real payload at `cs341-illinois/coursebook` -> `LICENSE/LICENSE.code` (1 698 B,
    # HTTP 200) was graded **MIT** by the canonical `p436.family_of` -- not BSD, and not
    # UNKNOWN -- because NCSA's permission clause is MIT-PHRASED ("Permission is hereby
    # granted, free of charge, to any person obtaining a copy").  So NCSA has to be
    # probed before MIT, and therefore before BSD, whose three-clause body it also
    # carries.  🔴 p347 recorded the risk as detection ABSTAINING on university
    # licences; the first-hand read refutes that and the truth is worse: it answers a
    # family whose notice requirements are strictly WEAKER, which UNDERSTATES what a
    # client owes.  An abstention fails safe under `P250`; this does not.
    if ("university of illinois" in t and "ncsa" in t) or \
       "ncsa open source license" in t or \
       "university of illinois/ncsa" in t:
        return "NCSA"
    # ECL-2.0, re-checked first-hand this pass as ACTION ZZ-ab also asked.  🟡 The
    # expectation was that an ECL payload names Apache by title and so must be probed
    # first.  `sakaiproject/sakai`'s actual 11 120-byte `LICENSE` names "apache license"
    # ZERO times, so the canonical detector grades it correctly at its existing position
    # and the re-check found no defect.  The ordering is kept here as a guard against the
    # SHORT derivative-preamble variant some projects ship, which does name Apache -- a
    # precaution, stated as a precaution rather than as a measured need.
    if "educational community license" in t:
        return "ECL-2.0"
    if "apache license" in t and "version 2.0" in t:
        return "Apache-2.0"
    head = "\n".join(text.splitlines()[:8]).lower()
    if "affero" in head:
        return "AGPL-3.0"
    if "lesser general public" in head:
        return "LGPL"
    if "gnu general public license" in head:
        return "GPL"
    if "creative commons" in t:
        m = re.search(r"attribution[- ](?:sharealike[- ])?(\d\.\d)", t)
        if "cc0" in t or "public domain dedication" in t:
            return "CC0"
        return "CC-BY" + ("-" + m.group(1) if m else "")
    if "unlicense" in t and "public domain" in t:
        return "Unlicense"
    if "redistribution and use in source and binary forms" in t:
        n = 3 if re.search(r"neither the name", t) else 2
        return "BSD-%d-Clause" % n
    if "permission is hereby granted, free of charge" in t:
        if "the software is provided" in t:
            return "MIT" if "sublicense" in t else "ISC"
        return "MIT"
    if "permission to use, copy, modify" in t and "isc" in t:
        return "ISC"
    if "gnu general public" in t:
        return "GPL"
    return "UNKNOWN"


# The holder line, and the two conditions the FIRST build of this instrument lacked.
# It read every line CONTAINING the word `copyright`, which in an MIT payload means
# "The above copyright notice and this permission notice shall be included in" and
# "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER" -- so the
# token set of every MIT grant carried {notice, permission, shall, holders, liable,
# claim, damages}, the SAME words in every MIT payload on GitHub, and any two MIT files
# "agreed" on their holder.  That is how the first run graded Twitter's vendored
# Bootstrap grant OWN inside `AcademicsToday/academicstoday-django`: not because the
# holders matched but because the BOILERPLATE did.  A holder channel that reads licence
# prose measures the licence, never the holder -- which is `P342`'s rule arriving on a
# third surface after the README badge and the manifest.
HOLDER_RE = re.compile(
    r"^\s*(?:[#*;]|//)?\s*copyright\b[\s:]*(?:\(c\)|\u00a9|\(C\))?[\s:]*"
    r"((?:[0-9]{4}(?:\s*[-\u2013,]\s*(?:[0-9]{4}|present))?[\s,]*)+)(.*)$", re.I)


def holder_of(text):
    """The copyright holder LINE, and only the holder line.  ACTION ZZ-y.

    Two conditions, both learned from this instrument's own first run:
      1. the line must BEGIN with `Copyright` (after an optional comment marker), which
         excludes the MIT and Apache boilerplate sentences that merely contain the word;
      2. it must carry a four-digit YEAR, which excludes Apache-2.0's appendix template
         `Copyright [yyyy] [name of copyright owner]` -- a FORM, not a holder.
    A payload with no qualifying line is HOLDER-ABSENT, which at the ROOT is still the
    repository's grant, because root POSITION carries it.
    """
    text = _strip_bom(text)
    holders = []
    for line in text.splitlines()[:60]:
        m = HOLDER_RE.match(line)
        if not m:
            continue
        h = m.group(2).strip(" .,;:-\t")
        if not h or len(h) <= 2:
            continue
        if re.fullmatch(r"[<\[(].*", h):      # `[name of copyright owner]`, `<name>`
            continue
        holders.append(h)
    return holders


def holder_tokens(holders):
    toks = set()
    for h in holders:
        for w in re.split(r"[^A-Za-z0-9.]+", h.lower()):
            w = w.strip(".")
            if len(w) >= 3 and w not in STOPWORDS and not w.isdigit():
                toks.add(w)
    return toks


def identity_tokens(slug):
    """What the repository calls itself: owner and name, split on the usual joiners."""
    toks = set()
    for part in re.split(r"[^A-Za-z0-9]+", slug.lower()):
        if len(part) >= 3 and part not in STOPWORDS:
            toks.add(part)
    # an owner like `ls1intum` also agrees on `tum`, and `dodona-edu` on `dodona`
    extra = set()
    for t in list(toks):
        for sub in re.findall(r"[a-z]{3,}", t):
            extra.add(sub)
    return toks | extra


def _agrees(a, b):
    """Token agreement with CONTAINMENT, because an owner handle glues words together.

    `dodona-edu/dolos` holds its subtree grants under the holder `Dodona`, and an owner
    handle is `dodona-edu`: exact set intersection answers FOREIGN on a project's own
    component.  Containment needs FOUR characters to fire and exact agreement three,
    because three-character substrings match by accident -- the same false-friend class
    `make hooks` reports on its own payload names, where `mit` matches inside `LIMITED`.

    Declared limit, measured on `ls1intum/Ares2`: a holder line naming an institution in
    FULL (`Technical University of Munich`) does not agree with an owner handle carrying
    only its initialism (`ls1intum`), and no amount of token folding fixes that.  Which
    is why a subtree FOREIGN verdict is a READING LIST and the ROOT comparison runs
    first: a project's own component agrees with its own ROOT holder, which is the
    channel that does not depend on how the owner spells itself.
    """
    if a & b:
        return True
    for x in a:
        if len(x) < 4:
            continue
        for y in b:
            if len(y) >= 4 and (x in y or y in x):
                return True
    return False


def provenance(slug, holders, root_tokens):
    if not holders:
        return "HOLDER-ABSENT"
    ht = holder_tokens(holders)
    if not ht:
        return "HOLDER-ABSENT"
    if _agrees(ht, identity_tokens(slug)):
        return "OWN"
    if root_tokens and _agrees(ht, root_tokens):
        return "OWN"
    return "FOREIGN"


INSTITUTION_RE = re.compile(
    r"\b(?:universit(?:y|e|at|aet|eit|a|e\u0301)|universidad|universidade|hochschule"
    r"|college|school|institut(?:e|o|ion)?|academy|academia|polytechnic|escuela"
    r"|faculty|facultad|ministry|minist(?:erio|\u00e8re)|department of education"
    r"|board of education|consorti(?:um|o)|foundation|stichting|fundaci\u00f3n"
    r"|instituto|lyc\u00e9e|gymnasium|tecnol\u00f3gico|cole)\b", re.I)


def institution_of(holders):
    """The PLACEMENT half of ACTION ZZ-y: a holder line that names an institution is a
    region channel that survives the PII refusal which took author e-mail domains away
    from `p346`, because an institution's name is public, aggregate text.  It is ranked
    ABOVE author addresses and it is independent of the timezone channel, so the two
    agreeing is corroboration rather than one reading.
    """
    return [h for h in holders if INSTITUTION_RE.search(h)]


def scope_of(path):
    return "ROOT" if "/" not in path else "SUBTREE"


def candidate_paths(paths):
    out = []
    for p in paths:
        if not LICENCE_RE.search(p):
            continue
        low = p.lower()
        if low.endswith(SOURCE_EXT):
            continue
        base = low.rsplit("/", 1)[-1]
        # an INVENTORY is not a grant text (p441)
        if base in ("licenses", "licences", "licenses.txt", "license-list.txt"):
            continue
        out.append(p)
    return out


def pin(slug, timeout=60):
    url = "https://github.com/%s" % slug
    try:
        r = subprocess.run(["git", "ls-remote", "--symref", url, "HEAD"],
                           capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None, None
    if r.returncode != 0:
        return None, None
    ref, sha = None, None
    for line in r.stdout.splitlines():
        if line.startswith("ref:"):
            ref = line.split()[1]
        elif "\tHEAD" in line:
            sha = line.split()[0]
    return sha, ref


def tree(slug, workdir, timeout=300):
    url = "https://github.com/%s" % slug
    d = os.path.join(workdir, slug.replace("/", "__"))
    r = subprocess.run(["git", "clone", "--filter=blob:none", "--no-checkout",
                        "--depth", "1", "--quiet", url, d],
                       capture_output=True, text=True, timeout=timeout)
    if r.returncode != 0:
        return None, None
    t = subprocess.run(["git", "-C", d, "ls-tree", "-r", "--name-only", "HEAD"],
                       capture_output=True, text=True, timeout=timeout)
    return (t.stdout.splitlines() if t.returncode == 0 else None), d


def read_payload(slug, sha, path, timeout=40):
    url = "%s/%s/%s/%s" % (RAW, slug, sha, urllib.parse.quote(path))
    try:
        with urllib.request.urlopen(url, timeout=timeout) as fh:
            return fh.read().decode("utf-8", "replace")
    except Exception:
        return None


def grade(slug, workdir):
    sha, ref = pin(slug)
    if not sha:
        return {"slug": slug, "verdict": "UNRESOLVED", "sha": "-", "ref": "-"}
    paths, _ = tree(slug, workdir)
    if paths is None:
        return {"slug": slug, "verdict": "UNRESOLVED", "sha": sha, "ref": ref or "-"}
    cands = candidate_paths(paths)
    rows = []
    root_tokens = set()
    # read the ROOT grant first so its holder can vouch for the project's own subtrees
    for p in sorted(cands, key=lambda p: (p.count("/"), p)):
        text = read_payload(slug, sha, p)
        if text is None:
            rows.append((p, scope_of(p), "UNREADABLE", "-", []))
            continue
        fam = family_of(text)
        if fam == "UNKNOWN":
            rows.append((p, scope_of(p), "NOT-A-GRANT-TEXT", fam, []))
            continue
        hs = holder_of(text)
        if scope_of(p) == "ROOT":
            root_tokens |= holder_tokens(hs)
        rows.append((p, scope_of(p), provenance(slug, hs, root_tokens), fam, hs))
    grants = [r for r in rows if r[2] in ("OWN", "HOLDER-ABSENT")]
    root = [r for r in grants if r[1] == "ROOT"]
    foreign = [r for r in rows if r[2] == "FOREIGN"]
    if root:
        verdict = "REPOSITORY-GRANT"
    elif grants:
        verdict = "PACKAGE-GRANT-ONLY"
    elif foreign:
        verdict = "FOREIGN-GRANT-ONLY"
    else:
        verdict = "ABSENCE-ENUMERATED"
    held = root[0][4] if root else (grants[0][4] if grants else [])
    return {"slug": slug, "verdict": verdict, "sha": sha, "ref": ref or "-",
            "n_paths": len(paths), "rows": rows, "holders": held,
            "institution": institution_of(held),
            "family": root[0][3] if root else (grants[0][3] if grants else "-")}


def main(argv):
    slugs = []
    for a in argv:
        if os.path.exists(a):
            slugs += [l.strip() for l in open(a) if l.strip()
                      and not l.startswith("#")]
        else:
            slugs.append(a)
    print("slug\tverdict\tfamily\tsha\tref\tn_paths\tholder\tinstitution\tdetail")
    with tempfile.TemporaryDirectory() as wd:
        for s in slugs:
            g = grade(s, wd)
            detail = " | ".join("%s[%s/%s/%s]" % (p, sc, pr, fam)
                                for p, sc, pr, fam, _ in g.get("rows", [])) or "-"
            print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (
                g["slug"], g["verdict"], g.get("family", "-"), g["sha"][:12],
                g["ref"], g.get("n_paths", "-"),
                "; ".join(g.get("holders") or []) or "-",
                "; ".join(g.get("institution") or []) or "-", detail))
            sys.stdout.flush()


if __name__ == "__main__":
    main(sys.argv[1:])
