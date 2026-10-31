#!/usr/bin/env python3
"""history-plausibility.py — p570, authored in-session (569-B corollary).

WHY THIS EXISTS
---------------
p569 adopted commit count as the admission signal for the TOOLING layer,
because a star floor was discarding this base's best rows (568-C).  The very
first never-swept axis that rule was applied to (topic:rubric, p570) returned
CurveAhoead/ScoreRune: 35 stars, 2,137 commits, history starting 2014-06-10 --
which a commit-count gate admits and which is SYNTHETIC.

A star gate is gamed by buying stars (needs other people).  A commit gate is
gamed with a loop (needs nobody).  Commit count is therefore CHEAPER to forge
than the signal it replaced, and must never be read as a scalar.

THE FOUR CHECKS (all cheap, all local, no API)
  1. RAMP      -- commits/year max:min ratio over active years.  Real histories
                  are bursty (mirt: 8.5x).  A smooth monotonic ramp is a
                  generator artefact (ScoreRune: 1.7x, monotonic 12 years).
  2. ANACHRON  -- Conventional Commits prefixes (feat:/fix:/refactor:/chore:...)
                  dated before 2017.  The convention postdates Angular's ~2016
                  guidelines and the 2017+ Conventional Commits spec.
  3. DIVERGE   -- count of commits where author date != committer date.  A long
                  real history rebases, cherry-picks and merges, so this is
                  NONZERO (mirt: 19/3467).  Exactly 0 across thousands of
                  commits spanning years is a one-pass synthesis tell.
  4. GENESIS   -- the oldest commit's subject.  A repository cannot BEGIN by
                  refactoring.  "refactor:"/"fix:" as commit #1 is a tell.

Reports; does not gate.  Judgement stays with the pass.
"""
import subprocess, sys, collections

CC = ("feat", "fix", "refactor", "chore", "docs", "test", "ci", "perf", "style", "build")

def git(d, *a):
    return subprocess.run(["git", "-C", d, *a], capture_output=True, text=True).stdout

def audit(d, label):
    log = [l for l in git(d, "log", "--format=%as|%cs|%s").splitlines() if "|" in l]
    if not log:
        return {"label": label, "error": "no history"}
    rows = [l.split("|", 2) for l in log]
    years = collections.Counter(r[0][:4] for r in rows)
    active = sorted(v for v in years.values() if v > 0)
    ramp = (active[-1] / active[0]) if active and active[0] else 0.0
    yr_seq = [years[y] for y in sorted(years)]
    interior = yr_seq[:-1] if len(yr_seq) > 2 else yr_seq   # drop partial final year
    monotonic = len(interior) > 4 and all(
        b >= a for a, b in zip(interior, interior[1:]))
    pre17 = [r for r in rows if r[0] < "2017-01-01"]
    anach = sum(1 for r in pre17
                if r[2].split("(")[0].split(":")[0].strip().lower() in CC)
    diverge = sum(1 for r in rows if r[0] != r[1])
    genesis = rows[-1][2][:60]
    authors = len(set(git(d, "log", "--format=%ae").split()))
    span = f"{rows[-1][0]}..{rows[0][0]}"
    flags = []
    if monotonic and ramp < 3.0:
        flags.append("RAMP(monotonic,low-variance)")
    if pre17 and anach / len(pre17) > 0.25:
        flags.append(f"ANACHRON({anach}/{len(pre17)} pre-2017 conv-commits)")
    if diverge == 0 and len(rows) > 500 and len(years) > 3:
        flags.append("DIVERGE(0 across multi-year history)")
    if genesis.split(":")[0].strip().lower() in ("refactor", "fix"):
        flags.append("GENESIS(repo begins by refactoring)")
    return {"label": label, "commits": len(rows), "span": span, "years": len(years),
            "ramp": round(ramp, 2), "monotonic": monotonic, "anach": anach,
            "pre17": len(pre17), "diverge": diverge, "authors": authors,
            "genesis": genesis, "flags": flags}

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print(__doc__); sys.exit(0)
    print("label\tcommits\tspan\tyears\tramp\tmonotonic\tanach/pre17\tdiverge\tauthors\tverdict\tgenesis")
    worst = 0
    for a in args:
        d, _, label = a.partition("=")
        r = audit(d, label or d)
        if "error" in r:
            print(f"{r['label']}\tERROR\t{r['error']}"); continue
        verdict = "IMPLAUSIBLE: " + "; ".join(r["flags"]) if r["flags"] else "plausible"
        worst = max(worst, len(r["flags"]))
        print(f"{r['label']}\t{r['commits']}\t{r['span']}\t{r['years']}\t{r['ramp']}\t"
              f"{r['monotonic']}\t{r['anach']}/{r['pre17']}\t{r['diverge']}\t"
              f"{r['authors']}\t{verdict}\t{r['genesis']}")
    sys.exit(0)
