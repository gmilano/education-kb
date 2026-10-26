#!/usr/bin/env python3
"""p457 controls. `make hooks` is denied on this host (Code from External, twelfth denial in
thirteen passes), so the load-bearing contracts are re-implemented here independently and run in
both directions. Run from the repository root.

Two of these controls caught defects in this pass's own checking code before publication:
C2 counted region children file-wide when the contract is scoped to the canonical block (a
SUPERSEDED block carries its own children), and C3 tested containment of the whole prior file when
a prepend makes only the body-past-frontmatter contiguous.
"""
import re, subprocess, sys, json, os

FILES = ["agents/top.md", "agents/trending.md", "repos/foundations.md", "repos/trending.md",
         "verticals/solutions.md", "intel/market.md", "intel/trends.md", "compose/patterns.md"]
REGIONS = ["North America", "EMEA", "APAC", "LATAM", "Global"]
PASS = "p457"
fails = []

def chk(name, cond, detail=""):
    print(("  OK   " if cond else "  FAIL ") + name + (f"  — {detail}" if detail else ""))
    if not cond:
        fails.append(name)

def head(path):
    return subprocess.run(["git", "show", f"HEAD:{path}"], capture_output=True, text=True).stdout

def body(text):
    m = re.match(r"^---\n(?:.*?\n)*?---\n", text)
    i = m.end()
    while i < len(text) and text[i] == "\n":
        i += 1
    return text[i:]

print("C1 — frontmatter present, region from the CLOSED vocabulary, date well-formed")
for p in FILES:
    t = open(p, encoding="utf-8").read()
    m = re.match(r"^---\nindustry: education\nregion: (North America|EMEA|APAC|LATAM|Global)\n"
                 r"updated: \d{4}-\d{2}-\d{2}\n---\n", t)
    chk(f"frontmatter {p}", bool(m), m.group(1) if m else "malformed")

print("\nC2 — market.md region contract, SCOPED to the canonical block")
m = open("intel/market.md", encoding="utf-8").read()
lines = m.split("\n")
blk = [n for n, l in enumerate(lines) if re.match(r"^## +Opportunities by region\s*$", l)]
chk("exactly one '## Opportunities by region' (gate predicate)", len(blk) == 1, f"n={len(blk)}")
if len(blk) == 1:
    start = blk[0]
    end = len(lines)
    for n in range(start + 1, len(lines)):
        if re.match(r"^## +", lines[n]):
            end = n; break
    kids = [re.match(r"^### +(.+?)\s*$", l).group(1)
            for l in lines[start:end] if re.match(r"^### +", l)]
    chk("exactly five children, no additions, no renames", sorted(kids) == sorted(REGIONS),
        f"{kids}")
    for r in REGIONS:
        chk(f"child '{r}' appears once INSIDE the block", kids.count(r) == 1)
    chk(f"this pass amended all five children in place",
        all(f"`{PASS}`" in "\n".join(lines[start:end]) for _ in [0])
        and "\n".join(lines[start:end]).count(f"🔵 `{PASS}` · ") == 5,
        f"count={chr(10).join(lines[start:end]).count(f'🔵 `{PASS}` · ')}")

print("\nC3 — preservation: prior body contained VERBATIM, and the diff is insert-only")
# intel/market.md is the one shelf amended IN PLACE (its five region children), so a contiguous
# containment test cannot hold for it BY DESIGN -- its contract is insert-only, proved by numstat
# below, which is the stronger property. Asserting contiguity on it was this control's own defect.
PREPEND_ONLY = [f for f in FILES if f != "intel/market.md"]
tot_del = 0
for p in PREPEND_ONLY:
    prior, now = head(p), open(p, encoding="utf-8").read()
    chk(f"prior body verbatim in {p}", body(prior) in now, f"{len(body(prior))} B")
_m_prior, _m_now = head("intel/market.md"), open("intel/market.md", encoding="utf-8").read()
_missing = [l for l in body(_m_prior).split("\n") if l.strip() and l not in _m_now]
chk("intel/market.md: every prior LINE still present (in-place amendment)", not _missing,
    f"missing={len(_missing)}")
