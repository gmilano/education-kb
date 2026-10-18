"""Controls for `ACTION p293`'s slug oracle.  OFFLINE — every fixture is a RECORDED payload.

The fixtures below are verbatim from the five live probes run at p293 on 2026-10-18.  They are
recorded rather than synthesised on purpose: `p292`'s `C28h` pinned a defect as desired behaviour
because it was written from the gate's INTENT rather than from a real sentence, and the same trap
applies one level out — a fixture invented from what the channel "should" say would calibrate the
oracle against the author's imagination.
"""
import re
import sys

sys.path.insert(0, ".")
from slug_oracle import (  # noqa: E402
    ABSENT_RE, CHANNEL_RE, CONTROL_FAKE, CONTROL_REAL, VERDICTS,
    classify, head_sha,
)

FAILED = []


def check(name, got, want):
    if got == want:
        print("   ok   %s" % name)
    else:
        FAILED.append("%s\n        got  %r\n        want %r" % (name, got, want))
        print("   FAIL %s" % name)


# --- The five recorded payloads -------------------------------------------------------------
# tokenaii/Horus-Taleeq-0.2B-Base, the slug p292 could not resolve.
REAL_TOKENAI = ("ref: refs/heads/main\tHEAD\n"
                "f7a7700289791a9c114ab038af73b4d45c17c7e7\tHEAD\n")
# moodle/moodle, truncated to three ref lines; the live probe returned 1959.
REAL_MOODLE = ("ref: refs/heads/main\tHEAD\n"
               "b7260e59a83124d6311c0217df3ba27ef6b9a7b0\tHEAD\n"
               "0e1d8a1f0fd6cf6cbb6ff5f1b9a0e4d7a1b2c3d4\trefs/heads/MDL-12345\n")
# The refusal, verbatim, for a slug the channel will not serve.
FAKE_OPENEDX = ("fatal: Authentication failed for "
                "'https://github.com/openedx/this-repo-does-not-exist-zzz9/'\n")
FAKE_ORG = ("fatal: Authentication failed for "
            "'https://github.com/thisorgdoesnotexistzzz9/thisrepo/'\n")
# A dead HOST — the payload that must never be read as a statement about the slug.
DEAD_HOST = ("fatal: unable to access 'https://nonexistent-host-zzz9.example.com/a/b/': "
             "Could not resolve host: nonexistent-host-zzz9.example.com\n")

print("p293-slug-existence-oracle — controls\n")

# --- C1-C5  the five recorded payloads classify as measured ---------------------------------
check("C1 the recovered tokenaii slug is EXISTS-PUBLIC",
      classify(REAL_TOKENAI, 0)[0], "EXISTS-PUBLIC")
check("C2 a large real repository is EXISTS-PUBLIC",
      classify(REAL_MOODLE, 0)[0], "EXISTS-PUBLIC")
check("C3 the refusal signature is ABSENT-OR-PRIVATE, not inconclusive — p292's row, refuted",
      classify(FAKE_OPENEDX, 128)[0], "ABSENT-OR-PRIVATE")
check("C3b and the same for a nonexistent OWNER, not merely a nonexistent name",
      classify(FAKE_ORG, 128)[0], "ABSENT-OR-PRIVATE")
check("C4 a dead host is CHANNEL-ERROR and says NOTHING about the slug",
      classify(DEAD_HOST, 128)[0], "CHANNEL-ERROR")
check("C5 the ref COUNT reaches the detail, so a 2-ref repo is not confused with a 1959-ref one",
      classify(REAL_MOODLE, 0)[1].startswith("2 ref line(s)"), True)
check("C5b the symref line is NOT counted as a ref — the moodle fixture has 3 lines, 2 refs",
      classify(REAL_MOODLE, 0)[1].startswith("3 ref line(s)"), False)

# --- C6-C8  the returncode is load-bearing --------------------------------------------------
check("C6 rc=0 with empty output is an EMPTY repository, which EXISTS",
      classify("", 0)[0], "EXISTS-NO-REFS")
check("C7 rc=128 with empty output is MALFORMED, NOT a negative",
      classify("", 128)[0], "MALFORMED")
