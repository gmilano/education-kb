#!/usr/bin/env python3
"""`p407-i2-sweep-crosscheck` — `Gap 406-A`, the cross-check `p406` named as the next item.

🔴 `Gap 406-A` reads: *"The honest question is whether `I2`'s live-shelf test and this sweep
AGREE on all 59 — they were not cross-checked, and a disagreement would be a finding on one
of them."*

This module joins the two populations and grades every disagreement by MECHANISM, because
"they disagree" is not a finding — *why* they disagree is, and the two instruments turn out to
disagree for four different reasons that call for four different repairs.

🔵 **The join key is FOLDED, and the fold is load-bearing.** `p406` publishes folded addresses
(`population()` keys on `a` lowercased); `p372`'s re-probe publishes the shelf's own casing
(`EastArctica/canvas-mcp`, `1EdTech/caliper-java`, `AlekSIS/AlekSIS-Core`). A raw join reports
disagreements that are pure spelling — control `C2` asserts exactly that.

🔴 **And the fold is also where the obvious repair BREAKS.** `I2`'s detector is a
case-SENSITIVE substring (`f"github.com/{slug})" in line`). Wiring `p406`'s folded population
into `I2` — the natural fix for the population half of this gap — makes the detector stop
matching the three addresses whose live-shelf link is written in mixed case. `C10` pins that.
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))

# ── p372's taxonomy, IMPORTED — never reimplemented ──────────────────────────────────────
# 🔴 `P237`/`P960`: a second copy of a classifier is how this base published seven false
# AGPL verdicts and two wrong LGPL cells. `grant-ladder-v4` deliberately has no classifier
# of its own, and neither does this. The import is resolved relative to THIS file so the
# module runs from any cwd (`p355-cwd-portability`).
# 🔵 This pass's draft reimplemented it instead, on the belief that `P970` ("cannot execute
# repository code") still held. It does not hold this session — see this module's README.
# 🟢 `C11` still cross-checks the imported classifier against `p372`'s own published
# partition, because an import proves identity, not correctness.
sys.path.insert(0, os.path.join(_HERE, os.pardir, "p372-dead-citation"))
from dead_citation import (LIVE_SHELVES, RECORD_FILES,  # noqa: E402
                           citation_is_a_live_claim, classify_string)

#: `p406`'s shelf set, which is `p376`'s.
SWEPT_SHELVES = ("agents/top.md", "agents/trending.md", "repos/foundations.md",
                 "repos/trending.md", "verticals/solutions.md", "intel/market.md",
                 "intel/trends.md", "intel/open-gaps.md", "compose/patterns.md")

#: 🔴 `Gap 406-B`'s lesson, applied at construction rather than after the fact: the guard is on
#: COMPLETENESS of the shelf set, never on existence. A shelf that disappears must make this
#: instrument REFUSE, not silently shrink its population to the files that happen to resolve.
UNCLASSIFIED_SHELVES = tuple(s for s in SWEPT_SHELVES
                             if s not in LIVE_SHELVES and s not in RECORD_FILES)

I2_ABSENT_CLASSES = ("ABSENT-NO-SUCCESSOR-FOUND", "OWNER-ALIVE-REPO-ABSENT",
                     "MOVED", "ALIVE-OTHER-FORGE")


def i2_predicate(line, slug):
    """`gate-dead-citation` I2's detector, verbatim: only a LINKED row asserts usability."""
    return f"github.com/{slug})" in line or f"github.com/{slug} " in line


def rows(path):
    with open(path, encoding="utf-8") as fh:
        head = None
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if head is None:
                head = parts
                continue
            yield dict(zip(head, parts))


def load_sweep(path):
    """folded address -> (verdict, shelves tuple)."""
    out = {}
    for r in rows(path):
        out[r["address"]] = (r["verdict"], tuple(s for s in r["shelves"].split(";") if s))
    return out


