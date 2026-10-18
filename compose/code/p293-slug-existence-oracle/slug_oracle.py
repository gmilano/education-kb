"""`ACTION p293` — decide whether a GUESSED slug is a repository, with the channel CALIBRATED.

`p293`'s ranked item 1 was *"recover `tokenaii`'s real repository slug, then read the grant at
a pin"*.  The slug was recovered from a search leg, and the grant read `MIT` at
`f7a7700289791a9c114ab038af73b4d45c17c7e7`.  This file is the half that OUTLIVES that finding.

🔴 WHAT THIS REFUTES.  `p292` probed four guessed `tokenaii/*` slugs with `git ls-remote`, got an
anonymous credential prompt on all four, and recorded the result as *"INCONCLUSIVE and not a
negative"*.  Measured against controls, that verdict is wrong:

    known-REAL   github.com/moodle/moodle                    rc=0    1959 ref lines
    known-REAL   github.com/tokenaii/Horus-Taleeq-0.2B-Base   rc=0       2 ref lines
    known-FAKE   github.com/openedx/this-repo-does-not-...    rc=128  fatal: Authentication failed
    known-FAKE   github.com/thisorgdoesnotexistzzz9/thisrepo  rc=128  fatal: Authentication failed
    dead HOST    nonexistent-host-zzz9.example.com/a/b        rc=128  fatal: unable to access

The credential prompt DISCRIMINATES.  It is the channel's answer for "no repository I will serve
you", and it is a different string from the channel's answer for "I could not reach the host".
`p292` had the measurement and read it as noise, so three of its four `tokenaii` probes were
thrown away as inconclusive when they were real negatives.

🔴 THE BOUND, WHICH IS WHY THE TOKEN IS NOT `ABSENT`.  The same prompt answers for a repository
that exists and is PRIVATE.  Nothing in this channel separates those two, so the verdict token is
`ABSENT-OR-PRIVATE` and control `C9` forbids a bare `ABSENT` from ever appearing in the token set.
`p292`'s error was reading a discriminating signal as noise; the opposite error — reading it as
proof of non-existence — is the one this bound refuses.

🔴 AND WHY THE ORACLE CALIBRATES ITSELF.  The signature above is a property of THIS session's git
proxy, not of git or of github.com.  A channel that changes its refusal wording would silently
turn every `ABSENT-OR-PRIVATE` into a `CHANNEL-ERROR`, or worse, the reverse.  `--online`
therefore runs the two controls FIRST and refuses to report a single verdict unless the
known-real probe returns refs and the known-fake probe returns the refusal.  An uncalibrated
oracle is exactly the thing that produced `p292`'s row.

Offline, `classify()` is a pure function of (text, returncode) and the suite is its controls.
Standard library only; no network in `hooks`.
"""
import argparse
import os
import re
import subprocess
import sys

# The closed verdict vocabulary.  `NONE-DECLARED` has no analogue here: a probe always lands in
# exactly one of these, and `MALFORMED` is the bucket for "the oracle was handed nothing it can
# read" rather than a statement about the slug.
VERDICTS = (
    "EXISTS-PUBLIC",       # rc=0 and at least one ref line
    "EXISTS-NO-REFS",      # rc=0 and no ref line — an empty repository, which EXISTS
    "ABSENT-OR-PRIVATE",   # the channel's refusal signature; the two are NOT separable here
    "CHANNEL-ERROR",       # host/transport/timeout — genuinely inconclusive, p292's own word
    "MALFORMED",           # empty or unreadable probe output
)

# A ref line is 40 or 64 hex (sha1/sha256 object formats) then a tab then a ref name.
REF_RE = re.compile(r"^[0-9a-f]{40}(?:[0-9a-f]{24})?\t\S", re.M)
SYMREF_RE = re.compile(r"^ref:\s+(\S+)\s+HEAD$", re.M)

# The refusal signature.  Anchored on the two shapes this channel actually emits for a slug it
# will not serve.  `p1057`'s lesson one level out: a one-spelling match has not looked for the
# signature, it has looked for one spelling of it.
ABSENT_RE = re.compile(
    r"fatal:\s+(?:Authentication\s+failed|repository\s+'[^']*'\s+not\s+found"
    r"|could\s+not\s+read\s+Username)",
    re.I,
)
# Transport failures.  These must NOT be read as a statement about the slug.
CHANNEL_RE = re.compile(
    r"fatal:\s+unable\s+to\s+access|Could\s+not\s+resolve\s+host|Connection\s+timed\s+out"
    r"|Operation\s+timed\s+out|SSL\s+certificate\s+problem|proxy\s+CONNECT"
    r"|the\s+requested\s+URL\s+returned\s+error:\s+5\d\d|Too\s+many\s+concurrent",
    re.I,
)

# The calibration pair.  Shipped as data so a future pass can see what the signature was
# calibrated against, and change it in one place when the channel changes.
CONTROL_REAL = "https://github.com/moodle/moodle"
CONTROL_FAKE = "https://github.com/thisorgdoesnotexistzzz9/thisrepo-zzz9"