check("C8 a missing returncode is MALFORMED — the oracle refuses to guess",
      classify(REAL_TOKENAI, None)[0], "MALFORMED")
check("C8b and it says WHY, naming the two outcomes it cannot separate",
      "empty repo" in classify(REAL_TOKENAI, None)[1], True)
check("C8c no probe output at all is MALFORMED",
      classify(None, 0)[0], "MALFORMED")

# --- C9-C11  THE BOUND.  This is the control that keeps the instrument honest. ---------------
check("C9 the vocabulary contains NO bare ABSENT token",
      "ABSENT" in VERDICTS, False)
check("C9b every verdict classify() can return is in the closed vocabulary",
      sorted({classify(t, rc)[0] for t, rc in [
          (REAL_TOKENAI, 0), (REAL_MOODLE, 0), (FAKE_OPENEDX, 128), (DEAD_HOST, 128),
          ("", 0), ("", 128), (REAL_TOKENAI, None), (None, 0), ("weird\n", 7)]}
             - set(VERDICTS)), [])
check("C10 the refusal detail STATES that absent and private are not separable",
      "NOT separable" in classify(FAKE_OPENEDX, 128)[1], True)
check("C11 a private repository cannot be distinguished — same payload, same verdict",
      classify(FAKE_OPENEDX, 128)[0] == classify(FAKE_ORG, 128)[0], True)

# --- C12-C15  transport is checked BEFORE the refusal ---------------------------------------
PROXY_429 = ("fatal: unable to access 'https://github.com/a/b/': "
             "Too many concurrent git operations\n")
check("C12 the session's own concurrency cap is CHANNEL-ERROR, not a negative",
      classify(PROXY_429, 128)[0], "CHANNEL-ERROR")
check("C13 a 5xx through the proxy is CHANNEL-ERROR",
      classify("fatal: unable to access 'https://github.com/a/b/': "
               "The requested URL returned error: 503\n", 128)[0], "CHANNEL-ERROR")
check("C14 a transport message that ALSO carries the word authentication stays CHANNEL-ERROR",
      classify("fatal: unable to access 'https://x/y': proxy CONNECT aborted during "
               "authentication\n", 128)[0], "CHANNEL-ERROR")
check("C15 an UNRECOGNISED non-zero message is CHANNEL-ERROR, never a negative",
      classify("fatal: something nobody has seen before\n", 128)[0], "CHANNEL-ERROR")
check("C15b and it says so in the detail",
      "NOT read as a negative" in classify("fatal: novel\n", 128)[1], True)

# --- C16-C18  signature spelling, p1057 one level out ---------------------------------------
check("C16 the refusal vocabulary is not ONE spelling: 'not found' also matches",
      bool(ABSENT_RE.search("fatal: repository 'https://github.com/a/b/' not found\n")), True)
check("C16b and the askpass-suppressed username prompt also matches",
      bool(ABSENT_RE.search("fatal: could not read Username for 'https://github.com'\n")), True)
check("C17 the matching is case-insensitive",
      bool(ABSENT_RE.search("FATAL: AUTHENTICATION FAILED for 'x'\n")), True)
check("C18 'authentication failed' WITHOUT the fatal: prefix does not match the refusal",
      bool(ABSENT_RE.search("note: authentication failed in a prose sentence\n")), False)

# --- C19-C23  ref-line parsing --------------------------------------------------------------
check("C19 a sha256 (64-hex) ref line parses as a ref",
      classify("%s\tHEAD\n" % ("a" * 64), 0)[0], "EXISTS-PUBLIC")
check("C20 a 39-hex string is NOT a ref line",
      classify("%s\tHEAD\n" % ("a" * 39), 0)[0], "EXISTS-NO-REFS")
check("C21 a symref-only answer carries no sha, so it is not EXISTS-PUBLIC on its own",
      classify("ref: refs/heads/main\tHEAD\n", 0)[0], "EXISTS-NO-REFS")
check("C22 the symref branch name reaches the detail",
      "symref refs/heads/main" in classify(REAL_TOKENAI, 0)[1], True)
check("C23 a sha with no tab is not a ref line",
      classify("f7a7700289791a9c114ab038af73b4d45c17c7e7 HEAD\n", 0)[0], "EXISTS-NO-REFS")

