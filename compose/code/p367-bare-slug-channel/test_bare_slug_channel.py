#!/usr/bin/env python3
"""Offline controls for `p367-bare-slug-channel` — `gate-bare-slug-channel`.

🔵 Every control is a string, not a network call: the online leg's correctness is
`probe_slugs.sh`'s business and is measured by its survivor precision and its
false-rejection sample, not asserted here.
"""
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bare_slug_channel as B  # noqa: E402

FAILED = []
N = 0


def check(num, what, got, want):
    global N
    N += 1
    if got != want:
        FAILED.append(f"🔴 {num}. {what}\n     got:  {got!r}\n     want: {want!r}")


def shelf(text):
    fh = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8")
    fh.write(text)
    fh.close()
    return fh.name


def only_b(text):
    p = shelf(text)
    try:
        u = B.channel_u([p])
        surv, rej = B.channel_b([p])
        return sorted(a for a in surv if a not in u), rej
    finally:
        os.unlink(p)


# ── the defect this instrument exists for ────────────────────────────────────
check(1, "ZZ-bv's specimen: a bare backticked slug is FOUND by channel B",
      only_b("the subject of `Gap 264` is `CAHLR/OATutor-Content`, ungranted")[0],
      ["cahlr/oatutor-content"])
check(2, "and it is INVISIBLE to the URL channel, which is the whole defect",
      list(B.channel_u([shelf("`CAHLR/OATutor-Content`")])), [])
check(3, "an address already held as a URL is not reported as channel-B-only",
      only_b("https://github.com/HKUDS/DeepTutor and also `HKUDS/DeepTutor`")[0], [])

# ── the four arms, each with the specimen that prompted it ───────────────────
check(4, "arm 1: a shelf path is not an address (`agents/top.md`, 504 occurrences)",
      B.classify_b("agents/top.md"), "REF-OR-PATH-SEGMENT")
check(5, "arm 1: a grant rung is not an address (`main/license`, 483 occurrences)",
      B.classify_b("main/license"), "REF-OR-PATH-SEGMENT")
check(6, "arm 2: a second segment that is a FILE is not a repository name",
      B.classify_b("openedx/__init__.py"), "DOC-PATH")
check(7, "arm 3: a ratio is not an address (`47/47`)",
      B.classify_b("47/47"), "NUMERIC-PAIR")
check(8, "arm 3: a date-shaped pair is not an address (`2026/1744`)",
      B.classify_b("2026/1744"), "NUMERIC-PAIR")
check(9, "arm 4: a licence pair is shaped exactly like an address",
      B.classify_b("mit/apache-2.0"), "GRANT-ID-PAIR")
check(10, "a real address survives all four arms", B.classify_b("hkuds/deeptutor"), None)

# 🔴 Arm 2 must NOT eat a repository that is legitimately named with a dot.
check(11, "a dotted repository name is not a DOC-PATH (`socket.io`)",
      B.classify_b("socketio/socket.io"), None)

# ── p351 is the owner of shape, and is NOT reimplemented here ────────────────
check(12, "p351 still rejects a nav namespace, through this channel",
      only_b("see `topics/ai-tutor` for the tag")[0], [])
check(13, "p351 still rejects a placeholder owner, through this channel",
      only_b("clone `yourusername/SUMRY` to start")[0], [])
check(14, "p351's class name is reported, not re-labelled by p367",
      only_b("`topics/ai-tutor`")[1].get("topics/ai-tutor"), "NAV-NAMESPACE")

# ── the `.git` fold: p367's own first-draft defect ───────────────────────────
# 🔴 The first draft did not strip `.git`, which put 7 spelling artefacts into the
# live population and 7 false rows into the sha-collision table.
check(15, "`.git` folds to the bare address", B.fold("cvmcosta/ltijs.git"), "cvmcosta/ltijs")
check(16, "a `.git` spelling does not become a SECOND address",
      only_b("`cvmcosta/ltijs.git` and https://github.com/cvmcosta/ltijs")[0], [])

# ── the backtick is load-bearing ─────────────────────────────────────────────
check(17, "unticked prose is NOT harvested — an English pair is not an address",
      only_b("the split is pass/fail and spanish/portuguese")[0], [])
check(18, "a ticked token with two slashes is not a one-slash address",
      only_b("`refs/heads/main`")[0], [])

# ── the empty-input contract (P541) ──────────────────────────────────────────
check(19, "census over no files REFUSES rather than publishing a corpus of zero",
      B.main(["census"]), 2)
check(20, "candidates over no files REFUSES", B.main(["candidates"]), 2)

# ── de-duplication ───────────────────────────────────────────────────────────
check(21, "one address named nine times is one address",
      only_b(" ".join(["`weiwei0614/math-bank`"] * 9))[0], ["weiwei0614/math-bank"])
check(22, "case variants fold to one address",
      only_b("`Weiwei0614/Math-Bank` and `weiwei0614/math-bank`")[0],
      ["weiwei0614/math-bank"])

print(f"{N - len(FAILED)}/{N} controls pass")
for f in FAILED:
    print(f)
sys.exit(1 if FAILED else 0)
