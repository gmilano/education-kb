#!/usr/bin/env python3
"""derive-counts.py -- the general form of Gap 543-E / 534-E / 544-E.

ONE defect class, now caught three times in three different files:
  * p543 -- agents/top.md's shelf heading, stale by a whole pass
  * p545 -- repos/foundations.md's "seventy-two" against a derived 156 (pass arithmetic
            frozen at p534 while nine later passes filed rows)
  * p545 -- compose/patterns.md's "Thirty-eight" against 47 recipes actually present

The class is: A COUNT WRITTEN IN PROSE BESIDE THE ROWS IT COUNTS. It goes stale the moment
a pass adds a row and forgets the sentence, and no amount of care prevents it -- only
derivation does.

This script derives every such count that CAN be derived from a page's own structure, and
abstains loudly where it cannot. repos/foundations.md needs a declared disposition per
table and is handled by its own script, derive-foundations.py, which this one defers to.

usage: python3 -I ingest/derive-counts.py [repo-root]
exit 0 all green / 1 a header disagrees with its page / 2 a page could not be parsed
"""
import os
import re
import sys

root = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rc = 0

def header_of(path, lines=40):
    return "\n".join(open(path, encoding="utf-8").read().split("\n")[:lines])


def claim_in(path, noun):
    """Read an EXPLICIT machine-readable claim: 'derived <noun>: **N**'.

    p545's first draft matched any '**N** recipes' in the header and picked up the digit
    inside its own retraction sentence ("this page held **47** recipes"), reporting RED on
    a page that was right. A count claim must be unambiguous to a reader AND to the gate,
    so the page carries one marked form and the gate reads only that.
    """
    m = re.search(r"derived %s: \*\*(\d+)\*\*" % re.escape(noun), header_of(path), re.I)
    return int(m.group(1)) if m else None


# --- compose/patterns.md: recipes are '## [marks] P-<n>-<X> — ...' ------------------------
# p568: the id scheme on the page is FAMILY-SUFFIXED -- 'P-571-A', not 'P571'. The original
# pattern (r"P(\d+) —") matched none of the 17 headings present, so `ids` came back empty and
# `ids[0]` raised IndexError at this line, ABORTING THE WHOLE GATE before agents/top.md and
# intel/trends.md were ever reached. Two fixes, both deliberate:
#   * accept the hyphenated, letter-suffixed form (and the bare 'P<n>' form, for history);
#   * count RECIPE HEADINGS, not distinct family numbers -- 'P-571-A' and 'P-571-B' are two
#     recipes, and counting families under-reported a page that carries several per family.
# Contiguity is still checked over the FAMILY numbers, which is where a missing id is a signal.
pat = os.path.join(root, "compose", "patterns.md")
if os.path.exists(pat):
    body = open(pat, encoding="utf-8").read()
    found = re.findall(r"^## [^A-Za-z0-9]*P-?(\d+)(?:-([A-Z]))? —", body, re.M)
    n = len(found)
    fams = sorted({int(num) for num, _ in found})
    gaps = [i for i in range(fams[0], fams[-1] + 1) if i not in fams] if fams else []
    claimed = claim_in(pat, "recipes")
    if not found:
        print("compose/patterns.md   recipes: ABSTAIN -- no recipe heading matched; id scheme changed?")
        rc = 2
    else:
        rng = f"P-{fams[0]}..P-{fams[-1]}"
        print(f"compose/patterns.md   recipes: derived={n}  families={len(fams)}  range={rng}  claimed={claimed}")
    if gaps:
        print(f"  AMBER non-contiguous families: missing {['P-%d' % g for g in gaps]}")
    if not found:
        pass  # already abstained above; do not also grade a count we could not derive
    elif claimed is None:
        print("  AMBER no 'derived recipes: **N**' claim in the header.")
    elif claimed != n:
        print(f"  RED  header claims {claimed}, page holds {n} -- rewrite the header, not the page.")
        rc = 1
    else:
        print("  GREEN header agrees with its page.")