def classify(text, returncode):
    """Return (verdict, detail).  Pure: no network, no clock, no filesystem.

    `returncode` is load-bearing and not decoration.  Without it an empty answer from a
    reachable-but-empty repository is indistinguishable from a transport failure that printed
    nothing, and the oracle would have to guess between `EXISTS-NO-REFS` and `CHANNEL-ERROR`.
    """
    if text is None:
        return ("MALFORMED", "no probe output")
    body = text.strip()
    if returncode is None:
        return ("MALFORMED", "no returncode: cannot separate an empty repo from a dead channel")
    if returncode == 0:
        refs = len(REF_RE.findall(text))
        if refs:
            sym = SYMREF_RE.search(text)
            where = ", symref %s" % sym.group(1) if sym else ""
            return ("EXISTS-PUBLIC", "%d ref line(s)%s" % (refs, where))
        if not body:
            return ("EXISTS-NO-REFS", "rc=0 with no refs: an empty repository")
        return ("EXISTS-NO-REFS", "rc=0, no ref line parsed; output kept verbatim in evidence")
    # Non-zero.  Transport is checked BEFORE the refusal, because a proxy error can carry the
    # word "authentication" in an unrelated clause and transport is the weaker claim.
    if CHANNEL_RE.search(text):
        return ("CHANNEL-ERROR", "transport/host failure — says nothing about the slug")
    if ABSENT_RE.search(text):
        return ("ABSENT-OR-PRIVATE", "channel refusal signature (absent and private NOT separable)")
    if not body:
        return ("MALFORMED", "rc=%d with no output" % returncode)
    return ("CHANNEL-ERROR", "rc=%d, unrecognised message — NOT read as a negative" % returncode)


def head_sha(text):
    """The HEAD sha from a probe body, or None.  Used to adjudicate two names for one tree."""
    for line in text.splitlines():
        parts = line.split("\t")
        if len(parts) == 2 and parts[1] == "HEAD" and re.fullmatch(r"[0-9a-f]{40,64}", parts[0]):
            return parts[0]
    return None


def probe(url, timeout=45):
    """One `git ls-remote --symref`.  Returns (text, returncode).  ONLINE."""
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0", GIT_ASKPASS="/bin/true",
               GIT_CONFIG_NOSYSTEM="1")
    try:
        p = subprocess.run(["git", "ls-remote", "--symref", url, "HEAD"],
                           capture_output=True, text=True, timeout=timeout, env=env)
        return (p.stdout + p.stderr, p.returncode)
    except subprocess.TimeoutExpired:
        return ("fatal: unable to access '%s': Operation timed out" % url, 128)
    except OSError as exc:
        return ("fatal: unable to access '%s': %s" % (url, exc), 128)


def calibrate(timeout=45):
    """Run the control pair.  Returns (ok, rows).  ONLINE.

    This is the gate on reporting, not a diagnostic.  `p292` trusted an uncalibrated reading of
    this channel and published "inconclusive" over three real negatives.
    """
    rows = []
    real_text, real_rc = probe(CONTROL_REAL, timeout)
    real_v, real_d = classify(real_text, real_rc)
    rows.append(("control-real", CONTROL_REAL, real_v, real_d))
    fake_text, fake_rc = probe(CONTROL_FAKE, timeout)
    fake_v, fake_d = classify(fake_text, fake_rc)
    rows.append(("control-fake", CONTROL_FAKE, fake_v, fake_d))
    ok = real_v == "EXISTS-PUBLIC" and fake_v == "ABSENT-OR-PRIVATE"
    return (ok, rows)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("slugs", nargs="*", help="owner/name, or a full https URL")
    ap.add_argument("--online", action="store_true", help="probe the network (calibrates first)")
    ap.add_argument("--timeout", type=int, default=45)
    ap.add_argument("--out", help="write a TSV here")
    args = ap.parse_args(argv)

    if not args.online:
        print("offline: classify() is importable and the suite is its controls.")
        print("verdict vocabulary: " + " ".join(VERDICTS))
        print("run with --online SLUG... to probe; the control pair gates every verdict.")
        return 0

    ok, rows = calibrate(args.timeout)
    for leg, url, verdict, detail in rows:
        print("%-14s %-62s %-18s %s" % (leg, url, verdict, detail))
    if not ok:
        print("\n🔴 CALIBRATION FAILED — the channel no longer answers as this oracle was built")
        print("   against, so NO verdict is reported.  Re-measure the signature, then update")
        print("   ABSENT_RE / CHANNEL_RE and this suite's fixtures together.")
        return 1
    print("\n🟢 calibrated: known-real returns refs, known-fake returns the refusal signature.\n")

    out = []
    for slug in args.slugs:
        url = slug if slug.startswith("http") else "https://github.com/" + slug
        text, rc = probe(url, args.timeout)
        verdict, detail = classify(text, rc)
        sha = head_sha(text) or "-"
        print("%-18s %-46s %s" % (verdict, slug, sha))
        out.append((slug, url, verdict, sha, detail))

    # Two names, one HEAD, is a FINDING and not a verdict — p283's rule, reused not re-invented.
    by_sha = {}
    for slug, _u, verdict, sha, _d in out:
        if verdict == "EXISTS-PUBLIC" and sha != "-":
            by_sha.setdefault(sha, []).append(slug)
    for sha, slugs in sorted(by_sha.items()):
        if len(slugs) > 1:
            print("\n🟡 HEAD COLLISION at %s: %s" % (sha[:12], ", ".join(slugs)))
            print("   One tree under %d names, or one forked from another TODAY." % len(slugs))
            print("   Adjudicate per p283; do not shelve both as separate rows.")

    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write("# p293 slug-existence oracle — calibrated against the control pair above.\n")
            fh.write("# ABSENT-OR-PRIVATE does NOT mean absent: this channel cannot separate\n")
            fh.write("# a missing repository from a private one.\n")
            fh.write("slug\turl\tverdict\thead_sha\tdetail\n")
            for row in out:
                fh.write("\t".join(row) + "\n")
        print("\nwrote %s" % args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
