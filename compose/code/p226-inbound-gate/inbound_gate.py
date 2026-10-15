"""ACTION SH (p226) - move the refuted-claims gate from OUTBOUND prose to INBOUND search results.

ACTION SA (p223/p224) built a (subject, refuted-claim, correction) table and ran it over this
KB's own published prose. It reported 0 ASSERTED / 5 ATTRIBUTED at p224 and p225 - which can be
read as "solved". p225 showed it is not: both refuted claims came back INBOUND, through the
mandated regional query itself, carried by sources never cited here.

This instrument runs the SAME table, the SAME regexes, one step earlier in the pipeline:
against a pass's raw search results, BEFORE anything is written to a shelf.

A row FIRES when, within one record:
    subject_pattern matches AND refuted_pattern matches AND exempt_pattern does NOT match.
The conjunction matters: subject_pattern alone is far too broad (every AI Act paragraph
mentions "high-risk"), and refuted_pattern alone would fire on unrelated August-2026 prose.

Stdlib only. No requests. The text is text the pass already has.
"""

import csv
import re
import sys


def load_table(tsv_path):
    """Read sa-refuted-claims.tsv into compiled rows. Comment lines (#) are skipped."""
    rows = []
    with open(tsv_path, encoding="utf-8") as fh:
        lines = [ln for ln in fh if not ln.startswith("#")]
    for rec in csv.DictReader(lines, delimiter="\t"):
        if not rec.get("subject_pattern") or not rec.get("refuted_pattern"):
            continue
        rows.append(
            {
                "subject": rec["subject"],
                "subject_re": re.compile(rec["subject_pattern"]),
                "refuted_re": re.compile(rec["refuted_pattern"]),
                "exempt_re": re.compile(rec["exempt_pattern"]) if rec.get("exempt_pattern") else None,
                "correction": rec.get("correction", ""),
                "refuted_by": rec.get("refuted_by", ""),
            }
        )
    return rows


def split_records(text):
    """Split a raw-results file into (query, lineno, line) records.

    A record is ONE LINE. Line is the right unit here: a search-result summary puts one claim
    per line, and a whole-block unit would let a subject in paragraph 1 pair with an unrelated
    date in paragraph 9 - the exact ENTITY-grep -> AXIS-claim inference ACTION QY tracks.
    """
    query = "(none)"
    out = []
    for i, line in enumerate(text.splitlines(), start=1):
        if line.startswith("=====QUERY:"):
            query = line.split(":", 1)[1].strip()
            continue
        if line.strip():
            out.append((query, i, line))
    return out


def scan(records, rows):
    """Return (hits, near_misses).

    A NEAR MISS is subject_pattern matching with refuted_pattern NOT matching, on a record that
    nonetheless carries the refuted claim's date token. It is reported separately because a gate
    that only reports its own firings cannot tell a clean pass from a blind spot.
    """
    hits, near = [], []
    date_token = re.compile(r"(?i)(august|agosto)\s*2026")
    for query, lineno, line in records:
        for row in rows:
            if not row["subject_re"].search(line):
                continue
            if row["refuted_re"].search(line):
                if row["exempt_re"] and row["exempt_re"].search(line):
                    continue
                hits.append((query, lineno, row["subject"], line.strip(), row["correction"]))
            elif date_token.search(line) and "ai act" in row["subject"].lower():
                near.append((query, lineno, row["subject"], line.strip()))
    return hits, near


def main():
    table, raw = sys.argv[1], sys.argv[2]
    rows = load_table(table)
    records = split_records(open(raw, encoding="utf-8").read())
    hits, near = scan(records, rows)
    print(f"table rows      : {len(rows)}")
    print(f"inbound records : {len(records)}")
    print(f"INBOUND HITS    : {len(hits)}")
    for q, ln, subj, line, corr in hits:
        print(f"  HIT  [{q}] l.{ln}\n       subject   : {subj}\n       matched   : {line[:220]}\n       correction: {corr}")
    print(f"NEAR MISSES     : {len(near)}")
    for q, ln, subj, line in near:
        print(f"  NEAR [{q}] l.{ln}\n       subject   : {subj}\n       text      : {line[:220]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