# --- intel/trends.md: trends are numbered '## <n>. ' or '## ... Trend <n>:' ---------------
tre = os.path.join(root, "intel", "trends.md")
if os.path.exists(tre):
    body = open(tre, encoding="utf-8").read()
    ids = {int(m) for m in re.findall(r"^## (\d+)\. ", body, re.M)}
    ids |= {int(m) for m in re.findall(r"^## .*?Trend (\d+):", body, re.M)}
    # p812: the ONLY id scheme this page has ever used is '## T<n> — ...'. The two patterns
    # above accept '## 31. ' and '## ... Trend 31:' and matched NEITHER of the 33 headings
    # present, so the gate reported derived=0/claimed=None -- an AMBER abstain, which in
    # `make hooks` output is indistinguishable from a pass -- for every pass since it was
    # written. Widened to the page's actual convention, exactly as p568 widened the recipe
    # pattern for family-suffixed ids ('P-571-A') and p718 replaced prose-keying with column
    # signatures. Same defect class, third file.
    ids |= {int(m) for m in re.findall(r"^## [^A-Za-z0-9]*T(\d+)\b", body, re.M)}
    n = len(ids)
    claimed = claim_in(tre, "trends")
    print(f"intel/trends.md       trends:  derived={n}  claimed={claimed}")
    if claimed is None:
        print("  AMBER no 'derived trends: **N**' claim in the header.")
    elif claimed != n:
        print(f"  RED  header claims {claimed}, page holds {n}.")
        rc = 1
    else:
        print("  GREEN header agrees with its page.")

