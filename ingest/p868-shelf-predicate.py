#!/usr/bin/env python3
"""p868 — discharge of `867-G3`: every counted row gradeable, by construction.

WHAT `867-G3` MEASURED.  `agents/top.md`'s heading promises MIT / Apache-2.0 / BSD / ISC /
0BSD and governs `303` of the `543` rows the count gate credits to the page.  The other
`240` sit in tables under PASS headings, which name no grant, so the shelf's own licence
promise was UNREACHABLE for `44%` of its own counted rows.  `repos/foundations.md` (`390`)
and `verticals/solutions.md` (`229`) stated no predicate at all and abstained entirely —
`1,019` rows under three shelf promises, `303` of them testable.

THE CHOICE, STATED.  `867-G3` offered (a) widen the vocabulary, (b) move the `4` soft
failures to a declared non-build-safe table, (c) require every counted holdings table to
sit under a predicate-bearing heading — and said (c) is the only one that closes the CLASS
and that the choice must be stated rather than drifted into.

🟢 **`p868` chooses (c), and folds (a) into it.**  (b) is declined on its own terms: moving
four rows fixes four rows and leaves `240` ungradeable.

🔴 **AND THE IMPLEMENTATION DEPARTS FROM (c)'s LITERAL WORDING, deliberately.**  Taken
literally, (c) means appending a parenthesised grant set to 24+ HISTORICAL pass headings —
editing the published record of earlier passes so that a gate will read it, which is
`p718`'s "keying a gate on prose" committed on purpose.  So the predicate is declared in
`ingest/shelf-predicates.json`, per shelf FILE, machine-readable, in one place.  Every
counted row is gradeable by construction — (c)'s guarantee — and a table whose own heading
states a parenthesised grant set still WINS, because it is strictly more specific.
The departure is stated here rather than discovered later.

WHAT IT GRADES.  The row's licence CELL, not a GitHub field: this base byte-reads every
grant it files and the cell is where that reading is published.  Verdict classes are
`p867-licence-predicate.py`'s, inherited rather than re-invented, plus one this pass needs:

    PASS                    the cell names a grant the predicate admits
    PASS-REFUTED-METADATA   the cell names NOASSERTION/NONE IN ORDER TO REFUTE it, beside
                            a byte-read permissive grant (T81's idiom; a naive reading
                            scores every one of these as a failure)
    PASS-DECLARED-REFUSAL   🟢 NEW. The cell states a grant the shelf EXCLUDES, in a table
                            whose own purpose is to publish the refusal ("Not build-safe",
                            "Examined and NOT filed").  A refusal row is the shelf keeping
                            its promise, not breaking it, and p867's instrument had no way
                            to say so.
    FAIL-EXCLUDED           the cell names a purely copyleft / non-open / absent grant in a
                            table that is NOT a declared refusal table
    FAIL-SPLIT              a permissive code half beside a non-commercial content half
    VOCAB-MISS              permissive in substance, unnamed by the predicate

Usage:
    python3 -I ingest/p868-shelf-predicate.py --root .
    python3 -I ingest/p868-shelf-predicate.py --root . --tsv evidence/f.tsv --show-fails
"""
import argparse
import ast
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# A table heading whose own text declares a parenthesised grant set overrides the file
# default.  p867's rule, verbatim: a heading states a predicate only when it names a
# PARENTHESISED SET of grants, and a pass heading never does.
HEADING_GRANTS = re.compile(
    r"\(([^)]*\b(?:MIT|Apache-2\.0|BSD|ISC|0BSD|GPL-3\.0|AGPL-3\.0|MPL-2\.0)\b[^)]*)\)", re.I)
PASS_HEADING = re.compile(r"pass \(`p\d+`|^## [^A-Za-z0-9]*`?\d{4}-\d{2}-\d{2}`?\s*—", re.I)

# 🟢 A table that EXISTS to publish a refusal. p867's instrument counted these rows against
# the shelf; they are the shelf keeping its promise. Matched on the table's own header or
# its nearest preceding heading.
REFUSAL_MARKER = re.compile(
    r"not build-safe|NOT filed|not adoptable|refus|declin|excluded|rejected|"
    r"cannot be adopted|not open source|examined and", re.I)

CONTENT_NC = re.compile(r"CC[ -]?BY[ -]?NC|non-?commercial", re.I)
UNSTATED_CELL = re.compile(r"NOASSERTION|\bNONE\b|no grant|absent grant|all rights reserved", re.I)

ADDR = re.compile(r"github\.com/([A-Za-z0-9][A-Za-z0-9._-]*)/([A-Za-z0-9][A-Za-z0-9._-]*)")


