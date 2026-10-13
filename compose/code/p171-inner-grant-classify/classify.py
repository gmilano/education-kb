#!/usr/bin/env python3
"""ACTION JK - classify the inner grant BODIES that P170-A counts, by FAMILY, deduplicated by BLOB.

P170-A step 2 decides IF a candidate carries a grant. This adds the step after it: WHICH grant,
and is it COMPATIBLE with the repository's outer grant.

Two rules inherited from P170-A, both load-bearing:
  step 4  MULTI-FAMILY: count families PER FILE, never first-match-wins. An ordered case statement
          reads a 3-package bundle as whichever family it tests for first.
  step 5  ELECTION: a dual licence is an OPTION, not an obligation. "MIT or GPLv3" -> elect MIT and
          RECORD the election. An EPL-2.0 Exhibit A naming a secondary licence is an unfilled FORM.

Reads blob bodies on stdin as NUL-delimited "path\\0blobsha\\0body\\0" records so one subprocess
serves the whole tree, and no body is ever re-fetched.
"""
import re
import sys

# Family predicates. Deliberately keyed on OPERATIVE text, not on a name or an SPDX tag, because
# T213 established that a label is not a grant -- in both directions.
# ---------------------------------------------------------------------------
# P171-A. FAMILY IDENTITY COMES FROM THE TITLE, NOT FROM ANYWHERE IN THE BODY.
#
# p171's first attempt matched family names anywhere in the body, case-insensitively, and was
# wrong on 3 of Sakai's 72 blobs -- caught by READING them, not by the tally:
#   * LGPL-2.1 verbatim (26 426 B) was read as "GPL+LGPL", because LGPL-2.1's OWN TEXT names the
#     ordinary "GNU General Public License" in prose -- its section 3 offers relicensing under the
#     GPL. A prose reference to another licence is not a second grant.
#   * licenses/junit-3.8.1.license.txt was read as "GPL+MPL+Python". Its body is the IBM PUBLIC
#     LICENSE Version 1.0, a family the first attempt did not know, so every hit was a prose
#     reference in IPL's own comparison clauses. Wrong on all three families at once.
# This is T213's class again -- a predicate deciding a legal question from a string -- one level in.
#
# So: TITLE patterns are anchored to a line of their own (the heading), and prose references are
# kept in a SEPARATE informational column. LGPL is tested before GPL and consumes its line.
# ---------------------------------------------------------------------------

# (name, title-line pattern). Matched against lines, not the whole blob.
FAMILY_TITLES = [
    ("AGPL-3.0",   r"^\s*GNU AFFERO GENERAL PUBLIC LICENSE\s*$"),
    ("LGPL",       r"^\s*GNU LESSER GENERAL PUBLIC LICENSE\s*$"),
    ("LGPL",       r"^\s*GNU LIBRARY GENERAL PUBLIC LICENSE\s*$"),
    ("GPL",        r"^\s*GNU GENERAL PUBLIC LICENSE\s*$"),
    ("ECL-2.0",    r"^\s*(?:The )?Educational Community License,? Version 2\.0\s*$"),
    ("Apache-2.0", r"^\s*Apache License\s*$"),
    ("EPL",        r"^\s*Eclipse Public License\b.*$"),
    ("IPL-1.0",    r"^\s*IBM Public License Version 1\.0\s*$"),
    ("CPL-1.0",    r"^\s*Common Public License\b.*$"),
    ("MPL",        r"^\s*MOZILLA PUBLIC LICENSE\s*$"),
    ("MPL",        r"^\s*Mozilla Public License,? Version \d",),
    ("CDDL",       r"^\s*COMMON DEVELOPMENT AND DISTRIBUTION LICENSE\b.*$"),
    ("Artistic",   r"^\s*The Artistic License\b.*$"),
    ("OFL",        r"^\s*SIL OPEN FONT LICENSE\b.*$"),
    ("Python",     r"^\s*PYTHON SOFTWARE FOUNDATION LICENSE\b.*$"),
    ("WTFPL",      r"^\s*DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE\s*$"),
    ("CC",         r"^\s*Creative Commons\b.*$"),
]

