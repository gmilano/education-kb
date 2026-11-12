#!/usr/bin/env python3
"""p779 instrument: operative-word diff between two licence prints.

Tokenises each file to lowercase word tokens (runs of [a-z0-9] after folding
every other character to a separator), diffs the token streams, and reports
(a) the token-level delta, (b) which deontic operators appear in the changed
runs, and (c) whether the whole delta is accounted for by a NAMED trailing
appendix section. A deontic operator is what makes a licence term operative:
if none differ, the two prints grant and forbid the same things.
"""
import re, sys, difflib

DEONTIC = {"must","shall","may","cannot","can","will","required","require","requires",
           "permitted","permit","permits","prohibited","prohibit","forbidden",
           "grant","grants","granted","not","no","nor","except","unless","provided",
           "subject","condition","conditions","liable","liability","warranty","warranties"}

def toks(p):
    b = open(p, "rb").read()
    t = b.decode("utf-8", "replace").lower()
    return [w for w in re.split(r"[^a-z0-9]+", t) if w]

def main(a, b, appendix_marker=None):
    ta, tb = toks(a), toks(b)
    print(f"A {a}\n  {len(open(a,'rb').read())} B  {len(ta)} word tokens")
    print(f"B {b}\n  {len(open(b,'rb').read())} B  {len(tb)} word tokens")
    sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    only_a, only_b, ops = [], [], []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        ra, rb = ta[i1:i2], tb[j1:j2]
        only_a += ra; only_b += rb
        ops.append((tag, i1, i2, j1, j2, ra, rb))
    print(f"\nmatching ratio (token level): {sm.ratio():.6f}")
    print(f"changed runs: {len(ops)}   tokens only in A: {len(only_a)}   only in B: {len(only_b)}")
    for tag, i1, i2, j1, j2, ra, rb in ops:
        print(f"\n--- {tag}  A[{i1}:{i2}] ({len(ra)} tok)  B[{j1}:{j2}] ({len(rb)} tok)")
        if ra: print("    only in A: " + " ".join(ra[:80]) + (" …" if len(ra) > 80 else ""))
        if rb: print("    only in B: " + " ".join(rb[:80]) + (" …" if len(rb) > 80 else ""))
    da = sorted(set(only_a) & DEONTIC); db = sorted(set(only_b) & DEONTIC)
    print(f"\nDEONTIC operators present in A-only tokens: {da if da else 'NONE'}")
    print(f"DEONTIC operators present in B-only tokens: {db if db else 'NONE'}")
    if appendix_marker:
        m = appendix_marker.lower().split()
        def tail_at(t):
            for k in range(len(t) - len(m), -1, -1):
                if t[k:k+len(m)] == m: return k
            return None
        ka, kb = tail_at(ta), tail_at(tb)
        print(f"\nappendix marker {m!r}: A at token {ka}, B at token {kb}")
        if ka is not None or kb is not None:
            ca = ta[:ka] if ka is not None else ta
            cb = tb[:kb] if kb is not None else tb
            print(f"  operative bodies (marker stripped): A {len(ca)} tok, B {len(cb)} tok")
            print(f"  OPERATIVE BODIES IDENTICAL: {ca == cb}")
            if ca != cb:
                s2 = difflib.SequenceMatcher(None, ca, cb, autojunk=False)
                oa=[]; ob=[]
                for tag,i1,i2,j1,j2 in s2.get_opcodes():
                    if tag!="equal": oa+=ca[i1:i2]; ob+=cb[j1:j2]
                print(f"  residual A-only: {' '.join(oa[:60])}")
                print(f"  residual B-only: {' '.join(ob[:60])}")
                print(f"  residual deontic A: {sorted(set(oa)&DEONTIC) or 'NONE'}")
                print(f"  residual deontic B: {sorted(set(ob)&DEONTIC) or 'NONE'}")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
