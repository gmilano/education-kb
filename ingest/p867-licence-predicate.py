#!/usr/bin/env python3
"""p867 -- discharge of `866-G4`: run each shelf heading's OWN licence predicate over
every row the count gate credits to that shelf.

WHY THIS EXISTS.  `p866` raised three shelves by `97` rows without adding a row, by
sorting `54` undeclared table headers into HOLDINGS and MEASUREMENT.  That sort was one
pass reading one header line at a time, and exactly one error of the dangerous kind was
caught in the act: the seven-column holdings signature would have imported
`nurkan1/anatria-3d` (`BSL 1.1`) into a shelf whose heading promises MIT / Apache-2.0 /
BSD / ISC / 0BSD.  One caught error in a 54-way manual sort is not evidence it was the
only one, and `866-G4` asked for the cheap check nobody had run.

WHAT IT DOES NOT DO.  It does not re-read licence payloads and it does not re-declare
signatures.  The signatures are read OUT OF `ingest/derive-counts.py` with `ast`, never
re-typed and never executed -- `ingest/p587-crosspage-naive.py` is this base's standing
warning about writing the fourth copy of an instrument it already owns, and a second
hand-maintained signature list is exactly that defect.  The licence VERDICT here is the
shelf's own cell, graded against the shelf's own heading: this instrument asks whether
the page contradicts itself, which needs no network at all.

WHAT A PREDICATE IS.  A shelf heading that NAMES grants ("Build-safe agents (MIT /
Apache-2.0 / BSD / ISC / 0BSD)") states a predicate its rows must satisfy.  A heading
that names none ("Foundational repos", "Education vertical platforms") states no
predicate, and this instrument ABSTAINS on it rather than inventing one -- those two
shelves carry GPL/AGPL/LGPL rows deliberately (Moodle, BigBlueButton, Open edX), so a
borrowed permissive predicate would manufacture ~200 false failures and teach the next
pass to ignore the gate.

Usage:
    python3 -I ingest/p867-licence-predicate.py [--root .] [--tsv out.tsv]
Exit: 0 no counted row contradicts its heading / 1 at least one does / 2 unparseable.
"""
import argparse
import ast
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# Grants the heading's own words admit, and grants that contradict them.  Order matters:
# a cell is FAIL if it names any excluder, even when it also names a permissive token
# (dual-licensed and "MIT code, GPL data" cells must not pass silently).
PERMISSIVE = [
    r"\bmit\b", r"\bapache[-\s]?2(?:\.0)?\b", r"\bbsd[-\s]?[23](?:[-\s]clause)?\b",
    r"\bbsd\b", r"\bisc\b", r"\b0bsd\b", r"\becl[-\s]?2(?:\.0)?\b", r"\bunlicense\b",
]
EXCLUDERS = [
    (r"\bagpl", "AGPL"), (r"\blgpl", "LGPL"), (r"\bgpl", "GPL"), (r"\bmpl", "MPL"),
    (r"\bepl", "EPL"), (r"\bcddl", "CDDL"), (r"\bosl", "OSL"),
    (r"\bbusl|\bbsl[-\s]?1", "BUSL/BSL"), (r"\bsspl", "SSPL"), (r"\belastic licen", "Elastic"),
    (r"\bcc[-\s]?by[-\s]?nc|\bnoncommercial|\bnon[-\s]commercial", "CC-BY-NC"),
    (r"\bproprietar", "proprietary"), (r"\bsustainable use", "Sustainable-Use"),
    (r"no licen|without a licen|\bnone\b|\bnoassertion\b|all rights reserved", "no grant"),
]
# Heading -> predicate.  A heading is matched by the grants it NAMES, not by its wording,
# so a reworded heading that still names the same grants keeps the same predicate (which
# is p718's lesson: never key a gate on prose).
# 🟢 A heading states a PREDICATE when it names a SET of grants as a qualifier -- parenthesised
# and separated, as in "Build-safe agents (MIT / Apache-2.0 / BSD / ISC / 0BSD) — 535 rows".
# 🔴 p867's SECOND draft keyed on "two grant tokens anywhere in the heading line", and its own
# pass headings -- which narrate licences in prose ("`6` foundation rows … `21` Apache-2.0 against
# `71` AGPL-3.0", "`5` copyleft-by-platform") -- then became predicates for the tables beneath
# them.  The foundations shelf scored a FAIL-SPLIT on `mitodl/open-edx-plugins`, whose cell
# EXPLAINS that the BSD-3 form opens "All rights reserved", and the platform shelf was about to
# fail its copyleft incumbents against a predicate no shelf heading states.  Same defect class as
# the first draft, one level down: a gate must not key on prose (p718's standing lesson).
GRANT_TOKEN = r"(?:MIT|Apache[-\s]?2(?:\.0)?|BSD(?:[-\s]?[0234](?:[-\s]clause)?)?|ISC|0BSD|ECL[-\s]?2\.0)"
HEADING_GRANTS = re.compile(
    r"\(\s*%s(?:\s*[/,]\s*%s)+\s*\)" % (GRANT_TOKEN, GRANT_TOKEN), re.I)
# 🔴 And a PASS heading is never a predicate, however it is worded.
PASS_HEADING = re.compile(r"pass \(`p\d+`|^## [^A-Za-z0-9]*`?\d{4}-\d{2}-\d{2}`?\s*—", re.I)
REFUTATION = re.compile(
    r"against (?:github|the field|metadata)|github (?:\w+ ){0,2}(?:says|reports|claims)|"
    r"refut|while github|despite github|field says", re.I)