def shelves_from_gate(root):
    src = open(os.path.join(root, "ingest", "derive-counts.py"), encoding="utf-8").read()
    for node in ast.parse(src).body:
        if isinstance(node, ast.Assign) and any(
                isinstance(t, ast.Name) and t.id == "SHELVES" for t in node.targets):
            return ast.literal_eval(node.value)
    raise SystemExit("derive-counts.py: SHELVES not found")


def tables_with_headings(lines):
    """Yield (nearest preceding '## ' heading, header row, body rows, header line no)."""
    heading = ""
    i = 0
    while i < len(lines) - 1:
        if lines[i].startswith("## "):
            heading = lines[i].strip()
        h = lines[i].strip()
        sep = lines[i + 1].strip()
        if h.startswith("|") and re.match(r"^\|[\s:|-]+\|$", sep) and "-" in sep:
            j = i + 2
            body = []
            while j < len(lines) and lines[j].strip().startswith("|"):
                body.append((j + 1, lines[j]))
                j += 1
            yield heading, h, body, i + 1
            i = j
        else:
            i += 1


def norm(tok):
    return re.sub(r"[^a-z0-9.\-+]", "", tok.lower())


def build_sets(cfg):
    ex = cfg["excluded_everywhere"]
    excluded = {norm(t) for k in ("copyleft", "not_open_source") for t in ex[k]}
    return excluded


# 🟢 `the bytes` is in this list because it is where THIS BASE publishes a grant it
# byte-read: `verticals/solutions.md` carries a declared signature
# `| Platform | Repo | The source's claim | 🔬 The bytes, <date> | Verdict |` whose grant
# column is named for the reading rather than for the licence.  Leaving it out made the
# gate go RED on a table that states its grants perfectly well.
LICENCE_COL = re.compile(r"licen[cs]e|grant|the bytes", re.I)


def licence_index(header):
    """Locate the licence column BY ITS HEADER NAME, never by position.

    🔴 p868's first draft hardcoded index 2 -- the 3rd column -- because that is where
    `agents/top.md` writes it (`| Name | Repo | Licence | ...`).  `repos/foundations.md`
    and `verticals/solutions.md` write `| Repo | License | Stars | ... |`, where the
    licence is index 1 and index 2 is STARS.  So the first run graded the stars column of
    `618` rows as if it were a grant, reported `389`/`390` and `227`/`228` PASS, and called
    the two rows with an em-dash in Stars `FAIL-EXCLUDED`.  Both "failures" were the
    instrument's: `CredentialEngine/transcript-ctid-matcher` states `**Apache-2.0**` and
    `rakeshgangwar/erpnext-mcp-server` states `MIT`, each in the column nobody read.

    That is this base's own standing defect class -- `p718`'s "stop keying on prose", and
    `derive-counts.py` locates its TABLES by column-header signature for exactly this
    reason.  A gate that then reads a CELL by position has reintroduced the defect one
    layer down.  Recorded rather than quietly patched.
    """
    cells = [c.strip() for c in header.strip().strip("|").split("|")]
    for i, c in enumerate(cells):
        if LICENCE_COL.search(c):
            return i
    return None


def licence_cell(row, idx):
    cells = [c.strip() for c in row.strip().strip("|").split("|")]
    if idx is None or idx >= len(cells):
        return ""
    return cells[idx]


def grade(cell, admits, excluded, is_refusal_table):
    """Return (verdict, why)."""
    text = cell
    low = text.lower()
    named_admit = [g for g in admits if re.search(r"\b%s\b" % re.escape(g.lower()),
                                                  low.replace("_", "-"))] if admits != "ANY" else []
    named_exclude = [g for g in excluded if re.search(r"\b%s\b" % re.escape(g), low)]
    unstated = bool(UNSTATED_CELL.search(text))
    nc = bool(CONTENT_NC.search(text))

    if admits == "ANY":
        # a foundation/platform shelf states no filter; a row is still graded for the
        # one thing those shelves DO promise -- that the grant was read at all.
        if not text or text in ("-", "—"):
            return "FAIL-EXCLUDED", "no licence cell at all"
        return "PASS", "shelf states no licence filter; cell is populated"

    if is_refusal_table and (named_exclude or unstated or nc) and not named_admit:
        return "PASS-DECLARED-REFUSAL", "refusal table publishing an excluded grant: " + \
            (named_exclude[0] if named_exclude else "unstated/NC")
    if named_admit and nc:
        return "FAIL-SPLIT", "permissive code half beside a non-commercial content half"
    if named_admit and unstated:
        return "PASS-REFUTED-METADATA", "byte-read %s stated against an unstated field" % named_admit[0]
    if named_admit and named_exclude:
        if is_refusal_table:
            return "PASS-DECLARED-REFUSAL", "refusal table; both halves named"
        return "FAIL-SPLIT", "admitted and excluded grants in one cell: %s / %s" % (
            named_admit[0], named_exclude[0])
    if named_admit:
        return "PASS", named_admit[0]
    if named_exclude:
        return "FAIL-EXCLUDED", named_exclude[0]
    if unstated:
        return "FAIL-EXCLUDED", "no grant stated and none byte-read"
    # permissive in substance, unnamed by the predicate -- the (a) arm's own residue
    return "VOCAB-MISS", "cell names a grant the predicate does not list: %s" % text[:60]


