#!/usr/bin/env python3
"""p227 ACTION SO / ACTION SH instrument: the refuted-claims gate, made BIDIRECTIONAL.

Two jobs, deliberately kept separate because they fail differently:

1. inbound_gate()  - p226's gate, unchanged in behaviour, now reading a table that also
                     carries RESTRICTIVE-direction rows. A claim is flagged when the
                     subject_pattern matches AND the refuted_pattern matches AND the
                     exempt_pattern does NOT. The exempt column is what keeps a source
                     that FLAGS the error from being counted as circulating it.

2. family_of()     - the GPL-3.0 vs AGPL-3.0 discriminator. This exists because the
                     canonical bodies are 15 BYTES apart (35 121 vs 35 136) and because
                     GPL-3.0's section 13 is titled "Use with the GNU Affero General
                     Public License" - so a bare grep for "affero" returns 3 hits on a
                     GPL-3.0 body. Byte size and token presence are both unsafe. The
                     TITLE LINE is the channel.

Stdlib only, by design: ACTION QO wants this wired into `make hooks`.
"""
import re
import sys

TABLE_COLS = ("subject", "subject_pattern", "refuted_pattern",
              "correction", "refuted_by", "exempt_pattern", "direction")


def load_table(path):
    """Columns 1-6 are p226-compatible. Column 7 (direction) is optional, so a p226-era
    table loads here and defaults to PERMISSIVE - the only direction it could express."""
    rows = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if parts[0] == "subject":          # header
                continue
            if len(parts) < 6:
                raise ValueError(f"table row has {len(parts)} columns, need >= 6: {parts[0]!r}")
            row = dict(zip(TABLE_COLS, parts[:6]))
            row["direction"] = parts[6] if len(parts) > 6 and parts[6] else "PERMISSIVE"
            rows.append(row)
    return rows


def load_records(path):
    """QUERY<TAB>TEXT, one inbound record per line."""
    out = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            query, _, text = line.rstrip("\n").partition("\t")
            if text:
                out.append((query, text))
    return out


def inbound_gate(table, records):
    """Returns (hits, near_misses). A near miss matched the subject but not the refuted
    pattern - reported, never silently dropped, because p226's T226-1 showed a near miss
    can be a TRUE statement that a widened pattern would wrongly flag."""
    hits, near = [], []
    for query, text in records:
        for row in table:
            if not re.search(row["subject_pattern"], text):
                continue
            if re.search(row["refuted_pattern"], text):
                if row["exempt_pattern"] and re.search(row["exempt_pattern"], text):
                    continue                      # the source is reporting the error, not circulating it
                hits.append({"query": query, "text": text, "subject": row["subject"],
                             "direction": row["direction"], "correction": row["correction"]})
            else:
                near.append({"query": query, "text": text, "subject": row["subject"],
                             "direction": row["direction"]})
    return hits, near


# --- the GPL-3.0 / AGPL-3.0 family discriminator -----------------------------------------
# Section 13 is the mechanism. In GPL-3.0 it is a COMPATIBILITY clause naming Affero;
# in AGPL-3.0 it is the network-use clause. So the heading alone also separates them.
TITLE_AGPL = re.compile(r"GNU AFFERO GENERAL PUBLIC LICENSE", re.I)
TITLE_GPL = re.compile(r"GNU (?!AFFERO)GENERAL PUBLIC LICENSE", re.I)
S13_GPL = re.compile(r"13\.\s*Use with the GNU Affero General Public License", re.I)
S13_AGPL = re.compile(r"13\.\s*Remote Network Interaction", re.I)


def family_of(body):
    """Decide GPL-3.0 vs AGPL-3.0 from a licence body. Returns (family, channel, note).

    Three channels were tried on these shelves and only the third survives, because
    GPL-3.0's section 13 is a COMPATIBILITY clause that names the Affero licence in full:

      1. byte size            - UNSAFE: the canonical bodies are 15 B apart (35 121 / 35 136).
      2. a bare 'affero' grep - UNSAFE: a GPL-3.0 body carries 3 such tokens (naive_affero_grep).
      3. a whole-body search for the AGPL title - ALSO UNSAFE, and this one defeated p227's
         own first draft: the string "GNU Affero General Public License" appears INSIDE a
         GPL-3.0 body, in section 13. Searching the whole body finds it and inverts the answer.

    So the title must be read POSITIONALLY - the first licence title in document order - and
    the AGPL title must be excluded from the GPL pattern so the two cannot both match at 0.
    """
    m_agpl = TITLE_AGPL.search(body)
    m_gpl = TITLE_GPL.search(body)
    if not m_agpl and not m_gpl:
        return (None, None, "no GNU title line - not a GPL-family body")
    if m_agpl and (not m_gpl or m_agpl.start() < m_gpl.start()):
        fam, chan = "AGPL-3.0", "title line"
    else:
        fam, chan = "GPL-3.0", "title line"

    # Corroborate on section 13, and report rather than silently prefer one channel.
    if fam == "GPL-3.0" and S13_AGPL.search(body):
        return (None, "conflict", "title says GPL-3.0 but section 13 is the AGPL network clause")
    if fam == "AGPL-3.0" and S13_GPL.search(body) and not S13_AGPL.search(body):
        return (None, "conflict", "title says AGPL-3.0 but section 13 is the GPL compatibility clause")
    s13 = "section 13 agrees" if (S13_GPL.search(body) or S13_AGPL.search(body)) else "section 13 absent"
    return (fam, chan, s13)


def naive_affero_grep(body):
    """The WRONG method, kept as a control so the defect stays demonstrable."""
    return "AGPL-3.0" if re.search(r"affero", body, re.I) else "GPL-3.0"


def main(argv):
    if len(argv) < 3:
        print("usage: direction_gate.py <table.tsv> <records.txt>", file=sys.stderr)
        return 2
    table = load_table(argv[1])
    records = load_records(argv[2])
    hits, near = inbound_gate(table, records)

    perm = sum(1 for r in table if r["direction"] == "PERMISSIVE")
    rest = sum(1 for r in table if r["direction"] == "RESTRICTIVE")
    print(f"table: {len(table)} subjects ({perm} PERMISSIVE, {rest} RESTRICTIVE)")
    print(f"records: {len(records)}")
    print(f"HITS: {len(hits)}   near misses: {len(near)}")
    for h in hits:
        print(f"\n  [HIT/{h['direction']}] {h['subject']}")
        print(f"    query : {h['query']}")
        print(f"    text  : {h['text'][:200]}")
        print(f"    truth : {h['correction'][:200]}")
    for n in near:
        print(f"\n  [near/{n['direction']}] {n['subject']}")
        print(f"    query : {n['query']}")
        print(f"    text  : {n['text'][:200]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