# Grants that have no title line because the grant IS the sentence. Matched on the whole body.
FAMILY_SENTENCES = [
    ("MIT",        r"Permission is hereby granted, free of charge"),
    ("ISC",        r"Permission to use, copy, modify, and/or distribute"),
    ("BSD",        r"Redistributions of source code must retain"),
    ("Unlicense",  r"free and unencumbered software released into the public domain"),
    ("Zlib",       r"This software is provided ['\"]as-is['\"]"),
    # Apache's SHORT FORM notice, used where the full text is not shipped.
    ("Apache-2.0", r"[Ll]icensed under the Apache License,? Version 2\.0"),
    ("ECL-2.0",    r"[Ll]icensed under the Educational Community License"),
    # GNU SHORT-FORM notices. A 300-byte license.md that points at gnu.org is still a grant
    # statement, and the full-text title patterns cannot see it (Moodle's bundled TinyMCE).
    # MD = Markdown link/emphasis punctuation, which sits between the verb and the licence name
    # in real notices: "terms of [GNU General Public License Version 2 or later](http://...)".
    # Formatting, not law, is what defeats these patterns -- so the patterns tolerate formatting.
    ("AGPL-3.0",   r"(?:[Ll]icensed under|terms of)(?:\s+the)?[\s\[\(*]*GNU Affero General Public License"),
    ("LGPL",       r"(?:[Ll]icensed under|terms of)(?:\s+the)?[\s\[\(*]*GNU (?:Lesser|Library) General Public License"),
    ("GPL",        r"(?:[Ll]icensed under|terms of)(?:\s+the)?[\s\[\(*]*GNU General Public License"),
]

# Prose references: recorded, never counted as a grant. This column is what makes the
# LGPL-names-the-GPL case legible instead of invisible.
MENTIONS = [
    ("GPL",  r"GNU General Public License"),
    ("LGPL", r"GNU Lesser General Public License|GNU Library General Public License"),
    ("MPL",  r"Mozilla Public License"),
    ("CPL",  r"Common Public License"),
    ("EPL",  r"Eclipse Public License"),
]

# The falsifier's own terms: a body is HOSTILE if it withholds commercial use or redistribution.
# Phrased to catch the obligation, not the word -- "commercial" appears innocently in MIT's
# "including without limitation the rights to use, copy, modify, merge, publish, distribute".
# GPL-3.0 section 6(b) permits one alternative conveying method "only occasionally and
# noncommercially". That is a condition on a DISTRIBUTION METHOD inside the GPL itself, not a
# non-commercial restriction on the software -- so every full GPL-3.0 body trips a naive search.
# It did: 4 of Moodle's 6 raw hostile hits were this one clause, including Moodle's own COPYING.txt.
GPL_S6_CARVEOUT = r"allowed only occasionally and noncommercially"

HOSTILE = [
    ("non-commercial",   r"[Nn]on-?[Cc]ommercial(?! use is permitted| and [Cc]ommercial)"),
    ("no-commercial-use", r"not (?:be )?(?:used|be used) for commercial"),
    ("evaluation-only",  r"for evaluation purposes only"),
    ("proprietary",      r"[Pp]roprietary and [Cc]onfidential"),
    ("no-redistribution", r"may not be (?:redistributed|distributed|copied)"),
    ("all-rights-reserved-bare", r"All [Rr]ights [Rr]eserved\.?\s*$"),
]

# A dual grant is an OPTION. Recorded, never counted as an obligation (P170-A step 5).
ELECTION = r"(?:either|at your option|dual[- ]licen[cs]ed|or, at your|licensed under either)"


