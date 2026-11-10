#!/usr/bin/env python3
"""Licence gates that canonicalise the TERMS, not the whole file (p732).

Supersedes the line rule for MIT (T272) and whole-file canonicalisation for
Apache-2.0 (T274).

  MIT    -> 1020 B / fe2a9817987f   (18/18 payloads at p732)
  Apache -> 8484 B / c7396247b0c2   ( 5/5  payloads at p732)

Why: the previous MIT rule dropped every line containing the substring
"copyright", which in a stock MIT payload is THREE lines -- the holder
attribution (correct), the attribution obligation (MIT's only condition) and
part of the liability disclaimer. The old 870 B constant was therefore computed
over a text with two binding terms deleted, and was holder-invariant *because*
of that deletion.

The previous Apache rule hashed the APPENDIX, which the licence text itself
places outside the terms; a two-character "[]"->"{}" variation there produced a
same-length, different-hash false refusal of a stock grant.

Usage:  gate_terms.py mit    <payload> [...]
        gate_terms.py apache <payload> [...]
"""
import sys, re, hashlib

MIT_LEN, MIT_SHA = 1020, "fe2a9817987f"
APACHE_LEN, APACHE_SHA = 8484, "c7396247b0c2"

HOLDER = re.compile(
    r'^copyright\s*(\(c\)|\(C\)|©)?\s*'
    r'((?:19|20)\d{2}(?:\s*[-–,]\s*(?:19|20)\d{2})?)\s+(.+?)\s*$', re.I)
BANNED = re.compile(
    r'non[-\s]?commercial|no\s+commercial|academic\s+use\s+only|'
    r'research\s+use\s+only|all\s+rights\s+reserved|not\s+for\s+redistribution', re.I)


def _digest(lines):
    e = re.sub(r'\s+', ' ', ' '.join(lines)).strip().encode('utf-8')
    return len(e), hashlib.sha256(e).hexdigest()[:12]


def mit_gate(path):
    """Channel H + holder-line shape assertion. -> (problems, len, sha12)"""
    t = open(path, 'rb').read().decode('utf-8', 'replace')
    body, holders, problems = [], [], []
    for ln in t.splitlines():
        s = ln.strip()
        if not s:
            continue
        if re.match(r'^(the\s+)?mit\s+license.*$', s, re.I):
            continue
        m = HOLDER.match(s)
        if m:                                  # holder line: drop, but inspect
            holders.append(s)
            if BANNED.search(m.group(3)):
                problems.append(
                    f"holder line carries an extra restriction: {m.group(3)!r}")
            continue
        body.append(s)                         # every term is kept
    n, sha = _digest(body)
    if (n, sha) != (MIT_LEN, MIT_SHA):
        problems.append(
            f"terms differ from stock MIT: {n}B/{sha} != {MIT_LEN}B/{MIT_SHA}")
    if not holders:
        problems.append("no holder-attribution line found")
    return problems, n, sha


def apache_gate(path):
    """Terms-only canonicalisation: truncate at ^APPENDIX:."""
    t = open(path, 'rb').read().decode('utf-8', 'replace')
    m = re.search(r'^\s*APPENDIX:', t, re.M)
    if m:
        t = t[:m.start()]
    body = [ln.strip() for ln in t.splitlines()
            if ln.strip() and 'copyright' not in ln.lower()]
    n, sha = _digest(body)
    problems = []
    if (n, sha) != (APACHE_LEN, APACHE_SHA):
        problems.append(
            f"terms differ from stock Apache-2.0: {n}B/{sha} "
            f"!= {APACHE_LEN}B/{APACHE_SHA}")
    return problems, n, sha


def main(argv):
    if len(argv) < 3 or argv[1] not in ("mit", "apache"):
        print(__doc__)
        return 2
    gate = mit_gate if argv[1] == "mit" else apache_gate
    rc = 0
    for p in argv[2:]:
        probs, n, sha = gate(p)
        print(f"{'PASS' if not probs else 'FLAG'}  "
              f"{p.split('/')[-1]:<44} {n}B/{sha}")
        for x in probs:
            print(f"      -> {x}")
            rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv))