# --- p718: all three shelves, located by COLUMN-HEADER SIGNATURE ------------------------
# 🔴 p718's primary finding. This block previously looked for the *wording* of the prose
# heading ('## Shelf', widened at p568 to '## The shelf'). agents/top.md's heading has since
# been reworded to '## The agents -- N rows', so the predicate stopped matching and the gate
# ABSTAINED -- silently passing -- on the one shelf it was built for. That is the THIRD time
# this same predicate has been defeated by a rewrite (p543 built it, p568 widened it, p718
# found it abstaining again), and in the interval foundations.md went stale by 10 and
# solutions.md by 5 while `make hooks` reported no count defect at all.
#
# 🟢 The fix is to stop keying on prose. A shelf table is identified by its own COLUMN-HEADER
# ROW -- a structural contract the shelves' own prose already says they use (`680-F2`) and
# which a rewrite of the surrounding sentence cannot touch. The count claim is then read from
# the nearest PRECEDING '## ' heading. Reword the heading however you like; the gate still
# finds the table and still grades the number in it.
# --- p813: ACTION p811-A, discharged with option (a) --------------------------------------
# 🔴 p811 recorded the defect: this list assumed ONE canonical table per file with a fixed
# column signature, while repos/foundations.md (14 tables) and verticals/solutions.md (10)
# are deliberately SECTIONED BY ARCHITECTURAL LAYER. Both files had been RED since p718 --
# not stale, not neglected, structurally ungradeable -- and the expected signatures below
# were additionally wrong on their face ('Licence' where both files write 'License',
# 'Default branch' and 'Branch | Stack' columns that have never existed).
#
# 🟢 p811 chose between (a) teach the gate a LIST of signatures per file and sum the rows,
# and (b) give each file one roll-up table and demote the layer tables to prose -- and chose
# (a), because the layering IS the value of those files. This is (a).
#
# 🟢 And it closes the defect CLASS, not just the instance. Every previous repair here
# (p543, p568, p718, p812) widened a predicate and left the gate able to go blind again the
# next time the pages changed shape. So the sum is now accompanied by UNCOUNTED-TABLE
# DETECTION: any table in the file whose body carries github.com addresses but whose header
# is not in the list below is a RED naming the line. A new layer table can be added freely;
# it cannot be added SILENTLY.
SHELVES = [
    ("agents/top.md", [
        "| Name | Repo | Licence | Stars | Region | Description |",
        # 🟢 p866 — 865-G1's repair. These two signatures carry HOLDINGS and were
        # counted NOWHERE: 36 rows under the seven-column shape (p857-p862 filed their agent
        # rows under it) and 4 under a shape whose own last column reads "Why it is a row".
        # They sat inside a 24-table standing RED on this shelf, which is exactly the
        # no-delta defect 865-G2 names. Declaring them raises the shelf from 495 to its
        # measured holding count; it does not add a single new row to the file.
        "| Agent | Repo | Licence, as measured | ★ / forks | Default ref · pushed | "
        "Region | What it actually does, and the posture |",
        "| Agent / library | Repo | License | ★ | Why it is a row |",
    ], [
        # 🟢 Declared NOT-counted, deliberately: the shelf figure is the build-safe table.
        # Declaring them is what makes the detector below meaningful -- an undeclared table
        # is an omission, a declared one is a decision.
        "| Agent | Repo | License | Stars | What it does |",            # copyleft
        "| Candidate | Repo | Actual license | Stars | Why rejected |",  # rejected
        # 🟢 p854: the DECLINES table of the non-English pass -- rows measured and refused,
        # with the probe that refused them.  Not counted: a decline is not a holding.
        "| Repo | \u2605 / forks | What was measured | Why it is NOT shelved |",
        # 🟢 p855: the LATAM grant CENSUS table -- verdict tallies over the 18-address
        # ENEM/exam estate, one row per p834-grantprobe verdict class.  Not counted: its
        # rows are VERDICTS over a population, not holdings, and the two addresses it
        # names are named precisely because they are NOT shelf rows (one dead, one
        # proprietary).  Declared rather than left silent -- p811's rule.
        "| Verdict | Count | What it means |",
        # 🟢 p858: the EXAMINED-AND-NOT-FILED table.  Declared NOT-counted: its rows
        # are refusals carrying the address that was refused, and a refusal is not a holding
        # (same reasoning as p854's DECLINES signature above).  Declared rather than left to
        # the uncounted-table detector, which is p811's rule.
        "| Not filed | Why |",
        # 🟢 p866 — the other half of 865-G1/865-G2. 62 rows in 14 tables on this
        # shelf are MEASUREMENTS, not holdings, and were indistinguishable from an
        # undeclared holdings table while every one of them sat in the same RED block.
        # Each is declared here with the reason, per p811: an undeclared table is an
        # omission, a declared one is a decision.
        "| Channel | Result |",                  # channel declarations (863-G1)
        "| Probe | Result |",                    # a single probe's outcome
        "| | |",                                 # continuation fragments, no header
        "| Address returned by a mandated generic leg | On a graded shelf? | "
        "In trending history? | New to this base? |",   # a triage measurement (865-G4's ancestor)
        "| Address | ★ / forks | `search/repositories` says | 🔴 Byte-read says | "
        "Verdict |",                             # field-vs-bytes refutation
        "| Address | `search/repositories` | Owner sweep | `raw.githubusercontent.com` | "
        "Verdict `2026-11-16` |",                # channel-by-channel grading
        "| Candidate | Stars | Why not shelved as build-safe |",
        "| Candidate | First-party metadata 2026-11-16 | Why it is not a row |",
        "| Candidate | HEAD `sha₁₂` measured `2026-11-16` | Why it is NOT a row |",
        "| Candidate | Repo | Grant | ★ | Why it is NOT on the shelf |",
        "| Row | Licence | ★ | Last push |",       # re-measure of rows already counted
        "| Row | Shelf claims | GitHub reports `2026-11-16` | Reading |",
        "| Row | Shelved as | Status 2026-11-16 |",
        "| Row | Was shelved as | Byte-read 2026-11-16 | Verdict |",
        # \U0001f7e2 p866 -- the NOT-BUILD-SAFE arm of the seven-column holdings shape. One row
        # (`nurkan1/anatria-3d`, BSL 1.1) sat in a table of that shape, and this shelf's
        # heading promises MIT / Apache-2.0 / BSD / ISC / 0BSD. Declaring the holdings
        # signature countable would have imported a row the heading's own predicate
        # excludes, so that table's first column header reads `Not build-safe` and lands
        # here instead. Visible on the page, absent from the total.
        "| Not build-safe | Repo | Licence, as measured | ★ / forks | Default ref · pushed | "
        "Region | What it actually does, and the posture |",
    ]),
    ("repos/foundations.md", [
        "| Repo | License | Stars | Notes |",
        "| Repo | License | Stars | What it is, and what it is not |",
        # 🟢 p853 declared this signature rather than adding a layer table silently,
        # which is the path p811's comment above prescribes.  It is the six-column
        # shape the agent shelf already uses (grant evidence, traction, resolved ref,
        # region, posture), carried onto the foundations shelf for the speech layer.
        "| Repo | Licence, as measured | \u2605 / forks | Default ref \u00b7 pushed | Region | "
        "Why it is a foundation and not a row on another shelf |",
        # 🟢 p858 declared this signature rather than adding a layer table silently --
        # the p811/p853 path.  It is the SAME six-column shape with one column renamed:
        # `Default ref \u00b7 pushed` becomes `Default ref \u00b7 HEAD commit`, because T197
        # measured GitHub's `pushed_at` as an ORGANISATION event (51 of 56 repositories at one
        # agency reporting one date, with commits up to 47 months older, on no branch).  The
        # column now carries `git log -1 --format=%cI` on the default ref, which the blobless
        # clone returns for free.  Both signatures are counted: the older rows are not
        # re-dated by this pass and must not be silently reinterpreted.
        "| Repo | Licence, as measured | \u2605 / forks | Default ref \u00b7 HEAD commit | Region | "
        "Why it is a foundation and not a row on another shelf |",
        # \U0001f7e2 p866 -- 865-G1's repair on this shelf. 22 rows in 8 tables carried a
        # foundation HOLDING under a header one or two words off a declared signature and
        # were counted nowhere. p865 recovered 7 of them by hand; these are the signatures
        # themselves, so the recovery stops being a per-pass manual act.
        "| Repo | License | Stars | Region | Description |",
        "| Repo | License | Stars | Region | Description | Why it is a foundation |",
        "| Repo | License | Stars | Why it is a foundation |",
        "| Repo | Licence (byte-read `2026-11-16`) | ★ | Pushed | Region | Why it is here |",
        "| Repo | Grant, byte-read `2026-11-16` | ★ / forks | Ref · pushed | Region | "
        "Why it is a foundation |",
        "| Repo | Licence, re-read `2026-11-16` | ★ / forks | Default ref · pushed | "
        "Why it is a FOUNDATION and not a platform |",
        "| Repo | Licence, byte-read `2026-11-16` | ★ / forks | Default ref · pushed | "
        "What it is |",
    ], [
        # \U0001f7e2 p866 -- declared NOT holdings on this shelf, each with its reason.
        "| Measure | Value |",                     # a scalar measurement, no address semantics
        "| Repo | Licence | Stars | Last push |",  # re-measure of rows already counted above
        # \U0001f7e2 p866 -- the licence byte-band MECHANISM table: one row per measured payload
        # offset with the diff that caused it. Its rows are payload measurements over
        # repositories shelved elsewhere (or deliberately not shelved at all), never
        # holdings. Declared because p866's own delta instrument caught it on first run.
        "| Bytes | Repo | `sha256₁₂` | Offset | \U0001f52c Cause, measured by diff |",
    ]),
    ("verticals/solutions.md", [
        # 🟢 p867 declared this signature rather than filing eight platform rows under a
        # header no declared signature matched -- the p811/p853/p858 path. It is the
        # Region-carrying shape the other two shelves already use, which this shelf needed
        # because `866-G2` is about placement and a platform row with no region column
        # cannot answer it.
        "| Platform | Repo | Licence, byte-read `2026-11-17` | \u2605 / forks | "
        "Default ref \u00b7 pushed | Region | Role in an engagement |",
        "| Platform | Repo | License | Stars | Notes |",
        "| Platform | Repo | Licence | Stars | What it is |",
        "| Platform | Repo | License | Stars | Why it is the right base for education admissions |",
        "| Platform | Repo | License | Stars | Where it is the incumbent | AI customization surface |",
        "| Platform | Repo | License (payload-verified) | Stars | What you actually get | What you do NOT get |",
        "| Platform | What institutions run it | Agent surface found this pass | License | Risk posture |",
        "| Platform | What institutions run it | Agent surface added this pass | License | Risk posture |",
        "| Platform | Operated by | Country | Agent surface found this pass | Licence | Stars |",
        "| Platform | Incumbent where | Open agent surface found | License | Stars |",
        "| Library | Repo | License | Stars | Use when |",
        # 🟢 p854: the licence-REFUTATION table -- a secondary source's licence claim set
        # against the bytes.  Not counted: it grades CLAIMS, and its rows are already
        # shelved (or refused) in the counted table beneath it.
        "| Platform | Repo | The source's claim | \U0001f52c **The bytes, `2026-11-16`** | Verdict |",
        # \U0001f7e2 p866 -- 865-G1's repair on this shelf: 41 rows in 12 tables are platform
        # or address HOLDINGS filed under a header that no declared signature matched.
        "| Address | Licence, byte-read `2026-11-17` | ★ / forks | Pushed | "
        "Role in an engagement |",
        "| Address | Licence, byte-read `2026-11-17` | ★ | Pushed | Role in an engagement |",
        "| Address | Licence | Pushed | Role in a PHP LMS engagement |",
        "| Platform | Repo | Licence | ★ | Region | Scale it is built for | "
        "Where the AI layer goes |",
        "| Platform | Repo | Licence | ★ | Region | Why it is a vertical starting point |",
        "| Platform / plugin | Repo | Grant, byte-read `2026-11-16` | ★ / forks | "
        "Ref · pushed | What it is, and the licence boundary it imposes |",
        "| Platform | What institutions run it | Agent surface | "
        "Licence, re-read `2026-11-16` | Posture |",
        "| Platform | What it is | Licence, byte-read `2026-11-16` | "
        "★ / forks · ref · pushed | Region & posture |",
        "| Repo | Licence | Stars | Status 2026-11-16 |",
    ], [
        # \U0001f7e2 p866 -- declared NOT holdings on this shelf: verdict and refusal tables.
        "| Address | ★ | Platform it is | Why it is not a row |",
        "| Platform | GitHub's licence field | \U0001f52c Byte-read verdict, `2026-11-16` | "
        "Verdict for a studio |",
        "| Platform | Grant (byte-read `2026-11-16`) | Verdict for a studio |",
        "| Platform | ★ | Grant | What that means for a studio |",
        "| Role in a migration | Artefact | Licence | Consequence for a studio |",
        "| System | Operator | Region | Access | Licence posture | Note |",
        "| | This shelf said | \U0001f7e2 GitHub reports `2026-11-16` |",
        # 🟢 p858: the NATIONAL PLATFORM tier.  Declared NOT-counted, deliberately and
        # for a structural reason rather than convenience: each row is a platform FAMILY whose
        # cell names three to five addresses (Opintopolku names five), so its rows are not
        # one-address holdings and summing them into a row count would double-count against
        # repos/foundations.md, where those same addresses are shelved individually.
        "| Platform | Operator \u00b7 country | \U0001f52c Licence, byte-read `2026-11-16` | "
        "Verdict for a studio |",
    ]),
]


