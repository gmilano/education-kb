#!/usr/bin/env python3
"""`p349-alias-gate` — a STALE ADDRESS ANSWERS 200, so nothing but a register catches it.

What p349 measured: the bounded HEAD-equality run over these shelves returned **21 alias
groups across 43 addresses**, where this base believed it had four — and three of those
groups have BOTH members on the LIVE shelves, one of them (`learner-credential-wallet`)
in four files, identified at p348 and never applied.

🔴 The mechanism, which is why no existing gate sees it: GitHub keeps every former
address of a transferred or renamed repository answering FOREVER, by redirect. A stale
row resolves, clones, and serves raw payloads at the same HEAD as the canonical one. So
`gate-fold-identity` (same address, different casing) is blind to it, `gate-pin-grant`
reads a real grant through it, and a client is told two things exist where one does.

The register is the control. It is a committed, dated TSV — never a judgement at gate
time — because the canonical answer comes from a channel this session may not have on a
later day (see the README: the HTML `301` channel answered `403` on all 43 addresses).

Two findings, both judged over the LIVE pass section only (the `p348-fold-identity`
contract: an append-only shelf cannot be repaired backwards, so the gate binds the text
this pass writes):

    P349-ALIAS-DOUBLE-COUNT   the live section cites two addresses of ONE repository
    P349-STALE-ADDRESS        the live section cites an address the register calls STALE

🟢 Both are discharged the same way and the discharge is cheap: cite the canonical
address, and when a stale one has to be NAMED (a correction has to say what it is
correcting), name it on a line that also carries the canonical address or the token
`STALE`. Naming a stale address as stale is not the defect; publishing it as a row is.

    alias_gate.py <register.tsv> <shelf files...>
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                os.pardir, "p348-fold-identity"))
from fold_identity import slugs_in, split_live_section  # noqa: E402


def read_register(path):
    """folded address -> (group, state, canonical-address-as-published)."""
    reg = {}
    canon = {}
    rows = []
    with open(path, encoding="utf-8") as fh:
        head = fh.readline().rstrip("\n").split("\t")
        for line in fh:
            if not line.strip():
                continue
            r = dict(zip(head, line.rstrip("\n").split("\t")))
            rows.append(r)
            if r["state"] == "CANONICAL":
                canon[r["group"]] = r["address"]
    for r in rows:
        reg[r["address"].lower()] = (r["group"], r["state"], canon.get(r["group"], ""))
    return reg


def gate(register, paths):
    reg = read_register(register)
    findings = []
    for p in paths:
        with open(p, encoding="utf-8") as fh:
            text = fh.read()
        live, _ = split_live_section(text)
        lines = live.splitlines()
        seen = {}
        for s in slugs_in(live):
            hit = reg.get(s.lower())
            if not hit:
                continue
            group, state, canonical = hit
            # the lines this address appears on
            where = [l for l in lines if s.lower() in l.lower()]
            excused = all(
                (canonical and canonical.lower() in l.lower()) or "STALE" in l
                for l in where
            ) if where else False
            if state == "STALE" and not excused:
                findings.append((p, "P349-STALE-ADDRESS", s,
                                 "register: stale address of %s; canonical is %s"
                                 % (group, canonical or "UNRESOLVED")))
            seen.setdefault(group, {})[s.lower()] = excused
        for group, addrs in seen.items():
            if len(addrs) > 1 and not all(addrs.values()):
                findings.append((p, "P349-ALIAS-DOUBLE-COUNT", group,
                                 "one repository published under %d addresses: %s"
                                 % (len(addrs), ", ".join(sorted(addrs)))))
    return findings


def main(argv):
    # P541: a gate that measures the files it is GIVEN must refuse an empty argument list.
    if len(argv) < 2:
        sys.stderr.write("p349-alias-gate: needs <register.tsv> and at least one shelf "
                         "file — refusing (P541)\n")
        return 2
    register, paths = argv[0], argv[1:]
    findings = gate(register, paths)
    print("archivo\thallazgo\tclave\tdetalle")
    for f in findings:
        print("\t".join(f))
    print("#\ttotal\t%d" % len(findings))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
