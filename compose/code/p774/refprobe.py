#!/usr/bin/env python3
"""p774 ref-channel prober -- written FROM SCRATCH (the repository's own
probe.sh is DENIED in this session as `[Code from External]`).

Every address this pass displays is probed here BEFORE it is shelved, which is
the standing instruction from `ACTION p772-I` and `ACTION p773-I`. The ref
channel (`git ls-remote --symref`) is used rather than `api.github.com`, which
is 403 in this session: it reports existence, the real default branch, and the
HEAD sha without authentication and without a rate limit worth worrying about.

States distinguished (p772's T740 found the last of these and this base had
never recorded it):
  RESOLVES           HEAD advertised
  EXISTS-BUT-EMPTY   authenticates, advertises 0 refs
  ABSENT-OR-PRIVATE  not found / asks for credentials
  TIMEOUT / OTHER
"""
import subprocess, sys, re, os
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, GIT_TERMINAL_PROMPT="0", GIT_ASKPASS="true")

def probe(slug):
    try:
        r = subprocess.run(["git", "ls-remote", "--symref",
                            f"https://github.com/{slug}"],
                           capture_output=True, text=True, timeout=40, env=ENV)
        out = (r.stdout or "") + (r.stderr or "")
    except subprocess.TimeoutExpired:
        return slug, "TIMEOUT", "-", "-", "-"
    refs = re.findall(r"^([0-9a-f]{40})\s+(\S+)$", out, re.M)
    head = [s for s, n in refs if n == "HEAD"]
    sym = re.search(r"^ref:\s+(\S+)\s+HEAD$", out, re.M)
    if head:
        br = sym.group(1).replace("refs/heads/", "") if sym else "HEAD"
        return slug, "RESOLVES", br, head[0][:12], str(len(refs))
    if re.search(r"could not read Username|Authentication failed|not found|"
                 r"Repository not found|does not exist", out, re.I):
        return slug, "ABSENT-OR-PRIVATE", "-", "-", "0"
    if not refs:
        return slug, "EXISTS-BUT-EMPTY", "-", "-", "0"
    return slug, "OTHER", "-", "-", str(len(refs))

def controls():
    """A prober that cannot tell existence from absence is worthless, so both
    arms are asserted before any address is reported."""
    fails = []
    s, st, br, _, _ = probe("moodle/moodle")
    if st != "RESOLVES":
        fails.append(f"K1 a known-live repo must RESOLVE, got {st}")
    s, st, _, _, _ = probe("gmilano/this-repository-does-not-exist-p774")
    if st != "ABSENT-OR-PRIVATE":
        fails.append(f"K2 a known-absent repo must be ABSENT-OR-PRIVATE, got {st}")
    return fails

if __name__ == "__main__":
    f = controls()
    print(f"refprobe CONTROLS: {2-len(f)}/2 pass", file=sys.stderr)
    for x in f:
        print("  FAIL", x, file=sys.stderr)
    if f:
        sys.exit(2)
    slugs = [l.strip() for l in open(sys.argv[1]) if l.strip() and not l.startswith("#")]
    with ThreadPoolExecutor(max_workers=10) as ex:
        for slug, st, br, sha, n in ex.map(probe, slugs):
            print(f"{slug}\t{st}\t{br}\t{sha}\t{n}", flush=True)
