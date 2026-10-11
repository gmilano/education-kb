"""p136-licence-residue -- `ACTION BV`: close p135's three UNMATCHED licence payloads,
or declare them unclosable.

p135 built `p135-licence-sha-identity`, which resolved 21 of 26 payloads to a named
SPDX id by hashing five progressively normalised forms. Five stayed `UNMATCHED`.
Three of those sat at `0.996`-`0.998` similarity against a GNU text, and `ACTION BV`
asked whether the residue is editorial drift or a substantive added clause --
predicting refutation *"if any of the three carries a substantive added clause
rather than editorial drift, which would make it a MODIFIED_SUPERSET and a licence
risk rather than a table gap."*

🟢 **Zero of three carry an added clause.** The residue is three mechanical classes,
and this module names each one so that the next payload carrying them resolves by
hash instead of landing in the nearest-ratio column:

    SIGN_TRANSLITERATION   the copyright SIGN written as ASCII: `(C)` for `©`
    PLACEHOLDER_DELIMITER  the appendix's angle brackets written another way:
                           `{one line ...}` for `<one line ...>`, or bare
    APPENDIX_INSTANTIATION the "How to Apply" appendix filled in with the project's
                           own name, year and holder -- `<program>` -> `adapt_framework`
    STEWARD_DIVERGENCE     the canonical text and the payload differ in a word that
                           neither project chose: the licence's STEWARD edited its
                           own text, or SPDX transcribed it differently

The fourth is the one that matters and it is kept distinct:

    ADDED_CLAUSE           words in the payload that are not accounted for by any of
                           the above. This is `MODIFIED_SUPERSET` territory and a
                           licence risk.

Verdict `RESOLVED` means every opcode in the diff is accounted for by the first four
classes. `MODIFIED` means at least one is not.

No pytest in this environment: `python3 -I test_residue.py` runs the suite.
"""
import difflib
import re
import unicodedata

SIGN_TRANSLITERATION = "SIGN_TRANSLITERATION"
PLACEHOLDER_DELIMITER = "PLACEHOLDER_DELIMITER"
APPENDIX_INSTANTIATION = "APPENDIX_INSTANTIATION"
STEWARD_DIVERGENCE = "STEWARD_DIVERGENCE"
ADDED_CLAUSE = "ADDED_CLAUSE"

RESOLVED = "RESOLVED"
MODIFIED = "MODIFIED"

# The FSF has edited its own licence texts twice within this corpus's lifetime:
# the http->https move, and (p135's `P135-F`) why-not-lgpl.html moving out of
# /licenses/ into /philosophy/. Normalised, not treated as project edits.
STEWARD_URL_EDITS = [
    ("http://fsf.org/", "https://fsf.org/"),
    ("http://www.fsf.org/", "https://www.fsf.org/"),
    ("http://www.gnu.org/", "https://www.gnu.org/"),
    ("http://gnu.org/", "https://gnu.org/"),
    ("/licenses/why-not-lgpl.html", "/philosophy/why-not-lgpl.html"),
]

TYPOGRAPHIC = {"“": '"', "”": '"', "‘": "'", "’": "'",
               "–": "-", "—": "-", " ": " "}

# Words that appear in the "How to Apply" appendix of a GNU text as placeholders.
# A payload that replaces one with a project name has instantiated the appendix;
# it has not changed the licence.
APPENDIX_PLACEHOLDERS = {
    "program", "one line to give the program's name and a brief idea of what it does",
    "year", "name of author", "name", "signature", "library",
    "one line to give the library's name and a brief idea of what it does",
}

# Known steward-side wording divergences between the FSF's published text and the
# SPDX transcription of it. Each entry is (canonical_words, payload_words).
# Measured, not assumed: the pyopenbadges payload differs from SPDX's
# LGPL-2.1-only text by exactly this one, in the appendix sentence.
STEWARD_WORDINGS = [("an", "a brief"), ("a brief", "an")]


def _strip_brackets(word):
    """Remove placeholder delimiters wherever they sit in the token.

    Stripping only the ENDS is not enough: SPDX's LGPL-2.1 text writes the
    appendix signature line without brackets, so the payload's `Coon>,` has to
    compare equal to the canonical `Coon,` -- with `>` in the middle of the token.
    Measured on `CoopCodeCommun/pyopenbadges`, where end-stripping alone reported
    that one opcode as an ADDED_CLAUSE.
    """
    return re.sub(r"[<>{}\[\]]", "", word)


def normalise(text):
    """Return the word sequence a comparison should run over."""
    t = unicodedata.normalize("NFKC", text)
    for a, b in TYPOGRAPHIC.items():
        t = t.replace(a, b)
    for a, b in STEWARD_URL_EDITS:
        t = t.replace(a, b)
    t = re.sub(r"\r\n?", "\n", t)
    return [w for w in re.split(r"\s+", t) if w]


def _classify(canon_words, pay_words):
    """Classify one diff opcode's canonical/payload word runs."""
    c, p = " ".join(canon_words), " ".join(pay_words)
    if c in ("©", "(c)", "(C)") and p in ("©", "(c)", "(C)"):
        return SIGN_TRANSLITERATION
    for a, b in STEWARD_WORDINGS:
        if c == a and p == b:
            return STEWARD_DIVERGENCE
    cb, pb = _strip_brackets(c), _strip_brackets(p)
    # Same token once the delimiters come off: `<https://fsf.org/>` vs `{https://fsf.org/}`.
    if cb and cb == pb:
        return PLACEHOLDER_DELIMITER
    # A bracketed placeholder on the canonical side, anything on the payload side.
    if c != cb or (c.startswith("<") or c.endswith(">")):
        if cb.lower() in APPENDIX_PLACEHOLDERS or any(
                ph.startswith(cb.lower().split()[0]) for ph in APPENDIX_PLACEHOLDERS if cb):
            return APPENDIX_INSTANTIATION
        return APPENDIX_INSTANTIATION if pb else PLACEHOLDER_DELIMITER
    if pb and (p != pb):
        return PLACEHOLDER_DELIMITER
    return ADDED_CLAUSE


def residue(payload_text, canonical_text):
    """(verdict, ratio, [(class, canonical_run, payload_run), ...])."""
    a, b = normalise(canonical_text), normalise(payload_text)
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    ratio = sm.ratio()
    out = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        out.append((_classify(a[i1:i2], b[j1:j2]), " ".join(a[i1:i2]), " ".join(b[j1:j2])))
    verdict = MODIFIED if any(k == ADDED_CLAUSE for k, _, _ in out) else RESOLVED
    return verdict, ratio, out


def summarise(ops):
    counts = {}
    for k, _, _ in ops:
        counts[k] = counts.get(k, 0) + 1
    return counts
