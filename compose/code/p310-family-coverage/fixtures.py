#!/usr/bin/env python3
"""p310 — the pinned payloads this pass added, and the CANONICAL answer for each.

🔵 Every fixture is a real file from a real repository, read first-hand at p310
over `raw.githubusercontent.com`, with its byte length and `sha256_12` in its own
filename.  That is this base's standing evidence format and it is what makes a
fixture re-checkable rather than a claim.

🔴 WHY THESE FOUR.  `p309` built the dynamic arm — the right mechanism — and gave
it FOUR payloads covering THREE families (`GPL-3.0` twice, `AGPL-3.0`, and a
`CC-BY-SA-4.0` POINTER of 1 230 B that carries no legalcode body at all).  It then
reported `11/11 CORRECT` and `DEFECT=0`.  Both statements are true and the second
one is worth nothing outside those three families: at `p310` the same ladder,
FIVE LINES BELOW the rung `p309` repaired, graded a real `CC-BY-NC-4.0` payload as
`CC0-1.0`.

🔵 So the lesson `p309` could not reach from inside its own corpus: **a dynamic
gate is only as strong as the FAMILIES in its fixture set, and the families it
needs are not a matter of taste — they are the ones this base PUBLISHES.**
`family_coverage.py` derives that set from the shelves and reports the uncovered
remainder as exposure with a denominator.

The `commercial` field exists because of `P250`, which this base settled 60 passes
ago: *familia de licencia y uso comercial son dos preguntas y se contestan en dos
columnas.*  🔴 `p306-licence-probe` has one column, so for the three noncommercial
payloads below its verdict cannot express the only fact a studio needs.
"""
import hashlib
import os

HERE = os.path.dirname(os.path.abspath(__file__))
FIX = os.path.join(HERE, "fixtures")

# 🔵 The handle is a PREFIX and the file is resolved by listing the directory —
# `p309-affero-rung-census/fixtures.py`'s convention, adopted rather than
# reinvented. 🔴 It also matters mechanically: spelling `...LICENSE` as a literal
# in this file makes `p283-ladder-case-audit` read it as a one-rung licence-path
# ladder and the STANDING ratchet goes red, because the audit cannot tell a
# fixture's filename from a remote path a prober will probe. Naming the pin and
# globbing for the file says what is meant and costs nothing.

# 🔵 (filename, canonical family, canonical commercial-use verdict, why it is here).
# The family is what the payload's OWN TITLE LINE says, which is the channel
# `p124-correction-form-marker/cc_version.py` was built on and the channel
# `p150`/`p198` settled for the GNU families.  Nothing here is inferred from a
# body scan, because a body scan is the defect under test.
DECLARED = [
    ("ccbync-4.0-aegis-graph", "CC-BY-NC-4.0", "PROHIBITED",
     "aclascollege/aegis-graph — title line `Attribution-NonCommercial 4.0 "
     "International`. 🔴 The payload names `CC0` exactly ONCE, in the "
     "`Considerations for licensors` boilerplate, and that single mention is "
     "enough to carry a whole-body ladder to `CC0-1.0` — a NonCommercial grant "
     "reported as a public-domain dedication."),
    ("ccby-4.0-writing-support", "CC-BY-4.0", "OK",
     "Amey-Thakur/WRITING-SUPPORT — title line `Attribution 4.0 International`. "
     "Same single `CC0` mention, same wrong verdict, lower cost: CC-BY is "
     "permissive, but it carries an attribution condition that `CC0-1.0` does "
     "not, and this base's own shelf cell calls CC0 *more permissive than MIT*."),
    ("polyform-nc-1.0.0-paper-tutor-skills", "PolyForm-Noncommercial-1.0.0",
     "PROHIBITED",
     "cabbage2000-lab/paper-tutor-skills — a REAL grant (`## Copyright License`, "
     "`## Acceptance`) that no clause in `p306`'s `GRANT_CLAUSES` matches, so the "
     "verdict is `NO-GRANT-CLAUSE`. 🔵 A false NEGATIVE on the grant axis and a "
     "silent one on the commercial axis, on the fastest-growing form factor in "
     "this domain (agent SKILLS, `p309`'s finding)."),
    ("cc0-1.0-gen-mentor", "CC0-1.0", "OK",
     "GeminiLight/gen-mentor — the CC0 1.0 LEGALCODE, 7 048 B, the exact file all "
     "SEVEN CC0 rows on this base serve. 🔴 It is here because the coverage census "
     "listed `CC0-1.0` among the 15 unexercised families and the first run against "
     "a real payload found a SECOND false negative: `p306`'s CC0 grant clause was "
     "`has waived all copyright`, which is the DEED SUMMARY's wording and appears "
     "ZERO times in the legalcode. 🔵 A clause list written against a document the "
     "prober never fetches is the same error as a rung asserted and never run."),
    ("proprietary-algomind", "proprietary", "PROHIBITED",
     "SiddharthGarkoti/algomind — *«published for reference, portfolio "
     "evaluation, and demonstration purposes only»*. 🟢 The one row of the four "
     "`p306` grades CORRECTLY (`RESERVED-NO-GRANT`), and it is in the set as a "
     "POSITIVE control: a gate whose corpus contains no row the instrument gets "
     "right cannot distinguish a broken classifier from a broken gate."),
]


def resolve(prefix):
    """The one file in `fixtures/` whose name starts with `prefix`."""
    hits = sorted(n for n in os.listdir(FIX) if n.startswith(prefix))
    if len(hits) != 1:
        raise LookupError("%s resolves to %d files, expected 1" % (prefix, len(hits)))
    return os.path.join(FIX, hits[0])


def load(prefix):
    """Return (text, bytes_len, sha256_12) for a pinned fixture."""
    with open(resolve(prefix), "rb") as fh:
        raw = fh.read()
    return raw.decode("utf-8", "replace"), len(raw), hashlib.sha256(raw).hexdigest()[:12]


def declared():
    """[(name, family, commercial, why, text, bytes, sha12)] for every fixture."""
    out = []
    for name, fam, com, why in DECLARED:
        text, n, sha = load(name)
        out.append((name, fam, com, why, text, n, sha))
    return out


# 🔵 p309's corpus, IMPORTED rather than restated — this pass's whole subject.
def p309_fixtures():
    """p309's four payloads, or None if that instrument is not reachable."""
    import importlib.util
    path = os.path.normpath(os.path.join(HERE, "..", "p309-affero-rung-census",
                                         "fixtures.py"))
    if not os.path.exists(path):
        return None
    spec = importlib.util.spec_from_file_location("p309_fixtures", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


if __name__ == "__main__":
    for name, fam, com, _why, _text, n, sha in declared():
        print("%-48s %-30s %-11s %7d B  %s" % (name, fam, com, n, sha))
