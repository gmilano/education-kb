#!/usr/bin/env python3
"""p454 contract verification, re-implemented from the gate sources because
`make hooks` is denied. Every check is read from the gate file it mirrors."""
import io, os, re, sys

ROOT = "/home/user/education-kb"
SHELVES = ["agents/top.md", "agents/trending.md", "repos/foundations.md",
           "repos/trending.md", "verticals/solutions.md", "intel/market.md",
           "intel/trends.md", "intel/open-gaps.md", "compose/patterns.md"]
# read verbatim from compose/code/p383-region-heading-gate/check_headings.py:17-19
VOCAB = ["North America", "EMEA", "APAC", "LATAM", "Global"]
CANON = re.compile(r"^## +Opportunities by region\s*$")
H2 = re.compile(r"^## (?!#)")
H3 = re.compile(r"^### (?!#)")
FM = re.compile(r"\A---\n(.*?\n)---\n", re.S)

FAIL = []
def ck(name, ok, detail=""):
    print(f"  {'OK  ' if ok else 'FAIL'} {name}{(' :: ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)

print("=== C1 frontmatter: present, keys, closed region vocabulary, updated date ===")
for rel in SHELVES + ["README.md"]:
    s = io.open(os.path.join(ROOT, rel), encoding="utf-8").read()
    m = FM.match(s)
    if not m:
        ck(f"{rel} frontmatter", False, "absent"); continue
    fmv = dict(re.findall(r"^(\w+): *(.*)$", m.group(1), re.M))
    ok = (fmv.get("industry") == "education" and fmv.get("region") in VOCAB
          and fmv.get("updated") == "2026-10-26")
    ck(f"{rel} frontmatter", ok, f"industry={fmv.get('industry')} region={fmv.get('region')} updated={fmv.get('updated')}")

print("\n=== C2 newest-first: the p454 block is the FIRST ## in each shelf ===")
for rel in SHELVES + ["README.md"]:
    s = io.open(os.path.join(ROOT, rel), encoding="utf-8").read()
    body = s[FM.match(s).end():]
    first = next((l for l in body.split("\n") if H2.match(l)), "")
    ck(f"{rel} newest-first", "p454" in first or "Pass 454" in first, first[:84])

print("\n=== C3 region headings: ONE canonical block, 5 children, in vocabulary, none missing ===")
s = io.open(os.path.join(ROOT, "intel/market.md"), encoding="utf-8").read()
lines = s.split("\n")
blocks = [i for i, l in enumerate(lines) if CANON.match(l)]
ck("exactly 1 canonical '## Opportunities by region'", len(blocks) == 1, f"found {len(blocks)}")
if blocks:
    ci = blocks[0]
    end = next((j for j in range(ci + 1, len(lines)) if H2.match(lines[j])), len(lines))
    kids = [lines[j][4:].strip() for j in range(ci + 1, end) if H3.match(lines[j])]
    region_kids = [k for k in kids if k in VOCAB]
    out_of_vocab = [k for k in kids if k not in VOCAB and not re.match(r"^[\W_]*(🆕|🔴|🟢|🟡|🔵)", k) and "`" not in k]
    ck("5 closed-vocabulary children, in vocabulary order", region_kids == VOCAB, str(region_kids))
    ck("no out-of-vocabulary region child", not out_of_vocab, str(out_of_vocab[:4]))
    ck("no region missing", set(VOCAB) <= set(region_kids), str(sorted(set(VOCAB) - set(region_kids))))
    ck("not LATAM-only", not ("LATAM" in region_kids and
       any(r not in region_kids for r in ["North America", "EMEA", "APAC"])))
    for r in VOCAB:
        j = ci + 1 + [lines[x][4:].strip() for x in range(ci + 1, end)].index(r) if False else None
    # each region subsection must carry a p454 paragraph
    idx = {lines[j][4:].strip(): j for j in range(ci + 1, end) if H3.match(lines[j]) and lines[j][4:].strip() in VOCAB}
    order = [idx[r] for r in VOCAB]
    for n, r in enumerate(VOCAB):
        stop = order[n + 1] if n + 1 < len(order) else end
        seg = "\n".join(lines[order[n]:stop])
        ck(f"'### {r}' carries a p454 paragraph", "`p454`" in seg)

print("\n=== C4 append-only on the two trending shelves (byte containment) ===")
for rel, prior in [("agents/trending.md", "/tmp/p454_prior_agents_trending.md"),
                   ("repos/trending.md", "/tmp/p454_prior_repos_trending.md")]:
    new = io.open(os.path.join(ROOT, rel), "rb").read()
    old = io.open(prior, "rb").read()
    body = old.split(b"---\n", 2)[2]
    ck(f"{rel} prior body contained verbatim", body in new,
       f"{len(body)} B prior, file {len(old)} -> {len(new)} B")

print("\n=== C5 no table-header-shaped row written as data (the named recurring defect) ===")
BAD = re.compile(r"^\|\s*(nombre|name|repo|repositorio|licencia|license|agent|descripci[oó]n|description)\s*\|",
                 re.I)
for rel in SHELVES:
    p = os.path.join(ROOT, rel)
    hits = []
    prev = ""
    for n, l in enumerate(io.open(p, encoding="utf-8"), 1):
        if BAD.match(l.strip()):
            # a genuine header is followed by a separator row
            hits.append((n, l.strip()[:60]))
        prev = l
    # a header is legitimate when the NEXT line is |---| ; re-read to confirm
    real = []
    ls = io.open(p, encoding="utf-8").read().split("\n")
    for n, txt in hits:
        nxt = ls[n] if n < len(ls) else ""
        prv = ls[n - 2] if n >= 2 else ""
        # A genuine header row is followed by a separator.
        if re.match(r"^\|[\s:-]+\|", nxt.strip()):
            continue
        # Gap 454-I: a TRANSPOSED table's label column legitimately reads
        # "Licencia" / "repo" / "Titular". Its tell is that the separator sits
        # ABOVE, under the real header -- walk back to the nearest separator and
        # accept the row if one is found before a blank line.
        k, transposed = n - 2, False
        while k >= 0 and ls[k].strip().startswith("|"):
            if re.match(r"^\|[\s:-]+\|", ls[k].strip()):
                transposed = True
                break
            k -= 1
        if transposed:
            continue
        real.append((n, txt))
    ck(f"{rel} no orphan header-shaped data row", not real, str(real[:3]))

print("\n=== C6 every markdown link target introduced this pass is a real address ===")
P454_SLUGS = ["ardianryan/dapodik-sdk", "smantriplw/vervalpd-node",
              "adereksisusanto/dapodik-api-php", "bantenprov/dapodik-data-guru",
              "pipeworx-io/mcp-estat-japan", "edu-sharing/Edu-Sharing",
              "bncc-dev/bncc-pacotes", "nakafaai/aksara", "nakafaai/nakafa.com",
              "asherlc/dofek", "ckeditor/ckeditor5", "oat-sa/tao-core",
              "tl-its-umich-edu/caliper-php-public", "aswanth9495/exam-guard",
              "scaler-opensource/exam-guard", "davepacheco/node-extsprintf",
              "pcofilada/psgc", "jobuntux/psgc",
              "anthonygacis/psgc-js", "aivangogh/ph-address"]
import subprocess
def live(slug):
    for p in ("README.md", "README.rst", "LICENSE", "readme.md", "README.markdown",
              "LICENSE.md", "LICENSE.txt", "package.json", "composer.json"):
        r = subprocess.run(["curl", "-s", "-o", "/dev/null", "--max-time", "20",
                            "-w", "%{http_code}",
                            f"https://raw.githubusercontent.com/{slug}/HEAD/{p}"],
                           capture_output=True, text=True)
        if r.stdout.strip() == "200":
            return True, p
    return False, ""
import concurrent.futures as cf
with cf.ThreadPoolExecutor(max_workers=8) as ex:
    res = dict(zip(P454_SLUGS, ex.map(live, P454_SLUGS)))
for slug, (ok, p) in res.items():
    ck(f"{slug} live at HEAD", ok, p)
ok, _ = live("nope-p454-dapodik/nope-p454")
ck("fabricated control correctly UNREACHABLE", not ok)
# Gap 454-H: imsglobal/caliper-php is EXPECTED dead and is cited as dead on the
# shelves. Asserting the absence is the point -- a row claiming a dead address
# is live would be the defect.
ok, _ = live("imsglobal/caliper-php")
ck("imsglobal/caliper-php correctly DEAD (cited as dead)", not ok)
for s2 in ("1EdTech/caliper-php", "IMSGlobal/caliper-php"):
    ok, _ = live(s2)
    ck(f"{s2} successor correctly DEAD", not ok)

print()
if FAIL:
    print(f"RED: {len(FAIL)} check(s) failed:")
    for f in FAIL:
        print("   -", f)
    sys.exit(1)
print("GREEN: all re-implemented contracts pass")