def classify(body):
    # Licence documents ship as Markdown too, where the title is "# Apache License" and the
    # heading marker defeats a line-anchored plain-text pattern (Moodle's bundled aws-sdk).
    # Strip Markdown heading markers and emphasis before title matching, never before body matching.
    lines = [re.sub(r"^[#>\s]*", "", l).replace("**", "").strip()
             for l in body.splitlines()]
    # Licence texts are HARD-WRAPPED at ~70 columns, so any multi-word phrase search must run on
    # whitespace-normalised text or it silently UNDER-reads: LGPL-2.1 contains the phrase
    # "GNU General Public\nLicense" split across a line break, and a flat search misses it.
    # p171's own regression test caught this -- the fixture matched nothing where the real body did.
    # Titles stay LINE-anchored, which is the whole point of P171-A.
    flat = re.sub(r"\s+", " ", body)
    fams = set()
    for name, pat in FAMILY_TITLES:
        rx = re.compile(pat, re.IGNORECASE)
        if any(rx.match(l) for l in lines):
            fams.add(name)
    # LGPL's title also satisfies nothing else; but a document titled LGPL must not also be
    # reported as GPL on the strength of its own section 3. Title matching already prevents that
    # -- this assertion keeps it true if a pattern is ever loosened.
    if "LGPL" in fams and "GPL" in fams:
        gpl_titles = [l for l in lines
                      if re.match(r"^\s*GNU GENERAL PUBLIC LICENSE\s*$", l, re.IGNORECASE)]
        if not gpl_titles:
            fams.discard("GPL")
    for name, pat in FAMILY_SENTENCES:
        if name in fams:
            continue
        if re.search(pat, flat, re.IGNORECASE):
            fams.add(name)
    mentions = sorted({name for name, pat in MENTIONS
                       if re.search(pat, flat)} - fams)
    # Strip the GPL section 6(b) clause before testing for withheld commercial rights.
    flat_for_hostile = re.sub(GPL_S6_CARVEOUT, " ", flat)
    hostile = sorted({name for name, pat in HOSTILE if re.search(pat, flat_for_hostile)})
    if "all-rights-reserved-bare" in hostile and fams:
        hostile.remove("all-rights-reserved-bare")
    election = bool(re.search(ELECTION, flat, re.IGNORECASE)) and len(fams) > 1
    return sorted(fams), hostile, election, mentions


def read_records(stream):
    """Parse NUL-delimited path\\0blob\\0body\\0 triples."""
    parts = stream.read().split("\0")
    for i in range(0, len(parts) - 2, 3):
        yield parts[i], parts[i + 1], parts[i + 2]


def main():
    repo = sys.argv[1] if len(sys.argv) > 1 else "?"
    outer = sys.argv[2] if len(sys.argv) > 2 else "?"
    by_blob = {}
    paths = 0
    for path, blob, body in read_records(sys.stdin):
        if not blob:
            continue
        paths += 1
        if blob not in by_blob:
            by_blob[blob] = (classify(body), [path], len(body))
        else:
            by_blob[blob][1].append(path)

    print(f"# repo\t{repo}\touter_grant\t{outer}")
    print(f"# grant paths {paths}\tdistinct blobs {len(by_blob)}")
    print("blob\tfamilies\tn_families\telection\thostile\tprose_mentions\tbytes\tn_paths\texample_path")
    fam_tally, hostile_rows, multi = {}, [], 0
    for blob, ((fams, hostile, election, mentions), plist, nbytes) in sorted(
            by_blob.items(), key=lambda kv: (-len(kv[1][1]), kv[0])):
        key = "+".join(fams) if fams else "NONE"
        fam_tally[key] = fam_tally.get(key, 0) + 1
        if len(fams) > 1:
            multi += 1
        if hostile:
            hostile_rows.append((blob, key, hostile, plist))
        print(f"{blob}\t{key}\t{len(fams)}\t{'yes' if election else 'no'}"
              f"\t{','.join(hostile) or '-'}\t{','.join(mentions) or '-'}"
              f"\t{nbytes}\t{len(plist)}\t{plist[0]}")

    print(f"# FAMILY TALLY (by distinct blob), {len(by_blob)} blobs")
    for k, v in sorted(fam_tally.items(), key=lambda kv: -kv[1]):
        print(f"#   {v:4d}  {k}")
    print(f"# multi-family blobs: {multi}")
    print(f"# HOSTILE blobs: {len(hostile_rows)}")
    for blob, key, hostile, plist in hostile_rows:
        print(f"#   {blob}  {key}  {','.join(hostile)}  {plist[0]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
