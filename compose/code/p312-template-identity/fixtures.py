#!/usr/bin/env python3
"""p312 — this instrument's pinned payloads, in the form the census DISCOVERS.

🟢 WHY THIS FILE EXISTS, and it is not boilerplate. `p311` repaired
`p310-family-coverage/corpus_families()` so that sibling instruments are
**discovered** rather than named, after that loader's own docstring — *"a
restated list goes stale silently"* — came true within one pass. The contract it
discovers is a sibling directory exporting `DECLARED` as
`(prefix, family, commercial, why)`.

🔴 `p312` first wired itself into that census the OTHER way: by adding a
`_p312_pins()` helper to `family_coverage.py` that named
`p312-template-identity` as a literal path. 🔵 **That is the exact defect `p311`
had just removed from the same function, re-introduced one pass later by the
instrument that benefits from it.** The helper is deleted and this file replaces
it, so the census finds these pins by the same rule it finds every other
instrument's.

🔵 `DECLARED` is DERIVED from the payloads on disk, never typed: the family comes
from each fixture's own name prefix and the canonical answer from
`template_identity.identify()`. A digest or a family spelled by hand here would
be a second source of truth for something the bytes already decide.
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def _ti():
    spec = importlib.util.spec_from_file_location(
        "p312_ti_for_fixtures", os.path.join(HERE, "template_identity.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_T = _ti()
FIX = _T.FIX

# 🔵 Every family pinned here permits commercial use. Copyleft is not
# noncommercial — `P250`'s two columns are separate questions, and reciprocity is
# an obligation on distribution, not a bar on selling. `GPL-2.0` and `MPL-2.0`
# are therefore `OK` on this axis and carry their obligation in the shelf cell.
_COMMERCIAL = {
    "MIT": "OK",
    "Apache-2.0": "OK",
    "BSD-2-Clause": "OK",
    "MPL-2.0": "OK",
    "GPL-2.0": "OK",
}

_WHY = {
    "MIT": "The most-published family on this base and never run through a "
           "dynamic arm before `ACTION p310-R` item 1. Nine payloads from nine "
           "unrelated repositories across three topic axes: eight share ONE "
           "normalised template digest at `bytes - len(declaration) = 1 038`, "
           "the ninth is a second template at `1 047`. The published byte band "
           "`1 062`-`1 074` is refuted at both ends and is UNCLOSABLE, because "
           "the length is `constant(template) + len(holder)`.",
    "Apache-2.0": "The second most-published family. A FIXED DOCUMENT with no "
                  "holder slot, bimodal by SECTION: the `10 173` B payload is a "
                  "STRICT BYTE PREFIX of the `11 357` B one, delta exactly "
                  "`1 184` B — the `APPENDIX: How to apply` block. Both modes "
                  "are holder-blind for DIFFERENT reasons (`NO-DECLARATION` vs "
                  "`PLACEHOLDER-DECLARATION`).",
    "BSD-2-Clause": "A fill-in form whose title line reads `BSD 2-Clause "
                    "License`, shelved by `p310` as a bare `BSD` — a spelling "
                    "the family grammar had no bucket for at all. 🔴 Also the "
                    "family where the classifiers are weakest: 4 of 9 abstain.",
    "MPL-2.0": "Pinned from `SafeExamBrowser/seb-win-refactoring`, which "
               "narrows `p310`'s proctoring nil. 🔴 `p311` found `p153` read "
               "EVERY `MPL-2.0` payload as `GPL-3.0`; this is a second, "
               "independent payload for that repaired rung.",
    "GPL-2.0": "Three payloads from three unrelated education repositories — "
               "`15 214`, `18 092`, `18 097` B — and 🔴 NO ONE of them is a byte "
               "prefix of another. The appendix relation that holds for "
               "Apache-2.0 and GPL-3.0 FAILS here, because the FSF boilerplate "
               "address differs before the appendix is reached. Kept as the "
               "measured boundary of `P312-T`.",
}


def _build():
    out, seen = [], set()
    for name in _T.fixture_names():
        fam = _T._family_of(name)
        if fam in seen or fam == "UNKNOWN":
            continue
        seen.add(fam)
        out.append((_T.stem_of(name), fam, _COMMERCIAL.get(fam, "OK"),
                    _WHY.get(fam, "")))
    return sorted(out, key=lambda r: r[1])


DECLARED = _build()


def declared():
    """[(name, family, commercial, why, text, bytes, sha12)] for each pin."""
    rows = []
    for name, fam, com, why in DECLARED:
        text, n, sha = _T.load(name)
        rows.append((name, fam, com, why, text, n, sha))
    return rows


if __name__ == "__main__":
    for name, fam, com, _why, _text, n, sha in declared():
        print("%-46s %-14s %-5s %7d B  %s" % (name, fam, com, n, sha))