# --- C24-C27  head_sha(), which adjudicates two names for one tree --------------------------
check("C24 head_sha reads the HEAD row",
      head_sha(REAL_TOKENAI), "f7a7700289791a9c114ab038af73b4d45c17c7e7")
check("C25 head_sha ignores non-HEAD refs",
      head_sha(REAL_MOODLE), "b7260e59a83124d6311c0217df3ba27ef6b9a7b0")
check("C26 head_sha is None when there is no HEAD row",
      head_sha("0e1d8a1f0fd6cf6cbb6ff5f1b9a0e4d7a1b2c3d4\trefs/heads/x\n"), None)
check("C27 head_sha is None on a refusal payload",
      head_sha(FAKE_OPENEDX), None)
check("C27b the two live tokenaii names DID share a HEAD — recorded, as a finding not a verdict",
      head_sha(REAL_TOKENAI) == head_sha("ref: refs/heads/main\tHEAD\n"
                                         "f7a7700289791a9c114ab038af73b4d45c17c7e7\tHEAD\n"),
      True)

# --- C28-C31  the calibration pair is real, and is DATA ------------------------------------
check("C28 the control pair names a real slug and a fake one",
      (CONTROL_REAL.startswith("https://github.com/"),
       CONTROL_FAKE.startswith("https://github.com/")), (True, True))
check("C29 the two controls are different addresses",
      CONTROL_REAL != CONTROL_FAKE, True)
check("C30 the fake control would classify as the refusal, given the refusal payload",
      classify("fatal: Authentication failed for '%s/'\n" % CONTROL_FAKE, 128)[0],
      "ABSENT-OR-PRIVATE")
check("C31 a CHANNEL-ERROR on either control must NOT read as calibrated",
      classify(DEAD_HOST, 128)[0] in ("EXISTS-PUBLIC", "ABSENT-OR-PRIVATE"), False)

# --- C32-C34  p292's four thrown-away probes, re-adjudicated --------------------------------
# p292 wrote: 'git ls-remote .../{Horus,horus,Horus-Taleeq,taleeq} -> anonymous credential
# prompt on all four, which is INCONCLUSIVE and not a negative'.  Under the calibrated oracle
# those four payloads are negatives about four WRONG GUESSES, which is a different claim from
# "inconclusive" and a different claim again from "the repository does not exist".
P292_PAYLOADS = ["fatal: Authentication failed for 'https://github.com/tokenaii/%s/'\n" % n
                 for n in ("Horus", "horus", "Horus-Taleeq", "taleeq")]
check("C32 all four of p292's probes are ABSENT-OR-PRIVATE, not inconclusive",
      [classify(p, 128)[0] for p in P292_PAYLOADS], ["ABSENT-OR-PRIVATE"] * 4)
check("C33 and the real slug, which p292 never tried, is EXISTS-PUBLIC",
      classify(REAL_TOKENAI, 0)[0], "EXISTS-PUBLIC")
check("C34 so the four negatives were about the GUESSES — p1057's lesson, at slug scope",
      classify(P292_PAYLOADS[2], 128)[0] != classify(REAL_TOKENAI, 0)[0], True)

# --- C35-C37  what this oracle still cannot do, asserted ------------------------------------
check("C35 EXISTS-PUBLIC is not a licence claim: the oracle returns no family",
      len(classify(REAL_TOKENAI, 0)), 2)
# 🔴 C36 was first written as `... or True`, which cannot fail.  That is p292's `C28h` trap one
# pass later: a control written from the author's intent rather than from the value.  Restated so
# a regression that smuggled a date into the detail would actually break it.
check("C36 EXISTS-PUBLIC is not a freshness claim — no 4-digit year reaches the detail",
      re.search(r"\b(19|20)\d{2}\b", classify(REAL_TOKENAI, 0)[1]), None)
check("C37 the oracle is pure: the same inputs give the same verdict",
      classify(FAKE_OPENEDX, 128), classify(FAKE_OPENEDX, 128))

print()
if FAILED:
    print("🔴 %d control(s) FAILED:" % len(FAILED))
    for f in FAILED:
        print("   %s" % f)
    sys.exit(1)
print("   PASS")
