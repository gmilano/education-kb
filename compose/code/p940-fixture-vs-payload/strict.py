#!/usr/bin/env python3
"""p940 STRICT arm. The naive arm (sweep.py) reported 1,502 conflicts; p928-G1 says
control the control first. This arm admits a published fixture ONLY when the line is
unambiguous:

  * exactly ONE repo slug on the line
  * exactly ONE 12-hex hash on the line
  * exactly ONE byte figure on the line
  * the slug is a plausible owner/repo (not a URL path fragment like main/LICENSE)

and compares it only against evidence rows for THAT slug that carry BOTH a byte count
and a hash. Everything else is reported as ABSTAIN, not as a conflict.
"""
import re, sys, glob, os, collections

ROOT = os.path.join(os.path.dirname(__file__), "..", "..", "..")
LIVE = ["agents/top.md", "agents/trending.md", "repos/foundations.md",
        "repos/trending.md", "verticals/solutions.md", "intel/market.md",
        "intel/trends.md", "compose/patterns.md", "intel/open-gaps.md",
        "intel/measured-unusable.md"]

SLUG  = re.compile(r"github\.com/([A-Za-z0-9][\w.-]*)/([\w.-]+?)(?=[)\s`,\]/]|$)")
BYTES = re.compile(r"([0-9][0-9,   ]{0,9}[0-9]|[0-9])\s*B\b")
HASH12= re.compile(r"\b([0-9a-f]{12})\b")
REFWORD = {"main","master","blob","tree","raw","LICENSE","LICENSE.md","COPYING"}

def ni(s): return int(re.sub(r"[^0-9]", "", s))

def strict_fixtures():
    out, abstain = [], 0
    for rel in LIVE:
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p): continue
        for ln, line in enumerate(open(p, encoding="utf-8"), 1):
            hs = set(HASH12.findall(line))
            if not hs: continue
            slugs = {f"{o}/{r}" for o, r in SLUG.findall(line)
                     if o not in REFWORD and r not in REFWORD}
            bs = {ni(b) for b in BYTES.findall(line)}
            if len(hs) == 1 and len(slugs) == 1 and len(bs) == 1:
                out.append((rel, ln, slugs.pop(), bs.pop(), hs.pop()))
            else:
                abstain += 1
    return out, abstain

def evidence_pairs():
    """slug -> {(bytes, hash12): {files}}  only rows carrying BOTH."""
    ev = collections.defaultdict(lambda: collections.defaultdict(set))
    for p in glob.glob(os.path.join(ROOT, "evidence", "*.tsv")):
        base = os.path.basename(p)
        for line in open(p, encoding="utf-8", errors="replace"):
            if "\t" not in line: continue
            f = [c.strip() for c in line.split("\t")]
            slug = next((c for c in f[:2] if re.fullmatch(r"[\w.-]+/[\w.-]+", c)), None)
            if not slug: continue
            h = next((c for c in f if re.fullmatch(r"[0-9a-f]{12}", c)), None)
            b = next((int(c) for c in f
                      if re.fullmatch(r"[0-9]{2,7}", c) and 50 <= int(c) <= 200000), None)
            if h and b:
                ev[slug][(b, h)].add(base)
    return ev

def main():
    fx, abstain = strict_fixtures()
    ev = evidence_pairs()
    print(f"ADMITTED fixtures (1 slug + 1 hash + 1 byte figure): {len(fx)}")
    print(f"ABSTAINED lines (ambiguous, NOT judged):             {abstain}")
    agree, nobacking, conflict = 0, 0, []
    for rel, ln, slug, b, h in fx:
        pairs = ev.get(slug)
        if not pairs:
            nobacking += 1; continue
        if (b, h) in pairs:
            agree += 1
        elif h in {hh for (_, hh) in pairs}:
            # hash known, byte count differs by 1 -> newline/trailing-byte accounting
            conflict.append(("BYTES-ONLY", rel, ln, slug, b, h, dict(
                ((bb, hh), sorted(v)) for (bb, hh), v in pairs.items() if hh == h)))
        else:
            conflict.append(("HASH", rel, ln, slug, b, h, dict(
                (k, sorted(v)) for k, v in pairs.items())))
    print(f"  agree with a byte-read pair exactly:               {agree}")
    print(f"  slug has no (bytes,hash) evidence:                 {nobacking}")
    print(f"  CONFLICT:                                          {len(conflict)}")
    print()
    for kind, rel, ln, slug, b, h, pairs in conflict:
        print(f"[{kind}] {slug}   {rel}:{ln}")
        print(f"   published: {b} B / {h}")
        for (bb, hh), files in sorted(pairs.items()):
            print(f"   byte-read: {bb} B / {hh}   <- {', '.join(files[:4])}")
        print()
    return 0

if __name__ == "__main__":
    sys.exit(main())
