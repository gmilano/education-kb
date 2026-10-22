#!/usr/bin/env python3
"""Offline controls for `p375-census-union` — `gate-census-union`, `ACTION p374-J`.

🔵 Every control here is a string or a committed file.  The 756 `ls-remote` verdicts this
instrument's vocabulary was DERIVED from are a first-hand measurement, committed as
`evidence/census-union-grade.2026-10-22-p375.tsv`; group 2 re-reads that file rather than
restating its numbers, so a later edit that adds a word with a live instance turns this suite
red instead of silently widening a rejection class.
"""
import os
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import census_union as C  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, os.pardir, os.pardir, os.pardir))
EVIDENCE = os.path.join(ROOT, "evidence", "census-union-grade.2026-10-22-p375.tsv")
SHELF_FILES = [
    "agents/top.md", "agents/trending.md", "repos/foundations.md", "repos/trending.md",
    "verticals/solutions.md", "intel/market.md", "intel/trends.md", "intel/open-gaps.md",
    "compose/patterns.md",
]

FAILED = []
N = 0


def check(num, what, got, want):
    global N
    N += 1
    if got != want:
        FAILED.append(f"🔴 {num}. {what}\n     got:  {got!r}\n     want: {want!r}")


def shelves():
    return [os.path.join(ROOT, f) for f in SHELF_FILES]


# ── group 1: the two one-sided arms, each with the string that prompted it ───────────────
check(1, "p367's arm 1 tests the OWNER position only, so a ref word in the NAME position "
         "survived it — `aoe-web-backend/license`, 16 of them in the 756",
      C.name_reject("aoe-web-backend/license"), "NAME-REF-OR-PATH")
check(2, "p351's NAME_RESERVED is {'.', '..'}, so a THREE-dot name survived — the residue "
         "of prose writing `github.com/owner/...`",
      C.name_reject("emaanrana012/..."), "NAME-DOT-RUN")
check(3, "a two-dot name stays p351's business, so the two rules cannot disagree",
      C.name_reject("foo/.."), None)
check(4, "an ellided OWNER stays p351's OWNER-ELLIDED, not re-judged here",
      C.name_reject(".../archive"), None)
check(5, "a token with no separator is not this arm's business",
      C.name_reject("notaslug"), None)
check(6, "a four-dot name is the same class as a three-dot name",
      C.name_reject("mebis-lp/...."), "NAME-DOT-RUN")
check(7, "an ordinary repository name is untouched",
      C.name_reject("hkuds/deeptutor"), None)

# ── group 2: the blanket fix is REFUTED BY MEASUREMENT, and the refutation is pinned ────
check(8, "the blanket fix would have eaten a LIVE repository: `mattpocock/skills`",
      C.name_reject("mattpocock/skills"), None)
check(9, "and a second one: `vercel-labs/skills`",
      C.name_reject("vercel-labs/skills"), None)
check(10, "`skills` must never enter the rejection vocabulary — 2 LIVE, 0 ABSENT measured",
       "skills" in C.NAME_NOT_A_REPO, False)
check(11, "every pinned negative control survives the vocabulary, whatever it grows to",
       [C.name_reject(s) for s in C.NAME_POSITION_NEGATIVE_CONTROLS], [None, None])

# 🔴 The self-checking control: the vocabulary is only legitimate while the committed
# measurement shows ZERO live instances of each word in the NAME position.
if os.path.exists(EVIDENCE):
    live_names = set()
    with open(EVIDENCE, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or "\t" not in line:
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) >= 3 and parts[2] in ("LIVE-ADDRESS", "LIVE-COMMITLESS"):
                live_names.add(parts[0].split("/", 1)[-1])
    check(12, "no word in NAME_NOT_A_REPO has a LIVE instance in the committed 756-row "
              "measurement — the vocabulary is derived, not guessed",
           sorted(C.NAME_NOT_A_REPO & live_names), [])
    check(13, "the committed measurement is the 756 the action named, not a sample",
           sum(1 for line in open(EVIDENCE, encoding="utf-8")
               if not line.startswith(("#", "folded")) and "\t" in line), 756)
else:
    check(12, "the derivation evidence file is committed beside the instrument",
           os.path.exists(EVIDENCE), True)

