#!/usr/bin/env python3
"""p672 leg scorer.

Implements 667-C: a leg scorer is only trustworthy with BOTH controls --
a nonsense needle (must score 0 at both scopes; guards 647-L false positives)
and a known-held fact in VARIANT spelling (must score >0; guards 667-B false
negatives from needle orthography).

Two scopes:
  shelf       = the 8 curated KB files the prompt names
  full_corpus = every text file in the tree except .git (archive, README,
                evidence, scratchpad included)

Needles are pipe-separated variants; a fact is HELD if ANY variant hits.
Matching is case-insensitive fixed-string over whitespace-collapsed text.
"""
import os, re, sys, json

ROOT = "/tmp/education-kb"
SHELF = ["agents/top.md","agents/trending.md","repos/foundations.md","repos/trending.md",
         "verticals/solutions.md","intel/market.md","intel/trends.md","compose/patterns.md"]

TEXT_EXT = {".md",".markdown",".rst",".txt",".json",".yml",".yaml",".toml",".html",
            ".py",".ts",".tsx",".js",".jsx",".sh",".tsv",".csv",".cfg"}

def collapse(s):
    return re.sub(r"\s+", " ", s).lower()

def load(paths):
    buf = []
    for p in paths:
        try:
            with open(p, "r", errors="replace") as fh:
                buf.append(collapse(fh.read()))
        except Exception:
            pass
    return "\n".join(buf)

def walk_corpus():
    out = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        # 672-A: the scorer must not read its own inputs/outputs. A tree-wide
        # corpus walk that includes this pass's scratchpad counts the needle
        # list itself, which lifts EVERY fact by at least 1 and converts a
        # genuine nil into a false HELD. The nonsense control is what catches
        # it: it scored 1, and 1 was its own definition.
        if os.path.abspath(dirpath).startswith(os.path.join(ROOT, "scratchpad", "p672")):
            dirnames[:] = []
            continue
        for fn in filenames:
            ext = os.path.splitext(fn)[1].lower()
            if ext in TEXT_EXT or fn.upper().startswith(("LICENSE","LICENCE","MAKEFILE")):
                fp = os.path.join(dirpath, fn)
                try:
                    if os.path.getsize(fp) < 12_000_000:
                        out.append(fp)
                except OSError:
                    pass
    return out

shelf_txt = load([os.path.join(ROOT,p) for p in SHELF])
corpus_files = walk_corpus()
corpus_txt = load(corpus_files)
sys.stderr.write("shelf chars=%d  corpus files=%d chars=%d\n"
                 % (len(shelf_txt), len(corpus_files), len(corpus_txt)))

def count(txt, needle):
    return txt.count(collapse(needle))

rows = json.load(open(sys.argv[1]))
print("region\tfact\tneedle_variants\tshelf_hits\tfull_corpus_hits\tverdict\tnote")
for r in rows:
    variants = r["needle"].split("|")
    s = sum(count(shelf_txt, v) for v in variants)
    c = sum(count(corpus_txt, v) for v in variants)
    if r.get("note") == "control":
        verdict = "HELD-ON-SHELF" if c > 0 else "NOVEL"
    else:
        verdict = "HELD-ON-SHELF" if c > 0 else "NOVEL"
    print("\t".join([r["region"], r["fact"], r["needle"], str(s), str(c), verdict,
                     r.get("note","-")]))