def load_i2_absent(path):
    """p372's absent set, in the shelf's own casing, plus the folded index."""
    original = [r["slug"] for r in rows(path) if r["class_p372"] in I2_ABSENT_CLASSES]
    return original, {s.lower(): s for s in original}


def shelf_lines(root, shelves):
    """🔴 Completeness, not existence (`Gap 406-B`). A missing shelf raises."""
    missing = [s for s in shelves if not os.path.exists(os.path.join(root, s))]
    if missing:
        raise SystemExit("p407: shelf set incomplete, refusing to grade: %s" % ", ".join(missing))
    out = {}
    for s in shelves:
        with open(os.path.join(root, s), encoding="utf-8") as fh:
            out[s] = fh.readlines()
    return out


def i2_hits(lines_by_shelf, slug, fold_line=False):
    """Where I2's detector fires. `fold_line` models a case-INSENSITIVE detector."""
    hits = []
    for shelf, lines in lines_by_shelf.items():
        for n, line in enumerate(lines, 1):
            probe = line.lower() if fold_line else line
            if i2_predicate(probe, slug):
                hits.append((shelf, n))
    return hits


def grade(sweep, i2_original, i2_folded, live_lines):
    """One row per sweep-unresolved address, with the mechanism of any disagreement."""
    graded = []
    for addr, (verdict, shelves) in sorted(sweep.items()):
        if verdict != "ABSENT-OR-PRIVATE":
            continue
        shape = classify_string(addr)
        on_live = tuple(s for s in shelves if s in LIVE_SHELVES)
        in_pop = addr in i2_folded
        # the detector as it ships, fed the folded population this gap invites
        fires_folded = i2_hits(live_lines, addr) if on_live else []
        # the detector fed the casing p372 actually holds
        fires_original = (i2_hits(live_lines, i2_folded[addr]) if in_pop and on_live else [])
        # a case-insensitive detector: the ceiling of what a link test can see
        fires_ci = i2_hits(live_lines, addr, fold_line=True) if on_live else []

        if shape != "ADDRESS":
            mech = "NOT-DECAY-P372-REFUTES"
        elif not on_live:
            mech = "AGREE-OFF-LIVE-SHELVES"
        elif not in_pop:
            mech = "DISAGREE-I2-POPULATION-FROZEN"
        elif fires_ci and not fires_folded:
            mech = "DISAGREE-CASE-SENSITIVE-DETECTOR"
        elif fires_ci:
            mech = "DISAGREE-I2-WOULD-FIRE-ON-A-RECORD"
        else:
            mech = "AGREE-NOT-A-LIVE-CLAIM"
        graded.append({
            "address": addr, "shape": shape, "on_live_shelf": ";".join(on_live) or "-",
            "in_i2_population": "yes" if in_pop else "no",
            "i2_fires_folded": len(fires_folded), "i2_fires_original": len(fires_original),
            "i2_fires_caseless": len(fires_ci), "mechanism": mech,
            "first_hit": ("%s:%d" % fires_ci[0]) if fires_ci else "-",
        })
    return graded


def substring_inflation(sweep):
    """🔴 `p406`'s attribution is `if a in body` on the folded file — `p400`'s defect class.

    Any swept address that is a PROPER SUBSTRING of another swept address inherits every
    shelf the longer one appears on. Returns (short, long) pairs.
    """
    addrs = list(sweep)
    return sorted((a, b) for a in addrs for b in addrs if a != b and a in b)


def decay(sweep, contaminants):
    """`p406`'s rate, and the rate with the non-addresses taken off both sides."""
    resolved = sum(1 for v, _ in sweep.values() if v in ("EXISTS-PUBLIC", "EXISTS-NO-REFS"))
    unresolved = sum(1 for v, _ in sweep.values() if v == "ABSENT-OR-PRIVATE")
    graded_den = resolved + unresolved
    published = unresolved / graded_den if graded_den else None
    corrected_den = graded_den - contaminants
    corrected = (unresolved - contaminants) / corrected_den if corrected_den else None
    return resolved, unresolved, published, corrected