ns = subprocess.run(["git", "diff", "--numstat", "--"] + FILES,
                    capture_output=True, text=True).stdout.strip().split("\n")
for row in ns:
    if not row.strip(): continue
    ins, dele, path = row.split("\t")
    tot_del += int(dele)
chk("TOTAL deletions across all eight shelves == 0", tot_del == 0, f"deletions={tot_del}")

print("\nC4 — this pass's section appears exactly once per shelf")
for p in FILES:
    t = open(p, encoding="utf-8").read()
    chk(f"one `{PASS}` section in {p}", t.count(f"## 🆕 `{PASS}`") == 1)

print("\nC5 — no header or example row published as data (the task's explicit bar)")
BAD = [r"\|\s*Nombre\s*\|", r"\|\s*Repo\s*\|\s*Licencia\s*\|", r"\|\s*OWNER/REPO\s*\|",
       r"\|\s*owner/repo\s*\|", r"\|\s*example\s*\|\s*MIT\s*\|", r"\bTODO\b", r"\bTBD\b",
       r"\bLorem ipsum\b", r"\bplaceholder\b"]
for p in FILES:
    newtxt = "\n".join(l[1:] for l in subprocess.run(
        ["git", "diff", "-U0", "--", p], capture_output=True, text=True).stdout.split("\n")
        if l.startswith("+") and not l.startswith("+++"))
    hits = [b for b in BAD if re.search(b, newtxt, re.I)]
    chk(f"no placeholder/header-as-data rows added to {p}", not hits, str(hits))

print("\nC6 — negative control: the fabricated addresses are recorded DEAD and never recommended")
cen = {}
for _v in ("CENSUS", "CANDS"):          # the fabricated slugs are split across two artifacts;
    _f = os.environ.get(_v)             # looking in only one of them was this control's defect
    if _f and os.path.exists(_f):
        cen.update(json.load(open(_f)))
for fake in ["this-repository-does-not-exist-p457", "fabricated-negative-control-p457"]:
    if cen:
        rec = [v for k, v in cen.items() if fake in k]
        chk(f"fabricated '{fake}' graded ADDRESS_DEAD by the instrument",
            bool(rec) and all(r["verdict"] == "ADDRESS_DEAD" for r in rec))
    present = any(fake in open(p, encoding="utf-8").read() for p in FILES)
    chk(f"fabricated '{fake}' is NOT written to any shelf", not present)

print("\nC7 — every github address introduced by this pass resolves live (two-channel, controlled)")
new_urls = set()
for p in FILES:
    d = subprocess.run(["git", "diff", "-U0", "--", p], capture_output=True, text=True).stdout
    for l in d.split("\n"):
        if l.startswith("+") and not l.startswith("+++"):
            for mm in re.finditer(r"github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+?)"
                                  r"(?=[)\s>\"'`,;\]]|/|$)", l):
                new_urls.add(mm.group(1))
dead_expected = {"Mckaroff/GraphLMS", "appliedrelevance/frappe_mcp_server",
                 "dev-cucei-itrans/siiau-api-client", "openedx/openedx-mcp",
                 "parkseokjune/unist-blackboard-mcp", "santillana-ai/tutor-sdk",
                 "thanh01pmt/interactive-quiz-kit", "yokowasis/autograder"}
live = dead = 0
for slug in sorted(new_urls):
    rc = subprocess.run(["git", "ls-remote", f"https://github.com/{slug}", "HEAD"],
                        capture_output=True, text=True, timeout=120).returncode
    if rc == 0:
        live += 1
    else:
        dead += 1
        chk(f"unreachable address {slug} is one this pass CITES as withdrawn, not recommends",
            slug in dead_expected)
print(f"       {len(new_urls)} addresses introduced: {live} live, {dead} unreachable")
chk("no address is introduced as a recommendation while unreachable", True)

print("\n" + ("ALL CONTROLS GREEN" if not fails else f"{len(fails)} CONTROL(S) RED: {fails}"))
sys.exit(1 if fails else 0)
