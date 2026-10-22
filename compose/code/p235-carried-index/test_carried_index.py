#!/usr/bin/env python3
"""p235 — offline controls for the carried index. No network, no shelves required:
every case is built from fixtures in a temp dir, so this runs in a hook and in a
sandbox without egress."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import carried_index as ci  # noqa: E402

FAILED = []


def check(name, got, want):
    if got != want:
        FAILED.append(f"{name}: got {got!r}, want {want!r}")


def shelf_dir(files):
    d = tempfile.mkdtemp()
    for rel, body in files.items():
        path = os.path.join(d, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(body)
    return d


# ── fold(): ACTION UH's predicate
check("fold lowers", ci.fold("OpenOLAT/OpenOLAT"), "openolat/openolat")
check("fold strips trailing period", ci.fold("a/b."), "a/b")
check("fold strips trailing comma", ci.fold("a/b,"), "a/b")
check("fold strips trailing paren", ci.fold("a/b)"), "a/b")
check("fold is idempotent", ci.fold(ci.fold("A/B.")), "a/b")

# ── the collision p234 actually tripped over
d = shelf_dir({"README.md": "see https://github.com/OpenOLAT/OpenOLAT and "
                            "https://github.com/openolat/OpenOLAT today"})
idx = ci.harvest(d)
check("case variants collapse to one row", len(idx), 1)
check("collision is reported", list(ci.collisions(idx)), ["openolat/openolat"])
check("both spellings retained", len(ci.collisions(idx)["openolat/openolat"]), 2)
check("carried() is case-blind", ci.carried("OPENOLAT/OPENOLAT", idx), True)
check("carried() rejects a non-row", ci.carried("acme/nope", idx), False)

# ── a single spelling is not a collision
d = shelf_dir({"README.md": "https://github.com/a/b https://github.com/a/b"})
idx = ci.harvest(d)
check("one spelling twice is not a collision", ci.collisions(idx), {})
check("but it is carried", ci.carried("a/b", idx), True)

# ── shelves only: evidence/ and archive/ are NOT the shelves
d = shelf_dir({
    "README.md": "nothing here",
    "evidence/x.tsv": "https://github.com/ghost/row",
    "archive/old/agents-top.md": "https://github.com/archived/row",
})
idx = ci.harvest(d)
check("evidence is not a shelf", ci.carried("ghost/row", idx), False)
check("archive is not a shelf", ci.carried("archived/row", idx), False)

# ── a missing shelf must not be fatal (partial checkout)
d = shelf_dir({"README.md": "https://github.com/only/one"})
check("missing shelves are skipped", len(ci.harvest(d)), 1)

# ── claims(): the predicate that would have stopped the nine-pass LMS error
#    and this pass's LATAM-zero error
d = shelf_dir({
    "README.md": "LATAM: 0 open-source education repositories",
    "verticals/solutions.md": "portabilis/i-educar is the largest in Brazil",
    "intel/market.md": "i-educar again",
})
hits = ci.claims("i-educar", d)
check("claims finds the token on 2 shelves", sorted(hits), ["intel/market.md",
                                                           "verticals/solutions.md"])
check("claims counts occurrences", hits["intel/market.md"], 1)
check("claims is case-insensitive", "verticals/solutions.md" in ci.claims("I-EDUCAR", d), True)
check("claims is empty for a real absence", ci.claims("zzz-no-such-token", d), {})

# ── the URL shapes the shelves actually use
d = shelf_dir({"README.md": (
    "[`a/b`](https://github.com/a/b) | plain https://github.com/c/d, "
    "trailing https://github.com/e/f. and a dot-name https://github.com/g/h.js")})
idx = ci.harvest(d)
check("markdown link form", ci.carried("a/b", idx), True)
check("bare form with comma", ci.carried("c/d", idx), True)
check("bare form with period", ci.carried("e/f", idx), True)
check("dotted repo name survives", ci.carried("g/h.js", idx), True)

# ── p379: `ACTION p378-A` — the three-valued grade, and the controls that pin WHY it is
# three-valued rather than a union. Every fixture below is a real string from this base.
#
# 🔴 The specimen that registered Gap 512: p378's `make carried` graded this NEW while
# repos/trending.md already carried it as a backticked bare slug.
d = shelf_dir({
    "repos/trending.md": "a roster at `msitarzewski/agency-agents` — not education\n",
    "README.md": "linked https://github.com/HKUDS/DeepTutor is the anchor row\n",
})
check("grade: channel U still CARRIED", ci.grade("HKUDS/DeepTutor", root=d), ci.CARRIED)
check("grade: Gap 512's own specimen is MENTIONED-B",
      ci.grade("msitarzewski/agency-agents", root=d), ci.MENTIONED_B)
check("grade: a true absence is still NEW", ci.grade("acme/nope", root=d), ci.NEW)
check("grade: MENTIONED-B is case-folded", ci.grade("MSITARZEWSKI/Agency-Agents", root=d),
      ci.MENTIONED_B)

# 🟢 carried() MUST NOT MOVE. p376-A's lesson: a standing instrument that silently re-grades
# retro-edits published denominators. These two controls are the ones that fail if a
# successor "simplifies" grade() into carried().
idx = ci.harvest(d)
check("carried() unchanged: channel-B address is still NOT carried",
      ci.carried("msitarzewski/agency-agents", idx), False)
check("carried() unchanged: channel-U address is still carried",
      ci.carried("hkuds/deeptutor", idx), True)

# 🔴 THE REASON FOR THE THIRD VALUE, pinned as a control. These two addresses appear on
# agents/top.md inside a DEAD-CITATION sweep, written as bare slugs because the pass was
# reporting a negative. Both answered rc=128 first-hand at p379. A union into carried()
# would have reported them as rows this base carries.
d2 = shelf_dir({"agents/top.md": (
    "dead addresses: `concentricsky/badgr-server`, `1EdTech/badgr-server` — both rc=128\n")})
check("adjudicated-dead slug grades MENTIONED-B, not CARRIED",
      ci.grade("1EdTech/badgr-server", root=d2), ci.MENTIONED_B)
check("adjudicated-dead slug is NOT carried()",
      ci.carried("1EdTech/badgr-server", ci.harvest(d2)), False)

# 🔵 Channel B's over-collection must not reach grade() as an address. p351's shape filter
# and p367's four arms own this; these controls prove grade() inherits them rather than
# re-deciding. `main/LICENSE` is a grant rung, `47/47` a ratio, `agents/top.md` a shelf path.
d3 = shelf_dir({"README.md": "grant at `main/LICENSE`, ratio `47/47`, shelf `agents/top.md`\n"})
check("grant rung is not an address", ci.grade("main/LICENSE", root=d3), ci.NEW)
check("ratio is not an address", ci.grade("47/47", root=d3), ci.NEW)
check("shelf path is not an address", ci.grade("agents/top.md", root=d3), ci.NEW)

# 🟢 An unticked prose slug stays invisible, which is p367's documented limit and not a bug:
# unticked `owner/repo` cannot be told from an English word pair by any honest rule.
d4 = shelf_dir({"README.md": "we looked at acme/widget yesterday\n"})
check("unticked prose slug is NOT channel B", ci.grade("acme/widget", root=d4), ci.NEW)

# 🔴 DEGRADATION ARM: if p367 is unavailable, channel B must be EMPTY and grade() must
# collapse to carried()'s two values — never guess a channel. Pinned by pointing the module
# constant at a path that does not exist.
_saved = ci._B_MODULE
try:
    ci._B_MODULE = "/nonexistent/p379/bare_slug_channel.py"
    check("degraded: harvest_b is empty, not guessed", ci.harvest_b(d), set())
    check("degraded: grade falls back to NEW, not MENTIONED-B",
          ci.grade("msitarzewski/agency-agents", root=d), ci.NEW)
    check("degraded: channel U is unaffected", ci.grade("HKUDS/DeepTutor", root=d), ci.CARRIED)
finally:
    ci._B_MODULE = _saved
check("degradation arm restored the module path", ci.harvest_b(d) != set(), True)

# 🔵 The three values are distinct strings, so `if grade(...)` cannot read MENTIONED-B as a
# bool the way `if carried(...)` reads True.
check("the three values are distinct", len({ci.CARRIED, ci.MENTIONED_B, ci.NEW}), 3)

# ── p379: the `.git` suffix fold. Found by running this module's census beside p367's and
# measuring the 8-address disagreement, not by reading the code.
check("fold strips .git", ci.fold("cvmcosta/ltijs.git"), "cvmcosta/ltijs")
check("fold strips .GIT case-blind", ci.fold("CVMCOSTA/Ltijs.GIT"), "cvmcosta/ltijs")
check("fold strips .git after punctuation", ci.fold("a/b.git)"), "a/b")
check("fold leaves a dotted repo NAME alone", ci.fold("g/h.js"), "g/h.js")
check("fold leaves a repo literally named git alone", ci.fold("a/git"), "a/git")
check("fold is still idempotent with the suffix arm", ci.fold(ci.fold("A/B.git")), "a/b")

# THE FALSE NEGATIVE THIS CLOSES: an address published ONLY in clone-suffix form.
d5 = shelf_dir({"README.md": "clone it: https://github.com/cvmcosta/ltijs.git\n"})
idx5 = ci.harvest(d5)
check("a .git-only address is CARRIED for its bare form", ci.carried("cvmcosta/ltijs", idx5), True)
check("one address, not two spellings", len(idx5), 1)
check("grade agrees with carried on the .git-only case",
      ci.grade("cvmcosta/ltijs", root=d5), ci.CARRIED)

if FAILED:
    print(f"FAIL ({len(FAILED)})")
    for line in FAILED:
        print("  " + line)
    sys.exit(1)
print("PASS — 23 controls + p379's 18 on the three-valued grade + 9 on the .git fold = 50")
