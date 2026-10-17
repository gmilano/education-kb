"""Controls for `ACTION XN`.  Run from this directory:

    python3 test_prefix_collision.py

Explicit non-zero exit and an asserted total, per `p251`'s own `ACTION XM`
finding: a control wired through `unittest.main()` passes while collecting
nothing.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from prefix_collision import (harvest, pair_class, collisions, refusals, flagged,
                              line_scope_collisions, published_as_url)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
passed = failed = 0

def chk(name, got, want):
    global passed, failed
    if got == want:
        passed += 1
        print("ok   %-64s" % name)
    else:
        failed += 1
        print("FAIL %-64s got=%r want=%r" % (name, got, want))

def verdicts(text):
    return {(r["short"], r["long"]): r["verdict"] for r in collisions(text)}

# ── the harvest keeps a dotted name whole (p250's repair, re-asserted here) ────
chk("dotted name survives the harvest", harvest("see `TouchRefletz/maia.edu` now"),
    ["TouchRefletz/maia.edu"])
chk("sentence-final dot is shed", harvest("at processing/p5.js."), ["processing/p5.js"])
chk("two slugs on one line", harvest("a/b and c/d."), ["a/b", "c/d"])

# ── XN's falsifier, both scopes, on the real shelf shape ──────────────────────
TABLE = ("| the real row, [`TouchRefletz/maia.edu`](https://github.com/TouchRefletz/maia.edu) | `master` |\n"
         "| the stump, [`TouchRefletz/maia`](https://github.com/TouchRefletz/maia) | `main` |\n")
chk("FILE scope FLAGS the maia stump (XN's falsifier)",
    [(r["short"], r["long"]) for r in flagged(TABLE)],
    [("TouchRefletz/maia", "TouchRefletz/maia.edu")])
chk("and p250's own wording annotates it, so the gate does not FAIL on it",
    verdicts(TABLE)[("TouchRefletz/maia", "TouchRefletz/maia.edu")], "REFUSE-ANNOTATED")
BARE = ("| [`TouchRefletz/maia.edu`](https://github.com/TouchRefletz/maia.edu) | `AGPL-3.0` |\n"
        "| [`TouchRefletz/maia`](https://github.com/TouchRefletz/maia) | `AGPL-3.0` |\n")
chk("an UNANNOTATED stump row is a REFUSAL the gate fails on",
    [(r["short"], r["long"]) for r in refusals(BARE)],
    [("TouchRefletz/maia", "TouchRefletz/maia.edu")])
chk("XN's LINE scope MISSES it (the prescription is the wrong scope)",
    [c for c in line_scope_collisions(TABLE) if c["short"] == "TouchRefletz/maia"], [])
chk("the flag names the bare line", flagged(TABLE)[0]["bare_lines"], [2])

# ── the exemption: a pass that documents a truncation writes both forms ───────
DOC = "the lint's own example `processing/p5.js` was carried as `processing/p5` for eleven passes\n"
chk("both forms on one line is DOCUMENTED, not REFUSE",
    verdicts(DOC)[("processing/p5", "processing/p5.js")], "DOCUMENTED")

# ── the false-positive population, each class measured on a real shape ────────
# the real shape on these shelves: a probe ladder written out in prose, where
# the BRANCH name occupies the slot an owner would.
PATHS = "probed `main/LICENSE`, then `main/LICENSE.md`, then `main/LICENSE.txt`\n"
chk("branch in the owner slot is a PATH FRAGMENT",
    verdicts(PATHS)[("main/LICENSE", "main/LICENSE.md")], "IGNORED-PATH-FRAGMENT")
SEP = "`moodle/moodle` and `moodle/moodle-docker`\n"
chk("a `-` continuation only WARNs", verdicts(SEP)[("moodle/moodle", "moodle/moodle-docker")], "WARN")
OWNERS = "`dmitry-viskov/pylti1.3` and `ucfopen/pylti1.3`\n"
chk("different owners are not a pair", collisions(OWNERS), [])
chk("a lone address makes no pair", collisions("`owner/repo`\n"), [])

# ── the URL test that the naive form gets wrong ───────────────────────────────
URL = "[`JushBJJ/Mr.-Ranedeer-AI-Tutor`](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor)"
chk("the long URL does not publish the stump", published_as_url("JushBJJ/Mr", URL), False)
chk("the long form IS published", published_as_url("JushBJJ/Mr.-Ranedeer-AI-Tutor", URL), True)
chk("naive substring containment would have said yes",
    ("github.com/JushBJJ/Mr" in URL), True)

# ── and the live shelves: the canonical instance must still trip ──────────────
top = os.path.join(ROOT, "agents", "top.md")
if os.path.exists(top):
    text = open(top, encoding="utf-8").read()
    rs = {(r["short"], r["long"]) for r in flagged(text)}
    # 🔴 p265: this leg pinned the PRESENCE of ("TouchRefletz/maia",
    # "TouchRefletz/maia.edu") in the live shelf.  p264 rewrote `agents/top.md` and
    # dropped that row legitimately, so the control went red on a shelf edit rather
    # than on a detector regression — a fixture masquerading as a check.
    # 🟢 The detector's capability against that exact stump is already pinned above,
    # on a FIXTURE ("FILE scope FLAGS the maia stump (XN's falsifier)").  What the
    # LIVE shelf owes is the INVARIANT: if the stump is there, it is flagged.  An
    # empty shelf passes; a shelf carrying an unflagged stump still fails.
    chk("live agents/top.md: the maia stump, if present, is flagged",
        ("TouchRefletz/maia.edu" not in text)
        or (("TouchRefletz/maia", "TouchRefletz/maia.edu") in rs), True)
    chk("and it is annotated, so the live shelf has 0 hard refusals",
        [(r["short"], r["long"]) for r in refusals(text)], [])
    chk("no PATH-FRAGMENT pair is ever flagged",
        [r for r in flagged(text) if r["short"].split("/")[0] in
         {"main", "master", "docs", "lib", "package"}], [])
else:                                            # pragma: no cover
    chk("live shelf reachable", False, True)
    chk("live shelf reachable", False, True)

chk("control total", passed + failed, 19)
print("\n%d/%d passed" % (passed, passed + failed))
sys.exit(1 if failed else 0)
