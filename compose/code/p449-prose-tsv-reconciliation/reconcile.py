#!/usr/bin/env python3
"""p449 -- the gate this corpus has needed for two passes: PROSE against DATA.

Pass 26's closing sentence was a diagnosis and not a fix:

    "Four of this pass's five findings are instruments disagreeing with sentences in
     these files, and in four cases out of four the sentence was right. A corpus that
     versions both prose and instruments has to reconcile them, and nothing in this
     repository did -- `p342` explicitly chose the other direction, asserting
     *'against the TSVs, not against the prose'*."

Pass 28 then ran three unrelated pre-registered actions and landed in the same place a
THIRD time. Every licence fact its sweeps surfaced was already written, correctly, in
these files:

    axe-core, OCRmyPDF, coqui-ai/TTS, idiap/coqui-ai-TTS, edrys-org/edrys
        `repos/foundations.md` carries a TABLE, written in pass 26, with the
        heading "Filed | Actually" and the five rows GPL -> MPL-2.0, and the
        sentence "the prose was right and the measurement was wrong".
        `p436`'s `payloads.tsv` still says GPL for all five.
    Opetushallitus/valtionavustus     published EUPL-1.1 in prose; UNKNOWN in the TSV.
    sign/translate                    published "Non-OSI, dual-tier" in three files;
                                      CC-BY in the TSV.
    seamless_communication            published "CC BY-NC-4.0 -- Hard reject"; CC-BY.

So the defect is not any one classifier. It is that this corpus has TWO layers that can
disagree and NO instrument that notices. Pass 26 corrected the classifiers and never
re-ran them over the shelf, so its own corrections never reached the data -- which means
the reconciliation debt is self-inflicted and recurring, not a legacy.

**P450: a corpus that versions prose and data must gate them against each other.**
The prose is the human layer and has been right four times out of four; the TSV is what
a compiler reads. Where they disagree, this gate says so and names the file and line.

## The binding problem, and why this does not re-import `P385`

Harvesting "the licence of X" from prose is a binding task, and this KB already measured
how badly a naive binding performs: `P385` found that anchoring to the LINE gives an
INTERVAL `[3, 22]` rather than a number, because a permissive matcher ties every repo on
a line to every licence on it, and `P391` narrowed it to `[5, 14]` by reading the CELL
and the typed COLUMN instead.

So this gate binds conservatively and REFUSES rather than guesses:

    table row   a slug in a cell binds to licence tokens in THE SAME CELL; failing
                that, to the row's tokens only when the row names exactly ONE slug
    prose line  binds only when the line names exactly ONE slug
    otherwise   UNBINDABLE, counted and published, never guessed

A refusal is a measurement (`P160`, `P184`): the denominator is published next to it.

Verdicts per (slug, file, line):
    AGREE        prose family == the family measured today
    CONTRADICT   both known and different  -- the actionable class
    STALE-DATA   prose agrees with today's measurement, the PUBLISHED TSV does not
                 (so the prose was right and the data is behind -- pass 26's class)
    PROSE-ONLY   prose names a family for a slug the data layer has no row for
    UNBINDABLE   a slug and a licence token co-occur but the binding rules refuse
"""

import os
import re
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))

SLUG_RE = re.compile(r"(?<![A-Za-z0-9_./-])([A-Za-z0-9][A-Za-z0-9_.-]{0,38})"
                     r"/([A-Za-z0-9][A-Za-z0-9_.-]{0,99})(?![A-Za-z0-9_./-])")

# Licence tokens as this KB's PROSE spells them, longest-first so `CC BY-NC-SA` wins
# over `CC BY` and `AGPL-3.0` over `GPL`.  Order is the whole function, again.
LICENCE_TOKENS = [
    (r"CC\s*BY-NC-SA(?:\s*4\.0)?", "CC-BY", "NC+SA"),
    (r"CC\s*BY-NC(?:-4\.0|\s*4\.0)?", "CC-BY", "NC"),
    (r"CC\s*BY-SA(?:\s*[34]\.0)?", "CC-BY", "SA"),
    (r"Attribution-NonCommercial-ShareAlike", "CC-BY", "NC+SA"),
    (r"Attribution-NonCommercial", "CC-BY", "NC"),
    (r"Attribution-ShareAlike", "CC-BY", "SA"),
    (r"CC0(?:-1\.0)?", "CC0-1.0", ""),
    (r"CC\s*BY(?:\s*4\.0)?", "CC-BY", ""),
    (r"Creative\s+Commons", "CC-BY", ""),
    (r"AGPL(?:-3\.0|\s*3)?", "AGPL-3.0", ""),
    (r"LGPL(?:-[23]\.[01])?", "LGPL", ""),
    (r"GPL(?:-[23]\.0|v[23])?", "GPL", ""),
    (r"MPL(?:-2\.0)?", "MPL-2.0", ""),
    (r"EUPL(?:-1\.[12])?", "EUPL", ""),
    (r"EPL(?:-[12]\.0)?", "EPL", ""),
    (r"Apache(?:\s+Licen[cs]e)?(?:[-\s]*2\.0)?", "Apache-2.0", ""),
    (r"ECL(?:-2\.0)?", "ECL-2.0", ""),
    (r"BSD(?:-[23](?:-Clause)?)?", "BSD", ""),
    (r"\bISC\b", "ISC", ""),
    (r"\bUnlicense\b", "Unlicense", ""),
    (r"\bMIT\b", "MIT", ""),
    (r"MulanPSL(?:-2\.0)?", "MulanPSL", ""),
]
# `P451`: EVERY token is anchored with \b on both sides, and that is not cosmetic.
# The first build of this gate wrote these patterns bare, and the acronyms are common
# English substrings:
#
#     MPL   matches inside "exa|mpl|e"   -> blackboard/BBDN-lti-1p3-tool-example and
#                                            UOC/java-lti-1.3-provider-example were
#                                            both reported as prose-claims of MPL-2.0
#     ECL   matches inside "edgam|ecl|aw" -> yh2072/edgameclaw read as ECL-2.0
#
# Pass 26 found this exact defect one function away and one pass earlier: its finding 2
# was the bare pattern `r"UNLICENSE"` matching inside `UNLICENSED`, npm's documented
# value for a REFUSAL to grant, which it had classified as the most permissive licence
# in the table.  A from-scratch instrument re-imported the known defect (`p432`), which
# is the third time this corpus has done that.
_LIC_RE = [(re.compile(r"\b(?:%s)\b" % p, re.I), fam, qual)
           for p, fam, qual in LICENCE_TOKENS]

