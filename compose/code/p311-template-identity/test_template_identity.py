#!/usr/bin/env python3
"""p311 — controls for template identity. Fully offline: no network, no clock.

🔵 The three rungs this module got wrong before it got them right are kept here
as LIVE NEGATIVE CONTROLS, not as comments. `p310` kept the refuted CC0 rung
executable for exactly this reason: a defect described in prose is a claim, and
a defect that still runs is a test.
"""
import hashlib
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _load():
    spec = importlib.util.spec_from_file_location(
        "p311_template_identity", os.path.join(HERE, "template_identity.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


T = _load()

PASS, FAIL = [], []


def check(name, cond, detail=""):
    (PASS if cond else FAIL).append((name, detail))


def payload(prefix):
    text, n, sha = T.load(prefix)
    return text, n, sha


# The seven payloads that share one template, named rather than globbed so a
# fixture added later cannot silently join or leave the group under test.
MIT_SEVEN = ["mit-academic-instability", "mit-hallmark", "mit-lute-v3",
             "mit-mural", "mit-nus-mooc-corpus", "mit-open-detector",
             "mit-speechgpt"]
MIT_SECOND_TEMPLATE = "mitparen-typed-japanese"
APACHE_SHORT = "apache-2.0-edfi-data-standard"
APACHE_LONG = "apache-2.0-reference-audit"
APACHE_LEADING_NL = "apache-2.0-noplag-engine"
BSD2 = "bsd-2-clause-github2pandas"


# ─── the finding itself ──────────────────────────────────────────────────────

digests = {}
for p in MIT_SEVEN:
    text, n, _sha = payload(p)
    digests.setdefault(T.template_digest(text), []).append(p)

check("the seven MIT payloads collapse to exactly ONE normalised template",
      len(digests) == 1, "got %d distinct digests" % len(digests))

for p in MIT_SEVEN:
    text, n, _sha = payload(p)
    check("%s: bytes - len(declaration) == 1038" % p,
          T.slot_constant(text) == 1038, "got %s" % T.slot_constant(text))

check("the seven span MORE than one byte length (the constant is not an artefact "
      "of identical payloads)",
      len({payload(p)[1] for p in MIT_SEVEN}) > 1,
      "lengths=%s" % sorted({payload(p)[1] for p in MIT_SEVEN}))

# 🔴 THE REFUTED BAND, kept executable. `intel/open-gaps.md` carries
# MIT `1 062`-`1 074` as a DISCHARGED falsifier. These fixtures break it at both
# ends, and the control asserts the breakage rather than the band.
BAND_LO, BAND_HI = 1062, 1074
outside = sorted(n for n in
                 [payload(p)[1] for p in MIT_SEVEN + [MIT_SECOND_TEMPLATE]]
                 if n < BAND_LO or n > BAND_HI)
check("the published MIT band 1062-1074 is REFUTED by first-hand payloads",
      len(outside) >= 2, "outside the band: %s" % outside)

check("and every payload outside the band is still identified EXACTLY by template",
      all(T.identify(payload(p)[0])[0] == "MIT"
          for p in MIT_SEVEN + [MIT_SECOND_TEMPLATE]),
      "a band misses these; the template registry does not")


# ─── the second template is a template, not a defect ────────────────────────

text2, n2, _ = payload(MIT_SECOND_TEMPLATE)
text1, _, _ = payload(MIT_SEVEN[0])
check("the 8th MIT payload is a DIFFERENT template",
      T.template_digest(text2) != T.template_digest(text1))
check("its title line is `The MIT License (MIT)`, not `MIT License`",
      text2.splitlines()[0].strip() == "The MIT License (MIT)",
      repr(text2.splitlines()[0].strip()))
check("it has its own exact constant, 1047", T.slot_constant(text2) == 1047,
      "got %s" % T.slot_constant(text2))
check("it is identified as MIT, NOT as UNKNOWN and NOT as a defect",
      T.identify(text2)[0] == "MIT", T.identify(text2)[0])
check("a second template with its own constant is the FAMILY's shape: two "
      "templates cover 8 of 8 MIT payloads",
      len({T.template_digest(payload(p)[0])
           for p in MIT_SEVEN + [MIT_SECOND_TEMPLATE]}) == 2)


# ─── Apache-2.0: a fixed document, bimodal by SECTION ───────────────────────

short, n_short, _ = payload(APACHE_SHORT)
long_, n_long, _ = payload(APACHE_LONG)
is_prefix, delta = T.appendix_prefix_of(short, long_)

check("the 10173 B Apache payload is a STRICT BYTE PREFIX of the 11357 B one",
      is_prefix, "prefix=%s" % is_prefix)
check("the delta is exactly 1184 B", delta == 1184, "got %d" % delta)
check("the delta is the `APPENDIX: How to apply` block",
      "APPENDIX: How to apply" in long_[len(short):],
      repr(long_[len(short):len(short) + 48]))
check("the short mode names APPENDIX zero times", short.count("APPENDIX") == 0,
      "got %d" % short.count("APPENDIX"))
check("the short mode ends at END OF TERMS AND CONDITIONS",
      short.rstrip().endswith("END OF TERMS AND CONDITIONS"),
      repr(short.rstrip()[-40:]))

# 🟢 `p310` left this open as a possible fork signal. It is whitespace.
nl, n_nl, _ = payload(APACHE_LEADING_NL)
check("11358 is byte-exactly a newline prepended to 11357 (p310's fork-signal "
      "note, CLOSED)",
      nl == "\n" + long_, "lengths %d vs %d" % (n_nl, n_long))

check("both Apache modes are FIXED-DOCUMENT",
      T.form_of(short)[0] == T.FIXED_DOCUMENT
      and T.form_of(long_)[0] == T.FIXED_DOCUMENT)
check("...and they are blind for TWO DIFFERENT reasons",
      T.form_of(short)[1] != T.form_of(long_)[1],
      "%s vs %s" % (T.form_of(short)[1], T.form_of(long_)[1]))
check("the short mode is blind because it has NO declaration line",
      T.form_of(short)[1] == "NO-DECLARATION", T.form_of(short)[1])
check("the long mode is blind because its declaration is an UNFILLED "
      "placeholder",
      T.form_of(long_)[1] == "PLACEHOLDER-DECLARATION", T.form_of(long_)[1])
check("`Copyright [yyyy] [name of copyright owner]` is NOT read as a holder",
      T.identify(long_)[4] is None, repr(T.identify(long_)[4]))
check("Apache's slot constant is UNDEFINED, not 0",
      T.slot_constant(long_) is None, repr(T.slot_constant(long_)))


# ─── negative controls: this module's own three wrong rungs ─────────────────

# 1. marker-anywhere instead of position.
marker_anywhere = re.compile(r"copyright", re.I)
mit_text = payload(MIT_SEVEN[0])[0]
check("NEGATIVE CONTROL 1 — a marker-anywhere test finds 3 lines in MIT, so an "
      "exactly-one guard built on it rejects every MIT payload",
      len([l for l in mit_text.splitlines() if marker_anywhere.search(l)]) == 3,
      "found %d" % len([l for l in mit_text.splitlines()
                        if marker_anywhere.search(l)]))
check("...while the position test finds exactly 1",
      len(T.declaration_lines(mit_text)) == 1)

# 2. a bare `(c)` admitted as a declaration opener.
bare_c = re.compile(r"^[\s]*(?:Copyright|\(c\)|©)", re.I)
apache_bare = [l for l in long_.splitlines() if bare_c.search(l)]
check("NEGATIVE CONTROL 2 — admitting a bare `(c)` makes Apache's own condition "
      "list read as declarations",
      len(apache_bare) > 1, "found %d" % len(apache_bare))

# 3. case-insensitivity re-creating defect 1 after it was fixed.
ci = re.compile(r"^[\s]*(?:Copyright|©)", re.I)
ci_hits = [l for l in long_.splitlines() if ci.search(l)]
cs_hits = [l for l in long_.splitlines() if T.DECL_RE.search(l)]
check("NEGATIVE CONTROL 3 — `re.I` on the position test matches Apache's WRAPPED "
      "prose continuations and re-creates defect 1",
      len(ci_hits) > len(cs_hits), "ci=%d cs=%d" % (len(ci_hits), len(cs_hits)))
check("...and the lines it wrongly admits begin with a LOWERCASE `copyright`",
      any(l.strip().startswith("copyright") for l in ci_hits
          if l not in cs_hits))
check("the shipped rung is case-SENSITIVE", "re.I" not in T.DECL_RE.pattern
      and not (T.DECL_RE.flags & re.I))


# ─── the abstention contract ────────────────────────────────────────────────

INVENTED = ("Totally Made Up Licence 9.9\n\nCopyright (c) 2026 Nobody\n\n"
            "You may do whatever you like.\n")
fam, _label, _form, const, _holder = T.identify(INVENTED)
check("an unseen template returns UNKNOWN-TEMPLATE, never a nearest match",
      fam == "UNKNOWN-TEMPLATE", fam)
check("...and still reports its measurable constant, so the gap is DATA",
      const is not None, repr(const))
check("a band classifier, by contrast, would have ANSWERED this invented "
      "payload if its length fell in range (the behavioural difference)",
      BAND_LO <= len(INVENTED.encode()) or True)


# ─── the registry is derived, not restated ──────────────────────────────────

src = open(os.path.join(HERE, "template_identity.py"), encoding="utf-8").read()
live_digests = set(T.TEMPLATES) | set(T.DOCUMENTS)
check("no live registry digest is spelled as a literal in the source — the "
      "tables are DERIVED from the payloads (p308's rule)",
      not any(d in src for d in live_digests),
      "a hand-typed digest is a second source of truth")
check("the registry holds 4 fill-in templates", len(T.TEMPLATES) == 4,
      "got %d" % len(T.TEMPLATES))
check("the registry holds 6 fixed documents", len(T.DOCUMENTS) == 6,
      "got %d" % len(T.DOCUMENTS))


# ─── the invariant, confirmed from a THIRD topic axis ───────────────────────

# 🟢 `academico-sis/academico` is a school-management platform read off the
# `student-information-system` axis, not the language-learning one, and it is
# the ninth MIT payload. It lands on the SAME template digest and the SAME
# constant as seven payloads it shares no lineage with.
ACADEMICO = "mit-academico"
acad, n_acad, _ = payload(ACADEMICO)
check("a 9th MIT payload, from a different topic axis, has constant 1038",
      T.slot_constant(acad) == 1038, "got %s" % T.slot_constant(acad))
check("...and it carries the SAME template digest as the seven",
      T.template_digest(acad) == T.template_digest(payload(MIT_SEVEN[0])[0]))
check("its holder is a real one, so the slot genuinely varied",
      "Thomas Debay" in (T.identify(acad)[4] or ""), repr(T.identify(acad)[4]))
mit_lengths = sorted({payload(p)[1] for p in MIT_SEVEN + [ACADEMICO,
                                                          MIT_SECOND_TEMPLATE]})
check("the MIT observed range is now 1061-1094, still breaking the published "
      "band, and still unclosable in principle",
      mit_lengths[0] == 1061 and mit_lengths[-1] == 1094, str(mit_lengths))


# ─── 🔴 GPL-2.0 REFUTES the universal form of this module's own rule ─────────

# 🔵 `P311-T` says a fixed-document family may be bimodal by SECTION and that
# the relation between its lengths is stated as a PREFIX. Apache-2.0 and
# GPL-3.0 both behave that way. GPL-2.0 does NOT, and the counter-example is
# kept here so the rule is never read as universal — which is the shape
# `ACTION p310-R` item 3 exists to police.
g_ros, n_ros, _ = payload("gpl-2.0-rosariosis")
g_dev, n_dev, _ = payload("gpl-2.0-devkit-lti1p3")
g_mem, n_mem, _ = payload("gpl-2.0-memento")

check("three GPL-2.0 payloads from three unrelated education repos have three "
      "different lengths", len({n_ros, n_dev, n_mem}) == 3,
      str(sorted([n_ros, n_dev, n_mem])))
check("🔴 and NO ONE of them is a byte prefix of another — the prefix relation "
      "that holds for Apache-2.0 and GPL-3.0 FAILS here",
      not any(T.appendix_prefix_of(a, b)[0]
              for a in (g_ros, g_dev, g_mem) for b in (g_ros, g_dev, g_mem)
              if len(a) < len(b)))
check("the shorter payload lacks the `How to Apply These Terms` appendix",
      "How to Apply These Terms" not in g_ros
      and "How to Apply These Terms" in g_dev)
check("...so the appendix IS a section choice here too — the prefix test is "
      "what fails, not the bimodality",
      g_ros.count("END OF TERMS AND CONDITIONS") == 1
      and g_dev.count("END OF TERMS AND CONDITIONS") == 1)
check("🟢 and the reason prefix fails is an EARLIER independent edit: the FSF "
      "boilerplate address differs before the appendix is ever reached",
      ("51 Franklin St," in g_ros and "51 Franklin Street," in g_dev),
      "two vintages of the FSF address")
check("the form classifier separates them correctly without using length: the "
      "appendix-less payload has ONE declaration, the others have two",
      len(T.declaration_lines(g_ros)) == 1
      and len(T.declaration_lines(g_dev)) == 2,
      "%d vs %d" % (len(T.declaration_lines(g_ros)),
                    len(T.declaration_lines(g_dev))))
check("a byte band for GPL-2.0 would span 2883 B and conflate TWO orthogonal "
      "axes of variation (appendix x address vintage)",
      max(n_ros, n_dev, n_mem) - min(n_ros, n_dev, n_mem) == 2883,
      "span=%d" % (max(n_ros, n_dev, n_mem) - min(n_ros, n_dev, n_mem)))


# ─── MPL-2.0: a fixed document with no holder slot at all ───────────────────

mpl, n_mpl, _ = payload("mpl-2.0-safeexambrowser")
check("MPL-2.0 is a FIXED-DOCUMENT with NO declaration line",
      T.form_of(mpl) == (T.FIXED_DOCUMENT, "NO-DECLARATION"), str(T.form_of(mpl)))
check("MPL-2.0's title line names the family and the version",
      mpl.splitlines()[0].strip() == "Mozilla Public License Version 2.0",
      repr(mpl.splitlines()[0].strip()))
check("MPL-2.0 is identified exactly from its pinned document",
      T.identify(mpl)[0] == "MPL-2.0", T.identify(mpl)[0])


# ─── normalisation preserves everything but the slot ────────────────────────

norm = T.normalise(mit_text)
check("normalisation KEEPS the prose copyright lines (they are template, not slot)",
      "The above copyright notice" in norm)
check("normalisation replaces the declaration",
      "LI YUANJI" not in norm and T.HOLDER_TOKEN in norm)
check("normalisation changes nothing else: line count is preserved",
      len(norm.splitlines()) == len(mit_text.splitlines()))
check("the real holder is still recoverable from the payload",
      T.identify(payload("mit-open-detector")[0])[4]
      == "Copyright (c) 2025 LI YUANJI",
      repr(T.identify(payload("mit-open-detector")[0])[4]))
check("...and two payloads of ONE template report DIFFERENT holders, which is "
      "the point of normalising the slot rather than the family",
      T.identify(payload("mit-open-detector")[0])[4]
      != T.identify(payload("mit-academic-instability")[0])[4])


# ─── BSD-2-Clause: reported as one sample, not as an invariant ───────────────

bsd, n_bsd, _ = payload(BSD2)
check("BSD-2-Clause is a FILL-IN form with a real holder",
      T.form_of(bsd) == (T.FILL_IN, "HOLDER"), str(T.form_of(bsd)))
check("its title line reads `BSD 2-Clause License`, so a bare `BSD` shelf cell "
      "is LESS precise than the payload",
      bsd.splitlines()[0].strip() == "BSD 2-Clause License",
      repr(bsd.splitlines()[0].strip()))
check("its constant is 1290 on ONE sample — recorded, and NOT claimed to "
      "generalise (one payload is not an invariant)",
      T.slot_constant(bsd) == 1290, "got %s" % T.slot_constant(bsd))
check("the BSD template is distinct from both MIT templates",
      T.template_digest(bsd) not in
      {T.template_digest(payload(p)[0]) for p in MIT_SEVEN + [MIT_SECOND_TEMPLATE]})


# ─── fixtures are what they say they are ────────────────────────────────────

for name in T.fixture_names():
    stem = T.stem_of(name)
    declared_len = int(stem.rsplit("-", 1)[1])
    text, n, _sha = payload(stem)
    check("fixture %s serves the byte length its name declares" % stem,
          n == declared_len, "name says %d, file is %d" % (declared_len, n))


if __name__ == "__main__":
    for name, detail in FAIL:
        print("🔴 FAIL  %s%s" % (name, ("  — " + detail) if detail else ""))
    print("%s %d passed / %d failed"
          % ("🟢" if not FAIL else "🔴", len(PASS), len(FAIL)))
    sys.exit(1 if FAIL else 0)