def signatures(path):
    """Read SHELVES out of derive-counts.py without executing it."""
    tree = ast.parse(open(path, encoding="utf-8").read())
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
                getattr(t, "id", "") == "SHELVES" for t in node.targets):
            return ast.literal_eval(node.value)
    raise SystemExit("🔴 SHELVES not found in derive-counts.py — has it been renamed?")


def norm(line):
    return re.sub(r"\s+", " ", line.strip())


def cells(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in s.split("|")]


SEP = re.compile(r"^\|[\s:|-]+\|?\s*$")
ADDRESS = re.compile(r"github\.com/([A-Za-z0-9._-]+)/([A-Za-z0-9._-]+)")


def grade(cell):
    """Five verdicts, because a heading can be contradicted in more than one way."""
    low = cell.lower()
    hits = sorted({name for pat, name in EXCLUDERS if re.search(pat, low)})
    permissive = any(re.search(p, low) for p in PERMISSIVE)
    if not hits:
        return ("PASS", "permissive") if permissive \
            else ("VOCAB-MISS", "names a grant outside the heading's five")
    if hits == ["no grant"]:
        if permissive and REFUTATION.search(cell):
            return "PASS-REFUTED-METADATA", "byte-read grant stated against a NOASSERTION/NONE field"
        if permissive:
            return "FAIL-SPLIT", "permissive token and a no-grant token, no refutation marker"
        return "FAIL-EXCLUDED", "no grant"
    if permissive:
        return "FAIL-SPLIT", ",".join(hits) + " alongside a permissive half"
    return "FAIL-EXCLUDED", ",".join(hits)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--tsv")
    args = ap.parse_args(argv)

    shelves = signatures(os.path.join(HERE, "derive-counts.py"))
    rows_out, rc, summary = [], 0, []

    for rel, counted, _notcounted in shelves:
        path = os.path.join(args.root, rel)
        if not os.path.exists(path):
            continue
        counted_n = {norm(s) for s in counted}
        lines = open(path, encoding="utf-8", errors="replace").read().split("\n")

        VERDICTS = ["PASS", "PASS-REFUTED-METADATA", "FAIL-EXCLUDED", "FAIL-SPLIT",
                    "VOCAB-MISS"]
        i, n_rows, verdicts = 0, 0, {k: 0 for k in VERDICTS}
        abstained, predicates = 0, set()
        while i < len(lines):
            if norm(lines[i]) in counted_n:
                # The predicate is this TABLE's nearest preceding '## ' heading.
                heading = next((lines[k] for k in range(i, -1, -1)
                                if lines[k].startswith("## ")), "")
                predicate = (norm(heading)
                             if HEADING_GRANTS.search(heading)
                             and not PASS_HEADING.search(heading) else None)
                header = cells(lines[i])
                lic_idx = next((k for k, c in enumerate(header)
                                if re.fullmatch(r"licen[cs]e.*", c.strip().lower())
                                or c.strip().lower().startswith(("licence", "license", "grant", "actual licen"))), None)
                j = i + 1
                if j < len(lines) and SEP.match(lines[j]):
                    j += 1
                while j < len(lines) and lines[j].lstrip().startswith("|") and not SEP.match(lines[j]):
                    c = cells(lines[j])
                    if lic_idx is not None and lic_idx < len(c) and c[lic_idx]:
                        if predicate is None:
                            abstained += 1
                            j += 1
                            continue
                        predicates.add(predicate)
                        n_rows += 1
                        v, why = grade(c[lic_idx])
                        verdicts[v] += 1
                        m = ADDRESS.search(lines[j])
                        addr = f"{m.group(1)}/{m.group(2)}" if m else "-"
                        if v != "PASS":
                            rows_out.append((rel, str(j + 1), addr, v, why,
                                             c[lic_idx][:110].replace("\t", " ")))
                    j += 1
                i = j
            else:
                i += 1

        fails = verdicts["FAIL-EXCLUDED"] + verdicts["FAIL-SPLIT"]
        print(f"{rel:<26} graded={n_rows}  abstained={abstained} (table under a heading that "
              f"names no grant)")
        for p in sorted(predicates):
            print(f"{'':26} predicate: {p[:88]}")
        if not n_rows:
            print(f"{'':26} ABSTAIN — no counted table on this page sits under a "
                  f"grant-naming heading")
            summary.append((rel, "ABSTAIN", 0, abstained, 0))
            continue
        print(f"{'':26} PASS={verdicts['PASS']}  "
              f"PASS-REFUTED-METADATA={verdicts['PASS-REFUTED-METADATA']}  "
              f"FAIL-EXCLUDED={verdicts['FAIL-EXCLUDED']}  "
              f"FAIL-SPLIT={verdicts['FAIL-SPLIT']}  VOCAB-MISS={verdicts['VOCAB-MISS']}")
        summary.append((rel, "GRADED", n_rows, fails, verdicts["VOCAB-MISS"]))
        if fails:
            rc = 1

    for rel, line, addr, v, why, cell in rows_out:
        print(f"  {v:<10} {rel}:{line}  {addr}  [{why}]  {cell}")
    if args.tsv:
        with open(args.tsv, "w", encoding="utf-8") as fh:
            fh.write("shelf\tline\taddress\tverdict\twhy\tlicence_cell\n")
            for r in rows_out:
                fh.write("\t".join(r) + "\n")
        print(f"\nper-row record -> {args.tsv}")
    return rc


if __name__ == "__main__":
    sys.exit(main())
