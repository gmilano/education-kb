"""Offline controls for `ACTION ZZ-bo`'s companion extractor.

🔵 Every control below is a shape this instrument MET on real payloads in `p364`, not an
invented case.  The two NAV rungs (`user-attachments`, `activities`) are holes this sweep
found in `p351-address-shape` and closed; control 14 pins the hole it deliberately did NOT
close, so a successor meets it as a fixture rather than as a surprise.
"""
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from companion_closure import (extract_companions, fold,  # noqa: E402
                                README_LADDER, resolve_readme)


def _shape():
    path = os.path.join(HERE, "..", "p351-address-shape", "address_shape.py")
    spec = importlib.util.spec_from_file_location("p351_address_shape", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


SHAPE = _shape()
FAILED = []


def check(n, label, got, want):
    if got != want:
        FAILED.append("%2d %s\n     got  %r\n     want %r" % (n, label, got, want))
        print("   🔴 %2d %s" % (n, label))
    else:
        print("   🟢 %2d %s" % (n, label))


def comps(text, slug):
    return extract_companions(text, slug, shape=SHAPE)


SELF = "QingdaoU/OnlineJudge"

check(1, "the row itself is not its own companion",
      comps("https://github.com/QingdaoU/OnlineJudge", SELF), [])

check(2, "self is excluded under a DIFFERENT CASING (ZZ-x's rule at source)",
      comps("https://github.com/qingdaou/onlinejudge", SELF), [])

check(3, "self reached by a SUB-PATH is still self, never a companion",
      comps("https://github.com/QingdaoU/OnlineJudge/issues/1", SELF), [])

check(4, "a `.git` clone suffix folds onto the bare address",
      comps("https://github.com/QingdaoU/Judger.git", SELF),
      [("qingdaou/judger", "SAME-OWNER")])

check(5, "a badge image path does not invent a repository named `x.svg`",
      comps("https://github.com/QingdaoU/Judger/workflows/ci/badge.svg", SELF),
      [("qingdaou/judger", "SAME-OWNER")])

check(6, "p351's NAV namespace still rejects `marketplace`",
      comps("https://github.com/marketplace/actions/checkout", SELF), [])

check(7, "🆕 p364: `user-attachments` is GitHub's attachment CDN, not an owner",
      comps("https://github.com/user-attachments/assets/abc-123", SELF), [])

check(8, "🆕 p364: `activities` is a github.com page, not an owner",
      comps("https://github.com/activities/contributing-to-open-source", SELF), [])

check(9, "SAME-OWNER is decided on the FOLDED owner, so casing cannot split it",
      comps("https://github.com/QINGDAOU/JudgeServer", SELF),
      [("qingdaou/judgeserver", "SAME-OWNER")])

check(10, "a different owner is THIRD-PARTY and is kept, not dropped",
       comps("https://github.com/ioi/isolate", SELF),
       [("ioi/isolate", "THIRD-PARTY")])

check(11, "one component named nine times is ONE companion",
       comps(" ".join(["https://github.com/QingdaoU/Judger"] * 9), SELF),
       [("qingdaou/judger", "SAME-OWNER")])

check(12, "an empty README is no companions rather than a crash",
       comps("", SELF), [])
check(13, "a None README is no companions rather than a crash",
       comps(None, SELF), [])

# 🟢 p362's own specimen, which is the reason this instrument exists.
check(14, "the p362 OnlineJudge specimen returns both execution components",
       comps("""Judge server: https://github.com/QingdaoU/JudgeServer
                Sandbox: https://github.com/QingdaoU/Judger
                Deploy: https://github.com/QingdaoU/OnlineJudgeDeploy""", SELF),
       [("qingdaou/judger", "SAME-OWNER"),
        ("qingdaou/judgeserver", "SAME-OWNER"),
        ("qingdaou/onlinejudgedeploy", "SAME-OWNER")])

# 🔴 THE HOLE THIS PASS DID NOT CLOSE, pinned so it cannot change in silence.
#
# `github.com/en/get-started` is a LOCALE-PREFIXED docs path and it survives the shape
# filter, because a two-letter first segment is indistinguishable BY SHAPE from a short
# legitimate owner.  Adding `en` to NAV_NAMESPACES would reject any real owner called
# `en`, so the rejection is left to the `ls-remote` channel, which answered NO-REF for it
# in this pass.  🟡 This control asserts the CURRENT behaviour, not the desired one.
check(15, "KNOWN HOLE pinned: a locale docs path is NOT rejected by shape alone",
       comps("https://github.com/en/get-started/quickstart", SELF),
       [("en/get-started", "THIRD-PARTY")])

check(16, "fold strips `.git` and lowercases both halves",
       fold("QingdaoU", "Judger.git"), "qingdaou/judger")

# 🟢 The README ladder p283's audit demanded, exercised rather than merely declared.
import tempfile  # noqa: E402

with tempfile.TemporaryDirectory() as d:
    check(17, "an EMPTY directory is a real absence, not a spelling miss",
          resolve_readme(d), None)
    odd = os.path.join(d, "Readme.md")
    open(odd, "w").write("https://github.com/ioi/isolate")
    check(18, "a `Readme.md` anchor is FOUND — the spelling a one-rung ladder misses",
          resolve_readme(d), odd)
    # 🔴 This control's FIRST draft asserted `README.txt` wins and was wrong: the ladder
    # puts every markdown spelling ahead of every `.txt` one, deliberately, because a
    # project that ships both keeps its prose in the markdown file.  🟢 The control now
    # pins the ORDER the ladder actually encodes, which is the thing worth protecting.
    txt = os.path.join(d, "README.txt")
    open(txt, "w").write("x")
    check(19, "first-hit-wins: a markdown spelling outranks `README.txt`",
          os.path.basename(resolve_readme(d)), "Readme.md")

check(20, "the ladder varies stem case AND extension case",
      (any(r.startswith("README") for r in README_LADDER),
       any(r.startswith("readme") for r in README_LADDER),
       any(r.startswith("Readme") for r in README_LADDER),
       any(r.endswith(".MD") for r in README_LADDER),
       any(r.endswith(".md") for r in README_LADDER)),
      (True, True, True, True, True))

print()
if FAILED:
    print("🔴 p364-companion-closure: %d/%d controls FAILED" % (len(FAILED), 20))
    for f in FAILED:
        print("  " + f)
    sys.exit(1)
print("🟢 PASS — 20/20 controls (p364 companion extraction + the README ladder p283 demanded, ACTION ZZ-bo)")