def _tables(lines):
    """Yield (header_index, header_text, [body rows]) for every markdown table."""
    i = 0
    while i < len(lines) - 1:
        h = lines[i].strip()
        sep = lines[i + 1].strip()
        if h.startswith("|") and re.match(r"^\|[\s:|-]+\|$", sep) and "-" in sep:
            j = i + 2
            body = []
            while j < len(lines) and lines[j].strip().startswith("|"):
                body.append(lines[j])
                j += 1
            yield i, h, body
            i = j
        else:
            i += 1


for rel, signatures, excluded in SHELVES:

    path = os.path.join(root, rel)
    if not os.path.exists(path):
        print("%-22s ABSTAIN file absent." % rel)
        continue
    lines = open(path, encoding="utf-8").read().split("\n")

    sigset = set(signatures)
    rows, ragged, uncounted, matched = [], 0, [], 0
    for hi, header, body in _tables(lines):
        linked = [r for r in body if "github.com/" in r]
        if header in sigset:
            matched += 1
            ncol = len(header.strip().strip("|").split("|"))
            rows.extend(linked)
            ragged += sum(1 for r in linked
                          if len(r.strip().strip("|").split("|")) != ncol)
        elif linked and header not in set(excluded):
            uncounted.append((hi + 1, header, len(linked)))

    if matched == 0:
        print("%-22s RED  none of the %d declared column-header signatures was found; "
              "no table can be located." % (rel, len(signatures)))
        for sig in signatures:
            print("                       expected: %s" % sig)
        rc = 1
        continue

    if uncounted:
        print("%-22s RED  %d table(s) carry github.com rows but no declared signature; "
              "they are NOT counted." % (rel, len(uncounted)))
        for ln, header, n in uncounted:
            print("                       line %d (%d rows): %s" % (ln, n, header))
        rc = 1
    # p718: the count claim is NOT in the nearest preceding '## ' -- every shelf carries pass
    # narrative between its count heading and its table. It lives in the file's UNIQUE
    # canonical count heading, of the shape '## <name> -- N rows'. Graded as a SINGLETON
    # (`p699`'s rule): zero such headings or more than one is itself a RED, because both are
    # states in which a reader cannot tell which number is the shelf's.
    CLAIM = re.compile(r"^## .*?[\u2014-]\s*(\d[\d,]*)\s+rows\b")
    claims = [(j, m) for j, l in enumerate(lines)
              if l.startswith("## ") for m in [CLAIM.match(l)] if m]
    claimed = None
    if len(claims) == 1:
        claimed = int(claims[0][1].group(1).replace(",", ""))
    elif len(claims) == 0:
        print("  RED  no canonical count heading ('## <name> - N rows') in the file.")
        rc = 1
    else:
        print("  RED  %d canonical count headings; the shelf's figure is ambiguous: lines %s."
              % (len(claims), ", ".join(str(j + 1) for j, _ in claims)))
        rc = 1
    subj = []
    for r in rows:
        m = re.search(r"github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)", r)
        subj.append(m.group(1).lower().rstrip(".)") if m else None)
    nolink = sum(1 for s in subj if not s)
    seen, dupes = set(), 0
    for s in subj:
        if s and s in seen:
            dupes += 1
        elif s:
            seen.add(s)
    # 🟢 p813: on a file summed across LAYER tables, one repository legitimately appears in
    # two layers (frappe/education sits in the Frappe layer and in the ERP layer, and that
    # repetition is the point of the layering). So a repeat is a duplicate ROW, not a
    # duplicate SUBJECT, and the claim is graded against DISTINCT subjects. On a
    # single-table shelf a repeat is still a defect and still RED.
    multi = len(signatures) > 1
    distinct = len(seen)
    graded = distinct if multi else len(rows)
    print("%-22s shelf: tables=%d rows=%d distinct=%d graded=%d claimed=%s "
          "ragged=%d nolink=%d dupes=%d"
          % (rel, matched, len(rows), distinct, graded, claimed, ragged, nolink, dupes))
    if claimed is None:
        print("  AMBER no 'N rows' claim in the heading above the table; nothing to compare.")
    elif claimed != graded:
        print("  RED  heading claims %d, the file holds %d." % (claimed, graded))
        rc = 1
    else:
        print("  GREEN heading agrees with its page.")
    if ragged:
        print("  RED  %d row(s) disagree with their header's column count (the p674 L55 class)." % ragged)
        rc = 1
    if nolink:
        print("  RED  %d row(s) carry no repository link." % nolink)
        rc = 1
    if dupes and multi:
        print("  INFO %d repository/ies appear in more than one layer table; counted once."
              % dupes)
    elif dupes:
        print("  RED  %d duplicate subject(s)." % dupes)
        rc = 1

sys.exit(rc)