# A licence token inside one of these is NOT a claim about the slug beside it: it is
# this KB narrating a past error, a refusal or somebody else's grant.  Derived from the
# lines that forced each one, not guessed.
NEGATED_RE = re.compile(
    r"\bnot\b|\bwas\b|\bfiled\b|\bwrongly\b|\bincorrect|\binstead of\b|\brather than\b"
    r"|\bno longer\b|\bused to\b|\bclaim(?:s|ed)?\b|\bbadge\b|\bassert|\bungranted\b"
    r"|\bvendored\b|\bdependenc|\bupstream\b|\bfork\b|\bUNKNOWN\b|\bsecondary licen"
    r"|\bcompatible licen|\bexception\b", re.I)


def licence_tokens(text):
    """Every (family, qualifier) this text names, longest-token-first, non-overlapping."""
    found, spans = [], []
    for rx, fam, qual in _LIC_RE:
        for m in rx.finditer(text):
            if any(m.start() < e and s < m.end() for s, e in spans):
                continue
            spans.append((m.start(), m.end()))
            found.append((fam, qual, m.group(0)))
    return found


# A URL is the most common way this corpus names a repository, and the slug regex
# cannot start inside one: its left look-behind rejects the `/` of `github.com/`.  The
# first build therefore found NOTHING in `github.com/oat-sa/qti-sdk` -- caught by the
# control, not by the sweep.  Hosts are stripped before extraction.
HOST_RE = re.compile(r"\b(?:https?://)?(?:www\.)?(?:raw\.githubusercontent\.com"
                     r"|github\.com|gitlab\.com|codeload\.github\.com)/", re.I)
# An owner segment that is really a branch, a ref or a directory.  `main/LICENSE` has
# exactly the shape of a slug, and the first build bound the licence of every row to it
# instead of to the repository: the cell `**MIT** (`main/LICENSE`)` contains one
# slug-shaped token, so the one-slug-per-cell rule fired on the PATH.
NOT_OWNER = {"main", "master", "head", "blob", "tree", "raw", "refs", "heads", "tags",
             "docs", "doc", "src", "dist", "lib", "libs", "test", "tests", "api",
             "www", "en", "release", "releases", "archive", "commit", "commits"}
NUMERIC_RE = re.compile(r"^[v.\d]+$", re.I)
FILENAME_RE = re.compile(r"\.(?:md|markdown|rst|txt|py|js|ts|json|ya?ml|toml|xml|cfg"
                         r"|ini|lock|sh|php|java|rb|go|rs|html?|svg|png|pdf|csv|tsv"
                         r"|lesser|gpl)$", re.I)


def slugs_in(text):
    out = []
    for m in SLUG_RE.finditer(HOST_RE.sub(" ", text)):
        owner, repo = m.group(1), m.group(2)
        if owner.lower() in NOT_OWNER:
            continue
        if NUMERIC_RE.match(owner) or NUMERIC_RE.match(repo):
            continue
        # a licence FILENAME is not a repository: LICENSE, COPYING, LICENCE.TXT
        if repo.isupper() and len(repo) > 2:
            continue
        if FILENAME_RE.search(repo):
            continue
        out.append("%s/%s" % (owner, repo))
    return out


