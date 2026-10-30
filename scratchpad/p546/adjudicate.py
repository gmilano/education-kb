#!/usr/bin/env python3
"""p546 — final adjudication of the quote gate, with the gate's own defects applied.

Three defects were found in this instrument's construction and are corrected
here rather than hidden, because each one produced a WRONG VERDICT on a row that
is in fact correct:

  D1  ` / ` is this base's line-join notation inside a quoted title block.
      PAIDEIA's row quotes *"MIT License / Copyright (c) 2026 Taewoo Park"*, and
      the LICENSE file really does carry both lines — the slash does not occur
      in it. Treated as one literal string the gate FAILED a correct row.
      ` / ` is now a span separator, exactly like an ellipsis.

  D2  three "quotes" are parser artefacts, not quotes: the quote regex
      straddled a markdown emphasis marker and captured fragments like
      "*), and it states it is *". They are dropped, not scored.

  D3  the self-attribution filter is deliberately conservative and still missed
      one base-internal quote (mcp-canvas-lms' "for four passes, and this base's
      own `gate-enumeration`…"). Dropped on the same rule, applied late.

Residual verdicts are then split by FIELD, because the fields do not share a
channel:
  PASS                      found in the artefact's own files
  ABOUT-ONLY/UNADJUDICABLE  a `description`-field quote absent from the tree.
                            The GitHub About line is metadata, not a file; it is
                            served only by the API, and the API is refused for
                            repositories outside this session's scope. So the
                            gate CANNOT separate a legitimate About-line quote
                            from the avit defect for these rows, and says so.
  FAIL                      absent from the tree in a field the tree does hold
                            (licence, region, prose) — the avit class.
"""
import csv
import json
import re
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from importlib import import_module
qg = import_module("quote-gate")

SPAN_SPLIT = re.compile(r"\s*(?:\.\.\.|…|\s/\s)\s*")
ARTEFACT_QUOTE = re.compile(r"^\W{0,3}(\*|\))|\*\s*$|^\s*(is|and|for)\s")


def spans(quote):
    return [s for s in SPAN_SPLIT.split(qg.norm(quote).rstrip(".!?,;: ")) if len(s) >= 10]


charged = {str(r["qid"]): r for r in json.load(open("charged.json")) if "qid" in r}
rows = list(csv.DictReader(open("out/fulltree.tsv"), delimiter="\t"))

out, counts = [], {}
for r in rows:
    c = charged.get(r["id"])
    if not c:
        continue
    q, field, v = c["quote"], c["field"], r["verdict"]

    if ARTEFACT_QUOTE.search(q) or len(qg.norm(q)) < 12:
        v2, why = "DROPPED", "D2 parser artefact, not a quote"
    elif qg.SELF_ATTRIB_RE.search(q):
        v2, why = "DROPPED", "D3 base-internal quote caught late"
    elif v == "PASS":
        v2, why = "PASS", r["file"]
    elif v == "CLONE-FAILED":
        v2, why = "NO-PAYLOAD", "tree not served"
    elif len(spans(q)) > 1:
        v2, why = "RECHECK-SPANS", "D1 multi-span quote; needs per-span probe"
    elif field == "description":
        v2, why = "ABOUT-ONLY", "absent from tree; About line unreachable (API scope)"
    else:
        v2, why = "FAIL", f"absent from tree in field '{field}'"

    counts[v2] = counts.get(v2, 0) + 1
    out.append({"verdict": v2, "slug": r["slug"], "field": field,
                "why": why, "quote": q, "line": c["line"]})

with open("out/adjudicated.tsv", "w", encoding="utf-8") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(["verdict", "line", "slug", "field", "why", "quote"])
    for r in sorted(out, key=lambda x: (x["verdict"], x["slug"])):
        w.writerow([r["verdict"], r["line"], r["slug"], r["field"],
                    r["why"], r["quote"].replace("\t", " ")])

print("# adjudicated:", counts)
for want in ("FAIL", "RECHECK-SPANS", "NO-PAYLOAD"):
    sel = [r for r in out if r["verdict"] == want]
    if sel:
        print(f"\n# {want} ({len(sel)})")
        for r in sel:
            print(f"  L{r['line']} {r['slug']} [{r['field']}]  {r['quote'][:100]}")