# ── group 3: grading precedence and p372's three liveness classes ───────────────────────
check(14, "SHAPE is asked before the network: a string that cannot be an address is a false "
          "positive whatever ls-remote says",
       C.grade("x/license", "LIVE"), "NAME-REF-OR-PATH")
check(15, "a live address grades as one", C.grade("hkuds/deeptutor", "LIVE"), "LIVE-ADDRESS")
check(16, "p372's third class is honoured: rc=0 with an EMPTY advertisement is a live "
          "repository holding zero commits, NOT an absence",
       C.grade("junjie1005/plataforma-ia-educativa-rutas-personalizadas", "LIVE-EMPTY"),
       "LIVE-COMMITLESS")
check(17, "an address that does not answer is an ABSENCE, which is p372's question not this "
          "module's — it is never promoted to a repository",
       C.grade("apereo/openlrs", "ABSENT"), "ABSENT-ADDRESS")
check(18, "this base's own planted controls are not findings and must not inflate the "
          "absence count",
       C.grade("gmilano/definitely-not-a-repo-156", "ABSENT"), "OWN-NEGATIVE-CONTROL")
check(19, "the z-prefixed control shape, which this instrument's FIRST draft missed",
       C.grade("zzzznotarealowner/zzzznotarealrepo", "ABSENT"), "OWN-NEGATIVE-CONTROL")
check(20, "a negative control that is LIVE would be a defect in the control, not a class — "
          "liveness still wins over the control pattern",
       C.grade("nope-but-live/x", "LIVE"), "LIVE-ADDRESS")

# ── group 4: limb 3 — the invariant that forbids the defect recurring ───────────────────
sv = shelves()
if all(os.path.exists(p) for p in sv):
    addresses, rejected, harvested_u, b_survivors = C.union_harvest(sv)
    unaccounted = len(b_survivors) - len(b_survivors & addresses) - sum(
        1 for a in b_survivors if a in rejected)
    check(21, "limb 3: EVERY channel-B survivor is accounted for by the census — counted as "
              "an address or named in a rejection class.  This count was 756 before p375",
           unaccounted, 0)
    p351 = C._p351()
    u_addresses, _u_rej = p351.partition(p351.harvest(sv))
    check(22, "the union is a SUPERSET of the channel-U addresses it replaces: no address the "
              "published census already counted is lost",
           sorted(set(u_addresses) - set(addresses) - set(rejected)), [])
    check(23, "and it is strictly larger, which is the defect being real rather than cosmetic",
           len(addresses) > len(u_addresses), True)
    check(24, "the two new rejection classes both fire on the live shelves, so neither arm is "
              "dead code carried for a fixture",
           sorted({c for c in rejected.values()
                   if c in ("NAME-REF-OR-PATH", "NAME-DOT-RUN")}),
           ["NAME-DOT-RUN", "NAME-REF-OR-PATH"])

# ── group 5: P541 — an instrument that takes its population by argument refuses an empty one
def run(args):
    return subprocess.run([sys.executable, "-I",
                           os.path.join(HERE, "census_union.py")] + args,
                          capture_output=True, text=True).returncode


check(25, "P541: a census over no files refuses rather than publishing a denominator of zero",
       run(["census"]), 2)
check(26, "P541: a grade over an empty adjudication file refuses", run(["grade"]), 2)
empty = tempfile.NamedTemporaryFile("w", suffix=".tsv", delete=False)
empty.close()
check(27, "P541: and an adjudication file with no rows is the same refusal",
       run(["grade", empty.name]), 2)
os.unlink(empty.name)

# ── report ──────────────────────────────────────────────────────────────────────────────
print(f"── p375-census-union ({N} controls over 5 groups: both one-sided arms with the "
      f"strings that prompted them, the two LIVE `*/skills` repositories that refute the "
      f"blanket fix, the committed 756-row derivation re-read rather than restated, p372's "
      f"three liveness classes, limb 3's unaccounted-survivor invariant, and the P541 "
      f"refusals)")
if FAILED:
    print("   FAIL")
    for f in FAILED:
        print(f)
    sys.exit(1)
print("   PASS")
