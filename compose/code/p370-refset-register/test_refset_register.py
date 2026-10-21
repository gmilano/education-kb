"""p370 tests. Every fixture is VERBATIM `git ls-remote --symref` output captured on
2026-10-21 and committed under ./refsets/. No invented ref sets."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from refset_register import (parse_ls_remote, ref_names, fingerprint, head_sha,
                             classify, register_verdict, STALE_IS_SOUND)

HERE = os.path.dirname(os.path.abspath(__file__))
REFS = os.path.join(HERE, "refsets")


def cap(addr):
    with open(os.path.join(REFS, addr.replace("/", "%") + ".refs"),
              encoding="utf-8", errors="replace") as fh:
        return parse_ls_remote(fh.read())


# --- the pair that turned the gate red -------------------------------------------
DYMAYO = cap("dymayo/moodler-mcp")
GHAITH = cap("GhaithAlHallak8/moodler-mcp")
# --- the pair whose PULL REF proves the direction of the relationship ------------
ROHAN = cap("rohanmuppa/purdue-mcp")
SHARZIKI = cap("sharziki/purdue-mcp")
# --- a TRUE alias: an org rename, ref sets byte-identical ------------------------
STANFORD = cap("stanfordnlp/edu-convokit")
EDUNLP = cap("EduNLP/edu-convokit")

fails = []
_CALLS = 0


def check(name, got, want):
    global _CALLS
    _CALLS += 1
    if got != want:
        fails.append("%s: got %r, want %r" % (name, got, want))


# --- parsing ---------------------------------------------------------------------
check("the symref line is not a ref", "ref: refs/heads/main" in DYMAYO, False)
check("HEAD is parsed", head_sha(DYMAYO), "4e6139eb9c6bab760fbd64eb7fe94459e5e79ffb")
check("empty text parses to nothing", parse_ls_remote(""), {})
check("None parses to nothing", parse_ls_remote(None), {})

# --- HEAD carries no identity: it is excluded from the fingerprint ---------------
check("HEAD excluded from the name set", "HEAD" in ref_names(DYMAYO), False)
check("an empty ref set has the empty fingerprint", fingerprint({}), "")

# --- the finding: identical HEAD, different ref sets ----------------------------
check("the moodler-mcp pair agrees on HEAD", head_sha(DYMAYO), head_sha(GHAITH))
check("and disagrees on the ref set", fingerprint(DYMAYO) == fingerprint(GHAITH), False)
check("moodler-mcp is SAME-HEAD-ONLY", classify(DYMAYO, GHAITH), "SAME-HEAD-ONLY")
check("the fork side carries 2 refs", len(ref_names(DYMAYO)), 2)
check("the parent side carries 62 refs", len(ref_names(GHAITH)), 62)
check("so the register's STALE row is demoted",
      register_verdict(classify(DYMAYO, GHAITH), "STALE")[0], "DEMOTE")

# --- the pull ref: the relationship has a DIRECTION, and it is the opposite one --
# `rohanmuppa/purdue-mcp` was registered as a STALE address OF `sharziki/purdue-mcp`.
# sharziki's `refs/pull/1/head` IS rohanmuppa's `fix/current-term-default` tip, so
# rohanmuppa is the repository that opened a pull request against sharziki. Two
# repositories in a contributor relationship cannot be one address and its redirect.
check("rohanmuppa's branch tip is sharziki's pull-1 head",
      ROHAN["refs/heads/fix/current-term-default"], SHARZIKI["refs/pull/1/head"])
check("purdue-mcp is SAME-HEAD-ONLY", classify(ROHAN, SHARZIKI), "SAME-HEAD-ONLY")
check("purdue-mcp's STALE row is demoted",
      register_verdict(classify(ROHAN, SHARZIKI), "STALE")[0], "DEMOTE")

# --- the positive control: a real rename must still pass -------------------------
check("edu-convokit ref sets are identical",
      fingerprint(STANFORD), fingerprint(EDUNLP))
check("edu-convokit is SAME-REF-SET", classify(STANFORD, EDUNLP), "SAME-REF-SET")
check("so its STALE row is KEPT",
      register_verdict(classify(STANFORD, EDUNLP), "STALE")[0], "KEEP")
check("SAME-REF-SET is the ONLY sound ground for STALE",
      STALE_IS_SOUND, ("SAME-REF-SET",))

# --- the verdicts that must not be guessed --------------------------------------
check("a dead side yields no verdict", classify({}, GHAITH), "ONE-SIDE-DEAD")
check("a dead side yields UNPROVEN, never a demotion",
      register_verdict("ONE-SIDE-DEAD", "STALE")[0], "UNPROVEN")
check("both dead is still ONE-SIDE-DEAD", classify({}, {}), "ONE-SIDE-DEAD")
check("a CANONICAL row is not this instrument's business",
      register_verdict("SAME-HEAD-ONLY", "CANONICAL")[0], "KEEP")
check("an UNKNOWN row is not demoted either",
      register_verdict("DIFFERENT-HEAD", "UNKNOWN")[0], "KEEP")
check("a missing state is not a STALE row",
      register_verdict("SAME-HEAD-ONLY", "")[0], "KEEP")

# --- fingerprint properties ------------------------------------------------------
check("the fingerprint ignores ref ORDER",
      fingerprint({"refs/heads/a": "1", "refs/heads/b": "2"}),
      fingerprint({"refs/heads/b": "2", "refs/heads/a": "1"}))
check("the fingerprint ignores SHAS — names only",
      fingerprint({"refs/heads/a": "1"}), fingerprint({"refs/heads/a": "ffff"}))
check("the fingerprint does NOT ignore a missing ref",
      fingerprint({"refs/heads/a": "1"}) == fingerprint({"refs/heads/a": "1",
                                                         "refs/heads/b": "1"}), False)
check("refs/pull is KEPT — it is the fork discriminator",
      any(n.startswith("refs/pull/") for n in ref_names(SHARZIKI)), True)
check("a HEAD-only remote fingerprints as empty",
      fingerprint({"HEAD": "abc"}), "")
check("DIFFERENT-HEAD when neither channel agrees",
      classify({"refs/heads/a": "1", "HEAD": "1"},
               {"refs/heads/b": "2", "HEAD": "2"}), "DIFFERENT-HEAD")

# --- P541: the module must refuse to invent ------------------------------------
check("a verdict this instrument does not know is UNPROVEN, not KEEP",
      register_verdict("NO-CANONICAL", "STALE")[0], "UNPROVEN")

TOTAL = 32  # the number of check() calls above; asserted so a silently skipped
            # control cannot be mistaken for a green suite (p277's rule).
if _CALLS != TOTAL:
    print("🔴 p370-refset-register: %d controls ran, %d declared" % (_CALLS, TOTAL))
    sys.exit(1)
if fails:
    print("🔴 p370-refset-register FAILED %d of %d controls" % (len(fails), TOTAL))
    for f in fails:
        print("   " + f)
    sys.exit(1)
print("🟢 p370-refset-register PASS %d/%d — a HEAD sha is not an identity proof"
      % (TOTAL, TOTAL))
