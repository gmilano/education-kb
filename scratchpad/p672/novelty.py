#!/usr/bin/env python3
"""667-H: novelty must be tested against a TREE CORPUS, not evidence/address-ledger.tsv
(the ledger over-reported by 44.2% at p667: 683 'novel' of which 302 were already
in the non-archive tree). 672-A: the corpus walk must EXCLUDE this pass's own
scratchpad, or the candidate list scores itself as held."""
import os, re, sys, csv
csv.field_size_limit(10_000_000)  # one repo description exceeded the 128 KiB default

ROOT="/tmp/education-kb"
EXCL=os.path.join(ROOT,"scratchpad","p672")
TEXT_EXT={".md",".markdown",".rst",".txt",".json",".yml",".yaml",".toml",".html",
          ".py",".ts",".tsx",".js",".jsx",".sh",".tsv",".csv",".cfg"}
def collapse(s): return re.sub(r"\s+"," ",s).lower()

buf=[]
for dp,dn,fn in os.walk(ROOT):
    dn[:]=[d for d in dn if d!=".git"]
    if os.path.abspath(dp).startswith(EXCL):
        dn[:]=[]; continue
    for f in fn:
        if os.path.splitext(f)[1].lower() in TEXT_EXT:
            p=os.path.join(dp,f)
            try:
                if os.path.getsize(p)<12_000_000:
                    buf.append(collapse(open(p,errors="replace").read()))
            except OSError: pass
corpus="\n".join(buf)
sys.stderr.write("corpus chars=%d\n"%len(corpus))
# control: a nonsense slug must be novel
assert collapse("zzqx672nobodyrepo/nothing") not in corpus, "CONTROL FAILED"
sys.stderr.write("control OK: nonsense slug absent\n")
# control: a known-held slug must NOT be novel
assert collapse("moodle/moodle") in corpus, "CONTROL FAILED (known-held absent)"
sys.stderr.write("control OK: moodle/moodle present\n")

rows=list(csv.DictReader(open(sys.argv[1]), delimiter="\t"))
print("leg\tslug\tstars\tspdx\tpushed_at\tnovelty\tdescription")
seen=set()
for r in rows:
    slug=r["slug"]
    if slug in seen: continue
    seen.add(slug)
    owner,_,name=slug.partition("/")
    full = collapse(slug) in corpus
    nameonly = collapse(name) in corpus
    nov = "HELD-FULL-SLUG" if full else ("NAME-SEEN" if nameonly else "NOVEL")
    print("\t".join([r["leg"],slug,r["stars"],r["spdx"],r["pushed_at"],nov,r["description"][:90]]))