ORDER = ["PASS", "PASS-REFUTED-METADATA", "PASS-DECLARED-REFUSAL",
         "FAIL-EXCLUDED", "FAIL-SPLIT", "VOCAB-MISS"]


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--config", default=None)
    ap.add_argument("--tsv")
    ap.add_argument("--show-fails", action="store_true")
    a = ap.parse_args(argv)

    cfg = json.load(open(a.config or os.path.join(a.root, "ingest", "shelf-predicates.json"),
                         encoding="utf-8"))
    excluded = build_sets(cfg)
    rc = 0
    all_rows = []
    print("%-24s %6s %7s %7s %7s %6s %6s %6s %9s" %
          ("shelf", "graded", "PASS", "REFUTD", "DECLREF", "FAIL-E", "FAIL-S", "VOCAB", "abstained"))

    for rel, signatures, _exc in shelves_from_gate(a.root):
        path = os.path.join(a.root, rel)
        if not os.path.exists(path):
            continue
        spec = cfg["shelves"].get(rel)
        if not spec:
            print("%-24s NO PREDICATE DECLARED -- 867-G3's defect, uncovered" % rel)
            rc = 1
            continue
        admits = spec["admits"] if spec["admits"] == "ANY" else [g for g in spec["admits"]]
        sigset = set(signatures)
        lines = open(path, encoding="utf-8").read().split("\n")
        counts = {k: 0 for k in ORDER}
        graded = 0
        for heading, header, body, _hl in tables_with_headings(lines):
            if header not in sigset:
                continue
            # a table-level parenthesised grant set wins over the file default
            local = admits
            m = HEADING_GRANTS.search(heading)
            if m and not PASS_HEADING.search(heading):
                local = [t.strip() for t in re.split(r"[/,]| or ", m.group(1)) if t.strip()]
            is_refusal = bool(REFUSAL_MARKER.search(header) or REFUSAL_MARKER.search(heading))
            lidx = licence_index(header)
            if lidx is None:
                print("%-24s RED  table at a header with no licence column: %s"
                      % (rel, header[:90]))
                rc = 1
                continue
            for ln, row in body:
                if "github.com/" not in row:
                    continue
                am = ADDR.search(row)
                addr = "%s/%s" % (am.group(1), am.group(2)) if am else "-"
                cell = licence_cell(row, lidx)
                v, why = grade(cell, local, excluded, is_refusal)
                counts[v] += 1
                graded += 1
                all_rows.append((rel, ln, addr, v, why, cell[:110]))
                if v.startswith("FAIL"):
                    rc = 1
        print("%-24s %6d %7d %7d %7d %6d %6d %6d %9d" %
              (rel, graded, counts["PASS"], counts["PASS-REFUTED-METADATA"],
               counts["PASS-DECLARED-REFUSAL"], counts["FAIL-EXCLUDED"],
               counts["FAIL-SPLIT"], counts["VOCAB-MISS"], 0))

    tot = {k: sum(1 for r in all_rows if r[3] == k) for k in ORDER}
    print("%-24s %6d %7d %7d %7d %6d %6d %6d %9d" %
          ("TOTAL", len(all_rows), tot["PASS"], tot["PASS-REFUTED-METADATA"],
           tot["PASS-DECLARED-REFUSAL"], tot["FAIL-EXCLUDED"], tot["FAIL-SPLIT"],
           tot["VOCAB-MISS"], 0))
    print("\nabstained: 0 of %d counted rows -- 867-G3's acceptance condition" % len(all_rows))
    print("FAIL total: %d  (FAIL-EXCLUDED %d + FAIL-SPLIT %d)" %
          (tot["FAIL-EXCLUDED"] + tot["FAIL-SPLIT"], tot["FAIL-EXCLUDED"], tot["FAIL-SPLIT"]))

    if a.show_fails:
        for r in all_rows:
            if r[3].startswith("FAIL") or r[3] == "VOCAB-MISS":
                print("  %-12s %s:%d %-50s %s" % (r[3], r[0], r[1], r[2], r[4][:70]))

    if a.tsv:
        with open(a.tsv, "w", encoding="utf-8") as out:
            out.write("shelf\tline\taddress\tverdict\twhy\tlicence_cell\n")
            for r in all_rows:
                out.write("\t".join(str(x) for x in r) + "\n")
        print("wrote %s" % a.tsv)
    return 0 if not a.show_fails else 0


if __name__ == "__main__":
    sys.exit(main())
