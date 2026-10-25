#!/usr/bin/env python3
"""Extract (slug, grant-present) from this base's accumulated evidence corpus.

`Gap 444-A` asks whether "the institution publishes and does not licence" holds outside
Brazil.  p444 measured it on FIVE rows.  Every address this base has ever verified
first-hand is already on disk under `evidence/`, so the census costs no network.

The schemas are heterogeneous (61 `verified-repos.*.tsv` alone carry 20+ header forms, and
the wider corpus is wilder), so this extractor does NOT trust column names.  Per row it:

  1. finds the slug by PATTERN (`owner/repo`), not by position;
  2. decides grant presence by looking for a recognised licence FAMILY token anywhere in
     the row, against the absence markers this base actually emits;
  3. refuses to guess: a row with neither signal is EXCLUDED and counted as excluded.

Dedupe: one verdict per slug, from the HIGHEST pass number that measured it, because a
later pass's first-hand read supersedes an earlier one (that is why `p442` repaired cells).
"""
import os, re, sys, csv, glob, collections

EV = os.path.join(os.path.dirname(__file__), "..", "..", "..", "evidence")

SLUG_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*/[A-Za-z0-9][A-Za-z0-9._-]*$")

# Families this base's own classifier (`lib/license_family.sh`) emits, plus the SPDX ids
# the older TSVs wrote by hand.  Word-bounded so `MIT` does not match `TRANSMITTER`.
FAMILY_RE = re.compile(
    r"(?<![A-Za-z0-9])("
    r"MIT|Apache-?2(\.0)?|BSD(-[23](-Clause)?)?|"
    r"A?GPL-?[23](\.0)?|LGPL-?[23](\.0)?|MPL-?2(\.0)?|EUPL-?1(\.2)?|"
    r"CC-?BY(-SA|-NC|-ND)*(-4\.0)?|CC0|ISC|Unlicense|Zlib|EPL-?[12]|ODbL|OFL"
    r")(?![A-Za-z0-9])", re.I)

# The exact verdicts this base emits for an absence, from `probe_payload.sh` and the
# hand-written TSVs.  An absence is a FINDING here, not a missing value.
ABSENT_RE = re.compile(
    r"(NO-PAYLOAD|NO-GRANT-PATH|ABSENCE-ENUMERATED|DECLARED-NOT-GRANTED|"
    r"DANGLING-README-LINK|NO[ -]GRANT|NONE|UNLICEN[CS]ED|NO LICEN[CS]E)", re.I)

# A row we must not score either way.
UNRESOLVED_RE = re.compile(r"(UNRESOLVED|UNCLASSIFIED|UNKNOWN|404|GONE|MOVED)", re.I)

PASS_RE = re.compile(r"p(?:ass)?[-.]?(\d+)", re.I)


def pass_number(path):
    m = PASS_RE.findall(os.path.basename(path))
    return max((int(x) for x in m), default=0)


LICENCE_ID_RE = re.compile(r"^(" + FAMILY_RE.pattern.split("(?<![A-Za-z0-9])(")[1].rsplit(")(?![A-Za-z0-9])", 1)[0] + r")$", re.I)


def is_junk(slug):
    """A licence identifier, a bare version or a numeric owner is not an address.

    Measured need: the corpus carries rows like `0/agpl-3.0` from the grammar censuses,
    which are LICENCE IDS written in a slug-shaped cell.  Scoring them would count the
    classifier's own vocabulary as repositories.
    """
    owner, _, repo = slug.partition("/")
    if owner.isdigit() or len(owner) < 2:
        return True
    if LICENCE_ID_RE.match(repo) or LICENCE_ID_RE.match(owner):
        return True
    return False


def row_slugs(cells):
    out = []
    for c in cells:
        c = c.strip()
        if SLUG_RE.match(c) and not is_junk(c):
            out.append(c)
    return out


def classify_row(cells):
    """-> 'GRANT' | 'ABSENT' | None (unscoreable)."""
    joined = "\t".join(cells)
    if FAMILY_RE.search(joined):
        return "GRANT"
    if ABSENT_RE.search(joined):
        return "ABSENT"
    if UNRESOLVED_RE.search(joined):
        return None
    return None


def main():
    best = {}          # slug -> (pass_no, verdict, source)
    stats = collections.Counter()
    files = sorted(glob.glob(os.path.join(EV, "*.tsv")))
    for path in files:
        pno = pass_number(path)
        try:
            with open(path, newline="", encoding="utf-8", errors="replace") as fh:
                for cells in csv.reader(fh, delimiter="\t"):
                    if not cells or cells[0].lstrip().startswith("#"):
                        continue
                    slugs = row_slugs(cells)
                    if len(slugs) != 1:
                        stats["row_no_single_slug"] += 1
                        continue
                    slug = slugs[0]
                    key = slug.lower()
                    verdict = classify_row(cells)
                    if verdict is None:
                        stats["row_unscoreable"] += 1
                        continue
                    stats["row_scored"] += 1
                    prev = best.get(key)
                    if prev is None or pno >= prev[0]:
                        best[key] = (pno, verdict, os.path.basename(path), slug)
        except Exception as e:                      # a corrupt evidence file is a finding
            stats["file_error"] += 1
            print(f"# ERROR {path}: {e}", file=sys.stderr)
    print("slug\tverdict\tfrom_pass\tsource")
    for key in sorted(best):
        pno, verdict, src, slug = best[key]
        print(f"{slug}\t{verdict}\t{pno}\t{src}")
    for k, v in sorted(stats.items()):
        print(f"# {k}\t{v}", file=sys.stderr)
    print(f"# files_read\t{len(files)}", file=sys.stderr)
    print(f"# distinct_slugs\t{len(best)}", file=sys.stderr)


if __name__ == "__main__":
    main()
