"""p886 — the p228 shelf gate, with p886's title/token/rider rows layered on.
Prints: family<TAB>rider_flag
"""
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import grant_titles_x as X  # noqa: E402

spec = importlib.util.spec_from_file_location(
    "cg", os.path.join(HERE, "..", "p228-shelf-gate", "classify_grant.py"))
cg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cg)


def classify_full(body):
    """p228 first; p886's rows only decide when p228 abstains or is OUT-POSITIONED.

    The earliest-title rule is global, so a p886 title that sits EARLIER than
    p228's match wins -- otherwise a Portuguese AGPL body whose English appendix
    mentions the GNU title later would resolve on the appendix.
    """
    bare = X.bare_token_grant(body)
    if bare:
        return bare[0], ""
    fam, _chan, _note = cg.classify(body)
    p228_at = None
    if fam:
        for f, rx in cg._COMPILED:
            m = rx.search(body)
            if m and (p228_at is None or m.start() < p228_at):
                p228_at = m.start()
    best = None
    for f, pat in X.TITLES_X:
        m = re.search(pat, body, re.I)
        if m and (best is None or m.start() < best[1]):
            best = (f, m.start())
    if best and (p228_at is None or best[1] < p228_at):
        fam = best[0]
        if fam in ("GPL", "LGPL"):
            if X.VER3_X.search(body):
                fam = "GPL-3.0" if fam == "GPL" else "LGPL-3.0"
            elif X.VER2_X.search(body):
                fam = "GPL-2.0"
            elif X.VER21_X.search(body):
                fam = "LGPL-2.1"
            else:
                fam = fam + "-?"
    rider = "RIDER" if X.additional_terms_rider(body) else ""
    return (fam or "UNRECOGNISED"), rider


if __name__ == "__main__":
    with open(sys.argv[1], encoding="utf-8", errors="replace") as fh:
        f, r = classify_full(fh.read())
    print("%s\t%s" % (f, r))
