#!/usr/bin/env python3
"""p370 — re-derive every register row's identity on the ref-set fingerprint.

Reads the committed register plus the verbatim `ls-remote` captures under ./refsets/
(written by probe_refsets.sh) and emits one TSV row per register address:

    group  address  state_p349  refs  fingerprint  head  verdict  register_verdict  reason

No network: the captures are the input, so the derivation is reproducible from the
committed bytes on a day with no egress.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from refset_register import (parse_ls_remote, fingerprint, head_sha, ref_names,
                             classify, register_verdict)

HERE = os.path.dirname(os.path.abspath(__file__))


def capture_path(outdir, addr):
    """The capture for an address, matched CASE-INSENSITIVELY.

    🔴 p370's own first defect: the probe folds case when it de-duplicates the
    address list (GitHub addresses are case-insensitive — `p348`'s rule), so a
    capture is written under ONE spelling while the register may hold another.
    A case-sensitive lookup therefore reported `ONE-SIDE-DEAD` for 10 rows whose
    remotes had every one answered `0`. Folding here is not a convenience; an
    identity instrument that distinguishes addresses GitHub does not would be
    measuring its own filenames.
    """
    exact = os.path.join(outdir, addr.replace("/", "%") + ".refs")
    if os.path.exists(exact):
        return exact
    want = (addr.replace("/", "%") + ".refs").lower()
    try:
        for name in os.listdir(outdir):
            if name.lower() == want:
                return os.path.join(outdir, name)
    except OSError:
        pass
    return exact


def load(outdir, addr):
    p = capture_path(outdir, addr)
    if not os.path.exists(p):
        return {}
    with open(p, encoding="utf-8", errors="replace") as fh:
        return parse_ls_remote(fh.read())


def main(argv):
    if len(argv) < 2:
        sys.stderr.write("rederive.py <register.tsv> <refsets-dir> — refusing (P541)\n")
        return 2
    register, outdir = argv[0], argv[1]
    with open(register, encoding="utf-8") as fh:
        head = fh.readline().rstrip("\n").split("\t")
        rows = [dict(zip(head, l.rstrip("\n").split("\t")))
                for l in fh if l.strip()]

    by_group = {}
    for r in rows:
        by_group.setdefault(r["group"], []).append(r)

    print("\t".join(["group", "address", "state_p349", "refs", "fingerprint",
                     "head", "verdict", "register_verdict", "reason"]))
    counts = {}
    for group in sorted(by_group):
        members = by_group[group]
        canon = next((m for m in members if m["state"] == "CANONICAL"), None)
        ca = load(outdir, canon["address"]) if canon else {}
        for m in members:
            refs = load(outdir, m["address"])
            if canon and m["address"] == canon["address"]:
                verdict = "CANONICAL-SELF"
            else:
                verdict = classify(refs, ca) if canon else "NO-CANONICAL"
            rv, reason = register_verdict(verdict, m["state"])
            counts[(m["state"], verdict, rv)] = counts.get((m["state"], verdict, rv), 0) + 1
            print("\t".join([group, m["address"], m["state"],
                             str(len(ref_names(refs))), fingerprint(refs) or "-",
                             (head_sha(refs) or "-")[:12], verdict, rv, reason]))
    print("#\tsummary")
    for k in sorted(counts):
        print("#\t%s\t%s\t%s\t%d" % (k[0], k[1], k[2], counts[k]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
