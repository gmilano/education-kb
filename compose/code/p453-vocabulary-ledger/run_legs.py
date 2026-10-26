#!/usr/bin/env python3
"""Run vocabulary legs on the npm registry channel and write the spend ledger.

Gap 452-A: the channel is NOT the variable -- the WORD LIST is. These shelves
have exhaustively covered {moodle, canvas, blackboard, brightspace, LMS, SIS} x
{mcp, agent, tutor, server}. Every term below is outside that product.
"""
import json, subprocess, sys, os
import vocab_probe as v

SHELVES = "/tmp/education-kb"

# Vocabulary classes Gap 452-A names as unspent. Recorded so the NEXT pass can
# read what has been spent instead of re-spending it blind.
LEGS = [
    ("pedagogy",          "pedagogy didactic teaching"),
    ("assessment",        "rubric formative assessment grading"),
    ("credentialing",     "open badges verifiable credential"),
    ("special-education", "IEP special education accessibility"),
    ("early-years",       "early years kindergarten literacy"),
    ("vocational",        "vocational apprenticeship training"),
    ("curriculum",        "curriculum standards alignment"),
    ("non-en-es",         "educacion escuela aprendizaje"),
    ("non-en-pt",         "educacao escolar aprendizagem"),
    ("non-en-fr",         "pedagogie scolaire enseignement"),
]


def prior_hits(token):
    """How many non-archive shelf files already mention this token."""
    r = subprocess.run(["grep", "-rli", "--include=*.md", "--", token, SHELVES],
                       capture_output=True, text=True)
    files = [f for f in r.stdout.splitlines() if "/archive/" not in f]
    return len(files)


def main():
    rows, seen = [], set()
    for leg, term in LEGS:
        res, code = v.npm_search(term, size=25)
        if not res:
            rows.append([leg, term, "CHANNEL_FAIL", code, "", "", "", "", "", ""])
            continue
        hits = res.get("objects", [])
        print(f"[{leg}] '{term}' -> {res.get('total')} total, {len(hits)} read",
              file=sys.stderr)
        for o in hits:
            pkg = o["package"]["name"]
            rec = v.npm_record(pkg)
            back, lic = v.backlink_of(rec)
            n = v.norm(back)
            if not n:
                rows.append([leg, term, "NO_BACKLINK", pkg, "", "", lic or "", "", "", ""])
                continue
            kind, forge, owner, repo = n
            if kind != "OK":
                rows.append([leg, term, kind, pkg, f"{forge}/{owner}/{repo}", "",
                             lic or "", "", "", ""])
                continue
            key = f"{forge}/{owner}/{repo}"          # case-folded (Gap 452-F)
            if key in seen:
                continue
            seen.add(key)
            ph = prior_hits(f"{owner}/{repo}")
            # Gap 452-B: the back-link is NOT evidence of reachability. Probe.
            live, how = v.live_probe(forge, owner, repo)
            rows.append([leg, term, "CANDIDATE", pkg, key, live, lic or "",
                         how, str(ph), "ZERO_PRIOR" if ph == 0 else "prior"])
    out = "/tmp/education-kb/evidence/vocabulary-spend-ledger.2026-10-26-p453.tsv"
    with open(out, "w") as f:
        f.write("leg\tterm\tverdict\tpackage\taddress\treachable\tlicence_declared\t"
                "probe_leg\tprior_shelf_files\tnovelty\n")
        for r in rows:
            f.write("\t".join(r) + "\n")
    print(f"\nwrote {len(rows)} rows -> {out}")
    cands = [r for r in rows if r[2] == "CANDIDATE"]
    live = [r for r in cands if r[5] == "LIVE"]
    novel = [r for r in live if r[9] == "ZERO_PRIOR"]
    print(f"candidates={len(cands)} live={len(live)} ZERO-PRIOR-AND-LIVE={len(novel)}")
    for r in novel:
        print("  NOVEL:", r[4], "|", r[6], "|", r[3], "| leg", r[0])


if __name__ == "__main__":
    main()