def claims_in_line(line):
    """[(slug, family, qualifier, binding)] with the conservative rules of P391."""
    out = []
    if line.lstrip().startswith("|"):
        cells = [c for c in line.split("|")]
        row_slugs = [s for c in cells for s in slugs_in(c)]
        for c in cells:
            cs, ct = slugs_in(c), licence_tokens(c)
            # ONE slug per cell, or refuse.  `P385` measured line-anchored binding as
            # an INTERVAL rather than a number because a permissive matcher ties every
            # repo on a line to every licence on it; the first build of this gate
            # re-imported that at CELL level and reported `frappe/erpnext` as a prose
            # claim of AGPL-3.0 from `repos/foundations.md:607`, whose cell reads
            # "kuali/kc | AGPL-3.0 ... after `frappe/lms` and `frappe/erpnext`" --
            # three slugs, one licence, and the licence belongs to the first.
            if len(set(cs)) == 1 and ct and not NEGATED_RE.search(c):
                for fam, qual, _raw in ct:
                    out.append((cs[0], fam, qual, "cell"))
        if not out and len(set(row_slugs)) == 1:
            # the typed-column case: one slug in the row, licence in another cell
            for c in cells:
                if slugs_in(c) or NEGATED_RE.search(c):
                    continue
                for fam, qual, _raw in licence_tokens(c):
                    out.append((row_slugs[0], fam, qual, "row"))
        return out, (bool(row_slugs) and not out)
    ls, lt = slugs_in(line), licence_tokens(line)
    if len(set(ls)) == 1 and lt and not NEGATED_RE.search(line):
        for fam, qual, _raw in lt:
            out.append((ls[0], fam, qual, "line"))
        return out, False
    return out, bool(ls and lt)


def main():
    md_files = sys.argv[1:-2] if len(sys.argv) > 3 else []
    measured_tsv, published_tsv = sys.argv[-2], sys.argv[-1]

    measured, published = {}, {}
    with open(measured_tsv) as f:
        next(f)
        for line in f:
            p = line.rstrip("\n").split("\t")
            if len(p) > 4:
                measured[p[0].lower()] = p[4]
    with open(published_tsv) as f:
        for line in f:
            p = line.rstrip("\n").split("\t")
            if len(p) > 4 and p[1] == "LICENSED":
                published[p[0].lower()] = p[4]

    claims = defaultdict(list)
    unbindable = 0
    for path in md_files:
        if not os.path.exists(path):
            continue
        for i, line in enumerate(open(path, errors="replace"), 1):
            got, unb = claims_in_line(line)
            unbindable += 1 if unb else 0
            for slug, fam, qual, binding in got:
                claims[slug.lower()].append((fam, qual, path, i, binding))

    rows, counts = [], Counter()
    for slug, cl in sorted(claims.items()):
        if slug not in measured:
            counts["PROSE-ONLY"] += 1
            continue
        today, pub = measured[slug], published.get(slug, "-")
        fams = {f for f, _q, _p, _i, _b in cl}
        # The prose is a whole corpus talking about a repo over many passes; a slug
        # whose prose mentions DISAGREE WITH EACH OTHER is its own class and must not
        # be scored as agreement just because one mention happens to match.
        if today == "UNKNOWN":
            # `P160`/`P184`: an instrument that declined to answer has not contradicted
            # anything.  The first build scored these as CONTRADICT, which counted the
            # classifier's own gaps as prose errors -- six of its eleven.
            counts["DATA-ABSTAINS"] += 1
            rows.append((slug, "DATA-ABSTAINS", today, pub,
                         ",".join(sorted(fams)),
                         "%s:%d" % (cl[0][2], cl[0][3]), cl[0][4], len(cl)))
            continue
        if len(fams) > 1:
            verdict = ("PROSE-SELF-INCONSISTENT" if today not in fams
                       else "PROSE-MIXED-INCLUDES-TODAY")
        elif today in fams:
            verdict = "STALE-DATA" if pub not in (today, "-") else "AGREE"
        else:
            verdict = "CONTRADICT"
        counts[verdict] += 1
        f0, q0, p0, i0, b0 = cl[0]
        rows.append((slug, verdict, today, pub, ",".join(sorted(fams)),
                     "%s:%d" % (p0, i0), b0, len(cl)))

    with open(os.path.join(HERE, "reconcile.tsv"), "w") as f:
        f.write("slug\tverdict\tmeasured_today\tpublished_tsv\tprose_families"
                "\tfirst_citation\tbinding\tn_mentions\n")
        for r in rows:
            f.write("\t".join(str(x) for x in r) + "\n")

    print("## p449 -- prose vs data, over %d markdown files" % len(md_files))
    print("## slugs with at least one BOUND licence claim in prose: %d" % len(claims))
    print("## lines where a slug and a licence co-occur and binding REFUSED: %d"
          % unbindable)
    print()
    for k, v in counts.most_common():
        print("  %-26s %d" % (k, v))
    print()
    print("### 🔴 CONTRADICT -- prose and today's measurement disagree")
    for r in rows:
        if r[1] == "CONTRADICT":
            print("  %-46s prose=%-22s today=%-11s %s" % (r[0], r[4], r[2], r[5]))
    print()
    print("### 🟡 STALE-DATA -- prose right, published TSV behind (pass 26's class)")
    for r in rows:
        if r[1] == "STALE-DATA":
            print("  %-46s prose=%-12s today=%-11s tsv=%-11s %s"
                  % (r[0], r[4], r[2], r[3], r[5]))


if __name__ == "__main__":
    main()
