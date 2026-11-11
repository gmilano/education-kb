#!/usr/bin/env python3
"""p776 licence grader -- written from scratch.

Three doctrines this base has already paid for, implemented rather than cited:

T729 (p770-C, refined p775): the unit of licence identity is the NORMALISED
     OPERATIVE BODY. Neither byte length nor sha256 tracks the grant -- three
     Apache payloads at exactly 11,357 B have three different hashes, and the
     hash separates payloads that ARE the same licence.

p775's difflib defect: SequenceMatcher's autojunk heuristic fires once the
     second sequence has >= 200 elements and silently drops "popular" tokens,
     which made the comparison ASYMMETRIC and hid an 87% match. Fixed here by
     autojunk=False plus scoring BOTH directions and keeping the max.

ACTION p774-C (standing contract): a deontic guard on every verdict. Inserting
     `never` into the AGPL costs 6 characters, passes any size budget, and
     INVERTS the obligation -- so identity turns on whether an edit touches a
     deontic operator, not on how big the edit is.
"""
import difflib, hashlib, re, sys, json, pathlib

CANON_DIR = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "canonical")

# the copyright slot is a FILL-IN, not part of the grant; canonical texts ship it
# unfilled ("Copyright [yyyy] [name of copyright owner]") and real repos fill it.
COPYRIGHT_LINE = re.compile(
    r"^\s*(copyright|\(c\)|©)\b.*$|^\s*\[?yyyy\]?.*$", re.I | re.M)
# D2 (caught by control): the conventional "All rights reserved." rides with the
# copyright notice and is not part of the grant. Leaving it in made
# Open-TutorAi/open-tutor-ai-CE grade near-canonical (d=3) and would have
# published a FALSE CORRECTION to p775's correct body:canonical verdict.
RIGHTS_RESERVED = re.compile(r"\ball rights reserved\b\.?", re.I)

DEONTIC = {
    "not", "no", "never", "nor", "cannot", "without", "unless", "except",
    "must", "shall", "may", "should", "will", "required", "requires",
    "prohibited", "forbidden", "permitted", "granted", "denied", "subject",
    "provided", "limited", "restricted", "only", "non", "noncommercial",
}


def normalise(b):
    """Normalised operative body: the unit of identity."""
    t = b.decode("utf-8", "replace")
    t = t.replace(" ", " ")
    t = COPYRIGHT_LINE.sub("", t)          # drop the fill-in slot
    t = RIGHTS_RESERVED.sub("", t)         # D2: rides with the notice
    t = re.sub(r"[^a-z0-9]+", " ", t.lower())
    return t.strip()


def words(t):
    return t.split()


def ratio(a, b):
    """Symmetric, autojunk-free. p775's hidden-87%-match defect lives here."""
    wa, wb = words(a), words(b)
    f = difflib.SequenceMatcher(None, wa, wb, autojunk=False).ratio()
    r = difflib.SequenceMatcher(None, wb, wa, autojunk=False).ratio()
    return max(f, r)


def deontic_profile(t):
    ws = words(t)
    return {d: ws.count(d) for d in DEONTIC if ws.count(d)}


# D1 (caught by control): a GLOBAL deontic count is moved by difflib's own
# alignment choices. frappe/erpnext's GPL-3.0 scored ALTERED-DEONTIC on
# `provided` 12-vs-13 -- but both "omitted" clauses are present in BOTH texts
# (the opcodes were alignment artefacts) and the only real difference is a URL
# path segment, `gnu.org/licenses/` for `gnu.org/philosophy/`. Publishing that
# would have been a false "altered licence" claim against a flagship project --
# the THIRD false verdict erpnext has induced on this base in three passes.
# So: restrict to POLARITY/MODAL operators, and measure them only inside the
# regions difflib actually reports as different.
POLARITY = {
    "not", "no", "never", "nor", "cannot", "unless", "except", "without",
    "non", "noncommercial", "prohibited", "forbidden",
    "must", "shall", "may",
}


def deontic_delta(a, b):
    wa, wb = words(a), words(b)
    sm = difflib.SequenceMatcher(None, wa, wb, autojunk=False)
    moved = {}
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        for w in set(wa[i1:i2]) | set(wb[j1:j2]):
            if w in POLARITY:
                ca = wa[i1:i2].count(w)
                cb = wb[j1:j2].count(w)
                if ca != cb:
                    moved[w] = (ca, cb)
    return moved


def load_canon():
    out = {}
    for p in sorted(CANON_DIR.glob("*.txt")):
        out[p.stem] = normalise(p.read_bytes())
    return out


def grade(payload_bytes, canon):
    body = normalise(payload_bytes)
    wc = len(words(body))
    scored = sorted(((ratio(body, c), name) for name, c in canon.items()), reverse=True)
    best_r, best = scored[0]
    dd = deontic_delta(body, canon[best])
    wdelta = abs(wc - len(words(canon[best])))

    if best_r >= 0.9995 and not dd:
        verdict = "body:canonical"
    elif best_r >= 0.97 and not dd:
        verdict = "body:near-canonical"
    elif best_r >= 0.97 and dd:
        verdict = "ALTERED-DEONTIC"          # the guard earns its keep here
    elif best_r >= 0.75:
        verdict = "ALTERED" if not dd else "ALTERED-DEONTIC"
    elif len(words(body)) < 40:
        verdict = "POINTER-OR-SHORT-NOTICE"
    else:
        verdict = "UNRESOLVED"
    return {
        "family": best, "ratio": round(best_r, 4), "verdict": verdict,
        "words": wc, "word_delta": wdelta,
        "deontic_delta": dd,
        "runner_up": [scored[1][1], round(scored[1][0], 4)] if len(scored) > 1 else None,
        "sha256_12": hashlib.sha256(payload_bytes).hexdigest()[:12],
        "bytes": len(payload_bytes),
    }


if __name__ == "__main__":
    canon = load_canon()
    print(f"# canonical texts loaded: {len(canon)}", file=sys.stderr)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        slug, _, path = line.partition("\t")
        data = pathlib.Path(path).read_bytes()
        r = grade(data, canon)
        r["slug"] = slug
        print(json.dumps(r), flush=True)
